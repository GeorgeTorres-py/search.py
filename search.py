import glob, re

for msg in glob.glob('/tmp/*.txt'):
    filler = open((msg), 'r')
    data = re.filler.read()
    message = re.findall(r'<message>(.*?)>/message>', data.re.DOTALL)
    print('File %s contains %s'(str(msg),message))
    filler.close
