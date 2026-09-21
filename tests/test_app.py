import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "app"))

from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello from DevOps APSIT - Docker v2!"
