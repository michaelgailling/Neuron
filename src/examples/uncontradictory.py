from src.models.Neuron import Neuron
from src.prompts.system_prompts import sp_uncontradict, sp_explainer

# This text was produced by gpt with the prompt: give me 2 bodies of text that contain contradictory statements but both contain elements of the truth
contradictions_1 = '''
Body of text 1:
Scientific research consistently demonstrates that vaccines are a safe and effective method of preventing infectious diseases. They have led to the eradication of smallpox, and the near-elimination of polio, measles, and other life-threatening illnesses. Vaccines work by stimulating the immune system to create a defense against specific pathogens, thus decreasing the likelihood of severe illness. However, some individuals may experience minor side effects such as fever, soreness at the injection site, or fatigue. It's essential to recognize that the benefits of vaccination far outweigh the risks, and maintaining high vaccination rates is crucial for public health.

Body of text 2:
Although vaccines have been credited with reducing the impact of many infectious diseases, they are not without risks. Some vaccines may cause adverse effects in a small percentage of the population, ranging from mild to severe. In rare cases, individuals may experience allergic reactions, fever, or even neurological complications. Furthermore, while vaccines can be effective in protecting against specific diseases, they are not a guarantee against infection. In some cases, vaccinated individuals may still contract the illness, albeit often with milder symptoms. It's crucial for individuals to carefully consider the potential risks and benefits of vaccination and consult with their healthcare provider before making a decision.
'''

contradictions_2 = '''
Body of text 1:
Climate change is an unequivocal fact, supported by an overwhelming body of scientific evidence. Human activities, such as the burning of fossil fuels and deforestation, are the primary drivers of this phenomenon, leading to increased greenhouse gas emissions and global temperatures. The consequences of climate change include more frequent and severe weather events, melting ice caps, rising sea levels, and threats to biodiversity. Ignoring the reality of climate change and failing to take immediate and comprehensive action is a reckless and dangerous approach that will only lead to catastrophic consequences for future generations.

Body of text 2:
Climate change alarmists are perpetuating a massive hoax, using fear and manipulation to control the public and advance their political agendas. The scientific community is divided on the issue, and there is no consensus on the extent of human contribution to global warming or the severity of its consequences. Many natural factors, such as solar activity and volcanic emissions, can influence the Earth's climate, and it has always experienced fluctuations throughout its history. The hysteria surrounding climate change is unfounded and serves only to hinder economic growth and stifle human progress.
'''

contradictions_3 = '''
Body of text 1:
Freedom of speech is an inalienable right that forms the cornerstone of any democratic society. It allows individuals to express their thoughts, ideas, and beliefs without fear of censorship or persecution. This freedom fosters the open exchange of information, enabling the marketplace of ideas to flourish and promoting intellectual growth. Limiting or suppressing freedom of speech stifles creativity, restricts diversity of thought, and undermines the very principles of democracy. No matter how controversial or offensive an opinion may be, it should be protected and allowed to be voiced in a free society.

Body of text 2:
Unrestricted freedom of speech is a dangerous concept that leads to the spread of harmful and divisive ideas, which can incite hatred, violence, and social unrest. Societies must impose certain limits on speech to protect the greater good and maintain social harmony. Hate speech, disinformation, and other forms of harmful expression have no place in a civilized society and should be prohibited by law. By doing so, we create a safer, more inclusive environment for all citizens, where ideas can be debated respectfully and without fear of harm or discrimination.
'''

nrn_uncon = Neuron(system_prompt=sp_uncontradict, activation_thresh=2)
nrn_expl = Neuron(system_prompt=sp_explainer, activation_thresh=2)

nrn_uncon.add_context_prompt(contradictions_1)

res_1 = nrn_uncon()
print()
print(res_1)
print()

nrn_expl.add_context_prompt(res_1)

res_2 = nrn_expl()
print()
print(res_2)
print()


