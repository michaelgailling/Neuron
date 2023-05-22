from src.models.Neuron import Neuron
from src.prompts.system_prompts import sp_complexity


nrn_complex = Neuron(system_prompt=sp_complexity, activation_thresh=2, json_output=True)

input_text = '''How to fly'''

# nrn_complex.add_context_prompt(input_text)

n = 20

total = 0

for i in range(n):
    nrn_complex.add_context_prompt(input_text)
    rating = nrn_complex()
    print(rating)
    total += int(rating["rating"])

print(total/n)

