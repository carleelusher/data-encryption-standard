# CS 465 Programming Assignment 1

- Name: Rohit Chivukula 
- Date: February 7th, 2023 

# Data Encryption Standard
A program which implements a secret key encryption system based on Data Encryption Standard (DES). 

## Key Generation functions:
- permute() for generating subkeys from the initial key
- left_shift() for rotating the bits of a given subkey to the left
- compress() for compressing the key

## Initial Permutation (IP) function:
- initial_permute() for rearranging the input data according to the IP table

## Expansion function:
- expand() for expanding the R value of the input data

## Substitution Box (S-box) functions:
- s_box_substitute() for replacing the expanded R value with the result of the S-box substitution
- s_box() for returning the corresponding S-box value for a given 6-bit input

## Permutation function:
- permute() for rearranging the output of the S-box substitution according to the P table

## Final Permutation (FP) function:
- final_permute() for rearranging the output of the permutation function according to the FP table

## Main encryption function:
- encrypt() for combining all the above functions to encrypt a given input data using the DES algorithm

## Main decryption function:
- decrypt() for combining all the above functions to decrypt a given encrypted data using the DES algorithm.

