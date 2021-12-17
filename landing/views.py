from django.shortcuts import render
from .models import Doctor, DocumentImage, LegalInformation, ServiceCategory, ServiceImage

def home(req):
  doctors = Doctor.objects.all()
  service_categories = ServiceCategory.objects.all()
  document_images = DocumentImage.objects.all()
  service_images = ServiceImage.objects.all()
  legal_documents = LegalInformation.objects.all()
  context = {"doctors": doctors, "service_categories": service_categories,
             "document_images": document_images, "service_images": service_images,
             "legal_documents": legal_documents}
  return render(req, "index.html", context)