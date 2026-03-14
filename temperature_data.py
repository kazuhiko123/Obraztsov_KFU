from itertools import accumulate
import numpy as np
import math as m
from functools import reduce

anomaly_count = 0
package_counter = 0
ready_data = []
temperatures = np.random.randint(-20, 40, 10000)
print(temperatures)
it = iter(temperatures)
bug_cleaned_temperatures = []

try:
    while True:
        val = next(it)
        if val > -15 and val < 35:
            bug_cleaned_temperatures.append(val)
except StopIteration:
    print("Температурные данные очищены от ошибочных")


def normalised_temperature_data(bug_cleaned_temperatures):
    std_val = np.std(bug_cleaned_temperatures)
    mean_val = np.mean(bug_cleaned_temperatures)
    normalised_temperature = []
    for x in bug_cleaned_temperatures:
        normalized = (x - mean_val) / std_val
        normalised_temperature.append(normalized)
    for i in normalised_temperature:
        ready_val = m.sin(i) + i**2
        ready_data.append(ready_val)

normalised_temperature_data(bug_cleaned_temperatures)

def group_by_packages(ready_data, package_size=30):
    package = []
    for item in ready_data:
        package.append(item)
        if len(package) == package_size:
            yield package
            package = []
    if package:
        yield package

packages_stats =[]
package_means = []

'''Анализатор пакетов данных'''
for package in group_by_packages(ready_data, 30):
    package_counter += 1
    average_temperature = np.mean(package)
    median = np.median(package)
    std_temperature = np.std(package)
    min_temperature = min(package)
    max_temperature = max(package)

    packages_stats.append({
        'number': package_counter,
        'mean': average_temperature,
        'std': std_temperature,
        'min': min_temperature,
        'max': max_temperature

    })
    package_means.append(average_temperature)

initial_stats = (0, 0.0, float('-inf'))

def calculate_stats(acc, package):
    anomaly_count, sum_means, max_mean = acc
    is_anomaly = abs(package['mean']) > 1 or package['std'] > 1
    if is_anomaly:
        anomaly_count += 1
    sum_means += package['mean']
    if package['mean'] > max_mean:
        max_mean = package['mean']
    return (anomaly_count, sum_means, max_mean)

anomaly_count, sum_of_means, max_mean = reduce(calculate_stats, packages_stats, initial_stats)

print(f"Всего пакетов: {package_counter}")
print(f"Аномальных пакетов данных: {anomaly_count}")
print(f"Максимальное среднее значение: {max_mean:.4f}")
print(f"Сумма средних значений: {sum_of_means:.4f}")