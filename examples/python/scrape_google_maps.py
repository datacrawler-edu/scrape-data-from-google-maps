"""Run the hosted Google Maps Business Scraper and print Dataset items."""

from __future__ import annotations

import json
import os
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/actor-google-maps"
ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"


def scrape_google_maps(run_input: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Run the hosted Actor and yield unique business Dataset items."""
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise RuntimeError("Set APIFY_API_TOKEN before running this example.")

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    yield from client.dataset(run["defaultDatasetId"]).iterate_items()


def main() -> None:
    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    for item in scrape_google_maps(run_input):
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
