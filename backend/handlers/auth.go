package handlers

import (
	"empregaVale/config"
	"empregaVale/database"
	"empregaVale/models"
	"empregaVale/utils"
	"github.com/dgrijalva/jwt-go"
	"github.com/gin-gonic/gin"
	"time"
)

type registerInput struct {
	Email string `json:"email" binding:"required,email"`
	Password string `json:"password" binding:"required"`
	Group string `json:"group" binding:"required"`
}


func Register(c *gin.Context) {
	db := database.DB
	var register registerInput
	var group models.Group

	if err := c.ShouldBindJSON(&register); err != nil {
		utils.RespondJson(c, 422, err)
		return
	}

	if err := db.Where(&models.Group{Name: register.Group}).First(&group).Error; err != nil {
		utils.RespondJson(c, 400, err.Error())
		return
	}

	user := models.User{
		Email:     register.Email,
		Password:  utils.HashAndSalt([]byte(register.Password)),
		Activated: true,
		GroupID:   group.ID,
	}

	if err := db.Create(&user).Error; err != nil {
		utils.RespondJson(c, 400, err.Error())
		return
	}

	token := jwt.New(jwt.SigningMethodHS512)

	claims := token.Claims.(jwt.MapClaims)
	claims["identity"] = user.Email
	claims["sub"] = user.ID
	claims["group"] = user.Group.Name
	claims["exp"] = time.Now().Add(time.Minute * 15).Unix()
	claims["orig_iat"] = time.Now().Add(time.Minute * 15).Unix()

	t, err := token.SignedString([]byte(config.Config("SECRET")))
	if err != nil {
		utils.RespondJson(c, 401, err)
		return
	}

	utils.RespondJson(c, 201, gin.H{"email": user.Email, "token": t})
}
