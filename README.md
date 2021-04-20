# BigData project

>Final project for the "BigData" course of Master degree in computer engineering at University of Verona: "Querying the MovieLens Dataset using PySpark".
>
## :memo: Objectives:
- [x] Download MovieLens dataset available at https://web2.qatar.cmu.edu/~mhhammou/15415-s14/projects/project1/index.html. 
- [x] Download the queries file available at https://web2.qatar.cmu.edu/~mhhammou/15415-f16/projects/project1/P1_Handout.pdf.
- [x] Solve the queries.

## :white_check_mark: Prerequisites:

- Spark >= 3.0.2, pre-build for Apache Hadoop 2.7 available here https://spark.apache.org/downloads.html or you can just clone this repo.
- Python 3

### Prerequisites for solving queries with Pyspark
The data provided by Movielens are in `.dat` format. `.csv` format is more suitable than `.dat` format because **PySpark** provides a list of methods, such as `map`, which allows to convert `.csv` files to DataFrame.

You can choose to convert the data independently, or use our already converted to `.csv` (present in the folder `spark-3.0.2-bin-hadoop2.7/dataset/`) converted with the code called `converter.py`.

at this point you will have transformed / obtained some .csv that represent these tables:


![](https://i.imgur.com/HMnzQGd.png)

Now you just have to transform the `.csv` into `df` and solve the queries of the document independently.

:bulb: **Hint:** If you want check our solutions you can find them in the folder:`spark-3.0.2-bin-hadoop2.7/BigData-Project.ipynb` .



## References

* [MovieLens](https://grouplens.org/datasets/movielens/)
* [Project page ](https://web2.qatar.cmu.edu/~mhhammou/15415-s14/projects/project1/index.html) - page from where this project was inspired.
* [Spark](https://spark.apache.org/)

## Authors
* **Luca Marzari** - [LM095](https://github.com/LM095)
* **Deborah Pintani** - [DebbyX3](https://github.com/DebbyX3)
