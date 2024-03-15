echo "========================"
echo "Running Test 1"
echo "========================"
python3 test_1.py

echo "========================"
echo "Running Test 2"
echo "========================"
python3 test_2.py

echo "========================"
echo "Running Test 3"
echo "========================"
python3 test_3.py

echo "========================"
echo "Running Unit Tests"
echo "========================"
pytest

echo "========================"
echo "Pylint"
echo "========================"
pylint test_2.py
