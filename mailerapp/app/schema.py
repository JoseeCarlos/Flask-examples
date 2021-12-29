instructions = [
    'DROP TABLE IF EXISTS `email`;',
    """
    CREATE TABLE `email` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `email` varchar(255) NOT NULL,
        `subject` varchar(255) NOT NULL,
        `content` varchar(255) NOT NULL,
        PRIMARY KEY (`id`)
        );
        """,
]