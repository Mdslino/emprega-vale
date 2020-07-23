FROM golang:alpine AS builder

RUN apk --no-cache add build-base git musl-dev

WORKDIR /src

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o goapp

FROM alpine:latest

RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

WORKDIR /app

COPY --from=builder /src/goapp/ /app/

EXPOSE 5000

ENTRYPOINT ["./goapp"]