package utils

import (
	"github.com/iancoleman/strcase"
	"gopkg.in/go-playground/validator.v9"
)

func ListOfErrors(e error) []map[string]string {
	ve := e.(validator.ValidationErrors)
	invalidFields := make([]map[string]string, 0)

	for _, e := range ve {
		errors := map[string]string{}
		errors["field"] = strcase.ToLowerCamel(e.Field())
		errors["validation"] = e.Tag()
		invalidFields = append(invalidFields, errors)
	}

	return invalidFields
}
