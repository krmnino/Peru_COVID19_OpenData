#include "RTPErrorHandler.hpp"

RTP_Error::RTP_Error() {
	this->err_code = ErrorCode::OK;
}

RTP_Error::RTP_Error(ErrorCode error) {
	this->err_code = error;
	switch (this->err_code) {
	case ErrorCode::OK:
		break;
	case ErrorCode::INVALID_STR2INT:
		this->message = "Error: Could not convert string to integer.";
		break;
	case ErrorCode::INVALID_STR2DBL:
		this->message = "Error: Could not convert string to double.";
		break;
	case ErrorCode::UNEQUAL_ROWS:
		this->message = "Error: Expected number of rows.";
		break;
	default:
		this->message = "Undefinded error.";
		break;
	}
}

RTP_Error::~RTP_Error() noexcept {}

const char* RTP_Error::what() const noexcept {
	return this->message.c_str();
}