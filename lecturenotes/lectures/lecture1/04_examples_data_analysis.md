
# Examples of Data Analysis: the Good, the Bad, and the Ugly
Before concluding this introduction, we will analyze and discuss some notable examples of data analyses. Since we don't have any theoretical or technical tool to understand these analysis in depth, we will just focus on the stories behind these analyses and their main outcomes.

It is important to emphasize that analyzing data is a complex process, hence it is prone to error. Moreover, when collecting data about people, such as their preferences and tastes, we should be careful of what kind of conclusion we draw from the analysis and what we do with the data. Keeping these pitfalls in mind, we will discuss three examples of data analysis, a **good** example in which data analysis can be used to make decisions and save lives, a **bad** example in which data analysis has been intentionally used to lie and deceive, and an **ugly** example in which data analysis has probably been performed in a technical correct, but unethical way.

These example are meant as a way to illustrate the power of data analysis and warn about the pitfalls and ethical implications.

## The Good: Stopping the Spread of Cholera

In the nineteenth century, cholera pandemics were common, but little was understood about them. A common belief was that cholera pandemics was caused by "miasma", particles in the air carrying the disease (see {numref}`miasma`). This was justified by the observation that pandemics tended to be localized, meaning that people getting the disease were living in the same house or neighborhood.

```{figure} /_static/lecture_specific/lecture1/miasma.jpg
---
name: miasma
---
A 19th century color lithograph by Robert Seymour depicting cholera as a skeletal creature emanating a deadly black cloud, based on the popular belief of miasma. Image from https://en.wikipedia.org/wiki/Miasma_theory.
```

In 1854, John Snow (See {numref}`jonsnow`), an English doctor, hypothesized that, instead, pandemics were due to the contamination of water with the contents of the sewer's system. 

```{figure} /_static/lecture_specific/lecture1/John_Snow.jpg
---
name: jonsnow
---
John Snow (1813 – 1858) was an English physician and a key figure in the development of anaesthesia and medical hygiene. Image from https://en.wikipedia.org/wiki/John_Snow.
```

When a severe outbreak of cholera started in Broad Street in London, John Snow started to analyze the deaths due to cholera and put them on a dot distribution map, which was later known as the "Ghost Map" (see {numref}`ghostmap`), since it took track of how many people died in a given place of the map. To collect, the data, John Snow interviewed local residents with the help of Reverend Henry Whitehead.

```{figure} /_static/lecture_specific/lecture1/ghostmap.jpeg
---
name: jonsnow
---
The ghost map made by Jon Snow to study the cholera outbreak. Image from https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak
```

In the map, bars represented the deaths, while circles represented the positions of public water pumps. At the time, people did not have water in their homes, hence they had to reach water pumps and get water from there. John Snow computed the distance of each of the houses to each water pump in the area and noted that for places with more deaths, the closest pump was located in Broad Street.

Based on this evidence, John Snow managed to convince the authorities to remove the handle of the pump, hence forcing people to take water from somewhere else. John Snow noted a drastic reduction in the number of deaths in the subsequent days. Since the water coming to the surrounding pumps was from the same source, Snow concluded that the pipes connected to pump in Broad Street must have been contaminated with sewage.

After the cholera epidemic stopped, government officials replaced the pump handle, refusing John Snow's theory. It will take time for his theories to be accepted.

In 1992, a replica of the pump with the handle removed was installed at the site of the 1854 pump (figure {numref}`pump`).

```{figure} /_static/lecture_specific/lecture1/broad_street_pump_handle.jpeg
---
name: pump
---
The replica of the pump with the handle removed installed in 1992. Image from https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak
```

## The Bad: Proving Nonexistent Links Between MMR Vaccines and Autism
In 1998, Andrew Wakefield and twelve coauthors published a paper entitled "Ileal-lymphoid-nodular hyperplasia, non-specific colitis, and pervasive developmental disorder in children" in The Lancet (one of the most important medical Journals). The paper claimed the existence of a causative link between the MMR vaccine and colitis and between colitis and autism.

```{figure} /_static/lecture_specific/lecture1/retracted.png
---
name: retracted
---
The paper published in the Lancet, and later retracted. From https://www.thelancet.com/journals/lancet/article/PIIS0140673697110960/fulltext.
```

Several studies (at least 20) tried to replicate  Wakefield's study and where not able to show any link between vaccine and autism, hence assessing that there is no associated between the two. 

Some facts about the paper:
* The study was based on 12 children, which had been carefully selected to allow to verify the claim. Many of their parents already believed that the MMR vaccination had caused their children's autism.
* Wakefield had not disclosed a serious financial conflict: he had been paid by lawyers involved in lawsuits against immunization manufacturers and was applying for a new vaccine patent.
* In 2004, 10 of the 13 authors retracted their support for the MMR-autism association.
* Britain’s General Medical Council investigation found Wakefield guilty of dishonesty and irresponsibility.

In 2010, the Lancet fully retracted the Wakefield study (see {ref}`retracted`).

Despite the fraudulent nature of this data analysis has now been uncovered, the paper had a profound impact on the rate of immunizations which decreased dramatically, with increased risks for children (see {ref}`mmrcoverage`). 

```{figure} /_static/lecture_specific/lecture1/mmr_coverage.jpg
---
name: mmrcoverage
---
MMR vaccination coverage in relationship with the publication of Wakefield's paper.
© Tangled Bank Studios; data from the National Health Service of the United Kingdom. Image from https://www.pbs.org/wgbh/nova/article/autism-vaccine-myth/
```

This is an example of how a fraudulent data analysis can be crafted in a convincing way (the paper was accepted by The Lancet!) and what kind of damage it can do to society.

More information about this story here:
* https://en.wikipedia.org/wiki/Lancet_MMR_autism_fraud
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2954080/


## The Ugly: Manipulating Voters with Stolen Data - The Facebook-Cambridge Analytica Scandal

In 2013, a company called Cambridge Analytica ({numref}`cambridge_analytica`) was founded with the intention of utilizing data analysis and strategic communication to influence political campaigns. Their claimed expertise lay in psychographic profiling, a method that categorizes individuals based on their psychological traits and behaviors.

```{figure} /_static/lecture_specific/lecture1/cambridge_analytica.png
---
name: cambridge_analytica
---
Image from https://en.wikipedia.org/wiki/Cambridge_Analytica
```

In 2014, Aleksandr Kogan, a researcher at Cambridge Analytica, developed an app named "This Is Your Digital Life." On the surface, it appeared to be a harmless personality quiz. However, without the consent of the users, the app collected not only their personal data but also the information of their Facebook friends.

Through the "This Is Your Digital Life" app, Cambridge Analytica gained access to an astonishing amount of personal data. They obtained profiles from around 87 million Facebook users, obtaining a vast quantity of information including public profiles, likes, preferences, and more.

```{figure} /_static/lecture_specific/lecture1/bigfive.png
---
name: bigfive
---
Image from https://commons.wikimedia.org/wiki/File:Wiki-grafik_peats-de_big_five_ENG.png
```

Based on this data, Cambridge Analytica employed data analysis techniques to construct detailed psychological profiles of individuals using the Big Five personality traits model (see {numref}`bigfive`). They claimed to possess thousands of data points on each person, enabling them to tailor political messages and advertisements to specific personality types.

As Alexander Nix, the chief executive of Cambridge Analytica claimed:

> Today in the United States we have somewhere close to four or five thousand data points on every individual ... So we model the personality of every adult across the United States, some 230 million people.

(Source https://en.wikipedia.org/wiki/Cambridge_Analytica)

The unethical aspect of Cambridge Analytica's actions lay in their misuse of personal data obtained without proper consent. Furthermore, their involvement in political campaigns raised concerns about potential manipulation of democratic processes through targeted misinformation and propaganda.

The scandal erupted into the public eye in 2018, when investigations exposed Cambridge Analytica's practices. The revelation sparked a massive outcry over privacy violations, ethical standards, and the regulation of data analytics. Facebook, being the platform from which the data was harvested, faced intense scrutiny for their failure to safeguard user data and prevent unauthorized access. The scandal triggered investigations by regulatory bodies and lawmakers, leading to increased calls for stricter data protection regulations.

The story of the Cambridge Analytica scandal is a good example of the risks associated with unethical data practices.