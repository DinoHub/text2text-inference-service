from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseSettings, Field


class TritonMode(str, Enum):
    polling = "POLLING"
    explicit = "EXPLICIT"


class Config(BaseSettings):
    """Define any config here.
    See here for documentation:
    https://pydantic-docs.helpmanual.io/usage/settings/
    """

    # App Settings
    # KNative assigns a $PORT environment variable to the container
    port: int = Field(
        default=8080, env="PORT", description="Gradio App Server Port"
    )

config = Config()