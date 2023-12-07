# voting_functions.py
import tkinter as tk
from tkinter import messagebox
from typing import Tuple

class VotingAppFunctions:
    """
    Class for handling voting-related functions.
    """
    def __init__(self):
        """
        Initialize the VotingAppFunctions.
        """
        self.can_votes = [0, 0, 0, 0]

    def validate_name(self, name: str) -> bool:
        """
        Validate the entered name.

        Parameters:
            name (str): The entered name.

        Returns:
            bool: True if the name is valid, False otherwise.
        """
        if any(char.isdigit() for char in name):
            messagebox.showwarning("Invalid Name", "Name cannot contain numeric characters.")
            return False
        return True

    def vote(self, candidate: int, name_entry: tk.Entry) -> None:
        """
        Register a vote for the specified candidate and display a message.

        Parameters:
            candidate (int): The candidate for whom the vote is registered.
            name_entry (tk.Entry): The Entry widget for the voter's name.
        """
        try:
            voter_name = name_entry.get()

            if not self.validate_name(voter_name):
                return

            if not voter_name:
                messagebox.showwarning("Missing Name", "Please enter your name before voting.")
                return

            self.can_votes[candidate - 1] += 1

            # Display a message indicating for whom the user voted
            candidate_names = ['John', 'Jane', 'Jack', 'Jill']
            messagebox.showinfo("Vote", f"{voter_name} voted for {candidate_names[candidate - 1]}")

            # Clear the content of the name entry
            name_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def get_candidate_votes(self) -> Tuple[int, int, int, int]:
        """
        Get the total votes for each candidate.

        Returns:
            Tuple[int, int, int, int]: Votes for each candidate.
        """
        return tuple(self.can_votes)
