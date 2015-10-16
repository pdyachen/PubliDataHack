


2015-10-07 13:02:25 [ERROR ] [Kondor] DatabaseErrorProcess: 
BEGIN SQL-REQUEST:
SELECT BD.* , B.Bonds_Id , BRTV.Bonds_Id , A001.Depository, A001.Portfolio
FROM kplus..Bonds B, kplus..BondsRT BRTV, kplus..BondsDeals BD INNER JOIN kplus..FlattenedHierarchy FH_FILTER ON BD.Folders_Id = FH_FILTER.Folders_Id AND FH_FILTER.Portfolios_Id IN (52883, 55058) LEFT OUTER JOIN Kustom..Depositories A001 ON BD.BondsDeals_Id = A001.DealId AND A001.DealType = BondsDeals AND A001.DealType = BondsDeals
WHERE (B.Bonds_Id = BD.Bonds_Id AND BRTV.Bonds_Id = BD.Bonds_Id AND BD.TypeOfEvent != 'F') 
AND B.StructuredBonds IN ('N', 'A', 'Y')
AND BD.DealStatus <> 'S'
 AND EXISTS (SELECT 1 FROM #E1bonds_temp_table
WHERE BD.Bonds_Id = #E1bonds_temp_table.Bonds_Id )
 
 --MDC
 

 DROP TABLE #E1bonds_temp_table 

END SQL-REQUEST
2015-10-07 13:02:25 [ERROR ] [Kondor] : Cannot perform your action:
Server Message:
	 number(207) severity(16) state(4) line(1)
	Connection Id:482 [kplus@KONDOR-kplus]
Server KONDOR
Message string Invalid column name 'Portfolio'.