🚀 Web Dev Final Project  

Project: FilmSpace: Beyond Watching  
Team: WebDeb-Project 💻  

👩‍💻 Team members:  
• Mukhtarkyzy Assem  
• Mukatay Nurdana  
• Toltay Azat  

---

🎯 FilmSpace: Beyond Watching  
Interactive Movie Experience Platform

---

📌 Project Description

FilmSpace is a full-stack web application developed as part of the Web Development (Angular + Django) course at KBTU.

Unlike traditional movie platforms, FilmSpace focuses on personalized and interactive movie discovery. Instead of simply browsing films, users engage in a guided cinematic experience through emotion-based recommendations, personality analysis, and social interaction.

The platform combines Angular frontend with Django REST Framework backend, using JWT authentication to provide secure and personalized user experiences.

---

🧠 Core Concept

👉 Users do not just search for movies  
👉 The system understands user preferences and emotions  
👉 The platform creates a cinematic journey

---

🔥 Key Features

---

### 🟢 1. Your Life → Movie Mapping

Users can describe their current emotional or life situation:

> “I feel lost studying abroad”

The system analyzes input and suggests relevant movies based on:
• mood tags  
• genres  
• themes  

This creates a personalized movie recommendation experience.

---

### 🟣 2. Personality Test & Taste DNA

Users take an interactive test to define their movie personality.

Example result:

Your cinema personality:  
🎭 Emotional Explorer

Taste DNA:  
• 40% Drama  
• 30% Sci-Fi  
• 30% Romance  

This profile is used to enhance recommendations and comparisons.

---

### 🔵 3. Social Match & Movie Interaction

Users can interact socially:

• Follow other users  
• Compare movie tastes  
• View compatibility score (e.g., 78% match)  
• Send movie recommendations  
• Create polls: “What should we watch?”  

---

### 🗳️ 4. Movie Poll System

Users can create polls to decide what to watch together.

• Add multiple movies  
• Vote on options  
• System determines winner  

---

### 📊 5. Reviews & Ratings

• Add, edit, delete reviews  
• Rate movies (1–5 stars)  
• View average ratings  

---

### 🎮 6. Gamification System

Users earn coins for activity:

• Writing reviews  
• Rating movies  
• Completing tests  

Levels:
• Beginner  
• Explorer  
• Film Expert  

---

## 🧱 Application Structure

### Pages:
1. Login / Register  
2. Home (interactive dashboard)  
3. Movies  
4. Movie Detail  
5. Personality Test  
6. Social / Match  
7. Profile  

---

## 🛠 Tech Stack  

| Layer       | Technology |
|------------|-----------|
| Frontend   | Angular, TypeScript, CSS |
| Backend    | Django, Django REST Framework |
| Auth       | JWT (SimpleJWT) |
| Database   | SQLite |
| HTTP       | Angular HttpClient |

---

## 📡 API Endpoints (Example)

| Method | Endpoint | Description |
|--------|--------|------------|
| POST | /auth/register/ | Register |
| POST | /auth/login/ | Login |
| GET | /movies/ | List movies |
| GET | /movies/:id/ | Movie details |
| POST | /reviews/ | Create review |
| POST | /emotion/ | Emotion-based recommendation |
| POST | /test/ | Submit personality test |
| GET | /match/:user_id/ | Get compatibility |
| POST | /polls/ | Create poll |
| POST | /polls/vote/ | Vote |

___
