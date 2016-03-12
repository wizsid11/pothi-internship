# pothi-internship
The Twitter streaming API is used to download twitter messages in real time. It is useful for obtaining a high volume of tweets.
With the help of the tweepy library it gets easy to handle authentication, connection. 

The on_data method of Tweepy’s StreamListener is modified. It inherits from the StreamListener class.

STEPS TO FOLLOW ONCE YOU RUN THE PYTHON FILE:
	1.FIRST ENTER A KEYWORD AND PRESS ENTER.
	2.WAIT FOR 60 SECONDS FOR THE FIRST PRINT OF WORDS ALONG WITH THEIR SCORE.
	3.AFTER THE FIRST PRINT WAIT AGAIN FOR THE SECOND PRINT(AGAIN ANOTHER 60 SECONDS).
	4.THE PROGRAM KEEPS RUNNING ANDS KEEPS PRINTING THE WORDS IN THE CACHE EVERY 60 SECONDS UTIL YOU FORCIBILIY STOP IT.

HOW IT WORKS:
	1.THE STREAM OF DATA RECEIVED IS IN JSON FORMAT.
	2.JSON IS A FILE WHICH IS BASICALLY A COLLECTION OF LISTS AND DICTIONARIES.
	3.WE COLLECT THE TEXT FROM THE JSON DATA THAT WE RECEIVE.
	4.A LIST OF WORDS IN THE TWEET IS CREATED AT FIRST.
	5.DICTIONARY IS THEN CREATED WHERE THE KEY ARE THE WORDS AND VALUES IS THE SCORE.
	6.ANOTHER LIST IS CREATED.THE ELEMENTS OF THIS LIST ARE ALSO LISTS.THE SUBLIST CONTAINS THE WORD AND THE TIMESTAMP OF THE WORD.
	7.THE IDEA IS TO UPDATE THE TIME TIMESTAMP WHEN THE WORD IS SEEN AGAIN IF NOT SEE THE SCORE REDUCES BY 1. 
	8.WHICH CAN BE EASILY HANDLED AS EACH WORD HAS A TIMESTAMP.THIS IS TAKEN CARE OF WHEN SCORE IS UPDATED AFTER 30 SECONDS.
	9.FINALLY WE PRINT ALL THE WORDS IN THE CACHE(SCORE > 1) EVERY 60 SECONDS.

CERTAIN THINGS THAT I HAVEN'T INCULDED:
	1.THERE IS NO RESTRICTION ON THE SIZE OF THE DICTIONARY.

YOU CAN CHANGE THE TIME FOR PRINTING TO SOMETHING LIKE 15 SECONDS FOR FASTER OUTPUT.

I HAVE ALSO INCLUDED COMMENTS EVEN IN THE PYTHON FILE.

YOU CAN CONTACT ME THROUGH MY EMAIL-ID: msid@iitk.ac.in IN CASE OF ANY ISSUES
