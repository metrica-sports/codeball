# What's a CodeballFrame?

CodeballFrames are subclasses of Pandas DataFrames. They have all the methods of a 
standard DataFrame, but have additional methods and attributes that make it easier
to work, filter, and handle data from the game. The base class is `BaseFrame`, and
the main CodeballFrame classes are `TrackingFrame` and `EventsFrame`. An important
aspect of CodeballFrame, as it is the case for DataFrames, is that methods can be chained.

## BaseFrame

### Attributes / properties

All CodeballFrame have 3 attributes:

* records: this holds the records from the datasets created by Kloppy when reading in the
data. This attribute is not passed to the result of any action that modifies the data frame.
* metadata: this holds the metadata from the datasets created by Kloppy when reading in 
the data. This attribute is preserved when filtering or modifying the data frame. 
However is lost if the result is a series. 
* data_type: this indicates what type of data the data frame holds. For example 
`DataType.TRACKING` or `DataType.EVENT`

### Methods

* ***get_team_by_id***
* ***get_period_by_id***
* ***get_other_team_id***

## TrackingFrame

A CodeballFrame that holds tracking data.

### Methods

* ***team()***: `TrackingFrame.team(team_id)` will return a TrackingFrame only 
containing the columns that have data for team with id team_id.
* ***dimension()***: `TrackingFrame.dimension('x')` will return a TrackingFrame only 
containing the columns with data on the x axis. 
* ***players()***: `TrackingFrame.players('field')` will return a TrackingFrame only 
containing the columns with data for the field players (excluding goalkeeper). 
`TrackingFrame.players()` will return a TrackingFrame containing the data for all players
but drop all the other columns. 
* ***phase()***: `TrackingFrame.phase(defending_team=team_id)` will return a Series
with True on the frames the team with id `team_id` was defending and False otherwise.
* ***stretched()***: `TrackingFrame.stretched(50)` will return a Series
with True on the frames the stretched of the values in the columns of the TrackingFrame
is higher than the threshold. 

Since all these methods can be chained, is you want to get the x coordinates of field players
for team with id `team_id`, you can do: 
```python
TrackingDataFrame.team(team_id).players(field).dimension('x')
```

## EventsFrame

A CodeballFrame that holds event data.

### Methods

* ***type()***: This allows to filter by the`type` column. `EventsFrame.type('PASS')`
will return a EventsFrame only containing the rows that correspond to `PASS` type events.
* ***result()***: This allows to filter by the`result` column. `EventsFrame.result('COMPLETE')`
will return a EventsFrame only containing the events with result `COMPLETE`
* ***into()***, ***starts_inside()***, ***starts_outside()***, ***ends_inside()***,
***ends_outside()***: are all similar. They take one or more `Zones` or `Area`(see the [tactical](../tactical) section) and 
filter events depending on whether they start, end, etc in that `Zones`. Zones will be able
to be defined by the user, or use any of the ones defined in the package (link to Tactical)
module to be added later to the documentation.

These methods can also be chained, so if you wanted to filter by completed passes into the
opponents box you can do: 
```python
EventsFrame.type("PASS").into(Zones.OPPONENT_BOX).result("COMPLETE")
```

## CodesFrame

A CodeballFrame that holds codes from an xml file.

The columns present on this CodeballFrame will depend on how your XML is format, but as a general rule you'll
see one row per `code`, with columns for the `code_id`, `timestamp`, `end_timestamp`, `code` (name) and then one column for each tag. 