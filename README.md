# MT Exercise 4: Layer Normalization for Transformer Models

# Group Members: 
Mengjie Wu (22-747-869)
Ruomeng Xu (22-748-339)

This repo is a collection of scripts showing how to install [JoeyNMT](https://github.com/joeynmt/joeynmt), download
data and train & evaluate models, as well as the necessary data for training your own model

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3.10 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv, pandas, matplotlib are installed on your system. To install, e.g.

    `pip install virtualenv`

    `pip install pandas`
    
    `pip install matplotlib`


# Steps

Clone this repository or your fork thereof in the desired place:

    git clone https://github.com/momoieaso/mt-exercise-4.git

    git clone https://github.com/momoieaso/joeynmt.git

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    cd mt-exercise-4

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Make sure to install the exact software versions specified in the the exercise sheet before continuing.

Download Moses for post-processing:

    ./scripts/download_moses.sh


Train a model of prenorm:

    ./scripts/train_pre.sh

Train a model of postnorm:

    ./scripts/train_post.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved. It is also possible to continue training from there later on. 

Note: Our models were trained using CPU. 

After training, the table is created manually. It is located in the folder of visualizaiton. Based on the table, the line chart is visualized by running the script in the folder: 

    cd visualization

    python line_chart.py


# Changes and Additions

1. The original script ./scripts/train.sh was modified into two additional scripts to train two models: prenorm and postnorm

    ./scripts/train_pre.sh

    ./scripts/train_post.sh

2. To adapt to the process of training, the yaml file in configs folder is also changed. As a result, there are two additional yaml files: 

    ./configs/deen_transformer_pre.yaml

    ./configs/deen_transformer_post.yaml

3. The table and the line chart are added in the new folder: 

    ./visualization

4. The line chart is visualized using the script: 

    ./visualization/line_chart.py
