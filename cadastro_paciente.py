from plano_saude import Plano_saude

class Cadastro_paciente:
    def __init__(self, nome, idade, cpf, endereco, telefone, num_cadastro, plano_saude):
        self._nome = nome
        self._idade = idade 
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone 
        self._num_cadastro = num_cadastro
        self._plano_saude = plano_saude

    def pegar_tipo_plano (self):
        return "%s" % (self._plano_saude._tipo_plano)
    def pegar_cobertura (self):
        return "%s" % (self._plano_saude._cobertura)
    def pegar_num_cadastro (self):
        return "%s" % (self._plano_saude._num_cadastro)
        