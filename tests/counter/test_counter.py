from src.counter import count_ocurrences

path = 'src/jobs.csv'


def test_counter():
    'Testa a função recebendo uma string'
    assert count_ocurrences(path, 'junior') == 211
