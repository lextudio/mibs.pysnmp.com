# SNMP MIB module (CISCO-WAN-CES-RSRC-PART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-CES-RSRC-PART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:59 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(cesmPort,) = mibBuilder.importSymbols(
    "CISCO-WAN-CES-PORT-MIB",
    "cesmPort")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanCesRsrcPartMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 41)
)
ciscoWanCesRsrcPartMIB.setRevisions(
        ("2002-09-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesmPortCnfResPartGrp_ObjectIdentity = ObjectIdentity
cesmPortCnfResPartGrp = _CesmPortCnfResPartGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2)
)
_CesmPortCnfResPartGrpTable_Object = MibTable
cesmPortCnfResPartGrpTable = _CesmPortCnfResPartGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cesmPortCnfResPartGrpTable.setStatus("current")
_CesmPortCnfResPartGrpEntry_Object = MibTableRow
cesmPortCnfResPartGrpEntry = _CesmPortCnfResPartGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1)
)
cesmPortCnfResPartGrpEntry.setIndexNames(
    (0, "CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartPortNum"),
    (0, "CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartCtrlrNum"),
)
if mibBuilder.loadTexts:
    cesmPortCnfResPartGrpEntry.setStatus("current")


class _CesmResPartPortNum_Type(Integer32):
    """Custom type cesmResPartPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CesmResPartPortNum_Type.__name__ = "Integer32"
_CesmResPartPortNum_Object = MibTableColumn
cesmResPartPortNum = _CesmResPartPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 1),
    _CesmResPartPortNum_Type()
)
cesmResPartPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesmResPartPortNum.setStatus("current")


class _CesmResPartCtrlrNum_Type(Integer32):
    """Custom type cesmResPartCtrlrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("par", 1),
          ("pnni", 2),
          ("tag", 3))
    )


_CesmResPartCtrlrNum_Type.__name__ = "Integer32"
_CesmResPartCtrlrNum_Object = MibTableColumn
cesmResPartCtrlrNum = _CesmResPartCtrlrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 2),
    _CesmResPartCtrlrNum_Type()
)
cesmResPartCtrlrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesmResPartCtrlrNum.setStatus("current")


class _CesmResPartRowStatus_Type(Integer32):
    """Custom type cesmResPartRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_CesmResPartRowStatus_Type.__name__ = "Integer32"
_CesmResPartRowStatus_Object = MibTableColumn
cesmResPartRowStatus = _CesmResPartRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 3),
    _CesmResPartRowStatus_Type()
)
cesmResPartRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmResPartRowStatus.setStatus("current")


class _CesmResPartNumOfLcnAvail_Type(Integer32):
    """Custom type cesmResPartNumOfLcnAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CesmResPartNumOfLcnAvail_Type.__name__ = "Integer32"
_CesmResPartNumOfLcnAvail_Object = MibTableColumn
cesmResPartNumOfLcnAvail = _CesmResPartNumOfLcnAvail_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 4),
    _CesmResPartNumOfLcnAvail_Type()
)
cesmResPartNumOfLcnAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmResPartNumOfLcnAvail.setStatus("current")


class _CesmResPartLcnLow_Type(Integer32):
    """Custom type cesmResPartLcnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CesmResPartLcnLow_Type.__name__ = "Integer32"
_CesmResPartLcnLow_Object = MibTableColumn
cesmResPartLcnLow = _CesmResPartLcnLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 5),
    _CesmResPartLcnLow_Type()
)
cesmResPartLcnLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmResPartLcnLow.setStatus("current")


class _CesmResPartLcnHigh_Type(Integer32):
    """Custom type cesmResPartLcnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CesmResPartLcnHigh_Type.__name__ = "Integer32"
_CesmResPartLcnHigh_Object = MibTableColumn
cesmResPartLcnHigh = _CesmResPartLcnHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 6),
    _CesmResPartLcnHigh_Type()
)
cesmResPartLcnHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmResPartLcnHigh.setStatus("current")


class _CesmResPartIngrPctBW_Type(Integer32):
    """Custom type cesmResPartIngrPctBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CesmResPartIngrPctBW_Type.__name__ = "Integer32"
_CesmResPartIngrPctBW_Object = MibTableColumn
cesmResPartIngrPctBW = _CesmResPartIngrPctBW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 7),
    _CesmResPartIngrPctBW_Type()
)
cesmResPartIngrPctBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmResPartIngrPctBW.setStatus("current")


class _CesmResPartEgrPctBW_Type(Integer32):
    """Custom type cesmResPartEgrPctBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CesmResPartEgrPctBW_Type.__name__ = "Integer32"
_CesmResPartEgrPctBW_Object = MibTableColumn
cesmResPartEgrPctBW = _CesmResPartEgrPctBW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 8),
    _CesmResPartEgrPctBW_Type()
)
cesmResPartEgrPctBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmResPartEgrPctBW.setStatus("current")


class _CesmResPartCtrlrID_Type(Integer32):
    """Custom type cesmResPartCtrlrID based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CesmResPartCtrlrID_Type.__name__ = "Integer32"
_CesmResPartCtrlrID_Object = MibTableColumn
cesmResPartCtrlrID = _CesmResPartCtrlrID_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 2, 1, 1, 9),
    _CesmResPartCtrlrID_Type()
)
cesmResPartCtrlrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesmResPartCtrlrID.setStatus("current")
_CwcRsrcPartMIBConformance_ObjectIdentity = ObjectIdentity
cwcRsrcPartMIBConformance = _CwcRsrcPartMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 41, 2)
)
_CwcRsrcPartMIBCompliances_ObjectIdentity = ObjectIdentity
cwcRsrcPartMIBCompliances = _CwcRsrcPartMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 41, 2, 1)
)
_CwcRsrcPartMIBGroups_ObjectIdentity = ObjectIdentity
cwcRsrcPartMIBGroups = _CwcRsrcPartMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 41, 2, 2)
)

# Managed Objects groups

ciscoWanCesRsrcPartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 41, 2, 2, 1)
)
ciscoWanCesRsrcPartGroup.setObjects(
      *(("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartPortNum"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartCtrlrNum"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartRowStatus"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartNumOfLcnAvail"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartLcnLow"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartLcnHigh"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartIngrPctBW"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartEgrPctBW"),
        ("CISCO-WAN-CES-RSRC-PART-MIB", "cesmResPartCtrlrID"))
)
if mibBuilder.loadTexts:
    ciscoWanCesRsrcPartGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanCesRsrcPartCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 41, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanCesRsrcPartCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-CES-RSRC-PART-MIB",
    **{"cesmPortCnfResPartGrp": cesmPortCnfResPartGrp,
       "cesmPortCnfResPartGrpTable": cesmPortCnfResPartGrpTable,
       "cesmPortCnfResPartGrpEntry": cesmPortCnfResPartGrpEntry,
       "cesmResPartPortNum": cesmResPartPortNum,
       "cesmResPartCtrlrNum": cesmResPartCtrlrNum,
       "cesmResPartRowStatus": cesmResPartRowStatus,
       "cesmResPartNumOfLcnAvail": cesmResPartNumOfLcnAvail,
       "cesmResPartLcnLow": cesmResPartLcnLow,
       "cesmResPartLcnHigh": cesmResPartLcnHigh,
       "cesmResPartIngrPctBW": cesmResPartIngrPctBW,
       "cesmResPartEgrPctBW": cesmResPartEgrPctBW,
       "cesmResPartCtrlrID": cesmResPartCtrlrID,
       "ciscoWanCesRsrcPartMIB": ciscoWanCesRsrcPartMIB,
       "cwcRsrcPartMIBConformance": cwcRsrcPartMIBConformance,
       "cwcRsrcPartMIBCompliances": cwcRsrcPartMIBCompliances,
       "ciscoWanCesRsrcPartCompliance": ciscoWanCesRsrcPartCompliance,
       "cwcRsrcPartMIBGroups": cwcRsrcPartMIBGroups,
       "ciscoWanCesRsrcPartGroup": ciscoWanCesRsrcPartGroup}
)
