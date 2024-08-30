# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage

# def upload_view(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage()
#         filename = fs.save(pdf_file.name, pdf_file)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'NERapp/upload.html', {'uploaded_file_url': uploaded_file_url})
#     return render(request, 'NERapp/upload.html')

# def extracted_view(request):
#     return render(request, 'NERapp/extracted_info.html')

#----------------------------------\/\/\/\/\/

# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage

# def upload_view(request):
#     return render(request, 'NERapp/upload.html')

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage

# @csrf_exempt
# def upload_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage()
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_url = fs.url(filename)
#         return JsonResponse({'file_url': file_url, 'message': 'File uploaded successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

#----------------------------------------^^^^^^

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings

# @csrf_exempt
# def upload_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_url = fs.url(filename)
#         return JsonResponse({'file_url': file_url, 'message': 'File uploaded successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# NERapp/views.py
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings

# @csrf_exempt
# def upload_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_url = fs.url(filename)
#         return JsonResponse({'file_url': file_url, 'message': 'File uploaded successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)


# --------------------------------------------

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import os
# import fitz  # PyMuPDF
# import pytesseract
# from PIL import Image
# import spacy

# # Load the spaCy model
# model_path = os.path.join(settings.BASE_DIR, 'NERapp/model-best')
# nlp = spacy.load(model_path)

# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         pix = page.get_pixmap()
#         img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#         text += pytesseract.image_to_string(img, lang='mar')  # Use Tesseract for OCR with Marathi language
#     return text

# def run_model_inference(pdf_path):
#     text = extract_text_from_pdf(pdf_path)
#     doc = nlp(text)

#     # Extract entities
#     extracted_data = {
#         'court_name': '',
#         'act': '',
#         'person_name': '',
#         'order_no': '',
#         'order_date': ''
#     }
    
#     for ent in doc.ents:
#         if ent.label_ == 'CourtName':
#             extracted_data['court_name'] = ent.text
#         elif ent.label_ == 'Act':
#             extracted_data['act'] = ent.text
#         elif ent.label_ == 'PersonName':
#             extracted_data['person_name'] = ent.text
#         elif ent.label_ == 'OrderNo':
#             extracted_data['order_no'] = ent.text
#         elif ent.label_ == 'OrderDate':
#             extracted_data['order_date'] = ent.text

#     return extracted_data

# @csrf_exempt
# def upload_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_url = fs.url(filename)

#         # Run model inference
#         extracted_data = run_model_inference(os.path.join(settings.MEDIA_ROOT, filename))

#         return JsonResponse({'file_url': file_url, 'extracted_data': extracted_data, 'message': 'File uploaded and processed successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# -------------------------------------------

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from .model_processing import process_file  
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Home Page")

# @api_view(['POST'])
# def process_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_path = fs.path(filename)
        
#         # Process the PDF file with your model
#         annotated_entities = process_file(file_path, settings.SPACY_MODEL)
        
#         # Return the annotated entities as a JSON response
#         return Response(annotated_entities)
#     return Response({'error': 'Invalid request'}, status=400)

# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage

# def upload_view(request):
#     return render(request, 'NERapp/upload.html')

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage

# @csrf_exempt
# def upload_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage()
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_url = fs.url(filename)
#         return JsonResponse({'file_url': file_url, 'message': 'File uploaded successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# ---------------------21
# NERapp/views.py
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from .model_processing import process_file
# import os

# def home(request):
#     return render(request, 'NERapp/upload.html')

# def upload_view(request):
#     return render(request, 'NERapp/upload.html')

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def upload_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage()
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_url = fs.url(filename)
#         return JsonResponse({'file_url': file_url, 'message': 'File uploaded successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)
# ---------------------21

# @api_view(['POST'])
# def process_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_path = fs.path(filename)
        
#         # Process the PDF file with your model
#         annotated_entities = process_file(file_path, settings.SPACY_MODEL)
        
#         # Save the annotated entities to a file (if needed)
#         annotated_file_path = os.path.join(settings.MEDIA_ROOT, f"annotated_{filename}.txt")
#         with open(annotated_file_path, 'w') as f:
#             for key, value in annotated_entities.items():
#                 f.write(f"{key}: {value}\n")
        
#         # Return the annotated entities as a JSON response
#         return Response(annotated_entities)
#     return Response({'error': 'Invalid request'}, status=400)

# \/\/\/----------\/\/\/
# import os
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from .model_processing import process_file
# import json 
# import spacy

# model_ner = spacy.load(r"D:\Web Dev\django\django_project\NERapp\model-best")
# @api_view(['POST'])
# def process_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_path = fs.path(filename)
#         print(pdf_file.name)
        
#         # Process the PDF file with your model
#         annotated_entities = process_file(file_path, settings.SPACY_MODEL)
        
#         # Create the 'json' directory inside MEDIA_ROOT if it doesn't exist
#         json_dir = os.path.join(settings.MEDIA_ROOT, 'json')
#         os.makedirs(json_dir, exist_ok=True)
        
#         # Save the annotated entities to a file in the 'json' directory
#         annotated_file_path = os.path.join(json_dir, f"annotated_{filename}.json")
#         with open(annotated_file_path, 'w') as f:
#             json.dump(annotated_entities, f)  # Save as JSON

#         # Return the annotated entities as a JSON response
#         print(annotated_entities, "done!")
#         return Response(annotated_entities)
#     return Response({'error': 'Invalid request'}, status=400)
# ^^^^^^^^^^^^^^^^^^

# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.files.storage import FileSystemStorage
# from django.http import JsonResponse
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# import os
# import json
# import spacy
# from .model_processing import process_file

# # Load your SpaCy model once at the beginning
# model_ner = spacy.load(r"D:\Web Dev\django\django_project\NERapp\model-best")

# def home(request):
#     return render(request, 'NERapp/upload.html')

# def upload_view(request):
#     return render(request, 'NERapp/upload.html')

# @csrf_exempt
# def upload_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage()
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_url = fs.url(filename)
#         return JsonResponse({'file_url': file_url, 'message': 'File uploaded successfully'})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# import os
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from .model_processing import process_file
# import json 
# import spacy

# model_ner = spacy.load(r"D:\Web Dev\django\django_project\NERapp\model-best")

# @api_view(['POST'])
# def process_pdf(request):
#     if request.method == 'POST' and request.FILES.get('pdf_file'):
#         pdf_file = request.FILES['pdf_file']
#         fs = FileSystemStorage(location=settings.MEDIA_ROOT)
#         filename = fs.save(pdf_file.name, pdf_file)
#         file_path = fs.path(filename)
#         print(pdf_file.name)
        
#         # Process the PDF file with your model
#         annotated_entities = process_file(file_path, model_ner)
        
#         # Create the 'json' directory inside MEDIA_ROOT if it doesn't exist
#         json_dir = os.path.join(settings.MEDIA_ROOT, 'json')
#         os.makedirs(json_dir, exist_ok=True)
        
#         # Save the annotated entities to a file in the 'json' directory
#         annotated_file_path = os.path.join(json_dir, f"annotated_{filename}.json")
#         with open(annotated_file_path, 'w', encoding='utf-8') as f:
#             json.dump(annotated_entities, f, ensure_ascii=False, indent=4)  # Save as JSON with Unicode characters

#         # Return the annotated entities as a JSON response
#         return Response(annotated_entities)
#     return Response({'error': 'Invalid request'}, status=400)

# p--------------------------------------
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import json
import spacy
from .model_processing import process_file

model_ner = spacy.load(r"D:\Web Dev\django\django_project\NERapp\model-best")

def home(request):
    return render(request, 'NERapp/upload.html')

def upload_view(request):
    return render(request, 'NERapp/upload.html')

@csrf_exempt
def upload_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        file_url = fs.url(filename)
        return JsonResponse({'file_url': file_url, 'message': 'File uploaded successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@api_view(['POST'])
def process_pdf(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(pdf_file.name, pdf_file)
        file_path = fs.path(filename)

        annotated_entities = process_file(file_path, model_ner)
        
        json_dir = os.path.join(settings.MEDIA_ROOT, 'json')
        os.makedirs(json_dir, exist_ok=True)
        
        annotated_file_path = os.path.join(json_dir, f"annotated_{filename}.json")
        with open(annotated_file_path, 'w', encoding='utf-8') as f:
            json.dump(annotated_entities, f, ensure_ascii=False, indent=4)

        return Response(annotated_entities)
    return Response({'error': 'Invalid request'}, status=400)


