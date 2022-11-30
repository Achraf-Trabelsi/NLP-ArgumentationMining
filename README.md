# Extraction of Argumentative Elements from Text

## About / Synopsis

* Argumentation mining is a research field in Natural Language Processing. The objective is to
  automatically extract and identify argumentative structures from a natural language text. This project provides notebooks aiming to solve that task.
* Project status: Completed
* This project was presented at INSAT university as end of year project.


## How to run it?

* You can run it with google colab plateform by click its icon on the notebook. Note: we recommend using GPU for faster proceessing.
* You can also run them local with jupyter but you need to pay attention to the diffrent packages and requirements.

## Usage

### Screenshots

![image](https://user-images.githubusercontent.com/98907083/204883783-a32eba0b-7777-46b6-a537-613a54f00792.png)

### Features

As highlighted in the above image the task is solved using that pipeline :
* Argument detection phase.
* Argument Classification phase.

The notebooks showcase various NLP ecniques that were used on the embedding level as well as the model.
Word2Vec, Fastext, RNNs, CNNs, Naive Bayes to name a few.

## Code


### Content

![nlp-pipeline](https://user-images.githubusercontent.com/98907083/204885989-e5cfb89b-9758-4c78-b703-f4bcc52bf447.png)

Our notebooks follow the classical NLP pipeline, we tried to test a set of techniques for each step in each notebook.

To better understand our data, you can run the [EDA](https://github.com/Achraf-Trabelsi/PFA-NLP/blob/main/EDA.ipynb) notebook.

Example : the [feature engineering](https://github.com/Achraf-Trabelsi/PFA-NLP/blob/main/Feature_Engineering.ipynb) notebook is good example following those steps with diffrent models running.

### Results

| Model     | f1-score      | 
| --------- | ------------------- | 
| BiLSTM+PoS |   0.7703       | 
| SimpleBiLSTM      | 0.7626        | 
| Random Forest       | 0.73        | 


### Limitations

* Due to hardware limitations we couldn't run complex models such as Transformers namely Bert.
* Due to time constraints we didn't finish the deployement phase, we focused all of our efforts on building rebost models.

## Resources (Documentation and other links)

We provide useful link that can help you with understanding this project :

* You can find a link for the project report with in length details [here](https://drive.google.com/file/d/1eH7tPCUZCi816QWIlSlGSV2yDcHhygmc/view?usp=sharing)
* You can find the dataset [here](https://www.kaggle.com/competitions/feedback-prize-2021/data)

## Contributors 

[Achraf Trabelsi](https://github.com/Achraf-Trabelsi)  

[Chedly ben Azizi](https://github.com/chedlyba)


