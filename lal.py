import os
import time
import random
import jap

# Configuration
LANGUAGE_SELECTION = {1: 'Japanese', 2: 'French'}

# Scoring
NUMBER_OF_CORRECT   = 0
NUMBER_OF_INCORRECT = 0
NUMBER_OF_QUESTIONS = 0

def __clear_screen():
  if os.name == "posix":               # Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"): # DOS/Windows
    os.system('CLS')

def __build_question_pairs(language='Japanese', reversed=False):
  # Builds the question pairs in memory so they may be posed to the individual later

  file = open('./voc/%s.txt'%(language,), 'rb')

  question_pairs = dict()
  for line in file.readlines():
    if '|' in line:
      line_list = line.strip().split('|')
      if reversed:
        question_pairs[line_list[1]] = line_list[0]
      else:
        question_pairs[line_list[0]] = line_list[1]
  return question_pairs

def __pose_language_to_learn():
  # Determines the language the individual is attempting to learn
  
  language_identified = False

  while (not language_identified):
    __clear_screen()
    language = None
    in_int = raw_input('What language would you like to learn?\n\t[1] Japanese\n\t[2] Russian\n\n--> ')
    try:
      language = LANGUAGE_SELECTION[int(in_int)]
      if language is not None:
        language_identified = True
    except:
      continue

  return language

def __pose_reversals(language):
  
  reversal_identified = False
  
  while (not reversal_identified):
    __clear_screen()
    reverse = None
    in_int = raw_input('How would you like to learn?\n\t[1] Respond w/ English\n\t[2] Respond w/ %s'%(language,))
    try:
      reverse = True if int(in_int) == 1 else False
      if reverse is not None:
        reversal_identified = True
    except:
      continue

  return reverse

def __pose_random_question(language, question_pairs):
  # Poses a random question to the user and expects an output
  
#  NUMBER_OF_QUESTIONS += 1
  
  __clear_screen()
  
  key = random.choice(question_pairs.keys())
  ans = question_pairs[key]
  
  user_answer = raw_input('Please enter the %s equivalent to the english phrase.\n\t[ %s ]\n\n>> '%(language, key, ))
  if user_answer == ans:
#    NUMBER_OF_CORRECT += 1
    
    print 
    print '-'*80
    print 'CORRECT'
#    print 'SCORE: (%d/%d)'%(NUMBER_OF_CORRECT, NUMBER_OF_INCORRECT, )
    print '-'*80
    time.sleep(1)
    
  else:
  
    print
    print '-'*80
    print 'INCORRECT'
#    print 'SCORE: (%d/%d)'%(NUMBER_OF_CORRECT, NUMBER_OF_INCORRECT, )
    print 'The correct answer is:\n\t[ %s ]\n\t[ %s ]'%(
      ans, jap.reformat_string(ans), )
    print 'Please type the answer three times.'
    print '-'*80
    print     
    
    number_of_times_typed = 0
    while (number_of_times_typed < 3):
      try_again_text = raw_input('(%d) >> '%(number_of_times_typed+1, ))
      if try_again_text.strip() == ans:
        number_of_times_typed += 1

if __name__ == '__main__':
  language       = __pose_language_to_learn()
  reverse        = __pose_reversals(language)
  question_pairs = __build_question_pairs(language, reverse)
  print question_pairs
  while(True):
    __pose_random_question(language, question_pairs)
