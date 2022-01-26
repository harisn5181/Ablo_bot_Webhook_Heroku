

import threading

import time
import random
import os
import telebot
from telebot import types
from Messages import *
from dataEgine import *
from telebot.apihelper import ApiTelegramException
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5032197084:AAHJ0sp9VtOFgWz0GzOrTM0t_AbiGqBY46Q'
bot = telebot.TeleBot(TOKEN)


def caps(update, context):
  print("caps")
  

  text_caps = "hi how are you"
  context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)



def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
    user_id=message.chat.id
    bot.send_message(user_id,"hi how are you")



def rules(update,context):

  try:

     user_id = update.effective_chat.id

  
     context.bot.send_message(user_id,rules_msg,parse_mode="HTML")



  except:
      print("error-rules")

    

#reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)








p=0
k=0
m=0

f=0
g=0

def inline_menu():
    """
    Create inline menu for new chat
    :return: InlineKeyboardMarkup
    """
    #callback = types.InlineKeyboardButton(text='\U0001f680 1.Join Community  Group ',url="https://t.me/joinchat/v0Wc6hFsoJk4OTc9")
  

    feedback = types.InlineKeyboardButton(text='\U0001f699 Join Community Channel',url="https://t.me/Paradisechatchannell" )
    menu = types.InlineKeyboardMarkup()
    #menu.add(callback)
    menu.add(feedback)

    return menu





def inline1_menu():
  """
  Create inline menu for new chat
  :return: InlineKeyboardMarkup
  """
  callback = types.InlineKeyboardButton(text='REPORT 👉 ', callback_data='/report')


  #feedback = types.InlineKeyboardButton(text='\U0001f699 feedback', callback_data='/feedback')

  menu = types.InlineKeyboardMarkup()
  menu.add(callback)
  #menu.add(feedback)

  return menu



def connect_user(user_id):
    



    if user_id in communications:
        return True
    else:
        bot.send_message(user_id,m_disconnect_user1,parse_mode="HTML")


        








        return False







def report(context,update):
  try:
    user_id = update.effective_chat.id
    context.bot.send_message(user_id,"report message is sended to admin",parse_mode="HTML")
  except:
    print("error-/report not call report")


  







@bot.callback_query_handler(func=lambda call: True)
def echo(call):


  try:

  
  
    if call.data == '/report':
      user_id = call.message.chat.id

      if user_id in communications:


        user_id = call.message.chat.id
        user_to_id = communications[user_id]['UserTo']
      




        post1 = {
                
                "user_reported": user_to_id,
                
                "report":0
              
            }



        posts1 = db.post1

        post_id = posts1.insert_one(post1).inserted_id
        posts1.update_one({"user_reported": user_to_id}, {'$inc': {'report': 1}})
    

      
    
        print("a")

        a=posts1.find_one({"user_reported": user_to_id})
    
        flag1=False
        b=(a.get('report'))  
      

        report_msg_print=(" you are getting report %d times" % b)
        print(report_msg_print)
      
        
              
        
    
        bot.send_message(user_id,report_msg,parse_mode="HTML")


        bot.send_message(communications[user_id]['UserTo'], """Your partner reported you...if you flirted your partner about sexualiy, your account will permanently ban. otherwise no need to worry.some people will report without any reason """,parse_mode="HTML")


        bot.send_message(communications[user_id]['UserTo'],report_msg_print)



        
      else:
        user_id = call.message.chat.id

        
        bot.send_message(user_id, report_previous_user,parse_mode="HTML")
      
      
  except Exception as e:
    print(e)

    print("error during report")





def admin(context,update):
  try:
    user_id = update.effective_chat.id
    context.bot.send_message(user_id,msg_admin)

  except:
    print("error-admin")



def support(context,update):
  try:
    user_id = update.effective_chat.id

    context.bot.send_message(user_id,support_msg)

  except:
    print("error-support")


def sharelink(context,update):   
  try:

  
    user_id = update.effective_chat.id

    if user_id not in communications:
  
        context.bot.send_message(user_id, m_has_not_dialog,parse_mode="HTML")
        return

    user_to_id = communications[user_id]['UserTo']
    if update.effective_chat.username is None:
      context.bot.send_message(user_id, m_is_not_user_name,parse_mode="HTML") 
      return
  

    context.bot.send_message(user_id,m_sharelink)

    
    context.bot.send_message(user_to_id,sharelink,parse_mode="HTML")
    context.bot.send_message(user_to_id, m_all_like(communications[user_to_id]['UserName']))
          
  except:
    
    print("error during sharelink command")  




    
        
  


def help(context,update):

  try:
    user_id = update.effective_chat.id

    if user_id in communications:
            user_id = update.effective_chat.id
          
              
            menu = types.ReplyKeyboardRemove()
            menu = inline_menu()

            context.bot.send_message(user_id,"<b> 🔗join the official channel and and community group.Paradisers from all around the globe is talking there🔗</b>", reply_markup=menu,parse_mode="HTML")
      
    else:
      user_id = update.effective_chat.id
      menu = types.ReplyKeyboardRemove()
      menu = inline_menu()

      context.bot.send_message(user_id,"<b> 🔗join the official channel and and community group.Paradisers from all around the globe is talking there🔗</b>", reply_markup=menu,parse_mode="HTML")
      
    
    
  except:

    print("error during share community")


  

def next(update, context):
  try:
    try:
            user_id=update.effective_chat.id
        

          
            not_found = False
            join= bot.get_chat_member(-1001744633800, user_id,)
            if (join.status == "kicked") or (join.status == "left") or not_found == True:



              not_found = True    
            flag=False  
            if   not_found == True:




              
              menu = types.ReplyKeyboardRemove()
              menu = inline_menu()

              context.bot.send_message(user_id,"<b> 🔗Before use paradise chat bot.You need to join the official channel and come back.Then press /start 🔗</b>", reply_markup=menu,parse_mode="HTML")

          
              flag=True
            
              
            if flag==True:

                return






            
        

        

              
            

              
          
                
      
    except Exception as e:
      print(e)

      print("error during channel adding")     






    try:


      


        Flag=False
    
        if update.effective_chat.id in communications:
            user_id=update.effective_chat.id

          
      
            context.bot.send_message(communications[user_id]['UserTo'], m_disconnect_user,parse_mode="HTML")

            tmp_id = communications[user_id]['UserTo']
            delete_info(tmp_id)




      
            





            time.sleep(0.3)




            global p
            p=p+1
            print(p)
            if p==8:

              p=0
              update.effective_chat.id
              context.bot.send_message(user_id,m_is_not_free_users ,parse_mode="HTML")




      
              
        if Flag==False:

          
          user_id = update.effective_chat.id
          
          context.bot.send_message(user_id,m_is_not_free_users3 ,parse_mode="HTML") 
        
        
    
      

        user_id = update.effective_chat.id
        user_to_id = None
    
        add_users(chat= update.effective_chat.id,username=update.effective_chat.username)
  

    
        
        if len(free_users) < 2:  
            return
        
        
          

        if free_users[user_id]['state'] == 0:
              return


        for user in free_users.values():
              if user['state'] == 0:
                    user_to_id = user['ID']
                    break

        if user_to_id is None:
          
            return



        add_communications(user_id, user_to_id)

        context.bot.send_message(user_id, m_is_connect,parse_mode="HTML")
        context.bot.send_message(user_to_id, m_is_connect,parse_mode="HTML") 
            

    except ApiTelegramException as ex:

        tmp_id = communications[user_id]['UserTo']
        user_id = update.effective_chat.id

        communications.pop(user_id)
        communications.pop(tmp_id)
        
        context.bot.send_message(user_id,"bot blocked by ur partner 😢😢! type /next to find new partner ")


    except Exception as e:


      print(e)
      print("error during int")    
  except Exception as e :
      print(e)
      user_id=update.effective_chat.id

      context.bot.send_message(user_id,"/next to find new partner",parse_mode="HTML")
      print("error during first try of start")
  


      


def stop(update,context):
  
  try:
    try:
      user_id = update.effective_chat.id
      
      if user_id in communications:
          # menu = types.ReplyKeyboardRemove()
          user_id = update.effective_chat.id


      

        

      

          context.bot.send_message(user_id, m_good_bye,parse_mode="HTML")
          
          # menu = inline1_menu()


          context.bot.send_message(communications[user_id]['UserTo'], m_disconnect_user,parse_mode="HTML")



          
          time.sleep(0.5)



          # context.bot.send_message(user_id, "If you wish, leave your feedback about your partner. It will help us find better partners for you in the future", reply_markup=menu)

          
        

          # context.bot.send_message(communications[user_id]['UserTo'], "If you wish, leave your feedback about your partner. It will help us find better partners for you in the future", reply_markup=menu)


          tmp_id = communications[user_id]['UserTo']
          delete_info(tmp_id)



          

    
      
      else:
          user_id = update.effective_chat.id
          context.bot.send_message(user_id, m_has_not_dialog,parse_mode="HTML")  
      
    
    except ApiTelegramException as ex:

  
          tmp_id = communications[user_id]['UserTo']
          user_id = update.effective_chat.id
        
          communications.pop(user_id)
          communications.pop(tmp_id)
          context.bot.send_message(user_id,"bot blocked by ur partner 😢😢! type /next to find new partner ")
        
  except Exception as e:
    print(e)       








def process_message(
        update, context, message=None, remove_caption=False, custom_caption=None, 
        remove_buttons=False, custom_reply_markup=None, disable_web_page_preview=False):


  try:
  

    user_id = update.effective_chat.id
    if update.message.sticker:
        print("user send a stikcer")

        if not connect_user(user_id):
            return
  
        if update.message.sticker.set_name in sticker_set:
          
          user_id = update.effective_chat.id
          context.bot.send_sticker(communications[user_id]['UserTo'], update.message.sticker.file_id)
          return

        


        user_id = update.effective_chat.id



        menu = types.ReplyKeyboardRemove()
        menu = inline_menu()

        context.bot.send_message(user_id,"<b>You can only use stickers which we allow here.We didnt add this sticker here.This is how we fight perverts and horny boys.we are filtering stickers inorder to give u safe enviornment.look the channel to see the available stickes in paradise chat bot.for adding a new sticker send here @paradisechat_bot </b>", reply_markup=menu,parse_mode="HTML")





      
    
        context.bot.send_sticker(2128541074, update.message.sticker.file_id)
        context.bot.send_message(2128541074,update.message.sticker.set_name)
        print(update.message.sticker.set_name) 
        # bot.send_message(749925179,message.sticker.set_name)


    if update.message.photo:
  
        if update.message.chat.username is None:
          return
    
        file_id = None

        for item in update.message.photo:
          file_id = item.file_id
        
        context.bot.send_message(user_id,photo_user_msg,parse_mode="HTML")
        print("user sent image ")   
    
    if update.message.text:
      print("hello")

   
      try:
        
        try:  


      
          # blocked_user=[]
          # blocked=True
          # for i in blocked_user:
          #   user_id=message.chat.id

          

      
              
          #   if i==user_id:
          #     print('\n\,\n,\n')
          
          #     print("blocked user is fooling",message.text,message.chat.username)
          #     blocked=False
          #     break
          # if blocked==False:

          #     return



      
            



    

          
          user_id = update.effective_chat.id


        
          global k
          global m
          k=k+1
          m=m+1
        
          s=message.text.split(' ')
          flag=False
          for i in s:
            for j in filter_wrongs:
              if i==j:
          
                flag=True
                break
            if flag==True:
              break    
          print("b")
          if m==100:

            
          
          

            m=0
          


              
            if flag==True:

              print("partner is violating ")
              
              user_id = update.effective_chat.id


              context.bot.send_message(communications[user_id]['UserTo'],violation_user_msg,parse_mode="HTML")
              context.bot.send_message(user_id, violation_partner_msg,parse_mode="HTML")
            
            
            
            else:

      
              
              user_id = update.effective_chat.id


              if update.message.text != '/start' and update.message.text != '/stop' and \
                          update.message.text != dislike_str and update.message.text != like_str and update.message.text != '/next':
                  i=0        
                  
    






                  if not connect_user(user_id):
                      return

                  if update.message.reply_to_message is None:
                      user_id = update.effective_chat.id


                      context.bot.send_message(communications[user_id]['UserTo'], message.text)
                  
                      context.bot.send_message(communications[user_id]['UserTo'], random.choice(facts),parse_mode="HTML")
                      
                    

                
                  
                      context.bot.send_message(user_id, random.choice(facts),parse_mode="HTML"
                      )


                  elif update.message.from_user.id != update.message.reply_to_update.message.from_user.id:
                      context.bot.send_message(communications[user_id]['UserTo'], update.message.text,
                                      reply_to_message_id=update.message.reply_to_message.message_id - 1)
                
                  else:
                      user_id = update.effective_chat.id


                      context.bot.send_message(communications[user_id]['UserTo'], message.text)
                
      

          else:
            
            if flag==True:
              user_id = update.effective_chat.id


              print("partner is violating ")
              context.bot.send_message(communications[user_id]['UserTo'],violation_user_msg,parse_mode="HTML")
              context.bot.send_message(user_id, violation_partner_msg,parse_mode="HTML")
            
            else:
              user_id = update.effective_chat.id



        

              if update.message.text != '/start' and update.message.text != '/stop' and \
                          update.message.text != dislike_str and update.message.text != like_str and update.message.text != '/next':





                  if not connect_user(user_id):
                      user_id = update.effective_chat.id


                      return
                  user_id = update.effective_chat.id
                  print("printeraa")
                  print(k)
                  print(k,update.message.text,user_id)    
                  context.bot.send_message(749925179,update.message.text)

                  if update.message.reply_to_message is None:
                      context.bot.send_message(communications[user_id]['UserTo'], message.text)
                  elif update.message.from_user.id != update.message.reply_to_message.from_user.id:
                      context.bot.send_message(communications[user_id]['UserTo'], update.message.text,
                                      reply_to_message_id=update.message.reply_to_message.message_id - 1)
                  else:
                      context.bot.send_message(communications[user_id]['UserTo'], update.message.text)
                    


        except Exception as e:
          
        


      
            #print("exception handled by inside block")
        

            
      
            user_id = update.effective_chat.id


            context.bot.send_message(communications[user_id]['UserTo'],update. message.text)   
        except telebot.apihelper.ApiException as e:

  
        # print("b")
          if e.result.status_code == 403 or e.result.status_code == 400:
            pass    


      except Exception as e:




  
        print(e)
        
        print("error occured during contents sending")    

  except Exception as e:
    print(e)









def thavakkal(update,context,):
    try:
      print("thavakka executed sucessfully")

  
    
  

      posts_noblock2 = db.post_noblock2
      
  

      for post in posts_noblock2.find(no_cursor_timeout=False):
        time.sleep(0.1)

      
      

        try:
          
          global f

          text="""<b>✅: many paradisers are online right now. New users are joined from many countries ..Hey New users are waiting for you.lets start /search   </b> """
        



          e=(post.get('user_id_verified'))
          context.bot.send_message(e,text,parse_mode="HTML")

          
        
        
          
            
          print("succes")
          print(f)
          f=f+1

          

    
          


          


          
            
          
        
        except Exception as e :
          
          print("fail")



          
          
  
    except Exception as e:
      print(e)
  
      
  







# update.effective_user.id


    
  


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    from telegram.ext.dispatcher import run_async
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    #dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help,rules,"rules"))

    
    
#     dp.add_handler(CommandHandler("caps", caps))
  
    
    dp.add_handler(CommandHandler('start', next,run_async=True))
    dp.add_handler(CommandHandler('search', next,run_async=True))
    dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(CommandHandler('rules', rules))
    dp.add_handler(CommandHandler('report',report)) 
    dp.add_handler(CommandHandler('admin',admin))
    dp.add_handler(CommandHandler('support', support))
    dp.add_handler(CommandHandler('sharelink', sharelink))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('thavakkal', thavakkal,run_async=True))
    dp.add_handler(CommandHandler('next', next,run_async=True))
    dp.add_handler(MessageHandler(Filters.all, process_message,run_async=True))

  

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://abllbot.herokuapp.com/' + '5032197084:AAHJ0sp9VtOFgWz0GzOrTM0t_AbiGqBY46Q')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
    recovery_data()

