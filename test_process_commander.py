import pytest
import process_commander as pc

def test_process_commander():
  pc.hello()
    
def test_data_wrapper_split_works_for_unix():
  data = pc.DataWrapper("unix\nlines")
  results = data.as_lines()

  assert results == ["unix", "lines"]

def test_data_wrapper_split_works_for_windows():
  data = pc.DataWrapper("windows\r\nlines")
  results = data.as_lines()

  assert results == ["windows", "lines"]

def test_data_wrapper_split_works_for_mixed():
  data = pc.DataWrapper("windows\r\nunix\nlines")
  results = data.as_lines()

  assert results == ["windows", "unix", "lines"]

def test_run_works():
  result = pc.run("ls")

  assert result.result == 0

def test_run_result_code_works():
  # I was hoping for the result value being set, exception is ok too
  with pytest.raises(OSError) as e_info:
    result = pc.run("ls -badarg")

