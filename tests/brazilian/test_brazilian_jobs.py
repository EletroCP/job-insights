from src.brazilian_jobs import read_brazilian_file


path = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    result = read_brazilian_file(path)
    for job in result:
        assert 'title' in job
        assert 'salary' in job
        assert 'type' in job
        assert 'titulo' not in job
        assert 'salario' not in job
        assert 'tipo' not in job
