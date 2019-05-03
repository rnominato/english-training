__author__ = 'Renan Nominato'
__version__ = '0.0.1'


""""
This script selects randomly words, and create multiple choice questions looking for the meaning.
"""


import pandas as pd
import numpy as np
import random as rn
import os
from gtts import gTTS
import time
questions = pd.read_csv("Planilha sem título - Vocab.csv") #dataframe with all tested words.
#questions = questions[0:5][:]
mistakes = []
mistakes = pd.DataFrame(mistakes)
for i in range(0, len(questions)):

	questions = questions.sample(frac=1).reset_index(drop=True)
	#tts = gTTS("What is the meaning of " "{}" .format(questions.loc[0,'Word']))
	#tts = gTTS ("{}".format (questions.loc[0, 'Word']))
	#tts.save('hello.mp3')
	#os.system("mpg123 hello.mp3")
	print ("\n"*10)
	print('What is the meaning of ' '{} ?'.format(questions.loc[0,'Word']))
	questions2 = questions[0:5][:]
	questions2 = questions2.sample(frac=1).reset_index(drop=True)
	if len(questions)> 0:
		print('0)' '{}'.format(questions2.loc[0,'Desc']))
	if len (questions) > 1:
		print('1)' '{}'.format(questions2.loc[1,'Desc']))
	if len (questions) > 2:
		print('2)' '{}'.format(questions2.loc[2,'Desc']))
	if len (questions) > 3:
		print('3)' '{}'.format(questions2.loc[3,'Desc']))
	if len (questions) > 4:
		print('4)' '{}'.format(questions2.loc[4,'Desc']))
	print('')

	resp = int(input('Write your answer as the number in the choice:'))
	print('')

	if questions2.loc[resp,'Desc'] == questions.loc[0,'Desc']:
		print('You are right! ' '{}: {} - {}'.format(questions.loc[0,'Word'], questions.loc[0,'Desc'], questions.loc[0,'Tran']))
	else:
		print('You are wrong. This word will be back on the mistakes list')
		mistakes = mistakes.append(questions.loc[0][:])
	time.sleep(3)
	questions = questions.drop (questions.index[0])

#mistakes.to_csv("mistakes.csv")
	#clear = lambda: os.system('clear')