print('''
"This is a basic password validator, follow the rules below and check if your password is strong.
      Password should:
      - be between 5 and 10 signs
      - should contain minimum one number
      - should contain minimum one special sign(#,@ etc)
      - no space is allowed
      ''')

numbers = str((1,2,3,4,5,6,7,8,9,0))

special_characters = str(("!","@","#","$","%","^","&","?",",",".","*"))

while True:

      x = str(input("Check Your Password: "))

      if len(x) > 5 and len(x) <= 10:
            if x.__contains__(" "):
                  print("Space is not allowed!")
                  break
            for i in numbers and special_characters:
                  if x.__contains__(i):
                        print("Correct Password!")
            else:
                  print("Requirments not met :( , please try again")
      else:
            print("Requirments not met :( , please try again")

