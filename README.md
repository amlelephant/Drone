# Modular Drone Project

This project has been in development for quite some time and is still a work in progress. Since most of the software tuning is handled through **Mission Planner**, this repository focuses primarily on the **hardware and physical design** aspects of the build.

> ⚙️ *Note:* This repo was created after much of the project was already complete, so the version history isn’t perfectly linear. The files with the **highest version numbers** represent the most up-to-date designs.

## Overview

The biggest challenge in creating a custom drone lies in **parameter tuning**. Because each build varies in frame size, weight distribution, and components, parameter files are **not portable** between systems. For that reason, I haven’t included my personal parameter file here—it wouldn’t be useful for anyone replicating this project.

My current build consists of:
- **Flight Controller:** SpeedyBee F405 V4  
- **Companion Computer:** Raspberry Pi Zero  
- **Motors:** Generic Amazon brushless motors  
- **Additional Components:** Detailed in the included hand-drawn schematics  

STEP files are provided for **dimension checking and CAD modeling** in Onshape.

## Contents

- `/Drone` – contains test code for potential applications  
- `/Schematics` – hand-drawn diagrams of circuit connections and layout  
- `/CAD` – STEP files and mechanical designs for 3D visualization  

---

This project represents my ongoing effort to design a modular drone platform—built from scratch, parameter-tuned by hand, and continually improved through iteration and testing.
