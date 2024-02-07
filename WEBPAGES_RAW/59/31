// David Eppstein, UC Irvine, 11 Jun 1997
//
// Component for containing an image, including automatic tracking

import java.awt.*;

class ImageUnavailable extends RuntimeException { }

public class ImageComponent extends Canvas 
{
	Image image;
	boolean tracked = false;

	void trackImage(Image i) {
		if (tracked) return;
		MediaTracker tracker = new MediaTracker(this);
		tracker.addImage(i,0);
		try {
			tracker.waitForID(0);
		} catch (InterruptedException e) {
			throw new ImageUnavailable();
		}
	}

	public ImageComponent(Image i) { image = i; }
	public void paint(Graphics g) {
		trackImage(image);
		g.drawImage(image, 0, 0, this);
	}
	public Dimension minimumSize() {
		trackImage(image);
		return new Dimension(image.getWidth(this), image.getHeight(this));
	}
	public Dimension preferredSize() { return minimumSize(); }
}
