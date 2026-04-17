from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import time
import logging
import traceback

# Correct imports
from app.core.database import get_db, engine, Base
from app.core.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

app = FastAPI(title="IdeaFlow API", redirect_slashes=False)

# ------------------- CORS HEADERS UTILITY -------------------
def get_cors_headers(request: Request):
    origin = request.headers.get("origin")
    return {
        "Access-Control-Allow-Origin": origin if origin else "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Headers": "*",
    }

# ------------------- EXCEPTION HANDLERS -------------------

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"CRITICAL ERROR: {type(exc).__name__}: {str(exc)}")
    logger.error(traceback.format_exc())
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error",
            "error_type": type(exc).__name__,
            "error_msg": str(exc),
            "path": request.url.path
        },
        headers=get_cors_headers(request)
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "path": request.url.path},
        headers=get_cors_headers(request)
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body, "path": request.url.path},
        headers=get_cors_headers(request)
    )

# ------------------- MIDDLEWARE -------------------

@app.middleware("http")
async def log_origin_header(request: Request, call_next):
    origin = request.headers.get("origin")
    method = request.method
    path = request.url.path

    if origin:
        logger.info(f"{method} {path} from {origin}")
    else:
        logger.info(f"{method} {path} (No Origin)")

    response = await call_next(request)
    return response

# ✅ FIXED CORS (NO trailing slash)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://creator-hub-frontend-nine.vercel.app",
        "https://ideaflow-f.vercel.app",
        "https://ideaflow-lyart.vercel.app",
        "https://ideaflow-taupe.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- ROUTES -------------------

from app.routes import auth, ideas, ai, notes, projects, checklist

app.include_router(auth.router)
app.include_router(ideas.router)
app.include_router(ai.router)
app.include_router(notes.router)
app.include_router(projects.router)
app.include_router(checklist.router)

# ------------------- STARTUP -------------------

@app.on_event("startup")
async def startup_event():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Tables created successfully")
    except Exception as e:
        print("DB Error:", e)

# ------------------- ROUTES -------------------

@app.get("/")
async def root():
    return {
        "message": "IdeaFlow API is running",
        "docs": "/docs",
        "status": "online"
    }

@app.get("/health")
async def health_check(request: Request, db: AsyncSession = Depends(get_db)):
    try:
        start = time.time()
        await db.execute(text("SELECT 1"))
        latency = time.time() - start

        return {
            "status": "healthy",
            "database": "connected",
            "latency": round(latency, 4)
        }

    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "database": "disconnected",
                "error": str(e)
            },
            headers=get_cors_headers(request)
        )