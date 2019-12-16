import pandas as pd
import input


def get_images():
    data = str(input.data)
    chunks, chunk_size = len(data), 25
    rows = [data[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

    start = 0
    end = 6
    images = []
    for x in range(0, int(len(rows) / 6) - 1):
        images.append('\n'.join(rows[start:end]))
        start += 6
        end += 6
    return images


def part_one(images):
    df = pd.DataFrame(columns=['zeros', 'image'])
    for image in images:
        zeros = image.count('0')
        df = df.append({'zeros': zeros,
                        'image': image},
                       ignore_index=True)
    suspect = df.sort_values(by='zeros').reset_index()
    return suspect['image'][0]


images = get_images()
suspect = part_one(images)

# Part One
print(suspect.count('1') * suspect.count('2'))
