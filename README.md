# VtextureSwap

A VTubeStudio(VTS) plugin for live2d model texture swapping by hotkeys

## User Guide

### Install Libraries (Requirement)<br/>
reuqires websocket for VTS connection
For people who's not familiar with python:<br/>
Run install_libraries.bat<br/>

### Configure Your Live2d model<br/>
Copy textureSwap.exp3.json to your model floder/motion e.g.
textureSwap.exp3.json needs to be placed in the motions folder of the model directory.
Bind textureSwap.exp3.json to an hotkey event in VTS (here the set hotkey is the hotkey for texture swapping later),
and set it to "close after 0.1 seconds"<br/>

In the hotkey event list, there must be one hotkey event named after "ReloadModelTexture" (case sensitive),
with the trigger event set to "reload model texture".
It is not necessary to bind any hotkey to this event.<br/>

Please ensure there are original texture and texture to swap with.
For default, they are named after texture_00.png and texture_00_swap.png.
It can be renamed in VtextureSwap.py<br/>

### Configure the Python script<br/>
Current version needs you open VtextureSwap.py with editor and fill the absolute direatory for the texture floder 
(unsually named model_name.texture_resulution, e.g, my_model.4096)
Please see the annotation in VtextureSwap.py for further instruction.

For people who's not familiar with code:
You can edit .py files by renaming it's surfix to .txt and open it with txt editor.
Rename it back to .py after edition is done.<br/>

### Ready to Go?<br/>
After launching VTS, run launch.bat (python VtextureSwap.py)
VTS will ask for permission to establish connection, please allow.<br/>

### Contact
Email: sawaumi@foxmail.com 
Discord: Shamil_Saw#1756
Twitter: @Juzi_Saw

#### Huge thanks to emlo40's frame work: https://github.com/mlo40/VsPyYt
