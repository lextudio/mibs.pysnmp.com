# SNMP MIB module (VMWARE-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:47 2024
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

vmware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876)
)
vmware.setRevisions(
        ("2016-01-02 20:00",
         "2010-04-02 00:00",
         "2007-07-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwNotifications_ObjectIdentity = ObjectIdentity
vmwNotifications = _VmwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 0)
)
if mibBuilder.loadTexts:
    vmwNotifications.setStatus("current")
_VmwSystem_ObjectIdentity = ObjectIdentity
vmwSystem = _VmwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1)
)
if mibBuilder.loadTexts:
    vmwSystem.setStatus("current")
_VmwVirtMachines_ObjectIdentity = ObjectIdentity
vmwVirtMachines = _VmwVirtMachines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 2)
)
if mibBuilder.loadTexts:
    vmwVirtMachines.setStatus("current")
_VmwResources_ObjectIdentity = ObjectIdentity
vmwResources = _VmwResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 3)
)
if mibBuilder.loadTexts:
    vmwResources.setStatus("current")
_VmwProductSpecific_ObjectIdentity = ObjectIdentity
vmwProductSpecific = _VmwProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4)
)
if mibBuilder.loadTexts:
    vmwProductSpecific.setStatus("current")
_VmwLdap_ObjectIdentity = ObjectIdentity
vmwLdap = _VmwLdap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 40)
)
if mibBuilder.loadTexts:
    vmwLdap.setStatus("current")
_VmwTraps_ObjectIdentity = ObjectIdentity
vmwTraps = _VmwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 50)
)
if mibBuilder.loadTexts:
    vmwTraps.setStatus("current")
_VmwSRM_ObjectIdentity = ObjectIdentity
vmwSRM = _VmwSRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 51)
)
if mibBuilder.loadTexts:
    vmwSRM.setStatus("current")
_VmwVCHA_ObjectIdentity = ObjectIdentity
vmwVCHA = _VmwVCHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 53)
)
if mibBuilder.loadTexts:
    vmwVCHA.setStatus("current")
_VmwOID_ObjectIdentity = ObjectIdentity
vmwOID = _VmwOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 60)
)
if mibBuilder.loadTexts:
    vmwOID.setStatus("deprecated")
_VmwareAgentCapabilities_ObjectIdentity = ObjectIdentity
vmwareAgentCapabilities = _VmwareAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70)
)
if mibBuilder.loadTexts:
    vmwareAgentCapabilities.setStatus("current")
_VmwNsxManager_ObjectIdentity = ObjectIdentity
vmwNsxManager = _VmwNsxManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 90)
)
if mibBuilder.loadTexts:
    vmwNsxManager.setStatus("current")
_VmwExperimental_ObjectIdentity = ObjectIdentity
vmwExperimental = _VmwExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 700)
)
if mibBuilder.loadTexts:
    vmwExperimental.setStatus("current")
_VmwDocumentation_ObjectIdentity = ObjectIdentity
vmwDocumentation = _VmwDocumentation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 750)
)
if mibBuilder.loadTexts:
    vmwDocumentation.setStatus("current")
_VmwObsolete_ObjectIdentity = ObjectIdentity
vmwObsolete = _VmwObsolete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 800)
)
if mibBuilder.loadTexts:
    vmwObsolete.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-ROOT-MIB",
    **{"vmware": vmware,
       "vmwNotifications": vmwNotifications,
       "vmwSystem": vmwSystem,
       "vmwVirtMachines": vmwVirtMachines,
       "vmwResources": vmwResources,
       "vmwProductSpecific": vmwProductSpecific,
       "vmwLdap": vmwLdap,
       "vmwTraps": vmwTraps,
       "vmwSRM": vmwSRM,
       "vmwVCHA": vmwVCHA,
       "vmwOID": vmwOID,
       "vmwareAgentCapabilities": vmwareAgentCapabilities,
       "vmwNsxManager": vmwNsxManager,
       "vmwExperimental": vmwExperimental,
       "vmwDocumentation": vmwDocumentation,
       "vmwObsolete": vmwObsolete}
)
