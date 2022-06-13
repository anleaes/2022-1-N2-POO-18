class Consulta:
    def __init__(self, temperatura, pressao, remedios_tomados, alergias, exame_fisico, diagnostico, equipe_medica):
        self._temperatura = temperatura
        self._pressao = pressao 
        self._remedios_tomados = remedios_tomados
        self._alergias = alergias 
        self._exame_fisico = exame_fisico
        self._diagnostico = diagnostico
        self._equipe_medica = equipe_medica
    
    def pegar_nome_medico (self):
        return "%s" % (self._equipe_medica._nome_medico)

    def pegar_nome_enfermeiras (self):
        return "%s" % (self._equipe_medica._nome_enfermeiras)

    