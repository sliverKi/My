from rest_framework.serializers import ModelSerializer

from .models import Idol, Schedule


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            "pk",
            "ScheduleTitle",
            "ScheduleType",
            "idol_groupName",
            "idol_name",
            "participant",  # idol_name (?)
            "description",
        )


class IdolsListSerializer(ModelSerializer):
    class Meta:
        model = Idol
        fields = ("pk", "idol_solo", "idol_profile", "paticipant,")


class IdolDetailSerializer(ModelSerializer):

    idol_schedules = ScheduleSerializer(
        read_only=True, many=True  # 스케줄을 필수 항목으로 인식하지 않음
    )

    class Meta:
        model = Idol
        fields = "__all__"
