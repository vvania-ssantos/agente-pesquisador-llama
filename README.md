# 🧠 Agente Pesquisador com LLaMA 3.2 (via Ollama)

Este projeto apresenta um **agente de pesquisa local**, desenvolvido em **Python**, que utiliza o modelo **LLaMA 3.2** através da plataforma **Ollama** para:

- analisar perguntas,
- interpretar arquivos `.txt` ou `.md`,
- sintetizar informações,
- gerar respostas estruturadas,
- realizar raciocínio baseado em contexto.

É um projeto demonstrativo para estudo de **IA local**, **sistemas multiagentes** e **raciocínio assistido por LLM**.

---

## ✨ Funcionalidades

- 🔍 **Lê arquivos externos** (texto ou markdown)
- 🧠 **Analisa pergunta + conteúdo do arquivo**
- 📝 **Gera resposta detalhada e estruturada**
- ⚡ **Roda totalmente offline** usando Ollama
- 📂 **Código simples e direto** para aprendizado
- 🤖 **Base ideal para agentes mais avançados**

---

## 🧰 Tecnologias Utilizadas

- **Python 3.10+**
- **Ollama**
- **Modelo LLaMA 3.2**
- `subprocess` para comunicação com o modelo local
- Estrutura de agente com raciocínio programado

---

## 🚀 Como Executar

### **1. Instale o Ollama**
Baixe e instale em:

👉 https://ollama.com/download

### **2. Baixe o modelo LLaMA 3.2**
```bash
ollama pull llama3.2
3. Execute o agente

python agente_pesquisador.py
Você verá:

=== AGENTE PESQUISADOR ===
Digite sua pergunta:

📂 Exemplo de Uso
Pergunta:
Qual o maior animal do planeta?
Arquivo teste.txt:
A baleia-azul é o maior animal do planeta.
Ela pode chegar a 30 metros de comprimento.

Saída do agente:
A baleia-azul é o maior animal do planeta.

📦 Estrutura do Projeto

📁 agente-pesquisador-llama
 └── agente_pesquisador.py

🛠️ Melhorias Futuras
Suporte a PDF
Análise multi-documento
Modo “pesquisador profundo”
Exportação das respostas em Markdown
Versão multiagente

👩‍💻 Autora
Vania dos Santos
Analista de Dados | Engenharia da Computação | Estudando IA e Multiagentes
Projetos em Python, PostgreSQL, NLP e Sistemas Inteligentes

⭐ Contribuições
Sugestões, melhorias ou pull requests são sempre bem-vindos!
