# SNMP MIB module (VMWARE-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-PRODUCTS-MIB
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

(vmwOID,
 vmwProductSpecific) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwOID",
    "vmwProductSpecific")


# MODULE-IDENTITY

vmwProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 11)
)
vmwProducts.setRevisions(
        ("2015-07-17 00:00",
         "2014-09-19 00:00",
         "2011-09-29 00:00",
         "2007-07-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwESX_ObjectIdentity = ObjectIdentity
vmwESX = _VmwESX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1)
)
_VmwDVS_ObjectIdentity = ObjectIdentity
vmwDVS = _VmwDVS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 2)
)
_VmwVC_ObjectIdentity = ObjectIdentity
vmwVC = _VmwVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3)
)
_VmwServer_ObjectIdentity = ObjectIdentity
vmwServer = _VmwServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 4)
)
_VmwVCOps_ObjectIdentity = ObjectIdentity
vmwVCOps = _VmwVCOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 5)
)
_VmwGenericAppliance_ObjectIdentity = ObjectIdentity
vmwGenericAppliance = _VmwGenericAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 6)
)
_VmwEmbeddedVirtualCenterAppliance_ObjectIdentity = ObjectIdentity
vmwEmbeddedVirtualCenterAppliance = _VmwEmbeddedVirtualCenterAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 7)
)
_VmwInfrastructureAppliance_ObjectIdentity = ObjectIdentity
vmwInfrastructureAppliance = _VmwInfrastructureAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 8)
)
_VmwManagementAppliance_ObjectIdentity = ObjectIdentity
vmwManagementAppliance = _VmwManagementAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 9)
)
_VmwNSX_ObjectIdentity = ObjectIdentity
vmwNSX = _VmwNSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 10)
)
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
    "VMWARE-PRODUCTS-MIB",
    **{"vmwESX": vmwESX,
       "vmwDVS": vmwDVS,
       "vmwVC": vmwVC,
       "vmwServer": vmwServer,
       "vmwVCOps": vmwVCOps,
       "vmwGenericAppliance": vmwGenericAppliance,
       "vmwEmbeddedVirtualCenterAppliance": vmwEmbeddedVirtualCenterAppliance,
       "vmwInfrastructureAppliance": vmwInfrastructureAppliance,
       "vmwManagementAppliance": vmwManagementAppliance,
       "vmwNSX": vmwNSX,
       "vmwProducts": vmwProducts,
       "oidESX": oidESX}
)
