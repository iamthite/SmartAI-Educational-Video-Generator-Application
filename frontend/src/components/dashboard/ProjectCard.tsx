import React from 'react';
import { Link } from 'react-router-dom';
import { Project } from '../../services/contentService';

interface ProjectCardProps {
  project: Project;
}

const ProjectCard: React.FC<ProjectCardProps> = ({ project }) => {
  const statusColors = {
    created: 'bg-gray-100 text-gray-800',
    processing: 'bg-blue-100 text-blue-800',
    completed: 'bg-green-100 text-green-800',
    failed: 'bg-red-100 text-red-800',
  };

  const statusColor = statusColors[project.status as keyof typeof statusColors] || statusColors.created;

  return (
    <Link to={`/editor/${project.id}`}>
      <div className="bg-white rounded-lg shadow-sm p-6 hover:shadow-md transition-shadow cursor-pointer">
        <div className="flex justify-between items-start mb-3">
          <h3 className="text-lg font-semibold">{project.title}</h3>
          <span className={`px-3 py-1 rounded-full text-xs font-medium ${statusColor}`}>
            {project.status}
          </span>
        </div>
        
        {project.description && (
          <p className="text-gray-600 text-sm mb-4 line-clamp-2">
            {project.description}
          </p>
        )}

        <div className="text-xs text-gray-500">
          Created: {new Date(project.created_at).toLocaleDateString()}
        </div>
      </div>
    </Link>
  );
};

export default ProjectCard;
