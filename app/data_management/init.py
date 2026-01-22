from os import makedirs
from pathlib import Path
import sqlite3

def db_init(path):
    db_path = Path(path)

    if not db_path.exists():
        db_path.mkdir(parents=True, exist_ok=True)

    