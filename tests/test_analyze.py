def test_analyze_missing_image(client, headers):
    response = client.post(
        "/v1/analyze",
        headers=headers,
        params={"image_id": "nonexistent"},
    )
    assert response.status_code == 404
