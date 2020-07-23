package database

import (
	"empregaVale/models"
	"github.com/jinzhu/gorm"
)

var DB *gorm.DB

func Migrate() {
	DB.AutoMigrate(&models.Group{}, &models.User{})
	DB.Model(&models.User{}).AddForeignKey("group_id", "groups(id)", "CASCADE", "CASCADE")
	DB.Model(&models.User{}).AddIndex("idx_group_id", "group_id")

	DB.Create(&models.Group{Name: "Candidate"})
	DB.Create(&models.Group{Name: "Company"})
	DB.Create(&models.Group{Name: "Admin"})

}
