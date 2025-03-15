import sqlite3
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

DB_PATH = os.path.join(os.getcwd(), "database_files", "sangeet_database_main.db")
PLAYLIST_DB_PATH = os.path.join(os.getcwd(), "database_files", "playlists.db")

# Initialize SQLite database for caching lyrics
def init_lyrics_db():
    """Initialize the lyrics cache database."""
    conn = sqlite3.connect(os.path.join(os.getcwd(), "database_files", "lyrics_cache.db"))
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS lyrics_cache (
        song_id TEXT PRIMARY KEY,
        lyrics TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()
    logger.info("Lyrics cache database initialized successfully")

# Master database initialization
def init_db():
    """Initialize the main database with all necessary tables."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    try:
        # User Authentication Tables
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                totp_secret TEXT,
                twofa_method TEXT DEFAULT 'none',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # User-specific Downloads
        c.execute("""
            CREATE TABLE IF NOT EXISTS user_downloads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                video_id TEXT NOT NULL,
                title TEXT,
                artist TEXT,
                album TEXT,
                path TEXT,
                downloaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # Listening History
        c.execute("""
            CREATE TABLE IF NOT EXISTS listening_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                song_id TEXT NOT NULL,
                title TEXT,
                artist TEXT,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ended_at TIMESTAMP,
                duration INTEGER,
                listened_duration INTEGER,
                completion_rate FLOAT,
                session_id TEXT,
                listen_type TEXT CHECK(listen_type IN ('full', 'partial', 'skip')) DEFAULT 'partial'
            )
        """)
        
        # User Statistics (optional, kept for compatibility)
        c.execute("""
            CREATE TABLE IF NOT EXISTS user_stats (
                user_id INTEGER PRIMARY KEY,
                total_plays INTEGER DEFAULT 0,
                total_listened_time INTEGER DEFAULT 0,
                favorite_song_id TEXT,
                favorite_artist TEXT,
                last_played TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # Session Management
        c.execute("""
            CREATE TABLE IF NOT EXISTS active_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                session_token TEXT UNIQUE NOT NULL,
                expires_at TIMESTAMP NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        
        # OTP Management
        c.execute("""
            CREATE TABLE IF NOT EXISTS pending_otps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                otp TEXT NOT NULL,
                purpose TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP NOT NULL
            )
        """)
        
        # Create indexes for performance
        c.execute("CREATE INDEX IF NOT EXISTS idx_user_downloads_user ON user_downloads(user_id)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_listening_history_user ON listening_history(user_id)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_listening_dates ON listening_history(started_at)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_listening_song ON listening_history(song_id)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_listening_completion ON listening_history(completion_rate)")
        
        conn.commit()
        logger.info("Main database initialized successfully")
        
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

# Playlist database initialization
def init_playlist_db():
    """Initialize the playlist database."""
    conn = sqlite3.connect(PLAYLIST_DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS playlists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT NOT NULL,
        is_public INTEGER DEFAULT 0,
        share_id TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS playlist_songs (
        playlist_id INTEGER,
        song_id TEXT,
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (playlist_id) REFERENCES playlists(id)
    )''')
    conn.commit()
    conn.close()
    logger.info("Playlist database initialized successfully")

