package models

import uuid "github.com/satori/go.uuid"

type User struct {
	Model
	Email     string    `json:"email" binding:"required,email" gorm:"UNIQUE_INDEX"`
	Password  string    `json:"password,readonly" binding:"required" rw:"w" gorm:"type:varchar(1500)"`
	Activated bool      `json:"-" gorm:"DEFAULT:true"`
	GroupID   uuid.UUID `json:"-" gorm:"type:uuid;not"`
	Group     Group     `json:"group" gorm:"FOREIGNKEY:GroupID"`
}
