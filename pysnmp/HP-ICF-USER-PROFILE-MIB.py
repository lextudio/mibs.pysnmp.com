# SNMP MIB module (HP-ICF-USER-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-USER-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:25 2024
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

(HpicfUsrProfilePortSpeed,) = mibBuilder.importSymbols(
    "CONFIG-MIB",
    "HpicfUsrProfilePortSpeed")

(hpicfCommonSecurity,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommonSecurity")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfUsrProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1)
)
hpicfUsrProfileMIB.setRevisions(
        ("2013-06-12 22:48",
         "2008-03-17 15:39",
         "2007-07-16 21:10",
         "2007-06-19 21:40",
         "2007-03-14 23:35",
         "2007-02-06 20:28",
         "2005-10-12 00:00",
         "2005-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfUsrProfileCapability_ObjectIdentity = ObjectIdentity
hpicfUsrProfileCapability = _HpicfUsrProfileCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 0)
)


class _HpicfUsrProfileCapabilityByPortMap_Type(OctetString):
    """Custom type hpicfUsrProfileCapabilityByPortMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpicfUsrProfileCapabilityByPortMap_Type.__name__ = "OctetString"
_HpicfUsrProfileCapabilityByPortMap_Object = MibScalar
hpicfUsrProfileCapabilityByPortMap = _HpicfUsrProfileCapabilityByPortMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 0, 1),
    _HpicfUsrProfileCapabilityByPortMap_Type()
)
hpicfUsrProfileCapabilityByPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileCapabilityByPortMap.setStatus("current")


class _HpicfUsrProfileCapabilityByUserMap_Type(OctetString):
    """Custom type hpicfUsrProfileCapabilityByUserMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpicfUsrProfileCapabilityByUserMap_Type.__name__ = "OctetString"
_HpicfUsrProfileCapabilityByUserMap_Object = MibScalar
hpicfUsrProfileCapabilityByUserMap = _HpicfUsrProfileCapabilityByUserMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 0, 2),
    _HpicfUsrProfileCapabilityByUserMap_Type()
)
hpicfUsrProfileCapabilityByUserMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileCapabilityByUserMap.setStatus("current")
_HpicfUsrProfileConfig_ObjectIdentity = ObjectIdentity
hpicfUsrProfileConfig = _HpicfUsrProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1)
)
_HpicfUsrProfileConfigFilterListTable_Object = MibTable
hpicfUsrProfileConfigFilterListTable = _HpicfUsrProfileConfigFilterListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterListTable.setStatus("current")
_HpicfUsrProfileConfigFilterListEntry_Object = MibTableRow
hpicfUsrProfileConfigFilterListEntry = _HpicfUsrProfileConfigFilterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 1, 1)
)
hpicfUsrProfileConfigFilterListEntry.setIndexNames(
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileFilterListIndex"),
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterListEntry.setStatus("current")


class _HpicfUsrProfileFilterListIndex_Type(Integer32):
    """Custom type hpicfUsrProfileFilterListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HpicfUsrProfileFilterListIndex_Type.__name__ = "Integer32"
_HpicfUsrProfileFilterListIndex_Object = MibTableColumn
hpicfUsrProfileFilterListIndex = _HpicfUsrProfileFilterListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 1, 1, 1),
    _HpicfUsrProfileFilterListIndex_Type()
)
hpicfUsrProfileFilterListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrProfileFilterListIndex.setStatus("current")
_HpicfUsrProfileConfigFilterListRowStatus_Type = RowStatus
_HpicfUsrProfileConfigFilterListRowStatus_Object = MibTableColumn
hpicfUsrProfileConfigFilterListRowStatus = _HpicfUsrProfileConfigFilterListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 1, 1, 2),
    _HpicfUsrProfileConfigFilterListRowStatus_Type()
)
hpicfUsrProfileConfigFilterListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterListRowStatus.setStatus("current")


class _HpicfUsrProfileConfigNasRulesIpv6_Type(Integer32):
    """Custom type hpicfUsrProfileConfigNasRulesIpv6 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfUsrProfileConfigNasRulesIpv6_Type.__name__ = "Integer32"
_HpicfUsrProfileConfigNasRulesIpv6_Object = MibTableColumn
hpicfUsrProfileConfigNasRulesIpv6 = _HpicfUsrProfileConfigNasRulesIpv6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 1, 1, 3),
    _HpicfUsrProfileConfigNasRulesIpv6_Type()
)
hpicfUsrProfileConfigNasRulesIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigNasRulesIpv6.setStatus("current")
_HpicfUsrProfileConfigFilterRuleTable_Object = MibTable
hpicfUsrProfileConfigFilterRuleTable = _HpicfUsrProfileConfigFilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterRuleTable.setStatus("current")
_HpicfUsrProfileConfigFilterRuleEntry_Object = MibTableRow
hpicfUsrProfileConfigFilterRuleEntry = _HpicfUsrProfileConfigFilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 2, 1)
)
hpicfUsrProfileConfigFilterRuleEntry.setIndexNames(
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileFilterRuleListIndex"),
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterRuleEntry.setStatus("current")


class _HpicfUsrProfileFilterRuleListIndex_Type(Integer32):
    """Custom type hpicfUsrProfileFilterRuleListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HpicfUsrProfileFilterRuleListIndex_Type.__name__ = "Integer32"
_HpicfUsrProfileFilterRuleListIndex_Object = MibTableColumn
hpicfUsrProfileFilterRuleListIndex = _HpicfUsrProfileFilterRuleListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 2, 1, 1),
    _HpicfUsrProfileFilterRuleListIndex_Type()
)
hpicfUsrProfileFilterRuleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrProfileFilterRuleListIndex.setStatus("current")


class _HpicfUsrProfileFilterRuleIndex_Type(Integer32):
    """Custom type hpicfUsrProfileFilterRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HpicfUsrProfileFilterRuleIndex_Type.__name__ = "Integer32"
_HpicfUsrProfileFilterRuleIndex_Object = MibTableColumn
hpicfUsrProfileFilterRuleIndex = _HpicfUsrProfileFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 2, 1, 2),
    _HpicfUsrProfileFilterRuleIndex_Type()
)
hpicfUsrProfileFilterRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrProfileFilterRuleIndex.setStatus("current")


class _HpicfUsrProfileConfigFilterRule_Type(OctetString):
    """Custom type hpicfUsrProfileConfigFilterRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpicfUsrProfileConfigFilterRule_Type.__name__ = "OctetString"
_HpicfUsrProfileConfigFilterRule_Object = MibTableColumn
hpicfUsrProfileConfigFilterRule = _HpicfUsrProfileConfigFilterRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 2, 1, 3),
    _HpicfUsrProfileConfigFilterRule_Type()
)
hpicfUsrProfileConfigFilterRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterRule.setStatus("current")
_HpicfUsrProfileConfigFilterRuleRowStatus_Type = RowStatus
_HpicfUsrProfileConfigFilterRuleRowStatus_Object = MibTableColumn
hpicfUsrProfileConfigFilterRuleRowStatus = _HpicfUsrProfileConfigFilterRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 2, 1, 4),
    _HpicfUsrProfileConfigFilterRuleRowStatus_Type()
)
hpicfUsrProfileConfigFilterRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterRuleRowStatus.setStatus("current")
_HpicfUsrProfileConfigTable_Object = MibTable
hpicfUsrProfileConfigTable = _HpicfUsrProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigTable.setStatus("current")
_HpicfUsrProfileConfigEntry_Object = MibTableRow
hpicfUsrProfileConfigEntry = _HpicfUsrProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1)
)
hpicfUsrProfileConfigEntry.setIndexNames(
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigIndex"),
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigEntry.setStatus("current")


class _HpicfUsrProfileConfigIndex_Type(Integer32):
    """Custom type hpicfUsrProfileConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HpicfUsrProfileConfigIndex_Type.__name__ = "Integer32"
_HpicfUsrProfileConfigIndex_Object = MibTableColumn
hpicfUsrProfileConfigIndex = _HpicfUsrProfileConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 1),
    _HpicfUsrProfileConfigIndex_Type()
)
hpicfUsrProfileConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigIndex.setStatus("current")
_HpicfUsrProfileConfigPvid_Type = VlanIndex
_HpicfUsrProfileConfigPvid_Object = MibTableColumn
hpicfUsrProfileConfigPvid = _HpicfUsrProfileConfigPvid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 2),
    _HpicfUsrProfileConfigPvid_Type()
)
hpicfUsrProfileConfigPvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigPvid.setStatus("current")
_HpicfUsrProfileConfigPvidEnable_Type = TruthValue
_HpicfUsrProfileConfigPvidEnable_Object = MibTableColumn
hpicfUsrProfileConfigPvidEnable = _HpicfUsrProfileConfigPvidEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 3),
    _HpicfUsrProfileConfigPvidEnable_Type()
)
hpicfUsrProfileConfigPvidEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigPvidEnable.setStatus("current")


class _HpicfUsrProfileConfigTaggedEgressVlanMap1k_Type(OctetString):
    """Custom type hpicfUsrProfileConfigTaggedEgressVlanMap1k based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileConfigTaggedEgressVlanMap1k_Type.__name__ = "OctetString"
_HpicfUsrProfileConfigTaggedEgressVlanMap1k_Object = MibTableColumn
hpicfUsrProfileConfigTaggedEgressVlanMap1k = _HpicfUsrProfileConfigTaggedEgressVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 4),
    _HpicfUsrProfileConfigTaggedEgressVlanMap1k_Type()
)
hpicfUsrProfileConfigTaggedEgressVlanMap1k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigTaggedEgressVlanMap1k.setStatus("current")


class _HpicfUsrProfileConfigTaggedEgressVlanMap2k_Type(OctetString):
    """Custom type hpicfUsrProfileConfigTaggedEgressVlanMap2k based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileConfigTaggedEgressVlanMap2k_Type.__name__ = "OctetString"
_HpicfUsrProfileConfigTaggedEgressVlanMap2k_Object = MibTableColumn
hpicfUsrProfileConfigTaggedEgressVlanMap2k = _HpicfUsrProfileConfigTaggedEgressVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 5),
    _HpicfUsrProfileConfigTaggedEgressVlanMap2k_Type()
)
hpicfUsrProfileConfigTaggedEgressVlanMap2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigTaggedEgressVlanMap2k.setStatus("current")


class _HpicfUsrProfileConfigTaggedEgressVlanMap3k_Type(OctetString):
    """Custom type hpicfUsrProfileConfigTaggedEgressVlanMap3k based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileConfigTaggedEgressVlanMap3k_Type.__name__ = "OctetString"
_HpicfUsrProfileConfigTaggedEgressVlanMap3k_Object = MibTableColumn
hpicfUsrProfileConfigTaggedEgressVlanMap3k = _HpicfUsrProfileConfigTaggedEgressVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 6),
    _HpicfUsrProfileConfigTaggedEgressVlanMap3k_Type()
)
hpicfUsrProfileConfigTaggedEgressVlanMap3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigTaggedEgressVlanMap3k.setStatus("current")


class _HpicfUsrProfileConfigTaggedEgressVlanMap4k_Type(OctetString):
    """Custom type hpicfUsrProfileConfigTaggedEgressVlanMap4k based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileConfigTaggedEgressVlanMap4k_Type.__name__ = "OctetString"
_HpicfUsrProfileConfigTaggedEgressVlanMap4k_Object = MibTableColumn
hpicfUsrProfileConfigTaggedEgressVlanMap4k = _HpicfUsrProfileConfigTaggedEgressVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 7),
    _HpicfUsrProfileConfigTaggedEgressVlanMap4k_Type()
)
hpicfUsrProfileConfigTaggedEgressVlanMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigTaggedEgressVlanMap4k.setStatus("current")


class _HpicfUsrProfileConfigTaggedEgressVlanEnable_Type(TruthValue):
    """Custom type hpicfUsrProfileConfigTaggedEgressVlanEnable based on TruthValue"""


_HpicfUsrProfileConfigTaggedEgressVlanEnable_Object = MibTableColumn
hpicfUsrProfileConfigTaggedEgressVlanEnable = _HpicfUsrProfileConfigTaggedEgressVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 8),
    _HpicfUsrProfileConfigTaggedEgressVlanEnable_Type()
)
hpicfUsrProfileConfigTaggedEgressVlanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigTaggedEgressVlanEnable.setStatus("current")


class _HpicfUsrProfileConfigIngressVlanFilterEnable_Type(TruthValue):
    """Custom type hpicfUsrProfileConfigIngressVlanFilterEnable based on TruthValue"""


_HpicfUsrProfileConfigIngressVlanFilterEnable_Object = MibTableColumn
hpicfUsrProfileConfigIngressVlanFilterEnable = _HpicfUsrProfileConfigIngressVlanFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 9),
    _HpicfUsrProfileConfigIngressVlanFilterEnable_Type()
)
hpicfUsrProfileConfigIngressVlanFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigIngressVlanFilterEnable.setStatus("current")


class _HpicfUsrProfileConfigPriorityRegenTable_Type(OctetString):
    """Custom type hpicfUsrProfileConfigPriorityRegenTable based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpicfUsrProfileConfigPriorityRegenTable_Type.__name__ = "OctetString"
_HpicfUsrProfileConfigPriorityRegenTable_Object = MibTableColumn
hpicfUsrProfileConfigPriorityRegenTable = _HpicfUsrProfileConfigPriorityRegenTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 10),
    _HpicfUsrProfileConfigPriorityRegenTable_Type()
)
hpicfUsrProfileConfigPriorityRegenTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigPriorityRegenTable.setStatus("current")
_HpicfUsrProfileConfigPriorityRegenTableEnable_Type = TruthValue
_HpicfUsrProfileConfigPriorityRegenTableEnable_Object = MibTableColumn
hpicfUsrProfileConfigPriorityRegenTableEnable = _HpicfUsrProfileConfigPriorityRegenTableEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 11),
    _HpicfUsrProfileConfigPriorityRegenTableEnable_Type()
)
hpicfUsrProfileConfigPriorityRegenTableEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigPriorityRegenTableEnable.setStatus("current")
_HpicfUsrProfileConfigMaxIngressBandwidth_Type = Unsigned32
_HpicfUsrProfileConfigMaxIngressBandwidth_Object = MibTableColumn
hpicfUsrProfileConfigMaxIngressBandwidth = _HpicfUsrProfileConfigMaxIngressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 12),
    _HpicfUsrProfileConfigMaxIngressBandwidth_Type()
)
hpicfUsrProfileConfigMaxIngressBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigMaxIngressBandwidth.setStatus("current")
_HpicfUsrProfileConfigMaxIngressBandwidthEnable_Type = TruthValue
_HpicfUsrProfileConfigMaxIngressBandwidthEnable_Object = MibTableColumn
hpicfUsrProfileConfigMaxIngressBandwidthEnable = _HpicfUsrProfileConfigMaxIngressBandwidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 13),
    _HpicfUsrProfileConfigMaxIngressBandwidthEnable_Type()
)
hpicfUsrProfileConfigMaxIngressBandwidthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigMaxIngressBandwidthEnable.setStatus("current")
_HpicfUsrProfileConfigMaxEgressBandwidth_Type = Unsigned32
_HpicfUsrProfileConfigMaxEgressBandwidth_Object = MibTableColumn
hpicfUsrProfileConfigMaxEgressBandwidth = _HpicfUsrProfileConfigMaxEgressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 14),
    _HpicfUsrProfileConfigMaxEgressBandwidth_Type()
)
hpicfUsrProfileConfigMaxEgressBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigMaxEgressBandwidth.setStatus("current")
_HpicfUsrProfileConfigMaxEgressBandwidthEnable_Type = TruthValue
_HpicfUsrProfileConfigMaxEgressBandwidthEnable_Object = MibTableColumn
hpicfUsrProfileConfigMaxEgressBandwidthEnable = _HpicfUsrProfileConfigMaxEgressBandwidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 15),
    _HpicfUsrProfileConfigMaxEgressBandwidthEnable_Type()
)
hpicfUsrProfileConfigMaxEgressBandwidthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigMaxEgressBandwidthEnable.setStatus("current")


class _HpicfUsrProfileConfigFilterListIndex_Type(Integer32):
    """Custom type hpicfUsrProfileConfigFilterListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HpicfUsrProfileConfigFilterListIndex_Type.__name__ = "Integer32"
_HpicfUsrProfileConfigFilterListIndex_Object = MibTableColumn
hpicfUsrProfileConfigFilterListIndex = _HpicfUsrProfileConfigFilterListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 16),
    _HpicfUsrProfileConfigFilterListIndex_Type()
)
hpicfUsrProfileConfigFilterListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterListIndex.setStatus("current")
_HpicfUsrProfileConfigFilterListEnable_Type = TruthValue
_HpicfUsrProfileConfigFilterListEnable_Object = MibTableColumn
hpicfUsrProfileConfigFilterListEnable = _HpicfUsrProfileConfigFilterListEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 17),
    _HpicfUsrProfileConfigFilterListEnable_Type()
)
hpicfUsrProfileConfigFilterListEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigFilterListEnable.setStatus("current")
_HpicfUsrProfileConfigEntryRowStatus_Type = RowStatus
_HpicfUsrProfileConfigEntryRowStatus_Object = MibTableColumn
hpicfUsrProfileConfigEntryRowStatus = _HpicfUsrProfileConfigEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 3, 1, 18),
    _HpicfUsrProfileConfigEntryRowStatus_Type()
)
hpicfUsrProfileConfigEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigEntryRowStatus.setStatus("current")
_HpicfUsrProfileConfigBindTable_Object = MibTable
hpicfUsrProfileConfigBindTable = _HpicfUsrProfileConfigBindTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigBindTable.setStatus("current")
_HpicfUsrProfileConfigBindEntry_Object = MibTableRow
hpicfUsrProfileConfigBindEntry = _HpicfUsrProfileConfigBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 4, 1)
)
hpicfUsrProfileConfigBindEntry.setIndexNames(
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileUserPortNumber"),
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileUserMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigBindEntry.setStatus("current")
_HpicfUsrProfileUserPortNumber_Type = InterfaceIndex
_HpicfUsrProfileUserPortNumber_Object = MibTableColumn
hpicfUsrProfileUserPortNumber = _HpicfUsrProfileUserPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 4, 1, 1),
    _HpicfUsrProfileUserPortNumber_Type()
)
hpicfUsrProfileUserPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrProfileUserPortNumber.setStatus("current")
_HpicfUsrProfileUserMacAddr_Type = MacAddress
_HpicfUsrProfileUserMacAddr_Object = MibTableColumn
hpicfUsrProfileUserMacAddr = _HpicfUsrProfileUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 4, 1, 2),
    _HpicfUsrProfileUserMacAddr_Type()
)
hpicfUsrProfileUserMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUsrProfileUserMacAddr.setStatus("current")


class _HpicfUsrProfileSelector_Type(Integer32):
    """Custom type hpicfUsrProfileSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_HpicfUsrProfileSelector_Type.__name__ = "Integer32"
_HpicfUsrProfileSelector_Object = MibTableColumn
hpicfUsrProfileSelector = _HpicfUsrProfileSelector_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 4, 1, 3),
    _HpicfUsrProfileSelector_Type()
)
hpicfUsrProfileSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileSelector.setStatus("current")
_HpicfUsrProfileConfigBindEntryRowStatus_Type = RowStatus
_HpicfUsrProfileConfigBindEntryRowStatus_Object = MibTableColumn
hpicfUsrProfileConfigBindEntryRowStatus = _HpicfUsrProfileConfigBindEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 4, 1, 4),
    _HpicfUsrProfileConfigBindEntryRowStatus_Type()
)
hpicfUsrProfileConfigBindEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigBindEntryRowStatus.setStatus("current")


class _HpicfUsrProfileConfigConflictResolveQoS_Type(Integer32):
    """Custom type hpicfUsrProfileConfigConflictResolveQoS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-strict", 0),
          ("strict", 1))
    )


_HpicfUsrProfileConfigConflictResolveQoS_Type.__name__ = "Integer32"
_HpicfUsrProfileConfigConflictResolveQoS_Object = MibScalar
hpicfUsrProfileConfigConflictResolveQoS = _HpicfUsrProfileConfigConflictResolveQoS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 5),
    _HpicfUsrProfileConfigConflictResolveQoS_Type()
)
hpicfUsrProfileConfigConflictResolveQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigConflictResolveQoS.setStatus("current")


class _HpicfUsrProfileConfigConflictResolveMaxIngressBandwidth_Type(Integer32):
    """Custom type hpicfUsrProfileConfigConflictResolveMaxIngressBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-strict", 0),
          ("strict", 1))
    )


_HpicfUsrProfileConfigConflictResolveMaxIngressBandwidth_Type.__name__ = "Integer32"
_HpicfUsrProfileConfigConflictResolveMaxIngressBandwidth_Object = MibScalar
hpicfUsrProfileConfigConflictResolveMaxIngressBandwidth = _HpicfUsrProfileConfigConflictResolveMaxIngressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 6),
    _HpicfUsrProfileConfigConflictResolveMaxIngressBandwidth_Type()
)
hpicfUsrProfileConfigConflictResolveMaxIngressBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigConflictResolveMaxIngressBandwidth.setStatus("current")


class _HpicfUsrProfileConfigConflictResolveMaxEgressBandwidth_Type(Integer32):
    """Custom type hpicfUsrProfileConfigConflictResolveMaxEgressBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-strict", 0),
          ("strict", 1))
    )


_HpicfUsrProfileConfigConflictResolveMaxEgressBandwidth_Type.__name__ = "Integer32"
_HpicfUsrProfileConfigConflictResolveMaxEgressBandwidth_Object = MibScalar
hpicfUsrProfileConfigConflictResolveMaxEgressBandwidth = _HpicfUsrProfileConfigConflictResolveMaxEgressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 1, 7),
    _HpicfUsrProfileConfigConflictResolveMaxEgressBandwidth_Type()
)
hpicfUsrProfileConfigConflictResolveMaxEgressBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigConflictResolveMaxEgressBandwidth.setStatus("current")
_HpicfUsrProfileStats_ObjectIdentity = ObjectIdentity
hpicfUsrProfileStats = _HpicfUsrProfileStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2)
)
_HpicfUsrProfileLastUpdate_Type = TimeTicks
_HpicfUsrProfileLastUpdate_Object = MibScalar
hpicfUsrProfileLastUpdate = _HpicfUsrProfileLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 1),
    _HpicfUsrProfileLastUpdate_Type()
)
hpicfUsrProfileLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileLastUpdate.setStatus("current")
_HpicfUsrProfileStatsFilterTable_Object = MibTable
hpicfUsrProfileStatsFilterTable = _HpicfUsrProfileStatsFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsFilterTable.setStatus("current")
_HpicfUsrProfileStatsFilterEntry_Object = MibTableRow
hpicfUsrProfileStatsFilterEntry = _HpicfUsrProfileStatsFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 2, 1)
)
hpicfUsrProfileStatsFilterEntry.setIndexNames(
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileFilterListIndex"),
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsFilterEntry.setStatus("current")


class _HpicfUsrProfileStatsFilterRule_Type(OctetString):
    """Custom type hpicfUsrProfileStatsFilterRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpicfUsrProfileStatsFilterRule_Type.__name__ = "OctetString"
_HpicfUsrProfileStatsFilterRule_Object = MibTableColumn
hpicfUsrProfileStatsFilterRule = _HpicfUsrProfileStatsFilterRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 2, 1, 1),
    _HpicfUsrProfileStatsFilterRule_Type()
)
hpicfUsrProfileStatsFilterRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsFilterRule.setStatus("current")
_HpicfUsrProfileStatsFilterRuleHitCount_Type = Counter64
_HpicfUsrProfileStatsFilterRuleHitCount_Object = MibTableColumn
hpicfUsrProfileStatsFilterRuleHitCount = _HpicfUsrProfileStatsFilterRuleHitCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 2, 1, 2),
    _HpicfUsrProfileStatsFilterRuleHitCount_Type()
)
hpicfUsrProfileStatsFilterRuleHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsFilterRuleHitCount.setStatus("current")
_HpicfUsrProfileStatsFilterRuleHitCountEnabled_Type = TruthValue
_HpicfUsrProfileStatsFilterRuleHitCountEnabled_Object = MibTableColumn
hpicfUsrProfileStatsFilterRuleHitCountEnabled = _HpicfUsrProfileStatsFilterRuleHitCountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 2, 1, 3),
    _HpicfUsrProfileStatsFilterRuleHitCountEnabled_Type()
)
hpicfUsrProfileStatsFilterRuleHitCountEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsFilterRuleHitCountEnabled.setStatus("current")
_HpicfUsrProfileStatsTable_Object = MibTable
hpicfUsrProfileStatsTable = _HpicfUsrProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsTable.setStatus("current")
_HpicfUsrProfileStatsEntry_Object = MibTableRow
hpicfUsrProfileStatsEntry = _HpicfUsrProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1)
)
hpicfUsrProfileStatsEntry.setIndexNames(
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileUserPortNumber"),
    (0, "HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileUserMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsEntry.setStatus("current")
_HpicfUsrProfileStatsPvid_Type = VlanIndex
_HpicfUsrProfileStatsPvid_Object = MibTableColumn
hpicfUsrProfileStatsPvid = _HpicfUsrProfileStatsPvid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 1),
    _HpicfUsrProfileStatsPvid_Type()
)
hpicfUsrProfileStatsPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsPvid.setStatus("current")


class _HpicfUsrProfileStatsTaggedEgressVlanMap1k_Type(OctetString):
    """Custom type hpicfUsrProfileStatsTaggedEgressVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileStatsTaggedEgressVlanMap1k_Type.__name__ = "OctetString"
_HpicfUsrProfileStatsTaggedEgressVlanMap1k_Object = MibTableColumn
hpicfUsrProfileStatsTaggedEgressVlanMap1k = _HpicfUsrProfileStatsTaggedEgressVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 2),
    _HpicfUsrProfileStatsTaggedEgressVlanMap1k_Type()
)
hpicfUsrProfileStatsTaggedEgressVlanMap1k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsTaggedEgressVlanMap1k.setStatus("current")


class _HpicfUsrProfileStatsTaggedEgressVlanMap2k_Type(OctetString):
    """Custom type hpicfUsrProfileStatsTaggedEgressVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileStatsTaggedEgressVlanMap2k_Type.__name__ = "OctetString"
_HpicfUsrProfileStatsTaggedEgressVlanMap2k_Object = MibTableColumn
hpicfUsrProfileStatsTaggedEgressVlanMap2k = _HpicfUsrProfileStatsTaggedEgressVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 3),
    _HpicfUsrProfileStatsTaggedEgressVlanMap2k_Type()
)
hpicfUsrProfileStatsTaggedEgressVlanMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsTaggedEgressVlanMap2k.setStatus("current")


class _HpicfUsrProfileStatsTaggedEgressVlanMap3k_Type(OctetString):
    """Custom type hpicfUsrProfileStatsTaggedEgressVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileStatsTaggedEgressVlanMap3k_Type.__name__ = "OctetString"
_HpicfUsrProfileStatsTaggedEgressVlanMap3k_Object = MibTableColumn
hpicfUsrProfileStatsTaggedEgressVlanMap3k = _HpicfUsrProfileStatsTaggedEgressVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 4),
    _HpicfUsrProfileStatsTaggedEgressVlanMap3k_Type()
)
hpicfUsrProfileStatsTaggedEgressVlanMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsTaggedEgressVlanMap3k.setStatus("current")


class _HpicfUsrProfileStatsTaggedEgressVlanMap4k_Type(OctetString):
    """Custom type hpicfUsrProfileStatsTaggedEgressVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfUsrProfileStatsTaggedEgressVlanMap4k_Type.__name__ = "OctetString"
_HpicfUsrProfileStatsTaggedEgressVlanMap4k_Object = MibTableColumn
hpicfUsrProfileStatsTaggedEgressVlanMap4k = _HpicfUsrProfileStatsTaggedEgressVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 5),
    _HpicfUsrProfileStatsTaggedEgressVlanMap4k_Type()
)
hpicfUsrProfileStatsTaggedEgressVlanMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsTaggedEgressVlanMap4k.setStatus("current")
_HpicfUsrProfileStatsIngressVlanFilterEnable_Type = TruthValue
_HpicfUsrProfileStatsIngressVlanFilterEnable_Object = MibTableColumn
hpicfUsrProfileStatsIngressVlanFilterEnable = _HpicfUsrProfileStatsIngressVlanFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 6),
    _HpicfUsrProfileStatsIngressVlanFilterEnable_Type()
)
hpicfUsrProfileStatsIngressVlanFilterEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsIngressVlanFilterEnable.setStatus("current")


class _HpicfUsrProfileStatsPriorityRegenTable_Type(OctetString):
    """Custom type hpicfUsrProfileStatsPriorityRegenTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpicfUsrProfileStatsPriorityRegenTable_Type.__name__ = "OctetString"
_HpicfUsrProfileStatsPriorityRegenTable_Object = MibTableColumn
hpicfUsrProfileStatsPriorityRegenTable = _HpicfUsrProfileStatsPriorityRegenTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 7),
    _HpicfUsrProfileStatsPriorityRegenTable_Type()
)
hpicfUsrProfileStatsPriorityRegenTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsPriorityRegenTable.setStatus("current")
_HpicfUsrProfileStatsMaxIngressBandwidth_Type = Unsigned32
_HpicfUsrProfileStatsMaxIngressBandwidth_Object = MibTableColumn
hpicfUsrProfileStatsMaxIngressBandwidth = _HpicfUsrProfileStatsMaxIngressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 8),
    _HpicfUsrProfileStatsMaxIngressBandwidth_Type()
)
hpicfUsrProfileStatsMaxIngressBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsMaxIngressBandwidth.setStatus("current")
_HpicfUsrProfileStatsMaxEgressBandwidth_Type = Unsigned32
_HpicfUsrProfileStatsMaxEgressBandwidth_Object = MibTableColumn
hpicfUsrProfileStatsMaxEgressBandwidth = _HpicfUsrProfileStatsMaxEgressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 9),
    _HpicfUsrProfileStatsMaxEgressBandwidth_Type()
)
hpicfUsrProfileStatsMaxEgressBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsMaxEgressBandwidth.setStatus("current")


class _HpicfUsrProfileStatsFilterListIndex_Type(Integer32):
    """Custom type hpicfUsrProfileStatsFilterListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_HpicfUsrProfileStatsFilterListIndex_Type.__name__ = "Integer32"
_HpicfUsrProfileStatsFilterListIndex_Object = MibTableColumn
hpicfUsrProfileStatsFilterListIndex = _HpicfUsrProfileStatsFilterListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 10),
    _HpicfUsrProfileStatsFilterListIndex_Type()
)
hpicfUsrProfileStatsFilterListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsFilterListIndex.setStatus("current")


class _HpicfUsrProfileStatsAccessMode_Type(Integer32):
    """Custom type hpicfUsrProfileStatsAccessMode based on Integer32"""
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
        *(("dot8021x", 2),
          ("macauth", 4),
          ("snmp", 1),
          ("webauth", 3),
          ("webmacauth", 5))
    )


_HpicfUsrProfileStatsAccessMode_Type.__name__ = "Integer32"
_HpicfUsrProfileStatsAccessMode_Object = MibTableColumn
hpicfUsrProfileStatsAccessMode = _HpicfUsrProfileStatsAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 11),
    _HpicfUsrProfileStatsAccessMode_Type()
)
hpicfUsrProfileStatsAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsAccessMode.setStatus("current")
_HpicfUsrProfilePortSpeedOverRidden_Type = TruthValue
_HpicfUsrProfilePortSpeedOverRidden_Object = MibTableColumn
hpicfUsrProfilePortSpeedOverRidden = _HpicfUsrProfilePortSpeedOverRidden_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 12),
    _HpicfUsrProfilePortSpeedOverRidden_Type()
)
hpicfUsrProfilePortSpeedOverRidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfilePortSpeedOverRidden.setStatus("current")
_HpicfUsrProfileStatsPortSpeedVSA_Type = HpicfUsrProfilePortSpeed
_HpicfUsrProfileStatsPortSpeedVSA_Object = MibTableColumn
hpicfUsrProfileStatsPortSpeedVSA = _HpicfUsrProfileStatsPortSpeedVSA_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 2, 3, 1, 13),
    _HpicfUsrProfileStatsPortSpeedVSA_Type()
)
hpicfUsrProfileStatsPortSpeedVSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsPortSpeedVSA.setStatus("current")
_HpicfUsrProfileConformance_ObjectIdentity = ObjectIdentity
hpicfUsrProfileConformance = _HpicfUsrProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3)
)
_HpicfUsrProfileGroup_ObjectIdentity = ObjectIdentity
hpicfUsrProfileGroup = _HpicfUsrProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 1)
)
_HpicfUsrProfileCompliances_ObjectIdentity = ObjectIdentity
hpicfUsrProfileCompliances = _HpicfUsrProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 2)
)

# Managed Objects groups

hpicfUsrProfileCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 1, 1)
)
hpicfUsrProfileCapabilityGroup.setObjects(
      *(("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileCapabilityByPortMap"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileCapabilityByUserMap"))
)
if mibBuilder.loadTexts:
    hpicfUsrProfileCapabilityGroup.setStatus("current")

hpicfUsrProfileConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 1, 2)
)
hpicfUsrProfileConfigGroup.setObjects(
      *(("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigFilterListRowStatus"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigFilterRule"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigFilterRuleRowStatus"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigPvid"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigPvidEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigTaggedEgressVlanMap1k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigTaggedEgressVlanMap2k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigTaggedEgressVlanMap3k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigTaggedEgressVlanMap4k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigTaggedEgressVlanEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigIngressVlanFilterEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigPriorityRegenTable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigPriorityRegenTableEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigMaxIngressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigMaxIngressBandwidthEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigMaxEgressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigMaxEgressBandwidthEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigFilterListIndex"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigFilterListEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigEntryRowStatus"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigConflictResolveQoS"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigConflictResolveMaxIngressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigConflictResolveMaxEgressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigNasRulesIpv6"))
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigGroup.setStatus("current")

hpicfUsrProfileStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 1, 3)
)
hpicfUsrProfileStatsGroup.setObjects(
      *(("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileLastUpdate"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterRule"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterRuleHitCount"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterRuleHitCountEnabled"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsPvid"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap1k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap2k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap3k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap4k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsIngressVlanFilterEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsPriorityRegenTable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsMaxIngressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsMaxEgressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterListIndex"))
)
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsGroup.setStatus("deprecated")

hpicfUsrProfileConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 1, 4)
)
hpicfUsrProfileConfigGroup2.setObjects(
      *(("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileSelector"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileConfigBindEntryRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfUsrProfileConfigGroup2.setStatus("current")

hpicfUsrProfileStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 1, 5)
)
hpicfUsrProfileStatsGroup1.setObjects(
      *(("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileLastUpdate"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterRule"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterRuleHitCount"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterRuleHitCountEnabled"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsPvid"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap1k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap2k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap3k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsTaggedEgressVlanMap4k"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsIngressVlanFilterEnable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsPriorityRegenTable"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsMaxIngressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsMaxEgressBandwidth"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsFilterListIndex"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsAccessMode"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfileStatsPortSpeedVSA"),
        ("HP-ICF-USER-PROFILE-MIB", "hpicfUsrProfilePortSpeedOverRidden"))
)
if mibBuilder.loadTexts:
    hpicfUsrProfileStatsGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfUsrProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileCompliance.setStatus(
        "deprecated"
    )

hpicfUsrProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileCompliance2.setStatus(
        "deprecated"
    )

hpicfUsrProfileCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileCompliance3.setStatus(
        "current"
    )

hpicfUsrProfileCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfUsrProfileCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-USER-PROFILE-MIB",
    **{"hpicfUsrProfileMIB": hpicfUsrProfileMIB,
       "hpicfUsrProfileCapability": hpicfUsrProfileCapability,
       "hpicfUsrProfileCapabilityByPortMap": hpicfUsrProfileCapabilityByPortMap,
       "hpicfUsrProfileCapabilityByUserMap": hpicfUsrProfileCapabilityByUserMap,
       "hpicfUsrProfileConfig": hpicfUsrProfileConfig,
       "hpicfUsrProfileConfigFilterListTable": hpicfUsrProfileConfigFilterListTable,
       "hpicfUsrProfileConfigFilterListEntry": hpicfUsrProfileConfigFilterListEntry,
       "hpicfUsrProfileFilterListIndex": hpicfUsrProfileFilterListIndex,
       "hpicfUsrProfileConfigFilterListRowStatus": hpicfUsrProfileConfigFilterListRowStatus,
       "hpicfUsrProfileConfigNasRulesIpv6": hpicfUsrProfileConfigNasRulesIpv6,
       "hpicfUsrProfileConfigFilterRuleTable": hpicfUsrProfileConfigFilterRuleTable,
       "hpicfUsrProfileConfigFilterRuleEntry": hpicfUsrProfileConfigFilterRuleEntry,
       "hpicfUsrProfileFilterRuleListIndex": hpicfUsrProfileFilterRuleListIndex,
       "hpicfUsrProfileFilterRuleIndex": hpicfUsrProfileFilterRuleIndex,
       "hpicfUsrProfileConfigFilterRule": hpicfUsrProfileConfigFilterRule,
       "hpicfUsrProfileConfigFilterRuleRowStatus": hpicfUsrProfileConfigFilterRuleRowStatus,
       "hpicfUsrProfileConfigTable": hpicfUsrProfileConfigTable,
       "hpicfUsrProfileConfigEntry": hpicfUsrProfileConfigEntry,
       "hpicfUsrProfileConfigIndex": hpicfUsrProfileConfigIndex,
       "hpicfUsrProfileConfigPvid": hpicfUsrProfileConfigPvid,
       "hpicfUsrProfileConfigPvidEnable": hpicfUsrProfileConfigPvidEnable,
       "hpicfUsrProfileConfigTaggedEgressVlanMap1k": hpicfUsrProfileConfigTaggedEgressVlanMap1k,
       "hpicfUsrProfileConfigTaggedEgressVlanMap2k": hpicfUsrProfileConfigTaggedEgressVlanMap2k,
       "hpicfUsrProfileConfigTaggedEgressVlanMap3k": hpicfUsrProfileConfigTaggedEgressVlanMap3k,
       "hpicfUsrProfileConfigTaggedEgressVlanMap4k": hpicfUsrProfileConfigTaggedEgressVlanMap4k,
       "hpicfUsrProfileConfigTaggedEgressVlanEnable": hpicfUsrProfileConfigTaggedEgressVlanEnable,
       "hpicfUsrProfileConfigIngressVlanFilterEnable": hpicfUsrProfileConfigIngressVlanFilterEnable,
       "hpicfUsrProfileConfigPriorityRegenTable": hpicfUsrProfileConfigPriorityRegenTable,
       "hpicfUsrProfileConfigPriorityRegenTableEnable": hpicfUsrProfileConfigPriorityRegenTableEnable,
       "hpicfUsrProfileConfigMaxIngressBandwidth": hpicfUsrProfileConfigMaxIngressBandwidth,
       "hpicfUsrProfileConfigMaxIngressBandwidthEnable": hpicfUsrProfileConfigMaxIngressBandwidthEnable,
       "hpicfUsrProfileConfigMaxEgressBandwidth": hpicfUsrProfileConfigMaxEgressBandwidth,
       "hpicfUsrProfileConfigMaxEgressBandwidthEnable": hpicfUsrProfileConfigMaxEgressBandwidthEnable,
       "hpicfUsrProfileConfigFilterListIndex": hpicfUsrProfileConfigFilterListIndex,
       "hpicfUsrProfileConfigFilterListEnable": hpicfUsrProfileConfigFilterListEnable,
       "hpicfUsrProfileConfigEntryRowStatus": hpicfUsrProfileConfigEntryRowStatus,
       "hpicfUsrProfileConfigBindTable": hpicfUsrProfileConfigBindTable,
       "hpicfUsrProfileConfigBindEntry": hpicfUsrProfileConfigBindEntry,
       "hpicfUsrProfileUserPortNumber": hpicfUsrProfileUserPortNumber,
       "hpicfUsrProfileUserMacAddr": hpicfUsrProfileUserMacAddr,
       "hpicfUsrProfileSelector": hpicfUsrProfileSelector,
       "hpicfUsrProfileConfigBindEntryRowStatus": hpicfUsrProfileConfigBindEntryRowStatus,
       "hpicfUsrProfileConfigConflictResolveQoS": hpicfUsrProfileConfigConflictResolveQoS,
       "hpicfUsrProfileConfigConflictResolveMaxIngressBandwidth": hpicfUsrProfileConfigConflictResolveMaxIngressBandwidth,
       "hpicfUsrProfileConfigConflictResolveMaxEgressBandwidth": hpicfUsrProfileConfigConflictResolveMaxEgressBandwidth,
       "hpicfUsrProfileStats": hpicfUsrProfileStats,
       "hpicfUsrProfileLastUpdate": hpicfUsrProfileLastUpdate,
       "hpicfUsrProfileStatsFilterTable": hpicfUsrProfileStatsFilterTable,
       "hpicfUsrProfileStatsFilterEntry": hpicfUsrProfileStatsFilterEntry,
       "hpicfUsrProfileStatsFilterRule": hpicfUsrProfileStatsFilterRule,
       "hpicfUsrProfileStatsFilterRuleHitCount": hpicfUsrProfileStatsFilterRuleHitCount,
       "hpicfUsrProfileStatsFilterRuleHitCountEnabled": hpicfUsrProfileStatsFilterRuleHitCountEnabled,
       "hpicfUsrProfileStatsTable": hpicfUsrProfileStatsTable,
       "hpicfUsrProfileStatsEntry": hpicfUsrProfileStatsEntry,
       "hpicfUsrProfileStatsPvid": hpicfUsrProfileStatsPvid,
       "hpicfUsrProfileStatsTaggedEgressVlanMap1k": hpicfUsrProfileStatsTaggedEgressVlanMap1k,
       "hpicfUsrProfileStatsTaggedEgressVlanMap2k": hpicfUsrProfileStatsTaggedEgressVlanMap2k,
       "hpicfUsrProfileStatsTaggedEgressVlanMap3k": hpicfUsrProfileStatsTaggedEgressVlanMap3k,
       "hpicfUsrProfileStatsTaggedEgressVlanMap4k": hpicfUsrProfileStatsTaggedEgressVlanMap4k,
       "hpicfUsrProfileStatsIngressVlanFilterEnable": hpicfUsrProfileStatsIngressVlanFilterEnable,
       "hpicfUsrProfileStatsPriorityRegenTable": hpicfUsrProfileStatsPriorityRegenTable,
       "hpicfUsrProfileStatsMaxIngressBandwidth": hpicfUsrProfileStatsMaxIngressBandwidth,
       "hpicfUsrProfileStatsMaxEgressBandwidth": hpicfUsrProfileStatsMaxEgressBandwidth,
       "hpicfUsrProfileStatsFilterListIndex": hpicfUsrProfileStatsFilterListIndex,
       "hpicfUsrProfileStatsAccessMode": hpicfUsrProfileStatsAccessMode,
       "hpicfUsrProfilePortSpeedOverRidden": hpicfUsrProfilePortSpeedOverRidden,
       "hpicfUsrProfileStatsPortSpeedVSA": hpicfUsrProfileStatsPortSpeedVSA,
       "hpicfUsrProfileConformance": hpicfUsrProfileConformance,
       "hpicfUsrProfileGroup": hpicfUsrProfileGroup,
       "hpicfUsrProfileCapabilityGroup": hpicfUsrProfileCapabilityGroup,
       "hpicfUsrProfileConfigGroup": hpicfUsrProfileConfigGroup,
       "hpicfUsrProfileStatsGroup": hpicfUsrProfileStatsGroup,
       "hpicfUsrProfileConfigGroup2": hpicfUsrProfileConfigGroup2,
       "hpicfUsrProfileStatsGroup1": hpicfUsrProfileStatsGroup1,
       "hpicfUsrProfileCompliances": hpicfUsrProfileCompliances,
       "hpicfUsrProfileCompliance": hpicfUsrProfileCompliance,
       "hpicfUsrProfileCompliance2": hpicfUsrProfileCompliance2,
       "hpicfUsrProfileCompliance3": hpicfUsrProfileCompliance3,
       "hpicfUsrProfileCompliance4": hpicfUsrProfileCompliance4}
)
