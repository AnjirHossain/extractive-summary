### Overview

This repo expores rapid-prototyping [extractive](https://ieeexplore.ieee.org/abstract/document/8817040)/[abstractive](https://ai.googleblog.com/2016/08/text-summarization-with-tensorflow.html) text summarization methods. Primary method used for extractive summarization is [cosine similarity](https://www.tensorflow.org/api_docs/python/tf/keras/losses/CosineSimilarity) and [ranking](https://arxiv.org/abs/1703.09902v1). Currently the application is wrapped in a REST API, plans for next features includes wrapping in protobuf/grpc system for much faster api calls, using pre-trained word2vec systems, and caching.

### Dependencies:

- Docker
- Docker compose
- python 3

### Intructions to run:

1) `docker-compose build`
2) `docker-compose up`
3) App running on port http://0.0.0.0:80/
4) Post to http://0.0.0.0:80/api/v1/getsummary using: 
  `
    {
      "text": "Text you wish to summarize"
    }
  `
  
### Example results:
 
Prod url:
[https://nlprnd.com/api/v1/getsummary](https://nlprnd.com/api/v1/getsummary)

Test data for prod:
`{
	"text": "when the virus came here, it found a country with serious underlying conditions, and it exploited them ruthlessly. Chronic ills—a corrupt political class, a sclerotic bureaucracy, a heartless economy, a divided and distracted public—had gone untreated for years. We had learned to live, uncomfortably, with the symptoms. It took the scale and intimacy of a pandemic to expose their severity—to shock Americans with the recognition that we are in the high-risk category.The crisis demanded a response that was swift, rational, and collective. The United States reacted instead like Pakistan or Belarus—like a country with shoddy infrastructure and a dysfunctional government whose leaders were too corrupt or stupid to head off mass suffering. The administration squandered two irretrievable months to prepare. From the president came willful blindness, scapegoating, boasts, and lies. From his mouthpieces, conspiracy theories and miracle cures. A few senators and corporate executives acted quickly—not to prevent the coming disaster, but to profit from it. When a government doctor tried to warn the public of the danger, the White House took the mic and politicized the message.Every morning in the endless month of March, Americans woke up to find themselves citizens of a failed state. With no national plan—no coherent instructions at all—families, schools, and offices were left to decide on their own whether to shut down and take shelter. When test kits, masks, gowns, and ventilators were found to be in desperately short supply, governors pleaded for them from the White House, which stalled, then called on private enterprise, which couldn’t deliver. States and cities were forced into bidding wars that left them prey to price gouging and corporate profiteering. Civilians took out their sewing machines to try to keep ill-equipped hospital workers healthy and their patients alive. Russia, Taiwan, and the United Nations sent humanitarian aid to the world’s richest power—a beggar nation in utter chaos.Donald Trump saw the crisis almost entirely in personal and political terms. Fearing for his reelection, he declared the coronavirus pandemic a war, and himself a wartime president. But the leader he brings to mind is Marshal Philippe Pétain, the French general who, in 1940, signed an armistice with Germany after its rout of French defenses, then formed the pro-Nazi Vichy regime. Like Pétain, Trump collaborated with the invader and abandoned his country to a prolonged disaster. And, like France in 1940, America in 2020 has stunned itself with a collapse that’s larger and deeper than one miserable leader. Some future autopsy of the pandemic might be called Strange Defeat, after the historian and Resistance fighter Marc Bloch’s contemporaneous study of the fall of France. Despite countless examples around the U.S. of individual courage and sacrifice, the failure is national. And it should force a question that most Americans have never had to ask: Do we trust our leaders and one another enough to summon a collective response to a mortal threat? Are we still capable of self-government? This is the third major crisis of the short 21st century. The first, on September 11, 2001, came when Americans were still living mentally in the previous century, and the memory of depression, world war, and cold war remained strong. On that day, people in the rural heartland did not see New York as an alien stew of immigrants and liberals that deserved its fate, but as a great American city that had taken a hit for the whole country. Firefighters from Indiana drove 800 miles to help the rescue effort at Ground Zero. Our civic reflex was to mourn and mobilize together. Partisan politics and terrible policies, especially the Iraq War, erased the sense of national unity and fed a bitterness toward the political class that never really faded. The second crisis, in 2008, intensified it. At the top, the financial crash could almost be considered a success. Congress passed a bipartisan bailout bill that saved the financial system. Outgoing Bush-administration officials cooperated with incoming Obama administration officials. The experts at the Federal Reserve and the Treasury Department used monetary and fiscal policy to prevent a second Great Depression. Leading bankers were shamed but not prosecuted; most of them kept their fortunes and some their jobs. Before long they were back in business. A Wall Street trader told me that the financial crisis had been a “speed bump.” All of the lasting pain was felt in the middle and at the bottom, by Americans who had taken on debt and lost their jobs, homes, and retirement savings. Many of them never recovered, and young people who came of age in the Great Recession are doomed to be poorer than their parents. Inequality—the fundamental, relentless force in American life since the late 1970s—grew worse. This second crisis drove a profound wedge between Americans: between the upper and lower classes, Republicans and Democrats, metropolitan and rural people, the native-born and immigrants, ordinary Americans and their leaders. Social bonds had been under growing strain for several decades, and now they began to tear. The reforms of the Obama years, important as they were—in health care, financial regulation, green energy—had only palliative effects. The long recovery over the past decade enriched corporations and investors, lulled professionals, and left the working class further behind. The lasting effect of the slump was to increase polarization and to discredit authority, especially government’s. Both parties were slow to grasp how much credibility they’d lost. The coming politics was populist. Its harbinger wasn’t Barack Obama but Sarah Palin, the absurdly unready vice-presidential candidate who scorned expertise and reveled in celebrity. She was Donald Trump’s John the Baptist. David Frum: This is Trump’s fault Trump came to power as the repudiation of the Republican establishment. But the conservative political class and the new leader soon reached an understanding. Whatever their differences on issues like trade and immigration, they shared a basic goal: to strip-mine public assets for the benefit of private interests. Republican politicians and donors who wanted government to do as little as possible for the common good could live happily with a regime that barely knew how to govern at all, and they made themselves Trump’s footmen. Like a wanton boy throwing matches in a parched field, Trump began to immolate what was left of national civic life. He never even pretended to be president of the whole country, but pitted us against one another along lines of race, sex, religion, citizenship, education, region, and—every day of his presidency—political party. His main tool of governance was to lie. A third of the country locked itself in a hall of mirrors that it believed to be reality; a third drove itself mad with the effort to hold on to the idea of knowable truth; and a third gave up even trying. Trump acquired a federal government crippled by years of right-wing ideological assault, politicization by both parties, and steady defunding. He set about finishing off the job and destroying the professional civil service. He drove out some of the most talented and experienced career officials, left essential positions unfilled, and installed loyalists as commissars over the cowed survivors, with one purpose: to serve his own interests. His major legislative accomplishment, one of the largest tax cuts in history, sent hundreds of billions of dollars to corporations and the rich. The beneficiaries flocked to patronize his resorts and line his reelection pockets. If lying was his means for using power, corruption was his end. Read: The coronavirus’s real and immediate threat to democracy This was the American landscape that lay open to the virus: in prosperous cities, a class of globally connected desk workers dependent on a class of precarious and invisible service workers; in the countryside, decaying communities in revolt against the modern world; on social media, mutual hatred and endless vituperation among different camps; in the economy, even with full employment, a large and growing gap between triumphant capital and beleaguered labor; in Washington, an empty government led by a con man and his intellectually bankrupt party; around the country, a mood of cynical exhaustion, with no vision of a shared identity or future. If the pandemic really is a kind of war, it’s the first to be fought on this soil in a century and a half. Invasion and occupation expose a society’s fault lines, exaggerating what goes unnoticed or accepted in peacetime, clarifying essential truths, raising the smell of buried rot. The virus should have united Americans against a common threat. With different leadership, it might have. Instead, even as it spread from blue to red areas, attitudes broke down along familiar partisan lines. The virus also should have been a great leveler. You don’t have to be in the military or in debt to be a target—you just have to be human. But from the start, its effects have been skewed by the inequality that we’ve tolerated for so long. When tests for the virus were almost impossible to find, the wealthy and connected—the model and reality-TV host Heidi Klum, the entire roster of the Brooklyn Nets, the president’s conservative allies—were somehow able to get tested, despite many showing no symptoms. The smattering of individual results did nothing to protect public health. Meanwhile, ordinary people with fevers and chills had to wait in long and possibly infectious lines, only to be turned away because they weren’t actually suffocating. An internet joke proposed that the only way to find out whether you had the virus was to sneeze in a rich person’s face. When Trump was asked about this blatant unfairness, he expressed disapproval but added, “Perhaps that’s been the story of life.” Most Americans hardly register this kind of special privilege in normal times. But in the first weeks of the pandemic it sparked outrage, as if, during a general mobilization, the rich had been allowed to buy their way out of military service and hoard gas masks. As the contagion has spread, its victims have been likely to be poor, black, and brown people. The gross inequality of our health-care system is evident in the sight of refrigerated trucks lined up outside public hospitals. We now have two categories of work: essential and nonessential. Who have the essential workers turned out to be? Mostly people in low-paying jobs that require their physical presence and put their health directly at risk: warehouse workers, shelf-stockers, Instacart shoppers, delivery drivers, municipal employees, hospital staffers, home health aides, long-haul truckers. Doctors and nurses are the pandemic’s combat heroes, but the supermarket cashier with her bottle of sanitizer and the UPS driver with his latex gloves are the supply and logistics troops who keep the frontline forces intact. In a smartphone economy that hides whole classes of human beings, we’re learning where our food and goods come from, who keeps us alive. An order of organic baby arugula on AmazonFresh is cheap and arrives overnight in part because the people who grow it, sort it, pack it, and deliver it have to keep working while sick. For most service workers, sick leave turns out to be an impossible luxury. It’s worth asking if we would accept a higher price and slower delivery so that they could stay home. The pandemic has also clarified the meaning of nonessential workers. One example is Kelly Loeffler, the Republican junior senator from Georgia, whose sole qualification for the empty seat that she was given in January is her immense wealth. Less than three weeks into the job, after a dire private briefing about the virus, she got even richer from the selling-off of stocks, then she accused Democrats of exaggerating the danger and gave her constituents false assurances that may well have gotten them killed. Loeffler’s impulses in public service are those of a dangerous parasite. A body politic that would place someone like this in high office is well advanced in decay. The purest embodiment of political nihilism is not Trump himself but his son-in-law and senior adviser, Jared Kushner. In his short lifetime, Kushner has been fraudulently promoted as both a meritocrat and a populist. He was born into a moneyed real-estate family the month Ronald Reagan entered the Oval Office, in 1981—a princeling of the second Gilded Age. Despite Jared’s mediocre academic record, he was admitted to Harvard after his father, Charles, pledged a $2.5 million donation to the university. Father helped son with $10 million in loans for a start in the family business, then Jared continued his elite education at the law and business schools of NYU, where his father had contributed $3 million. Jared repaid his father’s support with fierce loyalty when Charles was sentenced to two years in federal prison in 2005 for trying to resolve a family legal quarrel by entrapping his sister’s husband with a prostitute and videotaping the encounter. Francis Fukuyama: The thing that determines a country’s resistance to the coronavirus Jared Kushner failed as a skyscraper owner and a newspaper publisher, but he always found someone to rescue him, and his self-confidence only grew. In American Oligarchs, Andrea Bernstein describes how he adopted the outlook of a risk-taking entrepreneur, a “disruptor” of the new economy. Under the influence of his mentor Rupert Murdoch, he found ways to fuse his financial, political, and journalistic pursuits. He made conflicts of interest his business model. So when his father-in-law became president, Kushner quickly gained power in an administration that raised amateurism, nepotism, and corruption to governing principles. As long as he busied himself with Middle East peace, his feckless meddling didn’t matter to most Americans. But since he became an influential adviser to Trump on the coronavirus pandemic, the result has been mass death. In his first week on the job, in mid-March, Kushner co-authored the worst Oval Office speech in memory, interrupted the vital work of other officials, may have compromised security protocols, flirted with conflicts of interest and violations of federal law, and made fatuous promises that quickly turned to dust. “The federal government is not designed to solve all our problems,” he said, explaining how he would tap his corporate connections to create drive-through testing sites. They never materialized. He was convinced by corporate leaders that Trump should not use presidential authority to compel industries to manufacture ventilators—then Kushner’s own attempt to negotiate a deal with General Motors fell through. With no loss of faith in himself, he blamed shortages of necessary equipment and gear on incompetent state governors. To watch this pale, slim-suited dilettante breeze into the middle of a deadly crisis, dispensing business-school jargon to cloud the massive failure of his father-in-law’s administration, is to see the collapse of a whole approach to governing. It turns out that scientific experts and other civil servants are not traitorous members of a “deep state”—they’re essential workers, and marginalizing them in favor of ideologues and sycophants is a threat to the nation’s health. It turns out that “nimble” companies can’t prepare for a catastrophe or distribute lifesaving goods—only a competent federal government can do that. It turns out that everything has a cost, and years of attacking government, squeezing it dry and draining its morale, inflict a heavy cost that the public has to pay in lives. All the programs defunded, stockpiles depleted, and plans scrapped meant that we had become a second-rate nation. Then came the virus and this strange defeat. Read: Trump’s coronavirus message is revisionist history The fight to overcome the pandemic must also be a fight to recover the health of our country, and build it anew, or the hardship and grief we’re now enduring will never be redeemed. Under our current leadership, nothing will change. If 9/11 and 2008 wore out trust in the old political establishment, 2020 should kill off the idea that anti-politics is our salvation. But putting an end to this regime, so necessary and deserved, is only the beginning. We’re faced with a choice that the crisis makes inescapably clear. We can stay hunkered down in self-isolation, fearing and shunning one another, letting our common bond wear away to nothing. Or we can use this pause in our normal lives to pay attention to the hospital workers holding up cellphones so their patients can say goodbye to loved ones; the planeload of medical workers flying from Atlanta to help in New York; the aerospace workers in Massachusetts demanding that their factory be converted to ventilator production; the Floridians standing in long lines because they couldn’t get through by phone to the skeletal unemployment office; the residents of Milwaukee braving endless waits, hail, and contagion to vote in an election forced on them by partisan justices. We can learn from these dreadful days that stupidity and injustice are lethal; that, in a democracy, being a citizen is essential work; that the alternative to solidarity is death. After we’ve come out of hiding and taken off our masks, we should not forget what it was like to be alone."
}`

