from __future__ import annotations

import logging

from py_logging.constants import CURRENT_COMIC_URL, URL_BASE, URL_POSTFIX

import hishel
import httpx
from red_utils.ext import httpx_utils

log = logging.getLogger(__name__)


def test_current_xkcd_comic():
    CACHE_TRANSPORT: hishel.CacheTransport = httpx_utils.get_cache_transport()

    with httpx_utils.HTTPXController(transport=CACHE_TRANSPORT) as httpx_ctl:
        current_comic_req: httpx.Request = httpx_ctl.new_request(url=CURRENT_COMIC_URL)

        log.info(f"Requesting URL: {CURRENT_COMIC_URL}")
        try:
            current_comic_res: httpx.Response = httpx_ctl.send_request(
                request=current_comic_req
            )
        except Exception as exc:
            msg = Exception(f"Unhandled exception sending request. Details: {exc}")
            log.error(f"[ERROR] {msg}")

            raise exc

        if current_comic_res.status_code == 200:
            log.debug(
                f"Current comic response: [{current_comic_res.status_code}: {current_comic_res.reason_phrase}]"
            )
        else:
            log.debug(
                f"Current comic response: [{current_comic_res.status_code}: {current_comic_res.reason_phrase}]: {current_comic_res.text}"
            )


if __name__ == "__main__":
    test_current_xkcd_comic()
