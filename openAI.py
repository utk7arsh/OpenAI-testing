import openai
from api_secrets import API_KEY
import math

openai.api_key = API_KEY

prompt = "Tom was known for having a bit of a short fuse, so it was no surprise when he snapped one day after a guest said something that set him off. In a fit of anger, Tom let out a mighty roar and punched a hole right through the wall of his house. The guest, who had never seen Tom lose his cool like this before, was terrified and quickly made a hasty retreat out the door. As Tom sat on his couch, surrounded by the debris of his destroyed wall, he couldn't help but feel a little sheepish. 'Well, that wasn't exactly my finest moment,' he thought to himself. 'I guess I better start working on my anger management techniques before I end up with a house full of holes.' The end."
response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1, logprobs=5, echo=True)
#print(response)

xd = response["choices"]
xd2 = xd[0]["logprobs"]
xd3 = xd2["token_logprobs"] #this is the prob of all the words in the prompt
xd4 = xd2["tokens"]
xd5 = xd2["top_logprobs"] #this is the list of most probable words in that spot
#print(len(xd5) == len(xd3))


arr = []

for i in range(0, len(xd5)):
    maxki = None
    maxv = float("-inf")
    if xd5[i] is not None:
        for k,v in xd5[i].items():
            if k is not None:
                if v is not None and v > maxv:
                    maxki = k
                    maxv = v
        max_prob_word = maxki
        max_prob = maxv
        
        #print((math.e)**max_prob)
        antilog_most_prob_outcome = (math.e)**max_prob


        #print(antilog_most_prob_outcome)
        if xd3[i] is None:
            xd3[i] = 0.0
        arr.append([xd4[i], float(xd3[i] * antilog_most_prob_outcome)])
#print(arr)
arr.sort(key = lambda x:x[1])

print(arr)

#byte pairning coding - words breaking into parts because of the tokenizing