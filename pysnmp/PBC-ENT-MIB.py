# SNMP MIB module (PBC-ENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PBC-ENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:59 2024
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

pacificBroadband = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5987)
)
pacificBroadband.setRevisions(
        ("2002-10-08 12:38",
         "2002-09-25 17:30",
         "2002-09-23 18:47")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PbcRegs_ObjectIdentity = ObjectIdentity
pbcRegs = _PbcRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 1)
)
if mibBuilder.loadTexts:
    pbcRegs.setStatus("current")
_PbcModuleRegs_ObjectIdentity = ObjectIdentity
pbcModuleRegs = _PbcModuleRegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 1, 1)
)
if mibBuilder.loadTexts:
    pbcModuleRegs.setStatus("current")
_PbcManagement_ObjectIdentity = ObjectIdentity
pbcManagement = _PbcManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 2)
)
if mibBuilder.loadTexts:
    pbcManagement.setStatus("current")
_PbcProducts_ObjectIdentity = ObjectIdentity
pbcProducts = _PbcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 3)
)
if mibBuilder.loadTexts:
    pbcProducts.setStatus("current")
_PbcCaps_ObjectIdentity = ObjectIdentity
pbcCaps = _PbcCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 4)
)
if mibBuilder.loadTexts:
    pbcCaps.setStatus("current")
_PbcReqs_ObjectIdentity = ObjectIdentity
pbcReqs = _PbcReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 5)
)
if mibBuilder.loadTexts:
    pbcReqs.setStatus("current")
_PbcExpr_ObjectIdentity = ObjectIdentity
pbcExpr = _PbcExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5987, 6)
)
if mibBuilder.loadTexts:
    pbcExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PBC-ENT-MIB",
    **{"pacificBroadband": pacificBroadband,
       "pbcRegs": pbcRegs,
       "pbcModuleRegs": pbcModuleRegs,
       "pbcManagement": pbcManagement,
       "pbcProducts": pbcProducts,
       "pbcCaps": pbcCaps,
       "pbcReqs": pbcReqs,
       "pbcExpr": pbcExpr}
)
