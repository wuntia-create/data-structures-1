def computer_guesses_number():
    print("🧠 Think of a number between 1 and 100.")
    print("I'll try to guess it. After each guess, respond with:")
    print("  'h' → too high\n  'l' → too low\n  'c' → correct")

    low = 1
    high = 100
    attempts = 0

    def too_high(state):
        state["high"] = state["guess"] - 1

    def too_low(state):
        state["low"] = state["guess"] + 1

    def correct(state):
        print(f"🎯 Got it in {state['attempts']} attempts!")
        print(f"💭 Final guess: {state['guess']}")
        state["done"] = True

    actions = {
        'h': too_high,
        'l': too_low,
        'c': correct
    }

    game_state = {"low": low, "high": high, "attempts": attempts, "done": False, "guess": None}

    while not game_state["done"] and game_state["low"] <= game_state["high"]:
        game_state["guess"] = (game_state["low"] + game_state["high"]) // 2
        print(f"🤔 My guess: {game_state['guess']}")
        response = input("Your feedback (h/l/c): ").lower()
        game_state["attempts"] += 1

        actions.get(response, lambda state: print("❗ Invalid input. Try h, l, or c."))(game_state)

computer_guesses_number()
