"""
Ensures the DHT implementation has the required constants defined
"""
import drogulus.dht.constants as constants
import unittest

class TestConstants(unittest.TestCase):
    """
    Ensures the drogulus.dht.constants module contains the required / expected
    declarations.
    """

    def test_ALPHA(self):
        """
        The alpha number represents the degree of parallelism in network calls.
        """
        self.assertIsInstance(constants.ALPHA, int,
            "constant.ALPHA must be an integer.")

    def test_K(self):
        """
        The k number (so named from the original Kademlia paper) defines the
        maximum number of contacts stored in a k-bucket. This should be an even
        number.
        """
        self.assertIsInstance(constants.K, int,
            "constant.K must be an integer.")
        self.assertEqual(0, constants.K % 2)

    def test_RPC_TIMEOUT(self):
        """
        The rpc timeout number defines the timeout for network operations in
        seconds.
        """
        self.assertIsInstance(constant.RPC_TIMEOUT, int,
            "constant.RPC_TIMEOUT must be an integer.")

    def test_ITERATIVE_LOOKUP_DELAY(self):
        """
        The iterative lookup delay defines the delay (in seconds) between
        iterations of iterative node lookups for loose parallelism.
        """
        self.assertIsInstance(constant.ITERATIVE_LOOKUP_DELAY, int,
            "constant.ITERATIVE_LOOKUP_DELAY must be an integer.")

    def test_REFRESH_TIMEOUT(self):
        """
        The refresh timeout defines how long to wait (in seconds) before an
        unused k-bucket is refreshed.
        """
        self.assertIsInstance(constant.REFRESH_TIMEOUT, int,
            "constant.REFRESH_TIMEOUT must be an integer.")

    def test_REPLICATE_INTERVAL(self):
        """
        The replication interval defines how long to wait (in seconds) before a
        node replicates (republishes / refreshes) any data it stores.
        """
        self.assertIsInstance(constant.REPLICATE_INTERVAL, int,
            "constant.REPLICATE_INTERVAL must be an integer.")
