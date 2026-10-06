#!/usr/bin/env python3
"""Generate a 3D coconut-harvesting robot scene and an animated MP4 demo.

Outputs:
  sim/assets/coconut_harvester_3d.glb
  sim/assets/coconut_harvester_demo.mp4

This is a visualization/simulation asset. For physics-backed execution, load the
existing robots/coconut_harvester.urdf into Isaac Sim or Gazebo/ROS 2.
"""
from pathlib import Path
import numpy as np
import trimesh
import imageio.v2 as imageio
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"sim"/"assets"
OUT.mkdir(parents=True,exist_ok=True)

scene=trimesh.Scene()
def box(name, ext, loc, color):
    m=trimesh.creation.box(extents=ext); m.apply_translation(loc)
    m.visual.face_colors=np.array(color,dtype=np.uint8); scene.add_geometry(m,node_name=name)
def cyl(name,r,h,loc,color):
    m=trimesh.creation.cylinder(radius=r,height=h,sections=32); m.apply_translation(loc)
    m.visual.face_colors=np.array(color,dtype=np.uint8); scene.add_geometry(m,node_name=name)
def sphere(name,r,loc,color):
    m=trimesh.creation.icosphere(subdivisions=2,radius=r); m.apply_translation(loc)
    m.visual.face_colors=np.array(color,dtype=np.uint8); scene.add_geometry(m,node_name=name)

box("base",(2.2,1.45,.42),(0,0,.45),(55,65,72,255))
for x in (-.78,.78):
    for y in (-.78,.78): cyl("wheel",.32,.20,(x,y,.35),(35,35,35,255))
box("mast",(.35,.35,2.3),(0,0,1.8),(100,110,120,255))
joints=[np.array([0,0,2.75]),np.array([.35,0,3.55]),np.array([.85,.05,4.05]),np.array([1.25,.12,4.18]),np.array([1.55,.12,4.10])]
for i,(a,b) in enumerate(zip(joints[:-1],joints[1:])):
    mid=(a+b)/2; L=np.linalg.norm(b-a); box(f"arm_link_{i}",(.18,.18,L),mid,(190,200,210,255))
for i,p in enumerate(joints): sphere(f"joint_{i}",.13,p,(45,150,170,255))
box("tool",(.42,.24,.18),(1.72,.12,4.08),(220,150,40,255))
cyl("trunk",.28,5,(3,0,2.5),(110,70,40,255))
for k in range(14):
    a=2*np.pi*k/14; sphere(f"leaf_{k}",.65,(3+.9*np.cos(a),.8*np.sin(a),5.2+.35*np.sin(2*a)),(55,130,55,255))
for k,p in enumerate([(3.4,.2,4.9),(2.75,-.3,5.15),(3,.35,5.55),(3.55,-.35,5.35)]):
    sphere(f"coconut_{k}",.18,p,(105,70,35,255))
scene.export(OUT/"coconut_harvester_3d.glb")

frames=[]
for f in range(120):
    t=f/119
    fig=plt.figure(figsize=(9.6,5.44),dpi=100)
    ax=fig.add_subplot(111,projection="3d")
    ax.set_xlim(-2,4.8); ax.set_ylim(-2,2.2); ax.set_zlim(0,6.2)
    ax.set_box_aspect((6.8,4.2,6.2)); ax.view_init(elev=22,azim=-58+12*np.sin(t*2*np.pi))
    ax.set_axis_off(); ax.set_facecolor("#eaf3e7")
    X,Y=np.meshgrid(np.linspace(-2,5,8),np.linspace(-2,2,6))
    ax.plot_surface(X,Y,np.zeros_like(X),alpha=.25,color="#8bbf75",linewidth=0)
    ax.bar3d(-1.1,-.72,.25,2.2,1.44,.4,color="#38434a",shade=True)
    for x in (-.78,.78):
        for y in (-.78,.78): ax.scatter([x],[y],[.25],s=700,c="#222222",marker="o")
    ax.plot([0,0],[0,0],[.65,2.7],lw=8,c="#9aa6ad")
    phase=t*4; reach=.35+.65*(.5+.5*np.sin(phase*2*np.pi-np.pi/2))
    a1=-.35+.65*reach; a2=.35-.55*reach
    pts=[np.array([0,0,2.7]),np.array([.35+.25*np.sin(a1),0,3.35+.25*np.cos(a1)]),
         np.array([.95+.35*np.cos(a2),.05,3.8+.35*np.sin(a2)]),
         np.array([1.45+.35*reach,.1,4.05]),np.array([1.72+.25*reach,.12,4.0])]
    for p in pts: ax.scatter(*p,s=90,c="#2e9bb0")
    for a,b in zip(pts[:-1],pts[1:]): ax.plot([a[0],b[0]],[a[1],b[1]],[a[2],b[2]],lw=8,c="#c5d0d6")
    target=np.array([3+.45*np.sin(phase),.25,5.05]); ax.scatter(*target,s=160,c="#6b4526")
    ax.plot([pts[-1][0],target[0]],[pts[-1][1],target[1]],[pts[-1][2],target[2]],lw=2,c="#e39b2e",alpha=.55)
    ax.plot([3,3],[0,0],[0,5],lw=18,c="#754b2a")
    for a in np.linspace(0,2*np.pi,12,endpoint=False):
        ax.scatter(3+np.cos(a),.7*np.sin(a),5.2+.35*np.sin(2*a),s=800,c="#4f9b45",alpha=.75)
    ax.text2D(.03,.93,"COCONUT HARVESTER • AUTONOMOUS 3D DEMO",transform=ax.transAxes,fontsize=13,weight="bold")
    ax.text2D(.03,.88,"Drive → scan → approach → cut → verify → retract",transform=ax.transAxes,fontsize=10)
    fig.canvas.draw(); frames.append(np.asarray(fig.canvas.buffer_rgba())[:,:,:3].copy()); plt.close(fig)
imageio.mimsave(OUT/"coconut_harvester_demo.mp4",frames,fps=24,codec="libx264",quality=7)
print("Generated",OUT/"coconut_harvester_3d.glb",OUT/"coconut_harvester_demo.mp4")
