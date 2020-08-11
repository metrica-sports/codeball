from kloppy.domain.models import Event, EventType, PassResult
from codeball.models.tactical import Zone


@property
def is_pass(self):
    return self.event_type == EventType.PASS


@property
def is_complete(self):
    return self.result == PassResult.COMPLETE


def into(self, zone: Zone):
    ends_in_box = (
        zone.vertices.top_left[0]
        <= self.receiver_coordinates.x
        <= zone.vertices.bottom_right[0]
        and zone.vertices.top_left[1]
        <= self.receiver_coordinates.y
        <= zone.vertices.bottom_right[1]
    )
    return ends_in_box


Event.is_pass = is_pass
Event.is_complete = is_complete
Event.into = into
