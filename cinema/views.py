from rest_framework import viewsets

from cinema.models import CinemaHall, Genre, Actor, Movie
from cinema.serializers import CinemaHallSerializer, GenreSerializer, \
    ActorSerializer, MovieListSerializer, \
    MovieDetailSerializer, MovieSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaHallSerializer
    queryset = CinemaHall.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        if self.action == "retrieve":
            return MovieDetailSerializer
        return MovieSerializer
