"""One-command setup for the local demo after dependencies are installed."""
from database.create_database import create_database
from rag.vector_store import build_vector_store

def extract_datasets():
    import gzip
    import shutil
    from pathlib import Path
    for archive in (Path(__file__).resolve().parent / "data").glob("*.csv.gz"):
        target = archive.with_suffix("")
        if not target.exists():
            with gzip.open(archive, "rb") as source, target.open("wb") as output:
                shutil.copyfileobj(source, output)


if __name__ == "__main__":
    extract_datasets()
    print("1/2 Creating SQLite database...")
    create_database()
    print("2/2 Building policy retrieval index...")
    info = build_vector_store(prefer_semantic=True)
    print("Setup complete:", info)
