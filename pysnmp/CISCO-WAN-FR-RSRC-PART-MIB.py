# SNMP MIB module (CISCO-WAN-FR-RSRC-PART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-FR-RSRC-PART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:05 2024
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

(frPortCnfResPartGrp,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "frPortCnfResPartGrp")

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

ciscoWanFrRsrcPartMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 45)
)
ciscoWanFrRsrcPartMIB.setRevisions(
        ("2002-09-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrPortCnfResPartGrpTable_Object = MibTable
frPortCnfResPartGrpTable = _FrPortCnfResPartGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    frPortCnfResPartGrpTable.setStatus("current")
_FrPortCnfResPartGrpEntry_Object = MibTableRow
frPortCnfResPartGrpEntry = _FrPortCnfResPartGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1)
)
frPortCnfResPartGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-RSRC-PART-MIB", "frResPartPortNum"),
    (0, "CISCO-WAN-FR-RSRC-PART-MIB", "frResPartCtrlrNum"),
)
if mibBuilder.loadTexts:
    frPortCnfResPartGrpEntry.setStatus("current")


class _FrResPartPortNum_Type(Integer32):
    """Custom type frResPartPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrResPartPortNum_Type.__name__ = "Integer32"
_FrResPartPortNum_Object = MibTableColumn
frResPartPortNum = _FrResPartPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 1),
    _FrResPartPortNum_Type()
)
frResPartPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frResPartPortNum.setStatus("current")


class _FrResPartCtrlrNum_Type(Integer32):
    """Custom type frResPartCtrlrNum based on Integer32"""
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


_FrResPartCtrlrNum_Type.__name__ = "Integer32"
_FrResPartCtrlrNum_Object = MibTableColumn
frResPartCtrlrNum = _FrResPartCtrlrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 2),
    _FrResPartCtrlrNum_Type()
)
frResPartCtrlrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frResPartCtrlrNum.setStatus("current")


class _FrResPartRowStatus_Type(Integer32):
    """Custom type frResPartRowStatus based on Integer32"""
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


_FrResPartRowStatus_Type.__name__ = "Integer32"
_FrResPartRowStatus_Object = MibTableColumn
frResPartRowStatus = _FrResPartRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 3),
    _FrResPartRowStatus_Type()
)
frResPartRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frResPartRowStatus.setStatus("current")


class _FrResPartNumOfLcnAvail_Type(Integer32):
    """Custom type frResPartNumOfLcnAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_FrResPartNumOfLcnAvail_Type.__name__ = "Integer32"
_FrResPartNumOfLcnAvail_Object = MibTableColumn
frResPartNumOfLcnAvail = _FrResPartNumOfLcnAvail_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 4),
    _FrResPartNumOfLcnAvail_Type()
)
frResPartNumOfLcnAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frResPartNumOfLcnAvail.setStatus("current")


class _FrResPartDlciLow_Type(Integer32):
    """Custom type frResPartDlciLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_FrResPartDlciLow_Type.__name__ = "Integer32"
_FrResPartDlciLow_Object = MibTableColumn
frResPartDlciLow = _FrResPartDlciLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 5),
    _FrResPartDlciLow_Type()
)
frResPartDlciLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frResPartDlciLow.setStatus("current")


class _FrResPartDlciHigh_Type(Integer32):
    """Custom type frResPartDlciHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_FrResPartDlciHigh_Type.__name__ = "Integer32"
_FrResPartDlciHigh_Object = MibTableColumn
frResPartDlciHigh = _FrResPartDlciHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 6),
    _FrResPartDlciHigh_Type()
)
frResPartDlciHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frResPartDlciHigh.setStatus("current")


class _FrResPartIngrPctBW_Type(Integer32):
    """Custom type frResPartIngrPctBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrResPartIngrPctBW_Type.__name__ = "Integer32"
_FrResPartIngrPctBW_Object = MibTableColumn
frResPartIngrPctBW = _FrResPartIngrPctBW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 7),
    _FrResPartIngrPctBW_Type()
)
frResPartIngrPctBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frResPartIngrPctBW.setStatus("current")
if mibBuilder.loadTexts:
    frResPartIngrPctBW.setUnits("percentage")


class _FrResPartEgrPctBW_Type(Integer32):
    """Custom type frResPartEgrPctBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrResPartEgrPctBW_Type.__name__ = "Integer32"
_FrResPartEgrPctBW_Object = MibTableColumn
frResPartEgrPctBW = _FrResPartEgrPctBW_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 8),
    _FrResPartEgrPctBW_Type()
)
frResPartEgrPctBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frResPartEgrPctBW.setStatus("current")
if mibBuilder.loadTexts:
    frResPartEgrPctBW.setUnits("percentage")


class _FrResPartCtrlrID_Type(Integer32):
    """Custom type frResPartCtrlrID based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrResPartCtrlrID_Type.__name__ = "Integer32"
_FrResPartCtrlrID_Object = MibTableColumn
frResPartCtrlrID = _FrResPartCtrlrID_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5, 1, 1, 9),
    _FrResPartCtrlrID_Type()
)
frResPartCtrlrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frResPartCtrlrID.setStatus("current")
_CwfRsrcPartMIBConformance_ObjectIdentity = ObjectIdentity
cwfRsrcPartMIBConformance = _CwfRsrcPartMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 45, 2)
)
_CwfRsrcPartMIBCompliances_ObjectIdentity = ObjectIdentity
cwfRsrcPartMIBCompliances = _CwfRsrcPartMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 45, 2, 1)
)
_CwfRsrcPartMIBGroups_ObjectIdentity = ObjectIdentity
cwfRsrcPartMIBGroups = _CwfRsrcPartMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 45, 2, 2)
)

# Managed Objects groups

ciscoWanFrRsrcPartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 45, 2, 2, 1)
)
ciscoWanFrRsrcPartGroup.setObjects(
      *(("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartPortNum"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartCtrlrNum"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartRowStatus"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartNumOfLcnAvail"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartDlciLow"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartDlciHigh"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartIngrPctBW"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartEgrPctBW"),
        ("CISCO-WAN-FR-RSRC-PART-MIB", "frResPartCtrlrID"))
)
if mibBuilder.loadTexts:
    ciscoWanFrRsrcPartGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanFrRsrcPartCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 45, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanFrRsrcPartCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-FR-RSRC-PART-MIB",
    **{"frPortCnfResPartGrpTable": frPortCnfResPartGrpTable,
       "frPortCnfResPartGrpEntry": frPortCnfResPartGrpEntry,
       "frResPartPortNum": frResPartPortNum,
       "frResPartCtrlrNum": frResPartCtrlrNum,
       "frResPartRowStatus": frResPartRowStatus,
       "frResPartNumOfLcnAvail": frResPartNumOfLcnAvail,
       "frResPartDlciLow": frResPartDlciLow,
       "frResPartDlciHigh": frResPartDlciHigh,
       "frResPartIngrPctBW": frResPartIngrPctBW,
       "frResPartEgrPctBW": frResPartEgrPctBW,
       "frResPartCtrlrID": frResPartCtrlrID,
       "ciscoWanFrRsrcPartMIB": ciscoWanFrRsrcPartMIB,
       "cwfRsrcPartMIBConformance": cwfRsrcPartMIBConformance,
       "cwfRsrcPartMIBCompliances": cwfRsrcPartMIBCompliances,
       "ciscoWanFrRsrcPartCompliance": ciscoWanFrRsrcPartCompliance,
       "cwfRsrcPartMIBGroups": cwfRsrcPartMIBGroups,
       "ciscoWanFrRsrcPartGroup": ciscoWanFrRsrcPartGroup}
)
