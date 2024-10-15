# SNMP MIB module (TIMETRA-DA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-DA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:05 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxOperState")


# MODULE-IDENTITY

timetraDAMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 82)
)
timetraDAMIBModule.setRevisions(
        ("1911-05-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxDAConformance_ObjectIdentity = ObjectIdentity
tmnxDAConformance = _TmnxDAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 82)
)
_TmnxDACompliances_ObjectIdentity = ObjectIdentity
tmnxDACompliances = _TmnxDACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 82, 1)
)
_TmnxDAGroups_ObjectIdentity = ObjectIdentity
tmnxDAGroups = _TmnxDAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 82, 2)
)
_TmnxDA_ObjectIdentity = ObjectIdentity
tmnxDA = _TmnxDA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82)
)
_TmnxDAObjs_ObjectIdentity = ObjectIdentity
tmnxDAObjs = _TmnxDAObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1)
)
_TmnxDASvrGrpTableLastChanged_Type = TimeStamp
_TmnxDASvrGrpTableLastChanged_Object = MibScalar
tmnxDASvrGrpTableLastChanged = _TmnxDASvrGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 1),
    _TmnxDASvrGrpTableLastChanged_Type()
)
tmnxDASvrGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASvrGrpTableLastChanged.setStatus("current")
_TmnxDASvrGrpTable_Object = MibTable
tmnxDASvrGrpTable = _TmnxDASvrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxDASvrGrpTable.setStatus("current")
_TmnxDASvrGrpEntry_Object = MibTableRow
tmnxDASvrGrpEntry = _TmnxDASvrGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2, 1)
)
tmnxDASvrGrpEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDASvrGrpIndex"),
)
if mibBuilder.loadTexts:
    tmnxDASvrGrpEntry.setStatus("current")


class _TmnxDASvrGrpIndex_Type(Unsigned32):
    """Custom type tmnxDASvrGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4),
    )


_TmnxDASvrGrpIndex_Type.__name__ = "Unsigned32"
_TmnxDASvrGrpIndex_Object = MibTableColumn
tmnxDASvrGrpIndex = _TmnxDASvrGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2, 1, 1),
    _TmnxDASvrGrpIndex_Type()
)
tmnxDASvrGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDASvrGrpIndex.setStatus("current")
_TmnxDASvrGrpRowStatus_Type = RowStatus
_TmnxDASvrGrpRowStatus_Object = MibTableColumn
tmnxDASvrGrpRowStatus = _TmnxDASvrGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2, 1, 2),
    _TmnxDASvrGrpRowStatus_Type()
)
tmnxDASvrGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDASvrGrpRowStatus.setStatus("current")
_TmnxDASvrGrpLastChanged_Type = TimeStamp
_TmnxDASvrGrpLastChanged_Object = MibTableColumn
tmnxDASvrGrpLastChanged = _TmnxDASvrGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2, 1, 3),
    _TmnxDASvrGrpLastChanged_Type()
)
tmnxDASvrGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASvrGrpLastChanged.setStatus("current")


class _TmnxDASvrGrpCardSlotNumber_Type(Bits):
    """Custom type tmnxDASvrGrpCardSlotNumber based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("card1", 0),
          ("card10", 9),
          ("card2", 1),
          ("card3", 2),
          ("card4", 3),
          ("card5", 4),
          ("card6", 5),
          ("card7", 6),
          ("card8", 7),
          ("card9", 8))
    )

_TmnxDASvrGrpCardSlotNumber_Type.__name__ = "Bits"
_TmnxDASvrGrpCardSlotNumber_Object = MibTableColumn
tmnxDASvrGrpCardSlotNumber = _TmnxDASvrGrpCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2, 1, 4),
    _TmnxDASvrGrpCardSlotNumber_Type()
)
tmnxDASvrGrpCardSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDASvrGrpCardSlotNumber.setStatus("current")


class _TmnxDASvrGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxDASvrGrpAdminState based on TmnxAdminState"""


_TmnxDASvrGrpAdminState_Object = MibTableColumn
tmnxDASvrGrpAdminState = _TmnxDASvrGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2, 1, 5),
    _TmnxDASvrGrpAdminState_Type()
)
tmnxDASvrGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDASvrGrpAdminState.setStatus("current")
_TmnxDASvrGrpOperState_Type = TmnxOperState
_TmnxDASvrGrpOperState_Object = MibTableColumn
tmnxDASvrGrpOperState = _TmnxDASvrGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 2, 1, 6),
    _TmnxDASvrGrpOperState_Type()
)
tmnxDASvrGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASvrGrpOperState.setStatus("current")
_TmnxDAGrpTableLastChanged_Type = TimeStamp
_TmnxDAGrpTableLastChanged_Object = MibScalar
tmnxDAGrpTableLastChanged = _TmnxDAGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 3),
    _TmnxDAGrpTableLastChanged_Type()
)
tmnxDAGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpTableLastChanged.setStatus("current")
_TmnxDAGrpTable_Object = MibTable
tmnxDAGrpTable = _TmnxDAGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxDAGrpTable.setStatus("current")
_TmnxDAGrpEntry_Object = MibTableRow
tmnxDAGrpEntry = _TmnxDAGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1)
)
tmnxDAGrpEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
)
if mibBuilder.loadTexts:
    tmnxDAGrpEntry.setStatus("current")
_TmnxDAGrpName_Type = TNamedItem
_TmnxDAGrpName_Object = MibTableColumn
tmnxDAGrpName = _TmnxDAGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 1),
    _TmnxDAGrpName_Type()
)
tmnxDAGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAGrpName.setStatus("current")
_TmnxDAGrpRowStatus_Type = RowStatus
_TmnxDAGrpRowStatus_Object = MibTableColumn
tmnxDAGrpRowStatus = _TmnxDAGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 2),
    _TmnxDAGrpRowStatus_Type()
)
tmnxDAGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpRowStatus.setStatus("current")
_TmnxDAGrpLastChanged_Type = TimeStamp
_TmnxDAGrpLastChanged_Object = MibTableColumn
tmnxDAGrpLastChanged = _TmnxDAGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 3),
    _TmnxDAGrpLastChanged_Type()
)
tmnxDAGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpLastChanged.setStatus("current")


class _TmnxDAGrpServerGroupIndex_Type(Unsigned32):
    """Custom type tmnxDAGrpServerGroupIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4),
    )


_TmnxDAGrpServerGroupIndex_Type.__name__ = "Unsigned32"
_TmnxDAGrpServerGroupIndex_Object = MibTableColumn
tmnxDAGrpServerGroupIndex = _TmnxDAGrpServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 4),
    _TmnxDAGrpServerGroupIndex_Type()
)
tmnxDAGrpServerGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpServerGroupIndex.setStatus("current")


class _TmnxDAGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxDAGrpAdminState based on TmnxAdminState"""


_TmnxDAGrpAdminState_Object = MibTableColumn
tmnxDAGrpAdminState = _TmnxDAGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 5),
    _TmnxDAGrpAdminState_Type()
)
tmnxDAGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpAdminState.setStatus("current")


class _TmnxDAGrpDescription_Type(TItemDescription):
    """Custom type tmnxDAGrpDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxDAGrpDescription_Object = MibTableColumn
tmnxDAGrpDescription = _TmnxDAGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 6),
    _TmnxDAGrpDescription_Type()
)
tmnxDAGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDescription.setStatus("current")


class _TmnxDAGrpDnsClientIsmLinkName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDAGrpDnsClientIsmLinkName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxDAGrpDnsClientIsmLinkName_Object = MibTableColumn
tmnxDAGrpDnsClientIsmLinkName = _TmnxDAGrpDnsClientIsmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 7),
    _TmnxDAGrpDnsClientIsmLinkName_Type()
)
tmnxDAGrpDnsClientIsmLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDnsClientIsmLinkName.setStatus("current")


class _TmnxDAGrpDCAuthCache_Type(Integer32):
    """Custom type tmnxDAGrpDCAuthCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("useCache", 2))
    )


_TmnxDAGrpDCAuthCache_Type.__name__ = "Integer32"
_TmnxDAGrpDCAuthCache_Object = MibTableColumn
tmnxDAGrpDCAuthCache = _TmnxDAGrpDCAuthCache_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 8),
    _TmnxDAGrpDCAuthCache_Type()
)
tmnxDAGrpDCAuthCache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAuthCache.setStatus("current")


class _TmnxDAGrpDCAdminState_Type(TmnxAdminState):
    """Custom type tmnxDAGrpDCAdminState based on TmnxAdminState"""


_TmnxDAGrpDCAdminState_Object = MibTableColumn
tmnxDAGrpDCAdminState = _TmnxDAGrpDCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 9),
    _TmnxDAGrpDCAdminState_Type()
)
tmnxDAGrpDCAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAdminState.setStatus("current")


class _TmnxDAGrpDCIsmLinkName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDAGrpDCIsmLinkName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxDAGrpDCIsmLinkName_Object = MibTableColumn
tmnxDAGrpDCIsmLinkName = _TmnxDAGrpDCIsmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 10),
    _TmnxDAGrpDCIsmLinkName_Type()
)
tmnxDAGrpDCIsmLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDCIsmLinkName.setStatus("current")


class _TmnxDAGrpDCBootStrapPort_Type(InetPortNumber):
    """Custom type tmnxDAGrpDCBootStrapPort based on InetPortNumber"""
    defaultValue = 22345


_TmnxDAGrpDCBootStrapPort_Object = MibTableColumn
tmnxDAGrpDCBootStrapPort = _TmnxDAGrpDCBootStrapPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 11),
    _TmnxDAGrpDCBootStrapPort_Type()
)
tmnxDAGrpDCBootStrapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDCBootStrapPort.setStatus("current")


class _TmnxDAGrpDCConnRetryTimer_Type(Unsigned32):
    """Custom type tmnxDAGrpDCConnRetryTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300000),
    )


_TmnxDAGrpDCConnRetryTimer_Type.__name__ = "Unsigned32"
_TmnxDAGrpDCConnRetryTimer_Object = MibTableColumn
tmnxDAGrpDCConnRetryTimer = _TmnxDAGrpDCConnRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 12),
    _TmnxDAGrpDCConnRetryTimer_Type()
)
tmnxDAGrpDCConnRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDCConnRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAGrpDCConnRetryTimer.setUnits("milliseconds")


class _TmnxDAGrpDCIdleTimeout_Type(Unsigned32):
    """Custom type tmnxDAGrpDCIdleTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TmnxDAGrpDCIdleTimeout_Type.__name__ = "Unsigned32"
_TmnxDAGrpDCIdleTimeout_Object = MibTableColumn
tmnxDAGrpDCIdleTimeout = _TmnxDAGrpDCIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 13),
    _TmnxDAGrpDCIdleTimeout_Type()
)
tmnxDAGrpDCIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDCIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAGrpDCIdleTimeout.setUnits("seconds")
_TmnxDAGrpBytesFromCache_Type = Counter64
_TmnxDAGrpBytesFromCache_Object = MibTableColumn
tmnxDAGrpBytesFromCache = _TmnxDAGrpBytesFromCache_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 14),
    _TmnxDAGrpBytesFromCache_Type()
)
tmnxDAGrpBytesFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpBytesFromCache.setStatus("current")
_TmnxDAGrpBytesFromCacheL32_Type = Counter32
_TmnxDAGrpBytesFromCacheL32_Object = MibTableColumn
tmnxDAGrpBytesFromCacheL32 = _TmnxDAGrpBytesFromCacheL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 15),
    _TmnxDAGrpBytesFromCacheL32_Type()
)
tmnxDAGrpBytesFromCacheL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpBytesFromCacheL32.setStatus("current")
_TmnxDAGrpBytesFromCacheH32_Type = Counter32
_TmnxDAGrpBytesFromCacheH32_Object = MibTableColumn
tmnxDAGrpBytesFromCacheH32 = _TmnxDAGrpBytesFromCacheH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 16),
    _TmnxDAGrpBytesFromCacheH32_Type()
)
tmnxDAGrpBytesFromCacheH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpBytesFromCacheH32.setStatus("current")
_TmnxDAGrpBytesNotFromCache_Type = Counter64
_TmnxDAGrpBytesNotFromCache_Object = MibTableColumn
tmnxDAGrpBytesNotFromCache = _TmnxDAGrpBytesNotFromCache_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 17),
    _TmnxDAGrpBytesNotFromCache_Type()
)
tmnxDAGrpBytesNotFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpBytesNotFromCache.setStatus("current")
_TmnxDAGrpBytesNotFromCacheL32_Type = Counter32
_TmnxDAGrpBytesNotFromCacheL32_Object = MibTableColumn
tmnxDAGrpBytesNotFromCacheL32 = _TmnxDAGrpBytesNotFromCacheL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 18),
    _TmnxDAGrpBytesNotFromCacheL32_Type()
)
tmnxDAGrpBytesNotFromCacheL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpBytesNotFromCacheL32.setStatus("current")
_TmnxDAGrpBytesNotFromCacheH32_Type = Counter32
_TmnxDAGrpBytesNotFromCacheH32_Object = MibTableColumn
tmnxDAGrpBytesNotFromCacheH32 = _TmnxDAGrpBytesNotFromCacheH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 19),
    _TmnxDAGrpBytesNotFromCacheH32_Type()
)
tmnxDAGrpBytesNotFromCacheH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpBytesNotFromCacheH32.setStatus("current")
_TmnxDAGrpObjectsFromCache_Type = Counter64
_TmnxDAGrpObjectsFromCache_Object = MibTableColumn
tmnxDAGrpObjectsFromCache = _TmnxDAGrpObjectsFromCache_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 20),
    _TmnxDAGrpObjectsFromCache_Type()
)
tmnxDAGrpObjectsFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectsFromCache.setStatus("current")
_TmnxDAGrpObjectsFromCacheL32_Type = Counter32
_TmnxDAGrpObjectsFromCacheL32_Object = MibTableColumn
tmnxDAGrpObjectsFromCacheL32 = _TmnxDAGrpObjectsFromCacheL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 21),
    _TmnxDAGrpObjectsFromCacheL32_Type()
)
tmnxDAGrpObjectsFromCacheL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectsFromCacheL32.setStatus("current")
_TmnxDAGrpObjectsFromCacheH32_Type = Counter32
_TmnxDAGrpObjectsFromCacheH32_Object = MibTableColumn
tmnxDAGrpObjectsFromCacheH32 = _TmnxDAGrpObjectsFromCacheH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 22),
    _TmnxDAGrpObjectsFromCacheH32_Type()
)
tmnxDAGrpObjectsFromCacheH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectsFromCacheH32.setStatus("current")
_TmnxDAGrpObjectsNotFromCache_Type = Counter64
_TmnxDAGrpObjectsNotFromCache_Object = MibTableColumn
tmnxDAGrpObjectsNotFromCache = _TmnxDAGrpObjectsNotFromCache_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 23),
    _TmnxDAGrpObjectsNotFromCache_Type()
)
tmnxDAGrpObjectsNotFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectsNotFromCache.setStatus("current")
_TmnxDAGrpObjectsNotFromCacheL32_Type = Counter32
_TmnxDAGrpObjectsNotFromCacheL32_Object = MibTableColumn
tmnxDAGrpObjectsNotFromCacheL32 = _TmnxDAGrpObjectsNotFromCacheL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 24),
    _TmnxDAGrpObjectsNotFromCacheL32_Type()
)
tmnxDAGrpObjectsNotFromCacheL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectsNotFromCacheL32.setStatus("current")
_TmnxDAGrpObjectsNotFromCacheH32_Type = Counter32
_TmnxDAGrpObjectsNotFromCacheH32_Object = MibTableColumn
tmnxDAGrpObjectsNotFromCacheH32 = _TmnxDAGrpObjectsNotFromCacheH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 25),
    _TmnxDAGrpObjectsNotFromCacheH32_Type()
)
tmnxDAGrpObjectsNotFromCacheH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectsNotFromCacheH32.setStatus("current")
_TmnxDAGrpObjectByteCount_Type = Counter64
_TmnxDAGrpObjectByteCount_Object = MibTableColumn
tmnxDAGrpObjectByteCount = _TmnxDAGrpObjectByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 26),
    _TmnxDAGrpObjectByteCount_Type()
)
tmnxDAGrpObjectByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectByteCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectByteCount.setUnits("megabytes")
_TmnxDAGrpObjectByteCountL32_Type = Counter32
_TmnxDAGrpObjectByteCountL32_Object = MibTableColumn
tmnxDAGrpObjectByteCountL32 = _TmnxDAGrpObjectByteCountL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 27),
    _TmnxDAGrpObjectByteCountL32_Type()
)
tmnxDAGrpObjectByteCountL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectByteCountL32.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectByteCountL32.setUnits("megabytes")
_TmnxDAGrpObjectByteCountH32_Type = Counter32
_TmnxDAGrpObjectByteCountH32_Object = MibTableColumn
tmnxDAGrpObjectByteCountH32 = _TmnxDAGrpObjectByteCountH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 28),
    _TmnxDAGrpObjectByteCountH32_Type()
)
tmnxDAGrpObjectByteCountH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectByteCountH32.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAGrpObjectByteCountH32.setUnits("megabytes")
_TmnxDAGrpNumberOfOrigins_Type = Counter64
_TmnxDAGrpNumberOfOrigins_Object = MibTableColumn
tmnxDAGrpNumberOfOrigins = _TmnxDAGrpNumberOfOrigins_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 29),
    _TmnxDAGrpNumberOfOrigins_Type()
)
tmnxDAGrpNumberOfOrigins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpNumberOfOrigins.setStatus("current")
_TmnxDAGrpNumberOfOriginsL32_Type = Counter32
_TmnxDAGrpNumberOfOriginsL32_Object = MibTableColumn
tmnxDAGrpNumberOfOriginsL32 = _TmnxDAGrpNumberOfOriginsL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 30),
    _TmnxDAGrpNumberOfOriginsL32_Type()
)
tmnxDAGrpNumberOfOriginsL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpNumberOfOriginsL32.setStatus("current")
_TmnxDAGrpNumberOfOriginsH32_Type = Counter32
_TmnxDAGrpNumberOfOriginsH32_Object = MibTableColumn
tmnxDAGrpNumberOfOriginsH32 = _TmnxDAGrpNumberOfOriginsH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 31),
    _TmnxDAGrpNumberOfOriginsH32_Type()
)
tmnxDAGrpNumberOfOriginsH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpNumberOfOriginsH32.setStatus("current")
_TmnxDAGrpDCAuthCacheHit_Type = Counter64
_TmnxDAGrpDCAuthCacheHit_Object = MibTableColumn
tmnxDAGrpDCAuthCacheHit = _TmnxDAGrpDCAuthCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 32),
    _TmnxDAGrpDCAuthCacheHit_Type()
)
tmnxDAGrpDCAuthCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAuthCacheHit.setStatus("current")
_TmnxDAGrpDCAuthCacheHitL32_Type = Counter32
_TmnxDAGrpDCAuthCacheHitL32_Object = MibTableColumn
tmnxDAGrpDCAuthCacheHitL32 = _TmnxDAGrpDCAuthCacheHitL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 33),
    _TmnxDAGrpDCAuthCacheHitL32_Type()
)
tmnxDAGrpDCAuthCacheHitL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAuthCacheHitL32.setStatus("current")
_TmnxDAGrpDCAuthCacheHitH32_Type = Counter32
_TmnxDAGrpDCAuthCacheHitH32_Object = MibTableColumn
tmnxDAGrpDCAuthCacheHitH32 = _TmnxDAGrpDCAuthCacheHitH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 34),
    _TmnxDAGrpDCAuthCacheHitH32_Type()
)
tmnxDAGrpDCAuthCacheHitH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAuthCacheHitH32.setStatus("current")
_TmnxDAGrpDCAuthCacheMiss_Type = Counter64
_TmnxDAGrpDCAuthCacheMiss_Object = MibTableColumn
tmnxDAGrpDCAuthCacheMiss = _TmnxDAGrpDCAuthCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 35),
    _TmnxDAGrpDCAuthCacheMiss_Type()
)
tmnxDAGrpDCAuthCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAuthCacheMiss.setStatus("current")
_TmnxDAGrpDCAuthCacheMissL32_Type = Counter32
_TmnxDAGrpDCAuthCacheMissL32_Object = MibTableColumn
tmnxDAGrpDCAuthCacheMissL32 = _TmnxDAGrpDCAuthCacheMissL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 36),
    _TmnxDAGrpDCAuthCacheMissL32_Type()
)
tmnxDAGrpDCAuthCacheMissL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAuthCacheMissL32.setStatus("current")
_TmnxDAGrpDCAuthCacheMissH32_Type = Counter32
_TmnxDAGrpDCAuthCacheMissH32_Object = MibTableColumn
tmnxDAGrpDCAuthCacheMissH32 = _TmnxDAGrpDCAuthCacheMissH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 37),
    _TmnxDAGrpDCAuthCacheMissH32_Type()
)
tmnxDAGrpDCAuthCacheMissH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAuthCacheMissH32.setStatus("current")
_TmnxDAGrpDCDeniedAuth_Type = Counter64
_TmnxDAGrpDCDeniedAuth_Object = MibTableColumn
tmnxDAGrpDCDeniedAuth = _TmnxDAGrpDCDeniedAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 38),
    _TmnxDAGrpDCDeniedAuth_Type()
)
tmnxDAGrpDCDeniedAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCDeniedAuth.setStatus("current")
_TmnxDAGrpDCDeniedAuthL32_Type = Counter32
_TmnxDAGrpDCDeniedAuthL32_Object = MibTableColumn
tmnxDAGrpDCDeniedAuthL32 = _TmnxDAGrpDCDeniedAuthL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 39),
    _TmnxDAGrpDCDeniedAuthL32_Type()
)
tmnxDAGrpDCDeniedAuthL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCDeniedAuthL32.setStatus("current")
_TmnxDAGrpDCDeniedAuthH32_Type = Counter32
_TmnxDAGrpDCDeniedAuthH32_Object = MibTableColumn
tmnxDAGrpDCDeniedAuthH32 = _TmnxDAGrpDCDeniedAuthH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 40),
    _TmnxDAGrpDCDeniedAuthH32_Type()
)
tmnxDAGrpDCDeniedAuthH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCDeniedAuthH32.setStatus("current")
_TmnxDAGrpDCMinRTTPerPeer_Type = Counter32
_TmnxDAGrpDCMinRTTPerPeer_Object = MibTableColumn
tmnxDAGrpDCMinRTTPerPeer = _TmnxDAGrpDCMinRTTPerPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 41),
    _TmnxDAGrpDCMinRTTPerPeer_Type()
)
tmnxDAGrpDCMinRTTPerPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCMinRTTPerPeer.setStatus("current")
_TmnxDAGrpDCAvgRTTPerPeer_Type = Counter32
_TmnxDAGrpDCAvgRTTPerPeer_Object = MibTableColumn
tmnxDAGrpDCAvgRTTPerPeer = _TmnxDAGrpDCAvgRTTPerPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 42),
    _TmnxDAGrpDCAvgRTTPerPeer_Type()
)
tmnxDAGrpDCAvgRTTPerPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCAvgRTTPerPeer.setStatus("current")
_TmnxDAGrpDCMaxRTTPerPeer_Type = Counter32
_TmnxDAGrpDCMaxRTTPerPeer_Object = MibTableColumn
tmnxDAGrpDCMaxRTTPerPeer = _TmnxDAGrpDCMaxRTTPerPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 4, 1, 43),
    _TmnxDAGrpDCMaxRTTPerPeer_Type()
)
tmnxDAGrpDCMaxRTTPerPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDCMaxRTTPerPeer.setStatus("current")
_TmnxDAGrpDnsSvrTableLastChanged_Type = TimeStamp
_TmnxDAGrpDnsSvrTableLastChanged_Object = MibScalar
tmnxDAGrpDnsSvrTableLastChanged = _TmnxDAGrpDnsSvrTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 5),
    _TmnxDAGrpDnsSvrTableLastChanged_Type()
)
tmnxDAGrpDnsSvrTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDnsSvrTableLastChanged.setStatus("current")
_TmnxDAGrpDnsSvrTable_Object = MibTable
tmnxDAGrpDnsSvrTable = _TmnxDAGrpDnsSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxDAGrpDnsSvrTable.setStatus("current")
_TmnxDAGrpDnsSvrEntry_Object = MibTableRow
tmnxDAGrpDnsSvrEntry = _TmnxDAGrpDnsSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 6, 1)
)
tmnxDAGrpDnsSvrEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpDnsSvrAddrTyp"),
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpDnsSvrAddress"),
)
if mibBuilder.loadTexts:
    tmnxDAGrpDnsSvrEntry.setStatus("current")
_TmnxDAGrpDnsSvrAddrTyp_Type = InetAddressType
_TmnxDAGrpDnsSvrAddrTyp_Object = MibTableColumn
tmnxDAGrpDnsSvrAddrTyp = _TmnxDAGrpDnsSvrAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 6, 1, 1),
    _TmnxDAGrpDnsSvrAddrTyp_Type()
)
tmnxDAGrpDnsSvrAddrTyp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAGrpDnsSvrAddrTyp.setStatus("current")


class _TmnxDAGrpDnsSvrAddress_Type(InetAddress):
    """Custom type tmnxDAGrpDnsSvrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDAGrpDnsSvrAddress_Type.__name__ = "InetAddress"
_TmnxDAGrpDnsSvrAddress_Object = MibTableColumn
tmnxDAGrpDnsSvrAddress = _TmnxDAGrpDnsSvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 6, 1, 2),
    _TmnxDAGrpDnsSvrAddress_Type()
)
tmnxDAGrpDnsSvrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAGrpDnsSvrAddress.setStatus("current")
_TmnxDAGrpDnsSvrRowStatus_Type = RowStatus
_TmnxDAGrpDnsSvrRowStatus_Object = MibTableColumn
tmnxDAGrpDnsSvrRowStatus = _TmnxDAGrpDnsSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 6, 1, 3),
    _TmnxDAGrpDnsSvrRowStatus_Type()
)
tmnxDAGrpDnsSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAGrpDnsSvrRowStatus.setStatus("current")
_TmnxDAGrpDnsSvrLastChanged_Type = TimeStamp
_TmnxDAGrpDnsSvrLastChanged_Object = MibTableColumn
tmnxDAGrpDnsSvrLastChanged = _TmnxDAGrpDnsSvrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 6, 1, 4),
    _TmnxDAGrpDnsSvrLastChanged_Type()
)
tmnxDAGrpDnsSvrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpDnsSvrLastChanged.setStatus("current")
_TmnxDADCBtStSvrTableLastChanged_Type = TimeStamp
_TmnxDADCBtStSvrTableLastChanged_Object = MibScalar
tmnxDADCBtStSvrTableLastChanged = _TmnxDADCBtStSvrTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 7),
    _TmnxDADCBtStSvrTableLastChanged_Type()
)
tmnxDADCBtStSvrTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrTableLastChanged.setStatus("current")
_TmnxDADCBtStSvrTable_Object = MibTable
tmnxDADCBtStSvrTable = _TmnxDADCBtStSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrTable.setStatus("current")
_TmnxDADCBtStSvrEntry_Object = MibTableRow
tmnxDADCBtStSvrEntry = _TmnxDADCBtStSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 8, 1)
)
tmnxDADCBtStSvrEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
    (0, "TIMETRA-DA-MIB", "tmnxDADCBtStSvrIndex"),
)
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrEntry.setStatus("current")


class _TmnxDADCBtStSvrIndex_Type(Unsigned32):
    """Custom type tmnxDADCBtStSvrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4),
    )


_TmnxDADCBtStSvrIndex_Type.__name__ = "Unsigned32"
_TmnxDADCBtStSvrIndex_Object = MibTableColumn
tmnxDADCBtStSvrIndex = _TmnxDADCBtStSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 8, 1, 1),
    _TmnxDADCBtStSvrIndex_Type()
)
tmnxDADCBtStSvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrIndex.setStatus("current")
_TmnxDADCBtStSvrRowStatus_Type = RowStatus
_TmnxDADCBtStSvrRowStatus_Object = MibTableColumn
tmnxDADCBtStSvrRowStatus = _TmnxDADCBtStSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 8, 1, 2),
    _TmnxDADCBtStSvrRowStatus_Type()
)
tmnxDADCBtStSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrRowStatus.setStatus("current")
_TmnxDADCBtStSvrLastChanged_Type = TimeStamp
_TmnxDADCBtStSvrLastChanged_Object = MibTableColumn
tmnxDADCBtStSvrLastChanged = _TmnxDADCBtStSvrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 8, 1, 3),
    _TmnxDADCBtStSvrLastChanged_Type()
)
tmnxDADCBtStSvrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrLastChanged.setStatus("current")


class _TmnxDADCBtStSvrAddrType_Type(InetAddressType):
    """Custom type tmnxDADCBtStSvrAddrType based on InetAddressType"""


_TmnxDADCBtStSvrAddrType_Object = MibTableColumn
tmnxDADCBtStSvrAddrType = _TmnxDADCBtStSvrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 8, 1, 4),
    _TmnxDADCBtStSvrAddrType_Type()
)
tmnxDADCBtStSvrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrAddrType.setStatus("current")


class _TmnxDADCBtStSvrAddress_Type(InetAddress):
    """Custom type tmnxDADCBtStSvrAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxDADCBtStSvrAddress_Type.__name__ = "InetAddress"
_TmnxDADCBtStSvrAddress_Object = MibTableColumn
tmnxDADCBtStSvrAddress = _TmnxDADCBtStSvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 8, 1, 5),
    _TmnxDADCBtStSvrAddress_Type()
)
tmnxDADCBtStSvrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDADCBtStSvrAddress.setStatus("current")
_TmnxDAHttpTableLastChanged_Type = TimeStamp
_TmnxDAHttpTableLastChanged_Object = MibScalar
tmnxDAHttpTableLastChanged = _TmnxDAHttpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 9),
    _TmnxDAHttpTableLastChanged_Type()
)
tmnxDAHttpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpTableLastChanged.setStatus("current")
_TmnxDAHttpTable_Object = MibTable
tmnxDAHttpTable = _TmnxDAHttpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxDAHttpTable.setStatus("current")
_TmnxDAHttpEntry_Object = MibTableRow
tmnxDAHttpEntry = _TmnxDAHttpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxDAHttpEntry.setStatus("current")
_TmnxDAHttpLastChanged_Type = TimeStamp
_TmnxDAHttpLastChanged_Object = MibTableColumn
tmnxDAHttpLastChanged = _TmnxDAHttpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 1),
    _TmnxDAHttpLastChanged_Type()
)
tmnxDAHttpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpLastChanged.setStatus("current")


class _TmnxDAHttpServerAdminState_Type(TmnxAdminState):
    """Custom type tmnxDAHttpServerAdminState based on TmnxAdminState"""


_TmnxDAHttpServerAdminState_Object = MibTableColumn
tmnxDAHttpServerAdminState = _TmnxDAHttpServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 2),
    _TmnxDAHttpServerAdminState_Type()
)
tmnxDAHttpServerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAHttpServerAdminState.setStatus("current")
_TmnxDAHttpServerOperState_Type = TmnxOperState
_TmnxDAHttpServerOperState_Object = MibTableColumn
tmnxDAHttpServerOperState = _TmnxDAHttpServerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 3),
    _TmnxDAHttpServerOperState_Type()
)
tmnxDAHttpServerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerOperState.setStatus("current")


class _TmnxDAHttpServerIdleTimeout_Type(Unsigned32):
    """Custom type tmnxDAHttpServerIdleTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_TmnxDAHttpServerIdleTimeout_Type.__name__ = "Unsigned32"
_TmnxDAHttpServerIdleTimeout_Object = MibTableColumn
tmnxDAHttpServerIdleTimeout = _TmnxDAHttpServerIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 4),
    _TmnxDAHttpServerIdleTimeout_Type()
)
tmnxDAHttpServerIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAHttpServerIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAHttpServerIdleTimeout.setUnits("seconds")


class _TmnxDAHttpServerViaString_Type(DisplayString):
    """Custom type tmnxDAHttpServerViaString based on DisplayString"""
    defaultHexValue = ""


_TmnxDAHttpServerViaString_Object = MibTableColumn
tmnxDAHttpServerViaString = _TmnxDAHttpServerViaString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 5),
    _TmnxDAHttpServerViaString_Type()
)
tmnxDAHttpServerViaString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAHttpServerViaString.setStatus("current")
_TmnxDAHttpServerStrBWInUse_Type = Counter64
_TmnxDAHttpServerStrBWInUse_Object = MibTableColumn
tmnxDAHttpServerStrBWInUse = _TmnxDAHttpServerStrBWInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 6),
    _TmnxDAHttpServerStrBWInUse_Type()
)
tmnxDAHttpServerStrBWInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerStrBWInUse.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAHttpServerStrBWInUse.setUnits("kbps")
_TmnxDAHttpServerStrBWInUseL32_Type = Counter32
_TmnxDAHttpServerStrBWInUseL32_Object = MibTableColumn
tmnxDAHttpServerStrBWInUseL32 = _TmnxDAHttpServerStrBWInUseL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 7),
    _TmnxDAHttpServerStrBWInUseL32_Type()
)
tmnxDAHttpServerStrBWInUseL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerStrBWInUseL32.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAHttpServerStrBWInUseL32.setUnits("kbps")
_TmnxDAHttpServerStrBWInUseH32_Type = Counter32
_TmnxDAHttpServerStrBWInUseH32_Object = MibTableColumn
tmnxDAHttpServerStrBWInUseH32 = _TmnxDAHttpServerStrBWInUseH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 8),
    _TmnxDAHttpServerStrBWInUseH32_Type()
)
tmnxDAHttpServerStrBWInUseH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerStrBWInUseH32.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAHttpServerStrBWInUseH32.setUnits("kbps")
_TmnxDAHttpServerXferInProg_Type = Gauge32
_TmnxDAHttpServerXferInProg_Object = MibTableColumn
tmnxDAHttpServerXferInProg = _TmnxDAHttpServerXferInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 9),
    _TmnxDAHttpServerXferInProg_Type()
)
tmnxDAHttpServerXferInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerXferInProg.setStatus("current")
_TmnxDAHttpServerXferCompleted_Type = Counter64
_TmnxDAHttpServerXferCompleted_Object = MibTableColumn
tmnxDAHttpServerXferCompleted = _TmnxDAHttpServerXferCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 10),
    _TmnxDAHttpServerXferCompleted_Type()
)
tmnxDAHttpServerXferCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerXferCompleted.setStatus("current")
_TmnxDAHttpServerXferCompletedL32_Type = Counter32
_TmnxDAHttpServerXferCompletedL32_Object = MibTableColumn
tmnxDAHttpServerXferCompletedL32 = _TmnxDAHttpServerXferCompletedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 11),
    _TmnxDAHttpServerXferCompletedL32_Type()
)
tmnxDAHttpServerXferCompletedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerXferCompletedL32.setStatus("current")
_TmnxDAHttpServerXferCompletedH32_Type = Counter32
_TmnxDAHttpServerXferCompletedH32_Object = MibTableColumn
tmnxDAHttpServerXferCompletedH32 = _TmnxDAHttpServerXferCompletedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 12),
    _TmnxDAHttpServerXferCompletedH32_Type()
)
tmnxDAHttpServerXferCompletedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerXferCompletedH32.setStatus("current")
_TmnxDAHttpServerXferTimeouts_Type = Gauge32
_TmnxDAHttpServerXferTimeouts_Object = MibTableColumn
tmnxDAHttpServerXferTimeouts = _TmnxDAHttpServerXferTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 13),
    _TmnxDAHttpServerXferTimeouts_Type()
)
tmnxDAHttpServerXferTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerXferTimeouts.setStatus("current")
_TmnxDAHttpServerXferFailed_Type = Gauge32
_TmnxDAHttpServerXferFailed_Object = MibTableColumn
tmnxDAHttpServerXferFailed = _TmnxDAHttpServerXferFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 14),
    _TmnxDAHttpServerXferFailed_Type()
)
tmnxDAHttpServerXferFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerXferFailed.setStatus("current")
_TmnxDAHttpServerValidRequests_Type = Counter64
_TmnxDAHttpServerValidRequests_Object = MibTableColumn
tmnxDAHttpServerValidRequests = _TmnxDAHttpServerValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 15),
    _TmnxDAHttpServerValidRequests_Type()
)
tmnxDAHttpServerValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerValidRequests.setStatus("current")
_TmnxDAHttpServerValidRequestsL32_Type = Counter32
_TmnxDAHttpServerValidRequestsL32_Object = MibTableColumn
tmnxDAHttpServerValidRequestsL32 = _TmnxDAHttpServerValidRequestsL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 16),
    _TmnxDAHttpServerValidRequestsL32_Type()
)
tmnxDAHttpServerValidRequestsL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerValidRequestsL32.setStatus("current")
_TmnxDAHttpServerValidRequestsH32_Type = Counter32
_TmnxDAHttpServerValidRequestsH32_Object = MibTableColumn
tmnxDAHttpServerValidRequestsH32 = _TmnxDAHttpServerValidRequestsH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 17),
    _TmnxDAHttpServerValidRequestsH32_Type()
)
tmnxDAHttpServerValidRequestsH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerValidRequestsH32.setStatus("current")
_TmnxDAHttpServerInvalidRequests_Type = Gauge32
_TmnxDAHttpServerInvalidRequests_Object = MibTableColumn
tmnxDAHttpServerInvalidRequests = _TmnxDAHttpServerInvalidRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 18),
    _TmnxDAHttpServerInvalidRequests_Type()
)
tmnxDAHttpServerInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerInvalidRequests.setStatus("current")
_TmnxDAHttpServerMethodNotSuppted_Type = Gauge32
_TmnxDAHttpServerMethodNotSuppted_Object = MibTableColumn
tmnxDAHttpServerMethodNotSuppted = _TmnxDAHttpServerMethodNotSuppted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 19),
    _TmnxDAHttpServerMethodNotSuppted_Type()
)
tmnxDAHttpServerMethodNotSuppted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerMethodNotSuppted.setStatus("current")
_TmnxDAHttpServerHostNotSuppted_Type = Gauge32
_TmnxDAHttpServerHostNotSuppted_Object = MibTableColumn
tmnxDAHttpServerHostNotSuppted = _TmnxDAHttpServerHostNotSuppted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 20),
    _TmnxDAHttpServerHostNotSuppted_Type()
)
tmnxDAHttpServerHostNotSuppted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServerHostNotSuppted.setStatus("current")
_TmnxDAHttpServer1XXCountSent_Type = Counter64
_TmnxDAHttpServer1XXCountSent_Object = MibTableColumn
tmnxDAHttpServer1XXCountSent = _TmnxDAHttpServer1XXCountSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 21),
    _TmnxDAHttpServer1XXCountSent_Type()
)
tmnxDAHttpServer1XXCountSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer1XXCountSent.setStatus("current")
_TmnxDAHttpServer1XXCountSentL32_Type = Counter32
_TmnxDAHttpServer1XXCountSentL32_Object = MibTableColumn
tmnxDAHttpServer1XXCountSentL32 = _TmnxDAHttpServer1XXCountSentL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 22),
    _TmnxDAHttpServer1XXCountSentL32_Type()
)
tmnxDAHttpServer1XXCountSentL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer1XXCountSentL32.setStatus("current")
_TmnxDAHttpServer1XXCountSentH32_Type = Counter32
_TmnxDAHttpServer1XXCountSentH32_Object = MibTableColumn
tmnxDAHttpServer1XXCountSentH32 = _TmnxDAHttpServer1XXCountSentH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 23),
    _TmnxDAHttpServer1XXCountSentH32_Type()
)
tmnxDAHttpServer1XXCountSentH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer1XXCountSentH32.setStatus("current")
_TmnxDAHttpServer2XXCountSent_Type = Counter64
_TmnxDAHttpServer2XXCountSent_Object = MibTableColumn
tmnxDAHttpServer2XXCountSent = _TmnxDAHttpServer2XXCountSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 24),
    _TmnxDAHttpServer2XXCountSent_Type()
)
tmnxDAHttpServer2XXCountSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer2XXCountSent.setStatus("current")
_TmnxDAHttpServer2XXCountSentL32_Type = Counter32
_TmnxDAHttpServer2XXCountSentL32_Object = MibTableColumn
tmnxDAHttpServer2XXCountSentL32 = _TmnxDAHttpServer2XXCountSentL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 25),
    _TmnxDAHttpServer2XXCountSentL32_Type()
)
tmnxDAHttpServer2XXCountSentL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer2XXCountSentL32.setStatus("current")
_TmnxDAHttpServer2XXCountSentH32_Type = Counter32
_TmnxDAHttpServer2XXCountSentH32_Object = MibTableColumn
tmnxDAHttpServer2XXCountSentH32 = _TmnxDAHttpServer2XXCountSentH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 26),
    _TmnxDAHttpServer2XXCountSentH32_Type()
)
tmnxDAHttpServer2XXCountSentH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer2XXCountSentH32.setStatus("current")
_TmnxDAHttpServer3XXCountSent_Type = Counter64
_TmnxDAHttpServer3XXCountSent_Object = MibTableColumn
tmnxDAHttpServer3XXCountSent = _TmnxDAHttpServer3XXCountSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 27),
    _TmnxDAHttpServer3XXCountSent_Type()
)
tmnxDAHttpServer3XXCountSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer3XXCountSent.setStatus("current")
_TmnxDAHttpServer3XXCountSentL32_Type = Counter32
_TmnxDAHttpServer3XXCountSentL32_Object = MibTableColumn
tmnxDAHttpServer3XXCountSentL32 = _TmnxDAHttpServer3XXCountSentL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 28),
    _TmnxDAHttpServer3XXCountSentL32_Type()
)
tmnxDAHttpServer3XXCountSentL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer3XXCountSentL32.setStatus("current")
_TmnxDAHttpServer3XXCountSentH32_Type = Counter32
_TmnxDAHttpServer3XXCountSentH32_Object = MibTableColumn
tmnxDAHttpServer3XXCountSentH32 = _TmnxDAHttpServer3XXCountSentH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 29),
    _TmnxDAHttpServer3XXCountSentH32_Type()
)
tmnxDAHttpServer3XXCountSentH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer3XXCountSentH32.setStatus("current")
_TmnxDAHttpServer4XXCountSent_Type = Counter64
_TmnxDAHttpServer4XXCountSent_Object = MibTableColumn
tmnxDAHttpServer4XXCountSent = _TmnxDAHttpServer4XXCountSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 30),
    _TmnxDAHttpServer4XXCountSent_Type()
)
tmnxDAHttpServer4XXCountSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer4XXCountSent.setStatus("current")
_TmnxDAHttpServer4XXCountSentL32_Type = Counter32
_TmnxDAHttpServer4XXCountSentL32_Object = MibTableColumn
tmnxDAHttpServer4XXCountSentL32 = _TmnxDAHttpServer4XXCountSentL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 31),
    _TmnxDAHttpServer4XXCountSentL32_Type()
)
tmnxDAHttpServer4XXCountSentL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer4XXCountSentL32.setStatus("current")
_TmnxDAHttpServer4XXCountSentH32_Type = Counter32
_TmnxDAHttpServer4XXCountSentH32_Object = MibTableColumn
tmnxDAHttpServer4XXCountSentH32 = _TmnxDAHttpServer4XXCountSentH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 32),
    _TmnxDAHttpServer4XXCountSentH32_Type()
)
tmnxDAHttpServer4XXCountSentH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer4XXCountSentH32.setStatus("current")
_TmnxDAHttpServer5XXCountSent_Type = Counter64
_TmnxDAHttpServer5XXCountSent_Object = MibTableColumn
tmnxDAHttpServer5XXCountSent = _TmnxDAHttpServer5XXCountSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 33),
    _TmnxDAHttpServer5XXCountSent_Type()
)
tmnxDAHttpServer5XXCountSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer5XXCountSent.setStatus("current")
_TmnxDAHttpServer5XXCountSentL32_Type = Counter32
_TmnxDAHttpServer5XXCountSentL32_Object = MibTableColumn
tmnxDAHttpServer5XXCountSentL32 = _TmnxDAHttpServer5XXCountSentL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 34),
    _TmnxDAHttpServer5XXCountSentL32_Type()
)
tmnxDAHttpServer5XXCountSentL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer5XXCountSentL32.setStatus("current")
_TmnxDAHttpServer5XXCountSentH32_Type = Counter32
_TmnxDAHttpServer5XXCountSentH32_Object = MibTableColumn
tmnxDAHttpServer5XXCountSentH32 = _TmnxDAHttpServer5XXCountSentH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 35),
    _TmnxDAHttpServer5XXCountSentH32_Type()
)
tmnxDAHttpServer5XXCountSentH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpServer5XXCountSentH32.setStatus("current")


class _TmnxDAHttpIngestAdminState_Type(TmnxAdminState):
    """Custom type tmnxDAHttpIngestAdminState based on TmnxAdminState"""


_TmnxDAHttpIngestAdminState_Object = MibTableColumn
tmnxDAHttpIngestAdminState = _TmnxDAHttpIngestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 36),
    _TmnxDAHttpIngestAdminState_Type()
)
tmnxDAHttpIngestAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestAdminState.setStatus("current")
_TmnxDAHttpIngestOperState_Type = TmnxOperState
_TmnxDAHttpIngestOperState_Object = MibTableColumn
tmnxDAHttpIngestOperState = _TmnxDAHttpIngestOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 37),
    _TmnxDAHttpIngestOperState_Type()
)
tmnxDAHttpIngestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestOperState.setStatus("current")


class _TmnxDAHttpIngestIsmLinkName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDAHttpIngestIsmLinkName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxDAHttpIngestIsmLinkName_Object = MibTableColumn
tmnxDAHttpIngestIsmLinkName = _TmnxDAHttpIngestIsmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 38),
    _TmnxDAHttpIngestIsmLinkName_Type()
)
tmnxDAHttpIngestIsmLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestIsmLinkName.setStatus("current")


class _TmnxDAHttpIngestIdleTimeout_Type(Unsigned32):
    """Custom type tmnxDAHttpIngestIdleTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_TmnxDAHttpIngestIdleTimeout_Type.__name__ = "Unsigned32"
_TmnxDAHttpIngestIdleTimeout_Object = MibTableColumn
tmnxDAHttpIngestIdleTimeout = _TmnxDAHttpIngestIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 39),
    _TmnxDAHttpIngestIdleTimeout_Type()
)
tmnxDAHttpIngestIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestIdleTimeout.setUnits("seconds")
_TmnxDAHttpIngestXferInProg_Type = Gauge32
_TmnxDAHttpIngestXferInProg_Object = MibTableColumn
tmnxDAHttpIngestXferInProg = _TmnxDAHttpIngestXferInProg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 40),
    _TmnxDAHttpIngestXferInProg_Type()
)
tmnxDAHttpIngestXferInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestXferInProg.setStatus("current")
_TmnxDAHttpIngestXferCompleted_Type = Counter64
_TmnxDAHttpIngestXferCompleted_Object = MibTableColumn
tmnxDAHttpIngestXferCompleted = _TmnxDAHttpIngestXferCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 41),
    _TmnxDAHttpIngestXferCompleted_Type()
)
tmnxDAHttpIngestXferCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestXferCompleted.setStatus("current")
_TmnxDAHttpIngestXferCompletedL32_Type = Counter32
_TmnxDAHttpIngestXferCompletedL32_Object = MibTableColumn
tmnxDAHttpIngestXferCompletedL32 = _TmnxDAHttpIngestXferCompletedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 42),
    _TmnxDAHttpIngestXferCompletedL32_Type()
)
tmnxDAHttpIngestXferCompletedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestXferCompletedL32.setStatus("current")
_TmnxDAHttpIngestXferCompletedH32_Type = Counter32
_TmnxDAHttpIngestXferCompletedH32_Object = MibTableColumn
tmnxDAHttpIngestXferCompletedH32 = _TmnxDAHttpIngestXferCompletedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 43),
    _TmnxDAHttpIngestXferCompletedH32_Type()
)
tmnxDAHttpIngestXferCompletedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestXferCompletedH32.setStatus("current")
_TmnxDAHttpIngestXferTimeouts_Type = Gauge32
_TmnxDAHttpIngestXferTimeouts_Object = MibTableColumn
tmnxDAHttpIngestXferTimeouts = _TmnxDAHttpIngestXferTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 44),
    _TmnxDAHttpIngestXferTimeouts_Type()
)
tmnxDAHttpIngestXferTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestXferTimeouts.setStatus("current")
_TmnxDAHttpIngestXferFailed_Type = Gauge32
_TmnxDAHttpIngestXferFailed_Object = MibTableColumn
tmnxDAHttpIngestXferFailed = _TmnxDAHttpIngestXferFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 45),
    _TmnxDAHttpIngestXferFailed_Type()
)
tmnxDAHttpIngestXferFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngestXferFailed.setStatus("current")
_TmnxDAHttpIngest1XXCountRecd_Type = Counter64
_TmnxDAHttpIngest1XXCountRecd_Object = MibTableColumn
tmnxDAHttpIngest1XXCountRecd = _TmnxDAHttpIngest1XXCountRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 46),
    _TmnxDAHttpIngest1XXCountRecd_Type()
)
tmnxDAHttpIngest1XXCountRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest1XXCountRecd.setStatus("current")
_TmnxDAHttpIngest1XXCountRecdL32_Type = Counter32
_TmnxDAHttpIngest1XXCountRecdL32_Object = MibTableColumn
tmnxDAHttpIngest1XXCountRecdL32 = _TmnxDAHttpIngest1XXCountRecdL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 47),
    _TmnxDAHttpIngest1XXCountRecdL32_Type()
)
tmnxDAHttpIngest1XXCountRecdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest1XXCountRecdL32.setStatus("current")
_TmnxDAHttpIngest1XXCountRecdH32_Type = Counter32
_TmnxDAHttpIngest1XXCountRecdH32_Object = MibTableColumn
tmnxDAHttpIngest1XXCountRecdH32 = _TmnxDAHttpIngest1XXCountRecdH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 48),
    _TmnxDAHttpIngest1XXCountRecdH32_Type()
)
tmnxDAHttpIngest1XXCountRecdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest1XXCountRecdH32.setStatus("current")
_TmnxDAHttpIngest2XXCountRecd_Type = Counter64
_TmnxDAHttpIngest2XXCountRecd_Object = MibTableColumn
tmnxDAHttpIngest2XXCountRecd = _TmnxDAHttpIngest2XXCountRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 49),
    _TmnxDAHttpIngest2XXCountRecd_Type()
)
tmnxDAHttpIngest2XXCountRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest2XXCountRecd.setStatus("current")
_TmnxDAHttpIngest2XXCountRecdL32_Type = Counter32
_TmnxDAHttpIngest2XXCountRecdL32_Object = MibTableColumn
tmnxDAHttpIngest2XXCountRecdL32 = _TmnxDAHttpIngest2XXCountRecdL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 50),
    _TmnxDAHttpIngest2XXCountRecdL32_Type()
)
tmnxDAHttpIngest2XXCountRecdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest2XXCountRecdL32.setStatus("current")
_TmnxDAHttpIngest2XXCountRecdH32_Type = Counter32
_TmnxDAHttpIngest2XXCountRecdH32_Object = MibTableColumn
tmnxDAHttpIngest2XXCountRecdH32 = _TmnxDAHttpIngest2XXCountRecdH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 51),
    _TmnxDAHttpIngest2XXCountRecdH32_Type()
)
tmnxDAHttpIngest2XXCountRecdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest2XXCountRecdH32.setStatus("current")
_TmnxDAHttpIngest3XXCountRecd_Type = Counter64
_TmnxDAHttpIngest3XXCountRecd_Object = MibTableColumn
tmnxDAHttpIngest3XXCountRecd = _TmnxDAHttpIngest3XXCountRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 52),
    _TmnxDAHttpIngest3XXCountRecd_Type()
)
tmnxDAHttpIngest3XXCountRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest3XXCountRecd.setStatus("current")
_TmnxDAHttpIngest3XXCountRecdL32_Type = Counter32
_TmnxDAHttpIngest3XXCountRecdL32_Object = MibTableColumn
tmnxDAHttpIngest3XXCountRecdL32 = _TmnxDAHttpIngest3XXCountRecdL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 53),
    _TmnxDAHttpIngest3XXCountRecdL32_Type()
)
tmnxDAHttpIngest3XXCountRecdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest3XXCountRecdL32.setStatus("current")
_TmnxDAHttpIngest3XXCountRecdH32_Type = Counter32
_TmnxDAHttpIngest3XXCountRecdH32_Object = MibTableColumn
tmnxDAHttpIngest3XXCountRecdH32 = _TmnxDAHttpIngest3XXCountRecdH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 54),
    _TmnxDAHttpIngest3XXCountRecdH32_Type()
)
tmnxDAHttpIngest3XXCountRecdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest3XXCountRecdH32.setStatus("current")
_TmnxDAHttpIngest4XXCountRecd_Type = Counter64
_TmnxDAHttpIngest4XXCountRecd_Object = MibTableColumn
tmnxDAHttpIngest4XXCountRecd = _TmnxDAHttpIngest4XXCountRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 55),
    _TmnxDAHttpIngest4XXCountRecd_Type()
)
tmnxDAHttpIngest4XXCountRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest4XXCountRecd.setStatus("current")
_TmnxDAHttpIngest4XXCountRecdL32_Type = Counter32
_TmnxDAHttpIngest4XXCountRecdL32_Object = MibTableColumn
tmnxDAHttpIngest4XXCountRecdL32 = _TmnxDAHttpIngest4XXCountRecdL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 56),
    _TmnxDAHttpIngest4XXCountRecdL32_Type()
)
tmnxDAHttpIngest4XXCountRecdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest4XXCountRecdL32.setStatus("current")
_TmnxDAHttpIngest4XXCountRecdH32_Type = Counter32
_TmnxDAHttpIngest4XXCountRecdH32_Object = MibTableColumn
tmnxDAHttpIngest4XXCountRecdH32 = _TmnxDAHttpIngest4XXCountRecdH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 57),
    _TmnxDAHttpIngest4XXCountRecdH32_Type()
)
tmnxDAHttpIngest4XXCountRecdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest4XXCountRecdH32.setStatus("current")
_TmnxDAHttpIngest5XXCountRecd_Type = Counter64
_TmnxDAHttpIngest5XXCountRecd_Object = MibTableColumn
tmnxDAHttpIngest5XXCountRecd = _TmnxDAHttpIngest5XXCountRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 58),
    _TmnxDAHttpIngest5XXCountRecd_Type()
)
tmnxDAHttpIngest5XXCountRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest5XXCountRecd.setStatus("current")
_TmnxDAHttpIngest5XXCountRecdL32_Type = Counter32
_TmnxDAHttpIngest5XXCountRecdL32_Object = MibTableColumn
tmnxDAHttpIngest5XXCountRecdL32 = _TmnxDAHttpIngest5XXCountRecdL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 59),
    _TmnxDAHttpIngest5XXCountRecdL32_Type()
)
tmnxDAHttpIngest5XXCountRecdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest5XXCountRecdL32.setStatus("current")
_TmnxDAHttpIngest5XXCountRecdH32_Type = Counter32
_TmnxDAHttpIngest5XXCountRecdH32_Object = MibTableColumn
tmnxDAHttpIngest5XXCountRecdH32 = _TmnxDAHttpIngest5XXCountRecdH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 10, 1, 60),
    _TmnxDAHttpIngest5XXCountRecdH32_Type()
)
tmnxDAHttpIngest5XXCountRecdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAHttpIngest5XXCountRecdH32.setStatus("current")
_TmnxDAIsmLinkTableLastChanged_Type = TimeStamp
_TmnxDAIsmLinkTableLastChanged_Object = MibScalar
tmnxDAIsmLinkTableLastChanged = _TmnxDAIsmLinkTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 11),
    _TmnxDAIsmLinkTableLastChanged_Type()
)
tmnxDAIsmLinkTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkTableLastChanged.setStatus("current")
_TmnxDAIsmLinkTable_Object = MibTable
tmnxDAIsmLinkTable = _TmnxDAIsmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxDAIsmLinkTable.setStatus("current")
_TmnxDAIsmLinkEntry_Object = MibTableRow
tmnxDAIsmLinkEntry = _TmnxDAIsmLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1)
)
tmnxDAIsmLinkEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
    (0, "TIMETRA-DA-MIB", "tmnxDAIsmLinkName"),
)
if mibBuilder.loadTexts:
    tmnxDAIsmLinkEntry.setStatus("current")
_TmnxDAIsmLinkName_Type = TNamedItem
_TmnxDAIsmLinkName_Object = MibTableColumn
tmnxDAIsmLinkName = _TmnxDAIsmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 1),
    _TmnxDAIsmLinkName_Type()
)
tmnxDAIsmLinkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkName.setStatus("current")
_TmnxDAIsmLinkRowStatus_Type = RowStatus
_TmnxDAIsmLinkRowStatus_Object = MibTableColumn
tmnxDAIsmLinkRowStatus = _TmnxDAIsmLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 2),
    _TmnxDAIsmLinkRowStatus_Type()
)
tmnxDAIsmLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkRowStatus.setStatus("current")
_TmnxDAIsmLinkLastChanged_Type = TimeStamp
_TmnxDAIsmLinkLastChanged_Object = MibTableColumn
tmnxDAIsmLinkLastChanged = _TmnxDAIsmLinkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 3),
    _TmnxDAIsmLinkLastChanged_Type()
)
tmnxDAIsmLinkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkLastChanged.setStatus("current")


class _TmnxDAIsmLinkAddrType_Type(InetAddressType):
    """Custom type tmnxDAIsmLinkAddrType based on InetAddressType"""


_TmnxDAIsmLinkAddrType_Object = MibTableColumn
tmnxDAIsmLinkAddrType = _TmnxDAIsmLinkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 4),
    _TmnxDAIsmLinkAddrType_Type()
)
tmnxDAIsmLinkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkAddrType.setStatus("current")


class _TmnxDAIsmLinkAddress_Type(InetAddress):
    """Custom type tmnxDAIsmLinkAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDAIsmLinkAddress_Type.__name__ = "InetAddress"
_TmnxDAIsmLinkAddress_Object = MibTableColumn
tmnxDAIsmLinkAddress = _TmnxDAIsmLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 5),
    _TmnxDAIsmLinkAddress_Type()
)
tmnxDAIsmLinkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkAddress.setStatus("current")


class _TmnxDAIsmLinkAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxDAIsmLinkAddrPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxDAIsmLinkAddrPrefixLength_Object = MibTableColumn
tmnxDAIsmLinkAddrPrefixLength = _TmnxDAIsmLinkAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 6),
    _TmnxDAIsmLinkAddrPrefixLength_Type()
)
tmnxDAIsmLinkAddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkAddrPrefixLength.setStatus("current")


class _TmnxDAIsmLinkDescription_Type(TItemDescription):
    """Custom type tmnxDAIsmLinkDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxDAIsmLinkDescription_Object = MibTableColumn
tmnxDAIsmLinkDescription = _TmnxDAIsmLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 7),
    _TmnxDAIsmLinkDescription_Type()
)
tmnxDAIsmLinkDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkDescription.setStatus("current")


class _TmnxDAIsmLinkHttpd_Type(TruthValue):
    """Custom type tmnxDAIsmLinkHttpd based on TruthValue"""


_TmnxDAIsmLinkHttpd_Object = MibTableColumn
tmnxDAIsmLinkHttpd = _TmnxDAIsmLinkHttpd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 8),
    _TmnxDAIsmLinkHttpd_Type()
)
tmnxDAIsmLinkHttpd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkHttpd.setStatus("current")


class _TmnxDAIsmLinkHttpListenPort_Type(InetPortNumber):
    """Custom type tmnxDAIsmLinkHttpListenPort based on InetPortNumber"""
    defaultValue = 80


_TmnxDAIsmLinkHttpListenPort_Object = MibTableColumn
tmnxDAIsmLinkHttpListenPort = _TmnxDAIsmLinkHttpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 9),
    _TmnxDAIsmLinkHttpListenPort_Type()
)
tmnxDAIsmLinkHttpListenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkHttpListenPort.setStatus("current")


class _TmnxDAIsmLinkIpMtu_Type(Unsigned32):
    """Custom type tmnxDAIsmLinkIpMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9212),
    )


_TmnxDAIsmLinkIpMtu_Type.__name__ = "Unsigned32"
_TmnxDAIsmLinkIpMtu_Object = MibTableColumn
tmnxDAIsmLinkIpMtu = _TmnxDAIsmLinkIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 10),
    _TmnxDAIsmLinkIpMtu_Type()
)
tmnxDAIsmLinkIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkIpMtu.setStatus("current")


class _TmnxDAIsmLinkQtag_Type(Unsigned32):
    """Custom type tmnxDAIsmLinkQtag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_TmnxDAIsmLinkQtag_Type.__name__ = "Unsigned32"
_TmnxDAIsmLinkQtag_Object = MibTableColumn
tmnxDAIsmLinkQtag = _TmnxDAIsmLinkQtag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 11),
    _TmnxDAIsmLinkQtag_Type()
)
tmnxDAIsmLinkQtag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkQtag.setStatus("current")


class _TmnxDAIsmLinkMacAddress_Type(MacAddress):
    """Custom type tmnxDAIsmLinkMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDAIsmLinkMacAddress_Object = MibTableColumn
tmnxDAIsmLinkMacAddress = _TmnxDAIsmLinkMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 12),
    _TmnxDAIsmLinkMacAddress_Type()
)
tmnxDAIsmLinkMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkMacAddress.setStatus("current")


class _TmnxDAIsmLinkAdminState_Type(TmnxAdminState):
    """Custom type tmnxDAIsmLinkAdminState based on TmnxAdminState"""


_TmnxDAIsmLinkAdminState_Object = MibTableColumn
tmnxDAIsmLinkAdminState = _TmnxDAIsmLinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 13),
    _TmnxDAIsmLinkAdminState_Type()
)
tmnxDAIsmLinkAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkAdminState.setStatus("current")
_TmnxDAIsmLinkOperState_Type = TmnxOperState
_TmnxDAIsmLinkOperState_Object = MibTableColumn
tmnxDAIsmLinkOperState = _TmnxDAIsmLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 14),
    _TmnxDAIsmLinkOperState_Type()
)
tmnxDAIsmLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkOperState.setStatus("current")


class _TmnxDAIsmLinkBindings_Type(Bits):
    """Custom type tmnxDAIsmLinkBindings based on Bits"""
    namedValues = NamedValues(
        *(("deliveryController", 0),
          ("dnsClient", 2),
          ("httpIngest", 1))
    )

_TmnxDAIsmLinkBindings_Type.__name__ = "Bits"
_TmnxDAIsmLinkBindings_Object = MibTableColumn
tmnxDAIsmLinkBindings = _TmnxDAIsmLinkBindings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 12, 1, 15),
    _TmnxDAIsmLinkBindings_Type()
)
tmnxDAIsmLinkBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkBindings.setStatus("current")
_TmnxDAIsmLinkArpTableLastChanged_Type = TimeStamp
_TmnxDAIsmLinkArpTableLastChanged_Object = MibScalar
tmnxDAIsmLinkArpTableLastChanged = _TmnxDAIsmLinkArpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 13),
    _TmnxDAIsmLinkArpTableLastChanged_Type()
)
tmnxDAIsmLinkArpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpTableLastChanged.setStatus("current")
_TmnxDAIsmLinkArpTable_Object = MibTable
tmnxDAIsmLinkArpTable = _TmnxDAIsmLinkArpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpTable.setStatus("current")
_TmnxDAIsmLinkArpEntry_Object = MibTableRow
tmnxDAIsmLinkArpEntry = _TmnxDAIsmLinkArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14, 1)
)
tmnxDAIsmLinkArpEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
    (0, "TIMETRA-DA-MIB", "tmnxDAIsmLinkName"),
    (0, "TIMETRA-DA-MIB", "tmnxDAIsmLinkArpAddrType"),
    (0, "TIMETRA-DA-MIB", "tmnxDAIsmLinkArpAddress"),
)
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpEntry.setStatus("current")
_TmnxDAIsmLinkArpAddrType_Type = InetAddressType
_TmnxDAIsmLinkArpAddrType_Object = MibTableColumn
tmnxDAIsmLinkArpAddrType = _TmnxDAIsmLinkArpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14, 1, 1),
    _TmnxDAIsmLinkArpAddrType_Type()
)
tmnxDAIsmLinkArpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpAddrType.setStatus("current")


class _TmnxDAIsmLinkArpAddress_Type(InetAddress):
    """Custom type tmnxDAIsmLinkArpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDAIsmLinkArpAddress_Type.__name__ = "InetAddress"
_TmnxDAIsmLinkArpAddress_Object = MibTableColumn
tmnxDAIsmLinkArpAddress = _TmnxDAIsmLinkArpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14, 1, 2),
    _TmnxDAIsmLinkArpAddress_Type()
)
tmnxDAIsmLinkArpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpAddress.setStatus("current")
_TmnxDAIsmLinkArpRowStatus_Type = RowStatus
_TmnxDAIsmLinkArpRowStatus_Object = MibTableColumn
tmnxDAIsmLinkArpRowStatus = _TmnxDAIsmLinkArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14, 1, 3),
    _TmnxDAIsmLinkArpRowStatus_Type()
)
tmnxDAIsmLinkArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpRowStatus.setStatus("current")
_TmnxDAIsmLinkArpLastChanged_Type = TimeStamp
_TmnxDAIsmLinkArpLastChanged_Object = MibTableColumn
tmnxDAIsmLinkArpLastChanged = _TmnxDAIsmLinkArpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14, 1, 4),
    _TmnxDAIsmLinkArpLastChanged_Type()
)
tmnxDAIsmLinkArpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpLastChanged.setStatus("current")


class _TmnxDAIsmLinkArpMacAddr_Type(MacAddress):
    """Custom type tmnxDAIsmLinkArpMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDAIsmLinkArpMacAddr_Object = MibTableColumn
tmnxDAIsmLinkArpMacAddr = _TmnxDAIsmLinkArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14, 1, 5),
    _TmnxDAIsmLinkArpMacAddr_Type()
)
tmnxDAIsmLinkArpMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpMacAddr.setStatus("current")
_TmnxDAIsmLinkArpType_Type = TruthValue
_TmnxDAIsmLinkArpType_Object = MibTableColumn
tmnxDAIsmLinkArpType = _TmnxDAIsmLinkArpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 14, 1, 6),
    _TmnxDAIsmLinkArpType_Type()
)
tmnxDAIsmLinkArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAIsmLinkArpType.setStatus("current")
_TmnxDAStRouteTableLastChanged_Type = TimeStamp
_TmnxDAStRouteTableLastChanged_Object = MibScalar
tmnxDAStRouteTableLastChanged = _TmnxDAStRouteTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 15),
    _TmnxDAStRouteTableLastChanged_Type()
)
tmnxDAStRouteTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAStRouteTableLastChanged.setStatus("current")
_TmnxDAStRouteTable_Object = MibTable
tmnxDAStRouteTable = _TmnxDAStRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxDAStRouteTable.setStatus("current")
_TmnxDAStRouteEntry_Object = MibTableRow
tmnxDAStRouteEntry = _TmnxDAStRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1)
)
tmnxDAStRouteEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
    (0, "TIMETRA-DA-MIB", "tmnxDAStRouteAddrType"),
    (0, "TIMETRA-DA-MIB", "tmnxDAStRouteAddress"),
    (0, "TIMETRA-DA-MIB", "tmnxDAStRoutePrefixLength"),
    (0, "TIMETRA-DA-MIB", "tmnxDAStRouteNextHopAddrType"),
    (0, "TIMETRA-DA-MIB", "tmnxDAStRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    tmnxDAStRouteEntry.setStatus("current")
_TmnxDAStRouteAddrType_Type = InetAddressType
_TmnxDAStRouteAddrType_Object = MibTableColumn
tmnxDAStRouteAddrType = _TmnxDAStRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 1),
    _TmnxDAStRouteAddrType_Type()
)
tmnxDAStRouteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAStRouteAddrType.setStatus("current")


class _TmnxDAStRouteAddress_Type(InetAddress):
    """Custom type tmnxDAStRouteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDAStRouteAddress_Type.__name__ = "InetAddress"
_TmnxDAStRouteAddress_Object = MibTableColumn
tmnxDAStRouteAddress = _TmnxDAStRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 2),
    _TmnxDAStRouteAddress_Type()
)
tmnxDAStRouteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAStRouteAddress.setStatus("current")
_TmnxDAStRoutePrefixLength_Type = InetAddressPrefixLength
_TmnxDAStRoutePrefixLength_Object = MibTableColumn
tmnxDAStRoutePrefixLength = _TmnxDAStRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 3),
    _TmnxDAStRoutePrefixLength_Type()
)
tmnxDAStRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAStRoutePrefixLength.setStatus("current")
_TmnxDAStRouteNextHopAddrType_Type = InetAddressType
_TmnxDAStRouteNextHopAddrType_Object = MibTableColumn
tmnxDAStRouteNextHopAddrType = _TmnxDAStRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 4),
    _TmnxDAStRouteNextHopAddrType_Type()
)
tmnxDAStRouteNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAStRouteNextHopAddrType.setStatus("current")


class _TmnxDAStRouteNextHopAddress_Type(InetAddress):
    """Custom type tmnxDAStRouteNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDAStRouteNextHopAddress_Type.__name__ = "InetAddress"
_TmnxDAStRouteNextHopAddress_Object = MibTableColumn
tmnxDAStRouteNextHopAddress = _TmnxDAStRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 5),
    _TmnxDAStRouteNextHopAddress_Type()
)
tmnxDAStRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAStRouteNextHopAddress.setStatus("current")
_TmnxDAStRouteRowStatus_Type = RowStatus
_TmnxDAStRouteRowStatus_Object = MibTableColumn
tmnxDAStRouteRowStatus = _TmnxDAStRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 6),
    _TmnxDAStRouteRowStatus_Type()
)
tmnxDAStRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAStRouteRowStatus.setStatus("current")
_TmnxDAStRouteLastChanged_Type = TimeStamp
_TmnxDAStRouteLastChanged_Object = MibTableColumn
tmnxDAStRouteLastChanged = _TmnxDAStRouteLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 7),
    _TmnxDAStRouteLastChanged_Type()
)
tmnxDAStRouteLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAStRouteLastChanged.setStatus("current")


class _TmnxDAStRouteMetric_Type(Unsigned32):
    """Custom type tmnxDAStRouteMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxDAStRouteMetric_Type.__name__ = "Unsigned32"
_TmnxDAStRouteMetric_Object = MibTableColumn
tmnxDAStRouteMetric = _TmnxDAStRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 16, 1, 8),
    _TmnxDAStRouteMetric_Type()
)
tmnxDAStRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDAStRouteMetric.setStatus("current")
_TmnxDASGCardTable_Object = MibTable
tmnxDASGCardTable = _TmnxDASGCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxDASGCardTable.setStatus("current")
_TmnxDASGCardEntry_Object = MibTableRow
tmnxDASGCardEntry = _TmnxDASGCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1)
)
tmnxDASGCardEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDASvrGrpIndex"),
    (0, "TIMETRA-DA-MIB", "tmnxDASGCardNumber"),
)
if mibBuilder.loadTexts:
    tmnxDASGCardEntry.setStatus("current")


class _TmnxDASGCardNumber_Type(Integer32):
    """Custom type tmnxDASGCardNumber based on Integer32"""
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
        *(("card1", 1),
          ("card10", 10),
          ("card2", 2),
          ("card3", 3),
          ("card4", 4),
          ("card5", 5),
          ("card6", 6),
          ("card7", 7),
          ("card8", 8),
          ("card9", 9))
    )


_TmnxDASGCardNumber_Type.__name__ = "Integer32"
_TmnxDASGCardNumber_Object = MibTableColumn
tmnxDASGCardNumber = _TmnxDASGCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 1),
    _TmnxDASGCardNumber_Type()
)
tmnxDASGCardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDASGCardNumber.setStatus("current")
_TmnxDASGCardUpTime_Type = Gauge32
_TmnxDASGCardUpTime_Object = MibTableColumn
tmnxDASGCardUpTime = _TmnxDASGCardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 2),
    _TmnxDASGCardUpTime_Type()
)
tmnxDASGCardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardUpTime.setStatus("current")
_TmnxDASGCardTotNumTCPConn_Type = Counter32
_TmnxDASGCardTotNumTCPConn_Object = MibTableColumn
tmnxDASGCardTotNumTCPConn = _TmnxDASGCardTotNumTCPConn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 3),
    _TmnxDASGCardTotNumTCPConn_Type()
)
tmnxDASGCardTotNumTCPConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTotNumTCPConn.setStatus("current")
_TmnxDASGCardTCPConnEstab_Type = Counter64
_TmnxDASGCardTCPConnEstab_Object = MibTableColumn
tmnxDASGCardTCPConnEstab = _TmnxDASGCardTCPConnEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 4),
    _TmnxDASGCardTCPConnEstab_Type()
)
tmnxDASGCardTCPConnEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPConnEstab.setStatus("current")
_TmnxDASGCardTCPConnEstabL32_Type = Counter32
_TmnxDASGCardTCPConnEstabL32_Object = MibTableColumn
tmnxDASGCardTCPConnEstabL32 = _TmnxDASGCardTCPConnEstabL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 5),
    _TmnxDASGCardTCPConnEstabL32_Type()
)
tmnxDASGCardTCPConnEstabL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPConnEstabL32.setStatus("current")
_TmnxDASGCardTCPConnEstabH32_Type = Counter32
_TmnxDASGCardTCPConnEstabH32_Object = MibTableColumn
tmnxDASGCardTCPConnEstabH32 = _TmnxDASGCardTCPConnEstabH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 6),
    _TmnxDASGCardTCPConnEstabH32_Type()
)
tmnxDASGCardTCPConnEstabH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPConnEstabH32.setStatus("current")
_TmnxDASGCardTCPConnClosed_Type = Counter64
_TmnxDASGCardTCPConnClosed_Object = MibTableColumn
tmnxDASGCardTCPConnClosed = _TmnxDASGCardTCPConnClosed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 7),
    _TmnxDASGCardTCPConnClosed_Type()
)
tmnxDASGCardTCPConnClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPConnClosed.setStatus("current")
_TmnxDASGCardTCPConnClosedL32_Type = Counter32
_TmnxDASGCardTCPConnClosedL32_Object = MibTableColumn
tmnxDASGCardTCPConnClosedL32 = _TmnxDASGCardTCPConnClosedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 8),
    _TmnxDASGCardTCPConnClosedL32_Type()
)
tmnxDASGCardTCPConnClosedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPConnClosedL32.setStatus("current")
_TmnxDASGCardTCPConnClosedH32_Type = Counter32
_TmnxDASGCardTCPConnClosedH32_Object = MibTableColumn
tmnxDASGCardTCPConnClosedH32 = _TmnxDASGCardTCPConnClosedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 9),
    _TmnxDASGCardTCPConnClosedH32_Type()
)
tmnxDASGCardTCPConnClosedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPConnClosedH32.setStatus("current")
_TmnxDASGCardTCPRetries_Type = Counter64
_TmnxDASGCardTCPRetries_Object = MibTableColumn
tmnxDASGCardTCPRetries = _TmnxDASGCardTCPRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 10),
    _TmnxDASGCardTCPRetries_Type()
)
tmnxDASGCardTCPRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPRetries.setStatus("current")
_TmnxDASGCardTCPRetriesL32_Type = Counter32
_TmnxDASGCardTCPRetriesL32_Object = MibTableColumn
tmnxDASGCardTCPRetriesL32 = _TmnxDASGCardTCPRetriesL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 11),
    _TmnxDASGCardTCPRetriesL32_Type()
)
tmnxDASGCardTCPRetriesL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPRetriesL32.setStatus("current")
_TmnxDASGCardTCPRetriesH32_Type = Counter32
_TmnxDASGCardTCPRetriesH32_Object = MibTableColumn
tmnxDASGCardTCPRetriesH32 = _TmnxDASGCardTCPRetriesH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 12),
    _TmnxDASGCardTCPRetriesH32_Type()
)
tmnxDASGCardTCPRetriesH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPRetriesH32.setStatus("current")
_TmnxDASGCardTCPAckTimeOut_Type = Counter64
_TmnxDASGCardTCPAckTimeOut_Object = MibTableColumn
tmnxDASGCardTCPAckTimeOut = _TmnxDASGCardTCPAckTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 13),
    _TmnxDASGCardTCPAckTimeOut_Type()
)
tmnxDASGCardTCPAckTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPAckTimeOut.setStatus("current")
_TmnxDASGCardTCPAckTimeOutL32_Type = Counter32
_TmnxDASGCardTCPAckTimeOutL32_Object = MibTableColumn
tmnxDASGCardTCPAckTimeOutL32 = _TmnxDASGCardTCPAckTimeOutL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 14),
    _TmnxDASGCardTCPAckTimeOutL32_Type()
)
tmnxDASGCardTCPAckTimeOutL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPAckTimeOutL32.setStatus("current")
_TmnxDASGCardTCPAckTimeOutH32_Type = Counter32
_TmnxDASGCardTCPAckTimeOutH32_Object = MibTableColumn
tmnxDASGCardTCPAckTimeOutH32 = _TmnxDASGCardTCPAckTimeOutH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 15),
    _TmnxDASGCardTCPAckTimeOutH32_Type()
)
tmnxDASGCardTCPAckTimeOutH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPAckTimeOutH32.setStatus("current")
_TmnxDASGCardTCPFarEndClosed_Type = Counter64
_TmnxDASGCardTCPFarEndClosed_Object = MibTableColumn
tmnxDASGCardTCPFarEndClosed = _TmnxDASGCardTCPFarEndClosed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 16),
    _TmnxDASGCardTCPFarEndClosed_Type()
)
tmnxDASGCardTCPFarEndClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPFarEndClosed.setStatus("current")
_TmnxDASGCardTCPFarEndClosedL32_Type = Counter32
_TmnxDASGCardTCPFarEndClosedL32_Object = MibTableColumn
tmnxDASGCardTCPFarEndClosedL32 = _TmnxDASGCardTCPFarEndClosedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 17),
    _TmnxDASGCardTCPFarEndClosedL32_Type()
)
tmnxDASGCardTCPFarEndClosedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPFarEndClosedL32.setStatus("current")
_TmnxDASGCardTCPFarEndClosedH32_Type = Counter32
_TmnxDASGCardTCPFarEndClosedH32_Object = MibTableColumn
tmnxDASGCardTCPFarEndClosedH32 = _TmnxDASGCardTCPFarEndClosedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 18),
    _TmnxDASGCardTCPFarEndClosedH32_Type()
)
tmnxDASGCardTCPFarEndClosedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPFarEndClosedH32.setStatus("current")
_TmnxDASGCardTCPLocalEndClosed_Type = Counter64
_TmnxDASGCardTCPLocalEndClosed_Object = MibTableColumn
tmnxDASGCardTCPLocalEndClosed = _TmnxDASGCardTCPLocalEndClosed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 19),
    _TmnxDASGCardTCPLocalEndClosed_Type()
)
tmnxDASGCardTCPLocalEndClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPLocalEndClosed.setStatus("current")
_TmnxDASGCardTCPLocalEndClosedL32_Type = Counter32
_TmnxDASGCardTCPLocalEndClosedL32_Object = MibTableColumn
tmnxDASGCardTCPLocalEndClosedL32 = _TmnxDASGCardTCPLocalEndClosedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 20),
    _TmnxDASGCardTCPLocalEndClosedL32_Type()
)
tmnxDASGCardTCPLocalEndClosedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPLocalEndClosedL32.setStatus("current")
_TmnxDASGCardTCPLocalEndClosedH32_Type = Counter32
_TmnxDASGCardTCPLocalEndClosedH32_Object = MibTableColumn
tmnxDASGCardTCPLocalEndClosedH32 = _TmnxDASGCardTCPLocalEndClosedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 21),
    _TmnxDASGCardTCPLocalEndClosedH32_Type()
)
tmnxDASGCardTCPLocalEndClosedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardTCPLocalEndClosedH32.setStatus("current")
_TmnxDASGCardUsedStorageCpcty_Type = Counter64
_TmnxDASGCardUsedStorageCpcty_Object = MibTableColumn
tmnxDASGCardUsedStorageCpcty = _TmnxDASGCardUsedStorageCpcty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 22),
    _TmnxDASGCardUsedStorageCpcty_Type()
)
tmnxDASGCardUsedStorageCpcty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardUsedStorageCpcty.setStatus("current")
_TmnxDASGCardUsedStorageCpctyL32_Type = Counter32
_TmnxDASGCardUsedStorageCpctyL32_Object = MibTableColumn
tmnxDASGCardUsedStorageCpctyL32 = _TmnxDASGCardUsedStorageCpctyL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 23),
    _TmnxDASGCardUsedStorageCpctyL32_Type()
)
tmnxDASGCardUsedStorageCpctyL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardUsedStorageCpctyL32.setStatus("current")
_TmnxDASGCardUsedStorageCpctyH32_Type = Counter32
_TmnxDASGCardUsedStorageCpctyH32_Object = MibTableColumn
tmnxDASGCardUsedStorageCpctyH32 = _TmnxDASGCardUsedStorageCpctyH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 24),
    _TmnxDASGCardUsedStorageCpctyH32_Type()
)
tmnxDASGCardUsedStorageCpctyH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardUsedStorageCpctyH32.setStatus("current")
_TmnxDASGCardRemStorageCpcty_Type = Counter64
_TmnxDASGCardRemStorageCpcty_Object = MibTableColumn
tmnxDASGCardRemStorageCpcty = _TmnxDASGCardRemStorageCpcty_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 25),
    _TmnxDASGCardRemStorageCpcty_Type()
)
tmnxDASGCardRemStorageCpcty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardRemStorageCpcty.setStatus("current")
_TmnxDASGCardRemStorageCpctyL32_Type = Counter32
_TmnxDASGCardRemStorageCpctyL32_Object = MibTableColumn
tmnxDASGCardRemStorageCpctyL32 = _TmnxDASGCardRemStorageCpctyL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 26),
    _TmnxDASGCardRemStorageCpctyL32_Type()
)
tmnxDASGCardRemStorageCpctyL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardRemStorageCpctyL32.setStatus("current")
_TmnxDASGCardRemStorageCpctyH32_Type = Counter32
_TmnxDASGCardRemStorageCpctyH32_Object = MibTableColumn
tmnxDASGCardRemStorageCpctyH32 = _TmnxDASGCardRemStorageCpctyH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 27),
    _TmnxDASGCardRemStorageCpctyH32_Type()
)
tmnxDASGCardRemStorageCpctyH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardRemStorageCpctyH32.setStatus("current")
_TmnxDASGCardNumberOfAssets_Type = Gauge32
_TmnxDASGCardNumberOfAssets_Object = MibTableColumn
tmnxDASGCardNumberOfAssets = _TmnxDASGCardNumberOfAssets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 28),
    _TmnxDASGCardNumberOfAssets_Type()
)
tmnxDASGCardNumberOfAssets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardNumberOfAssets.setStatus("current")
_TmnxDASGCardNumberOfOrigins_Type = Gauge32
_TmnxDASGCardNumberOfOrigins_Object = MibTableColumn
tmnxDASGCardNumberOfOrigins = _TmnxDASGCardNumberOfOrigins_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 29),
    _TmnxDASGCardNumberOfOrigins_Type()
)
tmnxDASGCardNumberOfOrigins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardNumberOfOrigins.setStatus("current")
_TmnxDASGCardNumberOfURIs_Type = Gauge32
_TmnxDASGCardNumberOfURIs_Object = MibTableColumn
tmnxDASGCardNumberOfURIs = _TmnxDASGCardNumberOfURIs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 30),
    _TmnxDASGCardNumberOfURIs_Type()
)
tmnxDASGCardNumberOfURIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardNumberOfURIs.setStatus("current")
_TmnxDASGCardECCBlockCorrections_Type = Gauge32
_TmnxDASGCardECCBlockCorrections_Object = MibTableColumn
tmnxDASGCardECCBlockCorrections = _TmnxDASGCardECCBlockCorrections_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 31),
    _TmnxDASGCardECCBlockCorrections_Type()
)
tmnxDASGCardECCBlockCorrections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardECCBlockCorrections.setStatus("current")
_TmnxDASGCardECCBlockFailures_Type = Gauge32
_TmnxDASGCardECCBlockFailures_Object = MibTableColumn
tmnxDASGCardECCBlockFailures = _TmnxDASGCardECCBlockFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 32),
    _TmnxDASGCardECCBlockFailures_Type()
)
tmnxDASGCardECCBlockFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardECCBlockFailures.setStatus("current")
_TmnxDASGCardPercentBadBlocks_Type = Gauge32
_TmnxDASGCardPercentBadBlocks_Object = MibTableColumn
tmnxDASGCardPercentBadBlocks = _TmnxDASGCardPercentBadBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 33),
    _TmnxDASGCardPercentBadBlocks_Type()
)
tmnxDASGCardPercentBadBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardPercentBadBlocks.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDASGCardPercentBadBlocks.setUnits("hundredths of a percent")
_TmnxDASGCardFPGATotPktsSent_Type = Counter64
_TmnxDASGCardFPGATotPktsSent_Object = MibTableColumn
tmnxDASGCardFPGATotPktsSent = _TmnxDASGCardFPGATotPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 34),
    _TmnxDASGCardFPGATotPktsSent_Type()
)
tmnxDASGCardFPGATotPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotPktsSent.setStatus("current")
_TmnxDASGCardFPGATotPktsSentL32_Type = Counter32
_TmnxDASGCardFPGATotPktsSentL32_Object = MibTableColumn
tmnxDASGCardFPGATotPktsSentL32 = _TmnxDASGCardFPGATotPktsSentL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 35),
    _TmnxDASGCardFPGATotPktsSentL32_Type()
)
tmnxDASGCardFPGATotPktsSentL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotPktsSentL32.setStatus("current")
_TmnxDASGCardFPGATotPktsSentH32_Type = Counter32
_TmnxDASGCardFPGATotPktsSentH32_Object = MibTableColumn
tmnxDASGCardFPGATotPktsSentH32 = _TmnxDASGCardFPGATotPktsSentH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 36),
    _TmnxDASGCardFPGATotPktsSentH32_Type()
)
tmnxDASGCardFPGATotPktsSentH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotPktsSentH32.setStatus("current")
_TmnxDASGCardFPGATotBytesSent_Type = Counter64
_TmnxDASGCardFPGATotBytesSent_Object = MibTableColumn
tmnxDASGCardFPGATotBytesSent = _TmnxDASGCardFPGATotBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 37),
    _TmnxDASGCardFPGATotBytesSent_Type()
)
tmnxDASGCardFPGATotBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotBytesSent.setStatus("current")
_TmnxDASGCardFPGATotBytesSentL32_Type = Counter32
_TmnxDASGCardFPGATotBytesSentL32_Object = MibTableColumn
tmnxDASGCardFPGATotBytesSentL32 = _TmnxDASGCardFPGATotBytesSentL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 38),
    _TmnxDASGCardFPGATotBytesSentL32_Type()
)
tmnxDASGCardFPGATotBytesSentL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotBytesSentL32.setStatus("current")
_TmnxDASGCardFPGATotBytesSentH32_Type = Counter32
_TmnxDASGCardFPGATotBytesSentH32_Object = MibTableColumn
tmnxDASGCardFPGATotBytesSentH32 = _TmnxDASGCardFPGATotBytesSentH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 39),
    _TmnxDASGCardFPGATotBytesSentH32_Type()
)
tmnxDASGCardFPGATotBytesSentH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotBytesSentH32.setStatus("current")
_TmnxDASGCardFPGATotPktsRecd_Type = Counter64
_TmnxDASGCardFPGATotPktsRecd_Object = MibTableColumn
tmnxDASGCardFPGATotPktsRecd = _TmnxDASGCardFPGATotPktsRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 40),
    _TmnxDASGCardFPGATotPktsRecd_Type()
)
tmnxDASGCardFPGATotPktsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotPktsRecd.setStatus("current")
_TmnxDASGCardFPGATotPktsRecdL32_Type = Counter32
_TmnxDASGCardFPGATotPktsRecdL32_Object = MibTableColumn
tmnxDASGCardFPGATotPktsRecdL32 = _TmnxDASGCardFPGATotPktsRecdL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 41),
    _TmnxDASGCardFPGATotPktsRecdL32_Type()
)
tmnxDASGCardFPGATotPktsRecdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotPktsRecdL32.setStatus("current")
_TmnxDASGCardFPGATotPktsRecdH32_Type = Counter32
_TmnxDASGCardFPGATotPktsRecdH32_Object = MibTableColumn
tmnxDASGCardFPGATotPktsRecdH32 = _TmnxDASGCardFPGATotPktsRecdH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 42),
    _TmnxDASGCardFPGATotPktsRecdH32_Type()
)
tmnxDASGCardFPGATotPktsRecdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotPktsRecdH32.setStatus("current")
_TmnxDASGCardFPGATotBytesRecd_Type = Counter64
_TmnxDASGCardFPGATotBytesRecd_Object = MibTableColumn
tmnxDASGCardFPGATotBytesRecd = _TmnxDASGCardFPGATotBytesRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 43),
    _TmnxDASGCardFPGATotBytesRecd_Type()
)
tmnxDASGCardFPGATotBytesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotBytesRecd.setStatus("current")
_TmnxDASGCardFPGATotBytesRecdL32_Type = Counter32
_TmnxDASGCardFPGATotBytesRecdL32_Object = MibTableColumn
tmnxDASGCardFPGATotBytesRecdL32 = _TmnxDASGCardFPGATotBytesRecdL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 44),
    _TmnxDASGCardFPGATotBytesRecdL32_Type()
)
tmnxDASGCardFPGATotBytesRecdL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotBytesRecdL32.setStatus("current")
_TmnxDASGCardFPGATotBytesRecdH32_Type = Counter32
_TmnxDASGCardFPGATotBytesRecdH32_Object = MibTableColumn
tmnxDASGCardFPGATotBytesRecdH32 = _TmnxDASGCardFPGATotBytesRecdH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 45),
    _TmnxDASGCardFPGATotBytesRecdH32_Type()
)
tmnxDASGCardFPGATotBytesRecdH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGATotBytesRecdH32.setStatus("current")
_TmnxDASGCardFPGAUnderflowErrors_Type = Gauge32
_TmnxDASGCardFPGAUnderflowErrors_Object = MibTableColumn
tmnxDASGCardFPGAUnderflowErrors = _TmnxDASGCardFPGAUnderflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 46),
    _TmnxDASGCardFPGAUnderflowErrors_Type()
)
tmnxDASGCardFPGAUnderflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGAUnderflowErrors.setStatus("current")
_TmnxDASGCardFPGAOverflowErrors_Type = Gauge32
_TmnxDASGCardFPGAOverflowErrors_Object = MibTableColumn
tmnxDASGCardFPGAOverflowErrors = _TmnxDASGCardFPGAOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 17, 1, 47),
    _TmnxDASGCardFPGAOverflowErrors_Type()
)
tmnxDASGCardFPGAOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDASGCardFPGAOverflowErrors.setStatus("current")
_TmnxDADCIntfTable_Object = MibTable
tmnxDADCIntfTable = _TmnxDADCIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxDADCIntfTable.setStatus("current")
_TmnxDADCIntfEntry_Object = MibTableRow
tmnxDADCIntfEntry = _TmnxDADCIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1)
)
tmnxDADCIntfEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
    (0, "TIMETRA-DA-MIB", "tmnxDADCIntfServerIndex"),
    (0, "TIMETRA-DA-MIB", "tmnxDADCIntfType"),
    (0, "TIMETRA-DA-MIB", "tmnxDADCIntfIPAddrType"),
    (0, "TIMETRA-DA-MIB", "tmnxDADCIntfIPAddress"),
)
if mibBuilder.loadTexts:
    tmnxDADCIntfEntry.setStatus("current")
_TmnxDADCIntfServerIndex_Type = Gauge32
_TmnxDADCIntfServerIndex_Object = MibTableColumn
tmnxDADCIntfServerIndex = _TmnxDADCIntfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 1),
    _TmnxDADCIntfServerIndex_Type()
)
tmnxDADCIntfServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDADCIntfServerIndex.setStatus("current")


class _TmnxDADCIntfType_Type(Integer32):
    """Custom type tmnxDADCIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auth", 6),
          ("config", 2),
          ("event", 7),
          ("health", 3),
          ("job", 4),
          ("metadata", 5),
          ("service", 1))
    )


_TmnxDADCIntfType_Type.__name__ = "Integer32"
_TmnxDADCIntfType_Object = MibTableColumn
tmnxDADCIntfType = _TmnxDADCIntfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 2),
    _TmnxDADCIntfType_Type()
)
tmnxDADCIntfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDADCIntfType.setStatus("current")
_TmnxDADCIntfIPAddrType_Type = InetAddressType
_TmnxDADCIntfIPAddrType_Object = MibTableColumn
tmnxDADCIntfIPAddrType = _TmnxDADCIntfIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 3),
    _TmnxDADCIntfIPAddrType_Type()
)
tmnxDADCIntfIPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDADCIntfIPAddrType.setStatus("current")


class _TmnxDADCIntfIPAddress_Type(InetAddress):
    """Custom type tmnxDADCIntfIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDADCIntfIPAddress_Type.__name__ = "InetAddress"
_TmnxDADCIntfIPAddress_Object = MibTableColumn
tmnxDADCIntfIPAddress = _TmnxDADCIntfIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 4),
    _TmnxDADCIntfIPAddress_Type()
)
tmnxDADCIntfIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDADCIntfIPAddress.setStatus("current")
_TmnxDADCIntfFQDNType_Type = InetAddressType
_TmnxDADCIntfFQDNType_Object = MibTableColumn
tmnxDADCIntfFQDNType = _TmnxDADCIntfFQDNType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 5),
    _TmnxDADCIntfFQDNType_Type()
)
tmnxDADCIntfFQDNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfFQDNType.setStatus("current")


class _TmnxDADCIntfFQDN_Type(InetAddress):
    """Custom type tmnxDADCIntfFQDN based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TmnxDADCIntfFQDN_Type.__name__ = "InetAddress"
_TmnxDADCIntfFQDN_Object = MibTableColumn
tmnxDADCIntfFQDN = _TmnxDADCIntfFQDN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 6),
    _TmnxDADCIntfFQDN_Type()
)
tmnxDADCIntfFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfFQDN.setStatus("current")
_TmnxDADCIntfSrcPort_Type = InetPortNumber
_TmnxDADCIntfSrcPort_Object = MibTableColumn
tmnxDADCIntfSrcPort = _TmnxDADCIntfSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 7),
    _TmnxDADCIntfSrcPort_Type()
)
tmnxDADCIntfSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfSrcPort.setStatus("current")
_TmnxDADCIntfDestPort_Type = InetPortNumber
_TmnxDADCIntfDestPort_Object = MibTableColumn
tmnxDADCIntfDestPort = _TmnxDADCIntfDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 8),
    _TmnxDADCIntfDestPort_Type()
)
tmnxDADCIntfDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfDestPort.setStatus("current")
_TmnxDADCIntfOperState_Type = TmnxOperState
_TmnxDADCIntfOperState_Object = MibTableColumn
tmnxDADCIntfOperState = _TmnxDADCIntfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 9),
    _TmnxDADCIntfOperState_Type()
)
tmnxDADCIntfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfOperState.setStatus("current")
_TmnxDADCIntfIPUpTime_Type = Gauge32
_TmnxDADCIntfIPUpTime_Object = MibTableColumn
tmnxDADCIntfIPUpTime = _TmnxDADCIntfIPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 10),
    _TmnxDADCIntfIPUpTime_Type()
)
tmnxDADCIntfIPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfIPUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDADCIntfIPUpTime.setUnits("seconds")
_TmnxDADCIntfIdleTime_Type = Gauge32
_TmnxDADCIntfIdleTime_Object = MibTableColumn
tmnxDADCIntfIdleTime = _TmnxDADCIntfIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 11),
    _TmnxDADCIntfIdleTime_Type()
)
tmnxDADCIntfIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDADCIntfIdleTime.setUnits("seconds")
_TmnxDADCIntfRetry_Type = Gauge32
_TmnxDADCIntfRetry_Object = MibTableColumn
tmnxDADCIntfRetry = _TmnxDADCIntfRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 12),
    _TmnxDADCIntfRetry_Type()
)
tmnxDADCIntfRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfRetry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDADCIntfRetry.setUnits("seconds")


class _TmnxDADCIntfTimeToLive_Type(Gauge32):
    """Custom type tmnxDADCIntfTimeToLive based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxDADCIntfTimeToLive_Type.__name__ = "Gauge32"
_TmnxDADCIntfTimeToLive_Object = MibTableColumn
tmnxDADCIntfTimeToLive = _TmnxDADCIntfTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 13),
    _TmnxDADCIntfTimeToLive_Type()
)
tmnxDADCIntfTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfTimeToLive.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDADCIntfTimeToLive.setUnits("seconds")
_TmnxDADCIntfEtag_Type = TLNamedItemOrEmpty
_TmnxDADCIntfEtag_Object = MibTableColumn
tmnxDADCIntfEtag = _TmnxDADCIntfEtag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 14),
    _TmnxDADCIntfEtag_Type()
)
tmnxDADCIntfEtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfEtag.setStatus("current")
_TmnxDADCIntfInterval_Type = Gauge32
_TmnxDADCIntfInterval_Object = MibTableColumn
tmnxDADCIntfInterval = _TmnxDADCIntfInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 15),
    _TmnxDADCIntfInterval_Type()
)
tmnxDADCIntfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfInterval.setStatus("current")
_TmnxDADCIntfPriority_Type = Gauge32
_TmnxDADCIntfPriority_Object = MibTableColumn
tmnxDADCIntfPriority = _TmnxDADCIntfPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 16),
    _TmnxDADCIntfPriority_Type()
)
tmnxDADCIntfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfPriority.setStatus("current")
_TmnxDADCIntfWeight_Type = Gauge32
_TmnxDADCIntfWeight_Object = MibTableColumn
tmnxDADCIntfWeight = _TmnxDADCIntfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 17),
    _TmnxDADCIntfWeight_Type()
)
tmnxDADCIntfWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfWeight.setStatus("current")
_TmnxDADCIntfAttemptedSessStups_Type = Counter32
_TmnxDADCIntfAttemptedSessStups_Object = MibTableColumn
tmnxDADCIntfAttemptedSessStups = _TmnxDADCIntfAttemptedSessStups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 18),
    _TmnxDADCIntfAttemptedSessStups_Type()
)
tmnxDADCIntfAttemptedSessStups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfAttemptedSessStups.setStatus("current")
_TmnxDADCIntfFailedSessStups_Type = Counter32
_TmnxDADCIntfFailedSessStups_Object = MibTableColumn
tmnxDADCIntfFailedSessStups = _TmnxDADCIntfFailedSessStups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 19),
    _TmnxDADCIntfFailedSessStups_Type()
)
tmnxDADCIntfFailedSessStups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfFailedSessStups.setStatus("current")
_TmnxDADCIntfPingReqTxCount_Type = Counter32
_TmnxDADCIntfPingReqTxCount_Object = MibTableColumn
tmnxDADCIntfPingReqTxCount = _TmnxDADCIntfPingReqTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 20),
    _TmnxDADCIntfPingReqTxCount_Type()
)
tmnxDADCIntfPingReqTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfPingReqTxCount.setStatus("current")
_TmnxDADCIntfPingResRxCount_Type = Counter32
_TmnxDADCIntfPingResRxCount_Object = MibTableColumn
tmnxDADCIntfPingResRxCount = _TmnxDADCIntfPingResRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 21),
    _TmnxDADCIntfPingResRxCount_Type()
)
tmnxDADCIntfPingResRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfPingResRxCount.setStatus("current")
_TmnxDADCIntfReqMsgTxCount_Type = Counter64
_TmnxDADCIntfReqMsgTxCount_Object = MibTableColumn
tmnxDADCIntfReqMsgTxCount = _TmnxDADCIntfReqMsgTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 22),
    _TmnxDADCIntfReqMsgTxCount_Type()
)
tmnxDADCIntfReqMsgTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfReqMsgTxCount.setStatus("current")
_TmnxDADCIntfReqMsgTxCountL32_Type = Counter32
_TmnxDADCIntfReqMsgTxCountL32_Object = MibTableColumn
tmnxDADCIntfReqMsgTxCountL32 = _TmnxDADCIntfReqMsgTxCountL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 23),
    _TmnxDADCIntfReqMsgTxCountL32_Type()
)
tmnxDADCIntfReqMsgTxCountL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfReqMsgTxCountL32.setStatus("current")
_TmnxDADCIntfReqMsgTxCountH32_Type = Counter32
_TmnxDADCIntfReqMsgTxCountH32_Object = MibTableColumn
tmnxDADCIntfReqMsgTxCountH32 = _TmnxDADCIntfReqMsgTxCountH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 24),
    _TmnxDADCIntfReqMsgTxCountH32_Type()
)
tmnxDADCIntfReqMsgTxCountH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfReqMsgTxCountH32.setStatus("current")
_TmnxDADCIntfResMsgRxCount_Type = Counter64
_TmnxDADCIntfResMsgRxCount_Object = MibTableColumn
tmnxDADCIntfResMsgRxCount = _TmnxDADCIntfResMsgRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 25),
    _TmnxDADCIntfResMsgRxCount_Type()
)
tmnxDADCIntfResMsgRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfResMsgRxCount.setStatus("current")
_TmnxDADCIntfResMsgRxCountL32_Type = Counter32
_TmnxDADCIntfResMsgRxCountL32_Object = MibTableColumn
tmnxDADCIntfResMsgRxCountL32 = _TmnxDADCIntfResMsgRxCountL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 26),
    _TmnxDADCIntfResMsgRxCountL32_Type()
)
tmnxDADCIntfResMsgRxCountL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfResMsgRxCountL32.setStatus("current")
_TmnxDADCIntfResMsgRxCountH32_Type = Counter32
_TmnxDADCIntfResMsgRxCountH32_Object = MibTableColumn
tmnxDADCIntfResMsgRxCountH32 = _TmnxDADCIntfResMsgRxCountH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 27),
    _TmnxDADCIntfResMsgRxCountH32_Type()
)
tmnxDADCIntfResMsgRxCountH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfResMsgRxCountH32.setStatus("current")
_TmnxDADCIntfDecodeErrors_Type = Counter32
_TmnxDADCIntfDecodeErrors_Object = MibTableColumn
tmnxDADCIntfDecodeErrors = _TmnxDADCIntfDecodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 28),
    _TmnxDADCIntfDecodeErrors_Type()
)
tmnxDADCIntfDecodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfDecodeErrors.setStatus("current")
_TmnxDADCIntfConnectionBounce_Type = Counter32
_TmnxDADCIntfConnectionBounce_Object = MibTableColumn
tmnxDADCIntfConnectionBounce = _TmnxDADCIntfConnectionBounce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 29),
    _TmnxDADCIntfConnectionBounce_Type()
)
tmnxDADCIntfConnectionBounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfConnectionBounce.setStatus("current")
_TmnxDADCIntfRemoteClose_Type = Counter32
_TmnxDADCIntfRemoteClose_Object = MibTableColumn
tmnxDADCIntfRemoteClose = _TmnxDADCIntfRemoteClose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 30),
    _TmnxDADCIntfRemoteClose_Type()
)
tmnxDADCIntfRemoteClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfRemoteClose.setStatus("current")
_TmnxDADCIntfNoResponse_Type = Counter32
_TmnxDADCIntfNoResponse_Object = MibTableColumn
tmnxDADCIntfNoResponse = _TmnxDADCIntfNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 18, 1, 31),
    _TmnxDADCIntfNoResponse_Type()
)
tmnxDADCIntfNoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDADCIntfNoResponse.setStatus("current")
_TmnxDAGrpOrigSvrTable_Object = MibTable
tmnxDAGrpOrigSvrTable = _TmnxDAGrpOrigSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrTable.setStatus("current")
_TmnxDAGrpOrigSvrEntry_Object = MibTableRow
tmnxDAGrpOrigSvrEntry = _TmnxDAGrpOrigSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1)
)
tmnxDAGrpOrigSvrEntry.setIndexNames(
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpName"),
    (0, "TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrName"),
)
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrEntry.setStatus("current")


class _TmnxDAGrpOrigSvrName_Type(DisplayString):
    """Custom type tmnxDAGrpOrigSvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 94),
    )


_TmnxDAGrpOrigSvrName_Type.__name__ = "DisplayString"
_TmnxDAGrpOrigSvrName_Object = MibTableColumn
tmnxDAGrpOrigSvrName = _TmnxDAGrpOrigSvrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 1),
    _TmnxDAGrpOrigSvrName_Type()
)
tmnxDAGrpOrigSvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrName.setStatus("current")
_TmnxDAGrpOrigSvrIPAddrType_Type = InetAddressType
_TmnxDAGrpOrigSvrIPAddrType_Object = MibTableColumn
tmnxDAGrpOrigSvrIPAddrType = _TmnxDAGrpOrigSvrIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 2),
    _TmnxDAGrpOrigSvrIPAddrType_Type()
)
tmnxDAGrpOrigSvrIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrIPAddrType.setStatus("current")


class _TmnxDAGrpOrigSvrIPAddress_Type(InetAddress):
    """Custom type tmnxDAGrpOrigSvrIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxDAGrpOrigSvrIPAddress_Type.__name__ = "InetAddress"
_TmnxDAGrpOrigSvrIPAddress_Object = MibTableColumn
tmnxDAGrpOrigSvrIPAddress = _TmnxDAGrpOrigSvrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 3),
    _TmnxDAGrpOrigSvrIPAddress_Type()
)
tmnxDAGrpOrigSvrIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrIPAddress.setStatus("current")
_TmnxDAGrpOrigSvrNumObjDelvred_Type = Counter64
_TmnxDAGrpOrigSvrNumObjDelvred_Object = MibTableColumn
tmnxDAGrpOrigSvrNumObjDelvred = _TmnxDAGrpOrigSvrNumObjDelvred_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 4),
    _TmnxDAGrpOrigSvrNumObjDelvred_Type()
)
tmnxDAGrpOrigSvrNumObjDelvred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrNumObjDelvred.setStatus("current")
_TmnxDAGrpOrigSvrNumObjDelvredL32_Type = Counter32
_TmnxDAGrpOrigSvrNumObjDelvredL32_Object = MibTableColumn
tmnxDAGrpOrigSvrNumObjDelvredL32 = _TmnxDAGrpOrigSvrNumObjDelvredL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 5),
    _TmnxDAGrpOrigSvrNumObjDelvredL32_Type()
)
tmnxDAGrpOrigSvrNumObjDelvredL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrNumObjDelvredL32.setStatus("current")
_TmnxDAGrpOrigSvrNumObjDelvredH32_Type = Counter32
_TmnxDAGrpOrigSvrNumObjDelvredH32_Object = MibTableColumn
tmnxDAGrpOrigSvrNumObjDelvredH32 = _TmnxDAGrpOrigSvrNumObjDelvredH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 6),
    _TmnxDAGrpOrigSvrNumObjDelvredH32_Type()
)
tmnxDAGrpOrigSvrNumObjDelvredH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrNumObjDelvredH32.setStatus("current")
_TmnxDAGrpOrigSvrNumObjFailed_Type = Counter64
_TmnxDAGrpOrigSvrNumObjFailed_Object = MibTableColumn
tmnxDAGrpOrigSvrNumObjFailed = _TmnxDAGrpOrigSvrNumObjFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 7),
    _TmnxDAGrpOrigSvrNumObjFailed_Type()
)
tmnxDAGrpOrigSvrNumObjFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrNumObjFailed.setStatus("current")
_TmnxDAGrpOrigSvrNumObjFailedL32_Type = Counter32
_TmnxDAGrpOrigSvrNumObjFailedL32_Object = MibTableColumn
tmnxDAGrpOrigSvrNumObjFailedL32 = _TmnxDAGrpOrigSvrNumObjFailedL32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 8),
    _TmnxDAGrpOrigSvrNumObjFailedL32_Type()
)
tmnxDAGrpOrigSvrNumObjFailedL32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrNumObjFailedL32.setStatus("current")
_TmnxDAGrpOrigSvrNumObjFailedH32_Type = Counter32
_TmnxDAGrpOrigSvrNumObjFailedH32_Object = MibTableColumn
tmnxDAGrpOrigSvrNumObjFailedH32 = _TmnxDAGrpOrigSvrNumObjFailedH32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 9),
    _TmnxDAGrpOrigSvrNumObjFailedH32_Type()
)
tmnxDAGrpOrigSvrNumObjFailedH32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrNumObjFailedH32.setStatus("current")
_TmnxDAGrpOrigSvrNumCurTCPConn_Type = Counter32
_TmnxDAGrpOrigSvrNumCurTCPConn_Object = MibTableColumn
tmnxDAGrpOrigSvrNumCurTCPConn = _TmnxDAGrpOrigSvrNumCurTCPConn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 82, 1, 19, 1, 10),
    _TmnxDAGrpOrigSvrNumCurTCPConn_Type()
)
tmnxDAGrpOrigSvrNumCurTCPConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDAGrpOrigSvrNumCurTCPConn.setStatus("current")
_TmnxDANotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDANotifyPrefix = _TmnxDANotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 82)
)
_TmnxDANotifications_ObjectIdentity = ObjectIdentity
tmnxDANotifications = _TmnxDANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 82, 0)
)
tmnxDAGrpEntry.registerAugmentions(
    ("TIMETRA-DA-MIB",
     "tmnxDAHttpEntry")
)
tmnxDAHttpEntry.setIndexNames(*tmnxDAGrpEntry.getIndexNames())

# Managed Objects groups

tmnxDAV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 82, 2, 1)
)
tmnxDAV10v0Group.setObjects(
      *(("TIMETRA-DA-MIB", "tmnxDASvrGrpTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDASvrGrpRowStatus"),
        ("TIMETRA-DA-MIB", "tmnxDASvrGrpLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDASvrGrpCardSlotNumber"),
        ("TIMETRA-DA-MIB", "tmnxDASvrGrpAdminState"),
        ("TIMETRA-DA-MIB", "tmnxDASvrGrpOperState"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpRowStatus"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpServerGroupIndex"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpAdminState"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDescription"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDnsClientIsmLinkName"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAuthCache"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAdminState"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCIsmLinkName"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCBootStrapPort"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCConnRetryTimer"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCIdleTimeout"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpBytesFromCache"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpBytesFromCacheL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpBytesFromCacheH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpBytesNotFromCache"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpBytesNotFromCacheL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpBytesNotFromCacheH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectsFromCache"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectsFromCacheL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectsFromCacheH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectsNotFromCache"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectsNotFromCacheL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectsNotFromCacheH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectByteCount"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectByteCountL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpObjectByteCountH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpNumberOfOrigins"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpNumberOfOriginsL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpNumberOfOriginsH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAuthCacheHit"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAuthCacheHitL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAuthCacheHitH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAuthCacheMiss"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAuthCacheMissL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAuthCacheMissH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCDeniedAuth"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCDeniedAuthL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCDeniedAuthH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCMinRTTPerPeer"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCAvgRTTPerPeer"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDCMaxRTTPerPeer"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDnsSvrTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDnsSvrRowStatus"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpDnsSvrLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDADCBtStSvrTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDADCBtStSvrRowStatus"),
        ("TIMETRA-DA-MIB", "tmnxDADCBtStSvrLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDADCBtStSvrAddrType"),
        ("TIMETRA-DA-MIB", "tmnxDADCBtStSvrAddress"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerAdminState"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerOperState"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerIdleTimeout"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerViaString"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerStrBWInUse"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerStrBWInUseL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerStrBWInUseH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerXferInProg"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerXferCompleted"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerXferCompletedL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerXferCompletedH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerXferTimeouts"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerXferFailed"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerValidRequests"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerValidRequestsL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerValidRequestsH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerInvalidRequests"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerMethodNotSuppted"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServerHostNotSuppted"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer1XXCountSent"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer1XXCountSentL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer1XXCountSentH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer2XXCountSent"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer2XXCountSentL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer2XXCountSentH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer3XXCountSent"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer3XXCountSentL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer3XXCountSentH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer4XXCountSent"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer4XXCountSentL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer4XXCountSentH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer5XXCountSent"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer5XXCountSentL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpServer5XXCountSentH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestAdminState"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestOperState"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestIsmLinkName"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestIdleTimeout"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestXferInProg"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestXferCompleted"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestXferCompletedL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestXferCompletedH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestXferTimeouts"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngestXferFailed"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest1XXCountRecd"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest1XXCountRecdL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest1XXCountRecdH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest2XXCountRecd"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest2XXCountRecdL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest2XXCountRecdH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest3XXCountRecd"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest3XXCountRecdL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest3XXCountRecdH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest4XXCountRecd"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest4XXCountRecdL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest4XXCountRecdH32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest5XXCountRecd"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest5XXCountRecdL32"),
        ("TIMETRA-DA-MIB", "tmnxDAHttpIngest5XXCountRecdH32"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkRowStatus"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkAddrType"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkAddress"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkAddrPrefixLength"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkDescription"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkHttpd"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkHttpListenPort"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkIpMtu"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkQtag"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkMacAddress"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkAdminState"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkOperState"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkBindings"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkArpTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkArpRowStatus"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkArpLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkArpMacAddr"),
        ("TIMETRA-DA-MIB", "tmnxDAIsmLinkArpType"),
        ("TIMETRA-DA-MIB", "tmnxDAStRouteTableLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAStRouteRowStatus"),
        ("TIMETRA-DA-MIB", "tmnxDAStRouteLastChanged"),
        ("TIMETRA-DA-MIB", "tmnxDAStRouteMetric"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardUpTime"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTotNumTCPConn"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPConnEstab"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPConnEstabL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPConnEstabH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPConnClosed"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPConnClosedL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPConnClosedH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPRetries"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPRetriesL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPRetriesH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPAckTimeOut"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPAckTimeOutL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPAckTimeOutH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPFarEndClosed"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPFarEndClosedL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPFarEndClosedH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPLocalEndClosed"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPLocalEndClosedL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardTCPLocalEndClosedH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardUsedStorageCpcty"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardUsedStorageCpctyL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardUsedStorageCpctyH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardRemStorageCpcty"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardRemStorageCpctyL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardRemStorageCpctyH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardNumberOfAssets"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardNumberOfOrigins"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardNumberOfURIs"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardECCBlockCorrections"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardECCBlockFailures"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardPercentBadBlocks"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotPktsSent"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotPktsSentL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotPktsSentH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotBytesSent"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotBytesSentL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotBytesSentH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotPktsRecd"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotPktsRecdL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotPktsRecdH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotBytesRecd"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotBytesRecdL32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGATotBytesRecdH32"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGAUnderflowErrors"),
        ("TIMETRA-DA-MIB", "tmnxDASGCardFPGAOverflowErrors"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfFQDNType"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfFQDN"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfSrcPort"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfDestPort"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfOperState"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfIPUpTime"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfIdleTime"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfRetry"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfTimeToLive"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfEtag"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfInterval"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfPriority"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfWeight"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfAttemptedSessStups"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfFailedSessStups"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfPingReqTxCount"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfPingResRxCount"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfReqMsgTxCount"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfReqMsgTxCountL32"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfReqMsgTxCountH32"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfResMsgRxCount"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfResMsgRxCountL32"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfResMsgRxCountH32"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfDecodeErrors"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfConnectionBounce"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfRemoteClose"),
        ("TIMETRA-DA-MIB", "tmnxDADCIntfNoResponse"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrIPAddrType"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrIPAddress"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrNumObjDelvred"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrNumObjDelvredL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrNumObjDelvredH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrNumObjFailed"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrNumObjFailedL32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrNumObjFailedH32"),
        ("TIMETRA-DA-MIB", "tmnxDAGrpOrigSvrNumCurTCPConn"))
)
if mibBuilder.loadTexts:
    tmnxDAV10v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxDAV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 82, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDAV10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DA-MIB",
    **{"timetraDAMIBModule": timetraDAMIBModule,
       "tmnxDAConformance": tmnxDAConformance,
       "tmnxDACompliances": tmnxDACompliances,
       "tmnxDAV10v0Compliance": tmnxDAV10v0Compliance,
       "tmnxDAGroups": tmnxDAGroups,
       "tmnxDAV10v0Group": tmnxDAV10v0Group,
       "tmnxDA": tmnxDA,
       "tmnxDAObjs": tmnxDAObjs,
       "tmnxDASvrGrpTableLastChanged": tmnxDASvrGrpTableLastChanged,
       "tmnxDASvrGrpTable": tmnxDASvrGrpTable,
       "tmnxDASvrGrpEntry": tmnxDASvrGrpEntry,
       "tmnxDASvrGrpIndex": tmnxDASvrGrpIndex,
       "tmnxDASvrGrpRowStatus": tmnxDASvrGrpRowStatus,
       "tmnxDASvrGrpLastChanged": tmnxDASvrGrpLastChanged,
       "tmnxDASvrGrpCardSlotNumber": tmnxDASvrGrpCardSlotNumber,
       "tmnxDASvrGrpAdminState": tmnxDASvrGrpAdminState,
       "tmnxDASvrGrpOperState": tmnxDASvrGrpOperState,
       "tmnxDAGrpTableLastChanged": tmnxDAGrpTableLastChanged,
       "tmnxDAGrpTable": tmnxDAGrpTable,
       "tmnxDAGrpEntry": tmnxDAGrpEntry,
       "tmnxDAGrpName": tmnxDAGrpName,
       "tmnxDAGrpRowStatus": tmnxDAGrpRowStatus,
       "tmnxDAGrpLastChanged": tmnxDAGrpLastChanged,
       "tmnxDAGrpServerGroupIndex": tmnxDAGrpServerGroupIndex,
       "tmnxDAGrpAdminState": tmnxDAGrpAdminState,
       "tmnxDAGrpDescription": tmnxDAGrpDescription,
       "tmnxDAGrpDnsClientIsmLinkName": tmnxDAGrpDnsClientIsmLinkName,
       "tmnxDAGrpDCAuthCache": tmnxDAGrpDCAuthCache,
       "tmnxDAGrpDCAdminState": tmnxDAGrpDCAdminState,
       "tmnxDAGrpDCIsmLinkName": tmnxDAGrpDCIsmLinkName,
       "tmnxDAGrpDCBootStrapPort": tmnxDAGrpDCBootStrapPort,
       "tmnxDAGrpDCConnRetryTimer": tmnxDAGrpDCConnRetryTimer,
       "tmnxDAGrpDCIdleTimeout": tmnxDAGrpDCIdleTimeout,
       "tmnxDAGrpBytesFromCache": tmnxDAGrpBytesFromCache,
       "tmnxDAGrpBytesFromCacheL32": tmnxDAGrpBytesFromCacheL32,
       "tmnxDAGrpBytesFromCacheH32": tmnxDAGrpBytesFromCacheH32,
       "tmnxDAGrpBytesNotFromCache": tmnxDAGrpBytesNotFromCache,
       "tmnxDAGrpBytesNotFromCacheL32": tmnxDAGrpBytesNotFromCacheL32,
       "tmnxDAGrpBytesNotFromCacheH32": tmnxDAGrpBytesNotFromCacheH32,
       "tmnxDAGrpObjectsFromCache": tmnxDAGrpObjectsFromCache,
       "tmnxDAGrpObjectsFromCacheL32": tmnxDAGrpObjectsFromCacheL32,
       "tmnxDAGrpObjectsFromCacheH32": tmnxDAGrpObjectsFromCacheH32,
       "tmnxDAGrpObjectsNotFromCache": tmnxDAGrpObjectsNotFromCache,
       "tmnxDAGrpObjectsNotFromCacheL32": tmnxDAGrpObjectsNotFromCacheL32,
       "tmnxDAGrpObjectsNotFromCacheH32": tmnxDAGrpObjectsNotFromCacheH32,
       "tmnxDAGrpObjectByteCount": tmnxDAGrpObjectByteCount,
       "tmnxDAGrpObjectByteCountL32": tmnxDAGrpObjectByteCountL32,
       "tmnxDAGrpObjectByteCountH32": tmnxDAGrpObjectByteCountH32,
       "tmnxDAGrpNumberOfOrigins": tmnxDAGrpNumberOfOrigins,
       "tmnxDAGrpNumberOfOriginsL32": tmnxDAGrpNumberOfOriginsL32,
       "tmnxDAGrpNumberOfOriginsH32": tmnxDAGrpNumberOfOriginsH32,
       "tmnxDAGrpDCAuthCacheHit": tmnxDAGrpDCAuthCacheHit,
       "tmnxDAGrpDCAuthCacheHitL32": tmnxDAGrpDCAuthCacheHitL32,
       "tmnxDAGrpDCAuthCacheHitH32": tmnxDAGrpDCAuthCacheHitH32,
       "tmnxDAGrpDCAuthCacheMiss": tmnxDAGrpDCAuthCacheMiss,
       "tmnxDAGrpDCAuthCacheMissL32": tmnxDAGrpDCAuthCacheMissL32,
       "tmnxDAGrpDCAuthCacheMissH32": tmnxDAGrpDCAuthCacheMissH32,
       "tmnxDAGrpDCDeniedAuth": tmnxDAGrpDCDeniedAuth,
       "tmnxDAGrpDCDeniedAuthL32": tmnxDAGrpDCDeniedAuthL32,
       "tmnxDAGrpDCDeniedAuthH32": tmnxDAGrpDCDeniedAuthH32,
       "tmnxDAGrpDCMinRTTPerPeer": tmnxDAGrpDCMinRTTPerPeer,
       "tmnxDAGrpDCAvgRTTPerPeer": tmnxDAGrpDCAvgRTTPerPeer,
       "tmnxDAGrpDCMaxRTTPerPeer": tmnxDAGrpDCMaxRTTPerPeer,
       "tmnxDAGrpDnsSvrTableLastChanged": tmnxDAGrpDnsSvrTableLastChanged,
       "tmnxDAGrpDnsSvrTable": tmnxDAGrpDnsSvrTable,
       "tmnxDAGrpDnsSvrEntry": tmnxDAGrpDnsSvrEntry,
       "tmnxDAGrpDnsSvrAddrTyp": tmnxDAGrpDnsSvrAddrTyp,
       "tmnxDAGrpDnsSvrAddress": tmnxDAGrpDnsSvrAddress,
       "tmnxDAGrpDnsSvrRowStatus": tmnxDAGrpDnsSvrRowStatus,
       "tmnxDAGrpDnsSvrLastChanged": tmnxDAGrpDnsSvrLastChanged,
       "tmnxDADCBtStSvrTableLastChanged": tmnxDADCBtStSvrTableLastChanged,
       "tmnxDADCBtStSvrTable": tmnxDADCBtStSvrTable,
       "tmnxDADCBtStSvrEntry": tmnxDADCBtStSvrEntry,
       "tmnxDADCBtStSvrIndex": tmnxDADCBtStSvrIndex,
       "tmnxDADCBtStSvrRowStatus": tmnxDADCBtStSvrRowStatus,
       "tmnxDADCBtStSvrLastChanged": tmnxDADCBtStSvrLastChanged,
       "tmnxDADCBtStSvrAddrType": tmnxDADCBtStSvrAddrType,
       "tmnxDADCBtStSvrAddress": tmnxDADCBtStSvrAddress,
       "tmnxDAHttpTableLastChanged": tmnxDAHttpTableLastChanged,
       "tmnxDAHttpTable": tmnxDAHttpTable,
       "tmnxDAHttpEntry": tmnxDAHttpEntry,
       "tmnxDAHttpLastChanged": tmnxDAHttpLastChanged,
       "tmnxDAHttpServerAdminState": tmnxDAHttpServerAdminState,
       "tmnxDAHttpServerOperState": tmnxDAHttpServerOperState,
       "tmnxDAHttpServerIdleTimeout": tmnxDAHttpServerIdleTimeout,
       "tmnxDAHttpServerViaString": tmnxDAHttpServerViaString,
       "tmnxDAHttpServerStrBWInUse": tmnxDAHttpServerStrBWInUse,
       "tmnxDAHttpServerStrBWInUseL32": tmnxDAHttpServerStrBWInUseL32,
       "tmnxDAHttpServerStrBWInUseH32": tmnxDAHttpServerStrBWInUseH32,
       "tmnxDAHttpServerXferInProg": tmnxDAHttpServerXferInProg,
       "tmnxDAHttpServerXferCompleted": tmnxDAHttpServerXferCompleted,
       "tmnxDAHttpServerXferCompletedL32": tmnxDAHttpServerXferCompletedL32,
       "tmnxDAHttpServerXferCompletedH32": tmnxDAHttpServerXferCompletedH32,
       "tmnxDAHttpServerXferTimeouts": tmnxDAHttpServerXferTimeouts,
       "tmnxDAHttpServerXferFailed": tmnxDAHttpServerXferFailed,
       "tmnxDAHttpServerValidRequests": tmnxDAHttpServerValidRequests,
       "tmnxDAHttpServerValidRequestsL32": tmnxDAHttpServerValidRequestsL32,
       "tmnxDAHttpServerValidRequestsH32": tmnxDAHttpServerValidRequestsH32,
       "tmnxDAHttpServerInvalidRequests": tmnxDAHttpServerInvalidRequests,
       "tmnxDAHttpServerMethodNotSuppted": tmnxDAHttpServerMethodNotSuppted,
       "tmnxDAHttpServerHostNotSuppted": tmnxDAHttpServerHostNotSuppted,
       "tmnxDAHttpServer1XXCountSent": tmnxDAHttpServer1XXCountSent,
       "tmnxDAHttpServer1XXCountSentL32": tmnxDAHttpServer1XXCountSentL32,
       "tmnxDAHttpServer1XXCountSentH32": tmnxDAHttpServer1XXCountSentH32,
       "tmnxDAHttpServer2XXCountSent": tmnxDAHttpServer2XXCountSent,
       "tmnxDAHttpServer2XXCountSentL32": tmnxDAHttpServer2XXCountSentL32,
       "tmnxDAHttpServer2XXCountSentH32": tmnxDAHttpServer2XXCountSentH32,
       "tmnxDAHttpServer3XXCountSent": tmnxDAHttpServer3XXCountSent,
       "tmnxDAHttpServer3XXCountSentL32": tmnxDAHttpServer3XXCountSentL32,
       "tmnxDAHttpServer3XXCountSentH32": tmnxDAHttpServer3XXCountSentH32,
       "tmnxDAHttpServer4XXCountSent": tmnxDAHttpServer4XXCountSent,
       "tmnxDAHttpServer4XXCountSentL32": tmnxDAHttpServer4XXCountSentL32,
       "tmnxDAHttpServer4XXCountSentH32": tmnxDAHttpServer4XXCountSentH32,
       "tmnxDAHttpServer5XXCountSent": tmnxDAHttpServer5XXCountSent,
       "tmnxDAHttpServer5XXCountSentL32": tmnxDAHttpServer5XXCountSentL32,
       "tmnxDAHttpServer5XXCountSentH32": tmnxDAHttpServer5XXCountSentH32,
       "tmnxDAHttpIngestAdminState": tmnxDAHttpIngestAdminState,
       "tmnxDAHttpIngestOperState": tmnxDAHttpIngestOperState,
       "tmnxDAHttpIngestIsmLinkName": tmnxDAHttpIngestIsmLinkName,
       "tmnxDAHttpIngestIdleTimeout": tmnxDAHttpIngestIdleTimeout,
       "tmnxDAHttpIngestXferInProg": tmnxDAHttpIngestXferInProg,
       "tmnxDAHttpIngestXferCompleted": tmnxDAHttpIngestXferCompleted,
       "tmnxDAHttpIngestXferCompletedL32": tmnxDAHttpIngestXferCompletedL32,
       "tmnxDAHttpIngestXferCompletedH32": tmnxDAHttpIngestXferCompletedH32,
       "tmnxDAHttpIngestXferTimeouts": tmnxDAHttpIngestXferTimeouts,
       "tmnxDAHttpIngestXferFailed": tmnxDAHttpIngestXferFailed,
       "tmnxDAHttpIngest1XXCountRecd": tmnxDAHttpIngest1XXCountRecd,
       "tmnxDAHttpIngest1XXCountRecdL32": tmnxDAHttpIngest1XXCountRecdL32,
       "tmnxDAHttpIngest1XXCountRecdH32": tmnxDAHttpIngest1XXCountRecdH32,
       "tmnxDAHttpIngest2XXCountRecd": tmnxDAHttpIngest2XXCountRecd,
       "tmnxDAHttpIngest2XXCountRecdL32": tmnxDAHttpIngest2XXCountRecdL32,
       "tmnxDAHttpIngest2XXCountRecdH32": tmnxDAHttpIngest2XXCountRecdH32,
       "tmnxDAHttpIngest3XXCountRecd": tmnxDAHttpIngest3XXCountRecd,
       "tmnxDAHttpIngest3XXCountRecdL32": tmnxDAHttpIngest3XXCountRecdL32,
       "tmnxDAHttpIngest3XXCountRecdH32": tmnxDAHttpIngest3XXCountRecdH32,
       "tmnxDAHttpIngest4XXCountRecd": tmnxDAHttpIngest4XXCountRecd,
       "tmnxDAHttpIngest4XXCountRecdL32": tmnxDAHttpIngest4XXCountRecdL32,
       "tmnxDAHttpIngest4XXCountRecdH32": tmnxDAHttpIngest4XXCountRecdH32,
       "tmnxDAHttpIngest5XXCountRecd": tmnxDAHttpIngest5XXCountRecd,
       "tmnxDAHttpIngest5XXCountRecdL32": tmnxDAHttpIngest5XXCountRecdL32,
       "tmnxDAHttpIngest5XXCountRecdH32": tmnxDAHttpIngest5XXCountRecdH32,
       "tmnxDAIsmLinkTableLastChanged": tmnxDAIsmLinkTableLastChanged,
       "tmnxDAIsmLinkTable": tmnxDAIsmLinkTable,
       "tmnxDAIsmLinkEntry": tmnxDAIsmLinkEntry,
       "tmnxDAIsmLinkName": tmnxDAIsmLinkName,
       "tmnxDAIsmLinkRowStatus": tmnxDAIsmLinkRowStatus,
       "tmnxDAIsmLinkLastChanged": tmnxDAIsmLinkLastChanged,
       "tmnxDAIsmLinkAddrType": tmnxDAIsmLinkAddrType,
       "tmnxDAIsmLinkAddress": tmnxDAIsmLinkAddress,
       "tmnxDAIsmLinkAddrPrefixLength": tmnxDAIsmLinkAddrPrefixLength,
       "tmnxDAIsmLinkDescription": tmnxDAIsmLinkDescription,
       "tmnxDAIsmLinkHttpd": tmnxDAIsmLinkHttpd,
       "tmnxDAIsmLinkHttpListenPort": tmnxDAIsmLinkHttpListenPort,
       "tmnxDAIsmLinkIpMtu": tmnxDAIsmLinkIpMtu,
       "tmnxDAIsmLinkQtag": tmnxDAIsmLinkQtag,
       "tmnxDAIsmLinkMacAddress": tmnxDAIsmLinkMacAddress,
       "tmnxDAIsmLinkAdminState": tmnxDAIsmLinkAdminState,
       "tmnxDAIsmLinkOperState": tmnxDAIsmLinkOperState,
       "tmnxDAIsmLinkBindings": tmnxDAIsmLinkBindings,
       "tmnxDAIsmLinkArpTableLastChanged": tmnxDAIsmLinkArpTableLastChanged,
       "tmnxDAIsmLinkArpTable": tmnxDAIsmLinkArpTable,
       "tmnxDAIsmLinkArpEntry": tmnxDAIsmLinkArpEntry,
       "tmnxDAIsmLinkArpAddrType": tmnxDAIsmLinkArpAddrType,
       "tmnxDAIsmLinkArpAddress": tmnxDAIsmLinkArpAddress,
       "tmnxDAIsmLinkArpRowStatus": tmnxDAIsmLinkArpRowStatus,
       "tmnxDAIsmLinkArpLastChanged": tmnxDAIsmLinkArpLastChanged,
       "tmnxDAIsmLinkArpMacAddr": tmnxDAIsmLinkArpMacAddr,
       "tmnxDAIsmLinkArpType": tmnxDAIsmLinkArpType,
       "tmnxDAStRouteTableLastChanged": tmnxDAStRouteTableLastChanged,
       "tmnxDAStRouteTable": tmnxDAStRouteTable,
       "tmnxDAStRouteEntry": tmnxDAStRouteEntry,
       "tmnxDAStRouteAddrType": tmnxDAStRouteAddrType,
       "tmnxDAStRouteAddress": tmnxDAStRouteAddress,
       "tmnxDAStRoutePrefixLength": tmnxDAStRoutePrefixLength,
       "tmnxDAStRouteNextHopAddrType": tmnxDAStRouteNextHopAddrType,
       "tmnxDAStRouteNextHopAddress": tmnxDAStRouteNextHopAddress,
       "tmnxDAStRouteRowStatus": tmnxDAStRouteRowStatus,
       "tmnxDAStRouteLastChanged": tmnxDAStRouteLastChanged,
       "tmnxDAStRouteMetric": tmnxDAStRouteMetric,
       "tmnxDASGCardTable": tmnxDASGCardTable,
       "tmnxDASGCardEntry": tmnxDASGCardEntry,
       "tmnxDASGCardNumber": tmnxDASGCardNumber,
       "tmnxDASGCardUpTime": tmnxDASGCardUpTime,
       "tmnxDASGCardTotNumTCPConn": tmnxDASGCardTotNumTCPConn,
       "tmnxDASGCardTCPConnEstab": tmnxDASGCardTCPConnEstab,
       "tmnxDASGCardTCPConnEstabL32": tmnxDASGCardTCPConnEstabL32,
       "tmnxDASGCardTCPConnEstabH32": tmnxDASGCardTCPConnEstabH32,
       "tmnxDASGCardTCPConnClosed": tmnxDASGCardTCPConnClosed,
       "tmnxDASGCardTCPConnClosedL32": tmnxDASGCardTCPConnClosedL32,
       "tmnxDASGCardTCPConnClosedH32": tmnxDASGCardTCPConnClosedH32,
       "tmnxDASGCardTCPRetries": tmnxDASGCardTCPRetries,
       "tmnxDASGCardTCPRetriesL32": tmnxDASGCardTCPRetriesL32,
       "tmnxDASGCardTCPRetriesH32": tmnxDASGCardTCPRetriesH32,
       "tmnxDASGCardTCPAckTimeOut": tmnxDASGCardTCPAckTimeOut,
       "tmnxDASGCardTCPAckTimeOutL32": tmnxDASGCardTCPAckTimeOutL32,
       "tmnxDASGCardTCPAckTimeOutH32": tmnxDASGCardTCPAckTimeOutH32,
       "tmnxDASGCardTCPFarEndClosed": tmnxDASGCardTCPFarEndClosed,
       "tmnxDASGCardTCPFarEndClosedL32": tmnxDASGCardTCPFarEndClosedL32,
       "tmnxDASGCardTCPFarEndClosedH32": tmnxDASGCardTCPFarEndClosedH32,
       "tmnxDASGCardTCPLocalEndClosed": tmnxDASGCardTCPLocalEndClosed,
       "tmnxDASGCardTCPLocalEndClosedL32": tmnxDASGCardTCPLocalEndClosedL32,
       "tmnxDASGCardTCPLocalEndClosedH32": tmnxDASGCardTCPLocalEndClosedH32,
       "tmnxDASGCardUsedStorageCpcty": tmnxDASGCardUsedStorageCpcty,
       "tmnxDASGCardUsedStorageCpctyL32": tmnxDASGCardUsedStorageCpctyL32,
       "tmnxDASGCardUsedStorageCpctyH32": tmnxDASGCardUsedStorageCpctyH32,
       "tmnxDASGCardRemStorageCpcty": tmnxDASGCardRemStorageCpcty,
       "tmnxDASGCardRemStorageCpctyL32": tmnxDASGCardRemStorageCpctyL32,
       "tmnxDASGCardRemStorageCpctyH32": tmnxDASGCardRemStorageCpctyH32,
       "tmnxDASGCardNumberOfAssets": tmnxDASGCardNumberOfAssets,
       "tmnxDASGCardNumberOfOrigins": tmnxDASGCardNumberOfOrigins,
       "tmnxDASGCardNumberOfURIs": tmnxDASGCardNumberOfURIs,
       "tmnxDASGCardECCBlockCorrections": tmnxDASGCardECCBlockCorrections,
       "tmnxDASGCardECCBlockFailures": tmnxDASGCardECCBlockFailures,
       "tmnxDASGCardPercentBadBlocks": tmnxDASGCardPercentBadBlocks,
       "tmnxDASGCardFPGATotPktsSent": tmnxDASGCardFPGATotPktsSent,
       "tmnxDASGCardFPGATotPktsSentL32": tmnxDASGCardFPGATotPktsSentL32,
       "tmnxDASGCardFPGATotPktsSentH32": tmnxDASGCardFPGATotPktsSentH32,
       "tmnxDASGCardFPGATotBytesSent": tmnxDASGCardFPGATotBytesSent,
       "tmnxDASGCardFPGATotBytesSentL32": tmnxDASGCardFPGATotBytesSentL32,
       "tmnxDASGCardFPGATotBytesSentH32": tmnxDASGCardFPGATotBytesSentH32,
       "tmnxDASGCardFPGATotPktsRecd": tmnxDASGCardFPGATotPktsRecd,
       "tmnxDASGCardFPGATotPktsRecdL32": tmnxDASGCardFPGATotPktsRecdL32,
       "tmnxDASGCardFPGATotPktsRecdH32": tmnxDASGCardFPGATotPktsRecdH32,
       "tmnxDASGCardFPGATotBytesRecd": tmnxDASGCardFPGATotBytesRecd,
       "tmnxDASGCardFPGATotBytesRecdL32": tmnxDASGCardFPGATotBytesRecdL32,
       "tmnxDASGCardFPGATotBytesRecdH32": tmnxDASGCardFPGATotBytesRecdH32,
       "tmnxDASGCardFPGAUnderflowErrors": tmnxDASGCardFPGAUnderflowErrors,
       "tmnxDASGCardFPGAOverflowErrors": tmnxDASGCardFPGAOverflowErrors,
       "tmnxDADCIntfTable": tmnxDADCIntfTable,
       "tmnxDADCIntfEntry": tmnxDADCIntfEntry,
       "tmnxDADCIntfServerIndex": tmnxDADCIntfServerIndex,
       "tmnxDADCIntfType": tmnxDADCIntfType,
       "tmnxDADCIntfIPAddrType": tmnxDADCIntfIPAddrType,
       "tmnxDADCIntfIPAddress": tmnxDADCIntfIPAddress,
       "tmnxDADCIntfFQDNType": tmnxDADCIntfFQDNType,
       "tmnxDADCIntfFQDN": tmnxDADCIntfFQDN,
       "tmnxDADCIntfSrcPort": tmnxDADCIntfSrcPort,
       "tmnxDADCIntfDestPort": tmnxDADCIntfDestPort,
       "tmnxDADCIntfOperState": tmnxDADCIntfOperState,
       "tmnxDADCIntfIPUpTime": tmnxDADCIntfIPUpTime,
       "tmnxDADCIntfIdleTime": tmnxDADCIntfIdleTime,
       "tmnxDADCIntfRetry": tmnxDADCIntfRetry,
       "tmnxDADCIntfTimeToLive": tmnxDADCIntfTimeToLive,
       "tmnxDADCIntfEtag": tmnxDADCIntfEtag,
       "tmnxDADCIntfInterval": tmnxDADCIntfInterval,
       "tmnxDADCIntfPriority": tmnxDADCIntfPriority,
       "tmnxDADCIntfWeight": tmnxDADCIntfWeight,
       "tmnxDADCIntfAttemptedSessStups": tmnxDADCIntfAttemptedSessStups,
       "tmnxDADCIntfFailedSessStups": tmnxDADCIntfFailedSessStups,
       "tmnxDADCIntfPingReqTxCount": tmnxDADCIntfPingReqTxCount,
       "tmnxDADCIntfPingResRxCount": tmnxDADCIntfPingResRxCount,
       "tmnxDADCIntfReqMsgTxCount": tmnxDADCIntfReqMsgTxCount,
       "tmnxDADCIntfReqMsgTxCountL32": tmnxDADCIntfReqMsgTxCountL32,
       "tmnxDADCIntfReqMsgTxCountH32": tmnxDADCIntfReqMsgTxCountH32,
       "tmnxDADCIntfResMsgRxCount": tmnxDADCIntfResMsgRxCount,
       "tmnxDADCIntfResMsgRxCountL32": tmnxDADCIntfResMsgRxCountL32,
       "tmnxDADCIntfResMsgRxCountH32": tmnxDADCIntfResMsgRxCountH32,
       "tmnxDADCIntfDecodeErrors": tmnxDADCIntfDecodeErrors,
       "tmnxDADCIntfConnectionBounce": tmnxDADCIntfConnectionBounce,
       "tmnxDADCIntfRemoteClose": tmnxDADCIntfRemoteClose,
       "tmnxDADCIntfNoResponse": tmnxDADCIntfNoResponse,
       "tmnxDAGrpOrigSvrTable": tmnxDAGrpOrigSvrTable,
       "tmnxDAGrpOrigSvrEntry": tmnxDAGrpOrigSvrEntry,
       "tmnxDAGrpOrigSvrName": tmnxDAGrpOrigSvrName,
       "tmnxDAGrpOrigSvrIPAddrType": tmnxDAGrpOrigSvrIPAddrType,
       "tmnxDAGrpOrigSvrIPAddress": tmnxDAGrpOrigSvrIPAddress,
       "tmnxDAGrpOrigSvrNumObjDelvred": tmnxDAGrpOrigSvrNumObjDelvred,
       "tmnxDAGrpOrigSvrNumObjDelvredL32": tmnxDAGrpOrigSvrNumObjDelvredL32,
       "tmnxDAGrpOrigSvrNumObjDelvredH32": tmnxDAGrpOrigSvrNumObjDelvredH32,
       "tmnxDAGrpOrigSvrNumObjFailed": tmnxDAGrpOrigSvrNumObjFailed,
       "tmnxDAGrpOrigSvrNumObjFailedL32": tmnxDAGrpOrigSvrNumObjFailedL32,
       "tmnxDAGrpOrigSvrNumObjFailedH32": tmnxDAGrpOrigSvrNumObjFailedH32,
       "tmnxDAGrpOrigSvrNumCurTCPConn": tmnxDAGrpOrigSvrNumCurTCPConn,
       "tmnxDANotifyPrefix": tmnxDANotifyPrefix,
       "tmnxDANotifications": tmnxDANotifications}
)
