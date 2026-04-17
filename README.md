# 🌌 IdeaFlow – The Cinematic Architect's Workspace

[![Live Demo (Frontend)](https://img.shields.io/badge/Vercel-View_Live_Demo-white?style=for-the-badge&logo=vercel&logoColor=black)](https://ideaflow-taupe.vercel.app/)
[![Backend API](https://img.shields.io/badge/Render-API_Status-green?style=for-the-badge&logo=render&logoColor=white)](https://ideaflow-1-3dh9.onrender.com/health)

> **"Where the void meets vision."**  
> IdeaFlow is a full-stack creative engine designed to capture, structure, and accelerate breakthroughs within a high-performance, cinematic 3D environment.

---

## 🏗️ Clean Architecture

IdeaFlow is built on a modular, decoupled architecture designed for scale and high performance.

### **1. The Presentation Layer (3DVERSE)**
Built with **React 19** and **Three.js**, the frontend is not just a UI, but a spatially conscious environment.
- **Framework**: Vite + React (TypeScript)
- **3D Engine**: `@react-three/fiber` & `@react-three/drei`
- **Design System**: Tailwind CSS v4 utilizing custom design tokens and silver/black contrast palettes.
- **State Management**: React Context API + Axios Interceptors for centralized session handling.

### **2. The Logic Engine (Backend)**
A high-velocity **FastAPI** service optimized for asynchronous traffic and AI integration.
- **Framework**: Python 3.11+ (FastAPI)
- **Database Logic**: **SQLAlchemy 2.0 (Async)** with `aiomysql` for non-blocking database operations.
- **Security**: JWT (OAuth2) with salted `Bcrypt` password hashing.
- **Migrations**: Alembic for persistent version control.

### **3. The Data Persistence Layer**
- **Cloud Database**: Aiven MySQL (Managed Service) with SSL-enforced connectivity.
- **Schema Management**: Strictly typed pydantic models ensuring data integrity across the stack.

---

## 🦾 Core Functionality & Features

### **🤖 AI Cyber Companion**
A stateful AI engine integrated natively into the workspace.
- **Contextual Awareness**: Analyzes your current projects and ideas to offer real-time insights.
- **High Performance**: Powered by **Groq**, delivering low-latency responses via a dedicated backend service.

### **💡 Automated Idea Incubation**
- **Dynamic Conception**: Generate structured project concepts from simple keywords using AI.
- **Atomic Tracking**: Full CRUD management of your ideas with real-time status persistence.

### **🏁 Hackathon Velocity Tracker**
- **Sprint Management**: Organize multiple projects with visual status badges and priority tags.
- **Deadline Awareness**: Real-time "Days Left" calculations with visual urgency indicators.

### **📝 Notion-Style Documents**
- **Focused Writing**: A minimalist markdown-compatible editor for deep dive documentation.
- **Autosave Engine**: Your creative context is never lost, even across sessions.

---

## 📚 Technical Terminology

- **3DVERSE**: The immersive space where technical logic meets cinematic aesthetics.
- **Total Site Blackout**: A design philosophy minimizing visual noise through pure obsidian backgrounds and glass UI.
- **Glassmorphism**: UI components with high refraction (`backdrop-blur-3xl`) that create a "frosted obsidian" look.
- **Atomic Persistence**: The principle of ensuring every backend operation is handled asynchronously to prevent UI lag.

---

## 🚀 Future Roadmap & Improvements

- [ ] **Spatial Reality (AR)**: Optimizing the 3DVERSE for spatial computing environments (Apple Vision Pro/Meta Quest).
- [ ] **Collaborative Sprints**: Real-time websocket-based collaboration for creative teams.
- [ ] **AI Asset Generation**: Using Generative AI to automatically create 3D assets based on your captured ideas.
- [ ] **Mobile Native Sync**: A flutter-based companion app for capturing ideas on the move with biometric security.

---

## 🛠️ Quick Start

### **1. Backend Setup**
```bash
cd backend
pip install -r requirements.txt
# Set DATABASE_URL in .env (Aiven MySQL URI)
uvicorn app.main:app --reload
```

### **2. Frontend Setup**
```bash
cd frontend
npm install
# Set NEXT_PUBLIC_API_URL in .env
npm run dev
```

---

*Engineered for the elite creative mind.*  
🌌 **IdeaFlow Engineering Team**
