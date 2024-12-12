from jinja2 import Enviroment, FileSystem
import os

class Post:
    def __init__ (self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    def __str__(self):
        print(f"Tytuł: {self.title}, Zawartość")
        
class BlogModel:
    def __init__ (self):
        self.posts = []
    def add_post(self, title, content, author):
        post = {
            "title": title,
            "content": content,
            "author": author
        }
        self.posts.append(post)

    def get_all_posts(self):
        return self.post
    
class BlogView:
    def __init__(self):
        template = self.emv.get_template("blog.html")
        self.emv = Enviroment(loader=FileSystemLoader("template"))

    def render_blog(self, posts):
        template = self.emv.get_template("blog.html")
        return template.render(posts)
    
    def create_new_blog(model):
        title = input("wprowadź tytuł posta: ")
        content = input("wprowadź treść posta: ")
        author = input("wprowadź autora posta: ")
        model.add_post(title, content, author)
# Logika główna
def create_blog_page(posts):

    view = BlogView
    html_output = view

if __name__ == "__main__":
    # Inicjalizacja modelu
    model = BlogModel()

    # Dodanie ilku początkowych postów
    model.add_post("My 1 post", "content of My 1 post", "john Doe")
    model.add_post("My 2 post", "content of My 2 post", "john Doe")

    # Generowanie strony HTML początkowe
    create_blog_page(model.get_all_posts)

    while True:
        #zapytaj użytkownika czy chce zrobić nowego posta
