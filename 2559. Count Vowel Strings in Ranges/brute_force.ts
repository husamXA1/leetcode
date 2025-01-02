// Time Limit Exceeded
function vowelStrings(words: string[], queries: number[][]): number[] {
    const results = []
    for (const query of queries) {
        let counter = 0
        for (let i = query[0]; i <= query[1]; i++) {
            if (isVowel(words[i])) counter++
        }
        results.push(counter)
    }
    return results
};

function isVowel(word: string): boolean {
    const vowels = ['a', 'e', 'i', 'o', 'u']
    return vowels.includes(word.at(0)) && vowels.includes(word.at(-1))
}
