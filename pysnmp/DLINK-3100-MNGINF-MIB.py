# SNMP MIB module (DLINK-3100-MNGINF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-MNGINF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:08 2024
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
    "DLINK-3100-MIB",
    "rnd")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlMngInf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89)
)
rlMngInf.setRevisions(
        ("2003-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlMngInfServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dontCare", 0),
          ("http", 3),
          ("https", 4),
          ("icmp", 6),
          ("snmp", 2),
          ("ssh", 5),
          ("telnet", 1))
    )



class RlMngInfActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )



# MIB Managed Objects in the order of their OIDs

_RlMngInfMibVersion_Type = Integer32
_RlMngInfMibVersion_Object = MibScalar
rlMngInfMibVersion = _RlMngInfMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 1),
    _RlMngInfMibVersion_Type()
)
rlMngInfMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMngInfMibVersion.setStatus("current")
_RlMngInfEnable_Type = TruthValue
_RlMngInfEnable_Object = MibScalar
rlMngInfEnable = _RlMngInfEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 2),
    _RlMngInfEnable_Type()
)
rlMngInfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfEnable.setStatus("current")


class _RlMngInfActiveListName_Type(DisplayString):
    """Custom type rlMngInfActiveListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlMngInfActiveListName_Type.__name__ = "DisplayString"
_RlMngInfActiveListName_Object = MibScalar
rlMngInfActiveListName = _RlMngInfActiveListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 3),
    _RlMngInfActiveListName_Type()
)
rlMngInfActiveListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfActiveListName.setStatus("current")
_RlMngInfListTable_Object = MibTable
rlMngInfListTable = _RlMngInfListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4)
)
if mibBuilder.loadTexts:
    rlMngInfListTable.setStatus("current")
_RlMngInfListEntry_Object = MibTableRow
rlMngInfListEntry = _RlMngInfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1)
)
rlMngInfListEntry.setIndexNames(
    (0, "DLINK-3100-MNGINF-MIB", "rlMngInfListName"),
    (0, "DLINK-3100-MNGINF-MIB", "rlMngInfListPriority"),
)
if mibBuilder.loadTexts:
    rlMngInfListEntry.setStatus("current")


class _RlMngInfListName_Type(DisplayString):
    """Custom type rlMngInfListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlMngInfListName_Type.__name__ = "DisplayString"
_RlMngInfListName_Object = MibTableColumn
rlMngInfListName = _RlMngInfListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 1),
    _RlMngInfListName_Type()
)
rlMngInfListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMngInfListName.setStatus("current")


class _RlMngInfListPriority_Type(Unsigned32):
    """Custom type rlMngInfListPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlMngInfListPriority_Type.__name__ = "Unsigned32"
_RlMngInfListPriority_Object = MibTableColumn
rlMngInfListPriority = _RlMngInfListPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 2),
    _RlMngInfListPriority_Type()
)
rlMngInfListPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMngInfListPriority.setStatus("current")
_RlMngInfListIfIndex_Type = Unsigned32
_RlMngInfListIfIndex_Object = MibTableColumn
rlMngInfListIfIndex = _RlMngInfListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 3),
    _RlMngInfListIfIndex_Type()
)
rlMngInfListIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListIfIndex.setStatus("current")
_RlMngInfListIpAddr_Type = IpAddress
_RlMngInfListIpAddr_Object = MibTableColumn
rlMngInfListIpAddr = _RlMngInfListIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 4),
    _RlMngInfListIpAddr_Type()
)
rlMngInfListIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListIpAddr.setStatus("current")
_RlMngInfListIpNetMask_Type = IpAddress
_RlMngInfListIpNetMask_Object = MibTableColumn
rlMngInfListIpNetMask = _RlMngInfListIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 5),
    _RlMngInfListIpNetMask_Type()
)
rlMngInfListIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListIpNetMask.setStatus("current")
_RlMngInfListService_Type = RlMngInfServiceType
_RlMngInfListService_Object = MibTableColumn
rlMngInfListService = _RlMngInfListService_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 6),
    _RlMngInfListService_Type()
)
rlMngInfListService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListService.setStatus("current")
_RlMngInfListAction_Type = RlMngInfActionType
_RlMngInfListAction_Object = MibTableColumn
rlMngInfListAction = _RlMngInfListAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 7),
    _RlMngInfListAction_Type()
)
rlMngInfListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListAction.setStatus("current")
_RlMngInfListRowStatus_Type = RowStatus
_RlMngInfListRowStatus_Object = MibTableColumn
rlMngInfListRowStatus = _RlMngInfListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 4, 1, 8),
    _RlMngInfListRowStatus_Type()
)
rlMngInfListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListRowStatus.setStatus("current")


class _RlMngInfAuditingEnable_Type(TruthValue):
    """Custom type rlMngInfAuditingEnable based on TruthValue"""


_RlMngInfAuditingEnable_Object = MibScalar
rlMngInfAuditingEnable = _RlMngInfAuditingEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 5),
    _RlMngInfAuditingEnable_Type()
)
rlMngInfAuditingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfAuditingEnable.setStatus("current")
_RlMngInfListInetTable_Object = MibTable
rlMngInfListInetTable = _RlMngInfListInetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6)
)
if mibBuilder.loadTexts:
    rlMngInfListInetTable.setStatus("current")
_RlMngInfListInetEntry_Object = MibTableRow
rlMngInfListInetEntry = _RlMngInfListInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1)
)
rlMngInfListInetEntry.setIndexNames(
    (0, "DLINK-3100-MNGINF-MIB", "rlMngInfListInetName"),
    (0, "DLINK-3100-MNGINF-MIB", "rlMngInfListInetPriority"),
)
if mibBuilder.loadTexts:
    rlMngInfListInetEntry.setStatus("current")


class _RlMngInfListInetName_Type(DisplayString):
    """Custom type rlMngInfListInetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlMngInfListInetName_Type.__name__ = "DisplayString"
_RlMngInfListInetName_Object = MibTableColumn
rlMngInfListInetName = _RlMngInfListInetName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 1),
    _RlMngInfListInetName_Type()
)
rlMngInfListInetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMngInfListInetName.setStatus("current")


class _RlMngInfListInetPriority_Type(Unsigned32):
    """Custom type rlMngInfListInetPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlMngInfListInetPriority_Type.__name__ = "Unsigned32"
_RlMngInfListInetPriority_Object = MibTableColumn
rlMngInfListInetPriority = _RlMngInfListInetPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 2),
    _RlMngInfListInetPriority_Type()
)
rlMngInfListInetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMngInfListInetPriority.setStatus("current")
_RlMngInfListInetIfIndex_Type = Unsigned32
_RlMngInfListInetIfIndex_Object = MibTableColumn
rlMngInfListInetIfIndex = _RlMngInfListInetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 3),
    _RlMngInfListInetIfIndex_Type()
)
rlMngInfListInetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetIfIndex.setStatus("current")
_RlMngInfListInetIpAddrType_Type = InetAddressType
_RlMngInfListInetIpAddrType_Object = MibTableColumn
rlMngInfListInetIpAddrType = _RlMngInfListInetIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 4),
    _RlMngInfListInetIpAddrType_Type()
)
rlMngInfListInetIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetIpAddrType.setStatus("current")
_RlMngInfListInetIpAddr_Type = InetAddress
_RlMngInfListInetIpAddr_Object = MibTableColumn
rlMngInfListInetIpAddr = _RlMngInfListInetIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 5),
    _RlMngInfListInetIpAddr_Type()
)
rlMngInfListInetIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetIpAddr.setStatus("current")
_RlMngInfListInetIpNetMask_Type = IpAddress
_RlMngInfListInetIpNetMask_Object = MibTableColumn
rlMngInfListInetIpNetMask = _RlMngInfListInetIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 6),
    _RlMngInfListInetIpNetMask_Type()
)
rlMngInfListInetIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetIpNetMask.setStatus("current")
_RlMngInfListInetService_Type = RlMngInfServiceType
_RlMngInfListInetService_Object = MibTableColumn
rlMngInfListInetService = _RlMngInfListInetService_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 7),
    _RlMngInfListInetService_Type()
)
rlMngInfListInetService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetService.setStatus("current")
_RlMngInfListInetAction_Type = RlMngInfActionType
_RlMngInfListInetAction_Object = MibTableColumn
rlMngInfListInetAction = _RlMngInfListInetAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 8),
    _RlMngInfListInetAction_Type()
)
rlMngInfListInetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetAction.setStatus("current")
_RlMngInfListInetRowStatus_Type = RowStatus
_RlMngInfListInetRowStatus_Object = MibTableColumn
rlMngInfListInetRowStatus = _RlMngInfListInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 9),
    _RlMngInfListInetRowStatus_Type()
)
rlMngInfListInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetRowStatus.setStatus("current")


class _RlMngInfListInetIPv6PrefixLength_Type(Integer32):
    """Custom type rlMngInfListInetIPv6PrefixLength based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RlMngInfListInetIPv6PrefixLength_Type.__name__ = "Integer32"
_RlMngInfListInetIPv6PrefixLength_Object = MibTableColumn
rlMngInfListInetIPv6PrefixLength = _RlMngInfListInetIPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 89, 6, 1, 10),
    _RlMngInfListInetIPv6PrefixLength_Type()
)
rlMngInfListInetIPv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMngInfListInetIPv6PrefixLength.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-MNGINF-MIB",
    **{"RlMngInfServiceType": RlMngInfServiceType,
       "RlMngInfActionType": RlMngInfActionType,
       "rlMngInf": rlMngInf,
       "rlMngInfMibVersion": rlMngInfMibVersion,
       "rlMngInfEnable": rlMngInfEnable,
       "rlMngInfActiveListName": rlMngInfActiveListName,
       "rlMngInfListTable": rlMngInfListTable,
       "rlMngInfListEntry": rlMngInfListEntry,
       "rlMngInfListName": rlMngInfListName,
       "rlMngInfListPriority": rlMngInfListPriority,
       "rlMngInfListIfIndex": rlMngInfListIfIndex,
       "rlMngInfListIpAddr": rlMngInfListIpAddr,
       "rlMngInfListIpNetMask": rlMngInfListIpNetMask,
       "rlMngInfListService": rlMngInfListService,
       "rlMngInfListAction": rlMngInfListAction,
       "rlMngInfListRowStatus": rlMngInfListRowStatus,
       "rlMngInfAuditingEnable": rlMngInfAuditingEnable,
       "rlMngInfListInetTable": rlMngInfListInetTable,
       "rlMngInfListInetEntry": rlMngInfListInetEntry,
       "rlMngInfListInetName": rlMngInfListInetName,
       "rlMngInfListInetPriority": rlMngInfListInetPriority,
       "rlMngInfListInetIfIndex": rlMngInfListInetIfIndex,
       "rlMngInfListInetIpAddrType": rlMngInfListInetIpAddrType,
       "rlMngInfListInetIpAddr": rlMngInfListInetIpAddr,
       "rlMngInfListInetIpNetMask": rlMngInfListInetIpNetMask,
       "rlMngInfListInetService": rlMngInfListInetService,
       "rlMngInfListInetAction": rlMngInfListInetAction,
       "rlMngInfListInetRowStatus": rlMngInfListInetRowStatus,
       "rlMngInfListInetIPv6PrefixLength": rlMngInfListInetIPv6PrefixLength}
)
