from tweepy import Stream #Tweepy to use the twitter streaming api by handling authentication, connection. 
from tweepy import OAuthHandler#The Twitter streaming API is used to download twitter messages in real time. It is useful for obtaining a high volume of tweets
from tweepy.streaming import StreamListener
import time
import json

keyword=raw_input("Please Enter the keyword: ")	
#consumer key, consumer secret, access token, access secret needed to access the Twitter API.
c_key="n1FXjOdFzsAf1Qs7LaQMvG7bA"
c_secret="rnHZOJ121RkdIjj7zeU3RhcuLF6JijCtbcPfth4oKXjrVlxGpE"
a_token="307761968-yx5ZCtJyiAeNFlAt2ZEiR1Bsowxd2bsI6S4mYFxX"
a_secret="R9dlmSZZL2GCL9FTotyQRUbhRJKQzmhqTGf7Wbj1PqMBD"

class listener(StreamListener):
	counts=dict()
	start=time.time()
	start1=time.time()
	size=50
	def del_unnecessary_items(self):# FUNTION TO DELETE ITEMS WHOSE SCORE IS LESS THAN ZERO
		for word in listener.counts.keys():
			if(listener.counts[word][0] < 0):
				del listener.counts[word]
	def update_count(self):# FUNCTTION TO UPDATE SCORE OF WORDS EVERY 30 SECONDS
		for word in listener.counts.keys():
				if(time.time() - listener.counts[word][1] >= 10):	
					listener.counts[word][0] = listener.counts[word][0] - 1
					if(listener.counts[word][0] < 0):		
						del listener.counts[word]

	def print_items(self):# FUNCTION TO PRINT WORDS IN CACHE EVERY 60 SECONDS
		lst=list()
		for word in listener.counts.keys():		
			lst.append((listener.counts[word][0],word))
		lst.sort(reverse=True)
		for count,word in lst:
			if count>4:
				print count,word # PRINTS THE WORDS WITH THE HIGHEST SCORE FIRST AND SO ON
	def on_data(self, data):
		all_data = json.loads(data)
		t=time.time()
		if("text" in all_data):
			
			tweet = all_data["text"].encode('ascii','ignore')
		else:
			return True
		words=tweet.split()
		for word in words:	

			try:
			   	if(word in listener.counts):

					listener.counts[word][0] = listener.counts[word][0] + 1
					listener.counts[word][1] = time.time()
				else:							
					listener.counts[word] = [1, time.time()]	
			except:
				continue
		listener.del_unnecessary_items(self)
		if(t-listener.start >=10):#CALL TO UPDATE SCORE
			listener.update_count(self)
			listener.start=time.time()#RESET TIME
		if(t-listener.start1 >=15):#CALL TO PRINT WORDS IN CACHE
			listener.start1=time.time()#RESET TIME
			listener.print_items(self)
			print("Wait for sometime")
	def on_error(self, status):
	    print status

auth = OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_secret)
twitterStream = Stream(auth, listener()) #THIS OBJECT IS RESPONSIBLE FOR STREAMING
twitterStream.filter(track=[keyword])# STREAMING IS BASED ON A FILTER( THE KEYWORD IN THIS CASE )
