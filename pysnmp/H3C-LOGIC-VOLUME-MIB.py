# SNMP MIB module (H3C-LOGIC-VOLUME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-LOGIC-VOLUME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:51 2024
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

(H3cLvIDType,
 H3cRaidIDType,
 H3cSessionIDType,
 H3cStorageActionType,
 H3cStorageEnableState,
 H3cStorageLedStateType,
 H3cWwpnListType,
 h3cStorageRef) = mibBuilder.importSymbols(
    "H3C-STORAGE-REF-MIB",
    "H3cLvIDType",
    "H3cRaidIDType",
    "H3cSessionIDType",
    "H3cStorageActionType",
    "H3cStorageEnableState",
    "H3cStorageLedStateType",
    "H3cWwpnListType",
    "h3cStorageRef")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cLogicVolume = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cLvMibObjects_ObjectIdentity = ObjectIdentity
h3cLvMibObjects = _H3cLvMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1)
)
_H3cLogicResourceCapacityObject_ObjectIdentity = ObjectIdentity
h3cLogicResourceCapacityObject = _H3cLogicResourceCapacityObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1)
)
_H3cLvCount_Type = Integer32
_H3cLvCount_Object = MibScalar
h3cLvCount = _H3cLvCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 1),
    _H3cLvCount_Type()
)
h3cLvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvCount.setStatus("current")
_H3cLvMaxSize_Type = Integer32
_H3cLvMaxSize_Object = MibScalar
h3cLvMaxSize = _H3cLvMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 2),
    _H3cLvMaxSize_Type()
)
h3cLvMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cLvMaxSize.setUnits("TB")
_H3cTargetCount_Type = Integer32
_H3cTargetCount_Object = MibScalar
h3cTargetCount = _H3cTargetCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 3),
    _H3cTargetCount_Type()
)
h3cTargetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTargetCount.setStatus("current")
_H3cInitiatorCount_Type = Integer32
_H3cInitiatorCount_Object = MibScalar
h3cInitiatorCount = _H3cInitiatorCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 4),
    _H3cInitiatorCount_Type()
)
h3cInitiatorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cInitiatorCount.setStatus("current")
_H3cSanClientCount_Type = Integer32
_H3cSanClientCount_Object = MibScalar
h3cSanClientCount = _H3cSanClientCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 1, 5),
    _H3cSanClientCount_Type()
)
h3cSanClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSanClientCount.setStatus("current")
_H3cLogicVolumeResource_ObjectIdentity = ObjectIdentity
h3cLogicVolumeResource = _H3cLogicVolumeResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2)
)
_H3cLvCreateIndex_Type = H3cLvIDType
_H3cLvCreateIndex_Object = MibScalar
h3cLvCreateIndex = _H3cLvCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 1),
    _H3cLvCreateIndex_Type()
)
h3cLvCreateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvCreateIndex.setStatus("current")
_H3cLvTable_Object = MibTable
h3cLvTable = _H3cLvTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cLvTable.setStatus("current")
_H3cLvEntry_Object = MibTableRow
h3cLvEntry = _H3cLvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1)
)
h3cLvEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"),
)
if mibBuilder.loadTexts:
    h3cLvEntry.setStatus("current")
_H3cLvIndex_Type = H3cLvIDType
_H3cLvIndex_Object = MibTableColumn
h3cLvIndex = _H3cLvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 1),
    _H3cLvIndex_Type()
)
h3cLvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLvIndex.setStatus("current")


class _H3cLvName_Type(OctetString):
    """Custom type h3cLvName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cLvName_Type.__name__ = "OctetString"
_H3cLvName_Object = MibTableColumn
h3cLvName = _H3cLvName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 2),
    _H3cLvName_Type()
)
h3cLvName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLvName.setStatus("current")
_H3cLvTotalSize_Type = Integer32
_H3cLvTotalSize_Object = MibTableColumn
h3cLvTotalSize = _H3cLvTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 3),
    _H3cLvTotalSize_Type()
)
h3cLvTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cLvTotalSize.setUnits("MB")
_H3cLvCreateRaidUuid_Type = H3cRaidIDType
_H3cLvCreateRaidUuid_Object = MibTableColumn
h3cLvCreateRaidUuid = _H3cLvCreateRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 4),
    _H3cLvCreateRaidUuid_Type()
)
h3cLvCreateRaidUuid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLvCreateRaidUuid.setStatus("current")
_H3cLvCreateRaidSize_Type = Integer32
_H3cLvCreateRaidSize_Object = MibTableColumn
h3cLvCreateRaidSize = _H3cLvCreateRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 5),
    _H3cLvCreateRaidSize_Type()
)
h3cLvCreateRaidSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLvCreateRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cLvCreateRaidSize.setUnits("MB")
_H3cLvSedInquiryStringKeep_Type = TruthValue
_H3cLvSedInquiryStringKeep_Object = MibTableColumn
h3cLvSedInquiryStringKeep = _H3cLvSedInquiryStringKeep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 6),
    _H3cLvSedInquiryStringKeep_Type()
)
h3cLvSedInquiryStringKeep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLvSedInquiryStringKeep.setStatus("current")
_H3cLvSedRaidUuid_Type = H3cRaidIDType
_H3cLvSedRaidUuid_Object = MibTableColumn
h3cLvSedRaidUuid = _H3cLvSedRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 7),
    _H3cLvSedRaidUuid_Type()
)
h3cLvSedRaidUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvSedRaidUuid.setStatus("current")


class _H3cLvState_Type(Integer32):
    """Custom type h3cLvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("conflict", 3),
          ("unusable", 2),
          ("usable", 1))
    )


_H3cLvState_Type.__name__ = "Integer32"
_H3cLvState_Object = MibTableColumn
h3cLvState = _H3cLvState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 8),
    _H3cLvState_Type()
)
h3cLvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvState.setStatus("current")


class _H3cLvAssigned_Type(Integer32):
    """Custom type h3cLvAssigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 2),
          ("use", 1))
    )


_H3cLvAssigned_Type.__name__ = "Integer32"
_H3cLvAssigned_Object = MibTableColumn
h3cLvAssigned = _H3cLvAssigned_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 9),
    _H3cLvAssigned_Type()
)
h3cLvAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvAssigned.setStatus("current")


class _H3cLvType_Type(Integer32):
    """Custom type h3cLvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("serviceEnabled", 3),
          ("virtual", 1))
    )


_H3cLvType_Type.__name__ = "Integer32"
_H3cLvType_Object = MibTableColumn
h3cLvType = _H3cLvType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 10),
    _H3cLvType_Type()
)
h3cLvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvType.setStatus("current")
_H3cLvExtendTimes_Type = Integer32
_H3cLvExtendTimes_Object = MibTableColumn
h3cLvExtendTimes = _H3cLvExtendTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 11),
    _H3cLvExtendTimes_Type()
)
h3cLvExtendTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvExtendTimes.setStatus("current")
_H3cLvRowStatus_Type = RowStatus
_H3cLvRowStatus_Object = MibTableColumn
h3cLvRowStatus = _H3cLvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 2, 2, 1, 12),
    _H3cLvRowStatus_Type()
)
h3cLvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLvRowStatus.setStatus("current")
_H3cLvExtTable_Object = MibTable
h3cLvExtTable = _H3cLvExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3)
)
if mibBuilder.loadTexts:
    h3cLvExtTable.setStatus("current")
_H3cLvExtEntry_Object = MibTableRow
h3cLvExtEntry = _H3cLvExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1)
)
h3cLvExtEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvRaidUuid"),
)
if mibBuilder.loadTexts:
    h3cLvExtEntry.setStatus("current")
_H3cLvRaidUuid_Type = H3cRaidIDType
_H3cLvRaidUuid_Object = MibTableColumn
h3cLvRaidUuid = _H3cLvRaidUuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 1),
    _H3cLvRaidUuid_Type()
)
h3cLvRaidUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLvRaidUuid.setStatus("current")


class _H3cLvExtSize_Type(Integer32):
    """Custom type h3cLvExtSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cLvExtSize_Type.__name__ = "Integer32"
_H3cLvExtSize_Object = MibTableColumn
h3cLvExtSize = _H3cLvExtSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 2),
    _H3cLvExtSize_Type()
)
h3cLvExtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLvExtSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cLvExtSize.setUnits("MB")
_H3cLvRaidSize_Type = Integer32
_H3cLvRaidSize_Object = MibTableColumn
h3cLvRaidSize = _H3cLvRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 3),
    _H3cLvRaidSize_Type()
)
h3cLvRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLvRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cLvRaidSize.setUnits("MB")
_H3cLvExtRowStatus_Type = RowStatus
_H3cLvExtRowStatus_Object = MibTableColumn
h3cLvExtRowStatus = _H3cLvExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 3, 1, 4),
    _H3cLvExtRowStatus_Type()
)
h3cLvExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLvExtRowStatus.setStatus("current")
_H3cTargetResource_ObjectIdentity = ObjectIdentity
h3cTargetResource = _H3cTargetResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4)
)
_H3cTargetCreateIndex_Type = Integer32
_H3cTargetCreateIndex_Object = MibScalar
h3cTargetCreateIndex = _H3cTargetCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 1),
    _H3cTargetCreateIndex_Type()
)
h3cTargetCreateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTargetCreateIndex.setStatus("current")
_H3cTargetTable_Object = MibTable
h3cTargetTable = _H3cTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h3cTargetTable.setStatus("current")
_H3cTargetEntry_Object = MibTableRow
h3cTargetEntry = _H3cTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1)
)
h3cTargetEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"),
)
if mibBuilder.loadTexts:
    h3cTargetEntry.setStatus("current")
_H3cTargetId_Type = Integer32
_H3cTargetId_Object = MibTableColumn
h3cTargetId = _H3cTargetId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 1),
    _H3cTargetId_Type()
)
h3cTargetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTargetId.setStatus("current")


class _H3cTargetName_Type(OctetString):
    """Custom type h3cTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 223),
    )


_H3cTargetName_Type.__name__ = "OctetString"
_H3cTargetName_Object = MibTableColumn
h3cTargetName = _H3cTargetName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 2),
    _H3cTargetName_Type()
)
h3cTargetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTargetName.setStatus("current")


class _H3cTargetMinLun_Type(Integer32):
    """Custom type h3cTargetMinLun based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_H3cTargetMinLun_Type.__name__ = "Integer32"
_H3cTargetMinLun_Object = MibTableColumn
h3cTargetMinLun = _H3cTargetMinLun_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 3),
    _H3cTargetMinLun_Type()
)
h3cTargetMinLun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTargetMinLun.setStatus("current")
_H3cTargetRowStatus_Type = RowStatus
_H3cTargetRowStatus_Object = MibTableColumn
h3cTargetRowStatus = _H3cTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 4, 2, 1, 4),
    _H3cTargetRowStatus_Type()
)
h3cTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTargetRowStatus.setStatus("current")
_H3cTargetAddressTable_Object = MibTable
h3cTargetAddressTable = _H3cTargetAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5)
)
if mibBuilder.loadTexts:
    h3cTargetAddressTable.setStatus("current")
_H3cTargetAddressEntry_Object = MibTableRow
h3cTargetAddressEntry = _H3cTargetAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1)
)
h3cTargetAddressEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetIpAddrType"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetIpAddress"),
)
if mibBuilder.loadTexts:
    h3cTargetAddressEntry.setStatus("current")
_H3cTargetIpAddress_Type = InetAddress
_H3cTargetIpAddress_Object = MibTableColumn
h3cTargetIpAddress = _H3cTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1, 1),
    _H3cTargetIpAddress_Type()
)
h3cTargetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTargetIpAddress.setStatus("current")
_H3cTargetIpAddrType_Type = InetAddressType
_H3cTargetIpAddrType_Object = MibTableColumn
h3cTargetIpAddrType = _H3cTargetIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1, 2),
    _H3cTargetIpAddrType_Type()
)
h3cTargetIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTargetIpAddrType.setStatus("current")
_H3cTargetIpRowStatus_Type = RowStatus
_H3cTargetIpRowStatus_Object = MibTableColumn
h3cTargetIpRowStatus = _H3cTargetIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 5, 1, 3),
    _H3cTargetIpRowStatus_Type()
)
h3cTargetIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTargetIpRowStatus.setStatus("current")
_H3cTargetLvAssignTable_Object = MibTable
h3cTargetLvAssignTable = _H3cTargetLvAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6)
)
if mibBuilder.loadTexts:
    h3cTargetLvAssignTable.setStatus("current")
_H3cTargetLvAssignEntry_Object = MibTableRow
h3cTargetLvAssignEntry = _H3cTargetLvAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6, 1)
)
h3cTargetLvAssignEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"),
)
if mibBuilder.loadTexts:
    h3cTargetLvAssignEntry.setStatus("current")


class _H3cTargetLvLun_Type(Integer32):
    """Custom type h3cTargetLvLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_H3cTargetLvLun_Type.__name__ = "Integer32"
_H3cTargetLvLun_Object = MibTableColumn
h3cTargetLvLun = _H3cTargetLvLun_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6, 1, 1),
    _H3cTargetLvLun_Type()
)
h3cTargetLvLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTargetLvLun.setStatus("current")
_H3cTargetLvRowStatus_Type = RowStatus
_H3cTargetLvRowStatus_Object = MibTableColumn
h3cTargetLvRowStatus = _H3cTargetLvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 6, 1, 2),
    _H3cTargetLvRowStatus_Type()
)
h3cTargetLvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTargetLvRowStatus.setStatus("current")
_H3cInitiatorResource_ObjectIdentity = ObjectIdentity
h3cInitiatorResource = _H3cInitiatorResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7)
)
_H3cInitiatorCreateIndex_Type = Integer32
_H3cInitiatorCreateIndex_Object = MibScalar
h3cInitiatorCreateIndex = _H3cInitiatorCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 1),
    _H3cInitiatorCreateIndex_Type()
)
h3cInitiatorCreateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cInitiatorCreateIndex.setStatus("current")
_H3cInitiatorTable_Object = MibTable
h3cInitiatorTable = _H3cInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    h3cInitiatorTable.setStatus("current")
_H3cInitiatorEntry_Object = MibTableRow
h3cInitiatorEntry = _H3cInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1)
)
h3cInitiatorEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cSanClientId"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cInitiatorId"),
)
if mibBuilder.loadTexts:
    h3cInitiatorEntry.setStatus("current")
_H3cInitiatorId_Type = Integer32
_H3cInitiatorId_Object = MibTableColumn
h3cInitiatorId = _H3cInitiatorId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1, 1),
    _H3cInitiatorId_Type()
)
h3cInitiatorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cInitiatorId.setStatus("current")


class _H3cInitiatorName_Type(OctetString):
    """Custom type h3cInitiatorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 223),
    )


_H3cInitiatorName_Type.__name__ = "OctetString"
_H3cInitiatorName_Object = MibTableColumn
h3cInitiatorName = _H3cInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1, 2),
    _H3cInitiatorName_Type()
)
h3cInitiatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cInitiatorName.setStatus("current")
_H3cInitiatorRowStatus_Type = RowStatus
_H3cInitiatorRowStatus_Object = MibTableColumn
h3cInitiatorRowStatus = _H3cInitiatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 7, 2, 1, 3),
    _H3cInitiatorRowStatus_Type()
)
h3cInitiatorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cInitiatorRowStatus.setStatus("current")
_H3cTargetInitiatorAssociateTable_Object = MibTable
h3cTargetInitiatorAssociateTable = _H3cTargetInitiatorAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8)
)
if mibBuilder.loadTexts:
    h3cTargetInitiatorAssociateTable.setStatus("current")
_H3cTargetInitiatorAssociateEntry_Object = MibTableRow
h3cTargetInitiatorAssociateEntry = _H3cTargetInitiatorAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1)
)
h3cTargetInitiatorAssociateEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cInitiatorId"),
)
if mibBuilder.loadTexts:
    h3cTargetInitiatorAssociateEntry.setStatus("current")


class _H3cTIAccessMode_Type(Integer32):
    """Custom type h3cTIAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonexclusive", 3),
          ("read", 1),
          ("write", 2))
    )


_H3cTIAccessMode_Type.__name__ = "Integer32"
_H3cTIAccessMode_Object = MibTableColumn
h3cTIAccessMode = _H3cTIAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 1),
    _H3cTIAccessMode_Type()
)
h3cTIAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTIAccessMode.setStatus("current")


class _H3cTIChap_Type(H3cStorageEnableState):
    """Custom type h3cTIChap based on H3cStorageEnableState"""


_H3cTIChap_Object = MibTableColumn
h3cTIChap = _H3cTIChap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 2),
    _H3cTIChap_Type()
)
h3cTIChap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTIChap.setStatus("current")


class _H3cTIUserName_Type(OctetString):
    """Custom type h3cTIUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_H3cTIUserName_Type.__name__ = "OctetString"
_H3cTIUserName_Object = MibTableColumn
h3cTIUserName = _H3cTIUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 3),
    _H3cTIUserName_Type()
)
h3cTIUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTIUserName.setStatus("current")


class _H3cTIPassword_Type(OctetString):
    """Custom type h3cTIPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 16),
    )


_H3cTIPassword_Type.__name__ = "OctetString"
_H3cTIPassword_Object = MibTableColumn
h3cTIPassword = _H3cTIPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 4),
    _H3cTIPassword_Type()
)
h3cTIPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTIPassword.setStatus("current")
_H3cTIRowStatus_Type = RowStatus
_H3cTIRowStatus_Object = MibTableColumn
h3cTIRowStatus = _H3cTIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 8, 1, 5),
    _H3cTIRowStatus_Type()
)
h3cTIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTIRowStatus.setStatus("current")
_H3cTISessionTable_Object = MibTable
h3cTISessionTable = _H3cTISessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9)
)
if mibBuilder.loadTexts:
    h3cTISessionTable.setStatus("current")
_H3cTISessionEntry_Object = MibTableRow
h3cTISessionEntry = _H3cTISessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1)
)
h3cTISessionEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTargetId"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cTISessionId"),
)
if mibBuilder.loadTexts:
    h3cTISessionEntry.setStatus("current")
_H3cTISessionId_Type = H3cSessionIDType
_H3cTISessionId_Object = MibTableColumn
h3cTISessionId = _H3cTISessionId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1, 1),
    _H3cTISessionId_Type()
)
h3cTISessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTISessionId.setStatus("current")
_H3cTISessionConnectionCount_Type = Counter32
_H3cTISessionConnectionCount_Object = MibTableColumn
h3cTISessionConnectionCount = _H3cTISessionConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1, 2),
    _H3cTISessionConnectionCount_Type()
)
h3cTISessionConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTISessionConnectionCount.setStatus("current")


class _H3cTISessionInitiatorName_Type(OctetString):
    """Custom type h3cTISessionInitiatorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 223),
    )


_H3cTISessionInitiatorName_Type.__name__ = "OctetString"
_H3cTISessionInitiatorName_Object = MibTableColumn
h3cTISessionInitiatorName = _H3cTISessionInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 9, 1, 3),
    _H3cTISessionInitiatorName_Type()
)
h3cTISessionInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTISessionInitiatorName.setStatus("current")
_H3cSanClientResource_ObjectIdentity = ObjectIdentity
h3cSanClientResource = _H3cSanClientResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10)
)
_H3cSanClientCreateIndex_Type = Integer32
_H3cSanClientCreateIndex_Object = MibScalar
h3cSanClientCreateIndex = _H3cSanClientCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 1),
    _H3cSanClientCreateIndex_Type()
)
h3cSanClientCreateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSanClientCreateIndex.setStatus("current")
_H3cSanClientTable_Object = MibTable
h3cSanClientTable = _H3cSanClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2)
)
if mibBuilder.loadTexts:
    h3cSanClientTable.setStatus("current")
_H3cSanClientEntry_Object = MibTableRow
h3cSanClientEntry = _H3cSanClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1)
)
h3cSanClientEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cSanClientId"),
)
if mibBuilder.loadTexts:
    h3cSanClientEntry.setStatus("current")
_H3cSanClientId_Type = Integer32
_H3cSanClientId_Object = MibTableColumn
h3cSanClientId = _H3cSanClientId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 1),
    _H3cSanClientId_Type()
)
h3cSanClientId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSanClientId.setStatus("current")


class _H3cSanClientName_Type(OctetString):
    """Custom type h3cSanClientName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cSanClientName_Type.__name__ = "OctetString"
_H3cSanClientName_Object = MibTableColumn
h3cSanClientName = _H3cSanClientName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 2),
    _H3cSanClientName_Type()
)
h3cSanClientName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSanClientName.setStatus("current")


class _H3cSanClientType_Type(Integer32):
    """Custom type h3cSanClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fc", 2),
          ("iscsi", 1))
    )


_H3cSanClientType_Type.__name__ = "Integer32"
_H3cSanClientType_Object = MibTableColumn
h3cSanClientType = _H3cSanClientType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 3),
    _H3cSanClientType_Type()
)
h3cSanClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSanClientType.setStatus("current")
_H3cFcInitiatorWwpnList_Type = H3cWwpnListType
_H3cFcInitiatorWwpnList_Object = MibTableColumn
h3cFcInitiatorWwpnList = _H3cFcInitiatorWwpnList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 4),
    _H3cFcInitiatorWwpnList_Type()
)
h3cFcInitiatorWwpnList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcInitiatorWwpnList.setStatus("current")


class _H3cFcAccessMode_Type(Integer32):
    """Custom type h3cFcAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonexclusive", 3),
          ("read", 1),
          ("write", 2))
    )


_H3cFcAccessMode_Type.__name__ = "Integer32"
_H3cFcAccessMode_Object = MibTableColumn
h3cFcAccessMode = _H3cFcAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 6),
    _H3cFcAccessMode_Type()
)
h3cFcAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcAccessMode.setStatus("current")
_H3cSanClientRowStatus_Type = RowStatus
_H3cSanClientRowStatus_Object = MibTableColumn
h3cSanClientRowStatus = _H3cSanClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 10, 2, 1, 7),
    _H3cSanClientRowStatus_Type()
)
h3cSanClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSanClientRowStatus.setStatus("current")
_H3cFcLogicResourceTable_Object = MibTable
h3cFcLogicResourceTable = _H3cFcLogicResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11)
)
if mibBuilder.loadTexts:
    h3cFcLogicResourceTable.setStatus("current")
_H3cFcLogicResourceEntry_Object = MibTableRow
h3cFcLogicResourceEntry = _H3cFcLogicResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1)
)
h3cFcLogicResourceEntry.setIndexNames(
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cSanClientId"),
    (0, "H3C-LOGIC-VOLUME-MIB", "h3cLvIndex"),
)
if mibBuilder.loadTexts:
    h3cFcLogicResourceEntry.setStatus("current")


class _H3cFcLvLun_Type(Integer32):
    """Custom type h3cFcLvLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_H3cFcLvLun_Type.__name__ = "Integer32"
_H3cFcLvLun_Object = MibTableColumn
h3cFcLvLun = _H3cFcLvLun_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 1),
    _H3cFcLvLun_Type()
)
h3cFcLvLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcLvLun.setStatus("current")
_H3cFcTargetWwpnName_Type = H3cWwpnListType
_H3cFcTargetWwpnName_Object = MibTableColumn
h3cFcTargetWwpnName = _H3cFcTargetWwpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 2),
    _H3cFcTargetWwpnName_Type()
)
h3cFcTargetWwpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcTargetWwpnName.setStatus("current")
_H3cFcInitiatorWwpnName_Type = H3cWwpnListType
_H3cFcInitiatorWwpnName_Object = MibTableColumn
h3cFcInitiatorWwpnName = _H3cFcInitiatorWwpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 3),
    _H3cFcInitiatorWwpnName_Type()
)
h3cFcInitiatorWwpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcInitiatorWwpnName.setStatus("current")
_H3cFcLvRowStatus_Type = RowStatus
_H3cFcLvRowStatus_Object = MibTableColumn
h3cFcLvRowStatus = _H3cFcLvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 5, 1, 11, 1, 4),
    _H3cFcLvRowStatus_Type()
)
h3cFcLvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcLvRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-LOGIC-VOLUME-MIB",
    **{"h3cLogicVolume": h3cLogicVolume,
       "h3cLvMibObjects": h3cLvMibObjects,
       "h3cLogicResourceCapacityObject": h3cLogicResourceCapacityObject,
       "h3cLvCount": h3cLvCount,
       "h3cLvMaxSize": h3cLvMaxSize,
       "h3cTargetCount": h3cTargetCount,
       "h3cInitiatorCount": h3cInitiatorCount,
       "h3cSanClientCount": h3cSanClientCount,
       "h3cLogicVolumeResource": h3cLogicVolumeResource,
       "h3cLvCreateIndex": h3cLvCreateIndex,
       "h3cLvTable": h3cLvTable,
       "h3cLvEntry": h3cLvEntry,
       "h3cLvIndex": h3cLvIndex,
       "h3cLvName": h3cLvName,
       "h3cLvTotalSize": h3cLvTotalSize,
       "h3cLvCreateRaidUuid": h3cLvCreateRaidUuid,
       "h3cLvCreateRaidSize": h3cLvCreateRaidSize,
       "h3cLvSedInquiryStringKeep": h3cLvSedInquiryStringKeep,
       "h3cLvSedRaidUuid": h3cLvSedRaidUuid,
       "h3cLvState": h3cLvState,
       "h3cLvAssigned": h3cLvAssigned,
       "h3cLvType": h3cLvType,
       "h3cLvExtendTimes": h3cLvExtendTimes,
       "h3cLvRowStatus": h3cLvRowStatus,
       "h3cLvExtTable": h3cLvExtTable,
       "h3cLvExtEntry": h3cLvExtEntry,
       "h3cLvRaidUuid": h3cLvRaidUuid,
       "h3cLvExtSize": h3cLvExtSize,
       "h3cLvRaidSize": h3cLvRaidSize,
       "h3cLvExtRowStatus": h3cLvExtRowStatus,
       "h3cTargetResource": h3cTargetResource,
       "h3cTargetCreateIndex": h3cTargetCreateIndex,
       "h3cTargetTable": h3cTargetTable,
       "h3cTargetEntry": h3cTargetEntry,
       "h3cTargetId": h3cTargetId,
       "h3cTargetName": h3cTargetName,
       "h3cTargetMinLun": h3cTargetMinLun,
       "h3cTargetRowStatus": h3cTargetRowStatus,
       "h3cTargetAddressTable": h3cTargetAddressTable,
       "h3cTargetAddressEntry": h3cTargetAddressEntry,
       "h3cTargetIpAddress": h3cTargetIpAddress,
       "h3cTargetIpAddrType": h3cTargetIpAddrType,
       "h3cTargetIpRowStatus": h3cTargetIpRowStatus,
       "h3cTargetLvAssignTable": h3cTargetLvAssignTable,
       "h3cTargetLvAssignEntry": h3cTargetLvAssignEntry,
       "h3cTargetLvLun": h3cTargetLvLun,
       "h3cTargetLvRowStatus": h3cTargetLvRowStatus,
       "h3cInitiatorResource": h3cInitiatorResource,
       "h3cInitiatorCreateIndex": h3cInitiatorCreateIndex,
       "h3cInitiatorTable": h3cInitiatorTable,
       "h3cInitiatorEntry": h3cInitiatorEntry,
       "h3cInitiatorId": h3cInitiatorId,
       "h3cInitiatorName": h3cInitiatorName,
       "h3cInitiatorRowStatus": h3cInitiatorRowStatus,
       "h3cTargetInitiatorAssociateTable": h3cTargetInitiatorAssociateTable,
       "h3cTargetInitiatorAssociateEntry": h3cTargetInitiatorAssociateEntry,
       "h3cTIAccessMode": h3cTIAccessMode,
       "h3cTIChap": h3cTIChap,
       "h3cTIUserName": h3cTIUserName,
       "h3cTIPassword": h3cTIPassword,
       "h3cTIRowStatus": h3cTIRowStatus,
       "h3cTISessionTable": h3cTISessionTable,
       "h3cTISessionEntry": h3cTISessionEntry,
       "h3cTISessionId": h3cTISessionId,
       "h3cTISessionConnectionCount": h3cTISessionConnectionCount,
       "h3cTISessionInitiatorName": h3cTISessionInitiatorName,
       "h3cSanClientResource": h3cSanClientResource,
       "h3cSanClientCreateIndex": h3cSanClientCreateIndex,
       "h3cSanClientTable": h3cSanClientTable,
       "h3cSanClientEntry": h3cSanClientEntry,
       "h3cSanClientId": h3cSanClientId,
       "h3cSanClientName": h3cSanClientName,
       "h3cSanClientType": h3cSanClientType,
       "h3cFcInitiatorWwpnList": h3cFcInitiatorWwpnList,
       "h3cFcAccessMode": h3cFcAccessMode,
       "h3cSanClientRowStatus": h3cSanClientRowStatus,
       "h3cFcLogicResourceTable": h3cFcLogicResourceTable,
       "h3cFcLogicResourceEntry": h3cFcLogicResourceEntry,
       "h3cFcLvLun": h3cFcLvLun,
       "h3cFcTargetWwpnName": h3cFcTargetWwpnName,
       "h3cFcInitiatorWwpnName": h3cFcInitiatorWwpnName,
       "h3cFcLvRowStatus": h3cFcLvRowStatus}
)
