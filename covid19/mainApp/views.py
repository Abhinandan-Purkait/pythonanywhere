from django.shortcuts import render
import cv2
import warnings
from .models import Images
import numpy as np
import keras
import cv2
import keras
import warnings
from .models import Images
import tensorflow
import tensorflow_core
# MKIT STARTS


def load_models():
    model1 = keras.models.load_model("models/first_level_hierarchy.h5")
    model2 = keras.models.load_model("models/second_level_hierarchy.h5")
    return model1, model2


def test_pneumonia(image, model1, model2):
    logs = ["Covid 19", "Bacterial Pneumonia", "Viral Pneumonia", "Negative"]
    result = dict()
    image = (np.array([cv2.resize(image, (150, 150))]).reshape(
        1, 150, 150, 3)).astype('float32')/255
    base = model1.predict(image)
    indx = np.argmax(base)
    if indx == 1:
        derived = model2.predict(image)
        indx_der = np.argmax(derived)
        result['Pneumonia'] = [logs[indx_der], derived[0][indx_der]*100]
    elif indx == 0:
        result['Pneumonia'] = [logs[3], base[0][indx]*100]
    return(result)


def index(request):
    return render(request, 'index.html')


def statistics(request):
    return render(request, "statistics.html")


def prevention(request):
    return render(request, 'prevention.html')


def symptoms(request):
    return render(request, 'symptoms.html')


def faq(request):
    return render(request, 'faq.html')


def map_stats(request):
    return render(request, 'india_map.html')


def prediction(request):
    return render(request, 'prediction.html')


def about(request):
    return render(request, 'about.html')


def vitualMedicalKit(request):
    if request.method == 'POST':
        model1, model2 = load_models()
        typelis = []
        problis = []
        imgs = []
        for count, x in enumerate(request.FILES.getlist('image')):
            img = Images()
            print(x, "**")
            img.image = x
            print(x, "**")
            img.save()
            print(x, "**")
            imgs.append(str(x))

        for x in imgs:
            imageFile = cv2.imread("media/images/"+x)
            out = test_pneumonia(imageFile, model1, model2)
            res = out['Pneumonia']
            typelis.append(res[0])
            problis.append(res[1])

        abc = Images.objects.all()
        abc.delete()
        mainlist = zip(imgs, typelis, problis)
        return render(request, 'mkit.html', {'lis': mainlist, "Res": 'result'})
    else:
        return render(request, 'mkit.html')


def indiaAnalysis(request):
    return render(request, 'indiaanalysis.html')
