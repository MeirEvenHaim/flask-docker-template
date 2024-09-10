import os

class Config:
    # Secret key for JWT
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    
    # Database settings for MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://username:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT settings
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'superjwtsecretkey')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expiration time in seconds
    
    # Redis settings
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # CORS settings
    CORS_ALLOW_ALL_ORIGINS = True
    
    # File upload settings (Pillow)
    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Docker configurations (if needed)
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
