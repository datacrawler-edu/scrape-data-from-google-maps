# Scrape Data from Google Maps

Scrape data from Google Maps through the hosted [Google Maps Business Scraper on Apify](https://apify.com/datascraperes/actor-google-maps?fpr=edudata) without writing code, or integrate it with Python, JavaScript or cURL to collect structured business listings.

[Browse the API examples and sample Google Maps Dataset](https://github.com/datacrawler-edu/scrape-data-from-google-maps)

This repository contains executable requests, verified sample input, a complete real Dataset item and a CSV export. It documents the public integration surface without exposing the Actor's private implementation, infrastructure or credentials.

## What this repository helps you do

- Scrape Google Maps business names, addresses, phones and websites by category and location.
- Collect ratings, review counts, categories, photos, opening hours and coordinates when available.
- Search cities, regions or complete countries with a shared country and language setting.
- Deduplicate businesses across queries, locations and search sectors by Google Place ID.
- Export Google Maps business data to JSON, CSV, Excel or JSONL for lead generation, local SEO and market research.

## Example result

The complete verified Dataset item is available in [`data/sample-output.json`](data/sample-output.json), with the same public fields in [`data/sample-output.csv`](data/sample-output.csv).

```json
{
  "name": "HUNDRED",
  "placeId": "ChIJE6tFsFOFQQ0Rz192-I_0ZVg",
  "googleMapsUrl": "https://www.google.com/maps/place/?q=place_id:ChIJE6tFsFOFQQ0Rz192-I_0ZVg",
  "address": "Av. de la Victoria, 144",
  "city": "Madrid",
  "countryCode": "ES",
  "phone": "919 99 27 18",
  "website": "https://hundredburgers.com/",
  "avgRating": 4.7,
  "tags": ["Hamburguesería"],
  "lat": 40.474943499999995,
  "long": -3.8360741
}
```

The fixture comes from a successful published Actor run. Google Maps listings change over time, so it proves the output contract rather than promising that every optional field remains available.

## Run Google Maps Scraper without code

1. Open [Google Maps Business Scraper on Apify](https://apify.com/datascraperes/actor-google-maps?fpr=edudata).
2. In the **Input** tab, add one or more **Locations** and **Search Queries**.
3. Select the language and matching country code, then set **Max Results**.
4. Click **Start**.
5. Open **Dataset** to inspect and export the unique business results.

Use [`data/sample-input.json`](data/sample-input.json) for a one-result test and [`docs/no-code-guide.md`](docs/no-code-guide.md) for the complete web-interface walkthrough.

## Try Google Maps Scraper with Apify's free plan

Apify's Free plan currently includes **$5 in monthly prepaid usage** and does not require a credit card. At the current Actor price, available credit can cover a small first test, but it is not unlimited free usage.

Unused credit expires at the end of the billing cycle. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata) before running a larger search.

## Quick start for developers

### Python

#### 1. Install the client

```bash
pip install -r examples/python/requirements.txt
```

#### 2. Set your Apify token

Linux/macOS:

```bash
export APIFY_API_TOKEN="your-token"
```

Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

#### 3. Run the example

```bash
python examples/python/scrape_google_maps.py
```

The script reads [`data/sample-input.json`](data/sample-input.json), runs the hosted Actor and prints each unique business Dataset item as JSON.

## Input example

```json
{
  "locations": [
    "Madrid"
  ],
  "queries": [
    "restaurants"
  ],
  "language": "es",
  "countryCode": "ES",
  "maxResults": 1
}
```

See [`docs/input-reference.md`](docs/input-reference.md) for defaults, normalization, location scope and result-limit behavior.

## Request examples

### cURL

[`examples/curl-request.md`](examples/curl-request.md) uses the synchronous Dataset endpoint and the checked-in sample input.

### Python

[`examples/python/scrape_google_maps.py`](examples/python/scrape_google_maps.py) runs the sample input. [`examples/python/batch_google_maps.py`](examples/python/batch_google_maps.py) demonstrates several business queries, and [`examples/python/export_google_maps_csv.py`](examples/python/export_google_maps_csv.py) converts Dataset JSON to CSV.

### JavaScript

[`examples/javascript/request.mjs`](examples/javascript/request.mjs) uses the official Apify JavaScript client.

All request examples call the hosted Actor. They do not contain a token, proxy URL, private endpoint or scraping implementation.

## Output fields

| Field | Meaning |
| --- | --- |
| `name`, `placeId` | Required business name and stable Google Place ID. |
| `googleMapsUrl` | Direct URL to the Google Maps listing. |
| `address`, `city`, `region`, `postalCode`, `countryCode` | Available business location components. |
| `phone`, `website` | Public contact details when exposed by the listing. |
| `avgRating`, `totalReviews`, `priceRange` | Available rating, review-count and price-level data. |
| `tags`, `description` | Localized business categories and description when available. |
| `businessPhoto`, `photoUrls` | Main image and additional returned photo URLs. |
| `hours` | Available localized opening-hours entries. |
| `lat`, `long` | Business coordinates. |
| `discoveryQuery`, `searchLocation`, `searchCoordinates` | Search context that discovered the business. |
| `scrapeTimestamp` | ISO 8601 collection timestamp. |

See [`docs/output-reference.md`](docs/output-reference.md) for types, nullable fields and nested object details.

## Common use cases

Read [`docs/use-cases.md`](docs/use-cases.md) for complete workflows covering:

- Local business lead generation and CRM enrichment.
- Local SEO and competitor coverage research.
- Market mapping by city, region or country.
- Business directory creation and CSV export.
- Recurring monitoring with Place ID deduplication.

## How to scrape data from Google Maps with Python

Use [`examples/python/scrape_google_maps.py`](examples/python/scrape_google_maps.py) for a complete hosted integration. It loads a JSON input, calls the Actor and iterates over the default Dataset without reproducing the scraping infrastructure locally.

For several categories, use [`examples/python/batch_google_maps.py`](examples/python/batch_google_maps.py). Every query is combined with every location, while `maxResults` limits unique results across the complete run.

## Scrape Google Maps business data by location

Put cities, regions or country names in `locations`, business categories in `queries`, and select the matching `countryCode`. For example, `Madrid` with `restaurants` searches that city, while `Spain` with the same query plans a wider country search that can take longer.

Use separate runs for locations in different countries because one country code applies to the entire run.

## Export Google Maps data to CSV

Run `python examples/python/export_google_maps_csv.py`. It reads the real sample JSON by default and writes `data/exported-google-maps.csv`, preserving nested arrays and objects as JSON strings.

You can also export the hosted Apify Dataset directly as CSV, Excel, JSON or JSONL.

## FAQ

See [`docs/faq.md`](docs/faq.md) for answers about no-code usage, Python integration, location scope, duplicates, missing fields, reviews, billing and CSV export.

## Limits and pricing

- At least one location and one query are required.
- Every query is searched in every location.
- One `language` and one `countryCode` apply to the complete run.
- `maxResults` is a global limit for unique businesses; `0` removes that result limit.
- Current public price: **$1.00 per 1,000 unique business results delivered**.

One unique business successfully written to the Dataset triggers one `business-result` event at `$0.001`. Duplicate Place IDs, out-of-area candidates, failed requests and results not written to the Dataset do not trigger that event. Verify the current contract on the [Actor page](https://apify.com/datascraperes/actor-google-maps?fpr=edudata) before production use.

## Hosted version

Use the hosted Actor for geographic planning, deduplication, batching, schedules, API access, webhooks and managed Dataset storage:

[Run Google Maps Business Scraper on Apify](https://apify.com/datascraperes/actor-google-maps?fpr=edudata)

## Responsible use

Google Maps data is dynamic and optional values vary by business, query, location, language and time. The Actor returns public listing fields when available; it does not collect individual review text or reviewer profiles.

Use returned data lawfully and respect the terms, access rules, privacy obligations and database rights that apply to your use case. Never commit an Apify token or other credentials to this repository.

## Support

For a problem with these examples, [open a GitHub issue](https://github.com/datacrawler-edu/scrape-data-from-google-maps/issues) with sanitized input and the error message. For an Actor execution problem, include the Apify run ID but never include your token.

## License

This repository is released under the MIT License.
