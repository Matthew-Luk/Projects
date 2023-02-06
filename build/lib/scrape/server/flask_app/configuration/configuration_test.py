import unittest, os
from configuration import Config


class TestConfiguration(unittest.TestCase):

    def test_default_variables(self):
        config = Config()
        self.assertEqual(config.POSTGRES_URL, "", f"Expected: ''; Received: {config.POSTGRES_URL}")
        self.assertEqual(config.REDIS_URL, "", f"Expected: ''; Received: {config.REDIS_URL}")

    def test_read_environment_variables(self):
        postgres_url = "localhost:5432"
        redis_url = "localhost:3679"

        os.environ["POSTGRES_URL"] = postgres_url
        os.environ["REDIS_URL"] = redis_url

        config = Config()
        self.assertEqual(config.POSTGRES_URL, postgres_url, f"Expected: {postgres_url}; Received: {config.POSTGRES_URL}")
        self.assertEqual(config.REDIS_URL, redis_url, f"Expected: {redis_url}; Received: {config.REDIS_URL}")


if __name__ == '__main__':
    unittest.main()