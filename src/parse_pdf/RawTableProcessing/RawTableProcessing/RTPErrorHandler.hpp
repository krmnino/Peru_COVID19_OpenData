#include <exception>
#include <string>

enum class ErrorCode {
	OK,
	INVALID_STR2INT,
	INVALID_STR2DBL,
	UNEQUAL_ROWS,
};

class RTP_Error : public std::exception {
protected:
	ErrorCode err_code;
	std::string message;

public:
	explicit RTP_Error();
	explicit RTP_Error(ErrorCode);
	virtual ~RTP_Error() noexcept;
	virtual const char* what() const noexcept;
};