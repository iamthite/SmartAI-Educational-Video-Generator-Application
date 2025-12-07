// ============================================
// frontend/src/components/content/ContentUpload.tsx 
// ============================================

import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';

interface ContentUploadProps {
  onUpload: (file: File) => void;
  loading: boolean;
}

const ContentUpload: React.FC<ContentUploadProps> = ({ onUpload, loading }) => {
  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      onUpload(acceptedFiles[0]);
    }
  }, [onUpload]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'text/plain': ['.txt'],
    },
    maxFiles: 1,
    disabled: loading,
  });

  return (
    <div
      {...getRootProps()}
      className={`border-2 border-dashed rounded-lg p-12 text-center cursor-pointer transition-colors ${
        isDragActive
          ? 'border-blue-500 bg-blue-50'
          : 'border-gray-300 hover:border-gray-400'
      } ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
    >
      <input {...getInputProps()} />
      
      <svg
        className="mx-auto h-12 w-12 text-gray-400 mb-4"
        stroke="currentColor"
        fill="none"
        viewBox="0 0 48 48"
      >
        <path
          d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
          strokeWidth={2}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>

      {loading ? (
        <p className="text-lg text-gray-600">Uploading...</p>
      ) : isDragActive ? (
        <p className="text-lg text-blue-600">Drop the file here</p>
      ) : (
        <div>
          <p className="text-lg text-gray-600 mb-2">
            Drag & drop a file here, or click to select
          </p>
          <p className="text-sm text-gray-500">
            Supported: PDF, DOCX, TXT (Max 50MB)
          </p>
        </div>
      )}
    </div>
  );
};

export default ContentUpload;
