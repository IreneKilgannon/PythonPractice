from urllib.request import urlretrieve

url = (
    'https://courses.cs.washington.edu/courses/cse390c/22sp/lectures/moby.txt'
    )

filename = 'moby_dicktrial.txt'

urlretrieve(url, filename)

path, headers = urlretrieve(url, filename)
for name, value in headers.items():
    print(name, value)