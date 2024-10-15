# SNMP MIB module (JUNIPER-WX-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-WX-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:29 2024
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

(jnxWxMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxWxMibRoot")

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

jnxWxGrpModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWxGrp_ObjectIdentity = ObjectIdentity
jnxWxGrp = _JnxWxGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrp.setStatus("current")
_JnxWxGrpStatus_ObjectIdentity = ObjectIdentity
jnxWxGrpStatus = _JnxWxGrpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpStatus.setStatus("current")
_JnxWxGrpStats_ObjectIdentity = ObjectIdentity
jnxWxGrpStats = _JnxWxGrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpStats.setStatus("current")
_JnxWxGrpEvents_ObjectIdentity = ObjectIdentity
jnxWxGrpEvents = _JnxWxGrpEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxWxGrpEvents.setStatus("current")
_JnxWxGrpConf_ObjectIdentity = ObjectIdentity
jnxWxGrpConf = _JnxWxGrpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxWxGrpConf.setStatus("current")
_JnxWxGrpProduct_ObjectIdentity = ObjectIdentity
jnxWxGrpProduct = _JnxWxGrpProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxWxGrpProduct.setStatus("current")
_JnxWxGrpProductWxc250_ObjectIdentity = ObjectIdentity
jnxWxGrpProductWxc250 = _JnxWxGrpProductWxc250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpProductWxc250.setStatus("current")
_JnxWxGrpProductWxc500_ObjectIdentity = ObjectIdentity
jnxWxGrpProductWxc500 = _JnxWxGrpProductWxc500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpProductWxc500.setStatus("current")
_JnxWxGrpProductWxc590_ObjectIdentity = ObjectIdentity
jnxWxGrpProductWxc590 = _JnxWxGrpProductWxc590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    jnxWxGrpProductWxc590.setStatus("current")
_JnxWxGrpProductWxc1800_ObjectIdentity = ObjectIdentity
jnxWxGrpProductWxc1800 = _JnxWxGrpProductWxc1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    jnxWxGrpProductWxc1800.setStatus("current")
_JnxWxGrpProductWxc2600_ObjectIdentity = ObjectIdentity
jnxWxGrpProductWxc2600 = _JnxWxGrpProductWxc2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    jnxWxGrpProductWxc2600.setStatus("current")
_JnxWxGrpProductWxc3400_ObjectIdentity = ObjectIdentity
jnxWxGrpProductWxc3400 = _JnxWxGrpProductWxc3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    jnxWxGrpProductWxc3400.setStatus("current")
_JnxWxGrpProductWxc7800_ObjectIdentity = ObjectIdentity
jnxWxGrpProductWxc7800 = _JnxWxGrpProductWxc7800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    jnxWxGrpProductWxc7800.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-GLOBAL-MIB",
    **{"jnxWxGrpModule": jnxWxGrpModule,
       "jnxWxGrp": jnxWxGrp,
       "jnxWxGrpStatus": jnxWxGrpStatus,
       "jnxWxGrpStats": jnxWxGrpStats,
       "jnxWxGrpEvents": jnxWxGrpEvents,
       "jnxWxGrpConf": jnxWxGrpConf,
       "jnxWxGrpProduct": jnxWxGrpProduct,
       "jnxWxGrpProductWxc250": jnxWxGrpProductWxc250,
       "jnxWxGrpProductWxc500": jnxWxGrpProductWxc500,
       "jnxWxGrpProductWxc590": jnxWxGrpProductWxc590,
       "jnxWxGrpProductWxc1800": jnxWxGrpProductWxc1800,
       "jnxWxGrpProductWxc2600": jnxWxGrpProductWxc2600,
       "jnxWxGrpProductWxc3400": jnxWxGrpProductWxc3400,
       "jnxWxGrpProductWxc7800": jnxWxGrpProductWxc7800}
)
