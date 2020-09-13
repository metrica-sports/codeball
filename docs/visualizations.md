# Visualizations types and settings
This section describes all the possible visualizations that can be added to an event, as well as the aPI to be imported in Metrica Play. For each one of these possibilities, there is a dataclass defined in `visualizaitons.py` so that they can be easily added from the code.  

## Fields common to all visualizations

The following attributes have to be defined for each tool. Annotations' order matters, they will be created and displayed in the same order they are declared, first annotation will be rendered at the bottom/background.
```
{
  start_time : 1040, // Milliseconds
  end_time   : 2130, // Milliseconds
  tool_id    : 'players', // The ID of the tool
  ... // Each tool could have other mandatory attributes
  options    : {} // Optional object attribute for the tool
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
  id             : true,
  speed          : true,
  spotlight      : false,
  ring           : false,
  spotlightColor : '#FFFFFF',
  ringColor      : '#000000',
  size           : 1.0 // Multiplier, [0.6, 1.5]
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
  color : '#E66F7E',
  width : 1.0 // Multiplier, [0.5, 2.0]
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
  color : '#E66F7E',
  width : 1.0 // Multiplier, [0.5, 2.0]
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
  zoom : 1.0, // Multiplier, [0.2, 1.5]
  size : 1.0 // Multiplier, [0.5, 1.5]
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
  color     : '#040602',
  width     : 1.0, // Multiplier, [0.5, 2.0]
  filled    : false,
  distances : true,
  closed    : false
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
  color: '#E66F7E'
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
  color     : '#E66F7E',
  distances : false,
  closed    : false // Only used when line is 'midfielders'
}
```
***
### Line 3D
The `tool_id` is `line3d`.

**Points**
```
// Normalized
points: {
  start : { x: 0.0, y: 0.0 },
  end   : { x: 0.0, y: 0.0 }
}
```

**Options**
```
options: {
  color      : '#E66F7E',
  height     : 1.0, // Multiplier, [0.2, 3.0]
  width      : 1.0, // Multiplier, [0.5, 3.0]
  continuous : true, // If false, dotted
  pinned     : false // If true, anchored to field
}
```
***
### Freehand
The `tool_id` is `freehand`.

**Points**
```
// Normalized
points: [
  { x: 0.0, y: 0.0 },
  ...,
  { x: 0.0, y: 0.0 }
]
```

**Options**
```
options: {
  color      : '#E66F7E',
  width      : 1.0,  // Multiplier, [0.5, 3.0]
  continuous : true, // If false, dotted
  pinned     : false // If true, anchored to field
}
```
***
### Circle
The `tool_id` is `circle`.

**Center and Radius**
```
// Normalized
center: { x: 0.0, y: 0.0 },
radius: { x: 0.1, y: 0.1 }
```

**Options**
```
options: {
  color     : '#E66F7E',
  opacity   : 0.5,  // [0.1, 1.0]
  filled    : true,
  pinned    : false // If true, anchored to field
}
```
***
### Shape
The `tool_id` is `shape`.

**Points**
```
// Normalized
points: [
  { x: 0.0, y: 0.0 },
  ...,
  { x: 0.0, y: 0.0 }
]
```

**Options**
```
options: {
  color     : '#E66F7E',
  width     : 1.0, // Multiplier, [0.5, 3.0]
  distances : false,
  closed    : false,
  filled    : true,
  pinned    : false // If true, anchored to field
}
```
***
### Arrow
The `tool_id` is `arrow`.

**Points**
```
// Normalized
points: {
  start : { x: 0.0, y: 0.0 },
  end   : { x: 0.0, y: 0.0 }
}
```

**Options**
```
options: {
  color      : '#E66F7E',
  width      : 1.0, // Multiplier, [0.5, 3.0]
  distance   : false,
  continuous : true, // If false, dotted
  pinned     : false // If true, anchored to field
}
```
***
### Dragger
The `tool_id` is `dragger`.

**Points**
```
// Normalized
points: {
  start : { x: 0.0, y: 0.0 },
  end   : { x: 0.0, y: 0.0 }
}
```

**Options**
```
options: {
  color      : '#E66F7E',
  arrow      : true,
  threshold  : 0.2,  // [0.0, 1.0]
  smoothing  : 0.05, // [0.0, 1.0]
  fade       : 0.5,  // [0.1, 1.0]
  opacity    : 0.4,  // [0.0, 1.0]
  scale      : 1.0,  // [0.2, 2.0]
  size       : 1.0   // [0.5, 4.0]
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
position: { x: 0.0, y: 0.0 } // Normalized
```

**Options**
```
options: {
  width           : 0.1, // Normalized
  height          : 0.1, // Normalized
  size            : 1.0, // Multiplier, [0.5, 4.0]
  align           : 'center', // Values: 'left', 'center' or 'right'
  color           : '#FFFFFF',
  background      : false,
  backgroundColor : '#000000'
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
position: { x: 0.0, y: 0.0 } // Normalized
```

**Scale**
```
scale: { x: 0.0, y: 0.0 } // Normalized
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
The `tool_id` is `chromaKey`. It'll be computed on each clip created. Options should be set according to the scene, so if it remains similar during a game, maybe you want to adapt these values from a sample clip in Metrica Play and use them in all chroma-key events. Otherwise, you should not pass any option, use default values and fit them in each clip if needed. 

Since the order in which visualizaitons added declared in the event is preserved when they are imported in play, the Chroma-key tool should be added in the specific desired position. For example, if you want to add shape in the field and an arrow, but chroma key only to have an effect on the shape on the field, the order in the event should be: shape - chroma key - arrow.

**Options**
```
options: {
  threshold : 0.01, // [0.0, 1.0]
  smoothing : 0.1   // [0.0, 1.0]
}
```