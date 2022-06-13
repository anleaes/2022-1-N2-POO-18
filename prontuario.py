class Prontuario: 
    def __init__(self, data, id_prontuario, cadastro_paciente, equipe_medica, hospital, tratamento ):
        self._data = data
        self._id_prontuario = id_prontuario
        self._cadastro_paciente = cadastro_paciente
        self._equipe_medica = equipe_medica
        self._hospital = hospital
        self._tratamento = tratamento 
        
    def pegar_nome (self):
        return "%s" % (self._cadastro_paciente._nome)
    def pegar_idade (self):
        return "%s" % (self._cadastro_paciente._idade)
    def pegar_num_cadastro (self):
        return "%s" % (self._cadastro_paciente._num_cadastro)
    
    def pegar_nome_medico (self):
        return "%s" % (self._equipe_medica._nome_medico)
    def pegar_nome_enfermeiras (self):
        return "%s" % (self._equipe_medica._nome_enfermeiras)
    def pegar_crm_medico (self):
        return "%s" % (self._equipe_medica._crm_medico)
    
    def pegar_nome_hospital (self):
        return "%s" % (self._hospital._nome_hospital)
    def pegar_endereco_hospital (self):
        return "%s" % (self._hospital._endereco_hospital)
    def pegar_ala_hospital (self):
        return "%s" % (self._hospital._ala_hospital)
    def pegar_sala (self):
        return "%s" % (self._hospital._sala)
    
    def pegar_remedios (self):
        return "%s" % (self._tratamento._remedios)
    def pegar_restricoes (self):
        return "%s" % (self._tratamento._restricoes)  
    
         
    
    
    