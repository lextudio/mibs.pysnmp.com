# SNMP MIB module (SONUS-DIRECTORY-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-DIRECTORY-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:54 2024
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

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(SonusName,) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusName")


# MODULE-IDENTITY

sonusDirectoryServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusDirectoryServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusDirectoryServicesMIBObjects = _SonusDirectoryServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1)
)
_SonusRouteObjects_ObjectIdentity = ObjectIdentity
sonusRouteObjects = _SonusRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1)
)
_SonusRouteNameObjects_ObjectIdentity = ObjectIdentity
sonusRouteNameObjects = _SonusRouteNameObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1)
)
_SonusDsRouteNameNextIndex_Type = Integer32
_SonusDsRouteNameNextIndex_Object = MibScalar
sonusDsRouteNameNextIndex = _SonusDsRouteNameNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 1),
    _SonusDsRouteNameNextIndex_Type()
)
sonusDsRouteNameNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsRouteNameNextIndex.setStatus("current")
_SonusDsRouteNameTable_Object = MibTable
sonusDsRouteNameTable = _SonusDsRouteNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusDsRouteNameTable.setStatus("current")
_SonusDsRouteNameEntry_Object = MibTableRow
sonusDsRouteNameEntry = _SonusDsRouteNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1)
)
sonusDsRouteNameEntry.setIndexNames(
    (0, "SONUS-DIRECTORY-SERVICES-MIB", "sonusDsNameRouteTableIndex"),
    (0, "SONUS-DIRECTORY-SERVICES-MIB", "sonusDsRouteNameIndex"),
)
if mibBuilder.loadTexts:
    sonusDsRouteNameEntry.setStatus("current")
_SonusDsNameRouteTableIndex_Type = Integer32
_SonusDsNameRouteTableIndex_Object = MibTableColumn
sonusDsNameRouteTableIndex = _SonusDsNameRouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 1),
    _SonusDsNameRouteTableIndex_Type()
)
sonusDsNameRouteTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsNameRouteTableIndex.setStatus("current")
_SonusDsRouteNameIndex_Type = Integer32
_SonusDsRouteNameIndex_Object = MibTableColumn
sonusDsRouteNameIndex = _SonusDsRouteNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 2),
    _SonusDsRouteNameIndex_Type()
)
sonusDsRouteNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsRouteNameIndex.setStatus("current")


class _SonusDsRouteName_Type(DisplayString):
    """Custom type sonusDsRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsRouteName_Type.__name__ = "DisplayString"
_SonusDsRouteName_Object = MibTableColumn
sonusDsRouteName = _SonusDsRouteName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 3),
    _SonusDsRouteName_Type()
)
sonusDsRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRouteName.setStatus("current")


class _SonusDsRoute1TgName_Type(DisplayString):
    """Custom type sonusDsRoute1TgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsRoute1TgName_Type.__name__ = "DisplayString"
_SonusDsRoute1TgName_Object = MibTableColumn
sonusDsRoute1TgName = _SonusDsRoute1TgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 4),
    _SonusDsRoute1TgName_Type()
)
sonusDsRoute1TgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRoute1TgName.setStatus("current")


class _SonusDsRoute2TgName_Type(DisplayString):
    """Custom type sonusDsRoute2TgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsRoute2TgName_Type.__name__ = "DisplayString"
_SonusDsRoute2TgName_Object = MibTableColumn
sonusDsRoute2TgName = _SonusDsRoute2TgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 5),
    _SonusDsRoute2TgName_Type()
)
sonusDsRoute2TgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRoute2TgName.setStatus("current")


class _SonusDsRoute3TgName_Type(DisplayString):
    """Custom type sonusDsRoute3TgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsRoute3TgName_Type.__name__ = "DisplayString"
_SonusDsRoute3TgName_Object = MibTableColumn
sonusDsRoute3TgName = _SonusDsRoute3TgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 6),
    _SonusDsRoute3TgName_Type()
)
sonusDsRoute3TgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRoute3TgName.setStatus("current")


class _SonusDsRoute4TgName_Type(DisplayString):
    """Custom type sonusDsRoute4TgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsRoute4TgName_Type.__name__ = "DisplayString"
_SonusDsRoute4TgName_Object = MibTableColumn
sonusDsRoute4TgName = _SonusDsRoute4TgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 7),
    _SonusDsRoute4TgName_Type()
)
sonusDsRoute4TgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRoute4TgName.setStatus("current")


class _SonusDsRouteNameAdminState_Type(Integer32):
    """Custom type sonusDsRouteNameAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusDsRouteNameAdminState_Type.__name__ = "Integer32"
_SonusDsRouteNameAdminState_Object = MibTableColumn
sonusDsRouteNameAdminState = _SonusDsRouteNameAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 8),
    _SonusDsRouteNameAdminState_Type()
)
sonusDsRouteNameAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRouteNameAdminState.setStatus("current")
_SonusDsRouteNameRowStatus_Type = RowStatus
_SonusDsRouteNameRowStatus_Object = MibTableColumn
sonusDsRouteNameRowStatus = _SonusDsRouteNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 1, 2, 1, 9),
    _SonusDsRouteNameRowStatus_Type()
)
sonusDsRouteNameRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRouteNameRowStatus.setStatus("current")
_SonusRouteTableObjects_ObjectIdentity = ObjectIdentity
sonusRouteTableObjects = _SonusRouteTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2)
)
_SonusDsRouteTableNextIndex_Type = Integer32
_SonusDsRouteTableNextIndex_Object = MibScalar
sonusDsRouteTableNextIndex = _SonusDsRouteTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 1),
    _SonusDsRouteTableNextIndex_Type()
)
sonusDsRouteTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsRouteTableNextIndex.setStatus("current")
_SonusDsRouteTable_Object = MibTable
sonusDsRouteTable = _SonusDsRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusDsRouteTable.setStatus("current")
_SonusDsRouteTableEntry_Object = MibTableRow
sonusDsRouteTableEntry = _SonusDsRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1)
)
sonusDsRouteTableEntry.setIndexNames(
    (0, "SONUS-DIRECTORY-SERVICES-MIB", "sonusDsRouteTableIndex"),
)
if mibBuilder.loadTexts:
    sonusDsRouteTableEntry.setStatus("current")
_SonusDsRouteTableIndex_Type = Integer32
_SonusDsRouteTableIndex_Object = MibTableColumn
sonusDsRouteTableIndex = _SonusDsRouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 1),
    _SonusDsRouteTableIndex_Type()
)
sonusDsRouteTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsRouteTableIndex.setStatus("current")
_SonusDsRouteTableName_Type = SonusName
_SonusDsRouteTableName_Object = MibTableColumn
sonusDsRouteTableName = _SonusDsRouteTableName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 2),
    _SonusDsRouteTableName_Type()
)
sonusDsRouteTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRouteTableName.setStatus("current")


class _SonusDsRouteTableType_Type(Integer32):
    """Custom type sonusDsRouteTableType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_SonusDsRouteTableType_Type.__name__ = "Integer32"
_SonusDsRouteTableType_Object = MibTableColumn
sonusDsRouteTableType = _SonusDsRouteTableType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 3),
    _SonusDsRouteTableType_Type()
)
sonusDsRouteTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRouteTableType.setStatus("current")


class _SonusDsMaxDigits_Type(Integer32):
    """Custom type sonusDsMaxDigits based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SonusDsMaxDigits_Type.__name__ = "Integer32"
_SonusDsMaxDigits_Object = MibTableColumn
sonusDsMaxDigits = _SonusDsMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 4),
    _SonusDsMaxDigits_Type()
)
sonusDsMaxDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsMaxDigits.setStatus("current")


class _SonusDsMaxRoutes_Type(Integer32):
    """Custom type sonusDsMaxRoutes based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SonusDsMaxRoutes_Type.__name__ = "Integer32"
_SonusDsMaxRoutes_Object = MibTableColumn
sonusDsMaxRoutes = _SonusDsMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 5),
    _SonusDsMaxRoutes_Type()
)
sonusDsMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsMaxRoutes.setStatus("current")


class _SonusDsTableCountryCode_Type(DisplayString):
    """Custom type sonusDsTableCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_SonusDsTableCountryCode_Type.__name__ = "DisplayString"
_SonusDsTableCountryCode_Object = MibTableColumn
sonusDsTableCountryCode = _SonusDsTableCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 6),
    _SonusDsTableCountryCode_Type()
)
sonusDsTableCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsTableCountryCode.setStatus("current")


class _SonusDsRouteTableAdminState_Type(Integer32):
    """Custom type sonusDsRouteTableAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusDsRouteTableAdminState_Type.__name__ = "Integer32"
_SonusDsRouteTableAdminState_Object = MibTableColumn
sonusDsRouteTableAdminState = _SonusDsRouteTableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 7),
    _SonusDsRouteTableAdminState_Type()
)
sonusDsRouteTableAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRouteTableAdminState.setStatus("current")
_SonusDsRouteTableRowStatus_Type = RowStatus
_SonusDsRouteTableRowStatus_Object = MibTableColumn
sonusDsRouteTableRowStatus = _SonusDsRouteTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 2, 2, 1, 8),
    _SonusDsRouteTableRowStatus_Type()
)
sonusDsRouteTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsRouteTableRowStatus.setStatus("current")
_SonusRouteAddressObjects_ObjectIdentity = ObjectIdentity
sonusRouteAddressObjects = _SonusRouteAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3)
)
_SonusDsAddressRouteTable_Object = MibTable
sonusDsAddressRouteTable = _SonusDsAddressRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sonusDsAddressRouteTable.setStatus("current")
_SonusDsAddressRouteEntry_Object = MibTableRow
sonusDsAddressRouteEntry = _SonusDsAddressRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1)
)
sonusDsAddressRouteEntry.setIndexNames(
    (0, "SONUS-DIRECTORY-SERVICES-MIB", "sonusDsAddressRouteTableIndex"),
    (0, "SONUS-DIRECTORY-SERVICES-MIB", "sonusDsAddressRouteIndex"),
)
if mibBuilder.loadTexts:
    sonusDsAddressRouteEntry.setStatus("current")
_SonusDsAddressRouteTableIndex_Type = Integer32
_SonusDsAddressRouteTableIndex_Object = MibTableColumn
sonusDsAddressRouteTableIndex = _SonusDsAddressRouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1, 1),
    _SonusDsAddressRouteTableIndex_Type()
)
sonusDsAddressRouteTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsAddressRouteTableIndex.setStatus("current")
_SonusDsAddressRouteIndex_Type = Integer32
_SonusDsAddressRouteIndex_Object = MibTableColumn
sonusDsAddressRouteIndex = _SonusDsAddressRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1, 2),
    _SonusDsAddressRouteIndex_Type()
)
sonusDsAddressRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsAddressRouteIndex.setStatus("current")


class _SonusDsAddressCountryCode_Type(DisplayString):
    """Custom type sonusDsAddressCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SonusDsAddressCountryCode_Type.__name__ = "DisplayString"
_SonusDsAddressCountryCode_Object = MibTableColumn
sonusDsAddressCountryCode = _SonusDsAddressCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1, 3),
    _SonusDsAddressCountryCode_Type()
)
sonusDsAddressCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsAddressCountryCode.setStatus("current")


class _SonusDsAddress_Type(DisplayString):
    """Custom type sonusDsAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SonusDsAddress_Type.__name__ = "DisplayString"
_SonusDsAddress_Object = MibTableColumn
sonusDsAddress = _SonusDsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1, 4),
    _SonusDsAddress_Type()
)
sonusDsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsAddress.setStatus("current")


class _SonusDsAddressRouteName_Type(DisplayString):
    """Custom type sonusDsAddressRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsAddressRouteName_Type.__name__ = "DisplayString"
_SonusDsAddressRouteName_Object = MibTableColumn
sonusDsAddressRouteName = _SonusDsAddressRouteName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1, 5),
    _SonusDsAddressRouteName_Type()
)
sonusDsAddressRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsAddressRouteName.setStatus("current")


class _SonusDsAddressRouteAdminState_Type(Integer32):
    """Custom type sonusDsAddressRouteAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusDsAddressRouteAdminState_Type.__name__ = "Integer32"
_SonusDsAddressRouteAdminState_Object = MibTableColumn
sonusDsAddressRouteAdminState = _SonusDsAddressRouteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1, 6),
    _SonusDsAddressRouteAdminState_Type()
)
sonusDsAddressRouteAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsAddressRouteAdminState.setStatus("current")
_SonusDsAddressRouteRowStatus_Type = RowStatus
_SonusDsAddressRouteRowStatus_Object = MibTableColumn
sonusDsAddressRouteRowStatus = _SonusDsAddressRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 3, 1, 1, 7),
    _SonusDsAddressRouteRowStatus_Type()
)
sonusDsAddressRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsAddressRouteRowStatus.setStatus("current")
_SonusDestinationTrunkObjects_ObjectIdentity = ObjectIdentity
sonusDestinationTrunkObjects = _SonusDestinationTrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4)
)
_SonusDsDestTgNextIndex_Type = Integer32
_SonusDsDestTgNextIndex_Object = MibScalar
sonusDsDestTgNextIndex = _SonusDsDestTgNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 1),
    _SonusDsDestTgNextIndex_Type()
)
sonusDsDestTgNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsDestTgNextIndex.setStatus("current")
_SonusDsDestTgTable_Object = MibTable
sonusDsDestTgTable = _SonusDsDestTgTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sonusDsDestTgTable.setStatus("current")
_SonusDsDestTgEntry_Object = MibTableRow
sonusDsDestTgEntry = _SonusDsDestTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1)
)
sonusDsDestTgEntry.setIndexNames(
    (0, "SONUS-DIRECTORY-SERVICES-MIB", "sonusDsDestTgIndex"),
)
if mibBuilder.loadTexts:
    sonusDsDestTgEntry.setStatus("current")
_SonusDsDestTgIndex_Type = Integer32
_SonusDsDestTgIndex_Object = MibTableColumn
sonusDsDestTgIndex = _SonusDsDestTgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 1),
    _SonusDsDestTgIndex_Type()
)
sonusDsDestTgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsDestTgIndex.setStatus("current")
_SonusDsDestTgName_Type = SonusName
_SonusDsDestTgName_Object = MibTableColumn
sonusDsDestTgName = _SonusDsDestTgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 2),
    _SonusDsDestTgName_Type()
)
sonusDsDestTgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsDestTgName.setStatus("current")


class _SonusDsDestTrunk_Type(Integer32):
    """Custom type sonusDsDestTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("res", 2),
          ("unres", 1))
    )


_SonusDsDestTrunk_Type.__name__ = "Integer32"
_SonusDsDestTrunk_Object = MibTableColumn
sonusDsDestTrunk = _SonusDsDestTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 3),
    _SonusDsDestTrunk_Type()
)
sonusDsDestTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsDestTrunk.setStatus("current")


class _SonusDsDestTgSignaling_Type(Integer32):
    """Custom type sonusDsDestTgSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cas", 3),
          ("isdn", 2),
          ("isup", 1))
    )


_SonusDsDestTgSignaling_Type.__name__ = "Integer32"
_SonusDsDestTgSignaling_Object = MibTableColumn
sonusDsDestTgSignaling = _SonusDsDestTgSignaling_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 4),
    _SonusDsDestTgSignaling_Type()
)
sonusDsDestTgSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsDestTgSignaling.setStatus("current")


class _SonusDsDestGwName_Type(DisplayString):
    """Custom type sonusDsDestGwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsDestGwName_Type.__name__ = "DisplayString"
_SonusDsDestGwName_Object = MibTableColumn
sonusDsDestGwName = _SonusDsDestGwName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 5),
    _SonusDsDestGwName_Type()
)
sonusDsDestGwName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsDestGwName.setStatus("current")


class _SonusDsDestCarrier_Type(DisplayString):
    """Custom type sonusDsDestCarrier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusDsDestCarrier_Type.__name__ = "DisplayString"
_SonusDsDestCarrier_Object = MibTableColumn
sonusDsDestCarrier = _SonusDsDestCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 6),
    _SonusDsDestCarrier_Type()
)
sonusDsDestCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsDestCarrier.setStatus("current")


class _SonusDsDestTgAdminState_Type(Integer32):
    """Custom type sonusDsDestTgAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusDsDestTgAdminState_Type.__name__ = "Integer32"
_SonusDsDestTgAdminState_Object = MibTableColumn
sonusDsDestTgAdminState = _SonusDsDestTgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 7),
    _SonusDsDestTgAdminState_Type()
)
sonusDsDestTgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsDestTgAdminState.setStatus("current")
_SonusDsDestTgRowStatus_Type = RowStatus
_SonusDsDestTgRowStatus_Object = MibTableColumn
sonusDsDestTgRowStatus = _SonusDsDestTgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 4, 2, 1, 8),
    _SonusDsDestTgRowStatus_Type()
)
sonusDsDestTgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsDestTgRowStatus.setStatus("current")
_SonusRouteStatusObjects_ObjectIdentity = ObjectIdentity
sonusRouteStatusObjects = _SonusRouteStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 5)
)
_SonusUnknownRoutes_Type = Integer32
_SonusUnknownRoutes_Object = MibScalar
sonusUnknownRoutes = _SonusUnknownRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 1, 5, 1),
    _SonusUnknownRoutes_Type()
)
sonusUnknownRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUnknownRoutes.setStatus("current")
_SonusDirectoryConfigObjects_ObjectIdentity = ObjectIdentity
sonusDirectoryConfigObjects = _SonusDirectoryConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2)
)


class _SonusDsCountryCode_Type(DisplayString):
    """Custom type sonusDsCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_SonusDsCountryCode_Type.__name__ = "DisplayString"
_SonusDsCountryCode_Object = MibScalar
sonusDsCountryCode = _SonusDsCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2, 1),
    _SonusDsCountryCode_Type()
)
sonusDsCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsCountryCode.setStatus("current")


class _SonusDsMaxRemoteTg_Type(Integer32):
    """Custom type sonusDsMaxRemoteTg based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_SonusDsMaxRemoteTg_Type.__name__ = "Integer32"
_SonusDsMaxRemoteTg_Object = MibScalar
sonusDsMaxRemoteTg = _SonusDsMaxRemoteTg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2, 2),
    _SonusDsMaxRemoteTg_Type()
)
sonusDsMaxRemoteTg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsMaxRemoteTg.setStatus("current")


class _SonusDsMaxRouteNames_Type(Integer32):
    """Custom type sonusDsMaxRouteNames based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_SonusDsMaxRouteNames_Type.__name__ = "Integer32"
_SonusDsMaxRouteNames_Object = MibScalar
sonusDsMaxRouteNames = _SonusDsMaxRouteNames_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2, 3),
    _SonusDsMaxRouteNames_Type()
)
sonusDsMaxRouteNames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsMaxRouteNames.setStatus("current")


class _SonusDsAccess_Type(Integer32):
    """Custom type sonusDsAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_SonusDsAccess_Type.__name__ = "Integer32"
_SonusDsAccess_Object = MibScalar
sonusDsAccess = _SonusDsAccess_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2, 4),
    _SonusDsAccess_Type()
)
sonusDsAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsAccess.setStatus("current")


class _SonusDsMaxTables_Type(Integer32):
    """Custom type sonusDsMaxTables based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SonusDsMaxTables_Type.__name__ = "Integer32"
_SonusDsMaxTables_Object = MibScalar
sonusDsMaxTables = _SonusDsMaxTables_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2, 5),
    _SonusDsMaxTables_Type()
)
sonusDsMaxTables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsMaxTables.setStatus("current")


class _SonusDsMaxAddresses_Type(Integer32):
    """Custom type sonusDsMaxAddresses based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SonusDsMaxAddresses_Type.__name__ = "Integer32"
_SonusDsMaxAddresses_Object = MibScalar
sonusDsMaxAddresses = _SonusDsMaxAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2, 6),
    _SonusDsMaxAddresses_Type()
)
sonusDsMaxAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsMaxAddresses.setStatus("current")


class _SonusDsMaxTollFreePrefixes_Type(Integer32):
    """Custom type sonusDsMaxTollFreePrefixes based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusDsMaxTollFreePrefixes_Type.__name__ = "Integer32"
_SonusDsMaxTollFreePrefixes_Object = MibScalar
sonusDsMaxTollFreePrefixes = _SonusDsMaxTollFreePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 2, 7),
    _SonusDsMaxTollFreePrefixes_Type()
)
sonusDsMaxTollFreePrefixes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsMaxTollFreePrefixes.setStatus("current")
_SonusTollFreeObjects_ObjectIdentity = ObjectIdentity
sonusTollFreeObjects = _SonusTollFreeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 3)
)
_SonusDsTollFreeNpaTable_Object = MibTable
sonusDsTollFreeNpaTable = _SonusDsTollFreeNpaTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sonusDsTollFreeNpaTable.setStatus("current")
_SonusDsTollFreeNpaEntry_Object = MibTableRow
sonusDsTollFreeNpaEntry = _SonusDsTollFreeNpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 3, 1, 1)
)
sonusDsTollFreeNpaEntry.setIndexNames(
    (0, "SONUS-DIRECTORY-SERVICES-MIB", "sonusDsTollFreeNpaIndex"),
)
if mibBuilder.loadTexts:
    sonusDsTollFreeNpaEntry.setStatus("current")
_SonusDsTollFreeNpaIndex_Type = Integer32
_SonusDsTollFreeNpaIndex_Object = MibTableColumn
sonusDsTollFreeNpaIndex = _SonusDsTollFreeNpaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 3, 1, 1, 1),
    _SonusDsTollFreeNpaIndex_Type()
)
sonusDsTollFreeNpaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDsTollFreeNpaIndex.setStatus("current")


class _SonusDsTollFreeNpaNumber_Type(DisplayString):
    """Custom type sonusDsTollFreeNpaNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_SonusDsTollFreeNpaNumber_Type.__name__ = "DisplayString"
_SonusDsTollFreeNpaNumber_Object = MibTableColumn
sonusDsTollFreeNpaNumber = _SonusDsTollFreeNpaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 3, 1, 1, 2),
    _SonusDsTollFreeNpaNumber_Type()
)
sonusDsTollFreeNpaNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsTollFreeNpaNumber.setStatus("current")


class _SonusDsTollFreeNpaAdminState_Type(Integer32):
    """Custom type sonusDsTollFreeNpaAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusDsTollFreeNpaAdminState_Type.__name__ = "Integer32"
_SonusDsTollFreeNpaAdminState_Object = MibTableColumn
sonusDsTollFreeNpaAdminState = _SonusDsTollFreeNpaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 3, 1, 1, 3),
    _SonusDsTollFreeNpaAdminState_Type()
)
sonusDsTollFreeNpaAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsTollFreeNpaAdminState.setStatus("current")
_SonusDsTollFreeNpaRowStatus_Type = RowStatus
_SonusDsTollFreeNpaRowStatus_Object = MibTableColumn
sonusDsTollFreeNpaRowStatus = _SonusDsTollFreeNpaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 1, 1, 3, 1, 1, 4),
    _SonusDsTollFreeNpaRowStatus_Type()
)
sonusDsTollFreeNpaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusDsTollFreeNpaRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-DIRECTORY-SERVICES-MIB",
    **{"sonusDirectoryServicesMIB": sonusDirectoryServicesMIB,
       "sonusDirectoryServicesMIBObjects": sonusDirectoryServicesMIBObjects,
       "sonusRouteObjects": sonusRouteObjects,
       "sonusRouteNameObjects": sonusRouteNameObjects,
       "sonusDsRouteNameNextIndex": sonusDsRouteNameNextIndex,
       "sonusDsRouteNameTable": sonusDsRouteNameTable,
       "sonusDsRouteNameEntry": sonusDsRouteNameEntry,
       "sonusDsNameRouteTableIndex": sonusDsNameRouteTableIndex,
       "sonusDsRouteNameIndex": sonusDsRouteNameIndex,
       "sonusDsRouteName": sonusDsRouteName,
       "sonusDsRoute1TgName": sonusDsRoute1TgName,
       "sonusDsRoute2TgName": sonusDsRoute2TgName,
       "sonusDsRoute3TgName": sonusDsRoute3TgName,
       "sonusDsRoute4TgName": sonusDsRoute4TgName,
       "sonusDsRouteNameAdminState": sonusDsRouteNameAdminState,
       "sonusDsRouteNameRowStatus": sonusDsRouteNameRowStatus,
       "sonusRouteTableObjects": sonusRouteTableObjects,
       "sonusDsRouteTableNextIndex": sonusDsRouteTableNextIndex,
       "sonusDsRouteTable": sonusDsRouteTable,
       "sonusDsRouteTableEntry": sonusDsRouteTableEntry,
       "sonusDsRouteTableIndex": sonusDsRouteTableIndex,
       "sonusDsRouteTableName": sonusDsRouteTableName,
       "sonusDsRouteTableType": sonusDsRouteTableType,
       "sonusDsMaxDigits": sonusDsMaxDigits,
       "sonusDsMaxRoutes": sonusDsMaxRoutes,
       "sonusDsTableCountryCode": sonusDsTableCountryCode,
       "sonusDsRouteTableAdminState": sonusDsRouteTableAdminState,
       "sonusDsRouteTableRowStatus": sonusDsRouteTableRowStatus,
       "sonusRouteAddressObjects": sonusRouteAddressObjects,
       "sonusDsAddressRouteTable": sonusDsAddressRouteTable,
       "sonusDsAddressRouteEntry": sonusDsAddressRouteEntry,
       "sonusDsAddressRouteTableIndex": sonusDsAddressRouteTableIndex,
       "sonusDsAddressRouteIndex": sonusDsAddressRouteIndex,
       "sonusDsAddressCountryCode": sonusDsAddressCountryCode,
       "sonusDsAddress": sonusDsAddress,
       "sonusDsAddressRouteName": sonusDsAddressRouteName,
       "sonusDsAddressRouteAdminState": sonusDsAddressRouteAdminState,
       "sonusDsAddressRouteRowStatus": sonusDsAddressRouteRowStatus,
       "sonusDestinationTrunkObjects": sonusDestinationTrunkObjects,
       "sonusDsDestTgNextIndex": sonusDsDestTgNextIndex,
       "sonusDsDestTgTable": sonusDsDestTgTable,
       "sonusDsDestTgEntry": sonusDsDestTgEntry,
       "sonusDsDestTgIndex": sonusDsDestTgIndex,
       "sonusDsDestTgName": sonusDsDestTgName,
       "sonusDsDestTrunk": sonusDsDestTrunk,
       "sonusDsDestTgSignaling": sonusDsDestTgSignaling,
       "sonusDsDestGwName": sonusDsDestGwName,
       "sonusDsDestCarrier": sonusDsDestCarrier,
       "sonusDsDestTgAdminState": sonusDsDestTgAdminState,
       "sonusDsDestTgRowStatus": sonusDsDestTgRowStatus,
       "sonusRouteStatusObjects": sonusRouteStatusObjects,
       "sonusUnknownRoutes": sonusUnknownRoutes,
       "sonusDirectoryConfigObjects": sonusDirectoryConfigObjects,
       "sonusDsCountryCode": sonusDsCountryCode,
       "sonusDsMaxRemoteTg": sonusDsMaxRemoteTg,
       "sonusDsMaxRouteNames": sonusDsMaxRouteNames,
       "sonusDsAccess": sonusDsAccess,
       "sonusDsMaxTables": sonusDsMaxTables,
       "sonusDsMaxAddresses": sonusDsMaxAddresses,
       "sonusDsMaxTollFreePrefixes": sonusDsMaxTollFreePrefixes,
       "sonusTollFreeObjects": sonusTollFreeObjects,
       "sonusDsTollFreeNpaTable": sonusDsTollFreeNpaTable,
       "sonusDsTollFreeNpaEntry": sonusDsTollFreeNpaEntry,
       "sonusDsTollFreeNpaIndex": sonusDsTollFreeNpaIndex,
       "sonusDsTollFreeNpaNumber": sonusDsTollFreeNpaNumber,
       "sonusDsTollFreeNpaAdminState": sonusDsTollFreeNpaAdminState,
       "sonusDsTollFreeNpaRowStatus": sonusDsTollFreeNpaRowStatus}
)
