package utils

import (
	"golang.org/x/crypto/bcrypt"
	"log"
)

func HashAndSalt(pwd []byte) string {
	hash, err := bcrypt.GenerateFromPassword(pwd, bcrypt.DefaultCost)
	if err != nil {
		log.Fatalln(err.Error())
	}

	return string(hash)
}

func ComparePasswords(hashedPwd string, plainPwd []byte) bool {
	byteHash := []byte(hashedPwd)

	if err := bcrypt.CompareHashAndPassword(byteHash, plainPwd); err != nil {
		log.Println(err)
		return false
	}
	return true
}