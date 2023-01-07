import requests
import threading
import time
import sys
import click
Counter = 0
Timeout = 1

@click.command()
@click.argument("url")
def main(url):
    downloadThread = threading.Thread(target=downloadFile, args=(str(url)), daemon = True)   
    idleThread = threading.Thread(target=getLoadInfo, daemon= True)     
    downloadThread.start()
    idleThread.start()
    
    

def downloadFile(url):
    if url is None:
        return

    cuttedUrl = url.split("/")
    name = cuttedUrl[len(cuttedUrl) - 1]
    response = requests.get(url=url, stream=True)
    global Counter
    file = open(str(name), mode='wb')
    for i in response.iter_content(chunk_size=256):
        if i is not None:
            Counter += 256
            file.write(i)
    print(f"Totaly {Counter} bytes is uploaded")

def getLoadInfo():
    try:
        while True:
            time.sleep(Timeout)
            print(f"{Counter} bytes is loaded")
            sys.stdout.flush()
    finally:
        print("Load is done")


if __name__ == '__main__':
    main()
