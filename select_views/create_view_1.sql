CREATE VIEW
    techchallengeefase5.view_dados_alunos AS
SELECT
    nome,
    instituicao_ensino_aluno,
    idade_aluno,
    anos_pm,
    fase_turma AS fase,
    ponto_virada,
    inde,
    inde_conceito,
    pedra,
    destaque_ieg,
    destaque_ida,
    destaque_ipv,
    iaa,
    ieg,
    ips,
    ida,
    ipp,
    ipv,
    ian,
    ano,
    dt_pst
FROM
    techchallengeefase5.tb_dados_principais_2020
UNION ALL
SELECT
    nome,
    instituicao_ensino_aluno,
    NULL AS idade_aluno, -- Não existe na tabela 2021
    NULL AS anos_pm, -- Não existe na tabela 2021
    fase,
    ponto_virada,
    inde,
    NULL AS inde_conceito, -- Não existe na tabela 2021
    pedra,
    NULL AS destaque_ieg, -- Não existe na tabela 2021
    NULL AS destaque_ida, -- Não existe na tabela 2021
    NULL AS destaque_ipv, -- Não existe na tabela 2021
    iaa,
    ieg,
    ips,
    ida,
    ipp,
    ipv,
    ian,
    ano,
    dt_pst
FROM
    techchallengeefase5.tb_dados_principais_2021
UNION ALL
SELECT
    nome,
    NULL AS instituicao_ensino_aluno, -- Não existe na tabela 2022
    NULL AS idade_aluno, -- Não existe na tabela 2022
    NULL AS anos_pm, -- Não existe na tabela 2022
    fase,
    ponto_virada,
    inde,
    NULL AS inde_conceito, -- Não existe na tabela 2022
    pedra,
    destaque_ieg,
    destaque_ida,
    destaque_ipv,
    iaa,
    ieg,
    ips,
    ida,
    ipp,
    ipv,
    ian,
    ano,
    dt_pst
FROM
    techchallengeefase5.tb_dados_principais_2022;