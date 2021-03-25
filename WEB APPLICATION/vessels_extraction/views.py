from django.shortcuts import render
from vessels_extraction.predictions.predict_retinal_vessels import predict_vessels
from PIL import Image
from io import BytesIO
from pathlib import Path
import os
import matplotlib.pyplot as plt


# Create your views here.
def vessels_segment(request):
    template_name = 'vessels_extraction/vessels_extraction.html'
    context = {
        'status': "not-uploaded"
    }
    if request.method == 'POST':
        if request.POST.get("upload_vessels"):
            image_files = request.FILES.getlist('browse_vessels')
            if not image_files:
                context = {
                    'status': "no-image"
                }
                return render(request, template_name, context)
            images = []
            for img in image_files:
                img_name = img.name
                image = Image.open(BytesIO(img.read()))
                images.append(image)
            for file in os.listdir("media/blood_vessels/"):
                os.remove("media/blood_vessels/" + file)
            images[0].save("media/blood_vessels/predict_vessels.jpg", "JPEG", quality=100)

            context = {
                'status': "uploaded",
                'predict': "false"
            }
            return render(request, template_name, context)

        elif request.POST.get("predict_vessels"):
            my_file = Path("media/blood_vessels/predict_vessels.jpg")
            if my_file.is_file():
                input_image = Image.open("media/blood_vessels/predict_vessels.jpg")
            else:
                context = {
                    'status': "no-image"
                }
                return render(request, template_name, context)
            predicted_image = predict_vessels(input_image)
            # predicted_image.save("media/blood_vessels/predicted_vessels.jpg", "JPEG", quality=100)
            plt.imsave("media/blood_vessels/predicted_vessels.jpg", predicted_image)
            context = {
                'status': "uploaded",
                'predict': "true"
            }
            return render(request, template_name, context)

    return render(request, template_name, context)
