UCB W205 Exercise 2

Step 1. Environment and Tool Setup

First create EC2 instance using the AMI provided; makesure hadoop is running
and postgres has started and running; python should be running with psycopg
installed.

Step 2. Setup github and make sure it is the correct repository

a:  git clone the correct repo

$ git clone https://github.com/goldenmonster0602/w205_exercise_2.git

b: now we need to create the database tcount and the table tweetwordcount
first.   under extweetwordcount/src/bolts/ ,  run creatdatabase.py till you
see the database and table have been created.

$ ./creatdatabase.py

c: now we can run the sparse command.  under extweetwordcount/, start
streaming twitter word count:

S sparse run

d: press anytime Ctrl+C to stop streaming.


Step 3: checking on final results and histogram range

a: you can check either all the word count or single word count by running
finalresults.py in the main w205_exercise_2 folder.

$ ./finalresults.py 

or specific word:

$ ./finalresults.py hello

By intering two integers k1 and K2, histogram.py returns all the words with a total number of
occurrences greater than or equal to k1, and less than or equal to k2.

$ ./histogram.py 3 10


Step 4: checking top 20 words in twitter stream.

You can check the top 20 word in the twitter account by using postgres:

$ psql -U postgres
postgres=# \\c tcount
tcount=# SELECT * FROM tweetwordcount ORDER BY count DESC LIMIT 20;



