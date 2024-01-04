class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]
            image[i]=[1 if im==0 else 0 for im in image[i] ] 
        return image

        