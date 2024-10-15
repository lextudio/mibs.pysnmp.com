# SNMP MIB module (IEEE8021-DDCFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-DDCFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:17 2024
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

(Dot1agCfmMDLevel,
 Dot1agCfmMpDirection) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMpDirection")

(ieee802dot1mibs,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "ieee802dot1mibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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

ieee8021DdcfmMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11)
)
ieee8021DdcfmMIB.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2009-04-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021MIBObjects_ObjectIdentity = ObjectIdentity
ieee8021MIBObjects = _Ieee8021MIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 1)
)
_Ieee8021DdcfmStack_ObjectIdentity = ObjectIdentity
ieee8021DdcfmStack = _Ieee8021DdcfmStack_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1)
)
_Ieee8021DdcfmStackTable_Object = MibTable
ieee8021DdcfmStackTable = _Ieee8021DdcfmStackTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021DdcfmStackTable.setStatus("current")
_Ieee8021DdcfmStackEntry_Object = MibTableRow
ieee8021DdcfmStackEntry = _Ieee8021DdcfmStackEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1)
)
ieee8021DdcfmStackEntry.setIndexNames(
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021DdcfmStackEntry.setStatus("current")
_Ieee8021DdcfmStackIfIndex_Type = InterfaceIndex
_Ieee8021DdcfmStackIfIndex_Object = MibTableColumn
ieee8021DdcfmStackIfIndex = _Ieee8021DdcfmStackIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 1),
    _Ieee8021DdcfmStackIfIndex_Type()
)
ieee8021DdcfmStackIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackIfIndex.setStatus("current")
_Ieee8021DdcfmStackRrMdLevel_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmStackRrMdLevel_Object = MibTableColumn
ieee8021DdcfmStackRrMdLevel = _Ieee8021DdcfmStackRrMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 2),
    _Ieee8021DdcfmStackRrMdLevel_Type()
)
ieee8021DdcfmStackRrMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackRrMdLevel.setStatus("current")
_Ieee8021DdcfmStackRrDirection_Type = Dot1agCfmMpDirection
_Ieee8021DdcfmStackRrDirection_Object = MibTableColumn
ieee8021DdcfmStackRrDirection = _Ieee8021DdcfmStackRrDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 3),
    _Ieee8021DdcfmStackRrDirection_Type()
)
ieee8021DdcfmStackRrDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackRrDirection.setStatus("current")
_Ieee8021DdcfmStackRFMreceiverMdLevel_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmStackRFMreceiverMdLevel_Object = MibTableColumn
ieee8021DdcfmStackRFMreceiverMdLevel = _Ieee8021DdcfmStackRFMreceiverMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 4),
    _Ieee8021DdcfmStackRFMreceiverMdLevel_Type()
)
ieee8021DdcfmStackRFMreceiverMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackRFMreceiverMdLevel.setStatus("current")
_Ieee8021DdcfmStackDrMdLevel_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmStackDrMdLevel_Object = MibTableColumn
ieee8021DdcfmStackDrMdLevel = _Ieee8021DdcfmStackDrMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 5),
    _Ieee8021DdcfmStackDrMdLevel_Type()
)
ieee8021DdcfmStackDrMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackDrMdLevel.setStatus("current")
_Ieee8021DdcfmStackDrVlanIdOrNone_Type = VlanIdOrNone
_Ieee8021DdcfmStackDrVlanIdOrNone_Object = MibTableColumn
ieee8021DdcfmStackDrVlanIdOrNone = _Ieee8021DdcfmStackDrVlanIdOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 6),
    _Ieee8021DdcfmStackDrVlanIdOrNone_Type()
)
ieee8021DdcfmStackDrVlanIdOrNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackDrVlanIdOrNone.setStatus("current")
_Ieee8021DdcfmStackSFMOriginatorMdLevel_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmStackSFMOriginatorMdLevel_Object = MibTableColumn
ieee8021DdcfmStackSFMOriginatorMdLevel = _Ieee8021DdcfmStackSFMOriginatorMdLevel_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 7),
    _Ieee8021DdcfmStackSFMOriginatorMdLevel_Type()
)
ieee8021DdcfmStackSFMOriginatorMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackSFMOriginatorMdLevel.setStatus("current")
_Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Type = VlanIdOrNone
_Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Object = MibTableColumn
ieee8021DdcfmStackSFMOriginatorVlanIdOrNone = _Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 8),
    _Ieee8021DdcfmStackSFMOriginatorVlanIdOrNone_Type()
)
ieee8021DdcfmStackSFMOriginatorVlanIdOrNone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackSFMOriginatorVlanIdOrNone.setStatus("current")
_Ieee8021DdcfmStackSFMOriginatorDirection_Type = Dot1agCfmMpDirection
_Ieee8021DdcfmStackSFMOriginatorDirection_Object = MibTableColumn
ieee8021DdcfmStackSFMOriginatorDirection = _Ieee8021DdcfmStackSFMOriginatorDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 1, 1, 1, 9),
    _Ieee8021DdcfmStackSFMOriginatorDirection_Type()
)
ieee8021DdcfmStackSFMOriginatorDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmStackSFMOriginatorDirection.setStatus("current")
_Ieee8021DdcfmRr_ObjectIdentity = ObjectIdentity
ieee8021DdcfmRr = _Ieee8021DdcfmRr_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2)
)
_Ieee8021DdcfmRrTable_Object = MibTable
ieee8021DdcfmRrTable = _Ieee8021DdcfmRrTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021DdcfmRrTable.setStatus("current")
_Ieee8021DdcfmRrEntry_Object = MibTableRow
ieee8021DdcfmRrEntry = _Ieee8021DdcfmRrEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1)
)
ieee8021DdcfmRrEntry.setIndexNames(
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrIfIndex"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrMdIndex"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrDirection"),
)
if mibBuilder.loadTexts:
    ieee8021DdcfmRrEntry.setStatus("current")
_Ieee8021DdcfmRrIfIndex_Type = InterfaceIndex
_Ieee8021DdcfmRrIfIndex_Object = MibTableColumn
ieee8021DdcfmRrIfIndex = _Ieee8021DdcfmRrIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 1),
    _Ieee8021DdcfmRrIfIndex_Type()
)
ieee8021DdcfmRrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrIfIndex.setStatus("current")
_Ieee8021DdcfmRrMdIndex_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmRrMdIndex_Object = MibTableColumn
ieee8021DdcfmRrMdIndex = _Ieee8021DdcfmRrMdIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 2),
    _Ieee8021DdcfmRrMdIndex_Type()
)
ieee8021DdcfmRrMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrMdIndex.setStatus("current")
_Ieee8021DdcfmRrDirection_Type = Dot1agCfmMpDirection
_Ieee8021DdcfmRrDirection_Object = MibTableColumn
ieee8021DdcfmRrDirection = _Ieee8021DdcfmRrDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 3),
    _Ieee8021DdcfmRrDirection_Type()
)
ieee8021DdcfmRrDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrDirection.setStatus("current")


class _Ieee8021DdcfmRrPrimaryVlanIdOrNone_Type(VlanIdOrNone):
    """Custom type ieee8021DdcfmRrPrimaryVlanIdOrNone based on VlanIdOrNone"""
    defaultValue = 0


_Ieee8021DdcfmRrPrimaryVlanIdOrNone_Object = MibTableColumn
ieee8021DdcfmRrPrimaryVlanIdOrNone = _Ieee8021DdcfmRrPrimaryVlanIdOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 4),
    _Ieee8021DdcfmRrPrimaryVlanIdOrNone_Type()
)
ieee8021DdcfmRrPrimaryVlanIdOrNone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrPrimaryVlanIdOrNone.setStatus("current")


class _Ieee8021DdcfmRrFilter_Type(OctetString):
    """Custom type ieee8021DdcfmRrFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_Ieee8021DdcfmRrFilter_Type.__name__ = "OctetString"
_Ieee8021DdcfmRrFilter_Object = MibTableColumn
ieee8021DdcfmRrFilter = _Ieee8021DdcfmRrFilter_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 5),
    _Ieee8021DdcfmRrFilter_Type()
)
ieee8021DdcfmRrFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrFilter.setStatus("current")
_Ieee8021DdcfmRrSamplingInterval_Type = Unsigned32
_Ieee8021DdcfmRrSamplingInterval_Object = MibTableColumn
ieee8021DdcfmRrSamplingInterval = _Ieee8021DdcfmRrSamplingInterval_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 6),
    _Ieee8021DdcfmRrSamplingInterval_Type()
)
ieee8021DdcfmRrSamplingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrSamplingInterval.setUnits("miliseconds")
_Ieee8021DdcfmRrTargetAddress_Type = MacAddress
_Ieee8021DdcfmRrTargetAddress_Object = MibTableColumn
ieee8021DdcfmRrTargetAddress = _Ieee8021DdcfmRrTargetAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 7),
    _Ieee8021DdcfmRrTargetAddress_Type()
)
ieee8021DdcfmRrTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrTargetAddress.setStatus("current")


class _Ieee8021DdcfmRrContinueFlag_Type(TruthValue):
    """Custom type ieee8021DdcfmRrContinueFlag based on TruthValue"""


_Ieee8021DdcfmRrContinueFlag_Object = MibTableColumn
ieee8021DdcfmRrContinueFlag = _Ieee8021DdcfmRrContinueFlag_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 8),
    _Ieee8021DdcfmRrContinueFlag_Type()
)
ieee8021DdcfmRrContinueFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrContinueFlag.setStatus("current")
_Ieee8021DdcfmRrDuration_Type = Unsigned32
_Ieee8021DdcfmRrDuration_Object = MibTableColumn
ieee8021DdcfmRrDuration = _Ieee8021DdcfmRrDuration_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 9),
    _Ieee8021DdcfmRrDuration_Type()
)
ieee8021DdcfmRrDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrDuration.setStatus("current")


class _Ieee8021DdcfmRrDurationInTimeFlag_Type(TruthValue):
    """Custom type ieee8021DdcfmRrDurationInTimeFlag based on TruthValue"""


_Ieee8021DdcfmRrDurationInTimeFlag_Object = MibTableColumn
ieee8021DdcfmRrDurationInTimeFlag = _Ieee8021DdcfmRrDurationInTimeFlag_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 10),
    _Ieee8021DdcfmRrDurationInTimeFlag_Type()
)
ieee8021DdcfmRrDurationInTimeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrDurationInTimeFlag.setStatus("current")


class _Ieee8021DdcfmRrVlanPriority_Type(Integer32):
    """Custom type ieee8021DdcfmRrVlanPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021DdcfmRrVlanPriority_Type.__name__ = "Integer32"
_Ieee8021DdcfmRrVlanPriority_Object = MibTableColumn
ieee8021DdcfmRrVlanPriority = _Ieee8021DdcfmRrVlanPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 11),
    _Ieee8021DdcfmRrVlanPriority_Type()
)
ieee8021DdcfmRrVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrVlanPriority.setStatus("current")


class _Ieee8021DdcfmRrVlanDropEligible_Type(TruthValue):
    """Custom type ieee8021DdcfmRrVlanDropEligible based on TruthValue"""


_Ieee8021DdcfmRrVlanDropEligible_Object = MibTableColumn
ieee8021DdcfmRrVlanDropEligible = _Ieee8021DdcfmRrVlanDropEligible_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 12),
    _Ieee8021DdcfmRrVlanDropEligible_Type()
)
ieee8021DdcfmRrVlanDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrVlanDropEligible.setStatus("current")


class _Ieee8021DdcfmRrFloodingFlag_Type(TruthValue):
    """Custom type ieee8021DdcfmRrFloodingFlag based on TruthValue"""


_Ieee8021DdcfmRrFloodingFlag_Object = MibTableColumn
ieee8021DdcfmRrFloodingFlag = _Ieee8021DdcfmRrFloodingFlag_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 13),
    _Ieee8021DdcfmRrFloodingFlag_Type()
)
ieee8021DdcfmRrFloodingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrFloodingFlag.setStatus("current")


class _Ieee8021DdcfmRrTruncationFlag_Type(TruthValue):
    """Custom type ieee8021DdcfmRrTruncationFlag based on TruthValue"""


_Ieee8021DdcfmRrTruncationFlag_Object = MibTableColumn
ieee8021DdcfmRrTruncationFlag = _Ieee8021DdcfmRrTruncationFlag_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 14),
    _Ieee8021DdcfmRrTruncationFlag_Type()
)
ieee8021DdcfmRrTruncationFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrTruncationFlag.setStatus("current")


class _Ieee8021DdcfmRrActivationStatus_Type(TruthValue):
    """Custom type ieee8021DdcfmRrActivationStatus based on TruthValue"""


_Ieee8021DdcfmRrActivationStatus_Object = MibTableColumn
ieee8021DdcfmRrActivationStatus = _Ieee8021DdcfmRrActivationStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 15),
    _Ieee8021DdcfmRrActivationStatus_Type()
)
ieee8021DdcfmRrActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrActivationStatus.setStatus("current")
_Ieee8021DdcfmRrRemainDuration_Type = Unsigned32
_Ieee8021DdcfmRrRemainDuration_Object = MibTableColumn
ieee8021DdcfmRrRemainDuration = _Ieee8021DdcfmRrRemainDuration_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 16),
    _Ieee8021DdcfmRrRemainDuration_Type()
)
ieee8021DdcfmRrRemainDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrRemainDuration.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrRemainDuration.setUnits("seconds")
_Ieee8021DdcfmRrNextRfmTransID_Type = Unsigned32
_Ieee8021DdcfmRrNextRfmTransID_Object = MibTableColumn
ieee8021DdcfmRrNextRfmTransID = _Ieee8021DdcfmRrNextRfmTransID_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 17),
    _Ieee8021DdcfmRrNextRfmTransID_Type()
)
ieee8021DdcfmRrNextRfmTransID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrNextRfmTransID.setStatus("current")
_Ieee8021DdcfmRrRowStatus_Type = RowStatus
_Ieee8021DdcfmRrRowStatus_Object = MibTableColumn
ieee8021DdcfmRrRowStatus = _Ieee8021DdcfmRrRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 2, 1, 1, 18),
    _Ieee8021DdcfmRrRowStatus_Type()
)
ieee8021DdcfmRrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRrRowStatus.setStatus("current")
_Ieee8021DdcfmRFMReceiver_ObjectIdentity = ObjectIdentity
ieee8021DdcfmRFMReceiver = _Ieee8021DdcfmRFMReceiver_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 3)
)
_Ieee8021DdcfmRFMReceiverTable_Object = MibTable
ieee8021DdcfmRFMReceiverTable = _Ieee8021DdcfmRFMReceiverTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021DdcfmRFMReceiverTable.setStatus("current")
_Ieee8021DdcfmRFMReceiverEntry_Object = MibTableRow
ieee8021DdcfmRFMReceiverEntry = _Ieee8021DdcfmRFMReceiverEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1)
)
ieee8021DdcfmRFMReceiverEntry.setIndexNames(
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRfmReceiverIfIndex"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmRfmReceiverMdIndex"),
)
if mibBuilder.loadTexts:
    ieee8021DdcfmRFMReceiverEntry.setStatus("current")
_Ieee8021DdcfmRfmReceiverIfIndex_Type = InterfaceIndex
_Ieee8021DdcfmRfmReceiverIfIndex_Object = MibTableColumn
ieee8021DdcfmRfmReceiverIfIndex = _Ieee8021DdcfmRfmReceiverIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1, 1),
    _Ieee8021DdcfmRfmReceiverIfIndex_Type()
)
ieee8021DdcfmRfmReceiverIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmRfmReceiverIfIndex.setStatus("current")
_Ieee8021DdcfmRfmReceiverMdIndex_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmRfmReceiverMdIndex_Object = MibTableColumn
ieee8021DdcfmRfmReceiverMdIndex = _Ieee8021DdcfmRfmReceiverMdIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1, 2),
    _Ieee8021DdcfmRfmReceiverMdIndex_Type()
)
ieee8021DdcfmRfmReceiverMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmRfmReceiverMdIndex.setStatus("current")
_Ieee8021DdcfmRFMRowStatus_Type = RowStatus
_Ieee8021DdcfmRFMRowStatus_Object = MibTableColumn
ieee8021DdcfmRFMRowStatus = _Ieee8021DdcfmRFMRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 3, 1, 1, 3),
    _Ieee8021DdcfmRFMRowStatus_Type()
)
ieee8021DdcfmRFMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmRFMRowStatus.setStatus("current")
_Ieee8021DdcfmDr_ObjectIdentity = ObjectIdentity
ieee8021DdcfmDr = _Ieee8021DdcfmDr_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4)
)
_Ieee8021DdcfmDrTable_Object = MibTable
ieee8021DdcfmDrTable = _Ieee8021DdcfmDrTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021DdcfmDrTable.setStatus("current")
_Ieee8021DdcfmDrEntry_Object = MibTableRow
ieee8021DdcfmDrEntry = _Ieee8021DdcfmDrEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1)
)
ieee8021DdcfmDrEntry.setIndexNames(
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrIfIndex"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrMdIndex"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrVlanIdOrNone"),
)
if mibBuilder.loadTexts:
    ieee8021DdcfmDrEntry.setStatus("current")
_Ieee8021DdcfmDrIfIndex_Type = InterfaceIndex
_Ieee8021DdcfmDrIfIndex_Object = MibTableColumn
ieee8021DdcfmDrIfIndex = _Ieee8021DdcfmDrIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 1),
    _Ieee8021DdcfmDrIfIndex_Type()
)
ieee8021DdcfmDrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrIfIndex.setStatus("current")
_Ieee8021DdcfmDrMdIndex_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmDrMdIndex_Object = MibTableColumn
ieee8021DdcfmDrMdIndex = _Ieee8021DdcfmDrMdIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 2),
    _Ieee8021DdcfmDrMdIndex_Type()
)
ieee8021DdcfmDrMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrMdIndex.setStatus("current")
_Ieee8021DdcfmDrVlanIdOrNone_Type = VlanIdOrNone
_Ieee8021DdcfmDrVlanIdOrNone_Object = MibTableColumn
ieee8021DdcfmDrVlanIdOrNone = _Ieee8021DdcfmDrVlanIdOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 3),
    _Ieee8021DdcfmDrVlanIdOrNone_Type()
)
ieee8021DdcfmDrVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrVlanIdOrNone.setStatus("current")
_Ieee8021DdcfmDrSfmOriginator_Type = MacAddress
_Ieee8021DdcfmDrSfmOriginator_Object = MibTableColumn
ieee8021DdcfmDrSfmOriginator = _Ieee8021DdcfmDrSfmOriginator_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 4),
    _Ieee8021DdcfmDrSfmOriginator_Type()
)
ieee8021DdcfmDrSfmOriginator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrSfmOriginator.setStatus("current")


class _Ieee8021DdcfmDrSourceAddressStayFlag_Type(TruthValue):
    """Custom type ieee8021DdcfmDrSourceAddressStayFlag based on TruthValue"""


_Ieee8021DdcfmDrSourceAddressStayFlag_Object = MibTableColumn
ieee8021DdcfmDrSourceAddressStayFlag = _Ieee8021DdcfmDrSourceAddressStayFlag_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 5),
    _Ieee8021DdcfmDrSourceAddressStayFlag_Type()
)
ieee8021DdcfmDrSourceAddressStayFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrSourceAddressStayFlag.setStatus("current")


class _Ieee8021DdcfmDrFloodingFlag_Type(TruthValue):
    """Custom type ieee8021DdcfmDrFloodingFlag based on TruthValue"""


_Ieee8021DdcfmDrFloodingFlag_Object = MibTableColumn
ieee8021DdcfmDrFloodingFlag = _Ieee8021DdcfmDrFloodingFlag_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 6),
    _Ieee8021DdcfmDrFloodingFlag_Type()
)
ieee8021DdcfmDrFloodingFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrFloodingFlag.setStatus("current")
_Ieee8021DdcfmDrDuration_Type = Unsigned32
_Ieee8021DdcfmDrDuration_Object = MibTableColumn
ieee8021DdcfmDrDuration = _Ieee8021DdcfmDrDuration_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 7),
    _Ieee8021DdcfmDrDuration_Type()
)
ieee8021DdcfmDrDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrDuration.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrDuration.setUnits("seconds")


class _Ieee8021DdcfmDrActivationStatus_Type(TruthValue):
    """Custom type ieee8021DdcfmDrActivationStatus based on TruthValue"""


_Ieee8021DdcfmDrActivationStatus_Object = MibTableColumn
ieee8021DdcfmDrActivationStatus = _Ieee8021DdcfmDrActivationStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 8),
    _Ieee8021DdcfmDrActivationStatus_Type()
)
ieee8021DdcfmDrActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrActivationStatus.setStatus("current")
_Ieee8021DdcfmDrRemainDuration_Type = Unsigned32
_Ieee8021DdcfmDrRemainDuration_Object = MibTableColumn
ieee8021DdcfmDrRemainDuration = _Ieee8021DdcfmDrRemainDuration_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 9),
    _Ieee8021DdcfmDrRemainDuration_Type()
)
ieee8021DdcfmDrRemainDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrRemainDuration.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrRemainDuration.setUnits("seconds")
_Ieee8021DdcfmDrSFMsequenceErrors_Type = Unsigned32
_Ieee8021DdcfmDrSFMsequenceErrors_Object = MibTableColumn
ieee8021DdcfmDrSFMsequenceErrors = _Ieee8021DdcfmDrSFMsequenceErrors_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 10),
    _Ieee8021DdcfmDrSFMsequenceErrors_Type()
)
ieee8021DdcfmDrSFMsequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrSFMsequenceErrors.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrSFMsequenceErrors.setUnits("integer")
_Ieee8021DdcfmDrRowStatus_Type = RowStatus
_Ieee8021DdcfmDrRowStatus_Object = MibTableColumn
ieee8021DdcfmDrRowStatus = _Ieee8021DdcfmDrRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 4, 1, 1, 11),
    _Ieee8021DdcfmDrRowStatus_Type()
)
ieee8021DdcfmDrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmDrRowStatus.setStatus("current")
_Ieee8021DdcfmSFMOriginator_ObjectIdentity = ObjectIdentity
ieee8021DdcfmSFMOriginator = _Ieee8021DdcfmSFMOriginator_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5)
)
_Ieee8021DdcfmSoTable_Object = MibTable
ieee8021DdcfmSoTable = _Ieee8021DdcfmSoTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021DdcfmSoTable.setStatus("current")
_Ieee8021DdcfmSoEntry_Object = MibTableRow
ieee8021DdcfmSoEntry = _Ieee8021DdcfmSoEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1)
)
ieee8021DdcfmSoEntry.setIndexNames(
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSfmIfIndex"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoMdIndex"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoVlanIdOrNone"),
    (0, "IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoDirection"),
)
if mibBuilder.loadTexts:
    ieee8021DdcfmSoEntry.setStatus("current")
_Ieee8021DdcfmSfmIfIndex_Type = InterfaceIndex
_Ieee8021DdcfmSfmIfIndex_Object = MibTableColumn
ieee8021DdcfmSfmIfIndex = _Ieee8021DdcfmSfmIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 1),
    _Ieee8021DdcfmSfmIfIndex_Type()
)
ieee8021DdcfmSfmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmSfmIfIndex.setStatus("current")
_Ieee8021DdcfmSoMdIndex_Type = Dot1agCfmMDLevel
_Ieee8021DdcfmSoMdIndex_Object = MibTableColumn
ieee8021DdcfmSoMdIndex = _Ieee8021DdcfmSoMdIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 2),
    _Ieee8021DdcfmSoMdIndex_Type()
)
ieee8021DdcfmSoMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoMdIndex.setStatus("current")
_Ieee8021DdcfmSoVlanIdOrNone_Type = VlanIdOrNone
_Ieee8021DdcfmSoVlanIdOrNone_Object = MibTableColumn
ieee8021DdcfmSoVlanIdOrNone = _Ieee8021DdcfmSoVlanIdOrNone_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 3),
    _Ieee8021DdcfmSoVlanIdOrNone_Type()
)
ieee8021DdcfmSoVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoVlanIdOrNone.setStatus("current")
_Ieee8021DdcfmSoDirection_Type = Dot1agCfmMpDirection
_Ieee8021DdcfmSoDirection_Object = MibTableColumn
ieee8021DdcfmSoDirection = _Ieee8021DdcfmSoDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 4),
    _Ieee8021DdcfmSoDirection_Type()
)
ieee8021DdcfmSoDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoDirection.setStatus("current")
_Ieee8021DdcfmSoDrMacAddress_Type = MacAddress
_Ieee8021DdcfmSoDrMacAddress_Object = MibTableColumn
ieee8021DdcfmSoDrMacAddress = _Ieee8021DdcfmSoDrMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 5),
    _Ieee8021DdcfmSoDrMacAddress_Type()
)
ieee8021DdcfmSoDrMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoDrMacAddress.setStatus("current")
_Ieee8021DdcfmSoDuration_Type = Unsigned32
_Ieee8021DdcfmSoDuration_Object = MibTableColumn
ieee8021DdcfmSoDuration = _Ieee8021DdcfmSoDuration_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 6),
    _Ieee8021DdcfmSoDuration_Type()
)
ieee8021DdcfmSoDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoDuration.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoDuration.setUnits("seconds")


class _Ieee8021DdcfmSoActivationStatus_Type(TruthValue):
    """Custom type ieee8021DdcfmSoActivationStatus based on TruthValue"""


_Ieee8021DdcfmSoActivationStatus_Object = MibTableColumn
ieee8021DdcfmSoActivationStatus = _Ieee8021DdcfmSoActivationStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 7),
    _Ieee8021DdcfmSoActivationStatus_Type()
)
ieee8021DdcfmSoActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoActivationStatus.setStatus("current")
_Ieee8021DdcfmSoRemainDuration_Type = Unsigned32
_Ieee8021DdcfmSoRemainDuration_Object = MibTableColumn
ieee8021DdcfmSoRemainDuration = _Ieee8021DdcfmSoRemainDuration_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 8),
    _Ieee8021DdcfmSoRemainDuration_Type()
)
ieee8021DdcfmSoRemainDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoRemainDuration.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoRemainDuration.setUnits("seconds")
_Ieee8021DdcfmSoRowStatus_Type = RowStatus
_Ieee8021DdcfmSoRowStatus_Object = MibTableColumn
ieee8021DdcfmSoRowStatus = _Ieee8021DdcfmSoRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 11, 1, 5, 1, 1, 9),
    _Ieee8021DdcfmSoRowStatus_Type()
)
ieee8021DdcfmSoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021DdcfmSoRowStatus.setStatus("current")
_Ieee8021DdcfmConformance_ObjectIdentity = ObjectIdentity
ieee8021DdcfmConformance = _Ieee8021DdcfmConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 2)
)
_Ieee8021DdcfmCompliances_ObjectIdentity = ObjectIdentity
ieee8021DdcfmCompliances = _Ieee8021DdcfmCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 1)
)
_Ieee8021DdcfmGroups_ObjectIdentity = ObjectIdentity
ieee8021DdcfmGroups = _Ieee8021DdcfmGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 2)
)

# Managed Objects groups

ieee8021DdcfmStackGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 1)
)
ieee8021DdcfmStackGroup.setObjects(
      *(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackRrMdLevel"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackRrDirection"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackRFMreceiverMdLevel"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackDrMdLevel"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackDrVlanIdOrNone"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackSFMOriginatorMdLevel"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackSFMOriginatorVlanIdOrNone"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmStackSFMOriginatorDirection"))
)
if mibBuilder.loadTexts:
    ieee8021DdcfmStackGroup.setStatus("current")

ieee8021DdcfmRrGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 2)
)
ieee8021DdcfmRrGroup.setObjects(
      *(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrPrimaryVlanIdOrNone"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrFilter"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrSamplingInterval"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrTargetAddress"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrContinueFlag"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrDuration"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrDurationInTimeFlag"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrVlanPriority"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrVlanDropEligible"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrFloodingFlag"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrTruncationFlag"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrActivationStatus"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrRemainDuration"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrNextRfmTransID"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRrRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021DdcfmRrGroup.setStatus("current")

ieee8021DdcfmRFMReceiverGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 3)
)
ieee8021DdcfmRFMReceiverGroup.setObjects(
    ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmRFMRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021DdcfmRFMReceiverGroup.setStatus("current")

ieee8021DdcfmDrGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 4)
)
ieee8021DdcfmDrGroup.setObjects(
      *(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrSourceAddressStayFlag"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrSfmOriginator"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrFloodingFlag"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrDuration"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrActivationStatus"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrRemainDuration"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrSFMsequenceErrors"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmDrRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021DdcfmDrGroup.setStatus("current")

ieee8021DdcfmSoGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 2, 5)
)
ieee8021DdcfmSoGroup.setObjects(
      *(("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoDrMacAddress"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoDuration"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoActivationStatus"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoRemainDuration"),
        ("IEEE8021-DDCFM-MIB", "ieee8021DdcfmSoRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021DdcfmSoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021DdcfmCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021DdcfmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-DDCFM-MIB",
    **{"ieee8021DdcfmMIB": ieee8021DdcfmMIB,
       "ieee8021MIBObjects": ieee8021MIBObjects,
       "ieee8021DdcfmStack": ieee8021DdcfmStack,
       "ieee8021DdcfmStackTable": ieee8021DdcfmStackTable,
       "ieee8021DdcfmStackEntry": ieee8021DdcfmStackEntry,
       "ieee8021DdcfmStackIfIndex": ieee8021DdcfmStackIfIndex,
       "ieee8021DdcfmStackRrMdLevel": ieee8021DdcfmStackRrMdLevel,
       "ieee8021DdcfmStackRrDirection": ieee8021DdcfmStackRrDirection,
       "ieee8021DdcfmStackRFMreceiverMdLevel": ieee8021DdcfmStackRFMreceiverMdLevel,
       "ieee8021DdcfmStackDrMdLevel": ieee8021DdcfmStackDrMdLevel,
       "ieee8021DdcfmStackDrVlanIdOrNone": ieee8021DdcfmStackDrVlanIdOrNone,
       "ieee8021DdcfmStackSFMOriginatorMdLevel": ieee8021DdcfmStackSFMOriginatorMdLevel,
       "ieee8021DdcfmStackSFMOriginatorVlanIdOrNone": ieee8021DdcfmStackSFMOriginatorVlanIdOrNone,
       "ieee8021DdcfmStackSFMOriginatorDirection": ieee8021DdcfmStackSFMOriginatorDirection,
       "ieee8021DdcfmRr": ieee8021DdcfmRr,
       "ieee8021DdcfmRrTable": ieee8021DdcfmRrTable,
       "ieee8021DdcfmRrEntry": ieee8021DdcfmRrEntry,
       "ieee8021DdcfmRrIfIndex": ieee8021DdcfmRrIfIndex,
       "ieee8021DdcfmRrMdIndex": ieee8021DdcfmRrMdIndex,
       "ieee8021DdcfmRrDirection": ieee8021DdcfmRrDirection,
       "ieee8021DdcfmRrPrimaryVlanIdOrNone": ieee8021DdcfmRrPrimaryVlanIdOrNone,
       "ieee8021DdcfmRrFilter": ieee8021DdcfmRrFilter,
       "ieee8021DdcfmRrSamplingInterval": ieee8021DdcfmRrSamplingInterval,
       "ieee8021DdcfmRrTargetAddress": ieee8021DdcfmRrTargetAddress,
       "ieee8021DdcfmRrContinueFlag": ieee8021DdcfmRrContinueFlag,
       "ieee8021DdcfmRrDuration": ieee8021DdcfmRrDuration,
       "ieee8021DdcfmRrDurationInTimeFlag": ieee8021DdcfmRrDurationInTimeFlag,
       "ieee8021DdcfmRrVlanPriority": ieee8021DdcfmRrVlanPriority,
       "ieee8021DdcfmRrVlanDropEligible": ieee8021DdcfmRrVlanDropEligible,
       "ieee8021DdcfmRrFloodingFlag": ieee8021DdcfmRrFloodingFlag,
       "ieee8021DdcfmRrTruncationFlag": ieee8021DdcfmRrTruncationFlag,
       "ieee8021DdcfmRrActivationStatus": ieee8021DdcfmRrActivationStatus,
       "ieee8021DdcfmRrRemainDuration": ieee8021DdcfmRrRemainDuration,
       "ieee8021DdcfmRrNextRfmTransID": ieee8021DdcfmRrNextRfmTransID,
       "ieee8021DdcfmRrRowStatus": ieee8021DdcfmRrRowStatus,
       "ieee8021DdcfmRFMReceiver": ieee8021DdcfmRFMReceiver,
       "ieee8021DdcfmRFMReceiverTable": ieee8021DdcfmRFMReceiverTable,
       "ieee8021DdcfmRFMReceiverEntry": ieee8021DdcfmRFMReceiverEntry,
       "ieee8021DdcfmRfmReceiverIfIndex": ieee8021DdcfmRfmReceiverIfIndex,
       "ieee8021DdcfmRfmReceiverMdIndex": ieee8021DdcfmRfmReceiverMdIndex,
       "ieee8021DdcfmRFMRowStatus": ieee8021DdcfmRFMRowStatus,
       "ieee8021DdcfmDr": ieee8021DdcfmDr,
       "ieee8021DdcfmDrTable": ieee8021DdcfmDrTable,
       "ieee8021DdcfmDrEntry": ieee8021DdcfmDrEntry,
       "ieee8021DdcfmDrIfIndex": ieee8021DdcfmDrIfIndex,
       "ieee8021DdcfmDrMdIndex": ieee8021DdcfmDrMdIndex,
       "ieee8021DdcfmDrVlanIdOrNone": ieee8021DdcfmDrVlanIdOrNone,
       "ieee8021DdcfmDrSfmOriginator": ieee8021DdcfmDrSfmOriginator,
       "ieee8021DdcfmDrSourceAddressStayFlag": ieee8021DdcfmDrSourceAddressStayFlag,
       "ieee8021DdcfmDrFloodingFlag": ieee8021DdcfmDrFloodingFlag,
       "ieee8021DdcfmDrDuration": ieee8021DdcfmDrDuration,
       "ieee8021DdcfmDrActivationStatus": ieee8021DdcfmDrActivationStatus,
       "ieee8021DdcfmDrRemainDuration": ieee8021DdcfmDrRemainDuration,
       "ieee8021DdcfmDrSFMsequenceErrors": ieee8021DdcfmDrSFMsequenceErrors,
       "ieee8021DdcfmDrRowStatus": ieee8021DdcfmDrRowStatus,
       "ieee8021DdcfmSFMOriginator": ieee8021DdcfmSFMOriginator,
       "ieee8021DdcfmSoTable": ieee8021DdcfmSoTable,
       "ieee8021DdcfmSoEntry": ieee8021DdcfmSoEntry,
       "ieee8021DdcfmSfmIfIndex": ieee8021DdcfmSfmIfIndex,
       "ieee8021DdcfmSoMdIndex": ieee8021DdcfmSoMdIndex,
       "ieee8021DdcfmSoVlanIdOrNone": ieee8021DdcfmSoVlanIdOrNone,
       "ieee8021DdcfmSoDirection": ieee8021DdcfmSoDirection,
       "ieee8021DdcfmSoDrMacAddress": ieee8021DdcfmSoDrMacAddress,
       "ieee8021DdcfmSoDuration": ieee8021DdcfmSoDuration,
       "ieee8021DdcfmSoActivationStatus": ieee8021DdcfmSoActivationStatus,
       "ieee8021DdcfmSoRemainDuration": ieee8021DdcfmSoRemainDuration,
       "ieee8021DdcfmSoRowStatus": ieee8021DdcfmSoRowStatus,
       "ieee8021DdcfmConformance": ieee8021DdcfmConformance,
       "ieee8021DdcfmCompliances": ieee8021DdcfmCompliances,
       "ieee8021DdcfmCompliance": ieee8021DdcfmCompliance,
       "ieee8021DdcfmGroups": ieee8021DdcfmGroups,
       "ieee8021DdcfmStackGroup": ieee8021DdcfmStackGroup,
       "ieee8021DdcfmRrGroup": ieee8021DdcfmRrGroup,
       "ieee8021DdcfmRFMReceiverGroup": ieee8021DdcfmRFMReceiverGroup,
       "ieee8021DdcfmDrGroup": ieee8021DdcfmDrGroup,
       "ieee8021DdcfmSoGroup": ieee8021DdcfmSoGroup}
)
