# from django.shortcuts import render
# from result.models import Result
# from feedback.models import Feedback
# from book.models import Book
# # Create your views here.
#
# import tensorflow
# import cv2
# from mtcnn.mtcnn import MTCNN
# import numpy as np
# from keras.preprocessing import image
# from autismdet import settings
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# def process(request):
#     ss=request.session["u_id"]
#     if request.method=="POST":
#         mfile=request.FILES['file']
#         fs=FileSystemStorage()
#         fname=fs.save(mfile.name,mfile)
#         print(fname)
#         # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#         filename = str(settings.BASE_DIR) + str(settings.STATIC_URL) + fname
#
#         modelfile = "Autism7.hdf5"
#         # modelfile1 = "model.hdf5"
#         modelfile = str(settings.BASE_DIR) + str(settings.STATIC_URL) + modelfile
#         # modelfile1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + modelfile1
#         model = tensorflow.keras.models.load_model(modelfile)
#         # model1 = tensorflow.keras.models.load_model(modelfile1)
#         filename = str(settings.BASE_DIR) + str(settings.STATIC_URL) + fname
#         new_img = image.load_img(filename, target_size=(150, 150), color_mode="grayscale")
#         img = image.img_to_array(new_img)
#         img = np.expand_dims(img, axis=0)
#         img = img / 255
#         pred = (model.predict(img) > 0.5).astype("int32")
#         if pred[0][0] == 0:
#             # print('Autistic')
#             # return HttpResponse('Aut')
#             a="Autistic"
#             context={
#                 'k':a
#             }
#             obv=Result()
#             obv.image=mfile
#             obv.result=a
#             obv.user_id=ss
#             # kk=Book.objects.get(user_id=ss)
#             # obv.book_id=kk.book_id
#             obv.book_id=1
#
#             obv.save()
#
#             obb = Feedback()
#             obb.feedback = "Pending"
#             obb.result = a
#             obb.image = mfile
#             obb.user_id = ss
#             # kk = Book.objects.get(user_id=ss)
#             # obb.book_id = kk.book_id
#             obb.book_id=1
#
#             obb.save()
#             return render(request,'auti_tech/result.html',context)
#         else:
#             # print('Normal')
#             # return HttpResponse('Normal')
#             a = "Normal"
#             context = {
#                 'k': a
#             }
#             obb = Result()
#             obb.image = mfile
#             obb.result = a
#             obb.user_id = ss
#             # kk = Book.objects.get(user_id=ss)
#             # obb.book_id = kk.book_id
#             obb.book_id=1
#             obb.save()
#
#
#             obb=Feedback()
#             obb.feedback="Pending"
#             obb.result=a
#             obb.image=mfile
#             obb.user_id=ss
#             # kk = Book.objects.get(user_id=ss)
#             # obb.book_id = kk.book_id
#             obb.book_id=1
#             obb.save()
#             return render(request, 'auti_tech/result.html', context)
#
#     return render(request, 'auti_tech/index.html')
#
#
#
#
#
#
#
# from django.shortcuts import render
# from result.models import Result
# from feedback.models import Feedback
# from book.models import Book
# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.preprocessing import image
# from autismdet import settings
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
#
# def process(request):
#     ss = request.session["u_id"]
#     if request.method == "POST":
#         mfile = request.FILES['file']
#         fs = FileSystemStorage()
#         fname = fs.save(mfile.name, mfile)
#         print(fname)
#
#         modelfile = "Autism7.hdf5"
#         modelfile = str(settings.BASE_DIR) + str(settings.STATIC_URL) + modelfile
#         model = tf.keras.models.load_model(modelfile)
#         filename = str(settings.BASE_DIR) + str(settings.STATIC_URL) + fname
#         new_img = image.load_img(filename, target_size=(150, 150), color_mode="grayscale")
#         img = image.img_to_array(new_img)
#         img = np.expand_dims(img, axis=0)
#         img = img / 255
#         pred = (model.predict(img) > 0.5).astype("int32")
#         if pred[0][0] == 0:
#             a = "Autistic"
#             context = {'k': a}
#             obv = Result()
#             obv.image = mfile
#             obv.result = a
#             obv.user_id = ss
#             obv.book_id = 1
#             obv.save()
#
#             obb = Feedback()
#             obb.feedback = "Pending"
#             obb.result = a
#             obb.image = mfile
#             obb.user_id = ss
#             obb.book_id = 1
#             obb.save()
#             return render(request, 'auti_tech/result.html', context)
#         else:
#             a = "Normal"
#             context = {'k': a}
#             obb = Result()
#             obb.image = mfile
#             obb.result = a
#             obb.user_id = ss
#             obb.book_id = 1
#             obb.save()
#
#             obb = Feedback()
#             obb.feedback = "Pending"
#             obb.result = a
#             obb.image = mfile
#             obb.user_id = ss
#             obb.book_id = 1
#             obb.save()
#
#             return render(request, 'auti_tech/result.html', context)
#     return render(request, 'auti_tech/index.html')



import os
from django.shortcuts import render
from result.models import Result
from feedback.models import Feedback
from book.models import Book
import tensorflow as tf
import numpy as np
import cv2
from autismdet import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def process(request):
    ss = request.session["u_id"]
    if request.method == "POST":
        mfile = request.FILES['file']
        fs = FileSystemStorage()
        fname = fs.save(mfile.name, mfile)
        print(fname)

        # Load the trained model for human detection
        human_model_file_path = os.path.join(settings.BASE_DIR, r"C:\Users\amalr\OneDrive\Desktop\Autism\autismdet\static\fd.hdf5")
        human_model = tf.keras.models.load_model(human_model_file_path)

        # Preprocess the image for human detection
        filename = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, fname)
        img_human = cv2.imread(filename)
        img_human = cv2.resize(img_human, (150, 150))  # Resize the image to 150x150 for human detection
        img_human = cv2.cvtColor(img_human, cv2.COLOR_BGR2GRAY)
        img_human = cv2.equalizeHist(img_human)
        img_human = img_human / 255
        img_human = np.expand_dims(img_human, axis=0)  # Add batch dimension
        img_human = np.expand_dims(img_human, axis=-1)  # Add channel dimension

        # Get the prediction from the human detection model
        prediction = human_model.predict(img_human)
        predicted_class = np.argmax(prediction)

        # If human faces are detected (predicted class is 1), proceed with autism prediction
        if predicted_class == 1:
            print("Human detected.")

            # Load the trained model for autism prediction
            autism_model_file_path = os.path.join(settings.BASE_DIR, "static", "Autism7.hdf5")
            autism_model = tf.keras.models.load_model(autism_model_file_path)

            # Preprocess the image for autism prediction
            img_autism = cv2.imread(filename)
            img_autism = cv2.resize(img_autism, (150, 150))  # Resize the image to 150x150 for autism prediction
            img_autism = cv2.cvtColor(img_autism, cv2.COLOR_BGR2GRAY)
            img_autism = cv2.equalizeHist(img_autism)
            img_autism = img_autism / 255
            img_autism = np.expand_dims(img_autism, axis=0)  # Add batch dimension
            img_autism = np.expand_dims(img_autism, axis=-1)  # Add channel dimension

            # Get the prediction from the autism model
            pred = (autism_model.predict(img_autism) > 0.5).astype("int32")
            if pred[0][0] == 0:
                a = "Autistic"
            else:
                a = "Normal"
        else:
            print("Not Human")
            a = "Not Human"

        # Save the result and feedback
        context = {'k': a}
        obv = Result()
        obv.image = mfile
        obv.result = a
        obv.user_id = ss
        obv.book_id = 1
        obv.save()

        obb = Feedback()
        obb.feedback = "Pending"
        obb.result = a
        obb.image = mfile
        obb.user_id = ss
        obb.book_id = 1
        obb.save()

        return render(request, 'auti_tech/result.html', context)

    return render(request, 'auti_tech/index.html')
