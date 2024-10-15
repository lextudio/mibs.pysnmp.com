# SNMP MIB module (DQLEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DQLEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:26 2024
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

(dqlExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "dqlExt")

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

apDqlExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApDqlTable_Object = MibTable
apDqlTable = _ApDqlTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 2)
)
if mibBuilder.loadTexts:
    apDqlTable.setStatus("current")
_ApDqlEntry_Object = MibTableRow
apDqlEntry = _ApDqlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 2, 1)
)
apDqlEntry.setIndexNames(
    (0, "DQLEXT-MIB", "apDqlName"),
)
if mibBuilder.loadTexts:
    apDqlEntry.setStatus("current")
_ApDqlStatus_Type = RowStatus
_ApDqlStatus_Object = MibTableColumn
apDqlStatus = _ApDqlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 2, 1, 1),
    _ApDqlStatus_Type()
)
apDqlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDqlStatus.setStatus("current")


class _ApDqlName_Type(DisplayString):
    """Custom type apDqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApDqlName_Type.__name__ = "DisplayString"
_ApDqlName_Object = MibTableColumn
apDqlName = _ApDqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 2, 1, 2),
    _ApDqlName_Type()
)
apDqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDqlName.setStatus("current")


class _ApDqlDescription_Type(DisplayString):
    """Custom type apDqlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ApDqlDescription_Type.__name__ = "DisplayString"
_ApDqlDescription_Object = MibTableColumn
apDqlDescription = _ApDqlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 2, 1, 3),
    _ApDqlDescription_Type()
)
apDqlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDqlDescription.setStatus("current")
_ApDqlDomainTable_Object = MibTable
apDqlDomainTable = _ApDqlDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 3)
)
if mibBuilder.loadTexts:
    apDqlDomainTable.setStatus("current")
_ApDqlDomainEntry_Object = MibTableRow
apDqlDomainEntry = _ApDqlDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 3, 1)
)
apDqlDomainEntry.setIndexNames(
    (0, "DQLEXT-MIB", "apDqlName"),
    (0, "DQLEXT-MIB", "apDqlDomainName"),
)
if mibBuilder.loadTexts:
    apDqlDomainEntry.setStatus("current")
_ApDqlDomainStatus_Type = RowStatus
_ApDqlDomainStatus_Object = MibTableColumn
apDqlDomainStatus = _ApDqlDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 3, 1, 1),
    _ApDqlDomainStatus_Type()
)
apDqlDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDqlDomainStatus.setStatus("current")


class _ApDqlDomainName_Type(DisplayString):
    """Custom type apDqlDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ApDqlDomainName_Type.__name__ = "DisplayString"
_ApDqlDomainName_Object = MibTableColumn
apDqlDomainName = _ApDqlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 3, 1, 2),
    _ApDqlDomainName_Type()
)
apDqlDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDqlDomainName.setStatus("current")


class _ApDqlDomainDescription_Type(DisplayString):
    """Custom type apDqlDomainDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ApDqlDomainDescription_Type.__name__ = "DisplayString"
_ApDqlDomainDescription_Object = MibTableColumn
apDqlDomainDescription = _ApDqlDomainDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 3, 1, 3),
    _ApDqlDomainDescription_Type()
)
apDqlDomainDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDqlDomainDescription.setStatus("current")


class _ApDqlDomainBucketIndex_Type(Integer32):
    """Custom type apDqlDomainBucketIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ApDqlDomainBucketIndex_Type.__name__ = "Integer32"
_ApDqlDomainBucketIndex_Object = MibTableColumn
apDqlDomainBucketIndex = _ApDqlDomainBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 51, 3, 1, 4),
    _ApDqlDomainBucketIndex_Type()
)
apDqlDomainBucketIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDqlDomainBucketIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DQLEXT-MIB",
    **{"apDqlExtMib": apDqlExtMib,
       "apDqlTable": apDqlTable,
       "apDqlEntry": apDqlEntry,
       "apDqlStatus": apDqlStatus,
       "apDqlName": apDqlName,
       "apDqlDescription": apDqlDescription,
       "apDqlDomainTable": apDqlDomainTable,
       "apDqlDomainEntry": apDqlDomainEntry,
       "apDqlDomainStatus": apDqlDomainStatus,
       "apDqlDomainName": apDqlDomainName,
       "apDqlDomainDescription": apDqlDomainDescription,
       "apDqlDomainBucketIndex": apDqlDomainBucketIndex}
)
