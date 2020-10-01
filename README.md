# This is an rest API to manage product inventory.

## Installation guide

1. Required environment.

```
- Python 3.7 
- MongoDB 3.4 >
```

2. clone the repo.

```sh
$ git clone git@github.com:felipe-dna/product-api.git
```

3. Install the requirements.

```
$ cd product-api

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt
```

4. Set environment required variables:

| variable name | description |
|---------------|-------------|
| DATABASE_NAME | The name of the database |
| DEBUG         | A boolean value that define the DEBUG value for Django |
| SECRET_KEY    | A key used to encrypt and decrypt some data in Django |

5. If your database need authentication or the host where it is running is different from the default, pass this another 
variables:

| variable name | description |
|---------------|-------------|
| DATABASE_USER     | The database user |
| DATABASE_PASSWORD | The database password |
| DATABASE_HOST     | The database host |
| DATABASE_PORT     | The database port |


7. Make the migrations.

```
$ python manage.py makemigrations accounts kits products
$ python migrate
```

8. Run the server.

```
$ python manage.py runserver
```


## Database Modelling


1. Products table

| column     | type                      | description                                        | unique             |
|------------|---------------------------|----------------------------------------------------|:------------------:|
| id         | string(UUID)              | the product identifier                             | :heavy_check_mark: |
| name       | string                    | the product name                                   | :x:                | 
| sku        | string                    | the product sku                                    | :heavy_check_mark: |
| cost       | float                     | the product cost                                   | :x:                |
| price      | float                     | the unit price                                     | :x:                |
| quantity   | int                       | the quantity in stock                              | :x:                |

2. Kit table

| column     | type                      | description                                                                                | unique             |
|------------|---------------------------|--------------------------------------------------------------------------------------------|:------------------:|
| id         | string(UUID)              | the kit identifier                                                                         | :heavy_check_mark: |      
| name       | string                    | the kit name                                                                               | :x:                | 
| sku        | string                    | the kit sku                                                                                | :heavy_check_mark: |
| products   | array                     | a list of products                                                                         | :x:                |
| price      | float                     | the sum of all the products subtracting the discount percentage of each product in the kit | :x:                |
| cost       | float                     | the sum of all the products that compose the kit                                           | :x:                | 
| stock      | int                       | the quantity of possible kits in the stock based in the kit products stock                 | :x:                | 

2.1 products

Products is a list of objects that must have the follow fields:

- sku: the product sku;
- quantity: the quantity of items in each kit;
- discount: the discount percentage from when comparing the product unit price and the kit price;

---


## Endpoints


### Summary

| entity   | path                 | http method | needs authentication | internal route     | Description               |
|----------|----------------------|-------------|:--------------------:|:------------------:|---------------------------|
| Users    | /users               | POST        | :heavy_check_mark:   | :heavy_check_mark: | Creates a new user        |
| Users    | /users/authenticate  | POST        | :x:                  | :x:                | Authenticates the user    |
| Products | /products            | POST        | :heavy_check_mark:   | :x:                | Creates a new product     |
| Products | /products            | GET         | :heavy_check_mark:   | :x:                | Lists all the products    |
| Products | /products/id         | GET         | :heavy_check_mark:   | :x:                | Retrieves a product by id |
| Products | /products/id         | PATCH       | :heavy_check_mark:   | :x:                | Updates a product         |
| Products | /products/id         | DELETE      | :heavy_check_mark:   | :x:                | Deletes a product         |
| Kits     | /kits                | POST        | :heavy_check_mark:   | :x:                | Creates a new kit         |
| Kits     | /kits                | GET         | :heavy_check_mark:   | :x:                | Lists all the kits        |
| Kits     | /kits/id             | GET         | :heavy_check_mark:   | :x:                | Retrieves a kit by id     |
| Kits     | /kits/id             | PATCH       | :heavy_check_mark:   | :x:                | Updates a kit             |
| Kits     | /kits/id             | DELETE      | :heavy_check_mark:   | :x:                | Deletes a kit             |


### Users

1. Create a new user. Needs the internal key.

1.1 Path:
> POST
> /v1/users


1.2 Needed headers:

```json
{
  "Authorization": "<internal-api-key>"
}
```

1.3 Body example:

```json
{
  "first-name": "jhon",
  "last-name": "Doe",
  "email": "john@doe.com",
  "password": "something-very-secret"
}
```

1.4 Response example:

```json5
// status-code:200
{
  "id": 1,
  "first-name": "jhon",
  "last-name": "Doe",
  "email": "john@doe.com",
  "api-key": "the-created-user-api-key"
}
```

2. Authenticate in the system.

2.1 Path:
> POST
> /v1/users/authenticate

2.2 Body example:

```json

{
  "email": "john@doe.com",
  "password": "something-very-secret"
}
```

2.3 Response example:

```json5
// status-code: 200
{
  "api-key": "the-created-user-api-key"
}
```


### Products

1. Create new products.

1.1 Path:
> POST
> /v1/products

1.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

1.3 Body example:

```json
[
  {
    "name": "product 1",
    "sku": "d8gasd8gasd8sagd8as",
    "cost": 17.50,
    "price": 30.00,
    "quantity": 100
  },
  {
    "name": "product 2",
    "sku": "9dh9h9dh9hd92h9dh9hasd",
    "cost": 32.50,
    "price": 73.00,
    "quantity": 200
  }
]
```

1.4 Response example:

```json5
// status-code: 201
[
  {
    "id": 1,
    "name": "product 1",
    "sku": "d8gasd8gasd8sagd8as",
    "cost": 17.50,
    "price": 30.00,
    "quantity": 100
  },
  {
    "id": 2,
    "name": "product 2",
    "sku": "9dh9h9dh9hd92h9dh9hasd",
    "cost": 32.50,
    "price": 73.00,
    "quantity": 200
  }
]
```

2. Read Products.

2.1 Read products by filters or not.

2.1.1 Path:
> GET
> /v1/products

2.1.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

2.1.3 Possible query filters:

| name                 | type     | format   | example                                | description                                                            | 
|----------------------|----------|----------|----------------------------------------|------------------------------------------------------------------------|
| cost-lower-than      | float    | 00.00    | /v1/products?cost-lower-than=100.00    | retrieves the products with cost lower than the given value            |
| cost-bigger-than     | float    | 00.00    | /v1/products?cost-bigger-than=100.00   | retrieves the products with cost bigger than the given value           |
| price-lower-than     | float    | 00.00    | /v1/products?price-lower-than=100.00   | retrieves the products with price lower than the given value           |
| cost-bigger-than     | float    | 00.00    | /v1/products?price-bigger-than=100.00  | retrieves the products with the price bigger than the given value      | 
| quantity-bigger-than | number   | 100000   | /v1/products?quantity-bigger-than=7    | retrieves the products with stock quantity bigger than the given value |
| quantity-lower-than  | number   | 100000   | /v1/products?quantity-lower-than=100   | retrieves the products with stock quantity lower than given value      |
| created-after        | datetime | YY-mm-dd | /v1/products?crated-after=2020-09-11   | retrieves the products that was created after the given date           |
| created-before       | datetime | YY-mm-dd | /v1/products?created-before=2020-11-12 | retrieves the products that was created before the given date          |
| created-by           | string   | UUID     | /v1/products?created-by=9jda9dj9asdas  | retrieves the products that was created by the given user              |

2.1.4 Response example:

```json5
// status-code: 200
[
  {
    "id": 1,
    "name": "product 1",
    "sku": "d8gasd8gasd8sagd8as",
    "cost": 17.50,
    "price": 30.00,
    "quantity": 100,
    "created-by": {
      "id": "hd9ashdashdashd9a",
      "first-name": "John",
      "last-name": "Doe"
    },
    "created-at": "2020-02-09T22:50:00Z"
  },
  {
    "id": 2,
    "name": "product 2",
    "sku": "9dh9h9dh9hd92h9dh9hasd",
    "cost": 32.50,
    "price": 73.00,
    "quantity": 200,
    "created-by": {
      "id": "hd9ashdashdashd9a",
      "first-name": "John",
      "last-name": "Doe"
    },
    "created-at": "2020-02-09T22:50:00Z"
  }
]
```


2.2 Read products by id.

2.2.1 Path:
> GET
> /v1/products/:id

2.2.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

2.2.3 Needed path parameters:

| name  | type   | format | example                        | description                                          | 
|-------|--------|--------|--------------------------------|------------------------------------------------------|
| id    | string | UUID   | /v1/products/jd9a9djsajd9da99a | defines the id of the product that must be retrieved |


2.2.4 Response example:

```json5
// status-code: 200
{
    "id": 1,
    "name": "product 1",
    "sku": "d8gasd8gasd8sagd8as",
    "cost": 17.50,
    "price": 30.00,
    "quantity": 100,
    "created-by": {
      "id": "hd9ashdashdashd9a",
      "first-name": "John",
      "last-name": "Doe"
    },
    "created-at": "2020-02-09T22:50:00Z"
}
```

3. Update an product.

3.1 Path:
> PATCH
> /v1/products/:id

3.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

3.3 Needed path parameters:

| name  | type   | format | example                        | description                                        | 
|-------|--------|--------|--------------------------------|----------------------------------------------------|
| id    | string | UUID   | /v1/products/jd9a9djsajd9da99a | defines the id of the product that will be updated |


3.4 Possible body parameters:

| name     | type   | format | 
|----------|--------|--------|
| name     | string |        |
| cost     | float  | 00.00  |
| price    | float  | 00.00  |
| quantity | int    | 100    |


3.5 Response example:

```md
> **status-code:** 204
> NO BODY
```

4. Delete an product.

4.1 Path:
> DELETE
> /v1/products/:id

4.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

4.3 Needed path parameters:

| name  | type   | format | example                        | description                                        | 
|-------|--------|--------|--------------------------------|----------------------------------------------------|
| id    | string | UUID   | /v1/products/jd9a9djsajd9da99a | defines the id of the product that will be deleted |


4.4 Response example:

```md
> **status-code:** 204
> NO BODY
```


### Kits


1. Create an kits.

1.1 Path:
> POST
> /v1/kits

1.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

1.3 Body example:

```json
{
    "name": "kit 1",
    "sku": "d8gasd8gasd8sagd8as",
    "products": [
      {
        "id": "d9sh9dsdhs9dhs9dh",
        "discount": 11.5,
        "quantity": 2
      },
      {
        "id": "hd9ah9dsah9hdsada",
        "discount": 0.0,
        "quantity": 1
      }
    ]
}
```

1.4 Response example:

```json5
// status-code: 201
{
  "name": "kit 1",
  "sku": "d8gasd8gasd8sagd8as",
  "products": [
    {
      "id": "d9sh9dsdhs9dhs9dh",
      "name": "par de meias",
      "discount": 11.5,
      "quantity": 2,
    },
    {
      "id": "hd9ah9dsah9hdsada",
      "name": "tênis",
      "discount": 0.0,
      "quantity": 1,
    }
  ],
  "price": 30.00,
  "cost": 25.00,
  "stock": 10
}
```

2. Read Kits.

2.1 Read kits by filters or not.

2.1.1 Path:
> GET
> /v1/kits

2.1.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

2.1.3 Possible query filters:

| name              | type     | format   | example                            | description                                                     | 
|-------------------|----------|----------|------------------------------------|-----------------------------------------------------------------|
| cost-lower-than   | float    | 00.00    | /v1/kits?cost-lower-than=100.00    | retrieves the kits with cost lower than the given value         |
| cost-bigger-than  | float    | 00.00    | /v1/kits?cost-bigger-than=100.00   | retrieves the kits with cost bigger than the given value        |
| price-lower-than  | float    | 00.00    | /v1/kits?price-lower-than=100.00   | retrieves the kits with price lower than the given value        |
| cost-bigger-than  | float    | 00.00    | /v1/kits?price-bigger-than=100.00  | retrieves the kits with the price bigger than the given value   | 
| stock-bigger-than | number   | 100000   | /v1/kits?stock-bigger-than=7       | retrieves the kits with stock stock bigger than the given value |
| stock-lower-than  | number   | 100000   | /v1/kits?stock-lower-than=100      | retrieves the kits with stock stock lower than given value      |
| created-after     | datetime | YY-mm-dd | /v1/kits?crated-after=2020-09-11   | retrieves the kits that was created after the given date        |
| created-before    | datetime | YY-mm-dd | /v1/kits?created-before=2020-11-12 | retrieves the kits that was created before the given date       |
| created-by        | string   | UUID     | /v1/kits?created-by=9jda9dj9asdas  | retrieves the kits that was created by the given user           |
| product-id        | string   | UUID     | /v1/kits?product-id=hh2gd78ags8g2  | retrieves the kits that contains the given product              |

2.1.4 Response example:

```json5
// status-code: 200
[
  {
    "name": "kit 1",
    "sku": "d8gasd8gasd8sagd8as",
    "products": [
      {
        "id": "d9sh9dsdhs9dhs9dh",
        "name": "par de meias",
        "discount": 11.5,
        "quantity": 2,
      },
      {
        "id": "hd9ah9dsah9hdsada",
        "name": "tênis",
        "discount": 0.0,
        "quantity": 1,
      }
    ],
    "price": 30.00,
    "cost": 25.00,
    "stock": 10
  },
  {
    "name": "kit 2",
    "sku": "82g87dgg8g82",
    "products": [
      {
        "id": "d9sh9dsdhs9dhs9dh",
        "name": "par de meias rosas",
        "discount": 15.00,
        "quantity": 2,
      },
      {
        "id": "hd9ah9dsah9hdsada",
        "name": "tênis",
        "discount": 0.0,
        "quantity": 1,
      }
    ],
    "price": 30.00,
    "cost": 25.00,
    "stock": 10
  }
]
```

2.2 Read kits by id.

2.2.1 Path:
> GET
> /v1/kits/:id

2.2.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

2.2.3 Needed path parameters:

| name  | type   | format | example                    | description                                      | 
|-------|--------|--------|----------------------------|--------------------------------------------------|
| id    | string | UUID   | /v1/kits/jd9a9djsajd9da99a | defines the id of the kit that must be retrieved |


2.2.4 Response example:

```json5
// status-code: 200
{
  "name": "kit 1",
  "sku": "d8gasd8gasd8sagd8as",
  "products": [
    {
      "id": "d9sh9dsdhs9dhs9dh",
      "name": "par de meias",
      "discount": 11.5,
      "quantity": 2,
    },
    {
      "id": "hd9ah9dsah9hdsada",
      "name": "tênis",
      "discount": 0.0,
      "quantity": 1,
    }
  ],
  "price": 30.00,
  "cost": 25.00,
  "stock": 10
}
```

3. Update an kit.

3.1 Path:
> PATCH
> /v1/kits/:id

3.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

3.3 Needed path parameters:

| name  | type   | format | example                    | description                                    | 
|-------|--------|--------|----------------------------|------------------------------------------------|
| id    | string | UUID   | /v1/kits/jd9a9djsajd9da99a | defines the id of the kit that will be updated |


3.4 Possible body parameters:

| name     | type   | format | 
|----------|--------|--------|
| name     | string |        |
| products | float  | 00.00  |


3.5 Response example:

```md
> **status-code:** 204
> NO BODY
```

4. Delete an kit.

4.1 Path:
> DELETE
> /v1/kits/:id

4.2 Needed headers:

```json
{
  "Authorization": "Bearer <access-token>"
}
```

4.3 Needed path parameters:

| name  | type   | format | example                    | description                                    | 
|-------|--------|--------|----------------------------|------------------------------------------------|
| id    | string | UUID   | /v1/kits/jd9a9djsajd9da99a | defines the id of the kit that will be deleted |


4.4 Response example:

```md
> **status-code:** 204
> NO BODY
```
