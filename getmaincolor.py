import Image

File = "File/images.jpg"
def get_main_color(File):
    img = Image.open(File)
    colors = img.getcolors(2560000) #need to put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")
    
    
if __name__ == '__main__':
    
    print get_main_color(File)
    # prints the tuple with(R G B) values
    