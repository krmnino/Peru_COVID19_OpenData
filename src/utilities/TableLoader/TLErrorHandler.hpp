#ifndef TLERROR
#define TLERROR

#include <exception>
#include <string>

namespace tl {
enum class TLErrorCode {
	OK,
    INVALID_ROW_LEGNTH,
	FIELD_NOT_FOUND,
	INVALID_ROW_INDEX,
	INVALID_COLUMN_INDEX,
	DUPLICATE_FIELD,
	UNEVEN_TABLES,
};

class TL_Error : public std::exception {
protected:
	TLErrorCode err_code;
	std::string message;

public:
	explicit TL_Error();
	explicit TL_Error(TLErrorCode);
	virtual ~TL_Error() noexcept;
	virtual const char* what() const noexcept;
	TLErrorCode get_error_code();
};
}

#endif // !TLERROR