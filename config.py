from os import environ
import logging

class Config:
    
    API_ID = int(environ.get("API_ID", "11671320"))
    API_HASH = environ.get("API_HASH", "8e409e260f1d80f0ead65da912ee07bb")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5813212548:AAG1503Ilf2se-uiHkWwNSxPSr20v0yL6Oo") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    CAPTION = environ.get("CAPTION", "")
    FROM_CHANNEL = environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = environ.get("FILTER_TYPE", "")
    OWNER_ID = environ.get("OWNER_ID", "1983530070")
    LIMIT = int(environ.get("LIMIT", "25000"))
    SKIP_NO = int(environ.get("SKIP_NO", "0"))
    SESSION = environ.getenv("SESSION", "BQAo3w6AHb9jOnnCRyiDBRIyFSX7PWisgQKSttm3q2HetCeqMI6kViupUKycgUwuBfMr8-GawlSuyRLREouTPYlj8C6VnDGwaHqkT3c5bSHXig8ua3mKFayhECY8UjxB52QcbZtdVaZ-GEw_Tsd7g7Ddqbygu9tep65Qgvj6GXOnnAJPT80O0sHUDqPdLv2_P3yQDbTwwmvqzXvKGKiMoFLW83l9rosZTELNAtfrmBZ5vXjp797jJ-m7gMhZBGhVlImRX9n5hld7OsRfHdTA-5u6u9T8bjS2dr_vwB1fpHIqmv6A2W__veGWoUv5GUxODmcwDGUxzBqpXGsAYoOgi1CEdjpEVgA")
    TO_CHANNEL = int(environ.get("TO_CHANNEL", "-1001629175532"))

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
