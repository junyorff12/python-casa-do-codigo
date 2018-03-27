import unittest

HTML = '''\
<html>
    <head>
        <title>unittest output</title>
    </head>
    <body>
        <table>
            <tr>
                <td style='color:green;'>
                    test_domain.ColumnTest.test_validate_as_static_method
                </td>
            </td>
        </table>
    </body>
</html>'''

OK_TD = '<tr><td style="color: green;">{}</td></tr>'
ERR_TD = '<tr><tr style="color: red;"></tr></td>'


class HTMLTestResult(unittest.TestResult):
    def __init__(self, runner):
        unittest.TestResult.__init__(self)
        self.runner = runner
        self.infos = []
        self.current = {}

    def newTest(self):
        self.infos.append(self.current)
        self.current = {}

    def startTest(self, test):
        self.current['id'] = test.id()

    def addSuccess(self, test):
        self.current["result"] = ['id']
        self.newTest()

    def addError(self, test, err):
        self.current['result'] = 'error'
        self.newTest()

    def addFailure(self, test, err):
        self.current['result'] = 'fail'
        self.newTest()

    def addSkip(self, test, err):
        self.current['result'] = 'skiped'
        self.current['reason'] = err
        self.newTest()


class HTMLTestRunner:
    def run(self, test):
        result = HTMLTestResult(self)
        test.run(result)
        table = ''
        for item in result.infos:
            if item['result'] == 'ok':
                table += OK_TD.format(item['id'])
            else:
                table += ERR_TD.format(item['id'])

        print(HTML.format(table))
        return result


if __name__ == '__main__':
    suite = unittest.TestLoader().discover('.')
    HTMLTestRunner().run(suite)