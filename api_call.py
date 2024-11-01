import os
from openai import OpenAI
from dotenv import load_dotenv
import tiktoken

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Constants
MODEL_NAME = "gpt-3.5-turbo-0125"
MAX_TOKENS = 16385  # Correct context window size for this model

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_tokens(text):
    encoding = tiktoken.encoding_for_model(MODEL_NAME)
    return len(encoding.encode(text))

def truncate_text(text, max_tokens):
    encoding = tiktoken.encoding_for_model(MODEL_NAME)
    return encoding.decode(encoding.encode(text)[:max_tokens])

def classify_paper(text, max_input_tokens=MAX_TOKENS):
    prompt = """
    Classify the following research paper into one of these classes:
    1. wheat_content_estimation
    2. wheat_grain_identification
    3. wheat_production_modeling
    4. wheat_root_modeling
    5. wheat_spatial_distribution_extraction
    6. wheat_spike_detection_and_counting

    Your primary task is to determine the main goal of the paper and select the most appropriate class. In most cases, you should choose only one class. However, if you find that the paper's primary goal genuinely encompasses two of the classes equally, you may provide two classes. This should be rare and only done when it's clear that the paper focuses equally on two areas.

    Provide your response in the following format:

    Class: [exact name of the chosen class(es), separated by a comma if two are chosen]

    Summary: [A one-paragraph summary of the paper's main goal(s) and the model or approach used]

    Here's the paper text:

    {text}
    """

    encoding = tiktoken.encoding_for_model(MODEL_NAME)
    prompt_tokens = len(encoding.encode(prompt))
    available_tokens = max_input_tokens - prompt_tokens

    truncated_text = truncate_text(text, available_tokens)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a research paper classifier specializing in wheat-related studies."},
                {"role": "user", "content": prompt.format(text=truncated_text)}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def process_papers(input_folder, output_folder, token_counts_file):
    with open(token_counts_file, 'r') as f:
        token_counts = dict(line.strip().split(': ') for line in f)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            paper_text = read_text_file(input_path)
            token_count = int(token_counts.get(filename, 0))

            if token_count > MAX_TOKENS:
                print(f"Truncating {filename} from {token_count} tokens to {MAX_TOKENS} tokens")
                paper_text = truncate_text(paper_text, MAX_TOKENS)

            classification_result = classify_paper(paper_text)

            if classification_result:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(classification_result)

                print(f"Processed: {filename}")
            else:
                print(f"Failed to process: {filename}")

if __name__ == "__main__":
    input_folder = "papers/txts"
    output_folder = "papers/api_results"
    token_counts_file = "papers/token_counts.txt"
    os.makedirs(output_folder, exist_ok=True)
    process_papers(input_folder, output_folder, token_counts_file)
