# SNMP MIB module (SW3810PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW3810PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:43 2024
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

(dlink_mgmt,
 dlink_products) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-mgmt",
    "dlink-products")

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

_Dlink_Des3810Series_ObjectIdentity = ObjectIdentity
dlink_Des3810Series = _Dlink_Des3810Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114)
)
_Des3810_ObjectIdentity = ObjectIdentity
des3810 = _Des3810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1)
)
_Des3810_28_ObjectIdentity = ObjectIdentity
des3810_28 = _Des3810_28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1)
)
_Des3810_28DC_ObjectIdentity = ObjectIdentity
des3810_28DC = _Des3810_28DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 2)
)
_Des3810_52_ObjectIdentity = ObjectIdentity
des3810_52 = _Des3810_52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3810PRIMGMT-MIB",
    **{"dlink-Des3810Series": dlink_Des3810Series,
       "des3810": des3810,
       "des3810-28": des3810_28,
       "des3810-28DC": des3810_28DC,
       "des3810-52": des3810_52}
)
