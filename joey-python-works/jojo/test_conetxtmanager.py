import contextlib


class Pipeline(object):

    def _publish(selfs, objects):
        print objects

    def _flush(self):
        print 'flush'

    @contextlib.contextmanager
    def publisher(self):
        try:
            yield self._publish
        finally:
            self._flush()

    @contextlib.contextmanager
    def error_out_instance_on_exception(self):
        try:
            yield
        except NotImplementedError as error:
            print 'not implements'
        except Exception:
            print 'Exception occurs.'


pipeline = Pipeline()
with pipeline.publisher() as publisher:
    publisher([1, 2, 3, 4, 5])

with pipeline.error_out_instance_on_exception():
    raise NotImplementedError('aa')


