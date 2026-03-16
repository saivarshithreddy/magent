"""Streamlit application for Magent AI Research Assistant."""

import streamlit as st
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from research_assistant.ui.components import render_header, render_sidebar, render_document_upload
from research_assistant.graph import run_research
from research_assistant.services import get_llm_service


def main():
    """Main application entry point."""
    render_header()
    settings = render_sidebar()

    # Check LLM availability
    llm = get_llm_service()
    ollama_available = llm.is_available()
    
    # Status indicator
    if ollama_available:
        st.markdown("""
        <div style="
            background: linear-gradient(90deg, #1e293b 0%, #334155 100%);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        ">
            <h3 style="margin: 0; font-weight: 700;">
                🤖 AI System Online - Ready for Research
            </h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background: linear-gradient(90deg, #334155 0%, #475569 100%);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        ">
            <h3 style="margin: 0; font-weight: 700;">
                ⚠️ AI System Initializing - Models Downloading
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
        border-radius: 12px;
        margin-bottom: 1rem;
        border-left: 4px solid #1e293b;
    ">
        <h3 style="margin: 0; color: #1e293b; font-weight: 700;">
            💬 Research Chat
            <span style="
                background: #1e293b;
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
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                st.markdown("📚 **Sources:**")
                for src in msg["sources"]:
                    st.markdown(f"• {src}")

    # Chat input
    if prompt := st.chat_input("🔍 Ask anything about your documents..."):
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
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("🤖 AI Agents Working..."):
                result = run_research(prompt)
                st.markdown(result["response"])

                if result.get("sources"):
                    st.markdown("📚 **Research Sources:**")
                    for src in result.get("sources"):
                        st.markdown(f"• {src.get('source', 'Unknown')}")

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": result["response"],
                "sources": [s.get("source") for s in result.get("sources", [])],
            }
        )


if __name__ == "__main__":
    main()
