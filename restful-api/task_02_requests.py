#!/usr/bin/python3

import requests
import csv


def fetch_and_print_post_titles():
    """Fetch post titles from an API and print them."""
    api_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {api_response.status_code}")

    if api_response.status_code == 200:
        list_of_posts = api_response.json()
        for one_post in list_of_posts:
            print(one_post["title"])


def fetch_and_save_posts_to_csv():
    """Fetch posts from an API and save them to a CSV file."""
    api_response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if api_response.status_code == 200:
        list_of_posts = api_response.json()
        structured_posts = []

        for post in list_of_posts:
            structured_post = {
                'post_id': post['id'],
                'post_title': post['title'],
                'post_content': post['body']
            }
            structured_posts.append(structured_post)

        with open('posts.csv', 'w', newline='') as csvfile:
            column_names = ['post_id', 'post_title', 'post_content']
            csv_writer = csv.DictWriter(csvfile, fieldnames=column_names)
            csv_writer.writeheader()
            for one_post in structured_posts:
                csv_writer.writerow(one_post)


if __name__ == "__main__":
    fetch_and_print_post_titles()
    fetch_and_save_posts_to_csv()
