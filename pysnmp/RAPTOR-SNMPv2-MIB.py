# SNMP MIB module (RAPTOR-SNMPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPTOR-SNMPv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:43 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

raptorNotify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1294, 1, 1)
)
raptorNotify.setRevisions(
        ("1998-10-27 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaptorSystems_ObjectIdentity = ObjectIdentity
raptorSystems = _RaptorSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1294)
)
_RaptorModules_ObjectIdentity = ObjectIdentity
raptorModules = _RaptorModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1294, 1)
)
_RaptorObjects_ObjectIdentity = ObjectIdentity
raptorObjects = _RaptorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1294, 2)
)
_RaptorNotifyMessage_Type = OctetString
_RaptorNotifyMessage_Object = MibScalar
raptorNotifyMessage = _RaptorNotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 1294, 2, 1),
    _RaptorNotifyMessage_Type()
)
raptorNotifyMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raptorNotifyMessage.setStatus("current")
_RaptorTraps_ObjectIdentity = ObjectIdentity
raptorTraps = _RaptorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1294, 3)
)

# Managed Objects groups


# Notification objects

raptorNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1294, 3, 1)
)
raptorNotifyTrap.setObjects(
    ("RAPTOR-SNMPv2-MIB", "raptorNotifyMessage")
)
if mibBuilder.loadTexts:
    raptorNotifyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPTOR-SNMPv2-MIB",
    **{"raptorSystems": raptorSystems,
       "raptorModules": raptorModules,
       "raptorNotify": raptorNotify,
       "raptorObjects": raptorObjects,
       "raptorNotifyMessage": raptorNotifyMessage,
       "raptorTraps": raptorTraps,
       "raptorNotifyTrap": raptorNotifyTrap}
)
