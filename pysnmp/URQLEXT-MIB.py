# SNMP MIB module (URQLEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/URQLEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:39 2024
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

(urqlExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "urqlExt")

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

apUrqlExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApUrqlTable_Object = MibTable
apUrqlTable = _ApUrqlTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2)
)
if mibBuilder.loadTexts:
    apUrqlTable.setStatus("current")
_ApUrqlEntry_Object = MibTableRow
apUrqlEntry = _ApUrqlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1)
)
apUrqlEntry.setIndexNames(
    (0, "URQLEXT-MIB", "apUrqlName"),
)
if mibBuilder.loadTexts:
    apUrqlEntry.setStatus("current")


class _ApUrqlName_Type(DisplayString):
    """Custom type apUrqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApUrqlName_Type.__name__ = "DisplayString"
_ApUrqlName_Object = MibTableColumn
apUrqlName = _ApUrqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 1),
    _ApUrqlName_Type()
)
apUrqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlName.setStatus("current")


class _ApUrqlDescription_Type(DisplayString):
    """Custom type apUrqlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApUrqlDescription_Type.__name__ = "DisplayString"
_ApUrqlDescription_Object = MibTableColumn
apUrqlDescription = _ApUrqlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 2),
    _ApUrqlDescription_Type()
)
apUrqlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlDescription.setStatus("current")


class _ApUrqlCreateType_Type(Integer32):
    """Custom type apUrqlCreateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ApUrqlCreateType_Type.__name__ = "Integer32"
_ApUrqlCreateType_Object = MibTableColumn
apUrqlCreateType = _ApUrqlCreateType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 3),
    _ApUrqlCreateType_Type()
)
apUrqlCreateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUrqlCreateType.setStatus("current")
_ApUrqlStatus_Type = RowStatus
_ApUrqlStatus_Object = MibTableColumn
apUrqlStatus = _ApUrqlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 4),
    _ApUrqlStatus_Type()
)
apUrqlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlStatus.setStatus("current")


class _ApUrqlEnable_Type(Integer32):
    """Custom type apUrqlEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApUrqlEnable_Type.__name__ = "Integer32"
_ApUrqlEnable_Object = MibTableColumn
apUrqlEnable = _ApUrqlEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 5),
    _ApUrqlEnable_Type()
)
apUrqlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlEnable.setStatus("current")


class _ApUrqlDomain_Type(DisplayString):
    """Custom type apUrqlDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ApUrqlDomain_Type.__name__ = "DisplayString"
_ApUrqlDomain_Object = MibTableColumn
apUrqlDomain = _ApUrqlDomain_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 2, 1, 6),
    _ApUrqlDomain_Type()
)
apUrqlDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlDomain.setStatus("current")
_ApUrqlExtTable_Object = MibTable
apUrqlExtTable = _ApUrqlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 3)
)
if mibBuilder.loadTexts:
    apUrqlExtTable.setStatus("current")
_ApUrqlExtEntry_Object = MibTableRow
apUrqlExtEntry = _ApUrqlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1)
)
apUrqlExtEntry.setIndexNames(
    (0, "URQLEXT-MIB", "apUrqlName"),
    (0, "URQLEXT-MIB", "apUrqlExtUrlNumber"),
)
if mibBuilder.loadTexts:
    apUrqlExtEntry.setStatus("current")


class _ApUrqlExtUrlNumber_Type(Integer32):
    """Custom type apUrqlExtUrlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApUrqlExtUrlNumber_Type.__name__ = "Integer32"
_ApUrqlExtUrlNumber_Object = MibTableColumn
apUrqlExtUrlNumber = _ApUrqlExtUrlNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 1),
    _ApUrqlExtUrlNumber_Type()
)
apUrqlExtUrlNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlExtUrlNumber.setStatus("current")


class _ApUrqlExtUrlName_Type(DisplayString):
    """Custom type apUrqlExtUrlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 251),
    )


_ApUrqlExtUrlName_Type.__name__ = "DisplayString"
_ApUrqlExtUrlName_Object = MibTableColumn
apUrqlExtUrlName = _ApUrqlExtUrlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 2),
    _ApUrqlExtUrlName_Type()
)
apUrqlExtUrlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlExtUrlName.setStatus("current")


class _ApUrqlExtUrlDescription_Type(DisplayString):
    """Custom type apUrqlExtUrlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApUrqlExtUrlDescription_Type.__name__ = "DisplayString"
_ApUrqlExtUrlDescription_Object = MibTableColumn
apUrqlExtUrlDescription = _ApUrqlExtUrlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 3),
    _ApUrqlExtUrlDescription_Type()
)
apUrqlExtUrlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlExtUrlDescription.setStatus("current")


class _ApUrqlExtUrlCreateType_Type(Integer32):
    """Custom type apUrqlExtUrlCreateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ApUrqlExtUrlCreateType_Type.__name__ = "Integer32"
_ApUrqlExtUrlCreateType_Object = MibTableColumn
apUrqlExtUrlCreateType = _ApUrqlExtUrlCreateType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 4),
    _ApUrqlExtUrlCreateType_Type()
)
apUrqlExtUrlCreateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUrqlExtUrlCreateType.setStatus("current")
_ApUrqlExtUrlStatus_Type = RowStatus
_ApUrqlExtUrlStatus_Object = MibTableColumn
apUrqlExtUrlStatus = _ApUrqlExtUrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 49, 3, 1, 5),
    _ApUrqlExtUrlStatus_Type()
)
apUrqlExtUrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apUrqlExtUrlStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "URQLEXT-MIB",
    **{"apUrqlExtMib": apUrqlExtMib,
       "apUrqlTable": apUrqlTable,
       "apUrqlEntry": apUrqlEntry,
       "apUrqlName": apUrqlName,
       "apUrqlDescription": apUrqlDescription,
       "apUrqlCreateType": apUrqlCreateType,
       "apUrqlStatus": apUrqlStatus,
       "apUrqlEnable": apUrqlEnable,
       "apUrqlDomain": apUrqlDomain,
       "apUrqlExtTable": apUrqlExtTable,
       "apUrqlExtEntry": apUrqlExtEntry,
       "apUrqlExtUrlNumber": apUrqlExtUrlNumber,
       "apUrqlExtUrlName": apUrqlExtUrlName,
       "apUrqlExtUrlDescription": apUrqlExtUrlDescription,
       "apUrqlExtUrlCreateType": apUrqlExtUrlCreateType,
       "apUrqlExtUrlStatus": apUrqlExtUrlStatus}
)
