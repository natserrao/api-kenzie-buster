from rest_framework import serializers
from .models import RatingMovie, Movie, MovieOrder
from datetime import datetime
from django.utils import timezone


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, required=True)
    duration = serializers.CharField(max_length=10, required=False, allow_null=True)
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices,
        default=RatingMovie.RATED_G,
    )
    synopsis = serializers.CharField(required=False, allow_null=True)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie) -> str:
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2, required=True)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj: MovieOrder):
        return obj.movie.title

    def get_buyed_by(self, obj: MovieOrder):
        return obj.user.email

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
