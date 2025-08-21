import os 
from app.core.config import get_settings 

def test_settings_load():
    settings = get_settings()
    assert settings.PROJECT_NAME == "TaskAI"
    assert "postgresql" in str(settings.DATABASE_URI)
