import { api } from './api';

export interface VideoGenerateResponse {
  message: string;
  task_id: string;
  project_id: number;
}

export interface TaskStatus {
  task_id: string;
  status: string;
  result?: any;
  error?: string;
  progress?: any;
}

export const videoService = {
  generateVideo: async (projectId: number): Promise<VideoGenerateResponse> => {
    const response = await api.post(`/video/generate/${projectId}`);
    return response.data;
  },

  getTaskStatus: async (taskId: string): Promise<TaskStatus> => {
    const response = await api.get(`/status/task/${taskId}`);
    return response.data;
  },

  getProjectVideos: async (projectId: number) => {
    const response = await api.get(`/video/projects/${projectId}/videos`);
    return response.data;
  },

  downloadVideo: async (videoId: number) => {
    const response = await api.get(`/video/${videoId}/download`);
    return response.data;
  },
};
