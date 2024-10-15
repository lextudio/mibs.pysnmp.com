# SNMP MIB module (SONUS-SS7-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SS7-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:12 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(PointCode,
 SonusName,
 SonusPointCode,
 SonusPointCodeFormat) = mibBuilder.importSymbols(
    "SONUS-TC",
    "PointCode",
    "SonusName",
    "SonusPointCode",
    "SonusPointCodeFormat")


# MODULE-IDENTITY

sonusSs7ServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SonusSs7GatewayLinkSelection(Integer32, TextualConvention):
    status = "current"
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
        *(("none", 3),
          ("primary", 1),
          ("primaryAlt", 4),
          ("secondary", 2),
          ("secondaryAlt", 5))
    )



# MIB Managed Objects in the order of their OIDs

_SonusSs7ServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusSs7ServicesMIBObjects = _SonusSs7ServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1)
)
_SonusSs7Gateway_ObjectIdentity = ObjectIdentity
sonusSs7Gateway = _SonusSs7Gateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1)
)
_SonusSs7GatewayNextIndex_Type = Integer32
_SonusSs7GatewayNextIndex_Object = MibScalar
sonusSs7GatewayNextIndex = _SonusSs7GatewayNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 1),
    _SonusSs7GatewayNextIndex_Type()
)
sonusSs7GatewayNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayNextIndex.setStatus("current")
_SonusSs7GatewayTable_Object = MibTable
sonusSs7GatewayTable = _SonusSs7GatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusSs7GatewayTable.setStatus("current")
_SonusSs7GatewayEntry_Object = MibTableRow
sonusSs7GatewayEntry = _SonusSs7GatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1)
)
sonusSs7GatewayEntry.setIndexNames(
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7GatewayIndex"),
)
if mibBuilder.loadTexts:
    sonusSs7GatewayEntry.setStatus("current")
_SonusSs7GatewayIndex_Type = Integer32
_SonusSs7GatewayIndex_Object = MibTableColumn
sonusSs7GatewayIndex = _SonusSs7GatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 1),
    _SonusSs7GatewayIndex_Type()
)
sonusSs7GatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayIndex.setStatus("current")


class _SonusSs7GatewayState_Type(Integer32):
    """Custom type sonusSs7GatewayState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusSs7GatewayState_Type.__name__ = "Integer32"
_SonusSs7GatewayState_Object = MibTableColumn
sonusSs7GatewayState = _SonusSs7GatewayState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 2),
    _SonusSs7GatewayState_Type()
)
sonusSs7GatewayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayState.setStatus("current")
_SonusSs7GatewayName_Type = SonusName
_SonusSs7GatewayName_Object = MibTableColumn
sonusSs7GatewayName = _SonusSs7GatewayName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 3),
    _SonusSs7GatewayName_Type()
)
sonusSs7GatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayName.setStatus("current")


class _SonusSs7GatewaySocketType_Type(Integer32):
    """Custom type sonusSs7GatewaySocketType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tcp", 1)
    )


_SonusSs7GatewaySocketType_Type.__name__ = "Integer32"
_SonusSs7GatewaySocketType_Object = MibTableColumn
sonusSs7GatewaySocketType = _SonusSs7GatewaySocketType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 4),
    _SonusSs7GatewaySocketType_Type()
)
sonusSs7GatewaySocketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySocketType.setStatus("current")


class _SonusSs7GatewayActiveHost_Type(Integer32):
    """Custom type sonusSs7GatewayActiveHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_SonusSs7GatewayActiveHost_Type.__name__ = "Integer32"
_SonusSs7GatewayActiveHost_Object = MibTableColumn
sonusSs7GatewayActiveHost = _SonusSs7GatewayActiveHost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 5),
    _SonusSs7GatewayActiveHost_Type()
)
sonusSs7GatewayActiveHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayActiveHost.setStatus("deprecated")


class _SonusSs7GatewayPriHostName_Type(DisplayString):
    """Custom type sonusSs7GatewayPriHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_SonusSs7GatewayPriHostName_Type.__name__ = "DisplayString"
_SonusSs7GatewayPriHostName_Object = MibTableColumn
sonusSs7GatewayPriHostName = _SonusSs7GatewayPriHostName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 6),
    _SonusSs7GatewayPriHostName_Type()
)
sonusSs7GatewayPriHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriHostName.setStatus("current")
_SonusSs7GatewayPriHostIpaddr_Type = IpAddress
_SonusSs7GatewayPriHostIpaddr_Object = MibTableColumn
sonusSs7GatewayPriHostIpaddr = _SonusSs7GatewayPriHostIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 7),
    _SonusSs7GatewayPriHostIpaddr_Type()
)
sonusSs7GatewayPriHostIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriHostIpaddr.setStatus("current")


class _SonusSs7GatewayPriHostMode_Type(Integer32):
    """Custom type sonusSs7GatewayPriHostMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_SonusSs7GatewayPriHostMode_Type.__name__ = "Integer32"
_SonusSs7GatewayPriHostMode_Object = MibTableColumn
sonusSs7GatewayPriHostMode = _SonusSs7GatewayPriHostMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 8),
    _SonusSs7GatewayPriHostMode_Type()
)
sonusSs7GatewayPriHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriHostMode.setStatus("current")


class _SonusSs7GatewayPriHostOosDelayTimer_Type(Integer32):
    """Custom type sonusSs7GatewayPriHostOosDelayTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusSs7GatewayPriHostOosDelayTimer_Type.__name__ = "Integer32"
_SonusSs7GatewayPriHostOosDelayTimer_Object = MibTableColumn
sonusSs7GatewayPriHostOosDelayTimer = _SonusSs7GatewayPriHostOosDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 9),
    _SonusSs7GatewayPriHostOosDelayTimer_Type()
)
sonusSs7GatewayPriHostOosDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriHostOosDelayTimer.setStatus("current")


class _SonusSs7GatewaySecHostName_Type(DisplayString):
    """Custom type sonusSs7GatewaySecHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_SonusSs7GatewaySecHostName_Type.__name__ = "DisplayString"
_SonusSs7GatewaySecHostName_Object = MibTableColumn
sonusSs7GatewaySecHostName = _SonusSs7GatewaySecHostName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 10),
    _SonusSs7GatewaySecHostName_Type()
)
sonusSs7GatewaySecHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecHostName.setStatus("current")
_SonusSs7GatewaySecHostIpaddr_Type = IpAddress
_SonusSs7GatewaySecHostIpaddr_Object = MibTableColumn
sonusSs7GatewaySecHostIpaddr = _SonusSs7GatewaySecHostIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 11),
    _SonusSs7GatewaySecHostIpaddr_Type()
)
sonusSs7GatewaySecHostIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecHostIpaddr.setStatus("current")


class _SonusSs7GatewaySecHostMode_Type(Integer32):
    """Custom type sonusSs7GatewaySecHostMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_SonusSs7GatewaySecHostMode_Type.__name__ = "Integer32"
_SonusSs7GatewaySecHostMode_Object = MibTableColumn
sonusSs7GatewaySecHostMode = _SonusSs7GatewaySecHostMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 12),
    _SonusSs7GatewaySecHostMode_Type()
)
sonusSs7GatewaySecHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecHostMode.setStatus("current")


class _SonusSs7GatewaySecHostOosDelayTimer_Type(Integer32):
    """Custom type sonusSs7GatewaySecHostOosDelayTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SonusSs7GatewaySecHostOosDelayTimer_Type.__name__ = "Integer32"
_SonusSs7GatewaySecHostOosDelayTimer_Object = MibTableColumn
sonusSs7GatewaySecHostOosDelayTimer = _SonusSs7GatewaySecHostOosDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 13),
    _SonusSs7GatewaySecHostOosDelayTimer_Type()
)
sonusSs7GatewaySecHostOosDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecHostOosDelayTimer.setStatus("current")
_SonusSs7GatewayRowStatus_Type = RowStatus
_SonusSs7GatewayRowStatus_Object = MibTableColumn
sonusSs7GatewayRowStatus = _SonusSs7GatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 14),
    _SonusSs7GatewayRowStatus_Type()
)
sonusSs7GatewayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayRowStatus.setStatus("current")
_SonusSs7GatewayPriAltHostIpaddr_Type = IpAddress
_SonusSs7GatewayPriAltHostIpaddr_Object = MibTableColumn
sonusSs7GatewayPriAltHostIpaddr = _SonusSs7GatewayPriAltHostIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 15),
    _SonusSs7GatewayPriAltHostIpaddr_Type()
)
sonusSs7GatewayPriAltHostIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriAltHostIpaddr.setStatus("current")
_SonusSs7GatewaySecAltHostIpaddr_Type = IpAddress
_SonusSs7GatewaySecAltHostIpaddr_Object = MibTableColumn
sonusSs7GatewaySecAltHostIpaddr = _SonusSs7GatewaySecAltHostIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 16),
    _SonusSs7GatewaySecAltHostIpaddr_Type()
)
sonusSs7GatewaySecAltHostIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecAltHostIpaddr.setStatus("current")


class _SonusSs7GatewayGwType_Type(Integer32):
    """Custom type sonusSs7GatewayGwType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dgms", 2),
          ("tali", 1))
    )


_SonusSs7GatewayGwType_Type.__name__ = "Integer32"
_SonusSs7GatewayGwType_Object = MibTableColumn
sonusSs7GatewayGwType = _SonusSs7GatewayGwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 17),
    _SonusSs7GatewayGwType_Type()
)
sonusSs7GatewayGwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayGwType.setStatus("current")


class _SonusSs7GatewayServerTcpPort_Type(Integer32):
    """Custom type sonusSs7GatewayServerTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_SonusSs7GatewayServerTcpPort_Type.__name__ = "Integer32"
_SonusSs7GatewayServerTcpPort_Object = MibTableColumn
sonusSs7GatewayServerTcpPort = _SonusSs7GatewayServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 18),
    _SonusSs7GatewayServerTcpPort_Type()
)
sonusSs7GatewayServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayServerTcpPort.setStatus("current")


class _SonusSs7GatewayClientTcpPort_Type(Integer32):
    """Custom type sonusSs7GatewayClientTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_SonusSs7GatewayClientTcpPort_Type.__name__ = "Integer32"
_SonusSs7GatewayClientTcpPort_Object = MibTableColumn
sonusSs7GatewayClientTcpPort = _SonusSs7GatewayClientTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 19),
    _SonusSs7GatewayClientTcpPort_Type()
)
sonusSs7GatewayClientTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayClientTcpPort.setStatus("current")


class _SonusSs7GatewayPriTaliTrafficControl_Type(Integer32):
    """Custom type sonusSs7GatewayPriTaliTrafficControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("prohibit", 2))
    )


_SonusSs7GatewayPriTaliTrafficControl_Type.__name__ = "Integer32"
_SonusSs7GatewayPriTaliTrafficControl_Object = MibTableColumn
sonusSs7GatewayPriTaliTrafficControl = _SonusSs7GatewayPriTaliTrafficControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 20),
    _SonusSs7GatewayPriTaliTrafficControl_Type()
)
sonusSs7GatewayPriTaliTrafficControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriTaliTrafficControl.setStatus("current")


class _SonusSs7GatewayPriAltTaliTrafficControl_Type(Integer32):
    """Custom type sonusSs7GatewayPriAltTaliTrafficControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("prohibit", 2))
    )


_SonusSs7GatewayPriAltTaliTrafficControl_Type.__name__ = "Integer32"
_SonusSs7GatewayPriAltTaliTrafficControl_Object = MibTableColumn
sonusSs7GatewayPriAltTaliTrafficControl = _SonusSs7GatewayPriAltTaliTrafficControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 21),
    _SonusSs7GatewayPriAltTaliTrafficControl_Type()
)
sonusSs7GatewayPriAltTaliTrafficControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriAltTaliTrafficControl.setStatus("current")


class _SonusSs7GatewaySecTaliTrafficControl_Type(Integer32):
    """Custom type sonusSs7GatewaySecTaliTrafficControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("prohibit", 2))
    )


_SonusSs7GatewaySecTaliTrafficControl_Type.__name__ = "Integer32"
_SonusSs7GatewaySecTaliTrafficControl_Object = MibTableColumn
sonusSs7GatewaySecTaliTrafficControl = _SonusSs7GatewaySecTaliTrafficControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 22),
    _SonusSs7GatewaySecTaliTrafficControl_Type()
)
sonusSs7GatewaySecTaliTrafficControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecTaliTrafficControl.setStatus("current")


class _SonusSs7GatewaySecAltTaliTrafficControl_Type(Integer32):
    """Custom type sonusSs7GatewaySecAltTaliTrafficControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("prohibit", 2))
    )


_SonusSs7GatewaySecAltTaliTrafficControl_Type.__name__ = "Integer32"
_SonusSs7GatewaySecAltTaliTrafficControl_Object = MibTableColumn
sonusSs7GatewaySecAltTaliTrafficControl = _SonusSs7GatewaySecAltTaliTrafficControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 23),
    _SonusSs7GatewaySecAltTaliTrafficControl_Type()
)
sonusSs7GatewaySecAltTaliTrafficControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecAltTaliTrafficControl.setStatus("current")


class _SonusSs7GatewayTimerTaliT1_Type(Integer32):
    """Custom type sonusSs7GatewayTimerTaliT1 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_SonusSs7GatewayTimerTaliT1_Type.__name__ = "Integer32"
_SonusSs7GatewayTimerTaliT1_Object = MibTableColumn
sonusSs7GatewayTimerTaliT1 = _SonusSs7GatewayTimerTaliT1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 24),
    _SonusSs7GatewayTimerTaliT1_Type()
)
sonusSs7GatewayTimerTaliT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTimerTaliT1.setStatus("current")


class _SonusSs7GatewayTimerTaliT2_Type(Integer32):
    """Custom type sonusSs7GatewayTimerTaliT2 based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_SonusSs7GatewayTimerTaliT2_Type.__name__ = "Integer32"
_SonusSs7GatewayTimerTaliT2_Object = MibTableColumn
sonusSs7GatewayTimerTaliT2 = _SonusSs7GatewayTimerTaliT2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 25),
    _SonusSs7GatewayTimerTaliT2_Type()
)
sonusSs7GatewayTimerTaliT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTimerTaliT2.setStatus("current")


class _SonusSs7GatewayTimerTaliT3_Type(Integer32):
    """Custom type sonusSs7GatewayTimerTaliT3 based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_SonusSs7GatewayTimerTaliT3_Type.__name__ = "Integer32"
_SonusSs7GatewayTimerTaliT3_Object = MibTableColumn
sonusSs7GatewayTimerTaliT3 = _SonusSs7GatewayTimerTaliT3_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 26),
    _SonusSs7GatewayTimerTaliT3_Type()
)
sonusSs7GatewayTimerTaliT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTimerTaliT3.setStatus("current")


class _SonusSs7GatewayTimerTaliT4_Type(Integer32):
    """Custom type sonusSs7GatewayTimerTaliT4 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_SonusSs7GatewayTimerTaliT4_Type.__name__ = "Integer32"
_SonusSs7GatewayTimerTaliT4_Object = MibTableColumn
sonusSs7GatewayTimerTaliT4 = _SonusSs7GatewayTimerTaliT4_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 27),
    _SonusSs7GatewayTimerTaliT4_Type()
)
sonusSs7GatewayTimerTaliT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTimerTaliT4.setStatus("current")


class _SonusSs7GatewayTaliSs7Type_Type(Integer32):
    """Custom type sonusSs7GatewayTaliSs7Type based on Integer32"""
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
        *(("ansi", 1),
          ("ituIntl", 2),
          ("ituNatl", 3))
    )


_SonusSs7GatewayTaliSs7Type_Type.__name__ = "Integer32"
_SonusSs7GatewayTaliSs7Type_Object = MibTableColumn
sonusSs7GatewayTaliSs7Type = _SonusSs7GatewayTaliSs7Type_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 28),
    _SonusSs7GatewayTaliSs7Type_Type()
)
sonusSs7GatewayTaliSs7Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTaliSs7Type.setStatus("current")


class _SonusSs7GatewaySlsBits_Type(Integer32):
    """Custom type sonusSs7GatewaySlsBits based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_SonusSs7GatewaySlsBits_Type.__name__ = "Integer32"
_SonusSs7GatewaySlsBits_Object = MibTableColumn
sonusSs7GatewaySlsBits = _SonusSs7GatewaySlsBits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 29),
    _SonusSs7GatewaySlsBits_Type()
)
sonusSs7GatewaySlsBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewaySlsBits.setStatus("current")


class _SonusSs7GatewayTaliIsupNormalization_Type(Integer32):
    """Custom type sonusSs7GatewayTaliIsupNormalization based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("raw", 2))
    )


_SonusSs7GatewayTaliIsupNormalization_Type.__name__ = "Integer32"
_SonusSs7GatewayTaliIsupNormalization_Object = MibTableColumn
sonusSs7GatewayTaliIsupNormalization = _SonusSs7GatewayTaliIsupNormalization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 30),
    _SonusSs7GatewayTaliIsupNormalization_Type()
)
sonusSs7GatewayTaliIsupNormalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTaliIsupNormalization.setStatus("current")


class _SonusSs7GatewayTaliPstnPresentation_Type(Integer32):
    """Custom type sonusSs7GatewayTaliPstnPresentation based on Integer32"""
    defaultValue = 2

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
        *(("etsiIsup", 2),
          ("grIsup", 4),
          ("q767", 1),
          ("ukIsup", 3))
    )


_SonusSs7GatewayTaliPstnPresentation_Type.__name__ = "Integer32"
_SonusSs7GatewayTaliPstnPresentation_Object = MibTableColumn
sonusSs7GatewayTaliPstnPresentation = _SonusSs7GatewayTaliPstnPresentation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 31),
    _SonusSs7GatewayTaliPstnPresentation_Type()
)
sonusSs7GatewayTaliPstnPresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTaliPstnPresentation.setStatus("current")


class _SonusSs7GatewayTaliGroupCode_Type(DisplayString):
    """Custom type sonusSs7GatewayTaliGroupCode based on DisplayString"""
    defaultValue = OctetString("aa")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SonusSs7GatewayTaliGroupCode_Type.__name__ = "DisplayString"
_SonusSs7GatewayTaliGroupCode_Object = MibTableColumn
sonusSs7GatewayTaliGroupCode = _SonusSs7GatewayTaliGroupCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 2, 1, 32),
    _SonusSs7GatewayTaliGroupCode_Type()
)
sonusSs7GatewayTaliGroupCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7GatewayTaliGroupCode.setStatus("current")
_SonusSs7GatewayStatusTable_Object = MibTable
sonusSs7GatewayStatusTable = _SonusSs7GatewayStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusTable.setStatus("current")
_SonusSs7GatewayStatusEntry_Object = MibTableRow
sonusSs7GatewayStatusEntry = _SonusSs7GatewayStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1)
)
sonusSs7GatewayStatusEntry.setIndexNames(
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7GatewayStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusEntry.setStatus("current")
_SonusSs7GatewayStatusIndex_Type = Integer32
_SonusSs7GatewayStatusIndex_Object = MibTableColumn
sonusSs7GatewayStatusIndex = _SonusSs7GatewayStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 1),
    _SonusSs7GatewayStatusIndex_Type()
)
sonusSs7GatewayStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusIndex.setStatus("current")


class _SonusSs7GatewayNextHost_Type(SonusSs7GatewayLinkSelection):
    """Custom type sonusSs7GatewayNextHost based on SonusSs7GatewayLinkSelection"""


_SonusSs7GatewayNextHost_Object = MibTableColumn
sonusSs7GatewayNextHost = _SonusSs7GatewayNextHost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 2),
    _SonusSs7GatewayNextHost_Type()
)
sonusSs7GatewayNextHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayNextHost.setStatus("current")


class _SonusSs7GatewaySelectHost_Type(SonusSs7GatewayLinkSelection):
    """Custom type sonusSs7GatewaySelectHost based on SonusSs7GatewayLinkSelection"""


_SonusSs7GatewaySelectHost_Object = MibTableColumn
sonusSs7GatewaySelectHost = _SonusSs7GatewaySelectHost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 3),
    _SonusSs7GatewaySelectHost_Type()
)
sonusSs7GatewaySelectHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewaySelectHost.setStatus("current")


class _SonusSs7GatewayPriTaliConnState_Type(Integer32):
    """Custom type sonusSs7GatewayPriTaliConnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 2),
          ("neaFea", 6),
          ("neaFep", 5),
          ("nepFea", 4),
          ("nepFep", 3),
          ("oos", 1))
    )


_SonusSs7GatewayPriTaliConnState_Type.__name__ = "Integer32"
_SonusSs7GatewayPriTaliConnState_Object = MibTableColumn
sonusSs7GatewayPriTaliConnState = _SonusSs7GatewayPriTaliConnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 4),
    _SonusSs7GatewayPriTaliConnState_Type()
)
sonusSs7GatewayPriTaliConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriTaliConnState.setStatus("current")


class _SonusSs7GatewaySecTaliConnState_Type(Integer32):
    """Custom type sonusSs7GatewaySecTaliConnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 2),
          ("neaFea", 6),
          ("neaFep", 5),
          ("nepFea", 4),
          ("nepFep", 3),
          ("oos", 1))
    )


_SonusSs7GatewaySecTaliConnState_Type.__name__ = "Integer32"
_SonusSs7GatewaySecTaliConnState_Object = MibTableColumn
sonusSs7GatewaySecTaliConnState = _SonusSs7GatewaySecTaliConnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 5),
    _SonusSs7GatewaySecTaliConnState_Type()
)
sonusSs7GatewaySecTaliConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecTaliConnState.setStatus("current")


class _SonusSs7GatewayPriAltTaliConnState_Type(Integer32):
    """Custom type sonusSs7GatewayPriAltTaliConnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 2),
          ("neaFea", 6),
          ("neaFep", 5),
          ("nepFea", 4),
          ("nepFep", 3),
          ("oos", 1))
    )


_SonusSs7GatewayPriAltTaliConnState_Type.__name__ = "Integer32"
_SonusSs7GatewayPriAltTaliConnState_Object = MibTableColumn
sonusSs7GatewayPriAltTaliConnState = _SonusSs7GatewayPriAltTaliConnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 6),
    _SonusSs7GatewayPriAltTaliConnState_Type()
)
sonusSs7GatewayPriAltTaliConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriAltTaliConnState.setStatus("current")


class _SonusSs7GatewaySecAltTaliConnState_Type(Integer32):
    """Custom type sonusSs7GatewaySecAltTaliConnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 2),
          ("neaFea", 6),
          ("neaFep", 5),
          ("nepFea", 4),
          ("nepFep", 3),
          ("oos", 1))
    )


_SonusSs7GatewaySecAltTaliConnState_Type.__name__ = "Integer32"
_SonusSs7GatewaySecAltTaliConnState_Object = MibTableColumn
sonusSs7GatewaySecAltTaliConnState = _SonusSs7GatewaySecAltTaliConnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 7),
    _SonusSs7GatewaySecAltTaliConnState_Type()
)
sonusSs7GatewaySecAltTaliConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecAltTaliConnState.setStatus("current")


class _SonusSs7GatewayPriNearEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewayPriNearEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewayPriNearEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewayPriNearEndTaliVersion_Object = MibTableColumn
sonusSs7GatewayPriNearEndTaliVersion = _SonusSs7GatewayPriNearEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 8),
    _SonusSs7GatewayPriNearEndTaliVersion_Type()
)
sonusSs7GatewayPriNearEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriNearEndTaliVersion.setStatus("current")


class _SonusSs7GatewayPriFarEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewayPriFarEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewayPriFarEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewayPriFarEndTaliVersion_Object = MibTableColumn
sonusSs7GatewayPriFarEndTaliVersion = _SonusSs7GatewayPriFarEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 9),
    _SonusSs7GatewayPriFarEndTaliVersion_Type()
)
sonusSs7GatewayPriFarEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriFarEndTaliVersion.setStatus("current")


class _SonusSs7GatewayPriAltNearEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewayPriAltNearEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewayPriAltNearEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewayPriAltNearEndTaliVersion_Object = MibTableColumn
sonusSs7GatewayPriAltNearEndTaliVersion = _SonusSs7GatewayPriAltNearEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 10),
    _SonusSs7GatewayPriAltNearEndTaliVersion_Type()
)
sonusSs7GatewayPriAltNearEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriAltNearEndTaliVersion.setStatus("current")


class _SonusSs7GatewayPriAltFarEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewayPriAltFarEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewayPriAltFarEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewayPriAltFarEndTaliVersion_Object = MibTableColumn
sonusSs7GatewayPriAltFarEndTaliVersion = _SonusSs7GatewayPriAltFarEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 11),
    _SonusSs7GatewayPriAltFarEndTaliVersion_Type()
)
sonusSs7GatewayPriAltFarEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPriAltFarEndTaliVersion.setStatus("current")


class _SonusSs7GatewaySecNearEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewaySecNearEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewaySecNearEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewaySecNearEndTaliVersion_Object = MibTableColumn
sonusSs7GatewaySecNearEndTaliVersion = _SonusSs7GatewaySecNearEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 12),
    _SonusSs7GatewaySecNearEndTaliVersion_Type()
)
sonusSs7GatewaySecNearEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecNearEndTaliVersion.setStatus("current")


class _SonusSs7GatewaySecFarEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewaySecFarEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewaySecFarEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewaySecFarEndTaliVersion_Object = MibTableColumn
sonusSs7GatewaySecFarEndTaliVersion = _SonusSs7GatewaySecFarEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 13),
    _SonusSs7GatewaySecFarEndTaliVersion_Type()
)
sonusSs7GatewaySecFarEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecFarEndTaliVersion.setStatus("current")


class _SonusSs7GatewaySecAltNearEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewaySecAltNearEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewaySecAltNearEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewaySecAltNearEndTaliVersion_Object = MibTableColumn
sonusSs7GatewaySecAltNearEndTaliVersion = _SonusSs7GatewaySecAltNearEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 14),
    _SonusSs7GatewaySecAltNearEndTaliVersion_Type()
)
sonusSs7GatewaySecAltNearEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecAltNearEndTaliVersion.setStatus("current")


class _SonusSs7GatewaySecAltFarEndTaliVersion_Type(DisplayString):
    """Custom type sonusSs7GatewaySecAltFarEndTaliVersion based on DisplayString"""
    defaultValue = OctetString("001.000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SonusSs7GatewaySecAltFarEndTaliVersion_Type.__name__ = "DisplayString"
_SonusSs7GatewaySecAltFarEndTaliVersion_Object = MibTableColumn
sonusSs7GatewaySecAltFarEndTaliVersion = _SonusSs7GatewaySecAltFarEndTaliVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 3, 1, 15),
    _SonusSs7GatewaySecAltFarEndTaliVersion_Type()
)
sonusSs7GatewaySecAltFarEndTaliVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewaySecAltFarEndTaliVersion.setStatus("current")
_SonusSs7GatewayPSStatusTable_Object = MibTable
sonusSs7GatewayPSStatusTable = _SonusSs7GatewayPSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sonusSs7GatewayPSStatusTable.setStatus("current")
_SonusSs7GatewayPSStatusEntry_Object = MibTableRow
sonusSs7GatewayPSStatusEntry = _SonusSs7GatewayPSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 4, 1)
)
sonusSs7GatewayPSStatusEntry.setIndexNames(
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7GatewayPSStatusIndex"),
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7GatewayPSStatusPSIndex"),
)
if mibBuilder.loadTexts:
    sonusSs7GatewayPSStatusEntry.setStatus("current")
_SonusSs7GatewayPSStatusIndex_Type = Integer32
_SonusSs7GatewayPSStatusIndex_Object = MibTableColumn
sonusSs7GatewayPSStatusIndex = _SonusSs7GatewayPSStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 4, 1, 1),
    _SonusSs7GatewayPSStatusIndex_Type()
)
sonusSs7GatewayPSStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPSStatusIndex.setStatus("current")


class _SonusSs7GatewayPSStatusPSIndex_Type(Integer32):
    """Custom type sonusSs7GatewayPSStatusPSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("primaryAlt", 2),
          ("secondary", 1),
          ("secondaryAlt", 3))
    )


_SonusSs7GatewayPSStatusPSIndex_Type.__name__ = "Integer32"
_SonusSs7GatewayPSStatusPSIndex_Object = MibTableColumn
sonusSs7GatewayPSStatusPSIndex = _SonusSs7GatewayPSStatusPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 4, 1, 2),
    _SonusSs7GatewayPSStatusPSIndex_Type()
)
sonusSs7GatewayPSStatusPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPSStatusPSIndex.setStatus("current")
_SonusSs7GatewayPSStatusPrimaryCE_Type = Integer32
_SonusSs7GatewayPSStatusPrimaryCE_Object = MibTableColumn
sonusSs7GatewayPSStatusPrimaryCE = _SonusSs7GatewayPSStatusPrimaryCE_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 4, 1, 3),
    _SonusSs7GatewayPSStatusPrimaryCE_Type()
)
sonusSs7GatewayPSStatusPrimaryCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPSStatusPrimaryCE.setStatus("current")


class _SonusSs7GatewayPSStatusActiveLink_Type(Integer32):
    """Custom type sonusSs7GatewayPSStatusActiveLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SonusSs7GatewayPSStatusActiveLink_Type.__name__ = "Integer32"
_SonusSs7GatewayPSStatusActiveLink_Object = MibTableColumn
sonusSs7GatewayPSStatusActiveLink = _SonusSs7GatewayPSStatusActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 4, 1, 4),
    _SonusSs7GatewayPSStatusActiveLink_Type()
)
sonusSs7GatewayPSStatusActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayPSStatusActiveLink.setStatus("current")
_SonusSs7GatewayLinkStatusTable_Object = MibTable
sonusSs7GatewayLinkStatusTable = _SonusSs7GatewayLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sonusSs7GatewayLinkStatusTable.setStatus("current")
_SonusSs7GatewayLinkStatusEntry_Object = MibTableRow
sonusSs7GatewayLinkStatusEntry = _SonusSs7GatewayLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1)
)
sonusSs7GatewayLinkStatusEntry.setIndexNames(
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7GatewayStatusLinkIndex"),
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7GatewayStatusLinkPSIndex"),
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7GatewayStatusLinkHostIndex"),
)
if mibBuilder.loadTexts:
    sonusSs7GatewayLinkStatusEntry.setStatus("current")
_SonusSs7GatewayStatusLinkIndex_Type = Integer32
_SonusSs7GatewayStatusLinkIndex_Object = MibTableColumn
sonusSs7GatewayStatusLinkIndex = _SonusSs7GatewayStatusLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1, 1),
    _SonusSs7GatewayStatusLinkIndex_Type()
)
sonusSs7GatewayStatusLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusLinkIndex.setStatus("current")


class _SonusSs7GatewayStatusLinkPSIndex_Type(Integer32):
    """Custom type sonusSs7GatewayStatusLinkPSIndex based on Integer32"""
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
        *(("primary", 1),
          ("primaryAlt", 3),
          ("secondary", 2),
          ("secondaryAlt", 4))
    )


_SonusSs7GatewayStatusLinkPSIndex_Type.__name__ = "Integer32"
_SonusSs7GatewayStatusLinkPSIndex_Object = MibTableColumn
sonusSs7GatewayStatusLinkPSIndex = _SonusSs7GatewayStatusLinkPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1, 2),
    _SonusSs7GatewayStatusLinkPSIndex_Type()
)
sonusSs7GatewayStatusLinkPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusLinkPSIndex.setStatus("current")
_SonusSs7GatewayStatusLinkHostIndex_Type = Integer32
_SonusSs7GatewayStatusLinkHostIndex_Object = MibTableColumn
sonusSs7GatewayStatusLinkHostIndex = _SonusSs7GatewayStatusLinkHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1, 3),
    _SonusSs7GatewayStatusLinkHostIndex_Type()
)
sonusSs7GatewayStatusLinkHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusLinkHostIndex.setStatus("current")


class _SonusSs7GatewayStatusHostName_Type(DisplayString):
    """Custom type sonusSs7GatewayStatusHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_SonusSs7GatewayStatusHostName_Type.__name__ = "DisplayString"
_SonusSs7GatewayStatusHostName_Object = MibTableColumn
sonusSs7GatewayStatusHostName = _SonusSs7GatewayStatusHostName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1, 4),
    _SonusSs7GatewayStatusHostName_Type()
)
sonusSs7GatewayStatusHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusHostName.setStatus("current")
_SonusSs7GatewayStatusHostIpaddr_Type = IpAddress
_SonusSs7GatewayStatusHostIpaddr_Object = MibTableColumn
sonusSs7GatewayStatusHostIpaddr = _SonusSs7GatewayStatusHostIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1, 5),
    _SonusSs7GatewayStatusHostIpaddr_Type()
)
sonusSs7GatewayStatusHostIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusHostIpaddr.setStatus("current")


class _SonusSs7GatewayStatusHostState_Type(Integer32):
    """Custom type sonusSs7GatewayStatusHostState based on Integer32"""
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
        *(("available", 3),
          ("broken", 4),
          ("empty", 1),
          ("init", 2))
    )


_SonusSs7GatewayStatusHostState_Type.__name__ = "Integer32"
_SonusSs7GatewayStatusHostState_Object = MibTableColumn
sonusSs7GatewayStatusHostState = _SonusSs7GatewayStatusHostState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1, 6),
    _SonusSs7GatewayStatusHostState_Type()
)
sonusSs7GatewayStatusHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusHostState.setStatus("current")
_SonusSs7GatewayStatusHostCE_Type = Integer32
_SonusSs7GatewayStatusHostCE_Object = MibTableColumn
sonusSs7GatewayStatusHostCE = _SonusSs7GatewayStatusHostCE_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 5, 1, 7),
    _SonusSs7GatewayStatusHostCE_Type()
)
sonusSs7GatewayStatusHostCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7GatewayStatusHostCE.setStatus("current")
_SonusSs7NodeStatusTable_Object = MibTable
sonusSs7NodeStatusTable = _SonusSs7NodeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sonusSs7NodeStatusTable.setStatus("current")
_SonusSs7NodeStatusEntry_Object = MibTableRow
sonusSs7NodeStatusEntry = _SonusSs7NodeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 6, 1)
)
sonusSs7NodeStatusEntry.setIndexNames(
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7NodeStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusSs7NodeStatusEntry.setStatus("current")
_SonusSs7NodeStatusIndex_Type = Integer32
_SonusSs7NodeStatusIndex_Object = MibTableColumn
sonusSs7NodeStatusIndex = _SonusSs7NodeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 6, 1, 1),
    _SonusSs7NodeStatusIndex_Type()
)
sonusSs7NodeStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeStatusIndex.setStatus("current")


class _SonusSs7NodeStatIsup_Type(Integer32):
    """Custom type sonusSs7NodeStatIsup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("congested", 6),
          ("disabled", 5),
          ("failed", 4),
          ("initializing", 3),
          ("offline", 1))
    )


_SonusSs7NodeStatIsup_Type.__name__ = "Integer32"
_SonusSs7NodeStatIsup_Object = MibTableColumn
sonusSs7NodeStatIsup = _SonusSs7NodeStatIsup_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 6, 1, 2),
    _SonusSs7NodeStatIsup_Type()
)
sonusSs7NodeStatIsup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeStatIsup.setStatus("current")


class _SonusSs7NodeStatMtp_Type(Integer32):
    """Custom type sonusSs7NodeStatMtp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("paused", 1),
          ("resumed", 2))
    )


_SonusSs7NodeStatMtp_Type.__name__ = "Integer32"
_SonusSs7NodeStatMtp_Object = MibTableColumn
sonusSs7NodeStatMtp = _SonusSs7NodeStatMtp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 1, 6, 1, 3),
    _SonusSs7NodeStatMtp_Type()
)
sonusSs7NodeStatMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeStatMtp.setStatus("current")
_SonusSs7Node_ObjectIdentity = ObjectIdentity
sonusSs7Node = _SonusSs7Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2)
)
_SonusSs7NodeNextIndex_Type = Integer32
_SonusSs7NodeNextIndex_Object = MibScalar
sonusSs7NodeNextIndex = _SonusSs7NodeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 1),
    _SonusSs7NodeNextIndex_Type()
)
sonusSs7NodeNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeNextIndex.setStatus("current")
_SonusSs7NodeTable_Object = MibTable
sonusSs7NodeTable = _SonusSs7NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusSs7NodeTable.setStatus("current")
_SonusSs7NodeEntry_Object = MibTableRow
sonusSs7NodeEntry = _SonusSs7NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1)
)
sonusSs7NodeEntry.setIndexNames(
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7NodeIndex"),
)
if mibBuilder.loadTexts:
    sonusSs7NodeEntry.setStatus("current")
_SonusSs7NodeIndex_Type = Integer32
_SonusSs7NodeIndex_Object = MibTableColumn
sonusSs7NodeIndex = _SonusSs7NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 1),
    _SonusSs7NodeIndex_Type()
)
sonusSs7NodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeIndex.setStatus("current")


class _SonusSs7NodeState_Type(Integer32):
    """Custom type sonusSs7NodeState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusSs7NodeState_Type.__name__ = "Integer32"
_SonusSs7NodeState_Object = MibTableColumn
sonusSs7NodeState = _SonusSs7NodeState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 2),
    _SonusSs7NodeState_Type()
)
sonusSs7NodeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeState.setStatus("current")
_SonusSs7NodeName_Type = SonusName
_SonusSs7NodeName_Object = MibTableColumn
sonusSs7NodeName = _SonusSs7NodeName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 3),
    _SonusSs7NodeName_Type()
)
sonusSs7NodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeName.setStatus("current")
_SonusSs7NodePointCode_Type = PointCode
_SonusSs7NodePointCode_Object = MibTableColumn
sonusSs7NodePointCode = _SonusSs7NodePointCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 4),
    _SonusSs7NodePointCode_Type()
)
sonusSs7NodePointCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodePointCode.setStatus("current")


class _SonusSs7NodeServices_Type(Integer32):
    """Custom type sonusSs7NodeServices based on Integer32"""
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
        *(("isupAndTcap", 3),
          ("isupOnly", 1),
          ("tcapOnly", 2))
    )


_SonusSs7NodeServices_Type.__name__ = "Integer32"
_SonusSs7NodeServices_Object = MibTableColumn
sonusSs7NodeServices = _SonusSs7NodeServices_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 5),
    _SonusSs7NodeServices_Type()
)
sonusSs7NodeServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeServices.setStatus("current")


class _SonusSs7NodeProtocol_Type(Integer32):
    """Custom type sonusSs7NodeProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ansi", 1),
          ("etsi", 3),
          ("itu", 2),
          ("japan", 4))
    )


_SonusSs7NodeProtocol_Type.__name__ = "Integer32"
_SonusSs7NodeProtocol_Object = MibTableColumn
sonusSs7NodeProtocol = _SonusSs7NodeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 6),
    _SonusSs7NodeProtocol_Type()
)
sonusSs7NodeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeProtocol.setStatus("current")


class _SonusSs7NodeTcapSsn_Type(Integer32):
    """Custom type sonusSs7NodeTcapSsn based on Integer32"""
    defaultValue = 0


_SonusSs7NodeTcapSsn_Object = MibTableColumn
sonusSs7NodeTcapSsn = _SonusSs7NodeTcapSsn_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 7),
    _SonusSs7NodeTcapSsn_Type()
)
sonusSs7NodeTcapSsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTcapSsn.setStatus("obsolete")


class _SonusSs7NodeIsupStatus_Type(Integer32):
    """Custom type sonusSs7NodeIsupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("congested", 6),
          ("disabled", 5),
          ("failed", 4),
          ("initializing", 3),
          ("offline", 1))
    )


_SonusSs7NodeIsupStatus_Type.__name__ = "Integer32"
_SonusSs7NodeIsupStatus_Object = MibTableColumn
sonusSs7NodeIsupStatus = _SonusSs7NodeIsupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 8),
    _SonusSs7NodeIsupStatus_Type()
)
sonusSs7NodeIsupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeIsupStatus.setStatus("deprecated")


class _SonusSs7NodeTcapStatus_Type(Integer32):
    """Custom type sonusSs7NodeTcapStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("congested", 6),
          ("disabled", 5),
          ("failed", 4),
          ("initializing", 3),
          ("offline", 1))
    )


_SonusSs7NodeTcapStatus_Type.__name__ = "Integer32"
_SonusSs7NodeTcapStatus_Object = MibTableColumn
sonusSs7NodeTcapStatus = _SonusSs7NodeTcapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 9),
    _SonusSs7NodeTcapStatus_Type()
)
sonusSs7NodeTcapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeTcapStatus.setStatus("obsolete")


class _SonusSs7NodeMtpStatus_Type(Integer32):
    """Custom type sonusSs7NodeMtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("paused", 1),
          ("resumed", 2))
    )


_SonusSs7NodeMtpStatus_Type.__name__ = "Integer32"
_SonusSs7NodeMtpStatus_Object = MibTableColumn
sonusSs7NodeMtpStatus = _SonusSs7NodeMtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 10),
    _SonusSs7NodeMtpStatus_Type()
)
sonusSs7NodeMtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeMtpStatus.setStatus("deprecated")


class _SonusSs7NodeGatewayAssignment_Type(DisplayString):
    """Custom type sonusSs7NodeGatewayAssignment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SonusSs7NodeGatewayAssignment_Type.__name__ = "DisplayString"
_SonusSs7NodeGatewayAssignment_Object = MibTableColumn
sonusSs7NodeGatewayAssignment = _SonusSs7NodeGatewayAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 11),
    _SonusSs7NodeGatewayAssignment_Type()
)
sonusSs7NodeGatewayAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeGatewayAssignment.setStatus("current")


class _SonusSs7NodeNativePointCode_Type(Integer32):
    """Custom type sonusSs7NodeNativePointCode based on Integer32"""
    defaultValue = 0


_SonusSs7NodeNativePointCode_Object = MibTableColumn
sonusSs7NodeNativePointCode = _SonusSs7NodeNativePointCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 12),
    _SonusSs7NodeNativePointCode_Type()
)
sonusSs7NodeNativePointCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeNativePointCode.setStatus("current")


class _SonusSs7NodeMode_Type(Integer32):
    """Custom type sonusSs7NodeMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )


_SonusSs7NodeMode_Type.__name__ = "Integer32"
_SonusSs7NodeMode_Object = MibTableColumn
sonusSs7NodeMode = _SonusSs7NodeMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 13),
    _SonusSs7NodeMode_Type()
)
sonusSs7NodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeMode.setStatus("current")


class _SonusSs7NodeConnCntrl_Type(Integer32):
    """Custom type sonusSs7NodeConnCntrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("asNeeded", 2))
    )


_SonusSs7NodeConnCntrl_Type.__name__ = "Integer32"
_SonusSs7NodeConnCntrl_Object = MibTableColumn
sonusSs7NodeConnCntrl = _SonusSs7NodeConnCntrl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 14),
    _SonusSs7NodeConnCntrl_Type()
)
sonusSs7NodeConnCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeConnCntrl.setStatus("current")
_SonusSs7NodeRowStatus_Type = RowStatus
_SonusSs7NodeRowStatus_Object = MibTableColumn
sonusSs7NodeRowStatus = _SonusSs7NodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 15),
    _SonusSs7NodeRowStatus_Type()
)
sonusSs7NodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeRowStatus.setStatus("current")
_SonusSs7NodeStdPointCode_Type = SonusPointCode
_SonusSs7NodeStdPointCode_Object = MibTableColumn
sonusSs7NodeStdPointCode = _SonusSs7NodeStdPointCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 16),
    _SonusSs7NodeStdPointCode_Type()
)
sonusSs7NodeStdPointCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeStdPointCode.setStatus("current")


class _SonusSs7NodePointCodeSize_Type(Integer32):
    """Custom type sonusSs7NodePointCodeSize based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusSs7NodePointCodeSize_Type.__name__ = "Integer32"
_SonusSs7NodePointCodeSize_Object = MibTableColumn
sonusSs7NodePointCodeSize = _SonusSs7NodePointCodeSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 17),
    _SonusSs7NodePointCodeSize_Type()
)
sonusSs7NodePointCodeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodePointCodeSize.setStatus("current")
_SonusSs7NodePointCodeFormatType_Type = SonusPointCodeFormat
_SonusSs7NodePointCodeFormatType_Object = MibTableColumn
sonusSs7NodePointCodeFormatType = _SonusSs7NodePointCodeFormatType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 18),
    _SonusSs7NodePointCodeFormatType_Type()
)
sonusSs7NodePointCodeFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodePointCodeFormatType.setStatus("current")


class _SonusSs7NodeServerProtocol_Type(Integer32):
    """Custom type sonusSs7NodeServerProtocol based on Integer32"""
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
        *(("dgmsProp", 1),
          ("dgmsRaw", 2),
          ("tekTali", 3))
    )


_SonusSs7NodeServerProtocol_Type.__name__ = "Integer32"
_SonusSs7NodeServerProtocol_Object = MibTableColumn
sonusSs7NodeServerProtocol = _SonusSs7NodeServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 19),
    _SonusSs7NodeServerProtocol_Type()
)
sonusSs7NodeServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeServerProtocol.setStatus("current")


class _SonusSs7NodeHandShakeInterval_Type(Integer32):
    """Custom type sonusSs7NodeHandShakeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusSs7NodeHandShakeInterval_Type.__name__ = "Integer32"
_SonusSs7NodeHandShakeInterval_Object = MibTableColumn
sonusSs7NodeHandShakeInterval = _SonusSs7NodeHandShakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 20),
    _SonusSs7NodeHandShakeInterval_Type()
)
sonusSs7NodeHandShakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeHandShakeInterval.setStatus("current")


class _SonusSs7NodeTimerT1_Type(Integer32):
    """Custom type sonusSs7NodeTimerT1 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7NodeTimerT1_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT1_Object = MibTableColumn
sonusSs7NodeTimerT1 = _SonusSs7NodeTimerT1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 21),
    _SonusSs7NodeTimerT1_Type()
)
sonusSs7NodeTimerT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT1.setStatus("current")


class _SonusSs7NodeTimerT2_Type(Integer32):
    """Custom type sonusSs7NodeTimerT2 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusSs7NodeTimerT2_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT2_Object = MibTableColumn
sonusSs7NodeTimerT2 = _SonusSs7NodeTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 22),
    _SonusSs7NodeTimerT2_Type()
)
sonusSs7NodeTimerT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT2.setStatus("current")


class _SonusSs7NodeTimerT3_Type(Integer32):
    """Custom type sonusSs7NodeTimerT3 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusSs7NodeTimerT3_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT3_Object = MibTableColumn
sonusSs7NodeTimerT3 = _SonusSs7NodeTimerT3_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 23),
    _SonusSs7NodeTimerT3_Type()
)
sonusSs7NodeTimerT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT3.setStatus("current")


class _SonusSs7NodeTimerT4_Type(Integer32):
    """Custom type sonusSs7NodeTimerT4 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 900),
    )


_SonusSs7NodeTimerT4_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT4_Object = MibTableColumn
sonusSs7NodeTimerT4 = _SonusSs7NodeTimerT4_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 24),
    _SonusSs7NodeTimerT4_Type()
)
sonusSs7NodeTimerT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT4.setStatus("current")


class _SonusSs7NodeTimerT5_Type(Integer32):
    """Custom type sonusSs7NodeTimerT5 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7NodeTimerT5_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT5_Object = MibTableColumn
sonusSs7NodeTimerT5 = _SonusSs7NodeTimerT5_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 25),
    _SonusSs7NodeTimerT5_Type()
)
sonusSs7NodeTimerT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT5.setStatus("current")


class _SonusSs7NodeTimerT6_Type(Integer32):
    """Custom type sonusSs7NodeTimerT6 based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SonusSs7NodeTimerT6_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT6_Object = MibTableColumn
sonusSs7NodeTimerT6 = _SonusSs7NodeTimerT6_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 26),
    _SonusSs7NodeTimerT6_Type()
)
sonusSs7NodeTimerT6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT6.setStatus("current")


class _SonusSs7NodeTimerT7_Type(Integer32):
    """Custom type sonusSs7NodeTimerT7 based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 30),
    )


_SonusSs7NodeTimerT7_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT7_Object = MibTableColumn
sonusSs7NodeTimerT7 = _SonusSs7NodeTimerT7_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 27),
    _SonusSs7NodeTimerT7_Type()
)
sonusSs7NodeTimerT7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT7.setStatus("current")


class _SonusSs7NodeTimerT8_Type(Integer32):
    """Custom type sonusSs7NodeTimerT8 based on Integer32"""
    defaultValue = 13

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15),
    )


_SonusSs7NodeTimerT8_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT8_Object = MibTableColumn
sonusSs7NodeTimerT8 = _SonusSs7NodeTimerT8_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 28),
    _SonusSs7NodeTimerT8_Type()
)
sonusSs7NodeTimerT8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT8.setStatus("current")


class _SonusSs7NodeTimerT9_Type(Integer32):
    """Custom type sonusSs7NodeTimerT9 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 240),
    )


_SonusSs7NodeTimerT9_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT9_Object = MibTableColumn
sonusSs7NodeTimerT9 = _SonusSs7NodeTimerT9_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 29),
    _SonusSs7NodeTimerT9_Type()
)
sonusSs7NodeTimerT9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT9.setStatus("current")


class _SonusSs7NodeTimerT10_Type(Integer32):
    """Custom type sonusSs7NodeTimerT10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 6),
    )


_SonusSs7NodeTimerT10_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT10_Object = MibTableColumn
sonusSs7NodeTimerT10 = _SonusSs7NodeTimerT10_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 30),
    _SonusSs7NodeTimerT10_Type()
)
sonusSs7NodeTimerT10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT10.setStatus("current")


class _SonusSs7NodeTimerT11_Type(Integer32):
    """Custom type sonusSs7NodeTimerT11 based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 20),
    )


_SonusSs7NodeTimerT11_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT11_Object = MibTableColumn
sonusSs7NodeTimerT11 = _SonusSs7NodeTimerT11_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 31),
    _SonusSs7NodeTimerT11_Type()
)
sonusSs7NodeTimerT11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT11.setStatus("current")


class _SonusSs7NodeTimerT12_Type(Integer32):
    """Custom type sonusSs7NodeTimerT12 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7NodeTimerT12_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT12_Object = MibTableColumn
sonusSs7NodeTimerT12 = _SonusSs7NodeTimerT12_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 32),
    _SonusSs7NodeTimerT12_Type()
)
sonusSs7NodeTimerT12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT12.setStatus("current")


class _SonusSs7NodeTimerT13_Type(Integer32):
    """Custom type sonusSs7NodeTimerT13 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7NodeTimerT13_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT13_Object = MibTableColumn
sonusSs7NodeTimerT13 = _SonusSs7NodeTimerT13_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 33),
    _SonusSs7NodeTimerT13_Type()
)
sonusSs7NodeTimerT13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT13.setStatus("current")


class _SonusSs7NodeTimerT14_Type(Integer32):
    """Custom type sonusSs7NodeTimerT14 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7NodeTimerT14_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT14_Object = MibTableColumn
sonusSs7NodeTimerT14 = _SonusSs7NodeTimerT14_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 34),
    _SonusSs7NodeTimerT14_Type()
)
sonusSs7NodeTimerT14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT14.setStatus("current")


class _SonusSs7NodeTimerT15_Type(Integer32):
    """Custom type sonusSs7NodeTimerT15 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7NodeTimerT15_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT15_Object = MibTableColumn
sonusSs7NodeTimerT15 = _SonusSs7NodeTimerT15_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 35),
    _SonusSs7NodeTimerT15_Type()
)
sonusSs7NodeTimerT15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT15.setStatus("current")


class _SonusSs7NodeTimerT16_Type(Integer32):
    """Custom type sonusSs7NodeTimerT16 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7NodeTimerT16_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT16_Object = MibTableColumn
sonusSs7NodeTimerT16 = _SonusSs7NodeTimerT16_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 36),
    _SonusSs7NodeTimerT16_Type()
)
sonusSs7NodeTimerT16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT16.setStatus("current")


class _SonusSs7NodeTimerT17_Type(Integer32):
    """Custom type sonusSs7NodeTimerT17 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7NodeTimerT17_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT17_Object = MibTableColumn
sonusSs7NodeTimerT17 = _SonusSs7NodeTimerT17_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 37),
    _SonusSs7NodeTimerT17_Type()
)
sonusSs7NodeTimerT17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT17.setStatus("current")


class _SonusSs7NodeTimerT18_Type(Integer32):
    """Custom type sonusSs7NodeTimerT18 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7NodeTimerT18_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT18_Object = MibTableColumn
sonusSs7NodeTimerT18 = _SonusSs7NodeTimerT18_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 38),
    _SonusSs7NodeTimerT18_Type()
)
sonusSs7NodeTimerT18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT18.setStatus("current")


class _SonusSs7NodeTimerT19_Type(Integer32):
    """Custom type sonusSs7NodeTimerT19 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7NodeTimerT19_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT19_Object = MibTableColumn
sonusSs7NodeTimerT19 = _SonusSs7NodeTimerT19_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 39),
    _SonusSs7NodeTimerT19_Type()
)
sonusSs7NodeTimerT19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT19.setStatus("current")


class _SonusSs7NodeTimerT20_Type(Integer32):
    """Custom type sonusSs7NodeTimerT20 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7NodeTimerT20_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT20_Object = MibTableColumn
sonusSs7NodeTimerT20 = _SonusSs7NodeTimerT20_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 40),
    _SonusSs7NodeTimerT20_Type()
)
sonusSs7NodeTimerT20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT20.setStatus("current")


class _SonusSs7NodeTimerT21_Type(Integer32):
    """Custom type sonusSs7NodeTimerT21 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7NodeTimerT21_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT21_Object = MibTableColumn
sonusSs7NodeTimerT21 = _SonusSs7NodeTimerT21_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 41),
    _SonusSs7NodeTimerT21_Type()
)
sonusSs7NodeTimerT21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT21.setStatus("current")


class _SonusSs7NodeTimerT22_Type(Integer32):
    """Custom type sonusSs7NodeTimerT22 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7NodeTimerT22_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT22_Object = MibTableColumn
sonusSs7NodeTimerT22 = _SonusSs7NodeTimerT22_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 42),
    _SonusSs7NodeTimerT22_Type()
)
sonusSs7NodeTimerT22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT22.setStatus("current")


class _SonusSs7NodeTimerT23_Type(Integer32):
    """Custom type sonusSs7NodeTimerT23 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7NodeTimerT23_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT23_Object = MibTableColumn
sonusSs7NodeTimerT23 = _SonusSs7NodeTimerT23_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 43),
    _SonusSs7NodeTimerT23_Type()
)
sonusSs7NodeTimerT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT23.setStatus("current")


class _SonusSs7NodeTimerT24_Type(Integer32):
    """Custom type sonusSs7NodeTimerT24 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonusSs7NodeTimerT24_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT24_Object = MibTableColumn
sonusSs7NodeTimerT24 = _SonusSs7NodeTimerT24_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 44),
    _SonusSs7NodeTimerT24_Type()
)
sonusSs7NodeTimerT24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT24.setStatus("current")


class _SonusSs7NodeTimerT25_Type(Integer32):
    """Custom type sonusSs7NodeTimerT25 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SonusSs7NodeTimerT25_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT25_Object = MibTableColumn
sonusSs7NodeTimerT25 = _SonusSs7NodeTimerT25_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 45),
    _SonusSs7NodeTimerT25_Type()
)
sonusSs7NodeTimerT25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT25.setStatus("current")


class _SonusSs7NodeTimerT26_Type(Integer32):
    """Custom type sonusSs7NodeTimerT26 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 180),
    )


_SonusSs7NodeTimerT26_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT26_Object = MibTableColumn
sonusSs7NodeTimerT26 = _SonusSs7NodeTimerT26_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 46),
    _SonusSs7NodeTimerT26_Type()
)
sonusSs7NodeTimerT26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT26.setStatus("current")


class _SonusSs7NodeTimerT27_Type(Integer32):
    """Custom type sonusSs7NodeTimerT27 based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 36000),
    )


_SonusSs7NodeTimerT27_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT27_Object = MibTableColumn
sonusSs7NodeTimerT27 = _SonusSs7NodeTimerT27_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 47),
    _SonusSs7NodeTimerT27_Type()
)
sonusSs7NodeTimerT27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT27.setStatus("current")


class _SonusSs7NodeTimerT28_Type(Integer32):
    """Custom type sonusSs7NodeTimerT28 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_SonusSs7NodeTimerT28_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT28_Object = MibTableColumn
sonusSs7NodeTimerT28 = _SonusSs7NodeTimerT28_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 48),
    _SonusSs7NodeTimerT28_Type()
)
sonusSs7NodeTimerT28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT28.setStatus("current")


class _SonusSs7NodeTimerT29_Type(Integer32):
    """Custom type sonusSs7NodeTimerT29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 600),
    )


_SonusSs7NodeTimerT29_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT29_Object = MibTableColumn
sonusSs7NodeTimerT29 = _SonusSs7NodeTimerT29_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 49),
    _SonusSs7NodeTimerT29_Type()
)
sonusSs7NodeTimerT29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT29.setStatus("current")


class _SonusSs7NodeTimerT30_Type(Integer32):
    """Custom type sonusSs7NodeTimerT30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_SonusSs7NodeTimerT30_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT30_Object = MibTableColumn
sonusSs7NodeTimerT30 = _SonusSs7NodeTimerT30_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 50),
    _SonusSs7NodeTimerT30_Type()
)
sonusSs7NodeTimerT30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT30.setStatus("current")


class _SonusSs7NodeTimerT31_Type(Integer32):
    """Custom type sonusSs7NodeTimerT31 based on Integer32"""
    defaultValue = 420

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(360, 65520),
    )


_SonusSs7NodeTimerT31_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT31_Object = MibTableColumn
sonusSs7NodeTimerT31 = _SonusSs7NodeTimerT31_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 51),
    _SonusSs7NodeTimerT31_Type()
)
sonusSs7NodeTimerT31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT31.setStatus("current")


class _SonusSs7NodeTimerT32_Type(Integer32):
    """Custom type sonusSs7NodeTimerT32 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_SonusSs7NodeTimerT32_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT32_Object = MibTableColumn
sonusSs7NodeTimerT32 = _SonusSs7NodeTimerT32_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 52),
    _SonusSs7NodeTimerT32_Type()
)
sonusSs7NodeTimerT32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT32.setStatus("current")


class _SonusSs7NodeTimerT33_Type(Integer32):
    """Custom type sonusSs7NodeTimerT33 based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 15),
    )


_SonusSs7NodeTimerT33_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT33_Object = MibTableColumn
sonusSs7NodeTimerT33 = _SonusSs7NodeTimerT33_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 53),
    _SonusSs7NodeTimerT33_Type()
)
sonusSs7NodeTimerT33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT33.setStatus("current")


class _SonusSs7NodeTimerT34_Type(Integer32):
    """Custom type sonusSs7NodeTimerT34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_SonusSs7NodeTimerT34_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT34_Object = MibTableColumn
sonusSs7NodeTimerT34 = _SonusSs7NodeTimerT34_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 54),
    _SonusSs7NodeTimerT34_Type()
)
sonusSs7NodeTimerT34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT34.setStatus("current")


class _SonusSs7NodeTimerT35_Type(Integer32):
    """Custom type sonusSs7NodeTimerT35 based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 20),
    )


_SonusSs7NodeTimerT35_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT35_Object = MibTableColumn
sonusSs7NodeTimerT35 = _SonusSs7NodeTimerT35_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 55),
    _SonusSs7NodeTimerT35_Type()
)
sonusSs7NodeTimerT35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT35.setStatus("current")


class _SonusSs7NodeTimerT36_Type(Integer32):
    """Custom type sonusSs7NodeTimerT36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_SonusSs7NodeTimerT36_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT36_Object = MibTableColumn
sonusSs7NodeTimerT36 = _SonusSs7NodeTimerT36_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 56),
    _SonusSs7NodeTimerT36_Type()
)
sonusSs7NodeTimerT36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT36.setStatus("current")


class _SonusSs7NodeTimerT37_Type(Integer32):
    """Custom type sonusSs7NodeTimerT37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_SonusSs7NodeTimerT37_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT37_Object = MibTableColumn
sonusSs7NodeTimerT37 = _SonusSs7NodeTimerT37_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 57),
    _SonusSs7NodeTimerT37_Type()
)
sonusSs7NodeTimerT37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT37.setStatus("current")


class _SonusSs7NodeTimerT38_Type(Integer32):
    """Custom type sonusSs7NodeTimerT38 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_SonusSs7NodeTimerT38_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT38_Object = MibTableColumn
sonusSs7NodeTimerT38 = _SonusSs7NodeTimerT38_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 58),
    _SonusSs7NodeTimerT38_Type()
)
sonusSs7NodeTimerT38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT38.setStatus("current")


class _SonusSs7NodeTimerT39_Type(Integer32):
    """Custom type sonusSs7NodeTimerT39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSs7NodeTimerT39_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT39_Object = MibTableColumn
sonusSs7NodeTimerT39 = _SonusSs7NodeTimerT39_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 59),
    _SonusSs7NodeTimerT39_Type()
)
sonusSs7NodeTimerT39.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT39.setStatus("current")


class _SonusSs7NodeTimerT40_Type(Integer32):
    """Custom type sonusSs7NodeTimerT40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSs7NodeTimerT40_Type.__name__ = "Integer32"
_SonusSs7NodeTimerT40_Object = MibTableColumn
sonusSs7NodeTimerT40 = _SonusSs7NodeTimerT40_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 60),
    _SonusSs7NodeTimerT40_Type()
)
sonusSs7NodeTimerT40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerT40.setStatus("current")


class _SonusSs7NodeTimerTAcc_Type(Integer32):
    """Custom type sonusSs7NodeTimerTAcc based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_SonusSs7NodeTimerTAcc_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTAcc_Object = MibTableColumn
sonusSs7NodeTimerTAcc = _SonusSs7NodeTimerTAcc_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 61),
    _SonusSs7NodeTimerTAcc_Type()
)
sonusSs7NodeTimerTAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTAcc.setStatus("current")


class _SonusSs7NodeTimerTCcr_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCcr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSs7NodeTimerTCcr_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCcr_Object = MibTableColumn
sonusSs7NodeTimerTCcr = _SonusSs7NodeTimerTCcr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 62),
    _SonusSs7NodeTimerTCcr_Type()
)
sonusSs7NodeTimerTCcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCcr.setStatus("current")


class _SonusSs7NodeTimerTCcrr_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCcrr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 31),
    )


_SonusSs7NodeTimerTCcrr_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCcrr_Object = MibTableColumn
sonusSs7NodeTimerTCcrr = _SonusSs7NodeTimerTCcrr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 63),
    _SonusSs7NodeTimerTCcrr_Type()
)
sonusSs7NodeTimerTCcrr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCcrr.setStatus("current")


class _SonusSs7NodeTimerTCgb_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCgb based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_SonusSs7NodeTimerTCgb_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCgb_Object = MibTableColumn
sonusSs7NodeTimerTCgb = _SonusSs7NodeTimerTCgb_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 64),
    _SonusSs7NodeTimerTCgb_Type()
)
sonusSs7NodeTimerTCgb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCgb.setStatus("current")


class _SonusSs7NodeTimerTCra_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCra based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 31),
    )


_SonusSs7NodeTimerTCra_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCra_Object = MibTableColumn
sonusSs7NodeTimerTCra = _SonusSs7NodeTimerTCra_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 65),
    _SonusSs7NodeTimerTCra_Type()
)
sonusSs7NodeTimerTCra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCra.setStatus("current")


class _SonusSs7NodeTimerTCrm_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCrm based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4),
    )


_SonusSs7NodeTimerTCrm_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCrm_Object = MibTableColumn
sonusSs7NodeTimerTCrm = _SonusSs7NodeTimerTCrm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 66),
    _SonusSs7NodeTimerTCrm_Type()
)
sonusSs7NodeTimerTCrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCrm.setStatus("current")


class _SonusSs7NodeTimerTCvt_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCvt based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_SonusSs7NodeTimerTCvt_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCvt_Object = MibTableColumn
sonusSs7NodeTimerTCvt = _SonusSs7NodeTimerTCvt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 67),
    _SonusSs7NodeTimerTCvt_Type()
)
sonusSs7NodeTimerTCvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCvt.setStatus("current")


class _SonusSs7NodeTimerTExm_Type(Integer32):
    """Custom type sonusSs7NodeTimerTExm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSs7NodeTimerTExm_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTExm_Object = MibTableColumn
sonusSs7NodeTimerTExm = _SonusSs7NodeTimerTExm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 68),
    _SonusSs7NodeTimerTExm_Type()
)
sonusSs7NodeTimerTExm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTExm.setStatus("current")


class _SonusSs7NodeTimerTGrs_Type(Integer32):
    """Custom type sonusSs7NodeTimerTGrs based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_SonusSs7NodeTimerTGrs_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTGrs_Object = MibTableColumn
sonusSs7NodeTimerTGrs = _SonusSs7NodeTimerTGrs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 69),
    _SonusSs7NodeTimerTGrs_Type()
)
sonusSs7NodeTimerTGrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTGrs.setStatus("current")


class _SonusSs7NodeTimerTHga_Type(Integer32):
    """Custom type sonusSs7NodeTimerTHga based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SonusSs7NodeTimerTHga_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTHga_Object = MibTableColumn
sonusSs7NodeTimerTHga = _SonusSs7NodeTimerTHga_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 70),
    _SonusSs7NodeTimerTHga_Type()
)
sonusSs7NodeTimerTHga.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTHga.setStatus("current")


class _SonusSs7NodeTimerTScga_Type(Integer32):
    """Custom type sonusSs7NodeTimerTScga based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SonusSs7NodeTimerTScga_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTScga_Object = MibTableColumn
sonusSs7NodeTimerTScga = _SonusSs7NodeTimerTScga_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 71),
    _SonusSs7NodeTimerTScga_Type()
)
sonusSs7NodeTimerTScga.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTScga.setStatus("current")


class _SonusSs7NodeTimerTScgad_Type(Integer32):
    """Custom type sonusSs7NodeTimerTScgad based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_SonusSs7NodeTimerTScgad_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTScgad_Object = MibTableColumn
sonusSs7NodeTimerTScgad = _SonusSs7NodeTimerTScgad_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 72),
    _SonusSs7NodeTimerTScgad_Type()
)
sonusSs7NodeTimerTScgad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTScgad.setStatus("current")


class _SonusSs7NodeApplProfileName_Type(DisplayString):
    """Custom type sonusSs7NodeApplProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusSs7NodeApplProfileName_Type.__name__ = "DisplayString"
_SonusSs7NodeApplProfileName_Object = MibTableColumn
sonusSs7NodeApplProfileName = _SonusSs7NodeApplProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 73),
    _SonusSs7NodeApplProfileName_Type()
)
sonusSs7NodeApplProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeApplProfileName.setStatus("current")


class _SonusSs7NodeNetworkInd_Type(Integer32):
    """Custom type sonusSs7NodeNetworkInd based on Integer32"""
    defaultValue = 3

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
        *(("intl0", 1),
          ("intl1", 2),
          ("natl0", 3),
          ("natl1", 4))
    )


_SonusSs7NodeNetworkInd_Type.__name__ = "Integer32"
_SonusSs7NodeNetworkInd_Object = MibTableColumn
sonusSs7NodeNetworkInd = _SonusSs7NodeNetworkInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 74),
    _SonusSs7NodeNetworkInd_Type()
)
sonusSs7NodeNetworkInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeNetworkInd.setStatus("current")


class _SonusSs7NodeSlsBits_Type(Integer32):
    """Custom type sonusSs7NodeSlsBits based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_SonusSs7NodeSlsBits_Type.__name__ = "Integer32"
_SonusSs7NodeSlsBits_Object = MibTableColumn
sonusSs7NodeSlsBits = _SonusSs7NodeSlsBits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 75),
    _SonusSs7NodeSlsBits_Type()
)
sonusSs7NodeSlsBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeSlsBits.setStatus("current")


class _SonusSs7NodeTimerTA_Type(Integer32):
    """Custom type sonusSs7NodeTimerTA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SonusSs7NodeTimerTA_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTA_Object = MibTableColumn
sonusSs7NodeTimerTA = _SonusSs7NodeTimerTA_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 76),
    _SonusSs7NodeTimerTA_Type()
)
sonusSs7NodeTimerTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTA.setStatus("current")


class _SonusSs7NodeTimerTBlom_Type(Integer32):
    """Custom type sonusSs7NodeTimerTBlom based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(240, 360),
    )


_SonusSs7NodeTimerTBlom_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTBlom_Object = MibTableColumn
sonusSs7NodeTimerTBlom = _SonusSs7NodeTimerTBlom_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 77),
    _SonusSs7NodeTimerTBlom_Type()
)
sonusSs7NodeTimerTBlom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTBlom.setStatus("current")


class _SonusSs7NodeTimerTCotd_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCotd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SonusSs7NodeTimerTCotd_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCotd_Object = MibTableColumn
sonusSs7NodeTimerTCotd = _SonusSs7NodeTimerTCotd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 78),
    _SonusSs7NodeTimerTCotd_Type()
)
sonusSs7NodeTimerTCotd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCotd.setStatus("current")


class _SonusSs7NodeTimerTCotl_Type(Integer32):
    """Custom type sonusSs7NodeTimerTCotl based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(240, 300),
    )


_SonusSs7NodeTimerTCotl_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTCotl_Object = MibTableColumn
sonusSs7NodeTimerTCotl = _SonusSs7NodeTimerTCotl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 79),
    _SonusSs7NodeTimerTCotl_Type()
)
sonusSs7NodeTimerTCotl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTCotl.setStatus("current")


class _SonusSs7NodeTimerTSus_Type(Integer32):
    """Custom type sonusSs7NodeTimerTSus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 16),
    )


_SonusSs7NodeTimerTSus_Type.__name__ = "Integer32"
_SonusSs7NodeTimerTSus_Object = MibTableColumn
sonusSs7NodeTimerTSus = _SonusSs7NodeTimerTSus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 2, 2, 1, 80),
    _SonusSs7NodeTimerTSus_Type()
)
sonusSs7NodeTimerTSus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeTimerTSus.setStatus("current")
_SonusSs7NodeProfile_ObjectIdentity = ObjectIdentity
sonusSs7NodeProfile = _SonusSs7NodeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3)
)
_SonusSs7NodeProfileNextIndex_Type = Integer32
_SonusSs7NodeProfileNextIndex_Object = MibScalar
sonusSs7NodeProfileNextIndex = _SonusSs7NodeProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 1),
    _SonusSs7NodeProfileNextIndex_Type()
)
sonusSs7NodeProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeProfileNextIndex.setStatus("current")
_SonusSs7NodeProfileTable_Object = MibTable
sonusSs7NodeProfileTable = _SonusSs7NodeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonusSs7NodeProfileTable.setStatus("current")
_SonusSs7NodeProfileEntry_Object = MibTableRow
sonusSs7NodeProfileEntry = _SonusSs7NodeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1)
)
sonusSs7NodeProfileEntry.setIndexNames(
    (0, "SONUS-SS7-SERVICES-MIB", "sonusSs7NodeProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusSs7NodeProfileEntry.setStatus("current")
_SonusSs7NodeProfileIndex_Type = Integer32
_SonusSs7NodeProfileIndex_Object = MibTableColumn
sonusSs7NodeProfileIndex = _SonusSs7NodeProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 1),
    _SonusSs7NodeProfileIndex_Type()
)
sonusSs7NodeProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeProfileIndex.setStatus("current")
_SonusSs7NodeProfileName_Type = SonusName
_SonusSs7NodeProfileName_Object = MibTableColumn
sonusSs7NodeProfileName = _SonusSs7NodeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 2),
    _SonusSs7NodeProfileName_Type()
)
sonusSs7NodeProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeProfileName.setStatus("current")


class _SonusSs7PointCodeSize_Type(Integer32):
    """Custom type sonusSs7PointCodeSize based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusSs7PointCodeSize_Type.__name__ = "Integer32"
_SonusSs7PointCodeSize_Object = MibTableColumn
sonusSs7PointCodeSize = _SonusSs7PointCodeSize_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 3),
    _SonusSs7PointCodeSize_Type()
)
sonusSs7PointCodeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7PointCodeSize.setStatus("current")
_SonusSs7PointCodeFormatType_Type = SonusPointCodeFormat
_SonusSs7PointCodeFormatType_Object = MibTableColumn
sonusSs7PointCodeFormatType = _SonusSs7PointCodeFormatType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 4),
    _SonusSs7PointCodeFormatType_Type()
)
sonusSs7PointCodeFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7PointCodeFormatType.setStatus("current")


class _SonusSs7ServerProtocol_Type(Integer32):
    """Custom type sonusSs7ServerProtocol based on Integer32"""
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
        *(("dgmsProp", 1),
          ("dgmsRaw", 2),
          ("tekTali", 3))
    )


_SonusSs7ServerProtocol_Type.__name__ = "Integer32"
_SonusSs7ServerProtocol_Object = MibTableColumn
sonusSs7ServerProtocol = _SonusSs7ServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 5),
    _SonusSs7ServerProtocol_Type()
)
sonusSs7ServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7ServerProtocol.setStatus("current")


class _SonusSs7HandShakeInterval_Type(Integer32):
    """Custom type sonusSs7HandShakeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusSs7HandShakeInterval_Type.__name__ = "Integer32"
_SonusSs7HandShakeInterval_Object = MibTableColumn
sonusSs7HandShakeInterval = _SonusSs7HandShakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 6),
    _SonusSs7HandShakeInterval_Type()
)
sonusSs7HandShakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7HandShakeInterval.setStatus("current")


class _SonusSs7TimerT1_Type(Integer32):
    """Custom type sonusSs7TimerT1 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7TimerT1_Type.__name__ = "Integer32"
_SonusSs7TimerT1_Object = MibTableColumn
sonusSs7TimerT1 = _SonusSs7TimerT1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 7),
    _SonusSs7TimerT1_Type()
)
sonusSs7TimerT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT1.setStatus("current")


class _SonusSs7TimerT2_Type(Integer32):
    """Custom type sonusSs7TimerT2 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusSs7TimerT2_Type.__name__ = "Integer32"
_SonusSs7TimerT2_Object = MibTableColumn
sonusSs7TimerT2 = _SonusSs7TimerT2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 8),
    _SonusSs7TimerT2_Type()
)
sonusSs7TimerT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT2.setStatus("current")


class _SonusSs7TimerT3_Type(Integer32):
    """Custom type sonusSs7TimerT3 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusSs7TimerT3_Type.__name__ = "Integer32"
_SonusSs7TimerT3_Object = MibTableColumn
sonusSs7TimerT3 = _SonusSs7TimerT3_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 9),
    _SonusSs7TimerT3_Type()
)
sonusSs7TimerT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT3.setStatus("current")


class _SonusSs7TimerT4_Type(Integer32):
    """Custom type sonusSs7TimerT4 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 900),
    )


_SonusSs7TimerT4_Type.__name__ = "Integer32"
_SonusSs7TimerT4_Object = MibTableColumn
sonusSs7TimerT4 = _SonusSs7TimerT4_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 10),
    _SonusSs7TimerT4_Type()
)
sonusSs7TimerT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT4.setStatus("current")


class _SonusSs7TimerT5_Type(Integer32):
    """Custom type sonusSs7TimerT5 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7TimerT5_Type.__name__ = "Integer32"
_SonusSs7TimerT5_Object = MibTableColumn
sonusSs7TimerT5 = _SonusSs7TimerT5_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 11),
    _SonusSs7TimerT5_Type()
)
sonusSs7TimerT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT5.setStatus("current")


class _SonusSs7TimerT6_Type(Integer32):
    """Custom type sonusSs7TimerT6 based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32),
    )


_SonusSs7TimerT6_Type.__name__ = "Integer32"
_SonusSs7TimerT6_Object = MibTableColumn
sonusSs7TimerT6 = _SonusSs7TimerT6_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 12),
    _SonusSs7TimerT6_Type()
)
sonusSs7TimerT6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT6.setStatus("current")


class _SonusSs7TimerT7_Type(Integer32):
    """Custom type sonusSs7TimerT7 based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 30),
    )


_SonusSs7TimerT7_Type.__name__ = "Integer32"
_SonusSs7TimerT7_Object = MibTableColumn
sonusSs7TimerT7 = _SonusSs7TimerT7_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 13),
    _SonusSs7TimerT7_Type()
)
sonusSs7TimerT7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT7.setStatus("current")


class _SonusSs7TimerT8_Type(Integer32):
    """Custom type sonusSs7TimerT8 based on Integer32"""
    defaultValue = 13

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15),
    )


_SonusSs7TimerT8_Type.__name__ = "Integer32"
_SonusSs7TimerT8_Object = MibTableColumn
sonusSs7TimerT8 = _SonusSs7TimerT8_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 14),
    _SonusSs7TimerT8_Type()
)
sonusSs7TimerT8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT8.setStatus("current")


class _SonusSs7TimerT9_Type(Integer32):
    """Custom type sonusSs7TimerT9 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 240),
    )


_SonusSs7TimerT9_Type.__name__ = "Integer32"
_SonusSs7TimerT9_Object = MibTableColumn
sonusSs7TimerT9 = _SonusSs7TimerT9_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 15),
    _SonusSs7TimerT9_Type()
)
sonusSs7TimerT9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT9.setStatus("current")


class _SonusSs7TimerT10_Type(Integer32):
    """Custom type sonusSs7TimerT10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(240, 360),
    )


_SonusSs7TimerT10_Type.__name__ = "Integer32"
_SonusSs7TimerT10_Object = MibTableColumn
sonusSs7TimerT10 = _SonusSs7TimerT10_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 16),
    _SonusSs7TimerT10_Type()
)
sonusSs7TimerT10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT10.setStatus("current")


class _SonusSs7TimerT11_Type(Integer32):
    """Custom type sonusSs7TimerT11 based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 20),
    )


_SonusSs7TimerT11_Type.__name__ = "Integer32"
_SonusSs7TimerT11_Object = MibTableColumn
sonusSs7TimerT11 = _SonusSs7TimerT11_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 17),
    _SonusSs7TimerT11_Type()
)
sonusSs7TimerT11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT11.setStatus("current")


class _SonusSs7TimerT12_Type(Integer32):
    """Custom type sonusSs7TimerT12 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7TimerT12_Type.__name__ = "Integer32"
_SonusSs7TimerT12_Object = MibTableColumn
sonusSs7TimerT12 = _SonusSs7TimerT12_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 18),
    _SonusSs7TimerT12_Type()
)
sonusSs7TimerT12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT12.setStatus("current")


class _SonusSs7TimerT13_Type(Integer32):
    """Custom type sonusSs7TimerT13 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7TimerT13_Type.__name__ = "Integer32"
_SonusSs7TimerT13_Object = MibTableColumn
sonusSs7TimerT13 = _SonusSs7TimerT13_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 19),
    _SonusSs7TimerT13_Type()
)
sonusSs7TimerT13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT13.setStatus("current")


class _SonusSs7TimerT14_Type(Integer32):
    """Custom type sonusSs7TimerT14 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7TimerT14_Type.__name__ = "Integer32"
_SonusSs7TimerT14_Object = MibTableColumn
sonusSs7TimerT14 = _SonusSs7TimerT14_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 20),
    _SonusSs7TimerT14_Type()
)
sonusSs7TimerT14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT14.setStatus("current")


class _SonusSs7TimerT15_Type(Integer32):
    """Custom type sonusSs7TimerT15 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7TimerT15_Type.__name__ = "Integer32"
_SonusSs7TimerT15_Object = MibTableColumn
sonusSs7TimerT15 = _SonusSs7TimerT15_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 21),
    _SonusSs7TimerT15_Type()
)
sonusSs7TimerT15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT15.setStatus("current")


class _SonusSs7TimerT16_Type(Integer32):
    """Custom type sonusSs7TimerT16 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7TimerT16_Type.__name__ = "Integer32"
_SonusSs7TimerT16_Object = MibTableColumn
sonusSs7TimerT16 = _SonusSs7TimerT16_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 22),
    _SonusSs7TimerT16_Type()
)
sonusSs7TimerT16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT16.setStatus("current")


class _SonusSs7TimerT17_Type(Integer32):
    """Custom type sonusSs7TimerT17 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7TimerT17_Type.__name__ = "Integer32"
_SonusSs7TimerT17_Object = MibTableColumn
sonusSs7TimerT17 = _SonusSs7TimerT17_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 23),
    _SonusSs7TimerT17_Type()
)
sonusSs7TimerT17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT17.setStatus("current")


class _SonusSs7TimerT18_Type(Integer32):
    """Custom type sonusSs7TimerT18 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7TimerT18_Type.__name__ = "Integer32"
_SonusSs7TimerT18_Object = MibTableColumn
sonusSs7TimerT18 = _SonusSs7TimerT18_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 24),
    _SonusSs7TimerT18_Type()
)
sonusSs7TimerT18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT18.setStatus("current")


class _SonusSs7TimerT19_Type(Integer32):
    """Custom type sonusSs7TimerT19 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7TimerT19_Type.__name__ = "Integer32"
_SonusSs7TimerT19_Object = MibTableColumn
sonusSs7TimerT19 = _SonusSs7TimerT19_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 25),
    _SonusSs7TimerT19_Type()
)
sonusSs7TimerT19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT19.setStatus("current")


class _SonusSs7TimerT20_Type(Integer32):
    """Custom type sonusSs7TimerT20 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7TimerT20_Type.__name__ = "Integer32"
_SonusSs7TimerT20_Object = MibTableColumn
sonusSs7TimerT20 = _SonusSs7TimerT20_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 26),
    _SonusSs7TimerT20_Type()
)
sonusSs7TimerT20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT20.setStatus("current")


class _SonusSs7TimerT21_Type(Integer32):
    """Custom type sonusSs7TimerT21 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7TimerT21_Type.__name__ = "Integer32"
_SonusSs7TimerT21_Object = MibTableColumn
sonusSs7TimerT21 = _SonusSs7TimerT21_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 27),
    _SonusSs7TimerT21_Type()
)
sonusSs7TimerT21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT21.setStatus("current")


class _SonusSs7TimerT22_Type(Integer32):
    """Custom type sonusSs7TimerT22 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_SonusSs7TimerT22_Type.__name__ = "Integer32"
_SonusSs7TimerT22_Object = MibTableColumn
sonusSs7TimerT22 = _SonusSs7TimerT22_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 28),
    _SonusSs7TimerT22_Type()
)
sonusSs7TimerT22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT22.setStatus("current")


class _SonusSs7TimerT23_Type(Integer32):
    """Custom type sonusSs7TimerT23 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_SonusSs7TimerT23_Type.__name__ = "Integer32"
_SonusSs7TimerT23_Object = MibTableColumn
sonusSs7TimerT23 = _SonusSs7TimerT23_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 29),
    _SonusSs7TimerT23_Type()
)
sonusSs7TimerT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT23.setStatus("current")


class _SonusSs7TimerT24_Type(Integer32):
    """Custom type sonusSs7TimerT24 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonusSs7TimerT24_Type.__name__ = "Integer32"
_SonusSs7TimerT24_Object = MibTableColumn
sonusSs7TimerT24 = _SonusSs7TimerT24_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 30),
    _SonusSs7TimerT24_Type()
)
sonusSs7TimerT24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT24.setStatus("current")


class _SonusSs7TimerT25_Type(Integer32):
    """Custom type sonusSs7TimerT25 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SonusSs7TimerT25_Type.__name__ = "Integer32"
_SonusSs7TimerT25_Object = MibTableColumn
sonusSs7TimerT25 = _SonusSs7TimerT25_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 31),
    _SonusSs7TimerT25_Type()
)
sonusSs7TimerT25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT25.setStatus("current")


class _SonusSs7TimerT26_Type(Integer32):
    """Custom type sonusSs7TimerT26 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 180),
    )


_SonusSs7TimerT26_Type.__name__ = "Integer32"
_SonusSs7TimerT26_Object = MibTableColumn
sonusSs7TimerT26 = _SonusSs7TimerT26_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 32),
    _SonusSs7TimerT26_Type()
)
sonusSs7TimerT26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT26.setStatus("current")


class _SonusSs7TimerT27_Type(Integer32):
    """Custom type sonusSs7TimerT27 based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 36000),
    )


_SonusSs7TimerT27_Type.__name__ = "Integer32"
_SonusSs7TimerT27_Object = MibTableColumn
sonusSs7TimerT27 = _SonusSs7TimerT27_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 33),
    _SonusSs7TimerT27_Type()
)
sonusSs7TimerT27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT27.setStatus("current")


class _SonusSs7TimerT28_Type(Integer32):
    """Custom type sonusSs7TimerT28 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_SonusSs7TimerT28_Type.__name__ = "Integer32"
_SonusSs7TimerT28_Object = MibTableColumn
sonusSs7TimerT28 = _SonusSs7TimerT28_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 34),
    _SonusSs7TimerT28_Type()
)
sonusSs7TimerT28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT28.setStatus("current")


class _SonusSs7TimerT29_Type(Integer32):
    """Custom type sonusSs7TimerT29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 600),
    )


_SonusSs7TimerT29_Type.__name__ = "Integer32"
_SonusSs7TimerT29_Object = MibTableColumn
sonusSs7TimerT29 = _SonusSs7TimerT29_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 35),
    _SonusSs7TimerT29_Type()
)
sonusSs7TimerT29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT29.setStatus("current")


class _SonusSs7TimerT30_Type(Integer32):
    """Custom type sonusSs7TimerT30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_SonusSs7TimerT30_Type.__name__ = "Integer32"
_SonusSs7TimerT30_Object = MibTableColumn
sonusSs7TimerT30 = _SonusSs7TimerT30_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 36),
    _SonusSs7TimerT30_Type()
)
sonusSs7TimerT30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT30.setStatus("current")


class _SonusSs7TimerT31_Type(Integer32):
    """Custom type sonusSs7TimerT31 based on Integer32"""
    defaultValue = 420

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(360, 65520),
    )


_SonusSs7TimerT31_Type.__name__ = "Integer32"
_SonusSs7TimerT31_Object = MibTableColumn
sonusSs7TimerT31 = _SonusSs7TimerT31_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 37),
    _SonusSs7TimerT31_Type()
)
sonusSs7TimerT31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT31.setStatus("current")


class _SonusSs7TimerT32_Type(Integer32):
    """Custom type sonusSs7TimerT32 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_SonusSs7TimerT32_Type.__name__ = "Integer32"
_SonusSs7TimerT32_Object = MibTableColumn
sonusSs7TimerT32 = _SonusSs7TimerT32_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 38),
    _SonusSs7TimerT32_Type()
)
sonusSs7TimerT32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT32.setStatus("current")


class _SonusSs7TimerT33_Type(Integer32):
    """Custom type sonusSs7TimerT33 based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 15),
    )


_SonusSs7TimerT33_Type.__name__ = "Integer32"
_SonusSs7TimerT33_Object = MibTableColumn
sonusSs7TimerT33 = _SonusSs7TimerT33_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 39),
    _SonusSs7TimerT33_Type()
)
sonusSs7TimerT33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT33.setStatus("current")


class _SonusSs7TimerT34_Type(Integer32):
    """Custom type sonusSs7TimerT34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_SonusSs7TimerT34_Type.__name__ = "Integer32"
_SonusSs7TimerT34_Object = MibTableColumn
sonusSs7TimerT34 = _SonusSs7TimerT34_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 40),
    _SonusSs7TimerT34_Type()
)
sonusSs7TimerT34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT34.setStatus("current")


class _SonusSs7TimerT35_Type(Integer32):
    """Custom type sonusSs7TimerT35 based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 20),
    )


_SonusSs7TimerT35_Type.__name__ = "Integer32"
_SonusSs7TimerT35_Object = MibTableColumn
sonusSs7TimerT35 = _SonusSs7TimerT35_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 41),
    _SonusSs7TimerT35_Type()
)
sonusSs7TimerT35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT35.setStatus("current")


class _SonusSs7TimerT36_Type(Integer32):
    """Custom type sonusSs7TimerT36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_SonusSs7TimerT36_Type.__name__ = "Integer32"
_SonusSs7TimerT36_Object = MibTableColumn
sonusSs7TimerT36 = _SonusSs7TimerT36_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 42),
    _SonusSs7TimerT36_Type()
)
sonusSs7TimerT36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT36.setStatus("current")


class _SonusSs7TimerT37_Type(Integer32):
    """Custom type sonusSs7TimerT37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_SonusSs7TimerT37_Type.__name__ = "Integer32"
_SonusSs7TimerT37_Object = MibTableColumn
sonusSs7TimerT37 = _SonusSs7TimerT37_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 43),
    _SonusSs7TimerT37_Type()
)
sonusSs7TimerT37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT37.setStatus("current")


class _SonusSs7TimerT38_Type(Integer32):
    """Custom type sonusSs7TimerT38 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_SonusSs7TimerT38_Type.__name__ = "Integer32"
_SonusSs7TimerT38_Object = MibTableColumn
sonusSs7TimerT38 = _SonusSs7TimerT38_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 44),
    _SonusSs7TimerT38_Type()
)
sonusSs7TimerT38.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT38.setStatus("current")


class _SonusSs7TimerT39_Type(Integer32):
    """Custom type sonusSs7TimerT39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSs7TimerT39_Type.__name__ = "Integer32"
_SonusSs7TimerT39_Object = MibTableColumn
sonusSs7TimerT39 = _SonusSs7TimerT39_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 45),
    _SonusSs7TimerT39_Type()
)
sonusSs7TimerT39.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT39.setStatus("current")


class _SonusSs7TimerT40_Type(Integer32):
    """Custom type sonusSs7TimerT40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSs7TimerT40_Type.__name__ = "Integer32"
_SonusSs7TimerT40_Object = MibTableColumn
sonusSs7TimerT40 = _SonusSs7TimerT40_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 46),
    _SonusSs7TimerT40_Type()
)
sonusSs7TimerT40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerT40.setStatus("current")


class _SonusSs7TimerTAcc_Type(Integer32):
    """Custom type sonusSs7TimerTAcc based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_SonusSs7TimerTAcc_Type.__name__ = "Integer32"
_SonusSs7TimerTAcc_Object = MibTableColumn
sonusSs7TimerTAcc = _SonusSs7TimerTAcc_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 47),
    _SonusSs7TimerTAcc_Type()
)
sonusSs7TimerTAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTAcc.setStatus("current")


class _SonusSs7TimerTCcr_Type(Integer32):
    """Custom type sonusSs7TimerTCcr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusSs7TimerTCcr_Type.__name__ = "Integer32"
_SonusSs7TimerTCcr_Object = MibTableColumn
sonusSs7TimerTCcr = _SonusSs7TimerTCcr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 48),
    _SonusSs7TimerTCcr_Type()
)
sonusSs7TimerTCcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCcr.setStatus("current")


class _SonusSs7TimerTCcrr_Type(Integer32):
    """Custom type sonusSs7TimerTCcrr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 31),
    )


_SonusSs7TimerTCcrr_Type.__name__ = "Integer32"
_SonusSs7TimerTCcrr_Object = MibTableColumn
sonusSs7TimerTCcrr = _SonusSs7TimerTCcrr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 49),
    _SonusSs7TimerTCcrr_Type()
)
sonusSs7TimerTCcrr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCcrr.setStatus("current")


class _SonusSs7TimerTCgb_Type(Integer32):
    """Custom type sonusSs7TimerTCgb based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_SonusSs7TimerTCgb_Type.__name__ = "Integer32"
_SonusSs7TimerTCgb_Object = MibTableColumn
sonusSs7TimerTCgb = _SonusSs7TimerTCgb_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 50),
    _SonusSs7TimerTCgb_Type()
)
sonusSs7TimerTCgb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCgb.setStatus("current")


class _SonusSs7TimerTCra_Type(Integer32):
    """Custom type sonusSs7TimerTCra based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 31),
    )


_SonusSs7TimerTCra_Type.__name__ = "Integer32"
_SonusSs7TimerTCra_Object = MibTableColumn
sonusSs7TimerTCra = _SonusSs7TimerTCra_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 51),
    _SonusSs7TimerTCra_Type()
)
sonusSs7TimerTCra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCra.setStatus("current")


class _SonusSs7TimerTCrm_Type(Integer32):
    """Custom type sonusSs7TimerTCrm based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4),
    )


_SonusSs7TimerTCrm_Type.__name__ = "Integer32"
_SonusSs7TimerTCrm_Object = MibTableColumn
sonusSs7TimerTCrm = _SonusSs7TimerTCrm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 52),
    _SonusSs7TimerTCrm_Type()
)
sonusSs7TimerTCrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCrm.setStatus("current")


class _SonusSs7TimerTCvt_Type(Integer32):
    """Custom type sonusSs7TimerTCvt based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_SonusSs7TimerTCvt_Type.__name__ = "Integer32"
_SonusSs7TimerTCvt_Object = MibTableColumn
sonusSs7TimerTCvt = _SonusSs7TimerTCvt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 53),
    _SonusSs7TimerTCvt_Type()
)
sonusSs7TimerTCvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCvt.setStatus("current")


class _SonusSs7TimerTExm_Type(Integer32):
    """Custom type sonusSs7TimerTExm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSs7TimerTExm_Type.__name__ = "Integer32"
_SonusSs7TimerTExm_Object = MibTableColumn
sonusSs7TimerTExm = _SonusSs7TimerTExm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 54),
    _SonusSs7TimerTExm_Type()
)
sonusSs7TimerTExm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTExm.setStatus("current")


class _SonusSs7TimerTGrs_Type(Integer32):
    """Custom type sonusSs7TimerTGrs based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_SonusSs7TimerTGrs_Type.__name__ = "Integer32"
_SonusSs7TimerTGrs_Object = MibTableColumn
sonusSs7TimerTGrs = _SonusSs7TimerTGrs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 55),
    _SonusSs7TimerTGrs_Type()
)
sonusSs7TimerTGrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTGrs.setStatus("current")


class _SonusSs7TimerTHga_Type(Integer32):
    """Custom type sonusSs7TimerTHga based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SonusSs7TimerTHga_Type.__name__ = "Integer32"
_SonusSs7TimerTHga_Object = MibTableColumn
sonusSs7TimerTHga = _SonusSs7TimerTHga_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 56),
    _SonusSs7TimerTHga_Type()
)
sonusSs7TimerTHga.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTHga.setStatus("current")


class _SonusSs7TimerTScga_Type(Integer32):
    """Custom type sonusSs7TimerTScga based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SonusSs7TimerTScga_Type.__name__ = "Integer32"
_SonusSs7TimerTScga_Object = MibTableColumn
sonusSs7TimerTScga = _SonusSs7TimerTScga_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 57),
    _SonusSs7TimerTScga_Type()
)
sonusSs7TimerTScga.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTScga.setStatus("current")


class _SonusSs7TimerTScgad_Type(Integer32):
    """Custom type sonusSs7TimerTScgad based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_SonusSs7TimerTScgad_Type.__name__ = "Integer32"
_SonusSs7TimerTScgad_Object = MibTableColumn
sonusSs7TimerTScgad = _SonusSs7TimerTScgad_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 58),
    _SonusSs7TimerTScgad_Type()
)
sonusSs7TimerTScgad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTScgad.setStatus("current")


class _SonusSs7NodeProfileState_Type(Integer32):
    """Custom type sonusSs7NodeProfileState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusSs7NodeProfileState_Type.__name__ = "Integer32"
_SonusSs7NodeProfileState_Object = MibTableColumn
sonusSs7NodeProfileState = _SonusSs7NodeProfileState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 59),
    _SonusSs7NodeProfileState_Type()
)
sonusSs7NodeProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeProfileState.setStatus("current")
_SonusSs7NodeProfileRowStatus_Type = RowStatus
_SonusSs7NodeProfileRowStatus_Object = MibTableColumn
sonusSs7NodeProfileRowStatus = _SonusSs7NodeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 60),
    _SonusSs7NodeProfileRowStatus_Type()
)
sonusSs7NodeProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeProfileRowStatus.setStatus("current")


class _SonusSs7NodeProfileNetworkInd_Type(Integer32):
    """Custom type sonusSs7NodeProfileNetworkInd based on Integer32"""
    defaultValue = 3

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
        *(("intl0", 1),
          ("intl1", 2),
          ("natl0", 3),
          ("natl1", 4))
    )


_SonusSs7NodeProfileNetworkInd_Type.__name__ = "Integer32"
_SonusSs7NodeProfileNetworkInd_Object = MibTableColumn
sonusSs7NodeProfileNetworkInd = _SonusSs7NodeProfileNetworkInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 61),
    _SonusSs7NodeProfileNetworkInd_Type()
)
sonusSs7NodeProfileNetworkInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7NodeProfileNetworkInd.setStatus("current")


class _SonusSs7SlsBits_Type(Integer32):
    """Custom type sonusSs7SlsBits based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_SonusSs7SlsBits_Type.__name__ = "Integer32"
_SonusSs7SlsBits_Object = MibTableColumn
sonusSs7SlsBits = _SonusSs7SlsBits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 62),
    _SonusSs7SlsBits_Type()
)
sonusSs7SlsBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7SlsBits.setStatus("current")


class _SonusSs7TimerTA_Type(Integer32):
    """Custom type sonusSs7TimerTA based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SonusSs7TimerTA_Type.__name__ = "Integer32"
_SonusSs7TimerTA_Object = MibTableColumn
sonusSs7TimerTA = _SonusSs7TimerTA_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 63),
    _SonusSs7TimerTA_Type()
)
sonusSs7TimerTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTA.setStatus("current")


class _SonusSs7TimerTBlom_Type(Integer32):
    """Custom type sonusSs7TimerTBlom based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(240, 360),
    )


_SonusSs7TimerTBlom_Type.__name__ = "Integer32"
_SonusSs7TimerTBlom_Object = MibTableColumn
sonusSs7TimerTBlom = _SonusSs7TimerTBlom_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 64),
    _SonusSs7TimerTBlom_Type()
)
sonusSs7TimerTBlom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTBlom.setStatus("current")


class _SonusSs7TimerTCotd_Type(Integer32):
    """Custom type sonusSs7TimerTCotd based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SonusSs7TimerTCotd_Type.__name__ = "Integer32"
_SonusSs7TimerTCotd_Object = MibTableColumn
sonusSs7TimerTCotd = _SonusSs7TimerTCotd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 65),
    _SonusSs7TimerTCotd_Type()
)
sonusSs7TimerTCotd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCotd.setStatus("current")


class _SonusSs7TimerTCotl_Type(Integer32):
    """Custom type sonusSs7TimerTCotl based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(240, 300),
    )


_SonusSs7TimerTCotl_Type.__name__ = "Integer32"
_SonusSs7TimerTCotl_Object = MibTableColumn
sonusSs7TimerTCotl = _SonusSs7TimerTCotl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 66),
    _SonusSs7TimerTCotl_Type()
)
sonusSs7TimerTCotl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTCotl.setStatus("current")


class _SonusSs7TimerTSus_Type(Integer32):
    """Custom type sonusSs7TimerTSus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 16),
    )


_SonusSs7TimerTSus_Type.__name__ = "Integer32"
_SonusSs7TimerTSus_Object = MibTableColumn
sonusSs7TimerTSus = _SonusSs7TimerTSus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 1, 3, 2, 1, 67),
    _SonusSs7TimerTSus_Type()
)
sonusSs7TimerTSus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSs7TimerTSus.setStatus("current")
_SonusSs7ServicesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusSs7ServicesMIBNotifications = _SonusSs7ServicesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2)
)
_SonusSs7ServicesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusSs7ServicesMIBNotificationsPrefix = _SonusSs7ServicesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 0)
)
_SonusSs7ServicesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusSs7ServicesMIBNotificationsObjects = _SonusSs7ServicesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 1)
)


class _SonusSs7NodeServiceType_Type(DisplayString):
    """Custom type sonusSs7NodeServiceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_SonusSs7NodeServiceType_Type.__name__ = "DisplayString"
_SonusSs7NodeServiceType_Object = MibScalar
sonusSs7NodeServiceType = _SonusSs7NodeServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 1, 1),
    _SonusSs7NodeServiceType_Type()
)
sonusSs7NodeServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeServiceType.setStatus("current")


class _SonusSs7NodeStateChangeReason_Type(DisplayString):
    """Custom type sonusSs7NodeStateChangeReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 101),
    )


_SonusSs7NodeStateChangeReason_Type.__name__ = "DisplayString"
_SonusSs7NodeStateChangeReason_Object = MibScalar
sonusSs7NodeStateChangeReason = _SonusSs7NodeStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 1, 2),
    _SonusSs7NodeStateChangeReason_Type()
)
sonusSs7NodeStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeStateChangeReason.setStatus("current")


class _SonusSs7NodeCurrentState_Type(Integer32):
    """Custom type sonusSs7NodeCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("congested", 6),
          ("disabled", 5),
          ("failed", 4),
          ("initializing", 3),
          ("offline", 1))
    )


_SonusSs7NodeCurrentState_Type.__name__ = "Integer32"
_SonusSs7NodeCurrentState_Object = MibScalar
sonusSs7NodeCurrentState = _SonusSs7NodeCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 1, 3),
    _SonusSs7NodeCurrentState_Type()
)
sonusSs7NodeCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeCurrentState.setStatus("current")
_SonusSs7NodeAffectedPointCode_Type = PointCode
_SonusSs7NodeAffectedPointCode_Object = MibScalar
sonusSs7NodeAffectedPointCode = _SonusSs7NodeAffectedPointCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 1, 4),
    _SonusSs7NodeAffectedPointCode_Type()
)
sonusSs7NodeAffectedPointCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSs7NodeAffectedPointCode.setStatus("current")

# Managed Objects groups


# Notification objects

sonusSs7NodeConnectionEstablishedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 0, 1)
)
sonusSs7NodeConnectionEstablishedNotification.setObjects(
      *(("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeName"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeGatewayAssignment"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeServiceType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSs7NodeConnectionEstablishedNotification.setStatus(
        "current"
    )

sonusSs7NodeConnectionFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 0, 2)
)
sonusSs7NodeConnectionFailedNotification.setObjects(
      *(("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeName"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeGatewayAssignment"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeServiceType"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeStateChangeReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSs7NodeConnectionFailedNotification.setStatus(
        "current"
    )

sonusSs7NodeConnectionStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 0, 3)
)
sonusSs7NodeConnectionStateChangeNotification.setObjects(
      *(("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeName"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeGatewayAssignment"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeServiceType"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeCurrentState"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeStateChangeReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSs7NodeConnectionStateChangeNotification.setStatus(
        "current"
    )

sonusSs7NodeMtpStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 3, 2, 0, 4)
)
sonusSs7NodeMtpStateChangeNotification.setObjects(
      *(("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeName"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeGatewayAssignment"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeServiceType"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeMtpStatus"),
        ("SONUS-SS7-SERVICES-MIB", "sonusSs7NodeAffectedPointCode"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSs7NodeMtpStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SS7-SERVICES-MIB",
    **{"SonusSs7GatewayLinkSelection": SonusSs7GatewayLinkSelection,
       "sonusSs7ServicesMIB": sonusSs7ServicesMIB,
       "sonusSs7ServicesMIBObjects": sonusSs7ServicesMIBObjects,
       "sonusSs7Gateway": sonusSs7Gateway,
       "sonusSs7GatewayNextIndex": sonusSs7GatewayNextIndex,
       "sonusSs7GatewayTable": sonusSs7GatewayTable,
       "sonusSs7GatewayEntry": sonusSs7GatewayEntry,
       "sonusSs7GatewayIndex": sonusSs7GatewayIndex,
       "sonusSs7GatewayState": sonusSs7GatewayState,
       "sonusSs7GatewayName": sonusSs7GatewayName,
       "sonusSs7GatewaySocketType": sonusSs7GatewaySocketType,
       "sonusSs7GatewayActiveHost": sonusSs7GatewayActiveHost,
       "sonusSs7GatewayPriHostName": sonusSs7GatewayPriHostName,
       "sonusSs7GatewayPriHostIpaddr": sonusSs7GatewayPriHostIpaddr,
       "sonusSs7GatewayPriHostMode": sonusSs7GatewayPriHostMode,
       "sonusSs7GatewayPriHostOosDelayTimer": sonusSs7GatewayPriHostOosDelayTimer,
       "sonusSs7GatewaySecHostName": sonusSs7GatewaySecHostName,
       "sonusSs7GatewaySecHostIpaddr": sonusSs7GatewaySecHostIpaddr,
       "sonusSs7GatewaySecHostMode": sonusSs7GatewaySecHostMode,
       "sonusSs7GatewaySecHostOosDelayTimer": sonusSs7GatewaySecHostOosDelayTimer,
       "sonusSs7GatewayRowStatus": sonusSs7GatewayRowStatus,
       "sonusSs7GatewayPriAltHostIpaddr": sonusSs7GatewayPriAltHostIpaddr,
       "sonusSs7GatewaySecAltHostIpaddr": sonusSs7GatewaySecAltHostIpaddr,
       "sonusSs7GatewayGwType": sonusSs7GatewayGwType,
       "sonusSs7GatewayServerTcpPort": sonusSs7GatewayServerTcpPort,
       "sonusSs7GatewayClientTcpPort": sonusSs7GatewayClientTcpPort,
       "sonusSs7GatewayPriTaliTrafficControl": sonusSs7GatewayPriTaliTrafficControl,
       "sonusSs7GatewayPriAltTaliTrafficControl": sonusSs7GatewayPriAltTaliTrafficControl,
       "sonusSs7GatewaySecTaliTrafficControl": sonusSs7GatewaySecTaliTrafficControl,
       "sonusSs7GatewaySecAltTaliTrafficControl": sonusSs7GatewaySecAltTaliTrafficControl,
       "sonusSs7GatewayTimerTaliT1": sonusSs7GatewayTimerTaliT1,
       "sonusSs7GatewayTimerTaliT2": sonusSs7GatewayTimerTaliT2,
       "sonusSs7GatewayTimerTaliT3": sonusSs7GatewayTimerTaliT3,
       "sonusSs7GatewayTimerTaliT4": sonusSs7GatewayTimerTaliT4,
       "sonusSs7GatewayTaliSs7Type": sonusSs7GatewayTaliSs7Type,
       "sonusSs7GatewaySlsBits": sonusSs7GatewaySlsBits,
       "sonusSs7GatewayTaliIsupNormalization": sonusSs7GatewayTaliIsupNormalization,
       "sonusSs7GatewayTaliPstnPresentation": sonusSs7GatewayTaliPstnPresentation,
       "sonusSs7GatewayTaliGroupCode": sonusSs7GatewayTaliGroupCode,
       "sonusSs7GatewayStatusTable": sonusSs7GatewayStatusTable,
       "sonusSs7GatewayStatusEntry": sonusSs7GatewayStatusEntry,
       "sonusSs7GatewayStatusIndex": sonusSs7GatewayStatusIndex,
       "sonusSs7GatewayNextHost": sonusSs7GatewayNextHost,
       "sonusSs7GatewaySelectHost": sonusSs7GatewaySelectHost,
       "sonusSs7GatewayPriTaliConnState": sonusSs7GatewayPriTaliConnState,
       "sonusSs7GatewaySecTaliConnState": sonusSs7GatewaySecTaliConnState,
       "sonusSs7GatewayPriAltTaliConnState": sonusSs7GatewayPriAltTaliConnState,
       "sonusSs7GatewaySecAltTaliConnState": sonusSs7GatewaySecAltTaliConnState,
       "sonusSs7GatewayPriNearEndTaliVersion": sonusSs7GatewayPriNearEndTaliVersion,
       "sonusSs7GatewayPriFarEndTaliVersion": sonusSs7GatewayPriFarEndTaliVersion,
       "sonusSs7GatewayPriAltNearEndTaliVersion": sonusSs7GatewayPriAltNearEndTaliVersion,
       "sonusSs7GatewayPriAltFarEndTaliVersion": sonusSs7GatewayPriAltFarEndTaliVersion,
       "sonusSs7GatewaySecNearEndTaliVersion": sonusSs7GatewaySecNearEndTaliVersion,
       "sonusSs7GatewaySecFarEndTaliVersion": sonusSs7GatewaySecFarEndTaliVersion,
       "sonusSs7GatewaySecAltNearEndTaliVersion": sonusSs7GatewaySecAltNearEndTaliVersion,
       "sonusSs7GatewaySecAltFarEndTaliVersion": sonusSs7GatewaySecAltFarEndTaliVersion,
       "sonusSs7GatewayPSStatusTable": sonusSs7GatewayPSStatusTable,
       "sonusSs7GatewayPSStatusEntry": sonusSs7GatewayPSStatusEntry,
       "sonusSs7GatewayPSStatusIndex": sonusSs7GatewayPSStatusIndex,
       "sonusSs7GatewayPSStatusPSIndex": sonusSs7GatewayPSStatusPSIndex,
       "sonusSs7GatewayPSStatusPrimaryCE": sonusSs7GatewayPSStatusPrimaryCE,
       "sonusSs7GatewayPSStatusActiveLink": sonusSs7GatewayPSStatusActiveLink,
       "sonusSs7GatewayLinkStatusTable": sonusSs7GatewayLinkStatusTable,
       "sonusSs7GatewayLinkStatusEntry": sonusSs7GatewayLinkStatusEntry,
       "sonusSs7GatewayStatusLinkIndex": sonusSs7GatewayStatusLinkIndex,
       "sonusSs7GatewayStatusLinkPSIndex": sonusSs7GatewayStatusLinkPSIndex,
       "sonusSs7GatewayStatusLinkHostIndex": sonusSs7GatewayStatusLinkHostIndex,
       "sonusSs7GatewayStatusHostName": sonusSs7GatewayStatusHostName,
       "sonusSs7GatewayStatusHostIpaddr": sonusSs7GatewayStatusHostIpaddr,
       "sonusSs7GatewayStatusHostState": sonusSs7GatewayStatusHostState,
       "sonusSs7GatewayStatusHostCE": sonusSs7GatewayStatusHostCE,
       "sonusSs7NodeStatusTable": sonusSs7NodeStatusTable,
       "sonusSs7NodeStatusEntry": sonusSs7NodeStatusEntry,
       "sonusSs7NodeStatusIndex": sonusSs7NodeStatusIndex,
       "sonusSs7NodeStatIsup": sonusSs7NodeStatIsup,
       "sonusSs7NodeStatMtp": sonusSs7NodeStatMtp,
       "sonusSs7Node": sonusSs7Node,
       "sonusSs7NodeNextIndex": sonusSs7NodeNextIndex,
       "sonusSs7NodeTable": sonusSs7NodeTable,
       "sonusSs7NodeEntry": sonusSs7NodeEntry,
       "sonusSs7NodeIndex": sonusSs7NodeIndex,
       "sonusSs7NodeState": sonusSs7NodeState,
       "sonusSs7NodeName": sonusSs7NodeName,
       "sonusSs7NodePointCode": sonusSs7NodePointCode,
       "sonusSs7NodeServices": sonusSs7NodeServices,
       "sonusSs7NodeProtocol": sonusSs7NodeProtocol,
       "sonusSs7NodeTcapSsn": sonusSs7NodeTcapSsn,
       "sonusSs7NodeIsupStatus": sonusSs7NodeIsupStatus,
       "sonusSs7NodeTcapStatus": sonusSs7NodeTcapStatus,
       "sonusSs7NodeMtpStatus": sonusSs7NodeMtpStatus,
       "sonusSs7NodeGatewayAssignment": sonusSs7NodeGatewayAssignment,
       "sonusSs7NodeNativePointCode": sonusSs7NodeNativePointCode,
       "sonusSs7NodeMode": sonusSs7NodeMode,
       "sonusSs7NodeConnCntrl": sonusSs7NodeConnCntrl,
       "sonusSs7NodeRowStatus": sonusSs7NodeRowStatus,
       "sonusSs7NodeStdPointCode": sonusSs7NodeStdPointCode,
       "sonusSs7NodePointCodeSize": sonusSs7NodePointCodeSize,
       "sonusSs7NodePointCodeFormatType": sonusSs7NodePointCodeFormatType,
       "sonusSs7NodeServerProtocol": sonusSs7NodeServerProtocol,
       "sonusSs7NodeHandShakeInterval": sonusSs7NodeHandShakeInterval,
       "sonusSs7NodeTimerT1": sonusSs7NodeTimerT1,
       "sonusSs7NodeTimerT2": sonusSs7NodeTimerT2,
       "sonusSs7NodeTimerT3": sonusSs7NodeTimerT3,
       "sonusSs7NodeTimerT4": sonusSs7NodeTimerT4,
       "sonusSs7NodeTimerT5": sonusSs7NodeTimerT5,
       "sonusSs7NodeTimerT6": sonusSs7NodeTimerT6,
       "sonusSs7NodeTimerT7": sonusSs7NodeTimerT7,
       "sonusSs7NodeTimerT8": sonusSs7NodeTimerT8,
       "sonusSs7NodeTimerT9": sonusSs7NodeTimerT9,
       "sonusSs7NodeTimerT10": sonusSs7NodeTimerT10,
       "sonusSs7NodeTimerT11": sonusSs7NodeTimerT11,
       "sonusSs7NodeTimerT12": sonusSs7NodeTimerT12,
       "sonusSs7NodeTimerT13": sonusSs7NodeTimerT13,
       "sonusSs7NodeTimerT14": sonusSs7NodeTimerT14,
       "sonusSs7NodeTimerT15": sonusSs7NodeTimerT15,
       "sonusSs7NodeTimerT16": sonusSs7NodeTimerT16,
       "sonusSs7NodeTimerT17": sonusSs7NodeTimerT17,
       "sonusSs7NodeTimerT18": sonusSs7NodeTimerT18,
       "sonusSs7NodeTimerT19": sonusSs7NodeTimerT19,
       "sonusSs7NodeTimerT20": sonusSs7NodeTimerT20,
       "sonusSs7NodeTimerT21": sonusSs7NodeTimerT21,
       "sonusSs7NodeTimerT22": sonusSs7NodeTimerT22,
       "sonusSs7NodeTimerT23": sonusSs7NodeTimerT23,
       "sonusSs7NodeTimerT24": sonusSs7NodeTimerT24,
       "sonusSs7NodeTimerT25": sonusSs7NodeTimerT25,
       "sonusSs7NodeTimerT26": sonusSs7NodeTimerT26,
       "sonusSs7NodeTimerT27": sonusSs7NodeTimerT27,
       "sonusSs7NodeTimerT28": sonusSs7NodeTimerT28,
       "sonusSs7NodeTimerT29": sonusSs7NodeTimerT29,
       "sonusSs7NodeTimerT30": sonusSs7NodeTimerT30,
       "sonusSs7NodeTimerT31": sonusSs7NodeTimerT31,
       "sonusSs7NodeTimerT32": sonusSs7NodeTimerT32,
       "sonusSs7NodeTimerT33": sonusSs7NodeTimerT33,
       "sonusSs7NodeTimerT34": sonusSs7NodeTimerT34,
       "sonusSs7NodeTimerT35": sonusSs7NodeTimerT35,
       "sonusSs7NodeTimerT36": sonusSs7NodeTimerT36,
       "sonusSs7NodeTimerT37": sonusSs7NodeTimerT37,
       "sonusSs7NodeTimerT38": sonusSs7NodeTimerT38,
       "sonusSs7NodeTimerT39": sonusSs7NodeTimerT39,
       "sonusSs7NodeTimerT40": sonusSs7NodeTimerT40,
       "sonusSs7NodeTimerTAcc": sonusSs7NodeTimerTAcc,
       "sonusSs7NodeTimerTCcr": sonusSs7NodeTimerTCcr,
       "sonusSs7NodeTimerTCcrr": sonusSs7NodeTimerTCcrr,
       "sonusSs7NodeTimerTCgb": sonusSs7NodeTimerTCgb,
       "sonusSs7NodeTimerTCra": sonusSs7NodeTimerTCra,
       "sonusSs7NodeTimerTCrm": sonusSs7NodeTimerTCrm,
       "sonusSs7NodeTimerTCvt": sonusSs7NodeTimerTCvt,
       "sonusSs7NodeTimerTExm": sonusSs7NodeTimerTExm,
       "sonusSs7NodeTimerTGrs": sonusSs7NodeTimerTGrs,
       "sonusSs7NodeTimerTHga": sonusSs7NodeTimerTHga,
       "sonusSs7NodeTimerTScga": sonusSs7NodeTimerTScga,
       "sonusSs7NodeTimerTScgad": sonusSs7NodeTimerTScgad,
       "sonusSs7NodeApplProfileName": sonusSs7NodeApplProfileName,
       "sonusSs7NodeNetworkInd": sonusSs7NodeNetworkInd,
       "sonusSs7NodeSlsBits": sonusSs7NodeSlsBits,
       "sonusSs7NodeTimerTA": sonusSs7NodeTimerTA,
       "sonusSs7NodeTimerTBlom": sonusSs7NodeTimerTBlom,
       "sonusSs7NodeTimerTCotd": sonusSs7NodeTimerTCotd,
       "sonusSs7NodeTimerTCotl": sonusSs7NodeTimerTCotl,
       "sonusSs7NodeTimerTSus": sonusSs7NodeTimerTSus,
       "sonusSs7NodeProfile": sonusSs7NodeProfile,
       "sonusSs7NodeProfileNextIndex": sonusSs7NodeProfileNextIndex,
       "sonusSs7NodeProfileTable": sonusSs7NodeProfileTable,
       "sonusSs7NodeProfileEntry": sonusSs7NodeProfileEntry,
       "sonusSs7NodeProfileIndex": sonusSs7NodeProfileIndex,
       "sonusSs7NodeProfileName": sonusSs7NodeProfileName,
       "sonusSs7PointCodeSize": sonusSs7PointCodeSize,
       "sonusSs7PointCodeFormatType": sonusSs7PointCodeFormatType,
       "sonusSs7ServerProtocol": sonusSs7ServerProtocol,
       "sonusSs7HandShakeInterval": sonusSs7HandShakeInterval,
       "sonusSs7TimerT1": sonusSs7TimerT1,
       "sonusSs7TimerT2": sonusSs7TimerT2,
       "sonusSs7TimerT3": sonusSs7TimerT3,
       "sonusSs7TimerT4": sonusSs7TimerT4,
       "sonusSs7TimerT5": sonusSs7TimerT5,
       "sonusSs7TimerT6": sonusSs7TimerT6,
       "sonusSs7TimerT7": sonusSs7TimerT7,
       "sonusSs7TimerT8": sonusSs7TimerT8,
       "sonusSs7TimerT9": sonusSs7TimerT9,
       "sonusSs7TimerT10": sonusSs7TimerT10,
       "sonusSs7TimerT11": sonusSs7TimerT11,
       "sonusSs7TimerT12": sonusSs7TimerT12,
       "sonusSs7TimerT13": sonusSs7TimerT13,
       "sonusSs7TimerT14": sonusSs7TimerT14,
       "sonusSs7TimerT15": sonusSs7TimerT15,
       "sonusSs7TimerT16": sonusSs7TimerT16,
       "sonusSs7TimerT17": sonusSs7TimerT17,
       "sonusSs7TimerT18": sonusSs7TimerT18,
       "sonusSs7TimerT19": sonusSs7TimerT19,
       "sonusSs7TimerT20": sonusSs7TimerT20,
       "sonusSs7TimerT21": sonusSs7TimerT21,
       "sonusSs7TimerT22": sonusSs7TimerT22,
       "sonusSs7TimerT23": sonusSs7TimerT23,
       "sonusSs7TimerT24": sonusSs7TimerT24,
       "sonusSs7TimerT25": sonusSs7TimerT25,
       "sonusSs7TimerT26": sonusSs7TimerT26,
       "sonusSs7TimerT27": sonusSs7TimerT27,
       "sonusSs7TimerT28": sonusSs7TimerT28,
       "sonusSs7TimerT29": sonusSs7TimerT29,
       "sonusSs7TimerT30": sonusSs7TimerT30,
       "sonusSs7TimerT31": sonusSs7TimerT31,
       "sonusSs7TimerT32": sonusSs7TimerT32,
       "sonusSs7TimerT33": sonusSs7TimerT33,
       "sonusSs7TimerT34": sonusSs7TimerT34,
       "sonusSs7TimerT35": sonusSs7TimerT35,
       "sonusSs7TimerT36": sonusSs7TimerT36,
       "sonusSs7TimerT37": sonusSs7TimerT37,
       "sonusSs7TimerT38": sonusSs7TimerT38,
       "sonusSs7TimerT39": sonusSs7TimerT39,
       "sonusSs7TimerT40": sonusSs7TimerT40,
       "sonusSs7TimerTAcc": sonusSs7TimerTAcc,
       "sonusSs7TimerTCcr": sonusSs7TimerTCcr,
       "sonusSs7TimerTCcrr": sonusSs7TimerTCcrr,
       "sonusSs7TimerTCgb": sonusSs7TimerTCgb,
       "sonusSs7TimerTCra": sonusSs7TimerTCra,
       "sonusSs7TimerTCrm": sonusSs7TimerTCrm,
       "sonusSs7TimerTCvt": sonusSs7TimerTCvt,
       "sonusSs7TimerTExm": sonusSs7TimerTExm,
       "sonusSs7TimerTGrs": sonusSs7TimerTGrs,
       "sonusSs7TimerTHga": sonusSs7TimerTHga,
       "sonusSs7TimerTScga": sonusSs7TimerTScga,
       "sonusSs7TimerTScgad": sonusSs7TimerTScgad,
       "sonusSs7NodeProfileState": sonusSs7NodeProfileState,
       "sonusSs7NodeProfileRowStatus": sonusSs7NodeProfileRowStatus,
       "sonusSs7NodeProfileNetworkInd": sonusSs7NodeProfileNetworkInd,
       "sonusSs7SlsBits": sonusSs7SlsBits,
       "sonusSs7TimerTA": sonusSs7TimerTA,
       "sonusSs7TimerTBlom": sonusSs7TimerTBlom,
       "sonusSs7TimerTCotd": sonusSs7TimerTCotd,
       "sonusSs7TimerTCotl": sonusSs7TimerTCotl,
       "sonusSs7TimerTSus": sonusSs7TimerTSus,
       "sonusSs7ServicesMIBNotifications": sonusSs7ServicesMIBNotifications,
       "sonusSs7ServicesMIBNotificationsPrefix": sonusSs7ServicesMIBNotificationsPrefix,
       "sonusSs7NodeConnectionEstablishedNotification": sonusSs7NodeConnectionEstablishedNotification,
       "sonusSs7NodeConnectionFailedNotification": sonusSs7NodeConnectionFailedNotification,
       "sonusSs7NodeConnectionStateChangeNotification": sonusSs7NodeConnectionStateChangeNotification,
       "sonusSs7NodeMtpStateChangeNotification": sonusSs7NodeMtpStateChangeNotification,
       "sonusSs7ServicesMIBNotificationsObjects": sonusSs7ServicesMIBNotificationsObjects,
       "sonusSs7NodeServiceType": sonusSs7NodeServiceType,
       "sonusSs7NodeStateChangeReason": sonusSs7NodeStateChangeReason,
       "sonusSs7NodeCurrentState": sonusSs7NodeCurrentState,
       "sonusSs7NodeAffectedPointCode": sonusSs7NodeAffectedPointCode}
)
