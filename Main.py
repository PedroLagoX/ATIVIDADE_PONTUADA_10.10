from projeto_equipe.models.engenheiro import Engenheiro
from projeto_equipe.models.medico import Medico
from projeto_equipe.models.funcionario import Funcionario
from projeto_equipe.models.Endereco import Endereco

endereco1=Endereco("Rua A","42","900","213343-322","Salvador")
funcionario=Funcionario("Pedro Lago","7198284324","pedrolago@gmail.com",endereco1)

print(funcionario)