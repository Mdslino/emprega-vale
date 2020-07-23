package router

import (
	"empregaVale/handlers"
	"empregaVale/middleware"
	"empregaVale/utils"
	"github.com/gin-gonic/gin"
)

func healthCheck(context *gin.Context) {
	context.JSON(200, gin.H{
		"code":    200,
		"message": "Working",
		"data":    nil,
	})
}
func SetupRouter() *gin.Engine {
	authMiddleware := middleware.AuthMiddleware()
	router := gin.Default()

	router.GET("/health-check", healthCheck)
	router.GET("", healthCheck)

	api := router.Group("/api")

	apiV1 := api.Group("/v1")

	auth := apiV1.Group("/auth")
	auth.POST("/login", authMiddleware.LoginHandler)
	auth.POST("/refresh-token", authMiddleware.RefreshHandler)
	auth.POST("/register", handlers.Register)
	auth.Use(authMiddleware.MiddlewareFunc())
	{
		auth.GET("/protect", func(context *gin.Context) {
			utils.RespondJson(context, 200, gin.H{"message": "worked"})
		})
	}

	apiV1.GET("", healthCheck)

	return router
}
