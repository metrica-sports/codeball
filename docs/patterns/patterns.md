## TeamStretched

This pattern looks for moments in which the team is streched horizontally while 
defending for more than 5 seconds. It returns those moments with a TeamSize length 
visualization for the duration of the infringement. This pattern doesn't add anything
on the 2D field. 

Parameters:  

* team: str -> Code of the team you want to analyze  
* threshold: float -> What is the stretch threshold in meters  

<p align="center">
  <img src="../test.gif" width="75%" />
</p>

****

## SetPieces

This pattern return set Pieces include: kick offs, throw ins, corner kicks penalties, 
free kicks. Beside indicating the moment of the game in which they tke place, it adds a 
spotlight on the player tacking the set piece. This pattern also adds a dot on the 2D
field for each event. 

<p align="center">
  <img src="../test.png" width="75%" />
</p>

****

## PassesIntoTheBox

This pattern finds completed passes into the opponent box. For each one of those passes, 
it creates a pattern event that at the moment of the pass makes a 2s pause and draws an 
arrow on the video showing the pass. This pattern also adds an arrow on the 2D field
for each event.

<p float="left">
  <img src="../test.gif" width="45%" />
  <img src="../test.png" width="45%" />
</p>