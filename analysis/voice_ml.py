'''
    run model code in here
    1. get file url -> file_url
    2. run code
    3. return data
    4. text is str, data is list
'''
def run_ml(file_path):
    # input code here

    # example data
    # you sould follow under data type
    result={}
    text = "어 저의 가장 친한 친구는 냐옹이에요." + '\n' + "음 길가다 우연히 마주쳤어요"
    data = [1,2,3,4]

    #--------
    result['text'] = text
    result['data'] = data
    # print("result: {}".format(result))
    return result