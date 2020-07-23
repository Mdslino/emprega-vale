package config

import (
	"os"

	"github.com/joho/godotenv"
)

func Config(key string) string {
	_ = godotenv.Load(".env")
	return os.Getenv(key)
}
