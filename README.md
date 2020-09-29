# This is an rest API to manage product inventory.


## Database Modelling


knitr::kable(top_gap, caption = "Products table modelling")

| column   | type   | description           | unique |
|:--------:|:------:|:---------------------:|:-------|
| name     | string | the product name      | True   | 
| sku      | string | the product sku       | True   |
| cost     | float  | the product cost      | False  |
| price    | float  | the unit price        | False  |
| quantity | int    | the quantity in stock | False  |
