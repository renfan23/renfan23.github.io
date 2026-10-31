from PIL import Image, ImageDraw


W, H = 1800, 960
image = Image.new("RGB", (W, H), "#172c29")
draw = ImageDraw.Draw(image)

# Quiet negative space on the left keeps the title legible over the artwork.
draw.rectangle((0, 0, W, 650), fill="#172c29")
draw.rectangle((0, 650, W, H), fill="#203a35")
draw.rectangle((920, 90, W, 652), fill="#1b3430")

for x in range(920, W, 150):
    draw.line((x, 90, x, 650), fill="#24413b", width=2)
for y in range(120, 651, 120):
    draw.line((920, y, W, y), fill="#24413b", width=2)

# Wall panels and a task surface establish a recognizable lab setting.
draw.rectangle((1030, 170, 1710, 504), fill="#213b36", outline="#35534b", width=4)
draw.rectangle((1070, 206, 1320, 434), fill="#142724", outline="#38574e", width=3)
draw.rectangle((1360, 206, 1670, 434), fill="#1b302d", outline="#38574e", width=3)
draw.line((70, 760, 1730, 760), fill="#34534b", width=3)
for x in range(120, 1780, 160):
    draw.line((x, 790, x - 38, 960), fill="#29463f", width=2)
draw.ellipse((930, 696, 1660, 850), fill="#142724")

# Small environment details suggest depth without competing with the robot.
draw.rectangle((1490, 390, 1662, 525), fill="#a95b41", outline="#d5855d", width=4)
draw.polygon(((1490, 390), (1542, 354), (1710, 354), (1662, 390)), fill="#c77753")
draw.line((1542, 354, 1542, 488), fill="#e0956d", width=3)
draw.line((1614, 365, 1614, 508), fill="#824431", width=3)

# Mobile base, wheels, lift column and a six-link articulated arm.
draw.ellipse((1072, 722, 1210, 842), fill="#111f1d", outline="#53655f", width=5)
draw.ellipse((1320, 722, 1458, 842), fill="#111f1d", outline="#53655f", width=5)
draw.ellipse((1105, 750, 1177, 814), fill="#62746c")
draw.ellipse((1353, 750, 1425, 814), fill="#62746c")
draw.rounded_rectangle((1048, 634, 1490, 773), radius=28, fill="#c5d0c7", outline="#74877e", width=6)
draw.rectangle((1094, 654, 1440, 682), fill="#e1e6dd")
draw.rounded_rectangle((1124, 694, 1396, 739), radius=10, fill="#70847b")
draw.rounded_rectangle((1211, 514, 1328, 650), radius=18, fill="#488c7b", outline="#9bc3ae", width=5)
draw.rectangle((1230, 545, 1309, 618), fill="#2e675c")

arm_segments = [((1268, 520), (1152, 408)), ((1152, 408), (1280, 299)), ((1280, 299), (1450, 356)), ((1450, 356), (1547, 257))]
for start, end in arm_segments:
    draw.line((start, end), fill="#6d8179", width=68)
    draw.line((start, end), fill="#d1dbd1", width=45)

for cx, cy, radius, core in [
    (1268, 520, 42, "#b6c6b9"),
    (1152, 408, 39, "#d9e1d7"),
    (1280, 299, 37, "#b9cabe"),
    (1450, 356, 34, "#d8dfd6"),
    (1547, 257, 29, "#b7c8bd"),
]:
    draw.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), fill="#40574f", outline="#142724", width=6)
    draw.ellipse((cx-radius+11, cy-radius+11, cx+radius-11, cy+radius-11), fill=core)
    draw.ellipse((cx-8, cy-8, cx+8, cy+8), fill="#426e63")

# Compact wrist and open gripper point toward the workpiece.
draw.line((1547, 257, 1613, 293), fill="#74877e", width=30)
draw.line((1547, 257, 1613, 293), fill="#d4ddd4", width=19)
draw.rounded_rectangle((1598, 275, 1667, 311), radius=11, fill="#91a69a", outline="#273e37", width=4)
draw.line((1656, 285, 1701, 256), fill="#d4ddd4", width=13)
draw.line((1656, 301, 1706, 329), fill="#d4ddd4", width=13)
draw.ellipse((1691, 244, 1713, 266), fill="#d4ddd4")
draw.ellipse((1696, 319, 1718, 341), fill="#d4ddd4")

# Sensor head and restrained indicator lights.
draw.rounded_rectangle((1200, 466, 1329, 507), radius=12, fill="#233b35", outline="#10211e", width=5)
draw.rectangle((1221, 477, 1256, 495), fill="#d45f48")
draw.rectangle((1270, 477, 1307, 495), fill="#94c5bb")
draw.ellipse((1058, 647, 1088, 677), fill="#d95b43")
draw.ellipse((1450, 647, 1480, 677), fill="#77b6a2")

# A few depth points hint at perception data, kept away from the copy area.
for cx, cy, radius, color in [
    (930, 266, 5, "#77b8a9"), (980, 310, 4, "#d7795e"), (1010, 215, 4, "#a5c9bb"),
    (1420, 175, 4, "#77b8a9"), (1580, 150, 5, "#d7795e"), (1710, 205, 4, "#a5c9bb"),
    (990, 510, 4, "#d7795e"), (1540, 570, 5, "#77b8a9"), (1700, 612, 4, "#a5c9bb"),
]:
    draw.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), fill=color)

image.save("assets/robot-platform.png", optimize=True)
