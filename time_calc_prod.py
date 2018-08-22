import time

# Another way to profile your code is to use the cProfile.run() function.


def calc_prod():
    # Calculate the product (nasobek in Czech) of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


start_time = time.time()
prod = calc_prod()
end_time = time.time()

print(f'The result is {len(str(prod))} digits long.')
print(f'Took {end_time - start_time} seconds to calculate.')
