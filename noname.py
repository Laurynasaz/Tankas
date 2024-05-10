laurynas = """ echo "# Tankas" >> README.md
 git init
 git add README.md
 git commit -m "first commit"
 git branch -M main
 git remote add origin https://github.com/Laurynasaz/Tankas.git
 git push -u origin main """

print(laurynas)

for letter in laurynas:
    print(laurynas)