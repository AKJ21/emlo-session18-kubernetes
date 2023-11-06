import requests
import time


for i in range(0,1000):
    t1 = time.time()
    text = "India"
    url = f"http://localhost/infer?text={text}"
    # print(url)
    response = requests.post(url)
    print(response.json())
    print("Time taken {0:.2f}".format(time.time() - t1))

