# SNMP MIB module (FORCE10-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORCE10-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:14 2024
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

force10 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027)
)
force10.setRevisions(
        ("2007-06-15 12:00",
         "1900-10-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10Products_ObjectIdentity = ObjectIdentity
f10Products = _F10Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1)
)
if mibBuilder.loadTexts:
    f10Products.setStatus("current")
_F10Common_ObjectIdentity = ObjectIdentity
f10Common = _F10Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 2)
)
if mibBuilder.loadTexts:
    f10Common.setStatus("current")
_F10Mgmt_ObjectIdentity = ObjectIdentity
f10Mgmt = _F10Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3)
)
if mibBuilder.loadTexts:
    f10Mgmt.setStatus("current")
_F10Modules_ObjectIdentity = ObjectIdentity
f10Modules = _F10Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 4)
)
if mibBuilder.loadTexts:
    f10Modules.setStatus("current")
_F10Experiment_ObjectIdentity = ObjectIdentity
f10Experiment = _F10Experiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20)
)
if mibBuilder.loadTexts:
    f10Experiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-SMI",
    **{"force10": force10,
       "f10Products": f10Products,
       "f10Common": f10Common,
       "f10Mgmt": f10Mgmt,
       "f10Modules": f10Modules,
       "f10Experiment": f10Experiment}
)
