# SNMP MIB module (JUNIPER-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:01 2024
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

(OperationResponseStatus,
 pingCtlTargetAddress,
 pingCtlTargetAddressType,
 pingProbeHistoryEntry,
 pingResultsAverageRtt,
 pingResultsEntry,
 pingResultsIpTargetAddress,
 pingResultsIpTargetAddressType,
 pingResultsLastGoodProbe,
 pingResultsMaxRtt,
 pingResultsMinRtt,
 pingResultsOperStatus,
 pingResultsProbeResponses,
 pingResultsRttSumOfSquares,
 pingResultsSentProbes) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "OperationResponseStatus",
    "pingCtlTargetAddress",
    "pingCtlTargetAddressType",
    "pingProbeHistoryEntry",
    "pingResultsAverageRtt",
    "pingResultsEntry",
    "pingResultsIpTargetAddress",
    "pingResultsIpTargetAddressType",
    "pingResultsLastGoodProbe",
    "pingResultsMaxRtt",
    "pingResultsMinRtt",
    "pingResultsOperStatus",
    "pingResultsProbeResponses",
    "pingResultsRttSumOfSquares",
    "pingResultsSentProbes")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(jnxMibs,
 jnxPingNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxPingNotifications")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7)
)
jnxPingMIB.setRevisions(
        ("2011-09-20 00:00",
         "2009-11-18 00:00",
         "2009-04-20 00:00",
         "2005-05-01 00:00",
         "2004-04-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxPingObjects_ObjectIdentity = ObjectIdentity
jnxPingObjects = _JnxPingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1)
)
_JnxPingCtlTable_Object = MibTable
jnxPingCtlTable = _JnxPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    jnxPingCtlTable.setStatus("current")
_JnxPingCtlEntry_Object = MibTableRow
jnxPingCtlEntry = _JnxPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1)
)
jnxPingCtlEntry.setIndexNames(
    (0, "JUNIPER-PING-MIB", "jnxPingCtlOwnerIndex"),
    (0, "JUNIPER-PING-MIB", "jnxPingCtlTestName"),
)
if mibBuilder.loadTexts:
    jnxPingCtlEntry.setStatus("current")


class _JnxPingCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type jnxPingCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxPingCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_JnxPingCtlOwnerIndex_Object = MibTableColumn
jnxPingCtlOwnerIndex = _JnxPingCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 1),
    _JnxPingCtlOwnerIndex_Type()
)
jnxPingCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPingCtlOwnerIndex.setStatus("current")


class _JnxPingCtlTestName_Type(SnmpAdminString):
    """Custom type jnxPingCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxPingCtlTestName_Type.__name__ = "SnmpAdminString"
_JnxPingCtlTestName_Object = MibTableColumn
jnxPingCtlTestName = _JnxPingCtlTestName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 2),
    _JnxPingCtlTestName_Type()
)
jnxPingCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPingCtlTestName.setStatus("current")


class _JnxPingCtlIfName_Type(DisplayString):
    """Custom type jnxPingCtlIfName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_JnxPingCtlIfName_Type.__name__ = "DisplayString"
_JnxPingCtlIfName_Object = MibTableColumn
jnxPingCtlIfName = _JnxPingCtlIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 3),
    _JnxPingCtlIfName_Type()
)
jnxPingCtlIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlIfName.setStatus("current")


class _JnxPingCtlRoutingIfIndex_Type(InterfaceIndexOrZero):
    """Custom type jnxPingCtlRoutingIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_JnxPingCtlRoutingIfIndex_Object = MibTableColumn
jnxPingCtlRoutingIfIndex = _JnxPingCtlRoutingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 4),
    _JnxPingCtlRoutingIfIndex_Type()
)
jnxPingCtlRoutingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlRoutingIfIndex.setStatus("deprecated")


class _JnxPingCtlRoutingIfName_Type(DisplayString):
    """Custom type jnxPingCtlRoutingIfName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_JnxPingCtlRoutingIfName_Type.__name__ = "DisplayString"
_JnxPingCtlRoutingIfName_Object = MibTableColumn
jnxPingCtlRoutingIfName = _JnxPingCtlRoutingIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 5),
    _JnxPingCtlRoutingIfName_Type()
)
jnxPingCtlRoutingIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlRoutingIfName.setStatus("deprecated")


class _JnxPingCtlRoutingInstanceName_Type(DisplayString):
    """Custom type jnxPingCtlRoutingInstanceName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxPingCtlRoutingInstanceName_Type.__name__ = "DisplayString"
_JnxPingCtlRoutingInstanceName_Object = MibTableColumn
jnxPingCtlRoutingInstanceName = _JnxPingCtlRoutingInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 6),
    _JnxPingCtlRoutingInstanceName_Type()
)
jnxPingCtlRoutingInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlRoutingInstanceName.setStatus("current")


class _JnxPingCtlRttThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlRttThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000000),
    )


_JnxPingCtlRttThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlRttThreshold_Object = MibTableColumn
jnxPingCtlRttThreshold = _JnxPingCtlRttThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 7),
    _JnxPingCtlRttThreshold_Type()
)
jnxPingCtlRttThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlRttThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlRttThreshold.setUnits("microseconds")


class _JnxPingCtlRttStdDevThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlRttStdDevThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000000),
    )


_JnxPingCtlRttStdDevThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlRttStdDevThreshold_Object = MibTableColumn
jnxPingCtlRttStdDevThreshold = _JnxPingCtlRttStdDevThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 8),
    _JnxPingCtlRttStdDevThreshold_Type()
)
jnxPingCtlRttStdDevThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlRttStdDevThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlRttStdDevThreshold.setUnits("microseconds")


class _JnxPingCtlRttJitterThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlRttJitterThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000000),
    )


_JnxPingCtlRttJitterThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlRttJitterThreshold_Object = MibTableColumn
jnxPingCtlRttJitterThreshold = _JnxPingCtlRttJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 9),
    _JnxPingCtlRttJitterThreshold_Type()
)
jnxPingCtlRttJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlRttJitterThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlRttJitterThreshold.setUnits("microseconds")


class _JnxPingCtlEgressTimeThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlEgressTimeThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_JnxPingCtlEgressTimeThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlEgressTimeThreshold_Object = MibTableColumn
jnxPingCtlEgressTimeThreshold = _JnxPingCtlEgressTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 10),
    _JnxPingCtlEgressTimeThreshold_Type()
)
jnxPingCtlEgressTimeThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlEgressTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlEgressTimeThreshold.setUnits("microseconds")


class _JnxPingCtlEgressStdDevThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlEgressStdDevThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_JnxPingCtlEgressStdDevThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlEgressStdDevThreshold_Object = MibTableColumn
jnxPingCtlEgressStdDevThreshold = _JnxPingCtlEgressStdDevThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 11),
    _JnxPingCtlEgressStdDevThreshold_Type()
)
jnxPingCtlEgressStdDevThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlEgressStdDevThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlEgressStdDevThreshold.setUnits("microseconds")


class _JnxPingCtlEgressJitterThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlEgressJitterThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_JnxPingCtlEgressJitterThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlEgressJitterThreshold_Object = MibTableColumn
jnxPingCtlEgressJitterThreshold = _JnxPingCtlEgressJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 12),
    _JnxPingCtlEgressJitterThreshold_Type()
)
jnxPingCtlEgressJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlEgressJitterThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlEgressJitterThreshold.setUnits("microseconds")


class _JnxPingCtlIngressTimeThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlIngressTimeThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_JnxPingCtlIngressTimeThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlIngressTimeThreshold_Object = MibTableColumn
jnxPingCtlIngressTimeThreshold = _JnxPingCtlIngressTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 13),
    _JnxPingCtlIngressTimeThreshold_Type()
)
jnxPingCtlIngressTimeThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlIngressTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlIngressTimeThreshold.setUnits("microseconds")


class _JnxPingCtlIngressStddevThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlIngressStddevThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_JnxPingCtlIngressStddevThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlIngressStddevThreshold_Object = MibTableColumn
jnxPingCtlIngressStddevThreshold = _JnxPingCtlIngressStddevThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 14),
    _JnxPingCtlIngressStddevThreshold_Type()
)
jnxPingCtlIngressStddevThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlIngressStddevThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlIngressStddevThreshold.setUnits("microseconds")


class _JnxPingCtlIngressJitterThreshold_Type(Unsigned32):
    """Custom type jnxPingCtlIngressJitterThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_JnxPingCtlIngressJitterThreshold_Type.__name__ = "Unsigned32"
_JnxPingCtlIngressJitterThreshold_Object = MibTableColumn
jnxPingCtlIngressJitterThreshold = _JnxPingCtlIngressJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 15),
    _JnxPingCtlIngressJitterThreshold_Type()
)
jnxPingCtlIngressJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlIngressJitterThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingCtlIngressJitterThreshold.setUnits("microseconds")


class _JnxPingCtlTrapGeneration_Type(Bits):
    """Custom type jnxPingCtlTrapGeneration based on Bits"""
    namedValues = NamedValues(
        *(("egressJitterThreshold", 5),
          ("egressStdDevThreshold", 4),
          ("egressThreshold", 3),
          ("ingressJitterThreshold", 8),
          ("ingressStdDevThreshold", 7),
          ("ingressThreshold", 6),
          ("rttJitterThreshold", 2),
          ("rttStdDevThreshold", 1),
          ("rttThreshold", 0))
    )

_JnxPingCtlTrapGeneration_Type.__name__ = "Bits"
_JnxPingCtlTrapGeneration_Object = MibTableColumn
jnxPingCtlTrapGeneration = _JnxPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 16),
    _JnxPingCtlTrapGeneration_Type()
)
jnxPingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlTrapGeneration.setStatus("current")


class _JnxPingCtlTargetPort_Type(InetPortNumber):
    """Custom type jnxPingCtlTargetPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(49152, 65535),
    )


_JnxPingCtlTargetPort_Type.__name__ = "InetPortNumber"
_JnxPingCtlTargetPort_Object = MibTableColumn
jnxPingCtlTargetPort = _JnxPingCtlTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 17),
    _JnxPingCtlTargetPort_Type()
)
jnxPingCtlTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlTargetPort.setStatus("current")


class _JnxPingCtlJseriesHWTimeStamp_Type(TruthValue):
    """Custom type jnxPingCtlJseriesHWTimeStamp based on TruthValue"""


_JnxPingCtlJseriesHWTimeStamp_Object = MibTableColumn
jnxPingCtlJseriesHWTimeStamp = _JnxPingCtlJseriesHWTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 18),
    _JnxPingCtlJseriesHWTimeStamp_Type()
)
jnxPingCtlJseriesHWTimeStamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlJseriesHWTimeStamp.setStatus("current")


class _JnxPingCtlOneWayHWTimeStamp_Type(TruthValue):
    """Custom type jnxPingCtlOneWayHWTimeStamp based on TruthValue"""


_JnxPingCtlOneWayHWTimeStamp_Object = MibTableColumn
jnxPingCtlOneWayHWTimeStamp = _JnxPingCtlOneWayHWTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 19),
    _JnxPingCtlOneWayHWTimeStamp_Type()
)
jnxPingCtlOneWayHWTimeStamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlOneWayHWTimeStamp.setStatus("current")


class _JnxPingCtlMovAvgSize_Type(Unsigned32):
    """Custom type jnxPingCtlMovAvgSize based on Unsigned32"""
    defaultValue = 0


_JnxPingCtlMovAvgSize_Object = MibTableColumn
jnxPingCtlMovAvgSize = _JnxPingCtlMovAvgSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 20),
    _JnxPingCtlMovAvgSize_Type()
)
jnxPingCtlMovAvgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlMovAvgSize.setStatus("current")


class _JnxPingCtlMXseriesHWTimeStamp_Type(TruthValue):
    """Custom type jnxPingCtlMXseriesHWTimeStamp based on TruthValue"""


_JnxPingCtlMXseriesHWTimeStamp_Object = MibTableColumn
jnxPingCtlMXseriesHWTimeStamp = _JnxPingCtlMXseriesHWTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 21),
    _JnxPingCtlMXseriesHWTimeStamp_Type()
)
jnxPingCtlMXseriesHWTimeStamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlMXseriesHWTimeStamp.setStatus("current")


class _JnxPingCtlEXseriesHWTimeStamp_Type(TruthValue):
    """Custom type jnxPingCtlEXseriesHWTimeStamp based on TruthValue"""


_JnxPingCtlEXseriesHWTimeStamp_Object = MibTableColumn
jnxPingCtlEXseriesHWTimeStamp = _JnxPingCtlEXseriesHWTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 2, 1, 22),
    _JnxPingCtlEXseriesHWTimeStamp_Type()
)
jnxPingCtlEXseriesHWTimeStamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxPingCtlEXseriesHWTimeStamp.setStatus("current")
_JnxPingResultsTable_Object = MibTable
jnxPingResultsTable = _JnxPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3)
)
if mibBuilder.loadTexts:
    jnxPingResultsTable.setStatus("current")
_JnxPingResultsEntry_Object = MibTableRow
jnxPingResultsEntry = _JnxPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxPingResultsEntry.setStatus("current")
_JnxPingResultsRttUs_Type = Unsigned32
_JnxPingResultsRttUs_Object = MibTableColumn
jnxPingResultsRttUs = _JnxPingResultsRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 1),
    _JnxPingResultsRttUs_Type()
)
jnxPingResultsRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsRttUs.setUnits("microseconds")
_JnxPingResultsSumRttUs_Type = Unsigned32
_JnxPingResultsSumRttUs_Object = MibTableColumn
jnxPingResultsSumRttUs = _JnxPingResultsSumRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 2),
    _JnxPingResultsSumRttUs_Type()
)
jnxPingResultsSumRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsSumRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsSumRttUs.setUnits("microseconds")
_JnxPingResultsMinRttUs_Type = Unsigned32
_JnxPingResultsMinRttUs_Object = MibTableColumn
jnxPingResultsMinRttUs = _JnxPingResultsMinRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 3),
    _JnxPingResultsMinRttUs_Type()
)
jnxPingResultsMinRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsMinRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsMinRttUs.setUnits("microseconds")
_JnxPingResultsMaxRttUs_Type = Unsigned32
_JnxPingResultsMaxRttUs_Object = MibTableColumn
jnxPingResultsMaxRttUs = _JnxPingResultsMaxRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 4),
    _JnxPingResultsMaxRttUs_Type()
)
jnxPingResultsMaxRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsMaxRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsMaxRttUs.setUnits("microseconds")
_JnxPingResultsAvgRttUs_Type = Unsigned32
_JnxPingResultsAvgRttUs_Object = MibTableColumn
jnxPingResultsAvgRttUs = _JnxPingResultsAvgRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 5),
    _JnxPingResultsAvgRttUs_Type()
)
jnxPingResultsAvgRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsAvgRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsAvgRttUs.setUnits("microseconds")
_JnxPingResultsStdDevRttUs_Type = Unsigned32
_JnxPingResultsStdDevRttUs_Object = MibTableColumn
jnxPingResultsStdDevRttUs = _JnxPingResultsStdDevRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 6),
    _JnxPingResultsStdDevRttUs_Type()
)
jnxPingResultsStdDevRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsStdDevRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsStdDevRttUs.setUnits("microseconds")
_JnxPingResultsEgressUs_Type = Unsigned32
_JnxPingResultsEgressUs_Object = MibTableColumn
jnxPingResultsEgressUs = _JnxPingResultsEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 7),
    _JnxPingResultsEgressUs_Type()
)
jnxPingResultsEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsEgressUs.setUnits("microseconds")
_JnxPingResultsMinEgressUs_Type = Unsigned32
_JnxPingResultsMinEgressUs_Object = MibTableColumn
jnxPingResultsMinEgressUs = _JnxPingResultsMinEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 8),
    _JnxPingResultsMinEgressUs_Type()
)
jnxPingResultsMinEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsMinEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsMinEgressUs.setUnits("microseconds")
_JnxPingResultsMaxEgressUs_Type = Unsigned32
_JnxPingResultsMaxEgressUs_Object = MibTableColumn
jnxPingResultsMaxEgressUs = _JnxPingResultsMaxEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 9),
    _JnxPingResultsMaxEgressUs_Type()
)
jnxPingResultsMaxEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsMaxEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsMaxEgressUs.setUnits("microseconds")
_JnxPingResultsAvgEgressUs_Type = Unsigned32
_JnxPingResultsAvgEgressUs_Object = MibTableColumn
jnxPingResultsAvgEgressUs = _JnxPingResultsAvgEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 10),
    _JnxPingResultsAvgEgressUs_Type()
)
jnxPingResultsAvgEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsAvgEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsAvgEgressUs.setUnits("microseconds")
_JnxPingResultsStddevEgressUs_Type = Unsigned32
_JnxPingResultsStddevEgressUs_Object = MibTableColumn
jnxPingResultsStddevEgressUs = _JnxPingResultsStddevEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 11),
    _JnxPingResultsStddevEgressUs_Type()
)
jnxPingResultsStddevEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsStddevEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsStddevEgressUs.setUnits("microseconds")
_JnxPingResultsIngressUs_Type = Unsigned32
_JnxPingResultsIngressUs_Object = MibTableColumn
jnxPingResultsIngressUs = _JnxPingResultsIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 12),
    _JnxPingResultsIngressUs_Type()
)
jnxPingResultsIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsIngressUs.setUnits("microseconds")
_JnxPingResultsMinIngressUs_Type = Unsigned32
_JnxPingResultsMinIngressUs_Object = MibTableColumn
jnxPingResultsMinIngressUs = _JnxPingResultsMinIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 13),
    _JnxPingResultsMinIngressUs_Type()
)
jnxPingResultsMinIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsMinIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsMinIngressUs.setUnits("microseconds")
_JnxPingResultsMaxIngressUs_Type = Unsigned32
_JnxPingResultsMaxIngressUs_Object = MibTableColumn
jnxPingResultsMaxIngressUs = _JnxPingResultsMaxIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 14),
    _JnxPingResultsMaxIngressUs_Type()
)
jnxPingResultsMaxIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsMaxIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsMaxIngressUs.setUnits("microseconds")
_JnxPingResultsAvgIngressUs_Type = Unsigned32
_JnxPingResultsAvgIngressUs_Object = MibTableColumn
jnxPingResultsAvgIngressUs = _JnxPingResultsAvgIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 15),
    _JnxPingResultsAvgIngressUs_Type()
)
jnxPingResultsAvgIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsAvgIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsAvgIngressUs.setUnits("microseconds")
_JnxPingResultsStddevIngressUs_Type = Unsigned32
_JnxPingResultsStddevIngressUs_Object = MibTableColumn
jnxPingResultsStddevIngressUs = _JnxPingResultsStddevIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 16),
    _JnxPingResultsStddevIngressUs_Type()
)
jnxPingResultsStddevIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsStddevIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsStddevIngressUs.setUnits("microseconds")
_JnxPingResultsJitterRttUs_Type = Unsigned32
_JnxPingResultsJitterRttUs_Object = MibTableColumn
jnxPingResultsJitterRttUs = _JnxPingResultsJitterRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 17),
    _JnxPingResultsJitterRttUs_Type()
)
jnxPingResultsJitterRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsJitterRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsJitterRttUs.setUnits("microseconds")
_JnxPingResultsJitterEgressUs_Type = Unsigned32
_JnxPingResultsJitterEgressUs_Object = MibTableColumn
jnxPingResultsJitterEgressUs = _JnxPingResultsJitterEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 18),
    _JnxPingResultsJitterEgressUs_Type()
)
jnxPingResultsJitterEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsJitterEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsJitterEgressUs.setUnits("microseconds")
_JnxPingResultsJitterIngressUs_Type = Unsigned32
_JnxPingResultsJitterIngressUs_Object = MibTableColumn
jnxPingResultsJitterIngressUs = _JnxPingResultsJitterIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 19),
    _JnxPingResultsJitterIngressUs_Type()
)
jnxPingResultsJitterIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsJitterIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingResultsJitterIngressUs.setUnits("microseconds")
_JnxPingResultsStatus_Type = OperationResponseStatus
_JnxPingResultsStatus_Object = MibTableColumn
jnxPingResultsStatus = _JnxPingResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 20),
    _JnxPingResultsStatus_Type()
)
jnxPingResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsStatus.setStatus("current")
_JnxPingResultsTime_Type = DateAndTime
_JnxPingResultsTime_Object = MibTableColumn
jnxPingResultsTime = _JnxPingResultsTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 21),
    _JnxPingResultsTime_Type()
)
jnxPingResultsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsTime.setStatus("current")


class _JnxPingResultsOwnerIndex_Type(SnmpAdminString):
    """Custom type jnxPingResultsOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxPingResultsOwnerIndex_Type.__name__ = "SnmpAdminString"
_JnxPingResultsOwnerIndex_Object = MibTableColumn
jnxPingResultsOwnerIndex = _JnxPingResultsOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 22),
    _JnxPingResultsOwnerIndex_Type()
)
jnxPingResultsOwnerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsOwnerIndex.setStatus("current")


class _JnxPingResultsTestName_Type(SnmpAdminString):
    """Custom type jnxPingResultsTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxPingResultsTestName_Type.__name__ = "SnmpAdminString"
_JnxPingResultsTestName_Object = MibTableColumn
jnxPingResultsTestName = _JnxPingResultsTestName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 3, 1, 23),
    _JnxPingResultsTestName_Type()
)
jnxPingResultsTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingResultsTestName.setStatus("current")
_JnxPingProbeHistoryTable_Object = MibTable
jnxPingProbeHistoryTable = _JnxPingProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4)
)
if mibBuilder.loadTexts:
    jnxPingProbeHistoryTable.setStatus("current")
_JnxPingProbeHistoryEntry_Object = MibTableRow
jnxPingProbeHistoryEntry = _JnxPingProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jnxPingProbeHistoryEntry.setStatus("current")
_JnxPingProbeHistoryResponseUs_Type = Unsigned32
_JnxPingProbeHistoryResponseUs_Object = MibTableColumn
jnxPingProbeHistoryResponseUs = _JnxPingProbeHistoryResponseUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4, 1, 1),
    _JnxPingProbeHistoryResponseUs_Type()
)
jnxPingProbeHistoryResponseUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryResponseUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryResponseUs.setUnits("microseconds")
_JnxPingProbeHistoryJitterUs_Type = Unsigned32
_JnxPingProbeHistoryJitterUs_Object = MibTableColumn
jnxPingProbeHistoryJitterUs = _JnxPingProbeHistoryJitterUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4, 1, 2),
    _JnxPingProbeHistoryJitterUs_Type()
)
jnxPingProbeHistoryJitterUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryJitterUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryJitterUs.setUnits("microseconds")
_JnxPingProbeHistoryResponseEgressUs_Type = Unsigned32
_JnxPingProbeHistoryResponseEgressUs_Object = MibTableColumn
jnxPingProbeHistoryResponseEgressUs = _JnxPingProbeHistoryResponseEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4, 1, 3),
    _JnxPingProbeHistoryResponseEgressUs_Type()
)
jnxPingProbeHistoryResponseEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryResponseEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryResponseEgressUs.setUnits("microseconds")
_JnxPingProbeHistoryResponseIngressUs_Type = Unsigned32
_JnxPingProbeHistoryResponseIngressUs_Object = MibTableColumn
jnxPingProbeHistoryResponseIngressUs = _JnxPingProbeHistoryResponseIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4, 1, 4),
    _JnxPingProbeHistoryResponseIngressUs_Type()
)
jnxPingProbeHistoryResponseIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryResponseIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryResponseIngressUs.setUnits("microseconds")
_JnxPingProbeHistoryEgressJitterUs_Type = Unsigned32
_JnxPingProbeHistoryEgressJitterUs_Object = MibTableColumn
jnxPingProbeHistoryEgressJitterUs = _JnxPingProbeHistoryEgressJitterUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4, 1, 5),
    _JnxPingProbeHistoryEgressJitterUs_Type()
)
jnxPingProbeHistoryEgressJitterUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryEgressJitterUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryEgressJitterUs.setUnits("microseconds")
_JnxPingProbeHistoryIngressJitterUs_Type = Unsigned32
_JnxPingProbeHistoryIngressJitterUs_Object = MibTableColumn
jnxPingProbeHistoryIngressJitterUs = _JnxPingProbeHistoryIngressJitterUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 4, 1, 6),
    _JnxPingProbeHistoryIngressJitterUs_Type()
)
jnxPingProbeHistoryIngressJitterUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryIngressJitterUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingProbeHistoryIngressJitterUs.setUnits("microseconds")
_JnxPingLastTestResultTable_Object = MibTable
jnxPingLastTestResultTable = _JnxPingLastTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5)
)
if mibBuilder.loadTexts:
    jnxPingLastTestResultTable.setStatus("current")
_JnxPingLastTestResultEntry_Object = MibTableRow
jnxPingLastTestResultEntry = _JnxPingLastTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1)
)
jnxPingLastTestResultEntry.setIndexNames(
    (0, "JUNIPER-PING-MIB", "jnxPingCtlOwnerIndex"),
    (0, "JUNIPER-PING-MIB", "jnxPingCtlTestName"),
)
if mibBuilder.loadTexts:
    jnxPingLastTestResultEntry.setStatus("current")
_JnxPingLastTestResultProbeResponses_Type = Unsigned32
_JnxPingLastTestResultProbeResponses_Object = MibTableColumn
jnxPingLastTestResultProbeResponses = _JnxPingLastTestResultProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 1),
    _JnxPingLastTestResultProbeResponses_Type()
)
jnxPingLastTestResultProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultProbeResponses.setUnits("responses")
_JnxPingLastTestResultSentProbes_Type = Unsigned32
_JnxPingLastTestResultSentProbes_Object = MibTableColumn
jnxPingLastTestResultSentProbes = _JnxPingLastTestResultSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 2),
    _JnxPingLastTestResultSentProbes_Type()
)
jnxPingLastTestResultSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultSentProbes.setUnits("probes")
_JnxPingLastTestResultSumRttUs_Type = Unsigned32
_JnxPingLastTestResultSumRttUs_Object = MibTableColumn
jnxPingLastTestResultSumRttUs = _JnxPingLastTestResultSumRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 3),
    _JnxPingLastTestResultSumRttUs_Type()
)
jnxPingLastTestResultSumRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultSumRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultSumRttUs.setUnits("microseconds")
_JnxPingLastTestResultMinRttUs_Type = Unsigned32
_JnxPingLastTestResultMinRttUs_Object = MibTableColumn
jnxPingLastTestResultMinRttUs = _JnxPingLastTestResultMinRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 4),
    _JnxPingLastTestResultMinRttUs_Type()
)
jnxPingLastTestResultMinRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMinRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMinRttUs.setUnits("microseconds")
_JnxPingLastTestResultMaxRttUs_Type = Unsigned32
_JnxPingLastTestResultMaxRttUs_Object = MibTableColumn
jnxPingLastTestResultMaxRttUs = _JnxPingLastTestResultMaxRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 5),
    _JnxPingLastTestResultMaxRttUs_Type()
)
jnxPingLastTestResultMaxRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMaxRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMaxRttUs.setUnits("microseconds")
_JnxPingLastTestResultAvgRttUs_Type = Unsigned32
_JnxPingLastTestResultAvgRttUs_Object = MibTableColumn
jnxPingLastTestResultAvgRttUs = _JnxPingLastTestResultAvgRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 6),
    _JnxPingLastTestResultAvgRttUs_Type()
)
jnxPingLastTestResultAvgRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultAvgRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultAvgRttUs.setUnits("microseconds")
_JnxPingLastTestResultStdDevRttUs_Type = Unsigned32
_JnxPingLastTestResultStdDevRttUs_Object = MibTableColumn
jnxPingLastTestResultStdDevRttUs = _JnxPingLastTestResultStdDevRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 7),
    _JnxPingLastTestResultStdDevRttUs_Type()
)
jnxPingLastTestResultStdDevRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultStdDevRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultStdDevRttUs.setUnits("microseconds")
_JnxPingLastTestResultMinEgressUs_Type = Unsigned32
_JnxPingLastTestResultMinEgressUs_Object = MibTableColumn
jnxPingLastTestResultMinEgressUs = _JnxPingLastTestResultMinEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 8),
    _JnxPingLastTestResultMinEgressUs_Type()
)
jnxPingLastTestResultMinEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMinEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMinEgressUs.setUnits("microseconds")
_JnxPingLastTestResultMaxEgressUs_Type = Unsigned32
_JnxPingLastTestResultMaxEgressUs_Object = MibTableColumn
jnxPingLastTestResultMaxEgressUs = _JnxPingLastTestResultMaxEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 9),
    _JnxPingLastTestResultMaxEgressUs_Type()
)
jnxPingLastTestResultMaxEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMaxEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMaxEgressUs.setUnits("microseconds")
_JnxPingLastTestResultAvgEgressUs_Type = Unsigned32
_JnxPingLastTestResultAvgEgressUs_Object = MibTableColumn
jnxPingLastTestResultAvgEgressUs = _JnxPingLastTestResultAvgEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 10),
    _JnxPingLastTestResultAvgEgressUs_Type()
)
jnxPingLastTestResultAvgEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultAvgEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultAvgEgressUs.setUnits("microseconds")
_JnxPingLastTestResultStddevEgressUs_Type = Unsigned32
_JnxPingLastTestResultStddevEgressUs_Object = MibTableColumn
jnxPingLastTestResultStddevEgressUs = _JnxPingLastTestResultStddevEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 11),
    _JnxPingLastTestResultStddevEgressUs_Type()
)
jnxPingLastTestResultStddevEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultStddevEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultStddevEgressUs.setUnits("microseconds")
_JnxPingLastTestResultMinIngressUs_Type = Unsigned32
_JnxPingLastTestResultMinIngressUs_Object = MibTableColumn
jnxPingLastTestResultMinIngressUs = _JnxPingLastTestResultMinIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 12),
    _JnxPingLastTestResultMinIngressUs_Type()
)
jnxPingLastTestResultMinIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMinIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMinIngressUs.setUnits("microseconds")
_JnxPingLastTestResultMaxIngressUs_Type = Unsigned32
_JnxPingLastTestResultMaxIngressUs_Object = MibTableColumn
jnxPingLastTestResultMaxIngressUs = _JnxPingLastTestResultMaxIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 13),
    _JnxPingLastTestResultMaxIngressUs_Type()
)
jnxPingLastTestResultMaxIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMaxIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultMaxIngressUs.setUnits("microseconds")
_JnxPingLastTestResultAvgIngressUs_Type = Unsigned32
_JnxPingLastTestResultAvgIngressUs_Object = MibTableColumn
jnxPingLastTestResultAvgIngressUs = _JnxPingLastTestResultAvgIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 14),
    _JnxPingLastTestResultAvgIngressUs_Type()
)
jnxPingLastTestResultAvgIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultAvgIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultAvgIngressUs.setUnits("microseconds")
_JnxPingLastTestResultStddevIngressUs_Type = Unsigned32
_JnxPingLastTestResultStddevIngressUs_Object = MibTableColumn
jnxPingLastTestResultStddevIngressUs = _JnxPingLastTestResultStddevIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 15),
    _JnxPingLastTestResultStddevIngressUs_Type()
)
jnxPingLastTestResultStddevIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultStddevIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultStddevIngressUs.setUnits("microseconds")
_JnxPingLastTestResultPeakToPeakJitterRttUs_Type = Unsigned32
_JnxPingLastTestResultPeakToPeakJitterRttUs_Object = MibTableColumn
jnxPingLastTestResultPeakToPeakJitterRttUs = _JnxPingLastTestResultPeakToPeakJitterRttUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 16),
    _JnxPingLastTestResultPeakToPeakJitterRttUs_Type()
)
jnxPingLastTestResultPeakToPeakJitterRttUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultPeakToPeakJitterRttUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultPeakToPeakJitterRttUs.setUnits("microseconds")
_JnxPingLastTestResultPeakToPeakJitterEgressUs_Type = Unsigned32
_JnxPingLastTestResultPeakToPeakJitterEgressUs_Object = MibTableColumn
jnxPingLastTestResultPeakToPeakJitterEgressUs = _JnxPingLastTestResultPeakToPeakJitterEgressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 17),
    _JnxPingLastTestResultPeakToPeakJitterEgressUs_Type()
)
jnxPingLastTestResultPeakToPeakJitterEgressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultPeakToPeakJitterEgressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultPeakToPeakJitterEgressUs.setUnits("microseconds")
_JnxPingLastTestResultPeakToPeakJitterIngressUs_Type = Unsigned32
_JnxPingLastTestResultPeakToPeakJitterIngressUs_Object = MibTableColumn
jnxPingLastTestResultPeakToPeakJitterIngressUs = _JnxPingLastTestResultPeakToPeakJitterIngressUs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 18),
    _JnxPingLastTestResultPeakToPeakJitterIngressUs_Type()
)
jnxPingLastTestResultPeakToPeakJitterIngressUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultPeakToPeakJitterIngressUs.setStatus("current")
if mibBuilder.loadTexts:
    jnxPingLastTestResultPeakToPeakJitterIngressUs.setUnits("microseconds")
_JnxPingLastTestResultTime_Type = DateAndTime
_JnxPingLastTestResultTime_Object = MibTableColumn
jnxPingLastTestResultTime = _JnxPingLastTestResultTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 1, 5, 1, 19),
    _JnxPingLastTestResultTime_Type()
)
jnxPingLastTestResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPingLastTestResultTime.setStatus("current")
_JnxPingImplementationTypeDomains_ObjectIdentity = ObjectIdentity
jnxPingImplementationTypeDomains = _JnxPingImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 2)
)
_JnxPingIcmpTimeStamp_ObjectIdentity = ObjectIdentity
jnxPingIcmpTimeStamp = _JnxPingIcmpTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    jnxPingIcmpTimeStamp.setStatus("current")
_JnxPingHttpGet_ObjectIdentity = ObjectIdentity
jnxPingHttpGet = _JnxPingHttpGet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    jnxPingHttpGet.setStatus("current")
_JnxPingHttpGetMetadata_ObjectIdentity = ObjectIdentity
jnxPingHttpGetMetadata = _JnxPingHttpGetMetadata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 2, 3)
)
if mibBuilder.loadTexts:
    jnxPingHttpGetMetadata.setStatus("current")
_JnxPingDnsQuery_ObjectIdentity = ObjectIdentity
jnxPingDnsQuery = _JnxPingDnsQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 2, 4)
)
if mibBuilder.loadTexts:
    jnxPingDnsQuery.setStatus("current")
_JnxPingNtpQuery_ObjectIdentity = ObjectIdentity
jnxPingNtpQuery = _JnxPingNtpQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 2, 5)
)
if mibBuilder.loadTexts:
    jnxPingNtpQuery.setStatus("current")
_JnxPingUdpTimestamp_ObjectIdentity = ObjectIdentity
jnxPingUdpTimestamp = _JnxPingUdpTimestamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 7, 2, 6)
)
if mibBuilder.loadTexts:
    jnxPingUdpTimestamp.setStatus("current")
_JnxPingNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxPingNotificationPrefix = _JnxPingNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0)
)
if mibBuilder.loadTexts:
    jnxPingNotificationPrefix.setStatus("current")
pingResultsEntry.registerAugmentions(
    ("JUNIPER-PING-MIB",
     "jnxPingResultsEntry")
)
jnxPingResultsEntry.setIndexNames(*pingResultsEntry.getIndexNames())
pingProbeHistoryEntry.registerAugmentions(
    ("JUNIPER-PING-MIB",
     "jnxPingProbeHistoryEntry")
)
jnxPingProbeHistoryEntry.setIndexNames(*pingProbeHistoryEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxPingRttThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 1)
)
jnxPingRttThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinRttUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxRttUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgRttUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingCtlRttThreshold"),
        ("JUNIPER-PING-MIB", "jnxPingResultsRttUs"))
)
if mibBuilder.loadTexts:
    jnxPingRttThresholdExceeded.setStatus(
        "current"
    )

jnxPingRttStdDevThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 2)
)
jnxPingRttStdDevThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinRttUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxRttUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgRttUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingCtlRttStdDevThreshold"),
        ("JUNIPER-PING-MIB", "jnxPingResultsStdDevRttUs"))
)
if mibBuilder.loadTexts:
    jnxPingRttStdDevThresholdExceeded.setStatus(
        "current"
    )

jnxPingRttJitterThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 3)
)
jnxPingRttJitterThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinRttUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxRttUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgRttUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsRttSumOfSquares"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingCtlRttJitterThreshold"))
)
if mibBuilder.loadTexts:
    jnxPingRttJitterThresholdExceeded.setStatus(
        "current"
    )

jnxPingEgressThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 4)
)
jnxPingEgressThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinEgressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxEgressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgEgressUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingCtlEgressTimeThreshold"),
        ("JUNIPER-PING-MIB", "jnxPingResultsEgressUs"))
)
if mibBuilder.loadTexts:
    jnxPingEgressThresholdExceeded.setStatus(
        "current"
    )

jnxPingEgressStdDevThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 5)
)
jnxPingEgressStdDevThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinEgressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxEgressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgEgressUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingResultsStddevEgressUs"),
        ("JUNIPER-PING-MIB", "jnxPingCtlEgressStdDevThreshold"),
        ("JUNIPER-PING-MIB", "jnxPingResultsStddevEgressUs"))
)
if mibBuilder.loadTexts:
    jnxPingEgressStdDevThresholdExceeded.setStatus(
        "current"
    )

jnxPingEgressJitterThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 6)
)
jnxPingEgressJitterThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinEgressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxEgressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgEgressUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingCtlEgressJitterThreshold"))
)
if mibBuilder.loadTexts:
    jnxPingEgressJitterThresholdExceeded.setStatus(
        "current"
    )

jnxPingIngressThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 7)
)
jnxPingIngressThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinIngressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxIngressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgIngressUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingCtlIngressTimeThreshold"),
        ("JUNIPER-PING-MIB", "jnxPingResultsIngressUs"))
)
if mibBuilder.loadTexts:
    jnxPingIngressThresholdExceeded.setStatus(
        "current"
    )

jnxPingIngressStddevThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 8)
)
jnxPingIngressStddevThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinIngressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxIngressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgIngressUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingResultsStddevIngressUs"),
        ("JUNIPER-PING-MIB", "jnxPingCtlIngressStddevThreshold"),
        ("JUNIPER-PING-MIB", "jnxPingResultsStddevIngressUs"))
)
if mibBuilder.loadTexts:
    jnxPingIngressStddevThresholdExceeded.setStatus(
        "current"
    )

jnxPingIngressJitterThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 9, 0, 9)
)
jnxPingIngressJitterThresholdExceeded.setObjects(
      *(("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingResultsOperStatus"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddressType"),
        ("DISMAN-PING-MIB", "pingResultsIpTargetAddress"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMinIngressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsMaxIngressUs"),
        ("JUNIPER-PING-MIB", "jnxPingResultsAvgIngressUs"),
        ("DISMAN-PING-MIB", "pingResultsProbeResponses"),
        ("DISMAN-PING-MIB", "pingResultsSentProbes"),
        ("DISMAN-PING-MIB", "pingResultsLastGoodProbe"),
        ("JUNIPER-PING-MIB", "jnxPingCtlIngressJitterThreshold"))
)
if mibBuilder.loadTexts:
    jnxPingIngressJitterThresholdExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-PING-MIB",
    **{"jnxPingMIB": jnxPingMIB,
       "jnxPingObjects": jnxPingObjects,
       "jnxPingCtlTable": jnxPingCtlTable,
       "jnxPingCtlEntry": jnxPingCtlEntry,
       "jnxPingCtlOwnerIndex": jnxPingCtlOwnerIndex,
       "jnxPingCtlTestName": jnxPingCtlTestName,
       "jnxPingCtlIfName": jnxPingCtlIfName,
       "jnxPingCtlRoutingIfIndex": jnxPingCtlRoutingIfIndex,
       "jnxPingCtlRoutingIfName": jnxPingCtlRoutingIfName,
       "jnxPingCtlRoutingInstanceName": jnxPingCtlRoutingInstanceName,
       "jnxPingCtlRttThreshold": jnxPingCtlRttThreshold,
       "jnxPingCtlRttStdDevThreshold": jnxPingCtlRttStdDevThreshold,
       "jnxPingCtlRttJitterThreshold": jnxPingCtlRttJitterThreshold,
       "jnxPingCtlEgressTimeThreshold": jnxPingCtlEgressTimeThreshold,
       "jnxPingCtlEgressStdDevThreshold": jnxPingCtlEgressStdDevThreshold,
       "jnxPingCtlEgressJitterThreshold": jnxPingCtlEgressJitterThreshold,
       "jnxPingCtlIngressTimeThreshold": jnxPingCtlIngressTimeThreshold,
       "jnxPingCtlIngressStddevThreshold": jnxPingCtlIngressStddevThreshold,
       "jnxPingCtlIngressJitterThreshold": jnxPingCtlIngressJitterThreshold,
       "jnxPingCtlTrapGeneration": jnxPingCtlTrapGeneration,
       "jnxPingCtlTargetPort": jnxPingCtlTargetPort,
       "jnxPingCtlJseriesHWTimeStamp": jnxPingCtlJseriesHWTimeStamp,
       "jnxPingCtlOneWayHWTimeStamp": jnxPingCtlOneWayHWTimeStamp,
       "jnxPingCtlMovAvgSize": jnxPingCtlMovAvgSize,
       "jnxPingCtlMXseriesHWTimeStamp": jnxPingCtlMXseriesHWTimeStamp,
       "jnxPingCtlEXseriesHWTimeStamp": jnxPingCtlEXseriesHWTimeStamp,
       "jnxPingResultsTable": jnxPingResultsTable,
       "jnxPingResultsEntry": jnxPingResultsEntry,
       "jnxPingResultsRttUs": jnxPingResultsRttUs,
       "jnxPingResultsSumRttUs": jnxPingResultsSumRttUs,
       "jnxPingResultsMinRttUs": jnxPingResultsMinRttUs,
       "jnxPingResultsMaxRttUs": jnxPingResultsMaxRttUs,
       "jnxPingResultsAvgRttUs": jnxPingResultsAvgRttUs,
       "jnxPingResultsStdDevRttUs": jnxPingResultsStdDevRttUs,
       "jnxPingResultsEgressUs": jnxPingResultsEgressUs,
       "jnxPingResultsMinEgressUs": jnxPingResultsMinEgressUs,
       "jnxPingResultsMaxEgressUs": jnxPingResultsMaxEgressUs,
       "jnxPingResultsAvgEgressUs": jnxPingResultsAvgEgressUs,
       "jnxPingResultsStddevEgressUs": jnxPingResultsStddevEgressUs,
       "jnxPingResultsIngressUs": jnxPingResultsIngressUs,
       "jnxPingResultsMinIngressUs": jnxPingResultsMinIngressUs,
       "jnxPingResultsMaxIngressUs": jnxPingResultsMaxIngressUs,
       "jnxPingResultsAvgIngressUs": jnxPingResultsAvgIngressUs,
       "jnxPingResultsStddevIngressUs": jnxPingResultsStddevIngressUs,
       "jnxPingResultsJitterRttUs": jnxPingResultsJitterRttUs,
       "jnxPingResultsJitterEgressUs": jnxPingResultsJitterEgressUs,
       "jnxPingResultsJitterIngressUs": jnxPingResultsJitterIngressUs,
       "jnxPingResultsStatus": jnxPingResultsStatus,
       "jnxPingResultsTime": jnxPingResultsTime,
       "jnxPingResultsOwnerIndex": jnxPingResultsOwnerIndex,
       "jnxPingResultsTestName": jnxPingResultsTestName,
       "jnxPingProbeHistoryTable": jnxPingProbeHistoryTable,
       "jnxPingProbeHistoryEntry": jnxPingProbeHistoryEntry,
       "jnxPingProbeHistoryResponseUs": jnxPingProbeHistoryResponseUs,
       "jnxPingProbeHistoryJitterUs": jnxPingProbeHistoryJitterUs,
       "jnxPingProbeHistoryResponseEgressUs": jnxPingProbeHistoryResponseEgressUs,
       "jnxPingProbeHistoryResponseIngressUs": jnxPingProbeHistoryResponseIngressUs,
       "jnxPingProbeHistoryEgressJitterUs": jnxPingProbeHistoryEgressJitterUs,
       "jnxPingProbeHistoryIngressJitterUs": jnxPingProbeHistoryIngressJitterUs,
       "jnxPingLastTestResultTable": jnxPingLastTestResultTable,
       "jnxPingLastTestResultEntry": jnxPingLastTestResultEntry,
       "jnxPingLastTestResultProbeResponses": jnxPingLastTestResultProbeResponses,
       "jnxPingLastTestResultSentProbes": jnxPingLastTestResultSentProbes,
       "jnxPingLastTestResultSumRttUs": jnxPingLastTestResultSumRttUs,
       "jnxPingLastTestResultMinRttUs": jnxPingLastTestResultMinRttUs,
       "jnxPingLastTestResultMaxRttUs": jnxPingLastTestResultMaxRttUs,
       "jnxPingLastTestResultAvgRttUs": jnxPingLastTestResultAvgRttUs,
       "jnxPingLastTestResultStdDevRttUs": jnxPingLastTestResultStdDevRttUs,
       "jnxPingLastTestResultMinEgressUs": jnxPingLastTestResultMinEgressUs,
       "jnxPingLastTestResultMaxEgressUs": jnxPingLastTestResultMaxEgressUs,
       "jnxPingLastTestResultAvgEgressUs": jnxPingLastTestResultAvgEgressUs,
       "jnxPingLastTestResultStddevEgressUs": jnxPingLastTestResultStddevEgressUs,
       "jnxPingLastTestResultMinIngressUs": jnxPingLastTestResultMinIngressUs,
       "jnxPingLastTestResultMaxIngressUs": jnxPingLastTestResultMaxIngressUs,
       "jnxPingLastTestResultAvgIngressUs": jnxPingLastTestResultAvgIngressUs,
       "jnxPingLastTestResultStddevIngressUs": jnxPingLastTestResultStddevIngressUs,
       "jnxPingLastTestResultPeakToPeakJitterRttUs": jnxPingLastTestResultPeakToPeakJitterRttUs,
       "jnxPingLastTestResultPeakToPeakJitterEgressUs": jnxPingLastTestResultPeakToPeakJitterEgressUs,
       "jnxPingLastTestResultPeakToPeakJitterIngressUs": jnxPingLastTestResultPeakToPeakJitterIngressUs,
       "jnxPingLastTestResultTime": jnxPingLastTestResultTime,
       "jnxPingImplementationTypeDomains": jnxPingImplementationTypeDomains,
       "jnxPingIcmpTimeStamp": jnxPingIcmpTimeStamp,
       "jnxPingHttpGet": jnxPingHttpGet,
       "jnxPingHttpGetMetadata": jnxPingHttpGetMetadata,
       "jnxPingDnsQuery": jnxPingDnsQuery,
       "jnxPingNtpQuery": jnxPingNtpQuery,
       "jnxPingUdpTimestamp": jnxPingUdpTimestamp,
       "jnxPingNotificationPrefix": jnxPingNotificationPrefix,
       "jnxPingRttThresholdExceeded": jnxPingRttThresholdExceeded,
       "jnxPingRttStdDevThresholdExceeded": jnxPingRttStdDevThresholdExceeded,
       "jnxPingRttJitterThresholdExceeded": jnxPingRttJitterThresholdExceeded,
       "jnxPingEgressThresholdExceeded": jnxPingEgressThresholdExceeded,
       "jnxPingEgressStdDevThresholdExceeded": jnxPingEgressStdDevThresholdExceeded,
       "jnxPingEgressJitterThresholdExceeded": jnxPingEgressJitterThresholdExceeded,
       "jnxPingIngressThresholdExceeded": jnxPingIngressThresholdExceeded,
       "jnxPingIngressStddevThresholdExceeded": jnxPingIngressStddevThresholdExceeded,
       "jnxPingIngressJitterThresholdExceeded": jnxPingIngressJitterThresholdExceeded}
)
