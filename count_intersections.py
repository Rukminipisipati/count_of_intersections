def count_of_intersections(rad_measures, identifiers):
    chords = []

    for i in range(0, len(identifiers), 2):
        start_index = i
        end_index = i + 1
        chord = (rad_measures[start_index], True, identifiers[start_index])  # True for start point
        chords.append(chord)
        chord = (rad_measures[end_index], False, identifiers[end_index])  # False for end point
        chords.append(chord)

    chords.sort()

    intersections_count = 0
    active_chords = set()

    for chord in chords:
        if chord[1]:  # If it's a start point
            for active_chord in active_chords:
                if active_chord[2][1:] != chord[2][1:] and active_chord[0] < chord[0] < active_chord[1]:
                    intersections_count += 1
            active_chords.add((chord[0], float('inf'), chord[2]))
        else:  # If it's an end point
            active_chords.remove((float('-inf'), chord[0], chord[2]))

    return intersections_count

#Input
rad_measures_1 = [0.78, 1.47, 1.77, 3.92]
identifiers_1 = ["s_1", "s_2", "e_1", "e_2"]
result_1 = count_of_intersections(rad_measures_1, identifiers_1)
print("Input 1 Result:", result_1)

rad_measures_2 = [0.9, 1.3, 1.70, 2.92]
identifiers_2 = ["s1", "e1", "s2", "e2"]
result_2 = count_of_intersections(rad_measures_2, identifiers_2)
print("Input 2 Result:", result_2)
