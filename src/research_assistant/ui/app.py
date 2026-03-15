"""Main Streamlit application."""

import streamlit as st
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

_health_server_started = False


class _HealthHandler(BaseHTTPRequestHandler):
    """Simple /healthz endpoint for k8s probes."""

    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()


def start_health_server(port: int = 8500):
    """Start a lightweight health server on a separate thread."""
    global _health_server_started
    if _health_server_started:
        return

    def _serve():
        server = HTTPServer(("0.0.0.0", port), _HealthHandler)
        server.serve_forever()

    thread = threading.Thread(target=_serve, daemon=True)
    thread.start()
    _health_server_started = True

from research_assistant.ui.components import render_header, render_sidebar, render_document_upload
from research_assistant.graph import run_research
from research_assistant.services import get_llm_service


def main():
    """Main application entry point."""
    render_header()
    settings = render_sidebar()

    # Start lightweight health endpoint for probes
    start_health_server()

    # Check LLM availability
    llm = get_llm_service()
    ollama_available = llm.is_available()
    
    # Beautiful status indicator
    if ollama_available:
        st.markdown("""
        <div style="
            background: linear-gradient(90deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(16, 185, 129, 0.2);
        ">
            <h3 style="margin: 0; display: flex; align-items: center; justify-content: center;">
                <span>🤖 AI System Online</span>
                <span style="
                    background: rgba(255,255,255,0.2);
                    padding: 0.2rem 0.5rem;
                    border-radius: 20px;
                    font-size: 0.8rem;
                    margin-left: 1rem;
                ">Ready for Research</span>
            </h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(245, 158, 11, 0.2);
        ">
            <h3 style="margin: 0; display: flex; align-items: center; justify-content: center;">
                <span>⚠️ AI System Initializing</span>
                <span style="
                    background: rgba(255,255,255,0.2);
                    padding: 0.2rem 0.5rem;
                    border-radius: 20px;
                    font-size: 0.8rem;
                    margin-left: 1rem;
                ">Models Downloading</span>
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="
            background: #fef3c7;
            border: 1px solid #fbbf24;
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 2rem;
        ">
            <h4 style="margin: 0 0 0.5rem 0; color: #92400e;">💡 Quick Start Guide</h4>
            <ol style="color: #78350f; line-height: 1.6;">
                <li><strong>Upload Documents:</strong> Add research papers below</li>
                <li><strong>Wait for AI:</strong> Models are downloading (2-3 minutes)</li>
                <li><strong>Start Research:</strong> Ask questions when ready</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Document upload section
    st.markdown("---")
    render_document_upload()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat section header
    st.markdown("---")
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #6366f1;
    ">
        <h3 style="margin: 0; color: #1f2937; display: flex; align-items: center;">
            💬 Research Chat
            <span style="
                background: #6366f1;
                color: white;
                padding: 0.2rem 0.5rem;
                border-radius: 15px;
                font-size: 0.75rem;
                margin-left: 1rem;
            ">AI-Powered</span>
        </h3>
        <p style="margin: 0.5rem 0 0 0; color: #4b5563; font-size: 0.9rem;">
            Ask questions about your uploaded documents and get intelligent, cited responses
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Display chat history
    for msg in st.session_state.messages:
        render_chat_message(msg["role"], msg["content"], msg.get("sources"))

    # Beautiful chat input
    if prompt := st.chat_input("🔍 Ask anything about your documents...", key="chat_input"):
        if not ollama_available:
            st.markdown("""
            <div style="
                background: #fee2e2;
                border: 1px solid #fca5a5;
                border-radius: 8px;
                padding: 1rem;
                margin-bottom: 1rem;
            ">
                <h4 style="margin: 0; color: #dc2626;">⏳ Please Wait</h4>
                <p style="margin: 0; color: #ea580c;">
                    AI models are still downloading. This usually takes 2-3 minutes on first deployment.
                    The interface will be ready automatically.
                </p>
            </div>
            """, unsafe_allow_html=True)
            return
            
        st.session_state.messages.append({"role": "user", "content": prompt})
        render_chat_message("user", prompt)

        # Generate response
        render_chat_message("assistant", "", None)  # Start assistant message
        
        with st.spinner("🤖 AI Agents Working..."):
            # Show agent status
            status_container = st.container()
            with status_container:
                st.markdown("""
                <div style="
                    background: #f0f9ff;
                    border: 1px solid #3b82f6;
                    border-radius: 8px;
                    padding: 1rem;
                    margin-bottom: 1rem;
                ">
                    <h5 style="margin: 0; color: #1e40af;">🔄 Multi-Agent Workflow Active</h5>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; margin-top: 0.5rem;">
                        <div style="text-align: center; padding: 0.5rem; background: white; border-radius: 6px;">
                            <div style="font-size: 1.5rem;">👨‍💼</div>
                            <div style="font-size: 0.8rem; color: #374151;">Supervisor</div>
                        </div>
                        <div style="text-align: center; padding: 0.5rem; background: white; border-radius: 6px;">
                            <div style="font-size: 1.5rem;">🔍</div>
                            <div style="font-size: 0.8rem; color: #374151;">Researcher</div>
                        </div>
                        <div style="text-align: center; padding: 0.5rem; background: white; border-radius: 6px;">
                            <div style="font-size: 1.5rem;">✍️</div>
                            <div style="font-size: 0.8rem; color: #374151;">Writer</div>
                        </div>
                        <div style="text-align: center; padding: 0.5rem; background: white; border-radius: 6px;">
                            <div style="font-size: 1.5rem;">🔬</div>
                            <div style="font-size: 0.8rem; color: #374151;">Critic</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                result = run_research(prompt)
                
                # Clear status and show result
                status_container.empty()
                
                st.markdown(result["response"])

                if result.get("sources"):
                    st.markdown("""
                    <div style="
                        background: #f0fdf4;
                        border: 1px solid #10b981;
                        border-radius: 8px;
                        padding: 1rem;
                        margin-top: 1rem;
                    ">
                        <h4 style="margin: 0 0 0.5rem 0; color: #065f46; display: flex; align-items: center;">
                            📚 Research Sources
                            <span style="
                                background: #10b981;
                                color: white;
                                padding: 0.2rem 0.5rem;
                                border-radius: 12px;
                                font-size: 0.75rem;
                                margin-left: 1rem;
                            ">{len(result.get('sources', []))} sources found</span>
                        </h4>
                    </div>
                    """, unsafe_allow_html=True)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result["response"],
                "sources": [s.get("source") for s in result.get("sources", [])],
            }
        )


if __name__ == "__main__":
    main()
