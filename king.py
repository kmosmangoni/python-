
#------------this for loop can solve many ways-------------------

#1

country = ["bangladesh","india","nepal","bhutan","srilanka","pakisthan"]
friend= ["habib","ira","shezan","mehedi","sazid","omer"]

for index,x in enumerate(country):
  print(country[index][0].lower(),friend[index][-1].lower())
  if(country[index][0].lower() == friend[index][0].lower() and country[index][-1].lower() == friend[index][-1].lower()):
    print("I am not")
  else:
    print("I am the king")

   
   #2
   # country = ["bangladesh","india","nepal","bhutan","srilanka","pakisthan"]
#friend= ["habib","ira","shezan","mehedi","sazid","omer"]

#for x in country:
    #for y in friend:
        #if x [0] == y [-1]:
            #print(y, "The king of",x)


#3
   # country = ["bangladesh","india","nepal","bhutan","srilanka","pakisthan"]
#friend= ["habib","ira","shezan","mehedi","sazid","omer"]

#for x in country:
  #for y in friend:
    #if x[0] == y[-1]:
      #print(f"{x} is king")
      #print("looser")