"""Configuration helpers for loopos-core."""
from __future__ import annotations

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Runtime settings for controlling verification loops."""

    deep_mode: bool = Field(False, description="Use deep L3 loop when True.")
    loop_depth: int = Field(2, ge=1, le=4, description="Default loop depth to execute.")

    class Config:
        env_prefix = "LOOPOS_"
        env_file = ".env"


settings = Settings()

__all__ = ["Settings", "settings"]
