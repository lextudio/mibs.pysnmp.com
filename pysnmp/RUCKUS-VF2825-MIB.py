# SNMP MIB module (RUCKUS-VF2825-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-VF2825-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:50 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruckusVF2825,) = mibBuilder.importSymbols(
    "RUCKUS-PRODUCTS-MIB",
    "ruckusVF2825")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ruckusVF2825MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusVF2825Objects_ObjectIdentity = ObjectIdentity
ruckusVF2825Objects = _RuckusVF2825Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 1)
)
_RuckusVF2825Info_ObjectIdentity = ObjectIdentity
ruckusVF2825Info = _RuckusVF2825Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 1, 1)
)
_RuckusVF2825NetworkTable_Object = MibTable
ruckusVF2825NetworkTable = _RuckusVF2825NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusVF2825NetworkTable.setStatus("current")
_RuckusVF2825NetworkEntry_Object = MibTableRow
ruckusVF2825NetworkEntry = _RuckusVF2825NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 1, 1, 1, 1)
)
ruckusVF2825NetworkEntry.setIndexNames(
    (0, "RUCKUS-VF2825-MIB", "ruckusVF2825NetworkName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusVF2825NetworkEntry.setStatus("current")


class _RuckusVF2825NetworkName_Type(DisplayString):
    """Custom type ruckusVF2825NetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RuckusVF2825NetworkName_Type.__name__ = "DisplayString"
_RuckusVF2825NetworkName_Object = MibTableColumn
ruckusVF2825NetworkName = _RuckusVF2825NetworkName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    _RuckusVF2825NetworkName_Type()
)
ruckusVF2825NetworkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusVF2825NetworkName.setStatus("current")


class _RuckusVF2825NetworkIfName_Type(DisplayString):
    """Custom type ruckusVF2825NetworkIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RuckusVF2825NetworkIfName_Type.__name__ = "DisplayString"
_RuckusVF2825NetworkIfName_Object = MibTableColumn
ruckusVF2825NetworkIfName = _RuckusVF2825NetworkIfName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2),
    _RuckusVF2825NetworkIfName_Type()
)
ruckusVF2825NetworkIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusVF2825NetworkIfName.setStatus("current")
_RuckusVF2825Events_ObjectIdentity = ObjectIdentity
ruckusVF2825Events = _RuckusVF2825Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 2)
)
_RuckusVF2825Conf_ObjectIdentity = ObjectIdentity
ruckusVF2825Conf = _RuckusVF2825Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 3)
)
_RuckusVF2825Groups_ObjectIdentity = ObjectIdentity
ruckusVF2825Groups = _RuckusVF2825Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1, 1, 3, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-VF2825-MIB",
    **{"ruckusVF2825MIB": ruckusVF2825MIB,
       "ruckusVF2825Objects": ruckusVF2825Objects,
       "ruckusVF2825Info": ruckusVF2825Info,
       "ruckusVF2825NetworkTable": ruckusVF2825NetworkTable,
       "ruckusVF2825NetworkEntry": ruckusVF2825NetworkEntry,
       "ruckusVF2825NetworkName": ruckusVF2825NetworkName,
       "ruckusVF2825NetworkIfName": ruckusVF2825NetworkIfName,
       "ruckusVF2825Events": ruckusVF2825Events,
       "ruckusVF2825Conf": ruckusVF2825Conf,
       "ruckusVF2825Groups": ruckusVF2825Groups}
)
