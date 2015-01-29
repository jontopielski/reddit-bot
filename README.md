# RedditBot
Python script that parses through specified subreddits, obtaining all top comments (replies) from submissions ending in a '?'

# End Goal
To parse all posts in a given subreddit and store all submissions that are questions (ending with a '?') in a list,
along with their top comments in another list (usually the answer to those questions) and observe the data.

# Side Goal
Parse through all the questions and store the questions based on frequency of common words, ignoring common words such as
the, and, or, etc. Show how many questions contain certain words and summarize the answer to the most frequent problems.

# Current Status

Jan 28, 8:00pm:
Bot successfully retrieves the questions from submissions, finds the comment with the highest score, and adds both to a list which is printed at the end.
However, everytime the bot runs, it does not remember where it left off and so repeats through the same submissions every time.  Currently working on a way for the bot to remember where it left off, or possibly skip 'n' number of submissions, where n is the number of total submissions it checked.

Jan 28, 11:49pm:
Removed the retrieval limit on the bot.  It now runs at Reddit's max request limit.  However, once the bot reaches the bottom of the current page, it does not know how to turn the page, since the content grabbed is based on the url (the front page of that subreddit).  Also note that 'pages' beyond the front page are mapped to a randomly generated url, so incrementing a page count and appending it to the subreddit's url is not an option.
Also added file writing, so the results of the script are written to a .txt file and formatted.
