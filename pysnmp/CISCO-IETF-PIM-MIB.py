# SNMP MIB module (CISCO-IETF-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:49 2024
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

(cIpMRouteAddrType,
 cIpMRouteGroup,
 cIpMRouteNextHopAddrType,
 cIpMRouteNextHopAddress,
 cIpMRouteNextHopGroup,
 cIpMRouteNextHopIfIndex,
 cIpMRouteNextHopSource,
 cIpMRouteNextHopSourceMask,
 cIpMRouteSource,
 cIpMRouteSourceMask) = mibBuilder.importSymbols(
    "CISCO-IETF-IPMROUTE-MIB",
    "cIpMRouteAddrType",
    "cIpMRouteGroup",
    "cIpMRouteNextHopAddrType",
    "cIpMRouteNextHopAddress",
    "cIpMRouteNextHopGroup",
    "cIpMRouteNextHopIfIndex",
    "cIpMRouteNextHopSource",
    "cIpMRouteNextHopSourceMask",
    "cIpMRouteSource",
    "cIpMRouteSourceMask")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 119)
)
ciscoIetfPimMIB.setRevisions(
        ("2005-02-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CPimNotifs_ObjectIdentity = ObjectIdentity
cPimNotifs = _CPimNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 0)
)
_CPimMIBObjects_ObjectIdentity = ObjectIdentity
cPimMIBObjects = _CPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1)
)
_CPim_ObjectIdentity = ObjectIdentity
cPim = _CPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1)
)


class _CPimJoinPruneInterval_Type(Unsigned32):
    """Custom type cPimJoinPruneInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPimJoinPruneInterval_Type.__name__ = "Unsigned32"
_CPimJoinPruneInterval_Object = MibScalar
cPimJoinPruneInterval = _CPimJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 1),
    _CPimJoinPruneInterval_Type()
)
cPimJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPimJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    cPimJoinPruneInterval.setUnits("seconds")
_CPimIfTable_Object = MibTable
cPimIfTable = _CPimIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cPimIfTable.setStatus("current")
_CPimIfEntry_Object = MibTableRow
cPimIfEntry = _CPimIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1)
)
cPimIfEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-MIB", "cPimIfIndex"),
    (0, "CISCO-IETF-PIM-MIB", "cPimIfInetVersion"),
)
if mibBuilder.loadTexts:
    cPimIfEntry.setStatus("current")
_CPimIfIndex_Type = InterfaceIndex
_CPimIfIndex_Object = MibTableColumn
cPimIfIndex = _CPimIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 1),
    _CPimIfIndex_Type()
)
cPimIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimIfIndex.setStatus("current")
_CPimIfInetVersion_Type = InetVersion
_CPimIfInetVersion_Object = MibTableColumn
cPimIfInetVersion = _CPimIfInetVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 2),
    _CPimIfInetVersion_Type()
)
cPimIfInetVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimIfInetVersion.setStatus("current")
_CPimIfAddressType_Type = InetAddressType
_CPimIfAddressType_Object = MibTableColumn
cPimIfAddressType = _CPimIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 3),
    _CPimIfAddressType_Type()
)
cPimIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimIfAddressType.setStatus("current")


class _CPimIfAddress_Type(InetAddress):
    """Custom type cPimIfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimIfAddress_Type.__name__ = "InetAddress"
_CPimIfAddress_Object = MibTableColumn
cPimIfAddress = _CPimIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 4),
    _CPimIfAddress_Type()
)
cPimIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimIfAddress.setStatus("current")
_CPimIfNetMask_Type = InetAddressPrefixLength
_CPimIfNetMask_Object = MibTableColumn
cPimIfNetMask = _CPimIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 5),
    _CPimIfNetMask_Type()
)
cPimIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimIfNetMask.setStatus("current")


class _CPimIfMode_Type(Integer32):
    """Custom type cPimIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2),
          ("sparseDense", 3))
    )


_CPimIfMode_Type.__name__ = "Integer32"
_CPimIfMode_Object = MibTableColumn
cPimIfMode = _CPimIfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 6),
    _CPimIfMode_Type()
)
cPimIfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimIfMode.setStatus("current")


class _CPimIfDR_Type(InetAddress):
    """Custom type cPimIfDR based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimIfDR_Type.__name__ = "InetAddress"
_CPimIfDR_Object = MibTableColumn
cPimIfDR = _CPimIfDR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 7),
    _CPimIfDR_Type()
)
cPimIfDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimIfDR.setStatus("current")


class _CPimIfHelloInterval_Type(Unsigned32):
    """Custom type cPimIfHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPimIfHelloInterval_Type.__name__ = "Unsigned32"
_CPimIfHelloInterval_Object = MibTableColumn
cPimIfHelloInterval = _CPimIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 8),
    _CPimIfHelloInterval_Type()
)
cPimIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    cPimIfHelloInterval.setUnits("seconds")


class _CPimIfJoinPruneInterval_Type(Unsigned32):
    """Custom type cPimIfJoinPruneInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPimIfJoinPruneInterval_Type.__name__ = "Unsigned32"
_CPimIfJoinPruneInterval_Object = MibTableColumn
cPimIfJoinPruneInterval = _CPimIfJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 9),
    _CPimIfJoinPruneInterval_Type()
)
cPimIfJoinPruneInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimIfJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    cPimIfJoinPruneInterval.setUnits("seconds")


class _CPimIfCBSRPreference_Type(Integer32):
    """Custom type cPimIfCBSRPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CPimIfCBSRPreference_Type.__name__ = "Integer32"
_CPimIfCBSRPreference_Object = MibTableColumn
cPimIfCBSRPreference = _CPimIfCBSRPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 10),
    _CPimIfCBSRPreference_Type()
)
cPimIfCBSRPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimIfCBSRPreference.setStatus("current")
_CPimIfStatus_Type = RowStatus
_CPimIfStatus_Object = MibTableColumn
cPimIfStatus = _CPimIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 2, 1, 11),
    _CPimIfStatus_Type()
)
cPimIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimIfStatus.setStatus("current")
_CPimNbrTable_Object = MibTable
cPimNbrTable = _CPimNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cPimNbrTable.setStatus("current")
_CPimNbrEntry_Object = MibTableRow
cPimNbrEntry = _CPimNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 3, 1)
)
cPimNbrEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-MIB", "cPimNbrIfIndex"),
    (0, "CISCO-IETF-PIM-MIB", "cPimNbrAddressType"),
    (0, "CISCO-IETF-PIM-MIB", "cPimNbrAddress"),
)
if mibBuilder.loadTexts:
    cPimNbrEntry.setStatus("current")
_CPimNbrIfIndex_Type = InterfaceIndex
_CPimNbrIfIndex_Object = MibTableColumn
cPimNbrIfIndex = _CPimNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 3, 1, 1),
    _CPimNbrIfIndex_Type()
)
cPimNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimNbrIfIndex.setStatus("current")
_CPimNbrAddressType_Type = InetAddressType
_CPimNbrAddressType_Object = MibTableColumn
cPimNbrAddressType = _CPimNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 3, 1, 2),
    _CPimNbrAddressType_Type()
)
cPimNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimNbrAddressType.setStatus("current")


class _CPimNbrAddress_Type(InetAddress):
    """Custom type cPimNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimNbrAddress_Type.__name__ = "InetAddress"
_CPimNbrAddress_Object = MibTableColumn
cPimNbrAddress = _CPimNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 3, 1, 3),
    _CPimNbrAddress_Type()
)
cPimNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimNbrAddress.setStatus("current")
_CPimNbrUpTime_Type = TimeTicks
_CPimNbrUpTime_Object = MibTableColumn
cPimNbrUpTime = _CPimNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 3, 1, 4),
    _CPimNbrUpTime_Type()
)
cPimNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimNbrUpTime.setStatus("current")
_CPimNbrExpiryTime_Type = TimeTicks
_CPimNbrExpiryTime_Object = MibTableColumn
cPimNbrExpiryTime = _CPimNbrExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 3, 1, 5),
    _CPimNbrExpiryTime_Type()
)
cPimNbrExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimNbrExpiryTime.setStatus("current")
_CPimInetMRouteTable_Object = MibTable
cPimInetMRouteTable = _CPimInetMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cPimInetMRouteTable.setStatus("current")
_CPimInetMRouteEntry_Object = MibTableRow
cPimInetMRouteEntry = _CPimInetMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 4, 1)
)
cPimInetMRouteEntry.setIndexNames(
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteAddrType"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteGroup"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteSource"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    cPimInetMRouteEntry.setStatus("current")
_CPimInetMRouteUpstreamAssertTime_Type = TimeTicks
_CPimInetMRouteUpstreamAssertTime_Object = MibTableColumn
cPimInetMRouteUpstreamAssertTime = _CPimInetMRouteUpstreamAssertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 4, 1, 1),
    _CPimInetMRouteUpstreamAssertTime_Type()
)
cPimInetMRouteUpstreamAssertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimInetMRouteUpstreamAssertTime.setStatus("current")


class _CPimInetMRouteAssertMetric_Type(Unsigned32):
    """Custom type cPimInetMRouteAssertMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CPimInetMRouteAssertMetric_Type.__name__ = "Unsigned32"
_CPimInetMRouteAssertMetric_Object = MibTableColumn
cPimInetMRouteAssertMetric = _CPimInetMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 4, 1, 2),
    _CPimInetMRouteAssertMetric_Type()
)
cPimInetMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimInetMRouteAssertMetric.setStatus("current")


class _CPimInetMRouteAssertMetricPref_Type(Unsigned32):
    """Custom type cPimInetMRouteAssertMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CPimInetMRouteAssertMetricPref_Type.__name__ = "Unsigned32"
_CPimInetMRouteAssertMetricPref_Object = MibTableColumn
cPimInetMRouteAssertMetricPref = _CPimInetMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 4, 1, 3),
    _CPimInetMRouteAssertMetricPref_Type()
)
cPimInetMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimInetMRouteAssertMetricPref.setStatus("current")
_CPimInetMRouteAssertRPTBit_Type = TruthValue
_CPimInetMRouteAssertRPTBit_Object = MibTableColumn
cPimInetMRouteAssertRPTBit = _CPimInetMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 4, 1, 4),
    _CPimInetMRouteAssertRPTBit_Type()
)
cPimInetMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimInetMRouteAssertRPTBit.setStatus("current")


class _CPimInetMRouteFlags_Type(Bits):
    """Custom type cPimInetMRouteFlags based on Bits"""
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )

_CPimInetMRouteFlags_Type.__name__ = "Bits"
_CPimInetMRouteFlags_Object = MibTableColumn
cPimInetMRouteFlags = _CPimInetMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 4, 1, 5),
    _CPimInetMRouteFlags_Type()
)
cPimInetMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimInetMRouteFlags.setStatus("current")
_CPimInetMRouteNextHopTable_Object = MibTable
cPimInetMRouteNextHopTable = _CPimInetMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cPimInetMRouteNextHopTable.setStatus("current")
_CPimInetMRouteNextHopEntry_Object = MibTableRow
cPimInetMRouteNextHopEntry = _CPimInetMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 5, 1)
)
cPimInetMRouteNextHopEntry.setIndexNames(
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopAddrType"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopGroup"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopSource"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopSourceMask"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopIfIndex"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    cPimInetMRouteNextHopEntry.setStatus("current")


class _CPimInetMRouteNextHopPruneReason_Type(Integer32):
    """Custom type cPimInetMRouteNextHopPruneReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assert", 3),
          ("other", 1),
          ("prune", 2))
    )


_CPimInetMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_CPimInetMRouteNextHopPruneReason_Object = MibTableColumn
cPimInetMRouteNextHopPruneReason = _CPimInetMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 5, 1, 2),
    _CPimInetMRouteNextHopPruneReason_Type()
)
cPimInetMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimInetMRouteNextHopPruneReason.setStatus("current")
_CPimRPMapTable_Object = MibTable
cPimRPMapTable = _CPimRPMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cPimRPMapTable.setStatus("current")
_CPimRPMapEntry_Object = MibTableRow
cPimRPMapEntry = _CPimRPMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1)
)
cPimRPMapEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-MIB", "cPimRPMapComponent"),
    (0, "CISCO-IETF-PIM-MIB", "cPimRPMapAddrType"),
    (0, "CISCO-IETF-PIM-MIB", "cPimRPMapGroupAddress"),
    (0, "CISCO-IETF-PIM-MIB", "cPimRPMapGroupMask"),
    (0, "CISCO-IETF-PIM-MIB", "cPimRPMapAddress"),
)
if mibBuilder.loadTexts:
    cPimRPMapEntry.setStatus("current")


class _CPimRPMapComponent_Type(Unsigned32):
    """Custom type cPimRPMapComponent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CPimRPMapComponent_Type.__name__ = "Unsigned32"
_CPimRPMapComponent_Object = MibTableColumn
cPimRPMapComponent = _CPimRPMapComponent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1, 1),
    _CPimRPMapComponent_Type()
)
cPimRPMapComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimRPMapComponent.setStatus("current")
_CPimRPMapAddrType_Type = InetAddressType
_CPimRPMapAddrType_Object = MibTableColumn
cPimRPMapAddrType = _CPimRPMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1, 2),
    _CPimRPMapAddrType_Type()
)
cPimRPMapAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimRPMapAddrType.setStatus("current")


class _CPimRPMapGroupAddress_Type(InetAddress):
    """Custom type cPimRPMapGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimRPMapGroupAddress_Type.__name__ = "InetAddress"
_CPimRPMapGroupAddress_Object = MibTableColumn
cPimRPMapGroupAddress = _CPimRPMapGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1, 3),
    _CPimRPMapGroupAddress_Type()
)
cPimRPMapGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimRPMapGroupAddress.setStatus("current")
_CPimRPMapGroupMask_Type = InetAddressPrefixLength
_CPimRPMapGroupMask_Object = MibTableColumn
cPimRPMapGroupMask = _CPimRPMapGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1, 4),
    _CPimRPMapGroupMask_Type()
)
cPimRPMapGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimRPMapGroupMask.setStatus("current")


class _CPimRPMapAddress_Type(InetAddress):
    """Custom type cPimRPMapAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimRPMapAddress_Type.__name__ = "InetAddress"
_CPimRPMapAddress_Object = MibTableColumn
cPimRPMapAddress = _CPimRPMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1, 5),
    _CPimRPMapAddress_Type()
)
cPimRPMapAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimRPMapAddress.setStatus("current")


class _CPimRPMapHoldTime_Type(Unsigned32):
    """Custom type cPimRPMapHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPimRPMapHoldTime_Type.__name__ = "Unsigned32"
_CPimRPMapHoldTime_Object = MibTableColumn
cPimRPMapHoldTime = _CPimRPMapHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1, 6),
    _CPimRPMapHoldTime_Type()
)
cPimRPMapHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimRPMapHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cPimRPMapHoldTime.setUnits("seconds")
_CPimRPMapExpiryTime_Type = TimeTicks
_CPimRPMapExpiryTime_Object = MibTableColumn
cPimRPMapExpiryTime = _CPimRPMapExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 6, 1, 7),
    _CPimRPMapExpiryTime_Type()
)
cPimRPMapExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPimRPMapExpiryTime.setStatus("current")
_CPimCRPTable_Object = MibTable
cPimCRPTable = _CPimCRPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cPimCRPTable.setStatus("current")
_CPimCRPEntry_Object = MibTableRow
cPimCRPEntry = _CPimCRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 7, 1)
)
cPimCRPEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-MIB", "cPimCRPAddrType"),
    (0, "CISCO-IETF-PIM-MIB", "cPimCRPGroupAddress"),
    (0, "CISCO-IETF-PIM-MIB", "cPimCRPGroupMask"),
)
if mibBuilder.loadTexts:
    cPimCRPEntry.setStatus("current")
_CPimCRPAddrType_Type = InetAddressType
_CPimCRPAddrType_Object = MibTableColumn
cPimCRPAddrType = _CPimCRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 7, 1, 1),
    _CPimCRPAddrType_Type()
)
cPimCRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimCRPAddrType.setStatus("current")


class _CPimCRPGroupAddress_Type(InetAddress):
    """Custom type cPimCRPGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimCRPGroupAddress_Type.__name__ = "InetAddress"
_CPimCRPGroupAddress_Object = MibTableColumn
cPimCRPGroupAddress = _CPimCRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 7, 1, 2),
    _CPimCRPGroupAddress_Type()
)
cPimCRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimCRPGroupAddress.setStatus("current")
_CPimCRPGroupMask_Type = InetAddressPrefixLength
_CPimCRPGroupMask_Object = MibTableColumn
cPimCRPGroupMask = _CPimCRPGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 7, 1, 3),
    _CPimCRPGroupMask_Type()
)
cPimCRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimCRPGroupMask.setStatus("current")


class _CPimCRPAddress_Type(InetAddress):
    """Custom type cPimCRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimCRPAddress_Type.__name__ = "InetAddress"
_CPimCRPAddress_Object = MibTableColumn
cPimCRPAddress = _CPimCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 7, 1, 4),
    _CPimCRPAddress_Type()
)
cPimCRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimCRPAddress.setStatus("current")
_CPimCRPRowStatus_Type = RowStatus
_CPimCRPRowStatus_Object = MibTableColumn
cPimCRPRowStatus = _CPimCRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 7, 1, 5),
    _CPimCRPRowStatus_Type()
)
cPimCRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimCRPRowStatus.setStatus("current")
_CPimComponentTable_Object = MibTable
cPimComponentTable = _CPimComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cPimComponentTable.setStatus("current")
_CPimComponentEntry_Object = MibTableRow
cPimComponentEntry = _CPimComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8, 1)
)
cPimComponentEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-MIB", "cPimComponentIndex"),
)
if mibBuilder.loadTexts:
    cPimComponentEntry.setStatus("current")


class _CPimComponentIndex_Type(Unsigned32):
    """Custom type cPimComponentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CPimComponentIndex_Type.__name__ = "Unsigned32"
_CPimComponentIndex_Object = MibTableColumn
cPimComponentIndex = _CPimComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8, 1, 1),
    _CPimComponentIndex_Type()
)
cPimComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPimComponentIndex.setStatus("current")
_CPimComponentBSRAddrType_Type = InetAddressType
_CPimComponentBSRAddrType_Object = MibTableColumn
cPimComponentBSRAddrType = _CPimComponentBSRAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8, 1, 2),
    _CPimComponentBSRAddrType_Type()
)
cPimComponentBSRAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimComponentBSRAddrType.setStatus("current")


class _CPimComponentBSRAddress_Type(InetAddress):
    """Custom type cPimComponentBSRAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CPimComponentBSRAddress_Type.__name__ = "InetAddress"
_CPimComponentBSRAddress_Object = MibTableColumn
cPimComponentBSRAddress = _CPimComponentBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8, 1, 3),
    _CPimComponentBSRAddress_Type()
)
cPimComponentBSRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimComponentBSRAddress.setStatus("current")
_CPimComponentBSRExpiryTime_Type = TimeTicks
_CPimComponentBSRExpiryTime_Object = MibTableColumn
cPimComponentBSRExpiryTime = _CPimComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8, 1, 4),
    _CPimComponentBSRExpiryTime_Type()
)
cPimComponentBSRExpiryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimComponentBSRExpiryTime.setStatus("current")


class _CPimComponentCRPHoldTime_Type(Unsigned32):
    """Custom type cPimComponentCRPHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPimComponentCRPHoldTime_Type.__name__ = "Unsigned32"
_CPimComponentCRPHoldTime_Object = MibTableColumn
cPimComponentCRPHoldTime = _CPimComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8, 1, 5),
    _CPimComponentCRPHoldTime_Type()
)
cPimComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cPimComponentCRPHoldTime.setUnits("seconds")
_CPimComponentStatus_Type = RowStatus
_CPimComponentStatus_Object = MibTableColumn
cPimComponentStatus = _CPimComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 1, 1, 8, 1, 6),
    _CPimComponentStatus_Type()
)
cPimComponentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPimComponentStatus.setStatus("current")
_CPimMIBConformance_ObjectIdentity = ObjectIdentity
cPimMIBConformance = _CPimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2)
)
_CPimMIBCompliances_ObjectIdentity = ObjectIdentity
cPimMIBCompliances = _CPimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 1)
)
_CPimMIBGroups_ObjectIdentity = ObjectIdentity
cPimMIBGroups = _CPimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 2)
)

# Managed Objects groups

cPimV2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 2, 2)
)
cPimV2MIBGroup.setObjects(
      *(("CISCO-IETF-PIM-MIB", "cPimJoinPruneInterval"),
        ("CISCO-IETF-PIM-MIB", "cPimNbrUpTime"),
        ("CISCO-IETF-PIM-MIB", "cPimNbrExpiryTime"),
        ("CISCO-IETF-PIM-MIB", "cPimIfAddressType"),
        ("CISCO-IETF-PIM-MIB", "cPimIfAddress"),
        ("CISCO-IETF-PIM-MIB", "cPimIfNetMask"),
        ("CISCO-IETF-PIM-MIB", "cPimIfDR"),
        ("CISCO-IETF-PIM-MIB", "cPimIfHelloInterval"),
        ("CISCO-IETF-PIM-MIB", "cPimIfStatus"),
        ("CISCO-IETF-PIM-MIB", "cPimIfJoinPruneInterval"),
        ("CISCO-IETF-PIM-MIB", "cPimIfCBSRPreference"),
        ("CISCO-IETF-PIM-MIB", "cPimIfMode"),
        ("CISCO-IETF-PIM-MIB", "cPimRPMapHoldTime"),
        ("CISCO-IETF-PIM-MIB", "cPimRPMapExpiryTime"),
        ("CISCO-IETF-PIM-MIB", "cPimComponentBSRAddrType"),
        ("CISCO-IETF-PIM-MIB", "cPimComponentBSRAddress"),
        ("CISCO-IETF-PIM-MIB", "cPimComponentBSRExpiryTime"),
        ("CISCO-IETF-PIM-MIB", "cPimComponentCRPHoldTime"),
        ("CISCO-IETF-PIM-MIB", "cPimComponentStatus"),
        ("CISCO-IETF-PIM-MIB", "cPimInetMRouteFlags"),
        ("CISCO-IETF-PIM-MIB", "cPimInetMRouteUpstreamAssertTime"))
)
if mibBuilder.loadTexts:
    cPimV2MIBGroup.setStatus("current")

cPimDenseV2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 2, 3)
)
cPimDenseV2MIBGroup.setObjects(
      *(("CISCO-IETF-PIM-MIB", "cPimNbrUpTime"),
        ("CISCO-IETF-PIM-MIB", "cPimNbrExpiryTime"),
        ("CISCO-IETF-PIM-MIB", "cPimIfAddress"),
        ("CISCO-IETF-PIM-MIB", "cPimIfNetMask"),
        ("CISCO-IETF-PIM-MIB", "cPimIfDR"),
        ("CISCO-IETF-PIM-MIB", "cPimIfHelloInterval"),
        ("CISCO-IETF-PIM-MIB", "cPimIfStatus"),
        ("CISCO-IETF-PIM-MIB", "cPimIfMode"))
)
if mibBuilder.loadTexts:
    cPimDenseV2MIBGroup.setStatus("current")

cPimV2CRPMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 2, 4)
)
cPimV2CRPMIBGroup.setObjects(
      *(("CISCO-IETF-PIM-MIB", "cPimCRPAddress"),
        ("CISCO-IETF-PIM-MIB", "cPimCRPRowStatus"))
)
if mibBuilder.loadTexts:
    cPimV2CRPMIBGroup.setStatus("current")

cPimNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 2, 5)
)
cPimNextHopGroup.setObjects(
    ("CISCO-IETF-PIM-MIB", "cPimInetMRouteNextHopPruneReason")
)
if mibBuilder.loadTexts:
    cPimNextHopGroup.setStatus("current")

cPimAssertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 2, 6)
)
cPimAssertGroup.setObjects(
      *(("CISCO-IETF-PIM-MIB", "cPimInetMRouteAssertMetric"),
        ("CISCO-IETF-PIM-MIB", "cPimInetMRouteAssertMetricPref"),
        ("CISCO-IETF-PIM-MIB", "cPimInetMRouteAssertRPTBit"))
)
if mibBuilder.loadTexts:
    cPimAssertGroup.setStatus("current")


# Notification objects

cPimNbrLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 0, 2)
)
cPimNbrLoss.setObjects(
    ("CISCO-IETF-PIM-MIB", "cPimNbrUpTime")
)
if mibBuilder.loadTexts:
    cPimNbrLoss.setStatus(
        "current"
    )


# Notifications groups

cPimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 2, 1)
)
cPimNotificationGroup.setObjects(
    ("CISCO-IETF-PIM-MIB", "cPimNbrLoss")
)
if mibBuilder.loadTexts:
    cPimNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cPimSparseV2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cPimSparseV2MIBCompliance.setStatus(
        "current"
    )

cPimDenseV2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 119, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cPimDenseV2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PIM-MIB",
    **{"ciscoIetfPimMIB": ciscoIetfPimMIB,
       "cPimNotifs": cPimNotifs,
       "cPimNbrLoss": cPimNbrLoss,
       "cPimMIBObjects": cPimMIBObjects,
       "cPim": cPim,
       "cPimJoinPruneInterval": cPimJoinPruneInterval,
       "cPimIfTable": cPimIfTable,
       "cPimIfEntry": cPimIfEntry,
       "cPimIfIndex": cPimIfIndex,
       "cPimIfInetVersion": cPimIfInetVersion,
       "cPimIfAddressType": cPimIfAddressType,
       "cPimIfAddress": cPimIfAddress,
       "cPimIfNetMask": cPimIfNetMask,
       "cPimIfMode": cPimIfMode,
       "cPimIfDR": cPimIfDR,
       "cPimIfHelloInterval": cPimIfHelloInterval,
       "cPimIfJoinPruneInterval": cPimIfJoinPruneInterval,
       "cPimIfCBSRPreference": cPimIfCBSRPreference,
       "cPimIfStatus": cPimIfStatus,
       "cPimNbrTable": cPimNbrTable,
       "cPimNbrEntry": cPimNbrEntry,
       "cPimNbrIfIndex": cPimNbrIfIndex,
       "cPimNbrAddressType": cPimNbrAddressType,
       "cPimNbrAddress": cPimNbrAddress,
       "cPimNbrUpTime": cPimNbrUpTime,
       "cPimNbrExpiryTime": cPimNbrExpiryTime,
       "cPimInetMRouteTable": cPimInetMRouteTable,
       "cPimInetMRouteEntry": cPimInetMRouteEntry,
       "cPimInetMRouteUpstreamAssertTime": cPimInetMRouteUpstreamAssertTime,
       "cPimInetMRouteAssertMetric": cPimInetMRouteAssertMetric,
       "cPimInetMRouteAssertMetricPref": cPimInetMRouteAssertMetricPref,
       "cPimInetMRouteAssertRPTBit": cPimInetMRouteAssertRPTBit,
       "cPimInetMRouteFlags": cPimInetMRouteFlags,
       "cPimInetMRouteNextHopTable": cPimInetMRouteNextHopTable,
       "cPimInetMRouteNextHopEntry": cPimInetMRouteNextHopEntry,
       "cPimInetMRouteNextHopPruneReason": cPimInetMRouteNextHopPruneReason,
       "cPimRPMapTable": cPimRPMapTable,
       "cPimRPMapEntry": cPimRPMapEntry,
       "cPimRPMapComponent": cPimRPMapComponent,
       "cPimRPMapAddrType": cPimRPMapAddrType,
       "cPimRPMapGroupAddress": cPimRPMapGroupAddress,
       "cPimRPMapGroupMask": cPimRPMapGroupMask,
       "cPimRPMapAddress": cPimRPMapAddress,
       "cPimRPMapHoldTime": cPimRPMapHoldTime,
       "cPimRPMapExpiryTime": cPimRPMapExpiryTime,
       "cPimCRPTable": cPimCRPTable,
       "cPimCRPEntry": cPimCRPEntry,
       "cPimCRPAddrType": cPimCRPAddrType,
       "cPimCRPGroupAddress": cPimCRPGroupAddress,
       "cPimCRPGroupMask": cPimCRPGroupMask,
       "cPimCRPAddress": cPimCRPAddress,
       "cPimCRPRowStatus": cPimCRPRowStatus,
       "cPimComponentTable": cPimComponentTable,
       "cPimComponentEntry": cPimComponentEntry,
       "cPimComponentIndex": cPimComponentIndex,
       "cPimComponentBSRAddrType": cPimComponentBSRAddrType,
       "cPimComponentBSRAddress": cPimComponentBSRAddress,
       "cPimComponentBSRExpiryTime": cPimComponentBSRExpiryTime,
       "cPimComponentCRPHoldTime": cPimComponentCRPHoldTime,
       "cPimComponentStatus": cPimComponentStatus,
       "cPimMIBConformance": cPimMIBConformance,
       "cPimMIBCompliances": cPimMIBCompliances,
       "cPimSparseV2MIBCompliance": cPimSparseV2MIBCompliance,
       "cPimDenseV2MIBCompliance": cPimDenseV2MIBCompliance,
       "cPimMIBGroups": cPimMIBGroups,
       "cPimNotificationGroup": cPimNotificationGroup,
       "cPimV2MIBGroup": cPimV2MIBGroup,
       "cPimDenseV2MIBGroup": cPimDenseV2MIBGroup,
       "cPimV2CRPMIBGroup": cPimV2CRPMIBGroup,
       "cPimNextHopGroup": cPimNextHopGroup,
       "cPimAssertGroup": cPimAssertGroup}
)
