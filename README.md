# Projeto NumenIT Demo AMS

## Descrição
Sistema simples de administração de tarefas.

## Estrutura do Projeto

### 1. Página de Autenticação
- Tipo de Usuário Cliente
- Tipo de Usuário Gerente de Projeto
- Tipo de Usuário Desenvolvedor
- Tipo de Usuário Gerente Geral*

### 2. Página Dashboard
- Exibir (dependendo do usuário) relatório de horas e chamados por cliente
- Navegação:
    - Página "Dashboard"
    - Página "Administrar Tarefas"
    - Página "Gerenciador de Segredos"
    - Página "Base de Conhecimento"
    - Página "Timesheet"

### 3. Banco de Dados

#### Usuário
- ID
- TP Usuário
- Login
- Senha (hash)
- Nome
- Data início
- Data fim

#### Cliente
- ID cliente
- Nome Cliente
- Identificação
- Telefone
- Email
- Responsável
- Segmento

#### Dados Projeto
- ID projeto
- Nome do Projeto
- Descrição do Projeto
- Horas de Alocação do Gerente
- Data início contrato
- Data fim contrato

#### Projeto x Recurso(s)
- ID projeto
- ID gerente
- ID recurso
- Hr. Alocação Recurso
- Data início contrato recurso
- Data fim contrato recurso

#### Chamado x Projeto
- ID chamado
- ID projeto
- Tp. Chamado
- User Abertura
- Descrição
- Módulo
- Status
- Data Abertura
- Data Atualização (Calculado)
- Recurso Alocado
- Horas Estimadas
- Horas Aprovadas
- Horas Gastas (Calculado)
- Gerente (Calculado)
- Alterado Por (Calculado)
- Segmento (Calculado)
- Data Apr. Horas
- Tipo de Contrato (Calculado)
