from api.api_kma_uvi import KmaUvi
from basemodule import AbsLogger


class KmaUviLogger(AbsLogger):
    def __init__(self, **log_prop):
        tag = 'KmaUviLogger'
        self.api = KmaUvi()
        super().__init__(self.api, tag, 600000, **log_prop)


if __name__ == '__main__':
    log_properties = {'db_type': ['hdfs'],
                      'mode': 'append',
                      'station': 'all',
                      'term': '10min'}
    kul = KmaUviLogger(**log_properties)
    kul.start_logging()

    try:
        if input('press <ENTER> key to stop logging...\n'):
            kul.stop()
    except KeyboardInterrupt:
        kul.stop()

