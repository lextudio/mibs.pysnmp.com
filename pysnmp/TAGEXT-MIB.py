# SNMP MIB module (TAGEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TAGEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:52 2024
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

(tagExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "tagExt")

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

apTagExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApTagListTable_Object = MibTable
apTagListTable = _ApTagListTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 2)
)
if mibBuilder.loadTexts:
    apTagListTable.setStatus("current")
_ApTagListEntry_Object = MibTableRow
apTagListEntry = _ApTagListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 2, 1)
)
apTagListEntry.setIndexNames(
    (0, "TAGEXT-MIB", "apTagListName"),
)
if mibBuilder.loadTexts:
    apTagListEntry.setStatus("current")


class _ApTagListName_Type(DisplayString):
    """Custom type apTagListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApTagListName_Type.__name__ = "DisplayString"
_ApTagListName_Object = MibTableColumn
apTagListName = _ApTagListName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 2, 1, 1),
    _ApTagListName_Type()
)
apTagListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagListName.setStatus("current")


class _ApTagListDescription_Type(DisplayString):
    """Custom type apTagListDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApTagListDescription_Type.__name__ = "DisplayString"
_ApTagListDescription_Object = MibTableColumn
apTagListDescription = _ApTagListDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 2, 1, 2),
    _ApTagListDescription_Type()
)
apTagListDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagListDescription.setStatus("current")
_ApTagListStatus_Type = RowStatus
_ApTagListStatus_Object = MibTableColumn
apTagListStatus = _ApTagListStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 2, 1, 3),
    _ApTagListStatus_Type()
)
apTagListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagListStatus.setStatus("current")
_ApTagInfoTable_Object = MibTable
apTagInfoTable = _ApTagInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3)
)
if mibBuilder.loadTexts:
    apTagInfoTable.setStatus("current")
_ApTagInfoEntry_Object = MibTableRow
apTagInfoEntry = _ApTagInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1)
)
apTagInfoEntry.setIndexNames(
    (0, "TAGEXT-MIB", "apTagListName"),
    (0, "TAGEXT-MIB", "apTagName"),
)
if mibBuilder.loadTexts:
    apTagInfoEntry.setStatus("current")
_ApTagIndex_Type = Integer32
_ApTagIndex_Object = MibTableColumn
apTagIndex = _ApTagIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 1),
    _ApTagIndex_Type()
)
apTagIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagIndex.setStatus("current")


class _ApTagType_Type(Integer32):
    """Custom type apTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("accept", 10),
          ("cache-control", 5),
          ("charset", 8),
          ("connection", 7),
          ("cookies", 6),
          ("encoding", 9),
          ("host", 3),
          ("language", 2),
          ("pragma", 4),
          ("referer", 11),
          ("request-line", 0),
          ("user-agent", 1))
    )


_ApTagType_Type.__name__ = "Integer32"
_ApTagType_Object = MibTableColumn
apTagType = _ApTagType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 2),
    _ApTagType_Type()
)
apTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagType.setStatus("current")


class _ApTagName_Type(DisplayString):
    """Custom type apTagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApTagName_Type.__name__ = "DisplayString"
_ApTagName_Object = MibTableColumn
apTagName = _ApTagName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 3),
    _ApTagName_Type()
)
apTagName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagName.setStatus("current")


class _ApTagDescription_Type(DisplayString):
    """Custom type apTagDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApTagDescription_Type.__name__ = "DisplayString"
_ApTagDescription_Object = MibTableColumn
apTagDescription = _ApTagDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 4),
    _ApTagDescription_Type()
)
apTagDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagDescription.setStatus("current")


class _ApTagOperator_Type(Integer32):
    """Custom type apTagOperator based on Integer32"""
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
        *(("contain", 1),
          ("equal", 3),
          ("exist", 5),
          ("not-contain", 2),
          ("not-equal", 4),
          ("not-exist", 6))
    )


_ApTagOperator_Type.__name__ = "Integer32"
_ApTagOperator_Object = MibTableColumn
apTagOperator = _ApTagOperator_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 5),
    _ApTagOperator_Type()
)
apTagOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagOperator.setStatus("current")


class _ApTagKeyword_Type(DisplayString):
    """Custom type apTagKeyword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApTagKeyword_Type.__name__ = "DisplayString"
_ApTagKeyword_Object = MibTableColumn
apTagKeyword = _ApTagKeyword_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 6),
    _ApTagKeyword_Type()
)
apTagKeyword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagKeyword.setStatus("current")


class _ApTagKeywordLen_Type(Integer32):
    """Custom type apTagKeywordLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ApTagKeywordLen_Type.__name__ = "Integer32"
_ApTagKeywordLen_Object = MibTableColumn
apTagKeywordLen = _ApTagKeywordLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 7),
    _ApTagKeywordLen_Type()
)
apTagKeywordLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagKeywordLen.setStatus("current")


class _ApTagKqlName_Type(DisplayString):
    """Custom type apTagKqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApTagKqlName_Type.__name__ = "DisplayString"
_ApTagKqlName_Object = MibTableColumn
apTagKqlName = _ApTagKqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 8),
    _ApTagKqlName_Type()
)
apTagKqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagKqlName.setStatus("current")


class _ApTagSearchLen_Type(Integer32):
    """Custom type apTagSearchLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ApTagSearchLen_Type.__name__ = "Integer32"
_ApTagSearchLen_Object = MibTableColumn
apTagSearchLen = _ApTagSearchLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 9),
    _ApTagSearchLen_Type()
)
apTagSearchLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagSearchLen.setStatus("current")
_ApTagStatus_Type = RowStatus
_ApTagStatus_Object = MibTableColumn
apTagStatus = _ApTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 3, 1, 10),
    _ApTagStatus_Type()
)
apTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apTagStatus.setStatus("current")
_ApKqlTable_Object = MibTable
apKqlTable = _ApKqlTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 4)
)
if mibBuilder.loadTexts:
    apKqlTable.setStatus("current")
_ApKqlEntry_Object = MibTableRow
apKqlEntry = _ApKqlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 4, 1)
)
apKqlEntry.setIndexNames(
    (0, "TAGEXT-MIB", "apKqlName"),
)
if mibBuilder.loadTexts:
    apKqlEntry.setStatus("current")


class _ApKqlName_Type(DisplayString):
    """Custom type apKqlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApKqlName_Type.__name__ = "DisplayString"
_ApKqlName_Object = MibTableColumn
apKqlName = _ApKqlName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 4, 1, 1),
    _ApKqlName_Type()
)
apKqlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKqlName.setStatus("current")


class _ApKqlDescription_Type(DisplayString):
    """Custom type apKqlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApKqlDescription_Type.__name__ = "DisplayString"
_ApKqlDescription_Object = MibTableColumn
apKqlDescription = _ApKqlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 4, 1, 2),
    _ApKqlDescription_Type()
)
apKqlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKqlDescription.setStatus("current")
_ApKqlStatus_Type = RowStatus
_ApKqlStatus_Object = MibTableColumn
apKqlStatus = _ApKqlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 4, 1, 3),
    _ApKqlStatus_Type()
)
apKqlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKqlStatus.setStatus("current")
_ApKeywordTable_Object = MibTable
apKeywordTable = _ApKeywordTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 5)
)
if mibBuilder.loadTexts:
    apKeywordTable.setStatus("current")
_ApKeywordEntry_Object = MibTableRow
apKeywordEntry = _ApKeywordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 5, 1)
)
apKeywordEntry.setIndexNames(
    (0, "TAGEXT-MIB", "apKqlName"),
    (0, "TAGEXT-MIB", "apKeywordStr"),
)
if mibBuilder.loadTexts:
    apKeywordEntry.setStatus("current")


class _ApKeywordStr_Type(DisplayString):
    """Custom type apKeywordStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApKeywordStr_Type.__name__ = "DisplayString"
_ApKeywordStr_Object = MibTableColumn
apKeywordStr = _ApKeywordStr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 5, 1, 1),
    _ApKeywordStr_Type()
)
apKeywordStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKeywordStr.setStatus("current")
_ApKeywordStatus_Type = RowStatus
_ApKeywordStatus_Object = MibTableColumn
apKeywordStatus = _ApKeywordStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 53, 5, 1, 2),
    _ApKeywordStatus_Type()
)
apKeywordStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apKeywordStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAGEXT-MIB",
    **{"apTagExtMib": apTagExtMib,
       "apTagListTable": apTagListTable,
       "apTagListEntry": apTagListEntry,
       "apTagListName": apTagListName,
       "apTagListDescription": apTagListDescription,
       "apTagListStatus": apTagListStatus,
       "apTagInfoTable": apTagInfoTable,
       "apTagInfoEntry": apTagInfoEntry,
       "apTagIndex": apTagIndex,
       "apTagType": apTagType,
       "apTagName": apTagName,
       "apTagDescription": apTagDescription,
       "apTagOperator": apTagOperator,
       "apTagKeyword": apTagKeyword,
       "apTagKeywordLen": apTagKeywordLen,
       "apTagKqlName": apTagKqlName,
       "apTagSearchLen": apTagSearchLen,
       "apTagStatus": apTagStatus,
       "apKqlTable": apKqlTable,
       "apKqlEntry": apKqlEntry,
       "apKqlName": apKqlName,
       "apKqlDescription": apKqlDescription,
       "apKqlStatus": apKqlStatus,
       "apKeywordTable": apKeywordTable,
       "apKeywordEntry": apKeywordEntry,
       "apKeywordStr": apKeywordStr,
       "apKeywordStatus": apKeywordStatus}
)
