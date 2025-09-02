def hIndex(citations):
    n = len(citations)
    paper_counts = [0] * (n+1)   # reason for (n+1) is because 0 takes up a spot nad h-index is max upto len(citations)
    for c in citations:
        paper_counts[min(c, n)] += 1     # Here the length is defined but citations could be more. H-Index is limited to the length of citations

    h = n
    papers = paper_counts[h] # Last value so decrementing on our way down to find h_index

    while h > papers:
        h -= 1
        papers += paper_counts[h]
    return h


citations = [3,0,6,1,5]
print(hIndex(citations))