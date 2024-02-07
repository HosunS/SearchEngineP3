// David Eppstein, UC Irvine, 11 Jun 1997
//
// Buttons to change the game state

import java.awt.*;
import java.util.*;
import gui.*;

class PassButton extends GameButton {
	public PassButton(Game g) { super(g, "Pass"); }
	public boolean active() { return game.humanToMove() && game.getBoard().midCapture(); }
	public void action() { game.setBoard(new Board(game.getBoard(), 0L)); }
	public String status() { return "Stop eating pieces and finish your turn"; }
}
