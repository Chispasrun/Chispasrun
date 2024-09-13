import imageio.v3 as iio

# List of filenames
filenames = ['hippocorn1.png', 'hippocorn2.png', 'hippocorn3.png', 'hippocorn4.png']
images = []

# Reading each image and appending to the images list
for filename in filenames:
    try:
        images.append(iio.imread(filename))
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please check the file path.")

# Writing the images to a GIF
iio.imwrite('team.gif', images, duration=0.5, loop=0)  # duration is in seconds per frame
