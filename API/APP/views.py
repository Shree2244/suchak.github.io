from django.shortcuts import render

# Create your views here.
# import pytesseract
# from pdf2image import convert_from_path
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import os
# import json
# import spacy
# from .serializers import PDFUploadSerializer
# from .model_processing import process_file

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the NER API")

# # Load the custom NER model
# model_ner = spacy.load(os.path.join(settings.BASE_DIR, 'APP', 'model-best'))

# class ExtractEntitiesView(APIView):
#     def post(self, request):
#         serializer = PDFUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             pdf_file = serializer.validated_data['pdf_file']
#             fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'pdfs'))
#             filename = fs.save(pdf_file.name, pdf_file)
#             file_path = fs.path(filename)

#             annotated_entities = process_file(file_path, model_ner)
            
#             json_dir = os.path.join(settings.MEDIA_ROOT, 'json')
#             os.makedirs(json_dir, exist_ok=True)
            
#             annotated_file_path = os.path.join(json_dir, f"annotated_{os.path.splitext(filename)[0]}.json")
#             with open(annotated_file_path, 'w', encoding='utf-8') as f:
#                 json.dump(annotated_entities, f, ensure_ascii=False, indent=4)

#             return Response(annotated_entities, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

model_ner = spacy.load(r"D:\Web Dev\django\API\APP\model-best")

@csrf_exempt
@api_view(['POST'])
def process_pdf(request):
    api_key = request.headers.get('API-Key') or request.POST.get('api_key')

    if api_key not in settings.VALID_API_KEYS:
        return Response({'error': 'You are not an authenticated user.'}, status=403)

    if request.method == 'POST' and request.FILES:
        pdf_file = list(request.FILES.values())[0]
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
