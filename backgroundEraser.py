from rembg import remove

input_file = "sincap.jpg"
output_file = "sincap.png"

with open(input_file, "rb") as i:
    with open(output_file, "wb") as o:
        input_path = i.read()
        output_path = remove(input_path)
        o.write(output_path)
