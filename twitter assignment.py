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
	words_stamp=list()
	n=1
	size=500
	def update_count(self):# FUNCTTION TO UPDATE SCORE OF WORDS EVERY 30 SECONDS
		for word_stamp in self.words_stamp:
			if(time.time()-word_stamp[1]>60): # IF WORD NOT SEEN FOR 60 SECONDS REDUCE SCORE BY 1 
				try:
					self.counts[word_stamp[0]]=self.counts[word_stamp[0]]-1
				except:
					continue
		listener.delete_items(self,self.counts)# CALL TO DELETE WORDS FROM CACHE IF SCORE IS LESS THAN ZERO





	def check_word(self,word):# FUNCTION TO CHECK IF WORD ALREADY EXISTS IN CACHE,IF IT DOES IT RETURNS THE LOCATION OF THE WORD 
		k=0
		for word_stamp in self.words_stamp:
			
			if word==word_stamp[0]:
				if (k==0):
					self.words_stamp[0][1]=time.time()
				else:
					return k
			else:
				return 0 
			k=k+1
	def delete_items(self,a_dict):# FUNCTION TO DELETE WORD FROM CACHE IF SCORE FALLS BELOW ZERO
		#del_word=list()
		for k,v in a_dict.items():
			if v<0:
				try:

					del a_dict[k]
				except:
					continue
				for word_stamp in self.words_stamp:
					if word_stamp[0]==k:
						self.words_stamp.remove(word_stamp)

	def print_items(self):# FUNCTION TO PRINT WORDS IN CACHE EVERY 60 SECONDS
		lst=list()
		for word,count in self.counts.items():
			lst.append((count,word))
		lst.sort(reverse=True)
		for count,word in lst:
			if count>1:
				print count,word # PRINTS THE WORDS WITH THE HIGHEST SCORE FIRST AND SO ON
	def on_data(self, data):
		all_data = json.loads(data)
		t=time.time()
		if("text" in all_data):
			
			tweet = all_data["text"]
		else:
			return True
		words=tweet.split()
		
		if(listener.n==1):
			for word in words:
				listener.words_stamp.append([word,time.time()])
			listener.n=2
		if(listener.n==3):
			for word in words:
				num=listener.check_word(self,word)
				if num:
					listener.words_stamp[num][1]=time.time()
				else:
					listener.words_stamp.append([word,time.time()])
		listener.n=3
		for word in words:
			if (len(listener.counts)==listener.size):
				for key,val in listener.counts.items():
					if val==0:
						del listener.counts[key]
						for word_stamp in words_stamp:
							if word_stamp[0]==key:
								words_stamp.remove(word_stamp)
				if (len(listener.counts)==listener.size):
					break

			try:
				listener.counts[word] = listener.counts.get(word,0) + 1# UPDATES SCORE +1 EVERY TIME IT SEES A WORD
			except:
				continue
		if(t-listener.start >=30):#CALL TO UPDATE SCORE
			listener.update_count(self)
			listener.start=time.time()#RESET TIME
		if(t-listener.start1 >=60):#CALL TO PRINT WORDS IN CACHE
			listener.start1=time.time()#RESET TIME
			listener.print_items(self)
			print("Wait for sometime")
	def on_error(self, status):
	    print status

auth = OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_secret)
twitterStream = Stream(auth, listener()) #THIS OBJECT IS RESPONSIBLE FOR STREAMING
twitterStream.filter(track=[keyword])# STREAMING IS BASED ON A FILTER( THE KEYWORD IN THIS CASE )
