# SNMP MIB module (ENTERASYS-LSNAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-LSNAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:05 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber",
    "InetVersion")

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

etsysLsnatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74)
)
etsysLsnatMIB.setRevisions(
        ("2010-06-01 14:40",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysLsnatGlobal_ObjectIdentity = ObjectIdentity
etsysLsnatGlobal = _EtsysLsnatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1)
)
_EtsysLsnatGlobalStats_ObjectIdentity = ObjectIdentity
etsysLsnatGlobalStats = _EtsysLsnatGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1)
)
_EtsysLsnatStatsRealsUsed_Type = Gauge32
_EtsysLsnatStatsRealsUsed_Object = MibScalar
etsysLsnatStatsRealsUsed = _EtsysLsnatStatsRealsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 1),
    _EtsysLsnatStatsRealsUsed_Type()
)
etsysLsnatStatsRealsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsRealsUsed.setStatus("current")
_EtsysLsnatStatsServerfarmsUsed_Type = Gauge32
_EtsysLsnatStatsServerfarmsUsed_Object = MibScalar
etsysLsnatStatsServerfarmsUsed = _EtsysLsnatStatsServerfarmsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 2),
    _EtsysLsnatStatsServerfarmsUsed_Type()
)
etsysLsnatStatsServerfarmsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsServerfarmsUsed.setStatus("current")
_EtsysLsnatStatsVserversUsed_Type = Gauge32
_EtsysLsnatStatsVserversUsed_Object = MibScalar
etsysLsnatStatsVserversUsed = _EtsysLsnatStatsVserversUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 3),
    _EtsysLsnatStatsVserversUsed_Type()
)
etsysLsnatStatsVserversUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsVserversUsed.setStatus("current")
_EtsysLsnatStatsVserversIPsUsed_Type = Gauge32
_EtsysLsnatStatsVserversIPsUsed_Object = MibScalar
etsysLsnatStatsVserversIPsUsed = _EtsysLsnatStatsVserversIPsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 4),
    _EtsysLsnatStatsVserversIPsUsed_Type()
)
etsysLsnatStatsVserversIPsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsVserversIPsUsed.setStatus("current")
_EtsysLsnatStatsBindingsCurrent_Type = Gauge32
_EtsysLsnatStatsBindingsCurrent_Object = MibScalar
etsysLsnatStatsBindingsCurrent = _EtsysLsnatStatsBindingsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 5),
    _EtsysLsnatStatsBindingsCurrent_Type()
)
etsysLsnatStatsBindingsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsCurrent.setStatus("current")
_EtsysLsnatStatsBindingsHigh_Type = Gauge32
_EtsysLsnatStatsBindingsHigh_Object = MibScalar
etsysLsnatStatsBindingsHigh = _EtsysLsnatStatsBindingsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 6),
    _EtsysLsnatStatsBindingsHigh_Type()
)
etsysLsnatStatsBindingsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsHigh.setStatus("current")
_EtsysLsnatStatsBindingsDeleted_Type = Counter32
_EtsysLsnatStatsBindingsDeleted_Object = MibScalar
etsysLsnatStatsBindingsDeleted = _EtsysLsnatStatsBindingsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 7),
    _EtsysLsnatStatsBindingsDeleted_Type()
)
etsysLsnatStatsBindingsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsDeleted.setStatus("current")
_EtsysLsnatStatsBindingsTotal_Type = Counter32
_EtsysLsnatStatsBindingsTotal_Object = MibScalar
etsysLsnatStatsBindingsTotal = _EtsysLsnatStatsBindingsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 8),
    _EtsysLsnatStatsBindingsTotal_Type()
)
etsysLsnatStatsBindingsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsTotal.setStatus("current")
_EtsysLsnatStatsBindingsExhausted_Type = Counter32
_EtsysLsnatStatsBindingsExhausted_Object = MibScalar
etsysLsnatStatsBindingsExhausted = _EtsysLsnatStatsBindingsExhausted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 9),
    _EtsysLsnatStatsBindingsExhausted_Type()
)
etsysLsnatStatsBindingsExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsExhausted.setStatus("current")
_EtsysLsnatStatsBindingsNoReals_Type = Counter32
_EtsysLsnatStatsBindingsNoReals_Object = MibScalar
etsysLsnatStatsBindingsNoReals = _EtsysLsnatStatsBindingsNoReals_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 10),
    _EtsysLsnatStatsBindingsNoReals_Type()
)
etsysLsnatStatsBindingsNoReals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsNoReals.setStatus("current")
_EtsysLsnatStatsBindingsNoPortmapPort_Type = Counter32
_EtsysLsnatStatsBindingsNoPortmapPort_Object = MibScalar
etsysLsnatStatsBindingsNoPortmapPort = _EtsysLsnatStatsBindingsNoPortmapPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 11),
    _EtsysLsnatStatsBindingsNoPortmapPort_Type()
)
etsysLsnatStatsBindingsNoPortmapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsNoPortmapPort.setStatus("current")
_EtsysLsnatStatsBindingsNoFtpALG_Type = Counter32
_EtsysLsnatStatsBindingsNoFtpALG_Object = MibScalar
etsysLsnatStatsBindingsNoFtpALG = _EtsysLsnatStatsBindingsNoFtpALG_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 12),
    _EtsysLsnatStatsBindingsNoFtpALG_Type()
)
etsysLsnatStatsBindingsNoFtpALG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsNoFtpALG.setStatus("current")
_EtsysLsnatStatsBindingsPerSecond_Type = Gauge32
_EtsysLsnatStatsBindingsPerSecond_Object = MibScalar
etsysLsnatStatsBindingsPerSecond = _EtsysLsnatStatsBindingsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 13),
    _EtsysLsnatStatsBindingsPerSecond_Type()
)
etsysLsnatStatsBindingsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsBindingsPerSecond.setStatus("current")
_EtsysLsnatStatsVserverActive_Type = Gauge32
_EtsysLsnatStatsVserverActive_Object = MibScalar
etsysLsnatStatsVserverActive = _EtsysLsnatStatsVserverActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 14),
    _EtsysLsnatStatsVserverActive_Type()
)
etsysLsnatStatsVserverActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsVserverActive.setStatus("current")
_EtsysLsnatStatsVserverHigh_Type = Gauge32
_EtsysLsnatStatsVserverHigh_Object = MibScalar
etsysLsnatStatsVserverHigh = _EtsysLsnatStatsVserverHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 15),
    _EtsysLsnatStatsVserverHigh_Type()
)
etsysLsnatStatsVserverHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsVserverHigh.setStatus("current")
_EtsysLsnatStatsServerfarmActive_Type = Gauge32
_EtsysLsnatStatsServerfarmActive_Object = MibScalar
etsysLsnatStatsServerfarmActive = _EtsysLsnatStatsServerfarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 16),
    _EtsysLsnatStatsServerfarmActive_Type()
)
etsysLsnatStatsServerfarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsServerfarmActive.setStatus("current")
_EtsysLsnatStatsServerfarmHigh_Type = Gauge32
_EtsysLsnatStatsServerfarmHigh_Object = MibScalar
etsysLsnatStatsServerfarmHigh = _EtsysLsnatStatsServerfarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 17),
    _EtsysLsnatStatsServerfarmHigh_Type()
)
etsysLsnatStatsServerfarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsServerfarmHigh.setStatus("current")
_EtsysLsnatStatsRealActive_Type = Gauge32
_EtsysLsnatStatsRealActive_Object = MibScalar
etsysLsnatStatsRealActive = _EtsysLsnatStatsRealActive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 18),
    _EtsysLsnatStatsRealActive_Type()
)
etsysLsnatStatsRealActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsRealActive.setStatus("current")
_EtsysLsnatStatsRealHigh_Type = Gauge32
_EtsysLsnatStatsRealHigh_Object = MibScalar
etsysLsnatStatsRealHigh = _EtsysLsnatStatsRealHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 19),
    _EtsysLsnatStatsRealHigh_Type()
)
etsysLsnatStatsRealHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsRealHigh.setStatus("current")
_EtsysLsnatStatsStickyEntriesTotal_Type = Counter32
_EtsysLsnatStatsStickyEntriesTotal_Object = MibScalar
etsysLsnatStatsStickyEntriesTotal = _EtsysLsnatStatsStickyEntriesTotal_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 20),
    _EtsysLsnatStatsStickyEntriesTotal_Type()
)
etsysLsnatStatsStickyEntriesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsStickyEntriesTotal.setStatus("current")
_EtsysLsnatStatsStickyBindingsStuckTotal_Type = Counter32
_EtsysLsnatStatsStickyBindingsStuckTotal_Object = MibScalar
etsysLsnatStatsStickyBindingsStuckTotal = _EtsysLsnatStatsStickyBindingsStuckTotal_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 21),
    _EtsysLsnatStatsStickyBindingsStuckTotal_Type()
)
etsysLsnatStatsStickyBindingsStuckTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsStickyBindingsStuckTotal.setStatus("current")
_EtsysLsnatStatsStickyBindingsStuckCurrent_Type = Gauge32
_EtsysLsnatStatsStickyBindingsStuckCurrent_Object = MibScalar
etsysLsnatStatsStickyBindingsStuckCurrent = _EtsysLsnatStatsStickyBindingsStuckCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 22),
    _EtsysLsnatStatsStickyBindingsStuckCurrent_Type()
)
etsysLsnatStatsStickyBindingsStuckCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsStickyBindingsStuckCurrent.setStatus("current")
_EtsysLsnatStatsStickyActiveEntries_Type = Gauge32
_EtsysLsnatStatsStickyActiveEntries_Object = MibScalar
etsysLsnatStatsStickyActiveEntries = _EtsysLsnatStatsStickyActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 23),
    _EtsysLsnatStatsStickyActiveEntries_Type()
)
etsysLsnatStatsStickyActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsStickyActiveEntries.setStatus("current")
_EtsysLsnatStatsStickyActiveEntriesHigh_Type = Gauge32
_EtsysLsnatStatsStickyActiveEntriesHigh_Object = MibScalar
etsysLsnatStatsStickyActiveEntriesHigh = _EtsysLsnatStatsStickyActiveEntriesHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 24),
    _EtsysLsnatStatsStickyActiveEntriesHigh_Type()
)
etsysLsnatStatsStickyActiveEntriesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsStickyActiveEntriesHigh.setStatus("current")
_EtsysLsnatStatsStickyEntriesExhausted_Type = Counter32
_EtsysLsnatStatsStickyEntriesExhausted_Object = MibScalar
etsysLsnatStatsStickyEntriesExhausted = _EtsysLsnatStatsStickyEntriesExhausted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 25),
    _EtsysLsnatStatsStickyEntriesExhausted_Type()
)
etsysLsnatStatsStickyEntriesExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsStickyEntriesExhausted.setStatus("current")


class _EtsysLsnatStatsClear_Type(TruthValue):
    """Custom type etsysLsnatStatsClear based on TruthValue"""


_EtsysLsnatStatsClear_Object = MibScalar
etsysLsnatStatsClear = _EtsysLsnatStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 26),
    _EtsysLsnatStatsClear_Type()
)
etsysLsnatStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatStatsClear.setStatus("current")
_EtsysLsnatStatsClearDateAndTime_Type = DateAndTime
_EtsysLsnatStatsClearDateAndTime_Object = MibScalar
etsysLsnatStatsClearDateAndTime = _EtsysLsnatStatsClearDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 27),
    _EtsysLsnatStatsClearDateAndTime_Type()
)
etsysLsnatStatsClearDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsClearDateAndTime.setStatus("current")
_EtsysLsnatStatsRealServerAccessClientsCount_Type = Gauge32
_EtsysLsnatStatsRealServerAccessClientsCount_Object = MibScalar
etsysLsnatStatsRealServerAccessClientsCount = _EtsysLsnatStatsRealServerAccessClientsCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 28),
    _EtsysLsnatStatsRealServerAccessClientsCount_Type()
)
etsysLsnatStatsRealServerAccessClientsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsRealServerAccessClientsCount.setStatus("current")
_EtsysLsnatStatsMinTimeoutValue_Type = Unsigned32
_EtsysLsnatStatsMinTimeoutValue_Object = MibScalar
etsysLsnatStatsMinTimeoutValue = _EtsysLsnatStatsMinTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 29),
    _EtsysLsnatStatsMinTimeoutValue_Type()
)
etsysLsnatStatsMinTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsMinTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatStatsMinTimeoutValue.setUnits("seconds")
_EtsysLsnatStatsMaxTimeoutValue_Type = Unsigned32
_EtsysLsnatStatsMaxTimeoutValue_Object = MibScalar
etsysLsnatStatsMaxTimeoutValue = _EtsysLsnatStatsMaxTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 1, 30),
    _EtsysLsnatStatsMaxTimeoutValue_Type()
)
etsysLsnatStatsMaxTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStatsMaxTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatStatsMaxTimeoutValue.setUnits("seconds")
_EtsysLsnatGlobalIpv4Config_ObjectIdentity = ObjectIdentity
etsysLsnatGlobalIpv4Config = _EtsysLsnatGlobalIpv4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 2)
)


class _EtsysLsnatIpv4ConfigFTPCtrlPort_Type(InetPortNumber):
    """Custom type etsysLsnatIpv4ConfigFTPCtrlPort based on InetPortNumber"""
    defaultValue = 21

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatIpv4ConfigFTPCtrlPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatIpv4ConfigFTPCtrlPort_Object = MibScalar
etsysLsnatIpv4ConfigFTPCtrlPort = _EtsysLsnatIpv4ConfigFTPCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 2, 1),
    _EtsysLsnatIpv4ConfigFTPCtrlPort_Type()
)
etsysLsnatIpv4ConfigFTPCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatIpv4ConfigFTPCtrlPort.setStatus("current")


class _EtsysLsnatIpv4ConfigTFTPCtrlPort_Type(InetPortNumber):
    """Custom type etsysLsnatIpv4ConfigTFTPCtrlPort based on InetPortNumber"""
    defaultValue = 69

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatIpv4ConfigTFTPCtrlPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatIpv4ConfigTFTPCtrlPort_Object = MibScalar
etsysLsnatIpv4ConfigTFTPCtrlPort = _EtsysLsnatIpv4ConfigTFTPCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 2, 2),
    _EtsysLsnatIpv4ConfigTFTPCtrlPort_Type()
)
etsysLsnatIpv4ConfigTFTPCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatIpv4ConfigTFTPCtrlPort.setStatus("current")


class _EtsysLsnatIpv4ConfigRealServerAccess_Type(Integer32):
    """Custom type etsysLsnatIpv4ConfigRealServerAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unrestricted", 2))
    )


_EtsysLsnatIpv4ConfigRealServerAccess_Type.__name__ = "Integer32"
_EtsysLsnatIpv4ConfigRealServerAccess_Object = MibScalar
etsysLsnatIpv4ConfigRealServerAccess = _EtsysLsnatIpv4ConfigRealServerAccess_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 2, 3),
    _EtsysLsnatIpv4ConfigRealServerAccess_Type()
)
etsysLsnatIpv4ConfigRealServerAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatIpv4ConfigRealServerAccess.setStatus("current")


class _EtsysLsnatIpv4ConfigFinRstTimeout_Type(Unsigned32):
    """Custom type etsysLsnatIpv4ConfigFinRstTimeout based on Unsigned32"""
    defaultValue = 3


_EtsysLsnatIpv4ConfigFinRstTimeout_Object = MibScalar
etsysLsnatIpv4ConfigFinRstTimeout = _EtsysLsnatIpv4ConfigFinRstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 2, 4),
    _EtsysLsnatIpv4ConfigFinRstTimeout_Type()
)
etsysLsnatIpv4ConfigFinRstTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatIpv4ConfigFinRstTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatIpv4ConfigFinRstTimeout.setUnits("seconds")


class _EtsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus_Type(Integer32):
    """Custom type etsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus based on Integer32"""
    defaultValue = 2

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


_EtsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus_Type.__name__ = "Integer32"
_EtsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus_Object = MibScalar
etsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus = _EtsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 1, 2, 5),
    _EtsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus_Type()
)
etsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus.setStatus("current")
_EtsysLsnatTables_ObjectIdentity = ObjectIdentity
etsysLsnatTables = _EtsysLsnatTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2)
)
_EtsysLsnatRealServerAccessClientTable_Object = MibTable
etsysLsnatRealServerAccessClientTable = _EtsysLsnatRealServerAccessClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 1)
)
if mibBuilder.loadTexts:
    etsysLsnatRealServerAccessClientTable.setStatus("current")
_EtsysLsnatRealServerAccessClientEntry_Object = MibTableRow
etsysLsnatRealServerAccessClientEntry = _EtsysLsnatRealServerAccessClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 1, 1)
)
etsysLsnatRealServerAccessClientEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerAccessClientAddressType"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerAccessClientIp"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerAccessClientPrefixLen"),
)
if mibBuilder.loadTexts:
    etsysLsnatRealServerAccessClientEntry.setStatus("current")
_EtsysLsnatRealServerAccessClientAddressType_Type = InetAddressType
_EtsysLsnatRealServerAccessClientAddressType_Object = MibTableColumn
etsysLsnatRealServerAccessClientAddressType = _EtsysLsnatRealServerAccessClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 1, 1, 1),
    _EtsysLsnatRealServerAccessClientAddressType_Type()
)
etsysLsnatRealServerAccessClientAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatRealServerAccessClientAddressType.setStatus("current")
_EtsysLsnatRealServerAccessClientIp_Type = InetAddress
_EtsysLsnatRealServerAccessClientIp_Object = MibTableColumn
etsysLsnatRealServerAccessClientIp = _EtsysLsnatRealServerAccessClientIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 1, 1, 2),
    _EtsysLsnatRealServerAccessClientIp_Type()
)
etsysLsnatRealServerAccessClientIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatRealServerAccessClientIp.setStatus("current")
_EtsysLsnatRealServerAccessClientPrefixLen_Type = InetAddressPrefixLength
_EtsysLsnatRealServerAccessClientPrefixLen_Object = MibTableColumn
etsysLsnatRealServerAccessClientPrefixLen = _EtsysLsnatRealServerAccessClientPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 1, 1, 3),
    _EtsysLsnatRealServerAccessClientPrefixLen_Type()
)
etsysLsnatRealServerAccessClientPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatRealServerAccessClientPrefixLen.setStatus("current")
_EtsysLsnatRealServerAccessClientRowStatus_Type = RowStatus
_EtsysLsnatRealServerAccessClientRowStatus_Object = MibTableColumn
etsysLsnatRealServerAccessClientRowStatus = _EtsysLsnatRealServerAccessClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 1, 1, 4),
    _EtsysLsnatRealServerAccessClientRowStatus_Type()
)
etsysLsnatRealServerAccessClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerAccessClientRowStatus.setStatus("current")
_EtsysLsnatServerfarmTable_Object = MibTable
etsysLsnatServerfarmTable = _EtsysLsnatServerfarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2)
)
if mibBuilder.loadTexts:
    etsysLsnatServerfarmTable.setStatus("current")
_EtsysLsnatServerfarmEntry_Object = MibTableRow
etsysLsnatServerfarmEntry = _EtsysLsnatServerfarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1)
)
etsysLsnatServerfarmEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmInetVersion"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmName"),
)
if mibBuilder.loadTexts:
    etsysLsnatServerfarmEntry.setStatus("current")
_EtsysLsnatServerfarmInetVersion_Type = InetVersion
_EtsysLsnatServerfarmInetVersion_Object = MibTableColumn
etsysLsnatServerfarmInetVersion = _EtsysLsnatServerfarmInetVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 1),
    _EtsysLsnatServerfarmInetVersion_Type()
)
etsysLsnatServerfarmInetVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmInetVersion.setStatus("current")


class _EtsysLsnatServerfarmName_Type(SnmpAdminString):
    """Custom type etsysLsnatServerfarmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysLsnatServerfarmName_Type.__name__ = "SnmpAdminString"
_EtsysLsnatServerfarmName_Object = MibTableColumn
etsysLsnatServerfarmName = _EtsysLsnatServerfarmName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 2),
    _EtsysLsnatServerfarmName_Type()
)
etsysLsnatServerfarmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmName.setStatus("current")


class _EtsysLsnatServerfarmPredictor_Type(Integer32):
    """Custom type etsysLsnatServerfarmPredictor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leastconns", 2),
          ("roundrobin", 1))
    )


_EtsysLsnatServerfarmPredictor_Type.__name__ = "Integer32"
_EtsysLsnatServerfarmPredictor_Object = MibTableColumn
etsysLsnatServerfarmPredictor = _EtsysLsnatServerfarmPredictor_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 3),
    _EtsysLsnatServerfarmPredictor_Type()
)
etsysLsnatServerfarmPredictor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmPredictor.setStatus("current")


class _EtsysLsnatServerfarmAdminStatus_Type(Integer32):
    """Custom type etsysLsnatServerfarmAdminStatus based on Integer32"""
    defaultValue = 2

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


_EtsysLsnatServerfarmAdminStatus_Type.__name__ = "Integer32"
_EtsysLsnatServerfarmAdminStatus_Object = MibTableColumn
etsysLsnatServerfarmAdminStatus = _EtsysLsnatServerfarmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 4),
    _EtsysLsnatServerfarmAdminStatus_Type()
)
etsysLsnatServerfarmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmAdminStatus.setStatus("current")


class _EtsysLsnatServerfarmOperStatus_Type(Integer32):
    """Custom type etsysLsnatServerfarmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtsysLsnatServerfarmOperStatus_Type.__name__ = "Integer32"
_EtsysLsnatServerfarmOperStatus_Object = MibTableColumn
etsysLsnatServerfarmOperStatus = _EtsysLsnatServerfarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 5),
    _EtsysLsnatServerfarmOperStatus_Type()
)
etsysLsnatServerfarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmOperStatus.setStatus("current")
_EtsysLsnatServerfarmConns_Type = Gauge32
_EtsysLsnatServerfarmConns_Object = MibTableColumn
etsysLsnatServerfarmConns = _EtsysLsnatServerfarmConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 6),
    _EtsysLsnatServerfarmConns_Type()
)
etsysLsnatServerfarmConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmConns.setStatus("current")
_EtsysLsnatServerfarmHits_Type = Counter32
_EtsysLsnatServerfarmHits_Object = MibTableColumn
etsysLsnatServerfarmHits = _EtsysLsnatServerfarmHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 7),
    _EtsysLsnatServerfarmHits_Type()
)
etsysLsnatServerfarmHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmHits.setStatus("current")
_EtsysLsnatServerfarmStateChanges_Type = Counter32
_EtsysLsnatServerfarmStateChanges_Object = MibTableColumn
etsysLsnatServerfarmStateChanges = _EtsysLsnatServerfarmStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 8),
    _EtsysLsnatServerfarmStateChanges_Type()
)
etsysLsnatServerfarmStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmStateChanges.setStatus("current")
_EtsysLsnatServerfarmLastStateChangeDateAndTime_Type = DateAndTime
_EtsysLsnatServerfarmLastStateChangeDateAndTime_Object = MibTableColumn
etsysLsnatServerfarmLastStateChangeDateAndTime = _EtsysLsnatServerfarmLastStateChangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 9),
    _EtsysLsnatServerfarmLastStateChangeDateAndTime_Type()
)
etsysLsnatServerfarmLastStateChangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmLastStateChangeDateAndTime.setStatus("current")
_EtsysLsnatServerfarmRealsCfg_Type = Gauge32
_EtsysLsnatServerfarmRealsCfg_Object = MibTableColumn
etsysLsnatServerfarmRealsCfg = _EtsysLsnatServerfarmRealsCfg_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 10),
    _EtsysLsnatServerfarmRealsCfg_Type()
)
etsysLsnatServerfarmRealsCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmRealsCfg.setStatus("current")
_EtsysLsnatServerfarmRealsUp_Type = Gauge32
_EtsysLsnatServerfarmRealsUp_Object = MibTableColumn
etsysLsnatServerfarmRealsUp = _EtsysLsnatServerfarmRealsUp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 11),
    _EtsysLsnatServerfarmRealsUp_Type()
)
etsysLsnatServerfarmRealsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmRealsUp.setStatus("current")
_EtsysLsnatServerfarmVserversCfg_Type = Gauge32
_EtsysLsnatServerfarmVserversCfg_Object = MibTableColumn
etsysLsnatServerfarmVserversCfg = _EtsysLsnatServerfarmVserversCfg_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 12),
    _EtsysLsnatServerfarmVserversCfg_Type()
)
etsysLsnatServerfarmVserversCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmVserversCfg.setStatus("current")
_EtsysLsnatServerfarmRowStatus_Type = RowStatus
_EtsysLsnatServerfarmRowStatus_Object = MibTableColumn
etsysLsnatServerfarmRowStatus = _EtsysLsnatServerfarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 2, 1, 13),
    _EtsysLsnatServerfarmRowStatus_Type()
)
etsysLsnatServerfarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatServerfarmRowStatus.setStatus("current")
_EtsysLsnatRealServerTable_Object = MibTable
etsysLsnatRealServerTable = _EtsysLsnatRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3)
)
if mibBuilder.loadTexts:
    etsysLsnatRealServerTable.setStatus("current")
_EtsysLsnatRealServerEntry_Object = MibTableRow
etsysLsnatRealServerEntry = _EtsysLsnatRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1)
)
etsysLsnatRealServerEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerAddressType"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmName"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerIp"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerPort"),
)
if mibBuilder.loadTexts:
    etsysLsnatRealServerEntry.setStatus("current")
_EtsysLsnatRealServerAddressType_Type = InetAddressType
_EtsysLsnatRealServerAddressType_Object = MibTableColumn
etsysLsnatRealServerAddressType = _EtsysLsnatRealServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 1),
    _EtsysLsnatRealServerAddressType_Type()
)
etsysLsnatRealServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatRealServerAddressType.setStatus("current")
_EtsysLsnatRealServerIp_Type = InetAddress
_EtsysLsnatRealServerIp_Object = MibTableColumn
etsysLsnatRealServerIp = _EtsysLsnatRealServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 2),
    _EtsysLsnatRealServerIp_Type()
)
etsysLsnatRealServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatRealServerIp.setStatus("current")


class _EtsysLsnatRealServerPort_Type(InetPortNumber):
    """Custom type etsysLsnatRealServerPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatRealServerPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatRealServerPort_Object = MibTableColumn
etsysLsnatRealServerPort = _EtsysLsnatRealServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 3),
    _EtsysLsnatRealServerPort_Type()
)
etsysLsnatRealServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatRealServerPort.setStatus("current")


class _EtsysLsnatRealServerWeight_Type(Unsigned32):
    """Custom type etsysLsnatRealServerWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 155),
    )


_EtsysLsnatRealServerWeight_Type.__name__ = "Unsigned32"
_EtsysLsnatRealServerWeight_Object = MibTableColumn
etsysLsnatRealServerWeight = _EtsysLsnatRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 4),
    _EtsysLsnatRealServerWeight_Type()
)
etsysLsnatRealServerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerWeight.setStatus("current")


class _EtsysLsnatRealServerMaxConns_Type(Unsigned32):
    """Custom type etsysLsnatRealServerMaxConns based on Unsigned32"""
    defaultValue = 0


_EtsysLsnatRealServerMaxConns_Object = MibTableColumn
etsysLsnatRealServerMaxConns = _EtsysLsnatRealServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 5),
    _EtsysLsnatRealServerMaxConns_Type()
)
etsysLsnatRealServerMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerMaxConns.setStatus("current")


class _EtsysLsnatRealServerFailDetectType_Type(Integer32):
    """Custom type etsysLsnatRealServerFailDetectType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("probe", 2))
    )


_EtsysLsnatRealServerFailDetectType_Type.__name__ = "Integer32"
_EtsysLsnatRealServerFailDetectType_Object = MibTableColumn
etsysLsnatRealServerFailDetectType = _EtsysLsnatRealServerFailDetectType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 6),
    _EtsysLsnatRealServerFailDetectType_Type()
)
etsysLsnatRealServerFailDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerFailDetectType.setStatus("current")


class _EtsysLsnatRealServerFailDetectProbeOne_Type(SnmpAdminString):
    """Custom type etsysLsnatRealServerFailDetectProbeOne based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EtsysLsnatRealServerFailDetectProbeOne_Type.__name__ = "SnmpAdminString"
_EtsysLsnatRealServerFailDetectProbeOne_Object = MibTableColumn
etsysLsnatRealServerFailDetectProbeOne = _EtsysLsnatRealServerFailDetectProbeOne_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 7),
    _EtsysLsnatRealServerFailDetectProbeOne_Type()
)
etsysLsnatRealServerFailDetectProbeOne.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerFailDetectProbeOne.setStatus("current")


class _EtsysLsnatRealServerFailDetectProbeTwo_Type(SnmpAdminString):
    """Custom type etsysLsnatRealServerFailDetectProbeTwo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_EtsysLsnatRealServerFailDetectProbeTwo_Type.__name__ = "SnmpAdminString"
_EtsysLsnatRealServerFailDetectProbeTwo_Object = MibTableColumn
etsysLsnatRealServerFailDetectProbeTwo = _EtsysLsnatRealServerFailDetectProbeTwo_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 8),
    _EtsysLsnatRealServerFailDetectProbeTwo_Type()
)
etsysLsnatRealServerFailDetectProbeTwo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerFailDetectProbeTwo.setStatus("current")


class _EtsysLsnatRealServerAdminStatus_Type(Integer32):
    """Custom type etsysLsnatRealServerAdminStatus based on Integer32"""
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


_EtsysLsnatRealServerAdminStatus_Type.__name__ = "Integer32"
_EtsysLsnatRealServerAdminStatus_Object = MibTableColumn
etsysLsnatRealServerAdminStatus = _EtsysLsnatRealServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 9),
    _EtsysLsnatRealServerAdminStatus_Type()
)
etsysLsnatRealServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerAdminStatus.setStatus("current")


class _EtsysLsnatRealServerOperStatus_Type(Integer32):
    """Custom type etsysLsnatRealServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtsysLsnatRealServerOperStatus_Type.__name__ = "Integer32"
_EtsysLsnatRealServerOperStatus_Object = MibTableColumn
etsysLsnatRealServerOperStatus = _EtsysLsnatRealServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 10),
    _EtsysLsnatRealServerOperStatus_Type()
)
etsysLsnatRealServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatRealServerOperStatus.setStatus("current")
_EtsysLsnatRealServerConns_Type = Gauge32
_EtsysLsnatRealServerConns_Object = MibTableColumn
etsysLsnatRealServerConns = _EtsysLsnatRealServerConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 11),
    _EtsysLsnatRealServerConns_Type()
)
etsysLsnatRealServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatRealServerConns.setStatus("current")
_EtsysLsnatRealServerHits_Type = Counter32
_EtsysLsnatRealServerHits_Object = MibTableColumn
etsysLsnatRealServerHits = _EtsysLsnatRealServerHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 12),
    _EtsysLsnatRealServerHits_Type()
)
etsysLsnatRealServerHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatRealServerHits.setStatus("current")
_EtsysLsnatRealServerStateChanges_Type = Counter32
_EtsysLsnatRealServerStateChanges_Object = MibTableColumn
etsysLsnatRealServerStateChanges = _EtsysLsnatRealServerStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 13),
    _EtsysLsnatRealServerStateChanges_Type()
)
etsysLsnatRealServerStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatRealServerStateChanges.setStatus("current")
_EtsysLsnatRealServerLastStateChangeDateAndTime_Type = DateAndTime
_EtsysLsnatRealServerLastStateChangeDateAndTime_Object = MibTableColumn
etsysLsnatRealServerLastStateChangeDateAndTime = _EtsysLsnatRealServerLastStateChangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 14),
    _EtsysLsnatRealServerLastStateChangeDateAndTime_Type()
)
etsysLsnatRealServerLastStateChangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatRealServerLastStateChangeDateAndTime.setStatus("current")
_EtsysLsnatRealServerRowStatus_Type = RowStatus
_EtsysLsnatRealServerRowStatus_Object = MibTableColumn
etsysLsnatRealServerRowStatus = _EtsysLsnatRealServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 3, 1, 15),
    _EtsysLsnatRealServerRowStatus_Type()
)
etsysLsnatRealServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatRealServerRowStatus.setStatus("current")
_EtsysLsnatVserverTable_Object = MibTable
etsysLsnatVserverTable = _EtsysLsnatVserverTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4)
)
if mibBuilder.loadTexts:
    etsysLsnatVserverTable.setStatus("current")
_EtsysLsnatVserverEntry_Object = MibTableRow
etsysLsnatVserverEntry = _EtsysLsnatVserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1)
)
etsysLsnatVserverEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverInetVersion"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverName"),
)
if mibBuilder.loadTexts:
    etsysLsnatVserverEntry.setStatus("current")
_EtsysLsnatVserverInetVersion_Type = InetVersion
_EtsysLsnatVserverInetVersion_Object = MibTableColumn
etsysLsnatVserverInetVersion = _EtsysLsnatVserverInetVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 1),
    _EtsysLsnatVserverInetVersion_Type()
)
etsysLsnatVserverInetVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverInetVersion.setStatus("current")


class _EtsysLsnatVserverName_Type(SnmpAdminString):
    """Custom type etsysLsnatVserverName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysLsnatVserverName_Type.__name__ = "SnmpAdminString"
_EtsysLsnatVserverName_Object = MibTableColumn
etsysLsnatVserverName = _EtsysLsnatVserverName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 2),
    _EtsysLsnatVserverName_Type()
)
etsysLsnatVserverName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverName.setStatus("current")


class _EtsysLsnatVserverServerfarmName_Type(SnmpAdminString):
    """Custom type etsysLsnatVserverServerfarmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EtsysLsnatVserverServerfarmName_Type.__name__ = "SnmpAdminString"
_EtsysLsnatVserverServerfarmName_Object = MibTableColumn
etsysLsnatVserverServerfarmName = _EtsysLsnatVserverServerfarmName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 3),
    _EtsysLsnatVserverServerfarmName_Type()
)
etsysLsnatVserverServerfarmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverServerfarmName.setStatus("current")


class _EtsysLsnatVserverIdleTimeout_Type(Unsigned32):
    """Custom type etsysLsnatVserverIdleTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysLsnatVserverIdleTimeout_Object = MibTableColumn
etsysLsnatVserverIdleTimeout = _EtsysLsnatVserverIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 4),
    _EtsysLsnatVserverIdleTimeout_Type()
)
etsysLsnatVserverIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatVserverIdleTimeout.setUnits("seconds")


class _EtsysLsnatVserverStickyType_Type(Integer32):
    """Custom type etsysLsnatVserverStickyType based on Integer32"""
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
        *(("none", 1),
          ("sip", 2),
          ("sipDipDport", 3))
    )


_EtsysLsnatVserverStickyType_Type.__name__ = "Integer32"
_EtsysLsnatVserverStickyType_Object = MibTableColumn
etsysLsnatVserverStickyType = _EtsysLsnatVserverStickyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 5),
    _EtsysLsnatVserverStickyType_Type()
)
etsysLsnatVserverStickyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverStickyType.setStatus("current")


class _EtsysLsnatVserverStickyTimeout_Type(Unsigned32):
    """Custom type etsysLsnatVserverStickyTimeout based on Unsigned32"""
    defaultValue = 7200


_EtsysLsnatVserverStickyTimeout_Object = MibTableColumn
etsysLsnatVserverStickyTimeout = _EtsysLsnatVserverStickyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 6),
    _EtsysLsnatVserverStickyTimeout_Type()
)
etsysLsnatVserverStickyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverStickyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatVserverStickyTimeout.setUnits("seconds")


class _EtsysLsnatVserverUDPOneShot_Type(Integer32):
    """Custom type etsysLsnatVserverUDPOneShot based on Integer32"""
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


_EtsysLsnatVserverUDPOneShot_Type.__name__ = "Integer32"
_EtsysLsnatVserverUDPOneShot_Object = MibTableColumn
etsysLsnatVserverUDPOneShot = _EtsysLsnatVserverUDPOneShot_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 7),
    _EtsysLsnatVserverUDPOneShot_Type()
)
etsysLsnatVserverUDPOneShot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverUDPOneShot.setStatus("current")


class _EtsysLsnatVserverVrrpInterface_Type(InterfaceIndexOrZero):
    """Custom type etsysLsnatVserverVrrpInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_EtsysLsnatVserverVrrpInterface_Object = MibTableColumn
etsysLsnatVserverVrrpInterface = _EtsysLsnatVserverVrrpInterface_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 8),
    _EtsysLsnatVserverVrrpInterface_Type()
)
etsysLsnatVserverVrrpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverVrrpInterface.setStatus("current")


class _EtsysLsnatVserverVrrpVrid_Type(Unsigned32):
    """Custom type etsysLsnatVserverVrrpVrid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EtsysLsnatVserverVrrpVrid_Type.__name__ = "Unsigned32"
_EtsysLsnatVserverVrrpVrid_Object = MibTableColumn
etsysLsnatVserverVrrpVrid = _EtsysLsnatVserverVrrpVrid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 9),
    _EtsysLsnatVserverVrrpVrid_Type()
)
etsysLsnatVserverVrrpVrid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverVrrpVrid.setStatus("current")
_EtsysLsnatVserverSourceNatPoolName_Type = SnmpAdminString
_EtsysLsnatVserverSourceNatPoolName_Object = MibTableColumn
etsysLsnatVserverSourceNatPoolName = _EtsysLsnatVserverSourceNatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 10),
    _EtsysLsnatVserverSourceNatPoolName_Type()
)
etsysLsnatVserverSourceNatPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverSourceNatPoolName.setStatus("current")


class _EtsysLsnatVserverAdminStatus_Type(Integer32):
    """Custom type etsysLsnatVserverAdminStatus based on Integer32"""
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


_EtsysLsnatVserverAdminStatus_Type.__name__ = "Integer32"
_EtsysLsnatVserverAdminStatus_Object = MibTableColumn
etsysLsnatVserverAdminStatus = _EtsysLsnatVserverAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 11),
    _EtsysLsnatVserverAdminStatus_Type()
)
etsysLsnatVserverAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverAdminStatus.setStatus("current")


class _EtsysLsnatVserverOperStatus_Type(Integer32):
    """Custom type etsysLsnatVserverOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_EtsysLsnatVserverOperStatus_Type.__name__ = "Integer32"
_EtsysLsnatVserverOperStatus_Object = MibTableColumn
etsysLsnatVserverOperStatus = _EtsysLsnatVserverOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 12),
    _EtsysLsnatVserverOperStatus_Type()
)
etsysLsnatVserverOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverOperStatus.setStatus("current")


class _EtsysLsnatVserverLastStateChangeReason_Type(SnmpAdminString):
    """Custom type etsysLsnatVserverLastStateChangeReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EtsysLsnatVserverLastStateChangeReason_Type.__name__ = "SnmpAdminString"
_EtsysLsnatVserverLastStateChangeReason_Object = MibTableColumn
etsysLsnatVserverLastStateChangeReason = _EtsysLsnatVserverLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 13),
    _EtsysLsnatVserverLastStateChangeReason_Type()
)
etsysLsnatVserverLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverLastStateChangeReason.setStatus("current")
_EtsysLsnatVserverLastStateChangeDateAndTime_Type = DateAndTime
_EtsysLsnatVserverLastStateChangeDateAndTime_Object = MibTableColumn
etsysLsnatVserverLastStateChangeDateAndTime = _EtsysLsnatVserverLastStateChangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 14),
    _EtsysLsnatVserverLastStateChangeDateAndTime_Type()
)
etsysLsnatVserverLastStateChangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverLastStateChangeDateAndTime.setStatus("current")
_EtsysLsnatVserverConns_Type = Gauge32
_EtsysLsnatVserverConns_Object = MibTableColumn
etsysLsnatVserverConns = _EtsysLsnatVserverConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 15),
    _EtsysLsnatVserverConns_Type()
)
etsysLsnatVserverConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverConns.setStatus("current")
_EtsysLsnatVserverHits_Type = Counter32
_EtsysLsnatVserverHits_Object = MibTableColumn
etsysLsnatVserverHits = _EtsysLsnatVserverHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 16),
    _EtsysLsnatVserverHits_Type()
)
etsysLsnatVserverHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverHits.setStatus("current")
_EtsysLsnatVserverStateChanges_Type = Counter32
_EtsysLsnatVserverStateChanges_Object = MibTableColumn
etsysLsnatVserverStateChanges = _EtsysLsnatVserverStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 17),
    _EtsysLsnatVserverStateChanges_Type()
)
etsysLsnatVserverStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverStateChanges.setStatus("current")


class _EtsysLsnatVserverVirtualAddressStatus_Type(Integer32):
    """Custom type etsysLsnatVserverVirtualAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_EtsysLsnatVserverVirtualAddressStatus_Type.__name__ = "Integer32"
_EtsysLsnatVserverVirtualAddressStatus_Object = MibTableColumn
etsysLsnatVserverVirtualAddressStatus = _EtsysLsnatVserverVirtualAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 18),
    _EtsysLsnatVserverVirtualAddressStatus_Type()
)
etsysLsnatVserverVirtualAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressStatus.setStatus("current")
_EtsysLsnatVserverClientCount_Type = Counter32
_EtsysLsnatVserverClientCount_Object = MibTableColumn
etsysLsnatVserverClientCount = _EtsysLsnatVserverClientCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 19),
    _EtsysLsnatVserverClientCount_Type()
)
etsysLsnatVserverClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatVserverClientCount.setStatus("current")
_EtsysLsnatVserverRowStatus_Type = RowStatus
_EtsysLsnatVserverRowStatus_Object = MibTableColumn
etsysLsnatVserverRowStatus = _EtsysLsnatVserverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 20),
    _EtsysLsnatVserverRowStatus_Type()
)
etsysLsnatVserverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverRowStatus.setStatus("current")


class _EtsysLsnatVserverBindingMatchSourcePort_Type(Integer32):
    """Custom type etsysLsnatVserverBindingMatchSourcePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("exact", 1))
    )


_EtsysLsnatVserverBindingMatchSourcePort_Type.__name__ = "Integer32"
_EtsysLsnatVserverBindingMatchSourcePort_Object = MibTableColumn
etsysLsnatVserverBindingMatchSourcePort = _EtsysLsnatVserverBindingMatchSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 4, 1, 21),
    _EtsysLsnatVserverBindingMatchSourcePort_Type()
)
etsysLsnatVserverBindingMatchSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverBindingMatchSourcePort.setStatus("current")
_EtsysLsnatVserverVirtualAddressTable_Object = MibTable
etsysLsnatVserverVirtualAddressTable = _EtsysLsnatVserverVirtualAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5)
)
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressTable.setStatus("current")
_EtsysLsnatVserverVirtualAddressEntry_Object = MibTableRow
etsysLsnatVserverVirtualAddressEntry = _EtsysLsnatVserverVirtualAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1)
)
etsysLsnatVserverVirtualAddressEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressType"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverName"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressFirstIp"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressLastIp"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressProtocol"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressPort"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressServiceType"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressAllVrfs"),
)
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressEntry.setStatus("current")
_EtsysLsnatVserverVirtualAddressType_Type = InetAddressType
_EtsysLsnatVserverVirtualAddressType_Object = MibTableColumn
etsysLsnatVserverVirtualAddressType = _EtsysLsnatVserverVirtualAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 1),
    _EtsysLsnatVserverVirtualAddressType_Type()
)
etsysLsnatVserverVirtualAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressType.setStatus("current")
_EtsysLsnatVserverVirtualAddressFirstIp_Type = InetAddress
_EtsysLsnatVserverVirtualAddressFirstIp_Object = MibTableColumn
etsysLsnatVserverVirtualAddressFirstIp = _EtsysLsnatVserverVirtualAddressFirstIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 2),
    _EtsysLsnatVserverVirtualAddressFirstIp_Type()
)
etsysLsnatVserverVirtualAddressFirstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressFirstIp.setStatus("current")
_EtsysLsnatVserverVirtualAddressLastIp_Type = InetAddress
_EtsysLsnatVserverVirtualAddressLastIp_Object = MibTableColumn
etsysLsnatVserverVirtualAddressLastIp = _EtsysLsnatVserverVirtualAddressLastIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 3),
    _EtsysLsnatVserverVirtualAddressLastIp_Type()
)
etsysLsnatVserverVirtualAddressLastIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressLastIp.setStatus("current")


class _EtsysLsnatVserverVirtualAddressProtocol_Type(Integer32):
    """Custom type etsysLsnatVserverVirtualAddressProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_EtsysLsnatVserverVirtualAddressProtocol_Type.__name__ = "Integer32"
_EtsysLsnatVserverVirtualAddressProtocol_Object = MibTableColumn
etsysLsnatVserverVirtualAddressProtocol = _EtsysLsnatVserverVirtualAddressProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 4),
    _EtsysLsnatVserverVirtualAddressProtocol_Type()
)
etsysLsnatVserverVirtualAddressProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressProtocol.setStatus("current")


class _EtsysLsnatVserverVirtualAddressPort_Type(InetPortNumber):
    """Custom type etsysLsnatVserverVirtualAddressPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatVserverVirtualAddressPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatVserverVirtualAddressPort_Object = MibTableColumn
etsysLsnatVserverVirtualAddressPort = _EtsysLsnatVserverVirtualAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 5),
    _EtsysLsnatVserverVirtualAddressPort_Type()
)
etsysLsnatVserverVirtualAddressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressPort.setStatus("current")


class _EtsysLsnatVserverVirtualAddressServiceType_Type(Integer32):
    """Custom type etsysLsnatVserverVirtualAddressServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("none", 0),
          ("tftp", 2))
    )


_EtsysLsnatVserverVirtualAddressServiceType_Type.__name__ = "Integer32"
_EtsysLsnatVserverVirtualAddressServiceType_Object = MibTableColumn
etsysLsnatVserverVirtualAddressServiceType = _EtsysLsnatVserverVirtualAddressServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 6),
    _EtsysLsnatVserverVirtualAddressServiceType_Type()
)
etsysLsnatVserverVirtualAddressServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressServiceType.setStatus("current")


class _EtsysLsnatVserverVirtualAddressAllVrfs_Type(Integer32):
    """Custom type etsysLsnatVserverVirtualAddressAllVrfs based on Integer32"""
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


_EtsysLsnatVserverVirtualAddressAllVrfs_Type.__name__ = "Integer32"
_EtsysLsnatVserverVirtualAddressAllVrfs_Object = MibTableColumn
etsysLsnatVserverVirtualAddressAllVrfs = _EtsysLsnatVserverVirtualAddressAllVrfs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 7),
    _EtsysLsnatVserverVirtualAddressAllVrfs_Type()
)
etsysLsnatVserverVirtualAddressAllVrfs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressAllVrfs.setStatus("current")
_EtsysLsnatVserverVirtualAddressRowStatus_Type = RowStatus
_EtsysLsnatVserverVirtualAddressRowStatus_Object = MibTableColumn
etsysLsnatVserverVirtualAddressRowStatus = _EtsysLsnatVserverVirtualAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 5, 1, 8),
    _EtsysLsnatVserverVirtualAddressRowStatus_Type()
)
etsysLsnatVserverVirtualAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverVirtualAddressRowStatus.setStatus("current")
_EtsysLsnatVserverClientTable_Object = MibTable
etsysLsnatVserverClientTable = _EtsysLsnatVserverClientTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 6)
)
if mibBuilder.loadTexts:
    etsysLsnatVserverClientTable.setStatus("current")
_EtsysLsnatVserverClientEntry_Object = MibTableRow
etsysLsnatVserverClientEntry = _EtsysLsnatVserverClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 6, 1)
)
etsysLsnatVserverClientEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverClientAddressType"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverName"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverClientIp"),
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatVserverClientPrefixLen"),
)
if mibBuilder.loadTexts:
    etsysLsnatVserverClientEntry.setStatus("current")
_EtsysLsnatVserverClientAddressType_Type = InetAddressType
_EtsysLsnatVserverClientAddressType_Object = MibTableColumn
etsysLsnatVserverClientAddressType = _EtsysLsnatVserverClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 6, 1, 1),
    _EtsysLsnatVserverClientAddressType_Type()
)
etsysLsnatVserverClientAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverClientAddressType.setStatus("current")
_EtsysLsnatVserverClientIp_Type = InetAddress
_EtsysLsnatVserverClientIp_Object = MibTableColumn
etsysLsnatVserverClientIp = _EtsysLsnatVserverClientIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 6, 1, 2),
    _EtsysLsnatVserverClientIp_Type()
)
etsysLsnatVserverClientIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverClientIp.setStatus("current")
_EtsysLsnatVserverClientPrefixLen_Type = InetAddressPrefixLength
_EtsysLsnatVserverClientPrefixLen_Object = MibTableColumn
etsysLsnatVserverClientPrefixLen = _EtsysLsnatVserverClientPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 6, 1, 3),
    _EtsysLsnatVserverClientPrefixLen_Type()
)
etsysLsnatVserverClientPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatVserverClientPrefixLen.setStatus("current")
_EtsysLsnatVserverClientRowStatus_Type = RowStatus
_EtsysLsnatVserverClientRowStatus_Object = MibTableColumn
etsysLsnatVserverClientRowStatus = _EtsysLsnatVserverClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 6, 1, 4),
    _EtsysLsnatVserverClientRowStatus_Type()
)
etsysLsnatVserverClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysLsnatVserverClientRowStatus.setStatus("current")
_EtsysLsnatBindingTable_Object = MibTable
etsysLsnatBindingTable = _EtsysLsnatBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7)
)
if mibBuilder.loadTexts:
    etsysLsnatBindingTable.setStatus("current")
_EtsysLsnatBindingEntry_Object = MibTableRow
etsysLsnatBindingEntry = _EtsysLsnatBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1)
)
etsysLsnatBindingEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatBindingId"),
)
if mibBuilder.loadTexts:
    etsysLsnatBindingEntry.setStatus("current")
_EtsysLsnatBindingId_Type = Unsigned32
_EtsysLsnatBindingId_Object = MibTableColumn
etsysLsnatBindingId = _EtsysLsnatBindingId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 1),
    _EtsysLsnatBindingId_Type()
)
etsysLsnatBindingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatBindingId.setStatus("current")


class _EtsysLsnatBindingState_Type(Integer32):
    """Custom type etsysLsnatBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("established", 3),
          ("init", 1),
          ("syncing", 2))
    )


_EtsysLsnatBindingState_Type.__name__ = "Integer32"
_EtsysLsnatBindingState_Object = MibTableColumn
etsysLsnatBindingState = _EtsysLsnatBindingState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 2),
    _EtsysLsnatBindingState_Type()
)
etsysLsnatBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingState.setStatus("current")
_EtsysLsnatBindingAddressType_Type = InetAddressType
_EtsysLsnatBindingAddressType_Object = MibTableColumn
etsysLsnatBindingAddressType = _EtsysLsnatBindingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 3),
    _EtsysLsnatBindingAddressType_Type()
)
etsysLsnatBindingAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingAddressType.setStatus("current")
_EtsysLsnatBindingForwardSrcIp_Type = InetAddress
_EtsysLsnatBindingForwardSrcIp_Object = MibTableColumn
etsysLsnatBindingForwardSrcIp = _EtsysLsnatBindingForwardSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 4),
    _EtsysLsnatBindingForwardSrcIp_Type()
)
etsysLsnatBindingForwardSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingForwardSrcIp.setStatus("current")


class _EtsysLsnatBindingForwardSrcPort_Type(InetPortNumber):
    """Custom type etsysLsnatBindingForwardSrcPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatBindingForwardSrcPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatBindingForwardSrcPort_Object = MibTableColumn
etsysLsnatBindingForwardSrcPort = _EtsysLsnatBindingForwardSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 5),
    _EtsysLsnatBindingForwardSrcPort_Type()
)
etsysLsnatBindingForwardSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingForwardSrcPort.setStatus("current")
_EtsysLsnatBindingForwardDstIp_Type = InetAddress
_EtsysLsnatBindingForwardDstIp_Object = MibTableColumn
etsysLsnatBindingForwardDstIp = _EtsysLsnatBindingForwardDstIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 6),
    _EtsysLsnatBindingForwardDstIp_Type()
)
etsysLsnatBindingForwardDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingForwardDstIp.setStatus("current")


class _EtsysLsnatBindingForwardDstPort_Type(InetPortNumber):
    """Custom type etsysLsnatBindingForwardDstPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatBindingForwardDstPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatBindingForwardDstPort_Object = MibTableColumn
etsysLsnatBindingForwardDstPort = _EtsysLsnatBindingForwardDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 7),
    _EtsysLsnatBindingForwardDstPort_Type()
)
etsysLsnatBindingForwardDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingForwardDstPort.setStatus("current")
_EtsysLsnatBindingReverseSrcIp_Type = InetAddress
_EtsysLsnatBindingReverseSrcIp_Object = MibTableColumn
etsysLsnatBindingReverseSrcIp = _EtsysLsnatBindingReverseSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 8),
    _EtsysLsnatBindingReverseSrcIp_Type()
)
etsysLsnatBindingReverseSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingReverseSrcIp.setStatus("current")


class _EtsysLsnatBindingReverseSrcPort_Type(InetPortNumber):
    """Custom type etsysLsnatBindingReverseSrcPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatBindingReverseSrcPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatBindingReverseSrcPort_Object = MibTableColumn
etsysLsnatBindingReverseSrcPort = _EtsysLsnatBindingReverseSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 9),
    _EtsysLsnatBindingReverseSrcPort_Type()
)
etsysLsnatBindingReverseSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingReverseSrcPort.setStatus("current")
_EtsysLsnatBindingReverseDstIp_Type = InetAddress
_EtsysLsnatBindingReverseDstIp_Object = MibTableColumn
etsysLsnatBindingReverseDstIp = _EtsysLsnatBindingReverseDstIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 10),
    _EtsysLsnatBindingReverseDstIp_Type()
)
etsysLsnatBindingReverseDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingReverseDstIp.setStatus("current")


class _EtsysLsnatBindingReverseDstPort_Type(InetPortNumber):
    """Custom type etsysLsnatBindingReverseDstPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatBindingReverseDstPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatBindingReverseDstPort_Object = MibTableColumn
etsysLsnatBindingReverseDstPort = _EtsysLsnatBindingReverseDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 11),
    _EtsysLsnatBindingReverseDstPort_Type()
)
etsysLsnatBindingReverseDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingReverseDstPort.setStatus("current")


class _EtsysLsnatBindingProtocol_Type(Integer32):
    """Custom type etsysLsnatBindingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_EtsysLsnatBindingProtocol_Type.__name__ = "Integer32"
_EtsysLsnatBindingProtocol_Object = MibTableColumn
etsysLsnatBindingProtocol = _EtsysLsnatBindingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 12),
    _EtsysLsnatBindingProtocol_Type()
)
etsysLsnatBindingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingProtocol.setStatus("current")


class _EtsysLsnatBindingAlgType_Type(Integer32):
    """Custom type etsysLsnatBindingAlgType based on Integer32"""
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
        *(("ftpctrl", 2),
          ("ftpdata", 3),
          ("none", 1),
          ("tftpctrl", 4))
    )


_EtsysLsnatBindingAlgType_Type.__name__ = "Integer32"
_EtsysLsnatBindingAlgType_Object = MibTableColumn
etsysLsnatBindingAlgType = _EtsysLsnatBindingAlgType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 13),
    _EtsysLsnatBindingAlgType_Type()
)
etsysLsnatBindingAlgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingAlgType.setStatus("current")
_EtsysLsnatBindingFtpDataBindingCount_Type = Unsigned32
_EtsysLsnatBindingFtpDataBindingCount_Object = MibTableColumn
etsysLsnatBindingFtpDataBindingCount = _EtsysLsnatBindingFtpDataBindingCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 14),
    _EtsysLsnatBindingFtpDataBindingCount_Type()
)
etsysLsnatBindingFtpDataBindingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingFtpDataBindingCount.setStatus("current")


class _EtsysLsnatBindingSticky_Type(Integer32):
    """Custom type etsysLsnatBindingSticky based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EtsysLsnatBindingSticky_Type.__name__ = "Integer32"
_EtsysLsnatBindingSticky_Object = MibTableColumn
etsysLsnatBindingSticky = _EtsysLsnatBindingSticky_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 15),
    _EtsysLsnatBindingSticky_Type()
)
etsysLsnatBindingSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingSticky.setStatus("current")
_EtsysLsnatBindingHWConns_Type = Gauge32
_EtsysLsnatBindingHWConns_Object = MibTableColumn
etsysLsnatBindingHWConns = _EtsysLsnatBindingHWConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 16),
    _EtsysLsnatBindingHWConns_Type()
)
etsysLsnatBindingHWConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingHWConns.setStatus("current")


class _EtsysLsnatBindingVserverName_Type(SnmpAdminString):
    """Custom type etsysLsnatBindingVserverName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysLsnatBindingVserverName_Type.__name__ = "SnmpAdminString"
_EtsysLsnatBindingVserverName_Object = MibTableColumn
etsysLsnatBindingVserverName = _EtsysLsnatBindingVserverName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 17),
    _EtsysLsnatBindingVserverName_Type()
)
etsysLsnatBindingVserverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingVserverName.setStatus("current")


class _EtsysLsnatBindingServerfarmName_Type(SnmpAdminString):
    """Custom type etsysLsnatBindingServerfarmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysLsnatBindingServerfarmName_Type.__name__ = "SnmpAdminString"
_EtsysLsnatBindingServerfarmName_Object = MibTableColumn
etsysLsnatBindingServerfarmName = _EtsysLsnatBindingServerfarmName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 18),
    _EtsysLsnatBindingServerfarmName_Type()
)
etsysLsnatBindingServerfarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingServerfarmName.setStatus("current")
_EtsysLsnatBindingRealIp_Type = InetAddress
_EtsysLsnatBindingRealIp_Object = MibTableColumn
etsysLsnatBindingRealIp = _EtsysLsnatBindingRealIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 19),
    _EtsysLsnatBindingRealIp_Type()
)
etsysLsnatBindingRealIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingRealIp.setStatus("current")


class _EtsysLsnatBindingRealPort_Type(InetPortNumber):
    """Custom type etsysLsnatBindingRealPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatBindingRealPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatBindingRealPort_Object = MibTableColumn
etsysLsnatBindingRealPort = _EtsysLsnatBindingRealPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 20),
    _EtsysLsnatBindingRealPort_Type()
)
etsysLsnatBindingRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingRealPort.setStatus("current")
_EtsysLsnatBindingCreationDate_Type = DateAndTime
_EtsysLsnatBindingCreationDate_Object = MibTableColumn
etsysLsnatBindingCreationDate = _EtsysLsnatBindingCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 21),
    _EtsysLsnatBindingCreationDate_Type()
)
etsysLsnatBindingCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingCreationDate.setStatus("current")
_EtsysLsnatBindingExpirationDate_Type = DateAndTime
_EtsysLsnatBindingExpirationDate_Object = MibTableColumn
etsysLsnatBindingExpirationDate = _EtsysLsnatBindingExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 22),
    _EtsysLsnatBindingExpirationDate_Type()
)
etsysLsnatBindingExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingExpirationDate.setStatus("current")
_EtsysLsnatBindingIdleTime_Type = Unsigned32
_EtsysLsnatBindingIdleTime_Object = MibTableColumn
etsysLsnatBindingIdleTime = _EtsysLsnatBindingIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 23),
    _EtsysLsnatBindingIdleTime_Type()
)
etsysLsnatBindingIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatBindingIdleTime.setUnits("seconds")
_EtsysLsnatBindingExpireTime_Type = Unsigned32
_EtsysLsnatBindingExpireTime_Object = MibTableColumn
etsysLsnatBindingExpireTime = _EtsysLsnatBindingExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 24),
    _EtsysLsnatBindingExpireTime_Type()
)
etsysLsnatBindingExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatBindingExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatBindingExpireTime.setUnits("seconds")


class _EtsysLsnatBindingClear_Type(TruthValue):
    """Custom type etsysLsnatBindingClear based on TruthValue"""


_EtsysLsnatBindingClear_Object = MibTableColumn
etsysLsnatBindingClear = _EtsysLsnatBindingClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 7, 1, 25),
    _EtsysLsnatBindingClear_Type()
)
etsysLsnatBindingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatBindingClear.setStatus("current")
_EtsysLsnatStickyTable_Object = MibTable
etsysLsnatStickyTable = _EtsysLsnatStickyTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8)
)
if mibBuilder.loadTexts:
    etsysLsnatStickyTable.setStatus("current")
_EtsysLsnatStickyEntry_Object = MibTableRow
etsysLsnatStickyEntry = _EtsysLsnatStickyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1)
)
etsysLsnatStickyEntry.setIndexNames(
    (0, "ENTERASYS-LSNAT-MIB", "etsysLsnatStickyId"),
)
if mibBuilder.loadTexts:
    etsysLsnatStickyEntry.setStatus("current")
_EtsysLsnatStickyId_Type = Unsigned32
_EtsysLsnatStickyId_Object = MibTableColumn
etsysLsnatStickyId = _EtsysLsnatStickyId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 1),
    _EtsysLsnatStickyId_Type()
)
etsysLsnatStickyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysLsnatStickyId.setStatus("current")


class _EtsysLsnatStickyType_Type(Integer32):
    """Custom type etsysLsnatStickyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("sipDipDport", 2))
    )


_EtsysLsnatStickyType_Type.__name__ = "Integer32"
_EtsysLsnatStickyType_Object = MibTableColumn
etsysLsnatStickyType = _EtsysLsnatStickyType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 2),
    _EtsysLsnatStickyType_Type()
)
etsysLsnatStickyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyType.setStatus("current")
_EtsysLsnatStickyAddressType_Type = InetAddressType
_EtsysLsnatStickyAddressType_Object = MibTableColumn
etsysLsnatStickyAddressType = _EtsysLsnatStickyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 3),
    _EtsysLsnatStickyAddressType_Type()
)
etsysLsnatStickyAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyAddressType.setStatus("current")
_EtsysLsnatStickySrcIp_Type = InetAddress
_EtsysLsnatStickySrcIp_Object = MibTableColumn
etsysLsnatStickySrcIp = _EtsysLsnatStickySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 4),
    _EtsysLsnatStickySrcIp_Type()
)
etsysLsnatStickySrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickySrcIp.setStatus("current")
_EtsysLsnatStickyDstIp_Type = InetAddress
_EtsysLsnatStickyDstIp_Object = MibTableColumn
etsysLsnatStickyDstIp = _EtsysLsnatStickyDstIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 5),
    _EtsysLsnatStickyDstIp_Type()
)
etsysLsnatStickyDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyDstIp.setStatus("current")


class _EtsysLsnatStickyDstPort_Type(InetPortNumber):
    """Custom type etsysLsnatStickyDstPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatStickyDstPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatStickyDstPort_Object = MibTableColumn
etsysLsnatStickyDstPort = _EtsysLsnatStickyDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 6),
    _EtsysLsnatStickyDstPort_Type()
)
etsysLsnatStickyDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyDstPort.setStatus("current")
_EtsysLsnatStickyHits_Type = Counter32
_EtsysLsnatStickyHits_Object = MibTableColumn
etsysLsnatStickyHits = _EtsysLsnatStickyHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 7),
    _EtsysLsnatStickyHits_Type()
)
etsysLsnatStickyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyHits.setStatus("current")
_EtsysLsnatStickyBindings_Type = Counter32
_EtsysLsnatStickyBindings_Object = MibTableColumn
etsysLsnatStickyBindings = _EtsysLsnatStickyBindings_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 8),
    _EtsysLsnatStickyBindings_Type()
)
etsysLsnatStickyBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyBindings.setStatus("current")


class _EtsysLsnatStickyVserverName_Type(SnmpAdminString):
    """Custom type etsysLsnatStickyVserverName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysLsnatStickyVserverName_Type.__name__ = "SnmpAdminString"
_EtsysLsnatStickyVserverName_Object = MibTableColumn
etsysLsnatStickyVserverName = _EtsysLsnatStickyVserverName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 9),
    _EtsysLsnatStickyVserverName_Type()
)
etsysLsnatStickyVserverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyVserverName.setStatus("current")


class _EtsysLsnatStickyServerfarmName_Type(SnmpAdminString):
    """Custom type etsysLsnatStickyServerfarmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysLsnatStickyServerfarmName_Type.__name__ = "SnmpAdminString"
_EtsysLsnatStickyServerfarmName_Object = MibTableColumn
etsysLsnatStickyServerfarmName = _EtsysLsnatStickyServerfarmName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 10),
    _EtsysLsnatStickyServerfarmName_Type()
)
etsysLsnatStickyServerfarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyServerfarmName.setStatus("current")
_EtsysLsnatStickyRealIp_Type = InetAddress
_EtsysLsnatStickyRealIp_Object = MibTableColumn
etsysLsnatStickyRealIp = _EtsysLsnatStickyRealIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 11),
    _EtsysLsnatStickyRealIp_Type()
)
etsysLsnatStickyRealIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyRealIp.setStatus("current")


class _EtsysLsnatStickyRealPort_Type(InetPortNumber):
    """Custom type etsysLsnatStickyRealPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysLsnatStickyRealPort_Type.__name__ = "InetPortNumber"
_EtsysLsnatStickyRealPort_Object = MibTableColumn
etsysLsnatStickyRealPort = _EtsysLsnatStickyRealPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 12),
    _EtsysLsnatStickyRealPort_Type()
)
etsysLsnatStickyRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyRealPort.setStatus("current")
_EtsysLsnatStickyCreationDate_Type = DateAndTime
_EtsysLsnatStickyCreationDate_Object = MibTableColumn
etsysLsnatStickyCreationDate = _EtsysLsnatStickyCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 13),
    _EtsysLsnatStickyCreationDate_Type()
)
etsysLsnatStickyCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyCreationDate.setStatus("current")
_EtsysLsnatStickyExpirationDate_Type = DateAndTime
_EtsysLsnatStickyExpirationDate_Object = MibTableColumn
etsysLsnatStickyExpirationDate = _EtsysLsnatStickyExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 14),
    _EtsysLsnatStickyExpirationDate_Type()
)
etsysLsnatStickyExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyExpirationDate.setStatus("current")
_EtsysLsnatStickyIdleTime_Type = Unsigned32
_EtsysLsnatStickyIdleTime_Object = MibTableColumn
etsysLsnatStickyIdleTime = _EtsysLsnatStickyIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 15),
    _EtsysLsnatStickyIdleTime_Type()
)
etsysLsnatStickyIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatStickyIdleTime.setUnits("seconds")
_EtsysLsnatStickyExpireTime_Type = Unsigned32
_EtsysLsnatStickyExpireTime_Object = MibTableColumn
etsysLsnatStickyExpireTime = _EtsysLsnatStickyExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 16),
    _EtsysLsnatStickyExpireTime_Type()
)
etsysLsnatStickyExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLsnatStickyExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysLsnatStickyExpireTime.setUnits("seconds")


class _EtsysLsnatStickyClear_Type(TruthValue):
    """Custom type etsysLsnatStickyClear based on TruthValue"""


_EtsysLsnatStickyClear_Object = MibTableColumn
etsysLsnatStickyClear = _EtsysLsnatStickyClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 2, 8, 1, 17),
    _EtsysLsnatStickyClear_Type()
)
etsysLsnatStickyClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLsnatStickyClear.setStatus("current")
_EtsysLsnatConformance_ObjectIdentity = ObjectIdentity
etsysLsnatConformance = _EtsysLsnatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3)
)
_EtsysLsnatMIBGroups_ObjectIdentity = ObjectIdentity
etsysLsnatMIBGroups = _EtsysLsnatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1)
)
_EtsysLsnatMIBCompliances_ObjectIdentity = ObjectIdentity
etsysLsnatMIBCompliances = _EtsysLsnatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 2)
)

# Managed Objects groups

etsysLsnatMIBGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 1)
)
etsysLsnatMIBGlobalStatsGroup.setObjects(
      *(("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsRealsUsed"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsServerfarmsUsed"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsVserversUsed"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsVserversIPsUsed"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsCurrent"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsHigh"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsDeleted"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsTotal"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsExhausted"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsNoReals"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsNoPortmapPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsNoFtpALG"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsBindingsPerSecond"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsVserverActive"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsVserverHigh"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsServerfarmActive"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsServerfarmHigh"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsRealActive"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsRealHigh"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsStickyEntriesTotal"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsStickyBindingsStuckTotal"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsStickyBindingsStuckCurrent"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsStickyActiveEntries"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsStickyActiveEntriesHigh"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsStickyEntriesExhausted"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsClear"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStatsClearDateAndTime"))
)
if mibBuilder.loadTexts:
    etsysLsnatMIBGlobalStatsGroup.setStatus("current")

etsysLsnatMIBGlobalIpv4ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 2)
)
etsysLsnatMIBGlobalIpv4ConfigGroup.setObjects(
      *(("ENTERASYS-LSNAT-MIB", "etsysLsnatIpv4ConfigFTPCtrlPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatIpv4ConfigTFTPCtrlPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatIpv4ConfigRealServerAccess"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatIpv4ConfigFinRstTimeout"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus"))
)
if mibBuilder.loadTexts:
    etsysLsnatMIBGlobalIpv4ConfigGroup.setStatus("current")

etsysLsnatMIBRealServerAccessClientTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 3)
)
etsysLsnatMIBRealServerAccessClientTableGroup.setObjects(
    ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerAccessClientRowStatus")
)
if mibBuilder.loadTexts:
    etsysLsnatMIBRealServerAccessClientTableGroup.setStatus("current")

etsysLsnatMIBServerfarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 4)
)
etsysLsnatMIBServerfarmTableGroup.setObjects(
      *(("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmPredictor"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmAdminStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmOperStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmConns"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmHits"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmStateChanges"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmLastStateChangeDateAndTime"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmRealsCfg"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmRealsUp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmVserversCfg"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatServerfarmRowStatus"))
)
if mibBuilder.loadTexts:
    etsysLsnatMIBServerfarmTableGroup.setStatus("current")

etsysLsnatMIBRealServerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 5)
)
etsysLsnatMIBRealServerTableGroup.setObjects(
      *(("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerWeight"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerMaxConns"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerFailDetectType"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerFailDetectProbeOne"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerFailDetectProbeTwo"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerAdminStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerOperStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerConns"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerHits"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerStateChanges"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerLastStateChangeDateAndTime"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatRealServerRowStatus"))
)
if mibBuilder.loadTexts:
    etsysLsnatMIBRealServerTableGroup.setStatus("current")

etsysLsnatMIBVserverTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 6)
)
etsysLsnatMIBVserverTableGroup.setObjects(
      *(("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverServerfarmName"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverIdleTimeout"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverStickyType"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverStickyTimeout"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverUDPOneShot"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVrrpInterface"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVrrpVrid"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverSourceNatPoolName"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverAdminStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverOperStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverLastStateChangeReason"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverLastStateChangeDateAndTime"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverConns"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverHits"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverStateChanges"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverClientCount"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverRowStatus"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverBindingMatchSourcePort"))
)
if mibBuilder.loadTexts:
    etsysLsnatMIBVserverTableGroup.setStatus("current")

etsysLsnatMIBVserverVirtualAddressTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 7)
)
etsysLsnatMIBVserverVirtualAddressTableGroup.setObjects(
    ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverVirtualAddressRowStatus")
)
if mibBuilder.loadTexts:
    etsysLsnatMIBVserverVirtualAddressTableGroup.setStatus("current")

etsysLsnatMIBVserverClientTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 8)
)
etsysLsnatMIBVserverClientTableGroup.setObjects(
    ("ENTERASYS-LSNAT-MIB", "etsysLsnatVserverClientRowStatus")
)
if mibBuilder.loadTexts:
    etsysLsnatMIBVserverClientTableGroup.setStatus("current")

etsysLsnatMIBBindingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 9)
)
etsysLsnatMIBBindingTableGroup.setObjects(
      *(("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingState"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingAddressType"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingForwardSrcIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingForwardSrcPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingForwardDstIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingForwardDstPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingReverseSrcIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingReverseSrcPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingReverseDstIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingReverseDstPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingProtocol"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingAlgType"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingFtpDataBindingCount"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingSticky"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingHWConns"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingVserverName"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingServerfarmName"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingRealIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingRealPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingCreationDate"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingExpirationDate"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingIdleTime"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingExpireTime"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatBindingClear"))
)
if mibBuilder.loadTexts:
    etsysLsnatMIBBindingTableGroup.setStatus("current")

etsysLsnatMIBStickyTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 1, 10)
)
etsysLsnatMIBStickyTableGroup.setObjects(
      *(("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyType"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyAddressType"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickySrcIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyDstIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyDstPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyHits"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyBindings"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyVserverName"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyServerfarmName"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyRealIp"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyRealPort"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyCreationDate"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyExpirationDate"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyIdleTime"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyExpireTime"),
        ("ENTERASYS-LSNAT-MIB", "etsysLsnatStickyClear"))
)
if mibBuilder.loadTexts:
    etsysLsnatMIBStickyTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysLsnatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 74, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etsysLsnatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-LSNAT-MIB",
    **{"etsysLsnatMIB": etsysLsnatMIB,
       "etsysLsnatGlobal": etsysLsnatGlobal,
       "etsysLsnatGlobalStats": etsysLsnatGlobalStats,
       "etsysLsnatStatsRealsUsed": etsysLsnatStatsRealsUsed,
       "etsysLsnatStatsServerfarmsUsed": etsysLsnatStatsServerfarmsUsed,
       "etsysLsnatStatsVserversUsed": etsysLsnatStatsVserversUsed,
       "etsysLsnatStatsVserversIPsUsed": etsysLsnatStatsVserversIPsUsed,
       "etsysLsnatStatsBindingsCurrent": etsysLsnatStatsBindingsCurrent,
       "etsysLsnatStatsBindingsHigh": etsysLsnatStatsBindingsHigh,
       "etsysLsnatStatsBindingsDeleted": etsysLsnatStatsBindingsDeleted,
       "etsysLsnatStatsBindingsTotal": etsysLsnatStatsBindingsTotal,
       "etsysLsnatStatsBindingsExhausted": etsysLsnatStatsBindingsExhausted,
       "etsysLsnatStatsBindingsNoReals": etsysLsnatStatsBindingsNoReals,
       "etsysLsnatStatsBindingsNoPortmapPort": etsysLsnatStatsBindingsNoPortmapPort,
       "etsysLsnatStatsBindingsNoFtpALG": etsysLsnatStatsBindingsNoFtpALG,
       "etsysLsnatStatsBindingsPerSecond": etsysLsnatStatsBindingsPerSecond,
       "etsysLsnatStatsVserverActive": etsysLsnatStatsVserverActive,
       "etsysLsnatStatsVserverHigh": etsysLsnatStatsVserverHigh,
       "etsysLsnatStatsServerfarmActive": etsysLsnatStatsServerfarmActive,
       "etsysLsnatStatsServerfarmHigh": etsysLsnatStatsServerfarmHigh,
       "etsysLsnatStatsRealActive": etsysLsnatStatsRealActive,
       "etsysLsnatStatsRealHigh": etsysLsnatStatsRealHigh,
       "etsysLsnatStatsStickyEntriesTotal": etsysLsnatStatsStickyEntriesTotal,
       "etsysLsnatStatsStickyBindingsStuckTotal": etsysLsnatStatsStickyBindingsStuckTotal,
       "etsysLsnatStatsStickyBindingsStuckCurrent": etsysLsnatStatsStickyBindingsStuckCurrent,
       "etsysLsnatStatsStickyActiveEntries": etsysLsnatStatsStickyActiveEntries,
       "etsysLsnatStatsStickyActiveEntriesHigh": etsysLsnatStatsStickyActiveEntriesHigh,
       "etsysLsnatStatsStickyEntriesExhausted": etsysLsnatStatsStickyEntriesExhausted,
       "etsysLsnatStatsClear": etsysLsnatStatsClear,
       "etsysLsnatStatsClearDateAndTime": etsysLsnatStatsClearDateAndTime,
       "etsysLsnatStatsRealServerAccessClientsCount": etsysLsnatStatsRealServerAccessClientsCount,
       "etsysLsnatStatsMinTimeoutValue": etsysLsnatStatsMinTimeoutValue,
       "etsysLsnatStatsMaxTimeoutValue": etsysLsnatStatsMaxTimeoutValue,
       "etsysLsnatGlobalIpv4Config": etsysLsnatGlobalIpv4Config,
       "etsysLsnatIpv4ConfigFTPCtrlPort": etsysLsnatIpv4ConfigFTPCtrlPort,
       "etsysLsnatIpv4ConfigTFTPCtrlPort": etsysLsnatIpv4ConfigTFTPCtrlPort,
       "etsysLsnatIpv4ConfigRealServerAccess": etsysLsnatIpv4ConfigRealServerAccess,
       "etsysLsnatIpv4ConfigFinRstTimeout": etsysLsnatIpv4ConfigFinRstTimeout,
       "etsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus": etsysLsnatIpv4ConfigFinRstTimeoutHalfClosedStatus,
       "etsysLsnatTables": etsysLsnatTables,
       "etsysLsnatRealServerAccessClientTable": etsysLsnatRealServerAccessClientTable,
       "etsysLsnatRealServerAccessClientEntry": etsysLsnatRealServerAccessClientEntry,
       "etsysLsnatRealServerAccessClientAddressType": etsysLsnatRealServerAccessClientAddressType,
       "etsysLsnatRealServerAccessClientIp": etsysLsnatRealServerAccessClientIp,
       "etsysLsnatRealServerAccessClientPrefixLen": etsysLsnatRealServerAccessClientPrefixLen,
       "etsysLsnatRealServerAccessClientRowStatus": etsysLsnatRealServerAccessClientRowStatus,
       "etsysLsnatServerfarmTable": etsysLsnatServerfarmTable,
       "etsysLsnatServerfarmEntry": etsysLsnatServerfarmEntry,
       "etsysLsnatServerfarmInetVersion": etsysLsnatServerfarmInetVersion,
       "etsysLsnatServerfarmName": etsysLsnatServerfarmName,
       "etsysLsnatServerfarmPredictor": etsysLsnatServerfarmPredictor,
       "etsysLsnatServerfarmAdminStatus": etsysLsnatServerfarmAdminStatus,
       "etsysLsnatServerfarmOperStatus": etsysLsnatServerfarmOperStatus,
       "etsysLsnatServerfarmConns": etsysLsnatServerfarmConns,
       "etsysLsnatServerfarmHits": etsysLsnatServerfarmHits,
       "etsysLsnatServerfarmStateChanges": etsysLsnatServerfarmStateChanges,
       "etsysLsnatServerfarmLastStateChangeDateAndTime": etsysLsnatServerfarmLastStateChangeDateAndTime,
       "etsysLsnatServerfarmRealsCfg": etsysLsnatServerfarmRealsCfg,
       "etsysLsnatServerfarmRealsUp": etsysLsnatServerfarmRealsUp,
       "etsysLsnatServerfarmVserversCfg": etsysLsnatServerfarmVserversCfg,
       "etsysLsnatServerfarmRowStatus": etsysLsnatServerfarmRowStatus,
       "etsysLsnatRealServerTable": etsysLsnatRealServerTable,
       "etsysLsnatRealServerEntry": etsysLsnatRealServerEntry,
       "etsysLsnatRealServerAddressType": etsysLsnatRealServerAddressType,
       "etsysLsnatRealServerIp": etsysLsnatRealServerIp,
       "etsysLsnatRealServerPort": etsysLsnatRealServerPort,
       "etsysLsnatRealServerWeight": etsysLsnatRealServerWeight,
       "etsysLsnatRealServerMaxConns": etsysLsnatRealServerMaxConns,
       "etsysLsnatRealServerFailDetectType": etsysLsnatRealServerFailDetectType,
       "etsysLsnatRealServerFailDetectProbeOne": etsysLsnatRealServerFailDetectProbeOne,
       "etsysLsnatRealServerFailDetectProbeTwo": etsysLsnatRealServerFailDetectProbeTwo,
       "etsysLsnatRealServerAdminStatus": etsysLsnatRealServerAdminStatus,
       "etsysLsnatRealServerOperStatus": etsysLsnatRealServerOperStatus,
       "etsysLsnatRealServerConns": etsysLsnatRealServerConns,
       "etsysLsnatRealServerHits": etsysLsnatRealServerHits,
       "etsysLsnatRealServerStateChanges": etsysLsnatRealServerStateChanges,
       "etsysLsnatRealServerLastStateChangeDateAndTime": etsysLsnatRealServerLastStateChangeDateAndTime,
       "etsysLsnatRealServerRowStatus": etsysLsnatRealServerRowStatus,
       "etsysLsnatVserverTable": etsysLsnatVserverTable,
       "etsysLsnatVserverEntry": etsysLsnatVserverEntry,
       "etsysLsnatVserverInetVersion": etsysLsnatVserverInetVersion,
       "etsysLsnatVserverName": etsysLsnatVserverName,
       "etsysLsnatVserverServerfarmName": etsysLsnatVserverServerfarmName,
       "etsysLsnatVserverIdleTimeout": etsysLsnatVserverIdleTimeout,
       "etsysLsnatVserverStickyType": etsysLsnatVserverStickyType,
       "etsysLsnatVserverStickyTimeout": etsysLsnatVserverStickyTimeout,
       "etsysLsnatVserverUDPOneShot": etsysLsnatVserverUDPOneShot,
       "etsysLsnatVserverVrrpInterface": etsysLsnatVserverVrrpInterface,
       "etsysLsnatVserverVrrpVrid": etsysLsnatVserverVrrpVrid,
       "etsysLsnatVserverSourceNatPoolName": etsysLsnatVserverSourceNatPoolName,
       "etsysLsnatVserverAdminStatus": etsysLsnatVserverAdminStatus,
       "etsysLsnatVserverOperStatus": etsysLsnatVserverOperStatus,
       "etsysLsnatVserverLastStateChangeReason": etsysLsnatVserverLastStateChangeReason,
       "etsysLsnatVserverLastStateChangeDateAndTime": etsysLsnatVserverLastStateChangeDateAndTime,
       "etsysLsnatVserverConns": etsysLsnatVserverConns,
       "etsysLsnatVserverHits": etsysLsnatVserverHits,
       "etsysLsnatVserverStateChanges": etsysLsnatVserverStateChanges,
       "etsysLsnatVserverVirtualAddressStatus": etsysLsnatVserverVirtualAddressStatus,
       "etsysLsnatVserverClientCount": etsysLsnatVserverClientCount,
       "etsysLsnatVserverRowStatus": etsysLsnatVserverRowStatus,
       "etsysLsnatVserverBindingMatchSourcePort": etsysLsnatVserverBindingMatchSourcePort,
       "etsysLsnatVserverVirtualAddressTable": etsysLsnatVserverVirtualAddressTable,
       "etsysLsnatVserverVirtualAddressEntry": etsysLsnatVserverVirtualAddressEntry,
       "etsysLsnatVserverVirtualAddressType": etsysLsnatVserverVirtualAddressType,
       "etsysLsnatVserverVirtualAddressFirstIp": etsysLsnatVserverVirtualAddressFirstIp,
       "etsysLsnatVserverVirtualAddressLastIp": etsysLsnatVserverVirtualAddressLastIp,
       "etsysLsnatVserverVirtualAddressProtocol": etsysLsnatVserverVirtualAddressProtocol,
       "etsysLsnatVserverVirtualAddressPort": etsysLsnatVserverVirtualAddressPort,
       "etsysLsnatVserverVirtualAddressServiceType": etsysLsnatVserverVirtualAddressServiceType,
       "etsysLsnatVserverVirtualAddressAllVrfs": etsysLsnatVserverVirtualAddressAllVrfs,
       "etsysLsnatVserverVirtualAddressRowStatus": etsysLsnatVserverVirtualAddressRowStatus,
       "etsysLsnatVserverClientTable": etsysLsnatVserverClientTable,
       "etsysLsnatVserverClientEntry": etsysLsnatVserverClientEntry,
       "etsysLsnatVserverClientAddressType": etsysLsnatVserverClientAddressType,
       "etsysLsnatVserverClientIp": etsysLsnatVserverClientIp,
       "etsysLsnatVserverClientPrefixLen": etsysLsnatVserverClientPrefixLen,
       "etsysLsnatVserverClientRowStatus": etsysLsnatVserverClientRowStatus,
       "etsysLsnatBindingTable": etsysLsnatBindingTable,
       "etsysLsnatBindingEntry": etsysLsnatBindingEntry,
       "etsysLsnatBindingId": etsysLsnatBindingId,
       "etsysLsnatBindingState": etsysLsnatBindingState,
       "etsysLsnatBindingAddressType": etsysLsnatBindingAddressType,
       "etsysLsnatBindingForwardSrcIp": etsysLsnatBindingForwardSrcIp,
       "etsysLsnatBindingForwardSrcPort": etsysLsnatBindingForwardSrcPort,
       "etsysLsnatBindingForwardDstIp": etsysLsnatBindingForwardDstIp,
       "etsysLsnatBindingForwardDstPort": etsysLsnatBindingForwardDstPort,
       "etsysLsnatBindingReverseSrcIp": etsysLsnatBindingReverseSrcIp,
       "etsysLsnatBindingReverseSrcPort": etsysLsnatBindingReverseSrcPort,
       "etsysLsnatBindingReverseDstIp": etsysLsnatBindingReverseDstIp,
       "etsysLsnatBindingReverseDstPort": etsysLsnatBindingReverseDstPort,
       "etsysLsnatBindingProtocol": etsysLsnatBindingProtocol,
       "etsysLsnatBindingAlgType": etsysLsnatBindingAlgType,
       "etsysLsnatBindingFtpDataBindingCount": etsysLsnatBindingFtpDataBindingCount,
       "etsysLsnatBindingSticky": etsysLsnatBindingSticky,
       "etsysLsnatBindingHWConns": etsysLsnatBindingHWConns,
       "etsysLsnatBindingVserverName": etsysLsnatBindingVserverName,
       "etsysLsnatBindingServerfarmName": etsysLsnatBindingServerfarmName,
       "etsysLsnatBindingRealIp": etsysLsnatBindingRealIp,
       "etsysLsnatBindingRealPort": etsysLsnatBindingRealPort,
       "etsysLsnatBindingCreationDate": etsysLsnatBindingCreationDate,
       "etsysLsnatBindingExpirationDate": etsysLsnatBindingExpirationDate,
       "etsysLsnatBindingIdleTime": etsysLsnatBindingIdleTime,
       "etsysLsnatBindingExpireTime": etsysLsnatBindingExpireTime,
       "etsysLsnatBindingClear": etsysLsnatBindingClear,
       "etsysLsnatStickyTable": etsysLsnatStickyTable,
       "etsysLsnatStickyEntry": etsysLsnatStickyEntry,
       "etsysLsnatStickyId": etsysLsnatStickyId,
       "etsysLsnatStickyType": etsysLsnatStickyType,
       "etsysLsnatStickyAddressType": etsysLsnatStickyAddressType,
       "etsysLsnatStickySrcIp": etsysLsnatStickySrcIp,
       "etsysLsnatStickyDstIp": etsysLsnatStickyDstIp,
       "etsysLsnatStickyDstPort": etsysLsnatStickyDstPort,
       "etsysLsnatStickyHits": etsysLsnatStickyHits,
       "etsysLsnatStickyBindings": etsysLsnatStickyBindings,
       "etsysLsnatStickyVserverName": etsysLsnatStickyVserverName,
       "etsysLsnatStickyServerfarmName": etsysLsnatStickyServerfarmName,
       "etsysLsnatStickyRealIp": etsysLsnatStickyRealIp,
       "etsysLsnatStickyRealPort": etsysLsnatStickyRealPort,
       "etsysLsnatStickyCreationDate": etsysLsnatStickyCreationDate,
       "etsysLsnatStickyExpirationDate": etsysLsnatStickyExpirationDate,
       "etsysLsnatStickyIdleTime": etsysLsnatStickyIdleTime,
       "etsysLsnatStickyExpireTime": etsysLsnatStickyExpireTime,
       "etsysLsnatStickyClear": etsysLsnatStickyClear,
       "etsysLsnatConformance": etsysLsnatConformance,
       "etsysLsnatMIBGroups": etsysLsnatMIBGroups,
       "etsysLsnatMIBGlobalStatsGroup": etsysLsnatMIBGlobalStatsGroup,
       "etsysLsnatMIBGlobalIpv4ConfigGroup": etsysLsnatMIBGlobalIpv4ConfigGroup,
       "etsysLsnatMIBRealServerAccessClientTableGroup": etsysLsnatMIBRealServerAccessClientTableGroup,
       "etsysLsnatMIBServerfarmTableGroup": etsysLsnatMIBServerfarmTableGroup,
       "etsysLsnatMIBRealServerTableGroup": etsysLsnatMIBRealServerTableGroup,
       "etsysLsnatMIBVserverTableGroup": etsysLsnatMIBVserverTableGroup,
       "etsysLsnatMIBVserverVirtualAddressTableGroup": etsysLsnatMIBVserverVirtualAddressTableGroup,
       "etsysLsnatMIBVserverClientTableGroup": etsysLsnatMIBVserverClientTableGroup,
       "etsysLsnatMIBBindingTableGroup": etsysLsnatMIBBindingTableGroup,
       "etsysLsnatMIBStickyTableGroup": etsysLsnatMIBStickyTableGroup,
       "etsysLsnatMIBCompliances": etsysLsnatMIBCompliances,
       "etsysLsnatMIBCompliance": etsysLsnatMIBCompliance}
)
