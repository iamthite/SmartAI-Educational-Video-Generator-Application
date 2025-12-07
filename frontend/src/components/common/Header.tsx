import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-blue-600">
          EduVideoGen
        </Link>
        
        <nav className="flex gap-6">
          <Link to="/dashboard" className="text-gray-700 hover:text-blue-600">
            Dashboard
          </Link>
          <Link to="/create" className="text-gray-700 hover:text-blue-600">
            Create
          </Link>
        </nav>
      </div>
    </header>
  );
};

export default Header;
