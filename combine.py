with open("features_test.csv", "w") as res:
    res.write("afe,dsfe,sdf\n")
    for i in range(1, 11):
        with open("features_test_part_" + str(i) + ".csv", "r") as f:
            res.writelines(f.readlines()[1:])
