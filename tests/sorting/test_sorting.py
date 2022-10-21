import pytest
from src.sorting import sort_by


@pytest.fixture
def mock_jobs():
    return [
        {"title": "Job1", "min_salary": 15, "max_salary": 85,
        "date_posted": '2022-05-28'},
        {"title": "Job2", "min_salary": 20, "max_salary": 60,
        "date_posted": '2022-06-28'},
        {"title": "Job3", "min_salary": 3, "max_salary": 50,
        "date_posted": '2022-07-28'},
    ]


def test_sort_by_criteria(mock_jobs):
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs[0]["min_salary"] == 3
    sort_by(mock_jobs, "max_salary")
    assert mock_jobs[0]["max_salary"] == 85
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs[0]["date_posted"] == '2022-07-28'
