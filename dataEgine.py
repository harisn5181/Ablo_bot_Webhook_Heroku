
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete


from models import User, Contact, Base


communications = {}

in_users = 0
out_users = 0

engine = create_engine('sqlite:///Data.db',)

free_users = {}


    
import pymongo

client = pymongo.MongoClient(
    """mongodb+srv://harisn5181:thavakkal5181@cluster0.poiqa.mongodb.net/test?retryWrites=true&w=majority"""
)

db = client.test_collection  

try:
    db.create_collection("paradise_users")
except:

    print("exist")

collection = db.test_collection

import datetime

Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)

def add_users(chat=None, user_chat_id=None, username=None):
  try:

    """
    This function add new user in Data Base.
    Information about user_chat_id and username you can take from chat, but Data Base save only
    user_chat_id and username, so for interactions with DB, function use additional arguments:
    user_chat_id and username

    :param chat: It structure call.message.chat from telebot
    :param user_chat_id: Chat id with user
    :param username:
    :return:
    """
    
    global free_users
    global out_users
    global in_users

    if chat is not None:
        user_id = chat
        user_name = username

    else:
        user_id = user_chat_id
        user_name = username

   

    blocked_user=[5093542187,456913260,248009518,50919140250,1223776195,1781500643,5082992814,2111567791,2105715355,2118316448,2124786672,456913260,248009518,50919140250,1223776195,1781500643,5082992814,1105845958,1759821538,2039159352,850353581,668648018,507989958,585844365,5093542187,749925179,5093542187,986197680,2052007234,984439945,2143687742,2010780125,1930689346,5010208871,169170338,1631843898,1497207800, 972729001,1929660700,696090129,1093823695, 435800610,355799238]
    blocked=True
    for i in blocked_user:


       if chat is not None:
        user_id = chat
      

       else:
        user_id = user_chat_id

      
      




          

      
          
       if i==user_id:
         return


      
        
    

        






    if user_id in free_users.values():
        return

    if in_users >= out_users:
      
        free_users[user_id] = {
            'state': 0,
            'ID': user_id,
            'UserName': user_name
        }
        out_users = out_users + 1
    elif in_users < out_users:
        free_users[user_id] = {
            'state': 1,
            'ID': user_id,
            'UserName': user_name
        }
        in_users = in_users + 1

    post1 = {
              "user_id": user_id,
              
              "user_block4":1
            
          }



    posts1 = db.post1

    post_id = posts1.insert_one(post1).inserted_id
    
    posts1.update_one({"user_id": user_id}, {'$inc': {'user_block4': 1}})      

    s = session()
    if len(s.query(User).filter(User.id == user_id).all()) > 0:
        s.query(User).filter(User.id == user_id).update({'status': 0})

        s.commit()
        s.close()
        return

    import string    
    import random 
    S = 15  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    




    if user_name is None:
        user_name = ran

    s.add(User(id=user_id, username=user_name, like=False, status=0))

    s.commit()
    s.close()
  except Exception as e:
    
    print("\n") ,print("\n") ,print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n")

   
    print(e)
    print("\n")
    
    print("error during add users")













def delete_info(user_id):

    try:
        try:
            global communications
            tmp_id = communications[user_id]['UserTo']
            communications.pop(user_id)
            communications.pop(tmp_id)

        except Exception as e:
            print(e)
    except Exception as e:
        print(e)










 
  
    

h=0

def add_communications(user_id, user_to_id):
  try:
    """
    Add dialog in Data Base
    :param user_id: Chat id with first user
    :param user_to_id: Chat id with second user
    :return:
    """
    global free_users
    global h
   
    h=h+1
 

    communications[user_id] = {'UserTo': user_to_id, 'UserName': free_users[user_to_id]['UserName'], 'like': False}


    communications[user_to_id] = {'UserTo': user_id, 'UserName': free_users[user_id]['UserName'], 'like': False}
    

    print(h,communications[user_id], ' ', communications[user_to_id])

    free_users.pop(user_id)
    free_users.pop(user_to_id)

    s = session()

    s.query(User).filter(User.id == user_id).update({'status': 1})
    s.query(User).filter(User.id == user_to_id).update({'status': 1})

    s.add(Contact(userID=user_id, userToID=user_to_id))

    s.commit()
    s.close()
  except Exception as e:




    print("error due to add communication")  


def recovery_data():
  try:
    """
    This function recovers data from Data Base, if server was temporarily disabled
    :return:
    """
    global communications

    s = session()

    for i in s.query(Contact).all():
        first = s.query(User).filter(User.id == i.userID).first()
        second = s.query(User).filter(User.id == i.userToID).first()

        communications[i.userID] = {'UserTo': second.id, 'UserName': second.username, 'like': second.like}
        communications[i.userToID] = {'UserTo': first.id, 'UserName': first.username, 'like': first.like}

    for i in s.query(User).filter(User.status == 0).all():
        add_users(user_chat_id=i.id, username=i.username)

    s.close()
  except Exception as e:

    print("\n") ,print("\n") ,print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n"),  print("\n")

    print(e)
    print("\n")
    
    print(" recovery data")  


