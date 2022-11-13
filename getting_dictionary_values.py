courses = {
    "js": "JavaScript 101",
    "python": ["python 101", "Python 201"],
    "html": "HTML 101"
}

# print(courses.get("python"))
if courses.get("css", None):
    print("you are enrolled in CSS 101 ")
