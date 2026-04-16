import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "IdeaFlow"
    @property
    def ASYNC_DATABASE_URL(self) -> str:
        url = os.getenv("DATABASE_URL", "")
        if not url:
            # Fallback for local development
            return "mysql+aiomysql://user:password@localhost/ideaflow"
        
        # Some providers give mysql:// but sqlalchemy async needs mysql+aiomysql://
        if url.startswith("mysql://"):
            url = url.replace("mysql://", "mysql+aiomysql://", 1)
        elif url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
            
        return url

    # Keeping this for backwards compatibility if needed elsewhere
    DATABASE_URL: str = "" 
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key-change-it")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    
    # Mail settings
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD", "")
    MAIL_FROM: str = os.getenv("MAIL_FROM", "")
    MAIL_PORT: int = int(os.getenv("MAIL_PORT", 587))
    MAIL_SERVER: str = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_FROM_NAME: str = os.getenv("MAIL_FROM_NAME", "IdeaFlow")
    MAIL_STARTTLS: bool = os.getenv("MAIL_STARTTLS", "True") == "True"
    MAIL_SSL_TLS: bool = os.getenv("MAIL_SSL_TLS", "False") == "True"

settings = Settings()
