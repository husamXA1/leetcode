function vowelStrings(words: string[], queries: number[][]): number[] {
    const prefixSum: number[] = [0]
    let counter = 0
    for (const word of words) {
        if (isVowel(word)) counter++
        prefixSum.push(counter)
    }
    const results: number[] = []
    for (const query of queries) {
        results.push(prefixSum[query[1] + 1] - prefixSum[query[0]])
    }
    return results
};

function isVowel(word: string): boolean {
    const vowels = ['a', 'e', 'i', 'o', 'u']
    return vowels.includes(word.at(0)) && vowels.includes(word.at(-1))
}
