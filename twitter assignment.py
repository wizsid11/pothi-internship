from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import pprint

keyword=raw_input("Please Enter the keyword: ")	
#consumer key, consumer secret, access token, access secret.
ckey="n1FXjOdFzsAf1Qs7LaQMvG7bA"
csecret="rnHZOJ121RkdIjj7zeU3RhcuLF6JijCtbcPfth4oKXjrVlxGpE"
atoken="307761968-yx5ZCtJyiAeNFlAt2ZEiR1Bsowxd2bsI6S4mYFxX"
asecret="R9dlmSZZL2GCL9FTotyQRUbhRJKQzmhqTGf7Wbj1PqMBD"

class listener(StreamListener):
	counts=dict()
	start=time.time()
	start1=time.time()
	words_stamp=list()
	n=1


	#def counter(self,a_list):
	#	for word in a_list:
	#		self.counts[word] = self.counts.get(word,0) + 1
	#	self.start=time.time()
	#	return((self.counts,self.start))
	def update_count(self,tim):
		for word_stamp in self.words_stamp:
			if(tim-word_stamp[1]>60):
				self.counts[word_stamp[0]]=self.counts[word_stamp[0]]-1
		listener.delete_items(self,self.counts)



	def check_word(self,word,time):
		k=0
		for word_stamp in self.words_stamp:
			
			if word==word_stamp[0]:
				if (k==0):
					self.words_stamp[0][1]=time
				else:
					return k
			else:
				return 0 
			k=k+1
	def delete_items(self,a_dict):
		for k,v in a_dict.items():
			if v<0:
				del a_dict[k]
	def print_items(self,a_dict):
		lst=list()
		for word,count in a_dict.items():
			lst.append((count,word))
		lst.sort(reverse=True)
		for count,word in lst:
			print count,word
	def on_data(self, data):
		all_data = json.loads(data)
		t=time.time()
		tweet = all_data["text"]
		words=tweet.split()
		
		if(listener.n==1):
			for word in words:
				listener.words_stamp.append([word,t])
				#print listener.words_stamp
			listener.n=2
		if(listener.n==3):
			for word in words:

	
				num=listener.check_word(self,word,t)
				if num:
					listener.words_stamp[num][1]=t
				else:
					listener.words_stamp.append([word,t])
		listener.n=3
		for word in words:
			listener.counts[word] = listener.counts.get(word,0) + 1
		#print listener.counts
		if(t-listener.start >= 30):
			tim=time.time()
			listener.update_count(self,tim)
			listener.start=time.time()
		if(t-listener.start1 >= 15):
			listener.start1=time.time()
			
			listener.print_items(self,listener.counts)
			#print listener.words_stamp
			print("Wait for sometime")
	def on_error(self, status):
	    print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[keyword])
