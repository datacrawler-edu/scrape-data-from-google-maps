# FAQ

## Can I scrape data from Google Maps without Python or code?

Yes. Open the [hosted Actor on Apify](https://apify.com/datascraperes/actor-google-maps?fpr=edudata), add locations and queries in the **Input** tab, click **Start** and inspect or export results from **Dataset**. See the [no-code guide](no-code-guide.md).

## Can I test it with Apify's free plan?

Apify's Free plan currently includes **$5 in monthly prepaid usage** and does not require a credit card. It can cover a small test while credit is available, but it is not unlimited free usage. Unused credit expires at the end of the billing cycle. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata).

## How do I scrape Google Maps with Python?

Install the dependency in `examples/python/requirements.txt`, set `APIFY_API_TOKEN` and run [`examples/python/scrape_google_maps.py`](../examples/python/scrape_google_maps.py). It sends the checked-in JSON input to the hosted Actor and prints unique business Dataset items.

## Do I need a Google Maps API key or Google account?

No. The hosted Actor does not require a Google API key, Google Cloud project, Google account or OAuth setup.

## Can I search multiple locations and categories?

Yes. Add multiple values to `locations` and `queries`. Every query runs in every location, while `maxResults` limits unique businesses across the complete run.

## Can I search multiple countries in one run?

One shared `countryCode` applies to every location. Use separate runs when locations belong to different countries.

## How are duplicate businesses handled?

The Actor deduplicates results by Google Place ID across queries, locations and search sectors. A unique business is written and charged only once per run.

## Why are some fields empty?

Google Maps does not expose every field for every listing. Optional fields can be `null`, an empty string or an empty array rather than an invented value.

## Does the output contain individual reviews?

No. It can include `avgRating` and `totalReviews` when available, but it does not collect individual review text or reviewer profiles.

## How do I export Google Maps results to CSV?

Run `python examples/python/export_google_maps_csv.py`. It reads `data/sample-output.json` and writes `data/exported-google-maps.csv` by default. Apify can also export the Dataset directly as CSV.

## How are results billed?

The current public price is $1.00 per 1,000 unique businesses. Each unique Dataset item triggers one `business-result` event. Duplicate Place IDs, out-of-area candidates, failed requests and undelivered results do not trigger that event. Verify current pricing on the [Actor page](https://apify.com/datascraperes/actor-google-maps?fpr=edudata).
