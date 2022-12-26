from rest_framework import serializers
from todo.models import Task
from accounts.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["pk","author", "title", "status", "created_date", "updated_date"]
        read_only_fields = ["author","created_date", "updated_date"]

    def create(self, validated_data):
        validated_data["author"] = User.objects.get(
            id=self.context.get("request").user.id
        )
        return super().create(validated_data)