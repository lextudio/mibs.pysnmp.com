# SNMP MIB module (BWDTHEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BWDTHEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:11 2024
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

(bwdthExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "bwdthExt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apBwdthExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApBwdthTable_Object = MibTable
apBwdthTable = _ApBwdthTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2)
)
if mibBuilder.loadTexts:
    apBwdthTable.setStatus("current")
_ApBwdthEntry_Object = MibTableRow
apBwdthEntry = _ApBwdthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1)
)
apBwdthEntry.setIndexNames(
    (0, "BWDTHEXT-MIB", "apBwdthOwnerName"),
    (0, "BWDTHEXT-MIB", "apBwdthQOSClass"),
)
if mibBuilder.loadTexts:
    apBwdthEntry.setStatus("current")


class _ApBwdthOwnerName_Type(DisplayString):
    """Custom type apBwdthOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApBwdthOwnerName_Type.__name__ = "DisplayString"
_ApBwdthOwnerName_Object = MibTableColumn
apBwdthOwnerName = _ApBwdthOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 1),
    _ApBwdthOwnerName_Type()
)
apBwdthOwnerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBwdthOwnerName.setStatus("current")
_ApBwdthIndex_Type = Integer32
_ApBwdthIndex_Object = MibTableColumn
apBwdthIndex = _ApBwdthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 2),
    _ApBwdthIndex_Type()
)
apBwdthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBwdthIndex.setStatus("current")


class _ApBwdthQOSClass_Type(Integer32):
    """Custom type apBwdthQOSClass based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ApBwdthQOSClass_Type.__name__ = "Integer32"
_ApBwdthQOSClass_Object = MibTableColumn
apBwdthQOSClass = _ApBwdthQOSClass_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 3),
    _ApBwdthQOSClass_Type()
)
apBwdthQOSClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBwdthQOSClass.setStatus("current")
_ApBwdthOwnerId_Type = Integer32
_ApBwdthOwnerId_Object = MibTableColumn
apBwdthOwnerId = _ApBwdthOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 4),
    _ApBwdthOwnerId_Type()
)
apBwdthOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBwdthOwnerId.setStatus("current")


class _ApBwdthMaxBwdth_Type(Integer32):
    """Custom type apBwdthMaxBwdth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApBwdthMaxBwdth_Type.__name__ = "Integer32"
_ApBwdthMaxBwdth_Object = MibTableColumn
apBwdthMaxBwdth = _ApBwdthMaxBwdth_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 5),
    _ApBwdthMaxBwdth_Type()
)
apBwdthMaxBwdth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBwdthMaxBwdth.setStatus("current")


class _ApBwdthAvgBwdth_Type(Integer32):
    """Custom type apBwdthAvgBwdth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApBwdthAvgBwdth_Type.__name__ = "Integer32"
_ApBwdthAvgBwdth_Object = MibTableColumn
apBwdthAvgBwdth = _ApBwdthAvgBwdth_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 6),
    _ApBwdthAvgBwdth_Type()
)
apBwdthAvgBwdth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBwdthAvgBwdth.setStatus("current")


class _ApBwdthAllocStat_Type(Integer32):
    """Custom type apBwdthAllocStat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_ApBwdthAllocStat_Type.__name__ = "Integer32"
_ApBwdthAllocStat_Object = MibTableColumn
apBwdthAllocStat = _ApBwdthAllocStat_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 7),
    _ApBwdthAllocStat_Type()
)
apBwdthAllocStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBwdthAllocStat.setStatus("current")
_ApBwdthStatus_Type = RowStatus
_ApBwdthStatus_Object = MibTableColumn
apBwdthStatus = _ApBwdthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 26, 2, 1, 8),
    _ApBwdthStatus_Type()
)
apBwdthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apBwdthStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BWDTHEXT-MIB",
    **{"apBwdthExtMib": apBwdthExtMib,
       "apBwdthTable": apBwdthTable,
       "apBwdthEntry": apBwdthEntry,
       "apBwdthOwnerName": apBwdthOwnerName,
       "apBwdthIndex": apBwdthIndex,
       "apBwdthQOSClass": apBwdthQOSClass,
       "apBwdthOwnerId": apBwdthOwnerId,
       "apBwdthMaxBwdth": apBwdthMaxBwdth,
       "apBwdthAvgBwdth": apBwdthAvgBwdth,
       "apBwdthAllocStat": apBwdthAllocStat,
       "apBwdthStatus": apBwdthStatus}
)
