def detect_spoilers(content, keywords):
    spoilers = [keyword for keyword in keywords if keyword.lower() in content.lower()]
    return spoilers
