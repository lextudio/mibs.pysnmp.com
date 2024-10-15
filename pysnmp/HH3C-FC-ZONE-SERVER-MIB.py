# SNMP MIB module (HH3C-FC-ZONE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FC-ZONE-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:21 2024
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

(Hh3cFcNameId,) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcNameId")

(hh3cSan,
 hh3cVsanIndex) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan",
    "hh3cVsanIndex")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(t11ZsActiveZoneIndex,
 t11ZsActiveZoneMemberIndex) = mibBuilder.importSymbols(
    "T11-FC-ZONE-SERVER-MIB",
    "t11ZsActiveZoneIndex",
    "t11ZsActiveZoneMemberIndex")


# MODULE-IDENTITY

hh3cFcZoneServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9)
)
hh3cFcZoneServer.setRevisions(
        ("2013-12-25 15:07",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cFcZsGenName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class Hh3cFcZsGenNameOrZero(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class Hh3cFcZsZoneMemberType(Integer32, TextualConvention):
    status = "current"
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
        *(("aliasName", 4),
          ("fcid", 1),
          ("fwwn", 2),
          ("pwwn", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cFcZoneMibObjects_ObjectIdentity = ObjectIdentity
hh3cFcZoneMibObjects = _Hh3cFcZoneMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1)
)
_Hh3cFcZsConfiguration_ObjectIdentity = ObjectIdentity
hh3cFcZsConfiguration = _Hh3cFcZsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1)
)
_Hh3cFcZsServerTable_Object = MibTable
hh3cFcZsServerTable = _Hh3cFcZsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFcZsServerTable.setStatus("current")
_Hh3cFcZsServerEntry_Object = MibTableRow
hh3cFcZsServerEntry = _Hh3cFcZsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1, 1)
)
hh3cFcZsServerEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsServerEntry.setStatus("current")


class _Hh3cFcZsZoneModeCfg_Type(Integer32):
    """Custom type hh3cFcZsZoneModeCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhanced", 2))
    )


_Hh3cFcZsZoneModeCfg_Type.__name__ = "Integer32"
_Hh3cFcZsZoneModeCfg_Object = MibTableColumn
hh3cFcZsZoneModeCfg = _Hh3cFcZsZoneModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1, 1, 1),
    _Hh3cFcZsZoneModeCfg_Type()
)
hh3cFcZsZoneModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsZoneModeCfg.setStatus("current")
_Hh3cFcZsHardZoneEnable_Type = TruthValue
_Hh3cFcZsHardZoneEnable_Object = MibTableColumn
hh3cFcZsHardZoneEnable = _Hh3cFcZsHardZoneEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1, 1, 2),
    _Hh3cFcZsHardZoneEnable_Type()
)
hh3cFcZsHardZoneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsHardZoneEnable.setStatus("current")


class _Hh3cFcZsDistributeRule_Type(Integer32):
    """Custom type hh3cFcZsDistributeRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeOnly", 2),
          ("full", 3),
          ("none", 1))
    )


_Hh3cFcZsDistributeRule_Type.__name__ = "Integer32"
_Hh3cFcZsDistributeRule_Object = MibTableColumn
hh3cFcZsDistributeRule = _Hh3cFcZsDistributeRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1, 1, 3),
    _Hh3cFcZsDistributeRule_Type()
)
hh3cFcZsDistributeRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsDistributeRule.setStatus("current")


class _Hh3cFcZsDefaultZoneSetting_Type(Integer32):
    """Custom type hh3cFcZsDefaultZoneSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_Hh3cFcZsDefaultZoneSetting_Type.__name__ = "Integer32"
_Hh3cFcZsDefaultZoneSetting_Object = MibTableColumn
hh3cFcZsDefaultZoneSetting = _Hh3cFcZsDefaultZoneSetting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1, 1, 4),
    _Hh3cFcZsDefaultZoneSetting_Type()
)
hh3cFcZsDefaultZoneSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsDefaultZoneSetting.setStatus("current")


class _Hh3cFcZsMergeControlSetting_Type(Integer32):
    """Custom type hh3cFcZsMergeControlSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("none", 1),
          ("restrict", 3))
    )


_Hh3cFcZsMergeControlSetting_Type.__name__ = "Integer32"
_Hh3cFcZsMergeControlSetting_Object = MibTableColumn
hh3cFcZsMergeControlSetting = _Hh3cFcZsMergeControlSetting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1, 1, 5),
    _Hh3cFcZsMergeControlSetting_Type()
)
hh3cFcZsMergeControlSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsMergeControlSetting.setStatus("current")


class _Hh3cFcZsServerLastResult_Type(Integer32):
    """Custom type hh3cFcZsServerLastResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("activeZoneSetTooBig", 7),
          ("busy", 3),
          ("noSupportInBasic", 5),
          ("noSupportInEnhanced", 6),
          ("noSupportInFabric", 4),
          ("none", 1),
          ("otherFault", 8),
          ("success", 2))
    )


_Hh3cFcZsServerLastResult_Type.__name__ = "Integer32"
_Hh3cFcZsServerLastResult_Object = MibTableColumn
hh3cFcZsServerLastResult = _Hh3cFcZsServerLastResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 1, 1, 6),
    _Hh3cFcZsServerLastResult_Type()
)
hh3cFcZsServerLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsServerLastResult.setStatus("current")
_Hh3cFcZsZonesetTable_Object = MibTable
hh3cFcZsZonesetTable = _Hh3cFcZsZonesetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFcZsZonesetTable.setStatus("current")
_Hh3cFcZsZonesetEntry_Object = MibTableRow
hh3cFcZsZonesetEntry = _Hh3cFcZsZonesetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 2, 1)
)
hh3cFcZsZonesetEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZonesetIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsZonesetEntry.setStatus("current")


class _Hh3cFcZsZonesetIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZonesetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZonesetIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZonesetIndex_Object = MibTableColumn
hh3cFcZsZonesetIndex = _Hh3cFcZsZonesetIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 2, 1, 1),
    _Hh3cFcZsZonesetIndex_Type()
)
hh3cFcZsZonesetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcZsZonesetIndex.setStatus("current")
_Hh3cFcZsZonesetName_Type = Hh3cFcZsGenName
_Hh3cFcZsZonesetName_Object = MibTableColumn
hh3cFcZsZonesetName = _Hh3cFcZsZonesetName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 2, 1, 2),
    _Hh3cFcZsZonesetName_Type()
)
hh3cFcZsZonesetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZonesetName.setStatus("current")
_Hh3cFcZsZonesetRowStatus_Type = RowStatus
_Hh3cFcZsZonesetRowStatus_Object = MibTableColumn
hh3cFcZsZonesetRowStatus = _Hh3cFcZsZonesetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 2, 1, 3),
    _Hh3cFcZsZonesetRowStatus_Type()
)
hh3cFcZsZonesetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZonesetRowStatus.setStatus("current")
_Hh3cFcZsZoneTable_Object = MibTable
hh3cFcZsZoneTable = _Hh3cFcZsZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneTable.setStatus("current")
_Hh3cFcZsZoneEntry_Object = MibTableRow
hh3cFcZsZoneEntry = _Hh3cFcZsZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 3, 1)
)
hh3cFcZsZoneEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneEntry.setStatus("current")


class _Hh3cFcZsZoneIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZoneIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneIndex_Object = MibTableColumn
hh3cFcZsZoneIndex = _Hh3cFcZsZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 3, 1, 1),
    _Hh3cFcZsZoneIndex_Type()
)
hh3cFcZsZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcZsZoneIndex.setStatus("current")
_Hh3cFcZsZoneName_Type = Hh3cFcZsGenName
_Hh3cFcZsZoneName_Object = MibTableColumn
hh3cFcZsZoneName = _Hh3cFcZsZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 3, 1, 2),
    _Hh3cFcZsZoneName_Type()
)
hh3cFcZsZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneName.setStatus("current")


class _Hh3cFcZsZonePairwiseEnable_Type(TruthValue):
    """Custom type hh3cFcZsZonePairwiseEnable based on TruthValue"""


_Hh3cFcZsZonePairwiseEnable_Object = MibTableColumn
hh3cFcZsZonePairwiseEnable = _Hh3cFcZsZonePairwiseEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 3, 1, 3),
    _Hh3cFcZsZonePairwiseEnable_Type()
)
hh3cFcZsZonePairwiseEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZonePairwiseEnable.setStatus("current")
_Hh3cFcZsZoneRowStatus_Type = RowStatus
_Hh3cFcZsZoneRowStatus_Object = MibTableColumn
hh3cFcZsZoneRowStatus = _Hh3cFcZsZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 3, 1, 4),
    _Hh3cFcZsZoneRowStatus_Type()
)
hh3cFcZsZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneRowStatus.setStatus("current")
_Hh3cFcZsSetZoneTable_Object = MibTable
hh3cFcZsSetZoneTable = _Hh3cFcZsSetZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cFcZsSetZoneTable.setStatus("current")
_Hh3cFcZsSetZoneEntry_Object = MibTableRow
hh3cFcZsSetZoneEntry = _Hh3cFcZsSetZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 4, 1)
)
hh3cFcZsSetZoneEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZonesetIndex"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsSetZoneEntry.setStatus("current")
_Hh3cFcZsSetZoneRowStatus_Type = RowStatus
_Hh3cFcZsSetZoneRowStatus_Object = MibTableColumn
hh3cFcZsSetZoneRowStatus = _Hh3cFcZsSetZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 4, 1, 1),
    _Hh3cFcZsSetZoneRowStatus_Type()
)
hh3cFcZsSetZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsSetZoneRowStatus.setStatus("current")
_Hh3cFcZsZoneAliasTable_Object = MibTable
hh3cFcZsZoneAliasTable = _Hh3cFcZsZoneAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneAliasTable.setStatus("current")
_Hh3cFcZsZoneAliasEntry_Object = MibTableRow
hh3cFcZsZoneAliasEntry = _Hh3cFcZsZoneAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 5, 1)
)
hh3cFcZsZoneAliasEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneAliasIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneAliasEntry.setStatus("current")


class _Hh3cFcZsZoneAliasIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZoneAliasIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZoneAliasIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneAliasIndex_Object = MibTableColumn
hh3cFcZsZoneAliasIndex = _Hh3cFcZsZoneAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 5, 1, 1),
    _Hh3cFcZsZoneAliasIndex_Type()
)
hh3cFcZsZoneAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcZsZoneAliasIndex.setStatus("current")
_Hh3cFcZsZoneAliasName_Type = Hh3cFcZsGenName
_Hh3cFcZsZoneAliasName_Object = MibTableColumn
hh3cFcZsZoneAliasName = _Hh3cFcZsZoneAliasName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 5, 1, 2),
    _Hh3cFcZsZoneAliasName_Type()
)
hh3cFcZsZoneAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneAliasName.setStatus("current")
_Hh3cFcZsZoneAliasRowStatus_Type = RowStatus
_Hh3cFcZsZoneAliasRowStatus_Object = MibTableColumn
hh3cFcZsZoneAliasRowStatus = _Hh3cFcZsZoneAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 5, 1, 3),
    _Hh3cFcZsZoneAliasRowStatus_Type()
)
hh3cFcZsZoneAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneAliasRowStatus.setStatus("current")
_Hh3cFcZsZoneMemberTable_Object = MibTable
hh3cFcZsZoneMemberTable = _Hh3cFcZsZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberTable.setStatus("current")
_Hh3cFcZsZoneMemberEntry_Object = MibTableRow
hh3cFcZsZoneMemberEntry = _Hh3cFcZsZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1)
)
hh3cFcZsZoneMemberEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneMemberParentType"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneMemberParentIndex"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberEntry.setStatus("current")


class _Hh3cFcZsZoneMemberParentType_Type(Integer32):
    """Custom type hh3cFcZsZoneMemberParentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alias", 2),
          ("zone", 1))
    )


_Hh3cFcZsZoneMemberParentType_Type.__name__ = "Integer32"
_Hh3cFcZsZoneMemberParentType_Object = MibTableColumn
hh3cFcZsZoneMemberParentType = _Hh3cFcZsZoneMemberParentType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1, 1),
    _Hh3cFcZsZoneMemberParentType_Type()
)
hh3cFcZsZoneMemberParentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberParentType.setStatus("current")


class _Hh3cFcZsZoneMemberParentIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZoneMemberParentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZoneMemberParentIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneMemberParentIndex_Object = MibTableColumn
hh3cFcZsZoneMemberParentIndex = _Hh3cFcZsZoneMemberParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1, 2),
    _Hh3cFcZsZoneMemberParentIndex_Type()
)
hh3cFcZsZoneMemberParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberParentIndex.setStatus("current")


class _Hh3cFcZsZoneMemberIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZoneMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZoneMemberIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneMemberIndex_Object = MibTableColumn
hh3cFcZsZoneMemberIndex = _Hh3cFcZsZoneMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1, 3),
    _Hh3cFcZsZoneMemberIndex_Type()
)
hh3cFcZsZoneMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberIndex.setStatus("current")
_Hh3cFcZsZoneMemberFormat_Type = Hh3cFcZsZoneMemberType
_Hh3cFcZsZoneMemberFormat_Object = MibTableColumn
hh3cFcZsZoneMemberFormat = _Hh3cFcZsZoneMemberFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1, 4),
    _Hh3cFcZsZoneMemberFormat_Type()
)
hh3cFcZsZoneMemberFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberFormat.setStatus("current")


class _Hh3cFcZsZoneMemberIdentifier_Type(OctetString):
    """Custom type hh3cFcZsZoneMemberIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cFcZsZoneMemberIdentifier_Type.__name__ = "OctetString"
_Hh3cFcZsZoneMemberIdentifier_Object = MibTableColumn
hh3cFcZsZoneMemberIdentifier = _Hh3cFcZsZoneMemberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1, 5),
    _Hh3cFcZsZoneMemberIdentifier_Type()
)
hh3cFcZsZoneMemberIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberIdentifier.setStatus("current")


class _Hh3cFcZsZoneMemberPairwiseRole_Type(Integer32):
    """Custom type hh3cFcZsZoneMemberPairwiseRole based on Integer32"""
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
        *(("both", 2),
          ("initiator", 3),
          ("none", 1),
          ("target", 4))
    )


_Hh3cFcZsZoneMemberPairwiseRole_Type.__name__ = "Integer32"
_Hh3cFcZsZoneMemberPairwiseRole_Object = MibTableColumn
hh3cFcZsZoneMemberPairwiseRole = _Hh3cFcZsZoneMemberPairwiseRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1, 6),
    _Hh3cFcZsZoneMemberPairwiseRole_Type()
)
hh3cFcZsZoneMemberPairwiseRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberPairwiseRole.setStatus("current")
_Hh3cFcZsZoneMemberRowStatus_Type = RowStatus
_Hh3cFcZsZoneMemberRowStatus_Object = MibTableColumn
hh3cFcZsZoneMemberRowStatus = _Hh3cFcZsZoneMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 1, 6, 1, 7),
    _Hh3cFcZsZoneMemberRowStatus_Type()
)
hh3cFcZsZoneMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberRowStatus.setStatus("current")
_Hh3cFcZsOperation_ObjectIdentity = ObjectIdentity
hh3cFcZsOperation = _Hh3cFcZsOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2)
)
_Hh3cFcZsActivateTable_Object = MibTable
hh3cFcZsActivateTable = _Hh3cFcZsActivateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFcZsActivateTable.setStatus("current")
_Hh3cFcZsActivateEntry_Object = MibTableRow
hh3cFcZsActivateEntry = _Hh3cFcZsActivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 1, 1)
)
hh3cFcZsActivateEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsActivateEntry.setStatus("current")
_Hh3cFcZsActivate_Type = Hh3cFcZsGenNameOrZero
_Hh3cFcZsActivate_Object = MibTableColumn
hh3cFcZsActivate = _Hh3cFcZsActivate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 1, 1, 1),
    _Hh3cFcZsActivate_Type()
)
hh3cFcZsActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsActivate.setStatus("current")


class _Hh3cFcZsDeactivate_Type(Integer32):
    """Custom type hh3cFcZsDeactivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deactivate", 2),
          ("noOper", 1))
    )


_Hh3cFcZsDeactivate_Type.__name__ = "Integer32"
_Hh3cFcZsDeactivate_Object = MibTableColumn
hh3cFcZsDeactivate = _Hh3cFcZsDeactivate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 1, 1, 2),
    _Hh3cFcZsDeactivate_Type()
)
hh3cFcZsDeactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsDeactivate.setStatus("current")


class _Hh3cFcZsActivateResult_Type(Integer32):
    """Custom type hh3cFcZsActivateResult based on Integer32"""
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
        *(("activateFailure", 4),
          ("activateSuccess", 3),
          ("deactivateFailure", 6),
          ("deactivateSuccess", 5),
          ("inProgress", 2),
          ("none", 1))
    )


_Hh3cFcZsActivateResult_Type.__name__ = "Integer32"
_Hh3cFcZsActivateResult_Object = MibTableColumn
hh3cFcZsActivateResult = _Hh3cFcZsActivateResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 1, 1, 3),
    _Hh3cFcZsActivateResult_Type()
)
hh3cFcZsActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsActivateResult.setStatus("current")


class _Hh3cFcZsActivateFailReason_Type(Integer32):
    """Custom type hh3cFcZsActivateFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activeZoneSetTooBig", 3),
          ("busy", 2),
          ("noMember", 5),
          ("noZoneSet", 4),
          ("none", 1))
    )


_Hh3cFcZsActivateFailReason_Type.__name__ = "Integer32"
_Hh3cFcZsActivateFailReason_Object = MibTableColumn
hh3cFcZsActivateFailReason = _Hh3cFcZsActivateFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 1, 1, 4),
    _Hh3cFcZsActivateFailReason_Type()
)
hh3cFcZsActivateFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsActivateFailReason.setStatus("current")
_Hh3cFcZsDistributeTable_Object = MibTable
hh3cFcZsDistributeTable = _Hh3cFcZsDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cFcZsDistributeTable.setStatus("current")
_Hh3cFcZsDistributeEntry_Object = MibTableRow
hh3cFcZsDistributeEntry = _Hh3cFcZsDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 2, 1)
)
hh3cFcZsDistributeEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsDistributeEntry.setStatus("current")


class _Hh3cFcZsDistribute_Type(Integer32):
    """Custom type hh3cFcZsDistribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distribute", 2),
          ("noOper", 1))
    )


_Hh3cFcZsDistribute_Type.__name__ = "Integer32"
_Hh3cFcZsDistribute_Object = MibTableColumn
hh3cFcZsDistribute = _Hh3cFcZsDistribute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 2, 1, 1),
    _Hh3cFcZsDistribute_Type()
)
hh3cFcZsDistribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsDistribute.setStatus("current")


class _Hh3cFcZsDistributeLastResult_Type(Integer32):
    """Custom type hh3cFcZsDistributeLastResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 3),
          ("none", 1),
          ("otherFault", 5),
          ("rejectFailure", 4),
          ("success", 2))
    )


_Hh3cFcZsDistributeLastResult_Type.__name__ = "Integer32"
_Hh3cFcZsDistributeLastResult_Object = MibTableColumn
hh3cFcZsDistributeLastResult = _Hh3cFcZsDistributeLastResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 2, 1, 2),
    _Hh3cFcZsDistributeLastResult_Type()
)
hh3cFcZsDistributeLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsDistributeLastResult.setStatus("current")
_Hh3cFcZsDistributeReasonCode_Type = Unsigned32
_Hh3cFcZsDistributeReasonCode_Object = MibTableColumn
hh3cFcZsDistributeReasonCode = _Hh3cFcZsDistributeReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 2, 1, 3),
    _Hh3cFcZsDistributeReasonCode_Type()
)
hh3cFcZsDistributeReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsDistributeReasonCode.setStatus("current")
_Hh3cFcZsDistributeExplainCode_Type = Unsigned32
_Hh3cFcZsDistributeExplainCode_Object = MibTableColumn
hh3cFcZsDistributeExplainCode = _Hh3cFcZsDistributeExplainCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 2, 1, 4),
    _Hh3cFcZsDistributeExplainCode_Type()
)
hh3cFcZsDistributeExplainCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsDistributeExplainCode.setStatus("current")
_Hh3cFcZsClearDatabaseTable_Object = MibTable
hh3cFcZsClearDatabaseTable = _Hh3cFcZsClearDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cFcZsClearDatabaseTable.setStatus("current")
_Hh3cFcZsClearDatabaseEntry_Object = MibTableRow
hh3cFcZsClearDatabaseEntry = _Hh3cFcZsClearDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 3, 1)
)
hh3cFcZsClearDatabaseEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsClearDatabaseEntry.setStatus("current")


class _Hh3cFcZsClearDatabase_Type(Integer32):
    """Custom type hh3cFcZsClearDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearDb", 2),
          ("noOper", 1))
    )


_Hh3cFcZsClearDatabase_Type.__name__ = "Integer32"
_Hh3cFcZsClearDatabase_Object = MibTableColumn
hh3cFcZsClearDatabase = _Hh3cFcZsClearDatabase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 3, 1, 1),
    _Hh3cFcZsClearDatabase_Type()
)
hh3cFcZsClearDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsClearDatabase.setStatus("current")
_Hh3cFcZsClearPktStatsTable_Object = MibTable
hh3cFcZsClearPktStatsTable = _Hh3cFcZsClearPktStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cFcZsClearPktStatsTable.setStatus("current")
_Hh3cFcZsClearPktStatsEntry_Object = MibTableRow
hh3cFcZsClearPktStatsEntry = _Hh3cFcZsClearPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 4, 1)
)
hh3cFcZsClearPktStatsEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsClearPktStatsEntry.setStatus("current")


class _Hh3cFcZsClearPktStats_Type(Integer32):
    """Custom type hh3cFcZsClearPktStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearStats", 2),
          ("noOper", 1))
    )


_Hh3cFcZsClearPktStats_Type.__name__ = "Integer32"
_Hh3cFcZsClearPktStats_Object = MibTableColumn
hh3cFcZsClearPktStats = _Hh3cFcZsClearPktStats_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 4, 1, 1),
    _Hh3cFcZsClearPktStats_Type()
)
hh3cFcZsClearPktStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsClearPktStats.setStatus("current")


class _Hh3cFcZsClearAllPktStats_Type(Integer32):
    """Custom type hh3cFcZsClearAllPktStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearStats", 2),
          ("noOper", 1))
    )


_Hh3cFcZsClearAllPktStats_Type.__name__ = "Integer32"
_Hh3cFcZsClearAllPktStats_Object = MibScalar
hh3cFcZsClearAllPktStats = _Hh3cFcZsClearAllPktStats_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 2, 5),
    _Hh3cFcZsClearAllPktStats_Type()
)
hh3cFcZsClearAllPktStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsClearAllPktStats.setStatus("current")
_Hh3cFcZsInformation_ObjectIdentity = ObjectIdentity
hh3cFcZsInformation = _Hh3cFcZsInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3)
)
_Hh3cFcZsActiveZoneTable_Object = MibTable
hh3cFcZsActiveZoneTable = _Hh3cFcZsActiveZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cFcZsActiveZoneTable.setStatus("current")
_Hh3cFcZsActiveZoneEntry_Object = MibTableRow
hh3cFcZsActiveZoneEntry = _Hh3cFcZsActiveZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 1, 1)
)
hh3cFcZsActiveZoneEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsActiveZoneEntry.setStatus("current")
_Hh3cFcZsActiveZonePairwiseEnable_Type = TruthValue
_Hh3cFcZsActiveZonePairwiseEnable_Object = MibTableColumn
hh3cFcZsActiveZonePairwiseEnable = _Hh3cFcZsActiveZonePairwiseEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 1, 1, 1),
    _Hh3cFcZsActiveZonePairwiseEnable_Type()
)
hh3cFcZsActiveZonePairwiseEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsActiveZonePairwiseEnable.setStatus("current")
_Hh3cFcZsActiveMemberTable_Object = MibTable
hh3cFcZsActiveMemberTable = _Hh3cFcZsActiveMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cFcZsActiveMemberTable.setStatus("current")
_Hh3cFcZsActiveMemberEntry_Object = MibTableRow
hh3cFcZsActiveMemberEntry = _Hh3cFcZsActiveMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 2, 1)
)
hh3cFcZsActiveMemberEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsActiveMemberEntry.setStatus("current")


class _Hh3cFcZsActiveMemberPairwiseRole_Type(Integer32):
    """Custom type hh3cFcZsActiveMemberPairwiseRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("initiator", 2),
          ("target", 3))
    )


_Hh3cFcZsActiveMemberPairwiseRole_Type.__name__ = "Integer32"
_Hh3cFcZsActiveMemberPairwiseRole_Object = MibTableColumn
hh3cFcZsActiveMemberPairwiseRole = _Hh3cFcZsActiveMemberPairwiseRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 2, 1, 1),
    _Hh3cFcZsActiveMemberPairwiseRole_Type()
)
hh3cFcZsActiveMemberPairwiseRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsActiveMemberPairwiseRole.setStatus("current")
_Hh3cFcZsServerStatusTable_Object = MibTable
hh3cFcZsServerStatusTable = _Hh3cFcZsServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cFcZsServerStatusTable.setStatus("current")
_Hh3cFcZsServerStatusEntry_Object = MibTableRow
hh3cFcZsServerStatusEntry = _Hh3cFcZsServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 3, 1)
)
hh3cFcZsServerStatusEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsServerStatusEntry.setStatus("current")


class _Hh3cFcZsServerStatus_Type(Integer32):
    """Custom type hh3cFcZsServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("distribute", 2),
          ("free", 1),
          ("merge", 3))
    )


_Hh3cFcZsServerStatus_Type.__name__ = "Integer32"
_Hh3cFcZsServerStatus_Object = MibTableColumn
hh3cFcZsServerStatus = _Hh3cFcZsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 3, 1, 1),
    _Hh3cFcZsServerStatus_Type()
)
hh3cFcZsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsServerStatus.setStatus("current")


class _Hh3cFcZsHardZoneStatus_Type(Integer32):
    """Custom type hh3cFcZsHardZoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDisable", 2),
          ("enable", 1),
          ("noResourceDisable", 3))
    )


_Hh3cFcZsHardZoneStatus_Type.__name__ = "Integer32"
_Hh3cFcZsHardZoneStatus_Object = MibTableColumn
hh3cFcZsHardZoneStatus = _Hh3cFcZsHardZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 3, 1, 2),
    _Hh3cFcZsHardZoneStatus_Type()
)
hh3cFcZsHardZoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsHardZoneStatus.setStatus("current")


class _Hh3cFcZsAliasCount_Type(Unsigned32):
    """Custom type hh3cFcZsAliasCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cFcZsAliasCount_Type.__name__ = "Unsigned32"
_Hh3cFcZsAliasCount_Object = MibTableColumn
hh3cFcZsAliasCount = _Hh3cFcZsAliasCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 3, 1, 3),
    _Hh3cFcZsAliasCount_Type()
)
hh3cFcZsAliasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsAliasCount.setStatus("current")


class _Hh3cFcZsZoneCount_Type(Unsigned32):
    """Custom type hh3cFcZsZoneCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cFcZsZoneCount_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneCount_Object = MibTableColumn
hh3cFcZsZoneCount = _Hh3cFcZsZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 3, 1, 4),
    _Hh3cFcZsZoneCount_Type()
)
hh3cFcZsZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsZoneCount.setStatus("current")


class _Hh3cFcZsZonesetCount_Type(Unsigned32):
    """Custom type hh3cFcZsZonesetCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cFcZsZonesetCount_Type.__name__ = "Unsigned32"
_Hh3cFcZsZonesetCount_Object = MibTableColumn
hh3cFcZsZonesetCount = _Hh3cFcZsZonesetCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 3, 1, 5),
    _Hh3cFcZsZonesetCount_Type()
)
hh3cFcZsZonesetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsZonesetCount.setStatus("current")
_Hh3cFcZsPktStatsTable_Object = MibTable
hh3cFcZsPktStatsTable = _Hh3cFcZsPktStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cFcZsPktStatsTable.setStatus("current")
_Hh3cFcZsPktStatsEntry_Object = MibTableRow
hh3cFcZsPktStatsEntry = _Hh3cFcZsPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1)
)
hh3cFcZsPktStatsEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsPktStatsEntry.setStatus("current")
_Hh3cFcZsPktInMergeReqCount_Type = Counter64
_Hh3cFcZsPktInMergeReqCount_Object = MibTableColumn
hh3cFcZsPktInMergeReqCount = _Hh3cFcZsPktInMergeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 1),
    _Hh3cFcZsPktInMergeReqCount_Type()
)
hh3cFcZsPktInMergeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktInMergeReqCount.setStatus("current")
_Hh3cFcZsPktOutMergeReqCount_Type = Counter64
_Hh3cFcZsPktOutMergeReqCount_Object = MibTableColumn
hh3cFcZsPktOutMergeReqCount = _Hh3cFcZsPktOutMergeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 2),
    _Hh3cFcZsPktOutMergeReqCount_Type()
)
hh3cFcZsPktOutMergeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktOutMergeReqCount.setStatus("current")
_Hh3cFcZsPktInMergeAccCount_Type = Counter64
_Hh3cFcZsPktInMergeAccCount_Object = MibTableColumn
hh3cFcZsPktInMergeAccCount = _Hh3cFcZsPktInMergeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 3),
    _Hh3cFcZsPktInMergeAccCount_Type()
)
hh3cFcZsPktInMergeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktInMergeAccCount.setStatus("current")
_Hh3cFcZsPktOutMergeAccCount_Type = Counter64
_Hh3cFcZsPktOutMergeAccCount_Object = MibTableColumn
hh3cFcZsPktOutMergeAccCount = _Hh3cFcZsPktOutMergeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 4),
    _Hh3cFcZsPktOutMergeAccCount_Type()
)
hh3cFcZsPktOutMergeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktOutMergeAccCount.setStatus("current")
_Hh3cFcZsPktInMergeRjtCount_Type = Counter64
_Hh3cFcZsPktInMergeRjtCount_Object = MibTableColumn
hh3cFcZsPktInMergeRjtCount = _Hh3cFcZsPktInMergeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 5),
    _Hh3cFcZsPktInMergeRjtCount_Type()
)
hh3cFcZsPktInMergeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktInMergeRjtCount.setStatus("current")
_Hh3cFcZsPktOutMergeRjtCount_Type = Counter64
_Hh3cFcZsPktOutMergeRjtCount_Object = MibTableColumn
hh3cFcZsPktOutMergeRjtCount = _Hh3cFcZsPktOutMergeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 6),
    _Hh3cFcZsPktOutMergeRjtCount_Type()
)
hh3cFcZsPktOutMergeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktOutMergeRjtCount.setStatus("current")
_Hh3cFcZsPktInChangeReqCount_Type = Counter64
_Hh3cFcZsPktInChangeReqCount_Object = MibTableColumn
hh3cFcZsPktInChangeReqCount = _Hh3cFcZsPktInChangeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 7),
    _Hh3cFcZsPktInChangeReqCount_Type()
)
hh3cFcZsPktInChangeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktInChangeReqCount.setStatus("current")
_Hh3cFcZsPktOutChangeReqCount_Type = Counter64
_Hh3cFcZsPktOutChangeReqCount_Object = MibTableColumn
hh3cFcZsPktOutChangeReqCount = _Hh3cFcZsPktOutChangeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 8),
    _Hh3cFcZsPktOutChangeReqCount_Type()
)
hh3cFcZsPktOutChangeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktOutChangeReqCount.setStatus("current")
_Hh3cFcZsPktInChangeAccCount_Type = Counter64
_Hh3cFcZsPktInChangeAccCount_Object = MibTableColumn
hh3cFcZsPktInChangeAccCount = _Hh3cFcZsPktInChangeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 9),
    _Hh3cFcZsPktInChangeAccCount_Type()
)
hh3cFcZsPktInChangeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktInChangeAccCount.setStatus("current")
_Hh3cFcZsPktOutChangeAccCount_Type = Counter64
_Hh3cFcZsPktOutChangeAccCount_Object = MibTableColumn
hh3cFcZsPktOutChangeAccCount = _Hh3cFcZsPktOutChangeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 10),
    _Hh3cFcZsPktOutChangeAccCount_Type()
)
hh3cFcZsPktOutChangeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktOutChangeAccCount.setStatus("current")
_Hh3cFcZsPktInChangeRjtCount_Type = Counter64
_Hh3cFcZsPktInChangeRjtCount_Object = MibTableColumn
hh3cFcZsPktInChangeRjtCount = _Hh3cFcZsPktInChangeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 11),
    _Hh3cFcZsPktInChangeRjtCount_Type()
)
hh3cFcZsPktInChangeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktInChangeRjtCount.setStatus("current")
_Hh3cFcZsPktOutChangeRjtCount_Type = Counter64
_Hh3cFcZsPktOutChangeRjtCount_Object = MibTableColumn
hh3cFcZsPktOutChangeRjtCount = _Hh3cFcZsPktOutChangeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 4, 1, 12),
    _Hh3cFcZsPktOutChangeRjtCount_Type()
)
hh3cFcZsPktOutChangeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsPktOutChangeRjtCount.setStatus("current")
_Hh3cFcZsNextFreeIndexInfo_ObjectIdentity = ObjectIdentity
hh3cFcZsNextFreeIndexInfo = _Hh3cFcZsNextFreeIndexInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 5)
)


class _Hh3cFcZsZonesetNextFreeIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZonesetNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZonesetNextFreeIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZonesetNextFreeIndex_Object = MibScalar
hh3cFcZsZonesetNextFreeIndex = _Hh3cFcZsZonesetNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 5, 1),
    _Hh3cFcZsZonesetNextFreeIndex_Type()
)
hh3cFcZsZonesetNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsZonesetNextFreeIndex.setStatus("current")


class _Hh3cFcZsZoneNextFreeIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZoneNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZoneNextFreeIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneNextFreeIndex_Object = MibScalar
hh3cFcZsZoneNextFreeIndex = _Hh3cFcZsZoneNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 5, 2),
    _Hh3cFcZsZoneNextFreeIndex_Type()
)
hh3cFcZsZoneNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsZoneNextFreeIndex.setStatus("current")


class _Hh3cFcZsZoneAliasNextFreeIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZoneAliasNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZoneAliasNextFreeIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneAliasNextFreeIndex_Object = MibScalar
hh3cFcZsZoneAliasNextFreeIndex = _Hh3cFcZsZoneAliasNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 5, 3),
    _Hh3cFcZsZoneAliasNextFreeIndex_Type()
)
hh3cFcZsZoneAliasNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsZoneAliasNextFreeIndex.setStatus("current")
_Hh3cFcZsZoneMemberNextFreeIndexTable_Object = MibTable
hh3cFcZsZoneMemberNextFreeIndexTable = _Hh3cFcZsZoneMemberNextFreeIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberNextFreeIndexTable.setStatus("current")
_Hh3cFcZsZoneMemberNextFreeIndexEntry_Object = MibTableRow
hh3cFcZsZoneMemberNextFreeIndexEntry = _Hh3cFcZsZoneMemberNextFreeIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 5, 4, 1)
)
hh3cFcZsZoneMemberNextFreeIndexEntry.setIndexNames(
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneMemberParentType"),
    (0, "HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsZoneMemberParentIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberNextFreeIndexEntry.setStatus("current")


class _Hh3cFcZsZoneMemberNextFreeIndex_Type(Unsigned32):
    """Custom type hh3cFcZsZoneMemberNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cFcZsZoneMemberNextFreeIndex_Type.__name__ = "Unsigned32"
_Hh3cFcZsZoneMemberNextFreeIndex_Object = MibTableColumn
hh3cFcZsZoneMemberNextFreeIndex = _Hh3cFcZsZoneMemberNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 3, 5, 4, 1, 1),
    _Hh3cFcZsZoneMemberNextFreeIndex_Type()
)
hh3cFcZsZoneMemberNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcZsZoneMemberNextFreeIndex.setStatus("current")
_Hh3cFcZsNotification_ObjectIdentity = ObjectIdentity
hh3cFcZsNotification = _Hh3cFcZsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4)
)
_Hh3cFcZsNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cFcZsNotificationPrefix = _Hh3cFcZsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 0)
)
_Hh3cFcZsNotificationSwitch_ObjectIdentity = ObjectIdentity
hh3cFcZsNotificationSwitch = _Hh3cFcZsNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 1)
)
_Hh3cFcZsDefaultZoneChangedEnable_Type = TruthValue
_Hh3cFcZsDefaultZoneChangedEnable_Object = MibScalar
hh3cFcZsDefaultZoneChangedEnable = _Hh3cFcZsDefaultZoneChangedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 1, 1),
    _Hh3cFcZsDefaultZoneChangedEnable_Type()
)
hh3cFcZsDefaultZoneChangedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsDefaultZoneChangedEnable.setStatus("current")
_Hh3cFcZsHardZoneChangedEnable_Type = TruthValue
_Hh3cFcZsHardZoneChangedEnable_Object = MibScalar
hh3cFcZsHardZoneChangedEnable = _Hh3cFcZsHardZoneChangedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 1, 2),
    _Hh3cFcZsHardZoneChangedEnable_Type()
)
hh3cFcZsHardZoneChangedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsHardZoneChangedEnable.setStatus("current")
_Hh3cFcZsMergeFailedEnable_Type = TruthValue
_Hh3cFcZsMergeFailedEnable_Object = MibScalar
hh3cFcZsMergeFailedEnable = _Hh3cFcZsMergeFailedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 1, 3),
    _Hh3cFcZsMergeFailedEnable_Type()
)
hh3cFcZsMergeFailedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsMergeFailedEnable.setStatus("current")
_Hh3cFcZsMergeSucceededEnable_Type = TruthValue
_Hh3cFcZsMergeSucceededEnable_Object = MibScalar
hh3cFcZsMergeSucceededEnable = _Hh3cFcZsMergeSucceededEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 1, 4),
    _Hh3cFcZsMergeSucceededEnable_Type()
)
hh3cFcZsMergeSucceededEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsMergeSucceededEnable.setStatus("current")
_Hh3cFcZsActivationCompletedEnable_Type = TruthValue
_Hh3cFcZsActivationCompletedEnable_Object = MibScalar
hh3cFcZsActivationCompletedEnable = _Hh3cFcZsActivationCompletedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 1, 5),
    _Hh3cFcZsActivationCompletedEnable_Type()
)
hh3cFcZsActivationCompletedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcZsActivationCompletedEnable.setStatus("current")
_Hh3cFcZsObjsForNotification_ObjectIdentity = ObjectIdentity
hh3cFcZsObjsForNotification = _Hh3cFcZsObjsForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 2)
)
_Hh3cFcZsLocalSwitchWWN_Type = Hh3cFcNameId
_Hh3cFcZsLocalSwitchWWN_Object = MibScalar
hh3cFcZsLocalSwitchWWN = _Hh3cFcZsLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 2, 1),
    _Hh3cFcZsLocalSwitchWWN_Type()
)
hh3cFcZsLocalSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFcZsLocalSwitchWWN.setStatus("current")
_Hh3cFcZsPeerSwitchWWN_Type = Hh3cFcNameId
_Hh3cFcZsPeerSwitchWWN_Object = MibScalar
hh3cFcZsPeerSwitchWWN = _Hh3cFcZsPeerSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 2, 2),
    _Hh3cFcZsPeerSwitchWWN_Type()
)
hh3cFcZsPeerSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFcZsPeerSwitchWWN.setStatus("current")


class _Hh3cFcZsMergeFailCause_Type(Integer32):
    """Custom type hh3cFcZsMergeFailCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("activeZoneSetMergeFailed", 5),
          ("dataNotEqualInRestrict", 4),
          ("hardZoneInconsistent", 3),
          ("other", 10),
          ("zoneDbMergeFaildInBasic", 8),
          ("zoneDbMergeFaildInEnhanced", 9),
          ("zoneMergeDataTooBig", 6),
          ("zoneModeInconsistent", 1),
          ("zonePolicyNotEqual", 2),
          ("zoningObjectNumberTooBig", 7))
    )


_Hh3cFcZsMergeFailCause_Type.__name__ = "Integer32"
_Hh3cFcZsMergeFailCause_Object = MibScalar
hh3cFcZsMergeFailCause = _Hh3cFcZsMergeFailCause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 2, 3),
    _Hh3cFcZsMergeFailCause_Type()
)
hh3cFcZsMergeFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFcZsMergeFailCause.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cFcZsDefaultZoneChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 0, 1)
)
hh3cFcZsDefaultZoneChangedNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsLocalSwitchWWN"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsDefaultZoneSetting"))
)
if mibBuilder.loadTexts:
    hh3cFcZsDefaultZoneChangedNotify.setStatus(
        "current"
    )

hh3cFcZsHardZoneChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 0, 2)
)
hh3cFcZsHardZoneChangedNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsLocalSwitchWWN"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsHardZoneStatus"))
)
if mibBuilder.loadTexts:
    hh3cFcZsHardZoneChangedNotify.setStatus(
        "current"
    )

hh3cFcZsMergeFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 0, 3)
)
hh3cFcZsMergeFailedNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsLocalSwitchWWN"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsPeerSwitchWWN"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsMergeFailCause"))
)
if mibBuilder.loadTexts:
    hh3cFcZsMergeFailedNotify.setStatus(
        "current"
    )

hh3cFcZsMergeSucceededNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 0, 4)
)
hh3cFcZsMergeSucceededNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsLocalSwitchWWN"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsPeerSwitchWWN"))
)
if mibBuilder.loadTexts:
    hh3cFcZsMergeSucceededNotify.setStatus(
        "current"
    )

hh3cFcZsActivationCompletedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 9, 1, 4, 0, 5)
)
hh3cFcZsActivationCompletedNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsLocalSwitchWWN"),
        ("HH3C-FC-ZONE-SERVER-MIB", "hh3cFcZsActivateResult"))
)
if mibBuilder.loadTexts:
    hh3cFcZsActivationCompletedNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FC-ZONE-SERVER-MIB",
    **{"Hh3cFcZsGenName": Hh3cFcZsGenName,
       "Hh3cFcZsGenNameOrZero": Hh3cFcZsGenNameOrZero,
       "Hh3cFcZsZoneMemberType": Hh3cFcZsZoneMemberType,
       "hh3cFcZoneServer": hh3cFcZoneServer,
       "hh3cFcZoneMibObjects": hh3cFcZoneMibObjects,
       "hh3cFcZsConfiguration": hh3cFcZsConfiguration,
       "hh3cFcZsServerTable": hh3cFcZsServerTable,
       "hh3cFcZsServerEntry": hh3cFcZsServerEntry,
       "hh3cFcZsZoneModeCfg": hh3cFcZsZoneModeCfg,
       "hh3cFcZsHardZoneEnable": hh3cFcZsHardZoneEnable,
       "hh3cFcZsDistributeRule": hh3cFcZsDistributeRule,
       "hh3cFcZsDefaultZoneSetting": hh3cFcZsDefaultZoneSetting,
       "hh3cFcZsMergeControlSetting": hh3cFcZsMergeControlSetting,
       "hh3cFcZsServerLastResult": hh3cFcZsServerLastResult,
       "hh3cFcZsZonesetTable": hh3cFcZsZonesetTable,
       "hh3cFcZsZonesetEntry": hh3cFcZsZonesetEntry,
       "hh3cFcZsZonesetIndex": hh3cFcZsZonesetIndex,
       "hh3cFcZsZonesetName": hh3cFcZsZonesetName,
       "hh3cFcZsZonesetRowStatus": hh3cFcZsZonesetRowStatus,
       "hh3cFcZsZoneTable": hh3cFcZsZoneTable,
       "hh3cFcZsZoneEntry": hh3cFcZsZoneEntry,
       "hh3cFcZsZoneIndex": hh3cFcZsZoneIndex,
       "hh3cFcZsZoneName": hh3cFcZsZoneName,
       "hh3cFcZsZonePairwiseEnable": hh3cFcZsZonePairwiseEnable,
       "hh3cFcZsZoneRowStatus": hh3cFcZsZoneRowStatus,
       "hh3cFcZsSetZoneTable": hh3cFcZsSetZoneTable,
       "hh3cFcZsSetZoneEntry": hh3cFcZsSetZoneEntry,
       "hh3cFcZsSetZoneRowStatus": hh3cFcZsSetZoneRowStatus,
       "hh3cFcZsZoneAliasTable": hh3cFcZsZoneAliasTable,
       "hh3cFcZsZoneAliasEntry": hh3cFcZsZoneAliasEntry,
       "hh3cFcZsZoneAliasIndex": hh3cFcZsZoneAliasIndex,
       "hh3cFcZsZoneAliasName": hh3cFcZsZoneAliasName,
       "hh3cFcZsZoneAliasRowStatus": hh3cFcZsZoneAliasRowStatus,
       "hh3cFcZsZoneMemberTable": hh3cFcZsZoneMemberTable,
       "hh3cFcZsZoneMemberEntry": hh3cFcZsZoneMemberEntry,
       "hh3cFcZsZoneMemberParentType": hh3cFcZsZoneMemberParentType,
       "hh3cFcZsZoneMemberParentIndex": hh3cFcZsZoneMemberParentIndex,
       "hh3cFcZsZoneMemberIndex": hh3cFcZsZoneMemberIndex,
       "hh3cFcZsZoneMemberFormat": hh3cFcZsZoneMemberFormat,
       "hh3cFcZsZoneMemberIdentifier": hh3cFcZsZoneMemberIdentifier,
       "hh3cFcZsZoneMemberPairwiseRole": hh3cFcZsZoneMemberPairwiseRole,
       "hh3cFcZsZoneMemberRowStatus": hh3cFcZsZoneMemberRowStatus,
       "hh3cFcZsOperation": hh3cFcZsOperation,
       "hh3cFcZsActivateTable": hh3cFcZsActivateTable,
       "hh3cFcZsActivateEntry": hh3cFcZsActivateEntry,
       "hh3cFcZsActivate": hh3cFcZsActivate,
       "hh3cFcZsDeactivate": hh3cFcZsDeactivate,
       "hh3cFcZsActivateResult": hh3cFcZsActivateResult,
       "hh3cFcZsActivateFailReason": hh3cFcZsActivateFailReason,
       "hh3cFcZsDistributeTable": hh3cFcZsDistributeTable,
       "hh3cFcZsDistributeEntry": hh3cFcZsDistributeEntry,
       "hh3cFcZsDistribute": hh3cFcZsDistribute,
       "hh3cFcZsDistributeLastResult": hh3cFcZsDistributeLastResult,
       "hh3cFcZsDistributeReasonCode": hh3cFcZsDistributeReasonCode,
       "hh3cFcZsDistributeExplainCode": hh3cFcZsDistributeExplainCode,
       "hh3cFcZsClearDatabaseTable": hh3cFcZsClearDatabaseTable,
       "hh3cFcZsClearDatabaseEntry": hh3cFcZsClearDatabaseEntry,
       "hh3cFcZsClearDatabase": hh3cFcZsClearDatabase,
       "hh3cFcZsClearPktStatsTable": hh3cFcZsClearPktStatsTable,
       "hh3cFcZsClearPktStatsEntry": hh3cFcZsClearPktStatsEntry,
       "hh3cFcZsClearPktStats": hh3cFcZsClearPktStats,
       "hh3cFcZsClearAllPktStats": hh3cFcZsClearAllPktStats,
       "hh3cFcZsInformation": hh3cFcZsInformation,
       "hh3cFcZsActiveZoneTable": hh3cFcZsActiveZoneTable,
       "hh3cFcZsActiveZoneEntry": hh3cFcZsActiveZoneEntry,
       "hh3cFcZsActiveZonePairwiseEnable": hh3cFcZsActiveZonePairwiseEnable,
       "hh3cFcZsActiveMemberTable": hh3cFcZsActiveMemberTable,
       "hh3cFcZsActiveMemberEntry": hh3cFcZsActiveMemberEntry,
       "hh3cFcZsActiveMemberPairwiseRole": hh3cFcZsActiveMemberPairwiseRole,
       "hh3cFcZsServerStatusTable": hh3cFcZsServerStatusTable,
       "hh3cFcZsServerStatusEntry": hh3cFcZsServerStatusEntry,
       "hh3cFcZsServerStatus": hh3cFcZsServerStatus,
       "hh3cFcZsHardZoneStatus": hh3cFcZsHardZoneStatus,
       "hh3cFcZsAliasCount": hh3cFcZsAliasCount,
       "hh3cFcZsZoneCount": hh3cFcZsZoneCount,
       "hh3cFcZsZonesetCount": hh3cFcZsZonesetCount,
       "hh3cFcZsPktStatsTable": hh3cFcZsPktStatsTable,
       "hh3cFcZsPktStatsEntry": hh3cFcZsPktStatsEntry,
       "hh3cFcZsPktInMergeReqCount": hh3cFcZsPktInMergeReqCount,
       "hh3cFcZsPktOutMergeReqCount": hh3cFcZsPktOutMergeReqCount,
       "hh3cFcZsPktInMergeAccCount": hh3cFcZsPktInMergeAccCount,
       "hh3cFcZsPktOutMergeAccCount": hh3cFcZsPktOutMergeAccCount,
       "hh3cFcZsPktInMergeRjtCount": hh3cFcZsPktInMergeRjtCount,
       "hh3cFcZsPktOutMergeRjtCount": hh3cFcZsPktOutMergeRjtCount,
       "hh3cFcZsPktInChangeReqCount": hh3cFcZsPktInChangeReqCount,
       "hh3cFcZsPktOutChangeReqCount": hh3cFcZsPktOutChangeReqCount,
       "hh3cFcZsPktInChangeAccCount": hh3cFcZsPktInChangeAccCount,
       "hh3cFcZsPktOutChangeAccCount": hh3cFcZsPktOutChangeAccCount,
       "hh3cFcZsPktInChangeRjtCount": hh3cFcZsPktInChangeRjtCount,
       "hh3cFcZsPktOutChangeRjtCount": hh3cFcZsPktOutChangeRjtCount,
       "hh3cFcZsNextFreeIndexInfo": hh3cFcZsNextFreeIndexInfo,
       "hh3cFcZsZonesetNextFreeIndex": hh3cFcZsZonesetNextFreeIndex,
       "hh3cFcZsZoneNextFreeIndex": hh3cFcZsZoneNextFreeIndex,
       "hh3cFcZsZoneAliasNextFreeIndex": hh3cFcZsZoneAliasNextFreeIndex,
       "hh3cFcZsZoneMemberNextFreeIndexTable": hh3cFcZsZoneMemberNextFreeIndexTable,
       "hh3cFcZsZoneMemberNextFreeIndexEntry": hh3cFcZsZoneMemberNextFreeIndexEntry,
       "hh3cFcZsZoneMemberNextFreeIndex": hh3cFcZsZoneMemberNextFreeIndex,
       "hh3cFcZsNotification": hh3cFcZsNotification,
       "hh3cFcZsNotificationPrefix": hh3cFcZsNotificationPrefix,
       "hh3cFcZsDefaultZoneChangedNotify": hh3cFcZsDefaultZoneChangedNotify,
       "hh3cFcZsHardZoneChangedNotify": hh3cFcZsHardZoneChangedNotify,
       "hh3cFcZsMergeFailedNotify": hh3cFcZsMergeFailedNotify,
       "hh3cFcZsMergeSucceededNotify": hh3cFcZsMergeSucceededNotify,
       "hh3cFcZsActivationCompletedNotify": hh3cFcZsActivationCompletedNotify,
       "hh3cFcZsNotificationSwitch": hh3cFcZsNotificationSwitch,
       "hh3cFcZsDefaultZoneChangedEnable": hh3cFcZsDefaultZoneChangedEnable,
       "hh3cFcZsHardZoneChangedEnable": hh3cFcZsHardZoneChangedEnable,
       "hh3cFcZsMergeFailedEnable": hh3cFcZsMergeFailedEnable,
       "hh3cFcZsMergeSucceededEnable": hh3cFcZsMergeSucceededEnable,
       "hh3cFcZsActivationCompletedEnable": hh3cFcZsActivationCompletedEnable,
       "hh3cFcZsObjsForNotification": hh3cFcZsObjsForNotification,
       "hh3cFcZsLocalSwitchWWN": hh3cFcZsLocalSwitchWWN,
       "hh3cFcZsPeerSwitchWWN": hh3cFcZsPeerSwitchWWN,
       "hh3cFcZsMergeFailCause": hh3cFcZsMergeFailCause}
)
