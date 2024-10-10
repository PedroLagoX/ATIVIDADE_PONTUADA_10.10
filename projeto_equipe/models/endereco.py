class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self.__verificar_logradouro(logradouro)
        self.numero = self.__verificar_numero(numero)
        self.complemento = self.__verificar_complemento(complemento)
        self.cep = self.__verificar_cep(cep)
        self.cidade = self.__verificar_cidade(cidade)

    def __verificar_logradouro(self,logradouro):
        try:
            if not logradouro:
                raise ValueError("1O logradouro não pode estar vazio")
            if not isinstance(logradouro,str):
                raise TypeError("O logradouro só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
            
        return logradouro
    
    def __verificar_numero(self,numero):
        try:
            if not numero:
                raise ValueError("O numero não pode estar vazio")
            if not isinstance(numero,str):
                raise TypeError("O numero só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
            
        return numero
    
    def __verificar_complemento(self,complemento):
        try:
            if not complemento:
                raise ValueError("O complemento não pode estar vazio")
            if not isinstance(complemento,str):
                raise TypeError("O complemento só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
            
        return complemento
    
    def __verificar_cep(self,cep):
        try:
            if not cep:
                raise ValueError("O cep não pode estar vazio")
            if not isinstance(cep,str):
                raise TypeError("O cep só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
            
        return cep

    def __verificar_cidade(self,cidade):
        try:
            if not cidade:
                raise ValueError("O cidade não pode estar vazio")
            if not isinstance(cidade,str):
                raise TypeError("O cidade só pode ser uma string")
        except(ValueError,TypeError) as erro:
            print(erro)
            
        return cidade        
    
    
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
        )