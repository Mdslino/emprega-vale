package main

import (
	"empregaVale/config"
	"empregaVale/database"
	"empregaVale/router"
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"strconv"
)

func ConnectDB() {
	var err error

	p := config.Config("DB_PORT")
	port, _ := strconv.ParseUint(p, 10, 32)

	database.DB, err = gorm.Open("postgres", fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", config.Config("DB_HOST"), port, config.Config("DB_USER"), config.Config("DB_PASSWORD"), config.Config("DB_NAME")))

	if err != nil {
		panic(err.Error())
	}

	fmt.Println("Connection Opened to Database")
	database.Migrate()
	fmt.Println("Database Migrated")
}

func main() {
	ConnectDB()

	r := router.SetupRouter()

	r.Run(":5000")

	defer database.DB.Close()
}
