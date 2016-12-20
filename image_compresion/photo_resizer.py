# открыть фото файл, открыть программу, сохранить результат в новую папку Result
import glob
import os.path
import subprocess
from pprint import pprint

source = 'Source'
convert_exe = "C:\\Program Files\\ImageMagick-7.0.3-Q16\\convert.exe"

files = glob.glob(os.path.join(source, "*.jpg"))
if not os.path.exists('Result'):
    os.mkdir('Result')
for original_file in files:
    pprint('File %s is processing' % original_file)
    output_file_name = original_file.replace('Source', 'Result')
    e = subprocess.run(
        [convert_exe, original_file, '-resize', '200', output_file_name])

print('Done')
