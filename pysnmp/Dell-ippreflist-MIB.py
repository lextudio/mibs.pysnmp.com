# SNMP MIB module (Dell-ippreflist-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dell-ippreflist-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:31 2024
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

(rnd,) = mibBuilder.importSymbols(
    "Dell-MIB",
    "rnd")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class RlIpPrefListEntryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("description", 2),
          ("rule", 1))
    )



class RlIpPrefListActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("permit", 2))
    )



class RlIpPrefListType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlIpPrefList_ObjectIdentity = ObjectIdentity
rlIpPrefList = _RlIpPrefList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 212)
)
_RlIpPrefListTable_Object = MibTable
rlIpPrefListTable = _RlIpPrefListTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1)
)
if mibBuilder.loadTexts:
    rlIpPrefListTable.setStatus("current")
_RlIpPrefListEntry_Object = MibTableRow
rlIpPrefListEntry = _RlIpPrefListEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1)
)
rlIpPrefListEntry.setIndexNames(
    (0, "Dell-ippreflist-MIB", "rlIpPrefListType"),
    (0, "Dell-ippreflist-MIB", "rlIpPrefListName"),
    (0, "Dell-ippreflist-MIB", "rlIpPrefListEntryIndex"),
)
if mibBuilder.loadTexts:
    rlIpPrefListEntry.setStatus("current")
_RlIpPrefListType_Type = RlIpPrefListType
_RlIpPrefListType_Object = MibTableColumn
rlIpPrefListType = _RlIpPrefListType_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 1),
    _RlIpPrefListType_Type()
)
rlIpPrefListType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpPrefListType.setStatus("current")


class _RlIpPrefListName_Type(DisplayString):
    """Custom type rlIpPrefListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlIpPrefListName_Type.__name__ = "DisplayString"
_RlIpPrefListName_Object = MibTableColumn
rlIpPrefListName = _RlIpPrefListName_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 2),
    _RlIpPrefListName_Type()
)
rlIpPrefListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpPrefListName.setStatus("current")


class _RlIpPrefListEntryIndex_Type(Unsigned32):
    """Custom type rlIpPrefListEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_RlIpPrefListEntryIndex_Type.__name__ = "Unsigned32"
_RlIpPrefListEntryIndex_Object = MibTableColumn
rlIpPrefListEntryIndex = _RlIpPrefListEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 3),
    _RlIpPrefListEntryIndex_Type()
)
rlIpPrefListEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpPrefListEntryIndex.setStatus("current")
_RlIpPrefListEntryType_Type = RlIpPrefListEntryType
_RlIpPrefListEntryType_Object = MibTableColumn
rlIpPrefListEntryType = _RlIpPrefListEntryType_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 4),
    _RlIpPrefListEntryType_Type()
)
rlIpPrefListEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListEntryType.setStatus("current")
_RlIpPrefListInetAddrType_Type = InetAddressType
_RlIpPrefListInetAddrType_Object = MibTableColumn
rlIpPrefListInetAddrType = _RlIpPrefListInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 5),
    _RlIpPrefListInetAddrType_Type()
)
rlIpPrefListInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListInetAddrType.setStatus("current")
_RlIpPrefListInetAddr_Type = InetAddress
_RlIpPrefListInetAddr_Object = MibTableColumn
rlIpPrefListInetAddr = _RlIpPrefListInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 6),
    _RlIpPrefListInetAddr_Type()
)
rlIpPrefListInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListInetAddr.setStatus("current")


class _RlIpPrefListPrefixLength_Type(Integer32):
    """Custom type rlIpPrefListPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RlIpPrefListPrefixLength_Type.__name__ = "Integer32"
_RlIpPrefListPrefixLength_Object = MibTableColumn
rlIpPrefListPrefixLength = _RlIpPrefListPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 7),
    _RlIpPrefListPrefixLength_Type()
)
rlIpPrefListPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListPrefixLength.setStatus("current")
_RlIpPrefListAction_Type = RlIpPrefListActionType
_RlIpPrefListAction_Object = MibTableColumn
rlIpPrefListAction = _RlIpPrefListAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 8),
    _RlIpPrefListAction_Type()
)
rlIpPrefListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListAction.setStatus("current")


class _RlIpPrefListGeLength_Type(Integer32):
    """Custom type rlIpPrefListGeLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RlIpPrefListGeLength_Type.__name__ = "Integer32"
_RlIpPrefListGeLength_Object = MibTableColumn
rlIpPrefListGeLength = _RlIpPrefListGeLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 9),
    _RlIpPrefListGeLength_Type()
)
rlIpPrefListGeLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListGeLength.setStatus("current")


class _RlIpPrefListLeLength_Type(Integer32):
    """Custom type rlIpPrefListLeLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RlIpPrefListLeLength_Type.__name__ = "Integer32"
_RlIpPrefListLeLength_Object = MibTableColumn
rlIpPrefListLeLength = _RlIpPrefListLeLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 10),
    _RlIpPrefListLeLength_Type()
)
rlIpPrefListLeLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListLeLength.setStatus("current")


class _RlIpPrefListDescription_Type(DisplayString):
    """Custom type rlIpPrefListDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RlIpPrefListDescription_Type.__name__ = "DisplayString"
_RlIpPrefListDescription_Object = MibTableColumn
rlIpPrefListDescription = _RlIpPrefListDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 11),
    _RlIpPrefListDescription_Type()
)
rlIpPrefListDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListDescription.setStatus("current")
_RlIpPrefListHitCount_Type = Integer32
_RlIpPrefListHitCount_Object = MibTableColumn
rlIpPrefListHitCount = _RlIpPrefListHitCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 12),
    _RlIpPrefListHitCount_Type()
)
rlIpPrefListHitCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpPrefListHitCount.setStatus("current")
_RlIpPrefListRowStatus_Type = RowStatus
_RlIpPrefListRowStatus_Object = MibTableColumn
rlIpPrefListRowStatus = _RlIpPrefListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 1, 1, 13),
    _RlIpPrefListRowStatus_Type()
)
rlIpPrefListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpPrefListRowStatus.setStatus("current")
_RlIpPrefListInfoTable_Object = MibTable
rlIpPrefListInfoTable = _RlIpPrefListInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 2)
)
if mibBuilder.loadTexts:
    rlIpPrefListInfoTable.setStatus("current")
_RlIpPrefListInfoEntry_Object = MibTableRow
rlIpPrefListInfoEntry = _RlIpPrefListInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 2, 1)
)
rlIpPrefListInfoEntry.setIndexNames(
    (0, "Dell-ippreflist-MIB", "rlIpPrefListInfoType"),
    (0, "Dell-ippreflist-MIB", "rlIpPrefListInfoName"),
)
if mibBuilder.loadTexts:
    rlIpPrefListInfoEntry.setStatus("current")
_RlIpPrefListInfoType_Type = RlIpPrefListType
_RlIpPrefListInfoType_Object = MibTableColumn
rlIpPrefListInfoType = _RlIpPrefListInfoType_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 1),
    _RlIpPrefListInfoType_Type()
)
rlIpPrefListInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpPrefListInfoType.setStatus("current")


class _RlIpPrefListInfoName_Type(DisplayString):
    """Custom type rlIpPrefListInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlIpPrefListInfoName_Type.__name__ = "DisplayString"
_RlIpPrefListInfoName_Object = MibTableColumn
rlIpPrefListInfoName = _RlIpPrefListInfoName_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 2),
    _RlIpPrefListInfoName_Type()
)
rlIpPrefListInfoName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpPrefListInfoName.setStatus("current")
_RlIpPrefListInfoEntriesNumber_Type = Integer32
_RlIpPrefListInfoEntriesNumber_Object = MibTableColumn
rlIpPrefListInfoEntriesNumber = _RlIpPrefListInfoEntriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 3),
    _RlIpPrefListInfoEntriesNumber_Type()
)
rlIpPrefListInfoEntriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpPrefListInfoEntriesNumber.setStatus("current")
_RlIpPrefListInfoRangeEntries_Type = Integer32
_RlIpPrefListInfoRangeEntries_Object = MibTableColumn
rlIpPrefListInfoRangeEntries = _RlIpPrefListInfoRangeEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 4),
    _RlIpPrefListInfoRangeEntries_Type()
)
rlIpPrefListInfoRangeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpPrefListInfoRangeEntries.setStatus("current")
_RlIpPrefListInfoNextFreeIndex_Type = Integer32
_RlIpPrefListInfoNextFreeIndex_Object = MibTableColumn
rlIpPrefListInfoNextFreeIndex = _RlIpPrefListInfoNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 212, 2, 1, 5),
    _RlIpPrefListInfoNextFreeIndex_Type()
)
rlIpPrefListInfoNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpPrefListInfoNextFreeIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-ippreflist-MIB",
    **{"RlIpPrefListEntryType": RlIpPrefListEntryType,
       "RlIpPrefListActionType": RlIpPrefListActionType,
       "RlIpPrefListType": RlIpPrefListType,
       "rlIpPrefList": rlIpPrefList,
       "rlIpPrefListTable": rlIpPrefListTable,
       "rlIpPrefListEntry": rlIpPrefListEntry,
       "rlIpPrefListType": rlIpPrefListType,
       "rlIpPrefListName": rlIpPrefListName,
       "rlIpPrefListEntryIndex": rlIpPrefListEntryIndex,
       "rlIpPrefListEntryType": rlIpPrefListEntryType,
       "rlIpPrefListInetAddrType": rlIpPrefListInetAddrType,
       "rlIpPrefListInetAddr": rlIpPrefListInetAddr,
       "rlIpPrefListPrefixLength": rlIpPrefListPrefixLength,
       "rlIpPrefListAction": rlIpPrefListAction,
       "rlIpPrefListGeLength": rlIpPrefListGeLength,
       "rlIpPrefListLeLength": rlIpPrefListLeLength,
       "rlIpPrefListDescription": rlIpPrefListDescription,
       "rlIpPrefListHitCount": rlIpPrefListHitCount,
       "rlIpPrefListRowStatus": rlIpPrefListRowStatus,
       "rlIpPrefListInfoTable": rlIpPrefListInfoTable,
       "rlIpPrefListInfoEntry": rlIpPrefListInfoEntry,
       "rlIpPrefListInfoType": rlIpPrefListInfoType,
       "rlIpPrefListInfoName": rlIpPrefListInfoName,
       "rlIpPrefListInfoEntriesNumber": rlIpPrefListInfoEntriesNumber,
       "rlIpPrefListInfoRangeEntries": rlIpPrefListInfoRangeEntries,
       "rlIpPrefListInfoNextFreeIndex": rlIpPrefListInfoNextFreeIndex}
)
