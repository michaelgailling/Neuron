import json

from src.models.Neuron import Neuron
from src.prompts.system_prompts import sp_list, sp_detail


nrn_uh_list = Neuron(system_prompt=sp_list, activation_thresh=2, json_output=True)
nrn_uh_detail = Neuron(system_prompt=sp_detail, activation_thresh=2, json_output=True)

objective = "How to fly"

nrn_uh_list.add_context_prompt(objective)

res_list = nrn_uh_list()

instructions = res_list["instructions"]

for i in instructions:
    print(i)

full_details = []

for i in range(len(instructions)):
    step_desc = f'''
    Objective: {objective}
    Step {i+1}: {instructions[i]} 
    '''
    print(step_desc)
    nrn_uh_detail.add_context_prompt(step_desc)
    res = nrn_uh_detail()
    full_details.append(res)

for fd in full_details:
    print(json.dumps(fd, indent=4))

