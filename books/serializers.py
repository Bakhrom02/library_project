
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhasi kiritilishi shart"
                }
            )

        if not all(word.isalpha() for word in title.split()):
            raise ValidationError(
                {
                    "status": False,
                    "message": "kitobni sarlavhasi harflardan tashkil topgan bolishi kerak"
                }
            )
        #check author and title existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz"
                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx noto'g'ri kiritilgan"
                }
            )
