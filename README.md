# This is an rest API to manage product inventory.


## Database Modelling


1. Products table

| column     | type                      | description                                   | unique             |
|------------|---------------------------|-----------------------------------------------|:------------------:|
| id         | string(UUID)              | the product identifier                        | :heavy_check_mark: |
| name       | string                    | the product name                              | :x:                | 
| sku        | string                    | the product sku                               | :heavy_check_mark: |
| cost       | float                     | the product cost                              | :x:                |
| price      | float                     | the unit price                                | :x:                |
| quantity   | int                       | the quantity in stock                         | :x:                |
| created at | datetime(Y/m/dTHH:MM:SSZ) | the datetime where the product was created    | :x:                | 
| created at | str(UUID)                 | the id of the member that created the product | :x:                | 

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
| created at | datetime(Y/m/dTHH:MM:SSZ) | the datetime where the product was created                                                 | :x:                | 
| created by | str(UUID)                 | the id of the member that created the product                                              | :x:                | 


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
  "Authorization": "your-api-key"
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
  "Authorization": "your-api-key"
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
  "Authorization": "your-api-key"
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
