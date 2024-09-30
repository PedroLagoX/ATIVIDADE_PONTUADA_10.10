from projeto_equipe.models.engenheiro import Engenheiro
from projeto_equipe.models.medico import Medico
from projeto_equipe.models.funcionario import Funcionario
from projeto_equipe.models.Endereco import Endereco
import os

os.system("cls||clear")

endereco1=Endereco("Rua A","42","900","213343-322","Salvador")
endereco2=Endereco("Rua B","41","600","321021-213","Salvador")
endereco3=Endereco("Rua C","40","500","123023-123","Salvador")


funcionario=Funcionario("Pedro Lago","7198284324","pedrolago@gmail.com",endereco1)
engenheiro=Engenheiro("Julio Cesar","7198291283","juliocesar@gmail.com",endereco2,"67732421")
medico=Medico("Caio Fernando","719828213","caiofernando@gmail.com",endereco3,"232302131")


print(funcionario)
print(engenheiro)
print(medico)