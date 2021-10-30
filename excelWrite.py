import xlsxwriter

class excelWrite():

    def __init__(self, fileName):
        self.workbook = xlsxwriter.Workbook(fileName)
        self.worksheet = self.openXLSXFile()

    def openXLSXFile(self):
        
        worksheet = self.workbook.add_worksheet()

        # Add a format for the header cells.
        header_format = self.workbook.add_format({
            'border': 1,
            'bg_color': '#C6EFCE',
            'bold': True,
            'text_wrap': True,
            'valign': 'vcenter',
            'indent': 1,
        })
        
        # Freeze pane on the top row
        worksheet.freeze_panes(1, 0)

        # Set up layout of the worksheet.
        worksheet.set_column('A:A', 150)
        worksheet.set_column('B:B', 15)
        worksheet.set_row(0, 25)

        # Write the header cells and some data that will be used in the examples.
        heading1 = 'Sentence'
        heading2 = 'Emotion'
        
        worksheet.write('A1', heading1, header_format)
        worksheet.write('B1', heading2, header_format)

        return worksheet

    def writeText(self, tweetsListWithEmotion) :
        
        for ind in range(len(tweetsListWithEmotion)) :
            tweet, emotion = str(tweetsListWithEmotion[ind][0]), str(tweetsListWithEmotion[ind][1])
            self.worksheet.write('A' + str((ind%1000)+2), tweet)
            self.worksheet.write('B' + str((ind%1000)+2), emotion)

        self.workbook.close()




















