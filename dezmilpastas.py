import pathlib


for i in range(10000):
    pathlib.Path(f'{i}/').mkdir()
    with open(f'./{i}/helloworld.txt', 'w') as helloworld:
        helloworld.write(f'OLÁ MUNDO {i}')
