# SNMP MIB module (HP-SN-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:43 2024
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

(snIgmp,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snIgmp")

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

_SnIgmpMIBObjects_ObjectIdentity = ObjectIdentity
snIgmpMIBObjects = _SnIgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1)
)


class _SnIgmpQueryInterval_Type(Integer32):
    """Custom type snIgmpQueryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SnIgmpQueryInterval_Type.__name__ = "Integer32"
_SnIgmpQueryInterval_Object = MibScalar
snIgmpQueryInterval = _SnIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 1),
    _SnIgmpQueryInterval_Type()
)
snIgmpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIgmpQueryInterval.setStatus("mandatory")


class _SnIgmpGroupMembershipTime_Type(Integer32):
    """Custom type snIgmpGroupMembershipTime based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_SnIgmpGroupMembershipTime_Type.__name__ = "Integer32"
_SnIgmpGroupMembershipTime_Object = MibScalar
snIgmpGroupMembershipTime = _SnIgmpGroupMembershipTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 2),
    _SnIgmpGroupMembershipTime_Type()
)
snIgmpGroupMembershipTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snIgmpGroupMembershipTime.setStatus("mandatory")
_SnIgmpIfTable_Object = MibTable
snIgmpIfTable = _SnIgmpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    snIgmpIfTable.setStatus("mandatory")
_SnIgmpIfEntry_Object = MibTableRow
snIgmpIfEntry = _SnIgmpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 3, 1)
)
snIgmpIfEntry.setIndexNames(
    (0, "HP-SN-IGMP-MIB", "snIgmpIfEntryIndex"),
)
if mibBuilder.loadTexts:
    snIgmpIfEntry.setStatus("mandatory")
_SnIgmpIfEntryIndex_Type = Integer32
_SnIgmpIfEntryIndex_Object = MibTableColumn
snIgmpIfEntryIndex = _SnIgmpIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 3, 1, 1),
    _SnIgmpIfEntryIndex_Type()
)
snIgmpIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIgmpIfEntryIndex.setStatus("mandatory")
_SnIgmpIfPortNumber_Type = Integer32
_SnIgmpIfPortNumber_Object = MibTableColumn
snIgmpIfPortNumber = _SnIgmpIfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 3, 1, 2),
    _SnIgmpIfPortNumber_Type()
)
snIgmpIfPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIgmpIfPortNumber.setStatus("mandatory")
_SnIgmpIfGroupAddress_Type = IpAddress
_SnIgmpIfGroupAddress_Object = MibTableColumn
snIgmpIfGroupAddress = _SnIgmpIfGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 3, 1, 3),
    _SnIgmpIfGroupAddress_Type()
)
snIgmpIfGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIgmpIfGroupAddress.setStatus("mandatory")
_SnIgmpIfGroupAge_Type = Integer32
_SnIgmpIfGroupAge_Object = MibTableColumn
snIgmpIfGroupAge = _SnIgmpIfGroupAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6, 1, 3, 1, 4),
    _SnIgmpIfGroupAge_Type()
)
snIgmpIfGroupAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snIgmpIfGroupAge.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-IGMP-MIB",
    **{"snIgmpMIBObjects": snIgmpMIBObjects,
       "snIgmpQueryInterval": snIgmpQueryInterval,
       "snIgmpGroupMembershipTime": snIgmpGroupMembershipTime,
       "snIgmpIfTable": snIgmpIfTable,
       "snIgmpIfEntry": snIgmpIfEntry,
       "snIgmpIfEntryIndex": snIgmpIfEntryIndex,
       "snIgmpIfPortNumber": snIgmpIfPortNumber,
       "snIgmpIfGroupAddress": snIgmpIfGroupAddress,
       "snIgmpIfGroupAge": snIgmpIfGroupAge}
)
