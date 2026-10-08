# GAIN World Food Day 2026: handover notes

Owner: Peddy Oniango (GAIN Communications) · Last updated: 8 October 2026
World Food Day: **Friday 16 October 2026** · FAO theme: **"Innovate today. Nourish tomorrow."**

This pack holds everything made so far, so the work can continue in a new session (for example Claude Code on API credits). Read this file first.

---

## 1. Where things stand

| Workstream | Status | Files |
|---|---|---|
| Campaign concept note | Done (v4); Peddy has a newer, hand-edited Word copy | `final_outputs/GAIN_World_Food_Day_2026_Concept_Note_v4.docx` |
| Team briefing deck + speaker notes | Done (15 slides, GAIN template, feedback applied) | `final_outputs/GAIN_World_Food_Day_2026_Team_Briefing.pptx`, rebuild scripts in `deck/` |
| Photo frame (A2) | Final, print-ready CMYK | `final_outputs/GAIN_WFD2026_Photo_Frame_A2_CMYK.pdf` |
| Placard, red + white (A2) | Final, print-ready CMYK | `final_outputs/GAIN_WFD2026_Placard_*_A2_CMYK.pdf` |
| QR stickers (A4, 20 per sheet) | Final | `final_outputs/GAIN_WFD2026_QR_Stickers_A4.pdf` |
| Guide for comms leads + HR focal points | Final, 2 placeholders left (see 4) | `final_outputs/GAIN_WFD2026_Frame_and_Placard_Guide.docx` |
| **Pillar carousels for next week** | **To do** | see 5 |
| **Concept note / brief for the flagship video editors** | **To do** | see 5 |

Older versions are in `final_outputs/_superseded/`.

---

## 2. Campaign in one paragraph

Working concept: **"Innovation that nourishes."** Three pillars tell one story, with GAIN's AI strategy running through all three:

| Pillar | Lead item | Supporting | Podcast clip | AI thread |
|---|---|---|---|---|
| 1. Know what nourishes (evidence and data) | Priority Micronutrient Density list (Ty Beal) | Food Systems Dashboard; Diet Quality Questionnaire (DQQ) | Bite the Talk EP 26 | Design |
| 2. Make systems deliver (technology and policy) | DFQT+ digital fortification traceability | Nutrition Futures Initiative | EP 30 | Delivery |
| 3. Back the innovators (businesses and youth) | NourishNext West Africa youth innovation challenge | N3F; MSME Week stories (Nutribaik = climate angle; I-CAN, Anthony) | EP 33 (Aida Eyasu) | Scale |

- Main audience: governments and policymakers (also donors, businesses/MSMEs, researchers, public/youth).
- Rollout: teasers 12 to 15 Oct (one pillar per day) · 16 Oct flagship video + web page (Gloria Ireri) · deep dives 17 to 23 Oct.
- Rules: one colour and icon per pillar, one card template, lead item first, same pillar order everywhere, one campaign hashtag + #WorldFoodDay.
- Still open: campaign hashtag (not agreed), how GAIN's new/evolving strategy is tied in (document not yet shared), DFQT+ spokesperson, budget (Tanvi Sood).

Key sources: FAO WFD page https://www.fao.org/world-food-day/en/ · GAIN AI strategy https://www.gainhealth.org/gains-strategy-harnessing-artificial-intelligence-programmes · NourishNext https://nutritionconnect.org/west-africa-youth-agrifood-innovation-challenge-2026-en · DFQT+ https://www.gainhealth.org/digital-fortification-quality-traceability · N3F 2025 impact https://www.gainhealth.org/blogs/n3fs-2025-nutrition-impact-scaling-access-affordable-nutritious-foods-across-sub-saharan · Podcasts https://www.gainhealth.org/resources/multimedia/bite-talk-gain-podcast-series

---

## 3. Brand rules used (from GAIN Brand Identity Guidelines)

| Colour | HEX | CMYK |
|---|---|---|
| GAIN Red | #98103A | 0 / 78 / 31 / 43 |
| White | #FFFFFF | 0 / 0 / 0 / 0 |
| Black | #1D1D1B | 50 / 40 / 40 / 100 |
| Grey | #B9B8B8 | 0 / 0 / 0 / 37 |
| Yellow (secondary) | #FFD80D | 0 / 15 / 95 / 0 |

Font: Montserrat (headings bold, ALL CAPS; body regular). Avenir only where Montserrat isn't available. British English, day-month-year dates. Logo: white on red or red on white; don't recolour/stretch; guidelines prefer it left or right aligned (Peddy chose centred on the frame/placard).

---

## 4. Frame, placard and QR: details

**Final size: A2 landscape (59.4 × 42 cm)** for all three. Frame window ≈ 47.5 × 25.5 cm; placard writing box ≈ 47.5 × 11 cm.

- Frame layout: top "INNOVATE TODAY. NOURISH TOMORROW." · left side "GREETINGS FROM GAIN" · right side "16 OCTOBER 2026 · #WORLDFOODDAY" · bottom centred GAIN logo | "HAPPY / WORLD FOOD DAY".
- Placard: same top/bottom system; "HAPPY / WORLD FOOD DAY" left, salad-bowl line drawing right (from `design/assets/bowl_lineart_source.ai`), large "GREETINGS FROM GAIN" write-in box; **country name only** (no personal names). White version: bowl and box border in black.
- Google Drive: print files https://drive.google.com/drive/folders/1t1oD5D78Q39vkthJTdIrbr5pX-vsydsZ · submissions https://drive.google.com/drive/folders/1RFKq5NJ1LSXvxx9V7kbRnecj1sM_-JS3
- QR code → submissions folder (verified scanning). Stickers 4.2 × 4.8 cm: frame = back of bottom border near a corner; placard = back, top-right corner. QR pixels forced to 100% K in the print PDF.
- Upload deadline in materials: **14 October 2026**; file naming e.g. `KENYA_1.jpg`.

**Left to finalise**
1. Guide: replace "[name, email]" contact placeholder (last section).
2. Submissions folder sharing must allow uploads by anyone with the link.
3. Optional: swap the PNG logo for a vector logo from GAIN brand assets (sharper at A2).
4. Upload the A2 PDFs, sticker sheet and guide to the print files folder; remove superseded files there.

**Rebuild**: edit `design/frame.html` / `design/placard.html` / `design/qr/stickers.html`, then run `design/build_print_files.sh` (needs node+playwright, python3 with pypdf/pikepdf/numpy, ghostscript). `tools/to_cmyk.py` converts to CMYK and snaps colours to the exact brand values.

---

## 5. Next tasks (brief for the next session)

### A. Pillar carousels (for next week)
- One carousel per pillar (3 in total), plus optionally one AI-thread carousel. 3 to 5 slides each, square 1080 × 1080 (or 1080 × 1350 for Instagram).
- Structure per carousel: hook slide (a striking fact, not GAIN's name) → the problem → what GAIN built (lead item) → supporting item(s) → what changed / one number → "what AI adds next" line → call to action + link to the campaign web page.
- Brand: GAIN red/white, yellow accent, Montserrat, squiggly line drawings; one consistent colour/icon per pillar.
- Confirm with the team: what content already exists (Ty Beal carousel exists; N3F videos exist; AI strategy videos/carousels/blog exist; DFQT+ has nothing public yet), the campaign hashtag, and number of slides.
- Build approach that worked: HTML + Montserrat → Playwright screenshots/PDF.

### B. Concept note / brief for the flagship video editors
- 60 to 90 seconds; cut-downs: 30-second teaser, 15-second social clips, one short clip per pillar.
- Arc: problem (diets lacking key nutrients) → innovations by pillar (evidence/data, tech/policy, businesses/youth) → result → close on AI strategy and "Innovate today. Nourish tomorrow."
- Voices: GAINer/voice-over on the evidence; one MSME founder (MSME Week footage: Kennie O. Cold Chain, Whey2Value, Nutribaik); podcast audio (EP 26, 30, 33) as optional bites.
- Brief should include: objective, audience, key message, structure with timings, shot/asset list and sources, on-screen text, music/tone, brand rules (section 3), formats/aspect ratios (16:9, 1:1, 9:16), captions/subtitles, delivery dates (video needed for 16 Oct launch; teaser 12 Oct).

### C. Other open items
- Internal all-staff email before WFD; country teams' ideas for the photo competition; budget (Tanvi Sood); CASCADE separate campaign (legacy angle; ends Dec 2026).

---

## 6. Folder map

```
HANDOVER.md                 this file
final_outputs/              latest deliverables (_superseded/ = older versions)
design/                     HTML sources for frame, placard, QR stickers + assets + build script
deck/                       python-pptx scripts and GAIN PPT template used for the briefing deck
tools/to_cmyk.py            RGB → CMYK conversion with exact brand values
```
