# Visualizations types and settings
This section describes all the possible visualizations that can be added to an event, as well as the API to be imported into Play. For each one of these possibilities, there is a dataclass defined in `visualizations.py` so that they can be easily added from the code.  

## Fields common to all visualizations

The following attributes have to be defined for each tool. Annotations' order matters, they will be created and displayed in the same order they are declared, first annotation will be rendered at the bottom/background.
```
{
  start_time: 1040, // Milliseconds
  end_time: 2130, // Milliseconds
  tool_id: 'players', // The ID of the tool
  ... // Each tool could have other mandatory attributes
  options: {}, // Optional object attribute for the tool
  version: 2 // Which version of API it's the viz compatible with
}
```

## Tools
This is a list of all the tools that is possible to add as annotations. Each option of each tool is optional. If you don't include some of them, default value will be used. The `options` attribute and the children of it are optional. If you don't include some or all of them, default values will be used

### Players
The `tool_id` is `players`.

**Players**
```
players: ['P001', 'P002']
```

**Options**
```
options: {
  id: false,
  speed: false,
  size: 1.0, // [0.2, 2.5]
  color: '#000000',
  boxPositionDown: false,
  spotlight: false,
  spotlightSize: 0.5, // Multiplier [0.2, 4.0]
  spotlightColor: '#FFFFFF',
  spotlightOpacity: 0.43, // [0.0, 1.0]
  spotlightHeight: 2.0, // [0.1, 10.0]
  ringSize: 0.73,
  ringBorder: false,
  ringBorderColor: '#FFFFFF',
  ringFill: false,
  ringFillColor: '#DC3322',
  is3d: false
}

```
***
### Trails
The `tool_id` is `trails`.

**Players**
```
players: ['P001', 'P002']
```

**Options**
```
options: {
  color: '#0062ad',
  continuous: true,
  dotted: false,
  dashSize: 1.0, // Multiplier [0.2, 2.5]. Only Dotted
  is3d: false,
  ringBorder: true,
  offsetOpacity: 0.26, // [0.0, 1.0]
  opacity: 1.0, // [0.0, 1.0]
  ringBorderColor: "#ffffff",
  ringFill: true,
  ringFillColor: '#009cdd',
  ringSize: 1.0, // Multiplier [0.6, 4.0]
  seconds: 5.0, // [1.0, 99.0]
  thickness: 0.1, // Multiplier [0.1, 5.0]. Only in 3D
  width: 0.24 // Multiplier [0.1, 2.0]
}
```
***
### Future Trails
The `tool_id` is `futureTrails`.

**Players**
```
players: ['P001', 'P002']
```

**Options**
```
options: {
  color: '#ff9e2d',
  continuous: true,
  dashSize: 0.6, // Multiplier [0.2, 2.5]. Only Dotted
  dotted: false,
  is3d: false,
  offsetOpacity: 0.05, // [0.0, 1.0]
  opacity: 1.0, // [0.0, 1.0]
  ringBorder: true,
  ringBorderColor: "#ffffff",
  ringFill: true,
  ringFillColor: '#ffdc3a',
  ringSize: 1.0, // Multiplier [0.6, 4.0]
  seconds: 5.0, // [1.0, 99.0]
  thickness: 0.23, // Multiplier [0.1, 5.0]. Only in 3D
  width: 0.29 // Multiplier [0.1, 2.0]
}
```
***
### Magnifiers
The `tool_id` is `magnifiers`.

**Players**
```
players: ['P001', 'P002']
```

**Options**
```
options: {
  color: '#ffffff',
  zoom: 1.0, // [0.2, 1.5]
  size: 1.0 // [0.5, 1.5]
}
```
***
### Measurer
The `tool_id` is `measurer`.

**Players**
```
players: ['P001', 'P002']
```

**Options**
```
options: {
  borderColor: '#dc3322',
  borderEdgeOpacity: 0.4, // [0.0, 1.0]
  borderOpacity: 0.9, // [0.0, 1.0]
  closed: false,
  continuous: true,
  dashSize: 1.45, // Multiplier [0.2, 2.5]. Only Dotted
  distance: true,
  distanceColor: '#ffffff',
  distanceIs3d: false,
  distancePosition: 0.92, // Multiplier [0.5, 2.0]
  distanceOpacity: 1.0, // [0.0, 1.0]
  distanceSize: 1.01, // Multiplier [0.5, 1.5]
  dotted: false,
  fillColor: '#dc3322',  Only Closed
  fillOpacity: 0.42, // [0.0, 1.0]
  is3d: false,
  ringBorder: true,
  ringBorderColor: '#ffffff',
  ringFill: true,
  ringFillColor: '#dc3322',
  ringSize: 0.91, // Multiplier [0.6, 4.0]
  thickness: 0.13, // Multiplier [0.0, 5.0]. Only in 3D
  width: 0.23, // Multiplier [0.15, 2.0]
}
```
***
### Team Size
The `tool_id` is `teamSize`.

**Team**
```
team: 'T001'
```

**Line**
```
line: 'width' // Values: 'width' or 'length'
```

**Options**
```
options: {
  continuous: true,
  dotted: false,
  color: '#683391',
  x: 0.0,
  y: 0.0,
  width: 0.23, // [0.1, 5.0]
  edgeOpacity: 0.0, // [0.0, 1.0]
  opacity: 1.0, // [0.0, 1.0]
  thickness: 0.22, // Multiplier [0.0, 5.0]. Only in 3D
  dashSize: 0.6, // Multiplier [0.2, 2.5]. Only Dotted
  distance: true,
  distanceColor: '#ffffff',
  distancePosition: 1.12, // [0.5, 2.0]
  distanceOpacity: 1.0, // Multiplier [0.0, 1.0]
  distanceSize: 1.3, // Multiplier [0.5, 1.5]
  distanceIs3d: false,
  is3d: false
}
```
***
### Tactical Lines
The `tool_id` is `tacticalLines`.

**Team**
```
team: 'T001'
```

**Line**
```
line: 'defenders' // Values: 'defenders', 'midfielders' or 'strikers'
```

**Options**
```
options: {
  borderColor: "#ffffff",
  borderEdgeOpacity: 0.3, // [0.1, 1.0]
  borderOpacity: 1.0, // [0.0, 1.0]
  fillColor: "#ffffff",
  fillOpacity: 0.4, // [0.0, 1.0]
  closed: false, // Only used when line is 'midfielders'
  width: 0.23, // [0.1, 2.0]
  thickness: 0.3, // Multiplier [0.0, 5.0]. Only in 3D
  dashSize: 1.0, // Multiplier [0.2, 2.5]. Only Dotted
  continuous: true,
  dotted: false,
  is3d: false,
  ringBorder: true,
  ringBorderColor: "#ffffff",
  ringFill: true,
  ringFillColor: "#ffffff",
  ringSize: 0.6, // [0.6, 4.0]
  distance: true,
  distanceColor: "#ffffff",
  distancePosition: 0.5, // Multiplier [0.5, 2.0]
  distanceOpacity: 1.0, // [0.0, 1.0]
  distanceSize: 0.73, // [0.5, 1.5]
  distanceIs3d: false
}
```
***
### Line 3D
The `tool_id` is `line3d`.

**Points**
```
// Normalized
points: {
  start: { x: 0.0, y: 0.0 },
  end: { x: 0.0, y: 0.0 }
}
```

**Options**
```
options: {
  arrowheadWidth: 1.5, // [0.99, 2.0]
  color: '#ff4f43',
  continuous: true,
  curvature: 0.0, // [-1.0, 1.0]
  dashSize: 0.4, // Multiplier [0.2, 2.5]
  distance: false,
  distanceColor: '#ffffff',
  distancePosition: 0.92, // Multiplier [0.5, 2.0]
  distanceOpacity: 1.0, // [0.0, 1.0]
  distanceSize: 1.01, // Multiplier [0.5, 4.0]
  distanceIs3d: false,
  dotted: false,
  dynamic: false,
  edgeOpacity: 0.2, // [0.0, 1.0]
  opacity: 0.9, // [0.0, 1.0]
  height: 0.075, // [0.0, 0.15]
  heightCenter: 0.0, // [-1.0, 1.0]
  is3d: false,
  pinned: false,
  thickness: 0.15, // Multiplier [0.0, 5.0]
  width: 0.5 // [0.1, 5.0]
}
```
***
### Freehand
The `tool_id` is `freehand`.

**Points**
```
// Normalized: screen-space or field-space if 'is3d' is enabled.
points: [
  { x: 0.0, y: 0.0 },
  ...,
  { x: 0.0, y: 0.0 }
]
```

**Options**
```
options: {
  color: '#9edd34',
  arrowheadWidth: 3.0, // [0.99, 5.0]
  continuous: true,
  dashSize: 0.5, // Multiplier [0.2, 2.0]. Only Dotted
  dotted: false,
  offsetOpacity: 0.2, // [0.0, 1.0]
  opacity: 0.9, // [0.0, 1.0]
  is3d: false,
  pinned: false,
  thickness: 0.07, // Multiplier [0.0, 5.0]. Only in 3D
  width: 0.2 // [0.1, 0.2]
}
```
***
### Circle
The `tool_id` is `circle`.

**Center and Radius**
```
// Normalized: screen-space or field-space if 'is3d' is enabled.
center: { x: 0.0, y: 0.0 },
radius: { x: 0.1, y: 0.1 }
```

**Options**
```
options: {
  borderColor: '#b3b3b3',
  borderOpacity: 1.0, // [0.0, 1.0]
  fillColor: '#ffdc3a',
  fillOpacity: 0.26, // [0.0, 1.0]
  fillSolid: true,
  fillPattern: false,
  is3d: false,
  pinned: false,
  thickness: 0.5, // Multiplier [0.0, 5.0]. Only in 3D
  width: 0.62 // [0.0, 3.0]
}
```
***
### Shape
The `tool_id` is `shape`.

**Points**
```
// Normalized: screen-space or field-space if 'is3d' is enabled.
points: [
  { x: 0.0, y: 0.0 },
  ...,
  { x: 0.0, y: 0.0 }
]
```

**Options**
```
options: {
  borderColor: '#0062ad',
  borderOpacity: 1.0, // [0.1, 1.0]
  borderContinuous: false,
  borderDotted: true,
  closed: false,
  dashSize: 0.6, // Multiplier [0.5, 1.5]. Only Dotted
  distance: true,
  distanceColor: "#ffffff",
  distancePosition: 1.0, // Multiplier [0.5, 2.0]
  distanceOpacity: 1.0, // [0.0, 1.0]
  distanceSize: 1.0, // [0.5, 1.5]
  distanceIs3d: false,
  fillColor: '#0062ad',
  fillOpacity: 0.25, // [0.0, 1.0]
  fillSolid: true,
  fillPattern: false,
  is3d: false,
  pinned: false,
  thickness: 0.1, // Multiplier [0.0, 5.0]. Only in 3D
  width: 0.15 // [0.0, 2.0]
}
```
***
### Arrow
The `tool_id` is `arrow`.

**Points**
```
// Normalized: screen-space or field-space if 'is3d' is enabled.
points: {
  start: { x: 0.0, y: 0.0 },
  end: { x: 0.0, y: 0.0 }
}
```

**Options**
```
options: {
  arrowheadWidth: 1.5,  // [0.99, 2.0]
  color: '#ff4f43',
  continuous: true,
  curvature: 0.0,  // Multiplier [-1.0, 1.0]. Only in 3D
  dashSize: 0.4, // Multiplier [0.2, 2.5]. Only Dotted
  distance: false,
  distanceColor: "#ffffff",
  distancePosition: 0.92, // Multiplier [0.5, 2.0]
  distanceOpacity: 1.0, // [0.0, 1.0]
  distanceSize: 1.01, // [0.5, 4.0]
  distanceIs3d: false,
  dotted: false,
  dynamic: false,
  edgeOpacity: 0.2, // [0.0, 1.0]
  opacity: 0.9, // [0.0, 1.0]
  height: 0.0, // [0.0, 0.15]
  heightCenter: 0.0,  // [-1.0, 1.0]
  is3d: false,
  pinned: false,
  thickness: 0.15, // Multiplier [0.0, 5.0]. Only in 3D
  width: 0.5 // [0.1, 5.0]
}
```
***
### Dragger
The `tool_id` is `dragger`.

**Points**
```
// Normalized: screen-space only. Flag 'is3d' is only applied to arrow.
points: {
  start: { x: 0.0, y: 0.0 },
  end: { x: 0.0, y: 0.0 }
}
```

**Options**
```
options: {
  arrowColor: '#ffdc3a',
  arrowContinuous: true,
  arrowDashSize: 0.6, // Multiplier [0.6, 2.5]. Only arrowDotted
  arrowDotted: false,
  arrowDynamic: false,
  arrowheadWidth: 2.0, // [0.0, 2.0]
  arrowEdgeOpacity: 0.2, // [0.0, 1.0]
  arrowOpacity: 0.9, // [0.0, 1.0]
  arrowOffsetY: 0.46, // [-1.0, 1.0]
  arrowThickness: 0.23, // Multiplier [0.0, 5.0]. Only in 3D
  arrowWidth: 0.65, // [0.2, 5.0]
  distance: false,
  distanceColor: "#ffffff",
  distanceIs3d: false,
  distancePosition: 1.0, // [0.5, 2.0]
  distanceOpacity: 1.0, // [0.0, 1.0]
  distanceSize: 1.0, // [0.5, 4.0]
  fade: 0.5, // [0.1, 1.0]
  is3d: false, // Refer to arrow
  opacity: 0.4, // [0.0, 1.0]
  scale: 1.0, // [0.2, 2.0]
  size: 1.0, // [0.5, 4.0]
  smoothing: 0.05, // [0.0, 1.0]
  threshold: 0.2 // [0.0, 1.0]
}
```
***
### Text Box
The `tool_id` is `textBox`.

**Text**
```
text: 'Insert Text'
```

**Position**
```
position: { x: 0.45, y: 0.45 } // Normalized: screen-space or field-space if 'is3d' is enabled.
```

**Options**
```
options: {
  width: 0.1,
  height: 0.1,
  size: 1.0, // [0.5, 4.0]
  rotation: 0.0, // [-Math.PI, Math.PI]
  color: "#ffffff",
  opacity: 1.0, // [0.0, 1.0]
  align: 'center',
  background: false,
  backgroundColor: "#000000",
  backgroundOpacity: 0.5, // [0.0, 1.0]
  is3d: false
}
```
***
### Image
The `tool_id` is `image`. Image will be downloaded locally and placed in the workspace path.

**URL**
```
url: 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'
```

**Position**
```
position: { x: 0.25, y: 0.25 } // Normalized: screen-space or field-space if 'is3d' is enabled.
```

**Scale**
```
scale: { x: 0.5, y: 0.5 } // Normalized: screen-space or field-space if 'is3d' is enabled.
```

**Options**
```
options: {
  rotation: 0.0, // [-Math.PI, Math.PI]
  opacity: 1.0, // [0.0, 1.0]
  is3d: false
}
```

***
### Pause
The `tool_id` is `pause`.

**Pause Time**
```
pause_time: 5000 // Milliseconds
```
***
### Chroma-Key
The `tool_id` is `chromaKey`. It'll be computed on each clip created. Options should be set according to the scene, so if it remains similar during a game, maybe you want to adapt these values from a sample clip in Play and use them in all chroma-key events. Otherwise, you should not pass any option, use default values and fit them in each clip if needed. 

Since the order in which visualizations added declared in the event is preserved when they are imported in Play, the chroma-key tool should be added in the specific desired position. For example, if you want to add shape in the field and an arrow, but chroma key only to have an effect on the shape on the field, the order in the event should be: shape - chroma key - arrow.

**Options**
```
options: {
  threshold: 0.01, // [0.0, 1.0]
  smoothing: 0.1 // [0.0, 1.0]
}
```

### Timer
The `tool_id` is `timer`.

**Options**
```
options: {
  x: 0.825, // Normalized: screen-space or field-space if 'is3d' is enabled.
  y: 0.02, // Normalized: screen-space or field-space if 'is3d' is enabled.
  width: 0.16,
  height: 0.15,
  offsetTime: 0, // Unix timestamp.
  decimals: 0, // 0 (no decimals), 1 (tenths of second), 2 (hundredths of second) and 3 (thousandths of second)
  size: 2.7, // [0.5, 4.0]
  rotation: 0.0, [-Math.PI, Math.PI]
  color: '#ffffff',
  opacity: 1.0, // [0.0, 1.0]
  background: true,
  backgroundColor: '#000000',
  backgroundOpacity: 0.75, // [0.0, 1.0]
  clockwise: true,
  is3d: false
}
```

### Offside
The `tool_id` is `offside`.

**Options**
```
options: {
  teamId:  'T001',
  defender: true,
  defenderColor: '#ffffff',
  defenderOpacity: 1.0, // [0.0, 1.0]
  defenderContinuous: true,
  defenderDotted: false,
  defenderWidth: 0.12, // [0.05, 1.0]
  defenderThickness: 0.05, // [0.0, 7.5]
  defenderDashSize: 0.6, // [0.2, 2.5]
  defenderFieldColor: '#000000',
  defenderFieldOpacity: 0.55, // [0.0, 1.0]
  defenderFieldFade: 5.0, // [1.0, 8.0]
  attacker: true,
  automaticColor: false,
  attackerColor: '#ffff00',
  attackerOpacity: 1.0, // [0.0, 1.0]
  attackerContinuous: true,
  attackerDotted: false,
  attackerWidth: 0.12, // [0.05, 1.0]
  attackerThickness: 0.05, // [0.0, 7.5]
  attackerDashSize: 0.6, // [0.2, 2.5]
  attackerFieldColor: '#ffff00',
  attackerFieldOpacity: 0.0, // [0.0, 1.0]
  attackerFieldFade: 2.0 // [1.0, 8.0]
}
```