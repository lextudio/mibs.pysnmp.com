# SNMP MIB module (CISCO-DMN-DSG-FAVORITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-FAVORITE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:23 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGFavorite = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29)
)
ciscoDSGFavorite.setRevisions(
        ("2010-08-30 11:00",
         "2010-05-11 09:30",
         "2010-04-12 06:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FavoriteCtrl_ObjectIdentity = ObjectIdentity
favoriteCtrl = _FavoriteCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 1)
)


class _FavoriteCtrlID_Type(Integer32):
    """Custom type favoriteCtrlID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("favorite1", 1),
          ("favorite2", 2),
          ("favorite3", 3),
          ("favorite4", 4),
          ("favorite5", 5),
          ("favorite6", 6))
    )


_FavoriteCtrlID_Type.__name__ = "Integer32"
_FavoriteCtrlID_Object = MibScalar
favoriteCtrlID = _FavoriteCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 1, 1),
    _FavoriteCtrlID_Type()
)
favoriteCtrlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    favoriteCtrlID.setStatus("current")


class _FavoriteCtrlCmd_Type(Integer32):
    """Custom type favoriteCtrlCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("change", 2),
          ("writeOnly", 1))
    )


_FavoriteCtrlCmd_Type.__name__ = "Integer32"
_FavoriteCtrlCmd_Object = MibScalar
favoriteCtrlCmd = _FavoriteCtrlCmd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 1, 2),
    _FavoriteCtrlCmd_Type()
)
favoriteCtrlCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    favoriteCtrlCmd.setStatus("current")


class _FavoriteChScanMode_Type(Integer32):
    """Custom type favoriteChScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("authorizedOnly", 2))
    )


_FavoriteChScanMode_Type.__name__ = "Integer32"
_FavoriteChScanMode_Object = MibScalar
favoriteChScanMode = _FavoriteChScanMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 1, 3),
    _FavoriteChScanMode_Type()
)
favoriteChScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    favoriteChScanMode.setStatus("current")
_FavoriteTable_ObjectIdentity = ObjectIdentity
favoriteTable = _FavoriteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2)
)
_FavoriteListTable_Object = MibTable
favoriteListTable = _FavoriteListTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1)
)
if mibBuilder.loadTexts:
    favoriteListTable.setStatus("current")
_FavoriteListEntry_Object = MibTableRow
favoriteListEntry = _FavoriteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1, 1)
)
favoriteListEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FAVORITE-MIB", "favoriteListID"),
)
if mibBuilder.loadTexts:
    favoriteListEntry.setStatus("current")


class _FavoriteListID_Type(Integer32):
    """Custom type favoriteListID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("favorite1", 1),
          ("favorite2", 2),
          ("favorite3", 3),
          ("favorite4", 4),
          ("favorite5", 5),
          ("favorite6", 6))
    )


_FavoriteListID_Type.__name__ = "Integer32"
_FavoriteListID_Object = MibTableColumn
favoriteListID = _FavoriteListID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1, 1, 1),
    _FavoriteListID_Type()
)
favoriteListID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    favoriteListID.setStatus("current")


class _FavoriteListPosition_Type(Integer32):
    """Custom type favoriteListPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FavoriteListPosition_Type.__name__ = "Integer32"
_FavoriteListPosition_Object = MibTableColumn
favoriteListPosition = _FavoriteListPosition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1, 1, 2),
    _FavoriteListPosition_Type()
)
favoriteListPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    favoriteListPosition.setStatus("current")


class _FavoriteListName_Type(DisplayString):
    """Custom type favoriteListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FavoriteListName_Type.__name__ = "DisplayString"
_FavoriteListName_Object = MibTableColumn
favoriteListName = _FavoriteListName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1, 1, 3),
    _FavoriteListName_Type()
)
favoriteListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    favoriteListName.setStatus("current")


class _FavoriteListType_Type(Integer32):
    """Custom type favoriteListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("providerRadio", 3),
          ("providerTv", 4),
          ("userRadio", 1),
          ("userTv", 2))
    )


_FavoriteListType_Type.__name__ = "Integer32"
_FavoriteListType_Object = MibTableColumn
favoriteListType = _FavoriteListType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1, 1, 4),
    _FavoriteListType_Type()
)
favoriteListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    favoriteListType.setStatus("current")


class _FavoriteListChLastViewed_Type(Integer32):
    """Custom type favoriteListChLastViewed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FavoriteListChLastViewed_Type.__name__ = "Integer32"
_FavoriteListChLastViewed_Object = MibTableColumn
favoriteListChLastViewed = _FavoriteListChLastViewed_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1, 1, 5),
    _FavoriteListChLastViewed_Type()
)
favoriteListChLastViewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    favoriteListChLastViewed.setStatus("current")
_FavoriteListRowStatus_Type = RowStatus
_FavoriteListRowStatus_Object = MibTableColumn
favoriteListRowStatus = _FavoriteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 1, 1, 6),
    _FavoriteListRowStatus_Type()
)
favoriteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    favoriteListRowStatus.setStatus("current")
_FavoriteMapTable_Object = MibTable
favoriteMapTable = _FavoriteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 2)
)
if mibBuilder.loadTexts:
    favoriteMapTable.setStatus("current")
_FavoriteMapEntry_Object = MibTableRow
favoriteMapEntry = _FavoriteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 2, 1)
)
favoriteMapEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FAVORITE-MIB", "favoriteMapID"),
    (0, "CISCO-DMN-DSG-FAVORITE-MIB", "favoriteMapChPosition"),
)
if mibBuilder.loadTexts:
    favoriteMapEntry.setStatus("current")


class _FavoriteMapID_Type(Integer32):
    """Custom type favoriteMapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("favorite3", 3),
          ("favorite4", 4),
          ("favorite5", 5),
          ("favorite6", 6))
    )


_FavoriteMapID_Type.__name__ = "Integer32"
_FavoriteMapID_Object = MibTableColumn
favoriteMapID = _FavoriteMapID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 2, 1, 1),
    _FavoriteMapID_Type()
)
favoriteMapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    favoriteMapID.setStatus("current")


class _FavoriteMapChPosition_Type(Integer32):
    """Custom type favoriteMapChPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_FavoriteMapChPosition_Type.__name__ = "Integer32"
_FavoriteMapChPosition_Object = MibTableColumn
favoriteMapChPosition = _FavoriteMapChPosition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 2, 1, 2),
    _FavoriteMapChPosition_Type()
)
favoriteMapChPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    favoriteMapChPosition.setStatus("current")


class _FavoriteMapChNum_Type(Integer32):
    """Custom type favoriteMapChNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FavoriteMapChNum_Type.__name__ = "Integer32"
_FavoriteMapChNum_Object = MibTableColumn
favoriteMapChNum = _FavoriteMapChNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 2, 1, 3),
    _FavoriteMapChNum_Type()
)
favoriteMapChNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    favoriteMapChNum.setStatus("current")
_FavoriteMapRowStatus_Type = RowStatus
_FavoriteMapRowStatus_Object = MibTableColumn
favoriteMapRowStatus = _FavoriteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 29, 2, 2, 1, 4),
    _FavoriteMapRowStatus_Type()
)
favoriteMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    favoriteMapRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-FAVORITE-MIB",
    **{"ciscoDSGFavorite": ciscoDSGFavorite,
       "favoriteCtrl": favoriteCtrl,
       "favoriteCtrlID": favoriteCtrlID,
       "favoriteCtrlCmd": favoriteCtrlCmd,
       "favoriteChScanMode": favoriteChScanMode,
       "favoriteTable": favoriteTable,
       "favoriteListTable": favoriteListTable,
       "favoriteListEntry": favoriteListEntry,
       "favoriteListID": favoriteListID,
       "favoriteListPosition": favoriteListPosition,
       "favoriteListName": favoriteListName,
       "favoriteListType": favoriteListType,
       "favoriteListChLastViewed": favoriteListChLastViewed,
       "favoriteListRowStatus": favoriteListRowStatus,
       "favoriteMapTable": favoriteMapTable,
       "favoriteMapEntry": favoriteMapEntry,
       "favoriteMapID": favoriteMapID,
       "favoriteMapChPosition": favoriteMapChPosition,
       "favoriteMapChNum": favoriteMapChNum,
       "favoriteMapRowStatus": favoriteMapRowStatus}
)
