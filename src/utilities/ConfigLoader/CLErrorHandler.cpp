#include "CLErrorHandler.hpp"

namespace cl {
CL_Error::CL_Error() {
	this->err_code = CLErrorCode::OK;
}

CL_Error::CL_Error(CLErrorCode error) {
	this->err_code = error;
	switch (this->err_code) {
	case CLErrorCode::OK:
		break;
	case CLErrorCode::SEMICOLON:
		this->message = "Missing semicolon in config file.";
		break;
	case CLErrorCode::EQUALS_SIGN:
		this->message = "Missing equals sign at an entry in config file.";
		break;
	case CLErrorCode::KEY_NOT_FOUND:
		this->message = "Key not found in config file.";
		break;
	case CLErrorCode::ADD_KEY_REPEAT:
		this->message = "Key already exists in config file.";
		break;
	case CLErrorCode::FAILED_2_OPEN:
		this->message = "Could not open/find specified config file.";
		break;
	default:
		this->message = "Undefinded error.";
		break;
	}
}

CL_Error::~CL_Error() noexcept {}

const char* CL_Error::what() const noexcept {
	return this->message.c_str();
}

CLErrorCode CL_Error::get_error_code() {
	return this->err_code;
}
}
