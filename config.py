from os import environ
import logging

class Config:
    
    API_ID = int(environ.get("API_ID", ""))
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    CAPTION = environ.get("CAPTION", "")
    FROM_CHANNEL = environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = environ.get("FILTER_TYPE", "")
    OWNER_ID = environ.get("OWNER_ID", "")
    LIMIT = int(environ.get("LIMIT", "25000"))
    SKIP_NO = int(environ.get("SKIP_NO", "0"))
    SESSION = environ.get("SESSION", "")
    TO_CHANNEL = int(environ.get("TO_CHANNEL", ""))

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
