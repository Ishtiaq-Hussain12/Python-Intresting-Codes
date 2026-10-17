import math
import tkinter as tk


WIDTH = 640
HEIGHT = 560
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
HEART_SIZE = 9.2

root = tk.Tk()
root.title("A Heart for Pico")
root.resizable(False, False)
root.configure(bg="#120d18")

canvas = tk.Canvas(
	root,
	width=WIDTH,
	height=HEIGHT,
	bg="#120d18",
	highlightthickness=0,
)
canvas.pack()

heart = canvas.create_polygon(
	0,
	0,
	fill="#f04472",
	outline="#ff91aa",
	width=3,
	smooth=True,
	splinesteps=24,
)

canvas.create_text(
	CENTER_X,
	CENTER_Y + 18,
	text="Pico",
	fill="white",
	font=("DejaVu Sans", 30, "bold"),
)


def animate(frame=0):
	pulse = 1 + 0.045 * math.sin(frame * 0.12)
	points = []

	for step in range(160):
		angle = 2 * math.pi * step / 160
		x = 16 * math.sin(angle) ** 3
		y = (
			13 * math.cos(angle)
			- 5 * math.cos(2 * angle)
			- 2 * math.cos(3 * angle)
			- math.cos(4 * angle)
		)
		points.extend(
			(
				CENTER_X + x * HEART_SIZE * pulse,
				CENTER_Y - y * HEART_SIZE * pulse,
			)
		)

	canvas.coords(heart, *points)
	root.after(20, animate, frame + 1)


animate()
root.mainloop()
