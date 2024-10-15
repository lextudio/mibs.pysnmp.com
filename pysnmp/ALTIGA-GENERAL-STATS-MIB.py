# SNMP MIB module (ALTIGA-GENERAL-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-GENERAL-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:11 2024
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

(alGeneralMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alGeneralMibModule")

(alGeneralGroup,
 alStatsGeneral) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alGeneralGroup",
    "alStatsGeneral")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

altigaGeneralStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2)
)
altigaGeneralStatsMibModule.setRevisions(
        ("2002-09-11 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaGeneralStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaGeneralStatsMibConformance = _AltigaGeneralStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1)
)
_AltigaGeneralStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaGeneralStatsMibCompliances = _AltigaGeneralStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1)
)
_AlStatsGeneralGlobal_ObjectIdentity = ObjectIdentity
alStatsGeneralGlobal = _AlStatsGeneralGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1)
)
_AlGeneralTime_Type = Counter32
_AlGeneralTime_Object = MibScalar
alGeneralTime = _AlGeneralTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 1),
    _AlGeneralTime_Type()
)
alGeneralTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGeneralTime.setStatus("current")


class _AlGeneralGaugeCpuUtil_Type(Gauge32):
    """Custom type alGeneralGaugeCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlGeneralGaugeCpuUtil_Type.__name__ = "Gauge32"
_AlGeneralGaugeCpuUtil_Object = MibScalar
alGeneralGaugeCpuUtil = _AlGeneralGaugeCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 2),
    _AlGeneralGaugeCpuUtil_Type()
)
alGeneralGaugeCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGeneralGaugeCpuUtil.setStatus("current")


class _AlGeneralGaugeActiveSessions_Type(Gauge32):
    """Custom type alGeneralGaugeActiveSessions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlGeneralGaugeActiveSessions_Type.__name__ = "Gauge32"
_AlGeneralGaugeActiveSessions_Object = MibScalar
alGeneralGaugeActiveSessions = _AlGeneralGaugeActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 3),
    _AlGeneralGaugeActiveSessions_Type()
)
alGeneralGaugeActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGeneralGaugeActiveSessions.setStatus("current")


class _AlGeneralGaugeThroughput_Type(Gauge32):
    """Custom type alGeneralGaugeThroughput based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlGeneralGaugeThroughput_Type.__name__ = "Gauge32"
_AlGeneralGaugeThroughput_Object = MibScalar
alGeneralGaugeThroughput = _AlGeneralGaugeThroughput_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 4),
    _AlGeneralGaugeThroughput_Type()
)
alGeneralGaugeThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGeneralGaugeThroughput.setStatus("current")
_AlGeneralTimeZone_Type = Integer32
_AlGeneralTimeZone_Object = MibScalar
alGeneralTimeZone = _AlGeneralTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 25, 1, 5),
    _AlGeneralTimeZone_Type()
)
alGeneralTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alGeneralTimeZone.setStatus("current")

# Managed Objects groups

altigaGeneralStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 25, 2)
)
altigaGeneralStatsGroup.setObjects(
      *(("ALTIGA-GENERAL-STATS-MIB", "alGeneralTime"),
        ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeCpuUtil"),
        ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeActiveSessions"),
        ("ALTIGA-GENERAL-STATS-MIB", "alGeneralGaugeThroughput"),
        ("ALTIGA-GENERAL-STATS-MIB", "alGeneralTimeZone"))
)
if mibBuilder.loadTexts:
    altigaGeneralStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaGeneralStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 30, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaGeneralStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-GENERAL-STATS-MIB",
    **{"altigaGeneralStatsMibModule": altigaGeneralStatsMibModule,
       "altigaGeneralStatsMibConformance": altigaGeneralStatsMibConformance,
       "altigaGeneralStatsMibCompliances": altigaGeneralStatsMibCompliances,
       "altigaGeneralStatsMibCompliance": altigaGeneralStatsMibCompliance,
       "altigaGeneralStatsGroup": altigaGeneralStatsGroup,
       "alStatsGeneralGlobal": alStatsGeneralGlobal,
       "alGeneralTime": alGeneralTime,
       "alGeneralGaugeCpuUtil": alGeneralGaugeCpuUtil,
       "alGeneralGaugeActiveSessions": alGeneralGaugeActiveSessions,
       "alGeneralGaugeThroughput": alGeneralGaugeThroughput,
       "alGeneralTimeZone": alGeneralTimeZone}
)
