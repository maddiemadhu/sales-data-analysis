| Column Name | Description                                               | Data Type            | Business Meaning                                                                      |
| ----------- | --------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| ordernumber | Unique identifier for each order                          | Integer              | Used to calculate total distinct orders and transactional volume                      |
| sales       | Revenue generated per transaction                         | Float                | Primary revenue metric used for Total Sales and AOV calculations                      |
| productline | Product category classification                           | Categorical          | Used to analyze performance across product segments                                   |
| productcode | Unique identifier assigned to each product                | Categorical / String | Enables product-level analysis and SKU-level performance tracking                     |
| msrp        | Manufacturer’s Suggested Retail Price                     | Float                | Used to compare actual sales price against listed price and evaluate pricing strategy |
| country     | Customer’s country of purchase                            | Categorical          | Used for regional sales performance and geographic segmentation                       |
| dealsize    | Classification of transaction size (Small, Medium, Large) | Categorical          | Helps analyze deal distribution and revenue concentration by transaction tier         |
| year_id     | Year in which the transaction occurred                    | Integer              | Used for time-based trend analysis and growth evaluation                              |

