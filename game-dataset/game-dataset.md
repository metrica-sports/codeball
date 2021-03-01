# What's a GameDataset?

A GameDataset is a class that serves 2 purposes:

1. Hold CodeballFrames for tracking, event, and other data types
2. Provide methods to enrich those CodeballFrames
3. Provide auxiliary methods to process and handle data that require information from the game_dataset (e.g. frame rate)

## Attributes

* ***tracking***: contains a `TrackingFrame`
* ***events***: contains an `EventsFrame`

## Properties

* ***game_dataset_type***: return an Enum with the type of the dataset, which could be [ONLY_TRACKING, ONLY_EVENTS, FULL_SAME_PROVIDER, FULL_MIXED_PROVIDERS]
* ***metadata***: the metadata of the dataset (unless it's a FULL_MIXED_PROVIDERS type) that comes from loading the data with kloppy. 

## Enrichment methods

There is a main method ***_enrich_data*** that runs all the below:

* ***_build_possessions***
* ***_set_periods_attacking_direction***
* ***_enrich_events***
* ***_enrich_tracking***

## Auxiliar methods
* ***find_interval***: given a Series of bool values computes the intervals of True values. 
* ***frame_to_milliseconds***: given a frame number it returns the value in milliseconds of that moment in the video. 

