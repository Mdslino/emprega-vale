package models

import (
	"github.com/jinzhu/gorm"
	"github.com/satori/go.uuid"
	"time"
)

type Model struct {
	ID        uuid.UUID `json:"id" gorm:"type:uuid;primary_key"`
	CreatedAt time.Time `json:"createdAt"`
	UpdatedAt time.Time `json:"updatedAt"`
}

func (base *Model) BeforeCreate(scope *gorm.Scope) error {
	uid := uuid.NewV4()

	return scope.SetColumn("ID", uid)
}
