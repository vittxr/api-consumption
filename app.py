#Tarefas: 
   #renomear as variáveis  

import json
from flask import Flask, redirect, url_for, render_template, request
from os.path import exists

from static.python.manageApi import get_users, post_newUser, change_user, delete_user
from static.python.dataHandler import get_userdata, post_userdata, change_userdata, delete_userdata

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
   users = get_users()
     #get_users na api 
   usuarios = get_userdata(users)
     #get_users no arquivo

   return render_template("index.html", users=usuarios)

@app.route('/', methods = ['POST'])
def add_newUser():
   user_list = get_users()
      #dado da api

   if request.method == 'POST': 
        name = request.form.get('name')
        email = request.form.get('email')
        avatar = request.form.get('avatar')
            #Essas são as três variáveis inputados no form

        newUser = post_newUser(name, email, avatar)
        post_userdata(newUser)

        
   return redirect(url_for('index'))

@app.route('/change', methods = ['POST'])
def change():
   if request.content_type == 'application/json': 
      #já que estou enviando a informação de duas formas diferentes (pelo action e pelo ajax), é preciso verificar o tipo do conteúdo para evitar de dar erro, pois o request.get_json() só funcionará se conteúdo do request for json. 
      userToBeChanged = request.get_json()

      global userToBeChanged_json
      userToBeChanged_json = json.loads(userToBeChanged)

   if request.method == 'POST': 
      name = request.form.get('name')
      email = request.form.get('email')
      avatar = request.form.get('avatar')
         #Essas são as três variáveis inputados no form

      global newUserData
      newUserData = change_user(name, email, avatar)
      if name != None and email != None and avatar != None: 
         change_userdata(userToBeChanged_json, newUserData)
 
   return redirect(url_for('index'))



@app.route('/delete', methods=['POST'])
   #embora eu quero deletar os dados, primeiro preciso envia-los a função abaixo... O delete é feito apenas na API, com o dado postado nessa rota. (>> não sei se essa ideia é a correta << )
def delete():
   output = request.get_json()
   print(output)
   result = json.loads(output)

   res = delete_user(result)
      #delete user na api

   delete_userdata(result)
      #delete user no arquivo 

   return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = 1)