# 🌞🔋 AI-Powered Optimization & LLM Fault Detection in Smart Solar Lighting Systems


> MSc Artificial Intelligence Dissertation  
> Birmingham City University  
> Author: Salaheddine Chouikh  
> Academic Supervisor: Dr. 
> Industry Partner: Agamine Solar
> Industry Supervisor: Dr. Khalid Cherifi
---

## 🔍 Project Overview

This research explores the integration of AI in solar-powered smart lighting systems, in collaboration with Agamine Solar.  
The aim is to develop a dual-model architecture that enables:

1. **LLM-Powered Troubleshooting Assistant**  
   - Natural language query interface for LED performance logs  
   - Historical data analysis and fault explanation  
   - Custom-trained model using real pole sensor data

2. **Predictive Dimming Optimization**  
   - Energy-aware dimming adjustments based on battery health and predicted charge  
   - Simulation of multiple dimming scenarios using real field data  
   - Deep learning and/or reinforcement learning strategies under consideration

---

## 📊 Dataset

- Source: Agamine Solar’s smart controller logs (live + historical)
- Poles: 5 real-world installations + 2 simulation-ready test units
- Format: `.csv` logs containing battery %, dimming %, temperature, charge/discharge rate, etc.
- Logging frequency: Configurable (10–15 min intervals)

---

## 🧪 Experiments

### 🔋 Battery Health Evaluation
- Develop a discharge-based health metric  
- Compare battery performance across poles and dimming levels

### 💡 Dimming Trials
- Assign fixed dimming levels to test poles (60–100%)  
- Monitor overnight battery depletion and system uptime

### ⚠️ Fault Simulations
- Manual fault injections (e.g. cable unplugging, shading)  
- Used to train the LLM and anomaly detection systems

---

## 🧰 Codebase Structure

```
Agamine Solar RESEARCH/
├── Code/
│   ├── serial_data_logger.py         # Real-time serial logger with auto-versioning
│   ├── history/                      # Script version backups
│   └── ...
│
├── Data/
│   ├── LED_151/                      # Raw and cleaned CSV data from each pole
│   └── ...
│
├── Notes/
│   ├── Weekly_Objectives.md          # Planning & progress tracking
│   └── Daily_Log.docx                # Detailed researcher notes
│
├── Paper/
│   └── Drafts, citations, figures
│
├── Results/
│   └── Power BI screenshots, graph
│
└── Simulations/
    └── Experiment rotation matrix, fault scenarios
```

---

## 📍 Project Status

- ✅ System folder structured in OneDrive  
- ✅ Serial data logger functional and versioned  
- ✅ Experiment plan and simulation tracker prepared  
- ❎ Awaiting hardware access to begin live data logging  
- ❎ Dashboard development (Looker Studio or Power BI)  
- ❎ Battery health model and dimming optimization

---

## 📌 Aiming for Publication

This project is being conducted with the goal of producing a publishable scientific paper, with potential applications in:
- Energy-efficient public lighting
- AI-driven smart infrastructure
- Industrial language model use cases

---

## 📬 Contact

For collaboration, replication, or questions:

**Salaheddine Chouikh**  
Email: [salaheddine.chouikh@mail.bcu.ac.uk]  
GitHub: [github.com/Galuyoo](https://github.com/Galuyoo)
LinkedIn: [linkedin.com/in/salaheddine-chouikh](https://linkedin.com/in/salaheddine-chouikh)

**Industry Partner**
Industry Partner: [Agamine Solar](https://agaminesolar.com)
