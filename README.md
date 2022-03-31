# VTS-texture-swap

A VTubeStudio(VTS) plugin for live2d model texture swapping by hotkeys


### Frame work from: emlo40's VsPyYt
VsPyYt:https://github.com/mlo40/VsPyYt
Huge thanks to emlo40 :D

## User Guide

Now packaged as .exe for version >= v0.2.*alpha, no library installation required.

### Configure Your Live2d model<br/>
~~Copy textureSwap.exp3.json to your model floder/motion e.g.
textureSwap.exp3.json needs to be placed in the motions folder of the model directory.~~

VtextureSwap will check if all needed exp3 files are in place and generate the missing ones.

**Bind textureSwap.exp3.json to an hotkey event in VTS** (here the key bind is the key bind for texture swapping later),
and **leave the setting as default** 
(no "Fade for sec.", "Stop after sec." off, "Stop when key is let go" off).
The naming or key bind is free of your choice.

![textureSwap_hotkey_screenshot](https://user-images.githubusercontent.com/72533095/159108150-6822ace5-06c1-4cf7-8088-d39436edff9f.png)

For any future key trigger function, the set up should be the same.

**Create a hotkey event named as "ReloadModelTexture"**(case sensitive, VtextureSwap will use this request VTS to reload model texture),
**with the trigger event set to "reload model texture".**
It is not necessary to bind any hotkey to this event.

![ReloadModelTexture_event_screenshot](https://user-images.githubusercontent.com/72533095/159108305-6eebd18b-7b7d-48eb-be16-d6f3e370633f.png)

Please ensure your texture png to swap with is placed in the same folder.
For default, the swap texture(s) should be named as texture_00_swap.png (For multiple texture files, please name them as texture_01_swap.png, texture_02_swap.png, etc., as the live2D default texture names would be texture_00, texture_01...)
Also, please leave the original texture(s) as their default name.

![texture_naming_example](https://user-images.githubusercontent.com/72533095/159108509-e32c8934-166b-4775-91b1-4692d08acd37.png)

### Ready to Go?<br/>
After launching VTS, run VtextureSwap.exe
VTS will ask for permission to establish connection, please allow.


### Configure the Python script<br/>
If you want to modify the python script further, I left more info in the annotations among scripts, hopefully those will help. You can also conntact me via the following:

### Contact Me
Email: sawaumi@foxmail.com 
Discord: Shamil_Saw#1756
Twitter: @Juzi_Saw
