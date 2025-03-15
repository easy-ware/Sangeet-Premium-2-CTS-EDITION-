# Sangeet Premium 🎵 V2 CTS

<p align="center">
  <img src="promo/logo.png" alt="Sangeet Premium Logo" width="600" height="400"/>
</p>

A modern, open-source music player with a stunning user interface, smart recommendations, and high-quality audio streaming - completely free forever.

## 📋 Table of Contents
- [Why Sangeet Premium?](#-why-sangeet-premium)
- [Features](#-features)
- [CTS Support](#-cts-support)
- [Requirements](#-requirements)
- [Installation](#-installation)
  - [Standard Installation](#standard-installation)
  - [Docker Installation](#docker-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

## 🌟 Why Sangeet Premium?
In today's digital music landscape, listeners face several challenges:
- Major streaming platforms charge premium fees for high-quality audio
- Expensive subscription models with restrictive features
- Limited control over music organization and playback
- Closed ecosystems that lock users into specific platforms
- Algorithmic recommendations that often prioritize promoted content

Sangeet Premium solves these issues by providing:
- Completely free, high-quality audio streaming
- Beautiful, responsive user interface
- Advanced music recommendation system
- Full control over your music library
- No ads, no subscriptions, no limitations
- Ability to share songs and embed them in other platforms

## ✨ Features
- **Stunning UI/UX**: Modern, intuitive interface with smooth animations
- **Smart Recommendations**: AI-powered music suggestions based on your listening habits
- **High-Quality Audio**: Crystal clear audio streaming with no compromises
- **Library Management**: Organize your music collection effortlessly
- **Cross-Platform**: Available on Windows, macOS, and Linux
- **Offline Mode**: Download your favorite tracks for offline listening
- **Last.fm Integration**: Scrobble your listening history
- **Customizable Themes**: Personalize your player's appearance
- **Lyrics Support**: Real-time synchronized lyrics
- **Smart Login System**: Secure and easy authentication
- **Playlist System**: Create, manage, and share playlists with friends
- **Songs Embed**: Embed your songs to other pages via iframe and customized
- **Share**: Share your favorite songs with friends
- **Download**: Download your favorite songs
- **CTS Support**: Conditional term support (see CTS section below)
- **Redis Integration**: For lightning speed performance

## 🔄 CTS Support
**CTS (Conditional Term Support)** is our approach to software maintenance that differs from traditional LTS (Long Term Support). While LTS provides regular updates for an extended period, CTS works as follows:

- Updates are provided conditionally rather than on a regular schedule
- Support is activated during major issues, security vulnerabilities, or significant changes in the ecosystem
- Similar to how discontinued software might still receive critical updates (like when Microsoft provides security patches for end-of-life products)
- The software remains functional but doesn't receive constant updates
- Development team reserves the right to provide updates when deemed necessary

This approach allows us to maintain the software's core functionality while focusing development resources on critical improvements rather than routine updates.

## 📋 Requirements
- Python 3.12 or higher
- Docker (for containerized deployment and Redis)

## 🚀 Installation

### Standard Installation

1. **Clone the repository**
```bash
git clone https://github.com/easy-ware/Sangeet-Premium-2-CTS-EDITION-.git
cd Sangeet-Premium-2-CTS-EDITION-
```

2. **Install dependencies**
```bash
pip install -r requirements/req.txt
```

3. **Configure environment variables**
Create a `/config/.env` file in the root directory with the following configuration:
```env
# ---------------------------
# SMTP Credentials
# ---------------------------
SMTP_USER=your_email@gmail.com         # Email address for SMTP authentication
SMTP_PASSWORD="your_app_password"      # SMTP password or app-specific password
SMTP_HOST=smtp.gmail.com               # SMTP server hostname
SMTP_PORT=587                          # SMTP server port number

# ---------------------------
# Local Music Configuration
# ---------------------------
LOCAL_SONGS_PATHS="/path/to/music"     # Primary path for local music files
music_path="/path/to/sangeet/music"    # Sangeet music directory path

# ---------------------------
# Server Configuration
# ---------------------------
SANGEET_BACKEND=http://localhost       # Backend server URL
PORT=80                                # Server port number

# ---------------------------
# Database Configuration
# ---------------------------
DB_PATH="database_files"               # Path to database files

# ---------------------------
# Authentication For Admin
# ---------------------------
admin_pass="your_secure_password"      # Admin password for authentication
```

5. **Run the application**
Start Redis:
```bash
docker compose -f redis.yaml up 
```
Then start the application:
```bash
python start_server.py
# or
python3 start_server.py
```

If you encounter any issues, try running the server directly:
```bash
python sangeet_server.py
# or
python3 sangeet_server.py
```

### Docker Installation (Recommended)

1. **Clone the repository**
```bash
git clone https://github.com/easy-ware/Sangeet-Premium-2-CTS-EDITION-.git
cd Sangeet-Premium-2-CTS-EDITION-
```

2. **Run with Docker**
```bash
docker compose up
```
For detached mode:
```bash
docker compose up -d
```

## ⚙️ Configuration

### Environment Variables
For detailed explanation of each environment variable, refer to the comments in the `.env` file template above.

### Directory Structure
- `/config` - Contains configuration files including `.env`
- `/database_files` - Stores SQLite database files
- `/music` - Directory for storing music files
- `/requirements` - Contains dependency files

## 🎮 Usage
Once the server is running, access the Sangeet Premium interface by navigating to:
- Local access: `http://localhost:80` (or the port you configured)
- Remote access: Use the Cloudflared tunnel URL generated during startup

> **Note:** For accessing Sangeet from other devices on your network, you must use the Cloudflared tunnel URL (ending with `.trycloudflare.com`). Direct access via local IP addresses (like 192.168.0.1) may not work properly.

Visit `/settings` to manage your server (enter admin password).

## 🔧 Troubleshooting

### Common Issues
1. **Server won't start**
   - Ensure Python 3.12+ is installed
   - Verify all dependencies are installed correctly
   - Check if the required ports are available

2. **Can't access from other devices**
   - Make sure to use the Cloudflared tunnel URL
   - Verify network settings and firewall configurations

### Reporting Issues
If you encounter any bugs or have feature requests, please report them on our [GitHub Issues page](https://github.com/easy-ware/Sangeet-Premium-2-CTS-EDITION-/issues) with the following information:
- Detailed description of the issue
- Steps to reproduce
- Expected vs. actual behavior
- System information (OS, Python version, etc.)
- Screenshots or logs (if applicable)

## 🤝 Contributing
We welcome contributions from the community! Here's how you can contribute:

1. **Fork the repository**
2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**
   ```bash
   git commit -m "Add feature: your feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

Please ensure your code follows our coding standards and includes appropriate documentation.

## 📜 License
This project is licensed under the Apache-2.0 license - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- All the open-source libraries and tools used in this project
- The community of contributors and users

## 📧 Contact
- GitHub: [Easy Ware](https://github.com/easy-ware)
- Issue Tracker: [GitHub Issues](https://github.com/easy-ware/Sangeet-Premium/issues)

---
<p align="center">
  Made with ❤️ by the Sangeet Premium Team and AI
</p>