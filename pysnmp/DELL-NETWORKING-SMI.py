# SNMP MIB module (DELL-NETWORKING-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:47 2024
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

dellNet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027)
)
dellNet.setRevisions(
        ("2007-06-15 12:00",
         "1900-10-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetProducts_ObjectIdentity = ObjectIdentity
dellNetProducts = _DellNetProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1)
)
if mibBuilder.loadTexts:
    dellNetProducts.setStatus("current")
_DellNetCommon_ObjectIdentity = ObjectIdentity
dellNetCommon = _DellNetCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 2)
)
if mibBuilder.loadTexts:
    dellNetCommon.setStatus("current")
_DellNetMgmt_ObjectIdentity = ObjectIdentity
dellNetMgmt = _DellNetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3)
)
if mibBuilder.loadTexts:
    dellNetMgmt.setStatus("current")
_DellNetModules_ObjectIdentity = ObjectIdentity
dellNetModules = _DellNetModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 4)
)
if mibBuilder.loadTexts:
    dellNetModules.setStatus("current")
_DellNetExperiment_ObjectIdentity = ObjectIdentity
dellNetExperiment = _DellNetExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20)
)
if mibBuilder.loadTexts:
    dellNetExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-SMI",
    **{"dellNet": dellNet,
       "dellNetProducts": dellNetProducts,
       "dellNetCommon": dellNetCommon,
       "dellNetMgmt": dellNetMgmt,
       "dellNetModules": dellNetModules,
       "dellNetExperiment": dellNetExperiment}
)
