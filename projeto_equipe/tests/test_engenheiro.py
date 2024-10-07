import pytest
from projeto_equipe.models.engenheiro import Engenheiro
from projeto_equipe.models.Endereco import Endereco


@pytest.fixture
def engenheiro_valido():
    return Engenheiro("Julio Cesar","7198291283","juliocesar@gmail.com","67732421")


def test_criar_engenheiro(engenheiro_valido):
    assert engenheiro_valido.nome== "Julio Cesar"

def test_criar_engenheiro(engenheiro_valido):
    assert engenheiro_valido.telefone== "7198291283"

def test_criar_engenheiro(engenheiro_valido):
    assert engenheiro_valido.email== "juliocesar@gmail.com"

def test_criar_engenheiro(engenheiro_valido):
    assert engenheiro_valido.crea== "67732421"


