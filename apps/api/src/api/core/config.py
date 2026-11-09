from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Config(BaseSettings):
    OPENAI_API_KEY: SecretStr
    GROQ_API_KEY: SecretStr
    GEMINI_API_KEY: SecretStr
    MONO_TOKEN: SecretStr
    model_config = SettingsConfigDict(env_file=".env", hide_input_in_errors=True)


config = Config()