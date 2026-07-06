name = input("What's your name? ").strip().title() # Ask user for their name

#name = name.strip().title() # Remove whitespaces from str and title

#name = name.title() # Capitilize
first , last = name.split(" ") #split user name into first name and last name 

#print("hello, ", name , " Welcome! ", end="", sep="   ") # Say hello to user  end="\n" separator=" "
#print(name)

#print("hello , \"Ayesha\"")

print(f"hello, {first}")