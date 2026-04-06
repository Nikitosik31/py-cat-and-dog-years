from app.main import get_human_age


def test_return_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_return_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_return_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_return_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_return_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_dog_age_after_24_years() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_and_dog_return_different_result() -> None:
    assert get_human_age(28, 28) == [3, 2]
