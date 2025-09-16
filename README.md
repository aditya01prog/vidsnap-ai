Flask Video Reel Automation App
===============================

Description
-----------
This is a Flask-based web application that automates the generation of short video reels.
It integrates the ElevenLabs API for AI-generated audio, uses ffmpeg for media processing,
and displays the generated reels in a gallery. The project demonstrates backend development,
API integration, and automation skills.

Features
--------
- Generate video reels automatically.
- Integrate AI voice generation with ElevenLabs API.
- Process media using ffmpeg.
- View and manage generated reels in a gallery interface.
- Secure handling of environment variables and API keys.

Technologies Used
-----------------
- Python (Flask)
- ElevenLabs API
- ffmpeg
- HTML/CSS/JavaScript (for the gallery frontend)

Setup Instructions
------------------
1. Clone the repository:
   git clone https://github.com/yourusername/your-repo-name.git

2. Navigate into the project folder:
   cd your-repo-name

3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # For Unix/macOS
   venv\Scripts\activate      # For Windows

4. Install dependencies:
   pip install -r requirements.txt

5. Create a `.env` file in the root directory and add your API keys and configurations:
   FLASK_APP=app.py
   FLASK_ENV=development
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

6. Ensure `ffmpeg` is installed and available in your system's PATH.

7. Run the application:
   flask run

8. Open your browser and go to `http://127.0.0.1:5000` to start using the app.

Environment Variables
--------------------
- `ELEVENLABS_API_KEY`: API key for ElevenLabs voice synthesis.
- Other optional configurations can be added in `.env` as needed.

Important Notes
---------------
✔ Do not commit your `.env` file or any sensitive keys to the repository.  
✔ Add media output folders like `/media` or `/output` to `.gitignore`.  
✔ ffmpeg must be installed separately on your system.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
-------
For issues or contributions, please open an issue or create a pull request on GitHub.

