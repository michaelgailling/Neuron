from __future__ import annotations
from pydantic import BaseModel


class SPPrompt(BaseModel):
    identity: str
    input_format: str
    goals: list
    bounds: list
    output_format: dict


if __name__ == "__main__":
    pd_poetry = {
        "identity": "Poet",
        "input_format": "You will be provided with a request for poetry.",
        "goals":
            [
                "You will write 5 lines of poetry.",
                "You will make all five lines rhyme."
            ],
        "bounds":
            [
                "You will not exceed 5 lines of poetry."
            ],
        "output_format":
            {
                "poem":
                    [
                        "Line of poetry.",
                        "Line of poetry.",
                        "Line of poetry.",
                        "Line of poetry.",
                        "Line of poetry."
                    ]
            }
    }

    spp = SPPrompt(**pd_poetry)

    print(spp.dict())
