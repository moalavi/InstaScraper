import requests
from bs4 import BeautifulSoup

# Set up session and login
session = requests.Session()
login_url = 'https://www.instagram.com/accounts/login/ajax/'
username = 'your_instagram_username'
password = 'your_instagram_password'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Send login request
session.headers = {'User-Agent': user_agent}
session.headers.update({'Referer': 'https://www.instagram.com/'})
login_data = {'username': username, 'password': password}
session.post(login_url, data=login_data, allow_redirects=True)

# Target user's profile page
target_user = 'target_user'
target_url = f'https://www.instagram.com/{target_user}/'

# Send request to target user's profile page
response = session.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
username = soup.find('h1', class_='rhpdm').get_text()
followers_count = soup.find('span', class_='g47SY').get_text().replace(',', '')
following_count = soup.find_all('span', class_='g47SY')[1].get_text().replace(',', '')
profile_picture_url = soup.find('img', class_='be6sR')['src']

# Output data
print(f'Username: {username}')
print(f'Followers: {followers_count}')
print(f'Following: {following_count}')
print(f'Profile Picture URL: {profile_picture_url}')

# Scrape list of followers
followers_url = f'https://www.instagram.com/{target_user}/followers/'
response = session.get(followers_url)
soup = BeautifulSoup(response.text, 'html.parser')
followers = []
for user in soup.find_all('a', class_='FPmhX notranslate _0imsa'):
    followers.append(user.get_text())

# Output list of followers
print(f'Followers List: {followers}')

# Scrape list of following
following_url = f'https://www.instagram.com/{target_user}/following/'
response = session.get(following_url)
soup = BeautifulSoup(response.text, 'html.parser')
following = []
for user in soup.find_all('a', class_='FPmhX notranslate _0imsa'):
    following.append(user.get_text())

# Output list of following
print(f'Following List: {following}')

# Target post page
target_post = 'target_post'
target_url = f'https://www.instagram.com/p/{target_post}/'

# Send request to target post page
response = session.get(target_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
likes_count = soup.find('div', class_='Nm9Fw').find('button').get_text().replace(',', '')
comments_count = soup.find('div', class_='eo2As').find_all('span')[1].get_text().replace(',', '')
views_count = soup.find('div', class_='eo2As').find('span', class_='vcOH2').get_text().replace(',', '')

# Output data
print(f'Likes: {likes_count}')
print(f'Comments: {comments_count}')
print(f'Views: {views_count}')