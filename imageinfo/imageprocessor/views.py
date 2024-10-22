from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
import os

def image_metadata(image_path):
    img = Image.open(image_path)
    metadata = {
        "Filename": os.path.basename(image_path),
        "Size (pixels)": img.size,  # Размер изображения (ширина, высота)
        "Resolution (dpi)": img.info.get("dpi", "Not available"),  # Разрешение (dpi)
        "Color depth (mode)": img.mode,  # Глубина цвета
        "Format": img.format,  # Формат изображения
    }

    if img.format == "JPEG":
        metadata["Compression"] = img.info.get("compression", "Not available")

    return metadata

def upload_images(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        files = request.FILES.getlist('images')
        fs = FileSystemStorage()
        metadata_list = []

        for file in files:
            filename = fs.save(file.name, file)
            file_path = fs.path(filename)
            img = Image.open(file_path)
            metadata = {
                "Filename": file.name,
                "Size_pixels": img.size,
                "Resolution_dpi": img.info.get("dpi", "Not available"),
                "Color_depth": img.mode, 
                "Format": img.format,
            }
            metadata_list.append(metadata)

        return render(request, 'imageprocessor/results.html', {'metadata_list': metadata_list})

    return render(request, 'imageprocessor/upload.html')

