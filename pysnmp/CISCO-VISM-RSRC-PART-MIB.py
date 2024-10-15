# SNMP MIB module (CISCO-VISM-RSRC-PART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-RSRC-PART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:55 2024
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

(vismPort,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "vismPort")

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

ciscoVismRsrcPartMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 93)
)
ciscoVismRsrcPartMIB.setRevisions(
        ("2003-12-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismPortResPartCnfGrp_ObjectIdentity = ObjectIdentity
vismPortResPartCnfGrp = _VismPortResPartCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2)
)
_VismPortResPartCnfGrpTable_Object = MibTable
vismPortResPartCnfGrpTable = _VismPortResPartCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vismPortResPartCnfGrpTable.setStatus("current")
_VismPortResPartCnfGrpEntry_Object = MibTableRow
vismPortResPartCnfGrpEntry = _VismPortResPartCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1)
)
vismPortResPartCnfGrpEntry.setIndexNames(
    (0, "CISCO-VISM-RSRC-PART-MIB", "vismResPartPortNum"),
    (0, "CISCO-VISM-RSRC-PART-MIB", "vismResPartCtrlrNum"),
)
if mibBuilder.loadTexts:
    vismPortResPartCnfGrpEntry.setStatus("current")


class _VismResPartPortNum_Type(Integer32):
    """Custom type vismResPartPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VismResPartPortNum_Type.__name__ = "Integer32"
_VismResPartPortNum_Object = MibTableColumn
vismResPartPortNum = _VismResPartPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 1),
    _VismResPartPortNum_Type()
)
vismResPartPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismResPartPortNum.setStatus("current")


class _VismResPartCtrlrNum_Type(Integer32):
    """Custom type vismResPartCtrlrNum based on Integer32"""
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


_VismResPartCtrlrNum_Type.__name__ = "Integer32"
_VismResPartCtrlrNum_Object = MibTableColumn
vismResPartCtrlrNum = _VismResPartCtrlrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 2),
    _VismResPartCtrlrNum_Type()
)
vismResPartCtrlrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismResPartCtrlrNum.setStatus("current")


class _VismResPartRowStatus_Type(Integer32):
    """Custom type vismResPartRowStatus based on Integer32"""
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


_VismResPartRowStatus_Type.__name__ = "Integer32"
_VismResPartRowStatus_Object = MibTableColumn
vismResPartRowStatus = _VismResPartRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 3),
    _VismResPartRowStatus_Type()
)
vismResPartRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismResPartRowStatus.setStatus("current")


class _VismResPartNumOfLcnAvail_Type(Integer32):
    """Custom type vismResPartNumOfLcnAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 380),
    )


_VismResPartNumOfLcnAvail_Type.__name__ = "Integer32"
_VismResPartNumOfLcnAvail_Object = MibTableColumn
vismResPartNumOfLcnAvail = _VismResPartNumOfLcnAvail_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 4),
    _VismResPartNumOfLcnAvail_Type()
)
vismResPartNumOfLcnAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismResPartNumOfLcnAvail.setStatus("current")


class _VismResPartLcnLow_Type(Integer32):
    """Custom type vismResPartLcnLow based on Integer32"""
    defaultValue = 131

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismResPartLcnLow_Type.__name__ = "Integer32"
_VismResPartLcnLow_Object = MibTableColumn
vismResPartLcnLow = _VismResPartLcnLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 5),
    _VismResPartLcnLow_Type()
)
vismResPartLcnLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismResPartLcnLow.setStatus("current")


class _VismResPartLcnHigh_Type(Integer32):
    """Custom type vismResPartLcnHigh based on Integer32"""
    defaultValue = 510

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismResPartLcnHigh_Type.__name__ = "Integer32"
_VismResPartLcnHigh_Object = MibTableColumn
vismResPartLcnHigh = _VismResPartLcnHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 6),
    _VismResPartLcnHigh_Type()
)
vismResPartLcnHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismResPartLcnHigh.setStatus("current")


class _VismResPartIngrPctBW_Type(Integer32):
    """Custom type vismResPartIngrPctBW based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismResPartIngrPctBW_Type.__name__ = "Integer32"
_VismResPartIngrPctBW_Object = MibTableColumn
vismResPartIngrPctBW = _VismResPartIngrPctBW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 7),
    _VismResPartIngrPctBW_Type()
)
vismResPartIngrPctBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismResPartIngrPctBW.setStatus("current")


class _VismResPartEgrPctBW_Type(Integer32):
    """Custom type vismResPartEgrPctBW based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismResPartEgrPctBW_Type.__name__ = "Integer32"
_VismResPartEgrPctBW_Object = MibTableColumn
vismResPartEgrPctBW = _VismResPartEgrPctBW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 8),
    _VismResPartEgrPctBW_Type()
)
vismResPartEgrPctBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismResPartEgrPctBW.setStatus("current")


class _VismResPartCtrlrID_Type(Integer32):
    """Custom type vismResPartCtrlrID based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VismResPartCtrlrID_Type.__name__ = "Integer32"
_VismResPartCtrlrID_Object = MibTableColumn
vismResPartCtrlrID = _VismResPartCtrlrID_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 2, 1, 1, 9),
    _VismResPartCtrlrID_Type()
)
vismResPartCtrlrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismResPartCtrlrID.setStatus("current")
_CiscoVismRsrcPartMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismRsrcPartMIBConformance = _CiscoVismRsrcPartMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 93, 2)
)
_CiscoVismRsrcPartMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismRsrcPartMIBGroups = _CiscoVismRsrcPartMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 93, 2, 1)
)
_CiscoVismRsrcPartMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismRsrcPartMIBCompliances = _CiscoVismRsrcPartMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 93, 2, 2)
)

# Managed Objects groups

ciscoVismRsrcPartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 93, 2, 1, 1)
)
ciscoVismRsrcPartGroup.setObjects(
      *(("CISCO-VISM-RSRC-PART-MIB", "vismResPartPortNum"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartCtrlrNum"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartRowStatus"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartNumOfLcnAvail"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartLcnLow"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartLcnHigh"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartIngrPctBW"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartEgrPctBW"),
        ("CISCO-VISM-RSRC-PART-MIB", "vismResPartCtrlrID"))
)
if mibBuilder.loadTexts:
    ciscoVismRsrcPartGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismRsrcPartCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 93, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismRsrcPartCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-RSRC-PART-MIB",
    **{"vismPortResPartCnfGrp": vismPortResPartCnfGrp,
       "vismPortResPartCnfGrpTable": vismPortResPartCnfGrpTable,
       "vismPortResPartCnfGrpEntry": vismPortResPartCnfGrpEntry,
       "vismResPartPortNum": vismResPartPortNum,
       "vismResPartCtrlrNum": vismResPartCtrlrNum,
       "vismResPartRowStatus": vismResPartRowStatus,
       "vismResPartNumOfLcnAvail": vismResPartNumOfLcnAvail,
       "vismResPartLcnLow": vismResPartLcnLow,
       "vismResPartLcnHigh": vismResPartLcnHigh,
       "vismResPartIngrPctBW": vismResPartIngrPctBW,
       "vismResPartEgrPctBW": vismResPartEgrPctBW,
       "vismResPartCtrlrID": vismResPartCtrlrID,
       "ciscoVismRsrcPartMIB": ciscoVismRsrcPartMIB,
       "ciscoVismRsrcPartMIBConformance": ciscoVismRsrcPartMIBConformance,
       "ciscoVismRsrcPartMIBGroups": ciscoVismRsrcPartMIBGroups,
       "ciscoVismRsrcPartGroup": ciscoVismRsrcPartGroup,
       "ciscoVismRsrcPartMIBCompliances": ciscoVismRsrcPartMIBCompliances,
       "ciscoVismRsrcPartCompliance": ciscoVismRsrcPartCompliance}
)
