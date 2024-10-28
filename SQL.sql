CREATE TABLE TIMES(
	id_time SERIAL NOT NULL CONSTRAINT pk_time PRIMARY KEY,
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
	id_jogador SERIAL NOT NULL CONSTRAINT pk_jogador PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	id_time INTEGER,
	posicao VARCHAR(20) NOT NULL,
	status VARCHAR(10) NOT NULL,
	amarelos INTEGER,
	vermelhos INTEGER,
	nota NUMERIC(2, 2),
	CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES TIMES(id_time)
);

CREATE TABLE TECNICOS(
	id_tecnico SERIAL NOT NULL CONSTRAINT pk_tecnico PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	id_time INTEGER,
	status VARCHAR(10) NOT NULL,
	nota NUMERIC(2,2),
	CONSTRAINT fk_time_t FOREIGN KEY (id_time) REFERENCES TIMES(id_time)
);

CREATE TABLE ARBITROS(
	id_arbitro SERIAL NOT NULL CONSTRAINT pk_arbitro PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	m_amarelos NUMERIC(2,2),
	m_vemelhos NUMERIC(2,2)
);

CREATE TABLE PARTIDA(
	id_partida SERIAL NOT NULL CONSTRAINT pk_partida PRIMARY KEY,
	id_mandante INTEGER,
	id_visitante INTEGER,
	escalacao_mandante INTEGER,
	escalacao_visitante INTEGER,
	id_arbitro INTEGER,
	CONSTRAINT fk_mandante FOREIGN KEY (id_mandante) REFERENCES TIMES(id_time),
	CONSTRAINT fk_visitante FOREIGN KEY (id_visitante) REFERENCES TIMES(id_time),
	CONSTRAINT fk_arbitro FOREIGN KEY (id_arbitro) REFERENCES ARBITROS(id_arbitro)
);

CREATE TABLE ESCALACAO(
	id_escalacao SERIAL NOT NULL CONSTRAINT pk_escalacao PRIMARY KEY,
	id_partida INTEGER,
	GL INTEGER,
	LE INTEGER,
	ZAG INTEGER,
	LD INTEGER,
	VOL INTEGER, 
	MEI INTEGER, 
	ATA INTEGER,
	CONSTRAINT fk_partida FOREIGN KEY (id_partida) REFERENCES PARTIDA(id_partida)
);

ALTER TABLE PARTIDA
	ADD CONSTRAINT fk_esc_mandante FOREIGN KEY (escalacao_mandante) REFERENCES ESCALACAO(id_escalacao),
	ADD CONSTRAINT fk_esc_visitante FOREIGN KEY (escalacao_visitante) REFERENCES ESCALACAO(id_escalacao);

CREATE TABLE RESULTADO(
	id_partida INTEGER,
	vencedor INTEGER,
	empate VARCHAR(3),
	perdedor INTEGER,
	amarelos INTEGER,
	vermelhos INTEGER
);
