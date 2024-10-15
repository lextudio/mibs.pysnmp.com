# SNMP MIB module (CISCO-WAN-CES-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-CES-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:58 2024
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

(circuitEmulation,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "circuitEmulation")

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

ciscoWanCesPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 40)
)
ciscoWanCesPortMIB.setRevisions(
        ("2002-11-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesmPort_ObjectIdentity = ObjectIdentity
cesmPort = _CesmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1)
)
_CesmPortCnfGrp_ObjectIdentity = ObjectIdentity
cesmPortCnfGrp = _CesmPortCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1)
)
_CesmPortCnfGrpTable_Object = MibTable
cesmPortCnfGrpTable = _CesmPortCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cesmPortCnfGrpTable.setStatus("current")
_CesmPortCnfGrpEntry_Object = MibTableRow
cesmPortCnfGrpEntry = _CesmPortCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1)
)
cesmPortCnfGrpEntry.setIndexNames(
    (0, "CISCO-WAN-CES-PORT-MIB", "cesPortNum"),
)
if mibBuilder.loadTexts:
    cesmPortCnfGrpEntry.setStatus("current")


class _CesPortNum_Type(Integer32):
    """Custom type cesPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CesPortNum_Type.__name__ = "Integer32"
_CesPortNum_Object = MibTableColumn
cesPortNum = _CesPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 1),
    _CesPortNum_Type()
)
cesPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortNum.setStatus("current")


class _CesPortRowStatus_Type(Integer32):
    """Custom type cesPortRowStatus based on Integer32"""
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


_CesPortRowStatus_Type.__name__ = "Integer32"
_CesPortRowStatus_Object = MibTableColumn
cesPortRowStatus = _CesPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 2),
    _CesPortRowStatus_Type()
)
cesPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPortRowStatus.setStatus("current")


class _CesPortLineNum_Type(Integer32):
    """Custom type cesPortLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CesPortLineNum_Type.__name__ = "Integer32"
_CesPortLineNum_Object = MibTableColumn
cesPortLineNum = _CesPortLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 3),
    _CesPortLineNum_Type()
)
cesPortLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPortLineNum.setStatus("current")


class _CesPortType_Type(Integer32):
    """Custom type cesPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("framingOnVcDisconnect", 3),
          ("strau", 4),
          ("structured", 1),
          ("unstructured", 2))
    )


_CesPortType_Type.__name__ = "Integer32"
_CesPortType_Object = MibTableColumn
cesPortType = _CesPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 4),
    _CesPortType_Type()
)
cesPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPortType.setStatus("current")


class _CesPortDs0ConfigBitMap_Type(Integer32):
    """Custom type cesPortDs0ConfigBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortDs0ConfigBitMap_Type.__name__ = "Integer32"
_CesPortDs0ConfigBitMap_Object = MibTableColumn
cesPortDs0ConfigBitMap = _CesPortDs0ConfigBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 5),
    _CesPortDs0ConfigBitMap_Type()
)
cesPortDs0ConfigBitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPortDs0ConfigBitMap.setStatus("current")


class _CesPortNumOfDs0Slot_Type(Integer32):
    """Custom type cesPortNumOfDs0Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CesPortNumOfDs0Slot_Type.__name__ = "Integer32"
_CesPortNumOfDs0Slot_Object = MibTableColumn
cesPortNumOfDs0Slot = _CesPortNumOfDs0Slot_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 6),
    _CesPortNumOfDs0Slot_Type()
)
cesPortNumOfDs0Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPortNumOfDs0Slot.setStatus("current")


class _CesPortNumOfSCIPerDS0_Type(Integer32):
    """Custom type cesPortNumOfSCIPerDS0 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CesPortNumOfSCIPerDS0_Type.__name__ = "Integer32"
_CesPortNumOfSCIPerDS0_Object = MibTableColumn
cesPortNumOfSCIPerDS0 = _CesPortNumOfSCIPerDS0_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 7),
    _CesPortNumOfSCIPerDS0_Type()
)
cesPortNumOfSCIPerDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPortNumOfSCIPerDS0.setStatus("current")


class _CesPortSpeed_Type(Integer32):
    """Custom type cesPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44736),
    )


_CesPortSpeed_Type.__name__ = "Integer32"
_CesPortSpeed_Object = MibTableColumn
cesPortSpeed = _CesPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 8),
    _CesPortSpeed_Type()
)
cesPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cesPortSpeed.setUnits("kbps")


class _CesPortState_Type(Integer32):
    """Custom type cesPortState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("failedDueToLine", 4),
          ("failedDueToSignalling", 5),
          ("farEndRemoteLoopback", 8),
          ("inBert", 7),
          ("inactive", 6),
          ("notConfigured", 1),
          ("remoteLoopback", 3))
    )


_CesPortState_Type.__name__ = "Integer32"
_CesPortState_Object = MibTableColumn
cesPortState = _CesPortState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 9),
    _CesPortState_Type()
)
cesPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortState.setStatus("current")


class _CesPortBERTEnable_Type(Integer32):
    """Custom type cesPortBERTEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CesPortBERTEnable_Type.__name__ = "Integer32"
_CesPortBERTEnable_Object = MibTableColumn
cesPortBERTEnable = _CesPortBERTEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 1, 1, 10),
    _CesPortBERTEnable_Type()
)
cesPortBERTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesPortBERTEnable.setStatus("current")


class _CesPortNextAvailable_Type(Integer32):
    """Custom type cesPortNextAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CesPortNextAvailable_Type.__name__ = "Integer32"
_CesPortNextAvailable_Object = MibScalar
cesPortNextAvailable = _CesPortNextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 2),
    _CesPortNextAvailable_Type()
)
cesPortNextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortNextAvailable.setStatus("current")


class _CesPortsUsedLine1_Type(Integer32):
    """Custom type cesPortsUsedLine1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine1_Type.__name__ = "Integer32"
_CesPortsUsedLine1_Object = MibScalar
cesPortsUsedLine1 = _CesPortsUsedLine1_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 3),
    _CesPortsUsedLine1_Type()
)
cesPortsUsedLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine1.setStatus("current")


class _CesPortsUsedLine2_Type(Integer32):
    """Custom type cesPortsUsedLine2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine2_Type.__name__ = "Integer32"
_CesPortsUsedLine2_Object = MibScalar
cesPortsUsedLine2 = _CesPortsUsedLine2_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 4),
    _CesPortsUsedLine2_Type()
)
cesPortsUsedLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine2.setStatus("current")


class _CesPortsUsedLine3_Type(Integer32):
    """Custom type cesPortsUsedLine3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine3_Type.__name__ = "Integer32"
_CesPortsUsedLine3_Object = MibScalar
cesPortsUsedLine3 = _CesPortsUsedLine3_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 5),
    _CesPortsUsedLine3_Type()
)
cesPortsUsedLine3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine3.setStatus("current")


class _CesPortsUsedLine4_Type(Integer32):
    """Custom type cesPortsUsedLine4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine4_Type.__name__ = "Integer32"
_CesPortsUsedLine4_Object = MibScalar
cesPortsUsedLine4 = _CesPortsUsedLine4_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 6),
    _CesPortsUsedLine4_Type()
)
cesPortsUsedLine4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine4.setStatus("current")


class _CesPortsUsedLine5_Type(Integer32):
    """Custom type cesPortsUsedLine5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine5_Type.__name__ = "Integer32"
_CesPortsUsedLine5_Object = MibScalar
cesPortsUsedLine5 = _CesPortsUsedLine5_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 7),
    _CesPortsUsedLine5_Type()
)
cesPortsUsedLine5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine5.setStatus("current")


class _CesPortsUsedLine6_Type(Integer32):
    """Custom type cesPortsUsedLine6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine6_Type.__name__ = "Integer32"
_CesPortsUsedLine6_Object = MibScalar
cesPortsUsedLine6 = _CesPortsUsedLine6_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 8),
    _CesPortsUsedLine6_Type()
)
cesPortsUsedLine6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine6.setStatus("current")


class _CesPortsUsedLine7_Type(Integer32):
    """Custom type cesPortsUsedLine7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine7_Type.__name__ = "Integer32"
_CesPortsUsedLine7_Object = MibScalar
cesPortsUsedLine7 = _CesPortsUsedLine7_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 9),
    _CesPortsUsedLine7_Type()
)
cesPortsUsedLine7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine7.setStatus("current")


class _CesPortsUsedLine8_Type(Integer32):
    """Custom type cesPortsUsedLine8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CesPortsUsedLine8_Type.__name__ = "Integer32"
_CesPortsUsedLine8_Object = MibScalar
cesPortsUsedLine8 = _CesPortsUsedLine8_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 1, 1, 10),
    _CesPortsUsedLine8_Type()
)
cesPortsUsedLine8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesPortsUsedLine8.setStatus("current")
_CiscoWanCesPortMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanCesPortMIBConformance = _CiscoWanCesPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 40, 2)
)
_CiscoWanCesPortMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanCesPortMIBGroups = _CiscoWanCesPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 40, 2, 1)
)
_CiscoWanCesPortMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanCesPortMIBCompliances = _CiscoWanCesPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 40, 2, 2)
)

# Managed Objects groups

ciscoWanCesPortsUsedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 40, 2, 1, 1)
)
ciscoWanCesPortsUsedGroup.setObjects(
    ("CISCO-WAN-CES-PORT-MIB", "cesPortNextAvailable")
)
if mibBuilder.loadTexts:
    ciscoWanCesPortsUsedGroup.setStatus("current")

ciscoWanCesPortConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 40, 2, 1, 2)
)
ciscoWanCesPortConfGroup.setObjects(
      *(("CISCO-WAN-CES-PORT-MIB", "cesPortNum"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortRowStatus"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortLineNum"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortType"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortDs0ConfigBitMap"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortNumOfDs0Slot"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortNumOfSCIPerDS0"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortSpeed"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortState"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortBERTEnable"))
)
if mibBuilder.loadTexts:
    ciscoWanCesPortConfGroup.setStatus("current")

ciscoWanCesPortDs0InDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 40, 2, 1, 3)
)
ciscoWanCesPortDs0InDs1Group.setObjects(
      *(("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine1"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine2"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine3"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine4"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine5"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine6"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine7"),
        ("CISCO-WAN-CES-PORT-MIB", "cesPortsUsedLine8"))
)
if mibBuilder.loadTexts:
    ciscoWanCesPortDs0InDs1Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanCesPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoWanCesPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-CES-PORT-MIB",
    **{"cesmPort": cesmPort,
       "cesmPortCnfGrp": cesmPortCnfGrp,
       "cesmPortCnfGrpTable": cesmPortCnfGrpTable,
       "cesmPortCnfGrpEntry": cesmPortCnfGrpEntry,
       "cesPortNum": cesPortNum,
       "cesPortRowStatus": cesPortRowStatus,
       "cesPortLineNum": cesPortLineNum,
       "cesPortType": cesPortType,
       "cesPortDs0ConfigBitMap": cesPortDs0ConfigBitMap,
       "cesPortNumOfDs0Slot": cesPortNumOfDs0Slot,
       "cesPortNumOfSCIPerDS0": cesPortNumOfSCIPerDS0,
       "cesPortSpeed": cesPortSpeed,
       "cesPortState": cesPortState,
       "cesPortBERTEnable": cesPortBERTEnable,
       "cesPortNextAvailable": cesPortNextAvailable,
       "cesPortsUsedLine1": cesPortsUsedLine1,
       "cesPortsUsedLine2": cesPortsUsedLine2,
       "cesPortsUsedLine3": cesPortsUsedLine3,
       "cesPortsUsedLine4": cesPortsUsedLine4,
       "cesPortsUsedLine5": cesPortsUsedLine5,
       "cesPortsUsedLine6": cesPortsUsedLine6,
       "cesPortsUsedLine7": cesPortsUsedLine7,
       "cesPortsUsedLine8": cesPortsUsedLine8,
       "ciscoWanCesPortMIB": ciscoWanCesPortMIB,
       "ciscoWanCesPortMIBConformance": ciscoWanCesPortMIBConformance,
       "ciscoWanCesPortMIBGroups": ciscoWanCesPortMIBGroups,
       "ciscoWanCesPortsUsedGroup": ciscoWanCesPortsUsedGroup,
       "ciscoWanCesPortConfGroup": ciscoWanCesPortConfGroup,
       "ciscoWanCesPortDs0InDs1Group": ciscoWanCesPortDs0InDs1Group,
       "ciscoWanCesPortMIBCompliances": ciscoWanCesPortMIBCompliances,
       "ciscoWanCesPortCompliance": ciscoWanCesPortCompliance}
)
