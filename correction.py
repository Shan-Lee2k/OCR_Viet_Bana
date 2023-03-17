import os

inputDir = 'fix_input'
resultDir = 'Final'
path = os.listdir(inputDir)
print(path)

dict = {'ð': 'ơ̆', 'ẽ': 'ĕ', '¡': 'i', 'mĩ': 'mĭ', 'ợ': 'ơ', 'ồ': 'ŏ', 'ố': 'ơ̆', 'ỗ': 'ô̆', 'ơi': 'ơĭ', 'ổi': 'ôĭ',
        'š': 'ĕ', 'Š': 'ê̆', 'ủ': 'ŭ', 'Ủ': 'Ŭ', 'ũ': 'ŭ', 'Ũ': 'Ŭ'}

for txt in path:
    txtFile = open(inputDir + '/' + txt, encoding='utf-8', errors='ignore').read()
    print(txtFile)
    for original, replace in dict.items():
        txtFile = txtFile.replace(original, replace)
    # Open resultDir
    with open(resultDir + '/' + txt, 'w', encoding='utf-8') as f:
        f.write(txtFile)
