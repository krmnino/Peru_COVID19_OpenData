linux:
	g++ -g -std=c++17 -D LINUX							\
	../utilities/DataVariant/Variant.hpp				\
	../utilities/DataVariant/Variant.cpp				\
	../utilities/TableLoader/Table.hpp					\
	../utilities/TableLoader/Table.cpp					\
	../utilities/TableLoader/TLErrorHandler.hpp			\
	../utilities/TableLoader/TLErrorHandler.cpp			\
	../utilities/ConfigLoader/ConfigLoader.hpp			\
	../utilities/ConfigLoader/ConfigLoader.cpp			\
	../utilities/ConfigLoader/Value.hpp					\
	../utilities/ConfigLoader/Value.cpp					\
	../utilities/ConfigLoader/CLErrorHandler.hpp		\
	../utilities/ConfigLoader/CLErrorHandler.cpp		\
	RawTableProcessing.hpp								\
	RTPErrorHandler.hpp									\
	RTPErrorHandler.cpp									\
	ProcessRawTables.cpp								\
	AddBeginRow.cpp										\
	AddEndRow.cpp 										\
	Main.cpp -o rawtableprocessing

clean:
	rm rawtableprocessing