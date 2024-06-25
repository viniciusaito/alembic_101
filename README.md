# Comandos usados neste estudo:

## O ambiente python não está incluso, porém o projeto usa poetry, para mais referência pesquisar.

### Este exemplo usa um banco de dados postgres. Favor subir um container com a seguinte configuração para rodar os exemplos:

```bash
docker run --name example     --rm -d     -e POSTGRES_PASSWORD=app_password     -e POSTGRES_DB=app_db -e POSTGRES_USER=app_user     -p 5432:5432     postgres
```

```bash
alembic init alembic

    Creating directory '/home/va_notebook/vini/live_de_python/alembic_101/alembic' ...  done
    Creating directory '/home/va_notebook/vini/live_de_python/alembic_101/alembic/versions' ...  done
    Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic/env.py ...  done
    Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic/script.py.mako ...  done
    Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic/README ...  done
    Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic.ini ...  done
    Please edit configuration/connection/logging settings in '/home/va_notebook/vini/live_de_python/alembic_101/alembic.ini' before proceeding.
```

```bash
alembic revision -m "primeira migração"

      Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic/versions/5c4a1ec24e87_primeira_migração.py ...  done
```

```bash
alembic upgrade head

        INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
        INFO  [alembic.runtime.migration] Will assume transactional DDL.
        INFO  [alembic.runtime.migration] Running upgrade  -> 5c4a1ec24e87, primeira migração
```

```bash
alembic downgrade base

        INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
        INFO  [alembic.runtime.migration] Will assume transactional DDL.
        INFO  [alembic.runtime.migration] Running downgrade 5c4a1ec24e87 -> , primeira migração
```

```bash
alembic history

        <base> -> 5c4a1ec24e87 (head), primeira migração
```

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic history -i

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
<base> -> 5c4a1ec24e87 (head), primeira migração
```

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic upgrade head

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 5c4a1ec24e87, primeira migração
```

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic history -i

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
<base> -> 5c4a1ec24e87 (head) (current), primeira migração
```

### Base.metadata foi importado e adicionado na env.py do alembic

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic revision --autogenerate -m "Criando campo de senha na tabela pessoa"

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] Detected sequence named 'pessoa_id_seq' as owned by integer column 'pessoa(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare] Detected added column 'pessoa.senha'
INFO  [alembic.autogenerate.compare] Detected type change from VARCHAR(length=50) to String(length=100) on 'pessoa.email'
  Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic/versions/ca305f62830c_criando_campo_de_senha_na_tabela_pessoa.py ...  done
```

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic upgrade +1

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 5c4a1ec24e87 -> ca305f62830c, Criando campo de senha na tabela pessoa
```

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic history -i

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
5c4a1ec24e87 -> ca305f62830c (head) (current), Criando campo de senha na tabela pessoa
<base> -> 5c4a1ec24e87, primeira migração
```

### Adicionando diversas mudanças sequenciais para verificar history -i

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic revision --autogenerate -m "Criando tabela pessoa 2"

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'pessoa2'
INFO  [alembic.ddl.postgresql] Detected sequence named 'pessoa_id_seq' as owned by integer column 'pessoa(id)', assuming SERIAL and omitting
  Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic/versions/0f9273c29cb8_criando_tabela_pessoa_2.py ...  done

(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic upgrade +1

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade ca305f62830c -> 0f9273c29cb8, Criando tabela pessoa 2

(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic revision --autogenerate -m "Adicionando campo idade na tabela pessoa 2"

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] Detected sequence named 'pessoa_id_seq' as owned by integer column 'pessoa(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'pessoa2_id_seq' as owned by integer column 'pessoa2(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare] Detected added column 'pessoa2.idade'
  Generating /home/va_notebook/vini/live_de_python/alembic_101/alembic/versions/d8ef4bed783a_adicionando_campo_idade_na_tabela_.py ...  done

(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic upgrade +1

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 0f9273c29cb8 -> d8ef4bed783a, Adicionando campo idade na tabela pessoa 2

(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic history -i

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
0f9273c29cb8 -> d8ef4bed783a (head) (current), Adicionando campo idade na tabela pessoa 2
ca305f62830c -> 0f9273c29cb8, Criando tabela pessoa 2
5c4a1ec24e87 -> ca305f62830c, Criando campo de senha na tabela pessoa
<base> -> 5c4a1ec24e87, primeira 
```

### Fazendo downgrade e verificando history

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic downgrade -1

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade d8ef4bed783a -> 0f9273c29cb8, Adicionando campo idade na tabela pessoa 2

(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic downgrade -1

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade 0f9273c29cb8 -> ca305f62830c, Criando tabela pessoa 2

(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic history -i

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
0f9273c29cb8 -> d8ef4bed783a (head), Adicionando campo idade na tabela pessoa 2
ca305f62830c -> 0f9273c29cb8, Criando tabela pessoa 2
5c4a1ec24e87 -> ca305f62830c (current), Criando campo de senha na tabela pessoa
<base> -> 5c4a1ec24e87, primeira migração
```

### Voltando tabela para o head

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic upgrade head

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade ca305f62830c -> 0f9273c29cb8, Criando tabela pessoa 2
INFO  [alembic.runtime.migration] Running upgrade 0f9273c29cb8 -> d8ef4bed783a, Adicionando campo idade na tabela pessoa 2

(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic history -i

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
0f9273c29cb8 -> d8ef4bed783a (head) (current), Adicionando campo idade na tabela pessoa 2
ca305f62830c -> 0f9273c29cb8, Criando tabela pessoa 2
5c4a1ec24e87 -> ca305f62830c, Criando campo de senha na tabela pessoa
<base> -> 5c4a1ec24e87, primeira migração
```

### Gerando SQL para migração offline

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic upgrade +1 --sql

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Generating static SQL
INFO  [alembic.runtime.migration] Will assume transactional DDL.
BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

INFO  [alembic.runtime.migration] Running upgrade  -> 5c4a1ec24e87, primeira migração
-- Running upgrade  -> 5c4a1ec24e87

CREATE TABLE pessoa (
    id SERIAL NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('5c4a1ec24e87') RETURNING alembic_version.version_num;

COMMIT;
```

### Gerando SQL de downgrade para migração offline

```bash
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic history -i

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
0f9273c29cb8 -> d8ef4bed783a (head), Adicionando campo idade na tabela pessoa 2
ca305f62830c -> 0f9273c29cb8 (current), Criando tabela pessoa 2
5c4a1ec24e87 -> ca305f62830c, Criando campo de senha na tabela pessoa
<base> -> 5c4a1ec24e87, primeira migração
(alembic-101-py3.12) va_notebook@DESKTOP-ORTG019:~/vini/live_de_python/alembic_101$ alembic downgrade d8ef4bed783a:ca305f62830c --sql
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Generating static SQL
INFO  [alembic.runtime.migration] Will assume transactional DDL.
BEGIN;

INFO  [alembic.runtime.migration] Running downgrade d8ef4bed783a -> 0f9273c29cb8, Adicionando campo idade na tabela pessoa 2
-- Running downgrade d8ef4bed783a -> 0f9273c29cb8

ALTER TABLE pessoa2 DROP COLUMN idade;

UPDATE alembic_version SET version_num='0f9273c29cb8' WHERE alembic_version.version_num = 'd8ef4bed783a';

INFO  [alembic.runtime.migration] Running downgrade 0f9273c29cb8 -> ca305f62830c, Criando tabela pessoa 2
-- Running downgrade 0f9273c29cb8 -> ca305f62830c

DROP TABLE pessoa2;

UPDATE alembic_version SET version_num='ca305f62830c' WHERE alembic_version.version_num = '0f9273c29cb8';

COMMIT;
```

### OBS: Algumas mudanças de config foram feitas, para gerar deployments como batch e habilitar a flag compare_type, verificar arquivo env.py