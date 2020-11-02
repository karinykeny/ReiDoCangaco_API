DROP VIEW IF EXISTS `reicangaco`.`vendaspordia` ;
USE `reicangaco`;
CREATE 
 OR REPLACE VIEW `vendasdodia` AS
    SELECT 
        `v`.`nome_vendedor` AS `VENDEDOR`,
        `pp`.`qtd_produto` AS `QUANTIDADE`,
        `pro`.`nome_produto` AS `PRODUTO`,
        `pro`.`cod_produto` AS `CODIGO`,
        `pp`.`valor_parcial` AS `VALOR`,
        `p`.`status` AS `SITUACAO`
    FROM
        (((`vendedor` `v`
        JOIN `pedido` `p` ON ((`v`.`cod_vendedor` = `p`.`cod_vendedor`)))
        JOIN `produto_pedido` `pp` ON ((`p`.`cod_pedido` = `pp`.`cod_pedido`)))
        JOIN `produto` `pro` ON ((`pp`.`id_produto` = `pro`.`id_produto`)))
    WHERE
        (`p`.`data_pedido` = (SELECT CURDATE()))
    ORDER BY `pp`.`qtd_produto` DESC;