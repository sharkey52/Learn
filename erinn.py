import requests
maptype = 'satellite'
KEY = 'AIzaSyBtHWR-B_VqK-vO7YQMgBPYxnD9QiYN0hk'
location = 'airplane boneyard'
zoom = '16'
size = '600x600'
maptype = 'satellite'
image = f'https://maps.googleapis.com/maps/api/staticmap?format=png&center={location}&zoom={zoom}&maptype={maptype}&size={size}&key={KEY}'

image_url = 'https://www.boredpanda.com/blog/wp-content/uploads/2021/11/cute-rabbits-307-618b7d91f120c__700.jpg'

img_data = requests.get(image).content
with open('image.png', 'wb') as handler:
    handler.write(img_data)

