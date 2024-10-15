# SNMP MIB module (NMS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:36 2024
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

(pbn,) = mibBuilder.importSymbols(
    "PBN-ROOT",
    "pbn")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nms_ObjectIdentity = ObjectIdentity
nms = _Nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10)
)
if mibBuilder.loadTexts:
    nms.setStatus("current")
_NmsProducts_ObjectIdentity = ObjectIdentity
nmsProducts = _NmsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 1)
)
if mibBuilder.loadTexts:
    nmsProducts.setStatus("current")
_Nmslocal_ObjectIdentity = ObjectIdentity
nmslocal = _Nmslocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2)
)
if mibBuilder.loadTexts:
    nmslocal.setStatus("current")
_Nmstemporary_ObjectIdentity = ObjectIdentity
nmstemporary = _Nmstemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 3)
)
if mibBuilder.loadTexts:
    nmstemporary.setStatus("current")
_NmsMgmt_ObjectIdentity = ObjectIdentity
nmsMgmt = _NmsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9)
)
if mibBuilder.loadTexts:
    nmsMgmt.setStatus("current")
_NmsModules_ObjectIdentity = ObjectIdentity
nmsModules = _NmsModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 12)
)
if mibBuilder.loadTexts:
    nmsModules.setStatus("current")
_NmsPolicyAuto_ObjectIdentity = ObjectIdentity
nmsPolicyAuto = _NmsPolicyAuto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 18)
)
if mibBuilder.loadTexts:
    nmsPolicyAuto.setStatus("current")
_NmsPibToMib_ObjectIdentity = ObjectIdentity
nmsPibToMib = _NmsPibToMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 18, 2)
)
if mibBuilder.loadTexts:
    nmsPibToMib.setStatus("current")
_NmsWorkGroup_ObjectIdentity = ObjectIdentity
nmsWorkGroup = _NmsWorkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 20)
)
if mibBuilder.loadTexts:
    nmsWorkGroup.setStatus("current")
_NmsEPONGroup_ObjectIdentity = ObjectIdentity
nmsEPONGroup = _NmsEPONGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101)
)
if mibBuilder.loadTexts:
    nmsEPONGroup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-SMI",
    **{"nms": nms,
       "nmsProducts": nmsProducts,
       "nmslocal": nmslocal,
       "nmstemporary": nmstemporary,
       "nmsMgmt": nmsMgmt,
       "nmsModules": nmsModules,
       "nmsPolicyAuto": nmsPolicyAuto,
       "nmsPibToMib": nmsPibToMib,
       "nmsWorkGroup": nmsWorkGroup,
       "nmsEPONGroup": nmsEPONGroup}
)
