
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sofar = 0
        m_end = 0
        for a in range(0,len(nums)-1):
            m_end = m_end + nums[a]
            if(m_sofar < m_end):
                m_sofar = m_end
            if(m_end < 0):
                m_end = 0

        return m_sofar
