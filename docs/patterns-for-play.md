# Patterns and events format for Metrica Play
This documentation describes the API to import into import events with annotaitons associated to them into Metrica Play. We refer to this type of events as `patterns`. Patterns are imported into metrica play via a `json` file with a `.patt` extension. Below an explanation of how this file sould be formatted. This documentation is compatible **Metrica Play 2.1.2** onwards.

## Format

The patterns files is in JSON format. It has to main entry points: `events` and `insert`

The **events** entry is an array containing all the events you detect for each game. Those events are going to be stored and associated to the game you are uploading them to.

The **insert** entry is an object that will contain a declaration of `patterns` , `tags` and `tag_groups` you want to create. **It's important to notice that this will be created and store in the database and will be shared among all you games.**

You don't need to create all the patterns, tags and groups each time. If you want to add them to all of your files, that's not a problem. As long the unique code you added to any of them is already in the database there will be no duplicates.

You can use the **insert** field for updating your patterns, tags and tag_groups. More on that in the Patterns, Tags and Tag Groups sections.

```
{
  "events": [
    // Here you'll list al events you want to create
  ],
  "insert": {
    "patterns": [
      // By listing patterns here you'll be able to create
      // and update patterns
    ],
    "tag_groups": [
      // By listing tag groups here you'll be able to create
      // and update tag groups
    ],
    "tags": [
      // By listing tags here you'll be able to create
      // and update tags
    ]
  }
}
```

## Prefix

Every time you want to create something in our database, like a Pattern, Tag Group or Tag you'll need to add a code to it. You can manage your codes any way you like as long you create unique codes for each resource. We'll provide you wit a **prefix** you'll need to add to your codes. If a resource you want to create doesn't have the appropriate prefix it will be omitted. Let's say you want to create some patterns and your prefix is **RCNG.** You could do something like RCNG_001 and RCNG_002 or RCNG_COUNTER and RCNG_POSESSION. It's up to you how you manage codes, but the prefix is mandatory.

## Patterns

We call Pattern to a type of detection. Let's say you create an algorithm for detecting Counter-attacks. You'll create a Pattern called Counter-Attacks and each Counter-attack you detect will be an event associated to this Pattern.

A Pattern needs to have a unique code and a name, that's it. If a code already exists on the database it would not create the pattern again it will update the name to what's written in the current file. It's important to remember that Patterns are shared by all your games, so updating the name will have an effect on previous and future games.

```
"patterns": [
    {
        "name": "Counter Attack",
        "code": "RCNG_001"
    },
    {
        "name": "Defensive Positioning",
        "code": "RCNG_002"
    }
 ],
```

This is how patterns will be listed in Metrica Play for each game:

![image.png](https://storage.googleapis.com/slite-api-files-production/files/e161fbb9-ed22-4329-98f7-5a8d0c0b2285/image.png)

## Tags and Tag Groups

For any given Pattern you create, most likely you'll want to create some Tags and Tag Groups as well. Let's say you have your Counter Attacks pattern and you want to be able to filter by "Fast" and "Slow", or "Successful" and "Failed". For that you can create Tags. And those Tags can be grouped. For example, "Fast" and "Slow" could be two tags on the group "Counter Speed".

For creating a Tag Group you only need to add a unique code and a name.

For creating a Tag you'll need to add a unique code, a name and the code of the group the tags belongs to.

```
"tag_groups": [
    {
        "name": "Counter Speed",
        "code": "RCNG_GROUP_001"
    },
    {
        "name": "Counter Quality",
        "code": "RCNG_GROUP_002"
    }
 ],
 "tags": [
    {
        "name": "Fast",
        "code": "RCNG_TAG_001",
        "group": "RCNG_GROUP_001"
    },
    {
        "name": "Slow",
        "code": "RCNG_TAG_002",
        "group": "RCNG_GROUP_001"
    }
 ],
```

You'll see Tags organised by groups in the filter section when a Pattern is selected

![image.png](https://storage.googleapis.com/slite-api-files-production/files/967dd7e4-6d86-4a07-9acc-3df7ba14438c/image.png)

Once you create a Tag Group, and associate a Tag with it, the tag associated to a group will always be organised based no that group.

An important point. Players and Team codes, for example **ESPBCN** or **P030** can be used as tags directly. So no need to create tags for teams and players. Just use them as any other tags you have created. 

## Creating and updating

This information about patterns, tags and tag groups, can be included every time the json is uploaded. However they are only needed when you want to create one of them, or when you want to update on of them (e.g. change name).  


# Events

On event is one detection of a Pattern. Events happen at a given time in the video and have a duration and many other properties. An Events belongs to a Pattern and has Tags associated to it. This is how, when you select a Pattern you will see a list with all the Events belonging to that Pattern. And when you select an event you will see a list with all the tags added to that Event. This is how you construct events. There are three main categories of concepts. 1) One is the information about the event itself. 2) Another is the information about the annotations. 3) The last one is the tags and team information for filtering in Metrica Play. 

An example event with annotations looks like this:

```
{
  "pattern": RCNG_PATTERN_001,
  "start_time": 5000,
  "event_time": 10000,
  "end_time": 25000,
  "coordinates": [
    [0.39,0.51],
    [0.44,0.42]
  ],
  "visualizations": {
    "start_time": 7000,
    "end_time": 23000,
    "players": "P030",
    "tool_id": "players",
    "options": {
      "speed": 1
    }
  },
  "tags": [
    "ESPBCN",
    "P030",
    "RCGN_TAG_001",
    "RCGN_TAG_007"
  ],
  "team": "ESPBCN"
}
```

This is an example of a sprint type event wihch has a `speed` visualization. 

This is an event that belongs to the `pattern` code  `RCNG_PATTERN_001`, that starts at time `5000` and ends at time `25000`, with the event indicator being located at `10000` in the timeline of the video. All times are in miliseconds. 

In this case, in Metrica Play the event will be located at time `10000` in the timeline that , but when you select it, the video will play from time `5000` to `25000`. 

Moreover, this event has coordiantes. There are two options for coordiantes. If you proivde just a pair of xy coordiantes, it will show a dot on the 2D field in Metrica Play. If you provide two pairs, it will show an arrow. In this case it will show an arrow in the 2D field (NOT in the video) going from `[0.39, 0.51]` to `[0.44, 0.42]`.

This event also has a annotation. In this case, the speed will show up for this player from time `7000` to `23000` for player `P030`. To code for that, the `tool_id` is set to `players` type visualization that has `speed` as `1` (true).

Finally, this event has the tags `"ESPBCN","P030",RCGN_TAG_001,RCGN_TAG_007` and belongs to the team `ESPBCN`.

Below a summary of the information about fields related events and fields related to annotations. 

## Fields common to all events

```
{
  "pattern": 15, // Pattern code
  "start_time": 5000, // Number in miliseconds
  "event_time": 10000, // Number in miliseconds 
  "end_time": 25000, // Number in miliseconds
  "coordinates": [ // In normalized coordinates. `null` if empty.
    [0.39,0.51],
    [0.44,0.42]
  ]
  "visualizations":[...], // See below. `null` if empty.
  "tags": [ // Codes of the tags. `[]` if empty. 
    "ESPBCN",
    "P030"
  ],
  "team": "ESPBCN" // `null` if empty.
}
```


## Fields common to all visualizations

The following attributes have to be defined for each tool. Annotations' order matters, they will be created and displayed in the same order they are declared, first annotation will be rendered at the bottom/background.
```
{
  start_time : 1040, // Milliseconds
  end_time   : 2130, // Milliseconds
  tool_id    : 'players', // The ID of the tool
  ... // Each tool could have other mandatory attributes (players, team, points, etc.)
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