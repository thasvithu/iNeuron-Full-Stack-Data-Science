from PIL import Image, ImageDraw, ImageFont

# List of names for certificates
list_names = ['Vimalathas Vithusan', 'Ravichandran Niranjala', 'Anura Kumara Dissanayaka', 'Vimalathas Kudumpam Namathesiya Sarvam']

# Load HKGrotesk-Bold font (Adjust the path to where the .otf font is located)
font_path = "./HKGrotesk-Bold.otf"  # Replace with the actual path to HKGrotesk-Bold.otf
font_size = 36
font = ImageFont.truetype(font_path, font_size)

# Set text color (using #050a30 which is RGB: 5, 10, 48)
text_color = (5, 10, 48)

# Path to save the generated certificates
output_folder = r'G:\Data Science\iNeuron Full Stack Data Science Full Course\iNeuron Full Stack Data Science Full Course - Repo\01 Python\Projects\02 Auto\Generated Certificates'

# Iterate over the list of names
for name in list_names:
    # Open the certificate template
    template = Image.open('certificate.png')

    # Create a drawing context
    draw = ImageDraw.Draw(template)

    # Get the image size and calculate text size
    image_width, image_height = template.size
    text_width, text_height = draw.textsize(name, font=font)

    # Calculate position to center the name horizontally
    text_x = (image_width - text_width) // 2
    text_y = image_height // 2  # Adjust if necessary to vertically position the name

    # Add the name to the certificate
    draw.text((text_x, text_y), name, font=font, fill=text_color)

    # Save the certificate with the name
    certificate_path = f"{output_folder}/{name}.jpg"
    template.save(certificate_path)

    print(f"Certificate generated for {name} at {certificate_path}")

print("All certificates have been generated successfully!")
