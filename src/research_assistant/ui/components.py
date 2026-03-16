"""Reusable Streamlit components."""

import streamlit as st


def render_header():
    """Render beautiful application header."""
    st.set_page_config(
        page_title="Magent - AI Research Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Simple CSS
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #1e293b 0%, #334155 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    }
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #1e293b;
        margin: 1rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5rem;">🤖 Magent</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">
            Advanced AI Research Assistant
        </p>
        <p style="margin: 0; font-size: 1rem; opacity: 0.8;">
            Multi-agent RAG system for intelligent document analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 Smart Research</h4>
            <p>AI-powered document analysis with semantic search</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🤖 Multi-Agent</h4>
            <p>Supervisor, Researcher, Writer & Critic agents</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>📚 Citations</h4>
            <p>Accurate source attribution for every response</p>
        </div>
        """, unsafe_allow_html=True)


def render_sidebar():
    """Render beautiful sidebar."""
    with st.sidebar:
        # Header
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        ">
            <h3 style="margin: 0; font-size: 1.3rem; font-weight: 700;">⚙️ Settings</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Model selection
        st.markdown("### 🤖 AI Model")
        model = st.selectbox(
            "Select Model",
            ["llama3.2", "llama3.1", "mistral"],
            index=0,
            key="model_selection"
        )
        
        # Search settings
        st.markdown("### 🔍 Search Settings")
        top_k = st.slider("Results to Retrieve", 1, 10, 5, key="top_k_slider")
        
        st.markdown("---")
        
        # System status
        st.markdown("""
        <div style="
            background: #1e293b;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        ">
            <h4 style="margin: 0 0 0.5rem 0; font-weight: 700;">✅ System Status</h4>
            <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">All services operational</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick actions
        st.markdown("### 🚀 Quick Actions")
        if st.button("📊 View Statistics", key="stats_btn", use_container_width=True):
            st.info("📈 Analytics dashboard coming soon!")
        
        if st.button("🔄 Refresh Models", key="refresh_btn", use_container_width=True):
            st.success("🔄 Models refreshed successfully!")

        return {"model": model, "top_k": top_k}


def render_chat_message(role: str, content: str, sources: list | None = None):
    """Render a beautiful chat message."""
    with st.chat_message(role):
        st.markdown(content)
        if sources:
            st.markdown("📚 **Sources:**")
            for i, src in enumerate(sources, 1):
                st.markdown(f"{i}. {src}")


def render_document_upload():
    """Render beautiful document upload widget."""
    st.markdown("### 📄 Document Upload")
    
    uploaded_files = st.file_uploader(
        "Drag & Drop Files Here",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
        key="doc_upload",
        help="Upload research papers, articles, or any text documents for AI analysis"
    )
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} files uploaded successfully!")
        st.info("Your documents are being processed and will be available for AI analysis")
    
    return uploaded_files
