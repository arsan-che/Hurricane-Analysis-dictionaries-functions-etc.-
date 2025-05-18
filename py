# Data lists for Category 5 hurricanes
# Names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# Months of hurricane occurrences
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# Years of hurricane occurrences
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# Maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# Areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# Damages (USD) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# Deaths caused by each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# Convert damage strings to float values
def convert_damages_data(damages):
    """Convert damages data from string to float and return converted data as a list."""
    conversion = {"M": 1000000, "B": 1000000000}
    updated_damages = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        elif damage.find('M') != -1:
            updated_damages.append(float(damage[:damage.find('M')]) * conversion["M"])
        elif damage.find('B') != -1:
            updated_damages.append(float(damage[:damage.find('B')]) * conversion["B"])
    return updated_damages

# Test damage conversion
updated_damages = convert_damages_data(damages)
# print(updated_damages)

# Create dictionary with hurricane names as keys
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    """Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value."""
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": updated_damages[i],
            "Deaths": deaths[i]
        }
    return hurricanes

# Create hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# print(hurricanes)

# Organize hurricanes by year
def create_year_dictionary(hurricanes):
    """Convert dictionary with hurricane name as key to a new dictionary with year as the key."""
    hurricanes_by_year = {}
    for cane in hurricanes:
        current_year = hurricanes[cane]['Year']
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [hurricanes[cane]]
        else:
            hurricanes_by_year[current_year].append(hurricanes[cane])
    return hurricanes_by_year

# Test year-based dictionary
hurricanes_by_year = create_year_dictionary(hurricanes)
# print(hurricanes_by_year[1932])

# Count occurrences of affected areas
def count_affected_areas(hurricanes):
    """Count hurricanes affecting each area and return a dictionary with area counts."""
    affected_areas_count = {}
    for cane in hurricanes:
        for area in hurricanes[cane]['Areas Affected']:
            affected_areas_count[area] = affected_areas_count.get(area, 0) + 1
    return affected_areas_count

# Test affected areas count
affected_areas_count = count_affected_areas(hurricanes)
# print(affected_areas_count)
# Find the most affected area
def most_affected_area(affected_areas_count):
    """Identify the area affected by the most hurricanes and its count."""
    max_area = 'Central America'
    max_area_count = 0
    for area, count in affected_areas_count.items():
        if count > max_area_count:
            max_area = area
            max_area_count = count
    return max_area, max_area_count

# Test most affected area
max_area, max_area_count = most_affected_area(affected_areas_count)
# print(max_area, max_area_count)
# Find hurricane with highest death toll
def most_deaths_hurricane(hurricanes):
    """Identify the hurricane with the greatest number of deaths and its death toll."""
    max_mortality_cane = 'Cuba I'
    max_mortality = 0
    for cane in hurricanes:
        if hurricanes[cane]['Deaths'] > max_mortality:
            max_mortality_cane = cane
            max_mortality = hurricanes[cane]['Deaths']
    return max_mortality_cane, max_mortality

# Test highest mortality
max_mortality_cane, max_mortality = most_deaths_hurricane(hurricanes)
# print(max_mortality_cane, max_mortality)
