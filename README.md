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

## Advanced Features

### ✅ Multiple Specialist Agents

Implemented separate specialist agents for different domains:

- Exam Specialist
- Career Specialist

Each specialist handles queries related to its area of expertise and receives the conversation through an intelligent handoff process.

---

### ✅ Context Sharing

User information and query context are passed directly to specialists without requiring users to repeat their requests.

**Example:**

User: I am stressed about my MBA exams.

Main Agent transfers the query directly to the Exam Specialist while preserving the original context.

---

### ✅ Return to Main Agent

After providing specialized assistance, the conversation can be returned to the Main Agent for handling general educational queries.

---

### ✅ Failed Handoff Handling

If a specialist is unavailable or a handoff cannot be completed successfully, the Main Agent continues assisting the user instead of ending the conversation.

---

### ✅ Routing Validation

Multiple test cases were executed to verify that user queries are routed to the correct agent.

---

## 🧪 Routing Test Results

| User Query | Assigned Agent |
|------------|---------------|
| What is Shiksha Saathi? | Main Agent |
| I am stressed about exams | Exam Specialist |
| Create a study plan | Exam Specialist |
| MBA exam preparation | Exam Specialist |
| Resume review | Career Specialist |
| Internship guidance | Career Specialist |
| LinkedIn optimization | Career Specialist |
| Interview preparation | Career Specialist |
| What services do you provide? | Main Agent |
| Career planning | Career Specialist |

---

## 🛠 Tech Stack

- Python
- Multi-Agent Architecture
- Agent Routing Logic
- Murf AI Voice Agent Framework

---

## Day 9 Achievement

Successfully implemented:

- ✅ Main Agent
- ✅ Exam Specialist Agent
- ✅ Career Specialist Agent
- ✅ Agent Handoff Mechanism
- ✅ Multi-Agent Routing
- ✅ Context Transfer
- ✅ Return-to-Main-Agent Flow
- ✅ Failed Handoff Handling
- ✅ Routing Validation Tests

---

## Conclusion

The Day 9 implementation successfully demonstrates a Multi-Agent Educational Assistant capable of intelligently routing user requests to specialized agents while maintaining conversation context and ensuring a seamless user experience.

---

#10DaysOfAIVoiceAgents  
#MurfFalcon  
#VoiceForBharat
