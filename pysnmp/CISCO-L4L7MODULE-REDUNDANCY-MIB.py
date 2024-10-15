# SNMP MIB module (CISCO-L4L7MODULE-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L4L7MODULE-REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:50 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoL4L7moduleRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650)
)
ciscoL4L7moduleRedundancyMIB.setRevisions(
        ("2008-04-04 00:00",
         "2008-03-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoL4L7RedState(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("initializing", 3),
          ("negotiation", 4),
          ("nonRedundant", 2),
          ("other", 1),
          ("standbyBulk", 8),
          ("standbyCold", 6),
          ("standbyConfig", 7),
          ("standbyHot", 9),
          ("standbyWarm", 10))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLmRedundancyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLmRedundancyMIBNotifs = _CiscoLmRedundancyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 0)
)
_CiscoLmRedundancyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLmRedundancyMIBObjects = _CiscoLmRedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1)
)
_ClrConfig_ObjectIdentity = ObjectIdentity
clrConfig = _ClrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1)
)
_ClrPeerConfigTable_Object = MibTable
clrPeerConfigTable = _ClrPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clrPeerConfigTable.setStatus("current")
_ClrPeerConfigEntry_Object = MibTableRow
clrPeerConfigEntry = _ClrPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1)
)
clrPeerConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerId"),
)
if mibBuilder.loadTexts:
    clrPeerConfigEntry.setStatus("current")


class _ClrPeerId_Type(Unsigned32):
    """Custom type clrPeerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClrPeerId_Type.__name__ = "Unsigned32"
_ClrPeerId_Object = MibTableColumn
clrPeerId = _ClrPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1, 1),
    _ClrPeerId_Type()
)
clrPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrPeerId.setStatus("current")
_ClrPeerInterface_Type = InterfaceIndex
_ClrPeerInterface_Object = MibTableColumn
clrPeerInterface = _ClrPeerInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1, 2),
    _ClrPeerInterface_Type()
)
clrPeerInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrPeerInterface.setStatus("current")


class _ClrPeerBackupInterface_Type(InterfaceIndexOrZero):
    """Custom type clrPeerBackupInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_ClrPeerBackupInterface_Object = MibTableColumn
clrPeerBackupInterface = _ClrPeerBackupInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1, 3),
    _ClrPeerBackupInterface_Type()
)
clrPeerBackupInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrPeerBackupInterface.setStatus("current")


class _ClrPeerHeartBeatTime_Type(Unsigned32):
    """Custom type clrPeerHeartBeatTime based on Unsigned32"""
    defaultValue = 1


_ClrPeerHeartBeatTime_Object = MibTableColumn
clrPeerHeartBeatTime = _ClrPeerHeartBeatTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1, 4),
    _ClrPeerHeartBeatTime_Type()
)
clrPeerHeartBeatTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrPeerHeartBeatTime.setStatus("current")
if mibBuilder.loadTexts:
    clrPeerHeartBeatTime.setUnits("milliseconds")


class _ClrPeerHeartBeatCount_Type(Unsigned32):
    """Custom type clrPeerHeartBeatCount based on Unsigned32"""
    defaultValue = 1


_ClrPeerHeartBeatCount_Object = MibTableColumn
clrPeerHeartBeatCount = _ClrPeerHeartBeatCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1, 5),
    _ClrPeerHeartBeatCount_Type()
)
clrPeerHeartBeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrPeerHeartBeatCount.setStatus("current")


class _ClrPeerStorageType_Type(StorageType):
    """Custom type clrPeerStorageType based on StorageType"""


_ClrPeerStorageType_Object = MibTableColumn
clrPeerStorageType = _ClrPeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1, 6),
    _ClrPeerStorageType_Type()
)
clrPeerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrPeerStorageType.setStatus("current")
_ClrPeerRowStatus_Type = RowStatus
_ClrPeerRowStatus_Object = MibTableColumn
clrPeerRowStatus = _ClrPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 1, 1, 7),
    _ClrPeerRowStatus_Type()
)
clrPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrPeerRowStatus.setStatus("current")
_ClrPeerInfoTable_Object = MibTable
clrPeerInfoTable = _ClrPeerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clrPeerInfoTable.setStatus("current")
_ClrPeerInfoEntry_Object = MibTableRow
clrPeerInfoEntry = _ClrPeerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2, 1)
)
clrPeerInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerId"),
)
if mibBuilder.loadTexts:
    clrPeerInfoEntry.setStatus("current")


class _ClrPeerOperStatus_Type(Integer32):
    """Custom type clrPeerOperStatus based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 8),
          ("down", 10),
          ("error", 11),
          ("init", 1),
          ("licCheck", 7),
          ("localIPaddr", 2),
          ("peerIPAddr", 3),
          ("peerInterfaceDown", 9),
          ("srgCheck", 6),
          ("startHB", 4),
          ("tcpSetup", 5))
    )


_ClrPeerOperStatus_Type.__name__ = "Integer32"
_ClrPeerOperStatus_Object = MibTableColumn
clrPeerOperStatus = _ClrPeerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2, 1, 1),
    _ClrPeerOperStatus_Type()
)
clrPeerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrPeerOperStatus.setStatus("current")
_ClrPeerIpAddressType_Type = InetAddressType
_ClrPeerIpAddressType_Object = MibTableColumn
clrPeerIpAddressType = _ClrPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2, 1, 2),
    _ClrPeerIpAddressType_Type()
)
clrPeerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrPeerIpAddressType.setStatus("current")
_ClrPeerIpAddress_Type = InetAddress
_ClrPeerIpAddress_Object = MibTableColumn
clrPeerIpAddress = _ClrPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2, 1, 3),
    _ClrPeerIpAddress_Type()
)
clrPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrPeerIpAddress.setStatus("current")


class _ClrPeerSoftwareCompatibilty_Type(Integer32):
    """Custom type clrPeerSoftwareCompatibilty based on Integer32"""
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
        *(("compatible", 2),
          ("inCompatible", 3),
          ("init", 1),
          ("warmCompatible", 4))
    )


_ClrPeerSoftwareCompatibilty_Type.__name__ = "Integer32"
_ClrPeerSoftwareCompatibilty_Object = MibTableColumn
clrPeerSoftwareCompatibilty = _ClrPeerSoftwareCompatibilty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2, 1, 4),
    _ClrPeerSoftwareCompatibilty_Type()
)
clrPeerSoftwareCompatibilty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrPeerSoftwareCompatibilty.setStatus("current")


class _ClrPeerLicenseCompatibility_Type(Integer32):
    """Custom type clrPeerLicenseCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 2),
          ("inCompatible", 3),
          ("init", 1))
    )


_ClrPeerLicenseCompatibility_Type.__name__ = "Integer32"
_ClrPeerLicenseCompatibility_Object = MibTableColumn
clrPeerLicenseCompatibility = _ClrPeerLicenseCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2, 1, 5),
    _ClrPeerLicenseCompatibility_Type()
)
clrPeerLicenseCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrPeerLicenseCompatibility.setStatus("current")


class _ClrPeerRedGroups_Type(Unsigned32):
    """Custom type clrPeerRedGroups based on Unsigned32"""
    defaultValue = 0


_ClrPeerRedGroups_Object = MibTableColumn
clrPeerRedGroups = _ClrPeerRedGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 2, 1, 6),
    _ClrPeerRedGroups_Type()
)
clrPeerRedGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrPeerRedGroups.setStatus("current")
_ClrRedundancyConfigTable_Object = MibTable
clrRedundancyConfigTable = _ClrRedundancyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clrRedundancyConfigTable.setStatus("current")
_ClrRedundancyConfigEntry_Object = MibTableRow
clrRedundancyConfigEntry = _ClrRedundancyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1)
)
clrRedundancyConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedGroupId"),
)
if mibBuilder.loadTexts:
    clrRedundancyConfigEntry.setStatus("current")


class _ClrRedGroupId_Type(Unsigned32):
    """Custom type clrRedGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ClrRedGroupId_Type.__name__ = "Unsigned32"
_ClrRedGroupId_Object = MibTableColumn
clrRedGroupId = _ClrRedGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 1),
    _ClrRedGroupId_Type()
)
clrRedGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRedGroupId.setStatus("current")


class _ClrRedPeerId_Type(Unsigned32):
    """Custom type clrRedPeerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClrRedPeerId_Type.__name__ = "Unsigned32"
_ClrRedPeerId_Object = MibTableColumn
clrRedPeerId = _ClrRedPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 2),
    _ClrRedPeerId_Type()
)
clrRedPeerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRedPeerId.setStatus("current")


class _ClrRedPriority_Type(Unsigned32):
    """Custom type clrRedPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClrRedPriority_Type.__name__ = "Unsigned32"
_ClrRedPriority_Object = MibTableColumn
clrRedPriority = _ClrRedPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 3),
    _ClrRedPriority_Type()
)
clrRedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRedPriority.setStatus("current")


class _ClrRedPreempt_Type(TruthValue):
    """Custom type clrRedPreempt based on TruthValue"""


_ClrRedPreempt_Object = MibTableColumn
clrRedPreempt = _ClrRedPreempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 4),
    _ClrRedPreempt_Type()
)
clrRedPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRedPreempt.setStatus("current")


class _ClrRedFailOverTime_Type(Unsigned32):
    """Custom type clrRedFailOverTime based on Unsigned32"""
    defaultValue = 3


_ClrRedFailOverTime_Object = MibTableColumn
clrRedFailOverTime = _ClrRedFailOverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 5),
    _ClrRedFailOverTime_Type()
)
clrRedFailOverTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRedFailOverTime.setStatus("current")
_ClrRedState_Type = CiscoL4L7RedState
_ClrRedState_Object = MibTableColumn
clrRedState = _ClrRedState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 6),
    _ClrRedState_Type()
)
clrRedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRedState.setStatus("current")
_ClrRedStateChangeTime_Type = TimeStamp
_ClrRedStateChangeTime_Object = MibTableColumn
clrRedStateChangeTime = _ClrRedStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 7),
    _ClrRedStateChangeTime_Type()
)
clrRedStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRedStateChangeTime.setStatus("current")
_ClrRedContext_Type = OctetString
_ClrRedContext_Object = MibTableColumn
clrRedContext = _ClrRedContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 8),
    _ClrRedContext_Type()
)
clrRedContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRedContext.setStatus("current")


class _ClrRedStorageType_Type(StorageType):
    """Custom type clrRedStorageType based on StorageType"""


_ClrRedStorageType_Object = MibTableColumn
clrRedStorageType = _ClrRedStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 9),
    _ClrRedStorageType_Type()
)
clrRedStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRedStorageType.setStatus("current")
_ClrRedRowStatus_Type = RowStatus
_ClrRedRowStatus_Object = MibTableColumn
clrRedRowStatus = _ClrRedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 3, 1, 10),
    _ClrRedRowStatus_Type()
)
clrRedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRedRowStatus.setStatus("current")
_ClrRedundancyInfoTable_Object = MibTable
clrRedundancyInfoTable = _ClrRedundancyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 4)
)
if mibBuilder.loadTexts:
    clrRedundancyInfoTable.setStatus("current")
_ClrRedundancyInfoEntry_Object = MibTableRow
clrRedundancyInfoEntry = _ClrRedundancyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 4, 1)
)
clrRedundancyInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedGroupId"),
)
if mibBuilder.loadTexts:
    clrRedundancyInfoEntry.setStatus("current")


class _ClrRedundancyPriority_Type(Unsigned32):
    """Custom type clrRedundancyPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClrRedundancyPriority_Type.__name__ = "Unsigned32"
_ClrRedundancyPriority_Object = MibTableColumn
clrRedundancyPriority = _ClrRedundancyPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 4, 1, 1),
    _ClrRedundancyPriority_Type()
)
clrRedundancyPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRedundancyPriority.setStatus("current")
_ClrRedundancyState_Type = CiscoL4L7RedState
_ClrRedundancyState_Object = MibTableColumn
clrRedundancyState = _ClrRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 4, 1, 2),
    _ClrRedundancyState_Type()
)
clrRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRedundancyState.setStatus("current")
_ClrRedundancyStateChangeTime_Type = TimeStamp
_ClrRedundancyStateChangeTime_Object = MibTableColumn
clrRedundancyStateChangeTime = _ClrRedundancyStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 4, 1, 3),
    _ClrRedundancyStateChangeTime_Type()
)
clrRedundancyStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRedundancyStateChangeTime.setStatus("current")
_ClrRedundancyIpAddressType_Type = InetAddressType
_ClrRedundancyIpAddressType_Object = MibTableColumn
clrRedundancyIpAddressType = _ClrRedundancyIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 4, 1, 4),
    _ClrRedundancyIpAddressType_Type()
)
clrRedundancyIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRedundancyIpAddressType.setStatus("current")
_ClrRedundancyIpAddress_Type = InetAddress
_ClrRedundancyIpAddress_Object = MibTableColumn
clrRedundancyIpAddress = _ClrRedundancyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 1, 4, 1, 5),
    _ClrRedundancyIpAddress_Type()
)
clrRedundancyIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRedundancyIpAddress.setStatus("current")
_ClrStats_ObjectIdentity = ObjectIdentity
clrStats = _ClrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2)
)
_ClrLBStatsTable_Object = MibTable
clrLBStatsTable = _ClrLBStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clrLBStatsTable.setStatus("current")
_ClrLBStatsEntry_Object = MibTableRow
clrLBStatsEntry = _ClrLBStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1, 1)
)
clrLBStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedGroupId"),
)
if mibBuilder.loadTexts:
    clrLBStatsEntry.setStatus("current")
_ClrLBStatsSharedStickyEntries_Type = Counter64
_ClrLBStatsSharedStickyEntries_Object = MibTableColumn
clrLBStatsSharedStickyEntries = _ClrLBStatsSharedStickyEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1, 1, 1),
    _ClrLBStatsSharedStickyEntries_Type()
)
clrLBStatsSharedStickyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrLBStatsSharedStickyEntries.setStatus("current")
_ClrLBStatsSentPackets_Type = Counter64
_ClrLBStatsSentPackets_Object = MibTableColumn
clrLBStatsSentPackets = _ClrLBStatsSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1, 1, 2),
    _ClrLBStatsSentPackets_Type()
)
clrLBStatsSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrLBStatsSentPackets.setStatus("current")
_ClrLBStatsSendFailures_Type = Counter64
_ClrLBStatsSendFailures_Object = MibTableColumn
clrLBStatsSendFailures = _ClrLBStatsSendFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1, 1, 3),
    _ClrLBStatsSendFailures_Type()
)
clrLBStatsSendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrLBStatsSendFailures.setStatus("current")
_ClrLBStatsDroppedEntries_Type = Counter64
_ClrLBStatsDroppedEntries_Object = MibTableColumn
clrLBStatsDroppedEntries = _ClrLBStatsDroppedEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1, 1, 4),
    _ClrLBStatsDroppedEntries_Type()
)
clrLBStatsDroppedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrLBStatsDroppedEntries.setStatus("current")
_ClrLBStatsReceivedPackets_Type = Counter64
_ClrLBStatsReceivedPackets_Object = MibTableColumn
clrLBStatsReceivedPackets = _ClrLBStatsReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1, 1, 5),
    _ClrLBStatsReceivedPackets_Type()
)
clrLBStatsReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrLBStatsReceivedPackets.setStatus("current")
_ClrLBStatsReceiveFailures_Type = Counter64
_ClrLBStatsReceiveFailures_Object = MibTableColumn
clrLBStatsReceiveFailures = _ClrLBStatsReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 1, 1, 6),
    _ClrLBStatsReceiveFailures_Type()
)
clrLBStatsReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrLBStatsReceiveFailures.setStatus("current")
_ClrHAStatsTable_Object = MibTable
clrHAStatsTable = _ClrHAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2)
)
if mibBuilder.loadTexts:
    clrHAStatsTable.setStatus("current")
_ClrHAStatsEntry_Object = MibTableRow
clrHAStatsEntry = _ClrHAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1)
)
clrHAStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerId"),
)
if mibBuilder.loadTexts:
    clrHAStatsEntry.setStatus("current")
_ClrHAStatsTxHeartBeatMsgs_Type = Counter64
_ClrHAStatsTxHeartBeatMsgs_Object = MibTableColumn
clrHAStatsTxHeartBeatMsgs = _ClrHAStatsTxHeartBeatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1, 1),
    _ClrHAStatsTxHeartBeatMsgs_Type()
)
clrHAStatsTxHeartBeatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrHAStatsTxHeartBeatMsgs.setStatus("current")
_ClrHAStatsRxHeartBeatMsgs_Type = Counter64
_ClrHAStatsRxHeartBeatMsgs_Object = MibTableColumn
clrHAStatsRxHeartBeatMsgs = _ClrHAStatsRxHeartBeatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1, 2),
    _ClrHAStatsRxHeartBeatMsgs_Type()
)
clrHAStatsRxHeartBeatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrHAStatsRxHeartBeatMsgs.setStatus("current")
_ClrHAStatsMissedHeartBeatMsgs_Type = Counter64
_ClrHAStatsMissedHeartBeatMsgs_Object = MibTableColumn
clrHAStatsMissedHeartBeatMsgs = _ClrHAStatsMissedHeartBeatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1, 3),
    _ClrHAStatsMissedHeartBeatMsgs_Type()
)
clrHAStatsMissedHeartBeatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrHAStatsMissedHeartBeatMsgs.setStatus("current")
_ClrHAStatsRxUniDirectionalHeartBeatMsgs_Type = Counter64
_ClrHAStatsRxUniDirectionalHeartBeatMsgs_Object = MibTableColumn
clrHAStatsRxUniDirectionalHeartBeatMsgs = _ClrHAStatsRxUniDirectionalHeartBeatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1, 4),
    _ClrHAStatsRxUniDirectionalHeartBeatMsgs_Type()
)
clrHAStatsRxUniDirectionalHeartBeatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrHAStatsRxUniDirectionalHeartBeatMsgs.setStatus("current")
_ClrHAStatsHeartBeatTimeoutMismatches_Type = Counter64
_ClrHAStatsHeartBeatTimeoutMismatches_Object = MibTableColumn
clrHAStatsHeartBeatTimeoutMismatches = _ClrHAStatsHeartBeatTimeoutMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1, 5),
    _ClrHAStatsHeartBeatTimeoutMismatches_Type()
)
clrHAStatsHeartBeatTimeoutMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrHAStatsHeartBeatTimeoutMismatches.setStatus("current")
_ClrHAStatsPeerUpEvents_Type = Counter64
_ClrHAStatsPeerUpEvents_Object = MibTableColumn
clrHAStatsPeerUpEvents = _ClrHAStatsPeerUpEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1, 6),
    _ClrHAStatsPeerUpEvents_Type()
)
clrHAStatsPeerUpEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrHAStatsPeerUpEvents.setStatus("current")
_ClrHAStatsPeerDownEvents_Type = Counter64
_ClrHAStatsPeerDownEvents_Object = MibTableColumn
clrHAStatsPeerDownEvents = _ClrHAStatsPeerDownEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 2, 2, 1, 7),
    _ClrHAStatsPeerDownEvents_Type()
)
clrHAStatsPeerDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrHAStatsPeerDownEvents.setStatus("current")
_ClrNotifObjects_ObjectIdentity = ObjectIdentity
clrNotifObjects = _ClrNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 3)
)


class _ClrStateChangeNotifEnabled_Type(TruthValue):
    """Custom type clrStateChangeNotifEnabled based on TruthValue"""


_ClrStateChangeNotifEnabled_Object = MibScalar
clrStateChangeNotifEnabled = _ClrStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 1, 3, 1),
    _ClrStateChangeNotifEnabled_Type()
)
clrStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrStateChangeNotifEnabled.setStatus("current")
_CiscoLmRedundancyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoLmRedundancyMIBConformance = _CiscoLmRedundancyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2)
)
_CiscoLmRedundancyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLmRedundancyMIBCompliances = _CiscoLmRedundancyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 1)
)
_CiscoLmRedundancyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLmRedundancyMIBGroups = _CiscoLmRedundancyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 2)
)

# Managed Objects groups

clrPeerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 2, 1)
)
clrPeerConfigGroup.setObjects(
      *(("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerInterface"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerBackupInterface"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerHeartBeatTime"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerHeartBeatCount"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerOperStatus"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerIpAddressType"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerIpAddress"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerStorageType"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerRowStatus"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerSoftwareCompatibilty"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerLicenseCompatibility"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrPeerRedGroups"))
)
if mibBuilder.loadTexts:
    clrPeerConfigGroup.setStatus("current")

clrRedConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 2, 2)
)
clrRedConfigGroup.setObjects(
      *(("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedPeerId"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedPriority"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedPreempt"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedFailOverTime"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedState"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedStateChangeTime"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedStorageType"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedRowStatus"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedContext"))
)
if mibBuilder.loadTexts:
    clrRedConfigGroup.setStatus("current")

clrRedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 2, 3)
)
clrRedInfoGroup.setObjects(
      *(("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedundancyPriority"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedundancyState"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedundancyStateChangeTime"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedundancyIpAddressType"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedundancyIpAddress"))
)
if mibBuilder.loadTexts:
    clrRedInfoGroup.setStatus("current")

cslbxNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 2, 4)
)
cslbxNotifControlGroup.setObjects(
    ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrStateChangeNotifEnabled")
)
if mibBuilder.loadTexts:
    cslbxNotifControlGroup.setStatus("current")

clrRedundancyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 2, 6)
)
clrRedundancyStatsGroup.setObjects(
      *(("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrHAStatsTxHeartBeatMsgs"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrHAStatsRxHeartBeatMsgs"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrHAStatsMissedHeartBeatMsgs"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrHAStatsRxUniDirectionalHeartBeatMsgs"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrHAStatsHeartBeatTimeoutMismatches"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrHAStatsPeerUpEvents"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrHAStatsPeerDownEvents"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrLBStatsSharedStickyEntries"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrLBStatsSentPackets"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrLBStatsSendFailures"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrLBStatsDroppedEntries"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrLBStatsReceivedPackets"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrLBStatsReceiveFailures"))
)
if mibBuilder.loadTexts:
    clrRedundancyStatsGroup.setStatus("current")


# Notification objects

clrRedundancyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 0, 1)
)
clrRedundancyStateChange.setObjects(
      *(("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedState"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedStateChangeTime"),
        ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedPeerId"))
)
if mibBuilder.loadTexts:
    clrRedundancyStateChange.setStatus(
        "current"
    )


# Notifications groups

cslbxNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 2, 5)
)
cslbxNotifGroup.setObjects(
    ("CISCO-L4L7MODULE-REDUNDANCY-MIB", "clrRedundancyStateChange")
)
if mibBuilder.loadTexts:
    cslbxNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLmRedundancyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 650, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLmRedundancyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L4L7MODULE-REDUNDANCY-MIB",
    **{"CiscoL4L7RedState": CiscoL4L7RedState,
       "ciscoL4L7moduleRedundancyMIB": ciscoL4L7moduleRedundancyMIB,
       "ciscoLmRedundancyMIBNotifs": ciscoLmRedundancyMIBNotifs,
       "clrRedundancyStateChange": clrRedundancyStateChange,
       "ciscoLmRedundancyMIBObjects": ciscoLmRedundancyMIBObjects,
       "clrConfig": clrConfig,
       "clrPeerConfigTable": clrPeerConfigTable,
       "clrPeerConfigEntry": clrPeerConfigEntry,
       "clrPeerId": clrPeerId,
       "clrPeerInterface": clrPeerInterface,
       "clrPeerBackupInterface": clrPeerBackupInterface,
       "clrPeerHeartBeatTime": clrPeerHeartBeatTime,
       "clrPeerHeartBeatCount": clrPeerHeartBeatCount,
       "clrPeerStorageType": clrPeerStorageType,
       "clrPeerRowStatus": clrPeerRowStatus,
       "clrPeerInfoTable": clrPeerInfoTable,
       "clrPeerInfoEntry": clrPeerInfoEntry,
       "clrPeerOperStatus": clrPeerOperStatus,
       "clrPeerIpAddressType": clrPeerIpAddressType,
       "clrPeerIpAddress": clrPeerIpAddress,
       "clrPeerSoftwareCompatibilty": clrPeerSoftwareCompatibilty,
       "clrPeerLicenseCompatibility": clrPeerLicenseCompatibility,
       "clrPeerRedGroups": clrPeerRedGroups,
       "clrRedundancyConfigTable": clrRedundancyConfigTable,
       "clrRedundancyConfigEntry": clrRedundancyConfigEntry,
       "clrRedGroupId": clrRedGroupId,
       "clrRedPeerId": clrRedPeerId,
       "clrRedPriority": clrRedPriority,
       "clrRedPreempt": clrRedPreempt,
       "clrRedFailOverTime": clrRedFailOverTime,
       "clrRedState": clrRedState,
       "clrRedStateChangeTime": clrRedStateChangeTime,
       "clrRedContext": clrRedContext,
       "clrRedStorageType": clrRedStorageType,
       "clrRedRowStatus": clrRedRowStatus,
       "clrRedundancyInfoTable": clrRedundancyInfoTable,
       "clrRedundancyInfoEntry": clrRedundancyInfoEntry,
       "clrRedundancyPriority": clrRedundancyPriority,
       "clrRedundancyState": clrRedundancyState,
       "clrRedundancyStateChangeTime": clrRedundancyStateChangeTime,
       "clrRedundancyIpAddressType": clrRedundancyIpAddressType,
       "clrRedundancyIpAddress": clrRedundancyIpAddress,
       "clrStats": clrStats,
       "clrLBStatsTable": clrLBStatsTable,
       "clrLBStatsEntry": clrLBStatsEntry,
       "clrLBStatsSharedStickyEntries": clrLBStatsSharedStickyEntries,
       "clrLBStatsSentPackets": clrLBStatsSentPackets,
       "clrLBStatsSendFailures": clrLBStatsSendFailures,
       "clrLBStatsDroppedEntries": clrLBStatsDroppedEntries,
       "clrLBStatsReceivedPackets": clrLBStatsReceivedPackets,
       "clrLBStatsReceiveFailures": clrLBStatsReceiveFailures,
       "clrHAStatsTable": clrHAStatsTable,
       "clrHAStatsEntry": clrHAStatsEntry,
       "clrHAStatsTxHeartBeatMsgs": clrHAStatsTxHeartBeatMsgs,
       "clrHAStatsRxHeartBeatMsgs": clrHAStatsRxHeartBeatMsgs,
       "clrHAStatsMissedHeartBeatMsgs": clrHAStatsMissedHeartBeatMsgs,
       "clrHAStatsRxUniDirectionalHeartBeatMsgs": clrHAStatsRxUniDirectionalHeartBeatMsgs,
       "clrHAStatsHeartBeatTimeoutMismatches": clrHAStatsHeartBeatTimeoutMismatches,
       "clrHAStatsPeerUpEvents": clrHAStatsPeerUpEvents,
       "clrHAStatsPeerDownEvents": clrHAStatsPeerDownEvents,
       "clrNotifObjects": clrNotifObjects,
       "clrStateChangeNotifEnabled": clrStateChangeNotifEnabled,
       "ciscoLmRedundancyMIBConformance": ciscoLmRedundancyMIBConformance,
       "ciscoLmRedundancyMIBCompliances": ciscoLmRedundancyMIBCompliances,
       "ciscoLmRedundancyMIBCompliance": ciscoLmRedundancyMIBCompliance,
       "ciscoLmRedundancyMIBGroups": ciscoLmRedundancyMIBGroups,
       "clrPeerConfigGroup": clrPeerConfigGroup,
       "clrRedConfigGroup": clrRedConfigGroup,
       "clrRedInfoGroup": clrRedInfoGroup,
       "cslbxNotifControlGroup": cslbxNotifControlGroup,
       "cslbxNotifGroup": cslbxNotifGroup,
       "clrRedundancyStatsGroup": clrRedundancyStatsGroup}
)
