# Lista de Usuário, onde cada usuário é um dicionário
usuarios = [
    {"tipo": "aluno", "matricula":"A001", "historico_emprestimos":[]},
    {"tipo": "professor", "matricula":"P001", "historico_emprestimos":[]},
    {"tipo": "funcionario", "matricula":"F001", "historico_emprestimos":[]}
]

print("Lista inicial de usuário: ")
for u in usuarios:
  print(u)
print()

livros = [
    {"isbn": "12345", "titulo": "Python para Iniciantes", "disponivel": True, "localizacao": "Estante A", "prazo_devolucao": None},
    {"isbn": "67890", "titulo": "Modelagem e Simulação", "disponivel": True, "localizacao": "Estante B", "prazo_devolucao": None},
]

print("Lista inicial de livro: ")
for l in livros:
  print(l)
print()

emprestimos_ativos = {}

bibliotecarios = [
    {"nome": "João", "turno": "manhã", "especialiazacao": None},
    {"nome": "Maria", "turno": "tarde", "especialiazacao": None}
]

print("Lista inicial de bibliotecarios: ")
for b in bibliotecarios:
  print(b)
print()

print('Lista inicial de usuários:')
for u in usuario:
  print(u)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('Lista inicial de Livros:')
for l in livros:
  print(l)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('Lista inicial de Bibliotecarios:')
for b in bibliotecarios:
  print(b)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

def encontrar_usuario(matricula):
  """
  funcao que encontra usuario retornando-o caso encontre ou retornando None caso não encontre

  args:
    matricula(str)
  return:
    usuario(dict) or none
  """
  for m in usuarios:
    if m['matricula'] == matricula :
      return m
  return None


def encontrar_livro(isbn):
  """
  funcao que encontra livro retornando-o caso encontre ou retornando None caso não encontre

  args:
    livro(str)
  return:
    livro(dict) or none
  """
  for l in livros:
    if l['isbn'] == isbn :
      return l
  return None


def emprestar_livro(matricula_usuario,isbn_livro):
  """
  funcao que empresta livro para o usuario

  verifica se usuario existe
  verifica se livro existe
  encontra livro e verifica se está disponivel
  adiciona ao historico de emprestimos do usuario e de emprestimos ativos

  args:
    matricula_usuario(str)
    isbn_livro(str)
  return:
    None
  """
  usuario_encontrado = encontrar_usuario(matricula_usuario)
  if usuario_encontrado is None:
    print('ERRO ao realizar o empréstimo: usuario não encontrado no sistema')
    return # encerra a função não executa nada que vem depois
  livro_encontrado = encontrar_livro(isbn_livro)
  if livro_encontrado is None:
    print('ERRO ao realizar o empréstimo: livro não encontrado na biblioteca')
    return

  for l in livros:
    if l['isbn'] == isbn_livro and l['disponivel'] == True:
      livro_encontrado['disponivel'] = False
      emprestimos_ativos[isbn_livro] = matricula_usuario
      for u in usuarios:
        if u['matricula'] == matricula_usuario:
          u['historico_emprestimos'].append(isbn_livro)
          print(f"Livro '{l['titulo']}' emprestado com SUCESSO para {u['tipo']} com matricula {matricula_usuario}!!!")
          return

  print(f"Livro '{l['titulo']}' não está disponível para emprestimo")



def devolver_livro(matricula_usuario,isbn_livro):
  """
  funcao que devolve livro para o usuario

  verifica se usuario existe
  verifica se livro existe
  encontra livro e verifica se está emprestado para a matricula do usuario
  retira o livro dos emprestimos ativos 

  args:
    matricula_usuario(str)
    isbn_livro(str)
  return:
    None
  """
  usuario_encontrado = encontrar_usuario(matricula_usuario)
  if usuario_encontrado is None:
    print('ERRO ao realizar a devolução: usuario não encontrado no sistema')
    return
  livro_encontrado = encontrar_livro(isbn_livro)
  if livro_encontrado is None:
    print('ERRO ao realizar a devolução: livro não encontrado na biblioteca')
    return

  for l in livros:
    if l['isbn'] == isbn_livro:
      if l['disponivel'] == True:
        print('Não é possível fazer a devolução pois o livro não está emprestado')
        return
      elif  l['disponivel'] == False and emprestimos_ativos.get(isbn_livro) != matricula_usuario:
        print('ERRO ao realizar a devolução: livro não está emprestado para esta matricula')
        return
      else:# l['disponivel'] == False
        l['disponivel'] = True
        del emprestimos_ativos[isbn_livro] # retira o livro dos emprestimos ativos
        for u in usuarios:
          if u['matricula'] == matricula_usuario:
            print(f"Livro '{l['titulo']}' devolvido com SUCESSO pelo {u['tipo']} de matricula {matricula_usuario}!!!")
        return

print('\n\t-=-=-=-=- SIMULAÇÃO BIBLIOTECA -=-=-=-=-')
emprestar_livro('A001','12345')
emprestar_livro('P001','67890')
emprestar_livro('A001','67890')
devolver_livro('A001','12345')
emprestar_livro('F001','12345')

print('\n\t-=-=-=-=- ESTADO FINAL DA SIMULAÇÃO -=-=-=-=-')

print('Lista dos livros com seus status:')
for l in livros:
  if l['disponivel'] == True:
    print(f"{l['titulo']} (ISBN:{l['isbn']}) : Disponível")
  else:
    print(f"{l['titulo']} (ISBN:{l['isbn']}) : Emprestado")

print('------')
print('Lista dos usuários com seus históricos de empréstimos:')
for u in usuarios:
  print(f"{u['tipo']} {u['matricula']}: Emprestimos:{u['historico_emprestimos']} ")

print('-------')


print('Lista dos Empréstimos ativos:')
for l in livros:
  if l['disponivel'] == False:
    for u in usuarios:
      if u['matricula'] == emprestimos_ativos[l['isbn']]:# emprestimo_ativos[l['isbn']] acessa o dicionario com chave isbn e retorna o valor da matricula
        print(f"{l['titulo']} (ISBN:{l['isbn']}) : Emprestado para {u['tipo']} com a matricula {emprestimos_ativos[l['isbn']]}")

