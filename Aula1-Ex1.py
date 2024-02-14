# Definindo as variáveis de senha e email cadastrados
senha_cadastrada = "senha123"
email_cadastrado = "usuario@example.com"

# Loop principal para solicitar email e senha até que coincidam com os cadastrados
while True:
    # Solicitar email e senha ao usuário
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    # Verificar se o email e a senha digitados coincidem com os cadastrados
    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Login bem-sucedido!")
        break  # Encerrar o loop se as credenciais estiverem corretas
    else:
        print("Email ou senha incorretos. Tente novamente.")