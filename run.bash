echo "-----------------------Data Set Information-----------------------------"
#don't run 3 and 4 at the same time
python3 extract_data.py 300_train.nl 300_train.en sample.dat sample_test.dat result.dat 0.6   #you can change the last number from 0.1- 0.9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ``
#python3 extract_data.py dutch.txt english.txt sample.dat sample_test.dat result.dat 0.6  #you can change the last number from 0.1- 0.9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ``
echo "---------------------------------ada-------------------------------------"
python3 train.py sample.dat hypothesisOut  ada
python3 predict.py hypothesisOut  sample_test.dat > predic_result.dat
python3 compare.py result.dat predic_result.dat

echo "---------------------------------dt--------------------------------------"
python3 train.py sample.dat hypothesisOut  dt
python3 predict.py hypothesisOut  sample_test.dat > predic_result.dat
python3 compare.py result.dat predic_result.dat