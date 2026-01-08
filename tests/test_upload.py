def test_upload_invalid_file(client, headers):
    response = client.post(
        "/v1/upload",
        headers=headers,
        files={"file": ("test.txt", b"not an image", "text/plain")},
    )
    assert response.status_code == 400


def test_upload_missing_api_key(client):
    response = client.post("/v1/upload")
    assert response.status_code == 422 or response.status_code == 401
