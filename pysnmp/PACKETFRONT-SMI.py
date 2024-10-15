# SNMP MIB module (PACKETFRONT-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETFRONT-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:04 2024
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

packetfront = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303)
)
packetfront.setRevisions(
        ("2009-03-23 10:39",
         "2008-01-17 14:05",
         "2007-05-11 12:28")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PfProduct_ObjectIdentity = ObjectIdentity
pfProduct = _PfProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1)
)
if mibBuilder.loadTexts:
    pfProduct.setStatus("current")
_PfConfig_ObjectIdentity = ObjectIdentity
pfConfig = _PfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 2)
)
if mibBuilder.loadTexts:
    pfConfig.setStatus("current")
_IpdConfig_ObjectIdentity = ObjectIdentity
ipdConfig = _IpdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 2, 1)
)
if mibBuilder.loadTexts:
    ipdConfig.setStatus("current")
_PfExperiment_ObjectIdentity = ObjectIdentity
pfExperiment = _PfExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 3)
)
if mibBuilder.loadTexts:
    pfExperiment.setStatus("current")
_PfMgmt_ObjectIdentity = ObjectIdentity
pfMgmt = _PfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4)
)
if mibBuilder.loadTexts:
    pfMgmt.setStatus("current")
_PfModules_ObjectIdentity = ObjectIdentity
pfModules = _PfModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 5)
)
if mibBuilder.loadTexts:
    pfModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFRONT-SMI",
    **{"packetfront": packetfront,
       "pfProduct": pfProduct,
       "pfConfig": pfConfig,
       "ipdConfig": ipdConfig,
       "pfExperiment": pfExperiment,
       "pfMgmt": pfMgmt,
       "pfModules": pfModules}
)
