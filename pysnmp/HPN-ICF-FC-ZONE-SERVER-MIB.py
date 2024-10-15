# SNMP MIB module (HPN-ICF-FC-ZONE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FC-ZONE-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:20 2024
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

(HpnicfFcNameId,) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcNameId")

(hpnicfSan,
 hpnicfVsanIndex) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan",
    "hpnicfVsanIndex")

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

hpnicfFcZoneServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9)
)
hpnicfFcZoneServer.setRevisions(
        ("2013-12-25 15:07",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfFcZsGenName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class HpnicfFcZsGenNameOrZero(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class HpnicfFcZsZoneMemberType(Integer32, TextualConvention):
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

_HpnicfFcZoneMibObjects_ObjectIdentity = ObjectIdentity
hpnicfFcZoneMibObjects = _HpnicfFcZoneMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1)
)
_HpnicfFcZsConfiguration_ObjectIdentity = ObjectIdentity
hpnicfFcZsConfiguration = _HpnicfFcZsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1)
)
_HpnicfFcZsServerTable_Object = MibTable
hpnicfFcZsServerTable = _HpnicfFcZsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcZsServerTable.setStatus("current")
_HpnicfFcZsServerEntry_Object = MibTableRow
hpnicfFcZsServerEntry = _HpnicfFcZsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1, 1)
)
hpnicfFcZsServerEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsServerEntry.setStatus("current")


class _HpnicfFcZsZoneModeCfg_Type(Integer32):
    """Custom type hpnicfFcZsZoneModeCfg based on Integer32"""
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


_HpnicfFcZsZoneModeCfg_Type.__name__ = "Integer32"
_HpnicfFcZsZoneModeCfg_Object = MibTableColumn
hpnicfFcZsZoneModeCfg = _HpnicfFcZsZoneModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1, 1, 1),
    _HpnicfFcZsZoneModeCfg_Type()
)
hpnicfFcZsZoneModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneModeCfg.setStatus("current")
_HpnicfFcZsHardZoneEnable_Type = TruthValue
_HpnicfFcZsHardZoneEnable_Object = MibTableColumn
hpnicfFcZsHardZoneEnable = _HpnicfFcZsHardZoneEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1, 1, 2),
    _HpnicfFcZsHardZoneEnable_Type()
)
hpnicfFcZsHardZoneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsHardZoneEnable.setStatus("current")


class _HpnicfFcZsDistributeRule_Type(Integer32):
    """Custom type hpnicfFcZsDistributeRule based on Integer32"""
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


_HpnicfFcZsDistributeRule_Type.__name__ = "Integer32"
_HpnicfFcZsDistributeRule_Object = MibTableColumn
hpnicfFcZsDistributeRule = _HpnicfFcZsDistributeRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1, 1, 3),
    _HpnicfFcZsDistributeRule_Type()
)
hpnicfFcZsDistributeRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsDistributeRule.setStatus("current")


class _HpnicfFcZsDefaultZoneSetting_Type(Integer32):
    """Custom type hpnicfFcZsDefaultZoneSetting based on Integer32"""
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


_HpnicfFcZsDefaultZoneSetting_Type.__name__ = "Integer32"
_HpnicfFcZsDefaultZoneSetting_Object = MibTableColumn
hpnicfFcZsDefaultZoneSetting = _HpnicfFcZsDefaultZoneSetting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1, 1, 4),
    _HpnicfFcZsDefaultZoneSetting_Type()
)
hpnicfFcZsDefaultZoneSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsDefaultZoneSetting.setStatus("current")


class _HpnicfFcZsMergeControlSetting_Type(Integer32):
    """Custom type hpnicfFcZsMergeControlSetting based on Integer32"""
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


_HpnicfFcZsMergeControlSetting_Type.__name__ = "Integer32"
_HpnicfFcZsMergeControlSetting_Object = MibTableColumn
hpnicfFcZsMergeControlSetting = _HpnicfFcZsMergeControlSetting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1, 1, 5),
    _HpnicfFcZsMergeControlSetting_Type()
)
hpnicfFcZsMergeControlSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsMergeControlSetting.setStatus("current")


class _HpnicfFcZsServerLastResult_Type(Integer32):
    """Custom type hpnicfFcZsServerLastResult based on Integer32"""
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


_HpnicfFcZsServerLastResult_Type.__name__ = "Integer32"
_HpnicfFcZsServerLastResult_Object = MibTableColumn
hpnicfFcZsServerLastResult = _HpnicfFcZsServerLastResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 1, 1, 6),
    _HpnicfFcZsServerLastResult_Type()
)
hpnicfFcZsServerLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsServerLastResult.setStatus("current")
_HpnicfFcZsZonesetTable_Object = MibTable
hpnicfFcZsZonesetTable = _HpnicfFcZsZonesetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfFcZsZonesetTable.setStatus("current")
_HpnicfFcZsZonesetEntry_Object = MibTableRow
hpnicfFcZsZonesetEntry = _HpnicfFcZsZonesetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 2, 1)
)
hpnicfFcZsZonesetEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZonesetIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsZonesetEntry.setStatus("current")


class _HpnicfFcZsZonesetIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZonesetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZonesetIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZonesetIndex_Object = MibTableColumn
hpnicfFcZsZonesetIndex = _HpnicfFcZsZonesetIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 2, 1, 1),
    _HpnicfFcZsZonesetIndex_Type()
)
hpnicfFcZsZonesetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcZsZonesetIndex.setStatus("current")
_HpnicfFcZsZonesetName_Type = HpnicfFcZsGenName
_HpnicfFcZsZonesetName_Object = MibTableColumn
hpnicfFcZsZonesetName = _HpnicfFcZsZonesetName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 2, 1, 2),
    _HpnicfFcZsZonesetName_Type()
)
hpnicfFcZsZonesetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZonesetName.setStatus("current")
_HpnicfFcZsZonesetRowStatus_Type = RowStatus
_HpnicfFcZsZonesetRowStatus_Object = MibTableColumn
hpnicfFcZsZonesetRowStatus = _HpnicfFcZsZonesetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 2, 1, 3),
    _HpnicfFcZsZonesetRowStatus_Type()
)
hpnicfFcZsZonesetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZonesetRowStatus.setStatus("current")
_HpnicfFcZsZoneTable_Object = MibTable
hpnicfFcZsZoneTable = _HpnicfFcZsZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneTable.setStatus("current")
_HpnicfFcZsZoneEntry_Object = MibTableRow
hpnicfFcZsZoneEntry = _HpnicfFcZsZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 3, 1)
)
hpnicfFcZsZoneEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneEntry.setStatus("current")


class _HpnicfFcZsZoneIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZoneIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneIndex_Object = MibTableColumn
hpnicfFcZsZoneIndex = _HpnicfFcZsZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 3, 1, 1),
    _HpnicfFcZsZoneIndex_Type()
)
hpnicfFcZsZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneIndex.setStatus("current")
_HpnicfFcZsZoneName_Type = HpnicfFcZsGenName
_HpnicfFcZsZoneName_Object = MibTableColumn
hpnicfFcZsZoneName = _HpnicfFcZsZoneName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 3, 1, 2),
    _HpnicfFcZsZoneName_Type()
)
hpnicfFcZsZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneName.setStatus("current")


class _HpnicfFcZsZonePairwiseEnable_Type(TruthValue):
    """Custom type hpnicfFcZsZonePairwiseEnable based on TruthValue"""


_HpnicfFcZsZonePairwiseEnable_Object = MibTableColumn
hpnicfFcZsZonePairwiseEnable = _HpnicfFcZsZonePairwiseEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 3, 1, 3),
    _HpnicfFcZsZonePairwiseEnable_Type()
)
hpnicfFcZsZonePairwiseEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZonePairwiseEnable.setStatus("current")
_HpnicfFcZsZoneRowStatus_Type = RowStatus
_HpnicfFcZsZoneRowStatus_Object = MibTableColumn
hpnicfFcZsZoneRowStatus = _HpnicfFcZsZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 3, 1, 4),
    _HpnicfFcZsZoneRowStatus_Type()
)
hpnicfFcZsZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneRowStatus.setStatus("current")
_HpnicfFcZsSetZoneTable_Object = MibTable
hpnicfFcZsSetZoneTable = _HpnicfFcZsSetZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfFcZsSetZoneTable.setStatus("current")
_HpnicfFcZsSetZoneEntry_Object = MibTableRow
hpnicfFcZsSetZoneEntry = _HpnicfFcZsSetZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 4, 1)
)
hpnicfFcZsSetZoneEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZonesetIndex"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsSetZoneEntry.setStatus("current")
_HpnicfFcZsSetZoneRowStatus_Type = RowStatus
_HpnicfFcZsSetZoneRowStatus_Object = MibTableColumn
hpnicfFcZsSetZoneRowStatus = _HpnicfFcZsSetZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 4, 1, 1),
    _HpnicfFcZsSetZoneRowStatus_Type()
)
hpnicfFcZsSetZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsSetZoneRowStatus.setStatus("current")
_HpnicfFcZsZoneAliasTable_Object = MibTable
hpnicfFcZsZoneAliasTable = _HpnicfFcZsZoneAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneAliasTable.setStatus("current")
_HpnicfFcZsZoneAliasEntry_Object = MibTableRow
hpnicfFcZsZoneAliasEntry = _HpnicfFcZsZoneAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 5, 1)
)
hpnicfFcZsZoneAliasEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneAliasIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneAliasEntry.setStatus("current")


class _HpnicfFcZsZoneAliasIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneAliasIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZoneAliasIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneAliasIndex_Object = MibTableColumn
hpnicfFcZsZoneAliasIndex = _HpnicfFcZsZoneAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 5, 1, 1),
    _HpnicfFcZsZoneAliasIndex_Type()
)
hpnicfFcZsZoneAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneAliasIndex.setStatus("current")
_HpnicfFcZsZoneAliasName_Type = HpnicfFcZsGenName
_HpnicfFcZsZoneAliasName_Object = MibTableColumn
hpnicfFcZsZoneAliasName = _HpnicfFcZsZoneAliasName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 5, 1, 2),
    _HpnicfFcZsZoneAliasName_Type()
)
hpnicfFcZsZoneAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneAliasName.setStatus("current")
_HpnicfFcZsZoneAliasRowStatus_Type = RowStatus
_HpnicfFcZsZoneAliasRowStatus_Object = MibTableColumn
hpnicfFcZsZoneAliasRowStatus = _HpnicfFcZsZoneAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 5, 1, 3),
    _HpnicfFcZsZoneAliasRowStatus_Type()
)
hpnicfFcZsZoneAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneAliasRowStatus.setStatus("current")
_HpnicfFcZsZoneMemberTable_Object = MibTable
hpnicfFcZsZoneMemberTable = _HpnicfFcZsZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberTable.setStatus("current")
_HpnicfFcZsZoneMemberEntry_Object = MibTableRow
hpnicfFcZsZoneMemberEntry = _HpnicfFcZsZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1)
)
hpnicfFcZsZoneMemberEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneMemberParentType"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneMemberParentIndex"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberEntry.setStatus("current")


class _HpnicfFcZsZoneMemberParentType_Type(Integer32):
    """Custom type hpnicfFcZsZoneMemberParentType based on Integer32"""
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


_HpnicfFcZsZoneMemberParentType_Type.__name__ = "Integer32"
_HpnicfFcZsZoneMemberParentType_Object = MibTableColumn
hpnicfFcZsZoneMemberParentType = _HpnicfFcZsZoneMemberParentType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1, 1),
    _HpnicfFcZsZoneMemberParentType_Type()
)
hpnicfFcZsZoneMemberParentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberParentType.setStatus("current")


class _HpnicfFcZsZoneMemberParentIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneMemberParentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZoneMemberParentIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneMemberParentIndex_Object = MibTableColumn
hpnicfFcZsZoneMemberParentIndex = _HpnicfFcZsZoneMemberParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1, 2),
    _HpnicfFcZsZoneMemberParentIndex_Type()
)
hpnicfFcZsZoneMemberParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberParentIndex.setStatus("current")


class _HpnicfFcZsZoneMemberIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZoneMemberIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneMemberIndex_Object = MibTableColumn
hpnicfFcZsZoneMemberIndex = _HpnicfFcZsZoneMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1, 3),
    _HpnicfFcZsZoneMemberIndex_Type()
)
hpnicfFcZsZoneMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberIndex.setStatus("current")
_HpnicfFcZsZoneMemberFormat_Type = HpnicfFcZsZoneMemberType
_HpnicfFcZsZoneMemberFormat_Object = MibTableColumn
hpnicfFcZsZoneMemberFormat = _HpnicfFcZsZoneMemberFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1, 4),
    _HpnicfFcZsZoneMemberFormat_Type()
)
hpnicfFcZsZoneMemberFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberFormat.setStatus("current")


class _HpnicfFcZsZoneMemberIdentifier_Type(OctetString):
    """Custom type hpnicfFcZsZoneMemberIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfFcZsZoneMemberIdentifier_Type.__name__ = "OctetString"
_HpnicfFcZsZoneMemberIdentifier_Object = MibTableColumn
hpnicfFcZsZoneMemberIdentifier = _HpnicfFcZsZoneMemberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1, 5),
    _HpnicfFcZsZoneMemberIdentifier_Type()
)
hpnicfFcZsZoneMemberIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberIdentifier.setStatus("current")


class _HpnicfFcZsZoneMemberPairwiseRole_Type(Integer32):
    """Custom type hpnicfFcZsZoneMemberPairwiseRole based on Integer32"""
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


_HpnicfFcZsZoneMemberPairwiseRole_Type.__name__ = "Integer32"
_HpnicfFcZsZoneMemberPairwiseRole_Object = MibTableColumn
hpnicfFcZsZoneMemberPairwiseRole = _HpnicfFcZsZoneMemberPairwiseRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1, 6),
    _HpnicfFcZsZoneMemberPairwiseRole_Type()
)
hpnicfFcZsZoneMemberPairwiseRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberPairwiseRole.setStatus("current")
_HpnicfFcZsZoneMemberRowStatus_Type = RowStatus
_HpnicfFcZsZoneMemberRowStatus_Object = MibTableColumn
hpnicfFcZsZoneMemberRowStatus = _HpnicfFcZsZoneMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 1, 6, 1, 7),
    _HpnicfFcZsZoneMemberRowStatus_Type()
)
hpnicfFcZsZoneMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberRowStatus.setStatus("current")
_HpnicfFcZsOperation_ObjectIdentity = ObjectIdentity
hpnicfFcZsOperation = _HpnicfFcZsOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2)
)
_HpnicfFcZsActivateTable_Object = MibTable
hpnicfFcZsActivateTable = _HpnicfFcZsActivateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcZsActivateTable.setStatus("current")
_HpnicfFcZsActivateEntry_Object = MibTableRow
hpnicfFcZsActivateEntry = _HpnicfFcZsActivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 1, 1)
)
hpnicfFcZsActivateEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsActivateEntry.setStatus("current")
_HpnicfFcZsActivate_Type = HpnicfFcZsGenNameOrZero
_HpnicfFcZsActivate_Object = MibTableColumn
hpnicfFcZsActivate = _HpnicfFcZsActivate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 1, 1, 1),
    _HpnicfFcZsActivate_Type()
)
hpnicfFcZsActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsActivate.setStatus("current")


class _HpnicfFcZsDeactivate_Type(Integer32):
    """Custom type hpnicfFcZsDeactivate based on Integer32"""
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


_HpnicfFcZsDeactivate_Type.__name__ = "Integer32"
_HpnicfFcZsDeactivate_Object = MibTableColumn
hpnicfFcZsDeactivate = _HpnicfFcZsDeactivate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 1, 1, 2),
    _HpnicfFcZsDeactivate_Type()
)
hpnicfFcZsDeactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsDeactivate.setStatus("current")


class _HpnicfFcZsActivateResult_Type(Integer32):
    """Custom type hpnicfFcZsActivateResult based on Integer32"""
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


_HpnicfFcZsActivateResult_Type.__name__ = "Integer32"
_HpnicfFcZsActivateResult_Object = MibTableColumn
hpnicfFcZsActivateResult = _HpnicfFcZsActivateResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 1, 1, 3),
    _HpnicfFcZsActivateResult_Type()
)
hpnicfFcZsActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsActivateResult.setStatus("current")


class _HpnicfFcZsActivateFailReason_Type(Integer32):
    """Custom type hpnicfFcZsActivateFailReason based on Integer32"""
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


_HpnicfFcZsActivateFailReason_Type.__name__ = "Integer32"
_HpnicfFcZsActivateFailReason_Object = MibTableColumn
hpnicfFcZsActivateFailReason = _HpnicfFcZsActivateFailReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 1, 1, 4),
    _HpnicfFcZsActivateFailReason_Type()
)
hpnicfFcZsActivateFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsActivateFailReason.setStatus("current")
_HpnicfFcZsDistributeTable_Object = MibTable
hpnicfFcZsDistributeTable = _HpnicfFcZsDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfFcZsDistributeTable.setStatus("current")
_HpnicfFcZsDistributeEntry_Object = MibTableRow
hpnicfFcZsDistributeEntry = _HpnicfFcZsDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 2, 1)
)
hpnicfFcZsDistributeEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsDistributeEntry.setStatus("current")


class _HpnicfFcZsDistribute_Type(Integer32):
    """Custom type hpnicfFcZsDistribute based on Integer32"""
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


_HpnicfFcZsDistribute_Type.__name__ = "Integer32"
_HpnicfFcZsDistribute_Object = MibTableColumn
hpnicfFcZsDistribute = _HpnicfFcZsDistribute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 2, 1, 1),
    _HpnicfFcZsDistribute_Type()
)
hpnicfFcZsDistribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsDistribute.setStatus("current")


class _HpnicfFcZsDistributeLastResult_Type(Integer32):
    """Custom type hpnicfFcZsDistributeLastResult based on Integer32"""
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


_HpnicfFcZsDistributeLastResult_Type.__name__ = "Integer32"
_HpnicfFcZsDistributeLastResult_Object = MibTableColumn
hpnicfFcZsDistributeLastResult = _HpnicfFcZsDistributeLastResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 2, 1, 2),
    _HpnicfFcZsDistributeLastResult_Type()
)
hpnicfFcZsDistributeLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsDistributeLastResult.setStatus("current")
_HpnicfFcZsDistributeReasonCode_Type = Unsigned32
_HpnicfFcZsDistributeReasonCode_Object = MibTableColumn
hpnicfFcZsDistributeReasonCode = _HpnicfFcZsDistributeReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 2, 1, 3),
    _HpnicfFcZsDistributeReasonCode_Type()
)
hpnicfFcZsDistributeReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsDistributeReasonCode.setStatus("current")
_HpnicfFcZsDistributeExplainCode_Type = Unsigned32
_HpnicfFcZsDistributeExplainCode_Object = MibTableColumn
hpnicfFcZsDistributeExplainCode = _HpnicfFcZsDistributeExplainCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 2, 1, 4),
    _HpnicfFcZsDistributeExplainCode_Type()
)
hpnicfFcZsDistributeExplainCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsDistributeExplainCode.setStatus("current")
_HpnicfFcZsClearDatabaseTable_Object = MibTable
hpnicfFcZsClearDatabaseTable = _HpnicfFcZsClearDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfFcZsClearDatabaseTable.setStatus("current")
_HpnicfFcZsClearDatabaseEntry_Object = MibTableRow
hpnicfFcZsClearDatabaseEntry = _HpnicfFcZsClearDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 3, 1)
)
hpnicfFcZsClearDatabaseEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsClearDatabaseEntry.setStatus("current")


class _HpnicfFcZsClearDatabase_Type(Integer32):
    """Custom type hpnicfFcZsClearDatabase based on Integer32"""
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


_HpnicfFcZsClearDatabase_Type.__name__ = "Integer32"
_HpnicfFcZsClearDatabase_Object = MibTableColumn
hpnicfFcZsClearDatabase = _HpnicfFcZsClearDatabase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 3, 1, 1),
    _HpnicfFcZsClearDatabase_Type()
)
hpnicfFcZsClearDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsClearDatabase.setStatus("current")
_HpnicfFcZsClearPktStatsTable_Object = MibTable
hpnicfFcZsClearPktStatsTable = _HpnicfFcZsClearPktStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfFcZsClearPktStatsTable.setStatus("current")
_HpnicfFcZsClearPktStatsEntry_Object = MibTableRow
hpnicfFcZsClearPktStatsEntry = _HpnicfFcZsClearPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 4, 1)
)
hpnicfFcZsClearPktStatsEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsClearPktStatsEntry.setStatus("current")


class _HpnicfFcZsClearPktStats_Type(Integer32):
    """Custom type hpnicfFcZsClearPktStats based on Integer32"""
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


_HpnicfFcZsClearPktStats_Type.__name__ = "Integer32"
_HpnicfFcZsClearPktStats_Object = MibTableColumn
hpnicfFcZsClearPktStats = _HpnicfFcZsClearPktStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 4, 1, 1),
    _HpnicfFcZsClearPktStats_Type()
)
hpnicfFcZsClearPktStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsClearPktStats.setStatus("current")


class _HpnicfFcZsClearAllPktStats_Type(Integer32):
    """Custom type hpnicfFcZsClearAllPktStats based on Integer32"""
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


_HpnicfFcZsClearAllPktStats_Type.__name__ = "Integer32"
_HpnicfFcZsClearAllPktStats_Object = MibScalar
hpnicfFcZsClearAllPktStats = _HpnicfFcZsClearAllPktStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 2, 5),
    _HpnicfFcZsClearAllPktStats_Type()
)
hpnicfFcZsClearAllPktStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsClearAllPktStats.setStatus("current")
_HpnicfFcZsInformation_ObjectIdentity = ObjectIdentity
hpnicfFcZsInformation = _HpnicfFcZsInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3)
)
_HpnicfFcZsActiveZoneTable_Object = MibTable
hpnicfFcZsActiveZoneTable = _HpnicfFcZsActiveZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcZsActiveZoneTable.setStatus("current")
_HpnicfFcZsActiveZoneEntry_Object = MibTableRow
hpnicfFcZsActiveZoneEntry = _HpnicfFcZsActiveZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 1, 1)
)
hpnicfFcZsActiveZoneEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsActiveZoneEntry.setStatus("current")
_HpnicfFcZsActiveZonePairwiseEnable_Type = TruthValue
_HpnicfFcZsActiveZonePairwiseEnable_Object = MibTableColumn
hpnicfFcZsActiveZonePairwiseEnable = _HpnicfFcZsActiveZonePairwiseEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 1, 1, 1),
    _HpnicfFcZsActiveZonePairwiseEnable_Type()
)
hpnicfFcZsActiveZonePairwiseEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsActiveZonePairwiseEnable.setStatus("current")
_HpnicfFcZsActiveMemberTable_Object = MibTable
hpnicfFcZsActiveMemberTable = _HpnicfFcZsActiveMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfFcZsActiveMemberTable.setStatus("current")
_HpnicfFcZsActiveMemberEntry_Object = MibTableRow
hpnicfFcZsActiveMemberEntry = _HpnicfFcZsActiveMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 2, 1)
)
hpnicfFcZsActiveMemberEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsActiveMemberEntry.setStatus("current")


class _HpnicfFcZsActiveMemberPairwiseRole_Type(Integer32):
    """Custom type hpnicfFcZsActiveMemberPairwiseRole based on Integer32"""
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


_HpnicfFcZsActiveMemberPairwiseRole_Type.__name__ = "Integer32"
_HpnicfFcZsActiveMemberPairwiseRole_Object = MibTableColumn
hpnicfFcZsActiveMemberPairwiseRole = _HpnicfFcZsActiveMemberPairwiseRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 2, 1, 1),
    _HpnicfFcZsActiveMemberPairwiseRole_Type()
)
hpnicfFcZsActiveMemberPairwiseRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsActiveMemberPairwiseRole.setStatus("current")
_HpnicfFcZsServerStatusTable_Object = MibTable
hpnicfFcZsServerStatusTable = _HpnicfFcZsServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfFcZsServerStatusTable.setStatus("current")
_HpnicfFcZsServerStatusEntry_Object = MibTableRow
hpnicfFcZsServerStatusEntry = _HpnicfFcZsServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 3, 1)
)
hpnicfFcZsServerStatusEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsServerStatusEntry.setStatus("current")


class _HpnicfFcZsServerStatus_Type(Integer32):
    """Custom type hpnicfFcZsServerStatus based on Integer32"""
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


_HpnicfFcZsServerStatus_Type.__name__ = "Integer32"
_HpnicfFcZsServerStatus_Object = MibTableColumn
hpnicfFcZsServerStatus = _HpnicfFcZsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 3, 1, 1),
    _HpnicfFcZsServerStatus_Type()
)
hpnicfFcZsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsServerStatus.setStatus("current")


class _HpnicfFcZsHardZoneStatus_Type(Integer32):
    """Custom type hpnicfFcZsHardZoneStatus based on Integer32"""
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


_HpnicfFcZsHardZoneStatus_Type.__name__ = "Integer32"
_HpnicfFcZsHardZoneStatus_Object = MibTableColumn
hpnicfFcZsHardZoneStatus = _HpnicfFcZsHardZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 3, 1, 2),
    _HpnicfFcZsHardZoneStatus_Type()
)
hpnicfFcZsHardZoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsHardZoneStatus.setStatus("current")


class _HpnicfFcZsAliasCount_Type(Unsigned32):
    """Custom type hpnicfFcZsAliasCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfFcZsAliasCount_Type.__name__ = "Unsigned32"
_HpnicfFcZsAliasCount_Object = MibTableColumn
hpnicfFcZsAliasCount = _HpnicfFcZsAliasCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 3, 1, 3),
    _HpnicfFcZsAliasCount_Type()
)
hpnicfFcZsAliasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsAliasCount.setStatus("current")


class _HpnicfFcZsZoneCount_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfFcZsZoneCount_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneCount_Object = MibTableColumn
hpnicfFcZsZoneCount = _HpnicfFcZsZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 3, 1, 4),
    _HpnicfFcZsZoneCount_Type()
)
hpnicfFcZsZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneCount.setStatus("current")


class _HpnicfFcZsZonesetCount_Type(Unsigned32):
    """Custom type hpnicfFcZsZonesetCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfFcZsZonesetCount_Type.__name__ = "Unsigned32"
_HpnicfFcZsZonesetCount_Object = MibTableColumn
hpnicfFcZsZonesetCount = _HpnicfFcZsZonesetCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 3, 1, 5),
    _HpnicfFcZsZonesetCount_Type()
)
hpnicfFcZsZonesetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsZonesetCount.setStatus("current")
_HpnicfFcZsPktStatsTable_Object = MibTable
hpnicfFcZsPktStatsTable = _HpnicfFcZsPktStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hpnicfFcZsPktStatsTable.setStatus("current")
_HpnicfFcZsPktStatsEntry_Object = MibTableRow
hpnicfFcZsPktStatsEntry = _HpnicfFcZsPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1)
)
hpnicfFcZsPktStatsEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsPktStatsEntry.setStatus("current")
_HpnicfFcZsPktInMergeReqCount_Type = Counter64
_HpnicfFcZsPktInMergeReqCount_Object = MibTableColumn
hpnicfFcZsPktInMergeReqCount = _HpnicfFcZsPktInMergeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 1),
    _HpnicfFcZsPktInMergeReqCount_Type()
)
hpnicfFcZsPktInMergeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktInMergeReqCount.setStatus("current")
_HpnicfFcZsPktOutMergeReqCount_Type = Counter64
_HpnicfFcZsPktOutMergeReqCount_Object = MibTableColumn
hpnicfFcZsPktOutMergeReqCount = _HpnicfFcZsPktOutMergeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 2),
    _HpnicfFcZsPktOutMergeReqCount_Type()
)
hpnicfFcZsPktOutMergeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktOutMergeReqCount.setStatus("current")
_HpnicfFcZsPktInMergeAccCount_Type = Counter64
_HpnicfFcZsPktInMergeAccCount_Object = MibTableColumn
hpnicfFcZsPktInMergeAccCount = _HpnicfFcZsPktInMergeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 3),
    _HpnicfFcZsPktInMergeAccCount_Type()
)
hpnicfFcZsPktInMergeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktInMergeAccCount.setStatus("current")
_HpnicfFcZsPktOutMergeAccCount_Type = Counter64
_HpnicfFcZsPktOutMergeAccCount_Object = MibTableColumn
hpnicfFcZsPktOutMergeAccCount = _HpnicfFcZsPktOutMergeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 4),
    _HpnicfFcZsPktOutMergeAccCount_Type()
)
hpnicfFcZsPktOutMergeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktOutMergeAccCount.setStatus("current")
_HpnicfFcZsPktInMergeRjtCount_Type = Counter64
_HpnicfFcZsPktInMergeRjtCount_Object = MibTableColumn
hpnicfFcZsPktInMergeRjtCount = _HpnicfFcZsPktInMergeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 5),
    _HpnicfFcZsPktInMergeRjtCount_Type()
)
hpnicfFcZsPktInMergeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktInMergeRjtCount.setStatus("current")
_HpnicfFcZsPktOutMergeRjtCount_Type = Counter64
_HpnicfFcZsPktOutMergeRjtCount_Object = MibTableColumn
hpnicfFcZsPktOutMergeRjtCount = _HpnicfFcZsPktOutMergeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 6),
    _HpnicfFcZsPktOutMergeRjtCount_Type()
)
hpnicfFcZsPktOutMergeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktOutMergeRjtCount.setStatus("current")
_HpnicfFcZsPktInChangeReqCount_Type = Counter64
_HpnicfFcZsPktInChangeReqCount_Object = MibTableColumn
hpnicfFcZsPktInChangeReqCount = _HpnicfFcZsPktInChangeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 7),
    _HpnicfFcZsPktInChangeReqCount_Type()
)
hpnicfFcZsPktInChangeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktInChangeReqCount.setStatus("current")
_HpnicfFcZsPktOutChangeReqCount_Type = Counter64
_HpnicfFcZsPktOutChangeReqCount_Object = MibTableColumn
hpnicfFcZsPktOutChangeReqCount = _HpnicfFcZsPktOutChangeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 8),
    _HpnicfFcZsPktOutChangeReqCount_Type()
)
hpnicfFcZsPktOutChangeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktOutChangeReqCount.setStatus("current")
_HpnicfFcZsPktInChangeAccCount_Type = Counter64
_HpnicfFcZsPktInChangeAccCount_Object = MibTableColumn
hpnicfFcZsPktInChangeAccCount = _HpnicfFcZsPktInChangeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 9),
    _HpnicfFcZsPktInChangeAccCount_Type()
)
hpnicfFcZsPktInChangeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktInChangeAccCount.setStatus("current")
_HpnicfFcZsPktOutChangeAccCount_Type = Counter64
_HpnicfFcZsPktOutChangeAccCount_Object = MibTableColumn
hpnicfFcZsPktOutChangeAccCount = _HpnicfFcZsPktOutChangeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 10),
    _HpnicfFcZsPktOutChangeAccCount_Type()
)
hpnicfFcZsPktOutChangeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktOutChangeAccCount.setStatus("current")
_HpnicfFcZsPktInChangeRjtCount_Type = Counter64
_HpnicfFcZsPktInChangeRjtCount_Object = MibTableColumn
hpnicfFcZsPktInChangeRjtCount = _HpnicfFcZsPktInChangeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 11),
    _HpnicfFcZsPktInChangeRjtCount_Type()
)
hpnicfFcZsPktInChangeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktInChangeRjtCount.setStatus("current")
_HpnicfFcZsPktOutChangeRjtCount_Type = Counter64
_HpnicfFcZsPktOutChangeRjtCount_Object = MibTableColumn
hpnicfFcZsPktOutChangeRjtCount = _HpnicfFcZsPktOutChangeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 4, 1, 12),
    _HpnicfFcZsPktOutChangeRjtCount_Type()
)
hpnicfFcZsPktOutChangeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsPktOutChangeRjtCount.setStatus("current")
_HpnicfFcZsNextFreeIndexInfo_ObjectIdentity = ObjectIdentity
hpnicfFcZsNextFreeIndexInfo = _HpnicfFcZsNextFreeIndexInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 5)
)


class _HpnicfFcZsZonesetNextFreeIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZonesetNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZonesetNextFreeIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZonesetNextFreeIndex_Object = MibScalar
hpnicfFcZsZonesetNextFreeIndex = _HpnicfFcZsZonesetNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 5, 1),
    _HpnicfFcZsZonesetNextFreeIndex_Type()
)
hpnicfFcZsZonesetNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsZonesetNextFreeIndex.setStatus("current")


class _HpnicfFcZsZoneNextFreeIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZoneNextFreeIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneNextFreeIndex_Object = MibScalar
hpnicfFcZsZoneNextFreeIndex = _HpnicfFcZsZoneNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 5, 2),
    _HpnicfFcZsZoneNextFreeIndex_Type()
)
hpnicfFcZsZoneNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneNextFreeIndex.setStatus("current")


class _HpnicfFcZsZoneAliasNextFreeIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneAliasNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZoneAliasNextFreeIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneAliasNextFreeIndex_Object = MibScalar
hpnicfFcZsZoneAliasNextFreeIndex = _HpnicfFcZsZoneAliasNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 5, 3),
    _HpnicfFcZsZoneAliasNextFreeIndex_Type()
)
hpnicfFcZsZoneAliasNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneAliasNextFreeIndex.setStatus("current")
_HpnicfFcZsZoneMemberNextFreeIndexTable_Object = MibTable
hpnicfFcZsZoneMemberNextFreeIndexTable = _HpnicfFcZsZoneMemberNextFreeIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberNextFreeIndexTable.setStatus("current")
_HpnicfFcZsZoneMemberNextFreeIndexEntry_Object = MibTableRow
hpnicfFcZsZoneMemberNextFreeIndexEntry = _HpnicfFcZsZoneMemberNextFreeIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 5, 4, 1)
)
hpnicfFcZsZoneMemberNextFreeIndexEntry.setIndexNames(
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneMemberParentType"),
    (0, "HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsZoneMemberParentIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberNextFreeIndexEntry.setStatus("current")


class _HpnicfFcZsZoneMemberNextFreeIndex_Type(Unsigned32):
    """Custom type hpnicfFcZsZoneMemberNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfFcZsZoneMemberNextFreeIndex_Type.__name__ = "Unsigned32"
_HpnicfFcZsZoneMemberNextFreeIndex_Object = MibTableColumn
hpnicfFcZsZoneMemberNextFreeIndex = _HpnicfFcZsZoneMemberNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 3, 5, 4, 1, 1),
    _HpnicfFcZsZoneMemberNextFreeIndex_Type()
)
hpnicfFcZsZoneMemberNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcZsZoneMemberNextFreeIndex.setStatus("current")
_HpnicfFcZsNotification_ObjectIdentity = ObjectIdentity
hpnicfFcZsNotification = _HpnicfFcZsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4)
)
_HpnicfFcZsNotificationPrefix_ObjectIdentity = ObjectIdentity
hpnicfFcZsNotificationPrefix = _HpnicfFcZsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 0)
)
_HpnicfFcZsNotificationSwitch_ObjectIdentity = ObjectIdentity
hpnicfFcZsNotificationSwitch = _HpnicfFcZsNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 1)
)
_HpnicfFcZsDefaultZoneChangedEnable_Type = TruthValue
_HpnicfFcZsDefaultZoneChangedEnable_Object = MibScalar
hpnicfFcZsDefaultZoneChangedEnable = _HpnicfFcZsDefaultZoneChangedEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 1, 1),
    _HpnicfFcZsDefaultZoneChangedEnable_Type()
)
hpnicfFcZsDefaultZoneChangedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsDefaultZoneChangedEnable.setStatus("current")
_HpnicfFcZsHardZoneChangedEnable_Type = TruthValue
_HpnicfFcZsHardZoneChangedEnable_Object = MibScalar
hpnicfFcZsHardZoneChangedEnable = _HpnicfFcZsHardZoneChangedEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 1, 2),
    _HpnicfFcZsHardZoneChangedEnable_Type()
)
hpnicfFcZsHardZoneChangedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsHardZoneChangedEnable.setStatus("current")
_HpnicfFcZsMergeFailedEnable_Type = TruthValue
_HpnicfFcZsMergeFailedEnable_Object = MibScalar
hpnicfFcZsMergeFailedEnable = _HpnicfFcZsMergeFailedEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 1, 3),
    _HpnicfFcZsMergeFailedEnable_Type()
)
hpnicfFcZsMergeFailedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsMergeFailedEnable.setStatus("current")
_HpnicfFcZsMergeSucceededEnable_Type = TruthValue
_HpnicfFcZsMergeSucceededEnable_Object = MibScalar
hpnicfFcZsMergeSucceededEnable = _HpnicfFcZsMergeSucceededEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 1, 4),
    _HpnicfFcZsMergeSucceededEnable_Type()
)
hpnicfFcZsMergeSucceededEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsMergeSucceededEnable.setStatus("current")
_HpnicfFcZsActivationCompletedEnable_Type = TruthValue
_HpnicfFcZsActivationCompletedEnable_Object = MibScalar
hpnicfFcZsActivationCompletedEnable = _HpnicfFcZsActivationCompletedEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 1, 5),
    _HpnicfFcZsActivationCompletedEnable_Type()
)
hpnicfFcZsActivationCompletedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcZsActivationCompletedEnable.setStatus("current")
_HpnicfFcZsObjsForNotification_ObjectIdentity = ObjectIdentity
hpnicfFcZsObjsForNotification = _HpnicfFcZsObjsForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 2)
)
_HpnicfFcZsLocalSwitchWWN_Type = HpnicfFcNameId
_HpnicfFcZsLocalSwitchWWN_Object = MibScalar
hpnicfFcZsLocalSwitchWWN = _HpnicfFcZsLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 2, 1),
    _HpnicfFcZsLocalSwitchWWN_Type()
)
hpnicfFcZsLocalSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFcZsLocalSwitchWWN.setStatus("current")
_HpnicfFcZsPeerSwitchWWN_Type = HpnicfFcNameId
_HpnicfFcZsPeerSwitchWWN_Object = MibScalar
hpnicfFcZsPeerSwitchWWN = _HpnicfFcZsPeerSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 2, 2),
    _HpnicfFcZsPeerSwitchWWN_Type()
)
hpnicfFcZsPeerSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFcZsPeerSwitchWWN.setStatus("current")


class _HpnicfFcZsMergeFailCause_Type(Integer32):
    """Custom type hpnicfFcZsMergeFailCause based on Integer32"""
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


_HpnicfFcZsMergeFailCause_Type.__name__ = "Integer32"
_HpnicfFcZsMergeFailCause_Object = MibScalar
hpnicfFcZsMergeFailCause = _HpnicfFcZsMergeFailCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 2, 3),
    _HpnicfFcZsMergeFailCause_Type()
)
hpnicfFcZsMergeFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfFcZsMergeFailCause.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfFcZsDefaultZoneChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 0, 1)
)
hpnicfFcZsDefaultZoneChangedNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsLocalSwitchWWN"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsDefaultZoneSetting"))
)
if mibBuilder.loadTexts:
    hpnicfFcZsDefaultZoneChangedNotify.setStatus(
        "current"
    )

hpnicfFcZsHardZoneChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 0, 2)
)
hpnicfFcZsHardZoneChangedNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsLocalSwitchWWN"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsHardZoneStatus"))
)
if mibBuilder.loadTexts:
    hpnicfFcZsHardZoneChangedNotify.setStatus(
        "current"
    )

hpnicfFcZsMergeFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 0, 3)
)
hpnicfFcZsMergeFailedNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsLocalSwitchWWN"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsPeerSwitchWWN"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsMergeFailCause"))
)
if mibBuilder.loadTexts:
    hpnicfFcZsMergeFailedNotify.setStatus(
        "current"
    )

hpnicfFcZsMergeSucceededNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 0, 4)
)
hpnicfFcZsMergeSucceededNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsLocalSwitchWWN"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsPeerSwitchWWN"))
)
if mibBuilder.loadTexts:
    hpnicfFcZsMergeSucceededNotify.setStatus(
        "current"
    )

hpnicfFcZsActivationCompletedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 9, 1, 4, 0, 5)
)
hpnicfFcZsActivationCompletedNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsLocalSwitchWWN"),
        ("HPN-ICF-FC-ZONE-SERVER-MIB", "hpnicfFcZsActivateResult"))
)
if mibBuilder.loadTexts:
    hpnicfFcZsActivationCompletedNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FC-ZONE-SERVER-MIB",
    **{"HpnicfFcZsGenName": HpnicfFcZsGenName,
       "HpnicfFcZsGenNameOrZero": HpnicfFcZsGenNameOrZero,
       "HpnicfFcZsZoneMemberType": HpnicfFcZsZoneMemberType,
       "hpnicfFcZoneServer": hpnicfFcZoneServer,
       "hpnicfFcZoneMibObjects": hpnicfFcZoneMibObjects,
       "hpnicfFcZsConfiguration": hpnicfFcZsConfiguration,
       "hpnicfFcZsServerTable": hpnicfFcZsServerTable,
       "hpnicfFcZsServerEntry": hpnicfFcZsServerEntry,
       "hpnicfFcZsZoneModeCfg": hpnicfFcZsZoneModeCfg,
       "hpnicfFcZsHardZoneEnable": hpnicfFcZsHardZoneEnable,
       "hpnicfFcZsDistributeRule": hpnicfFcZsDistributeRule,
       "hpnicfFcZsDefaultZoneSetting": hpnicfFcZsDefaultZoneSetting,
       "hpnicfFcZsMergeControlSetting": hpnicfFcZsMergeControlSetting,
       "hpnicfFcZsServerLastResult": hpnicfFcZsServerLastResult,
       "hpnicfFcZsZonesetTable": hpnicfFcZsZonesetTable,
       "hpnicfFcZsZonesetEntry": hpnicfFcZsZonesetEntry,
       "hpnicfFcZsZonesetIndex": hpnicfFcZsZonesetIndex,
       "hpnicfFcZsZonesetName": hpnicfFcZsZonesetName,
       "hpnicfFcZsZonesetRowStatus": hpnicfFcZsZonesetRowStatus,
       "hpnicfFcZsZoneTable": hpnicfFcZsZoneTable,
       "hpnicfFcZsZoneEntry": hpnicfFcZsZoneEntry,
       "hpnicfFcZsZoneIndex": hpnicfFcZsZoneIndex,
       "hpnicfFcZsZoneName": hpnicfFcZsZoneName,
       "hpnicfFcZsZonePairwiseEnable": hpnicfFcZsZonePairwiseEnable,
       "hpnicfFcZsZoneRowStatus": hpnicfFcZsZoneRowStatus,
       "hpnicfFcZsSetZoneTable": hpnicfFcZsSetZoneTable,
       "hpnicfFcZsSetZoneEntry": hpnicfFcZsSetZoneEntry,
       "hpnicfFcZsSetZoneRowStatus": hpnicfFcZsSetZoneRowStatus,
       "hpnicfFcZsZoneAliasTable": hpnicfFcZsZoneAliasTable,
       "hpnicfFcZsZoneAliasEntry": hpnicfFcZsZoneAliasEntry,
       "hpnicfFcZsZoneAliasIndex": hpnicfFcZsZoneAliasIndex,
       "hpnicfFcZsZoneAliasName": hpnicfFcZsZoneAliasName,
       "hpnicfFcZsZoneAliasRowStatus": hpnicfFcZsZoneAliasRowStatus,
       "hpnicfFcZsZoneMemberTable": hpnicfFcZsZoneMemberTable,
       "hpnicfFcZsZoneMemberEntry": hpnicfFcZsZoneMemberEntry,
       "hpnicfFcZsZoneMemberParentType": hpnicfFcZsZoneMemberParentType,
       "hpnicfFcZsZoneMemberParentIndex": hpnicfFcZsZoneMemberParentIndex,
       "hpnicfFcZsZoneMemberIndex": hpnicfFcZsZoneMemberIndex,
       "hpnicfFcZsZoneMemberFormat": hpnicfFcZsZoneMemberFormat,
       "hpnicfFcZsZoneMemberIdentifier": hpnicfFcZsZoneMemberIdentifier,
       "hpnicfFcZsZoneMemberPairwiseRole": hpnicfFcZsZoneMemberPairwiseRole,
       "hpnicfFcZsZoneMemberRowStatus": hpnicfFcZsZoneMemberRowStatus,
       "hpnicfFcZsOperation": hpnicfFcZsOperation,
       "hpnicfFcZsActivateTable": hpnicfFcZsActivateTable,
       "hpnicfFcZsActivateEntry": hpnicfFcZsActivateEntry,
       "hpnicfFcZsActivate": hpnicfFcZsActivate,
       "hpnicfFcZsDeactivate": hpnicfFcZsDeactivate,
       "hpnicfFcZsActivateResult": hpnicfFcZsActivateResult,
       "hpnicfFcZsActivateFailReason": hpnicfFcZsActivateFailReason,
       "hpnicfFcZsDistributeTable": hpnicfFcZsDistributeTable,
       "hpnicfFcZsDistributeEntry": hpnicfFcZsDistributeEntry,
       "hpnicfFcZsDistribute": hpnicfFcZsDistribute,
       "hpnicfFcZsDistributeLastResult": hpnicfFcZsDistributeLastResult,
       "hpnicfFcZsDistributeReasonCode": hpnicfFcZsDistributeReasonCode,
       "hpnicfFcZsDistributeExplainCode": hpnicfFcZsDistributeExplainCode,
       "hpnicfFcZsClearDatabaseTable": hpnicfFcZsClearDatabaseTable,
       "hpnicfFcZsClearDatabaseEntry": hpnicfFcZsClearDatabaseEntry,
       "hpnicfFcZsClearDatabase": hpnicfFcZsClearDatabase,
       "hpnicfFcZsClearPktStatsTable": hpnicfFcZsClearPktStatsTable,
       "hpnicfFcZsClearPktStatsEntry": hpnicfFcZsClearPktStatsEntry,
       "hpnicfFcZsClearPktStats": hpnicfFcZsClearPktStats,
       "hpnicfFcZsClearAllPktStats": hpnicfFcZsClearAllPktStats,
       "hpnicfFcZsInformation": hpnicfFcZsInformation,
       "hpnicfFcZsActiveZoneTable": hpnicfFcZsActiveZoneTable,
       "hpnicfFcZsActiveZoneEntry": hpnicfFcZsActiveZoneEntry,
       "hpnicfFcZsActiveZonePairwiseEnable": hpnicfFcZsActiveZonePairwiseEnable,
       "hpnicfFcZsActiveMemberTable": hpnicfFcZsActiveMemberTable,
       "hpnicfFcZsActiveMemberEntry": hpnicfFcZsActiveMemberEntry,
       "hpnicfFcZsActiveMemberPairwiseRole": hpnicfFcZsActiveMemberPairwiseRole,
       "hpnicfFcZsServerStatusTable": hpnicfFcZsServerStatusTable,
       "hpnicfFcZsServerStatusEntry": hpnicfFcZsServerStatusEntry,
       "hpnicfFcZsServerStatus": hpnicfFcZsServerStatus,
       "hpnicfFcZsHardZoneStatus": hpnicfFcZsHardZoneStatus,
       "hpnicfFcZsAliasCount": hpnicfFcZsAliasCount,
       "hpnicfFcZsZoneCount": hpnicfFcZsZoneCount,
       "hpnicfFcZsZonesetCount": hpnicfFcZsZonesetCount,
       "hpnicfFcZsPktStatsTable": hpnicfFcZsPktStatsTable,
       "hpnicfFcZsPktStatsEntry": hpnicfFcZsPktStatsEntry,
       "hpnicfFcZsPktInMergeReqCount": hpnicfFcZsPktInMergeReqCount,
       "hpnicfFcZsPktOutMergeReqCount": hpnicfFcZsPktOutMergeReqCount,
       "hpnicfFcZsPktInMergeAccCount": hpnicfFcZsPktInMergeAccCount,
       "hpnicfFcZsPktOutMergeAccCount": hpnicfFcZsPktOutMergeAccCount,
       "hpnicfFcZsPktInMergeRjtCount": hpnicfFcZsPktInMergeRjtCount,
       "hpnicfFcZsPktOutMergeRjtCount": hpnicfFcZsPktOutMergeRjtCount,
       "hpnicfFcZsPktInChangeReqCount": hpnicfFcZsPktInChangeReqCount,
       "hpnicfFcZsPktOutChangeReqCount": hpnicfFcZsPktOutChangeReqCount,
       "hpnicfFcZsPktInChangeAccCount": hpnicfFcZsPktInChangeAccCount,
       "hpnicfFcZsPktOutChangeAccCount": hpnicfFcZsPktOutChangeAccCount,
       "hpnicfFcZsPktInChangeRjtCount": hpnicfFcZsPktInChangeRjtCount,
       "hpnicfFcZsPktOutChangeRjtCount": hpnicfFcZsPktOutChangeRjtCount,
       "hpnicfFcZsNextFreeIndexInfo": hpnicfFcZsNextFreeIndexInfo,
       "hpnicfFcZsZonesetNextFreeIndex": hpnicfFcZsZonesetNextFreeIndex,
       "hpnicfFcZsZoneNextFreeIndex": hpnicfFcZsZoneNextFreeIndex,
       "hpnicfFcZsZoneAliasNextFreeIndex": hpnicfFcZsZoneAliasNextFreeIndex,
       "hpnicfFcZsZoneMemberNextFreeIndexTable": hpnicfFcZsZoneMemberNextFreeIndexTable,
       "hpnicfFcZsZoneMemberNextFreeIndexEntry": hpnicfFcZsZoneMemberNextFreeIndexEntry,
       "hpnicfFcZsZoneMemberNextFreeIndex": hpnicfFcZsZoneMemberNextFreeIndex,
       "hpnicfFcZsNotification": hpnicfFcZsNotification,
       "hpnicfFcZsNotificationPrefix": hpnicfFcZsNotificationPrefix,
       "hpnicfFcZsDefaultZoneChangedNotify": hpnicfFcZsDefaultZoneChangedNotify,
       "hpnicfFcZsHardZoneChangedNotify": hpnicfFcZsHardZoneChangedNotify,
       "hpnicfFcZsMergeFailedNotify": hpnicfFcZsMergeFailedNotify,
       "hpnicfFcZsMergeSucceededNotify": hpnicfFcZsMergeSucceededNotify,
       "hpnicfFcZsActivationCompletedNotify": hpnicfFcZsActivationCompletedNotify,
       "hpnicfFcZsNotificationSwitch": hpnicfFcZsNotificationSwitch,
       "hpnicfFcZsDefaultZoneChangedEnable": hpnicfFcZsDefaultZoneChangedEnable,
       "hpnicfFcZsHardZoneChangedEnable": hpnicfFcZsHardZoneChangedEnable,
       "hpnicfFcZsMergeFailedEnable": hpnicfFcZsMergeFailedEnable,
       "hpnicfFcZsMergeSucceededEnable": hpnicfFcZsMergeSucceededEnable,
       "hpnicfFcZsActivationCompletedEnable": hpnicfFcZsActivationCompletedEnable,
       "hpnicfFcZsObjsForNotification": hpnicfFcZsObjsForNotification,
       "hpnicfFcZsLocalSwitchWWN": hpnicfFcZsLocalSwitchWWN,
       "hpnicfFcZsPeerSwitchWWN": hpnicfFcZsPeerSwitchWWN,
       "hpnicfFcZsMergeFailCause": hpnicfFcZsMergeFailCause}
)
