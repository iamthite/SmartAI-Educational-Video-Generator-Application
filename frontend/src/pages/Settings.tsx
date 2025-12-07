// frontend/src/pages/Settings.tsx
// ============================================

import React from 'react';
import Header from '../components/common/Header.tsx';

const Settings: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <div className="max-w-7xl mx-auto py-8 px-4">
        <h1 className="text-3xl font-bold">Settings</h1>
        <p className="text-gray-600 mt-2">Configure your preferences...</p>
      </div>
    </div>
  );
};

export default Settings;