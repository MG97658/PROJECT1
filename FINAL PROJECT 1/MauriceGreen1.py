def candidate_menu() -> int:
    """
    Displays the candidate menu and returns the user's choice (1, 2, 3, or 4).

    Returns:
        int: The user's choice representing the selected candidate (1, 2, 3, or 4).
    """
    while True:
        try:
            print('----------------------\nCANDIDATE MENU\n----------------------')
            print('1 - John')
            print('2 - Jane')
            print('3 - Jack')
            print('4 - Jill')
            choice = int(input('Candidate: '))
            if 1 <= choice <= 4:
                return choice
            else:
                print('Invalid choice. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter a valid integer (1, 2, 3, or 4).')

def main() -> int:
    """
    Main function to run the voting program.

    Returns:
        int: Always returns 0.
    """
    chosen = vote_menu()
    Can1: int = 0
    Can2: int = 0
    Can3: int = 0
    Can4: int = 0

    while chosen != 'x':
        user_vote = candidate_menu()
        if user_vote == 1:
            print('Voted John')
            Can1 += 1
        elif user_vote == 2:
            print('Voted Jane')
            Can2 += 1
        elif user_vote == 3:
            print('Voted Jack')
            Can3 += 1
        elif user_vote == 4:
            print('Voted Jill')
            Can4 += 1

        chosen = vote_menu()

    total_votes = Can1 + Can2 + Can3 + Can4
    print(f'-------------------------\n John - {Can1}, Jane - {Can2}, Jack - {Can3}, Jill - {Can4}, Total - {total_votes}\n-------------------------')
    return 0

def vote_menu() -> str:
    """
    Displays the vote menu and returns the user's option ('v' for vote, 'x' for exit).

    Returns:
        str: The user's option ('v' for vote, 'x' for exit).
    """
    while True:
        try:
            print('---------\nVOTE MENU\n---------')
            print('v: VOTE\nx: Exit')
            option = input('Option: ').strip().lower()
            if option in ('v', 'x'):
                return option
            else:
                print('Invalid option. Please enter either "v" for vote or "x" for exit.')
        except Exception:
            print('An unexpected error occurred.')

if __name__ == '__main__':
    main()
