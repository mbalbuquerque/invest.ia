# Invest.AI 📈🤖

**Invest.AI** é uma plataforma inteligente de apoio ao investidor, desenvolvida para reunir educação financeira, análise de perfil, acompanhamento de carteira, simulações e inteligência artificial em uma experiência simples e moderna.

A proposta é ajudar o usuário a **entender melhor seus investimentos e tomar decisões mais conscientes**, utilizando dados, motores financeiros e IA para transformar informações complexas em análises compreensíveis.

> **Uma IA que entende não apenas onde você investe, mas como você investe.**

---

## 🎯 Objetivo do projeto

O Invest.AI está sendo desenvolvido para permitir que investidores acompanhem sua evolução financeira e compreendam melhor seu próprio comportamento.

A plataforma deverá combinar:

* perfil do investidor;
* comportamento financeiro;
* carteira de investimentos;
* objetivos financeiros;
* simulações;
* informações do mercado;
* análise de risco;
* inteligência artificial.

A IA será utilizada principalmente para **interpretar informações, identificar padrões e explicar resultados**, enquanto cálculos financeiros e regras de negócio serão tratados por componentes específicos e auditáveis.

---

## 🧠 Perfil Vivo do Investidor

Um dos principais conceitos do Invest.AI é o **Perfil Vivo**.

Em vez de considerar apenas o questionário tradicional de suitability, a plataforma deverá acompanhar também o comportamento do investidor ao longo do tempo.

O sistema poderá trabalhar com três perspectivas:

### Perfil Declarado

Obtido através do questionário inicial de perfil do investidor.

### Perfil Observado

Calculado a partir do comportamento e da composição da carteira.

### Perfil Recomendado

Considera fatores como:

* objetivos financeiros;
* horizonte de investimento;
* necessidade de liquidez;
* tolerância ao risco;
* capacidade financeira;
* composição patrimonial.

Isso permitirá identificar divergências entre aquilo que o investidor declara e a forma como efetivamente investe.

---

## 💼 Investimentos previstos

A plataforma está sendo planejada para trabalhar com diferentes classes e produtos financeiros.

### Renda fixa

* Tesouro Direto
* CDB
* LCI
* LCA
* outros produtos de renda fixa

### Previdência privada

* PGBL
* VGBL
* aportes periódicos
* projeções de aposentadoria
* comparação de cenários

### Renda variável

* ações
* ETFs
* FIIs
* fundos

### Investimentos internacionais

* ETFs internacionais
* fundos
* exposição cambial

### Ativos alternativos

* Bitcoin
* outros criptoativos

Criptoativos serão tratados considerando volatilidade, concentração, exposição patrimonial e riscos relacionados à custódia.

---

## 📰 Radar do Mercado

A landing page possui um **Radar do Mercado**, desenvolvido para apresentar informações e notícias relevantes para investidores.

Entre as fontes consideradas estão:

* Valor Econômico
* CVM
* B3
* XP
* BTG Pactual
* Genial Investimentos
* Clear
* outras fontes especializadas

A evolução prevista é permitir que o agente de IA responda:

> **“Como esta notícia pode impactar minha carteira?”**

O objetivo é transformar notícias de mercado em informações contextualizadas para cada investidor.

---

## 🧮 Simuladores

A plataforma deverá disponibilizar simuladores financeiros para diferentes objetivos.

Entre eles:

* aposentadoria;
* previdência privada;
* evolução patrimonial;
* aportes mensais;
* comparação entre investimentos;
* LCI x LCA x CDB;
* objetivos financeiros;
* impacto de diferentes cenários sobre a carteira.

Os cálculos serão executados por motores financeiros próprios, evitando que valores matemáticos dependam exclusivamente de respostas produzidas pelo modelo de IA.

---

## 🤖 Agente de Inteligência Artificial

O agente Invest.AI deverá utilizar informações autorizadas pelo usuário para compreender:

```text
Perfil do investidor
        +
Carteira
        +
Objetivos
        +
Comportamento
        +
Simulações
        +
Dados financeiros
        ↓
     Agente IA
        ↓
Análises e explicações
```

Exemplos de perguntas futuras:

* Minha carteira está muito concentrada?
* Meu perfil mudou?
* Estou assumindo risco acima do meu perfil?
* Quanto preciso investir para minha aposentadoria?
* LCI ou CDB faz mais sentido para meu objetivo?
* Qual o impacto de uma queda do mercado na minha carteira?
* Quanto Bitcoin representa no risco total da minha carteira?
* Como determinada notícia pode afetar meus investimentos?

---

## 📊 Dashboard

O dashboard está planejado para apresentar informações como:

* patrimônio total;
* distribuição da carteira;
* evolução patrimonial;
* perfil do investidor;
* score de risco;
* concentração;
* diversificação;
* objetivos;
* alertas;
* oportunidades de análise;
* acesso ao agente de IA.

---

## 📱 Progressive Web App — PWA

A primeira versão do Invest.AI está sendo desenvolvida como uma **Progressive Web App (PWA)**.

Isso permitirá uma experiência semelhante à de um aplicativo, incluindo instalação em dispositivos compatíveis.

Atualmente o projeto possui:

* Landing Page responsiva
* Manifest PWA
* Service Worker
* Cache básico
* Ícones do aplicativo
* Suporte à instalação
* Layout adaptado para desktop e dispositivos móveis
* Radar do Mercado

---

## 🏗️ Arquitetura planejada

A evolução da plataforma prevê:

```text
PWA / Frontend
       │
       ▼
Django / API
       │
 ┌─────┼─────────────┐
 │     │             │
 ▼     ▼             ▼
Perfil Carteira  Simuladores
 │     │             │
 └─────┼─────────────┘
       ▼
 Motores Financeiros
       │
       ▼
   Agente de IA
       │
       ▼
Dados e fontes externas
```

### Tecnologias previstas

**Frontend**

* HTML5
* CSS3
* JavaScript
* PWA

**Backend**

* Python
* Django
* Django REST Framework

**Banco de dados**

* PostgreSQL

**Inteligência Artificial**

* integração via API
* ferramentas financeiras internas
* contexto da carteira e perfil
* recuperação de informações financeiras

---

## 📂 Estrutura atual

```text
invest-ai/
│
├── index.html
├── styles.css
├── script.js
├── manifest.webmanifest
├── sw.js
│
├── icons/
│   ├── icon-192.png
│   └── icon-512.png
│
├── .gitignore
└── README.md
```

A estrutura será ampliada conforme o backend Django for implementado.

---

## 🚧 Status do projeto

**Em desenvolvimento.**

### Concluído

* [x] Definição inicial do produto
* [x] Conceito do agente de IA
* [x] Conceito de Perfil Vivo
* [x] Definição inicial dos produtos financeiros
* [x] Protótipo visual
* [x] Landing Page
* [x] Estrutura PWA
* [x] Radar do Mercado

### Próximas etapas

* [ ] Cadastro e autenticação
* [ ] Questionário do perfil do investidor
* [ ] Motor de scoring
* [ ] Perfil Vivo
* [ ] Dashboard
* [ ] Cadastro da carteira
* [ ] Simulador de previdência privada
* [ ] Comparador de renda fixa
* [ ] Objetivos financeiros
* [ ] Histórico comportamental
* [ ] Integração com agente de IA
* [ ] Integração com fontes financeiras
* [ ] Alertas inteligentes

---

## 🔐 Segurança

Por se tratar de uma plataforma relacionada a informações financeiras, segurança e privacidade deverão fazer parte da arquitetura desde o início.

Entre os princípios previstos estão:

* proteção de dados pessoais;
* controle de acesso;
* autenticação segura;
* criptografia de informações sensíveis;
* registro de eventos relevantes;
* separação entre cálculos e respostas da IA;
* rastreabilidade das análises;
* transparência sobre fontes utilizadas.

---

## ⚖️ Aviso importante

O Invest.AI encontra-se em desenvolvimento.

As funcionalidades de análise, simulação e inteligência artificial não devem ser interpretadas automaticamente como promessa de rentabilidade ou garantia de resultados.

Antes da disponibilização comercial de funcionalidades envolvendo recomendações individualizadas de investimentos, deverão ser avaliados os requisitos legais, regulatórios e de suitability aplicáveis.

---

## 🗺️ Roadmap

### Fase 1 — Fundação

Landing Page, PWA, identidade visual e arquitetura.

### Fase 2 — Investidor

Cadastro, autenticação, questionário e Perfil Vivo.

### Fase 3 — Carteira

Patrimônio, investimentos, concentração, diversificação e risco.

### Fase 4 — Planejamento

Objetivos, previdência e simuladores financeiros.

### Fase 5 — Inteligência Artificial

Agente contextualizado com perfil, carteira e objetivos.

### Fase 6 — Mercado

Dados financeiros, Radar do Mercado e análise contextualizada de notícias.

### Fase 7 — Evolução

Alertas inteligentes, acompanhamento comportamental e integrações financeiras.

---

## 📌 Versão

**Versão inicial:** `0.1.0`

Projeto em fase de desenvolvimento e validação do MVP.

---

**Invest.AI**

*Inteligência para entender seu dinheiro. Clareza para decidir seu futuro.*
