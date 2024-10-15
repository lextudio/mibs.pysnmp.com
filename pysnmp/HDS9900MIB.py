# SNMP MIB module (HDS9900MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDS9900MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:05 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hitachi_ObjectIdentity = ObjectIdentity
hitachi = _Hitachi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11)
)
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4)
)
_RaidDummy_ObjectIdentity = ObjectIdentity
raidDummy = _RaidDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1)
)
_RaidRoot_ObjectIdentity = ObjectIdentity
raidRoot = _RaidRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1)
)
_EventTrapSerialNumber_Type = Integer32
_EventTrapSerialNumber_Object = MibScalar
eventTrapSerialNumber = _EventTrapSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 1),
    _EventTrapSerialNumber_Type()
)
eventTrapSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTrapSerialNumber.setStatus("mandatory")
_EventTrapNickname_Type = DisplayString
_EventTrapNickname_Object = MibScalar
eventTrapNickname = _EventTrapNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 2),
    _EventTrapNickname_Type()
)
eventTrapNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTrapNickname.setStatus("mandatory")
_EventTrapREFCODE_Type = DisplayString
_EventTrapREFCODE_Object = MibScalar
eventTrapREFCODE = _EventTrapREFCODE_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 3),
    _EventTrapREFCODE_Type()
)
eventTrapREFCODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTrapREFCODE.setStatus("mandatory")
_EventTrapPartsID_Type = Integer32
_EventTrapPartsID_Object = MibScalar
eventTrapPartsID = _EventTrapPartsID_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 4),
    _EventTrapPartsID_Type()
)
eventTrapPartsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTrapPartsID.setStatus("mandatory")
_RaidEventCommandTable_Object = MibTable
raidEventCommandTable = _RaidEventCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    raidEventCommandTable.setStatus("mandatory")
_RaidEventCommandEntry_Object = MibTableRow
raidEventCommandEntry = _RaidEventCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 9, 1)
)
raidEventCommandEntry.setIndexNames(
    (0, "HDS9900MIB", "trapCommandSerialNumber"),
)
if mibBuilder.loadTexts:
    raidEventCommandEntry.setStatus("mandatory")
_TrapCommandSerialNumber_Type = Integer32
_TrapCommandSerialNumber_Object = MibTableColumn
trapCommandSerialNumber = _TrapCommandSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 9, 1, 1),
    _TrapCommandSerialNumber_Type()
)
trapCommandSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCommandSerialNumber.setStatus("mandatory")


class _TrapCommandManagerName_Type(DisplayString):
    """Custom type trapCommandManagerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TrapCommandManagerName_Type.__name__ = "DisplayString"
_TrapCommandManagerName_Object = MibTableColumn
trapCommandManagerName = _TrapCommandManagerName_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 9, 1, 2),
    _TrapCommandManagerName_Type()
)
trapCommandManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCommandManagerName.setStatus("mandatory")
_TrapCommandKind_Type = Integer32
_TrapCommandKind_Object = MibTableColumn
trapCommandKind = _TrapCommandKind_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 9, 1, 3),
    _TrapCommandKind_Type()
)
trapCommandKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCommandKind.setStatus("mandatory")
_TrapCommandStatus_Type = Integer32
_TrapCommandStatus_Object = MibTableColumn
trapCommandStatus = _TrapCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 9, 1, 4),
    _TrapCommandStatus_Type()
)
trapCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCommandStatus.setStatus("mandatory")
_SystemExMib_ObjectIdentity = ObjectIdentity
systemExMib = _SystemExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5)
)
_StorageExMib_ObjectIdentity = ObjectIdentity
storageExMib = _StorageExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11)
)
_RaidExMib_ObjectIdentity = ObjectIdentity
raidExMib = _RaidExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4)
)
_RaidExMibDummy_ObjectIdentity = ObjectIdentity
raidExMibDummy = _RaidExMibDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1)
)
_RaidExMibRoot_ObjectIdentity = ObjectIdentity
raidExMibRoot = _RaidExMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1)
)
_RaidExMibName_Type = DisplayString
_RaidExMibName_Object = MibScalar
raidExMibName = _RaidExMibName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 1),
    _RaidExMibName_Type()
)
raidExMibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibName.setStatus("mandatory")
_RaidExMibVersion_Type = DisplayString
_RaidExMibVersion_Object = MibScalar
raidExMibVersion = _RaidExMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 2),
    _RaidExMibVersion_Type()
)
raidExMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibVersion.setStatus("mandatory")
_RaidExMibAgentVersion_Type = DisplayString
_RaidExMibAgentVersion_Object = MibScalar
raidExMibAgentVersion = _RaidExMibAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 3),
    _RaidExMibAgentVersion_Type()
)
raidExMibAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibAgentVersion.setStatus("mandatory")
_RaidExMibDkcCount_Type = Integer32
_RaidExMibDkcCount_Object = MibScalar
raidExMibDkcCount = _RaidExMibDkcCount_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 4),
    _RaidExMibDkcCount_Type()
)
raidExMibDkcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibDkcCount.setStatus("mandatory")
_RaidExMibRaidListTable_Object = MibTable
raidExMibRaidListTable = _RaidExMibRaidListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    raidExMibRaidListTable.setStatus("mandatory")
_RaidExMibRaidListEntry_Object = MibTableRow
raidExMibRaidListEntry = _RaidExMibRaidListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1)
)
raidExMibRaidListEntry.setIndexNames(
    (0, "HDS9900MIB", "raidlistSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibRaidListEntry.setStatus("mandatory")
_RaidlistSerialNumber_Type = Integer32
_RaidlistSerialNumber_Object = MibTableColumn
raidlistSerialNumber = _RaidlistSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 1),
    _RaidlistSerialNumber_Type()
)
raidlistSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistSerialNumber.setStatus("mandatory")


class _RaidlistMibNickName_Type(DisplayString):
    """Custom type raidlistMibNickName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_RaidlistMibNickName_Type.__name__ = "DisplayString"
_RaidlistMibNickName_Object = MibTableColumn
raidlistMibNickName = _RaidlistMibNickName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 2),
    _RaidlistMibNickName_Type()
)
raidlistMibNickName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistMibNickName.setStatus("mandatory")
_RaidlistDKCMainVersion_Type = DisplayString
_RaidlistDKCMainVersion_Object = MibTableColumn
raidlistDKCMainVersion = _RaidlistDKCMainVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 3),
    _RaidlistDKCMainVersion_Type()
)
raidlistDKCMainVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistDKCMainVersion.setStatus("mandatory")
_RaidlistDKCProductName_Type = DisplayString
_RaidlistDKCProductName_Object = MibTableColumn
raidlistDKCProductName = _RaidlistDKCProductName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 4),
    _RaidlistDKCProductName_Type()
)
raidlistDKCProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistDKCProductName.setStatus("mandatory")
_RaidExMibDKCHWTable_Object = MibTable
raidExMibDKCHWTable = _RaidExMibDKCHWTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    raidExMibDKCHWTable.setStatus("mandatory")
_RaidExMibDKCHWEntry_Object = MibTableRow
raidExMibDKCHWEntry = _RaidExMibDKCHWEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1)
)
raidExMibDKCHWEntry.setIndexNames(
    (0, "HDS9900MIB", "dkcRaidListIndexSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibDKCHWEntry.setStatus("mandatory")
_DkcRaidListIndexSerialNumber_Type = Integer32
_DkcRaidListIndexSerialNumber_Object = MibTableColumn
dkcRaidListIndexSerialNumber = _DkcRaidListIndexSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 1),
    _DkcRaidListIndexSerialNumber_Type()
)
dkcRaidListIndexSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcRaidListIndexSerialNumber.setStatus("mandatory")


class _DkcHWProcessor_Type(Integer32):
    """Custom type dkcHWProcessor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWProcessor_Type.__name__ = "Integer32"
_DkcHWProcessor_Object = MibTableColumn
dkcHWProcessor = _DkcHWProcessor_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 2),
    _DkcHWProcessor_Type()
)
dkcHWProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWProcessor.setStatus("mandatory")


class _DkcHWCSW_Type(Integer32):
    """Custom type dkcHWCSW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWCSW_Type.__name__ = "Integer32"
_DkcHWCSW_Object = MibTableColumn
dkcHWCSW = _DkcHWCSW_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 3),
    _DkcHWCSW_Type()
)
dkcHWCSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWCSW.setStatus("mandatory")


class _DkcHWCache_Type(Integer32):
    """Custom type dkcHWCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWCache_Type.__name__ = "Integer32"
_DkcHWCache_Object = MibTableColumn
dkcHWCache = _DkcHWCache_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 4),
    _DkcHWCache_Type()
)
dkcHWCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWCache.setStatus("mandatory")


class _DkcHWSM_Type(Integer32):
    """Custom type dkcHWSM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWSM_Type.__name__ = "Integer32"
_DkcHWSM_Object = MibTableColumn
dkcHWSM = _DkcHWSM_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 5),
    _DkcHWSM_Type()
)
dkcHWSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWSM.setStatus("mandatory")


class _DkcHWPS_Type(Integer32):
    """Custom type dkcHWPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWPS_Type.__name__ = "Integer32"
_DkcHWPS_Object = MibTableColumn
dkcHWPS = _DkcHWPS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 6),
    _DkcHWPS_Type()
)
dkcHWPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWPS.setStatus("mandatory")


class _DkcHWBattery_Type(Integer32):
    """Custom type dkcHWBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWBattery_Type.__name__ = "Integer32"
_DkcHWBattery_Object = MibTableColumn
dkcHWBattery = _DkcHWBattery_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 7),
    _DkcHWBattery_Type()
)
dkcHWBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWBattery.setStatus("mandatory")


class _DkcHWFan_Type(Integer32):
    """Custom type dkcHWFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWFan_Type.__name__ = "Integer32"
_DkcHWFan_Object = MibTableColumn
dkcHWFan = _DkcHWFan_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 8),
    _DkcHWFan_Type()
)
dkcHWFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWFan.setStatus("mandatory")


class _DkcHWEnvironment_Type(Integer32):
    """Custom type dkcHWEnvironment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkcHWEnvironment_Type.__name__ = "Integer32"
_DkcHWEnvironment_Object = MibTableColumn
dkcHWEnvironment = _DkcHWEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 9),
    _DkcHWEnvironment_Type()
)
dkcHWEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWEnvironment.setStatus("mandatory")
_RaidExMibDKUHWTable_Object = MibTable
raidExMibDKUHWTable = _RaidExMibDKUHWTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    raidExMibDKUHWTable.setStatus("mandatory")
_RaidExMibDKUHWEntry_Object = MibTableRow
raidExMibDKUHWEntry = _RaidExMibDKUHWEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1)
)
raidExMibDKUHWEntry.setIndexNames(
    (0, "HDS9900MIB", "dkuRaidListIndexSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibDKUHWEntry.setStatus("mandatory")
_DkuRaidListIndexSerialNumber_Type = Integer32
_DkuRaidListIndexSerialNumber_Object = MibTableColumn
dkuRaidListIndexSerialNumber = _DkuRaidListIndexSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 1),
    _DkuRaidListIndexSerialNumber_Type()
)
dkuRaidListIndexSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuRaidListIndexSerialNumber.setStatus("mandatory")


class _DkuHWPS_Type(Integer32):
    """Custom type dkuHWPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkuHWPS_Type.__name__ = "Integer32"
_DkuHWPS_Object = MibTableColumn
dkuHWPS = _DkuHWPS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 2),
    _DkuHWPS_Type()
)
dkuHWPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWPS.setStatus("mandatory")


class _DkuHWFan_Type(Integer32):
    """Custom type dkuHWFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkuHWFan_Type.__name__ = "Integer32"
_DkuHWFan_Object = MibTableColumn
dkuHWFan = _DkuHWFan_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 3),
    _DkuHWFan_Type()
)
dkuHWFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWFan.setStatus("mandatory")


class _DkuHWEnvironment_Type(Integer32):
    """Custom type dkuHWEnvironment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkuHWEnvironment_Type.__name__ = "Integer32"
_DkuHWEnvironment_Object = MibTableColumn
dkuHWEnvironment = _DkuHWEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 4),
    _DkuHWEnvironment_Type()
)
dkuHWEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWEnvironment.setStatus("mandatory")


class _DkuHWDrive_Type(Integer32):
    """Custom type dkuHWDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acute", 2),
          ("moderate", 4),
          ("noError", 1),
          ("serious", 3),
          ("service", 5))
    )


_DkuHWDrive_Type.__name__ = "Integer32"
_DkuHWDrive_Object = MibTableColumn
dkuHWDrive = _DkuHWDrive_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 5),
    _DkuHWDrive_Type()
)
dkuHWDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWDrive.setStatus("mandatory")
_RaidExMibTrapListTable_Object = MibTable
raidExMibTrapListTable = _RaidExMibTrapListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    raidExMibTrapListTable.setStatus("mandatory")
_RaidExMibTrapListEntry_Object = MibTableRow
raidExMibTrapListEntry = _RaidExMibTrapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1)
)
raidExMibTrapListEntry.setIndexNames(
    (0, "HDS9900MIB", "eventListIndexSerialNumber"),
    (0, "HDS9900MIB", "eventListIndexRecordNo"),
)
if mibBuilder.loadTexts:
    raidExMibTrapListEntry.setStatus("mandatory")
_EventListIndexSerialNumber_Type = Integer32
_EventListIndexSerialNumber_Object = MibTableColumn
eventListIndexSerialNumber = _EventListIndexSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 1),
    _EventListIndexSerialNumber_Type()
)
eventListIndexSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListIndexSerialNumber.setStatus("mandatory")


class _EventListNickname_Type(DisplayString):
    """Custom type eventListNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_EventListNickname_Type.__name__ = "DisplayString"
_EventListNickname_Object = MibTableColumn
eventListNickname = _EventListNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 2),
    _EventListNickname_Type()
)
eventListNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListNickname.setStatus("mandatory")
_EventListIndexRecordNo_Type = Counter32
_EventListIndexRecordNo_Object = MibTableColumn
eventListIndexRecordNo = _EventListIndexRecordNo_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 3),
    _EventListIndexRecordNo_Type()
)
eventListIndexRecordNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListIndexRecordNo.setStatus("mandatory")


class _EventListREFCODE_Type(DisplayString):
    """Custom type eventListREFCODE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EventListREFCODE_Type.__name__ = "DisplayString"
_EventListREFCODE_Object = MibTableColumn
eventListREFCODE = _EventListREFCODE_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 4),
    _EventListREFCODE_Type()
)
eventListREFCODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListREFCODE.setStatus("mandatory")
_RaidExMibCommandTable_Object = MibTable
raidExMibCommandTable = _RaidExMibCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    raidExMibCommandTable.setStatus("mandatory")
_RaidExMibCommandEntry_Object = MibTableRow
raidExMibCommandEntry = _RaidExMibCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1)
)
raidExMibCommandEntry.setIndexNames(
    (0, "HDS9900MIB", "commandSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCommandEntry.setStatus("mandatory")
_CommandSerialNumber_Type = Integer32
_CommandSerialNumber_Object = MibTableColumn
commandSerialNumber = _CommandSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1, 1),
    _CommandSerialNumber_Type()
)
commandSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandSerialNumber.setStatus("mandatory")


class _CommandManagerName_Type(DisplayString):
    """Custom type commandManagerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CommandManagerName_Type.__name__ = "DisplayString"
_CommandManagerName_Object = MibTableColumn
commandManagerName = _CommandManagerName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1, 2),
    _CommandManagerName_Type()
)
commandManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandManagerName.setStatus("mandatory")
_CommandKind_Type = Integer32
_CommandKind_Object = MibTableColumn
commandKind = _CommandKind_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1, 3),
    _CommandKind_Type()
)
commandKind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandKind.setStatus("mandatory")
_CommandStatus_Type = Integer32
_CommandStatus_Object = MibTableColumn
commandStatus = _CommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1, 4),
    _CommandStatus_Type()
)
commandStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandStatus.setStatus("mandatory")
_CommandProgress_Type = Integer32
_CommandProgress_Object = MibTableColumn
commandProgress = _CommandProgress_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1, 5),
    _CommandProgress_Type()
)
commandProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandProgress.setStatus("mandatory")
_CommandRefreshTarget_Type = Integer32
_CommandRefreshTarget_Object = MibTableColumn
commandRefreshTarget = _CommandRefreshTarget_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1, 6),
    _CommandRefreshTarget_Type()
)
commandRefreshTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandRefreshTarget.setStatus("mandatory")
_CommandRefreshTarget2_Type = OctetString
_CommandRefreshTarget2_Object = MibTableColumn
commandRefreshTarget2 = _CommandRefreshTarget2_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 9, 1, 7),
    _CommandRefreshTarget2_Type()
)
commandRefreshTarget2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commandRefreshTarget2.setStatus("mandatory")
_RaidExMibLDev_ObjectIdentity = ObjectIdentity
raidExMibLDev = _RaidExMibLDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10)
)
_RaidExMibLogicalDeviceTable_Object = MibTable
raidExMibLogicalDeviceTable = _RaidExMibLogicalDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    raidExMibLogicalDeviceTable.setStatus("mandatory")
_RaidExMibLogicalDeviceEntry_Object = MibTableRow
raidExMibLogicalDeviceEntry = _RaidExMibLogicalDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1)
)
raidExMibLogicalDeviceEntry.setIndexNames(
    (0, "HDS9900MIB", "logicalDeviceSerialNumber"),
    (0, "HDS9900MIB", "logicalDeviceCU"),
    (0, "HDS9900MIB", "logicalDeviceLDEV"),
)
if mibBuilder.loadTexts:
    raidExMibLogicalDeviceEntry.setStatus("mandatory")
_LogicalDeviceSerialNumber_Type = Integer32
_LogicalDeviceSerialNumber_Object = MibTableColumn
logicalDeviceSerialNumber = _LogicalDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 1),
    _LogicalDeviceSerialNumber_Type()
)
logicalDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceSerialNumber.setStatus("mandatory")
_LogicalDeviceCU_Type = Integer32
_LogicalDeviceCU_Object = MibTableColumn
logicalDeviceCU = _LogicalDeviceCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 2),
    _LogicalDeviceCU_Type()
)
logicalDeviceCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceCU.setStatus("mandatory")
_LogicalDeviceLDEV_Type = Integer32
_LogicalDeviceLDEV_Object = MibTableColumn
logicalDeviceLDEV = _LogicalDeviceLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 3),
    _LogicalDeviceLDEV_Type()
)
logicalDeviceLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceLDEV.setStatus("mandatory")
_LogicalDeviceEmulation_Type = DisplayString
_LogicalDeviceEmulation_Object = MibTableColumn
logicalDeviceEmulation = _LogicalDeviceEmulation_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 4),
    _LogicalDeviceEmulation_Type()
)
logicalDeviceEmulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceEmulation.setStatus("mandatory")
_LogicalDeviceCylinder_Type = Integer32
_LogicalDeviceCylinder_Object = MibTableColumn
logicalDeviceCylinder = _LogicalDeviceCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 5),
    _LogicalDeviceCylinder_Type()
)
logicalDeviceCylinder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceCylinder.setStatus("mandatory")
_LogicalDeviceLUExpand_Type = Integer32
_LogicalDeviceLUExpand_Object = MibTableColumn
logicalDeviceLUExpand = _LogicalDeviceLUExpand_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 6),
    _LogicalDeviceLUExpand_Type()
)
logicalDeviceLUExpand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceLUExpand.setStatus("mandatory")
_LogicalDeviceLUPath_Type = Integer32
_LogicalDeviceLUPath_Object = MibTableColumn
logicalDeviceLUPath = _LogicalDeviceLUPath_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 7),
    _LogicalDeviceLUPath_Type()
)
logicalDeviceLUPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceLUPath.setStatus("mandatory")
_LogicalDeviceSize_Type = Integer32
_LogicalDeviceSize_Object = MibTableColumn
logicalDeviceSize = _LogicalDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 8),
    _LogicalDeviceSize_Type()
)
logicalDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceSize.setStatus("mandatory")
_LogicalDeviceLBA_Type = Integer32
_LogicalDeviceLBA_Object = MibTableColumn
logicalDeviceLBA = _LogicalDeviceLBA_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 9),
    _LogicalDeviceLBA_Type()
)
logicalDeviceLBA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceLBA.setStatus("mandatory")
_LogicalDeviceHIHSMReserve_Type = Integer32
_LogicalDeviceHIHSMReserve_Object = MibTableColumn
logicalDeviceHIHSMReserve = _LogicalDeviceHIHSMReserve_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 10),
    _LogicalDeviceHIHSMReserve_Type()
)
logicalDeviceHIHSMReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logicalDeviceHIHSMReserve.setStatus("mandatory")
_LogicalDeviceControlStatus_Type = Integer32
_LogicalDeviceControlStatus_Object = MibTableColumn
logicalDeviceControlStatus = _LogicalDeviceControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 11),
    _LogicalDeviceControlStatus_Type()
)
logicalDeviceControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logicalDeviceControlStatus.setStatus("mandatory")
_LogicalDeviceRAIDLevel_Type = DisplayString
_LogicalDeviceRAIDLevel_Object = MibTableColumn
logicalDeviceRAIDLevel = _LogicalDeviceRAIDLevel_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 12),
    _LogicalDeviceRAIDLevel_Type()
)
logicalDeviceRAIDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceRAIDLevel.setStatus("mandatory")
_LogicalDeviceSlotSize_Type = Integer32
_LogicalDeviceSlotSize_Object = MibTableColumn
logicalDeviceSlotSize = _LogicalDeviceSlotSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 10, 1, 1, 13),
    _LogicalDeviceSlotSize_Type()
)
logicalDeviceSlotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDeviceSlotSize.setStatus("mandatory")
_RaidExMibLUConfiguration_ObjectIdentity = ObjectIdentity
raidExMibLUConfiguration = _RaidExMibLUConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11)
)
_RaidExMibPortTable_Object = MibTable
raidExMibPortTable = _RaidExMibPortTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    raidExMibPortTable.setStatus("mandatory")
_RaidExMibPortEntry_Object = MibTableRow
raidExMibPortEntry = _RaidExMibPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1)
)
raidExMibPortEntry.setIndexNames(
    (0, "HDS9900MIB", "portSerialNumber"),
    (0, "HDS9900MIB", "portID"),
)
if mibBuilder.loadTexts:
    raidExMibPortEntry.setStatus("mandatory")
_PortSerialNumber_Type = Integer32
_PortSerialNumber_Object = MibTableColumn
portSerialNumber = _PortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 1),
    _PortSerialNumber_Type()
)
portSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSerialNumber.setStatus("mandatory")
_PortID_Type = Integer32
_PortID_Object = MibTableColumn
portID = _PortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 2),
    _PortID_Type()
)
portID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portID.setStatus("mandatory")
_PortKind_Type = DisplayString
_PortKind_Object = MibTableColumn
portKind = _PortKind_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 3),
    _PortKind_Type()
)
portKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portKind.setStatus("mandatory")


class _PortHostMode_Type(OctetString):
    """Custom type portHostMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PortHostMode_Type.__name__ = "OctetString"
_PortHostMode_Object = MibTableColumn
portHostMode = _PortHostMode_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 4),
    _PortHostMode_Type()
)
portHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portHostMode.setStatus("mandatory")
_PortFibreAddress_Type = Integer32
_PortFibreAddress_Object = MibTableColumn
portFibreAddress = _PortFibreAddress_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 5),
    _PortFibreAddress_Type()
)
portFibreAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFibreAddress.setStatus("mandatory")
_PortFibreTopology_Type = Integer32
_PortFibreTopology_Object = MibTableColumn
portFibreTopology = _PortFibreTopology_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 6),
    _PortFibreTopology_Type()
)
portFibreTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFibreTopology.setStatus("mandatory")
_PortControlStatus_Type = Integer32
_PortControlStatus_Object = MibTableColumn
portControlStatus = _PortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 7),
    _PortControlStatus_Type()
)
portControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlStatus.setStatus("mandatory")
_PortDisplayName_Type = DisplayString
_PortDisplayName_Object = MibTableColumn
portDisplayName = _PortDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 8),
    _PortDisplayName_Type()
)
portDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDisplayName.setStatus("mandatory")


class _PortWWN_Type(OctetString):
    """Custom type portWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PortWWN_Type.__name__ = "OctetString"
_PortWWN_Object = MibTableColumn
portWWN = _PortWWN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 1, 1, 9),
    _PortWWN_Type()
)
portWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portWWN.setStatus("mandatory")
_RaidExMibLU_ObjectIdentity = ObjectIdentity
raidExMibLU = _RaidExMibLU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2)
)
_RaidExMibLUInformationLUTable_Object = MibTable
raidExMibLUInformationLUTable = _RaidExMibLUInformationLUTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    raidExMibLUInformationLUTable.setStatus("mandatory")
_RaidExMibLUInformationLUEntry_Object = MibTableRow
raidExMibLUInformationLUEntry = _RaidExMibLUInformationLUEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1)
)
raidExMibLUInformationLUEntry.setIndexNames(
    (0, "HDS9900MIB", "luSerialNumber"),
    (0, "HDS9900MIB", "luDeviceCU"),
    (0, "HDS9900MIB", "luDeviceLDEV"),
)
if mibBuilder.loadTexts:
    raidExMibLUInformationLUEntry.setStatus("mandatory")
_LuSerialNumber_Type = Integer32
_LuSerialNumber_Object = MibTableColumn
luSerialNumber = _LuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 1),
    _LuSerialNumber_Type()
)
luSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSerialNumber.setStatus("mandatory")
_LuDeviceCU_Type = Integer32
_LuDeviceCU_Object = MibTableColumn
luDeviceCU = _LuDeviceCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 2),
    _LuDeviceCU_Type()
)
luDeviceCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceCU.setStatus("mandatory")
_LuDeviceLDEV_Type = Integer32
_LuDeviceLDEV_Object = MibTableColumn
luDeviceLDEV = _LuDeviceLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 3),
    _LuDeviceLDEV_Type()
)
luDeviceLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceLDEV.setStatus("mandatory")
_LuEmuID_Type = DisplayString
_LuEmuID_Object = MibTableColumn
luEmuID = _LuEmuID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 4),
    _LuEmuID_Type()
)
luEmuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luEmuID.setStatus("mandatory")
_LuCount_Type = Integer32
_LuCount_Object = MibTableColumn
luCount = _LuCount_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 5),
    _LuCount_Type()
)
luCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luCount.setStatus("mandatory")
_LuSize_Type = Integer32
_LuSize_Object = MibTableColumn
luSize = _LuSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 6),
    _LuSize_Type()
)
luSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSize.setStatus("mandatory")
_LuPath_Type = Integer32
_LuPath_Object = MibTableColumn
luPath = _LuPath_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 7),
    _LuPath_Type()
)
luPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luPath.setStatus("mandatory")
_LuCommandDev_Type = Integer32
_LuCommandDev_Object = MibTableColumn
luCommandDev = _LuCommandDev_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 8),
    _LuCommandDev_Type()
)
luCommandDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luCommandDev.setStatus("mandatory")
_LuControlStatus_Type = Integer32
_LuControlStatus_Object = MibTableColumn
luControlStatus = _LuControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 1, 1, 9),
    _LuControlStatus_Type()
)
luControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luControlStatus.setStatus("mandatory")
_RaidExMibLUPathTable_Object = MibTable
raidExMibLUPathTable = _RaidExMibLUPathTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    raidExMibLUPathTable.setStatus("mandatory")
_RaidExMibLUPathEntry_Object = MibTableRow
raidExMibLUPathEntry = _RaidExMibLUPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1)
)
raidExMibLUPathEntry.setIndexNames(
    (0, "HDS9900MIB", "luPathSerialNumber"),
    (0, "HDS9900MIB", "luPathControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibLUPathEntry.setStatus("mandatory")
_LuPathSerialNumber_Type = Integer32
_LuPathSerialNumber_Object = MibTableColumn
luPathSerialNumber = _LuPathSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 1),
    _LuPathSerialNumber_Type()
)
luPathSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luPathSerialNumber.setStatus("mandatory")
_LuPathControlIndex_Type = Integer32
_LuPathControlIndex_Object = MibTableColumn
luPathControlIndex = _LuPathControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 2),
    _LuPathControlIndex_Type()
)
luPathControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luPathControlIndex.setStatus("mandatory")
_LuPathPortID_Type = Integer32
_LuPathPortID_Object = MibTableColumn
luPathPortID = _LuPathPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 3),
    _LuPathPortID_Type()
)
luPathPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luPathPortID.setStatus("mandatory")
_LuPathSCSIID_Type = Integer32
_LuPathSCSIID_Object = MibTableColumn
luPathSCSIID = _LuPathSCSIID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 4),
    _LuPathSCSIID_Type()
)
luPathSCSIID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luPathSCSIID.setStatus("mandatory")
_LuPathLUN_Type = Integer32
_LuPathLUN_Object = MibTableColumn
luPathLUN = _LuPathLUN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 5),
    _LuPathLUN_Type()
)
luPathLUN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luPathLUN.setStatus("mandatory")
_LuPathDeviceCU_Type = Integer32
_LuPathDeviceCU_Object = MibTableColumn
luPathDeviceCU = _LuPathDeviceCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 6),
    _LuPathDeviceCU_Type()
)
luPathDeviceCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luPathDeviceCU.setStatus("mandatory")
_LuPathDeviceLDEV_Type = Integer32
_LuPathDeviceLDEV_Object = MibTableColumn
luPathDeviceLDEV = _LuPathDeviceLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 7),
    _LuPathDeviceLDEV_Type()
)
luPathDeviceLDEV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luPathDeviceLDEV.setStatus("mandatory")
_LuPathControlStatus_Type = Integer32
_LuPathControlStatus_Object = MibTableColumn
luPathControlStatus = _LuPathControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 2, 2, 1, 8),
    _LuPathControlStatus_Type()
)
luPathControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luPathControlStatus.setStatus("mandatory")
_RaidExMibLUSE_ObjectIdentity = ObjectIdentity
raidExMibLUSE = _RaidExMibLUSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3)
)
_RaidExMibLUSEStructureTable_Object = MibTable
raidExMibLUSEStructureTable = _RaidExMibLUSEStructureTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    raidExMibLUSEStructureTable.setStatus("mandatory")
_RaidExMibLUSEStructureEntry_Object = MibTableRow
raidExMibLUSEStructureEntry = _RaidExMibLUSEStructureEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1)
)
raidExMibLUSEStructureEntry.setIndexNames(
    (0, "HDS9900MIB", "luSEStructSerialNumber"),
    (0, "HDS9900MIB", "luSEStructControlIndex"),
    (0, "HDS9900MIB", "luSEStructOffset"),
)
if mibBuilder.loadTexts:
    raidExMibLUSEStructureEntry.setStatus("mandatory")
_LuSEStructSerialNumber_Type = Integer32
_LuSEStructSerialNumber_Object = MibTableColumn
luSEStructSerialNumber = _LuSEStructSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 1),
    _LuSEStructSerialNumber_Type()
)
luSEStructSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSEStructSerialNumber.setStatus("mandatory")
_LuSEStructControlIndex_Type = Integer32
_LuSEStructControlIndex_Object = MibTableColumn
luSEStructControlIndex = _LuSEStructControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 2),
    _LuSEStructControlIndex_Type()
)
luSEStructControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSEStructControlIndex.setStatus("mandatory")
_LuSEStructOffset_Type = Counter32
_LuSEStructOffset_Object = MibTableColumn
luSEStructOffset = _LuSEStructOffset_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 3),
    _LuSEStructOffset_Type()
)
luSEStructOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSEStructOffset.setStatus("mandatory")
_LuSEStructTopDeviceCU_Type = Integer32
_LuSEStructTopDeviceCU_Object = MibTableColumn
luSEStructTopDeviceCU = _LuSEStructTopDeviceCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 4),
    _LuSEStructTopDeviceCU_Type()
)
luSEStructTopDeviceCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luSEStructTopDeviceCU.setStatus("mandatory")
_LuSEStructTopDeviceLDEV_Type = Integer32
_LuSEStructTopDeviceLDEV_Object = MibTableColumn
luSEStructTopDeviceLDEV = _LuSEStructTopDeviceLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 5),
    _LuSEStructTopDeviceLDEV_Type()
)
luSEStructTopDeviceLDEV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luSEStructTopDeviceLDEV.setStatus("mandatory")
_LuSEStructDeviceCU_Type = Integer32
_LuSEStructDeviceCU_Object = MibTableColumn
luSEStructDeviceCU = _LuSEStructDeviceCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 6),
    _LuSEStructDeviceCU_Type()
)
luSEStructDeviceCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luSEStructDeviceCU.setStatus("mandatory")
_LuSEStructDeviceLDEV_Type = Integer32
_LuSEStructDeviceLDEV_Object = MibTableColumn
luSEStructDeviceLDEV = _LuSEStructDeviceLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 7),
    _LuSEStructDeviceLDEV_Type()
)
luSEStructDeviceLDEV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luSEStructDeviceLDEV.setStatus("mandatory")
_LuSEStructControlStatus_Type = Integer32
_LuSEStructControlStatus_Object = MibTableColumn
luSEStructControlStatus = _LuSEStructControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 3, 1, 1, 8),
    _LuSEStructControlStatus_Type()
)
luSEStructControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    luSEStructControlStatus.setStatus("mandatory")
_RaidExMibLUNS_ObjectIdentity = ObjectIdentity
raidExMibLUNS = _RaidExMibLUNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4)
)
_RaidExMibLUNSSwitchTable_Object = MibTable
raidExMibLUNSSwitchTable = _RaidExMibLUNSSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    raidExMibLUNSSwitchTable.setStatus("mandatory")
_RaidExMibLUNSSwitchEntry_Object = MibTableRow
raidExMibLUNSSwitchEntry = _RaidExMibLUNSSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 1, 1)
)
raidExMibLUNSSwitchEntry.setIndexNames(
    (0, "HDS9900MIB", "switchSerialNumber"),
    (0, "HDS9900MIB", "switchPortID"),
)
if mibBuilder.loadTexts:
    raidExMibLUNSSwitchEntry.setStatus("mandatory")
_SwitchSerialNumber_Type = Integer32
_SwitchSerialNumber_Object = MibTableColumn
switchSerialNumber = _SwitchSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 1, 1, 1),
    _SwitchSerialNumber_Type()
)
switchSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchSerialNumber.setStatus("mandatory")
_SwitchPortID_Type = Integer32
_SwitchPortID_Object = MibTableColumn
switchPortID = _SwitchPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 1, 1, 2),
    _SwitchPortID_Type()
)
switchPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortID.setStatus("mandatory")
_SwitchOnOff_Type = Integer32
_SwitchOnOff_Object = MibTableColumn
switchOnOff = _SwitchOnOff_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 1, 1, 3),
    _SwitchOnOff_Type()
)
switchOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchOnOff.setStatus("mandatory")
_SwitchControlStatus_Type = Integer32
_SwitchControlStatus_Object = MibTableColumn
switchControlStatus = _SwitchControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 1, 1, 4),
    _SwitchControlStatus_Type()
)
switchControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchControlStatus.setStatus("mandatory")
_RaidExMibLUNSWWNTable_Object = MibTable
raidExMibLUNSWWNTable = _RaidExMibLUNSWWNTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2)
)
if mibBuilder.loadTexts:
    raidExMibLUNSWWNTable.setStatus("mandatory")
_RaidExMibLUNSWWNEntry_Object = MibTableRow
raidExMibLUNSWWNEntry = _RaidExMibLUNSWWNEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1)
)
raidExMibLUNSWWNEntry.setIndexNames(
    (0, "HDS9900MIB", "wwnSerialNumber"),
    (0, "HDS9900MIB", "wwnPortID"),
    (0, "HDS9900MIB", "wwnControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibLUNSWWNEntry.setStatus("mandatory")
_WwnSerialNumber_Type = Integer32
_WwnSerialNumber_Object = MibTableColumn
wwnSerialNumber = _WwnSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 1),
    _WwnSerialNumber_Type()
)
wwnSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnSerialNumber.setStatus("mandatory")
_WwnPortID_Type = Integer32
_WwnPortID_Object = MibTableColumn
wwnPortID = _WwnPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 2),
    _WwnPortID_Type()
)
wwnPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnPortID.setStatus("mandatory")
_WwnControlIndex_Type = Integer32
_WwnControlIndex_Object = MibTableColumn
wwnControlIndex = _WwnControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 3),
    _WwnControlIndex_Type()
)
wwnControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnControlIndex.setStatus("mandatory")


class _WwnWWN_Type(OctetString):
    """Custom type wwnWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WwnWWN_Type.__name__ = "OctetString"
_WwnWWN_Object = MibTableColumn
wwnWWN = _WwnWWN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 4),
    _WwnWWN_Type()
)
wwnWWN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnWWN.setStatus("mandatory")
_WwnID_Type = Integer32
_WwnID_Object = MibTableColumn
wwnID = _WwnID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 5),
    _WwnID_Type()
)
wwnID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnID.setStatus("mandatory")


class _WwnNickname_Type(DisplayString):
    """Custom type wwnNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WwnNickname_Type.__name__ = "DisplayString"
_WwnNickname_Object = MibTableColumn
wwnNickname = _WwnNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 6),
    _WwnNickname_Type()
)
wwnNickname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnNickname.setStatus("deprecated")
_WwnUseNickname_Type = Integer32
_WwnUseNickname_Object = MibTableColumn
wwnUseNickname = _WwnUseNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 7),
    _WwnUseNickname_Type()
)
wwnUseNickname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnUseNickname.setStatus("mandatory")
_WwnControlStatus_Type = Integer32
_WwnControlStatus_Object = MibTableColumn
wwnControlStatus = _WwnControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 2, 1, 8),
    _WwnControlStatus_Type()
)
wwnControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnControlStatus.setStatus("mandatory")
_RaidExMibLUNSWWNGroupTable_Object = MibTable
raidExMibLUNSWWNGroupTable = _RaidExMibLUNSWWNGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3)
)
if mibBuilder.loadTexts:
    raidExMibLUNSWWNGroupTable.setStatus("mandatory")
_RaidExMibLUNSWWNGroupEntry_Object = MibTableRow
raidExMibLUNSWWNGroupEntry = _RaidExMibLUNSWWNGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1)
)
raidExMibLUNSWWNGroupEntry.setIndexNames(
    (0, "HDS9900MIB", "wwnGroupSerialNumber"),
    (0, "HDS9900MIB", "wwnGroupPortID"),
    (0, "HDS9900MIB", "wwnGroupControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibLUNSWWNGroupEntry.setStatus("mandatory")
_WwnGroupSerialNumber_Type = Integer32
_WwnGroupSerialNumber_Object = MibTableColumn
wwnGroupSerialNumber = _WwnGroupSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1, 1),
    _WwnGroupSerialNumber_Type()
)
wwnGroupSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnGroupSerialNumber.setStatus("mandatory")
_WwnGroupPortID_Type = Integer32
_WwnGroupPortID_Object = MibTableColumn
wwnGroupPortID = _WwnGroupPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1, 2),
    _WwnGroupPortID_Type()
)
wwnGroupPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnGroupPortID.setStatus("mandatory")
_WwnGroupControlIndex_Type = Integer32
_WwnGroupControlIndex_Object = MibTableColumn
wwnGroupControlIndex = _WwnGroupControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1, 3),
    _WwnGroupControlIndex_Type()
)
wwnGroupControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwnGroupControlIndex.setStatus("mandatory")
_WwnGroupID_Type = Integer32
_WwnGroupID_Object = MibTableColumn
wwnGroupID = _WwnGroupID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1, 4),
    _WwnGroupID_Type()
)
wwnGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnGroupID.setStatus("mandatory")


class _WwnGroupNickname_Type(DisplayString):
    """Custom type wwnGroupNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WwnGroupNickname_Type.__name__ = "DisplayString"
_WwnGroupNickname_Object = MibTableColumn
wwnGroupNickname = _WwnGroupNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1, 5),
    _WwnGroupNickname_Type()
)
wwnGroupNickname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnGroupNickname.setStatus("mandatory")
_WwnGroupControlStatus_Type = Integer32
_WwnGroupControlStatus_Object = MibTableColumn
wwnGroupControlStatus = _WwnGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1, 7),
    _WwnGroupControlStatus_Type()
)
wwnGroupControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnGroupControlStatus.setStatus("mandatory")
_WwnGroupedWWNsVL_Type = OctetString
_WwnGroupedWWNsVL_Object = MibTableColumn
wwnGroupedWWNsVL = _WwnGroupedWWNsVL_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 3, 1, 8),
    _WwnGroupedWWNsVL_Type()
)
wwnGroupedWWNsVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwnGroupedWWNsVL.setStatus("mandatory")
_RaidExMibLUNSLUNTable_Object = MibTable
raidExMibLUNSLUNTable = _RaidExMibLUNSLUNTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4)
)
if mibBuilder.loadTexts:
    raidExMibLUNSLUNTable.setStatus("mandatory")
_RaidExMibLUNSLUNEntry_Object = MibTableRow
raidExMibLUNSLUNEntry = _RaidExMibLUNSLUNEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4, 1)
)
raidExMibLUNSLUNEntry.setIndexNames(
    (0, "HDS9900MIB", "lunSerialNumber"),
    (0, "HDS9900MIB", "lunPortID"),
    (0, "HDS9900MIB", "lunLUN"),
)
if mibBuilder.loadTexts:
    raidExMibLUNSLUNEntry.setStatus("mandatory")
_LunSerialNumber_Type = Integer32
_LunSerialNumber_Object = MibTableColumn
lunSerialNumber = _LunSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4, 1, 1),
    _LunSerialNumber_Type()
)
lunSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSerialNumber.setStatus("mandatory")
_LunPortID_Type = Integer32
_LunPortID_Object = MibTableColumn
lunPortID = _LunPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4, 1, 2),
    _LunPortID_Type()
)
lunPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunPortID.setStatus("mandatory")
_LunLUN_Type = Integer32
_LunLUN_Object = MibTableColumn
lunLUN = _LunLUN_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4, 1, 3),
    _LunLUN_Type()
)
lunLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLUN.setStatus("mandatory")
_LunControlStatus_Type = Integer32
_LunControlStatus_Object = MibTableColumn
lunControlStatus = _LunControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4, 1, 6),
    _LunControlStatus_Type()
)
lunControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunControlStatus.setStatus("mandatory")
_LunWWNSecurityVL_Type = OctetString
_LunWWNSecurityVL_Object = MibTableColumn
lunWWNSecurityVL = _LunWWNSecurityVL_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4, 1, 7),
    _LunWWNSecurityVL_Type()
)
lunWWNSecurityVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunWWNSecurityVL.setStatus("mandatory")
_LunWWNGroupSecurityVL_Type = OctetString
_LunWWNGroupSecurityVL_Object = MibTableColumn
lunWWNGroupSecurityVL = _LunWWNGroupSecurityVL_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 4, 1, 8),
    _LunWWNGroupSecurityVL_Type()
)
lunWWNGroupSecurityVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunWWNGroupSecurityVL.setStatus("mandatory")
_RaidExMibLUNSLUNGroupTable_Object = MibTable
raidExMibLUNSLUNGroupTable = _RaidExMibLUNSLUNGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5)
)
if mibBuilder.loadTexts:
    raidExMibLUNSLUNGroupTable.setStatus("mandatory")
_RaidExMibLUNSLUNGroupEntry_Object = MibTableRow
raidExMibLUNSLUNGroupEntry = _RaidExMibLUNSLUNGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1)
)
raidExMibLUNSLUNGroupEntry.setIndexNames(
    (0, "HDS9900MIB", "lunGroupSerialNumber"),
    (0, "HDS9900MIB", "lunGroupPortID"),
    (0, "HDS9900MIB", "lunGroupControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibLUNSLUNGroupEntry.setStatus("mandatory")
_LunGroupSerialNumber_Type = Integer32
_LunGroupSerialNumber_Object = MibTableColumn
lunGroupSerialNumber = _LunGroupSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 1),
    _LunGroupSerialNumber_Type()
)
lunGroupSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunGroupSerialNumber.setStatus("mandatory")
_LunGroupPortID_Type = Integer32
_LunGroupPortID_Object = MibTableColumn
lunGroupPortID = _LunGroupPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 2),
    _LunGroupPortID_Type()
)
lunGroupPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunGroupPortID.setStatus("mandatory")
_LunGroupControlIndex_Type = Integer32
_LunGroupControlIndex_Object = MibTableColumn
lunGroupControlIndex = _LunGroupControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 3),
    _LunGroupControlIndex_Type()
)
lunGroupControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunGroupControlIndex.setStatus("mandatory")
_LunGroupID_Type = Integer32
_LunGroupID_Object = MibTableColumn
lunGroupID = _LunGroupID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 4),
    _LunGroupID_Type()
)
lunGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunGroupID.setStatus("mandatory")


class _LunGroupNickname_Type(DisplayString):
    """Custom type lunGroupNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LunGroupNickname_Type.__name__ = "DisplayString"
_LunGroupNickname_Object = MibTableColumn
lunGroupNickname = _LunGroupNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 5),
    _LunGroupNickname_Type()
)
lunGroupNickname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunGroupNickname.setStatus("deprecated")
_LunGroupControlStatus_Type = Integer32
_LunGroupControlStatus_Object = MibTableColumn
lunGroupControlStatus = _LunGroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 9),
    _LunGroupControlStatus_Type()
)
lunGroupControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunGroupControlStatus.setStatus("mandatory")
_LunGroupedLUNsVL_Type = OctetString
_LunGroupedLUNsVL_Object = MibTableColumn
lunGroupedLUNsVL = _LunGroupedLUNsVL_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 10),
    _LunGroupedLUNsVL_Type()
)
lunGroupedLUNsVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunGroupedLUNsVL.setStatus("mandatory")
_LunGroupWWNSecurityVL_Type = OctetString
_LunGroupWWNSecurityVL_Object = MibTableColumn
lunGroupWWNSecurityVL = _LunGroupWWNSecurityVL_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 11),
    _LunGroupWWNSecurityVL_Type()
)
lunGroupWWNSecurityVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunGroupWWNSecurityVL.setStatus("mandatory")
_LunGroupWWNGroupSecurityVL_Type = OctetString
_LunGroupWWNGroupSecurityVL_Object = MibTableColumn
lunGroupWWNGroupSecurityVL = _LunGroupWWNGroupSecurityVL_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 11, 4, 5, 1, 12),
    _LunGroupWWNGroupSecurityVL_Type()
)
lunGroupWWNGroupSecurityVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lunGroupWWNGroupSecurityVL.setStatus("mandatory")
_RaidExMibDCRConfiguration_ObjectIdentity = ObjectIdentity
raidExMibDCRConfiguration = _RaidExMibDCRConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12)
)
_RaidExMibCacheSizeTable_Object = MibTable
raidExMibCacheSizeTable = _RaidExMibCacheSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    raidExMibCacheSizeTable.setStatus("mandatory")
_RaidExMibCacheSizeEntry_Object = MibTableRow
raidExMibCacheSizeEntry = _RaidExMibCacheSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 1, 1)
)
raidExMibCacheSizeEntry.setIndexNames(
    (0, "HDS9900MIB", "cacheSizeSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCacheSizeEntry.setStatus("mandatory")
_CacheSizeSerialNumber_Type = Integer32
_CacheSizeSerialNumber_Object = MibTableColumn
cacheSizeSerialNumber = _CacheSizeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 1, 1, 1),
    _CacheSizeSerialNumber_Type()
)
cacheSizeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSizeSerialNumber.setStatus("mandatory")
_CacheSizeTotalCacheSize_Type = Integer32
_CacheSizeTotalCacheSize_Object = MibTableColumn
cacheSizeTotalCacheSize = _CacheSizeTotalCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 1, 1, 2),
    _CacheSizeTotalCacheSize_Type()
)
cacheSizeTotalCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSizeTotalCacheSize.setStatus("mandatory")
_CacheSizeUseCacheSize_Type = Integer32
_CacheSizeUseCacheSize_Object = MibTableColumn
cacheSizeUseCacheSize = _CacheSizeUseCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 1, 1, 3),
    _CacheSizeUseCacheSize_Type()
)
cacheSizeUseCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSizeUseCacheSize.setStatus("mandatory")
_CacheSizeRemainCacheSize_Type = Integer32
_CacheSizeRemainCacheSize_Object = MibTableColumn
cacheSizeRemainCacheSize = _CacheSizeRemainCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 1, 1, 4),
    _CacheSizeRemainCacheSize_Type()
)
cacheSizeRemainCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSizeRemainCacheSize.setStatus("mandatory")
_RaidExMibCacheDCRTable_Object = MibTable
raidExMibCacheDCRTable = _RaidExMibCacheDCRTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    raidExMibCacheDCRTable.setStatus("mandatory")
_RaidExMibCacheDCREntry_Object = MibTableRow
raidExMibCacheDCREntry = _RaidExMibCacheDCREntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1)
)
raidExMibCacheDCREntry.setIndexNames(
    (0, "HDS9900MIB", "cacheDCRSerialNumber"),
    (0, "HDS9900MIB", "cacheDCRCU"),
    (0, "HDS9900MIB", "cacheDCRLDEV"),
    (0, "HDS9900MIB", "cacheDCRControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibCacheDCREntry.setStatus("mandatory")
_CacheDCRSerialNumber_Type = Integer32
_CacheDCRSerialNumber_Object = MibTableColumn
cacheDCRSerialNumber = _CacheDCRSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 1),
    _CacheDCRSerialNumber_Type()
)
cacheDCRSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDCRSerialNumber.setStatus("mandatory")
_CacheDCRCU_Type = Integer32
_CacheDCRCU_Object = MibTableColumn
cacheDCRCU = _CacheDCRCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 2),
    _CacheDCRCU_Type()
)
cacheDCRCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDCRCU.setStatus("mandatory")
_CacheDCRLDEV_Type = Integer32
_CacheDCRLDEV_Object = MibTableColumn
cacheDCRLDEV = _CacheDCRLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 3),
    _CacheDCRLDEV_Type()
)
cacheDCRLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDCRLDEV.setStatus("mandatory")
_CacheDCRControlIndex_Type = Integer32
_CacheDCRControlIndex_Object = MibTableColumn
cacheDCRControlIndex = _CacheDCRControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 4),
    _CacheDCRControlIndex_Type()
)
cacheDCRControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDCRControlIndex.setStatus("mandatory")
_CacheDCRMode_Type = Integer32
_CacheDCRMode_Object = MibTableColumn
cacheDCRMode = _CacheDCRMode_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 5),
    _CacheDCRMode_Type()
)
cacheDCRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCRMode.setStatus("mandatory")
_CacheDCRAllOfDevice_Type = Integer32
_CacheDCRAllOfDevice_Object = MibTableColumn
cacheDCRAllOfDevice = _CacheDCRAllOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 6),
    _CacheDCRAllOfDevice_Type()
)
cacheDCRAllOfDevice.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cacheDCRAllOfDevice.setStatus("mandatory")
_CacheDCRStartCylinder_Type = Integer32
_CacheDCRStartCylinder_Object = MibTableColumn
cacheDCRStartCylinder = _CacheDCRStartCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 7),
    _CacheDCRStartCylinder_Type()
)
cacheDCRStartCylinder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCRStartCylinder.setStatus("mandatory")
_CacheDCRStartHead_Type = Integer32
_CacheDCRStartHead_Object = MibTableColumn
cacheDCRStartHead = _CacheDCRStartHead_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 8),
    _CacheDCRStartHead_Type()
)
cacheDCRStartHead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCRStartHead.setStatus("mandatory")
_CacheDCREndCylinder_Type = Integer32
_CacheDCREndCylinder_Object = MibTableColumn
cacheDCREndCylinder = _CacheDCREndCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 9),
    _CacheDCREndCylinder_Type()
)
cacheDCREndCylinder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCREndCylinder.setStatus("mandatory")
_CacheDCREndHead_Type = Integer32
_CacheDCREndHead_Object = MibTableColumn
cacheDCREndHead = _CacheDCREndHead_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 10),
    _CacheDCREndHead_Type()
)
cacheDCREndHead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCREndHead.setStatus("mandatory")
_CacheDCRCylinderSize_Type = Integer32
_CacheDCRCylinderSize_Object = MibTableColumn
cacheDCRCylinderSize = _CacheDCRCylinderSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 11),
    _CacheDCRCylinderSize_Type()
)
cacheDCRCylinderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDCRCylinderSize.setStatus("mandatory")
_CacheDCRHeadSize_Type = Integer32
_CacheDCRHeadSize_Object = MibTableColumn
cacheDCRHeadSize = _CacheDCRHeadSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 12),
    _CacheDCRHeadSize_Type()
)
cacheDCRHeadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDCRHeadSize.setStatus("mandatory")
_CacheDCRStartLBA_Type = Integer32
_CacheDCRStartLBA_Object = MibTableColumn
cacheDCRStartLBA = _CacheDCRStartLBA_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 13),
    _CacheDCRStartLBA_Type()
)
cacheDCRStartLBA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCRStartLBA.setStatus("mandatory")
_CacheDCREndLBA_Type = Integer32
_CacheDCREndLBA_Object = MibTableColumn
cacheDCREndLBA = _CacheDCREndLBA_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 14),
    _CacheDCREndLBA_Type()
)
cacheDCREndLBA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCREndLBA.setStatus("mandatory")
_CacheDCRLBASize_Type = Integer32
_CacheDCRLBASize_Object = MibTableColumn
cacheDCRLBASize = _CacheDCRLBASize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 15),
    _CacheDCRLBASize_Type()
)
cacheDCRLBASize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDCRLBASize.setStatus("mandatory")
_CacheDCRControlStatus_Type = Integer32
_CacheDCRControlStatus_Object = MibTableColumn
cacheDCRControlStatus = _CacheDCRControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 12, 2, 1, 16),
    _CacheDCRControlStatus_Type()
)
cacheDCRControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cacheDCRControlStatus.setStatus("mandatory")
_RaidExMibCVSConfiguration_ObjectIdentity = ObjectIdentity
raidExMibCVSConfiguration = _RaidExMibCVSConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13)
)
_RaidExMibCustomizedVolumeTable_Object = MibTable
raidExMibCustomizedVolumeTable = _RaidExMibCustomizedVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3)
)
if mibBuilder.loadTexts:
    raidExMibCustomizedVolumeTable.setStatus("mandatory")
_RaidExMibCustomizedVolumeEntry_Object = MibTableRow
raidExMibCustomizedVolumeEntry = _RaidExMibCustomizedVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1)
)
raidExMibCustomizedVolumeEntry.setIndexNames(
    (0, "HDS9900MIB", "customizedVolumeSerialNumber"),
    (0, "HDS9900MIB", "customizedVolumeFB4Number"),
    (0, "HDS9900MIB", "customizedVolumePGNumber"),
    (0, "HDS9900MIB", "customizedVolumeCU"),
    (0, "HDS9900MIB", "customizedVolumeLDEV"),
)
if mibBuilder.loadTexts:
    raidExMibCustomizedVolumeEntry.setStatus("mandatory")
_CustomizedVolumeSerialNumber_Type = Integer32
_CustomizedVolumeSerialNumber_Object = MibTableColumn
customizedVolumeSerialNumber = _CustomizedVolumeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 1),
    _CustomizedVolumeSerialNumber_Type()
)
customizedVolumeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumeSerialNumber.setStatus("mandatory")
_CustomizedVolumeFB4Number_Type = Integer32
_CustomizedVolumeFB4Number_Object = MibTableColumn
customizedVolumeFB4Number = _CustomizedVolumeFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 2),
    _CustomizedVolumeFB4Number_Type()
)
customizedVolumeFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumeFB4Number.setStatus("mandatory")
_CustomizedVolumePGNumber_Type = Integer32
_CustomizedVolumePGNumber_Object = MibTableColumn
customizedVolumePGNumber = _CustomizedVolumePGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 3),
    _CustomizedVolumePGNumber_Type()
)
customizedVolumePGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumePGNumber.setStatus("mandatory")
_CustomizedVolumeCU_Type = Integer32
_CustomizedVolumeCU_Object = MibTableColumn
customizedVolumeCU = _CustomizedVolumeCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 4),
    _CustomizedVolumeCU_Type()
)
customizedVolumeCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumeCU.setStatus("mandatory")
_CustomizedVolumeLDEV_Type = Integer32
_CustomizedVolumeLDEV_Object = MibTableColumn
customizedVolumeLDEV = _CustomizedVolumeLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 5),
    _CustomizedVolumeLDEV_Type()
)
customizedVolumeLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumeLDEV.setStatus("mandatory")
_CustomizedVolumeType_Type = Integer32
_CustomizedVolumeType_Object = MibTableColumn
customizedVolumeType = _CustomizedVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 6),
    _CustomizedVolumeType_Type()
)
customizedVolumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumeType.setStatus("mandatory")
_CustomizedVolumeEmulation_Type = DisplayString
_CustomizedVolumeEmulation_Object = MibTableColumn
customizedVolumeEmulation = _CustomizedVolumeEmulation_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 7),
    _CustomizedVolumeEmulation_Type()
)
customizedVolumeEmulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customizedVolumeEmulation.setStatus("mandatory")
_CustomizedVolumeUserCylinder_Type = Integer32
_CustomizedVolumeUserCylinder_Object = MibTableColumn
customizedVolumeUserCylinder = _CustomizedVolumeUserCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 8),
    _CustomizedVolumeUserCylinder_Type()
)
customizedVolumeUserCylinder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customizedVolumeUserCylinder.setStatus("mandatory")
_CustomizedVolumeUserSize_Type = Integer32
_CustomizedVolumeUserSize_Object = MibTableColumn
customizedVolumeUserSize = _CustomizedVolumeUserSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 9),
    _CustomizedVolumeUserSize_Type()
)
customizedVolumeUserSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customizedVolumeUserSize.setStatus("mandatory")
_CustomizedVolumeControlCylinder_Type = Integer32
_CustomizedVolumeControlCylinder_Object = MibTableColumn
customizedVolumeControlCylinder = _CustomizedVolumeControlCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 10),
    _CustomizedVolumeControlCylinder_Type()
)
customizedVolumeControlCylinder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumeControlCylinder.setStatus("mandatory")
_CustomizedVolumeControlSize_Type = Integer32
_CustomizedVolumeControlSize_Object = MibTableColumn
customizedVolumeControlSize = _CustomizedVolumeControlSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 11),
    _CustomizedVolumeControlSize_Type()
)
customizedVolumeControlSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedVolumeControlSize.setStatus("mandatory")
_CustomizedVolumeControlStatus_Type = Integer32
_CustomizedVolumeControlStatus_Object = MibTableColumn
customizedVolumeControlStatus = _CustomizedVolumeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 3, 1, 12),
    _CustomizedVolumeControlStatus_Type()
)
customizedVolumeControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customizedVolumeControlStatus.setStatus("mandatory")
_RaidExMibCVSDeletedVolumeTable_Object = MibTable
raidExMibCVSDeletedVolumeTable = _RaidExMibCVSDeletedVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4)
)
if mibBuilder.loadTexts:
    raidExMibCVSDeletedVolumeTable.setStatus("mandatory")
_RaidExMibCVSDeletedVolumeEntry_Object = MibTableRow
raidExMibCVSDeletedVolumeEntry = _RaidExMibCVSDeletedVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1)
)
raidExMibCVSDeletedVolumeEntry.setIndexNames(
    (0, "HDS9900MIB", "cvsDVSerialNumber"),
    (0, "HDS9900MIB", "cvsDVFB4Number"),
    (0, "HDS9900MIB", "cvsDVPGNumber"),
    (0, "HDS9900MIB", "cvsDVControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibCVSDeletedVolumeEntry.setStatus("mandatory")
_CvsDVSerialNumber_Type = Integer32
_CvsDVSerialNumber_Object = MibTableColumn
cvsDVSerialNumber = _CvsDVSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 1),
    _CvsDVSerialNumber_Type()
)
cvsDVSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVSerialNumber.setStatus("mandatory")
_CvsDVFB4Number_Type = Integer32
_CvsDVFB4Number_Object = MibTableColumn
cvsDVFB4Number = _CvsDVFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 2),
    _CvsDVFB4Number_Type()
)
cvsDVFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVFB4Number.setStatus("mandatory")
_CvsDVPGNumber_Type = Integer32
_CvsDVPGNumber_Object = MibTableColumn
cvsDVPGNumber = _CvsDVPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 3),
    _CvsDVPGNumber_Type()
)
cvsDVPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVPGNumber.setStatus("mandatory")
_CvsDVControlIndex_Type = Integer32
_CvsDVControlIndex_Object = MibTableColumn
cvsDVControlIndex = _CvsDVControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 4),
    _CvsDVControlIndex_Type()
)
cvsDVControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVControlIndex.setStatus("mandatory")
_CvsDVCU_Type = Integer32
_CvsDVCU_Object = MibTableColumn
cvsDVCU = _CvsDVCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 5),
    _CvsDVCU_Type()
)
cvsDVCU.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cvsDVCU.setStatus("mandatory")
_CvsDVLDEV_Type = Integer32
_CvsDVLDEV_Object = MibTableColumn
cvsDVLDEV = _CvsDVLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 6),
    _CvsDVLDEV_Type()
)
cvsDVLDEV.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cvsDVLDEV.setStatus("mandatory")
_CvsDVEmulation_Type = DisplayString
_CvsDVEmulation_Object = MibTableColumn
cvsDVEmulation = _CvsDVEmulation_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 7),
    _CvsDVEmulation_Type()
)
cvsDVEmulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVEmulation.setStatus("mandatory")
_CvsDVCylinder_Type = Integer32
_CvsDVCylinder_Object = MibTableColumn
cvsDVCylinder = _CvsDVCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 8),
    _CvsDVCylinder_Type()
)
cvsDVCylinder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVCylinder.setStatus("mandatory")
_CvsDVSize_Type = Integer32
_CvsDVSize_Object = MibTableColumn
cvsDVSize = _CvsDVSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 9),
    _CvsDVSize_Type()
)
cvsDVSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVSize.setStatus("mandatory")
_CvsDVControlCylinder_Type = Integer32
_CvsDVControlCylinder_Object = MibTableColumn
cvsDVControlCylinder = _CvsDVControlCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 10),
    _CvsDVControlCylinder_Type()
)
cvsDVControlCylinder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVControlCylinder.setStatus("mandatory")
_CvsDVControlSize_Type = Integer32
_CvsDVControlSize_Object = MibTableColumn
cvsDVControlSize = _CvsDVControlSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 11),
    _CvsDVControlSize_Type()
)
cvsDVControlSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsDVControlSize.setStatus("mandatory")
_CvsDVControlStatus_Type = Integer32
_CvsDVControlStatus_Object = MibTableColumn
cvsDVControlStatus = _CvsDVControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 4, 1, 12),
    _CvsDVControlStatus_Type()
)
cvsDVControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsDVControlStatus.setStatus("mandatory")
_RaidExMibCVSFreeSpaceTable_Object = MibTable
raidExMibCVSFreeSpaceTable = _RaidExMibCVSFreeSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5)
)
if mibBuilder.loadTexts:
    raidExMibCVSFreeSpaceTable.setStatus("mandatory")
_RaidExMibCVSFreeSpaceEntry_Object = MibTableRow
raidExMibCVSFreeSpaceEntry = _RaidExMibCVSFreeSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5, 1)
)
raidExMibCVSFreeSpaceEntry.setIndexNames(
    (0, "HDS9900MIB", "cvsFSSerialNumber"),
    (0, "HDS9900MIB", "cvsFSFB4Number"),
    (0, "HDS9900MIB", "cvsFSPGNumber"),
    (0, "HDS9900MIB", "cvsFSControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibCVSFreeSpaceEntry.setStatus("mandatory")
_CvsFSSerialNumber_Type = Integer32
_CvsFSSerialNumber_Object = MibTableColumn
cvsFSSerialNumber = _CvsFSSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5, 1, 1),
    _CvsFSSerialNumber_Type()
)
cvsFSSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsFSSerialNumber.setStatus("mandatory")
_CvsFSFB4Number_Type = Integer32
_CvsFSFB4Number_Object = MibTableColumn
cvsFSFB4Number = _CvsFSFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5, 1, 2),
    _CvsFSFB4Number_Type()
)
cvsFSFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsFSFB4Number.setStatus("mandatory")
_CvsFSPGNumber_Type = Integer32
_CvsFSPGNumber_Object = MibTableColumn
cvsFSPGNumber = _CvsFSPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5, 1, 3),
    _CvsFSPGNumber_Type()
)
cvsFSPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsFSPGNumber.setStatus("mandatory")
_CvsFSControlIndex_Type = Integer32
_CvsFSControlIndex_Object = MibTableColumn
cvsFSControlIndex = _CvsFSControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5, 1, 4),
    _CvsFSControlIndex_Type()
)
cvsFSControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsFSControlIndex.setStatus("mandatory")
_CvsFSCylinder_Type = Integer32
_CvsFSCylinder_Object = MibTableColumn
cvsFSCylinder = _CvsFSCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5, 1, 5),
    _CvsFSCylinder_Type()
)
cvsFSCylinder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsFSCylinder.setStatus("mandatory")
_CvsFSSize_Type = Integer32
_CvsFSSize_Object = MibTableColumn
cvsFSSize = _CvsFSSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 5, 1, 6),
    _CvsFSSize_Type()
)
cvsFSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsFSSize.setStatus("mandatory")
_RaidExMibCVSParityGroupTable_Object = MibTable
raidExMibCVSParityGroupTable = _RaidExMibCVSParityGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6)
)
if mibBuilder.loadTexts:
    raidExMibCVSParityGroupTable.setStatus("mandatory")
_RaidExMibCVSParityGroupEntry_Object = MibTableRow
raidExMibCVSParityGroupEntry = _RaidExMibCVSParityGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1)
)
raidExMibCVSParityGroupEntry.setIndexNames(
    (0, "HDS9900MIB", "cvsPGSerialNumber"),
    (0, "HDS9900MIB", "cvsPGFB4Number"),
    (0, "HDS9900MIB", "cvsPGPGNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCVSParityGroupEntry.setStatus("mandatory")
_CvsPGSerialNumber_Type = Integer32
_CvsPGSerialNumber_Object = MibTableColumn
cvsPGSerialNumber = _CvsPGSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 1),
    _CvsPGSerialNumber_Type()
)
cvsPGSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGSerialNumber.setStatus("mandatory")
_CvsPGFB4Number_Type = Integer32
_CvsPGFB4Number_Object = MibTableColumn
cvsPGFB4Number = _CvsPGFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 2),
    _CvsPGFB4Number_Type()
)
cvsPGFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGFB4Number.setStatus("mandatory")
_CvsPGPGNumber_Type = Integer32
_CvsPGPGNumber_Object = MibTableColumn
cvsPGPGNumber = _CvsPGPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 3),
    _CvsPGPGNumber_Type()
)
cvsPGPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGPGNumber.setStatus("mandatory")
_CvsPGDisplayName_Type = DisplayString
_CvsPGDisplayName_Object = MibTableColumn
cvsPGDisplayName = _CvsPGDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 4),
    _CvsPGDisplayName_Type()
)
cvsPGDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGDisplayName.setStatus("mandatory")
_CvsPGRAIDType_Type = DisplayString
_CvsPGRAIDType_Object = MibTableColumn
cvsPGRAIDType = _CvsPGRAIDType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 5),
    _CvsPGRAIDType_Type()
)
cvsPGRAIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGRAIDType.setStatus("mandatory")
_CvsPGDriveType_Type = DisplayString
_CvsPGDriveType_Object = MibTableColumn
cvsPGDriveType = _CvsPGDriveType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 6),
    _CvsPGDriveType_Type()
)
cvsPGDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGDriveType.setStatus("mandatory")
_CvsPGFreeCylinder_Type = Integer32
_CvsPGFreeCylinder_Object = MibTableColumn
cvsPGFreeCylinder = _CvsPGFreeCylinder_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 7),
    _CvsPGFreeCylinder_Type()
)
cvsPGFreeCylinder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGFreeCylinder.setStatus("mandatory")
_CvsPGFreeSize_Type = Integer32
_CvsPGFreeSize_Object = MibTableColumn
cvsPGFreeSize = _CvsPGFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 8),
    _CvsPGFreeSize_Type()
)
cvsPGFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsPGFreeSize.setStatus("mandatory")
_CvsPGControlStatus_Type = Integer32
_CvsPGControlStatus_Object = MibTableColumn
cvsPGControlStatus = _CvsPGControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 6, 1, 9),
    _CvsPGControlStatus_Type()
)
cvsPGControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsPGControlStatus.setStatus("mandatory")
_RaidExMibCVSCUInfTable_Object = MibTable
raidExMibCVSCUInfTable = _RaidExMibCVSCUInfTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 7)
)
if mibBuilder.loadTexts:
    raidExMibCVSCUInfTable.setStatus("mandatory")
_RaidExMibCVSCUInfEntry_Object = MibTableRow
raidExMibCVSCUInfEntry = _RaidExMibCVSCUInfEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 7, 1)
)
raidExMibCVSCUInfEntry.setIndexNames(
    (0, "HDS9900MIB", "cvsCUInfSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCVSCUInfEntry.setStatus("mandatory")
_CvsCUInfSerialNumber_Type = Integer32
_CvsCUInfSerialNumber_Object = MibTableColumn
cvsCUInfSerialNumber = _CvsCUInfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 7, 1, 1),
    _CvsCUInfSerialNumber_Type()
)
cvsCUInfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsCUInfSerialNumber.setStatus("mandatory")
_CvsCUInfFreeCUNum_Type = Integer32
_CvsCUInfFreeCUNum_Object = MibTableColumn
cvsCUInfFreeCUNum = _CvsCUInfFreeCUNum_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 13, 7, 1, 2),
    _CvsCUInfFreeCUNum_Type()
)
cvsCUInfFreeCUNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsCUInfFreeCUNum.setStatus("mandatory")
_RaidExMibSubsystemInfo_ObjectIdentity = ObjectIdentity
raidExMibSubsystemInfo = _RaidExMibSubsystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14)
)
_RaidExMibSubsystemIDTable_Object = MibTable
raidExMibSubsystemIDTable = _RaidExMibSubsystemIDTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    raidExMibSubsystemIDTable.setStatus("mandatory")
_RaidExMibSubsystemIDEntry_Object = MibTableRow
raidExMibSubsystemIDEntry = _RaidExMibSubsystemIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1, 1)
)
raidExMibSubsystemIDEntry.setIndexNames(
    (0, "HDS9900MIB", "subsystemIDSerialNumber"),
    (0, "HDS9900MIB", "subsystemIDCU"),
    (0, "HDS9900MIB", "subsystemIDStartLDEV"),
)
if mibBuilder.loadTexts:
    raidExMibSubsystemIDEntry.setStatus("mandatory")
_SubsystemIDSerialNumber_Type = Integer32
_SubsystemIDSerialNumber_Object = MibTableColumn
subsystemIDSerialNumber = _SubsystemIDSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1, 1, 1),
    _SubsystemIDSerialNumber_Type()
)
subsystemIDSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subsystemIDSerialNumber.setStatus("mandatory")
_SubsystemIDCU_Type = Integer32
_SubsystemIDCU_Object = MibTableColumn
subsystemIDCU = _SubsystemIDCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1, 1, 2),
    _SubsystemIDCU_Type()
)
subsystemIDCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subsystemIDCU.setStatus("mandatory")
_SubsystemIDStartLDEV_Type = Integer32
_SubsystemIDStartLDEV_Object = MibTableColumn
subsystemIDStartLDEV = _SubsystemIDStartLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1, 1, 3),
    _SubsystemIDStartLDEV_Type()
)
subsystemIDStartLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subsystemIDStartLDEV.setStatus("mandatory")
_SubsystemIDEndLDEV_Type = Integer32
_SubsystemIDEndLDEV_Object = MibTableColumn
subsystemIDEndLDEV = _SubsystemIDEndLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1, 1, 4),
    _SubsystemIDEndLDEV_Type()
)
subsystemIDEndLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subsystemIDEndLDEV.setStatus("mandatory")
_SubsystemIDSSID_Type = Integer32
_SubsystemIDSSID_Object = MibTableColumn
subsystemIDSSID = _SubsystemIDSSID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1, 1, 5),
    _SubsystemIDSSID_Type()
)
subsystemIDSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subsystemIDSSID.setStatus("mandatory")
_SubsystemIDControlStatus_Type = Integer32
_SubsystemIDControlStatus_Object = MibTableColumn
subsystemIDControlStatus = _SubsystemIDControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 1, 1, 6),
    _SubsystemIDControlStatus_Type()
)
subsystemIDControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subsystemIDControlStatus.setStatus("mandatory")
_RaidExMibSSIDBoundaryTable_Object = MibTable
raidExMibSSIDBoundaryTable = _RaidExMibSSIDBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    raidExMibSSIDBoundaryTable.setStatus("mandatory")
_RaidExMibSSIDBoundaryEntry_Object = MibTableRow
raidExMibSSIDBoundaryEntry = _RaidExMibSSIDBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 2, 1)
)
raidExMibSSIDBoundaryEntry.setIndexNames(
    (0, "HDS9900MIB", "ssidBoundarySerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibSSIDBoundaryEntry.setStatus("mandatory")
_SsidBoundarySerialNumber_Type = Integer32
_SsidBoundarySerialNumber_Object = MibTableColumn
ssidBoundarySerialNumber = _SsidBoundarySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 2, 1, 1),
    _SsidBoundarySerialNumber_Type()
)
ssidBoundarySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssidBoundarySerialNumber.setStatus("mandatory")
_SsidBoundaryBoundary_Type = Integer32
_SsidBoundaryBoundary_Object = MibTableColumn
ssidBoundaryBoundary = _SsidBoundaryBoundary_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 14, 2, 1, 2),
    _SsidBoundaryBoundary_Type()
)
ssidBoundaryBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssidBoundaryBoundary.setStatus("mandatory")
_RaidExMibEnvironmentInfo_ObjectIdentity = ObjectIdentity
raidExMibEnvironmentInfo = _RaidExMibEnvironmentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 15)
)
_RaidExMibTimeZoneDataTable_Object = MibTable
raidExMibTimeZoneDataTable = _RaidExMibTimeZoneDataTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    raidExMibTimeZoneDataTable.setStatus("mandatory")
_RaidExMibTimeZoneDataEntry_Object = MibTableRow
raidExMibTimeZoneDataEntry = _RaidExMibTimeZoneDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 15, 1, 1)
)
raidExMibTimeZoneDataEntry.setIndexNames(
    (0, "HDS9900MIB", "timeZoneSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibTimeZoneDataEntry.setStatus("mandatory")
_TimeZoneSerialNumber_Type = Integer32
_TimeZoneSerialNumber_Object = MibTableColumn
timeZoneSerialNumber = _TimeZoneSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 15, 1, 1, 1),
    _TimeZoneSerialNumber_Type()
)
timeZoneSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeZoneSerialNumber.setStatus("mandatory")
_TimeZoneID_Type = DisplayString
_TimeZoneID_Object = MibTableColumn
timeZoneID = _TimeZoneID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 15, 1, 1, 2),
    _TimeZoneID_Type()
)
timeZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeZoneID.setStatus("mandatory")
_RaidExMibChannelAdapter_ObjectIdentity = ObjectIdentity
raidExMibChannelAdapter = _RaidExMibChannelAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16)
)
_RaidExMibCHAConfigurationTable_Object = MibTable
raidExMibCHAConfigurationTable = _RaidExMibCHAConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    raidExMibCHAConfigurationTable.setStatus("mandatory")
_RaidExMibCHAConfigurationEntry_Object = MibTableRow
raidExMibCHAConfigurationEntry = _RaidExMibCHAConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1)
)
raidExMibCHAConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "chaSerialNumber"),
    (0, "HDS9900MIB", "chaClusterNumber"),
    (0, "HDS9900MIB", "chaNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCHAConfigurationEntry.setStatus("mandatory")
_ChaSerialNumber_Type = Integer32
_ChaSerialNumber_Object = MibTableColumn
chaSerialNumber = _ChaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1, 1),
    _ChaSerialNumber_Type()
)
chaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chaSerialNumber.setStatus("mandatory")
_ChaClusterNumber_Type = Integer32
_ChaClusterNumber_Object = MibTableColumn
chaClusterNumber = _ChaClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1, 2),
    _ChaClusterNumber_Type()
)
chaClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chaClusterNumber.setStatus("mandatory")
_ChaNumber_Type = Integer32
_ChaNumber_Object = MibTableColumn
chaNumber = _ChaNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1, 3),
    _ChaNumber_Type()
)
chaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chaNumber.setStatus("mandatory")
_ChaDisplayName_Type = DisplayString
_ChaDisplayName_Object = MibTableColumn
chaDisplayName = _ChaDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1, 4),
    _ChaDisplayName_Type()
)
chaDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chaDisplayName.setStatus("mandatory")
_ChaPackageType_Type = Integer32
_ChaPackageType_Object = MibTableColumn
chaPackageType = _ChaPackageType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1, 5),
    _ChaPackageType_Type()
)
chaPackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chaPackageType.setStatus("mandatory")
_ChaMode_Type = Integer32
_ChaMode_Object = MibTableColumn
chaMode = _ChaMode_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1, 6),
    _ChaMode_Type()
)
chaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chaMode.setStatus("mandatory")
_ChaControlStatus_Type = Integer32
_ChaControlStatus_Object = MibTableColumn
chaControlStatus = _ChaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 1, 1, 7),
    _ChaControlStatus_Type()
)
chaControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chaControlStatus.setStatus("mandatory")
_RaidExMibCHPConfigurationTable_Object = MibTable
raidExMibCHPConfigurationTable = _RaidExMibCHPConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 2)
)
if mibBuilder.loadTexts:
    raidExMibCHPConfigurationTable.setStatus("mandatory")
_RaidExMibCHPConfigurationEntry_Object = MibTableRow
raidExMibCHPConfigurationEntry = _RaidExMibCHPConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 2, 1)
)
raidExMibCHPConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "chpSerialNumber"),
    (0, "HDS9900MIB", "chpClusterNumber"),
    (0, "HDS9900MIB", "chpCHANumber"),
    (0, "HDS9900MIB", "chpNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCHPConfigurationEntry.setStatus("mandatory")
_ChpSerialNumber_Type = Integer32
_ChpSerialNumber_Object = MibTableColumn
chpSerialNumber = _ChpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 2, 1, 1),
    _ChpSerialNumber_Type()
)
chpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chpSerialNumber.setStatus("mandatory")
_ChpClusterNumber_Type = Integer32
_ChpClusterNumber_Object = MibTableColumn
chpClusterNumber = _ChpClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 2, 1, 2),
    _ChpClusterNumber_Type()
)
chpClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chpClusterNumber.setStatus("mandatory")
_ChpCHANumber_Type = Integer32
_ChpCHANumber_Object = MibTableColumn
chpCHANumber = _ChpCHANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 2, 1, 3),
    _ChpCHANumber_Type()
)
chpCHANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chpCHANumber.setStatus("mandatory")
_ChpNumber_Type = Integer32
_ChpNumber_Object = MibTableColumn
chpNumber = _ChpNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 2, 1, 4),
    _ChpNumber_Type()
)
chpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chpNumber.setStatus("mandatory")
_ChpDisplayName_Type = DisplayString
_ChpDisplayName_Object = MibTableColumn
chpDisplayName = _ChpDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 16, 2, 1, 5),
    _ChpDisplayName_Type()
)
chpDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chpDisplayName.setStatus("mandatory")
_RaidExMibDiskAdapter_ObjectIdentity = ObjectIdentity
raidExMibDiskAdapter = _RaidExMibDiskAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17)
)
_RaidExMibDKAConfigurationTable_Object = MibTable
raidExMibDKAConfigurationTable = _RaidExMibDKAConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    raidExMibDKAConfigurationTable.setStatus("mandatory")
_RaidExMibDKAConfigurationEntry_Object = MibTableRow
raidExMibDKAConfigurationEntry = _RaidExMibDKAConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 1, 1)
)
raidExMibDKAConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "dkaSerialNumber"),
    (0, "HDS9900MIB", "dkaClusterNumber"),
    (0, "HDS9900MIB", "dkaNumber"),
)
if mibBuilder.loadTexts:
    raidExMibDKAConfigurationEntry.setStatus("mandatory")
_DkaSerialNumber_Type = Integer32
_DkaSerialNumber_Object = MibTableColumn
dkaSerialNumber = _DkaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 1, 1, 1),
    _DkaSerialNumber_Type()
)
dkaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkaSerialNumber.setStatus("mandatory")
_DkaClusterNumber_Type = Integer32
_DkaClusterNumber_Object = MibTableColumn
dkaClusterNumber = _DkaClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 1, 1, 2),
    _DkaClusterNumber_Type()
)
dkaClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkaClusterNumber.setStatus("mandatory")
_DkaNumber_Type = Integer32
_DkaNumber_Object = MibTableColumn
dkaNumber = _DkaNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 1, 1, 3),
    _DkaNumber_Type()
)
dkaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkaNumber.setStatus("mandatory")
_DkaDisplayName_Type = DisplayString
_DkaDisplayName_Object = MibTableColumn
dkaDisplayName = _DkaDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 1, 1, 4),
    _DkaDisplayName_Type()
)
dkaDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkaDisplayName.setStatus("mandatory")
_RaidExMibDKPConfigurationTable_Object = MibTable
raidExMibDKPConfigurationTable = _RaidExMibDKPConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 2)
)
if mibBuilder.loadTexts:
    raidExMibDKPConfigurationTable.setStatus("mandatory")
_RaidExMibDKPConfigurationEntry_Object = MibTableRow
raidExMibDKPConfigurationEntry = _RaidExMibDKPConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 2, 1)
)
raidExMibDKPConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "dkpSerialNumber"),
    (0, "HDS9900MIB", "dkpClusterNumber"),
    (0, "HDS9900MIB", "dkpDKANumber"),
    (0, "HDS9900MIB", "dkpNumber"),
)
if mibBuilder.loadTexts:
    raidExMibDKPConfigurationEntry.setStatus("mandatory")
_DkpSerialNumber_Type = Integer32
_DkpSerialNumber_Object = MibTableColumn
dkpSerialNumber = _DkpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 2, 1, 1),
    _DkpSerialNumber_Type()
)
dkpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkpSerialNumber.setStatus("mandatory")
_DkpClusterNumber_Type = Integer32
_DkpClusterNumber_Object = MibTableColumn
dkpClusterNumber = _DkpClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 2, 1, 2),
    _DkpClusterNumber_Type()
)
dkpClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkpClusterNumber.setStatus("mandatory")
_DkpDKANumber_Type = Integer32
_DkpDKANumber_Object = MibTableColumn
dkpDKANumber = _DkpDKANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 2, 1, 3),
    _DkpDKANumber_Type()
)
dkpDKANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkpDKANumber.setStatus("mandatory")
_DkpNumber_Type = Integer32
_DkpNumber_Object = MibTableColumn
dkpNumber = _DkpNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 2, 1, 4),
    _DkpNumber_Type()
)
dkpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkpNumber.setStatus("mandatory")
_DkpDisplayName_Type = DisplayString
_DkpDisplayName_Object = MibTableColumn
dkpDisplayName = _DkpDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 2, 1, 5),
    _DkpDisplayName_Type()
)
dkpDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkpDisplayName.setStatus("mandatory")
_RaidExMibDRRConfigurationTable_Object = MibTable
raidExMibDRRConfigurationTable = _RaidExMibDRRConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 3)
)
if mibBuilder.loadTexts:
    raidExMibDRRConfigurationTable.setStatus("mandatory")
_RaidExMibDRRConfigurationEntry_Object = MibTableRow
raidExMibDRRConfigurationEntry = _RaidExMibDRRConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 3, 1)
)
raidExMibDRRConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "drrSerialNumber"),
    (0, "HDS9900MIB", "drrClusterNumber"),
    (0, "HDS9900MIB", "drrDKANumber"),
    (0, "HDS9900MIB", "drrNumber"),
)
if mibBuilder.loadTexts:
    raidExMibDRRConfigurationEntry.setStatus("mandatory")
_DrrSerialNumber_Type = Integer32
_DrrSerialNumber_Object = MibTableColumn
drrSerialNumber = _DrrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 3, 1, 1),
    _DrrSerialNumber_Type()
)
drrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrSerialNumber.setStatus("mandatory")
_DrrClusterNumber_Type = Integer32
_DrrClusterNumber_Object = MibTableColumn
drrClusterNumber = _DrrClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 3, 1, 2),
    _DrrClusterNumber_Type()
)
drrClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrClusterNumber.setStatus("mandatory")
_DrrDKANumber_Type = Integer32
_DrrDKANumber_Object = MibTableColumn
drrDKANumber = _DrrDKANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 3, 1, 3),
    _DrrDKANumber_Type()
)
drrDKANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrDKANumber.setStatus("mandatory")
_DrrNumber_Type = Integer32
_DrrNumber_Object = MibTableColumn
drrNumber = _DrrNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 3, 1, 4),
    _DrrNumber_Type()
)
drrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrNumber.setStatus("mandatory")
_DrrDisplayName_Type = DisplayString
_DrrDisplayName_Object = MibTableColumn
drrDisplayName = _DrrDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 17, 3, 1, 5),
    _DrrDisplayName_Type()
)
drrDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrDisplayName.setStatus("mandatory")
_RaidExMibParityGroup_ObjectIdentity = ObjectIdentity
raidExMibParityGroup = _RaidExMibParityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18)
)
_RaidExMibParityGroupListTable_Object = MibTable
raidExMibParityGroupListTable = _RaidExMibParityGroupListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    raidExMibParityGroupListTable.setStatus("mandatory")
_RaidExMibParityGroupListEntry_Object = MibTableRow
raidExMibParityGroupListEntry = _RaidExMibParityGroupListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1)
)
raidExMibParityGroupListEntry.setIndexNames(
    (0, "HDS9900MIB", "pgSerialNumber"),
    (0, "HDS9900MIB", "pgFB4Number"),
    (0, "HDS9900MIB", "pgNumber"),
)
if mibBuilder.loadTexts:
    raidExMibParityGroupListEntry.setStatus("mandatory")
_PgSerialNumber_Type = Integer32
_PgSerialNumber_Object = MibTableColumn
pgSerialNumber = _PgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 1),
    _PgSerialNumber_Type()
)
pgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgSerialNumber.setStatus("mandatory")
_PgFB4Number_Type = Integer32
_PgFB4Number_Object = MibTableColumn
pgFB4Number = _PgFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 2),
    _PgFB4Number_Type()
)
pgFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgFB4Number.setStatus("mandatory")
_PgNumber_Type = Integer32
_PgNumber_Object = MibTableColumn
pgNumber = _PgNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 3),
    _PgNumber_Type()
)
pgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgNumber.setStatus("mandatory")
_PgDisplayName_Type = DisplayString
_PgDisplayName_Object = MibTableColumn
pgDisplayName = _PgDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 4),
    _PgDisplayName_Type()
)
pgDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDisplayName.setStatus("mandatory")
_PgRAIDType_Type = DisplayString
_PgRAIDType_Object = MibTableColumn
pgRAIDType = _PgRAIDType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 5),
    _PgRAIDType_Type()
)
pgRAIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRAIDType.setStatus("mandatory")
_PgDriveType_Type = DisplayString
_PgDriveType_Object = MibTableColumn
pgDriveType = _PgDriveType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 6),
    _PgDriveType_Type()
)
pgDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgDriveType.setStatus("mandatory")
_PgHIHSMFixed_Type = Integer32
_PgHIHSMFixed_Object = MibTableColumn
pgHIHSMFixed = _PgHIHSMFixed_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 7),
    _PgHIHSMFixed_Type()
)
pgHIHSMFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgHIHSMFixed.setStatus("mandatory")
_PgControlStatus_Type = Integer32
_PgControlStatus_Object = MibTableColumn
pgControlStatus = _PgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 1, 1, 8),
    _PgControlStatus_Type()
)
pgControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgControlStatus.setStatus("mandatory")
_RaidExMibParityGroupLDEVTable_Object = MibTable
raidExMibParityGroupLDEVTable = _RaidExMibParityGroupLDEVTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2)
)
if mibBuilder.loadTexts:
    raidExMibParityGroupLDEVTable.setStatus("mandatory")
_RaidExMibParityGroupLDEVEntry_Object = MibTableRow
raidExMibParityGroupLDEVEntry = _RaidExMibParityGroupLDEVEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2, 1)
)
raidExMibParityGroupLDEVEntry.setIndexNames(
    (0, "HDS9900MIB", "pgLDEVSerialNumber"),
    (0, "HDS9900MIB", "pgLDEVFB4Number"),
    (0, "HDS9900MIB", "pgLDEVPGNumber"),
    (0, "HDS9900MIB", "pgLDEVControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibParityGroupLDEVEntry.setStatus("mandatory")
_PgLDEVSerialNumber_Type = Integer32
_PgLDEVSerialNumber_Object = MibTableColumn
pgLDEVSerialNumber = _PgLDEVSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2, 1, 1),
    _PgLDEVSerialNumber_Type()
)
pgLDEVSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLDEVSerialNumber.setStatus("mandatory")
_PgLDEVFB4Number_Type = Integer32
_PgLDEVFB4Number_Object = MibTableColumn
pgLDEVFB4Number = _PgLDEVFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2, 1, 2),
    _PgLDEVFB4Number_Type()
)
pgLDEVFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLDEVFB4Number.setStatus("mandatory")
_PgLDEVPGNumber_Type = Integer32
_PgLDEVPGNumber_Object = MibTableColumn
pgLDEVPGNumber = _PgLDEVPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2, 1, 3),
    _PgLDEVPGNumber_Type()
)
pgLDEVPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLDEVPGNumber.setStatus("mandatory")
_PgLDEVControlIndex_Type = Integer32
_PgLDEVControlIndex_Object = MibTableColumn
pgLDEVControlIndex = _PgLDEVControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2, 1, 4),
    _PgLDEVControlIndex_Type()
)
pgLDEVControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLDEVControlIndex.setStatus("mandatory")
_PgLDEVCU_Type = Integer32
_PgLDEVCU_Object = MibTableColumn
pgLDEVCU = _PgLDEVCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2, 1, 5),
    _PgLDEVCU_Type()
)
pgLDEVCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLDEVCU.setStatus("mandatory")
_PgLDEVLDEV_Type = Integer32
_PgLDEVLDEV_Object = MibTableColumn
pgLDEVLDEV = _PgLDEVLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 18, 2, 1, 6),
    _PgLDEVLDEV_Type()
)
pgLDEVLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLDEVLDEV.setStatus("mandatory")
_RaidExMibHIHSM_ObjectIdentity = ObjectIdentity
raidExMibHIHSM = _RaidExMibHIHSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20)
)
_HihsmMonitoringParameterTable_Object = MibTable
hihsmMonitoringParameterTable = _HihsmMonitoringParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    hihsmMonitoringParameterTable.setStatus("mandatory")
_HihsmMonitoringParameterEntry_Object = MibTableRow
hihsmMonitoringParameterEntry = _HihsmMonitoringParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1)
)
hihsmMonitoringParameterEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmMonParamSerialNumber"),
)
if mibBuilder.loadTexts:
    hihsmMonitoringParameterEntry.setStatus("mandatory")
_HihsmMonParamSerialNumber_Type = Integer32
_HihsmMonParamSerialNumber_Object = MibTableColumn
hihsmMonParamSerialNumber = _HihsmMonParamSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 1),
    _HihsmMonParamSerialNumber_Type()
)
hihsmMonParamSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmMonParamSerialNumber.setStatus("mandatory")
_HihsmMonParamFunctionSwitch_Type = Integer32
_HihsmMonParamFunctionSwitch_Object = MibTableColumn
hihsmMonParamFunctionSwitch = _HihsmMonParamFunctionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 2),
    _HihsmMonParamFunctionSwitch_Type()
)
hihsmMonParamFunctionSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmMonParamFunctionSwitch.setStatus("mandatory")
_HihsmMonParamGatheringTime_Type = DisplayString
_HihsmMonParamGatheringTime_Object = MibTableColumn
hihsmMonParamGatheringTime = _HihsmMonParamGatheringTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 3),
    _HihsmMonParamGatheringTime_Type()
)
hihsmMonParamGatheringTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmMonParamGatheringTime.setStatus("mandatory")
_HihsmMonParamGatheredFromDate_Type = DisplayString
_HihsmMonParamGatheredFromDate_Object = MibTableColumn
hihsmMonParamGatheredFromDate = _HihsmMonParamGatheredFromDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 4),
    _HihsmMonParamGatheredFromDate_Type()
)
hihsmMonParamGatheredFromDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmMonParamGatheredFromDate.setStatus("mandatory")
_HihsmMonParamGatheredFromTime_Type = DisplayString
_HihsmMonParamGatheredFromTime_Object = MibTableColumn
hihsmMonParamGatheredFromTime = _HihsmMonParamGatheredFromTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 5),
    _HihsmMonParamGatheredFromTime_Type()
)
hihsmMonParamGatheredFromTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmMonParamGatheredFromTime.setStatus("mandatory")
_HihsmMonParamGatheredToDate_Type = DisplayString
_HihsmMonParamGatheredToDate_Object = MibTableColumn
hihsmMonParamGatheredToDate = _HihsmMonParamGatheredToDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 6),
    _HihsmMonParamGatheredToDate_Type()
)
hihsmMonParamGatheredToDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmMonParamGatheredToDate.setStatus("mandatory")
_HihsmMonParamGatheredToTime_Type = DisplayString
_HihsmMonParamGatheredToTime_Object = MibTableColumn
hihsmMonParamGatheredToTime = _HihsmMonParamGatheredToTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 7),
    _HihsmMonParamGatheredToTime_Type()
)
hihsmMonParamGatheredToTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmMonParamGatheredToTime.setStatus("mandatory")
_HihsmMonParamControlStatus_Type = Integer32
_HihsmMonParamControlStatus_Object = MibTableColumn
hihsmMonParamControlStatus = _HihsmMonParamControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 1, 1, 8),
    _HihsmMonParamControlStatus_Type()
)
hihsmMonParamControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmMonParamControlStatus.setStatus("mandatory")
_HihsmCalculationParameterTable_Object = MibTable
hihsmCalculationParameterTable = _HihsmCalculationParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    hihsmCalculationParameterTable.setStatus("mandatory")
_HihsmCalculationParameterEntry_Object = MibTableRow
hihsmCalculationParameterEntry = _HihsmCalculationParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1)
)
hihsmCalculationParameterEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmCalcParamSerialNumber"),
)
if mibBuilder.loadTexts:
    hihsmCalculationParameterEntry.setStatus("mandatory")
_HihsmCalcParamSerialNumber_Type = Integer32
_HihsmCalcParamSerialNumber_Object = MibTableColumn
hihsmCalcParamSerialNumber = _HihsmCalcParamSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 1),
    _HihsmCalcParamSerialNumber_Type()
)
hihsmCalcParamSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCalcParamSerialNumber.setStatus("mandatory")
_HihsmCalcParamCalcType_Type = Integer32
_HihsmCalcParamCalcType_Object = MibTableColumn
hihsmCalcParamCalcType = _HihsmCalcParamCalcType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 2),
    _HihsmCalcParamCalcType_Type()
)
hihsmCalcParamCalcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmCalcParamCalcType.setStatus("mandatory")
_HihsmCalcParamFromDate_Type = DisplayString
_HihsmCalcParamFromDate_Object = MibTableColumn
hihsmCalcParamFromDate = _HihsmCalcParamFromDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 3),
    _HihsmCalcParamFromDate_Type()
)
hihsmCalcParamFromDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmCalcParamFromDate.setStatus("mandatory")
_HihsmCalcParamFromTime_Type = DisplayString
_HihsmCalcParamFromTime_Object = MibTableColumn
hihsmCalcParamFromTime = _HihsmCalcParamFromTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 4),
    _HihsmCalcParamFromTime_Type()
)
hihsmCalcParamFromTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmCalcParamFromTime.setStatus("mandatory")
_HihsmCalcParamToDate_Type = DisplayString
_HihsmCalcParamToDate_Object = MibTableColumn
hihsmCalcParamToDate = _HihsmCalcParamToDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 5),
    _HihsmCalcParamToDate_Type()
)
hihsmCalcParamToDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmCalcParamToDate.setStatus("mandatory")
_HihsmCalcParamToTime_Type = DisplayString
_HihsmCalcParamToTime_Object = MibTableColumn
hihsmCalcParamToTime = _HihsmCalcParamToTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 6),
    _HihsmCalcParamToTime_Type()
)
hihsmCalcParamToTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmCalcParamToTime.setStatus("mandatory")
_HihsmCalcParamDataType_Type = Integer32
_HihsmCalcParamDataType_Object = MibTableColumn
hihsmCalcParamDataType = _HihsmCalcParamDataType_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 7),
    _HihsmCalcParamDataType_Type()
)
hihsmCalcParamDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmCalcParamDataType.setStatus("mandatory")
_HihsmCalcParamControlStatus_Type = Integer32
_HihsmCalcParamControlStatus_Object = MibTableColumn
hihsmCalcParamControlStatus = _HihsmCalcParamControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 2, 1, 8),
    _HihsmCalcParamControlStatus_Type()
)
hihsmCalcParamControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmCalcParamControlStatus.setStatus("mandatory")
_HihsmCalculatedData_ObjectIdentity = ObjectIdentity
hihsmCalculatedData = _HihsmCalculatedData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3)
)
_HihsmCHPUtilizationTable_Object = MibTable
hihsmCHPUtilizationTable = _HihsmCHPUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 1)
)
if mibBuilder.loadTexts:
    hihsmCHPUtilizationTable.setStatus("mandatory")
_HihsmCHPUtilizationEntry_Object = MibTableRow
hihsmCHPUtilizationEntry = _HihsmCHPUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 1, 1)
)
hihsmCHPUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmCHPUtilSerialNumber"),
    (0, "HDS9900MIB", "hihsmCHPUtilClusterNumber"),
    (0, "HDS9900MIB", "hihsmCHPUtilCHANumber"),
    (0, "HDS9900MIB", "hihsmCHPUtilCHPNumber"),
)
if mibBuilder.loadTexts:
    hihsmCHPUtilizationEntry.setStatus("mandatory")
_HihsmCHPUtilSerialNumber_Type = Integer32
_HihsmCHPUtilSerialNumber_Object = MibTableColumn
hihsmCHPUtilSerialNumber = _HihsmCHPUtilSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 1, 1, 1),
    _HihsmCHPUtilSerialNumber_Type()
)
hihsmCHPUtilSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHPUtilSerialNumber.setStatus("mandatory")
_HihsmCHPUtilClusterNumber_Type = Integer32
_HihsmCHPUtilClusterNumber_Object = MibTableColumn
hihsmCHPUtilClusterNumber = _HihsmCHPUtilClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 1, 1, 2),
    _HihsmCHPUtilClusterNumber_Type()
)
hihsmCHPUtilClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHPUtilClusterNumber.setStatus("mandatory")
_HihsmCHPUtilCHANumber_Type = Integer32
_HihsmCHPUtilCHANumber_Object = MibTableColumn
hihsmCHPUtilCHANumber = _HihsmCHPUtilCHANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 1, 1, 3),
    _HihsmCHPUtilCHANumber_Type()
)
hihsmCHPUtilCHANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHPUtilCHANumber.setStatus("mandatory")
_HihsmCHPUtilCHPNumber_Type = Integer32
_HihsmCHPUtilCHPNumber_Object = MibTableColumn
hihsmCHPUtilCHPNumber = _HihsmCHPUtilCHPNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 1, 1, 4),
    _HihsmCHPUtilCHPNumber_Type()
)
hihsmCHPUtilCHPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHPUtilCHPNumber.setStatus("mandatory")
_HihsmCHPUtilData_Type = DisplayString
_HihsmCHPUtilData_Object = MibTableColumn
hihsmCHPUtilData = _HihsmCHPUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 1, 1, 5),
    _HihsmCHPUtilData_Type()
)
hihsmCHPUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHPUtilData.setStatus("mandatory")
_HihsmDKPUtilizationTable_Object = MibTable
hihsmDKPUtilizationTable = _HihsmDKPUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 2)
)
if mibBuilder.loadTexts:
    hihsmDKPUtilizationTable.setStatus("mandatory")
_HihsmDKPUtilizationEntry_Object = MibTableRow
hihsmDKPUtilizationEntry = _HihsmDKPUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 2, 1)
)
hihsmDKPUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmDKPUtilSerialNumber"),
    (0, "HDS9900MIB", "hihsmDKPUtilClusterNumber"),
    (0, "HDS9900MIB", "hihsmDKPUtilDKANumber"),
    (0, "HDS9900MIB", "hihsmDKPUtilDKPNumber"),
)
if mibBuilder.loadTexts:
    hihsmDKPUtilizationEntry.setStatus("mandatory")
_HihsmDKPUtilSerialNumber_Type = Integer32
_HihsmDKPUtilSerialNumber_Object = MibTableColumn
hihsmDKPUtilSerialNumber = _HihsmDKPUtilSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 2, 1, 1),
    _HihsmDKPUtilSerialNumber_Type()
)
hihsmDKPUtilSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKPUtilSerialNumber.setStatus("mandatory")
_HihsmDKPUtilClusterNumber_Type = Integer32
_HihsmDKPUtilClusterNumber_Object = MibTableColumn
hihsmDKPUtilClusterNumber = _HihsmDKPUtilClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 2, 1, 2),
    _HihsmDKPUtilClusterNumber_Type()
)
hihsmDKPUtilClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKPUtilClusterNumber.setStatus("mandatory")
_HihsmDKPUtilDKANumber_Type = Integer32
_HihsmDKPUtilDKANumber_Object = MibTableColumn
hihsmDKPUtilDKANumber = _HihsmDKPUtilDKANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 2, 1, 3),
    _HihsmDKPUtilDKANumber_Type()
)
hihsmDKPUtilDKANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKPUtilDKANumber.setStatus("mandatory")
_HihsmDKPUtilDKPNumber_Type = Integer32
_HihsmDKPUtilDKPNumber_Object = MibTableColumn
hihsmDKPUtilDKPNumber = _HihsmDKPUtilDKPNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 2, 1, 4),
    _HihsmDKPUtilDKPNumber_Type()
)
hihsmDKPUtilDKPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKPUtilDKPNumber.setStatus("mandatory")
_HihsmDKPUtilData_Type = DisplayString
_HihsmDKPUtilData_Object = MibTableColumn
hihsmDKPUtilData = _HihsmDKPUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 2, 1, 5),
    _HihsmDKPUtilData_Type()
)
hihsmDKPUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKPUtilData.setStatus("mandatory")
_HihsmDRRUtilizationTable_Object = MibTable
hihsmDRRUtilizationTable = _HihsmDRRUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 3)
)
if mibBuilder.loadTexts:
    hihsmDRRUtilizationTable.setStatus("mandatory")
_HihsmDRRUtilizationEntry_Object = MibTableRow
hihsmDRRUtilizationEntry = _HihsmDRRUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 3, 1)
)
hihsmDRRUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmDRRUtilSerialNumber"),
    (0, "HDS9900MIB", "hihsmDRRUtilClusterNumber"),
    (0, "HDS9900MIB", "hihsmDRRUtilDKANumber"),
    (0, "HDS9900MIB", "hihsmDRRUtilDRRNumber"),
)
if mibBuilder.loadTexts:
    hihsmDRRUtilizationEntry.setStatus("mandatory")
_HihsmDRRUtilSerialNumber_Type = Integer32
_HihsmDRRUtilSerialNumber_Object = MibTableColumn
hihsmDRRUtilSerialNumber = _HihsmDRRUtilSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 3, 1, 1),
    _HihsmDRRUtilSerialNumber_Type()
)
hihsmDRRUtilSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDRRUtilSerialNumber.setStatus("mandatory")
_HihsmDRRUtilClusterNumber_Type = Integer32
_HihsmDRRUtilClusterNumber_Object = MibTableColumn
hihsmDRRUtilClusterNumber = _HihsmDRRUtilClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 3, 1, 2),
    _HihsmDRRUtilClusterNumber_Type()
)
hihsmDRRUtilClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDRRUtilClusterNumber.setStatus("mandatory")
_HihsmDRRUtilDKANumber_Type = Integer32
_HihsmDRRUtilDKANumber_Object = MibTableColumn
hihsmDRRUtilDKANumber = _HihsmDRRUtilDKANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 3, 1, 3),
    _HihsmDRRUtilDKANumber_Type()
)
hihsmDRRUtilDKANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDRRUtilDKANumber.setStatus("mandatory")
_HihsmDRRUtilDRRNumber_Type = Integer32
_HihsmDRRUtilDRRNumber_Object = MibTableColumn
hihsmDRRUtilDRRNumber = _HihsmDRRUtilDRRNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 3, 1, 4),
    _HihsmDRRUtilDRRNumber_Type()
)
hihsmDRRUtilDRRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDRRUtilDRRNumber.setStatus("mandatory")
_HihsmDRRUtilData_Type = DisplayString
_HihsmDRRUtilData_Object = MibTableColumn
hihsmDRRUtilData = _HihsmDRRUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 3, 1, 5),
    _HihsmDRRUtilData_Type()
)
hihsmDRRUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDRRUtilData.setStatus("mandatory")
_HihsmPGUtilizationTable_Object = MibTable
hihsmPGUtilizationTable = _HihsmPGUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 4)
)
if mibBuilder.loadTexts:
    hihsmPGUtilizationTable.setStatus("mandatory")
_HihsmPGUtilizationEntry_Object = MibTableRow
hihsmPGUtilizationEntry = _HihsmPGUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 4, 1)
)
hihsmPGUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmPGUtilSerialNumber"),
    (0, "HDS9900MIB", "hihsmPGUtilFB4Number"),
    (0, "HDS9900MIB", "hihsmPGUtilPGNumber"),
)
if mibBuilder.loadTexts:
    hihsmPGUtilizationEntry.setStatus("mandatory")
_HihsmPGUtilSerialNumber_Type = Integer32
_HihsmPGUtilSerialNumber_Object = MibTableColumn
hihsmPGUtilSerialNumber = _HihsmPGUtilSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 4, 1, 1),
    _HihsmPGUtilSerialNumber_Type()
)
hihsmPGUtilSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPGUtilSerialNumber.setStatus("mandatory")
_HihsmPGUtilFB4Number_Type = Integer32
_HihsmPGUtilFB4Number_Object = MibTableColumn
hihsmPGUtilFB4Number = _HihsmPGUtilFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 4, 1, 2),
    _HihsmPGUtilFB4Number_Type()
)
hihsmPGUtilFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPGUtilFB4Number.setStatus("mandatory")
_HihsmPGUtilPGNumber_Type = Integer32
_HihsmPGUtilPGNumber_Object = MibTableColumn
hihsmPGUtilPGNumber = _HihsmPGUtilPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 4, 1, 3),
    _HihsmPGUtilPGNumber_Type()
)
hihsmPGUtilPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPGUtilPGNumber.setStatus("mandatory")
_HihsmPGUtilData_Type = DisplayString
_HihsmPGUtilData_Object = MibTableColumn
hihsmPGUtilData = _HihsmPGUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 4, 1, 4),
    _HihsmPGUtilData_Type()
)
hihsmPGUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPGUtilData.setStatus("mandatory")
_HihsmLDEVUtilizationTable_Object = MibTable
hihsmLDEVUtilizationTable = _HihsmLDEVUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5)
)
if mibBuilder.loadTexts:
    hihsmLDEVUtilizationTable.setStatus("mandatory")
_HihsmLDEVUtilizationEntry_Object = MibTableRow
hihsmLDEVUtilizationEntry = _HihsmLDEVUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5, 1)
)
hihsmLDEVUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmLDEVUtilSerialNumber"),
    (0, "HDS9900MIB", "hihsmLDEVUtilFB4Number"),
    (0, "HDS9900MIB", "hihsmLDEVUtilPGNumber"),
    (0, "HDS9900MIB", "hihsmLDEVUtilCU"),
    (0, "HDS9900MIB", "hihsmLDEVUtilLDEV"),
)
if mibBuilder.loadTexts:
    hihsmLDEVUtilizationEntry.setStatus("mandatory")
_HihsmLDEVUtilSerialNumber_Type = Integer32
_HihsmLDEVUtilSerialNumber_Object = MibTableColumn
hihsmLDEVUtilSerialNumber = _HihsmLDEVUtilSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5, 1, 1),
    _HihsmLDEVUtilSerialNumber_Type()
)
hihsmLDEVUtilSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmLDEVUtilSerialNumber.setStatus("mandatory")
_HihsmLDEVUtilFB4Number_Type = Integer32
_HihsmLDEVUtilFB4Number_Object = MibTableColumn
hihsmLDEVUtilFB4Number = _HihsmLDEVUtilFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5, 1, 2),
    _HihsmLDEVUtilFB4Number_Type()
)
hihsmLDEVUtilFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmLDEVUtilFB4Number.setStatus("mandatory")
_HihsmLDEVUtilPGNumber_Type = Integer32
_HihsmLDEVUtilPGNumber_Object = MibTableColumn
hihsmLDEVUtilPGNumber = _HihsmLDEVUtilPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5, 1, 3),
    _HihsmLDEVUtilPGNumber_Type()
)
hihsmLDEVUtilPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmLDEVUtilPGNumber.setStatus("mandatory")
_HihsmLDEVUtilCU_Type = Integer32
_HihsmLDEVUtilCU_Object = MibTableColumn
hihsmLDEVUtilCU = _HihsmLDEVUtilCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5, 1, 4),
    _HihsmLDEVUtilCU_Type()
)
hihsmLDEVUtilCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmLDEVUtilCU.setStatus("mandatory")
_HihsmLDEVUtilLDEV_Type = Integer32
_HihsmLDEVUtilLDEV_Object = MibTableColumn
hihsmLDEVUtilLDEV = _HihsmLDEVUtilLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5, 1, 5),
    _HihsmLDEVUtilLDEV_Type()
)
hihsmLDEVUtilLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmLDEVUtilLDEV.setStatus("mandatory")
_HihsmLDEVUtilData_Type = DisplayString
_HihsmLDEVUtilData_Object = MibTableColumn
hihsmLDEVUtilData = _HihsmLDEVUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 5, 1, 6),
    _HihsmLDEVUtilData_Type()
)
hihsmLDEVUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmLDEVUtilData.setStatus("mandatory")
_HihsmCHAtoCSWUtilizationTable_Object = MibTable
hihsmCHAtoCSWUtilizationTable = _HihsmCHAtoCSWUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6)
)
if mibBuilder.loadTexts:
    hihsmCHAtoCSWUtilizationTable.setStatus("mandatory")
_HihsmCHAtoCSWUtilizationEntry_Object = MibTableRow
hihsmCHAtoCSWUtilizationEntry = _HihsmCHAtoCSWUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6, 1)
)
hihsmCHAtoCSWUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmCHACSWSerialNumber"),
    (0, "HDS9900MIB", "hihsmCHACSWCHAClusterNumber"),
    (0, "HDS9900MIB", "hihsmCHACSWCHANumber"),
    (0, "HDS9900MIB", "hihsmCHACSWCSWClusterNumber"),
    (0, "HDS9900MIB", "hihsmCHACSWCSWNumber"),
)
if mibBuilder.loadTexts:
    hihsmCHAtoCSWUtilizationEntry.setStatus("mandatory")
_HihsmCHACSWSerialNumber_Type = Integer32
_HihsmCHACSWSerialNumber_Object = MibTableColumn
hihsmCHACSWSerialNumber = _HihsmCHACSWSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6, 1, 1),
    _HihsmCHACSWSerialNumber_Type()
)
hihsmCHACSWSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHACSWSerialNumber.setStatus("mandatory")
_HihsmCHACSWCHAClusterNumber_Type = Integer32
_HihsmCHACSWCHAClusterNumber_Object = MibTableColumn
hihsmCHACSWCHAClusterNumber = _HihsmCHACSWCHAClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6, 1, 2),
    _HihsmCHACSWCHAClusterNumber_Type()
)
hihsmCHACSWCHAClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHACSWCHAClusterNumber.setStatus("mandatory")
_HihsmCHACSWCHANumber_Type = Integer32
_HihsmCHACSWCHANumber_Object = MibTableColumn
hihsmCHACSWCHANumber = _HihsmCHACSWCHANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6, 1, 3),
    _HihsmCHACSWCHANumber_Type()
)
hihsmCHACSWCHANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHACSWCHANumber.setStatus("mandatory")
_HihsmCHACSWCSWClusterNumber_Type = Integer32
_HihsmCHACSWCSWClusterNumber_Object = MibTableColumn
hihsmCHACSWCSWClusterNumber = _HihsmCHACSWCSWClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6, 1, 4),
    _HihsmCHACSWCSWClusterNumber_Type()
)
hihsmCHACSWCSWClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHACSWCSWClusterNumber.setStatus("mandatory")
_HihsmCHACSWCSWNumber_Type = Integer32
_HihsmCHACSWCSWNumber_Object = MibTableColumn
hihsmCHACSWCSWNumber = _HihsmCHACSWCSWNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6, 1, 5),
    _HihsmCHACSWCSWNumber_Type()
)
hihsmCHACSWCSWNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHACSWCSWNumber.setStatus("mandatory")
_HihsmCHACSWUtilData_Type = DisplayString
_HihsmCHACSWUtilData_Object = MibTableColumn
hihsmCHACSWUtilData = _HihsmCHACSWUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 6, 1, 6),
    _HihsmCHACSWUtilData_Type()
)
hihsmCHACSWUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHACSWUtilData.setStatus("mandatory")
_HihsmDKAtoCSWUtilizationTable_Object = MibTable
hihsmDKAtoCSWUtilizationTable = _HihsmDKAtoCSWUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7)
)
if mibBuilder.loadTexts:
    hihsmDKAtoCSWUtilizationTable.setStatus("mandatory")
_HihsmDKAtoCSWUtilizationEntry_Object = MibTableRow
hihsmDKAtoCSWUtilizationEntry = _HihsmDKAtoCSWUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7, 1)
)
hihsmDKAtoCSWUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmDKACSWSerialNumber"),
    (0, "HDS9900MIB", "hihsmDKACSWDKAClusterNumber"),
    (0, "HDS9900MIB", "hihsmDKACSWDKANumber"),
    (0, "HDS9900MIB", "hihsmDKACSWCSWClusterNumber"),
    (0, "HDS9900MIB", "hihsmDKACSWCSWNumber"),
)
if mibBuilder.loadTexts:
    hihsmDKAtoCSWUtilizationEntry.setStatus("mandatory")
_HihsmDKACSWSerialNumber_Type = Integer32
_HihsmDKACSWSerialNumber_Object = MibTableColumn
hihsmDKACSWSerialNumber = _HihsmDKACSWSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7, 1, 1),
    _HihsmDKACSWSerialNumber_Type()
)
hihsmDKACSWSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKACSWSerialNumber.setStatus("mandatory")
_HihsmDKACSWDKAClusterNumber_Type = Integer32
_HihsmDKACSWDKAClusterNumber_Object = MibTableColumn
hihsmDKACSWDKAClusterNumber = _HihsmDKACSWDKAClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7, 1, 2),
    _HihsmDKACSWDKAClusterNumber_Type()
)
hihsmDKACSWDKAClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKACSWDKAClusterNumber.setStatus("mandatory")
_HihsmDKACSWDKANumber_Type = Integer32
_HihsmDKACSWDKANumber_Object = MibTableColumn
hihsmDKACSWDKANumber = _HihsmDKACSWDKANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7, 1, 3),
    _HihsmDKACSWDKANumber_Type()
)
hihsmDKACSWDKANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKACSWDKANumber.setStatus("mandatory")
_HihsmDKACSWCSWClusterNumber_Type = Integer32
_HihsmDKACSWCSWClusterNumber_Object = MibTableColumn
hihsmDKACSWCSWClusterNumber = _HihsmDKACSWCSWClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7, 1, 4),
    _HihsmDKACSWCSWClusterNumber_Type()
)
hihsmDKACSWCSWClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKACSWCSWClusterNumber.setStatus("mandatory")
_HihsmDKACSWCSWNumber_Type = Integer32
_HihsmDKACSWCSWNumber_Object = MibTableColumn
hihsmDKACSWCSWNumber = _HihsmDKACSWCSWNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7, 1, 5),
    _HihsmDKACSWCSWNumber_Type()
)
hihsmDKACSWCSWNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKACSWCSWNumber.setStatus("mandatory")
_HihsmDKACSWUtilData_Type = DisplayString
_HihsmDKACSWUtilData_Object = MibTableColumn
hihsmDKACSWUtilData = _HihsmDKACSWUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 7, 1, 6),
    _HihsmDKACSWUtilData_Type()
)
hihsmDKACSWUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKACSWUtilData.setStatus("mandatory")
_HihsmCSWtoCacheUtilizationTable_Object = MibTable
hihsmCSWtoCacheUtilizationTable = _HihsmCSWtoCacheUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8)
)
if mibBuilder.loadTexts:
    hihsmCSWtoCacheUtilizationTable.setStatus("mandatory")
_HihsmCSWtoCacheUtilizationEntry_Object = MibTableRow
hihsmCSWtoCacheUtilizationEntry = _HihsmCSWtoCacheUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8, 1)
)
hihsmCSWtoCacheUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmCSWCacheSerialNumber"),
    (0, "HDS9900MIB", "hihsmCSWCacheCSWClusterNumber"),
    (0, "HDS9900MIB", "hihsmCSWCacheCSWNumber"),
    (0, "HDS9900MIB", "hihsmCSWCacheCacheClusterNumber"),
    (0, "HDS9900MIB", "hihsmCSWCacheCacheNumber"),
)
if mibBuilder.loadTexts:
    hihsmCSWtoCacheUtilizationEntry.setStatus("mandatory")
_HihsmCSWCacheSerialNumber_Type = Integer32
_HihsmCSWCacheSerialNumber_Object = MibTableColumn
hihsmCSWCacheSerialNumber = _HihsmCSWCacheSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8, 1, 1),
    _HihsmCSWCacheSerialNumber_Type()
)
hihsmCSWCacheSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCSWCacheSerialNumber.setStatus("mandatory")
_HihsmCSWCacheCSWClusterNumber_Type = Integer32
_HihsmCSWCacheCSWClusterNumber_Object = MibTableColumn
hihsmCSWCacheCSWClusterNumber = _HihsmCSWCacheCSWClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8, 1, 2),
    _HihsmCSWCacheCSWClusterNumber_Type()
)
hihsmCSWCacheCSWClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCSWCacheCSWClusterNumber.setStatus("mandatory")
_HihsmCSWCacheCSWNumber_Type = Integer32
_HihsmCSWCacheCSWNumber_Object = MibTableColumn
hihsmCSWCacheCSWNumber = _HihsmCSWCacheCSWNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8, 1, 3),
    _HihsmCSWCacheCSWNumber_Type()
)
hihsmCSWCacheCSWNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCSWCacheCSWNumber.setStatus("mandatory")
_HihsmCSWCacheCacheClusterNumber_Type = Integer32
_HihsmCSWCacheCacheClusterNumber_Object = MibTableColumn
hihsmCSWCacheCacheClusterNumber = _HihsmCSWCacheCacheClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8, 1, 4),
    _HihsmCSWCacheCacheClusterNumber_Type()
)
hihsmCSWCacheCacheClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCSWCacheCacheClusterNumber.setStatus("mandatory")
_HihsmCSWCacheCacheNumber_Type = Integer32
_HihsmCSWCacheCacheNumber_Object = MibTableColumn
hihsmCSWCacheCacheNumber = _HihsmCSWCacheCacheNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8, 1, 5),
    _HihsmCSWCacheCacheNumber_Type()
)
hihsmCSWCacheCacheNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCSWCacheCacheNumber.setStatus("mandatory")
_HihsmCSWCacheUtilData_Type = DisplayString
_HihsmCSWCacheUtilData_Object = MibTableColumn
hihsmCSWCacheUtilData = _HihsmCSWCacheUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 8, 1, 6),
    _HihsmCSWCacheUtilData_Type()
)
hihsmCSWCacheUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCSWCacheUtilData.setStatus("mandatory")
_HihsmCHAtoSMUtilizationTable_Object = MibTable
hihsmCHAtoSMUtilizationTable = _HihsmCHAtoSMUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 9)
)
if mibBuilder.loadTexts:
    hihsmCHAtoSMUtilizationTable.setStatus("mandatory")
_HihsmCHAtoSMUtilizationEntry_Object = MibTableRow
hihsmCHAtoSMUtilizationEntry = _HihsmCHAtoSMUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 9, 1)
)
hihsmCHAtoSMUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmCHASMSerialNumber"),
    (0, "HDS9900MIB", "hihsmCHASMCHAClusterNumber"),
    (0, "HDS9900MIB", "hihsmCHASMCHANumber"),
    (0, "HDS9900MIB", "hihsmCHASMSMClusterNumber"),
)
if mibBuilder.loadTexts:
    hihsmCHAtoSMUtilizationEntry.setStatus("mandatory")
_HihsmCHASMSerialNumber_Type = Integer32
_HihsmCHASMSerialNumber_Object = MibTableColumn
hihsmCHASMSerialNumber = _HihsmCHASMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 9, 1, 1),
    _HihsmCHASMSerialNumber_Type()
)
hihsmCHASMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHASMSerialNumber.setStatus("mandatory")
_HihsmCHASMCHAClusterNumber_Type = Integer32
_HihsmCHASMCHAClusterNumber_Object = MibTableColumn
hihsmCHASMCHAClusterNumber = _HihsmCHASMCHAClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 9, 1, 2),
    _HihsmCHASMCHAClusterNumber_Type()
)
hihsmCHASMCHAClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHASMCHAClusterNumber.setStatus("mandatory")
_HihsmCHASMCHANumber_Type = Integer32
_HihsmCHASMCHANumber_Object = MibTableColumn
hihsmCHASMCHANumber = _HihsmCHASMCHANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 9, 1, 3),
    _HihsmCHASMCHANumber_Type()
)
hihsmCHASMCHANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHASMCHANumber.setStatus("mandatory")
_HihsmCHASMSMClusterNumber_Type = Integer32
_HihsmCHASMSMClusterNumber_Object = MibTableColumn
hihsmCHASMSMClusterNumber = _HihsmCHASMSMClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 9, 1, 4),
    _HihsmCHASMSMClusterNumber_Type()
)
hihsmCHASMSMClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHASMSMClusterNumber.setStatus("mandatory")
_HihsmCHASMUtilData_Type = DisplayString
_HihsmCHASMUtilData_Object = MibTableColumn
hihsmCHASMUtilData = _HihsmCHASMUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 9, 1, 5),
    _HihsmCHASMUtilData_Type()
)
hihsmCHASMUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmCHASMUtilData.setStatus("mandatory")
_HihsmDKAtoSMUtilizationTable_Object = MibTable
hihsmDKAtoSMUtilizationTable = _HihsmDKAtoSMUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 10)
)
if mibBuilder.loadTexts:
    hihsmDKAtoSMUtilizationTable.setStatus("mandatory")
_HihsmDKAtoSMUtilizationEntry_Object = MibTableRow
hihsmDKAtoSMUtilizationEntry = _HihsmDKAtoSMUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 10, 1)
)
hihsmDKAtoSMUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmDKASMSerialNumber"),
    (0, "HDS9900MIB", "hihsmDKASMDKAClusterNumber"),
    (0, "HDS9900MIB", "hihsmDKASMDKANumber"),
    (0, "HDS9900MIB", "hihsmDKASMSMClusterNumber"),
)
if mibBuilder.loadTexts:
    hihsmDKAtoSMUtilizationEntry.setStatus("mandatory")
_HihsmDKASMSerialNumber_Type = Integer32
_HihsmDKASMSerialNumber_Object = MibTableColumn
hihsmDKASMSerialNumber = _HihsmDKASMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 10, 1, 1),
    _HihsmDKASMSerialNumber_Type()
)
hihsmDKASMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKASMSerialNumber.setStatus("mandatory")
_HihsmDKASMDKAClusterNumber_Type = Integer32
_HihsmDKASMDKAClusterNumber_Object = MibTableColumn
hihsmDKASMDKAClusterNumber = _HihsmDKASMDKAClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 10, 1, 2),
    _HihsmDKASMDKAClusterNumber_Type()
)
hihsmDKASMDKAClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKASMDKAClusterNumber.setStatus("mandatory")
_HihsmDKASMDKANumber_Type = Integer32
_HihsmDKASMDKANumber_Object = MibTableColumn
hihsmDKASMDKANumber = _HihsmDKASMDKANumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 10, 1, 3),
    _HihsmDKASMDKANumber_Type()
)
hihsmDKASMDKANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKASMDKANumber.setStatus("mandatory")
_HihsmDKASMSMClusterNumber_Type = Integer32
_HihsmDKASMSMClusterNumber_Object = MibTableColumn
hihsmDKASMSMClusterNumber = _HihsmDKASMSMClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 10, 1, 4),
    _HihsmDKASMSMClusterNumber_Type()
)
hihsmDKASMSMClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKASMSMClusterNumber.setStatus("mandatory")
_HihsmDKASMUtilData_Type = DisplayString
_HihsmDKASMUtilData_Object = MibTableColumn
hihsmDKASMUtilData = _HihsmDKASMUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 10, 1, 5),
    _HihsmDKASMUtilData_Type()
)
hihsmDKASMUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKASMUtilData.setStatus("mandatory")
_HihsmDKCUtilizationTable_Object = MibTable
hihsmDKCUtilizationTable = _HihsmDKCUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 11)
)
if mibBuilder.loadTexts:
    hihsmDKCUtilizationTable.setStatus("mandatory")
_HihsmDKCUtilizationEntry_Object = MibTableRow
hihsmDKCUtilizationEntry = _HihsmDKCUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 11, 1)
)
hihsmDKCUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmCHASMSerialNumber"),
)
if mibBuilder.loadTexts:
    hihsmDKCUtilizationEntry.setStatus("mandatory")
_HihsmDKCUtilSerialNumber_Type = Integer32
_HihsmDKCUtilSerialNumber_Object = MibTableColumn
hihsmDKCUtilSerialNumber = _HihsmDKCUtilSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 11, 1, 1),
    _HihsmDKCUtilSerialNumber_Type()
)
hihsmDKCUtilSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKCUtilSerialNumber.setStatus("mandatory")
_HihsmDKCUtilWritePending_Type = DisplayString
_HihsmDKCUtilWritePending_Object = MibTableColumn
hihsmDKCUtilWritePending = _HihsmDKCUtilWritePending_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 3, 11, 1, 2),
    _HihsmDKCUtilWritePending_Type()
)
hihsmDKCUtilWritePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmDKCUtilWritePending.setStatus("mandatory")
_HihsmAutomaticMigration_ObjectIdentity = ObjectIdentity
hihsmAutomaticMigration = _HihsmAutomaticMigration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4)
)
_HihsmAutomaticMigrationParameterTable_Object = MibTable
hihsmAutomaticMigrationParameterTable = _HihsmAutomaticMigrationParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1)
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationParameterTable.setStatus("mandatory")
_HihsmAutomaticMigrationParameterEntry_Object = MibTableRow
hihsmAutomaticMigrationParameterEntry = _HihsmAutomaticMigrationParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1)
)
hihsmAutomaticMigrationParameterEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmAutoParamSerialNumber"),
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationParameterEntry.setStatus("mandatory")
_HihsmAutoParamSerialNumber_Type = Integer32
_HihsmAutoParamSerialNumber_Object = MibTableColumn
hihsmAutoParamSerialNumber = _HihsmAutoParamSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 1),
    _HihsmAutoParamSerialNumber_Type()
)
hihsmAutoParamSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmAutoParamSerialNumber.setStatus("mandatory")
_HihsmAutoParamFunctionSwitch_Type = Integer32
_HihsmAutoParamFunctionSwitch_Object = MibTableColumn
hihsmAutoParamFunctionSwitch = _HihsmAutoParamFunctionSwitch_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 2),
    _HihsmAutoParamFunctionSwitch_Type()
)
hihsmAutoParamFunctionSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamFunctionSwitch.setStatus("mandatory")
_HihsmAutoParamPlanningDay_Type = Integer32
_HihsmAutoParamPlanningDay_Object = MibTableColumn
hihsmAutoParamPlanningDay = _HihsmAutoParamPlanningDay_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 3),
    _HihsmAutoParamPlanningDay_Type()
)
hihsmAutoParamPlanningDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamPlanningDay.setStatus("mandatory")
_HihsmAutoParamIntervalDay_Type = Integer32
_HihsmAutoParamIntervalDay_Object = MibTableColumn
hihsmAutoParamIntervalDay = _HihsmAutoParamIntervalDay_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 4),
    _HihsmAutoParamIntervalDay_Type()
)
hihsmAutoParamIntervalDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamIntervalDay.setStatus("mandatory")
_HihsmAutoParamDayOfWeek_Type = Integer32
_HihsmAutoParamDayOfWeek_Object = MibTableColumn
hihsmAutoParamDayOfWeek = _HihsmAutoParamDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 5),
    _HihsmAutoParamDayOfWeek_Type()
)
hihsmAutoParamDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamDayOfWeek.setStatus("mandatory")
_HihsmAutoParamUseFromTime_Type = DisplayString
_HihsmAutoParamUseFromTime_Object = MibTableColumn
hihsmAutoParamUseFromTime = _HihsmAutoParamUseFromTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 6),
    _HihsmAutoParamUseFromTime_Type()
)
hihsmAutoParamUseFromTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamUseFromTime.setStatus("mandatory")
_HihsmAutoParamUseToTime_Type = DisplayString
_HihsmAutoParamUseToTime_Object = MibTableColumn
hihsmAutoParamUseToTime = _HihsmAutoParamUseToTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 7),
    _HihsmAutoParamUseToTime_Type()
)
hihsmAutoParamUseToTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamUseToTime.setStatus("mandatory")
_HihsmAutoParamJudgeMethod_Type = Integer32
_HihsmAutoParamJudgeMethod_Object = MibTableColumn
hihsmAutoParamJudgeMethod = _HihsmAutoParamJudgeMethod_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 8),
    _HihsmAutoParamJudgeMethod_Type()
)
hihsmAutoParamJudgeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamJudgeMethod.setStatus("mandatory")
_HihsmAutoParamHightestPoints_Type = Integer32
_HihsmAutoParamHightestPoints_Object = MibTableColumn
hihsmAutoParamHightestPoints = _HihsmAutoParamHightestPoints_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 9),
    _HihsmAutoParamHightestPoints_Type()
)
hihsmAutoParamHightestPoints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamHightestPoints.setStatus("mandatory")
_HihsmAutoParamExecutionTime_Type = DisplayString
_HihsmAutoParamExecutionTime_Object = MibTableColumn
hihsmAutoParamExecutionTime = _HihsmAutoParamExecutionTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 10),
    _HihsmAutoParamExecutionTime_Type()
)
hihsmAutoParamExecutionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamExecutionTime.setStatus("mandatory")
_HihsmAutoParamMaxDuration_Type = Integer32
_HihsmAutoParamMaxDuration_Object = MibTableColumn
hihsmAutoParamMaxDuration = _HihsmAutoParamMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 11),
    _HihsmAutoParamMaxDuration_Type()
)
hihsmAutoParamMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamMaxDuration.setStatus("mandatory")
_HihsmAutoParamMaxUtilization_Type = Integer32
_HihsmAutoParamMaxUtilization_Object = MibTableColumn
hihsmAutoParamMaxUtilization = _HihsmAutoParamMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 12),
    _HihsmAutoParamMaxUtilization_Type()
)
hihsmAutoParamMaxUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamMaxUtilization.setStatus("mandatory")
_HihsmAutoParamMaxVolumes_Type = Integer32
_HihsmAutoParamMaxVolumes_Object = MibTableColumn
hihsmAutoParamMaxVolumes = _HihsmAutoParamMaxVolumes_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 13),
    _HihsmAutoParamMaxVolumes_Type()
)
hihsmAutoParamMaxVolumes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamMaxVolumes.setStatus("mandatory")
_HihsmAutoParamControlStatus_Type = Integer32
_HihsmAutoParamControlStatus_Object = MibTableColumn
hihsmAutoParamControlStatus = _HihsmAutoParamControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 14),
    _HihsmAutoParamControlStatus_Type()
)
hihsmAutoParamControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamControlStatus.setStatus("mandatory")
_HihsmAutoParamDayOfMonth_Type = Integer32
_HihsmAutoParamDayOfMonth_Object = MibTableColumn
hihsmAutoParamDayOfMonth = _HihsmAutoParamDayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 1, 1, 15),
    _HihsmAutoParamDayOfMonth_Type()
)
hihsmAutoParamDayOfMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoParamDayOfMonth.setStatus("mandatory")
_HihsmAutomaticMigrationClass_ObjectIdentity = ObjectIdentity
hihsmAutomaticMigrationClass = _HihsmAutomaticMigrationClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2)
)
_HihsmAutomaticMigrationClassListTable_Object = MibTable
hihsmAutomaticMigrationClassListTable = _HihsmAutomaticMigrationClassListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationClassListTable.setStatus("mandatory")
_HihsmAutomaticMigrationClassListEntry_Object = MibTableRow
hihsmAutomaticMigrationClassListEntry = _HihsmAutomaticMigrationClassListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 1, 1)
)
hihsmAutomaticMigrationClassListEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmClassListSerialNumber"),
    (0, "HDS9900MIB", "hihsmClassListClassNumber"),
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationClassListEntry.setStatus("mandatory")
_HihsmClassListSerialNumber_Type = Integer32
_HihsmClassListSerialNumber_Object = MibTableColumn
hihsmClassListSerialNumber = _HihsmClassListSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 1, 1, 1),
    _HihsmClassListSerialNumber_Type()
)
hihsmClassListSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassListSerialNumber.setStatus("mandatory")
_HihsmClassListClassNumber_Type = Integer32
_HihsmClassListClassNumber_Object = MibTableColumn
hihsmClassListClassNumber = _HihsmClassListClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 1, 1, 2),
    _HihsmClassListClassNumber_Type()
)
hihsmClassListClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassListClassNumber.setStatus("mandatory")
_HihsmClassListDisplayName_Type = DisplayString
_HihsmClassListDisplayName_Object = MibTableColumn
hihsmClassListDisplayName = _HihsmClassListDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 1, 1, 3),
    _HihsmClassListDisplayName_Type()
)
hihsmClassListDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassListDisplayName.setStatus("mandatory")
_HihsmClassListMaxUtilization_Type = Integer32
_HihsmClassListMaxUtilization_Object = MibTableColumn
hihsmClassListMaxUtilization = _HihsmClassListMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 1, 1, 4),
    _HihsmClassListMaxUtilization_Type()
)
hihsmClassListMaxUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmClassListMaxUtilization.setStatus("mandatory")
_HihsmClassListControlStatus_Type = Integer32
_HihsmClassListControlStatus_Object = MibTableColumn
hihsmClassListControlStatus = _HihsmClassListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 1, 1, 5),
    _HihsmClassListControlStatus_Type()
)
hihsmClassListControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmClassListControlStatus.setStatus("mandatory")
_HihsmAutomaticMigrationClassPGTable_Object = MibTable
hihsmAutomaticMigrationClassPGTable = _HihsmAutomaticMigrationClassPGTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationClassPGTable.setStatus("mandatory")
_HihsmAutomaticMigrationClassPGEntry_Object = MibTableRow
hihsmAutomaticMigrationClassPGEntry = _HihsmAutomaticMigrationClassPGEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 2, 1)
)
hihsmAutomaticMigrationClassPGEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmClassPGSerialNumber"),
    (0, "HDS9900MIB", "hihsmClassPGClassNumber"),
    (0, "HDS9900MIB", "hihsmClassPGControlIndex"),
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationClassPGEntry.setStatus("mandatory")
_HihsmClassPGSerialNumber_Type = Integer32
_HihsmClassPGSerialNumber_Object = MibTableColumn
hihsmClassPGSerialNumber = _HihsmClassPGSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 2, 1, 1),
    _HihsmClassPGSerialNumber_Type()
)
hihsmClassPGSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassPGSerialNumber.setStatus("mandatory")
_HihsmClassPGClassNumber_Type = Integer32
_HihsmClassPGClassNumber_Object = MibTableColumn
hihsmClassPGClassNumber = _HihsmClassPGClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 2, 1, 2),
    _HihsmClassPGClassNumber_Type()
)
hihsmClassPGClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassPGClassNumber.setStatus("mandatory")
_HihsmClassPGControlIndex_Type = Integer32
_HihsmClassPGControlIndex_Object = MibTableColumn
hihsmClassPGControlIndex = _HihsmClassPGControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 2, 1, 3),
    _HihsmClassPGControlIndex_Type()
)
hihsmClassPGControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassPGControlIndex.setStatus("mandatory")
_HihsmClassPGFB4Number_Type = Integer32
_HihsmClassPGFB4Number_Object = MibTableColumn
hihsmClassPGFB4Number = _HihsmClassPGFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 2, 1, 4),
    _HihsmClassPGFB4Number_Type()
)
hihsmClassPGFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassPGFB4Number.setStatus("mandatory")
_HihsmClassPGPGNumber_Type = Integer32
_HihsmClassPGPGNumber_Object = MibTableColumn
hihsmClassPGPGNumber = _HihsmClassPGPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 2, 2, 1, 5),
    _HihsmClassPGPGNumber_Type()
)
hihsmClassPGPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmClassPGPGNumber.setStatus("mandatory")
_HihsmAutomaticMigrationPlan_ObjectIdentity = ObjectIdentity
hihsmAutomaticMigrationPlan = _HihsmAutomaticMigrationPlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3)
)
_HihsmAutomaticMigrationPlanStatusTable_Object = MibTable
hihsmAutomaticMigrationPlanStatusTable = _HihsmAutomaticMigrationPlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationPlanStatusTable.setStatus("mandatory")
_HihsmAutomaticMigrationPlanStatusEntry_Object = MibTableRow
hihsmAutomaticMigrationPlanStatusEntry = _HihsmAutomaticMigrationPlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1)
)
hihsmAutomaticMigrationPlanStatusEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmPlanStatusSerialNumber"),
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationPlanStatusEntry.setStatus("mandatory")
_HihsmPlanStatusSerialNumber_Type = Integer32
_HihsmPlanStatusSerialNumber_Object = MibTableColumn
hihsmPlanStatusSerialNumber = _HihsmPlanStatusSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1, 1),
    _HihsmPlanStatusSerialNumber_Type()
)
hihsmPlanStatusSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanStatusSerialNumber.setStatus("mandatory")
_HihsmPlanStatusData_Type = Integer32
_HihsmPlanStatusData_Object = MibTableColumn
hihsmPlanStatusData = _HihsmPlanStatusData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1, 2),
    _HihsmPlanStatusData_Type()
)
hihsmPlanStatusData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanStatusData.setStatus("mandatory")
_HihsmPlanStatusCheckDate_Type = DisplayString
_HihsmPlanStatusCheckDate_Object = MibTableColumn
hihsmPlanStatusCheckDate = _HihsmPlanStatusCheckDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1, 3),
    _HihsmPlanStatusCheckDate_Type()
)
hihsmPlanStatusCheckDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanStatusCheckDate.setStatus("mandatory")
_HihsmPlanStatusCheckTime_Type = DisplayString
_HihsmPlanStatusCheckTime_Object = MibTableColumn
hihsmPlanStatusCheckTime = _HihsmPlanStatusCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1, 4),
    _HihsmPlanStatusCheckTime_Type()
)
hihsmPlanStatusCheckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanStatusCheckTime.setStatus("mandatory")
_HihsmPlanStatusMigrationDate_Type = DisplayString
_HihsmPlanStatusMigrationDate_Object = MibTableColumn
hihsmPlanStatusMigrationDate = _HihsmPlanStatusMigrationDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1, 5),
    _HihsmPlanStatusMigrationDate_Type()
)
hihsmPlanStatusMigrationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanStatusMigrationDate.setStatus("mandatory")
_HihsmPlanStatusMigrationTime_Type = DisplayString
_HihsmPlanStatusMigrationTime_Object = MibTableColumn
hihsmPlanStatusMigrationTime = _HihsmPlanStatusMigrationTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1, 6),
    _HihsmPlanStatusMigrationTime_Type()
)
hihsmPlanStatusMigrationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanStatusMigrationTime.setStatus("mandatory")
_HihsmPlanStatusControlStatus_Type = Integer32
_HihsmPlanStatusControlStatus_Object = MibTableColumn
hihsmPlanStatusControlStatus = _HihsmPlanStatusControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 1, 1, 7),
    _HihsmPlanStatusControlStatus_Type()
)
hihsmPlanStatusControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmPlanStatusControlStatus.setStatus("mandatory")
_HihsmAutomaticMigrationPlanLDEVTable_Object = MibTable
hihsmAutomaticMigrationPlanLDEVTable = _HihsmAutomaticMigrationPlanLDEVTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2)
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationPlanLDEVTable.setStatus("mandatory")
_HihsmAutomaticMigrationPlanLDEVEntry_Object = MibTableRow
hihsmAutomaticMigrationPlanLDEVEntry = _HihsmAutomaticMigrationPlanLDEVEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1)
)
hihsmAutomaticMigrationPlanLDEVEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmPlanLDEVSerialNumber"),
    (0, "HDS9900MIB", "hihsmPlanLDEVControlIndex"),
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationPlanLDEVEntry.setStatus("mandatory")
_HihsmPlanLDEVSerialNumber_Type = Integer32
_HihsmPlanLDEVSerialNumber_Object = MibTableColumn
hihsmPlanLDEVSerialNumber = _HihsmPlanLDEVSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 1),
    _HihsmPlanLDEVSerialNumber_Type()
)
hihsmPlanLDEVSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVSerialNumber.setStatus("mandatory")
_HihsmPlanLDEVControlIndex_Type = Integer32
_HihsmPlanLDEVControlIndex_Object = MibTableColumn
hihsmPlanLDEVControlIndex = _HihsmPlanLDEVControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 2),
    _HihsmPlanLDEVControlIndex_Type()
)
hihsmPlanLDEVControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVControlIndex.setStatus("mandatory")
_HihsmPlanLDEVSrcFB4Number_Type = Integer32
_HihsmPlanLDEVSrcFB4Number_Object = MibTableColumn
hihsmPlanLDEVSrcFB4Number = _HihsmPlanLDEVSrcFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 3),
    _HihsmPlanLDEVSrcFB4Number_Type()
)
hihsmPlanLDEVSrcFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVSrcFB4Number.setStatus("mandatory")
_HihsmPlanLDEVSrcPGNumber_Type = Integer32
_HihsmPlanLDEVSrcPGNumber_Object = MibTableColumn
hihsmPlanLDEVSrcPGNumber = _HihsmPlanLDEVSrcPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 4),
    _HihsmPlanLDEVSrcPGNumber_Type()
)
hihsmPlanLDEVSrcPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVSrcPGNumber.setStatus("mandatory")
_HihsmPlanLDEVSrcCU_Type = Integer32
_HihsmPlanLDEVSrcCU_Object = MibTableColumn
hihsmPlanLDEVSrcCU = _HihsmPlanLDEVSrcCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 5),
    _HihsmPlanLDEVSrcCU_Type()
)
hihsmPlanLDEVSrcCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVSrcCU.setStatus("mandatory")
_HihsmPlanLDEVSrcLDEV_Type = Integer32
_HihsmPlanLDEVSrcLDEV_Object = MibTableColumn
hihsmPlanLDEVSrcLDEV = _HihsmPlanLDEVSrcLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 6),
    _HihsmPlanLDEVSrcLDEV_Type()
)
hihsmPlanLDEVSrcLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVSrcLDEV.setStatus("mandatory")
_HihsmPlanLDEVDstFB4Number_Type = Integer32
_HihsmPlanLDEVDstFB4Number_Object = MibTableColumn
hihsmPlanLDEVDstFB4Number = _HihsmPlanLDEVDstFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 7),
    _HihsmPlanLDEVDstFB4Number_Type()
)
hihsmPlanLDEVDstFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVDstFB4Number.setStatus("mandatory")
_HihsmPlanLDEVDstPGNumber_Type = Integer32
_HihsmPlanLDEVDstPGNumber_Object = MibTableColumn
hihsmPlanLDEVDstPGNumber = _HihsmPlanLDEVDstPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 8),
    _HihsmPlanLDEVDstPGNumber_Type()
)
hihsmPlanLDEVDstPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVDstPGNumber.setStatus("mandatory")
_HihsmPlanLDEVDstCU_Type = Integer32
_HihsmPlanLDEVDstCU_Object = MibTableColumn
hihsmPlanLDEVDstCU = _HihsmPlanLDEVDstCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 9),
    _HihsmPlanLDEVDstCU_Type()
)
hihsmPlanLDEVDstCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVDstCU.setStatus("mandatory")
_HihsmPlanLDEVDstLDEV_Type = Integer32
_HihsmPlanLDEVDstLDEV_Object = MibTableColumn
hihsmPlanLDEVDstLDEV = _HihsmPlanLDEVDstLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 3, 2, 1, 10),
    _HihsmPlanLDEVDstLDEV_Type()
)
hihsmPlanLDEVDstLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmPlanLDEVDstLDEV.setStatus("mandatory")
_HihsmAutomaticMigrationHistory_ObjectIdentity = ObjectIdentity
hihsmAutomaticMigrationHistory = _HihsmAutomaticMigrationHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4)
)
_HihsmAutomaticMigrationHistoryCtrlTable_Object = MibTable
hihsmAutomaticMigrationHistoryCtrlTable = _HihsmAutomaticMigrationHistoryCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationHistoryCtrlTable.setStatus("mandatory")
_HihsmAutomaticMigrationHistoryCtrlEntry_Object = MibTableRow
hihsmAutomaticMigrationHistoryCtrlEntry = _HihsmAutomaticMigrationHistoryCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 1, 1)
)
hihsmAutomaticMigrationHistoryCtrlEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmAutoHstCtrlSerialNumber"),
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationHistoryCtrlEntry.setStatus("mandatory")
_HihsmAutoHstCtrlSerialNumber_Type = Integer32
_HihsmAutoHstCtrlSerialNumber_Object = MibTableColumn
hihsmAutoHstCtrlSerialNumber = _HihsmAutoHstCtrlSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 1, 1, 1),
    _HihsmAutoHstCtrlSerialNumber_Type()
)
hihsmAutoHstCtrlSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmAutoHstCtrlSerialNumber.setStatus("mandatory")
_HihsmAutoHstCtrlControlStatus_Type = Integer32
_HihsmAutoHstCtrlControlStatus_Object = MibTableColumn
hihsmAutoHstCtrlControlStatus = _HihsmAutoHstCtrlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 1, 1, 2),
    _HihsmAutoHstCtrlControlStatus_Type()
)
hihsmAutoHstCtrlControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmAutoHstCtrlControlStatus.setStatus("mandatory")
_HihsmAutomaticMigrationHistoryListTable_Object = MibTable
hihsmAutomaticMigrationHistoryListTable = _HihsmAutomaticMigrationHistoryListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 2)
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationHistoryListTable.setStatus("mandatory")
_HihsmAutomaticMigrationHistoryListEntry_Object = MibTableRow
hihsmAutomaticMigrationHistoryListEntry = _HihsmAutomaticMigrationHistoryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 2, 1)
)
hihsmAutomaticMigrationHistoryListEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmAutoHstListSerialNumber"),
    (0, "HDS9900MIB", "hihsmAutoHstListControlIndex"),
)
if mibBuilder.loadTexts:
    hihsmAutomaticMigrationHistoryListEntry.setStatus("mandatory")
_HihsmAutoHstListSerialNumber_Type = Integer32
_HihsmAutoHstListSerialNumber_Object = MibTableColumn
hihsmAutoHstListSerialNumber = _HihsmAutoHstListSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 2, 1, 1),
    _HihsmAutoHstListSerialNumber_Type()
)
hihsmAutoHstListSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmAutoHstListSerialNumber.setStatus("mandatory")
_HihsmAutoHstListControlIndex_Type = Integer32
_HihsmAutoHstListControlIndex_Object = MibTableColumn
hihsmAutoHstListControlIndex = _HihsmAutoHstListControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 2, 1, 2),
    _HihsmAutoHstListControlIndex_Type()
)
hihsmAutoHstListControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmAutoHstListControlIndex.setStatus("mandatory")
_HihsmAutoHstListMessage_Type = DisplayString
_HihsmAutoHstListMessage_Object = MibTableColumn
hihsmAutoHstListMessage = _HihsmAutoHstListMessage_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 4, 2, 1, 3),
    _HihsmAutoHstListMessage_Type()
)
hihsmAutoHstListMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmAutoHstListMessage.setStatus("mandatory")
_HihsmVolumeMigrationHistory_ObjectIdentity = ObjectIdentity
hihsmVolumeMigrationHistory = _HihsmVolumeMigrationHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5)
)
_HihsmVolumeMigrationHistoryCtrlTable_Object = MibTable
hihsmVolumeMigrationHistoryCtrlTable = _HihsmVolumeMigrationHistoryCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 1)
)
if mibBuilder.loadTexts:
    hihsmVolumeMigrationHistoryCtrlTable.setStatus("mandatory")
_HihsmVolumeMigrationHistoryCtrlEntry_Object = MibTableRow
hihsmVolumeMigrationHistoryCtrlEntry = _HihsmVolumeMigrationHistoryCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 1, 1)
)
hihsmVolumeMigrationHistoryCtrlEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmVolHstCtrlSerialNumber"),
)
if mibBuilder.loadTexts:
    hihsmVolumeMigrationHistoryCtrlEntry.setStatus("mandatory")
_HihsmVolHstCtrlSerialNumber_Type = Integer32
_HihsmVolHstCtrlSerialNumber_Object = MibTableColumn
hihsmVolHstCtrlSerialNumber = _HihsmVolHstCtrlSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 1, 1, 1),
    _HihsmVolHstCtrlSerialNumber_Type()
)
hihsmVolHstCtrlSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstCtrlSerialNumber.setStatus("mandatory")
_HihsmVolHstCtrlControlStatus_Type = Integer32
_HihsmVolHstCtrlControlStatus_Object = MibTableColumn
hihsmVolHstCtrlControlStatus = _HihsmVolHstCtrlControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 1, 1, 2),
    _HihsmVolHstCtrlControlStatus_Type()
)
hihsmVolHstCtrlControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmVolHstCtrlControlStatus.setStatus("mandatory")
_HihsmVolumeMigrationHistoryListTable_Object = MibTable
hihsmVolumeMigrationHistoryListTable = _HihsmVolumeMigrationHistoryListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2)
)
if mibBuilder.loadTexts:
    hihsmVolumeMigrationHistoryListTable.setStatus("mandatory")
_HihsmVolumeMigrationHistoryListEntry_Object = MibTableRow
hihsmVolumeMigrationHistoryListEntry = _HihsmVolumeMigrationHistoryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1)
)
hihsmVolumeMigrationHistoryListEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmVolHstListSerialNumber"),
    (0, "HDS9900MIB", "hihsmVolHstListControlIndex"),
)
if mibBuilder.loadTexts:
    hihsmVolumeMigrationHistoryListEntry.setStatus("mandatory")
_HihsmVolHstListSerialNumber_Type = Integer32
_HihsmVolHstListSerialNumber_Object = MibTableColumn
hihsmVolHstListSerialNumber = _HihsmVolHstListSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 1),
    _HihsmVolHstListSerialNumber_Type()
)
hihsmVolHstListSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListSerialNumber.setStatus("mandatory")
_HihsmVolHstListControlIndex_Type = Integer32
_HihsmVolHstListControlIndex_Object = MibTableColumn
hihsmVolHstListControlIndex = _HihsmVolHstListControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 2),
    _HihsmVolHstListControlIndex_Type()
)
hihsmVolHstListControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListControlIndex.setStatus("mandatory")
_HihsmVolHstListDate_Type = DisplayString
_HihsmVolHstListDate_Object = MibTableColumn
hihsmVolHstListDate = _HihsmVolHstListDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 3),
    _HihsmVolHstListDate_Type()
)
hihsmVolHstListDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListDate.setStatus("mandatory")
_HihsmVolHstListTime_Type = DisplayString
_HihsmVolHstListTime_Object = MibTableColumn
hihsmVolHstListTime = _HihsmVolHstListTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 4),
    _HihsmVolHstListTime_Type()
)
hihsmVolHstListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListTime.setStatus("mandatory")
_HihsmVolHstListAction_Type = DisplayString
_HihsmVolHstListAction_Object = MibTableColumn
hihsmVolHstListAction = _HihsmVolHstListAction_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 5),
    _HihsmVolHstListAction_Type()
)
hihsmVolHstListAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListAction.setStatus("mandatory")
_HihsmVolHstListSrcFB4Number_Type = Integer32
_HihsmVolHstListSrcFB4Number_Object = MibTableColumn
hihsmVolHstListSrcFB4Number = _HihsmVolHstListSrcFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 6),
    _HihsmVolHstListSrcFB4Number_Type()
)
hihsmVolHstListSrcFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListSrcFB4Number.setStatus("mandatory")
_HihsmVolHstListSrcPGNumber_Type = Integer32
_HihsmVolHstListSrcPGNumber_Object = MibTableColumn
hihsmVolHstListSrcPGNumber = _HihsmVolHstListSrcPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 7),
    _HihsmVolHstListSrcPGNumber_Type()
)
hihsmVolHstListSrcPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListSrcPGNumber.setStatus("mandatory")
_HihsmVolHstListSrcCU_Type = Integer32
_HihsmVolHstListSrcCU_Object = MibTableColumn
hihsmVolHstListSrcCU = _HihsmVolHstListSrcCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 8),
    _HihsmVolHstListSrcCU_Type()
)
hihsmVolHstListSrcCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListSrcCU.setStatus("mandatory")
_HihsmVolHstListSrcLDEV_Type = Integer32
_HihsmVolHstListSrcLDEV_Object = MibTableColumn
hihsmVolHstListSrcLDEV = _HihsmVolHstListSrcLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 9),
    _HihsmVolHstListSrcLDEV_Type()
)
hihsmVolHstListSrcLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListSrcLDEV.setStatus("mandatory")
_HihsmVolHstListDstFB4Number_Type = Integer32
_HihsmVolHstListDstFB4Number_Object = MibTableColumn
hihsmVolHstListDstFB4Number = _HihsmVolHstListDstFB4Number_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 10),
    _HihsmVolHstListDstFB4Number_Type()
)
hihsmVolHstListDstFB4Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListDstFB4Number.setStatus("mandatory")
_HihsmVolHstListDstPGNumber_Type = Integer32
_HihsmVolHstListDstPGNumber_Object = MibTableColumn
hihsmVolHstListDstPGNumber = _HihsmVolHstListDstPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 11),
    _HihsmVolHstListDstPGNumber_Type()
)
hihsmVolHstListDstPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListDstPGNumber.setStatus("mandatory")
_HihsmVolHstListDstCU_Type = Integer32
_HihsmVolHstListDstCU_Object = MibTableColumn
hihsmVolHstListDstCU = _HihsmVolHstListDstCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 12),
    _HihsmVolHstListDstCU_Type()
)
hihsmVolHstListDstCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListDstCU.setStatus("mandatory")
_HihsmVolHstListDstLDEV_Type = Integer32
_HihsmVolHstListDstLDEV_Object = MibTableColumn
hihsmVolHstListDstLDEV = _HihsmVolHstListDstLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 4, 5, 2, 1, 13),
    _HihsmVolHstListDstLDEV_Type()
)
hihsmVolHstListDstLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmVolHstListDstLDEV.setStatus("mandatory")
_HihsmManualMigration_ObjectIdentity = ObjectIdentity
hihsmManualMigration = _HihsmManualMigration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6)
)
_HihsmManualVolumeMigrationTable_Object = MibTable
hihsmManualVolumeMigrationTable = _HihsmManualVolumeMigrationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1)
)
if mibBuilder.loadTexts:
    hihsmManualVolumeMigrationTable.setStatus("mandatory")
_HihsmManualVolumeMigrationEntry_Object = MibTableRow
hihsmManualVolumeMigrationEntry = _HihsmManualVolumeMigrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1)
)
hihsmManualVolumeMigrationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmManVolMigSerialNumber"),
    (0, "HDS9900MIB", "hihsmManVolMigSrcCU"),
    (0, "HDS9900MIB", "hihsmManVolMigSrcLDEV"),
)
if mibBuilder.loadTexts:
    hihsmManualVolumeMigrationEntry.setStatus("mandatory")
_HihsmManVolMigSerialNumber_Type = Integer32
_HihsmManVolMigSerialNumber_Object = MibTableColumn
hihsmManVolMigSerialNumber = _HihsmManVolMigSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1, 1),
    _HihsmManVolMigSerialNumber_Type()
)
hihsmManVolMigSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmManVolMigSerialNumber.setStatus("mandatory")
_HihsmManVolMigSrcCU_Type = Integer32
_HihsmManVolMigSrcCU_Object = MibTableColumn
hihsmManVolMigSrcCU = _HihsmManVolMigSrcCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1, 2),
    _HihsmManVolMigSrcCU_Type()
)
hihsmManVolMigSrcCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmManVolMigSrcCU.setStatus("mandatory")
_HihsmManVolMigSrcLDEV_Type = Integer32
_HihsmManVolMigSrcLDEV_Object = MibTableColumn
hihsmManVolMigSrcLDEV = _HihsmManVolMigSrcLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1, 3),
    _HihsmManVolMigSrcLDEV_Type()
)
hihsmManVolMigSrcLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmManVolMigSrcLDEV.setStatus("mandatory")
_HihsmManVolMigDstCU_Type = Integer32
_HihsmManVolMigDstCU_Object = MibTableColumn
hihsmManVolMigDstCU = _HihsmManVolMigDstCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1, 4),
    _HihsmManVolMigDstCU_Type()
)
hihsmManVolMigDstCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmManVolMigDstCU.setStatus("mandatory")
_HihsmManVolMigDstLDEV_Type = Integer32
_HihsmManVolMigDstLDEV_Object = MibTableColumn
hihsmManVolMigDstLDEV = _HihsmManVolMigDstLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1, 5),
    _HihsmManVolMigDstLDEV_Type()
)
hihsmManVolMigDstLDEV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmManVolMigDstLDEV.setStatus("mandatory")
_HihsmManVolMigProgress_Type = Integer32
_HihsmManVolMigProgress_Object = MibTableColumn
hihsmManVolMigProgress = _HihsmManVolMigProgress_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1, 6),
    _HihsmManVolMigProgress_Type()
)
hihsmManVolMigProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmManVolMigProgress.setStatus("mandatory")
_HihsmManVolMigControlStatus_Type = Integer32
_HihsmManVolMigControlStatus_Object = MibTableColumn
hihsmManVolMigControlStatus = _HihsmManVolMigControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 6, 1, 1, 7),
    _HihsmManVolMigControlStatus_Type()
)
hihsmManVolMigControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmManVolMigControlStatus.setStatus("mandatory")
_HihsmMigrationExceptation_ObjectIdentity = ObjectIdentity
hihsmMigrationExceptation = _HihsmMigrationExceptation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7)
)
_HihsmExpectationPGUtilizationTable_Object = MibTable
hihsmExpectationPGUtilizationTable = _HihsmExpectationPGUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1)
)
if mibBuilder.loadTexts:
    hihsmExpectationPGUtilizationTable.setStatus("mandatory")
_HihsmExpectationPGUtilizationEntry_Object = MibTableRow
hihsmExpectationPGUtilizationEntry = _HihsmExpectationPGUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1)
)
hihsmExpectationPGUtilizationEntry.setIndexNames(
    (0, "HDS9900MIB", "hihsmExpPGUtilSerialNumber"),
    (0, "HDS9900MIB", "hihsmExpPGUtilSrcCU"),
    (0, "HDS9900MIB", "hihsmExpPGUtilSrcLDEV"),
    (0, "HDS9900MIB", "hihsmExpPGUtilDstFB4"),
    (0, "HDS9900MIB", "hihsmExpPGUtilDstPG"),
)
if mibBuilder.loadTexts:
    hihsmExpectationPGUtilizationEntry.setStatus("mandatory")
_HihsmExpPGUtilSerialNumber_Type = Integer32
_HihsmExpPGUtilSerialNumber_Object = MibTableColumn
hihsmExpPGUtilSerialNumber = _HihsmExpPGUtilSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1, 1),
    _HihsmExpPGUtilSerialNumber_Type()
)
hihsmExpPGUtilSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmExpPGUtilSerialNumber.setStatus("mandatory")
_HihsmExpPGUtilSrcCU_Type = Integer32
_HihsmExpPGUtilSrcCU_Object = MibTableColumn
hihsmExpPGUtilSrcCU = _HihsmExpPGUtilSrcCU_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1, 2),
    _HihsmExpPGUtilSrcCU_Type()
)
hihsmExpPGUtilSrcCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmExpPGUtilSrcCU.setStatus("mandatory")
_HihsmExpPGUtilSrcLDEV_Type = Integer32
_HihsmExpPGUtilSrcLDEV_Object = MibTableColumn
hihsmExpPGUtilSrcLDEV = _HihsmExpPGUtilSrcLDEV_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1, 3),
    _HihsmExpPGUtilSrcLDEV_Type()
)
hihsmExpPGUtilSrcLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmExpPGUtilSrcLDEV.setStatus("mandatory")
_HihsmExpPGUtilDstFB4_Type = Integer32
_HihsmExpPGUtilDstFB4_Object = MibTableColumn
hihsmExpPGUtilDstFB4 = _HihsmExpPGUtilDstFB4_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1, 4),
    _HihsmExpPGUtilDstFB4_Type()
)
hihsmExpPGUtilDstFB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmExpPGUtilDstFB4.setStatus("mandatory")
_HihsmExpPGUtilDstPG_Type = Integer32
_HihsmExpPGUtilDstPG_Object = MibTableColumn
hihsmExpPGUtilDstPG = _HihsmExpPGUtilDstPG_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1, 5),
    _HihsmExpPGUtilDstPG_Type()
)
hihsmExpPGUtilDstPG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmExpPGUtilDstPG.setStatus("mandatory")
_HihsmExpPGUtilData_Type = DisplayString
_HihsmExpPGUtilData_Object = MibTableColumn
hihsmExpPGUtilData = _HihsmExpPGUtilData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1, 6),
    _HihsmExpPGUtilData_Type()
)
hihsmExpPGUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hihsmExpPGUtilData.setStatus("mandatory")
_HihsmExpPGUtilControlStatus_Type = Integer32
_HihsmExpPGUtilControlStatus_Object = MibTableColumn
hihsmExpPGUtilControlStatus = _HihsmExpPGUtilControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 20, 7, 1, 1, 7),
    _HihsmExpPGUtilControlStatus_Type()
)
hihsmExpPGUtilControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hihsmExpPGUtilControlStatus.setStatus("mandatory")
_RaidExMibCSW_ObjectIdentity = ObjectIdentity
raidExMibCSW = _RaidExMibCSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 21)
)
_RaidExMibCSWConfigurationTable_Object = MibTable
raidExMibCSWConfigurationTable = _RaidExMibCSWConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 21, 1)
)
if mibBuilder.loadTexts:
    raidExMibCSWConfigurationTable.setStatus("mandatory")
_RaidExMibCSWConfigurationEntry_Object = MibTableRow
raidExMibCSWConfigurationEntry = _RaidExMibCSWConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 21, 1, 1)
)
raidExMibCSWConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "cswSerialNumber"),
    (0, "HDS9900MIB", "cswClusterNumber"),
    (0, "HDS9900MIB", "cswNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCSWConfigurationEntry.setStatus("mandatory")
_CswSerialNumber_Type = Integer32
_CswSerialNumber_Object = MibTableColumn
cswSerialNumber = _CswSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 21, 1, 1, 1),
    _CswSerialNumber_Type()
)
cswSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswSerialNumber.setStatus("mandatory")
_CswClusterNumber_Type = Integer32
_CswClusterNumber_Object = MibTableColumn
cswClusterNumber = _CswClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 21, 1, 1, 2),
    _CswClusterNumber_Type()
)
cswClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswClusterNumber.setStatus("mandatory")
_CswNumber_Type = Integer32
_CswNumber_Object = MibTableColumn
cswNumber = _CswNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 21, 1, 1, 3),
    _CswNumber_Type()
)
cswNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswNumber.setStatus("mandatory")
_CswDisplayName_Type = DisplayString
_CswDisplayName_Object = MibTableColumn
cswDisplayName = _CswDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 21, 1, 1, 4),
    _CswDisplayName_Type()
)
cswDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswDisplayName.setStatus("mandatory")
_RaidExMibSharedMemory_ObjectIdentity = ObjectIdentity
raidExMibSharedMemory = _RaidExMibSharedMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 22)
)
_RaidExMibSMConfigurationTable_Object = MibTable
raidExMibSMConfigurationTable = _RaidExMibSMConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    raidExMibSMConfigurationTable.setStatus("mandatory")
_RaidExMibSMConfigurationEntry_Object = MibTableRow
raidExMibSMConfigurationEntry = _RaidExMibSMConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 22, 1, 1)
)
raidExMibSMConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "smSerialNumber"),
    (0, "HDS9900MIB", "smClusterNumber"),
)
if mibBuilder.loadTexts:
    raidExMibSMConfigurationEntry.setStatus("mandatory")
_SmSerialNumber_Type = Integer32
_SmSerialNumber_Object = MibTableColumn
smSerialNumber = _SmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 22, 1, 1, 1),
    _SmSerialNumber_Type()
)
smSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSerialNumber.setStatus("mandatory")
_SmClusterNumber_Type = Integer32
_SmClusterNumber_Object = MibTableColumn
smClusterNumber = _SmClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 22, 1, 1, 2),
    _SmClusterNumber_Type()
)
smClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smClusterNumber.setStatus("mandatory")
_SmDisplayName_Type = DisplayString
_SmDisplayName_Object = MibTableColumn
smDisplayName = _SmDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 22, 1, 1, 3),
    _SmDisplayName_Type()
)
smDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smDisplayName.setStatus("mandatory")
_RaidExMibCacheMemory_ObjectIdentity = ObjectIdentity
raidExMibCacheMemory = _RaidExMibCacheMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 23)
)
_RaidExMibCacheConfigurationTable_Object = MibTable
raidExMibCacheConfigurationTable = _RaidExMibCacheConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    raidExMibCacheConfigurationTable.setStatus("mandatory")
_RaidExMibCacheConfigurationEntry_Object = MibTableRow
raidExMibCacheConfigurationEntry = _RaidExMibCacheConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 23, 1, 1)
)
raidExMibCacheConfigurationEntry.setIndexNames(
    (0, "HDS9900MIB", "cacheConfSerialNumber"),
    (0, "HDS9900MIB", "cacheConfClusterNumber"),
    (0, "HDS9900MIB", "cacheConfCacheNumber"),
)
if mibBuilder.loadTexts:
    raidExMibCacheConfigurationEntry.setStatus("mandatory")
_CacheConfSerialNumber_Type = Integer32
_CacheConfSerialNumber_Object = MibTableColumn
cacheConfSerialNumber = _CacheConfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 23, 1, 1, 1),
    _CacheConfSerialNumber_Type()
)
cacheConfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheConfSerialNumber.setStatus("mandatory")
_CacheConfClusterNumber_Type = Integer32
_CacheConfClusterNumber_Object = MibTableColumn
cacheConfClusterNumber = _CacheConfClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 23, 1, 1, 2),
    _CacheConfClusterNumber_Type()
)
cacheConfClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheConfClusterNumber.setStatus("mandatory")
_CacheConfCacheNumber_Type = Integer32
_CacheConfCacheNumber_Object = MibTableColumn
cacheConfCacheNumber = _CacheConfCacheNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 23, 1, 1, 3),
    _CacheConfCacheNumber_Type()
)
cacheConfCacheNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheConfCacheNumber.setStatus("mandatory")
_CacheConfDisplayName_Type = DisplayString
_CacheConfDisplayName_Object = MibTableColumn
cacheConfDisplayName = _CacheConfDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 23, 1, 1, 4),
    _CacheConfDisplayName_Type()
)
cacheConfDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheConfDisplayName.setStatus("mandatory")
_RaidExMibPortControlConfiguration_ObjectIdentity = ObjectIdentity
raidExMibPortControlConfiguration = _RaidExMibPortControlConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24)
)
_RaidExMibPortControlSwitchTable_Object = MibTable
raidExMibPortControlSwitchTable = _RaidExMibPortControlSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 1)
)
if mibBuilder.loadTexts:
    raidExMibPortControlSwitchTable.setStatus("mandatory")
_RaidExMibPortControlSwitchEntry_Object = MibTableRow
raidExMibPortControlSwitchEntry = _RaidExMibPortControlSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 1, 1)
)
raidExMibPortControlSwitchEntry.setIndexNames(
    (0, "HDS9900MIB", "portControlSwitchSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibPortControlSwitchEntry.setStatus("mandatory")
_PortControlSwitchSerialNumber_Type = Integer32
_PortControlSwitchSerialNumber_Object = MibTableColumn
portControlSwitchSerialNumber = _PortControlSwitchSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 1, 1, 1),
    _PortControlSwitchSerialNumber_Type()
)
portControlSwitchSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portControlSwitchSerialNumber.setStatus("mandatory")
_PortControlSwitchOnOff_Type = Integer32
_PortControlSwitchOnOff_Object = MibTableColumn
portControlSwitchOnOff = _PortControlSwitchOnOff_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 1, 1, 2),
    _PortControlSwitchOnOff_Type()
)
portControlSwitchOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlSwitchOnOff.setStatus("mandatory")
_PortControlSwitchStatus_Type = Integer32
_PortControlSwitchStatus_Object = MibTableColumn
portControlSwitchStatus = _PortControlSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 1, 1, 3),
    _PortControlSwitchStatus_Type()
)
portControlSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlSwitchStatus.setStatus("mandatory")
_RaidExMibPortControlSetUpTable_Object = MibTable
raidExMibPortControlSetUpTable = _RaidExMibPortControlSetUpTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2)
)
if mibBuilder.loadTexts:
    raidExMibPortControlSetUpTable.setStatus("mandatory")
_RaidExMibPortControlSetUpEntry_Object = MibTableRow
raidExMibPortControlSetUpEntry = _RaidExMibPortControlSetUpEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2, 1)
)
raidExMibPortControlSetUpEntry.setIndexNames(
    (0, "HDS9900MIB", "portControlSetUpSerialNumber"),
    (0, "HDS9900MIB", "portControlSetUpPortID"),
)
if mibBuilder.loadTexts:
    raidExMibPortControlSetUpEntry.setStatus("mandatory")
_PortControlSetUpSerialNumber_Type = Integer32
_PortControlSetUpSerialNumber_Object = MibTableColumn
portControlSetUpSerialNumber = _PortControlSetUpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2, 1, 1),
    _PortControlSetUpSerialNumber_Type()
)
portControlSetUpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portControlSetUpSerialNumber.setStatus("mandatory")
_PortControlSetUpPortID_Type = Integer32
_PortControlSetUpPortID_Object = MibTableColumn
portControlSetUpPortID = _PortControlSetUpPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2, 1, 2),
    _PortControlSetUpPortID_Type()
)
portControlSetUpPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlSetUpPortID.setStatus("mandatory")
_PortControlSetUpControlIndex_Type = Integer32
_PortControlSetUpControlIndex_Object = MibTableColumn
portControlSetUpControlIndex = _PortControlSetUpControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2, 1, 3),
    _PortControlSetUpControlIndex_Type()
)
portControlSetUpControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlSetUpControlIndex.setStatus("mandatory")
_PortControlSetUpDisplayName_Type = DisplayString
_PortControlSetUpDisplayName_Object = MibTableColumn
portControlSetUpDisplayName = _PortControlSetUpDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2, 1, 4),
    _PortControlSetUpDisplayName_Type()
)
portControlSetUpDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlSetUpDisplayName.setStatus("mandatory")
_PortControlSetUpSetting_Type = Integer32
_PortControlSetUpSetting_Object = MibTableColumn
portControlSetUpSetting = _PortControlSetUpSetting_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2, 1, 5),
    _PortControlSetUpSetting_Type()
)
portControlSetUpSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlSetUpSetting.setStatus("mandatory")
_PortControlSetUpStatus_Type = Integer32
_PortControlSetUpStatus_Object = MibTableColumn
portControlSetUpStatus = _PortControlSetUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 2, 1, 6),
    _PortControlSetUpStatus_Type()
)
portControlSetUpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portControlSetUpStatus.setStatus("mandatory")
_RaidExMibPortControlParameter_ObjectIdentity = ObjectIdentity
raidExMibPortControlParameter = _RaidExMibPortControlParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3)
)
_RaidExMibPortParameterTable_Object = MibTable
raidExMibPortParameterTable = _RaidExMibPortParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1)
)
if mibBuilder.loadTexts:
    raidExMibPortParameterTable.setStatus("mandatory")
_RaidExMibPortParameterEntry_Object = MibTableRow
raidExMibPortParameterEntry = _RaidExMibPortParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1)
)
raidExMibPortParameterEntry.setIndexNames(
    (0, "HDS9900MIB", "portPrmSerialNumber"),
    (0, "HDS9900MIB", "portPrmPortID"),
    (0, "HDS9900MIB", "portPrmControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibPortParameterEntry.setStatus("mandatory")
_PortPrmSerialNumber_Type = Integer32
_PortPrmSerialNumber_Object = MibTableColumn
portPrmSerialNumber = _PortPrmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 1),
    _PortPrmSerialNumber_Type()
)
portPrmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrmSerialNumber.setStatus("mandatory")
_PortPrmPortID_Type = Integer32
_PortPrmPortID_Object = MibTableColumn
portPrmPortID = _PortPrmPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 2),
    _PortPrmPortID_Type()
)
portPrmPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrmPortID.setStatus("mandatory")
_PortPrmControlIndex_Type = Integer32
_PortPrmControlIndex_Object = MibTableColumn
portPrmControlIndex = _PortPrmControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 3),
    _PortPrmControlIndex_Type()
)
portPrmControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrmControlIndex.setStatus("mandatory")
_PortPrmDisplayName_Type = DisplayString
_PortPrmDisplayName_Object = MibTableColumn
portPrmDisplayName = _PortPrmDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 4),
    _PortPrmDisplayName_Type()
)
portPrmDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrmDisplayName.setStatus("mandatory")
_PortPrmSetting_Type = Integer32
_PortPrmSetting_Object = MibTableColumn
portPrmSetting = _PortPrmSetting_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 5),
    _PortPrmSetting_Type()
)
portPrmSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrmSetting.setStatus("mandatory")
_PortPrmPrioIOPS_Type = Integer32
_PortPrmPrioIOPS_Object = MibTableColumn
portPrmPrioIOPS = _PortPrmPrioIOPS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 6),
    _PortPrmPrioIOPS_Type()
)
portPrmPrioIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrmPrioIOPS.setStatus("mandatory")
_PortPrmPrioMBS_Type = Integer32
_PortPrmPrioMBS_Object = MibTableColumn
portPrmPrioMBS = _PortPrmPrioMBS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 7),
    _PortPrmPrioMBS_Type()
)
portPrmPrioMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrmPrioMBS.setStatus("mandatory")
_PortNPrmnPrioIOPS_Type = Integer32
_PortNPrmnPrioIOPS_Object = MibTableColumn
portNPrmnPrioIOPS = _PortNPrmnPrioIOPS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 8),
    _PortNPrmnPrioIOPS_Type()
)
portNPrmnPrioIOPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNPrmnPrioIOPS.setStatus("mandatory")
_PortNPrmnPrioMBS_Type = Integer32
_PortNPrmnPrioMBS_Object = MibTableColumn
portNPrmnPrioMBS = _PortNPrmnPrioMBS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 9),
    _PortNPrmnPrioMBS_Type()
)
portNPrmnPrioMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portNPrmnPrioMBS.setStatus("mandatory")
_PortPrmThreshold_Type = Integer32
_PortPrmThreshold_Object = MibTableColumn
portPrmThreshold = _PortPrmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 10),
    _PortPrmThreshold_Type()
)
portPrmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPrmThreshold.setStatus("mandatory")
_PortPrmStatus_Type = Integer32
_PortPrmStatus_Object = MibTableColumn
portPrmStatus = _PortPrmStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 1, 1, 11),
    _PortPrmStatus_Type()
)
portPrmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPrmStatus.setStatus("mandatory")
_RaidExMibPrioAllPortParameterTable_Object = MibTable
raidExMibPrioAllPortParameterTable = _RaidExMibPrioAllPortParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 2)
)
if mibBuilder.loadTexts:
    raidExMibPrioAllPortParameterTable.setStatus("mandatory")
_RaidExMibPrioAllPortParameterEntry_Object = MibTableRow
raidExMibPrioAllPortParameterEntry = _RaidExMibPrioAllPortParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 2, 1)
)
raidExMibPrioAllPortParameterEntry.setIndexNames(
    (0, "HDS9900MIB", "prioAllPortPrmSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibPrioAllPortParameterEntry.setStatus("mandatory")
_PrioAllPortPrmSerialNumber_Type = Integer32
_PrioAllPortPrmSerialNumber_Object = MibTableColumn
prioAllPortPrmSerialNumber = _PrioAllPortPrmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 2, 1, 1),
    _PrioAllPortPrmSerialNumber_Type()
)
prioAllPortPrmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioAllPortPrmSerialNumber.setStatus("mandatory")
_PrioAllPortPrmPrioIOPS_Type = Integer32
_PrioAllPortPrmPrioIOPS_Object = MibTableColumn
prioAllPortPrmPrioIOPS = _PrioAllPortPrmPrioIOPS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 2, 1, 2),
    _PrioAllPortPrmPrioIOPS_Type()
)
prioAllPortPrmPrioIOPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioAllPortPrmPrioIOPS.setStatus("mandatory")
_PrioAllPortPrmPrioMBS_Type = Integer32
_PrioAllPortPrmPrioMBS_Object = MibTableColumn
prioAllPortPrmPrioMBS = _PrioAllPortPrmPrioMBS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 2, 1, 3),
    _PrioAllPortPrmPrioMBS_Type()
)
prioAllPortPrmPrioMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioAllPortPrmPrioMBS.setStatus("mandatory")
_PrioAllPortPrmThreshold_Type = Integer32
_PrioAllPortPrmThreshold_Object = MibTableColumn
prioAllPortPrmThreshold = _PrioAllPortPrmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 2, 1, 4),
    _PrioAllPortPrmThreshold_Type()
)
prioAllPortPrmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioAllPortPrmThreshold.setStatus("mandatory")
_PrioAllPortPrmStatus_Type = Integer32
_PrioAllPortPrmStatus_Object = MibTableColumn
prioAllPortPrmStatus = _PrioAllPortPrmStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 2, 1, 5),
    _PrioAllPortPrmStatus_Type()
)
prioAllPortPrmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioAllPortPrmStatus.setStatus("mandatory")
_RaidExMibAllPortParameterTable_Object = MibTable
raidExMibAllPortParameterTable = _RaidExMibAllPortParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 3)
)
if mibBuilder.loadTexts:
    raidExMibAllPortParameterTable.setStatus("mandatory")
_RaidExMibAllPortParameterEntry_Object = MibTableRow
raidExMibAllPortParameterEntry = _RaidExMibAllPortParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 3, 1)
)
raidExMibAllPortParameterEntry.setIndexNames(
    (0, "HDS9900MIB", "allPortPrmSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibAllPortParameterEntry.setStatus("mandatory")
_AllPortPrmSerialNumber_Type = Integer32
_AllPortPrmSerialNumber_Object = MibTableColumn
allPortPrmSerialNumber = _AllPortPrmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 3, 1, 1),
    _AllPortPrmSerialNumber_Type()
)
allPortPrmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allPortPrmSerialNumber.setStatus("mandatory")
_AllPortPrmStatus_Type = Integer32
_AllPortPrmStatus_Object = MibTableColumn
allPortPrmStatus = _AllPortPrmStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 3, 3, 1, 2),
    _AllPortPrmStatus_Type()
)
allPortPrmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allPortPrmStatus.setStatus("mandatory")
_RaidExMibRealTimeMonitoringInformation_ObjectIdentity = ObjectIdentity
raidExMibRealTimeMonitoringInformation = _RaidExMibRealTimeMonitoringInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4)
)
_RaidExMibRTMonitoringCntlTable_Object = MibTable
raidExMibRTMonitoringCntlTable = _RaidExMibRTMonitoringCntlTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 1)
)
if mibBuilder.loadTexts:
    raidExMibRTMonitoringCntlTable.setStatus("mandatory")
_RaidExMibRTMonitoringCntlEntry_Object = MibTableRow
raidExMibRTMonitoringCntlEntry = _RaidExMibRTMonitoringCntlEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 1, 1)
)
raidExMibRTMonitoringCntlEntry.setIndexNames(
    (0, "HDS9900MIB", "rTMonitoringCntlSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibRTMonitoringCntlEntry.setStatus("mandatory")
_RTMonitoringCntlSerialNumber_Type = Integer32
_RTMonitoringCntlSerialNumber_Object = MibTableColumn
rTMonitoringCntlSerialNumber = _RTMonitoringCntlSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 1, 1, 1),
    _RTMonitoringCntlSerialNumber_Type()
)
rTMonitoringCntlSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitoringCntlSerialNumber.setStatus("mandatory")
_RTMonitoringCntlStatus_Type = Integer32
_RTMonitoringCntlStatus_Object = MibTableColumn
rTMonitoringCntlStatus = _RTMonitoringCntlStatus_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 1, 1, 2),
    _RTMonitoringCntlStatus_Type()
)
rTMonitoringCntlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rTMonitoringCntlStatus.setStatus("mandatory")
_RaidExMibRTMonitorDataTable_Object = MibTable
raidExMibRTMonitorDataTable = _RaidExMibRTMonitorDataTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2)
)
if mibBuilder.loadTexts:
    raidExMibRTMonitorDataTable.setStatus("mandatory")
_RaidExMibRTMonitorDataEntry_Object = MibTableRow
raidExMibRTMonitorDataEntry = _RaidExMibRTMonitorDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1)
)
raidExMibRTMonitorDataEntry.setIndexNames(
    (0, "HDS9900MIB", "rTMonitorDataSerialNumber"),
    (0, "HDS9900MIB", "rTMonitorDataPortID"),
    (0, "HDS9900MIB", "rTMonitorDataControlIndex"),
)
if mibBuilder.loadTexts:
    raidExMibRTMonitorDataEntry.setStatus("mandatory")
_RTMonitorDataSerialNumber_Type = Integer32
_RTMonitorDataSerialNumber_Object = MibTableColumn
rTMonitorDataSerialNumber = _RTMonitorDataSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 1),
    _RTMonitorDataSerialNumber_Type()
)
rTMonitorDataSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataSerialNumber.setStatus("mandatory")
_RTMonitorDataPortID_Type = Integer32
_RTMonitorDataPortID_Object = MibTableColumn
rTMonitorDataPortID = _RTMonitorDataPortID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 2),
    _RTMonitorDataPortID_Type()
)
rTMonitorDataPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataPortID.setStatus("mandatory")
_RTMonitorDataControlIndex_Type = Integer32
_RTMonitorDataControlIndex_Object = MibTableColumn
rTMonitorDataControlIndex = _RTMonitorDataControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 3),
    _RTMonitorDataControlIndex_Type()
)
rTMonitorDataControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataControlIndex.setStatus("mandatory")
_RTMonitorDataGatheredDate_Type = DisplayString
_RTMonitorDataGatheredDate_Object = MibTableColumn
rTMonitorDataGatheredDate = _RTMonitorDataGatheredDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 4),
    _RTMonitorDataGatheredDate_Type()
)
rTMonitorDataGatheredDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataGatheredDate.setStatus("mandatory")
_RTMonitorDataGatheredTime_Type = DisplayString
_RTMonitorDataGatheredTime_Object = MibTableColumn
rTMonitorDataGatheredTime = _RTMonitorDataGatheredTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 5),
    _RTMonitorDataGatheredTime_Type()
)
rTMonitorDataGatheredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataGatheredTime.setStatus("mandatory")
_RTMonitorDataSetting_Type = Integer32
_RTMonitorDataSetting_Object = MibTableColumn
rTMonitorDataSetting = _RTMonitorDataSetting_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 6),
    _RTMonitorDataSetting_Type()
)
rTMonitorDataSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataSetting.setStatus("mandatory")
_RTMonitorDataIOPSMax_Type = Integer32
_RTMonitorDataIOPSMax_Object = MibTableColumn
rTMonitorDataIOPSMax = _RTMonitorDataIOPSMax_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 7),
    _RTMonitorDataIOPSMax_Type()
)
rTMonitorDataIOPSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataIOPSMax.setStatus("mandatory")
_RTMonitorDataIOPSAve_Type = Integer32
_RTMonitorDataIOPSAve_Object = MibTableColumn
rTMonitorDataIOPSAve = _RTMonitorDataIOPSAve_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 8),
    _RTMonitorDataIOPSAve_Type()
)
rTMonitorDataIOPSAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataIOPSAve.setStatus("mandatory")
_RTMonitorDataIOPSMin_Type = Integer32
_RTMonitorDataIOPSMin_Object = MibTableColumn
rTMonitorDataIOPSMin = _RTMonitorDataIOPSMin_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 9),
    _RTMonitorDataIOPSMin_Type()
)
rTMonitorDataIOPSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataIOPSMin.setStatus("mandatory")
_RTMonitorDataMBSMax_Type = Integer32
_RTMonitorDataMBSMax_Object = MibTableColumn
rTMonitorDataMBSMax = _RTMonitorDataMBSMax_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 10),
    _RTMonitorDataMBSMax_Type()
)
rTMonitorDataMBSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataMBSMax.setStatus("mandatory")
_RTMonitorDataMBSAve_Type = Integer32
_RTMonitorDataMBSAve_Object = MibTableColumn
rTMonitorDataMBSAve = _RTMonitorDataMBSAve_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 11),
    _RTMonitorDataMBSAve_Type()
)
rTMonitorDataMBSAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataMBSAve.setStatus("mandatory")
_RTMonitorDataMBSMin_Type = Integer32
_RTMonitorDataMBSMin_Object = MibTableColumn
rTMonitorDataMBSMin = _RTMonitorDataMBSMin_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 2, 1, 12),
    _RTMonitorDataMBSMin_Type()
)
rTMonitorDataMBSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTMonitorDataMBSMin.setStatus("mandatory")
_RaidExMibPrioRTMonitorDataTable_Object = MibTable
raidExMibPrioRTMonitorDataTable = _RaidExMibPrioRTMonitorDataTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3)
)
if mibBuilder.loadTexts:
    raidExMibPrioRTMonitorDataTable.setStatus("mandatory")
_RaidExMibPrioRTMonitorDataEntry_Object = MibTableRow
raidExMibPrioRTMonitorDataEntry = _RaidExMibPrioRTMonitorDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1)
)
raidExMibPrioRTMonitorDataEntry.setIndexNames(
    (0, "HDS9900MIB", "prioRTMonitorDataSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibPrioRTMonitorDataEntry.setStatus("mandatory")
_PrioRTMonitorDataSerialNumber_Type = Integer32
_PrioRTMonitorDataSerialNumber_Object = MibTableColumn
prioRTMonitorDataSerialNumber = _PrioRTMonitorDataSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 1),
    _PrioRTMonitorDataSerialNumber_Type()
)
prioRTMonitorDataSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataSerialNumber.setStatus("mandatory")
_PrioRTMonitorDataGatheredDate_Type = DisplayString
_PrioRTMonitorDataGatheredDate_Object = MibTableColumn
prioRTMonitorDataGatheredDate = _PrioRTMonitorDataGatheredDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 2),
    _PrioRTMonitorDataGatheredDate_Type()
)
prioRTMonitorDataGatheredDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataGatheredDate.setStatus("mandatory")
_PrioRTMonitorDataGatheredTime_Type = DisplayString
_PrioRTMonitorDataGatheredTime_Object = MibTableColumn
prioRTMonitorDataGatheredTime = _PrioRTMonitorDataGatheredTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 3),
    _PrioRTMonitorDataGatheredTime_Type()
)
prioRTMonitorDataGatheredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataGatheredTime.setStatus("mandatory")
_PrioRTMonitorDataIOPSMax_Type = Integer32
_PrioRTMonitorDataIOPSMax_Object = MibTableColumn
prioRTMonitorDataIOPSMax = _PrioRTMonitorDataIOPSMax_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 4),
    _PrioRTMonitorDataIOPSMax_Type()
)
prioRTMonitorDataIOPSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataIOPSMax.setStatus("mandatory")
_PrioRTMonitorDataIOPSAve_Type = Integer32
_PrioRTMonitorDataIOPSAve_Object = MibTableColumn
prioRTMonitorDataIOPSAve = _PrioRTMonitorDataIOPSAve_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 5),
    _PrioRTMonitorDataIOPSAve_Type()
)
prioRTMonitorDataIOPSAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataIOPSAve.setStatus("mandatory")
_PrioRTMonitorDataIOPSMin_Type = Integer32
_PrioRTMonitorDataIOPSMin_Object = MibTableColumn
prioRTMonitorDataIOPSMin = _PrioRTMonitorDataIOPSMin_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 6),
    _PrioRTMonitorDataIOPSMin_Type()
)
prioRTMonitorDataIOPSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataIOPSMin.setStatus("mandatory")
_PrioRTMonitorDataMBSMax_Type = Integer32
_PrioRTMonitorDataMBSMax_Object = MibTableColumn
prioRTMonitorDataMBSMax = _PrioRTMonitorDataMBSMax_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 7),
    _PrioRTMonitorDataMBSMax_Type()
)
prioRTMonitorDataMBSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataMBSMax.setStatus("mandatory")
_PrioRTMonitorDataMBSAve_Type = Integer32
_PrioRTMonitorDataMBSAve_Object = MibTableColumn
prioRTMonitorDataMBSAve = _PrioRTMonitorDataMBSAve_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 8),
    _PrioRTMonitorDataMBSAve_Type()
)
prioRTMonitorDataMBSAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataMBSAve.setStatus("mandatory")
_PrioRTMonitorDataMBSMin_Type = Integer32
_PrioRTMonitorDataMBSMin_Object = MibTableColumn
prioRTMonitorDataMBSMin = _PrioRTMonitorDataMBSMin_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 3, 1, 9),
    _PrioRTMonitorDataMBSMin_Type()
)
prioRTMonitorDataMBSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prioRTMonitorDataMBSMin.setStatus("mandatory")
_RaidExMibNPrioRTMonitorDataTable_Object = MibTable
raidExMibNPrioRTMonitorDataTable = _RaidExMibNPrioRTMonitorDataTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4)
)
if mibBuilder.loadTexts:
    raidExMibNPrioRTMonitorDataTable.setStatus("mandatory")
_RaidExMibNPrioRTMonitorDataEntry_Object = MibTableRow
raidExMibNPrioRTMonitorDataEntry = _RaidExMibNPrioRTMonitorDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1)
)
raidExMibNPrioRTMonitorDataEntry.setIndexNames(
    (0, "HDS9900MIB", "nPrioRTMonitorDataSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibNPrioRTMonitorDataEntry.setStatus("mandatory")
_NPrioRTMonitorDataSerialNumber_Type = Integer32
_NPrioRTMonitorDataSerialNumber_Object = MibTableColumn
nPrioRTMonitorDataSerialNumber = _NPrioRTMonitorDataSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 1),
    _NPrioRTMonitorDataSerialNumber_Type()
)
nPrioRTMonitorDataSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataSerialNumber.setStatus("mandatory")
_NPrioRTMonitorDataGatheredDate_Type = DisplayString
_NPrioRTMonitorDataGatheredDate_Object = MibTableColumn
nPrioRTMonitorDataGatheredDate = _NPrioRTMonitorDataGatheredDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 2),
    _NPrioRTMonitorDataGatheredDate_Type()
)
nPrioRTMonitorDataGatheredDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataGatheredDate.setStatus("mandatory")
_NPrioRTMonitorDataGatheredTime_Type = DisplayString
_NPrioRTMonitorDataGatheredTime_Object = MibTableColumn
nPrioRTMonitorDataGatheredTime = _NPrioRTMonitorDataGatheredTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 3),
    _NPrioRTMonitorDataGatheredTime_Type()
)
nPrioRTMonitorDataGatheredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataGatheredTime.setStatus("mandatory")
_NPrioRTMonitorDataIOPSMax_Type = Integer32
_NPrioRTMonitorDataIOPSMax_Object = MibTableColumn
nPrioRTMonitorDataIOPSMax = _NPrioRTMonitorDataIOPSMax_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 4),
    _NPrioRTMonitorDataIOPSMax_Type()
)
nPrioRTMonitorDataIOPSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataIOPSMax.setStatus("mandatory")
_NPrioRTMonitorDataIOPSAve_Type = Integer32
_NPrioRTMonitorDataIOPSAve_Object = MibTableColumn
nPrioRTMonitorDataIOPSAve = _NPrioRTMonitorDataIOPSAve_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 5),
    _NPrioRTMonitorDataIOPSAve_Type()
)
nPrioRTMonitorDataIOPSAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataIOPSAve.setStatus("mandatory")
_NPrioRTMonitorDataIOPSMin_Type = Integer32
_NPrioRTMonitorDataIOPSMin_Object = MibTableColumn
nPrioRTMonitorDataIOPSMin = _NPrioRTMonitorDataIOPSMin_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 6),
    _NPrioRTMonitorDataIOPSMin_Type()
)
nPrioRTMonitorDataIOPSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataIOPSMin.setStatus("mandatory")
_NPrioRTMonitorDataMBSMax_Type = Integer32
_NPrioRTMonitorDataMBSMax_Object = MibTableColumn
nPrioRTMonitorDataMBSMax = _NPrioRTMonitorDataMBSMax_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 7),
    _NPrioRTMonitorDataMBSMax_Type()
)
nPrioRTMonitorDataMBSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataMBSMax.setStatus("mandatory")
_NPrioRTMonitorDataMBSAve_Type = Integer32
_NPrioRTMonitorDataMBSAve_Object = MibTableColumn
nPrioRTMonitorDataMBSAve = _NPrioRTMonitorDataMBSAve_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 8),
    _NPrioRTMonitorDataMBSAve_Type()
)
nPrioRTMonitorDataMBSAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataMBSAve.setStatus("mandatory")
_NPrioRTMonitorDataMBSMin_Type = Integer32
_NPrioRTMonitorDataMBSMin_Object = MibTableColumn
nPrioRTMonitorDataMBSMin = _NPrioRTMonitorDataMBSMin_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 24, 4, 4, 1, 9),
    _NPrioRTMonitorDataMBSMin_Type()
)
nPrioRTMonitorDataMBSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nPrioRTMonitorDataMBSMin.setStatus("mandatory")
_RaidExMibVersionManagement_ObjectIdentity = ObjectIdentity
raidExMibVersionManagement = _RaidExMibVersionManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50)
)
_MibAllLeafVersionTable_Object = MibTable
mibAllLeafVersionTable = _MibAllLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 1)
)
if mibBuilder.loadTexts:
    mibAllLeafVersionTable.setStatus("mandatory")
_MibAllLeafVersionEntry_Object = MibTableRow
mibAllLeafVersionEntry = _MibAllLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 1, 1)
)
mibAllLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibAllLeafVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibAllLeafVersionEntry.setStatus("mandatory")
_MibAllLeafVersionSerialNumber_Type = Integer32
_MibAllLeafVersionSerialNumber_Object = MibTableColumn
mibAllLeafVersionSerialNumber = _MibAllLeafVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 1, 1, 1),
    _MibAllLeafVersionSerialNumber_Type()
)
mibAllLeafVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibAllLeafVersionSerialNumber.setStatus("mandatory")
_MibAllLeafVersionMIBVersionData_Type = DisplayString
_MibAllLeafVersionMIBVersionData_Object = MibTableColumn
mibAllLeafVersionMIBVersionData = _MibAllLeafVersionMIBVersionData_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 1, 1, 2),
    _MibAllLeafVersionMIBVersionData_Type()
)
mibAllLeafVersionMIBVersionData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibAllLeafVersionMIBVersionData.setStatus("mandatory")
_MibAllLeafVersionMIBVersion_Type = Integer32
_MibAllLeafVersionMIBVersion_Object = MibTableColumn
mibAllLeafVersionMIBVersion = _MibAllLeafVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 1, 1, 3),
    _MibAllLeafVersionMIBVersion_Type()
)
mibAllLeafVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibAllLeafVersionMIBVersion.setStatus("mandatory")
_MibLdevLeafVersionTable_Object = MibTable
mibLdevLeafVersionTable = _MibLdevLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 10)
)
if mibBuilder.loadTexts:
    mibLdevLeafVersionTable.setStatus("mandatory")
_MibLdevLeafVersionEntry_Object = MibTableRow
mibLdevLeafVersionEntry = _MibLdevLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 10, 1)
)
mibLdevLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibLdevVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibLdevLeafVersionEntry.setStatus("mandatory")
_MibLdevVersionSerialNumber_Type = Integer32
_MibLdevVersionSerialNumber_Object = MibTableColumn
mibLdevVersionSerialNumber = _MibLdevVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 10, 1, 1),
    _MibLdevVersionSerialNumber_Type()
)
mibLdevVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibLdevVersionSerialNumber.setStatus("mandatory")
_MibLdevVersionMIBVersion_Type = Integer32
_MibLdevVersionMIBVersion_Object = MibTableColumn
mibLdevVersionMIBVersion = _MibLdevVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 10, 1, 2),
    _MibLdevVersionMIBVersion_Type()
)
mibLdevVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibLdevVersionMIBVersion.setStatus("mandatory")
_MibLdevVersionMIBOID_Type = ObjectIdentifier
_MibLdevVersionMIBOID_Object = MibTableColumn
mibLdevVersionMIBOID = _MibLdevVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 10, 1, 3),
    _MibLdevVersionMIBOID_Type()
)
mibLdevVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibLdevVersionMIBOID.setStatus("mandatory")
_MibLuLeafVersion_ObjectIdentity = ObjectIdentity
mibLuLeafVersion = _MibLuLeafVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11)
)
_MibPortleafVersionTable_Object = MibTable
mibPortleafVersionTable = _MibPortleafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 1)
)
if mibBuilder.loadTexts:
    mibPortleafVersionTable.setStatus("mandatory")
_MibPortleafVersionEntry_Object = MibTableRow
mibPortleafVersionEntry = _MibPortleafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 1, 1)
)
mibPortleafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibPortVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibPortleafVersionEntry.setStatus("mandatory")
_MibPortVersionSerialNumber_Type = Integer32
_MibPortVersionSerialNumber_Object = MibTableColumn
mibPortVersionSerialNumber = _MibPortVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 1, 1, 1),
    _MibPortVersionSerialNumber_Type()
)
mibPortVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPortVersionSerialNumber.setStatus("mandatory")
_MibPortVersionMIBVersion_Type = Integer32
_MibPortVersionMIBVersion_Object = MibTableColumn
mibPortVersionMIBVersion = _MibPortVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 1, 1, 2),
    _MibPortVersionMIBVersion_Type()
)
mibPortVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPortVersionMIBVersion.setStatus("mandatory")
_MibPortVersionMIBOID_Type = ObjectIdentifier
_MibPortVersionMIBOID_Object = MibTableColumn
mibPortVersionMIBOID = _MibPortVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 1, 1, 3),
    _MibPortVersionMIBOID_Type()
)
mibPortVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPortVersionMIBOID.setStatus("mandatory")
_MibPathLeafVersionTable_Object = MibTable
mibPathLeafVersionTable = _MibPathLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 2)
)
if mibBuilder.loadTexts:
    mibPathLeafVersionTable.setStatus("mandatory")
_MibPathLeafVersionEntry_Object = MibTableRow
mibPathLeafVersionEntry = _MibPathLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 2, 1)
)
mibPathLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibPathVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibPathLeafVersionEntry.setStatus("mandatory")
_MibPathVersionSerialNumber_Type = Integer32
_MibPathVersionSerialNumber_Object = MibTableColumn
mibPathVersionSerialNumber = _MibPathVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 2, 1, 1),
    _MibPathVersionSerialNumber_Type()
)
mibPathVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPathVersionSerialNumber.setStatus("mandatory")
_MibPathVersionMIBVersion_Type = Integer32
_MibPathVersionMIBVersion_Object = MibTableColumn
mibPathVersionMIBVersion = _MibPathVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 2, 1, 2),
    _MibPathVersionMIBVersion_Type()
)
mibPathVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPathVersionMIBVersion.setStatus("mandatory")
_MibPathVersionMIBOID_Type = ObjectIdentifier
_MibPathVersionMIBOID_Object = MibTableColumn
mibPathVersionMIBOID = _MibPathVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 2, 1, 3),
    _MibPathVersionMIBOID_Type()
)
mibPathVersionMIBOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibPathVersionMIBOID.setStatus("mandatory")
_MibLuseLeafVersionTable_Object = MibTable
mibLuseLeafVersionTable = _MibLuseLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 3)
)
if mibBuilder.loadTexts:
    mibLuseLeafVersionTable.setStatus("mandatory")
_MibLuseLeafVersionEntry_Object = MibTableRow
mibLuseLeafVersionEntry = _MibLuseLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 3, 1)
)
mibLuseLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibLuseVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibLuseLeafVersionEntry.setStatus("mandatory")
_MibLuseVersionSerialNumber_Type = Integer32
_MibLuseVersionSerialNumber_Object = MibTableColumn
mibLuseVersionSerialNumber = _MibLuseVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 3, 1, 1),
    _MibLuseVersionSerialNumber_Type()
)
mibLuseVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibLuseVersionSerialNumber.setStatus("mandatory")
_MibLuseVersionMIBVersion_Type = Integer32
_MibLuseVersionMIBVersion_Object = MibTableColumn
mibLuseVersionMIBVersion = _MibLuseVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 3, 1, 2),
    _MibLuseVersionMIBVersion_Type()
)
mibLuseVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibLuseVersionMIBVersion.setStatus("mandatory")
_MibLuseVersionMIBOID_Type = ObjectIdentifier
_MibLuseVersionMIBOID_Object = MibTableColumn
mibLuseVersionMIBOID = _MibLuseVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 3, 1, 3),
    _MibLuseVersionMIBOID_Type()
)
mibLuseVersionMIBOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibLuseVersionMIBOID.setStatus("mandatory")
_MibLunsLeafVersionTable_Object = MibTable
mibLunsLeafVersionTable = _MibLunsLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 4)
)
if mibBuilder.loadTexts:
    mibLunsLeafVersionTable.setStatus("mandatory")
_MibLunsLeafVersionEntry_Object = MibTableRow
mibLunsLeafVersionEntry = _MibLunsLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 4, 1)
)
mibLunsLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibLunsVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibLunsLeafVersionEntry.setStatus("mandatory")
_MibLunsVersionSerialNumber_Type = Integer32
_MibLunsVersionSerialNumber_Object = MibTableColumn
mibLunsVersionSerialNumber = _MibLunsVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 4, 1, 1),
    _MibLunsVersionSerialNumber_Type()
)
mibLunsVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibLunsVersionSerialNumber.setStatus("mandatory")
_MibLunsVersionMIBVersion_Type = Integer32
_MibLunsVersionMIBVersion_Object = MibTableColumn
mibLunsVersionMIBVersion = _MibLunsVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 4, 1, 2),
    _MibLunsVersionMIBVersion_Type()
)
mibLunsVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibLunsVersionMIBVersion.setStatus("mandatory")
_MibLunsVersionMIBOID_Type = ObjectIdentifier
_MibLunsVersionMIBOID_Object = MibTableColumn
mibLunsVersionMIBOID = _MibLunsVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 11, 4, 1, 3),
    _MibLunsVersionMIBOID_Type()
)
mibLunsVersionMIBOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibLunsVersionMIBOID.setStatus("mandatory")
_MibDcrLeafVersionTable_Object = MibTable
mibDcrLeafVersionTable = _MibDcrLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 12)
)
if mibBuilder.loadTexts:
    mibDcrLeafVersionTable.setStatus("mandatory")
_MibDcrLeafVersionEntry_Object = MibTableRow
mibDcrLeafVersionEntry = _MibDcrLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 12, 1)
)
mibDcrLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibDcrVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibDcrLeafVersionEntry.setStatus("mandatory")
_MibDcrVersionSerialNumber_Type = Integer32
_MibDcrVersionSerialNumber_Object = MibTableColumn
mibDcrVersionSerialNumber = _MibDcrVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 12, 1, 1),
    _MibDcrVersionSerialNumber_Type()
)
mibDcrVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibDcrVersionSerialNumber.setStatus("mandatory")
_MibDcrVersionMIBVersion_Type = Integer32
_MibDcrVersionMIBVersion_Object = MibTableColumn
mibDcrVersionMIBVersion = _MibDcrVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 12, 1, 2),
    _MibDcrVersionMIBVersion_Type()
)
mibDcrVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibDcrVersionMIBVersion.setStatus("mandatory")
_MibDcrVersionMIBOID_Type = ObjectIdentifier
_MibDcrVersionMIBOID_Object = MibTableColumn
mibDcrVersionMIBOID = _MibDcrVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 12, 1, 3),
    _MibDcrVersionMIBOID_Type()
)
mibDcrVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibDcrVersionMIBOID.setStatus("mandatory")
_MibCvsLeafVersionTable_Object = MibTable
mibCvsLeafVersionTable = _MibCvsLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 13)
)
if mibBuilder.loadTexts:
    mibCvsLeafVersionTable.setStatus("mandatory")
_MibCvsLeafVersionEntry_Object = MibTableRow
mibCvsLeafVersionEntry = _MibCvsLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 13, 1)
)
mibCvsLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibCvsLeafVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibCvsLeafVersionEntry.setStatus("mandatory")
_MibCvsLeafVersionSerialNumber_Type = Integer32
_MibCvsLeafVersionSerialNumber_Object = MibTableColumn
mibCvsLeafVersionSerialNumber = _MibCvsLeafVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 13, 1, 1),
    _MibCvsLeafVersionSerialNumber_Type()
)
mibCvsLeafVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCvsLeafVersionSerialNumber.setStatus("mandatory")
_MibCvsLeafVersionMIBVersion_Type = Integer32
_MibCvsLeafVersionMIBVersion_Object = MibTableColumn
mibCvsLeafVersionMIBVersion = _MibCvsLeafVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 13, 1, 2),
    _MibCvsLeafVersionMIBVersion_Type()
)
mibCvsLeafVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCvsLeafVersionMIBVersion.setStatus("mandatory")
_MibCvsLeafVersionMIBOID_Type = ObjectIdentifier
_MibCvsLeafVersionMIBOID_Object = MibTableColumn
mibCvsLeafVersionMIBOID = _MibCvsLeafVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 13, 1, 3),
    _MibCvsLeafVersionMIBOID_Type()
)
mibCvsLeafVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCvsLeafVersionMIBOID.setStatus("mandatory")
_MibSsidLeafVersionTable_Object = MibTable
mibSsidLeafVersionTable = _MibSsidLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 14)
)
if mibBuilder.loadTexts:
    mibSsidLeafVersionTable.setStatus("mandatory")
_MibSsidLeafVersionEntry_Object = MibTableRow
mibSsidLeafVersionEntry = _MibSsidLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 14, 1)
)
mibSsidLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibSsidVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibSsidLeafVersionEntry.setStatus("mandatory")
_MibSsidVersionSerialNumber_Type = Integer32
_MibSsidVersionSerialNumber_Object = MibTableColumn
mibSsidVersionSerialNumber = _MibSsidVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 14, 1, 1),
    _MibSsidVersionSerialNumber_Type()
)
mibSsidVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibSsidVersionSerialNumber.setStatus("mandatory")
_MibSsidVersionMIBVersion_Type = Integer32
_MibSsidVersionMIBVersion_Object = MibTableColumn
mibSsidVersionMIBVersion = _MibSsidVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 14, 1, 2),
    _MibSsidVersionMIBVersion_Type()
)
mibSsidVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibSsidVersionMIBVersion.setStatus("mandatory")
_MibSsidVersionMIBOID_Type = ObjectIdentifier
_MibSsidVersionMIBOID_Object = MibTableColumn
mibSsidVersionMIBOID = _MibSsidVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 14, 1, 3),
    _MibSsidVersionMIBOID_Type()
)
mibSsidVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibSsidVersionMIBOID.setStatus("mandatory")
_MibEnvLeafVersionTable_Object = MibTable
mibEnvLeafVersionTable = _MibEnvLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 15)
)
if mibBuilder.loadTexts:
    mibEnvLeafVersionTable.setStatus("mandatory")
_MibEnvLeafVersionEntry_Object = MibTableRow
mibEnvLeafVersionEntry = _MibEnvLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 15, 1)
)
mibEnvLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibEnvVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibEnvLeafVersionEntry.setStatus("mandatory")
_MibEnvVersionSerialNumber_Type = Integer32
_MibEnvVersionSerialNumber_Object = MibTableColumn
mibEnvVersionSerialNumber = _MibEnvVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 15, 1, 1),
    _MibEnvVersionSerialNumber_Type()
)
mibEnvVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibEnvVersionSerialNumber.setStatus("mandatory")
_MibEnvVersionMIBVersion_Type = Integer32
_MibEnvVersionMIBVersion_Object = MibTableColumn
mibEnvVersionMIBVersion = _MibEnvVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 15, 1, 2),
    _MibEnvVersionMIBVersion_Type()
)
mibEnvVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibEnvVersionMIBVersion.setStatus("mandatory")
_MibEnvVersionMIBOID_Type = ObjectIdentifier
_MibEnvVersionMIBOID_Object = MibTableColumn
mibEnvVersionMIBOID = _MibEnvVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 15, 1, 3),
    _MibEnvVersionMIBOID_Type()
)
mibEnvVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibEnvVersionMIBOID.setStatus("mandatory")
_MibChaLeafVersionTable_Object = MibTable
mibChaLeafVersionTable = _MibChaLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 16)
)
if mibBuilder.loadTexts:
    mibChaLeafVersionTable.setStatus("mandatory")
_MibChaLeafVersionEntry_Object = MibTableRow
mibChaLeafVersionEntry = _MibChaLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 16, 1)
)
mibChaLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibChaVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibChaLeafVersionEntry.setStatus("mandatory")
_MibChaVersionSerialNumber_Type = Integer32
_MibChaVersionSerialNumber_Object = MibTableColumn
mibChaVersionSerialNumber = _MibChaVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 16, 1, 1),
    _MibChaVersionSerialNumber_Type()
)
mibChaVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibChaVersionSerialNumber.setStatus("mandatory")
_MibChaVersionMIBVersion_Type = Integer32
_MibChaVersionMIBVersion_Object = MibTableColumn
mibChaVersionMIBVersion = _MibChaVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 16, 1, 2),
    _MibChaVersionMIBVersion_Type()
)
mibChaVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibChaVersionMIBVersion.setStatus("mandatory")
_MibChaVersionMIBOID_Type = ObjectIdentifier
_MibChaVersionMIBOID_Object = MibTableColumn
mibChaVersionMIBOID = _MibChaVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 16, 1, 3),
    _MibChaVersionMIBOID_Type()
)
mibChaVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibChaVersionMIBOID.setStatus("mandatory")
_MibDkaLeafVersionTable_Object = MibTable
mibDkaLeafVersionTable = _MibDkaLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 17)
)
if mibBuilder.loadTexts:
    mibDkaLeafVersionTable.setStatus("mandatory")
_MibDkaLeafVersionEntry_Object = MibTableRow
mibDkaLeafVersionEntry = _MibDkaLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 17, 1)
)
mibDkaLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibDkaVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibDkaLeafVersionEntry.setStatus("mandatory")
_MibDkaVersionSerialNumber_Type = Integer32
_MibDkaVersionSerialNumber_Object = MibTableColumn
mibDkaVersionSerialNumber = _MibDkaVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 17, 1, 1),
    _MibDkaVersionSerialNumber_Type()
)
mibDkaVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibDkaVersionSerialNumber.setStatus("mandatory")
_MibDkaVersionMIBVersion_Type = Integer32
_MibDkaVersionMIBVersion_Object = MibTableColumn
mibDkaVersionMIBVersion = _MibDkaVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 17, 1, 2),
    _MibDkaVersionMIBVersion_Type()
)
mibDkaVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibDkaVersionMIBVersion.setStatus("mandatory")
_MibDkaVersionMIBOID_Type = ObjectIdentifier
_MibDkaVersionMIBOID_Object = MibTableColumn
mibDkaVersionMIBOID = _MibDkaVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 17, 1, 3),
    _MibDkaVersionMIBOID_Type()
)
mibDkaVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibDkaVersionMIBOID.setStatus("mandatory")
_MibPgLeafVersionTable_Object = MibTable
mibPgLeafVersionTable = _MibPgLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 18)
)
if mibBuilder.loadTexts:
    mibPgLeafVersionTable.setStatus("mandatory")
_MibPgLeafVersionEntry_Object = MibTableRow
mibPgLeafVersionEntry = _MibPgLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 18, 1)
)
mibPgLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibPgVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibPgLeafVersionEntry.setStatus("mandatory")
_MibPgVersionSerialNumber_Type = Integer32
_MibPgVersionSerialNumber_Object = MibTableColumn
mibPgVersionSerialNumber = _MibPgVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 18, 1, 1),
    _MibPgVersionSerialNumber_Type()
)
mibPgVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPgVersionSerialNumber.setStatus("mandatory")
_MibPgVersionMIBVersion_Type = Integer32
_MibPgVersionMIBVersion_Object = MibTableColumn
mibPgVersionMIBVersion = _MibPgVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 18, 1, 2),
    _MibPgVersionMIBVersion_Type()
)
mibPgVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPgVersionMIBVersion.setStatus("mandatory")
_MibPgVersionMIBOID_Type = ObjectIdentifier
_MibPgVersionMIBOID_Object = MibTableColumn
mibPgVersionMIBOID = _MibPgVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 18, 1, 3),
    _MibPgVersionMIBOID_Type()
)
mibPgVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPgVersionMIBOID.setStatus("mandatory")
_MibHihsmLeafVersionTable_Object = MibTable
mibHihsmLeafVersionTable = _MibHihsmLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 20)
)
if mibBuilder.loadTexts:
    mibHihsmLeafVersionTable.setStatus("mandatory")
_MibHihsmLeafVersionEntry_Object = MibTableRow
mibHihsmLeafVersionEntry = _MibHihsmLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 20, 1)
)
mibHihsmLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibHihsmVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibHihsmLeafVersionEntry.setStatus("mandatory")
_MibHihsmVersionSerialNumber_Type = Integer32
_MibHihsmVersionSerialNumber_Object = MibTableColumn
mibHihsmVersionSerialNumber = _MibHihsmVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 20, 1, 1),
    _MibHihsmVersionSerialNumber_Type()
)
mibHihsmVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibHihsmVersionSerialNumber.setStatus("mandatory")
_MibHihsmVersionMIBVersion_Type = Integer32
_MibHihsmVersionMIBVersion_Object = MibTableColumn
mibHihsmVersionMIBVersion = _MibHihsmVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 20, 1, 2),
    _MibHihsmVersionMIBVersion_Type()
)
mibHihsmVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibHihsmVersionMIBVersion.setStatus("mandatory")
_MibHihsmVersionMIBOID_Type = ObjectIdentifier
_MibHihsmVersionMIBOID_Object = MibTableColumn
mibHihsmVersionMIBOID = _MibHihsmVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 20, 1, 3),
    _MibHihsmVersionMIBOID_Type()
)
mibHihsmVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibHihsmVersionMIBOID.setStatus("mandatory")
_MibCswLeafVersionTable_Object = MibTable
mibCswLeafVersionTable = _MibCswLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 21)
)
if mibBuilder.loadTexts:
    mibCswLeafVersionTable.setStatus("mandatory")
_MibCswLeafVersionEntry_Object = MibTableRow
mibCswLeafVersionEntry = _MibCswLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 21, 1)
)
mibCswLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibCswVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibCswLeafVersionEntry.setStatus("mandatory")
_MibCswVersionSerialNumber_Type = Integer32
_MibCswVersionSerialNumber_Object = MibTableColumn
mibCswVersionSerialNumber = _MibCswVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 21, 1, 1),
    _MibCswVersionSerialNumber_Type()
)
mibCswVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCswVersionSerialNumber.setStatus("mandatory")
_MibCswVersionMIBVersion_Type = Integer32
_MibCswVersionMIBVersion_Object = MibTableColumn
mibCswVersionMIBVersion = _MibCswVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 21, 1, 2),
    _MibCswVersionMIBVersion_Type()
)
mibCswVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCswVersionMIBVersion.setStatus("mandatory")
_MibCswVersionMIBOID_Type = ObjectIdentifier
_MibCswVersionMIBOID_Object = MibTableColumn
mibCswVersionMIBOID = _MibCswVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 21, 1, 3),
    _MibCswVersionMIBOID_Type()
)
mibCswVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCswVersionMIBOID.setStatus("mandatory")
_MibSmLeafVersionTable_Object = MibTable
mibSmLeafVersionTable = _MibSmLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 22)
)
if mibBuilder.loadTexts:
    mibSmLeafVersionTable.setStatus("mandatory")
_MibSmLeafVersionEntry_Object = MibTableRow
mibSmLeafVersionEntry = _MibSmLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 22, 1)
)
mibSmLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibSmLeafVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibSmLeafVersionEntry.setStatus("mandatory")
_MibSmLeafVersionSerialNumber_Type = Integer32
_MibSmLeafVersionSerialNumber_Object = MibTableColumn
mibSmLeafVersionSerialNumber = _MibSmLeafVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 22, 1, 1),
    _MibSmLeafVersionSerialNumber_Type()
)
mibSmLeafVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibSmLeafVersionSerialNumber.setStatus("mandatory")
_MibSmLeafVersionMIBVersion_Type = Integer32
_MibSmLeafVersionMIBVersion_Object = MibTableColumn
mibSmLeafVersionMIBVersion = _MibSmLeafVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 22, 1, 2),
    _MibSmLeafVersionMIBVersion_Type()
)
mibSmLeafVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibSmLeafVersionMIBVersion.setStatus("mandatory")
_MibSmLeafVersionMIBOID_Type = ObjectIdentifier
_MibSmLeafVersionMIBOID_Object = MibTableColumn
mibSmLeafVersionMIBOID = _MibSmLeafVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 22, 1, 3),
    _MibSmLeafVersionMIBOID_Type()
)
mibSmLeafVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibSmLeafVersionMIBOID.setStatus("mandatory")
_MibCmLeafVersionTable_Object = MibTable
mibCmLeafVersionTable = _MibCmLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 23)
)
if mibBuilder.loadTexts:
    mibCmLeafVersionTable.setStatus("mandatory")
_MibCmLeafVersionEntry_Object = MibTableRow
mibCmLeafVersionEntry = _MibCmLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 23, 1)
)
mibCmLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibCmVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibCmLeafVersionEntry.setStatus("mandatory")
_MibCmVersionSerialNumber_Type = Integer32
_MibCmVersionSerialNumber_Object = MibTableColumn
mibCmVersionSerialNumber = _MibCmVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 23, 1, 1),
    _MibCmVersionSerialNumber_Type()
)
mibCmVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCmVersionSerialNumber.setStatus("mandatory")
_MibCmVersionMIBVersion_Type = Integer32
_MibCmVersionMIBVersion_Object = MibTableColumn
mibCmVersionMIBVersion = _MibCmVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 23, 1, 2),
    _MibCmVersionMIBVersion_Type()
)
mibCmVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCmVersionMIBVersion.setStatus("mandatory")
_MibCmVersionMIBOID_Type = ObjectIdentifier
_MibCmVersionMIBOID_Object = MibTableColumn
mibCmVersionMIBOID = _MibCmVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 23, 1, 3),
    _MibCmVersionMIBOID_Type()
)
mibCmVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibCmVersionMIBOID.setStatus("mandatory")
_MibPortControlLeafVersionTable_Object = MibTable
mibPortControlLeafVersionTable = _MibPortControlLeafVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 24)
)
if mibBuilder.loadTexts:
    mibPortControlLeafVersionTable.setStatus("mandatory")
_MibPortControlLeafVersionEntry_Object = MibTableRow
mibPortControlLeafVersionEntry = _MibPortControlLeafVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 24, 1)
)
mibPortControlLeafVersionEntry.setIndexNames(
    (0, "HDS9900MIB", "mibPortControlVersionSerialNumber"),
)
if mibBuilder.loadTexts:
    mibPortControlLeafVersionEntry.setStatus("mandatory")
_MibPortControlVersionSerialNumber_Type = Integer32
_MibPortControlVersionSerialNumber_Object = MibTableColumn
mibPortControlVersionSerialNumber = _MibPortControlVersionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 24, 1, 1),
    _MibPortControlVersionSerialNumber_Type()
)
mibPortControlVersionSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPortControlVersionSerialNumber.setStatus("mandatory")
_MibPortControlVersionMIBVersion_Type = Integer32
_MibPortControlVersionMIBVersion_Object = MibTableColumn
mibPortControlVersionMIBVersion = _MibPortControlVersionMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 24, 1, 2),
    _MibPortControlVersionMIBVersion_Type()
)
mibPortControlVersionMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPortControlVersionMIBVersion.setStatus("mandatory")
_MibPortControlVersionMIBOID_Type = ObjectIdentifier
_MibPortControlVersionMIBOID_Object = MibTableColumn
mibPortControlVersionMIBOID = _MibPortControlVersionMIBOID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 50, 24, 1, 3),
    _MibPortControlVersionMIBOID_Type()
)
mibPortControlVersionMIBOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibPortControlVersionMIBOID.setStatus("mandatory")

# Managed Objects groups


# Notification objects

raidEventUserAcute = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 1)
)
raidEventUserAcute.setObjects(
      *(("HDS9900MIB", "eventTrapSerialNumber"),
        ("HDS9900MIB", "eventTrapNickname"),
        ("HDS9900MIB", "eventTrapREFCODE"),
        ("HDS9900MIB", "eventTrapPartsID"))
)
if mibBuilder.loadTexts:
    raidEventUserAcute.setStatus(
        ""
    )

raidEventUserSerious = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 2)
)
raidEventUserSerious.setObjects(
      *(("HDS9900MIB", "eventTrapSerialNumber"),
        ("HDS9900MIB", "eventTrapNickname"),
        ("HDS9900MIB", "eventTrapREFCODE"),
        ("HDS9900MIB", "eventTrapPartsID"))
)
if mibBuilder.loadTexts:
    raidEventUserSerious.setStatus(
        ""
    )

raidEventUserModerate = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 3)
)
raidEventUserModerate.setObjects(
      *(("HDS9900MIB", "eventTrapSerialNumber"),
        ("HDS9900MIB", "eventTrapNickname"),
        ("HDS9900MIB", "eventTrapREFCODE"),
        ("HDS9900MIB", "eventTrapPartsID"))
)
if mibBuilder.loadTexts:
    raidEventUserModerate.setStatus(
        ""
    )

raidEventUserService = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 4)
)
raidEventUserService.setObjects(
      *(("HDS9900MIB", "eventTrapSerialNumber"),
        ("HDS9900MIB", "eventTrapNickname"),
        ("HDS9900MIB", "eventTrapREFCODE"),
        ("HDS9900MIB", "eventTrapPartsID"))
)
if mibBuilder.loadTexts:
    raidEventUserService.setStatus(
        ""
    )

raidEventCommandFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 100)
)
raidEventCommandFinished.setObjects(
      *(("HDS9900MIB", "trapCommandSerialNumber"),
        ("HDS9900MIB", "trapCommandManagerName"),
        ("HDS9900MIB", "trapCommandKind"),
        ("HDS9900MIB", "trapCommandStatus"))
)
if mibBuilder.loadTexts:
    raidEventCommandFinished.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDS9900MIB",
    **{"hitachi": hitachi,
       "system": system,
       "storage": storage,
       "raid": raid,
       "raidDummy": raidDummy,
       "raidRoot": raidRoot,
       "raidEventUserAcute": raidEventUserAcute,
       "raidEventUserSerious": raidEventUserSerious,
       "raidEventUserModerate": raidEventUserModerate,
       "raidEventUserService": raidEventUserService,
       "raidEventCommandFinished": raidEventCommandFinished,
       "eventTrapSerialNumber": eventTrapSerialNumber,
       "eventTrapNickname": eventTrapNickname,
       "eventTrapREFCODE": eventTrapREFCODE,
       "eventTrapPartsID": eventTrapPartsID,
       "raidEventCommandTable": raidEventCommandTable,
       "raidEventCommandEntry": raidEventCommandEntry,
       "trapCommandSerialNumber": trapCommandSerialNumber,
       "trapCommandManagerName": trapCommandManagerName,
       "trapCommandKind": trapCommandKind,
       "trapCommandStatus": trapCommandStatus,
       "systemExMib": systemExMib,
       "storageExMib": storageExMib,
       "raidExMib": raidExMib,
       "raidExMibDummy": raidExMibDummy,
       "raidExMibRoot": raidExMibRoot,
       "raidExMibName": raidExMibName,
       "raidExMibVersion": raidExMibVersion,
       "raidExMibAgentVersion": raidExMibAgentVersion,
       "raidExMibDkcCount": raidExMibDkcCount,
       "raidExMibRaidListTable": raidExMibRaidListTable,
       "raidExMibRaidListEntry": raidExMibRaidListEntry,
       "raidlistSerialNumber": raidlistSerialNumber,
       "raidlistMibNickName": raidlistMibNickName,
       "raidlistDKCMainVersion": raidlistDKCMainVersion,
       "raidlistDKCProductName": raidlistDKCProductName,
       "raidExMibDKCHWTable": raidExMibDKCHWTable,
       "raidExMibDKCHWEntry": raidExMibDKCHWEntry,
       "dkcRaidListIndexSerialNumber": dkcRaidListIndexSerialNumber,
       "dkcHWProcessor": dkcHWProcessor,
       "dkcHWCSW": dkcHWCSW,
       "dkcHWCache": dkcHWCache,
       "dkcHWSM": dkcHWSM,
       "dkcHWPS": dkcHWPS,
       "dkcHWBattery": dkcHWBattery,
       "dkcHWFan": dkcHWFan,
       "dkcHWEnvironment": dkcHWEnvironment,
       "raidExMibDKUHWTable": raidExMibDKUHWTable,
       "raidExMibDKUHWEntry": raidExMibDKUHWEntry,
       "dkuRaidListIndexSerialNumber": dkuRaidListIndexSerialNumber,
       "dkuHWPS": dkuHWPS,
       "dkuHWFan": dkuHWFan,
       "dkuHWEnvironment": dkuHWEnvironment,
       "dkuHWDrive": dkuHWDrive,
       "raidExMibTrapListTable": raidExMibTrapListTable,
       "raidExMibTrapListEntry": raidExMibTrapListEntry,
       "eventListIndexSerialNumber": eventListIndexSerialNumber,
       "eventListNickname": eventListNickname,
       "eventListIndexRecordNo": eventListIndexRecordNo,
       "eventListREFCODE": eventListREFCODE,
       "raidExMibCommandTable": raidExMibCommandTable,
       "raidExMibCommandEntry": raidExMibCommandEntry,
       "commandSerialNumber": commandSerialNumber,
       "commandManagerName": commandManagerName,
       "commandKind": commandKind,
       "commandStatus": commandStatus,
       "commandProgress": commandProgress,
       "commandRefreshTarget": commandRefreshTarget,
       "commandRefreshTarget2": commandRefreshTarget2,
       "raidExMibLDev": raidExMibLDev,
       "raidExMibLogicalDeviceTable": raidExMibLogicalDeviceTable,
       "raidExMibLogicalDeviceEntry": raidExMibLogicalDeviceEntry,
       "logicalDeviceSerialNumber": logicalDeviceSerialNumber,
       "logicalDeviceCU": logicalDeviceCU,
       "logicalDeviceLDEV": logicalDeviceLDEV,
       "logicalDeviceEmulation": logicalDeviceEmulation,
       "logicalDeviceCylinder": logicalDeviceCylinder,
       "logicalDeviceLUExpand": logicalDeviceLUExpand,
       "logicalDeviceLUPath": logicalDeviceLUPath,
       "logicalDeviceSize": logicalDeviceSize,
       "logicalDeviceLBA": logicalDeviceLBA,
       "logicalDeviceHIHSMReserve": logicalDeviceHIHSMReserve,
       "logicalDeviceControlStatus": logicalDeviceControlStatus,
       "logicalDeviceRAIDLevel": logicalDeviceRAIDLevel,
       "logicalDeviceSlotSize": logicalDeviceSlotSize,
       "raidExMibLUConfiguration": raidExMibLUConfiguration,
       "raidExMibPortTable": raidExMibPortTable,
       "raidExMibPortEntry": raidExMibPortEntry,
       "portSerialNumber": portSerialNumber,
       "portID": portID,
       "portKind": portKind,
       "portHostMode": portHostMode,
       "portFibreAddress": portFibreAddress,
       "portFibreTopology": portFibreTopology,
       "portControlStatus": portControlStatus,
       "portDisplayName": portDisplayName,
       "portWWN": portWWN,
       "raidExMibLU": raidExMibLU,
       "raidExMibLUInformationLUTable": raidExMibLUInformationLUTable,
       "raidExMibLUInformationLUEntry": raidExMibLUInformationLUEntry,
       "luSerialNumber": luSerialNumber,
       "luDeviceCU": luDeviceCU,
       "luDeviceLDEV": luDeviceLDEV,
       "luEmuID": luEmuID,
       "luCount": luCount,
       "luSize": luSize,
       "luPath": luPath,
       "luCommandDev": luCommandDev,
       "luControlStatus": luControlStatus,
       "raidExMibLUPathTable": raidExMibLUPathTable,
       "raidExMibLUPathEntry": raidExMibLUPathEntry,
       "luPathSerialNumber": luPathSerialNumber,
       "luPathControlIndex": luPathControlIndex,
       "luPathPortID": luPathPortID,
       "luPathSCSIID": luPathSCSIID,
       "luPathLUN": luPathLUN,
       "luPathDeviceCU": luPathDeviceCU,
       "luPathDeviceLDEV": luPathDeviceLDEV,
       "luPathControlStatus": luPathControlStatus,
       "raidExMibLUSE": raidExMibLUSE,
       "raidExMibLUSEStructureTable": raidExMibLUSEStructureTable,
       "raidExMibLUSEStructureEntry": raidExMibLUSEStructureEntry,
       "luSEStructSerialNumber": luSEStructSerialNumber,
       "luSEStructControlIndex": luSEStructControlIndex,
       "luSEStructOffset": luSEStructOffset,
       "luSEStructTopDeviceCU": luSEStructTopDeviceCU,
       "luSEStructTopDeviceLDEV": luSEStructTopDeviceLDEV,
       "luSEStructDeviceCU": luSEStructDeviceCU,
       "luSEStructDeviceLDEV": luSEStructDeviceLDEV,
       "luSEStructControlStatus": luSEStructControlStatus,
       "raidExMibLUNS": raidExMibLUNS,
       "raidExMibLUNSSwitchTable": raidExMibLUNSSwitchTable,
       "raidExMibLUNSSwitchEntry": raidExMibLUNSSwitchEntry,
       "switchSerialNumber": switchSerialNumber,
       "switchPortID": switchPortID,
       "switchOnOff": switchOnOff,
       "switchControlStatus": switchControlStatus,
       "raidExMibLUNSWWNTable": raidExMibLUNSWWNTable,
       "raidExMibLUNSWWNEntry": raidExMibLUNSWWNEntry,
       "wwnSerialNumber": wwnSerialNumber,
       "wwnPortID": wwnPortID,
       "wwnControlIndex": wwnControlIndex,
       "wwnWWN": wwnWWN,
       "wwnID": wwnID,
       "wwnNickname": wwnNickname,
       "wwnUseNickname": wwnUseNickname,
       "wwnControlStatus": wwnControlStatus,
       "raidExMibLUNSWWNGroupTable": raidExMibLUNSWWNGroupTable,
       "raidExMibLUNSWWNGroupEntry": raidExMibLUNSWWNGroupEntry,
       "wwnGroupSerialNumber": wwnGroupSerialNumber,
       "wwnGroupPortID": wwnGroupPortID,
       "wwnGroupControlIndex": wwnGroupControlIndex,
       "wwnGroupID": wwnGroupID,
       "wwnGroupNickname": wwnGroupNickname,
       "wwnGroupControlStatus": wwnGroupControlStatus,
       "wwnGroupedWWNsVL": wwnGroupedWWNsVL,
       "raidExMibLUNSLUNTable": raidExMibLUNSLUNTable,
       "raidExMibLUNSLUNEntry": raidExMibLUNSLUNEntry,
       "lunSerialNumber": lunSerialNumber,
       "lunPortID": lunPortID,
       "lunLUN": lunLUN,
       "lunControlStatus": lunControlStatus,
       "lunWWNSecurityVL": lunWWNSecurityVL,
       "lunWWNGroupSecurityVL": lunWWNGroupSecurityVL,
       "raidExMibLUNSLUNGroupTable": raidExMibLUNSLUNGroupTable,
       "raidExMibLUNSLUNGroupEntry": raidExMibLUNSLUNGroupEntry,
       "lunGroupSerialNumber": lunGroupSerialNumber,
       "lunGroupPortID": lunGroupPortID,
       "lunGroupControlIndex": lunGroupControlIndex,
       "lunGroupID": lunGroupID,
       "lunGroupNickname": lunGroupNickname,
       "lunGroupControlStatus": lunGroupControlStatus,
       "lunGroupedLUNsVL": lunGroupedLUNsVL,
       "lunGroupWWNSecurityVL": lunGroupWWNSecurityVL,
       "lunGroupWWNGroupSecurityVL": lunGroupWWNGroupSecurityVL,
       "raidExMibDCRConfiguration": raidExMibDCRConfiguration,
       "raidExMibCacheSizeTable": raidExMibCacheSizeTable,
       "raidExMibCacheSizeEntry": raidExMibCacheSizeEntry,
       "cacheSizeSerialNumber": cacheSizeSerialNumber,
       "cacheSizeTotalCacheSize": cacheSizeTotalCacheSize,
       "cacheSizeUseCacheSize": cacheSizeUseCacheSize,
       "cacheSizeRemainCacheSize": cacheSizeRemainCacheSize,
       "raidExMibCacheDCRTable": raidExMibCacheDCRTable,
       "raidExMibCacheDCREntry": raidExMibCacheDCREntry,
       "cacheDCRSerialNumber": cacheDCRSerialNumber,
       "cacheDCRCU": cacheDCRCU,
       "cacheDCRLDEV": cacheDCRLDEV,
       "cacheDCRControlIndex": cacheDCRControlIndex,
       "cacheDCRMode": cacheDCRMode,
       "cacheDCRAllOfDevice": cacheDCRAllOfDevice,
       "cacheDCRStartCylinder": cacheDCRStartCylinder,
       "cacheDCRStartHead": cacheDCRStartHead,
       "cacheDCREndCylinder": cacheDCREndCylinder,
       "cacheDCREndHead": cacheDCREndHead,
       "cacheDCRCylinderSize": cacheDCRCylinderSize,
       "cacheDCRHeadSize": cacheDCRHeadSize,
       "cacheDCRStartLBA": cacheDCRStartLBA,
       "cacheDCREndLBA": cacheDCREndLBA,
       "cacheDCRLBASize": cacheDCRLBASize,
       "cacheDCRControlStatus": cacheDCRControlStatus,
       "raidExMibCVSConfiguration": raidExMibCVSConfiguration,
       "raidExMibCustomizedVolumeTable": raidExMibCustomizedVolumeTable,
       "raidExMibCustomizedVolumeEntry": raidExMibCustomizedVolumeEntry,
       "customizedVolumeSerialNumber": customizedVolumeSerialNumber,
       "customizedVolumeFB4Number": customizedVolumeFB4Number,
       "customizedVolumePGNumber": customizedVolumePGNumber,
       "customizedVolumeCU": customizedVolumeCU,
       "customizedVolumeLDEV": customizedVolumeLDEV,
       "customizedVolumeType": customizedVolumeType,
       "customizedVolumeEmulation": customizedVolumeEmulation,
       "customizedVolumeUserCylinder": customizedVolumeUserCylinder,
       "customizedVolumeUserSize": customizedVolumeUserSize,
       "customizedVolumeControlCylinder": customizedVolumeControlCylinder,
       "customizedVolumeControlSize": customizedVolumeControlSize,
       "customizedVolumeControlStatus": customizedVolumeControlStatus,
       "raidExMibCVSDeletedVolumeTable": raidExMibCVSDeletedVolumeTable,
       "raidExMibCVSDeletedVolumeEntry": raidExMibCVSDeletedVolumeEntry,
       "cvsDVSerialNumber": cvsDVSerialNumber,
       "cvsDVFB4Number": cvsDVFB4Number,
       "cvsDVPGNumber": cvsDVPGNumber,
       "cvsDVControlIndex": cvsDVControlIndex,
       "cvsDVCU": cvsDVCU,
       "cvsDVLDEV": cvsDVLDEV,
       "cvsDVEmulation": cvsDVEmulation,
       "cvsDVCylinder": cvsDVCylinder,
       "cvsDVSize": cvsDVSize,
       "cvsDVControlCylinder": cvsDVControlCylinder,
       "cvsDVControlSize": cvsDVControlSize,
       "cvsDVControlStatus": cvsDVControlStatus,
       "raidExMibCVSFreeSpaceTable": raidExMibCVSFreeSpaceTable,
       "raidExMibCVSFreeSpaceEntry": raidExMibCVSFreeSpaceEntry,
       "cvsFSSerialNumber": cvsFSSerialNumber,
       "cvsFSFB4Number": cvsFSFB4Number,
       "cvsFSPGNumber": cvsFSPGNumber,
       "cvsFSControlIndex": cvsFSControlIndex,
       "cvsFSCylinder": cvsFSCylinder,
       "cvsFSSize": cvsFSSize,
       "raidExMibCVSParityGroupTable": raidExMibCVSParityGroupTable,
       "raidExMibCVSParityGroupEntry": raidExMibCVSParityGroupEntry,
       "cvsPGSerialNumber": cvsPGSerialNumber,
       "cvsPGFB4Number": cvsPGFB4Number,
       "cvsPGPGNumber": cvsPGPGNumber,
       "cvsPGDisplayName": cvsPGDisplayName,
       "cvsPGRAIDType": cvsPGRAIDType,
       "cvsPGDriveType": cvsPGDriveType,
       "cvsPGFreeCylinder": cvsPGFreeCylinder,
       "cvsPGFreeSize": cvsPGFreeSize,
       "cvsPGControlStatus": cvsPGControlStatus,
       "raidExMibCVSCUInfTable": raidExMibCVSCUInfTable,
       "raidExMibCVSCUInfEntry": raidExMibCVSCUInfEntry,
       "cvsCUInfSerialNumber": cvsCUInfSerialNumber,
       "cvsCUInfFreeCUNum": cvsCUInfFreeCUNum,
       "raidExMibSubsystemInfo": raidExMibSubsystemInfo,
       "raidExMibSubsystemIDTable": raidExMibSubsystemIDTable,
       "raidExMibSubsystemIDEntry": raidExMibSubsystemIDEntry,
       "subsystemIDSerialNumber": subsystemIDSerialNumber,
       "subsystemIDCU": subsystemIDCU,
       "subsystemIDStartLDEV": subsystemIDStartLDEV,
       "subsystemIDEndLDEV": subsystemIDEndLDEV,
       "subsystemIDSSID": subsystemIDSSID,
       "subsystemIDControlStatus": subsystemIDControlStatus,
       "raidExMibSSIDBoundaryTable": raidExMibSSIDBoundaryTable,
       "raidExMibSSIDBoundaryEntry": raidExMibSSIDBoundaryEntry,
       "ssidBoundarySerialNumber": ssidBoundarySerialNumber,
       "ssidBoundaryBoundary": ssidBoundaryBoundary,
       "raidExMibEnvironmentInfo": raidExMibEnvironmentInfo,
       "raidExMibTimeZoneDataTable": raidExMibTimeZoneDataTable,
       "raidExMibTimeZoneDataEntry": raidExMibTimeZoneDataEntry,
       "timeZoneSerialNumber": timeZoneSerialNumber,
       "timeZoneID": timeZoneID,
       "raidExMibChannelAdapter": raidExMibChannelAdapter,
       "raidExMibCHAConfigurationTable": raidExMibCHAConfigurationTable,
       "raidExMibCHAConfigurationEntry": raidExMibCHAConfigurationEntry,
       "chaSerialNumber": chaSerialNumber,
       "chaClusterNumber": chaClusterNumber,
       "chaNumber": chaNumber,
       "chaDisplayName": chaDisplayName,
       "chaPackageType": chaPackageType,
       "chaMode": chaMode,
       "chaControlStatus": chaControlStatus,
       "raidExMibCHPConfigurationTable": raidExMibCHPConfigurationTable,
       "raidExMibCHPConfigurationEntry": raidExMibCHPConfigurationEntry,
       "chpSerialNumber": chpSerialNumber,
       "chpClusterNumber": chpClusterNumber,
       "chpCHANumber": chpCHANumber,
       "chpNumber": chpNumber,
       "chpDisplayName": chpDisplayName,
       "raidExMibDiskAdapter": raidExMibDiskAdapter,
       "raidExMibDKAConfigurationTable": raidExMibDKAConfigurationTable,
       "raidExMibDKAConfigurationEntry": raidExMibDKAConfigurationEntry,
       "dkaSerialNumber": dkaSerialNumber,
       "dkaClusterNumber": dkaClusterNumber,
       "dkaNumber": dkaNumber,
       "dkaDisplayName": dkaDisplayName,
       "raidExMibDKPConfigurationTable": raidExMibDKPConfigurationTable,
       "raidExMibDKPConfigurationEntry": raidExMibDKPConfigurationEntry,
       "dkpSerialNumber": dkpSerialNumber,
       "dkpClusterNumber": dkpClusterNumber,
       "dkpDKANumber": dkpDKANumber,
       "dkpNumber": dkpNumber,
       "dkpDisplayName": dkpDisplayName,
       "raidExMibDRRConfigurationTable": raidExMibDRRConfigurationTable,
       "raidExMibDRRConfigurationEntry": raidExMibDRRConfigurationEntry,
       "drrSerialNumber": drrSerialNumber,
       "drrClusterNumber": drrClusterNumber,
       "drrDKANumber": drrDKANumber,
       "drrNumber": drrNumber,
       "drrDisplayName": drrDisplayName,
       "raidExMibParityGroup": raidExMibParityGroup,
       "raidExMibParityGroupListTable": raidExMibParityGroupListTable,
       "raidExMibParityGroupListEntry": raidExMibParityGroupListEntry,
       "pgSerialNumber": pgSerialNumber,
       "pgFB4Number": pgFB4Number,
       "pgNumber": pgNumber,
       "pgDisplayName": pgDisplayName,
       "pgRAIDType": pgRAIDType,
       "pgDriveType": pgDriveType,
       "pgHIHSMFixed": pgHIHSMFixed,
       "pgControlStatus": pgControlStatus,
       "raidExMibParityGroupLDEVTable": raidExMibParityGroupLDEVTable,
       "raidExMibParityGroupLDEVEntry": raidExMibParityGroupLDEVEntry,
       "pgLDEVSerialNumber": pgLDEVSerialNumber,
       "pgLDEVFB4Number": pgLDEVFB4Number,
       "pgLDEVPGNumber": pgLDEVPGNumber,
       "pgLDEVControlIndex": pgLDEVControlIndex,
       "pgLDEVCU": pgLDEVCU,
       "pgLDEVLDEV": pgLDEVLDEV,
       "raidExMibHIHSM": raidExMibHIHSM,
       "hihsmMonitoringParameterTable": hihsmMonitoringParameterTable,
       "hihsmMonitoringParameterEntry": hihsmMonitoringParameterEntry,
       "hihsmMonParamSerialNumber": hihsmMonParamSerialNumber,
       "hihsmMonParamFunctionSwitch": hihsmMonParamFunctionSwitch,
       "hihsmMonParamGatheringTime": hihsmMonParamGatheringTime,
       "hihsmMonParamGatheredFromDate": hihsmMonParamGatheredFromDate,
       "hihsmMonParamGatheredFromTime": hihsmMonParamGatheredFromTime,
       "hihsmMonParamGatheredToDate": hihsmMonParamGatheredToDate,
       "hihsmMonParamGatheredToTime": hihsmMonParamGatheredToTime,
       "hihsmMonParamControlStatus": hihsmMonParamControlStatus,
       "hihsmCalculationParameterTable": hihsmCalculationParameterTable,
       "hihsmCalculationParameterEntry": hihsmCalculationParameterEntry,
       "hihsmCalcParamSerialNumber": hihsmCalcParamSerialNumber,
       "hihsmCalcParamCalcType": hihsmCalcParamCalcType,
       "hihsmCalcParamFromDate": hihsmCalcParamFromDate,
       "hihsmCalcParamFromTime": hihsmCalcParamFromTime,
       "hihsmCalcParamToDate": hihsmCalcParamToDate,
       "hihsmCalcParamToTime": hihsmCalcParamToTime,
       "hihsmCalcParamDataType": hihsmCalcParamDataType,
       "hihsmCalcParamControlStatus": hihsmCalcParamControlStatus,
       "hihsmCalculatedData": hihsmCalculatedData,
       "hihsmCHPUtilizationTable": hihsmCHPUtilizationTable,
       "hihsmCHPUtilizationEntry": hihsmCHPUtilizationEntry,
       "hihsmCHPUtilSerialNumber": hihsmCHPUtilSerialNumber,
       "hihsmCHPUtilClusterNumber": hihsmCHPUtilClusterNumber,
       "hihsmCHPUtilCHANumber": hihsmCHPUtilCHANumber,
       "hihsmCHPUtilCHPNumber": hihsmCHPUtilCHPNumber,
       "hihsmCHPUtilData": hihsmCHPUtilData,
       "hihsmDKPUtilizationTable": hihsmDKPUtilizationTable,
       "hihsmDKPUtilizationEntry": hihsmDKPUtilizationEntry,
       "hihsmDKPUtilSerialNumber": hihsmDKPUtilSerialNumber,
       "hihsmDKPUtilClusterNumber": hihsmDKPUtilClusterNumber,
       "hihsmDKPUtilDKANumber": hihsmDKPUtilDKANumber,
       "hihsmDKPUtilDKPNumber": hihsmDKPUtilDKPNumber,
       "hihsmDKPUtilData": hihsmDKPUtilData,
       "hihsmDRRUtilizationTable": hihsmDRRUtilizationTable,
       "hihsmDRRUtilizationEntry": hihsmDRRUtilizationEntry,
       "hihsmDRRUtilSerialNumber": hihsmDRRUtilSerialNumber,
       "hihsmDRRUtilClusterNumber": hihsmDRRUtilClusterNumber,
       "hihsmDRRUtilDKANumber": hihsmDRRUtilDKANumber,
       "hihsmDRRUtilDRRNumber": hihsmDRRUtilDRRNumber,
       "hihsmDRRUtilData": hihsmDRRUtilData,
       "hihsmPGUtilizationTable": hihsmPGUtilizationTable,
       "hihsmPGUtilizationEntry": hihsmPGUtilizationEntry,
       "hihsmPGUtilSerialNumber": hihsmPGUtilSerialNumber,
       "hihsmPGUtilFB4Number": hihsmPGUtilFB4Number,
       "hihsmPGUtilPGNumber": hihsmPGUtilPGNumber,
       "hihsmPGUtilData": hihsmPGUtilData,
       "hihsmLDEVUtilizationTable": hihsmLDEVUtilizationTable,
       "hihsmLDEVUtilizationEntry": hihsmLDEVUtilizationEntry,
       "hihsmLDEVUtilSerialNumber": hihsmLDEVUtilSerialNumber,
       "hihsmLDEVUtilFB4Number": hihsmLDEVUtilFB4Number,
       "hihsmLDEVUtilPGNumber": hihsmLDEVUtilPGNumber,
       "hihsmLDEVUtilCU": hihsmLDEVUtilCU,
       "hihsmLDEVUtilLDEV": hihsmLDEVUtilLDEV,
       "hihsmLDEVUtilData": hihsmLDEVUtilData,
       "hihsmCHAtoCSWUtilizationTable": hihsmCHAtoCSWUtilizationTable,
       "hihsmCHAtoCSWUtilizationEntry": hihsmCHAtoCSWUtilizationEntry,
       "hihsmCHACSWSerialNumber": hihsmCHACSWSerialNumber,
       "hihsmCHACSWCHAClusterNumber": hihsmCHACSWCHAClusterNumber,
       "hihsmCHACSWCHANumber": hihsmCHACSWCHANumber,
       "hihsmCHACSWCSWClusterNumber": hihsmCHACSWCSWClusterNumber,
       "hihsmCHACSWCSWNumber": hihsmCHACSWCSWNumber,
       "hihsmCHACSWUtilData": hihsmCHACSWUtilData,
       "hihsmDKAtoCSWUtilizationTable": hihsmDKAtoCSWUtilizationTable,
       "hihsmDKAtoCSWUtilizationEntry": hihsmDKAtoCSWUtilizationEntry,
       "hihsmDKACSWSerialNumber": hihsmDKACSWSerialNumber,
       "hihsmDKACSWDKAClusterNumber": hihsmDKACSWDKAClusterNumber,
       "hihsmDKACSWDKANumber": hihsmDKACSWDKANumber,
       "hihsmDKACSWCSWClusterNumber": hihsmDKACSWCSWClusterNumber,
       "hihsmDKACSWCSWNumber": hihsmDKACSWCSWNumber,
       "hihsmDKACSWUtilData": hihsmDKACSWUtilData,
       "hihsmCSWtoCacheUtilizationTable": hihsmCSWtoCacheUtilizationTable,
       "hihsmCSWtoCacheUtilizationEntry": hihsmCSWtoCacheUtilizationEntry,
       "hihsmCSWCacheSerialNumber": hihsmCSWCacheSerialNumber,
       "hihsmCSWCacheCSWClusterNumber": hihsmCSWCacheCSWClusterNumber,
       "hihsmCSWCacheCSWNumber": hihsmCSWCacheCSWNumber,
       "hihsmCSWCacheCacheClusterNumber": hihsmCSWCacheCacheClusterNumber,
       "hihsmCSWCacheCacheNumber": hihsmCSWCacheCacheNumber,
       "hihsmCSWCacheUtilData": hihsmCSWCacheUtilData,
       "hihsmCHAtoSMUtilizationTable": hihsmCHAtoSMUtilizationTable,
       "hihsmCHAtoSMUtilizationEntry": hihsmCHAtoSMUtilizationEntry,
       "hihsmCHASMSerialNumber": hihsmCHASMSerialNumber,
       "hihsmCHASMCHAClusterNumber": hihsmCHASMCHAClusterNumber,
       "hihsmCHASMCHANumber": hihsmCHASMCHANumber,
       "hihsmCHASMSMClusterNumber": hihsmCHASMSMClusterNumber,
       "hihsmCHASMUtilData": hihsmCHASMUtilData,
       "hihsmDKAtoSMUtilizationTable": hihsmDKAtoSMUtilizationTable,
       "hihsmDKAtoSMUtilizationEntry": hihsmDKAtoSMUtilizationEntry,
       "hihsmDKASMSerialNumber": hihsmDKASMSerialNumber,
       "hihsmDKASMDKAClusterNumber": hihsmDKASMDKAClusterNumber,
       "hihsmDKASMDKANumber": hihsmDKASMDKANumber,
       "hihsmDKASMSMClusterNumber": hihsmDKASMSMClusterNumber,
       "hihsmDKASMUtilData": hihsmDKASMUtilData,
       "hihsmDKCUtilizationTable": hihsmDKCUtilizationTable,
       "hihsmDKCUtilizationEntry": hihsmDKCUtilizationEntry,
       "hihsmDKCUtilSerialNumber": hihsmDKCUtilSerialNumber,
       "hihsmDKCUtilWritePending": hihsmDKCUtilWritePending,
       "hihsmAutomaticMigration": hihsmAutomaticMigration,
       "hihsmAutomaticMigrationParameterTable": hihsmAutomaticMigrationParameterTable,
       "hihsmAutomaticMigrationParameterEntry": hihsmAutomaticMigrationParameterEntry,
       "hihsmAutoParamSerialNumber": hihsmAutoParamSerialNumber,
       "hihsmAutoParamFunctionSwitch": hihsmAutoParamFunctionSwitch,
       "hihsmAutoParamPlanningDay": hihsmAutoParamPlanningDay,
       "hihsmAutoParamIntervalDay": hihsmAutoParamIntervalDay,
       "hihsmAutoParamDayOfWeek": hihsmAutoParamDayOfWeek,
       "hihsmAutoParamUseFromTime": hihsmAutoParamUseFromTime,
       "hihsmAutoParamUseToTime": hihsmAutoParamUseToTime,
       "hihsmAutoParamJudgeMethod": hihsmAutoParamJudgeMethod,
       "hihsmAutoParamHightestPoints": hihsmAutoParamHightestPoints,
       "hihsmAutoParamExecutionTime": hihsmAutoParamExecutionTime,
       "hihsmAutoParamMaxDuration": hihsmAutoParamMaxDuration,
       "hihsmAutoParamMaxUtilization": hihsmAutoParamMaxUtilization,
       "hihsmAutoParamMaxVolumes": hihsmAutoParamMaxVolumes,
       "hihsmAutoParamControlStatus": hihsmAutoParamControlStatus,
       "hihsmAutoParamDayOfMonth": hihsmAutoParamDayOfMonth,
       "hihsmAutomaticMigrationClass": hihsmAutomaticMigrationClass,
       "hihsmAutomaticMigrationClassListTable": hihsmAutomaticMigrationClassListTable,
       "hihsmAutomaticMigrationClassListEntry": hihsmAutomaticMigrationClassListEntry,
       "hihsmClassListSerialNumber": hihsmClassListSerialNumber,
       "hihsmClassListClassNumber": hihsmClassListClassNumber,
       "hihsmClassListDisplayName": hihsmClassListDisplayName,
       "hihsmClassListMaxUtilization": hihsmClassListMaxUtilization,
       "hihsmClassListControlStatus": hihsmClassListControlStatus,
       "hihsmAutomaticMigrationClassPGTable": hihsmAutomaticMigrationClassPGTable,
       "hihsmAutomaticMigrationClassPGEntry": hihsmAutomaticMigrationClassPGEntry,
       "hihsmClassPGSerialNumber": hihsmClassPGSerialNumber,
       "hihsmClassPGClassNumber": hihsmClassPGClassNumber,
       "hihsmClassPGControlIndex": hihsmClassPGControlIndex,
       "hihsmClassPGFB4Number": hihsmClassPGFB4Number,
       "hihsmClassPGPGNumber": hihsmClassPGPGNumber,
       "hihsmAutomaticMigrationPlan": hihsmAutomaticMigrationPlan,
       "hihsmAutomaticMigrationPlanStatusTable": hihsmAutomaticMigrationPlanStatusTable,
       "hihsmAutomaticMigrationPlanStatusEntry": hihsmAutomaticMigrationPlanStatusEntry,
       "hihsmPlanStatusSerialNumber": hihsmPlanStatusSerialNumber,
       "hihsmPlanStatusData": hihsmPlanStatusData,
       "hihsmPlanStatusCheckDate": hihsmPlanStatusCheckDate,
       "hihsmPlanStatusCheckTime": hihsmPlanStatusCheckTime,
       "hihsmPlanStatusMigrationDate": hihsmPlanStatusMigrationDate,
       "hihsmPlanStatusMigrationTime": hihsmPlanStatusMigrationTime,
       "hihsmPlanStatusControlStatus": hihsmPlanStatusControlStatus,
       "hihsmAutomaticMigrationPlanLDEVTable": hihsmAutomaticMigrationPlanLDEVTable,
       "hihsmAutomaticMigrationPlanLDEVEntry": hihsmAutomaticMigrationPlanLDEVEntry,
       "hihsmPlanLDEVSerialNumber": hihsmPlanLDEVSerialNumber,
       "hihsmPlanLDEVControlIndex": hihsmPlanLDEVControlIndex,
       "hihsmPlanLDEVSrcFB4Number": hihsmPlanLDEVSrcFB4Number,
       "hihsmPlanLDEVSrcPGNumber": hihsmPlanLDEVSrcPGNumber,
       "hihsmPlanLDEVSrcCU": hihsmPlanLDEVSrcCU,
       "hihsmPlanLDEVSrcLDEV": hihsmPlanLDEVSrcLDEV,
       "hihsmPlanLDEVDstFB4Number": hihsmPlanLDEVDstFB4Number,
       "hihsmPlanLDEVDstPGNumber": hihsmPlanLDEVDstPGNumber,
       "hihsmPlanLDEVDstCU": hihsmPlanLDEVDstCU,
       "hihsmPlanLDEVDstLDEV": hihsmPlanLDEVDstLDEV,
       "hihsmAutomaticMigrationHistory": hihsmAutomaticMigrationHistory,
       "hihsmAutomaticMigrationHistoryCtrlTable": hihsmAutomaticMigrationHistoryCtrlTable,
       "hihsmAutomaticMigrationHistoryCtrlEntry": hihsmAutomaticMigrationHistoryCtrlEntry,
       "hihsmAutoHstCtrlSerialNumber": hihsmAutoHstCtrlSerialNumber,
       "hihsmAutoHstCtrlControlStatus": hihsmAutoHstCtrlControlStatus,
       "hihsmAutomaticMigrationHistoryListTable": hihsmAutomaticMigrationHistoryListTable,
       "hihsmAutomaticMigrationHistoryListEntry": hihsmAutomaticMigrationHistoryListEntry,
       "hihsmAutoHstListSerialNumber": hihsmAutoHstListSerialNumber,
       "hihsmAutoHstListControlIndex": hihsmAutoHstListControlIndex,
       "hihsmAutoHstListMessage": hihsmAutoHstListMessage,
       "hihsmVolumeMigrationHistory": hihsmVolumeMigrationHistory,
       "hihsmVolumeMigrationHistoryCtrlTable": hihsmVolumeMigrationHistoryCtrlTable,
       "hihsmVolumeMigrationHistoryCtrlEntry": hihsmVolumeMigrationHistoryCtrlEntry,
       "hihsmVolHstCtrlSerialNumber": hihsmVolHstCtrlSerialNumber,
       "hihsmVolHstCtrlControlStatus": hihsmVolHstCtrlControlStatus,
       "hihsmVolumeMigrationHistoryListTable": hihsmVolumeMigrationHistoryListTable,
       "hihsmVolumeMigrationHistoryListEntry": hihsmVolumeMigrationHistoryListEntry,
       "hihsmVolHstListSerialNumber": hihsmVolHstListSerialNumber,
       "hihsmVolHstListControlIndex": hihsmVolHstListControlIndex,
       "hihsmVolHstListDate": hihsmVolHstListDate,
       "hihsmVolHstListTime": hihsmVolHstListTime,
       "hihsmVolHstListAction": hihsmVolHstListAction,
       "hihsmVolHstListSrcFB4Number": hihsmVolHstListSrcFB4Number,
       "hihsmVolHstListSrcPGNumber": hihsmVolHstListSrcPGNumber,
       "hihsmVolHstListSrcCU": hihsmVolHstListSrcCU,
       "hihsmVolHstListSrcLDEV": hihsmVolHstListSrcLDEV,
       "hihsmVolHstListDstFB4Number": hihsmVolHstListDstFB4Number,
       "hihsmVolHstListDstPGNumber": hihsmVolHstListDstPGNumber,
       "hihsmVolHstListDstCU": hihsmVolHstListDstCU,
       "hihsmVolHstListDstLDEV": hihsmVolHstListDstLDEV,
       "hihsmManualMigration": hihsmManualMigration,
       "hihsmManualVolumeMigrationTable": hihsmManualVolumeMigrationTable,
       "hihsmManualVolumeMigrationEntry": hihsmManualVolumeMigrationEntry,
       "hihsmManVolMigSerialNumber": hihsmManVolMigSerialNumber,
       "hihsmManVolMigSrcCU": hihsmManVolMigSrcCU,
       "hihsmManVolMigSrcLDEV": hihsmManVolMigSrcLDEV,
       "hihsmManVolMigDstCU": hihsmManVolMigDstCU,
       "hihsmManVolMigDstLDEV": hihsmManVolMigDstLDEV,
       "hihsmManVolMigProgress": hihsmManVolMigProgress,
       "hihsmManVolMigControlStatus": hihsmManVolMigControlStatus,
       "hihsmMigrationExceptation": hihsmMigrationExceptation,
       "hihsmExpectationPGUtilizationTable": hihsmExpectationPGUtilizationTable,
       "hihsmExpectationPGUtilizationEntry": hihsmExpectationPGUtilizationEntry,
       "hihsmExpPGUtilSerialNumber": hihsmExpPGUtilSerialNumber,
       "hihsmExpPGUtilSrcCU": hihsmExpPGUtilSrcCU,
       "hihsmExpPGUtilSrcLDEV": hihsmExpPGUtilSrcLDEV,
       "hihsmExpPGUtilDstFB4": hihsmExpPGUtilDstFB4,
       "hihsmExpPGUtilDstPG": hihsmExpPGUtilDstPG,
       "hihsmExpPGUtilData": hihsmExpPGUtilData,
       "hihsmExpPGUtilControlStatus": hihsmExpPGUtilControlStatus,
       "raidExMibCSW": raidExMibCSW,
       "raidExMibCSWConfigurationTable": raidExMibCSWConfigurationTable,
       "raidExMibCSWConfigurationEntry": raidExMibCSWConfigurationEntry,
       "cswSerialNumber": cswSerialNumber,
       "cswClusterNumber": cswClusterNumber,
       "cswNumber": cswNumber,
       "cswDisplayName": cswDisplayName,
       "raidExMibSharedMemory": raidExMibSharedMemory,
       "raidExMibSMConfigurationTable": raidExMibSMConfigurationTable,
       "raidExMibSMConfigurationEntry": raidExMibSMConfigurationEntry,
       "smSerialNumber": smSerialNumber,
       "smClusterNumber": smClusterNumber,
       "smDisplayName": smDisplayName,
       "raidExMibCacheMemory": raidExMibCacheMemory,
       "raidExMibCacheConfigurationTable": raidExMibCacheConfigurationTable,
       "raidExMibCacheConfigurationEntry": raidExMibCacheConfigurationEntry,
       "cacheConfSerialNumber": cacheConfSerialNumber,
       "cacheConfClusterNumber": cacheConfClusterNumber,
       "cacheConfCacheNumber": cacheConfCacheNumber,
       "cacheConfDisplayName": cacheConfDisplayName,
       "raidExMibPortControlConfiguration": raidExMibPortControlConfiguration,
       "raidExMibPortControlSwitchTable": raidExMibPortControlSwitchTable,
       "raidExMibPortControlSwitchEntry": raidExMibPortControlSwitchEntry,
       "portControlSwitchSerialNumber": portControlSwitchSerialNumber,
       "portControlSwitchOnOff": portControlSwitchOnOff,
       "portControlSwitchStatus": portControlSwitchStatus,
       "raidExMibPortControlSetUpTable": raidExMibPortControlSetUpTable,
       "raidExMibPortControlSetUpEntry": raidExMibPortControlSetUpEntry,
       "portControlSetUpSerialNumber": portControlSetUpSerialNumber,
       "portControlSetUpPortID": portControlSetUpPortID,
       "portControlSetUpControlIndex": portControlSetUpControlIndex,
       "portControlSetUpDisplayName": portControlSetUpDisplayName,
       "portControlSetUpSetting": portControlSetUpSetting,
       "portControlSetUpStatus": portControlSetUpStatus,
       "raidExMibPortControlParameter": raidExMibPortControlParameter,
       "raidExMibPortParameterTable": raidExMibPortParameterTable,
       "raidExMibPortParameterEntry": raidExMibPortParameterEntry,
       "portPrmSerialNumber": portPrmSerialNumber,
       "portPrmPortID": portPrmPortID,
       "portPrmControlIndex": portPrmControlIndex,
       "portPrmDisplayName": portPrmDisplayName,
       "portPrmSetting": portPrmSetting,
       "portPrmPrioIOPS": portPrmPrioIOPS,
       "portPrmPrioMBS": portPrmPrioMBS,
       "portNPrmnPrioIOPS": portNPrmnPrioIOPS,
       "portNPrmnPrioMBS": portNPrmnPrioMBS,
       "portPrmThreshold": portPrmThreshold,
       "portPrmStatus": portPrmStatus,
       "raidExMibPrioAllPortParameterTable": raidExMibPrioAllPortParameterTable,
       "raidExMibPrioAllPortParameterEntry": raidExMibPrioAllPortParameterEntry,
       "prioAllPortPrmSerialNumber": prioAllPortPrmSerialNumber,
       "prioAllPortPrmPrioIOPS": prioAllPortPrmPrioIOPS,
       "prioAllPortPrmPrioMBS": prioAllPortPrmPrioMBS,
       "prioAllPortPrmThreshold": prioAllPortPrmThreshold,
       "prioAllPortPrmStatus": prioAllPortPrmStatus,
       "raidExMibAllPortParameterTable": raidExMibAllPortParameterTable,
       "raidExMibAllPortParameterEntry": raidExMibAllPortParameterEntry,
       "allPortPrmSerialNumber": allPortPrmSerialNumber,
       "allPortPrmStatus": allPortPrmStatus,
       "raidExMibRealTimeMonitoringInformation": raidExMibRealTimeMonitoringInformation,
       "raidExMibRTMonitoringCntlTable": raidExMibRTMonitoringCntlTable,
       "raidExMibRTMonitoringCntlEntry": raidExMibRTMonitoringCntlEntry,
       "rTMonitoringCntlSerialNumber": rTMonitoringCntlSerialNumber,
       "rTMonitoringCntlStatus": rTMonitoringCntlStatus,
       "raidExMibRTMonitorDataTable": raidExMibRTMonitorDataTable,
       "raidExMibRTMonitorDataEntry": raidExMibRTMonitorDataEntry,
       "rTMonitorDataSerialNumber": rTMonitorDataSerialNumber,
       "rTMonitorDataPortID": rTMonitorDataPortID,
       "rTMonitorDataControlIndex": rTMonitorDataControlIndex,
       "rTMonitorDataGatheredDate": rTMonitorDataGatheredDate,
       "rTMonitorDataGatheredTime": rTMonitorDataGatheredTime,
       "rTMonitorDataSetting": rTMonitorDataSetting,
       "rTMonitorDataIOPSMax": rTMonitorDataIOPSMax,
       "rTMonitorDataIOPSAve": rTMonitorDataIOPSAve,
       "rTMonitorDataIOPSMin": rTMonitorDataIOPSMin,
       "rTMonitorDataMBSMax": rTMonitorDataMBSMax,
       "rTMonitorDataMBSAve": rTMonitorDataMBSAve,
       "rTMonitorDataMBSMin": rTMonitorDataMBSMin,
       "raidExMibPrioRTMonitorDataTable": raidExMibPrioRTMonitorDataTable,
       "raidExMibPrioRTMonitorDataEntry": raidExMibPrioRTMonitorDataEntry,
       "prioRTMonitorDataSerialNumber": prioRTMonitorDataSerialNumber,
       "prioRTMonitorDataGatheredDate": prioRTMonitorDataGatheredDate,
       "prioRTMonitorDataGatheredTime": prioRTMonitorDataGatheredTime,
       "prioRTMonitorDataIOPSMax": prioRTMonitorDataIOPSMax,
       "prioRTMonitorDataIOPSAve": prioRTMonitorDataIOPSAve,
       "prioRTMonitorDataIOPSMin": prioRTMonitorDataIOPSMin,
       "prioRTMonitorDataMBSMax": prioRTMonitorDataMBSMax,
       "prioRTMonitorDataMBSAve": prioRTMonitorDataMBSAve,
       "prioRTMonitorDataMBSMin": prioRTMonitorDataMBSMin,
       "raidExMibNPrioRTMonitorDataTable": raidExMibNPrioRTMonitorDataTable,
       "raidExMibNPrioRTMonitorDataEntry": raidExMibNPrioRTMonitorDataEntry,
       "nPrioRTMonitorDataSerialNumber": nPrioRTMonitorDataSerialNumber,
       "nPrioRTMonitorDataGatheredDate": nPrioRTMonitorDataGatheredDate,
       "nPrioRTMonitorDataGatheredTime": nPrioRTMonitorDataGatheredTime,
       "nPrioRTMonitorDataIOPSMax": nPrioRTMonitorDataIOPSMax,
       "nPrioRTMonitorDataIOPSAve": nPrioRTMonitorDataIOPSAve,
       "nPrioRTMonitorDataIOPSMin": nPrioRTMonitorDataIOPSMin,
       "nPrioRTMonitorDataMBSMax": nPrioRTMonitorDataMBSMax,
       "nPrioRTMonitorDataMBSAve": nPrioRTMonitorDataMBSAve,
       "nPrioRTMonitorDataMBSMin": nPrioRTMonitorDataMBSMin,
       "raidExMibVersionManagement": raidExMibVersionManagement,
       "mibAllLeafVersionTable": mibAllLeafVersionTable,
       "mibAllLeafVersionEntry": mibAllLeafVersionEntry,
       "mibAllLeafVersionSerialNumber": mibAllLeafVersionSerialNumber,
       "mibAllLeafVersionMIBVersionData": mibAllLeafVersionMIBVersionData,
       "mibAllLeafVersionMIBVersion": mibAllLeafVersionMIBVersion,
       "mibLdevLeafVersionTable": mibLdevLeafVersionTable,
       "mibLdevLeafVersionEntry": mibLdevLeafVersionEntry,
       "mibLdevVersionSerialNumber": mibLdevVersionSerialNumber,
       "mibLdevVersionMIBVersion": mibLdevVersionMIBVersion,
       "mibLdevVersionMIBOID": mibLdevVersionMIBOID,
       "mibLuLeafVersion": mibLuLeafVersion,
       "mibPortleafVersionTable": mibPortleafVersionTable,
       "mibPortleafVersionEntry": mibPortleafVersionEntry,
       "mibPortVersionSerialNumber": mibPortVersionSerialNumber,
       "mibPortVersionMIBVersion": mibPortVersionMIBVersion,
       "mibPortVersionMIBOID": mibPortVersionMIBOID,
       "mibPathLeafVersionTable": mibPathLeafVersionTable,
       "mibPathLeafVersionEntry": mibPathLeafVersionEntry,
       "mibPathVersionSerialNumber": mibPathVersionSerialNumber,
       "mibPathVersionMIBVersion": mibPathVersionMIBVersion,
       "mibPathVersionMIBOID": mibPathVersionMIBOID,
       "mibLuseLeafVersionTable": mibLuseLeafVersionTable,
       "mibLuseLeafVersionEntry": mibLuseLeafVersionEntry,
       "mibLuseVersionSerialNumber": mibLuseVersionSerialNumber,
       "mibLuseVersionMIBVersion": mibLuseVersionMIBVersion,
       "mibLuseVersionMIBOID": mibLuseVersionMIBOID,
       "mibLunsLeafVersionTable": mibLunsLeafVersionTable,
       "mibLunsLeafVersionEntry": mibLunsLeafVersionEntry,
       "mibLunsVersionSerialNumber": mibLunsVersionSerialNumber,
       "mibLunsVersionMIBVersion": mibLunsVersionMIBVersion,
       "mibLunsVersionMIBOID": mibLunsVersionMIBOID,
       "mibDcrLeafVersionTable": mibDcrLeafVersionTable,
       "mibDcrLeafVersionEntry": mibDcrLeafVersionEntry,
       "mibDcrVersionSerialNumber": mibDcrVersionSerialNumber,
       "mibDcrVersionMIBVersion": mibDcrVersionMIBVersion,
       "mibDcrVersionMIBOID": mibDcrVersionMIBOID,
       "mibCvsLeafVersionTable": mibCvsLeafVersionTable,
       "mibCvsLeafVersionEntry": mibCvsLeafVersionEntry,
       "mibCvsLeafVersionSerialNumber": mibCvsLeafVersionSerialNumber,
       "mibCvsLeafVersionMIBVersion": mibCvsLeafVersionMIBVersion,
       "mibCvsLeafVersionMIBOID": mibCvsLeafVersionMIBOID,
       "mibSsidLeafVersionTable": mibSsidLeafVersionTable,
       "mibSsidLeafVersionEntry": mibSsidLeafVersionEntry,
       "mibSsidVersionSerialNumber": mibSsidVersionSerialNumber,
       "mibSsidVersionMIBVersion": mibSsidVersionMIBVersion,
       "mibSsidVersionMIBOID": mibSsidVersionMIBOID,
       "mibEnvLeafVersionTable": mibEnvLeafVersionTable,
       "mibEnvLeafVersionEntry": mibEnvLeafVersionEntry,
       "mibEnvVersionSerialNumber": mibEnvVersionSerialNumber,
       "mibEnvVersionMIBVersion": mibEnvVersionMIBVersion,
       "mibEnvVersionMIBOID": mibEnvVersionMIBOID,
       "mibChaLeafVersionTable": mibChaLeafVersionTable,
       "mibChaLeafVersionEntry": mibChaLeafVersionEntry,
       "mibChaVersionSerialNumber": mibChaVersionSerialNumber,
       "mibChaVersionMIBVersion": mibChaVersionMIBVersion,
       "mibChaVersionMIBOID": mibChaVersionMIBOID,
       "mibDkaLeafVersionTable": mibDkaLeafVersionTable,
       "mibDkaLeafVersionEntry": mibDkaLeafVersionEntry,
       "mibDkaVersionSerialNumber": mibDkaVersionSerialNumber,
       "mibDkaVersionMIBVersion": mibDkaVersionMIBVersion,
       "mibDkaVersionMIBOID": mibDkaVersionMIBOID,
       "mibPgLeafVersionTable": mibPgLeafVersionTable,
       "mibPgLeafVersionEntry": mibPgLeafVersionEntry,
       "mibPgVersionSerialNumber": mibPgVersionSerialNumber,
       "mibPgVersionMIBVersion": mibPgVersionMIBVersion,
       "mibPgVersionMIBOID": mibPgVersionMIBOID,
       "mibHihsmLeafVersionTable": mibHihsmLeafVersionTable,
       "mibHihsmLeafVersionEntry": mibHihsmLeafVersionEntry,
       "mibHihsmVersionSerialNumber": mibHihsmVersionSerialNumber,
       "mibHihsmVersionMIBVersion": mibHihsmVersionMIBVersion,
       "mibHihsmVersionMIBOID": mibHihsmVersionMIBOID,
       "mibCswLeafVersionTable": mibCswLeafVersionTable,
       "mibCswLeafVersionEntry": mibCswLeafVersionEntry,
       "mibCswVersionSerialNumber": mibCswVersionSerialNumber,
       "mibCswVersionMIBVersion": mibCswVersionMIBVersion,
       "mibCswVersionMIBOID": mibCswVersionMIBOID,
       "mibSmLeafVersionTable": mibSmLeafVersionTable,
       "mibSmLeafVersionEntry": mibSmLeafVersionEntry,
       "mibSmLeafVersionSerialNumber": mibSmLeafVersionSerialNumber,
       "mibSmLeafVersionMIBVersion": mibSmLeafVersionMIBVersion,
       "mibSmLeafVersionMIBOID": mibSmLeafVersionMIBOID,
       "mibCmLeafVersionTable": mibCmLeafVersionTable,
       "mibCmLeafVersionEntry": mibCmLeafVersionEntry,
       "mibCmVersionSerialNumber": mibCmVersionSerialNumber,
       "mibCmVersionMIBVersion": mibCmVersionMIBVersion,
       "mibCmVersionMIBOID": mibCmVersionMIBOID,
       "mibPortControlLeafVersionTable": mibPortControlLeafVersionTable,
       "mibPortControlLeafVersionEntry": mibPortControlLeafVersionEntry,
       "mibPortControlVersionSerialNumber": mibPortControlVersionSerialNumber,
       "mibPortControlVersionMIBVersion": mibPortControlVersionMIBVersion,
       "mibPortControlVersionMIBOID": mibPortControlVersionMIBOID}
)
