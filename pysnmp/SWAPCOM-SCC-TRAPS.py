# SNMP MIB module (SWAPCOM-SCC-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWAPCOM-SCC-TRAPS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:07 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")

(alarmProbeAlertSource,
 alarmProbeAlertType,
 alarmProbeSeverity) = mibBuilder.importSymbols(
    "SWAPCOM-SCC",
    "alarmProbeAlertSource",
    "alarmProbeAlertType",
    "alarmProbeSeverity")


# MODULE-IDENTITY

swapcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11308)
)
swapcom.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_SccTraps_ObjectIdentity = ObjectIdentity
sccTraps = _SccTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 4)
)

# Managed Objects groups


# Notification objects

sqlPoolUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 4, 1)
)
sqlPoolUnavailable.setObjects(
      *(("SWAPCOM-SCC", "alarmProbeAlertType"),
        ("SWAPCOM-SCC", "alarmProbeAlertSource"),
        ("SWAPCOM-SCC", "alarmProbeSeverity"))
)
if mibBuilder.loadTexts:
    sqlPoolUnavailable.setStatus(
        "current"
    )

sqlPoolHighCheckedOutConnections = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 4, 2)
)
sqlPoolHighCheckedOutConnections.setObjects(
      *(("SWAPCOM-SCC", "alarmProbeAlertType"),
        ("SWAPCOM-SCC", "alarmProbeAlertSource"),
        ("SWAPCOM-SCC", "alarmProbeSeverity"))
)
if mibBuilder.loadTexts:
    sqlPoolHighCheckedOutConnections.setStatus(
        "current"
    )

slsUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 4, 3)
)
slsUnavailable.setObjects(
      *(("SWAPCOM-SCC", "alarmProbeAlertType"),
        ("SWAPCOM-SCC", "alarmProbeAlertSource"),
        ("SWAPCOM-SCC", "alarmProbeSeverity"))
)
if mibBuilder.loadTexts:
    slsUnavailable.setStatus(
        "current"
    )

remotePlatformUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 4, 4)
)
remotePlatformUnavailable.setObjects(
      *(("SWAPCOM-SCC", "alarmProbeAlertType"),
        ("SWAPCOM-SCC", "alarmProbeAlertSource"),
        ("SWAPCOM-SCC", "alarmProbeSeverity"))
)
if mibBuilder.loadTexts:
    remotePlatformUnavailable.setStatus(
        "current"
    )

schedulerTaskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11308, 4, 5)
)
schedulerTaskError.setObjects(
      *(("SWAPCOM-SCC", "alarmProbeAlertType"),
        ("SWAPCOM-SCC", "alarmProbeAlertSource"),
        ("SWAPCOM-SCC", "alarmProbeSeverity"))
)
if mibBuilder.loadTexts:
    schedulerTaskError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWAPCOM-SCC-TRAPS",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "swapcom": swapcom,
       "sccTraps": sccTraps,
       "sqlPoolUnavailable": sqlPoolUnavailable,
       "sqlPoolHighCheckedOutConnections": sqlPoolHighCheckedOutConnections,
       "slsUnavailable": slsUnavailable,
       "remotePlatformUnavailable": remotePlatformUnavailable,
       "schedulerTaskError": schedulerTaskError}
)
