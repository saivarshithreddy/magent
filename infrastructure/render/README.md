# Render Deployment Guide

## Architecture Overview

This deployment uses **3 separate services** on Render:

1. **magent-app** (Web Service) - Main Streamlit application
2. **magent-chroma** (Private Service) - ChromaDB vector database
3. **magent-ollama** (Private Service) - Ollama LLM service

## Deployment Steps

### 1. Push to GitHub

```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### 2. Deploy on Render

#### Option A: Using Render Dashboard
1. Go to [render.com](https://render.com)
2. Connect your GitHub repository
3. Click "New +" → "Web Service"
4. Select your repository
5. Use the `render.yaml` configuration file
6. Deploy all 3 services

#### Option B: Using Render CLI
```bash
# Install Render CLI
npm install -g @render/cli

# Deploy
render deploy
```

### 3. Service URLs After Deployment

- **Main App**: https://magent-app.onrender.com
- **ChromaDB**: https://magent-chroma.onrender.com (Private)
- **Ollama**: https://magent-ollama.onrender.com (Private)

### 4. Environment Variables

The services will automatically connect using these URLs:
- `RESEARCH_OLLAMA_BASE_URL`: https://magent-ollama.onrender.com
- `RESEARCH_CHROMA_HOST`: magent-chroma.onrender.com

## Cost Breakdown

- **Web Service**: $7/month (Standard plan)
- **ChromaDB**: $7/month (Standard plan)
- **Ollama**: $7/month (Standard plan)
- **Total**: ~$21/month

## Monitoring

All services include health checks:
- Web Service: `/_stcore/health`
- ChromaDB: `/api/v1/heartbeat`
- Ollama: `/api/tags`

## Troubleshooting

### Common Issues

1. **Service Connection Errors**
   - Check service URLs in Render dashboard
   - Verify environment variables
   - Check service health status

2. **Model Download Issues**
   - Ollama service may take 5-10 minutes to download models
   - Check Ollama service logs

3. **Memory Issues**
   - Consider upgrading to Standard+ plan for better performance
   - Monitor resource usage in Render dashboard

### Logs Access

Access logs via Render dashboard:
1. Go to your service
2. Click "Logs" tab
3. Filter by time range

## Scaling

- **Web Service**: Can scale horizontally
- **Database Services**: Vertical scaling only
- Consider load balancer for high traffic
