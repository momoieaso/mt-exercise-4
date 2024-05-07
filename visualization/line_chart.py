import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Validation_ppl_table.csv')

data.columns = data.columns.str.strip()

plt.figure(figsize=(12, 8))

colors = {
    'Baseline': 'blue',
    'Prenorm': 'green',
    'Postnorm': 'red'
}

for column in data.columns[1:]:
    plt.plot(data['Validation ppl'], data[column], label=column, color=colors[column])

plt.xlabel('Steps')
plt.ylabel('Validation ppl')
plt.title('Validation Perplexities of Three Models')

plt.grid(True)

plt.legend()

plt.savefig('/home/moieaso/programming/mt/mt4/Validation_ppl_line_chart.png')
