# SNMP MIB module (NHDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NHDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:29 2024
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

nhdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 213)
)
nhdpMIB.setRevisions(
        ("2012-10-22 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NeighborIfIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NeighborRouterIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_NhdpNotifications_ObjectIdentity = ObjectIdentity
nhdpNotifications = _NhdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 0)
)
_NhdpNotificationsObjects_ObjectIdentity = ObjectIdentity
nhdpNotificationsObjects = _NhdpNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 0, 0)
)
_NhdpNotificationsControl_ObjectIdentity = ObjectIdentity
nhdpNotificationsControl = _NhdpNotificationsControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 0, 1)
)


class _NhdpNbrStateChangeThreshold_Type(Integer32):
    """Custom type nhdpNbrStateChangeThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NhdpNbrStateChangeThreshold_Type.__name__ = "Integer32"
_NhdpNbrStateChangeThreshold_Object = MibScalar
nhdpNbrStateChangeThreshold = _NhdpNbrStateChangeThreshold_Object(
    (1, 3, 6, 1, 2, 1, 213, 0, 1, 1),
    _NhdpNbrStateChangeThreshold_Type()
)
nhdpNbrStateChangeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nhdpNbrStateChangeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    nhdpNbrStateChangeThreshold.setUnits("changes")


class _NhdpNbrStateChangeWindow_Type(TimeTicks):
    """Custom type nhdpNbrStateChangeWindow based on TimeTicks"""
    defaultValue = 1000


_NhdpNbrStateChangeWindow_Object = MibScalar
nhdpNbrStateChangeWindow = _NhdpNbrStateChangeWindow_Object(
    (1, 3, 6, 1, 2, 1, 213, 0, 1, 2),
    _NhdpNbrStateChangeWindow_Type()
)
nhdpNbrStateChangeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nhdpNbrStateChangeWindow.setStatus("current")


class _Nhdp2HopNbrStateChangeThreshold_Type(Integer32):
    """Custom type nhdp2HopNbrStateChangeThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Nhdp2HopNbrStateChangeThreshold_Type.__name__ = "Integer32"
_Nhdp2HopNbrStateChangeThreshold_Object = MibScalar
nhdp2HopNbrStateChangeThreshold = _Nhdp2HopNbrStateChangeThreshold_Object(
    (1, 3, 6, 1, 2, 1, 213, 0, 1, 3),
    _Nhdp2HopNbrStateChangeThreshold_Type()
)
nhdp2HopNbrStateChangeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nhdp2HopNbrStateChangeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    nhdp2HopNbrStateChangeThreshold.setUnits("changes")


class _Nhdp2HopNbrStateChangeWindow_Type(TimeTicks):
    """Custom type nhdp2HopNbrStateChangeWindow based on TimeTicks"""
    defaultValue = 1000


_Nhdp2HopNbrStateChangeWindow_Object = MibScalar
nhdp2HopNbrStateChangeWindow = _Nhdp2HopNbrStateChangeWindow_Object(
    (1, 3, 6, 1, 2, 1, 213, 0, 1, 4),
    _Nhdp2HopNbrStateChangeWindow_Type()
)
nhdp2HopNbrStateChangeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nhdp2HopNbrStateChangeWindow.setStatus("current")
_NhdpNotificationsStates_ObjectIdentity = ObjectIdentity
nhdpNotificationsStates = _NhdpNotificationsStates_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 0, 2)
)


class _NhdpNbrState_Type(Integer32):
    """Custom type nhdpNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 1),
          ("down", 0),
          ("symmetric", 2))
    )


_NhdpNbrState_Type.__name__ = "Integer32"
_NhdpNbrState_Object = MibScalar
nhdpNbrState = _NhdpNbrState_Object(
    (1, 3, 6, 1, 2, 1, 213, 0, 2, 1),
    _NhdpNbrState_Type()
)
nhdpNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpNbrState.setStatus("current")


class _Nhdp2HopNbrState_Type(Integer32):
    """Custom type nhdp2HopNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_Nhdp2HopNbrState_Type.__name__ = "Integer32"
_Nhdp2HopNbrState_Object = MibScalar
nhdp2HopNbrState = _Nhdp2HopNbrState_Object(
    (1, 3, 6, 1, 2, 1, 213, 0, 2, 2),
    _Nhdp2HopNbrState_Type()
)
nhdp2HopNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdp2HopNbrState.setStatus("current")
_NhdpObjects_ObjectIdentity = ObjectIdentity
nhdpObjects = _NhdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 1)
)
_NhdpConfigurationObjGrp_ObjectIdentity = ObjectIdentity
nhdpConfigurationObjGrp = _NhdpConfigurationObjGrp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 1, 1)
)
_NhdpInterfaceTable_Object = MibTable
nhdpInterfaceTable = _NhdpInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nhdpInterfaceTable.setStatus("current")
_NhdpInterfaceEntry_Object = MibTableRow
nhdpInterfaceEntry = _NhdpInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1)
)
nhdpInterfaceEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpIfIndex"),
)
if mibBuilder.loadTexts:
    nhdpInterfaceEntry.setStatus("current")
_NhdpIfIndex_Type = InterfaceIndex
_NhdpIfIndex_Object = MibTableColumn
nhdpIfIndex = _NhdpIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 1),
    _NhdpIfIndex_Type()
)
nhdpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhdpIfIndex.setStatus("current")
_NhdpIfName_Type = SnmpAdminString
_NhdpIfName_Object = MibTableColumn
nhdpIfName = _NhdpIfName_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 2),
    _NhdpIfName_Type()
)
nhdpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfName.setStatus("current")


class _NhdpIfStatus_Type(TruthValue):
    """Custom type nhdpIfStatus based on TruthValue"""


_NhdpIfStatus_Object = MibTableColumn
nhdpIfStatus = _NhdpIfStatus_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 3),
    _NhdpIfStatus_Type()
)
nhdpIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpIfStatus.setStatus("current")


class _NhdpHelloInterval_Type(Unsigned32):
    """Custom type nhdpHelloInterval based on Unsigned32"""
    defaultValue = 2000


_NhdpHelloInterval_Object = MibTableColumn
nhdpHelloInterval = _NhdpHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 4),
    _NhdpHelloInterval_Type()
)
nhdpHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    nhdpHelloInterval.setUnits("milliseconds")


class _NhdpHelloMinInterval_Type(Unsigned32):
    """Custom type nhdpHelloMinInterval based on Unsigned32"""
    defaultValue = 500


_NhdpHelloMinInterval_Object = MibTableColumn
nhdpHelloMinInterval = _NhdpHelloMinInterval_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 5),
    _NhdpHelloMinInterval_Type()
)
nhdpHelloMinInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpHelloMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    nhdpHelloMinInterval.setUnits("milliseconds")


class _NhdpRefreshInterval_Type(Unsigned32):
    """Custom type nhdpRefreshInterval based on Unsigned32"""
    defaultValue = 2000


_NhdpRefreshInterval_Object = MibTableColumn
nhdpRefreshInterval = _NhdpRefreshInterval_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 6),
    _NhdpRefreshInterval_Type()
)
nhdpRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    nhdpRefreshInterval.setUnits("milliseconds")


class _NhdpLHoldTime_Type(Unsigned32):
    """Custom type nhdpLHoldTime based on Unsigned32"""
    defaultValue = 6000


_NhdpLHoldTime_Object = MibTableColumn
nhdpLHoldTime = _NhdpLHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 7),
    _NhdpLHoldTime_Type()
)
nhdpLHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpLHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    nhdpLHoldTime.setUnits("milliseconds")


class _NhdpHHoldTime_Type(Unsigned32):
    """Custom type nhdpHHoldTime based on Unsigned32"""
    defaultValue = 6000


_NhdpHHoldTime_Object = MibTableColumn
nhdpHHoldTime = _NhdpHHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 8),
    _NhdpHHoldTime_Type()
)
nhdpHHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpHHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    nhdpHHoldTime.setUnits("milliseconds")
_NhdpHystAcceptQuality_Type = Float32TC
_NhdpHystAcceptQuality_Object = MibTableColumn
nhdpHystAcceptQuality = _NhdpHystAcceptQuality_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 9),
    _NhdpHystAcceptQuality_Type()
)
nhdpHystAcceptQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpHystAcceptQuality.setStatus("current")
_NhdpHystRejectQuality_Type = Float32TC
_NhdpHystRejectQuality_Object = MibTableColumn
nhdpHystRejectQuality = _NhdpHystRejectQuality_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 10),
    _NhdpHystRejectQuality_Type()
)
nhdpHystRejectQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpHystRejectQuality.setStatus("current")
_NhdpInitialQuality_Type = Float32TC
_NhdpInitialQuality_Object = MibTableColumn
nhdpInitialQuality = _NhdpInitialQuality_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 11),
    _NhdpInitialQuality_Type()
)
nhdpInitialQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpInitialQuality.setStatus("current")


class _NhdpInitialPending_Type(TruthValue):
    """Custom type nhdpInitialPending based on TruthValue"""


_NhdpInitialPending_Object = MibTableColumn
nhdpInitialPending = _NhdpInitialPending_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 12),
    _NhdpInitialPending_Type()
)
nhdpInitialPending.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpInitialPending.setStatus("current")


class _NhdpHpMaxJitter_Type(Unsigned32):
    """Custom type nhdpHpMaxJitter based on Unsigned32"""
    defaultValue = 500


_NhdpHpMaxJitter_Object = MibTableColumn
nhdpHpMaxJitter = _NhdpHpMaxJitter_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 13),
    _NhdpHpMaxJitter_Type()
)
nhdpHpMaxJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpHpMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    nhdpHpMaxJitter.setUnits("milliseconds")


class _NhdpHtMaxJitter_Type(Unsigned32):
    """Custom type nhdpHtMaxJitter based on Unsigned32"""
    defaultValue = 500


_NhdpHtMaxJitter_Object = MibTableColumn
nhdpHtMaxJitter = _NhdpHtMaxJitter_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 14),
    _NhdpHtMaxJitter_Type()
)
nhdpHtMaxJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpHtMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    nhdpHtMaxJitter.setUnits("milliseconds")


class _NhdpIfRowStatus_Type(RowStatus):
    """Custom type nhdpIfRowStatus based on RowStatus"""


_NhdpIfRowStatus_Object = MibTableColumn
nhdpIfRowStatus = _NhdpIfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 1, 1, 15),
    _NhdpIfRowStatus_Type()
)
nhdpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpIfRowStatus.setStatus("current")


class _NhdpNHoldTime_Type(Unsigned32):
    """Custom type nhdpNHoldTime based on Unsigned32"""
    defaultValue = 6000


_NhdpNHoldTime_Object = MibScalar
nhdpNHoldTime = _NhdpNHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 2),
    _NhdpNHoldTime_Type()
)
nhdpNHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nhdpNHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    nhdpNHoldTime.setUnits("milliseconds")


class _NhdpIHoldTime_Type(Unsigned32):
    """Custom type nhdpIHoldTime based on Unsigned32"""
    defaultValue = 6000


_NhdpIHoldTime_Object = MibScalar
nhdpIHoldTime = _NhdpIHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 3),
    _NhdpIHoldTime_Type()
)
nhdpIHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nhdpIHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIHoldTime.setUnits("milliseconds")
_NhdpLibLocalIfSetTable_Object = MibTable
nhdpLibLocalIfSetTable = _NhdpLibLocalIfSetTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4)
)
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetTable.setStatus("current")
_NhdpLibLocalIfSetEntry_Object = MibTableRow
nhdpLibLocalIfSetEntry = _NhdpLibLocalIfSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4, 1)
)
nhdpLibLocalIfSetEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpLibLocalIfSetIndex"),
)
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetEntry.setStatus("current")


class _NhdpLibLocalIfSetIndex_Type(Integer32):
    """Custom type nhdpLibLocalIfSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhdpLibLocalIfSetIndex_Type.__name__ = "Integer32"
_NhdpLibLocalIfSetIndex_Object = MibTableColumn
nhdpLibLocalIfSetIndex = _NhdpLibLocalIfSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4, 1, 1),
    _NhdpLibLocalIfSetIndex_Type()
)
nhdpLibLocalIfSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetIndex.setStatus("current")
_NhdpLibLocalIfSetIfIndex_Type = InterfaceIndex
_NhdpLibLocalIfSetIfIndex_Object = MibTableColumn
nhdpLibLocalIfSetIfIndex = _NhdpLibLocalIfSetIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4, 1, 2),
    _NhdpLibLocalIfSetIfIndex_Type()
)
nhdpLibLocalIfSetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetIfIndex.setStatus("current")
_NhdpLibLocalIfSetIpAddrType_Type = InetAddressType
_NhdpLibLocalIfSetIpAddrType_Object = MibTableColumn
nhdpLibLocalIfSetIpAddrType = _NhdpLibLocalIfSetIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4, 1, 3),
    _NhdpLibLocalIfSetIpAddrType_Type()
)
nhdpLibLocalIfSetIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetIpAddrType.setStatus("current")


class _NhdpLibLocalIfSetIpAddr_Type(InetAddress):
    """Custom type nhdpLibLocalIfSetIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_NhdpLibLocalIfSetIpAddr_Type.__name__ = "InetAddress"
_NhdpLibLocalIfSetIpAddr_Object = MibTableColumn
nhdpLibLocalIfSetIpAddr = _NhdpLibLocalIfSetIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4, 1, 4),
    _NhdpLibLocalIfSetIpAddr_Type()
)
nhdpLibLocalIfSetIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetIpAddr.setStatus("current")
_NhdpLibLocalIfSetIpAddrPrefixLen_Type = InetAddressPrefixLength
_NhdpLibLocalIfSetIpAddrPrefixLen_Object = MibTableColumn
nhdpLibLocalIfSetIpAddrPrefixLen = _NhdpLibLocalIfSetIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4, 1, 5),
    _NhdpLibLocalIfSetIpAddrPrefixLen_Type()
)
nhdpLibLocalIfSetIpAddrPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetIpAddrPrefixLen.setStatus("current")


class _NhdpLibLocalIfSetRowStatus_Type(RowStatus):
    """Custom type nhdpLibLocalIfSetRowStatus based on RowStatus"""


_NhdpLibLocalIfSetRowStatus_Object = MibTableColumn
nhdpLibLocalIfSetRowStatus = _NhdpLibLocalIfSetRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 4, 1, 6),
    _NhdpLibLocalIfSetRowStatus_Type()
)
nhdpLibLocalIfSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nhdpLibLocalIfSetRowStatus.setStatus("current")
_NhdpLibRemovedIfAddrSetTable_Object = MibTable
nhdpLibRemovedIfAddrSetTable = _NhdpLibRemovedIfAddrSetTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5)
)
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetTable.setStatus("current")
_NhdpLibRemovedIfAddrSetEntry_Object = MibTableRow
nhdpLibRemovedIfAddrSetEntry = _NhdpLibRemovedIfAddrSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5, 1)
)
nhdpLibRemovedIfAddrSetEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpLibRemovedIfAddrSetIndex"),
)
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetEntry.setStatus("current")


class _NhdpLibRemovedIfAddrSetIndex_Type(Integer32):
    """Custom type nhdpLibRemovedIfAddrSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhdpLibRemovedIfAddrSetIndex_Type.__name__ = "Integer32"
_NhdpLibRemovedIfAddrSetIndex_Object = MibTableColumn
nhdpLibRemovedIfAddrSetIndex = _NhdpLibRemovedIfAddrSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5, 1, 1),
    _NhdpLibRemovedIfAddrSetIndex_Type()
)
nhdpLibRemovedIfAddrSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetIndex.setStatus("current")
_NhdpLibRemovedIfAddrSetIpAddrType_Type = InetAddressType
_NhdpLibRemovedIfAddrSetIpAddrType_Object = MibTableColumn
nhdpLibRemovedIfAddrSetIpAddrType = _NhdpLibRemovedIfAddrSetIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5, 1, 2),
    _NhdpLibRemovedIfAddrSetIpAddrType_Type()
)
nhdpLibRemovedIfAddrSetIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetIpAddrType.setStatus("current")


class _NhdpLibRemovedIfAddrSetIpAddr_Type(InetAddress):
    """Custom type nhdpLibRemovedIfAddrSetIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_NhdpLibRemovedIfAddrSetIpAddr_Type.__name__ = "InetAddress"
_NhdpLibRemovedIfAddrSetIpAddr_Object = MibTableColumn
nhdpLibRemovedIfAddrSetIpAddr = _NhdpLibRemovedIfAddrSetIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5, 1, 3),
    _NhdpLibRemovedIfAddrSetIpAddr_Type()
)
nhdpLibRemovedIfAddrSetIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetIpAddr.setStatus("current")
_NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Type = InetAddressPrefixLength
_NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Object = MibTableColumn
nhdpLibRemovedIfAddrSetIpAddrPrefixLen = _NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5, 1, 4),
    _NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Type()
)
nhdpLibRemovedIfAddrSetIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetIpAddrPrefixLen.setStatus("current")
_NhdpLibRemovedIfAddrSetIfIndex_Type = InterfaceIndex
_NhdpLibRemovedIfAddrSetIfIndex_Object = MibTableColumn
nhdpLibRemovedIfAddrSetIfIndex = _NhdpLibRemovedIfAddrSetIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5, 1, 5),
    _NhdpLibRemovedIfAddrSetIfIndex_Type()
)
nhdpLibRemovedIfAddrSetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetIfIndex.setStatus("current")
_NhdpLibRemovedIfAddrSetIRTime_Type = TimeStamp
_NhdpLibRemovedIfAddrSetIRTime_Object = MibTableColumn
nhdpLibRemovedIfAddrSetIRTime = _NhdpLibRemovedIfAddrSetIRTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 1, 5, 1, 6),
    _NhdpLibRemovedIfAddrSetIRTime_Type()
)
nhdpLibRemovedIfAddrSetIRTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpLibRemovedIfAddrSetIRTime.setStatus("current")
_NhdpStateObjGrp_ObjectIdentity = ObjectIdentity
nhdpStateObjGrp = _NhdpStateObjGrp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 1, 2)
)
_NhdpUpTime_Type = TimeStamp
_NhdpUpTime_Object = MibScalar
nhdpUpTime = _NhdpUpTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 1),
    _NhdpUpTime_Type()
)
nhdpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpUpTime.setStatus("current")
_NhdpInterfaceStateTable_Object = MibTable
nhdpInterfaceStateTable = _NhdpInterfaceStateTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nhdpInterfaceStateTable.setStatus("current")
_NhdpInterfaceStateEntry_Object = MibTableRow
nhdpInterfaceStateEntry = _NhdpInterfaceStateEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 2, 1)
)
nhdpInterfaceStateEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpIfIndex"),
)
if mibBuilder.loadTexts:
    nhdpInterfaceStateEntry.setStatus("current")
_NhdpIfStateUpTime_Type = TimeStamp
_NhdpIfStateUpTime_Object = MibTableColumn
nhdpIfStateUpTime = _NhdpIfStateUpTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 2, 1, 1),
    _NhdpIfStateUpTime_Type()
)
nhdpIfStateUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfStateUpTime.setStatus("current")
_NhdpDiscIfSetTable_Object = MibTable
nhdpDiscIfSetTable = _NhdpDiscIfSetTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3)
)
if mibBuilder.loadTexts:
    nhdpDiscIfSetTable.setStatus("current")
_NhdpDiscIfSetEntry_Object = MibTableRow
nhdpDiscIfSetEntry = _NhdpDiscIfSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3, 1)
)
nhdpDiscIfSetEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpDiscIfSetIndex"),
)
if mibBuilder.loadTexts:
    nhdpDiscIfSetEntry.setStatus("current")


class _NhdpDiscIfSetIndex_Type(Integer32):
    """Custom type nhdpDiscIfSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NhdpDiscIfSetIndex_Type.__name__ = "Integer32"
_NhdpDiscIfSetIndex_Object = MibTableColumn
nhdpDiscIfSetIndex = _NhdpDiscIfSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3, 1, 1),
    _NhdpDiscIfSetIndex_Type()
)
nhdpDiscIfSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhdpDiscIfSetIndex.setStatus("current")
_NhdpDiscIfIndex_Type = NeighborIfIndex
_NhdpDiscIfIndex_Object = MibTableColumn
nhdpDiscIfIndex = _NhdpDiscIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3, 1, 2),
    _NhdpDiscIfIndex_Type()
)
nhdpDiscIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscIfIndex.setStatus("current")
_NhdpDiscRouterIndex_Type = NeighborRouterIndex
_NhdpDiscRouterIndex_Object = MibTableColumn
nhdpDiscRouterIndex = _NhdpDiscRouterIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3, 1, 3),
    _NhdpDiscRouterIndex_Type()
)
nhdpDiscRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscRouterIndex.setStatus("current")
_NhdpDiscIfSetIpAddrType_Type = InetAddressType
_NhdpDiscIfSetIpAddrType_Object = MibTableColumn
nhdpDiscIfSetIpAddrType = _NhdpDiscIfSetIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3, 1, 4),
    _NhdpDiscIfSetIpAddrType_Type()
)
nhdpDiscIfSetIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscIfSetIpAddrType.setStatus("current")


class _NhdpDiscIfSetIpAddr_Type(InetAddress):
    """Custom type nhdpDiscIfSetIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_NhdpDiscIfSetIpAddr_Type.__name__ = "InetAddress"
_NhdpDiscIfSetIpAddr_Object = MibTableColumn
nhdpDiscIfSetIpAddr = _NhdpDiscIfSetIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3, 1, 5),
    _NhdpDiscIfSetIpAddr_Type()
)
nhdpDiscIfSetIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscIfSetIpAddr.setStatus("current")
_NhdpDiscIfSetIpAddrPrefixLen_Type = InetAddressPrefixLength
_NhdpDiscIfSetIpAddrPrefixLen_Object = MibTableColumn
nhdpDiscIfSetIpAddrPrefixLen = _NhdpDiscIfSetIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 3, 1, 6),
    _NhdpDiscIfSetIpAddrPrefixLen_Type()
)
nhdpDiscIfSetIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscIfSetIpAddrPrefixLen.setStatus("current")
_NhdpIibLinkSetTable_Object = MibTable
nhdpIibLinkSetTable = _NhdpIibLinkSetTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 4)
)
if mibBuilder.loadTexts:
    nhdpIibLinkSetTable.setStatus("current")
_NhdpIibLinkSetEntry_Object = MibTableRow
nhdpIibLinkSetEntry = _NhdpIibLinkSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 4, 1)
)
nhdpIibLinkSetEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpIfIndex"),
    (0, "NHDP-MIB", "nhdpDiscIfIndex"),
)
if mibBuilder.loadTexts:
    nhdpIibLinkSetEntry.setStatus("current")
_NhdpIibLinkSetLHeardTime_Type = TimeStamp
_NhdpIibLinkSetLHeardTime_Object = MibTableColumn
nhdpIibLinkSetLHeardTime = _NhdpIibLinkSetLHeardTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 4, 1, 1),
    _NhdpIibLinkSetLHeardTime_Type()
)
nhdpIibLinkSetLHeardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIibLinkSetLHeardTime.setStatus("current")
_NhdpIibLinkSetLSymTime_Type = TimeStamp
_NhdpIibLinkSetLSymTime_Object = MibTableColumn
nhdpIibLinkSetLSymTime = _NhdpIibLinkSetLSymTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 4, 1, 2),
    _NhdpIibLinkSetLSymTime_Type()
)
nhdpIibLinkSetLSymTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIibLinkSetLSymTime.setStatus("current")
_NhdpIibLinkSetLPending_Type = TruthValue
_NhdpIibLinkSetLPending_Object = MibTableColumn
nhdpIibLinkSetLPending = _NhdpIibLinkSetLPending_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 4, 1, 3),
    _NhdpIibLinkSetLPending_Type()
)
nhdpIibLinkSetLPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIibLinkSetLPending.setStatus("current")
_NhdpIibLinkSetLLost_Type = TruthValue
_NhdpIibLinkSetLLost_Object = MibTableColumn
nhdpIibLinkSetLLost = _NhdpIibLinkSetLLost_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 4, 1, 4),
    _NhdpIibLinkSetLLost_Type()
)
nhdpIibLinkSetLLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIibLinkSetLLost.setStatus("current")
_NhdpIibLinkSetLTime_Type = TimeStamp
_NhdpIibLinkSetLTime_Object = MibTableColumn
nhdpIibLinkSetLTime = _NhdpIibLinkSetLTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 4, 1, 5),
    _NhdpIibLinkSetLTime_Type()
)
nhdpIibLinkSetLTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIibLinkSetLTime.setStatus("current")
_NhdpIib2HopSetTable_Object = MibTable
nhdpIib2HopSetTable = _NhdpIib2HopSetTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 5)
)
if mibBuilder.loadTexts:
    nhdpIib2HopSetTable.setStatus("current")
_NhdpIib2HopSetEntry_Object = MibTableRow
nhdpIib2HopSetEntry = _NhdpIib2HopSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 5, 1)
)
nhdpIib2HopSetEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpIfIndex"),
    (0, "NHDP-MIB", "nhdpDiscIfIndex"),
    (0, "NHDP-MIB", "nhdpIib2HopSetIpAddressType"),
    (0, "NHDP-MIB", "nhdpIib2HopSetIpAddress"),
)
if mibBuilder.loadTexts:
    nhdpIib2HopSetEntry.setStatus("current")
_NhdpIib2HopSetIpAddressType_Type = InetAddressType
_NhdpIib2HopSetIpAddressType_Object = MibTableColumn
nhdpIib2HopSetIpAddressType = _NhdpIib2HopSetIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 5, 1, 1),
    _NhdpIib2HopSetIpAddressType_Type()
)
nhdpIib2HopSetIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhdpIib2HopSetIpAddressType.setStatus("current")


class _NhdpIib2HopSetIpAddress_Type(InetAddress):
    """Custom type nhdpIib2HopSetIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_NhdpIib2HopSetIpAddress_Type.__name__ = "InetAddress"
_NhdpIib2HopSetIpAddress_Object = MibTableColumn
nhdpIib2HopSetIpAddress = _NhdpIib2HopSetIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 5, 1, 2),
    _NhdpIib2HopSetIpAddress_Type()
)
nhdpIib2HopSetIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nhdpIib2HopSetIpAddress.setStatus("current")
_NhdpIib2HopSetIpAddrPrefixLen_Type = InetAddressPrefixLength
_NhdpIib2HopSetIpAddrPrefixLen_Object = MibTableColumn
nhdpIib2HopSetIpAddrPrefixLen = _NhdpIib2HopSetIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 5, 1, 3),
    _NhdpIib2HopSetIpAddrPrefixLen_Type()
)
nhdpIib2HopSetIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIib2HopSetIpAddrPrefixLen.setStatus("current")
_NhdpIib2HopSet1HopIfIndex_Type = NeighborIfIndex
_NhdpIib2HopSet1HopIfIndex_Object = MibTableColumn
nhdpIib2HopSet1HopIfIndex = _NhdpIib2HopSet1HopIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 5, 1, 4),
    _NhdpIib2HopSet1HopIfIndex_Type()
)
nhdpIib2HopSet1HopIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIib2HopSet1HopIfIndex.setStatus("current")
_NhdpIib2HopSetN2Time_Type = TimeStamp
_NhdpIib2HopSetN2Time_Object = MibTableColumn
nhdpIib2HopSetN2Time = _NhdpIib2HopSetN2Time_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 5, 1, 5),
    _NhdpIib2HopSetN2Time_Type()
)
nhdpIib2HopSetN2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIib2HopSetN2Time.setStatus("current")
_NhdpNibNeighborSetTable_Object = MibTable
nhdpNibNeighborSetTable = _NhdpNibNeighborSetTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 6)
)
if mibBuilder.loadTexts:
    nhdpNibNeighborSetTable.setStatus("current")
_NhdpNibNeighborSetEntry_Object = MibTableRow
nhdpNibNeighborSetEntry = _NhdpNibNeighborSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 6, 1)
)
nhdpNibNeighborSetEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpDiscRouterIndex"),
)
if mibBuilder.loadTexts:
    nhdpNibNeighborSetEntry.setStatus("current")
_NhdpNibNeighborSetNSymmetric_Type = TruthValue
_NhdpNibNeighborSetNSymmetric_Object = MibTableColumn
nhdpNibNeighborSetNSymmetric = _NhdpNibNeighborSetNSymmetric_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 6, 1, 1),
    _NhdpNibNeighborSetNSymmetric_Type()
)
nhdpNibNeighborSetNSymmetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpNibNeighborSetNSymmetric.setStatus("current")
_NhdpNibLostNeighborSetTable_Object = MibTable
nhdpNibLostNeighborSetTable = _NhdpNibLostNeighborSetTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 7)
)
if mibBuilder.loadTexts:
    nhdpNibLostNeighborSetTable.setStatus("current")
_NhdpNibLostNeighborSetEntry_Object = MibTableRow
nhdpNibLostNeighborSetEntry = _NhdpNibLostNeighborSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 7, 1)
)
nhdpNibLostNeighborSetEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpDiscRouterIndex"),
)
if mibBuilder.loadTexts:
    nhdpNibLostNeighborSetEntry.setStatus("current")
_NhdpNibLostNeighborSetNLTime_Type = TimeStamp
_NhdpNibLostNeighborSetNLTime_Object = MibTableColumn
nhdpNibLostNeighborSetNLTime = _NhdpNibLostNeighborSetNLTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 2, 7, 1, 1),
    _NhdpNibLostNeighborSetNLTime_Type()
)
nhdpNibLostNeighborSetNLTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpNibLostNeighborSetNLTime.setStatus("current")
_NhdpPerformanceObjGrp_ObjectIdentity = ObjectIdentity
nhdpPerformanceObjGrp = _NhdpPerformanceObjGrp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 1, 3)
)
_NhdpInterfacePerfTable_Object = MibTable
nhdpInterfacePerfTable = _NhdpInterfacePerfTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nhdpInterfacePerfTable.setStatus("current")
_NhdpInterfacePerfEntry_Object = MibTableRow
nhdpInterfacePerfEntry = _NhdpInterfacePerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1)
)
nhdpInterfacePerfEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpIfIndex"),
)
if mibBuilder.loadTexts:
    nhdpInterfacePerfEntry.setStatus("current")
_NhdpIfHelloMessageXmits_Type = Counter32
_NhdpIfHelloMessageXmits_Object = MibTableColumn
nhdpIfHelloMessageXmits = _NhdpIfHelloMessageXmits_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 1),
    _NhdpIfHelloMessageXmits_Type()
)
nhdpIfHelloMessageXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmits.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmits.setUnits("messages")
_NhdpIfHelloMessageRecvd_Type = Counter32
_NhdpIfHelloMessageRecvd_Object = MibTableColumn
nhdpIfHelloMessageRecvd = _NhdpIfHelloMessageRecvd_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 2),
    _NhdpIfHelloMessageRecvd_Type()
)
nhdpIfHelloMessageRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageRecvd.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageRecvd.setUnits("messages")
_NhdpIfHelloMessageXmitAccumulatedSize_Type = Counter64
_NhdpIfHelloMessageXmitAccumulatedSize_Object = MibTableColumn
nhdpIfHelloMessageXmitAccumulatedSize = _NhdpIfHelloMessageXmitAccumulatedSize_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 3),
    _NhdpIfHelloMessageXmitAccumulatedSize_Type()
)
nhdpIfHelloMessageXmitAccumulatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedSize.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedSize.setUnits("octets")
_NhdpIfHelloMessageRecvdAccumulatedSize_Type = Counter64
_NhdpIfHelloMessageRecvdAccumulatedSize_Object = MibTableColumn
nhdpIfHelloMessageRecvdAccumulatedSize = _NhdpIfHelloMessageRecvdAccumulatedSize_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 4),
    _NhdpIfHelloMessageRecvdAccumulatedSize_Type()
)
nhdpIfHelloMessageRecvdAccumulatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageRecvdAccumulatedSize.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageRecvdAccumulatedSize.setUnits("octets")
_NhdpIfHelloMessageTriggeredXmits_Type = Counter32
_NhdpIfHelloMessageTriggeredXmits_Object = MibTableColumn
nhdpIfHelloMessageTriggeredXmits = _NhdpIfHelloMessageTriggeredXmits_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 5),
    _NhdpIfHelloMessageTriggeredXmits_Type()
)
nhdpIfHelloMessageTriggeredXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageTriggeredXmits.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageTriggeredXmits.setUnits("messages")
_NhdpIfHelloMessagePeriodicXmits_Type = Counter32
_NhdpIfHelloMessagePeriodicXmits_Object = MibTableColumn
nhdpIfHelloMessagePeriodicXmits = _NhdpIfHelloMessagePeriodicXmits_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 6),
    _NhdpIfHelloMessagePeriodicXmits_Type()
)
nhdpIfHelloMessagePeriodicXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessagePeriodicXmits.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessagePeriodicXmits.setUnits("messages")
_NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Type = Counter32
_NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Object = MibTableColumn
nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount = _NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 7),
    _NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Type()
)
nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount.setUnits("neighbors")
_NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Type = Counter32
_NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Object = MibTableColumn
nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount = _NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 8),
    _NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Type()
)
nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount.setUnits("neighbors")
_NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Type = Counter32
_NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Object = MibTableColumn
nhdpIfHelloMessageXmitAccumulatedLostNeighborCount = _NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 1, 1, 9),
    _NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Type()
)
nhdpIfHelloMessageXmitAccumulatedLostNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedLostNeighborCount.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIfHelloMessageXmitAccumulatedLostNeighborCount.setUnits("neighbors")
_NhdpDiscIfSetPerfTable_Object = MibTable
nhdpDiscIfSetPerfTable = _NhdpDiscIfSetPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nhdpDiscIfSetPerfTable.setStatus("current")
_NhdpDiscIfSetPerfEntry_Object = MibTableRow
nhdpDiscIfSetPerfEntry = _NhdpDiscIfSetPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 2, 1)
)
nhdpDiscIfSetPerfEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpDiscIfIndex"),
)
if mibBuilder.loadTexts:
    nhdpDiscIfSetPerfEntry.setStatus("current")
_NhdpDiscIfRecvdPackets_Type = Counter32
_NhdpDiscIfRecvdPackets_Object = MibTableColumn
nhdpDiscIfRecvdPackets = _NhdpDiscIfRecvdPackets_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 2, 1, 1),
    _NhdpDiscIfRecvdPackets_Type()
)
nhdpDiscIfRecvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscIfRecvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    nhdpDiscIfRecvdPackets.setUnits("packets")
_NhdpDiscIfExpectedPackets_Type = Counter32
_NhdpDiscIfExpectedPackets_Object = MibTableColumn
nhdpDiscIfExpectedPackets = _NhdpDiscIfExpectedPackets_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 2, 1, 2),
    _NhdpDiscIfExpectedPackets_Type()
)
nhdpDiscIfExpectedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscIfExpectedPackets.setStatus("current")
if mibBuilder.loadTexts:
    nhdpDiscIfExpectedPackets.setUnits("packets")
_NhdpNibNeighborSetChanges_Type = Counter32
_NhdpNibNeighborSetChanges_Object = MibScalar
nhdpNibNeighborSetChanges = _NhdpNibNeighborSetChanges_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 3),
    _NhdpNibNeighborSetChanges_Type()
)
nhdpNibNeighborSetChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpNibNeighborSetChanges.setStatus("current")
if mibBuilder.loadTexts:
    nhdpNibNeighborSetChanges.setUnits("changes")
_NhdpDiscNeighborSetPerfTable_Object = MibTable
nhdpDiscNeighborSetPerfTable = _NhdpDiscNeighborSetPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 4)
)
if mibBuilder.loadTexts:
    nhdpDiscNeighborSetPerfTable.setStatus("current")
_NhdpDiscNeighborSetPerfEntry_Object = MibTableRow
nhdpDiscNeighborSetPerfEntry = _NhdpDiscNeighborSetPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 4, 1)
)
nhdpDiscNeighborSetPerfEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpDiscRouterIndex"),
)
if mibBuilder.loadTexts:
    nhdpDiscNeighborSetPerfEntry.setStatus("current")
_NhdpDiscNeighborNibNeighborSetChanges_Type = Counter32
_NhdpDiscNeighborNibNeighborSetChanges_Object = MibTableColumn
nhdpDiscNeighborNibNeighborSetChanges = _NhdpDiscNeighborNibNeighborSetChanges_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 4, 1, 1),
    _NhdpDiscNeighborNibNeighborSetChanges_Type()
)
nhdpDiscNeighborNibNeighborSetChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscNeighborNibNeighborSetChanges.setStatus("current")
if mibBuilder.loadTexts:
    nhdpDiscNeighborNibNeighborSetChanges.setUnits("changes")
_NhdpDiscNeighborNibNeighborSetUpTime_Type = TimeStamp
_NhdpDiscNeighborNibNeighborSetUpTime_Object = MibTableColumn
nhdpDiscNeighborNibNeighborSetUpTime = _NhdpDiscNeighborNibNeighborSetUpTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 4, 1, 2),
    _NhdpDiscNeighborNibNeighborSetUpTime_Type()
)
nhdpDiscNeighborNibNeighborSetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscNeighborNibNeighborSetUpTime.setStatus("current")
_NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Type = Counter32
_NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Object = MibTableColumn
nhdpDiscNeighborNibNeighborSetReachableLinkChanges = _NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 4, 1, 3),
    _NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Type()
)
nhdpDiscNeighborNibNeighborSetReachableLinkChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpDiscNeighborNibNeighborSetReachableLinkChanges.setStatus("current")
if mibBuilder.loadTexts:
    nhdpDiscNeighborNibNeighborSetReachableLinkChanges.setUnits("changes")
_NhdpIib2HopSetPerfTable_Object = MibTable
nhdpIib2HopSetPerfTable = _NhdpIib2HopSetPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 5)
)
if mibBuilder.loadTexts:
    nhdpIib2HopSetPerfTable.setStatus("current")
_NhdpIib2HopSetPerfEntry_Object = MibTableRow
nhdpIib2HopSetPerfEntry = _NhdpIib2HopSetPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 5, 1)
)
nhdpIib2HopSetPerfEntry.setIndexNames(
    (0, "NHDP-MIB", "nhdpDiscRouterIndex"),
)
if mibBuilder.loadTexts:
    nhdpIib2HopSetPerfEntry.setStatus("current")
_NhdpIib2HopSetPerfChanges_Type = Counter32
_NhdpIib2HopSetPerfChanges_Object = MibTableColumn
nhdpIib2HopSetPerfChanges = _NhdpIib2HopSetPerfChanges_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 5, 1, 1),
    _NhdpIib2HopSetPerfChanges_Type()
)
nhdpIib2HopSetPerfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIib2HopSetPerfChanges.setStatus("current")
if mibBuilder.loadTexts:
    nhdpIib2HopSetPerfChanges.setUnits("changes")
_NhdpIib2HopSetPerfUpTime_Type = TimeStamp
_NhdpIib2HopSetPerfUpTime_Object = MibTableColumn
nhdpIib2HopSetPerfUpTime = _NhdpIib2HopSetPerfUpTime_Object(
    (1, 3, 6, 1, 2, 1, 213, 1, 3, 5, 1, 2),
    _NhdpIib2HopSetPerfUpTime_Type()
)
nhdpIib2HopSetPerfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdpIib2HopSetPerfUpTime.setStatus("current")
_NhdpConformance_ObjectIdentity = ObjectIdentity
nhdpConformance = _NhdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 2)
)
_NhdpCompliances_ObjectIdentity = ObjectIdentity
nhdpCompliances = _NhdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 2, 1)
)
_NhdpMIBGroups_ObjectIdentity = ObjectIdentity
nhdpMIBGroups = _NhdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 213, 2, 2)
)

# Managed Objects groups

nhdpConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 213, 2, 2, 2)
)
nhdpConfigurationGroup.setObjects(
      *(("NHDP-MIB", "nhdpIfName"),
        ("NHDP-MIB", "nhdpIfStatus"),
        ("NHDP-MIB", "nhdpHelloInterval"),
        ("NHDP-MIB", "nhdpHelloMinInterval"),
        ("NHDP-MIB", "nhdpRefreshInterval"),
        ("NHDP-MIB", "nhdpLHoldTime"),
        ("NHDP-MIB", "nhdpHHoldTime"),
        ("NHDP-MIB", "nhdpHystAcceptQuality"),
        ("NHDP-MIB", "nhdpHystRejectQuality"),
        ("NHDP-MIB", "nhdpInitialQuality"),
        ("NHDP-MIB", "nhdpInitialPending"),
        ("NHDP-MIB", "nhdpHpMaxJitter"),
        ("NHDP-MIB", "nhdpHtMaxJitter"),
        ("NHDP-MIB", "nhdpNHoldTime"),
        ("NHDP-MIB", "nhdpIHoldTime"),
        ("NHDP-MIB", "nhdpIfRowStatus"),
        ("NHDP-MIB", "nhdpLibLocalIfSetIfIndex"),
        ("NHDP-MIB", "nhdpLibLocalIfSetIpAddrType"),
        ("NHDP-MIB", "nhdpLibLocalIfSetIpAddr"),
        ("NHDP-MIB", "nhdpLibLocalIfSetIpAddrPrefixLen"),
        ("NHDP-MIB", "nhdpLibLocalIfSetRowStatus"),
        ("NHDP-MIB", "nhdpLibRemovedIfAddrSetIpAddrType"),
        ("NHDP-MIB", "nhdpLibRemovedIfAddrSetIpAddr"),
        ("NHDP-MIB", "nhdpLibRemovedIfAddrSetIpAddrPrefixLen"),
        ("NHDP-MIB", "nhdpLibRemovedIfAddrSetIfIndex"),
        ("NHDP-MIB", "nhdpLibRemovedIfAddrSetIRTime"))
)
if mibBuilder.loadTexts:
    nhdpConfigurationGroup.setStatus("current")

nhdpStateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 213, 2, 2, 3)
)
nhdpStateGroup.setObjects(
      *(("NHDP-MIB", "nhdpUpTime"),
        ("NHDP-MIB", "nhdpIfStateUpTime"),
        ("NHDP-MIB", "nhdpDiscRouterIndex"),
        ("NHDP-MIB", "nhdpDiscIfIndex"),
        ("NHDP-MIB", "nhdpDiscIfSetIpAddrType"),
        ("NHDP-MIB", "nhdpDiscIfSetIpAddr"),
        ("NHDP-MIB", "nhdpDiscIfSetIpAddrPrefixLen"),
        ("NHDP-MIB", "nhdpIibLinkSetLHeardTime"),
        ("NHDP-MIB", "nhdpIibLinkSetLSymTime"),
        ("NHDP-MIB", "nhdpIibLinkSetLPending"),
        ("NHDP-MIB", "nhdpIibLinkSetLLost"),
        ("NHDP-MIB", "nhdpIibLinkSetLTime"),
        ("NHDP-MIB", "nhdpIib2HopSetIpAddrPrefixLen"),
        ("NHDP-MIB", "nhdpIib2HopSet1HopIfIndex"),
        ("NHDP-MIB", "nhdpIib2HopSetN2Time"),
        ("NHDP-MIB", "nhdpNibNeighborSetNSymmetric"),
        ("NHDP-MIB", "nhdpNibLostNeighborSetNLTime"))
)
if mibBuilder.loadTexts:
    nhdpStateGroup.setStatus("current")

nhdpPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 213, 2, 2, 4)
)
nhdpPerformanceGroup.setObjects(
      *(("NHDP-MIB", "nhdpIfHelloMessageXmits"),
        ("NHDP-MIB", "nhdpIfHelloMessageRecvd"),
        ("NHDP-MIB", "nhdpIfHelloMessageXmitAccumulatedSize"),
        ("NHDP-MIB", "nhdpIfHelloMessageRecvdAccumulatedSize"),
        ("NHDP-MIB", "nhdpIfHelloMessageTriggeredXmits"),
        ("NHDP-MIB", "nhdpIfHelloMessagePeriodicXmits"),
        ("NHDP-MIB", "nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount"),
        ("NHDP-MIB", "nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount"),
        ("NHDP-MIB", "nhdpIfHelloMessageXmitAccumulatedLostNeighborCount"),
        ("NHDP-MIB", "nhdpDiscIfRecvdPackets"),
        ("NHDP-MIB", "nhdpDiscIfExpectedPackets"),
        ("NHDP-MIB", "nhdpNibNeighborSetChanges"),
        ("NHDP-MIB", "nhdpDiscNeighborNibNeighborSetChanges"),
        ("NHDP-MIB", "nhdpDiscNeighborNibNeighborSetUpTime"),
        ("NHDP-MIB", "nhdpDiscNeighborNibNeighborSetReachableLinkChanges"),
        ("NHDP-MIB", "nhdpIib2HopSetPerfChanges"),
        ("NHDP-MIB", "nhdpIib2HopSetPerfUpTime"))
)
if mibBuilder.loadTexts:
    nhdpPerformanceGroup.setStatus("current")

nhdpNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 213, 2, 2, 5)
)
nhdpNotificationObjectGroup.setObjects(
      *(("NHDP-MIB", "nhdpNbrStateChangeThreshold"),
        ("NHDP-MIB", "nhdpNbrStateChangeWindow"),
        ("NHDP-MIB", "nhdp2HopNbrStateChangeThreshold"),
        ("NHDP-MIB", "nhdp2HopNbrStateChangeWindow"),
        ("NHDP-MIB", "nhdpNbrState"),
        ("NHDP-MIB", "nhdp2HopNbrState"))
)
if mibBuilder.loadTexts:
    nhdpNotificationObjectGroup.setStatus("current")


# Notification objects

nhdpNbrStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 213, 0, 0, 1)
)
nhdpNbrStateChange.setObjects(
      *(("NHDP-MIB", "nhdpIfName"),
        ("NHDP-MIB", "nhdpNbrState"))
)
if mibBuilder.loadTexts:
    nhdpNbrStateChange.setStatus(
        "current"
    )

nhdp2HopNbrStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 213, 0, 0, 2)
)
nhdp2HopNbrStateChange.setObjects(
      *(("NHDP-MIB", "nhdpIfName"),
        ("NHDP-MIB", "nhdp2HopNbrState"))
)
if mibBuilder.loadTexts:
    nhdp2HopNbrStateChange.setStatus(
        "current"
    )

nhdpIfStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 213, 0, 0, 3)
)
nhdpIfStateChange.setObjects(
      *(("NHDP-MIB", "nhdpIfName"),
        ("NHDP-MIB", "nhdpIfStatus"))
)
if mibBuilder.loadTexts:
    nhdpIfStateChange.setStatus(
        "current"
    )


# Notifications groups

nhdpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 213, 2, 2, 6)
)
nhdpNotificationGroup.setObjects(
      *(("NHDP-MIB", "nhdpNbrStateChange"),
        ("NHDP-MIB", "nhdp2HopNbrStateChange"),
        ("NHDP-MIB", "nhdpIfStateChange"))
)
if mibBuilder.loadTexts:
    nhdpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nhdpBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 213, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nhdpBasicCompliance.setStatus(
        "current"
    )

nhdpFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 213, 2, 1, 2)
)
if mibBuilder.loadTexts:
    nhdpFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NHDP-MIB",
    **{"NeighborIfIndex": NeighborIfIndex,
       "NeighborRouterIndex": NeighborRouterIndex,
       "nhdpMIB": nhdpMIB,
       "nhdpNotifications": nhdpNotifications,
       "nhdpNotificationsObjects": nhdpNotificationsObjects,
       "nhdpNbrStateChange": nhdpNbrStateChange,
       "nhdp2HopNbrStateChange": nhdp2HopNbrStateChange,
       "nhdpIfStateChange": nhdpIfStateChange,
       "nhdpNotificationsControl": nhdpNotificationsControl,
       "nhdpNbrStateChangeThreshold": nhdpNbrStateChangeThreshold,
       "nhdpNbrStateChangeWindow": nhdpNbrStateChangeWindow,
       "nhdp2HopNbrStateChangeThreshold": nhdp2HopNbrStateChangeThreshold,
       "nhdp2HopNbrStateChangeWindow": nhdp2HopNbrStateChangeWindow,
       "nhdpNotificationsStates": nhdpNotificationsStates,
       "nhdpNbrState": nhdpNbrState,
       "nhdp2HopNbrState": nhdp2HopNbrState,
       "nhdpObjects": nhdpObjects,
       "nhdpConfigurationObjGrp": nhdpConfigurationObjGrp,
       "nhdpInterfaceTable": nhdpInterfaceTable,
       "nhdpInterfaceEntry": nhdpInterfaceEntry,
       "nhdpIfIndex": nhdpIfIndex,
       "nhdpIfName": nhdpIfName,
       "nhdpIfStatus": nhdpIfStatus,
       "nhdpHelloInterval": nhdpHelloInterval,
       "nhdpHelloMinInterval": nhdpHelloMinInterval,
       "nhdpRefreshInterval": nhdpRefreshInterval,
       "nhdpLHoldTime": nhdpLHoldTime,
       "nhdpHHoldTime": nhdpHHoldTime,
       "nhdpHystAcceptQuality": nhdpHystAcceptQuality,
       "nhdpHystRejectQuality": nhdpHystRejectQuality,
       "nhdpInitialQuality": nhdpInitialQuality,
       "nhdpInitialPending": nhdpInitialPending,
       "nhdpHpMaxJitter": nhdpHpMaxJitter,
       "nhdpHtMaxJitter": nhdpHtMaxJitter,
       "nhdpIfRowStatus": nhdpIfRowStatus,
       "nhdpNHoldTime": nhdpNHoldTime,
       "nhdpIHoldTime": nhdpIHoldTime,
       "nhdpLibLocalIfSetTable": nhdpLibLocalIfSetTable,
       "nhdpLibLocalIfSetEntry": nhdpLibLocalIfSetEntry,
       "nhdpLibLocalIfSetIndex": nhdpLibLocalIfSetIndex,
       "nhdpLibLocalIfSetIfIndex": nhdpLibLocalIfSetIfIndex,
       "nhdpLibLocalIfSetIpAddrType": nhdpLibLocalIfSetIpAddrType,
       "nhdpLibLocalIfSetIpAddr": nhdpLibLocalIfSetIpAddr,
       "nhdpLibLocalIfSetIpAddrPrefixLen": nhdpLibLocalIfSetIpAddrPrefixLen,
       "nhdpLibLocalIfSetRowStatus": nhdpLibLocalIfSetRowStatus,
       "nhdpLibRemovedIfAddrSetTable": nhdpLibRemovedIfAddrSetTable,
       "nhdpLibRemovedIfAddrSetEntry": nhdpLibRemovedIfAddrSetEntry,
       "nhdpLibRemovedIfAddrSetIndex": nhdpLibRemovedIfAddrSetIndex,
       "nhdpLibRemovedIfAddrSetIpAddrType": nhdpLibRemovedIfAddrSetIpAddrType,
       "nhdpLibRemovedIfAddrSetIpAddr": nhdpLibRemovedIfAddrSetIpAddr,
       "nhdpLibRemovedIfAddrSetIpAddrPrefixLen": nhdpLibRemovedIfAddrSetIpAddrPrefixLen,
       "nhdpLibRemovedIfAddrSetIfIndex": nhdpLibRemovedIfAddrSetIfIndex,
       "nhdpLibRemovedIfAddrSetIRTime": nhdpLibRemovedIfAddrSetIRTime,
       "nhdpStateObjGrp": nhdpStateObjGrp,
       "nhdpUpTime": nhdpUpTime,
       "nhdpInterfaceStateTable": nhdpInterfaceStateTable,
       "nhdpInterfaceStateEntry": nhdpInterfaceStateEntry,
       "nhdpIfStateUpTime": nhdpIfStateUpTime,
       "nhdpDiscIfSetTable": nhdpDiscIfSetTable,
       "nhdpDiscIfSetEntry": nhdpDiscIfSetEntry,
       "nhdpDiscIfSetIndex": nhdpDiscIfSetIndex,
       "nhdpDiscIfIndex": nhdpDiscIfIndex,
       "nhdpDiscRouterIndex": nhdpDiscRouterIndex,
       "nhdpDiscIfSetIpAddrType": nhdpDiscIfSetIpAddrType,
       "nhdpDiscIfSetIpAddr": nhdpDiscIfSetIpAddr,
       "nhdpDiscIfSetIpAddrPrefixLen": nhdpDiscIfSetIpAddrPrefixLen,
       "nhdpIibLinkSetTable": nhdpIibLinkSetTable,
       "nhdpIibLinkSetEntry": nhdpIibLinkSetEntry,
       "nhdpIibLinkSetLHeardTime": nhdpIibLinkSetLHeardTime,
       "nhdpIibLinkSetLSymTime": nhdpIibLinkSetLSymTime,
       "nhdpIibLinkSetLPending": nhdpIibLinkSetLPending,
       "nhdpIibLinkSetLLost": nhdpIibLinkSetLLost,
       "nhdpIibLinkSetLTime": nhdpIibLinkSetLTime,
       "nhdpIib2HopSetTable": nhdpIib2HopSetTable,
       "nhdpIib2HopSetEntry": nhdpIib2HopSetEntry,
       "nhdpIib2HopSetIpAddressType": nhdpIib2HopSetIpAddressType,
       "nhdpIib2HopSetIpAddress": nhdpIib2HopSetIpAddress,
       "nhdpIib2HopSetIpAddrPrefixLen": nhdpIib2HopSetIpAddrPrefixLen,
       "nhdpIib2HopSet1HopIfIndex": nhdpIib2HopSet1HopIfIndex,
       "nhdpIib2HopSetN2Time": nhdpIib2HopSetN2Time,
       "nhdpNibNeighborSetTable": nhdpNibNeighborSetTable,
       "nhdpNibNeighborSetEntry": nhdpNibNeighborSetEntry,
       "nhdpNibNeighborSetNSymmetric": nhdpNibNeighborSetNSymmetric,
       "nhdpNibLostNeighborSetTable": nhdpNibLostNeighborSetTable,
       "nhdpNibLostNeighborSetEntry": nhdpNibLostNeighborSetEntry,
       "nhdpNibLostNeighborSetNLTime": nhdpNibLostNeighborSetNLTime,
       "nhdpPerformanceObjGrp": nhdpPerformanceObjGrp,
       "nhdpInterfacePerfTable": nhdpInterfacePerfTable,
       "nhdpInterfacePerfEntry": nhdpInterfacePerfEntry,
       "nhdpIfHelloMessageXmits": nhdpIfHelloMessageXmits,
       "nhdpIfHelloMessageRecvd": nhdpIfHelloMessageRecvd,
       "nhdpIfHelloMessageXmitAccumulatedSize": nhdpIfHelloMessageXmitAccumulatedSize,
       "nhdpIfHelloMessageRecvdAccumulatedSize": nhdpIfHelloMessageRecvdAccumulatedSize,
       "nhdpIfHelloMessageTriggeredXmits": nhdpIfHelloMessageTriggeredXmits,
       "nhdpIfHelloMessagePeriodicXmits": nhdpIfHelloMessagePeriodicXmits,
       "nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount": nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount,
       "nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount": nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount,
       "nhdpIfHelloMessageXmitAccumulatedLostNeighborCount": nhdpIfHelloMessageXmitAccumulatedLostNeighborCount,
       "nhdpDiscIfSetPerfTable": nhdpDiscIfSetPerfTable,
       "nhdpDiscIfSetPerfEntry": nhdpDiscIfSetPerfEntry,
       "nhdpDiscIfRecvdPackets": nhdpDiscIfRecvdPackets,
       "nhdpDiscIfExpectedPackets": nhdpDiscIfExpectedPackets,
       "nhdpNibNeighborSetChanges": nhdpNibNeighborSetChanges,
       "nhdpDiscNeighborSetPerfTable": nhdpDiscNeighborSetPerfTable,
       "nhdpDiscNeighborSetPerfEntry": nhdpDiscNeighborSetPerfEntry,
       "nhdpDiscNeighborNibNeighborSetChanges": nhdpDiscNeighborNibNeighborSetChanges,
       "nhdpDiscNeighborNibNeighborSetUpTime": nhdpDiscNeighborNibNeighborSetUpTime,
       "nhdpDiscNeighborNibNeighborSetReachableLinkChanges": nhdpDiscNeighborNibNeighborSetReachableLinkChanges,
       "nhdpIib2HopSetPerfTable": nhdpIib2HopSetPerfTable,
       "nhdpIib2HopSetPerfEntry": nhdpIib2HopSetPerfEntry,
       "nhdpIib2HopSetPerfChanges": nhdpIib2HopSetPerfChanges,
       "nhdpIib2HopSetPerfUpTime": nhdpIib2HopSetPerfUpTime,
       "nhdpConformance": nhdpConformance,
       "nhdpCompliances": nhdpCompliances,
       "nhdpBasicCompliance": nhdpBasicCompliance,
       "nhdpFullCompliance": nhdpFullCompliance,
       "nhdpMIBGroups": nhdpMIBGroups,
       "nhdpConfigurationGroup": nhdpConfigurationGroup,
       "nhdpStateGroup": nhdpStateGroup,
       "nhdpPerformanceGroup": nhdpPerformanceGroup,
       "nhdpNotificationObjectGroup": nhdpNotificationObjectGroup,
       "nhdpNotificationGroup": nhdpNotificationGroup}
)
