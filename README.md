# 🚀 The Org Org Chart & Decision Makers Scraper

**Scrape The Org company org charts, executive hierarchy, team structures, reporting lines, C-level decision makers, photos, and corporate intelligence to JSON, CSV, or Excel in seconds without browser overhead.** Extract full organizational charts, executive roles, direct report counts, parent-child reporting structures, profile URLs, CDN photos, and verified company metadata (website, LinkedIn, HQ location, headcount range) from **The Org (theorg.com)** — the world's largest open database of 300,000+ tech company org charts.

Built specifically for B2B sales development reps (SDRs), account executives (AEs), executive recruiters, private equity analysts, and autonomous AI prospecting agents. Powered by lightweight HTTP requests with **zero browser overhead** and **100% Pay-Per-Event (PPE) pricing** — you only pay for verified team member and executive records delivered ($0.005/record).

---

## ⚡ Speed & Value Comparison

| Feature | Our Lightweight The Org Scraper | Heavy Browser Scrapers (Playwright / Puppeteer) |
|---|---|---|
| **Memory Consumption** | **128 MB – 256 MB** | 2 GB – 4 GB |
| **Startup Cost** | **$0.00 (Zero Start Fee)** | $0.05 – $0.10 per run |
| **Extraction Speed** | **0.2s – 0.5s per company org chart** | 10s – 25s per company page |
| **Pricing Model** | **Pay-Per-Event ($0.005 / person record)** | Expensive Flat Fee ($40–$80/mo) |
| **Data Enrichment** | **Hierarchy structure + Report counts + CDN photos** | Basic unlinked card dumps |
| **AI & MCP Ready** | **Instant clean JSON for Claude / Cursor MCP** | Bulky unstructured HTML payloads |

---

## 📦 Sample JSON Output

```json
{
  "companyName": "OpenAI",
  "companySlug": "openai",
  "theorgCompanyUrl": "https://theorg.com/org/openai",
  "companyWebsite": "https://openai.com",
  "companyLinkedIn": "https://linkedin.com/company/openai",
  "companyTwitter": "https://twitter.com/openai",
  "companyLocation": "San Francisco, California, United States",
  "companyDescription": "OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity.",
  "companyStage": "startup",
  "employeeRange": "501-1000",
  "teamsCount": 14,
  "totalPositionsInOrg": 820,
  "fullName": "Sam Altman",
  "role": "CEO & Co-Founder",
  "personSlug": "sam-altman",
  "profileUrl": "https://theorg.com/org/openai/org-chart/sam-altman",
  "photoUrl": "https://cdn.theorg.com/29503f81-013a-4e2c-aca6-5274013acfe0.jpg",
  "reportCount": 1236,
  "parentId": null,
  "order": -1,
  "scrapedAt": "2026-11-22T21:30:00.000000+00:00"
}
```

---

## 🎯 Use Cases & Business Value

- **Account-Based Marketing (ABM) & Enterprise Prospecting**: Identify the exact reporting tree of your target accounts. Understand whether the VP of Engineering reports directly to the CTO or CEO, and pinpoint every department head before initiating cold outreach.
- **Executive Recruiting & Headhunting**: Map complete engineering, product, sales, and AI leadership teams at hyper-growth tech companies, unicorns, and Fortune 500 enterprises.
- **Competitor Organization Benchmarking**: Benchmark competitor organizational scale, reporting ratios, span of control, and executive changes over time.
- **Venture Capital & Talent Diligence**: Track executive additions, leadership churn, and team expansions at portfolio companies and potential seed/Series A-D investments.
- **Autonomous AI Agents & Sales Copilots**: Supply clean, structured organizational graphs to AI agents (via Apify MCP Server) to dynamically find the optimal decision maker for any B2B pitch.

---

## ⚙️ Input Parameters

| Parameter | Type | Required | Description | Example |
|---|---|---|---|---|
| `companySlugs` | Array of Strings | No | List of company slugs from The Org (e.g. `openai`, `stripe`, `scale-ai`). | `["openai", "stripe"]` |
| `startUrls` | Array of Objects | No | Alternative: direct URLs to company org charts on The Org. | `[{"url": "https://theorg.com/org/openai"}]` |
| `maxMembersPerCompany` | Integer | No | Max team members to extract per company (default: `50`, set `0` for unlimited). | `50` |
| `maxItems` | Integer | No | Maximum total decision maker records saved across all target companies (default: `20`). | `20` |
| `proxyConfiguration` | Object | No | Optional proxy configuration. Default uses zero proxy overhead via Chrome TLS impersonation. | `{"useApifyProxy": false}` |

---

## 🤖 Integrations & AI Agent Workflows

### 1. Claude & Cursor via Apify MCP Server
Connect this scraper directly to your Claude Desktop or Cursor AI IDE using the Apify MCP Server:
```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```
Ask your AI assistant:
> *"Query The Org Org Chart Scraper on Apify for company 'stripe', find the Chief Revenue Officer and VP of Sales, and generate a personalized outreach sequence."*

### 2. n8n Workflow Automation
Use the included workflow template in `workflows/n8n_template.json`:
1. Add the **Apify Node** ➔ Set Actor ID: `moneygain/theorg-org-chart-scraper`.
2. Pass your target accounts list (e.g. from HubSpot or a Google Sheet).
3. Route extracted executive contacts directly into your CRM, Slack, or email sequencer.

### 3. Make.com (Integromat)
1. Add the **Apify Module** ➔ `Run Actor and get dataset items`.
2. Set Actor ID to `moneygain/theorg-org-chart-scraper`.
3. Map `fullName`, `role`, `reportCount`, and `profileUrl` directly into Pipedrive, Salesforce, or Airtable.

### 4. Clay.com B2B Enrichment
1. Use the **Apify Integration** inside your Clay table.
2. Enrich target company domains by pulling C-level leaders and org hierarchy directly into your contact columns.

### 5. Python SDK Integration
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_API_TOKEN")
run_input = {
    "companySlugs": ["openai", "stripe", "airbnb"],
    "maxMembersPerCompany": 30,
    "maxItems": 50
}
run = client.actor("moneygain/theorg-org-chart-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"{item['fullName']} | {item['role']} at {item['companyName']} (Reports: {item['reportCount']})")
```

---

## ❓ Frequently Asked Questions (SEO FAQ)

### Q1: Is it legal to scrape data from The Org?
**Yes.** This scraper extracts only publicly available org charts, company profiles, and executive position descriptions published on The Org. It does not access private behind-the-login data, personal passwords, or non-public personal information. Always adhere to applicable privacy laws (such as GDPR, CCPA) when conducting B2B marketing outreach.

### Q2: How much does it cost to scrape 1,000 executive profiles?
Under our **Pay-Per-Event (PPE)** pricing, you pay only **$0.005 per verified team member record**, which equals **$5.00 per 1,000 executive profiles**. You are charged $0.00 for empty runs or failed queries, and Apify Bronze/Silver/Gold/Diamond tiers receive automatic volume discounts up to 20% ($4.00 per 1,000).

### Q3: How do I export org chart data to Excel or Google Sheets?
Apify offers instant one-click exports in CSV, JSON, Excel (.xlsx), XML, and HTML formats. You can also automate live synchronization into Google Sheets or Airtable using Apify's native integrations or webhooks.

### Q4: Do I need proxies to run this scraper?
**No.** Thanks to our optimized `curl_cffi` engine with browser TLS fingerprint impersonation, requests connect seamlessly without triggering anti-bot blocks. You do not need to purchase expensive residential proxies.

### Q5: Can I extract full hierarchical org charts for large enterprises?
**Yes.** By increasing `maxMembersPerCompany` (e.g. to 500 or 1,000), you can extract complete leadership hierarchies, reporting tiers, and departmental structures for fast-growing companies and major tech corporations.

---

## 🔗 Explore More High-Speed B2B Scrapers & Enrichers by Our Team

Supercharge your data pipelines, sales outreach, and AI agents with our suite of lightweight, Pay-Per-Event scrapers:

| Scraper | Segment / Target | Key Value | Store Link |
|---|---|---|---|
| **The Org Org Chart Scraper** | Executive Org Charts & Decision Makers | Full org charts, C-suite hierarchy, reporting lines & CDN photos | [Open on Apify Store](https://apify.com/moneygain/theorg-org-chart-scraper) |
| **TrustMRR SaaS Startups Scraper** | SaaS Revenue & M&A Data | Stripe-verified MRR, 30d revenue, active subscriptions & founder contacts | [Open on Apify Store](https://apify.com/moneygain/trustmrr-startups-scraper) |
| **Ashby ATS Tech Jobs Scraper** | Next-Gen ATS Career Feeds | Direct ATS API extraction, salaries, departments & remote flags | [Open on Apify Store](https://apify.com/moneygain/ashby-jobs-scraper) |
| **Clutch B2B Agencies Scraper** | B2B Agencies & IT Services | Decoded direct websites, review ratings, hourly rates & service focus | [Open on Apify Store](https://apify.com/moneygain/clutch-agencies-scraper) |
| **Wellfound Startup Talent Scraper** | AI & Tech Startup Jobs | Startup jobs, compensation ranges, equity & tech stack tags | [Open on Apify Store](https://apify.com/moneygain/wellfound-jobs-scraper) |
| **TheProtocol.it IT Careers Scraper** | IT Salaries & Vacancies | Verified salary brackets, tech requirements & seniority levels | [Open on Apify Store](https://apify.com/moneygain/theprotocol-scraper) |
| **Bulldogjob Tech Recruitment Scraper** | Tech Recruitment Feeds | B2B/Employment rates, tech tags & recruiter contacts | [Open on Apify Store](https://apify.com/moneygain/bulldogjob-scraper) |
| **Devpost Hackathons Scraper** | Hackathons & AI Competitions | Prize money, submission deadlines, themes & project inspiration | [Open on Apify Store](https://apify.com/moneygain/devpost-hackathons-scraper) |
