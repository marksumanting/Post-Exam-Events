print("Title of program: Post Exam Bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find something fun to do")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append("Sleep")
      counter += 1
    if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append("Me too! I'm so happy for you! Have fun!")
      counter += 1
   if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("There will always be a next time, do not lose hope!")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
