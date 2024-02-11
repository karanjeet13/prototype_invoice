import unittest
from enum import Enum
from copy import deepcopy


class InvoiceType(Enum):
    SALES = 1
    PURCHASE = 2
    SERVICE = 3


class ClonableObject:
    def cloneObject(self):
        return deepcopy(self)


class Invoice(ClonableObject):
    def __init__(self, invoice_id, customer_name, amount, payment_method, type):
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.amount = amount
        self.payment_method = payment_method
        self.type = type

    def getInvoiceId(self):
        return self.invoice_id

    def getCustomerName(self):
        return self.customer_name

    def getAmount(self):
        return self.amount

    def getPaymentMethod(self):
        return self.payment_method

    def getType(self):
        return self.type


class InvoicePrototypeRegistry:
    def __init__(self):
        self.invoices = {}

    def addPrototype(self, invoice):
        self.invoices[invoice.getType()] = invoice

    def getPrototype(self, type):
        return self.invoices.get(type)

    def clone(self, type):
        return self.invoices[type].cloneObject()


class TestInvoice(unittest.TestCase):

    def getRegistry(self):
        for name, obj in globals().items():
            if isinstance(obj, type) and issubclass(obj, InvoicePrototypeRegistry):
                return obj()
        return None

    def test_invoice_implements_clonable_object(self):
        self.assertTrue(issubclass(Invoice, ClonableObject),
                        "If the prototype pattern is implemented correctly, the Invoice class should implement the ClonableObject interface")

    def test_invoice_clone_method_creates_distinct_object(self):
        invoice = Invoice(1, "testinvoice", 100.0, "CARD", InvoiceType.SALES)
        cloned_invoice = invoice.cloneObject()
        self.assertIsNot(invoice, cloned_invoice,
                         "If the clone method is implemented correctly, it should return a new object")

    def test_registry(self):
        registry = self.getRegistry()
        self.assertIsNotNone(registry,
                             "If the registry pattern is implemented correctly, the registry should not be None")

        invoice = Invoice(1, "testinvoice", 100.0, "CARD", InvoiceType.SALES)
        registry.addPrototype(invoice)

        prototype = registry.getPrototype(invoice.getType())
        self.assertIsNotNone(prototype,
                             "If the clone method is implemented correctly, it should return a non-None object")
        self.assertIs(invoice, prototype,
                      "If the registry pattern is implemented correctly, the registry should return the same object that was added")

    def test_registry_clone(self):
        invoice = Invoice(1, "testinvoice", 100.0, "CARD", InvoiceType.SALES)
        registry = self.getRegistry()
        self.assertIsNotNone(registry,
                             "If the registry pattern is implemented correctly, the registry should not be None")

        registry.addPrototype(invoice)

        # Clone the prototype and validate it's a distinct object with the same values
        cloned_invoice = registry.clone(invoice.getType())
        self.assertIsNotNone(cloned_invoice,
                             "If the clone method is implemented correctly, it should return a non-None object")
        self.assertIsNot(invoice, cloned_invoice,
                         "If the clone method is implemented correctly, it should return a new object")

        self.assertEqual(invoice.getInvoiceId(), cloned_invoice.getInvoiceId(),
                         "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(invoice.getAmount(), cloned_invoice.getAmount(),
                         "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(invoice.getPaymentMethod(), cloned_invoice.getPaymentMethod(),
                         "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(invoice.getCustomerName(), cloned_invoice.getCustomerName(),
                         "If the clone method is implemented correctly, it should return a new object with the same values as the original object")
        self.assertEqual(invoice.getType(), cloned_invoice.getType(),
                         "If the clone method is implemented correctly, it should return a new object with the same values as the original object")


if __name__ == '__main__':
    unittest.main()
