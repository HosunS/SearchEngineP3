// David Eppstein, UC Irvine, 11 Jun 1997
//
// Collection of lines of text *WITHOUT SCROLLBAR*

import java.awt.*;
import gui.*;

public class TextPanel extends FlatPanel {
	public TextPanel(Color background, Color foreground) {
		super();
		setBackground(background);
		setForeground(foreground);
		setLayout(new StackLayout(StackLayout.VERTICAL, 0));
	}
	public void addLine(String s) {
		Label lab = new ThinLabel(s);
		lab.setBackground(getBackground());
		lab.setForeground(getForeground());
		add("Left", lab);
	}
}
