## Configuration

All the patterns below, are available included in Codeball and ready to be used. They have a default configuration included with the package, but you can create your own config file if you want to change for example, the name of the patterns, the in and out time, or the parameters the use to compute events. The configuration for a pattern looks like the below. For more details check the example pattern in the Examples section. 

```json
{
    "include": true,
    "name": "Passes into the box",
    "code": "MET_003",
    "pattern_class": "PassesIntoTheBox",
    "parameters": null,
    "in_time": 2,
    "out_time": 2
}
```

****

## Available patterns

### TeamStretched

This pattern looks for moments in which the team is stretched horizontally while defending for more than 5 seconds. It returns those moments with a TeamSize length visualization for the duration of the infringement. This pattern doesn't add anything on the 2D field. 

Parameters:  

* team: str -> Code of the team you want to analyze  
* threshold: float -> What is the stretch threshold in meters  

In this example the threshold is at 35 meters.

<p align="center">
  <img src="../media/team_stretched.gif" width="80%" />
</p>

****

### SetPieces

This pattern return set Pieces include: kick offs, throw ins, corner kicks penalties, free kicks. Beside indicating the moment of the game in which they tke place, it adds a spotlight on the player tacking the set piece. This pattern also adds a dot on the 2D field for each event. 

<p align="center">
  <img src="../media/set_pieces.gif" width="80%" />
</p>

****

### PassesIntoTheBox

This pattern finds completed passes into the opponent box. For each one of those passes, it creates a pattern event that at the moment of the pass makes a 2s pause and draws an arrow on the video showing the pass. This pattern also adds an arrow on the 2D field for each event.

<p align="center">
  <img src="../media/passes_into_the_box.gif" width="80%" />
</p>