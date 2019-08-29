import base64
import faker

fake = faker.Faker()

url = fake.uri()

print(url)
print(base64.urlsafe_b64encode(url.encode("utf-8")))