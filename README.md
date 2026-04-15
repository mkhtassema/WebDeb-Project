🚀 Web Dev Final Project  

Project: FilmSpace    

👩‍💻 Team members:  
• Mukhtarkyzy Assem  
• Mukatay Nurdana  
• Toltay Azat  

---

🎯 FilmSpace  
Smart Movie Discovery & Social Review Platform

---

📌 Project Description

FilmSpace is a full-stack web application developed as part of the Web Development (Angular + Django) course at KBTU.  

Unlike basic movie review platforms, FilmSpace combines personalized recommendations, social interaction, and interactive decision-making tools to create a more engaging user experience.  

Users can not only explore movies and leave reviews, but also track their watch history, follow other users, receive recommendations based on their preferences, and participate in movie selection polls.  

The application is built using an Angular frontend and a Django REST Framework backend, with JWT authentication обеспечивающим secure and personalized access.

---

👤 User Functionality

### 1. 🔐 Authentication & Personal Dashboard

Users can register and log in using JWT authentication.  

After login, each user accesses a personalized dashboard displaying:  
📌 Recommended movies based on ratings  
🎬 Popular and recently added movies  
👥 Activity from followed users  
🗳️ Active movie polls  

---

### 2. 🎥 Movie Browsing & Reviews

Users can:  
• Browse a list of movies  
• View detailed movie pages  
• Leave reviews and ratings (1–5 stars)  
• Edit or delete their reviews  

Each movie page includes:  
⭐ Average rating  
👥 Number of users who rated  
📝 User reviews  

---

### 3. 📌 Watchlist & Watched System

Users can manage their personal movie activity:  

➕ Add movies to Watchlist (Want to Watch)  
✅ Mark movies as Watched  
❌ Remove movies from lists  

This transforms the platform into a movie tracking system.

---

### 4. 🧠 Personalized Recommendation System

FilmSpace provides dynamic movie recommendations based on user behavior.  

The system analyzes:  
• User ratings  
• Preferred genres  

And suggests:  
🎯 Movies similar to highly rated ones  

---

### 5. 👥 Follow System & Social Interaction

Users can interact with each other through a social system:  

• Follow / Unfollow users  
• View other users’ profiles  
• See their reviews and ratings  

Optional feed includes:  
📰 Recent activity (e.g., “User rated Inception 5⭐”)  

---

### 6. 🗳️ Movie Poll System

Users can create polls to decide what to watch:  

Poll creation includes:  
📋 Poll title  
🎬 List of movies  
👥 Voting by users  

System features:  
✔ Vote for a movie  
🏆 Display winning option  

This adds interactive group decision-making to the platform.

---

### 7. 📊 Smart Rating Statistics

Each movie includes analytical insights:  

• ⭐ Average rating  
• 👥 Total number of ratings  
• 🟢 User’s personal rating  

This enhances the user experience with data-driven feedback.

---

## 🔥 Features

### Authentication
• JWT-based login & registration  
• HTTP Interceptor for attaching tokens  
• Protected routes  

### Movies
• List & detail views  
• Review system (CRUD)  
• Rating system  

### User Features
• Watchlist & watched tracking  
• Personalized recommendations  
• Follow system  

### Social & Interactive
• Movie polls  
• User activity  

### Analytics
• Smart rating statistics  

---

## 🛠 Tech Stack  

| Layer       | Technology |
|------------|-----------|
| Frontend   | Angular, TypeScript, CSS |
| Backend    | Django, Django REST Framework |
| Auth       | JWT (SimpleJWT) |
| Database   | SQLite / PostgreSQL |
| HTTP       | Angular HttpClient + Interceptors |

---

## 📡 Example API Endpoints  

| Method | Endpoint | Description |
|--------|--------|------------|
| POST | /auth/register/ | Register user |
| POST | /auth/login/ | Login |
| POST | /auth/logout/ | Logout |
| GET | /movies/ | Get all movies |
| GET | /movies/:id/ | Movie details |
| POST | /reviews/ | Create review |
| GET | /watchlist/ | Get user watchlist |
| POST | /follow/ | Follow user |
| GET | /recommendations/ | Get recommendations |
| POST | /polls/ | Create poll |
| POST | /polls/vote/ | Vote in poll |
