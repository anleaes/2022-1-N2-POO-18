class Hospital:
    def __init__(self, nome_hospital, endereco_hospital, ala_hospitalar, sala, equipe_medica):
        self._nome_hospital = nome_hospital
        self._endereco_hospital = endereco_hospital
        self._ala_hospitalar = ala_hospitalar
        self._sala = sala
        self._equipe_medica = equipe_medica


    def pegar_nome_medico (self):
        return "%s" % (self._equipe_medica._nome_medico)

    def pegar_crm_medico (self):
        return "%s" % (self._equipe_medica._crm_medico)

    def pegar_nome_enfermeiras (self):
        return "%s" % (self._equipe_medica._nome_enfermeiras)
   