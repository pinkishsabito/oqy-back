from rest_framework import serializers
from oqy.core.domain.entities import Book, BookQuestion


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()
    publication_date = serializers.DateField()
    group_id = serializers.IntegerField()

    def create(self, validated_data):
        return Book(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.publication_date = validated_data.get(
            "publication_date", instance.publication_date
        )
        return instance


class BookQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question_text = serializers.CharField()
    book_id = serializers.IntegerField()

    def create(self, validated_data):
        return BookQuestion(**validated_data)

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get(
            "question_text", instance.question_text
        )
        return instance
