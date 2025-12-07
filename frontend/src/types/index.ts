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
