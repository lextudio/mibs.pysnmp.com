# SNMP MIB module (ALTIGA-VERSION-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-VERSION-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:26 2024
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

(alVersionMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alVersionMibModule")

(alStatsVersion,
 alVersionGroup) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alStatsVersion",
    "alVersionGroup")

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

altigaVersionStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2)
)
altigaVersionStatsMibModule.setRevisions(
        ("2002-09-05 13:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaVersionStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaVersionStatsMibConformance = _AltigaVersionStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1)
)
_AltigaVersionStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaVersionStatsMibCompliances = _AltigaVersionStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1)
)
_AlStatsVersionGlobal_ObjectIdentity = ObjectIdentity
alStatsVersionGlobal = _AlStatsVersionGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1)
)
_AlVersionMajor_Type = Unsigned32
_AlVersionMajor_Object = MibScalar
alVersionMajor = _AlVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 1),
    _AlVersionMajor_Type()
)
alVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVersionMajor.setStatus("current")
_AlVersionMinor_Type = Unsigned32
_AlVersionMinor_Object = MibScalar
alVersionMinor = _AlVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 2),
    _AlVersionMinor_Type()
)
alVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVersionMinor.setStatus("current")
_AlVersionInt_Type = DisplayString
_AlVersionInt_Object = MibScalar
alVersionInt = _AlVersionInt_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 3),
    _AlVersionInt_Type()
)
alVersionInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVersionInt.setStatus("current")
_AlVersionString_Type = DisplayString
_AlVersionString_Object = MibScalar
alVersionString = _AlVersionString_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 4),
    _AlVersionString_Type()
)
alVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVersionString.setStatus("current")
_AlVersionLong_Type = DisplayString
_AlVersionLong_Object = MibScalar
alVersionLong = _AlVersionLong_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 5),
    _AlVersionLong_Type()
)
alVersionLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVersionLong.setStatus("current")
_AlVersionShort_Type = DisplayString
_AlVersionShort_Object = MibScalar
alVersionShort = _AlVersionShort_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 6),
    _AlVersionShort_Type()
)
alVersionShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVersionShort.setStatus("current")
_AlVersionBoot_Type = DisplayString
_AlVersionBoot_Object = MibScalar
alVersionBoot = _AlVersionBoot_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 1, 1, 7),
    _AlVersionBoot_Type()
)
alVersionBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVersionBoot.setStatus("current")

# Managed Objects groups

altigaVersionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 1, 2)
)
altigaVersionStatsGroup.setObjects(
      *(("ALTIGA-VERSION-STATS-MIB", "alVersionMajor"),
        ("ALTIGA-VERSION-STATS-MIB", "alVersionMinor"),
        ("ALTIGA-VERSION-STATS-MIB", "alVersionInt"),
        ("ALTIGA-VERSION-STATS-MIB", "alVersionString"),
        ("ALTIGA-VERSION-STATS-MIB", "alVersionLong"),
        ("ALTIGA-VERSION-STATS-MIB", "alVersionShort"),
        ("ALTIGA-VERSION-STATS-MIB", "alVersionBoot"))
)
if mibBuilder.loadTexts:
    altigaVersionStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaVersionStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 6, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaVersionStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-VERSION-STATS-MIB",
    **{"altigaVersionStatsMibModule": altigaVersionStatsMibModule,
       "altigaVersionStatsMibConformance": altigaVersionStatsMibConformance,
       "altigaVersionStatsMibCompliances": altigaVersionStatsMibCompliances,
       "altigaVersionStatsMibCompliance": altigaVersionStatsMibCompliance,
       "altigaVersionStatsGroup": altigaVersionStatsGroup,
       "alStatsVersionGlobal": alStatsVersionGlobal,
       "alVersionMajor": alVersionMajor,
       "alVersionMinor": alVersionMinor,
       "alVersionInt": alVersionInt,
       "alVersionString": alVersionString,
       "alVersionLong": alVersionLong,
       "alVersionShort": alVersionShort,
       "alVersionBoot": alVersionBoot}
)
