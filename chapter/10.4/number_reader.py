from pathlib import Path
import json

path = Path('numbers.json')

contents = path.read_text()
print(contents)

numbers = json.loads(contents)
print(numbers)
