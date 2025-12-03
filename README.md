# PawMatch

PawMatch is a web application built with Flask that allows registered users to create profiles for their dogs, browse other dogs, and find matches based on location, breed, size, and other preferences. The project aims to be a fun, community-driven platform for dog owners, and is structured to support future enhancements like chat, AI-powered dog bios, and more.

## Features (Implemented & Planned)

**Implemented:**
- User registration and login (authentication via Flask-Login)  
- Ability for logged-in users to create and manage their dog profiles  
- Browsing of all dog profiles (public view)  
- Basic matching recommendations by city  
- Clean frontend built with Flask + Jinja templates + HTML/CSS  

**Planned / Coming soon:**
- AI-powered features (e.g., automatic generation of dog bios or “ice-breaker” messages)  
- Real-time chat between matched users  
- Swipe-style matching UI  
- Email verification and password reset  
- Improved matching algorithm (filter by breed, size, temperament, distance radius)  
- Containerization (Docker) and cloud deployment (e.g., Render / Cloud Run)  
- REST API support for external clients / mobile apps  

## Tech Stack

- **Backend:** Flask (Python)  
- **Database:** SQLite for development (can be easily switched to PostgreSQL or MySQL)  
- **ORM:** SQLAlchemy  
- **Authentication:** Flask-Login  
- **Frontend:** Jinja2 templates, HTML, CSS  
- **Optional / future:** MongoDB (for logs / analytics), AI models / APIs for bio generation  

## Project Structure

```
pawmatch/
│
├── app/                # Main application package
│   ├── routes/         # Flask route handlers (auth, dog creation, browsing, matching)
│   ├── models/         # SQLAlchemy models (User/Owner, Dog, …)
│   ├── templates/      # HTML templates (Jinja2)
│   ├── static/         # CSS
│   ├── extensions.py   # DB / login manager initialization
│   └── config.py       # Configuration settings
│
├── requirements.txt    # Python dependencies
└── run.py              # Entry point to run the app
```

## Setup & Running Locally

1. Clone the repository  
   ```bash
   git clone https://github.com/CodeOn-Shyam/pawmatch.git
   cd pawmatch
   ```

2. Create and activate a virtual environment  
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application  
   ```bash
   python run.py
   ```

5. Open your browser and navigate to  
   ```
   http://127.0.0.1:5000/
   ```

## How to Contribute

Contributions are welcome! Whether you want to fix bugs, add new features, improve UI, or help with documentation — your help is appreciated.

1. Fork the repository  
2. Create a new branch for your feature or fix  
   ```bash
   git checkout -b feature/your-feature-name
   ```  
3. Make your changes and commit them with a clear message  
4. Push to your fork and open a Pull Request (PR) against the `main` branch  
5. Ensure that your code is clean and follows the existing style  
6. If you're adding a new feature, consider adding documentation (or update README)  

### Ideas for Contribution

- Add AI-powered dog bio generator (backed by an LLM or simple template logic)  
- Implement a more advanced matching algorithm (based on breed, size, distance, etc.)  
- Add user profile pictures and dog pictures (file upload, image storage)  
- Add test suite (unit tests for routes, models)  
- Add REST API endpoints (so external clients / mobile apps can use the backend)  
- Dockerization and deployment configuration  

## License & Community Guidelines

PawMatch is licensed under the MIT License, enabling open collaboration and reuse.

The project includes established guidelines for contributions and responsible participation. Please review the following documents before submitting changes or opening discussions:

- LICENSE
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md

We look forward to contributions from the community and welcome new ideas, improvements, and feature suggestions.


