
#set
    # unordered collection of uniquie, immutable objects
    # delimited by { and }
    # single comma separated items,
    # empty {} makes a dict, so for empty set use the set() constructor
    # constructure accepts:
        # iterable series of values
        # dublicates are discarded
        # often used specifically to remove dublicates - not order preserving
    # Order is arbitrary
    # Membership / Containment
        # Fundamentail operation for sets
        # Use 'in' and 'not in' operators
    # adding => add(item) inserts a single element
    # duplicates are silently ignored
    # for multiple elements use update(items) passing any iterable series
    # removing => remove(item) requires that item is present, otherwise raises KeyError
    # discard(item) always succeeds
    # coping => 
        # s.copy() method
        # Use contructor: set(s)
        # Copies are shallow!
    # Union => 
        # s.union(t) method
        # commutative
    # Intersection =>
        # s.intersection(t)
        # commutative
    # Difference =>
        # s.difference(t) method
        # non-commutative
    # Symetric Difference =>
        # s.simetric_difference(t)
        # commutative
    # Set 
        # Subset => s.issubset(t) method
        # Superset => s.issuperset(t) method
        # Disjoin => s.isdisjoint(t) method




blue_eyes = { 'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia' }
blond_hair = { 'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua' }
smell_hcn = { 'Harry', 'Amelia' }
taste_ptc = { 'Harry', 'Lily', 'Amelia', 'Lola' }
o_blood = { 'Mia', 'Joshua', 'Lily', 'Olivia' }
b_blood = { 'Amelia', 'Jack' }
a_blood = { 'Harry' }
ab_blood = { 'Joshua', 'Lola' }


print(blue_eyes.union(blond_hair)) # {'Olivia', 'Harry', 'Amelia', 'Mia', 'Joshua', 'Jack', 'Lily'}

print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes)) # True

print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes)) # True

print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair)) # False

print(blond_hair.symmetric_difference(blue_eyes)) # {'Lily', 'Mia', 'Olivia', 'Joshua'}

print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair)) # True

print(smell_hcn.issubset(blond_hair)) # True

print(taste_ptc.issuperset(smell_hcn)) # True

print(a_blood.isdisjoint(o_blood)) # True