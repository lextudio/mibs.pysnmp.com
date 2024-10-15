# SNMP MIB module (EXTREME-CLEARFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-CLEARFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:27 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

extremeClearflow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeClearflowTraps_ObjectIdentity = ObjectIdentity
extremeClearflowTraps = _ExtremeClearflowTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 0)
)
_ExtremeClearflowTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeClearflowTrapsPrefix = _ExtremeClearflowTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 0, 0)
)
_ExtremeClearflowMsgId_Type = Unsigned32
_ExtremeClearflowMsgId_Object = MibScalar
extremeClearflowMsgId = _ExtremeClearflowMsgId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 1),
    _ExtremeClearflowMsgId_Type()
)
extremeClearflowMsgId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowMsgId.setStatus("current")


class _ExtremeClearflowMsg_Type(DisplayString):
    """Custom type extremeClearflowMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_ExtremeClearflowMsg_Type.__name__ = "DisplayString"
_ExtremeClearflowMsg_Object = MibScalar
extremeClearflowMsg = _ExtremeClearflowMsg_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 2),
    _ExtremeClearflowMsg_Type()
)
extremeClearflowMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowMsg.setStatus("current")


class _ExtremeClearflowPolicyName_Type(DisplayString):
    """Custom type extremeClearflowPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeClearflowPolicyName_Type.__name__ = "DisplayString"
_ExtremeClearflowPolicyName_Object = MibScalar
extremeClearflowPolicyName = _ExtremeClearflowPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 3),
    _ExtremeClearflowPolicyName_Type()
)
extremeClearflowPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowPolicyName.setStatus("current")


class _ExtremeClearflowRuleName_Type(DisplayString):
    """Custom type extremeClearflowRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeClearflowRuleName_Type.__name__ = "DisplayString"
_ExtremeClearflowRuleName_Object = MibScalar
extremeClearflowRuleName = _ExtremeClearflowRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 4),
    _ExtremeClearflowRuleName_Type()
)
extremeClearflowRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowRuleName.setStatus("current")
_ExtremeClearflowRuleValue_Type = Counter64
_ExtremeClearflowRuleValue_Object = MibScalar
extremeClearflowRuleValue = _ExtremeClearflowRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 5),
    _ExtremeClearflowRuleValue_Type()
)
extremeClearflowRuleValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowRuleValue.setStatus("current")
_ExtremeClearflowRuleThreshold_Type = Counter64
_ExtremeClearflowRuleThreshold_Object = MibScalar
extremeClearflowRuleThreshold = _ExtremeClearflowRuleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 6),
    _ExtremeClearflowRuleThreshold_Type()
)
extremeClearflowRuleThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowRuleThreshold.setStatus("current")
_ExtremeClearflowRuleInterval_Type = Unsigned32
_ExtremeClearflowRuleInterval_Object = MibScalar
extremeClearflowRuleInterval = _ExtremeClearflowRuleInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 7),
    _ExtremeClearflowRuleInterval_Type()
)
extremeClearflowRuleInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowRuleInterval.setStatus("current")


class _ExtremeClearflowVlanName_Type(DisplayString):
    """Custom type extremeClearflowVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeClearflowVlanName_Type.__name__ = "DisplayString"
_ExtremeClearflowVlanName_Object = MibScalar
extremeClearflowVlanName = _ExtremeClearflowVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 8),
    _ExtremeClearflowVlanName_Type()
)
extremeClearflowVlanName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowVlanName.setStatus("current")


class _ExtremeClearflowPortName_Type(DisplayString):
    """Custom type extremeClearflowPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeClearflowPortName_Type.__name__ = "DisplayString"
_ExtremeClearflowPortName_Object = MibScalar
extremeClearflowPortName = _ExtremeClearflowPortName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 9),
    _ExtremeClearflowPortName_Type()
)
extremeClearflowPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeClearflowPortName.setStatus("current")
_ExtremeAclListTable_Object = MibTable
extremeAclListTable = _ExtremeAclListTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10)
)
if mibBuilder.loadTexts:
    extremeAclListTable.setStatus("current")
_ExtremeAclListEntry_Object = MibTableRow
extremeAclListEntry = _ExtremeAclListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1)
)
extremeAclListEntry.setIndexNames(
    (0, "EXTREME-CLEARFLOW-MIB", "extremeAclVlanIfIndex"),
    (0, "EXTREME-CLEARFLOW-MIB", "extremeAclPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeAclListEntry.setStatus("current")


class _ExtremeAclPortIfIndex_Type(Integer32):
    """Custom type extremeAclPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeAclPortIfIndex_Type.__name__ = "Integer32"
_ExtremeAclPortIfIndex_Object = MibTableColumn
extremeAclPortIfIndex = _ExtremeAclPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 1),
    _ExtremeAclPortIfIndex_Type()
)
extremeAclPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclPortIfIndex.setStatus("current")
_ExtremeAclVlanIfIndex_Type = Integer32
_ExtremeAclVlanIfIndex_Object = MibTableColumn
extremeAclVlanIfIndex = _ExtremeAclVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 2),
    _ExtremeAclVlanIfIndex_Type()
)
extremeAclVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclVlanIfIndex.setStatus("current")


class _ExtremeAclCounterName_Type(DisplayString):
    """Custom type extremeAclCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ExtremeAclCounterName_Type.__name__ = "DisplayString"
_ExtremeAclCounterName_Object = MibTableColumn
extremeAclCounterName = _ExtremeAclCounterName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 3),
    _ExtremeAclCounterName_Type()
)
extremeAclCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclCounterName.setStatus("current")


class _ExtremeAclVlanName_Type(DisplayString):
    """Custom type extremeAclVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeAclVlanName_Type.__name__ = "DisplayString"
_ExtremeAclVlanName_Object = MibTableColumn
extremeAclVlanName = _ExtremeAclVlanName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 4),
    _ExtremeAclVlanName_Type()
)
extremeAclVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclVlanName.setStatus("current")
_ExtremeAclPolicyName_Type = DisplayString
_ExtremeAclPolicyName_Object = MibTableColumn
extremeAclPolicyName = _ExtremeAclPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 5),
    _ExtremeAclPolicyName_Type()
)
extremeAclPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclPolicyName.setStatus("current")
_ExtremeAclDirection_Type = Integer32
_ExtremeAclDirection_Object = MibTableColumn
extremeAclDirection = _ExtremeAclDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 6),
    _ExtremeAclDirection_Type()
)
extremeAclDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclDirection.setStatus("current")
_ExtremeAclPktCount_Type = Counter64
_ExtremeAclPktCount_Object = MibTableColumn
extremeAclPktCount = _ExtremeAclPktCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 7),
    _ExtremeAclPktCount_Type()
)
extremeAclPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclPktCount.setStatus("current")
_ExtremeAclByteCount_Type = Counter64
_ExtremeAclByteCount_Object = MibTableColumn
extremeAclByteCount = _ExtremeAclByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 10, 1, 8),
    _ExtremeAclByteCount_Type()
)
extremeAclByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeAclByteCount.setStatus("current")
_ExtremeTrafficQueueStatsTable_Object = MibTable
extremeTrafficQueueStatsTable = _ExtremeTrafficQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11)
)
if mibBuilder.loadTexts:
    extremeTrafficQueueStatsTable.setStatus("current")
_ExtremeTrafficQueueStatsTableEntry_Object = MibTableRow
extremeTrafficQueueStatsTableEntry = _ExtremeTrafficQueueStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1)
)
extremeTrafficQueueStatsTableEntry.setIndexNames(
    (0, "EXTREME-CLEARFLOW-MIB", "extremeTrafficQueueName"),
)
if mibBuilder.loadTexts:
    extremeTrafficQueueStatsTableEntry.setStatus("current")


class _ExtremeTrafficQueueName_Type(DisplayString):
    """Custom type extremeTrafficQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ExtremeTrafficQueueName_Type.__name__ = "DisplayString"
_ExtremeTrafficQueueName_Object = MibTableColumn
extremeTrafficQueueName = _ExtremeTrafficQueueName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 1),
    _ExtremeTrafficQueueName_Type()
)
extremeTrafficQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueName.setStatus("current")
_ExtremeTrafficQueueDirection_Type = Integer32
_ExtremeTrafficQueueDirection_Object = MibTableColumn
extremeTrafficQueueDirection = _ExtremeTrafficQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 2),
    _ExtremeTrafficQueueDirection_Type()
)
extremeTrafficQueueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueDirection.setStatus("current")
_ExtremeTrafficQueueHighPassedPkts_Type = Counter64
_ExtremeTrafficQueueHighPassedPkts_Object = MibTableColumn
extremeTrafficQueueHighPassedPkts = _ExtremeTrafficQueueHighPassedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 3),
    _ExtremeTrafficQueueHighPassedPkts_Type()
)
extremeTrafficQueueHighPassedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueHighPassedPkts.setStatus("current")
_ExtremeTrafficQueueHighPassedBytes_Type = Counter64
_ExtremeTrafficQueueHighPassedBytes_Object = MibTableColumn
extremeTrafficQueueHighPassedBytes = _ExtremeTrafficQueueHighPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 4),
    _ExtremeTrafficQueueHighPassedBytes_Type()
)
extremeTrafficQueueHighPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueHighPassedBytes.setStatus("current")
_ExtremeTrafficQueueHighDroppedPkts_Type = Counter64
_ExtremeTrafficQueueHighDroppedPkts_Object = MibTableColumn
extremeTrafficQueueHighDroppedPkts = _ExtremeTrafficQueueHighDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 5),
    _ExtremeTrafficQueueHighDroppedPkts_Type()
)
extremeTrafficQueueHighDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueHighDroppedPkts.setStatus("current")
_ExtremeTrafficQueueHighDroppedBytes_Type = Counter64
_ExtremeTrafficQueueHighDroppedBytes_Object = MibTableColumn
extremeTrafficQueueHighDroppedBytes = _ExtremeTrafficQueueHighDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 6),
    _ExtremeTrafficQueueHighDroppedBytes_Type()
)
extremeTrafficQueueHighDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueHighDroppedBytes.setStatus("current")
_ExtremeTrafficQueueMedPassedPkts_Type = Counter64
_ExtremeTrafficQueueMedPassedPkts_Object = MibTableColumn
extremeTrafficQueueMedPassedPkts = _ExtremeTrafficQueueMedPassedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 7),
    _ExtremeTrafficQueueMedPassedPkts_Type()
)
extremeTrafficQueueMedPassedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueMedPassedPkts.setStatus("current")
_ExtremeTrafficQueueMedPassedBytes_Type = Counter64
_ExtremeTrafficQueueMedPassedBytes_Object = MibTableColumn
extremeTrafficQueueMedPassedBytes = _ExtremeTrafficQueueMedPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 8),
    _ExtremeTrafficQueueMedPassedBytes_Type()
)
extremeTrafficQueueMedPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueMedPassedBytes.setStatus("current")
_ExtremeTrafficQueueMedDroppedPkts_Type = Counter64
_ExtremeTrafficQueueMedDroppedPkts_Object = MibTableColumn
extremeTrafficQueueMedDroppedPkts = _ExtremeTrafficQueueMedDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 9),
    _ExtremeTrafficQueueMedDroppedPkts_Type()
)
extremeTrafficQueueMedDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueMedDroppedPkts.setStatus("current")
_ExtremeTrafficQueueMedDroppedBytes_Type = Counter64
_ExtremeTrafficQueueMedDroppedBytes_Object = MibTableColumn
extremeTrafficQueueMedDroppedBytes = _ExtremeTrafficQueueMedDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 10),
    _ExtremeTrafficQueueMedDroppedBytes_Type()
)
extremeTrafficQueueMedDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueMedDroppedBytes.setStatus("current")
_ExtremeTrafficQueueLowPassedPkts_Type = Counter64
_ExtremeTrafficQueueLowPassedPkts_Object = MibTableColumn
extremeTrafficQueueLowPassedPkts = _ExtremeTrafficQueueLowPassedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 11),
    _ExtremeTrafficQueueLowPassedPkts_Type()
)
extremeTrafficQueueLowPassedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueLowPassedPkts.setStatus("current")
_ExtremeTrafficQueueLowPassedBytes_Type = Counter64
_ExtremeTrafficQueueLowPassedBytes_Object = MibTableColumn
extremeTrafficQueueLowPassedBytes = _ExtremeTrafficQueueLowPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 12),
    _ExtremeTrafficQueueLowPassedBytes_Type()
)
extremeTrafficQueueLowPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueLowPassedBytes.setStatus("current")
_ExtremeTrafficQueueLowDroppedPkts_Type = Counter64
_ExtremeTrafficQueueLowDroppedPkts_Object = MibTableColumn
extremeTrafficQueueLowDroppedPkts = _ExtremeTrafficQueueLowDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 13),
    _ExtremeTrafficQueueLowDroppedPkts_Type()
)
extremeTrafficQueueLowDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueLowDroppedPkts.setStatus("current")
_ExtremeTrafficQueueLowDroppedBytes_Type = Counter64
_ExtremeTrafficQueueLowDroppedBytes_Object = MibTableColumn
extremeTrafficQueueLowDroppedBytes = _ExtremeTrafficQueueLowDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 14),
    _ExtremeTrafficQueueLowDroppedBytes_Type()
)
extremeTrafficQueueLowDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueLowDroppedBytes.setStatus("current")
_ExtremeTrafficQueueAggPassedPkts_Type = Counter64
_ExtremeTrafficQueueAggPassedPkts_Object = MibTableColumn
extremeTrafficQueueAggPassedPkts = _ExtremeTrafficQueueAggPassedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 15),
    _ExtremeTrafficQueueAggPassedPkts_Type()
)
extremeTrafficQueueAggPassedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueAggPassedPkts.setStatus("current")
_ExtremeTrafficQueueAggPassedBytes_Type = Counter64
_ExtremeTrafficQueueAggPassedBytes_Object = MibTableColumn
extremeTrafficQueueAggPassedBytes = _ExtremeTrafficQueueAggPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 16),
    _ExtremeTrafficQueueAggPassedBytes_Type()
)
extremeTrafficQueueAggPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueAggPassedBytes.setStatus("current")
_ExtremeTrafficQueueAggDroppedPkts_Type = Counter64
_ExtremeTrafficQueueAggDroppedPkts_Object = MibTableColumn
extremeTrafficQueueAggDroppedPkts = _ExtremeTrafficQueueAggDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 17),
    _ExtremeTrafficQueueAggDroppedPkts_Type()
)
extremeTrafficQueueAggDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueAggDroppedPkts.setStatus("current")
_ExtremeTrafficQueueAggDroppedBytes_Type = Counter64
_ExtremeTrafficQueueAggDroppedBytes_Object = MibTableColumn
extremeTrafficQueueAggDroppedBytes = _ExtremeTrafficQueueAggDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 11, 1, 18),
    _ExtremeTrafficQueueAggDroppedBytes_Type()
)
extremeTrafficQueueAggDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueAggDroppedBytes.setStatus("current")
_ExtremeTrafficQueueUtilTable_Object = MibTable
extremeTrafficQueueUtilTable = _ExtremeTrafficQueueUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 12)
)
if mibBuilder.loadTexts:
    extremeTrafficQueueUtilTable.setStatus("current")
_ExtremeTrafficQueueUtilTableEntry_Object = MibTableRow
extremeTrafficQueueUtilTableEntry = _ExtremeTrafficQueueUtilTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 12, 1)
)
extremeTrafficQueueUtilTableEntry.setIndexNames(
    (0, "EXTREME-CLEARFLOW-MIB", "extremeUtilTrafficQueueName"),
)
if mibBuilder.loadTexts:
    extremeTrafficQueueUtilTableEntry.setStatus("current")


class _ExtremeUtilTrafficQueueName_Type(DisplayString):
    """Custom type extremeUtilTrafficQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ExtremeUtilTrafficQueueName_Type.__name__ = "DisplayString"
_ExtremeUtilTrafficQueueName_Object = MibTableColumn
extremeUtilTrafficQueueName = _ExtremeUtilTrafficQueueName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 12, 1, 1),
    _ExtremeUtilTrafficQueueName_Type()
)
extremeUtilTrafficQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeUtilTrafficQueueName.setStatus("current")
_ExtremeUtilTrafficQueueDirection_Type = Integer32
_ExtremeUtilTrafficQueueDirection_Object = MibTableColumn
extremeUtilTrafficQueueDirection = _ExtremeUtilTrafficQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 12, 1, 2),
    _ExtremeUtilTrafficQueueDirection_Type()
)
extremeUtilTrafficQueueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeUtilTrafficQueueDirection.setStatus("current")
_ExtremeTrafficQueueHighUtilization_Type = DisplayString
_ExtremeTrafficQueueHighUtilization_Object = MibTableColumn
extremeTrafficQueueHighUtilization = _ExtremeTrafficQueueHighUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 12, 1, 3),
    _ExtremeTrafficQueueHighUtilization_Type()
)
extremeTrafficQueueHighUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueHighUtilization.setStatus("current")
_ExtremeTrafficQueueMedUtilization_Type = DisplayString
_ExtremeTrafficQueueMedUtilization_Object = MibTableColumn
extremeTrafficQueueMedUtilization = _ExtremeTrafficQueueMedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 12, 1, 4),
    _ExtremeTrafficQueueMedUtilization_Type()
)
extremeTrafficQueueMedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueMedUtilization.setStatus("current")
_ExtremeTrafficQueueLowUtilization_Type = DisplayString
_ExtremeTrafficQueueLowUtilization_Object = MibTableColumn
extremeTrafficQueueLowUtilization = _ExtremeTrafficQueueLowUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 12, 1, 5),
    _ExtremeTrafficQueueLowUtilization_Type()
)
extremeTrafficQueueLowUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeTrafficQueueLowUtilization.setStatus("current")

# Managed Objects groups


# Notification objects

extremeClearflowMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30, 0, 0, 1)
)
extremeClearflowMessage.setObjects(
      *(("EXTREME-CLEARFLOW-MIB", "extremeClearflowMsgId"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowMsg"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowPolicyName"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowRuleName"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowRuleValue"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowRuleThreshold"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowRuleInterval"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowVlanName"),
        ("EXTREME-CLEARFLOW-MIB", "extremeClearflowPortName"))
)
if mibBuilder.loadTexts:
    extremeClearflowMessage.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-CLEARFLOW-MIB",
    **{"extremeClearflow": extremeClearflow,
       "extremeClearflowTraps": extremeClearflowTraps,
       "extremeClearflowTrapsPrefix": extremeClearflowTrapsPrefix,
       "extremeClearflowMessage": extremeClearflowMessage,
       "extremeClearflowMsgId": extremeClearflowMsgId,
       "extremeClearflowMsg": extremeClearflowMsg,
       "extremeClearflowPolicyName": extremeClearflowPolicyName,
       "extremeClearflowRuleName": extremeClearflowRuleName,
       "extremeClearflowRuleValue": extremeClearflowRuleValue,
       "extremeClearflowRuleThreshold": extremeClearflowRuleThreshold,
       "extremeClearflowRuleInterval": extremeClearflowRuleInterval,
       "extremeClearflowVlanName": extremeClearflowVlanName,
       "extremeClearflowPortName": extremeClearflowPortName,
       "extremeAclListTable": extremeAclListTable,
       "extremeAclListEntry": extremeAclListEntry,
       "extremeAclPortIfIndex": extremeAclPortIfIndex,
       "extremeAclVlanIfIndex": extremeAclVlanIfIndex,
       "extremeAclCounterName": extremeAclCounterName,
       "extremeAclVlanName": extremeAclVlanName,
       "extremeAclPolicyName": extremeAclPolicyName,
       "extremeAclDirection": extremeAclDirection,
       "extremeAclPktCount": extremeAclPktCount,
       "extremeAclByteCount": extremeAclByteCount,
       "extremeTrafficQueueStatsTable": extremeTrafficQueueStatsTable,
       "extremeTrafficQueueStatsTableEntry": extremeTrafficQueueStatsTableEntry,
       "extremeTrafficQueueName": extremeTrafficQueueName,
       "extremeTrafficQueueDirection": extremeTrafficQueueDirection,
       "extremeTrafficQueueHighPassedPkts": extremeTrafficQueueHighPassedPkts,
       "extremeTrafficQueueHighPassedBytes": extremeTrafficQueueHighPassedBytes,
       "extremeTrafficQueueHighDroppedPkts": extremeTrafficQueueHighDroppedPkts,
       "extremeTrafficQueueHighDroppedBytes": extremeTrafficQueueHighDroppedBytes,
       "extremeTrafficQueueMedPassedPkts": extremeTrafficQueueMedPassedPkts,
       "extremeTrafficQueueMedPassedBytes": extremeTrafficQueueMedPassedBytes,
       "extremeTrafficQueueMedDroppedPkts": extremeTrafficQueueMedDroppedPkts,
       "extremeTrafficQueueMedDroppedBytes": extremeTrafficQueueMedDroppedBytes,
       "extremeTrafficQueueLowPassedPkts": extremeTrafficQueueLowPassedPkts,
       "extremeTrafficQueueLowPassedBytes": extremeTrafficQueueLowPassedBytes,
       "extremeTrafficQueueLowDroppedPkts": extremeTrafficQueueLowDroppedPkts,
       "extremeTrafficQueueLowDroppedBytes": extremeTrafficQueueLowDroppedBytes,
       "extremeTrafficQueueAggPassedPkts": extremeTrafficQueueAggPassedPkts,
       "extremeTrafficQueueAggPassedBytes": extremeTrafficQueueAggPassedBytes,
       "extremeTrafficQueueAggDroppedPkts": extremeTrafficQueueAggDroppedPkts,
       "extremeTrafficQueueAggDroppedBytes": extremeTrafficQueueAggDroppedBytes,
       "extremeTrafficQueueUtilTable": extremeTrafficQueueUtilTable,
       "extremeTrafficQueueUtilTableEntry": extremeTrafficQueueUtilTableEntry,
       "extremeUtilTrafficQueueName": extremeUtilTrafficQueueName,
       "extremeUtilTrafficQueueDirection": extremeUtilTrafficQueueDirection,
       "extremeTrafficQueueHighUtilization": extremeTrafficQueueHighUtilization,
       "extremeTrafficQueueMedUtilization": extremeTrafficQueueMedUtilization,
       "extremeTrafficQueueLowUtilization": extremeTrafficQueueLowUtilization}
)
