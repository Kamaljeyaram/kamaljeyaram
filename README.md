<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="Kamal Jeyaram — building AI agents that see, read and act" src="assets/banner-light.svg" width="100%">
</picture>

<br>

I build AI agents and the parts they're made of. **Perception** turns cameras and documents into structured signals. **Reasoning** combines LLMs with retrieval and knows when it isn't confident. **Action** reaches people through tools, APIs, bots and apps.

<p>
  <a href="https://kamal-jeyaram.vercel.app"><img alt="Portfolio" src="https://img.shields.io/badge/PORTFOLIO-FF4D2E?style=for-the-badge&logo=vercel&logoColor=111111"></a>
  <a href="https://github.com/Kamaljeyaram?tab=repositories"><img alt="Repositories" src="https://img.shields.io/badge/REPOSITORIES-111111?style=for-the-badge&logo=github&logoColor=F2EFE8"></a>
</p>

<br>

## The loop

| | Stage | What it means in my work |
|:-:|---|---|
| `01` | **Perceive** | Vision models and OCR that turn video, faces and documents into data an agent can use |
| `02` | **Reason** | LLMs grounded with retrieval, confidence thresholds and provenance, so the system knows when to look further |
| `03` | **Act** | Tool calls, FastAPI services, bots and mobile or web apps that put the result in front of people |

<br>

## Reason · LLM & agentic systems

<table>
<tr>
<td width="34%" valign="top">

**[DeepBlue](https://github.com/Kamaljeyaram/deepblue)**<br>
<sub>FAISS · Gemini · Tavily · FastAPI</sub>

</td>
<td valign="top">

A transaction categorizer that decides what to do next. It checks its own memory first, a FAISS index of labelled examples. When the match falls below a confidence threshold, it calls a web-search tool for context and lets Gemini make the final call.

</td>
</tr>
<tr>
<td width="34%" valign="top">

**[Resume Analyzer](https://github.com/Kamaljeyaram/ResumeAnalyzer)**<br>
<sub>PaddleOCR · Ollama · PyMuPDF</sub>

</td>
<td valign="top">

Document intelligence with a local LLM. PDF, DOCX and scanned resumes become structured JSON. It reads native text first, falls back to OCR only when needed, and keeps models warm between runs so batches stay fast.

</td>
</tr>
<tr>
<td width="34%" valign="top">

**[Candidate Data Transformer](https://github.com/Kamaljeyaram/eightfold_AI)**<br>
<sub>Python · Pydantic</sub>

</td>
<td valign="top">

A grounded data layer for hiring systems. It merges CSV exports, ATS JSON, resumes and recruiter notes into one validated profile, and tracks the source and a confidence score for every field. Agents can then trust the data and explain where it came from.

</td>
</tr>
</table>

<br>

## Perceive · computer vision

<table>
<tr>
<td width="34%" valign="top">

**[Fire & Smoke Detection](https://github.com/Kamaljeyaram/smokeandfiredetection)**<br>
<sub>YOLO · PyTorch · FastAPI</sub>

</td>
<td valign="top">

Two YOLO models, one for fire and one for smoke, run as an ensemble with their boxes merged by NMS. A FastAPI service accepts images or video and returns annotated results.

</td>
</tr>
<tr>
<td width="34%" valign="top">

**[Workplace Monitoring](https://github.com/Kamaljeyaram/Workplace_monitoring)**<br>
<sub>InsightFace · FAISS · ONNX</sub>

</td>
<td valign="top">

Real-time face recognition with region-of-interest tracking. It identifies each person in a zone you draw on a live feed and logs how long they stay.

</td>
</tr>
<tr>
<td width="34%" valign="top">

**[EmotiSense](https://github.com/Kamaljeyaram/emosense_final)**<br>
<sub>DeepFace · React · Chart.js</sub>

</td>
<td valign="top">

Classroom emotion analytics. DeepFace emotion recognition feeds a dashboard organized by department and section. Related experiments: [facial_emotion](https://github.com/Kamaljeyaram/facial_emotion) and [emosense_deepface](https://github.com/Kamaljeyaram/emosense_deepface).

</td>
</tr>
</table>

<br>

## Act · tools, APIs & apps

| Project | What it does | Stack |
|---|---|---|
| [Serverless Telegram FAQ Bot](https://github.com/Kamaljeyaram/Serverless-Telegram-FAQ-Bot-using-AWS) | Conversational bot answering from a serverless backend | Lambda · API Gateway · DynamoDB |
| [Voice Call Backend](https://github.com/Kamaljeyaram/VoiceCall_Backend) | Programmable voice calling API | Express · Twilio |
| [EduGuide](https://github.com/Kamaljeyaram/eduguide) | Learning app with real-time quizzes and PDF export | Flutter · Firebase · Socket.IO |
| [Deep Doctor](https://github.com/Kamaljeyaram/deep_doctor) | Doctors' portal app with built-in calling | Flutter · Firebase · Agora |
| [Health Stream Dashboard](https://github.com/Kamaljeyaram/Matrix) · [live](https://matrix-alpha-ebon.vercel.app) | Real-time health metrics dashboard | React · TypeScript |
| [Aquaponics](https://github.com/Kamaljeyaram/Aquaponics) · [app](https://github.com/Kamaljeyaram/aquaponics_app) | Monitoring dashboard and companion mobile app | React · Expo |
| [Book Backend](https://github.com/Kamaljeyaram/book-backend) | REST API with search, paging and PDF upload | Node · Express |
| [Freelance](https://github.com/Kamaljeyaram/freelance) · [live](https://freelance-beta-ten.vercel.app) | Freelance services site | Vue 3 · Vite |

<br>

## Toolbox

**LLMs & agents:** Gemini · Ollama · sentence-transformers · FAISS · Tavily · Pydantic<br>
**Vision:** YOLO · InsightFace · DeepFace · PaddleOCR · OpenCV

<p>
  <img alt="Languages" src="https://skillicons.dev/icons?i=python,ts,js,dart&theme=dark">
  &nbsp;&nbsp;
  <img alt="ML" src="https://skillicons.dev/icons?i=pytorch,opencv&theme=dark">
  &nbsp;&nbsp;
  <img alt="Backend and cloud" src="https://skillicons.dev/icons?i=fastapi,nodejs,express,aws,firebase&theme=dark">
  &nbsp;&nbsp;
  <img alt="Apps" src="https://skillicons.dev/icons?i=react,vue,flutter,tailwind&theme=dark">
</p>

<br>

## Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kamaljeyaram/kamaljeyaram/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kamaljeyaram/kamaljeyaram/output/github-snake.svg">
  <img alt="Contribution graph animation" src="https://raw.githubusercontent.com/Kamaljeyaram/kamaljeyaram/output/github-snake.svg" width="100%">
</picture>

<br>

<sub>PERCEIVE → REASON → ACT ↻ &nbsp;·&nbsp; If you're building agents too, open an issue on any repo and say hello.</sub>
