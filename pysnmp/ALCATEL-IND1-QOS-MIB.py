# SNMP MIB module (ALCATEL-IND1-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:53 2024
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

(softentIND1QoS,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1QoS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alaQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaQoSMIBObjects_ObjectIdentity = ObjectIdentity
alaQoSMIBObjects = _AlaQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1)
)
if mibBuilder.loadTexts:
    alaQoSMIBObjects.setStatus("current")
_AlaQoSRuleTable_Object = MibTable
alaQoSRuleTable = _AlaQoSRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaQoSRuleTable.setStatus("current")
_AlaQoSRuleEntry_Object = MibTableRow
alaQoSRuleEntry = _AlaQoSRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1)
)
alaQoSRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSRuleEntry.setStatus("current")


class _AlaQoSRuleName_Type(DisplayString):
    """Custom type alaQoSRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleName_Type.__name__ = "DisplayString"
_AlaQoSRuleName_Object = MibTableColumn
alaQoSRuleName = _AlaQoSRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 1),
    _AlaQoSRuleName_Type()
)
alaQoSRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSRuleName.setStatus("current")


class _AlaQoSRuleEnabled_Type(Integer32):
    """Custom type alaQoSRuleEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSRuleEnabled_Type.__name__ = "Integer32"
_AlaQoSRuleEnabled_Object = MibTableColumn
alaQoSRuleEnabled = _AlaQoSRuleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 2),
    _AlaQoSRuleEnabled_Type()
)
alaQoSRuleEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleEnabled.setStatus("current")


class _AlaQoSRuleSource_Type(Integer32):
    """Custom type alaQoSRuleSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSRuleSource_Type.__name__ = "Integer32"
_AlaQoSRuleSource_Object = MibTableColumn
alaQoSRuleSource = _AlaQoSRuleSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 3),
    _AlaQoSRuleSource_Type()
)
alaQoSRuleSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleSource.setStatus("current")


class _AlaQoSRulePrecedence_Type(Integer32):
    """Custom type alaQoSRulePrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSRulePrecedence_Type.__name__ = "Integer32"
_AlaQoSRulePrecedence_Object = MibTableColumn
alaQoSRulePrecedence = _AlaQoSRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 4),
    _AlaQoSRulePrecedence_Type()
)
alaQoSRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRulePrecedence.setStatus("current")


class _AlaQoSRuleCondition_Type(DisplayString):
    """Custom type alaQoSRuleCondition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleCondition_Type.__name__ = "DisplayString"
_AlaQoSRuleCondition_Object = MibTableColumn
alaQoSRuleCondition = _AlaQoSRuleCondition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 5),
    _AlaQoSRuleCondition_Type()
)
alaQoSRuleCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleCondition.setStatus("current")


class _AlaQoSRuleAction_Type(DisplayString):
    """Custom type alaQoSRuleAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleAction_Type.__name__ = "DisplayString"
_AlaQoSRuleAction_Object = MibTableColumn
alaQoSRuleAction = _AlaQoSRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 6),
    _AlaQoSRuleAction_Type()
)
alaQoSRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleAction.setStatus("current")


class _AlaQoSRuleReflexive_Type(Integer32):
    """Custom type alaQoSRuleReflexive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSRuleReflexive_Type.__name__ = "Integer32"
_AlaQoSRuleReflexive_Object = MibTableColumn
alaQoSRuleReflexive = _AlaQoSRuleReflexive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 7),
    _AlaQoSRuleReflexive_Type()
)
alaQoSRuleReflexive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleReflexive.setStatus("current")


class _AlaQoSRuleSave_Type(Integer32):
    """Custom type alaQoSRuleSave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSRuleSave_Type.__name__ = "Integer32"
_AlaQoSRuleSave_Object = MibTableColumn
alaQoSRuleSave = _AlaQoSRuleSave_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 8),
    _AlaQoSRuleSave_Type()
)
alaQoSRuleSave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleSave.setStatus("current")


class _AlaQoSRuleLog_Type(Integer32):
    """Custom type alaQoSRuleLog based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSRuleLog_Type.__name__ = "Integer32"
_AlaQoSRuleLog_Object = MibTableColumn
alaQoSRuleLog = _AlaQoSRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 9),
    _AlaQoSRuleLog_Type()
)
alaQoSRuleLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleLog.setStatus("current")
_AlaQoSRuleMatches_Type = Counter32
_AlaQoSRuleMatches_Object = MibTableColumn
alaQoSRuleMatches = _AlaQoSRuleMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 10),
    _AlaQoSRuleMatches_Type()
)
alaQoSRuleMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleMatches.setStatus("current")


class _AlaQoSRuleEnforced_Type(Integer32):
    """Custom type alaQoSRuleEnforced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSRuleEnforced_Type.__name__ = "Integer32"
_AlaQoSRuleEnforced_Object = MibTableColumn
alaQoSRuleEnforced = _AlaQoSRuleEnforced_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 11),
    _AlaQoSRuleEnforced_Type()
)
alaQoSRuleEnforced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleEnforced.setStatus("current")


class _AlaQoSRuleActive_Type(Integer32):
    """Custom type alaQoSRuleActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSRuleActive_Type.__name__ = "Integer32"
_AlaQoSRuleActive_Object = MibTableColumn
alaQoSRuleActive = _AlaQoSRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 12),
    _AlaQoSRuleActive_Type()
)
alaQoSRuleActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleActive.setStatus("current")
_AlaQoSRuleRowStatus_Type = RowStatus
_AlaQoSRuleRowStatus_Object = MibTableColumn
alaQoSRuleRowStatus = _AlaQoSRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 13),
    _AlaQoSRuleRowStatus_Type()
)
alaQoSRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleRowStatus.setStatus("current")


class _AlaQoSRuleValidityPeriod_Type(DisplayString):
    """Custom type alaQoSRuleValidityPeriod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleValidityPeriod_Type.__name__ = "DisplayString"
_AlaQoSRuleValidityPeriod_Object = MibTableColumn
alaQoSRuleValidityPeriod = _AlaQoSRuleValidityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 14),
    _AlaQoSRuleValidityPeriod_Type()
)
alaQoSRuleValidityPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleValidityPeriod.setStatus("current")


class _AlaQoSRuleValidityPeriodStatus_Type(Integer32):
    """Custom type alaQoSRuleValidityPeriodStatus based on Integer32"""
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


_AlaQoSRuleValidityPeriodStatus_Type.__name__ = "Integer32"
_AlaQoSRuleValidityPeriodStatus_Object = MibTableColumn
alaQoSRuleValidityPeriodStatus = _AlaQoSRuleValidityPeriodStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 15),
    _AlaQoSRuleValidityPeriodStatus_Type()
)
alaQoSRuleValidityPeriodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleValidityPeriodStatus.setStatus("current")


class _AlaQoSRuleLogInterval_Type(Integer32):
    """Custom type alaQoSRuleLogInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaQoSRuleLogInterval_Type.__name__ = "Integer32"
_AlaQoSRuleLogInterval_Object = MibTableColumn
alaQoSRuleLogInterval = _AlaQoSRuleLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 16),
    _AlaQoSRuleLogInterval_Type()
)
alaQoSRuleLogInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleLogInterval.setStatus("current")


class _AlaQoSRuleCountType_Type(Integer32):
    """Custom type alaQoSRuleCountType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 2),
          ("packets", 1))
    )


_AlaQoSRuleCountType_Type.__name__ = "Integer32"
_AlaQoSRuleCountType_Object = MibTableColumn
alaQoSRuleCountType = _AlaQoSRuleCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 17),
    _AlaQoSRuleCountType_Type()
)
alaQoSRuleCountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleCountType.setStatus("current")
_AlaQoSRulePacketCount_Type = Counter64
_AlaQoSRulePacketCount_Object = MibTableColumn
alaQoSRulePacketCount = _AlaQoSRulePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 18),
    _AlaQoSRulePacketCount_Type()
)
alaQoSRulePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRulePacketCount.setStatus("current")
_AlaQoSRuleByteCount_Type = Counter64
_AlaQoSRuleByteCount_Object = MibTableColumn
alaQoSRuleByteCount = _AlaQoSRuleByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 19),
    _AlaQoSRuleByteCount_Type()
)
alaQoSRuleByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleByteCount.setStatus("current")
_AlaQoSRuleExcessPacketCount_Type = Counter64
_AlaQoSRuleExcessPacketCount_Object = MibTableColumn
alaQoSRuleExcessPacketCount = _AlaQoSRuleExcessPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 20),
    _AlaQoSRuleExcessPacketCount_Type()
)
alaQoSRuleExcessPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleExcessPacketCount.setStatus("current")
_AlaQoSRuleExcessByteCount_Type = Counter64
_AlaQoSRuleExcessByteCount_Object = MibTableColumn
alaQoSRuleExcessByteCount = _AlaQoSRuleExcessByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 21),
    _AlaQoSRuleExcessByteCount_Type()
)
alaQoSRuleExcessByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleExcessByteCount.setStatus("current")
_AlaQoSRuleType_Type = Integer32
_AlaQoSRuleType_Object = MibTableColumn
alaQoSRuleType = _AlaQoSRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 22),
    _AlaQoSRuleType_Type()
)
alaQoSRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleType.setStatus("current")


class _AlaQoSRuleTrapEvents_Type(Integer32):
    """Custom type alaQoSRuleTrapEvents based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSRuleTrapEvents_Type.__name__ = "Integer32"
_AlaQoSRuleTrapEvents_Object = MibTableColumn
alaQoSRuleTrapEvents = _AlaQoSRuleTrapEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 23),
    _AlaQoSRuleTrapEvents_Type()
)
alaQoSRuleTrapEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleTrapEvents.setStatus("current")


class _AlaQoSRuleDefaultList_Type(Integer32):
    """Custom type alaQoSRuleDefaultList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSRuleDefaultList_Type.__name__ = "Integer32"
_AlaQoSRuleDefaultList_Object = MibTableColumn
alaQoSRuleDefaultList = _AlaQoSRuleDefaultList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 24),
    _AlaQoSRuleDefaultList_Type()
)
alaQoSRuleDefaultList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleDefaultList.setStatus("current")
_AlaQoSRuleGreenCount_Type = Counter64
_AlaQoSRuleGreenCount_Object = MibTableColumn
alaQoSRuleGreenCount = _AlaQoSRuleGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 25),
    _AlaQoSRuleGreenCount_Type()
)
alaQoSRuleGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGreenCount.setStatus("current")
_AlaQoSRuleYellowCount_Type = Counter64
_AlaQoSRuleYellowCount_Object = MibTableColumn
alaQoSRuleYellowCount = _AlaQoSRuleYellowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 26),
    _AlaQoSRuleYellowCount_Type()
)
alaQoSRuleYellowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleYellowCount.setStatus("current")
_AlaQoSRuleRedCount_Type = Counter64
_AlaQoSRuleRedCount_Object = MibTableColumn
alaQoSRuleRedCount = _AlaQoSRuleRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 27),
    _AlaQoSRuleRedCount_Type()
)
alaQoSRuleRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleRedCount.setStatus("current")
_AlaQoSRuleNonGreenCount_Type = Counter64
_AlaQoSRuleNonGreenCount_Object = MibTableColumn
alaQoSRuleNonGreenCount = _AlaQoSRuleNonGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 28),
    _AlaQoSRuleNonGreenCount_Type()
)
alaQoSRuleNonGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleNonGreenCount.setStatus("current")
_AlaQoSRuleNonRedCount_Type = Counter64
_AlaQoSRuleNonRedCount_Object = MibTableColumn
alaQoSRuleNonRedCount = _AlaQoSRuleNonRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 1, 1, 29),
    _AlaQoSRuleNonRedCount_Type()
)
alaQoSRuleNonRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleNonRedCount.setStatus("current")
_AlaQoSAppliedRuleTable_Object = MibTable
alaQoSAppliedRuleTable = _AlaQoSAppliedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleTable.setStatus("current")
_AlaQoSAppliedRuleEntry_Object = MibTableRow
alaQoSAppliedRuleEntry = _AlaQoSAppliedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1)
)
alaQoSAppliedRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleEntry.setStatus("current")


class _AlaQoSAppliedRuleName_Type(DisplayString):
    """Custom type alaQoSAppliedRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleName_Type.__name__ = "DisplayString"
_AlaQoSAppliedRuleName_Object = MibTableColumn
alaQoSAppliedRuleName = _AlaQoSAppliedRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 1),
    _AlaQoSAppliedRuleName_Type()
)
alaQoSAppliedRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleName.setStatus("current")


class _AlaQoSAppliedRuleEnabled_Type(Integer32):
    """Custom type alaQoSAppliedRuleEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSAppliedRuleEnabled_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleEnabled_Object = MibTableColumn
alaQoSAppliedRuleEnabled = _AlaQoSAppliedRuleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 2),
    _AlaQoSAppliedRuleEnabled_Type()
)
alaQoSAppliedRuleEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleEnabled.setStatus("current")


class _AlaQoSAppliedRuleSource_Type(Integer32):
    """Custom type alaQoSAppliedRuleSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedRuleSource_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleSource_Object = MibTableColumn
alaQoSAppliedRuleSource = _AlaQoSAppliedRuleSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 3),
    _AlaQoSAppliedRuleSource_Type()
)
alaQoSAppliedRuleSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleSource.setStatus("current")


class _AlaQoSAppliedRulePrecedence_Type(Integer32):
    """Custom type alaQoSAppliedRulePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedRulePrecedence_Type.__name__ = "Integer32"
_AlaQoSAppliedRulePrecedence_Object = MibTableColumn
alaQoSAppliedRulePrecedence = _AlaQoSAppliedRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 4),
    _AlaQoSAppliedRulePrecedence_Type()
)
alaQoSAppliedRulePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRulePrecedence.setStatus("current")


class _AlaQoSAppliedRuleCondition_Type(DisplayString):
    """Custom type alaQoSAppliedRuleCondition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleCondition_Type.__name__ = "DisplayString"
_AlaQoSAppliedRuleCondition_Object = MibTableColumn
alaQoSAppliedRuleCondition = _AlaQoSAppliedRuleCondition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 5),
    _AlaQoSAppliedRuleCondition_Type()
)
alaQoSAppliedRuleCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleCondition.setStatus("current")


class _AlaQoSAppliedRuleAction_Type(DisplayString):
    """Custom type alaQoSAppliedRuleAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleAction_Type.__name__ = "DisplayString"
_AlaQoSAppliedRuleAction_Object = MibTableColumn
alaQoSAppliedRuleAction = _AlaQoSAppliedRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 6),
    _AlaQoSAppliedRuleAction_Type()
)
alaQoSAppliedRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleAction.setStatus("current")


class _AlaQoSAppliedRuleReflexive_Type(Integer32):
    """Custom type alaQoSAppliedRuleReflexive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedRuleReflexive_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleReflexive_Object = MibTableColumn
alaQoSAppliedRuleReflexive = _AlaQoSAppliedRuleReflexive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 7),
    _AlaQoSAppliedRuleReflexive_Type()
)
alaQoSAppliedRuleReflexive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleReflexive.setStatus("current")


class _AlaQoSAppliedRuleSave_Type(Integer32):
    """Custom type alaQoSAppliedRuleSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedRuleSave_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleSave_Object = MibTableColumn
alaQoSAppliedRuleSave = _AlaQoSAppliedRuleSave_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 8),
    _AlaQoSAppliedRuleSave_Type()
)
alaQoSAppliedRuleSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleSave.setStatus("current")


class _AlaQoSAppliedRuleLog_Type(Integer32):
    """Custom type alaQoSAppliedRuleLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedRuleLog_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleLog_Object = MibTableColumn
alaQoSAppliedRuleLog = _AlaQoSAppliedRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 9),
    _AlaQoSAppliedRuleLog_Type()
)
alaQoSAppliedRuleLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleLog.setStatus("current")
_AlaQoSAppliedRuleMatches_Type = Counter32
_AlaQoSAppliedRuleMatches_Object = MibTableColumn
alaQoSAppliedRuleMatches = _AlaQoSAppliedRuleMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 10),
    _AlaQoSAppliedRuleMatches_Type()
)
alaQoSAppliedRuleMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleMatches.setStatus("current")


class _AlaQoSAppliedRuleEnforced_Type(Integer32):
    """Custom type alaQoSAppliedRuleEnforced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedRuleEnforced_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleEnforced_Object = MibTableColumn
alaQoSAppliedRuleEnforced = _AlaQoSAppliedRuleEnforced_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 11),
    _AlaQoSAppliedRuleEnforced_Type()
)
alaQoSAppliedRuleEnforced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleEnforced.setStatus("current")


class _AlaQoSAppliedRuleActive_Type(Integer32):
    """Custom type alaQoSAppliedRuleActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedRuleActive_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleActive_Object = MibTableColumn
alaQoSAppliedRuleActive = _AlaQoSAppliedRuleActive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 12),
    _AlaQoSAppliedRuleActive_Type()
)
alaQoSAppliedRuleActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleActive.setStatus("current")
_AlaQoSAppliedRuleRowStatus_Type = RowStatus
_AlaQoSAppliedRuleRowStatus_Object = MibTableColumn
alaQoSAppliedRuleRowStatus = _AlaQoSAppliedRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 13),
    _AlaQoSAppliedRuleRowStatus_Type()
)
alaQoSAppliedRuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleRowStatus.setStatus("current")


class _AlaQoSAppliedRuleValidityPeriod_Type(DisplayString):
    """Custom type alaQoSAppliedRuleValidityPeriod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleValidityPeriod_Type.__name__ = "DisplayString"
_AlaQoSAppliedRuleValidityPeriod_Object = MibTableColumn
alaQoSAppliedRuleValidityPeriod = _AlaQoSAppliedRuleValidityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 14),
    _AlaQoSAppliedRuleValidityPeriod_Type()
)
alaQoSAppliedRuleValidityPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleValidityPeriod.setStatus("current")


class _AlaQoSAppliedRuleValidityPeriodStatus_Type(Integer32):
    """Custom type alaQoSAppliedRuleValidityPeriodStatus based on Integer32"""
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


_AlaQoSAppliedRuleValidityPeriodStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleValidityPeriodStatus_Object = MibTableColumn
alaQoSAppliedRuleValidityPeriodStatus = _AlaQoSAppliedRuleValidityPeriodStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 15),
    _AlaQoSAppliedRuleValidityPeriodStatus_Type()
)
alaQoSAppliedRuleValidityPeriodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleValidityPeriodStatus.setStatus("current")


class _AlaQoSAppliedRuleLogInterval_Type(Integer32):
    """Custom type alaQoSAppliedRuleLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaQoSAppliedRuleLogInterval_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleLogInterval_Object = MibTableColumn
alaQoSAppliedRuleLogInterval = _AlaQoSAppliedRuleLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 16),
    _AlaQoSAppliedRuleLogInterval_Type()
)
alaQoSAppliedRuleLogInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleLogInterval.setStatus("current")


class _AlaQoSAppliedRuleCountType_Type(Integer32):
    """Custom type alaQoSAppliedRuleCountType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 2),
          ("packets", 1))
    )


_AlaQoSAppliedRuleCountType_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleCountType_Object = MibTableColumn
alaQoSAppliedRuleCountType = _AlaQoSAppliedRuleCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 17),
    _AlaQoSAppliedRuleCountType_Type()
)
alaQoSAppliedRuleCountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleCountType.setStatus("current")
_AlaQoSAppliedRulePacketCount_Type = Counter64
_AlaQoSAppliedRulePacketCount_Object = MibTableColumn
alaQoSAppliedRulePacketCount = _AlaQoSAppliedRulePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 18),
    _AlaQoSAppliedRulePacketCount_Type()
)
alaQoSAppliedRulePacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRulePacketCount.setStatus("current")
_AlaQoSAppliedRuleByteCount_Type = Counter64
_AlaQoSAppliedRuleByteCount_Object = MibTableColumn
alaQoSAppliedRuleByteCount = _AlaQoSAppliedRuleByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 19),
    _AlaQoSAppliedRuleByteCount_Type()
)
alaQoSAppliedRuleByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleByteCount.setStatus("current")
_AlaQoSAppliedRuleExcessPacketCount_Type = Counter64
_AlaQoSAppliedRuleExcessPacketCount_Object = MibTableColumn
alaQoSAppliedRuleExcessPacketCount = _AlaQoSAppliedRuleExcessPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 20),
    _AlaQoSAppliedRuleExcessPacketCount_Type()
)
alaQoSAppliedRuleExcessPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleExcessPacketCount.setStatus("current")
_AlaQoSAppliedRuleExcessByteCount_Type = Counter64
_AlaQoSAppliedRuleExcessByteCount_Object = MibTableColumn
alaQoSAppliedRuleExcessByteCount = _AlaQoSAppliedRuleExcessByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 21),
    _AlaQoSAppliedRuleExcessByteCount_Type()
)
alaQoSAppliedRuleExcessByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleExcessByteCount.setStatus("current")
_AlaQoSAppliedRuleType_Type = Integer32
_AlaQoSAppliedRuleType_Object = MibTableColumn
alaQoSAppliedRuleType = _AlaQoSAppliedRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 22),
    _AlaQoSAppliedRuleType_Type()
)
alaQoSAppliedRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleType.setStatus("current")


class _AlaQoSAppliedRuleTrapEvents_Type(Integer32):
    """Custom type alaQoSAppliedRuleTrapEvents based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedRuleTrapEvents_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleTrapEvents_Object = MibTableColumn
alaQoSAppliedRuleTrapEvents = _AlaQoSAppliedRuleTrapEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 23),
    _AlaQoSAppliedRuleTrapEvents_Type()
)
alaQoSAppliedRuleTrapEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleTrapEvents.setStatus("current")


class _AlaQoSAppliedRuleDefaultList_Type(Integer32):
    """Custom type alaQoSAppliedRuleDefaultList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedRuleDefaultList_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleDefaultList_Object = MibTableColumn
alaQoSAppliedRuleDefaultList = _AlaQoSAppliedRuleDefaultList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 24),
    _AlaQoSAppliedRuleDefaultList_Type()
)
alaQoSAppliedRuleDefaultList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleDefaultList.setStatus("current")
_AlaQoSAppliedRuleGreenCount_Type = Counter64
_AlaQoSAppliedRuleGreenCount_Object = MibTableColumn
alaQoSAppliedRuleGreenCount = _AlaQoSAppliedRuleGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 25),
    _AlaQoSAppliedRuleGreenCount_Type()
)
alaQoSAppliedRuleGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGreenCount.setStatus("current")
_AlaQoSAppliedRuleYellowCount_Type = Counter64
_AlaQoSAppliedRuleYellowCount_Object = MibTableColumn
alaQoSAppliedRuleYellowCount = _AlaQoSAppliedRuleYellowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 26),
    _AlaQoSAppliedRuleYellowCount_Type()
)
alaQoSAppliedRuleYellowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleYellowCount.setStatus("current")
_AlaQoSAppliedRuleRedCount_Type = Counter64
_AlaQoSAppliedRuleRedCount_Object = MibTableColumn
alaQoSAppliedRuleRedCount = _AlaQoSAppliedRuleRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 27),
    _AlaQoSAppliedRuleRedCount_Type()
)
alaQoSAppliedRuleRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleRedCount.setStatus("current")
_AlaQoSAppliedRuleNonGreenCount_Type = Counter64
_AlaQoSAppliedRuleNonGreenCount_Object = MibTableColumn
alaQoSAppliedRuleNonGreenCount = _AlaQoSAppliedRuleNonGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 28),
    _AlaQoSAppliedRuleNonGreenCount_Type()
)
alaQoSAppliedRuleNonGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleNonGreenCount.setStatus("current")
_AlaQoSAppliedRuleNonRedCount_Type = Counter64
_AlaQoSAppliedRuleNonRedCount_Object = MibTableColumn
alaQoSAppliedRuleNonRedCount = _AlaQoSAppliedRuleNonRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 2, 1, 29),
    _AlaQoSAppliedRuleNonRedCount_Type()
)
alaQoSAppliedRuleNonRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleNonRedCount.setStatus("current")
_AlaQoSConditionTable_Object = MibTable
alaQoSConditionTable = _AlaQoSConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaQoSConditionTable.setStatus("current")
_AlaQoSConditionEntry_Object = MibTableRow
alaQoSConditionEntry = _AlaQoSConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1)
)
alaQoSConditionEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSConditionName"),
)
if mibBuilder.loadTexts:
    alaQoSConditionEntry.setStatus("current")


class _AlaQoSConditionName_Type(DisplayString):
    """Custom type alaQoSConditionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionName_Type.__name__ = "DisplayString"
_AlaQoSConditionName_Object = MibTableColumn
alaQoSConditionName = _AlaQoSConditionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 1),
    _AlaQoSConditionName_Type()
)
alaQoSConditionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSConditionName.setStatus("current")


class _AlaQoSConditionSource_Type(Integer32):
    """Custom type alaQoSConditionSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSConditionSource_Type.__name__ = "Integer32"
_AlaQoSConditionSource_Object = MibTableColumn
alaQoSConditionSource = _AlaQoSConditionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 2),
    _AlaQoSConditionSource_Type()
)
alaQoSConditionSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSource.setStatus("current")


class _AlaQoSConditionSourceSlot_Type(Integer32):
    """Custom type alaQoSConditionSourceSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSConditionSourceSlot_Type.__name__ = "Integer32"
_AlaQoSConditionSourceSlot_Object = MibTableColumn
alaQoSConditionSourceSlot = _AlaQoSConditionSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 3),
    _AlaQoSConditionSourceSlot_Type()
)
alaQoSConditionSourceSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceSlot.setStatus("current")


class _AlaQoSConditionSourceSlotStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceSlotStatus based on Integer32"""
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


_AlaQoSConditionSourceSlotStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceSlotStatus_Object = MibTableColumn
alaQoSConditionSourceSlotStatus = _AlaQoSConditionSourceSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 4),
    _AlaQoSConditionSourceSlotStatus_Type()
)
alaQoSConditionSourceSlotStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceSlotStatus.setStatus("current")


class _AlaQoSConditionSourcePort_Type(Integer32):
    """Custom type alaQoSConditionSourcePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSConditionSourcePort_Type.__name__ = "Integer32"
_AlaQoSConditionSourcePort_Object = MibTableColumn
alaQoSConditionSourcePort = _AlaQoSConditionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 5),
    _AlaQoSConditionSourcePort_Type()
)
alaQoSConditionSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePort.setStatus("current")


class _AlaQoSConditionSourcePortGroup_Type(DisplayString):
    """Custom type alaQoSConditionSourcePortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourcePortGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionSourcePortGroup_Object = MibTableColumn
alaQoSConditionSourcePortGroup = _AlaQoSConditionSourcePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 6),
    _AlaQoSConditionSourcePortGroup_Type()
)
alaQoSConditionSourcePortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortGroup.setStatus("current")


class _AlaQoSConditionSourcePortGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourcePortGroupStatus based on Integer32"""
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


_AlaQoSConditionSourcePortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourcePortGroupStatus_Object = MibTableColumn
alaQoSConditionSourcePortGroupStatus = _AlaQoSConditionSourcePortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 7),
    _AlaQoSConditionSourcePortGroupStatus_Type()
)
alaQoSConditionSourcePortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortGroupStatus.setStatus("current")


class _AlaQoSConditionDestinationSlot_Type(Integer32):
    """Custom type alaQoSConditionDestinationSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSConditionDestinationSlot_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationSlot_Object = MibTableColumn
alaQoSConditionDestinationSlot = _AlaQoSConditionDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 8),
    _AlaQoSConditionDestinationSlot_Type()
)
alaQoSConditionDestinationSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationSlot.setStatus("current")


class _AlaQoSConditionDestinationSlotStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationSlotStatus based on Integer32"""
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


_AlaQoSConditionDestinationSlotStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationSlotStatus_Object = MibTableColumn
alaQoSConditionDestinationSlotStatus = _AlaQoSConditionDestinationSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 9),
    _AlaQoSConditionDestinationSlotStatus_Type()
)
alaQoSConditionDestinationSlotStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationSlotStatus.setStatus("current")


class _AlaQoSConditionDestinationPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSConditionDestinationPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationPort_Object = MibTableColumn
alaQoSConditionDestinationPort = _AlaQoSConditionDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 10),
    _AlaQoSConditionDestinationPort_Type()
)
alaQoSConditionDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPort.setStatus("current")


class _AlaQoSConditionDestinationPortGroup_Type(DisplayString):
    """Custom type alaQoSConditionDestinationPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionDestinationPortGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionDestinationPortGroup_Object = MibTableColumn
alaQoSConditionDestinationPortGroup = _AlaQoSConditionDestinationPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 11),
    _AlaQoSConditionDestinationPortGroup_Type()
)
alaQoSConditionDestinationPortGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPortGroup.setStatus("current")


class _AlaQoSConditionDestinationPortGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationPortGroupStatus based on Integer32"""
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


_AlaQoSConditionDestinationPortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationPortGroupStatus_Object = MibTableColumn
alaQoSConditionDestinationPortGroupStatus = _AlaQoSConditionDestinationPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 12),
    _AlaQoSConditionDestinationPortGroupStatus_Type()
)
alaQoSConditionDestinationPortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPortGroupStatus.setStatus("current")


class _AlaQoSConditionSourceInterfaceType_Type(Integer32):
    """Custom type alaQoSConditionSourceInterfaceType based on Integer32"""
    defaultValue = 1

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
        *(("aggregate", 7),
          ("ethernet", 1),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet10G", 6),
          ("ethernet1G", 5),
          ("wan", 2))
    )


_AlaQoSConditionSourceInterfaceType_Type.__name__ = "Integer32"
_AlaQoSConditionSourceInterfaceType_Object = MibTableColumn
alaQoSConditionSourceInterfaceType = _AlaQoSConditionSourceInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 13),
    _AlaQoSConditionSourceInterfaceType_Type()
)
alaQoSConditionSourceInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceInterfaceType.setStatus("current")


class _AlaQoSConditionSourceInterfaceTypeStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceInterfaceTypeStatus based on Integer32"""
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


_AlaQoSConditionSourceInterfaceTypeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceInterfaceTypeStatus_Object = MibTableColumn
alaQoSConditionSourceInterfaceTypeStatus = _AlaQoSConditionSourceInterfaceTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 14),
    _AlaQoSConditionSourceInterfaceTypeStatus_Type()
)
alaQoSConditionSourceInterfaceTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceInterfaceTypeStatus.setStatus("current")


class _AlaQoSConditionDestinationInterfaceType_Type(Integer32):
    """Custom type alaQoSConditionDestinationInterfaceType based on Integer32"""
    defaultValue = 1

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
        *(("aggregate", 7),
          ("ethernet", 1),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet10G", 6),
          ("ethernet1G", 5),
          ("wan", 2))
    )


_AlaQoSConditionDestinationInterfaceType_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationInterfaceType_Object = MibTableColumn
alaQoSConditionDestinationInterfaceType = _AlaQoSConditionDestinationInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 15),
    _AlaQoSConditionDestinationInterfaceType_Type()
)
alaQoSConditionDestinationInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationInterfaceType.setStatus("current")


class _AlaQoSConditionDestinationInterfaceTypeStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationInterfaceTypeStatus based on Integer32"""
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


_AlaQoSConditionDestinationInterfaceTypeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationInterfaceTypeStatus_Object = MibTableColumn
alaQoSConditionDestinationInterfaceTypeStatus = _AlaQoSConditionDestinationInterfaceTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 16),
    _AlaQoSConditionDestinationInterfaceTypeStatus_Type()
)
alaQoSConditionDestinationInterfaceTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationInterfaceTypeStatus.setStatus("current")


class _AlaQoSConditionSourceMacAddr_Type(MacAddress):
    """Custom type alaQoSConditionSourceMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSConditionSourceMacAddr_Object = MibTableColumn
alaQoSConditionSourceMacAddr = _AlaQoSConditionSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 17),
    _AlaQoSConditionSourceMacAddr_Type()
)
alaQoSConditionSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacAddr.setStatus("current")


class _AlaQoSConditionSourceMacAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceMacAddrStatus based on Integer32"""
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


_AlaQoSConditionSourceMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceMacAddrStatus_Object = MibTableColumn
alaQoSConditionSourceMacAddrStatus = _AlaQoSConditionSourceMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 18),
    _AlaQoSConditionSourceMacAddrStatus_Type()
)
alaQoSConditionSourceMacAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacAddrStatus.setStatus("current")


class _AlaQoSConditionSourceMacMask_Type(MacAddress):
    """Custom type alaQoSConditionSourceMacMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"


_AlaQoSConditionSourceMacMask_Object = MibTableColumn
alaQoSConditionSourceMacMask = _AlaQoSConditionSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 19),
    _AlaQoSConditionSourceMacMask_Type()
)
alaQoSConditionSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacMask.setStatus("current")


class _AlaQoSConditionSourceMacGroup_Type(DisplayString):
    """Custom type alaQoSConditionSourceMacGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourceMacGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionSourceMacGroup_Object = MibTableColumn
alaQoSConditionSourceMacGroup = _AlaQoSConditionSourceMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 20),
    _AlaQoSConditionSourceMacGroup_Type()
)
alaQoSConditionSourceMacGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacGroup.setStatus("current")


class _AlaQoSConditionSourceMacGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceMacGroupStatus based on Integer32"""
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


_AlaQoSConditionSourceMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceMacGroupStatus_Object = MibTableColumn
alaQoSConditionSourceMacGroupStatus = _AlaQoSConditionSourceMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 21),
    _AlaQoSConditionSourceMacGroupStatus_Type()
)
alaQoSConditionSourceMacGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceMacGroupStatus.setStatus("current")


class _AlaQoSConditionDestinationMacAddr_Type(MacAddress):
    """Custom type alaQoSConditionDestinationMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSConditionDestinationMacAddr_Object = MibTableColumn
alaQoSConditionDestinationMacAddr = _AlaQoSConditionDestinationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 22),
    _AlaQoSConditionDestinationMacAddr_Type()
)
alaQoSConditionDestinationMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacAddr.setStatus("current")


class _AlaQoSConditionDestinationMacAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationMacAddrStatus based on Integer32"""
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


_AlaQoSConditionDestinationMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationMacAddrStatus_Object = MibTableColumn
alaQoSConditionDestinationMacAddrStatus = _AlaQoSConditionDestinationMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 23),
    _AlaQoSConditionDestinationMacAddrStatus_Type()
)
alaQoSConditionDestinationMacAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacAddrStatus.setStatus("current")


class _AlaQoSConditionDestinationMacMask_Type(MacAddress):
    """Custom type alaQoSConditionDestinationMacMask based on MacAddress"""
    defaultHexValue = "ffffffffffff"


_AlaQoSConditionDestinationMacMask_Object = MibTableColumn
alaQoSConditionDestinationMacMask = _AlaQoSConditionDestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 24),
    _AlaQoSConditionDestinationMacMask_Type()
)
alaQoSConditionDestinationMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacMask.setStatus("current")


class _AlaQoSConditionDestinationMacGroup_Type(DisplayString):
    """Custom type alaQoSConditionDestinationMacGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionDestinationMacGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionDestinationMacGroup_Object = MibTableColumn
alaQoSConditionDestinationMacGroup = _AlaQoSConditionDestinationMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 25),
    _AlaQoSConditionDestinationMacGroup_Type()
)
alaQoSConditionDestinationMacGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacGroup.setStatus("current")


class _AlaQoSConditionDestinationMacGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationMacGroupStatus based on Integer32"""
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


_AlaQoSConditionDestinationMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationMacGroupStatus_Object = MibTableColumn
alaQoSConditionDestinationMacGroupStatus = _AlaQoSConditionDestinationMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 26),
    _AlaQoSConditionDestinationMacGroupStatus_Type()
)
alaQoSConditionDestinationMacGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationMacGroupStatus.setStatus("current")


class _AlaQoSConditionSourceVlan_Type(Integer32):
    """Custom type alaQoSConditionSourceVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSConditionSourceVlan_Type.__name__ = "Integer32"
_AlaQoSConditionSourceVlan_Object = MibTableColumn
alaQoSConditionSourceVlan = _AlaQoSConditionSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 27),
    _AlaQoSConditionSourceVlan_Type()
)
alaQoSConditionSourceVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceVlan.setStatus("current")


class _AlaQoSConditionSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceVlanStatus based on Integer32"""
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


_AlaQoSConditionSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceVlanStatus_Object = MibTableColumn
alaQoSConditionSourceVlanStatus = _AlaQoSConditionSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 28),
    _AlaQoSConditionSourceVlanStatus_Type()
)
alaQoSConditionSourceVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceVlanStatus.setStatus("current")


class _AlaQoSConditionDestinationVlan_Type(Integer32):
    """Custom type alaQoSConditionDestinationVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSConditionDestinationVlan_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationVlan_Object = MibTableColumn
alaQoSConditionDestinationVlan = _AlaQoSConditionDestinationVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 29),
    _AlaQoSConditionDestinationVlan_Type()
)
alaQoSConditionDestinationVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationVlan.setStatus("current")


class _AlaQoSConditionDestinationVlanStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationVlanStatus based on Integer32"""
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


_AlaQoSConditionDestinationVlanStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationVlanStatus_Object = MibTableColumn
alaQoSConditionDestinationVlanStatus = _AlaQoSConditionDestinationVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 30),
    _AlaQoSConditionDestinationVlanStatus_Type()
)
alaQoSConditionDestinationVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationVlanStatus.setStatus("current")


class _AlaQoSCondition8021p_Type(Integer32):
    """Custom type alaQoSCondition8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSCondition8021p_Type.__name__ = "Integer32"
_AlaQoSCondition8021p_Object = MibTableColumn
alaQoSCondition8021p = _AlaQoSCondition8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 31),
    _AlaQoSCondition8021p_Type()
)
alaQoSCondition8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSCondition8021p.setStatus("current")


class _AlaQoSCondition8021pStatus_Type(Integer32):
    """Custom type alaQoSCondition8021pStatus based on Integer32"""
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


_AlaQoSCondition8021pStatus_Type.__name__ = "Integer32"
_AlaQoSCondition8021pStatus_Object = MibTableColumn
alaQoSCondition8021pStatus = _AlaQoSCondition8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 32),
    _AlaQoSCondition8021pStatus_Type()
)
alaQoSCondition8021pStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSCondition8021pStatus.setStatus("current")


class _AlaQoSConditionSourceIpAddr_Type(IpAddress):
    """Custom type alaQoSConditionSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSConditionSourceIpAddr_Object = MibTableColumn
alaQoSConditionSourceIpAddr = _AlaQoSConditionSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 33),
    _AlaQoSConditionSourceIpAddr_Type()
)
alaQoSConditionSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpAddr.setStatus("current")


class _AlaQoSConditionSourceIpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceIpAddrStatus based on Integer32"""
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


_AlaQoSConditionSourceIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpAddrStatus_Object = MibTableColumn
alaQoSConditionSourceIpAddrStatus = _AlaQoSConditionSourceIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 34),
    _AlaQoSConditionSourceIpAddrStatus_Type()
)
alaQoSConditionSourceIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpAddrStatus.setStatus("current")


class _AlaQoSConditionSourceIpMask_Type(IpAddress):
    """Custom type alaQoSConditionSourceIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSConditionSourceIpMask_Object = MibTableColumn
alaQoSConditionSourceIpMask = _AlaQoSConditionSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 35),
    _AlaQoSConditionSourceIpMask_Type()
)
alaQoSConditionSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpMask.setStatus("current")


class _AlaQoSConditionSourceNetworkGroup_Type(DisplayString):
    """Custom type alaQoSConditionSourceNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourceNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionSourceNetworkGroup_Object = MibTableColumn
alaQoSConditionSourceNetworkGroup = _AlaQoSConditionSourceNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 36),
    _AlaQoSConditionSourceNetworkGroup_Type()
)
alaQoSConditionSourceNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceNetworkGroup.setStatus("current")


class _AlaQoSConditionSourceNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceNetworkGroupStatus based on Integer32"""
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


_AlaQoSConditionSourceNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceNetworkGroupStatus_Object = MibTableColumn
alaQoSConditionSourceNetworkGroupStatus = _AlaQoSConditionSourceNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 37),
    _AlaQoSConditionSourceNetworkGroupStatus_Type()
)
alaQoSConditionSourceNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceNetworkGroupStatus.setStatus("current")


class _AlaQoSConditionDestinationIpAddr_Type(IpAddress):
    """Custom type alaQoSConditionDestinationIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSConditionDestinationIpAddr_Object = MibTableColumn
alaQoSConditionDestinationIpAddr = _AlaQoSConditionDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 38),
    _AlaQoSConditionDestinationIpAddr_Type()
)
alaQoSConditionDestinationIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpAddr.setStatus("current")


class _AlaQoSConditionDestinationIpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpAddrStatus based on Integer32"""
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


_AlaQoSConditionDestinationIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpAddrStatus_Object = MibTableColumn
alaQoSConditionDestinationIpAddrStatus = _AlaQoSConditionDestinationIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 39),
    _AlaQoSConditionDestinationIpAddrStatus_Type()
)
alaQoSConditionDestinationIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpAddrStatus.setStatus("current")


class _AlaQoSConditionDestinationIpMask_Type(IpAddress):
    """Custom type alaQoSConditionDestinationIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSConditionDestinationIpMask_Object = MibTableColumn
alaQoSConditionDestinationIpMask = _AlaQoSConditionDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 40),
    _AlaQoSConditionDestinationIpMask_Type()
)
alaQoSConditionDestinationIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpMask.setStatus("current")


class _AlaQoSConditionDestinationNetworkGroup_Type(DisplayString):
    """Custom type alaQoSConditionDestinationNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionDestinationNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionDestinationNetworkGroup_Object = MibTableColumn
alaQoSConditionDestinationNetworkGroup = _AlaQoSConditionDestinationNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 41),
    _AlaQoSConditionDestinationNetworkGroup_Type()
)
alaQoSConditionDestinationNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationNetworkGroup.setStatus("current")


class _AlaQoSConditionDestinationNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationNetworkGroupStatus based on Integer32"""
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


_AlaQoSConditionDestinationNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationNetworkGroupStatus_Object = MibTableColumn
alaQoSConditionDestinationNetworkGroupStatus = _AlaQoSConditionDestinationNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 42),
    _AlaQoSConditionDestinationNetworkGroupStatus_Type()
)
alaQoSConditionDestinationNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationNetworkGroupStatus.setStatus("current")


class _AlaQoSConditionMulticastIpAddr_Type(IpAddress):
    """Custom type alaQoSConditionMulticastIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSConditionMulticastIpAddr_Object = MibTableColumn
alaQoSConditionMulticastIpAddr = _AlaQoSConditionMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 43),
    _AlaQoSConditionMulticastIpAddr_Type()
)
alaQoSConditionMulticastIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastIpAddr.setStatus("current")


class _AlaQoSConditionMulticastIpAddrStatus_Type(Integer32):
    """Custom type alaQoSConditionMulticastIpAddrStatus based on Integer32"""
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


_AlaQoSConditionMulticastIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionMulticastIpAddrStatus_Object = MibTableColumn
alaQoSConditionMulticastIpAddrStatus = _AlaQoSConditionMulticastIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 44),
    _AlaQoSConditionMulticastIpAddrStatus_Type()
)
alaQoSConditionMulticastIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastIpAddrStatus.setStatus("current")


class _AlaQoSConditionMulticastIpMask_Type(IpAddress):
    """Custom type alaQoSConditionMulticastIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSConditionMulticastIpMask_Object = MibTableColumn
alaQoSConditionMulticastIpMask = _AlaQoSConditionMulticastIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 45),
    _AlaQoSConditionMulticastIpMask_Type()
)
alaQoSConditionMulticastIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastIpMask.setStatus("current")


class _AlaQoSConditionMulticastNetworkGroup_Type(DisplayString):
    """Custom type alaQoSConditionMulticastNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionMulticastNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionMulticastNetworkGroup_Object = MibTableColumn
alaQoSConditionMulticastNetworkGroup = _AlaQoSConditionMulticastNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 46),
    _AlaQoSConditionMulticastNetworkGroup_Type()
)
alaQoSConditionMulticastNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastNetworkGroup.setStatus("current")


class _AlaQoSConditionMulticastNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionMulticastNetworkGroupStatus based on Integer32"""
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


_AlaQoSConditionMulticastNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionMulticastNetworkGroupStatus_Object = MibTableColumn
alaQoSConditionMulticastNetworkGroupStatus = _AlaQoSConditionMulticastNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 47),
    _AlaQoSConditionMulticastNetworkGroupStatus_Type()
)
alaQoSConditionMulticastNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMulticastNetworkGroupStatus.setStatus("current")


class _AlaQoSConditionTos_Type(Integer32):
    """Custom type alaQoSConditionTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSConditionTos_Type.__name__ = "Integer32"
_AlaQoSConditionTos_Object = MibTableColumn
alaQoSConditionTos = _AlaQoSConditionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 48),
    _AlaQoSConditionTos_Type()
)
alaQoSConditionTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTos.setStatus("current")


class _AlaQoSConditionTosStatus_Type(Integer32):
    """Custom type alaQoSConditionTosStatus based on Integer32"""
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


_AlaQoSConditionTosStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTosStatus_Object = MibTableColumn
alaQoSConditionTosStatus = _AlaQoSConditionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 49),
    _AlaQoSConditionTosStatus_Type()
)
alaQoSConditionTosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTosStatus.setStatus("current")


class _AlaQoSConditionTosMask_Type(Integer32):
    """Custom type alaQoSConditionTosMask based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSConditionTosMask_Type.__name__ = "Integer32"
_AlaQoSConditionTosMask_Object = MibTableColumn
alaQoSConditionTosMask = _AlaQoSConditionTosMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 50),
    _AlaQoSConditionTosMask_Type()
)
alaQoSConditionTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTosMask.setStatus("current")


class _AlaQoSConditionDscp_Type(Integer32):
    """Custom type alaQoSConditionDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSConditionDscp_Type.__name__ = "Integer32"
_AlaQoSConditionDscp_Object = MibTableColumn
alaQoSConditionDscp = _AlaQoSConditionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 51),
    _AlaQoSConditionDscp_Type()
)
alaQoSConditionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscp.setStatus("current")


class _AlaQoSConditionDscpStatus_Type(Integer32):
    """Custom type alaQoSConditionDscpStatus based on Integer32"""
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


_AlaQoSConditionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDscpStatus_Object = MibTableColumn
alaQoSConditionDscpStatus = _AlaQoSConditionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 52),
    _AlaQoSConditionDscpStatus_Type()
)
alaQoSConditionDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscpStatus.setStatus("current")


class _AlaQoSConditionDscpMask_Type(Integer32):
    """Custom type alaQoSConditionDscpMask based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSConditionDscpMask_Type.__name__ = "Integer32"
_AlaQoSConditionDscpMask_Object = MibTableColumn
alaQoSConditionDscpMask = _AlaQoSConditionDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 53),
    _AlaQoSConditionDscpMask_Type()
)
alaQoSConditionDscpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscpMask.setStatus("current")


class _AlaQoSConditionIpProtocol_Type(Integer32):
    """Custom type alaQoSConditionIpProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIpProtocol_Type.__name__ = "Integer32"
_AlaQoSConditionIpProtocol_Object = MibTableColumn
alaQoSConditionIpProtocol = _AlaQoSConditionIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 54),
    _AlaQoSConditionIpProtocol_Type()
)
alaQoSConditionIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpProtocol.setStatus("current")


class _AlaQoSConditionIpProtocolStatus_Type(Integer32):
    """Custom type alaQoSConditionIpProtocolStatus based on Integer32"""
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


_AlaQoSConditionIpProtocolStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIpProtocolStatus_Object = MibTableColumn
alaQoSConditionIpProtocolStatus = _AlaQoSConditionIpProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 55),
    _AlaQoSConditionIpProtocolStatus_Type()
)
alaQoSConditionIpProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpProtocolStatus.setStatus("current")


class _AlaQoSConditionSourceIpPort_Type(Integer32):
    """Custom type alaQoSConditionSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpPort_Object = MibTableColumn
alaQoSConditionSourceIpPort = _AlaQoSConditionSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 56),
    _AlaQoSConditionSourceIpPort_Type()
)
alaQoSConditionSourceIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpPort.setStatus("current")


class _AlaQoSConditionSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceIpPortStatus based on Integer32"""
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


_AlaQoSConditionSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpPortStatus_Object = MibTableColumn
alaQoSConditionSourceIpPortStatus = _AlaQoSConditionSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 57),
    _AlaQoSConditionSourceIpPortStatus_Type()
)
alaQoSConditionSourceIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpPortStatus.setStatus("current")


class _AlaQoSConditionDestinationIpPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpPort_Object = MibTableColumn
alaQoSConditionDestinationIpPort = _AlaQoSConditionDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 58),
    _AlaQoSConditionDestinationIpPort_Type()
)
alaQoSConditionDestinationIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpPort.setStatus("current")


class _AlaQoSConditionDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpPortStatus based on Integer32"""
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


_AlaQoSConditionDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpPortStatus_Object = MibTableColumn
alaQoSConditionDestinationIpPortStatus = _AlaQoSConditionDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 59),
    _AlaQoSConditionDestinationIpPortStatus_Type()
)
alaQoSConditionDestinationIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpPortStatus.setStatus("current")


class _AlaQoSConditionService_Type(DisplayString):
    """Custom type alaQoSConditionService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionService_Type.__name__ = "DisplayString"
_AlaQoSConditionService_Object = MibTableColumn
alaQoSConditionService = _AlaQoSConditionService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 60),
    _AlaQoSConditionService_Type()
)
alaQoSConditionService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionService.setStatus("current")


class _AlaQoSConditionServiceStatus_Type(Integer32):
    """Custom type alaQoSConditionServiceStatus based on Integer32"""
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


_AlaQoSConditionServiceStatus_Type.__name__ = "Integer32"
_AlaQoSConditionServiceStatus_Object = MibTableColumn
alaQoSConditionServiceStatus = _AlaQoSConditionServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 61),
    _AlaQoSConditionServiceStatus_Type()
)
alaQoSConditionServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionServiceStatus.setStatus("current")


class _AlaQoSConditionServiceGroup_Type(DisplayString):
    """Custom type alaQoSConditionServiceGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionServiceGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionServiceGroup_Object = MibTableColumn
alaQoSConditionServiceGroup = _AlaQoSConditionServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 62),
    _AlaQoSConditionServiceGroup_Type()
)
alaQoSConditionServiceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionServiceGroup.setStatus("current")


class _AlaQoSConditionServiceGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionServiceGroupStatus based on Integer32"""
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


_AlaQoSConditionServiceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionServiceGroupStatus_Object = MibTableColumn
alaQoSConditionServiceGroupStatus = _AlaQoSConditionServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 63),
    _AlaQoSConditionServiceGroupStatus_Type()
)
alaQoSConditionServiceGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionServiceGroupStatus.setStatus("current")


class _AlaQoSConditionIcmpType_Type(Integer32):
    """Custom type alaQoSConditionIcmpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIcmpType_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpType_Object = MibTableColumn
alaQoSConditionIcmpType = _AlaQoSConditionIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 64),
    _AlaQoSConditionIcmpType_Type()
)
alaQoSConditionIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpType.setStatus("current")


class _AlaQoSConditionIcmpTypeStatus_Type(Integer32):
    """Custom type alaQoSConditionIcmpTypeStatus based on Integer32"""
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


_AlaQoSConditionIcmpTypeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpTypeStatus_Object = MibTableColumn
alaQoSConditionIcmpTypeStatus = _AlaQoSConditionIcmpTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 65),
    _AlaQoSConditionIcmpTypeStatus_Type()
)
alaQoSConditionIcmpTypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpTypeStatus.setStatus("current")


class _AlaQoSConditionIcmpCode_Type(Integer32):
    """Custom type alaQoSConditionIcmpCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIcmpCode_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpCode_Object = MibTableColumn
alaQoSConditionIcmpCode = _AlaQoSConditionIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 66),
    _AlaQoSConditionIcmpCode_Type()
)
alaQoSConditionIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpCode.setStatus("current")


class _AlaQoSConditionIcmpCodeStatus_Type(Integer32):
    """Custom type alaQoSConditionIcmpCodeStatus based on Integer32"""
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


_AlaQoSConditionIcmpCodeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIcmpCodeStatus_Object = MibTableColumn
alaQoSConditionIcmpCodeStatus = _AlaQoSConditionIcmpCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 67),
    _AlaQoSConditionIcmpCodeStatus_Type()
)
alaQoSConditionIcmpCodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIcmpCodeStatus.setStatus("current")


class _AlaQoSConditionDlci_Type(Integer32):
    """Custom type alaQoSConditionDlci based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_AlaQoSConditionDlci_Type.__name__ = "Integer32"
_AlaQoSConditionDlci_Object = MibTableColumn
alaQoSConditionDlci = _AlaQoSConditionDlci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 68),
    _AlaQoSConditionDlci_Type()
)
alaQoSConditionDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDlci.setStatus("current")


class _AlaQoSConditionDlciStatus_Type(Integer32):
    """Custom type alaQoSConditionDlciStatus based on Integer32"""
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


_AlaQoSConditionDlciStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDlciStatus_Object = MibTableColumn
alaQoSConditionDlciStatus = _AlaQoSConditionDlciStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 69),
    _AlaQoSConditionDlciStatus_Type()
)
alaQoSConditionDlciStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDlciStatus.setStatus("current")
_AlaQoSConditionRowStatus_Type = RowStatus
_AlaQoSConditionRowStatus_Object = MibTableColumn
alaQoSConditionRowStatus = _AlaQoSConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 70),
    _AlaQoSConditionRowStatus_Type()
)
alaQoSConditionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionRowStatus.setStatus("current")


class _AlaQoSConditionSourcePortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourcePortEnd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSConditionSourcePortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourcePortEnd_Object = MibTableColumn
alaQoSConditionSourcePortEnd = _AlaQoSConditionSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 71),
    _AlaQoSConditionSourcePortEnd_Type()
)
alaQoSConditionSourcePortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourcePortEnd.setStatus("current")


class _AlaQoSConditionDestinationPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationPortEnd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSConditionDestinationPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationPortEnd_Object = MibTableColumn
alaQoSConditionDestinationPortEnd = _AlaQoSConditionDestinationPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 72),
    _AlaQoSConditionDestinationPortEnd_Type()
)
alaQoSConditionDestinationPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationPortEnd.setStatus("current")


class _AlaQoSConditionSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpPortEnd_Object = MibTableColumn
alaQoSConditionSourceIpPortEnd = _AlaQoSConditionSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 73),
    _AlaQoSConditionSourceIpPortEnd_Type()
)
alaQoSConditionSourceIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpPortEnd.setStatus("current")


class _AlaQoSConditionDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpPortEnd_Object = MibTableColumn
alaQoSConditionDestinationIpPortEnd = _AlaQoSConditionDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 74),
    _AlaQoSConditionDestinationIpPortEnd_Type()
)
alaQoSConditionDestinationIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpPortEnd.setStatus("current")


class _AlaQoSConditionSourceTcpPort_Type(Integer32):
    """Custom type alaQoSConditionSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSConditionSourceTcpPort_Object = MibTableColumn
alaQoSConditionSourceTcpPort = _AlaQoSConditionSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 75),
    _AlaQoSConditionSourceTcpPort_Type()
)
alaQoSConditionSourceTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceTcpPort.setStatus("current")


class _AlaQoSConditionSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceTcpPortStatus based on Integer32"""
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


_AlaQoSConditionSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceTcpPortStatus_Object = MibTableColumn
alaQoSConditionSourceTcpPortStatus = _AlaQoSConditionSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 76),
    _AlaQoSConditionSourceTcpPortStatus_Type()
)
alaQoSConditionSourceTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceTcpPortStatus.setStatus("current")


class _AlaQoSConditionSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourceTcpPortEnd_Object = MibTableColumn
alaQoSConditionSourceTcpPortEnd = _AlaQoSConditionSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 77),
    _AlaQoSConditionSourceTcpPortEnd_Type()
)
alaQoSConditionSourceTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceTcpPortEnd.setStatus("current")


class _AlaQoSConditionDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationTcpPort_Object = MibTableColumn
alaQoSConditionDestinationTcpPort = _AlaQoSConditionDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 78),
    _AlaQoSConditionDestinationTcpPort_Type()
)
alaQoSConditionDestinationTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationTcpPort.setStatus("current")


class _AlaQoSConditionDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationTcpPortStatus based on Integer32"""
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


_AlaQoSConditionDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationTcpPortStatus_Object = MibTableColumn
alaQoSConditionDestinationTcpPortStatus = _AlaQoSConditionDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 79),
    _AlaQoSConditionDestinationTcpPortStatus_Type()
)
alaQoSConditionDestinationTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationTcpPortStatus.setStatus("current")


class _AlaQoSConditionDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationTcpPortEnd_Object = MibTableColumn
alaQoSConditionDestinationTcpPortEnd = _AlaQoSConditionDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 80),
    _AlaQoSConditionDestinationTcpPortEnd_Type()
)
alaQoSConditionDestinationTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationTcpPortEnd.setStatus("current")


class _AlaQoSConditionSourceUdpPort_Type(Integer32):
    """Custom type alaQoSConditionSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSConditionSourceUdpPort_Object = MibTableColumn
alaQoSConditionSourceUdpPort = _AlaQoSConditionSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 81),
    _AlaQoSConditionSourceUdpPort_Type()
)
alaQoSConditionSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceUdpPort.setStatus("current")


class _AlaQoSConditionSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceUdpPortStatus based on Integer32"""
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


_AlaQoSConditionSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceUdpPortStatus_Object = MibTableColumn
alaQoSConditionSourceUdpPortStatus = _AlaQoSConditionSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 82),
    _AlaQoSConditionSourceUdpPortStatus_Type()
)
alaQoSConditionSourceUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceUdpPortStatus.setStatus("current")


class _AlaQoSConditionSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionSourceUdpPortEnd_Object = MibTableColumn
alaQoSConditionSourceUdpPortEnd = _AlaQoSConditionSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 83),
    _AlaQoSConditionSourceUdpPortEnd_Type()
)
alaQoSConditionSourceUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceUdpPortEnd.setStatus("current")


class _AlaQoSConditionDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSConditionDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationUdpPort_Object = MibTableColumn
alaQoSConditionDestinationUdpPort = _AlaQoSConditionDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 84),
    _AlaQoSConditionDestinationUdpPort_Type()
)
alaQoSConditionDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationUdpPort.setStatus("current")


class _AlaQoSConditionDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationUdpPortStatus based on Integer32"""
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


_AlaQoSConditionDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationUdpPortStatus_Object = MibTableColumn
alaQoSConditionDestinationUdpPortStatus = _AlaQoSConditionDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 85),
    _AlaQoSConditionDestinationUdpPortStatus_Type()
)
alaQoSConditionDestinationUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationUdpPortStatus.setStatus("current")


class _AlaQoSConditionDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSConditionDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationUdpPortEnd_Object = MibTableColumn
alaQoSConditionDestinationUdpPortEnd = _AlaQoSConditionDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 86),
    _AlaQoSConditionDestinationUdpPortEnd_Type()
)
alaQoSConditionDestinationUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationUdpPortEnd.setStatus("current")


class _AlaQoSConditionEthertype_Type(Integer32):
    """Custom type alaQoSConditionEthertype based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSConditionEthertype_Type.__name__ = "Integer32"
_AlaQoSConditionEthertype_Object = MibTableColumn
alaQoSConditionEthertype = _AlaQoSConditionEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 87),
    _AlaQoSConditionEthertype_Type()
)
alaQoSConditionEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionEthertype.setStatus("current")


class _AlaQoSConditionEthertypeStatus_Type(Integer32):
    """Custom type alaQoSConditionEthertypeStatus based on Integer32"""
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


_AlaQoSConditionEthertypeStatus_Type.__name__ = "Integer32"
_AlaQoSConditionEthertypeStatus_Object = MibTableColumn
alaQoSConditionEthertypeStatus = _AlaQoSConditionEthertypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 88),
    _AlaQoSConditionEthertypeStatus_Type()
)
alaQoSConditionEthertypeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionEthertypeStatus.setStatus("current")


class _AlaQoSConditionTcpFlags_Type(Integer32):
    """Custom type alaQoSConditionTcpFlags based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("any", 2))
    )


_AlaQoSConditionTcpFlags_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlags_Object = MibTableColumn
alaQoSConditionTcpFlags = _AlaQoSConditionTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 89),
    _AlaQoSConditionTcpFlags_Type()
)
alaQoSConditionTcpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlags.setStatus("current")


class _AlaQoSConditionTcpFlagsStatus_Type(Integer32):
    """Custom type alaQoSConditionTcpFlagsStatus based on Integer32"""
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


_AlaQoSConditionTcpFlagsStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlagsStatus_Object = MibTableColumn
alaQoSConditionTcpFlagsStatus = _AlaQoSConditionTcpFlagsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 90),
    _AlaQoSConditionTcpFlagsStatus_Type()
)
alaQoSConditionTcpFlagsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsStatus.setStatus("current")
_AlaQoSConditionTcpFlagsVal_Type = Integer32
_AlaQoSConditionTcpFlagsVal_Object = MibTableColumn
alaQoSConditionTcpFlagsVal = _AlaQoSConditionTcpFlagsVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 91),
    _AlaQoSConditionTcpFlagsVal_Type()
)
alaQoSConditionTcpFlagsVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsVal.setStatus("current")


class _AlaQoSConditionTcpFlagsValStatus_Type(Integer32):
    """Custom type alaQoSConditionTcpFlagsValStatus based on Integer32"""
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


_AlaQoSConditionTcpFlagsValStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlagsValStatus_Object = MibTableColumn
alaQoSConditionTcpFlagsValStatus = _AlaQoSConditionTcpFlagsValStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 92),
    _AlaQoSConditionTcpFlagsValStatus_Type()
)
alaQoSConditionTcpFlagsValStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsValStatus.setStatus("current")
_AlaQoSConditionTcpFlagsMask_Type = Integer32
_AlaQoSConditionTcpFlagsMask_Object = MibTableColumn
alaQoSConditionTcpFlagsMask = _AlaQoSConditionTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 93),
    _AlaQoSConditionTcpFlagsMask_Type()
)
alaQoSConditionTcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsMask.setStatus("current")


class _AlaQoSConditionTcpFlagsMaskStatus_Type(Integer32):
    """Custom type alaQoSConditionTcpFlagsMaskStatus based on Integer32"""
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


_AlaQoSConditionTcpFlagsMaskStatus_Type.__name__ = "Integer32"
_AlaQoSConditionTcpFlagsMaskStatus_Object = MibTableColumn
alaQoSConditionTcpFlagsMaskStatus = _AlaQoSConditionTcpFlagsMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 94),
    _AlaQoSConditionTcpFlagsMaskStatus_Type()
)
alaQoSConditionTcpFlagsMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpFlagsMaskStatus.setStatus("current")


class _AlaQoSConditionTcpEstablished_Type(Integer32):
    """Custom type alaQoSConditionTcpEstablished based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConditionTcpEstablished_Type.__name__ = "Integer32"
_AlaQoSConditionTcpEstablished_Object = MibTableColumn
alaQoSConditionTcpEstablished = _AlaQoSConditionTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 95),
    _AlaQoSConditionTcpEstablished_Type()
)
alaQoSConditionTcpEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionTcpEstablished.setStatus("current")


class _AlaQoSConditionSourceIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSConditionSourceIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSConditionSourceIpv6Addr_Object = MibTableColumn
alaQoSConditionSourceIpv6Addr = _AlaQoSConditionSourceIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 96),
    _AlaQoSConditionSourceIpv6Addr_Type()
)
alaQoSConditionSourceIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpv6Addr.setStatus("current")


class _AlaQoSConditionSourceIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceIpv6AddrStatus based on Integer32"""
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


_AlaQoSConditionSourceIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceIpv6AddrStatus_Object = MibTableColumn
alaQoSConditionSourceIpv6AddrStatus = _AlaQoSConditionSourceIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 97),
    _AlaQoSConditionSourceIpv6AddrStatus_Type()
)
alaQoSConditionSourceIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpv6AddrStatus.setStatus("current")


class _AlaQoSConditionSourceIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSConditionSourceIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSConditionSourceIpv6Mask_Object = MibTableColumn
alaQoSConditionSourceIpv6Mask = _AlaQoSConditionSourceIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 98),
    _AlaQoSConditionSourceIpv6Mask_Type()
)
alaQoSConditionSourceIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceIpv6Mask.setStatus("current")


class _AlaQoSConditionDestinationIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSConditionDestinationIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSConditionDestinationIpv6Addr_Object = MibTableColumn
alaQoSConditionDestinationIpv6Addr = _AlaQoSConditionDestinationIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 99),
    _AlaQoSConditionDestinationIpv6Addr_Type()
)
alaQoSConditionDestinationIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpv6Addr.setStatus("current")


class _AlaQoSConditionDestinationIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSConditionDestinationIpv6AddrStatus based on Integer32"""
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


_AlaQoSConditionDestinationIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionDestinationIpv6AddrStatus_Object = MibTableColumn
alaQoSConditionDestinationIpv6AddrStatus = _AlaQoSConditionDestinationIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 100),
    _AlaQoSConditionDestinationIpv6AddrStatus_Type()
)
alaQoSConditionDestinationIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpv6AddrStatus.setStatus("current")


class _AlaQoSConditionDestinationIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSConditionDestinationIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSConditionDestinationIpv6Mask_Object = MibTableColumn
alaQoSConditionDestinationIpv6Mask = _AlaQoSConditionDestinationIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 101),
    _AlaQoSConditionDestinationIpv6Mask_Type()
)
alaQoSConditionDestinationIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDestinationIpv6Mask.setStatus("current")


class _AlaQoSConditionIpv6Traffic_Type(Integer32):
    """Custom type alaQoSConditionIpv6Traffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConditionIpv6Traffic_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6Traffic_Object = MibTableColumn
alaQoSConditionIpv6Traffic = _AlaQoSConditionIpv6Traffic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 102),
    _AlaQoSConditionIpv6Traffic_Type()
)
alaQoSConditionIpv6Traffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6Traffic.setStatus("current")


class _AlaQoSConditionIpv6NH_Type(Integer32):
    """Custom type alaQoSConditionIpv6NH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSConditionIpv6NH_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6NH_Object = MibTableColumn
alaQoSConditionIpv6NH = _AlaQoSConditionIpv6NH_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 103),
    _AlaQoSConditionIpv6NH_Type()
)
alaQoSConditionIpv6NH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6NH.setStatus("current")


class _AlaQoSConditionIpv6NHStatus_Type(Integer32):
    """Custom type alaQoSConditionIpv6NHStatus based on Integer32"""
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


_AlaQoSConditionIpv6NHStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6NHStatus_Object = MibTableColumn
alaQoSConditionIpv6NHStatus = _AlaQoSConditionIpv6NHStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 104),
    _AlaQoSConditionIpv6NHStatus_Type()
)
alaQoSConditionIpv6NHStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6NHStatus.setStatus("current")


class _AlaQoSConditionIpv6FlowLabel_Type(Integer32):
    """Custom type alaQoSConditionIpv6FlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AlaQoSConditionIpv6FlowLabel_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6FlowLabel_Object = MibTableColumn
alaQoSConditionIpv6FlowLabel = _AlaQoSConditionIpv6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 105),
    _AlaQoSConditionIpv6FlowLabel_Type()
)
alaQoSConditionIpv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6FlowLabel.setStatus("current")


class _AlaQoSConditionIpv6FlowLabelStatus_Type(Integer32):
    """Custom type alaQoSConditionIpv6FlowLabelStatus based on Integer32"""
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


_AlaQoSConditionIpv6FlowLabelStatus_Type.__name__ = "Integer32"
_AlaQoSConditionIpv6FlowLabelStatus_Object = MibTableColumn
alaQoSConditionIpv6FlowLabelStatus = _AlaQoSConditionIpv6FlowLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 106),
    _AlaQoSConditionIpv6FlowLabelStatus_Type()
)
alaQoSConditionIpv6FlowLabelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionIpv6FlowLabelStatus.setStatus("current")


class _AlaQoSConditionMcastIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSConditionMcastIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSConditionMcastIpv6Addr_Object = MibTableColumn
alaQoSConditionMcastIpv6Addr = _AlaQoSConditionMcastIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 107),
    _AlaQoSConditionMcastIpv6Addr_Type()
)
alaQoSConditionMcastIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMcastIpv6Addr.setStatus("current")


class _AlaQoSConditionMcastIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSConditionMcastIpv6AddrStatus based on Integer32"""
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


_AlaQoSConditionMcastIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSConditionMcastIpv6AddrStatus_Object = MibTableColumn
alaQoSConditionMcastIpv6AddrStatus = _AlaQoSConditionMcastIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 108),
    _AlaQoSConditionMcastIpv6AddrStatus_Type()
)
alaQoSConditionMcastIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMcastIpv6AddrStatus.setStatus("current")


class _AlaQoSConditionMcastIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSConditionMcastIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSConditionMcastIpv6Mask_Object = MibTableColumn
alaQoSConditionMcastIpv6Mask = _AlaQoSConditionMcastIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 109),
    _AlaQoSConditionMcastIpv6Mask_Type()
)
alaQoSConditionMcastIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionMcastIpv6Mask.setStatus("current")


class _AlaQoSConditionDscpEnd_Type(Integer32):
    """Custom type alaQoSConditionDscpEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSConditionDscpEnd_Type.__name__ = "Integer32"
_AlaQoSConditionDscpEnd_Object = MibTableColumn
alaQoSConditionDscpEnd = _AlaQoSConditionDscpEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 110),
    _AlaQoSConditionDscpEnd_Type()
)
alaQoSConditionDscpEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionDscpEnd.setStatus("current")


class _AlaQoSConditionInnerSourceVlan_Type(Integer32):
    """Custom type alaQoSConditionInnerSourceVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSConditionInnerSourceVlan_Type.__name__ = "Integer32"
_AlaQoSConditionInnerSourceVlan_Object = MibTableColumn
alaQoSConditionInnerSourceVlan = _AlaQoSConditionInnerSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 111),
    _AlaQoSConditionInnerSourceVlan_Type()
)
alaQoSConditionInnerSourceVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInnerSourceVlan.setStatus("current")


class _AlaQoSConditionInnerSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSConditionInnerSourceVlanStatus based on Integer32"""
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


_AlaQoSConditionInnerSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSConditionInnerSourceVlanStatus_Object = MibTableColumn
alaQoSConditionInnerSourceVlanStatus = _AlaQoSConditionInnerSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 112),
    _AlaQoSConditionInnerSourceVlanStatus_Type()
)
alaQoSConditionInnerSourceVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInnerSourceVlanStatus.setStatus("current")


class _AlaQoSConditionInner8021p_Type(Integer32):
    """Custom type alaQoSConditionInner8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSConditionInner8021p_Type.__name__ = "Integer32"
_AlaQoSConditionInner8021p_Object = MibTableColumn
alaQoSConditionInner8021p = _AlaQoSConditionInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 113),
    _AlaQoSConditionInner8021p_Type()
)
alaQoSConditionInner8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInner8021p.setStatus("current")


class _AlaQoSConditionInner8021pStatus_Type(Integer32):
    """Custom type alaQoSConditionInner8021pStatus based on Integer32"""
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


_AlaQoSConditionInner8021pStatus_Type.__name__ = "Integer32"
_AlaQoSConditionInner8021pStatus_Object = MibTableColumn
alaQoSConditionInner8021pStatus = _AlaQoSConditionInner8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 114),
    _AlaQoSConditionInner8021pStatus_Type()
)
alaQoSConditionInner8021pStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInner8021pStatus.setStatus("current")


class _AlaQoSConditionVrfName_Type(DisplayString):
    """Custom type alaQoSConditionVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionVrfName_Type.__name__ = "DisplayString"
_AlaQoSConditionVrfName_Object = MibTableColumn
alaQoSConditionVrfName = _AlaQoSConditionVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 115),
    _AlaQoSConditionVrfName_Type()
)
alaQoSConditionVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVrfName.setStatus("current")


class _AlaQoSConditionVrfNameStatus_Type(Integer32):
    """Custom type alaQoSConditionVrfNameStatus based on Integer32"""
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


_AlaQoSConditionVrfNameStatus_Type.__name__ = "Integer32"
_AlaQoSConditionVrfNameStatus_Object = MibTableColumn
alaQoSConditionVrfNameStatus = _AlaQoSConditionVrfNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 116),
    _AlaQoSConditionVrfNameStatus_Type()
)
alaQoSConditionVrfNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionVrfNameStatus.setStatus("current")


class _AlaQoSCondition8021pEnd_Type(Integer32):
    """Custom type alaQoSCondition8021pEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSCondition8021pEnd_Type.__name__ = "Integer32"
_AlaQoSCondition8021pEnd_Object = MibTableColumn
alaQoSCondition8021pEnd = _AlaQoSCondition8021pEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 117),
    _AlaQoSCondition8021pEnd_Type()
)
alaQoSCondition8021pEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSCondition8021pEnd.setStatus("current")


class _AlaQoSConditionInner8021pEnd_Type(Integer32):
    """Custom type alaQoSConditionInner8021pEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSConditionInner8021pEnd_Type.__name__ = "Integer32"
_AlaQoSConditionInner8021pEnd_Object = MibTableColumn
alaQoSConditionInner8021pEnd = _AlaQoSConditionInner8021pEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 118),
    _AlaQoSConditionInner8021pEnd_Type()
)
alaQoSConditionInner8021pEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInner8021pEnd.setStatus("current")


class _AlaQoSConditionSourceVlanGroup_Type(DisplayString):
    """Custom type alaQoSConditionSourceVlanGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionSourceVlanGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionSourceVlanGroup_Object = MibTableColumn
alaQoSConditionSourceVlanGroup = _AlaQoSConditionSourceVlanGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 119),
    _AlaQoSConditionSourceVlanGroup_Type()
)
alaQoSConditionSourceVlanGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceVlanGroup.setStatus("current")


class _AlaQoSConditionSourceVlanGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionSourceVlanGroupStatus based on Integer32"""
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


_AlaQoSConditionSourceVlanGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionSourceVlanGroupStatus_Object = MibTableColumn
alaQoSConditionSourceVlanGroupStatus = _AlaQoSConditionSourceVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 120),
    _AlaQoSConditionSourceVlanGroupStatus_Type()
)
alaQoSConditionSourceVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionSourceVlanGroupStatus.setStatus("current")


class _AlaQoSConditionInnerSourceVlanGroup_Type(DisplayString):
    """Custom type alaQoSConditionInnerSourceVlanGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConditionInnerSourceVlanGroup_Type.__name__ = "DisplayString"
_AlaQoSConditionInnerSourceVlanGroup_Object = MibTableColumn
alaQoSConditionInnerSourceVlanGroup = _AlaQoSConditionInnerSourceVlanGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 121),
    _AlaQoSConditionInnerSourceVlanGroup_Type()
)
alaQoSConditionInnerSourceVlanGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInnerSourceVlanGroup.setStatus("current")


class _AlaQoSConditionInnerSourceVlanGroupStatus_Type(Integer32):
    """Custom type alaQoSConditionInnerSourceVlanGroupStatus based on Integer32"""
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


_AlaQoSConditionInnerSourceVlanGroupStatus_Type.__name__ = "Integer32"
_AlaQoSConditionInnerSourceVlanGroupStatus_Object = MibTableColumn
alaQoSConditionInnerSourceVlanGroupStatus = _AlaQoSConditionInnerSourceVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 3, 1, 122),
    _AlaQoSConditionInnerSourceVlanGroupStatus_Type()
)
alaQoSConditionInnerSourceVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConditionInnerSourceVlanGroupStatus.setStatus("current")
_AlaQoSAppliedConditionTable_Object = MibTable
alaQoSAppliedConditionTable = _AlaQoSAppliedConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTable.setStatus("current")
_AlaQoSAppliedConditionEntry_Object = MibTableRow
alaQoSAppliedConditionEntry = _AlaQoSAppliedConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1)
)
alaQoSAppliedConditionEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedConditionEntry.setStatus("current")


class _AlaQoSAppliedConditionName_Type(DisplayString):
    """Custom type alaQoSAppliedConditionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionName_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionName_Object = MibTableColumn
alaQoSAppliedConditionName = _AlaQoSAppliedConditionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 1),
    _AlaQoSAppliedConditionName_Type()
)
alaQoSAppliedConditionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionName.setStatus("current")


class _AlaQoSAppliedConditionSource_Type(Integer32):
    """Custom type alaQoSAppliedConditionSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedConditionSource_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSource_Object = MibTableColumn
alaQoSAppliedConditionSource = _AlaQoSAppliedConditionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 2),
    _AlaQoSAppliedConditionSource_Type()
)
alaQoSAppliedConditionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSource.setStatus("current")


class _AlaQoSAppliedConditionSourceSlot_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedConditionSourceSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceSlot_Object = MibTableColumn
alaQoSAppliedConditionSourceSlot = _AlaQoSAppliedConditionSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 3),
    _AlaQoSAppliedConditionSourceSlot_Type()
)
alaQoSAppliedConditionSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceSlot.setStatus("current")


class _AlaQoSAppliedConditionSourceSlotStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceSlotStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceSlotStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceSlotStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceSlotStatus = _AlaQoSAppliedConditionSourceSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 4),
    _AlaQoSAppliedConditionSourceSlotStatus_Type()
)
alaQoSAppliedConditionSourceSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceSlotStatus.setStatus("current")


class _AlaQoSAppliedConditionSourcePort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionSourcePort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourcePort_Object = MibTableColumn
alaQoSAppliedConditionSourcePort = _AlaQoSAppliedConditionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 5),
    _AlaQoSAppliedConditionSourcePort_Type()
)
alaQoSAppliedConditionSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePort.setStatus("current")


class _AlaQoSAppliedConditionSourcePortGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionSourcePortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourcePortGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionSourcePortGroup_Object = MibTableColumn
alaQoSAppliedConditionSourcePortGroup = _AlaQoSAppliedConditionSourcePortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 6),
    _AlaQoSAppliedConditionSourcePortGroup_Type()
)
alaQoSAppliedConditionSourcePortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortGroup.setStatus("current")


class _AlaQoSAppliedConditionSourcePortGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourcePortGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourcePortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourcePortGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourcePortGroupStatus = _AlaQoSAppliedConditionSourcePortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 7),
    _AlaQoSAppliedConditionSourcePortGroupStatus_Type()
)
alaQoSAppliedConditionSourcePortGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationSlot_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedConditionDestinationSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationSlot_Object = MibTableColumn
alaQoSAppliedConditionDestinationSlot = _AlaQoSAppliedConditionDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 8),
    _AlaQoSAppliedConditionDestinationSlot_Type()
)
alaQoSAppliedConditionDestinationSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationSlot.setStatus("current")


class _AlaQoSAppliedConditionDestinationSlotStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationSlotStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationSlotStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationSlotStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationSlotStatus = _AlaQoSAppliedConditionDestinationSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 9),
    _AlaQoSAppliedConditionDestinationSlotStatus_Type()
)
alaQoSAppliedConditionDestinationSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationSlotStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionDestinationPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationPort = _AlaQoSAppliedConditionDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 10),
    _AlaQoSAppliedConditionDestinationPort_Type()
)
alaQoSAppliedConditionDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationPortGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionDestinationPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionDestinationPortGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionDestinationPortGroup_Object = MibTableColumn
alaQoSAppliedConditionDestinationPortGroup = _AlaQoSAppliedConditionDestinationPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 11),
    _AlaQoSAppliedConditionDestinationPortGroup_Type()
)
alaQoSAppliedConditionDestinationPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPortGroup.setStatus("current")


class _AlaQoSAppliedConditionDestinationPortGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationPortGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationPortGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationPortGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationPortGroupStatus = _AlaQoSAppliedConditionDestinationPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 12),
    _AlaQoSAppliedConditionDestinationPortGroupStatus_Type()
)
alaQoSAppliedConditionDestinationPortGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPortGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceInterfaceType_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceInterfaceType based on Integer32"""
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
        *(("aggregate", 7),
          ("ethernet", 1),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet10G", 6),
          ("ethernet1G", 5),
          ("wan", 2))
    )


_AlaQoSAppliedConditionSourceInterfaceType_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceInterfaceType_Object = MibTableColumn
alaQoSAppliedConditionSourceInterfaceType = _AlaQoSAppliedConditionSourceInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 13),
    _AlaQoSAppliedConditionSourceInterfaceType_Type()
)
alaQoSAppliedConditionSourceInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceInterfaceType.setStatus("current")


class _AlaQoSAppliedConditionSourceInterfaceTypeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceInterfaceTypeStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceInterfaceTypeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceInterfaceTypeStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceInterfaceTypeStatus = _AlaQoSAppliedConditionSourceInterfaceTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 14),
    _AlaQoSAppliedConditionSourceInterfaceTypeStatus_Type()
)
alaQoSAppliedConditionSourceInterfaceTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceInterfaceTypeStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationInterfaceType_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationInterfaceType based on Integer32"""
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
        *(("aggregate", 7),
          ("ethernet", 1),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet10G", 6),
          ("ethernet1G", 5),
          ("wan", 2))
    )


_AlaQoSAppliedConditionDestinationInterfaceType_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationInterfaceType_Object = MibTableColumn
alaQoSAppliedConditionDestinationInterfaceType = _AlaQoSAppliedConditionDestinationInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 15),
    _AlaQoSAppliedConditionDestinationInterfaceType_Type()
)
alaQoSAppliedConditionDestinationInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationInterfaceType.setStatus("current")


class _AlaQoSAppliedConditionDestinationInterfaceTypeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationInterfaceTypeStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationInterfaceTypeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationInterfaceTypeStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationInterfaceTypeStatus = _AlaQoSAppliedConditionDestinationInterfaceTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 16),
    _AlaQoSAppliedConditionDestinationInterfaceTypeStatus_Type()
)
alaQoSAppliedConditionDestinationInterfaceTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationInterfaceTypeStatus.setStatus("current")
_AlaQoSAppliedConditionSourceMacAddr_Type = MacAddress
_AlaQoSAppliedConditionSourceMacAddr_Object = MibTableColumn
alaQoSAppliedConditionSourceMacAddr = _AlaQoSAppliedConditionSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 17),
    _AlaQoSAppliedConditionSourceMacAddr_Type()
)
alaQoSAppliedConditionSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacAddr.setStatus("current")


class _AlaQoSAppliedConditionSourceMacAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceMacAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceMacAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceMacAddrStatus = _AlaQoSAppliedConditionSourceMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 18),
    _AlaQoSAppliedConditionSourceMacAddrStatus_Type()
)
alaQoSAppliedConditionSourceMacAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacAddrStatus.setStatus("current")
_AlaQoSAppliedConditionSourceMacMask_Type = MacAddress
_AlaQoSAppliedConditionSourceMacMask_Object = MibTableColumn
alaQoSAppliedConditionSourceMacMask = _AlaQoSAppliedConditionSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 19),
    _AlaQoSAppliedConditionSourceMacMask_Type()
)
alaQoSAppliedConditionSourceMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacMask.setStatus("current")


class _AlaQoSAppliedConditionSourceMacGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionSourceMacGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourceMacGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionSourceMacGroup_Object = MibTableColumn
alaQoSAppliedConditionSourceMacGroup = _AlaQoSAppliedConditionSourceMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 20),
    _AlaQoSAppliedConditionSourceMacGroup_Type()
)
alaQoSAppliedConditionSourceMacGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacGroup.setStatus("current")


class _AlaQoSAppliedConditionSourceMacGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceMacGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceMacGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceMacGroupStatus = _AlaQoSAppliedConditionSourceMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 21),
    _AlaQoSAppliedConditionSourceMacGroupStatus_Type()
)
alaQoSAppliedConditionSourceMacGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceMacGroupStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationMacAddr_Type = MacAddress
_AlaQoSAppliedConditionDestinationMacAddr_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacAddr = _AlaQoSAppliedConditionDestinationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 22),
    _AlaQoSAppliedConditionDestinationMacAddr_Type()
)
alaQoSAppliedConditionDestinationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacAddr.setStatus("current")


class _AlaQoSAppliedConditionDestinationMacAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationMacAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationMacAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationMacAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacAddrStatus = _AlaQoSAppliedConditionDestinationMacAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 23),
    _AlaQoSAppliedConditionDestinationMacAddrStatus_Type()
)
alaQoSAppliedConditionDestinationMacAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacAddrStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationMacMask_Type = MacAddress
_AlaQoSAppliedConditionDestinationMacMask_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacMask = _AlaQoSAppliedConditionDestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 24),
    _AlaQoSAppliedConditionDestinationMacMask_Type()
)
alaQoSAppliedConditionDestinationMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacMask.setStatus("current")


class _AlaQoSAppliedConditionDestinationMacGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionDestinationMacGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionDestinationMacGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionDestinationMacGroup_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacGroup = _AlaQoSAppliedConditionDestinationMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 25),
    _AlaQoSAppliedConditionDestinationMacGroup_Type()
)
alaQoSAppliedConditionDestinationMacGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacGroup.setStatus("current")


class _AlaQoSAppliedConditionDestinationMacGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationMacGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationMacGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationMacGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationMacGroupStatus = _AlaQoSAppliedConditionDestinationMacGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 26),
    _AlaQoSAppliedConditionDestinationMacGroupStatus_Type()
)
alaQoSAppliedConditionDestinationMacGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationMacGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceVlan_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSAppliedConditionSourceVlan_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceVlan_Object = MibTableColumn
alaQoSAppliedConditionSourceVlan = _AlaQoSAppliedConditionSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 27),
    _AlaQoSAppliedConditionSourceVlan_Type()
)
alaQoSAppliedConditionSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceVlan.setStatus("current")


class _AlaQoSAppliedConditionSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceVlanStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceVlanStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceVlanStatus = _AlaQoSAppliedConditionSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 28),
    _AlaQoSAppliedConditionSourceVlanStatus_Type()
)
alaQoSAppliedConditionSourceVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceVlanStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationVlan_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSAppliedConditionDestinationVlan_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationVlan_Object = MibTableColumn
alaQoSAppliedConditionDestinationVlan = _AlaQoSAppliedConditionDestinationVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 29),
    _AlaQoSAppliedConditionDestinationVlan_Type()
)
alaQoSAppliedConditionDestinationVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationVlan.setStatus("current")


class _AlaQoSAppliedConditionDestinationVlanStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationVlanStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationVlanStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationVlanStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationVlanStatus = _AlaQoSAppliedConditionDestinationVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 30),
    _AlaQoSAppliedConditionDestinationVlanStatus_Type()
)
alaQoSAppliedConditionDestinationVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationVlanStatus.setStatus("current")


class _AlaQoSAppliedCondition8021p_Type(Integer32):
    """Custom type alaQoSAppliedCondition8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedCondition8021p_Type.__name__ = "Integer32"
_AlaQoSAppliedCondition8021p_Object = MibTableColumn
alaQoSAppliedCondition8021p = _AlaQoSAppliedCondition8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 31),
    _AlaQoSAppliedCondition8021p_Type()
)
alaQoSAppliedCondition8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedCondition8021p.setStatus("current")


class _AlaQoSAppliedCondition8021pStatus_Type(Integer32):
    """Custom type alaQoSAppliedCondition8021pStatus based on Integer32"""
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


_AlaQoSAppliedCondition8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedCondition8021pStatus_Object = MibTableColumn
alaQoSAppliedCondition8021pStatus = _AlaQoSAppliedCondition8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 32),
    _AlaQoSAppliedCondition8021pStatus_Type()
)
alaQoSAppliedCondition8021pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedCondition8021pStatus.setStatus("current")
_AlaQoSAppliedConditionSourceIpAddr_Type = IpAddress
_AlaQoSAppliedConditionSourceIpAddr_Object = MibTableColumn
alaQoSAppliedConditionSourceIpAddr = _AlaQoSAppliedConditionSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 33),
    _AlaQoSAppliedConditionSourceIpAddr_Type()
)
alaQoSAppliedConditionSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpAddr.setStatus("current")


class _AlaQoSAppliedConditionSourceIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceIpAddrStatus = _AlaQoSAppliedConditionSourceIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 34),
    _AlaQoSAppliedConditionSourceIpAddrStatus_Type()
)
alaQoSAppliedConditionSourceIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpAddrStatus.setStatus("current")
_AlaQoSAppliedConditionSourceIpMask_Type = IpAddress
_AlaQoSAppliedConditionSourceIpMask_Object = MibTableColumn
alaQoSAppliedConditionSourceIpMask = _AlaQoSAppliedConditionSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 35),
    _AlaQoSAppliedConditionSourceIpMask_Type()
)
alaQoSAppliedConditionSourceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpMask.setStatus("current")


class _AlaQoSAppliedConditionSourceNetworkGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionSourceNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourceNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionSourceNetworkGroup_Object = MibTableColumn
alaQoSAppliedConditionSourceNetworkGroup = _AlaQoSAppliedConditionSourceNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 36),
    _AlaQoSAppliedConditionSourceNetworkGroup_Type()
)
alaQoSAppliedConditionSourceNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceNetworkGroup.setStatus("current")


class _AlaQoSAppliedConditionSourceNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceNetworkGroupStatus = _AlaQoSAppliedConditionSourceNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 37),
    _AlaQoSAppliedConditionSourceNetworkGroupStatus_Type()
)
alaQoSAppliedConditionSourceNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceNetworkGroupStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationIpAddr_Type = IpAddress
_AlaQoSAppliedConditionDestinationIpAddr_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpAddr = _AlaQoSAppliedConditionDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 38),
    _AlaQoSAppliedConditionDestinationIpAddr_Type()
)
alaQoSAppliedConditionDestinationIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpAddr.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpAddrStatus = _AlaQoSAppliedConditionDestinationIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 39),
    _AlaQoSAppliedConditionDestinationIpAddrStatus_Type()
)
alaQoSAppliedConditionDestinationIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpAddrStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationIpMask_Type = IpAddress
_AlaQoSAppliedConditionDestinationIpMask_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpMask = _AlaQoSAppliedConditionDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 40),
    _AlaQoSAppliedConditionDestinationIpMask_Type()
)
alaQoSAppliedConditionDestinationIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpMask.setStatus("current")


class _AlaQoSAppliedConditionDestinationNetworkGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionDestinationNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionDestinationNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionDestinationNetworkGroup_Object = MibTableColumn
alaQoSAppliedConditionDestinationNetworkGroup = _AlaQoSAppliedConditionDestinationNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 41),
    _AlaQoSAppliedConditionDestinationNetworkGroup_Type()
)
alaQoSAppliedConditionDestinationNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationNetworkGroup.setStatus("current")


class _AlaQoSAppliedConditionDestinationNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationNetworkGroupStatus = _AlaQoSAppliedConditionDestinationNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 42),
    _AlaQoSAppliedConditionDestinationNetworkGroupStatus_Type()
)
alaQoSAppliedConditionDestinationNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationNetworkGroupStatus.setStatus("current")
_AlaQoSAppliedConditionMulticastIpAddr_Type = IpAddress
_AlaQoSAppliedConditionMulticastIpAddr_Object = MibTableColumn
alaQoSAppliedConditionMulticastIpAddr = _AlaQoSAppliedConditionMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 43),
    _AlaQoSAppliedConditionMulticastIpAddr_Type()
)
alaQoSAppliedConditionMulticastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastIpAddr.setStatus("current")


class _AlaQoSAppliedConditionMulticastIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionMulticastIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionMulticastIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionMulticastIpAddrStatus_Object = MibTableColumn
alaQoSAppliedConditionMulticastIpAddrStatus = _AlaQoSAppliedConditionMulticastIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 44),
    _AlaQoSAppliedConditionMulticastIpAddrStatus_Type()
)
alaQoSAppliedConditionMulticastIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastIpAddrStatus.setStatus("current")
_AlaQoSAppliedConditionMulticastIpMask_Type = IpAddress
_AlaQoSAppliedConditionMulticastIpMask_Object = MibTableColumn
alaQoSAppliedConditionMulticastIpMask = _AlaQoSAppliedConditionMulticastIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 45),
    _AlaQoSAppliedConditionMulticastIpMask_Type()
)
alaQoSAppliedConditionMulticastIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastIpMask.setStatus("current")


class _AlaQoSAppliedConditionMulticastNetworkGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionMulticastNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionMulticastNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionMulticastNetworkGroup_Object = MibTableColumn
alaQoSAppliedConditionMulticastNetworkGroup = _AlaQoSAppliedConditionMulticastNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 46),
    _AlaQoSAppliedConditionMulticastNetworkGroup_Type()
)
alaQoSAppliedConditionMulticastNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastNetworkGroup.setStatus("current")


class _AlaQoSAppliedConditionMulticastNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionMulticastNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionMulticastNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionMulticastNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionMulticastNetworkGroupStatus = _AlaQoSAppliedConditionMulticastNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 47),
    _AlaQoSAppliedConditionMulticastNetworkGroupStatus_Type()
)
alaQoSAppliedConditionMulticastNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMulticastNetworkGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionTos_Type(Integer32):
    """Custom type alaQoSAppliedConditionTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedConditionTos_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTos_Object = MibTableColumn
alaQoSAppliedConditionTos = _AlaQoSAppliedConditionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 48),
    _AlaQoSAppliedConditionTos_Type()
)
alaQoSAppliedConditionTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTos.setStatus("current")


class _AlaQoSAppliedConditionTosStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTosStatus based on Integer32"""
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


_AlaQoSAppliedConditionTosStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTosStatus_Object = MibTableColumn
alaQoSAppliedConditionTosStatus = _AlaQoSAppliedConditionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 49),
    _AlaQoSAppliedConditionTosStatus_Type()
)
alaQoSAppliedConditionTosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTosStatus.setStatus("current")


class _AlaQoSAppliedConditionTosMask_Type(Integer32):
    """Custom type alaQoSAppliedConditionTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedConditionTosMask_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTosMask_Object = MibTableColumn
alaQoSAppliedConditionTosMask = _AlaQoSAppliedConditionTosMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 50),
    _AlaQoSAppliedConditionTosMask_Type()
)
alaQoSAppliedConditionTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTosMask.setStatus("current")


class _AlaQoSAppliedConditionDscp_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedConditionDscp_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscp_Object = MibTableColumn
alaQoSAppliedConditionDscp = _AlaQoSAppliedConditionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 51),
    _AlaQoSAppliedConditionDscp_Type()
)
alaQoSAppliedConditionDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscp.setStatus("current")


class _AlaQoSAppliedConditionDscpStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscpStatus based on Integer32"""
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


_AlaQoSAppliedConditionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscpStatus_Object = MibTableColumn
alaQoSAppliedConditionDscpStatus = _AlaQoSAppliedConditionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 52),
    _AlaQoSAppliedConditionDscpStatus_Type()
)
alaQoSAppliedConditionDscpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscpStatus.setStatus("current")


class _AlaQoSAppliedConditionDscpMask_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedConditionDscpMask_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscpMask_Object = MibTableColumn
alaQoSAppliedConditionDscpMask = _AlaQoSAppliedConditionDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 53),
    _AlaQoSAppliedConditionDscpMask_Type()
)
alaQoSAppliedConditionDscpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscpMask.setStatus("current")


class _AlaQoSAppliedConditionIpProtocol_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIpProtocol_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpProtocol_Object = MibTableColumn
alaQoSAppliedConditionIpProtocol = _AlaQoSAppliedConditionIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 54),
    _AlaQoSAppliedConditionIpProtocol_Type()
)
alaQoSAppliedConditionIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpProtocol.setStatus("current")


class _AlaQoSAppliedConditionIpProtocolStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpProtocolStatus based on Integer32"""
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


_AlaQoSAppliedConditionIpProtocolStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpProtocolStatus_Object = MibTableColumn
alaQoSAppliedConditionIpProtocolStatus = _AlaQoSAppliedConditionIpProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 55),
    _AlaQoSAppliedConditionIpProtocolStatus_Type()
)
alaQoSAppliedConditionIpProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpProtocolStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceIpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpPort_Object = MibTableColumn
alaQoSAppliedConditionSourceIpPort = _AlaQoSAppliedConditionSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 56),
    _AlaQoSAppliedConditionSourceIpPort_Type()
)
alaQoSAppliedConditionSourceIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpPort.setStatus("current")


class _AlaQoSAppliedConditionSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceIpPortStatus = _AlaQoSAppliedConditionSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 57),
    _AlaQoSAppliedConditionSourceIpPortStatus_Type()
)
alaQoSAppliedConditionSourceIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpPort = _AlaQoSAppliedConditionDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 58),
    _AlaQoSAppliedConditionDestinationIpPort_Type()
)
alaQoSAppliedConditionDestinationIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpPortStatus = _AlaQoSAppliedConditionDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 59),
    _AlaQoSAppliedConditionDestinationIpPortStatus_Type()
)
alaQoSAppliedConditionDestinationIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionService_Type(DisplayString):
    """Custom type alaQoSAppliedConditionService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionService_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionService_Object = MibTableColumn
alaQoSAppliedConditionService = _AlaQoSAppliedConditionService_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 60),
    _AlaQoSAppliedConditionService_Type()
)
alaQoSAppliedConditionService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionService.setStatus("current")


class _AlaQoSAppliedConditionServiceStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionServiceStatus based on Integer32"""
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


_AlaQoSAppliedConditionServiceStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionServiceStatus_Object = MibTableColumn
alaQoSAppliedConditionServiceStatus = _AlaQoSAppliedConditionServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 61),
    _AlaQoSAppliedConditionServiceStatus_Type()
)
alaQoSAppliedConditionServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionServiceStatus.setStatus("current")


class _AlaQoSAppliedConditionServiceGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionServiceGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionServiceGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionServiceGroup_Object = MibTableColumn
alaQoSAppliedConditionServiceGroup = _AlaQoSAppliedConditionServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 62),
    _AlaQoSAppliedConditionServiceGroup_Type()
)
alaQoSAppliedConditionServiceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionServiceGroup.setStatus("current")


class _AlaQoSAppliedConditionServiceGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionServiceGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionServiceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionServiceGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionServiceGroupStatus = _AlaQoSAppliedConditionServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 63),
    _AlaQoSAppliedConditionServiceGroupStatus_Type()
)
alaQoSAppliedConditionServiceGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionServiceGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionIcmpType_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIcmpType_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpType_Object = MibTableColumn
alaQoSAppliedConditionIcmpType = _AlaQoSAppliedConditionIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 64),
    _AlaQoSAppliedConditionIcmpType_Type()
)
alaQoSAppliedConditionIcmpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpType.setStatus("current")


class _AlaQoSAppliedConditionIcmpTypeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpTypeStatus based on Integer32"""
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


_AlaQoSAppliedConditionIcmpTypeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpTypeStatus_Object = MibTableColumn
alaQoSAppliedConditionIcmpTypeStatus = _AlaQoSAppliedConditionIcmpTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 65),
    _AlaQoSAppliedConditionIcmpTypeStatus_Type()
)
alaQoSAppliedConditionIcmpTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpTypeStatus.setStatus("current")


class _AlaQoSAppliedConditionIcmpCode_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIcmpCode_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpCode_Object = MibTableColumn
alaQoSAppliedConditionIcmpCode = _AlaQoSAppliedConditionIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 66),
    _AlaQoSAppliedConditionIcmpCode_Type()
)
alaQoSAppliedConditionIcmpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpCode.setStatus("current")


class _AlaQoSAppliedConditionIcmpCodeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIcmpCodeStatus based on Integer32"""
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


_AlaQoSAppliedConditionIcmpCodeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIcmpCodeStatus_Object = MibTableColumn
alaQoSAppliedConditionIcmpCodeStatus = _AlaQoSAppliedConditionIcmpCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 67),
    _AlaQoSAppliedConditionIcmpCodeStatus_Type()
)
alaQoSAppliedConditionIcmpCodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIcmpCodeStatus.setStatus("current")


class _AlaQoSAppliedConditionDlci_Type(Integer32):
    """Custom type alaQoSAppliedConditionDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_AlaQoSAppliedConditionDlci_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDlci_Object = MibTableColumn
alaQoSAppliedConditionDlci = _AlaQoSAppliedConditionDlci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 68),
    _AlaQoSAppliedConditionDlci_Type()
)
alaQoSAppliedConditionDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDlci.setStatus("current")


class _AlaQoSAppliedConditionDlciStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDlciStatus based on Integer32"""
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


_AlaQoSAppliedConditionDlciStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDlciStatus_Object = MibTableColumn
alaQoSAppliedConditionDlciStatus = _AlaQoSAppliedConditionDlciStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 69),
    _AlaQoSAppliedConditionDlciStatus_Type()
)
alaQoSAppliedConditionDlciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDlciStatus.setStatus("current")
_AlaQoSAppliedConditionRowStatus_Type = RowStatus
_AlaQoSAppliedConditionRowStatus_Object = MibTableColumn
alaQoSAppliedConditionRowStatus = _AlaQoSAppliedConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 70),
    _AlaQoSAppliedConditionRowStatus_Type()
)
alaQoSAppliedConditionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionRowStatus.setStatus("current")


class _AlaQoSAppliedConditionSourcePortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionSourcePortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourcePortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourcePortEnd = _AlaQoSAppliedConditionSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 71),
    _AlaQoSAppliedConditionSourcePortEnd_Type()
)
alaQoSAppliedConditionSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourcePortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedConditionDestinationPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationPortEnd = _AlaQoSAppliedConditionDestinationPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 72),
    _AlaQoSAppliedConditionDestinationPortEnd_Type()
)
alaQoSAppliedConditionDestinationPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationPortEnd.setStatus("current")


class _AlaQoSAppliedConditionSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourceIpPortEnd = _AlaQoSAppliedConditionSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 73),
    _AlaQoSAppliedConditionSourceIpPortEnd_Type()
)
alaQoSAppliedConditionSourceIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpPortEnd = _AlaQoSAppliedConditionDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 74),
    _AlaQoSAppliedConditionDestinationIpPortEnd_Type()
)
alaQoSAppliedConditionDestinationIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionSourceTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceTcpPort_Object = MibTableColumn
alaQoSAppliedConditionSourceTcpPort = _AlaQoSAppliedConditionSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 75),
    _AlaQoSAppliedConditionSourceTcpPort_Type()
)
alaQoSAppliedConditionSourceTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceTcpPort.setStatus("current")


class _AlaQoSAppliedConditionSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceTcpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceTcpPortStatus = _AlaQoSAppliedConditionSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 76),
    _AlaQoSAppliedConditionSourceTcpPortStatus_Type()
)
alaQoSAppliedConditionSourceTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceTcpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceTcpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourceTcpPortEnd = _AlaQoSAppliedConditionSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 77),
    _AlaQoSAppliedConditionSourceTcpPortEnd_Type()
)
alaQoSAppliedConditionSourceTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceTcpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationTcpPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationTcpPort = _AlaQoSAppliedConditionDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 78),
    _AlaQoSAppliedConditionDestinationTcpPort_Type()
)
alaQoSAppliedConditionDestinationTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationTcpPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationTcpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationTcpPortStatus = _AlaQoSAppliedConditionDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 79),
    _AlaQoSAppliedConditionDestinationTcpPortStatus_Type()
)
alaQoSAppliedConditionDestinationTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationTcpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationTcpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationTcpPortEnd = _AlaQoSAppliedConditionDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 80),
    _AlaQoSAppliedConditionDestinationTcpPortEnd_Type()
)
alaQoSAppliedConditionDestinationTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationTcpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionSourceUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceUdpPort_Object = MibTableColumn
alaQoSAppliedConditionSourceUdpPort = _AlaQoSAppliedConditionSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 81),
    _AlaQoSAppliedConditionSourceUdpPort_Type()
)
alaQoSAppliedConditionSourceUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceUdpPort.setStatus("current")


class _AlaQoSAppliedConditionSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceUdpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceUdpPortStatus = _AlaQoSAppliedConditionSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 82),
    _AlaQoSAppliedConditionSourceUdpPortStatus_Type()
)
alaQoSAppliedConditionSourceUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceUdpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceUdpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionSourceUdpPortEnd = _AlaQoSAppliedConditionSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 83),
    _AlaQoSAppliedConditionSourceUdpPortEnd_Type()
)
alaQoSAppliedConditionSourceUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceUdpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationUdpPort_Object = MibTableColumn
alaQoSAppliedConditionDestinationUdpPort = _AlaQoSAppliedConditionDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 84),
    _AlaQoSAppliedConditionDestinationUdpPort_Type()
)
alaQoSAppliedConditionDestinationUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationUdpPort.setStatus("current")


class _AlaQoSAppliedConditionDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationUdpPortStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationUdpPortStatus = _AlaQoSAppliedConditionDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 85),
    _AlaQoSAppliedConditionDestinationUdpPortStatus_Type()
)
alaQoSAppliedConditionDestinationUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationUdpPortStatus.setStatus("current")


class _AlaQoSAppliedConditionDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationUdpPortEnd_Object = MibTableColumn
alaQoSAppliedConditionDestinationUdpPortEnd = _AlaQoSAppliedConditionDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 86),
    _AlaQoSAppliedConditionDestinationUdpPortEnd_Type()
)
alaQoSAppliedConditionDestinationUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationUdpPortEnd.setStatus("current")


class _AlaQoSAppliedConditionEthertype_Type(Integer32):
    """Custom type alaQoSAppliedConditionEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedConditionEthertype_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionEthertype_Object = MibTableColumn
alaQoSAppliedConditionEthertype = _AlaQoSAppliedConditionEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 87),
    _AlaQoSAppliedConditionEthertype_Type()
)
alaQoSAppliedConditionEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionEthertype.setStatus("current")


class _AlaQoSAppliedConditionEthertypeStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionEthertypeStatus based on Integer32"""
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


_AlaQoSAppliedConditionEthertypeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionEthertypeStatus_Object = MibTableColumn
alaQoSAppliedConditionEthertypeStatus = _AlaQoSAppliedConditionEthertypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 88),
    _AlaQoSAppliedConditionEthertypeStatus_Type()
)
alaQoSAppliedConditionEthertypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionEthertypeStatus.setStatus("current")


class _AlaQoSAppliedConditionTcpFlags_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("any", 2))
    )


_AlaQoSAppliedConditionTcpFlags_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlags_Object = MibTableColumn
alaQoSAppliedConditionTcpFlags = _AlaQoSAppliedConditionTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 89),
    _AlaQoSAppliedConditionTcpFlags_Type()
)
alaQoSAppliedConditionTcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlags.setStatus("current")


class _AlaQoSAppliedConditionTcpFlagsStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlagsStatus based on Integer32"""
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


_AlaQoSAppliedConditionTcpFlagsStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlagsStatus_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsStatus = _AlaQoSAppliedConditionTcpFlagsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 90),
    _AlaQoSAppliedConditionTcpFlagsStatus_Type()
)
alaQoSAppliedConditionTcpFlagsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsStatus.setStatus("current")
_AlaQoSAppliedConditionTcpFlagsVal_Type = Integer32
_AlaQoSAppliedConditionTcpFlagsVal_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsVal = _AlaQoSAppliedConditionTcpFlagsVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 91),
    _AlaQoSAppliedConditionTcpFlagsVal_Type()
)
alaQoSAppliedConditionTcpFlagsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsVal.setStatus("current")


class _AlaQoSAppliedConditionTcpFlagsValStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlagsValStatus based on Integer32"""
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


_AlaQoSAppliedConditionTcpFlagsValStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlagsValStatus_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsValStatus = _AlaQoSAppliedConditionTcpFlagsValStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 92),
    _AlaQoSAppliedConditionTcpFlagsValStatus_Type()
)
alaQoSAppliedConditionTcpFlagsValStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsValStatus.setStatus("current")
_AlaQoSAppliedConditionTcpFlagsMask_Type = Integer32
_AlaQoSAppliedConditionTcpFlagsMask_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsMask = _AlaQoSAppliedConditionTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 93),
    _AlaQoSAppliedConditionTcpFlagsMask_Type()
)
alaQoSAppliedConditionTcpFlagsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsMask.setStatus("current")


class _AlaQoSAppliedConditionTcpFlagsMaskStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpFlagsMaskStatus based on Integer32"""
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


_AlaQoSAppliedConditionTcpFlagsMaskStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpFlagsMaskStatus_Object = MibTableColumn
alaQoSAppliedConditionTcpFlagsMaskStatus = _AlaQoSAppliedConditionTcpFlagsMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 94),
    _AlaQoSAppliedConditionTcpFlagsMaskStatus_Type()
)
alaQoSAppliedConditionTcpFlagsMaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpFlagsMaskStatus.setStatus("current")


class _AlaQoSAppliedConditionTcpEstablished_Type(Integer32):
    """Custom type alaQoSAppliedConditionTcpEstablished based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedConditionTcpEstablished_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionTcpEstablished_Object = MibTableColumn
alaQoSAppliedConditionTcpEstablished = _AlaQoSAppliedConditionTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 95),
    _AlaQoSAppliedConditionTcpEstablished_Type()
)
alaQoSAppliedConditionTcpEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionTcpEstablished.setStatus("current")
_AlaQoSAppliedConditionSourceIpv6Addr_Type = Ipv6Address
_AlaQoSAppliedConditionSourceIpv6Addr_Object = MibTableColumn
alaQoSAppliedConditionSourceIpv6Addr = _AlaQoSAppliedConditionSourceIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 96),
    _AlaQoSAppliedConditionSourceIpv6Addr_Type()
)
alaQoSAppliedConditionSourceIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpv6Addr.setStatus("current")


class _AlaQoSAppliedConditionSourceIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceIpv6AddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceIpv6AddrStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceIpv6AddrStatus = _AlaQoSAppliedConditionSourceIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 97),
    _AlaQoSAppliedConditionSourceIpv6AddrStatus_Type()
)
alaQoSAppliedConditionSourceIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpv6AddrStatus.setStatus("current")
_AlaQoSAppliedConditionSourceIpv6Mask_Type = Ipv6Address
_AlaQoSAppliedConditionSourceIpv6Mask_Object = MibTableColumn
alaQoSAppliedConditionSourceIpv6Mask = _AlaQoSAppliedConditionSourceIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 98),
    _AlaQoSAppliedConditionSourceIpv6Mask_Type()
)
alaQoSAppliedConditionSourceIpv6Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceIpv6Mask.setStatus("current")
_AlaQoSAppliedConditionDestinationIpv6Addr_Type = Ipv6Address
_AlaQoSAppliedConditionDestinationIpv6Addr_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpv6Addr = _AlaQoSAppliedConditionDestinationIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 99),
    _AlaQoSAppliedConditionDestinationIpv6Addr_Type()
)
alaQoSAppliedConditionDestinationIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpv6Addr.setStatus("current")


class _AlaQoSAppliedConditionDestinationIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionDestinationIpv6AddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionDestinationIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDestinationIpv6AddrStatus_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpv6AddrStatus = _AlaQoSAppliedConditionDestinationIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 100),
    _AlaQoSAppliedConditionDestinationIpv6AddrStatus_Type()
)
alaQoSAppliedConditionDestinationIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpv6AddrStatus.setStatus("current")
_AlaQoSAppliedConditionDestinationIpv6Mask_Type = Ipv6Address
_AlaQoSAppliedConditionDestinationIpv6Mask_Object = MibTableColumn
alaQoSAppliedConditionDestinationIpv6Mask = _AlaQoSAppliedConditionDestinationIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 101),
    _AlaQoSAppliedConditionDestinationIpv6Mask_Type()
)
alaQoSAppliedConditionDestinationIpv6Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDestinationIpv6Mask.setStatus("current")


class _AlaQoSAppliedConditionIpv6Traffic_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6Traffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedConditionIpv6Traffic_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6Traffic_Object = MibTableColumn
alaQoSAppliedConditionIpv6Traffic = _AlaQoSAppliedConditionIpv6Traffic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 102),
    _AlaQoSAppliedConditionIpv6Traffic_Type()
)
alaQoSAppliedConditionIpv6Traffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6Traffic.setStatus("current")


class _AlaQoSAppliedConditionIpv6NH_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6NH based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedConditionIpv6NH_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6NH_Object = MibTableColumn
alaQoSAppliedConditionIpv6NH = _AlaQoSAppliedConditionIpv6NH_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 103),
    _AlaQoSAppliedConditionIpv6NH_Type()
)
alaQoSAppliedConditionIpv6NH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6NH.setStatus("current")


class _AlaQoSAppliedConditionIpv6NHStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6NHStatus based on Integer32"""
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


_AlaQoSAppliedConditionIpv6NHStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6NHStatus_Object = MibTableColumn
alaQoSAppliedConditionIpv6NHStatus = _AlaQoSAppliedConditionIpv6NHStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 104),
    _AlaQoSAppliedConditionIpv6NHStatus_Type()
)
alaQoSAppliedConditionIpv6NHStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6NHStatus.setStatus("current")


class _AlaQoSAppliedConditionIpv6FlowLabel_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6FlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AlaQoSAppliedConditionIpv6FlowLabel_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6FlowLabel_Object = MibTableColumn
alaQoSAppliedConditionIpv6FlowLabel = _AlaQoSAppliedConditionIpv6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 105),
    _AlaQoSAppliedConditionIpv6FlowLabel_Type()
)
alaQoSAppliedConditionIpv6FlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6FlowLabel.setStatus("current")


class _AlaQoSAppliedConditionIpv6FlowLabelStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionIpv6FlowLabelStatus based on Integer32"""
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


_AlaQoSAppliedConditionIpv6FlowLabelStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionIpv6FlowLabelStatus_Object = MibTableColumn
alaQoSAppliedConditionIpv6FlowLabelStatus = _AlaQoSAppliedConditionIpv6FlowLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 106),
    _AlaQoSAppliedConditionIpv6FlowLabelStatus_Type()
)
alaQoSAppliedConditionIpv6FlowLabelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionIpv6FlowLabelStatus.setStatus("current")


class _AlaQoSAppliedConditionMcastIpv6Addr_Type(Ipv6Address):
    """Custom type alaQoSAppliedConditionMcastIpv6Addr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_AlaQoSAppliedConditionMcastIpv6Addr_Object = MibTableColumn
alaQoSAppliedConditionMcastIpv6Addr = _AlaQoSAppliedConditionMcastIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 107),
    _AlaQoSAppliedConditionMcastIpv6Addr_Type()
)
alaQoSAppliedConditionMcastIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMcastIpv6Addr.setStatus("current")


class _AlaQoSAppliedConditionMcastIpv6AddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionMcastIpv6AddrStatus based on Integer32"""
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


_AlaQoSAppliedConditionMcastIpv6AddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionMcastIpv6AddrStatus_Object = MibTableColumn
alaQoSAppliedConditionMcastIpv6AddrStatus = _AlaQoSAppliedConditionMcastIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 108),
    _AlaQoSAppliedConditionMcastIpv6AddrStatus_Type()
)
alaQoSAppliedConditionMcastIpv6AddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMcastIpv6AddrStatus.setStatus("current")


class _AlaQoSAppliedConditionMcastIpv6Mask_Type(Ipv6Address):
    """Custom type alaQoSAppliedConditionMcastIpv6Mask based on Ipv6Address"""
    defaultHexValue = "ffffffffffffffffffffffffffffffff"


_AlaQoSAppliedConditionMcastIpv6Mask_Object = MibTableColumn
alaQoSAppliedConditionMcastIpv6Mask = _AlaQoSAppliedConditionMcastIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 109),
    _AlaQoSAppliedConditionMcastIpv6Mask_Type()
)
alaQoSAppliedConditionMcastIpv6Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionMcastIpv6Mask.setStatus("current")


class _AlaQoSAppliedConditionDscpEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionDscpEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedConditionDscpEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionDscpEnd_Object = MibTableColumn
alaQoSAppliedConditionDscpEnd = _AlaQoSAppliedConditionDscpEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 110),
    _AlaQoSAppliedConditionDscpEnd_Type()
)
alaQoSAppliedConditionDscpEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionDscpEnd.setStatus("current")


class _AlaQoSAppliedConditionInnerSourceVlan_Type(Integer32):
    """Custom type alaQoSAppliedConditionInnerSourceVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSAppliedConditionInnerSourceVlan_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInnerSourceVlan_Object = MibTableColumn
alaQoSAppliedConditionInnerSourceVlan = _AlaQoSAppliedConditionInnerSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 111),
    _AlaQoSAppliedConditionInnerSourceVlan_Type()
)
alaQoSAppliedConditionInnerSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInnerSourceVlan.setStatus("current")


class _AlaQoSAppliedConditionInnerSourceVlanStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionInnerSourceVlanStatus based on Integer32"""
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


_AlaQoSAppliedConditionInnerSourceVlanStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInnerSourceVlanStatus_Object = MibTableColumn
alaQoSAppliedConditionInnerSourceVlanStatus = _AlaQoSAppliedConditionInnerSourceVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 112),
    _AlaQoSAppliedConditionInnerSourceVlanStatus_Type()
)
alaQoSAppliedConditionInnerSourceVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInnerSourceVlanStatus.setStatus("current")


class _AlaQoSAppliedConditionInner8021p_Type(Integer32):
    """Custom type alaQoSAppliedConditionInner8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedConditionInner8021p_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInner8021p_Object = MibTableColumn
alaQoSAppliedConditionInner8021p = _AlaQoSAppliedConditionInner8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 113),
    _AlaQoSAppliedConditionInner8021p_Type()
)
alaQoSAppliedConditionInner8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInner8021p.setStatus("current")


class _AlaQoSAppliedConditionInner8021pStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionInner8021pStatus based on Integer32"""
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


_AlaQoSAppliedConditionInner8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInner8021pStatus_Object = MibTableColumn
alaQoSAppliedConditionInner8021pStatus = _AlaQoSAppliedConditionInner8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 114),
    _AlaQoSAppliedConditionInner8021pStatus_Type()
)
alaQoSAppliedConditionInner8021pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInner8021pStatus.setStatus("current")


class _AlaQoSAppliedConditionVrfName_Type(DisplayString):
    """Custom type alaQoSAppliedConditionVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionVrfName_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionVrfName_Object = MibTableColumn
alaQoSAppliedConditionVrfName = _AlaQoSAppliedConditionVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 115),
    _AlaQoSAppliedConditionVrfName_Type()
)
alaQoSAppliedConditionVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVrfName.setStatus("current")


class _AlaQoSAppliedConditionVrfNameStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionVrfNameStatus based on Integer32"""
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


_AlaQoSAppliedConditionVrfNameStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionVrfNameStatus_Object = MibTableColumn
alaQoSAppliedConditionVrfNameStatus = _AlaQoSAppliedConditionVrfNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 116),
    _AlaQoSAppliedConditionVrfNameStatus_Type()
)
alaQoSAppliedConditionVrfNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionVrfNameStatus.setStatus("current")


class _AlaQoSAppliedCondition8021pEnd_Type(Integer32):
    """Custom type alaQoSAppliedCondition8021pEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedCondition8021pEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedCondition8021pEnd_Object = MibTableColumn
alaQoSAppliedCondition8021pEnd = _AlaQoSAppliedCondition8021pEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 117),
    _AlaQoSAppliedCondition8021pEnd_Type()
)
alaQoSAppliedCondition8021pEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedCondition8021pEnd.setStatus("current")


class _AlaQoSAppliedConditionInner8021pEnd_Type(Integer32):
    """Custom type alaQoSAppliedConditionInner8021pEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedConditionInner8021pEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInner8021pEnd_Object = MibTableColumn
alaQoSAppliedConditionInner8021pEnd = _AlaQoSAppliedConditionInner8021pEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 118),
    _AlaQoSAppliedConditionInner8021pEnd_Type()
)
alaQoSAppliedConditionInner8021pEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInner8021pEnd.setStatus("current")


class _AlaQoSAppliedConditionSourceVlanGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionSourceVlanGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionSourceVlanGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionSourceVlanGroup_Object = MibTableColumn
alaQoSAppliedConditionSourceVlanGroup = _AlaQoSAppliedConditionSourceVlanGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 119),
    _AlaQoSAppliedConditionSourceVlanGroup_Type()
)
alaQoSAppliedConditionSourceVlanGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceVlanGroup.setStatus("current")


class _AlaQoSAppliedConditionSourceVlanGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionSourceVlanGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionSourceVlanGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionSourceVlanGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionSourceVlanGroupStatus = _AlaQoSAppliedConditionSourceVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 120),
    _AlaQoSAppliedConditionSourceVlanGroupStatus_Type()
)
alaQoSAppliedConditionSourceVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionSourceVlanGroupStatus.setStatus("current")


class _AlaQoSAppliedConditionInnerSourceVlanGroup_Type(DisplayString):
    """Custom type alaQoSAppliedConditionInnerSourceVlanGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedConditionInnerSourceVlanGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedConditionInnerSourceVlanGroup_Object = MibTableColumn
alaQoSAppliedConditionInnerSourceVlanGroup = _AlaQoSAppliedConditionInnerSourceVlanGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 121),
    _AlaQoSAppliedConditionInnerSourceVlanGroup_Type()
)
alaQoSAppliedConditionInnerSourceVlanGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInnerSourceVlanGroup.setStatus("current")


class _AlaQoSAppliedConditionInnerSourceVlanGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedConditionInnerSourceVlanGroupStatus based on Integer32"""
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


_AlaQoSAppliedConditionInnerSourceVlanGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedConditionInnerSourceVlanGroupStatus_Object = MibTableColumn
alaQoSAppliedConditionInnerSourceVlanGroupStatus = _AlaQoSAppliedConditionInnerSourceVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 4, 1, 122),
    _AlaQoSAppliedConditionInnerSourceVlanGroupStatus_Type()
)
alaQoSAppliedConditionInnerSourceVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedConditionInnerSourceVlanGroupStatus.setStatus("current")
_AlaQoSServiceTable_Object = MibTable
alaQoSServiceTable = _AlaQoSServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaQoSServiceTable.setStatus("current")
_AlaQoSServiceEntry_Object = MibTableRow
alaQoSServiceEntry = _AlaQoSServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1)
)
alaQoSServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSServiceEntry.setStatus("current")


class _AlaQoSServiceName_Type(DisplayString):
    """Custom type alaQoSServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSServiceName_Type.__name__ = "DisplayString"
_AlaQoSServiceName_Object = MibTableColumn
alaQoSServiceName = _AlaQoSServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 1),
    _AlaQoSServiceName_Type()
)
alaQoSServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSServiceName.setStatus("current")


class _AlaQoSServiceSource_Type(Integer32):
    """Custom type alaQoSServiceSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSServiceSource_Type.__name__ = "Integer32"
_AlaQoSServiceSource_Object = MibTableColumn
alaQoSServiceSource = _AlaQoSServiceSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 2),
    _AlaQoSServiceSource_Type()
)
alaQoSServiceSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSource.setStatus("current")


class _AlaQoSServiceProtocol_Type(Integer32):
    """Custom type alaQoSServiceProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSServiceProtocol_Type.__name__ = "Integer32"
_AlaQoSServiceProtocol_Object = MibTableColumn
alaQoSServiceProtocol = _AlaQoSServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 3),
    _AlaQoSServiceProtocol_Type()
)
alaQoSServiceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceProtocol.setStatus("current")


class _AlaQoSServiceSourceIpPort_Type(Integer32):
    """Custom type alaQoSServiceSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSServiceSourceIpPort_Object = MibTableColumn
alaQoSServiceSourceIpPort = _AlaQoSServiceSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 4),
    _AlaQoSServiceSourceIpPort_Type()
)
alaQoSServiceSourceIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceIpPort.setStatus("current")


class _AlaQoSServiceSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceSourceIpPortStatus based on Integer32"""
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


_AlaQoSServiceSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceSourceIpPortStatus_Object = MibTableColumn
alaQoSServiceSourceIpPortStatus = _AlaQoSServiceSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 5),
    _AlaQoSServiceSourceIpPortStatus_Type()
)
alaQoSServiceSourceIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceIpPortStatus.setStatus("current")


class _AlaQoSServiceDestinationIpPort_Type(Integer32):
    """Custom type alaQoSServiceDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationIpPort_Object = MibTableColumn
alaQoSServiceDestinationIpPort = _AlaQoSServiceDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 6),
    _AlaQoSServiceDestinationIpPort_Type()
)
alaQoSServiceDestinationIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationIpPort.setStatus("current")


class _AlaQoSServiceDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceDestinationIpPortStatus based on Integer32"""
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


_AlaQoSServiceDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationIpPortStatus_Object = MibTableColumn
alaQoSServiceDestinationIpPortStatus = _AlaQoSServiceDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 7),
    _AlaQoSServiceDestinationIpPortStatus_Type()
)
alaQoSServiceDestinationIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationIpPortStatus.setStatus("current")
_AlaQoSServiceRowStatus_Type = RowStatus
_AlaQoSServiceRowStatus_Object = MibTableColumn
alaQoSServiceRowStatus = _AlaQoSServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 8),
    _AlaQoSServiceRowStatus_Type()
)
alaQoSServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceRowStatus.setStatus("current")


class _AlaQoSServiceSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceSourceIpPortEnd_Object = MibTableColumn
alaQoSServiceSourceIpPortEnd = _AlaQoSServiceSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 9),
    _AlaQoSServiceSourceIpPortEnd_Type()
)
alaQoSServiceSourceIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceIpPortEnd.setStatus("current")


class _AlaQoSServiceDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationIpPortEnd_Object = MibTableColumn
alaQoSServiceDestinationIpPortEnd = _AlaQoSServiceDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 10),
    _AlaQoSServiceDestinationIpPortEnd_Type()
)
alaQoSServiceDestinationIpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationIpPortEnd.setStatus("current")


class _AlaQoSServiceSourceTcpPort_Type(Integer32):
    """Custom type alaQoSServiceSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSServiceSourceTcpPort_Object = MibTableColumn
alaQoSServiceSourceTcpPort = _AlaQoSServiceSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 11),
    _AlaQoSServiceSourceTcpPort_Type()
)
alaQoSServiceSourceTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceTcpPort.setStatus("current")


class _AlaQoSServiceSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceSourceTcpPortStatus based on Integer32"""
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


_AlaQoSServiceSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceSourceTcpPortStatus_Object = MibTableColumn
alaQoSServiceSourceTcpPortStatus = _AlaQoSServiceSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 12),
    _AlaQoSServiceSourceTcpPortStatus_Type()
)
alaQoSServiceSourceTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceTcpPortStatus.setStatus("current")


class _AlaQoSServiceSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceSourceTcpPortEnd_Object = MibTableColumn
alaQoSServiceSourceTcpPortEnd = _AlaQoSServiceSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 13),
    _AlaQoSServiceSourceTcpPortEnd_Type()
)
alaQoSServiceSourceTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceTcpPortEnd.setStatus("current")


class _AlaQoSServiceDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSServiceDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationTcpPort_Object = MibTableColumn
alaQoSServiceDestinationTcpPort = _AlaQoSServiceDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 14),
    _AlaQoSServiceDestinationTcpPort_Type()
)
alaQoSServiceDestinationTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationTcpPort.setStatus("current")


class _AlaQoSServiceDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceDestinationTcpPortStatus based on Integer32"""
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


_AlaQoSServiceDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationTcpPortStatus_Object = MibTableColumn
alaQoSServiceDestinationTcpPortStatus = _AlaQoSServiceDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 15),
    _AlaQoSServiceDestinationTcpPortStatus_Type()
)
alaQoSServiceDestinationTcpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationTcpPortStatus.setStatus("current")


class _AlaQoSServiceDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationTcpPortEnd_Object = MibTableColumn
alaQoSServiceDestinationTcpPortEnd = _AlaQoSServiceDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 16),
    _AlaQoSServiceDestinationTcpPortEnd_Type()
)
alaQoSServiceDestinationTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationTcpPortEnd.setStatus("current")


class _AlaQoSServiceSourceUdpPort_Type(Integer32):
    """Custom type alaQoSServiceSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSServiceSourceUdpPort_Object = MibTableColumn
alaQoSServiceSourceUdpPort = _AlaQoSServiceSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 17),
    _AlaQoSServiceSourceUdpPort_Type()
)
alaQoSServiceSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceUdpPort.setStatus("current")


class _AlaQoSServiceSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceSourceUdpPortStatus based on Integer32"""
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


_AlaQoSServiceSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceSourceUdpPortStatus_Object = MibTableColumn
alaQoSServiceSourceUdpPortStatus = _AlaQoSServiceSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 18),
    _AlaQoSServiceSourceUdpPortStatus_Type()
)
alaQoSServiceSourceUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceUdpPortStatus.setStatus("current")


class _AlaQoSServiceSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceSourceUdpPortEnd_Object = MibTableColumn
alaQoSServiceSourceUdpPortEnd = _AlaQoSServiceSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 19),
    _AlaQoSServiceSourceUdpPortEnd_Type()
)
alaQoSServiceSourceUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceSourceUdpPortEnd.setStatus("current")


class _AlaQoSServiceDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSServiceDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationUdpPort_Object = MibTableColumn
alaQoSServiceDestinationUdpPort = _AlaQoSServiceDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 20),
    _AlaQoSServiceDestinationUdpPort_Type()
)
alaQoSServiceDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationUdpPort.setStatus("current")


class _AlaQoSServiceDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSServiceDestinationUdpPortStatus based on Integer32"""
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


_AlaQoSServiceDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationUdpPortStatus_Object = MibTableColumn
alaQoSServiceDestinationUdpPortStatus = _AlaQoSServiceDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 21),
    _AlaQoSServiceDestinationUdpPortStatus_Type()
)
alaQoSServiceDestinationUdpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationUdpPortStatus.setStatus("current")


class _AlaQoSServiceDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSServiceDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSServiceDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSServiceDestinationUdpPortEnd_Object = MibTableColumn
alaQoSServiceDestinationUdpPortEnd = _AlaQoSServiceDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 5, 1, 22),
    _AlaQoSServiceDestinationUdpPortEnd_Type()
)
alaQoSServiceDestinationUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceDestinationUdpPortEnd.setStatus("current")
_AlaQoSAppliedServiceTable_Object = MibTable
alaQoSAppliedServiceTable = _AlaQoSAppliedServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceTable.setStatus("current")
_AlaQoSAppliedServiceEntry_Object = MibTableRow
alaQoSAppliedServiceEntry = _AlaQoSAppliedServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1)
)
alaQoSAppliedServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceEntry.setStatus("current")


class _AlaQoSAppliedServiceName_Type(DisplayString):
    """Custom type alaQoSAppliedServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedServiceName_Type.__name__ = "DisplayString"
_AlaQoSAppliedServiceName_Object = MibTableColumn
alaQoSAppliedServiceName = _AlaQoSAppliedServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 1),
    _AlaQoSAppliedServiceName_Type()
)
alaQoSAppliedServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceName.setStatus("current")


class _AlaQoSAppliedServiceSource_Type(Integer32):
    """Custom type alaQoSAppliedServiceSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedServiceSource_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSource_Object = MibTableColumn
alaQoSAppliedServiceSource = _AlaQoSAppliedServiceSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 2),
    _AlaQoSAppliedServiceSource_Type()
)
alaQoSAppliedServiceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSource.setStatus("current")


class _AlaQoSAppliedServiceProtocol_Type(Integer32):
    """Custom type alaQoSAppliedServiceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSAppliedServiceProtocol_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceProtocol_Object = MibTableColumn
alaQoSAppliedServiceProtocol = _AlaQoSAppliedServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 3),
    _AlaQoSAppliedServiceProtocol_Type()
)
alaQoSAppliedServiceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceProtocol.setStatus("current")


class _AlaQoSAppliedServiceSourceIpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceIpPort_Object = MibTableColumn
alaQoSAppliedServiceSourceIpPort = _AlaQoSAppliedServiceSourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 4),
    _AlaQoSAppliedServiceSourceIpPort_Type()
)
alaQoSAppliedServiceSourceIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceIpPort.setStatus("current")


class _AlaQoSAppliedServiceSourceIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceIpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceSourceIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceIpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceSourceIpPortStatus = _AlaQoSAppliedServiceSourceIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 5),
    _AlaQoSAppliedServiceSourceIpPortStatus_Type()
)
alaQoSAppliedServiceSourceIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceIpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceDestinationIpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationIpPort_Object = MibTableColumn
alaQoSAppliedServiceDestinationIpPort = _AlaQoSAppliedServiceDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 6),
    _AlaQoSAppliedServiceDestinationIpPort_Type()
)
alaQoSAppliedServiceDestinationIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationIpPort.setStatus("current")


class _AlaQoSAppliedServiceDestinationIpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationIpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceDestinationIpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationIpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceDestinationIpPortStatus = _AlaQoSAppliedServiceDestinationIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 7),
    _AlaQoSAppliedServiceDestinationIpPortStatus_Type()
)
alaQoSAppliedServiceDestinationIpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationIpPortStatus.setStatus("current")
_AlaQoSAppliedServiceRowStatus_Type = RowStatus
_AlaQoSAppliedServiceRowStatus_Object = MibTableColumn
alaQoSAppliedServiceRowStatus = _AlaQoSAppliedServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 8),
    _AlaQoSAppliedServiceRowStatus_Type()
)
alaQoSAppliedServiceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceRowStatus.setStatus("current")


class _AlaQoSAppliedServiceSourceIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceIpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceSourceIpPortEnd = _AlaQoSAppliedServiceSourceIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 9),
    _AlaQoSAppliedServiceSourceIpPortEnd_Type()
)
alaQoSAppliedServiceSourceIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceIpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceDestinationIpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationIpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationIpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationIpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceDestinationIpPortEnd = _AlaQoSAppliedServiceDestinationIpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 10),
    _AlaQoSAppliedServiceDestinationIpPortEnd_Type()
)
alaQoSAppliedServiceDestinationIpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationIpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceSourceTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceTcpPort_Object = MibTableColumn
alaQoSAppliedServiceSourceTcpPort = _AlaQoSAppliedServiceSourceTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 11),
    _AlaQoSAppliedServiceSourceTcpPort_Type()
)
alaQoSAppliedServiceSourceTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceTcpPort.setStatus("current")


class _AlaQoSAppliedServiceSourceTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceSourceTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceTcpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceSourceTcpPortStatus = _AlaQoSAppliedServiceSourceTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 12),
    _AlaQoSAppliedServiceSourceTcpPortStatus_Type()
)
alaQoSAppliedServiceSourceTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceTcpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceSourceTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceTcpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceSourceTcpPortEnd = _AlaQoSAppliedServiceSourceTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 13),
    _AlaQoSAppliedServiceSourceTcpPortEnd_Type()
)
alaQoSAppliedServiceSourceTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceTcpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceDestinationTcpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationTcpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationTcpPort_Object = MibTableColumn
alaQoSAppliedServiceDestinationTcpPort = _AlaQoSAppliedServiceDestinationTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 14),
    _AlaQoSAppliedServiceDestinationTcpPort_Type()
)
alaQoSAppliedServiceDestinationTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationTcpPort.setStatus("current")


class _AlaQoSAppliedServiceDestinationTcpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationTcpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceDestinationTcpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationTcpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceDestinationTcpPortStatus = _AlaQoSAppliedServiceDestinationTcpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 15),
    _AlaQoSAppliedServiceDestinationTcpPortStatus_Type()
)
alaQoSAppliedServiceDestinationTcpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationTcpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceDestinationTcpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationTcpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationTcpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceDestinationTcpPortEnd = _AlaQoSAppliedServiceDestinationTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 16),
    _AlaQoSAppliedServiceDestinationTcpPortEnd_Type()
)
alaQoSAppliedServiceDestinationTcpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationTcpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceSourceUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceUdpPort_Object = MibTableColumn
alaQoSAppliedServiceSourceUdpPort = _AlaQoSAppliedServiceSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 17),
    _AlaQoSAppliedServiceSourceUdpPort_Type()
)
alaQoSAppliedServiceSourceUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceUdpPort.setStatus("current")


class _AlaQoSAppliedServiceSourceUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceSourceUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceUdpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceSourceUdpPortStatus = _AlaQoSAppliedServiceSourceUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 18),
    _AlaQoSAppliedServiceSourceUdpPortStatus_Type()
)
alaQoSAppliedServiceSourceUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceUdpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceSourceUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceSourceUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceSourceUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceSourceUdpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceSourceUdpPortEnd = _AlaQoSAppliedServiceSourceUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 19),
    _AlaQoSAppliedServiceSourceUdpPortEnd_Type()
)
alaQoSAppliedServiceSourceUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceSourceUdpPortEnd.setStatus("current")


class _AlaQoSAppliedServiceDestinationUdpPort_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationUdpPort_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationUdpPort_Object = MibTableColumn
alaQoSAppliedServiceDestinationUdpPort = _AlaQoSAppliedServiceDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 20),
    _AlaQoSAppliedServiceDestinationUdpPort_Type()
)
alaQoSAppliedServiceDestinationUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationUdpPort.setStatus("current")


class _AlaQoSAppliedServiceDestinationUdpPortStatus_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationUdpPortStatus based on Integer32"""
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


_AlaQoSAppliedServiceDestinationUdpPortStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationUdpPortStatus_Object = MibTableColumn
alaQoSAppliedServiceDestinationUdpPortStatus = _AlaQoSAppliedServiceDestinationUdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 21),
    _AlaQoSAppliedServiceDestinationUdpPortStatus_Type()
)
alaQoSAppliedServiceDestinationUdpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationUdpPortStatus.setStatus("current")


class _AlaQoSAppliedServiceDestinationUdpPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedServiceDestinationUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedServiceDestinationUdpPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceDestinationUdpPortEnd_Object = MibTableColumn
alaQoSAppliedServiceDestinationUdpPortEnd = _AlaQoSAppliedServiceDestinationUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 6, 1, 22),
    _AlaQoSAppliedServiceDestinationUdpPortEnd_Type()
)
alaQoSAppliedServiceDestinationUdpPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceDestinationUdpPortEnd.setStatus("current")
_AlaQoSServiceGroupsTable_Object = MibTable
alaQoSServiceGroupsTable = _AlaQoSServiceGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupsTable.setStatus("current")
_AlaQoSServiceGroupsEntry_Object = MibTableRow
alaQoSServiceGroupsEntry = _AlaQoSServiceGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1)
)
alaQoSServiceGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSServiceGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupsEntry.setStatus("current")


class _AlaQoSServiceGroupsName_Type(DisplayString):
    """Custom type alaQoSServiceGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSServiceGroupsName_Type.__name__ = "DisplayString"
_AlaQoSServiceGroupsName_Object = MibTableColumn
alaQoSServiceGroupsName = _AlaQoSServiceGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1, 1),
    _AlaQoSServiceGroupsName_Type()
)
alaQoSServiceGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSServiceGroupsName.setStatus("current")


class _AlaQoSServiceGroupsSource_Type(Integer32):
    """Custom type alaQoSServiceGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSServiceGroupsSource_Type.__name__ = "Integer32"
_AlaQoSServiceGroupsSource_Object = MibTableColumn
alaQoSServiceGroupsSource = _AlaQoSServiceGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1, 2),
    _AlaQoSServiceGroupsSource_Type()
)
alaQoSServiceGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceGroupsSource.setStatus("current")
_AlaQoSServiceGroupsStatus_Type = RowStatus
_AlaQoSServiceGroupsStatus_Object = MibTableColumn
alaQoSServiceGroupsStatus = _AlaQoSServiceGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 7, 1, 3),
    _AlaQoSServiceGroupsStatus_Type()
)
alaQoSServiceGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceGroupsStatus.setStatus("current")
_AlaQoSAppliedServiceGroupsTable_Object = MibTable
alaQoSAppliedServiceGroupsTable = _AlaQoSAppliedServiceGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsTable.setStatus("current")
_AlaQoSAppliedServiceGroupsEntry_Object = MibTableRow
alaQoSAppliedServiceGroupsEntry = _AlaQoSAppliedServiceGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1)
)
alaQoSAppliedServiceGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsEntry.setStatus("current")


class _AlaQoSAppliedServiceGroupsName_Type(DisplayString):
    """Custom type alaQoSAppliedServiceGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedServiceGroupsName_Type.__name__ = "DisplayString"
_AlaQoSAppliedServiceGroupsName_Object = MibTableColumn
alaQoSAppliedServiceGroupsName = _AlaQoSAppliedServiceGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1, 1),
    _AlaQoSAppliedServiceGroupsName_Type()
)
alaQoSAppliedServiceGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsName.setStatus("current")


class _AlaQoSAppliedServiceGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedServiceGroupsSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedServiceGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedServiceGroupsSource_Object = MibTableColumn
alaQoSAppliedServiceGroupsSource = _AlaQoSAppliedServiceGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1, 2),
    _AlaQoSAppliedServiceGroupsSource_Type()
)
alaQoSAppliedServiceGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsSource.setStatus("current")
_AlaQoSAppliedServiceGroupsStatus_Type = RowStatus
_AlaQoSAppliedServiceGroupsStatus_Object = MibTableColumn
alaQoSAppliedServiceGroupsStatus = _AlaQoSAppliedServiceGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 8, 1, 3),
    _AlaQoSAppliedServiceGroupsStatus_Type()
)
alaQoSAppliedServiceGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupsStatus.setStatus("current")
_AlaQoSServiceGroupTable_Object = MibTable
alaQoSServiceGroupTable = _AlaQoSServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupTable.setStatus("current")
_AlaQoSServiceGroupEntry_Object = MibTableRow
alaQoSServiceGroupEntry = _AlaQoSServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9, 1)
)
alaQoSServiceGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSServiceGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSServiceGroupServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSServiceGroupEntry.setStatus("current")


class _AlaQoSServiceGroupServiceName_Type(DisplayString):
    """Custom type alaQoSServiceGroupServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSServiceGroupServiceName_Type.__name__ = "DisplayString"
_AlaQoSServiceGroupServiceName_Object = MibTableColumn
alaQoSServiceGroupServiceName = _AlaQoSServiceGroupServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9, 1, 1),
    _AlaQoSServiceGroupServiceName_Type()
)
alaQoSServiceGroupServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSServiceGroupServiceName.setStatus("current")
_AlaQoSServiceGroupStatus_Type = RowStatus
_AlaQoSServiceGroupStatus_Object = MibTableColumn
alaQoSServiceGroupStatus = _AlaQoSServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 9, 1, 2),
    _AlaQoSServiceGroupStatus_Type()
)
alaQoSServiceGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSServiceGroupStatus.setStatus("current")
_AlaQoSAppliedServiceGroupTable_Object = MibTable
alaQoSAppliedServiceGroupTable = _AlaQoSAppliedServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupTable.setStatus("current")
_AlaQoSAppliedServiceGroupEntry_Object = MibTableRow
alaQoSAppliedServiceGroupEntry = _AlaQoSAppliedServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10, 1)
)
alaQoSAppliedServiceGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceGroupServiceName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupEntry.setStatus("current")


class _AlaQoSAppliedServiceGroupServiceName_Type(DisplayString):
    """Custom type alaQoSAppliedServiceGroupServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedServiceGroupServiceName_Type.__name__ = "DisplayString"
_AlaQoSAppliedServiceGroupServiceName_Object = MibTableColumn
alaQoSAppliedServiceGroupServiceName = _AlaQoSAppliedServiceGroupServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10, 1, 1),
    _AlaQoSAppliedServiceGroupServiceName_Type()
)
alaQoSAppliedServiceGroupServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupServiceName.setStatus("current")
_AlaQoSAppliedServiceGroupStatus_Type = RowStatus
_AlaQoSAppliedServiceGroupStatus_Object = MibTableColumn
alaQoSAppliedServiceGroupStatus = _AlaQoSAppliedServiceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 10, 1, 2),
    _AlaQoSAppliedServiceGroupStatus_Type()
)
alaQoSAppliedServiceGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedServiceGroupStatus.setStatus("current")
_AlaQoSNetworkGroupsTable_Object = MibTable
alaQoSNetworkGroupsTable = _AlaQoSNetworkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsTable.setStatus("current")
_AlaQoSNetworkGroupsEntry_Object = MibTableRow
alaQoSNetworkGroupsEntry = _AlaQoSNetworkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1)
)
alaQoSNetworkGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSNetworkGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsEntry.setStatus("current")


class _AlaQoSNetworkGroupsName_Type(DisplayString):
    """Custom type alaQoSNetworkGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSNetworkGroupsName_Type.__name__ = "DisplayString"
_AlaQoSNetworkGroupsName_Object = MibTableColumn
alaQoSNetworkGroupsName = _AlaQoSNetworkGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1, 1),
    _AlaQoSNetworkGroupsName_Type()
)
alaQoSNetworkGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsName.setStatus("current")


class _AlaQoSNetworkGroupsSource_Type(Integer32):
    """Custom type alaQoSNetworkGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSNetworkGroupsSource_Type.__name__ = "Integer32"
_AlaQoSNetworkGroupsSource_Object = MibTableColumn
alaQoSNetworkGroupsSource = _AlaQoSNetworkGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1, 2),
    _AlaQoSNetworkGroupsSource_Type()
)
alaQoSNetworkGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsSource.setStatus("current")
_AlaQoSNetworkGroupsStatus_Type = RowStatus
_AlaQoSNetworkGroupsStatus_Object = MibTableColumn
alaQoSNetworkGroupsStatus = _AlaQoSNetworkGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 11, 1, 3),
    _AlaQoSNetworkGroupsStatus_Type()
)
alaQoSNetworkGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupsStatus.setStatus("current")
_AlaQoSAppliedNetworkGroupsTable_Object = MibTable
alaQoSAppliedNetworkGroupsTable = _AlaQoSAppliedNetworkGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsTable.setStatus("current")
_AlaQoSAppliedNetworkGroupsEntry_Object = MibTableRow
alaQoSAppliedNetworkGroupsEntry = _AlaQoSAppliedNetworkGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1)
)
alaQoSAppliedNetworkGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedNetworkGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsEntry.setStatus("current")


class _AlaQoSAppliedNetworkGroupsName_Type(DisplayString):
    """Custom type alaQoSAppliedNetworkGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedNetworkGroupsName_Type.__name__ = "DisplayString"
_AlaQoSAppliedNetworkGroupsName_Object = MibTableColumn
alaQoSAppliedNetworkGroupsName = _AlaQoSAppliedNetworkGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1, 1),
    _AlaQoSAppliedNetworkGroupsName_Type()
)
alaQoSAppliedNetworkGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsName.setStatus("current")


class _AlaQoSAppliedNetworkGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedNetworkGroupsSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedNetworkGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedNetworkGroupsSource_Object = MibTableColumn
alaQoSAppliedNetworkGroupsSource = _AlaQoSAppliedNetworkGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1, 2),
    _AlaQoSAppliedNetworkGroupsSource_Type()
)
alaQoSAppliedNetworkGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsSource.setStatus("current")
_AlaQoSAppliedNetworkGroupsStatus_Type = RowStatus
_AlaQoSAppliedNetworkGroupsStatus_Object = MibTableColumn
alaQoSAppliedNetworkGroupsStatus = _AlaQoSAppliedNetworkGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 12, 1, 3),
    _AlaQoSAppliedNetworkGroupsStatus_Type()
)
alaQoSAppliedNetworkGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupsStatus.setStatus("current")
_AlaQoSNetworkGroupTable_Object = MibTable
alaQoSNetworkGroupTable = _AlaQoSNetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupTable.setStatus("current")
_AlaQoSNetworkGroupEntry_Object = MibTableRow
alaQoSNetworkGroupEntry = _AlaQoSNetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1)
)
alaQoSNetworkGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSNetworkGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSNetworkGroupIpAddr"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSNetworkGroupIpMask"),
)
if mibBuilder.loadTexts:
    alaQoSNetworkGroupEntry.setStatus("current")
_AlaQoSNetworkGroupIpAddr_Type = IpAddress
_AlaQoSNetworkGroupIpAddr_Object = MibTableColumn
alaQoSNetworkGroupIpAddr = _AlaQoSNetworkGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1, 1),
    _AlaQoSNetworkGroupIpAddr_Type()
)
alaQoSNetworkGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupIpAddr.setStatus("current")
_AlaQoSNetworkGroupIpMask_Type = IpAddress
_AlaQoSNetworkGroupIpMask_Object = MibTableColumn
alaQoSNetworkGroupIpMask = _AlaQoSNetworkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1, 2),
    _AlaQoSNetworkGroupIpMask_Type()
)
alaQoSNetworkGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupIpMask.setStatus("current")
_AlaQoSNetworkGroupStatus_Type = RowStatus
_AlaQoSNetworkGroupStatus_Object = MibTableColumn
alaQoSNetworkGroupStatus = _AlaQoSNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 13, 1, 3),
    _AlaQoSNetworkGroupStatus_Type()
)
alaQoSNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSNetworkGroupStatus.setStatus("current")
_AlaQoSAppliedNetworkGroupTable_Object = MibTable
alaQoSAppliedNetworkGroupTable = _AlaQoSAppliedNetworkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupTable.setStatus("current")
_AlaQoSAppliedNetworkGroupEntry_Object = MibTableRow
alaQoSAppliedNetworkGroupEntry = _AlaQoSAppliedNetworkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1)
)
alaQoSAppliedNetworkGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedNetworkGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedNetworkGroupIpAddr"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedNetworkGroupIpMask"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupEntry.setStatus("current")
_AlaQoSAppliedNetworkGroupIpAddr_Type = IpAddress
_AlaQoSAppliedNetworkGroupIpAddr_Object = MibTableColumn
alaQoSAppliedNetworkGroupIpAddr = _AlaQoSAppliedNetworkGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1, 1),
    _AlaQoSAppliedNetworkGroupIpAddr_Type()
)
alaQoSAppliedNetworkGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupIpAddr.setStatus("current")
_AlaQoSAppliedNetworkGroupIpMask_Type = IpAddress
_AlaQoSAppliedNetworkGroupIpMask_Object = MibTableColumn
alaQoSAppliedNetworkGroupIpMask = _AlaQoSAppliedNetworkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1, 2),
    _AlaQoSAppliedNetworkGroupIpMask_Type()
)
alaQoSAppliedNetworkGroupIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupIpMask.setStatus("current")
_AlaQoSAppliedNetworkGroupStatus_Type = RowStatus
_AlaQoSAppliedNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedNetworkGroupStatus = _AlaQoSAppliedNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 14, 1, 3),
    _AlaQoSAppliedNetworkGroupStatus_Type()
)
alaQoSAppliedNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedNetworkGroupStatus.setStatus("current")
_AlaQoSMACGroupsTable_Object = MibTable
alaQoSMACGroupsTable = _AlaQoSMACGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaQoSMACGroupsTable.setStatus("current")
_AlaQoSMACGroupsEntry_Object = MibTableRow
alaQoSMACGroupsEntry = _AlaQoSMACGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1)
)
alaQoSMACGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMACGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSMACGroupsEntry.setStatus("current")


class _AlaQoSMACGroupsName_Type(DisplayString):
    """Custom type alaQoSMACGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSMACGroupsName_Type.__name__ = "DisplayString"
_AlaQoSMACGroupsName_Object = MibTableColumn
alaQoSMACGroupsName = _AlaQoSMACGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1, 1),
    _AlaQoSMACGroupsName_Type()
)
alaQoSMACGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMACGroupsName.setStatus("current")


class _AlaQoSMACGroupsSource_Type(Integer32):
    """Custom type alaQoSMACGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSMACGroupsSource_Type.__name__ = "Integer32"
_AlaQoSMACGroupsSource_Object = MibTableColumn
alaQoSMACGroupsSource = _AlaQoSMACGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1, 2),
    _AlaQoSMACGroupsSource_Type()
)
alaQoSMACGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMACGroupsSource.setStatus("current")
_AlaQoSMACGroupsStatus_Type = RowStatus
_AlaQoSMACGroupsStatus_Object = MibTableColumn
alaQoSMACGroupsStatus = _AlaQoSMACGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 15, 1, 3),
    _AlaQoSMACGroupsStatus_Type()
)
alaQoSMACGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMACGroupsStatus.setStatus("current")
_AlaQoSAppliedMACGroupsTable_Object = MibTable
alaQoSAppliedMACGroupsTable = _AlaQoSAppliedMACGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsTable.setStatus("current")
_AlaQoSAppliedMACGroupsEntry_Object = MibTableRow
alaQoSAppliedMACGroupsEntry = _AlaQoSAppliedMACGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1)
)
alaQoSAppliedMACGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMACGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsEntry.setStatus("current")


class _AlaQoSAppliedMACGroupsName_Type(DisplayString):
    """Custom type alaQoSAppliedMACGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedMACGroupsName_Type.__name__ = "DisplayString"
_AlaQoSAppliedMACGroupsName_Object = MibTableColumn
alaQoSAppliedMACGroupsName = _AlaQoSAppliedMACGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1, 1),
    _AlaQoSAppliedMACGroupsName_Type()
)
alaQoSAppliedMACGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsName.setStatus("current")


class _AlaQoSAppliedMACGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedMACGroupsSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedMACGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedMACGroupsSource_Object = MibTableColumn
alaQoSAppliedMACGroupsSource = _AlaQoSAppliedMACGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1, 2),
    _AlaQoSAppliedMACGroupsSource_Type()
)
alaQoSAppliedMACGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsSource.setStatus("current")
_AlaQoSAppliedMACGroupsStatus_Type = RowStatus
_AlaQoSAppliedMACGroupsStatus_Object = MibTableColumn
alaQoSAppliedMACGroupsStatus = _AlaQoSAppliedMACGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 16, 1, 3),
    _AlaQoSAppliedMACGroupsStatus_Type()
)
alaQoSAppliedMACGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupsStatus.setStatus("current")
_AlaQoSMACGroupTable_Object = MibTable
alaQoSMACGroupTable = _AlaQoSMACGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaQoSMACGroupTable.setStatus("current")
_AlaQoSMACGroupEntry_Object = MibTableRow
alaQoSMACGroupEntry = _AlaQoSMACGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1)
)
alaQoSMACGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMACGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMACGroupMacAddr"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMACGroupMacMask"),
)
if mibBuilder.loadTexts:
    alaQoSMACGroupEntry.setStatus("current")
_AlaQoSMACGroupMacAddr_Type = MacAddress
_AlaQoSMACGroupMacAddr_Object = MibTableColumn
alaQoSMACGroupMacAddr = _AlaQoSMACGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1, 1),
    _AlaQoSMACGroupMacAddr_Type()
)
alaQoSMACGroupMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMACGroupMacAddr.setStatus("current")
_AlaQoSMACGroupMacMask_Type = MacAddress
_AlaQoSMACGroupMacMask_Object = MibTableColumn
alaQoSMACGroupMacMask = _AlaQoSMACGroupMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1, 2),
    _AlaQoSMACGroupMacMask_Type()
)
alaQoSMACGroupMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMACGroupMacMask.setStatus("current")
_AlaQoSMACGroupStatus_Type = RowStatus
_AlaQoSMACGroupStatus_Object = MibTableColumn
alaQoSMACGroupStatus = _AlaQoSMACGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 17, 1, 3),
    _AlaQoSMACGroupStatus_Type()
)
alaQoSMACGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMACGroupStatus.setStatus("current")
_AlaQoSAppliedMACGroupTable_Object = MibTable
alaQoSAppliedMACGroupTable = _AlaQoSAppliedMACGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupTable.setStatus("current")
_AlaQoSAppliedMACGroupEntry_Object = MibTableRow
alaQoSAppliedMACGroupEntry = _AlaQoSAppliedMACGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1)
)
alaQoSAppliedMACGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMACGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMACGroupMacAddr"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMACGroupMacMask"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupEntry.setStatus("current")
_AlaQoSAppliedMACGroupMacAddr_Type = MacAddress
_AlaQoSAppliedMACGroupMacAddr_Object = MibTableColumn
alaQoSAppliedMACGroupMacAddr = _AlaQoSAppliedMACGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1, 1),
    _AlaQoSAppliedMACGroupMacAddr_Type()
)
alaQoSAppliedMACGroupMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupMacAddr.setStatus("current")
_AlaQoSAppliedMACGroupMacMask_Type = MacAddress
_AlaQoSAppliedMACGroupMacMask_Object = MibTableColumn
alaQoSAppliedMACGroupMacMask = _AlaQoSAppliedMACGroupMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1, 2),
    _AlaQoSAppliedMACGroupMacMask_Type()
)
alaQoSAppliedMACGroupMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupMacMask.setStatus("current")
_AlaQoSAppliedMACGroupStatus_Type = RowStatus
_AlaQoSAppliedMACGroupStatus_Object = MibTableColumn
alaQoSAppliedMACGroupStatus = _AlaQoSAppliedMACGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 18, 1, 3),
    _AlaQoSAppliedMACGroupStatus_Type()
)
alaQoSAppliedMACGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMACGroupStatus.setStatus("current")
_AlaQoSPortGroupsTable_Object = MibTable
alaQoSPortGroupsTable = _AlaQoSPortGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19)
)
if mibBuilder.loadTexts:
    alaQoSPortGroupsTable.setStatus("current")
_AlaQoSPortGroupsEntry_Object = MibTableRow
alaQoSPortGroupsEntry = _AlaQoSPortGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1)
)
alaQoSPortGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSPortGroupsEntry.setStatus("current")


class _AlaQoSPortGroupsName_Type(DisplayString):
    """Custom type alaQoSPortGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSPortGroupsName_Type.__name__ = "DisplayString"
_AlaQoSPortGroupsName_Object = MibTableColumn
alaQoSPortGroupsName = _AlaQoSPortGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1, 1),
    _AlaQoSPortGroupsName_Type()
)
alaQoSPortGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupsName.setStatus("current")


class _AlaQoSPortGroupsSource_Type(Integer32):
    """Custom type alaQoSPortGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSPortGroupsSource_Type.__name__ = "Integer32"
_AlaQoSPortGroupsSource_Object = MibTableColumn
alaQoSPortGroupsSource = _AlaQoSPortGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1, 2),
    _AlaQoSPortGroupsSource_Type()
)
alaQoSPortGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortGroupsSource.setStatus("current")
_AlaQoSPortGroupsStatus_Type = RowStatus
_AlaQoSPortGroupsStatus_Object = MibTableColumn
alaQoSPortGroupsStatus = _AlaQoSPortGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 19, 1, 3),
    _AlaQoSPortGroupsStatus_Type()
)
alaQoSPortGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortGroupsStatus.setStatus("current")
_AlaQoSAppliedPortGroupsTable_Object = MibTable
alaQoSAppliedPortGroupsTable = _AlaQoSAppliedPortGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20)
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsTable.setStatus("current")
_AlaQoSAppliedPortGroupsEntry_Object = MibTableRow
alaQoSAppliedPortGroupsEntry = _AlaQoSAppliedPortGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1)
)
alaQoSAppliedPortGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsEntry.setStatus("current")


class _AlaQoSAppliedPortGroupsName_Type(DisplayString):
    """Custom type alaQoSAppliedPortGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedPortGroupsName_Type.__name__ = "DisplayString"
_AlaQoSAppliedPortGroupsName_Object = MibTableColumn
alaQoSAppliedPortGroupsName = _AlaQoSAppliedPortGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1, 1),
    _AlaQoSAppliedPortGroupsName_Type()
)
alaQoSAppliedPortGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsName.setStatus("current")


class _AlaQoSAppliedPortGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupsSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedPortGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupsSource_Object = MibTableColumn
alaQoSAppliedPortGroupsSource = _AlaQoSAppliedPortGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1, 2),
    _AlaQoSAppliedPortGroupsSource_Type()
)
alaQoSAppliedPortGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsSource.setStatus("current")
_AlaQoSAppliedPortGroupsStatus_Type = RowStatus
_AlaQoSAppliedPortGroupsStatus_Object = MibTableColumn
alaQoSAppliedPortGroupsStatus = _AlaQoSAppliedPortGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 20, 1, 3),
    _AlaQoSAppliedPortGroupsStatus_Type()
)
alaQoSAppliedPortGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupsStatus.setStatus("current")
_AlaQoSPortGroupTable_Object = MibTable
alaQoSPortGroupTable = _AlaQoSPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21)
)
if mibBuilder.loadTexts:
    alaQoSPortGroupTable.setStatus("current")
_AlaQoSPortGroupEntry_Object = MibTableRow
alaQoSPortGroupEntry = _AlaQoSPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1)
)
alaQoSPortGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupPort"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupPortEnd"),
)
if mibBuilder.loadTexts:
    alaQoSPortGroupEntry.setStatus("current")


class _AlaQoSPortGroupSlot_Type(Integer32):
    """Custom type alaQoSPortGroupSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaQoSPortGroupSlot_Type.__name__ = "Integer32"
_AlaQoSPortGroupSlot_Object = MibTableColumn
alaQoSPortGroupSlot = _AlaQoSPortGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 1),
    _AlaQoSPortGroupSlot_Type()
)
alaQoSPortGroupSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupSlot.setStatus("current")


class _AlaQoSPortGroupPort_Type(Integer32):
    """Custom type alaQoSPortGroupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSPortGroupPort_Type.__name__ = "Integer32"
_AlaQoSPortGroupPort_Object = MibTableColumn
alaQoSPortGroupPort = _AlaQoSPortGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 2),
    _AlaQoSPortGroupPort_Type()
)
alaQoSPortGroupPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupPort.setStatus("current")
_AlaQoSPortGroupStatus_Type = RowStatus
_AlaQoSPortGroupStatus_Object = MibTableColumn
alaQoSPortGroupStatus = _AlaQoSPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 3),
    _AlaQoSPortGroupStatus_Type()
)
alaQoSPortGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortGroupStatus.setStatus("current")


class _AlaQoSPortGroupPortEnd_Type(Integer32):
    """Custom type alaQoSPortGroupPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSPortGroupPortEnd_Type.__name__ = "Integer32"
_AlaQoSPortGroupPortEnd_Object = MibTableColumn
alaQoSPortGroupPortEnd = _AlaQoSPortGroupPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 21, 1, 4),
    _AlaQoSPortGroupPortEnd_Type()
)
alaQoSPortGroupPortEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortGroupPortEnd.setStatus("current")
_AlaQoSAppliedPortGroupTable_Object = MibTable
alaQoSAppliedPortGroupTable = _AlaQoSAppliedPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22)
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupTable.setStatus("current")
_AlaQoSAppliedPortGroupEntry_Object = MibTableRow
alaQoSAppliedPortGroupEntry = _AlaQoSAppliedPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1)
)
alaQoSAppliedPortGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupPort"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupPortEnd"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupEntry.setStatus("current")


class _AlaQoSAppliedPortGroupSlot_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaQoSAppliedPortGroupSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupSlot_Object = MibTableColumn
alaQoSAppliedPortGroupSlot = _AlaQoSAppliedPortGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 1),
    _AlaQoSAppliedPortGroupSlot_Type()
)
alaQoSAppliedPortGroupSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupSlot.setStatus("current")


class _AlaQoSAppliedPortGroupPort_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedPortGroupPort_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupPort_Object = MibTableColumn
alaQoSAppliedPortGroupPort = _AlaQoSAppliedPortGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 2),
    _AlaQoSAppliedPortGroupPort_Type()
)
alaQoSAppliedPortGroupPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupPort.setStatus("current")
_AlaQoSAppliedPortGroupStatus_Type = RowStatus
_AlaQoSAppliedPortGroupStatus_Object = MibTableColumn
alaQoSAppliedPortGroupStatus = _AlaQoSAppliedPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 3),
    _AlaQoSAppliedPortGroupStatus_Type()
)
alaQoSAppliedPortGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupStatus.setStatus("current")


class _AlaQoSAppliedPortGroupPortEnd_Type(Integer32):
    """Custom type alaQoSAppliedPortGroupPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSAppliedPortGroupPortEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedPortGroupPortEnd_Object = MibTableColumn
alaQoSAppliedPortGroupPortEnd = _AlaQoSAppliedPortGroupPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 22, 1, 4),
    _AlaQoSAppliedPortGroupPortEnd_Type()
)
alaQoSAppliedPortGroupPortEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedPortGroupPortEnd.setStatus("current")
_AlaQoSMapGroupsTable_Object = MibTable
alaQoSMapGroupsTable = _AlaQoSMapGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23)
)
if mibBuilder.loadTexts:
    alaQoSMapGroupsTable.setStatus("current")
_AlaQoSMapGroupsEntry_Object = MibTableRow
alaQoSMapGroupsEntry = _AlaQoSMapGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1)
)
alaQoSMapGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSMapGroupsEntry.setStatus("current")


class _AlaQoSMapGroupsName_Type(DisplayString):
    """Custom type alaQoSMapGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSMapGroupsName_Type.__name__ = "DisplayString"
_AlaQoSMapGroupsName_Object = MibTableColumn
alaQoSMapGroupsName = _AlaQoSMapGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1, 1),
    _AlaQoSMapGroupsName_Type()
)
alaQoSMapGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupsName.setStatus("current")


class _AlaQoSMapGroupsSource_Type(Integer32):
    """Custom type alaQoSMapGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSMapGroupsSource_Type.__name__ = "Integer32"
_AlaQoSMapGroupsSource_Object = MibTableColumn
alaQoSMapGroupsSource = _AlaQoSMapGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1, 2),
    _AlaQoSMapGroupsSource_Type()
)
alaQoSMapGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMapGroupsSource.setStatus("current")
_AlaQoSMapGroupsStatus_Type = RowStatus
_AlaQoSMapGroupsStatus_Object = MibTableColumn
alaQoSMapGroupsStatus = _AlaQoSMapGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 23, 1, 3),
    _AlaQoSMapGroupsStatus_Type()
)
alaQoSMapGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMapGroupsStatus.setStatus("current")
_AlaQoSAppliedMapGroupsTable_Object = MibTable
alaQoSAppliedMapGroupsTable = _AlaQoSAppliedMapGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsTable.setStatus("current")
_AlaQoSAppliedMapGroupsEntry_Object = MibTableRow
alaQoSAppliedMapGroupsEntry = _AlaQoSAppliedMapGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1)
)
alaQoSAppliedMapGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsEntry.setStatus("current")


class _AlaQoSAppliedMapGroupsName_Type(DisplayString):
    """Custom type alaQoSAppliedMapGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedMapGroupsName_Type.__name__ = "DisplayString"
_AlaQoSAppliedMapGroupsName_Object = MibTableColumn
alaQoSAppliedMapGroupsName = _AlaQoSAppliedMapGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1, 1),
    _AlaQoSAppliedMapGroupsName_Type()
)
alaQoSAppliedMapGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsName.setStatus("current")


class _AlaQoSAppliedMapGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupsSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedMapGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupsSource_Object = MibTableColumn
alaQoSAppliedMapGroupsSource = _AlaQoSAppliedMapGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1, 2),
    _AlaQoSAppliedMapGroupsSource_Type()
)
alaQoSAppliedMapGroupsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsSource.setStatus("current")
_AlaQoSAppliedMapGroupsStatus_Type = RowStatus
_AlaQoSAppliedMapGroupsStatus_Object = MibTableColumn
alaQoSAppliedMapGroupsStatus = _AlaQoSAppliedMapGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 24, 1, 3),
    _AlaQoSAppliedMapGroupsStatus_Type()
)
alaQoSAppliedMapGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupsStatus.setStatus("current")
_AlaQoSMapGroupTable_Object = MibTable
alaQoSMapGroupTable = _AlaQoSMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25)
)
if mibBuilder.loadTexts:
    alaQoSMapGroupTable.setStatus("current")
_AlaQoSMapGroupEntry_Object = MibTableRow
alaQoSMapGroupEntry = _AlaQoSMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1)
)
alaQoSMapGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupKey"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupKeyEnd"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupValue"),
)
if mibBuilder.loadTexts:
    alaQoSMapGroupEntry.setStatus("current")


class _AlaQoSMapGroupKey_Type(Integer32):
    """Custom type alaQoSMapGroupKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSMapGroupKey_Type.__name__ = "Integer32"
_AlaQoSMapGroupKey_Object = MibTableColumn
alaQoSMapGroupKey = _AlaQoSMapGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 1),
    _AlaQoSMapGroupKey_Type()
)
alaQoSMapGroupKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupKey.setStatus("current")


class _AlaQoSMapGroupKeyEnd_Type(Integer32):
    """Custom type alaQoSMapGroupKeyEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSMapGroupKeyEnd_Type.__name__ = "Integer32"
_AlaQoSMapGroupKeyEnd_Object = MibTableColumn
alaQoSMapGroupKeyEnd = _AlaQoSMapGroupKeyEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 2),
    _AlaQoSMapGroupKeyEnd_Type()
)
alaQoSMapGroupKeyEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupKeyEnd.setStatus("current")


class _AlaQoSMapGroupValue_Type(Integer32):
    """Custom type alaQoSMapGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSMapGroupValue_Type.__name__ = "Integer32"
_AlaQoSMapGroupValue_Object = MibTableColumn
alaQoSMapGroupValue = _AlaQoSMapGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 3),
    _AlaQoSMapGroupValue_Type()
)
alaQoSMapGroupValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSMapGroupValue.setStatus("current")
_AlaQoSMapGroupStatus_Type = RowStatus
_AlaQoSMapGroupStatus_Object = MibTableColumn
alaQoSMapGroupStatus = _AlaQoSMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 25, 1, 4),
    _AlaQoSMapGroupStatus_Type()
)
alaQoSMapGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSMapGroupStatus.setStatus("current")
_AlaQoSAppliedMapGroupTable_Object = MibTable
alaQoSAppliedMapGroupTable = _AlaQoSAppliedMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26)
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupTable.setStatus("current")
_AlaQoSAppliedMapGroupEntry_Object = MibTableRow
alaQoSAppliedMapGroupEntry = _AlaQoSAppliedMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1)
)
alaQoSAppliedMapGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupKey"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupKeyEnd"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupValue"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupEntry.setStatus("current")


class _AlaQoSAppliedMapGroupKey_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedMapGroupKey_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupKey_Object = MibTableColumn
alaQoSAppliedMapGroupKey = _AlaQoSAppliedMapGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 1),
    _AlaQoSAppliedMapGroupKey_Type()
)
alaQoSAppliedMapGroupKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupKey.setStatus("current")


class _AlaQoSAppliedMapGroupKeyEnd_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupKeyEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedMapGroupKeyEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupKeyEnd_Object = MibTableColumn
alaQoSAppliedMapGroupKeyEnd = _AlaQoSAppliedMapGroupKeyEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 2),
    _AlaQoSAppliedMapGroupKeyEnd_Type()
)
alaQoSAppliedMapGroupKeyEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupKeyEnd.setStatus("current")


class _AlaQoSAppliedMapGroupValue_Type(Integer32):
    """Custom type alaQoSAppliedMapGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedMapGroupValue_Type.__name__ = "Integer32"
_AlaQoSAppliedMapGroupValue_Object = MibTableColumn
alaQoSAppliedMapGroupValue = _AlaQoSAppliedMapGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 3),
    _AlaQoSAppliedMapGroupValue_Type()
)
alaQoSAppliedMapGroupValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupValue.setStatus("current")
_AlaQoSAppliedMapGroupStatus_Type = RowStatus
_AlaQoSAppliedMapGroupStatus_Object = MibTableColumn
alaQoSAppliedMapGroupStatus = _AlaQoSAppliedMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 26, 1, 4),
    _AlaQoSAppliedMapGroupStatus_Type()
)
alaQoSAppliedMapGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedMapGroupStatus.setStatus("current")
_AlaQoSActionTable_Object = MibTable
alaQoSActionTable = _AlaQoSActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27)
)
if mibBuilder.loadTexts:
    alaQoSActionTable.setStatus("current")
_AlaQoSActionEntry_Object = MibTableRow
alaQoSActionEntry = _AlaQoSActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1)
)
alaQoSActionEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSActionName"),
)
if mibBuilder.loadTexts:
    alaQoSActionEntry.setStatus("current")


class _AlaQoSActionName_Type(DisplayString):
    """Custom type alaQoSActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSActionName_Type.__name__ = "DisplayString"
_AlaQoSActionName_Object = MibTableColumn
alaQoSActionName = _AlaQoSActionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 1),
    _AlaQoSActionName_Type()
)
alaQoSActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSActionName.setStatus("current")


class _AlaQoSActionSource_Type(Integer32):
    """Custom type alaQoSActionSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSActionSource_Type.__name__ = "Integer32"
_AlaQoSActionSource_Object = MibTableColumn
alaQoSActionSource = _AlaQoSActionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 2),
    _AlaQoSActionSource_Type()
)
alaQoSActionSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionSource.setStatus("current")


class _AlaQoSActionDisposition_Type(Integer32):
    """Custom type alaQoSActionDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSActionDisposition_Type.__name__ = "Integer32"
_AlaQoSActionDisposition_Object = MibTableColumn
alaQoSActionDisposition = _AlaQoSActionDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 3),
    _AlaQoSActionDisposition_Type()
)
alaQoSActionDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDisposition.setStatus("current")


class _AlaQoSActionDropAlgorithm_Type(Integer32):
    """Custom type alaQoSActionDropAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tail", 1),
          ("wred", 2))
    )


_AlaQoSActionDropAlgorithm_Type.__name__ = "Integer32"
_AlaQoSActionDropAlgorithm_Object = MibTableColumn
alaQoSActionDropAlgorithm = _AlaQoSActionDropAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 4),
    _AlaQoSActionDropAlgorithm_Type()
)
alaQoSActionDropAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDropAlgorithm.setStatus("current")


class _AlaQoSActionWredMaximumThreshold_Type(Integer32):
    """Custom type alaQoSActionWredMaximumThreshold based on Integer32"""
    defaultValue = 0


_AlaQoSActionWredMaximumThreshold_Object = MibTableColumn
alaQoSActionWredMaximumThreshold = _AlaQoSActionWredMaximumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 5),
    _AlaQoSActionWredMaximumThreshold_Type()
)
alaQoSActionWredMaximumThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionWredMaximumThreshold.setStatus("current")


class _AlaQoSActionWredMaximumThresholdStatus_Type(Integer32):
    """Custom type alaQoSActionWredMaximumThresholdStatus based on Integer32"""
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


_AlaQoSActionWredMaximumThresholdStatus_Type.__name__ = "Integer32"
_AlaQoSActionWredMaximumThresholdStatus_Object = MibTableColumn
alaQoSActionWredMaximumThresholdStatus = _AlaQoSActionWredMaximumThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 6),
    _AlaQoSActionWredMaximumThresholdStatus_Type()
)
alaQoSActionWredMaximumThresholdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionWredMaximumThresholdStatus.setStatus("current")


class _AlaQoSActionWredMinimumThreshold_Type(Integer32):
    """Custom type alaQoSActionWredMinimumThreshold based on Integer32"""
    defaultValue = 0


_AlaQoSActionWredMinimumThreshold_Object = MibTableColumn
alaQoSActionWredMinimumThreshold = _AlaQoSActionWredMinimumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 7),
    _AlaQoSActionWredMinimumThreshold_Type()
)
alaQoSActionWredMinimumThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionWredMinimumThreshold.setStatus("current")


class _AlaQoSActionWredMinimumThresholdStatus_Type(Integer32):
    """Custom type alaQoSActionWredMinimumThresholdStatus based on Integer32"""
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


_AlaQoSActionWredMinimumThresholdStatus_Type.__name__ = "Integer32"
_AlaQoSActionWredMinimumThresholdStatus_Object = MibTableColumn
alaQoSActionWredMinimumThresholdStatus = _AlaQoSActionWredMinimumThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 8),
    _AlaQoSActionWredMinimumThresholdStatus_Type()
)
alaQoSActionWredMinimumThresholdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionWredMinimumThresholdStatus.setStatus("current")


class _AlaQoSActionWredMaximumProbability_Type(Integer32):
    """Custom type alaQoSActionWredMaximumProbability based on Integer32"""
    defaultValue = 0


_AlaQoSActionWredMaximumProbability_Object = MibTableColumn
alaQoSActionWredMaximumProbability = _AlaQoSActionWredMaximumProbability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 9),
    _AlaQoSActionWredMaximumProbability_Type()
)
alaQoSActionWredMaximumProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionWredMaximumProbability.setStatus("current")


class _AlaQoSActionWredMaximumProbabilityStatus_Type(Integer32):
    """Custom type alaQoSActionWredMaximumProbabilityStatus based on Integer32"""
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


_AlaQoSActionWredMaximumProbabilityStatus_Type.__name__ = "Integer32"
_AlaQoSActionWredMaximumProbabilityStatus_Object = MibTableColumn
alaQoSActionWredMaximumProbabilityStatus = _AlaQoSActionWredMaximumProbabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 10),
    _AlaQoSActionWredMaximumProbabilityStatus_Type()
)
alaQoSActionWredMaximumProbabilityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionWredMaximumProbabilityStatus.setStatus("current")


class _AlaQoSActionMinimumBandwidth_Type(Integer32):
    """Custom type alaQoSActionMinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSActionMinimumBandwidth_Object = MibTableColumn
alaQoSActionMinimumBandwidth = _AlaQoSActionMinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 11),
    _AlaQoSActionMinimumBandwidth_Type()
)
alaQoSActionMinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMinimumBandwidth.setStatus("current")


class _AlaQoSActionMinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSActionMinimumBandwidthStatus based on Integer32"""
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


_AlaQoSActionMinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSActionMinimumBandwidthStatus_Object = MibTableColumn
alaQoSActionMinimumBandwidthStatus = _AlaQoSActionMinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 12),
    _AlaQoSActionMinimumBandwidthStatus_Type()
)
alaQoSActionMinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMinimumBandwidthStatus.setStatus("current")


class _AlaQoSActionMaximumBandwidth_Type(Integer32):
    """Custom type alaQoSActionMaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSActionMaximumBandwidth_Object = MibTableColumn
alaQoSActionMaximumBandwidth = _AlaQoSActionMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 13),
    _AlaQoSActionMaximumBandwidth_Type()
)
alaQoSActionMaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumBandwidth.setStatus("current")


class _AlaQoSActionMaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSActionMaximumBandwidthStatus based on Integer32"""
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


_AlaQoSActionMaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSActionMaximumBandwidthStatus_Object = MibTableColumn
alaQoSActionMaximumBandwidthStatus = _AlaQoSActionMaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 14),
    _AlaQoSActionMaximumBandwidthStatus_Type()
)
alaQoSActionMaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumBandwidthStatus.setStatus("current")


class _AlaQoSActionPeakBandwidth_Type(Integer32):
    """Custom type alaQoSActionPeakBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSActionPeakBandwidth_Object = MibTableColumn
alaQoSActionPeakBandwidth = _AlaQoSActionPeakBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 15),
    _AlaQoSActionPeakBandwidth_Type()
)
alaQoSActionPeakBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPeakBandwidth.setStatus("current")


class _AlaQoSActionPeakBandwidthStatus_Type(Integer32):
    """Custom type alaQoSActionPeakBandwidthStatus based on Integer32"""
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


_AlaQoSActionPeakBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSActionPeakBandwidthStatus_Object = MibTableColumn
alaQoSActionPeakBandwidthStatus = _AlaQoSActionPeakBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 16),
    _AlaQoSActionPeakBandwidthStatus_Type()
)
alaQoSActionPeakBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPeakBandwidthStatus.setStatus("current")


class _AlaQoSActionPriority_Type(Integer32):
    """Custom type alaQoSActionPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSActionPriority_Type.__name__ = "Integer32"
_AlaQoSActionPriority_Object = MibTableColumn
alaQoSActionPriority = _AlaQoSActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 17),
    _AlaQoSActionPriority_Type()
)
alaQoSActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPriority.setStatus("current")


class _AlaQoSActionPriorityStatus_Type(Integer32):
    """Custom type alaQoSActionPriorityStatus based on Integer32"""
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


_AlaQoSActionPriorityStatus_Type.__name__ = "Integer32"
_AlaQoSActionPriorityStatus_Object = MibTableColumn
alaQoSActionPriorityStatus = _AlaQoSActionPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 18),
    _AlaQoSActionPriorityStatus_Type()
)
alaQoSActionPriorityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPriorityStatus.setStatus("current")


class _AlaQoSActionShared_Type(Integer32):
    """Custom type alaQoSActionShared based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSActionShared_Type.__name__ = "Integer32"
_AlaQoSActionShared_Object = MibTableColumn
alaQoSActionShared = _AlaQoSActionShared_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 19),
    _AlaQoSActionShared_Type()
)
alaQoSActionShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionShared.setStatus("current")


class _AlaQoSActionJitter_Type(Integer32):
    """Custom type alaQoSActionJitter based on Integer32"""
    defaultValue = 0


_AlaQoSActionJitter_Object = MibTableColumn
alaQoSActionJitter = _AlaQoSActionJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 20),
    _AlaQoSActionJitter_Type()
)
alaQoSActionJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionJitter.setStatus("current")


class _AlaQoSActionJitterStatus_Type(Integer32):
    """Custom type alaQoSActionJitterStatus based on Integer32"""
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


_AlaQoSActionJitterStatus_Type.__name__ = "Integer32"
_AlaQoSActionJitterStatus_Object = MibTableColumn
alaQoSActionJitterStatus = _AlaQoSActionJitterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 21),
    _AlaQoSActionJitterStatus_Type()
)
alaQoSActionJitterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionJitterStatus.setStatus("current")


class _AlaQoSActionLatency_Type(Integer32):
    """Custom type alaQoSActionLatency based on Integer32"""
    defaultValue = 0


_AlaQoSActionLatency_Object = MibTableColumn
alaQoSActionLatency = _AlaQoSActionLatency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 22),
    _AlaQoSActionLatency_Type()
)
alaQoSActionLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionLatency.setStatus("current")


class _AlaQoSActionLatencyStatus_Type(Integer32):
    """Custom type alaQoSActionLatencyStatus based on Integer32"""
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


_AlaQoSActionLatencyStatus_Type.__name__ = "Integer32"
_AlaQoSActionLatencyStatus_Object = MibTableColumn
alaQoSActionLatencyStatus = _AlaQoSActionLatencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 23),
    _AlaQoSActionLatencyStatus_Type()
)
alaQoSActionLatencyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionLatencyStatus.setStatus("current")


class _AlaQoSActionMaximumDepth_Type(Integer32):
    """Custom type alaQoSActionMaximumDepth based on Integer32"""
    defaultValue = 0


_AlaQoSActionMaximumDepth_Object = MibTableColumn
alaQoSActionMaximumDepth = _AlaQoSActionMaximumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 24),
    _AlaQoSActionMaximumDepth_Type()
)
alaQoSActionMaximumDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumDepth.setStatus("current")


class _AlaQoSActionMaximumDepthStatus_Type(Integer32):
    """Custom type alaQoSActionMaximumDepthStatus based on Integer32"""
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


_AlaQoSActionMaximumDepthStatus_Type.__name__ = "Integer32"
_AlaQoSActionMaximumDepthStatus_Object = MibTableColumn
alaQoSActionMaximumDepthStatus = _AlaQoSActionMaximumDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 25),
    _AlaQoSActionMaximumDepthStatus_Type()
)
alaQoSActionMaximumDepthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumDepthStatus.setStatus("current")


class _AlaQoSActionMaximumBuffers_Type(Integer32):
    """Custom type alaQoSActionMaximumBuffers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_AlaQoSActionMaximumBuffers_Type.__name__ = "Integer32"
_AlaQoSActionMaximumBuffers_Object = MibTableColumn
alaQoSActionMaximumBuffers = _AlaQoSActionMaximumBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 26),
    _AlaQoSActionMaximumBuffers_Type()
)
alaQoSActionMaximumBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumBuffers.setStatus("current")


class _AlaQoSActionMaximumBuffersStatus_Type(Integer32):
    """Custom type alaQoSActionMaximumBuffersStatus based on Integer32"""
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


_AlaQoSActionMaximumBuffersStatus_Type.__name__ = "Integer32"
_AlaQoSActionMaximumBuffersStatus_Object = MibTableColumn
alaQoSActionMaximumBuffersStatus = _AlaQoSActionMaximumBuffersStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 27),
    _AlaQoSActionMaximumBuffersStatus_Type()
)
alaQoSActionMaximumBuffersStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMaximumBuffersStatus.setStatus("current")


class _AlaQoSAction8021p_Type(Integer32):
    """Custom type alaQoSAction8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAction8021p_Type.__name__ = "Integer32"
_AlaQoSAction8021p_Object = MibTableColumn
alaQoSAction8021p = _AlaQoSAction8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 28),
    _AlaQoSAction8021p_Type()
)
alaQoSAction8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAction8021p.setStatus("current")


class _AlaQoSAction8021pStatus_Type(Integer32):
    """Custom type alaQoSAction8021pStatus based on Integer32"""
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


_AlaQoSAction8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAction8021pStatus_Object = MibTableColumn
alaQoSAction8021pStatus = _AlaQoSAction8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 29),
    _AlaQoSAction8021pStatus_Type()
)
alaQoSAction8021pStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAction8021pStatus.setStatus("current")


class _AlaQoSActionTos_Type(Integer32):
    """Custom type alaQoSActionTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSActionTos_Type.__name__ = "Integer32"
_AlaQoSActionTos_Object = MibTableColumn
alaQoSActionTos = _AlaQoSActionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 30),
    _AlaQoSActionTos_Type()
)
alaQoSActionTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionTos.setStatus("current")


class _AlaQoSActionTosStatus_Type(Integer32):
    """Custom type alaQoSActionTosStatus based on Integer32"""
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


_AlaQoSActionTosStatus_Type.__name__ = "Integer32"
_AlaQoSActionTosStatus_Object = MibTableColumn
alaQoSActionTosStatus = _AlaQoSActionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 31),
    _AlaQoSActionTosStatus_Type()
)
alaQoSActionTosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionTosStatus.setStatus("current")


class _AlaQoSActionDscp_Type(Integer32):
    """Custom type alaQoSActionDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSActionDscp_Type.__name__ = "Integer32"
_AlaQoSActionDscp_Object = MibTableColumn
alaQoSActionDscp = _AlaQoSActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 32),
    _AlaQoSActionDscp_Type()
)
alaQoSActionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDscp.setStatus("current")


class _AlaQoSActionDscpStatus_Type(Integer32):
    """Custom type alaQoSActionDscpStatus based on Integer32"""
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


_AlaQoSActionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSActionDscpStatus_Object = MibTableColumn
alaQoSActionDscpStatus = _AlaQoSActionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 33),
    _AlaQoSActionDscpStatus_Type()
)
alaQoSActionDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDscpStatus.setStatus("current")


class _AlaQoSActionMapFrom_Type(Integer32):
    """Custom type alaQoSActionMapFrom based on Integer32"""
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
        *(("b8021p", 1),
          ("dscp", 3),
          ("tos", 2))
    )


_AlaQoSActionMapFrom_Type.__name__ = "Integer32"
_AlaQoSActionMapFrom_Object = MibTableColumn
alaQoSActionMapFrom = _AlaQoSActionMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 34),
    _AlaQoSActionMapFrom_Type()
)
alaQoSActionMapFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapFrom.setStatus("current")


class _AlaQoSActionMapTo_Type(Integer32):
    """Custom type alaQoSActionMapTo based on Integer32"""
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
        *(("b8021p", 1),
          ("dscp", 3),
          ("tos", 2))
    )


_AlaQoSActionMapTo_Type.__name__ = "Integer32"
_AlaQoSActionMapTo_Object = MibTableColumn
alaQoSActionMapTo = _AlaQoSActionMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 35),
    _AlaQoSActionMapTo_Type()
)
alaQoSActionMapTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapTo.setStatus("current")


class _AlaQoSActionMapGroup_Type(DisplayString):
    """Custom type alaQoSActionMapGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSActionMapGroup_Type.__name__ = "DisplayString"
_AlaQoSActionMapGroup_Object = MibTableColumn
alaQoSActionMapGroup = _AlaQoSActionMapGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 36),
    _AlaQoSActionMapGroup_Type()
)
alaQoSActionMapGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapGroup.setStatus("current")


class _AlaQoSActionMapGroupStatus_Type(Integer32):
    """Custom type alaQoSActionMapGroupStatus based on Integer32"""
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


_AlaQoSActionMapGroupStatus_Type.__name__ = "Integer32"
_AlaQoSActionMapGroupStatus_Object = MibTableColumn
alaQoSActionMapGroupStatus = _AlaQoSActionMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 37),
    _AlaQoSActionMapGroupStatus_Type()
)
alaQoSActionMapGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMapGroupStatus.setStatus("current")


class _AlaQoSActionSourceRewriteIpAddr_Type(IpAddress):
    """Custom type alaQoSActionSourceRewriteIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSActionSourceRewriteIpAddr_Object = MibTableColumn
alaQoSActionSourceRewriteIpAddr = _AlaQoSActionSourceRewriteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 38),
    _AlaQoSActionSourceRewriteIpAddr_Type()
)
alaQoSActionSourceRewriteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionSourceRewriteIpAddr.setStatus("current")


class _AlaQoSActionSourceRewriteIpAddrStatus_Type(Integer32):
    """Custom type alaQoSActionSourceRewriteIpAddrStatus based on Integer32"""
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


_AlaQoSActionSourceRewriteIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSActionSourceRewriteIpAddrStatus_Object = MibTableColumn
alaQoSActionSourceRewriteIpAddrStatus = _AlaQoSActionSourceRewriteIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 39),
    _AlaQoSActionSourceRewriteIpAddrStatus_Type()
)
alaQoSActionSourceRewriteIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionSourceRewriteIpAddrStatus.setStatus("current")


class _AlaQoSActionSourceRewriteIpMask_Type(IpAddress):
    """Custom type alaQoSActionSourceRewriteIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSActionSourceRewriteIpMask_Object = MibTableColumn
alaQoSActionSourceRewriteIpMask = _AlaQoSActionSourceRewriteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 40),
    _AlaQoSActionSourceRewriteIpMask_Type()
)
alaQoSActionSourceRewriteIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionSourceRewriteIpMask.setStatus("current")


class _AlaQoSActionSourceRewriteNetworkGroup_Type(DisplayString):
    """Custom type alaQoSActionSourceRewriteNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSActionSourceRewriteNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSActionSourceRewriteNetworkGroup_Object = MibTableColumn
alaQoSActionSourceRewriteNetworkGroup = _AlaQoSActionSourceRewriteNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 41),
    _AlaQoSActionSourceRewriteNetworkGroup_Type()
)
alaQoSActionSourceRewriteNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionSourceRewriteNetworkGroup.setStatus("current")


class _AlaQoSActionSourceRewriteNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSActionSourceRewriteNetworkGroupStatus based on Integer32"""
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


_AlaQoSActionSourceRewriteNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSActionSourceRewriteNetworkGroupStatus_Object = MibTableColumn
alaQoSActionSourceRewriteNetworkGroupStatus = _AlaQoSActionSourceRewriteNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 42),
    _AlaQoSActionSourceRewriteNetworkGroupStatus_Type()
)
alaQoSActionSourceRewriteNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionSourceRewriteNetworkGroupStatus.setStatus("current")


class _AlaQoSActionDestinationRewriteIpAddr_Type(IpAddress):
    """Custom type alaQoSActionDestinationRewriteIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSActionDestinationRewriteIpAddr_Object = MibTableColumn
alaQoSActionDestinationRewriteIpAddr = _AlaQoSActionDestinationRewriteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 43),
    _AlaQoSActionDestinationRewriteIpAddr_Type()
)
alaQoSActionDestinationRewriteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDestinationRewriteIpAddr.setStatus("current")


class _AlaQoSActionDestinationRewriteIpAddrStatus_Type(Integer32):
    """Custom type alaQoSActionDestinationRewriteIpAddrStatus based on Integer32"""
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


_AlaQoSActionDestinationRewriteIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSActionDestinationRewriteIpAddrStatus_Object = MibTableColumn
alaQoSActionDestinationRewriteIpAddrStatus = _AlaQoSActionDestinationRewriteIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 44),
    _AlaQoSActionDestinationRewriteIpAddrStatus_Type()
)
alaQoSActionDestinationRewriteIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDestinationRewriteIpAddrStatus.setStatus("current")


class _AlaQoSActionDestinationRewriteIpMask_Type(IpAddress):
    """Custom type alaQoSActionDestinationRewriteIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AlaQoSActionDestinationRewriteIpMask_Object = MibTableColumn
alaQoSActionDestinationRewriteIpMask = _AlaQoSActionDestinationRewriteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 45),
    _AlaQoSActionDestinationRewriteIpMask_Type()
)
alaQoSActionDestinationRewriteIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDestinationRewriteIpMask.setStatus("current")


class _AlaQoSActionDestinationRewriteNetworkGroup_Type(DisplayString):
    """Custom type alaQoSActionDestinationRewriteNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSActionDestinationRewriteNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSActionDestinationRewriteNetworkGroup_Object = MibTableColumn
alaQoSActionDestinationRewriteNetworkGroup = _AlaQoSActionDestinationRewriteNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 46),
    _AlaQoSActionDestinationRewriteNetworkGroup_Type()
)
alaQoSActionDestinationRewriteNetworkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDestinationRewriteNetworkGroup.setStatus("current")


class _AlaQoSActionDestinationRewriteNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSActionDestinationRewriteNetworkGroupStatus based on Integer32"""
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


_AlaQoSActionDestinationRewriteNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSActionDestinationRewriteNetworkGroupStatus_Object = MibTableColumn
alaQoSActionDestinationRewriteNetworkGroupStatus = _AlaQoSActionDestinationRewriteNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 47),
    _AlaQoSActionDestinationRewriteNetworkGroupStatus_Type()
)
alaQoSActionDestinationRewriteNetworkGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionDestinationRewriteNetworkGroupStatus.setStatus("current")


class _AlaQoSActionLoadBalanceGroup_Type(DisplayString):
    """Custom type alaQoSActionLoadBalanceGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_AlaQoSActionLoadBalanceGroup_Type.__name__ = "DisplayString"
_AlaQoSActionLoadBalanceGroup_Object = MibTableColumn
alaQoSActionLoadBalanceGroup = _AlaQoSActionLoadBalanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 48),
    _AlaQoSActionLoadBalanceGroup_Type()
)
alaQoSActionLoadBalanceGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionLoadBalanceGroup.setStatus("current")


class _AlaQoSActionLoadBalanceGroupStatus_Type(Integer32):
    """Custom type alaQoSActionLoadBalanceGroupStatus based on Integer32"""
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


_AlaQoSActionLoadBalanceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSActionLoadBalanceGroupStatus_Object = MibTableColumn
alaQoSActionLoadBalanceGroupStatus = _AlaQoSActionLoadBalanceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 49),
    _AlaQoSActionLoadBalanceGroupStatus_Type()
)
alaQoSActionLoadBalanceGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionLoadBalanceGroupStatus.setStatus("current")


class _AlaQoSActionPermanentGatewayIpAddr_Type(IpAddress):
    """Custom type alaQoSActionPermanentGatewayIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSActionPermanentGatewayIpAddr_Object = MibTableColumn
alaQoSActionPermanentGatewayIpAddr = _AlaQoSActionPermanentGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 50),
    _AlaQoSActionPermanentGatewayIpAddr_Type()
)
alaQoSActionPermanentGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPermanentGatewayIpAddr.setStatus("current")


class _AlaQoSActionPermanentGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSActionPermanentGatewayIpAddrStatus based on Integer32"""
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


_AlaQoSActionPermanentGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSActionPermanentGatewayIpAddrStatus_Object = MibTableColumn
alaQoSActionPermanentGatewayIpAddrStatus = _AlaQoSActionPermanentGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 51),
    _AlaQoSActionPermanentGatewayIpAddrStatus_Type()
)
alaQoSActionPermanentGatewayIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPermanentGatewayIpAddrStatus.setStatus("current")


class _AlaQoSActionAlternateGatewayIpAddr_Type(IpAddress):
    """Custom type alaQoSActionAlternateGatewayIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaQoSActionAlternateGatewayIpAddr_Object = MibTableColumn
alaQoSActionAlternateGatewayIpAddr = _AlaQoSActionAlternateGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 52),
    _AlaQoSActionAlternateGatewayIpAddr_Type()
)
alaQoSActionAlternateGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionAlternateGatewayIpAddr.setStatus("current")


class _AlaQoSActionAlternateGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSActionAlternateGatewayIpAddrStatus based on Integer32"""
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


_AlaQoSActionAlternateGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSActionAlternateGatewayIpAddrStatus_Object = MibTableColumn
alaQoSActionAlternateGatewayIpAddrStatus = _AlaQoSActionAlternateGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 53),
    _AlaQoSActionAlternateGatewayIpAddrStatus_Type()
)
alaQoSActionAlternateGatewayIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionAlternateGatewayIpAddrStatus.setStatus("current")
_AlaQoSActionRowStatus_Type = RowStatus
_AlaQoSActionRowStatus_Object = MibTableColumn
alaQoSActionRowStatus = _AlaQoSActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 54),
    _AlaQoSActionRowStatus_Type()
)
alaQoSActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRowStatus.setStatus("current")


class _AlaQoSActionMinimumDepth_Type(Integer32):
    """Custom type alaQoSActionMinimumDepth based on Integer32"""
    defaultValue = 0


_AlaQoSActionMinimumDepth_Object = MibTableColumn
alaQoSActionMinimumDepth = _AlaQoSActionMinimumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 55),
    _AlaQoSActionMinimumDepth_Type()
)
alaQoSActionMinimumDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMinimumDepth.setStatus("current")


class _AlaQoSActionMinimumDepthStatus_Type(Integer32):
    """Custom type alaQoSActionMinimumDepthStatus based on Integer32"""
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


_AlaQoSActionMinimumDepthStatus_Type.__name__ = "Integer32"
_AlaQoSActionMinimumDepthStatus_Object = MibTableColumn
alaQoSActionMinimumDepthStatus = _AlaQoSActionMinimumDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 56),
    _AlaQoSActionMinimumDepthStatus_Type()
)
alaQoSActionMinimumDepthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMinimumDepthStatus.setStatus("current")


class _AlaQoSActionVPNAccess_Type(Integer32):
    """Custom type alaQoSActionVPNAccess based on Integer32"""
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
        *(("bypass", 2),
          ("drop", 3),
          ("protect", 1))
    )


_AlaQoSActionVPNAccess_Type.__name__ = "Integer32"
_AlaQoSActionVPNAccess_Object = MibTableColumn
alaQoSActionVPNAccess = _AlaQoSActionVPNAccess_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 57),
    _AlaQoSActionVPNAccess_Type()
)
alaQoSActionVPNAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionVPNAccess.setStatus("current")


class _AlaQoSActionNocache_Type(Integer32):
    """Custom type alaQoSActionNocache based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSActionNocache_Type.__name__ = "Integer32"
_AlaQoSActionNocache_Object = MibTableColumn
alaQoSActionNocache = _AlaQoSActionNocache_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 58),
    _AlaQoSActionNocache_Type()
)
alaQoSActionNocache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionNocache.setStatus("current")


class _AlaQoSActionPortdisable_Type(Integer32):
    """Custom type alaQoSActionPortdisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSActionPortdisable_Type.__name__ = "Integer32"
_AlaQoSActionPortdisable_Object = MibTableColumn
alaQoSActionPortdisable = _AlaQoSActionPortdisable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 59),
    _AlaQoSActionPortdisable_Type()
)
alaQoSActionPortdisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPortdisable.setStatus("current")


class _AlaQoSActionRedirectSlot_Type(Integer32):
    """Custom type alaQoSActionRedirectSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSActionRedirectSlot_Type.__name__ = "Integer32"
_AlaQoSActionRedirectSlot_Object = MibTableColumn
alaQoSActionRedirectSlot = _AlaQoSActionRedirectSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 60),
    _AlaQoSActionRedirectSlot_Type()
)
alaQoSActionRedirectSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectSlot.setStatus("current")


class _AlaQoSActionRedirectSlotStatus_Type(Integer32):
    """Custom type alaQoSActionRedirectSlotStatus based on Integer32"""
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


_AlaQoSActionRedirectSlotStatus_Type.__name__ = "Integer32"
_AlaQoSActionRedirectSlotStatus_Object = MibTableColumn
alaQoSActionRedirectSlotStatus = _AlaQoSActionRedirectSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 61),
    _AlaQoSActionRedirectSlotStatus_Type()
)
alaQoSActionRedirectSlotStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectSlotStatus.setStatus("current")


class _AlaQoSActionRedirectPort_Type(Integer32):
    """Custom type alaQoSActionRedirectPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSActionRedirectPort_Type.__name__ = "Integer32"
_AlaQoSActionRedirectPort_Object = MibTableColumn
alaQoSActionRedirectPort = _AlaQoSActionRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 62),
    _AlaQoSActionRedirectPort_Type()
)
alaQoSActionRedirectPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectPort.setStatus("current")


class _AlaQoSActionRedirectAgg_Type(Integer32):
    """Custom type alaQoSActionRedirectAgg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AlaQoSActionRedirectAgg_Type.__name__ = "Integer32"
_AlaQoSActionRedirectAgg_Object = MibTableColumn
alaQoSActionRedirectAgg = _AlaQoSActionRedirectAgg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 63),
    _AlaQoSActionRedirectAgg_Type()
)
alaQoSActionRedirectAgg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectAgg.setStatus("current")


class _AlaQoSActionRedirectAggStatus_Type(Integer32):
    """Custom type alaQoSActionRedirectAggStatus based on Integer32"""
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


_AlaQoSActionRedirectAggStatus_Type.__name__ = "Integer32"
_AlaQoSActionRedirectAggStatus_Object = MibTableColumn
alaQoSActionRedirectAggStatus = _AlaQoSActionRedirectAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 64),
    _AlaQoSActionRedirectAggStatus_Type()
)
alaQoSActionRedirectAggStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionRedirectAggStatus.setStatus("current")


class _AlaQoSActionMirrorSlot_Type(Integer32):
    """Custom type alaQoSActionMirrorSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSActionMirrorSlot_Type.__name__ = "Integer32"
_AlaQoSActionMirrorSlot_Object = MibTableColumn
alaQoSActionMirrorSlot = _AlaQoSActionMirrorSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 65),
    _AlaQoSActionMirrorSlot_Type()
)
alaQoSActionMirrorSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorSlot.setStatus("current")


class _AlaQoSActionMirrorPort_Type(Integer32):
    """Custom type alaQoSActionMirrorPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSActionMirrorPort_Type.__name__ = "Integer32"
_AlaQoSActionMirrorPort_Object = MibTableColumn
alaQoSActionMirrorPort = _AlaQoSActionMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 66),
    _AlaQoSActionMirrorPort_Type()
)
alaQoSActionMirrorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorPort.setStatus("current")


class _AlaQoSActionMirrorMode_Type(Integer32):
    """Custom type alaQoSActionMirrorMode based on Integer32"""
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
        *(("both", 3),
          ("egress", 2),
          ("ingress", 1))
    )


_AlaQoSActionMirrorMode_Type.__name__ = "Integer32"
_AlaQoSActionMirrorMode_Object = MibTableColumn
alaQoSActionMirrorMode = _AlaQoSActionMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 67),
    _AlaQoSActionMirrorMode_Type()
)
alaQoSActionMirrorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorMode.setStatus("current")


class _AlaQoSActionMirrorModeStatus_Type(Integer32):
    """Custom type alaQoSActionMirrorModeStatus based on Integer32"""
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


_AlaQoSActionMirrorModeStatus_Type.__name__ = "Integer32"
_AlaQoSActionMirrorModeStatus_Object = MibTableColumn
alaQoSActionMirrorModeStatus = _AlaQoSActionMirrorModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 68),
    _AlaQoSActionMirrorModeStatus_Type()
)
alaQoSActionMirrorModeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionMirrorModeStatus.setStatus("current")


class _AlaQoSActionCIR_Type(Integer32):
    """Custom type alaQoSActionCIR based on Integer32"""
    defaultValue = 0


_AlaQoSActionCIR_Object = MibTableColumn
alaQoSActionCIR = _AlaQoSActionCIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 69),
    _AlaQoSActionCIR_Type()
)
alaQoSActionCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSActionCIR.setUnits("kilobits per second")


class _AlaQoSActionCIRStatus_Type(Integer32):
    """Custom type alaQoSActionCIRStatus based on Integer32"""
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


_AlaQoSActionCIRStatus_Type.__name__ = "Integer32"
_AlaQoSActionCIRStatus_Object = MibTableColumn
alaQoSActionCIRStatus = _AlaQoSActionCIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 70),
    _AlaQoSActionCIRStatus_Type()
)
alaQoSActionCIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCIRStatus.setStatus("current")


class _AlaQoSActionCBS_Type(Integer32):
    """Custom type alaQoSActionCBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSActionCBS_Type.__name__ = "Integer32"
_AlaQoSActionCBS_Object = MibTableColumn
alaQoSActionCBS = _AlaQoSActionCBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 71),
    _AlaQoSActionCBS_Type()
)
alaQoSActionCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCBS.setStatus("current")


class _AlaQoSActionCBSStatus_Type(Integer32):
    """Custom type alaQoSActionCBSStatus based on Integer32"""
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


_AlaQoSActionCBSStatus_Type.__name__ = "Integer32"
_AlaQoSActionCBSStatus_Object = MibTableColumn
alaQoSActionCBSStatus = _AlaQoSActionCBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 72),
    _AlaQoSActionCBSStatus_Type()
)
alaQoSActionCBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCBSStatus.setStatus("current")


class _AlaQoSActionPIR_Type(Integer32):
    """Custom type alaQoSActionPIR based on Integer32"""
    defaultValue = 0


_AlaQoSActionPIR_Object = MibTableColumn
alaQoSActionPIR = _AlaQoSActionPIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 73),
    _AlaQoSActionPIR_Type()
)
alaQoSActionPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSActionPIR.setUnits("kilobits per second")


class _AlaQoSActionPIRStatus_Type(Integer32):
    """Custom type alaQoSActionPIRStatus based on Integer32"""
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


_AlaQoSActionPIRStatus_Type.__name__ = "Integer32"
_AlaQoSActionPIRStatus_Object = MibTableColumn
alaQoSActionPIRStatus = _AlaQoSActionPIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 74),
    _AlaQoSActionPIRStatus_Type()
)
alaQoSActionPIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPIRStatus.setStatus("current")


class _AlaQoSActionPBS_Type(Integer32):
    """Custom type alaQoSActionPBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSActionPBS_Type.__name__ = "Integer32"
_AlaQoSActionPBS_Object = MibTableColumn
alaQoSActionPBS = _AlaQoSActionPBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 75),
    _AlaQoSActionPBS_Type()
)
alaQoSActionPBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPBS.setStatus("current")


class _AlaQoSActionPBSStatus_Type(Integer32):
    """Custom type alaQoSActionPBSStatus based on Integer32"""
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


_AlaQoSActionPBSStatus_Type.__name__ = "Integer32"
_AlaQoSActionPBSStatus_Object = MibTableColumn
alaQoSActionPBSStatus = _AlaQoSActionPBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 76),
    _AlaQoSActionPBSStatus_Type()
)
alaQoSActionPBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionPBSStatus.setStatus("current")


class _AlaQoSActionCounterColor_Type(Integer32):
    """Custom type alaQoSActionCounterColor based on Integer32"""
    defaultValue = 5

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
        *(("greennongreen", 2),
          ("greenred", 3),
          ("greenyellow", 4),
          ("rednonred", 1),
          ("redyellow", 5))
    )


_AlaQoSActionCounterColor_Type.__name__ = "Integer32"
_AlaQoSActionCounterColor_Object = MibTableColumn
alaQoSActionCounterColor = _AlaQoSActionCounterColor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 27, 1, 77),
    _AlaQoSActionCounterColor_Type()
)
alaQoSActionCounterColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSActionCounterColor.setStatus("current")
_AlaQoSAppliedActionTable_Object = MibTable
alaQoSAppliedActionTable = _AlaQoSAppliedActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28)
)
if mibBuilder.loadTexts:
    alaQoSAppliedActionTable.setStatus("current")
_AlaQoSAppliedActionEntry_Object = MibTableRow
alaQoSAppliedActionEntry = _AlaQoSAppliedActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1)
)
alaQoSAppliedActionEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedActionEntry.setStatus("current")


class _AlaQoSAppliedActionName_Type(DisplayString):
    """Custom type alaQoSAppliedActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedActionName_Type.__name__ = "DisplayString"
_AlaQoSAppliedActionName_Object = MibTableColumn
alaQoSAppliedActionName = _AlaQoSAppliedActionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 1),
    _AlaQoSAppliedActionName_Type()
)
alaQoSAppliedActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedActionName.setStatus("current")


class _AlaQoSAppliedActionSource_Type(Integer32):
    """Custom type alaQoSAppliedActionSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedActionSource_Type.__name__ = "Integer32"
_AlaQoSAppliedActionSource_Object = MibTableColumn
alaQoSAppliedActionSource = _AlaQoSAppliedActionSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 2),
    _AlaQoSAppliedActionSource_Type()
)
alaQoSAppliedActionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionSource.setStatus("current")


class _AlaQoSAppliedActionDisposition_Type(Integer32):
    """Custom type alaQoSAppliedActionDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSAppliedActionDisposition_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDisposition_Object = MibTableColumn
alaQoSAppliedActionDisposition = _AlaQoSAppliedActionDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 3),
    _AlaQoSAppliedActionDisposition_Type()
)
alaQoSAppliedActionDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDisposition.setStatus("current")


class _AlaQoSAppliedActionDropAlgorithm_Type(Integer32):
    """Custom type alaQoSAppliedActionDropAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tail", 1),
          ("wred", 2))
    )


_AlaQoSAppliedActionDropAlgorithm_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDropAlgorithm_Object = MibTableColumn
alaQoSAppliedActionDropAlgorithm = _AlaQoSAppliedActionDropAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 4),
    _AlaQoSAppliedActionDropAlgorithm_Type()
)
alaQoSAppliedActionDropAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDropAlgorithm.setStatus("current")
_AlaQoSAppliedActionWredMaximumThreshold_Type = Integer32
_AlaQoSAppliedActionWredMaximumThreshold_Object = MibTableColumn
alaQoSAppliedActionWredMaximumThreshold = _AlaQoSAppliedActionWredMaximumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 5),
    _AlaQoSAppliedActionWredMaximumThreshold_Type()
)
alaQoSAppliedActionWredMaximumThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionWredMaximumThreshold.setStatus("current")


class _AlaQoSAppliedActionWredMaximumThresholdStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionWredMaximumThresholdStatus based on Integer32"""
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


_AlaQoSAppliedActionWredMaximumThresholdStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionWredMaximumThresholdStatus_Object = MibTableColumn
alaQoSAppliedActionWredMaximumThresholdStatus = _AlaQoSAppliedActionWredMaximumThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 6),
    _AlaQoSAppliedActionWredMaximumThresholdStatus_Type()
)
alaQoSAppliedActionWredMaximumThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionWredMaximumThresholdStatus.setStatus("current")
_AlaQoSAppliedActionWredMinimumThreshold_Type = Integer32
_AlaQoSAppliedActionWredMinimumThreshold_Object = MibTableColumn
alaQoSAppliedActionWredMinimumThreshold = _AlaQoSAppliedActionWredMinimumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 7),
    _AlaQoSAppliedActionWredMinimumThreshold_Type()
)
alaQoSAppliedActionWredMinimumThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionWredMinimumThreshold.setStatus("current")


class _AlaQoSAppliedActionWredMinimumThresholdStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionWredMinimumThresholdStatus based on Integer32"""
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


_AlaQoSAppliedActionWredMinimumThresholdStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionWredMinimumThresholdStatus_Object = MibTableColumn
alaQoSAppliedActionWredMinimumThresholdStatus = _AlaQoSAppliedActionWredMinimumThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 8),
    _AlaQoSAppliedActionWredMinimumThresholdStatus_Type()
)
alaQoSAppliedActionWredMinimumThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionWredMinimumThresholdStatus.setStatus("current")
_AlaQoSAppliedActionWredMaximumProbability_Type = Integer32
_AlaQoSAppliedActionWredMaximumProbability_Object = MibTableColumn
alaQoSAppliedActionWredMaximumProbability = _AlaQoSAppliedActionWredMaximumProbability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 9),
    _AlaQoSAppliedActionWredMaximumProbability_Type()
)
alaQoSAppliedActionWredMaximumProbability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionWredMaximumProbability.setStatus("current")


class _AlaQoSAppliedActionWredMaximumProbabilityStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionWredMaximumProbabilityStatus based on Integer32"""
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


_AlaQoSAppliedActionWredMaximumProbabilityStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionWredMaximumProbabilityStatus_Object = MibTableColumn
alaQoSAppliedActionWredMaximumProbabilityStatus = _AlaQoSAppliedActionWredMaximumProbabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 10),
    _AlaQoSAppliedActionWredMaximumProbabilityStatus_Type()
)
alaQoSAppliedActionWredMaximumProbabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionWredMaximumProbabilityStatus.setStatus("current")
_AlaQoSAppliedActionMinimumBandwidth_Type = Integer32
_AlaQoSAppliedActionMinimumBandwidth_Object = MibTableColumn
alaQoSAppliedActionMinimumBandwidth = _AlaQoSAppliedActionMinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 11),
    _AlaQoSAppliedActionMinimumBandwidth_Type()
)
alaQoSAppliedActionMinimumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMinimumBandwidth.setStatus("current")


class _AlaQoSAppliedActionMinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMinimumBandwidthStatus based on Integer32"""
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


_AlaQoSAppliedActionMinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMinimumBandwidthStatus_Object = MibTableColumn
alaQoSAppliedActionMinimumBandwidthStatus = _AlaQoSAppliedActionMinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 12),
    _AlaQoSAppliedActionMinimumBandwidthStatus_Type()
)
alaQoSAppliedActionMinimumBandwidthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMinimumBandwidthStatus.setStatus("current")
_AlaQoSAppliedActionMaximumBandwidth_Type = Integer32
_AlaQoSAppliedActionMaximumBandwidth_Object = MibTableColumn
alaQoSAppliedActionMaximumBandwidth = _AlaQoSAppliedActionMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 13),
    _AlaQoSAppliedActionMaximumBandwidth_Type()
)
alaQoSAppliedActionMaximumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumBandwidth.setStatus("current")


class _AlaQoSAppliedActionMaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMaximumBandwidthStatus based on Integer32"""
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


_AlaQoSAppliedActionMaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMaximumBandwidthStatus_Object = MibTableColumn
alaQoSAppliedActionMaximumBandwidthStatus = _AlaQoSAppliedActionMaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 14),
    _AlaQoSAppliedActionMaximumBandwidthStatus_Type()
)
alaQoSAppliedActionMaximumBandwidthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumBandwidthStatus.setStatus("current")
_AlaQoSAppliedActionPeakBandwidth_Type = Integer32
_AlaQoSAppliedActionPeakBandwidth_Object = MibTableColumn
alaQoSAppliedActionPeakBandwidth = _AlaQoSAppliedActionPeakBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 15),
    _AlaQoSAppliedActionPeakBandwidth_Type()
)
alaQoSAppliedActionPeakBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPeakBandwidth.setStatus("current")


class _AlaQoSAppliedActionPeakBandwidthStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPeakBandwidthStatus based on Integer32"""
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


_AlaQoSAppliedActionPeakBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPeakBandwidthStatus_Object = MibTableColumn
alaQoSAppliedActionPeakBandwidthStatus = _AlaQoSAppliedActionPeakBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 16),
    _AlaQoSAppliedActionPeakBandwidthStatus_Type()
)
alaQoSAppliedActionPeakBandwidthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPeakBandwidthStatus.setStatus("current")


class _AlaQoSAppliedActionPriority_Type(Integer32):
    """Custom type alaQoSAppliedActionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedActionPriority_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPriority_Object = MibTableColumn
alaQoSAppliedActionPriority = _AlaQoSAppliedActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 17),
    _AlaQoSAppliedActionPriority_Type()
)
alaQoSAppliedActionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPriority.setStatus("current")


class _AlaQoSAppliedActionPriorityStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPriorityStatus based on Integer32"""
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


_AlaQoSAppliedActionPriorityStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPriorityStatus_Object = MibTableColumn
alaQoSAppliedActionPriorityStatus = _AlaQoSAppliedActionPriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 18),
    _AlaQoSAppliedActionPriorityStatus_Type()
)
alaQoSAppliedActionPriorityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPriorityStatus.setStatus("current")


class _AlaQoSAppliedActionShared_Type(Integer32):
    """Custom type alaQoSAppliedActionShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedActionShared_Type.__name__ = "Integer32"
_AlaQoSAppliedActionShared_Object = MibTableColumn
alaQoSAppliedActionShared = _AlaQoSAppliedActionShared_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 19),
    _AlaQoSAppliedActionShared_Type()
)
alaQoSAppliedActionShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionShared.setStatus("current")
_AlaQoSAppliedActionJitter_Type = Integer32
_AlaQoSAppliedActionJitter_Object = MibTableColumn
alaQoSAppliedActionJitter = _AlaQoSAppliedActionJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 20),
    _AlaQoSAppliedActionJitter_Type()
)
alaQoSAppliedActionJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionJitter.setStatus("current")


class _AlaQoSAppliedActionJitterStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionJitterStatus based on Integer32"""
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


_AlaQoSAppliedActionJitterStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionJitterStatus_Object = MibTableColumn
alaQoSAppliedActionJitterStatus = _AlaQoSAppliedActionJitterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 21),
    _AlaQoSAppliedActionJitterStatus_Type()
)
alaQoSAppliedActionJitterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionJitterStatus.setStatus("current")
_AlaQoSAppliedActionLatency_Type = Integer32
_AlaQoSAppliedActionLatency_Object = MibTableColumn
alaQoSAppliedActionLatency = _AlaQoSAppliedActionLatency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 22),
    _AlaQoSAppliedActionLatency_Type()
)
alaQoSAppliedActionLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionLatency.setStatus("current")


class _AlaQoSAppliedActionLatencyStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionLatencyStatus based on Integer32"""
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


_AlaQoSAppliedActionLatencyStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionLatencyStatus_Object = MibTableColumn
alaQoSAppliedActionLatencyStatus = _AlaQoSAppliedActionLatencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 23),
    _AlaQoSAppliedActionLatencyStatus_Type()
)
alaQoSAppliedActionLatencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionLatencyStatus.setStatus("current")
_AlaQoSAppliedActionMaximumDepth_Type = Integer32
_AlaQoSAppliedActionMaximumDepth_Object = MibTableColumn
alaQoSAppliedActionMaximumDepth = _AlaQoSAppliedActionMaximumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 24),
    _AlaQoSAppliedActionMaximumDepth_Type()
)
alaQoSAppliedActionMaximumDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumDepth.setStatus("current")


class _AlaQoSAppliedActionMaximumDepthStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMaximumDepthStatus based on Integer32"""
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


_AlaQoSAppliedActionMaximumDepthStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMaximumDepthStatus_Object = MibTableColumn
alaQoSAppliedActionMaximumDepthStatus = _AlaQoSAppliedActionMaximumDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 25),
    _AlaQoSAppliedActionMaximumDepthStatus_Type()
)
alaQoSAppliedActionMaximumDepthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumDepthStatus.setStatus("current")


class _AlaQoSAppliedActionMaximumBuffers_Type(Integer32):
    """Custom type alaQoSAppliedActionMaximumBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_AlaQoSAppliedActionMaximumBuffers_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMaximumBuffers_Object = MibTableColumn
alaQoSAppliedActionMaximumBuffers = _AlaQoSAppliedActionMaximumBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 26),
    _AlaQoSAppliedActionMaximumBuffers_Type()
)
alaQoSAppliedActionMaximumBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumBuffers.setStatus("current")


class _AlaQoSAppliedActionMaximumBuffersStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMaximumBuffersStatus based on Integer32"""
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


_AlaQoSAppliedActionMaximumBuffersStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMaximumBuffersStatus_Object = MibTableColumn
alaQoSAppliedActionMaximumBuffersStatus = _AlaQoSAppliedActionMaximumBuffersStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 27),
    _AlaQoSAppliedActionMaximumBuffersStatus_Type()
)
alaQoSAppliedActionMaximumBuffersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMaximumBuffersStatus.setStatus("current")


class _AlaQoSAppliedAction8021p_Type(Integer32):
    """Custom type alaQoSAppliedAction8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedAction8021p_Type.__name__ = "Integer32"
_AlaQoSAppliedAction8021p_Object = MibTableColumn
alaQoSAppliedAction8021p = _AlaQoSAppliedAction8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 28),
    _AlaQoSAppliedAction8021p_Type()
)
alaQoSAppliedAction8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedAction8021p.setStatus("current")


class _AlaQoSAppliedAction8021pStatus_Type(Integer32):
    """Custom type alaQoSAppliedAction8021pStatus based on Integer32"""
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


_AlaQoSAppliedAction8021pStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedAction8021pStatus_Object = MibTableColumn
alaQoSAppliedAction8021pStatus = _AlaQoSAppliedAction8021pStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 29),
    _AlaQoSAppliedAction8021pStatus_Type()
)
alaQoSAppliedAction8021pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedAction8021pStatus.setStatus("current")


class _AlaQoSAppliedActionTos_Type(Integer32):
    """Custom type alaQoSAppliedActionTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSAppliedActionTos_Type.__name__ = "Integer32"
_AlaQoSAppliedActionTos_Object = MibTableColumn
alaQoSAppliedActionTos = _AlaQoSAppliedActionTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 30),
    _AlaQoSAppliedActionTos_Type()
)
alaQoSAppliedActionTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionTos.setStatus("current")


class _AlaQoSAppliedActionTosStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionTosStatus based on Integer32"""
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


_AlaQoSAppliedActionTosStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionTosStatus_Object = MibTableColumn
alaQoSAppliedActionTosStatus = _AlaQoSAppliedActionTosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 31),
    _AlaQoSAppliedActionTosStatus_Type()
)
alaQoSAppliedActionTosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionTosStatus.setStatus("current")


class _AlaQoSAppliedActionDscp_Type(Integer32):
    """Custom type alaQoSAppliedActionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSAppliedActionDscp_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDscp_Object = MibTableColumn
alaQoSAppliedActionDscp = _AlaQoSAppliedActionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 32),
    _AlaQoSAppliedActionDscp_Type()
)
alaQoSAppliedActionDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDscp.setStatus("current")


class _AlaQoSAppliedActionDscpStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionDscpStatus based on Integer32"""
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


_AlaQoSAppliedActionDscpStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDscpStatus_Object = MibTableColumn
alaQoSAppliedActionDscpStatus = _AlaQoSAppliedActionDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 33),
    _AlaQoSAppliedActionDscpStatus_Type()
)
alaQoSAppliedActionDscpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDscpStatus.setStatus("current")


class _AlaQoSAppliedActionMapFrom_Type(Integer32):
    """Custom type alaQoSAppliedActionMapFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b8021p", 1),
          ("dscp", 3),
          ("tos", 2))
    )


_AlaQoSAppliedActionMapFrom_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMapFrom_Object = MibTableColumn
alaQoSAppliedActionMapFrom = _AlaQoSAppliedActionMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 34),
    _AlaQoSAppliedActionMapFrom_Type()
)
alaQoSAppliedActionMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapFrom.setStatus("current")


class _AlaQoSAppliedActionMapTo_Type(Integer32):
    """Custom type alaQoSAppliedActionMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b8021p", 1),
          ("dscp", 3),
          ("tos", 2))
    )


_AlaQoSAppliedActionMapTo_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMapTo_Object = MibTableColumn
alaQoSAppliedActionMapTo = _AlaQoSAppliedActionMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 35),
    _AlaQoSAppliedActionMapTo_Type()
)
alaQoSAppliedActionMapTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapTo.setStatus("current")


class _AlaQoSAppliedActionMapGroup_Type(DisplayString):
    """Custom type alaQoSAppliedActionMapGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedActionMapGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedActionMapGroup_Object = MibTableColumn
alaQoSAppliedActionMapGroup = _AlaQoSAppliedActionMapGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 36),
    _AlaQoSAppliedActionMapGroup_Type()
)
alaQoSAppliedActionMapGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapGroup.setStatus("current")


class _AlaQoSAppliedActionMapGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMapGroupStatus based on Integer32"""
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


_AlaQoSAppliedActionMapGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMapGroupStatus_Object = MibTableColumn
alaQoSAppliedActionMapGroupStatus = _AlaQoSAppliedActionMapGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 37),
    _AlaQoSAppliedActionMapGroupStatus_Type()
)
alaQoSAppliedActionMapGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMapGroupStatus.setStatus("current")
_AlaQoSAppliedActionSourceRewriteIpAddr_Type = IpAddress
_AlaQoSAppliedActionSourceRewriteIpAddr_Object = MibTableColumn
alaQoSAppliedActionSourceRewriteIpAddr = _AlaQoSAppliedActionSourceRewriteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 38),
    _AlaQoSAppliedActionSourceRewriteIpAddr_Type()
)
alaQoSAppliedActionSourceRewriteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionSourceRewriteIpAddr.setStatus("current")


class _AlaQoSAppliedActionSourceRewriteIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionSourceRewriteIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedActionSourceRewriteIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionSourceRewriteIpAddrStatus_Object = MibTableColumn
alaQoSAppliedActionSourceRewriteIpAddrStatus = _AlaQoSAppliedActionSourceRewriteIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 39),
    _AlaQoSAppliedActionSourceRewriteIpAddrStatus_Type()
)
alaQoSAppliedActionSourceRewriteIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionSourceRewriteIpAddrStatus.setStatus("current")
_AlaQoSAppliedActionSourceRewriteIpMask_Type = IpAddress
_AlaQoSAppliedActionSourceRewriteIpMask_Object = MibTableColumn
alaQoSAppliedActionSourceRewriteIpMask = _AlaQoSAppliedActionSourceRewriteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 40),
    _AlaQoSAppliedActionSourceRewriteIpMask_Type()
)
alaQoSAppliedActionSourceRewriteIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionSourceRewriteIpMask.setStatus("current")


class _AlaQoSAppliedActionSourceRewriteNetworkGroup_Type(DisplayString):
    """Custom type alaQoSAppliedActionSourceRewriteNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedActionSourceRewriteNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedActionSourceRewriteNetworkGroup_Object = MibTableColumn
alaQoSAppliedActionSourceRewriteNetworkGroup = _AlaQoSAppliedActionSourceRewriteNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 41),
    _AlaQoSAppliedActionSourceRewriteNetworkGroup_Type()
)
alaQoSAppliedActionSourceRewriteNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionSourceRewriteNetworkGroup.setStatus("current")


class _AlaQoSAppliedActionSourceRewriteNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionSourceRewriteNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedActionSourceRewriteNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionSourceRewriteNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedActionSourceRewriteNetworkGroupStatus = _AlaQoSAppliedActionSourceRewriteNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 42),
    _AlaQoSAppliedActionSourceRewriteNetworkGroupStatus_Type()
)
alaQoSAppliedActionSourceRewriteNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionSourceRewriteNetworkGroupStatus.setStatus("current")
_AlaQoSAppliedActionDestinationRewriteIpAddr_Type = IpAddress
_AlaQoSAppliedActionDestinationRewriteIpAddr_Object = MibTableColumn
alaQoSAppliedActionDestinationRewriteIpAddr = _AlaQoSAppliedActionDestinationRewriteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 43),
    _AlaQoSAppliedActionDestinationRewriteIpAddr_Type()
)
alaQoSAppliedActionDestinationRewriteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDestinationRewriteIpAddr.setStatus("current")


class _AlaQoSAppliedActionDestinationRewriteIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionDestinationRewriteIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedActionDestinationRewriteIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDestinationRewriteIpAddrStatus_Object = MibTableColumn
alaQoSAppliedActionDestinationRewriteIpAddrStatus = _AlaQoSAppliedActionDestinationRewriteIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 44),
    _AlaQoSAppliedActionDestinationRewriteIpAddrStatus_Type()
)
alaQoSAppliedActionDestinationRewriteIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDestinationRewriteIpAddrStatus.setStatus("current")
_AlaQoSAppliedActionDestinationRewriteIpMask_Type = IpAddress
_AlaQoSAppliedActionDestinationRewriteIpMask_Object = MibTableColumn
alaQoSAppliedActionDestinationRewriteIpMask = _AlaQoSAppliedActionDestinationRewriteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 45),
    _AlaQoSAppliedActionDestinationRewriteIpMask_Type()
)
alaQoSAppliedActionDestinationRewriteIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDestinationRewriteIpMask.setStatus("current")


class _AlaQoSAppliedActionDestinationRewriteNetworkGroup_Type(DisplayString):
    """Custom type alaQoSAppliedActionDestinationRewriteNetworkGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedActionDestinationRewriteNetworkGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedActionDestinationRewriteNetworkGroup_Object = MibTableColumn
alaQoSAppliedActionDestinationRewriteNetworkGroup = _AlaQoSAppliedActionDestinationRewriteNetworkGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 46),
    _AlaQoSAppliedActionDestinationRewriteNetworkGroup_Type()
)
alaQoSAppliedActionDestinationRewriteNetworkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDestinationRewriteNetworkGroup.setStatus("current")


class _AlaQoSAppliedActionDestinationRewriteNetworkGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionDestinationRewriteNetworkGroupStatus based on Integer32"""
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


_AlaQoSAppliedActionDestinationRewriteNetworkGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionDestinationRewriteNetworkGroupStatus_Object = MibTableColumn
alaQoSAppliedActionDestinationRewriteNetworkGroupStatus = _AlaQoSAppliedActionDestinationRewriteNetworkGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 47),
    _AlaQoSAppliedActionDestinationRewriteNetworkGroupStatus_Type()
)
alaQoSAppliedActionDestinationRewriteNetworkGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionDestinationRewriteNetworkGroupStatus.setStatus("current")


class _AlaQoSAppliedActionLoadBalanceGroup_Type(DisplayString):
    """Custom type alaQoSAppliedActionLoadBalanceGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_AlaQoSAppliedActionLoadBalanceGroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedActionLoadBalanceGroup_Object = MibTableColumn
alaQoSAppliedActionLoadBalanceGroup = _AlaQoSAppliedActionLoadBalanceGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 48),
    _AlaQoSAppliedActionLoadBalanceGroup_Type()
)
alaQoSAppliedActionLoadBalanceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionLoadBalanceGroup.setStatus("current")


class _AlaQoSAppliedActionLoadBalanceGroupStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionLoadBalanceGroupStatus based on Integer32"""
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


_AlaQoSAppliedActionLoadBalanceGroupStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionLoadBalanceGroupStatus_Object = MibTableColumn
alaQoSAppliedActionLoadBalanceGroupStatus = _AlaQoSAppliedActionLoadBalanceGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 49),
    _AlaQoSAppliedActionLoadBalanceGroupStatus_Type()
)
alaQoSAppliedActionLoadBalanceGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionLoadBalanceGroupStatus.setStatus("current")
_AlaQoSAppliedActionPermanentGatewayIpAddr_Type = IpAddress
_AlaQoSAppliedActionPermanentGatewayIpAddr_Object = MibTableColumn
alaQoSAppliedActionPermanentGatewayIpAddr = _AlaQoSAppliedActionPermanentGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 50),
    _AlaQoSAppliedActionPermanentGatewayIpAddr_Type()
)
alaQoSAppliedActionPermanentGatewayIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPermanentGatewayIpAddr.setStatus("current")


class _AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPermanentGatewayIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Object = MibTableColumn
alaQoSAppliedActionPermanentGatewayIpAddrStatus = _AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 51),
    _AlaQoSAppliedActionPermanentGatewayIpAddrStatus_Type()
)
alaQoSAppliedActionPermanentGatewayIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPermanentGatewayIpAddrStatus.setStatus("current")
_AlaQoSAppliedActionAlternateGatewayIpAddr_Type = IpAddress
_AlaQoSAppliedActionAlternateGatewayIpAddr_Object = MibTableColumn
alaQoSAppliedActionAlternateGatewayIpAddr = _AlaQoSAppliedActionAlternateGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 52),
    _AlaQoSAppliedActionAlternateGatewayIpAddr_Type()
)
alaQoSAppliedActionAlternateGatewayIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionAlternateGatewayIpAddr.setStatus("current")


class _AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionAlternateGatewayIpAddrStatus based on Integer32"""
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


_AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Object = MibTableColumn
alaQoSAppliedActionAlternateGatewayIpAddrStatus = _AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 53),
    _AlaQoSAppliedActionAlternateGatewayIpAddrStatus_Type()
)
alaQoSAppliedActionAlternateGatewayIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionAlternateGatewayIpAddrStatus.setStatus("current")
_AlaQoSAppliedActionRowStatus_Type = RowStatus
_AlaQoSAppliedActionRowStatus_Object = MibTableColumn
alaQoSAppliedActionRowStatus = _AlaQoSAppliedActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 54),
    _AlaQoSAppliedActionRowStatus_Type()
)
alaQoSAppliedActionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRowStatus.setStatus("current")
_AlaQoSAppliedActionMinimumDepth_Type = Integer32
_AlaQoSAppliedActionMinimumDepth_Object = MibTableColumn
alaQoSAppliedActionMinimumDepth = _AlaQoSAppliedActionMinimumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 55),
    _AlaQoSAppliedActionMinimumDepth_Type()
)
alaQoSAppliedActionMinimumDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMinimumDepth.setStatus("current")


class _AlaQoSAppliedActionMinimumDepthStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMinimumDepthStatus based on Integer32"""
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


_AlaQoSAppliedActionMinimumDepthStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMinimumDepthStatus_Object = MibTableColumn
alaQoSAppliedActionMinimumDepthStatus = _AlaQoSAppliedActionMinimumDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 56),
    _AlaQoSAppliedActionMinimumDepthStatus_Type()
)
alaQoSAppliedActionMinimumDepthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMinimumDepthStatus.setStatus("current")


class _AlaQoSAppliedActionVPNAccess_Type(Integer32):
    """Custom type alaQoSAppliedActionVPNAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("drop", 3),
          ("protect", 1))
    )


_AlaQoSAppliedActionVPNAccess_Type.__name__ = "Integer32"
_AlaQoSAppliedActionVPNAccess_Object = MibTableColumn
alaQoSAppliedActionVPNAccess = _AlaQoSAppliedActionVPNAccess_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 57),
    _AlaQoSAppliedActionVPNAccess_Type()
)
alaQoSAppliedActionVPNAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionVPNAccess.setStatus("current")


class _AlaQoSAppliedActionNocache_Type(Integer32):
    """Custom type alaQoSAppliedActionNocache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedActionNocache_Type.__name__ = "Integer32"
_AlaQoSAppliedActionNocache_Object = MibTableColumn
alaQoSAppliedActionNocache = _AlaQoSAppliedActionNocache_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 58),
    _AlaQoSAppliedActionNocache_Type()
)
alaQoSAppliedActionNocache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionNocache.setStatus("current")


class _AlaQoSAppliedActionPortdisable_Type(Integer32):
    """Custom type alaQoSAppliedActionPortdisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSAppliedActionPortdisable_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPortdisable_Object = MibTableColumn
alaQoSAppliedActionPortdisable = _AlaQoSAppliedActionPortdisable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 59),
    _AlaQoSAppliedActionPortdisable_Type()
)
alaQoSAppliedActionPortdisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPortdisable.setStatus("current")


class _AlaQoSAppliedActionRedirectSlot_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedActionRedirectSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectSlot_Object = MibTableColumn
alaQoSAppliedActionRedirectSlot = _AlaQoSAppliedActionRedirectSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 60),
    _AlaQoSAppliedActionRedirectSlot_Type()
)
alaQoSAppliedActionRedirectSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectSlot.setStatus("current")


class _AlaQoSAppliedActionRedirectSlotStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectSlotStatus based on Integer32"""
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


_AlaQoSAppliedActionRedirectSlotStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectSlotStatus_Object = MibTableColumn
alaQoSAppliedActionRedirectSlotStatus = _AlaQoSAppliedActionRedirectSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 61),
    _AlaQoSAppliedActionRedirectSlotStatus_Type()
)
alaQoSAppliedActionRedirectSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectSlotStatus.setStatus("current")


class _AlaQoSAppliedActionRedirectPort_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedActionRedirectPort_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectPort_Object = MibTableColumn
alaQoSAppliedActionRedirectPort = _AlaQoSAppliedActionRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 62),
    _AlaQoSAppliedActionRedirectPort_Type()
)
alaQoSAppliedActionRedirectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectPort.setStatus("current")


class _AlaQoSAppliedActionRedirectAgg_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectAgg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AlaQoSAppliedActionRedirectAgg_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectAgg_Object = MibTableColumn
alaQoSAppliedActionRedirectAgg = _AlaQoSAppliedActionRedirectAgg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 63),
    _AlaQoSAppliedActionRedirectAgg_Type()
)
alaQoSAppliedActionRedirectAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectAgg.setStatus("current")


class _AlaQoSAppliedActionRedirectAggStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionRedirectAggStatus based on Integer32"""
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


_AlaQoSAppliedActionRedirectAggStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionRedirectAggStatus_Object = MibTableColumn
alaQoSAppliedActionRedirectAggStatus = _AlaQoSAppliedActionRedirectAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 64),
    _AlaQoSAppliedActionRedirectAggStatus_Type()
)
alaQoSAppliedActionRedirectAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionRedirectAggStatus.setStatus("current")


class _AlaQoSAppliedActionMirrorSlot_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedActionMirrorSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorSlot_Object = MibTableColumn
alaQoSAppliedActionMirrorSlot = _AlaQoSAppliedActionMirrorSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 65),
    _AlaQoSAppliedActionMirrorSlot_Type()
)
alaQoSAppliedActionMirrorSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorSlot.setStatus("current")


class _AlaQoSAppliedActionMirrorPort_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_AlaQoSAppliedActionMirrorPort_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorPort_Object = MibTableColumn
alaQoSAppliedActionMirrorPort = _AlaQoSAppliedActionMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 66),
    _AlaQoSAppliedActionMirrorPort_Type()
)
alaQoSAppliedActionMirrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorPort.setStatus("current")


class _AlaQoSAppliedActionMirrorMode_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorMode based on Integer32"""
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
        *(("both", 3),
          ("egress", 2),
          ("ingress", 1))
    )


_AlaQoSAppliedActionMirrorMode_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorMode_Object = MibTableColumn
alaQoSAppliedActionMirrorMode = _AlaQoSAppliedActionMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 67),
    _AlaQoSAppliedActionMirrorMode_Type()
)
alaQoSAppliedActionMirrorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorMode.setStatus("current")


class _AlaQoSAppliedActionMirrorModeStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionMirrorModeStatus based on Integer32"""
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


_AlaQoSAppliedActionMirrorModeStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionMirrorModeStatus_Object = MibTableColumn
alaQoSAppliedActionMirrorModeStatus = _AlaQoSAppliedActionMirrorModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 68),
    _AlaQoSAppliedActionMirrorModeStatus_Type()
)
alaQoSAppliedActionMirrorModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedActionMirrorModeStatus.setStatus("current")


class _AlaQoSAppliedActionCIR_Type(Integer32):
    """Custom type alaQoSAppliedActionCIR based on Integer32"""
    defaultValue = 0


_AlaQoSAppliedActionCIR_Object = MibTableColumn
alaQoSAppliedActionCIR = _AlaQoSAppliedActionCIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 69),
    _AlaQoSAppliedActionCIR_Type()
)
alaQoSAppliedActionCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCIR.setUnits("kilobits per second")


class _AlaQoSAppliedActionCIRStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionCIRStatus based on Integer32"""
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


_AlaQoSAppliedActionCIRStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCIRStatus_Object = MibTableColumn
alaQoSAppliedActionCIRStatus = _AlaQoSAppliedActionCIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 70),
    _AlaQoSAppliedActionCIRStatus_Type()
)
alaQoSAppliedActionCIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCIRStatus.setStatus("current")


class _AlaQoSAppliedActionCBS_Type(Integer32):
    """Custom type alaQoSAppliedActionCBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSAppliedActionCBS_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCBS_Object = MibTableColumn
alaQoSAppliedActionCBS = _AlaQoSAppliedActionCBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 71),
    _AlaQoSAppliedActionCBS_Type()
)
alaQoSAppliedActionCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCBS.setStatus("current")


class _AlaQoSAppliedActionCBSStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionCBSStatus based on Integer32"""
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


_AlaQoSAppliedActionCBSStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCBSStatus_Object = MibTableColumn
alaQoSAppliedActionCBSStatus = _AlaQoSAppliedActionCBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 72),
    _AlaQoSAppliedActionCBSStatus_Type()
)
alaQoSAppliedActionCBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCBSStatus.setStatus("current")


class _AlaQoSAppliedActionPIR_Type(Integer32):
    """Custom type alaQoSAppliedActionPIR based on Integer32"""
    defaultValue = 0


_AlaQoSAppliedActionPIR_Object = MibTableColumn
alaQoSAppliedActionPIR = _AlaQoSAppliedActionPIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 73),
    _AlaQoSAppliedActionPIR_Type()
)
alaQoSAppliedActionPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPIR.setStatus("current")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPIR.setUnits("kilobits per second")


class _AlaQoSAppliedActionPIRStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPIRStatus based on Integer32"""
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


_AlaQoSAppliedActionPIRStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPIRStatus_Object = MibTableColumn
alaQoSAppliedActionPIRStatus = _AlaQoSAppliedActionPIRStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 74),
    _AlaQoSAppliedActionPIRStatus_Type()
)
alaQoSAppliedActionPIRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPIRStatus.setStatus("current")


class _AlaQoSAppliedActionPBS_Type(Integer32):
    """Custom type alaQoSAppliedActionPBS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147450880),
    )


_AlaQoSAppliedActionPBS_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPBS_Object = MibTableColumn
alaQoSAppliedActionPBS = _AlaQoSAppliedActionPBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 75),
    _AlaQoSAppliedActionPBS_Type()
)
alaQoSAppliedActionPBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPBS.setStatus("current")


class _AlaQoSAppliedActionPBSStatus_Type(Integer32):
    """Custom type alaQoSAppliedActionPBSStatus based on Integer32"""
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


_AlaQoSAppliedActionPBSStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedActionPBSStatus_Object = MibTableColumn
alaQoSAppliedActionPBSStatus = _AlaQoSAppliedActionPBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 76),
    _AlaQoSAppliedActionPBSStatus_Type()
)
alaQoSAppliedActionPBSStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionPBSStatus.setStatus("current")


class _AlaQoSAppliedActionCounterColor_Type(Integer32):
    """Custom type alaQoSAppliedActionCounterColor based on Integer32"""
    defaultValue = 5

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
        *(("greennongreen", 2),
          ("greenred", 3),
          ("greenyellow", 4),
          ("rednonred", 1),
          ("redyellow", 5))
    )


_AlaQoSAppliedActionCounterColor_Type.__name__ = "Integer32"
_AlaQoSAppliedActionCounterColor_Object = MibTableColumn
alaQoSAppliedActionCounterColor = _AlaQoSAppliedActionCounterColor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 28, 1, 77),
    _AlaQoSAppliedActionCounterColor_Type()
)
alaQoSAppliedActionCounterColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedActionCounterColor.setStatus("current")
_AlaQoSPortTable_Object = MibTable
alaQoSPortTable = _AlaQoSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29)
)
if mibBuilder.loadTexts:
    alaQoSPortTable.setStatus("current")
_AlaQoSPortEntry_Object = MibTableRow
alaQoSPortEntry = _AlaQoSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1)
)
alaQoSPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortPort"),
)
if mibBuilder.loadTexts:
    alaQoSPortEntry.setStatus("current")


class _AlaQoSPortSlot_Type(Integer32):
    """Custom type alaQoSPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSPortSlot_Type.__name__ = "Integer32"
_AlaQoSPortSlot_Object = MibTableColumn
alaQoSPortSlot = _AlaQoSPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 1),
    _AlaQoSPortSlot_Type()
)
alaQoSPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortSlot.setStatus("current")


class _AlaQoSPortPort_Type(Integer32):
    """Custom type alaQoSPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSPortPort_Type.__name__ = "Integer32"
_AlaQoSPortPort_Object = MibTableColumn
alaQoSPortPort = _AlaQoSPortPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 2),
    _AlaQoSPortPort_Type()
)
alaQoSPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortPort.setStatus("current")


class _AlaQoSPortEnabled_Type(Integer32):
    """Custom type alaQoSPortEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSPortEnabled_Type.__name__ = "Integer32"
_AlaQoSPortEnabled_Object = MibTableColumn
alaQoSPortEnabled = _AlaQoSPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 3),
    _AlaQoSPortEnabled_Type()
)
alaQoSPortEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnabled.setStatus("current")


class _AlaQoSPortAppliedEnabled_Type(Integer32):
    """Custom type alaQoSPortAppliedEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSPortAppliedEnabled_Type.__name__ = "Integer32"
_AlaQoSPortAppliedEnabled_Object = MibTableColumn
alaQoSPortAppliedEnabled = _AlaQoSPortAppliedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 4),
    _AlaQoSPortAppliedEnabled_Type()
)
alaQoSPortAppliedEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedEnabled.setStatus("current")


class _AlaQoSPortInterfaceType_Type(Integer32):
    """Custom type alaQoSPortInterfaceType based on Integer32"""
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
        *(("aggregate", 7),
          ("ethernet", 1),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet10G", 6),
          ("ethernet1G", 5),
          ("wan", 2))
    )


_AlaQoSPortInterfaceType_Type.__name__ = "Integer32"
_AlaQoSPortInterfaceType_Object = MibTableColumn
alaQoSPortInterfaceType = _AlaQoSPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 5),
    _AlaQoSPortInterfaceType_Type()
)
alaQoSPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortInterfaceType.setStatus("current")


class _AlaQoSPortTrusted_Type(Integer32):
    """Custom type alaQoSPortTrusted based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSPortTrusted_Type.__name__ = "Integer32"
_AlaQoSPortTrusted_Object = MibTableColumn
alaQoSPortTrusted = _AlaQoSPortTrusted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 6),
    _AlaQoSPortTrusted_Type()
)
alaQoSPortTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortTrusted.setStatus("current")


class _AlaQoSPortDefault8021p_Type(Integer32):
    """Custom type alaQoSPortDefault8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSPortDefault8021p_Type.__name__ = "Integer32"
_AlaQoSPortDefault8021p_Object = MibTableColumn
alaQoSPortDefault8021p = _AlaQoSPortDefault8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 7),
    _AlaQoSPortDefault8021p_Type()
)
alaQoSPortDefault8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDefault8021p.setStatus("current")


class _AlaQoSPortDefaultDSCP_Type(Integer32):
    """Custom type alaQoSPortDefaultDSCP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSPortDefaultDSCP_Type.__name__ = "Integer32"
_AlaQoSPortDefaultDSCP_Object = MibTableColumn
alaQoSPortDefaultDSCP = _AlaQoSPortDefaultDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 8),
    _AlaQoSPortDefaultDSCP_Type()
)
alaQoSPortDefaultDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDefaultDSCP.setStatus("current")


class _AlaQoSPortMaximumReservedBandwidth_Type(Integer32):
    """Custom type alaQoSPortMaximumReservedBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumReservedBandwidth_Object = MibTableColumn
alaQoSPortMaximumReservedBandwidth = _AlaQoSPortMaximumReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 9),
    _AlaQoSPortMaximumReservedBandwidth_Type()
)
alaQoSPortMaximumReservedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumReservedBandwidth.setStatus("current")


class _AlaQoSPortMaximumReservedBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumReservedBandwidthStatus based on Integer32"""
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


_AlaQoSPortMaximumReservedBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumReservedBandwidthStatus_Object = MibTableColumn
alaQoSPortMaximumReservedBandwidthStatus = _AlaQoSPortMaximumReservedBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 10),
    _AlaQoSPortMaximumReservedBandwidthStatus_Type()
)
alaQoSPortMaximumReservedBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumReservedBandwidthStatus.setStatus("current")
_AlaQoSPortAppliedMaximumReservedBandwidth_Type = Integer32
_AlaQoSPortAppliedMaximumReservedBandwidth_Object = MibTableColumn
alaQoSPortAppliedMaximumReservedBandwidth = _AlaQoSPortAppliedMaximumReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 11),
    _AlaQoSPortAppliedMaximumReservedBandwidth_Type()
)
alaQoSPortAppliedMaximumReservedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumReservedBandwidth.setStatus("current")


class _AlaQoSPortAppliedMaximumReservedBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortAppliedMaximumReservedBandwidthStatus based on Integer32"""
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


_AlaQoSPortAppliedMaximumReservedBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortAppliedMaximumReservedBandwidthStatus_Object = MibTableColumn
alaQoSPortAppliedMaximumReservedBandwidthStatus = _AlaQoSPortAppliedMaximumReservedBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 12),
    _AlaQoSPortAppliedMaximumReservedBandwidthStatus_Type()
)
alaQoSPortAppliedMaximumReservedBandwidthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumReservedBandwidthStatus.setStatus("current")


class _AlaQoSPortMaximumSignalledBandwidth_Type(Integer32):
    """Custom type alaQoSPortMaximumSignalledBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumSignalledBandwidth_Object = MibTableColumn
alaQoSPortMaximumSignalledBandwidth = _AlaQoSPortMaximumSignalledBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 13),
    _AlaQoSPortMaximumSignalledBandwidth_Type()
)
alaQoSPortMaximumSignalledBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumSignalledBandwidth.setStatus("current")


class _AlaQoSPortMaximumSignalledBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumSignalledBandwidthStatus based on Integer32"""
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


_AlaQoSPortMaximumSignalledBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumSignalledBandwidthStatus_Object = MibTableColumn
alaQoSPortMaximumSignalledBandwidthStatus = _AlaQoSPortMaximumSignalledBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 14),
    _AlaQoSPortMaximumSignalledBandwidthStatus_Type()
)
alaQoSPortMaximumSignalledBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumSignalledBandwidthStatus.setStatus("current")
_AlaQoSPortAppliedMaximumSignalledBandwidth_Type = Integer32
_AlaQoSPortAppliedMaximumSignalledBandwidth_Object = MibTableColumn
alaQoSPortAppliedMaximumSignalledBandwidth = _AlaQoSPortAppliedMaximumSignalledBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 15),
    _AlaQoSPortAppliedMaximumSignalledBandwidth_Type()
)
alaQoSPortAppliedMaximumSignalledBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumSignalledBandwidth.setStatus("current")


class _AlaQoSPortAppliedMaximumSignalledBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortAppliedMaximumSignalledBandwidthStatus based on Integer32"""
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


_AlaQoSPortAppliedMaximumSignalledBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortAppliedMaximumSignalledBandwidthStatus_Object = MibTableColumn
alaQoSPortAppliedMaximumSignalledBandwidthStatus = _AlaQoSPortAppliedMaximumSignalledBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 16),
    _AlaQoSPortAppliedMaximumSignalledBandwidthStatus_Type()
)
alaQoSPortAppliedMaximumSignalledBandwidthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumSignalledBandwidthStatus.setStatus("current")


class _AlaQoSPortDefaultQueues_Type(Integer32):
    """Custom type alaQoSPortDefaultQueues based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
    )


_AlaQoSPortDefaultQueues_Type.__name__ = "Integer32"
_AlaQoSPortDefaultQueues_Object = MibTableColumn
alaQoSPortDefaultQueues = _AlaQoSPortDefaultQueues_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 17),
    _AlaQoSPortDefaultQueues_Type()
)
alaQoSPortDefaultQueues.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDefaultQueues.setStatus("current")


class _AlaQoSPortAppliedDefaultQueues_Type(Integer32):
    """Custom type alaQoSPortAppliedDefaultQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
    )


_AlaQoSPortAppliedDefaultQueues_Type.__name__ = "Integer32"
_AlaQoSPortAppliedDefaultQueues_Object = MibTableColumn
alaQoSPortAppliedDefaultQueues = _AlaQoSPortAppliedDefaultQueues_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 18),
    _AlaQoSPortAppliedDefaultQueues_Type()
)
alaQoSPortAppliedDefaultQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedDefaultQueues.setStatus("current")


class _AlaQoSPortMaximumDefaultBandwidth_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumDefaultBandwidth_Object = MibTableColumn
alaQoSPortMaximumDefaultBandwidth = _AlaQoSPortMaximumDefaultBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 19),
    _AlaQoSPortMaximumDefaultBandwidth_Type()
)
alaQoSPortMaximumDefaultBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultBandwidth.setStatus("current")


class _AlaQoSPortMaximumDefaultBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultBandwidthStatus based on Integer32"""
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


_AlaQoSPortMaximumDefaultBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumDefaultBandwidthStatus_Object = MibTableColumn
alaQoSPortMaximumDefaultBandwidthStatus = _AlaQoSPortMaximumDefaultBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 20),
    _AlaQoSPortMaximumDefaultBandwidthStatus_Type()
)
alaQoSPortMaximumDefaultBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultBandwidthStatus.setStatus("current")
_AlaQoSPortAppliedMaximumDefaultBandwidth_Type = Integer32
_AlaQoSPortAppliedMaximumDefaultBandwidth_Object = MibTableColumn
alaQoSPortAppliedMaximumDefaultBandwidth = _AlaQoSPortAppliedMaximumDefaultBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 21),
    _AlaQoSPortAppliedMaximumDefaultBandwidth_Type()
)
alaQoSPortAppliedMaximumDefaultBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumDefaultBandwidth.setStatus("current")


class _AlaQoSPortAppliedMaximumDefaultBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortAppliedMaximumDefaultBandwidthStatus based on Integer32"""
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


_AlaQoSPortAppliedMaximumDefaultBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortAppliedMaximumDefaultBandwidthStatus_Object = MibTableColumn
alaQoSPortAppliedMaximumDefaultBandwidthStatus = _AlaQoSPortAppliedMaximumDefaultBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 22),
    _AlaQoSPortAppliedMaximumDefaultBandwidthStatus_Type()
)
alaQoSPortAppliedMaximumDefaultBandwidthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumDefaultBandwidthStatus.setStatus("current")


class _AlaQoSPortMaximumDefaultDepth_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultDepth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumDefaultDepth_Object = MibTableColumn
alaQoSPortMaximumDefaultDepth = _AlaQoSPortMaximumDefaultDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 23),
    _AlaQoSPortMaximumDefaultDepth_Type()
)
alaQoSPortMaximumDefaultDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultDepth.setStatus("current")


class _AlaQoSPortMaximumDefaultDepthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultDepthStatus based on Integer32"""
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


_AlaQoSPortMaximumDefaultDepthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumDefaultDepthStatus_Object = MibTableColumn
alaQoSPortMaximumDefaultDepthStatus = _AlaQoSPortMaximumDefaultDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 24),
    _AlaQoSPortMaximumDefaultDepthStatus_Type()
)
alaQoSPortMaximumDefaultDepthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultDepthStatus.setStatus("current")
_AlaQoSPortAppliedMaximumDefaultDepth_Type = Integer32
_AlaQoSPortAppliedMaximumDefaultDepth_Object = MibTableColumn
alaQoSPortAppliedMaximumDefaultDepth = _AlaQoSPortAppliedMaximumDefaultDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 25),
    _AlaQoSPortAppliedMaximumDefaultDepth_Type()
)
alaQoSPortAppliedMaximumDefaultDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumDefaultDepth.setStatus("current")


class _AlaQoSPortAppliedMaximumDefaultDepthStatus_Type(Integer32):
    """Custom type alaQoSPortAppliedMaximumDefaultDepthStatus based on Integer32"""
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


_AlaQoSPortAppliedMaximumDefaultDepthStatus_Type.__name__ = "Integer32"
_AlaQoSPortAppliedMaximumDefaultDepthStatus_Object = MibTableColumn
alaQoSPortAppliedMaximumDefaultDepthStatus = _AlaQoSPortAppliedMaximumDefaultDepthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 26),
    _AlaQoSPortAppliedMaximumDefaultDepthStatus_Type()
)
alaQoSPortAppliedMaximumDefaultDepthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumDefaultDepthStatus.setStatus("current")


class _AlaQoSPortMaximumDefaultBuffers_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultBuffers based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumDefaultBuffers_Object = MibTableColumn
alaQoSPortMaximumDefaultBuffers = _AlaQoSPortMaximumDefaultBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 27),
    _AlaQoSPortMaximumDefaultBuffers_Type()
)
alaQoSPortMaximumDefaultBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultBuffers.setStatus("current")


class _AlaQoSPortMaximumDefaultBuffersStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumDefaultBuffersStatus based on Integer32"""
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


_AlaQoSPortMaximumDefaultBuffersStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumDefaultBuffersStatus_Object = MibTableColumn
alaQoSPortMaximumDefaultBuffersStatus = _AlaQoSPortMaximumDefaultBuffersStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 28),
    _AlaQoSPortMaximumDefaultBuffersStatus_Type()
)
alaQoSPortMaximumDefaultBuffersStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumDefaultBuffersStatus.setStatus("current")
_AlaQoSPortAppliedMaximumDefaultBuffers_Type = Integer32
_AlaQoSPortAppliedMaximumDefaultBuffers_Object = MibTableColumn
alaQoSPortAppliedMaximumDefaultBuffers = _AlaQoSPortAppliedMaximumDefaultBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 29),
    _AlaQoSPortAppliedMaximumDefaultBuffers_Type()
)
alaQoSPortAppliedMaximumDefaultBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumDefaultBuffers.setStatus("current")


class _AlaQoSPortAppliedMaximumDefaultBuffersStatus_Type(Integer32):
    """Custom type alaQoSPortAppliedMaximumDefaultBuffersStatus based on Integer32"""
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


_AlaQoSPortAppliedMaximumDefaultBuffersStatus_Type.__name__ = "Integer32"
_AlaQoSPortAppliedMaximumDefaultBuffersStatus_Object = MibTableColumn
alaQoSPortAppliedMaximumDefaultBuffersStatus = _AlaQoSPortAppliedMaximumDefaultBuffersStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 30),
    _AlaQoSPortAppliedMaximumDefaultBuffersStatus_Type()
)
alaQoSPortAppliedMaximumDefaultBuffersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortAppliedMaximumDefaultBuffersStatus.setStatus("current")


class _AlaQoSPortReset_Type(Integer32):
    """Custom type alaQoSPortReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSPortReset_Type.__name__ = "Integer32"
_AlaQoSPortReset_Object = MibTableColumn
alaQoSPortReset = _AlaQoSPortReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 31),
    _AlaQoSPortReset_Type()
)
alaQoSPortReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortReset.setStatus("current")
_AlaQoSPortPhysicalBandwidth_Type = Integer32
_AlaQoSPortPhysicalBandwidth_Object = MibTableColumn
alaQoSPortPhysicalBandwidth = _AlaQoSPortPhysicalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 32),
    _AlaQoSPortPhysicalBandwidth_Type()
)
alaQoSPortPhysicalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPhysicalBandwidth.setStatus("current")
_AlaQoSPortReservedBandwidth_Type = Integer32
_AlaQoSPortReservedBandwidth_Object = MibTableColumn
alaQoSPortReservedBandwidth = _AlaQoSPortReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 33),
    _AlaQoSPortReservedBandwidth_Type()
)
alaQoSPortReservedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortReservedBandwidth.setStatus("current")
_AlaQoSPortSignalledBandwidth_Type = Integer32
_AlaQoSPortSignalledBandwidth_Object = MibTableColumn
alaQoSPortSignalledBandwidth = _AlaQoSPortSignalledBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 34),
    _AlaQoSPortSignalledBandwidth_Type()
)
alaQoSPortSignalledBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortSignalledBandwidth.setStatus("current")
_AlaQoSPortCurrentBandwidth_Type = Integer32
_AlaQoSPortCurrentBandwidth_Object = MibTableColumn
alaQoSPortCurrentBandwidth = _AlaQoSPortCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 35),
    _AlaQoSPortCurrentBandwidth_Type()
)
alaQoSPortCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortCurrentBandwidth.setStatus("current")
_AlaQoSPortDefaultQidLow_Type = Integer32
_AlaQoSPortDefaultQidLow_Object = MibTableColumn
alaQoSPortDefaultQidLow = _AlaQoSPortDefaultQidLow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 36),
    _AlaQoSPortDefaultQidLow_Type()
)
alaQoSPortDefaultQidLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortDefaultQidLow.setStatus("current")
_AlaQoSPortDefaultQidMedium_Type = Integer32
_AlaQoSPortDefaultQidMedium_Object = MibTableColumn
alaQoSPortDefaultQidMedium = _AlaQoSPortDefaultQidMedium_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 37),
    _AlaQoSPortDefaultQidMedium_Type()
)
alaQoSPortDefaultQidMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortDefaultQidMedium.setStatus("current")
_AlaQoSPortDefaultQidHigh_Type = Integer32
_AlaQoSPortDefaultQidHigh_Object = MibTableColumn
alaQoSPortDefaultQidHigh = _AlaQoSPortDefaultQidHigh_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 38),
    _AlaQoSPortDefaultQidHigh_Type()
)
alaQoSPortDefaultQidHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortDefaultQidHigh.setStatus("current")
_AlaQoSPortDefaultQidUrgent_Type = Integer32
_AlaQoSPortDefaultQidUrgent_Object = MibTableColumn
alaQoSPortDefaultQidUrgent = _AlaQoSPortDefaultQidUrgent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 39),
    _AlaQoSPortDefaultQidUrgent_Type()
)
alaQoSPortDefaultQidUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortDefaultQidUrgent.setStatus("current")
_AlaQoSPortFloodQid_Type = Integer32
_AlaQoSPortFloodQid_Object = MibTableColumn
alaQoSPortFloodQid = _AlaQoSPortFloodQid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 40),
    _AlaQoSPortFloodQid_Type()
)
alaQoSPortFloodQid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFloodQid.setStatus("current")
_AlaQoSPortQueues_Type = Integer32
_AlaQoSPortQueues_Object = MibTableColumn
alaQoSPortQueues = _AlaQoSPortQueues_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 41),
    _AlaQoSPortQueues_Type()
)
alaQoSPortQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortQueues.setStatus("current")
_AlaQoSPortQueuesCreated_Type = Integer32
_AlaQoSPortQueuesCreated_Object = MibTableColumn
alaQoSPortQueuesCreated = _AlaQoSPortQueuesCreated_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 42),
    _AlaQoSPortQueuesCreated_Type()
)
alaQoSPortQueuesCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortQueuesCreated.setStatus("current")
_AlaQoSPortQueuesFailed_Type = Integer32
_AlaQoSPortQueuesFailed_Object = MibTableColumn
alaQoSPortQueuesFailed = _AlaQoSPortQueuesFailed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 43),
    _AlaQoSPortQueuesFailed_Type()
)
alaQoSPortQueuesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortQueuesFailed.setStatus("current")
_AlaQoSPortQueuesPreempted_Type = Integer32
_AlaQoSPortQueuesPreempted_Object = MibTableColumn
alaQoSPortQueuesPreempted = _AlaQoSPortQueuesPreempted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 44),
    _AlaQoSPortQueuesPreempted_Type()
)
alaQoSPortQueuesPreempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortQueuesPreempted.setStatus("current")
_AlaQoSPortRowStatus_Type = RowStatus
_AlaQoSPortRowStatus_Object = MibTableColumn
alaQoSPortRowStatus = _AlaQoSPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 45),
    _AlaQoSPortRowStatus_Type()
)
alaQoSPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortRowStatus.setStatus("current")
_AlaQoSPortFirPrio0EnqBytes_Type = Counter64
_AlaQoSPortFirPrio0EnqBytes_Object = MibTableColumn
alaQoSPortFirPrio0EnqBytes = _AlaQoSPortFirPrio0EnqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 46),
    _AlaQoSPortFirPrio0EnqBytes_Type()
)
alaQoSPortFirPrio0EnqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio0EnqBytes.setStatus("current")
_AlaQoSPortFirPrio0DeqBytes_Type = Counter64
_AlaQoSPortFirPrio0DeqBytes_Object = MibTableColumn
alaQoSPortFirPrio0DeqBytes = _AlaQoSPortFirPrio0DeqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 47),
    _AlaQoSPortFirPrio0DeqBytes_Type()
)
alaQoSPortFirPrio0DeqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio0DeqBytes.setStatus("current")
_AlaQoSPortFirPrio0EnqPkts_Type = Counter64
_AlaQoSPortFirPrio0EnqPkts_Object = MibTableColumn
alaQoSPortFirPrio0EnqPkts = _AlaQoSPortFirPrio0EnqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 48),
    _AlaQoSPortFirPrio0EnqPkts_Type()
)
alaQoSPortFirPrio0EnqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio0EnqPkts.setStatus("current")
_AlaQoSPortFirPrio0DeqPkts_Type = Counter64
_AlaQoSPortFirPrio0DeqPkts_Object = MibTableColumn
alaQoSPortFirPrio0DeqPkts = _AlaQoSPortFirPrio0DeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 49),
    _AlaQoSPortFirPrio0DeqPkts_Type()
)
alaQoSPortFirPrio0DeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio0DeqPkts.setStatus("current")
_AlaQoSPortFirPrio0QidDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio0QidDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio0QidDiscardPkts = _AlaQoSPortFirPrio0QidDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 50),
    _AlaQoSPortFirPrio0QidDiscardPkts_Type()
)
alaQoSPortFirPrio0QidDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio0QidDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio0WredDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio0WredDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio0WredDiscardPkts = _AlaQoSPortFirPrio0WredDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 51),
    _AlaQoSPortFirPrio0WredDiscardPkts_Type()
)
alaQoSPortFirPrio0WredDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio0WredDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio0OverflowDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio0OverflowDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio0OverflowDiscardPkts = _AlaQoSPortFirPrio0OverflowDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 52),
    _AlaQoSPortFirPrio0OverflowDiscardPkts_Type()
)
alaQoSPortFirPrio0OverflowDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio0OverflowDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio1EnqBytes_Type = Counter64
_AlaQoSPortFirPrio1EnqBytes_Object = MibTableColumn
alaQoSPortFirPrio1EnqBytes = _AlaQoSPortFirPrio1EnqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 53),
    _AlaQoSPortFirPrio1EnqBytes_Type()
)
alaQoSPortFirPrio1EnqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio1EnqBytes.setStatus("current")
_AlaQoSPortFirPrio1DeqBytes_Type = Counter64
_AlaQoSPortFirPrio1DeqBytes_Object = MibTableColumn
alaQoSPortFirPrio1DeqBytes = _AlaQoSPortFirPrio1DeqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 54),
    _AlaQoSPortFirPrio1DeqBytes_Type()
)
alaQoSPortFirPrio1DeqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio1DeqBytes.setStatus("current")
_AlaQoSPortFirPrio1EnqPkts_Type = Counter64
_AlaQoSPortFirPrio1EnqPkts_Object = MibTableColumn
alaQoSPortFirPrio1EnqPkts = _AlaQoSPortFirPrio1EnqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 55),
    _AlaQoSPortFirPrio1EnqPkts_Type()
)
alaQoSPortFirPrio1EnqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio1EnqPkts.setStatus("current")
_AlaQoSPortFirPrio1DeqPkts_Type = Counter64
_AlaQoSPortFirPrio1DeqPkts_Object = MibTableColumn
alaQoSPortFirPrio1DeqPkts = _AlaQoSPortFirPrio1DeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 56),
    _AlaQoSPortFirPrio1DeqPkts_Type()
)
alaQoSPortFirPrio1DeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio1DeqPkts.setStatus("current")
_AlaQoSPortFirPrio1QidDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio1QidDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio1QidDiscardPkts = _AlaQoSPortFirPrio1QidDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 57),
    _AlaQoSPortFirPrio1QidDiscardPkts_Type()
)
alaQoSPortFirPrio1QidDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio1QidDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio1WredDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio1WredDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio1WredDiscardPkts = _AlaQoSPortFirPrio1WredDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 58),
    _AlaQoSPortFirPrio1WredDiscardPkts_Type()
)
alaQoSPortFirPrio1WredDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio1WredDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio1OverflowDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio1OverflowDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio1OverflowDiscardPkts = _AlaQoSPortFirPrio1OverflowDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 59),
    _AlaQoSPortFirPrio1OverflowDiscardPkts_Type()
)
alaQoSPortFirPrio1OverflowDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio1OverflowDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio2EnqBytes_Type = Counter64
_AlaQoSPortFirPrio2EnqBytes_Object = MibTableColumn
alaQoSPortFirPrio2EnqBytes = _AlaQoSPortFirPrio2EnqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 60),
    _AlaQoSPortFirPrio2EnqBytes_Type()
)
alaQoSPortFirPrio2EnqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio2EnqBytes.setStatus("current")
_AlaQoSPortFirPrio2DeqBytes_Type = Counter64
_AlaQoSPortFirPrio2DeqBytes_Object = MibTableColumn
alaQoSPortFirPrio2DeqBytes = _AlaQoSPortFirPrio2DeqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 61),
    _AlaQoSPortFirPrio2DeqBytes_Type()
)
alaQoSPortFirPrio2DeqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio2DeqBytes.setStatus("current")
_AlaQoSPortFirPrio2EnqPkts_Type = Counter64
_AlaQoSPortFirPrio2EnqPkts_Object = MibTableColumn
alaQoSPortFirPrio2EnqPkts = _AlaQoSPortFirPrio2EnqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 62),
    _AlaQoSPortFirPrio2EnqPkts_Type()
)
alaQoSPortFirPrio2EnqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio2EnqPkts.setStatus("current")
_AlaQoSPortFirPrio2DeqPkts_Type = Counter64
_AlaQoSPortFirPrio2DeqPkts_Object = MibTableColumn
alaQoSPortFirPrio2DeqPkts = _AlaQoSPortFirPrio2DeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 63),
    _AlaQoSPortFirPrio2DeqPkts_Type()
)
alaQoSPortFirPrio2DeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio2DeqPkts.setStatus("current")
_AlaQoSPortFirPrio2QidDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio2QidDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio2QidDiscardPkts = _AlaQoSPortFirPrio2QidDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 64),
    _AlaQoSPortFirPrio2QidDiscardPkts_Type()
)
alaQoSPortFirPrio2QidDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio2QidDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio2WredDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio2WredDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio2WredDiscardPkts = _AlaQoSPortFirPrio2WredDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 65),
    _AlaQoSPortFirPrio2WredDiscardPkts_Type()
)
alaQoSPortFirPrio2WredDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio2WredDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio2OverflowDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio2OverflowDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio2OverflowDiscardPkts = _AlaQoSPortFirPrio2OverflowDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 66),
    _AlaQoSPortFirPrio2OverflowDiscardPkts_Type()
)
alaQoSPortFirPrio2OverflowDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio2OverflowDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio3EnqBytes_Type = Counter64
_AlaQoSPortFirPrio3EnqBytes_Object = MibTableColumn
alaQoSPortFirPrio3EnqBytes = _AlaQoSPortFirPrio3EnqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 67),
    _AlaQoSPortFirPrio3EnqBytes_Type()
)
alaQoSPortFirPrio3EnqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio3EnqBytes.setStatus("current")
_AlaQoSPortFirPrio3DeqBytes_Type = Counter64
_AlaQoSPortFirPrio3DeqBytes_Object = MibTableColumn
alaQoSPortFirPrio3DeqBytes = _AlaQoSPortFirPrio3DeqBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 68),
    _AlaQoSPortFirPrio3DeqBytes_Type()
)
alaQoSPortFirPrio3DeqBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio3DeqBytes.setStatus("current")
_AlaQoSPortFirPrio3EnqPkts_Type = Counter64
_AlaQoSPortFirPrio3EnqPkts_Object = MibTableColumn
alaQoSPortFirPrio3EnqPkts = _AlaQoSPortFirPrio3EnqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 69),
    _AlaQoSPortFirPrio3EnqPkts_Type()
)
alaQoSPortFirPrio3EnqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio3EnqPkts.setStatus("current")
_AlaQoSPortFirPrio3DeqPkts_Type = Counter64
_AlaQoSPortFirPrio3DeqPkts_Object = MibTableColumn
alaQoSPortFirPrio3DeqPkts = _AlaQoSPortFirPrio3DeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 70),
    _AlaQoSPortFirPrio3DeqPkts_Type()
)
alaQoSPortFirPrio3DeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio3DeqPkts.setStatus("current")
_AlaQoSPortFirPrio3QidDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio3QidDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio3QidDiscardPkts = _AlaQoSPortFirPrio3QidDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 71),
    _AlaQoSPortFirPrio3QidDiscardPkts_Type()
)
alaQoSPortFirPrio3QidDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio3QidDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio3WredDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio3WredDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio3WredDiscardPkts = _AlaQoSPortFirPrio3WredDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 72),
    _AlaQoSPortFirPrio3WredDiscardPkts_Type()
)
alaQoSPortFirPrio3WredDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio3WredDiscardPkts.setStatus("current")
_AlaQoSPortFirPrio3OverflowDiscardPkts_Type = Counter64
_AlaQoSPortFirPrio3OverflowDiscardPkts_Object = MibTableColumn
alaQoSPortFirPrio3OverflowDiscardPkts = _AlaQoSPortFirPrio3OverflowDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 73),
    _AlaQoSPortFirPrio3OverflowDiscardPkts_Type()
)
alaQoSPortFirPrio3OverflowDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFirPrio3OverflowDiscardPkts.setStatus("current")


class _AlaQoSPortDefaultClassification_Type(Integer32):
    """Custom type alaQoSPortDefaultClassification based on Integer32"""
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
        *(("b8021p", 1),
          ("dscp", 3),
          ("tos", 2))
    )


_AlaQoSPortDefaultClassification_Type.__name__ = "Integer32"
_AlaQoSPortDefaultClassification_Object = MibTableColumn
alaQoSPortDefaultClassification = _AlaQoSPortDefaultClassification_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 74),
    _AlaQoSPortDefaultClassification_Type()
)
alaQoSPortDefaultClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDefaultClassification.setStatus("current")


class _AlaQoSPortLowPriorityWeight_Type(Integer32):
    """Custom type alaQoSPortLowPriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortLowPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortLowPriorityWeight_Object = MibTableColumn
alaQoSPortLowPriorityWeight = _AlaQoSPortLowPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 75),
    _AlaQoSPortLowPriorityWeight_Type()
)
alaQoSPortLowPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortLowPriorityWeight.setStatus("current")


class _AlaQoSPortMediumPriorityWeight_Type(Integer32):
    """Custom type alaQoSPortMediumPriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortMediumPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortMediumPriorityWeight_Object = MibTableColumn
alaQoSPortMediumPriorityWeight = _AlaQoSPortMediumPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 76),
    _AlaQoSPortMediumPriorityWeight_Type()
)
alaQoSPortMediumPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMediumPriorityWeight.setStatus("current")


class _AlaQoSPortHighPriorityWeight_Type(Integer32):
    """Custom type alaQoSPortHighPriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortHighPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortHighPriorityWeight_Object = MibTableColumn
alaQoSPortHighPriorityWeight = _AlaQoSPortHighPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 77),
    _AlaQoSPortHighPriorityWeight_Type()
)
alaQoSPortHighPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortHighPriorityWeight.setStatus("current")


class _AlaQoSPortUrgentPriorityWeight_Type(Integer32):
    """Custom type alaQoSPortUrgentPriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortUrgentPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortUrgentPriorityWeight_Object = MibTableColumn
alaQoSPortUrgentPriorityWeight = _AlaQoSPortUrgentPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 78),
    _AlaQoSPortUrgentPriorityWeight_Type()
)
alaQoSPortUrgentPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortUrgentPriorityWeight.setStatus("current")


class _AlaQoSPortMaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortMaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumBandwidth_Object = MibTableColumn
alaQoSPortMaximumBandwidth = _AlaQoSPortMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 79),
    _AlaQoSPortMaximumBandwidth_Type()
)
alaQoSPortMaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumBandwidth.setStatus("current")


class _AlaQoSPortMaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortMaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortMaximumBandwidthStatus = _AlaQoSPortMaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 80),
    _AlaQoSPortMaximumBandwidthStatus_Type()
)
alaQoSPortMaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP0Lower_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP0Lower based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP0Lower_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP0Lower_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP0Lower = _AlaQoSPortEnqueuingThresholdP0Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 81),
    _AlaQoSPortEnqueuingThresholdP0Lower_Type()
)
alaQoSPortEnqueuingThresholdP0Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP0Lower.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP0Upper_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP0Upper based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP0Upper_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP0Upper_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP0Upper = _AlaQoSPortEnqueuingThresholdP0Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 82),
    _AlaQoSPortEnqueuingThresholdP0Upper_Type()
)
alaQoSPortEnqueuingThresholdP0Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP0Upper.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP1Lower_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP1Lower based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP1Lower_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP1Lower_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP1Lower = _AlaQoSPortEnqueuingThresholdP1Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 83),
    _AlaQoSPortEnqueuingThresholdP1Lower_Type()
)
alaQoSPortEnqueuingThresholdP1Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP1Lower.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP1Upper_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP1Upper based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP1Upper_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP1Upper_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP1Upper = _AlaQoSPortEnqueuingThresholdP1Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 84),
    _AlaQoSPortEnqueuingThresholdP1Upper_Type()
)
alaQoSPortEnqueuingThresholdP1Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP1Upper.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP2Lower_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP2Lower based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP2Lower_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP2Lower_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP2Lower = _AlaQoSPortEnqueuingThresholdP2Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 85),
    _AlaQoSPortEnqueuingThresholdP2Lower_Type()
)
alaQoSPortEnqueuingThresholdP2Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP2Lower.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP2Upper_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP2Upper based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP2Upper_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP2Upper_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP2Upper = _AlaQoSPortEnqueuingThresholdP2Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 86),
    _AlaQoSPortEnqueuingThresholdP2Upper_Type()
)
alaQoSPortEnqueuingThresholdP2Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP2Upper.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP3Lower_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP3Lower based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP3Lower_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP3Lower_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP3Lower = _AlaQoSPortEnqueuingThresholdP3Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 87),
    _AlaQoSPortEnqueuingThresholdP3Lower_Type()
)
alaQoSPortEnqueuingThresholdP3Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP3Lower.setStatus("current")


class _AlaQoSPortEnqueuingThresholdP3Upper_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdP3Upper based on Integer32"""
    defaultValue = 575

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSPortEnqueuingThresholdP3Upper_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdP3Upper_Object = MibTableColumn
alaQoSPortEnqueuingThresholdP3Upper = _AlaQoSPortEnqueuingThresholdP3Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 88),
    _AlaQoSPortEnqueuingThresholdP3Upper_Type()
)
alaQoSPortEnqueuingThresholdP3Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdP3Upper.setStatus("current")


class _AlaQoSPortEnqueuingThresholdStatus_Type(Integer32):
    """Custom type alaQoSPortEnqueuingThresholdStatus based on Integer32"""
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


_AlaQoSPortEnqueuingThresholdStatus_Type.__name__ = "Integer32"
_AlaQoSPortEnqueuingThresholdStatus_Object = MibTableColumn
alaQoSPortEnqueuingThresholdStatus = _AlaQoSPortEnqueuingThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 89),
    _AlaQoSPortEnqueuingThresholdStatus_Type()
)
alaQoSPortEnqueuingThresholdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortEnqueuingThresholdStatus.setStatus("current")


class _AlaQoSPortHighDensity_Type(Integer32):
    """Custom type alaQoSPortHighDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSPortHighDensity_Type.__name__ = "Integer32"
_AlaQoSPortHighDensity_Object = MibTableColumn
alaQoSPortHighDensity = _AlaQoSPortHighDensity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 90),
    _AlaQoSPortHighDensity_Type()
)
alaQoSPortHighDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortHighDensity.setStatus("current")


class _AlaQoSPortServicingMode_Type(Integer32):
    """Custom type alaQoSPortServicingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("drr", 4),
          ("prioritywrr", 2),
          ("strictpriority", 1),
          ("wrr", 3))
    )


_AlaQoSPortServicingMode_Type.__name__ = "Integer32"
_AlaQoSPortServicingMode_Object = MibTableColumn
alaQoSPortServicingMode = _AlaQoSPortServicingMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 91),
    _AlaQoSPortServicingMode_Type()
)
alaQoSPortServicingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortServicingMode.setStatus("current")
_AlaQoSPortFreeFFPRules_Type = Integer32
_AlaQoSPortFreeFFPRules_Object = MibTableColumn
alaQoSPortFreeFFPRules = _AlaQoSPortFreeFFPRules_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 92),
    _AlaQoSPortFreeFFPRules_Type()
)
alaQoSPortFreeFFPRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFreeFFPRules.setStatus("current")
_AlaQoSPortUsedFFPRules_Type = Integer32
_AlaQoSPortUsedFFPRules_Object = MibTableColumn
alaQoSPortUsedFFPRules = _AlaQoSPortUsedFFPRules_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 93),
    _AlaQoSPortUsedFFPRules_Type()
)
alaQoSPortUsedFFPRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortUsedFFPRules.setStatus("current")
_AlaQoSPortFreeFFPMasks_Type = Integer32
_AlaQoSPortFreeFFPMasks_Object = MibTableColumn
alaQoSPortFreeFFPMasks = _AlaQoSPortFreeFFPMasks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 94),
    _AlaQoSPortFreeFFPMasks_Type()
)
alaQoSPortFreeFFPMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortFreeFFPMasks.setStatus("current")
_AlaQoSPortUsedFFPMasks_Type = Integer32
_AlaQoSPortUsedFFPMasks_Object = MibTableColumn
alaQoSPortUsedFFPMasks = _AlaQoSPortUsedFFPMasks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 95),
    _AlaQoSPortUsedFFPMasks_Type()
)
alaQoSPortUsedFFPMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortUsedFFPMasks.setStatus("current")
_AlaQoSPortSpoofedCount_Type = Integer32
_AlaQoSPortSpoofedCount_Object = MibTableColumn
alaQoSPortSpoofedCount = _AlaQoSPortSpoofedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 96),
    _AlaQoSPortSpoofedCount_Type()
)
alaQoSPortSpoofedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortSpoofedCount.setStatus("current")
_AlaQoSPortNonSpoofedCount_Type = Integer32
_AlaQoSPortNonSpoofedCount_Object = MibTableColumn
alaQoSPortNonSpoofedCount = _AlaQoSPortNonSpoofedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 97),
    _AlaQoSPortNonSpoofedCount_Type()
)
alaQoSPortNonSpoofedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortNonSpoofedCount.setStatus("current")


class _AlaQoSPortQ4PriorityWeight_Type(Integer32):
    """Custom type alaQoSPortQ4PriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortQ4PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortQ4PriorityWeight_Object = MibTableColumn
alaQoSPortQ4PriorityWeight = _AlaQoSPortQ4PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 98),
    _AlaQoSPortQ4PriorityWeight_Type()
)
alaQoSPortQ4PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortQ4PriorityWeight.setStatus("current")


class _AlaQoSPortQ5PriorityWeight_Type(Integer32):
    """Custom type alaQoSPortQ5PriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortQ5PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortQ5PriorityWeight_Object = MibTableColumn
alaQoSPortQ5PriorityWeight = _AlaQoSPortQ5PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 99),
    _AlaQoSPortQ5PriorityWeight_Type()
)
alaQoSPortQ5PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortQ5PriorityWeight.setStatus("current")


class _AlaQoSPortQ6PriorityWeight_Type(Integer32):
    """Custom type alaQoSPortQ6PriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortQ6PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortQ6PriorityWeight_Object = MibTableColumn
alaQoSPortQ6PriorityWeight = _AlaQoSPortQ6PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 100),
    _AlaQoSPortQ6PriorityWeight_Type()
)
alaQoSPortQ6PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortQ6PriorityWeight.setStatus("current")


class _AlaQoSPortQ7PriorityWeight_Type(Integer32):
    """Custom type alaQoSPortQ7PriorityWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSPortQ7PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSPortQ7PriorityWeight_Object = MibTableColumn
alaQoSPortQ7PriorityWeight = _AlaQoSPortQ7PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 101),
    _AlaQoSPortQ7PriorityWeight_Type()
)
alaQoSPortQ7PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortQ7PriorityWeight.setStatus("current")


class _AlaQoSPortCOS0MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS0MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS0MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS0MaximumBandwidth = _AlaQoSPortCOS0MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 102),
    _AlaQoSPortCOS0MaximumBandwidth_Type()
)
alaQoSPortCOS0MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS0MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS0MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS0MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS0MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS0MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS0MaximumBandwidthStatus = _AlaQoSPortCOS0MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 103),
    _AlaQoSPortCOS0MaximumBandwidthStatus_Type()
)
alaQoSPortCOS0MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS0MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS1MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS1MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS1MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS1MaximumBandwidth = _AlaQoSPortCOS1MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 104),
    _AlaQoSPortCOS1MaximumBandwidth_Type()
)
alaQoSPortCOS1MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS1MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS1MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS1MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS1MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS1MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS1MaximumBandwidthStatus = _AlaQoSPortCOS1MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 105),
    _AlaQoSPortCOS1MaximumBandwidthStatus_Type()
)
alaQoSPortCOS1MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS1MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS2MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS2MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS2MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS2MaximumBandwidth = _AlaQoSPortCOS2MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 106),
    _AlaQoSPortCOS2MaximumBandwidth_Type()
)
alaQoSPortCOS2MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS2MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS2MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS2MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS2MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS2MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS2MaximumBandwidthStatus = _AlaQoSPortCOS2MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 107),
    _AlaQoSPortCOS2MaximumBandwidthStatus_Type()
)
alaQoSPortCOS2MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS2MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS3MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS3MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS3MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS3MaximumBandwidth = _AlaQoSPortCOS3MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 108),
    _AlaQoSPortCOS3MaximumBandwidth_Type()
)
alaQoSPortCOS3MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS3MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS3MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS3MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS3MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS3MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS3MaximumBandwidthStatus = _AlaQoSPortCOS3MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 109),
    _AlaQoSPortCOS3MaximumBandwidthStatus_Type()
)
alaQoSPortCOS3MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS3MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS4MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS4MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS4MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS4MaximumBandwidth = _AlaQoSPortCOS4MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 110),
    _AlaQoSPortCOS4MaximumBandwidth_Type()
)
alaQoSPortCOS4MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS4MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS4MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS4MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS4MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS4MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS4MaximumBandwidthStatus = _AlaQoSPortCOS4MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 111),
    _AlaQoSPortCOS4MaximumBandwidthStatus_Type()
)
alaQoSPortCOS4MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS4MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS5MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS5MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS5MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS5MaximumBandwidth = _AlaQoSPortCOS5MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 112),
    _AlaQoSPortCOS5MaximumBandwidth_Type()
)
alaQoSPortCOS5MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS5MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS5MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS5MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS5MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS5MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS5MaximumBandwidthStatus = _AlaQoSPortCOS5MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 113),
    _AlaQoSPortCOS5MaximumBandwidthStatus_Type()
)
alaQoSPortCOS5MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS5MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS6MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS6MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS6MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS6MaximumBandwidth = _AlaQoSPortCOS6MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 114),
    _AlaQoSPortCOS6MaximumBandwidth_Type()
)
alaQoSPortCOS6MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS6MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS6MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS6MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS6MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS6MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS6MaximumBandwidthStatus = _AlaQoSPortCOS6MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 115),
    _AlaQoSPortCOS6MaximumBandwidthStatus_Type()
)
alaQoSPortCOS6MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS6MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS7MaximumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS7MaximumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS7MaximumBandwidth_Object = MibTableColumn
alaQoSPortCOS7MaximumBandwidth = _AlaQoSPortCOS7MaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 116),
    _AlaQoSPortCOS7MaximumBandwidth_Type()
)
alaQoSPortCOS7MaximumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS7MaximumBandwidth.setStatus("current")


class _AlaQoSPortCOS7MaximumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS7MaximumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS7MaximumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS7MaximumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS7MaximumBandwidthStatus = _AlaQoSPortCOS7MaximumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 117),
    _AlaQoSPortCOS7MaximumBandwidthStatus_Type()
)
alaQoSPortCOS7MaximumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS7MaximumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS0MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS0MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS0MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS0MinimumBandwidth = _AlaQoSPortCOS0MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 118),
    _AlaQoSPortCOS0MinimumBandwidth_Type()
)
alaQoSPortCOS0MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS0MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS0MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS0MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS0MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS0MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS0MinimumBandwidthStatus = _AlaQoSPortCOS0MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 119),
    _AlaQoSPortCOS0MinimumBandwidthStatus_Type()
)
alaQoSPortCOS0MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS0MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS1MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS1MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS1MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS1MinimumBandwidth = _AlaQoSPortCOS1MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 120),
    _AlaQoSPortCOS1MinimumBandwidth_Type()
)
alaQoSPortCOS1MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS1MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS1MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS1MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS1MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS1MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS1MinimumBandwidthStatus = _AlaQoSPortCOS1MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 121),
    _AlaQoSPortCOS1MinimumBandwidthStatus_Type()
)
alaQoSPortCOS1MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS1MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS2MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS2MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS2MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS2MinimumBandwidth = _AlaQoSPortCOS2MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 122),
    _AlaQoSPortCOS2MinimumBandwidth_Type()
)
alaQoSPortCOS2MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS2MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS2MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS2MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS2MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS2MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS2MinimumBandwidthStatus = _AlaQoSPortCOS2MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 123),
    _AlaQoSPortCOS2MinimumBandwidthStatus_Type()
)
alaQoSPortCOS2MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS2MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS3MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS3MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS3MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS3MinimumBandwidth = _AlaQoSPortCOS3MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 124),
    _AlaQoSPortCOS3MinimumBandwidth_Type()
)
alaQoSPortCOS3MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS3MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS3MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS3MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS3MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS3MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS3MinimumBandwidthStatus = _AlaQoSPortCOS3MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 125),
    _AlaQoSPortCOS3MinimumBandwidthStatus_Type()
)
alaQoSPortCOS3MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS3MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS4MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS4MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS4MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS4MinimumBandwidth = _AlaQoSPortCOS4MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 126),
    _AlaQoSPortCOS4MinimumBandwidth_Type()
)
alaQoSPortCOS4MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS4MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS4MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS4MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS4MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS4MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS4MinimumBandwidthStatus = _AlaQoSPortCOS4MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 127),
    _AlaQoSPortCOS4MinimumBandwidthStatus_Type()
)
alaQoSPortCOS4MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS4MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS5MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS5MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS5MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS5MinimumBandwidth = _AlaQoSPortCOS5MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 128),
    _AlaQoSPortCOS5MinimumBandwidth_Type()
)
alaQoSPortCOS5MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS5MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS5MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS5MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS5MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS5MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS5MinimumBandwidthStatus = _AlaQoSPortCOS5MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 129),
    _AlaQoSPortCOS5MinimumBandwidthStatus_Type()
)
alaQoSPortCOS5MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS5MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS6MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS6MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS6MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS6MinimumBandwidth = _AlaQoSPortCOS6MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 130),
    _AlaQoSPortCOS6MinimumBandwidth_Type()
)
alaQoSPortCOS6MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS6MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS6MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS6MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS6MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS6MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS6MinimumBandwidthStatus = _AlaQoSPortCOS6MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 131),
    _AlaQoSPortCOS6MinimumBandwidthStatus_Type()
)
alaQoSPortCOS6MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS6MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortCOS7MinimumBandwidth_Type(Integer32):
    """Custom type alaQoSPortCOS7MinimumBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortCOS7MinimumBandwidth_Object = MibTableColumn
alaQoSPortCOS7MinimumBandwidth = _AlaQoSPortCOS7MinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 132),
    _AlaQoSPortCOS7MinimumBandwidth_Type()
)
alaQoSPortCOS7MinimumBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS7MinimumBandwidth.setStatus("current")


class _AlaQoSPortCOS7MinimumBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortCOS7MinimumBandwidthStatus based on Integer32"""
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


_AlaQoSPortCOS7MinimumBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortCOS7MinimumBandwidthStatus_Object = MibTableColumn
alaQoSPortCOS7MinimumBandwidthStatus = _AlaQoSPortCOS7MinimumBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 133),
    _AlaQoSPortCOS7MinimumBandwidthStatus_Type()
)
alaQoSPortCOS7MinimumBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortCOS7MinimumBandwidthStatus.setStatus("current")


class _AlaQoSPortMaximumIngBandwidth_Type(Integer32):
    """Custom type alaQoSPortMaximumIngBandwidth based on Integer32"""
    defaultValue = 0


_AlaQoSPortMaximumIngBandwidth_Object = MibTableColumn
alaQoSPortMaximumIngBandwidth = _AlaQoSPortMaximumIngBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 134),
    _AlaQoSPortMaximumIngBandwidth_Type()
)
alaQoSPortMaximumIngBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumIngBandwidth.setStatus("current")


class _AlaQoSPortMaximumIngBandwidthStatus_Type(Integer32):
    """Custom type alaQoSPortMaximumIngBandwidthStatus based on Integer32"""
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


_AlaQoSPortMaximumIngBandwidthStatus_Type.__name__ = "Integer32"
_AlaQoSPortMaximumIngBandwidthStatus_Object = MibTableColumn
alaQoSPortMaximumIngBandwidthStatus = _AlaQoSPortMaximumIngBandwidthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 135),
    _AlaQoSPortMaximumIngBandwidthStatus_Type()
)
alaQoSPortMaximumIngBandwidthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMaximumIngBandwidthStatus.setStatus("current")


class _AlaQoSPortDEIMarking_Type(Integer32):
    """Custom type alaQoSPortDEIMarking based on Integer32"""
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


_AlaQoSPortDEIMarking_Type.__name__ = "Integer32"
_AlaQoSPortDEIMarking_Object = MibTableColumn
alaQoSPortDEIMarking = _AlaQoSPortDEIMarking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 136),
    _AlaQoSPortDEIMarking_Type()
)
alaQoSPortDEIMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDEIMarking.setStatus("current")


class _AlaQoSPortMonitor_Type(Integer32):
    """Custom type alaQoSPortMonitor based on Integer32"""
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


_AlaQoSPortMonitor_Type.__name__ = "Integer32"
_AlaQoSPortMonitor_Object = MibTableColumn
alaQoSPortMonitor = _AlaQoSPortMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 137),
    _AlaQoSPortMonitor_Type()
)
alaQoSPortMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortMonitor.setStatus("current")


class _AlaQoSPortDEIMapping_Type(Integer32):
    """Custom type alaQoSPortDEIMapping based on Integer32"""
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


_AlaQoSPortDEIMapping_Type.__name__ = "Integer32"
_AlaQoSPortDEIMapping_Object = MibTableColumn
alaQoSPortDEIMapping = _AlaQoSPortDEIMapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 29, 1, 138),
    _AlaQoSPortDEIMapping_Type()
)
alaQoSPortDEIMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortDEIMapping.setStatus("current")
_AlaQoSConfig_ObjectIdentity = ObjectIdentity
alaQoSConfig = _AlaQoSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30)
)


class _AlaQoSConfigEnabled_Type(Integer32):
    """Custom type alaQoSConfigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSConfigEnabled_Type.__name__ = "Integer32"
_AlaQoSConfigEnabled_Object = MibScalar
alaQoSConfigEnabled = _AlaQoSConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 1),
    _AlaQoSConfigEnabled_Type()
)
alaQoSConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigEnabled.setStatus("current")


class _AlaQoSConfigDefaultQueues_Type(Integer32):
    """Custom type alaQoSConfigDefaultQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_AlaQoSConfigDefaultQueues_Type.__name__ = "Integer32"
_AlaQoSConfigDefaultQueues_Object = MibScalar
alaQoSConfigDefaultQueues = _AlaQoSConfigDefaultQueues_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 2),
    _AlaQoSConfigDefaultQueues_Type()
)
alaQoSConfigDefaultQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigDefaultQueues.setStatus("current")


class _AlaQoSConfigAppliedDefaultQueues_Type(Integer32):
    """Custom type alaQoSConfigAppliedDefaultQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_AlaQoSConfigAppliedDefaultQueues_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedDefaultQueues_Object = MibScalar
alaQoSConfigAppliedDefaultQueues = _AlaQoSConfigAppliedDefaultQueues_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 3),
    _AlaQoSConfigAppliedDefaultQueues_Type()
)
alaQoSConfigAppliedDefaultQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedDefaultQueues.setStatus("current")


class _AlaQoSConfigTrustPorts_Type(Integer32):
    """Custom type alaQoSConfigTrustPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigTrustPorts_Type.__name__ = "Integer32"
_AlaQoSConfigTrustPorts_Object = MibScalar
alaQoSConfigTrustPorts = _AlaQoSConfigTrustPorts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 4),
    _AlaQoSConfigTrustPorts_Type()
)
alaQoSConfigTrustPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigTrustPorts.setStatus("current")


class _AlaQoSConfigFlowTimeout_Type(Integer32):
    """Custom type alaQoSConfigFlowTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_AlaQoSConfigFlowTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigFlowTimeout_Object = MibScalar
alaQoSConfigFlowTimeout = _AlaQoSConfigFlowTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 5),
    _AlaQoSConfigFlowTimeout_Type()
)
alaQoSConfigFlowTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigFlowTimeout.setStatus("current")


class _AlaQoSConfigAppliedFlowTimeout_Type(Integer32):
    """Custom type alaQoSConfigAppliedFlowTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_AlaQoSConfigAppliedFlowTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedFlowTimeout_Object = MibScalar
alaQoSConfigAppliedFlowTimeout = _AlaQoSConfigAppliedFlowTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 6),
    _AlaQoSConfigAppliedFlowTimeout_Type()
)
alaQoSConfigAppliedFlowTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedFlowTimeout.setStatus("current")


class _AlaQoSConfigFragmentTimeout_Type(Integer32):
    """Custom type alaQoSConfigFragmentTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_AlaQoSConfigFragmentTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigFragmentTimeout_Object = MibScalar
alaQoSConfigFragmentTimeout = _AlaQoSConfigFragmentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 7),
    _AlaQoSConfigFragmentTimeout_Type()
)
alaQoSConfigFragmentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigFragmentTimeout.setStatus("current")


class _AlaQoSConfigAppliedFragmentTimeout_Type(Integer32):
    """Custom type alaQoSConfigAppliedFragmentTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_AlaQoSConfigAppliedFragmentTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedFragmentTimeout_Object = MibScalar
alaQoSConfigAppliedFragmentTimeout = _AlaQoSConfigAppliedFragmentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 8),
    _AlaQoSConfigAppliedFragmentTimeout_Type()
)
alaQoSConfigAppliedFragmentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedFragmentTimeout.setStatus("current")


class _AlaQoSConfigReflexiveTimeout_Type(Integer32):
    """Custom type alaQoSConfigReflexiveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3000),
    )


_AlaQoSConfigReflexiveTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigReflexiveTimeout_Object = MibScalar
alaQoSConfigReflexiveTimeout = _AlaQoSConfigReflexiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 9),
    _AlaQoSConfigReflexiveTimeout_Type()
)
alaQoSConfigReflexiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigReflexiveTimeout.setStatus("current")


class _AlaQoSConfigAppliedReflfexiveTimeout_Type(Integer32):
    """Custom type alaQoSConfigAppliedReflfexiveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3000),
    )


_AlaQoSConfigAppliedReflfexiveTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedReflfexiveTimeout_Object = MibScalar
alaQoSConfigAppliedReflfexiveTimeout = _AlaQoSConfigAppliedReflfexiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 10),
    _AlaQoSConfigAppliedReflfexiveTimeout_Type()
)
alaQoSConfigAppliedReflfexiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedReflfexiveTimeout.setStatus("current")


class _AlaQoSConfigNatTimeout_Type(Integer32):
    """Custom type alaQoSConfigNatTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200000),
    )


_AlaQoSConfigNatTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigNatTimeout_Object = MibScalar
alaQoSConfigNatTimeout = _AlaQoSConfigNatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 11),
    _AlaQoSConfigNatTimeout_Type()
)
alaQoSConfigNatTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigNatTimeout.setStatus("current")


class _AlaQoSConfigAppliedNatTimeout_Type(Integer32):
    """Custom type alaQoSConfigAppliedNatTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200000),
    )


_AlaQoSConfigAppliedNatTimeout_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedNatTimeout_Object = MibScalar
alaQoSConfigAppliedNatTimeout = _AlaQoSConfigAppliedNatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 12),
    _AlaQoSConfigAppliedNatTimeout_Type()
)
alaQoSConfigAppliedNatTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedNatTimeout.setStatus("current")


class _AlaQoSConfigClassifyl3Bridged_Type(Integer32):
    """Custom type alaQoSConfigClassifyl3Bridged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigClassifyl3Bridged_Type.__name__ = "Integer32"
_AlaQoSConfigClassifyl3Bridged_Object = MibScalar
alaQoSConfigClassifyl3Bridged = _AlaQoSConfigClassifyl3Bridged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 13),
    _AlaQoSConfigClassifyl3Bridged_Type()
)
alaQoSConfigClassifyl3Bridged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigClassifyl3Bridged.setStatus("current")


class _AlaQoSConfigAppliedClassifyl3Bridged_Type(Integer32):
    """Custom type alaQoSConfigAppliedClassifyl3Bridged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigAppliedClassifyl3Bridged_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedClassifyl3Bridged_Object = MibScalar
alaQoSConfigAppliedClassifyl3Bridged = _AlaQoSConfigAppliedClassifyl3Bridged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 14),
    _AlaQoSConfigAppliedClassifyl3Bridged_Type()
)
alaQoSConfigAppliedClassifyl3Bridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedClassifyl3Bridged.setStatus("current")


class _AlaQoSConfigClassifyFragments_Type(Integer32):
    """Custom type alaQoSConfigClassifyFragments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigClassifyFragments_Type.__name__ = "Integer32"
_AlaQoSConfigClassifyFragments_Object = MibScalar
alaQoSConfigClassifyFragments = _AlaQoSConfigClassifyFragments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 15),
    _AlaQoSConfigClassifyFragments_Type()
)
alaQoSConfigClassifyFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigClassifyFragments.setStatus("current")


class _AlaQoSConfigAppliedClassifyFragments_Type(Integer32):
    """Custom type alaQoSConfigAppliedClassifyFragments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigAppliedClassifyFragments_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedClassifyFragments_Object = MibScalar
alaQoSConfigAppliedClassifyFragments = _AlaQoSConfigAppliedClassifyFragments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 16),
    _AlaQoSConfigAppliedClassifyFragments_Type()
)
alaQoSConfigAppliedClassifyFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedClassifyFragments.setStatus("current")


class _AlaQoSConfigDefaultBridgedDisposition_Type(Integer32):
    """Custom type alaQoSConfigDefaultBridgedDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSConfigDefaultBridgedDisposition_Type.__name__ = "Integer32"
_AlaQoSConfigDefaultBridgedDisposition_Object = MibScalar
alaQoSConfigDefaultBridgedDisposition = _AlaQoSConfigDefaultBridgedDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 17),
    _AlaQoSConfigDefaultBridgedDisposition_Type()
)
alaQoSConfigDefaultBridgedDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigDefaultBridgedDisposition.setStatus("current")


class _AlaQoSConfigAppliedDefaultBridgedDisposition_Type(Integer32):
    """Custom type alaQoSConfigAppliedDefaultBridgedDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSConfigAppliedDefaultBridgedDisposition_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedDefaultBridgedDisposition_Object = MibScalar
alaQoSConfigAppliedDefaultBridgedDisposition = _AlaQoSConfigAppliedDefaultBridgedDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 18),
    _AlaQoSConfigAppliedDefaultBridgedDisposition_Type()
)
alaQoSConfigAppliedDefaultBridgedDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedDefaultBridgedDisposition.setStatus("current")


class _AlaQoSConfigDefaultRoutedDisposition_Type(Integer32):
    """Custom type alaQoSConfigDefaultRoutedDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSConfigDefaultRoutedDisposition_Type.__name__ = "Integer32"
_AlaQoSConfigDefaultRoutedDisposition_Object = MibScalar
alaQoSConfigDefaultRoutedDisposition = _AlaQoSConfigDefaultRoutedDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 19),
    _AlaQoSConfigDefaultRoutedDisposition_Type()
)
alaQoSConfigDefaultRoutedDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigDefaultRoutedDisposition.setStatus("current")


class _AlaQoSConfigAppliedDefaultRoutedDisposition_Type(Integer32):
    """Custom type alaQoSConfigAppliedDefaultRoutedDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSConfigAppliedDefaultRoutedDisposition_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedDefaultRoutedDisposition_Object = MibScalar
alaQoSConfigAppliedDefaultRoutedDisposition = _AlaQoSConfigAppliedDefaultRoutedDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 20),
    _AlaQoSConfigAppliedDefaultRoutedDisposition_Type()
)
alaQoSConfigAppliedDefaultRoutedDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedDefaultRoutedDisposition.setStatus("current")


class _AlaQoSConfigDefaultMulticastDisposition_Type(Integer32):
    """Custom type alaQoSConfigDefaultMulticastDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSConfigDefaultMulticastDisposition_Type.__name__ = "Integer32"
_AlaQoSConfigDefaultMulticastDisposition_Object = MibScalar
alaQoSConfigDefaultMulticastDisposition = _AlaQoSConfigDefaultMulticastDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 21),
    _AlaQoSConfigDefaultMulticastDisposition_Type()
)
alaQoSConfigDefaultMulticastDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigDefaultMulticastDisposition.setStatus("current")


class _AlaQoSConfigAppliedDefaultMulticastDisposition_Type(Integer32):
    """Custom type alaQoSConfigAppliedDefaultMulticastDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSConfigAppliedDefaultMulticastDisposition_Type.__name__ = "Integer32"
_AlaQoSConfigAppliedDefaultMulticastDisposition_Object = MibScalar
alaQoSConfigAppliedDefaultMulticastDisposition = _AlaQoSConfigAppliedDefaultMulticastDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 22),
    _AlaQoSConfigAppliedDefaultMulticastDisposition_Type()
)
alaQoSConfigAppliedDefaultMulticastDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedDefaultMulticastDisposition.setStatus("current")


class _AlaQoSConfigStatsInterval_Type(Integer32):
    """Custom type alaQoSConfigStatsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AlaQoSConfigStatsInterval_Type.__name__ = "Integer32"
_AlaQoSConfigStatsInterval_Object = MibScalar
alaQoSConfigStatsInterval = _AlaQoSConfigStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 23),
    _AlaQoSConfigStatsInterval_Type()
)
alaQoSConfigStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigStatsInterval.setStatus("current")


class _AlaQoSConfigLogLines_Type(Integer32):
    """Custom type alaQoSConfigLogLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AlaQoSConfigLogLines_Type.__name__ = "Integer32"
_AlaQoSConfigLogLines_Object = MibScalar
alaQoSConfigLogLines = _AlaQoSConfigLogLines_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 24),
    _AlaQoSConfigLogLines_Type()
)
alaQoSConfigLogLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigLogLines.setStatus("current")


class _AlaQoSConfigLogLevel_Type(Integer32):
    """Custom type alaQoSConfigLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9),
    )


_AlaQoSConfigLogLevel_Type.__name__ = "Integer32"
_AlaQoSConfigLogLevel_Object = MibScalar
alaQoSConfigLogLevel = _AlaQoSConfigLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 25),
    _AlaQoSConfigLogLevel_Type()
)
alaQoSConfigLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigLogLevel.setStatus("current")


class _AlaQoSConfigLogConsole_Type(Integer32):
    """Custom type alaQoSConfigLogConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigLogConsole_Type.__name__ = "Integer32"
_AlaQoSConfigLogConsole_Object = MibScalar
alaQoSConfigLogConsole = _AlaQoSConfigLogConsole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 26),
    _AlaQoSConfigLogConsole_Type()
)
alaQoSConfigLogConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigLogConsole.setStatus("current")


class _AlaQoSConfigForwardLog_Type(Integer32):
    """Custom type alaQoSConfigForwardLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigForwardLog_Type.__name__ = "Integer32"
_AlaQoSConfigForwardLog_Object = MibScalar
alaQoSConfigForwardLog = _AlaQoSConfigForwardLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 27),
    _AlaQoSConfigForwardLog_Type()
)
alaQoSConfigForwardLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigForwardLog.setStatus("current")


class _AlaQoSConfigClearLog_Type(Integer32):
    """Custom type alaQoSConfigClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigClearLog_Type.__name__ = "Integer32"
_AlaQoSConfigClearLog_Object = MibScalar
alaQoSConfigClearLog = _AlaQoSConfigClearLog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 28),
    _AlaQoSConfigClearLog_Type()
)
alaQoSConfigClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigClearLog.setStatus("current")


class _AlaQoSConfigApply_Type(Integer32):
    """Custom type alaQoSConfigApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigApply_Type.__name__ = "Integer32"
_AlaQoSConfigApply_Object = MibScalar
alaQoSConfigApply = _AlaQoSConfigApply_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 29),
    _AlaQoSConfigApply_Type()
)
alaQoSConfigApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigApply.setStatus("current")


class _AlaQoSConfigRevert_Type(Integer32):
    """Custom type alaQoSConfigRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigRevert_Type.__name__ = "Integer32"
_AlaQoSConfigRevert_Object = MibScalar
alaQoSConfigRevert = _AlaQoSConfigRevert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 30),
    _AlaQoSConfigRevert_Type()
)
alaQoSConfigRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigRevert.setStatus("current")


class _AlaQoSConfigReset_Type(Integer32):
    """Custom type alaQoSConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigReset_Type.__name__ = "Integer32"
_AlaQoSConfigReset_Object = MibScalar
alaQoSConfigReset = _AlaQoSConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 31),
    _AlaQoSConfigReset_Type()
)
alaQoSConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigReset.setStatus("current")


class _AlaQoSConfigStatsReset_Type(Integer32):
    """Custom type alaQoSConfigStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigStatsReset_Type.__name__ = "Integer32"
_AlaQoSConfigStatsReset_Object = MibScalar
alaQoSConfigStatsReset = _AlaQoSConfigStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 32),
    _AlaQoSConfigStatsReset_Type()
)
alaQoSConfigStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigStatsReset.setStatus("current")


class _AlaQoSConfigFlush_Type(Integer32):
    """Custom type alaQoSConfigFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigFlush_Type.__name__ = "Integer32"
_AlaQoSConfigFlush_Object = MibScalar
alaQoSConfigFlush = _AlaQoSConfigFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 33),
    _AlaQoSConfigFlush_Type()
)
alaQoSConfigFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigFlush.setStatus("current")
_AlaQoSConfigDebug_Type = Integer32
_AlaQoSConfigDebug_Object = MibScalar
alaQoSConfigDebug = _AlaQoSConfigDebug_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 34),
    _AlaQoSConfigDebug_Type()
)
alaQoSConfigDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigDebug.setStatus("current")


class _AlaQoSConfigServicingMode_Type(Integer32):
    """Custom type alaQoSConfigServicingMode based on Integer32"""
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
        *(("drr", 4),
          ("prioritywrr", 2),
          ("strictpriority", 1),
          ("wrr", 3))
    )


_AlaQoSConfigServicingMode_Type.__name__ = "Integer32"
_AlaQoSConfigServicingMode_Object = MibScalar
alaQoSConfigServicingMode = _AlaQoSConfigServicingMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 35),
    _AlaQoSConfigServicingMode_Type()
)
alaQoSConfigServicingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigServicingMode.setStatus("current")


class _AlaQoSConfigLowPriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigLowPriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigLowPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigLowPriorityWeight_Object = MibScalar
alaQoSConfigLowPriorityWeight = _AlaQoSConfigLowPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 36),
    _AlaQoSConfigLowPriorityWeight_Type()
)
alaQoSConfigLowPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigLowPriorityWeight.setStatus("current")


class _AlaQoSConfigMediumPriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigMediumPriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigMediumPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigMediumPriorityWeight_Object = MibScalar
alaQoSConfigMediumPriorityWeight = _AlaQoSConfigMediumPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 37),
    _AlaQoSConfigMediumPriorityWeight_Type()
)
alaQoSConfigMediumPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigMediumPriorityWeight.setStatus("current")


class _AlaQoSConfigHighPriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigHighPriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigHighPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigHighPriorityWeight_Object = MibScalar
alaQoSConfigHighPriorityWeight = _AlaQoSConfigHighPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 38),
    _AlaQoSConfigHighPriorityWeight_Type()
)
alaQoSConfigHighPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigHighPriorityWeight.setStatus("current")


class _AlaQoSConfigUrgentPriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigUrgentPriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigUrgentPriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigUrgentPriorityWeight_Object = MibScalar
alaQoSConfigUrgentPriorityWeight = _AlaQoSConfigUrgentPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 39),
    _AlaQoSConfigUrgentPriorityWeight_Type()
)
alaQoSConfigUrgentPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigUrgentPriorityWeight.setStatus("current")


class _AlaQoSConfigQ4PriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigQ4PriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigQ4PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigQ4PriorityWeight_Object = MibScalar
alaQoSConfigQ4PriorityWeight = _AlaQoSConfigQ4PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 40),
    _AlaQoSConfigQ4PriorityWeight_Type()
)
alaQoSConfigQ4PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigQ4PriorityWeight.setStatus("current")


class _AlaQoSConfigQ5PriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigQ5PriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigQ5PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigQ5PriorityWeight_Object = MibScalar
alaQoSConfigQ5PriorityWeight = _AlaQoSConfigQ5PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 41),
    _AlaQoSConfigQ5PriorityWeight_Type()
)
alaQoSConfigQ5PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigQ5PriorityWeight.setStatus("current")


class _AlaQoSConfigQ6PriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigQ6PriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigQ6PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigQ6PriorityWeight_Object = MibScalar
alaQoSConfigQ6PriorityWeight = _AlaQoSConfigQ6PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 42),
    _AlaQoSConfigQ6PriorityWeight_Type()
)
alaQoSConfigQ6PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigQ6PriorityWeight.setStatus("current")


class _AlaQoSConfigQ7PriorityWeight_Type(Integer32):
    """Custom type alaQoSConfigQ7PriorityWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaQoSConfigQ7PriorityWeight_Type.__name__ = "Integer32"
_AlaQoSConfigQ7PriorityWeight_Object = MibScalar
alaQoSConfigQ7PriorityWeight = _AlaQoSConfigQ7PriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 43),
    _AlaQoSConfigQ7PriorityWeight_Type()
)
alaQoSConfigQ7PriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigQ7PriorityWeight.setStatus("current")
_AlaQoSConfigUserportFilter_Type = Integer32
_AlaQoSConfigUserportFilter_Object = MibScalar
alaQoSConfigUserportFilter = _AlaQoSConfigUserportFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 44),
    _AlaQoSConfigUserportFilter_Type()
)
alaQoSConfigUserportFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigUserportFilter.setStatus("current")
_AlaQoSConfigAppliedUserportFilter_Type = Integer32
_AlaQoSConfigAppliedUserportFilter_Object = MibScalar
alaQoSConfigAppliedUserportFilter = _AlaQoSConfigAppliedUserportFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 45),
    _AlaQoSConfigAppliedUserportFilter_Type()
)
alaQoSConfigAppliedUserportFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedUserportFilter.setStatus("current")
_AlaQoSConfigUserportShutdown_Type = Integer32
_AlaQoSConfigUserportShutdown_Object = MibScalar
alaQoSConfigUserportShutdown = _AlaQoSConfigUserportShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 46),
    _AlaQoSConfigUserportShutdown_Type()
)
alaQoSConfigUserportShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigUserportShutdown.setStatus("current")
_AlaQoSConfigAppliedUserportShutdown_Type = Integer32
_AlaQoSConfigAppliedUserportShutdown_Object = MibScalar
alaQoSConfigAppliedUserportShutdown = _AlaQoSConfigAppliedUserportShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 47),
    _AlaQoSConfigAppliedUserportShutdown_Type()
)
alaQoSConfigAppliedUserportShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSConfigAppliedUserportShutdown.setStatus("current")


class _AlaQoSConfigAutoNMS_Type(Integer32):
    """Custom type alaQoSConfigAutoNMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigAutoNMS_Type.__name__ = "Integer32"
_AlaQoSConfigAutoNMS_Object = MibScalar
alaQoSConfigAutoNMS = _AlaQoSConfigAutoNMS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 48),
    _AlaQoSConfigAutoNMS_Type()
)
alaQoSConfigAutoNMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigAutoNMS.setStatus("current")


class _AlaQoSConfigAutoPhones_Type(Integer32):
    """Custom type alaQoSConfigAutoPhones based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 9),
          ("pri0", 0),
          ("pri1", 1),
          ("pri2", 2),
          ("pri3", 3),
          ("pri4", 4),
          ("pri5", 5),
          ("pri6", 6),
          ("pri7", 7),
          ("trusted", 8))
    )


_AlaQoSConfigAutoPhones_Type.__name__ = "Integer32"
_AlaQoSConfigAutoPhones_Object = MibScalar
alaQoSConfigAutoPhones = _AlaQoSConfigAutoPhones_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 49),
    _AlaQoSConfigAutoPhones_Type()
)
alaQoSConfigAutoPhones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigAutoPhones.setStatus("current")


class _AlaQoSConfigQMPage_Type(Integer32):
    """Custom type alaQoSConfigQMPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigQMPage_Type.__name__ = "Integer32"
_AlaQoSConfigQMPage_Object = MibScalar
alaQoSConfigQMPage = _AlaQoSConfigQMPage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 50),
    _AlaQoSConfigQMPage_Type()
)
alaQoSConfigQMPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigQMPage.setStatus("current")


class _AlaQoSConfigQMMACGroup_Type(DisplayString):
    """Custom type alaQoSConfigQMMACGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSConfigQMMACGroup_Type.__name__ = "DisplayString"
_AlaQoSConfigQMMACGroup_Object = MibScalar
alaQoSConfigQMMACGroup = _AlaQoSConfigQMMACGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 51),
    _AlaQoSConfigQMMACGroup_Type()
)
alaQoSConfigQMMACGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigQMMACGroup.setStatus("current")


class _AlaQoSConfigQMPath_Type(DisplayString):
    """Custom type alaQoSConfigQMPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaQoSConfigQMPath_Type.__name__ = "DisplayString"
_AlaQoSConfigQMPath_Object = MibScalar
alaQoSConfigQMPath = _AlaQoSConfigQMPath_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 52),
    _AlaQoSConfigQMPath_Type()
)
alaQoSConfigQMPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigQMPath.setStatus("current")


class _AlaQoSConfigDEIMapping_Type(Integer32):
    """Custom type alaQoSConfigDEIMapping based on Integer32"""
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


_AlaQoSConfigDEIMapping_Type.__name__ = "Integer32"
_AlaQoSConfigDEIMapping_Object = MibScalar
alaQoSConfigDEIMapping = _AlaQoSConfigDEIMapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 53),
    _AlaQoSConfigDEIMapping_Type()
)
alaQoSConfigDEIMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigDEIMapping.setStatus("current")


class _AlaQoSConfigDEIMarking_Type(Integer32):
    """Custom type alaQoSConfigDEIMarking based on Integer32"""
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


_AlaQoSConfigDEIMarking_Type.__name__ = "Integer32"
_AlaQoSConfigDEIMarking_Object = MibScalar
alaQoSConfigDEIMarking = _AlaQoSConfigDEIMarking_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 54),
    _AlaQoSConfigDEIMarking_Type()
)
alaQoSConfigDEIMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSConfigDEIMarking.setStatus("current")


class _AlaQoSConfigStatsResetEgress_Type(Integer32):
    """Custom type alaQoSConfigStatsResetEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSConfigStatsResetEgress_Type.__name__ = "Integer32"
_AlaQoSConfigStatsResetEgress_Object = MibScalar
alaQoSConfigStatsResetEgress = _AlaQoSConfigStatsResetEgress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 30, 55),
    _AlaQoSConfigStatsResetEgress_Type()
)
alaQoSConfigStatsResetEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSConfigStatsResetEgress.setStatus("current")
_AlaQoSStats_ObjectIdentity = ObjectIdentity
alaQoSStats = _AlaQoSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31)
)
_AlaQoSStatsL2Events_Type = Counter32
_AlaQoSStatsL2Events_Object = MibScalar
alaQoSStatsL2Events = _AlaQoSStatsL2Events_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 1),
    _AlaQoSStatsL2Events_Type()
)
alaQoSStatsL2Events.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL2Events.setStatus("current")
_AlaQoSStatsL2Matches_Type = Counter32
_AlaQoSStatsL2Matches_Object = MibScalar
alaQoSStatsL2Matches = _AlaQoSStatsL2Matches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 2),
    _AlaQoSStatsL2Matches_Type()
)
alaQoSStatsL2Matches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL2Matches.setStatus("current")
_AlaQoSStatsL2Drops_Type = Counter32
_AlaQoSStatsL2Drops_Object = MibScalar
alaQoSStatsL2Drops = _AlaQoSStatsL2Drops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 3),
    _AlaQoSStatsL2Drops_Type()
)
alaQoSStatsL2Drops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL2Drops.setStatus("current")
_AlaQoSStatsL3IngressEvents_Type = Counter32
_AlaQoSStatsL3IngressEvents_Object = MibScalar
alaQoSStatsL3IngressEvents = _AlaQoSStatsL3IngressEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 4),
    _AlaQoSStatsL3IngressEvents_Type()
)
alaQoSStatsL3IngressEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL3IngressEvents.setStatus("current")
_AlaQoSStatsL3IngressMatches_Type = Counter32
_AlaQoSStatsL3IngressMatches_Object = MibScalar
alaQoSStatsL3IngressMatches = _AlaQoSStatsL3IngressMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 5),
    _AlaQoSStatsL3IngressMatches_Type()
)
alaQoSStatsL3IngressMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL3IngressMatches.setStatus("current")
_AlaQoSStatsL3IngressDrops_Type = Counter32
_AlaQoSStatsL3IngressDrops_Object = MibScalar
alaQoSStatsL3IngressDrops = _AlaQoSStatsL3IngressDrops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 6),
    _AlaQoSStatsL3IngressDrops_Type()
)
alaQoSStatsL3IngressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL3IngressDrops.setStatus("current")
_AlaQoSStatsL3EgressEvents_Type = Counter32
_AlaQoSStatsL3EgressEvents_Object = MibScalar
alaQoSStatsL3EgressEvents = _AlaQoSStatsL3EgressEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 7),
    _AlaQoSStatsL3EgressEvents_Type()
)
alaQoSStatsL3EgressEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL3EgressEvents.setStatus("current")
_AlaQoSStatsL3EgressMatches_Type = Counter32
_AlaQoSStatsL3EgressMatches_Object = MibScalar
alaQoSStatsL3EgressMatches = _AlaQoSStatsL3EgressMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 8),
    _AlaQoSStatsL3EgressMatches_Type()
)
alaQoSStatsL3EgressMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL3EgressMatches.setStatus("current")
_AlaQoSStatsL3EgressDrops_Type = Counter32
_AlaQoSStatsL3EgressDrops_Object = MibScalar
alaQoSStatsL3EgressDrops = _AlaQoSStatsL3EgressDrops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 9),
    _AlaQoSStatsL3EgressDrops_Type()
)
alaQoSStatsL3EgressDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsL3EgressDrops.setStatus("current")
_AlaQoSStatsMulticastEvents_Type = Counter32
_AlaQoSStatsMulticastEvents_Object = MibScalar
alaQoSStatsMulticastEvents = _AlaQoSStatsMulticastEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 10),
    _AlaQoSStatsMulticastEvents_Type()
)
alaQoSStatsMulticastEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsMulticastEvents.setStatus("current")
_AlaQoSStatsMulticastMatches_Type = Counter32
_AlaQoSStatsMulticastMatches_Object = MibScalar
alaQoSStatsMulticastMatches = _AlaQoSStatsMulticastMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 11),
    _AlaQoSStatsMulticastMatches_Type()
)
alaQoSStatsMulticastMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsMulticastMatches.setStatus("current")
_AlaQoSStatsMulticastDrops_Type = Counter32
_AlaQoSStatsMulticastDrops_Object = MibScalar
alaQoSStatsMulticastDrops = _AlaQoSStatsMulticastDrops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 12),
    _AlaQoSStatsMulticastDrops_Type()
)
alaQoSStatsMulticastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsMulticastDrops.setStatus("current")
_AlaQoSStatsFragments_Type = Counter32
_AlaQoSStatsFragments_Object = MibScalar
alaQoSStatsFragments = _AlaQoSStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 13),
    _AlaQoSStatsFragments_Type()
)
alaQoSStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsFragments.setStatus("current")
_AlaQoSStatsBadFragments_Type = Counter32
_AlaQoSStatsBadFragments_Object = MibScalar
alaQoSStatsBadFragments = _AlaQoSStatsBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 14),
    _AlaQoSStatsBadFragments_Type()
)
alaQoSStatsBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsBadFragments.setStatus("current")
_AlaQoSStatsUnknownFragments_Type = Counter32
_AlaQoSStatsUnknownFragments_Object = MibScalar
alaQoSStatsUnknownFragments = _AlaQoSStatsUnknownFragments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 15),
    _AlaQoSStatsUnknownFragments_Type()
)
alaQoSStatsUnknownFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsUnknownFragments.setStatus("current")
_AlaQoSStatsReflexiveFlows_Type = Counter32
_AlaQoSStatsReflexiveFlows_Object = MibScalar
alaQoSStatsReflexiveFlows = _AlaQoSStatsReflexiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 16),
    _AlaQoSStatsReflexiveFlows_Type()
)
alaQoSStatsReflexiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsReflexiveFlows.setStatus("current")
_AlaQoSStatsReflexiveCorrections_Type = Counter32
_AlaQoSStatsReflexiveCorrections_Object = MibScalar
alaQoSStatsReflexiveCorrections = _AlaQoSStatsReflexiveCorrections_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 17),
    _AlaQoSStatsReflexiveCorrections_Type()
)
alaQoSStatsReflexiveCorrections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsReflexiveCorrections.setStatus("current")
_AlaQoSStatsLoadBalanceFlows_Type = Counter32
_AlaQoSStatsLoadBalanceFlows_Object = MibScalar
alaQoSStatsLoadBalanceFlows = _AlaQoSStatsLoadBalanceFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 18),
    _AlaQoSStatsLoadBalanceFlows_Type()
)
alaQoSStatsLoadBalanceFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsLoadBalanceFlows.setStatus("current")
_AlaQoSStatsClassifierMaxNodes_Type = Counter32
_AlaQoSStatsClassifierMaxNodes_Object = MibScalar
alaQoSStatsClassifierMaxNodes = _AlaQoSStatsClassifierMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 19),
    _AlaQoSStatsClassifierMaxNodes_Type()
)
alaQoSStatsClassifierMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsClassifierMaxNodes.setStatus("current")
_AlaQoSStatsClassifierMaxDepth_Type = Counter32
_AlaQoSStatsClassifierMaxDepth_Object = MibScalar
alaQoSStatsClassifierMaxDepth = _AlaQoSStatsClassifierMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 20),
    _AlaQoSStatsClassifierMaxDepth_Type()
)
alaQoSStatsClassifierMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsClassifierMaxDepth.setStatus("current")
_AlaQoSStatsFlowLookups_Type = Counter32
_AlaQoSStatsFlowLookups_Object = MibScalar
alaQoSStatsFlowLookups = _AlaQoSStatsFlowLookups_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 21),
    _AlaQoSStatsFlowLookups_Type()
)
alaQoSStatsFlowLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsFlowLookups.setStatus("current")
_AlaQoSStatsFlowHits_Type = Counter32
_AlaQoSStatsFlowHits_Object = MibScalar
alaQoSStatsFlowHits = _AlaQoSStatsFlowHits_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 22),
    _AlaQoSStatsFlowHits_Type()
)
alaQoSStatsFlowHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsFlowHits.setStatus("current")
_AlaQoSStatsSentNIMessages_Type = Counter32
_AlaQoSStatsSentNIMessages_Object = MibScalar
alaQoSStatsSentNIMessages = _AlaQoSStatsSentNIMessages_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 23),
    _AlaQoSStatsSentNIMessages_Type()
)
alaQoSStatsSentNIMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsSentNIMessages.setStatus("current")
_AlaQoSStatsReceivedNIMessages_Type = Counter32
_AlaQoSStatsReceivedNIMessages_Object = MibScalar
alaQoSStatsReceivedNIMessages = _AlaQoSStatsReceivedNIMessages_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 24),
    _AlaQoSStatsReceivedNIMessages_Type()
)
alaQoSStatsReceivedNIMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsReceivedNIMessages.setStatus("current")
_AlaQoSStatsFailedNIMessages_Type = Counter32
_AlaQoSStatsFailedNIMessages_Object = MibScalar
alaQoSStatsFailedNIMessages = _AlaQoSStatsFailedNIMessages_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 25),
    _AlaQoSStatsFailedNIMessages_Type()
)
alaQoSStatsFailedNIMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsFailedNIMessages.setStatus("current")
_AlaQoSStatsSpoofedEvents_Type = Counter32
_AlaQoSStatsSpoofedEvents_Object = MibScalar
alaQoSStatsSpoofedEvents = _AlaQoSStatsSpoofedEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 26),
    _AlaQoSStatsSpoofedEvents_Type()
)
alaQoSStatsSpoofedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsSpoofedEvents.setStatus("current")
_AlaQoSStatsNonSpoofedEvents_Type = Counter32
_AlaQoSStatsNonSpoofedEvents_Object = MibScalar
alaQoSStatsNonSpoofedEvents = _AlaQoSStatsNonSpoofedEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 27),
    _AlaQoSStatsNonSpoofedEvents_Type()
)
alaQoSStatsNonSpoofedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsNonSpoofedEvents.setStatus("current")
_AlaQoSStatsDropServicesEvents_Type = Counter32
_AlaQoSStatsDropServicesEvents_Object = MibScalar
alaQoSStatsDropServicesEvents = _AlaQoSStatsDropServicesEvents_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 31, 28),
    _AlaQoSStatsDropServicesEvents_Type()
)
alaQoSStatsDropServicesEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSStatsDropServicesEvents.setStatus("current")
_AlaQoSQueueTable_Object = MibTable
alaQoSQueueTable = _AlaQoSQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32)
)
if mibBuilder.loadTexts:
    alaQoSQueueTable.setStatus("current")
_AlaQoSQueueEntry_Object = MibTableRow
alaQoSQueueEntry = _AlaQoSQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1)
)
alaQoSQueueEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSQueueId"),
)
if mibBuilder.loadTexts:
    alaQoSQueueEntry.setStatus("current")
_AlaQoSQueueId_Type = Integer32
_AlaQoSQueueId_Object = MibTableColumn
alaQoSQueueId = _AlaQoSQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 1),
    _AlaQoSQueueId_Type()
)
alaQoSQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSQueueId.setStatus("current")


class _AlaQoSQueueSlot_Type(Integer32):
    """Custom type alaQoSQueueSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSQueueSlot_Type.__name__ = "Integer32"
_AlaQoSQueueSlot_Object = MibTableColumn
alaQoSQueueSlot = _AlaQoSQueueSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 2),
    _AlaQoSQueueSlot_Type()
)
alaQoSQueueSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueSlot.setStatus("current")


class _AlaQoSQueuePort_Type(Integer32):
    """Custom type alaQoSQueuePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSQueuePort_Type.__name__ = "Integer32"
_AlaQoSQueuePort_Object = MibTableColumn
alaQoSQueuePort = _AlaQoSQueuePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 3),
    _AlaQoSQueuePort_Type()
)
alaQoSQueuePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueuePort.setStatus("current")


class _AlaQoSQueuePortId_Type(Integer32):
    """Custom type alaQoSQueuePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSQueuePortId_Type.__name__ = "Integer32"
_AlaQoSQueuePortId_Object = MibTableColumn
alaQoSQueuePortId = _AlaQoSQueuePortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 4),
    _AlaQoSQueuePortId_Type()
)
alaQoSQueuePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueuePortId.setStatus("current")


class _AlaQoSQueueType_Type(Integer32):
    """Custom type alaQoSQueueType based on Integer32"""
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
        *(("drr", 5),
          ("mammoth", 1),
          ("priority", 2),
          ("spwrr", 3),
          ("wrr", 4))
    )


_AlaQoSQueueType_Type.__name__ = "Integer32"
_AlaQoSQueueType_Object = MibTableColumn
alaQoSQueueType = _AlaQoSQueueType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 5),
    _AlaQoSQueueType_Type()
)
alaQoSQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueType.setStatus("current")


class _AlaQoSQueuePriority_Type(Integer32):
    """Custom type alaQoSQueuePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSQueuePriority_Type.__name__ = "Integer32"
_AlaQoSQueuePriority_Object = MibTableColumn
alaQoSQueuePriority = _AlaQoSQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 6),
    _AlaQoSQueuePriority_Type()
)
alaQoSQueuePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueuePriority.setStatus("current")
_AlaQoSQueueMinimumBandwidth_Type = Integer32
_AlaQoSQueueMinimumBandwidth_Object = MibTableColumn
alaQoSQueueMinimumBandwidth = _AlaQoSQueueMinimumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 7),
    _AlaQoSQueueMinimumBandwidth_Type()
)
alaQoSQueueMinimumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueMinimumBandwidth.setStatus("current")
_AlaQoSQueueMaximumBandwidth_Type = Integer32
_AlaQoSQueueMaximumBandwidth_Object = MibTableColumn
alaQoSQueueMaximumBandwidth = _AlaQoSQueueMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 8),
    _AlaQoSQueueMaximumBandwidth_Type()
)
alaQoSQueueMaximumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueMaximumBandwidth.setStatus("current")
_AlaQoSQueueAverageBandwidth_Type = Integer32
_AlaQoSQueueAverageBandwidth_Object = MibTableColumn
alaQoSQueueAverageBandwidth = _AlaQoSQueueAverageBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 9),
    _AlaQoSQueueAverageBandwidth_Type()
)
alaQoSQueueAverageBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueAverageBandwidth.setStatus("current")
_AlaQoSQueueMinimumDepth_Type = Integer32
_AlaQoSQueueMinimumDepth_Object = MibTableColumn
alaQoSQueueMinimumDepth = _AlaQoSQueueMinimumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 10),
    _AlaQoSQueueMinimumDepth_Type()
)
alaQoSQueueMinimumDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueMinimumDepth.setStatus("current")
_AlaQoSQueueMaximumDepth_Type = Integer32
_AlaQoSQueueMaximumDepth_Object = MibTableColumn
alaQoSQueueMaximumDepth = _AlaQoSQueueMaximumDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 11),
    _AlaQoSQueueMaximumDepth_Type()
)
alaQoSQueueMaximumDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueMaximumDepth.setStatus("current")


class _AlaQoSQueueMaximumBuffers_Type(Integer32):
    """Custom type alaQoSQueueMaximumBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSQueueMaximumBuffers_Type.__name__ = "Integer32"
_AlaQoSQueueMaximumBuffers_Object = MibTableColumn
alaQoSQueueMaximumBuffers = _AlaQoSQueueMaximumBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 12),
    _AlaQoSQueueMaximumBuffers_Type()
)
alaQoSQueueMaximumBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueMaximumBuffers.setStatus("current")


class _AlaQoSQueue8021p_Type(Integer32):
    """Custom type alaQoSQueue8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSQueue8021p_Type.__name__ = "Integer32"
_AlaQoSQueue8021p_Object = MibTableColumn
alaQoSQueue8021p = _AlaQoSQueue8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 13),
    _AlaQoSQueue8021p_Type()
)
alaQoSQueue8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueue8021p.setStatus("current")
_AlaQoSQueuePacketsSent_Type = Integer32
_AlaQoSQueuePacketsSent_Object = MibTableColumn
alaQoSQueuePacketsSent = _AlaQoSQueuePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 14),
    _AlaQoSQueuePacketsSent_Type()
)
alaQoSQueuePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueuePacketsSent.setStatus("current")
_AlaQoSQueuePacketsDropped_Type = Integer32
_AlaQoSQueuePacketsDropped_Object = MibTableColumn
alaQoSQueuePacketsDropped = _AlaQoSQueuePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 15),
    _AlaQoSQueuePacketsDropped_Type()
)
alaQoSQueuePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueuePacketsDropped.setStatus("current")
_AlaQoSQueueMaxLength_Type = Integer32
_AlaQoSQueueMaxLength_Object = MibTableColumn
alaQoSQueueMaxLength = _AlaQoSQueueMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 16),
    _AlaQoSQueueMaxLength_Type()
)
alaQoSQueueMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueMaxLength.setStatus("current")
_AlaQoSQueueAverageLength_Type = Integer32
_AlaQoSQueueAverageLength_Object = MibTableColumn
alaQoSQueueAverageLength = _AlaQoSQueueAverageLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 17),
    _AlaQoSQueueAverageLength_Type()
)
alaQoSQueueAverageLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueAverageLength.setStatus("current")
_AlaQoSQueueCurrentLength_Type = Integer32
_AlaQoSQueueCurrentLength_Object = MibTableColumn
alaQoSQueueCurrentLength = _AlaQoSQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 18),
    _AlaQoSQueueCurrentLength_Type()
)
alaQoSQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueCurrentLength.setStatus("current")


class _AlaQoSQueueAction_Type(DisplayString):
    """Custom type alaQoSQueueAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSQueueAction_Type.__name__ = "DisplayString"
_AlaQoSQueueAction_Object = MibTableColumn
alaQoSQueueAction = _AlaQoSQueueAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 32, 1, 19),
    _AlaQoSQueueAction_Type()
)
alaQoSQueueAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSQueueAction.setStatus("current")
_AlaQoSSlotTable_Object = MibTable
alaQoSSlotTable = _AlaQoSSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33)
)
if mibBuilder.loadTexts:
    alaQoSSlotTable.setStatus("current")
_AlaQoSSlotEntry_Object = MibTableRow
alaQoSSlotEntry = _AlaQoSSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1)
)
alaQoSSlotEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlice"),
)
if mibBuilder.loadTexts:
    alaQoSSlotEntry.setStatus("current")


class _AlaQoSSlotSlot_Type(Integer32):
    """Custom type alaQoSSlotSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaQoSSlotSlot_Type.__name__ = "Integer32"
_AlaQoSSlotSlot_Object = MibTableColumn
alaQoSSlotSlot = _AlaQoSSlotSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 1),
    _AlaQoSSlotSlot_Type()
)
alaQoSSlotSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSSlotSlot.setStatus("current")


class _AlaQoSSlotSlice_Type(Integer32):
    """Custom type alaQoSSlotSlice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AlaQoSSlotSlice_Type.__name__ = "Integer32"
_AlaQoSSlotSlice_Object = MibTableColumn
alaQoSSlotSlice = _AlaQoSSlotSlice_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 2),
    _AlaQoSSlotSlice_Type()
)
alaQoSSlotSlice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSSlotSlice.setStatus("current")


class _AlaQoSSlotType_Type(Integer32):
    """Custom type alaQoSSlotType based on Integer32"""
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
        *(("coronado", 4),
          ("fuji", 7),
          ("ixe2424", 5),
          ("kite", 6),
          ("kodiak", 2),
          ("mailbox", 3),
          ("mammoth", 1))
    )


_AlaQoSSlotType_Type.__name__ = "Integer32"
_AlaQoSSlotType_Object = MibTableColumn
alaQoSSlotType = _AlaQoSSlotType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 3),
    _AlaQoSSlotType_Type()
)
alaQoSSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotType.setStatus("current")
_AlaQoSSlotMaxBuffers_Type = Integer32
_AlaQoSSlotMaxBuffers_Object = MibTableColumn
alaQoSSlotMaxBuffers = _AlaQoSSlotMaxBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 4),
    _AlaQoSSlotMaxBuffers_Type()
)
alaQoSSlotMaxBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotMaxBuffers.setStatus("current")
_AlaQoSSlotFreeBuffers1_Type = Integer32
_AlaQoSSlotFreeBuffers1_Object = MibTableColumn
alaQoSSlotFreeBuffers1 = _AlaQoSSlotFreeBuffers1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 5),
    _AlaQoSSlotFreeBuffers1_Type()
)
alaQoSSlotFreeBuffers1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotFreeBuffers1.setStatus("current")
_AlaQoSSlotFreeBuffers2_Type = Integer32
_AlaQoSSlotFreeBuffers2_Object = MibTableColumn
alaQoSSlotFreeBuffers2 = _AlaQoSSlotFreeBuffers2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 6),
    _AlaQoSSlotFreeBuffers2_Type()
)
alaQoSSlotFreeBuffers2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotFreeBuffers2.setStatus("current")
_AlaQoSSlotThreshold1Low_Type = Integer32
_AlaQoSSlotThreshold1Low_Object = MibTableColumn
alaQoSSlotThreshold1Low = _AlaQoSSlotThreshold1Low_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 7),
    _AlaQoSSlotThreshold1Low_Type()
)
alaQoSSlotThreshold1Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold1Low.setStatus("current")
_AlaQoSSlotThreshold1Medium_Type = Integer32
_AlaQoSSlotThreshold1Medium_Object = MibTableColumn
alaQoSSlotThreshold1Medium = _AlaQoSSlotThreshold1Medium_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 8),
    _AlaQoSSlotThreshold1Medium_Type()
)
alaQoSSlotThreshold1Medium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold1Medium.setStatus("current")
_AlaQoSSlotThreshold1High_Type = Integer32
_AlaQoSSlotThreshold1High_Object = MibTableColumn
alaQoSSlotThreshold1High = _AlaQoSSlotThreshold1High_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 9),
    _AlaQoSSlotThreshold1High_Type()
)
alaQoSSlotThreshold1High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold1High.setStatus("current")
_AlaQoSSlotThreshold1Urgent_Type = Integer32
_AlaQoSSlotThreshold1Urgent_Object = MibTableColumn
alaQoSSlotThreshold1Urgent = _AlaQoSSlotThreshold1Urgent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 10),
    _AlaQoSSlotThreshold1Urgent_Type()
)
alaQoSSlotThreshold1Urgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold1Urgent.setStatus("current")
_AlaQoSSlotThreshold2Low_Type = Integer32
_AlaQoSSlotThreshold2Low_Object = MibTableColumn
alaQoSSlotThreshold2Low = _AlaQoSSlotThreshold2Low_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 11),
    _AlaQoSSlotThreshold2Low_Type()
)
alaQoSSlotThreshold2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold2Low.setStatus("current")
_AlaQoSSlotThreshold2Medium_Type = Integer32
_AlaQoSSlotThreshold2Medium_Object = MibTableColumn
alaQoSSlotThreshold2Medium = _AlaQoSSlotThreshold2Medium_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 12),
    _AlaQoSSlotThreshold2Medium_Type()
)
alaQoSSlotThreshold2Medium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold2Medium.setStatus("current")
_AlaQoSSlotThreshold2High_Type = Integer32
_AlaQoSSlotThreshold2High_Object = MibTableColumn
alaQoSSlotThreshold2High = _AlaQoSSlotThreshold2High_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 13),
    _AlaQoSSlotThreshold2High_Type()
)
alaQoSSlotThreshold2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold2High.setStatus("current")
_AlaQoSSlotThreshold2Urgent_Type = Integer32
_AlaQoSSlotThreshold2Urgent_Object = MibTableColumn
alaQoSSlotThreshold2Urgent = _AlaQoSSlotThreshold2Urgent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 14),
    _AlaQoSSlotThreshold2Urgent_Type()
)
alaQoSSlotThreshold2Urgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotThreshold2Urgent.setStatus("current")
_AlaQoSSlotBuffersDenied_Type = Integer32
_AlaQoSSlotBuffersDenied_Object = MibTableColumn
alaQoSSlotBuffersDenied = _AlaQoSSlotBuffersDenied_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 15),
    _AlaQoSSlotBuffersDenied_Type()
)
alaQoSSlotBuffersDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotBuffersDenied.setStatus("current")
_AlaQoSSlotBuffersDeniedAverage_Type = Integer32
_AlaQoSSlotBuffersDeniedAverage_Object = MibTableColumn
alaQoSSlotBuffersDeniedAverage = _AlaQoSSlotBuffersDeniedAverage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 16),
    _AlaQoSSlotBuffersDeniedAverage_Type()
)
alaQoSSlotBuffersDeniedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotBuffersDeniedAverage.setStatus("current")
_AlaQoSSlotBuffersDropped_Type = Integer32
_AlaQoSSlotBuffersDropped_Object = MibTableColumn
alaQoSSlotBuffersDropped = _AlaQoSSlotBuffersDropped_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 17),
    _AlaQoSSlotBuffersDropped_Type()
)
alaQoSSlotBuffersDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotBuffersDropped.setStatus("current")
_AlaQoSSlotBuffersDroppedAverage_Type = Integer32
_AlaQoSSlotBuffersDroppedAverage_Object = MibTableColumn
alaQoSSlotBuffersDroppedAverage = _AlaQoSSlotBuffersDroppedAverage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 18),
    _AlaQoSSlotBuffersDroppedAverage_Type()
)
alaQoSSlotBuffersDroppedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotBuffersDroppedAverage.setStatus("current")


class _AlaQoSSlotWredThresholdP0Lower_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP0Lower based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP0Lower_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP0Lower_Object = MibTableColumn
alaQoSSlotWredThresholdP0Lower = _AlaQoSSlotWredThresholdP0Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 19),
    _AlaQoSSlotWredThresholdP0Lower_Type()
)
alaQoSSlotWredThresholdP0Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP0Lower.setStatus("current")


class _AlaQoSSlotWredThresholdP0Upper_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP0Upper based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP0Upper_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP0Upper_Object = MibTableColumn
alaQoSSlotWredThresholdP0Upper = _AlaQoSSlotWredThresholdP0Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 20),
    _AlaQoSSlotWredThresholdP0Upper_Type()
)
alaQoSSlotWredThresholdP0Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP0Upper.setStatus("current")


class _AlaQoSSlotWredThresholdP1Lower_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP1Lower based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP1Lower_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP1Lower_Object = MibTableColumn
alaQoSSlotWredThresholdP1Lower = _AlaQoSSlotWredThresholdP1Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 21),
    _AlaQoSSlotWredThresholdP1Lower_Type()
)
alaQoSSlotWredThresholdP1Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP1Lower.setStatus("current")


class _AlaQoSSlotWredThresholdP1Upper_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP1Upper based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP1Upper_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP1Upper_Object = MibTableColumn
alaQoSSlotWredThresholdP1Upper = _AlaQoSSlotWredThresholdP1Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 22),
    _AlaQoSSlotWredThresholdP1Upper_Type()
)
alaQoSSlotWredThresholdP1Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP1Upper.setStatus("current")


class _AlaQoSSlotWredThresholdP2Lower_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP2Lower based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP2Lower_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP2Lower_Object = MibTableColumn
alaQoSSlotWredThresholdP2Lower = _AlaQoSSlotWredThresholdP2Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 23),
    _AlaQoSSlotWredThresholdP2Lower_Type()
)
alaQoSSlotWredThresholdP2Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP2Lower.setStatus("current")


class _AlaQoSSlotWredThresholdP2Upper_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP2Upper based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP2Upper_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP2Upper_Object = MibTableColumn
alaQoSSlotWredThresholdP2Upper = _AlaQoSSlotWredThresholdP2Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 24),
    _AlaQoSSlotWredThresholdP2Upper_Type()
)
alaQoSSlotWredThresholdP2Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP2Upper.setStatus("current")


class _AlaQoSSlotWredThresholdP3Lower_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP3Lower based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP3Lower_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP3Lower_Object = MibTableColumn
alaQoSSlotWredThresholdP3Lower = _AlaQoSSlotWredThresholdP3Lower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 25),
    _AlaQoSSlotWredThresholdP3Lower_Type()
)
alaQoSSlotWredThresholdP3Lower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP3Lower.setStatus("current")


class _AlaQoSSlotWredThresholdP3Upper_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdP3Upper based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotWredThresholdP3Upper_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdP3Upper_Object = MibTableColumn
alaQoSSlotWredThresholdP3Upper = _AlaQoSSlotWredThresholdP3Upper_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 26),
    _AlaQoSSlotWredThresholdP3Upper_Type()
)
alaQoSSlotWredThresholdP3Upper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdP3Upper.setStatus("current")


class _AlaQoSSlotWredAverageCounterWeight_Type(Integer32):
    """Custom type alaQoSSlotWredAverageCounterWeight based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSSlotWredAverageCounterWeight_Type.__name__ = "Integer32"
_AlaQoSSlotWredAverageCounterWeight_Object = MibTableColumn
alaQoSSlotWredAverageCounterWeight = _AlaQoSSlotWredAverageCounterWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 27),
    _AlaQoSSlotWredAverageCounterWeight_Type()
)
alaQoSSlotWredAverageCounterWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredAverageCounterWeight.setStatus("current")


class _AlaQoSSlotWredThresholdStatus_Type(Integer32):
    """Custom type alaQoSSlotWredThresholdStatus based on Integer32"""
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


_AlaQoSSlotWredThresholdStatus_Type.__name__ = "Integer32"
_AlaQoSSlotWredThresholdStatus_Object = MibTableColumn
alaQoSSlotWredThresholdStatus = _AlaQoSSlotWredThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 28),
    _AlaQoSSlotWredThresholdStatus_Type()
)
alaQoSSlotWredThresholdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotWredThresholdStatus.setStatus("current")


class _AlaQoSSlotCbqThresholdMode_Type(Integer32):
    """Custom type alaQoSSlotCbqThresholdMode based on Integer32"""
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
        *(("prioritywrr", 1),
          ("strictpriority", 3),
          ("wrr", 2))
    )


_AlaQoSSlotCbqThresholdMode_Type.__name__ = "Integer32"
_AlaQoSSlotCbqThresholdMode_Object = MibTableColumn
alaQoSSlotCbqThresholdMode = _AlaQoSSlotCbqThresholdMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 29),
    _AlaQoSSlotCbqThresholdMode_Type()
)
alaQoSSlotCbqThresholdMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotCbqThresholdMode.setStatus("current")


class _AlaQoSSlotCbqThresholdP1_Type(Integer32):
    """Custom type alaQoSSlotCbqThresholdP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotCbqThresholdP1_Type.__name__ = "Integer32"
_AlaQoSSlotCbqThresholdP1_Object = MibTableColumn
alaQoSSlotCbqThresholdP1 = _AlaQoSSlotCbqThresholdP1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 30),
    _AlaQoSSlotCbqThresholdP1_Type()
)
alaQoSSlotCbqThresholdP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotCbqThresholdP1.setStatus("current")


class _AlaQoSSlotCbqThresholdP2_Type(Integer32):
    """Custom type alaQoSSlotCbqThresholdP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotCbqThresholdP2_Type.__name__ = "Integer32"
_AlaQoSSlotCbqThresholdP2_Object = MibTableColumn
alaQoSSlotCbqThresholdP2 = _AlaQoSSlotCbqThresholdP2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 31),
    _AlaQoSSlotCbqThresholdP2_Type()
)
alaQoSSlotCbqThresholdP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotCbqThresholdP2.setStatus("current")


class _AlaQoSSlotCbqThresholdP3_Type(Integer32):
    """Custom type alaQoSSlotCbqThresholdP3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlaQoSSlotCbqThresholdP3_Type.__name__ = "Integer32"
_AlaQoSSlotCbqThresholdP3_Object = MibTableColumn
alaQoSSlotCbqThresholdP3 = _AlaQoSSlotCbqThresholdP3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 32),
    _AlaQoSSlotCbqThresholdP3_Type()
)
alaQoSSlotCbqThresholdP3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotCbqThresholdP3.setStatus("current")


class _AlaQoSSlotHighDensity_Type(Integer32):
    """Custom type alaQoSSlotHighDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSSlotHighDensity_Type.__name__ = "Integer32"
_AlaQoSSlotHighDensity_Object = MibTableColumn
alaQoSSlotHighDensity = _AlaQoSSlotHighDensity_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 33, 1, 33),
    _AlaQoSSlotHighDensity_Type()
)
alaQoSSlotHighDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotHighDensity.setStatus("current")
_AlaQoSClassify_ObjectIdentity = ObjectIdentity
alaQoSClassify = _AlaQoSClassify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34)
)


class _AlaQoSClassifyClassify_Type(Integer32):
    """Custom type alaQoSClassifyClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l2", 1),
          ("l3", 2),
          ("multicast", 3))
    )


_AlaQoSClassifyClassify_Type.__name__ = "Integer32"
_AlaQoSClassifyClassify_Object = MibScalar
alaQoSClassifyClassify = _AlaQoSClassifyClassify_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 1),
    _AlaQoSClassifyClassify_Type()
)
alaQoSClassifyClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyClassify.setStatus("current")


class _AlaQoSClassifyApplied_Type(Integer32):
    """Custom type alaQoSClassifyApplied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSClassifyApplied_Type.__name__ = "Integer32"
_AlaQoSClassifyApplied_Object = MibScalar
alaQoSClassifyApplied = _AlaQoSClassifyApplied_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 2),
    _AlaQoSClassifyApplied_Type()
)
alaQoSClassifyApplied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyApplied.setStatus("current")


class _AlaQoSClassifySourceSlot_Type(Integer32):
    """Custom type alaQoSClassifySourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSClassifySourceSlot_Type.__name__ = "Integer32"
_AlaQoSClassifySourceSlot_Object = MibScalar
alaQoSClassifySourceSlot = _AlaQoSClassifySourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 3),
    _AlaQoSClassifySourceSlot_Type()
)
alaQoSClassifySourceSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifySourceSlot.setStatus("current")


class _AlaQoSClassifySourcePort_Type(Integer32):
    """Custom type alaQoSClassifySourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSClassifySourcePort_Type.__name__ = "Integer32"
_AlaQoSClassifySourcePort_Object = MibScalar
alaQoSClassifySourcePort = _AlaQoSClassifySourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 4),
    _AlaQoSClassifySourcePort_Type()
)
alaQoSClassifySourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifySourcePort.setStatus("current")


class _AlaQoSClassifySourceInterfaceType_Type(Integer32):
    """Custom type alaQoSClassifySourceInterfaceType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 7),
          ("any", 0),
          ("ethernet", 1),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet10G", 6),
          ("ethernet1G", 5),
          ("wan", 2))
    )


_AlaQoSClassifySourceInterfaceType_Type.__name__ = "Integer32"
_AlaQoSClassifySourceInterfaceType_Object = MibScalar
alaQoSClassifySourceInterfaceType = _AlaQoSClassifySourceInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 5),
    _AlaQoSClassifySourceInterfaceType_Type()
)
alaQoSClassifySourceInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifySourceInterfaceType.setStatus("current")


class _AlaQoSClassifyDestinationSlot_Type(Integer32):
    """Custom type alaQoSClassifyDestinationSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSClassifyDestinationSlot_Type.__name__ = "Integer32"
_AlaQoSClassifyDestinationSlot_Object = MibScalar
alaQoSClassifyDestinationSlot = _AlaQoSClassifyDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 6),
    _AlaQoSClassifyDestinationSlot_Type()
)
alaQoSClassifyDestinationSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDestinationSlot.setStatus("current")


class _AlaQoSClassifyDestinationPort_Type(Integer32):
    """Custom type alaQoSClassifyDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSClassifyDestinationPort_Type.__name__ = "Integer32"
_AlaQoSClassifyDestinationPort_Object = MibScalar
alaQoSClassifyDestinationPort = _AlaQoSClassifyDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 7),
    _AlaQoSClassifyDestinationPort_Type()
)
alaQoSClassifyDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDestinationPort.setStatus("current")


class _AlaQoSClassifyDestinationInterfaceType_Type(Integer32):
    """Custom type alaQoSClassifyDestinationInterfaceType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 7),
          ("any", 0),
          ("ethernet", 1),
          ("ethernet10", 3),
          ("ethernet100", 4),
          ("ethernet10G", 6),
          ("ethernet1G", 5),
          ("wan", 2))
    )


_AlaQoSClassifyDestinationInterfaceType_Type.__name__ = "Integer32"
_AlaQoSClassifyDestinationInterfaceType_Object = MibScalar
alaQoSClassifyDestinationInterfaceType = _AlaQoSClassifyDestinationInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 8),
    _AlaQoSClassifyDestinationInterfaceType_Type()
)
alaQoSClassifyDestinationInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDestinationInterfaceType.setStatus("current")
_AlaQoSClassifySourceMac_Type = MacAddress
_AlaQoSClassifySourceMac_Object = MibScalar
alaQoSClassifySourceMac = _AlaQoSClassifySourceMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 9),
    _AlaQoSClassifySourceMac_Type()
)
alaQoSClassifySourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifySourceMac.setStatus("current")
_AlaQoSClassifyDestinationMac_Type = MacAddress
_AlaQoSClassifyDestinationMac_Object = MibScalar
alaQoSClassifyDestinationMac = _AlaQoSClassifyDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 10),
    _AlaQoSClassifyDestinationMac_Type()
)
alaQoSClassifyDestinationMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDestinationMac.setStatus("current")


class _AlaQoSClassifySourceVlan_Type(Integer32):
    """Custom type alaQoSClassifySourceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSClassifySourceVlan_Type.__name__ = "Integer32"
_AlaQoSClassifySourceVlan_Object = MibScalar
alaQoSClassifySourceVlan = _AlaQoSClassifySourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 11),
    _AlaQoSClassifySourceVlan_Type()
)
alaQoSClassifySourceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifySourceVlan.setStatus("current")


class _AlaQoSClassifyDestinationVlan_Type(Integer32):
    """Custom type alaQoSClassifyDestinationVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSClassifyDestinationVlan_Type.__name__ = "Integer32"
_AlaQoSClassifyDestinationVlan_Object = MibScalar
alaQoSClassifyDestinationVlan = _AlaQoSClassifyDestinationVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 12),
    _AlaQoSClassifyDestinationVlan_Type()
)
alaQoSClassifyDestinationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDestinationVlan.setStatus("current")


class _AlaQoSClassify8021p_Type(Integer32):
    """Custom type alaQoSClassify8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSClassify8021p_Type.__name__ = "Integer32"
_AlaQoSClassify8021p_Object = MibScalar
alaQoSClassify8021p = _AlaQoSClassify8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 13),
    _AlaQoSClassify8021p_Type()
)
alaQoSClassify8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassify8021p.setStatus("current")
_AlaQoSClassifySourceIp_Type = IpAddress
_AlaQoSClassifySourceIp_Object = MibScalar
alaQoSClassifySourceIp = _AlaQoSClassifySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 14),
    _AlaQoSClassifySourceIp_Type()
)
alaQoSClassifySourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifySourceIp.setStatus("current")
_AlaQoSClassifyDestinationIp_Type = IpAddress
_AlaQoSClassifyDestinationIp_Object = MibScalar
alaQoSClassifyDestinationIp = _AlaQoSClassifyDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 15),
    _AlaQoSClassifyDestinationIp_Type()
)
alaQoSClassifyDestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDestinationIp.setStatus("current")
_AlaQoSClassifyMulticastIp_Type = IpAddress
_AlaQoSClassifyMulticastIp_Object = MibScalar
alaQoSClassifyMulticastIp = _AlaQoSClassifyMulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 16),
    _AlaQoSClassifyMulticastIp_Type()
)
alaQoSClassifyMulticastIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyMulticastIp.setStatus("current")


class _AlaQoSClassifyTos_Type(Integer32):
    """Custom type alaQoSClassifyTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaQoSClassifyTos_Type.__name__ = "Integer32"
_AlaQoSClassifyTos_Object = MibScalar
alaQoSClassifyTos = _AlaQoSClassifyTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 17),
    _AlaQoSClassifyTos_Type()
)
alaQoSClassifyTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyTos.setStatus("current")


class _AlaQoSClassifyDscp_Type(Integer32):
    """Custom type alaQoSClassifyDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSClassifyDscp_Type.__name__ = "Integer32"
_AlaQoSClassifyDscp_Object = MibScalar
alaQoSClassifyDscp = _AlaQoSClassifyDscp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 18),
    _AlaQoSClassifyDscp_Type()
)
alaQoSClassifyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDscp.setStatus("current")


class _AlaQoSClassifyIpProtocol_Type(Integer32):
    """Custom type alaQoSClassifyIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSClassifyIpProtocol_Type.__name__ = "Integer32"
_AlaQoSClassifyIpProtocol_Object = MibScalar
alaQoSClassifyIpProtocol = _AlaQoSClassifyIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 19),
    _AlaQoSClassifyIpProtocol_Type()
)
alaQoSClassifyIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyIpProtocol.setStatus("current")


class _AlaQoSClassifySourceIpPort_Type(Integer32):
    """Custom type alaQoSClassifySourceIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSClassifySourceIpPort_Type.__name__ = "Integer32"
_AlaQoSClassifySourceIpPort_Object = MibScalar
alaQoSClassifySourceIpPort = _AlaQoSClassifySourceIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 20),
    _AlaQoSClassifySourceIpPort_Type()
)
alaQoSClassifySourceIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifySourceIpPort.setStatus("current")


class _AlaQoSClassifyDestinationIpPort_Type(Integer32):
    """Custom type alaQoSClassifyDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSClassifyDestinationIpPort_Type.__name__ = "Integer32"
_AlaQoSClassifyDestinationIpPort_Object = MibScalar
alaQoSClassifyDestinationIpPort = _AlaQoSClassifyDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 21),
    _AlaQoSClassifyDestinationIpPort_Type()
)
alaQoSClassifyDestinationIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyDestinationIpPort.setStatus("current")


class _AlaQoSClassifyExecute_Type(Integer32):
    """Custom type alaQoSClassifyExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSClassifyExecute_Type.__name__ = "Integer32"
_AlaQoSClassifyExecute_Object = MibScalar
alaQoSClassifyExecute = _AlaQoSClassifyExecute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 22),
    _AlaQoSClassifyExecute_Type()
)
alaQoSClassifyExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQoSClassifyExecute.setStatus("current")


class _AlaQoSClassifyL2SourceResultRule_Type(DisplayString):
    """Custom type alaQoSClassifyL2SourceResultRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSClassifyL2SourceResultRule_Type.__name__ = "DisplayString"
_AlaQoSClassifyL2SourceResultRule_Object = MibScalar
alaQoSClassifyL2SourceResultRule = _AlaQoSClassifyL2SourceResultRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 23),
    _AlaQoSClassifyL2SourceResultRule_Type()
)
alaQoSClassifyL2SourceResultRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyL2SourceResultRule.setStatus("current")


class _AlaQoSClassifyL2SourceResultDisposition_Type(Integer32):
    """Custom type alaQoSClassifyL2SourceResultDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSClassifyL2SourceResultDisposition_Type.__name__ = "Integer32"
_AlaQoSClassifyL2SourceResultDisposition_Object = MibScalar
alaQoSClassifyL2SourceResultDisposition = _AlaQoSClassifyL2SourceResultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 24),
    _AlaQoSClassifyL2SourceResultDisposition_Type()
)
alaQoSClassifyL2SourceResultDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyL2SourceResultDisposition.setStatus("current")


class _AlaQoSClassifyL2DestinationResultRule_Type(DisplayString):
    """Custom type alaQoSClassifyL2DestinationResultRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSClassifyL2DestinationResultRule_Type.__name__ = "DisplayString"
_AlaQoSClassifyL2DestinationResultRule_Object = MibScalar
alaQoSClassifyL2DestinationResultRule = _AlaQoSClassifyL2DestinationResultRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 25),
    _AlaQoSClassifyL2DestinationResultRule_Type()
)
alaQoSClassifyL2DestinationResultRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyL2DestinationResultRule.setStatus("current")


class _AlaQoSClassifyL2DestinationResultDisposition_Type(Integer32):
    """Custom type alaQoSClassifyL2DestinationResultDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSClassifyL2DestinationResultDisposition_Type.__name__ = "Integer32"
_AlaQoSClassifyL2DestinationResultDisposition_Object = MibScalar
alaQoSClassifyL2DestinationResultDisposition = _AlaQoSClassifyL2DestinationResultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 26),
    _AlaQoSClassifyL2DestinationResultDisposition_Type()
)
alaQoSClassifyL2DestinationResultDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyL2DestinationResultDisposition.setStatus("current")


class _AlaQoSClassifyL3ResultRule_Type(DisplayString):
    """Custom type alaQoSClassifyL3ResultRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSClassifyL3ResultRule_Type.__name__ = "DisplayString"
_AlaQoSClassifyL3ResultRule_Object = MibScalar
alaQoSClassifyL3ResultRule = _AlaQoSClassifyL3ResultRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 27),
    _AlaQoSClassifyL3ResultRule_Type()
)
alaQoSClassifyL3ResultRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyL3ResultRule.setStatus("current")


class _AlaQoSClassifyL3ResultDisposition_Type(Integer32):
    """Custom type alaQoSClassifyL3ResultDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSClassifyL3ResultDisposition_Type.__name__ = "Integer32"
_AlaQoSClassifyL3ResultDisposition_Object = MibScalar
alaQoSClassifyL3ResultDisposition = _AlaQoSClassifyL3ResultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 28),
    _AlaQoSClassifyL3ResultDisposition_Type()
)
alaQoSClassifyL3ResultDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyL3ResultDisposition.setStatus("current")


class _AlaQoSClassifyIGMPResultRule_Type(DisplayString):
    """Custom type alaQoSClassifyIGMPResultRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSClassifyIGMPResultRule_Type.__name__ = "DisplayString"
_AlaQoSClassifyIGMPResultRule_Object = MibScalar
alaQoSClassifyIGMPResultRule = _AlaQoSClassifyIGMPResultRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 29),
    _AlaQoSClassifyIGMPResultRule_Type()
)
alaQoSClassifyIGMPResultRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyIGMPResultRule.setStatus("current")


class _AlaQoSClassifyIGMPResultDisposition_Type(Integer32):
    """Custom type alaQoSClassifyIGMPResultDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSClassifyIGMPResultDisposition_Type.__name__ = "Integer32"
_AlaQoSClassifyIGMPResultDisposition_Object = MibScalar
alaQoSClassifyIGMPResultDisposition = _AlaQoSClassifyIGMPResultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 30),
    _AlaQoSClassifyIGMPResultDisposition_Type()
)
alaQoSClassifyIGMPResultDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyIGMPResultDisposition.setStatus("current")


class _AlaQoSClassifyMulticastResultRule_Type(DisplayString):
    """Custom type alaQoSClassifyMulticastResultRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSClassifyMulticastResultRule_Type.__name__ = "DisplayString"
_AlaQoSClassifyMulticastResultRule_Object = MibScalar
alaQoSClassifyMulticastResultRule = _AlaQoSClassifyMulticastResultRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 31),
    _AlaQoSClassifyMulticastResultRule_Type()
)
alaQoSClassifyMulticastResultRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyMulticastResultRule.setStatus("current")


class _AlaQoSClassifyMulticastResultDisposition_Type(Integer32):
    """Custom type alaQoSClassifyMulticastResultDisposition based on Integer32"""
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
          ("deny", 3),
          ("drop", 2))
    )


_AlaQoSClassifyMulticastResultDisposition_Type.__name__ = "Integer32"
_AlaQoSClassifyMulticastResultDisposition_Object = MibScalar
alaQoSClassifyMulticastResultDisposition = _AlaQoSClassifyMulticastResultDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 34, 32),
    _AlaQoSClassifyMulticastResultDisposition_Type()
)
alaQoSClassifyMulticastResultDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSClassifyMulticastResultDisposition.setStatus("current")
_AlaQoSSlotProtocolTable_Object = MibTable
alaQoSSlotProtocolTable = _AlaQoSSlotProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35)
)
if mibBuilder.loadTexts:
    alaQoSSlotProtocolTable.setStatus("current")
_AlaQoSSlotProtocolEntry_Object = MibTableRow
alaQoSSlotProtocolEntry = _AlaQoSSlotProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1)
)
alaQoSSlotProtocolEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlice"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotProtocolId"),
)
if mibBuilder.loadTexts:
    alaQoSSlotProtocolEntry.setStatus("current")


class _AlaQoSSlotProtocolId_Type(Integer32):
    """Custom type alaQoSSlotProtocolId based on Integer32"""
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
        *(("unknown", 5),
          ("user1", 1),
          ("user2", 2),
          ("user3", 3),
          ("user4", 4))
    )


_AlaQoSSlotProtocolId_Type.__name__ = "Integer32"
_AlaQoSSlotProtocolId_Object = MibTableColumn
alaQoSSlotProtocolId = _AlaQoSSlotProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 1),
    _AlaQoSSlotProtocolId_Type()
)
alaQoSSlotProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSSlotProtocolId.setStatus("current")


class _AlaQoSSlotProtocolEthertype_Type(Integer32):
    """Custom type alaQoSSlotProtocolEthertype based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSSlotProtocolEthertype_Type.__name__ = "Integer32"
_AlaQoSSlotProtocolEthertype_Object = MibTableColumn
alaQoSSlotProtocolEthertype = _AlaQoSSlotProtocolEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 2),
    _AlaQoSSlotProtocolEthertype_Type()
)
alaQoSSlotProtocolEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotProtocolEthertype.setStatus("current")


class _AlaQoSSlotProtocolDsap_Type(Integer32):
    """Custom type alaQoSSlotProtocolDsap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSSlotProtocolDsap_Type.__name__ = "Integer32"
_AlaQoSSlotProtocolDsap_Object = MibTableColumn
alaQoSSlotProtocolDsap = _AlaQoSSlotProtocolDsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 3),
    _AlaQoSSlotProtocolDsap_Type()
)
alaQoSSlotProtocolDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotProtocolDsap.setStatus("current")


class _AlaQoSSlotProtocolSsap_Type(Integer32):
    """Custom type alaQoSSlotProtocolSsap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSSlotProtocolSsap_Type.__name__ = "Integer32"
_AlaQoSSlotProtocolSsap_Object = MibTableColumn
alaQoSSlotProtocolSsap = _AlaQoSSlotProtocolSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 4),
    _AlaQoSSlotProtocolSsap_Type()
)
alaQoSSlotProtocolSsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotProtocolSsap.setStatus("current")


class _AlaQoSSlotProtocol8023Enabled_Type(Integer32):
    """Custom type alaQoSSlotProtocol8023Enabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSSlotProtocol8023Enabled_Type.__name__ = "Integer32"
_AlaQoSSlotProtocol8023Enabled_Object = MibTableColumn
alaQoSSlotProtocol8023Enabled = _AlaQoSSlotProtocol8023Enabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 5),
    _AlaQoSSlotProtocol8023Enabled_Type()
)
alaQoSSlotProtocol8023Enabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotProtocol8023Enabled.setStatus("current")


class _AlaQoSSlotProtocolType_Type(Integer32):
    """Custom type alaQoSSlotProtocolType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallback", 2),
          ("priority", 1))
    )


_AlaQoSSlotProtocolType_Type.__name__ = "Integer32"
_AlaQoSSlotProtocolType_Object = MibTableColumn
alaQoSSlotProtocolType = _AlaQoSSlotProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 6),
    _AlaQoSSlotProtocolType_Type()
)
alaQoSSlotProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotProtocolType.setStatus("current")
_AlaQoSSlotProtocolRowStatus_Type = RowStatus
_AlaQoSSlotProtocolRowStatus_Object = MibTableColumn
alaQoSSlotProtocolRowStatus = _AlaQoSSlotProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 35, 1, 7),
    _AlaQoSSlotProtocolRowStatus_Type()
)
alaQoSSlotProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotProtocolRowStatus.setStatus("current")
_AlaQoSPortProtocolTable_Object = MibTable
alaQoSPortProtocolTable = _AlaQoSPortProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36)
)
if mibBuilder.loadTexts:
    alaQoSPortProtocolTable.setStatus("current")
_AlaQoSPortProtocolEntry_Object = MibTableRow
alaQoSPortProtocolEntry = _AlaQoSPortProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1)
)
alaQoSPortProtocolEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortPort"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortProtocolId"),
)
if mibBuilder.loadTexts:
    alaQoSPortProtocolEntry.setStatus("current")


class _AlaQoSPortProtocolId_Type(Integer32):
    """Custom type alaQoSPortProtocolId based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("apple", 9),
          ("arp", 5),
          ("bpdu", 1),
          ("decnet", 11),
          ("ipv4", 4),
          ("ipv6", 7),
          ("ipx", 8),
          ("lcpeth", 3),
          ("lcpsnap", 2),
          ("rarp", 6),
          ("sna", 10),
          ("user1", 12),
          ("user2", 13),
          ("user3", 14),
          ("user4", 15))
    )


_AlaQoSPortProtocolId_Type.__name__ = "Integer32"
_AlaQoSPortProtocolId_Object = MibTableColumn
alaQoSPortProtocolId = _AlaQoSPortProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 1),
    _AlaQoSPortProtocolId_Type()
)
alaQoSPortProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortProtocolId.setStatus("current")


class _AlaQoSPortProtocolClassification_Type(Integer32):
    """Custom type alaQoSPortProtocolClassification based on Integer32"""
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
        *(("b8021p", 1),
          ("dscp", 3),
          ("tos", 2))
    )


_AlaQoSPortProtocolClassification_Type.__name__ = "Integer32"
_AlaQoSPortProtocolClassification_Object = MibTableColumn
alaQoSPortProtocolClassification = _AlaQoSPortProtocolClassification_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 2),
    _AlaQoSPortProtocolClassification_Type()
)
alaQoSPortProtocolClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolClassification.setStatus("current")


class _AlaQoSPortProtocolPriorityP0_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP0 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP0_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP0_Object = MibTableColumn
alaQoSPortProtocolPriorityP0 = _AlaQoSPortProtocolPriorityP0_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 3),
    _AlaQoSPortProtocolPriorityP0_Type()
)
alaQoSPortProtocolPriorityP0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP0.setStatus("current")


class _AlaQoSPortProtocolPriorityP1_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP1_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP1_Object = MibTableColumn
alaQoSPortProtocolPriorityP1 = _AlaQoSPortProtocolPriorityP1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 4),
    _AlaQoSPortProtocolPriorityP1_Type()
)
alaQoSPortProtocolPriorityP1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP1.setStatus("current")


class _AlaQoSPortProtocolPriorityP2_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP2_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP2_Object = MibTableColumn
alaQoSPortProtocolPriorityP2 = _AlaQoSPortProtocolPriorityP2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 5),
    _AlaQoSPortProtocolPriorityP2_Type()
)
alaQoSPortProtocolPriorityP2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP2.setStatus("current")


class _AlaQoSPortProtocolPriorityP3_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP3_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP3_Object = MibTableColumn
alaQoSPortProtocolPriorityP3 = _AlaQoSPortProtocolPriorityP3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 6),
    _AlaQoSPortProtocolPriorityP3_Type()
)
alaQoSPortProtocolPriorityP3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP3.setStatus("current")


class _AlaQoSPortProtocolPriorityP4_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP4 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP4_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP4_Object = MibTableColumn
alaQoSPortProtocolPriorityP4 = _AlaQoSPortProtocolPriorityP4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 7),
    _AlaQoSPortProtocolPriorityP4_Type()
)
alaQoSPortProtocolPriorityP4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP4.setStatus("current")


class _AlaQoSPortProtocolPriorityP5_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP5 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP5_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP5_Object = MibTableColumn
alaQoSPortProtocolPriorityP5 = _AlaQoSPortProtocolPriorityP5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 8),
    _AlaQoSPortProtocolPriorityP5_Type()
)
alaQoSPortProtocolPriorityP5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP5.setStatus("current")


class _AlaQoSPortProtocolPriorityP6_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP6 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP6_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP6_Object = MibTableColumn
alaQoSPortProtocolPriorityP6 = _AlaQoSPortProtocolPriorityP6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 9),
    _AlaQoSPortProtocolPriorityP6_Type()
)
alaQoSPortProtocolPriorityP6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP6.setStatus("current")


class _AlaQoSPortProtocolPriorityP7_Type(Integer32):
    """Custom type alaQoSPortProtocolPriorityP7 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSPortProtocolPriorityP7_Type.__name__ = "Integer32"
_AlaQoSPortProtocolPriorityP7_Object = MibTableColumn
alaQoSPortProtocolPriorityP7 = _AlaQoSPortProtocolPriorityP7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 10),
    _AlaQoSPortProtocolPriorityP7_Type()
)
alaQoSPortProtocolPriorityP7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolPriorityP7.setStatus("current")
_AlaQoSPortProtocolRowStatus_Type = RowStatus
_AlaQoSPortProtocolRowStatus_Object = MibTableColumn
alaQoSPortProtocolRowStatus = _AlaQoSPortProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 36, 1, 11),
    _AlaQoSPortProtocolRowStatus_Type()
)
alaQoSPortProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSPortProtocolRowStatus.setStatus("current")
_AlaQoSSlotDscpTable_Object = MibTable
alaQoSSlotDscpTable = _AlaQoSSlotDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37)
)
if mibBuilder.loadTexts:
    alaQoSSlotDscpTable.setStatus("current")
_AlaQoSSlotDscpEntry_Object = MibTableRow
alaQoSSlotDscpEntry = _AlaQoSSlotDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1)
)
alaQoSSlotDscpEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlice"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotDscpIndex"),
)
if mibBuilder.loadTexts:
    alaQoSSlotDscpEntry.setStatus("current")


class _AlaQoSSlotDscpIndex_Type(Integer32):
    """Custom type alaQoSSlotDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AlaQoSSlotDscpIndex_Type.__name__ = "Integer32"
_AlaQoSSlotDscpIndex_Object = MibTableColumn
alaQoSSlotDscpIndex = _AlaQoSSlotDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 1),
    _AlaQoSSlotDscpIndex_Type()
)
alaQoSSlotDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSSlotDscpIndex.setStatus("current")


class _AlaQoSSlotDscpPriority_Type(Integer32):
    """Custom type alaQoSSlotDscpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaQoSSlotDscpPriority_Type.__name__ = "Integer32"
_AlaQoSSlotDscpPriority_Object = MibTableColumn
alaQoSSlotDscpPriority = _AlaQoSSlotDscpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 37, 1, 2),
    _AlaQoSSlotDscpPriority_Type()
)
alaQoSSlotDscpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSSlotDscpPriority.setStatus("current")
_AlaQoSSlotPcamTable_Object = MibTable
alaQoSSlotPcamTable = _AlaQoSSlotPcamTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38)
)
if mibBuilder.loadTexts:
    alaQoSSlotPcamTable.setStatus("current")
_AlaQoSSlotPcamEntry_Object = MibTableRow
alaQoSSlotPcamEntry = _AlaQoSSlotPcamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1)
)
alaQoSSlotPcamEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotSlice"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSSlotPcamId"),
)
if mibBuilder.loadTexts:
    alaQoSSlotPcamEntry.setStatus("current")


class _AlaQoSSlotPcamId_Type(Integer32):
    """Custom type alaQoSSlotPcamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AlaQoSSlotPcamId_Type.__name__ = "Integer32"
_AlaQoSSlotPcamId_Object = MibTableColumn
alaQoSSlotPcamId = _AlaQoSSlotPcamId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 1),
    _AlaQoSSlotPcamId_Type()
)
alaQoSSlotPcamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSSlotPcamId.setStatus("current")


class _AlaQoSSlotPcamEthertype_Type(Integer32):
    """Custom type alaQoSSlotPcamEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSSlotPcamEthertype_Type.__name__ = "Integer32"
_AlaQoSSlotPcamEthertype_Object = MibTableColumn
alaQoSSlotPcamEthertype = _AlaQoSSlotPcamEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 2),
    _AlaQoSSlotPcamEthertype_Type()
)
alaQoSSlotPcamEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamEthertype.setStatus("current")


class _AlaQoSSlotPcamDsap_Type(Integer32):
    """Custom type alaQoSSlotPcamDsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSSlotPcamDsap_Type.__name__ = "Integer32"
_AlaQoSSlotPcamDsap_Object = MibTableColumn
alaQoSSlotPcamDsap = _AlaQoSSlotPcamDsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 3),
    _AlaQoSSlotPcamDsap_Type()
)
alaQoSSlotPcamDsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamDsap.setStatus("current")


class _AlaQoSSlotPcamSsap_Type(Integer32):
    """Custom type alaQoSSlotPcamSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSSlotPcamSsap_Type.__name__ = "Integer32"
_AlaQoSSlotPcamSsap_Object = MibTableColumn
alaQoSSlotPcamSsap = _AlaQoSSlotPcamSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 4),
    _AlaQoSSlotPcamSsap_Type()
)
alaQoSSlotPcamSsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamSsap.setStatus("current")


class _AlaQoSSlotPcam8023Enabled_Type(Integer32):
    """Custom type alaQoSSlotPcam8023Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSSlotPcam8023Enabled_Type.__name__ = "Integer32"
_AlaQoSSlotPcam8023Enabled_Object = MibTableColumn
alaQoSSlotPcam8023Enabled = _AlaQoSSlotPcam8023Enabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 5),
    _AlaQoSSlotPcam8023Enabled_Type()
)
alaQoSSlotPcam8023Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcam8023Enabled.setStatus("current")


class _AlaQoSSlotPcamProtocolNumber_Type(Integer32):
    """Custom type alaQoSSlotPcamProtocolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSSlotPcamProtocolNumber_Type.__name__ = "Integer32"
_AlaQoSSlotPcamProtocolNumber_Object = MibTableColumn
alaQoSSlotPcamProtocolNumber = _AlaQoSSlotPcamProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 6),
    _AlaQoSSlotPcamProtocolNumber_Type()
)
alaQoSSlotPcamProtocolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamProtocolNumber.setStatus("current")


class _AlaQoSSlotPcamEnableEntry_Type(Integer32):
    """Custom type alaQoSSlotPcamEnableEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSSlotPcamEnableEntry_Type.__name__ = "Integer32"
_AlaQoSSlotPcamEnableEntry_Object = MibTableColumn
alaQoSSlotPcamEnableEntry = _AlaQoSSlotPcamEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 7),
    _AlaQoSSlotPcamEnableEntry_Type()
)
alaQoSSlotPcamEnableEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamEnableEntry.setStatus("current")


class _AlaQoSSlotPcamEnable8023_Type(Integer32):
    """Custom type alaQoSSlotPcamEnable8023 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSSlotPcamEnable8023_Type.__name__ = "Integer32"
_AlaQoSSlotPcamEnable8023_Object = MibTableColumn
alaQoSSlotPcamEnable8023 = _AlaQoSSlotPcamEnable8023_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 8),
    _AlaQoSSlotPcamEnable8023_Type()
)
alaQoSSlotPcamEnable8023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamEnable8023.setStatus("current")


class _AlaQoSSlotPcamEnableDsap_Type(Integer32):
    """Custom type alaQoSSlotPcamEnableDsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSSlotPcamEnableDsap_Type.__name__ = "Integer32"
_AlaQoSSlotPcamEnableDsap_Object = MibTableColumn
alaQoSSlotPcamEnableDsap = _AlaQoSSlotPcamEnableDsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 9),
    _AlaQoSSlotPcamEnableDsap_Type()
)
alaQoSSlotPcamEnableDsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamEnableDsap.setStatus("current")


class _AlaQoSSlotPcamEnableSsap_Type(Integer32):
    """Custom type alaQoSSlotPcamEnableSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSSlotPcamEnableSsap_Type.__name__ = "Integer32"
_AlaQoSSlotPcamEnableSsap_Object = MibTableColumn
alaQoSSlotPcamEnableSsap = _AlaQoSSlotPcamEnableSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 10),
    _AlaQoSSlotPcamEnableSsap_Type()
)
alaQoSSlotPcamEnableSsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamEnableSsap.setStatus("current")


class _AlaQoSSlotPcamEnableEthertype_Type(Integer32):
    """Custom type alaQoSSlotPcamEnableEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AlaQoSSlotPcamEnableEthertype_Type.__name__ = "Integer32"
_AlaQoSSlotPcamEnableEthertype_Object = MibTableColumn
alaQoSSlotPcamEnableEthertype = _AlaQoSSlotPcamEnableEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 38, 1, 11),
    _AlaQoSSlotPcamEnableEthertype_Type()
)
alaQoSSlotPcamEnableEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSSlotPcamEnableEthertype.setStatus("current")
_AlaQoSPortPdiTable_Object = MibTable
alaQoSPortPdiTable = _AlaQoSPortPdiTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39)
)
if mibBuilder.loadTexts:
    alaQoSPortPdiTable.setStatus("current")
_AlaQoSPortPdiEntry_Object = MibTableRow
alaQoSPortPdiEntry = _AlaQoSPortPdiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1)
)
alaQoSPortPdiEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortSlot"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortPort"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSPortPdiId"),
)
if mibBuilder.loadTexts:
    alaQoSPortPdiEntry.setStatus("current")


class _AlaQoSPortPdiId_Type(Integer32):
    """Custom type alaQoSPortPdiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSPortPdiId_Type.__name__ = "Integer32"
_AlaQoSPortPdiId_Object = MibTableColumn
alaQoSPortPdiId = _AlaQoSPortPdiId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 1),
    _AlaQoSPortPdiId_Type()
)
alaQoSPortPdiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSPortPdiId.setStatus("current")


class _AlaQoSPortPdiPriorityType_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityType_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityType_Object = MibTableColumn
alaQoSPortPdiPriorityType = _AlaQoSPortPdiPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 2),
    _AlaQoSPortPdiPriorityType_Type()
)
alaQoSPortPdiPriorityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityType.setStatus("current")


class _AlaQoSPortPdiPriorityP0_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP0_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP0_Object = MibTableColumn
alaQoSPortPdiPriorityP0 = _AlaQoSPortPdiPriorityP0_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 3),
    _AlaQoSPortPdiPriorityP0_Type()
)
alaQoSPortPdiPriorityP0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP0.setStatus("current")


class _AlaQoSPortPdiPriorityP1_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP1_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP1_Object = MibTableColumn
alaQoSPortPdiPriorityP1 = _AlaQoSPortPdiPriorityP1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 4),
    _AlaQoSPortPdiPriorityP1_Type()
)
alaQoSPortPdiPriorityP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP1.setStatus("current")


class _AlaQoSPortPdiPriorityP2_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP2_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP2_Object = MibTableColumn
alaQoSPortPdiPriorityP2 = _AlaQoSPortPdiPriorityP2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 5),
    _AlaQoSPortPdiPriorityP2_Type()
)
alaQoSPortPdiPriorityP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP2.setStatus("current")


class _AlaQoSPortPdiPriorityP3_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP3_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP3_Object = MibTableColumn
alaQoSPortPdiPriorityP3 = _AlaQoSPortPdiPriorityP3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 6),
    _AlaQoSPortPdiPriorityP3_Type()
)
alaQoSPortPdiPriorityP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP3.setStatus("current")


class _AlaQoSPortPdiPriorityP4_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP4_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP4_Object = MibTableColumn
alaQoSPortPdiPriorityP4 = _AlaQoSPortPdiPriorityP4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 7),
    _AlaQoSPortPdiPriorityP4_Type()
)
alaQoSPortPdiPriorityP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP4.setStatus("current")


class _AlaQoSPortPdiPriorityP5_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP5_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP5_Object = MibTableColumn
alaQoSPortPdiPriorityP5 = _AlaQoSPortPdiPriorityP5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 8),
    _AlaQoSPortPdiPriorityP5_Type()
)
alaQoSPortPdiPriorityP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP5.setStatus("current")


class _AlaQoSPortPdiPriorityP6_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP6_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP6_Object = MibTableColumn
alaQoSPortPdiPriorityP6 = _AlaQoSPortPdiPriorityP6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 9),
    _AlaQoSPortPdiPriorityP6_Type()
)
alaQoSPortPdiPriorityP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP6.setStatus("current")


class _AlaQoSPortPdiPriorityP7_Type(Integer32):
    """Custom type alaQoSPortPdiPriorityP7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaQoSPortPdiPriorityP7_Type.__name__ = "Integer32"
_AlaQoSPortPdiPriorityP7_Object = MibTableColumn
alaQoSPortPdiPriorityP7 = _AlaQoSPortPdiPriorityP7_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 39, 1, 10),
    _AlaQoSPortPdiPriorityP7_Type()
)
alaQoSPortPdiPriorityP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSPortPdiPriorityP7.setStatus("current")
_AlaQoSValidityPeriodTable_Object = MibTable
alaQoSValidityPeriodTable = _AlaQoSValidityPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40)
)
if mibBuilder.loadTexts:
    alaQoSValidityPeriodTable.setStatus("current")
_AlaQoSValidityPeriodEntry_Object = MibTableRow
alaQoSValidityPeriodEntry = _AlaQoSValidityPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1)
)
alaQoSValidityPeriodEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSValidityPeriodName"),
)
if mibBuilder.loadTexts:
    alaQoSValidityPeriodEntry.setStatus("current")


class _AlaQoSValidityPeriodName_Type(DisplayString):
    """Custom type alaQoSValidityPeriodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSValidityPeriodName_Type.__name__ = "DisplayString"
_AlaQoSValidityPeriodName_Object = MibTableColumn
alaQoSValidityPeriodName = _AlaQoSValidityPeriodName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 1),
    _AlaQoSValidityPeriodName_Type()
)
alaQoSValidityPeriodName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodName.setStatus("current")


class _AlaQoSValidityPeriodSource_Type(Integer32):
    """Custom type alaQoSValidityPeriodSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSValidityPeriodSource_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodSource_Object = MibTableColumn
alaQoSValidityPeriodSource = _AlaQoSValidityPeriodSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 2),
    _AlaQoSValidityPeriodSource_Type()
)
alaQoSValidityPeriodSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodSource.setStatus("current")
_AlaQoSValidityPeriodDays_Type = Integer32
_AlaQoSValidityPeriodDays_Object = MibTableColumn
alaQoSValidityPeriodDays = _AlaQoSValidityPeriodDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 3),
    _AlaQoSValidityPeriodDays_Type()
)
alaQoSValidityPeriodDays.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodDays.setStatus("current")


class _AlaQoSValidityPeriodDaysStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodDaysStatus based on Integer32"""
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


_AlaQoSValidityPeriodDaysStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodDaysStatus_Object = MibTableColumn
alaQoSValidityPeriodDaysStatus = _AlaQoSValidityPeriodDaysStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 4),
    _AlaQoSValidityPeriodDaysStatus_Type()
)
alaQoSValidityPeriodDaysStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodDaysStatus.setStatus("current")
_AlaQoSValidityPeriodMonths_Type = Integer32
_AlaQoSValidityPeriodMonths_Object = MibTableColumn
alaQoSValidityPeriodMonths = _AlaQoSValidityPeriodMonths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 5),
    _AlaQoSValidityPeriodMonths_Type()
)
alaQoSValidityPeriodMonths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodMonths.setStatus("current")


class _AlaQoSValidityPeriodMonthsStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodMonthsStatus based on Integer32"""
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


_AlaQoSValidityPeriodMonthsStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodMonthsStatus_Object = MibTableColumn
alaQoSValidityPeriodMonthsStatus = _AlaQoSValidityPeriodMonthsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 6),
    _AlaQoSValidityPeriodMonthsStatus_Type()
)
alaQoSValidityPeriodMonthsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodMonthsStatus.setStatus("current")


class _AlaQoSValidityPeriodHour_Type(DisplayString):
    """Custom type alaQoSValidityPeriodHour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSValidityPeriodHour_Type.__name__ = "DisplayString"
_AlaQoSValidityPeriodHour_Object = MibTableColumn
alaQoSValidityPeriodHour = _AlaQoSValidityPeriodHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 7),
    _AlaQoSValidityPeriodHour_Type()
)
alaQoSValidityPeriodHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodHour.setStatus("current")


class _AlaQoSValidityPeriodHourStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodHourStatus based on Integer32"""
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


_AlaQoSValidityPeriodHourStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodHourStatus_Object = MibTableColumn
alaQoSValidityPeriodHourStatus = _AlaQoSValidityPeriodHourStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 8),
    _AlaQoSValidityPeriodHourStatus_Type()
)
alaQoSValidityPeriodHourStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodHourStatus.setStatus("current")


class _AlaQoSValidityPeriodEndHour_Type(DisplayString):
    """Custom type alaQoSValidityPeriodEndHour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSValidityPeriodEndHour_Type.__name__ = "DisplayString"
_AlaQoSValidityPeriodEndHour_Object = MibTableColumn
alaQoSValidityPeriodEndHour = _AlaQoSValidityPeriodEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 9),
    _AlaQoSValidityPeriodEndHour_Type()
)
alaQoSValidityPeriodEndHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodEndHour.setStatus("current")


class _AlaQoSValidityPeriodInterval_Type(DisplayString):
    """Custom type alaQoSValidityPeriodInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSValidityPeriodInterval_Type.__name__ = "DisplayString"
_AlaQoSValidityPeriodInterval_Object = MibTableColumn
alaQoSValidityPeriodInterval = _AlaQoSValidityPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 10),
    _AlaQoSValidityPeriodInterval_Type()
)
alaQoSValidityPeriodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodInterval.setStatus("current")


class _AlaQoSValidityPeriodIntervalStatus_Type(Integer32):
    """Custom type alaQoSValidityPeriodIntervalStatus based on Integer32"""
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


_AlaQoSValidityPeriodIntervalStatus_Type.__name__ = "Integer32"
_AlaQoSValidityPeriodIntervalStatus_Object = MibTableColumn
alaQoSValidityPeriodIntervalStatus = _AlaQoSValidityPeriodIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 11),
    _AlaQoSValidityPeriodIntervalStatus_Type()
)
alaQoSValidityPeriodIntervalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodIntervalStatus.setStatus("current")


class _AlaQoSValidityPeriodEndInterval_Type(DisplayString):
    """Custom type alaQoSValidityPeriodEndInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSValidityPeriodEndInterval_Type.__name__ = "DisplayString"
_AlaQoSValidityPeriodEndInterval_Object = MibTableColumn
alaQoSValidityPeriodEndInterval = _AlaQoSValidityPeriodEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 12),
    _AlaQoSValidityPeriodEndInterval_Type()
)
alaQoSValidityPeriodEndInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodEndInterval.setStatus("current")
_AlaQoSValidityPeriodRowStatus_Type = RowStatus
_AlaQoSValidityPeriodRowStatus_Object = MibTableColumn
alaQoSValidityPeriodRowStatus = _AlaQoSValidityPeriodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 40, 1, 13),
    _AlaQoSValidityPeriodRowStatus_Type()
)
alaQoSValidityPeriodRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSValidityPeriodRowStatus.setStatus("current")
_AlaQoSAppliedValidityPeriodTable_Object = MibTable
alaQoSAppliedValidityPeriodTable = _AlaQoSAppliedValidityPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41)
)
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodTable.setStatus("current")
_AlaQoSAppliedValidityPeriodEntry_Object = MibTableRow
alaQoSAppliedValidityPeriodEntry = _AlaQoSAppliedValidityPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1)
)
alaQoSAppliedValidityPeriodEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedValidityPeriodName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodEntry.setStatus("current")


class _AlaQoSAppliedValidityPeriodName_Type(DisplayString):
    """Custom type alaQoSAppliedValidityPeriodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedValidityPeriodName_Type.__name__ = "DisplayString"
_AlaQoSAppliedValidityPeriodName_Object = MibTableColumn
alaQoSAppliedValidityPeriodName = _AlaQoSAppliedValidityPeriodName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 1),
    _AlaQoSAppliedValidityPeriodName_Type()
)
alaQoSAppliedValidityPeriodName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodName.setStatus("current")


class _AlaQoSAppliedValidityPeriodSource_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodSource based on Integer32"""
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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedValidityPeriodSource_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodSource_Object = MibTableColumn
alaQoSAppliedValidityPeriodSource = _AlaQoSAppliedValidityPeriodSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 2),
    _AlaQoSAppliedValidityPeriodSource_Type()
)
alaQoSAppliedValidityPeriodSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodSource.setStatus("current")
_AlaQoSAppliedValidityPeriodDays_Type = Integer32
_AlaQoSAppliedValidityPeriodDays_Object = MibTableColumn
alaQoSAppliedValidityPeriodDays = _AlaQoSAppliedValidityPeriodDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 3),
    _AlaQoSAppliedValidityPeriodDays_Type()
)
alaQoSAppliedValidityPeriodDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodDays.setStatus("current")


class _AlaQoSAppliedValidityPeriodDaysStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodDaysStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodDaysStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodDaysStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodDaysStatus = _AlaQoSAppliedValidityPeriodDaysStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 4),
    _AlaQoSAppliedValidityPeriodDaysStatus_Type()
)
alaQoSAppliedValidityPeriodDaysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodDaysStatus.setStatus("current")
_AlaQoSAppliedValidityPeriodMonths_Type = Integer32
_AlaQoSAppliedValidityPeriodMonths_Object = MibTableColumn
alaQoSAppliedValidityPeriodMonths = _AlaQoSAppliedValidityPeriodMonths_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 5),
    _AlaQoSAppliedValidityPeriodMonths_Type()
)
alaQoSAppliedValidityPeriodMonths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodMonths.setStatus("current")


class _AlaQoSAppliedValidityPeriodMonthsStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodMonthsStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodMonthsStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodMonthsStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodMonthsStatus = _AlaQoSAppliedValidityPeriodMonthsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 6),
    _AlaQoSAppliedValidityPeriodMonthsStatus_Type()
)
alaQoSAppliedValidityPeriodMonthsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodMonthsStatus.setStatus("current")


class _AlaQoSAppliedValidityPeriodHour_Type(DisplayString):
    """Custom type alaQoSAppliedValidityPeriodHour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSAppliedValidityPeriodHour_Type.__name__ = "DisplayString"
_AlaQoSAppliedValidityPeriodHour_Object = MibTableColumn
alaQoSAppliedValidityPeriodHour = _AlaQoSAppliedValidityPeriodHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 7),
    _AlaQoSAppliedValidityPeriodHour_Type()
)
alaQoSAppliedValidityPeriodHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodHour.setStatus("current")


class _AlaQoSAppliedValidityPeriodHourStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodHourStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodHourStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodHourStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodHourStatus = _AlaQoSAppliedValidityPeriodHourStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 8),
    _AlaQoSAppliedValidityPeriodHourStatus_Type()
)
alaQoSAppliedValidityPeriodHourStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodHourStatus.setStatus("current")


class _AlaQoSAppliedValidityPeriodEndHour_Type(DisplayString):
    """Custom type alaQoSAppliedValidityPeriodEndHour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AlaQoSAppliedValidityPeriodEndHour_Type.__name__ = "DisplayString"
_AlaQoSAppliedValidityPeriodEndHour_Object = MibTableColumn
alaQoSAppliedValidityPeriodEndHour = _AlaQoSAppliedValidityPeriodEndHour_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 9),
    _AlaQoSAppliedValidityPeriodEndHour_Type()
)
alaQoSAppliedValidityPeriodEndHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodEndHour.setStatus("current")


class _AlaQoSAppliedValidityPeriodInterval_Type(DisplayString):
    """Custom type alaQoSAppliedValidityPeriodInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSAppliedValidityPeriodInterval_Type.__name__ = "DisplayString"
_AlaQoSAppliedValidityPeriodInterval_Object = MibTableColumn
alaQoSAppliedValidityPeriodInterval = _AlaQoSAppliedValidityPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 10),
    _AlaQoSAppliedValidityPeriodInterval_Type()
)
alaQoSAppliedValidityPeriodInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodInterval.setStatus("current")


class _AlaQoSAppliedValidityPeriodIntervalStatus_Type(Integer32):
    """Custom type alaQoSAppliedValidityPeriodIntervalStatus based on Integer32"""
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


_AlaQoSAppliedValidityPeriodIntervalStatus_Type.__name__ = "Integer32"
_AlaQoSAppliedValidityPeriodIntervalStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodIntervalStatus = _AlaQoSAppliedValidityPeriodIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 11),
    _AlaQoSAppliedValidityPeriodIntervalStatus_Type()
)
alaQoSAppliedValidityPeriodIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodIntervalStatus.setStatus("current")


class _AlaQoSAppliedValidityPeriodEndInterval_Type(DisplayString):
    """Custom type alaQoSAppliedValidityPeriodEndInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AlaQoSAppliedValidityPeriodEndInterval_Type.__name__ = "DisplayString"
_AlaQoSAppliedValidityPeriodEndInterval_Object = MibTableColumn
alaQoSAppliedValidityPeriodEndInterval = _AlaQoSAppliedValidityPeriodEndInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 12),
    _AlaQoSAppliedValidityPeriodEndInterval_Type()
)
alaQoSAppliedValidityPeriodEndInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodEndInterval.setStatus("current")
_AlaQoSAppliedValidityPeriodRowStatus_Type = RowStatus
_AlaQoSAppliedValidityPeriodRowStatus_Object = MibTableColumn
alaQoSAppliedValidityPeriodRowStatus = _AlaQoSAppliedValidityPeriodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 41, 1, 13),
    _AlaQoSAppliedValidityPeriodRowStatus_Type()
)
alaQoSAppliedValidityPeriodRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedValidityPeriodRowStatus.setStatus("current")
_AlaQoSImportTable_Object = MibTable
alaQoSImportTable = _AlaQoSImportTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42)
)
if mibBuilder.loadTexts:
    alaQoSImportTable.setStatus("current")
_AlaQoSImportEntry_Object = MibTableRow
alaQoSImportEntry = _AlaQoSImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1)
)
alaQoSImportEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSImportIndex"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSImportText"),
)
if mibBuilder.loadTexts:
    alaQoSImportEntry.setStatus("current")
_AlaQoSImportIndex_Type = Integer32
_AlaQoSImportIndex_Object = MibTableColumn
alaQoSImportIndex = _AlaQoSImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 1),
    _AlaQoSImportIndex_Type()
)
alaQoSImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSImportIndex.setStatus("current")


class _AlaQoSImportText_Type(DisplayString):
    """Custom type alaQoSImportText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaQoSImportText_Type.__name__ = "DisplayString"
_AlaQoSImportText_Object = MibTableColumn
alaQoSImportText = _AlaQoSImportText_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 2),
    _AlaQoSImportText_Type()
)
alaQoSImportText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSImportText.setStatus("current")


class _AlaQoSImportPrecedence_Type(Integer32):
    """Custom type alaQoSImportPrecedence based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSImportPrecedence_Type.__name__ = "Integer32"
_AlaQoSImportPrecedence_Object = MibTableColumn
alaQoSImportPrecedence = _AlaQoSImportPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 3),
    _AlaQoSImportPrecedence_Type()
)
alaQoSImportPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSImportPrecedence.setStatus("current")


class _AlaQoSImportPrefix_Type(DisplayString):
    """Custom type alaQoSImportPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AlaQoSImportPrefix_Type.__name__ = "DisplayString"
_AlaQoSImportPrefix_Object = MibTableColumn
alaQoSImportPrefix = _AlaQoSImportPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 4),
    _AlaQoSImportPrefix_Type()
)
alaQoSImportPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSImportPrefix.setStatus("current")


class _AlaQoSImportSlot_Type(Integer32):
    """Custom type alaQoSImportSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSImportSlot_Type.__name__ = "Integer32"
_AlaQoSImportSlot_Object = MibTableColumn
alaQoSImportSlot = _AlaQoSImportSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 5),
    _AlaQoSImportSlot_Type()
)
alaQoSImportSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSImportSlot.setStatus("current")


class _AlaQoSImportPort_Type(Integer32):
    """Custom type alaQoSImportPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSImportPort_Type.__name__ = "Integer32"
_AlaQoSImportPort_Object = MibTableColumn
alaQoSImportPort = _AlaQoSImportPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 6),
    _AlaQoSImportPort_Type()
)
alaQoSImportPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSImportPort.setStatus("current")


class _AlaQoSImportPortend_Type(Integer32):
    """Custom type alaQoSImportPortend based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSImportPortend_Type.__name__ = "Integer32"
_AlaQoSImportPortend_Object = MibTableColumn
alaQoSImportPortend = _AlaQoSImportPortend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 7),
    _AlaQoSImportPortend_Type()
)
alaQoSImportPortend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSImportPortend.setStatus("current")


class _AlaQoSImportPortgroup_Type(DisplayString):
    """Custom type alaQoSImportPortgroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSImportPortgroup_Type.__name__ = "DisplayString"
_AlaQoSImportPortgroup_Object = MibTableColumn
alaQoSImportPortgroup = _AlaQoSImportPortgroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 8),
    _AlaQoSImportPortgroup_Type()
)
alaQoSImportPortgroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSImportPortgroup.setStatus("current")
_AlaQoSImportRowStatus_Type = RowStatus
_AlaQoSImportRowStatus_Object = MibTableColumn
alaQoSImportRowStatus = _AlaQoSImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 42, 1, 9),
    _AlaQoSImportRowStatus_Type()
)
alaQoSImportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSImportRowStatus.setStatus("current")
_AlaQoSAppliedImportTable_Object = MibTable
alaQoSAppliedImportTable = _AlaQoSAppliedImportTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43)
)
if mibBuilder.loadTexts:
    alaQoSAppliedImportTable.setStatus("current")
_AlaQoSAppliedImportEntry_Object = MibTableRow
alaQoSAppliedImportEntry = _AlaQoSAppliedImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1)
)
alaQoSAppliedImportEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedImportIndex"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedImportText"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedImportEntry.setStatus("current")
_AlaQoSAppliedImportIndex_Type = Integer32
_AlaQoSAppliedImportIndex_Object = MibTableColumn
alaQoSAppliedImportIndex = _AlaQoSAppliedImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 1),
    _AlaQoSAppliedImportIndex_Type()
)
alaQoSAppliedImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedImportIndex.setStatus("current")


class _AlaQoSAppliedImportText_Type(DisplayString):
    """Custom type alaQoSAppliedImportText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaQoSAppliedImportText_Type.__name__ = "DisplayString"
_AlaQoSAppliedImportText_Object = MibTableColumn
alaQoSAppliedImportText = _AlaQoSAppliedImportText_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 2),
    _AlaQoSAppliedImportText_Type()
)
alaQoSAppliedImportText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedImportText.setStatus("current")


class _AlaQoSAppliedImportPrecedence_Type(Integer32):
    """Custom type alaQoSAppliedImportPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaQoSAppliedImportPrecedence_Type.__name__ = "Integer32"
_AlaQoSAppliedImportPrecedence_Object = MibTableColumn
alaQoSAppliedImportPrecedence = _AlaQoSAppliedImportPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 3),
    _AlaQoSAppliedImportPrecedence_Type()
)
alaQoSAppliedImportPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedImportPrecedence.setStatus("current")


class _AlaQoSAppliedImportPrefix_Type(DisplayString):
    """Custom type alaQoSAppliedImportPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AlaQoSAppliedImportPrefix_Type.__name__ = "DisplayString"
_AlaQoSAppliedImportPrefix_Object = MibTableColumn
alaQoSAppliedImportPrefix = _AlaQoSAppliedImportPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 4),
    _AlaQoSAppliedImportPrefix_Type()
)
alaQoSAppliedImportPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedImportPrefix.setStatus("current")


class _AlaQoSAppliedImportSlot_Type(Integer32):
    """Custom type alaQoSAppliedImportSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AlaQoSAppliedImportSlot_Type.__name__ = "Integer32"
_AlaQoSAppliedImportSlot_Object = MibTableColumn
alaQoSAppliedImportSlot = _AlaQoSAppliedImportSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 5),
    _AlaQoSAppliedImportSlot_Type()
)
alaQoSAppliedImportSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedImportSlot.setStatus("current")


class _AlaQoSAppliedImportPort_Type(Integer32):
    """Custom type alaQoSAppliedImportPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedImportPort_Type.__name__ = "Integer32"
_AlaQoSAppliedImportPort_Object = MibTableColumn
alaQoSAppliedImportPort = _AlaQoSAppliedImportPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 6),
    _AlaQoSAppliedImportPort_Type()
)
alaQoSAppliedImportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedImportPort.setStatus("current")


class _AlaQoSAppliedImportPortend_Type(Integer32):
    """Custom type alaQoSAppliedImportPortend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaQoSAppliedImportPortend_Type.__name__ = "Integer32"
_AlaQoSAppliedImportPortend_Object = MibTableColumn
alaQoSAppliedImportPortend = _AlaQoSAppliedImportPortend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 7),
    _AlaQoSAppliedImportPortend_Type()
)
alaQoSAppliedImportPortend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedImportPortend.setStatus("current")


class _AlaQoSAppliedImportPortgroup_Type(DisplayString):
    """Custom type alaQoSAppliedImportPortgroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedImportPortgroup_Type.__name__ = "DisplayString"
_AlaQoSAppliedImportPortgroup_Object = MibTableColumn
alaQoSAppliedImportPortgroup = _AlaQoSAppliedImportPortgroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 8),
    _AlaQoSAppliedImportPortgroup_Type()
)
alaQoSAppliedImportPortgroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedImportPortgroup.setStatus("current")
_AlaQoSAppliedImportRowStatus_Type = RowStatus
_AlaQoSAppliedImportRowStatus_Object = MibTableColumn
alaQoSAppliedImportRowStatus = _AlaQoSAppliedImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 43, 1, 9),
    _AlaQoSAppliedImportRowStatus_Type()
)
alaQoSAppliedImportRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedImportRowStatus.setStatus("current")
_AlaQoSRuleGroupsTable_Object = MibTable
alaQoSRuleGroupsTable = _AlaQoSRuleGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 44)
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupsTable.setStatus("current")
_AlaQoSRuleGroupsEntry_Object = MibTableRow
alaQoSRuleGroupsEntry = _AlaQoSRuleGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 44, 1)
)
alaQoSRuleGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupsEntry.setStatus("current")


class _AlaQoSRuleGroupsName_Type(DisplayString):
    """Custom type alaQoSRuleGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleGroupsName_Type.__name__ = "DisplayString"
_AlaQoSRuleGroupsName_Object = MibTableColumn
alaQoSRuleGroupsName = _AlaQoSRuleGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 44, 1, 1),
    _AlaQoSRuleGroupsName_Type()
)
alaQoSRuleGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsName.setStatus("current")


class _AlaQoSRuleGroupsSource_Type(Integer32):
    """Custom type alaQoSRuleGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSRuleGroupsSource_Type.__name__ = "Integer32"
_AlaQoSRuleGroupsSource_Object = MibTableColumn
alaQoSRuleGroupsSource = _AlaQoSRuleGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 44, 1, 2),
    _AlaQoSRuleGroupsSource_Type()
)
alaQoSRuleGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsSource.setStatus("current")


class _AlaQoSRuleGroupsType_Type(Integer32):
    """Custom type alaQoSRuleGroupsType based on Integer32"""
    defaultValue = 2

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
        *(("default", 1),
          ("egress", 5),
          ("ingress", 4),
          ("slb", 6),
          ("unp", 2),
          ("vrf", 3))
    )


_AlaQoSRuleGroupsType_Type.__name__ = "Integer32"
_AlaQoSRuleGroupsType_Object = MibTableColumn
alaQoSRuleGroupsType = _AlaQoSRuleGroupsType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 44, 1, 3),
    _AlaQoSRuleGroupsType_Type()
)
alaQoSRuleGroupsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsType.setStatus("current")


class _AlaQoSRuleGroupsEnabled_Type(Integer32):
    """Custom type alaQoSRuleGroupsEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSRuleGroupsEnabled_Type.__name__ = "Integer32"
_AlaQoSRuleGroupsEnabled_Object = MibTableColumn
alaQoSRuleGroupsEnabled = _AlaQoSRuleGroupsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 44, 1, 4),
    _AlaQoSRuleGroupsEnabled_Type()
)
alaQoSRuleGroupsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsEnabled.setStatus("current")
_AlaQoSRuleGroupsStatus_Type = RowStatus
_AlaQoSRuleGroupsStatus_Object = MibTableColumn
alaQoSRuleGroupsStatus = _AlaQoSRuleGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 44, 1, 5),
    _AlaQoSRuleGroupsStatus_Type()
)
alaQoSRuleGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupsStatus.setStatus("current")
_AlaQoSAppliedRuleGroupsTable_Object = MibTable
alaQoSAppliedRuleGroupsTable = _AlaQoSAppliedRuleGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 45)
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsTable.setStatus("current")
_AlaQoSAppliedRuleGroupsEntry_Object = MibTableRow
alaQoSAppliedRuleGroupsEntry = _AlaQoSAppliedRuleGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 45, 1)
)
alaQoSAppliedRuleGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsEntry.setStatus("current")


class _AlaQoSAppliedRuleGroupsName_Type(DisplayString):
    """Custom type alaQoSAppliedRuleGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleGroupsName_Type.__name__ = "DisplayString"
_AlaQoSAppliedRuleGroupsName_Object = MibTableColumn
alaQoSAppliedRuleGroupsName = _AlaQoSAppliedRuleGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 45, 1, 1),
    _AlaQoSAppliedRuleGroupsName_Type()
)
alaQoSAppliedRuleGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsName.setStatus("current")


class _AlaQoSAppliedRuleGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedRuleGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupsSource_Object = MibTableColumn
alaQoSAppliedRuleGroupsSource = _AlaQoSAppliedRuleGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 45, 1, 2),
    _AlaQoSAppliedRuleGroupsSource_Type()
)
alaQoSAppliedRuleGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsSource.setStatus("current")


class _AlaQoSAppliedRuleGroupsType_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupsType based on Integer32"""
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
        *(("defualt", 1),
          ("egress", 5),
          ("ingress", 4),
          ("slb", 6),
          ("unp", 2),
          ("vrf", 3))
    )


_AlaQoSAppliedRuleGroupsType_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupsType_Object = MibTableColumn
alaQoSAppliedRuleGroupsType = _AlaQoSAppliedRuleGroupsType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 45, 1, 3),
    _AlaQoSAppliedRuleGroupsType_Type()
)
alaQoSAppliedRuleGroupsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsType.setStatus("current")


class _AlaQoSAppliedRuleGroupsEnabled_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaQoSAppliedRuleGroupsEnabled_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupsEnabled_Object = MibTableColumn
alaQoSAppliedRuleGroupsEnabled = _AlaQoSAppliedRuleGroupsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 45, 1, 4),
    _AlaQoSAppliedRuleGroupsEnabled_Type()
)
alaQoSAppliedRuleGroupsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsEnabled.setStatus("current")
_AlaQoSAppliedRuleGroupsStatus_Type = RowStatus
_AlaQoSAppliedRuleGroupsStatus_Object = MibTableColumn
alaQoSAppliedRuleGroupsStatus = _AlaQoSAppliedRuleGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 45, 1, 5),
    _AlaQoSAppliedRuleGroupsStatus_Type()
)
alaQoSAppliedRuleGroupsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupsStatus.setStatus("current")
_AlaQoSRuleGroupTable_Object = MibTable
alaQoSRuleGroupTable = _AlaQoSRuleGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46)
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupTable.setStatus("current")
_AlaQoSRuleGroupEntry_Object = MibTableRow
alaQoSRuleGroupEntry = _AlaQoSRuleGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46, 1)
)
alaQoSRuleGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSRuleGroupEntry.setStatus("current")


class _AlaQoSRuleGroupRuleName_Type(DisplayString):
    """Custom type alaQoSRuleGroupRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSRuleGroupRuleName_Type.__name__ = "DisplayString"
_AlaQoSRuleGroupRuleName_Object = MibTableColumn
alaQoSRuleGroupRuleName = _AlaQoSRuleGroupRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46, 1, 1),
    _AlaQoSRuleGroupRuleName_Type()
)
alaQoSRuleGroupRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSRuleGroupRuleName.setStatus("current")
_AlaQoSRuleGroupMatches_Type = Counter32
_AlaQoSRuleGroupMatches_Object = MibTableColumn
alaQoSRuleGroupMatches = _AlaQoSRuleGroupMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46, 1, 2),
    _AlaQoSRuleGroupMatches_Type()
)
alaQoSRuleGroupMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGroupMatches.setStatus("current")


class _AlaQoSRuleGroupCountType_Type(Integer32):
    """Custom type alaQoSRuleGroupCountType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 2),
          ("packets", 1))
    )


_AlaQoSRuleGroupCountType_Type.__name__ = "Integer32"
_AlaQoSRuleGroupCountType_Object = MibTableColumn
alaQoSRuleGroupCountType = _AlaQoSRuleGroupCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46, 1, 3),
    _AlaQoSRuleGroupCountType_Type()
)
alaQoSRuleGroupCountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupCountType.setStatus("current")
_AlaQoSRuleGroupPacketCount_Type = Counter64
_AlaQoSRuleGroupPacketCount_Object = MibTableColumn
alaQoSRuleGroupPacketCount = _AlaQoSRuleGroupPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46, 1, 4),
    _AlaQoSRuleGroupPacketCount_Type()
)
alaQoSRuleGroupPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGroupPacketCount.setStatus("current")
_AlaQoSRuleGroupByteCount_Type = Counter64
_AlaQoSRuleGroupByteCount_Object = MibTableColumn
alaQoSRuleGroupByteCount = _AlaQoSRuleGroupByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46, 1, 5),
    _AlaQoSRuleGroupByteCount_Type()
)
alaQoSRuleGroupByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSRuleGroupByteCount.setStatus("current")
_AlaQoSRuleGroupStatus_Type = RowStatus
_AlaQoSRuleGroupStatus_Object = MibTableColumn
alaQoSRuleGroupStatus = _AlaQoSRuleGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 46, 1, 6),
    _AlaQoSRuleGroupStatus_Type()
)
alaQoSRuleGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSRuleGroupStatus.setStatus("current")
_AlaQoSAppliedRuleGroupTable_Object = MibTable
alaQoSAppliedRuleGroupTable = _AlaQoSAppliedRuleGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47)
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupTable.setStatus("current")
_AlaQoSAppliedRuleGroupEntry_Object = MibTableRow
alaQoSAppliedRuleGroupEntry = _AlaQoSAppliedRuleGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47, 1)
)
alaQoSAppliedRuleGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupRuleName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupEntry.setStatus("current")


class _AlaQoSAppliedRuleGroupRuleName_Type(DisplayString):
    """Custom type alaQoSAppliedRuleGroupRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedRuleGroupRuleName_Type.__name__ = "DisplayString"
_AlaQoSAppliedRuleGroupRuleName_Object = MibTableColumn
alaQoSAppliedRuleGroupRuleName = _AlaQoSAppliedRuleGroupRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47, 1, 1),
    _AlaQoSAppliedRuleGroupRuleName_Type()
)
alaQoSAppliedRuleGroupRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupRuleName.setStatus("current")
_AlaQoSAppliedRuleGroupMatches_Type = Counter32
_AlaQoSAppliedRuleGroupMatches_Object = MibTableColumn
alaQoSAppliedRuleGroupMatches = _AlaQoSAppliedRuleGroupMatches_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47, 1, 2),
    _AlaQoSAppliedRuleGroupMatches_Type()
)
alaQoSAppliedRuleGroupMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupMatches.setStatus("current")


class _AlaQoSAppliedRuleGroupCountType_Type(Integer32):
    """Custom type alaQoSAppliedRuleGroupCountType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 2),
          ("packets", 1))
    )


_AlaQoSAppliedRuleGroupCountType_Type.__name__ = "Integer32"
_AlaQoSAppliedRuleGroupCountType_Object = MibTableColumn
alaQoSAppliedRuleGroupCountType = _AlaQoSAppliedRuleGroupCountType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47, 1, 3),
    _AlaQoSAppliedRuleGroupCountType_Type()
)
alaQoSAppliedRuleGroupCountType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupCountType.setStatus("current")
_AlaQoSAppliedRuleGroupPacketCount_Type = Counter64
_AlaQoSAppliedRuleGroupPacketCount_Object = MibTableColumn
alaQoSAppliedRuleGroupPacketCount = _AlaQoSAppliedRuleGroupPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47, 1, 4),
    _AlaQoSAppliedRuleGroupPacketCount_Type()
)
alaQoSAppliedRuleGroupPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupPacketCount.setStatus("current")
_AlaQoSAppliedRuleGroupByteCount_Type = Counter64
_AlaQoSAppliedRuleGroupByteCount_Object = MibTableColumn
alaQoSAppliedRuleGroupByteCount = _AlaQoSAppliedRuleGroupByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47, 1, 5),
    _AlaQoSAppliedRuleGroupByteCount_Type()
)
alaQoSAppliedRuleGroupByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupByteCount.setStatus("current")
_AlaQoSAppliedRuleGroupStatus_Type = RowStatus
_AlaQoSAppliedRuleGroupStatus_Object = MibTableColumn
alaQoSAppliedRuleGroupStatus = _AlaQoSAppliedRuleGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 47, 1, 6),
    _AlaQoSAppliedRuleGroupStatus_Type()
)
alaQoSAppliedRuleGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaQoSAppliedRuleGroupStatus.setStatus("current")
_AlaQoSVlanGroupsTable_Object = MibTable
alaQoSVlanGroupsTable = _AlaQoSVlanGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 48)
)
if mibBuilder.loadTexts:
    alaQoSVlanGroupsTable.setStatus("current")
_AlaQoSVlanGroupsEntry_Object = MibTableRow
alaQoSVlanGroupsEntry = _AlaQoSVlanGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 48, 1)
)
alaQoSVlanGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSVlanGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSVlanGroupsEntry.setStatus("current")


class _AlaQoSVlanGroupsName_Type(DisplayString):
    """Custom type alaQoSVlanGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSVlanGroupsName_Type.__name__ = "DisplayString"
_AlaQoSVlanGroupsName_Object = MibTableColumn
alaQoSVlanGroupsName = _AlaQoSVlanGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 48, 1, 1),
    _AlaQoSVlanGroupsName_Type()
)
alaQoSVlanGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSVlanGroupsName.setStatus("current")


class _AlaQoSVlanGroupsSource_Type(Integer32):
    """Custom type alaQoSVlanGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSVlanGroupsSource_Type.__name__ = "Integer32"
_AlaQoSVlanGroupsSource_Object = MibTableColumn
alaQoSVlanGroupsSource = _AlaQoSVlanGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 48, 1, 2),
    _AlaQoSVlanGroupsSource_Type()
)
alaQoSVlanGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSVlanGroupsSource.setStatus("current")
_AlaQoSVlanGroupsStatus_Type = RowStatus
_AlaQoSVlanGroupsStatus_Object = MibTableColumn
alaQoSVlanGroupsStatus = _AlaQoSVlanGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 48, 1, 3),
    _AlaQoSVlanGroupsStatus_Type()
)
alaQoSVlanGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSVlanGroupsStatus.setStatus("current")
_AlaQoSAppliedVlanGroupsTable_Object = MibTable
alaQoSAppliedVlanGroupsTable = _AlaQoSAppliedVlanGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 49)
)
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupsTable.setStatus("current")
_AlaQoSAppliedVlanGroupsEntry_Object = MibTableRow
alaQoSAppliedVlanGroupsEntry = _AlaQoSAppliedVlanGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 49, 1)
)
alaQoSAppliedVlanGroupsEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedVlanGroupsName"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupsEntry.setStatus("current")


class _AlaQoSAppliedVlanGroupsName_Type(DisplayString):
    """Custom type alaQoSAppliedVlanGroupsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaQoSAppliedVlanGroupsName_Type.__name__ = "DisplayString"
_AlaQoSAppliedVlanGroupsName_Object = MibTableColumn
alaQoSAppliedVlanGroupsName = _AlaQoSAppliedVlanGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 49, 1, 1),
    _AlaQoSAppliedVlanGroupsName_Type()
)
alaQoSAppliedVlanGroupsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupsName.setStatus("current")


class _AlaQoSAppliedVlanGroupsSource_Type(Integer32):
    """Custom type alaQoSAppliedVlanGroupsSource based on Integer32"""
    defaultValue = 2

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
        *(("api", 4),
          ("blt", 3),
          ("cli", 2),
          ("imp", 5),
          ("ldap", 1))
    )


_AlaQoSAppliedVlanGroupsSource_Type.__name__ = "Integer32"
_AlaQoSAppliedVlanGroupsSource_Object = MibTableColumn
alaQoSAppliedVlanGroupsSource = _AlaQoSAppliedVlanGroupsSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 49, 1, 2),
    _AlaQoSAppliedVlanGroupsSource_Type()
)
alaQoSAppliedVlanGroupsSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupsSource.setStatus("current")
_AlaQoSAppliedVlanGroupsStatus_Type = RowStatus
_AlaQoSAppliedVlanGroupsStatus_Object = MibTableColumn
alaQoSAppliedVlanGroupsStatus = _AlaQoSAppliedVlanGroupsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 49, 1, 3),
    _AlaQoSAppliedVlanGroupsStatus_Type()
)
alaQoSAppliedVlanGroupsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupsStatus.setStatus("current")
_AlaQoSVlanGroupTable_Object = MibTable
alaQoSVlanGroupTable = _AlaQoSVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 50)
)
if mibBuilder.loadTexts:
    alaQoSVlanGroupTable.setStatus("current")
_AlaQoSVlanGroupEntry_Object = MibTableRow
alaQoSVlanGroupEntry = _AlaQoSVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 50, 1)
)
alaQoSVlanGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSVlanGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSVlanGroupVlan"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSVlanGroupVlanEnd"),
)
if mibBuilder.loadTexts:
    alaQoSVlanGroupEntry.setStatus("current")


class _AlaQoSVlanGroupVlan_Type(Integer32):
    """Custom type alaQoSVlanGroupVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaQoSVlanGroupVlan_Type.__name__ = "Integer32"
_AlaQoSVlanGroupVlan_Object = MibTableColumn
alaQoSVlanGroupVlan = _AlaQoSVlanGroupVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 50, 1, 1),
    _AlaQoSVlanGroupVlan_Type()
)
alaQoSVlanGroupVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSVlanGroupVlan.setStatus("current")


class _AlaQoSVlanGroupVlanEnd_Type(Integer32):
    """Custom type alaQoSVlanGroupVlanEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaQoSVlanGroupVlanEnd_Type.__name__ = "Integer32"
_AlaQoSVlanGroupVlanEnd_Object = MibTableColumn
alaQoSVlanGroupVlanEnd = _AlaQoSVlanGroupVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 50, 1, 2),
    _AlaQoSVlanGroupVlanEnd_Type()
)
alaQoSVlanGroupVlanEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSVlanGroupVlanEnd.setStatus("current")
_AlaQoSVlanGroupStatus_Type = RowStatus
_AlaQoSVlanGroupStatus_Object = MibTableColumn
alaQoSVlanGroupStatus = _AlaQoSVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 50, 1, 3),
    _AlaQoSVlanGroupStatus_Type()
)
alaQoSVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSVlanGroupStatus.setStatus("current")
_AlaQoSAppliedVlanGroupTable_Object = MibTable
alaQoSAppliedVlanGroupTable = _AlaQoSAppliedVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 51)
)
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupTable.setStatus("current")
_AlaQoSAppliedVlanGroupEntry_Object = MibTableRow
alaQoSAppliedVlanGroupEntry = _AlaQoSAppliedVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 51, 1)
)
alaQoSAppliedVlanGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedVlanGroupsName"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedVlanGroupVlan"),
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSAppliedVlanGroupVlanEnd"),
)
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupEntry.setStatus("current")


class _AlaQoSAppliedVlanGroupVlan_Type(Integer32):
    """Custom type alaQoSAppliedVlanGroupVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AlaQoSAppliedVlanGroupVlan_Type.__name__ = "Integer32"
_AlaQoSAppliedVlanGroupVlan_Object = MibTableColumn
alaQoSAppliedVlanGroupVlan = _AlaQoSAppliedVlanGroupVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 51, 1, 1),
    _AlaQoSAppliedVlanGroupVlan_Type()
)
alaQoSAppliedVlanGroupVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupVlan.setStatus("current")


class _AlaQoSAppliedVlanGroupVlanEnd_Type(Integer32):
    """Custom type alaQoSAppliedVlanGroupVlanEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AlaQoSAppliedVlanGroupVlanEnd_Type.__name__ = "Integer32"
_AlaQoSAppliedVlanGroupVlanEnd_Object = MibTableColumn
alaQoSAppliedVlanGroupVlanEnd = _AlaQoSAppliedVlanGroupVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 51, 1, 2),
    _AlaQoSAppliedVlanGroupVlanEnd_Type()
)
alaQoSAppliedVlanGroupVlanEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupVlanEnd.setStatus("current")
_AlaQoSAppliedVlanGroupStatus_Type = RowStatus
_AlaQoSAppliedVlanGroupStatus_Object = MibTableColumn
alaQoSAppliedVlanGroupStatus = _AlaQoSAppliedVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 51, 1, 3),
    _AlaQoSAppliedVlanGroupStatus_Type()
)
alaQoSAppliedVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupStatus.setStatus("current")
_AlaQoSHwLoopbackProfileTable_Object = MibTable
alaQoSHwLoopbackProfileTable = _AlaQoSHwLoopbackProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52)
)
if mibBuilder.loadTexts:
    alaQoSHwLoopbackProfileTable.setStatus("current")
_AlaQoSHwLoopbackProfileEntry_Object = MibTableRow
alaQoSHwLoopbackProfileEntry = _AlaQoSHwLoopbackProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1)
)
alaQoSHwLoopbackProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackProfileName"),
)
if mibBuilder.loadTexts:
    alaQoSHwLoopbackProfileEntry.setStatus("current")


class _AlaQoSHwLoopbackProfileName_Type(DisplayString):
    """Custom type alaQoSHwLoopbackProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaQoSHwLoopbackProfileName_Type.__name__ = "DisplayString"
_AlaQoSHwLoopbackProfileName_Object = MibTableColumn
alaQoSHwLoopbackProfileName = _AlaQoSHwLoopbackProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 1),
    _AlaQoSHwLoopbackProfileName_Type()
)
alaQoSHwLoopbackProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackProfileName.setStatus("current")


class _AlaQoSHwLoopbackSourceMac_Type(MacAddress):
    """Custom type alaQoSHwLoopbackSourceMac based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSHwLoopbackSourceMac_Object = MibTableColumn
alaQoSHwLoopbackSourceMac = _AlaQoSHwLoopbackSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 2),
    _AlaQoSHwLoopbackSourceMac_Type()
)
alaQoSHwLoopbackSourceMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackSourceMac.setStatus("current")


class _AlaQoSHwLoopbackDestinationMac_Type(MacAddress):
    """Custom type alaQoSHwLoopbackDestinationMac based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaQoSHwLoopbackDestinationMac_Object = MibTableColumn
alaQoSHwLoopbackDestinationMac = _AlaQoSHwLoopbackDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 3),
    _AlaQoSHwLoopbackDestinationMac_Type()
)
alaQoSHwLoopbackDestinationMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackDestinationMac.setStatus("current")


class _AlaQoSHwLoopbackVlan_Type(Integer32):
    """Custom type alaQoSHwLoopbackVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaQoSHwLoopbackVlan_Type.__name__ = "Integer32"
_AlaQoSHwLoopbackVlan_Object = MibTableColumn
alaQoSHwLoopbackVlan = _AlaQoSHwLoopbackVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 4),
    _AlaQoSHwLoopbackVlan_Type()
)
alaQoSHwLoopbackVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackVlan.setStatus("current")
_AlaQoSHwLoopbackPort_Type = InterfaceIndex
_AlaQoSHwLoopbackPort_Object = MibTableColumn
alaQoSHwLoopbackPort = _AlaQoSHwLoopbackPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 5),
    _AlaQoSHwLoopbackPort_Type()
)
alaQoSHwLoopbackPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackPort.setStatus("current")


class _AlaQoSHwLoopbackType_Type(Integer32):
    """Custom type alaQoSHwLoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inward", 1),
          ("outward", 2))
    )


_AlaQoSHwLoopbackType_Type.__name__ = "Integer32"
_AlaQoSHwLoopbackType_Object = MibTableColumn
alaQoSHwLoopbackType = _AlaQoSHwLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 6),
    _AlaQoSHwLoopbackType_Type()
)
alaQoSHwLoopbackType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackType.setStatus("current")


class _AlaQoSHwLoopbackProfileStatus_Type(Integer32):
    """Custom type alaQoSHwLoopbackProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 0),
          ("start", 1),
          ("stop", 2))
    )


_AlaQoSHwLoopbackProfileStatus_Type.__name__ = "Integer32"
_AlaQoSHwLoopbackProfileStatus_Object = MibTableColumn
alaQoSHwLoopbackProfileStatus = _AlaQoSHwLoopbackProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 7),
    _AlaQoSHwLoopbackProfileStatus_Type()
)
alaQoSHwLoopbackProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackProfileStatus.setStatus("current")
_AlaQoSHwLoopbackProfileRowStatus_Type = RowStatus
_AlaQoSHwLoopbackProfileRowStatus_Object = MibTableColumn
alaQoSHwLoopbackProfileRowStatus = _AlaQoSHwLoopbackProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 1, 52, 1, 8),
    _AlaQoSHwLoopbackProfileRowStatus_Type()
)
alaQoSHwLoopbackProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaQoSHwLoopbackProfileRowStatus.setStatus("current")
_AlaQoSMIBConformance_ObjectIdentity = ObjectIdentity
alaQoSMIBConformance = _AlaQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    alaQoSMIBConformance.setStatus("current")
_AlaQoSMIBGroups_ObjectIdentity = ObjectIdentity
alaQoSMIBGroups = _AlaQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaQoSMIBGroups.setStatus("current")
_AlaQoSMIBCompliances_ObjectIdentity = ObjectIdentity
alaQoSMIBCompliances = _AlaQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaQoSMIBCompliances.setStatus("current")

# Managed Objects groups

alaQoSMIBRuleObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 1)
)
alaQoSMIBRuleObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSRuleEnabled"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRulePrecedence"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleCondition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleAction"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleReflexive"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleSave"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleLog"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleMatches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleEnforced"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleActive"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleValidityPeriod"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleValidityPeriodStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleLogInterval"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleCountType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRulePacketCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleByteCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleExcessPacketCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleExcessByteCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleTrapEvents"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleDefaultList"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGreenCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleYellowCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleRedCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleNonGreenCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleNonRedCount"))
)
if mibBuilder.loadTexts:
    alaQoSMIBRuleObjects.setStatus("current")

alaQoSMIBAppliedRuleObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 2)
)
alaQoSMIBAppliedRuleObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleEnabled"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRulePrecedence"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleCondition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleAction"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleReflexive"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleSave"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleLog"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleMatches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleEnforced"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleActive"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleValidityPeriod"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleValidityPeriodStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleLogInterval"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleCountType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRulePacketCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleByteCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleExcessPacketCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleExcessByteCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleTrapEvents"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleDefaultList"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGreenCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleYellowCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleRedCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleNonGreenCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleNonRedCount"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedRuleObjects.setStatus("current")

alaQoSMIBConditionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 3)
)
alaQoSMIBConditionObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceSlotStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourcePort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourcePortGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourcePortGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationSlotStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationPortGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationPortGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceInterfaceType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceInterfaceTypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationInterfaceType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationInterfaceTypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceMacAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceMacAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceMacMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceMacGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceMacGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationMacAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationMacAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationMacMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationMacGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationMacGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceVlan"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceVlanStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationVlan"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationVlanStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSCondition8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSCondition8021pStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMulticastIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMulticastIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMulticastIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMulticastNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMulticastNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTos"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTosStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTosMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDscp"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDscpStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDscpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIpProtocol"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIpProtocolStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionService"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionServiceStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionServiceGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionServiceGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIcmpType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIcmpTypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIcmpCode"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIcmpCodeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDlci"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDlciStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourcePortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceUdpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationUdpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionEthertype"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionEthertypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTcpFlags"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTcpFlagsStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTcpFlagsVal"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTcpFlagsValStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTcpFlagsMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTcpFlagsMaskStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionTcpEstablished"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpv6Addr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpv6AddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceIpv6Mask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpv6Addr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpv6AddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDestinationIpv6Mask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIpv6Traffic"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIpv6NH"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIpv6NHStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIpv6FlowLabel"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionIpv6FlowLabelStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMcastIpv6Addr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMcastIpv6AddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionMcastIpv6Mask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionDscpEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionInnerSourceVlan"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionInnerSourceVlanStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionInner8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionInner8021pStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionVrfName"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionVrfNameStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSCondition8021pEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionInner8021pEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceVlanGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionSourceVlanGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionInnerSourceVlanGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConditionInnerSourceVlanGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBConditionObjects.setStatus("current")

alaQoSMIBAppliedConditionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 4)
)
alaQoSMIBAppliedConditionObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceSlotStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourcePort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourcePortGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourcePortGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationSlotStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationPortGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationPortGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceInterfaceType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceInterfaceTypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationInterfaceType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationInterfaceTypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceMacAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceMacAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceMacMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceMacGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceMacGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationMacAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationMacAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationMacMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationMacGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationMacGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceVlan"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceVlanStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationVlan"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationVlanStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedCondition8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedCondition8021pStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMulticastIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMulticastIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMulticastIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMulticastNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMulticastNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTos"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTosStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTosMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDscp"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDscpStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDscpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIpProtocol"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIpProtocolStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionService"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionServiceStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionServiceGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionServiceGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIcmpType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIcmpTypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIcmpCode"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIcmpCodeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDlci"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDlciStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourcePortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceUdpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationUdpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionEthertype"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionEthertypeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTcpFlags"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsVal"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsValStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTcpFlagsMaskStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionTcpEstablished"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpv6Addr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpv6AddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceIpv6Mask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpv6Addr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpv6AddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDestinationIpv6Mask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIpv6Traffic"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIpv6NH"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIpv6NHStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIpv6FlowLabel"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionIpv6FlowLabelStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMcastIpv6Addr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMcastIpv6AddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionMcastIpv6Mask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionDscpEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionInnerSourceVlan"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionInnerSourceVlanStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionInner8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionInner8021pStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionVrfName"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionVrfNameStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedCondition8021pEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionInner8021pEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceVlanGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionSourceVlanGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionInnerSourceVlanGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedConditionInnerSourceVlanGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedConditionObjects.setStatus("current")

alaQoSMIBServiceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 5)
)
alaQoSMIBServiceObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceProtocol"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceSourceUdpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceDestinationUdpPortEnd"))
)
if mibBuilder.loadTexts:
    alaQoSMIBServiceObjects.setStatus("current")

alaQoSMIBAppliedServiceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 6)
)
alaQoSMIBAppliedServiceObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceProtocol"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationIpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationIpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationIpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationTcpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationTcpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationTcpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceSourceUdpPortEnd"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationUdpPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationUdpPortStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceDestinationUdpPortEnd"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedServiceObjects.setStatus("current")

alaQoSMIBServiceGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 7)
)
alaQoSMIBServiceGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSServiceGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBServiceGroupsObjects.setStatus("current")

alaQoSMIBAppliedServiceGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 8)
)
alaQoSMIBAppliedServiceGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedServiceGroupsObjects.setStatus("current")

alaQoSMIBServiceGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 9)
)
alaQoSMIBServiceGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSServiceGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBServiceGroupObjects.setStatus("current")

alaQoSMIBAppliedServiceGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 10)
)
alaQoSMIBAppliedServiceGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedServiceGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedServiceGroupObjects.setStatus("current")

alaQoSMIBNetworkGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 11)
)
alaQoSMIBNetworkGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSNetworkGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSNetworkGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBNetworkGroupsObjects.setStatus("current")

alaQoSMIBAppliedNetworkGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 12)
)
alaQoSMIBAppliedNetworkGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedNetworkGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedNetworkGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedNetworkGroupsObjects.setStatus("current")

alaQoSMIBNetworkGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 13)
)
alaQoSMIBNetworkGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSNetworkGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBNetworkGroupObjects.setStatus("current")

alaQoSMIBAppliedNetworkGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 14)
)
alaQoSMIBAppliedNetworkGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedNetworkGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedNetworkGroupObjects.setStatus("current")

alaQoSMIBMACGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 15)
)
alaQoSMIBMACGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSMACGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSMACGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBMACGroupsObjects.setStatus("current")

alaQoSMIBAppliedMACGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 16)
)
alaQoSMIBAppliedMACGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMACGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMACGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMACGroupsObjects.setStatus("current")

alaQoSMIBMACGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 17)
)
alaQoSMIBMACGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSMACGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBMACGroupObjects.setStatus("current")

alaQoSMIBAppliedMACGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 18)
)
alaQoSMIBAppliedMACGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMACGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMACGroupObjects.setStatus("current")

alaQoSMIBPortGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 19)
)
alaQoSMIBPortGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBPortGroupsObjects.setStatus("current")

alaQoSMIBAppliedPortGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 20)
)
alaQoSMIBAppliedPortGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedPortGroupsObjects.setStatus("current")

alaQoSMIBPortGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 21)
)
alaQoSMIBPortGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSPortGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBPortGroupObjects.setStatus("current")

alaQoSMIBAppliedPortGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 22)
)
alaQoSMIBAppliedPortGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedPortGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedPortGroupObjects.setStatus("current")

alaQoSMIBMapGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 23)
)
alaQoSMIBMapGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBMapGroupsObjects.setStatus("current")

alaQoSMIBAppliedMapGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 24)
)
alaQoSMIBAppliedMapGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMapGroupsObjects.setStatus("current")

alaQoSMIBMapGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 25)
)
alaQoSMIBMapGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSMapGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBMapGroupObjects.setStatus("current")

alaQoSMIBAppliedMapGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 26)
)
alaQoSMIBAppliedMapGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedMapGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedMapGroupObjects.setStatus("current")

alaQoSMIBActionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 27)
)
alaQoSMIBActionObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSActionSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDropAlgorithm"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionWredMaximumThreshold"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionWredMaximumThresholdStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionWredMinimumThreshold"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionWredMinimumThresholdStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionWredMaximumProbability"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionWredMaximumProbabilityStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPeakBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPeakBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPriority"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPriorityStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionShared"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionJitter"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionJitterStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionLatency"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionLatencyStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMaximumDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMaximumDepthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMaximumBuffers"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMaximumBuffersStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAction8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAction8021pStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionTos"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionTosStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDscp"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDscpStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMapFrom"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMapTo"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMapGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMapGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionSourceRewriteIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionSourceRewriteIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionSourceRewriteIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionSourceRewriteNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionSourceRewriteNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDestinationRewriteIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDestinationRewriteIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDestinationRewriteIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDestinationRewriteNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionDestinationRewriteNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionLoadBalanceGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionLoadBalanceGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPermanentGatewayIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPermanentGatewayIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionAlternateGatewayIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionAlternateGatewayIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMinimumDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMinimumDepthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionVPNAccess"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionNocache"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPortdisable"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionRedirectSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionRedirectSlotStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionRedirectPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionRedirectAgg"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionRedirectAggStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMirrorSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMirrorPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMirrorMode"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionMirrorModeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionCIR"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionCIRStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionCBS"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionCBSStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPIR"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPIRStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPBS"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionPBSStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSActionCounterColor"))
)
if mibBuilder.loadTexts:
    alaQoSMIBActionObjects.setStatus("current")

alaQoSMIBAppliedActionObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 28)
)
alaQoSMIBAppliedActionObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDropAlgorithm"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionWredMaximumThreshold"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionWredMaximumThresholdStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionWredMinimumThreshold"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionWredMinimumThresholdStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionWredMaximumProbability"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionWredMaximumProbabilityStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPeakBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPeakBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPriority"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPriorityStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionShared"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionJitter"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionJitterStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionLatency"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionLatencyStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMaximumDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMaximumDepthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMaximumBuffers"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMaximumBuffersStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedAction8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedAction8021pStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionTos"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionTosStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDscp"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDscpStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMapFrom"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMapTo"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMapGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMapGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionSourceRewriteIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionSourceRewriteIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionSourceRewriteIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionSourceRewriteNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionSourceRewriteNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDestinationRewriteIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDestinationRewriteIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDestinationRewriteIpMask"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDestinationRewriteNetworkGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionDestinationRewriteNetworkGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionLoadBalanceGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionLoadBalanceGroupStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPermanentGatewayIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPermanentGatewayIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionAlternateGatewayIpAddr"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionAlternateGatewayIpAddrStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMinimumDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMinimumDepthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionVPNAccess"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionNocache"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPortdisable"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionRedirectSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionRedirectSlotStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionRedirectPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionRedirectAgg"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionRedirectAggStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMirrorSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMirrorPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMirrorMode"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionMirrorModeStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionCIR"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionCIRStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionCBS"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionCBSStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPIR"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPIRStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPBS"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionPBSStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedActionCounterColor"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedActionObjects.setStatus("current")

alaQoSMIBPortObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 29)
)
alaQoSMIBPortObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnabled"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedEnabled"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortInterfaceType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortTrusted"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefault8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefaultDSCP"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumReservedBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumReservedBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumReservedBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumReservedBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumSignalledBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumSignalledBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumSignalledBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumSignalledBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefaultQueues"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedDefaultQueues"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumDefaultBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumDefaultBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumDefaultBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumDefaultBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumDefaultDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumDefaultDepthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumDefaultDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumDefaultDepthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumDefaultBuffers"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumDefaultBuffersStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumDefaultBuffers"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortAppliedMaximumDefaultBuffersStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortReset"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortPhysicalBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortReservedBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortSignalledBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCurrentBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefaultQidLow"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefaultQidMedium"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefaultQidHigh"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefaultQidUrgent"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFloodQid"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQueues"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQueuesCreated"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQueuesFailed"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQueuesPreempted"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortRowStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio0EnqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio0DeqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio0EnqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio0DeqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio0QidDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio0WredDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio0OverflowDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio1EnqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio1DeqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio1EnqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio1DeqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio1QidDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio1WredDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio1OverflowDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio2EnqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio2DeqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio2EnqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio2DeqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio2QidDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio2WredDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio2OverflowDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio3EnqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio3DeqBytes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio3EnqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio3DeqPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio3QidDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio3WredDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFirPrio3OverflowDiscardPkts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDefaultClassification"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortLowPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMediumPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortHighPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortUrgentPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP0Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP0Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP1Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP1Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP2Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP2Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP3Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdP3Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortEnqueuingThresholdStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortServicingMode"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortHighDensity"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFreeFFPRules"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortUsedFFPRules"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortFreeFFPMasks"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortUsedFFPMasks"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortSpoofedCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortNonSpoofedCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQ4PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQ5PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQ6PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortQ7PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS0MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS0MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS1MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS1MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS2MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS2MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS3MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS3MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS4MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS4MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS5MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS5MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS6MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS6MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS7MaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS7MaximumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS0MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS0MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS1MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS1MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS2MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS2MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS3MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS3MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS4MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS4MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS5MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS5MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS6MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS6MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS7MinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortCOS7MinimumBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumIngBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMaximumIngBandwidthStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDEIMarking"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortMonitor"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSPortDEIMapping"))
)
if mibBuilder.loadTexts:
    alaQoSMIBPortObjects.setStatus("current")

alaQoSMIBConfigObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 30)
)
alaQoSMIBConfigObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSConfigEnabled"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigDefaultQueues"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedDefaultQueues"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigTrustPorts"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigFlowTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedFlowTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigFragmentTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedFragmentTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigReflexiveTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedReflfexiveTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigNatTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedNatTimeout"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigClassifyl3Bridged"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedClassifyl3Bridged"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigClassifyFragments"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedClassifyFragments"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigDefaultBridgedDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedDefaultBridgedDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigDefaultRoutedDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedDefaultRoutedDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigDefaultMulticastDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedDefaultMulticastDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigStatsInterval"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigLogLines"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigLogLevel"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigLogConsole"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigForwardLog"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigClearLog"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigApply"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigRevert"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigReset"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigStatsReset"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigFlush"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigDebug"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigServicingMode"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigLowPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigMediumPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigHighPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigUrgentPriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigQ4PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigQ5PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigQ6PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigQ7PriorityWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigUserportFilter"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedUserportFilter"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigUserportShutdown"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAppliedUserportShutdown"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAutoNMS"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigAutoPhones"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigQMPage"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigQMMACGroup"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigQMPath"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigDEIMapping"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigDEIMarking"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSConfigStatsResetEgress"))
)
if mibBuilder.loadTexts:
    alaQoSMIBConfigObjects.setStatus("current")

alaQoSMIBStatsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 31)
)
alaQoSMIBStatsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL2Events"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL2Matches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL2Drops"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL3IngressEvents"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL3IngressMatches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL3IngressDrops"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL3EgressEvents"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL3EgressMatches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsL3EgressDrops"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsMulticastEvents"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsMulticastMatches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsMulticastDrops"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsFragments"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsBadFragments"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsUnknownFragments"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsReflexiveFlows"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsReflexiveCorrections"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsLoadBalanceFlows"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsClassifierMaxNodes"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsClassifierMaxDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsFlowLookups"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsFlowHits"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsSentNIMessages"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsReceivedNIMessages"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsFailedNIMessages"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsSpoofedEvents"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsNonSpoofedEvents"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSStatsDropServicesEvents"))
)
if mibBuilder.loadTexts:
    alaQoSMIBStatsObjects.setStatus("current")

alaQoSMIBQueueObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 32)
)
alaQoSMIBQueueObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSQueueSlot"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueuePort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueuePortId"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueuePriority"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueMinimumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueMaximumBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueAverageBandwidth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueMinimumDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueMaximumDepth"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueMaximumBuffers"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueue8021p"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueuePacketsSent"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueuePacketsDropped"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueMaxLength"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueAverageLength"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueCurrentLength"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSQueueAction"))
)
if mibBuilder.loadTexts:
    alaQoSMIBQueueObjects.setStatus("current")

alaQoSMIBSlotObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 33)
)
alaQoSMIBSlotObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSSlotType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotMaxBuffers"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotFreeBuffers1"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotFreeBuffers2"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold1Low"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold1Medium"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold1High"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold1Urgent"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold2Low"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold2Medium"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold2High"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotThreshold2Urgent"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotBuffersDenied"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotBuffersDeniedAverage"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotBuffersDropped"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotBuffersDroppedAverage"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP0Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP0Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP1Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP1Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP2Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP2Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP3Lower"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdP3Upper"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredAverageCounterWeight"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotWredThresholdStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotCbqThresholdMode"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotCbqThresholdP1"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotCbqThresholdP2"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotCbqThresholdP3"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSSlotHighDensity"))
)
if mibBuilder.loadTexts:
    alaQoSMIBSlotObjects.setStatus("current")

alaQoSMIBClassifyObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 34)
)
alaQoSMIBClassifyObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyExecute"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyL2SourceResultRule"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyL2SourceResultDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyL2DestinationResultRule"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyL2DestinationResultDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyL3ResultRule"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyL3ResultDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyIGMPResultRule"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyIGMPResultDisposition"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyMulticastResultRule"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSClassifyMulticastResultDisposition"))
)
if mibBuilder.loadTexts:
    alaQoSMIBClassifyObjects.setStatus("current")

alaQoSMIBRuleGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 35)
)
alaQoSMIBRuleGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupsType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupsEnabled"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBRuleGroupsObjects.setStatus("current")

alaQoSMIBAppliedRuleGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 36)
)
alaQoSMIBAppliedRuleGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupsType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupsEnabled"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedRuleGroupsObjects.setStatus("current")

alaQoSMIBRuleGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 37)
)
alaQoSMIBRuleGroupObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupMatches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupCountType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupPacketCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupByteCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSRuleGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBRuleGroupObjects.setStatus("current")

alaQoSMIBAppliedRuleGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 38)
)
alaQoSMIBAppliedRuleGroupObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupMatches"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupCountType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupPacketCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupByteCount"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedRuleGroupStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBAppliedRuleGroupObjects.setStatus("current")

alaQoSVlanGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 39)
)
alaQoSVlanGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSVlanGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSVlanGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSVlanGroupsObjects.setStatus("current")

alaQoSAppliedVlanGroupsObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 40)
)
alaQoSAppliedVlanGroupsObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedVlanGroupsSource"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedVlanGroupsStatus"))
)
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupsObjects.setStatus("current")

alaQoSVlanGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 41)
)
alaQoSVlanGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSVlanGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSVlanGroupObjects.setStatus("current")

alaQoSAppliedVlanGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 42)
)
alaQoSAppliedVlanGroupObjects.setObjects(
    ("ALCATEL-IND1-QOS-MIB", "alaQoSAppliedVlanGroupStatus")
)
if mibBuilder.loadTexts:
    alaQoSAppliedVlanGroupObjects.setStatus("current")

alaQoSMIBHwLoopBackProfileObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 1, 43)
)
alaQoSMIBHwLoopBackProfileObjects.setObjects(
      *(("ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackSourceMac"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackDestinationMac"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackVlan"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackPort"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackType"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackProfileStatus"),
        ("ALCATEL-IND1-QOS-MIB", "alaQoSHwLoopbackProfileRowStatus"))
)
if mibBuilder.loadTexts:
    alaQoSMIBHwLoopBackProfileObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 22, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alaQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-QOS-MIB",
    **{"alaQoSMIB": alaQoSMIB,
       "alaQoSMIBObjects": alaQoSMIBObjects,
       "alaQoSRuleTable": alaQoSRuleTable,
       "alaQoSRuleEntry": alaQoSRuleEntry,
       "alaQoSRuleName": alaQoSRuleName,
       "alaQoSRuleEnabled": alaQoSRuleEnabled,
       "alaQoSRuleSource": alaQoSRuleSource,
       "alaQoSRulePrecedence": alaQoSRulePrecedence,
       "alaQoSRuleCondition": alaQoSRuleCondition,
       "alaQoSRuleAction": alaQoSRuleAction,
       "alaQoSRuleReflexive": alaQoSRuleReflexive,
       "alaQoSRuleSave": alaQoSRuleSave,
       "alaQoSRuleLog": alaQoSRuleLog,
       "alaQoSRuleMatches": alaQoSRuleMatches,
       "alaQoSRuleEnforced": alaQoSRuleEnforced,
       "alaQoSRuleActive": alaQoSRuleActive,
       "alaQoSRuleRowStatus": alaQoSRuleRowStatus,
       "alaQoSRuleValidityPeriod": alaQoSRuleValidityPeriod,
       "alaQoSRuleValidityPeriodStatus": alaQoSRuleValidityPeriodStatus,
       "alaQoSRuleLogInterval": alaQoSRuleLogInterval,
       "alaQoSRuleCountType": alaQoSRuleCountType,
       "alaQoSRulePacketCount": alaQoSRulePacketCount,
       "alaQoSRuleByteCount": alaQoSRuleByteCount,
       "alaQoSRuleExcessPacketCount": alaQoSRuleExcessPacketCount,
       "alaQoSRuleExcessByteCount": alaQoSRuleExcessByteCount,
       "alaQoSRuleType": alaQoSRuleType,
       "alaQoSRuleTrapEvents": alaQoSRuleTrapEvents,
       "alaQoSRuleDefaultList": alaQoSRuleDefaultList,
       "alaQoSRuleGreenCount": alaQoSRuleGreenCount,
       "alaQoSRuleYellowCount": alaQoSRuleYellowCount,
       "alaQoSRuleRedCount": alaQoSRuleRedCount,
       "alaQoSRuleNonGreenCount": alaQoSRuleNonGreenCount,
       "alaQoSRuleNonRedCount": alaQoSRuleNonRedCount,
       "alaQoSAppliedRuleTable": alaQoSAppliedRuleTable,
       "alaQoSAppliedRuleEntry": alaQoSAppliedRuleEntry,
       "alaQoSAppliedRuleName": alaQoSAppliedRuleName,
       "alaQoSAppliedRuleEnabled": alaQoSAppliedRuleEnabled,
       "alaQoSAppliedRuleSource": alaQoSAppliedRuleSource,
       "alaQoSAppliedRulePrecedence": alaQoSAppliedRulePrecedence,
       "alaQoSAppliedRuleCondition": alaQoSAppliedRuleCondition,
       "alaQoSAppliedRuleAction": alaQoSAppliedRuleAction,
       "alaQoSAppliedRuleReflexive": alaQoSAppliedRuleReflexive,
       "alaQoSAppliedRuleSave": alaQoSAppliedRuleSave,
       "alaQoSAppliedRuleLog": alaQoSAppliedRuleLog,
       "alaQoSAppliedRuleMatches": alaQoSAppliedRuleMatches,
       "alaQoSAppliedRuleEnforced": alaQoSAppliedRuleEnforced,
       "alaQoSAppliedRuleActive": alaQoSAppliedRuleActive,
       "alaQoSAppliedRuleRowStatus": alaQoSAppliedRuleRowStatus,
       "alaQoSAppliedRuleValidityPeriod": alaQoSAppliedRuleValidityPeriod,
       "alaQoSAppliedRuleValidityPeriodStatus": alaQoSAppliedRuleValidityPeriodStatus,
       "alaQoSAppliedRuleLogInterval": alaQoSAppliedRuleLogInterval,
       "alaQoSAppliedRuleCountType": alaQoSAppliedRuleCountType,
       "alaQoSAppliedRulePacketCount": alaQoSAppliedRulePacketCount,
       "alaQoSAppliedRuleByteCount": alaQoSAppliedRuleByteCount,
       "alaQoSAppliedRuleExcessPacketCount": alaQoSAppliedRuleExcessPacketCount,
       "alaQoSAppliedRuleExcessByteCount": alaQoSAppliedRuleExcessByteCount,
       "alaQoSAppliedRuleType": alaQoSAppliedRuleType,
       "alaQoSAppliedRuleTrapEvents": alaQoSAppliedRuleTrapEvents,
       "alaQoSAppliedRuleDefaultList": alaQoSAppliedRuleDefaultList,
       "alaQoSAppliedRuleGreenCount": alaQoSAppliedRuleGreenCount,
       "alaQoSAppliedRuleYellowCount": alaQoSAppliedRuleYellowCount,
       "alaQoSAppliedRuleRedCount": alaQoSAppliedRuleRedCount,
       "alaQoSAppliedRuleNonGreenCount": alaQoSAppliedRuleNonGreenCount,
       "alaQoSAppliedRuleNonRedCount": alaQoSAppliedRuleNonRedCount,
       "alaQoSConditionTable": alaQoSConditionTable,
       "alaQoSConditionEntry": alaQoSConditionEntry,
       "alaQoSConditionName": alaQoSConditionName,
       "alaQoSConditionSource": alaQoSConditionSource,
       "alaQoSConditionSourceSlot": alaQoSConditionSourceSlot,
       "alaQoSConditionSourceSlotStatus": alaQoSConditionSourceSlotStatus,
       "alaQoSConditionSourcePort": alaQoSConditionSourcePort,
       "alaQoSConditionSourcePortGroup": alaQoSConditionSourcePortGroup,
       "alaQoSConditionSourcePortGroupStatus": alaQoSConditionSourcePortGroupStatus,
       "alaQoSConditionDestinationSlot": alaQoSConditionDestinationSlot,
       "alaQoSConditionDestinationSlotStatus": alaQoSConditionDestinationSlotStatus,
       "alaQoSConditionDestinationPort": alaQoSConditionDestinationPort,
       "alaQoSConditionDestinationPortGroup": alaQoSConditionDestinationPortGroup,
       "alaQoSConditionDestinationPortGroupStatus": alaQoSConditionDestinationPortGroupStatus,
       "alaQoSConditionSourceInterfaceType": alaQoSConditionSourceInterfaceType,
       "alaQoSConditionSourceInterfaceTypeStatus": alaQoSConditionSourceInterfaceTypeStatus,
       "alaQoSConditionDestinationInterfaceType": alaQoSConditionDestinationInterfaceType,
       "alaQoSConditionDestinationInterfaceTypeStatus": alaQoSConditionDestinationInterfaceTypeStatus,
       "alaQoSConditionSourceMacAddr": alaQoSConditionSourceMacAddr,
       "alaQoSConditionSourceMacAddrStatus": alaQoSConditionSourceMacAddrStatus,
       "alaQoSConditionSourceMacMask": alaQoSConditionSourceMacMask,
       "alaQoSConditionSourceMacGroup": alaQoSConditionSourceMacGroup,
       "alaQoSConditionSourceMacGroupStatus": alaQoSConditionSourceMacGroupStatus,
       "alaQoSConditionDestinationMacAddr": alaQoSConditionDestinationMacAddr,
       "alaQoSConditionDestinationMacAddrStatus": alaQoSConditionDestinationMacAddrStatus,
       "alaQoSConditionDestinationMacMask": alaQoSConditionDestinationMacMask,
       "alaQoSConditionDestinationMacGroup": alaQoSConditionDestinationMacGroup,
       "alaQoSConditionDestinationMacGroupStatus": alaQoSConditionDestinationMacGroupStatus,
       "alaQoSConditionSourceVlan": alaQoSConditionSourceVlan,
       "alaQoSConditionSourceVlanStatus": alaQoSConditionSourceVlanStatus,
       "alaQoSConditionDestinationVlan": alaQoSConditionDestinationVlan,
       "alaQoSConditionDestinationVlanStatus": alaQoSConditionDestinationVlanStatus,
       "alaQoSCondition8021p": alaQoSCondition8021p,
       "alaQoSCondition8021pStatus": alaQoSCondition8021pStatus,
       "alaQoSConditionSourceIpAddr": alaQoSConditionSourceIpAddr,
       "alaQoSConditionSourceIpAddrStatus": alaQoSConditionSourceIpAddrStatus,
       "alaQoSConditionSourceIpMask": alaQoSConditionSourceIpMask,
       "alaQoSConditionSourceNetworkGroup": alaQoSConditionSourceNetworkGroup,
       "alaQoSConditionSourceNetworkGroupStatus": alaQoSConditionSourceNetworkGroupStatus,
       "alaQoSConditionDestinationIpAddr": alaQoSConditionDestinationIpAddr,
       "alaQoSConditionDestinationIpAddrStatus": alaQoSConditionDestinationIpAddrStatus,
       "alaQoSConditionDestinationIpMask": alaQoSConditionDestinationIpMask,
       "alaQoSConditionDestinationNetworkGroup": alaQoSConditionDestinationNetworkGroup,
       "alaQoSConditionDestinationNetworkGroupStatus": alaQoSConditionDestinationNetworkGroupStatus,
       "alaQoSConditionMulticastIpAddr": alaQoSConditionMulticastIpAddr,
       "alaQoSConditionMulticastIpAddrStatus": alaQoSConditionMulticastIpAddrStatus,
       "alaQoSConditionMulticastIpMask": alaQoSConditionMulticastIpMask,
       "alaQoSConditionMulticastNetworkGroup": alaQoSConditionMulticastNetworkGroup,
       "alaQoSConditionMulticastNetworkGroupStatus": alaQoSConditionMulticastNetworkGroupStatus,
       "alaQoSConditionTos": alaQoSConditionTos,
       "alaQoSConditionTosStatus": alaQoSConditionTosStatus,
       "alaQoSConditionTosMask": alaQoSConditionTosMask,
       "alaQoSConditionDscp": alaQoSConditionDscp,
       "alaQoSConditionDscpStatus": alaQoSConditionDscpStatus,
       "alaQoSConditionDscpMask": alaQoSConditionDscpMask,
       "alaQoSConditionIpProtocol": alaQoSConditionIpProtocol,
       "alaQoSConditionIpProtocolStatus": alaQoSConditionIpProtocolStatus,
       "alaQoSConditionSourceIpPort": alaQoSConditionSourceIpPort,
       "alaQoSConditionSourceIpPortStatus": alaQoSConditionSourceIpPortStatus,
       "alaQoSConditionDestinationIpPort": alaQoSConditionDestinationIpPort,
       "alaQoSConditionDestinationIpPortStatus": alaQoSConditionDestinationIpPortStatus,
       "alaQoSConditionService": alaQoSConditionService,
       "alaQoSConditionServiceStatus": alaQoSConditionServiceStatus,
       "alaQoSConditionServiceGroup": alaQoSConditionServiceGroup,
       "alaQoSConditionServiceGroupStatus": alaQoSConditionServiceGroupStatus,
       "alaQoSConditionIcmpType": alaQoSConditionIcmpType,
       "alaQoSConditionIcmpTypeStatus": alaQoSConditionIcmpTypeStatus,
       "alaQoSConditionIcmpCode": alaQoSConditionIcmpCode,
       "alaQoSConditionIcmpCodeStatus": alaQoSConditionIcmpCodeStatus,
       "alaQoSConditionDlci": alaQoSConditionDlci,
       "alaQoSConditionDlciStatus": alaQoSConditionDlciStatus,
       "alaQoSConditionRowStatus": alaQoSConditionRowStatus,
       "alaQoSConditionSourcePortEnd": alaQoSConditionSourcePortEnd,
       "alaQoSConditionDestinationPortEnd": alaQoSConditionDestinationPortEnd,
       "alaQoSConditionSourceIpPortEnd": alaQoSConditionSourceIpPortEnd,
       "alaQoSConditionDestinationIpPortEnd": alaQoSConditionDestinationIpPortEnd,
       "alaQoSConditionSourceTcpPort": alaQoSConditionSourceTcpPort,
       "alaQoSConditionSourceTcpPortStatus": alaQoSConditionSourceTcpPortStatus,
       "alaQoSConditionSourceTcpPortEnd": alaQoSConditionSourceTcpPortEnd,
       "alaQoSConditionDestinationTcpPort": alaQoSConditionDestinationTcpPort,
       "alaQoSConditionDestinationTcpPortStatus": alaQoSConditionDestinationTcpPortStatus,
       "alaQoSConditionDestinationTcpPortEnd": alaQoSConditionDestinationTcpPortEnd,
       "alaQoSConditionSourceUdpPort": alaQoSConditionSourceUdpPort,
       "alaQoSConditionSourceUdpPortStatus": alaQoSConditionSourceUdpPortStatus,
       "alaQoSConditionSourceUdpPortEnd": alaQoSConditionSourceUdpPortEnd,
       "alaQoSConditionDestinationUdpPort": alaQoSConditionDestinationUdpPort,
       "alaQoSConditionDestinationUdpPortStatus": alaQoSConditionDestinationUdpPortStatus,
       "alaQoSConditionDestinationUdpPortEnd": alaQoSConditionDestinationUdpPortEnd,
       "alaQoSConditionEthertype": alaQoSConditionEthertype,
       "alaQoSConditionEthertypeStatus": alaQoSConditionEthertypeStatus,
       "alaQoSConditionTcpFlags": alaQoSConditionTcpFlags,
       "alaQoSConditionTcpFlagsStatus": alaQoSConditionTcpFlagsStatus,
       "alaQoSConditionTcpFlagsVal": alaQoSConditionTcpFlagsVal,
       "alaQoSConditionTcpFlagsValStatus": alaQoSConditionTcpFlagsValStatus,
       "alaQoSConditionTcpFlagsMask": alaQoSConditionTcpFlagsMask,
       "alaQoSConditionTcpFlagsMaskStatus": alaQoSConditionTcpFlagsMaskStatus,
       "alaQoSConditionTcpEstablished": alaQoSConditionTcpEstablished,
       "alaQoSConditionSourceIpv6Addr": alaQoSConditionSourceIpv6Addr,
       "alaQoSConditionSourceIpv6AddrStatus": alaQoSConditionSourceIpv6AddrStatus,
       "alaQoSConditionSourceIpv6Mask": alaQoSConditionSourceIpv6Mask,
       "alaQoSConditionDestinationIpv6Addr": alaQoSConditionDestinationIpv6Addr,
       "alaQoSConditionDestinationIpv6AddrStatus": alaQoSConditionDestinationIpv6AddrStatus,
       "alaQoSConditionDestinationIpv6Mask": alaQoSConditionDestinationIpv6Mask,
       "alaQoSConditionIpv6Traffic": alaQoSConditionIpv6Traffic,
       "alaQoSConditionIpv6NH": alaQoSConditionIpv6NH,
       "alaQoSConditionIpv6NHStatus": alaQoSConditionIpv6NHStatus,
       "alaQoSConditionIpv6FlowLabel": alaQoSConditionIpv6FlowLabel,
       "alaQoSConditionIpv6FlowLabelStatus": alaQoSConditionIpv6FlowLabelStatus,
       "alaQoSConditionMcastIpv6Addr": alaQoSConditionMcastIpv6Addr,
       "alaQoSConditionMcastIpv6AddrStatus": alaQoSConditionMcastIpv6AddrStatus,
       "alaQoSConditionMcastIpv6Mask": alaQoSConditionMcastIpv6Mask,
       "alaQoSConditionDscpEnd": alaQoSConditionDscpEnd,
       "alaQoSConditionInnerSourceVlan": alaQoSConditionInnerSourceVlan,
       "alaQoSConditionInnerSourceVlanStatus": alaQoSConditionInnerSourceVlanStatus,
       "alaQoSConditionInner8021p": alaQoSConditionInner8021p,
       "alaQoSConditionInner8021pStatus": alaQoSConditionInner8021pStatus,
       "alaQoSConditionVrfName": alaQoSConditionVrfName,
       "alaQoSConditionVrfNameStatus": alaQoSConditionVrfNameStatus,
       "alaQoSCondition8021pEnd": alaQoSCondition8021pEnd,
       "alaQoSConditionInner8021pEnd": alaQoSConditionInner8021pEnd,
       "alaQoSConditionSourceVlanGroup": alaQoSConditionSourceVlanGroup,
       "alaQoSConditionSourceVlanGroupStatus": alaQoSConditionSourceVlanGroupStatus,
       "alaQoSConditionInnerSourceVlanGroup": alaQoSConditionInnerSourceVlanGroup,
       "alaQoSConditionInnerSourceVlanGroupStatus": alaQoSConditionInnerSourceVlanGroupStatus,
       "alaQoSAppliedConditionTable": alaQoSAppliedConditionTable,
       "alaQoSAppliedConditionEntry": alaQoSAppliedConditionEntry,
       "alaQoSAppliedConditionName": alaQoSAppliedConditionName,
       "alaQoSAppliedConditionSource": alaQoSAppliedConditionSource,
       "alaQoSAppliedConditionSourceSlot": alaQoSAppliedConditionSourceSlot,
       "alaQoSAppliedConditionSourceSlotStatus": alaQoSAppliedConditionSourceSlotStatus,
       "alaQoSAppliedConditionSourcePort": alaQoSAppliedConditionSourcePort,
       "alaQoSAppliedConditionSourcePortGroup": alaQoSAppliedConditionSourcePortGroup,
       "alaQoSAppliedConditionSourcePortGroupStatus": alaQoSAppliedConditionSourcePortGroupStatus,
       "alaQoSAppliedConditionDestinationSlot": alaQoSAppliedConditionDestinationSlot,
       "alaQoSAppliedConditionDestinationSlotStatus": alaQoSAppliedConditionDestinationSlotStatus,
       "alaQoSAppliedConditionDestinationPort": alaQoSAppliedConditionDestinationPort,
       "alaQoSAppliedConditionDestinationPortGroup": alaQoSAppliedConditionDestinationPortGroup,
       "alaQoSAppliedConditionDestinationPortGroupStatus": alaQoSAppliedConditionDestinationPortGroupStatus,
       "alaQoSAppliedConditionSourceInterfaceType": alaQoSAppliedConditionSourceInterfaceType,
       "alaQoSAppliedConditionSourceInterfaceTypeStatus": alaQoSAppliedConditionSourceInterfaceTypeStatus,
       "alaQoSAppliedConditionDestinationInterfaceType": alaQoSAppliedConditionDestinationInterfaceType,
       "alaQoSAppliedConditionDestinationInterfaceTypeStatus": alaQoSAppliedConditionDestinationInterfaceTypeStatus,
       "alaQoSAppliedConditionSourceMacAddr": alaQoSAppliedConditionSourceMacAddr,
       "alaQoSAppliedConditionSourceMacAddrStatus": alaQoSAppliedConditionSourceMacAddrStatus,
       "alaQoSAppliedConditionSourceMacMask": alaQoSAppliedConditionSourceMacMask,
       "alaQoSAppliedConditionSourceMacGroup": alaQoSAppliedConditionSourceMacGroup,
       "alaQoSAppliedConditionSourceMacGroupStatus": alaQoSAppliedConditionSourceMacGroupStatus,
       "alaQoSAppliedConditionDestinationMacAddr": alaQoSAppliedConditionDestinationMacAddr,
       "alaQoSAppliedConditionDestinationMacAddrStatus": alaQoSAppliedConditionDestinationMacAddrStatus,
       "alaQoSAppliedConditionDestinationMacMask": alaQoSAppliedConditionDestinationMacMask,
       "alaQoSAppliedConditionDestinationMacGroup": alaQoSAppliedConditionDestinationMacGroup,
       "alaQoSAppliedConditionDestinationMacGroupStatus": alaQoSAppliedConditionDestinationMacGroupStatus,
       "alaQoSAppliedConditionSourceVlan": alaQoSAppliedConditionSourceVlan,
       "alaQoSAppliedConditionSourceVlanStatus": alaQoSAppliedConditionSourceVlanStatus,
       "alaQoSAppliedConditionDestinationVlan": alaQoSAppliedConditionDestinationVlan,
       "alaQoSAppliedConditionDestinationVlanStatus": alaQoSAppliedConditionDestinationVlanStatus,
       "alaQoSAppliedCondition8021p": alaQoSAppliedCondition8021p,
       "alaQoSAppliedCondition8021pStatus": alaQoSAppliedCondition8021pStatus,
       "alaQoSAppliedConditionSourceIpAddr": alaQoSAppliedConditionSourceIpAddr,
       "alaQoSAppliedConditionSourceIpAddrStatus": alaQoSAppliedConditionSourceIpAddrStatus,
       "alaQoSAppliedConditionSourceIpMask": alaQoSAppliedConditionSourceIpMask,
       "alaQoSAppliedConditionSourceNetworkGroup": alaQoSAppliedConditionSourceNetworkGroup,
       "alaQoSAppliedConditionSourceNetworkGroupStatus": alaQoSAppliedConditionSourceNetworkGroupStatus,
       "alaQoSAppliedConditionDestinationIpAddr": alaQoSAppliedConditionDestinationIpAddr,
       "alaQoSAppliedConditionDestinationIpAddrStatus": alaQoSAppliedConditionDestinationIpAddrStatus,
       "alaQoSAppliedConditionDestinationIpMask": alaQoSAppliedConditionDestinationIpMask,
       "alaQoSAppliedConditionDestinationNetworkGroup": alaQoSAppliedConditionDestinationNetworkGroup,
       "alaQoSAppliedConditionDestinationNetworkGroupStatus": alaQoSAppliedConditionDestinationNetworkGroupStatus,
       "alaQoSAppliedConditionMulticastIpAddr": alaQoSAppliedConditionMulticastIpAddr,
       "alaQoSAppliedConditionMulticastIpAddrStatus": alaQoSAppliedConditionMulticastIpAddrStatus,
       "alaQoSAppliedConditionMulticastIpMask": alaQoSAppliedConditionMulticastIpMask,
       "alaQoSAppliedConditionMulticastNetworkGroup": alaQoSAppliedConditionMulticastNetworkGroup,
       "alaQoSAppliedConditionMulticastNetworkGroupStatus": alaQoSAppliedConditionMulticastNetworkGroupStatus,
       "alaQoSAppliedConditionTos": alaQoSAppliedConditionTos,
       "alaQoSAppliedConditionTosStatus": alaQoSAppliedConditionTosStatus,
       "alaQoSAppliedConditionTosMask": alaQoSAppliedConditionTosMask,
       "alaQoSAppliedConditionDscp": alaQoSAppliedConditionDscp,
       "alaQoSAppliedConditionDscpStatus": alaQoSAppliedConditionDscpStatus,
       "alaQoSAppliedConditionDscpMask": alaQoSAppliedConditionDscpMask,
       "alaQoSAppliedConditionIpProtocol": alaQoSAppliedConditionIpProtocol,
       "alaQoSAppliedConditionIpProtocolStatus": alaQoSAppliedConditionIpProtocolStatus,
       "alaQoSAppliedConditionSourceIpPort": alaQoSAppliedConditionSourceIpPort,
       "alaQoSAppliedConditionSourceIpPortStatus": alaQoSAppliedConditionSourceIpPortStatus,
       "alaQoSAppliedConditionDestinationIpPort": alaQoSAppliedConditionDestinationIpPort,
       "alaQoSAppliedConditionDestinationIpPortStatus": alaQoSAppliedConditionDestinationIpPortStatus,
       "alaQoSAppliedConditionService": alaQoSAppliedConditionService,
       "alaQoSAppliedConditionServiceStatus": alaQoSAppliedConditionServiceStatus,
       "alaQoSAppliedConditionServiceGroup": alaQoSAppliedConditionServiceGroup,
       "alaQoSAppliedConditionServiceGroupStatus": alaQoSAppliedConditionServiceGroupStatus,
       "alaQoSAppliedConditionIcmpType": alaQoSAppliedConditionIcmpType,
       "alaQoSAppliedConditionIcmpTypeStatus": alaQoSAppliedConditionIcmpTypeStatus,
       "alaQoSAppliedConditionIcmpCode": alaQoSAppliedConditionIcmpCode,
       "alaQoSAppliedConditionIcmpCodeStatus": alaQoSAppliedConditionIcmpCodeStatus,
       "alaQoSAppliedConditionDlci": alaQoSAppliedConditionDlci,
       "alaQoSAppliedConditionDlciStatus": alaQoSAppliedConditionDlciStatus,
       "alaQoSAppliedConditionRowStatus": alaQoSAppliedConditionRowStatus,
       "alaQoSAppliedConditionSourcePortEnd": alaQoSAppliedConditionSourcePortEnd,
       "alaQoSAppliedConditionDestinationPortEnd": alaQoSAppliedConditionDestinationPortEnd,
       "alaQoSAppliedConditionSourceIpPortEnd": alaQoSAppliedConditionSourceIpPortEnd,
       "alaQoSAppliedConditionDestinationIpPortEnd": alaQoSAppliedConditionDestinationIpPortEnd,
       "alaQoSAppliedConditionSourceTcpPort": alaQoSAppliedConditionSourceTcpPort,
       "alaQoSAppliedConditionSourceTcpPortStatus": alaQoSAppliedConditionSourceTcpPortStatus,
       "alaQoSAppliedConditionSourceTcpPortEnd": alaQoSAppliedConditionSourceTcpPortEnd,
       "alaQoSAppliedConditionDestinationTcpPort": alaQoSAppliedConditionDestinationTcpPort,
       "alaQoSAppliedConditionDestinationTcpPortStatus": alaQoSAppliedConditionDestinationTcpPortStatus,
       "alaQoSAppliedConditionDestinationTcpPortEnd": alaQoSAppliedConditionDestinationTcpPortEnd,
       "alaQoSAppliedConditionSourceUdpPort": alaQoSAppliedConditionSourceUdpPort,
       "alaQoSAppliedConditionSourceUdpPortStatus": alaQoSAppliedConditionSourceUdpPortStatus,
       "alaQoSAppliedConditionSourceUdpPortEnd": alaQoSAppliedConditionSourceUdpPortEnd,
       "alaQoSAppliedConditionDestinationUdpPort": alaQoSAppliedConditionDestinationUdpPort,
       "alaQoSAppliedConditionDestinationUdpPortStatus": alaQoSAppliedConditionDestinationUdpPortStatus,
       "alaQoSAppliedConditionDestinationUdpPortEnd": alaQoSAppliedConditionDestinationUdpPortEnd,
       "alaQoSAppliedConditionEthertype": alaQoSAppliedConditionEthertype,
       "alaQoSAppliedConditionEthertypeStatus": alaQoSAppliedConditionEthertypeStatus,
       "alaQoSAppliedConditionTcpFlags": alaQoSAppliedConditionTcpFlags,
       "alaQoSAppliedConditionTcpFlagsStatus": alaQoSAppliedConditionTcpFlagsStatus,
       "alaQoSAppliedConditionTcpFlagsVal": alaQoSAppliedConditionTcpFlagsVal,
       "alaQoSAppliedConditionTcpFlagsValStatus": alaQoSAppliedConditionTcpFlagsValStatus,
       "alaQoSAppliedConditionTcpFlagsMask": alaQoSAppliedConditionTcpFlagsMask,
       "alaQoSAppliedConditionTcpFlagsMaskStatus": alaQoSAppliedConditionTcpFlagsMaskStatus,
       "alaQoSAppliedConditionTcpEstablished": alaQoSAppliedConditionTcpEstablished,
       "alaQoSAppliedConditionSourceIpv6Addr": alaQoSAppliedConditionSourceIpv6Addr,
       "alaQoSAppliedConditionSourceIpv6AddrStatus": alaQoSAppliedConditionSourceIpv6AddrStatus,
       "alaQoSAppliedConditionSourceIpv6Mask": alaQoSAppliedConditionSourceIpv6Mask,
       "alaQoSAppliedConditionDestinationIpv6Addr": alaQoSAppliedConditionDestinationIpv6Addr,
       "alaQoSAppliedConditionDestinationIpv6AddrStatus": alaQoSAppliedConditionDestinationIpv6AddrStatus,
       "alaQoSAppliedConditionDestinationIpv6Mask": alaQoSAppliedConditionDestinationIpv6Mask,
       "alaQoSAppliedConditionIpv6Traffic": alaQoSAppliedConditionIpv6Traffic,
       "alaQoSAppliedConditionIpv6NH": alaQoSAppliedConditionIpv6NH,
       "alaQoSAppliedConditionIpv6NHStatus": alaQoSAppliedConditionIpv6NHStatus,
       "alaQoSAppliedConditionIpv6FlowLabel": alaQoSAppliedConditionIpv6FlowLabel,
       "alaQoSAppliedConditionIpv6FlowLabelStatus": alaQoSAppliedConditionIpv6FlowLabelStatus,
       "alaQoSAppliedConditionMcastIpv6Addr": alaQoSAppliedConditionMcastIpv6Addr,
       "alaQoSAppliedConditionMcastIpv6AddrStatus": alaQoSAppliedConditionMcastIpv6AddrStatus,
       "alaQoSAppliedConditionMcastIpv6Mask": alaQoSAppliedConditionMcastIpv6Mask,
       "alaQoSAppliedConditionDscpEnd": alaQoSAppliedConditionDscpEnd,
       "alaQoSAppliedConditionInnerSourceVlan": alaQoSAppliedConditionInnerSourceVlan,
       "alaQoSAppliedConditionInnerSourceVlanStatus": alaQoSAppliedConditionInnerSourceVlanStatus,
       "alaQoSAppliedConditionInner8021p": alaQoSAppliedConditionInner8021p,
       "alaQoSAppliedConditionInner8021pStatus": alaQoSAppliedConditionInner8021pStatus,
       "alaQoSAppliedConditionVrfName": alaQoSAppliedConditionVrfName,
       "alaQoSAppliedConditionVrfNameStatus": alaQoSAppliedConditionVrfNameStatus,
       "alaQoSAppliedCondition8021pEnd": alaQoSAppliedCondition8021pEnd,
       "alaQoSAppliedConditionInner8021pEnd": alaQoSAppliedConditionInner8021pEnd,
       "alaQoSAppliedConditionSourceVlanGroup": alaQoSAppliedConditionSourceVlanGroup,
       "alaQoSAppliedConditionSourceVlanGroupStatus": alaQoSAppliedConditionSourceVlanGroupStatus,
       "alaQoSAppliedConditionInnerSourceVlanGroup": alaQoSAppliedConditionInnerSourceVlanGroup,
       "alaQoSAppliedConditionInnerSourceVlanGroupStatus": alaQoSAppliedConditionInnerSourceVlanGroupStatus,
       "alaQoSServiceTable": alaQoSServiceTable,
       "alaQoSServiceEntry": alaQoSServiceEntry,
       "alaQoSServiceName": alaQoSServiceName,
       "alaQoSServiceSource": alaQoSServiceSource,
       "alaQoSServiceProtocol": alaQoSServiceProtocol,
       "alaQoSServiceSourceIpPort": alaQoSServiceSourceIpPort,
       "alaQoSServiceSourceIpPortStatus": alaQoSServiceSourceIpPortStatus,
       "alaQoSServiceDestinationIpPort": alaQoSServiceDestinationIpPort,
       "alaQoSServiceDestinationIpPortStatus": alaQoSServiceDestinationIpPortStatus,
       "alaQoSServiceRowStatus": alaQoSServiceRowStatus,
       "alaQoSServiceSourceIpPortEnd": alaQoSServiceSourceIpPortEnd,
       "alaQoSServiceDestinationIpPortEnd": alaQoSServiceDestinationIpPortEnd,
       "alaQoSServiceSourceTcpPort": alaQoSServiceSourceTcpPort,
       "alaQoSServiceSourceTcpPortStatus": alaQoSServiceSourceTcpPortStatus,
       "alaQoSServiceSourceTcpPortEnd": alaQoSServiceSourceTcpPortEnd,
       "alaQoSServiceDestinationTcpPort": alaQoSServiceDestinationTcpPort,
       "alaQoSServiceDestinationTcpPortStatus": alaQoSServiceDestinationTcpPortStatus,
       "alaQoSServiceDestinationTcpPortEnd": alaQoSServiceDestinationTcpPortEnd,
       "alaQoSServiceSourceUdpPort": alaQoSServiceSourceUdpPort,
       "alaQoSServiceSourceUdpPortStatus": alaQoSServiceSourceUdpPortStatus,
       "alaQoSServiceSourceUdpPortEnd": alaQoSServiceSourceUdpPortEnd,
       "alaQoSServiceDestinationUdpPort": alaQoSServiceDestinationUdpPort,
       "alaQoSServiceDestinationUdpPortStatus": alaQoSServiceDestinationUdpPortStatus,
       "alaQoSServiceDestinationUdpPortEnd": alaQoSServiceDestinationUdpPortEnd,
       "alaQoSAppliedServiceTable": alaQoSAppliedServiceTable,
       "alaQoSAppliedServiceEntry": alaQoSAppliedServiceEntry,
       "alaQoSAppliedServiceName": alaQoSAppliedServiceName,
       "alaQoSAppliedServiceSource": alaQoSAppliedServiceSource,
       "alaQoSAppliedServiceProtocol": alaQoSAppliedServiceProtocol,
       "alaQoSAppliedServiceSourceIpPort": alaQoSAppliedServiceSourceIpPort,
       "alaQoSAppliedServiceSourceIpPortStatus": alaQoSAppliedServiceSourceIpPortStatus,
       "alaQoSAppliedServiceDestinationIpPort": alaQoSAppliedServiceDestinationIpPort,
       "alaQoSAppliedServiceDestinationIpPortStatus": alaQoSAppliedServiceDestinationIpPortStatus,
       "alaQoSAppliedServiceRowStatus": alaQoSAppliedServiceRowStatus,
       "alaQoSAppliedServiceSourceIpPortEnd": alaQoSAppliedServiceSourceIpPortEnd,
       "alaQoSAppliedServiceDestinationIpPortEnd": alaQoSAppliedServiceDestinationIpPortEnd,
       "alaQoSAppliedServiceSourceTcpPort": alaQoSAppliedServiceSourceTcpPort,
       "alaQoSAppliedServiceSourceTcpPortStatus": alaQoSAppliedServiceSourceTcpPortStatus,
       "alaQoSAppliedServiceSourceTcpPortEnd": alaQoSAppliedServiceSourceTcpPortEnd,
       "alaQoSAppliedServiceDestinationTcpPort": alaQoSAppliedServiceDestinationTcpPort,
       "alaQoSAppliedServiceDestinationTcpPortStatus": alaQoSAppliedServiceDestinationTcpPortStatus,
       "alaQoSAppliedServiceDestinationTcpPortEnd": alaQoSAppliedServiceDestinationTcpPortEnd,
       "alaQoSAppliedServiceSourceUdpPort": alaQoSAppliedServiceSourceUdpPort,
       "alaQoSAppliedServiceSourceUdpPortStatus": alaQoSAppliedServiceSourceUdpPortStatus,
       "alaQoSAppliedServiceSourceUdpPortEnd": alaQoSAppliedServiceSourceUdpPortEnd,
       "alaQoSAppliedServiceDestinationUdpPort": alaQoSAppliedServiceDestinationUdpPort,
       "alaQoSAppliedServiceDestinationUdpPortStatus": alaQoSAppliedServiceDestinationUdpPortStatus,
       "alaQoSAppliedServiceDestinationUdpPortEnd": alaQoSAppliedServiceDestinationUdpPortEnd,
       "alaQoSServiceGroupsTable": alaQoSServiceGroupsTable,
       "alaQoSServiceGroupsEntry": alaQoSServiceGroupsEntry,
       "alaQoSServiceGroupsName": alaQoSServiceGroupsName,
       "alaQoSServiceGroupsSource": alaQoSServiceGroupsSource,
       "alaQoSServiceGroupsStatus": alaQoSServiceGroupsStatus,
       "alaQoSAppliedServiceGroupsTable": alaQoSAppliedServiceGroupsTable,
       "alaQoSAppliedServiceGroupsEntry": alaQoSAppliedServiceGroupsEntry,
       "alaQoSAppliedServiceGroupsName": alaQoSAppliedServiceGroupsName,
       "alaQoSAppliedServiceGroupsSource": alaQoSAppliedServiceGroupsSource,
       "alaQoSAppliedServiceGroupsStatus": alaQoSAppliedServiceGroupsStatus,
       "alaQoSServiceGroupTable": alaQoSServiceGroupTable,
       "alaQoSServiceGroupEntry": alaQoSServiceGroupEntry,
       "alaQoSServiceGroupServiceName": alaQoSServiceGroupServiceName,
       "alaQoSServiceGroupStatus": alaQoSServiceGroupStatus,
       "alaQoSAppliedServiceGroupTable": alaQoSAppliedServiceGroupTable,
       "alaQoSAppliedServiceGroupEntry": alaQoSAppliedServiceGroupEntry,
       "alaQoSAppliedServiceGroupServiceName": alaQoSAppliedServiceGroupServiceName,
       "alaQoSAppliedServiceGroupStatus": alaQoSAppliedServiceGroupStatus,
       "alaQoSNetworkGroupsTable": alaQoSNetworkGroupsTable,
       "alaQoSNetworkGroupsEntry": alaQoSNetworkGroupsEntry,
       "alaQoSNetworkGroupsName": alaQoSNetworkGroupsName,
       "alaQoSNetworkGroupsSource": alaQoSNetworkGroupsSource,
       "alaQoSNetworkGroupsStatus": alaQoSNetworkGroupsStatus,
       "alaQoSAppliedNetworkGroupsTable": alaQoSAppliedNetworkGroupsTable,
       "alaQoSAppliedNetworkGroupsEntry": alaQoSAppliedNetworkGroupsEntry,
       "alaQoSAppliedNetworkGroupsName": alaQoSAppliedNetworkGroupsName,
       "alaQoSAppliedNetworkGroupsSource": alaQoSAppliedNetworkGroupsSource,
       "alaQoSAppliedNetworkGroupsStatus": alaQoSAppliedNetworkGroupsStatus,
       "alaQoSNetworkGroupTable": alaQoSNetworkGroupTable,
       "alaQoSNetworkGroupEntry": alaQoSNetworkGroupEntry,
       "alaQoSNetworkGroupIpAddr": alaQoSNetworkGroupIpAddr,
       "alaQoSNetworkGroupIpMask": alaQoSNetworkGroupIpMask,
       "alaQoSNetworkGroupStatus": alaQoSNetworkGroupStatus,
       "alaQoSAppliedNetworkGroupTable": alaQoSAppliedNetworkGroupTable,
       "alaQoSAppliedNetworkGroupEntry": alaQoSAppliedNetworkGroupEntry,
       "alaQoSAppliedNetworkGroupIpAddr": alaQoSAppliedNetworkGroupIpAddr,
       "alaQoSAppliedNetworkGroupIpMask": alaQoSAppliedNetworkGroupIpMask,
       "alaQoSAppliedNetworkGroupStatus": alaQoSAppliedNetworkGroupStatus,
       "alaQoSMACGroupsTable": alaQoSMACGroupsTable,
       "alaQoSMACGroupsEntry": alaQoSMACGroupsEntry,
       "alaQoSMACGroupsName": alaQoSMACGroupsName,
       "alaQoSMACGroupsSource": alaQoSMACGroupsSource,
       "alaQoSMACGroupsStatus": alaQoSMACGroupsStatus,
       "alaQoSAppliedMACGroupsTable": alaQoSAppliedMACGroupsTable,
       "alaQoSAppliedMACGroupsEntry": alaQoSAppliedMACGroupsEntry,
       "alaQoSAppliedMACGroupsName": alaQoSAppliedMACGroupsName,
       "alaQoSAppliedMACGroupsSource": alaQoSAppliedMACGroupsSource,
       "alaQoSAppliedMACGroupsStatus": alaQoSAppliedMACGroupsStatus,
       "alaQoSMACGroupTable": alaQoSMACGroupTable,
       "alaQoSMACGroupEntry": alaQoSMACGroupEntry,
       "alaQoSMACGroupMacAddr": alaQoSMACGroupMacAddr,
       "alaQoSMACGroupMacMask": alaQoSMACGroupMacMask,
       "alaQoSMACGroupStatus": alaQoSMACGroupStatus,
       "alaQoSAppliedMACGroupTable": alaQoSAppliedMACGroupTable,
       "alaQoSAppliedMACGroupEntry": alaQoSAppliedMACGroupEntry,
       "alaQoSAppliedMACGroupMacAddr": alaQoSAppliedMACGroupMacAddr,
       "alaQoSAppliedMACGroupMacMask": alaQoSAppliedMACGroupMacMask,
       "alaQoSAppliedMACGroupStatus": alaQoSAppliedMACGroupStatus,
       "alaQoSPortGroupsTable": alaQoSPortGroupsTable,
       "alaQoSPortGroupsEntry": alaQoSPortGroupsEntry,
       "alaQoSPortGroupsName": alaQoSPortGroupsName,
       "alaQoSPortGroupsSource": alaQoSPortGroupsSource,
       "alaQoSPortGroupsStatus": alaQoSPortGroupsStatus,
       "alaQoSAppliedPortGroupsTable": alaQoSAppliedPortGroupsTable,
       "alaQoSAppliedPortGroupsEntry": alaQoSAppliedPortGroupsEntry,
       "alaQoSAppliedPortGroupsName": alaQoSAppliedPortGroupsName,
       "alaQoSAppliedPortGroupsSource": alaQoSAppliedPortGroupsSource,
       "alaQoSAppliedPortGroupsStatus": alaQoSAppliedPortGroupsStatus,
       "alaQoSPortGroupTable": alaQoSPortGroupTable,
       "alaQoSPortGroupEntry": alaQoSPortGroupEntry,
       "alaQoSPortGroupSlot": alaQoSPortGroupSlot,
       "alaQoSPortGroupPort": alaQoSPortGroupPort,
       "alaQoSPortGroupStatus": alaQoSPortGroupStatus,
       "alaQoSPortGroupPortEnd": alaQoSPortGroupPortEnd,
       "alaQoSAppliedPortGroupTable": alaQoSAppliedPortGroupTable,
       "alaQoSAppliedPortGroupEntry": alaQoSAppliedPortGroupEntry,
       "alaQoSAppliedPortGroupSlot": alaQoSAppliedPortGroupSlot,
       "alaQoSAppliedPortGroupPort": alaQoSAppliedPortGroupPort,
       "alaQoSAppliedPortGroupStatus": alaQoSAppliedPortGroupStatus,
       "alaQoSAppliedPortGroupPortEnd": alaQoSAppliedPortGroupPortEnd,
       "alaQoSMapGroupsTable": alaQoSMapGroupsTable,
       "alaQoSMapGroupsEntry": alaQoSMapGroupsEntry,
       "alaQoSMapGroupsName": alaQoSMapGroupsName,
       "alaQoSMapGroupsSource": alaQoSMapGroupsSource,
       "alaQoSMapGroupsStatus": alaQoSMapGroupsStatus,
       "alaQoSAppliedMapGroupsTable": alaQoSAppliedMapGroupsTable,
       "alaQoSAppliedMapGroupsEntry": alaQoSAppliedMapGroupsEntry,
       "alaQoSAppliedMapGroupsName": alaQoSAppliedMapGroupsName,
       "alaQoSAppliedMapGroupsSource": alaQoSAppliedMapGroupsSource,
       "alaQoSAppliedMapGroupsStatus": alaQoSAppliedMapGroupsStatus,
       "alaQoSMapGroupTable": alaQoSMapGroupTable,
       "alaQoSMapGroupEntry": alaQoSMapGroupEntry,
       "alaQoSMapGroupKey": alaQoSMapGroupKey,
       "alaQoSMapGroupKeyEnd": alaQoSMapGroupKeyEnd,
       "alaQoSMapGroupValue": alaQoSMapGroupValue,
       "alaQoSMapGroupStatus": alaQoSMapGroupStatus,
       "alaQoSAppliedMapGroupTable": alaQoSAppliedMapGroupTable,
       "alaQoSAppliedMapGroupEntry": alaQoSAppliedMapGroupEntry,
       "alaQoSAppliedMapGroupKey": alaQoSAppliedMapGroupKey,
       "alaQoSAppliedMapGroupKeyEnd": alaQoSAppliedMapGroupKeyEnd,
       "alaQoSAppliedMapGroupValue": alaQoSAppliedMapGroupValue,
       "alaQoSAppliedMapGroupStatus": alaQoSAppliedMapGroupStatus,
       "alaQoSActionTable": alaQoSActionTable,
       "alaQoSActionEntry": alaQoSActionEntry,
       "alaQoSActionName": alaQoSActionName,
       "alaQoSActionSource": alaQoSActionSource,
       "alaQoSActionDisposition": alaQoSActionDisposition,
       "alaQoSActionDropAlgorithm": alaQoSActionDropAlgorithm,
       "alaQoSActionWredMaximumThreshold": alaQoSActionWredMaximumThreshold,
       "alaQoSActionWredMaximumThresholdStatus": alaQoSActionWredMaximumThresholdStatus,
       "alaQoSActionWredMinimumThreshold": alaQoSActionWredMinimumThreshold,
       "alaQoSActionWredMinimumThresholdStatus": alaQoSActionWredMinimumThresholdStatus,
       "alaQoSActionWredMaximumProbability": alaQoSActionWredMaximumProbability,
       "alaQoSActionWredMaximumProbabilityStatus": alaQoSActionWredMaximumProbabilityStatus,
       "alaQoSActionMinimumBandwidth": alaQoSActionMinimumBandwidth,
       "alaQoSActionMinimumBandwidthStatus": alaQoSActionMinimumBandwidthStatus,
       "alaQoSActionMaximumBandwidth": alaQoSActionMaximumBandwidth,
       "alaQoSActionMaximumBandwidthStatus": alaQoSActionMaximumBandwidthStatus,
       "alaQoSActionPeakBandwidth": alaQoSActionPeakBandwidth,
       "alaQoSActionPeakBandwidthStatus": alaQoSActionPeakBandwidthStatus,
       "alaQoSActionPriority": alaQoSActionPriority,
       "alaQoSActionPriorityStatus": alaQoSActionPriorityStatus,
       "alaQoSActionShared": alaQoSActionShared,
       "alaQoSActionJitter": alaQoSActionJitter,
       "alaQoSActionJitterStatus": alaQoSActionJitterStatus,
       "alaQoSActionLatency": alaQoSActionLatency,
       "alaQoSActionLatencyStatus": alaQoSActionLatencyStatus,
       "alaQoSActionMaximumDepth": alaQoSActionMaximumDepth,
       "alaQoSActionMaximumDepthStatus": alaQoSActionMaximumDepthStatus,
       "alaQoSActionMaximumBuffers": alaQoSActionMaximumBuffers,
       "alaQoSActionMaximumBuffersStatus": alaQoSActionMaximumBuffersStatus,
       "alaQoSAction8021p": alaQoSAction8021p,
       "alaQoSAction8021pStatus": alaQoSAction8021pStatus,
       "alaQoSActionTos": alaQoSActionTos,
       "alaQoSActionTosStatus": alaQoSActionTosStatus,
       "alaQoSActionDscp": alaQoSActionDscp,
       "alaQoSActionDscpStatus": alaQoSActionDscpStatus,
       "alaQoSActionMapFrom": alaQoSActionMapFrom,
       "alaQoSActionMapTo": alaQoSActionMapTo,
       "alaQoSActionMapGroup": alaQoSActionMapGroup,
       "alaQoSActionMapGroupStatus": alaQoSActionMapGroupStatus,
       "alaQoSActionSourceRewriteIpAddr": alaQoSActionSourceRewriteIpAddr,
       "alaQoSActionSourceRewriteIpAddrStatus": alaQoSActionSourceRewriteIpAddrStatus,
       "alaQoSActionSourceRewriteIpMask": alaQoSActionSourceRewriteIpMask,
       "alaQoSActionSourceRewriteNetworkGroup": alaQoSActionSourceRewriteNetworkGroup,
       "alaQoSActionSourceRewriteNetworkGroupStatus": alaQoSActionSourceRewriteNetworkGroupStatus,
       "alaQoSActionDestinationRewriteIpAddr": alaQoSActionDestinationRewriteIpAddr,
       "alaQoSActionDestinationRewriteIpAddrStatus": alaQoSActionDestinationRewriteIpAddrStatus,
       "alaQoSActionDestinationRewriteIpMask": alaQoSActionDestinationRewriteIpMask,
       "alaQoSActionDestinationRewriteNetworkGroup": alaQoSActionDestinationRewriteNetworkGroup,
       "alaQoSActionDestinationRewriteNetworkGroupStatus": alaQoSActionDestinationRewriteNetworkGroupStatus,
       "alaQoSActionLoadBalanceGroup": alaQoSActionLoadBalanceGroup,
       "alaQoSActionLoadBalanceGroupStatus": alaQoSActionLoadBalanceGroupStatus,
       "alaQoSActionPermanentGatewayIpAddr": alaQoSActionPermanentGatewayIpAddr,
       "alaQoSActionPermanentGatewayIpAddrStatus": alaQoSActionPermanentGatewayIpAddrStatus,
       "alaQoSActionAlternateGatewayIpAddr": alaQoSActionAlternateGatewayIpAddr,
       "alaQoSActionAlternateGatewayIpAddrStatus": alaQoSActionAlternateGatewayIpAddrStatus,
       "alaQoSActionRowStatus": alaQoSActionRowStatus,
       "alaQoSActionMinimumDepth": alaQoSActionMinimumDepth,
       "alaQoSActionMinimumDepthStatus": alaQoSActionMinimumDepthStatus,
       "alaQoSActionVPNAccess": alaQoSActionVPNAccess,
       "alaQoSActionNocache": alaQoSActionNocache,
       "alaQoSActionPortdisable": alaQoSActionPortdisable,
       "alaQoSActionRedirectSlot": alaQoSActionRedirectSlot,
       "alaQoSActionRedirectSlotStatus": alaQoSActionRedirectSlotStatus,
       "alaQoSActionRedirectPort": alaQoSActionRedirectPort,
       "alaQoSActionRedirectAgg": alaQoSActionRedirectAgg,
       "alaQoSActionRedirectAggStatus": alaQoSActionRedirectAggStatus,
       "alaQoSActionMirrorSlot": alaQoSActionMirrorSlot,
       "alaQoSActionMirrorPort": alaQoSActionMirrorPort,
       "alaQoSActionMirrorMode": alaQoSActionMirrorMode,
       "alaQoSActionMirrorModeStatus": alaQoSActionMirrorModeStatus,
       "alaQoSActionCIR": alaQoSActionCIR,
       "alaQoSActionCIRStatus": alaQoSActionCIRStatus,
       "alaQoSActionCBS": alaQoSActionCBS,
       "alaQoSActionCBSStatus": alaQoSActionCBSStatus,
       "alaQoSActionPIR": alaQoSActionPIR,
       "alaQoSActionPIRStatus": alaQoSActionPIRStatus,
       "alaQoSActionPBS": alaQoSActionPBS,
       "alaQoSActionPBSStatus": alaQoSActionPBSStatus,
       "alaQoSActionCounterColor": alaQoSActionCounterColor,
       "alaQoSAppliedActionTable": alaQoSAppliedActionTable,
       "alaQoSAppliedActionEntry": alaQoSAppliedActionEntry,
       "alaQoSAppliedActionName": alaQoSAppliedActionName,
       "alaQoSAppliedActionSource": alaQoSAppliedActionSource,
       "alaQoSAppliedActionDisposition": alaQoSAppliedActionDisposition,
       "alaQoSAppliedActionDropAlgorithm": alaQoSAppliedActionDropAlgorithm,
       "alaQoSAppliedActionWredMaximumThreshold": alaQoSAppliedActionWredMaximumThreshold,
       "alaQoSAppliedActionWredMaximumThresholdStatus": alaQoSAppliedActionWredMaximumThresholdStatus,
       "alaQoSAppliedActionWredMinimumThreshold": alaQoSAppliedActionWredMinimumThreshold,
       "alaQoSAppliedActionWredMinimumThresholdStatus": alaQoSAppliedActionWredMinimumThresholdStatus,
       "alaQoSAppliedActionWredMaximumProbability": alaQoSAppliedActionWredMaximumProbability,
       "alaQoSAppliedActionWredMaximumProbabilityStatus": alaQoSAppliedActionWredMaximumProbabilityStatus,
       "alaQoSAppliedActionMinimumBandwidth": alaQoSAppliedActionMinimumBandwidth,
       "alaQoSAppliedActionMinimumBandwidthStatus": alaQoSAppliedActionMinimumBandwidthStatus,
       "alaQoSAppliedActionMaximumBandwidth": alaQoSAppliedActionMaximumBandwidth,
       "alaQoSAppliedActionMaximumBandwidthStatus": alaQoSAppliedActionMaximumBandwidthStatus,
       "alaQoSAppliedActionPeakBandwidth": alaQoSAppliedActionPeakBandwidth,
       "alaQoSAppliedActionPeakBandwidthStatus": alaQoSAppliedActionPeakBandwidthStatus,
       "alaQoSAppliedActionPriority": alaQoSAppliedActionPriority,
       "alaQoSAppliedActionPriorityStatus": alaQoSAppliedActionPriorityStatus,
       "alaQoSAppliedActionShared": alaQoSAppliedActionShared,
       "alaQoSAppliedActionJitter": alaQoSAppliedActionJitter,
       "alaQoSAppliedActionJitterStatus": alaQoSAppliedActionJitterStatus,
       "alaQoSAppliedActionLatency": alaQoSAppliedActionLatency,
       "alaQoSAppliedActionLatencyStatus": alaQoSAppliedActionLatencyStatus,
       "alaQoSAppliedActionMaximumDepth": alaQoSAppliedActionMaximumDepth,
       "alaQoSAppliedActionMaximumDepthStatus": alaQoSAppliedActionMaximumDepthStatus,
       "alaQoSAppliedActionMaximumBuffers": alaQoSAppliedActionMaximumBuffers,
       "alaQoSAppliedActionMaximumBuffersStatus": alaQoSAppliedActionMaximumBuffersStatus,
       "alaQoSAppliedAction8021p": alaQoSAppliedAction8021p,
       "alaQoSAppliedAction8021pStatus": alaQoSAppliedAction8021pStatus,
       "alaQoSAppliedActionTos": alaQoSAppliedActionTos,
       "alaQoSAppliedActionTosStatus": alaQoSAppliedActionTosStatus,
       "alaQoSAppliedActionDscp": alaQoSAppliedActionDscp,
       "alaQoSAppliedActionDscpStatus": alaQoSAppliedActionDscpStatus,
       "alaQoSAppliedActionMapFrom": alaQoSAppliedActionMapFrom,
       "alaQoSAppliedActionMapTo": alaQoSAppliedActionMapTo,
       "alaQoSAppliedActionMapGroup": alaQoSAppliedActionMapGroup,
       "alaQoSAppliedActionMapGroupStatus": alaQoSAppliedActionMapGroupStatus,
       "alaQoSAppliedActionSourceRewriteIpAddr": alaQoSAppliedActionSourceRewriteIpAddr,
       "alaQoSAppliedActionSourceRewriteIpAddrStatus": alaQoSAppliedActionSourceRewriteIpAddrStatus,
       "alaQoSAppliedActionSourceRewriteIpMask": alaQoSAppliedActionSourceRewriteIpMask,
       "alaQoSAppliedActionSourceRewriteNetworkGroup": alaQoSAppliedActionSourceRewriteNetworkGroup,
       "alaQoSAppliedActionSourceRewriteNetworkGroupStatus": alaQoSAppliedActionSourceRewriteNetworkGroupStatus,
       "alaQoSAppliedActionDestinationRewriteIpAddr": alaQoSAppliedActionDestinationRewriteIpAddr,
       "alaQoSAppliedActionDestinationRewriteIpAddrStatus": alaQoSAppliedActionDestinationRewriteIpAddrStatus,
       "alaQoSAppliedActionDestinationRewriteIpMask": alaQoSAppliedActionDestinationRewriteIpMask,
       "alaQoSAppliedActionDestinationRewriteNetworkGroup": alaQoSAppliedActionDestinationRewriteNetworkGroup,
       "alaQoSAppliedActionDestinationRewriteNetworkGroupStatus": alaQoSAppliedActionDestinationRewriteNetworkGroupStatus,
       "alaQoSAppliedActionLoadBalanceGroup": alaQoSAppliedActionLoadBalanceGroup,
       "alaQoSAppliedActionLoadBalanceGroupStatus": alaQoSAppliedActionLoadBalanceGroupStatus,
       "alaQoSAppliedActionPermanentGatewayIpAddr": alaQoSAppliedActionPermanentGatewayIpAddr,
       "alaQoSAppliedActionPermanentGatewayIpAddrStatus": alaQoSAppliedActionPermanentGatewayIpAddrStatus,
       "alaQoSAppliedActionAlternateGatewayIpAddr": alaQoSAppliedActionAlternateGatewayIpAddr,
       "alaQoSAppliedActionAlternateGatewayIpAddrStatus": alaQoSAppliedActionAlternateGatewayIpAddrStatus,
       "alaQoSAppliedActionRowStatus": alaQoSAppliedActionRowStatus,
       "alaQoSAppliedActionMinimumDepth": alaQoSAppliedActionMinimumDepth,
       "alaQoSAppliedActionMinimumDepthStatus": alaQoSAppliedActionMinimumDepthStatus,
       "alaQoSAppliedActionVPNAccess": alaQoSAppliedActionVPNAccess,
       "alaQoSAppliedActionNocache": alaQoSAppliedActionNocache,
       "alaQoSAppliedActionPortdisable": alaQoSAppliedActionPortdisable,
       "alaQoSAppliedActionRedirectSlot": alaQoSAppliedActionRedirectSlot,
       "alaQoSAppliedActionRedirectSlotStatus": alaQoSAppliedActionRedirectSlotStatus,
       "alaQoSAppliedActionRedirectPort": alaQoSAppliedActionRedirectPort,
       "alaQoSAppliedActionRedirectAgg": alaQoSAppliedActionRedirectAgg,
       "alaQoSAppliedActionRedirectAggStatus": alaQoSAppliedActionRedirectAggStatus,
       "alaQoSAppliedActionMirrorSlot": alaQoSAppliedActionMirrorSlot,
       "alaQoSAppliedActionMirrorPort": alaQoSAppliedActionMirrorPort,
       "alaQoSAppliedActionMirrorMode": alaQoSAppliedActionMirrorMode,
       "alaQoSAppliedActionMirrorModeStatus": alaQoSAppliedActionMirrorModeStatus,
       "alaQoSAppliedActionCIR": alaQoSAppliedActionCIR,
       "alaQoSAppliedActionCIRStatus": alaQoSAppliedActionCIRStatus,
       "alaQoSAppliedActionCBS": alaQoSAppliedActionCBS,
       "alaQoSAppliedActionCBSStatus": alaQoSAppliedActionCBSStatus,
       "alaQoSAppliedActionPIR": alaQoSAppliedActionPIR,
       "alaQoSAppliedActionPIRStatus": alaQoSAppliedActionPIRStatus,
       "alaQoSAppliedActionPBS": alaQoSAppliedActionPBS,
       "alaQoSAppliedActionPBSStatus": alaQoSAppliedActionPBSStatus,
       "alaQoSAppliedActionCounterColor": alaQoSAppliedActionCounterColor,
       "alaQoSPortTable": alaQoSPortTable,
       "alaQoSPortEntry": alaQoSPortEntry,
       "alaQoSPortSlot": alaQoSPortSlot,
       "alaQoSPortPort": alaQoSPortPort,
       "alaQoSPortEnabled": alaQoSPortEnabled,
       "alaQoSPortAppliedEnabled": alaQoSPortAppliedEnabled,
       "alaQoSPortInterfaceType": alaQoSPortInterfaceType,
       "alaQoSPortTrusted": alaQoSPortTrusted,
       "alaQoSPortDefault8021p": alaQoSPortDefault8021p,
       "alaQoSPortDefaultDSCP": alaQoSPortDefaultDSCP,
       "alaQoSPortMaximumReservedBandwidth": alaQoSPortMaximumReservedBandwidth,
       "alaQoSPortMaximumReservedBandwidthStatus": alaQoSPortMaximumReservedBandwidthStatus,
       "alaQoSPortAppliedMaximumReservedBandwidth": alaQoSPortAppliedMaximumReservedBandwidth,
       "alaQoSPortAppliedMaximumReservedBandwidthStatus": alaQoSPortAppliedMaximumReservedBandwidthStatus,
       "alaQoSPortMaximumSignalledBandwidth": alaQoSPortMaximumSignalledBandwidth,
       "alaQoSPortMaximumSignalledBandwidthStatus": alaQoSPortMaximumSignalledBandwidthStatus,
       "alaQoSPortAppliedMaximumSignalledBandwidth": alaQoSPortAppliedMaximumSignalledBandwidth,
       "alaQoSPortAppliedMaximumSignalledBandwidthStatus": alaQoSPortAppliedMaximumSignalledBandwidthStatus,
       "alaQoSPortDefaultQueues": alaQoSPortDefaultQueues,
       "alaQoSPortAppliedDefaultQueues": alaQoSPortAppliedDefaultQueues,
       "alaQoSPortMaximumDefaultBandwidth": alaQoSPortMaximumDefaultBandwidth,
       "alaQoSPortMaximumDefaultBandwidthStatus": alaQoSPortMaximumDefaultBandwidthStatus,
       "alaQoSPortAppliedMaximumDefaultBandwidth": alaQoSPortAppliedMaximumDefaultBandwidth,
       "alaQoSPortAppliedMaximumDefaultBandwidthStatus": alaQoSPortAppliedMaximumDefaultBandwidthStatus,
       "alaQoSPortMaximumDefaultDepth": alaQoSPortMaximumDefaultDepth,
       "alaQoSPortMaximumDefaultDepthStatus": alaQoSPortMaximumDefaultDepthStatus,
       "alaQoSPortAppliedMaximumDefaultDepth": alaQoSPortAppliedMaximumDefaultDepth,
       "alaQoSPortAppliedMaximumDefaultDepthStatus": alaQoSPortAppliedMaximumDefaultDepthStatus,
       "alaQoSPortMaximumDefaultBuffers": alaQoSPortMaximumDefaultBuffers,
       "alaQoSPortMaximumDefaultBuffersStatus": alaQoSPortMaximumDefaultBuffersStatus,
       "alaQoSPortAppliedMaximumDefaultBuffers": alaQoSPortAppliedMaximumDefaultBuffers,
       "alaQoSPortAppliedMaximumDefaultBuffersStatus": alaQoSPortAppliedMaximumDefaultBuffersStatus,
       "alaQoSPortReset": alaQoSPortReset,
       "alaQoSPortPhysicalBandwidth": alaQoSPortPhysicalBandwidth,
       "alaQoSPortReservedBandwidth": alaQoSPortReservedBandwidth,
       "alaQoSPortSignalledBandwidth": alaQoSPortSignalledBandwidth,
       "alaQoSPortCurrentBandwidth": alaQoSPortCurrentBandwidth,
       "alaQoSPortDefaultQidLow": alaQoSPortDefaultQidLow,
       "alaQoSPortDefaultQidMedium": alaQoSPortDefaultQidMedium,
       "alaQoSPortDefaultQidHigh": alaQoSPortDefaultQidHigh,
       "alaQoSPortDefaultQidUrgent": alaQoSPortDefaultQidUrgent,
       "alaQoSPortFloodQid": alaQoSPortFloodQid,
       "alaQoSPortQueues": alaQoSPortQueues,
       "alaQoSPortQueuesCreated": alaQoSPortQueuesCreated,
       "alaQoSPortQueuesFailed": alaQoSPortQueuesFailed,
       "alaQoSPortQueuesPreempted": alaQoSPortQueuesPreempted,
       "alaQoSPortRowStatus": alaQoSPortRowStatus,
       "alaQoSPortFirPrio0EnqBytes": alaQoSPortFirPrio0EnqBytes,
       "alaQoSPortFirPrio0DeqBytes": alaQoSPortFirPrio0DeqBytes,
       "alaQoSPortFirPrio0EnqPkts": alaQoSPortFirPrio0EnqPkts,
       "alaQoSPortFirPrio0DeqPkts": alaQoSPortFirPrio0DeqPkts,
       "alaQoSPortFirPrio0QidDiscardPkts": alaQoSPortFirPrio0QidDiscardPkts,
       "alaQoSPortFirPrio0WredDiscardPkts": alaQoSPortFirPrio0WredDiscardPkts,
       "alaQoSPortFirPrio0OverflowDiscardPkts": alaQoSPortFirPrio0OverflowDiscardPkts,
       "alaQoSPortFirPrio1EnqBytes": alaQoSPortFirPrio1EnqBytes,
       "alaQoSPortFirPrio1DeqBytes": alaQoSPortFirPrio1DeqBytes,
       "alaQoSPortFirPrio1EnqPkts": alaQoSPortFirPrio1EnqPkts,
       "alaQoSPortFirPrio1DeqPkts": alaQoSPortFirPrio1DeqPkts,
       "alaQoSPortFirPrio1QidDiscardPkts": alaQoSPortFirPrio1QidDiscardPkts,
       "alaQoSPortFirPrio1WredDiscardPkts": alaQoSPortFirPrio1WredDiscardPkts,
       "alaQoSPortFirPrio1OverflowDiscardPkts": alaQoSPortFirPrio1OverflowDiscardPkts,
       "alaQoSPortFirPrio2EnqBytes": alaQoSPortFirPrio2EnqBytes,
       "alaQoSPortFirPrio2DeqBytes": alaQoSPortFirPrio2DeqBytes,
       "alaQoSPortFirPrio2EnqPkts": alaQoSPortFirPrio2EnqPkts,
       "alaQoSPortFirPrio2DeqPkts": alaQoSPortFirPrio2DeqPkts,
       "alaQoSPortFirPrio2QidDiscardPkts": alaQoSPortFirPrio2QidDiscardPkts,
       "alaQoSPortFirPrio2WredDiscardPkts": alaQoSPortFirPrio2WredDiscardPkts,
       "alaQoSPortFirPrio2OverflowDiscardPkts": alaQoSPortFirPrio2OverflowDiscardPkts,
       "alaQoSPortFirPrio3EnqBytes": alaQoSPortFirPrio3EnqBytes,
       "alaQoSPortFirPrio3DeqBytes": alaQoSPortFirPrio3DeqBytes,
       "alaQoSPortFirPrio3EnqPkts": alaQoSPortFirPrio3EnqPkts,
       "alaQoSPortFirPrio3DeqPkts": alaQoSPortFirPrio3DeqPkts,
       "alaQoSPortFirPrio3QidDiscardPkts": alaQoSPortFirPrio3QidDiscardPkts,
       "alaQoSPortFirPrio3WredDiscardPkts": alaQoSPortFirPrio3WredDiscardPkts,
       "alaQoSPortFirPrio3OverflowDiscardPkts": alaQoSPortFirPrio3OverflowDiscardPkts,
       "alaQoSPortDefaultClassification": alaQoSPortDefaultClassification,
       "alaQoSPortLowPriorityWeight": alaQoSPortLowPriorityWeight,
       "alaQoSPortMediumPriorityWeight": alaQoSPortMediumPriorityWeight,
       "alaQoSPortHighPriorityWeight": alaQoSPortHighPriorityWeight,
       "alaQoSPortUrgentPriorityWeight": alaQoSPortUrgentPriorityWeight,
       "alaQoSPortMaximumBandwidth": alaQoSPortMaximumBandwidth,
       "alaQoSPortMaximumBandwidthStatus": alaQoSPortMaximumBandwidthStatus,
       "alaQoSPortEnqueuingThresholdP0Lower": alaQoSPortEnqueuingThresholdP0Lower,
       "alaQoSPortEnqueuingThresholdP0Upper": alaQoSPortEnqueuingThresholdP0Upper,
       "alaQoSPortEnqueuingThresholdP1Lower": alaQoSPortEnqueuingThresholdP1Lower,
       "alaQoSPortEnqueuingThresholdP1Upper": alaQoSPortEnqueuingThresholdP1Upper,
       "alaQoSPortEnqueuingThresholdP2Lower": alaQoSPortEnqueuingThresholdP2Lower,
       "alaQoSPortEnqueuingThresholdP2Upper": alaQoSPortEnqueuingThresholdP2Upper,
       "alaQoSPortEnqueuingThresholdP3Lower": alaQoSPortEnqueuingThresholdP3Lower,
       "alaQoSPortEnqueuingThresholdP3Upper": alaQoSPortEnqueuingThresholdP3Upper,
       "alaQoSPortEnqueuingThresholdStatus": alaQoSPortEnqueuingThresholdStatus,
       "alaQoSPortHighDensity": alaQoSPortHighDensity,
       "alaQoSPortServicingMode": alaQoSPortServicingMode,
       "alaQoSPortFreeFFPRules": alaQoSPortFreeFFPRules,
       "alaQoSPortUsedFFPRules": alaQoSPortUsedFFPRules,
       "alaQoSPortFreeFFPMasks": alaQoSPortFreeFFPMasks,
       "alaQoSPortUsedFFPMasks": alaQoSPortUsedFFPMasks,
       "alaQoSPortSpoofedCount": alaQoSPortSpoofedCount,
       "alaQoSPortNonSpoofedCount": alaQoSPortNonSpoofedCount,
       "alaQoSPortQ4PriorityWeight": alaQoSPortQ4PriorityWeight,
       "alaQoSPortQ5PriorityWeight": alaQoSPortQ5PriorityWeight,
       "alaQoSPortQ6PriorityWeight": alaQoSPortQ6PriorityWeight,
       "alaQoSPortQ7PriorityWeight": alaQoSPortQ7PriorityWeight,
       "alaQoSPortCOS0MaximumBandwidth": alaQoSPortCOS0MaximumBandwidth,
       "alaQoSPortCOS0MaximumBandwidthStatus": alaQoSPortCOS0MaximumBandwidthStatus,
       "alaQoSPortCOS1MaximumBandwidth": alaQoSPortCOS1MaximumBandwidth,
       "alaQoSPortCOS1MaximumBandwidthStatus": alaQoSPortCOS1MaximumBandwidthStatus,
       "alaQoSPortCOS2MaximumBandwidth": alaQoSPortCOS2MaximumBandwidth,
       "alaQoSPortCOS2MaximumBandwidthStatus": alaQoSPortCOS2MaximumBandwidthStatus,
       "alaQoSPortCOS3MaximumBandwidth": alaQoSPortCOS3MaximumBandwidth,
       "alaQoSPortCOS3MaximumBandwidthStatus": alaQoSPortCOS3MaximumBandwidthStatus,
       "alaQoSPortCOS4MaximumBandwidth": alaQoSPortCOS4MaximumBandwidth,
       "alaQoSPortCOS4MaximumBandwidthStatus": alaQoSPortCOS4MaximumBandwidthStatus,
       "alaQoSPortCOS5MaximumBandwidth": alaQoSPortCOS5MaximumBandwidth,
       "alaQoSPortCOS5MaximumBandwidthStatus": alaQoSPortCOS5MaximumBandwidthStatus,
       "alaQoSPortCOS6MaximumBandwidth": alaQoSPortCOS6MaximumBandwidth,
       "alaQoSPortCOS6MaximumBandwidthStatus": alaQoSPortCOS6MaximumBandwidthStatus,
       "alaQoSPortCOS7MaximumBandwidth": alaQoSPortCOS7MaximumBandwidth,
       "alaQoSPortCOS7MaximumBandwidthStatus": alaQoSPortCOS7MaximumBandwidthStatus,
       "alaQoSPortCOS0MinimumBandwidth": alaQoSPortCOS0MinimumBandwidth,
       "alaQoSPortCOS0MinimumBandwidthStatus": alaQoSPortCOS0MinimumBandwidthStatus,
       "alaQoSPortCOS1MinimumBandwidth": alaQoSPortCOS1MinimumBandwidth,
       "alaQoSPortCOS1MinimumBandwidthStatus": alaQoSPortCOS1MinimumBandwidthStatus,
       "alaQoSPortCOS2MinimumBandwidth": alaQoSPortCOS2MinimumBandwidth,
       "alaQoSPortCOS2MinimumBandwidthStatus": alaQoSPortCOS2MinimumBandwidthStatus,
       "alaQoSPortCOS3MinimumBandwidth": alaQoSPortCOS3MinimumBandwidth,
       "alaQoSPortCOS3MinimumBandwidthStatus": alaQoSPortCOS3MinimumBandwidthStatus,
       "alaQoSPortCOS4MinimumBandwidth": alaQoSPortCOS4MinimumBandwidth,
       "alaQoSPortCOS4MinimumBandwidthStatus": alaQoSPortCOS4MinimumBandwidthStatus,
       "alaQoSPortCOS5MinimumBandwidth": alaQoSPortCOS5MinimumBandwidth,
       "alaQoSPortCOS5MinimumBandwidthStatus": alaQoSPortCOS5MinimumBandwidthStatus,
       "alaQoSPortCOS6MinimumBandwidth": alaQoSPortCOS6MinimumBandwidth,
       "alaQoSPortCOS6MinimumBandwidthStatus": alaQoSPortCOS6MinimumBandwidthStatus,
       "alaQoSPortCOS7MinimumBandwidth": alaQoSPortCOS7MinimumBandwidth,
       "alaQoSPortCOS7MinimumBandwidthStatus": alaQoSPortCOS7MinimumBandwidthStatus,
       "alaQoSPortMaximumIngBandwidth": alaQoSPortMaximumIngBandwidth,
       "alaQoSPortMaximumIngBandwidthStatus": alaQoSPortMaximumIngBandwidthStatus,
       "alaQoSPortDEIMarking": alaQoSPortDEIMarking,
       "alaQoSPortMonitor": alaQoSPortMonitor,
       "alaQoSPortDEIMapping": alaQoSPortDEIMapping,
       "alaQoSConfig": alaQoSConfig,
       "alaQoSConfigEnabled": alaQoSConfigEnabled,
       "alaQoSConfigDefaultQueues": alaQoSConfigDefaultQueues,
       "alaQoSConfigAppliedDefaultQueues": alaQoSConfigAppliedDefaultQueues,
       "alaQoSConfigTrustPorts": alaQoSConfigTrustPorts,
       "alaQoSConfigFlowTimeout": alaQoSConfigFlowTimeout,
       "alaQoSConfigAppliedFlowTimeout": alaQoSConfigAppliedFlowTimeout,
       "alaQoSConfigFragmentTimeout": alaQoSConfigFragmentTimeout,
       "alaQoSConfigAppliedFragmentTimeout": alaQoSConfigAppliedFragmentTimeout,
       "alaQoSConfigReflexiveTimeout": alaQoSConfigReflexiveTimeout,
       "alaQoSConfigAppliedReflfexiveTimeout": alaQoSConfigAppliedReflfexiveTimeout,
       "alaQoSConfigNatTimeout": alaQoSConfigNatTimeout,
       "alaQoSConfigAppliedNatTimeout": alaQoSConfigAppliedNatTimeout,
       "alaQoSConfigClassifyl3Bridged": alaQoSConfigClassifyl3Bridged,
       "alaQoSConfigAppliedClassifyl3Bridged": alaQoSConfigAppliedClassifyl3Bridged,
       "alaQoSConfigClassifyFragments": alaQoSConfigClassifyFragments,
       "alaQoSConfigAppliedClassifyFragments": alaQoSConfigAppliedClassifyFragments,
       "alaQoSConfigDefaultBridgedDisposition": alaQoSConfigDefaultBridgedDisposition,
       "alaQoSConfigAppliedDefaultBridgedDisposition": alaQoSConfigAppliedDefaultBridgedDisposition,
       "alaQoSConfigDefaultRoutedDisposition": alaQoSConfigDefaultRoutedDisposition,
       "alaQoSConfigAppliedDefaultRoutedDisposition": alaQoSConfigAppliedDefaultRoutedDisposition,
       "alaQoSConfigDefaultMulticastDisposition": alaQoSConfigDefaultMulticastDisposition,
       "alaQoSConfigAppliedDefaultMulticastDisposition": alaQoSConfigAppliedDefaultMulticastDisposition,
       "alaQoSConfigStatsInterval": alaQoSConfigStatsInterval,
       "alaQoSConfigLogLines": alaQoSConfigLogLines,
       "alaQoSConfigLogLevel": alaQoSConfigLogLevel,
       "alaQoSConfigLogConsole": alaQoSConfigLogConsole,
       "alaQoSConfigForwardLog": alaQoSConfigForwardLog,
       "alaQoSConfigClearLog": alaQoSConfigClearLog,
       "alaQoSConfigApply": alaQoSConfigApply,
       "alaQoSConfigRevert": alaQoSConfigRevert,
       "alaQoSConfigReset": alaQoSConfigReset,
       "alaQoSConfigStatsReset": alaQoSConfigStatsReset,
       "alaQoSConfigFlush": alaQoSConfigFlush,
       "alaQoSConfigDebug": alaQoSConfigDebug,
       "alaQoSConfigServicingMode": alaQoSConfigServicingMode,
       "alaQoSConfigLowPriorityWeight": alaQoSConfigLowPriorityWeight,
       "alaQoSConfigMediumPriorityWeight": alaQoSConfigMediumPriorityWeight,
       "alaQoSConfigHighPriorityWeight": alaQoSConfigHighPriorityWeight,
       "alaQoSConfigUrgentPriorityWeight": alaQoSConfigUrgentPriorityWeight,
       "alaQoSConfigQ4PriorityWeight": alaQoSConfigQ4PriorityWeight,
       "alaQoSConfigQ5PriorityWeight": alaQoSConfigQ5PriorityWeight,
       "alaQoSConfigQ6PriorityWeight": alaQoSConfigQ6PriorityWeight,
       "alaQoSConfigQ7PriorityWeight": alaQoSConfigQ7PriorityWeight,
       "alaQoSConfigUserportFilter": alaQoSConfigUserportFilter,
       "alaQoSConfigAppliedUserportFilter": alaQoSConfigAppliedUserportFilter,
       "alaQoSConfigUserportShutdown": alaQoSConfigUserportShutdown,
       "alaQoSConfigAppliedUserportShutdown": alaQoSConfigAppliedUserportShutdown,
       "alaQoSConfigAutoNMS": alaQoSConfigAutoNMS,
       "alaQoSConfigAutoPhones": alaQoSConfigAutoPhones,
       "alaQoSConfigQMPage": alaQoSConfigQMPage,
       "alaQoSConfigQMMACGroup": alaQoSConfigQMMACGroup,
       "alaQoSConfigQMPath": alaQoSConfigQMPath,
       "alaQoSConfigDEIMapping": alaQoSConfigDEIMapping,
       "alaQoSConfigDEIMarking": alaQoSConfigDEIMarking,
       "alaQoSConfigStatsResetEgress": alaQoSConfigStatsResetEgress,
       "alaQoSStats": alaQoSStats,
       "alaQoSStatsL2Events": alaQoSStatsL2Events,
       "alaQoSStatsL2Matches": alaQoSStatsL2Matches,
       "alaQoSStatsL2Drops": alaQoSStatsL2Drops,
       "alaQoSStatsL3IngressEvents": alaQoSStatsL3IngressEvents,
       "alaQoSStatsL3IngressMatches": alaQoSStatsL3IngressMatches,
       "alaQoSStatsL3IngressDrops": alaQoSStatsL3IngressDrops,
       "alaQoSStatsL3EgressEvents": alaQoSStatsL3EgressEvents,
       "alaQoSStatsL3EgressMatches": alaQoSStatsL3EgressMatches,
       "alaQoSStatsL3EgressDrops": alaQoSStatsL3EgressDrops,
       "alaQoSStatsMulticastEvents": alaQoSStatsMulticastEvents,
       "alaQoSStatsMulticastMatches": alaQoSStatsMulticastMatches,
       "alaQoSStatsMulticastDrops": alaQoSStatsMulticastDrops,
       "alaQoSStatsFragments": alaQoSStatsFragments,
       "alaQoSStatsBadFragments": alaQoSStatsBadFragments,
       "alaQoSStatsUnknownFragments": alaQoSStatsUnknownFragments,
       "alaQoSStatsReflexiveFlows": alaQoSStatsReflexiveFlows,
       "alaQoSStatsReflexiveCorrections": alaQoSStatsReflexiveCorrections,
       "alaQoSStatsLoadBalanceFlows": alaQoSStatsLoadBalanceFlows,
       "alaQoSStatsClassifierMaxNodes": alaQoSStatsClassifierMaxNodes,
       "alaQoSStatsClassifierMaxDepth": alaQoSStatsClassifierMaxDepth,
       "alaQoSStatsFlowLookups": alaQoSStatsFlowLookups,
       "alaQoSStatsFlowHits": alaQoSStatsFlowHits,
       "alaQoSStatsSentNIMessages": alaQoSStatsSentNIMessages,
       "alaQoSStatsReceivedNIMessages": alaQoSStatsReceivedNIMessages,
       "alaQoSStatsFailedNIMessages": alaQoSStatsFailedNIMessages,
       "alaQoSStatsSpoofedEvents": alaQoSStatsSpoofedEvents,
       "alaQoSStatsNonSpoofedEvents": alaQoSStatsNonSpoofedEvents,
       "alaQoSStatsDropServicesEvents": alaQoSStatsDropServicesEvents,
       "alaQoSQueueTable": alaQoSQueueTable,
       "alaQoSQueueEntry": alaQoSQueueEntry,
       "alaQoSQueueId": alaQoSQueueId,
       "alaQoSQueueSlot": alaQoSQueueSlot,
       "alaQoSQueuePort": alaQoSQueuePort,
       "alaQoSQueuePortId": alaQoSQueuePortId,
       "alaQoSQueueType": alaQoSQueueType,
       "alaQoSQueuePriority": alaQoSQueuePriority,
       "alaQoSQueueMinimumBandwidth": alaQoSQueueMinimumBandwidth,
       "alaQoSQueueMaximumBandwidth": alaQoSQueueMaximumBandwidth,
       "alaQoSQueueAverageBandwidth": alaQoSQueueAverageBandwidth,
       "alaQoSQueueMinimumDepth": alaQoSQueueMinimumDepth,
       "alaQoSQueueMaximumDepth": alaQoSQueueMaximumDepth,
       "alaQoSQueueMaximumBuffers": alaQoSQueueMaximumBuffers,
       "alaQoSQueue8021p": alaQoSQueue8021p,
       "alaQoSQueuePacketsSent": alaQoSQueuePacketsSent,
       "alaQoSQueuePacketsDropped": alaQoSQueuePacketsDropped,
       "alaQoSQueueMaxLength": alaQoSQueueMaxLength,
       "alaQoSQueueAverageLength": alaQoSQueueAverageLength,
       "alaQoSQueueCurrentLength": alaQoSQueueCurrentLength,
       "alaQoSQueueAction": alaQoSQueueAction,
       "alaQoSSlotTable": alaQoSSlotTable,
       "alaQoSSlotEntry": alaQoSSlotEntry,
       "alaQoSSlotSlot": alaQoSSlotSlot,
       "alaQoSSlotSlice": alaQoSSlotSlice,
       "alaQoSSlotType": alaQoSSlotType,
       "alaQoSSlotMaxBuffers": alaQoSSlotMaxBuffers,
       "alaQoSSlotFreeBuffers1": alaQoSSlotFreeBuffers1,
       "alaQoSSlotFreeBuffers2": alaQoSSlotFreeBuffers2,
       "alaQoSSlotThreshold1Low": alaQoSSlotThreshold1Low,
       "alaQoSSlotThreshold1Medium": alaQoSSlotThreshold1Medium,
       "alaQoSSlotThreshold1High": alaQoSSlotThreshold1High,
       "alaQoSSlotThreshold1Urgent": alaQoSSlotThreshold1Urgent,
       "alaQoSSlotThreshold2Low": alaQoSSlotThreshold2Low,
       "alaQoSSlotThreshold2Medium": alaQoSSlotThreshold2Medium,
       "alaQoSSlotThreshold2High": alaQoSSlotThreshold2High,
       "alaQoSSlotThreshold2Urgent": alaQoSSlotThreshold2Urgent,
       "alaQoSSlotBuffersDenied": alaQoSSlotBuffersDenied,
       "alaQoSSlotBuffersDeniedAverage": alaQoSSlotBuffersDeniedAverage,
       "alaQoSSlotBuffersDropped": alaQoSSlotBuffersDropped,
       "alaQoSSlotBuffersDroppedAverage": alaQoSSlotBuffersDroppedAverage,
       "alaQoSSlotWredThresholdP0Lower": alaQoSSlotWredThresholdP0Lower,
       "alaQoSSlotWredThresholdP0Upper": alaQoSSlotWredThresholdP0Upper,
       "alaQoSSlotWredThresholdP1Lower": alaQoSSlotWredThresholdP1Lower,
       "alaQoSSlotWredThresholdP1Upper": alaQoSSlotWredThresholdP1Upper,
       "alaQoSSlotWredThresholdP2Lower": alaQoSSlotWredThresholdP2Lower,
       "alaQoSSlotWredThresholdP2Upper": alaQoSSlotWredThresholdP2Upper,
       "alaQoSSlotWredThresholdP3Lower": alaQoSSlotWredThresholdP3Lower,
       "alaQoSSlotWredThresholdP3Upper": alaQoSSlotWredThresholdP3Upper,
       "alaQoSSlotWredAverageCounterWeight": alaQoSSlotWredAverageCounterWeight,
       "alaQoSSlotWredThresholdStatus": alaQoSSlotWredThresholdStatus,
       "alaQoSSlotCbqThresholdMode": alaQoSSlotCbqThresholdMode,
       "alaQoSSlotCbqThresholdP1": alaQoSSlotCbqThresholdP1,
       "alaQoSSlotCbqThresholdP2": alaQoSSlotCbqThresholdP2,
       "alaQoSSlotCbqThresholdP3": alaQoSSlotCbqThresholdP3,
       "alaQoSSlotHighDensity": alaQoSSlotHighDensity,
       "alaQoSClassify": alaQoSClassify,
       "alaQoSClassifyClassify": alaQoSClassifyClassify,
       "alaQoSClassifyApplied": alaQoSClassifyApplied,
       "alaQoSClassifySourceSlot": alaQoSClassifySourceSlot,
       "alaQoSClassifySourcePort": alaQoSClassifySourcePort,
       "alaQoSClassifySourceInterfaceType": alaQoSClassifySourceInterfaceType,
       "alaQoSClassifyDestinationSlot": alaQoSClassifyDestinationSlot,
       "alaQoSClassifyDestinationPort": alaQoSClassifyDestinationPort,
       "alaQoSClassifyDestinationInterfaceType": alaQoSClassifyDestinationInterfaceType,
       "alaQoSClassifySourceMac": alaQoSClassifySourceMac,
       "alaQoSClassifyDestinationMac": alaQoSClassifyDestinationMac,
       "alaQoSClassifySourceVlan": alaQoSClassifySourceVlan,
       "alaQoSClassifyDestinationVlan": alaQoSClassifyDestinationVlan,
       "alaQoSClassify8021p": alaQoSClassify8021p,
       "alaQoSClassifySourceIp": alaQoSClassifySourceIp,
       "alaQoSClassifyDestinationIp": alaQoSClassifyDestinationIp,
       "alaQoSClassifyMulticastIp": alaQoSClassifyMulticastIp,
       "alaQoSClassifyTos": alaQoSClassifyTos,
       "alaQoSClassifyDscp": alaQoSClassifyDscp,
       "alaQoSClassifyIpProtocol": alaQoSClassifyIpProtocol,
       "alaQoSClassifySourceIpPort": alaQoSClassifySourceIpPort,
       "alaQoSClassifyDestinationIpPort": alaQoSClassifyDestinationIpPort,
       "alaQoSClassifyExecute": alaQoSClassifyExecute,
       "alaQoSClassifyL2SourceResultRule": alaQoSClassifyL2SourceResultRule,
       "alaQoSClassifyL2SourceResultDisposition": alaQoSClassifyL2SourceResultDisposition,
       "alaQoSClassifyL2DestinationResultRule": alaQoSClassifyL2DestinationResultRule,
       "alaQoSClassifyL2DestinationResultDisposition": alaQoSClassifyL2DestinationResultDisposition,
       "alaQoSClassifyL3ResultRule": alaQoSClassifyL3ResultRule,
       "alaQoSClassifyL3ResultDisposition": alaQoSClassifyL3ResultDisposition,
       "alaQoSClassifyIGMPResultRule": alaQoSClassifyIGMPResultRule,
       "alaQoSClassifyIGMPResultDisposition": alaQoSClassifyIGMPResultDisposition,
       "alaQoSClassifyMulticastResultRule": alaQoSClassifyMulticastResultRule,
       "alaQoSClassifyMulticastResultDisposition": alaQoSClassifyMulticastResultDisposition,
       "alaQoSSlotProtocolTable": alaQoSSlotProtocolTable,
       "alaQoSSlotProtocolEntry": alaQoSSlotProtocolEntry,
       "alaQoSSlotProtocolId": alaQoSSlotProtocolId,
       "alaQoSSlotProtocolEthertype": alaQoSSlotProtocolEthertype,
       "alaQoSSlotProtocolDsap": alaQoSSlotProtocolDsap,
       "alaQoSSlotProtocolSsap": alaQoSSlotProtocolSsap,
       "alaQoSSlotProtocol8023Enabled": alaQoSSlotProtocol8023Enabled,
       "alaQoSSlotProtocolType": alaQoSSlotProtocolType,
       "alaQoSSlotProtocolRowStatus": alaQoSSlotProtocolRowStatus,
       "alaQoSPortProtocolTable": alaQoSPortProtocolTable,
       "alaQoSPortProtocolEntry": alaQoSPortProtocolEntry,
       "alaQoSPortProtocolId": alaQoSPortProtocolId,
       "alaQoSPortProtocolClassification": alaQoSPortProtocolClassification,
       "alaQoSPortProtocolPriorityP0": alaQoSPortProtocolPriorityP0,
       "alaQoSPortProtocolPriorityP1": alaQoSPortProtocolPriorityP1,
       "alaQoSPortProtocolPriorityP2": alaQoSPortProtocolPriorityP2,
       "alaQoSPortProtocolPriorityP3": alaQoSPortProtocolPriorityP3,
       "alaQoSPortProtocolPriorityP4": alaQoSPortProtocolPriorityP4,
       "alaQoSPortProtocolPriorityP5": alaQoSPortProtocolPriorityP5,
       "alaQoSPortProtocolPriorityP6": alaQoSPortProtocolPriorityP6,
       "alaQoSPortProtocolPriorityP7": alaQoSPortProtocolPriorityP7,
       "alaQoSPortProtocolRowStatus": alaQoSPortProtocolRowStatus,
       "alaQoSSlotDscpTable": alaQoSSlotDscpTable,
       "alaQoSSlotDscpEntry": alaQoSSlotDscpEntry,
       "alaQoSSlotDscpIndex": alaQoSSlotDscpIndex,
       "alaQoSSlotDscpPriority": alaQoSSlotDscpPriority,
       "alaQoSSlotPcamTable": alaQoSSlotPcamTable,
       "alaQoSSlotPcamEntry": alaQoSSlotPcamEntry,
       "alaQoSSlotPcamId": alaQoSSlotPcamId,
       "alaQoSSlotPcamEthertype": alaQoSSlotPcamEthertype,
       "alaQoSSlotPcamDsap": alaQoSSlotPcamDsap,
       "alaQoSSlotPcamSsap": alaQoSSlotPcamSsap,
       "alaQoSSlotPcam8023Enabled": alaQoSSlotPcam8023Enabled,
       "alaQoSSlotPcamProtocolNumber": alaQoSSlotPcamProtocolNumber,
       "alaQoSSlotPcamEnableEntry": alaQoSSlotPcamEnableEntry,
       "alaQoSSlotPcamEnable8023": alaQoSSlotPcamEnable8023,
       "alaQoSSlotPcamEnableDsap": alaQoSSlotPcamEnableDsap,
       "alaQoSSlotPcamEnableSsap": alaQoSSlotPcamEnableSsap,
       "alaQoSSlotPcamEnableEthertype": alaQoSSlotPcamEnableEthertype,
       "alaQoSPortPdiTable": alaQoSPortPdiTable,
       "alaQoSPortPdiEntry": alaQoSPortPdiEntry,
       "alaQoSPortPdiId": alaQoSPortPdiId,
       "alaQoSPortPdiPriorityType": alaQoSPortPdiPriorityType,
       "alaQoSPortPdiPriorityP0": alaQoSPortPdiPriorityP0,
       "alaQoSPortPdiPriorityP1": alaQoSPortPdiPriorityP1,
       "alaQoSPortPdiPriorityP2": alaQoSPortPdiPriorityP2,
       "alaQoSPortPdiPriorityP3": alaQoSPortPdiPriorityP3,
       "alaQoSPortPdiPriorityP4": alaQoSPortPdiPriorityP4,
       "alaQoSPortPdiPriorityP5": alaQoSPortPdiPriorityP5,
       "alaQoSPortPdiPriorityP6": alaQoSPortPdiPriorityP6,
       "alaQoSPortPdiPriorityP7": alaQoSPortPdiPriorityP7,
       "alaQoSValidityPeriodTable": alaQoSValidityPeriodTable,
       "alaQoSValidityPeriodEntry": alaQoSValidityPeriodEntry,
       "alaQoSValidityPeriodName": alaQoSValidityPeriodName,
       "alaQoSValidityPeriodSource": alaQoSValidityPeriodSource,
       "alaQoSValidityPeriodDays": alaQoSValidityPeriodDays,
       "alaQoSValidityPeriodDaysStatus": alaQoSValidityPeriodDaysStatus,
       "alaQoSValidityPeriodMonths": alaQoSValidityPeriodMonths,
       "alaQoSValidityPeriodMonthsStatus": alaQoSValidityPeriodMonthsStatus,
       "alaQoSValidityPeriodHour": alaQoSValidityPeriodHour,
       "alaQoSValidityPeriodHourStatus": alaQoSValidityPeriodHourStatus,
       "alaQoSValidityPeriodEndHour": alaQoSValidityPeriodEndHour,
       "alaQoSValidityPeriodInterval": alaQoSValidityPeriodInterval,
       "alaQoSValidityPeriodIntervalStatus": alaQoSValidityPeriodIntervalStatus,
       "alaQoSValidityPeriodEndInterval": alaQoSValidityPeriodEndInterval,
       "alaQoSValidityPeriodRowStatus": alaQoSValidityPeriodRowStatus,
       "alaQoSAppliedValidityPeriodTable": alaQoSAppliedValidityPeriodTable,
       "alaQoSAppliedValidityPeriodEntry": alaQoSAppliedValidityPeriodEntry,
       "alaQoSAppliedValidityPeriodName": alaQoSAppliedValidityPeriodName,
       "alaQoSAppliedValidityPeriodSource": alaQoSAppliedValidityPeriodSource,
       "alaQoSAppliedValidityPeriodDays": alaQoSAppliedValidityPeriodDays,
       "alaQoSAppliedValidityPeriodDaysStatus": alaQoSAppliedValidityPeriodDaysStatus,
       "alaQoSAppliedValidityPeriodMonths": alaQoSAppliedValidityPeriodMonths,
       "alaQoSAppliedValidityPeriodMonthsStatus": alaQoSAppliedValidityPeriodMonthsStatus,
       "alaQoSAppliedValidityPeriodHour": alaQoSAppliedValidityPeriodHour,
       "alaQoSAppliedValidityPeriodHourStatus": alaQoSAppliedValidityPeriodHourStatus,
       "alaQoSAppliedValidityPeriodEndHour": alaQoSAppliedValidityPeriodEndHour,
       "alaQoSAppliedValidityPeriodInterval": alaQoSAppliedValidityPeriodInterval,
       "alaQoSAppliedValidityPeriodIntervalStatus": alaQoSAppliedValidityPeriodIntervalStatus,
       "alaQoSAppliedValidityPeriodEndInterval": alaQoSAppliedValidityPeriodEndInterval,
       "alaQoSAppliedValidityPeriodRowStatus": alaQoSAppliedValidityPeriodRowStatus,
       "alaQoSImportTable": alaQoSImportTable,
       "alaQoSImportEntry": alaQoSImportEntry,
       "alaQoSImportIndex": alaQoSImportIndex,
       "alaQoSImportText": alaQoSImportText,
       "alaQoSImportPrecedence": alaQoSImportPrecedence,
       "alaQoSImportPrefix": alaQoSImportPrefix,
       "alaQoSImportSlot": alaQoSImportSlot,
       "alaQoSImportPort": alaQoSImportPort,
       "alaQoSImportPortend": alaQoSImportPortend,
       "alaQoSImportPortgroup": alaQoSImportPortgroup,
       "alaQoSImportRowStatus": alaQoSImportRowStatus,
       "alaQoSAppliedImportTable": alaQoSAppliedImportTable,
       "alaQoSAppliedImportEntry": alaQoSAppliedImportEntry,
       "alaQoSAppliedImportIndex": alaQoSAppliedImportIndex,
       "alaQoSAppliedImportText": alaQoSAppliedImportText,
       "alaQoSAppliedImportPrecedence": alaQoSAppliedImportPrecedence,
       "alaQoSAppliedImportPrefix": alaQoSAppliedImportPrefix,
       "alaQoSAppliedImportSlot": alaQoSAppliedImportSlot,
       "alaQoSAppliedImportPort": alaQoSAppliedImportPort,
       "alaQoSAppliedImportPortend": alaQoSAppliedImportPortend,
       "alaQoSAppliedImportPortgroup": alaQoSAppliedImportPortgroup,
       "alaQoSAppliedImportRowStatus": alaQoSAppliedImportRowStatus,
       "alaQoSRuleGroupsTable": alaQoSRuleGroupsTable,
       "alaQoSRuleGroupsEntry": alaQoSRuleGroupsEntry,
       "alaQoSRuleGroupsName": alaQoSRuleGroupsName,
       "alaQoSRuleGroupsSource": alaQoSRuleGroupsSource,
       "alaQoSRuleGroupsType": alaQoSRuleGroupsType,
       "alaQoSRuleGroupsEnabled": alaQoSRuleGroupsEnabled,
       "alaQoSRuleGroupsStatus": alaQoSRuleGroupsStatus,
       "alaQoSAppliedRuleGroupsTable": alaQoSAppliedRuleGroupsTable,
       "alaQoSAppliedRuleGroupsEntry": alaQoSAppliedRuleGroupsEntry,
       "alaQoSAppliedRuleGroupsName": alaQoSAppliedRuleGroupsName,
       "alaQoSAppliedRuleGroupsSource": alaQoSAppliedRuleGroupsSource,
       "alaQoSAppliedRuleGroupsType": alaQoSAppliedRuleGroupsType,
       "alaQoSAppliedRuleGroupsEnabled": alaQoSAppliedRuleGroupsEnabled,
       "alaQoSAppliedRuleGroupsStatus": alaQoSAppliedRuleGroupsStatus,
       "alaQoSRuleGroupTable": alaQoSRuleGroupTable,
       "alaQoSRuleGroupEntry": alaQoSRuleGroupEntry,
       "alaQoSRuleGroupRuleName": alaQoSRuleGroupRuleName,
       "alaQoSRuleGroupMatches": alaQoSRuleGroupMatches,
       "alaQoSRuleGroupCountType": alaQoSRuleGroupCountType,
       "alaQoSRuleGroupPacketCount": alaQoSRuleGroupPacketCount,
       "alaQoSRuleGroupByteCount": alaQoSRuleGroupByteCount,
       "alaQoSRuleGroupStatus": alaQoSRuleGroupStatus,
       "alaQoSAppliedRuleGroupTable": alaQoSAppliedRuleGroupTable,
       "alaQoSAppliedRuleGroupEntry": alaQoSAppliedRuleGroupEntry,
       "alaQoSAppliedRuleGroupRuleName": alaQoSAppliedRuleGroupRuleName,
       "alaQoSAppliedRuleGroupMatches": alaQoSAppliedRuleGroupMatches,
       "alaQoSAppliedRuleGroupCountType": alaQoSAppliedRuleGroupCountType,
       "alaQoSAppliedRuleGroupPacketCount": alaQoSAppliedRuleGroupPacketCount,
       "alaQoSAppliedRuleGroupByteCount": alaQoSAppliedRuleGroupByteCount,
       "alaQoSAppliedRuleGroupStatus": alaQoSAppliedRuleGroupStatus,
       "alaQoSVlanGroupsTable": alaQoSVlanGroupsTable,
       "alaQoSVlanGroupsEntry": alaQoSVlanGroupsEntry,
       "alaQoSVlanGroupsName": alaQoSVlanGroupsName,
       "alaQoSVlanGroupsSource": alaQoSVlanGroupsSource,
       "alaQoSVlanGroupsStatus": alaQoSVlanGroupsStatus,
       "alaQoSAppliedVlanGroupsTable": alaQoSAppliedVlanGroupsTable,
       "alaQoSAppliedVlanGroupsEntry": alaQoSAppliedVlanGroupsEntry,
       "alaQoSAppliedVlanGroupsName": alaQoSAppliedVlanGroupsName,
       "alaQoSAppliedVlanGroupsSource": alaQoSAppliedVlanGroupsSource,
       "alaQoSAppliedVlanGroupsStatus": alaQoSAppliedVlanGroupsStatus,
       "alaQoSVlanGroupTable": alaQoSVlanGroupTable,
       "alaQoSVlanGroupEntry": alaQoSVlanGroupEntry,
       "alaQoSVlanGroupVlan": alaQoSVlanGroupVlan,
       "alaQoSVlanGroupVlanEnd": alaQoSVlanGroupVlanEnd,
       "alaQoSVlanGroupStatus": alaQoSVlanGroupStatus,
       "alaQoSAppliedVlanGroupTable": alaQoSAppliedVlanGroupTable,
       "alaQoSAppliedVlanGroupEntry": alaQoSAppliedVlanGroupEntry,
       "alaQoSAppliedVlanGroupVlan": alaQoSAppliedVlanGroupVlan,
       "alaQoSAppliedVlanGroupVlanEnd": alaQoSAppliedVlanGroupVlanEnd,
       "alaQoSAppliedVlanGroupStatus": alaQoSAppliedVlanGroupStatus,
       "alaQoSHwLoopbackProfileTable": alaQoSHwLoopbackProfileTable,
       "alaQoSHwLoopbackProfileEntry": alaQoSHwLoopbackProfileEntry,
       "alaQoSHwLoopbackProfileName": alaQoSHwLoopbackProfileName,
       "alaQoSHwLoopbackSourceMac": alaQoSHwLoopbackSourceMac,
       "alaQoSHwLoopbackDestinationMac": alaQoSHwLoopbackDestinationMac,
       "alaQoSHwLoopbackVlan": alaQoSHwLoopbackVlan,
       "alaQoSHwLoopbackPort": alaQoSHwLoopbackPort,
       "alaQoSHwLoopbackType": alaQoSHwLoopbackType,
       "alaQoSHwLoopbackProfileStatus": alaQoSHwLoopbackProfileStatus,
       "alaQoSHwLoopbackProfileRowStatus": alaQoSHwLoopbackProfileRowStatus,
       "alaQoSMIBConformance": alaQoSMIBConformance,
       "alaQoSMIBGroups": alaQoSMIBGroups,
       "alaQoSMIBRuleObjects": alaQoSMIBRuleObjects,
       "alaQoSMIBAppliedRuleObjects": alaQoSMIBAppliedRuleObjects,
       "alaQoSMIBConditionObjects": alaQoSMIBConditionObjects,
       "alaQoSMIBAppliedConditionObjects": alaQoSMIBAppliedConditionObjects,
       "alaQoSMIBServiceObjects": alaQoSMIBServiceObjects,
       "alaQoSMIBAppliedServiceObjects": alaQoSMIBAppliedServiceObjects,
       "alaQoSMIBServiceGroupsObjects": alaQoSMIBServiceGroupsObjects,
       "alaQoSMIBAppliedServiceGroupsObjects": alaQoSMIBAppliedServiceGroupsObjects,
       "alaQoSMIBServiceGroupObjects": alaQoSMIBServiceGroupObjects,
       "alaQoSMIBAppliedServiceGroupObjects": alaQoSMIBAppliedServiceGroupObjects,
       "alaQoSMIBNetworkGroupsObjects": alaQoSMIBNetworkGroupsObjects,
       "alaQoSMIBAppliedNetworkGroupsObjects": alaQoSMIBAppliedNetworkGroupsObjects,
       "alaQoSMIBNetworkGroupObjects": alaQoSMIBNetworkGroupObjects,
       "alaQoSMIBAppliedNetworkGroupObjects": alaQoSMIBAppliedNetworkGroupObjects,
       "alaQoSMIBMACGroupsObjects": alaQoSMIBMACGroupsObjects,
       "alaQoSMIBAppliedMACGroupsObjects": alaQoSMIBAppliedMACGroupsObjects,
       "alaQoSMIBMACGroupObjects": alaQoSMIBMACGroupObjects,
       "alaQoSMIBAppliedMACGroupObjects": alaQoSMIBAppliedMACGroupObjects,
       "alaQoSMIBPortGroupsObjects": alaQoSMIBPortGroupsObjects,
       "alaQoSMIBAppliedPortGroupsObjects": alaQoSMIBAppliedPortGroupsObjects,
       "alaQoSMIBPortGroupObjects": alaQoSMIBPortGroupObjects,
       "alaQoSMIBAppliedPortGroupObjects": alaQoSMIBAppliedPortGroupObjects,
       "alaQoSMIBMapGroupsObjects": alaQoSMIBMapGroupsObjects,
       "alaQoSMIBAppliedMapGroupsObjects": alaQoSMIBAppliedMapGroupsObjects,
       "alaQoSMIBMapGroupObjects": alaQoSMIBMapGroupObjects,
       "alaQoSMIBAppliedMapGroupObjects": alaQoSMIBAppliedMapGroupObjects,
       "alaQoSMIBActionObjects": alaQoSMIBActionObjects,
       "alaQoSMIBAppliedActionObjects": alaQoSMIBAppliedActionObjects,
       "alaQoSMIBPortObjects": alaQoSMIBPortObjects,
       "alaQoSMIBConfigObjects": alaQoSMIBConfigObjects,
       "alaQoSMIBStatsObjects": alaQoSMIBStatsObjects,
       "alaQoSMIBQueueObjects": alaQoSMIBQueueObjects,
       "alaQoSMIBSlotObjects": alaQoSMIBSlotObjects,
       "alaQoSMIBClassifyObjects": alaQoSMIBClassifyObjects,
       "alaQoSMIBRuleGroupsObjects": alaQoSMIBRuleGroupsObjects,
       "alaQoSMIBAppliedRuleGroupsObjects": alaQoSMIBAppliedRuleGroupsObjects,
       "alaQoSMIBRuleGroupObjects": alaQoSMIBRuleGroupObjects,
       "alaQoSMIBAppliedRuleGroupObjects": alaQoSMIBAppliedRuleGroupObjects,
       "alaQoSVlanGroupsObjects": alaQoSVlanGroupsObjects,
       "alaQoSAppliedVlanGroupsObjects": alaQoSAppliedVlanGroupsObjects,
       "alaQoSVlanGroupObjects": alaQoSVlanGroupObjects,
       "alaQoSAppliedVlanGroupObjects": alaQoSAppliedVlanGroupObjects,
       "alaQoSMIBHwLoopBackProfileObjects": alaQoSMIBHwLoopBackProfileObjects,
       "alaQoSMIBCompliances": alaQoSMIBCompliances,
       "alaQoSMIBCompliance": alaQoSMIBCompliance}
)
