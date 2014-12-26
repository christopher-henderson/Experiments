#!/usr/bin/env python
from __future__ import division
from math import sqrt

class StatsPackage:
        
    def __init__(self, data):
        self.data = data
        self.count = len(self.data)
        self.mean = None
        self.median = None
        self.variance = None
        self.stdDev = None
        self.range = None
        self.avgDeviation = None
        self.avgDifference = None
        
    def calcMean(self):
        self.mean = sum(self.data)/self.count
        return self.mean
    
    def calcMedian(self):
        if self.count % 2 is not 0:
            self.median = self.data[int(self.count/2)]
        else:
            self.median = (self.data[int(self.count/2)] + self.data[int(self.count/2) - 1])/2
        return self.median
    
    def calcVariance(self):
        if not self.mean:
            self.calcMean()
        generator = ((point-self.mean)**2 for point in self.data)
        self.variance = sum(generator)/self.count 
        return self.variance
    
    def calcStdDev(self):
        if not self.variance:
            self.stdDev = sqrt(self.calcVariance())
        else:
            self.stdDev = sqrt(self.variance)
        return self.stdDev
    
    def calcRange(self):
        self.data.sort()
        self.range = abs(self.data[-1] - self.data[0])
        return self.range    

    def calcAverageDeviation(self):
        generator = (abs(point-self.median) for point in self.data)
        self.avgDeviation = sum(generator)/self.count
        return self.avgDeviation
    
    def calcAverageDifference(self):
        self.data.sort()
        generator = (abs(self.data[index+1] - value) for index,value in enumerate(self.data) if self.data[index] is not self.data[-1])
        self.avgDifference = sum(generator)/(self.count-1)
        return self.avgDifference
    
    def histogram(self, interval):
        self.data.sort()
        bottom = self.data[0]
        top = self.data[-1]
        while bottom <= top:
            hist = 0
            for patient in self.data:
                if patient >= bottom and patient < bottom + interval:
                        hist += 1
            print '{BOTTOM}-{TOP} | {DATA}'.format(BOTTOM=bottom, TOP=bottom + interval - 1, DATA='*' * hist)
            bottom += interval
    
    def outside(self, stdevAway):
        pass

    def inside(self, stdevWithin):
        pass
    
def main():
    data = [41,48,43,38,35,37,44,44,44,62,75,77,58,82,39,85,55,54,67,69,69,70,65,72,74,74,74,60,60,60,61,62,63,64,64,64,54,54,55,56,56,56,57,58,59,45,47,47,48,48,50,52,52,53]
    data.sort()
    stats = StatsPackage(data)
    print 'Mean = {DATA}'.format(DATA=stats.calcMean())
    print 'Median = {DATA}'.format(DATA=stats.calcMedian())
    print 'Range = {DATA}'.format(DATA=stats.calcRange())
    print 'Variance = {DATA}'.format(DATA=stats.calcVariance())
    print 'Standard Deviation = {DATA}'.format(DATA=stats.calcStdDev())
    print 'Average Deviation = {DATA}'.format(DATA=stats.calcAverageDeviation())
    stats.histogram(5)
    print 'As per the Empirical Rule the percentage of patients with HDL between 34 and 69.1 is 81.85%.'
    actual = sum(1 for patient in data if patient >= 34 and patient <= 69.1)/len(data)
    print 'Actual percentage of patients with HDL between 34 ad 69.1 is {DATA}%'.format(DATA=actual*100)

main()
