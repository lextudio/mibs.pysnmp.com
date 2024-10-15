# SNMP MIB module (ELTEX-MES-SWITCH-RATE-LIMITER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-SWITCH-RATE-LIMITER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:01 2024
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

(eltMesSwitchRateLimiterMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesSwitchRateLimiterMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EltCpuRateLimiterTrafficType(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("ace", 17),
          ("arp", 7),
          ("arpInspec", 8),
          ("dhcpSnoop", 13),
          ("dhcpv6Snoop", 20),
          ("http", 1),
          ("igmpSnoop", 14),
          ("ip", 5),
          ("ipErrors", 18),
          ("ipOptions", 12),
          ("ipRouting", 11),
          ("linkLocal", 6),
          ("mldSnoop", 15),
          ("other", 19),
          ("otherBpdu", 10),
          ("sflow", 16),
          ("snmp", 4),
          ("ssh", 3),
          ("stpBpdu", 9),
          ("telnet", 2),
          ("vrrp", 21))
    )



class EltCpuRateStatisticsTrafficType(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("arp", 7),
          ("arpInspec", 8),
          ("dhcpSnooping", 16),
          ("dhcpv6Snooping", 25),
          ("http", 2),
          ("ieee", 10),
          ("igmpSnooping", 17),
          ("ip", 6),
          ("ipDaMismatch", 22),
          ("ipHopByHop", 12),
          ("ipv4HeaderError", 21),
          ("ipv4IllegalAddress", 20),
          ("ipv4Multicast", 14),
          ("ipv6HeaderError", 28),
          ("ipv6Multicast", 15),
          ("logDenyAces", 24),
          ("logPermitAces", 27),
          ("mldSnooping", 18),
          ("mtuExceeded", 13),
          ("routeUnknown", 11),
          ("sflow", 23),
          ("snmp", 5),
          ("ssh", 4),
          ("stack", 1),
          ("stp", 9),
          ("telnet", 3),
          ("ttlExceeded", 19),
          ("vrrp", 26))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesSwitchRateLimiterObjects_ObjectIdentity = ObjectIdentity
eltMesSwitchRateLimiterObjects = _EltMesSwitchRateLimiterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1)
)
_EltMesSwitchRateLimiterConfig_ObjectIdentity = ObjectIdentity
eltMesSwitchRateLimiterConfig = _EltMesSwitchRateLimiterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1)
)
_EltCpuRateLimiterTable_Object = MibTable
eltCpuRateLimiterTable = _EltCpuRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltCpuRateLimiterTable.setStatus("current")
_EltCpuRateLimiterEntry_Object = MibTableRow
eltCpuRateLimiterEntry = _EltCpuRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1)
)
eltCpuRateLimiterEntry.setIndexNames(
    (0, "ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateLimiterIndex"),
)
if mibBuilder.loadTexts:
    eltCpuRateLimiterEntry.setStatus("current")
_EltCpuRateLimiterIndex_Type = EltCpuRateLimiterTrafficType
_EltCpuRateLimiterIndex_Object = MibTableColumn
eltCpuRateLimiterIndex = _EltCpuRateLimiterIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1, 1),
    _EltCpuRateLimiterIndex_Type()
)
eltCpuRateLimiterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateLimiterIndex.setStatus("current")


class _EltCpuRateLimiterValue_Type(Integer32):
    """Custom type eltCpuRateLimiterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltCpuRateLimiterValue_Type.__name__ = "Integer32"
_EltCpuRateLimiterValue_Object = MibTableColumn
eltCpuRateLimiterValue = _EltCpuRateLimiterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1, 2),
    _EltCpuRateLimiterValue_Type()
)
eltCpuRateLimiterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCpuRateLimiterValue.setStatus("current")
_EltMesSwitchRateLimiterStatistics_ObjectIdentity = ObjectIdentity
eltMesSwitchRateLimiterStatistics = _EltMesSwitchRateLimiterStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2)
)
_EltCpuRateStatisticsTable_Object = MibTable
eltCpuRateStatisticsTable = _EltCpuRateStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltCpuRateStatisticsTable.setStatus("current")
_EltCpuRateStatisticsEntry_Object = MibTableRow
eltCpuRateStatisticsEntry = _EltCpuRateStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1)
)
eltCpuRateStatisticsEntry.setIndexNames(
    (0, "ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateStatisticsIndex"),
)
if mibBuilder.loadTexts:
    eltCpuRateStatisticsEntry.setStatus("current")
_EltCpuRateStatisticsIndex_Type = EltCpuRateStatisticsTrafficType
_EltCpuRateStatisticsIndex_Object = MibTableColumn
eltCpuRateStatisticsIndex = _EltCpuRateStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 1),
    _EltCpuRateStatisticsIndex_Type()
)
eltCpuRateStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateStatisticsIndex.setStatus("current")
_EltCpuRateStatisticsRate_Type = Gauge32
_EltCpuRateStatisticsRate_Object = MibTableColumn
eltCpuRateStatisticsRate = _EltCpuRateStatisticsRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 2),
    _EltCpuRateStatisticsRate_Type()
)
eltCpuRateStatisticsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateStatisticsRate.setStatus("current")
_EltCpuRateStatisticsCounter_Type = Counter32
_EltCpuRateStatisticsCounter_Object = MibTableColumn
eltCpuRateStatisticsCounter = _EltCpuRateStatisticsCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 3),
    _EltCpuRateStatisticsCounter_Type()
)
eltCpuRateStatisticsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateStatisticsCounter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-SWITCH-RATE-LIMITER-MIB",
    **{"EltCpuRateLimiterTrafficType": EltCpuRateLimiterTrafficType,
       "EltCpuRateStatisticsTrafficType": EltCpuRateStatisticsTrafficType,
       "eltMesSwitchRateLimiterObjects": eltMesSwitchRateLimiterObjects,
       "eltMesSwitchRateLimiterConfig": eltMesSwitchRateLimiterConfig,
       "eltCpuRateLimiterTable": eltCpuRateLimiterTable,
       "eltCpuRateLimiterEntry": eltCpuRateLimiterEntry,
       "eltCpuRateLimiterIndex": eltCpuRateLimiterIndex,
       "eltCpuRateLimiterValue": eltCpuRateLimiterValue,
       "eltMesSwitchRateLimiterStatistics": eltMesSwitchRateLimiterStatistics,
       "eltCpuRateStatisticsTable": eltCpuRateStatisticsTable,
       "eltCpuRateStatisticsEntry": eltCpuRateStatisticsEntry,
       "eltCpuRateStatisticsIndex": eltCpuRateStatisticsIndex,
       "eltCpuRateStatisticsRate": eltCpuRateStatisticsRate,
       "eltCpuRateStatisticsCounter": eltCpuRateStatisticsCounter}
)
