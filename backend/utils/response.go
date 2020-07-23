package utils

import "github.com/gin-gonic/gin"

type ResponseData struct {
	Status int         `json:"status"`
	Meta   interface{} `json:"meta"`
	Data   interface{} `json:"data"`
}

func RespondJson(w *gin.Context, status int, payload interface{}) {
	var response ResponseData

	response.Status = status

	response.Data = payload

	w.JSON(status, response)
}
