import { useState, useEffect } from 'react';
import { videoService } from '../services/videoService';

export const useVideoGenerator = () => {
  const [taskId, setTaskId] = useState<string | null>(null);
  const [status, setStatus] = useState<'idle' | 'generating' | 'completed' | 'failed'>('idle');
  const [progress, setProgress] = useState(0);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (taskId) {
      const interval = setInterval(async () => {
        try {
          const statusData = await videoService.getTaskStatus(taskId);
          
          if (statusData.status === 'SUCCESS') {
            setStatus('completed');
            setProgress(100);
            setVideoUrl(statusData.result?.video_url || null);
            clearInterval(interval);
          } else if (statusData.status === 'FAILURE') {
            setStatus('failed');
            setError(statusData.error || 'Generation failed');
            clearInterval(interval);
          } else if (statusData.status === 'PROGRESS') {
            const prog = statusData.progress?.percent || 0;
            setProgress(prog);
          }
        } catch (err) {
          console.error('Status check error:', err);
        }
      }, 3000);

      return () => clearInterval(interval);
    }
  }, [taskId]);

  const generateVideo = async (projectId: number) => {
    try {
      setStatus('generating');
      setProgress(0);
      setError(null);
      
      const response = await videoService.generateVideo(projectId);
      setTaskId(response.task_id);
    } catch (err: any) {
      setStatus('failed');
      setError(err.message || 'Failed to start generation');
    }
  };

  return {
    generateVideo,
    status,
    progress,
    videoUrl,
    error,
  };
};
