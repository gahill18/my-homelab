#!/bin/python3

from textual import events
from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Footer, Header, RichLog

from game import Game
from solver import Solver, Result
import words

class MainMenu(Widget):
    wordList = words.pullWordListFromURL()
    
#        button: str = ''
#        while button != 'Q':
#            button: str = input('\n[N]ew Game\n[S]olve Random\n[Q]uit\n').upper()
#            if button == 'N':
#                # remainingGuesses, wordLength, wordPoolSize = getConfigFromUser()
#                gameState = Game.randomGameFromWordList(wordList)
#                didPlayerWin = gameState.run()
#            elif button == 'S':
#                gameState = Game.randomGameFromWordList(wordList)
#                solver: Solver = Solver(gameState)
#                attemptResult: Result = solver.solve()
#                print(attemptResult)
#            else:
#                print(f'Did not recognize option {button}')
#
#        print('Thanks for playing!')

    def render(self) -> RenderResult:
        first,last = self.wordList[0], self.wordList[-1]
        wll = len(self.wordList)

        fmtOutputText = f'Dictionary Length: {wll}\nFirst: {first}\nLast: {last}'
        
        return fmtOutputText

class NewGame(Widget):
    def render(self) -> RenderResult:
        fmtOutputText = f'TODO: NewGame Widget'
        return fmtOutputText
                


class HackingMinigameApp(App):

        BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

        def compose(self) -> ComposeResult:
                """Create child widgets for the app."""
                yield Header()
                yield RichLog()
                yield MainMenu()
                yield NewGame()
                yield Footer()

        def on_key(self, event: events.Key) -> None:
                self.query_one(RichLog).write(event)

        def action_toggle_dark(self) -> None:
                """An action to toggle dark mode."""
                self.theme = ("textual-dark" if self.theme == "textual-light" else "textual-light")

if __name__ == "__main__":
    app = HackingMinigameApp()
    app.run()
