# Minecraft Liquid GIF Maker
<h1>Works on vanilla and modded fluids!</h1>

![Water GIF](gifs/water_still.gif)
![Lava GIF](gifs/lava_still.gif)
![Resonant Ender GIF](gifs/thermal_116/ender_still.gif)
![Energized Glowstone GIF](gifs/thermal_116/glowstone_still.gif)
![Molten Manyullyn GIF](gifs/tinkers_1710/liquid_manyullyn.gif)

<p>Looks for fluid texture files in the specified directory and processes all of them into animated .gif files. Uses the associated .png.mcmeta file for each texture file to determine the animation's speed, as well as whether the frames should be interpolated (each frame fades out instead of jumping to the next immediately) and/or reordered (as is done with the lava texture).</p>

<p>Note that this currently only works for still fluid textures, not flowing ones.</p>

<h2>Requirements</h2>
<p>Python 3 (https://www.python.org/downloads/)</p>
<p>Pillow for Python (https://pypi.org/project/pillow/)</p>

<h2>Usage</h2>

```python3 liquid_gif_maker.py source_directory gif_directory gif_scale_factor```

<p></p>

```source_directory```

<p>The directory which contains the .png and .png.mcmeta texture files.</p>

```gif_directory```

<p>The directory where you want the GIFs to be exported to.</p>

```gif_scale_factor```

<p>How much you want the GIFs to be scaled by. Whole integers are recommended. Use 1 if you want the GIFs to be their original size.</p>
