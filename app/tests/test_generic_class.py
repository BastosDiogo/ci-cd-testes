import unittest
from generic_class import api_registry, GenericAPI
from services import EmailService, MisconfiguredService

class TestAPIContract(unittest.TestCase):

    def test_service_registered(self):
        self.assertIn('EmailService', api_registry)
        self.assertTrue(issubclass(api_registry['EmailService'], GenericAPI))

    def test_service_methods_work(self):
        service = EmailService()
        self.assertEqual(service.start(), "Email service started")
        self.assertEqual(service.shutdown(), "Email service stopped")

    def test_invalid_runtime_raises(self):
        with self.assertRaises(RuntimeError) as ctx:
            MisconfiguredService()
        self.assertIn("required method 'shutdown()' is missing", str(ctx.exception))

    def test_api_base_not_registered(self):
        self.assertNotIn('GenericAPI', api_registry)

    def test_invalid_definition_raises_typeerror(self):
        invalid_class_code = """
class BrokenContract(GenericAPI):
    def start(self):
        pass  # missing shutdown
"""
        local_vars = {}
        with self.assertRaises(TypeError) as ctx:
            exec(invalid_class_code, globals(), local_vars)
        self.assertIn("must implement the required method 'shutdown'", str(ctx.exception))

if __name__ == '__main__':
    unittest.main()
