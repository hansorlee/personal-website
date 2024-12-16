from scholarly import scholarly

# Replace this with your Google Scholar ID
scholar_id = "vmcet8AAAAAJ"

# Fetch author profile
author = scholarly.search_author_id(scholar_id)
scholarly.fill(author)

# Open a Markdown file to save the output
with open("publications.md", "w") as f:
    f.write("# Publications\n\n")

    # Iterate through each publication
    for pub in author['publications']:
        # Fill in additional metadata for the publication
        filled_pub = scholarly.fill(pub)

        # Extract relevant metadata
        title = filled_pub['bib'].get('title', 'Untitled')
        year = filled_pub['bib'].get('pub_year', 'n.d.')
        citation = filled_pub['bib'].get('citation', 'Venue unavailable')

        # Extract author list and format it for APA
        authors = filled_pub['bib'].get('author', 'Unknown authors')
        authors_formatted = ', '.join(authors.split(' and ')) if ' and ' in authors else authors

        # Format the reference
        reference = f"{authors_formatted} ({year}). {title}. *{citation}*.\n"
        
        # Write to the Markdown file
        f.write(reference + "\n")
