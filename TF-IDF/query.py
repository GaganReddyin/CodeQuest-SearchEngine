import json
import sys
import os

def main(TF_IDF_map, document_links, document_names, document):
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = input("Enter your query: ")
        
    query = query.lower()
    query = query.split()

    potential_documents = {}
    results = []

    try:
        for word in query:
            if word in TF_IDF_map:
                for index in TF_IDF_map[word]:
                    if index in potential_documents:
                        potential_documents[index] += TF_IDF_map[word][index]
                    else:
                        potential_documents[index] = TF_IDF_map[word][index]
                        
        potential_documents = sorted(potential_documents.items(), key=lambda x: x[1], reverse=True)

        for index , score in potential_documents:
            index = int(index)
            results.append(str(document_links[index]) + "*" + str(document_names[index]))
    except:
        exit()
        
    results = list(set(results))
        
    output_data = {
        'results': results
    }

    # Convert the output data to JSON string
    json_data = json.dumps(output_data)

    print(json_data)
    
if __name__ == '__main__':
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(current_dir, 'output.json')
        doc_file = os.path.join(current_dir, 'doc.json')
        links_file = os.path.join(current_dir, 'links.json')
        names_file = os.path.join(current_dir, 'names.json')
        
        with open(output_file, 'r') as file:
            TF_IDF_map = json.load(file)

        with open(doc_file, 'r') as file:
            document = json.load(file)
        
        with open(links_file, 'r') as file:
            document_links = json.load(file)

        with open(names_file, 'r') as file:
            document_names = json.load(file)
    except:
        exit()
        
    main(TF_IDF_map, document_links, document_names, document)