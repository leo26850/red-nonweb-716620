# -*- coding: utf-8 -*-
S="https://docs.google.com/spreadsheets/d/%s/edit"
F="https://drive.google.com/file/d/%s/view"
R={
"LEADS":("HubSpot Leads",S%"11kx_D76BqR7ZdxxX5XFXTNQz3kXg130tU03kbcu975I",0),
"ROADMAP":("Roadmap",S%"12Qxsij-zd-i0YRZEUUJrdy4i6_NUQbhJXF-DveN2PTg",0),
"TRACKER":("Target Tracker",S%"1t0IqQSnME-dQTK0jsAws4JHeE4kwajG_HnwocrAgrwg",0),
"DOMAINS":("Domains & Accounts",S%"1FLRGdh2saho5EQYMsyFX877fTRd41VzNzX6IYRYXVyg",0),
"EXH":("Exhibitors",S%"1StAcVxmXoQT2fc1V5iF7KPsT53FN1i_HuHEnIHeWaf8",0),
"EVENTS":("Event Lists-100",S%"13WJgCUhWEss1SxEC09rHA-5nkePfUm_N-NyNnlZoNKE",0),
"OHIO":("Ohio OEM",S%"1m29O2WGQ5C0nEJs9PRDpbUBBHMlNhnfKOPEQrrRTzYs",0),
"COLDCALL":("Eric Cold Call List",S%"10cPya6DePu29YDn3CQZFbGm-tP28gYswxlarzG8izjE",0),
"SALES":("Sales Report",S%"1kr_mhcd_vmFq193MwqEUWq26A2nCRuupfvjmG6nUH_g",0),
"CLAIMS":("Content Claims Review",S%"1fYvU8ttKkYnS3eCZTYySDDgz8ZCRZX5m3-8aAdG-h2c",0),
"BRO":("Redstone brochure v4",F%"1_SipSJHFP8CW3u-m6M0HtrHJQCEOMdv6",1),
"DIE":("die-casting.pdf",F%"1jEkgcG9vijfm3PA2_-TAO7iptrcO7V8g",1),
"SAND":("sand-casting.pdf",F%"12-lczXZFZFAUQWSrbyhASQ1AiV4URGju",1),
"INV":("investment-casting.pdf",F%"16bP5aGW4-p6hAdq4WqY7vMCqhkuVMMuM",1),
"CNC":("cnc-machining.pdf",F%"1KzQtsPYP_PjsUoH4vD-SS4CX62oXs3Di",1),
"MIM":("mim.pdf",F%"1g3IEANJ1Z0AjXAFycbIftbV5Vw4WroM-",1),
"SHEET":("sheet-metal.pdf",F%"1pr-4LcpxB9xc12_K8EPCDMlQxNNqmQ_-",1),
}
CATN={"CE":"Cold email","PR":"Prospecting","CRM":"CRM/Attio","RPT":"Reporting","BR":"Brochures/decks","EM":"Email infra","AD":"Ads","MT":"Meetings","OP":"Ops"}

# id: [name, cat, res_key(or None), purpose, usecase, prio, state, date(or None), build(or None), blocked(or None), verify(or None), flag]
I={
"82":["Go Live with Cold Email","CE","DOMAINS","Launch the Redstone cold-email outbound channel into production.","Start generating outbound replies/leads alongside paid search.","none","Done","May 22",None,None,None,0],
"130":["Share Lemlist API key (cold-email stats pipeline)","CE","DOMAINS","Get the Lemlist API key to read cold-email stats programmatically.","Pull sent/open/reply/bounce volume into BigQuery beside the Ads funnel.","high","Done","Jun 3",None,None,None,0],
"68":["Lemlist reply webhook → BigQuery + Slack pipeline","CE",None,"Capture every Lemlist reply, classify sentiment, log to BigQuery.","Route positive/neutral replies to Slack #redstone-cold-email for follow-up.","high","Done","May 22",None,None,None,0],
"103":["Keep ≥1 outbound domain warming in reserve","CE","DOMAINS","Keep 1–2 outbound domains warmed in reserve at all times.","Launch trade-show campaigns instantly without a 4–6 week warm-up.","medium","Backlog",None,None,None,None,0],
"104":["\"Mexico→China switch on discovery\" outbound sequence","CE",None,"Test a cold-email angle leading with Mexico, switching to China on the call.","Convert buyers frustrated with India manufacturing; queued behind core outbound.","low","Backlog",None,None,None,None,0],
"133":["Compile June/July 2026 US industry-event list","PR","EVENTS","Build a date-verified US industry-event list for Jun/Jul 2026.","Feed trade-show targeting and team event registration.","none","Done","Jun 6",None,None,None,0],
"134":["Build exhibitor scraper (Map Your Show + A2Z adapters)","PR","EXH","Automate scraping exhibitor directories (Map Your Show + A2Z/SEMICON).","Turn show exhibitor lists into a prospect pool at scale.","none","Done","Jun 6",None,None,None,0],
"135":["Scrape exhibitor directories → 2,739 companies","PR","EXH","Populate the sheet with 2,739 scraped exhibitor companies.","Raw company pool for Apollo enrichment into contactable buyers.","none","Done","Jun 6",None,None,None,0],
"136":["Phase 2 — Apollo enrichment → decision-maker emails","PR","EXH","Filter exhibitors to ICP buyers; pull buyer/engineering contacts via Apollo People Search UI (no API key needed).","Build the Prospects tab — saved search + CSV export per show; recipe on the Plane task.","high","Todo",None,"build Prospects tab",None,None,0],
"137":["Crack SEMICON pagination + add H2 flagship shows","PR","EXH","Fix SEMICON pagination and add flagship shows (FABTECH, IMTS, NADCA, AUSA).","Maximize scraped exhibitor coverage across major H2 shows.","medium","Todo",None,"extend scraper",None,None,0],
"138":["Enroll team in priority June/July 2026 events","PR","EVENTS","Register the team for high-fit in-window June/July events.","Get Redstone onto show floors before imminent dates pass.","high","Todo",None,None,None,None,0],
"139":["Verify MD&M East 2026 dates with Informa","PR","EVENTS","Confirm the true 2026 MD&M East dates with Informa.","Avoid booking travel against a possibly-wrong 3rd-party date.","medium","Todo",None,None,None,"2026 dates w/ Informa",0],
"140":["Finalize Labs Facility Testing list (+Meta/Google/MS)","PR",None,"Finalize a ~1,100-contact list of tech/hardware firms needing test labs.","Send Eric the vetted list (with Meta/Google/MS added) for outreach.","high","Todo",None,"list to build",None,None,0],
"141":["Expand Aerospace & Defense Apollo list to ~80","PR",None,"Broaden the Aerospace & Defense list to ~80 quality contacts.","Eric personally calls ~10 of them — quality over volume.","medium","Todo",None,"expand list",None,None,0],
"142":["Refine Ohio OEM list (machinery/equipment only)","PR","OHIO","Refine the Ohio list to true machinery/equipment OEMs only.","Clean targeting for Brandon/Rachel outreach (drop product companies).","medium","Todo",None,"refine",None,None,0],
"143":["Build June–July US trade-show list (exhibitors)","PR","EVENTS","Pick the single biggest US show per vertical in Jun/Jul.","Source exhibitor lists for metal-parts buyer outreach.","high","Todo",None,"curate",None,None,0],
"124":["Create cold call list for Eric","PR","COLDCALL","Build a 50–75 contact new-space/defense cold-call sheet.","Eric dials procurement/supply-chain buyers himself.","none","Done","Jul 20",None,None,None,0],
"129":["Lab List at tech companies","PR",None,"Source lab-operations buyers for the Coupa/Amazon RF-enclosure storefront.","Reach people who need 1–10 stocked enclosures fast.","none","Backlog",None,"list to build",None,None,0],
"161":["Redstone USA — Target Account Tracker","PR","TRACKER","Enrich the target list with phones + correct engineering/supply-chain contacts.","Cold-calling to win business for the Seattle facility.","high","Done","Jul 20",None,None,None,0],
"168":["Send Eric the qualified-leads list (CPL dispute)","PR","LEADS","Pull the qualified-lead list backing our CPL figure.","Resolve Eric's cost-per-lead dispute with verifiable data.","urgent","Todo",None,None,None,None,0],
"147":["Email Eric: consolidated outreach lists + brochures","PR","TRACKER","Send Eric ONE consolidated email with all lists, brochures, and a checklist.","Stop losing action items in Slack; get his recorded review back.","high","Todo",None,None,None,None,0],
"113":["Eric/Alec: share next trade show details","PR","EVENTS","Get the next show's name, exhibitor and (key) attendee lists from Eric/Alec.","Powers the customized-brochure workflow + trade-show outbound.","high","Backlog",None,None,None,None,0],
"106":["Start Attio build (after website sent for approval)","CRM",None,"Build the Attio CRM to auto-reply, qualify, enrich, and nurture leads.","Replace manual HubSpot sequencing once the sitemap is sent.","high","Backlog",None,None,"trigger: sitemap → Eric",None,0],
"107":["Build qualification agent (rev/employee + headcount)","CRM",None,"Auto-qualify inbound leads on headcount/revenue/order signals.","Filter leads before they reach Alec's queue.","high","Backlog",None,None,None,None,0],
"108":["Attio AI agent finish (Redstone Attio install)","CRM",None,"Finish the Redstone Attio AI agent install.","Same CRM automation goal (pairs with R7/RED-120).","high","Backlog",None,None,None,None,0],
"120":["R7 — Attio AI agent finish","CRM",None,"Complete the Attio agent for Redstone's CRM (S1 sprint item).","Distinct from CPG's Attio; owned under RED.","medium","Backlog",None,None,None,None,0],
"119":["Xometry Lead Funnel","CRM","LEADS","Handle paid quotes and the instant-quote email flow.","Convert quote requests into tracked leads.","none","Done","Jun 23",None,None,None,0],
"127":["Add missing leads to HubSpot + forward to Eric/sales@","CRM","LEADS","Add missing leads to HubSpot and forward submissions to Eric/sales@.","Keep the CRM and Eric in sync on inbound.","high","Done","Jun 3",None,None,None,0],
"111":["Alec: log all outbound calls in HubSpot","CRM",None,"Ensure Alec logs all outbound calls in HubSpot, not his cell.","Unlocks the transcript pipeline for copy + enrichment.","high","Backlog",None,None,None,None,0],
"144":["Match HubSpot call list to leads","CRM","LEADS","Cross-check HubSpot calls vs leads for timely, qualified follow-up.","Feeds Alec's workflow / can auto-update the leads sheet.","medium","Todo",None,None,None,None,0],
"145":["Research HubSpot call-transcript extraction","CRM",None,"Timeboxed research for a cleaner way to pull HubSpot call transcripts.","Read call-quality themes for copy and Attio enrichment.","low","Todo",None,None,None,None,0],
"151":["Alec: send HubSpot call transcripts (Mexico-vs-China)","CRM",None,"Get 2–3 Alec calls showing the Mexico-vs-China cost explanation.","Source material for the Mexico brochure's cost-reality messaging.","medium","Todo",None,None,None,None,0],
"89":["Investigate scraping HubSpot call recordings","CRM",None,"Investigate scraping historical HubSpot call recordings/transcripts.","Context for landing-page copy and Attio account enrichment.","medium","Backlog",None,None,None,None,0],
"128":["Connect homepage form → Slack lead notification","CRM",None,"Wire the homepage quote form to post to #redstone-marketing.","Lead-notification parity with landing-page leads.","high","Done","Jun 10",None,None,None,1],
"74":["BQ leads → Google Sheet daily mirror","RPT","LEADS","Daily 8am cron mirrors new BigQuery leads into the Live Lead List tab.","Give the team an always-current lead sheet with dedup + alerts.","high","Done","May 19",None,None,None,0],
"86":["Define MQL vs SQL in writing + propagate","RPT","LEADS","Get Kas's written MQL/SQL definitions as the source of truth.","Apply consistently across sheet, reporting, and Attio.","high","Done","May 26",None,None,None,0],
"87":["Hard-block free-email providers from lead sheet","RPT","LEADS","Reject free-email (Gmail/Yahoo/Outlook) leads at the form.","Keep the inbound sheet to business leads only.","high","Done","May 26",None,None,None,0],
"88":["Add MQL/SQL + cadence + comments columns to lead sheet","RPT","LEADS","Add MQL/SQL, call-cadence, and comments columns to the lead sheet.","Let Alec track qualification status and follow-up.","high","Done","May 26",None,None,None,0],
"112":["Alec: backfill inbound lead sheet (2 new leads)","RPT","LEADS","Add 2 new leads with disqual reasons / qualification emails.","Keep the inbound sheet complete and actioned.","high","Done","May 26",None,None,None,0],
"90":["Month-by-month R2B2 company-size report","RPT","SALES","Break down R2B2 company-size data month-by-month, pre/post search-off.","Test whether paid search was secretly the highest-quality channel.","medium","Backlog",None,"build report",None,None,0],
"91":["Build CPL dashboard auto-updating from BigQuery/Attio","RPT","ROADMAP","Tie quotes, form-fills, and calls into one auto-updating CPL dashboard.","Eric sees CPL at a glance every check-in (via Attio Reports).","medium","Backlog",None,"build dashboard",None,None,0],
"92":["Set CPL targets (MQL ~$500 / SQL ~$1k / CPA ~$4k)","RPT","ROADMAP","Codify Eric's CPL targets (MQL ~$500 / SQL ~$1k / CPA ~$4k).","Flag off-target channels across all reporting.","high","Backlog",None,None,None,None,0],
"93":["Change call report format (lead numbers first)","RPT","SALES","Restructure the report so leads-across-all-channels come first.","Opens every Eric call with the metric he cares about; monthly cadence.","high","Backlog",None,None,None,None,0],
"121":["Eric monthly report (overdue catch-up + send)","RPT","SALES","Catch up and send the overdue Eric monthly report.","Keep the client's monthly performance reporting on track.","urgent","Backlog",None,None,None,None,0],
"162":["Review PostHog pipeline failure","RPT",None,"Fix >1% data-pipeline failures in PostHog and rotate the webhook secret.","Restore reliable event/analytics capture.","none","In Progress",None,None,None,None,0],
"55":["Hand-off note to Eric/Kas with monitoring dashboard link","RPT",None,"Hand off to Eric/Kas with a monitoring dashboard link.","Post-launch ownership and visibility.","high","Backlog",None,None,None,None,0],
"48":["Update /dashboard.html with new live URLs","RPT",None,"Update the internal dashboard.html with the new live URLs.","Keep the ops monitoring page pointed at production.","high","Backlog",None,None,None,None,1],
"80":["Virtual referral (stale) + CPL calculations","RPT",None,"Stale virtual-referral follow-up + CPL calculations.","Superseded — cancelled.","medium","Cancelled",None,None,None,None,0],
"77":["Virtual referral (stale) + CPL calculations","RPT",None,"Stale virtual-referral follow-up + CPL calculations.","Superseded — cancelled.","medium","Cancelled",None,None,None,None,0],
"163":["Service dedicated brochure (master)","BR","BRO","Produce 6 lean, geo-neutral service brochures from the brand template.","One-per-capability collateral reusing on-brand web copy.","high","Internal Approval",None,None,None,None,0],
"164":["Service Brochure — Die Casting","BR","DIE","Build the Die Casting brochure (pilot deck, built first).","Sales handout/attachment for die-casting prospects.","none","Internal Approval",None,None,None,None,0],
"165":["Service Brochure — Sand Casting","BR","SAND","Build the Sand Casting brochure.","Sales collateral for sand-casting prospects.","none","Internal Approval",None,None,None,None,0],
"166":["Service Brochure — Investment Casting","BR","INV","Build the Investment Casting brochure.","Sales collateral for investment-casting prospects.","none","Internal Approval",None,None,None,None,0],
"167":["Service Brochure — CNC Machining","BR","CNC","Build the CNC Machining brochure (notes IATF 16949 + US facility).","Sales collateral for CNC prospects.","none","Internal Approval",None,None,None,None,0],
"169":["Service Brochure — Metal Injection Molding (MIM)","BR","MIM","Build the Metal Injection Molding brochure.","Sales collateral for MIM prospects.","none","Internal Approval",None,None,None,None,0],
"170":["Service Brochure — Sheet Metal Fabrication","BR","SHEET","Build the Sheet Metal Fabrication brochure.","Sales collateral for sheet-metal prospects.","none","Internal Approval",None,None,None,None,0],
"132":["Brochure 2 — add product photos (canonical brochure)","BR","BRO","Add directed product/process photos to the canonical 17-sheet brochure.","Stronger general brochure, design untouched (awaiting Leo's 3 decisions).","medium","Backlog",None,None,"Leo's 3 decisions",None,0],
"149":["Replace live website brochure PDF with simplified version","BR","BRO","Replace the live-site brochure with the new simplified version.","Ensure the website serves the current approved brochure.","high","Todo",None,None,None,None,1],
"150":["Kas→Eric brochure \"homework\" email","BR",None,"Ask Eric to pick the next 2–3 brochure formats + objectives/outlines.","Direct the next wave of collateral to real needs.","medium","Todo",None,None,None,None,0],
"109":["Eric: send brochure feedback","BR",None,"Get Eric's written feedback on the brochure.","Unblocks the sales-deck build (RED-101).","urgent","Backlog",None,None,None,None,0],
"115":["Eric: think through how brochure/deck will be used","BR",None,"Have Eric decide how the brochure/deck is actually used.","Use (handout vs attachment vs leave-behind) drives structure/content.","medium","Done","Jun 23",None,None,None,0],
"101":["Build sales deck after brochure approved","BR",None,"Build the sales deck after brochure approval, with personalization slides.","Per-prospect pitch deck; blocked on Eric's brochure notes.","medium","Backlog",None,None,"RED-109 feedback",None,0],
"102":["Customized-brochure flow for trade-show top 10","BR",None,"Workflow to make personalized printed brochures for top-10 show attendees.","Hand a tailored, laminated brochure at the booth.","medium","Backlog",None,None,"attendee list (RED-113)",None,0],
"152":["Automate brochure delivery on lead-form submission","BR",None,"Auto-send the page-matched brochure (as a link) on any form submission.","Replace Manuel's manual follow-up; feeds Attio/HubSpot automation.","medium","Todo",None,None,"launch + brochure approval",None,0],
"56":["Copy items — Redstone items to use for copy","BR",None,"Reusable Redstone outreach/deck copy blocks (cold-email template etc.).","Source copy for decks and outreach.","none","Backlog",None,None,None,None,0],
"57":["General Deck — design conventions + WIP completion","BR",None,"Complete the 15-slide general deck to locked design conventions.","Finish the core sales deck build by the deadline.","high","Backlog",None,None,None,None,0],
"58":["General Deck — design inconsistency audit","BR",None,"Audit the general deck for design inconsistencies.","Ensure a visually consistent deck (companion to RED-57).","medium","Backlog",None,None,None,None,0],
"59":["General Deck — second copy review pass","BR",None,"Second copy-review pass on the general deck.","Catch residual copy issues the first pass missed.","high","Backlog",None,None,None,None,0],
"61":["General Deck — Round 3 revisions from Leo","BR",None,"Apply Leo's slide-by-slide feedback (round 3).","Log each feedback item → action → pending decision.","high","In Progress",None,None,None,None,0],
"62":["Eric: deck Quote SLA 14→5 business days","BR",None,"Change the deck quote SLA from 14 to 5 business days (two places).","Remove an off-putting claim per Eric.","urgent","Done","May 29",None,None,None,0],
"63":["Eric: sand casting max weight 7,000kg→300kg","BR",None,"Change sand-casting max weight 7,000kg→300kg on the deck.","Accurate capability claim.","urgent","Backlog",None,None,None,"max weight w/ Eric",0],
"64":["Eric: deck remove Ohio address, use Seattle only","BR",None,"Delete the blacklisted Ohio address; use Seattle only.","Avoid confusing Google / wrong-address issues.","urgent","Done","May 29",None,None,None,0],
"65":["Eric: deck logo bar — drop Mahindra/Honda/Mayer","BR",None,"Add a real-customer logo bar (drop Mahindra/Honda/Mayer; keep Halliburton/GameStop).","Credible social proof early in the deck.","urgent","Done","May 29",None,None,None,0],
"66":["Eric: deck Post-Processing slide tagline removal","BR",None,"Remove the confusing \"one supplier, one freight leg, one PO\" tagline.","Clearer \"no second vendor\" finishing message.","high","Backlog",None,None,None,None,0],
"347":["Set up Mailgun SMTP on the Redstone sales email","EM","DOMAINS","Stand up Mailgun SMTP for site notifications on the sales email.","Deliverable form notifications (A2/SendGrid were blocked).","high","Done","Jul 2",None,None,None,0],
"348":["Send SMTP switch details to Leo via Slack","EM",None,"Give Leo the Mailgun switch details via Slack.","Let Leo communicate/justify the change to Eric.","medium","Done","Jul 2",None,None,None,0],
"349":["Re-test notification deliverability after Mailgun","EM",None,"Verify notifications actually send and land after Mailgun.","Confirm the prior Gmail-block failure is resolved.","medium","Done","Jul 2",None,None,None,0],
"350":["Inform Eric of SMTP migration + justification","EM",None,"Communicate the SMTP migration + justification to Eric.","Client sign-off on the mail change.","medium","Done","Jul 6",None,None,None,0],
"429":["Lead-form auto-reply automation (enterprise leads)","EM",None,"Auto-reply to enterprise lead-form leads from Manuel's mailbox using his template.","Instant qualified-lead response (excludes free-mail); draft to Eric.","high","Internal Approval",None,None,None,None,1],
"69":["Pivot Google Ads to Mexico-only search campaigns","AD","ROADMAP","Restructure Google Ads to Mexico-only search campaigns.","Focus spend where the only qualified opportunities came from.","high","Backlog",None,None,None,None,0],
"171":["Fix Redstone Seattle Google Business Profile / listings","AD",None,"Fix the Seattle Google Business Profile + 32 directory listings (wrong phone).","Improve local presence with Jack/Outrider (Semrush audit).","high","Todo",None,None,None,None,0],
"98":["Disable exit-intent pop-up across ad landing pages","AD",None,"Disable the too-fast exit-intent popup on ad landing pages.","Re-enable later once nurture infrastructure exists.","high","Backlog",None,None,None,None,1],
"158":["Kas: book Rachel + full-team meeting (calendar invites)","MT",None,"Send invites for the June 12 Rachel/full-team meeting.","Broader strategy/CRM session (Attio/HubSpot).","urgent","Todo",None,None,None,None,0],
"122":["Jack/Rachel Friday lunch coord + Ash notes send","MT",None,"Coordinate the Jack/Rachel Friday lunch + send Ash call notes.","Bundled attended coordination window.","high","Backlog",None,None,None,None,0],
"79":["Eric call prep","MT",None,"Prep for the Eric call from Jack's emailed docs.","Be ready for the client delivery call (urgent).","urgent","Done","Jun 1",None,None,None,0],
"76":["Eric call prep (from Jack's emailed docs)","MT",None,"Earlier Eric call prep from Jack's docs.","Cancelled — folded into RED-79.","urgent","Cancelled",None,None,None,None,0],
"78":["Eric: recurring Tuesday meeting setup","MT",None,"Set up a recurring Tuesday Eric meeting.","Cancelled.","low","Cancelled",None,None,None,None,0],
"81":["Eric recurring Tuesday meeting setup","MT",None,"Recurring Tuesday Eric meeting setup.","Cancelled duplicate.","low","Cancelled",None,None,None,None,0],
"15":["Eric review session Sun May 10 — capture sign-off","MT",None,"Eric review session (May 10) with written sign-off.","Capture client approval in writing.","urgent","Done","Jun 6",None,None,None,0],
"27":["Internal review pass — Leo + Daniel sign off","MT",None,"Internal Leo + Daniel review pass.","Cancelled.","high","Cancelled",None,None,None,None,0],
"37":["Mid-phase Eric review session (target May 20)","MT",None,"Mid-phase Eric review session.","Cancelled.","high","Cancelled",None,None,None,None,0],
"153":["Guide: Gemini + NanoBanana API setup for image gen","OP",None,"Document a Gemini + NanoBanana image-gen workflow from reference photos.","Generate part imagery without exposing customer IP.","low","Todo",None,None,None,None,0],
"99":["Send Eric a Claude context-gathering prompt","OP",None,"Write a Claude context-gathering prompt for Eric to run locally.","Pull Eric's richer Redstone marketing context into ours.","high","Backlog",None,None,None,None,0],
"100":["Onboarding rule: capture client pitch language day 1","OP",None,"Make day-1 pitch-language capture a standard onboarding step.","Avoid missing positioning (e.g. \"not a sourcing company\").","medium","Backlog",None,None,None,None,0],
"110":["Eric: run local Claude on Kas's prompt → .md context","OP",None,"Eric runs Kas's prompt on his local Claude, returns .md context files.","Import his marketing context and positioning.","high","Backlog",None,None,None,None,0],
"105":["Plan Aerospace site build + outbound campaigns (US)","OP",None,"Plan a separate US-only Aerospace entity (site + outbound).","Deferred until after main-site launch; no China references.","low","Backlog",None,None,None,None,0],
"131":["Redstone copy review","OP","CLAIMS","Review Redstone copy for accuracy and claims.","Ensure on-brand, compliant messaging (see Content Claims Review).","medium","Backlog",None,None,None,None,1],
}

def esc(t): return t.replace("&","&amp;")
PRANK={"urgent":0,"high":1,"medium":2,"low":3,"none":4}
PLBL={"urgent":"Urgent","high":"High","medium":"Medium","low":"Low","none":"No priority"}

def row(i,d,show_date=False):
    name,cat,rk,pu,uc,prio,state,date,build,blocked,verify,flag=d
    chips=[]
    chips.append(f'<span class="cat">{esc(CATN[cat])}</span>')
    if rk:
        lbl,url,pdf=R[rk]
        cls="res pdf" if pdf else "res"
        ic="📕" if pdf else "📄"
        chips.append(f'<a class="{cls}" href="{url}" target="_blank">{ic} {esc(lbl)}</a>')
    if build: chips.append(f'<span class="build">⚠ {esc(build)}</span>')
    if blocked: chips.append(f'<span class="blocked">⛔ {esc(blocked)}</span>')
    if verify: chips.append(f'<span class="verify">⚠ verify · {esc(verify)}</span>')
    chips.append(f'<span class="prio p-{prio}">{PLBL[prio]}</span>')
    if show_date and date: chips.append(f'<span class="date">✓ {date}</span>')
    fl='<span class="flag">flag</span>' if flag else ''
    return (f'<li><span class="id">RED-{i}</span>'
            f'<span class="name">{esc(name)}{fl}'
            f'<span class="purpose"><b>Purpose:</b> {pu} <span class="dot">·</span> <b>Use case:</b> {uc}</span></span>'
            f'<span class="right">{"".join(chips)}</span></li>')

def sortkey(i): return (PRANK[I[i][5]], -int(i))

# agency-internal / meta work — not the Redstone business itself (onboarding SOP, internal
# tooling guides, context-gathering prompts, internal meetings, separate Aerospace entity)
EXCLUDE={"27","37","78","81","99","100","105","110","122","153"}
HIDE=[i for i in I if I[i][5]=="urgent"]   # urgent items removed from report per request
XI=[i for i in I if i in EXCLUDE and I[i][5]!="urgent"]  # non-Redstone items removed (not already urgent)
A=[i for i in I if I[i][5]!="urgent" and i not in EXCLUDE]
notstarted=[i for i in A if I[i][6] in ("Backlog","Todo")]
inprog=[i for i in A if I[i][6]=="In Progress"]
approval=[i for i in A if I[i][6]=="Internal Approval"]
done=[i for i in A if I[i][6]=="Done"]
canc=[i for i in A if I[i][6]=="Cancelled"]

def block(ids,show_date=False):
    return "\n".join(row(i,I[i],show_date) for i in sorted(ids,key=sortkey))

# not started grouped by priority
ns_html=""
for p in ["urgent","high","medium","low","none"]:
    grp=[i for i in notstarted if I[i][5]==p]
    if not grp: continue
    grp=sorted(grp,key=lambda i:-int(i))
    ns_html+=f'  <h3 class="pgrp"><span class="prio p-{p}">{PLBL[p]}</span> <span class="pc">{len(grp)}</span></h3>\n  <ul>\n'
    ns_html+="\n".join("    "+row(i,I[i]) for i in grp)
    ns_html+="\n  </ul>\n"

HTML=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Redstone Work</title>
<style>
  :root{{--bg:#0f1115;--card:#171a21;--card2:#1c2029;--ink:#e7ebf2;--muted:#9aa4b6;--line:#262b36;--accent:#e5484d;--accent2:#3e63dd;}}
  *{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}}
  a{{color:inherit}} .wrap{{max-width:1040px;margin:0 auto;padding:32px 20px 80px}}
  header{{border-bottom:1px solid var(--line);padding-bottom:22px}}
  .kicker{{color:var(--accent);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:12px}}
  h1{{margin:.35em 0 .2em;font-size:28px;line-height:1.2}} .sub{{color:var(--muted);max-width:78ch}}
  .meta{{color:var(--muted);font-size:12.5px;margin-top:14px}}
  .stats{{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 4px}}
  .stat{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;min-width:96px}}
  .stat b{{display:block;font-size:22px}} .stat span{{color:var(--muted);font-size:12px}}
  h2.sec{{font-size:19px;margin:34px 0 4px;display:flex;align-items:center;gap:10px}}
  h2.sec .c{{color:var(--muted);font-weight:500;font-size:13px}}
  .secdesc{{color:var(--muted);font-size:13px;margin:0 0 10px}}
  h3.pgrp{{font-size:13px;margin:20px 0 8px;display:flex;align-items:center;gap:8px}}
  h3.pgrp .pc{{color:var(--muted);font-size:12px}}
  ul{{list-style:none;margin:0 0 4px;padding:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--card)}}
  li{{display:flex;gap:12px;align-items:flex-start;padding:11px 14px;border-top:1px solid var(--line);flex-wrap:wrap}}
  li:first-child{{border-top:none}} li:hover{{background:var(--card2)}}
  .id{{font-variant-numeric:tabular-nums;font-weight:700;color:var(--accent2);min-width:66px;font-size:13.5px;padding-top:1px}}
  .name{{flex:1;min-width:200px;font-weight:500}}
  .purpose{{display:block;margin-top:4px;font-size:12px;color:var(--muted);line-height:1.45;font-weight:400}}
  .purpose b{{color:#c3ccdb;font-weight:600}} .purpose .dot{{opacity:.45;padding:0 2px}}
  .right{{display:flex;align-items:center;gap:7px;flex-wrap:wrap;justify-content:flex-end;padding-top:1px}}
  .flag{{color:var(--accent);font-size:11px;border:1px solid var(--accent);border-radius:6px;padding:1px 6px;margin-left:8px;white-space:nowrap}}
  .cat{{font-size:10.5px;color:var(--muted);background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:6px;padding:2px 7px;white-space:nowrap}}
  .res{{font-size:12px;text-decoration:none;border-radius:7px;padding:3px 9px;white-space:nowrap;color:#9be6b3;background:rgba(70,167,88,.12);border:1px solid rgba(70,167,88,.34)}}
  .res:hover{{background:rgba(70,167,88,.22)}}
  .res.pdf{{color:#f2b8bb;background:rgba(229,72,77,.12);border-color:rgba(229,72,77,.34)}} .res.pdf:hover{{background:rgba(229,72,77,.22)}}
  .build{{font-size:11px;font-weight:600;color:#ffd27a;background:rgba(245,158,11,.13);border:1px solid rgba(245,158,11,.34);border-radius:7px;padding:3px 9px;white-space:nowrap}}
  .blocked{{font-size:11px;font-weight:600;color:#f2a3a6;background:rgba(229,72,77,.14);border:1px solid rgba(229,72,77,.4);border-radius:7px;padding:3px 9px;white-space:nowrap}}
  .verify{{font-size:11px;font-weight:600;color:#ffcf85;background:rgba(245,158,11,.14);border:1px solid rgba(245,158,11,.4);border-radius:7px;padding:3px 9px;white-space:nowrap}}
  .date{{font-size:11.5px;color:#8fe6a8;white-space:nowrap;font-variant-numeric:tabular-nums;opacity:.9}}
  .prio{{font-size:10px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;padding:2px 8px;border-radius:999px;white-space:nowrap}}
  .p-urgent{{color:#ff9ea1;background:rgba(229,72,77,.16);border:1px solid rgba(229,72,77,.42)}}
  .p-high{{color:#ffc27a;background:rgba(245,158,11,.14);border:1px solid rgba(245,158,11,.38)}}
  .p-medium{{color:#9cb4ff;background:rgba(62,99,221,.14);border:1px solid rgba(62,99,221,.34)}}
  .p-low{{color:#b8c0cf;background:rgba(107,114,128,.16);border:1px solid rgba(107,114,128,.3)}}
  .p-none{{color:#8b93a1;background:rgba(82,88,99,.12);border:1px solid rgba(82,88,99,.28)}}
  .note{{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:10px;padding:16px 18px;margin-top:28px}}
  .note h3{{margin:0 0 8px;font-size:14px}} .note p{{margin:6px 0;color:var(--muted);font-size:13.5px}}
  .files{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px;margin-top:12px}}
  .files a{{display:block;text-decoration:none;background:var(--card2);border:1px solid var(--line);border-radius:9px;padding:9px 12px;font-size:12.5px}}
  .files a:hover{{border-color:var(--accent2)}} .files a b{{display:block;color:var(--ink)}} .files a span{{color:var(--muted);font-size:11.5px}}
  code{{background:#0b0d11;border:1px solid var(--line);border-radius:5px;padding:1px 5px;font-size:12.5px}}
  footer{{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);color:var(--muted);font-size:12px}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <div class="kicker">Redstone Manufacturing · Plane project RED</div>
  <h1>Redstone Work</h1>
  <p class="sub">Redstone-business work from project RED — outbound, CRM, brochures &amp; decks, reporting, email infra, ads — organised by status and priority so the not-started queue is front and centre. Each item carries its purpose, use case, GDrive link, and any blocked/verify/to-build flags. Website build and agency-internal work are excluded.</p>
  <div class="meta">Source: Plane <code>project-ares</code> · Drive: Redstone GDrive · state reconciled 2026-07-20 · <b>{len(HIDE)} urgent + {len(XI)} agency-internal items hidden per request</b></div>
  <div class="stats">
    <div class="stat"><b>{len(notstarted)}</b><span>not started</span></div>
    <div class="stat"><b>{len(inprog)}</b><span>in progress</span></div>
    <div class="stat"><b>{len(approval)}</b><span>in approval</span></div>
    <div class="stat"><b>{len(done)}</b><span>done</span></div>
    <div class="stat"><b>{len(canc)}</b><span>cancelled</span></div>
  </div>
</header>

<h2 class="sec">🔴 Not started <span class="c">{len(notstarted)} · Backlog + Todo, by priority</span></h2>
<p class="secdesc">The open queue. Grouped by Plane priority; ⛔ = blocked on a dependency, ⚠ verify = confirm before acting, ⚠ = a list still to build/expand.</p>
{ns_html}

<h2 class="sec">🟠 In progress <span class="c">{len(inprog)}</span></h2>
<ul>
{block(inprog)}
</ul>

<h2 class="sec">🟣 Internal approval <span class="c">{len(approval)} · awaiting sign-off before client</span></h2>
<ul>
{block(approval)}
</ul>

<h2 class="sec">✅ Done <span class="c">{len(done)} · with completion date</span></h2>
<ul>
{block(done,show_date=True)}
</ul>

<h2 class="sec">⨯ Cancelled <span class="c">{len(canc)}</span></h2>
<ul>
{block(canc)}
</ul>

<div class="note" style="border-left-color:#e5484d">
  <h3>Blocked / needs verification</h3>
  <p><b>⛔ Blocked</b> — can't progress until the dependency clears: <b>RED-132</b> (Leo's 3 photo decisions), <b>RED-101</b> (Eric's brochure feedback, RED-109), <b>RED-102</b> (next trade-show attendee list, RED-113), <b>RED-152</b> (website launch + brochure approval), <b>RED-106</b> (triggers when sitemap goes to Eric). <i>RED-136 unblocked 2026-07-20 — Apollo UI search, no API key.</i></p>
  <p><b>⚠ Verify</b> — confirm before acting/publishing: <b>RED-139</b> (MD&amp;M East 2026 dates — Informa's site shows May 2027, contradicting 3rd-party Jun 2026).</p>
</div>

<div class="note" style="border-left-color:#f59e0b">
  <h3>Lists still to build / expand</h3>
  <p>Tagged <span class="build" style="padding:1px 6px">⚠</span>: <b>RED-129</b> (Lab List — no sheet yet), <b>RED-140</b> (Labs Facility Testing list — no sheet yet), <b>RED-141</b> (expand A&amp;D Apollo to ~80), <b>RED-136</b> (Prospects/enrichment tab in Exhibitors sheet), <b>RED-137</b> (extend scraper for SEMICON + flagships), <b>RED-142</b> (refine Ohio OEM), <b>RED-143</b> (curate trade-show shortlist), <b>RED-90</b> (R2B2 report), <b>RED-91</b> (CPL dashboard).</p>
</div>

<h2 class="sec">Redstone GDrive — key files</h2>
<div class="files">
  <a href="{R['LEADS'][1]}" target="_blank"><b>HubSpot Redstone Leads</b><span>Inbound lead sheet · MQL/SQL, CPL</span></a>
  <a href="{R['ROADMAP'][1]}" target="_blank"><b>Redstone // Roadmap</b><span>Lead Data · CPL targets</span></a>
  <a href="{R['TRACKER'][1]}" target="_blank"><b>Target Account Tracker (Enriched)</b><span>Redstone USA target accounts</span></a>
  <a href="{R['DOMAINS'][1]}" target="_blank"><b>Domains &amp; Accounts</b><span>Outbound domains · Lemlist · SMTP</span></a>
  <a href="{R['EXH'][1]}" target="_blank"><b>Automate 2026 Exhibitors</b><span>Scraped exhibitor companies</span></a>
  <a href="{R['EVENTS'][1]}" target="_blank"><b>Event Lists — 100</b><span>US industry event / trade-show list</span></a>
  <a href="{R['OHIO'][1]}" target="_blank"><b>Ohio OEM Manufacturing</b><span>Ohio OEM prospect list</span></a>
  <a href="{R['COLDCALL'][1]}" target="_blank"><b>Eric Cold Call List</b><span>Cold-call targets for Eric</span></a>
  <a href="{R['SALES'][1]}" target="_blank"><b>Sales Report</b><span>Call / lead reporting</span></a>
  <a href="{R['CLAIMS'][1]}" target="_blank"><b>Content Claims Review (Eric)</b><span>Copy / claims review</span></a>
  <a href="{R['BRO'][1]}" target="_blank"><b>redstone-brochure-v4.pdf</b><span>Canonical brochure (current)</span></a>
</div>

<footer>Redstone Manufacturing · Plane project RED · non-website slice · organised by status + priority · 2026-07-20 · internal, unlisted</footer>
</div>
</body>
</html>'''
open("index.html","w").write(HTML)
print("items:",len(I),"notstarted:",len(notstarted),"inprog:",len(inprog),"approval:",len(approval),"done:",len(done),"canc:",len(canc))
