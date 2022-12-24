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
    SESSION = environ.get("SESSION", "BQBtDYfn0sUsI76Bhk6Ez-9Jx-Px-_TP50c4ZdXifWRdwVRcCXSvGSdXQ53X4aqdq0Wp5ptiSA-ql0waGMHDCQ_-NZmGvU4HkAGaMJvbg8FTgB6d9J3iBxFyeWmZ8t8CRe2jSyF7vvQ568FEGJ8cnoa8yreNhVJNxK_C8g3n1MHpt2jX0iwoPnwYByCl6o7zKIUyW3CFd0LP-o3h5tFrq3IDBgpnpUiVyfNdXSJ-q0jdeegbrEq-6ApotTWxS580NpbW1iq3fw21sBYrDvcFFxmhcx3uK5EIkvEJ4MLNoClQt9JSYtmgHNiKDBpIvSgwbIFX9dgBIBtSSbBxNb_e64X5djpEVgA")
    TO_CHANNEL = int(environ.get("TO_CHANNEL", "-1001629175532"))

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
