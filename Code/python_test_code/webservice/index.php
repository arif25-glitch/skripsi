<?php

function normalize($str) {
    $str = strtolower($str);
    $str = preg_replace("/[^a-z0-9\s]+/", "", $str);
    return preg_split('/\s+/', $str);
}

function tf_idf($corpus) {
    $tf = [];
    $df = [];
    $idf = [];
    $totalDocs = count($corpus);
    
    foreach ($corpus as $docId => $doc) {
        $tf[$docId] = array_count_values($doc);
        foreach ($doc as $term) {
            if (!isset($df[$term])) {
                $df[$term] = 0;
            }
            $df[$term]++;
        }
    }
    
    foreach ($df as $term => $count) {
        $idf[$term] = log($totalDocs / $count, 10);
    }
    
    $tfidf = [];
    foreach ($tf as $docId => $terms) {
        foreach ($terms as $term => $count) {
            if (!isset($tfidf[$docId])) {
                $tfidf[$docId] = [];
            }
            $tfidf[$docId][$term] = $count * $idf[$term];
        }
    }
    
    return $tfidf;
}

function cosine_similarity($vec1, $vec2) {
    $dotProduct = 0;
    $magnitude1 = 0;
    $magnitude2 = 0;
    
    $allTerms = array_unique(array_merge(array_keys($vec1), array_keys($vec2)));
    
    foreach ($allTerms as $term) {
        $val1 = isset($vec1[$term]) ? $vec1[$term] : 0;
        $val2 = isset($vec2[$term]) ? $vec2[$term] : 0;
        $dotProduct += $val1 * $val2;
        $magnitude1 += $val1 * $val1;
        $magnitude2 += $val2 * $val2;
    }
    
    $magnitude = sqrt($magnitude1) * sqrt($magnitude2);
    
    return $magnitude ? $dotProduct / $magnitude : 0;
}

function levenshtein_ratio($str1, $str2) {
    $distance = levenshtein($str1, $str2);
    $maxLen = max(strlen($str1), strlen($str2));
    return $maxLen == 0 ? 1.0 : 1 - ($distance / $maxLen);
}

function combined_similarity($str1, $str2) {
    $tokens1 = normalize($str1);
    $tokens2 = normalize($str2);
    
    $corpus = [$tokens1, $tokens2];
    $tfidf = tf_idf($corpus);
    
    $cosineSim = cosine_similarity($tfidf[0], $tfidf[1]);
    $levenshteinSim = levenshtein_ratio($str1, $str2);
    
    return ($cosineSim + $levenshteinSim) / 2;
}

// Example usage
$str1 = "Fuzzy Wuzzy was a bear";
$str2 = "Wuzzy fuzzy bear was";

$similarity = combined_similarity($str1, $str2);
echo "The combined similarity between '{$str1}' and '{$str2}' is " . number_format($similarity * 100, 2) . "%\n";

?>
