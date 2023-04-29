from src.models.Neuron import Neuron
from src.prompts.system_prompts import sp_sentence_adder



nrn_fb_adder = Neuron(system_prompt=sp_sentence_adder, activation_thresh=2)

input_text = "The shape of things to come..."
# Be careful how many times you loop this! It can get expensive!$!$!$!
for i in range(5):
    nrn_fb_adder.add_context_prompt(input_text)
    res = nrn_fb_adder()
    input_text += f" {res}"
    print()
    print(input_text)
    print()


