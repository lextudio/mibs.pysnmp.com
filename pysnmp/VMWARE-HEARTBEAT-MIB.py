# SNMP MIB module (VMWARE-HEARTBEAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-HEARTBEAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:51 2024
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

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

(vmwProductSpecific,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwProductSpecific")


# MODULE-IDENTITY

vmwHBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 66)
)
vmwHBMIB.setRevisions(
        ("2016-02-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwHb_ObjectIdentity = ObjectIdentity
vmwHb = _VmwHb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190)
)
_VmwHbNotifications_ObjectIdentity = ObjectIdentity
vmwHbNotifications = _VmwHbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 0)
)
_VmwHbMIBConformance_ObjectIdentity = ObjectIdentity
vmwHbMIBConformance = _VmwHbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2)
)
_VmwHbMIBCompliances_ObjectIdentity = ObjectIdentity
vmwHbMIBCompliances = _VmwHbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1)
)
_VmwHbMIBGroups_ObjectIdentity = ObjectIdentity
vmwHbMIBGroups = _VmwHbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2)
)

# Managed Objects groups


# Notification objects

vmwHbHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 0, 401)
)
vmwHbHeartbeat.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    vmwHbHeartbeat.setStatus(
        "current"
    )


# Notifications groups

vmwHbNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 2, 2)
)
vmwHbNotificationGroup.setObjects(
    ("VMWARE-HEARTBEAT-MIB", "vmwHbHeartbeat")
)
if mibBuilder.loadTexts:
    vmwHbNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwHbMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 190, 2, 1, 4)
)
if mibBuilder.loadTexts:
    vmwHbMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-HEARTBEAT-MIB",
    **{"vmwHb": vmwHb,
       "vmwHbNotifications": vmwHbNotifications,
       "vmwHbHeartbeat": vmwHbHeartbeat,
       "vmwHbMIBConformance": vmwHbMIBConformance,
       "vmwHbMIBCompliances": vmwHbMIBCompliances,
       "vmwHbMIBBasicCompliance": vmwHbMIBBasicCompliance,
       "vmwHbMIBGroups": vmwHbMIBGroups,
       "vmwHbNotificationGroup": vmwHbNotificationGroup,
       "vmwHBMIB": vmwHBMIB}
)
