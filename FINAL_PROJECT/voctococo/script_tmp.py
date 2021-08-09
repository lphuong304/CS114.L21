f_1 = open("C:/repos/voc2coco/sample/valid.txt", "r")
#f_2 = open("sample_ouput.txt", "r")
f_3 = open("C:/repos/voc2coco/sample/annpaths_list.txt", "w")


for l_1 in f_1:
    result = "./sample/Annotations/" + l_1.replace("\n", "") + ".xml\n"
    f_3.writelines(result)

f_1.close()
#f_2.close()
f_3.close()
