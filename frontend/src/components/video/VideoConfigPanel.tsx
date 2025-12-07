// // ============================================
// // frontend/src/components/VideoConfigPanel.tsx 
// // ============================================

// import React from 'react';

// interface VideoConfigPanelProps {
//   config: any;
//   onChange: (config: any) => void;
//   readonly?: boolean;
// }

// const VideoConfigPanel: React.FC<VideoConfigPanelProps> = ({ config, onChange, readonly = false }) => {
//   return (
//     <div className="bg-white rounded-2xl shadow-lg p-6">
//       <h3 className="text-xl font-bold mb-6">Video Configuration</h3>
      
//       <div className="space-y-6">
//         {/* Education Level */}
//         <div>
//           <label className="block text-sm font-semibold mb-2">Education Level</label>
//           <select 
//             className="w-full px-4 py-2 border rounded-lg"
//             disabled={readonly}
//             value={config?.education_level?.level || '10th'}
//             onChange={(e) => onChange({
//               ...config,
//               education_level: { ...config.education_level, level: e.target.value }
//             })}
//           >
//             <option value="1st">Class 1st</option>
//             <option value="5th">Class 5th</option>
//             <option value="10th">Class 10th</option>
//             <option value="12th">Class 12th</option>
//             <option value="diploma">Diploma</option>
//             <option value="engineering">Engineering</option>
//             <option value="medical">Medical</option>
//           </select>
//         </div>

//         {/* Voice Gender */}
//         <div>
//           <label className="block text-sm font-semibold mb-2">Voice</label>
//           <div className="flex gap-4">
//             <label className="flex items-center">
//               <input
//                 type="radio"
//                 name="gender"
//                 value="male"
//                 disabled={readonly}
//                 checked={config?.voice?.gender === 'male'}
//                 onChange={(e) => onChange({
//                   ...config,
//                   voice: { ...config.voice, gender: e.target.value }
//                 })}
//                 className="mr-2"
//               />
//               Male
//             </label>
//             <label className="flex items-center">
//               <input
//                 type="radio"
//                 name="gender"
//                 value="female"
//                 disabled={readonly}
//                 checked={config?.voice?.gender === 'female'}
//                 onChange={(e) => onChange({
//                   ...config,
//                   voice: { ...config.voice, gender: e.target.value }
//                 })}
//                 className="mr-2"
//               />
//               Female
//             </label>
//           </div>
//         </div>

//         {/* Language */}
//         <div>
//           <label className="block text-sm font-semibold mb-2">Language</label>
//           <select 
//             className="w-full px-4 py-2 border rounded-lg"
//             disabled={readonly}
//             value={config?.voice?.language || 'en-IN'}
//             onChange={(e) => onChange({
//               ...config,
//               voice: { ...config.voice, language: e.target.value }
//             })}
//           >
//             <option value="en-IN">English (Indian)</option>
//             <option value="hi-IN">Hindi</option>
//             <option value="ta-IN">Tamil</option>
//             <option value="te-IN">Telugu</option>
//             <option value="mr-IN">Marathi</option>
//           </select>
//         </div>

//         {/* Quality */}
//         <div>
//           <label className="block text-sm font-semibold mb-2">Video Quality</label>
//           <select 
//             className="w-full px-4 py-2 border rounded-lg"
//             disabled={readonly}
//             value={config?.quality || '1080p'}
//             onChange={(e) => onChange({ ...config, quality: e.target.value })}
//           >
//             <option value="720p">720p (Fast)</option>
//             <option value="1080p">1080p (Standard)</option>
//             <option value="1440p">1440p (High Quality)</option>
//           </select>
//         </div>

//         {/* Subtitles */}
//         <div className="flex items-center">
//           <input
//             type="checkbox"
//             id="subtitles"
//             disabled={readonly}
//             checked={config?.include_subtitles !== false}
//             onChange={(e) => onChange({ ...config, include_subtitles: e.target.checked })}
//             className="mr-2"
//           />
//           <label htmlFor="subtitles" className="text-sm">Include Subtitles</label>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default VideoConfigPanel;



// ============================================
// frontend/src/components/VideoConfigPanel.tsx - ENHANCED WITH CONFIG (fixed imports/prop name)
// ============================================

import React from 'react';

interface VideoConfigPanelProps {
  config: any;
  onChange: (config: any) => void;
  readOnly?: boolean;
}

const VideoConfigPanel: React.FC<VideoConfigPanelProps> = ({ config, onChange, readOnly = false }) => {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h3 className="text-xl font-bold mb-6">Video Configuration</h3>
      
      <div className="space-y-6">
        {/* Education Level */}
        <div>
          <label className="block text-sm font-semibold mb-2">Education Level</label>
          <select 
            className="w-full px-4 py-2 border rounded-lg"
            disabled={readOnly}
            value={config?.education_level?.level || '10th'}
            onChange={(e) => onChange({
              ...config,
              education_level: { ...config.education_level, level: e.target.value }
            })}
          >
            <option value="1st">Class 1st</option>
            <option value="5th">Class 5th</option>
            <option value="10th">Class 10th</option>
            <option value="12th">Class 12th</option>
            <option value="diploma">Diploma</option>
            <option value="engineering">Engineering</option>
            <option value="medical">Medical</option>
          </select>
        </div>

        {/* Voice Gender */}
        <div>
          <label className="block text-sm font-semibold mb-2">Voice</label>
          <div className="flex gap-4">
            <label className="flex items-center">
              <input
                type="radio"
                name="gender"
                value="male"
                disabled={readOnly}
                checked={config?.voice?.gender === 'male'}
                onChange={(e) => onChange({
                  ...config,
                  voice: { ...config.voice, gender: e.target.value }
                })}
                className="mr-2"
              />
              Male
            </label>
            <label className="flex items-center">
              <input
                type="radio"
                name="gender"
                value="female"
                disabled={readOnly}
                checked={config?.voice?.gender === 'female'}
                onChange={(e) => onChange({
                  ...config,
                  voice: { ...config.voice, gender: e.target.value }
                })}
                className="mr-2"
              />
              Female
            </label>
          </div>
        </div>

        {/* Language */}
        <div>
          <label className="block text-sm font-semibold mb-2">Language</label>
          <select 
            className="w-full px-4 py-2 border rounded-lg"
            disabled={readOnly}
            value={config?.voice?.language || 'en-IN'}
            onChange={(e) => onChange({
              ...config,
              voice: { ...config.voice, language: e.target.value }
            })}
          >
            <option value="en-IN">English (Indian)</option>
            <option value="hi-IN">Hindi</option>
            <option value="ta-IN">Tamil</option>
            <option value="te-IN">Telugu</option>
            <option value="mr-IN">Marathi</option>
          </select>
        </div>

        {/* Quality */}
        <div>
          <label className="block text-sm font-semibold mb-2">Video Quality</label>
          <select 
            className="w-full px-4 py-2 border rounded-lg"
            disabled={readOnly}
            value={config?.quality || '1080p'}
            onChange={(e) => onChange({ ...config, quality: e.target.value })}
          >
            <option value="720p">720p (Fast)</option>
            <option value="1080p">1080p (Standard)</option>
            <option value="1440p">1440p (High Quality)</option>
          </select>
        </div>

        {/* Subtitles */}
        <div className="flex items-center">
          <input
            type="checkbox"
            id="subtitles"
            disabled={readOnly}
            checked={config?.include_subtitles !== false}
            onChange={(e) => onChange({ ...config, include_subtitles: e.target.checked })}
            className="mr-2"
          />
          <label htmlFor="subtitles" className="text-sm">Include Subtitles</label>
        </div>
      </div>
    </div>
  );
};

export default VideoConfigPanel;
