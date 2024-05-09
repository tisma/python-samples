import urllib.request
import time


def download_image(pic_dir, url):
    result = urllib.request.urlopen(url)
    picture = result.read()
    with open(f'./{pic_id}.jpg','wb') as f:
        f.write(picture)
    print(f'Picture {pic_id} saved')
    
    
def main():
    url = 'https://picsum.photos/id/{}/200/300'
    args = [(n, url.format(n)) for n in range(20)]
    start = time.time()
    for _ in map(download_image, pic_ids, urls):
        pass
    end = time.time()
    message = 'Operation completed in {:.3f} seconds'
    print(message.format(end - start))
    
    
if __name__ == '__main__':
    main()
