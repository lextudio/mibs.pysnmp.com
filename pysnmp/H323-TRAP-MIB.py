# SNMP MIB module (H323-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H323-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:43 2024
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

(code,
 comment,
 csID,
 csType,
 gwID,
 gwIP,
 gwType,
 moduleID,
 percent,
 port,
 reason,
 registrationStatus,
 timeOccurred) = mibBuilder.importSymbols(
    "AGGREGATED-EXT-MIB",
    "code",
    "comment",
    "csID",
    "csType",
    "gwID",
    "gwIP",
    "gwType",
    "moduleID",
    "percent",
    "port",
    "reason",
    "registrationStatus",
    "timeOccurred")

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
 ObjectName,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

h323Traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_SoftSwitch_ObjectIdentity = ObjectIdentity
softSwitch = _SoftSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)
_H323DeviceServer_ObjectIdentity = ObjectIdentity
h323DeviceServer = _H323DeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3)
)

# Managed Objects groups


# Notification objects

h323CSConnectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 0)
)
h323CSConnectionStatus.setObjects(
      *(("AGGREGATED-EXT-MIB", "timeOccurred"),
        ("AGGREGATED-EXT-MIB", "code"),
        ("AGGREGATED-EXT-MIB", "csID"),
        ("AGGREGATED-EXT-MIB", "csType"),
        ("AGGREGATED-EXT-MIB", "registrationStatus"),
        ("AGGREGATED-EXT-MIB", "reason"),
        ("AGGREGATED-EXT-MIB", "comment"))
)
if mibBuilder.loadTexts:
    h323CSConnectionStatus.setStatus(
        "current"
    )

h323GatewayUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 1)
)
h323GatewayUtilization.setObjects(
      *(("AGGREGATED-EXT-MIB", "timeOccurred"),
        ("AGGREGATED-EXT-MIB", "code"),
        ("AGGREGATED-EXT-MIB", "gwID"),
        ("AGGREGATED-EXT-MIB", "moduleID"),
        ("AGGREGATED-EXT-MIB", "percent"),
        ("AGGREGATED-EXT-MIB", "comment"))
)
if mibBuilder.loadTexts:
    h323GatewayUtilization.setStatus(
        "current"
    )

h323DSError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 2)
)
h323DSError.setObjects(
      *(("AGGREGATED-EXT-MIB", "timeOccurred"),
        ("AGGREGATED-EXT-MIB", "code"),
        ("AGGREGATED-EXT-MIB", "reason"),
        ("AGGREGATED-EXT-MIB", "comment"))
)
if mibBuilder.loadTexts:
    h323DSError.setStatus(
        "current"
    )

h323UnreachableGateway = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 3)
)
h323UnreachableGateway.setObjects(
      *(("AGGREGATED-EXT-MIB", "timeOccurred"),
        ("AGGREGATED-EXT-MIB", "code"),
        ("AGGREGATED-EXT-MIB", "gwID"),
        ("AGGREGATED-EXT-MIB", "gwType"),
        ("AGGREGATED-EXT-MIB", "gwIP"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "comment"))
)
if mibBuilder.loadTexts:
    h323UnreachableGateway.setStatus(
        "current"
    )

h323CommandFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 3, 0, 4)
)
h323CommandFailed.setObjects(
      *(("AGGREGATED-EXT-MIB", "timeOccurred"),
        ("AGGREGATED-EXT-MIB", "code"),
        ("AGGREGATED-EXT-MIB", "reason"),
        ("AGGREGATED-EXT-MIB", "comment"))
)
if mibBuilder.loadTexts:
    h323CommandFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H323-TRAP-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "h323DeviceServer": h323DeviceServer,
       "h323Traps": h323Traps,
       "h323CSConnectionStatus": h323CSConnectionStatus,
       "h323GatewayUtilization": h323GatewayUtilization,
       "h323DSError": h323DSError,
       "h323UnreachableGateway": h323UnreachableGateway,
       "h323CommandFailed": h323CommandFailed}
)
