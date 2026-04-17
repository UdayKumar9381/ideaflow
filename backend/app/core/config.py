import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "IdeaFlow"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        url = self.DATABASE_URL
        if not url:
            if os.getenv("RENDER"):
                return "MISSING_DATABASE_URL_PRODUCTION"
            return "mysql+aiomysql://root:Uday%40123@localhost/ideaflow"
        
        # Ensure we use the async driver
        if url.startswith("mysql://"):
            url = url.replace("mysql://", "mysql+aiomysql://", 1)
        elif url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        
        # Strip query parameters (like ?ssl-mode=...) that aiomysql doesn't support
        if "?" in url:
            url = url.split("?")[0]
            
        return url
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key-change-it")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    DB_USE_SSL: bool = os.getenv("DB_USE_SSL", "True").lower() == "true"
    
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
