"""Calculates the amount that each flatmate must pay of the total cost of the
house.

This number is calculated based on square feet owned. Every flatmate pays for
a portion of common areas.
"""

# The number of people living in the house
flatmate_count = 5

# The total square feet of the house. Note that this is the number reported in
# the house's listing. We're assuming that it does not include outside areas
# like the patio and balcony, but we haven't confirmed that.
total_sqft = 1882

# The total cost of rent for the house per month
total_cost = 4900

# The square footage of each person's bedroom. "Thiele" is Alex and Bethany's
# cute couple name.
thiele_sqft = 286.2
beagle_sqft = 114.7
max_sqft = 106.9
tyler_sqft = 170.5

# The square foot of the common area, which is any area that is not a person's
# bedroom.
common_sqft = total_sqft - thiele_sqft - beagle_sqft - max_sqft - tyler_sqft

cost_per_sqft = total_cost / total_sqft

# The total cost of the common area
common_cost = common_sqft * cost_per_sqft

# The cost of each individual bedroom
thiele_room_cost = thiele_sqft * cost_per_sqft
beagle_room_cost = beagle_sqft * cost_per_sqft
max_room_cost = max_sqft * cost_per_sqft
tyler_room_cost = tyler_sqft * cost_per_sqft

# The cost that each person pays. This is calculated by splitting up the common
# area cost equally and adding each individual's room cost. Alex and Bethany
# are a special case because they share a room and each pay half.
alex_cost = (common_cost / flatmate_count) + (thiele_room_cost / 2)
bethany_cost = (common_cost / flatmate_count) + (thiele_room_cost / 2)
beagle_cost = (common_cost / flatmate_count) + beagle_room_cost
max_cost = (common_cost / flatmate_count) + max_room_cost
tyler_cost = (common_cost / flatmate_count) + tyler_room_cost

print("Alex:", alex_cost)
print("Bethany:", bethany_cost)
print("Beagle:", beagle_cost)
print("Max:", max_cost)
print("Tyler:", tyler_cost)

print("\nSum:", alex_cost + bethany_cost + beagle_cost + max_cost + tyler_cost)
