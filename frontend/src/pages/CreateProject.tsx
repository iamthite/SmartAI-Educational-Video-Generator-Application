// // ============================================
// // frontend/src/pages/CreateProject.tsx - ENHANCED WITH CONFIG
// // ============================================
// import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';
// import { FileText, Upload, Sparkles } from 'lucide-react';
// import toast from 'react-hot-toast';
// import { contentService } from '../services/contentService';
// import Header from '../components/common/Header';
// import VideoConfigPanel from '../components/video/VideoConfigPanel';
// import ContentUpload from '../components/content/ContentUpload';
// import TextEditor from '../components/content/TextEditor';

// const CreateProject: React.FC = () => {
//   const navigate = useNavigate();
//   const [uploadType, setUploadType] = useState<'text' | 'file'>('text');
//   const [title, setTitle] = useState('');
//   const [description, setDescription] = useState('');
//   const [content, setContent] = useState('');
//   const [config, setConfig] = useState({
//     education_level: {
//       level: '10th',
//       subject: 'Mathematics',
//       topic: ''
//     },
//     voice: {
//       gender: 'female',
//       language: 'en-IN',
//       accent: 'indian',
//       speed: 1.0,
//       pitch: 1.0
//     },
//     style: {
//       theme: 'educational',
//       color_scheme: 'blue',
//       animation_style: 'smooth',
//       include_transitions: true,
//       background_music: false,
//       music_volume: 30
//     },
//     quality: '1080p',
//     duration_preference: 'medium',
//     include_subtitles: true,
//     subtitle_language: 'en',
//     pacing: 'medium',
//     include_diagrams: true,
//     include_examples: true
//   });
//   const [loading, setLoading] = useState(false);

//   const handleSubmit = async () => {
//     if (!title || !content) {
//       toast.error('Title and content are required');
//       return;
//     }

//     if (content.length < 50) {
//       toast.error('Content must be at least 50 characters');
//       return;
//     }

//     setLoading(true);
//     try {
//       const result = await contentService.uploadContent({
//         title,
//         description,
//         content,
//         content_type: 'text',
//         config
//       });

//       toast.success('Project created successfully!');
//       navigate(`/editor/${result.project_id}`);
//     } catch (error: any) {
//       toast.error(error.response?.data?.detail || 'Failed to create project');
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleFileUpload = async (file: File) => {
//     setLoading(true);
//     try {
//       const result = await contentService.uploadFile(file);
//       toast.success('File uploaded successfully!');
//       navigate(`/editor/${result.project_id}`);
//     } catch (error: any) {
//       toast.error(error.response?.data?.detail || 'Failed to upload file');
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
//       <Header />
      
//       <div className="max-w-7xl mx-auto py-8 px-4">
//         <div className="text-center mb-8">
//           <div className="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full mb-4">
//             <Sparkles className="w-4 h-4" />
//             <span className="text-sm font-medium">AI-Powered Creation</span>
//           </div>
//           <h1 className="text-4xl font-bold mb-2">Create New Project</h1>
//           <p className="text-gray-600">Upload content and configure your educational video</p>
//         </div>

//         <div className="grid lg:grid-cols-3 gap-6">
//           {/* Main Content Area */}
//           <div className="lg:col-span-2">
//             <div className="bg-white rounded-2xl shadow-lg p-8">
//               {/* Upload Type Toggle */}
//               <div className="flex gap-4 mb-6">
//                 <button
//                   onClick={() => setUploadType('text')}
//                   className={`flex-1 flex items-center justify-center gap-2 px-6 py-4 rounded-xl font-medium transition ${
//                     uploadType === 'text'
//                       ? 'bg-blue-600 text-white shadow-lg'
//                       : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
//                   }`}
//                 >
//                   <FileText className="w-5 h-5" />
//                   Text Input
//                 </button>
//                 <button
//                   onClick={() => setUploadType('file')}
//                   className={`flex-1 flex items-center justify-center gap-2 px-6 py-4 rounded-xl font-medium transition ${
//                     uploadType === 'file'
//                       ? 'bg-blue-600 text-white shadow-lg'
//                       : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
//                   }`}
//                 >
//                   <Upload className="w-5 h-5" />
//                   File Upload
//                 </button>
//               </div>

//               {uploadType === 'text' ? (
//                 <>
//                   {/* Title */}
//                   <div className="mb-6">
//                     <label className="block text-sm font-semibold mb-2 text-gray-700">
//                       Project Title *
//                     </label>
//                     <input
//                       type="text"
//                       value={title}
//                       onChange={(e) => setTitle(e.target.value)}
//                       className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
//                       placeholder="e.g., Quadratic Equations - Class 10"
//                     />
//                   </div>

//                   {/* Description */}
//                   <div className="mb-6">
//                     <label className="block text-sm font-semibold mb-2 text-gray-700">
//                       Description (Optional)
//                     </label>
//                     <input
//                       type="text"
//                       value={description}
//                       onChange={(e) => setDescription(e.target.value)}
//                       className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
//                       placeholder="Brief description of the content"
//                     />
//                   </div>

//                   {/* Content Editor */}
//                   <TextEditor value={content} onChange={setContent} />

//                   {/* Character Count */}
//                   <div className="flex justify-between items-center mt-4 text-sm text-gray-500">
//                     <span>Minimum 50 characters required</span>
//                     <span className={content.length >= 50 ? 'text-green-600' : 'text-gray-400'}>
//                       {content.length} / 50
//                     </span>
//                   </div>

//                   {/* Submit Button */}
//                   <button
//                     onClick={handleSubmit}
//                     disabled={loading || !title || content.length < 50}
//                     className="mt-6 w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white py-4 rounded-xl font-semibold hover:shadow-lg transition disabled:opacity-50 disabled:cursor-not-allowed"
//                   >
//                     {loading ? (
//                       <span className="flex items-center justify-center gap-2">
//                         <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
//                         Creating Project...
//                       </span>
//                     ) : (
//                       'Create Project & Configure Video'
//                     )}
//                   </button>
//                 </>
//               ) : (
//                 <ContentUpload onUpload={handleFileUpload} loading={loading} />
//               )}
//             </div>
//           </div>

//           {/* Configuration Panel */}
//           <div className="lg:col-span-1">
//             <VideoConfigPanel config={config} onChange={setConfig} />
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default CreateProject;




// #====================================================================


// ============================================
// frontend/src/pages/CreateProject.tsx - ENHANCED WITH CONFIG (fixed import path)
// ============================================
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FileText, Upload, Sparkles } from 'lucide-react';
import toast from 'react-hot-toast';
import { contentService } from '../services/contentService.ts';
import Header from '../components/common/Header.tsx';
import VideoConfigPanel from '../components/video/VideoConfigPanel.tsx';
import ContentUpload from '../components/content/ContentUpload.tsx';
import TextEditor from '../components/content/TextEditor.tsx';

const CreateProject: React.FC = () => {
  const navigate = useNavigate();
  const [uploadType, setUploadType] = useState<'text' | 'file'>('text');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [content, setContent] = useState('');
  const [config, setConfig] = useState({
    education_level: {
      level: '10th',
      subject: 'Mathematics',
      topic: ''
    },
    voice: {
      gender: 'female',
      language: 'en-IN',
      accent: 'indian',
      speed: 1.0,
      pitch: 1.0
    },
    style: {
      theme: 'educational',
      color_scheme: 'blue',
      animation_style: 'smooth',
      include_transitions: true,
      background_music: false,
      music_volume: 30
    },
    quality: '1080p',
    duration_preference: 'medium',
    include_subtitles: true,
    subtitle_language: 'en',
    pacing: 'medium',
    include_diagrams: true,
    include_examples: true
  });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!title || !content) {
      toast.error('Title and content are required');
      return;
    }

    if (content.length < 50) {
      toast.error('Content must be at least 50 characters');
      return;
    }

    setLoading(true);
    try {
      const result = await contentService.uploadContent({
        title,
        description,
        content,
        content_type: 'text',
        config
      });

      toast.success('Project created successfully!');
      navigate(`/editor/${result.project_id}`);
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to create project');
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = async (file: File) => {
    setLoading(true);
    try {
      const result = await contentService.uploadFile(file);
      toast.success('File uploaded successfully!');
      navigate(`/editor/${result.project_id}`);
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to upload file');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
      <Header />
      
      <div className="max-w-7xl mx-auto py-8 px-4">
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full mb-4">
            <Sparkles className="w-4 h-4" />
            <span className="text-sm font-medium">AI-Powered Creation</span>
          </div>
          <h1 className="text-4xl font-bold mb-2">Create New Project</h1>
          <p className="text-gray-600">Upload content and configure your educational video</p>
        </div>

        <div className="grid lg:grid-cols-3 gap-6">
          {/* Main Content Area */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-2xl shadow-lg p-8">
              {/* Upload Type Toggle */}
              <div className="flex gap-4 mb-6">
                <button
                  onClick={() => setUploadType('text')}
                  className={`flex-1 flex items-center justify-center gap-2 px-6 py-4 rounded-xl font-medium transition ${
                    uploadType === 'text'
                      ? 'bg-blue-600 text-white shadow-lg'
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  <FileText className="w-5 h-5" />
                  Text Input
                </button>
                <button
                  onClick={() => setUploadType('file')}
                  className={`flex-1 flex items-center justify-center gap-2 px-6 py-4 rounded-xl font-medium transition ${
                    uploadType === 'file'
                      ? 'bg-blue-600 text-white shadow-lg'
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  <Upload className="w-5 h-5" />
                  File Upload
                </button>
              </div>

              {uploadType === 'text' ? (
                <>
                  {/* Title */}
                  <div className="mb-6">
                    <label className="block text-sm font-semibold mb-2 text-gray-700">
                      Project Title *
                    </label>
                    <input
                      type="text"
                      value={title}
                      onChange={(e) => setTitle(e.target.value)}
                      className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                      placeholder="e.g., Quadratic Equations - Class 10"
                    />
                  </div>

                  {/* Description */}
                  <div className="mb-6">
                    <label className="block text-sm font-semibold mb-2 text-gray-700">
                      Description (Optional)
                    </label>
                    <input
                      type="text"
                      value={description}
                      onChange={(e) => setDescription(e.target.value)}
                      className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                      placeholder="Brief description of the content"
                    />
                  </div>

                  {/* Content Editor */}
                  <TextEditor value={content} onChange={setContent} />

                  {/* Character Count */}
                  <div className="flex justify-between items-center mt-4 text-sm text-gray-500">
                    <span>Minimum 50 characters required</span>
                    <span className={content.length >= 50 ? 'text-green-600' : 'text-gray-400'}>
                      {content.length} / 50
                    </span>
                  </div>

                  {/* Submit Button */}
                  <button
                    onClick={handleSubmit}
                    disabled={loading || !title || content.length < 50}
                    className="mt-6 w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white py-4 rounded-xl font-semibold hover:shadow-lg transition disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {loading ? (
                      <span className="flex items-center justify-center gap-2">
                        <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                        Creating Project...
                      </span>
                    ) : (
                      'Create Project & Configure Video'
                    )}
                  </button>
                </>
              ) : (
                <ContentUpload onUpload={handleFileUpload} loading={loading} />
              )}
            </div>
          </div>

          {/* Configuration Panel */}
          <div className="lg:col-span-1">
            <VideoConfigPanel config={config} onChange={setConfig} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateProject;
