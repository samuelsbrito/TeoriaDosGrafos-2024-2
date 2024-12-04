CC = gcc
CFLAGS = -Wall -Wextra -g

SRC = main.c graph.c
OBJ = $(SRC:.c=.o)

TARGET = graph

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all clean
