# SNMP MIB module (TUBS-LINUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUBS-LINUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:58 2024
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

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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
 RowStatus,
 TAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

linuxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LinuxAgents_ObjectIdentity = ObjectIdentity
linuxAgents = _LinuxAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 1)
)
_LinuxMIBObjects_ObjectIdentity = ObjectIdentity
linuxMIBObjects = _LinuxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 2)
)
_LinuxCPU_Type = DisplayString
_LinuxCPU_Object = MibScalar
linuxCPU = _LinuxCPU_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 1),
    _LinuxCPU_Type()
)
linuxCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linuxCPU.setStatus("current")
_LinuxBogo_Type = Gauge32
_LinuxBogo_Object = MibScalar
linuxBogo = _LinuxBogo_Object(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 2),
    _LinuxBogo_Type()
)
linuxBogo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linuxBogo.setStatus("current")
_LinuxMIBConformance_ObjectIdentity = ObjectIdentity
linuxMIBConformance = _LinuxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 3)
)
_LinuxMIBCompliances_ObjectIdentity = ObjectIdentity
linuxMIBCompliances = _LinuxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 1)
)
_LinuxMIBGroups_ObjectIdentity = ObjectIdentity
linuxMIBGroups = _LinuxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

linuxAgent3dot1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 1575, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    linuxAgent3dot1.setProductRelease("cmu-snmp-linux-3.1")
if mibBuilder.loadTexts:
    linuxAgent3dot1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUBS-LINUX-MIB",
    **{"linuxMIB": linuxMIB,
       "linuxAgents": linuxAgents,
       "linuxAgent3dot1": linuxAgent3dot1,
       "linuxMIBObjects": linuxMIBObjects,
       "linuxCPU": linuxCPU,
       "linuxBogo": linuxBogo,
       "linuxMIBConformance": linuxMIBConformance,
       "linuxMIBCompliances": linuxMIBCompliances,
       "linuxMIBGroups": linuxMIBGroups}
)
