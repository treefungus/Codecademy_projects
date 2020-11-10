# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damage(damages):
    damages_updated = []
    convert = {"M":1000000, "B":1000000000}
    for damage in damages:
        if "not recorded" in damage:
            damages_updated.append(damage)
        for key in convert.keys():
            if key in damage:
                damages_updated.append(float(damage[:-1])*convert[key])
    return damages_updated

updated_damages = update_damage(damages)
print(updated_damages)

# write your construct hurricane dictionary function here:
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths):
    dict = {}
    for i in range(len(names)):
        dict[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds [i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
    return dict

hurricanes = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricanes)
# write your construct hurricane by year dictionary function here:
def group_by_year():
  by_years = {}
  for storm in hurricanes:
    year = hurricanes[storm]['Year']
    storm = hurricanes[storm]
    if year not in by_years:
      by_years[year] = [storm]
    else:
      by_years[year].append(storm)
  return by_years

print(group_by_year()[1932])

# write your count affected areas function here:
def count_affected_areas(given_area):
  new_dict = {}
  for storm in hurricanes:
    for area in hurricanes[storm]["Areas Affected"]:
      if area == given_area:
        if area not in new_dict.keys():
          new_dict[area] = 1
        else:
          new_dict.update({area: new_dict[area] + 1})
  return new_dict

print(count_affected_areas("Cuba"))
# write your find most affected area function here:
hit_areas_dict = {}
for storm in hurricanes:
  for area in hurricanes[storm]["Areas Affected"]:
    hit_areas_dict.update(count_affected_areas(area))

print(hit_areas_dict)
def most_affected_area(dictionary):
  most_hit = max(dictionary, key=dictionary.get)
  number = dictionary[most_hit]
  return most_hit, number

print(most_affected_area(hit_areas_dict))
# write your greatest number of deaths function here:
def by_mortality_scale(hurricanes):
  new_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
  for storm in hurricanes:
    if hurricanes[storm]["Deaths"] < 100:
      new_dict[0].append(storm)
    elif hurricanes[storm]["Deaths"] < 500:
      new_dict[1].append(storm)
    elif hurricanes[storm]["Deaths"] < 1000:
      new_dict[2].append(storm)
    elif hurricanes[storm]["Deaths"] < 10000:
      new_dict[3].append(storm)
    else:
      print(f"{storm} out of scale!")
  return new_dict

by_mortality = by_mortality_scale(hurricanes)
print(by_mortality)

# write your greatest damage function here:

def find_damage(hurricanes):
  max_damage = 0
  the_storm = 'default'
  for storm in hurricanes:
    if type(hurricanes[storm]["Damage"]) == str:
      continue
    elif hurricanes[storm]["Damage"] > max_damage:
      max_damage = hurricanes[storm]["Damage"]
      the_storm = f"{storm}:"
  
  print(the_storm, max_damage)
  return the_storm, max_damage

x, y = find_damage(hurricanes)
  
# write your catgeorize by damage function here:
def by_damage_scale(hurricanes):
  new_dict = {0: [], 1: [], 2: [], 3: [], 4: []}
  for storm in hurricanes:
    if type(hurricanes[storm]["Damage"]) == str:
      continue
    elif hurricanes[storm]["Damage"] < 100000000:
      new_dict[0].append(storm)
    elif hurricanes[storm]["Damage"] < 1000000000:
      new_dict[1].append(storm)
    elif hurricanes[storm]["Damage"] < 10000000000:
      new_dict[2].append(storm)
    elif hurricanes[storm]["Damage"] < 50000000000:
      new_dict[3].append(storm)
    else:
      print(f"{storm} out of scale!")
  return new_dict

by_damage = by_damage_scale(hurricanes)
print(by_damage)
