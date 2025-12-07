// ============================================
// frontend/src/pages/Home.tsx - BEAUTIFUL LANDING
// ============================================
import React from 'react';
import { Link } from 'react-router-dom';
import { Video, Sparkles, BookOpen, Zap, Shield, Globe } from 'lucide-react';

const Home: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="fixed top-0 w-full bg-white/80 backdrop-blur-md shadow-sm z-50">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <Video className="w-8 h-8 text-blue-600" />
            <span className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              EduVideoGen
            </span>
          </div>
          <nav className="hidden md:flex gap-8">
            <a href="#features" className="text-gray-700 hover:text-blue-600 transition">Features</a>
            <a href="#how-it-works" className="text-gray-700 hover:text-blue-600 transition">How It Works</a>
            <a href="#pricing" className="text-gray-700 hover:text-blue-600 transition">Pricing</a>
          </nav>
          <Link
            to="/dashboard"
            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
          >
            Get Started
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full mb-6 animate-fade-in">
            <Sparkles className="w-4 h-4" />
            <span className="text-sm font-medium">AI-Powered Educational Videos</span>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 bg-clip-text text-transparent animate-fade-in">
            Transform Content into
            <br />
            Professional Videos
          </h1>
          
          <p className="text-xl text-gray-600 mb-12 max-w-3xl mx-auto animate-fade-in">
            Create engaging educational videos for students from 1st to 12th grade, 
            diploma, engineering, medical, and all educational fields using AI
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center animate-fade-in">
            <Link
              to="/create"
              className="bg-blue-600 text-white px-8 py-4 rounded-xl text-lg font-semibold hover:bg-blue-700 transition shadow-lg hover:shadow-xl"
            >
              Create Your First Video
            </Link>
            <a
              href="#demo"
              className="bg-white text-blue-600 px-8 py-4 rounded-xl text-lg font-semibold hover:bg-gray-50 transition shadow-lg border-2 border-blue-600"
            >
              Watch Demo
            </a>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mt-20 max-w-4xl mx-auto">
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600">50K+</div>
              <div className="text-gray-600 mt-2">Videos Created</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-purple-600">15K+</div>
              <div className="text-gray-600 mt-2">Educators</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-pink-600">4.9/5</div>
              <div className="text-gray-600 mt-2">User Rating</div>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-green-600">100%</div>
              <div className="text-gray-600 mt-2">AI Powered</div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="py-20 px-4 bg-white">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16">
            Powerful Features for{' '}
            <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              Every Educator
            </span>
          </h2>

          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: BookOpen,
                title: "Multi-Subject Support",
                description: "Create videos for any subject from Mathematics to Medical Sciences",
                color: "blue"
              },
              {
                icon: Zap,
                title: "Lightning Fast",
                description: "Generate professional videos in minutes, not hours",
                color: "yellow"
              },
              {
                icon: Globe,
                title: "Indian Languages",
                description: "Support for Hindi, Tamil, Telugu, Marathi and more",
                color: "green"
              },
              {
                icon: Sparkles,
                title: "AI-Powered",
                description: "Smart script generation and visual creation",
                color: "purple"
              },
              {
                icon: Shield,
                title: "High Quality",
                description: "HD to 4K video quality with professional narration",
                color: "red"
              },
              {
                icon: Video,
                title: "Customizable",
                description: "Full control over voice, style, and content",
                color: "indigo"
              }
            ].map((feature, index) => (
              <div
                key={index}
                className="p-8 rounded-2xl bg-gradient-to-br from-gray-50 to-white border border-gray-200 card-hover"
              >
                <div className={`w-14 h-14 rounded-xl bg-${feature.color}-100 flex items-center justify-center mb-6`}>
                  <feature.icon className={`w-7 h-7 text-${feature.color}-600`} />
                </div>
                <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section id="how-it-works" className="py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16">
            Create Videos in{' '}
            <span className="bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              4 Simple Steps
            </span>
          </h2>

          <div className="grid md:grid-cols-4 gap-8">
            {[
              {
                step: "1",
                title: "Upload Content",
                description: "Paste text or upload PDF, DOCX files"
              },
              {
                step: "2",
                title: "Configure",
                description: "Choose voice, language, and style"
              },
              {
                step: "3",
                title: "Generate",
                description: "AI creates script, visuals, and narration"
              },
              {
                step: "4",
                title: "Download",
                description: "Get your professional video ready"
              }
            ].map((item, index) => (
              <div key={index} className="text-center">
                <div className="w-16 h-16 rounded-full bg-gradient-to-r from-blue-600 to-purple-600 text-white text-2xl font-bold flex items-center justify-center mx-auto mb-4">
                  {item.step}
                </div>
                <h3 className="text-xl font-bold mb-2">{item.title}</h3>
                <p className="text-gray-600">{item.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 px-4 bg-gradient-to-r from-blue-600 to-purple-600">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold text-white mb-6">
            Ready to Transform Your Educational Content?
          </h2>
          <p className="text-xl text-blue-100 mb-8">
            Join thousands of educators creating amazing videos
          </p>
          <Link
            to="/create"
            className="inline-block bg-white text-blue-600 px-10 py-4 rounded-xl text-lg font-semibold hover:bg-gray-100 transition shadow-xl"
          >
            Start Creating Free
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12 px-4">
        <div className="max-w-7xl mx-auto text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Video className="w-6 h-6" />
            <span className="text-xl font-bold">EduVideoGen</span>
          </div>
          <p className="text-gray-400 mb-6">
            AI-Powered Educational Video Generation Platform
          </p>
          <div className="flex justify-center gap-8 text-sm text-gray-400">
            <a href="#" className="hover:text-white transition">Privacy</a>
            <a href="#" className="hover:text-white transition">Terms</a>
            <a href="#" className="hover:text-white transition">Contact</a>
            <a href="#" className="hover:text-white transition">Support</a>
          </div>
          <p className="text-gray-600 mt-8">© 2024 EduVideoGen. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default Home;


