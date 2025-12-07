// ============================================
// frontend/src/components/video/ProgressTracker.tsx
// ============================================
import React from 'react';
import { CheckCircle, Circle, AlertCircle, Loader } from 'lucide-react';

interface ProgressTrackerProps {
  progress: number;
  status: string;
  message: string;
  isConnected: boolean;
}

const ProgressTracker: React.FC<ProgressTrackerProps> = ({ 
  progress, 
  status, 
  message,
  isConnected 
}) => {
  const steps = [
    { id: 'analyzing', label: 'Analyzing Content', range: [0, 20] },
    { id: 'generating_script', label: 'Generating Script', range: [20, 40] },
    { id: 'creating_visuals', label: 'Creating Visuals', range: [40, 60] },
    { id: 'generating_audio', label: 'Generating Audio', range: [60, 75] },
    { id: 'composing_video', label: 'Composing Video', range: [75, 95] },
    { id: 'uploading', label: 'Uploading', range: [95, 100] }
  ];

  const getStepStatus = (step: any) => {
    if (progress >= step.range[1]) return 'completed';
    if (status === step.id) return 'active';
    return 'pending';
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      {/* Connection Status */}
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold">Generating Video</h2>
        <div className="flex items-center gap-2">
          <div className={`w-2 h-2 rounded-full ${isConnected ? 'bg-green-500 animate-pulse' : 'bg-red-500'}`} />
          <span className="text-sm text-gray-600">
            {isConnected ? 'Connected' : 'Disconnected'}
          </span>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm font-medium text-gray-700">{message}</span>
          <span className="text-sm font-bold text-blue-600">{progress}%</span>
        </div>
        <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-blue-600 to-purple-600 rounded-full transition-all duration-500"
            style={{ width: `${progress}%` }}
          />
        </div>
      </div>

      {/* Steps */}
      <div className="space-y-4">
        {steps.map((step, index) => {
          const stepStatus = getStepStatus(step);
          return (
            <div
              key={step.id}
              className={`flex items-center gap-4 p-4 rounded-xl transition ${
                stepStatus === 'active' 
                  ? 'bg-blue-50 border-2 border-blue-200'
                  : stepStatus === 'completed'
                  ? 'bg-green-50'
                  : 'bg-gray-50'
              }`}
            >
              <div className="flex-shrink-0">
                {stepStatus === 'completed' ? (
                  <CheckCircle className="w-6 h-6 text-green-600" />
                ) : stepStatus === 'active' ? (
                  <Loader className="w-6 h-6 text-blue-600 animate-spin" />
                ) : (
                  <Circle className="w-6 h-6 text-gray-400" />
                )}
              </div>
              <div className="flex-1">
                <div className={`font-medium ${
                  stepStatus === 'active' ? 'text-blue-700' :
                  stepStatus === 'completed' ? 'text-green-700' :
                  'text-gray-500'
                }`}>
                  {step.label}
                </div>
                {stepStatus === 'active' && (
                  <div className="text-sm text-blue-600 mt-1">
                    In progress...
                  </div>
                )}
              </div>
              <div className="text-sm font-medium text-gray-500">
                {step.range[0]}-{step.range[1]}%
              </div>
            </div>
          );
        })}
      </div>

      {/* Estimated Time */}
      <div className="mt-6 p-4 bg-blue-50 rounded-xl">
        <div className="flex items-center justify-between">
          <span className="text-sm text-blue-700">Estimated time remaining</span>
          <span className="font-semibold text-blue-700">
            {Math.ceil((100 - progress) / 10)} minutes
          </span>
        </div>
      </div>
    </div>
  );
};

export default ProgressTracker;