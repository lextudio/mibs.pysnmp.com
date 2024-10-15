# SNMP MIB module (VIDEOFRAME-REGISTRATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-REGISTRATIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:29 2024
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

vfReg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 1)
)
vfReg.setRevisions(
        ("1901-01-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Videoframe_ObjectIdentity = ObjectIdentity
videoframe = _Videoframe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596)
)
if mibBuilder.loadTexts:
    videoframe.setStatus("current")
_VfGeneric_ObjectIdentity = ObjectIdentity
vfGeneric = _VfGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 3)
)
if mibBuilder.loadTexts:
    vfGeneric.setStatus("current")
_VfProducts_ObjectIdentity = ObjectIdentity
vfProducts = _VfProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4)
)
if mibBuilder.loadTexts:
    vfProducts.setStatus("current")
_VfExperimental_ObjectIdentity = ObjectIdentity
vfExperimental = _VfExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 5)
)
if mibBuilder.loadTexts:
    vfExperimental.setStatus("current")
_VfRegistrations_ObjectIdentity = ObjectIdentity
vfRegistrations = _VfRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6)
)
if mibBuilder.loadTexts:
    vfRegistrations.setStatus("current")
_VfMIBModules_ObjectIdentity = ObjectIdentity
vfMIBModules = _VfMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1)
)
if mibBuilder.loadTexts:
    vfMIBModules.setStatus("current")
_VfProductsReg_ObjectIdentity = ObjectIdentity
vfProductsReg = _VfProductsReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2)
)
if mibBuilder.loadTexts:
    vfProductsReg.setStatus("current")
_VfProductsRMCReg_ObjectIdentity = ObjectIdentity
vfProductsRMCReg = _VfProductsRMCReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vfProductsRMCReg.setStatus("current")
_VfProductsSAPSCtlReg_ObjectIdentity = ObjectIdentity
vfProductsSAPSCtlReg = _VfProductsSAPSCtlReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 2)
)
if mibBuilder.loadTexts:
    vfProductsSAPSCtlReg.setStatus("current")
_VfProductsGPIAgentReg_ObjectIdentity = ObjectIdentity
vfProductsGPIAgentReg = _VfProductsGPIAgentReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 3)
)
if mibBuilder.loadTexts:
    vfProductsGPIAgentReg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-REGISTRATIONS-MIB",
    **{"videoframe": videoframe,
       "vfGeneric": vfGeneric,
       "vfProducts": vfProducts,
       "vfExperimental": vfExperimental,
       "vfRegistrations": vfRegistrations,
       "vfMIBModules": vfMIBModules,
       "vfReg": vfReg,
       "vfProductsReg": vfProductsReg,
       "vfProductsRMCReg": vfProductsRMCReg,
       "vfProductsSAPSCtlReg": vfProductsSAPSCtlReg,
       "vfProductsGPIAgentReg": vfProductsGPIAgentReg}
)
