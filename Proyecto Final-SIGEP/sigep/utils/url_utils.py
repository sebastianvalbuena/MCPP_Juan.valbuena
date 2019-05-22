base_url = 'https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&entidadSeleccionado=%s&max=%s'


class UrlUtils:
    @staticmethod
    def get_url_by_entity(code, max=100):
        return base_url % (code, max)
