def find_needle(haystack: list):
    return f"found needle at position {haystack.index("needle")}"
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))