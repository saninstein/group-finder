from rest_framework import serializers

from app.models import Group
from app.group_finder import GroupFinder


class GroupSerializer(serializers.ModelSerializer):
    """
    Group serializer
    """
    items = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='value'
    )

    class Meta:
        model = Group
        fields = ('id', 'name', 'items')


class RawGroupItemsSerializer(serializers.Serializer):
    """
    Creates/Updates groups
    """

    items = serializers.ListField(
        child=serializers.CharField(min_length=5, max_length=128)
    )
    delimiter = serializers.RegexField(
        r'[_.*$-]', max_length=1, min_length=1, default='_', allow_blank=True
    )

    def create(self, validated_data: dict):
        """
        Updates/Creates group folders
        :param validated_data: validated data
        """
        grouped_data = GroupFinder.find(validated_data['items'], validated_data['delimiter'])
        Group.update_groups(grouped_data)
        return []
