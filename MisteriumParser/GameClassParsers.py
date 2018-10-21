from HTMLReader.BasePostContentParser import BasePostContentParser
from collections import deque

import re
from MisteriumParser.PrecompiledExpressions import EXPERIENCE_EXPR, FINISH_EXPRESSIONS, \
    WORD_COUNT_EXPRESSIONS, SPECIAL_WORDS_EXPRESSIONS

# TODO: i_belekhov remake this class to work with strings and post content itself and not a feed from parser

class BaseClassesParser(BasePostContentParser):

    def __init__(self):
        super(BaseClassesParser, self).__init__()

        self.__postContent = ""
        self.threeLineSegment = deque(maxlen=3)

    def handle_data(self, data):
        if self.isPostContentEncountered:
            self.threeLineSegment.append(str(data).strip())
            self.process_threeLines()

    # идём окошечком в три линии и обрабатываем. Как показывает практика - трёх линий достаточно
    # TODO: внутренние обработки лучше вынести в отдельные функции, типа как регэкспы
    def process_threeLines(self):
        if len(self.threeLineSegment) != 3:
            return

        # For debug
        self.show_buffer()

        # Если мы смогли запроцессить хотя бы одну строку, значит буфер изменился.
        # Необходимо почистить и пустить процесс заново
        for line in self.threeLineSegment:
            if self.processLine(line):
                self.clean_buffer()
                break

        # Пост-процессинг строк
        for line in self.threeLineSegment:
            if self.isLineFinished(line):
                print("pattern matched")
                self.__postContent += line + '\n'
                lineIndex = self.threeLineSegment.index(line)
                self.threeLineSegment[lineIndex] = ""
                self.clean_buffer()
                break

    # ========================= Utilities ==============================================================================

    # Чистим буфер от пустых строк чтобы было попроще его обрабатывать
    def clean_buffer(self):
        oldBuffer = [line for line in self.threeLineSegment if line != ""]
        self.threeLineSegment.clear()
        for line in oldBuffer:
            self.threeLineSegment.append(line)

    # Показываем буффер
    def show_buffer(self):
        print("==== Buffer starts here ====")
        for line in self.threeLineSegment:
            print(line)

    def showResultingContent(self):
        print(self.__postContent)

    # ========================= Processing =============================================================================

    # Обобщение обработчиков выражений
    def processLine(self, line):
        for handler in BaseClassesParser.LINE_ALL_HANDLERS:
            if handler(self, line):
                return True
        return False

    def processLineMatch(self, line):
        for handler in BaseClassesParser.LINE_MATCH_HANDLERS:
            if handler(self, line):
                return True
        return False

    def processLineStartsWith(self, line):
        for handler in BaseClassesParser.LINE_STARTSWITH_HANDLERS:
            if handler(self, line):
                return True
        return False

    def processLineEndsWith(self, line):
        for handler in BaseClassesParser.LINE_ENDSWITH_HANDLERS:
            if handler(self, line):
                return True
        return False

    # Подразумевается, что если line удовлетворяет финальным паттернам, то её надо
    # флашить как готовую и переходить к обработке следующих строк
    def isLineFinished(self, line):
        for pattern in FINISH_EXPRESSIONS:
            if pattern.match(line):
                return True
        return False

    # ========================= Match handlers =========================================================================
    def experience_handler(self, line):
        if EXPERIENCE_EXPR.match(line):
            lineIndex = self.threeLineSegment.index(line)
            if lineIndex >= 1:
                self.threeLineSegment[lineIndex-1] += " баллов опыта"
                self.threeLineSegment[lineIndex] = ""
                return True



    def special_word_handler(self, line):
        if any(expr.match(line) for expr in SPECIAL_WORDS_EXPRESSIONS):
            return True

    # TODO: i_belekhov убираем специальные слова из этого обработчика
    def loneWordHandler(self, line):
        WCE = WORD_COUNT_EXPRESSIONS
        if WCE.SINGLE_NON_SPECIAL_WORD_EXPR.match(line) and not WCE.DOUBLE_WORD_EXPR.match(line):
            lineIndex = self.threeLineSegment.index(line)
            if lineIndex >= 1:
                self.threeLineSegment[lineIndex-1] += " " + line
                self.threeLineSegment[lineIndex] = ""
                return True


    # ========================= startsWith handlers ====================================================================
    def general_startswith_handler(self, line):
        for start in BaseClassesParser.STARTSWITH:
            if line.startswith(start):
                lineIndex = self.threeLineSegment.index(line)
                if lineIndex > 0:
                    self.threeLineSegment[lineIndex - 1] += " " + line
                    self.threeLineSegment[lineIndex] = ""
                    return True
                else:
                    print("We did something wrong in parsing. lineIndex = %d for startswith case" % lineIndex)
                    return False
            else:
                return False

    # ========================= endsWith handlers ======================================================================
    def general_endswith_handler(self, line, endsWith=None):
        for end in BaseClassesParser.ENDSWITH:
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
        ","
    )

    LINE_ENDSWITH_HANDLERS = (
        general_endswith_handler,
    )

    ENDSWITH = (
        "-",
    )

    # Расположение в этом тупле имеет значение. Те что идут раньше - обрабатываются раньше
    LINE_MATCH_HANDLERS = (
        special_word_handler,
        experience_handler,
        loneWordHandler,
    )

    # Сначала точные совпадения, потом начало линии, потом конец
    LINE_ALL_HANDLERS = LINE_MATCH_HANDLERS + LINE_STARTSWITH_HANDLERS + LINE_ENDSWITH_HANDLERS

    # Подразумевается, что если line удовлетворяет этим паттернам, то её надо
    # флашить как готовую и переходить к обработке следующих строк
    FLUSH_MATCH_HANDLERS = (

    )
