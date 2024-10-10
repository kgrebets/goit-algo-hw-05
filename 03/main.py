import timeit
from pathlib import Path
from search_alg.boyer_moore_search import boyer_moore_search
from search_alg.kmp_search import kmp_search 
from search_alg.rabin_karp_search import rabin_karp_search

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def measure_time(search_func, text, pattern):
    timer = timeit.Timer(lambda: search_func(text, pattern))
    return timer.timeit(number=50)

def compare_algorithms(file_path, existing_substr, non_existing_substr):
    text = load_text(file_path)

    time_bm_existing = measure_time(boyer_moore_search, text, existing_substr)
    time_kmp_existing = measure_time(kmp_search, text, existing_substr)
    time_rk_existing = measure_time(rabin_karp_search, text, existing_substr)

    time_bm_non_existing = measure_time(boyer_moore_search, text, non_existing_substr)
    time_kmp_non_existing = measure_time(kmp_search, text, non_existing_substr)
    time_rk_non_existing = measure_time(rabin_karp_search, text, non_existing_substr)

    return {
        "existing": {
            "BM": time_bm_existing,
            "KMP": time_kmp_existing,
            "RK": time_rk_existing
        },
        "non_existing": {
            "BM": time_bm_non_existing,
            "KMP": time_kmp_non_existing,
            "RK": time_rk_non_existing
        }
    }

if __name__ == "__main__":
    existing_substring = "дерев"
    non_existing_substring = "non_existing_substring" 

    current_dir = Path(__file__).parent
    article_1_path = current_dir / "article1.txt"
    article_2_path = current_dir / "article2.txt"

    results_article_1 = compare_algorithms(article_1_path, existing_substring, non_existing_substring)
    results_article_2 = compare_algorithms(article_2_path, existing_substring, non_existing_substring)


    print("\nResults for Article 1:")
    print(f"Existing substring     - BM: {results_article_1['existing']['BM']:.6f}, KMP: {results_article_1['existing']['KMP']:.6f}, RK: {results_article_1['existing']['RK']:.6f}")
    print(f"Non-existing substring - BM: {results_article_1['non_existing']['BM']:.6f}, KMP: {results_article_1['non_existing']['KMP']:.6f}, RK: {results_article_1['non_existing']['RK']:.6f}")
    print("\nResults for Article 2:")
    print(f"Existing substring     - BM: {results_article_2['existing']['BM']:.6f}, KMP: {results_article_2['existing']['KMP']:.6f}, RK: {results_article_2['existing']['RK']:.6f}")
    print(f"Non-existing substring - BM: {results_article_2['non_existing']['BM']:.6f}, KMP: {results_article_2['non_existing']['KMP']:.6f}, RK: {results_article_2['non_existing']['RK']:.6f}")


    print("\nFastest algorithm for Article 1 (existing substring):", min(results_article_1['existing'], key=results_article_1['existing'].get))
    print("Fastest algorithm for Article 1 (non-existing substring):", min(results_article_1['non_existing'], key=results_article_1['non_existing'].get))
    print("\nFastest algorithm for Article 2 (existing substring):", min(results_article_2['existing'], key=results_article_2['existing'].get))
    print("Fastest algorithm for Article 2 (non-existing substring):", min(results_article_2['non_existing'], key=results_article_2['non_existing'].get))
