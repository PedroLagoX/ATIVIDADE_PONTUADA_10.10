from projeto_equipe.models.funcionario import Funcionario
from projeto_equipe.models.Endereco import Endereco
import pytest

@pytest.fixture
def endereco_valido():
    endereco1=Endereco("Rua A","42","900","213343-322","Salvador")
    return endereco1


@pytest.fixture
def funcionario_valido(endereco_valido):
    return Funcionario("Pedro Lago","7198284324","pedrolago@gmail.com",endereco_valido)

def test_validando_atributos_funcionario_nome(funcionario_valido):
    assert funcionario_valido.telefone=="Pedro Lago"

def test_validando_atributos_funcionario_nome(funcionario_valido):
    assert funcionario_valido.nome=="Pedro Lago"

def test_validando_atributos_funcionario_nome(funcionario_valido):
    assert funcionario_valido.nome=="Pedro Lago"

def test_validando_atributos_funcionario_nome(funcionario_valido):
    assert funcionario_valido.nome=="Pedro Lago"

def test_validando_atributos_funcionario_nome(funcionario_valido):
    assert funcionario_valido.nome=="Pedro Lago"