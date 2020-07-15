# kannada-Text-Summarizor
POS and text summarization are the core concepts of every Natural Language
processing Techniques, Text Summarization reduces the size of the content and give the
brief summary of the whole content. we have implemented Kannada text summarizer
using NLP. this model will allow the user to upload the files which is in Kannada. Once
the file is uploaded the text rank algorithm is processed in a few minutes get back to the
user and prompt the summary size from the whole document. the idea behind the
algorithm is ranking the sentences using the graph method, vector, cosine similarity.
Higher the cosine similarity is the top sentence. The page rank algorithm will take the
numerical values which obtain by the cosine similarity and arrange them in accordingly.
The end of the process, the model will generate top ranking sentences in the user
interface to perform print or generate the pdf. The process of generating summary
involves various sub methods or sub stages to generate the final summary. All the steps
from data cleaning to generate summary have done with specification and handled all the
exception.


The main objective of the project is to construct a text summarisation software that
specifically summarizes documents and articles in Kannada language while maintain its
original. It achieves this by
 The proposed system first takes the given the given Kannada document cleans
and formats it
 Then the Kannada word embedding’s found for the cleaned document.

28 | P a g
e
 The processed document undergoes cosine similarity to find similarity matrix is
found
 Finally, the summarized form of the input document is obtained using the text
rank algorithm.
By this process, we aim to obtain a summary any Kannada document.
