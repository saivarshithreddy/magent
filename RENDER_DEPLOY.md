# Render Deployment Instructions

## 🚀 Quick Deploy to Render

### **Step 1: Go to Render**
1. Visit [render.com](https://render.com)
2. Sign up/login

### **Step 2: Create Web Service**
1. Click **"New +" → "Web Service"**
2. **Connect Repository**: Select `saivarshithreddy/magent`
3. **Name**: `magent-app`
4. **Runtime**: **Docker**
5. **Root Directory**: Leave empty
6. **Dockerfile Path**: `Dockerfile`
7. **Plan**: Standard ($7/month)

### **Step 3: Environment Variables**
Copy these from `.env.example`:
```
RESEARCH_OLLAMA_BASE_URL=https://magent-ollama.onrender.com
RESEARCH_OLLAMA_MODEL=llama3.2
RESEARCH_CHROMA_HOST=magent-chroma.onrender.com
RESEARCH_CHROMA_PORT=8000
RESEARCH_LOG_LEVEL=INFO
RESEARCH_ENVIRONMENT=render
```

### **Step 4: Deploy**
Click **"Create Web Service"** - Render will build and deploy!

## 🔧 Alternative: Multi-Service

Use `.render.yaml` for full 3-service deployment:
- Web Service + ChromaDB + Ollama
- Total cost: ~$21/month

## ✅ After Deployment

Your app will be live at: `https://magent-app.onrender.com`

## 📋 Current Status

- ✅ Dockerfile exists in root
- ✅ Requirements.txt ready
- ✅ Environment variables configured
- ✅ Latest commit pushed: `5c84d7c`
- ✅ Ready for Render deployment
