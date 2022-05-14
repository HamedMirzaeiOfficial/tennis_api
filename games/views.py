from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Nationality, Player, Competition
from .serializers import NationalitySerializer, PlayerSerializer, CompetitionSerializer
from rest_framework.throttling import ScopedRateThrottle


class NationalityList(generics.ListCreateAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
    name = 'nationality-list'
    filter_fields = ('country', )
    search_fields = ('^country', )


class NationalityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
    name = 'nationality-detail'


class PlayerList(generics.ListCreateAPIView):
    throttle_scope = 'players'
    throttle_classes = (ScopedRateThrottle, )
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'
    filter_fields = ('first_name', 'last_name', 'country')
    search_fields = ('^first_name', '^last_name', '^country')
    ordering_fields = ('first_name', 'last_name', 'country', 'birth_day')


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'players'
    throttle_classes = (ScopedRateThrottle, )
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = 'competition-list'
    filter_fields = ('name', 'award')
    search_fields = ('^name', )
    ordering_fields = ('name', 'award')


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = 'competition-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'nationalities': reverse(NationalityList.name, request=request),
            'players': reverse(PlayerList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
        })
