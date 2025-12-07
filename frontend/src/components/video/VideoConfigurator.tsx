import React, { useState } from 'react';

interface VideoConfiguratorProps {
  onGenerate: () => void;
}

const VideoConfigurator: React.FC<VideoConfiguratorProps> = ({ onGenerate }) => {
  const [config, setConfig] = useState({
    voice: 'en-US-JennyNeural',
    style: 'professional',
    duration: 300,
    subtitles: true,
    music: false,
  });

  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-xl font-semibold mb-6">Video Settings</h2>

      <div className="space-y-6">
        {/* Voice Selection */}
        <div>
          <label className="block text-sm font-medium mb-2">Voice</label>
          <select
            value={config.voice}
            onChange={(e) => setConfig({ ...config, voice: e.target.value })}
            className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          >
            <option value="en-US-JennyNeural">Jenny (Female, US)</option>
            <option value="en-US-GuyNeural">Guy (Male, US)</option>
            <option value="en-GB-SoniaNeural">Sonia (Female, UK)</option>
            <option value="en-GB-RyanNeural">Ryan (Male, UK)</option>
          </select>
        </div>

        {/* Style Selection */}
        <div>
          <label className="block text-sm font-medium mb-2">Style</label>
          <select
            value={config.style}
            onChange={(e) => setConfig({ ...config, style: e.target.value })}
            className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          >
            <option value="professional">Professional</option>
            <option value="academic">Academic</option>
            <option value="casual">Casual</option>
            <option value="minimalist">Minimalist</option>
          </select>
        </div>

        {/* Duration */}
        <div>
          <label className="block text-sm font-medium mb-2">
            Target Duration: {Math.floor(config.duration / 60)}:{(config.duration % 60).toString().padStart(2, '0')}
          </label>
          <input
            type="range"
            min="60"
            max="600"
            step="30"
            value={config.duration}
            onChange={(e) => setConfig({ ...config, duration: parseInt(e.target.value) })}
            className="w-full"
          />
          <div className="flex justify-between text-xs text-gray-500 mt-1">
            <span>1 min</span>
            <span>10 min</span>
          </div>
        </div>

        {/* Subtitles */}
        <div className="flex items-center">
          <input
            type="checkbox"
            id="subtitles"
            checked={config.subtitles}
            onChange={(e) => setConfig({ ...config, subtitles: e.target.checked })}
            className="h-4 w-4 text-blue-600 rounded"
          />
          <label htmlFor="subtitles" className="ml-2 text-sm">
            Include Subtitles
          </label>
        </div>

        {/* Background Music */}
        <div className="flex items-center">
          <input
            type="checkbox"
            id="music"
            checked={config.music}
            onChange={(e) => setConfig({ ...config, music: e.target.checked })}
            className="h-4 w-4 text-blue-600 rounded"
          />
          <label htmlFor="music" className="ml-2 text-sm">
            Background Music
          </label>
        </div>

        {/* Generate Button */}
        <button
          onClick={onGenerate}
          className="w-full bg-blue-600 text-white py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors"
        >
          Generate Video
        </button>
      </div>
    </div>
  );
};

export default VideoConfigurator;
