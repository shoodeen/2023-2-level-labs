"""
Lab 4.

Top-p sampling generation and filling gaps with ngrams
"""
# pylint:disable=too-few-public-methods, too-many-arguments
from lab_3_generate_by_ngrams.main import (BeamSearchTextGenerator, GreedyTextGenerator,
                                           NGramLanguageModel, TextProcessor)


class WordProcessor(TextProcessor):
    """
    Handle text tokenization, encoding and decoding.
    """

    def _tokenize(self, text: str) -> tuple[str, ...]:  # type: ignore
        """
        Tokenize text into tokens, separating sentences with special token.

        Punctuation and digits are removed. EoW token is appended after the last word in sentence.

        Args:
            text (str): Original text

        Returns:
            tuple[str, ...]: Tokenized text

        Raises:
            ValueError: In case of inappropriate type input argument or if input argument is empty.
        """

    def _put(self, element: str) -> None:
        """
        Put an element into the storage, assign a unique id to it.

        Args:
            element (str): Element to put into storage

        Raises:
            ValueError: In case of inappropriate type input argument or if input argument is empty.
        """

    def _postprocess_decoded_text(self, decoded_corpus: tuple[str, ...]) -> str:  # type: ignore
        """
        Convert decoded sentence into the string sequence.

        Special symbols are replaced with spaces.
        The first word is capitalized, resulting sequence must end with a full stop.

        Args:
            decoded_corpus (tuple[str, ...]): Tuple of decoded tokens

        Returns:
            str: Resulting text

        Raises:
            ValueError: In case of inappropriate type input argument or if input argument is empty.
        """


class TopPGenerator:
    """
    Generator with top-p sampling strategy.

    Attributes:
        _model (NGramLanguageModel): NGramLanguageModel instance to use for text generation
        _word_processor (WordProcessor): WordProcessor instance to handle text processing
        _p_value (float) : Collective probability mass threshold for generation
    """

    def __init__(
        self, language_model: NGramLanguageModel, word_processor: WordProcessor, p_value: float
    ) -> None:
        """
        Initialize an instance of TopPGenerator.

        Args:
            language_model (NGramLanguageModel):
                NGramLanguageModel instance to use for text generation
            word_processor (WordProcessor): WordProcessor instance to handle text processing
            p_value (float): Collective probability mass threshold
        """

    def run(self, seq_len: int, prompt: str) -> str:  # type: ignore
        """
        Generate sequence with top-p sampling strategy.

        Args:
            seq_len (int): Number of tokens to generate
            prompt (str): Beginning of the sequence

        Returns:
            str: Generated sequence

        Raises:
            ValueError: In case of inappropriate type input arguments,
                or if input arguments are empty,
                or if sequence has inappropriate length,
                or if methods used return None.
        """


class GeneratorTypes:
    """
    A class that represents types of generators.

    Attributes:
        greedy (int): Numeric type of Greedy generator
        top_p (int): Numeric type of Top-P generator
        beam_search (int): Numeric type of Beam Search generator
    """

    def __init__(self) -> None:
        """
        Initialize an instance of GeneratorTypes.
        """

    def get_conversion_generator_type(self, generator_type: int) -> str:  # type: ignore
        """
        Retrieve string type of generator.

        Args:
            generator_type (int): Numeric type of the generator

        Returns:
            (str): Name of the generator.
        """


class GenerationResultDTO:
    """
    Class that represents results of QualityChecker.

    Attributes:
        __text (str): Text that used to calculate perplexity
        __perplexity (float): Calculated perplexity score
        __type (int): Numeric type of the generator
    """

    def __init__(self, text: str, perplexity: float, generation_type: int):
        """
        Initialize an instance of GenerationResultDTO.

        Args:
            text (str): The text used to calculate perplexity
            perplexity (float): Calculated perplexity score
            generation_type (int):
                Numeric type of the generator for which perplexity was calculated
        """

    def get_perplexity(self) -> float:  # type: ignore
        """
        Retrieve a perplexity value.

        Returns:
            (float): Perplexity value
        """

    def get_text(self) -> str:  # type: ignore
        """
        Retrieve a text.

        Returns:
            (str): Text for which the perplexity was count
        """

    def get_type(self) -> int:  # type: ignore
        """
        Retrieve a numeric type.

        Returns:
            (int): Numeric type of the generator
        """

    def __str__(self) -> str:  # type: ignore
        """
        Prints report after quality check.

        Returns:
            (str): String with report
        """


class QualityChecker:
    """
    Check the quality of different ways to generate sequence.

    Attributes:
        _generators (dict): Dictionary with generators to check quality
        _language_model (NGramLanguageModel): NGramLanguageModel instance
        _word_processor (WordProcessor): WordProcessor instance
    """

    def __init__(
        self, generators: dict, language_model: NGramLanguageModel, word_processor: WordProcessor
    ) -> None:
        """
        Initialize an instance of QualityChecker.

        Args:
            generators (dict): Dictionary in the form of {numeric type: generator}
            language_model (NGramLanguageModel):
                NGramLanguageModel instance to use for text generation
            word_processor (WordProcessor): WordProcessor instance to handle text processing
        """

    def _calculate_perplexity(self, generated_text: str) -> float:  # type: ignore
        """
        Calculate perplexity for the text made by generator.

        Args:
            generated_text (str): Text made by generator

        Returns:
            float: Perplexity score for generated text

        Raises:
            ValueError: In case of inappropriate type input argument,
                or if input argument is empty,
                or if methods used return None,
                or if nothing was generated.
        """

    def run(self, seq_len: int, prompt: str) -> list[GenerationResultDTO]:  # type: ignore
        """
        Check the quality of generators.

        Args:
            seq_len (int): Number of tokens to generate
            prompt (str): Beginning of the sequence

        Returns:
            list[GenerationResultDTO]:
                List of GenerationResultDTO instances in ascending order of perplexity score

        Raises:
            ValueError: In case of inappropriate type input arguments,
                or if input arguments are empty,
                or if sequence has inappropriate length,
                or if methods used return None.
        """


class Examiner:
    """
    A class that conducts an exam.

    Attributes:
        _json_path (str): Local path to assets file
        _questions_and_answers (dict[tuple[str, int], str]):
            Dictionary in the form of {(question, position of the word to be filled), answer}
    """

    def __init__(self, json_path: str) -> None:
        """
        Initialize an instance of Examiner.

        Args:
            json_path (str): Local path to assets file
        """

    def _load_from_json(self) -> dict[tuple[str, int], str]:  # type: ignore
        """
        Load questions and answers from JSON file.

        Returns:
            dict[tuple[str, int], str]:
                Dictionary in the form of {(question, position of the word to be filled), answer}

        Raises:
            ValueError: In case of inappropriate type of attribute _json_path,
                or if attribute _json_path is empty,
                or if attribute _json_path has inappropriate extension,
                or if inappropriate type loaded data.
        """

    def provide_questions(self) -> list[tuple[str, int]]:  # type: ignore
        """
        Provide questions for an exam.

        Returns:
            list[tuple[str, int]]:
                List in the form of [(question, position of the word to be filled)]
        """

    def assess_exam(self, answers: dict[str, str]) -> float:  # type: ignore
        """
        Assess an exam by counting accuracy.

        Args:
            answers(dict[str, str]): Dictionary in the form of {question: answer}

        Returns:
            float: Accuracy score

        Raises:
            ValueError: In case of inappropriate type input argument or if input argument is empty.
        """


class GeneratorRuleStudent:
    """
    Base class for students generators.
    """

    _generator: GreedyTextGenerator | TopPGenerator | BeamSearchTextGenerator
    _generator_type: int

    def __init__(
        self, generator_type: int, language_model: NGramLanguageModel, word_processor: WordProcessor
    ) -> None:
        """
        Initialize an instance of GeneratorRuleStudent.

        Args:
            generator_type (int): Numeric type of the generator
            language_model (NGramLanguageModel):
                NGramLanguageModel instance to use for text generation
            word_processor (WordProcessor): WordProcessor instance to handle text processing
        """

    def take_exam(self, tasks: list[tuple[str, int]]) -> dict[str, str]:  # type: ignore
        """
        Take an exam.

        Args:
            tasks (list[tuple[str, int]]):
                List with questions in the form of [(question, position of the word to be filled)]

        Returns:
            dict[str, str]: Dictionary in the form of {question: answer}

        Raises:
            ValueError: In case of inappropriate type input argument,
                or if input argument is empty,
                or if methods used return None.
        """

    def get_generator_type(self) -> str:  # type: ignore
        """
        Retrieve generator type.

        Returns:
            str: Generator type
        """
