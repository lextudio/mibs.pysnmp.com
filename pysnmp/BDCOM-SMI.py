# SNMP MIB module (BDCOM-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:32 2024
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

bdcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BdcomProducts_ObjectIdentity = ObjectIdentity
bdcomProducts = _BdcomProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 1)
)
if mibBuilder.loadTexts:
    bdcomProducts.setStatus("current")
_Bdlocal_ObjectIdentity = ObjectIdentity
bdlocal = _Bdlocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 2)
)
if mibBuilder.loadTexts:
    bdlocal.setStatus("current")
_Bdtemporary_ObjectIdentity = ObjectIdentity
bdtemporary = _Bdtemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 3)
)
if mibBuilder.loadTexts:
    bdtemporary.setStatus("current")
_BdMgmt_ObjectIdentity = ObjectIdentity
bdMgmt = _BdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9)
)
if mibBuilder.loadTexts:
    bdMgmt.setStatus("current")
_BdcomModules_ObjectIdentity = ObjectIdentity
bdcomModules = _BdcomModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 12)
)
if mibBuilder.loadTexts:
    bdcomModules.setStatus("current")
_BdcomPolicyAuto_ObjectIdentity = ObjectIdentity
bdcomPolicyAuto = _BdcomPolicyAuto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18)
)
if mibBuilder.loadTexts:
    bdcomPolicyAuto.setStatus("current")
_BdcomPibToMib_ObjectIdentity = ObjectIdentity
bdcomPibToMib = _BdcomPibToMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 18, 2)
)
if mibBuilder.loadTexts:
    bdcomPibToMib.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-SMI",
    **{"bdcom": bdcom,
       "bdcomProducts": bdcomProducts,
       "bdlocal": bdlocal,
       "bdtemporary": bdtemporary,
       "bdMgmt": bdMgmt,
       "bdcomModules": bdcomModules,
       "bdcomPolicyAuto": bdcomPolicyAuto,
       "bdcomPibToMib": bdcomPibToMib}
)
