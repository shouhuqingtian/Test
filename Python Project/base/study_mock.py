import mock


# 模拟mock封装
def mock_test(url, method, data, response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, data)
    return res
