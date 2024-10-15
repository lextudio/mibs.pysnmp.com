# SNMP MIB module (VMWARE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:56 2024
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

(vmwSystem,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwSystem")


# MODULE-IDENTITY

vmwSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10)
)
vmwSystemMIB.setRevisions(
        ("2010-08-02 00:00",
         "2008-01-12 00:00",
         "2007-12-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwProdName_Type = DisplayString
_VmwProdName_Object = MibScalar
vmwProdName = _VmwProdName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 1),
    _VmwProdName_Type()
)
vmwProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdName.setStatus("current")
_VmwProdVersion_Type = DisplayString
_VmwProdVersion_Object = MibScalar
vmwProdVersion = _VmwProdVersion_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 2),
    _VmwProdVersion_Type()
)
vmwProdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdVersion.setStatus("current")
_VmwProdBuild_Type = DisplayString
_VmwProdBuild_Object = MibScalar
vmwProdBuild = _VmwProdBuild_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 4),
    _VmwProdBuild_Type()
)
vmwProdBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdBuild.setStatus("current")
_VmwProdUpdate_Type = DisplayString
_VmwProdUpdate_Object = MibScalar
vmwProdUpdate = _VmwProdUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 5),
    _VmwProdUpdate_Type()
)
vmwProdUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdUpdate.setStatus("current")
_VmwProdPatch_Type = DisplayString
_VmwProdPatch_Object = MibScalar
vmwProdPatch = _VmwProdPatch_Object(
    (1, 3, 6, 1, 4, 1, 6876, 1, 6),
    _VmwProdPatch_Type()
)
vmwProdPatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwProdPatch.setStatus("current")
_VmwSystemMIBConformance_ObjectIdentity = ObjectIdentity
vmwSystemMIBConformance = _VmwSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2)
)
_VmwSystemMIBCompliances_ObjectIdentity = ObjectIdentity
vmwSystemMIBCompliances = _VmwSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1)
)
_VmwSysMIBGroups_ObjectIdentity = ObjectIdentity
vmwSysMIBGroups = _VmwSysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2)
)

# Managed Objects groups

vmwSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2, 1)
)
vmwSystemGroup.setObjects(
      *(("VMWARE-SYSTEM-MIB", "vmwProdName"),
        ("VMWARE-SYSTEM-MIB", "vmwProdVersion"),
        ("VMWARE-SYSTEM-MIB", "vmwProdBuild"),
        ("VMWARE-SYSTEM-MIB", "vmwProdUpdate"),
        ("VMWARE-SYSTEM-MIB", "vmwProdPatch"))
)
if mibBuilder.loadTexts:
    vmwSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vmwSysMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vmwSysMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-SYSTEM-MIB",
    **{"vmwProdName": vmwProdName,
       "vmwProdVersion": vmwProdVersion,
       "vmwProdBuild": vmwProdBuild,
       "vmwProdUpdate": vmwProdUpdate,
       "vmwProdPatch": vmwProdPatch,
       "vmwSystemMIB": vmwSystemMIB,
       "vmwSystemMIBConformance": vmwSystemMIBConformance,
       "vmwSystemMIBCompliances": vmwSystemMIBCompliances,
       "vmwSysMIBBasicCompliance": vmwSysMIBBasicCompliance,
       "vmwSysMIBGroups": vmwSysMIBGroups,
       "vmwSystemGroup": vmwSystemGroup}
)
