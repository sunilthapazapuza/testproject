from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def santhosh_version():
    return "santhosh"

def madesh():
    return "madesh"

def sunil():
    return "Sunil"