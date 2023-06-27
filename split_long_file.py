import os

# Variables to specify your directories and file names
input_directory = r'C:\Users\ARTO\GitLab\novosloth\notebooks\data'
output_directory = r'C:\Users\ARTO\GitLab\sandbox_arto\test_docsearch\privateGPT\source_documents'
file_name = 'paul_graham_essay.txt'

def split_file(input_dir, output_dir, filename, max_words=500):
    with open(os.path.join(input_dir, filename), 'r') as f:
        text = f.read()
        words = text.split()
        
    for i in range(0, len(words), max_words):
        segment = ' '.join(words[i:i+max_words])
        with open(os.path.join(output_dir, f'{filename[:-4]}_part_{i//max_words + 1}.txt'), 'w') as f:
            f.write(segment)

# Call the function with your directories and file name
split_file(input_directory, output_directory, file_name)
