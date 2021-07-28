#include "Variant.hpp"

Variant::Variant() {
	this->type = INTEGER;
	this->int_data = 0;
}

Variant::Variant(const Variant& src) {
	*this = src;
	if (src.type == STRING) {
		this->string_data = new std::string(*src.string_data);
	}
}

Variant::Variant(int data) {
	this->type = INTEGER;
	this->int_data = data;
}

Variant::Variant(double data) {
	this->type = DOUBLE;
	this->double_data = data;
}

Variant::Variant(std::string data) {
	this->type = STRING;
	this->string_data = new std::string(data);
}

Variant::Variant(bool data) {
	this->type = BOOLEAN;
	this->bool_data = data;
}

Variant::Variant(char data) {
	this->type = CHARACTER;
	this->char_data = data;
}

Variant::~Variant() {
	if (this->type == STRING) {
		delete this->string_data;
	}
}

Variant& Variant::operator= (int data) {
	if (this->type == STRING) {
		delete this->string_data;
	}
	this->type = INTEGER;
	this->int_data = data;
	return *this;
}

Variant& Variant::operator= (double data) {
	if (this->type == STRING) {
		delete this->string_data;
	}
	this->type = DOUBLE;
	this->double_data = data;
	return *this;
}

Variant& Variant::operator= (std::string& data) {
	if (this->type == STRING) {
		delete this->string_data;
	}
	this->type = STRING;
	this->string_data = new std::string(data);
	return *this;
}

Variant& Variant::operator= (bool data) {
	if (this->type == STRING) {
		delete this->string_data;
	}
	this->type = BOOLEAN;
	this->bool_data = data;
	return *this;
}

Variant& Variant::operator= (char data) {
	if (this->type == STRING) {
		delete this->string_data;
	}
	this->type = CHARACTER;
	this->char_data = data;
	return *this;
}

Variant& Variant::operator= (const Variant& data) {
	if (this == &data) {
		return *this;
	}
	if (this->type == STRING) {
		delete this->string_data;
	}
	switch (data.type) {
	case INTEGER:
		this->type = INTEGER;
		this->int_data = data.int_data;
		break;
	case DOUBLE:
		this->type = DOUBLE;
		this->double_data = data.double_data;
		break;
	case STRING:
		this->type = STRING;
		this->string_data = new std::string(*data.string_data);
		break;
	case BOOLEAN:
		this->type = BOOLEAN;
		this->bool_data = data.bool_data;
		break;
	case CHARACTER:
		this->type = CHARACTER;
		this->char_data = data.char_data;
		break;
	default:
		break;
	}
	return *this;
}

void* Variant::operator& () {
	switch (this->type) {
	case INTEGER:
		return (void*)& this->int_data;
		break;
	case DOUBLE:
		return (void*)& this->double_data;
		break;
	case STRING:
		return (void*)& this->string_data;
		break;
	case BOOLEAN:
		return (void*)& this->bool_data;
		break;
	case CHARACTER:
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
	case INTEGER:
		return this->int_data < other.int_data;
	case DOUBLE:
		return this->double_data < other.double_data;
	case STRING:
		return this->string_data < other.string_data;
	case BOOLEAN:
		return this->bool_data < other.bool_data;
	case CHARACTER:
		return this->char_data < other.char_data;
	default:
		break;
	}
	return false;
}

Variant Variant::operator+ (int data) {
	Variant out;
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = this->int_data + data;
		out.type = INTEGER;
		break;
	case DOUBLE:
		out = this->double_data + data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = this->char_data + data;
		out.type = CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator+ (double data) {
	Variant out;
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = (double)this->int_data + data;
		out.type = DOUBLE;
		break;
	case DOUBLE:
		out = this->double_data + data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = (double)this->char_data + data;
		out.type = DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator+ (std::string& data) {
	Variant out;
	if (this->type == INTEGER || this->type == DOUBLE ||
		this->type == BOOLEAN || this->type == CHARACTER) {
		return out;
	}
	switch (this->type) {
	case STRING:
		out = *out.string_data + data;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator+ (const Variant& data) {
	Variant out;
	if (this->type == BOOLEAN || data.type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			out = this->int_data + data.int_data;
			out.type = INTEGER;
			break;
		case DOUBLE:
			out = (double)this->int_data + data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = (char)this->int_data + data.char_data;
			out.type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			out = this->double_data + (double)data.int_data;
			out.type = DOUBLE;
			break;
		case DOUBLE:
			out = this->double_data + data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->double_data + (double)data.char_data;
			out.type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			out = this->char_data + (char)data.int_data;
			out.type = CHARACTER;
			break;
		case DOUBLE:
			out = (double)this->char_data + data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->char_data + data.char_data;
			out.type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case STRING:
		switch (data.type) {
		case STRING:
			out = *this->string_data + *data.string_data;
			out.type = STRING;
			break;
		case CHARACTER:
			out = *this->string_data + std::string(1, data.char_data);
			out.type = STRING;
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
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = this->int_data - data;
		out.type = INTEGER;
		break;
	case DOUBLE:
		out = this->double_data - data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = this->char_data - data;
		out.type = CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator- (double data) {
	Variant out;
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = (double)this->int_data - data;
		out.type = DOUBLE;
		break;
	case DOUBLE:
		out = this->double_data - data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = (double)this->char_data - data;
		out.type = DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator- (const Variant& data) {
	Variant out;
	if ((this->type == STRING || this->type == BOOLEAN) &&
		(data.type == STRING || data.type == BOOLEAN)) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			out = this->int_data - data.int_data;
			out.type = INTEGER;
			break;
		case DOUBLE:
			out = (double)this->int_data - data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = (char)this->int_data - data.char_data;
			out.type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			out = this->double_data - (double)data.int_data;
			out.type = DOUBLE;
			break;
		case DOUBLE:
			out = this->double_data - data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->double_data - (double)data.char_data;
			out.type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			out = this->char_data - (char)data.int_data;
			out.type = CHARACTER;
			break;
		case DOUBLE:
			out = (double)this->char_data - data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->char_data - data.char_data;
			out.type = CHARACTER;
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
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = this->int_data * data;
		out.type = INTEGER;
		break;
	case DOUBLE:
		out = this->double_data * data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = this->char_data * data;
		out.type = CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator* (double data) {
	Variant out;
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = (double)this->int_data * data;
		out.type = DOUBLE;
		break;
	case DOUBLE:
		out = this->double_data * data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = (double)this->char_data * data;
		out.type = DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator* (const Variant& data) {
	Variant out;
	if ((this->type == STRING || this->type == BOOLEAN) ||
		(data.type == STRING || data.type == BOOLEAN)) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			out = this->int_data * data.int_data;
			out.type = INTEGER;
			break;
		case DOUBLE:
			out = (double)this->int_data * data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = (char)this->int_data * data.char_data;
			out.type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			out = this->double_data * (double)data.int_data;
			out.type = DOUBLE;
			break;
		case DOUBLE:
			out = this->double_data * data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->double_data * (double)data.char_data;
			out.type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			out = this->char_data * (char)data.int_data;
			out.type = CHARACTER;
			break;
		case DOUBLE:
			out = (double)this->char_data * data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->char_data * data.char_data;
			out.type = CHARACTER;
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
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = this->int_data / data;
		out.type = INTEGER;
		break;
	case DOUBLE:
		out = this->double_data / data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = this->char_data / data;
		out.type = CHARACTER;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator/ (double data) {
	Variant out;
	if (this->type == STRING || this->type == BOOLEAN) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		out = (double)this->int_data / data;
		out.type = DOUBLE;
		break;
	case DOUBLE:
		out = this->double_data / data;
		out.type = DOUBLE;
		break;
	case CHARACTER:
		out = (double)this->char_data / data;
		out.type = DOUBLE;
		break;
	default:
		break;
	}
	return out;
}

Variant Variant::operator/ (const Variant& data) {
	Variant out;
	if ((this->type == STRING || this->type == BOOLEAN) ||
		(data.type == STRING || data.type == BOOLEAN)) {
		return out;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			out = this->int_data / data.int_data;
			out.type = INTEGER;
			break;
		case DOUBLE:
			out = (double)this->int_data / data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = (char)this->int_data / data.char_data;
			out.type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			out = this->double_data / (double)data.int_data;
			out.type = DOUBLE;
			break;
		case DOUBLE:
			out = this->double_data / data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->double_data / (double)data.char_data;
			out.type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			out = this->char_data / (char)data.int_data;
			out.type = CHARACTER;
			break;
		case DOUBLE:
			out = (double)this->char_data / data.double_data;
			out.type = DOUBLE;
			break;
		case CHARACTER:
			out = this->char_data / data.char_data;
			out.type = CHARACTER;
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
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data++;
		break;
	case DOUBLE:
		this->double_data++;
		break;
	case CHARACTER:
		this->char_data++;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator++ (int) {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data++;
		break;
	case DOUBLE:
		this->double_data++;
		break;
	case CHARACTER:
		this->char_data++;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-- () {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data--;
		break;
	case DOUBLE:
		this->double_data--;
		break;
	case CHARACTER:
		this->char_data--;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-- (int) {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data--;
		break;
	case DOUBLE:
		this->double_data--;
		break;
	case CHARACTER:
		this->char_data--;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (int data) {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data += data;
		break;
	case DOUBLE:
		this->double_data += data;
		break;
	case CHARACTER:
		this->char_data += data;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (double data) {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->double_data = this->int_data + data;
		this->type = DOUBLE;
		break;
	case DOUBLE:
		this->double_data += data;
		break;
	case CHARACTER:
		this->double_data = this->char_data + data;
		this->type = DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator+= (std::string& data) {
	if (this->type == INTEGER || this->type == DOUBLE ||
		this->type == BOOLEAN || this->type == CHARACTER) {
		return *this;
	}
	switch (this->type) {
	case STRING:
		*this->string_data += data;
		break;
	default:
		break;
	}
	return *this;
}


Variant& Variant::operator+= (const Variant& data) {
	if (this->type == BOOLEAN || data.type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			this->int_data += data.int_data;
			this->type = INTEGER;
			break;
		case DOUBLE:
			this->double_data = (double)this->int_data + data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data = (char)this->int_data + data.char_data;
			this->type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			this->double_data += (double)data.int_data;
			this->type = DOUBLE;
			break;
		case DOUBLE:
			this->double_data += data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->double_data += (double)data.char_data;
			this->type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			this->char_data += (char)data.int_data;
			this->type = CHARACTER;
			break;
		case DOUBLE:
			this->double_data = (double)this->char_data + data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data += data.char_data;
			this->type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case STRING:
		switch (data.type) {
		case STRING:
			*this->string_data += *data.string_data;
			break;
		case CHARACTER:
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
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data -= data;
		break;
	case DOUBLE:
		this->double_data -= data;
		break;
	case CHARACTER:
		this->char_data -= data;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-= (double data) {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->double_data = this->int_data - data;
		this->type = DOUBLE;
		break;
	case DOUBLE:
		this->double_data -= data;
		break;
	case CHARACTER:
		this->double_data = this->char_data - data;
		this->type = DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator-= (const Variant& data) {
	if ((this->type == STRING || this->type == BOOLEAN) &&
		(data.type == STRING || data.type == BOOLEAN)) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			this->int_data -= data.int_data;
			this->type = INTEGER;
			break;
		case DOUBLE:
			this->double_data = (double)this->int_data - data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data = (char)this->int_data - data.char_data;
			this->type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			this->double_data -= (double)data.int_data;
			this->type = DOUBLE;
			break;
		case DOUBLE:
			this->double_data -= data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->double_data -= (double)data.char_data;
			this->type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			this->char_data -= (char)data.int_data;
			this->type = CHARACTER;
			break;
		case DOUBLE:
			this->double_data = (double)this->char_data - data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data -= data.char_data;
			this->type = CHARACTER;
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
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data *= data;
		break;
	case DOUBLE:
		this->double_data *= data;
		break;
	case CHARACTER:
		this->char_data *= data;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator*= (double data) {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->double_data = this->int_data * data;
		this->type = DOUBLE;
		break;
	case DOUBLE:
		this->double_data *= data;
		break;
	case CHARACTER:
		this->double_data = this->char_data * data;
		this->type = DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator*= (const Variant& data) {
	if ((this->type == STRING || this->type == BOOLEAN) &&
		(data.type == STRING || data.type == BOOLEAN)) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			this->int_data *= data.int_data;
			this->type = INTEGER;
			break;
		case DOUBLE:
			this->double_data = (double)this->int_data * data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data = (char)this->int_data * data.char_data;
			this->type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			this->double_data *= (double)data.int_data;
			this->type = DOUBLE;
			break;
		case DOUBLE:
			this->double_data *= data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->double_data *= (double)data.char_data;
			this->type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			this->char_data *= (char)data.int_data;
			this->type = CHARACTER;
			break;
		case DOUBLE:
			this->double_data = (double)this->char_data * data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data *= data.char_data;
			this->type = CHARACTER;
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
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->int_data /= data;
		break;
	case DOUBLE:
		this->double_data /= data;
		break;
	case CHARACTER:
		this->char_data /= data;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator/= (double data) {
	if (this->type == STRING || this->type == BOOLEAN) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		this->double_data = this->int_data / data;
		this->type = DOUBLE;
		break;
	case DOUBLE:
		this->double_data /= data;
		break;
	case CHARACTER:
		this->double_data = this->char_data / data;
		this->type = DOUBLE;
		break;
	default:
		break;
	}
	return *this;
}

Variant& Variant::operator/= (const Variant& data) {
	if ((this->type == STRING || this->type == BOOLEAN) &&
		(data.type == STRING || data.type == BOOLEAN)) {
		return *this;
	}
	switch (this->type) {
	case INTEGER:
		switch (data.type) {
		case INTEGER:
			this->int_data /= data.int_data;
			this->type = INTEGER;
			break;
		case DOUBLE:
			this->double_data = (double)this->int_data / data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data = (char)this->int_data / data.char_data;
			this->type = CHARACTER;
			break;
		default:
			break;
		}
		break;
	case DOUBLE:
		switch (data.type) {
		case INTEGER:
			this->double_data /= (double)data.int_data;
			this->type = DOUBLE;
			break;
		case DOUBLE:
			this->double_data /= data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->double_data /= (double)data.char_data;
			this->type = DOUBLE;
			break;
		default:
			break;
		}
		break;
	case CHARACTER:
		switch (data.type) {
		case INTEGER:
			this->char_data /= (char)data.int_data;
			this->type = CHARACTER;
			break;
		case DOUBLE:
			this->double_data = (double)this->char_data / data.double_data;
			this->type = DOUBLE;
			break;
		case CHARACTER:
			this->char_data /= data.char_data;
			this->type = CHARACTER;
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

int Variant::get_type() {
	return this->type;
}

