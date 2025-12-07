import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface ProjectState {
  currentProject: any | null;
  projects: any[];
}

const initialState: ProjectState = {
  currentProject: null,
  projects: [],
};

const projectSlice = createSlice({
  name: 'project',
  initialState,
  reducers: {
    setCurrentProject: (state, action: PayloadAction<any>) => {
      state.currentProject = action.payload;
    },
    setProjects: (state, action: PayloadAction<any[]>) => {
      state.projects = action.payload;
    },
  },
});

export const { setCurrentProject, setProjects } = projectSlice.actions;
export default projectSlice.reducer;
