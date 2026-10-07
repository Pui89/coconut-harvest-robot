from pathlib import Path
import math, subprocess
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, FRAMES = 960, 540, 24, 144
OUT = Path("artifacts/coconut_harvest_robot_cinematic_3d_4d.mp4")
FRAMES_DIR = Path("artifacts/frames")
FRAMES_DIR.mkdir(parents=True, exist_ok=True)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font = ImageFont.truetype(font_path, 24)
small = ImageFont.truetype(font_path, 15)
for i in range(FRAMES):
    t = i/(FRAMES-1)
    im = Image.new("RGB", (W,H), (14,30,25)); d = ImageDraw.Draw(im)
    for y in range(H):
        d.line((0,y,W,y), fill=(14+int(35*y/H), 30+int(30*y/H), 25+int(18*y/H)))
    d.rectangle((0,350,W,H), fill=(34,70,34))
    # orchard silhouettes
    for x in range(-30,W,130):
        d.line((x+60,365,x+68,145), fill=(78,52,29), width=12)
        for a in range(0,360,45):
            ex=x+68+int(85*math.cos(math.radians(a))); ey=145+int(40*math.sin(math.radians(a)))
            d.line((x+68,145,ex,ey), fill=(37,108,43), width=8)
    bx, by = 245, 350
    d.rounded_rectangle((bx,by-80,bx+330,by), 24, fill=(66,75,82), outline=(195,205,210), width=4)
    d.rectangle((bx+45,by-60,bx+285,by-25), fill=(27,39,46), outline=(95,135,145), width=2)
    for wx in (bx+55,bx+275): d.ellipse((wx-38,by-8,wx+38,by+70), fill=(10,14,17), outline=(120,125,130), width=4)
    d.polygon([(bx+55,by-80),(bx+285,by-80),(bx+315,by-112),(bx+80,by-112)], fill=(25,55,78), outline=(110,160,185), width=3)
    for k in range(8): d.line((bx+90+k*25,by-110,bx+78+k*25,by-82), fill=(85,135,160), width=2)
    d.line((bx+170,by-112,bx+170,by-195), fill=(165,170,170), width=8)
    d.rounded_rectangle((bx+145,by-220,bx+195,by-190), 7, fill=(20,25,30), outline=(190,195,200), width=3)
    d.ellipse((bx+158,by-211,bx+182,by-198), fill=(70,190,215))
    shoulder=(bx+270,by-70)
    target=(690+90*math.sin(t*math.pi*2),150+38*math.cos(t*math.pi*2))
    elbow=(520+35*math.sin(t*math.pi*2),245+35*math.cos(t*math.pi*2))
    d.line((*shoulder,*elbow), fill=(215,220,220), width=24); d.ellipse((elbow[0]-18,elbow[1]-18,elbow[0]+18,elbow[1]+18), fill=(230,175,50))
    d.line((*elbow,*target), fill=(195,202,205), width=20)
    d.line((target[0]-30,target[1],target[0]+35,target[1]), fill=(225,225,225), width=7)
    for q in (-1,0,1): d.ellipse((target[0]+q*28-15,target[1]+q*8-15,target[0]+q*28+15,target[1]+q*8+15), fill=(108,65,27), outline=(190,130,55), width=2)
    d.rounded_rectangle((28,25,420,100), 16, fill=(7,16,20), outline=(70,150,140), width=2)
    d.text((48,40), "COCONUT HARVEST AI ROBOT", font=font, fill=(235,245,242))
    d.text((48,72), "CINEMATIC 3D / 4D • GEMMA 4 31B IT", font=small, fill=(105,220,195))
    d.rounded_rectangle((650,25,932,115), 16, fill=(7,16,20), outline=(70,150,140), width=2)
    d.text((670,42), "RGB-D + LiDAR  ONLINE", font=small, fill=(120,225,205))
    d.text((670,68), "ARM TRACKING  ACTIVE", font=small, fill=(235,200,100))
    d.text((670,94), "4D TARGET TIME-STATE", font=small, fill=(150,195,235))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    im.save(FRAMES_DIR/f"frame_{i:04d}.png", quality=95)
subprocess.run(["ffmpeg","-y","-framerate",str(FPS),"-i",str(FRAMES_DIR/"frame_%04d.png"),"-c:v","libx264","-pix_fmt","yuv420p","-crf","20","-preset","medium","-movflags","+faststart",str(OUT)], check=True)
print(OUT)
