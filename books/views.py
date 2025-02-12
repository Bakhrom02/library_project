from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from docutils.nodes import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status":f"Returned {len(books)} books.",
            "books":serializer_data,
        }
        return Response(data)




# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'status':"Successfull",
                'book':serializer_data,
            }

            return Response(data)
        except Exception:
            return Response(
                {"Status":"False",
                "Message":"Book is not found"}, status=status.HTTP_404_NOT_FOUND
            )






# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get_object_or_404(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "Successfully deleted"
            }, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({
                "status": False,
                "message": "Book not found"
            }, status=status.HTTP_404_NOT_FOUND)
# class BookUpdateview(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateview(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status":True,
                 "message":f"Book {book_saved} updated successfully"
            }
        )


# class BookCreatApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreatApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            contex = {
                'status':f'{len(data)} - BOOKS ARE CREATED',
                'books':serializer.data
            }
            return Response(contex)
        else:
            return Response(
                {'status':False,
                'message':"Serializer is not valid"}, status=status.HTTP_400_BAD_REQUEST
            )


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


