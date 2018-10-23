from collections import deque
import json

from MisteriumGameParsers.PrecompiledExpressions import EXPERIENCE_EXPR, FINISH_EXPRESSIONS, \
    WORD_COUNT_EXPRESSIONS, SPECIAL_WORDS_EXPRESSIONS
import copy

# TODO: i_belekhov remake this class to work with strings and post content itself and not a feed from parser
# TODO: in the end we should have a data structure converted to JSon for further use

class BasicParser:

    def __init__(self):
        self.__postContent = [] # list of strings
        self.threeLineSegment = deque(maxlen=3)

        self.initLocalProperties(self.__class__)


    def initLocalProperties(self, classRef):
        self.STARTSWITH = getattr(classRef, "STARTSWITH")
        self.ENDSWITH = getattr(classRef, "ENDSWITH")
        self.LINE_STARTSWITH_HANDLERS = getattr(classRef, "LINE_STARTSWITH_HANDLERS")
        self.LINE_ENDSWITH_HANDLERS = getattr(classRef, "LINE_ENDSWITH_HANDLERS")
        self.LINE_MATCH_HANDLERS = getattr(classRef, "LINE_MATCH_HANDLERS")
        self.LINE_ALL_HANDLERS = getattr(classRef, "LINE_ALL_HANDLERS")

    # In this method we do main processing
    def process(self, rawData):
        if not isinstance(rawData, list):
            assert "BaseClassParser should be provided with list of strings as rawData"
        for line in rawData:
            self.threeLineSegment.append(line)
            if len(self.threeLineSegment) == 3:
                self.process_segment()
        # Заходим сюда если итерирование закончено, а значит нам нужно из буфера стащить всё оставшееся содержимое
        # Учитывая предыдущую обработку там всегда окажется 2 строки или одна.
        else:
            for line in self.threeLineSegment:
                if line != "":
                    self.__postContent.append(line)

    def process_segment(self):
        if len(self.threeLineSegment) != 3:
            return

        isSomeLineProcessed = False
        print("==== Processing segment ====")
        # For debug
        self.show_buffer()

        # Если мы смогли запроцессить хотя бы одну строку, значит буфер изменился.
        # Необходимо почистить и пустить процесс заново
        for line in self.threeLineSegment:
            if self.processLine(line):
                isSomeLineProcessed = True
                self.clean_buffer()
                break

        print("==== Stopped processing segment ====")
        # For debug
        self.show_buffer()

        # Первая строка после обработки всегда должна быть правильной, по идее. Не надо надеяться, надо делать по уму
        if not isSomeLineProcessed:
            self.__postContent.append(self.threeLineSegment[0])
            self.threeLineSegment[0] = ""
            self.clean_buffer()

    # ========================= Utilities ==============================================================================

    # Чистим буфер от пустых строк чтобы было попроще его обрабатывать
    def clean_buffer(self):
        oldBuffer = [line for line in self.threeLineSegment if line != ""]
        self.threeLineSegment.clear()
        for line in oldBuffer:
            self.threeLineSegment.append(line)

    # Показываем буффер
    def show_buffer(self):
        for line in self.threeLineSegment:
            print(line)

    def showResultingContent(self):
        for line in self.__postContent:
            print(line)

    def getContentAndCleanUp(self):
        postContent = copy.deepcopy(self.__postContent)
        self.__postContent.clear()
        self.threeLineSegment.clear()
        return postContent

    # ========================= Processing =============================================================================

    # Обобщение обработчиков выражений
    def processLine(self, line):
        for handler in self.LINE_ALL_HANDLERS:
            if handler(self, line):
                return True
        return False

    def processLineStartsWith(self, line):
        for handler in self.LINE_STARTSWITH_HANDLERS:
            if handler(self, line):
                return True
        return False

    def processLineEndsWith(self, line):
        for handler in self.LINE_ENDSWITH_HANDLERS:
            if handler(self, line):
                return True
        return False

    # ========================= Match handlers =========================================================================
    # TODO: i_belekhov убираем специальные слова из этого обработчика
    def loneWordHandler(self, line):
        WCE = WORD_COUNT_EXPRESSIONS
        if WCE.SINGLE_NON_SPECIAL_WORD_EXPR.match(line) and not WCE.DOUBLE_WORD_EXPR.match(line) \
                and not any(expr.match(line) for expr in SPECIAL_WORDS_EXPRESSIONS):
            lineIndex = self.threeLineSegment.index(line)
            if lineIndex >= 1:
                self.threeLineSegment[lineIndex-1] += " " + line
                self.threeLineSegment[lineIndex] = ""
                return True

    def experience_handler(self, line):
        if EXPERIENCE_EXPR.match(line):
            lineIndex = self.threeLineSegment.index(line)
            if lineIndex >= 1:
                self.threeLineSegment[lineIndex-1] += " баллов опыта"
                self.threeLineSegment[lineIndex] = ""
                return True

    # ========================= startsWith handlers ====================================================================
    def general_startswith_handler(self, line):
        for start in self.STARTSWITH:
            if line.startswith(start):
                lineIndex = self.threeLineSegment.index(line)
                if lineIndex > 0:
                    self.threeLineSegment[lineIndex - 1] += " " + line
                    self.threeLineSegment[lineIndex] = ""
                    return True
                else:
                    print("We did something wrong in parsing. lineIndex = %d for startswith case" % lineIndex)
                    return False

    # ========================= endsWith handlers ======================================================================
    def general_endswith_handler(self, line, endsWith=None):
        for end in self.ENDSWITH:
            if line.endswith(end):
                lineIndex = self.threeLineSegment.index(line)
                if lineIndex == 1:
                    self.threeLineSegment[lineIndex] += " " + self.threeLineSegment[lineIndex + 1]
                    self.threeLineSegment[lineIndex + 1] = ""
                    return True
            else:
                return False

    # TODO: i_belekhov необходимо разбить обработчики на виды "начинает с", "оканчивается этим", "совпадает с паттерном"
    LINE_STARTSWITH_HANDLERS = (
        general_startswith_handler,
    )

    STARTSWITH = (
        "-",
        ".",
        ",",
        "+"
    )

    LINE_ENDSWITH_HANDLERS = (
        general_endswith_handler,
    )

    ENDSWITH = (
        "-",
    )

    LINE_MATCH_HANDLERS = (
        loneWordHandler,
        experience_handler,
    )

    # Сначала начало линии, потом конец
    LINE_ALL_HANDLERS = LINE_MATCH_HANDLERS + LINE_STARTSWITH_HANDLERS + LINE_ENDSWITH_HANDLERS


