class Exercism
  class PythonCurriculum
    def slugs
      %w(
          bob rna-transcription word-count anagram beer-song nucleotide-count
          point-mutations phone-number grade-school robot-name etl leap
          space-age grains gigasecond triangle scrabble-score roman-numerals
          binary prime-factors raindrops allergies
      )
    end

    def locale
      Locale.new('python', 'py', 'py')
    end
  end
end
