# SNMP MIB module (GRPSVCEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GRPSVCEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:54 2024
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

(grpsvcExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "grpsvcExt")

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

apGrpsvcExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApGrpsvcTable_Object = MibTable
apGrpsvcTable = _ApGrpsvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 2)
)
if mibBuilder.loadTexts:
    apGrpsvcTable.setStatus("current")
_ApGrpsvcEntry_Object = MibTableRow
apGrpsvcEntry = _ApGrpsvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 2, 1)
)
apGrpsvcEntry.setIndexNames(
    (0, "GRPSVCEXT-MIB", "apGrpsvcGrpName"),
    (0, "GRPSVCEXT-MIB", "apGrpsvcSvcName"),
)
if mibBuilder.loadTexts:
    apGrpsvcEntry.setStatus("current")


class _ApGrpsvcGrpName_Type(DisplayString):
    """Custom type apGrpsvcGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApGrpsvcGrpName_Type.__name__ = "DisplayString"
_ApGrpsvcGrpName_Object = MibTableColumn
apGrpsvcGrpName = _ApGrpsvcGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 2, 1, 1),
    _ApGrpsvcGrpName_Type()
)
apGrpsvcGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpsvcGrpName.setStatus("current")


class _ApGrpsvcSvcName_Type(DisplayString):
    """Custom type apGrpsvcSvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApGrpsvcSvcName_Type.__name__ = "DisplayString"
_ApGrpsvcSvcName_Object = MibTableColumn
apGrpsvcSvcName = _ApGrpsvcSvcName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 2, 1, 2),
    _ApGrpsvcSvcName_Type()
)
apGrpsvcSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpsvcSvcName.setStatus("current")
_ApGrpsvcStatus_Type = RowStatus
_ApGrpsvcStatus_Object = MibTableColumn
apGrpsvcStatus = _ApGrpsvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 2, 1, 3),
    _ApGrpsvcStatus_Type()
)
apGrpsvcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpsvcStatus.setStatus("current")
_ApGrpDestSvcTable_Object = MibTable
apGrpDestSvcTable = _ApGrpDestSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 3)
)
if mibBuilder.loadTexts:
    apGrpDestSvcTable.setStatus("current")
_ApGrpDestSvcEntry_Object = MibTableRow
apGrpDestSvcEntry = _ApGrpDestSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 3, 1)
)
apGrpDestSvcEntry.setIndexNames(
    (0, "GRPSVCEXT-MIB", "apGrpDestSvcGrpName"),
    (0, "GRPSVCEXT-MIB", "apGrpDestSvcSvcName"),
)
if mibBuilder.loadTexts:
    apGrpDestSvcEntry.setStatus("current")


class _ApGrpDestSvcGrpName_Type(DisplayString):
    """Custom type apGrpDestSvcGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApGrpDestSvcGrpName_Type.__name__ = "DisplayString"
_ApGrpDestSvcGrpName_Object = MibTableColumn
apGrpDestSvcGrpName = _ApGrpDestSvcGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 3, 1, 1),
    _ApGrpDestSvcGrpName_Type()
)
apGrpDestSvcGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpDestSvcGrpName.setStatus("current")


class _ApGrpDestSvcSvcName_Type(DisplayString):
    """Custom type apGrpDestSvcSvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApGrpDestSvcSvcName_Type.__name__ = "DisplayString"
_ApGrpDestSvcSvcName_Object = MibTableColumn
apGrpDestSvcSvcName = _ApGrpDestSvcSvcName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 3, 1, 2),
    _ApGrpDestSvcSvcName_Type()
)
apGrpDestSvcSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpDestSvcSvcName.setStatus("current")
_ApGrpDestSvcStatus_Type = RowStatus
_ApGrpDestSvcStatus_Object = MibTableColumn
apGrpDestSvcStatus = _ApGrpDestSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 19, 3, 1, 3),
    _ApGrpDestSvcStatus_Type()
)
apGrpDestSvcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apGrpDestSvcStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GRPSVCEXT-MIB",
    **{"apGrpsvcExtMib": apGrpsvcExtMib,
       "apGrpsvcTable": apGrpsvcTable,
       "apGrpsvcEntry": apGrpsvcEntry,
       "apGrpsvcGrpName": apGrpsvcGrpName,
       "apGrpsvcSvcName": apGrpsvcSvcName,
       "apGrpsvcStatus": apGrpsvcStatus,
       "apGrpDestSvcTable": apGrpDestSvcTable,
       "apGrpDestSvcEntry": apGrpDestSvcEntry,
       "apGrpDestSvcGrpName": apGrpDestSvcGrpName,
       "apGrpDestSvcSvcName": apGrpDestSvcSvcName,
       "apGrpDestSvcStatus": apGrpDestSvcStatus}
)
