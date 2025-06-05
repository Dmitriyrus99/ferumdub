import os
import openai

# Использует переменную окружения OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("\u274c OPENAI_API_KEY environment variable not set. Skipping audit.")
    raise SystemExit(1)

openai.api_key = api_key

# Фильтрация файлов по типу
FILE_EXTENSIONS = (".py", ".js")

def audit_code(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()
        if not code.strip():
            return

        print(f"\n🔍 Анализ: {path}")

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": f"Проанализируй код ниже. Найди ошибки, проблемы со стилем, плохие практики и предложи исправления:\n\n```python\n{code}\n```"}
            ],
            temperature=0,
            max_tokens=1024
        )

        print(response.choices[0].message.content)
    except Exception as e:
        print(f"⚠️ Ошибка при анализе {path}: {e}")

def scan_directory(root="."):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(FILE_EXTENSIONS):
                audit_code(os.path.join(dirpath, filename))

if __name__ == "__main__":
    scan_directory("ferumdub")
