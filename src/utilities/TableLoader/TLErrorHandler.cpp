#include "TLErrorHandler.hpp"

namespace tl {
TL_Error::TL_Error() {
	this->err_code = TLErrorCode::OK;
}

TL_Error::TL_Error(TLErrorCode error) {
	this->err_code = error;
	switch (this->err_code) {
	case TLErrorCode::OK:
		break;
	case TLErrorCode::INVALID_ROW_LEGNTH:
		this->message = "Input row length does not match table row length.";
		break;
	case TLErrorCode::FIELD_NOT_FOUND:
		this->message = "Field name does not exist in table instance.";
		break;
	case TLErrorCode::INVALID_ROW_INDEX:
		this->message = "Input row index is out of bounds.";
		break;
	case TLErrorCode::INVALID_COLUMN_INDEX:
		this->message = "Input column index is out of bounds.";
		break;
	case TLErrorCode::DUPLICATE_FIELD:
		this->message = "Field name passed already exist in table instance.";
		break;
	case TLErrorCode::UNEVEN_TABLES:
		this->message = "Column count between two tables is not the same.";
		break;
	case TLErrorCode::UNEVEN_NEW_HEADER:
		this->message = "The size of the new header does not match the current table header length.";
		break;
	default:
		this->message = "Undefinded error.";
		break;
	}
}

TL_Error::~TL_Error() noexcept {}

const char* TL_Error::what() const noexcept {
	return this->message.c_str();
}

TLErrorCode TL_Error::get_error_code() {
	return this->err_code;
}
}
