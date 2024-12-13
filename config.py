def config(filename='database.ini', section='postgresql'):
    from configparser import ConfigParser

    # Create a parser
    parser = ConfigParser()

    # Read config file
    parser.read(filename)
    print(f"Sections found: {parser.sections()}")  # Debugging line

    # Initialize a dictionary for the section
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        print(f"Parameters retrieved: {db}")  # Debugging line
    else:
        raise Exception(f"Section {section} not found in the {filename} file")

    return db
