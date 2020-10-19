As an example, the below code defines a pattern that will look for all passes into the opponents box. Moreover to be imported into Metrica Play, it will add an arrow and a 2s pause in the video at the moment of the pass, and will add an arrow to the 2D field indicating start and end position of the pass. 

```python
class PassesIntoTheBox(Pattern):
    def __init__(
        self,
        game_dataset: GameDataset,
        name: str,
        code: str,
        in_time: int = 0,
        out_time: int = 0,
        parameters: dict = None,
    ):
        super().__init__(
            name, code, in_time, out_time, parameters, game_dataset
        )

    def run(self) -> List[PatternEvent]:

        passes_into_the_box = (
            self.game_dataset.events.type("PASS")
            .into(Zones.OPPONENT_BOX)
            .result("COMPLETE")
        )

        return [
            self.build_pattern_event(event_row)
            for i, event_row in passes_into_the_box.iterrows()
        ]

    def build_pattern_event(self, event_row) -> PatternEvent:
        pattern_event = self.from_event(event_row)
        pattern_event.add_arrow(event_row)
        pattern_event.add_pause(pause_time=2000)

        return pattern_event
```

With this configuration:

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

Produces this output when imported into Metrica Play:

<p align="center">
  <img src="../../media/passes_into_the_box.gif" width="80%" />
</p>