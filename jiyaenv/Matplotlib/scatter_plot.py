import matplotlib.pyplot as plt

#plt.scatter(x,y,color='color_name', marker='marker_style', label='label_name')

hours_studies=[1,2,3,4,5,6,7,8]
exam_scores=[45,55,56,66,78,87,90,98]

plt.scatter(hours_studies,exam_scores,color='green',marker='o',label='Student data')

plt.xlabel(hours_studies)
plt.ylabel(exam_scores)

plt.title('Relationship between exam studies and hours of study')
plt.legend()
plt.grid(True)
plt.show()