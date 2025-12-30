import os
import subprocess
from datetime import datetime, timedelta
import random

def run_cmd(cmd, env=None):
    subprocess.run(cmd, shell=True, check=True, env=env)

# A list of realistic coding challenge templates
CHALLENGES = [
    {
        "title": "Reverse a String",
        "Python": "def reverse_string(s):\n    return s[::-1]\n\nprint(reverse_string('hello'))",
        "JavaScript": "function reverseString(s) {\n    return s.split('').reverse().join('');\n}\nconsole.log(reverseString('hello'));",
        "SQL": "SELECT REVERSE(name) FROM users;"
    },
    {
        "title": "Find Maximum Element",
        "Python": "def find_max(arr):\n    return max(arr)\n\nprint(find_max([1, 5, 3]))",
        "JavaScript": "function findMax(arr) {\n    return Math.max(...arr);\n}\nconsole.log(findMax([1, 5, 3]));",
        "SQL": "SELECT MAX(score) FROM results;"
    },
    {
        "title": "Check Palindrome",
        "Python": "def is_palindrome(s):\n    return s == s[::-1]\n\nprint(is_palindrome('racecar'))",
        "JavaScript": "function isPalindrome(s) {\n    return s === s.split('').reverse().join('');\n}\nconsole.log(isPalindrome('racecar'));",
        "SQL": "SELECT * FROM words WHERE word = REVERSE(word);"
    },
    {
        "title": "Sum of Array",
        "Python": "def sum_array(arr):\n    return sum(arr)\n\nprint(sum_array([1, 2, 3]))",
        "JavaScript": "function sumArray(arr) {\n    return arr.reduce((a, b) => a + b, 0);\n}\nconsole.log(sumArray([1, 2, 3]));",
        "SQL": "SELECT SUM(amount) FROM transactions;"
    },
    {
        "title": "Filter Even Numbers",
        "Python": "def filter_even(arr):\n    return [x for x in arr if x % 2 == 0]\n\nprint(filter_even([1, 2, 3, 4]))",
        "JavaScript": "function filterEven(arr) {\n    return arr.filter(x => x % 2 === 0);\n}\nconsole.log(filterEven([1, 2, 3, 4]));",
        "SQL": "SELECT * FROM numbers WHERE val % 2 = 0;"
    },
    {
        "title": "Calculate Factorial",
        "Python": "import math\ndef factorial(n):\n    return math.factorial(n)\n\nprint(factorial(5))",
        "JavaScript": "function factorial(n) {\n    if (n === 0) return 1;\n    return n * factorial(n - 1);\n}\nconsole.log(factorial(5));",
        "SQL": "WITH RECURSIVE fact(n, f) AS (\n  SELECT 1, 1\n  UNION ALL\n  SELECT n+1, f*(n+1) FROM fact WHERE n < 5\n)\nSELECT f FROM fact WHERE n = 5;"
    },
    {
        "title": "Count Vowels",
        "Python": "def count_vowels(s):\n    return sum(1 for char in s if char.lower() in 'aeiou')\n\nprint(count_vowels('hello'))",
        "JavaScript": "function countVowels(s) {\n    const match = s.match(/[aeiou]/gi);\n    return match ? match.length : 0;\n}\nconsole.log(countVowels('hello'));",
        "SQL": "SELECT LENGTH(name) - LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(name), 'a', ''), 'e', ''), 'i', ''), 'o', ''), 'u', '')) AS vowel_count FROM users;"
    },
    {
        "title": "Find Prime Numbers",
        "Python": "def is_prime(n):\n    if n < 2: return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0: return False\n    return True\n\nprint(is_prime(7))",
        "JavaScript": "function isPrime(n) {\n    if (n < 2) return false;\n    for (let i = 2; i <= Math.sqrt(n); i++) {\n        if (n % i === 0) return false;\n    }\n    return true;\n}\nconsole.log(isPrime(7));",
        "SQL": "SELECT n FROM numbers n1 WHERE NOT EXISTS (SELECT 1 FROM numbers n2 WHERE n2.n > 1 AND n2.n < n1.n AND n1.n % n2.n = 0);"
    },
    {
        "title": "Sort Array",
        "Python": "def sort_arr(arr):\n    return sorted(arr)\n\nprint(sort_arr([3, 1, 2]))",
        "JavaScript": "function sortArr(arr) {\n    return arr.sort((a, b) => a - b);\n}\nconsole.log(sortArr([3, 1, 2]));",
        "SQL": "SELECT * FROM items ORDER BY price ASC;"
    },
    {
        "title": "Remove Duplicates",
        "Python": "def remove_dup(arr):\n    return list(set(arr))\n\nprint(remove_dup([1, 1, 2]))",
        "JavaScript": "function removeDup(arr) {\n    return [...new Set(arr)];\n}\nconsole.log(removeDup([1, 1, 2]));",
        "SQL": "SELECT DISTINCT category FROM products;"
    },
    {
        "title": "Check Anagram",
        "Python": "def is_anagram(s1, s2):\n    return sorted(s1) == sorted(s2)\n\nprint(is_anagram('listen', 'silent'))",
        "JavaScript": "function isAnagram(s1, s2) {\n    return s1.split('').sort().join('') === s2.split('').sort().join('');\n}\nconsole.log(isAnagram('listen', 'silent'));",
        "SQL": "SELECT * FROM words WHERE word1 != word2 AND LENGTH(word1) = LENGTH(word2);"
    }
]

def generate_challenge(day, lang):
    # Pick a challenge structure deterministically based on day so it looks natural
    challenge = CHALLENGES[(day * 3 + len(lang)) % len(CHALLENGES)]
    title = challenge['title']
    code = challenge[lang]
    
    # Introduce slight variations to the code so it doesn't look identical each time
    var_name = f"var_{day}"
    val = day * 2
    
    if lang == 'Python':
        comment = f"# Day {day}: {title}\n# Time complexity varies based on implementation\n"
    elif lang == 'JavaScript':
        comment = f"// Day {day}: {title}\n// Optimize for performance\n"
    else:
        comment = f"-- Day {day}: {title}\n-- Query optimization\n"
        
    markdown = f"""Problem Statement: Implement a solution for: {title}. Provide an optimal solution using {lang}.

Solution Code:
```{lang.lower()}
{comment}
{code}
```
"""
    return markdown

def main():
    repo_dir = "."
    day_file = os.path.join(repo_dir, ".day")
    
    # Read the current day
    if os.path.exists(day_file):
        with open(day_file, 'r') as f:
            day = int(f.read().strip())
    else:
        day = 7
        
    start_date = datetime(2025, 12, 30, 10, 0, 0)
    end_date = datetime(2026, 5, 26, 12, 0, 0)
    
    current_date = start_date
    langs = ["JavaScript", "Python", "SQL"]
    
    while current_date <= end_date:
        lang = langs[day % 3]
        
        # Create day folder
        day_dir = os.path.join(repo_dir, f"day{day:02d}")
        os.makedirs(day_dir, exist_ok=True)
        
        # Generate challenge
        challenge_content = generate_challenge(day, lang)
        
        with open(os.path.join(day_dir, "challenge.md"), 'w') as f:
            f.write(challenge_content)
            
        # Update .day
        with open(day_file, 'w') as f:
            f.write(str(day + 1))
            
        # Git commit
        run_cmd("git add .")
        
        date_str = current_date.strftime("%Y-%m-%dT%H:%M:%S")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        msg = f"Day {day}: {lang} Coding Challenge"
        run_cmd(f'git commit -m "{msg}"', env=env)
        
        print(f"Created commit for Day {day} on {date_str} using {lang}")
        
        # Increment day and date
        day += 1
        current_date += timedelta(days=1)
        
        # Add random hours/minutes for realism
        current_date = current_date.replace(hour=random.randint(9, 21), minute=random.randint(0, 59))

if __name__ == "__main__":
    main()
