# 🎨 Frontend Documentation - React + TypeScript

Complete frontend code documentation for the Educational Video Generator.

---

## 📋 Overview

- **Framework:** React 18.2 with TypeScript 5.3
- **State Management:** Redux Toolkit 2.0
- **Styling:** Tailwind CSS 3.3
- **Build Tool:** Vite 5.0
- **HTTP Client:** Axios 1.6
- **Routing:** React Router 6.20
- **Icons:** Lucide React 0.294

---

## 🗂️ Folder Structure

```
frontend/src/
│
├── pages/                           ← Complete page components
│   ├── Home.tsx                    ← Landing page
│   ├── Login.tsx                   ← Authentication
│   ├── Dashboard.tsx               ← Project list
│   ├── CreateProject.tsx           ← Video creator
│   ├── VideoEditor.tsx             ← Video viewer & editor
│   ├── Settings.tsx                ← User preferences
│   └── Analytics.tsx               ← Usage statistics
│
├── components/                      ← Reusable components
│   ├── common/
│   │   ├── Header.tsx              ← Navigation header
│   │   ├── LoadingSpinner.tsx      ← Loading indicator
│   │   └── ProgressBar.tsx         ← Progress display
│   │
│   ├── content/
│   │   ├── ContentUpload.tsx       ← File drop zone
│   │   └── TextEditor.tsx          ← Text input area
│   │
│   ├── dashboard/
│   │   └── ProjectCard.tsx         ← Project display card
│   │
│   └── video/
│       ├── VideoPlayer.tsx         ← Video playback control
│       ├── VideoConfigPanel.tsx    ← Configuration form
│       ├── ProgressTracker.tsx     ← Generation progress
│       ├── VideoConfigurator.tsx   ← Settings UI
│       └── VideoPreview.tsx        ← Preview display
│
├── services/                        ← API clients
│   ├── api.ts                      ← Axios config & interceptors
│   ├── contentService.ts           ← Content operations
│   └── videoService.ts             ← Video operations
│
├── hooks/                           ← Custom React hooks
│   ├── useVideoGenerator.ts        ← Video generation logic
│   └── useWebSocket.ts             ← Real-time updates
│
├── store/                           ← Redux state management
│   ├── index.ts                    ← Store configuration
│   └── slices/
│       ├── authSlice.ts            ← User authentication
│       └── projectSlice.ts         ← Project management
│
├── types/                           ← TypeScript interfaces
│   └── index.ts                    ← All type definitions
│
├── App.tsx                          ← Main router component
├── main.tsx                         ← React entry point
├── App.css                          ← Global styles
├── index.css                        ← Base styles
└── vite-env.d.ts                   ← Vite env types
```

---

## 📄 File Details

### Pages

#### `pages/Home.tsx`
Landing page with:
- Hero section with CTA
- Feature highlights
- How-it-works steps
- Testimonials
- Footer

```typescript
export interface HomeProps {}
// Static landing page, no props
```

#### `pages/Login.tsx`
Authentication page with:
- Email input
- Password input
- Login button
- Remember me option

#### `pages/Dashboard.tsx`
Project management with:
- Project list display
- Create new project button
- Project search/filter
- Status indicators

```typescript
interface Project {
  id: number;
  title: string;
  description?: string;
  status: 'created' | 'processing' | 'completed' | 'failed';
  created_at: string;
}
```

#### `pages/CreateProject.tsx`
Video creation interface with:
- Text input option
- File upload option
- Video configuration panel
- Generate button

#### `pages/VideoEditor.tsx`
Video viewing & editing with:
- Project info display
- Video player
- Progress tracker
- Download/Share buttons
- History section

#### `pages/Settings.tsx`
User settings page

#### `pages/Analytics.tsx`
Usage analytics page

---

### Components

#### `components/common/Header.tsx`
Navigation header with:
- Logo
- Navigation links
- User menu

```typescript
interface HeaderProps {}
// No props, uses Router context
```

#### `components/common/LoadingSpinner.tsx`
Animated loading spinner

```typescript
interface LoadingSpinnerProps {}
```

#### `components/common/ProgressBar.tsx`
Horizontal progress indicator

```typescript
interface ProgressBarProps {
  progress: number;  // 0-100
}
```

#### `components/content/ContentUpload.tsx`
Drag-and-drop file uploader

```typescript
interface ContentUploadProps {
  onUpload: (file: File) => void;
  loading: boolean;
}
```

Supported formats:
- PDF (.pdf)
- Word (.docx)
- Text (.txt)

#### `components/content/TextEditor.tsx`
Text input area with character counter

```typescript
interface TextEditorProps {
  value: string;
  onChange: (value: string) => void;
}
```

#### `components/dashboard/ProjectCard.tsx`
Individual project card display

```typescript
interface ProjectCardProps {
  project: Project;
}
```

#### `components/video/VideoPlayer.tsx`
Custom HTML5 video player with:
- Play/Pause controls
- Progress bar
- Volume control
- Fullscreen

```typescript
interface VideoPlayerProps {
  url: string;
  title: string;
  duration: number;
}
```

#### `components/video/VideoConfigPanel.tsx`
Configuration form for:
- Education level
- Voice selection
- Language
- Quality
- Subtitles
- etc.

```typescript
interface VideoConfigPanelProps {
  config: any;
  onChange: (config: any) => void;
  readOnly?: boolean;
}
```

#### `components/video/ProgressTracker.tsx`
Shows video generation progress with:
- Overall progress percentage
- Step-by-step progress
- Current status
- Time remaining

```typescript
interface ProgressTrackerProps {
  progress: number;
  status: string;
  message: string;
  isConnected: boolean;
}
```

#### `components/video/VideoConfigurator.tsx`
Settings selection UI

#### `components/video/VideoPreview.tsx`
Video preview with download/share buttons

---

### Services

#### `services/api.ts`
Axios instance configuration:

```typescript
// Base configuration
const API_BASE_URL = 'http://localhost:8000';
const api = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  headers: { 'Content-Type': 'application/json' }
});

// Auto-add JWT token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export { api };
```

#### `services/contentService.ts`
Content management API:

```typescript
interface ContentUpload {
  title: string;
  description?: string;
  content: string;
  content_type?: string;
}

interface Project {
  id: number;
  title: string;
  description?: string;
  status: string;
  created_at: string;
}

export const contentService = {
  uploadContent: async (data: ContentUpload) => Promise,
  uploadFile: async (file: File) => Promise,
  getProjects: async () => Promise<Project[]>,
  getProject: async (projectId: number) => Promise<Project>
};
```

#### `services/videoService.ts`
Video generation API:

```typescript
interface VideoGenerateResponse {
  message: string;
  task_id: string;
  project_id: number;
}

export const videoService = {
  generateVideo: async (projectId: number) => Promise<VideoGenerateResponse>,
  getTaskStatus: async (taskId: string) => Promise<TaskStatus>,
  getProjectVideos: async (projectId: number) => Promise
};
```

---

### Hooks

#### `hooks/useVideoGenerator.ts`
Custom hook for video generation:

```typescript
export const useVideoGenerator = () => {
  const [taskId, setTaskId] = useState<string | null>(null);
  const [status, setStatus] = useState<'idle' | 'generating' | 'completed' | 'failed'>('idle');
  const [progress, setProgress] = useState(0);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const generateVideo = async (projectId: number) => Promise;
  
  return { generateVideo, status, progress, videoUrl, error };
};
```

#### `hooks/useWebSocket.ts`
WebSocket hook for real-time updates:

```typescript
export const useWebSocket = (clientId: string) => {
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState('idle');
  const [message, setMessage] = useState('');
  const [isConnected, setIsConnected] = useState(false);

  // Connects to ws://localhost:8000/ws/{clientId}
  // Updates state as messages arrive
  
  return { progress, status, message, isConnected };
};
```

---

### Redux Store

#### `store/index.ts`
Redux store configuration:

```typescript
export const store = configureStore({
  reducer: {
    auth: authReducer,
    project: projectReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

#### `store/slices/authSlice.ts`
Authentication state:

```typescript
interface AuthState {
  isAuthenticated: boolean;
  user: any | null;
  token: string | null;
}

// Actions: login, logout
```

#### `store/slices/projectSlice.ts`
Project state:

```typescript
interface ProjectState {
  currentProject: any | null;
  projects: any[];
}

// Actions: setCurrentProject, setProjects
```

---

### Types

#### `types/index.ts`
Central type definitions:

```typescript
export interface Project {
  id: number;
  title: string;
  description: string;
  content: string;
  status: 'created' | 'processing' | 'completed' | 'failed';
  created_at: string;
}

export interface Video {
  id: number;
  project_id: number;
  title: string;
  duration: number;
  file_url: string;
  thumbnail_url: string;
  status: string;
  created_at: string;
}

export interface Asset {
  id: number;
  project_id: number;
  asset_type: 'image' | 'audio' | 'diagram';
  file_url: string;
  file_metadata: Record<string, any>;
  created_at: string;
}

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  message?: string;
}
```

---

## 🚀 Component Usage Examples

### Using ContentUpload
```typescript
<ContentUpload 
  onUpload={(file) => handleFileUpload(file)}
  loading={isLoading}
/>
```

### Using VideoPlayer
```typescript
<VideoPlayer 
  url={videoUrl}
  title="Generated Video"
  duration={300}
/>
```

### Using ProgressTracker
```typescript
<ProgressTracker
  progress={75}
  status="generating_audio"
  message="Generating audio narration..."
  isConnected={true}
/>
```

### Using Redux
```typescript
import { useDispatch, useSelector } from 'react-redux';
import { setCurrentProject } from '../store/slices/projectSlice';

const MyComponent = () => {
  const dispatch = useDispatch();
  const currentProject = useSelector(state => state.project.currentProject);

  const handleSelect = (project) => {
    dispatch(setCurrentProject(project));
  };

  return (...);
};
```

---

## 🔄 Data Flow

```
User Input (Form)
        ↓
Event Handler (onClick, onChange)
        ↓
Service Call (contentService.uploadContent)
        ↓
HTTP Request (Axios)
        ↓
Redux Action (dispatch)
        ↓
State Update
        ↓
Component Re-render
        ↓
UI Display
```

---

## 🔌 API Integration

### Making Requests
```typescript
// In a service
const response = await api.post('/content/upload', data);

// In a component
const result = await contentService.uploadContent(formData);
```

### Error Handling
```typescript
try {
  await contentService.uploadContent(data);
  toast.success('Success!');
} catch (error: any) {
  toast.error(error.response?.data?.detail || 'Error');
}
```

### Authentication
```typescript
// Token automatically added by interceptor
const response = await api.get('/content/projects');
// Authorization header: Bearer {token}
```

---

## 🎨 Styling

Using **Tailwind CSS** for all styling:

```typescript
// Utility classes
<div className="bg-blue-600 text-white px-4 py-2 rounded-lg">
  Button
</div>

// Responsive
<div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
  Items
</div>

// Hover effects
<button className="hover:bg-blue-700 transition">
  Hover Me
</button>
```

---

## 🔄 State Management

### Using Redux
```typescript
// Dispatch action
dispatch(setCurrentProject(project));

// Select state
const project = useSelector(state => state.project.currentProject);
```

### Local State
```typescript
const [formData, setFormData] = useState({...});
const [loading, setLoading] = useState(false);
```

---

## 📱 Component Lifecycle

### useEffect Example
```typescript
useEffect(() => {
  // Load projects on mount
  loadProjects();
}, []);

useEffect(() => {
  // Update when projectId changes
  if (projectId) {
    loadProject(projectId);
  }
}, [projectId]);
```

---

## 🧪 Testing Components

### Component Structure
1. Props interface defined
2. Default values set
3. Event handlers prepared
4. Render JSX

### Example Test
```typescript
const MyComponent: React.FC<MyProps> = ({ prop1, onAction }) => {
  return (
    <div>
      <h1>{prop1}</h1>
      <button onClick={() => onAction()}>Click</button>
    </div>
  );
};
```

---

## 🔒 Security

### JWT Token Storage
```typescript
// Stored in localStorage (insecure for sensitive data)
localStorage.setItem('access_token', token);

// Alternative: Use httpOnly cookies (recommended for production)
```

### CORS Configuration
Backend should allow frontend origin:
```
Access-Control-Allow-Origin: http://localhost:5173
```

---

## ⚡ Performance Tips

1. **Code Splitting:** Use React.lazy() for pages
2. **Memoization:** Use useMemo() for expensive calculations
3. **Optimization:** Use useCallback() for event handlers
4. **Images:** Optimize and compress before upload
5. **Bundle:** Vite automatically splits chunks

---

## 🐛 Debugging

### Browser DevTools
1. **Console:** Check for errors
2. **Network:** Monitor API calls
3. **Redux DevTools:** View state changes
4. **Elements:** Inspect HTML structure

### VS Code
1. Open Terminal: `Ctrl + ~`
2. View Problems: `Ctrl + Shift + M`
3. Debug: Use breakpoints

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| react | 18.2 | UI framework |
| react-dom | 18.2 | DOM rendering |
| react-router-dom | 6.20 | Routing |
| @reduxjs/toolkit | 2.0 | State management |
| react-redux | 9.0 | Redux bindings |
| axios | 1.6 | HTTP client |
| react-dropzone | 14.2 | File upload |
| lucide-react | 0.294 | Icons |
| react-hot-toast | 2.4 | Notifications |
| tailwindcss | 3.3 | Styling |

---

## 🚀 Deployment

### Build for Production
```powershell
npm run build
# Creates dist/ folder with optimized files
```

### Preview Build Locally
```powershell
npm run preview
# Test the production build
```

### Deploy
- Copy `dist/` folder to web server
- Or use Docker: `docker build -t frontend .`

---

## 📚 Resources

- **React Docs:** https://react.dev
- **TypeScript Docs:** https://www.typescriptlang.org
- **Redux Toolkit:** https://redux-toolkit.js.org
- **React Router:** https://reactrouter.com
- **Tailwind CSS:** https://tailwindcss.com
- **Axios:** https://axios-http.com

---

## 🎯 Common Tasks

### Add a new page
1. Create file in `pages/`
2. Add route in `App.tsx`
3. Import in router

### Add a new component
1. Create in `components/`
2. Define props interface
3. Import where needed

### Add API call
1. Add method to `services/`
2. Use in component
3. Handle errors

### Add Redux state
1. Create slice in `store/slices/`
2. Add to store in `store/index.ts`
3. Use with useDispatch/useSelector

---

**Frontend is ready to use! 🎨**
