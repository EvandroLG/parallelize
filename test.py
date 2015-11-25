# -*- coding: utf-8 -*-

from unittest import TestCase, mock
import parallel_download as parallel, multiprocessing

class TestParallelDownload(TestCase):
    #def test_should_raise_a_exception_when_paramer_is_not_string_or_list(self):
        #self.assertRaises(TypeError, parallel.parallel_download(1))

    @mock.patch('parallel_download._download')
    def test_should_call_download_function_without_create_processes_when_parameter_is_a_string(self, *args):
        parallel.parallel_download('http://www.google.com/')
        self.assertEqual(parallel._download.call_count, 1)

    @mock.patch('parallel_download._download')
    @mock.patch('multiprocessing.pool.Pool')
    def test_should_call_download_function_3_times(self, *args):
        parallel.parallel_download([
            'http://www.google.com/',
            'http://www.github.com/',
            'http://www.facebook.com/'
        ])
        
        param = multiprocessing.pool.Pool.call_args_list[0][0][0]

        self.assertEqual(multiprocessing.pool.Pool.call_count, 1)
        self.assertEqual(param, 3)
