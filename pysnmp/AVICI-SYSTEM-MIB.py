# SNMP MIB module (AVICI-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:40 2024
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

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(AviciBayType,
 AviciInventoryType,
 AviciPlatformIndexType,
 AviciSlotType,
 AviciSystemType,
 AviciTrapDescrType) = mibBuilder.importSymbols(
    "AVICI-TC",
    "AviciBayType",
    "AviciInventoryType",
    "AviciPlatformIndexType",
    "AviciSlotType",
    "AviciSystemType",
    "AviciTrapDescrType")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

aviciSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciSystemObjects_ObjectIdentity = ObjectIdentity
aviciSystemObjects = _AviciSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1)
)
_AviciSysInventoryTable_Object = MibTable
aviciSysInventoryTable = _AviciSysInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aviciSysInventoryTable.setStatus("current")
_AviciSysInventoryEntry_Object = MibTableRow
aviciSysInventoryEntry = _AviciSysInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1, 1)
)
aviciSysInventoryEntry.setIndexNames(
    (0, "AVICI-SYSTEM-MIB", "aviciSysInventoryId"),
)
if mibBuilder.loadTexts:
    aviciSysInventoryEntry.setStatus("current")
_AviciSysInventoryId_Type = AviciPlatformIndexType
_AviciSysInventoryId_Object = MibTableColumn
aviciSysInventoryId = _AviciSysInventoryId_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1, 1, 1),
    _AviciSysInventoryId_Type()
)
aviciSysInventoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysInventoryId.setStatus("current")
_AviciSysInventoryType_Type = AviciInventoryType
_AviciSysInventoryType_Object = MibTableColumn
aviciSysInventoryType = _AviciSysInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1, 1, 2),
    _AviciSysInventoryType_Type()
)
aviciSysInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysInventoryType.setStatus("current")


class _AviciSysInventoryOperStatus_Type(Integer32):
    """Custom type aviciSysInventoryOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AviciSysInventoryOperStatus_Type.__name__ = "Integer32"
_AviciSysInventoryOperStatus_Object = MibTableColumn
aviciSysInventoryOperStatus = _AviciSysInventoryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1, 1, 3),
    _AviciSysInventoryOperStatus_Type()
)
aviciSysInventoryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysInventoryOperStatus.setStatus("current")
_AviciSysInventoryBay_Type = AviciBayType
_AviciSysInventoryBay_Object = MibTableColumn
aviciSysInventoryBay = _AviciSysInventoryBay_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1, 1, 4),
    _AviciSysInventoryBay_Type()
)
aviciSysInventoryBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysInventoryBay.setStatus("current")
_AviciSysInventorySlot_Type = AviciSlotType
_AviciSysInventorySlot_Object = MibTableColumn
aviciSysInventorySlot = _AviciSysInventorySlot_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1, 1, 5),
    _AviciSysInventorySlot_Type()
)
aviciSysInventorySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysInventorySlot.setStatus("current")


class _AviciSysInventoryDescr_Type(DisplayString):
    """Custom type aviciSysInventoryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciSysInventoryDescr_Type.__name__ = "DisplayString"
_AviciSysInventoryDescr_Object = MibTableColumn
aviciSysInventoryDescr = _AviciSysInventoryDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 1, 1, 6),
    _AviciSysInventoryDescr_Type()
)
aviciSysInventoryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysInventoryDescr.setStatus("current")
_AviciSysIfTransTable_Object = MibTable
aviciSysIfTransTable = _AviciSysIfTransTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    aviciSysIfTransTable.setStatus("current")
_AviciSysIfTransEntry_Object = MibTableRow
aviciSysIfTransEntry = _AviciSysIfTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2, 1)
)
aviciSysIfTransEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aviciSysIfTransEntry.setStatus("current")
_AviciSysIfTransBay_Type = AviciBayType
_AviciSysIfTransBay_Object = MibTableColumn
aviciSysIfTransBay = _AviciSysIfTransBay_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2, 1, 1),
    _AviciSysIfTransBay_Type()
)
aviciSysIfTransBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysIfTransBay.setStatus("current")
_AviciSysIfTransSlot_Type = AviciSlotType
_AviciSysIfTransSlot_Object = MibTableColumn
aviciSysIfTransSlot = _AviciSysIfTransSlot_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2, 1, 2),
    _AviciSysIfTransSlot_Type()
)
aviciSysIfTransSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysIfTransSlot.setStatus("current")
_AviciSysIfTransPort_Type = Integer32
_AviciSysIfTransPort_Object = MibTableColumn
aviciSysIfTransPort = _AviciSysIfTransPort_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2, 1, 3),
    _AviciSysIfTransPort_Type()
)
aviciSysIfTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysIfTransPort.setStatus("current")
_AviciSysIfTransIfc_Type = Integer32
_AviciSysIfTransIfc_Object = MibTableColumn
aviciSysIfTransIfc = _AviciSysIfTransIfc_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2, 1, 4),
    _AviciSysIfTransIfc_Type()
)
aviciSysIfTransIfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysIfTransIfc.setStatus("current")
_AviciSysIfTransType_Type = IANAifType
_AviciSysIfTransType_Object = MibTableColumn
aviciSysIfTransType = _AviciSysIfTransType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2, 1, 5),
    _AviciSysIfTransType_Type()
)
aviciSysIfTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysIfTransType.setStatus("current")


class _AviciSysIfTransName_Type(DisplayString):
    """Custom type aviciSysIfTransName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciSysIfTransName_Type.__name__ = "DisplayString"
_AviciSysIfTransName_Object = MibTableColumn
aviciSysIfTransName = _AviciSysIfTransName_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 1, 2, 1, 6),
    _AviciSysIfTransName_Type()
)
aviciSysIfTransName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysIfTransName.setStatus("current")
_AviciSystemGroup_ObjectIdentity = ObjectIdentity
aviciSystemGroup = _AviciSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 2)
)
_AviciSysRouterId_Type = IpAddress
_AviciSysRouterId_Object = MibScalar
aviciSysRouterId = _AviciSysRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 2, 1),
    _AviciSysRouterId_Type()
)
aviciSysRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysRouterId.setStatus("current")
_AviciSysType_Type = AviciSystemType
_AviciSysType_Object = MibScalar
aviciSysType = _AviciSysType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 2, 2),
    _AviciSysType_Type()
)
aviciSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysType.setStatus("current")
_AviciSysInventoryTableChange_Type = TimeTicks
_AviciSysInventoryTableChange_Object = MibScalar
aviciSysInventoryTableChange = _AviciSysInventoryTableChange_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 2, 3),
    _AviciSysInventoryTableChange_Type()
)
aviciSysInventoryTableChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSysInventoryTableChange.setStatus("current")
_AviciSysTrapDescr_Type = AviciTrapDescrType
_AviciSysTrapDescr_Object = MibScalar
aviciSysTrapDescr = _AviciSysTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 2, 4),
    _AviciSysTrapDescr_Type()
)
aviciSysTrapDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviciSysTrapDescr.setStatus("current")
_AviciSystemMIBConformance_ObjectIdentity = ObjectIdentity
aviciSystemMIBConformance = _AviciSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 3)
)
_AviciSystemMIBCompliances_ObjectIdentity = ObjectIdentity
aviciSystemMIBCompliances = _AviciSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 3, 1)
)
_AviciSystemMIBGroups_ObjectIdentity = ObjectIdentity
aviciSystemMIBGroups = _AviciSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 3, 2)
)

# Managed Objects groups

aviciSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 3, 2, 1)
)
aviciSysGroup.setObjects(
      *(("AVICI-SYSTEM-MIB", "aviciSysRouterId"),
        ("AVICI-SYSTEM-MIB", "aviciSysType"),
        ("AVICI-SYSTEM-MIB", "aviciSysInventoryTableChange"),
        ("AVICI-SYSTEM-MIB", "aviciSysInventoryId"),
        ("AVICI-SYSTEM-MIB", "aviciSysInventoryType"),
        ("AVICI-SYSTEM-MIB", "aviciSysInventoryOperStatus"),
        ("AVICI-SYSTEM-MIB", "aviciSysInventoryBay"),
        ("AVICI-SYSTEM-MIB", "aviciSysInventorySlot"),
        ("AVICI-SYSTEM-MIB", "aviciSysInventoryDescr"),
        ("AVICI-SYSTEM-MIB", "aviciSysIfTransBay"),
        ("AVICI-SYSTEM-MIB", "aviciSysIfTransSlot"),
        ("AVICI-SYSTEM-MIB", "aviciSysIfTransPort"),
        ("AVICI-SYSTEM-MIB", "aviciSysIfTransIfc"),
        ("AVICI-SYSTEM-MIB", "aviciSysIfTransType"),
        ("AVICI-SYSTEM-MIB", "aviciSysIfTransName"))
)
if mibBuilder.loadTexts:
    aviciSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviciSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aviciSystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-SYSTEM-MIB",
    **{"aviciSystemMIB": aviciSystemMIB,
       "aviciSystemObjects": aviciSystemObjects,
       "aviciSysInventoryTable": aviciSysInventoryTable,
       "aviciSysInventoryEntry": aviciSysInventoryEntry,
       "aviciSysInventoryId": aviciSysInventoryId,
       "aviciSysInventoryType": aviciSysInventoryType,
       "aviciSysInventoryOperStatus": aviciSysInventoryOperStatus,
       "aviciSysInventoryBay": aviciSysInventoryBay,
       "aviciSysInventorySlot": aviciSysInventorySlot,
       "aviciSysInventoryDescr": aviciSysInventoryDescr,
       "aviciSysIfTransTable": aviciSysIfTransTable,
       "aviciSysIfTransEntry": aviciSysIfTransEntry,
       "aviciSysIfTransBay": aviciSysIfTransBay,
       "aviciSysIfTransSlot": aviciSysIfTransSlot,
       "aviciSysIfTransPort": aviciSysIfTransPort,
       "aviciSysIfTransIfc": aviciSysIfTransIfc,
       "aviciSysIfTransType": aviciSysIfTransType,
       "aviciSysIfTransName": aviciSysIfTransName,
       "aviciSystemGroup": aviciSystemGroup,
       "aviciSysRouterId": aviciSysRouterId,
       "aviciSysType": aviciSysType,
       "aviciSysInventoryTableChange": aviciSysInventoryTableChange,
       "aviciSysTrapDescr": aviciSysTrapDescr,
       "aviciSystemMIBConformance": aviciSystemMIBConformance,
       "aviciSystemMIBCompliances": aviciSystemMIBCompliances,
       "aviciSystemMIBCompliance": aviciSystemMIBCompliance,
       "aviciSystemMIBGroups": aviciSystemMIBGroups,
       "aviciSysGroup": aviciSysGroup}
)
