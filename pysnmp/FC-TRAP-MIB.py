# SNMP MIB module (FC-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FC-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:24 2024
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

(devName,
 pepName,
 sbProducerHost,
 sbProducerPort) = mibBuilder.importSymbols(
    "AGGREGATED-EXT-MIB",
    "devName",
    "pepName",
    "sbProducerHost",
    "sbProducerPort")

(fCApp,
 fCDescText,
 fCServer) = mibBuilder.importSymbols(
    "FC-DS1-MIB",
    "fCApp",
    "fCDescText",
    "fCServer")

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

fcTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0)
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
_FcDeviceServer_ObjectIdentity = ObjectIdentity
fcDeviceServer = _FcDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9)
)

# Managed Objects groups


# Notification objects

fcSwitchRegnError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 1)
)
fcSwitchRegnError.setObjects(
    ("FC-DS1-MIB", "fCServer")
)
if mibBuilder.loadTexts:
    fcSwitchRegnError.setStatus(
        "current"
    )

fCSwitchRegnSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 2)
)
fCSwitchRegnSucc.setObjects(
    ("FC-DS1-MIB", "fCServer")
)
if mibBuilder.loadTexts:
    fCSwitchRegnSucc.setStatus(
        "current"
    )

fcAddLLCNodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 3)
)
fcAddLLCNodeError.setObjects(
    ("FC-DS1-MIB", "fCServer")
)
if mibBuilder.loadTexts:
    fcAddLLCNodeError.setStatus(
        "current"
    )

fcAddLLCNodeSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 4)
)
fcAddLLCNodeSucc.setObjects(
    ("FC-DS1-MIB", "fCServer")
)
if mibBuilder.loadTexts:
    fcAddLLCNodeSucc.setStatus(
        "current"
    )

fcAppStartSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 5)
)
fcAppStartSucc.setObjects(
      *(("FC-DS1-MIB", "fCServer"),
        ("FC-DS1-MIB", "fCApp"))
)
if mibBuilder.loadTexts:
    fcAppStartSucc.setStatus(
        "current"
    )

fcAppEndSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 6)
)
fcAppEndSucc.setObjects(
      *(("FC-DS1-MIB", "fCServer"),
        ("FC-DS1-MIB", "fCApp"))
)
if mibBuilder.loadTexts:
    fcAppEndSucc.setStatus(
        "current"
    )

fcAppStartError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 7)
)
fcAppStartError.setObjects(
      *(("FC-DS1-MIB", "fCServer"),
        ("FC-DS1-MIB", "fCApp"))
)
if mibBuilder.loadTexts:
    fcAppStartError.setStatus(
        "current"
    )

fcAppInfoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 8)
)
fcAppInfoError.setObjects(
      *(("FC-DS1-MIB", "fCServer"),
        ("FC-DS1-MIB", "fCApp"),
        ("FC-DS1-MIB", "fCDescText"))
)
if mibBuilder.loadTexts:
    fcAppInfoError.setStatus(
        "current"
    )

fcAppMajorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 9)
)
fcAppMajorError.setObjects(
      *(("FC-DS1-MIB", "fCServer"),
        ("FC-DS1-MIB", "fCApp"),
        ("FC-DS1-MIB", "fCDescText"))
)
if mibBuilder.loadTexts:
    fcAppMajorError.setStatus(
        "current"
    )

fcAppCritError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 10)
)
fcAppCritError.setObjects(
      *(("FC-DS1-MIB", "fCServer"),
        ("FC-DS1-MIB", "fCApp"),
        ("FC-DS1-MIB", "fCDescText"))
)
if mibBuilder.loadTexts:
    fcAppCritError.setStatus(
        "current"
    )

fcUnparsedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 9, 0, 11)
)
fcUnparsedEvent.setObjects(
    ("FC-DS1-MIB", "fCDescText")
)
if mibBuilder.loadTexts:
    fcUnparsedEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FC-TRAP-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "fcDeviceServer": fcDeviceServer,
       "fcTraps": fcTraps,
       "fcSwitchRegnError": fcSwitchRegnError,
       "fCSwitchRegnSucc": fCSwitchRegnSucc,
       "fcAddLLCNodeError": fcAddLLCNodeError,
       "fcAddLLCNodeSucc": fcAddLLCNodeSucc,
       "fcAppStartSucc": fcAppStartSucc,
       "fcAppEndSucc": fcAppEndSucc,
       "fcAppStartError": fcAppStartError,
       "fcAppInfoError": fcAppInfoError,
       "fcAppMajorError": fcAppMajorError,
       "fcAppCritError": fcAppCritError,
       "fcUnparsedEvent": fcUnparsedEvent}
)
