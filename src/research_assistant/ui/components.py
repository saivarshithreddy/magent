"""Reusable Streamlit components."""

import streamlit as st


def render_header():
    """Render lightweight application header for free tier."""
    st.set_page_config(
        page_title="Magent - AI Research Assistant",
        page_icon="🤖",
        layout="centered",  # Changed from wide to save memory
        initial_sidebar_state="auto",  # Changed to auto for faster load
    )
    
    # Minimal CSS for free tier performance
    st.markdown("""
    <style>
    .main-header {
        background: #1e293b;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        text-align: center;
        color: white;
    }
    .feature-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 3px solid #1e293b;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Lightweight header
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2rem;">🤖 Magent</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1rem;">
            AI Research Assistant - Free Tier
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Simplified feature cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 Research</h4>
            <p>Document analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🤖 AI Agents</h4>
            <p>Multi-agent system</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>📚 Sources</h4>
            <p>Cited responses</p>
        </div>
        """, unsafe_allow_html=True)


def render_sidebar():
    """Render lightweight sidebar for free tier."""
    with st.sidebar:
        # Simple header
        st.markdown("""
        <div style="
            background: #1e293b;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            text-align: center;
            color: white;
        ">
            <h3 style="margin: 0; font-size: 1.1rem;">⚙️ Settings</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Simple model selection
        st.markdown("### 🤖 Model")
        model = st.selectbox(
            "Choose Model",
            ["llama3.2", "llama3.1", "mistral"],
            index=0,
            key="model_selection"
        )
        
        # Simple search settings
        st.markdown("### 🔍 Search")
        top_k = st.slider("Results", 1, 10, 5, key="top_k_slider")
        
        # Status
        st.markdown("### 📊 Status")
        st.markdown("""
        <div style="
            background: #f0f9ff;
            padding: 0.5rem;
            border-radius: 6px;
            border-left: 3px solid #1e293b;
        ">
            <p style="margin: 0; font-size: 0.9rem;">✅ Free Tier Active</p>
        </div>
        """, unsafe_allow_html=True)

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
    """Render lightweight document upload for free tier."""
    st.markdown("### 📄 Upload Documents")
    
    uploaded_files = st.file_uploader(
        "Choose files",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
        key="doc_upload",
        help="Upload research papers for AI analysis"
    )
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} files ready")
        st.info("Processing on free tier - may take longer")
    
    return uploaded_files
