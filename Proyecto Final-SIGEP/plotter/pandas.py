import matplotlib.pyplot as plot

from pandas import DataFrame


class Pandas:
    title = 'Tipo de contrato'
    studies = 'Nivel de estudios'
    birthplace = 'Lugar de nacimiento'

    header = 'Alcaldía de %s'
    file = 'resources/plots/Alcaldía de %s - %s'

    def plot_data(self, data_frame, index, location):
        diagram = data_frame[index].value_counts()[data_frame[index].value_counts() > 1].plot.barh(
            title=self.header % location)
        diagram.set_xlabel(index)
        plot.tight_layout()
        plot.savefig(self.file % (location, index))

    def plot_location(self, location, data):
        data_frame = DataFrame(
            {Pandas.title: data[0], Pandas.studies: data[1], Pandas.birthplace: data[2]})
        self.plot_data(data_frame, self.title, location)
        self.plot_data(data_frame, self.studies, location)
        self.plot_data(data_frame, self.birthplace, location)

    def plot_directory(self, directory):
        for location in directory:
            self.plot_location(location, directory[location])
