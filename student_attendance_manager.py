import random

def play_hangman():
    # List of words for the game as required by minimum specifications
    word_list = ['python', 'programming', 'computer', 'science', 'university']
    
    # As per the assignment note: "for testing the secret word is fixed to 'python'"
    secret_word = 'python'
    
    # Trackers for game state
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    # Main game loop runs while wrong attempts are within the allowed limit
    while wrong_guesses < max_wrong_guesses:
        # Construct the progress string based on successfully guessed letters
        progress = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        
        # Display current word progress before asking for the next set of inputs
        if wrong_guesses < max_wrong_guesses:
            print(f"Progress: {progress}")
        
        # Check if the player has uncovered all letters (Win Condition)
        if progress == secret_word:
            print(f"You won! The word was {secret_word}.")
            print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
            return

        # Prompt for user input exactly as shown in the document
        user_input = input("Guesses: ").strip().lower()

        # Handle comma-separated bulk inputs (like Test Case 4: p, z, y, x, t, h, o, n)
        inputs_list = [i.strip() for i in user_input.split(',') if i.strip() != '']
        
        # If the user presses enter without writing anything, skip this iteration
        if not inputs_list:
            continue

        # Process each character provided in the current input line
        for current_guess in inputs_list:
            
            # Test Case 3: Validate input length and make sure it is a letter
            if len(current_guess) != 1 or not current_guess.isalpha():
                print("Invalid input. Enter a single letter.")
                continue

            # Test Case 3: Check if the letter was already processed in a prior turn
            if current_guess in guessed_letters:
                print(f"You already guessed '{current_guess}' Try another letter (no attempt lost)")
                continue

            # Save the valid, unique letter to our set
            guessed_letters.add(current_guess)

            # Check if the letter exists inside the hidden target word
            if current_guess in secret_word:
                # Print output statement inline using space separation to match Test Case 4
                print(f"{current_guess}: Correct", end=" ")
            else:
                wrong_guesses += 1
                print(f"{current_guess}: Wrong ({wrong_guesses}/{max_wrong_guesses})", end=" ")
                
                # Test Case 2: Check if maximum wrong attempts reached (Lose Condition)
                if wrong_guesses == max_wrong_guesses:
                    print()  # Move cursor to a new line
                    print(f"Wrong guess ({wrong_guesses}/{max_wrong_guesses})")
                    print(f"Game Over! The word was {secret_word}.")
                    return
        
        # Insert a newline separator after finishing the execution of the input list
        print()

if __name__ == "__main__":
    play_hangman()