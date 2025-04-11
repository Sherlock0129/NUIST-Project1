from gpiozero import LED, Button
from time import sleep, time
from random import uniform
import sys

class ReactionGame:
    def __init__(self):
        # Hardware initialization
        self.led = LED(4)
        self.right_button = Button(15)
        self.left_button = Button(14)
        
        # Game state
        self.left_score = 0
        self.right_score = 0
        self.current_round = 1
        self.winner = None
        self.reaction_time = 0
        
        # Get player information
        self._get_player_info()
        
    def _get_player_info(self):
        """Get player names and game settings from user input"""
        print("\n" + "="*40)
        print("REACTION TIME GAME".center(40))
        print("="*40 + "\n")
        
        self.left_name = input("Enter left player name: ").strip() or "Player 1"
        self.right_name = input("Enter right player name: ").strip() or "Player 2"
        
        while True:
            try:
                self.total_rounds = int(input("Enter number of rounds to play: "))
                if self.total_rounds > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
    
    def _display_round_info(self):
        """Show current round and score information"""
        print("\n" + "-"*40)
        print(f"ROUND {self.current_round}/{self.total_rounds}".center(40))
        print("-"*40)
        print(f"{self.left_name}: {self.left_score}  |  {self.right_name}: {self.right_score}")
        print("Get ready...")
    
    def _handle_button_press(self, button):
        """Callback function for button presses"""
        if self.winner is None:  # Only register first press
            self.reaction_time = time() - self.start_time
            if button.pin.number == 14:
                self.winner = self.left_name
                self.left_score += 1
            else:
                self.winner = self.right_name
                self.right_score += 1
            
            print(f"\n{self.winner} won this round!")
            print(f"Reaction time: {self.reaction_time:.3f} seconds")
    
    def _run_round(self):
        """Execute one round of the game"""
        self._display_round_info()
        sleep(2)  # Preparation time
        
        # LED activation with random duration
        self.led.on()
        on_time = uniform(1.5, 5)  # More reasonable time range
        sleep(on_time)
        self.led.off()
        
        # Record start time and reset winner
        self.start_time = time()
        self.winner = None
        
        # Set up button handlers
        self.right_button.when_pressed = self._handle_button_press
        self.left_button.when_pressed = self._handle_button_press
        
        # Wait for player reaction (with timeout)
        timeout = 3  # seconds to wait after LED turns off
        sleep(timeout)
        
        if self.winner is None:
            print("\nNo one pressed in time!")
        
        # Clean up for next round
        self.right_button.when_pressed = None
        self.left_button.when_pressed = None
        self.current_round += 1
        sleep(1)  # Short break between rounds
    
    def _display_final_results(self):
        """Show game results and winner"""
        print("\n" + "="*40)
        print("GAME OVER".center(40))
        print("="*40)
        print("\nFINAL SCORES:")
        print(f"{self.left_name}: {self.left_score}")
        print(f"{self.right_name}: {self.right_score}")
        print("\n" + "-"*40)
        
        if self.left_score > self.right_score:
            print(f"🏆 {self.left_name} WINS! 🏆")
        elif self.right_score > self.left_score:
            print(f"🏆 {self.right_name} WINS! 🏆")
        else:
            print("🤝 IT'S A TIE! 🤝")
        print("-"*40 + "\n")
    
    def run(self):
        """Main game loop"""
        try:
            while self.current_round <= self.total_rounds:
                self._run_round()
            
            self._display_final_results()
        except KeyboardInterrupt:
            print("\nGame interrupted by user")
            sys.exit(0)
        finally:
            self.led.off()  # Ensure LED is off when game ends

if __name__ == "__main__":
    game = ReactionGame()
    game.run()
