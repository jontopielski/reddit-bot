import praw
import time

r = praw.Reddit(user_agent = "fashion_info_finder bot v1.0 by /u/fashion_info_finder")
running = True
retrieve_limit = 5
counter = 0
questions = []
answers = []

mfa_url = 'http://www.reddit.com/r/malefashionadvice'
content = r.get_content(mfa_url, limit = retrieve_limit)
subreddit = r.get_subreddit("malefashionadvice")

# login preload
r.login("fashion_info_finder", "topielski")
print('Logging in...')

# primary function
while (True):
	for submission in content:
		if '?' in submission.title and submission.id not in questions:
			print('Question:')
			print(submission.title)
			questions.append(submission.id)
			
			comments = subreddit.get_comments(limit=retrieve_limit)
			for comment in comments:
				comment_text = comment.body.lower()
				print('Answer:')
				print(comment_text)
			print
	
	time.sleep(5)
	print('Reached end...')

