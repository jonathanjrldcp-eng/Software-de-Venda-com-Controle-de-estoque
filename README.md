# Sistema de Controle de Estoque e Vendas 📦🛒

Este é um sistema interativo de linha de comando (CLI) desenvolvido em Python para gerenciamento básico de estoque e registro de vendas. O aplicativo é ideal para pequenos comércios ou estudos práticos sobre manipulação de dicionários, listas e funções em Python.

## Funcionalidades

O sistema opera através de um menu principal com as seguintes opções:

1. **Cadastro de Produto (`1`)**: 
   - Adiciona um novo produto ao estoque.
   - Se o produto já existir, a quantidade informada é somada ao estoque atual.
   - Validação para aceitar apenas números inteiros positivos.
   
2. **Visualizar Estoque (`2`)**: 
   - Exibe uma tabela formatada contendo todos os produtos cadastrados e suas respectivas quantidades disponíveis.

3. **Iniciar Venda (`3`)**: 
   - Permite registrar a venda de um produto.
   - Verifica se o produto existe no estoque e se a quantidade solicitada está disponível.
   - Subtrai a quantidade vendida do estoque automaticamente e salva a transação no histórico.

4. **Vendas Realizadas (`4`)**: 
   - Gera um relatório (extrato) com todos os produtos vendidos durante a sessão.
   - Exibe o total geral de itens vendidos.

5. **Sair (`5`)**: 
   - Encerra a aplicação de forma limpa.

## Tecnologias e Conceitos Utilizados

- **Python 3.x**
- **Bibliotecas Embutidas:**
  - `os`: Para detectar o sistema operacional e limpar o terminal interativamente (`cls` para Windows, `clear` para Linux/Mac).
  - `time`: Para transições suaves de tela (delays).
- **Estruturas de Dados:**
  - `Dicionários (dict)`: Utilizado para gerenciar o estoque (Relação `Produto: Quantidade`).
  - `Listas (list)`: Utilizada para armazenar o histórico de vendas.
- **Tratamento de Exceções (`try-except`)**: Para evitar que o programa "quebre" caso o usuário digite letras em campos numéricos.

## Como Executar na sua Máquina

1. Certifique-se de ter o **Python** instalado (versão 3.6 ou superior).
2. Salve o código em um arquivo com a extensão `.py` (exemplo: `sistema_estoque.py`).
3. Abra o seu terminal ou prompt de comando.
4. Navegue até a pasta onde o arquivo foi salvo.
5. Execute o script com o comando:

```bash
python sistema_estoque.py
Observações
Case Insensitive: O sistema converte automaticamente o nome dos produtos digitados para letras maiúsculas (.upper()). Isso significa que "Maca", "MACA" e "maca" serão tratados como o mesmo item no estoque.

Dados Voláteis: Como este é um script de estudo/demonstração, os dados são salvos apenas na memória RAM (variáveis). Ao fechar o programa, o estoque e o histórico de vendas serão zerados.
