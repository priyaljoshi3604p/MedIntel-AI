MedIntel AI — Frontend

This frontend is a Vite + React single-page app that provides a professional medical dashboard UI for a multimodal clinical intelligence platform.

Quick start

PowerShell:

```powershell
cd "C:\Users\ACER\Desktop\dowload , games , etc etc vishnudev------\MedIntel-AI\frontend"
Set-ExecutionPolicy -Scope Process Bypass -Force
npm install
npm run dev
```

Cmd.exe:

```cmd
cd /d "C:\Users\ACER\Desktop\dowload , games , etc etc vishnudev------\MedIntel-AI\frontend"
npm install
npm run dev
```

Build for production:

```bash
npm run build
```

What’s included

- A professional dashboard layout with sidebar, header, and content areas
- Accessible SVG icons (no emojis)
- Mock components for patient snapshot, risk meter, timeline, and recommendations
- Simple `api.js` placeholder to integrate backend calls

Next steps

- Connect `src/services/api.js` to your backend endpoints
- Add charts (Chart.js / Recharts) for real-time vitals and risk trends
- Implement authentication and role-based access control

License: MIT
