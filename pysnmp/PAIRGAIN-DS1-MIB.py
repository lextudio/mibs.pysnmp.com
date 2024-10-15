# SNMP MIB module (PAIRGAIN-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:18 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pgds1Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pgds1MibObjects_ObjectIdentity = ObjectIdentity
pgds1MibObjects = _Pgds1MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1)
)
_Pgds1ConfigTable_Object = MibTable
pgds1ConfigTable = _Pgds1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1)
)
if mibBuilder.loadTexts:
    pgds1ConfigTable.setStatus("current")
_Pgds1ConfigEntry_Object = MibTableRow
pgds1ConfigEntry = _Pgds1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1)
)
pgds1ConfigEntry.setIndexNames(
    (0, "PAIRGAIN-DS1-MIB", "pgds1LineIndex"),
)
if mibBuilder.loadTexts:
    pgds1ConfigEntry.setStatus("current")
_Pgds1LineIndex_Type = InterfaceIndex
_Pgds1LineIndex_Object = MibTableColumn
pgds1LineIndex = _Pgds1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 1),
    _Pgds1LineIndex_Type()
)
pgds1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgds1LineIndex.setStatus("current")
_Pgds1IfIndex_Type = InterfaceIndex
_Pgds1IfIndex_Object = MibTableColumn
pgds1IfIndex = _Pgds1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 2),
    _Pgds1IfIndex_Type()
)
pgds1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgds1IfIndex.setStatus("deprecated")


class _Pgds1LineBuildout_Type(Integer32):
    """Custom type pgds1LineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Pgds1LineBuildout_Type.__name__ = "Integer32"
_Pgds1LineBuildout_Object = MibTableColumn
pgds1LineBuildout = _Pgds1LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 17, 1, 1, 1, 3),
    _Pgds1LineBuildout_Type()
)
pgds1LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgds1LineBuildout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-DS1-MIB",
    **{"pgds1Mib": pgds1Mib,
       "pgds1MibObjects": pgds1MibObjects,
       "pgds1ConfigTable": pgds1ConfigTable,
       "pgds1ConfigEntry": pgds1ConfigEntry,
       "pgds1LineIndex": pgds1LineIndex,
       "pgds1IfIndex": pgds1IfIndex,
       "pgds1LineBuildout": pgds1LineBuildout}
)
