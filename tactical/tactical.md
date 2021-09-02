# Tactical Module
The tactical module includes different classes and methods to help work with the data from a tactical perspective. 

## Areas
An Area is a class used to define an area of the pitch. You can define simple rectangular areas, or more complex polygonal ones. To define an area you need to provide 2 or more points (in normalized coordinates, for example (0.5,0.5) would be the center of the pitch). If you provide only two points it will define a rectangular area, in which the first point is the top-left one and the second one is the bottom-right one. If you provide 3 or more points it will be consider a polygon.

Areas have a `type` attribute that will return an Enum with either `AreaType.RECTANGLE` or `AreaType.POLYGON`.

## Zones
Zones is an Enum that defines a list of zones that are tactically relevant. Each type could be defined by one or more `Area`. The list of currently defined Zones is:

- OPPONENT_BOX
- OWN_BOX
- ATTACKING_THIRD
- MIDDLE_THIRD
- DEFENDING_THIRD
- OWN_HALF
- OPPONENT_HALF
- LEFT_HALF_SPACE
- RIGHT_HALF_SPACE
- HALF_SPACES
- CENTRE
- LEFT_WING
- RIGHT_WING
- WINGS
- ZONE_14

## Using Areas and Zones
You can use Areas and Zones in the methods provided by `CodeballFrames`. For example you can do:
```python
EventsFrame.into(Zones.HALF_SPACES)
```

Or you can define your own areas and then provide them as filters:
```python
custom_area = Area((0.16,0),(0.84,1)) 
EventsFrame.into(custom_area)
```

Finally, you can combine and provide one or more areas/zones, or a mix of zones and areas:
```python
custom_area = Area((0.16,0),(0.84,1)) 
EventsFrame.into(Zones.HALF_SPACES,custom_area)
```