package middleware

import (
	"empregaVale/config"
	"empregaVale/database"
	"empregaVale/models"
	"empregaVale/utils"
	"github.com/appleboy/gin-jwt/v2"
	"github.com/gin-gonic/gin"
	"log"
	"time"
)

var identityKey = "identity"

type login struct {
	Email    string `json:"email" form:"email" binding:"required,email"`
	Password string `json:"password" form:"password" binding:"required"`
}

func AuthMiddleware() *jwt.GinJWTMiddleware {
	authMiddleware, err := jwt.New(&jwt.GinJWTMiddleware{
		Realm:       "Emprega Vale",
		Key:         []byte(config.Config("SECRET")),
		Timeout:     time.Minute * 15,
		MaxRefresh:  time.Hour,
		IdentityKey: identityKey,
		PayloadFunc: func(data interface{}) jwt.MapClaims {
			if v, ok := data.(*models.User); ok {
				return jwt.MapClaims{
					identityKey: v.Email,
					"sub":       v.ID,
					"group":     v.Group.Name,
				}
			}
			return jwt.MapClaims{}
		},
		IdentityHandler: func(context *gin.Context) interface{} {
			claims := jwt.ExtractClaims(context)
			return &models.User{Email: claims[identityKey].(string)}
		},
		Authenticator: func(c *gin.Context) (interface{}, error) {
			var loginValues login
			var user models.User
			if err := c.ShouldBindJSON(&loginValues); err != nil {
				return nil, jwt.ErrMissingLoginValues
			}
			email := loginValues.Email
			password := loginValues.Password

			db := database.DB

			if err := db.Where(&models.User{Email: email}).First(&user).Error; err != nil {
				return nil, jwt.ErrFailedAuthentication
			}

			if utils.ComparePasswords(user.Password, []byte(password)) {
				return &user, nil
			}
			return nil, jwt.ErrFailedAuthentication
		},
		Unauthorized: func(context *gin.Context, code int, message string) {
			context.JSON(code, gin.H{
				"code":    code,
				"message": message,
			})
		},
		TokenLookup:      "header: Authorization, query: token, cookie: jwt",
		TokenHeadName:    "Bearer",
		TimeFunc:         time.Now,
		SigningAlgorithm: "HS512",
	})

	if err != nil {
		log.Fatalln("JWT Error: " + err.Error())
	}

	return authMiddleware
}
