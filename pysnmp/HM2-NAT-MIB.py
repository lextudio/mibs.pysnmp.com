# SNMP MIB module (HM2-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:08 2024
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
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmActionValue",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2NatMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80)
)
hm2NatMib.setRevisions(
        ("2011-11-30 00:00",
         "2011-10-24 00:00",
         "2011-09-13 00:00",
         "2011-07-01 00:00",
         "2011-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2NatNotifications_ObjectIdentity = ObjectIdentity
hm2NatNotifications = _Hm2NatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0)
)
_Hm2NatObjects_ObjectIdentity = ObjectIdentity
hm2NatObjects = _Hm2NatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1)
)
_Hm2NatGeneralSettings_ObjectIdentity = ObjectIdentity
hm2NatGeneralSettings = _Hm2NatGeneralSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 1)
)
_Hm2DnatMaxRules_Type = Integer32
_Hm2DnatMaxRules_Object = MibScalar
hm2DnatMaxRules = _Hm2DnatMaxRules_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 1, 2),
    _Hm2DnatMaxRules_Type()
)
hm2DnatMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatMaxRules.setStatus("current")
_Hm2OneToOneNatMaxRules_Type = Integer32
_Hm2OneToOneNatMaxRules_Object = MibScalar
hm2OneToOneNatMaxRules = _Hm2OneToOneNatMaxRules_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 1, 3),
    _Hm2OneToOneNatMaxRules_Type()
)
hm2OneToOneNatMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2OneToOneNatMaxRules.setStatus("current")
_Hm2MasqMaxRules_Type = Integer32
_Hm2MasqMaxRules_Object = MibScalar
hm2MasqMaxRules = _Hm2MasqMaxRules_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 1, 4),
    _Hm2MasqMaxRules_Type()
)
hm2MasqMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqMaxRules.setStatus("current")
_Hm2DoubleNatMaxRules_Type = Integer32
_Hm2DoubleNatMaxRules_Object = MibScalar
hm2DoubleNatMaxRules = _Hm2DoubleNatMaxRules_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 1, 5),
    _Hm2DoubleNatMaxRules_Type()
)
hm2DoubleNatMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DoubleNatMaxRules.setStatus("current")
_Hm2NatResetStatistics_Type = HmActionValue
_Hm2NatResetStatistics_Object = MibScalar
hm2NatResetStatistics = _Hm2NatResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 1, 6),
    _Hm2NatResetStatistics_Type()
)
hm2NatResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2NatResetStatistics.setStatus("current")
_Hm2Dnat_ObjectIdentity = ObjectIdentity
hm2Dnat = _Hm2Dnat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2)
)
_Hm2DnatRules_ObjectIdentity = ObjectIdentity
hm2DnatRules = _Hm2DnatRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1)
)
_Hm2DnatRulesObjects_ObjectIdentity = ObjectIdentity
hm2DnatRulesObjects = _Hm2DnatRulesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 1)
)
_Hm2DnatRuleCount_Type = Integer32
_Hm2DnatRuleCount_Object = MibScalar
hm2DnatRuleCount = _Hm2DnatRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 1, 1),
    _Hm2DnatRuleCount_Type()
)
hm2DnatRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatRuleCount.setStatus("current")
_Hm2DnatIfMappingRuleCount_Type = Integer32
_Hm2DnatIfMappingRuleCount_Object = MibScalar
hm2DnatIfMappingRuleCount = _Hm2DnatIfMappingRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 1, 2),
    _Hm2DnatIfMappingRuleCount_Type()
)
hm2DnatIfMappingRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatIfMappingRuleCount.setStatus("current")


class _Hm2DnatRulePendingActions_Type(TruthValue):
    """Custom type hm2DnatRulePendingActions based on TruthValue"""


_Hm2DnatRulePendingActions_Object = MibScalar
hm2DnatRulePendingActions = _Hm2DnatRulePendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 1, 3),
    _Hm2DnatRulePendingActions_Type()
)
hm2DnatRulePendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatRulePendingActions.setStatus("current")


class _Hm2DnatCommitPendingActions_Type(HmActionValue):
    """Custom type hm2DnatCommitPendingActions based on HmActionValue"""


_Hm2DnatCommitPendingActions_Object = MibScalar
hm2DnatCommitPendingActions = _Hm2DnatCommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 1, 4),
    _Hm2DnatCommitPendingActions_Type()
)
hm2DnatCommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DnatCommitPendingActions.setStatus("current")
_Hm2DnatRulesTables_ObjectIdentity = ObjectIdentity
hm2DnatRulesTables = _Hm2DnatRulesTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2)
)
_Hm2DnatRuleTable_Object = MibTable
hm2DnatRuleTable = _Hm2DnatRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DnatRuleTable.setStatus("current")
_Hm2DnatRuleEntry_Object = MibTableRow
hm2DnatRuleEntry = _Hm2DnatRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1)
)
hm2DnatRuleEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2DnatRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DnatRuleEntry.setStatus("current")


class _Hm2DnatRuleIndex_Type(Integer32):
    """Custom type hm2DnatRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2DnatRuleIndex_Type.__name__ = "Integer32"
_Hm2DnatRuleIndex_Object = MibTableColumn
hm2DnatRuleIndex = _Hm2DnatRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 1),
    _Hm2DnatRuleIndex_Type()
)
hm2DnatRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2DnatRuleIndex.setStatus("current")


class _Hm2DnatSourceAddress_Type(DisplayString):
    """Custom type hm2DnatSourceAddress based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DnatSourceAddress_Type.__name__ = "DisplayString"
_Hm2DnatSourceAddress_Object = MibTableColumn
hm2DnatSourceAddress = _Hm2DnatSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 3),
    _Hm2DnatSourceAddress_Type()
)
hm2DnatSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatSourceAddress.setStatus("current")


class _Hm2DnatSourcePort_Type(DisplayString):
    """Custom type hm2DnatSourcePort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2DnatSourcePort_Type.__name__ = "DisplayString"
_Hm2DnatSourcePort_Object = MibTableColumn
hm2DnatSourcePort = _Hm2DnatSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 4),
    _Hm2DnatSourcePort_Type()
)
hm2DnatSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatSourcePort.setStatus("current")


class _Hm2DnatTargetAddress_Type(DisplayString):
    """Custom type hm2DnatTargetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DnatTargetAddress_Type.__name__ = "DisplayString"
_Hm2DnatTargetAddress_Object = MibTableColumn
hm2DnatTargetAddress = _Hm2DnatTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 5),
    _Hm2DnatTargetAddress_Type()
)
hm2DnatTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatTargetAddress.setStatus("current")


class _Hm2DnatTargetPort_Type(DisplayString):
    """Custom type hm2DnatTargetPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2DnatTargetPort_Type.__name__ = "DisplayString"
_Hm2DnatTargetPort_Object = MibTableColumn
hm2DnatTargetPort = _Hm2DnatTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 6),
    _Hm2DnatTargetPort_Type()
)
hm2DnatTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatTargetPort.setStatus("current")


class _Hm2DnatNewTargetAddress_Type(DisplayString):
    """Custom type hm2DnatNewTargetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DnatNewTargetAddress_Type.__name__ = "DisplayString"
_Hm2DnatNewTargetAddress_Object = MibTableColumn
hm2DnatNewTargetAddress = _Hm2DnatNewTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 7),
    _Hm2DnatNewTargetAddress_Type()
)
hm2DnatNewTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatNewTargetAddress.setStatus("current")


class _Hm2DnatNewTargetPort_Type(DisplayString):
    """Custom type hm2DnatNewTargetPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2DnatNewTargetPort_Type.__name__ = "DisplayString"
_Hm2DnatNewTargetPort_Object = MibTableColumn
hm2DnatNewTargetPort = _Hm2DnatNewTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 8),
    _Hm2DnatNewTargetPort_Type()
)
hm2DnatNewTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatNewTargetPort.setStatus("current")


class _Hm2DnatProto_Type(Integer32):
    """Custom type hm2DnatProto based on Integer32"""
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


_Hm2DnatProto_Type.__name__ = "Integer32"
_Hm2DnatProto_Object = MibTableColumn
hm2DnatProto = _Hm2DnatProto_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 9),
    _Hm2DnatProto_Type()
)
hm2DnatProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatProto.setStatus("current")


class _Hm2DnatRuleParams_Type(DisplayString):
    """Custom type hm2DnatRuleParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hm2DnatRuleParams_Type.__name__ = "DisplayString"
_Hm2DnatRuleParams_Object = MibTableColumn
hm2DnatRuleParams = _Hm2DnatRuleParams_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 10),
    _Hm2DnatRuleParams_Type()
)
hm2DnatRuleParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatRuleParams.setStatus("current")


class _Hm2DnatLog_Type(TruthValue):
    """Custom type hm2DnatLog based on TruthValue"""


_Hm2DnatLog_Object = MibTableColumn
hm2DnatLog = _Hm2DnatLog_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 11),
    _Hm2DnatLog_Type()
)
hm2DnatLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatLog.setStatus("current")


class _Hm2DnatTrap_Type(TruthValue):
    """Custom type hm2DnatTrap based on TruthValue"""


_Hm2DnatTrap_Object = MibTableColumn
hm2DnatTrap = _Hm2DnatTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 12),
    _Hm2DnatTrap_Type()
)
hm2DnatTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatTrap.setStatus("current")
_Hm2DnatRowStatus_Type = RowStatus
_Hm2DnatRowStatus_Object = MibTableColumn
hm2DnatRowStatus = _Hm2DnatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 13),
    _Hm2DnatRowStatus_Type()
)
hm2DnatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatRowStatus.setStatus("current")


class _Hm2DnatDescription_Type(DisplayString):
    """Custom type hm2DnatDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2DnatDescription_Type.__name__ = "DisplayString"
_Hm2DnatDescription_Object = MibTableColumn
hm2DnatDescription = _Hm2DnatDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 1, 1, 14),
    _Hm2DnatDescription_Type()
)
hm2DnatDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatDescription.setStatus("current")
_Hm2DnatRuleIfMappingTable_Object = MibTable
hm2DnatRuleIfMappingTable = _Hm2DnatRuleIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hm2DnatRuleIfMappingTable.setStatus("current")
_Hm2DnatRuleIfMappingEntry_Object = MibTableRow
hm2DnatRuleIfMappingEntry = _Hm2DnatRuleIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 2, 1)
)
hm2DnatRuleIfMappingEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2DnatIfmInterface"),
    (0, "HM2-NAT-MIB", "hm2DnatIfmDirection"),
    (0, "HM2-NAT-MIB", "hm2DnatIfmRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DnatRuleIfMappingEntry.setStatus("current")


class _Hm2DnatIfmRuleIndex_Type(Integer32):
    """Custom type hm2DnatIfmRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Hm2DnatIfmRuleIndex_Type.__name__ = "Integer32"
_Hm2DnatIfmRuleIndex_Object = MibTableColumn
hm2DnatIfmRuleIndex = _Hm2DnatIfmRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 2, 1, 1),
    _Hm2DnatIfmRuleIndex_Type()
)
hm2DnatIfmRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DnatIfmRuleIndex.setStatus("current")


class _Hm2DnatIfmDirection_Type(Integer32):
    """Custom type hm2DnatIfmDirection based on Integer32"""
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


_Hm2DnatIfmDirection_Type.__name__ = "Integer32"
_Hm2DnatIfmDirection_Object = MibTableColumn
hm2DnatIfmDirection = _Hm2DnatIfmDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 2, 1, 2),
    _Hm2DnatIfmDirection_Type()
)
hm2DnatIfmDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DnatIfmDirection.setStatus("current")
_Hm2DnatIfmPriority_Type = Unsigned32
_Hm2DnatIfmPriority_Object = MibTableColumn
hm2DnatIfmPriority = _Hm2DnatIfmPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 2, 1, 3),
    _Hm2DnatIfmPriority_Type()
)
hm2DnatIfmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatIfmPriority.setStatus("current")
_Hm2DnatIfmInterface_Type = InterfaceIndex
_Hm2DnatIfmInterface_Object = MibTableColumn
hm2DnatIfmInterface = _Hm2DnatIfmInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 2, 1, 4),
    _Hm2DnatIfmInterface_Type()
)
hm2DnatIfmInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DnatIfmInterface.setStatus("current")
_Hm2DnatIfmRowStatus_Type = RowStatus
_Hm2DnatIfmRowStatus_Object = MibTableColumn
hm2DnatIfmRowStatus = _Hm2DnatIfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 1, 2, 2, 1, 5),
    _Hm2DnatIfmRowStatus_Type()
)
hm2DnatIfmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DnatIfmRowStatus.setStatus("current")
_Hm2DnatStats_ObjectIdentity = ObjectIdentity
hm2DnatStats = _Hm2DnatStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2)
)
_Hm2DnatGlobalStats_ObjectIdentity = ObjectIdentity
hm2DnatGlobalStats = _Hm2DnatGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 1)
)
_Hm2DnatStatsTotalPck_Type = Counter64
_Hm2DnatStatsTotalPck_Object = MibScalar
hm2DnatStatsTotalPck = _Hm2DnatStatsTotalPck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 1, 1),
    _Hm2DnatStatsTotalPck_Type()
)
hm2DnatStatsTotalPck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatStatsTotalPck.setStatus("current")
_Hm2DnatStatsTotalPckSize_Type = Counter64
_Hm2DnatStatsTotalPckSize_Object = MibScalar
hm2DnatStatsTotalPckSize = _Hm2DnatStatsTotalPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 1, 2),
    _Hm2DnatStatsTotalPckSize_Type()
)
hm2DnatStatsTotalPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatStatsTotalPckSize.setStatus("current")
_Hm2DnatStatsTotalPckDenDrop_Type = Counter64
_Hm2DnatStatsTotalPckDenDrop_Object = MibScalar
hm2DnatStatsTotalPckDenDrop = _Hm2DnatStatsTotalPckDenDrop_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 1, 3),
    _Hm2DnatStatsTotalPckDenDrop_Type()
)
hm2DnatStatsTotalPckDenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatStatsTotalPckDenDrop.setStatus("current")
_Hm2DnatStatsTotalPckAccepted_Type = Counter64
_Hm2DnatStatsTotalPckAccepted_Object = MibScalar
hm2DnatStatsTotalPckAccepted = _Hm2DnatStatsTotalPckAccepted_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 1, 4),
    _Hm2DnatStatsTotalPckAccepted_Type()
)
hm2DnatStatsTotalPckAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatStatsTotalPckAccepted.setStatus("current")
_Hm2DnatRuleStats_ObjectIdentity = ObjectIdentity
hm2DnatRuleStats = _Hm2DnatRuleStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 2)
)
_Hm2DnatStatsRuleTable_Object = MibTable
hm2DnatStatsRuleTable = _Hm2DnatStatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DnatStatsRuleTable.setStatus("current")
_Hm2DnatStatsRuleTableEntry_Object = MibTableRow
hm2DnatStatsRuleTableEntry = _Hm2DnatStatsRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 2, 1, 1)
)
hm2DnatStatsRuleTableEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2DnatRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DnatStatsRuleTableEntry.setStatus("current")
_Hm2DnatStatsPckCount_Type = Counter64
_Hm2DnatStatsPckCount_Object = MibTableColumn
hm2DnatStatsPckCount = _Hm2DnatStatsPckCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 2, 1, 1, 1),
    _Hm2DnatStatsPckCount_Type()
)
hm2DnatStatsPckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatStatsPckCount.setStatus("current")
_Hm2DnatStatsPckSize_Type = Counter64
_Hm2DnatStatsPckSize_Object = MibTableColumn
hm2DnatStatsPckSize = _Hm2DnatStatsPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 2, 1, 1, 2),
    _Hm2DnatStatsPckSize_Type()
)
hm2DnatStatsPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatStatsPckSize.setStatus("current")
_Hm2DnatStatsLastApplied_Type = HmTimeSeconds1970
_Hm2DnatStatsLastApplied_Object = MibTableColumn
hm2DnatStatsLastApplied = _Hm2DnatStatsLastApplied_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 2, 2, 2, 1, 1, 3),
    _Hm2DnatStatsLastApplied_Type()
)
hm2DnatStatsLastApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DnatStatsLastApplied.setStatus("current")
_Hm21to1_ObjectIdentity = ObjectIdentity
hm21to1 = _Hm21to1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4)
)
_Hm21to1RuleObjects_ObjectIdentity = ObjectIdentity
hm21to1RuleObjects = _Hm21to1RuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 1)
)
_Hm21to1RuleCount_Type = Integer32
_Hm21to1RuleCount_Object = MibScalar
hm21to1RuleCount = _Hm21to1RuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 1, 1),
    _Hm21to1RuleCount_Type()
)
hm21to1RuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1RuleCount.setStatus("current")
_Hm21to1IfMappingRuleCount_Type = Integer32
_Hm21to1IfMappingRuleCount_Object = MibScalar
hm21to1IfMappingRuleCount = _Hm21to1IfMappingRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 1, 2),
    _Hm21to1IfMappingRuleCount_Type()
)
hm21to1IfMappingRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1IfMappingRuleCount.setStatus("current")


class _Hm21to1RulePendingActions_Type(TruthValue):
    """Custom type hm21to1RulePendingActions based on TruthValue"""


_Hm21to1RulePendingActions_Object = MibScalar
hm21to1RulePendingActions = _Hm21to1RulePendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 1, 3),
    _Hm21to1RulePendingActions_Type()
)
hm21to1RulePendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1RulePendingActions.setStatus("current")


class _Hm21to1CommitPendingActions_Type(HmActionValue):
    """Custom type hm21to1CommitPendingActions based on HmActionValue"""


_Hm21to1CommitPendingActions_Object = MibScalar
hm21to1CommitPendingActions = _Hm21to1CommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 1, 4),
    _Hm21to1CommitPendingActions_Type()
)
hm21to1CommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm21to1CommitPendingActions.setStatus("current")


class _Hm21to1Alg_Type(Bits):
    """Custom type hm21to1Alg based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("ftp", 0),
          ("icmp", 1))
    )

_Hm21to1Alg_Type.__name__ = "Bits"
_Hm21to1Alg_Object = MibScalar
hm21to1Alg = _Hm21to1Alg_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 1, 5),
    _Hm21to1Alg_Type()
)
hm21to1Alg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm21to1Alg.setStatus("current")


class _Hm21to1PublicIntf_Type(InterfaceIndexOrZero):
    """Custom type hm21to1PublicIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm21to1PublicIntf_Object = MibScalar
hm21to1PublicIntf = _Hm21to1PublicIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 1, 6),
    _Hm21to1PublicIntf_Type()
)
hm21to1PublicIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm21to1PublicIntf.setStatus("current")
_Hm21to1RuleTables_ObjectIdentity = ObjectIdentity
hm21to1RuleTables = _Hm21to1RuleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2)
)
_Hm21to1RuleTable_Object = MibTable
hm21to1RuleTable = _Hm21to1RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hm21to1RuleTable.setStatus("current")
_Hm21to1RuleEntry_Object = MibTableRow
hm21to1RuleEntry = _Hm21to1RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1)
)
hm21to1RuleEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm21to1RuleIndex"),
)
if mibBuilder.loadTexts:
    hm21to1RuleEntry.setStatus("current")


class _Hm21to1RuleIndex_Type(Integer32):
    """Custom type hm21to1RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hm21to1RuleIndex_Type.__name__ = "Integer32"
_Hm21to1RuleIndex_Object = MibTableColumn
hm21to1RuleIndex = _Hm21to1RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 1),
    _Hm21to1RuleIndex_Type()
)
hm21to1RuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm21to1RuleIndex.setStatus("current")


class _Hm21to1TargetAddress_Type(DisplayString):
    """Custom type hm21to1TargetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm21to1TargetAddress_Type.__name__ = "DisplayString"
_Hm21to1TargetAddress_Object = MibTableColumn
hm21to1TargetAddress = _Hm21to1TargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 2),
    _Hm21to1TargetAddress_Type()
)
hm21to1TargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1TargetAddress.setStatus("current")


class _Hm21to1NewTargetAddress_Type(DisplayString):
    """Custom type hm21to1NewTargetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm21to1NewTargetAddress_Type.__name__ = "DisplayString"
_Hm21to1NewTargetAddress_Object = MibTableColumn
hm21to1NewTargetAddress = _Hm21to1NewTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 3),
    _Hm21to1NewTargetAddress_Type()
)
hm21to1NewTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1NewTargetAddress.setStatus("current")


class _Hm21to1RuleParams_Type(DisplayString):
    """Custom type hm21to1RuleParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hm21to1RuleParams_Type.__name__ = "DisplayString"
_Hm21to1RuleParams_Object = MibTableColumn
hm21to1RuleParams = _Hm21to1RuleParams_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 4),
    _Hm21to1RuleParams_Type()
)
hm21to1RuleParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1RuleParams.setStatus("current")


class _Hm21to1Log_Type(TruthValue):
    """Custom type hm21to1Log based on TruthValue"""


_Hm21to1Log_Object = MibTableColumn
hm21to1Log = _Hm21to1Log_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 5),
    _Hm21to1Log_Type()
)
hm21to1Log.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1Log.setStatus("current")


class _Hm21to1Trap_Type(TruthValue):
    """Custom type hm21to1Trap based on TruthValue"""


_Hm21to1Trap_Object = MibTableColumn
hm21to1Trap = _Hm21to1Trap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 6),
    _Hm21to1Trap_Type()
)
hm21to1Trap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1Trap.setStatus("current")
_Hm21to1RowStatus_Type = RowStatus
_Hm21to1RowStatus_Object = MibTableColumn
hm21to1RowStatus = _Hm21to1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 7),
    _Hm21to1RowStatus_Type()
)
hm21to1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1RowStatus.setStatus("current")


class _Hm21to1Description_Type(DisplayString):
    """Custom type hm21to1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm21to1Description_Type.__name__ = "DisplayString"
_Hm21to1Description_Object = MibTableColumn
hm21to1Description = _Hm21to1Description_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 8),
    _Hm21to1Description_Type()
)
hm21to1Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1Description.setStatus("current")


class _Hm21to1IngressIntf_Type(InterfaceIndexOrZero):
    """Custom type hm21to1IngressIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm21to1IngressIntf_Object = MibTableColumn
hm21to1IngressIntf = _Hm21to1IngressIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 9),
    _Hm21to1IngressIntf_Type()
)
hm21to1IngressIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1IngressIntf.setStatus("current")


class _Hm21to1EgressIntf_Type(InterfaceIndexOrZero):
    """Custom type hm21to1EgressIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm21to1EgressIntf_Object = MibTableColumn
hm21to1EgressIntf = _Hm21to1EgressIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 10),
    _Hm21to1EgressIntf_Type()
)
hm21to1EgressIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1EgressIntf.setStatus("current")


class _Hm21to1Priority_Type(Unsigned32):
    """Custom type hm21to1Priority based on Unsigned32"""
    defaultValue = 0


_Hm21to1Priority_Object = MibTableColumn
hm21to1Priority = _Hm21to1Priority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 11),
    _Hm21to1Priority_Type()
)
hm21to1Priority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1Priority.setStatus("current")


class _Hm21to1StorageType_Type(StorageType):
    """Custom type hm21to1StorageType based on StorageType"""


_Hm21to1StorageType_Object = MibTableColumn
hm21to1StorageType = _Hm21to1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 2, 1, 1, 12),
    _Hm21to1StorageType_Type()
)
hm21to1StorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm21to1StorageType.setStatus("current")
_Hm21to1Stats_ObjectIdentity = ObjectIdentity
hm21to1Stats = _Hm21to1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3)
)
_Hm21to1GeneralStats_ObjectIdentity = ObjectIdentity
hm21to1GeneralStats = _Hm21to1GeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 1)
)
_Hm21to1StatsTotalPck_Type = Counter64
_Hm21to1StatsTotalPck_Object = MibScalar
hm21to1StatsTotalPck = _Hm21to1StatsTotalPck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 1, 1),
    _Hm21to1StatsTotalPck_Type()
)
hm21to1StatsTotalPck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1StatsTotalPck.setStatus("current")
_Hm21to1StatsTotalPckSize_Type = Counter64
_Hm21to1StatsTotalPckSize_Object = MibScalar
hm21to1StatsTotalPckSize = _Hm21to1StatsTotalPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 1, 2),
    _Hm21to1StatsTotalPckSize_Type()
)
hm21to1StatsTotalPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1StatsTotalPckSize.setStatus("current")
_Hm21to1StatsTotalPckDenDrop_Type = Counter64
_Hm21to1StatsTotalPckDenDrop_Object = MibScalar
hm21to1StatsTotalPckDenDrop = _Hm21to1StatsTotalPckDenDrop_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 1, 3),
    _Hm21to1StatsTotalPckDenDrop_Type()
)
hm21to1StatsTotalPckDenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1StatsTotalPckDenDrop.setStatus("current")
_Hm21to1StatsTotalPckAccepted_Type = Counter64
_Hm21to1StatsTotalPckAccepted_Object = MibScalar
hm21to1StatsTotalPckAccepted = _Hm21to1StatsTotalPckAccepted_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 1, 4),
    _Hm21to1StatsTotalPckAccepted_Type()
)
hm21to1StatsTotalPckAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1StatsTotalPckAccepted.setStatus("current")
_Hm21to1StatsTables_ObjectIdentity = ObjectIdentity
hm21to1StatsTables = _Hm21to1StatsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 2)
)
_Hm21to1StatsRuleTable_Object = MibTable
hm21to1StatsRuleTable = _Hm21to1StatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm21to1StatsRuleTable.setStatus("current")
_Hm21to1StatsRuleTableEntry_Object = MibTableRow
hm21to1StatsRuleTableEntry = _Hm21to1StatsRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 2, 1, 1)
)
hm21to1StatsRuleTableEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm21to1RuleIndex"),
)
if mibBuilder.loadTexts:
    hm21to1StatsRuleTableEntry.setStatus("current")
_Hm21to1StatsPckCount_Type = Counter64
_Hm21to1StatsPckCount_Object = MibTableColumn
hm21to1StatsPckCount = _Hm21to1StatsPckCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 2, 1, 1, 1),
    _Hm21to1StatsPckCount_Type()
)
hm21to1StatsPckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1StatsPckCount.setStatus("current")
_Hm21to1StatsPckSize_Type = Counter64
_Hm21to1StatsPckSize_Object = MibTableColumn
hm21to1StatsPckSize = _Hm21to1StatsPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 2, 1, 1, 2),
    _Hm21to1StatsPckSize_Type()
)
hm21to1StatsPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1StatsPckSize.setStatus("current")
_Hm21to1StatsLastApplied_Type = HmTimeSeconds1970
_Hm21to1StatsLastApplied_Object = MibTableColumn
hm21to1StatsLastApplied = _Hm21to1StatsLastApplied_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 4, 3, 2, 1, 1, 3),
    _Hm21to1StatsLastApplied_Type()
)
hm21to1StatsLastApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm21to1StatsLastApplied.setStatus("current")
_Hm2Masquerading_ObjectIdentity = ObjectIdentity
hm2Masquerading = _Hm2Masquerading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5)
)
_Hm2MasqRuleObjects_ObjectIdentity = ObjectIdentity
hm2MasqRuleObjects = _Hm2MasqRuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 1)
)
_Hm2MasqRuleCount_Type = Integer32
_Hm2MasqRuleCount_Object = MibScalar
hm2MasqRuleCount = _Hm2MasqRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 1, 1),
    _Hm2MasqRuleCount_Type()
)
hm2MasqRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqRuleCount.setStatus("current")
_Hm2MasqIfMappingRuleCount_Type = Integer32
_Hm2MasqIfMappingRuleCount_Object = MibScalar
hm2MasqIfMappingRuleCount = _Hm2MasqIfMappingRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 1, 2),
    _Hm2MasqIfMappingRuleCount_Type()
)
hm2MasqIfMappingRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqIfMappingRuleCount.setStatus("current")


class _Hm2MasqRulePendingActions_Type(TruthValue):
    """Custom type hm2MasqRulePendingActions based on TruthValue"""


_Hm2MasqRulePendingActions_Object = MibScalar
hm2MasqRulePendingActions = _Hm2MasqRulePendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 1, 3),
    _Hm2MasqRulePendingActions_Type()
)
hm2MasqRulePendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqRulePendingActions.setStatus("current")


class _Hm2MasqCommitPendingActions_Type(HmActionValue):
    """Custom type hm2MasqCommitPendingActions based on HmActionValue"""


_Hm2MasqCommitPendingActions_Object = MibScalar
hm2MasqCommitPendingActions = _Hm2MasqCommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 1, 4),
    _Hm2MasqCommitPendingActions_Type()
)
hm2MasqCommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2MasqCommitPendingActions.setStatus("current")
_Hm2MasqRuleTables_ObjectIdentity = ObjectIdentity
hm2MasqRuleTables = _Hm2MasqRuleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2)
)
_Hm2MasqRuleTable_Object = MibTable
hm2MasqRuleTable = _Hm2MasqRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hm2MasqRuleTable.setStatus("current")
_Hm2MasqRuleEntry_Object = MibTableRow
hm2MasqRuleEntry = _Hm2MasqRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1)
)
hm2MasqRuleEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2MasqRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2MasqRuleEntry.setStatus("current")


class _Hm2MasqRuleIndex_Type(Integer32):
    """Custom type hm2MasqRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hm2MasqRuleIndex_Type.__name__ = "Integer32"
_Hm2MasqRuleIndex_Object = MibTableColumn
hm2MasqRuleIndex = _Hm2MasqRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 1),
    _Hm2MasqRuleIndex_Type()
)
hm2MasqRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2MasqRuleIndex.setStatus("current")


class _Hm2MasqSourceAddress_Type(DisplayString):
    """Custom type hm2MasqSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2MasqSourceAddress_Type.__name__ = "DisplayString"
_Hm2MasqSourceAddress_Object = MibTableColumn
hm2MasqSourceAddress = _Hm2MasqSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 2),
    _Hm2MasqSourceAddress_Type()
)
hm2MasqSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqSourceAddress.setStatus("current")


class _Hm2MasqSourcePort_Type(DisplayString):
    """Custom type hm2MasqSourcePort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hm2MasqSourcePort_Type.__name__ = "DisplayString"
_Hm2MasqSourcePort_Object = MibTableColumn
hm2MasqSourcePort = _Hm2MasqSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 3),
    _Hm2MasqSourcePort_Type()
)
hm2MasqSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqSourcePort.setStatus("current")


class _Hm2MasqProto_Type(Integer32):
    """Custom type hm2MasqProto based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("any", 9),
          ("tcp", 4),
          ("udp", 5))
    )


_Hm2MasqProto_Type.__name__ = "Integer32"
_Hm2MasqProto_Object = MibTableColumn
hm2MasqProto = _Hm2MasqProto_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 4),
    _Hm2MasqProto_Type()
)
hm2MasqProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqProto.setStatus("current")


class _Hm2MasqRuleParams_Type(DisplayString):
    """Custom type hm2MasqRuleParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hm2MasqRuleParams_Type.__name__ = "DisplayString"
_Hm2MasqRuleParams_Object = MibTableColumn
hm2MasqRuleParams = _Hm2MasqRuleParams_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 5),
    _Hm2MasqRuleParams_Type()
)
hm2MasqRuleParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqRuleParams.setStatus("current")


class _Hm2MasqLog_Type(TruthValue):
    """Custom type hm2MasqLog based on TruthValue"""


_Hm2MasqLog_Object = MibTableColumn
hm2MasqLog = _Hm2MasqLog_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 6),
    _Hm2MasqLog_Type()
)
hm2MasqLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqLog.setStatus("current")


class _Hm2MasqTrap_Type(TruthValue):
    """Custom type hm2MasqTrap based on TruthValue"""


_Hm2MasqTrap_Object = MibTableColumn
hm2MasqTrap = _Hm2MasqTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 7),
    _Hm2MasqTrap_Type()
)
hm2MasqTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqTrap.setStatus("current")
_Hm2MasqRowStatus_Type = RowStatus
_Hm2MasqRowStatus_Object = MibTableColumn
hm2MasqRowStatus = _Hm2MasqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 8),
    _Hm2MasqRowStatus_Type()
)
hm2MasqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqRowStatus.setStatus("current")


class _Hm2MasqDescription_Type(DisplayString):
    """Custom type hm2MasqDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2MasqDescription_Type.__name__ = "DisplayString"
_Hm2MasqDescription_Object = MibTableColumn
hm2MasqDescription = _Hm2MasqDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 9),
    _Hm2MasqDescription_Type()
)
hm2MasqDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqDescription.setStatus("current")


class _Hm2MasqIpsecExempt_Type(TruthValue):
    """Custom type hm2MasqIpsecExempt based on TruthValue"""


_Hm2MasqIpsecExempt_Object = MibTableColumn
hm2MasqIpsecExempt = _Hm2MasqIpsecExempt_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 1, 1, 10),
    _Hm2MasqIpsecExempt_Type()
)
hm2MasqIpsecExempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqIpsecExempt.setStatus("current")
_Hm2MasqRuleIfMappingTable_Object = MibTable
hm2MasqRuleIfMappingTable = _Hm2MasqRuleIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hm2MasqRuleIfMappingTable.setStatus("current")
_Hm2MasqRuleIfMappingEntry_Object = MibTableRow
hm2MasqRuleIfMappingEntry = _Hm2MasqRuleIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 2, 1)
)
hm2MasqRuleIfMappingEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2MasqIfmInterface"),
    (0, "HM2-NAT-MIB", "hm2MasqIfmDirection"),
    (0, "HM2-NAT-MIB", "hm2MasqIfmRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2MasqRuleIfMappingEntry.setStatus("current")


class _Hm2MasqIfmRuleIndex_Type(Integer32):
    """Custom type hm2MasqIfmRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Hm2MasqIfmRuleIndex_Type.__name__ = "Integer32"
_Hm2MasqIfmRuleIndex_Object = MibTableColumn
hm2MasqIfmRuleIndex = _Hm2MasqIfmRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 2, 1, 1),
    _Hm2MasqIfmRuleIndex_Type()
)
hm2MasqIfmRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2MasqIfmRuleIndex.setStatus("current")


class _Hm2MasqIfmDirection_Type(Integer32):
    """Custom type hm2MasqIfmDirection based on Integer32"""
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


_Hm2MasqIfmDirection_Type.__name__ = "Integer32"
_Hm2MasqIfmDirection_Object = MibTableColumn
hm2MasqIfmDirection = _Hm2MasqIfmDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 2, 1, 2),
    _Hm2MasqIfmDirection_Type()
)
hm2MasqIfmDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2MasqIfmDirection.setStatus("current")
_Hm2MasqIfmPriority_Type = Unsigned32
_Hm2MasqIfmPriority_Object = MibTableColumn
hm2MasqIfmPriority = _Hm2MasqIfmPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 2, 1, 3),
    _Hm2MasqIfmPriority_Type()
)
hm2MasqIfmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqIfmPriority.setStatus("current")
_Hm2MasqIfmInterface_Type = InterfaceIndex
_Hm2MasqIfmInterface_Object = MibTableColumn
hm2MasqIfmInterface = _Hm2MasqIfmInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 2, 1, 4),
    _Hm2MasqIfmInterface_Type()
)
hm2MasqIfmInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2MasqIfmInterface.setStatus("current")
_Hm2MasqIfmRowStatus_Type = RowStatus
_Hm2MasqIfmRowStatus_Object = MibTableColumn
hm2MasqIfmRowStatus = _Hm2MasqIfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 2, 2, 1, 5),
    _Hm2MasqIfmRowStatus_Type()
)
hm2MasqIfmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2MasqIfmRowStatus.setStatus("current")
_Hm2MasqStats_ObjectIdentity = ObjectIdentity
hm2MasqStats = _Hm2MasqStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3)
)
_Hm2MasqGeneralStats_ObjectIdentity = ObjectIdentity
hm2MasqGeneralStats = _Hm2MasqGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 1)
)
_Hm2MasqStatsTotalPck_Type = Counter64
_Hm2MasqStatsTotalPck_Object = MibScalar
hm2MasqStatsTotalPck = _Hm2MasqStatsTotalPck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 1, 1),
    _Hm2MasqStatsTotalPck_Type()
)
hm2MasqStatsTotalPck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqStatsTotalPck.setStatus("current")
_Hm2MasqStatsTotalPckSize_Type = Counter64
_Hm2MasqStatsTotalPckSize_Object = MibScalar
hm2MasqStatsTotalPckSize = _Hm2MasqStatsTotalPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 1, 2),
    _Hm2MasqStatsTotalPckSize_Type()
)
hm2MasqStatsTotalPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqStatsTotalPckSize.setStatus("current")
_Hm2MasqStatsTotalPckDenDrop_Type = Counter64
_Hm2MasqStatsTotalPckDenDrop_Object = MibScalar
hm2MasqStatsTotalPckDenDrop = _Hm2MasqStatsTotalPckDenDrop_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 1, 3),
    _Hm2MasqStatsTotalPckDenDrop_Type()
)
hm2MasqStatsTotalPckDenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqStatsTotalPckDenDrop.setStatus("current")
_Hm2MasqStatsTotalPckAccepted_Type = Counter64
_Hm2MasqStatsTotalPckAccepted_Object = MibScalar
hm2MasqStatsTotalPckAccepted = _Hm2MasqStatsTotalPckAccepted_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 1, 4),
    _Hm2MasqStatsTotalPckAccepted_Type()
)
hm2MasqStatsTotalPckAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqStatsTotalPckAccepted.setStatus("current")
_Hm2MasqStatsRuleTables_ObjectIdentity = ObjectIdentity
hm2MasqStatsRuleTables = _Hm2MasqStatsRuleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 2)
)
_Hm2MasqStatsRuleTable_Object = MibTable
hm2MasqStatsRuleTable = _Hm2MasqStatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2MasqStatsRuleTable.setStatus("current")
_Hm2MasqStatsRuleTableEntry_Object = MibTableRow
hm2MasqStatsRuleTableEntry = _Hm2MasqStatsRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 2, 1, 1)
)
hm2MasqStatsRuleTableEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2MasqRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2MasqStatsRuleTableEntry.setStatus("current")
_Hm2MasqStatsPckCount_Type = Counter64
_Hm2MasqStatsPckCount_Object = MibTableColumn
hm2MasqStatsPckCount = _Hm2MasqStatsPckCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 2, 1, 1, 1),
    _Hm2MasqStatsPckCount_Type()
)
hm2MasqStatsPckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqStatsPckCount.setStatus("current")
_Hm2MasqStatsPckSize_Type = Counter64
_Hm2MasqStatsPckSize_Object = MibTableColumn
hm2MasqStatsPckSize = _Hm2MasqStatsPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 2, 1, 1, 2),
    _Hm2MasqStatsPckSize_Type()
)
hm2MasqStatsPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqStatsPckSize.setStatus("current")
_Hm2MasqStatsLastApplied_Type = HmTimeSeconds1970
_Hm2MasqStatsLastApplied_Object = MibTableColumn
hm2MasqStatsLastApplied = _Hm2MasqStatsLastApplied_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 5, 3, 2, 1, 1, 3),
    _Hm2MasqStatsLastApplied_Type()
)
hm2MasqStatsLastApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2MasqStatsLastApplied.setStatus("current")
_Hm2DoubleNat_ObjectIdentity = ObjectIdentity
hm2DoubleNat = _Hm2DoubleNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6)
)
_Hm2DoubleNatRuleObjects_ObjectIdentity = ObjectIdentity
hm2DoubleNatRuleObjects = _Hm2DoubleNatRuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 1)
)
_Hm2DoubleNatRuleCount_Type = Integer32
_Hm2DoubleNatRuleCount_Object = MibScalar
hm2DoubleNatRuleCount = _Hm2DoubleNatRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 1, 1),
    _Hm2DoubleNatRuleCount_Type()
)
hm2DoubleNatRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DoubleNatRuleCount.setStatus("current")
_Hm2DoubleNatIfMappingRuleCount_Type = Integer32
_Hm2DoubleNatIfMappingRuleCount_Object = MibScalar
hm2DoubleNatIfMappingRuleCount = _Hm2DoubleNatIfMappingRuleCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 1, 2),
    _Hm2DoubleNatIfMappingRuleCount_Type()
)
hm2DoubleNatIfMappingRuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DoubleNatIfMappingRuleCount.setStatus("current")


class _Hm2DoubleNatRulePendingActions_Type(TruthValue):
    """Custom type hm2DoubleNatRulePendingActions based on TruthValue"""


_Hm2DoubleNatRulePendingActions_Object = MibScalar
hm2DoubleNatRulePendingActions = _Hm2DoubleNatRulePendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 1, 3),
    _Hm2DoubleNatRulePendingActions_Type()
)
hm2DoubleNatRulePendingActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DoubleNatRulePendingActions.setStatus("current")


class _Hm2DoubleNatCommitPendingActions_Type(HmActionValue):
    """Custom type hm2DoubleNatCommitPendingActions based on HmActionValue"""


_Hm2DoubleNatCommitPendingActions_Object = MibScalar
hm2DoubleNatCommitPendingActions = _Hm2DoubleNatCommitPendingActions_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 1, 4),
    _Hm2DoubleNatCommitPendingActions_Type()
)
hm2DoubleNatCommitPendingActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DoubleNatCommitPendingActions.setStatus("current")
_Hm2DoubleNatRuleTables_ObjectIdentity = ObjectIdentity
hm2DoubleNatRuleTables = _Hm2DoubleNatRuleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2)
)
_Hm2DoubleNatRuleTable_Object = MibTable
hm2DoubleNatRuleTable = _Hm2DoubleNatRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DoubleNatRuleTable.setStatus("current")
_Hm2DoubleNatRuleEntry_Object = MibTableRow
hm2DoubleNatRuleEntry = _Hm2DoubleNatRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1)
)
hm2DoubleNatRuleEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2DonatRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DoubleNatRuleEntry.setStatus("current")


class _Hm2DonatRuleIndex_Type(Integer32):
    """Custom type hm2DonatRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2DonatRuleIndex_Type.__name__ = "Integer32"
_Hm2DonatRuleIndex_Object = MibTableColumn
hm2DonatRuleIndex = _Hm2DonatRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 1),
    _Hm2DonatRuleIndex_Type()
)
hm2DonatRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2DonatRuleIndex.setStatus("current")


class _Hm2DonatLocalInternalIp_Type(DisplayString):
    """Custom type hm2DonatLocalInternalIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DonatLocalInternalIp_Type.__name__ = "DisplayString"
_Hm2DonatLocalInternalIp_Object = MibTableColumn
hm2DonatLocalInternalIp = _Hm2DonatLocalInternalIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 2),
    _Hm2DonatLocalInternalIp_Type()
)
hm2DonatLocalInternalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatLocalInternalIp.setStatus("current")


class _Hm2DonatLocalExternalIp_Type(DisplayString):
    """Custom type hm2DonatLocalExternalIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DonatLocalExternalIp_Type.__name__ = "DisplayString"
_Hm2DonatLocalExternalIp_Object = MibTableColumn
hm2DonatLocalExternalIp = _Hm2DonatLocalExternalIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 3),
    _Hm2DonatLocalExternalIp_Type()
)
hm2DonatLocalExternalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatLocalExternalIp.setStatus("current")


class _Hm2DonatRemoteInternalIp_Type(DisplayString):
    """Custom type hm2DonatRemoteInternalIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DonatRemoteInternalIp_Type.__name__ = "DisplayString"
_Hm2DonatRemoteInternalIp_Object = MibTableColumn
hm2DonatRemoteInternalIp = _Hm2DonatRemoteInternalIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 4),
    _Hm2DonatRemoteInternalIp_Type()
)
hm2DonatRemoteInternalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatRemoteInternalIp.setStatus("current")


class _Hm2DonatRemoteExternalIp_Type(DisplayString):
    """Custom type hm2DonatRemoteExternalIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hm2DonatRemoteExternalIp_Type.__name__ = "DisplayString"
_Hm2DonatRemoteExternalIp_Object = MibTableColumn
hm2DonatRemoteExternalIp = _Hm2DonatRemoteExternalIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 5),
    _Hm2DonatRemoteExternalIp_Type()
)
hm2DonatRemoteExternalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatRemoteExternalIp.setStatus("current")


class _Hm2DonatRuleParams_Type(DisplayString):
    """Custom type hm2DonatRuleParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hm2DonatRuleParams_Type.__name__ = "DisplayString"
_Hm2DonatRuleParams_Object = MibTableColumn
hm2DonatRuleParams = _Hm2DonatRuleParams_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 6),
    _Hm2DonatRuleParams_Type()
)
hm2DonatRuleParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatRuleParams.setStatus("current")


class _Hm2DonatLog_Type(TruthValue):
    """Custom type hm2DonatLog based on TruthValue"""


_Hm2DonatLog_Object = MibTableColumn
hm2DonatLog = _Hm2DonatLog_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 7),
    _Hm2DonatLog_Type()
)
hm2DonatLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatLog.setStatus("current")


class _Hm2DonatTrap_Type(TruthValue):
    """Custom type hm2DonatTrap based on TruthValue"""


_Hm2DonatTrap_Object = MibTableColumn
hm2DonatTrap = _Hm2DonatTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 8),
    _Hm2DonatTrap_Type()
)
hm2DonatTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatTrap.setStatus("current")
_Hm2DonatRowStatus_Type = RowStatus
_Hm2DonatRowStatus_Object = MibTableColumn
hm2DonatRowStatus = _Hm2DonatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 9),
    _Hm2DonatRowStatus_Type()
)
hm2DonatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatRowStatus.setStatus("current")


class _Hm2DonatDescription_Type(DisplayString):
    """Custom type hm2DonatDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2DonatDescription_Type.__name__ = "DisplayString"
_Hm2DonatDescription_Object = MibTableColumn
hm2DonatDescription = _Hm2DonatDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 1, 1, 10),
    _Hm2DonatDescription_Type()
)
hm2DonatDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatDescription.setStatus("current")
_Hm2DonatRuleIfMappingTable_Object = MibTable
hm2DonatRuleIfMappingTable = _Hm2DonatRuleIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hm2DonatRuleIfMappingTable.setStatus("current")
_Hm2DonatRuleIfMappingEntry_Object = MibTableRow
hm2DonatRuleIfMappingEntry = _Hm2DonatRuleIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 2, 1)
)
hm2DonatRuleIfMappingEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2DonatIfmInterface"),
    (0, "HM2-NAT-MIB", "hm2DonatIfmDirection"),
    (0, "HM2-NAT-MIB", "hm2DonatIfmRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DonatRuleIfMappingEntry.setStatus("current")


class _Hm2DonatIfmRuleIndex_Type(Integer32):
    """Custom type hm2DonatIfmRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Hm2DonatIfmRuleIndex_Type.__name__ = "Integer32"
_Hm2DonatIfmRuleIndex_Object = MibTableColumn
hm2DonatIfmRuleIndex = _Hm2DonatIfmRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 2, 1, 1),
    _Hm2DonatIfmRuleIndex_Type()
)
hm2DonatIfmRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DonatIfmRuleIndex.setStatus("current")


class _Hm2DonatIfmDirection_Type(Integer32):
    """Custom type hm2DonatIfmDirection based on Integer32"""
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


_Hm2DonatIfmDirection_Type.__name__ = "Integer32"
_Hm2DonatIfmDirection_Object = MibTableColumn
hm2DonatIfmDirection = _Hm2DonatIfmDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 2, 1, 2),
    _Hm2DonatIfmDirection_Type()
)
hm2DonatIfmDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DonatIfmDirection.setStatus("current")
_Hm2DonatIfmPriority_Type = Unsigned32
_Hm2DonatIfmPriority_Object = MibTableColumn
hm2DonatIfmPriority = _Hm2DonatIfmPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 2, 1, 3),
    _Hm2DonatIfmPriority_Type()
)
hm2DonatIfmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatIfmPriority.setStatus("current")
_Hm2DonatIfmInterface_Type = InterfaceIndex
_Hm2DonatIfmInterface_Object = MibTableColumn
hm2DonatIfmInterface = _Hm2DonatIfmInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 2, 1, 4),
    _Hm2DonatIfmInterface_Type()
)
hm2DonatIfmInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DonatIfmInterface.setStatus("current")
_Hm2DonatIfmRowStatus_Type = RowStatus
_Hm2DonatIfmRowStatus_Object = MibTableColumn
hm2DonatIfmRowStatus = _Hm2DonatIfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 2, 2, 1, 5),
    _Hm2DonatIfmRowStatus_Type()
)
hm2DonatIfmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DonatIfmRowStatus.setStatus("current")
_Hm2DonatStats_ObjectIdentity = ObjectIdentity
hm2DonatStats = _Hm2DonatStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3)
)
_Hm2DonatGeneralStats_ObjectIdentity = ObjectIdentity
hm2DonatGeneralStats = _Hm2DonatGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 1)
)
_Hm2DonatStatsTotalPck_Type = Counter64
_Hm2DonatStatsTotalPck_Object = MibScalar
hm2DonatStatsTotalPck = _Hm2DonatStatsTotalPck_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 1, 1),
    _Hm2DonatStatsTotalPck_Type()
)
hm2DonatStatsTotalPck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DonatStatsTotalPck.setStatus("current")
_Hm2DonatStatsTotalPckSize_Type = Counter64
_Hm2DonatStatsTotalPckSize_Object = MibScalar
hm2DonatStatsTotalPckSize = _Hm2DonatStatsTotalPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 1, 2),
    _Hm2DonatStatsTotalPckSize_Type()
)
hm2DonatStatsTotalPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DonatStatsTotalPckSize.setStatus("current")
_Hm2DonatStatsTotalPckDenDrop_Type = Counter64
_Hm2DonatStatsTotalPckDenDrop_Object = MibScalar
hm2DonatStatsTotalPckDenDrop = _Hm2DonatStatsTotalPckDenDrop_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 1, 3),
    _Hm2DonatStatsTotalPckDenDrop_Type()
)
hm2DonatStatsTotalPckDenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DonatStatsTotalPckDenDrop.setStatus("current")
_Hm2DonatStatsTotalPckAcc_Type = Counter64
_Hm2DonatStatsTotalPckAcc_Object = MibScalar
hm2DonatStatsTotalPckAcc = _Hm2DonatStatsTotalPckAcc_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 1, 4),
    _Hm2DonatStatsTotalPckAcc_Type()
)
hm2DonatStatsTotalPckAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DonatStatsTotalPckAcc.setStatus("current")
_Hm2DonatStatsRuleTables_ObjectIdentity = ObjectIdentity
hm2DonatStatsRuleTables = _Hm2DonatStatsRuleTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 2)
)
_Hm2DonatStatsRuleTable_Object = MibTable
hm2DonatStatsRuleTable = _Hm2DonatStatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DonatStatsRuleTable.setStatus("current")
_Hm2DonatStatsRuleTableEntry_Object = MibTableRow
hm2DonatStatsRuleTableEntry = _Hm2DonatStatsRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 2, 1, 1)
)
hm2DonatStatsRuleTableEntry.setIndexNames(
    (0, "HM2-NAT-MIB", "hm2DonatRuleIndex"),
)
if mibBuilder.loadTexts:
    hm2DonatStatsRuleTableEntry.setStatus("current")
_Hm2DonatStatsPckCount_Type = Counter64
_Hm2DonatStatsPckCount_Object = MibTableColumn
hm2DonatStatsPckCount = _Hm2DonatStatsPckCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 2, 1, 1, 1),
    _Hm2DonatStatsPckCount_Type()
)
hm2DonatStatsPckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DonatStatsPckCount.setStatus("current")
_Hm2DonatStatsPckSize_Type = Counter64
_Hm2DonatStatsPckSize_Object = MibTableColumn
hm2DonatStatsPckSize = _Hm2DonatStatsPckSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 2, 1, 1, 2),
    _Hm2DonatStatsPckSize_Type()
)
hm2DonatStatsPckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DonatStatsPckSize.setStatus("current")
_Hm2DonatStatsLastApplied_Type = HmTimeSeconds1970
_Hm2DonatStatsLastApplied_Object = MibTableColumn
hm2DonatStatsLastApplied = _Hm2DonatStatsLastApplied_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 1, 6, 3, 2, 1, 1, 3),
    _Hm2DonatStatsLastApplied_Type()
)
hm2DonatStatsLastApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DonatStatsLastApplied.setStatus("current")
_Hm2NatConformance_ObjectIdentity = ObjectIdentity
hm2NatConformance = _Hm2NatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 2)
)
_Hm2NatCompliances_ObjectIdentity = ObjectIdentity
hm2NatCompliances = _Hm2NatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 2, 1)
)
_Hm2NatGroups_ObjectIdentity = ObjectIdentity
hm2NatGroups = _Hm2NatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 2, 2)
)

# Managed Objects groups

hm2NatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 2, 2, 1)
)
hm2NatGeneralGroup.setObjects(
      *(("HM2-NAT-MIB", "hm2DnatMaxRules"),
        ("HM2-NAT-MIB", "hm2OneToOneNatMaxRules"),
        ("HM2-NAT-MIB", "hm2DoubleNatMaxRules"),
        ("HM2-NAT-MIB", "hm2MasqMaxRules"),
        ("HM2-NAT-MIB", "hm2NatResetStatistics"),
        ("HM2-NAT-MIB", "hm2DnatIfMappingRuleCount"),
        ("HM2-NAT-MIB", "hm2DnatRulePendingActions"),
        ("HM2-NAT-MIB", "hm2DnatCommitPendingActions"),
        ("HM2-NAT-MIB", "hm2DnatRuleCount"),
        ("HM2-NAT-MIB", "hm2DnatRuleIndex"),
        ("HM2-NAT-MIB", "hm2DnatSourceAddress"),
        ("HM2-NAT-MIB", "hm2DnatSourcePort"),
        ("HM2-NAT-MIB", "hm2DnatTargetAddress"),
        ("HM2-NAT-MIB", "hm2DnatTargetPort"),
        ("HM2-NAT-MIB", "hm2DnatNewTargetAddress"),
        ("HM2-NAT-MIB", "hm2DnatNewTargetPort"),
        ("HM2-NAT-MIB", "hm2DnatProto"),
        ("HM2-NAT-MIB", "hm2DnatRuleParams"),
        ("HM2-NAT-MIB", "hm2DnatLog"),
        ("HM2-NAT-MIB", "hm2DnatTrap"),
        ("HM2-NAT-MIB", "hm2DnatDescription"),
        ("HM2-NAT-MIB", "hm2DnatRowStatus"),
        ("HM2-NAT-MIB", "hm2DnatIfmPriority"),
        ("HM2-NAT-MIB", "hm2DnatIfmRowStatus"),
        ("HM2-NAT-MIB", "hm2DnatStatsPckCount"),
        ("HM2-NAT-MIB", "hm2DnatStatsPckSize"),
        ("HM2-NAT-MIB", "hm2DnatStatsLastApplied"),
        ("HM2-NAT-MIB", "hm2DnatStatsTotalPck"),
        ("HM2-NAT-MIB", "hm2DnatStatsTotalPckSize"),
        ("HM2-NAT-MIB", "hm2DnatStatsTotalPckDenDrop"),
        ("HM2-NAT-MIB", "hm2DnatStatsTotalPckAccepted"),
        ("HM2-NAT-MIB", "hm21to1IfMappingRuleCount"),
        ("HM2-NAT-MIB", "hm21to1RulePendingActions"),
        ("HM2-NAT-MIB", "hm21to1CommitPendingActions"),
        ("HM2-NAT-MIB", "hm21to1RuleCount"),
        ("HM2-NAT-MIB", "hm21to1RuleIndex"),
        ("HM2-NAT-MIB", "hm21to1TargetAddress"),
        ("HM2-NAT-MIB", "hm21to1NewTargetAddress"),
        ("HM2-NAT-MIB", "hm21to1RuleParams"),
        ("HM2-NAT-MIB", "hm21to1Log"),
        ("HM2-NAT-MIB", "hm21to1Trap"),
        ("HM2-NAT-MIB", "hm21to1Description"),
        ("HM2-NAT-MIB", "hm21to1IngressIntf"),
        ("HM2-NAT-MIB", "hm21to1EgressIntf"),
        ("HM2-NAT-MIB", "hm21to1Priority"),
        ("HM2-NAT-MIB", "hm21to1RowStatus"),
        ("HM2-NAT-MIB", "hm21to1StatsPckCount"),
        ("HM2-NAT-MIB", "hm21to1StatsPckSize"),
        ("HM2-NAT-MIB", "hm21to1StatsLastApplied"),
        ("HM2-NAT-MIB", "hm21to1StatsTotalPck"),
        ("HM2-NAT-MIB", "hm21to1StatsTotalPckSize"),
        ("HM2-NAT-MIB", "hm21to1StatsTotalPckDenDrop"),
        ("HM2-NAT-MIB", "hm21to1StatsTotalPckAccepted"),
        ("HM2-NAT-MIB", "hm2MasqIfMappingRuleCount"),
        ("HM2-NAT-MIB", "hm2MasqRulePendingActions"),
        ("HM2-NAT-MIB", "hm2MasqCommitPendingActions"),
        ("HM2-NAT-MIB", "hm2MasqRuleCount"),
        ("HM2-NAT-MIB", "hm2MasqRuleIndex"),
        ("HM2-NAT-MIB", "hm2MasqSourceAddress"),
        ("HM2-NAT-MIB", "hm2MasqSourcePort"),
        ("HM2-NAT-MIB", "hm2MasqProto"),
        ("HM2-NAT-MIB", "hm2MasqRuleParams"),
        ("HM2-NAT-MIB", "hm2MasqLog"),
        ("HM2-NAT-MIB", "hm2MasqTrap"),
        ("HM2-NAT-MIB", "hm2MasqDescription"),
        ("HM2-NAT-MIB", "hm2MasqRowStatus"),
        ("HM2-NAT-MIB", "hm2MasqIfmPriority"),
        ("HM2-NAT-MIB", "hm2MasqIfmRowStatus"),
        ("HM2-NAT-MIB", "hm2MasqStatsPckCount"),
        ("HM2-NAT-MIB", "hm2MasqStatsPckSize"),
        ("HM2-NAT-MIB", "hm2MasqStatsLastApplied"),
        ("HM2-NAT-MIB", "hm2MasqStatsTotalPck"),
        ("HM2-NAT-MIB", "hm2MasqStatsTotalPckSize"),
        ("HM2-NAT-MIB", "hm2MasqStatsTotalPckDenDrop"),
        ("HM2-NAT-MIB", "hm2MasqStatsTotalPckAccepted"),
        ("HM2-NAT-MIB", "hm2DoubleNatIfMappingRuleCount"),
        ("HM2-NAT-MIB", "hm2DoubleNatRulePendingActions"),
        ("HM2-NAT-MIB", "hm2DoubleNatCommitPendingActions"),
        ("HM2-NAT-MIB", "hm2DoubleNatRuleCount"),
        ("HM2-NAT-MIB", "hm2DonatRuleIndex"),
        ("HM2-NAT-MIB", "hm2DonatLocalInternalIp"),
        ("HM2-NAT-MIB", "hm2DonatLocalExternalIp"),
        ("HM2-NAT-MIB", "hm2DonatRemoteInternalIp"),
        ("HM2-NAT-MIB", "hm2DonatRemoteExternalIp"),
        ("HM2-NAT-MIB", "hm2DonatRuleParams"),
        ("HM2-NAT-MIB", "hm2DonatLog"),
        ("HM2-NAT-MIB", "hm2DonatTrap"),
        ("HM2-NAT-MIB", "hm2DonatDescription"),
        ("HM2-NAT-MIB", "hm2DonatIfmPriority"),
        ("HM2-NAT-MIB", "hm2DonatIfmRowStatus"),
        ("HM2-NAT-MIB", "hm2DonatRowStatus"),
        ("HM2-NAT-MIB", "hm2DonatStatsPckCount"),
        ("HM2-NAT-MIB", "hm2DonatStatsPckSize"),
        ("HM2-NAT-MIB", "hm2DonatStatsLastApplied"),
        ("HM2-NAT-MIB", "hm2DonatStatsTotalPck"),
        ("HM2-NAT-MIB", "hm2DonatStatsTotalPckSize"),
        ("HM2-NAT-MIB", "hm2DonatStatsTotalPckDenDrop"),
        ("HM2-NAT-MIB", "hm2DonatStatsTotalPckAcc"))
)
if mibBuilder.loadTexts:
    hm2NatGeneralGroup.setStatus("current")


# Notification objects

hm2DnatRuleAppliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 1)
)
hm2DnatRuleAppliedTrap.setObjects(
    ("HM2-NAT-MIB", "hm2DnatRuleIndex")
)
if mibBuilder.loadTexts:
    hm2DnatRuleAppliedTrap.setStatus(
        "current"
    )

hm2DnatRuleAppliedAndLoggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 2)
)
hm2DnatRuleAppliedAndLoggedTrap.setObjects(
    ("HM2-NAT-MIB", "hm2DnatRuleIndex")
)
if mibBuilder.loadTexts:
    hm2DnatRuleAppliedAndLoggedTrap.setStatus(
        "current"
    )

hm21to1RuleAppliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 5)
)
hm21to1RuleAppliedTrap.setObjects(
    ("HM2-NAT-MIB", "hm21to1RuleIndex")
)
if mibBuilder.loadTexts:
    hm21to1RuleAppliedTrap.setStatus(
        "current"
    )

hm21to1RuleAppliedAndLoggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 6)
)
hm21to1RuleAppliedAndLoggedTrap.setObjects(
    ("HM2-NAT-MIB", "hm21to1RuleIndex")
)
if mibBuilder.loadTexts:
    hm21to1RuleAppliedAndLoggedTrap.setStatus(
        "current"
    )

hm2MasqRuleAppliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 7)
)
hm2MasqRuleAppliedTrap.setObjects(
    ("HM2-NAT-MIB", "hm2MasqRuleIndex")
)
if mibBuilder.loadTexts:
    hm2MasqRuleAppliedTrap.setStatus(
        "current"
    )

hm2MasqRuleAppliedAndLoggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 8)
)
hm2MasqRuleAppliedAndLoggedTrap.setObjects(
    ("HM2-NAT-MIB", "hm2MasqRuleIndex")
)
if mibBuilder.loadTexts:
    hm2MasqRuleAppliedAndLoggedTrap.setStatus(
        "current"
    )

hm2DonatRuleAppliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 9)
)
hm2DonatRuleAppliedTrap.setObjects(
    ("HM2-NAT-MIB", "hm2DonatRuleIndex")
)
if mibBuilder.loadTexts:
    hm2DonatRuleAppliedTrap.setStatus(
        "current"
    )

hm2DonatRuleAppliedAndLoggedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 0, 10)
)
hm2DonatRuleAppliedAndLoggedTrap.setObjects(
    ("HM2-NAT-MIB", "hm2DonatRuleIndex")
)
if mibBuilder.loadTexts:
    hm2DonatRuleAppliedAndLoggedTrap.setStatus(
        "current"
    )


# Notifications groups

hm2NatNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 2, 2, 2)
)
hm2NatNotificationsGroup.setObjects(
      *(("HM2-NAT-MIB", "hm2DnatRuleAppliedTrap"),
        ("HM2-NAT-MIB", "hm2DnatRuleAppliedAndLoggedTrap"),
        ("HM2-NAT-MIB", "hm21to1RuleAppliedTrap"),
        ("HM2-NAT-MIB", "hm21to1RuleAppliedAndLoggedTrap"),
        ("HM2-NAT-MIB", "hm2MasqRuleAppliedTrap"),
        ("HM2-NAT-MIB", "hm2MasqRuleAppliedAndLoggedTrap"),
        ("HM2-NAT-MIB", "hm2DonatRuleAppliedTrap"),
        ("HM2-NAT-MIB", "hm2DonatRuleAppliedAndLoggedTrap"))
)
if mibBuilder.loadTexts:
    hm2NatNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hm2NatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 248, 11, 80, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hm2NatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-NAT-MIB",
    **{"hm2NatMib": hm2NatMib,
       "hm2NatNotifications": hm2NatNotifications,
       "hm2DnatRuleAppliedTrap": hm2DnatRuleAppliedTrap,
       "hm2DnatRuleAppliedAndLoggedTrap": hm2DnatRuleAppliedAndLoggedTrap,
       "hm21to1RuleAppliedTrap": hm21to1RuleAppliedTrap,
       "hm21to1RuleAppliedAndLoggedTrap": hm21to1RuleAppliedAndLoggedTrap,
       "hm2MasqRuleAppliedTrap": hm2MasqRuleAppliedTrap,
       "hm2MasqRuleAppliedAndLoggedTrap": hm2MasqRuleAppliedAndLoggedTrap,
       "hm2DonatRuleAppliedTrap": hm2DonatRuleAppliedTrap,
       "hm2DonatRuleAppliedAndLoggedTrap": hm2DonatRuleAppliedAndLoggedTrap,
       "hm2NatObjects": hm2NatObjects,
       "hm2NatGeneralSettings": hm2NatGeneralSettings,
       "hm2DnatMaxRules": hm2DnatMaxRules,
       "hm2OneToOneNatMaxRules": hm2OneToOneNatMaxRules,
       "hm2MasqMaxRules": hm2MasqMaxRules,
       "hm2DoubleNatMaxRules": hm2DoubleNatMaxRules,
       "hm2NatResetStatistics": hm2NatResetStatistics,
       "hm2Dnat": hm2Dnat,
       "hm2DnatRules": hm2DnatRules,
       "hm2DnatRulesObjects": hm2DnatRulesObjects,
       "hm2DnatRuleCount": hm2DnatRuleCount,
       "hm2DnatIfMappingRuleCount": hm2DnatIfMappingRuleCount,
       "hm2DnatRulePendingActions": hm2DnatRulePendingActions,
       "hm2DnatCommitPendingActions": hm2DnatCommitPendingActions,
       "hm2DnatRulesTables": hm2DnatRulesTables,
       "hm2DnatRuleTable": hm2DnatRuleTable,
       "hm2DnatRuleEntry": hm2DnatRuleEntry,
       "hm2DnatRuleIndex": hm2DnatRuleIndex,
       "hm2DnatSourceAddress": hm2DnatSourceAddress,
       "hm2DnatSourcePort": hm2DnatSourcePort,
       "hm2DnatTargetAddress": hm2DnatTargetAddress,
       "hm2DnatTargetPort": hm2DnatTargetPort,
       "hm2DnatNewTargetAddress": hm2DnatNewTargetAddress,
       "hm2DnatNewTargetPort": hm2DnatNewTargetPort,
       "hm2DnatProto": hm2DnatProto,
       "hm2DnatRuleParams": hm2DnatRuleParams,
       "hm2DnatLog": hm2DnatLog,
       "hm2DnatTrap": hm2DnatTrap,
       "hm2DnatRowStatus": hm2DnatRowStatus,
       "hm2DnatDescription": hm2DnatDescription,
       "hm2DnatRuleIfMappingTable": hm2DnatRuleIfMappingTable,
       "hm2DnatRuleIfMappingEntry": hm2DnatRuleIfMappingEntry,
       "hm2DnatIfmRuleIndex": hm2DnatIfmRuleIndex,
       "hm2DnatIfmDirection": hm2DnatIfmDirection,
       "hm2DnatIfmPriority": hm2DnatIfmPriority,
       "hm2DnatIfmInterface": hm2DnatIfmInterface,
       "hm2DnatIfmRowStatus": hm2DnatIfmRowStatus,
       "hm2DnatStats": hm2DnatStats,
       "hm2DnatGlobalStats": hm2DnatGlobalStats,
       "hm2DnatStatsTotalPck": hm2DnatStatsTotalPck,
       "hm2DnatStatsTotalPckSize": hm2DnatStatsTotalPckSize,
       "hm2DnatStatsTotalPckDenDrop": hm2DnatStatsTotalPckDenDrop,
       "hm2DnatStatsTotalPckAccepted": hm2DnatStatsTotalPckAccepted,
       "hm2DnatRuleStats": hm2DnatRuleStats,
       "hm2DnatStatsRuleTable": hm2DnatStatsRuleTable,
       "hm2DnatStatsRuleTableEntry": hm2DnatStatsRuleTableEntry,
       "hm2DnatStatsPckCount": hm2DnatStatsPckCount,
       "hm2DnatStatsPckSize": hm2DnatStatsPckSize,
       "hm2DnatStatsLastApplied": hm2DnatStatsLastApplied,
       "hm21to1": hm21to1,
       "hm21to1RuleObjects": hm21to1RuleObjects,
       "hm21to1RuleCount": hm21to1RuleCount,
       "hm21to1IfMappingRuleCount": hm21to1IfMappingRuleCount,
       "hm21to1RulePendingActions": hm21to1RulePendingActions,
       "hm21to1CommitPendingActions": hm21to1CommitPendingActions,
       "hm21to1Alg": hm21to1Alg,
       "hm21to1PublicIntf": hm21to1PublicIntf,
       "hm21to1RuleTables": hm21to1RuleTables,
       "hm21to1RuleTable": hm21to1RuleTable,
       "hm21to1RuleEntry": hm21to1RuleEntry,
       "hm21to1RuleIndex": hm21to1RuleIndex,
       "hm21to1TargetAddress": hm21to1TargetAddress,
       "hm21to1NewTargetAddress": hm21to1NewTargetAddress,
       "hm21to1RuleParams": hm21to1RuleParams,
       "hm21to1Log": hm21to1Log,
       "hm21to1Trap": hm21to1Trap,
       "hm21to1RowStatus": hm21to1RowStatus,
       "hm21to1Description": hm21to1Description,
       "hm21to1IngressIntf": hm21to1IngressIntf,
       "hm21to1EgressIntf": hm21to1EgressIntf,
       "hm21to1Priority": hm21to1Priority,
       "hm21to1StorageType": hm21to1StorageType,
       "hm21to1Stats": hm21to1Stats,
       "hm21to1GeneralStats": hm21to1GeneralStats,
       "hm21to1StatsTotalPck": hm21to1StatsTotalPck,
       "hm21to1StatsTotalPckSize": hm21to1StatsTotalPckSize,
       "hm21to1StatsTotalPckDenDrop": hm21to1StatsTotalPckDenDrop,
       "hm21to1StatsTotalPckAccepted": hm21to1StatsTotalPckAccepted,
       "hm21to1StatsTables": hm21to1StatsTables,
       "hm21to1StatsRuleTable": hm21to1StatsRuleTable,
       "hm21to1StatsRuleTableEntry": hm21to1StatsRuleTableEntry,
       "hm21to1StatsPckCount": hm21to1StatsPckCount,
       "hm21to1StatsPckSize": hm21to1StatsPckSize,
       "hm21to1StatsLastApplied": hm21to1StatsLastApplied,
       "hm2Masquerading": hm2Masquerading,
       "hm2MasqRuleObjects": hm2MasqRuleObjects,
       "hm2MasqRuleCount": hm2MasqRuleCount,
       "hm2MasqIfMappingRuleCount": hm2MasqIfMappingRuleCount,
       "hm2MasqRulePendingActions": hm2MasqRulePendingActions,
       "hm2MasqCommitPendingActions": hm2MasqCommitPendingActions,
       "hm2MasqRuleTables": hm2MasqRuleTables,
       "hm2MasqRuleTable": hm2MasqRuleTable,
       "hm2MasqRuleEntry": hm2MasqRuleEntry,
       "hm2MasqRuleIndex": hm2MasqRuleIndex,
       "hm2MasqSourceAddress": hm2MasqSourceAddress,
       "hm2MasqSourcePort": hm2MasqSourcePort,
       "hm2MasqProto": hm2MasqProto,
       "hm2MasqRuleParams": hm2MasqRuleParams,
       "hm2MasqLog": hm2MasqLog,
       "hm2MasqTrap": hm2MasqTrap,
       "hm2MasqRowStatus": hm2MasqRowStatus,
       "hm2MasqDescription": hm2MasqDescription,
       "hm2MasqIpsecExempt": hm2MasqIpsecExempt,
       "hm2MasqRuleIfMappingTable": hm2MasqRuleIfMappingTable,
       "hm2MasqRuleIfMappingEntry": hm2MasqRuleIfMappingEntry,
       "hm2MasqIfmRuleIndex": hm2MasqIfmRuleIndex,
       "hm2MasqIfmDirection": hm2MasqIfmDirection,
       "hm2MasqIfmPriority": hm2MasqIfmPriority,
       "hm2MasqIfmInterface": hm2MasqIfmInterface,
       "hm2MasqIfmRowStatus": hm2MasqIfmRowStatus,
       "hm2MasqStats": hm2MasqStats,
       "hm2MasqGeneralStats": hm2MasqGeneralStats,
       "hm2MasqStatsTotalPck": hm2MasqStatsTotalPck,
       "hm2MasqStatsTotalPckSize": hm2MasqStatsTotalPckSize,
       "hm2MasqStatsTotalPckDenDrop": hm2MasqStatsTotalPckDenDrop,
       "hm2MasqStatsTotalPckAccepted": hm2MasqStatsTotalPckAccepted,
       "hm2MasqStatsRuleTables": hm2MasqStatsRuleTables,
       "hm2MasqStatsRuleTable": hm2MasqStatsRuleTable,
       "hm2MasqStatsRuleTableEntry": hm2MasqStatsRuleTableEntry,
       "hm2MasqStatsPckCount": hm2MasqStatsPckCount,
       "hm2MasqStatsPckSize": hm2MasqStatsPckSize,
       "hm2MasqStatsLastApplied": hm2MasqStatsLastApplied,
       "hm2DoubleNat": hm2DoubleNat,
       "hm2DoubleNatRuleObjects": hm2DoubleNatRuleObjects,
       "hm2DoubleNatRuleCount": hm2DoubleNatRuleCount,
       "hm2DoubleNatIfMappingRuleCount": hm2DoubleNatIfMappingRuleCount,
       "hm2DoubleNatRulePendingActions": hm2DoubleNatRulePendingActions,
       "hm2DoubleNatCommitPendingActions": hm2DoubleNatCommitPendingActions,
       "hm2DoubleNatRuleTables": hm2DoubleNatRuleTables,
       "hm2DoubleNatRuleTable": hm2DoubleNatRuleTable,
       "hm2DoubleNatRuleEntry": hm2DoubleNatRuleEntry,
       "hm2DonatRuleIndex": hm2DonatRuleIndex,
       "hm2DonatLocalInternalIp": hm2DonatLocalInternalIp,
       "hm2DonatLocalExternalIp": hm2DonatLocalExternalIp,
       "hm2DonatRemoteInternalIp": hm2DonatRemoteInternalIp,
       "hm2DonatRemoteExternalIp": hm2DonatRemoteExternalIp,
       "hm2DonatRuleParams": hm2DonatRuleParams,
       "hm2DonatLog": hm2DonatLog,
       "hm2DonatTrap": hm2DonatTrap,
       "hm2DonatRowStatus": hm2DonatRowStatus,
       "hm2DonatDescription": hm2DonatDescription,
       "hm2DonatRuleIfMappingTable": hm2DonatRuleIfMappingTable,
       "hm2DonatRuleIfMappingEntry": hm2DonatRuleIfMappingEntry,
       "hm2DonatIfmRuleIndex": hm2DonatIfmRuleIndex,
       "hm2DonatIfmDirection": hm2DonatIfmDirection,
       "hm2DonatIfmPriority": hm2DonatIfmPriority,
       "hm2DonatIfmInterface": hm2DonatIfmInterface,
       "hm2DonatIfmRowStatus": hm2DonatIfmRowStatus,
       "hm2DonatStats": hm2DonatStats,
       "hm2DonatGeneralStats": hm2DonatGeneralStats,
       "hm2DonatStatsTotalPck": hm2DonatStatsTotalPck,
       "hm2DonatStatsTotalPckSize": hm2DonatStatsTotalPckSize,
       "hm2DonatStatsTotalPckDenDrop": hm2DonatStatsTotalPckDenDrop,
       "hm2DonatStatsTotalPckAcc": hm2DonatStatsTotalPckAcc,
       "hm2DonatStatsRuleTables": hm2DonatStatsRuleTables,
       "hm2DonatStatsRuleTable": hm2DonatStatsRuleTable,
       "hm2DonatStatsRuleTableEntry": hm2DonatStatsRuleTableEntry,
       "hm2DonatStatsPckCount": hm2DonatStatsPckCount,
       "hm2DonatStatsPckSize": hm2DonatStatsPckSize,
       "hm2DonatStatsLastApplied": hm2DonatStatsLastApplied,
       "hm2NatConformance": hm2NatConformance,
       "hm2NatCompliances": hm2NatCompliances,
       "hm2NatCompliance": hm2NatCompliance,
       "hm2NatGroups": hm2NatGroups,
       "hm2NatGeneralGroup": hm2NatGeneralGroup,
       "hm2NatNotificationsGroup": hm2NatNotificationsGroup}
)
