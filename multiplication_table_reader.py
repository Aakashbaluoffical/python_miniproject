# 1 fives are 5
# 2 fives are 10
import pyttsx3

num = input("Enter a number:")
dic = {
    "1": "ones",
    "2": "twos",
    "3": "threes",
    "4": "fours",
    "5": "fives",
    "6": "sixes",
    "7": "sevens",
    "8": "eightes",
    "9": "nines",
    "10": 'tens'
}
mix = ""
for i in range(1, 11):
    multi = i * int(num)
    mix = str(i) + " " + dic[num] + " are " + str(multi) + "\n"
    print(mix)
    # make request to google to get synthesis


    engine = pyttsx3.init()
    engine.say("I will speak this text")
    engine.runAndWait()