# codeball: data driven tactical and video analysis of football/soccer games

[![PyPI Latest Release](https://img.shields.io/pypi/v/codeball.svg)](https://pypi.org/project/codeball/)
![](https://img.shields.io/github/license/metrica-sports/codeball)
![](https://img.shields.io/pypi/pyversions/codeball)
[![Powered by Metrica Sports](https://img.shields.io/badge/Powered%20by-Metrica%20Sports-green)](https://metrica-sports.com/)
--------

## Why codeball

While there are several pieces of code / repositories around that provide different tools and bits of codes to do tactical analysis of individual games, there is no centralized place in which they live. Morevoer, most of the analysis done is usually not linked or easy to link with the actual footage of the match. Codeball's objective is to change that by:

1. Building a central repository for different types of data driven tactical analysis methods / tools.
2. Making it easy to link those analysis with a video of the game. 

## What can you do with it

The main types of work / development you can do with codeball are:

#### Work with tracking and event data

- Codeball creates subclasses of *Pandas DataFrames* for events and tracking data; and provides you with handy methods to work with the data.
- Work with or create your own tactical models like *Zones* so that you can for example do `game_dataset.events.into(Zone.OPPONENT_BOX)` and it will return a DataFrame only with the events into the opponents box. You can also chain methods, like `game_dataset.events.type("PASS").into(Zone.OPPONENT_BOX)` and will return only passes into the box.
- Easily access tactical tools or methods like computing passes networks, pitch control,EPV models, etc (Not yet implemented, WIP)

#### Create Patterns to analyze the game

- Analyze games based on Patterns. A Pattern is a unit of analysis that looks for moments in the game in which a certain thing happens. That certain thing is defined inside the Pattern, but codeball provides tools to easily create them, configure them and export them in different formats for different platforms.
- You can create your own patterns, or also use the ones provided with the package and configure them to your liking.

#### Add annotations to the events for Metrica Play

- Codeball incorporates all the annotations models and API information needed to import events with annotations into Metrica Play. - You can add directly from the code any visualization available in Metrica Play  (spotlights, rings, future trail, areas, drawings, text, etc) to any event.

## Supported Data Providers

This package is very much WIP. At the moment it only works based on Metrica Sports Elite datasets. However, it uses Kloppy to read in the data so that in the near future will support data from any provider.

## Trying it out

There are no open source Elite datasets at the moment that work with this package. However if you are interested in testing it out and developing your own patterns and/or test them in Metrica Play reach out to bruno@metrica-sports.com or @brunodagnino on Twitter.

## Install it / contribute

While created and maintained by Metrica Sports, it's distributed under an MIT license and it welcomes contributions from members of the community, clubs and other companies.

The source code is currently hosted on GitHub at: https://github.com/metrica-sports/codeball

Installers for the latest released version are available at the [Python package index](https://pypi.org/project/codeball).

```sh
pip install codeball
```

## Documentation

There is no oficial documentation yet, but it's coming :)
