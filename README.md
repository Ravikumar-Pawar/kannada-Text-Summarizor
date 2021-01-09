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


Text summarization is process of reducing the size of the text data and obtains a
meaningful para in any language. This can be either Abstractive or Extractive way.
We are going to implement the Extractive text summarization in Kannada language
using the NLP, unsupervised technique. Kannada is a major language in Karnataka in
written and speaking both perspectives. in implementation no efficient text summarizer is available till now! This becomes a major challenge to implement a efficient and
easy text summarizer to kannada people who can write and read kannada text. to
achieve this challenge we have used TextRank algorithm as our implementation major
part. This algorithm is quite similar to google page rank algorithm which we most
familiar. Major difference is that, in page rank algorithm, we are referring a particular
page and it is ranking, in other hand TextRank is focusing on text data, sentences.
This will give us a ranking value to the particular sentence. Which mean how important is that sentence in the given context? This is era behind the Text summarization, we are extracting high ranked sentence as our summary content.

![Rouge_results](/Images/rouge_result.png)
