"""Search several Google Maps business categories in one hosted Actor call."""

from __future__ import annotations

import json

from scrape_google_maps import INPUT_PATH, scrape_google_maps


def main() -> None:
    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    run_input["queries"] = ["restaurants", "cafes", "bakeries"]
    run_input["maxResults"] = 30

    for item in scrape_google_maps(run_input):
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
