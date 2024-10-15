# SNMP MIB module (HM2-FW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-FW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:57 2024
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

(HmActionValue,
 HmEnabledStatus,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmActionValue",
    "HmEnabledStatus",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2FwMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79)
)
hm2FwMib.setRevisions(
        ("2011-09-13 00:00",
         "2011-07-01 00:00",
         "2011-06-14 00:00",
         "2011-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2FwNotifications_ObjectIdentity = ObjectIdentity
hm2FwNotifications = _Hm2FwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 0)
)
_Hm2FwObjects_ObjectIdentity = ObjectIdentity
hm2FwObjects = _Hm2FwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1)
)
_Hm2FwGeneralSettings_ObjectIdentity = ObjectIdentity
hm2FwGeneralSettings = _Hm2FwGeneralSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1)
)
_Hm2DynFwMaxRules_Type = Integer32
_Hm2DynFwMaxRules_Object = MibScalar
hm2DynFwMaxRules = _Hm2DynFwMaxRules_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 1),
    _Hm2DynFwMaxRules_Type()
)
hm2DynFwMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwMaxRules.setStatus("current")
_Hm2L3MaxRules_Type = Integer32
_Hm2L3MaxRules_Object = MibScalar
hm2L3MaxRules = _Hm2L3MaxRules_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 2),
    _Hm2L3MaxRules_Type()
)
hm2L3MaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3MaxRules.setStatus("current")
_Hm2ResetStatistics_Type = HmActionValue
_Hm2ResetStatistics_Object = MibScalar
hm2ResetStatistics = _Hm2ResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 3),
    _Hm2ResetStatistics_Type()
)
hm2ResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ResetStatistics.setStatus("current")
_Hm2FlushTables_Type = HmActionValue
_Hm2FlushTables_Object = MibScalar
hm2FlushTables = _Hm2FlushTables_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 4),
    _Hm2FlushTables_Type()
)
hm2FlushTables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FlushTables.setStatus("current")


class _Hm2DefaultPolicy_Type(Integer32):
    """Custom type hm2DefaultPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_Hm2DefaultPolicy_Type.__name__ = "Integer32"
_Hm2DefaultPolicy_Object = MibScalar
hm2DefaultPolicy = _Hm2DefaultPolicy_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 5),
    _Hm2DefaultPolicy_Type()
)
hm2DefaultPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DefaultPolicy.setStatus("current")


class _Hm2ConnTrackValidateCheckSum_Type(TruthValue):
    """Custom type hm2ConnTrackValidateCheckSum based on TruthValue"""


_Hm2ConnTrackValidateCheckSum_Object = MibScalar
hm2ConnTrackValidateCheckSum = _Hm2ConnTrackValidateCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 1, 6),
    _Hm2ConnTrackValidateCheckSum_Type()
)
hm2ConnTrackValidateCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ConnTrackValidateCheckSum.setStatus("current")
_Hm2DynFw_ObjectIdentity = ObjectIdentity
hm2DynFw = _Hm2DynFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2)
)
_Hm2DynFwRuleObjects_ObjectIdentity = ObjectIdentity
hm2DynFwRuleObjects = _Hm2DynFwRuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1)
)
_Hm2DynFwRuleCount_Type = Integer32
_Hm2DynFwRuleCount_Object = MibScalar
hm2DynFwRuleCount = _Hm2DynFwRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 1),
    _Hm2DynFwRuleCount_Type()
)
hm2DynFwRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwRuleCount.setStatus("current")
_Hm2DynFwIfMappingRuleCount_Type = Integer32
_Hm2DynFwIfMappingRuleCount_Object = MibScalar
hm2DynFwIfMappingRuleCount = _Hm2DynFwIfMappingRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 2),
    _Hm2DynFwIfMappingRuleCount_Type()
)
hm2DynFwIfMappingRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwIfMappingRuleCount.setStatus("current")


class _Hm2DynFwRulePendingActions_Type(TruthValue):
    """Custom type hm2DynFwRulePendingActions based on TruthValue"""


_Hm2DynFwRulePendingActions_Object = MibScalar
hm2DynFwRulePendingActions = _Hm2DynFwRulePendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 3),
    _Hm2DynFwRulePendingActions_Type()
)
hm2DynFwRulePendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwRulePendingActions.setStatus("current")


class _Hm2DynFwCommitPendingActions_Type(HmActionValue):
    """Custom type hm2DynFwCommitPendingActions based on HmActionValue"""


_Hm2DynFwCommitPendingActions_Object = MibScalar
hm2DynFwCommitPendingActions = _Hm2DynFwCommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 1, 4),
    _Hm2DynFwCommitPendingActions_Type()
)
hm2DynFwCommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DynFwCommitPendingActions.setStatus("current")
_Hm2DynFwRuleTables_ObjectIdentity = ObjectIdentity
hm2DynFwRuleTables = _Hm2DynFwRuleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2)
)
_Hm2DynFwRuleTable_Object = MibTable
hm2DynFwRuleTable = _Hm2DynFwRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DynFwRuleTable.setStatus("current")
_Hm2DynFwRuleEntry_Object = MibTableRow
hm2DynFwRuleEntry = _Hm2DynFwRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1)
)
hm2DynFwRuleEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2DynFwRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DynFwRuleEntry.setStatus("current")


class _Hm2DynFwRuleIndex_Type(Integer32):
    """Custom type hm2DynFwRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_Hm2DynFwRuleIndex_Type.__name__ = "Integer32"
_Hm2DynFwRuleIndex_Object = MibTableColumn
hm2DynFwRuleIndex = _Hm2DynFwRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 1),
    _Hm2DynFwRuleIndex_Type()
)
hm2DynFwRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2DynFwRuleIndex.setStatus("current")


class _Hm2DynFwSourceAddress_Type(DisplayString):
    """Custom type hm2DynFwSourceAddress based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DynFwSourceAddress_Type.__name__ = "DisplayString"
_Hm2DynFwSourceAddress_Object = MibTableColumn
hm2DynFwSourceAddress = _Hm2DynFwSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 2),
    _Hm2DynFwSourceAddress_Type()
)
hm2DynFwSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwSourceAddress.setStatus("current")


class _Hm2DynFwSourcePort_Type(DisplayString):
    """Custom type hm2DynFwSourcePort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2DynFwSourcePort_Type.__name__ = "DisplayString"
_Hm2DynFwSourcePort_Object = MibTableColumn
hm2DynFwSourcePort = _Hm2DynFwSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 3),
    _Hm2DynFwSourcePort_Type()
)
hm2DynFwSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwSourcePort.setStatus("current")


class _Hm2DynFwTargetAddress_Type(DisplayString):
    """Custom type hm2DynFwTargetAddress based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DynFwTargetAddress_Type.__name__ = "DisplayString"
_Hm2DynFwTargetAddress_Object = MibTableColumn
hm2DynFwTargetAddress = _Hm2DynFwTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 4),
    _Hm2DynFwTargetAddress_Type()
)
hm2DynFwTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwTargetAddress.setStatus("current")


class _Hm2DynFwTargetPort_Type(DisplayString):
    """Custom type hm2DynFwTargetPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2DynFwTargetPort_Type.__name__ = "DisplayString"
_Hm2DynFwTargetPort_Object = MibTableColumn
hm2DynFwTargetPort = _Hm2DynFwTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 5),
    _Hm2DynFwTargetPort_Type()
)
hm2DynFwTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwTargetPort.setStatus("current")


class _Hm2DynFwProto_Type(Integer32):
    """Custom type hm2DynFwProto based on Integer32"""
    defaultValue = 9

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ah", 7),
          ("any", 9),
          ("esp", 6),
          ("icmp", 1),
          ("icmpv6", 8),
          ("igmp", 2),
          ("ipip", 3),
          ("tcp", 4),
          ("udp", 5))
    )


_Hm2DynFwProto_Type.__name__ = "Integer32"
_Hm2DynFwProto_Object = MibTableColumn
hm2DynFwProto = _Hm2DynFwProto_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 6),
    _Hm2DynFwProto_Type()
)
hm2DynFwProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwProto.setStatus("current")


class _Hm2DynFwRuleParams_Type(DisplayString):
    """Custom type hm2DynFwRuleParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hm2DynFwRuleParams_Type.__name__ = "DisplayString"
_Hm2DynFwRuleParams_Object = MibTableColumn
hm2DynFwRuleParams = _Hm2DynFwRuleParams_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 7),
    _Hm2DynFwRuleParams_Type()
)
hm2DynFwRuleParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwRuleParams.setStatus("current")


class _Hm2DynFwAction_Type(Integer32):
    """Custom type hm2DynFwAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_Hm2DynFwAction_Type.__name__ = "Integer32"
_Hm2DynFwAction_Object = MibTableColumn
hm2DynFwAction = _Hm2DynFwAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 8),
    _Hm2DynFwAction_Type()
)
hm2DynFwAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwAction.setStatus("current")


class _Hm2DynFwLog_Type(TruthValue):
    """Custom type hm2DynFwLog based on TruthValue"""


_Hm2DynFwLog_Object = MibTableColumn
hm2DynFwLog = _Hm2DynFwLog_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 9),
    _Hm2DynFwLog_Type()
)
hm2DynFwLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwLog.setStatus("current")


class _Hm2DynFwTrap_Type(TruthValue):
    """Custom type hm2DynFwTrap based on TruthValue"""


_Hm2DynFwTrap_Object = MibTableColumn
hm2DynFwTrap = _Hm2DynFwTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 10),
    _Hm2DynFwTrap_Type()
)
hm2DynFwTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwTrap.setStatus("current")
_Hm2DynFwRowStatus_Type = RowStatus
_Hm2DynFwRowStatus_Object = MibTableColumn
hm2DynFwRowStatus = _Hm2DynFwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 11),
    _Hm2DynFwRowStatus_Type()
)
hm2DynFwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwRowStatus.setStatus("current")


class _Hm2DynFwDescription_Type(DisplayString):
    """Custom type hm2DynFwDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2DynFwDescription_Type.__name__ = "DisplayString"
_Hm2DynFwDescription_Object = MibTableColumn
hm2DynFwDescription = _Hm2DynFwDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 1, 1, 12),
    _Hm2DynFwDescription_Type()
)
hm2DynFwDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwDescription.setStatus("current")
_Hm2DynFwRuleIfMappingTable_Object = MibTable
hm2DynFwRuleIfMappingTable = _Hm2DynFwRuleIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hm2DynFwRuleIfMappingTable.setStatus("current")
_Hm2DynFwRuleIfMappingEntry_Object = MibTableRow
hm2DynFwRuleIfMappingEntry = _Hm2DynFwRuleIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1)
)
hm2DynFwRuleIfMappingEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2DynFwIfmInterface"),
    (0, "HM2-FW-MIB", "hm2DynFwIfmDirection"),
    (0, "HM2-FW-MIB", "hm2DynFwIfmRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DynFwRuleIfMappingEntry.setStatus("current")


class _Hm2DynFwIfmRuleIndex_Type(Integer32):
    """Custom type hm2DynFwIfmRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Hm2DynFwIfmRuleIndex_Type.__name__ = "Integer32"
_Hm2DynFwIfmRuleIndex_Object = MibTableColumn
hm2DynFwIfmRuleIndex = _Hm2DynFwIfmRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 1),
    _Hm2DynFwIfmRuleIndex_Type()
)
hm2DynFwIfmRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DynFwIfmRuleIndex.setStatus("current")


class _Hm2DynFwIfmDirection_Type(Integer32):
    """Custom type hm2DynFwIfmDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("egress", 2),
          ("ingress", 1))
    )


_Hm2DynFwIfmDirection_Type.__name__ = "Integer32"
_Hm2DynFwIfmDirection_Object = MibTableColumn
hm2DynFwIfmDirection = _Hm2DynFwIfmDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 2),
    _Hm2DynFwIfmDirection_Type()
)
hm2DynFwIfmDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DynFwIfmDirection.setStatus("current")
_Hm2DynFwIfmPriority_Type = Unsigned32
_Hm2DynFwIfmPriority_Object = MibTableColumn
hm2DynFwIfmPriority = _Hm2DynFwIfmPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 3),
    _Hm2DynFwIfmPriority_Type()
)
hm2DynFwIfmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwIfmPriority.setStatus("current")
_Hm2DynFwIfmInterface_Type = InterfaceIndex
_Hm2DynFwIfmInterface_Object = MibTableColumn
hm2DynFwIfmInterface = _Hm2DynFwIfmInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 4),
    _Hm2DynFwIfmInterface_Type()
)
hm2DynFwIfmInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DynFwIfmInterface.setStatus("current")
_Hm2DynFwIfmRowStatus_Type = RowStatus
_Hm2DynFwIfmRowStatus_Object = MibTableColumn
hm2DynFwIfmRowStatus = _Hm2DynFwIfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 2, 2, 1, 5),
    _Hm2DynFwIfmRowStatus_Type()
)
hm2DynFwIfmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DynFwIfmRowStatus.setStatus("current")
_Hm2DynFwStats_ObjectIdentity = ObjectIdentity
hm2DynFwStats = _Hm2DynFwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4)
)
_Hm2DynFwGeneralStats_ObjectIdentity = ObjectIdentity
hm2DynFwGeneralStats = _Hm2DynFwGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1)
)
_Hm2DynFwStatsTtPck_Type = Counter64
_Hm2DynFwStatsTtPck_Object = MibScalar
hm2DynFwStatsTtPck = _Hm2DynFwStatsTtPck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 1),
    _Hm2DynFwStatsTtPck_Type()
)
hm2DynFwStatsTtPck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwStatsTtPck.setStatus("current")
_Hm2DynFwStatsTtPckSize_Type = Counter64
_Hm2DynFwStatsTtPckSize_Object = MibScalar
hm2DynFwStatsTtPckSize = _Hm2DynFwStatsTtPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 2),
    _Hm2DynFwStatsTtPckSize_Type()
)
hm2DynFwStatsTtPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwStatsTtPckSize.setStatus("current")
_Hm2DynFwStatsTtPckDenDrop_Type = Counter64
_Hm2DynFwStatsTtPckDenDrop_Object = MibScalar
hm2DynFwStatsTtPckDenDrop = _Hm2DynFwStatsTtPckDenDrop_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 3),
    _Hm2DynFwStatsTtPckDenDrop_Type()
)
hm2DynFwStatsTtPckDenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwStatsTtPckDenDrop.setStatus("current")
_Hm2DynFwStatsTtPckAccepted_Type = Counter64
_Hm2DynFwStatsTtPckAccepted_Object = MibScalar
hm2DynFwStatsTtPckAccepted = _Hm2DynFwStatsTtPckAccepted_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 1, 4),
    _Hm2DynFwStatsTtPckAccepted_Type()
)
hm2DynFwStatsTtPckAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwStatsTtPckAccepted.setStatus("current")
_Hm2DynFwStatsTables_ObjectIdentity = ObjectIdentity
hm2DynFwStatsTables = _Hm2DynFwStatsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2)
)
_Hm2DynFwStatsRuleTable_Object = MibTable
hm2DynFwStatsRuleTable = _Hm2DynFwStatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DynFwStatsRuleTable.setStatus("current")
_Hm2DynFwStatsRuleEntry_Object = MibTableRow
hm2DynFwStatsRuleEntry = _Hm2DynFwStatsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1)
)
hm2DynFwStatsRuleEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2DynFwRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DynFwStatsRuleEntry.setStatus("current")
_Hm2DynFwStatsPacketCount_Type = Counter64
_Hm2DynFwStatsPacketCount_Object = MibTableColumn
hm2DynFwStatsPacketCount = _Hm2DynFwStatsPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1, 1),
    _Hm2DynFwStatsPacketCount_Type()
)
hm2DynFwStatsPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwStatsPacketCount.setStatus("current")
_Hm2DynFwStatsPacketSize_Type = Counter64
_Hm2DynFwStatsPacketSize_Object = MibTableColumn
hm2DynFwStatsPacketSize = _Hm2DynFwStatsPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1, 2),
    _Hm2DynFwStatsPacketSize_Type()
)
hm2DynFwStatsPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwStatsPacketSize.setStatus("current")
_Hm2DynFwStatsLastApplied_Type = HmTimeSeconds1970
_Hm2DynFwStatsLastApplied_Object = MibTableColumn
hm2DynFwStatsLastApplied = _Hm2DynFwStatsLastApplied_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 2, 4, 2, 1, 1, 3),
    _Hm2DynFwStatsLastApplied_Type()
)
hm2DynFwStatsLastApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DynFwStatsLastApplied.setStatus("current")
_Hm2L3Fw_ObjectIdentity = ObjectIdentity
hm2L3Fw = _Hm2L3Fw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3)
)
_Hm2L3RuleObjects_ObjectIdentity = ObjectIdentity
hm2L3RuleObjects = _Hm2L3RuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1)
)
_Hm2L3RuleCount_Type = Integer32
_Hm2L3RuleCount_Object = MibScalar
hm2L3RuleCount = _Hm2L3RuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 1),
    _Hm2L3RuleCount_Type()
)
hm2L3RuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3RuleCount.setStatus("current")
_Hm2L3IfMappingRuleCount_Type = Integer32
_Hm2L3IfMappingRuleCount_Object = MibScalar
hm2L3IfMappingRuleCount = _Hm2L3IfMappingRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 2),
    _Hm2L3IfMappingRuleCount_Type()
)
hm2L3IfMappingRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3IfMappingRuleCount.setStatus("current")


class _Hm2L3RulePendingActions_Type(TruthValue):
    """Custom type hm2L3RulePendingActions based on TruthValue"""


_Hm2L3RulePendingActions_Object = MibScalar
hm2L3RulePendingActions = _Hm2L3RulePendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 3),
    _Hm2L3RulePendingActions_Type()
)
hm2L3RulePendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3RulePendingActions.setStatus("current")


class _Hm2L3CommitPendingActions_Type(HmActionValue):
    """Custom type hm2L3CommitPendingActions based on HmActionValue"""


_Hm2L3CommitPendingActions_Object = MibScalar
hm2L3CommitPendingActions = _Hm2L3CommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 1, 4),
    _Hm2L3CommitPendingActions_Type()
)
hm2L3CommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2L3CommitPendingActions.setStatus("current")
_Hm2L3RuleTables_ObjectIdentity = ObjectIdentity
hm2L3RuleTables = _Hm2L3RuleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2)
)
_Hm2L3RuleTable_Object = MibTable
hm2L3RuleTable = _Hm2L3RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2L3RuleTable.setStatus("current")
_Hm2L3RuleEntry_Object = MibTableRow
hm2L3RuleEntry = _Hm2L3RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1)
)
hm2L3RuleEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2L3RuleIndex"),
)
if mibBuilder.loadTexts:
    hm2L3RuleEntry.setStatus("current")


class _Hm2L3RuleIndex_Type(Integer32):
    """Custom type hm2L3RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Hm2L3RuleIndex_Type.__name__ = "Integer32"
_Hm2L3RuleIndex_Object = MibTableColumn
hm2L3RuleIndex = _Hm2L3RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 1),
    _Hm2L3RuleIndex_Type()
)
hm2L3RuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2L3RuleIndex.setStatus("current")


class _Hm2L3SourceAddress_Type(DisplayString):
    """Custom type hm2L3SourceAddress based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2L3SourceAddress_Type.__name__ = "DisplayString"
_Hm2L3SourceAddress_Object = MibTableColumn
hm2L3SourceAddress = _Hm2L3SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 2),
    _Hm2L3SourceAddress_Type()
)
hm2L3SourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3SourceAddress.setStatus("current")


class _Hm2L3SourcePort_Type(DisplayString):
    """Custom type hm2L3SourcePort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2L3SourcePort_Type.__name__ = "DisplayString"
_Hm2L3SourcePort_Object = MibTableColumn
hm2L3SourcePort = _Hm2L3SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 3),
    _Hm2L3SourcePort_Type()
)
hm2L3SourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3SourcePort.setStatus("current")


class _Hm2L3TargetAddress_Type(DisplayString):
    """Custom type hm2L3TargetAddress based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2L3TargetAddress_Type.__name__ = "DisplayString"
_Hm2L3TargetAddress_Object = MibTableColumn
hm2L3TargetAddress = _Hm2L3TargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 4),
    _Hm2L3TargetAddress_Type()
)
hm2L3TargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3TargetAddress.setStatus("current")


class _Hm2L3TargetPort_Type(DisplayString):
    """Custom type hm2L3TargetPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2L3TargetPort_Type.__name__ = "DisplayString"
_Hm2L3TargetPort_Object = MibTableColumn
hm2L3TargetPort = _Hm2L3TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 5),
    _Hm2L3TargetPort_Type()
)
hm2L3TargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3TargetPort.setStatus("current")


class _Hm2L3Proto_Type(Integer32):
    """Custom type hm2L3Proto based on Integer32"""
    defaultValue = 9

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ah", 7),
          ("any", 9),
          ("esp", 6),
          ("icmp", 1),
          ("icmpv6", 8),
          ("igmp", 2),
          ("ipip", 3),
          ("tcp", 4),
          ("udp", 5))
    )


_Hm2L3Proto_Type.__name__ = "Integer32"
_Hm2L3Proto_Object = MibTableColumn
hm2L3Proto = _Hm2L3Proto_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 6),
    _Hm2L3Proto_Type()
)
hm2L3Proto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3Proto.setStatus("current")


class _Hm2L3RuleParams_Type(DisplayString):
    """Custom type hm2L3RuleParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hm2L3RuleParams_Type.__name__ = "DisplayString"
_Hm2L3RuleParams_Object = MibTableColumn
hm2L3RuleParams = _Hm2L3RuleParams_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 7),
    _Hm2L3RuleParams_Type()
)
hm2L3RuleParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3RuleParams.setStatus("current")


class _Hm2L3Action_Type(Integer32):
    """Custom type hm2L3Action based on Integer32"""
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
        *(("accept", 1),
          ("drop", 2),
          ("enforce-modbus", 4),
          ("enforce-opc", 5),
          ("reject", 3))
    )


_Hm2L3Action_Type.__name__ = "Integer32"
_Hm2L3Action_Object = MibTableColumn
hm2L3Action = _Hm2L3Action_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 8),
    _Hm2L3Action_Type()
)
hm2L3Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3Action.setStatus("current")


class _Hm2L3Log_Type(TruthValue):
    """Custom type hm2L3Log based on TruthValue"""


_Hm2L3Log_Object = MibTableColumn
hm2L3Log = _Hm2L3Log_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 9),
    _Hm2L3Log_Type()
)
hm2L3Log.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3Log.setStatus("current")


class _Hm2L3Trap_Type(TruthValue):
    """Custom type hm2L3Trap based on TruthValue"""


_Hm2L3Trap_Object = MibTableColumn
hm2L3Trap = _Hm2L3Trap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 10),
    _Hm2L3Trap_Type()
)
hm2L3Trap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3Trap.setStatus("current")
_Hm2L3RowStatus_Type = RowStatus
_Hm2L3RowStatus_Object = MibTableColumn
hm2L3RowStatus = _Hm2L3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 11),
    _Hm2L3RowStatus_Type()
)
hm2L3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3RowStatus.setStatus("current")


class _Hm2L3Description_Type(DisplayString):
    """Custom type hm2L3Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2L3Description_Type.__name__ = "DisplayString"
_Hm2L3Description_Object = MibTableColumn
hm2L3Description = _Hm2L3Description_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 12),
    _Hm2L3Description_Type()
)
hm2L3Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3Description.setStatus("current")


class _Hm2DPIProfileIndex_Type(Integer32):
    """Custom type hm2DPIProfileIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hm2DPIProfileIndex_Type.__name__ = "Integer32"
_Hm2DPIProfileIndex_Object = MibTableColumn
hm2DPIProfileIndex = _Hm2DPIProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 1, 1, 13),
    _Hm2DPIProfileIndex_Type()
)
hm2DPIProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileIndex.setStatus("current")
_Hm2L3RuleIfMappingTable_Object = MibTable
hm2L3RuleIfMappingTable = _Hm2L3RuleIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hm2L3RuleIfMappingTable.setStatus("current")
_Hm2L3RuleIfMappingEntry_Object = MibTableRow
hm2L3RuleIfMappingEntry = _Hm2L3RuleIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1)
)
hm2L3RuleIfMappingEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2L3IfmInterface"),
    (0, "HM2-FW-MIB", "hm2L3IfmDirection"),
    (0, "HM2-FW-MIB", "hm2L3IfmRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2L3RuleIfMappingEntry.setStatus("current")


class _Hm2L3IfmRuleIndex_Type(Integer32):
    """Custom type hm2L3IfmRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Hm2L3IfmRuleIndex_Type.__name__ = "Integer32"
_Hm2L3IfmRuleIndex_Object = MibTableColumn
hm2L3IfmRuleIndex = _Hm2L3IfmRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 1),
    _Hm2L3IfmRuleIndex_Type()
)
hm2L3IfmRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2L3IfmRuleIndex.setStatus("current")


class _Hm2L3IfmDirection_Type(Integer32):
    """Custom type hm2L3IfmDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("egress", 2),
          ("ingress", 1))
    )


_Hm2L3IfmDirection_Type.__name__ = "Integer32"
_Hm2L3IfmDirection_Object = MibTableColumn
hm2L3IfmDirection = _Hm2L3IfmDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 2),
    _Hm2L3IfmDirection_Type()
)
hm2L3IfmDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2L3IfmDirection.setStatus("current")
_Hm2L3IfmPriority_Type = Unsigned32
_Hm2L3IfmPriority_Object = MibTableColumn
hm2L3IfmPriority = _Hm2L3IfmPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 3),
    _Hm2L3IfmPriority_Type()
)
hm2L3IfmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3IfmPriority.setStatus("current")
_Hm2L3IfmInterface_Type = InterfaceIndex
_Hm2L3IfmInterface_Object = MibTableColumn
hm2L3IfmInterface = _Hm2L3IfmInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 4),
    _Hm2L3IfmInterface_Type()
)
hm2L3IfmInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2L3IfmInterface.setStatus("current")
_Hm2L3IfmRowStatus_Type = RowStatus
_Hm2L3IfmRowStatus_Object = MibTableColumn
hm2L3IfmRowStatus = _Hm2L3IfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 2, 2, 1, 5),
    _Hm2L3IfmRowStatus_Type()
)
hm2L3IfmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2L3IfmRowStatus.setStatus("current")
_Hm2L3Stats_ObjectIdentity = ObjectIdentity
hm2L3Stats = _Hm2L3Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4)
)
_Hm2L3GeneralStats_ObjectIdentity = ObjectIdentity
hm2L3GeneralStats = _Hm2L3GeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1)
)
_Hm2L3StatsTotalPck_Type = Counter64
_Hm2L3StatsTotalPck_Object = MibScalar
hm2L3StatsTotalPck = _Hm2L3StatsTotalPck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 1),
    _Hm2L3StatsTotalPck_Type()
)
hm2L3StatsTotalPck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3StatsTotalPck.setStatus("current")
_Hm2L3StatsTotalPckSize_Type = Counter64
_Hm2L3StatsTotalPckSize_Object = MibScalar
hm2L3StatsTotalPckSize = _Hm2L3StatsTotalPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 2),
    _Hm2L3StatsTotalPckSize_Type()
)
hm2L3StatsTotalPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3StatsTotalPckSize.setStatus("current")
_Hm2L3StatsTotalPckDenDrop_Type = Counter64
_Hm2L3StatsTotalPckDenDrop_Object = MibScalar
hm2L3StatsTotalPckDenDrop = _Hm2L3StatsTotalPckDenDrop_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 3),
    _Hm2L3StatsTotalPckDenDrop_Type()
)
hm2L3StatsTotalPckDenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3StatsTotalPckDenDrop.setStatus("current")
_Hm2L3StatsTotalPckAccepted_Type = Counter64
_Hm2L3StatsTotalPckAccepted_Object = MibScalar
hm2L3StatsTotalPckAccepted = _Hm2L3StatsTotalPckAccepted_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 1, 4),
    _Hm2L3StatsTotalPckAccepted_Type()
)
hm2L3StatsTotalPckAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3StatsTotalPckAccepted.setStatus("current")
_Hm2L3StatsTables_ObjectIdentity = ObjectIdentity
hm2L3StatsTables = _Hm2L3StatsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2)
)
_Hm2L3StatsRuleTable_Object = MibTable
hm2L3StatsRuleTable = _Hm2L3StatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hm2L3StatsRuleTable.setStatus("current")
_Hm2L3StatsRuleEntry_Object = MibTableRow
hm2L3StatsRuleEntry = _Hm2L3StatsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1)
)
hm2L3StatsRuleEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2L3RuleIndex"),
)
if mibBuilder.loadTexts:
    hm2L3StatsRuleEntry.setStatus("current")
_Hm2L3StatsPacketCount_Type = Counter64
_Hm2L3StatsPacketCount_Object = MibTableColumn
hm2L3StatsPacketCount = _Hm2L3StatsPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1, 1),
    _Hm2L3StatsPacketCount_Type()
)
hm2L3StatsPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3StatsPacketCount.setStatus("current")
_Hm2L3StatsPacketSize_Type = Counter64
_Hm2L3StatsPacketSize_Object = MibTableColumn
hm2L3StatsPacketSize = _Hm2L3StatsPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1, 2),
    _Hm2L3StatsPacketSize_Type()
)
hm2L3StatsPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3StatsPacketSize.setStatus("current")
_Hm2L3StatsLastApplied_Type = HmTimeSeconds1970
_Hm2L3StatsLastApplied_Object = MibTableColumn
hm2L3StatsLastApplied = _Hm2L3StatsLastApplied_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 4, 2, 1, 1, 3),
    _Hm2L3StatsLastApplied_Type()
)
hm2L3StatsLastApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L3StatsLastApplied.setStatus("current")
_Hm2DPIProfileModbusObjects_ObjectIdentity = ObjectIdentity
hm2DPIProfileModbusObjects = _Hm2DPIProfileModbusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 11)
)


class _Hm2DPIProfileModbusPendingActions_Type(TruthValue):
    """Custom type hm2DPIProfileModbusPendingActions based on TruthValue"""


_Hm2DPIProfileModbusPendingActions_Object = MibScalar
hm2DPIProfileModbusPendingActions = _Hm2DPIProfileModbusPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 11, 1),
    _Hm2DPIProfileModbusPendingActions_Type()
)
hm2DPIProfileModbusPendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusPendingActions.setStatus("current")


class _Hm2DPIProfileModbusCommitPendingActions_Type(HmActionValue):
    """Custom type hm2DPIProfileModbusCommitPendingActions based on HmActionValue"""


_Hm2DPIProfileModbusCommitPendingActions_Object = MibScalar
hm2DPIProfileModbusCommitPendingActions = _Hm2DPIProfileModbusCommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 11, 2),
    _Hm2DPIProfileModbusCommitPendingActions_Type()
)
hm2DPIProfileModbusCommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusCommitPendingActions.setStatus("current")
_Hm2DPIProfileOpcObjects_ObjectIdentity = ObjectIdentity
hm2DPIProfileOpcObjects = _Hm2DPIProfileOpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 12)
)


class _Hm2DPIProfileOpcPendingActions_Type(TruthValue):
    """Custom type hm2DPIProfileOpcPendingActions based on TruthValue"""


_Hm2DPIProfileOpcPendingActions_Object = MibScalar
hm2DPIProfileOpcPendingActions = _Hm2DPIProfileOpcPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 12, 1),
    _Hm2DPIProfileOpcPendingActions_Type()
)
hm2DPIProfileOpcPendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcPendingActions.setStatus("current")


class _Hm2DPIProfileOpcCommitPendingActions_Type(HmActionValue):
    """Custom type hm2DPIProfileOpcCommitPendingActions based on HmActionValue"""


_Hm2DPIProfileOpcCommitPendingActions_Object = MibScalar
hm2DPIProfileOpcCommitPendingActions = _Hm2DPIProfileOpcCommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 12, 2),
    _Hm2DPIProfileOpcCommitPendingActions_Type()
)
hm2DPIProfileOpcCommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcCommitPendingActions.setStatus("current")
_Hm2DPIProfileTables_ObjectIdentity = ObjectIdentity
hm2DPIProfileTables = _Hm2DPIProfileTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21)
)
_Hm2DPIProfileModbusTable_Object = MibTable
hm2DPIProfileModbusTable = _Hm2DPIProfileModbusTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1)
)
if mibBuilder.loadTexts:
    hm2DPIProfileModbusTable.setStatus("current")
_Hm2DPIProfileModbusEntry_Object = MibTableRow
hm2DPIProfileModbusEntry = _Hm2DPIProfileModbusEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1)
)
hm2DPIProfileModbusEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2DPIProfileModbusIndex"),
)
if mibBuilder.loadTexts:
    hm2DPIProfileModbusEntry.setStatus("current")


class _Hm2DPIProfileModbusIndex_Type(Integer32):
    """Custom type hm2DPIProfileModbusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hm2DPIProfileModbusIndex_Type.__name__ = "Integer32"
_Hm2DPIProfileModbusIndex_Object = MibTableColumn
hm2DPIProfileModbusIndex = _Hm2DPIProfileModbusIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 1),
    _Hm2DPIProfileModbusIndex_Type()
)
hm2DPIProfileModbusIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusIndex.setStatus("current")


class _Hm2DPIProfileModbusDescription_Type(DisplayString):
    """Custom type hm2DPIProfileModbusDescription based on DisplayString"""
    defaultValue = OctetString("modbus")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2DPIProfileModbusDescription_Type.__name__ = "DisplayString"
_Hm2DPIProfileModbusDescription_Object = MibTableColumn
hm2DPIProfileModbusDescription = _Hm2DPIProfileModbusDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 2),
    _Hm2DPIProfileModbusDescription_Type()
)
hm2DPIProfileModbusDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusDescription.setStatus("current")


class _Hm2DPIProfileModbusFunctionType_Type(Integer32):
    """Custom type hm2DPIProfileModbusFunctionType based on Integer32"""
    defaultValue = 1

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
        *(("advanced", 5),
          ("all", 4),
          ("programming", 3),
          ("readonly", 1),
          ("readwrite", 2))
    )


_Hm2DPIProfileModbusFunctionType_Type.__name__ = "Integer32"
_Hm2DPIProfileModbusFunctionType_Object = MibTableColumn
hm2DPIProfileModbusFunctionType = _Hm2DPIProfileModbusFunctionType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 3),
    _Hm2DPIProfileModbusFunctionType_Type()
)
hm2DPIProfileModbusFunctionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusFunctionType.setStatus("current")


class _Hm2DPIProfileModbusFunctionCodeList_Type(DisplayString):
    """Custom type hm2DPIProfileModbusFunctionCodeList based on DisplayString"""
    defaultValue = OctetString("1,2,3,4,7,11,12,17,20,24")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1400),
    )


_Hm2DPIProfileModbusFunctionCodeList_Type.__name__ = "DisplayString"
_Hm2DPIProfileModbusFunctionCodeList_Object = MibTableColumn
hm2DPIProfileModbusFunctionCodeList = _Hm2DPIProfileModbusFunctionCodeList_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 4),
    _Hm2DPIProfileModbusFunctionCodeList_Type()
)
hm2DPIProfileModbusFunctionCodeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusFunctionCodeList.setStatus("current")


class _Hm2DPIProfileModbusUnitIdentifierList_Type(DisplayString):
    """Custom type hm2DPIProfileModbusUnitIdentifierList based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1400),
    )


_Hm2DPIProfileModbusUnitIdentifierList_Type.__name__ = "DisplayString"
_Hm2DPIProfileModbusUnitIdentifierList_Object = MibTableColumn
hm2DPIProfileModbusUnitIdentifierList = _Hm2DPIProfileModbusUnitIdentifierList_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 5),
    _Hm2DPIProfileModbusUnitIdentifierList_Type()
)
hm2DPIProfileModbusUnitIdentifierList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusUnitIdentifierList.setStatus("current")


class _Hm2DPIProfileModbusSanityCheck_Type(TruthValue):
    """Custom type hm2DPIProfileModbusSanityCheck based on TruthValue"""


_Hm2DPIProfileModbusSanityCheck_Object = MibTableColumn
hm2DPIProfileModbusSanityCheck = _Hm2DPIProfileModbusSanityCheck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 6),
    _Hm2DPIProfileModbusSanityCheck_Type()
)
hm2DPIProfileModbusSanityCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusSanityCheck.setStatus("current")


class _Hm2DPIProfileModbusException_Type(TruthValue):
    """Custom type hm2DPIProfileModbusException based on TruthValue"""


_Hm2DPIProfileModbusException_Object = MibTableColumn
hm2DPIProfileModbusException = _Hm2DPIProfileModbusException_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 7),
    _Hm2DPIProfileModbusException_Type()
)
hm2DPIProfileModbusException.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusException.setStatus("current")


class _Hm2DPIProfileModbusReset_Type(TruthValue):
    """Custom type hm2DPIProfileModbusReset based on TruthValue"""


_Hm2DPIProfileModbusReset_Object = MibTableColumn
hm2DPIProfileModbusReset = _Hm2DPIProfileModbusReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 8),
    _Hm2DPIProfileModbusReset_Type()
)
hm2DPIProfileModbusReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusReset.setStatus("current")
_Hm2DPIProfileModbusRowStatus_Type = RowStatus
_Hm2DPIProfileModbusRowStatus_Object = MibTableColumn
hm2DPIProfileModbusRowStatus = _Hm2DPIProfileModbusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 1, 1, 9),
    _Hm2DPIProfileModbusRowStatus_Type()
)
hm2DPIProfileModbusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileModbusRowStatus.setStatus("current")
_Hm2DPIProfileOpcTable_Object = MibTable
hm2DPIProfileOpcTable = _Hm2DPIProfileOpcTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2)
)
if mibBuilder.loadTexts:
    hm2DPIProfileOpcTable.setStatus("current")
_Hm2DPIProfileOpcEntry_Object = MibTableRow
hm2DPIProfileOpcEntry = _Hm2DPIProfileOpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1)
)
hm2DPIProfileOpcEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2DPIProfileOpcIndex"),
)
if mibBuilder.loadTexts:
    hm2DPIProfileOpcEntry.setStatus("current")


class _Hm2DPIProfileOpcIndex_Type(Integer32):
    """Custom type hm2DPIProfileOpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hm2DPIProfileOpcIndex_Type.__name__ = "Integer32"
_Hm2DPIProfileOpcIndex_Object = MibTableColumn
hm2DPIProfileOpcIndex = _Hm2DPIProfileOpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 1),
    _Hm2DPIProfileOpcIndex_Type()
)
hm2DPIProfileOpcIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcIndex.setStatus("current")


class _Hm2DPIProfileOpcDescription_Type(DisplayString):
    """Custom type hm2DPIProfileOpcDescription based on DisplayString"""
    defaultValue = OctetString("opc")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2DPIProfileOpcDescription_Type.__name__ = "DisplayString"
_Hm2DPIProfileOpcDescription_Object = MibTableColumn
hm2DPIProfileOpcDescription = _Hm2DPIProfileOpcDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 2),
    _Hm2DPIProfileOpcDescription_Type()
)
hm2DPIProfileOpcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcDescription.setStatus("current")


class _Hm2DPIProfileOpcSanityCheck_Type(TruthValue):
    """Custom type hm2DPIProfileOpcSanityCheck based on TruthValue"""


_Hm2DPIProfileOpcSanityCheck_Object = MibTableColumn
hm2DPIProfileOpcSanityCheck = _Hm2DPIProfileOpcSanityCheck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 3),
    _Hm2DPIProfileOpcSanityCheck_Type()
)
hm2DPIProfileOpcSanityCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcSanityCheck.setStatus("current")


class _Hm2DPIProfileOpcFragmentCheck_Type(TruthValue):
    """Custom type hm2DPIProfileOpcFragmentCheck based on TruthValue"""


_Hm2DPIProfileOpcFragmentCheck_Object = MibTableColumn
hm2DPIProfileOpcFragmentCheck = _Hm2DPIProfileOpcFragmentCheck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 4),
    _Hm2DPIProfileOpcFragmentCheck_Type()
)
hm2DPIProfileOpcFragmentCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcFragmentCheck.setStatus("current")


class _Hm2DPIProfileOpcTimeoutConnect_Type(Unsigned32):
    """Custom type hm2DPIProfileOpcTimeoutConnect based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Hm2DPIProfileOpcTimeoutConnect_Type.__name__ = "Unsigned32"
_Hm2DPIProfileOpcTimeoutConnect_Object = MibTableColumn
hm2DPIProfileOpcTimeoutConnect = _Hm2DPIProfileOpcTimeoutConnect_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 5),
    _Hm2DPIProfileOpcTimeoutConnect_Type()
)
hm2DPIProfileOpcTimeoutConnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcTimeoutConnect.setStatus("current")
_Hm2DPIProfileOpcRowStatus_Type = RowStatus
_Hm2DPIProfileOpcRowStatus_Object = MibTableColumn
hm2DPIProfileOpcRowStatus = _Hm2DPIProfileOpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 3, 21, 2, 1, 6),
    _Hm2DPIProfileOpcRowStatus_Type()
)
hm2DPIProfileOpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DPIProfileOpcRowStatus.setStatus("current")
_Hm2FwLearningMode_ObjectIdentity = ObjectIdentity
hm2FwLearningMode = _Hm2FwLearningMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4)
)
_Hm2FLMObjects_ObjectIdentity = ObjectIdentity
hm2FLMObjects = _Hm2FLMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1)
)


class _Hm2FLMAdminState_Type(HmEnabledStatus):
    """Custom type hm2FLMAdminState based on HmEnabledStatus"""


_Hm2FLMAdminState_Object = MibScalar
hm2FLMAdminState = _Hm2FLMAdminState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 1),
    _Hm2FLMAdminState_Type()
)
hm2FLMAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FLMAdminState.setStatus("current")


class _Hm2FLMAction_Type(Integer32):
    """Custom type hm2FLMAction based on Integer32"""
    defaultValue = 1

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
        *(("clear", 5),
          ("continue", 4),
          ("none", 1),
          ("start", 2),
          ("stop", 3))
    )


_Hm2FLMAction_Type.__name__ = "Integer32"
_Hm2FLMAction_Object = MibScalar
hm2FLMAction = _Hm2FLMAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 2),
    _Hm2FLMAction_Type()
)
hm2FLMAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FLMAction.setStatus("current")


class _Hm2FLMAppState_Type(Integer32):
    """Custom type hm2FLMAppState based on Integer32"""
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
        *(("learning", 4),
          ("off", 1),
          ("pending", 5),
          ("stopped-data-notpresent", 2),
          ("stopped-data-present", 3))
    )


_Hm2FLMAppState_Type.__name__ = "Integer32"
_Hm2FLMAppState_Object = MibScalar
hm2FLMAppState = _Hm2FLMAppState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 3),
    _Hm2FLMAppState_Type()
)
hm2FLMAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FLMAppState.setStatus("current")


class _Hm2FLMAppInfoEnum_Type(Integer32):
    """Custom type hm2FLMAppInfoEnum based on Integer32"""
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
        *(("connection-drop", 5),
          ("low-memory", 3),
          ("none", 1),
          ("normal", 2),
          ("out-of-memory", 4))
    )


_Hm2FLMAppInfoEnum_Type.__name__ = "Integer32"
_Hm2FLMAppInfoEnum_Object = MibScalar
hm2FLMAppInfoEnum = _Hm2FLMAppInfoEnum_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 4),
    _Hm2FLMAppInfoEnum_Type()
)
hm2FLMAppInfoEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FLMAppInfoEnum.setStatus("current")


class _Hm2FLMAppInfoString_Type(SnmpAdminString):
    """Custom type hm2FLMAppInfoString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hm2FLMAppInfoString_Type.__name__ = "SnmpAdminString"
_Hm2FLMAppInfoString_Object = MibScalar
hm2FLMAppInfoString = _Hm2FLMAppInfoString_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 5),
    _Hm2FLMAppInfoString_Type()
)
hm2FLMAppInfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FLMAppInfoString.setStatus("current")
_Hm2FLML3Entries_Type = Unsigned32
_Hm2FLML3Entries_Object = MibScalar
hm2FLML3Entries = _Hm2FLML3Entries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 6),
    _Hm2FLML3Entries_Type()
)
hm2FLML3Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FLML3Entries.setStatus("current")
_Hm2FLMFreeMem_Type = Unsigned32
_Hm2FLMFreeMem_Object = MibScalar
hm2FLMFreeMem = _Hm2FLMFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 7),
    _Hm2FLMFreeMem_Type()
)
hm2FLMFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FLMFreeMem.setStatus("current")
_Hm2FLMMaxEntries_Type = Unsigned32
_Hm2FLMMaxEntries_Object = MibScalar
hm2FLMMaxEntries = _Hm2FLMMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 1, 8),
    _Hm2FLMMaxEntries_Type()
)
hm2FLMMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2FLMMaxEntries.setStatus("current")
_Hm2FLMTables_ObjectIdentity = ObjectIdentity
hm2FLMTables = _Hm2FLMTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2)
)
_Hm2FLMInterfaceTable_Object = MibTable
hm2FLMInterfaceTable = _Hm2FLMInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hm2FLMInterfaceTable.setStatus("current")
_Hm2FLMInterfaceEntry_Object = MibTableRow
hm2FLMInterfaceEntry = _Hm2FLMInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1, 1)
)
hm2FLMInterfaceEntry.setIndexNames(
    (0, "HM2-FW-MIB", "hm2FLMInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hm2FLMInterfaceEntry.setStatus("current")
_Hm2FLMInterfaceIndex_Type = InterfaceIndex
_Hm2FLMInterfaceIndex_Object = MibTableColumn
hm2FLMInterfaceIndex = _Hm2FLMInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1, 1, 1),
    _Hm2FLMInterfaceIndex_Type()
)
hm2FLMInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2FLMInterfaceIndex.setStatus("current")
_Hm2FLMInterfaceRowStatus_Type = RowStatus
_Hm2FLMInterfaceRowStatus_Object = MibTableColumn
hm2FLMInterfaceRowStatus = _Hm2FLMInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 1, 4, 2, 1, 1, 2),
    _Hm2FLMInterfaceRowStatus_Type()
)
hm2FLMInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2FLMInterfaceRowStatus.setStatus("current")
_Hm2FwConformance_ObjectIdentity = ObjectIdentity
hm2FwConformance = _Hm2FwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 2)
)
_Hm2FwCompliances_ObjectIdentity = ObjectIdentity
hm2FwCompliances = _Hm2FwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 1)
)
_Hm2FwGroups_ObjectIdentity = ObjectIdentity
hm2FwGroups = _Hm2FwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 2)
)

# Managed Objects groups

hm2FwGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 2, 1)
)
hm2FwGeneralGroup.setObjects(
      *(("HM2-FW-MIB", "hm2DynFwMaxRules"),
        ("HM2-FW-MIB", "hm2L3MaxRules"),
        ("HM2-FW-MIB", "hm2ResetStatistics"),
        ("HM2-FW-MIB", "hm2FlushTables"),
        ("HM2-FW-MIB", "hm2DefaultPolicy"),
        ("HM2-FW-MIB", "hm2DynFwRuleCount"),
        ("HM2-FW-MIB", "hm2DynFwIfMappingRuleCount"),
        ("HM2-FW-MIB", "hm2DynFwRulePendingActions"),
        ("HM2-FW-MIB", "hm2DynFwCommitPendingActions"),
        ("HM2-FW-MIB", "hm2DynFwRuleIndex"),
        ("HM2-FW-MIB", "hm2DynFwSourceAddress"),
        ("HM2-FW-MIB", "hm2DynFwSourcePort"),
        ("HM2-FW-MIB", "hm2DynFwTargetAddress"),
        ("HM2-FW-MIB", "hm2DynFwTargetPort"),
        ("HM2-FW-MIB", "hm2DynFwProto"),
        ("HM2-FW-MIB", "hm2DynFwRuleParams"),
        ("HM2-FW-MIB", "hm2DynFwAction"),
        ("HM2-FW-MIB", "hm2DynFwLog"),
        ("HM2-FW-MIB", "hm2DynFwTrap"),
        ("HM2-FW-MIB", "hm2DynFwDescription"),
        ("HM2-FW-MIB", "hm2DynFwRowStatus"),
        ("HM2-FW-MIB", "hm2DynFwIfmPriority"),
        ("HM2-FW-MIB", "hm2DynFwIfmRowStatus"),
        ("HM2-FW-MIB", "hm2DynFwStatsPacketCount"),
        ("HM2-FW-MIB", "hm2DynFwStatsPacketSize"),
        ("HM2-FW-MIB", "hm2DynFwStatsLastApplied"),
        ("HM2-FW-MIB", "hm2DynFwStatsTtPck"),
        ("HM2-FW-MIB", "hm2DynFwStatsTtPckSize"),
        ("HM2-FW-MIB", "hm2DynFwStatsTtPckDenDrop"),
        ("HM2-FW-MIB", "hm2DynFwStatsTtPckAccepted"),
        ("HM2-FW-MIB", "hm2L3RuleCount"),
        ("HM2-FW-MIB", "hm2L3IfMappingRuleCount"),
        ("HM2-FW-MIB", "hm2L3RulePendingActions"),
        ("HM2-FW-MIB", "hm2L3CommitPendingActions"),
        ("HM2-FW-MIB", "hm2L3RuleIndex"),
        ("HM2-FW-MIB", "hm2L3SourceAddress"),
        ("HM2-FW-MIB", "hm2L3SourcePort"),
        ("HM2-FW-MIB", "hm2L3TargetAddress"),
        ("HM2-FW-MIB", "hm2L3TargetPort"),
        ("HM2-FW-MIB", "hm2L3Proto"),
        ("HM2-FW-MIB", "hm2L3Action"),
        ("HM2-FW-MIB", "hm2L3RuleParams"),
        ("HM2-FW-MIB", "hm2L3Log"),
        ("HM2-FW-MIB", "hm2L3Trap"),
        ("HM2-FW-MIB", "hm2L3Description"),
        ("HM2-FW-MIB", "hm2L3RowStatus"),
        ("HM2-FW-MIB", "hm2DPIProfileIndex"),
        ("HM2-FW-MIB", "hm2L3IfmPriority"),
        ("HM2-FW-MIB", "hm2L3IfmRowStatus"),
        ("HM2-FW-MIB", "hm2L3StatsPacketCount"),
        ("HM2-FW-MIB", "hm2L3StatsPacketSize"),
        ("HM2-FW-MIB", "hm2L3StatsLastApplied"),
        ("HM2-FW-MIB", "hm2L3StatsTotalPck"),
        ("HM2-FW-MIB", "hm2L3StatsTotalPckSize"),
        ("HM2-FW-MIB", "hm2L3StatsTotalPckDenDrop"),
        ("HM2-FW-MIB", "hm2L3StatsTotalPckAccepted"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusPendingActions"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusCommitPendingActions"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusIndex"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusDescription"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusFunctionType"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusFunctionCodeList"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusUnitIdentifierList"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusSanityCheck"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusException"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusReset"),
        ("HM2-FW-MIB", "hm2DPIProfileModbusRowStatus"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcPendingActions"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcCommitPendingActions"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcIndex"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcDescription"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcSanityCheck"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcFragmentCheck"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcTimeoutConnect"),
        ("HM2-FW-MIB", "hm2DPIProfileOpcRowStatus"))
)
if mibBuilder.loadTexts:
    hm2FwGeneralGroup.setStatus("current")


# Notification objects

hm2DynFwRuleAppliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 1)
)
hm2DynFwRuleAppliedTrap.setObjects(
    ("HM2-FW-MIB", "hm2DynFwRuleIndex")
)
if mibBuilder.loadTexts:
    hm2DynFwRuleAppliedTrap.setStatus(
        "current"
    )

hm2DynFwRuleAppliedAndLoggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 2)
)
hm2DynFwRuleAppliedAndLoggedTrap.setObjects(
    ("HM2-FW-MIB", "hm2DynFwRuleIndex")
)
if mibBuilder.loadTexts:
    hm2DynFwRuleAppliedAndLoggedTrap.setStatus(
        "current"
    )

hm2L3RuleAppliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 3)
)
hm2L3RuleAppliedTrap.setObjects(
    ("HM2-FW-MIB", "hm2L3RuleIndex")
)
if mibBuilder.loadTexts:
    hm2L3RuleAppliedTrap.setStatus(
        "current"
    )

hm2L3RuleAppliedAndLoggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 0, 4)
)
hm2L3RuleAppliedAndLoggedTrap.setObjects(
    ("HM2-FW-MIB", "hm2L3RuleIndex")
)
if mibBuilder.loadTexts:
    hm2L3RuleAppliedAndLoggedTrap.setStatus(
        "current"
    )


# Notifications groups

hm2FwNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 2, 2)
)
hm2FwNotificationsGroup.setObjects(
      *(("HM2-FW-MIB", "hm2DynFwRuleAppliedTrap"),
        ("HM2-FW-MIB", "hm2DynFwRuleAppliedAndLoggedTrap"),
        ("HM2-FW-MIB", "hm2L3RuleAppliedTrap"),
        ("HM2-FW-MIB", "hm2L3RuleAppliedAndLoggedTrap"))
)
if mibBuilder.loadTexts:
    hm2FwNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hm2FwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 11, 79, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hm2FwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-FW-MIB",
    **{"hm2FwMib": hm2FwMib,
       "hm2FwNotifications": hm2FwNotifications,
       "hm2DynFwRuleAppliedTrap": hm2DynFwRuleAppliedTrap,
       "hm2DynFwRuleAppliedAndLoggedTrap": hm2DynFwRuleAppliedAndLoggedTrap,
       "hm2L3RuleAppliedTrap": hm2L3RuleAppliedTrap,
       "hm2L3RuleAppliedAndLoggedTrap": hm2L3RuleAppliedAndLoggedTrap,
       "hm2FwObjects": hm2FwObjects,
       "hm2FwGeneralSettings": hm2FwGeneralSettings,
       "hm2DynFwMaxRules": hm2DynFwMaxRules,
       "hm2L3MaxRules": hm2L3MaxRules,
       "hm2ResetStatistics": hm2ResetStatistics,
       "hm2FlushTables": hm2FlushTables,
       "hm2DefaultPolicy": hm2DefaultPolicy,
       "hm2ConnTrackValidateCheckSum": hm2ConnTrackValidateCheckSum,
       "hm2DynFw": hm2DynFw,
       "hm2DynFwRuleObjects": hm2DynFwRuleObjects,
       "hm2DynFwRuleCount": hm2DynFwRuleCount,
       "hm2DynFwIfMappingRuleCount": hm2DynFwIfMappingRuleCount,
       "hm2DynFwRulePendingActions": hm2DynFwRulePendingActions,
       "hm2DynFwCommitPendingActions": hm2DynFwCommitPendingActions,
       "hm2DynFwRuleTables": hm2DynFwRuleTables,
       "hm2DynFwRuleTable": hm2DynFwRuleTable,
       "hm2DynFwRuleEntry": hm2DynFwRuleEntry,
       "hm2DynFwRuleIndex": hm2DynFwRuleIndex,
       "hm2DynFwSourceAddress": hm2DynFwSourceAddress,
       "hm2DynFwSourcePort": hm2DynFwSourcePort,
       "hm2DynFwTargetAddress": hm2DynFwTargetAddress,
       "hm2DynFwTargetPort": hm2DynFwTargetPort,
       "hm2DynFwProto": hm2DynFwProto,
       "hm2DynFwRuleParams": hm2DynFwRuleParams,
       "hm2DynFwAction": hm2DynFwAction,
       "hm2DynFwLog": hm2DynFwLog,
       "hm2DynFwTrap": hm2DynFwTrap,
       "hm2DynFwRowStatus": hm2DynFwRowStatus,
       "hm2DynFwDescription": hm2DynFwDescription,
       "hm2DynFwRuleIfMappingTable": hm2DynFwRuleIfMappingTable,
       "hm2DynFwRuleIfMappingEntry": hm2DynFwRuleIfMappingEntry,
       "hm2DynFwIfmRuleIndex": hm2DynFwIfmRuleIndex,
       "hm2DynFwIfmDirection": hm2DynFwIfmDirection,
       "hm2DynFwIfmPriority": hm2DynFwIfmPriority,
       "hm2DynFwIfmInterface": hm2DynFwIfmInterface,
       "hm2DynFwIfmRowStatus": hm2DynFwIfmRowStatus,
       "hm2DynFwStats": hm2DynFwStats,
       "hm2DynFwGeneralStats": hm2DynFwGeneralStats,
       "hm2DynFwStatsTtPck": hm2DynFwStatsTtPck,
       "hm2DynFwStatsTtPckSize": hm2DynFwStatsTtPckSize,
       "hm2DynFwStatsTtPckDenDrop": hm2DynFwStatsTtPckDenDrop,
       "hm2DynFwStatsTtPckAccepted": hm2DynFwStatsTtPckAccepted,
       "hm2DynFwStatsTables": hm2DynFwStatsTables,
       "hm2DynFwStatsRuleTable": hm2DynFwStatsRuleTable,
       "hm2DynFwStatsRuleEntry": hm2DynFwStatsRuleEntry,
       "hm2DynFwStatsPacketCount": hm2DynFwStatsPacketCount,
       "hm2DynFwStatsPacketSize": hm2DynFwStatsPacketSize,
       "hm2DynFwStatsLastApplied": hm2DynFwStatsLastApplied,
       "hm2L3Fw": hm2L3Fw,
       "hm2L3RuleObjects": hm2L3RuleObjects,
       "hm2L3RuleCount": hm2L3RuleCount,
       "hm2L3IfMappingRuleCount": hm2L3IfMappingRuleCount,
       "hm2L3RulePendingActions": hm2L3RulePendingActions,
       "hm2L3CommitPendingActions": hm2L3CommitPendingActions,
       "hm2L3RuleTables": hm2L3RuleTables,
       "hm2L3RuleTable": hm2L3RuleTable,
       "hm2L3RuleEntry": hm2L3RuleEntry,
       "hm2L3RuleIndex": hm2L3RuleIndex,
       "hm2L3SourceAddress": hm2L3SourceAddress,
       "hm2L3SourcePort": hm2L3SourcePort,
       "hm2L3TargetAddress": hm2L3TargetAddress,
       "hm2L3TargetPort": hm2L3TargetPort,
       "hm2L3Proto": hm2L3Proto,
       "hm2L3RuleParams": hm2L3RuleParams,
       "hm2L3Action": hm2L3Action,
       "hm2L3Log": hm2L3Log,
       "hm2L3Trap": hm2L3Trap,
       "hm2L3RowStatus": hm2L3RowStatus,
       "hm2L3Description": hm2L3Description,
       "hm2DPIProfileIndex": hm2DPIProfileIndex,
       "hm2L3RuleIfMappingTable": hm2L3RuleIfMappingTable,
       "hm2L3RuleIfMappingEntry": hm2L3RuleIfMappingEntry,
       "hm2L3IfmRuleIndex": hm2L3IfmRuleIndex,
       "hm2L3IfmDirection": hm2L3IfmDirection,
       "hm2L3IfmPriority": hm2L3IfmPriority,
       "hm2L3IfmInterface": hm2L3IfmInterface,
       "hm2L3IfmRowStatus": hm2L3IfmRowStatus,
       "hm2L3Stats": hm2L3Stats,
       "hm2L3GeneralStats": hm2L3GeneralStats,
       "hm2L3StatsTotalPck": hm2L3StatsTotalPck,
       "hm2L3StatsTotalPckSize": hm2L3StatsTotalPckSize,
       "hm2L3StatsTotalPckDenDrop": hm2L3StatsTotalPckDenDrop,
       "hm2L3StatsTotalPckAccepted": hm2L3StatsTotalPckAccepted,
       "hm2L3StatsTables": hm2L3StatsTables,
       "hm2L3StatsRuleTable": hm2L3StatsRuleTable,
       "hm2L3StatsRuleEntry": hm2L3StatsRuleEntry,
       "hm2L3StatsPacketCount": hm2L3StatsPacketCount,
       "hm2L3StatsPacketSize": hm2L3StatsPacketSize,
       "hm2L3StatsLastApplied": hm2L3StatsLastApplied,
       "hm2DPIProfileModbusObjects": hm2DPIProfileModbusObjects,
       "hm2DPIProfileModbusPendingActions": hm2DPIProfileModbusPendingActions,
       "hm2DPIProfileModbusCommitPendingActions": hm2DPIProfileModbusCommitPendingActions,
       "hm2DPIProfileOpcObjects": hm2DPIProfileOpcObjects,
       "hm2DPIProfileOpcPendingActions": hm2DPIProfileOpcPendingActions,
       "hm2DPIProfileOpcCommitPendingActions": hm2DPIProfileOpcCommitPendingActions,
       "hm2DPIProfileTables": hm2DPIProfileTables,
       "hm2DPIProfileModbusTable": hm2DPIProfileModbusTable,
       "hm2DPIProfileModbusEntry": hm2DPIProfileModbusEntry,
       "hm2DPIProfileModbusIndex": hm2DPIProfileModbusIndex,
       "hm2DPIProfileModbusDescription": hm2DPIProfileModbusDescription,
       "hm2DPIProfileModbusFunctionType": hm2DPIProfileModbusFunctionType,
       "hm2DPIProfileModbusFunctionCodeList": hm2DPIProfileModbusFunctionCodeList,
       "hm2DPIProfileModbusUnitIdentifierList": hm2DPIProfileModbusUnitIdentifierList,
       "hm2DPIProfileModbusSanityCheck": hm2DPIProfileModbusSanityCheck,
       "hm2DPIProfileModbusException": hm2DPIProfileModbusException,
       "hm2DPIProfileModbusReset": hm2DPIProfileModbusReset,
       "hm2DPIProfileModbusRowStatus": hm2DPIProfileModbusRowStatus,
       "hm2DPIProfileOpcTable": hm2DPIProfileOpcTable,
       "hm2DPIProfileOpcEntry": hm2DPIProfileOpcEntry,
       "hm2DPIProfileOpcIndex": hm2DPIProfileOpcIndex,
       "hm2DPIProfileOpcDescription": hm2DPIProfileOpcDescription,
       "hm2DPIProfileOpcSanityCheck": hm2DPIProfileOpcSanityCheck,
       "hm2DPIProfileOpcFragmentCheck": hm2DPIProfileOpcFragmentCheck,
       "hm2DPIProfileOpcTimeoutConnect": hm2DPIProfileOpcTimeoutConnect,
       "hm2DPIProfileOpcRowStatus": hm2DPIProfileOpcRowStatus,
       "hm2FwLearningMode": hm2FwLearningMode,
       "hm2FLMObjects": hm2FLMObjects,
       "hm2FLMAdminState": hm2FLMAdminState,
       "hm2FLMAction": hm2FLMAction,
       "hm2FLMAppState": hm2FLMAppState,
       "hm2FLMAppInfoEnum": hm2FLMAppInfoEnum,
       "hm2FLMAppInfoString": hm2FLMAppInfoString,
       "hm2FLML3Entries": hm2FLML3Entries,
       "hm2FLMFreeMem": hm2FLMFreeMem,
       "hm2FLMMaxEntries": hm2FLMMaxEntries,
       "hm2FLMTables": hm2FLMTables,
       "hm2FLMInterfaceTable": hm2FLMInterfaceTable,
       "hm2FLMInterfaceEntry": hm2FLMInterfaceEntry,
       "hm2FLMInterfaceIndex": hm2FLMInterfaceIndex,
       "hm2FLMInterfaceRowStatus": hm2FLMInterfaceRowStatus,
       "hm2FwConformance": hm2FwConformance,
       "hm2FwCompliances": hm2FwCompliances,
       "hm2FwCompliance": hm2FwCompliance,
       "hm2FwGroups": hm2FwGroups,
       "hm2FwGeneralGroup": hm2FwGeneralGroup,
       "hm2FwNotificationsGroup": hm2FwNotificationsGroup}
)
