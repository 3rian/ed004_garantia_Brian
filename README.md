Descrição do Projeto

O banco de dados app_garantia gerencia informações sobre lojas, equipamentos e garantias.
Ele permite armazenar dados sobre:

Lojas (loja)

Equipamentos vendidos por cada loja (equipamento)

Garantias associadas aos equipamentos (garantia)

O objetivo é manter a integridade dos dados e possibilitar consultas sobre vendas e garantias.

-------------------------------------------------------------------------------------------------

Estrutura do Banco de Dados

Tabela loja

Armazena informações das lojas:

| Coluna   | Tipo         | Restrição        |
| -------- | ------------ | ---------------- |
| id_loja  | SERIAL       | PRIMARY KEY      |
| nome     | VARCHAR(100) | NOT NULL         |
| cnpj     | VARCHAR(20)  | UNIQUE, NOT NULL |
| endereco | VARCHAR(200) |                  |
| telefone | VARCHAR(15)  |                  |

-------------------------------------------------------------------------------------------------

Relação: Uma loja pode vender vários equipamentos → 1:N com equipamento.


-------------------------------------------------------------------------------------------------

Tabela equipamento

Registra os equipamentos vendidos:

| Coluna         | Tipo          | Restrição                    |
| -------------- | ------------- | ---------------------------- |
| id_equipamento | SERIAL        | PRIMARY KEY                  |
| nome           | VARCHAR(100)  | NOT NULL                     |
| marca          | VARCHAR(50)   |                              |
| modelo         | VARCHAR(50)   |                              |
| numero_serie   | VARCHAR(50)   | UNIQUE                       |
| data_compra    | DATE          |                              |
| preco          | NUMERIC(10,2) |                              |
| data_venda     | DATE          |                              |
| id_loja        | INT           | FOREIGN KEY → `loja.id_loja` |

-------------------------------------------------------------------------------------------------

Relação:

Um equipamento pertence a uma loja

Uma loja pode ter vários equipamentos → 1:N

ON DELETE CASCADE garante que, ao apagar a loja, os equipamentos relacionados também sejam removidos.


-----------------------------------------------------------------------------------------------------

Tabela garantia

Registra as garantias de cada equipamento:

| Coluna         | Tipo        | Restrição                                  |
| -------------- | ----------- | ------------------------------------------ |
| id_garantia    | SERIAL      | PRIMARY KEY                                |
| id_equipamento | INT         | FOREIGN KEY → `equipamento.id_equipamento` |
| data_inicio    | DATE        | NOT NULL                                   |
| data_fim       | DATE        | NOT NULL                                   |
| tipo           | VARCHAR(50) | DEFAULT 'Padrão'                           |
| observacoes    | TEXT        |                                            |


Relação:

Uma garantia pertence a um equipamento

Um equipamento pode ter várias garantias → 1:N

ON DELETE CASCADE garante que, ao apagar um equipamento, suas garantias sejam removidas.