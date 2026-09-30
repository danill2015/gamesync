from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="GameSync Core API",
    version="1.0.0",
    description="Бекенд API для девлогів, реєстру білдів та аналітики плейтестів"
)

# Налаштування CORS для взаємодії зі Svelte на localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Схеми даних ---
class Devlog(BaseModel):
    id: str
    title: str
    project_name: str
    version_tag: str
    author: str
    read_time: str
    content: str
    tags: List[str]
    likes: int
    comments: int
    image_url: str

class Build(BaseModel):
    id: str
    version: str
    channel: str
    status: str
    platforms: List[str]
    size: str
    downloads: int
    active_players: int
    uploaded_at: str

# --- Тестові дані в оперативній пам'яті (відповідають макетам) ---
devlogs_db: List[Devlog] = [
    Devlog(
        id="devlog-047",
        title="Spatial Audio System & Enemy AI Refactor",
        project_name="VOID PROTOCOL",
        version_tag="v0.9.2-alpha",
        author="Mira Solvang",
        read_time="4 min read",
        content="Протягом останніх двох тижнів повністю перероблено сприйняття гравця ворогами. Старий метод рейкастингу викликав нестабільну поведінку у вузьких коридорах — тепер використовується багатошарова модель поля зору з динамічним конусом тривоги.",
        tags=["gameplay", "audio", "AI", "optimization", "stealth"],
        likes=127,
        comments=34,
        image_url="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200&q=80"
    )
]

builds_db: List[Build] = [
    Build(
        id="b-1",
        version="v0.9.2-alpha",
        channel="Public Alpha",
        status="Active Playtest",
        platforms=["Win64", "Linux"],
        size="1.42 GB",
        downloads=1482,
        active_players=89,
        uploaded_at="6 годин тому"
    ),
    Build(
        id="b-2",
        version="v0.9.1-alpha",
        channel="Public Alpha",
        status="Archived",
        platforms=["Win64"],
        size="1.38 GB",
        downloads=3120,
        active_players=0,
        uploaded_at="12 днів тому"
    ),
    Build(
        id="b-3",
        version="v0.9.3-nightly",
        channel="Internal Staging",
        status="Processing",
        platforms=["Win64"],
        size="1.47 GB",
        downloads=0,
        active_players=0,
        uploaded_at="41 хвилину тому"
    )
]

# --- Ендпоінти сервісу ---
@app.get("/api/v1/feed", response_model=List[Devlog])
async def get_feed():
    """Отримання списку останніх публікацій девлогів у стрічці"""
    return devlogs_db

@app.get("/api/v1/builds", response_model=List[Build])
async def get_builds():
    """Отримання списку всіх доступних тестових білдів"""
    return builds_db

@app.delete("/api/v1/builds/{build_id}")
async def delete_build(build_id: str):
    """Деструктивна дія: видалення білду за його ідентифікатором"""
    global builds_db
    initial_len = len(builds_db)
    builds_db = [b for b in builds_db if b.id != build_id]
    if len(builds_db) == initial_len:
        raise HTTPException(status_code=404, detail="Білд не знайдено")
    return {"status": "success", "message": f"Білд {build_id} успішно видалено"}

@app.get("/api/v1/lobbies")
async def get_lobbies():
    """Перевірка стану лобі багатокористувацької гри (для API Testing)"""
    return {
        "status": "success",
        "latency_ms": 38,
        "active_lobbies": [
            {"lobby_id": "eu-central-1", "players": 4, "max": 8, "map": "Cyber_Grid"},
            {"lobby_id": "us-east-1", "players": 8, "max": 8, "map": "Neon_Alley"}
        ]
    }

@app.get("/api/v1/analytics/telemetry")
async def get_telemetry():
    """Отримання аналітики та телеметрії за проектом (для тарифу Indie Pro)"""
    return {
        "total_downloads": 1482,
        "active_playtesters": 89,
        "avg_playtime": "24m 18s",
        "crash_free_rate": "98.4%",
        "traffic_sources": {"Reddit": 44, "GameJams": 28, "Direct": 18, "Twitter": 10},
        "bugs": {"critical": 2, "high": 8, "minor": 24, "resolved": 65}
    }