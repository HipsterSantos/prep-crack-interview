//linear search 
/**
 * 
 * @param {*} arr 
 * @param {*} n 
 * @returns true
 * 
 * Time complexity: O(n) */
function linearSearch(arr,n){
    for (let i = 0 ; i<arr.length-1;i++ ){
        if(arr[i] == n){
            return true;
        }
    }
}

/**
 * Binary Search
 */

function binarySearch(arr,n){
    let low = 0;
    let high = arr.length-1;

    while(low <= high){
        let mid = Math.floor((low+high)/2);
        if(arr[mid] == n){
            return true;
        }
        else if(arr[mid] < n){
            low = mid+1;
        }
        else{
            high = mid-1;
        }
    }
    return false;               
}

// Sorting algorithms
/**
 * 
 * Bubble sort
 */
let arr = [12,34,4,5]
let [a,b] = arr;
let [b,a] =  arr;
function swap(arr,prev,next){

}
function bubbleSort(arr,n){

}
