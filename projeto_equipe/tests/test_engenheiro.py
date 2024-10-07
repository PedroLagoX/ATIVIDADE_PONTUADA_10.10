import pytest
from projeto_equipe.models.engenheiro import Engenheiro
from projeto_equipe.models.Endereco import Endereco



endereco2=Endereco("Rua B","41","600","321021-213","Salvador")

@pytest.fixture
def engenheiro_valido():
    return Engenheiro(1234,2123,122,endereco2,21331)


def test_criar_engenheiro_nome(engenheiro_valido):
    assert engenheiro_valido.nome== "Julio Cesar"

def test_criar_engenheiro_telefone(engenheiro_valido):
    assert engenheiro_valido.telefone== "7198291283"

def test_criar_engenheiro_email(engenheiro_valido):
    assert engenheiro_valido.email== "juliocesar@gmail.com"

def test_criar_engenheiro_crea(engenheiro_valido):
    assert engenheiro_valido.crea== "67732421"


