# SNMP MIB module (SPINS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SPINS-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:24 2024
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

spinsTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0)
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
_SpinsDeviceServer_ObjectIdentity = ObjectIdentity
spinsDeviceServer = _SpinsDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8)
)

# Managed Objects groups


# Notification objects

spinsSmbiSocketConnError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0, 0)
)
if mibBuilder.loadTexts:
    spinsSmbiSocketConnError.setStatus(
        "current"
    )

spinsSmbiSocketConnOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0, 1)
)
if mibBuilder.loadTexts:
    spinsSmbiSocketConnOpen.setStatus(
        "current"
    )

spinsSbiSocketConnLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0, 2)
)
if mibBuilder.loadTexts:
    spinsSbiSocketConnLost.setStatus(
        "current"
    )

spinsSwitchRegnError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0, 3)
)
if mibBuilder.loadTexts:
    spinsSwitchRegnError.setStatus(
        "current"
    )

spinsSwitchRegnSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0, 4)
)
if mibBuilder.loadTexts:
    spinsSwitchRegnSucc.setStatus(
        "current"
    )

spinsAddLLCNodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0, 5)
)
if mibBuilder.loadTexts:
    spinsAddLLCNodeError.setStatus(
        "current"
    )

spinsAddLLCNodeSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 8, 0, 6)
)
if mibBuilder.loadTexts:
    spinsAddLLCNodeSucc.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPINS-TRAP-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "spinsDeviceServer": spinsDeviceServer,
       "spinsTraps": spinsTraps,
       "spinsSmbiSocketConnError": spinsSmbiSocketConnError,
       "spinsSmbiSocketConnOpen": spinsSmbiSocketConnOpen,
       "spinsSbiSocketConnLost": spinsSbiSocketConnLost,
       "spinsSwitchRegnError": spinsSwitchRegnError,
       "spinsSwitchRegnSucc": spinsSwitchRegnSucc,
       "spinsAddLLCNodeError": spinsAddLLCNodeError,
       "spinsAddLLCNodeSucc": spinsAddLLCNodeSucc}
)
