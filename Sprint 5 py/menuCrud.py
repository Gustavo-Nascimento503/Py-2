import cx_Oracle

def inserir_usuario():
    try:
        dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')

        conn = cx_Oracle.connect(user='Seu usuario', password='Sua senha', dsn=dsn)# Altere para suas credenciais

        cursor = conn.cursor()

        id = input('Digite o ID do usuário a ser inserido: ')
        nome = input('Digite o nome do usuário a ser inserido: ')

        if not id or not nome:
            print('ID e/ou nome não preenchidos.')
            return

        cursor.execute("INSERT INTO TB_USUARIO2 (ID, NOME) VALUES (:valor1, :valor2)", valor1=id, valor2=nome)
        conn.commit()

        print('Registro incluído com sucesso!')

    except cx_Oracle.Error as e:
        print('Erro ao inserir registro:', e)

    finally:
        cursor.close()
        conn.close()

while True:
    op = int(input("Digite a opção desejada: "))

    if op == 1:
        inserir_usuario()
    else:
        print("Encerrando o programa")
        exit()