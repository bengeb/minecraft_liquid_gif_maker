from PIL import Image
import re
import os
import sys


# Makes a GIF using the .png and .png.mcmeta files for the specified fluid
# in the specified directory. Saves the GIF to the other directory.
def makeGIF(directoryIn, directoryOut, fluidname, gifDelayBase, scaleFactor):
    filename = directoryIn + os.sep + fluidname + ".png"

    # Read the mcmeta file
    doInterp = False
    frametime = 1
    reorderFrames = False
    frameOrder = []
    parsingList = False
    metaFile = open(filename + ".mcmeta")
    for line in metaFile:
        tokens = line.strip().split(" ")
        tokens = [re.sub('[\W_]+', '', token) for token in tokens]
        #print(tokens)
        if (tokens[0] == "interpolate"):
            doInterp = (tokens[1][0] == "t")
        elif (tokens[0] == "frametime"):
            frametime = int(tokens[1])
        elif (tokens[0] == "frames"):
            reorderFrames = True
            parsingList = True
        elif parsingList:
            if ((len(tokens) < 1) or not tokens[0].isnumeric()):
                parsingList = False
            else:
                frameOrder.append(int(tokens[0]))
    metaFile.close()

    # Open and manipulate the image file
    imgs = []
    img = Image.open(filename)
    if (img.mode != "RGBA"): img = img.convert("RGBA")
    img = img.convert("RGB") # Remove the alpha channel
    imgSize = img.size
    for y in range(int(imgSize[1] / imgSize[0])):
        # crop format: (left, top, right, bottom)
        tempImg = img.crop((0, imgSize[0] * y, imgSize[0], imgSize[0] + (imgSize[0] * y)))
        tempImg = tempImg.resize((imgSize[0] * scaleFactor, imgSize[0] * scaleFactor), Image.Resampling.NEAREST)
        imgs.append(tempImg)

    # If necessary, reorder the frames according to the mcmeta file's specification
    if reorderFrames:
        newImgs = []
        for idx in frameOrder:
            newImgs.append(imgs[idx])
        imgs = newImgs

    # Calculate the gif's frames, interpolated if desired
    gifFrames = []
    if doInterp:
        for i in range(len(imgs)):
            nextIdx = (i + 1) % len(imgs) # the index of the frame after this one (loops back to 0 for final frame)
            for tweenFrame in range(frametime):
                gifFrames.append(Image.blend(imgs[i], imgs[nextIdx], (tweenFrame * 1.0) / frametime))
        frametime = 1
    else:
        for i in range(len(imgs)):
            gifFrames.append(imgs[i])

    # Export the gif
    gifFrames[0].save(directoryOut + os.sep + fluidname + ".gif", save_all=True, append_images=gifFrames[1:], duration = (gifDelayBase * frametime), loop=0)

    # Print a message about the gif
    message = "["
    message += "interp    | " if doInterp else "no interp | "
    message += "reorder   ] " if reorderFrames else "no reorder] "
    message += "Exported " + fluidname + ".gif"
    print(message)
    return


# The main function.
def main():
    args = sys.argv
    if len(args) != 4:
        print("Usage: python3 liquid_gif_maker.py source_directory gif_directory gif_scale_factor")
        return

    # Parameters
    directoryIn = args[1]
    directoryOut = args[2]
    scaleFactor = int(args[3]) # how much to scale the gifs up by
    gifDelayBase = 50 # in milliseconds; I think it's 50 (one tick) by default

    # Make and export GIFs for all relevant files in directoryIn
    fluidNames = []
    for file in os.listdir(directoryIn):
        if (file[-4:] == ".png") and not (file[-9:] == "_flow.png"):
            fluidNames.append(file[:-4])
    fluidNames.sort()
    for fluidName in fluidNames:
        makeGIF(directoryIn, directoryOut, fluidName, gifDelayBase, scaleFactor)
    return


if (__name__ == "__main__"):
    main()
