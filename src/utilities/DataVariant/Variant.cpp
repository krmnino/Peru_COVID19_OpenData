#include "Variant.hpp"

Variant::Variant() {
	this->type = DataType::INTEGER;
	this->int_data = 0;
}

Variant::Variant(const Variant& src) {
	if (src.type == DataType::STRING) {
		this->type = DataType::STRING;
		this->string_data = new std::string(*src.string_data);
	}
	else {
		*this = src;
	}
}

Variant::Variant(int data) {
	this->type = DataType::INTEGER;
	this->int_data = (INT)data;
}

Variant::Variant(INT data) {
	this->type = DataType::INTEGER;
	this->int_data = data;
}

Variant::Variant(double data) {
	this->type = DataType::DOUBLE;
	this->double_data = data;
}

Variant::Variant(std::string data) {
	this->type = DataType::STRING;
	this->string_data = new std::string(data);
}

Variant::Variant(const char* data) {
	this->type = DataType::STRING;
	this->string_data = new std::string(data);
}

Variant::Variant(bool data) {
	this->type = DataType::BOOLEAN;
	this->bool_data = data;
}

Variant::Variant(char data) {
	this->type = DataType::CHARACTER;
	this->char_data = data;
}

Variant::~Variant() {
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
}

Variant& Variant::operator= (INT data) {
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	this->type = DataType::INTEGER;
	this->int_data = data;
	return *this;
}

Variant& Variant::operator= (int data) {
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	this->type = DataType::INTEGER;
	this->int_data = (INT)data;
	return *this;
}

Variant& Variant::operator= (double data) {
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	this->type = DataType::DOUBLE;
	this->double_data = data;
	return *this;
}

Variant& Variant::operator= (std::string& data) {
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	this->type = DataType::STRING;
	this->string_data = new std::string(data);
	return *this;
}

Variant& Variant::operator= (const char* data){
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	this->type = DataType::STRING;
	this->string_data = new std::string(data);
	return *this;
}

Variant& Variant::operator= (bool data) {
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	this->type = DataType::BOOLEAN;
	this->bool_data = data;
	return *this;
}

Variant& Variant::operator= (char data) {
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	this->type = DataType::CHARACTER;
	this->char_data = data;
	return *this;
}

Variant& Variant::operator= (const Variant& data) {
	if (this == &data) {
		return *this;
	}
	if (this->type == DataType::STRING) {
		delete this->string_data;
	}
	switch (data.type) {
	case DataType::INTEGER:
		this->type = DataType::INTEGER;
		this->int_data = data.int_data;
		break;
	case DataType::DOUBLE:
		this->type = DataType::DOUBLE;
		this->double_data = data.double_data;
		break;
	case DataType::STRING:
		this->type = DataType::STRING;
		this->string_data = new std::string(*data.string_data);
		break;
	case DataType::BOOLEAN:
		this->type = DataType::BOOLEAN;
		this->bool_data = data.bool_data;
		break;
	case DataType::CHARACTER:
		this->type = DataType::CHARACTER;
		this->char_data = data.char_data;
		break;
	default:
		break;
	}
	return *this;
}

void* Variant::operator& () {
	switch (this->type) {
	case DataType::INTEGER:
		return (void*)& this->int_data;
		break;
	case DataType::DOUBLE:
		return (void*)& this->double_data;
		break;
	case DataType::STRING:
		return (void*)& this->string_data;
		break;
	case DataType::BOOLEAN:
		return (void*)& this->bool_data;
		break;
	case DataType::CHARACTER:
		return (void*)& this->char_data;
		break;
	default:
		break;
	}
	return (void*)& this->int_data;
}

bool Variant::operator< (const Variant& other) {
	if (this->type != other.type) {
		return false;
	}
	switch (this->type) {
	case DataType::INTEGER:
		return this->int_data < other.int_data;
	case DataType::DOUBLE:
		return this->double_data < other.double_data;
	case DataType::STRING:
		return this->string_data < other.string_data;
	case DataType::BOOLEAN:
		return this->bool_data < other.bool_data;
	case DataType::CHARACTER:
		return this->char_data < other.char_data;
	default:
		break;
	}
	return false;
}

Variant Variant::operator+ (int data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data + data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data + data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = this->char_data + data;
		out.type = DataType::CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator+ (INT data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data + data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data + data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = this->char_data + data;
		out.type = DataType::CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator+ (double data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = (double)this->int_data + data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		out = this->double_data + data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (double)this->char_data + data;
		out.type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator+ (std::string& data) {
	Variant out;
	if (this->type == DataType::INTEGER || this->type == DataType::DOUBLE ||
		this->type == DataType::BOOLEAN || this->type == DataType::CHARACTER) {
		return out;
	}
	switch (this->type) {
	case DataType::STRING:
		out = *out.string_data + data;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator+ (const Variant& data) {
	Variant out;
	if (this->type == DataType::BOOLEAN || data.type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->int_data + data.int_data;
			out.type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			out = (double)this->int_data + data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = (char)this->int_data + (INT)data.char_data;
			out.type = DataType::CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->double_data + (double)data.int_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			out = this->double_data + data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = this->double_data + (double)data.char_data;
			out.type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			out = (INT)this->char_data + (char)data.int_data;
			out.type = DataType::CHARACTER;
			break;
		case DataType::DOUBLE:
			out = (double)this->char_data + data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = this->char_data + (INT)data.char_data;
			out.type = DataType::CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DataType::STRING:
		switch (data.type) {
		case DataType::STRING:
			out = *this->string_data + *data.string_data;
			out.type = DataType::STRING;
			break;
		case DataType::CHARACTER:
			out = *this->string_data + std::string(1, data.char_data);
			out.type = DataType::STRING;
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator- (int data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data - data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data - data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = this->char_data - data;
		out.type = DataType::CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator- (INT data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data - data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data - data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = this->char_data - data;
		out.type = DataType::CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator- (double data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = (double)this->int_data - data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		out = this->double_data - data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (double)this->char_data - data;
		out.type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator- (const Variant& data) {
	Variant out;
	if ((this->type == DataType::STRING || this->type == DataType::BOOLEAN) &&
		(data.type == DataType::STRING || data.type == DataType::BOOLEAN)) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->int_data - data.int_data;
			out.type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			out = (double)this->int_data - data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = (char)this->int_data - (INT)data.char_data;
			out.type = DataType::CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->double_data - (double)data.int_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			out = this->double_data - data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = this->double_data - (double)data.char_data;
			out.type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			out = (INT)this->char_data - (char)data.int_data;
			out.type = DataType::CHARACTER;
			break;
		case DataType::DOUBLE:
			out = (double)this->char_data - data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = (INT)this->char_data - data.char_data;
			out.type = DataType::CHARACTER;
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator* (int data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data * data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data * data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (INT)this->char_data * data;
		out.type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator* (INT data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data * data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data * data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (INT)this->char_data * data;
		out.type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator* (double data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = (double)this->int_data * data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		out = this->double_data * data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (double)this->char_data * data;
		out.type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator* (const Variant& data) {
	Variant out;
	if ((this->type == DataType::STRING || this->type == DataType::BOOLEAN) ||
		(data.type == DataType::STRING || data.type == DataType::BOOLEAN)) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->int_data * data.int_data;
			out.type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			out = (double)this->int_data * data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = this->int_data * (INT)data.char_data;
			out.type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->double_data * (double)data.int_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			out = this->double_data * data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = this->double_data * (double)data.char_data;
			out.type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			out = (INT)this->char_data * data.int_data;
			out.type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			out = (double)this->char_data * data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = (INT)this->char_data * (INT)data.char_data;
			out.type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator/ (int data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data / data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data / data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (INT)this->char_data / data;
		out.type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator/ (INT data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = this->int_data / data;
		out.type = DataType::INTEGER;
		break;
	case DataType::DOUBLE:
		out = this->double_data / data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (INT)this->char_data / data;
		out.type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator/ (double data) {
	Variant out;
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		out = (double)this->int_data / data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		out = this->double_data / data;
		out.type = DataType::DOUBLE;
		break;
	case DataType::CHARACTER:
		out = (double)this->char_data / data;
		out.type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator/ (const Variant& data) {
	Variant out;
	if ((this->type == DataType::STRING || this->type == DataType::BOOLEAN) ||
		(data.type == DataType::STRING || data.type == DataType::BOOLEAN)) {
		return out;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->int_data / data.int_data;
			out.type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			out = (double)this->int_data / data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = this->int_data / (INT)data.char_data;
			out.type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			out = this->double_data / (double)data.int_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			out = this->double_data / data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = this->double_data / (double)data.char_data;
			out.type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			out = (INT)this->char_data / data.int_data;
			out.type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			out = (double)this->char_data / data.double_data;
			out.type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			out = (INT)this->char_data / data.char_data;
			out.type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return out;
}

Variant& Variant::operator++ () {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data++;
		break;
	case DataType::DOUBLE:
		this->double_data++;
		break;
	case DataType::CHARACTER:
		this->char_data++;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator++ (int) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data++;
		break;
	case DataType::DOUBLE:
		this->double_data++;
		break;
	case DataType::CHARACTER:
		this->char_data++;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-- () {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data--;
		break;
	case DataType::DOUBLE:
		this->double_data--;
		break;
	case DataType::CHARACTER:
		this->char_data--;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-- (int) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data--;
		break;
	case DataType::DOUBLE:
		this->double_data--;
		break;
	case DataType::CHARACTER:
		this->char_data--;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (int data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data += data;
		break;
	case DataType::DOUBLE:
		this->double_data += data;
		break;
	case DataType::CHARACTER:
		this->int_data = (INT)this->char_data + data;
		this->type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (INT data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data += data;
		break;
	case DataType::DOUBLE:
		this->double_data += data;
		break;
	case DataType::CHARACTER:
		this->int_data = (INT)this->char_data + data;
		this->type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (double data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->double_data = this->int_data + data;
		this->type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		this->double_data += data;
		break;
	case DataType::CHARACTER:
		this->double_data = this->char_data + data;
		this->type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (const char* data) {
	if (this->type == DataType::INTEGER || this->type == DataType::DOUBLE ||
		this->type == DataType::BOOLEAN || this->type == DataType::CHARACTER) {
		return *this;
	}
	switch (this->type) {
	case DataType::STRING:
		*this->string_data += std::string(data);
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (std::string& data) {
	if (this->type == DataType::INTEGER || this->type == DataType::DOUBLE ||
		this->type == DataType::BOOLEAN || this->type == DataType::CHARACTER) {
		return *this;
	}
	switch (this->type) {
	case DataType::STRING:
		*this->string_data += data;
		break;
	default:
		break;
	}
	return *this;
}


Variant& Variant::operator+= (const Variant& data) {
	if (this->type == DataType::BOOLEAN || data.type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data += data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->int_data + data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data += (INT)data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			this->double_data += (double)data.int_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			this->double_data += data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->double_data += (double)data.char_data;
			this->type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data = (INT)this->char_data + data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->char_data + data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data = (INT)this->char_data + (INT)data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	case DataType::STRING:
		switch (data.type) {
		case DataType::STRING:
			*this->string_data += *data.string_data;
			break;
		case DataType::CHARACTER:
			*this->string_data += std::string(1, data.char_data);
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-= (int data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data -= data;
		break;
	case DataType::DOUBLE:
		this->double_data -= data;
		break;
	case DataType::CHARACTER:
		this->int_data = (INT)this->char_data - data;
		this->type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-= (INT data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data -= data;
		break;
	case DataType::DOUBLE:
		this->double_data -= data;
		break;
	case DataType::CHARACTER:
		this->int_data = (INT)this->char_data - data;
		this->type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-= (double data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->double_data = this->int_data - data;
		this->type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		this->double_data -= data;
		break;
	case DataType::CHARACTER:
		this->double_data = this->char_data - data;
		this->type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-= (const Variant& data) {
	if ((this->type == DataType::STRING || this->type == DataType::BOOLEAN) &&
		(data.type == DataType::STRING || data.type == DataType::BOOLEAN)) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data -= data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->int_data - data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data = this->int_data - (INT)data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			this->double_data -= (double)data.int_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			this->double_data -= data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->double_data -= (double)data.char_data;
			this->type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data = (INT)this->char_data - data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->char_data - data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data = this->char_data - (INT)data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator*= (int data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data *= data;
		break;
	case DataType::DOUBLE:
		this->double_data *= data;
		break;
	case DataType::CHARACTER:
		this->int_data = this->char_data * data;
		this->type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator*= (INT data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data *= data;
		break;
	case DataType::DOUBLE:
		this->double_data *= data;
		break;
	case DataType::CHARACTER:
		this->int_data = this->char_data * data;
		this->type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator*= (double data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->double_data = this->int_data * data;
		this->type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		this->double_data *= data;
		break;
	case DataType::CHARACTER:
		this->double_data = this->char_data * data;
		this->type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator*= (const Variant& data) {
	if ((this->type == DataType::STRING || this->type == DataType::BOOLEAN) &&
		(data.type == DataType::STRING || data.type == DataType::BOOLEAN)) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data *= data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->int_data * data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data = this->int_data * (INT)data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			this->double_data *= (double)data.int_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			this->double_data *= data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->double_data *= (double)data.char_data;
			this->type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data = this->char_data * (INT)data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->char_data * data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data = this->char_data * (INT)data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator/= (int data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data /= data;
		break;
	case DataType::DOUBLE:
		this->double_data /= data;
		break;
	case DataType::CHARACTER:
		this->int_data = this->char_data / data;
		this->type = DataType::INTEGER;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator/= (INT data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->int_data /= data;
		break;
	case DataType::DOUBLE:
		this->double_data /= data;
		break;
	case DataType::CHARACTER:
		this->char_data /= data;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator/= (double data) {
	if (this->type == DataType::STRING || this->type == DataType::BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		this->double_data = this->int_data / data;
		this->type = DataType::DOUBLE;
		break;
	case DataType::DOUBLE:
		this->double_data /= data;
		break;
	case DataType::CHARACTER:
		this->double_data = this->char_data / data;
		this->type = DataType::DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator/= (const Variant& data) {
	if ((this->type == DataType::STRING || this->type == DataType::BOOLEAN) &&
		(data.type == DataType::STRING || data.type == DataType::BOOLEAN)) {
		return *this;
	}
	switch (this->type) {
	case DataType::INTEGER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data /= data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->int_data / data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data = this->int_data / (INT)data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	case DataType::DOUBLE:
		switch (data.type) {
		case DataType::INTEGER:
			this->double_data /= (double)data.int_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::DOUBLE:
			this->double_data /= data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->double_data /= (double)data.char_data;
			this->type = DataType::DOUBLE;
			break;
		default:
			break;
		}
		break;
	case DataType::CHARACTER:
		switch (data.type) {
		case DataType::INTEGER:
			this->int_data = this->char_data / data.int_data;
			this->type = DataType::INTEGER;
			break;
		case DataType::DOUBLE:
			this->double_data = (double)this->char_data / data.double_data;
			this->type = DataType::DOUBLE;
			break;
		case DataType::CHARACTER:
			this->int_data = this->char_data / data.char_data;
			this->type = DataType::INTEGER;
			break;
		default:
			break;
		}
		break;
	default:
		break;
	}
	return *this;
}

DataType Variant::get_type() {
	return this->type;
}
