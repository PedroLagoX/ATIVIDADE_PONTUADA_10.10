import os 
from projeto_equipe.models.endereco import Endereco
from abc import ABC, abstractmethod


os.system("cls||clear")

class Funcionario(ABC):
    def __init__(self,nome:str,telefone:str,email:str,endereco:Endereco) -> None:
        self.nome=nome
        self.telefone=telefone
        self.email=email
        self.endereco=endereco


    @abstractmethod
    def salario_final(self):
        pass

    
        
    
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail:{self.email}"
                f"\nEndereco:{self.endereco}")