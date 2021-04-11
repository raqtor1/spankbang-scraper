import requests
from bs4 import BeautifulSoup

query = input("Search: ")
limit = int(input("No. of videos you want: "))

r = requests.get(f"https://spankbang.com/s/{query}").text
soup = BeautifulSoup(r, 'lxml')

# even though theres a limit for the number
# of videos you can get, we ignore the max limit
# and get as much as possible. So for example,
# if we set limit to 100 or 10,000 the maximum
# results may just be something around 8 - 15.
for item in soup.find_all('div', class_='video-item')[0:limit]:

    full_video = item.find("a", class_='thumb')['href']
    # sometimes /category/ shows up
    # which isn't a video link.
    if "/category/" in full_video:
        continue

    # cba to find the proper title from html
    # note that this may not always give proper title
    title = full_video.split('/')[3].replace('+', ' ')

    prev = item.picture.img
    # sometimes preview image or preview video
    # won't load for whatever reason.
    try:
        prev_vid = prev['data-preview']
        image = prev['data-src']
    except:
        prev_vid = "Not Found"
        image = "Not Found"

print(
    f"""
    Title: {title}
    Thumbnail: {image}
    Preview Video: {prev_vid}
    Full Video: https://spankbang.com/watch{full_video}
    """
)
