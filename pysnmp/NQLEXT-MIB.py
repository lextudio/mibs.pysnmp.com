# SNMP MIB module (NQLEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NQLEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:09 2024
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

(nqlExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "nqlExt")

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

apNqlExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApNqlTable_Object = MibTable
apNqlTable = _ApNqlTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 2)
)
if mibBuilder.loadTexts:
    apNqlTable.setStatus("current")
_ApNqlEntry_Object = MibTableRow
apNqlEntry = _ApNqlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1)
)
apNqlEntry.setIndexNames(
    (0, "NQLEXT-MIB", "apNqlName"),
)
if mibBuilder.loadTexts:
    apNqlEntry.setStatus("current")
_ApNqlStatus_Type = RowStatus
_ApNqlStatus_Object = MibTableColumn
apNqlStatus = _ApNqlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1, 1),
    _ApNqlStatus_Type()
)
apNqlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlStatus.setStatus("current")


class _ApNqlName_Type(DisplayString):
    """Custom type apNqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApNqlName_Type.__name__ = "DisplayString"
_ApNqlName_Object = MibTableColumn
apNqlName = _ApNqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1, 2),
    _ApNqlName_Type()
)
apNqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlName.setStatus("current")


class _ApNqlDescription_Type(DisplayString):
    """Custom type apNqlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ApNqlDescription_Type.__name__ = "DisplayString"
_ApNqlDescription_Object = MibTableColumn
apNqlDescription = _ApNqlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 2, 1, 3),
    _ApNqlDescription_Type()
)
apNqlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlDescription.setStatus("current")
_ApNqlExtTable_Object = MibTable
apNqlExtTable = _ApNqlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 3)
)
if mibBuilder.loadTexts:
    apNqlExtTable.setStatus("current")
_ApNqlExtEntry_Object = MibTableRow
apNqlExtEntry = _ApNqlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1)
)
apNqlExtEntry.setIndexNames(
    (0, "NQLEXT-MIB", "apNqlName"),
    (0, "NQLEXT-MIB", "apNqlExtAddress"),
)
if mibBuilder.loadTexts:
    apNqlExtEntry.setStatus("current")
_ApNqlExtStatus_Type = RowStatus
_ApNqlExtStatus_Object = MibTableColumn
apNqlExtStatus = _ApNqlExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 1),
    _ApNqlExtStatus_Type()
)
apNqlExtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlExtStatus.setStatus("current")
_ApNqlExtAddress_Type = IpAddress
_ApNqlExtAddress_Object = MibTableColumn
apNqlExtAddress = _ApNqlExtAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 2),
    _ApNqlExtAddress_Type()
)
apNqlExtAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlExtAddress.setStatus("current")


class _ApNqlExtPrefixLen_Type(Integer32):
    """Custom type apNqlExtPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32),
    )


_ApNqlExtPrefixLen_Type.__name__ = "Integer32"
_ApNqlExtPrefixLen_Object = MibTableColumn
apNqlExtPrefixLen = _ApNqlExtPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 3),
    _ApNqlExtPrefixLen_Type()
)
apNqlExtPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlExtPrefixLen.setStatus("current")


class _ApNqlExtDescription_Type(DisplayString):
    """Custom type apNqlExtDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ApNqlExtDescription_Type.__name__ = "DisplayString"
_ApNqlExtDescription_Object = MibTableColumn
apNqlExtDescription = _ApNqlExtDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 4),
    _ApNqlExtDescription_Type()
)
apNqlExtDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlExtDescription.setStatus("current")


class _ApNqlExtLogEnable_Type(Integer32):
    """Custom type apNqlExtLogEnable based on Integer32"""
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


_ApNqlExtLogEnable_Type.__name__ = "Integer32"
_ApNqlExtLogEnable_Object = MibTableColumn
apNqlExtLogEnable = _ApNqlExtLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 50, 3, 1, 5),
    _ApNqlExtLogEnable_Type()
)
apNqlExtLogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apNqlExtLogEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NQLEXT-MIB",
    **{"apNqlExtMib": apNqlExtMib,
       "apNqlTable": apNqlTable,
       "apNqlEntry": apNqlEntry,
       "apNqlStatus": apNqlStatus,
       "apNqlName": apNqlName,
       "apNqlDescription": apNqlDescription,
       "apNqlExtTable": apNqlExtTable,
       "apNqlExtEntry": apNqlExtEntry,
       "apNqlExtStatus": apNqlExtStatus,
       "apNqlExtAddress": apNqlExtAddress,
       "apNqlExtPrefixLen": apNqlExtPrefixLen,
       "apNqlExtDescription": apNqlExtDescription,
       "apNqlExtLogEnable": apNqlExtLogEnable}
)
