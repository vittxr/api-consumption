import requests

def get_users():
    res = requests.get('https://reqres.in/api/users').json()
    return res['data']
      #res é os dados que estão na api

global new_users__list
new_users__list = []
def post_newUser(name, email, avatar):
  if isUserCreated(name, email, avatar):
     return new_users__list
        #Se o usuário já estiver criado, retorna-se a lista, sem nenhuma implementação nova.
  else:
    data = {
          "first_name": f"{name}",
          "email": f"{email}",
          "avatar": f"{avatar}"
    }
  
    res = requests.post('https://reqres.in/api/users', data=data)
    new_users__list.append(res.json())
      #coloca-se os novos usuários em uma lista global, para ficar armazenadas. Caso fosse usado uma variável, p seria sobrescrito com o novo dado sempre que houvesse um novo post. Assim, guarda os dados dos novos usuários (isso até o server ser fechado...)

    return new_users__list
      #é preciso colocar o post em uma variável para conseguir trabalhar com ela.

def change_user(name, email, avatar):
    data = {
          "name": f"{name}",
          "email": f"{email}",
          "avatar": f"{avatar}"
    }
    res = requests.put('https://reqres.in/api/users', data=data)
    return data

def delete_user(user):
   res = requests.delete('https://reqres.in/api/users/'+ user['id'])
   return res

def isUserCreated(name, email, avatar):
   for user in new_users__list:
    if name == user['first_name'] or email == user['email'] or avatar == user['avatar']:
        return True
   return False