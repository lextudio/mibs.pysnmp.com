# SNMP MIB module (VMWARE-ESX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-ESX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:50 2024
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

(vmwOID,
 vmwProductSpecific) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwOID",
    "vmwProductSpecific")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwESX_ObjectIdentity = ObjectIdentity
vmwESX = _VmwESX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1)
)
_EsxVMKernel_ObjectIdentity = ObjectIdentity
esxVMKernel = _EsxVMKernel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 1)
)
_VmkLoaded_Type = DisplayString
_VmkLoaded_Object = MibScalar
vmkLoaded = _VmkLoaded_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 1, 1),
    _VmkLoaded_Type()
)
vmkLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmkLoaded.setStatus("mandatory")
_OidESX_ObjectIdentity = ObjectIdentity
oidESX = _OidESX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 60, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-ESX-MIB",
    **{"vmwESX": vmwESX,
       "esxVMKernel": esxVMKernel,
       "vmkLoaded": vmkLoaded,
       "oidESX": oidESX}
)
