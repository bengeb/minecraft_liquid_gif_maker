![Water GIF](gifs/water_still.gif)
# Minecraft Liquid GIF Maker
![Lava GIF](gifs/lava_still.gif)

<p>
Looks for fluid texture files in the specified directory and processes all of them into animated .gif files. Uses the associated .png.mcmeta file for each texture file to determine the animation's speed, as well as whether the frames should be interpolated (each frame fades out instead of jumping to the next immediately) and/or reordered (as is done with the lava texture).
</p>

<h2>Requirements</h2>
<p>Python 3 (https://www.python.org/downloads/)</p>
<p>Pillow for Python (https://pypi.org/project/pillow/)</p>

<h2>Usage</h2>
<p>```python3 liquid_gif_maker.py source_directory gif_directory gif_scale_factor```</p>
<p>```source_directory``` is the directory which contains the .png and .png.mcmeta texture files</p>
<p>```gif_directory``` is the directory where you want the GIFs to be exported to</p>
<p>```gif_scale_factor``` is how much you want the GIFs to be scaled by. Whole integers are recommended. Use 1 if you want the GIFs to be their original size.</p>
