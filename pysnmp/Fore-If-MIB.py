# SNMP MIB module (Fore-If-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-If-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:03 2024
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

(foreIfExtension,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "foreIfExtension")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

foreIfModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 15, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ForeIfGroup_ObjectIdentity = ObjectIdentity
foreIfGroup = _ForeIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 15, 2)
)
_ForeIfTable_Object = MibTable
foreIfTable = _ForeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    foreIfTable.setStatus("current")
_ForeIfEntry_Object = MibTableRow
foreIfEntry = _ForeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 15, 2, 1, 1)
)
foreIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreIfEntry.setStatus("current")
_ForeIfMtu_Type = Integer32
_ForeIfMtu_Object = MibTableColumn
foreIfMtu = _ForeIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 15, 2, 1, 1, 1),
    _ForeIfMtu_Type()
)
foreIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreIfMtu.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-If-MIB",
    **{"foreIfModule": foreIfModule,
       "foreIfGroup": foreIfGroup,
       "foreIfTable": foreIfTable,
       "foreIfEntry": foreIfEntry,
       "foreIfMtu": foreIfMtu}
)
