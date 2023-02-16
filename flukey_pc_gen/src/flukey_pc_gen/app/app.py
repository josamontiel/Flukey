from textual.app import App

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Welcome, Static, Button
from textual import events
from guts import *


TITLE = """
WELCOME TO FLUKEY: THE TRULY RANDOM PASS-CODE GENERATOR
Generate completely random PINs, Passwords and/or Multi-Word Passphrases.
"""


class Generate(Static):

    def compose(self) -> ComposeResult:
        """Create Buttons for selection."""
        yield Static("Which would you like to generate?\n")
        yield Button("PIN", id="pin", variant="success")
        yield Button("Password", id="password", variant="primary")
        yield Button("Passphrase", id="passphrase", variant="warning")
    
    # def on_button_pressed(self, event: Button.Pressed) -> None:
    #     self.exit(str(event.button))
    #     pass
    
class PIN(self):
    # Class for executing the PIN Function
    # ##
    pin()
    pass

class Password(self):
    # Class for executing the password function
    # ##
    password()
    pass

class Passphrase(self):
    # Class for executing the passphrase function
    # ##
    passphrase()
    pass

    
class Flukey(App):
    CSS_PATH = "styling.css"
    BINDINGS = [
        ("D", "toggle_dark", "Toggle Dark Mode"),
        ("Q", "quit_app", "Quit"),
        ("H", "how_to", "Help"),
        ]
    
    def compose(self) -> ComposeResult:
        self.widget1 = Static(TITLE)
        yield self.widget1
        self.widget1.styles.background = "darkgreen"
        self.widget1.styles.width = "100%"
        self.widget1.styles.border = ("heavy", "white")
        self.widget1.styles.margin = 2
        
        # yield Container(pin(), password(), passphrase())
        yield Header()
        yield Footer()
        yield Container(Generate())
     
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == '__main__':
    app = Flukey()
    app.run()