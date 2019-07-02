"""Calculates the amount that each flatmate must pay of the total cost of the
house.

This number is calculated based on square feet owned. Every flatmate pays for
a portion of common areas.
"""

# The number of people living in the house
flatmate_count = 4

# The total square feet of the house. Note that this is the number reported in
# the house's listing. We're assuming that it does not include outside areas
# like the patio and balcony, but we haven't confirmed that.
total_sqft = 1882

# The total cost of rent for the house per month
total_cost = 4900

# The square footage of each person's bedroom. "Thiele" is Alex and Bethany's
# cute couple name.
_master_bed_bath = 286.2
_master_bedroom = 177.67
_master_bathroom = _master_bed_bath - _master_bedroom
unused_sqft = _master_bedroom
burgle_sqft = 114.7 + _master_bathroom
_hall_bathroom = 36.56
max_sqft = 106.9 + _hall_bathroom
tyler_sqft = 170.5

# The square foot of the common area, which is any area that is not a person's
# bedroom.
common_sqft = total_sqft - burgle_sqft - max_sqft - tyler_sqft

cost_per_sqft = total_cost / total_sqft

# The total cost of the common area
common_cost = common_sqft * cost_per_sqft

# The cost of each individual bedroom
burgle_room_cost = burgle_sqft * cost_per_sqft
max_room_cost = max_sqft * cost_per_sqft
tyler_room_cost = tyler_sqft * cost_per_sqft

# The cost that each person pays. This is calculated by splitting up the common
# area cost equally and adding each individual's room cost. Alex and Bethany
# are a special case because they share a room and each pay half.
bryce_cost = (common_cost / flatmate_count) + (burgle_room_cost / 2)
kylee_cost = (common_cost / flatmate_count) + (burgle_room_cost / 2)
max_cost = (common_cost / flatmate_count) + max_room_cost
tyler_cost = (common_cost / flatmate_count) + tyler_room_cost

print("Bryce:", bryce_cost)
print("Kylee:", kylee_cost)
print("Max:", max_cost)
print("Tyler:", tyler_cost)

print("\nSum:", bryce_cost + kylee_cost + max_cost + tyler_cost)
