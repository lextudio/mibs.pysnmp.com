# SNMP MIB module (OLSRv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLSRv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:11 2024
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

(IANAolsrv2LinkMetricTypeTC,) = mibBuilder.importSymbols(
    "IANA-OLSRv2-LINK-METRIC-TYPE-MIB",
    "IANAolsrv2LinkMetricTypeTC")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(nhdpIib2HopSetEntry,
 nhdpIibLinkSetEntry,
 nhdpInterfaceEntry,
 nhdpInterfacePerfEntry,
 nhdpNibNeighborSetEntry) = mibBuilder.importSymbols(
    "NHDP-MIB",
    "nhdpIib2HopSetEntry",
    "nhdpIibLinkSetEntry",
    "nhdpInterfaceEntry",
    "nhdpInterfacePerfEntry",
    "nhdpNibNeighborSetEntry")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

manetOlsrv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 219)
)
manetOlsrv2MIB.setRevisions(
        ("2014-04-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Olsrv2MetricValueCompressedFormTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16776960),
    )



class Olsrv2TimeValueCompressedForm32TC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3932160000),
    )



class Olsrv2StatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class WillingnessTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



# MIB Managed Objects in the order of their OIDs

_Olsrv2MIBNotifications_ObjectIdentity = ObjectIdentity
olsrv2MIBNotifications = _Olsrv2MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 0)
)
_Olsrv2NotificationsObjects_ObjectIdentity = ObjectIdentity
olsrv2NotificationsObjects = _Olsrv2NotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 0, 0)
)
_Olsrv2NotificationsControl_ObjectIdentity = ObjectIdentity
olsrv2NotificationsControl = _Olsrv2NotificationsControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 0, 1)
)


class _Olsrv2RoutingSetRecalculationCountThreshold_Type(Integer32):
    """Custom type olsrv2RoutingSetRecalculationCountThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Olsrv2RoutingSetRecalculationCountThreshold_Type.__name__ = "Integer32"
_Olsrv2RoutingSetRecalculationCountThreshold_Object = MibScalar
olsrv2RoutingSetRecalculationCountThreshold = _Olsrv2RoutingSetRecalculationCountThreshold_Object(
    (1, 3, 6, 1, 2, 1, 219, 0, 1, 1),
    _Olsrv2RoutingSetRecalculationCountThreshold_Type()
)
olsrv2RoutingSetRecalculationCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2RoutingSetRecalculationCountThreshold.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2RoutingSetRecalculationCountThreshold.setUnits("recalculations")


class _Olsrv2RoutingSetRecalculationCountWindow_Type(TimeTicks):
    """Custom type olsrv2RoutingSetRecalculationCountWindow based on TimeTicks"""
    defaultValue = 1000


_Olsrv2RoutingSetRecalculationCountWindow_Object = MibScalar
olsrv2RoutingSetRecalculationCountWindow = _Olsrv2RoutingSetRecalculationCountWindow_Object(
    (1, 3, 6, 1, 2, 1, 219, 0, 1, 2),
    _Olsrv2RoutingSetRecalculationCountWindow_Type()
)
olsrv2RoutingSetRecalculationCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2RoutingSetRecalculationCountWindow.setStatus("current")


class _Olsrv2MPRSetRecalculationCountThreshold_Type(Integer32):
    """Custom type olsrv2MPRSetRecalculationCountThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Olsrv2MPRSetRecalculationCountThreshold_Type.__name__ = "Integer32"
_Olsrv2MPRSetRecalculationCountThreshold_Object = MibScalar
olsrv2MPRSetRecalculationCountThreshold = _Olsrv2MPRSetRecalculationCountThreshold_Object(
    (1, 3, 6, 1, 2, 1, 219, 0, 1, 3),
    _Olsrv2MPRSetRecalculationCountThreshold_Type()
)
olsrv2MPRSetRecalculationCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2MPRSetRecalculationCountThreshold.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2MPRSetRecalculationCountThreshold.setUnits("recalculations")


class _Olsrv2MPRSetRecalculationCountWindow_Type(TimeTicks):
    """Custom type olsrv2MPRSetRecalculationCountWindow based on TimeTicks"""
    defaultValue = 1000


_Olsrv2MPRSetRecalculationCountWindow_Object = MibScalar
olsrv2MPRSetRecalculationCountWindow = _Olsrv2MPRSetRecalculationCountWindow_Object(
    (1, 3, 6, 1, 2, 1, 219, 0, 1, 4),
    _Olsrv2MPRSetRecalculationCountWindow_Type()
)
olsrv2MPRSetRecalculationCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2MPRSetRecalculationCountWindow.setStatus("current")
_Olsrv2NotificationsStates_ObjectIdentity = ObjectIdentity
olsrv2NotificationsStates = _Olsrv2NotificationsStates_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 0, 2)
)


class _Olsrv2PreviousOrigIpAddrType_Type(InetAddressType):
    """Custom type olsrv2PreviousOrigIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2PreviousOrigIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2PreviousOrigIpAddrType_Object = MibScalar
olsrv2PreviousOrigIpAddrType = _Olsrv2PreviousOrigIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 0, 2, 1),
    _Olsrv2PreviousOrigIpAddrType_Type()
)
olsrv2PreviousOrigIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2PreviousOrigIpAddrType.setStatus("current")


class _Olsrv2PreviousOrigIpAddr_Type(InetAddress):
    """Custom type olsrv2PreviousOrigIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2PreviousOrigIpAddr_Type.__name__ = "InetAddress"
_Olsrv2PreviousOrigIpAddr_Object = MibScalar
olsrv2PreviousOrigIpAddr = _Olsrv2PreviousOrigIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 0, 2, 2),
    _Olsrv2PreviousOrigIpAddr_Type()
)
olsrv2PreviousOrigIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2PreviousOrigIpAddr.setStatus("current")
_Olsrv2MIBObjects_ObjectIdentity = ObjectIdentity
olsrv2MIBObjects = _Olsrv2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 1)
)
_Olsrv2ConfigurationGroup_ObjectIdentity = ObjectIdentity
olsrv2ConfigurationGroup = _Olsrv2ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 1, 1)
)


class _Olsrv2AdminStatus_Type(Olsrv2StatusTC):
    """Custom type olsrv2AdminStatus based on Olsrv2StatusTC"""


_Olsrv2AdminStatus_Object = MibScalar
olsrv2AdminStatus = _Olsrv2AdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 1),
    _Olsrv2AdminStatus_Type()
)
olsrv2AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2AdminStatus.setStatus("current")
_Olsrv2InterfaceTable_Object = MibTable
olsrv2InterfaceTable = _Olsrv2InterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 2)
)
if mibBuilder.loadTexts:
    olsrv2InterfaceTable.setStatus("current")
_Olsrv2InterfaceEntry_Object = MibTableRow
olsrv2InterfaceEntry = _Olsrv2InterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    olsrv2InterfaceEntry.setStatus("current")


class _Olsrv2InterfaceAdminStatus_Type(Olsrv2StatusTC):
    """Custom type olsrv2InterfaceAdminStatus based on Olsrv2StatusTC"""


_Olsrv2InterfaceAdminStatus_Object = MibTableColumn
olsrv2InterfaceAdminStatus = _Olsrv2InterfaceAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 2, 1, 1),
    _Olsrv2InterfaceAdminStatus_Type()
)
olsrv2InterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrv2InterfaceAdminStatus.setStatus("current")


class _Olsrv2OrigIpAddrType_Type(InetAddressType):
    """Custom type olsrv2OrigIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2OrigIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2OrigIpAddrType_Object = MibScalar
olsrv2OrigIpAddrType = _Olsrv2OrigIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 3),
    _Olsrv2OrigIpAddrType_Type()
)
olsrv2OrigIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2OrigIpAddrType.setStatus("current")


class _Olsrv2OrigIpAddr_Type(InetAddress):
    """Custom type olsrv2OrigIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2OrigIpAddr_Type.__name__ = "InetAddress"
_Olsrv2OrigIpAddr_Object = MibScalar
olsrv2OrigIpAddr = _Olsrv2OrigIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 4),
    _Olsrv2OrigIpAddr_Type()
)
olsrv2OrigIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2OrigIpAddr.setStatus("current")


class _Olsrv2OHoldTime_Type(Unsigned32):
    """Custom type olsrv2OHoldTime based on Unsigned32"""
    defaultValue = 30000


_Olsrv2OHoldTime_Object = MibScalar
olsrv2OHoldTime = _Olsrv2OHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 5),
    _Olsrv2OHoldTime_Type()
)
olsrv2OHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2OHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2OHoldTime.setUnits("milliseconds")


class _Olsrv2TcInterval_Type(Olsrv2TimeValueCompressedForm32TC):
    """Custom type olsrv2TcInterval based on Olsrv2TimeValueCompressedForm32TC"""
    defaultValue = 5000


_Olsrv2TcInterval_Object = MibScalar
olsrv2TcInterval = _Olsrv2TcInterval_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 6),
    _Olsrv2TcInterval_Type()
)
olsrv2TcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2TcInterval.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TcInterval.setUnits("milliseconds")


class _Olsrv2TcMinInterval_Type(Olsrv2TimeValueCompressedForm32TC):
    """Custom type olsrv2TcMinInterval based on Olsrv2TimeValueCompressedForm32TC"""
    defaultValue = 1250


_Olsrv2TcMinInterval_Object = MibScalar
olsrv2TcMinInterval = _Olsrv2TcMinInterval_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 7),
    _Olsrv2TcMinInterval_Type()
)
olsrv2TcMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2TcMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TcMinInterval.setUnits("milliseconds")


class _Olsrv2THoldTime_Type(Olsrv2TimeValueCompressedForm32TC):
    """Custom type olsrv2THoldTime based on Olsrv2TimeValueCompressedForm32TC"""
    defaultValue = 15000


_Olsrv2THoldTime_Object = MibScalar
olsrv2THoldTime = _Olsrv2THoldTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 8),
    _Olsrv2THoldTime_Type()
)
olsrv2THoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2THoldTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2THoldTime.setUnits("milliseconds")


class _Olsrv2AHoldTime_Type(Olsrv2TimeValueCompressedForm32TC):
    """Custom type olsrv2AHoldTime based on Olsrv2TimeValueCompressedForm32TC"""
    defaultValue = 15000


_Olsrv2AHoldTime_Object = MibScalar
olsrv2AHoldTime = _Olsrv2AHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 9),
    _Olsrv2AHoldTime_Type()
)
olsrv2AHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2AHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2AHoldTime.setUnits("milliseconds")


class _Olsrv2RxHoldTime_Type(Unsigned32):
    """Custom type olsrv2RxHoldTime based on Unsigned32"""
    defaultValue = 30000


_Olsrv2RxHoldTime_Object = MibScalar
olsrv2RxHoldTime = _Olsrv2RxHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 10),
    _Olsrv2RxHoldTime_Type()
)
olsrv2RxHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2RxHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2RxHoldTime.setUnits("milliseconds")


class _Olsrv2PHoldTime_Type(Unsigned32):
    """Custom type olsrv2PHoldTime based on Unsigned32"""
    defaultValue = 30000


_Olsrv2PHoldTime_Object = MibScalar
olsrv2PHoldTime = _Olsrv2PHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 11),
    _Olsrv2PHoldTime_Type()
)
olsrv2PHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2PHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2PHoldTime.setUnits("milliseconds")


class _Olsrv2FHoldTime_Type(Unsigned32):
    """Custom type olsrv2FHoldTime based on Unsigned32"""
    defaultValue = 30000


_Olsrv2FHoldTime_Object = MibScalar
olsrv2FHoldTime = _Olsrv2FHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 12),
    _Olsrv2FHoldTime_Type()
)
olsrv2FHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2FHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2FHoldTime.setUnits("milliseconds")


class _Olsrv2TpMaxJitter_Type(Unsigned32):
    """Custom type olsrv2TpMaxJitter based on Unsigned32"""
    defaultValue = 500


_Olsrv2TpMaxJitter_Object = MibScalar
olsrv2TpMaxJitter = _Olsrv2TpMaxJitter_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 13),
    _Olsrv2TpMaxJitter_Type()
)
olsrv2TpMaxJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2TpMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TpMaxJitter.setUnits("milliseconds")


class _Olsrv2TtMaxJitter_Type(Unsigned32):
    """Custom type olsrv2TtMaxJitter based on Unsigned32"""
    defaultValue = 500


_Olsrv2TtMaxJitter_Object = MibScalar
olsrv2TtMaxJitter = _Olsrv2TtMaxJitter_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 14),
    _Olsrv2TtMaxJitter_Type()
)
olsrv2TtMaxJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2TtMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TtMaxJitter.setUnits("milliseconds")


class _Olsrv2FMaxJitter_Type(Unsigned32):
    """Custom type olsrv2FMaxJitter based on Unsigned32"""
    defaultValue = 500


_Olsrv2FMaxJitter_Object = MibScalar
olsrv2FMaxJitter = _Olsrv2FMaxJitter_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 15),
    _Olsrv2FMaxJitter_Type()
)
olsrv2FMaxJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2FMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2FMaxJitter.setUnits("milliseconds")


class _Olsrv2TcHopLimit_Type(Unsigned32):
    """Custom type olsrv2TcHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Olsrv2TcHopLimit_Type.__name__ = "Unsigned32"
_Olsrv2TcHopLimit_Object = MibScalar
olsrv2TcHopLimit = _Olsrv2TcHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 16),
    _Olsrv2TcHopLimit_Type()
)
olsrv2TcHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2TcHopLimit.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TcHopLimit.setUnits("hops")


class _Olsrv2WillRouting_Type(WillingnessTC):
    """Custom type olsrv2WillRouting based on WillingnessTC"""
    defaultValue = 7


_Olsrv2WillRouting_Object = MibScalar
olsrv2WillRouting = _Olsrv2WillRouting_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 17),
    _Olsrv2WillRouting_Type()
)
olsrv2WillRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2WillRouting.setStatus("current")


class _Olsrv2WillFlooding_Type(WillingnessTC):
    """Custom type olsrv2WillFlooding based on WillingnessTC"""
    defaultValue = 7


_Olsrv2WillFlooding_Object = MibScalar
olsrv2WillFlooding = _Olsrv2WillFlooding_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 18),
    _Olsrv2WillFlooding_Type()
)
olsrv2WillFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2WillFlooding.setStatus("current")


class _Olsrv2LinkMetricType_Type(IANAolsrv2LinkMetricTypeTC):
    """Custom type olsrv2LinkMetricType based on IANAolsrv2LinkMetricTypeTC"""


_Olsrv2LinkMetricType_Object = MibScalar
olsrv2LinkMetricType = _Olsrv2LinkMetricType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 1, 19),
    _Olsrv2LinkMetricType_Type()
)
olsrv2LinkMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2LinkMetricType.setStatus("current")
_Olsrv2StateGroup_ObjectIdentity = ObjectIdentity
olsrv2StateGroup = _Olsrv2StateGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 1, 2)
)
_Olsrv2IibLinkSetTable_Object = MibTable
olsrv2IibLinkSetTable = _Olsrv2IibLinkSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 1)
)
if mibBuilder.loadTexts:
    olsrv2IibLinkSetTable.setStatus("current")
_Olsrv2IibLinkSetEntry_Object = MibTableRow
olsrv2IibLinkSetEntry = _Olsrv2IibLinkSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    olsrv2IibLinkSetEntry.setStatus("current")
_Olsrv2IibLinkSetInMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2IibLinkSetInMetricValue_Object = MibTableColumn
olsrv2IibLinkSetInMetricValue = _Olsrv2IibLinkSetInMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 1, 1, 1),
    _Olsrv2IibLinkSetInMetricValue_Type()
)
olsrv2IibLinkSetInMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IibLinkSetInMetricValue.setStatus("current")
_Olsrv2IibLinkSetOutMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2IibLinkSetOutMetricValue_Object = MibTableColumn
olsrv2IibLinkSetOutMetricValue = _Olsrv2IibLinkSetOutMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 1, 1, 2),
    _Olsrv2IibLinkSetOutMetricValue_Type()
)
olsrv2IibLinkSetOutMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrv2IibLinkSetOutMetricValue.setStatus("current")
_Olsrv2IibLinkSetMprSelector_Type = TruthValue
_Olsrv2IibLinkSetMprSelector_Object = MibTableColumn
olsrv2IibLinkSetMprSelector = _Olsrv2IibLinkSetMprSelector_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 1, 1, 3),
    _Olsrv2IibLinkSetMprSelector_Type()
)
olsrv2IibLinkSetMprSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IibLinkSetMprSelector.setStatus("current")
_Olsrv2Iib2HopSetTable_Object = MibTable
olsrv2Iib2HopSetTable = _Olsrv2Iib2HopSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 2)
)
if mibBuilder.loadTexts:
    olsrv2Iib2HopSetTable.setStatus("current")
_Olsrv2Iib2HopSetEntry_Object = MibTableRow
olsrv2Iib2HopSetEntry = _Olsrv2Iib2HopSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    olsrv2Iib2HopSetEntry.setStatus("current")
_Olsrv2Iib2HopSetInMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2Iib2HopSetInMetricValue_Object = MibTableColumn
olsrv2Iib2HopSetInMetricValue = _Olsrv2Iib2HopSetInMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 2, 1, 1),
    _Olsrv2Iib2HopSetInMetricValue_Type()
)
olsrv2Iib2HopSetInMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2Iib2HopSetInMetricValue.setStatus("current")
_Olsrv2Iib2HopSetOutMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2Iib2HopSetOutMetricValue_Object = MibTableColumn
olsrv2Iib2HopSetOutMetricValue = _Olsrv2Iib2HopSetOutMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 2, 1, 2),
    _Olsrv2Iib2HopSetOutMetricValue_Type()
)
olsrv2Iib2HopSetOutMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2Iib2HopSetOutMetricValue.setStatus("current")
_Olsrv2LibOrigSetTable_Object = MibTable
olsrv2LibOrigSetTable = _Olsrv2LibOrigSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 3)
)
if mibBuilder.loadTexts:
    olsrv2LibOrigSetTable.setStatus("current")
_Olsrv2LibOrigSetEntry_Object = MibTableRow
olsrv2LibOrigSetEntry = _Olsrv2LibOrigSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 3, 1)
)
olsrv2LibOrigSetEntry.setIndexNames(
    (0, "OLSRv2-MIB", "olsrv2LibOrigSetIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2LibOrigSetIpAddr"),
)
if mibBuilder.loadTexts:
    olsrv2LibOrigSetEntry.setStatus("current")


class _Olsrv2LibOrigSetIpAddrType_Type(InetAddressType):
    """Custom type olsrv2LibOrigSetIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2LibOrigSetIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2LibOrigSetIpAddrType_Object = MibTableColumn
olsrv2LibOrigSetIpAddrType = _Olsrv2LibOrigSetIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 3, 1, 1),
    _Olsrv2LibOrigSetIpAddrType_Type()
)
olsrv2LibOrigSetIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2LibOrigSetIpAddrType.setStatus("current")


class _Olsrv2LibOrigSetIpAddr_Type(InetAddress):
    """Custom type olsrv2LibOrigSetIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2LibOrigSetIpAddr_Type.__name__ = "InetAddress"
_Olsrv2LibOrigSetIpAddr_Object = MibTableColumn
olsrv2LibOrigSetIpAddr = _Olsrv2LibOrigSetIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 3, 1, 2),
    _Olsrv2LibOrigSetIpAddr_Type()
)
olsrv2LibOrigSetIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2LibOrigSetIpAddr.setStatus("current")
_Olsrv2LibOrigSetExpireTime_Type = TimeStamp
_Olsrv2LibOrigSetExpireTime_Object = MibTableColumn
olsrv2LibOrigSetExpireTime = _Olsrv2LibOrigSetExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 3, 1, 3),
    _Olsrv2LibOrigSetExpireTime_Type()
)
olsrv2LibOrigSetExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2LibOrigSetExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2LibOrigSetExpireTime.setUnits("centiseconds")
_Olsrv2LibLocAttNetSetTable_Object = MibTable
olsrv2LibLocAttNetSetTable = _Olsrv2LibLocAttNetSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 4)
)
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetTable.setStatus("current")
_Olsrv2LibLocAttNetSetEntry_Object = MibTableRow
olsrv2LibLocAttNetSetEntry = _Olsrv2LibLocAttNetSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 4, 1)
)
olsrv2LibLocAttNetSetEntry.setIndexNames(
    (0, "OLSRv2-MIB", "olsrv2LibLocAttNetSetIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2LibLocAttNetSetIpAddr"),
    (0, "OLSRv2-MIB", "olsrv2LibLocAttNetSetIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetEntry.setStatus("current")


class _Olsrv2LibLocAttNetSetIpAddrType_Type(InetAddressType):
    """Custom type olsrv2LibLocAttNetSetIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2LibLocAttNetSetIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2LibLocAttNetSetIpAddrType_Object = MibTableColumn
olsrv2LibLocAttNetSetIpAddrType = _Olsrv2LibLocAttNetSetIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 4, 1, 1),
    _Olsrv2LibLocAttNetSetIpAddrType_Type()
)
olsrv2LibLocAttNetSetIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetIpAddrType.setStatus("current")


class _Olsrv2LibLocAttNetSetIpAddr_Type(InetAddress):
    """Custom type olsrv2LibLocAttNetSetIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2LibLocAttNetSetIpAddr_Type.__name__ = "InetAddress"
_Olsrv2LibLocAttNetSetIpAddr_Object = MibTableColumn
olsrv2LibLocAttNetSetIpAddr = _Olsrv2LibLocAttNetSetIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 4, 1, 2),
    _Olsrv2LibLocAttNetSetIpAddr_Type()
)
olsrv2LibLocAttNetSetIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetIpAddr.setStatus("current")
_Olsrv2LibLocAttNetSetIpAddrPrefixLen_Type = InetAddressPrefixLength
_Olsrv2LibLocAttNetSetIpAddrPrefixLen_Object = MibTableColumn
olsrv2LibLocAttNetSetIpAddrPrefixLen = _Olsrv2LibLocAttNetSetIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 4, 1, 3),
    _Olsrv2LibLocAttNetSetIpAddrPrefixLen_Type()
)
olsrv2LibLocAttNetSetIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetIpAddrPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetIpAddrPrefixLen.setUnits("bits")


class _Olsrv2LibLocAttNetSetDistance_Type(Unsigned32):
    """Custom type olsrv2LibLocAttNetSetDistance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Olsrv2LibLocAttNetSetDistance_Type.__name__ = "Unsigned32"
_Olsrv2LibLocAttNetSetDistance_Object = MibTableColumn
olsrv2LibLocAttNetSetDistance = _Olsrv2LibLocAttNetSetDistance_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 4, 1, 4),
    _Olsrv2LibLocAttNetSetDistance_Type()
)
olsrv2LibLocAttNetSetDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetDistance.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetDistance.setUnits("hops")
_Olsrv2LibLocAttNetSetMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2LibLocAttNetSetMetricValue_Object = MibTableColumn
olsrv2LibLocAttNetSetMetricValue = _Olsrv2LibLocAttNetSetMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 4, 1, 5),
    _Olsrv2LibLocAttNetSetMetricValue_Type()
)
olsrv2LibLocAttNetSetMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2LibLocAttNetSetMetricValue.setStatus("current")
_Olsrv2NibNeighborSetTable_Object = MibTable
olsrv2NibNeighborSetTable = _Olsrv2NibNeighborSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5)
)
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetTable.setStatus("current")
_Olsrv2NibNeighborSetEntry_Object = MibTableRow
olsrv2NibNeighborSetEntry = _Olsrv2NibNeighborSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetEntry.setStatus("current")


class _Olsrv2NibNeighborSetNOrigIpAddrType_Type(InetAddressType):
    """Custom type olsrv2NibNeighborSetNOrigIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2NibNeighborSetNOrigIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2NibNeighborSetNOrigIpAddrType_Object = MibTableColumn
olsrv2NibNeighborSetNOrigIpAddrType = _Olsrv2NibNeighborSetNOrigIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 1),
    _Olsrv2NibNeighborSetNOrigIpAddrType_Type()
)
olsrv2NibNeighborSetNOrigIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNOrigIpAddrType.setStatus("current")


class _Olsrv2NibNeighborSetNOrigIpAddr_Type(InetAddress):
    """Custom type olsrv2NibNeighborSetNOrigIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2NibNeighborSetNOrigIpAddr_Type.__name__ = "InetAddress"
_Olsrv2NibNeighborSetNOrigIpAddr_Object = MibTableColumn
olsrv2NibNeighborSetNOrigIpAddr = _Olsrv2NibNeighborSetNOrigIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 2),
    _Olsrv2NibNeighborSetNOrigIpAddr_Type()
)
olsrv2NibNeighborSetNOrigIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNOrigIpAddr.setStatus("current")
_Olsrv2NibNeighborSetNInMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2NibNeighborSetNInMetricValue_Object = MibTableColumn
olsrv2NibNeighborSetNInMetricValue = _Olsrv2NibNeighborSetNInMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 3),
    _Olsrv2NibNeighborSetNInMetricValue_Type()
)
olsrv2NibNeighborSetNInMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNInMetricValue.setStatus("current")
_Olsrv2NibNeighborSetNOutMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2NibNeighborSetNOutMetricValue_Object = MibTableColumn
olsrv2NibNeighborSetNOutMetricValue = _Olsrv2NibNeighborSetNOutMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 4),
    _Olsrv2NibNeighborSetNOutMetricValue_Type()
)
olsrv2NibNeighborSetNOutMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNOutMetricValue.setStatus("current")
_Olsrv2NibNeighborSetNWillFlooding_Type = WillingnessTC
_Olsrv2NibNeighborSetNWillFlooding_Object = MibTableColumn
olsrv2NibNeighborSetNWillFlooding = _Olsrv2NibNeighborSetNWillFlooding_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 5),
    _Olsrv2NibNeighborSetNWillFlooding_Type()
)
olsrv2NibNeighborSetNWillFlooding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNWillFlooding.setStatus("current")
_Olsrv2NibNeighborSetNWillRouting_Type = WillingnessTC
_Olsrv2NibNeighborSetNWillRouting_Object = MibTableColumn
olsrv2NibNeighborSetNWillRouting = _Olsrv2NibNeighborSetNWillRouting_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 6),
    _Olsrv2NibNeighborSetNWillRouting_Type()
)
olsrv2NibNeighborSetNWillRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNWillRouting.setStatus("current")
_Olsrv2NibNeighborSetNFloodingMpr_Type = TruthValue
_Olsrv2NibNeighborSetNFloodingMpr_Object = MibTableColumn
olsrv2NibNeighborSetNFloodingMpr = _Olsrv2NibNeighborSetNFloodingMpr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 7),
    _Olsrv2NibNeighborSetNFloodingMpr_Type()
)
olsrv2NibNeighborSetNFloodingMpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNFloodingMpr.setStatus("current")
_Olsrv2NibNeighborSetNRoutingMpr_Type = TruthValue
_Olsrv2NibNeighborSetNRoutingMpr_Object = MibTableColumn
olsrv2NibNeighborSetNRoutingMpr = _Olsrv2NibNeighborSetNRoutingMpr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 8),
    _Olsrv2NibNeighborSetNRoutingMpr_Type()
)
olsrv2NibNeighborSetNRoutingMpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNRoutingMpr.setStatus("current")
_Olsrv2NibNeighborSetNMprSelector_Type = TruthValue
_Olsrv2NibNeighborSetNMprSelector_Object = MibTableColumn
olsrv2NibNeighborSetNMprSelector = _Olsrv2NibNeighborSetNMprSelector_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 9),
    _Olsrv2NibNeighborSetNMprSelector_Type()
)
olsrv2NibNeighborSetNMprSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNMprSelector.setStatus("current")
_Olsrv2NibNeighborSetNAdvertised_Type = TruthValue
_Olsrv2NibNeighborSetNAdvertised_Object = MibTableColumn
olsrv2NibNeighborSetNAdvertised = _Olsrv2NibNeighborSetNAdvertised_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 5, 1, 10),
    _Olsrv2NibNeighborSetNAdvertised_Type()
)
olsrv2NibNeighborSetNAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetNAdvertised.setStatus("current")


class _Olsrv2NibNeighborSetTableAnsn_Type(Unsigned32):
    """Custom type olsrv2NibNeighborSetTableAnsn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Olsrv2NibNeighborSetTableAnsn_Type.__name__ = "Unsigned32"
_Olsrv2NibNeighborSetTableAnsn_Object = MibScalar
olsrv2NibNeighborSetTableAnsn = _Olsrv2NibNeighborSetTableAnsn_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 6),
    _Olsrv2NibNeighborSetTableAnsn_Type()
)
olsrv2NibNeighborSetTableAnsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2NibNeighborSetTableAnsn.setStatus("current")
_Olsrv2TibAdRemoteRouterSetTable_Object = MibTable
olsrv2TibAdRemoteRouterSetTable = _Olsrv2TibAdRemoteRouterSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 7)
)
if mibBuilder.loadTexts:
    olsrv2TibAdRemoteRouterSetTable.setStatus("current")
_Olsrv2TibAdRemoteRouterSetEntry_Object = MibTableRow
olsrv2TibAdRemoteRouterSetEntry = _Olsrv2TibAdRemoteRouterSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 7, 1)
)
olsrv2TibAdRemoteRouterSetEntry.setIndexNames(
    (0, "OLSRv2-MIB", "olsrv2TibAdRemoteRouterSetIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibAdRemoteRouterSetIpAddr"),
)
if mibBuilder.loadTexts:
    olsrv2TibAdRemoteRouterSetEntry.setStatus("current")


class _Olsrv2TibAdRemoteRouterSetIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibAdRemoteRouterSetIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibAdRemoteRouterSetIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibAdRemoteRouterSetIpAddrType_Object = MibTableColumn
olsrv2TibAdRemoteRouterSetIpAddrType = _Olsrv2TibAdRemoteRouterSetIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 7, 1, 1),
    _Olsrv2TibAdRemoteRouterSetIpAddrType_Type()
)
olsrv2TibAdRemoteRouterSetIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibAdRemoteRouterSetIpAddrType.setStatus("current")


class _Olsrv2TibAdRemoteRouterSetIpAddr_Type(InetAddress):
    """Custom type olsrv2TibAdRemoteRouterSetIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibAdRemoteRouterSetIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibAdRemoteRouterSetIpAddr_Object = MibTableColumn
olsrv2TibAdRemoteRouterSetIpAddr = _Olsrv2TibAdRemoteRouterSetIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 7, 1, 2),
    _Olsrv2TibAdRemoteRouterSetIpAddr_Type()
)
olsrv2TibAdRemoteRouterSetIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibAdRemoteRouterSetIpAddr.setStatus("current")


class _Olsrv2TibAdRemoteRouterSetMaxSeqNo_Type(Unsigned32):
    """Custom type olsrv2TibAdRemoteRouterSetMaxSeqNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Olsrv2TibAdRemoteRouterSetMaxSeqNo_Type.__name__ = "Unsigned32"
_Olsrv2TibAdRemoteRouterSetMaxSeqNo_Object = MibTableColumn
olsrv2TibAdRemoteRouterSetMaxSeqNo = _Olsrv2TibAdRemoteRouterSetMaxSeqNo_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 7, 1, 3),
    _Olsrv2TibAdRemoteRouterSetMaxSeqNo_Type()
)
olsrv2TibAdRemoteRouterSetMaxSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibAdRemoteRouterSetMaxSeqNo.setStatus("current")
_Olsrv2TibAdRemoteRouterSetExpireTime_Type = TimeStamp
_Olsrv2TibAdRemoteRouterSetExpireTime_Object = MibTableColumn
olsrv2TibAdRemoteRouterSetExpireTime = _Olsrv2TibAdRemoteRouterSetExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 7, 1, 4),
    _Olsrv2TibAdRemoteRouterSetExpireTime_Type()
)
olsrv2TibAdRemoteRouterSetExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibAdRemoteRouterSetExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibAdRemoteRouterSetExpireTime.setUnits("centiseconds")
_Olsrv2TibRouterTopologySetTable_Object = MibTable
olsrv2TibRouterTopologySetTable = _Olsrv2TibRouterTopologySetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8)
)
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetTable.setStatus("current")
_Olsrv2TibRouterTopologySetEntry_Object = MibTableRow
olsrv2TibRouterTopologySetEntry = _Olsrv2TibRouterTopologySetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1)
)
olsrv2TibRouterTopologySetEntry.setIndexNames(
    (0, "OLSRv2-MIB", "olsrv2TibRouterTopologySetFromOrigIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibRouterTopologySetFromOrigIpAddr"),
    (0, "OLSRv2-MIB", "olsrv2TibRouterTopologySetToOrigIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibRouterTopologySetToOrigIpAddr"),
)
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetEntry.setStatus("current")


class _Olsrv2TibRouterTopologySetFromOrigIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibRouterTopologySetFromOrigIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibRouterTopologySetFromOrigIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibRouterTopologySetFromOrigIpAddrType_Object = MibTableColumn
olsrv2TibRouterTopologySetFromOrigIpAddrType = _Olsrv2TibRouterTopologySetFromOrigIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1, 1),
    _Olsrv2TibRouterTopologySetFromOrigIpAddrType_Type()
)
olsrv2TibRouterTopologySetFromOrigIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetFromOrigIpAddrType.setStatus("current")


class _Olsrv2TibRouterTopologySetFromOrigIpAddr_Type(InetAddress):
    """Custom type olsrv2TibRouterTopologySetFromOrigIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibRouterTopologySetFromOrigIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibRouterTopologySetFromOrigIpAddr_Object = MibTableColumn
olsrv2TibRouterTopologySetFromOrigIpAddr = _Olsrv2TibRouterTopologySetFromOrigIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1, 2),
    _Olsrv2TibRouterTopologySetFromOrigIpAddr_Type()
)
olsrv2TibRouterTopologySetFromOrigIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetFromOrigIpAddr.setStatus("current")


class _Olsrv2TibRouterTopologySetToOrigIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibRouterTopologySetToOrigIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibRouterTopologySetToOrigIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibRouterTopologySetToOrigIpAddrType_Object = MibTableColumn
olsrv2TibRouterTopologySetToOrigIpAddrType = _Olsrv2TibRouterTopologySetToOrigIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1, 3),
    _Olsrv2TibRouterTopologySetToOrigIpAddrType_Type()
)
olsrv2TibRouterTopologySetToOrigIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetToOrigIpAddrType.setStatus("current")


class _Olsrv2TibRouterTopologySetToOrigIpAddr_Type(InetAddress):
    """Custom type olsrv2TibRouterTopologySetToOrigIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibRouterTopologySetToOrigIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibRouterTopologySetToOrigIpAddr_Object = MibTableColumn
olsrv2TibRouterTopologySetToOrigIpAddr = _Olsrv2TibRouterTopologySetToOrigIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1, 4),
    _Olsrv2TibRouterTopologySetToOrigIpAddr_Type()
)
olsrv2TibRouterTopologySetToOrigIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetToOrigIpAddr.setStatus("current")


class _Olsrv2TibRouterTopologySetSeqNo_Type(Unsigned32):
    """Custom type olsrv2TibRouterTopologySetSeqNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Olsrv2TibRouterTopologySetSeqNo_Type.__name__ = "Unsigned32"
_Olsrv2TibRouterTopologySetSeqNo_Object = MibTableColumn
olsrv2TibRouterTopologySetSeqNo = _Olsrv2TibRouterTopologySetSeqNo_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1, 5),
    _Olsrv2TibRouterTopologySetSeqNo_Type()
)
olsrv2TibRouterTopologySetSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetSeqNo.setStatus("current")
_Olsrv2TibRouterTopologySetMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2TibRouterTopologySetMetricValue_Object = MibTableColumn
olsrv2TibRouterTopologySetMetricValue = _Olsrv2TibRouterTopologySetMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1, 6),
    _Olsrv2TibRouterTopologySetMetricValue_Type()
)
olsrv2TibRouterTopologySetMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetMetricValue.setStatus("current")
_Olsrv2TibRouterTopologySetExpireTime_Type = TimeStamp
_Olsrv2TibRouterTopologySetExpireTime_Object = MibTableColumn
olsrv2TibRouterTopologySetExpireTime = _Olsrv2TibRouterTopologySetExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 8, 1, 7),
    _Olsrv2TibRouterTopologySetExpireTime_Type()
)
olsrv2TibRouterTopologySetExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibRouterTopologySetExpireTime.setUnits("centiseconds")
_Olsrv2TibRoutableAddressTopologySetTable_Object = MibTable
olsrv2TibRoutableAddressTopologySetTable = _Olsrv2TibRoutableAddressTopologySetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9)
)
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetTable.setStatus("current")
_Olsrv2TibRoutableAddressTopologySetEntry_Object = MibTableRow
olsrv2TibRoutableAddressTopologySetEntry = _Olsrv2TibRoutableAddressTopologySetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1)
)
olsrv2TibRoutableAddressTopologySetEntry.setIndexNames(
    (0, "OLSRv2-MIB", "olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibRoutableAddressTopologySetFromOrigIpAddr"),
    (0, "OLSRv2-MIB", "olsrv2TibRoutableAddressTopologySetDestIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibRoutableAddressTopologySetDestIpAddr"),
)
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetEntry.setStatus("current")


class _Olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType_Object = MibTableColumn
olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType = _Olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1, 1),
    _Olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType_Type()
)
olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType.setStatus("current")


class _Olsrv2TibRoutableAddressTopologySetFromOrigIpAddr_Type(InetAddress):
    """Custom type olsrv2TibRoutableAddressTopologySetFromOrigIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibRoutableAddressTopologySetFromOrigIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibRoutableAddressTopologySetFromOrigIpAddr_Object = MibTableColumn
olsrv2TibRoutableAddressTopologySetFromOrigIpAddr = _Olsrv2TibRoutableAddressTopologySetFromOrigIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1, 2),
    _Olsrv2TibRoutableAddressTopologySetFromOrigIpAddr_Type()
)
olsrv2TibRoutableAddressTopologySetFromOrigIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetFromOrigIpAddr.setStatus("current")


class _Olsrv2TibRoutableAddressTopologySetDestIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibRoutableAddressTopologySetDestIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibRoutableAddressTopologySetDestIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibRoutableAddressTopologySetDestIpAddrType_Object = MibTableColumn
olsrv2TibRoutableAddressTopologySetDestIpAddrType = _Olsrv2TibRoutableAddressTopologySetDestIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1, 3),
    _Olsrv2TibRoutableAddressTopologySetDestIpAddrType_Type()
)
olsrv2TibRoutableAddressTopologySetDestIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetDestIpAddrType.setStatus("current")


class _Olsrv2TibRoutableAddressTopologySetDestIpAddr_Type(InetAddress):
    """Custom type olsrv2TibRoutableAddressTopologySetDestIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibRoutableAddressTopologySetDestIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibRoutableAddressTopologySetDestIpAddr_Object = MibTableColumn
olsrv2TibRoutableAddressTopologySetDestIpAddr = _Olsrv2TibRoutableAddressTopologySetDestIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1, 4),
    _Olsrv2TibRoutableAddressTopologySetDestIpAddr_Type()
)
olsrv2TibRoutableAddressTopologySetDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetDestIpAddr.setStatus("current")


class _Olsrv2TibRoutableAddressTopologySetSeqNo_Type(Unsigned32):
    """Custom type olsrv2TibRoutableAddressTopologySetSeqNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Olsrv2TibRoutableAddressTopologySetSeqNo_Type.__name__ = "Unsigned32"
_Olsrv2TibRoutableAddressTopologySetSeqNo_Object = MibTableColumn
olsrv2TibRoutableAddressTopologySetSeqNo = _Olsrv2TibRoutableAddressTopologySetSeqNo_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1, 5),
    _Olsrv2TibRoutableAddressTopologySetSeqNo_Type()
)
olsrv2TibRoutableAddressTopologySetSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetSeqNo.setStatus("current")
_Olsrv2TibRoutableAddressTopologySetMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2TibRoutableAddressTopologySetMetricValue_Object = MibTableColumn
olsrv2TibRoutableAddressTopologySetMetricValue = _Olsrv2TibRoutableAddressTopologySetMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1, 6),
    _Olsrv2TibRoutableAddressTopologySetMetricValue_Type()
)
olsrv2TibRoutableAddressTopologySetMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetMetricValue.setStatus("current")
_Olsrv2TibRoutableAddressTopologySetExpireTime_Type = TimeStamp
_Olsrv2TibRoutableAddressTopologySetExpireTime_Object = MibTableColumn
olsrv2TibRoutableAddressTopologySetExpireTime = _Olsrv2TibRoutableAddressTopologySetExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 9, 1, 7),
    _Olsrv2TibRoutableAddressTopologySetExpireTime_Type()
)
olsrv2TibRoutableAddressTopologySetExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibRoutableAddressTopologySetExpireTime.setUnits("centiseconds")
_Olsrv2TibAttNetworksSetTable_Object = MibTable
olsrv2TibAttNetworksSetTable = _Olsrv2TibAttNetworksSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10)
)
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetTable.setStatus("current")
_Olsrv2TibAttNetworksSetEntry_Object = MibTableRow
olsrv2TibAttNetworksSetEntry = _Olsrv2TibAttNetworksSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1)
)
olsrv2TibAttNetworksSetEntry.setIndexNames(
    (0, "OLSRv2-MIB", "olsrv2TibAttNetworksSetOrigIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibAttNetworksSetOrigIpAddr"),
    (0, "OLSRv2-MIB", "olsrv2TibAttNetworksSetNetIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibAttNetworksSetNetIpAddr"),
    (0, "OLSRv2-MIB", "olsrv2TibAttNetworksSetNetIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetEntry.setStatus("current")


class _Olsrv2TibAttNetworksSetOrigIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibAttNetworksSetOrigIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibAttNetworksSetOrigIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibAttNetworksSetOrigIpAddrType_Object = MibTableColumn
olsrv2TibAttNetworksSetOrigIpAddrType = _Olsrv2TibAttNetworksSetOrigIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 1),
    _Olsrv2TibAttNetworksSetOrigIpAddrType_Type()
)
olsrv2TibAttNetworksSetOrigIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetOrigIpAddrType.setStatus("current")


class _Olsrv2TibAttNetworksSetOrigIpAddr_Type(InetAddress):
    """Custom type olsrv2TibAttNetworksSetOrigIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibAttNetworksSetOrigIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibAttNetworksSetOrigIpAddr_Object = MibTableColumn
olsrv2TibAttNetworksSetOrigIpAddr = _Olsrv2TibAttNetworksSetOrigIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 2),
    _Olsrv2TibAttNetworksSetOrigIpAddr_Type()
)
olsrv2TibAttNetworksSetOrigIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetOrigIpAddr.setStatus("current")


class _Olsrv2TibAttNetworksSetNetIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibAttNetworksSetNetIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibAttNetworksSetNetIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibAttNetworksSetNetIpAddrType_Object = MibTableColumn
olsrv2TibAttNetworksSetNetIpAddrType = _Olsrv2TibAttNetworksSetNetIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 3),
    _Olsrv2TibAttNetworksSetNetIpAddrType_Type()
)
olsrv2TibAttNetworksSetNetIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetNetIpAddrType.setStatus("current")


class _Olsrv2TibAttNetworksSetNetIpAddr_Type(InetAddress):
    """Custom type olsrv2TibAttNetworksSetNetIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibAttNetworksSetNetIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibAttNetworksSetNetIpAddr_Object = MibTableColumn
olsrv2TibAttNetworksSetNetIpAddr = _Olsrv2TibAttNetworksSetNetIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 4),
    _Olsrv2TibAttNetworksSetNetIpAddr_Type()
)
olsrv2TibAttNetworksSetNetIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetNetIpAddr.setStatus("current")
_Olsrv2TibAttNetworksSetNetIpAddrPrefixLen_Type = InetAddressPrefixLength
_Olsrv2TibAttNetworksSetNetIpAddrPrefixLen_Object = MibTableColumn
olsrv2TibAttNetworksSetNetIpAddrPrefixLen = _Olsrv2TibAttNetworksSetNetIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 5),
    _Olsrv2TibAttNetworksSetNetIpAddrPrefixLen_Type()
)
olsrv2TibAttNetworksSetNetIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetNetIpAddrPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetNetIpAddrPrefixLen.setUnits("bits")


class _Olsrv2TibAttNetworksSetSeqNo_Type(Unsigned32):
    """Custom type olsrv2TibAttNetworksSetSeqNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Olsrv2TibAttNetworksSetSeqNo_Type.__name__ = "Unsigned32"
_Olsrv2TibAttNetworksSetSeqNo_Object = MibTableColumn
olsrv2TibAttNetworksSetSeqNo = _Olsrv2TibAttNetworksSetSeqNo_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 6),
    _Olsrv2TibAttNetworksSetSeqNo_Type()
)
olsrv2TibAttNetworksSetSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetSeqNo.setStatus("current")


class _Olsrv2TibAttNetworksSetDist_Type(Unsigned32):
    """Custom type olsrv2TibAttNetworksSetDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Olsrv2TibAttNetworksSetDist_Type.__name__ = "Unsigned32"
_Olsrv2TibAttNetworksSetDist_Object = MibTableColumn
olsrv2TibAttNetworksSetDist = _Olsrv2TibAttNetworksSetDist_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 7),
    _Olsrv2TibAttNetworksSetDist_Type()
)
olsrv2TibAttNetworksSetDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetDist.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetDist.setUnits("hops")
_Olsrv2TibAttNetworksSetMetricValue_Type = Olsrv2MetricValueCompressedFormTC
_Olsrv2TibAttNetworksSetMetricValue_Object = MibTableColumn
olsrv2TibAttNetworksSetMetricValue = _Olsrv2TibAttNetworksSetMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 9),
    _Olsrv2TibAttNetworksSetMetricValue_Type()
)
olsrv2TibAttNetworksSetMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetMetricValue.setStatus("current")
_Olsrv2TibAttNetworksSetExpireTime_Type = TimeStamp
_Olsrv2TibAttNetworksSetExpireTime_Object = MibTableColumn
olsrv2TibAttNetworksSetExpireTime = _Olsrv2TibAttNetworksSetExpireTime_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 10, 1, 10),
    _Olsrv2TibAttNetworksSetExpireTime_Type()
)
olsrv2TibAttNetworksSetExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibAttNetworksSetExpireTime.setUnits("centiseconds")
_Olsrv2TibRoutingSetTable_Object = MibTable
olsrv2TibRoutingSetTable = _Olsrv2TibRoutingSetTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11)
)
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetTable.setStatus("current")
_Olsrv2TibRoutingSetEntry_Object = MibTableRow
olsrv2TibRoutingSetEntry = _Olsrv2TibRoutingSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1)
)
olsrv2TibRoutingSetEntry.setIndexNames(
    (0, "OLSRv2-MIB", "olsrv2TibRoutingSetDestIpAddrType"),
    (0, "OLSRv2-MIB", "olsrv2TibRoutingSetDestIpAddr"),
    (0, "OLSRv2-MIB", "olsrv2TibRoutingSetDestIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetEntry.setStatus("current")


class _Olsrv2TibRoutingSetDestIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibRoutingSetDestIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibRoutingSetDestIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibRoutingSetDestIpAddrType_Object = MibTableColumn
olsrv2TibRoutingSetDestIpAddrType = _Olsrv2TibRoutingSetDestIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 1),
    _Olsrv2TibRoutingSetDestIpAddrType_Type()
)
olsrv2TibRoutingSetDestIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetDestIpAddrType.setStatus("current")


class _Olsrv2TibRoutingSetDestIpAddr_Type(InetAddress):
    """Custom type olsrv2TibRoutingSetDestIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibRoutingSetDestIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibRoutingSetDestIpAddr_Object = MibTableColumn
olsrv2TibRoutingSetDestIpAddr = _Olsrv2TibRoutingSetDestIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 2),
    _Olsrv2TibRoutingSetDestIpAddr_Type()
)
olsrv2TibRoutingSetDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetDestIpAddr.setStatus("current")
_Olsrv2TibRoutingSetDestIpAddrPrefixLen_Type = InetAddressPrefixLength
_Olsrv2TibRoutingSetDestIpAddrPrefixLen_Object = MibTableColumn
olsrv2TibRoutingSetDestIpAddrPrefixLen = _Olsrv2TibRoutingSetDestIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 3),
    _Olsrv2TibRoutingSetDestIpAddrPrefixLen_Type()
)
olsrv2TibRoutingSetDestIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetDestIpAddrPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetDestIpAddrPrefixLen.setUnits("bits")


class _Olsrv2TibRoutingSetNextIfIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibRoutingSetNextIfIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibRoutingSetNextIfIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibRoutingSetNextIfIpAddrType_Object = MibTableColumn
olsrv2TibRoutingSetNextIfIpAddrType = _Olsrv2TibRoutingSetNextIfIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 4),
    _Olsrv2TibRoutingSetNextIfIpAddrType_Type()
)
olsrv2TibRoutingSetNextIfIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetNextIfIpAddrType.setStatus("current")


class _Olsrv2TibRoutingSetNextIfIpAddr_Type(InetAddress):
    """Custom type olsrv2TibRoutingSetNextIfIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibRoutingSetNextIfIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibRoutingSetNextIfIpAddr_Object = MibTableColumn
olsrv2TibRoutingSetNextIfIpAddr = _Olsrv2TibRoutingSetNextIfIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 5),
    _Olsrv2TibRoutingSetNextIfIpAddr_Type()
)
olsrv2TibRoutingSetNextIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetNextIfIpAddr.setStatus("current")


class _Olsrv2TibRoutingSetLocalIfIpAddrType_Type(InetAddressType):
    """Custom type olsrv2TibRoutingSetLocalIfIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
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


_Olsrv2TibRoutingSetLocalIfIpAddrType_Type.__name__ = "InetAddressType"
_Olsrv2TibRoutingSetLocalIfIpAddrType_Object = MibTableColumn
olsrv2TibRoutingSetLocalIfIpAddrType = _Olsrv2TibRoutingSetLocalIfIpAddrType_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 6),
    _Olsrv2TibRoutingSetLocalIfIpAddrType_Type()
)
olsrv2TibRoutingSetLocalIfIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetLocalIfIpAddrType.setStatus("current")


class _Olsrv2TibRoutingSetLocalIfIpAddr_Type(InetAddress):
    """Custom type olsrv2TibRoutingSetLocalIfIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Olsrv2TibRoutingSetLocalIfIpAddr_Type.__name__ = "InetAddress"
_Olsrv2TibRoutingSetLocalIfIpAddr_Object = MibTableColumn
olsrv2TibRoutingSetLocalIfIpAddr = _Olsrv2TibRoutingSetLocalIfIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 7),
    _Olsrv2TibRoutingSetLocalIfIpAddr_Type()
)
olsrv2TibRoutingSetLocalIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetLocalIfIpAddr.setStatus("current")


class _Olsrv2TibRoutingSetDist_Type(Unsigned32):
    """Custom type olsrv2TibRoutingSetDist based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Olsrv2TibRoutingSetDist_Type.__name__ = "Unsigned32"
_Olsrv2TibRoutingSetDist_Object = MibTableColumn
olsrv2TibRoutingSetDist = _Olsrv2TibRoutingSetDist_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 8),
    _Olsrv2TibRoutingSetDist_Type()
)
olsrv2TibRoutingSetDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetDist.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetDist.setUnits("hops")


class _Olsrv2TibRoutingSetMetricValue_Type(Unsigned32):
    """Custom type olsrv2TibRoutingSetMetricValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294901760),
    )


_Olsrv2TibRoutingSetMetricValue_Type.__name__ = "Unsigned32"
_Olsrv2TibRoutingSetMetricValue_Object = MibTableColumn
olsrv2TibRoutingSetMetricValue = _Olsrv2TibRoutingSetMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 2, 11, 1, 9),
    _Olsrv2TibRoutingSetMetricValue_Type()
)
olsrv2TibRoutingSetMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2TibRoutingSetMetricValue.setStatus("current")
_Olsrv2PerformanceObjGrp_ObjectIdentity = ObjectIdentity
olsrv2PerformanceObjGrp = _Olsrv2PerformanceObjGrp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 1, 3)
)
_Olsrv2InterfacePerfTable_Object = MibTable
olsrv2InterfacePerfTable = _Olsrv2InterfacePerfTable_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1)
)
if mibBuilder.loadTexts:
    olsrv2InterfacePerfTable.setStatus("current")
_Olsrv2InterfacePerfEntry_Object = MibTableRow
olsrv2InterfacePerfEntry = _Olsrv2InterfacePerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    olsrv2InterfacePerfEntry.setStatus("current")
_Olsrv2IfTcMessageXmits_Type = Counter32
_Olsrv2IfTcMessageXmits_Object = MibTableColumn
olsrv2IfTcMessageXmits = _Olsrv2IfTcMessageXmits_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 1),
    _Olsrv2IfTcMessageXmits_Type()
)
olsrv2IfTcMessageXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageXmits.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageXmits.setUnits("messages")
_Olsrv2IfTcMessageRecvd_Type = Counter32
_Olsrv2IfTcMessageRecvd_Object = MibTableColumn
olsrv2IfTcMessageRecvd = _Olsrv2IfTcMessageRecvd_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 2),
    _Olsrv2IfTcMessageRecvd_Type()
)
olsrv2IfTcMessageRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageRecvd.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageRecvd.setUnits("messages")
_Olsrv2IfTcMessageXmitAccumulatedSize_Type = Counter64
_Olsrv2IfTcMessageXmitAccumulatedSize_Object = MibTableColumn
olsrv2IfTcMessageXmitAccumulatedSize = _Olsrv2IfTcMessageXmitAccumulatedSize_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 3),
    _Olsrv2IfTcMessageXmitAccumulatedSize_Type()
)
olsrv2IfTcMessageXmitAccumulatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageXmitAccumulatedSize.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageXmitAccumulatedSize.setUnits("octets")
_Olsrv2IfTcMessageRecvdAccumulatedSize_Type = Counter64
_Olsrv2IfTcMessageRecvdAccumulatedSize_Object = MibTableColumn
olsrv2IfTcMessageRecvdAccumulatedSize = _Olsrv2IfTcMessageRecvdAccumulatedSize_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 4),
    _Olsrv2IfTcMessageRecvdAccumulatedSize_Type()
)
olsrv2IfTcMessageRecvdAccumulatedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageRecvdAccumulatedSize.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageRecvdAccumulatedSize.setUnits("octets")
_Olsrv2IfTcMessageTriggeredXmits_Type = Counter32
_Olsrv2IfTcMessageTriggeredXmits_Object = MibTableColumn
olsrv2IfTcMessageTriggeredXmits = _Olsrv2IfTcMessageTriggeredXmits_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 5),
    _Olsrv2IfTcMessageTriggeredXmits_Type()
)
olsrv2IfTcMessageTriggeredXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageTriggeredXmits.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageTriggeredXmits.setUnits("messages")
_Olsrv2IfTcMessagePeriodicXmits_Type = Counter32
_Olsrv2IfTcMessagePeriodicXmits_Object = MibTableColumn
olsrv2IfTcMessagePeriodicXmits = _Olsrv2IfTcMessagePeriodicXmits_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 6),
    _Olsrv2IfTcMessagePeriodicXmits_Type()
)
olsrv2IfTcMessagePeriodicXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessagePeriodicXmits.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessagePeriodicXmits.setUnits("messages")
_Olsrv2IfTcMessageForwardedXmits_Type = Counter32
_Olsrv2IfTcMessageForwardedXmits_Object = MibTableColumn
olsrv2IfTcMessageForwardedXmits = _Olsrv2IfTcMessageForwardedXmits_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 7),
    _Olsrv2IfTcMessageForwardedXmits_Type()
)
olsrv2IfTcMessageForwardedXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageForwardedXmits.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageForwardedXmits.setUnits("messages")
_Olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount_Type = Counter32
_Olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount_Object = MibTableColumn
olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount = _Olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 1, 1, 8),
    _Olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount_Type()
)
olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount.setUnits("advertised MPR selectors")
_Olsrv2RoutingSetRecalculationCount_Type = Counter32
_Olsrv2RoutingSetRecalculationCount_Object = MibScalar
olsrv2RoutingSetRecalculationCount = _Olsrv2RoutingSetRecalculationCount_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 2),
    _Olsrv2RoutingSetRecalculationCount_Type()
)
olsrv2RoutingSetRecalculationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2RoutingSetRecalculationCount.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2RoutingSetRecalculationCount.setUnits("recalculations")
_Olsrv2MPRSetRecalculationCount_Type = Counter32
_Olsrv2MPRSetRecalculationCount_Object = MibScalar
olsrv2MPRSetRecalculationCount = _Olsrv2MPRSetRecalculationCount_Object(
    (1, 3, 6, 1, 2, 1, 219, 1, 3, 3),
    _Olsrv2MPRSetRecalculationCount_Type()
)
olsrv2MPRSetRecalculationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olsrv2MPRSetRecalculationCount.setStatus("current")
if mibBuilder.loadTexts:
    olsrv2MPRSetRecalculationCount.setUnits("recalculations")
_Olsrv2MIBConformance_ObjectIdentity = ObjectIdentity
olsrv2MIBConformance = _Olsrv2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 2)
)
_Olsrv2Compliances_ObjectIdentity = ObjectIdentity
olsrv2Compliances = _Olsrv2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 2, 1)
)
_Olsrv2MIBGroups_ObjectIdentity = ObjectIdentity
olsrv2MIBGroups = _Olsrv2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 219, 2, 2)
)
nhdpInterfaceEntry.registerAugmentions(
    ("OLSRv2-MIB",
     "olsrv2InterfaceEntry")
)
olsrv2InterfaceEntry.setIndexNames(*nhdpInterfaceEntry.getIndexNames())
nhdpIibLinkSetEntry.registerAugmentions(
    ("OLSRv2-MIB",
     "olsrv2IibLinkSetEntry")
)
olsrv2IibLinkSetEntry.setIndexNames(*nhdpIibLinkSetEntry.getIndexNames())
nhdpIib2HopSetEntry.registerAugmentions(
    ("OLSRv2-MIB",
     "olsrv2Iib2HopSetEntry")
)
olsrv2Iib2HopSetEntry.setIndexNames(*nhdpIib2HopSetEntry.getIndexNames())
nhdpNibNeighborSetEntry.registerAugmentions(
    ("OLSRv2-MIB",
     "olsrv2NibNeighborSetEntry")
)
olsrv2NibNeighborSetEntry.setIndexNames(*nhdpNibNeighborSetEntry.getIndexNames())
nhdpInterfacePerfEntry.registerAugmentions(
    ("OLSRv2-MIB",
     "olsrv2InterfacePerfEntry")
)
olsrv2InterfacePerfEntry.setIndexNames(*nhdpInterfacePerfEntry.getIndexNames())

# Managed Objects groups

olsrv2ConfigObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 219, 2, 2, 1)
)
olsrv2ConfigObjectsGroup.setObjects(
      *(("OLSRv2-MIB", "olsrv2AdminStatus"),
        ("OLSRv2-MIB", "olsrv2InterfaceAdminStatus"),
        ("OLSRv2-MIB", "olsrv2OrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2OrigIpAddr"),
        ("OLSRv2-MIB", "olsrv2OHoldTime"),
        ("OLSRv2-MIB", "olsrv2TcInterval"),
        ("OLSRv2-MIB", "olsrv2TcMinInterval"),
        ("OLSRv2-MIB", "olsrv2THoldTime"),
        ("OLSRv2-MIB", "olsrv2AHoldTime"),
        ("OLSRv2-MIB", "olsrv2RxHoldTime"),
        ("OLSRv2-MIB", "olsrv2PHoldTime"),
        ("OLSRv2-MIB", "olsrv2FHoldTime"),
        ("OLSRv2-MIB", "olsrv2TpMaxJitter"),
        ("OLSRv2-MIB", "olsrv2TtMaxJitter"),
        ("OLSRv2-MIB", "olsrv2FMaxJitter"),
        ("OLSRv2-MIB", "olsrv2TcHopLimit"),
        ("OLSRv2-MIB", "olsrv2WillFlooding"),
        ("OLSRv2-MIB", "olsrv2WillRouting"),
        ("OLSRv2-MIB", "olsrv2LinkMetricType"))
)
if mibBuilder.loadTexts:
    olsrv2ConfigObjectsGroup.setStatus("current")

olsrv2StateObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 219, 2, 2, 2)
)
olsrv2StateObjectsGroup.setObjects(
      *(("OLSRv2-MIB", "olsrv2LibOrigSetExpireTime"),
        ("OLSRv2-MIB", "olsrv2LibLocAttNetSetDistance"),
        ("OLSRv2-MIB", "olsrv2LibLocAttNetSetMetricValue"),
        ("OLSRv2-MIB", "olsrv2IibLinkSetInMetricValue"),
        ("OLSRv2-MIB", "olsrv2IibLinkSetOutMetricValue"),
        ("OLSRv2-MIB", "olsrv2IibLinkSetMprSelector"),
        ("OLSRv2-MIB", "olsrv2Iib2HopSetInMetricValue"),
        ("OLSRv2-MIB", "olsrv2Iib2HopSetOutMetricValue"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNOrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNOrigIpAddr"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNInMetricValue"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNOutMetricValue"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNWillFlooding"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNWillRouting"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNFloodingMpr"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNRoutingMpr"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNMprSelector"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetNAdvertised"),
        ("OLSRv2-MIB", "olsrv2NibNeighborSetTableAnsn"),
        ("OLSRv2-MIB", "olsrv2TibAdRemoteRouterSetMaxSeqNo"),
        ("OLSRv2-MIB", "olsrv2TibAdRemoteRouterSetExpireTime"),
        ("OLSRv2-MIB", "olsrv2TibRouterTopologySetSeqNo"),
        ("OLSRv2-MIB", "olsrv2TibRouterTopologySetMetricValue"),
        ("OLSRv2-MIB", "olsrv2TibRouterTopologySetExpireTime"),
        ("OLSRv2-MIB", "olsrv2TibRoutableAddressTopologySetExpireTime"),
        ("OLSRv2-MIB", "olsrv2TibRoutableAddressTopologySetSeqNo"),
        ("OLSRv2-MIB", "olsrv2TibRoutableAddressTopologySetMetricValue"),
        ("OLSRv2-MIB", "olsrv2TibAttNetworksSetSeqNo"),
        ("OLSRv2-MIB", "olsrv2TibAttNetworksSetDist"),
        ("OLSRv2-MIB", "olsrv2TibAttNetworksSetMetricValue"),
        ("OLSRv2-MIB", "olsrv2TibAttNetworksSetExpireTime"),
        ("OLSRv2-MIB", "olsrv2TibRoutingSetNextIfIpAddrType"),
        ("OLSRv2-MIB", "olsrv2TibRoutingSetNextIfIpAddr"),
        ("OLSRv2-MIB", "olsrv2TibRoutingSetLocalIfIpAddrType"),
        ("OLSRv2-MIB", "olsrv2TibRoutingSetLocalIfIpAddr"),
        ("OLSRv2-MIB", "olsrv2TibRoutingSetDist"),
        ("OLSRv2-MIB", "olsrv2TibRoutingSetMetricValue"))
)
if mibBuilder.loadTexts:
    olsrv2StateObjectsGroup.setStatus("current")

olsrv2PerfObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 219, 2, 2, 3)
)
olsrv2PerfObjectsGroup.setObjects(
      *(("OLSRv2-MIB", "olsrv2IfTcMessageXmits"),
        ("OLSRv2-MIB", "olsrv2IfTcMessageRecvd"),
        ("OLSRv2-MIB", "olsrv2IfTcMessageXmitAccumulatedSize"),
        ("OLSRv2-MIB", "olsrv2IfTcMessageRecvdAccumulatedSize"),
        ("OLSRv2-MIB", "olsrv2IfTcMessageTriggeredXmits"),
        ("OLSRv2-MIB", "olsrv2IfTcMessagePeriodicXmits"),
        ("OLSRv2-MIB", "olsrv2IfTcMessageForwardedXmits"),
        ("OLSRv2-MIB", "olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount"),
        ("OLSRv2-MIB", "olsrv2RoutingSetRecalculationCount"),
        ("OLSRv2-MIB", "olsrv2MPRSetRecalculationCount"))
)
if mibBuilder.loadTexts:
    olsrv2PerfObjectsGroup.setStatus("current")

olsrv2NotificationsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 219, 2, 2, 4)
)
olsrv2NotificationsObjectsGroup.setObjects(
      *(("OLSRv2-MIB", "olsrv2RoutingSetRecalculationCountThreshold"),
        ("OLSRv2-MIB", "olsrv2RoutingSetRecalculationCountWindow"),
        ("OLSRv2-MIB", "olsrv2MPRSetRecalculationCountThreshold"),
        ("OLSRv2-MIB", "olsrv2MPRSetRecalculationCountWindow"),
        ("OLSRv2-MIB", "olsrv2PreviousOrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2PreviousOrigIpAddr"))
)
if mibBuilder.loadTexts:
    olsrv2NotificationsObjectsGroup.setStatus("current")


# Notification objects

olsrv2RouterStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 219, 0, 0, 1)
)
olsrv2RouterStatusChange.setObjects(
      *(("OLSRv2-MIB", "olsrv2OrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2OrigIpAddr"),
        ("OLSRv2-MIB", "olsrv2AdminStatus"))
)
if mibBuilder.loadTexts:
    olsrv2RouterStatusChange.setStatus(
        "current"
    )

olsrv2OrigIpAddrChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 219, 0, 0, 2)
)
olsrv2OrigIpAddrChange.setObjects(
      *(("OLSRv2-MIB", "olsrv2OrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2OrigIpAddr"),
        ("OLSRv2-MIB", "olsrv2PreviousOrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2PreviousOrigIpAddr"))
)
if mibBuilder.loadTexts:
    olsrv2OrigIpAddrChange.setStatus(
        "current"
    )

olsrv2RoutingSetRecalculationCountChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 219, 0, 0, 3)
)
olsrv2RoutingSetRecalculationCountChange.setObjects(
      *(("OLSRv2-MIB", "olsrv2OrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2OrigIpAddr"),
        ("OLSRv2-MIB", "olsrv2RoutingSetRecalculationCount"))
)
if mibBuilder.loadTexts:
    olsrv2RoutingSetRecalculationCountChange.setStatus(
        "current"
    )

olsrv2MPRSetRecalculationCountChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 219, 0, 0, 4)
)
olsrv2MPRSetRecalculationCountChange.setObjects(
      *(("OLSRv2-MIB", "olsrv2OrigIpAddrType"),
        ("OLSRv2-MIB", "olsrv2OrigIpAddr"),
        ("OLSRv2-MIB", "olsrv2MPRSetRecalculationCount"))
)
if mibBuilder.loadTexts:
    olsrv2MPRSetRecalculationCountChange.setStatus(
        "current"
    )


# Notifications groups

olsrv2NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 219, 2, 2, 5)
)
olsrv2NotificationsGroup.setObjects(
      *(("OLSRv2-MIB", "olsrv2RouterStatusChange"),
        ("OLSRv2-MIB", "olsrv2OrigIpAddrChange"),
        ("OLSRv2-MIB", "olsrv2RoutingSetRecalculationCountChange"),
        ("OLSRv2-MIB", "olsrv2MPRSetRecalculationCountChange"))
)
if mibBuilder.loadTexts:
    olsrv2NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

olsrv2BasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 219, 2, 1, 1)
)
if mibBuilder.loadTexts:
    olsrv2BasicCompliance.setStatus(
        "current"
    )

olsrv2FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 219, 2, 1, 2)
)
if mibBuilder.loadTexts:
    olsrv2FullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLSRv2-MIB",
    **{"Olsrv2MetricValueCompressedFormTC": Olsrv2MetricValueCompressedFormTC,
       "Olsrv2TimeValueCompressedForm32TC": Olsrv2TimeValueCompressedForm32TC,
       "Olsrv2StatusTC": Olsrv2StatusTC,
       "WillingnessTC": WillingnessTC,
       "manetOlsrv2MIB": manetOlsrv2MIB,
       "olsrv2MIBNotifications": olsrv2MIBNotifications,
       "olsrv2NotificationsObjects": olsrv2NotificationsObjects,
       "olsrv2RouterStatusChange": olsrv2RouterStatusChange,
       "olsrv2OrigIpAddrChange": olsrv2OrigIpAddrChange,
       "olsrv2RoutingSetRecalculationCountChange": olsrv2RoutingSetRecalculationCountChange,
       "olsrv2MPRSetRecalculationCountChange": olsrv2MPRSetRecalculationCountChange,
       "olsrv2NotificationsControl": olsrv2NotificationsControl,
       "olsrv2RoutingSetRecalculationCountThreshold": olsrv2RoutingSetRecalculationCountThreshold,
       "olsrv2RoutingSetRecalculationCountWindow": olsrv2RoutingSetRecalculationCountWindow,
       "olsrv2MPRSetRecalculationCountThreshold": olsrv2MPRSetRecalculationCountThreshold,
       "olsrv2MPRSetRecalculationCountWindow": olsrv2MPRSetRecalculationCountWindow,
       "olsrv2NotificationsStates": olsrv2NotificationsStates,
       "olsrv2PreviousOrigIpAddrType": olsrv2PreviousOrigIpAddrType,
       "olsrv2PreviousOrigIpAddr": olsrv2PreviousOrigIpAddr,
       "olsrv2MIBObjects": olsrv2MIBObjects,
       "olsrv2ConfigurationGroup": olsrv2ConfigurationGroup,
       "olsrv2AdminStatus": olsrv2AdminStatus,
       "olsrv2InterfaceTable": olsrv2InterfaceTable,
       "olsrv2InterfaceEntry": olsrv2InterfaceEntry,
       "olsrv2InterfaceAdminStatus": olsrv2InterfaceAdminStatus,
       "olsrv2OrigIpAddrType": olsrv2OrigIpAddrType,
       "olsrv2OrigIpAddr": olsrv2OrigIpAddr,
       "olsrv2OHoldTime": olsrv2OHoldTime,
       "olsrv2TcInterval": olsrv2TcInterval,
       "olsrv2TcMinInterval": olsrv2TcMinInterval,
       "olsrv2THoldTime": olsrv2THoldTime,
       "olsrv2AHoldTime": olsrv2AHoldTime,
       "olsrv2RxHoldTime": olsrv2RxHoldTime,
       "olsrv2PHoldTime": olsrv2PHoldTime,
       "olsrv2FHoldTime": olsrv2FHoldTime,
       "olsrv2TpMaxJitter": olsrv2TpMaxJitter,
       "olsrv2TtMaxJitter": olsrv2TtMaxJitter,
       "olsrv2FMaxJitter": olsrv2FMaxJitter,
       "olsrv2TcHopLimit": olsrv2TcHopLimit,
       "olsrv2WillRouting": olsrv2WillRouting,
       "olsrv2WillFlooding": olsrv2WillFlooding,
       "olsrv2LinkMetricType": olsrv2LinkMetricType,
       "olsrv2StateGroup": olsrv2StateGroup,
       "olsrv2IibLinkSetTable": olsrv2IibLinkSetTable,
       "olsrv2IibLinkSetEntry": olsrv2IibLinkSetEntry,
       "olsrv2IibLinkSetInMetricValue": olsrv2IibLinkSetInMetricValue,
       "olsrv2IibLinkSetOutMetricValue": olsrv2IibLinkSetOutMetricValue,
       "olsrv2IibLinkSetMprSelector": olsrv2IibLinkSetMprSelector,
       "olsrv2Iib2HopSetTable": olsrv2Iib2HopSetTable,
       "olsrv2Iib2HopSetEntry": olsrv2Iib2HopSetEntry,
       "olsrv2Iib2HopSetInMetricValue": olsrv2Iib2HopSetInMetricValue,
       "olsrv2Iib2HopSetOutMetricValue": olsrv2Iib2HopSetOutMetricValue,
       "olsrv2LibOrigSetTable": olsrv2LibOrigSetTable,
       "olsrv2LibOrigSetEntry": olsrv2LibOrigSetEntry,
       "olsrv2LibOrigSetIpAddrType": olsrv2LibOrigSetIpAddrType,
       "olsrv2LibOrigSetIpAddr": olsrv2LibOrigSetIpAddr,
       "olsrv2LibOrigSetExpireTime": olsrv2LibOrigSetExpireTime,
       "olsrv2LibLocAttNetSetTable": olsrv2LibLocAttNetSetTable,
       "olsrv2LibLocAttNetSetEntry": olsrv2LibLocAttNetSetEntry,
       "olsrv2LibLocAttNetSetIpAddrType": olsrv2LibLocAttNetSetIpAddrType,
       "olsrv2LibLocAttNetSetIpAddr": olsrv2LibLocAttNetSetIpAddr,
       "olsrv2LibLocAttNetSetIpAddrPrefixLen": olsrv2LibLocAttNetSetIpAddrPrefixLen,
       "olsrv2LibLocAttNetSetDistance": olsrv2LibLocAttNetSetDistance,
       "olsrv2LibLocAttNetSetMetricValue": olsrv2LibLocAttNetSetMetricValue,
       "olsrv2NibNeighborSetTable": olsrv2NibNeighborSetTable,
       "olsrv2NibNeighborSetEntry": olsrv2NibNeighborSetEntry,
       "olsrv2NibNeighborSetNOrigIpAddrType": olsrv2NibNeighborSetNOrigIpAddrType,
       "olsrv2NibNeighborSetNOrigIpAddr": olsrv2NibNeighborSetNOrigIpAddr,
       "olsrv2NibNeighborSetNInMetricValue": olsrv2NibNeighborSetNInMetricValue,
       "olsrv2NibNeighborSetNOutMetricValue": olsrv2NibNeighborSetNOutMetricValue,
       "olsrv2NibNeighborSetNWillFlooding": olsrv2NibNeighborSetNWillFlooding,
       "olsrv2NibNeighborSetNWillRouting": olsrv2NibNeighborSetNWillRouting,
       "olsrv2NibNeighborSetNFloodingMpr": olsrv2NibNeighborSetNFloodingMpr,
       "olsrv2NibNeighborSetNRoutingMpr": olsrv2NibNeighborSetNRoutingMpr,
       "olsrv2NibNeighborSetNMprSelector": olsrv2NibNeighborSetNMprSelector,
       "olsrv2NibNeighborSetNAdvertised": olsrv2NibNeighborSetNAdvertised,
       "olsrv2NibNeighborSetTableAnsn": olsrv2NibNeighborSetTableAnsn,
       "olsrv2TibAdRemoteRouterSetTable": olsrv2TibAdRemoteRouterSetTable,
       "olsrv2TibAdRemoteRouterSetEntry": olsrv2TibAdRemoteRouterSetEntry,
       "olsrv2TibAdRemoteRouterSetIpAddrType": olsrv2TibAdRemoteRouterSetIpAddrType,
       "olsrv2TibAdRemoteRouterSetIpAddr": olsrv2TibAdRemoteRouterSetIpAddr,
       "olsrv2TibAdRemoteRouterSetMaxSeqNo": olsrv2TibAdRemoteRouterSetMaxSeqNo,
       "olsrv2TibAdRemoteRouterSetExpireTime": olsrv2TibAdRemoteRouterSetExpireTime,
       "olsrv2TibRouterTopologySetTable": olsrv2TibRouterTopologySetTable,
       "olsrv2TibRouterTopologySetEntry": olsrv2TibRouterTopologySetEntry,
       "olsrv2TibRouterTopologySetFromOrigIpAddrType": olsrv2TibRouterTopologySetFromOrigIpAddrType,
       "olsrv2TibRouterTopologySetFromOrigIpAddr": olsrv2TibRouterTopologySetFromOrigIpAddr,
       "olsrv2TibRouterTopologySetToOrigIpAddrType": olsrv2TibRouterTopologySetToOrigIpAddrType,
       "olsrv2TibRouterTopologySetToOrigIpAddr": olsrv2TibRouterTopologySetToOrigIpAddr,
       "olsrv2TibRouterTopologySetSeqNo": olsrv2TibRouterTopologySetSeqNo,
       "olsrv2TibRouterTopologySetMetricValue": olsrv2TibRouterTopologySetMetricValue,
       "olsrv2TibRouterTopologySetExpireTime": olsrv2TibRouterTopologySetExpireTime,
       "olsrv2TibRoutableAddressTopologySetTable": olsrv2TibRoutableAddressTopologySetTable,
       "olsrv2TibRoutableAddressTopologySetEntry": olsrv2TibRoutableAddressTopologySetEntry,
       "olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType": olsrv2TibRoutableAddressTopologySetFromOrigIpAddrType,
       "olsrv2TibRoutableAddressTopologySetFromOrigIpAddr": olsrv2TibRoutableAddressTopologySetFromOrigIpAddr,
       "olsrv2TibRoutableAddressTopologySetDestIpAddrType": olsrv2TibRoutableAddressTopologySetDestIpAddrType,
       "olsrv2TibRoutableAddressTopologySetDestIpAddr": olsrv2TibRoutableAddressTopologySetDestIpAddr,
       "olsrv2TibRoutableAddressTopologySetSeqNo": olsrv2TibRoutableAddressTopologySetSeqNo,
       "olsrv2TibRoutableAddressTopologySetMetricValue": olsrv2TibRoutableAddressTopologySetMetricValue,
       "olsrv2TibRoutableAddressTopologySetExpireTime": olsrv2TibRoutableAddressTopologySetExpireTime,
       "olsrv2TibAttNetworksSetTable": olsrv2TibAttNetworksSetTable,
       "olsrv2TibAttNetworksSetEntry": olsrv2TibAttNetworksSetEntry,
       "olsrv2TibAttNetworksSetOrigIpAddrType": olsrv2TibAttNetworksSetOrigIpAddrType,
       "olsrv2TibAttNetworksSetOrigIpAddr": olsrv2TibAttNetworksSetOrigIpAddr,
       "olsrv2TibAttNetworksSetNetIpAddrType": olsrv2TibAttNetworksSetNetIpAddrType,
       "olsrv2TibAttNetworksSetNetIpAddr": olsrv2TibAttNetworksSetNetIpAddr,
       "olsrv2TibAttNetworksSetNetIpAddrPrefixLen": olsrv2TibAttNetworksSetNetIpAddrPrefixLen,
       "olsrv2TibAttNetworksSetSeqNo": olsrv2TibAttNetworksSetSeqNo,
       "olsrv2TibAttNetworksSetDist": olsrv2TibAttNetworksSetDist,
       "olsrv2TibAttNetworksSetMetricValue": olsrv2TibAttNetworksSetMetricValue,
       "olsrv2TibAttNetworksSetExpireTime": olsrv2TibAttNetworksSetExpireTime,
       "olsrv2TibRoutingSetTable": olsrv2TibRoutingSetTable,
       "olsrv2TibRoutingSetEntry": olsrv2TibRoutingSetEntry,
       "olsrv2TibRoutingSetDestIpAddrType": olsrv2TibRoutingSetDestIpAddrType,
       "olsrv2TibRoutingSetDestIpAddr": olsrv2TibRoutingSetDestIpAddr,
       "olsrv2TibRoutingSetDestIpAddrPrefixLen": olsrv2TibRoutingSetDestIpAddrPrefixLen,
       "olsrv2TibRoutingSetNextIfIpAddrType": olsrv2TibRoutingSetNextIfIpAddrType,
       "olsrv2TibRoutingSetNextIfIpAddr": olsrv2TibRoutingSetNextIfIpAddr,
       "olsrv2TibRoutingSetLocalIfIpAddrType": olsrv2TibRoutingSetLocalIfIpAddrType,
       "olsrv2TibRoutingSetLocalIfIpAddr": olsrv2TibRoutingSetLocalIfIpAddr,
       "olsrv2TibRoutingSetDist": olsrv2TibRoutingSetDist,
       "olsrv2TibRoutingSetMetricValue": olsrv2TibRoutingSetMetricValue,
       "olsrv2PerformanceObjGrp": olsrv2PerformanceObjGrp,
       "olsrv2InterfacePerfTable": olsrv2InterfacePerfTable,
       "olsrv2InterfacePerfEntry": olsrv2InterfacePerfEntry,
       "olsrv2IfTcMessageXmits": olsrv2IfTcMessageXmits,
       "olsrv2IfTcMessageRecvd": olsrv2IfTcMessageRecvd,
       "olsrv2IfTcMessageXmitAccumulatedSize": olsrv2IfTcMessageXmitAccumulatedSize,
       "olsrv2IfTcMessageRecvdAccumulatedSize": olsrv2IfTcMessageRecvdAccumulatedSize,
       "olsrv2IfTcMessageTriggeredXmits": olsrv2IfTcMessageTriggeredXmits,
       "olsrv2IfTcMessagePeriodicXmits": olsrv2IfTcMessagePeriodicXmits,
       "olsrv2IfTcMessageForwardedXmits": olsrv2IfTcMessageForwardedXmits,
       "olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount": olsrv2IfTcMessageXmitAccumulatedMPRSelectorCount,
       "olsrv2RoutingSetRecalculationCount": olsrv2RoutingSetRecalculationCount,
       "olsrv2MPRSetRecalculationCount": olsrv2MPRSetRecalculationCount,
       "olsrv2MIBConformance": olsrv2MIBConformance,
       "olsrv2Compliances": olsrv2Compliances,
       "olsrv2BasicCompliance": olsrv2BasicCompliance,
       "olsrv2FullCompliance": olsrv2FullCompliance,
       "olsrv2MIBGroups": olsrv2MIBGroups,
       "olsrv2ConfigObjectsGroup": olsrv2ConfigObjectsGroup,
       "olsrv2StateObjectsGroup": olsrv2StateObjectsGroup,
       "olsrv2PerfObjectsGroup": olsrv2PerfObjectsGroup,
       "olsrv2NotificationsObjectsGroup": olsrv2NotificationsObjectsGroup,
       "olsrv2NotificationsGroup": olsrv2NotificationsGroup}
)
