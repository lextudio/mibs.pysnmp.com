# SNMP MIB module (TIMETRA-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:03:54 2024
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
 MacAddress,
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")

(tmnxChassisIndex,
 tmnxHwConformance,
 tmnxHwNotification,
 tmnxHwObjs) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex",
    "tmnxHwConformance",
    "tmnxHwNotification",
    "tmnxHwObjs")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(tmnxPortPortID,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortPortID")


# MODULE-IDENTITY

tmnxPppMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 26)
)
tmnxPppMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-03-15 00:00",
         "1905-01-24 00:00",
         "1904-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPppCpState(Integer32, TextualConvention):
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
        *(("ackReceived", 8),
          ("ackSent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("requestSent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxPppConformance_ObjectIdentity = ObjectIdentity
tmnxPppConformance = _TmnxPppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3)
)
_TmnxPppCompliances_ObjectIdentity = ObjectIdentity
tmnxPppCompliances = _TmnxPppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 1)
)
_TmnxPppGroups_ObjectIdentity = ObjectIdentity
tmnxPppGroups = _TmnxPppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 2)
)
_TmnxPppObjs_ObjectIdentity = ObjectIdentity
tmnxPppObjs = _TmnxPppObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5)
)
_TmnxPppTable_Object = MibTable
tmnxPppTable = _TmnxPppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPppTable.setStatus("current")
_TmnxPppEntry_Object = MibTableRow
tmnxPppEntry = _TmnxPppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1)
)
tmnxPppEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxPppEntry.setStatus("current")


class _TmnxPppLinkPhase_Type(Integer32):
    """Custom type tmnxPppLinkPhase based on Integer32"""
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
        *(("authenticate", 3),
          ("dead", 1),
          ("establish", 2),
          ("network", 4),
          ("terminate", 5))
    )


_TmnxPppLinkPhase_Type.__name__ = "Integer32"
_TmnxPppLinkPhase_Object = MibTableColumn
tmnxPppLinkPhase = _TmnxPppLinkPhase_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 1),
    _TmnxPppLinkPhase_Type()
)
tmnxPppLinkPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLinkPhase.setStatus("current")
_TmnxPppLocalAddress_Type = IpAddress
_TmnxPppLocalAddress_Object = MibTableColumn
tmnxPppLocalAddress = _TmnxPppLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 2),
    _TmnxPppLocalAddress_Type()
)
tmnxPppLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLocalAddress.setStatus("obsolete")
_TmnxPppRemoteAddress_Type = IpAddress
_TmnxPppRemoteAddress_Object = MibTableColumn
tmnxPppRemoteAddress = _TmnxPppRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 3),
    _TmnxPppRemoteAddress_Type()
)
tmnxPppRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppRemoteAddress.setStatus("obsolete")
_TmnxPppRemoteMacAddress_Type = MacAddress
_TmnxPppRemoteMacAddress_Object = MibTableColumn
tmnxPppRemoteMacAddress = _TmnxPppRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 4),
    _TmnxPppRemoteMacAddress_Type()
)
tmnxPppRemoteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppRemoteMacAddress.setStatus("current")


class _TmnxPppLineMonitorMethod_Type(Integer32):
    """Custom type tmnxPppLineMonitorMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keepalive", 2),
          ("lqm", 3),
          ("none", 1))
    )


_TmnxPppLineMonitorMethod_Type.__name__ = "Integer32"
_TmnxPppLineMonitorMethod_Object = MibTableColumn
tmnxPppLineMonitorMethod = _TmnxPppLineMonitorMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 5),
    _TmnxPppLineMonitorMethod_Type()
)
tmnxPppLineMonitorMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLineMonitorMethod.setStatus("current")


class _TmnxPppKaPeriod_Type(Unsigned32):
    """Custom type tmnxPppKaPeriod based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TmnxPppKaPeriod_Type.__name__ = "Unsigned32"
_TmnxPppKaPeriod_Object = MibTableColumn
tmnxPppKaPeriod = _TmnxPppKaPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 6),
    _TmnxPppKaPeriod_Type()
)
tmnxPppKaPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppKaPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppKaPeriod.setUnits("seconds")


class _TmnxPppKaDropCount_Type(Unsigned32):
    """Custom type tmnxPppKaDropCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxPppKaDropCount_Type.__name__ = "Unsigned32"
_TmnxPppKaDropCount_Object = MibTableColumn
tmnxPppKaDropCount = _TmnxPppKaDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 7),
    _TmnxPppKaDropCount_Type()
)
tmnxPppKaDropCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppKaDropCount.setStatus("current")
_TmnxPppKaLastClearedTime_Type = TimeStamp
_TmnxPppKaLastClearedTime_Object = MibTableColumn
tmnxPppKaLastClearedTime = _TmnxPppKaLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 8),
    _TmnxPppKaLastClearedTime_Type()
)
tmnxPppKaLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppKaLastClearedTime.setStatus("current")
_TmnxPppKaThresholdExceedsCount_Type = Counter32
_TmnxPppKaThresholdExceedsCount_Object = MibTableColumn
tmnxPppKaThresholdExceedsCount = _TmnxPppKaThresholdExceedsCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 9),
    _TmnxPppKaThresholdExceedsCount_Type()
)
tmnxPppKaThresholdExceedsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppKaThresholdExceedsCount.setStatus("current")
_TmnxPppKaInPktCount_Type = Counter32
_TmnxPppKaInPktCount_Object = MibTableColumn
tmnxPppKaInPktCount = _TmnxPppKaInPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 10),
    _TmnxPppKaInPktCount_Type()
)
tmnxPppKaInPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppKaInPktCount.setStatus("current")
_TmnxPppKaOutPktCount_Type = Counter32
_TmnxPppKaOutPktCount_Object = MibTableColumn
tmnxPppKaOutPktCount = _TmnxPppKaOutPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 11),
    _TmnxPppKaOutPktCount_Type()
)
tmnxPppKaOutPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppKaOutPktCount.setStatus("current")
_TmnxPppKaTimeDropLink_Type = TimeInterval
_TmnxPppKaTimeDropLink_Object = MibTableColumn
tmnxPppKaTimeDropLink = _TmnxPppKaTimeDropLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 12),
    _TmnxPppKaTimeDropLink_Type()
)
tmnxPppKaTimeDropLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppKaTimeDropLink.setStatus("current")


class _TmnxPppQuality_Type(Unsigned32):
    """Custom type tmnxPppQuality based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPppQuality_Type.__name__ = "Unsigned32"
_TmnxPppQuality_Object = MibTableColumn
tmnxPppQuality = _TmnxPppQuality_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 13),
    _TmnxPppQuality_Type()
)
tmnxPppQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppQuality.setStatus("current")


class _TmnxPppLqmOperPeriod_Type(Unsigned32):
    """Custom type tmnxPppLqmOperPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TmnxPppLqmOperPeriod_Type.__name__ = "Unsigned32"
_TmnxPppLqmOperPeriod_Object = MibTableColumn
tmnxPppLqmOperPeriod = _TmnxPppLqmOperPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 14),
    _TmnxPppLqmOperPeriod_Type()
)
tmnxPppLqmOperPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmOperPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppLqmOperPeriod.setUnits("seconds")


class _TmnxPppLqmInRate_Type(Gauge32):
    """Custom type tmnxPppLqmInRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPppLqmInRate_Type.__name__ = "Gauge32"
_TmnxPppLqmInRate_Object = MibTableColumn
tmnxPppLqmInRate = _TmnxPppLqmInRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 15),
    _TmnxPppLqmInRate_Type()
)
tmnxPppLqmInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmInRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppLqmInRate.setUnits("percentage")


class _TmnxPppLqmOutRate_Type(Gauge32):
    """Custom type tmnxPppLqmOutRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPppLqmOutRate_Type.__name__ = "Gauge32"
_TmnxPppLqmOutRate_Object = MibTableColumn
tmnxPppLqmOutRate = _TmnxPppLqmOutRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 16),
    _TmnxPppLqmOutRate_Type()
)
tmnxPppLqmOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmOutRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPppLqmOutRate.setUnits("percentage")
_TmnxPppLqmLastClearedTime_Type = TimeStamp
_TmnxPppLqmLastClearedTime_Object = MibTableColumn
tmnxPppLqmLastClearedTime = _TmnxPppLqmLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 17),
    _TmnxPppLqmLastClearedTime_Type()
)
tmnxPppLqmLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmLastClearedTime.setStatus("current")
_TmnxPppLqmThresholdExceedsCount_Type = Counter32
_TmnxPppLqmThresholdExceedsCount_Object = MibTableColumn
tmnxPppLqmThresholdExceedsCount = _TmnxPppLqmThresholdExceedsCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 18),
    _TmnxPppLqmThresholdExceedsCount_Type()
)
tmnxPppLqmThresholdExceedsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmThresholdExceedsCount.setStatus("current")
_TmnxPppLqmInPktCount_Type = Counter32
_TmnxPppLqmInPktCount_Object = MibTableColumn
tmnxPppLqmInPktCount = _TmnxPppLqmInPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 19),
    _TmnxPppLqmInPktCount_Type()
)
tmnxPppLqmInPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmInPktCount.setStatus("current")
_TmnxPppLqmOutPktCount_Type = Counter32
_TmnxPppLqmOutPktCount_Object = MibTableColumn
tmnxPppLqmOutPktCount = _TmnxPppLqmOutPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 20),
    _TmnxPppLqmOutPktCount_Type()
)
tmnxPppLqmOutPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmOutPktCount.setStatus("current")
_TmnxPppLqmTimeDropLink_Type = TimeInterval
_TmnxPppLqmTimeDropLink_Object = MibTableColumn
tmnxPppLqmTimeDropLink = _TmnxPppLqmTimeDropLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 21),
    _TmnxPppLqmTimeDropLink_Type()
)
tmnxPppLqmTimeDropLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLqmTimeDropLink.setStatus("current")
_TmnxPppLocalMagicNumber_Type = Unsigned32
_TmnxPppLocalMagicNumber_Object = MibTableColumn
tmnxPppLocalMagicNumber = _TmnxPppLocalMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 22),
    _TmnxPppLocalMagicNumber_Type()
)
tmnxPppLocalMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLocalMagicNumber.setStatus("current")
_TmnxPppRemoteMagicNumber_Type = Unsigned32
_TmnxPppRemoteMagicNumber_Object = MibTableColumn
tmnxPppRemoteMagicNumber = _TmnxPppRemoteMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 23),
    _TmnxPppRemoteMagicNumber_Type()
)
tmnxPppRemoteMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppRemoteMagicNumber.setStatus("current")
_TmnxPppLocalIPv4AddressType_Type = InetAddressType
_TmnxPppLocalIPv4AddressType_Object = MibTableColumn
tmnxPppLocalIPv4AddressType = _TmnxPppLocalIPv4AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 24),
    _TmnxPppLocalIPv4AddressType_Type()
)
tmnxPppLocalIPv4AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLocalIPv4AddressType.setStatus("current")


class _TmnxPppLocalIPv4Address_Type(InetAddress):
    """Custom type tmnxPppLocalIPv4Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPppLocalIPv4Address_Type.__name__ = "InetAddress"
_TmnxPppLocalIPv4Address_Object = MibTableColumn
tmnxPppLocalIPv4Address = _TmnxPppLocalIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 25),
    _TmnxPppLocalIPv4Address_Type()
)
tmnxPppLocalIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLocalIPv4Address.setStatus("current")
_TmnxPppLocalIPv6AddressType_Type = InetAddressType
_TmnxPppLocalIPv6AddressType_Object = MibTableColumn
tmnxPppLocalIPv6AddressType = _TmnxPppLocalIPv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 26),
    _TmnxPppLocalIPv6AddressType_Type()
)
tmnxPppLocalIPv6AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLocalIPv6AddressType.setStatus("current")


class _TmnxPppLocalIPv6Address_Type(InetAddress):
    """Custom type tmnxPppLocalIPv6Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxPppLocalIPv6Address_Type.__name__ = "InetAddress"
_TmnxPppLocalIPv6Address_Object = MibTableColumn
tmnxPppLocalIPv6Address = _TmnxPppLocalIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 27),
    _TmnxPppLocalIPv6Address_Type()
)
tmnxPppLocalIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppLocalIPv6Address.setStatus("current")
_TmnxPppRemoteIPv4AddressType_Type = InetAddressType
_TmnxPppRemoteIPv4AddressType_Object = MibTableColumn
tmnxPppRemoteIPv4AddressType = _TmnxPppRemoteIPv4AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 28),
    _TmnxPppRemoteIPv4AddressType_Type()
)
tmnxPppRemoteIPv4AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppRemoteIPv4AddressType.setStatus("current")


class _TmnxPppRemoteIPv4Address_Type(InetAddress):
    """Custom type tmnxPppRemoteIPv4Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPppRemoteIPv4Address_Type.__name__ = "InetAddress"
_TmnxPppRemoteIPv4Address_Object = MibTableColumn
tmnxPppRemoteIPv4Address = _TmnxPppRemoteIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 29),
    _TmnxPppRemoteIPv4Address_Type()
)
tmnxPppRemoteIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppRemoteIPv4Address.setStatus("current")
_TmnxPppRemoteIPv6AddressType_Type = InetAddressType
_TmnxPppRemoteIPv6AddressType_Object = MibTableColumn
tmnxPppRemoteIPv6AddressType = _TmnxPppRemoteIPv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 30),
    _TmnxPppRemoteIPv6AddressType_Type()
)
tmnxPppRemoteIPv6AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppRemoteIPv6AddressType.setStatus("current")


class _TmnxPppRemoteIPv6Address_Type(InetAddress):
    """Custom type tmnxPppRemoteIPv6Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxPppRemoteIPv6Address_Type.__name__ = "InetAddress"
_TmnxPppRemoteIPv6Address_Object = MibTableColumn
tmnxPppRemoteIPv6Address = _TmnxPppRemoteIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 31),
    _TmnxPppRemoteIPv6Address_Type()
)
tmnxPppRemoteIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppRemoteIPv6Address.setStatus("current")


class _TmnxPppHdrCompression_Type(Bits):
    """Custom type tmnxPppHdrCompression based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("acfc", 0),
          ("pfc", 1))
    )

_TmnxPppHdrCompression_Type.__name__ = "Bits"
_TmnxPppHdrCompression_Object = MibTableColumn
tmnxPppHdrCompression = _TmnxPppHdrCompression_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 1, 1, 32),
    _TmnxPppHdrCompression_Type()
)
tmnxPppHdrCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPppHdrCompression.setStatus("current")
_TmnxPppCpTable_Object = MibTable
tmnxPppCpTable = _TmnxPppCpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxPppCpTable.setStatus("current")
_TmnxPppCpEntry_Object = MibTableRow
tmnxPppCpEntry = _TmnxPppCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 2, 1)
)
tmnxPppCpEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-PPP-MIB", "tmnxPppCpProtocol"),
)
if mibBuilder.loadTexts:
    tmnxPppCpEntry.setStatus("current")


class _TmnxPppCpProtocol_Type(Integer32):
    """Custom type tmnxPppCpProtocol based on Integer32"""
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
        *(("bcp", 4),
          ("ipcp", 2),
          ("ipv6cp", 7),
          ("lcp", 1),
          ("lqr", 6),
          ("mplscp", 3),
          ("osicp", 5))
    )


_TmnxPppCpProtocol_Type.__name__ = "Integer32"
_TmnxPppCpProtocol_Object = MibTableColumn
tmnxPppCpProtocol = _TmnxPppCpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 2, 1, 1),
    _TmnxPppCpProtocol_Type()
)
tmnxPppCpProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPppCpProtocol.setStatus("current")
_TmnxPppCpState_Type = TmnxPppCpState
_TmnxPppCpState_Object = MibTableColumn
tmnxPppCpState = _TmnxPppCpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 2, 1, 2),
    _TmnxPppCpState_Type()
)
tmnxPppCpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppCpState.setStatus("current")
_TmnxPppCpLastChange_Type = TimeStamp
_TmnxPppCpLastChange_Object = MibTableColumn
tmnxPppCpLastChange = _TmnxPppCpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 2, 1, 3),
    _TmnxPppCpLastChange_Type()
)
tmnxPppCpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppCpLastChange.setStatus("current")
_TmnxPppCpRestartCount_Type = Counter32
_TmnxPppCpRestartCount_Object = MibTableColumn
tmnxPppCpRestartCount = _TmnxPppCpRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 2, 1, 4),
    _TmnxPppCpRestartCount_Type()
)
tmnxPppCpRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppCpRestartCount.setStatus("current")
_TmnxPppCpLastClearedTime_Type = TimeStamp
_TmnxPppCpLastClearedTime_Object = MibTableColumn
tmnxPppCpLastClearedTime = _TmnxPppCpLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 2, 5, 2, 1, 5),
    _TmnxPppCpLastClearedTime_Type()
)
tmnxPppCpLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPppCpLastClearedTime.setStatus("current")
_TmnxPppNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPppNotifyPrefix = _TmnxPppNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3)
)
_TmnxPppNotification_ObjectIdentity = ObjectIdentity
tmnxPppNotification = _TmnxPppNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0)
)

# Managed Objects groups

tmnxPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 2, 1)
)
tmnxPppGroup.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppLinkPhase"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalAddress"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteAddress"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMacAddress"),
        ("TIMETRA-PPP-MIB", "tmnxPppLineMonitorMethod"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaPeriod"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaDropCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaThresholdExceedsCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaInPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaOutPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaTimeDropLink"),
        ("TIMETRA-PPP-MIB", "tmnxPppQuality"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOperPeriod"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmInRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOutRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmThresholdExceedsCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmInPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOutPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmTimeDropLink"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpState"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpLastChange"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpRestartCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpLastClearedTime"))
)
if mibBuilder.loadTexts:
    tmnxPppGroup.setStatus("obsolete")

tmnxPPPObsoleteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 2, 4)
)
tmnxPPPObsoleteV4v0Group.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppLocalAddress"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteAddress"))
)
if mibBuilder.loadTexts:
    tmnxPPPObsoleteV4v0Group.setStatus("current")

tmnxPpp7450V4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 2, 5)
)
tmnxPpp7450V4v0Group.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppLinkPhase"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMacAddress"),
        ("TIMETRA-PPP-MIB", "tmnxPppLineMonitorMethod"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaPeriod"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaDropCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaThresholdExceedsCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaInPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaOutPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaTimeDropLink"),
        ("TIMETRA-PPP-MIB", "tmnxPppQuality"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOperPeriod"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmInRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOutRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmThresholdExceedsCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmInPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOutPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmTimeDropLink"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpState"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpLastChange"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpRestartCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalIPv4AddressType"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalIPv4Address"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteIPv4AddressType"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteIPv4Address"))
)
if mibBuilder.loadTexts:
    tmnxPpp7450V4v0Group.setStatus("current")

tmnxPpp7750V4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 2, 6)
)
tmnxPpp7750V4v0Group.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppLinkPhase"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMacAddress"),
        ("TIMETRA-PPP-MIB", "tmnxPppLineMonitorMethod"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaPeriod"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaDropCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaThresholdExceedsCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaInPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaOutPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppKaTimeDropLink"),
        ("TIMETRA-PPP-MIB", "tmnxPppQuality"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOperPeriod"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmInRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOutRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmThresholdExceedsCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmInPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOutPktCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmTimeDropLink"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpState"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpLastChange"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpRestartCount"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpLastClearedTime"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalIPv4AddressType"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalIPv4Address"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalIPv6AddressType"),
        ("TIMETRA-PPP-MIB", "tmnxPppLocalIPv6Address"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteIPv4AddressType"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteIPv4Address"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteIPv6AddressType"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteIPv6Address"))
)
if mibBuilder.loadTexts:
    tmnxPpp7750V4v0Group.setStatus("current")

tmnxPppCompressionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 2, 7)
)
tmnxPppCompressionGroup.setObjects(
    ("TIMETRA-PPP-MIB", "tmnxPppHdrCompression")
)
if mibBuilder.loadTexts:
    tmnxPppCompressionGroup.setStatus("current")


# Notification objects

tmnxPppCpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 1)
)
tmnxPppCpUp.setObjects(
    ("TIMETRA-PPP-MIB", "tmnxPppCpState")
)
if mibBuilder.loadTexts:
    tmnxPppCpUp.setStatus(
        "current"
    )

tmnxPppCpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 2)
)
tmnxPppCpDown.setObjects(
    ("TIMETRA-PPP-MIB", "tmnxPppCpState")
)
if mibBuilder.loadTexts:
    tmnxPppCpDown.setStatus(
        "current"
    )

tmnxPppNcpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 3)
)
tmnxPppNcpUp.setObjects(
    ("TIMETRA-PPP-MIB", "tmnxPppCpState")
)
if mibBuilder.loadTexts:
    tmnxPppNcpUp.setStatus(
        "current"
    )

tmnxPppNcpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 4)
)
tmnxPppNcpDown.setObjects(
    ("TIMETRA-PPP-MIB", "tmnxPppCpState")
)
if mibBuilder.loadTexts:
    tmnxPppNcpDown.setStatus(
        "current"
    )

tmnxPppKeepaliveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 5)
)
tmnxPppKeepaliveFailure.setObjects(
    ("TIMETRA-PPP-MIB", "tmnxPppKaPeriod")
)
if mibBuilder.loadTexts:
    tmnxPppKeepaliveFailure.setStatus(
        "current"
    )

tmnxPppLqmFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 6)
)
tmnxPppLqmFailure.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppLqmInRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmOutRate"),
        ("TIMETRA-PPP-MIB", "tmnxPppQuality"))
)
if mibBuilder.loadTexts:
    tmnxPppLqmFailure.setStatus(
        "current"
    )

tmnxPppLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 7)
)
tmnxPppLoopback.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppLocalMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMagicNumber"))
)
if mibBuilder.loadTexts:
    tmnxPppLoopback.setStatus(
        "current"
    )

tmnxPppLoopbackClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 2, 3, 0, 8)
)
tmnxPppLoopbackClear.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppLocalMagicNumber"),
        ("TIMETRA-PPP-MIB", "tmnxPppRemoteMagicNumber"))
)
if mibBuilder.loadTexts:
    tmnxPppLoopbackClear.setStatus(
        "current"
    )


# Notifications groups

tmnxPppNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 2, 3)
)
tmnxPppNotificationGroup.setObjects(
      *(("TIMETRA-PPP-MIB", "tmnxPppCpUp"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpDown"),
        ("TIMETRA-PPP-MIB", "tmnxPppCpDown"),
        ("TIMETRA-PPP-MIB", "tmnxPppNcpUp"),
        ("TIMETRA-PPP-MIB", "tmnxPppNcpDown"),
        ("TIMETRA-PPP-MIB", "tmnxPppKeepaliveFailure"),
        ("TIMETRA-PPP-MIB", "tmnxPppLqmFailure"),
        ("TIMETRA-PPP-MIB", "tmnxPppLoopback"),
        ("TIMETRA-PPP-MIB", "tmnxPppLoopbackClear"))
)
if mibBuilder.loadTexts:
    tmnxPppNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxPppCompliance.setStatus(
        "obsolete"
    )

tmnxPpp7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxPpp7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxPpp7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxPpp7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxPpp7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxPpp7450V6v0Compliance.setStatus(
        "current"
    )

tmnxPpp77x0V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxPpp77x0V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PPP-MIB",
    **{"TmnxPppCpState": TmnxPppCpState,
       "tmnxPppMIBModule": tmnxPppMIBModule,
       "tmnxPppConformance": tmnxPppConformance,
       "tmnxPppCompliances": tmnxPppCompliances,
       "tmnxPppCompliance": tmnxPppCompliance,
       "tmnxPpp7450V4v0Compliance": tmnxPpp7450V4v0Compliance,
       "tmnxPpp7750V4v0Compliance": tmnxPpp7750V4v0Compliance,
       "tmnxPpp7450V6v0Compliance": tmnxPpp7450V6v0Compliance,
       "tmnxPpp77x0V6v0Compliance": tmnxPpp77x0V6v0Compliance,
       "tmnxPppGroups": tmnxPppGroups,
       "tmnxPppGroup": tmnxPppGroup,
       "tmnxPppNotificationGroup": tmnxPppNotificationGroup,
       "tmnxPPPObsoleteV4v0Group": tmnxPPPObsoleteV4v0Group,
       "tmnxPpp7450V4v0Group": tmnxPpp7450V4v0Group,
       "tmnxPpp7750V4v0Group": tmnxPpp7750V4v0Group,
       "tmnxPppCompressionGroup": tmnxPppCompressionGroup,
       "tmnxPppObjs": tmnxPppObjs,
       "tmnxPppTable": tmnxPppTable,
       "tmnxPppEntry": tmnxPppEntry,
       "tmnxPppLinkPhase": tmnxPppLinkPhase,
       "tmnxPppLocalAddress": tmnxPppLocalAddress,
       "tmnxPppRemoteAddress": tmnxPppRemoteAddress,
       "tmnxPppRemoteMacAddress": tmnxPppRemoteMacAddress,
       "tmnxPppLineMonitorMethod": tmnxPppLineMonitorMethod,
       "tmnxPppKaPeriod": tmnxPppKaPeriod,
       "tmnxPppKaDropCount": tmnxPppKaDropCount,
       "tmnxPppKaLastClearedTime": tmnxPppKaLastClearedTime,
       "tmnxPppKaThresholdExceedsCount": tmnxPppKaThresholdExceedsCount,
       "tmnxPppKaInPktCount": tmnxPppKaInPktCount,
       "tmnxPppKaOutPktCount": tmnxPppKaOutPktCount,
       "tmnxPppKaTimeDropLink": tmnxPppKaTimeDropLink,
       "tmnxPppQuality": tmnxPppQuality,
       "tmnxPppLqmOperPeriod": tmnxPppLqmOperPeriod,
       "tmnxPppLqmInRate": tmnxPppLqmInRate,
       "tmnxPppLqmOutRate": tmnxPppLqmOutRate,
       "tmnxPppLqmLastClearedTime": tmnxPppLqmLastClearedTime,
       "tmnxPppLqmThresholdExceedsCount": tmnxPppLqmThresholdExceedsCount,
       "tmnxPppLqmInPktCount": tmnxPppLqmInPktCount,
       "tmnxPppLqmOutPktCount": tmnxPppLqmOutPktCount,
       "tmnxPppLqmTimeDropLink": tmnxPppLqmTimeDropLink,
       "tmnxPppLocalMagicNumber": tmnxPppLocalMagicNumber,
       "tmnxPppRemoteMagicNumber": tmnxPppRemoteMagicNumber,
       "tmnxPppLocalIPv4AddressType": tmnxPppLocalIPv4AddressType,
       "tmnxPppLocalIPv4Address": tmnxPppLocalIPv4Address,
       "tmnxPppLocalIPv6AddressType": tmnxPppLocalIPv6AddressType,
       "tmnxPppLocalIPv6Address": tmnxPppLocalIPv6Address,
       "tmnxPppRemoteIPv4AddressType": tmnxPppRemoteIPv4AddressType,
       "tmnxPppRemoteIPv4Address": tmnxPppRemoteIPv4Address,
       "tmnxPppRemoteIPv6AddressType": tmnxPppRemoteIPv6AddressType,
       "tmnxPppRemoteIPv6Address": tmnxPppRemoteIPv6Address,
       "tmnxPppHdrCompression": tmnxPppHdrCompression,
       "tmnxPppCpTable": tmnxPppCpTable,
       "tmnxPppCpEntry": tmnxPppCpEntry,
       "tmnxPppCpProtocol": tmnxPppCpProtocol,
       "tmnxPppCpState": tmnxPppCpState,
       "tmnxPppCpLastChange": tmnxPppCpLastChange,
       "tmnxPppCpRestartCount": tmnxPppCpRestartCount,
       "tmnxPppCpLastClearedTime": tmnxPppCpLastClearedTime,
       "tmnxPppNotifyPrefix": tmnxPppNotifyPrefix,
       "tmnxPppNotification": tmnxPppNotification,
       "tmnxPppCpUp": tmnxPppCpUp,
       "tmnxPppCpDown": tmnxPppCpDown,
       "tmnxPppNcpUp": tmnxPppNcpUp,
       "tmnxPppNcpDown": tmnxPppNcpDown,
       "tmnxPppKeepaliveFailure": tmnxPppKeepaliveFailure,
       "tmnxPppLqmFailure": tmnxPppLqmFailure,
       "tmnxPppLoopback": tmnxPppLoopback,
       "tmnxPppLoopbackClear": tmnxPppLoopbackClear}
)
