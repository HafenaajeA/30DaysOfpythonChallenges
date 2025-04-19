class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        """Returns the number of items in the data"""
        return len(self.data)

    def sum(self):
        """Returns the sum of all items in the data"""
        return sum(self.data)

    def min(self):
        """Returns the minimum value in the data"""
        return min(self.data)

    def max(self):
        """Returns the maximum value in the data"""
        return max(self.data)

    def range(self):
        """Returns the range of the data"""
        return self.max() - self.min()

    def mean(self):
        """Returns the mean of the data"""
        return round(self.sum() / self.count(), 2)

    def median(self):
        """Returns the median of the data"""
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid-1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def mode(self):
        """Returns the mode and its count as a dictionary"""
        freq = {}
        for value in self.data:
            freq[value] = freq.get(value, 0) + 1
        mode_value = max(freq.items(), key=lambda x: x[1])
        return {'mode': mode_value[0], 'count': mode_value[1]}

    def var(self):
        """Returns the variance of the data"""
        mean = self.mean()
        squared_diff_sum = sum((x - mean) ** 2 for x in self.data)
        return round(squared_diff_sum / (len(self.data) - 1), 2)

    def std(self):
        """Returns the standard deviation of the data"""
        return round((self.var() ** 0.5), 2)

    def freq_dist(self):
        """Returns the frequency distribution as a list of tuples (percentage, value)"""
        freq = {}
        for value in self.data:
            freq[value] = freq.get(value, 0) + 1
        
        n = len(self.data)
        freq_dist = [(freq[value] * 100.0 / n, value) for value in freq]
        return sorted(freq_dist, reverse=True)