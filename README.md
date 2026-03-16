---
title: Magent AI Research Assistant
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.28.0
app_file: infrastructure/huggingface/app.py
pinned: true
license: mit
---

# Magent – Student Research Assistant

Multi-agent RAG assistant built with LangChain, LangGraph, Streamlit, ChromaDB, and Ollama. Students can upload documents, ask research questions, and get cited answers from a supervisor/researcher/writer/critic agent team.

## 🚀 Quick start
- Install deps: `python3 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"` (Ollama + models required: `ollama pull llama3.2`).
- Seed sample docs: `python scripts/seed_data.py` then ingest with `python -m research_assistant.cli ingest --dir data/documents`.
- Ask via CLI: `python -m research_assistant.cli query "What is machine learning?" --show-sources`.
- Run UI: `streamlit run src/research_assistant/ui/app.py`.
- Tests/quality: `pytest tests/ -v` and optional `pre-commit run --all-files`.

## 🎯 Features
- **Multi-agent system**: Supervisor, Researcher, Writer, Critic agents
- **RAG-powered**: Retrieval-augmented generation with ChromaDB
- **Document analysis**: PDF, TXT, MD support
- **Cited responses**: Source attribution for every answer
- **Beautiful UI**: Modern dark theme with professional design

## 🌐 Deployments
- **Render**: https://magent-kchc.onrender.com
- **Local**: `docker run -p 8501:8501 student-research-assistant:latest`

## 🤖 AI Models
- **LLM**: Llama 3.2 (via Ollama)
- **Embeddings**: Sentence Transformers
- **Vector Store**: ChromaDB

## Branches
- `main` – Stable
- `gk_poc` – GK POC
- `sv_poc` – SV POC (current)
- `dev` – Shared development
# Render Deployment Fix - Sun Mar 15 18:12:35 EDT 2026
