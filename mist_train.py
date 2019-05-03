__author__ = 'Renan Nominato'
__version__ = '0.0.1'


""""
This script selects randomly mistakes, and create multiple choice questions looking for the meaning.
"""


import pandas as pd
import numpy as np
import random as rn
import os
from gtts import gTTS
import time
questions = pd.read_csv("Planilha sem título - Mist.csv") #dataframe with all tested words.
#questions = questions[0:4][:]
mistakes2 = []
mistakes2 = pd.DataFrame(mistakes2)
tam = len(questions)
for i in range(0, tam):

	questions = questions.sample(frac=1).reset_index(drop=True)
	#tts = gTTS("What is the meaning of " "{}" .format(questions.loc[0,'Word']))
	#tts = gTTS ("{}".format (questions.loc[0, 'Word']))
	#tts.save('hello.mp3')
	#os.system("mpg123 hello.mp3")
	print ("\n"*10)
	print('What is the correct option ' '{} ?'.format(questions.loc[0,'Word']))
	print (questions.loc[0,'Desc'])
	resp = str(input('Write your answer as the correct word:'))
	print('')

	if questions.loc[0,'Tran'] == resp:
		print('You are right! {} is the correct option'.format(questions.loc[0,'Tran']))
	else:
		print('You are wrong. This question will be back on the mistakes list')
		mistakes2 = mistakes2.append(questions.loc[0][:])
	time.sleep(3)
	questions = questions.drop (questions.index[0])

mistakes2.to_csv("mistakes2.csv")
	#clear = lambda: os.system('clear')