# Shiksha Saathi – Multi-Agent Educational Assistant
## Day 9 – Agent Handoff | Murf AI Voice Agent Challenge

---

## About The Project

Shiksha Saathi is an AI-powered educational assistant designed to help students with:

- Academic support
- Exam preparation
- Career guidance
- Learning assistance

For Day 9, the system was upgraded from a single-agent architecture to a multi-agent architecture where a Main Agent intelligently transfers conversations to specialized agents.

---

## Day 9 Objective

Implement Agent Handoff so that:

- General questions remain with the Main Agent
- Exam-related queries are routed to the Exam Specialist
- Career-related queries are routed to the Career Specialist
- User context is shared during handoff
- Specialists continue the conversation without asking users to repeat information

---

## Agents Implemented

### Main Agent

Responsibilities:

- Handles general educational queries
- Detects user intent
- Decides whether specialist support is required
- Initiates handoff

Example:

**User:** What is Shiksha Saathi?

**Main Agent:**
I can answer that myself.
Shiksha Saathi is an AI-powered educational support system.

---

### Exam Support Specialist

Responsibilities:

- Exam preparation
- Revision planning
- Study schedules
- Academic stress management

Example:

**User:** I am stressed about my exams

**Main Agent:**
I will connect you to our Exam Support Specialist.

**Exam Specialist:**
Hello! I am the Exam Support Specialist.

---

### Career Specialist

Responsibilities:

- Resume review
- LinkedIn optimization
- Internship guidance
- Interview preparation
- Career planning

Example:

**User:** Help me improve my LinkedIn profile

**Main Agent:**
I will connect you to our Career Specialist.

**Career Specialist:**
Hello! I am the Career Specialist.

---

## Agent Handoff Workflow

```text
User Query
    |
    ▼
Main Agent
    |
    ├── Exam Related → Exam Specialist
    |
    ├── Career Related → Career Specialist
    |
    └── General Query → Main Agent

Advanced Features
✅ Multiple Specialist Agents

Implemented separate:

Exam Specialist
Career Specialist
✅ Context Sharing

User information is passed to specialists without requiring repetition.

✅ Return to Main Agent

Specialists return the conversation after completing their task.

✅ Failed Handoff Handling

If a specialist is unavailable, the Main Agent continues assisting.

✅ Routing Validation

Multiple test cases were executed to verify correct agent selection.

🧪 Routing Test Results
User Query	Assigned Agent
What is Shiksha Saathi?	Main Agent
I am stressed about exams	Exam Specialist
Create a study plan	Exam Specialist
MBA exam preparation	Exam Specialist
Resume review	Career Specialist
Internship guidance	Career Specialist
LinkedIn optimization	Career Specialist
Interview preparation	Career Specialist
What services do you provide?	Main Agent
Career planning	Career Specialist
🛠 Tech Stack
Python
Multi-Agent Architecture
Agent Routing Logic
Murf AI Voice Agent Framework

Day 9 Achievement

✅ Main Agent Implementation

✅ Specialist Agent Creation

✅ Agent Handoff Mechanism

✅ Multi-Agent Routing

✅ Context Transfer

✅ Return-to-Main-Agent Flow

✅ Routing Validation Tests

#10DaysOfAIVoiceAgents #MurfFalcon #VoiceForBharat
