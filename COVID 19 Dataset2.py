"""Small script that tracks a date range and prints start/end in ISO format.

Dates are stored as integers in yyyymmdd form (e.g. 20250913). The helper
`yyyymmdd_to_iso` below converts those into the human-readable ISO form
yyyy-mm-dd without importing any modules.
"""

# Define dataset as "date_range"
date_range = range(20200122, 20201207)


def yyyymmdd_to_iso(value):
	# Returns None for None/empty. Raises ValueError for values that are not exactly 8 digits.
	if value is None:
		return None
	s = str(value)
	if s == "":
		return None
	if len(s) != 8 or not s.isdigit():
		raise ValueError(f"expected 8-digit yyyymmdd, got {value!r}")
	return s[0:4] + "-" + s[4:6] + "-" + s[6:8]


# Print the date range :)
end_date_int = max(date_range)
start_date_int = min(date_range)

start_date = yyyymmdd_to_iso(start_date_int)
end_date = yyyymmdd_to_iso(end_date_int)

print("Start date:", start_date)
print("End date:", end_date)

