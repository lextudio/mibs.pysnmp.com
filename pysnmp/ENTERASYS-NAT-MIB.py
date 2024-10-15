# SNMP MIB module (ENTERASYS-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:17 2024
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

etsysNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75)
)
etsysNatMIB.setRevisions(
        ("2010-06-02 11:53",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysNatGlobal_ObjectIdentity = ObjectIdentity
etsysNatGlobal = _EtsysNatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1)
)
_EtsysNatGlobalStats_ObjectIdentity = ObjectIdentity
etsysNatGlobalStats = _EtsysNatGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1)
)
_EtsysNatStatsPoolsUsed_Type = Gauge32
_EtsysNatStatsPoolsUsed_Object = MibScalar
etsysNatStatsPoolsUsed = _EtsysNatStatsPoolsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 1),
    _EtsysNatStatsPoolsUsed_Type()
)
etsysNatStatsPoolsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsPoolsUsed.setStatus("current")
_EtsysNatStatsListRulesUsed_Type = Gauge32
_EtsysNatStatsListRulesUsed_Object = MibScalar
etsysNatStatsListRulesUsed = _EtsysNatStatsListRulesUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 2),
    _EtsysNatStatsListRulesUsed_Type()
)
etsysNatStatsListRulesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsListRulesUsed.setStatus("current")
_EtsysNatStatsStaticRulesUsed_Type = Gauge32
_EtsysNatStatsStaticRulesUsed_Object = MibScalar
etsysNatStatsStaticRulesUsed = _EtsysNatStatsStaticRulesUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 3),
    _EtsysNatStatsStaticRulesUsed_Type()
)
etsysNatStatsStaticRulesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsStaticRulesUsed.setStatus("current")
_EtsysNatStatsAddressUsed_Type = Gauge32
_EtsysNatStatsAddressUsed_Object = MibScalar
etsysNatStatsAddressUsed = _EtsysNatStatsAddressUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 4),
    _EtsysNatStatsAddressUsed_Type()
)
etsysNatStatsAddressUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsAddressUsed.setStatus("current")
_EtsysNatStatsPortMapsUsed_Type = Gauge32
_EtsysNatStatsPortMapsUsed_Object = MibScalar
etsysNatStatsPortMapsUsed = _EtsysNatStatsPortMapsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 5),
    _EtsysNatStatsPortMapsUsed_Type()
)
etsysNatStatsPortMapsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsPortMapsUsed.setStatus("current")
_EtsysNatStatsBindingsCurrent_Type = Gauge32
_EtsysNatStatsBindingsCurrent_Object = MibScalar
etsysNatStatsBindingsCurrent = _EtsysNatStatsBindingsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 6),
    _EtsysNatStatsBindingsCurrent_Type()
)
etsysNatStatsBindingsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsCurrent.setStatus("current")
_EtsysNatStatsBindingsHigh_Type = Gauge32
_EtsysNatStatsBindingsHigh_Object = MibScalar
etsysNatStatsBindingsHigh = _EtsysNatStatsBindingsHigh_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 7),
    _EtsysNatStatsBindingsHigh_Type()
)
etsysNatStatsBindingsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsHigh.setStatus("current")
_EtsysNatStatsBindingsDeleted_Type = Counter32
_EtsysNatStatsBindingsDeleted_Object = MibScalar
etsysNatStatsBindingsDeleted = _EtsysNatStatsBindingsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 8),
    _EtsysNatStatsBindingsDeleted_Type()
)
etsysNatStatsBindingsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsDeleted.setStatus("current")
_EtsysNatStatsBindingsTotal_Type = Counter32
_EtsysNatStatsBindingsTotal_Object = MibScalar
etsysNatStatsBindingsTotal = _EtsysNatStatsBindingsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 9),
    _EtsysNatStatsBindingsTotal_Type()
)
etsysNatStatsBindingsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsTotal.setStatus("current")
_EtsysNatStatsBindingsExhausted_Type = Counter32
_EtsysNatStatsBindingsExhausted_Object = MibScalar
etsysNatStatsBindingsExhausted = _EtsysNatStatsBindingsExhausted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 10),
    _EtsysNatStatsBindingsExhausted_Type()
)
etsysNatStatsBindingsExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsExhausted.setStatus("current")
_EtsysNatStatsBindingsMaxReached_Type = Counter32
_EtsysNatStatsBindingsMaxReached_Object = MibScalar
etsysNatStatsBindingsMaxReached = _EtsysNatStatsBindingsMaxReached_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 11),
    _EtsysNatStatsBindingsMaxReached_Type()
)
etsysNatStatsBindingsMaxReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsMaxReached.setStatus("current")
_EtsysNatStatsBindingsNoIpAddr_Type = Counter32
_EtsysNatStatsBindingsNoIpAddr_Object = MibScalar
etsysNatStatsBindingsNoIpAddr = _EtsysNatStatsBindingsNoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 12),
    _EtsysNatStatsBindingsNoIpAddr_Type()
)
etsysNatStatsBindingsNoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsNoIpAddr.setStatus("current")
_EtsysNatStatsBindingsNoPortmapPort_Type = Counter32
_EtsysNatStatsBindingsNoPortmapPort_Object = MibScalar
etsysNatStatsBindingsNoPortmapPort = _EtsysNatStatsBindingsNoPortmapPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 13),
    _EtsysNatStatsBindingsNoPortmapPort_Type()
)
etsysNatStatsBindingsNoPortmapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsNoPortmapPort.setStatus("current")
_EtsysNatStatsBindingsNoFtpALG_Type = Counter32
_EtsysNatStatsBindingsNoFtpALG_Object = MibScalar
etsysNatStatsBindingsNoFtpALG = _EtsysNatStatsBindingsNoFtpALG_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 14),
    _EtsysNatStatsBindingsNoFtpALG_Type()
)
etsysNatStatsBindingsNoFtpALG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsNoFtpALG.setStatus("current")
_EtsysNatStatsBindingsPerSecond_Type = Gauge32
_EtsysNatStatsBindingsPerSecond_Object = MibScalar
etsysNatStatsBindingsPerSecond = _EtsysNatStatsBindingsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 15),
    _EtsysNatStatsBindingsPerSecond_Type()
)
etsysNatStatsBindingsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsBindingsPerSecond.setStatus("current")


class _EtsysNatStatsClear_Type(TruthValue):
    """Custom type etsysNatStatsClear based on TruthValue"""


_EtsysNatStatsClear_Object = MibScalar
etsysNatStatsClear = _EtsysNatStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 16),
    _EtsysNatStatsClear_Type()
)
etsysNatStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatStatsClear.setStatus("current")
_EtsysNatStatsClearDateAndTime_Type = DateAndTime
_EtsysNatStatsClearDateAndTime_Object = MibScalar
etsysNatStatsClearDateAndTime = _EtsysNatStatsClearDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 17),
    _EtsysNatStatsClearDateAndTime_Type()
)
etsysNatStatsClearDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsClearDateAndTime.setStatus("current")
_EtsysNatStatsTranslationProtocolRulesCount_Type = Gauge32
_EtsysNatStatsTranslationProtocolRulesCount_Object = MibScalar
etsysNatStatsTranslationProtocolRulesCount = _EtsysNatStatsTranslationProtocolRulesCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 18),
    _EtsysNatStatsTranslationProtocolRulesCount_Type()
)
etsysNatStatsTranslationProtocolRulesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsTranslationProtocolRulesCount.setStatus("current")
_EtsysNatStatsMinTimeoutValue_Type = Unsigned32
_EtsysNatStatsMinTimeoutValue_Object = MibScalar
etsysNatStatsMinTimeoutValue = _EtsysNatStatsMinTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 19),
    _EtsysNatStatsMinTimeoutValue_Type()
)
etsysNatStatsMinTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsMinTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatStatsMinTimeoutValue.setUnits("seconds")
_EtsysNatStatsMaxTimeoutValue_Type = Unsigned32
_EtsysNatStatsMaxTimeoutValue_Object = MibScalar
etsysNatStatsMaxTimeoutValue = _EtsysNatStatsMaxTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 1, 20),
    _EtsysNatStatsMaxTimeoutValue_Type()
)
etsysNatStatsMaxTimeoutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStatsMaxTimeoutValue.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatStatsMaxTimeoutValue.setUnits("seconds")
_EtsysNatGlobalIpv4Config_ObjectIdentity = ObjectIdentity
etsysNatGlobalIpv4Config = _EtsysNatGlobalIpv4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2)
)


class _EtsysNatIpv4ConfigLogTranslations_Type(Integer32):
    """Custom type etsysNatIpv4ConfigLogTranslations based on Integer32"""
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


_EtsysNatIpv4ConfigLogTranslations_Type.__name__ = "Integer32"
_EtsysNatIpv4ConfigLogTranslations_Object = MibScalar
etsysNatIpv4ConfigLogTranslations = _EtsysNatIpv4ConfigLogTranslations_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 1),
    _EtsysNatIpv4ConfigLogTranslations_Type()
)
etsysNatIpv4ConfigLogTranslations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigLogTranslations.setStatus("current")


class _EtsysNatIpv4ConfigInspectDNS_Type(Integer32):
    """Custom type etsysNatIpv4ConfigInspectDNS based on Integer32"""
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


_EtsysNatIpv4ConfigInspectDNS_Type.__name__ = "Integer32"
_EtsysNatIpv4ConfigInspectDNS_Object = MibScalar
etsysNatIpv4ConfigInspectDNS = _EtsysNatIpv4ConfigInspectDNS_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 2),
    _EtsysNatIpv4ConfigInspectDNS_Type()
)
etsysNatIpv4ConfigInspectDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigInspectDNS.setStatus("current")


class _EtsysNatIpv4ConfigFtpCtrlPort_Type(InetPortNumber):
    """Custom type etsysNatIpv4ConfigFtpCtrlPort based on InetPortNumber"""
    defaultValue = 21

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatIpv4ConfigFtpCtrlPort_Type.__name__ = "InetPortNumber"
_EtsysNatIpv4ConfigFtpCtrlPort_Object = MibScalar
etsysNatIpv4ConfigFtpCtrlPort = _EtsysNatIpv4ConfigFtpCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 3),
    _EtsysNatIpv4ConfigFtpCtrlPort_Type()
)
etsysNatIpv4ConfigFtpCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigFtpCtrlPort.setStatus("current")


class _EtsysNatIpv4ConfigMaxEntries_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigMaxEntries based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysNatIpv4ConfigMaxEntries_Type.__name__ = "Unsigned32"
_EtsysNatIpv4ConfigMaxEntries_Object = MibScalar
etsysNatIpv4ConfigMaxEntries = _EtsysNatIpv4ConfigMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 4),
    _EtsysNatIpv4ConfigMaxEntries_Type()
)
etsysNatIpv4ConfigMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigMaxEntries.setStatus("current")


class _EtsysNatIpv4ConfigTimeout_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysNatIpv4ConfigTimeout_Object = MibScalar
etsysNatIpv4ConfigTimeout = _EtsysNatIpv4ConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 5),
    _EtsysNatIpv4ConfigTimeout_Type()
)
etsysNatIpv4ConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigTimeout.setUnits("seconds")


class _EtsysNatIpv4ConfigUdpTimeout_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigUdpTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysNatIpv4ConfigUdpTimeout_Object = MibScalar
etsysNatIpv4ConfigUdpTimeout = _EtsysNatIpv4ConfigUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 6),
    _EtsysNatIpv4ConfigUdpTimeout_Type()
)
etsysNatIpv4ConfigUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigUdpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigUdpTimeout.setUnits("seconds")


class _EtsysNatIpv4ConfigTcpTimeout_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigTcpTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysNatIpv4ConfigTcpTimeout_Object = MibScalar
etsysNatIpv4ConfigTcpTimeout = _EtsysNatIpv4ConfigTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 7),
    _EtsysNatIpv4ConfigTcpTimeout_Type()
)
etsysNatIpv4ConfigTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigTcpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigTcpTimeout.setUnits("seconds")


class _EtsysNatIpv4ConfigFtpTimeout_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigFtpTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysNatIpv4ConfigFtpTimeout_Object = MibScalar
etsysNatIpv4ConfigFtpTimeout = _EtsysNatIpv4ConfigFtpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 8),
    _EtsysNatIpv4ConfigFtpTimeout_Type()
)
etsysNatIpv4ConfigFtpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigFtpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigFtpTimeout.setUnits("seconds")


class _EtsysNatIpv4ConfigDnsTimeout_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigDnsTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysNatIpv4ConfigDnsTimeout_Object = MibScalar
etsysNatIpv4ConfigDnsTimeout = _EtsysNatIpv4ConfigDnsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 9),
    _EtsysNatIpv4ConfigDnsTimeout_Type()
)
etsysNatIpv4ConfigDnsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigDnsTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigDnsTimeout.setUnits("seconds")


class _EtsysNatIpv4ConfigIcmpTimeout_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigIcmpTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysNatIpv4ConfigIcmpTimeout_Object = MibScalar
etsysNatIpv4ConfigIcmpTimeout = _EtsysNatIpv4ConfigIcmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 10),
    _EtsysNatIpv4ConfigIcmpTimeout_Type()
)
etsysNatIpv4ConfigIcmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigIcmpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigIcmpTimeout.setUnits("seconds")


class _EtsysNatIpv4ConfigFinRstTimeout_Type(Unsigned32):
    """Custom type etsysNatIpv4ConfigFinRstTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysNatIpv4ConfigFinRstTimeout_Type.__name__ = "Unsigned32"
_EtsysNatIpv4ConfigFinRstTimeout_Object = MibScalar
etsysNatIpv4ConfigFinRstTimeout = _EtsysNatIpv4ConfigFinRstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 11),
    _EtsysNatIpv4ConfigFinRstTimeout_Type()
)
etsysNatIpv4ConfigFinRstTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigFinRstTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigFinRstTimeout.setUnits("seconds")


class _EtsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus_Type(Integer32):
    """Custom type etsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus based on Integer32"""
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


_EtsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus_Type.__name__ = "Integer32"
_EtsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus_Object = MibScalar
etsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus = _EtsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 1, 2, 12),
    _EtsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus_Type()
)
etsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus.setStatus("current")
_EtsysNatTables_ObjectIdentity = ObjectIdentity
etsysNatTables = _EtsysNatTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2)
)
_EtsysNatTranslationProtocolRulesTable_Object = MibTable
etsysNatTranslationProtocolRulesTable = _EtsysNatTranslationProtocolRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1)
)
if mibBuilder.loadTexts:
    etsysNatTranslationProtocolRulesTable.setStatus("current")
_EtsysNatTranslationProtocolRulesEntry_Object = MibTableRow
etsysNatTranslationProtocolRulesEntry = _EtsysNatTranslationProtocolRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1, 1)
)
etsysNatTranslationProtocolRulesEntry.setIndexNames(
    (0, "ENTERASYS-NAT-MIB", "etsysNatTranslationInetVersion"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatTranslationProtocol"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatTranslationPort"),
)
if mibBuilder.loadTexts:
    etsysNatTranslationProtocolRulesEntry.setStatus("current")
_EtsysNatTranslationInetVersion_Type = InetVersion
_EtsysNatTranslationInetVersion_Object = MibTableColumn
etsysNatTranslationInetVersion = _EtsysNatTranslationInetVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1, 1, 1),
    _EtsysNatTranslationInetVersion_Type()
)
etsysNatTranslationInetVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatTranslationInetVersion.setStatus("current")


class _EtsysNatTranslationProtocol_Type(Integer32):
    """Custom type etsysNatTranslationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysNatTranslationProtocol_Type.__name__ = "Integer32"
_EtsysNatTranslationProtocol_Object = MibTableColumn
etsysNatTranslationProtocol = _EtsysNatTranslationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1, 1, 2),
    _EtsysNatTranslationProtocol_Type()
)
etsysNatTranslationProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatTranslationProtocol.setStatus("current")


class _EtsysNatTranslationPort_Type(InetPortNumber):
    """Custom type etsysNatTranslationPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatTranslationPort_Type.__name__ = "InetPortNumber"
_EtsysNatTranslationPort_Object = MibTableColumn
etsysNatTranslationPort = _EtsysNatTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1, 1, 3),
    _EtsysNatTranslationPort_Type()
)
etsysNatTranslationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatTranslationPort.setStatus("current")


class _EtsysNatTranslationTimeout_Type(Unsigned32):
    """Custom type etsysNatTranslationTimeout based on Unsigned32"""
    defaultValue = 240


_EtsysNatTranslationTimeout_Object = MibTableColumn
etsysNatTranslationTimeout = _EtsysNatTranslationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1, 1, 4),
    _EtsysNatTranslationTimeout_Type()
)
etsysNatTranslationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatTranslationTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatTranslationTimeout.setUnits("seconds")


class _EtsysNatTranslationOneShot_Type(Integer32):
    """Custom type etsysNatTranslationOneShot based on Integer32"""
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


_EtsysNatTranslationOneShot_Type.__name__ = "Integer32"
_EtsysNatTranslationOneShot_Object = MibTableColumn
etsysNatTranslationOneShot = _EtsysNatTranslationOneShot_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1, 1, 5),
    _EtsysNatTranslationOneShot_Type()
)
etsysNatTranslationOneShot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatTranslationOneShot.setStatus("current")
_EtsysNatTranslationRowStatus_Type = RowStatus
_EtsysNatTranslationRowStatus_Object = MibTableColumn
etsysNatTranslationRowStatus = _EtsysNatTranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 1, 1, 6),
    _EtsysNatTranslationRowStatus_Type()
)
etsysNatTranslationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatTranslationRowStatus.setStatus("current")
_EtsysNatPoolTable_Object = MibTable
etsysNatPoolTable = _EtsysNatPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2)
)
if mibBuilder.loadTexts:
    etsysNatPoolTable.setStatus("current")
_EtsysNatPoolEntry_Object = MibTableRow
etsysNatPoolEntry = _EtsysNatPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1)
)
etsysNatPoolEntry.setIndexNames(
    (0, "ENTERASYS-NAT-MIB", "etsysNatPoolAddressType"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatPoolName"),
)
if mibBuilder.loadTexts:
    etsysNatPoolEntry.setStatus("current")
_EtsysNatPoolAddressType_Type = InetAddressType
_EtsysNatPoolAddressType_Object = MibTableColumn
etsysNatPoolAddressType = _EtsysNatPoolAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 1),
    _EtsysNatPoolAddressType_Type()
)
etsysNatPoolAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatPoolAddressType.setStatus("current")


class _EtsysNatPoolName_Type(SnmpAdminString):
    """Custom type etsysNatPoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysNatPoolName_Type.__name__ = "SnmpAdminString"
_EtsysNatPoolName_Object = MibTableColumn
etsysNatPoolName = _EtsysNatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 2),
    _EtsysNatPoolName_Type()
)
etsysNatPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatPoolName.setStatus("current")


class _EtsysNatPoolFirstIpAddr_Type(InetAddress):
    """Custom type etsysNatPoolFirstIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysNatPoolFirstIpAddr_Type.__name__ = "InetAddress"
_EtsysNatPoolFirstIpAddr_Object = MibTableColumn
etsysNatPoolFirstIpAddr = _EtsysNatPoolFirstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 3),
    _EtsysNatPoolFirstIpAddr_Type()
)
etsysNatPoolFirstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatPoolFirstIpAddr.setStatus("current")


class _EtsysNatPoolLastIpAddr_Type(InetAddress):
    """Custom type etsysNatPoolLastIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysNatPoolLastIpAddr_Type.__name__ = "InetAddress"
_EtsysNatPoolLastIpAddr_Object = MibTableColumn
etsysNatPoolLastIpAddr = _EtsysNatPoolLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 4),
    _EtsysNatPoolLastIpAddr_Type()
)
etsysNatPoolLastIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatPoolLastIpAddr.setStatus("current")
_EtsysNatPoolPrefixLen_Type = InetAddressPrefixLength
_EtsysNatPoolPrefixLen_Object = MibTableColumn
etsysNatPoolPrefixLen = _EtsysNatPoolPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 5),
    _EtsysNatPoolPrefixLen_Type()
)
etsysNatPoolPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatPoolPrefixLen.setStatus("current")


class _EtsysNatPoolNextIpAddr_Type(InetAddress):
    """Custom type etsysNatPoolNextIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysNatPoolNextIpAddr_Type.__name__ = "InetAddress"
_EtsysNatPoolNextIpAddr_Object = MibTableColumn
etsysNatPoolNextIpAddr = _EtsysNatPoolNextIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 6),
    _EtsysNatPoolNextIpAddr_Type()
)
etsysNatPoolNextIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolNextIpAddr.setStatus("current")
_EtsysNatPoolAddrCount_Type = Gauge32
_EtsysNatPoolAddrCount_Object = MibTableColumn
etsysNatPoolAddrCount = _EtsysNatPoolAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 7),
    _EtsysNatPoolAddrCount_Type()
)
etsysNatPoolAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolAddrCount.setStatus("current")
_EtsysNatPoolAddrUsed_Type = Gauge32
_EtsysNatPoolAddrUsed_Object = MibTableColumn
etsysNatPoolAddrUsed = _EtsysNatPoolAddrUsed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 8),
    _EtsysNatPoolAddrUsed_Type()
)
etsysNatPoolAddrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolAddrUsed.setStatus("current")
_EtsysNatPoolAddrAlloc_Type = Gauge32
_EtsysNatPoolAddrAlloc_Object = MibTableColumn
etsysNatPoolAddrAlloc = _EtsysNatPoolAddrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 9),
    _EtsysNatPoolAddrAlloc_Type()
)
etsysNatPoolAddrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolAddrAlloc.setStatus("current")
_EtsysNatPoolOutOfAddrs_Type = Counter32
_EtsysNatPoolOutOfAddrs_Object = MibTableColumn
etsysNatPoolOutOfAddrs = _EtsysNatPoolOutOfAddrs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 10),
    _EtsysNatPoolOutOfAddrs_Type()
)
etsysNatPoolOutOfAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolOutOfAddrs.setStatus("current")
_EtsysNatPoolPortAlloc_Type = Gauge32
_EtsysNatPoolPortAlloc_Object = MibTableColumn
etsysNatPoolPortAlloc = _EtsysNatPoolPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 11),
    _EtsysNatPoolPortAlloc_Type()
)
etsysNatPoolPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolPortAlloc.setStatus("current")
_EtsysNatPoolOutOfPorts_Type = Counter32
_EtsysNatPoolOutOfPorts_Object = MibTableColumn
etsysNatPoolOutOfPorts = _EtsysNatPoolOutOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 12),
    _EtsysNatPoolOutOfPorts_Type()
)
etsysNatPoolOutOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolOutOfPorts.setStatus("current")
_EtsysNatPoolConns_Type = Gauge32
_EtsysNatPoolConns_Object = MibTableColumn
etsysNatPoolConns = _EtsysNatPoolConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 13),
    _EtsysNatPoolConns_Type()
)
etsysNatPoolConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolConns.setStatus("current")
_EtsysNatPoolHits_Type = Counter32
_EtsysNatPoolHits_Object = MibTableColumn
etsysNatPoolHits = _EtsysNatPoolHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 14),
    _EtsysNatPoolHits_Type()
)
etsysNatPoolHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolHits.setStatus("current")
_EtsysNatPoolListRulesCount_Type = Gauge32
_EtsysNatPoolListRulesCount_Object = MibTableColumn
etsysNatPoolListRulesCount = _EtsysNatPoolListRulesCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 15),
    _EtsysNatPoolListRulesCount_Type()
)
etsysNatPoolListRulesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolListRulesCount.setStatus("current")
_EtsysNatPoolLsnatVservers_Type = Gauge32
_EtsysNatPoolLsnatVservers_Object = MibTableColumn
etsysNatPoolLsnatVservers = _EtsysNatPoolLsnatVservers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 16),
    _EtsysNatPoolLsnatVservers_Type()
)
etsysNatPoolLsnatVservers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatPoolLsnatVservers.setStatus("current")
_EtsysNatPoolRowStatus_Type = RowStatus
_EtsysNatPoolRowStatus_Object = MibTableColumn
etsysNatPoolRowStatus = _EtsysNatPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 2, 1, 17),
    _EtsysNatPoolRowStatus_Type()
)
etsysNatPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatPoolRowStatus.setStatus("current")
_EtsysNatListRuleTable_Object = MibTable
etsysNatListRuleTable = _EtsysNatListRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3)
)
if mibBuilder.loadTexts:
    etsysNatListRuleTable.setStatus("current")
_EtsysNatListRuleEntry_Object = MibTableRow
etsysNatListRuleEntry = _EtsysNatListRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1)
)
etsysNatListRuleEntry.setIndexNames(
    (0, "ENTERASYS-NAT-MIB", "etsysNatListRuleInetVersion"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatListRuleDirection"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatListRuleMatchType"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatListRuleName"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatListRuleInsideVrfName"),
)
if mibBuilder.loadTexts:
    etsysNatListRuleEntry.setStatus("current")
_EtsysNatListRuleInetVersion_Type = InetVersion
_EtsysNatListRuleInetVersion_Object = MibTableColumn
etsysNatListRuleInetVersion = _EtsysNatListRuleInetVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 1),
    _EtsysNatListRuleInetVersion_Type()
)
etsysNatListRuleInetVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatListRuleInetVersion.setStatus("current")


class _EtsysNatListRuleDirection_Type(Integer32):
    """Custom type etsysNatListRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2))
    )


_EtsysNatListRuleDirection_Type.__name__ = "Integer32"
_EtsysNatListRuleDirection_Object = MibTableColumn
etsysNatListRuleDirection = _EtsysNatListRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 2),
    _EtsysNatListRuleDirection_Type()
)
etsysNatListRuleDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatListRuleDirection.setStatus("current")


class _EtsysNatListRuleMatchType_Type(Integer32):
    """Custom type etsysNatListRuleMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1))
    )


_EtsysNatListRuleMatchType_Type.__name__ = "Integer32"
_EtsysNatListRuleMatchType_Object = MibTableColumn
etsysNatListRuleMatchType = _EtsysNatListRuleMatchType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 3),
    _EtsysNatListRuleMatchType_Type()
)
etsysNatListRuleMatchType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatListRuleMatchType.setStatus("current")


class _EtsysNatListRuleName_Type(SnmpAdminString):
    """Custom type etsysNatListRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysNatListRuleName_Type.__name__ = "SnmpAdminString"
_EtsysNatListRuleName_Object = MibTableColumn
etsysNatListRuleName = _EtsysNatListRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 4),
    _EtsysNatListRuleName_Type()
)
etsysNatListRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatListRuleName.setStatus("current")


class _EtsysNatListRuleInsideVrfName_Type(SnmpAdminString):
    """Custom type etsysNatListRuleInsideVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EtsysNatListRuleInsideVrfName_Type.__name__ = "SnmpAdminString"
_EtsysNatListRuleInsideVrfName_Object = MibTableColumn
etsysNatListRuleInsideVrfName = _EtsysNatListRuleInsideVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 5),
    _EtsysNatListRuleInsideVrfName_Type()
)
etsysNatListRuleInsideVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatListRuleInsideVrfName.setStatus("current")


class _EtsysNatListRulePoolName_Type(SnmpAdminString):
    """Custom type etsysNatListRulePoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysNatListRulePoolName_Type.__name__ = "SnmpAdminString"
_EtsysNatListRulePoolName_Object = MibTableColumn
etsysNatListRulePoolName = _EtsysNatListRulePoolName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 6),
    _EtsysNatListRulePoolName_Type()
)
etsysNatListRulePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatListRulePoolName.setStatus("current")


class _EtsysNatListRuleIfIndex_Type(InterfaceIndexOrZero):
    """Custom type etsysNatListRuleIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_EtsysNatListRuleIfIndex_Object = MibTableColumn
etsysNatListRuleIfIndex = _EtsysNatListRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 7),
    _EtsysNatListRuleIfIndex_Type()
)
etsysNatListRuleIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatListRuleIfIndex.setStatus("current")


class _EtsysNatListRuleOverloaded_Type(TruthValue):
    """Custom type etsysNatListRuleOverloaded based on TruthValue"""


_EtsysNatListRuleOverloaded_Object = MibTableColumn
etsysNatListRuleOverloaded = _EtsysNatListRuleOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 8),
    _EtsysNatListRuleOverloaded_Type()
)
etsysNatListRuleOverloaded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatListRuleOverloaded.setStatus("current")
_EtsysNatListRuleConns_Type = Gauge32
_EtsysNatListRuleConns_Object = MibTableColumn
etsysNatListRuleConns = _EtsysNatListRuleConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 9),
    _EtsysNatListRuleConns_Type()
)
etsysNatListRuleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatListRuleConns.setStatus("current")
_EtsysNatListRuleHits_Type = Counter32
_EtsysNatListRuleHits_Object = MibTableColumn
etsysNatListRuleHits = _EtsysNatListRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 10),
    _EtsysNatListRuleHits_Type()
)
etsysNatListRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatListRuleHits.setStatus("current")
_EtsysNatListRuleRowStatus_Type = RowStatus
_EtsysNatListRuleRowStatus_Object = MibTableColumn
etsysNatListRuleRowStatus = _EtsysNatListRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 3, 1, 11),
    _EtsysNatListRuleRowStatus_Type()
)
etsysNatListRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatListRuleRowStatus.setStatus("current")
_EtsysNatStaticRuleTable_Object = MibTable
etsysNatStaticRuleTable = _EtsysNatStaticRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4)
)
if mibBuilder.loadTexts:
    etsysNatStaticRuleTable.setStatus("current")
_EtsysNatStaticRuleEntry_Object = MibTableRow
etsysNatStaticRuleEntry = _EtsysNatStaticRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1)
)
etsysNatStaticRuleEntry.setIndexNames(
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleAddressType"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleDirection"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleMatchType"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleProtocol"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleLocalIpAddr"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleLocalPort"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleGlobalIpAddr"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleGlobalPort"),
    (0, "ENTERASYS-NAT-MIB", "etsysNatStaticRuleInsideVrfName"),
)
if mibBuilder.loadTexts:
    etsysNatStaticRuleEntry.setStatus("current")
_EtsysNatStaticRuleAddressType_Type = InetAddressType
_EtsysNatStaticRuleAddressType_Object = MibTableColumn
etsysNatStaticRuleAddressType = _EtsysNatStaticRuleAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 1),
    _EtsysNatStaticRuleAddressType_Type()
)
etsysNatStaticRuleAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleAddressType.setStatus("current")


class _EtsysNatStaticRuleDirection_Type(Integer32):
    """Custom type etsysNatStaticRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2))
    )


_EtsysNatStaticRuleDirection_Type.__name__ = "Integer32"
_EtsysNatStaticRuleDirection_Object = MibTableColumn
etsysNatStaticRuleDirection = _EtsysNatStaticRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 2),
    _EtsysNatStaticRuleDirection_Type()
)
etsysNatStaticRuleDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleDirection.setStatus("current")


class _EtsysNatStaticRuleMatchType_Type(Integer32):
    """Custom type etsysNatStaticRuleMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1))
    )


_EtsysNatStaticRuleMatchType_Type.__name__ = "Integer32"
_EtsysNatStaticRuleMatchType_Object = MibTableColumn
etsysNatStaticRuleMatchType = _EtsysNatStaticRuleMatchType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 3),
    _EtsysNatStaticRuleMatchType_Type()
)
etsysNatStaticRuleMatchType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleMatchType.setStatus("current")


class _EtsysNatStaticRuleProtocol_Type(Integer32):
    """Custom type etsysNatStaticRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_EtsysNatStaticRuleProtocol_Type.__name__ = "Integer32"
_EtsysNatStaticRuleProtocol_Object = MibTableColumn
etsysNatStaticRuleProtocol = _EtsysNatStaticRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 4),
    _EtsysNatStaticRuleProtocol_Type()
)
etsysNatStaticRuleProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleProtocol.setStatus("current")


class _EtsysNatStaticRuleLocalIpAddr_Type(InetAddress):
    """Custom type etsysNatStaticRuleLocalIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysNatStaticRuleLocalIpAddr_Type.__name__ = "InetAddress"
_EtsysNatStaticRuleLocalIpAddr_Object = MibTableColumn
etsysNatStaticRuleLocalIpAddr = _EtsysNatStaticRuleLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 5),
    _EtsysNatStaticRuleLocalIpAddr_Type()
)
etsysNatStaticRuleLocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleLocalIpAddr.setStatus("current")


class _EtsysNatStaticRuleLocalPort_Type(InetPortNumber):
    """Custom type etsysNatStaticRuleLocalPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatStaticRuleLocalPort_Type.__name__ = "InetPortNumber"
_EtsysNatStaticRuleLocalPort_Object = MibTableColumn
etsysNatStaticRuleLocalPort = _EtsysNatStaticRuleLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 6),
    _EtsysNatStaticRuleLocalPort_Type()
)
etsysNatStaticRuleLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleLocalPort.setStatus("current")


class _EtsysNatStaticRuleGlobalIpAddr_Type(InetAddress):
    """Custom type etsysNatStaticRuleGlobalIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysNatStaticRuleGlobalIpAddr_Type.__name__ = "InetAddress"
_EtsysNatStaticRuleGlobalIpAddr_Object = MibTableColumn
etsysNatStaticRuleGlobalIpAddr = _EtsysNatStaticRuleGlobalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 7),
    _EtsysNatStaticRuleGlobalIpAddr_Type()
)
etsysNatStaticRuleGlobalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleGlobalIpAddr.setStatus("current")


class _EtsysNatStaticRuleGlobalPort_Type(InetPortNumber):
    """Custom type etsysNatStaticRuleGlobalPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatStaticRuleGlobalPort_Type.__name__ = "InetPortNumber"
_EtsysNatStaticRuleGlobalPort_Object = MibTableColumn
etsysNatStaticRuleGlobalPort = _EtsysNatStaticRuleGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 8),
    _EtsysNatStaticRuleGlobalPort_Type()
)
etsysNatStaticRuleGlobalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleGlobalPort.setStatus("current")


class _EtsysNatStaticRuleInsideVrfName_Type(SnmpAdminString):
    """Custom type etsysNatStaticRuleInsideVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EtsysNatStaticRuleInsideVrfName_Type.__name__ = "SnmpAdminString"
_EtsysNatStaticRuleInsideVrfName_Object = MibTableColumn
etsysNatStaticRuleInsideVrfName = _EtsysNatStaticRuleInsideVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 9),
    _EtsysNatStaticRuleInsideVrfName_Type()
)
etsysNatStaticRuleInsideVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatStaticRuleInsideVrfName.setStatus("current")
_EtsysNatStaticRuleOverloaded_Type = TruthValue
_EtsysNatStaticRuleOverloaded_Object = MibTableColumn
etsysNatStaticRuleOverloaded = _EtsysNatStaticRuleOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 10),
    _EtsysNatStaticRuleOverloaded_Type()
)
etsysNatStaticRuleOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStaticRuleOverloaded.setStatus("current")
_EtsysNatStaticRuleConns_Type = Gauge32
_EtsysNatStaticRuleConns_Object = MibTableColumn
etsysNatStaticRuleConns = _EtsysNatStaticRuleConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 11),
    _EtsysNatStaticRuleConns_Type()
)
etsysNatStaticRuleConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStaticRuleConns.setStatus("current")
_EtsysNatStaticRuleHits_Type = Counter32
_EtsysNatStaticRuleHits_Object = MibTableColumn
etsysNatStaticRuleHits = _EtsysNatStaticRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 12),
    _EtsysNatStaticRuleHits_Type()
)
etsysNatStaticRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStaticRuleHits.setStatus("current")
_EtsysNatStaticRuleReservedBindingId_Type = Unsigned32
_EtsysNatStaticRuleReservedBindingId_Object = MibTableColumn
etsysNatStaticRuleReservedBindingId = _EtsysNatStaticRuleReservedBindingId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 13),
    _EtsysNatStaticRuleReservedBindingId_Type()
)
etsysNatStaticRuleReservedBindingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatStaticRuleReservedBindingId.setStatus("current")
_EtsysNatStaticRuleRowStatus_Type = RowStatus
_EtsysNatStaticRuleRowStatus_Object = MibTableColumn
etsysNatStaticRuleRowStatus = _EtsysNatStaticRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 4, 1, 14),
    _EtsysNatStaticRuleRowStatus_Type()
)
etsysNatStaticRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysNatStaticRuleRowStatus.setStatus("current")
_EtsysNatBindingTable_Object = MibTable
etsysNatBindingTable = _EtsysNatBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5)
)
if mibBuilder.loadTexts:
    etsysNatBindingTable.setStatus("current")
_EtsysNatBindingEntry_Object = MibTableRow
etsysNatBindingEntry = _EtsysNatBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1)
)
etsysNatBindingEntry.setIndexNames(
    (0, "ENTERASYS-NAT-MIB", "etsysNatBindingId"),
)
if mibBuilder.loadTexts:
    etsysNatBindingEntry.setStatus("current")
_EtsysNatBindingId_Type = Unsigned32
_EtsysNatBindingId_Object = MibTableColumn
etsysNatBindingId = _EtsysNatBindingId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 1),
    _EtsysNatBindingId_Type()
)
etsysNatBindingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNatBindingId.setStatus("current")


class _EtsysNatBindingState_Type(Integer32):
    """Custom type etsysNatBindingState based on Integer32"""
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
        *(("established", 4),
          ("init", 1),
          ("syncing", 2),
          ("waitroute", 3))
    )


_EtsysNatBindingState_Type.__name__ = "Integer32"
_EtsysNatBindingState_Object = MibTableColumn
etsysNatBindingState = _EtsysNatBindingState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 2),
    _EtsysNatBindingState_Type()
)
etsysNatBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingState.setStatus("current")
_EtsysNatBindingAddressType_Type = InetAddressType
_EtsysNatBindingAddressType_Object = MibTableColumn
etsysNatBindingAddressType = _EtsysNatBindingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 3),
    _EtsysNatBindingAddressType_Type()
)
etsysNatBindingAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingAddressType.setStatus("current")
_EtsysNatBindingForwardSrcIp_Type = InetAddress
_EtsysNatBindingForwardSrcIp_Object = MibTableColumn
etsysNatBindingForwardSrcIp = _EtsysNatBindingForwardSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 4),
    _EtsysNatBindingForwardSrcIp_Type()
)
etsysNatBindingForwardSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingForwardSrcIp.setStatus("current")


class _EtsysNatBindingForwardSrcPort_Type(InetPortNumber):
    """Custom type etsysNatBindingForwardSrcPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatBindingForwardSrcPort_Type.__name__ = "InetPortNumber"
_EtsysNatBindingForwardSrcPort_Object = MibTableColumn
etsysNatBindingForwardSrcPort = _EtsysNatBindingForwardSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 5),
    _EtsysNatBindingForwardSrcPort_Type()
)
etsysNatBindingForwardSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingForwardSrcPort.setStatus("current")
_EtsysNatBindingForwardDstIp_Type = InetAddress
_EtsysNatBindingForwardDstIp_Object = MibTableColumn
etsysNatBindingForwardDstIp = _EtsysNatBindingForwardDstIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 6),
    _EtsysNatBindingForwardDstIp_Type()
)
etsysNatBindingForwardDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingForwardDstIp.setStatus("current")


class _EtsysNatBindingForwardDstPort_Type(InetPortNumber):
    """Custom type etsysNatBindingForwardDstPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatBindingForwardDstPort_Type.__name__ = "InetPortNumber"
_EtsysNatBindingForwardDstPort_Object = MibTableColumn
etsysNatBindingForwardDstPort = _EtsysNatBindingForwardDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 7),
    _EtsysNatBindingForwardDstPort_Type()
)
etsysNatBindingForwardDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingForwardDstPort.setStatus("current")
_EtsysNatBindingReverseSrcIp_Type = InetAddress
_EtsysNatBindingReverseSrcIp_Object = MibTableColumn
etsysNatBindingReverseSrcIp = _EtsysNatBindingReverseSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 8),
    _EtsysNatBindingReverseSrcIp_Type()
)
etsysNatBindingReverseSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingReverseSrcIp.setStatus("current")


class _EtsysNatBindingReverseSrcPort_Type(InetPortNumber):
    """Custom type etsysNatBindingReverseSrcPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatBindingReverseSrcPort_Type.__name__ = "InetPortNumber"
_EtsysNatBindingReverseSrcPort_Object = MibTableColumn
etsysNatBindingReverseSrcPort = _EtsysNatBindingReverseSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 9),
    _EtsysNatBindingReverseSrcPort_Type()
)
etsysNatBindingReverseSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingReverseSrcPort.setStatus("current")
_EtsysNatBindingReverseDstIp_Type = InetAddress
_EtsysNatBindingReverseDstIp_Object = MibTableColumn
etsysNatBindingReverseDstIp = _EtsysNatBindingReverseDstIp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 10),
    _EtsysNatBindingReverseDstIp_Type()
)
etsysNatBindingReverseDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingReverseDstIp.setStatus("current")


class _EtsysNatBindingReverseDstPort_Type(InetPortNumber):
    """Custom type etsysNatBindingReverseDstPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatBindingReverseDstPort_Type.__name__ = "InetPortNumber"
_EtsysNatBindingReverseDstPort_Object = MibTableColumn
etsysNatBindingReverseDstPort = _EtsysNatBindingReverseDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 11),
    _EtsysNatBindingReverseDstPort_Type()
)
etsysNatBindingReverseDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingReverseDstPort.setStatus("current")


class _EtsysNatBindingRuleType_Type(Integer32):
    """Custom type etsysNatBindingRuleType based on Integer32"""
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
        *(("dynamic", 2),
          ("dynamicReserved", 4),
          ("static", 1),
          ("staticReserved", 3))
    )


_EtsysNatBindingRuleType_Type.__name__ = "Integer32"
_EtsysNatBindingRuleType_Object = MibTableColumn
etsysNatBindingRuleType = _EtsysNatBindingRuleType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 12),
    _EtsysNatBindingRuleType_Type()
)
etsysNatBindingRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingRuleType.setStatus("current")


class _EtsysNatBindingPoolName_Type(SnmpAdminString):
    """Custom type etsysNatBindingPoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EtsysNatBindingPoolName_Type.__name__ = "SnmpAdminString"
_EtsysNatBindingPoolName_Object = MibTableColumn
etsysNatBindingPoolName = _EtsysNatBindingPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 13),
    _EtsysNatBindingPoolName_Type()
)
etsysNatBindingPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingPoolName.setStatus("current")


class _EtsysNatBindingProtocol_Type(Integer32):
    """Custom type etsysNatBindingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_EtsysNatBindingProtocol_Type.__name__ = "Integer32"
_EtsysNatBindingProtocol_Object = MibTableColumn
etsysNatBindingProtocol = _EtsysNatBindingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 14),
    _EtsysNatBindingProtocol_Type()
)
etsysNatBindingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingProtocol.setStatus("current")


class _EtsysNatBindingAlgType_Type(Integer32):
    """Custom type etsysNatBindingAlgType based on Integer32"""
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
        *(("ftpctrl", 2),
          ("ftpdata", 3),
          ("icmpecho", 5),
          ("none", 1),
          ("tftpctrl", 4))
    )


_EtsysNatBindingAlgType_Type.__name__ = "Integer32"
_EtsysNatBindingAlgType_Object = MibTableColumn
etsysNatBindingAlgType = _EtsysNatBindingAlgType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 15),
    _EtsysNatBindingAlgType_Type()
)
etsysNatBindingAlgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingAlgType.setStatus("current")


class _EtsysNatBindingFtpDataChannelCount_Type(Unsigned32):
    """Custom type etsysNatBindingFtpDataChannelCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatBindingFtpDataChannelCount_Type.__name__ = "Unsigned32"
_EtsysNatBindingFtpDataChannelCount_Object = MibTableColumn
etsysNatBindingFtpDataChannelCount = _EtsysNatBindingFtpDataChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 16),
    _EtsysNatBindingFtpDataChannelCount_Type()
)
etsysNatBindingFtpDataChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingFtpDataChannelCount.setStatus("current")


class _EtsysNatBindingIcmpFwdIdent_Type(Unsigned32):
    """Custom type etsysNatBindingIcmpFwdIdent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatBindingIcmpFwdIdent_Type.__name__ = "Unsigned32"
_EtsysNatBindingIcmpFwdIdent_Object = MibTableColumn
etsysNatBindingIcmpFwdIdent = _EtsysNatBindingIcmpFwdIdent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 17),
    _EtsysNatBindingIcmpFwdIdent_Type()
)
etsysNatBindingIcmpFwdIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingIcmpFwdIdent.setStatus("current")


class _EtsysNatBindingIcmpRevIdent_Type(Unsigned32):
    """Custom type etsysNatBindingIcmpRevIdent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysNatBindingIcmpRevIdent_Type.__name__ = "Unsigned32"
_EtsysNatBindingIcmpRevIdent_Object = MibTableColumn
etsysNatBindingIcmpRevIdent = _EtsysNatBindingIcmpRevIdent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 18),
    _EtsysNatBindingIcmpRevIdent_Type()
)
etsysNatBindingIcmpRevIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingIcmpRevIdent.setStatus("current")
_EtsysNatBindingHWConns_Type = Gauge32
_EtsysNatBindingHWConns_Object = MibTableColumn
etsysNatBindingHWConns = _EtsysNatBindingHWConns_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 19),
    _EtsysNatBindingHWConns_Type()
)
etsysNatBindingHWConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingHWConns.setStatus("current")
_EtsysNatBindingCreationDate_Type = DateAndTime
_EtsysNatBindingCreationDate_Object = MibTableColumn
etsysNatBindingCreationDate = _EtsysNatBindingCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 20),
    _EtsysNatBindingCreationDate_Type()
)
etsysNatBindingCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingCreationDate.setStatus("current")
_EtsysNatBindingExpirationDate_Type = DateAndTime
_EtsysNatBindingExpirationDate_Object = MibTableColumn
etsysNatBindingExpirationDate = _EtsysNatBindingExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 21),
    _EtsysNatBindingExpirationDate_Type()
)
etsysNatBindingExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingExpirationDate.setStatus("current")
_EtsysNatBindingIdleTime_Type = Unsigned32
_EtsysNatBindingIdleTime_Object = MibTableColumn
etsysNatBindingIdleTime = _EtsysNatBindingIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 22),
    _EtsysNatBindingIdleTime_Type()
)
etsysNatBindingIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatBindingIdleTime.setUnits("seconds")
_EtsysNatBindingExpireTime_Type = Unsigned32
_EtsysNatBindingExpireTime_Object = MibTableColumn
etsysNatBindingExpireTime = _EtsysNatBindingExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 23),
    _EtsysNatBindingExpireTime_Type()
)
etsysNatBindingExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNatBindingExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysNatBindingExpireTime.setUnits("seconds")


class _EtsysNatBindingClear_Type(TruthValue):
    """Custom type etsysNatBindingClear based on TruthValue"""


_EtsysNatBindingClear_Object = MibTableColumn
etsysNatBindingClear = _EtsysNatBindingClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 2, 5, 1, 24),
    _EtsysNatBindingClear_Type()
)
etsysNatBindingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysNatBindingClear.setStatus("current")
_EtsysNatConformance_ObjectIdentity = ObjectIdentity
etsysNatConformance = _EtsysNatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3)
)
_EtsysNatMIBGroups_ObjectIdentity = ObjectIdentity
etsysNatMIBGroups = _EtsysNatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1)
)
_EtsysNatMIBCompliances_ObjectIdentity = ObjectIdentity
etsysNatMIBCompliances = _EtsysNatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 2)
)

# Managed Objects groups

etsysNatMIBGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1, 1)
)
etsysNatMIBGlobalStatsGroup.setObjects(
      *(("ENTERASYS-NAT-MIB", "etsysNatStatsPoolsUsed"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsListRulesUsed"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsStaticRulesUsed"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsAddressUsed"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsPortMapsUsed"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsCurrent"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsHigh"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsDeleted"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsTotal"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsExhausted"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsMaxReached"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsNoIpAddr"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsNoPortmapPort"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsNoFtpALG"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsBindingsPerSecond"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsClear"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsClearDateAndTime"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsTranslationProtocolRulesCount"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsMinTimeoutValue"),
        ("ENTERASYS-NAT-MIB", "etsysNatStatsMaxTimeoutValue"))
)
if mibBuilder.loadTexts:
    etsysNatMIBGlobalStatsGroup.setStatus("current")

etsysNatMIBGlobalIpv4ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1, 2)
)
etsysNatMIBGlobalIpv4ConfigGroup.setObjects(
      *(("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigLogTranslations"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigInspectDNS"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigFtpCtrlPort"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigMaxEntries"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigUdpTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigTcpTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigFtpTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigDnsTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigIcmpTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigFinRstTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus"))
)
if mibBuilder.loadTexts:
    etsysNatMIBGlobalIpv4ConfigGroup.setStatus("current")

etsysNatMIBTranslationProtocolRulesTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1, 3)
)
etsysNatMIBTranslationProtocolRulesTableGroup.setObjects(
      *(("ENTERASYS-NAT-MIB", "etsysNatTranslationTimeout"),
        ("ENTERASYS-NAT-MIB", "etsysNatTranslationOneShot"),
        ("ENTERASYS-NAT-MIB", "etsysNatTranslationRowStatus"))
)
if mibBuilder.loadTexts:
    etsysNatMIBTranslationProtocolRulesTableGroup.setStatus("current")

etsysNatMIBNatPoolTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1, 4)
)
etsysNatMIBNatPoolTableGroup.setObjects(
      *(("ENTERASYS-NAT-MIB", "etsysNatPoolFirstIpAddr"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolLastIpAddr"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolPrefixLen"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolNextIpAddr"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolAddrCount"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolAddrUsed"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolAddrAlloc"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolOutOfAddrs"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolPortAlloc"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolOutOfPorts"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolConns"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolHits"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolListRulesCount"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolLsnatVservers"),
        ("ENTERASYS-NAT-MIB", "etsysNatPoolRowStatus"))
)
if mibBuilder.loadTexts:
    etsysNatMIBNatPoolTableGroup.setStatus("current")

etsysNatMIBNatListRuleTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1, 5)
)
etsysNatMIBNatListRuleTableGroup.setObjects(
      *(("ENTERASYS-NAT-MIB", "etsysNatListRulePoolName"),
        ("ENTERASYS-NAT-MIB", "etsysNatListRuleIfIndex"),
        ("ENTERASYS-NAT-MIB", "etsysNatListRuleOverloaded"),
        ("ENTERASYS-NAT-MIB", "etsysNatListRuleConns"),
        ("ENTERASYS-NAT-MIB", "etsysNatListRuleHits"),
        ("ENTERASYS-NAT-MIB", "etsysNatListRuleRowStatus"))
)
if mibBuilder.loadTexts:
    etsysNatMIBNatListRuleTableGroup.setStatus("current")

etsysNatMIBNatStaticRuleTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1, 6)
)
etsysNatMIBNatStaticRuleTableGroup.setObjects(
      *(("ENTERASYS-NAT-MIB", "etsysNatStaticRuleOverloaded"),
        ("ENTERASYS-NAT-MIB", "etsysNatStaticRuleConns"),
        ("ENTERASYS-NAT-MIB", "etsysNatStaticRuleHits"),
        ("ENTERASYS-NAT-MIB", "etsysNatStaticRuleReservedBindingId"),
        ("ENTERASYS-NAT-MIB", "etsysNatStaticRuleRowStatus"))
)
if mibBuilder.loadTexts:
    etsysNatMIBNatStaticRuleTableGroup.setStatus("current")

etsysNatMIBNatBindingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 1, 7)
)
etsysNatMIBNatBindingTableGroup.setObjects(
      *(("ENTERASYS-NAT-MIB", "etsysNatBindingState"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingAddressType"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingForwardSrcIp"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingForwardSrcPort"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingForwardDstIp"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingForwardDstPort"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingReverseSrcIp"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingReverseSrcPort"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingReverseDstIp"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingReverseDstPort"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingRuleType"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingPoolName"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingProtocol"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingAlgType"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingFtpDataChannelCount"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingIcmpFwdIdent"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingIcmpRevIdent"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingHWConns"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingCreationDate"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingExpirationDate"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingIdleTime"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingExpireTime"),
        ("ENTERASYS-NAT-MIB", "etsysNatBindingClear"))
)
if mibBuilder.loadTexts:
    etsysNatMIBNatBindingTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysNatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 75, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etsysNatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-NAT-MIB",
    **{"etsysNatMIB": etsysNatMIB,
       "etsysNatGlobal": etsysNatGlobal,
       "etsysNatGlobalStats": etsysNatGlobalStats,
       "etsysNatStatsPoolsUsed": etsysNatStatsPoolsUsed,
       "etsysNatStatsListRulesUsed": etsysNatStatsListRulesUsed,
       "etsysNatStatsStaticRulesUsed": etsysNatStatsStaticRulesUsed,
       "etsysNatStatsAddressUsed": etsysNatStatsAddressUsed,
       "etsysNatStatsPortMapsUsed": etsysNatStatsPortMapsUsed,
       "etsysNatStatsBindingsCurrent": etsysNatStatsBindingsCurrent,
       "etsysNatStatsBindingsHigh": etsysNatStatsBindingsHigh,
       "etsysNatStatsBindingsDeleted": etsysNatStatsBindingsDeleted,
       "etsysNatStatsBindingsTotal": etsysNatStatsBindingsTotal,
       "etsysNatStatsBindingsExhausted": etsysNatStatsBindingsExhausted,
       "etsysNatStatsBindingsMaxReached": etsysNatStatsBindingsMaxReached,
       "etsysNatStatsBindingsNoIpAddr": etsysNatStatsBindingsNoIpAddr,
       "etsysNatStatsBindingsNoPortmapPort": etsysNatStatsBindingsNoPortmapPort,
       "etsysNatStatsBindingsNoFtpALG": etsysNatStatsBindingsNoFtpALG,
       "etsysNatStatsBindingsPerSecond": etsysNatStatsBindingsPerSecond,
       "etsysNatStatsClear": etsysNatStatsClear,
       "etsysNatStatsClearDateAndTime": etsysNatStatsClearDateAndTime,
       "etsysNatStatsTranslationProtocolRulesCount": etsysNatStatsTranslationProtocolRulesCount,
       "etsysNatStatsMinTimeoutValue": etsysNatStatsMinTimeoutValue,
       "etsysNatStatsMaxTimeoutValue": etsysNatStatsMaxTimeoutValue,
       "etsysNatGlobalIpv4Config": etsysNatGlobalIpv4Config,
       "etsysNatIpv4ConfigLogTranslations": etsysNatIpv4ConfigLogTranslations,
       "etsysNatIpv4ConfigInspectDNS": etsysNatIpv4ConfigInspectDNS,
       "etsysNatIpv4ConfigFtpCtrlPort": etsysNatIpv4ConfigFtpCtrlPort,
       "etsysNatIpv4ConfigMaxEntries": etsysNatIpv4ConfigMaxEntries,
       "etsysNatIpv4ConfigTimeout": etsysNatIpv4ConfigTimeout,
       "etsysNatIpv4ConfigUdpTimeout": etsysNatIpv4ConfigUdpTimeout,
       "etsysNatIpv4ConfigTcpTimeout": etsysNatIpv4ConfigTcpTimeout,
       "etsysNatIpv4ConfigFtpTimeout": etsysNatIpv4ConfigFtpTimeout,
       "etsysNatIpv4ConfigDnsTimeout": etsysNatIpv4ConfigDnsTimeout,
       "etsysNatIpv4ConfigIcmpTimeout": etsysNatIpv4ConfigIcmpTimeout,
       "etsysNatIpv4ConfigFinRstTimeout": etsysNatIpv4ConfigFinRstTimeout,
       "etsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus": etsysNatIpv4ConfigFinRstTimeoutHalfClosedStatus,
       "etsysNatTables": etsysNatTables,
       "etsysNatTranslationProtocolRulesTable": etsysNatTranslationProtocolRulesTable,
       "etsysNatTranslationProtocolRulesEntry": etsysNatTranslationProtocolRulesEntry,
       "etsysNatTranslationInetVersion": etsysNatTranslationInetVersion,
       "etsysNatTranslationProtocol": etsysNatTranslationProtocol,
       "etsysNatTranslationPort": etsysNatTranslationPort,
       "etsysNatTranslationTimeout": etsysNatTranslationTimeout,
       "etsysNatTranslationOneShot": etsysNatTranslationOneShot,
       "etsysNatTranslationRowStatus": etsysNatTranslationRowStatus,
       "etsysNatPoolTable": etsysNatPoolTable,
       "etsysNatPoolEntry": etsysNatPoolEntry,
       "etsysNatPoolAddressType": etsysNatPoolAddressType,
       "etsysNatPoolName": etsysNatPoolName,
       "etsysNatPoolFirstIpAddr": etsysNatPoolFirstIpAddr,
       "etsysNatPoolLastIpAddr": etsysNatPoolLastIpAddr,
       "etsysNatPoolPrefixLen": etsysNatPoolPrefixLen,
       "etsysNatPoolNextIpAddr": etsysNatPoolNextIpAddr,
       "etsysNatPoolAddrCount": etsysNatPoolAddrCount,
       "etsysNatPoolAddrUsed": etsysNatPoolAddrUsed,
       "etsysNatPoolAddrAlloc": etsysNatPoolAddrAlloc,
       "etsysNatPoolOutOfAddrs": etsysNatPoolOutOfAddrs,
       "etsysNatPoolPortAlloc": etsysNatPoolPortAlloc,
       "etsysNatPoolOutOfPorts": etsysNatPoolOutOfPorts,
       "etsysNatPoolConns": etsysNatPoolConns,
       "etsysNatPoolHits": etsysNatPoolHits,
       "etsysNatPoolListRulesCount": etsysNatPoolListRulesCount,
       "etsysNatPoolLsnatVservers": etsysNatPoolLsnatVservers,
       "etsysNatPoolRowStatus": etsysNatPoolRowStatus,
       "etsysNatListRuleTable": etsysNatListRuleTable,
       "etsysNatListRuleEntry": etsysNatListRuleEntry,
       "etsysNatListRuleInetVersion": etsysNatListRuleInetVersion,
       "etsysNatListRuleDirection": etsysNatListRuleDirection,
       "etsysNatListRuleMatchType": etsysNatListRuleMatchType,
       "etsysNatListRuleName": etsysNatListRuleName,
       "etsysNatListRuleInsideVrfName": etsysNatListRuleInsideVrfName,
       "etsysNatListRulePoolName": etsysNatListRulePoolName,
       "etsysNatListRuleIfIndex": etsysNatListRuleIfIndex,
       "etsysNatListRuleOverloaded": etsysNatListRuleOverloaded,
       "etsysNatListRuleConns": etsysNatListRuleConns,
       "etsysNatListRuleHits": etsysNatListRuleHits,
       "etsysNatListRuleRowStatus": etsysNatListRuleRowStatus,
       "etsysNatStaticRuleTable": etsysNatStaticRuleTable,
       "etsysNatStaticRuleEntry": etsysNatStaticRuleEntry,
       "etsysNatStaticRuleAddressType": etsysNatStaticRuleAddressType,
       "etsysNatStaticRuleDirection": etsysNatStaticRuleDirection,
       "etsysNatStaticRuleMatchType": etsysNatStaticRuleMatchType,
       "etsysNatStaticRuleProtocol": etsysNatStaticRuleProtocol,
       "etsysNatStaticRuleLocalIpAddr": etsysNatStaticRuleLocalIpAddr,
       "etsysNatStaticRuleLocalPort": etsysNatStaticRuleLocalPort,
       "etsysNatStaticRuleGlobalIpAddr": etsysNatStaticRuleGlobalIpAddr,
       "etsysNatStaticRuleGlobalPort": etsysNatStaticRuleGlobalPort,
       "etsysNatStaticRuleInsideVrfName": etsysNatStaticRuleInsideVrfName,
       "etsysNatStaticRuleOverloaded": etsysNatStaticRuleOverloaded,
       "etsysNatStaticRuleConns": etsysNatStaticRuleConns,
       "etsysNatStaticRuleHits": etsysNatStaticRuleHits,
       "etsysNatStaticRuleReservedBindingId": etsysNatStaticRuleReservedBindingId,
       "etsysNatStaticRuleRowStatus": etsysNatStaticRuleRowStatus,
       "etsysNatBindingTable": etsysNatBindingTable,
       "etsysNatBindingEntry": etsysNatBindingEntry,
       "etsysNatBindingId": etsysNatBindingId,
       "etsysNatBindingState": etsysNatBindingState,
       "etsysNatBindingAddressType": etsysNatBindingAddressType,
       "etsysNatBindingForwardSrcIp": etsysNatBindingForwardSrcIp,
       "etsysNatBindingForwardSrcPort": etsysNatBindingForwardSrcPort,
       "etsysNatBindingForwardDstIp": etsysNatBindingForwardDstIp,
       "etsysNatBindingForwardDstPort": etsysNatBindingForwardDstPort,
       "etsysNatBindingReverseSrcIp": etsysNatBindingReverseSrcIp,
       "etsysNatBindingReverseSrcPort": etsysNatBindingReverseSrcPort,
       "etsysNatBindingReverseDstIp": etsysNatBindingReverseDstIp,
       "etsysNatBindingReverseDstPort": etsysNatBindingReverseDstPort,
       "etsysNatBindingRuleType": etsysNatBindingRuleType,
       "etsysNatBindingPoolName": etsysNatBindingPoolName,
       "etsysNatBindingProtocol": etsysNatBindingProtocol,
       "etsysNatBindingAlgType": etsysNatBindingAlgType,
       "etsysNatBindingFtpDataChannelCount": etsysNatBindingFtpDataChannelCount,
       "etsysNatBindingIcmpFwdIdent": etsysNatBindingIcmpFwdIdent,
       "etsysNatBindingIcmpRevIdent": etsysNatBindingIcmpRevIdent,
       "etsysNatBindingHWConns": etsysNatBindingHWConns,
       "etsysNatBindingCreationDate": etsysNatBindingCreationDate,
       "etsysNatBindingExpirationDate": etsysNatBindingExpirationDate,
       "etsysNatBindingIdleTime": etsysNatBindingIdleTime,
       "etsysNatBindingExpireTime": etsysNatBindingExpireTime,
       "etsysNatBindingClear": etsysNatBindingClear,
       "etsysNatConformance": etsysNatConformance,
       "etsysNatMIBGroups": etsysNatMIBGroups,
       "etsysNatMIBGlobalStatsGroup": etsysNatMIBGlobalStatsGroup,
       "etsysNatMIBGlobalIpv4ConfigGroup": etsysNatMIBGlobalIpv4ConfigGroup,
       "etsysNatMIBTranslationProtocolRulesTableGroup": etsysNatMIBTranslationProtocolRulesTableGroup,
       "etsysNatMIBNatPoolTableGroup": etsysNatMIBNatPoolTableGroup,
       "etsysNatMIBNatListRuleTableGroup": etsysNatMIBNatListRuleTableGroup,
       "etsysNatMIBNatStaticRuleTableGroup": etsysNatMIBNatStaticRuleTableGroup,
       "etsysNatMIBNatBindingTableGroup": etsysNatMIBNatBindingTableGroup,
       "etsysNatMIBCompliances": etsysNatMIBCompliances,
       "etsysNatMIBCompliance": etsysNatMIBCompliance}
)
