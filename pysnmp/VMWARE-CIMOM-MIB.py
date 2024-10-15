# SNMP MIB module (VMWARE-CIMOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-CIMOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:48 2024
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

(vmwEnvIndicationTime,) = mibBuilder.importSymbols(
    "VMWARE-ENV-MIB",
    "vmwEnvIndicationTime")

(vmwProductSpecific,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwProductSpecific")


# MODULE-IDENTITY

vmwCIMOMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 10)
)
vmwCIMOMMIB.setRevisions(
        ("2010-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwCimOm_ObjectIdentity = ObjectIdentity
vmwCimOm = _VmwCimOm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90)
)
_VmwCimOmNotifications_ObjectIdentity = ObjectIdentity
vmwCimOmNotifications = _VmwCimOmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 0)
)
_VmwCimOmMIBConformance_ObjectIdentity = ObjectIdentity
vmwCimOmMIBConformance = _VmwCimOmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2)
)
_VmwCimOmMIBCompliances_ObjectIdentity = ObjectIdentity
vmwCimOmMIBCompliances = _VmwCimOmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1)
)
_VmwCimOmMIBGroups_ObjectIdentity = ObjectIdentity
vmwCimOmMIBGroups = _VmwCimOmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2)
)

# Managed Objects groups


# Notification objects

vmwCimOmHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 0, 401)
)
vmwCimOmHeartbeat.setObjects(
    ("VMWARE-ENV-MIB", "vmwEnvIndicationTime")
)
if mibBuilder.loadTexts:
    vmwCimOmHeartbeat.setStatus(
        "current"
    )


# Notifications groups

vmwCimOmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2, 2)
)
vmwCimOmNotificationGroup.setObjects(
    ("VMWARE-CIMOM-MIB", "vmwCimOmHeartbeat")
)
if mibBuilder.loadTexts:
    vmwCimOmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwCimOmMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1, 4)
)
if mibBuilder.loadTexts:
    vmwCimOmMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-CIMOM-MIB",
    **{"vmwCimOm": vmwCimOm,
       "vmwCimOmNotifications": vmwCimOmNotifications,
       "vmwCimOmHeartbeat": vmwCimOmHeartbeat,
       "vmwCimOmMIBConformance": vmwCimOmMIBConformance,
       "vmwCimOmMIBCompliances": vmwCimOmMIBCompliances,
       "vmwCimOmMIBBasicCompliance": vmwCimOmMIBBasicCompliance,
       "vmwCimOmMIBGroups": vmwCimOmMIBGroups,
       "vmwCimOmNotificationGroup": vmwCimOmNotificationGroup,
       "vmwCIMOMMIB": vmwCIMOMMIB}
)
