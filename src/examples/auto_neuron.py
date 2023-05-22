import json

from src.models.Neuron import Neuron
from src.prompts.prompt_dictionaries import pd_thinker, pd_rank
from src.services.PromptGenerator import PromptGenerator

if __name__ == "__main__":
    pg_auto = PromptGenerator(**pd_thinker)
    nrn_auto = Neuron(pg_auto.prompt, 2, True)
    pg_rank = PromptGenerator(**pd_rank)
    nrn_rank = Neuron(pg_rank.prompt, 2, True)
    objective = "Make $1000000 with $1000 in 12 months."
    thinker_dict = {
        "objective": objective,
        "actions_taken":
            []
    }

    for i in range(5):
        thinker_prompt = json.dumps(thinker_dict)

        print()
        print("Thinker Prompt:")
        print()
        print(thinker_prompt)
        print()

        nrn_auto.add_context_prompt(objective)

        action_dict = nrn_auto()
        print()
        print("Thinker Response:")
        print()
        print(json.dumps(action_dict, indent=4))
        print()

        action_list = action_dict["courses_of_action"]

        rank_str = f"Objective:\n{objective}\n"
        rank_str = "Actions:\n"

        for action in action_list:
            rank_str += f"{action}\n"

        nrn_rank.add_context_prompt(rank_str)

        rank_dict = nrn_rank()

        print()
        print("Ranker Response:")
        print()
        print(json.dumps(rank_dict, indent=4))
        print()

        rank_list = rank_dict["courses_of_action"]

        thinker_dict["actions_taken"].append(rank_list[0])

print()
print("Thinker Prompt:")
print()
print(thinker_prompt)
print()