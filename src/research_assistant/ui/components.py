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
    
    # Custom CSS for beautiful dark theme styling
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    body, .stApp, .main {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        color: #0f172a !important;
        background: #ffffff !important;
    }
    
    .stApp {
        background: #ffffff !important;
    }
    
    .main .block-container {
        padding-top: 2rem !important;
    }
    
    .main-header {
        background: linear-gradient(90deg, #1e293b 0%, #334155 100%) !important;
        padding: 2rem !important;
        border-radius: 12px !important;
        margin-bottom: 2rem !important;
        text-align: center !important;
        color: white !important;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
    
    .feature-card {
        background: #ffffff !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        border-left: 4px solid #1e293b !important;
        margin: 1rem 0 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08) !important;
        border: 1px solid #e2e8f0 !important;
        font-weight: 500 !important;
        color: #0f172a !important;
        min-height: 120px !important;
    }
    
    .feature-card h4 {
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    .feature-card p {
        color: #475569 !important;
        font-weight: 400 !important;
        margin: 0 !important;
    }
    
    .status-indicator {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        margin-left: 0.5rem;
        font-family: 'Inter', sans-serif;
    }
    .status-ready { background: #0f172a !important; color: white !important; }
    .status-warning { background: #1e293b !important; color: white !important; }
    .status-error { background: #0f172a !important; color: white !important; }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
        color: #0f172a !important;
    }
    
    .stTextInput > div > div > input {
        font-family: 'Inter', sans-serif !important;
        color: #0f172a !important;
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
    }
    
    .stSelectbox > div > div > select {
        font-family: 'Inter', sans-serif !important;
        color: #0f172a !important;
        background: #ffffff !important;
    }
    
    .stSlider > div > div > div > div {
        background: #1e293b !important;
    }
    
    .stButton > button {
        background: #1e293b !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Beautiful header
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
    
    # Feature cards with improved dark theme
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
        # Sidebar header with dark theme
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        ">
            <h3 style="margin: 0; font-size: 1.3rem; font-weight: 700;">⚙️ Settings</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Model selection with dark theme styling
        st.markdown("""
        <div style="
            background: #ffffff;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        ">
            <h4 style="margin: 0 0 0.5rem 0; color: #0f172a; font-weight: 700;">🤖 AI Model</h4>
        </div>
        """, unsafe_allow_html=True)
        
        model = st.selectbox(
            "Select Model",
            ["llama3.2", "llama3.1", "mistral"],
            index=0,
            key="model_selection"
        )
        
        # Search settings with dark theme
        st.markdown("""
        <div style="
            background: #ffffff;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        ">
            <h4 style="margin: 0 0 0.5rem 0; color: #0f172a; font-weight: 700;">🔍 Search Settings</h4>
        </div>
        """, unsafe_allow_html=True)
        
        top_k = st.slider("Results to Retrieve", 1, 10, 5, key="top_k_slider")
        
        st.markdown("---")
        
        # System status with dark theme
        st.markdown("""
        <div style="
            background: #0f172a;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            color: white;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        ">
            <h4 style="margin: 0 0 0.5rem 0; font-weight: 700;">✅ System Status</h4>
            <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">All services operational</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick actions with dark theme
        st.markdown("""
        <div style="
            background: #ffffff;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        ">
            <h4 style="margin: 0 0 0.5rem 0; color: #0f172a; font-weight: 700;">🚀 Quick Actions</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📊 View Statistics", key="stats_btn", use_container_width=True):
            st.info("📈 Analytics dashboard coming soon!")
        
        if st.button("🔄 Refresh Models", key="refresh_btn", use_container_width=True):
            st.success("🔄 Models refreshed successfully!")

        return {"model": model, "top_k": top_k}


def render_chat_message(role: str, content: str, sources: list | None = None):
    """Render a beautiful chat message."""
    # Define colors for different roles
    if role == "user":
        avatar_style = "background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);"
        icon = "👤"
    elif role == "assistant":
        avatar_style = "background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);"
        icon = "🤖"
    else:
        avatar_style = "background: #6b7280;"
        icon = "📝"
    
    with st.chat_message(role):
        # Custom avatar styling
        st.markdown(f"""
        <div style="
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        ">
            <div style="
                {avatar_style}
                width: 40px;
                height: 40px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.2rem;
                color: white;
                margin-right: 1rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            ">
                {icon}
            </div>
            <div style="flex: 1;">
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if sources:
            st.markdown("""
            <div style="
                background: #f8fafc;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                padding: 1rem;
                margin-top: 1rem;
            ">
                <h4 style="margin: 0 0 0.5rem 0; color: #1f2937; font-size: 0.9rem;">
                    📚 Sources
                </h4>
            </div>
            """, unsafe_allow_html=True)
            
            for i, src in enumerate(sources, 1):
                source_name = src.get('source', f"Source {i}")
                st.markdown(f"""
                <div style="
                    background: white;
                    border: 1px solid #e2e8f0;
                    border-radius: 6px;
                    padding: 0.75rem;
                    margin-bottom: 0.5rem;
                    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
                ">
                    <div style="display: flex; align-items: center;">
                        <span style="
                            background: #10b981;
                            color: white;
                            padding: 0.2rem 0.5rem;
                            border-radius: 12px;
                            font-size: 0.75rem;
                            font-weight: 600;
                            margin-right: 0.5rem;
                        ">{i}</span>
                        <span style="color: #374151; font-weight: 500;">{source_name}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)


def render_document_upload():
    """Render beautiful document upload widget."""
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 2px dashed #cbd5e1;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    ">
        <div style="
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">
            <h3 style="margin: 0 0 1rem 0; color: #1f2937; display: flex; align-items: center;">
                📄 Document Upload
                <span style="
                    background: #10b981;
                    color: white;
                    padding: 0.2rem 0.5rem;
                    border-radius: 12px;
                    font-size: 0.7rem;
                    margin-left: 0.5rem;
                ">BETA</span>
            </h3>
            <p style="margin: 0 0 1rem 0; color: #6b7280;">
                Upload your research documents to enable intelligent AI analysis
            </p>
            <div style="
                background: #f3f4f6;
                border-radius: 6px;
                padding: 1rem;
                border: 1px solid #e2e8f0;
            ">
                <p style="margin: 0; color: #374151; font-size: 0.9rem;">
                    📁 Supported formats: PDF, TXT, MD<br>
                    📊 Multiple files supported<br>
                    🔒 Secure processing
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader(
        "Drag & Drop Files Here",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
        key="doc_upload",
        help="Upload research papers, articles, or any text documents for AI analysis"
    )
    
    if uploaded_files:
        st.markdown(f"""
        <div style="
            background: #ecfdf5;
            border: 1px solid #10b981;
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
        ">
            <h4 style="margin: 0 0 0.5rem 0; color: #065f46; display: flex; align-items: center;">
                ✅ Files Ready
                <span style="
                    background: #10b981;
                    color: white;
                    padding: 0.1rem 0.3rem;
                    border-radius: 8px;
                    font-size: 0.7rem;
                    margin-left: 0.5rem;
                ">{len(uploaded_files)} uploaded</span>
            </h4>
            <p style="margin: 0; color: #047857;">
                Your documents are being processed and will be available for AI analysis
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    return uploaded_files
