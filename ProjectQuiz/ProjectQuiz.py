#Initial List of Questions for this project:

questions = ("Who is considered as 'Father of the Computer'?",
             "What animal is visible on the Firefox Web Browser logo?",
             "Who was invented the World Wide Web (www)?",
             "Google is the largest Search Engine in the World! What is the Second largest Search Engine in the World?",
             "Who is known as the creator of the 'Python' programming language?",
             "Cadabra.com was the original name of which famous tech company?",
             "Who is the current CEO of 'Apple Inc.'?",
             "Which tech company has a policy of all employees spending Two Days in every Two Years at the Customer Service Desk, even the Board of Directors and the CEO?",
             "It is common knowledge that Google is a misspell of 'Googol', which is a mathematical quantity. But, what was the proposed name of Google before this was settled on?",
             "Who is the current CEO of 'Microsoft Corporation'?")

#Initial List of Options for the above questions:

options = (("A. Ada Lovelace", "B. Herman Hollerith", "C. Alan Turing", "D. Charles Babbage"),
           ("A. Fox", "B. Squirrel", "C. Polar Bear", "D. Red Panda"),
           ("A. Michael Spindler", "B. Tim Berners-Lee", "C. Linus Torvalds", "D. Charles Babbage"),
           ("A. Yahoo", "B. Mozilla Firefox", "C. Facebook", "D. YouTube"),
           ("A. Larry Page", "B. Guido van Rossum", "C. James Gosling", "D. Dennis Ritchie"),
           ("A. yahoo.com", "B. aol.com", "C. Amazon.com", "D. Google.com"),
           ("A. Steve Jobs", "B. Gil Amelio", "C. Michael Spindler", "D. Tim Cook"),
           ("A. Uber", "B. Meta", "C. Amazon", "D. IBM"),
           ("A. Scrub", "B. Quora", "C. Hertz", "D. Backrub"),
           ("A. Paul Allen", "B. Bill Gates", "C. Satya Nadella", "D. Steve Ballmer"))

#Initial List of answers for the above questions:

answers = (("D. Charles Babbage","D", "d"),
           ("D. Red Panda", "D", "d"),
           ("B. Tim Berners-Lee", "B", "b"),
           ("D. YouTube","D", "d"),
           ("B. Guido van Rossum", "B", "b"),
           ("C. Amazon.com", "C", "c"),
           ("D. Tim Cook","D", "d"),
           ("C. Amazon", "C", "c"),
           ("D. Backrub","D", "d"),
           ("C. Satya Nadella", "C", "c"))


correct = 0
question_num = 0

#creating a for loop:

for ques in questions:
    print("--------------------------------------------")
    print(ques)

    print(options[question_num])
    print("Your Answer is:")
    ans = input()
    
    
    if(ans in answers[question_num]):
        correct +=1
        print("Great, Your Answer is Correct")
    else:
        print("Sorry, Your Answer is Incorrect")
        print(f"{answers[question_num][0]} is the correct answer")
    
    question_num +=1 

 
print("--------------------------------------------")
    
correct = int(correct / len(questions) * 100)
print(f"Your score is: {correct}%")

