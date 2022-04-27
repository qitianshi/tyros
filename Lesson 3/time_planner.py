school_tomorrow = input("Do I have school tomorrow? (Yes/No) ")
completed_homework = input("Have I completed my homework? (Yes/No) ")
friends_online = input("Do I have friends online (Yes/No) ")

if (completed_homework == "Yes" or friends_online == "No") and school_tomorrow == "No":
	print("Sleep early")
if school_tomorrow == "Yes":
	print("Homework")
if friends_online == "Yes" and school_tomorrow == "No":
	print("Play some games")