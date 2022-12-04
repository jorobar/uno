import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Azul', 'Naranja', 'Verde']
    values = [150, 50, 125]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()