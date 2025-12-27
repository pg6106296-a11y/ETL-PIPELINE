import pandas as pd

# -----------------------------
# 1. EXTRAÇÃO
# -----------------------------
# Lê os dados fictícios de um arquivo CSV
usuarios = pd.read_csv("usuarios.csv")

print("Dados extraídos:")
print(usuarios)

# -----------------------------
# 2. TRANSFORMAÇÃO
# -----------------------------
# Cria mensagens personalizadas para cada usuário
usuarios["mensagem"] = usuarios.apply(
    lambda row: f"Olá {row['nome']}, sua conta {row['conta']} está vinculada ao cartão {row['cartao']}.",
    axis=1
)

print("\nMensagens geradas:")
print(usuarios[["nome", "mensagem"]])

# -----------------------------
# 3. CARREGAMENTO
# -----------------------------
# Salva as mensagens em um novo arquivo CSV
usuarios[["nome", "mensagem"]].to_csv("mensagens.csv", index=False)

print("\nMensagens salvas em mensagens.csv")

