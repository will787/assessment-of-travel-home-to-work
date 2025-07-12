import basedosdados as bd

billing_id = "transporte-dados"

query = """
  SELECT
    dados.ano as ano,
    dados.sigla_uf AS sigla_uf,
    diretorio_sigla_uf.nome AS sigla_uf_nome,
    dados.id_municipio AS id_municipio,
    diretorio_id_municipio.nome AS id_municipio_nome,
    dados.tempo_medio_deslocamento as tempo_medio_deslocamento,
    dados.prop_deslocamento_acima_1_hora as prop_deslocamento_acima_1_hora
FROM `basedosdados.br_mobilidados_indicadores.tempo_deslocamento_casa_trabalho` AS dados
LEFT JOIN (SELECT DISTINCT sigla,nome  FROM `basedosdados.br_bd_diretorios_brasil.uf`) AS diretorio_sigla_uf
    ON dados.sigla_uf = diretorio_sigla_uf.sigla
LEFT JOIN (SELECT DISTINCT id_municipio,nome  FROM `basedosdados.br_bd_diretorios_brasil.municipio`) AS diretorio_id_municipio
    ON dados.id_municipio = diretorio_id_municipio.id_municipio
"""

database = bd.read_sql(query = query, billing_project_id = billing_id)