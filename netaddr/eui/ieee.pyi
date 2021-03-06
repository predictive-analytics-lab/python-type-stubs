from netaddr.core import Publisher, Subscriber
from typing import Any, TextIO, Union

"""
Provides access to public OUI and IAB registration data published by the IEEE.

More details can be found at the following URLs :-

    - IEEE Home Page - http://www.ieee.org/
    - Registration Authority Home Page - http://standards.ieee.org/regauth/
"""
OUI_INDEX = {}
IAB_INDEX = {}

class FileIndexer(Subscriber):
    """
    A concrete Subscriber that receives OUI record offset information that is
    written to an index data file as a set of comma separated records.
    """

    def __init__(self, index_file: TextIO) -> None:
        """
        Constructor.

        :param index_file: a file-like object or name of index file where
            index records will be written.
        """
        ...
    def update(self, data: Any) -> None:
        """
        Receives and writes index data to a CSV data file.

        :param data: record containing offset record information.
        """
        ...

class OUIIndexParser(Publisher):
    """
    A concrete Publisher that parses OUI (Organisationally Unique Identifier)
    records from IEEE text-based registration files

    It notifies registered Subscribers as each record is encountered, passing
    on the record's position relative to the start of the file (offset) and
    the size of the record (in bytes).

    The file processed by this parser is available online from this URL :-

        - http://standards.ieee.org/regauth/oui/oui.txt

    This is a sample of the record structure expected::

        00-CA-FE   (hex)        ACME CORPORATION
        00CAFE     (base 16)        ACME CORPORATION
                        1 MAIN STREET
                        SPRINGFIELD
                        UNITED STATES
    """

    def __init__(self, ieee_file: TextIO) -> None:
        """
        Constructor.

        :param ieee_file: a file-like object or name of file containing OUI
            records. When using a file-like object always open it in binary
            mode otherwise offsets will probably misbehave.
        """
        ...
    def parse(self) -> None:
        """
        Starts the parsing process which detects records and notifies
        registered subscribers as it finds each OUI record.
        """
        ...

class IABIndexParser(Publisher):
    """
    A concrete Publisher that parses IAB (Individual Address Block) records
    from IEEE text-based registration files

    It notifies registered Subscribers as each record is encountered, passing
    on the record's position relative to the start of the file (offset) and
    the size of the record (in bytes).

    The file processed by this parser is available online from this URL :-

        - http://standards.ieee.org/regauth/oui/iab.txt

    This is a sample of the record structure expected::

        00-50-C2   (hex)        ACME CORPORATION
        ABC000-ABCFFF     (base 16)        ACME CORPORATION
                        1 MAIN STREET
                        SPRINGFIELD
                        UNITED STATES
    """

    def __init__(self, ieee_file: TextIO) -> None:
        """
        Constructor.

        :param ieee_file: a file-like object or name of file containing IAB
            records. When using a file-like object always open it in binary
            mode otherwise offsets will probably misbehave.
        """
        ...
    def parse(self) -> None:
        """
        Starts the parsing process which detects records and notifies
        registered subscribers as it finds each IAB record.
        """
        ...

def create_index_from_registry(registry_fh: TextIO, index_path: str, parser: Union[OUIIndexParser, IABIndexParser]) -> None:
    """Generate an index files from the IEEE registry file."""
    ...

def create_indices() -> None:
    """Create indices for OUI and IAB file based lookups"""
    ...

def load_index(index, fp: TextIO) -> None:
    """Load index from file into index data structure."""
    ...

def load_indices() -> None:
    """Load OUI and IAB lookup indices into memory"""
    ...
