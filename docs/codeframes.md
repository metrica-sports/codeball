# What's a codeframe?

Codeframes are subclasses of Pandas DataFrames. They have all the methods of a 
standar DataFrame, but have additional methods and attributes that make it easier
to work, filter, and handle data from the game. The base class is `BaseDataFrame`, and
the main codeframes classes are `TrackingDataFrame` and `EventsDataFrame`. An important
aspect of codeframes, as it is the case for DataFrames, is that methods are chainable.

## BaseDataFrame

### Attributes / properties

All codeframes could have 3 attributes:

* records: this holds the records from the datesets created by Kloppy when reading in the
data. This attribute is not passed to the result of any action that modifies the data frame.
* metadata: this holds the metadata from the datasets created by Kloppy when reading in 
the data. This attribute is preserved when filtering or modifiying the data frame. 
However is lost if the result is a series. 
* data_type: this indicates what type of data the data frame holds. For example 
`DataType.TRACKING` or `DataType.EVENT`

### Methods

* ***get_team_by_id***
* ***get_period_by_id***
* ***get_other_team_id***

## TrackingDataFrame

A CodeFrame that holds tracking data.

### Methods

* ***team()***: `TrackingDataFrame.team(team_id)` will return a TrackingDataFrame only 
containing the columns that have data for team with id team_id.
* ***dimension()***: `TrackingDataFrame.dmension('x')` will return a TrackingDataFrame only 
containing the columns with data on the x axis. 
* ***players()***: `TrackingDataFrame.players('field')` will return a TrackingDataFrame only 
containing the columns with data for the field players (excluding goalkeeper). 
`TrackingDataFrame.playes()` will return a TrackingDataFrame containing the data for all players
but drop all the other columns. 
* ***phase()***: `TrackingDataFrame.phase(defending_team=team_id)` will return a Series
with True on the frames the team with id `team_id` was defending and False otherwise.
* ***stretched()***: `TrackingDataFrame.stretched(50)` will return a Series
with True on the frames the streteched of the values in the columns of the TrackingDataFrame
is higher than the threshold. 

Since all these methods are chainable, is you want to get the x coordinates of field players
for team with id `team_id`, you can do: 
```python
TrckingDataFrame.team(team_id).players(field).dimension('x')
```

## EventsDataFrame

A CodeFrame that holds event data.

### Methods

* ***type()***: This allows to filter by the`type` column. `EventsDataFrame.type('PASS')`
will return a EventsDataFrame only containing the rows that correspond to `PASS` type events.
* ***result()***: This allows to filter by the`result` column. `EventsDataFrame.result('COMPLETE')`
will return a EventsDataFrame only containing the events with result `COMPLETE`
* ***into()***, ***starts_inside()***, ***starts_outside()***, ***ends_inside()***,
***ends_outside()***: are all similar. They take a `Zone`, which is a list of boxes, and 
filter events depending on whether they start, end, etc in that `Zone`. Zones will be able
to be defined by the user, or use any of the ones defined in the package (link to Tactical)
module to be added later to the documentation.

These methods are also chainable, so if you wanted to filter by completed passes into the
opponents box you can do: 
```python
EventsDataFrame.type("PASS").into(Zone.OPPONENT_BOX).result("COMPLETE")
```
