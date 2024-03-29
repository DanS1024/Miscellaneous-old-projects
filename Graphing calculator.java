
import java.awt.*;
import javax.swing.*;

public class Graph extends JPanel {
	
	private static final long serialVersionUID = 1L;
	
	public void graph(Graphics graph, double left, double right) {
		
		double left_ = left;
		double right_ = right;
		
		//draw(graph, left, right, left_, right_);
		
	}
	
	public void draw(Graphics graph, double left, double right, double left_, double right_, int a) {
		
		int x = (int) (500 + 50 * left);
		int y = (int) (500 - 50 * right);
		int x_ = (int) (500 + 50 * left_);
		int y_ = (int) (500 - 50 * right_);
		
		if (a == 0) {
			graph.drawLine(x, y, x_, y_);
		} else {
			graph.drawRect(x, y, 1, 1);
		}
		
		
	}
	
	public void paintComponent(Graphics graph) {
		
		// Setup =========================================================
		super.paintComponent(graph);
		this.setBackground(Color.WHITE);
		
		graph.setColor(Color.LIGHT_GRAY);
		for (int i = 0; i < 20; i++) {
			
			graph.drawLine(0, i * 50, 1000, i * 50);
			graph.drawLine(i * 50, 0, i * 50, 1000);
			
			graph.drawString(Integer.toString(i - 10), i * 50 + 5, 515);
			graph.drawString(Integer.toString(i - 10), 505, 995 - i * 50);
			
		}
		// Setup =========================================================
		
		double x = -10;
		double y = 10;
		
		double x_ = 0;
		double y_ = 0;
		
		double left = 0;
		double right = 0;
		double left_ = 0;
		double right_ = 0;
		
		double left1 = 0;
		double right1 = 0;
		double left2 = 0;
		double right2 = 0;
		double left3 = 0;
		double right3 = 0;
		double left4 = 0;
		double right4 = 0;
		double left5 = 0;
		double right5 = 0;
		
		
		double y1 = 0;
		double y1_ = 0;
		
		double y2 = 0;
		double y2_ = 0;
		double waves = 0;
		double waves_ = 0;
		
		double err = 0.05;
		float c = 0;
		
		double t = 0;
		
		graph.setColor(Color.BLUE);
		for (double hor = -500; hor < 500; hor++) {
			
			for (double ver = -500; ver < 500; ver++) {
				
				graph.setColor(new Color(c, 0, 1 - c));
				
				x = hor / 50;
				y = ver / 50;
				
				if (hor < -499) {
					x_ = left;
					y_ = right;
				}
				
				left3 = 0;
				right3 = 0;
				
				try {
					
					left = (x + 7.5)*(x + 7.5) + (y - 7.5)*(y - 7.5);
					right = 4;
					
					left1 = (3*(x - 4)*(x - 4)) + (y - 7)*(y - 7);
					right1 = 5 + 2*(x - 4)*(y - 7);
					
					left2 = x*x*x;
					right2 = 1 + x*y*y;
					
					left3 = y;
					for (double n = 0; n <= 10; n++) {
						right3 += (1/(2*n+1))*Math.sin((2*n+1)*x);
					}
					
					left4 = (x - 6)*(x - 6)/3 + (y + 6)*(y + 6);
					right4 = 4;
					
					left5 = -6 + 2*Math.cos(t)+Math.cos(2*t);
					right5 = -6 + 2*Math.sin(t)-Math.sin(2*t);
					
				} catch (Exception e) {
					e.printStackTrace();
				}
				
				
				// Function
				if (left-right < err && left-right > -err && hor > -499) {
					draw(graph, x, y, x, y, 1);
					// draw(graph, x, y, x_, y_, 0);
					// x_ = x;
					// y_ = y;
				}
				
				if (left1-right1 < err && left1-right1 > -err && hor > -499) {
					draw(graph, x, y, x, y, 1);
				}
				if (left2-right2 < err && left2-right2 > -err && hor > -499) {
					draw(graph, x, y, x, y, 1);
				}
				if (left3-right3 < err && left3-right3 > -err && hor > -499) {
					draw(graph, x, y, x, y, 1);
				}
				if (left4-right4 < err && left4-right4 > -err && hor > -499) {
					draw(graph, x, y, x, y, 1);
				}
				
				// Parametric
				draw(graph,left5,right5,left5,right5,1);
				
			}
			
			t += 2*Math.PI / 1000;
			
			c = (float) ((hor + 500) / 1000);
			
			// Nothing special below this comment :)
			
			/*
			graph.setColor(new Color(c, 0, 1 - c));
			
			// remove for area
			left_ = left;
			right_ = right;
			
			y1_ = y1;
			
			y2_ = y2;
			waves_ = waves;
			
			try {
				// Insert function here
				left = y;
				right = x*x;
				
				y1 = Math.pow(2, x);
				
				y2 = Math.sin(x) * Math.abs(x);
				waves = Math.pow(Math.E, Math.sin(x));
				
			} catch (Exception e) {
				e.printStackTrace();
			}
			
			if (i > -499) {
				
				draw(graph, left, right, left_, right_);
				
				//draw(graph, i, y1, y1_);
				
				// draw(graph, i, waves, waves_);
				//draw(graph, i, y2, y2_);
				
			}
			
			c = (float) ((i + 500) / 1000);
			
			x = i / 50;
			y = x;
			*/
		}
		
	}
	
	// Setup ================================================
	public static void main(String[] args) {
		
		JFrame frame = new JFrame();
		frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Graph graph = new Graph();
		frame.add(graph);
		frame.setSize(1000, 1000);
		frame.setResizable(false);
		frame.setVisible(true);
		
	}
	// Setup ================================================
	
}
