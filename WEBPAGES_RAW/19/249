// David Eppstein, UC Irvine, 11 Jun 1997
//
// Buttons to change the game state

import java.awt.*;
import java.util.*;
import gui.*;

class ResetButton extends GameButton {
	public ResetButton(Game g) { super(g, "New Game"); }
	public boolean active() { return (game.getBoard().previousPosition != null); }
	public void action() {
		game.resetBoard();
		Fanorona.showMessage(this, "New game started", true);
	}
	public String status() { return "Reset the board to the starting position"; }
}
