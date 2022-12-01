import pytest
from model.model import find_keywords

# find_keywords() functionality testing:

def test_returns_list():
    liked_keywords = ["heart"]
    disliked_keywords = ["red"]
    assert type(find_keywords(liked_keywords, disliked_keywords)) is list

def test_returns_two_results():
    liked_keywords = ["heart"]
    disliked_keywords = ["red"]
    assert len(find_keywords(liked_keywords, disliked_keywords)) == 2


def test_returns_list_of_tuples():
    liked_keywords = ["heart"]
    disliked_keywords = ["red"]
    output = find_keywords(liked_keywords, disliked_keywords)
    for i in output:
        assert type(i) is tuple

def test_returns_list_of_correctly_formatted_tuples():
    liked_keywords = ["heart"]
    disliked_keywords = ["red"]
    output = find_keywords(liked_keywords, disliked_keywords)
    for i in output:
        assert type(i[0]) is str
        assert type(i[1]) is float

def test_returns_correct_result():
    liked_keywords = ["heart"]
    disliked_keywords = ["red"]
    expected_result = [('recycled', 0.39151617884635925), ('star', 0.37562987208366394)]
    assert find_keywords(liked_keywords, disliked_keywords) == expected_result

# find_keywords() error handling testing:

def test_raises_error_all_missing_args():
    with pytest.raises(TypeError):
      find_keywords()

def test_raises__error_one_missing_arg():
    liked_keywords = ["heart"]
    with pytest.raises(TypeError):
      find_keywords(liked_keywords)

def test_raises_error_empty_arrays():
    with pytest.raises(ValueError):
      find_keywords([],[])

def test_raises_error_unknown_word():
    liked_keywords = ["heart"]
    unknown_keyword = ["mansjk"]
    with pytest.raises(KeyError):
        find_keywords(liked_keywords, unknown_keyword)
