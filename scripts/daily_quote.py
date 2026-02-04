import random
import os

# Lista de citações tech/programação
QUOTES = [
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
    "Truth can only be found in one place: the code. - Robert C. Martin",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
    "Java is to JavaScript what car is to Carpet. - Chris Heilmann",
    "Knowledge is power. - Francis Bacon",
    "Code is like humor. When you have to explain it, it’s bad. - Cory House",
    "Fix the cause, not the symptom. - Steve Maguire",
    "Simplicity is the soul of efficiency. - Austin Freeman",
    "Make it work, make it right, make it fast. - Kent Beck",
    "Python is the new Excel.",
    "While there is code, there is a bug.",
    "It works on my machine!",
    "One man's crappy software is another man's full time job. - Jessica Gaston"
]

def update_readme():
    readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
    print(f"Reading from: {readme_path}")
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("README.md not found!")
        return

    quote = random.choice(QUOTES)
    
    start_marker = "<!-- START_SECTION:quote -->"
    end_marker = "<!-- END_SECTION:quote -->"
    
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        new_content = (
            content[:start_index + len(start_marker)]
            + f"\n> 💡 **Daily Wisdom:** {quote}\n"
            + content[end_index:]
        )
        
        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated README with quote: {quote}")
    else:
        print("Markers not found in README.md")

if __name__ == "__main__":
    update_readme()
