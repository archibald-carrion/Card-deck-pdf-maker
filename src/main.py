from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def main():
    # Directory containing images
    image_directory = './images'
    
    # Target dimensions in inches
    target_width_in = 2.5
    target_height_in = 3.5
    
    # Convert inches to points (1 inch = 72 points)
    target_width_pt = target_width_in * 72
    target_height_pt = target_height_in * 72
    
    # Create a PDF canvas
    pdf_filename = 'output.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Positions for images on the page
    positions = [(x, y) for x in range(3) for y in range(3)]

    # Counter for images
    image_count = 0
    
    for filename in os.listdir(image_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(image_directory, filename)
            img = Image.open(img_path)
            
            # Calculate position on the page
            col, row = positions[image_count % 9]
            x = 20 + col * (target_width_pt + 1)  # Add some padding between images
            y = letter[1] - (target_height_pt + 20) - row * (target_height_pt + 1)

            # Draw the image at the specified position and size
            c.drawImage(img_path, x=x, y=y, width=target_width_pt, height=target_height_pt)
            
            image_count += 1

            # Create a new page after 9 images
            if image_count % 9 == 0:
                c.showPage()
    
    # Save the PDF
    c.save()
    print(f"PDF saved as {pdf_filename}")

if __name__ == "__main__":
    main()
