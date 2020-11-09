from twilio.rest import Client 

account_sid = 'AC7d72e12cab1a1dd26653cdba23e34ba5' 
auth_token = 'eacda516815150ee54927cd72a91cfcf' 
client = Client(account_sid, auth_token) 
def send_love():
      message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Ola fazendo teste de msg automatica',      
                              to='whatsapp:+5519998573508' 
                          ) 
      print(message.sid)