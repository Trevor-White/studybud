from django.forms import ModelForm
from .models import Room, Topic


class RoomForm(ModelForm):
    """This is a doc string"""

    class Meta:
        """Child of RoomForm - pulls all fields"""

        model = Room
        fields = "__all__"


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
