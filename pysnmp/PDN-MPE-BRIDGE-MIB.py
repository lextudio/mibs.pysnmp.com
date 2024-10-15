# SNMP MIB module (PDN-MPE-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MPE-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:53 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mpe_bridge,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "mpe-bridge")

(VnidRange,) = mibBuilder.importSymbols(
    "PDN-TC",
    "VnidRange")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpePdnBridgeGenericMIBObjects_ObjectIdentity = ObjectIdentity
mpePdnBridgeGenericMIBObjects = _MpePdnBridgeGenericMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1)
)
_MpePdnDot1dGenericBridge_ObjectIdentity = ObjectIdentity
mpePdnDot1dGenericBridge = _MpePdnDot1dGenericBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1)
)
_MpePdnDot1dBridgeTable_Object = MibTable
mpePdnDot1dBridgeTable = _MpePdnDot1dBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpePdnDot1dBridgeTable.setStatus("mandatory")
_MpePdnDot1dBridgeEntry_Object = MibTableRow
mpePdnDot1dBridgeEntry = _MpePdnDot1dBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1)
)
mpePdnDot1dBridgeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpePdnDot1dBridgeEntry.setStatus("mandatory")
_MpePdnDot1dBaseBridgeAddress_Type = MacAddress
_MpePdnDot1dBaseBridgeAddress_Object = MibTableColumn
mpePdnDot1dBaseBridgeAddress = _MpePdnDot1dBaseBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 1),
    _MpePdnDot1dBaseBridgeAddress_Type()
)
mpePdnDot1dBaseBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dBaseBridgeAddress.setStatus("mandatory")
_MpePdnDot1dBaseNumPorts_Type = Integer32
_MpePdnDot1dBaseNumPorts_Object = MibTableColumn
mpePdnDot1dBaseNumPorts = _MpePdnDot1dBaseNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 2),
    _MpePdnDot1dBaseNumPorts_Type()
)
mpePdnDot1dBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dBaseNumPorts.setStatus("mandatory")


class _MpePdnDot1dBaseType_Type(Integer32):
    """Custom type mpePdnDot1dBaseType based on Integer32"""
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
        *(("sourceroute-only", 3),
          ("srt", 4),
          ("transparent-only", 2),
          ("unknown", 1))
    )


_MpePdnDot1dBaseType_Type.__name__ = "Integer32"
_MpePdnDot1dBaseType_Object = MibTableColumn
mpePdnDot1dBaseType = _MpePdnDot1dBaseType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 3),
    _MpePdnDot1dBaseType_Type()
)
mpePdnDot1dBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dBaseType.setStatus("mandatory")
_MpePdnDot1dTpLearnedEntryDiscards_Type = Counter32
_MpePdnDot1dTpLearnedEntryDiscards_Object = MibTableColumn
mpePdnDot1dTpLearnedEntryDiscards = _MpePdnDot1dTpLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 4),
    _MpePdnDot1dTpLearnedEntryDiscards_Type()
)
mpePdnDot1dTpLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dTpLearnedEntryDiscards.setStatus("mandatory")


class _MpePdnDot1dTpAgeingTime_Type(Integer32):
    """Custom type mpePdnDot1dTpAgeingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MpePdnDot1dTpAgeingTime_Type.__name__ = "Integer32"
_MpePdnDot1dTpAgeingTime_Object = MibTableColumn
mpePdnDot1dTpAgeingTime = _MpePdnDot1dTpAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 5),
    _MpePdnDot1dTpAgeingTime_Type()
)
mpePdnDot1dTpAgeingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnDot1dTpAgeingTime.setStatus("mandatory")


class _MpePdnDot1dTpAgeingCleanupTime_Type(Integer32):
    """Custom type mpePdnDot1dTpAgeingCleanupTime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500000),
    )


_MpePdnDot1dTpAgeingCleanupTime_Type.__name__ = "Integer32"
_MpePdnDot1dTpAgeingCleanupTime_Object = MibTableColumn
mpePdnDot1dTpAgeingCleanupTime = _MpePdnDot1dTpAgeingCleanupTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 1, 1, 1, 6),
    _MpePdnDot1dTpAgeingCleanupTime_Type()
)
mpePdnDot1dTpAgeingCleanupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnDot1dTpAgeingCleanupTime.setStatus("mandatory")
_MpePdnDot1dTpFdb_ObjectIdentity = ObjectIdentity
mpePdnDot1dTpFdb = _MpePdnDot1dTpFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2)
)
_MpePdnDot1dTpFdbTable_Object = MibTable
mpePdnDot1dTpFdbTable = _MpePdnDot1dTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbTable.setStatus("mandatory")
_MpePdnDot1dTpFdbEntry_Object = MibTableRow
mpePdnDot1dTpFdbEntry = _MpePdnDot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1)
)
mpePdnDot1dTpFdbEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "PDN-MPE-BRIDGE-MIB", "mpePdnDot1dTpFdbAddress"),
    (0, "PDN-MPE-BRIDGE-MIB", "mpePdnDot1dTpFdbVnidId"),
)
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbEntry.setStatus("mandatory")
_MpePdnDot1dTpFdbAddress_Type = MacAddress
_MpePdnDot1dTpFdbAddress_Object = MibTableColumn
mpePdnDot1dTpFdbAddress = _MpePdnDot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 1),
    _MpePdnDot1dTpFdbAddress_Type()
)
mpePdnDot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbAddress.setStatus("mandatory")
_MpePdnDot1dTpFdbVnidId_Type = VnidRange
_MpePdnDot1dTpFdbVnidId_Object = MibTableColumn
mpePdnDot1dTpFdbVnidId = _MpePdnDot1dTpFdbVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 2),
    _MpePdnDot1dTpFdbVnidId_Type()
)
mpePdnDot1dTpFdbVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbVnidId.setStatus("mandatory")
_MpePdnDot1dTpFdbIfIndex_Type = Integer32
_MpePdnDot1dTpFdbIfIndex_Object = MibTableColumn
mpePdnDot1dTpFdbIfIndex = _MpePdnDot1dTpFdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 3),
    _MpePdnDot1dTpFdbIfIndex_Type()
)
mpePdnDot1dTpFdbIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbIfIndex.setStatus("mandatory")


class _MpePdnDot1dTpFdbStatus_Type(Integer32):
    """Custom type mpePdnDot1dTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_MpePdnDot1dTpFdbStatus_Type.__name__ = "Integer32"
_MpePdnDot1dTpFdbStatus_Object = MibTableColumn
mpePdnDot1dTpFdbStatus = _MpePdnDot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 4),
    _MpePdnDot1dTpFdbStatus_Type()
)
mpePdnDot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbStatus.setStatus("mandatory")
_MpePdnDot1dTpFdbAgeTime_Type = Integer32
_MpePdnDot1dTpFdbAgeTime_Object = MibTableColumn
mpePdnDot1dTpFdbAgeTime = _MpePdnDot1dTpFdbAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 5),
    _MpePdnDot1dTpFdbAgeTime_Type()
)
mpePdnDot1dTpFdbAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbAgeTime.setStatus("mandatory")


class _MpePdnDot1dTpFdbFlags_Type(Integer32):
    """Custom type mpePdnDot1dTpFdbFlags based on Integer32"""
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
        *(("dynamic", 4),
          ("other", 1),
          ("permanentCONFIGURED", 3),
          ("permanentDHCP", 2))
    )


_MpePdnDot1dTpFdbFlags_Type.__name__ = "Integer32"
_MpePdnDot1dTpFdbFlags_Object = MibTableColumn
mpePdnDot1dTpFdbFlags = _MpePdnDot1dTpFdbFlags_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 1, 2, 1, 1, 6),
    _MpePdnDot1dTpFdbFlags_Type()
)
mpePdnDot1dTpFdbFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnDot1dTpFdbFlags.setStatus("mandatory")
_MpePdnBridgeMIBTraps_ObjectIdentity = ObjectIdentity
mpePdnBridgeMIBTraps = _MpePdnBridgeMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 21, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-BRIDGE-MIB",
    **{"mpePdnBridgeGenericMIBObjects": mpePdnBridgeGenericMIBObjects,
       "mpePdnDot1dGenericBridge": mpePdnDot1dGenericBridge,
       "mpePdnDot1dBridgeTable": mpePdnDot1dBridgeTable,
       "mpePdnDot1dBridgeEntry": mpePdnDot1dBridgeEntry,
       "mpePdnDot1dBaseBridgeAddress": mpePdnDot1dBaseBridgeAddress,
       "mpePdnDot1dBaseNumPorts": mpePdnDot1dBaseNumPorts,
       "mpePdnDot1dBaseType": mpePdnDot1dBaseType,
       "mpePdnDot1dTpLearnedEntryDiscards": mpePdnDot1dTpLearnedEntryDiscards,
       "mpePdnDot1dTpAgeingTime": mpePdnDot1dTpAgeingTime,
       "mpePdnDot1dTpAgeingCleanupTime": mpePdnDot1dTpAgeingCleanupTime,
       "mpePdnDot1dTpFdb": mpePdnDot1dTpFdb,
       "mpePdnDot1dTpFdbTable": mpePdnDot1dTpFdbTable,
       "mpePdnDot1dTpFdbEntry": mpePdnDot1dTpFdbEntry,
       "mpePdnDot1dTpFdbAddress": mpePdnDot1dTpFdbAddress,
       "mpePdnDot1dTpFdbVnidId": mpePdnDot1dTpFdbVnidId,
       "mpePdnDot1dTpFdbIfIndex": mpePdnDot1dTpFdbIfIndex,
       "mpePdnDot1dTpFdbStatus": mpePdnDot1dTpFdbStatus,
       "mpePdnDot1dTpFdbAgeTime": mpePdnDot1dTpFdbAgeTime,
       "mpePdnDot1dTpFdbFlags": mpePdnDot1dTpFdbFlags,
       "mpePdnBridgeMIBTraps": mpePdnBridgeMIBTraps}
)
