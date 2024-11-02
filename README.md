# Minecraft Liquid GIF Maker
<p>
Looks for fluid texture files in the specified directory and processes all of them into animated .gif files. Uses the associated .mcmeta file for each texture file to determine the animation's speed, as well as whether the frames should be interpolated (each frame fades out instead of jumping to the next immediately) and/or reordered (as is done with the lava texture).
</p>

<h2>
Requirements
</h2>
<p>
Python 3 (https://www.python.org/downloads/)
Pillow for Python (https://pypi.org/project/pillow/)
</p>

<h2>
Usage
</h2>
<p>
```python3 liquid_gif_maker.py source_directory gif_directory gif_scale_factor```
bottom text
</p>
