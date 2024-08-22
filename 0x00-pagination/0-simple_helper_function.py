#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Retrieves tha index range from tha given page and page size.
            """
                start = (page - 1) * page_size
                    end = start + page_size
                        return (start, end)
