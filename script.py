from PIL import Image

def son_imagenes_duplicadas(imagen1, imagen2):
    try:
        # Open the images with PIL
        img1 = Image.open(imagen1)
        img2 = Image.open(imagen2)

        # Check if the size of both images is the same
        if img1.size != img2.size:
            return False

        # Compare the pixels of both images
        for x in range(img1.width):
            for y in range(img1.height):
                if img1.getpixel((x, y)) != img2.getpixel((x, y)):
                    return False

        # If no differences were found, the images are duplicates
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

# Path of the images you want to compare
imagen1_path = "C:/Users/migue/OneDrive/Escritorio/OK/jaredmarciano1.jpg" # PATH 1 
imagen2_path = "C:/Users/migue/OneDrive/Escritorio/OK/jaredmarciano1.2.jpg" #PATH 2

if son_imagenes_duplicadas(imagen1_path, imagen2_path):
    print("Las imágenes son duplicadas.")
else:
    print("Las imágenes no son duplicadas.")
