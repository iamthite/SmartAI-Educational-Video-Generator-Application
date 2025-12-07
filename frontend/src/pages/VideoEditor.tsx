// // ============================================
// // frontend/src/pages/VideoEditor.tsx - WITH REAL-TIME PROGRESS
// // ============================================
// import React, { useEffect, useState } from 'react';
// import { useParams } from 'react-router-dom';
// import { Play, Download, Share2, Eye } from 'lucide-react';
// import toast from 'react-hot-toast';
// import { contentService } from '../services/contentService';
// import { videoService } from '../services/videoService';
// import Header from '../components/common/Header';
// import VideoPlayer from '../components/video/VideoPlayer';
// import ProgressTracker from '../components/video/ProgressTracker';
// import VideoConfigPanel from '../components/video/VideoConfigPanel';
// import { useWebSocket } from '../hooks/useWebSocket';

// const VideoEditor: React.FC = () => {
//   const { projectId } = useParams<{ projectId: string }>();
//   const [project, setProject] = useState<any>(null);
//   const [videos, setVideos] = useState<any[]>([]);
//   const [generating, setGenerating] = useState(false);
//   const [config, setConfig] = useState<any>(null);

//   const { progress, status, message, isConnected } = useWebSocket(projectId || '');

//   useEffect(() => {
//     if (projectId) {
//       loadProject();
//       loadVideos();
//     }
//   }, [projectId]);

//   const loadProject = async () => {
//     try {
//       const data = await contentService.getProject(parseInt(projectId!));
//       setProject(data);
//       setConfig(data.config || {});
//     } catch (error) {
//       toast.error('Failed to load project');
//     }
//   };

//   const loadVideos = async () => {
//     try {
//       const data = await videoService.getProjectVideos(parseInt(projectId!));
//       setVideos(data);
//     } catch (error) {
//       console.error('Failed to load videos');
//     }
//   };

//   const handleGenerate = async () => {
//     try {
//       setGenerating(true);
//       await videoService.generateVideo(parseInt(projectId!));
//       toast.success('Video generation started!');
//     } catch (error: any) {
//       toast.error(error.response?.data?.detail || 'Failed to start generation');
//       setGenerating(false);
//     }
//   };

//   const handleDownload = async (videoId: number) => {
//     try {
//       const result = await videoService.downloadVideo(videoId);
//       window.open(result.download_url, '_blank');
//       toast.success('Download started!');
//     } catch (error) {
//       toast.error('Failed to download video');
//     }
//   };

//   const completedVideo = videos.find(v => v.status === 'completed');

//   return (
//     <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
//       <Header />
      
//       <div className="max-w-7xl mx-auto py-8 px-4">
//         {project && (
//           <>
//             {/* Header Info */}
//             <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
//               <div className="flex items-start justify-between">
//                 <div>
//                   <h1 className="text-3xl font-bold mb-2">{project.title}</h1>
//                   <p className="text-gray-600">{project.description}</p>
//                   <div className="flex items-center gap-4 mt-4">
//                     <span className={`px-3 py-1 rounded-full text-sm font-medium ${
//                       project.status === 'completed' 
//                         ? 'bg-green-100 text-green-700'
//                         : project.status === 'failed'
//                         ? 'bg-red-100 text-red-700'
//                         : 'bg-blue-100 text-blue-700'
//                     }`}>
//                       {project.status}
//                     </span>
//                     <span className="text-sm text-gray-500">
//                       Created {new Date(project.created_at).toLocaleDateString()}
//                     </span>
//                   </div>
//                 </div>
                
//                 {!generating && project.status !== 'completed' && (
//                   <button
//                     onClick={handleGenerate}
//                     className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-3 rounded-xl font-semibold hover:shadow-lg transition flex items-center gap-2"
//                   >
//                     <Play className="w-5 h-5" />
//                     Generate Video
//                   </button>
//                 )}
//               </div>
//             </div>

//             <div className="grid lg:grid-cols-3 gap-6">
//               {/* Main Content */}
//               <div className="lg:col-span-2 space-y-6">
//                 {/* Progress Tracker */}
//                 {(generating || ['analyzing', 'generating_script', 'creating_visuals', 'generating_audio', 'composing_video', 'uploading'].includes(project.status)) && (
//                   <ProgressTracker
//                     progress={progress}
//                     status={status}
//                     message={message}
//                     isConnected={isConnected}
//                   />
//                 )}

//                 {/* Video Player */}
//                 {completedVideo && (
//                   <div className="bg-white rounded-2xl shadow-lg p-6">
//                     <div className="flex items-center justify-between mb-6">
//                       <h2 className="text-2xl font-bold">Generated Video</h2>
//                       <div className="flex gap-3">
//                         <button
//                           onClick={() => handleDownload(completedVideo.id)}
//                           className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
//                         >
//                           <Download className="w-4 h-4" />
//                           Download
//                         </button>
//                         <button className="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition">
//                           <Share2 className="w-4 h-4" />
//                           Share
//                         </button>
//                       </div>
//                     </div>
                    
//                     <VideoPlayer
//                       url={completedVideo.file_url}
//                       title={completedVideo.title}
//                       duration={completedVideo.duration}
//                     />

//                     {/* Video Info */}
//                     <div className="mt-6 grid grid-cols-3 gap-4 text-center">
//                       <div className="p-4 bg-gray-50 rounded-xl">
//                         <Eye className="w-5 h-5 mx-auto mb-2 text-blue-600" />
//                         <div className="text-2xl font-bold">{completedVideo.views}</div>
//                         <div className="text-sm text-gray-600">Views</div>
//                       </div>
//                       <div className="p-4 bg-gray-50 rounded-xl">
//                         <Download className="w-5 h-5 mx-auto mb-2 text-green-600" />
//                         <div className="text-2xl font-bold">{completedVideo.downloads}</div>
//                         <div className="text-sm text-gray-600">Downloads</div>
//                       </div>
//                       <div className="p-4 bg-gray-50 rounded-xl">
//                         <Play className="w-5 h-5 mx-auto mb-2 text-purple-600" />
//                         <div className="text-2xl font-bold">
//                           {Math.floor(completedVideo.duration / 60)}:{(completedVideo.duration % 60).toString().padStart(2, '0')}
//                         </div>
//                         <div className="text-sm text-gray-600">Duration</div>
//                       </div>
//                     </div>
//                   </div>
//                 )}

//                 {/* Video History */}
//                 {videos.length > 1 && (
//                   <div className="bg-white rounded-2xl shadow-lg p-6">
//                     <h3 className="text-xl font-bold mb-4">Generation History</h3>
//                     <div className="space-y-3">
//                       {videos.map((video) => (
//                         <div key={video.id} className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition">
//                           <div>
//                             <div className="font-medium">{video.title}</div>
//                             <div className="text-sm text-gray-500">
//                               {new Date(video.created_at).toLocaleString()}
//                             </div>
//                           </div>
//                           <div className="flex items-center gap-3">
//                             <span className={`px-3 py-1 rounded-full text-xs font-medium ${
//                               video.status === 'completed' 
//                                 ? 'bg-green-100 text-green-700'
//                                 : 'bg-gray-100 text-gray-700'
//                             }`}>
//                               {video.status}
//                             </span>
//                             {video.status === 'completed' && (
//                               <button
//                                 onClick={() => handleDownload(video.id)}
//                                 className="text-blue-600 hover:text-blue-700"
//                               >
//                                 <Download className="w-5 h-5" />
//                               </button>
//                             )}
//                           </div>
//                         </div>
//                       ))}
//                     </div>
//                   </div>
//                 )}
//               </div>

//               {/* Sidebar */}
//               <div className="lg:col-span-1">
//                 <VideoConfigPanel config={config} onChange={setConfig} readonly />
//               </div>
//             </div>
//           </>
//         )}
//       </div>
//     </div>
//   );
// };

// export default VideoEditor;






// ============================================
// frontend/src/pages/VideoEditor.tsx - WITH REAL-TIME PROGRESS (fixed import path & readOnly prop)
// ============================================
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Play, Download, Share2, Eye } from 'lucide-react';
import toast from 'react-hot-toast';
import { contentService } from '../services/contentService.ts';
import { videoService } from '../services/videoService.ts';
import Header from '../components/common/Header.tsx';
import VideoPlayer from '../components/video/VideoPlayer.tsx';
import ProgressTracker from '../components/video/ProgressTracker.tsx';
import VideoConfigPanel from '../components/video/VideoConfigPanel.tsx';
import { useWebSocket } from '../hooks/useWebSocket.ts';

const VideoEditor: React.FC = () => {
  const { projectId } = useParams<{ projectId: string }>();
  const [project, setProject] = useState<any>(null);
  const [videos, setVideos] = useState<any[]>([]);
  const [generating, setGenerating] = useState(false);
  const [config, setConfig] = useState<any>(null);

  const { progress, status, message, isConnected } = useWebSocket(projectId || '');

  useEffect(() => {
    if (projectId) {
      loadProject();
      loadVideos();
    }
  }, [projectId]);

  const loadProject = async () => {
    try {
      const data = await contentService.getProject(parseInt(projectId!));
      setProject(data);
      setConfig(data.config || {});
    } catch (error) {
      toast.error('Failed to load project');
    }
  };

  const loadVideos = async () => {
    try {
      const data = await videoService.getProjectVideos(parseInt(projectId!));
      setVideos(data);
    } catch (error) {
      console.error('Failed to load videos');
    }
  };

  const handleGenerate = async () => {
    try {
      setGenerating(true);
      await videoService.generateVideo(parseInt(projectId!));
      toast.success('Video generation started!');
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Failed to start generation');
      setGenerating(false);
    }
  };

  const handleDownload = async (videoId: number) => {
    try {
      const result = await videoService.downloadVideo(videoId);
      window.open(result.download_url, '_blank');
      toast.success('Download started!');
    } catch (error) {
      toast.error('Failed to download video');
    }
  };

  const completedVideo = videos.find(v => v.status === 'completed');

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
      <Header />
      
      <div className="max-w-7xl mx-auto py-8 px-4">
        {project && (
          <>
            {/* Header Info */}
            <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
              <div className="flex items-start justify-between">
                <div>
                  <h1 className="text-3xl font-bold mb-2">{project.title}</h1>
                  <p className="text-gray-600">{project.description}</p>
                  <div className="flex items-center gap-4 mt-4">
                    <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                      project.status === 'completed' 
                        ? 'bg-green-100 text-green-700'
                        : project.status === 'failed'
                        ? 'bg-red-100 text-red-700'
                        : 'bg-blue-100 text-blue-700'
                    }`}>
                      {project.status}
                    </span>
                    <span className="text-sm text-gray-500">
                      Created {new Date(project.created_at).toLocaleDateString()}
                    </span>
                  </div>
                </div>
                
                {!generating && project.status !== 'completed' && (
                  <button
                    onClick={handleGenerate}
                    className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-3 rounded-xl font-semibold hover:shadow-lg transition flex items-center gap-2"
                  >
                    <Play className="w-5 h-5" />
                    Generate Video
                  </button>
                )}
              </div>
            </div>

            <div className="grid lg:grid-cols-3 gap-6">
              {/* Main Content */}
              <div className="lg:col-span-2 space-y-6">
                {/* Progress Tracker */}
                {(generating || ['analyzing', 'generating_script', 'creating_visuals', 'generating_audio', 'composing_video', 'uploading'].includes(project.status)) && (
                  <ProgressTracker
                    progress={progress}
                    status={status}
                    message={message}
                    isConnected={isConnected}
                  />
                )}

                {/* Video Player */}
                {completedVideo && (
                  <div className="bg-white rounded-2xl shadow-lg p-6">
                    <div className="flex items-center justify-between mb-6">
                      <h2 className="text-2xl font-bold">Generated Video</h2>
                      <div className="flex gap-3">
                        <button
                          onClick={() => handleDownload(completedVideo.id)}
                          className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
                        >
                          <Download className="w-4 h-4" />
                          Download
                        </button>
                        <button className="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition">
                          <Share2 className="w-4 h-4" />
                          Share
                        </button>
                      </div>
                    </div>
                    
                    <VideoPlayer
                      url={completedVideo.file_url}
                      title={completedVideo.title}
                      duration={completedVideo.duration}
                    />

                    {/* Video Info */}
                    <div className="mt-6 grid grid-cols-3 gap-4 text-center">
                      <div className="p-4 bg-gray-50 rounded-xl">
                        <Eye className="w-5 h-5 mx-auto mb-2 text-blue-600" />
                        <div className="text-2xl font-bold">{completedVideo.views}</div>
                        <div className="text-sm text-gray-600">Views</div>
                      </div>
                      <div className="p-4 bg-gray-50 rounded-xl">
                        <Download className="w-5 h-5 mx-auto mb-2 text-green-600" />
                        <div className="text-2xl font-bold">{completedVideo.downloads}</div>
                        <div className="text-sm text-gray-600">Downloads</div>
                      </div>
                      <div className="p-4 bg-gray-50 rounded-xl">
                        <Play className="w-5 h-5 mx-auto mb-2 text-purple-600" />
                        <div className="text-2xl font-bold">
                          {Math.floor(completedVideo.duration / 60)}:{(completedVideo.duration % 60).toString().padStart(2, '0')}
                        </div>
                        <div className="text-sm text-gray-600">Duration</div>
                      </div>
                    </div>
                  </div>
                )}

                {/* Video History */}
                {videos.length > 1 && (
                  <div className="bg-white rounded-2xl shadow-lg p-6">
                    <h3 className="text-xl font-bold mb-4">Generation History</h3>
                    <div className="space-y-3">
                      {videos.map((video) => (
                        <div key={video.id} className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition">
                          <div>
                            <div className="font-medium">{video.title}</div>
                            <div className="text-sm text-gray-500">
                              {new Date(video.created_at).toLocaleString()}
                            </div>
                          </div>
                          <div className="flex items-center gap-3">
                            <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                              video.status === 'completed' 
                                ? 'bg-green-100 text-green-700'
                                : 'bg-gray-100 text-gray-700'
                            }`}>
                              {video.status}
                            </span>
                            {video.status === 'completed' && (
                              <button
                                onClick={() => handleDownload(video.id)}
                                className="text-blue-600 hover:text-blue-700"
                              >
                                <Download className="w-5 h-5" />
                              </button>
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Sidebar */}
              <div className="lg:col-span-1">
                <VideoConfigPanel config={config} onChange={setConfig} readOnly />
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default VideoEditor;
