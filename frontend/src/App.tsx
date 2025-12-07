// import React from 'react';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import { Provider } from 'react-redux';
// import { Toaster } from 'react-hot-toast';
// import { store } from './store';
// import Home from './pages/Home';
// import Dashboard from './pages/Dashboard';
// import CreateProject from './pages/CreateProject';
// import VideoEditor from './pages/VideoEditor';
// import Login from './pages/Login';
// import Analytics from './pages/Analytics';
// import Settings from './pages/Settings';
// import './App.css';

// function App() {
//   return (
//     <Provider store={store}>
//       <Router>
//         <Toaster position="top-right" />
//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/login" element={<Login />} />
//           <Route path="/dashboard" element={<Dashboard />} />
//           <Route path="/create" element={<CreateProject />} />
//           <Route path="/editor/:projectId" element={<VideoEditor />} />
//           <Route path="/analytics" element={<Analytics />} />
//           <Route path="/settings" element={<Settings />} />
//         </Routes>
//       </Router>
//     </Provider>
//   );
// }

// export default App;

// #================================================

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { Toaster } from 'react-hot-toast';
import { store } from './store/index';
import Home from './pages/Home.tsx';
import Dashboard from './pages/Dashboard.tsx';
import CreateProject from './pages/CreateProject.tsx';
import VideoEditor from './pages/VideoEditor.tsx';
import Login from './pages/Login.tsx';
import Analytics from './pages/Analytics.tsx';
import Settings from './pages/Settings.tsx';
import './App.css';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Toaster position="top-right" />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/create" element={<CreateProject />} />
          <Route path="/editor/:projectId" element={<VideoEditor />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;

