# SNMP MIB module (BAS-ALIAS-DOCS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-ALIAS-DOCS-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:17 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasDocsIf) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasDocsIf")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

basAliasDocsIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1)
)
basAliasDocsIfMib.setRevisions(
        ("1999-08-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TenthdBmV(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class TenthdB(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_BasDocsIfMibObjects_ObjectIdentity = ObjectIdentity
basDocsIfMibObjects = _BasDocsIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1)
)
_BasDocsIfBaseObjects_ObjectIdentity = ObjectIdentity
basDocsIfBaseObjects = _BasDocsIfBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1)
)
_BasDocsIfQosProfileTable_Object = MibTable
basDocsIfQosProfileTable = _BasDocsIfQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    basDocsIfQosProfileTable.setStatus("current")
_BasDocsIfQosProfileEntry_Object = MibTableRow
basDocsIfQosProfileEntry = _BasDocsIfQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1)
)
basDocsIfQosProfileEntry.setIndexNames(
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfQosProfChassis"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfQosProfSlot"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfQosProfIf"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfQosProfLPort"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfQosProfIndex"),
)
if mibBuilder.loadTexts:
    basDocsIfQosProfileEntry.setStatus("current")


class _BasDocsIfQosProfIndex_Type(Integer32):
    """Custom type basDocsIfQosProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_BasDocsIfQosProfIndex_Type.__name__ = "Integer32"
_BasDocsIfQosProfIndex_Object = MibTableColumn
basDocsIfQosProfIndex = _BasDocsIfQosProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 1),
    _BasDocsIfQosProfIndex_Type()
)
basDocsIfQosProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfQosProfIndex.setStatus("current")


class _BasDocsIfQosProfPriority_Type(Integer32):
    """Custom type basDocsIfQosProfPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BasDocsIfQosProfPriority_Type.__name__ = "Integer32"
_BasDocsIfQosProfPriority_Object = MibTableColumn
basDocsIfQosProfPriority = _BasDocsIfQosProfPriority_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 2),
    _BasDocsIfQosProfPriority_Type()
)
basDocsIfQosProfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsIfQosProfPriority.setStatus("current")


class _BasDocsIfQosProfMaxUpBandwidth_Type(Integer32):
    """Custom type basDocsIfQosProfMaxUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_BasDocsIfQosProfMaxUpBandwidth_Type.__name__ = "Integer32"
_BasDocsIfQosProfMaxUpBandwidth_Object = MibTableColumn
basDocsIfQosProfMaxUpBandwidth = _BasDocsIfQosProfMaxUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 3),
    _BasDocsIfQosProfMaxUpBandwidth_Type()
)
basDocsIfQosProfMaxUpBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsIfQosProfMaxUpBandwidth.setStatus("current")


class _BasDocsIfQosProfGuarUpBandwidth_Type(Integer32):
    """Custom type basDocsIfQosProfGuarUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_BasDocsIfQosProfGuarUpBandwidth_Type.__name__ = "Integer32"
_BasDocsIfQosProfGuarUpBandwidth_Object = MibTableColumn
basDocsIfQosProfGuarUpBandwidth = _BasDocsIfQosProfGuarUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 4),
    _BasDocsIfQosProfGuarUpBandwidth_Type()
)
basDocsIfQosProfGuarUpBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsIfQosProfGuarUpBandwidth.setStatus("current")


class _BasDocsIfQosProfMaxDownBandwidth_Type(Integer32):
    """Custom type basDocsIfQosProfMaxDownBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_BasDocsIfQosProfMaxDownBandwidth_Type.__name__ = "Integer32"
_BasDocsIfQosProfMaxDownBandwidth_Object = MibTableColumn
basDocsIfQosProfMaxDownBandwidth = _BasDocsIfQosProfMaxDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 5),
    _BasDocsIfQosProfMaxDownBandwidth_Type()
)
basDocsIfQosProfMaxDownBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsIfQosProfMaxDownBandwidth.setStatus("current")


class _BasDocsIfQosProfMaxTxBurst_Type(Integer32):
    """Custom type basDocsIfQosProfMaxTxBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasDocsIfQosProfMaxTxBurst_Type.__name__ = "Integer32"
_BasDocsIfQosProfMaxTxBurst_Object = MibTableColumn
basDocsIfQosProfMaxTxBurst = _BasDocsIfQosProfMaxTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 6),
    _BasDocsIfQosProfMaxTxBurst_Type()
)
basDocsIfQosProfMaxTxBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsIfQosProfMaxTxBurst.setStatus("current")


class _BasDocsIfQosProfBaselinePrivacy_Type(TruthValue):
    """Custom type basDocsIfQosProfBaselinePrivacy based on TruthValue"""


_BasDocsIfQosProfBaselinePrivacy_Object = MibTableColumn
basDocsIfQosProfBaselinePrivacy = _BasDocsIfQosProfBaselinePrivacy_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 7),
    _BasDocsIfQosProfBaselinePrivacy_Type()
)
basDocsIfQosProfBaselinePrivacy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsIfQosProfBaselinePrivacy.setStatus("current")
_BasDocsIfQosProfStatus_Type = RowStatus
_BasDocsIfQosProfStatus_Object = MibTableColumn
basDocsIfQosProfStatus = _BasDocsIfQosProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 8),
    _BasDocsIfQosProfStatus_Type()
)
basDocsIfQosProfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basDocsIfQosProfStatus.setStatus("current")
_BasDocsIfQosProfChassis_Type = BasChassisId
_BasDocsIfQosProfChassis_Object = MibTableColumn
basDocsIfQosProfChassis = _BasDocsIfQosProfChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 9),
    _BasDocsIfQosProfChassis_Type()
)
basDocsIfQosProfChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfQosProfChassis.setStatus("current")
_BasDocsIfQosProfSlot_Type = BasSlotId
_BasDocsIfQosProfSlot_Object = MibTableColumn
basDocsIfQosProfSlot = _BasDocsIfQosProfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 10),
    _BasDocsIfQosProfSlot_Type()
)
basDocsIfQosProfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfQosProfSlot.setStatus("current")
_BasDocsIfQosProfIf_Type = BasInterfaceId
_BasDocsIfQosProfIf_Object = MibTableColumn
basDocsIfQosProfIf = _BasDocsIfQosProfIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 11),
    _BasDocsIfQosProfIf_Type()
)
basDocsIfQosProfIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfQosProfIf.setStatus("current")
_BasDocsIfQosProfLPort_Type = BasLogicalPortId
_BasDocsIfQosProfLPort_Object = MibTableColumn
basDocsIfQosProfLPort = _BasDocsIfQosProfLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 1, 3, 1, 12),
    _BasDocsIfQosProfLPort_Type()
)
basDocsIfQosProfLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfQosProfLPort.setStatus("current")
_BasDocsIfCmObjects_ObjectIdentity = ObjectIdentity
basDocsIfCmObjects = _BasDocsIfCmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 2)
)
_BasDocsIfCmtsObjects_ObjectIdentity = ObjectIdentity
basDocsIfCmtsObjects = _BasDocsIfCmtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3)
)
_BasDocsIfCmtsCmStatusTable_Object = MibTable
basDocsIfCmtsCmStatusTable = _BasDocsIfCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusTable.setStatus("current")
_BasDocsIfCmtsCmStatusEntry_Object = MibTableRow
basDocsIfCmtsCmStatusEntry = _BasDocsIfCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1)
)
basDocsIfCmtsCmStatusEntry.setIndexNames(
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmStatusChassis"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmStatusSlot"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmStatusIf"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmStatusLPort"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusEntry.setStatus("current")


class _BasDocsIfCmtsCmStatusIndex_Type(Integer32):
    """Custom type basDocsIfCmtsCmStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasDocsIfCmtsCmStatusIndex_Type.__name__ = "Integer32"
_BasDocsIfCmtsCmStatusIndex_Object = MibTableColumn
basDocsIfCmtsCmStatusIndex = _BasDocsIfCmtsCmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 1),
    _BasDocsIfCmtsCmStatusIndex_Type()
)
basDocsIfCmtsCmStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusIndex.setStatus("current")
_BasDocsIfCmtsCmStatusMacAddress_Type = MacAddress
_BasDocsIfCmtsCmStatusMacAddress_Object = MibTableColumn
basDocsIfCmtsCmStatusMacAddress = _BasDocsIfCmtsCmStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 2),
    _BasDocsIfCmtsCmStatusMacAddress_Type()
)
basDocsIfCmtsCmStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusMacAddress.setStatus("current")
_BasDocsIfCmtsCmStatusIpAddress_Type = IpAddress
_BasDocsIfCmtsCmStatusIpAddress_Object = MibTableColumn
basDocsIfCmtsCmStatusIpAddress = _BasDocsIfCmtsCmStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 3),
    _BasDocsIfCmtsCmStatusIpAddress_Type()
)
basDocsIfCmtsCmStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusIpAddress.setStatus("current")
_BasDocsIfCmtsCmStatusDownChannelIfIndex_Type = InterfaceIndexOrZero
_BasDocsIfCmtsCmStatusDownChannelIfIndex_Object = MibTableColumn
basDocsIfCmtsCmStatusDownChannelIfIndex = _BasDocsIfCmtsCmStatusDownChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 4),
    _BasDocsIfCmtsCmStatusDownChannelIfIndex_Type()
)
basDocsIfCmtsCmStatusDownChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusDownChannelIfIndex.setStatus("current")
_BasDocsIfCmtsCmStatusUpChannelIfIndex_Type = InterfaceIndexOrZero
_BasDocsIfCmtsCmStatusUpChannelIfIndex_Object = MibTableColumn
basDocsIfCmtsCmStatusUpChannelIfIndex = _BasDocsIfCmtsCmStatusUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 5),
    _BasDocsIfCmtsCmStatusUpChannelIfIndex_Type()
)
basDocsIfCmtsCmStatusUpChannelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusUpChannelIfIndex.setStatus("current")
_BasDocsIfCmtsCmStatusRxPower_Type = TenthdBmV
_BasDocsIfCmtsCmStatusRxPower_Object = MibTableColumn
basDocsIfCmtsCmStatusRxPower = _BasDocsIfCmtsCmStatusRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 6),
    _BasDocsIfCmtsCmStatusRxPower_Type()
)
basDocsIfCmtsCmStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusRxPower.setStatus("current")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusRxPower.setUnits("dBmV")
_BasDocsIfCmtsCmStatusTimingOffset_Type = Unsigned32
_BasDocsIfCmtsCmStatusTimingOffset_Object = MibTableColumn
basDocsIfCmtsCmStatusTimingOffset = _BasDocsIfCmtsCmStatusTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 7),
    _BasDocsIfCmtsCmStatusTimingOffset_Type()
)
basDocsIfCmtsCmStatusTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusTimingOffset.setStatus("current")
_BasDocsIfCmtsCmStatusEqualizationData_Type = OctetString
_BasDocsIfCmtsCmStatusEqualizationData_Object = MibTableColumn
basDocsIfCmtsCmStatusEqualizationData = _BasDocsIfCmtsCmStatusEqualizationData_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 8),
    _BasDocsIfCmtsCmStatusEqualizationData_Type()
)
basDocsIfCmtsCmStatusEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusEqualizationData.setStatus("current")


class _BasDocsIfCmtsCmStatusValue_Type(Integer32):
    """Custom type basDocsIfCmtsCmStatusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 7),
          ("ipComplete", 5),
          ("other", 1),
          ("ranging", 2),
          ("rangingAborted", 3),
          ("rangingComplete", 4),
          ("registrationComplete", 6))
    )


_BasDocsIfCmtsCmStatusValue_Type.__name__ = "Integer32"
_BasDocsIfCmtsCmStatusValue_Object = MibTableColumn
basDocsIfCmtsCmStatusValue = _BasDocsIfCmtsCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 9),
    _BasDocsIfCmtsCmStatusValue_Type()
)
basDocsIfCmtsCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusValue.setStatus("current")
_BasDocsIfCmtsCmStatusUnerroreds_Type = Counter32
_BasDocsIfCmtsCmStatusUnerroreds_Object = MibTableColumn
basDocsIfCmtsCmStatusUnerroreds = _BasDocsIfCmtsCmStatusUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 10),
    _BasDocsIfCmtsCmStatusUnerroreds_Type()
)
basDocsIfCmtsCmStatusUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusUnerroreds.setStatus("current")
_BasDocsIfCmtsCmStatusCorrecteds_Type = Counter32
_BasDocsIfCmtsCmStatusCorrecteds_Object = MibTableColumn
basDocsIfCmtsCmStatusCorrecteds = _BasDocsIfCmtsCmStatusCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 11),
    _BasDocsIfCmtsCmStatusCorrecteds_Type()
)
basDocsIfCmtsCmStatusCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusCorrecteds.setStatus("current")
_BasDocsIfCmtsCmStatusUncorrectables_Type = Counter32
_BasDocsIfCmtsCmStatusUncorrectables_Object = MibTableColumn
basDocsIfCmtsCmStatusUncorrectables = _BasDocsIfCmtsCmStatusUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 12),
    _BasDocsIfCmtsCmStatusUncorrectables_Type()
)
basDocsIfCmtsCmStatusUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusUncorrectables.setStatus("current")
_BasDocsIfCmtsCmStatusSignalNoise_Type = TenthdB
_BasDocsIfCmtsCmStatusSignalNoise_Object = MibTableColumn
basDocsIfCmtsCmStatusSignalNoise = _BasDocsIfCmtsCmStatusSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 13),
    _BasDocsIfCmtsCmStatusSignalNoise_Type()
)
basDocsIfCmtsCmStatusSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusSignalNoise.setUnits("dB")


class _BasDocsIfCmtsCmStatusMicroreflections_Type(Integer32):
    """Custom type basDocsIfCmtsCmStatusMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasDocsIfCmtsCmStatusMicroreflections_Type.__name__ = "Integer32"
_BasDocsIfCmtsCmStatusMicroreflections_Object = MibTableColumn
basDocsIfCmtsCmStatusMicroreflections = _BasDocsIfCmtsCmStatusMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 14),
    _BasDocsIfCmtsCmStatusMicroreflections_Type()
)
basDocsIfCmtsCmStatusMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusMicroreflections.setUnits("dBc")
_BasDocsIfCmtsCmStatusChassis_Type = BasChassisId
_BasDocsIfCmtsCmStatusChassis_Object = MibTableColumn
basDocsIfCmtsCmStatusChassis = _BasDocsIfCmtsCmStatusChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 15),
    _BasDocsIfCmtsCmStatusChassis_Type()
)
basDocsIfCmtsCmStatusChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusChassis.setStatus("current")
_BasDocsIfCmtsCmStatusSlot_Type = BasSlotId
_BasDocsIfCmtsCmStatusSlot_Object = MibTableColumn
basDocsIfCmtsCmStatusSlot = _BasDocsIfCmtsCmStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 16),
    _BasDocsIfCmtsCmStatusSlot_Type()
)
basDocsIfCmtsCmStatusSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusSlot.setStatus("current")
_BasDocsIfCmtsCmStatusIf_Type = BasInterfaceId
_BasDocsIfCmtsCmStatusIf_Object = MibTableColumn
basDocsIfCmtsCmStatusIf = _BasDocsIfCmtsCmStatusIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 17),
    _BasDocsIfCmtsCmStatusIf_Type()
)
basDocsIfCmtsCmStatusIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusIf.setStatus("current")
_BasDocsIfCmtsCmStatusLPort_Type = BasLogicalPortId
_BasDocsIfCmtsCmStatusLPort_Object = MibTableColumn
basDocsIfCmtsCmStatusLPort = _BasDocsIfCmtsCmStatusLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 3, 1, 18),
    _BasDocsIfCmtsCmStatusLPort_Type()
)
basDocsIfCmtsCmStatusLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmStatusLPort.setStatus("current")
_BasDocsIfCmtsQosProfileTable_Object = MibTable
basDocsIfCmtsQosProfileTable = _BasDocsIfCmtsQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    basDocsIfCmtsQosProfileTable.setStatus("current")
_BasDocsIfCmtsQosProfileEntry_Object = MibTableRow
basDocsIfCmtsQosProfileEntry = _BasDocsIfCmtsQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 6, 1)
)
basDocsIfCmtsQosProfileEntry.setIndexNames(
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsQosProfileChassis"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsQosProfileSlot"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsQosProfileIf"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsQosProfileLPort"),
)
if mibBuilder.loadTexts:
    basDocsIfCmtsQosProfileEntry.setStatus("current")


class _BasDocsIfCmtsQosProfilePermissions_Type(Bits):
    """Custom type basDocsIfCmtsQosProfilePermissions based on Bits"""
    namedValues = NamedValues(
        *(("createByManagement", 0),
          ("createByModems", 2),
          ("updateByManagement", 1))
    )

_BasDocsIfCmtsQosProfilePermissions_Type.__name__ = "Bits"
_BasDocsIfCmtsQosProfilePermissions_Object = MibTableColumn
basDocsIfCmtsQosProfilePermissions = _BasDocsIfCmtsQosProfilePermissions_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 6, 1, 6),
    _BasDocsIfCmtsQosProfilePermissions_Type()
)
basDocsIfCmtsQosProfilePermissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basDocsIfCmtsQosProfilePermissions.setStatus("current")
_BasDocsIfCmtsQosProfileChassis_Type = BasChassisId
_BasDocsIfCmtsQosProfileChassis_Object = MibTableColumn
basDocsIfCmtsQosProfileChassis = _BasDocsIfCmtsQosProfileChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 6, 1, 7),
    _BasDocsIfCmtsQosProfileChassis_Type()
)
basDocsIfCmtsQosProfileChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsQosProfileChassis.setStatus("current")
_BasDocsIfCmtsQosProfileSlot_Type = BasSlotId
_BasDocsIfCmtsQosProfileSlot_Object = MibTableColumn
basDocsIfCmtsQosProfileSlot = _BasDocsIfCmtsQosProfileSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 6, 1, 8),
    _BasDocsIfCmtsQosProfileSlot_Type()
)
basDocsIfCmtsQosProfileSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsQosProfileSlot.setStatus("current")
_BasDocsIfCmtsQosProfileIf_Type = BasInterfaceId
_BasDocsIfCmtsQosProfileIf_Object = MibTableColumn
basDocsIfCmtsQosProfileIf = _BasDocsIfCmtsQosProfileIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 6, 1, 9),
    _BasDocsIfCmtsQosProfileIf_Type()
)
basDocsIfCmtsQosProfileIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsQosProfileIf.setStatus("current")
_BasDocsIfCmtsQosProfileLPort_Type = BasLogicalPortId
_BasDocsIfCmtsQosProfileLPort_Object = MibTableColumn
basDocsIfCmtsQosProfileLPort = _BasDocsIfCmtsQosProfileLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 6, 1, 10),
    _BasDocsIfCmtsQosProfileLPort_Type()
)
basDocsIfCmtsQosProfileLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsQosProfileLPort.setStatus("current")
_BasDocsIfCmtsMacToCmTable_Object = MibTable
basDocsIfCmtsMacToCmTable = _BasDocsIfCmtsMacToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    basDocsIfCmtsMacToCmTable.setStatus("current")
_BasDocsIfCmtsMacToCmEntry_Object = MibTableRow
basDocsIfCmtsMacToCmEntry = _BasDocsIfCmtsMacToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7, 1)
)
basDocsIfCmtsMacToCmEntry.setIndexNames(
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmChassis"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmSlot"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmIf"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmLPort"),
    (0, "BAS-ALIAS-DOCS-IF-MIB", "basDocsIfCmtsCmMac"),
)
if mibBuilder.loadTexts:
    basDocsIfCmtsMacToCmEntry.setStatus("current")
_BasDocsIfCmtsCmMac_Type = MacAddress
_BasDocsIfCmtsCmMac_Object = MibTableColumn
basDocsIfCmtsCmMac = _BasDocsIfCmtsCmMac_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7, 1, 1),
    _BasDocsIfCmtsCmMac_Type()
)
basDocsIfCmtsCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmMac.setStatus("current")


class _BasDocsIfCmtsCmPtr_Type(Integer32):
    """Custom type basDocsIfCmtsCmPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasDocsIfCmtsCmPtr_Type.__name__ = "Integer32"
_BasDocsIfCmtsCmPtr_Object = MibTableColumn
basDocsIfCmtsCmPtr = _BasDocsIfCmtsCmPtr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7, 1, 2),
    _BasDocsIfCmtsCmPtr_Type()
)
basDocsIfCmtsCmPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmPtr.setStatus("current")
_BasDocsIfCmtsCmChassis_Type = BasChassisId
_BasDocsIfCmtsCmChassis_Object = MibTableColumn
basDocsIfCmtsCmChassis = _BasDocsIfCmtsCmChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7, 1, 3),
    _BasDocsIfCmtsCmChassis_Type()
)
basDocsIfCmtsCmChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmChassis.setStatus("current")
_BasDocsIfCmtsCmSlot_Type = BasSlotId
_BasDocsIfCmtsCmSlot_Object = MibTableColumn
basDocsIfCmtsCmSlot = _BasDocsIfCmtsCmSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7, 1, 4),
    _BasDocsIfCmtsCmSlot_Type()
)
basDocsIfCmtsCmSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmSlot.setStatus("current")
_BasDocsIfCmtsCmIf_Type = BasInterfaceId
_BasDocsIfCmtsCmIf_Object = MibTableColumn
basDocsIfCmtsCmIf = _BasDocsIfCmtsCmIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7, 1, 5),
    _BasDocsIfCmtsCmIf_Type()
)
basDocsIfCmtsCmIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmIf.setStatus("current")
_BasDocsIfCmtsCmLPort_Type = BasLogicalPortId
_BasDocsIfCmtsCmLPort_Object = MibTableColumn
basDocsIfCmtsCmLPort = _BasDocsIfCmtsCmLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 8, 1, 1, 3, 7, 1, 6),
    _BasDocsIfCmtsCmLPort_Type()
)
basDocsIfCmtsCmLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basDocsIfCmtsCmLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-ALIAS-DOCS-IF-MIB",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "TenthdBmV": TenthdBmV,
       "TenthdB": TenthdB,
       "basAliasDocsIfMib": basAliasDocsIfMib,
       "basDocsIfMibObjects": basDocsIfMibObjects,
       "basDocsIfBaseObjects": basDocsIfBaseObjects,
       "basDocsIfQosProfileTable": basDocsIfQosProfileTable,
       "basDocsIfQosProfileEntry": basDocsIfQosProfileEntry,
       "basDocsIfQosProfIndex": basDocsIfQosProfIndex,
       "basDocsIfQosProfPriority": basDocsIfQosProfPriority,
       "basDocsIfQosProfMaxUpBandwidth": basDocsIfQosProfMaxUpBandwidth,
       "basDocsIfQosProfGuarUpBandwidth": basDocsIfQosProfGuarUpBandwidth,
       "basDocsIfQosProfMaxDownBandwidth": basDocsIfQosProfMaxDownBandwidth,
       "basDocsIfQosProfMaxTxBurst": basDocsIfQosProfMaxTxBurst,
       "basDocsIfQosProfBaselinePrivacy": basDocsIfQosProfBaselinePrivacy,
       "basDocsIfQosProfStatus": basDocsIfQosProfStatus,
       "basDocsIfQosProfChassis": basDocsIfQosProfChassis,
       "basDocsIfQosProfSlot": basDocsIfQosProfSlot,
       "basDocsIfQosProfIf": basDocsIfQosProfIf,
       "basDocsIfQosProfLPort": basDocsIfQosProfLPort,
       "basDocsIfCmObjects": basDocsIfCmObjects,
       "basDocsIfCmtsObjects": basDocsIfCmtsObjects,
       "basDocsIfCmtsCmStatusTable": basDocsIfCmtsCmStatusTable,
       "basDocsIfCmtsCmStatusEntry": basDocsIfCmtsCmStatusEntry,
       "basDocsIfCmtsCmStatusIndex": basDocsIfCmtsCmStatusIndex,
       "basDocsIfCmtsCmStatusMacAddress": basDocsIfCmtsCmStatusMacAddress,
       "basDocsIfCmtsCmStatusIpAddress": basDocsIfCmtsCmStatusIpAddress,
       "basDocsIfCmtsCmStatusDownChannelIfIndex": basDocsIfCmtsCmStatusDownChannelIfIndex,
       "basDocsIfCmtsCmStatusUpChannelIfIndex": basDocsIfCmtsCmStatusUpChannelIfIndex,
       "basDocsIfCmtsCmStatusRxPower": basDocsIfCmtsCmStatusRxPower,
       "basDocsIfCmtsCmStatusTimingOffset": basDocsIfCmtsCmStatusTimingOffset,
       "basDocsIfCmtsCmStatusEqualizationData": basDocsIfCmtsCmStatusEqualizationData,
       "basDocsIfCmtsCmStatusValue": basDocsIfCmtsCmStatusValue,
       "basDocsIfCmtsCmStatusUnerroreds": basDocsIfCmtsCmStatusUnerroreds,
       "basDocsIfCmtsCmStatusCorrecteds": basDocsIfCmtsCmStatusCorrecteds,
       "basDocsIfCmtsCmStatusUncorrectables": basDocsIfCmtsCmStatusUncorrectables,
       "basDocsIfCmtsCmStatusSignalNoise": basDocsIfCmtsCmStatusSignalNoise,
       "basDocsIfCmtsCmStatusMicroreflections": basDocsIfCmtsCmStatusMicroreflections,
       "basDocsIfCmtsCmStatusChassis": basDocsIfCmtsCmStatusChassis,
       "basDocsIfCmtsCmStatusSlot": basDocsIfCmtsCmStatusSlot,
       "basDocsIfCmtsCmStatusIf": basDocsIfCmtsCmStatusIf,
       "basDocsIfCmtsCmStatusLPort": basDocsIfCmtsCmStatusLPort,
       "basDocsIfCmtsQosProfileTable": basDocsIfCmtsQosProfileTable,
       "basDocsIfCmtsQosProfileEntry": basDocsIfCmtsQosProfileEntry,
       "basDocsIfCmtsQosProfilePermissions": basDocsIfCmtsQosProfilePermissions,
       "basDocsIfCmtsQosProfileChassis": basDocsIfCmtsQosProfileChassis,
       "basDocsIfCmtsQosProfileSlot": basDocsIfCmtsQosProfileSlot,
       "basDocsIfCmtsQosProfileIf": basDocsIfCmtsQosProfileIf,
       "basDocsIfCmtsQosProfileLPort": basDocsIfCmtsQosProfileLPort,
       "basDocsIfCmtsMacToCmTable": basDocsIfCmtsMacToCmTable,
       "basDocsIfCmtsMacToCmEntry": basDocsIfCmtsMacToCmEntry,
       "basDocsIfCmtsCmMac": basDocsIfCmtsCmMac,
       "basDocsIfCmtsCmPtr": basDocsIfCmtsCmPtr,
       "basDocsIfCmtsCmChassis": basDocsIfCmtsCmChassis,
       "basDocsIfCmtsCmSlot": basDocsIfCmtsCmSlot,
       "basDocsIfCmtsCmIf": basDocsIfCmtsCmIf,
       "basDocsIfCmtsCmLPort": basDocsIfCmtsCmLPort}
)
