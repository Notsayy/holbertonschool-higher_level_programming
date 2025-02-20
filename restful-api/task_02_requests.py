import requests
import csv

"""
Function to interact with the request library
"""


def fetch_and_print_post():
    """Fetch post titles from an API and print them."""
    api_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {api_response.status_code}")

    if api_response.status_code == 200:
        list_of_posts = api_response.json()
        for one_post in list_of_posts:
            print(one_post["title"])


def fetch_and_save_posts():
    """Fetch posts from an API and save them to a CSV file."""
    api_response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if api_response.status_code == 200:
        list_of_posts = api_response.json()
        structured_posts = [{'id': post['id'], 'title': post['title'],
                             'body': post['body']} for post in list_of_posts]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=['id',
                                                             'title', 'body'])
            csv_writer.writeheader()
            for one_post in structured_posts:
                csv_writer.writerow(one_post)
