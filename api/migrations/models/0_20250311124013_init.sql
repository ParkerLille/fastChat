-- upgrade --
CREATE TABLE IF NOT EXISTS `user_info` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '主键',
    `username` VARCHAR(255) NOT NULL UNIQUE COMMENT '账号',
    `nickname` VARCHAR(255) NOT NULL  COMMENT '昵称',
    `password` VARCHAR(255) NOT NULL  COMMENT '密码',
    `openid` VARCHAR(255) NOT NULL UNIQUE COMMENT 'OpenID',
    `mobile` VARCHAR(15) NOT NULL  COMMENT '手机',
    `avatar` VARCHAR(500)   COMMENT '头像',
    `country` VARCHAR(255)   COMMENT '国家',
    `province` VARCHAR(255)   COMMENT '省份',
    `city` VARCHAR(255)   COMMENT '城市',
    `sex` BOOL   COMMENT '性别' DEFAULT 1,
    `created_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_time` DATETIME(6)   COMMENT '删除时间',
    KEY `idx_user_info_nicknam_a9d217` (`nickname`),
    KEY `idx_user_info_mobile_299e81` (`mobile`)
) CHARACTER SET utf8;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(20) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8;
