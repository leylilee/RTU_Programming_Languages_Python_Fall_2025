"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [10, 11, 12, 9, 8, 11, 9]
city_population = {
    "Riga": 591882,
    "Daugavpils": 78112,
    "Liepaja": 67398,
    "Jelgava": 54821,
    "Jurmala": 51933

}

# TODO: Compute aggregates
average_temperature = sum(temperatures)/len(temperatures)

total_population = 0
largest_city = max(city_population, key=city_population.get)
smallest_city = min(city_population, key=city_population.get)
largest_population = city_population.get(largest_city)
smallest_population = city_population.get(smallest_city)

total_population = sum(city_population.values())

# TODO: Print results
print("Average temperature:", average_temperature)
print("Largest city:", largest_city, "-", largest_population)
print("Smallest city:", smallest_city, "-", smallest_population)
print("Total population:", total_population)
