from typing import Dict, List

from django.db import models, transaction


class Group(models.Model):
    name = models.CharField(
        max_length=128, blank=False, null=False, unique=True, db_index=True)

    @classmethod
    def update_groups(cls, grouped_strings: Dict[str, List[str]]):
        """
        Updates Group models with new group data
        :param grouped_strings: grouped strings
        """
        with transaction.atomic():
            for group_name, items in grouped_strings.items():
                group, _ = Group.objects.get_or_create(name=group_name)
                Item.objects.bulk_create(
                    [
                        Item(value=item, group=group)
                        for item in items
                    ],
                    ignore_conflicts=True  # to avoid duplicates errors
                )


class Item(models.Model):
    value = models.CharField(
        max_length=128, blank=False, null=False, unique=True, db_index=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=False, null=False, related_name='items')
