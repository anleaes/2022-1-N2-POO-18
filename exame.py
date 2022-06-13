class Exame:
    def __init__(self, tipo_exame, data_exame, local_exame, restricoes_exame, equipe_medica, consulta):
        self._tipo_exame = tipo_exame
        self._data_exame = data_exame 
        self._local_exame = local_exame
        self._restricoes_exame = restricoes_exame
        self._equipe_medica = equipe_medica
        self._consulta = consulta

    def pegar_nome_medico (self):
        return "%s" % (self._equipe_medica._nome_medico)

    def pegar_nome_enfermeiras (self):
        return "%s" % (self._equipe_medica._nome_enfermeiras)

    def pegar_exame_fisico (self):
        return "%s" % (self._consulta._exame_fisico)

    def pegar_pressao (self):
        return "%s" % (self._consulta._pressao)