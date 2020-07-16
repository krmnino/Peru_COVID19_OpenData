TARGET = CSVtoJSON

OBJS = CSVtoJSON.o

CXX = g++
CXXFLAGS = -std=c++17

$(TARGET):	$(OBJS)	
		$(CXX) $(CXXFLAGS) $(OBJS) -g -o $(TARGET) $(LDFLAGS)
		rm -f *.o

clean:
		rm -f *.o $(TARGET)

CSVtoJSON.o: 	CSVtoJSON.cpp

