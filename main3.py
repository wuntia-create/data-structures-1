def computer_guesses_number():
    print("🤖 Let's play! Think of a number between 1 and 100.")
    print("I'll try to guess it. After each guess, tell me:")
    print("'h' if my guess is too high, 'l' if it's too low, or 'c' if it's correct.")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        print(f"My guess is: {guess}")
        feedback = input("Is it too High (h), too Low (l), or Correct (c)? ").lower()
        attempts += 1

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 Yay! I guessed your number in {attempts} attempts.")
            break
        else:
            print("⚠️ Please enter 'h', 'l', or 'c'.")

computer_guesses_number()
