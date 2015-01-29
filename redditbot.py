import praw
import time

# reddit wrapper usage and defined user_agent
r = praw.Reddit(user_agent = "fashion_info_finder bot v1.0 by /u/fashion_info_finder")

# holds the questions and answers in a list
questions_id_cache = []
questions = []
answers = []
iterations = 0

# max iterations before script terminates
max_iterations = 5

# delay slot limited by reddit's max requests
delay_slot = 2

# url, content extracted from url, and desired subreddit
subreddit_name = "seduction"
url = 'http://www.reddit.com/r/'
url += subreddit_name
content = r.get_content(url)
subreddit = r.get_subreddit(subreddit_name)

# login preload
r.login("fashion_info_finder", "topielski")
print('Logging in...')

# primary function
while (True):

	# loop through all submissions
	for submission in content:

		# if it is a question, store the title and score
		if '?' in submission.title and submission.id not in questions_id_cache:
			print '\nQuestion: ', submission.title
			print 'Score: ', submission.score
			questions_id_cache.append(submission.id)
			questions.append(submission.title)

			# grab the comments from that submission
			comments = submission.comments
			top_score = 0
			top_comment = ''

			# loop through every comment, finding the top score
			# checking praw.helpers.flatten_tree(comments) also checks replies
			for comment in comments:
				comment_text = comment.body.lower()
				comment_score = comment.score
				# find the top scoring comment
				if (comment_score > top_score):
					top_comment = comment_text
					top_score = comment.score

			# append the top comment to the answers list
			answers.append(top_comment)
			iterations += 1

			# print the status
			print '\n================================='
			print 'Sleeping for 2 seconds...'
			print 'Total iterations: ', iterations
			print '================================='

			# delay slot needed to limit requests
			time.sleep(delay_slot)

			# when met, stop the script and create the file
			if (iterations == max_iterations):
				break

	# reached if max_iterations is met or no more content
	break



# store everything into a file
file = open('qa.txt', 'w')

# header to the file
file.write('=================================' + '\n')
file.write('Q&A for ' + subreddit_name + '\n')
file.write('=================================' + '\n\n')

# loop through all the elements of the lists
for counter in range(0, len(questions)):
	the_count = str(counter+1)
	file.write('Question ' + the_count + ': ' + questions[counter].encode('utf-8') + '\n\n')
	file.write('Answer ' + the_count + ': ' + answers[counter].encode('utf-8') + '\n')
	file.write('\n=================================\n\n')
