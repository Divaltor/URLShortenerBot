from .http_client import BaseHTTPClient

from typing import Optional, Union

from loguru import logger


class RelinkClient(BaseHTTPClient):

    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)

    def __repr__(self):
        return 'rel.ink'

    def _process_response(self, response: Union[list, dict]) -> Optional[str]:
        if isinstance(response, list):
            return None

        if response and isinstance(response.get('url'), list):
            logger.error(f'Error message of response: {response["url"]}')
            return None

        return f'https://rel.ink/{response["hashid"]}'

    async def get_short_link(self, url: str) -> Optional[str]:
        response = await self.post('/api/links/', data={'url': url})

        return self._process_response(response.json())
