#!/usr/bin/python3

import requests, csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for post in data:
            print(post.get('title'))


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = r.json()
    if r.status_code == 200:
        post_list = []
        for post in data:
            new_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            post_list.append(new_post)
    with open('posts.csv', "w", encoding='utf-8', newline='') as f:
       fieldnames = ['id', 'title', 'body']
       writer = csv.DictWriter(f, fieldnames=fieldnames)
       writer.writeheader()
       writer.writerows(post_list)
