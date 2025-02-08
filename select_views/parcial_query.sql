SELECT
2020 - EXTRACT(Year FROM to_timestamp(dim_aluno.datanascimento, 'YYYY-MM-DD HH24:MI:SS')) as idade,
dim_aluno.nomealuno,
T2020.instituicao_ensino_aluno,
T2020.nome,
T2020.idade_aluno,
T2020.anos_pm,
T2020.fase_turma,
T2020.ponto_virada,
T2020.inde,
T2020.inde_conceito,
T2020.pedra,
T2020.destaque_ieg,
T2020.destaque_ida,
T2020.destaque_ipv,
T2020.iaa,
T2020.ieg,
T2020.ips,
T2020.ida,
T2020.ipp,
T2020.ipv,
T2020.ian,
T2020.ano,
T2020.dt_pst
FROM techchallengefase5.tb_dados_principais_2020 as T2020
left join techchallengefase5.tb_aluno as dim_aluno on upper(trim(dim_aluno.nomealuno)) = REGEXP_REPLACE(upper(trim(T2020.nome)), '[^a-zA-Z0-9 ]', ' ')
where 
dim_aluno.datanascimento ~ '^\d{4}-\d{2}-\d{2}'



