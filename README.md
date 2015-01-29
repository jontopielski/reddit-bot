# RedditBot
Python script that parses through specified subreddits, obtaining all top comments (replies) from submissions ending in a '?'

# End Goal
To parse all posts in a given subreddit and store all submissions that are questions (ending with a '?') in a list,
along with their top comments in another list (usually the answer to those questions) and observe the data.

# Side Goal
Parse through all the questions and store the questions based on frequency of common words, ignoring common words such as
the, and, or, etc. Show how many questions contain certain words and summarize the answer to the most frequent problems.

# Current Status
Bot successfully retrieves the questions from submissions, finds the comment with the highest score, and adds both to a list which is printed at the end.
However, everytime the bot runs, it does not remember where it left off and so repeats through the same submissions every time.  Currently working on a way for the bot to remember where it left off, or possibly skip 'n' number of submissions, where n is the number of total submissions it checked.


