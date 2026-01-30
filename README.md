# 🎧 Spotify Roast

A fun web application that analyzes your Spotify listening habits and generates a humorous, AI-powered roast of your music taste.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- **OAuth 2.0 Integration**: Secure authentication with Spotify
- **Real-time Data Fetching**: Retrieves your top tracks and artists
- **AI-Powered Roasts**: Uses OpenAI's GPT models to generate witty, personalized roasts
- **Modern UI**: Clean, responsive design with Spotify-inspired aesthetics
- **Privacy-Focused**: No data storage - your information is only used to generate the roast

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3
- **APIs**: 
  - Spotify Web API
  - OpenAI API
- **Templating**: Jinja2
- **HTTP Client**: Requests
- **LLM Framework**: LangChain

## 📁 Project Structure

```
spotify-roast-app/
├── config/
│   └── settings.py          # Configuration and environment variables
├── models/
│   └── spotify_models.py    # Pydantic data models
├── services/
│   ├── spotify_service.py   # Spotify API interactions
│   └── roast_service.py     # LLM roast generation logic
├── static/
│   └── css/
│       └── style.css        # Stylesheet
├── templates/
│   ├── index.html           # Home page template
│   └── roast.html           # Roast result page template
├── main.py                  # FastAPI application entry point
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Spotify Developer Account
- OpenAI API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spotify-roast-app.git
   cd spotify-roast-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your credentials:
   ```env
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIFY_REDIRECT_URI=http://127.0.0.1:8000/callback
   OPENAI_API_KEY=your_openai_api_key
   ```

### Getting API Credentials

#### Spotify API
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Copy the **Client ID** and **Client Secret**
4. Add `http://127.0.0.1:8000/callback` to **Redirect URIs** in app settings

#### OpenAI API
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key to your `.env` file

### Running the Application

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`

## 📱 Usage

1. Visit `http://127.0.0.1:8000`
2. Click **"Login with Spotify"**
3. Authorize the application to access your Spotify data
4. Wait for the AI to analyze your music taste
5. Enjoy your personalized roast!
6. Share with friends (if you dare 😅)

## 🎯 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/login` | GET | Initiate Spotify OAuth flow |
| `/callback` | GET | OAuth callback handler |
| `/health` | GET | Health check endpoint |

## 🔒 Privacy & Security

- **No Data Storage**: Your Spotify data is only used to generate the roast and is not stored
- **Secure OAuth**: Uses OAuth 2.0 for secure authentication
- **Environment Variables**: Sensitive credentials are stored in environment variables

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Enhancement

- [ ] Add social sharing functionality
- [ ] Support for multiple languages
- [ ] User statistics dashboard
- [ ] Comparison feature (roast two users' tastes)
- [ ] Export roast as image
- [ ] Add more roast styles (gentle, brutal, poetic, etc.)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api)
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/)

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/spotify-roast-app](https://github.com/yourusername/spotify-roast-app)

---

Made with ❤️ and a bit of judgment 😌
