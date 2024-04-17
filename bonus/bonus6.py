contents = ["All carrots are to be sliced longitudinally",
            "The carrots were reportedly sliced.",
            "The carrots are in multiple colors of the rainbow."]

filenames = ["doc.txt", "presentation.txt", "report.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)