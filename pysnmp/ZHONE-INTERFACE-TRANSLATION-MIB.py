# SNMP MIB module (ZHONE-INTERFACE-TRANSLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-INTERFACE-TRANSLATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:09 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifEntry) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneInterfaceTranslation,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneInterfaceTranslation",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneIfType,
 ZhoneRowStatus,
 ZhoneShelfValue,
 ZhoneSlotValue) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneIfType",
    "ZhoneRowStatus",
    "ZhoneShelfValue",
    "ZhoneSlotValue")


# MODULE-IDENTITY

zhoneInterfaceTrans = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 6)
)
zhoneInterfaceTrans.setRevisions(
        ("2011-02-24 01:38",
         "2010-04-09 15:04",
         "2010-04-02 14:29",
         "2010-03-10 11:19",
         "2008-09-28 23:15",
         "2007-01-26 18:23",
         "2004-05-26 15:53",
         "2001-06-28 13:07",
         "2001-05-23 11:02",
         "2001-05-11 15:25",
         "2000-09-20 12:00",
         "2000-09-12 11:11")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfIndexNext_Type = InterfaceIndex
_IfIndexNext_Object = MibScalar
ifIndexNext = _IfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 1),
    _IfIndexNext_Type()
)
ifIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndexNext.setStatus("current")
_PhysicalToIfIndexTable_Object = MibTable
physicalToIfIndexTable = _PhysicalToIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 2)
)
if mibBuilder.loadTexts:
    physicalToIfIndexTable.setStatus("deprecated")
_PhysicalToIfIndexEntry_Object = MibTableRow
physicalToIfIndexEntry = _PhysicalToIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1)
)
physicalToIfIndexEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "pportIndex"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "subPortIndex"),
)
if mibBuilder.loadTexts:
    physicalToIfIndexEntry.setStatus("deprecated")


class _PportIndex_Type(Integer32):
    """Custom type pportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PportIndex_Type.__name__ = "Integer32"
_PportIndex_Object = MibTableColumn
pportIndex = _PportIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 1),
    _PportIndex_Type()
)
pportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pportIndex.setStatus("deprecated")


class _SubPortIndex_Type(Integer32):
    """Custom type subPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SubPortIndex_Type.__name__ = "Integer32"
_SubPortIndex_Object = MibTableColumn
subPortIndex = _SubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 2),
    _SubPortIndex_Type()
)
subPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subPortIndex.setStatus("deprecated")
_ZhoneIfIndex_Type = InterfaceIndex
_ZhoneIfIndex_Object = MibTableColumn
zhoneIfIndex = _ZhoneIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 3),
    _ZhoneIfIndex_Type()
)
zhoneIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIfIndex.setStatus("deprecated")
_XxxifTypexxx_Type = IANAifType
_XxxifTypexxx_Object = MibTableColumn
xxxifTypexxx = _XxxifTypexxx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 2, 1, 4),
    _XxxifTypexxx_Type()
)
xxxifTypexxx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xxxifTypexxx.setStatus("deprecated")
_IfIndexToPhysicalTable_Object = MibTable
ifIndexToPhysicalTable = _IfIndexToPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3)
)
if mibBuilder.loadTexts:
    ifIndexToPhysicalTable.setStatus("current")
_IfIndexToPhysicalEntry_Object = MibTableRow
ifIndexToPhysicalEntry = _IfIndexToPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1)
)
ifIndexToPhysicalEntry.setIndexNames(
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfIndex"),
)
if mibBuilder.loadTexts:
    ifIndexToPhysicalEntry.setStatus("current")
_ZhoneShelfNumber_Type = ZhoneShelfValue
_ZhoneShelfNumber_Object = MibTableColumn
zhoneShelfNumber = _ZhoneShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 1),
    _ZhoneShelfNumber_Type()
)
zhoneShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneShelfNumber.setStatus("current")
_ZhoneSlotNumber_Type = ZhoneSlotValue
_ZhoneSlotNumber_Object = MibTableColumn
zhoneSlotNumber = _ZhoneSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 2),
    _ZhoneSlotNumber_Type()
)
zhoneSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSlotNumber.setStatus("current")


class _PportNumber_Type(Integer32):
    """Custom type pportNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PportNumber_Type.__name__ = "Integer32"
_PportNumber_Object = MibTableColumn
pportNumber = _PportNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 3),
    _PportNumber_Type()
)
pportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportNumber.setStatus("current")


class _SubPortNumber_Type(Integer32):
    """Custom type subPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SubPortNumber_Type.__name__ = "Integer32"
_SubPortNumber_Object = MibTableColumn
subPortNumber = _SubPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 4),
    _SubPortNumber_Type()
)
subPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subPortNumber.setStatus("current")
_IfaceType_Type = IANAifType
_IfaceType_Object = MibTableColumn
ifaceType = _IfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 5),
    _IfaceType_Type()
)
ifaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceType.setStatus("current")
_IfaceTypeExtension_Type = ZhoneIfType
_IfaceTypeExtension_Object = MibTableColumn
ifaceTypeExtension = _IfaceTypeExtension_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 3, 1, 6),
    _IfaceTypeExtension_Type()
)
ifaceTypeExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceTypeExtension.setStatus("current")
_IfStackDefaultTable_Object = MibTable
ifStackDefaultTable = _IfStackDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4)
)
if mibBuilder.loadTexts:
    ifStackDefaultTable.setStatus("current")
_IfStackDefaultEntry_Object = MibTableRow
ifStackDefaultEntry = _IfStackDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1)
)
ifStackDefaultEntry.setIndexNames(
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifStkDefUpperType"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifStkDefLowerType"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifStkDefCardType"),
)
if mibBuilder.loadTexts:
    ifStackDefaultEntry.setStatus("current")


class _IfStkDefCardType_Type(Integer32):
    """Custom type ifStkDefCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfStkDefCardType_Type.__name__ = "Integer32"
_IfStkDefCardType_Object = MibTableColumn
ifStkDefCardType = _IfStkDefCardType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 1),
    _IfStkDefCardType_Type()
)
ifStkDefCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifStkDefCardType.setStatus("current")
_IfStkDefUpperType_Type = IANAifType
_IfStkDefUpperType_Object = MibTableColumn
ifStkDefUpperType = _IfStkDefUpperType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 2),
    _IfStkDefUpperType_Type()
)
ifStkDefUpperType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifStkDefUpperType.setStatus("current")
_IfStkDefLowerType_Type = IANAifType
_IfStkDefLowerType_Object = MibTableColumn
ifStkDefLowerType = _IfStkDefLowerType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 3),
    _IfStkDefLowerType_Type()
)
ifStkDefLowerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifStkDefLowerType.setStatus("current")


class _IfStkDefUnits_Type(Integer32):
    """Custom type ifStkDefUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfStkDefUnits_Type.__name__ = "Integer32"
_IfStkDefUnits_Object = MibTableColumn
ifStkDefUnits = _IfStkDefUnits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 4),
    _IfStkDefUnits_Type()
)
ifStkDefUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifStkDefUnits.setStatus("current")
if mibBuilder.loadTexts:
    ifStkDefUnits.setUnits("count")


class _IfStkDefAdminStatus_Type(Integer32):
    """Custom type ifStkDefAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_IfStkDefAdminStatus_Type.__name__ = "Integer32"
_IfStkDefAdminStatus_Object = MibTableColumn
ifStkDefAdminStatus = _IfStkDefAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 5),
    _IfStkDefAdminStatus_Type()
)
ifStkDefAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifStkDefAdminStatus.setStatus("current")
_IfStkDefRowStatus_Type = ZhoneRowStatus
_IfStkDefRowStatus_Object = MibTableColumn
ifStkDefRowStatus = _IfStkDefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 4, 1, 6),
    _IfStkDefRowStatus_Type()
)
ifStkDefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifStkDefRowStatus.setStatus("current")
_IfInverseStackTable_Object = MibTable
ifInverseStackTable = _IfInverseStackTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 5)
)
if mibBuilder.loadTexts:
    ifInverseStackTable.setStatus("current")
_IfInverseStackEntry_Object = MibTableRow
ifInverseStackEntry = _IfInverseStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1)
)
ifInverseStackEntry.setIndexNames(
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifInverseStackLowerLayer"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "ifInverseStackHigherLayer"),
)
if mibBuilder.loadTexts:
    ifInverseStackEntry.setStatus("current")
_IfInverseStackLowerLayer_Type = InterfaceIndex
_IfInverseStackLowerLayer_Object = MibTableColumn
ifInverseStackLowerLayer = _IfInverseStackLowerLayer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1, 1),
    _IfInverseStackLowerLayer_Type()
)
ifInverseStackLowerLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifInverseStackLowerLayer.setStatus("current")
_IfInverseStackHigherLayer_Type = InterfaceIndex
_IfInverseStackHigherLayer_Object = MibTableColumn
ifInverseStackHigherLayer = _IfInverseStackHigherLayer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1, 2),
    _IfInverseStackHigherLayer_Type()
)
ifInverseStackHigherLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifInverseStackHigherLayer.setStatus("current")


class _IfInverseStackStatus_Type(Integer32):
    """Custom type ifInverseStackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_IfInverseStackStatus_Type.__name__ = "Integer32"
_IfInverseStackStatus_Object = MibTableColumn
ifInverseStackStatus = _IfInverseStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 5, 1, 3),
    _IfInverseStackStatus_Type()
)
ifInverseStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInverseStackStatus.setStatus("current")
_ZhoneIfXTable_Object = MibTable
zhoneIfXTable = _ZhoneIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6)
)
if mibBuilder.loadTexts:
    zhoneIfXTable.setStatus("current")
_ZhoneIfXEntry_Object = MibTableRow
zhoneIfXEntry = _ZhoneIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1)
)
if mibBuilder.loadTexts:
    zhoneIfXEntry.setStatus("current")


class _PhysicalFlag_Type(TruthValue):
    """Custom type physicalFlag based on TruthValue"""


_PhysicalFlag_Object = MibTableColumn
physicalFlag = _PhysicalFlag_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 1),
    _PhysicalFlag_Type()
)
physicalFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    physicalFlag.setStatus("current")
_IfTypeExtension_Type = ZhoneIfType
_IfTypeExtension_Object = MibTableColumn
ifTypeExtension = _IfTypeExtension_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 2),
    _IfTypeExtension_Type()
)
ifTypeExtension.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifTypeExtension.setStatus("current")


class _RedundancyParam1_Type(Integer32):
    """Custom type redundancyParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_RedundancyParam1_Type.__name__ = "Integer32"
_RedundancyParam1_Object = MibTableColumn
redundancyParam1 = _RedundancyParam1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 3),
    _RedundancyParam1_Type()
)
redundancyParam1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redundancyParam1.setStatus("current")
_ZhoneIfXEntryIfTypeAlias_Type = IANAifType
_ZhoneIfXEntryIfTypeAlias_Object = MibTableColumn
zhoneIfXEntryIfTypeAlias = _ZhoneIfXEntryIfTypeAlias_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 4),
    _ZhoneIfXEntryIfTypeAlias_Type()
)
zhoneIfXEntryIfTypeAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIfXEntryIfTypeAlias.setStatus("current")
_ZhoneIfXEntryRowStatus_Type = ZhoneRowStatus
_ZhoneIfXEntryRowStatus_Object = MibTableColumn
zhoneIfXEntryRowStatus = _ZhoneIfXEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 5),
    _ZhoneIfXEntryRowStatus_Type()
)
zhoneIfXEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIfXEntryRowStatus.setStatus("current")


class _ZhoneIfXEntryShelfAlias_Type(Integer32):
    """Custom type zhoneIfXEntryShelfAlias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ZhoneIfXEntryShelfAlias_Type.__name__ = "Integer32"
_ZhoneIfXEntryShelfAlias_Object = MibTableColumn
zhoneIfXEntryShelfAlias = _ZhoneIfXEntryShelfAlias_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 6),
    _ZhoneIfXEntryShelfAlias_Type()
)
zhoneIfXEntryShelfAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIfXEntryShelfAlias.setStatus("current")


class _ZhoneIfXEntrySlotAlias_Type(Integer32):
    """Custom type zhoneIfXEntrySlotAlias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_ZhoneIfXEntrySlotAlias_Type.__name__ = "Integer32"
_ZhoneIfXEntrySlotAlias_Object = MibTableColumn
zhoneIfXEntrySlotAlias = _ZhoneIfXEntrySlotAlias_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 7),
    _ZhoneIfXEntrySlotAlias_Type()
)
zhoneIfXEntrySlotAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIfXEntrySlotAlias.setStatus("current")
_ZhoneIfXEntryPortAlias_Type = Integer32
_ZhoneIfXEntryPortAlias_Object = MibTableColumn
zhoneIfXEntryPortAlias = _ZhoneIfXEntryPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 8),
    _ZhoneIfXEntryPortAlias_Type()
)
zhoneIfXEntryPortAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIfXEntryPortAlias.setStatus("current")
_ZhoneIfXEntrySubportAlias_Type = Integer32
_ZhoneIfXEntrySubportAlias_Object = MibTableColumn
zhoneIfXEntrySubportAlias = _ZhoneIfXEntrySubportAlias_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 9),
    _ZhoneIfXEntrySubportAlias_Type()
)
zhoneIfXEntrySubportAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIfXEntrySubportAlias.setStatus("current")


class _ZhoneIfXDescriptionIndex_Type(Integer32):
    """Custom type zhoneIfXDescriptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneIfXDescriptionIndex_Type.__name__ = "Integer32"
_ZhoneIfXDescriptionIndex_Object = MibTableColumn
zhoneIfXDescriptionIndex = _ZhoneIfXDescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 6, 1, 10),
    _ZhoneIfXDescriptionIndex_Type()
)
zhoneIfXDescriptionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneIfXDescriptionIndex.setStatus("current")
_ZhonePhysicalToIfIndexTable_Object = MibTable
zhonePhysicalToIfIndexTable = _ZhonePhysicalToIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 7)
)
if mibBuilder.loadTexts:
    zhonePhysicalToIfIndexTable.setStatus("current")
_ZhonePhysicalToIfIndexEntry_Object = MibTableRow
zhonePhysicalToIfIndexEntry = _ZhonePhysicalToIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1)
)
zhonePhysicalToIfIndexEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhonePortIndex"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneSubPortIndex"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfType"),
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfTypeExtension"),
)
if mibBuilder.loadTexts:
    zhonePhysicalToIfIndexEntry.setStatus("current")


class _ZhonePortIndex_Type(Integer32):
    """Custom type zhonePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhonePortIndex_Type.__name__ = "Integer32"
_ZhonePortIndex_Object = MibTableColumn
zhonePortIndex = _ZhonePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 1),
    _ZhonePortIndex_Type()
)
zhonePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhonePortIndex.setStatus("current")


class _ZhoneSubPortIndex_Type(Integer32):
    """Custom type zhoneSubPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneSubPortIndex_Type.__name__ = "Integer32"
_ZhoneSubPortIndex_Object = MibTableColumn
zhoneSubPortIndex = _ZhoneSubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 2),
    _ZhoneSubPortIndex_Type()
)
zhoneSubPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneSubPortIndex.setStatus("current")
_ZhoneIfType_Type = IANAifType
_ZhoneIfType_Object = MibTableColumn
zhoneIfType = _ZhoneIfType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 4),
    _ZhoneIfType_Type()
)
zhoneIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIfType.setStatus("current")
_ZhoneIfTypeExtension_Type = ZhoneIfType
_ZhoneIfTypeExtension_Object = MibTableColumn
zhoneIfTypeExtension = _ZhoneIfTypeExtension_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 5),
    _ZhoneIfTypeExtension_Type()
)
zhoneIfTypeExtension.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIfTypeExtension.setStatus("current")
_ZhonePhysicalIfIndex_Type = InterfaceIndex
_ZhonePhysicalIfIndex_Object = MibTableColumn
zhonePhysicalIfIndex = _ZhonePhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 7, 1, 6),
    _ZhonePhysicalIfIndex_Type()
)
zhonePhysicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhonePhysicalIfIndex.setStatus("current")
_ZhoneDescriptionTable_Object = MibTable
zhoneDescriptionTable = _ZhoneDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 8)
)
if mibBuilder.loadTexts:
    zhoneDescriptionTable.setStatus("current")
_ZhoneDescriptionEntry_Object = MibTableRow
zhoneDescriptionEntry = _ZhoneDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 8, 1)
)
zhoneDescriptionEntry.setIndexNames(
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfXDescriptionIndex"),
)
if mibBuilder.loadTexts:
    zhoneDescriptionEntry.setStatus("current")
_ZhoneDescriptionRowStatus_Type = ZhoneRowStatus
_ZhoneDescriptionRowStatus_Object = MibTableColumn
zhoneDescriptionRowStatus = _ZhoneDescriptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 8, 1, 1),
    _ZhoneDescriptionRowStatus_Type()
)
zhoneDescriptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDescriptionRowStatus.setStatus("current")


class _ZhoneDescriptionText_Type(OctetString):
    """Custom type zhoneDescriptionText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZhoneDescriptionText_Type.__name__ = "OctetString"
_ZhoneDescriptionText_Object = MibTableColumn
zhoneDescriptionText = _ZhoneDescriptionText_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 8, 1, 2),
    _ZhoneDescriptionText_Type()
)
zhoneDescriptionText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDescriptionText.setStatus("current")
_ZhoneIfXDescriptionIndexNext_Type = Unsigned32
_ZhoneIfXDescriptionIndexNext_Object = MibScalar
zhoneIfXDescriptionIndexNext = _ZhoneIfXDescriptionIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 9),
    _ZhoneIfXDescriptionIndexNext_Type()
)
zhoneIfXDescriptionIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIfXDescriptionIndexNext.setStatus("current")
_ZhoneLineRedStatusTable_Object = MibTable
zhoneLineRedStatusTable = _ZhoneLineRedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 10)
)
if mibBuilder.loadTexts:
    zhoneLineRedStatusTable.setStatus("current")
_ZhoneLineRedStatusEntry_Object = MibTableRow
zhoneLineRedStatusEntry = _ZhoneLineRedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 10, 1)
)
zhoneLineRedStatusEntry.setIndexNames(
    (0, "ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneLineRedStatusEntry.setStatus("current")


class _ZhoneLineRedStatusFunction_Type(Integer32):
    """Custom type zhoneLineRedStatusFunction based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("standby", 2),
          ("unavailable", 4))
    )


_ZhoneLineRedStatusFunction_Type.__name__ = "Integer32"
_ZhoneLineRedStatusFunction_Object = MibTableColumn
zhoneLineRedStatusFunction = _ZhoneLineRedStatusFunction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 10, 1, 1),
    _ZhoneLineRedStatusFunction_Type()
)
zhoneLineRedStatusFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLineRedStatusFunction.setStatus("current")


class _ZhoneLineRedOpStatus_Type(Integer32):
    """Custom type zhoneLineRedOpStatus based on Integer32"""
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
        *(("active", 1),
          ("oos", 2),
          ("trafficDisabled", 3),
          ("unavailable", 4))
    )


_ZhoneLineRedOpStatus_Type.__name__ = "Integer32"
_ZhoneLineRedOpStatus_Object = MibTableColumn
zhoneLineRedOpStatus = _ZhoneLineRedOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 10, 1, 2),
    _ZhoneLineRedOpStatus_Type()
)
zhoneLineRedOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLineRedOpStatus.setStatus("current")
_ZhoneLineRedTraps_ObjectIdentity = ObjectIdentity
zhoneLineRedTraps = _ZhoneLineRedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 11)
)
if mibBuilder.loadTexts:
    zhoneLineRedTraps.setStatus("current")
_ZhoneLineRedTrapsPrefix_ObjectIdentity = ObjectIdentity
zhoneLineRedTrapsPrefix = _ZhoneLineRedTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 11, 0)
)
if mibBuilder.loadTexts:
    zhoneLineRedTrapsPrefix.setStatus("current")
ifEntry.registerAugmentions(
    ("ZHONE-INTERFACE-TRANSLATION-MIB",
     "zhoneIfXEntry")
)
zhoneIfXEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects

zhoneLineRedundancyUnsafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 11, 0, 1)
)
if mibBuilder.loadTexts:
    zhoneLineRedundancyUnsafe.setStatus(
        "current"
    )

zhoneLineRedundancySafe = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 5, 11, 0, 2)
)
if mibBuilder.loadTexts:
    zhoneLineRedundancySafe.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-INTERFACE-TRANSLATION-MIB",
    **{"ifIndexNext": ifIndexNext,
       "physicalToIfIndexTable": physicalToIfIndexTable,
       "physicalToIfIndexEntry": physicalToIfIndexEntry,
       "pportIndex": pportIndex,
       "subPortIndex": subPortIndex,
       "zhoneIfIndex": zhoneIfIndex,
       "xxxifTypexxx": xxxifTypexxx,
       "ifIndexToPhysicalTable": ifIndexToPhysicalTable,
       "ifIndexToPhysicalEntry": ifIndexToPhysicalEntry,
       "zhoneShelfNumber": zhoneShelfNumber,
       "zhoneSlotNumber": zhoneSlotNumber,
       "pportNumber": pportNumber,
       "subPortNumber": subPortNumber,
       "ifaceType": ifaceType,
       "ifaceTypeExtension": ifaceTypeExtension,
       "ifStackDefaultTable": ifStackDefaultTable,
       "ifStackDefaultEntry": ifStackDefaultEntry,
       "ifStkDefCardType": ifStkDefCardType,
       "ifStkDefUpperType": ifStkDefUpperType,
       "ifStkDefLowerType": ifStkDefLowerType,
       "ifStkDefUnits": ifStkDefUnits,
       "ifStkDefAdminStatus": ifStkDefAdminStatus,
       "ifStkDefRowStatus": ifStkDefRowStatus,
       "ifInverseStackTable": ifInverseStackTable,
       "ifInverseStackEntry": ifInverseStackEntry,
       "ifInverseStackLowerLayer": ifInverseStackLowerLayer,
       "ifInverseStackHigherLayer": ifInverseStackHigherLayer,
       "ifInverseStackStatus": ifInverseStackStatus,
       "zhoneIfXTable": zhoneIfXTable,
       "zhoneIfXEntry": zhoneIfXEntry,
       "physicalFlag": physicalFlag,
       "ifTypeExtension": ifTypeExtension,
       "redundancyParam1": redundancyParam1,
       "zhoneIfXEntryIfTypeAlias": zhoneIfXEntryIfTypeAlias,
       "zhoneIfXEntryRowStatus": zhoneIfXEntryRowStatus,
       "zhoneIfXEntryShelfAlias": zhoneIfXEntryShelfAlias,
       "zhoneIfXEntrySlotAlias": zhoneIfXEntrySlotAlias,
       "zhoneIfXEntryPortAlias": zhoneIfXEntryPortAlias,
       "zhoneIfXEntrySubportAlias": zhoneIfXEntrySubportAlias,
       "zhoneIfXDescriptionIndex": zhoneIfXDescriptionIndex,
       "zhonePhysicalToIfIndexTable": zhonePhysicalToIfIndexTable,
       "zhonePhysicalToIfIndexEntry": zhonePhysicalToIfIndexEntry,
       "zhonePortIndex": zhonePortIndex,
       "zhoneSubPortIndex": zhoneSubPortIndex,
       "zhoneIfType": zhoneIfType,
       "zhoneIfTypeExtension": zhoneIfTypeExtension,
       "zhonePhysicalIfIndex": zhonePhysicalIfIndex,
       "zhoneDescriptionTable": zhoneDescriptionTable,
       "zhoneDescriptionEntry": zhoneDescriptionEntry,
       "zhoneDescriptionRowStatus": zhoneDescriptionRowStatus,
       "zhoneDescriptionText": zhoneDescriptionText,
       "zhoneIfXDescriptionIndexNext": zhoneIfXDescriptionIndexNext,
       "zhoneLineRedStatusTable": zhoneLineRedStatusTable,
       "zhoneLineRedStatusEntry": zhoneLineRedStatusEntry,
       "zhoneLineRedStatusFunction": zhoneLineRedStatusFunction,
       "zhoneLineRedOpStatus": zhoneLineRedOpStatus,
       "zhoneLineRedTraps": zhoneLineRedTraps,
       "zhoneLineRedTrapsPrefix": zhoneLineRedTrapsPrefix,
       "zhoneLineRedundancyUnsafe": zhoneLineRedundancyUnsafe,
       "zhoneLineRedundancySafe": zhoneLineRedundancySafe,
       "zhoneInterfaceTrans": zhoneInterfaceTrans}
)
