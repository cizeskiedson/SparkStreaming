import socket
import tweepy


HOST = 'localhost'
PORT = 9009

s = socket.socket()
s.bind((HOST, PORT))
print('Aguardando conexão da porta: %d' % PORT)

s.listen(5)
conn, address = s.accept()

print(f'Recebendo solicitação de {address}')

token = ''
keyword = 'machine learning'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        conn.send(tweet.text.enconde('utf-8', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()
    
conn.close()