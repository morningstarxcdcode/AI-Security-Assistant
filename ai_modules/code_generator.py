class CodeGenerator:
    def __init__(self):
        pass

    def generate_code(self, prompt):
        print(f"[CodeGenerator] generate_code called with prompt of type {type(prompt)}: {repr(prompt)}")
        import ast
        # Try to parse the prompt as a dict
        try:
            if isinstance(prompt, str):
                prompt_dict = ast.literal_eval(prompt)
            else:
                prompt_dict = prompt
        except Exception as e:
            prompt_dict = {"goals": "", "instructions": "", "context": "", "constraints": ""}
        goals = prompt_dict.get("goals", "").lower()
        # If the goals mention IDOR, return a sample Python script
        if "idor" in goals:
            return (
                "```python\n"
                "import requests\n"
                "url = 'https://example.com/api/user/profile'\n"
                "cookies = {'session': 'YOUR_SESSION_COOKIE'}\n"
                "payload = {'user_id': 124, 'name': 'Hacked'}\n"
                "r = requests.post(url, cookies=cookies, data=payload)\n"
                "if r.status_code == 200:\n"
                "    print('Possible IDOR! Profile updated for user_id=124')\n"
                "elif r.status_code == 403:\n"
                "    print('Access denied (403) - likely protected')\n"
                "else:\n"
                "    print(f'Status: {r.status_code} - {r.text[:100]}')\n"
                "```\n"
            )
        # Default response
        return "No specific code generated. Please specify a vulnerability or goal."
