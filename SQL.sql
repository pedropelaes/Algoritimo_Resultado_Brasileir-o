CREATE TABLE TIMES(
	id_time INTEGER NOT NULL CONSTRAINT pk_time PRIMARY KEY,
	nome VARCHAR(80) NOT NULL,
	posicao VARCHAR(3) NOT NULL,
	vitorias INTEGER,
	empates INTEGER, 
	derrotas INTEGER,
	p_vitorias_casa NUMERIC(3, 2),
	p_vitorias_fora NUMERIC(3, 2),
	nota NUMERIC(2, 2)
);

CREATE TABLE JOGADORES(
	id_jogador INTEGER NOT NULL CONSTRAINT pk_jogador PRIMARY KEY,
	nome VARCAHR(100) NOT NULL,
	id_time INTEGER,
	posicao VARCHAR(20) NOT NULL,
	status VARCHAR(10) NOT NULL,
	amarelos INTEGER,
	vermelhos INTEGER,
	nota NUMERIC(2, 2),
	CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES TIMES(id_time)
);