def vowel(text):
    vowles="aeiouAIEOU"
    print(len([letter for letter in text if letter in vowles]))
    print([letter for letter in text if letter in vowles])
    print(len([letter for letter in text if letter not in vowles]))
    print([letter for letter in text if letter not in vowles])  
vowel('WelcomeToYou')
