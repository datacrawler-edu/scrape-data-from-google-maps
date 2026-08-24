# Use cases

## Local business lead generation

Combine a city with relevant commercial categories, then export `name`, `phone`, `website`, `address` and `placeId` to your CRM. Keep the original `discoveryQuery` and `searchLocation` so every lead remains traceable to the search that found it.

Optional contact fields can be missing. Do not infer or manufacture a phone number, website or email when it is unavailable.

## Local SEO and competitor research

Search the same service categories in neighboring cities or regions. Group results by `tags`, compare `avgRating` and `totalReviews` when available, and use `lat` and `long` to map market coverage.

Google Maps listings are dynamic observations. Keep the complete input and collection time when comparing periods.

## Country or regional market mapping

Use a country or large region in `locations` with its matching `countryCode`. Start with a bounded `maxResults`; broader geographic plans can run longer than city searches.

Use separate runs for different countries because one country code applies to the complete run.

## Business directory creation

Use `placeId` as the stable merge key, and include `googleMapsUrl`, address components, categories, contact fields and coordinates in the directory. Export the Apify Dataset directly or use [`examples/python/export_google_maps_csv.py`](../examples/python/export_google_maps_csv.py).

Review data accuracy and usage obligations before publishing a directory.

## Recurring local-market monitoring

Schedule a stable input in Apify and retain each run's Dataset. Compare Place ID sets to find newly discovered or missing listings, then compare optional fields only when both snapshots contain a value.

A missing result does not by itself prove a business closed; query wording, source availability and geographic coverage can also change.
