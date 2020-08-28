from kloppy.domain.models import Event, EventType, PassResult
from codeball.models import Zone


@property
def is_pass(self):
    return self.event_type == EventType.PASS


@property
def is_complete(self):
    return self.result == PassResult.COMPLETE


def starts(self, zone: Zone):
    return (
        zone.vertices.top_left[0]
        <= self.coordinates.x
        <= zone.vertices.bottom_right[0]
        and zone.vertices.top_left[1]
        <= self.coordinates.y
        <= zone.vertices.bottom_right[1]
    )


def ends(self, zone: Zone):
    return (
        zone.vertices.top_left[0]
        <= self.receiver_coordinates.x
        <= zone.vertices.bottom_right[0]
        and zone.vertices.top_left[1]
        <= self.receiver_coordinates.y
        <= zone.vertices.bottom_right[1]
    )


def into(self, zone: Zone):
    return not self.starts(zone) and self.ends(zone)


def inside(self, zone: Zone):
    return self.starts(zone) and self.ends(zone)


Event.is_pass = is_pass
Event.is_complete = is_complete
Event.starts = starts
Event.ends = ends
Event.into = into
Event.inside = inside
