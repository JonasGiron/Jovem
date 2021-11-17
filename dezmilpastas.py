import pathlib
import os


for i in pathlib.Path('./').iterdir():
    if i.name in [str(i) for i in range(10000)]:
        os.system(f'rmdir /S /Q {i}')


# for i in range(10000):
#     pathlib.Path(f'{i}/').mkdir()
#     with open(f'./{i}/helloworld.txt', 'w') as helloworld:
#         helloworld.write(f'OLÁ MUNDO {i}')
