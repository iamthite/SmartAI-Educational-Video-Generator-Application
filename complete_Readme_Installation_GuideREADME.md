# 🎓 Educational Video Generator - Production Ready v2.0

AI-Powered Educational Video Generation Platform for Indian Education System (1st-12th, Diploma, Engineering, Medical, and all educational fields)

## ✨ Features

### Core Features
- ✅ **Multi-Subject Support**: Mathematics, Physics, Biology, Chemistry, History, and more
- ✅ **Indian Voice Support**: Hindi, Tamil, Telugu, Marathi, and English with Indian accent
- ✅ **Real-Time Progress Tracking**: Live WebSocket updates during generation
- ✅ **Multiple Input Formats**: Text, PDF, DOCX, TXT, Markdown
- ✅ **HD Quality Videos**: 720p, 1080p, and 1440p support
- ✅ **Customizable Settings**: Voice, language, speed, style, and more
- ✅ **Professional Narration**: Azure Neural TTS with natural voices
- ✅ **Auto-Generated Visuals**: AI-powered diagrams and illustrations
- ✅ **Subtitle Support**: Multiple languages with auto-generation

### Production Features
- ✅ Real-time progress tracking with WebSocket
- ✅ Video preview and playback
- ✅ Download and share functionality
- ✅ Project management dashboard
- ✅ Error handling and user feedback
- ✅ Beautiful modern UI with Tailwind CSS
- ✅ Responsive design for all devices
- ✅ Toast notifications for user actions
- ✅ Analytics and statistics

---

## 🚀 Quick Start (Windows)

### Prerequisites
- Python 3.11 or higher
- Node.js 18 or higher
- Azure Account (for AI services)

### Step 1: Setup Azure Services

#### Azure OpenAI
1. Go to [Azure Portal](https://portal.azure.com)
2. Create "Azure OpenAI" resource
3. Deploy GPT-4 model
4. Copy: Endpoint, API Key, Deployment Name

#### Azure Speech Service
1. Create "Speech Services" resource
2. Copy: Key and Region

#### Azure Blob Storage
1. Create "Storage Account"
2. Create container named "videos"
3. Copy: Connection String

### Step 2: Clone or Download Project

```bash
# If you have the code
cd edu-video-generator

# Or create new folder and copy code
mkdir edu-video-generator
cd edu-video-generator
```

### Step 3: Run Setup Script

```cmd
setup-complete.bat
```

This will:
- Create Python virtual environment
- Install all backend dependencies
- Install all frontend dependencies
- Create database
- Copy environment templates

### Step 4: Configure Azure Credentials

Edit `backend\.env`:

```env
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Azure Speech
AZURE_SPEECH_KEY=your_speech_key_here
AZURE_SPEECH_REGION=eastus

# Azure Storage
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...
AZURE_STORAGE_CONTAINER_NAME=videos

# Database (SQLite - no change needed)
DATABASE_URL=sqlite:///./edu_video.db
```

### Step 5: Start Application

**Option A: Quick Start (Opens 2 windows)**
```cmd
quick-start.bat
```

**Option B: Manual Start (2 separate windows)**

Window 1 - Backend:
```cmd
start-backend.bat
```

Window 2 - Frontend:
```cmd
start-frontend.bat
```

### Step 6: Access Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## 📖 User Guide

### Creating Your First Video

1. **Go to Create Page**
   - Click "Get Started" or "Create" in navigation

2. **Choose Input Method**
   - Text Input: Type or paste content directly
   - File Upload: Upload PDF, DOCX, or TXT file

3. **Enter Project Details**
   - Title: e.g., "Quadratic Equations - Class 10"
   - Description: Brief overview
   - Content: Educational material (minimum 50 characters)

4. **Configure Video Settings**
   - Education Level: Select grade/level
   - Subject: Choose subject area
   - Voice: Select gender, language, accent
   - Quality: 720p, 1080p, or 1440p
   - Style: Educational, professional, or casual
   - Additional options: subtitles, diagrams, examples

5. **Generate Video**
   - Click "Create Project"
   - Watch real-time progress
   - Wait for completion (usually 5-10 minutes)

6. **Preview & Download**
   - Watch generated video
   - Download MP4 file
   - Share with students

---

## 🎨 Customization Options

### Voice Configuration

**Languages Supported:**
- English (Indian Accent) - `en-IN`
- Hindi - `hi-IN`
- Tamil - `ta-IN`
- Telugu - `te-IN`
- Marathi - `mr-IN`

**Voice Options:**
- Gender: Male / Female
- Speed: 0.5x to 2.0x
- Pitch: 0.5x to 2.0x

### Video Styles

**Themes:**
- Educational: Classic teaching style
- Professional: Business presentation
- Casual: Friendly and approachable

**Color Schemes:**
- Blue (default)
- Green
- Purple
- Custom

### Quality Settings

- **720p**: Fast generation (3-5 minutes)
- **1080p**: Standard quality (5-8 minutes)
- **1440p**: High quality (8-12 minutes)

---

## 🔧 Advanced Configuration

### Backend Configuration

Edit `backend/app/config.py` for:
- Maximum file size
- Supported file extensions
- Video duration limits
- Rate limiting

### Frontend Customization

Edit `frontend/src/App.css` for:
- Color schemes
- Font families
- Animation speeds
- Layout preferences

---

## 📊 API Documentation

Once backend is running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

**Content Management:**
```
POST /api/v1/content/upload         - Upload text content
POST /api/v1/content/upload-file    - Upload document
GET  /api/v1/content/projects       - List projects
GET  /api/v1/content/projects/{id}  - Get project
DELETE /api/v1/content/projects/{id} - Delete project
```

**Video Generation:**
```
POST /api/v1/video/generate/{id}        - Start generation
GET  /api/v1/video/projects/{id}/videos - List videos
GET  /api/v1/video/videos/{id}/download - Download video
```

**WebSocket:**
```
WS /ws/{project_id} - Real-time progress updates
```

---

## 🐛 Troubleshooting

### Backend Won't Start

**Error: "ModuleNotFoundError"**
```cmd
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

**Error: "Database connection failed"**
- Using SQLite by default, no database server needed
- Check `DATABASE_URL` in `.env`

**Error: "Azure API error"**
- Verify Azure credentials in `.env`
- Check API key is valid
- Ensure services are enabled

### Frontend Won't Start

**Error: "npm not found"**
- Install Node.js from https://nodejs.org

**Error: "Port 3000 already in use"**
```cmd
# Kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### Video Generation Fails

**Check:**
1. Azure credentials are correct
2. Backend server is running
3. WebSocket connection is active
4. Content meets minimum length (50 chars)

**Logs:**
```cmd
# Backend logs
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload --log-level debug
```

---

## 📈 Performance Optimization

### For Faster Video Generation

1. **Use 720p quality** for quick tests
2. **Shorter content** (5-10 minutes ideal)
3. **Disable background music** if not needed
4. **Use faster voice speed** (1.2x)

### For Better Quality

1. **Use 1080p or 1440p** quality
2. **Enable all features** (diagrams, examples)
3. **Use slower pacing** for clarity
4. **Include subtitles** for accessibility

---

## 🔐 Security Best Practices

1. **Never commit `.env` files** to version control
2. **Use strong SECRET_KEY** in production
3. **Enable HTTPS** for production deployment
4. **Implement rate limiting** on API
5. **Regular security updates** of dependencies

---

## 🚢 Production Deployment

### Deploy to Azure

**Backend (Azure App Service):**
```bash
az webapp up --name eduvidgen-api --runtime PYTHON:3.11 --sku B1
```

**Frontend (Azure Static Web Apps):**
```bash
cd frontend
npm run build
az staticwebapp create --name eduvidgen-web --source ./dist
```

### Environment Variables for Production

Set these in Azure App Service:
```
ENVIRONMENT=production
DEBUG=False
DATABASE_URL=<production_database>
SECRET_KEY=<strong_random_key>
CORS_ORIGINS=["https://yourdomain.com"]
```

---

## 📞 Support & Contribution

### Getting Help
- Check [Troubleshooting](#troubleshooting) section
- Review API documentation at `/docs`
- Check logs for error messages

### Contributing
1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

- Azure AI Services
- React & TypeScript
- FastAPI
- Tailwind CSS
- LangChain & LangGraph

---

## 🎯 Roadmap

### Phase 1 (Current)
- ✅ Basic video generation
- ✅ Real-time progress tracking
- ✅ Multiple language support
- ✅ File upload support

### Phase 2 (Coming Soon)
- ⏳ Video editing features
- ⏳ Batch generation
- ⏳ Template system
- ⏳ Analytics dashboard

### Phase 3 (Future)
- 🔮 AI-powered quizzes
- 🔮 Interactive elements
- 🔮 LMS integration
- 🔮 Mobile app

---

## 📊 System Requirements

### Minimum Requirements
- **CPU**: Dual-core processor
- **RAM**: 4GB
- **Storage**: 10GB free space
- **Internet**: Broadband connection

### Recommended Requirements
- **CPU**: Quad-core processor
- **RAM**: 8GB or more
- **Storage**: 50GB free space
- **Internet**: High-speed connection

---

## 🎓 Educational Use Cases

### Perfect For:
- School Teachers (1st-12th grade)
- College Professors
- Online Course Creators
- Educational Content Creators
- Tutorial Makers
- Training Organizations

### Subjects Supported:
- Mathematics
- Physics
- Chemistry
- Biology
- History
- Geography
- Computer Science
- Engineering
- Medical Sciences
- And more...

---

**Made with ❤️ for Indian Education System**

For questions or support, open an issue on GitHub.