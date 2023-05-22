from __future__ import annotations

import json

from src.models.Neuron import Neuron
from src.prompts.prompt_dictionaries import pd_thinker


class PromptGenerator:
    def __init__(self, identity: str, input_format, goals: list[str], bounds: list[str], output_format):
        self._ident: str = identity
        self._input = input_format
        self._goals: list = goals
        self._bounds: list = bounds
        self._output = output_format

    @property
    def prompt(self):
        compiled_prompt = f"Identity: {self._ident}\n"

        compiled_prompt += "Input:\n"

        if type(self._input) == dict:
            compiled_prompt += f"{json.dumps(self._input)} \n"
        elif type(self._input) == list:
            for i in range(len(self._input)):
                in_val = self._input[i]
                compiled_prompt += f"{i+1}. {in_val}\n"
        else:
            compiled_prompt += f"{self._input}\n"

        compiled_prompt += "Goals:\n"

        for i in range(len(self._goals)):
            goal = self._goals[i]
            compiled_prompt += f"{i+1}. {goal}\n"

        compiled_prompt += "Boundaries:\n"

        for i in range(len(self._bounds)):
            bound = self._bounds[i]
            compiled_prompt += f"{i+1}. {bound}\n"

        compiled_prompt += "Do not include any explanations, only provide a  RFC8259 compliant JSON response  following this format without deviation:\n"

        if type(self._output) == dict:
            compiled_prompt += f"{json.dumps(self._output)} \n"
        else:
            compiled_prompt += f"{self._output} \n"

        return compiled_prompt






