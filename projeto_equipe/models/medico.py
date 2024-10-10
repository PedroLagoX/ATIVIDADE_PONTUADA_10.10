from projeto_equipe.models.endereco import Endereco
from projeto_equipe.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = self.__verificar_crm(crm)
        self.telefone = self.__verificar_telefone(telefone)
        self.nome = self.__verificar_nome(nome)
        self.email = self.__verificar_email(email)
      
    def __verificar_nome(self,nome):
        try:
            if not nome:
                raise ValueError("O nome não pode estar vazio")
            if not isinstance(nome,str):
                raise TypeError("O nome só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
            
        return nome

    def __verificar_telefone(self,telefone):   
        try:
            if not telefone:
                raise ValueError("O telefone não pode estar vazio")
            if not isinstance(telefone,str):
                raise TypeError("O telefone só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
        return telefone
    def __verificar_email(self,email):
        try:
            if not email:
                raise ValueError("O email não pode estar vazio")
            if not isinstance(email,str):
                raise TypeError("O email só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
        
        return email
   
    def __verificar_crm(self,crm):
        try:
            if not crm:
                raise ValueError("O crm não pode estar vazio")
            if not isinstance(crm,str):
                raise TypeError("O crm só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
        return crm
    
    def salario_final(self):
        return 6000.0

    def __str__(self) -> str:
        return (f"{super().__str__()} \nCRM: {self.crm}, \nSalário Final: {self.salario_final()}")