#############################################################################
#
#    Makefile
#
#############################################################################


CXX      = g++
CXXFLAGS = -std=c++11 -g -O2 -Wall -Wextra

tester: tester.cpp implement_hw.o
	$(CXX) $(CXXFLAGS) -o hw implement_hw.o tester.cpp

implement_hw.o: implement_hw.cpp implement_hw.h
	$(CXX) $(CXXFLAGS) -c implement_hw.cpp

clean:
	rm -f hw *.o *~