from datasets import load_dataset

dataset = load_dataset("AI4Math/MathVerse", "testmini")
dataset_text_only = load_dataset("AI4Math/MathVerse", "testmini_text_only")
# print the first example on the testmini set
print("Dataset entry:\n")
print("Test sample ID:\n", dataset["testmini"][0]['sample_index'], "\n")  # print the test sample id
print("Unique problem ID:\n", dataset["testmini"][0]['problem_index'], "\n")  # print the unique problem id
print("Problem version:\n", dataset["testmini"][0]['problem_version'], "\n")  # print the problem version
print("Question text:\n", dataset["testmini"][0]['question'], "\n")  # print the question text
print("Answer:\n", dataset["testmini"][0]['answer'], "\n")  # print the answer
print("Query without scores (w/o):\n", dataset["testmini"][0]['query_wo'], "\n")  # the input query for w/o scores
print("Query for CoT evaluation scores:\n", dataset["testmini"][0]['query_cot'], "\n")  # the input query for CoT evaluation scores

# If you want to print information about the image, you can use the following line:
print("Image data:\n", dataset["testmini"][0]['image'], "\n")  # display the image (this might not be meaningful as plain text)
