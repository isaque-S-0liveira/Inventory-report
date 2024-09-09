# Inventory Report

## Contexto

O foco principal deste projeto é, com base nos ensinamentos da **Trybe**, desenvolver um gerador de relatórios de estoque. O objetivo é processar dados de estoque que podem ser fornecidos através de dois formatos de arquivo diferentes: **CSV** e **JSON**. A aplicação deve ser capaz de ler esses arquivos, importar os dados de forma estruturada e gerar relatórios que resumem as informações contidas no estoque.

<details>
  <summary>O que é a Trybe?🤔</summary>
  A Trybe é uma escola de desenvolvimento web genuinamente comprometida com o sucesso profissional de seus estudantes. Com o Modelo de Sucesso Compartilhado (MSC) oferecido pela Trybe Fintech, uma instituição financeira autorizada pelo Banco Central do Brasil, os alunos têm a opção de pagar apenas quando estiverem trabalhando.
</details>


O projeto é composto por várias etapas, como a criação de testes para garantir o correto funcionamento dos objetos e métodos, implementação de classes que herdam de interfaces para lidar com diferentes formatos de arquivo, e o desenvolvimento de um sistema de relatórios que pode produzir resumos simples ou completos dos itens em estoque.

### Funcionalidades e Tarefas Principais:

1. **Teste de Inicialização do Produto**:
   - Implementação de testes para garantir que o objeto `Product` possui os atributos corretos quando é instanciado.
   
2. **Relatório Individual de Produtos**:
   - Teste para validar se o método mágico `__str__` do objeto `Product` retorna as informações corretamente formatadas.

3. **Criação de Interface para Importação**:
   - Implementação de uma interface abstrata chamada `Importer`, que define o método `import_data`, responsável pela importação dos dados.

4. **Leitura de Arquivos JSON**:
   - Implementação da classe `JsonImporter`, que herda da interface `Importer` e implementa a lógica para leitura e processamento de arquivos no formato **JSON**.

5. **Gestão de Estoque**:
   - Criação da classe `Inventory`, que será responsável por armazenar os itens em estoque e permitir a adição de novos produtos.

6. **Sistema de Relatórios**:
   - Criação de um protocolo para gerar relatórios, que será utilizado como contrato para a criação de diferentes tipos de relatórios, como relatórios simples e completos.

### Habilidades Desenvolvidas:
- **Programação Orientada a Objetos (POO)**: Modelagem de produtos e estoque utilizando classes e objetos, aplicando conceitos de herança e abstração.
- **Leitura e Manipulação de Arquivos**: Leitura de arquivos nos formatos **CSV** e **JSON** para importar dados de estoque.
- **Testes Automatizados**: Criação de testes unitários para validar o comportamento correto das classes e métodos.
- **Gerador de Relatórios**: Implementação de um sistema flexível de relatórios para exibir informações detalhadas sobre o estoque.

---

## Tecnologias Usadas

- [Python](https://www.python.org/) - Linguagem de programação utilizada para o desenvolvimento do projeto.
- [Pytest](https://docs.pytest.org/en/7.0.x/) - Framework de testes utilizado para validar as funcionalidades e garantir a qualidade do código.
- **CSV & JSON Handling** - Manipulação de arquivos nos formatos **CSV** e **JSON** para importação e processamento de dados.
- **Programação Orientada a Objetos (POO)** - Paradigma de programação utilizado para estruturar o código e modelar as entidades como `Product`, `Inventory`, e `Importer`.
- **Protocolos e Interfaces** - Implementação de interfaces e protocolos para garantir contratos de funcionalidade entre as diferentes classes do sistema.



## Entre em contato:
<a href="mailto:zazac3179@gmail.com" target="_blank">
  <img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" height="40" width="auto" />
</a>
<a href="https://www.linkedin.com/in/isaque-s-oliveira/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="isaque oliveira" height="30" width="40" /></a>
<a href="https://wa.me/5574981510614" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" /></a>
