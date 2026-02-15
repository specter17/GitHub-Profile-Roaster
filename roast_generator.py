def generate_roast():
    roasts = [
        "Your face makes onions cry.",
        "You're like a cloud. When you disappear, it's a beautiful day.",
        "I would explain it to you but I left my English-to-Dingbat dictionary at home.",
        "You're proof that even evolution makes mistakes.",
        "I'd agree with you but then we'd both be wrong."
    ]
    import random
    return random.choice(roasts)

if __name__ == '__main__':
    print(generate_roast())