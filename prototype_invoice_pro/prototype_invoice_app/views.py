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

    def cloneObject(self):
        return Invoice(self.invoice_id, self.customer_name, self.amount, self.payment_method, self.type)

class InvoicePrototypeRegistry:
    def __init__(self):
        self.invoices = {}

    def addPrototype(self, invoice):
        self.invoices[invoice.getType()] = invoice

    def getPrototype(self, type):
        return self.invoices.get(type)

    def clone(self, type):
        return self.invoices[type].cloneObject()