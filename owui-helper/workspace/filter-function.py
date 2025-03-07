import logging
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
import httpx
import asyncio

IS_DOCKER = True
URL_BASE = "http://host.docker.internal" if IS_DOCKER else "http://localhost"
CORE_API_PORT = 3333
CORE_API_URL = f"{URL_BASE}:{CORE_API_PORT}"


class Filter:
    """
    Filter class for Open WebUI functionality.
    
    Filters are a flexible plugin system for modifying data before it's sent to the LLM (inlet)
    or after it's returned from the LLM (outlet), as well as intercepting streamed responses (stream).
    """
    class Valves(BaseModel):
        """Configuration options for the filter"""
        api_url: str = Field(
            default=CORE_API_URL,
            description="Base URL for the Core API")
        timeout: float = Field(
            default=10.0,
            description="Timeout in seconds for API requests")
        max_retries: int = Field(
            default=3,
            description="Maximum number of retries for failed requests")
        backoff_factor: float = Field(
            default=0.3,
            description="Backoff factor for retries")

    def __init__(self):
        """Initialize the filter with default values"""
        self.type = "filter"
        self.name = "wrapper_filter"
        self.valves = self.Valves()
        self._client = None
        
    async def _get_client(self):
        """Get or create an httpx AsyncClient"""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                timeout=self.valves.timeout,
                limits=httpx.Limits(max_connections=10),
                verify=False  # Disable SSL verification for local development
            )
        return self._client

    async def _make_request(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Helper method to make HTTP requests with retry logic.
        
        Args:
            endpoint: API endpoint to call
            data: JSON data to send
            
        Returns:
            Response data as dictionary
        """
        url = f"{self.valves.api_url}/{endpoint}"
        retry_count = 0
        
        while retry_count <= self.valves.max_retries:
            try:
                client = await self._get_client()
                response = await client.post(url, json=data)
                response.raise_for_status()
                return response.json()
            except (httpx.RequestError, httpx.TimeoutException) as e:
                retry_count += 1
                if retry_count > self.valves.max_retries:
                    logging.error(f"Request failed after {self.valves.max_retries} retries: {e}")
                    raise
                
                # Calculate backoff time with exponential backoff
                backoff_time = self.valves.backoff_factor * (2 ** (retry_count - 1))
                logging.warning(f"Request attempt {retry_count} failed, retrying in {backoff_time:.2f}s: {e}")
                await asyncio.sleep(backoff_time)
            except Exception as e:
                logging.error(f"Unexpected error during request: {e}")
                raise

    async def inlet(self, body: Dict[str, Any], __user__: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process user input before sending to the LLM.
        
        Args:
            body: The input data containing messages and other parameters
            __user__: Optional user information
            
        Returns:
            Modified input data or error information
        """
        try:
            return await self._make_request("filter/inlet", body)
        except httpx.HTTPStatusError as e:
            logging.error(f"HTTP error in inlet: {e}")
            return {"inlet_error": f"Error in inlet: {type(e).__name__}"}
        except Exception as e:
            logging.error(f"Unexpected error in inlet: {e}")
            return {"inlet_error": f"Error in inlet: {type(e).__name__}"}

    async def stream(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process streamed model responses in real-time.
        
        Args:
            event: The streamed chunk from the LLM
            
        Returns:
            Modified stream event
        """
        try:
            # Simple pass-through implementation
            return event
        except Exception as e:
            logging.error(f"Error in stream processing: {e}")
            return event

    async def outlet(self, body: Dict[str, Any], __user__: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process LLM output before returning to the user.
        
        Args:
            body: The output data from the LLM
            __user__: Optional user information
            
        Returns:
            Modified output data or error information
        """
        try:
            return await self._make_request("filter/outlet", body)
        except httpx.HTTPStatusError as e:
            logging.error(f"HTTP error in outlet: {e}")
            return {"outlet_error": f"Error in outlet: {type(e).__name__}"}
        except Exception as e:
            logging.error(f"Unexpected error in outlet: {e}")
            return {"outlet_error": f"Error in outlet: {type(e).__name__}"}
