import React from 'react';

interface TextEditorProps {
  value: string;
  onChange: (value: string) => void;
}

const TextEditor: React.FC<TextEditorProps> = ({ value, onChange }) => {
  return (
    <div>
      <label className="block text-sm font-medium mb-2">
        Content *
      </label>
      <textarea
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 min-h-[400px] font-mono"
        placeholder="Enter your educational content here...

Example:
Introduction to Machine Learning

Machine learning is a branch of artificial intelligence that focuses on...
"
      />
      <p className="text-sm text-gray-500 mt-2">
        Write or paste your educational content. The AI will structure it into a video.
      </p>
    </div>
  );
};

export default TextEditor;
