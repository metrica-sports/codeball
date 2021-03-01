# codeball: data driven tactical and video analysis of soccer games

[![PyPI Latest Release](https://img.shields.io/pypi/v/codeball.svg)](https://pypi.org/project/codeball/)
[![Downloads](https://pepy.tech/badge/codeball)](https://pepy.tech/project/codeball)
![](https://img.shields.io/github/license/metrica-sports/codeball)
![](https://img.shields.io/pypi/pyversions/codeball)
[![Powered by Metrica Sports](https://img.shields.io/badge/Powered%20by-Metrica%20Sports-green)](https://metrica-sports.com/)
--------

## Why codeball?

While there are several pieces of code / repositories around that provide different tools and bits of codes to do tactical analysis of individual games, there is no centralized place in which they live. Moreover, most of the analysis done is usually not linked or easy to link with the actual footage of the match. Codeball's objective is to change that by:

1. Building a central repository for different types of data driven tactical analysis methods / tools.
2. Making it easy to link those analyses with a video of the game in different formats.

## What can you do with it

The main types of work / development you can do with codeball are:

#### Work with tracking and event data

- Codeball creates subclasses of *Pandas DataFrames* for events and tracking data; and provides you with handy methods to work with the data.
- Work with or create your own tactical models like *Zones* so that you can for example do `game_dataset.events.into(Zones.OPPONENT_BOX)` and it will return a DataFrame only with the events into the opponents box. You can also chain methods, like `game_dataset.events.type("PASS").into(Zones.OPPONENT_BOX)` and will return only passes into the box. Or for example do `game_dataset.tracking.team('FIFATMA').players('field').dimension('x')` to get the x coordinate of the field players (no goalkeeper data) for team with id FIFATMA.
- [Not yet implemented] Easily access tactical tools or methods like computing passes networks, pitch control,EPV models, etc 

#### Create Patterns to analyze the game

- Analyze games based on Patterns. A Pattern is a unit of analysis that looks for moments in the game in which a certain thing happens. That certain thing is defined inside the Pattern, but codeball provides tools to easily create them, configure them and export them in different formats for different platforms.
- You can create your own patterns, or also use the ones provided with the package and configure them to your liking.

#### Add annotations to the events for Metrica Play

- Codeball incorporates all the annotations models and API information needed to import events with annotations into Metrica Play. 
- You can add directly from the code any visualization available in Metrica Play  (spotlights, rings, future trail, areas, drawings, text, etc) to any event.

## Example

You can use any of the above functionality independently. However they are most powerful when combined. As an example, the below code defines a pattern that will look for all passes into the opponent's box. Moreover to be imported into Metrica Play, it will add an arrow and a 2s pause in the video at the moment of the pass, and will add an arrow to the 2D field indicating start and end position of the pass. 

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

The above code produces this output when imported into Metrica Play:

<p align="center">
  <img src="https://media.giphy.com/media/MDxwU6ddqhGiP5M0iM/giphy.gif" width="80%" />
</p>

## Supported Data Providers

This package is very much WIP. At the moment it only works based on Metrica Sports Elite datasets. However, it uses Kloppy to read in the data so that in the near future will support data from any provider.

## Trying it out

There are no open source Elite datasets at the moment that work with this package. However if you are interested in testing it out and/or developing your own patterns and/or test them in Metrica Play reach out to bruno@metrica-sports.com or [@brunodagnino](https://twitter.com/brunodagnino) on Twitter.

## Install it 

Installers for the latest released version are available at the [Python package index](https://pypi.org/project/codeball).

```sh
pip install codeball
```

## Contribute

While created and maintained by Metrica Sports, it's distributed under an MIT license and it welcomes contributions from members of the community, clubs and other companies. You can find the repository on [Github](https://github.com/metrica-sports/codeball). Also, if you have ideas for patterns we should implement, or methods we should include (e.g. pitch control, EPV, similarity search, etc), let us know! You can create an issue on the repo, or reach out to bruno@metrica-sports.com or [@brunodagnino](https://twitter.com/brunodagnino) on Twitter.

## Documentation

Check the [documentation](https://codeball.metrica-sports.com) for a more detailed explanation of this package.

## Tentative TODO

This is a very incomplete list of the things we have in mind, and it will probably change as we get input from the community / users. However it gives you a rough idea of the direction in which we want to go with this project!

* more Zones (half spaces, thirds, 14, etc) - [done]
* crete types for players, events, etc to filter the data.
* more ways to filter event and tracking data (e.g pass length)
* more patterns (currently 4 in the making)
* pitch control from `game_dataset.pitch_control([frame/s])`, same with EPV.
* easily query xG, g+, xT, etc for events
* corner strategy classifier.
* support for other providers, likely StatsBomb next.
* export events in xml format
* methods to easily sync tracking and event from different providers.
* any suggestions?