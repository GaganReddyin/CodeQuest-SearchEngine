import re
import os

common_words = ["Input", "Output", "Explaination", "Example", "the", "a", "an", "is", "are", "and", "in", "of", "to", "that", "or", "at"]

def writeToFile(pageContent,index):
    file = open(f'cleanedQuestion/questionContentLeetcode{index}.txt','w')
    file.write(pageContent )
    file.close()

def getPageContent(index):
    target_directory = f'questionContent\questionContentLeetcode{index}.txt'
    file = open(target_directory,'r')
    content = file.read()
    return content

def remove(pattern,pageContent):
    pageContent = re.sub(r'\d+', '', pageContent)
    pageContent = re.sub(pattern, '', pageContent)
    pageContent = re.sub(r'\s+', ' ', pageContent).strip()
    pageContent = re.sub(r'[^\w\s]', '', pageContent)
    pageContent = re.sub(r'\b\w\b', '', pageContent)
    pageContent = ' '.join([word for word in pageContent.split() if word.lower() not in common_words])
    return pageContent
    
def main_function():
    pageContent = getPageContent(1)
    pattern = r'\[.*?\]'
    pageContent = remove(pattern,pageContent)
    print(pageContent)
    writeToFile(pageContent,1)
    
if __name__ == "__main__":
    main_function()