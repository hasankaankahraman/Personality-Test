
Name = str (input ('Enter Your Name: '))
Surname = str (input ('Enter Your Surname: '))
Age = str (input ('Enter Your Age: '))
Gender = str (input ('Enter Your Gender: (M or W): '))
question1 = str (input ('Do you usually eat out with your friends? (Answer as "YES" or "NO"): '))
question2 = str (input ('Can you quickly do Gamified Attention Tests?  (Answer as "YES" or "NO"): ')) 
question3 = str (input ('Do you keep your calm even under pressure?  (Answer as "YES" or "NO"): ')) 
question4 = str (input ('Do you arrive on time for a job interview? (Answer as "YES" or "NO"): ')) 
if question1 == 'YES':
  number = 1
elif question1 == 'NO':
    number = 9
else:
    print ("Invalid Status")
if question2 == 'YES':
  number = number
elif question2 == 'NO':
    number = number + 4
else:
    print ("Invalid Status")
if question3 == 'YES':
  number = number
elif question3 == 'NO':
    number = number + 2
else:
    print ("Invalid Status")
if question4 == 'YES':
  number = number
elif question4 == 'NO':
  number = number + 1
else:
  print ("Invalid Status")

if number == 1: 
  info = 'Extravert / Sensing / Thinking / Judging';
elif number == 2:
   info = 'Introvert / Sensing / Thinking / Judging';
elif number ==3: 
   info = 'Extravert / Sensing / Feeling / Judging';
elif number == 4: 
  info = 'Introvert / Sensing / Feeling / Judging';
elif 5: 
  info = 'Extravert / Sensing / Thinking / Perceiving';
elif number == 6: 
  info = 'Introvert / Sensing / Thinking / Perceiving';
elif number == 7: 
  info = 'Extravert / Sensing / Feeling / Perceiving';
elif number == 8: 
  info = 'Introvert / Sensing / Feeling / Perceiving';
elif number == 9: 
  info = 'Extravert / iNtuition / Thinking / Judging';
elif number == 10: 
  info = 'Introvert / iNtuition / Thinking / Judging';
elif number == 11: 
  info = 'Extravert / iNtuition / Feeling / Judging';
elif number == 12: 
  info = 'Introvert / iNtuition / Feeling / Judging';
elif number == 13: 
  info = 'Extravert / iNtuition / Thinking / Perceiving';
elif number == 14: 
  info = 'Introvert / iNtuition / Thinking / Perceiving';
elif number == 15: 
  info = 'Extravert / iNtuition / Feeling / Perceiving';
elif number == 16: 
  info = 'Introvert / iNtuition / Feeling / Perceiving';    

print(number,": ", info)
  
rate = str (input ('Rate the Questionnaire, Ranging From 1 to 10: '))
num = str(number)
out = Name +" " + Surname + " " + Age + " " + Gender + " " + num + " " + rate 

with open("output.txt","w",encoding="utf-8") as file:
  file.write(out)

'''192010010065
   192010010064
   192010010049'''
