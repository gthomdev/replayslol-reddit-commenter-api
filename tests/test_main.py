from fastapi.testclient import TestClient
from replayslol_reddit_commenter_api import main

client = TestClient(main.app)


def test_get_reddit_comment():
    response = client.get("/reddit_comments/")
    assert response.status_code == 403
