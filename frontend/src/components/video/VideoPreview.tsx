import React, { useEffect, useRef } from 'react';

interface VideoPreviewProps {
  videoUrl: string;
}

const VideoPreview: React.FC<VideoPreviewProps> = ({ videoUrl }) => {
  const videoRef = useRef<HTMLVideoElement>(null);

  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-xl font-semibold mb-4">Video Preview</h2>
      
      <div className="aspect-video bg-black rounded-lg overflow-hidden">
        <video
          ref={videoRef}
          src={videoUrl}
          controls
          className="w-full h-full"
        >
          Your browser does not support the video tag.
        </video>
      </div>

      <div className="mt-4 flex gap-4">
        <button className="flex-1 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700">
          Download
        </button>
        <button className="flex-1 border border-gray-300 py-2 rounded-lg hover:bg-gray-50">
          Share
        </button>
      </div>
    </div>
  );
};

export default VideoPreview;
