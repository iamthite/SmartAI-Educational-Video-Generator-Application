import { api } from './api';

export interface ContentUpload {
  title: string;
  description?: string;
  content: string;
  content_type?: string;
  config?: any;
}

export interface Project {
  id: number;
  title: string;
  description?: string;
  status: string;
  created_at: string;
  config?: any;
}

export const contentService = {
  uploadContent: async (data: ContentUpload) => {
    const response = await api.post('/content/upload', data);
    return response.data;
  },

  uploadFile: async (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await api.post('/content/upload-file', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  getProjects: async (): Promise<Project[]> => {
    const response = await api.get('/content/projects');
    return response.data;
  },

  getProject: async (projectId: number): Promise<Project> => {
    const response = await api.get(`/content/projects/${projectId}`);
    return response.data;
  },
};
