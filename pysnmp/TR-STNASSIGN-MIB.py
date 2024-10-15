# SNMP MIB module (TR-STNASSIGN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TR-STNASSIGN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:17 2024
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

(ctTRStnAssign,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctTRStnAssign")

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

_StnInterfaceCount_Type = Integer32
_StnInterfaceCount_Object = MibScalar
stnInterfaceCount = _StnInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 1),
    _StnInterfaceCount_Type()
)
stnInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnInterfaceCount.setStatus("mandatory")
_StnAssignTable_Object = MibTable
stnAssignTable = _StnAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    stnAssignTable.setStatus("mandatory")
_StnAssignTableEntry_Object = MibTableRow
stnAssignTableEntry = _StnAssignTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1)
)
stnAssignTableEntry.setIndexNames(
    (0, "TR-STNASSIGN-MIB", "stnAssignIndex"),
)
if mibBuilder.loadTexts:
    stnAssignTableEntry.setStatus("mandatory")
_StnAssignIndex_Type = Integer32
_StnAssignIndex_Object = MibTableColumn
stnAssignIndex = _StnAssignIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1, 1),
    _StnAssignIndex_Type()
)
stnAssignIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAssignIndex.setStatus("mandatory")
_StnAssignPortAssociation_Type = ObjectIdentifier
_StnAssignPortAssociation_Object = MibTableColumn
stnAssignPortAssociation = _StnAssignPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1, 2),
    _StnAssignPortAssociation_Type()
)
stnAssignPortAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnAssignPortAssociation.setStatus("mandatory")


class _StnAssignPortRing_Type(Integer32):
    """Custom type stnAssignPortRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StnAssignPortRing_Type.__name__ = "Integer32"
_StnAssignPortRing_Object = MibTableColumn
stnAssignPortRing = _StnAssignPortRing_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1, 3),
    _StnAssignPortRing_Type()
)
stnAssignPortRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnAssignPortRing.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TR-STNASSIGN-MIB",
    **{"stnInterfaceCount": stnInterfaceCount,
       "stnAssignTable": stnAssignTable,
       "stnAssignTableEntry": stnAssignTableEntry,
       "stnAssignIndex": stnAssignIndex,
       "stnAssignPortAssociation": stnAssignPortAssociation,
       "stnAssignPortRing": stnAssignPortRing}
)
