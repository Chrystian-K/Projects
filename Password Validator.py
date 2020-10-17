print('''
"This is a basic password validator, follow the rules below and check if your password is strong.
      Password should:
      - be between 5 and 10 signs
      - should contain minimum one number
      - should contain minimum one special sign(#,@ etc)
      - no space is allowed
      ''')

while True:
      x = str(input("Check Your Password: "))

      n1 = str(1)
      n2 = str(2)
      n3 = str(3)
      n4 = str(4)
      n5 = str(5)
      n6 = str(6)
      n7 = str(7)
      n8 = str(8)
      n9 = str(9)
      n0 = str(0)

      s1 = str("!")
      s2 = str("@")
      s3 = str("#")
      s4 = str("$")
      s5 = str("%")
      s6 = str("^")
      s7 = str("&")
      s8 = str("*")
      s9 = str(",")
      s10 = str(".")
      s11 = str("?")



      if len(x) > 5 and len(x) <= 10:
            if x.__contains__(n1) or x.__contains__(n2) or x.__contains__(n3) or x.__contains__(n4) or x.__contains__(n5) or x.__contains__(n6) or x.__contains__(n7)\
              or x.__contains__(n8) or x.__contains__(n9) or x.__contains__(n0):
                  if x.__contains__(s1) or x.__contains__(s2) or x.__contains__(s3) or x.__contains__(s4) or x.__contains__(s5)\
                    or x.__contains__(s6) or x.__contains__(s7) or x.__contains__(s8) or x.__contains__(s9) or x.__contains__(s10) or x.__contains__(s11):
                        if not x.__contains__(" "):
                              print("Good Password")
                        else:
                              print("Wrong Password, try again")
                  else:
                        print("Wrong Password, try again")
            else:
                   print("Wrong Password, try again")
      else:
            print("Wrong Password, try again")

