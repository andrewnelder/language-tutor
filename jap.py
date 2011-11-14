import re
import os
import random
from termcolor import colored

HIRAGANA_TABLE = {  
      'a'  : u"\u3042", '(a)' : u"\u3041",
      'i'  : u"\u3044", '(i)' : u"\u3043",
      'u'  : u"\u3046", '(u)' : u"\u3045",
      'e'  : u"\u3048", '(e)' : u"\u3047",
      'o'  : u"\u304A", '(o)' : u"\u3049",

      'ka' : u"\u304B", 'ga' : u"\u304C",
      'ki' : u"\u304D", 'gi' : u"\u304E",
      'ku' : u"\u304F", 'gu' : u"\u3050",
      'ke' : u"\u3051", 'ge' : u"\u3052",
      'ko' : u"\u3053", 'go' : u"\u3054",

      'sa'  : u"\u3055", 'za' : u"\u3056", 'ja' : u"\u3056",
      'shi' : u"\u3057", 'zi' : u"\u3058", 'ji' : u"\u3058",
      'su'  : u"\u3059", 'zu' : u"\u305A", 'ju' : u"\u305A",
      'se'  : u"\u305B", 'ze' : u"\u305C", 'je' : u"\u305C",
      'so'  : u"\u305D", 'zo' : u"\u305E", 'jo' : u"\u305E",

      'ta'  : u"\u305F", 'da' : u"\u3060",
      'chi' : u"\u3061", 'di' : u"\u3062",
      'tsu' : u"\u3064", 'du' : u"\u3065", '(tsu)' : u"\u3063",
      'te'  : u"\u3066", 'de' : u"\u3067",
      'to'  : u"\u3068", 'do' : u"\u3069",

      'na' : u"\u306A",
      'ni' : u"\u306B",
      'nu' : u"\u306C",
      'ne' : u"\u306D",
      'no' : u"\u306E",

      'ha' : u"\u306F", 'ba' : u"\u3070", 'pa' : u"\u3071",
      'hi' : u"\u3072", 'bi' : u"\u3073", 'pi' : u"\u3074",
      'hu' : u"\u3075", 'bu' : u"\u3076", 'pu' : u"\u3077", 'fu' : u"\u3075",
      'he' : u"\u3078", 'be' : u"\u3079", 'pe' : u"\u307A",
      'ho' : u"\u307B", 'bo' : u"\u307C", 'po' : u"\u307D",

      'ma' : u"\u307E",
      'mi' : u"\u307F",
      'mu' : u"\u3080",
      'me' : u"\u3081",
      'mo' : u"\u3082",

      'ya' : u"\u3084", '(ya)' : u"\u3083",
      'yu' : u"\u3086", '(yu)' : u"\u3085",
      'yo' : u"\u3088", '(yo)' : u"\u3087",

      'ra' : u"\u3089",
      'ri' : u"\u308A",
      'ru' : u"\u308B",
      're' : u"\u308C",
      'ro' : u"\u308D",

      'wa' : u"\u308F",
      'wi' : u"\u3090",
      'we' : u"\u3091",
      'wo' : u"\u3092", 
      
      'n' : u"\u3093"
}

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

def reformat_string(input_string):
  out = []
  try:
    for word in input_string.split():
      parsed_list = re.sub(r"(a|i|u|e|o)", lambda m: m.group(0).lower()+' ', word).split()
      unicode_string = u''.join([HIRAGANA_TABLE[kana] for kana in parsed_list])
      out.append(unicode_string)
  except:
    out = None
  
  if out != None:
    out = u' '.join(out)
  
  return out

def kana_state():

  total_questions = 0
  correct         = 0
  incorrect       = 0

  while(True):
  
    __clear_screen()
  
    eng = random.choice(HIRAGANA_TABLE.keys())
    jap = reformat_string(eng)
    
    if jap == None:
      continue
    
    total_questions += 1
    
    print colored('-'*80, 'magenta')
    print colored(jap, 'cyan') + colored(' [%d/%d]'%(correct, total_questions, ), 'white')
    print colored('-'*80, 'magenta')
    print 
    
    input_text = raw_input('>> ')
    if (eng == input_text):
      correct += 1
      print 'Correct   \t[ %s ]'%(eng, )
    else:
      incorrect += 1
      print 'Incorrect \t[ %s ]'%(eng, )
  
    raw_input('')

def phrase_state():

  question_pairs = __build_question_pairs()

  total_questions = 0
  correct         = 0
  incorrect       = 0

  while(True):
  
    __clear_screen()
    key = random.choice(question_pairs.keys())
    ans = question_pairs[key]
    jap = reformat_string(ans)

    if jap == None:
      continue

    total_questions += 1
    
    print colored('-'*80, 'magenta')
    print colored('%s [%d/%d]'%(key, correct, total_questions, ), 'white')
    print colored(jap, 'cyan')
    print colored('-'*80, 'magenta')
    print
    
    input_text = raw_input('>> ')
    if (ans == input_text):
      print 'Correct   \t[ %s ]'%(ans, )
    else:
      print 'Incorrect \t[ %s ]'%(ans, )
  
    raw_input('')

if __name__ == '__main__':
  kana_state()



  











  
