# cURL request

The synchronous endpoint waits for the Actor run to finish and returns its default Dataset items.

Set `APIFY_API_TOKEN`, then run:

```bash
curl --request POST \
  "https://api.apify.com/v2/acts/datascraperes~actor-google-maps/run-sync-get-dataset-items?token=$APIFY_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

Keep the token out of shell history where possible and never commit it to the repository.
