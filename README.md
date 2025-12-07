# 📚 Educational Video Generator - Complete Guide

An **AI-powered application** that automatically generates professional educational videos from text content.

**Version:** 2.0.0 | **Status:** Production Ready ✅ | **Updated:** December 7, 2025

---

## 🎯 Project Overview

```
Input Content (PDF, DOCX, TXT)
        ↓
   AI Analysis
        ↓
   Script Generation
        ↓
   Visual Planning
        ↓
   Audio Generation
        ↓
   Video Composition
        ↓
Output: Professional Video (MP4)
```

**Supports:** Classes 1-12, Diploma, Engineering, Medical, and all educational fields

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────┐
│              FRONTEND (React + TypeScript)              │
│           Running on http://localhost:5173             │
│                                                         │
│  - React Pages (Home, Dashboard, Create, Editor)       │
│  - Redux State Management                              │
│  - Tailwind CSS Styling                                │
│  - Real-time WebSocket Updates                         │
└──────────────────┬──────────────────────────────────────┘
                   │ HTTP/REST API
                   ↓
┌─────────────────────────────────────────────────────────┐
│         BACKEND (FastAPI + Python + LangGraph)         │
│           Running on http://localhost:8000             │
│                                                         │
│  ┌────────────────────────────────────────────────┐   │
│  │        LangGraph Agent Orchestrator            │   │
│  │                                                │   │
│  │  1. Content Analyzer     → Extract & Analyze  │   │
│  │  2. Script Generator     → Create Narration   │   │
│  │  3. Visual Planner       → Plan Visuals      │   │
│  │  4. Diagram Generator    → Generate Images   │   │
│  │  5. Video Composer       → Create MP4        │   │
│  └────────────────────────────────────────────────┘   │
│                                                         │
│  Celery Task Queue (Background Jobs)                   │
└──────────────────┬──────────────────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    ↓              ↓              ↓
┌─────────┐  ┌─────────┐  ┌──────────────┐
│ SQLite  │  │  Redis  │  │ Azure Cloud  │
│Database │  │ Cache   │  │ - OpenAI     │
│         │  │         │  │ - Speech     │
│         │  │         │  │ - Storage    │
└─────────┘  └─────────┘  └──────────────┘
```

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Node.js v18+ & npm
- Python 3.9+

### Step 1: Frontend
```powershell
cd frontend
npm install
npm run dev
```
**Opens:** http://localhost:5173

### Step 2: Backend
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
**Opens:** http://localhost:8000

### Step 3: Done! 🎉
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 📂 Folder Structure

```
edu-video-generator/
├── frontend/              ← React TypeScript App
│   ├── src/
│   │   ├── pages/        ← Home, Dashboard, Create, Editor
│   │   ├── components/   ← Reusable UI components
│   │   ├── services/     ← API clients
│   │   ├── hooks/        ← Custom hooks
│   │   ├── store/        ← Redux state
│   │   └── types/        ← TypeScript types
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── backend/               ← FastAPI Python App
│   ├── app/
│   │   ├── main.py       ← Entry point
│   │   ├── agents/       ← LangGraph agents (5 agents)
│   │   ├── api/          ← API endpoints
│   │   ├── services/     ← Business logic
│   │   ├── models/       ← Database models
│   │   ├── schemas/      ← Validators
│   │   ├── core/         ← Celery, Security
│   │   └── utils/        ← Helpers
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml    ← Multi-container setup
├── README.md            ← This file (Project overview)
├── FRONTEND.md          ← Frontend documentation
└── BACKEND.md           ← Backend documentation
```

---

## 🔧 Complete Setup Instructions

### Backend Setup

```powershell
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
copy .env.example .env
# Edit .env with your Azure credentials

# Run server
uvicorn app.main:app --reload
```

**Or with Celery (for background tasks):**
```powershell
# Terminal 1: API Server
uvicorn app.main:app --reload

# Terminal 2: Celery Worker
celery -A app.core.celery_app worker --loglevel=info

# Terminal 3: Redis (if local)
redis-server
```

### Frontend Setup

```powershell
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

---

## ✨ Key Features

✅ **Multi-Format Input:** PDF, DOCX, TXT files  
✅ **AI-Powered Analysis:** Extract concepts, assess difficulty  
✅ **Automatic Script Generation:** Create narration  
✅ **Visual Planning:** Generate diagrams & images  
✅ **Speech Synthesis:** Professional narration (10+ languages)  
✅ **Video Composition:** Create MP4 videos  
✅ **Real-Time Progress:** WebSocket updates  
✅ **Video Customization:** Voice, language, quality, subtitles  
✅ **Multi-User Support:** Authentication & projects  
✅ **Cloud Integration:** Azure OpenAI, Storage, Speech  

---

## 📊 Video Generation Workflow

```
1. User uploads content
            ↓
2. System extracts & analyzes text
            ↓
3. AI generates video structure
            ↓
4. Creates script with narration
            ↓
5. Plans visual elements
            ↓
6. Generates diagrams & images
            ↓
7. Synthesizes speech audio
            ↓
8. Composes final MP4 video
            ↓
9. Uploads to cloud storage
            ↓
10. User downloads/streams video
```

---

## 🔗 API Endpoints Overview

### Content Management
```
POST   /api/v1/content/upload           - Upload content
GET    /api/v1/content/projects         - List projects
GET    /api/v1/content/projects/{id}    - Get project
```

### Video Generation
```
POST   /api/v1/video/generate/{id}      - Start generation
GET    /api/v1/video/{id}               - Get video
GET    /api/v1/status/task/{taskId}     - Check progress
```

**Full API Documentation:** http://localhost:8000/docs

---

## 🔐 Environment Variables

### Backend `.env`
```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_SPEECH_KEY=your-key
AZURE_SPEECH_REGION=eastus
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./edu_video.db
```

### Frontend `.env.local`
```bash
VITE_API_BASE_URL=http://localhost:8000
```

---

## 🐳 Docker Setup

```powershell
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## 📚 Documentation

**For detailed information, see:**

1. **`FRONTEND.md`** - React components, services, hooks, state management
2. **`BACKEND.md`** - FastAPI endpoints, LangGraph agents, services, database
3. **`README.md`** - This file (Project overview & setup)

---

## 🛠️ Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Frontend** | React + TypeScript | 18.2 + 5.3 |
| | Vite | 5.0 |
| | Redux Toolkit | 2.0 |
| | Tailwind CSS | 3.3 |
| **Backend** | FastAPI | 0.109 |
| | Python | 3.9+ |
| | SQLAlchemy | 2.0 |
| | LangGraph | Latest |
| **Services** | Azure OpenAI | GPT-4 |
| | Celery | 5.3 |
| | Redis | Latest |
| **Video** | MoviePy | 1.0 |
| | Matplotlib | 3.8 |

---

## 📈 System Requirements

### Minimum
- CPU: 2 cores
- RAM: 4 GB
- Storage: 500 MB
- Network: 10 Mbps

### Recommended
- CPU: 4+ cores
- RAM: 8+ GB
- Storage: 10 GB
- Network: 100 Mbps

---

## ⚠️ Troubleshooting

### Frontend Issues
```powershell
# Clear cache
rm node_modules package-lock.json
npm install
npm run dev
```

### Backend Issues
```powershell
# Check .env file
cat .env

# Check Python version
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Port Already in Use
```powershell
# Find process
netstat -ano | findstr :5173

# Kill process
taskkill /PID <PID> /F
```

---

## 🎓 Learning Path

1. **Understand the architecture** - See architecture diagram above
2. **Read FRONTEND.md** - Understand UI & React components
3. **Read BACKEND.md** - Understand APIs & agents
4. **Explore the code** - Review source files
5. **Run examples** - Test API endpoints
6. **Build features** - Extend functionality

---

## ✅ Pre-Deployment Checklist

- [ ] All .env variables set
- [ ] Database initialized
- [ ] Frontend builds successfully
- [ ] Backend tests pass
- [ ] API documentation reviewed
- [ ] Azure credentials validated
- [ ] CORS configured
- [ ] Security headers set
- [ ] Deployment tested

---

## 🎯 Next Steps

1. **Setup Frontend:** Follow Frontend Setup above
2. **Setup Backend:** Follow Backend Setup above
3. **Run Both:** Start both servers simultaneously
4. **Test:** Open http://localhost:5173
5. **Create Content:** Upload & generate videos
6. **Deploy:** Use docker-compose for production

---

## 📞 Resources

- **API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **Frontend Docs:** See `FRONTEND.md`
- **Backend Docs:** See `BACKEND.md`

---

## 🎉 You're Ready!

Everything is set up and ready to use. Start creating amazing educational videos! 🚀

**Questions?** Check `FRONTEND.md` and `BACKEND.md` for detailed documentation.
