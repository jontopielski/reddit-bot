import praw
import time

r = praw.Reddit(user_agent = "fashion_info_finder bot v1.0 by /u/fashion_info_finder")
running = True
retrieve_limit = 25
counter = 0
questions = []
answers = []

# primary function
def bot_run():
	mfa_url = 'http://www.reddit.com/r/malefashionadvice'
	content = r.get_content(mfa_url, limit = retrieve_limit)

	for submission in content:
		if '?' in submission.title and submission.id not in questions:
			print(submission.title)
			questions.append(submission.id)
			'''
			comments = submission.get_comments
			top_comment = comments.get_top(comments)
			print(top_comment)
			print('\n')
			'''

# login preload
r.login("fashion_info_finder", "topielski")
print('Logging in...')

# 'main' function
while (running):
	bot_run()
	time.sleep(5)
	counter += 1
	print('Bot run ', counter, 'times...')
	print('Terminating after 5 executions...')

	if (counter == 5):
		running = False