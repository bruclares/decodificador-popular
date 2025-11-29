# ✊ Decodificador Popular de Termos de Uso

**"Traduzindo a vigilância corporativa para a linguagem da classe trabalhadora."**

## 📋 Descrição do Projeto

O **Decodificador Popular** é uma ferramenta de autodefesa digital projetada para quebrar a assimetria de informação existente nos "Termos de Uso". Enquanto as Big Techs utilizam o "juridiquês" para esconder práticas de exploração de dados e vigilância, nossa ferramenta utiliza análise semântica para destacar e traduzir esses trechos para uma linguagem clara, direta e política.

O objetivo não é apenas resumir, mas **revelar a intenção**: onde a empresa diz "melhorar sua experiência", nós traduzimos para "monitoramento comportamental para fins publicitários".

## 🛠️ Tecnologias e Arquitetura

Priorizamos uma stack robusta, escalável e baseada em Código Aberto, evitando dependência de APIs proprietárias (como OpenAI/GPT) para garantir a soberania do processamento.

- **Backend:** Python com **Flask**.
- **Arquitetura:** Padrão **MVC** (Model-View-Controller) com uso de **Blueprints** para modularização de rotas.
- **Banco de Dados:** **PostgreSQL** (via Neon Tech) gerenciado com **SQLAlchemy** (ORM) e versionado com **Flask-Migrate**.
- **Frontend:** HTML5 Semântico, CSS3 (Design System próprio "Cyberpunk Sovereign") e JavaScript Vanilla (sem frameworks pesados para garantir acessibilidade em dispositivos low-end).
- **Infraestrutura/Deploy:** Vercel (Serverless).

## 🧪 Instruções de Teste e Validação

### 1. Acesso Rápido

O projeto está rodando em produção:
🔗 **[Acesse o Decodificador Popular](https://decodificador-popular.vercel.app/)**

### 2. Cenário de Validação: "O Entregador Monitorado"

Para validar a eficácia da ferramenta, simule a análise de um contrato de plataforma de trabalho:

1.  Acesse a ferramenta.
2.  Copie e cole o seguinte trecho (fictício, baseado em apps reais):
    > _"Nossos parceiros selecionados poderão coletar dados de localização em segundo plano para melhorar sua experiência e garantir a segurança do serviço. Ao continuar, você aceita o compartilhamento de dados inferidos."_
3.  Clique em **Decodificar Vigilância**.
4.  **Resultado Esperado:**
    - O termo _"parceiros selecionados"_ será grifado, revelando: "Empresas terceiras que compraram seus dados".
    - O termo _"melhorar sua experiência"_ revelará: "Monitorar seu comportamento para criar perfil de consumo".
    - O termo _"dados inferidos"_ revelará a criação de perfis psicológicos não autorizados explicitamente.

## 🔍 Metodologia e Semiótica

A "IA" do projeto é simbólica e determinística. Criamos um dicionário de padrões semióticos baseados em três categorias de manipulação:

1.  **Suavização (Eufemismo):** Palavras que fazem a vigilância parecer um benefício.
2.  **Ocultação de Agência:** Frases na voz passiva que escondem quem está lucrando com o dado.
3.  **Coerção:** Termos que forçam um consentimento sem alternativa real.

## 🚧 Obstáculos e Aprendizados

Durante o desenvolvimento no hackathon, o maior desafio foi a transição do ambiente de desenvolvimento local (SQLite) para a arquitetura Serverless (Vercel + Postgres).
Isso exigiu a implementação de **Variáveis de Ambiente** robustas e uma estratégia de conexão com banco de dados que suportasse o ciclo de vida efêmero das funções serverless, garantindo que a ferramenta permaneça gratuita e sustentável a longo prazo.

---

_Projeto desenvolvido para o Hackathon Soberania Digital 2025._
