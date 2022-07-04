from os.path import exists

def get_userdata(users): 
   global usuarios
   usuarios = {}
   if not exists('static/data/dados.csv'):
      #quero adicionar os dados da api aqui apenas uma vez.
      #exists() verifica se o arquivo existe
      with open("static/data/dados.csv", "a") as file:
         for user in users: 
            linha=f"{user['first_name']};{user['email']};{user['avatar']};{user['id']}\n"
            file.write(linha)

   with open('static/data/dados.csv', 'r') as file:
      file = file.read()
      dados = file.split('\n')

      global i 
      i = 0
      for dado in dados:
            user = dado.split(";")
            
            if len(user) > 1:
               user_dict = {
                  "name": user[0],
                  "email": user[1],
                  "avatar": user[2],
                  "id": user[3]
               }

               usuarios[f'user{i}'] = user_dict
               i+=1
   return usuarios

def post_userdata(newUser):
    with open("static/data/dados.csv", "a") as file:
      for user in newUser: 
         linha=f"{user['first_name']};{user['email']};{user['avatar']};{user['id']}\n"
         file.write(linha) #Cria o usário com as informações inputadas.

def change_userdata(userToBeChanged, newUserData):
   #vou ter que colocar numa variável o usuário para ser alterado, pois user é o usuário inputado no form...
   newUserData['id'] = userToBeChanged['id']
      #mantem-se o id do usuário

   #lê todas linhas
   with open('static/data/dados.csv', 'r') as file:
      global lines
      lines = file.readlines()

   global i 
   i=0
   while i < len(lines):
      line_ = lines[i].replace('\n', '') 
      line__ = line_.split(';')
      if line__[1] == userToBeChanged['email']:
         print("ae deu certo") 
         lines[i] = f"{newUserData['name']};{newUserData['email']};{newUserData['avatar']};{newUserData['id']}\n"
      i+=1
   
   #rescreve as linhas com a linha alterada:
   with open ('static/data/dados.csv', 'w') as file:
      file.writelines(lines)

def delete_userdata(result):
   usuarios = []
   global prevUser
   prevUser = ''
   with open('static/data/dados.csv', 'r') as file:
      data = file.read()
      linhas = data.split('\n')

      for linha in linhas:
         user = linha.split(";")

         if len(user) > 1: 
            user_dict = {
               "name": user[0],
               "email": user[1],
               "avatar": user[2],
               "id": user[3]
            }

         if user_dict['name'] == 'slapo':
            if user_dict == result: 
               print('dicion igual')
            else: 
               print('dicio diferente')

            print(user_dict)
            print(result)
  
         if user_dict == result: 
            print('aeeeee')
         
         if user_dict != result and user_dict != prevUser:
            #Para não dar bug, é preciso de uma variável auxiliar que contenha o usuário anterior. Isso para que o usuário não seja colocado na lista duas vezes ou mais.
            usuarios.append(user_dict)
         prevUser = user_dict
         

   with open('static/data/dados.csv', 'r+') as file:
      #apaga-se o arquivo inteiro, para rescreve-lo no próximo with open.
      file.truncate()

   with open('static/data/dados.csv', 'a') as file:
      #o arquivo é rescrito, sem o usuário que foi deletado.
      for user in usuarios:
         file.write(f"{user['name']};{user['email']};{user['avatar']};{user['id']}\n")