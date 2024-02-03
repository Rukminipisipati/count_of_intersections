# Create tuples that represents chords with start and end points, and a flag indicating the type. True as start & False as end.
# Sort the chords based on their positions, using the start points as the key.
# Iterate through the sorted chords, maintaining a set of active chords.
# For each start point, check for intersections with active end points.
# Track the count of intersections and add the chord to the set of active chords.
# For each end point, remove the corresponding start point from the set of active chords.
# Big O-run time:
  # Creating and sorting the chords: O(n * log(n))
  # Iterating through the chords and checking intersections: O(n)
