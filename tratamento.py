class Tratamento:
   def __init__(self, duracao, remedios, qtd_remedio_dia, restricoes, exame, consulta):
        self._duracao = duracao
        self._remedios = remedios
        self._qtd_remedio_dia = qtd_remedio_dia
        self._restricoes = restricoes
        self._exame = exame
        self._consulta = consulta 
        
   def pegar_tipo_exame (self):
      return "%s" % (self._exame._tipo_exame)
   def pegar_restricoes_exame (self):
      return "%s" % (self._exame._restricoes_exame)
         
   def pegar_alergias (self):
      return "%s" % (self._consulta._alergias)
   def pegar_remedios_tomados (self):
          return "%s" % (self._consulta._remedios_tomados) 
