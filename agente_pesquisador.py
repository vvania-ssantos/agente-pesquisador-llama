import subprocess
import os

# ---------------------------
# Função para chamar o modelo LLaMA via Ollama
# ---------------------------

def chamar_modelo(prompt):
    comando = ["ollama", "run", "llama3.2", prompt]
    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()


# ---------------------------
# Ferramenta do agente: leitura de arquivos locais
# ---------------------------

def ler_arquivo(caminho):
    if not os.path.exists(caminho):
        return "Arquivo não encontrado."
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Erro ao tentar ler o arquivo."


# ---------------------------
# Agente Pesquisador
# ---------------------------

def agente_pesquisador(pergunta, arquivo=None):

    conteudo = ""
    if arquivo:
        conteudo = ler_arquivo(arquivo)

    prompt_sistema = f"""
Você é um AGENTE PESQUISADOR.
Seu objetivo é analisar perguntas, usar ferramentas quando necessário e responder com clareza.

Ferramenta disponível:
- Leitura de arquivos (.txt, .md)

Conteúdo do arquivo (se houver):
{conteudo}

Agora responda à pergunta abaixo de forma objetiva e estruturada.
"""

    prompt_final = f"{prompt_sistema}\nPergunta: {pergunta}\nResposta:"

    resposta = chamar_modelo(prompt_final)
    return resposta


# ---------------------------
# Execução direta via terminal
# ---------------------------

if __name__ == "__main__":
    print("=== AGENTE PESQUISADOR ===")
    pergunta = input("Digite sua pergunta: ")
    arquivo = input("Se desejar, indique o caminho do arquivo (.txt ou .md): ")
    arquivo = arquivo.strip() if arquivo else None

    print("\nAGENTE RESPONDE:\n")
    print(agente_pesquisador(pergunta, arquivo))
