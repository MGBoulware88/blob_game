# Playing around with modularization!

This Blob World "game" will let you create blobs and move them around.

Creating an instance of a blob requires passing an x and y boundary argument and each instance can have different boundaries.
Optionally, you can specify their size and the range used for decided their new location when the move() method is called.

You can also set the boundary of the viewable game and choose if you want to allow blobs to move out of bounds (default is no).

The move() method randomly selects an x and y coordinate to move the blob to.
If you pass **check_bounds_before_move()** as the argument, you can check the move keeps the blob inbounds first, then an x and y coordinate to move to instead.

The check_bounds_before_move() method is used to make sure the move is legal (within bounds). 
Pass in False argument **check_bounds(False)** to allow the blob to disappear from the screen.