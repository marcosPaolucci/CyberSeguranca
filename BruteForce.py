import PyPDF2

# Função para tentar desbloquear o PDF com todas as combinações numéricas de até 3 dígitos
def quebrar_senha_pdf(pdf_path):
    pdf = PyPDF2.PdfReader(pdf_path)
    
    # Loop através de todos os números de 0 a 999 para todas as combinações de 3 dígitos
    for i in range(1000):
        senha = f"{i:03}"  # Formatar o número com 3 dígitos (0 à esquerda se necessário)
        
        # Tente desbloquear o PDF com a senha atual
        if pdf.decrypt(senha):
            print("Senha encontrada:", senha)
            return senha
    
    # Se nenhuma senha correta for encontrada
    print("Nenhuma senha encontrada.")
    return None

# Nome do arquivo PDF no mesmo diretório do script
pdf_nome = "PASS_protected.pdf"

# Tentar quebrar a senha do PDF
senha_correta = quebrar_senha_pdf(pdf_nome)

# Se a senha foi encontrada, abrir o PDF
