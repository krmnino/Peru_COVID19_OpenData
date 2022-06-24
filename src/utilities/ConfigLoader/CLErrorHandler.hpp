#include <exception>
#include <string>

namespace cl {
enum class CLErrorCode {
	OK,
	SEMICOLON,
	EQUALS_SIGN,
	KEY_NOT_FOUND,
	ADD_KEY_REPEAT,
	FAIL_2_OPEN,
};

class CL_Error : public std::exception {
protected:
	CLErrorCode err_code;
	std::string message;

public:
	explicit CL_Error();
	explicit CL_Error(CLErrorCode);
	virtual ~CL_Error() noexcept;
	virtual const char* what() const noexcept;
	CLErrorCode get_error_code();
};
}
