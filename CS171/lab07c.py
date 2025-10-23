def is_balanced(expression):
    filtered_characters = []
    for character in expression:
        if character in "()":
            filtered_characters.append(character)
    expression = "".join(filtered_characters)
    
    if not expression:
        return True
    if "()" in expression:
        return is_balanced(expression.replace("()",""))
    
    return False

def main():
    character = input()
    print(f"is_balanced{character} returns {is_balanced (character)}")

if __name__ == '__main__':
    character = input()
    print(f"is_balanced{character} returns {is_balanced (character)}")