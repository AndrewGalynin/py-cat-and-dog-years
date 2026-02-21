from app.main import get_human_age


def test_returns_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_returns_zero_for_ages_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(10, 10) == [0, 0]


def test_returns_one_for_ages_exactly_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_returns_one_for_ages_between_15_and_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_returns_two_for_ages_exactly_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_calculates_correctly_for_ages_over_24() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_calculates_correctly_for_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_calculates_correctly_for_different_cat_and_dog_ages() -> None:
    assert get_human_age(15, 24) == [1, 2]
