im = Image.open(img_path)
rotated_img  = im.rotate(180)
img = ImageTk.PhotoImage(rotated_img)