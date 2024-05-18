root
├── pytest_cmdline_main
├── pytest_plugin_registered
├── pytest_configure
│   ├── pytest_plugin_registered
├── pytest_session_start
│   ├── pytest_plugin_registered
│   ├── pytest_report_header
├── pytest_collection
│   ├── pytest_collect_start
│   ├── pytest_make_collect_report
│   ├── ├── pytest_ignore_collect
│   ├── ├── pytest_collect_file
│   ├── ├── ├── pytest_pycollect_module
│   ├── ├── pytest_collectstart
│   ├── ├── ├── pytest_pycollect_module
│   ├── ├── pytest_pycollect_makeitem
│   ├── ├── ├── pytest_generate_tests
│   ├── ├── ├── ├── pytest_make_parametrize_id
│   ├── pytest_collect_report
│   ├── pytest_itemcollected
│   ├── pytest_collection_modifyitems
│   ├── pytest_collection_finish
│   ├── pytest_report_collectionfinish???
├── pytest_run_testloop
│   ├── pytest_runtest_protocol
│   ├── pytest_runtest_logstart
│   ├── pytest_runtest_setup
│   ├── ├── pytest_fixture_setup
│   ├── pytest_runtest_makereport
│   ├── pytest_runtest_logreport
│   ├── ├── pytest_report_teststatus
│   ├── pytest_runtest_call
│   ├── ├── pytest_pyfunc_call
│   ├── pytest_runtest_teardown
│   ├── ├── pytest_fixture_post_finalizer
│   ├── pytest_runtest_makereport
│   ├── pytest_runtest_logreport
│   ├── pytest_runtest_logfinish
├── pytest_session_finish
│   │   ├──pytest_terminal_summary
├── pytest_unconfigure