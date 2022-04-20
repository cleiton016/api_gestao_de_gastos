from django.db import models
class MES_LANCAMENTO(models.TextChoices):
        JANEIRO     = '01', 'Janeiro'
        FEVEREIRO   = '02', 'Fevereiro'
        MARCO       = '03', 'Março'
        ABRIL       = '04', 'Abril'
        MAIO        = '05', 'Maio'
        JUNHO       = '06', 'Junho'
        JULHO       = '07', 'Julho'
        AGOSTO      = '08', 'Agosto'
        SETEMBRO    = '09', 'Setembro'
        OUTUBRO     = '10', 'Outubro'
        NOVEMBRO    = '11', 'Novembro'
        DEZEMBRO    = '12', 'Dezembro'