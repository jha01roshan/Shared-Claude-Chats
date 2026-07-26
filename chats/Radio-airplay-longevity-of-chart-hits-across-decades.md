# Radio airplay longevity of chart hits across decades

- Source: https://claude.ai/share/e4d9b668-4a4b-487e-a80f-05b6e9ec1a07
- Author: Karl
- Created: 2026-04-19
- Messages: 2

---

## Human

I do have an assumption that might be wrong or right. I want you to think about it if you are able to find the right data that proves or contradicts that assumption.
Please do list all relevant sources in your answer so that this can be checked.
The assumption is: Top 10 chart hits of the more recent years will be played less often in public radio than top 10 chart hits from previous decades such as 70s to 90s. This is because an average top 10 chart song is no longer interesting after a couple of weeks or months. In contrast, songs that were popular in 70s-90s do have a higher popularity after the same amount of time.
In other words: within the same timely "distance", songs that were in the top 10 charts, e.g., in the 80s are played more often within the same time range after their chart positions.
If you check that assumption, you need to normalize the time ranges because a song, e.g., from the 80s had more chances to be played in public radio as there were more years since its peak in the 80s. So the total overall playback numbers are surely the wrong metric.
I would suggest to analyze the top 10 chart positions, ignore some time-frame in-between, and check what their chances were to be played again in a time-frame - for example - 5 years after their top chart position. This is just a rough idea and you may change the variables or method if you do find a better approach to check the assumption.
If you do think that it's easier to compare only 2 differen time ranges, maybe take (something from) the 80s and (something) after 2015 if feasible as I've got the impression that after 2015, those thow-away songs increased in the charts.
Tell me, if you can't find a good metric, method or the propriate data to check the assumption.

---

## Assistant

# Investigating your assumption about radio longevity of chart hits

This is a genuinely interesting question. Let me think about it carefully, search for relevant data, and tell you honestly what I find — including whether the assumption can be properly tested.

Let me start by searching for relevant research and data sources.
```
This block is not supported on your current device yet.
```

This is already very interesting. There's a paradox in the findings: recent songs are on airplay charts *longer* than before, but streaming peaks *faster*. Let me dig deeper into what's actually happening with catalog/gold radio airplay of older hits.
```
This block is not supported on your current device yet.
```

This is very illuminating. I'm getting strong qualitative evidence already. Let me search for any actual measured data — specifically airplay databases that could let us count.
```
This block is not supported on your current device yet.
```

I have enough to understand the landscape. Let me do one more search to see if there's any publicly-available dataset I could point you to for actually running the analysis yourself.
```
This block is not supported on your current device yet.
```

I now have a very good picture. I have enough information to give you a thoughtful, honest answer. Let me stop searching and write up what I found.

---

# My honest answer

**Your intuition is probably right — but it's worth understanding *why* the data to prove it cleanly is hard to get, and where the qualitative evidence points.**

Let me separate three things: (1) what the evidence says, (2) whether your proposed method works, and (3) what I'd actually recommend if you want to run the analysis yourself.

## 1. What the evidence suggests

There are several well-documented findings that, taken together, strongly support your assumption — though none is a direct clean test of it.

**Finding A: Chart lifetimes have diverged sharply by rank.** A 2024 paper analyzing 65 years of Billboard Hot 100 data found that "most songs spend less time on the chart now than songs did in the past," while top-1 songs have tripled their chart lifetime since the 1960s, the highest-ranked songs maintain their positions for far longer than previously, and the lowest-ranked songs are replaced more frequently than ever. This matches your intuition about "throw-away songs" — but it's about chart behavior, not long-term radio afterlife.

**Finding B: A separate study across US/UK/German/Dutch charts found that album lifetimes shifted from a log-normal to a power-law distribution** — meaning a few mega-hits dominate while most songs disappear almost immediately. The authors attribute this to a decoupling of individual time horizons from decision-making enabled by streaming.

**Finding C: The decisive qualitative evidence is the Classic Hits radio format itself.** This is probably the most important data point for your question. Classic Hits is a radio format which generally includes songs from the top 40 music charts from the late 1960s to the early 2000s, with music from the 1980s serving as the core of the format, and as of December 2019, there are now over 1,100 classic hits stations in the United States, the largest amount in format history. So there's an entire multi-billion-dollar radio segment explicitly built on replaying 70s–90s top 10 hits decades later. There is no equivalent format for mid-2010s pop.

**Finding D: Programmers themselves report difficulty finding 90s and 2000s songs that "work."** In industry interviews, a VP of Classic Hits Programming said when you look at the top 500 songs, there are only seven songs from the '90s or newer, and the '90s don't provide as many opportunities as we would like, but there's not a ton of opportunity within the 2000s either. When industry professionals whose job is to select catalog hits say newer decades produce fewer format-viable songs, that's direct anecdotal support for your assumption.

**Finding E: There's a real paradox to be aware of.** Recent hits actually stay on *airplay charts* longer than before — a spate of longevity records set by songs of recent vintage on Billboard's radio airplay charts during the last two years suggests that the medium is supporting hits for greater periods of time. But this is the *first run* lasting longer, not the long-term afterlife. The same article notes that UMG's top 300 singles peaked on streaming platforms twice as fast in 2018 as they did in 2017 — five weeks versus 10 weeks. So radio is increasingly a retention tool, not a discovery tool — which is consistent with recent songs having a long first run followed by a steep cliff, while 80s hits just keep returning in rotation forever.

So the qualitative picture strongly supports you. Whether it holds quantitatively at the exact "5 years after peak" comparison you proposed is a separate question.

## 2. Does your method work?

Your proposed method is actually quite good — the core idea (normalize by comparing same time-since-peak windows, not absolute play counts) is exactly the right statistical instinct. But there are three subtleties worth naming:

**Subtlety 1: Survivorship and format drift.** A 1985 song being played on a Classic Hits station in 1990 (5 years later) is not really comparable to a 2018 song being played on a Top 40 station in 2023. The *format categories themselves* have shifted. In the early 90s, Classic Hits barely existed; gold rotation happened on AC/oldies stations with different criteria. A cleaner comparison is "plays on any monitored station" — but then you're mixing apples (active rotation) and oranges (catalog rotation).

**Subtlety 2: The total radio audience has changed.** Total broadcast radio listenership has shrunk significantly since the 90s. So a song played X times in 2023 reaches fewer people than X times in 1990. You'd want plays *per monitored station per week*, not raw totals.

**Subtlety 3: Monitoring coverage itself changed.** During the 1960s and 1970s, Billboard continued to collect airplay data as a component of the Hot 100 but did not make the chart public, and BDS monitors airplay on more than 2,000 radio stations — but the number of stations, the fingerprinting technology, and the coverage have all evolved. So 80s data is much sparser than 2020s data.

With those caveats, your 5-years-after-peak comparison is still a reasonable framing. I'd suggest checking year 5, year 10, and year 15 to see the decay curve.

## 3. The hard part: data access

Here is where I have to tell you something disappointing. **The granular historical data you need is almost entirely behind paywalls.** The useful databases are:

- **Mediabase / Luminate (formerly Nielsen BDS)** — the industry standard; subscription only, thousands of dollars per year
- **Soundcharts, WARM, Digital Radio Tracker, Play MPE MTR** — commercial tools; all paid subscriptions
- **Billboard chart archives** — Billboard's Radio Songs chart exists back to October 1984 but historical data isn't easily exportable; kworb.net has some scrapable current-era data

I could not find a free, downloadable dataset that gives song-level weekly radio spins going back to the 1980s. If you know of a university library that subscribes to Luminate or a research partnership, that'd be the path. Without that, you're stuck with proxies.

## What I'd actually recommend if you want to do this yourself

Three feasible approaches, roughly in order of effort:

**Approach 1 (easy, proxy-only): Billboard Hot 100 recurrent re-entries.** You can scrape Wikipedia or Billboard year-end lists and count how many top-10 hits from year X re-enter or persist into the chart in year X+5, X+10, etc. This is a weak proxy for radio airplay but it's completely free. You'd want to compare, say, 1985 top 10 hits (how many appeared on any Hot 100 chart in 1990-1992?) vs. 2015 top 10 hits (how many in 2020-2022?). The Billboard chart incorporates airplay heavily, so it's not nothing.

**Approach 2 (medium effort): Spotify / YouTube popularity decay.** Not radio, but a reasonable proxy for sustained cultural interest. You can get play counts and monthly listener counts from the Spotify API for free. Compare the ratio (current streams) / (peak-era streams) for 80s top 10 hits vs. mid-2010s top 10 hits. This is actually a *better* metric for your underlying question of "are these songs still interesting years later," even if it's not strictly radio.

**Approach 3 (hardest): Sample current radio playlists yourself.** Pick 5–10 major radio stations across formats, scrape their "recently played" pages for a month (most stations publish these), and bucket every song by its original chart-peak year. Then compute the share of plays going to each year/decade. This gives you a real, current snapshot of how often 80s vs. mid-2010s top-10 hits are played *today*. It doesn't do the "5 years after peak" comparison directly, but it's the most honest current-state measurement and it's achievable as a Python project. Libraries like `requests` + `beautifulsoup` + a station list will get you most of the way there.

If you want, I can help you build approach 2 or 3 — approach 3 is a nice weekend Python project and would probably give you the cleanest answer to the "which decade dominates radio today" question.

## Bottom line

Your assumption is almost certainly correct in direction, and the existence of the booming Classic Hits format is the single strongest piece of evidence for it. However, I could not find a clean, free, quantitative dataset that proves it with the exact methodology you described (normalized 5-year-after-peak comparison). The proprietary data exists — it sits in Luminate/Mediabase — but it's not publicly accessible. If you want to check it yourself with public data, scraping recently-played lists from current radio stations is the most tractable approach.

## Sources used

1. Lorenz-Spreen et al., "Accelerating dynamics of collective attention" / music-charts paper — https://arxiv.org/pdf/1908.10694 and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6731713/
2. "Is it getting harder to make a hit? Evidence from 65 years of US music chart history" — https://arxiv.org/pdf/2405.07574
3. Wikipedia, "Pop Airplay" — https://en.wikipedia.org/wiki/Pop_Airplay
4. Wikipedia, "Radio Songs (chart)" — https://en.wikipedia.org/wiki/Radio_Songs_(chart)
5. Wikipedia, "Classic hits" — https://en.wikipedia.org/wiki/Classic_hits
6. Wikipedia, "Broadcast Data Systems" — https://en.wikipedia.org/wiki/Broadcast_Data_Systems
7. Billboard, "Hit Songs Are Staying On The Radio Airplay Charts Longer" — https://www.billboard.com/articles/deep-dive/the-state-of-radio/8530061/hit-songs-are-staying-on-the-radio-airplay-charts
8. Bridge Ratings, "Radio & Music Streaming — A Feedback Loop" (May 2025) — https://www.bridgeratings.com/blog/2025/5/10/radio-music-streaming-a-feedback-loop
9. RadioInsight, "What Classic Hits Stations Added In 2024" — https://radioinsight.com/blogs/267845/what-classic-hits-stations-added-in-2024/
10. RadioInsight, "The Other Half of Classic Hits" — https://radioinsight.com/blogs/208434/the-other-half-of-classic-hits/
11. InsideRadio, "What's The Musical Future Of An 'Oldies' Format?" — https://www.insideradio.com/what-s-the-musical-future-of-an-oldies-format/article_6b2cea32-de5b-11e7-9be3-dbdfcd175949.html
12. Powergold, "How To Make Your Gold-Based Format Shine" — https://www.powergold.com/2019/09/12/how-to-make-your-gold-based-format-shine-part-1/
13. Watson, "Gender Representation on Country Format Radio" (SongData, 2019) — https://songdata.ca/wp-content/uploads/2019/04/SongData-Watson-Country-Airplay-Study-FullReport-April2019.pdf
14. Dertouzos, "Radio Airplay and the Record Industry: An Economic Analysis" (NAB) — http://www.nab.org/documents/resources/061008_dertouzos_Ptax.pdf
15. kworb.net Radio Songs estimates — https://kworb.net/radio/

Want me to help you build the Python scraper for approach 3?
