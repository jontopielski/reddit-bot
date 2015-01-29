import praw
import time

# reddit wrapper usage and defined user_agent
r = praw.Reddit(user_agent = "fashion_info_finder bot v1.0 by /u/fashion_info_finder")
# make 5 requests per call
retrieve_limit = 25
# holds the questions and answers in a list
questions_id_cache = []
questions = []
answers = []

# for running once and exiting
running = True

# url, content extracted from url, and desired subreddit
mfa_url = 'http://www.reddit.com/r/malefashionadvice'
content = r.get_content(mfa_url, limit = retrieve_limit)
subreddit = r.get_subreddit("malefashionadvice")

# login preload
r.login("fashion_info_finder", "topielski")
print('Logging in...')

# primary function
while (running):

	# loop through all submissions
	for submission in content:

		# if it is a question, store the title and score
		if '?' in submission.title and submission.id not in questions_id_cache:
			print '\nQuestion: ', submission.title
			print '\nScore: ', submission.score
			questions_id_cache.append(submission.id)
			questions.append(submission.title)

			# grab the comments from that submission
			comments = submission.comments
			top_score = 0
			top_comment = ''

			# loop through every comment, finding the top score
			for comment in comments:
				comment_text = comment.body.lower()
				comment_score = comment.score
				if (comment_score > top_score):
					top_comment = comment_text
					top_score = comment.score
					
			answers.append(top_comment)

			print '\n================================='

	running = False

	for counter in range(0, len(questions)):
		print 'Question ', counter+1, ': ', questions[counter], '\n'
		print 'Answer ', counter+1, ': ', answers[counter], '\n'
		print '\n================================='
