


class Customer:
    class Address:
        def __init__(self, street,zip_code):
            self.street=street
            self.zip_code=zip_code
    def __init__(self,first_name,last_name,age,street,zip_code):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.address=self.Address(street,zip_code)

customer=Customer("Daniel", "Ivron", 14, "wyckoff",12345)
print(customer.address.street)

