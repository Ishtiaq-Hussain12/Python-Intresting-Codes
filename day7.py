import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

# -----------------------------
# Canvas
# -----------------------------
fig, ax = plt.subplots(figsize=(8,8))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

ax.set_xlim(0,100)
ax.set_ylim(0,100)
ax.set_aspect("equal")
ax.axis("off")

# -----------------------------
# Paint splash function
# -----------------------------
def splash(cx, cy, radius, color, n=900):
    theta = np.random.rand(n) * 2*np.pi
    r = radius * np.sqrt(np.random.rand(n))

    x = cx + r*np.cos(theta)
    y = cy + r*np.sin(theta)

    sizes = np.random.uniform(5,40,n)

    ax.scatter(x, y,
               s=sizes,
               c=color,
               alpha=0.9,
               linewidths=0)

# Red splash
splash(50,72,18,"red",1000)

# White splash
splash(50,60,16,"white",700)

# -----------------------------
# Pedestal
# -----------------------------
ax.add_patch(Rectangle((46,0),8,45,color="black"))

# -----------------------------
# Ninja silhouette
# -----------------------------
# Head
ax.add_patch(Circle((50,63),4,color="black"))

# Body
body = Polygon([
    (46,58),
    (54,58),
    (57,47),
    (43,47)
], closed=True,color="black")
ax.add_patch(body)

# Arms
left_arm = Polygon([
    (46,58),
    (40,55),
    (41,53),
    (47,56)
], closed=True,color="black")

right_arm = Polygon([
    (54,58),
    (60,55),
    (59,53),
    (53,56)
], closed=True,color="black")

ax.add_patch(left_arm)
ax.add_patch(right_arm)

# Legs
left_leg = Polygon([
    (47,47),
    (37,42),
    (36,39),
    (48,43)
], closed=True,color="black")

right_leg = Polygon([
    (53,47),
    (63,42),
    (64,39),
    (52,43)
], closed=True,color="black")

ax.add_patch(left_leg)
ax.add_patch(right_leg)

# Sword
ax.plot([54,60],[66,74],
        color="black",
        linewidth=4)

# -----------------------------
# Birds
# -----------------------------
def bird(x,y,s=2):
    t = np.linspace(0,np.pi,30)
    ax.plot(x+s*np.cos(t),
            y+s*0.4*np.sin(t),
            color="black",
            lw=2)

    ax.plot(x-s*np.cos(t),
            y+s*0.4*np.sin(t),
            color="black",
            lw=2)

bird(28,28,2)
bird(70,25,3)
bird(60,52,2)
bird(40,55,2)

# -----------------------------
# Extra splatters
# -----------------------------
for _ in range(120):
    x = np.random.uniform(25,75)
    y = np.random.uniform(45,90)
    c = np.random.choice(["red","white","black"])
    ax.scatter(x,y,
               s=np.random.uniform(2,25),
               c=c,
               alpha=0.8)

# -----------------------------
# Ground shadow
# -----------------------------
x = np.linspace(0,100,500)
y = 3*np.exp(-(x-50)**2/700)
ax.fill_between(x,0,y,color="black")

plt.show()