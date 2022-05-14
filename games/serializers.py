from rest_framework import serializers
from .models import Nationality, Player, Competition


class NationalitySerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='player-detail'
    )

    class Meta:
        model = Nationality
        fields = ('url', 'pk', 'country', 'country_flag', 'players')


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        queryset=Player.objects.all(), many=True, view_name='player-detail'
    )

    class Meta:
        model = Competition
        fields = ('url', 'pk', 'name', 'award', 'players')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    # Display Nationality
    country = serializers.SlugRelatedField(
        queryset=Nationality.objects.all(), slug_field='country'
    )
    competitions = CompetitionSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('url', 'first_name', 'last_name', 'birth_day', 'country', 'competitions')

