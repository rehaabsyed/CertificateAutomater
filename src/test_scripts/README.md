# Test Scripts

## Directory purpose

Put your test scripts here.

Remember to import your module being tested from the `src/` path. E.g. if testing `FileManager` in `src/file_manager/file_manager.py`, your test script needs the line

`from src/file_manager/file_manager.py`

near the top.

This is needed since the file being tested may assume that the root of this project is the top level heirarchy.

## Running your test script

To run your test script, run it from the `test_driver.py` in the root directory as

`python3 test_driver.py <test_script>`

where `<test_script>` is the name of the test script (including the `.py` extension).