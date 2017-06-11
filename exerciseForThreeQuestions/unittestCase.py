import unittest 
import traceback

def getNew_results(results):
    '''get new_results'''
    new_results = str(len(results))+'\n'
    for i in results:
        new_results += str(i)+'\n'
    return new_results

def getAnswer_results(answer_path):
    '''get answer_results'''
    answer_file = open(answer_path)
    answer_results = ''
    while 1:
        line = answer_file.readline()
        if not line:
            break
        else:
            answer_results += line
    return answer_results

class ParametrizedTestCase(unittest.TestCase):  
    """ TestCase classes that want to be parametrized should 
        inherit from this class. 
    """  
    def __init__(self, methodName='runTest', results=None,answer_path=None):  
        super(ParametrizedTestCase, self).__init__(methodName)  
        self.results = results  
        self.answer_path = answer_path 
    @staticmethod  
    def parametrize(testcase_class, results=None,answer_path=None):  
        """ Create a suite containing all tests taken from the given 
            subclass, passing them the parameter 'param'. 
        """  
        testloader = unittest.TestLoader()  
        testnames = testloader.getTestCaseNames(testcase_class)  
        suite = unittest.TestSuite()  
        for name in testnames:  
            suite.addTest(testcase_class(name, results=results,answer_path=answer_path))  
        return suite

class TestOne(ParametrizedTestCase):  
    def testTheAnswer(self):  
        # print ('results ='+str(self.results)  )
        # print ('answer_path ='+str(self.answer_path))  
        # print ('the new results ='+str(getNew_results(self.results)))  
        # print ('the answer ='+str(getAnswer_results(self.answer_path)))  
        try:
            self.assertEqual(getNew_results(self.results),getAnswer_results(self.answer_path)) 
        except:
            print('与答案不一致') 
    
def testUnit(results_new,answer_path_new):
    suite = unittest.TestSuite()  
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, results=results_new,answer_path=answer_path_new))  
    unittest.TextTestRunner(verbosity=2).run(suite)  


