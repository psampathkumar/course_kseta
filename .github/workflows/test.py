class Test(unittest.TestCase):
    def test_data_loaded(self):
        self.assertTrue(len(data) > 0, "No data loaded")