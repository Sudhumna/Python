
try:
    from googlesearch import search
except ImportError:
    print("module not found")
query = input("Enter your query: ")
for i in search(query,tld='com',num = 10, stop = 10, pause = 2):
    print(i)