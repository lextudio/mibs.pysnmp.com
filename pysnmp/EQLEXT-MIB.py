# SNMP MIB module (EQLEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:02 2024
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

(eqlExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "eqlExt")

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

apEqlExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApEqlTable_Object = MibTable
apEqlTable = _ApEqlTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 2)
)
if mibBuilder.loadTexts:
    apEqlTable.setStatus("current")
_ApEqlEntry_Object = MibTableRow
apEqlEntry = _ApEqlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 2, 1)
)
apEqlEntry.setIndexNames(
    (0, "EQLEXT-MIB", "apEqlName"),
)
if mibBuilder.loadTexts:
    apEqlEntry.setStatus("current")


class _ApEqlName_Type(DisplayString):
    """Custom type apEqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApEqlName_Type.__name__ = "DisplayString"
_ApEqlName_Object = MibTableColumn
apEqlName = _ApEqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 2, 1, 1),
    _ApEqlName_Type()
)
apEqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apEqlName.setStatus("current")


class _ApEqlDescription_Type(DisplayString):
    """Custom type apEqlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApEqlDescription_Type.__name__ = "DisplayString"
_ApEqlDescription_Object = MibTableColumn
apEqlDescription = _ApEqlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 2, 1, 2),
    _ApEqlDescription_Type()
)
apEqlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apEqlDescription.setStatus("current")
_ApEqlStatus_Type = RowStatus
_ApEqlStatus_Object = MibTableColumn
apEqlStatus = _ApEqlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 2, 1, 3),
    _ApEqlStatus_Type()
)
apEqlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apEqlStatus.setStatus("current")
_ApEqlExtTable_Object = MibTable
apEqlExtTable = _ApEqlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 3)
)
if mibBuilder.loadTexts:
    apEqlExtTable.setStatus("current")
_ApEqlExtEntry_Object = MibTableRow
apEqlExtEntry = _ApEqlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 3, 1)
)
apEqlExtEntry.setIndexNames(
    (0, "EQLEXT-MIB", "apEqlName"),
    (0, "EQLEXT-MIB", "apEqlExtName"),
)
if mibBuilder.loadTexts:
    apEqlExtEntry.setStatus("current")


class _ApEqlExtName_Type(DisplayString):
    """Custom type apEqlExtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_ApEqlExtName_Type.__name__ = "DisplayString"
_ApEqlExtName_Object = MibTableColumn
apEqlExtName = _ApEqlExtName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 3, 1, 1),
    _ApEqlExtName_Type()
)
apEqlExtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apEqlExtName.setStatus("current")


class _ApEqlExtDescription_Type(DisplayString):
    """Custom type apEqlExtDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApEqlExtDescription_Type.__name__ = "DisplayString"
_ApEqlExtDescription_Object = MibTableColumn
apEqlExtDescription = _ApEqlExtDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 3, 1, 2),
    _ApEqlExtDescription_Type()
)
apEqlExtDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apEqlExtDescription.setStatus("current")
_ApEqlExtStatus_Type = RowStatus
_ApEqlExtStatus_Object = MibTableColumn
apEqlExtStatus = _ApEqlExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 42, 3, 1, 3),
    _ApEqlExtStatus_Type()
)
apEqlExtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apEqlExtStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLEXT-MIB",
    **{"apEqlExtMib": apEqlExtMib,
       "apEqlTable": apEqlTable,
       "apEqlEntry": apEqlEntry,
       "apEqlName": apEqlName,
       "apEqlDescription": apEqlDescription,
       "apEqlStatus": apEqlStatus,
       "apEqlExtTable": apEqlExtTable,
       "apEqlExtEntry": apEqlExtEntry,
       "apEqlExtName": apEqlExtName,
       "apEqlExtDescription": apEqlExtDescription,
       "apEqlExtStatus": apEqlExtStatus}
)
