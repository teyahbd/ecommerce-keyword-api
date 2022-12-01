
import json
from app import app

# endpoint testing:

def test_home_route():
    response = app.test_client().get("/")
    res = json.loads(response.data.decode("utf-8")).get("Endpoints")

    assert type(res) is dict
    assert "/model" in res
    assert res["/model"] == "accepts POST request containing keywords which returns related keywords"
    assert response.status_code == 200

def test_model_route():
    expected_keywords = [
		[
			"recycled",
			0.39151617884635925
		],
		[
			"star",
			0.37562987208366394
		]
	]

    response = app.test_client().post("/model", json={"positive": ["heart"], "negative": ["red"]})
    res = json.loads(response.data.decode("utf-8")).get("keywords")

    assert type(res) is list
    assert len(res) == 2
    for i in res:
        assert type(i[0]) is str
        assert type(i[1]) is float
    assert res == expected_keywords
    assert response.status_code == 200

# endpoint error handling testing: