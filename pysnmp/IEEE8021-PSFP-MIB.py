# SNMP MIB module (IEEE8021-PSFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-PSFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:35 2024
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

(ieee8021BridgeBaseComponentId,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId")

(IEEE8021STPTPtimeValue,) = mibBuilder.importSymbols(
    "IEEE8021-ST-MIB",
    "IEEE8021STPTPtimeValue")

(ieee802dot1mibs,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "ieee802dot1mibs")

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

ieee8021PSFPMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31)
)
ieee8021PSFPMib.setRevisions(
        ("2018-06-28 00:00",
         "2017-09-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021PSFPNotifications_ObjectIdentity = ObjectIdentity
ieee8021PSFPNotifications = _Ieee8021PSFPNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 0)
)
_Ieee8021PSFPObjects_ObjectIdentity = ObjectIdentity
ieee8021PSFPObjects = _Ieee8021PSFPObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 1)
)
_Ieee8021PSFPStreamFilterParameters_ObjectIdentity = ObjectIdentity
ieee8021PSFPStreamFilterParameters = _Ieee8021PSFPStreamFilterParameters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1)
)
_Ieee8021PSFPStreamFilterTable_Object = MibTable
ieee8021PSFPStreamFilterTable = _Ieee8021PSFPStreamFilterTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PSFPStreamFilterTable.setStatus("current")
_Ieee8021PSFPStreamFilterEntry_Object = MibTableRow
ieee8021PSFPStreamFilterEntry = _Ieee8021PSFPStreamFilterEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1)
)
ieee8021PSFPStreamFilterEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-PSFP-MIB", "ieee8021PSFPStreamFilterInstance"),
)
if mibBuilder.loadTexts:
    ieee8021PSFPStreamFilterEntry.setStatus("current")
_Ieee8021PSFPStreamFilterInstance_Type = Unsigned32
_Ieee8021PSFPStreamFilterInstance_Object = MibTableColumn
ieee8021PSFPStreamFilterInstance = _Ieee8021PSFPStreamFilterInstance_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 1),
    _Ieee8021PSFPStreamFilterInstance_Type()
)
ieee8021PSFPStreamFilterInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamFilterInstance.setStatus("current")


class _Ieee8021PSFPStreamHandleSpec_Type(Integer32):
    """Custom type ieee8021PSFPStreamHandleSpec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Ieee8021PSFPStreamHandleSpec_Type.__name__ = "Integer32"
_Ieee8021PSFPStreamHandleSpec_Object = MibTableColumn
ieee8021PSFPStreamHandleSpec = _Ieee8021PSFPStreamHandleSpec_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 2),
    _Ieee8021PSFPStreamHandleSpec_Type()
)
ieee8021PSFPStreamHandleSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamHandleSpec.setStatus("current")


class _Ieee8021PSFPPrioritySpec_Type(Integer32):
    """Custom type ieee8021PSFPPrioritySpec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Ieee8021PSFPPrioritySpec_Type.__name__ = "Integer32"
_Ieee8021PSFPPrioritySpec_Object = MibTableColumn
ieee8021PSFPPrioritySpec = _Ieee8021PSFPPrioritySpec_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 3),
    _Ieee8021PSFPPrioritySpec_Type()
)
ieee8021PSFPPrioritySpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPPrioritySpec.setStatus("current")
_Ieee8021PSFPStreamGateInstanceID_Type = Unsigned32
_Ieee8021PSFPStreamGateInstanceID_Object = MibTableColumn
ieee8021PSFPStreamGateInstanceID = _Ieee8021PSFPStreamGateInstanceID_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 4),
    _Ieee8021PSFPStreamGateInstanceID_Type()
)
ieee8021PSFPStreamGateInstanceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamGateInstanceID.setStatus("current")
_Ieee8021PSFPFilterSpecificationList_Type = OctetString
_Ieee8021PSFPFilterSpecificationList_Object = MibTableColumn
ieee8021PSFPFilterSpecificationList = _Ieee8021PSFPFilterSpecificationList_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 5),
    _Ieee8021PSFPFilterSpecificationList_Type()
)
ieee8021PSFPFilterSpecificationList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFilterSpecificationList.setStatus("current")
_Ieee8021PSFPMatchingFramesCount_Type = Counter64
_Ieee8021PSFPMatchingFramesCount_Object = MibTableColumn
ieee8021PSFPMatchingFramesCount = _Ieee8021PSFPMatchingFramesCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 6),
    _Ieee8021PSFPMatchingFramesCount_Type()
)
ieee8021PSFPMatchingFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPMatchingFramesCount.setStatus("current")
_Ieee8021PSFPPassingFramesCount_Type = Counter64
_Ieee8021PSFPPassingFramesCount_Object = MibTableColumn
ieee8021PSFPPassingFramesCount = _Ieee8021PSFPPassingFramesCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 7),
    _Ieee8021PSFPPassingFramesCount_Type()
)
ieee8021PSFPPassingFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPPassingFramesCount.setStatus("current")
_Ieee8021PSFPNotPassingFramesCount_Type = Counter64
_Ieee8021PSFPNotPassingFramesCount_Object = MibTableColumn
ieee8021PSFPNotPassingFramesCount = _Ieee8021PSFPNotPassingFramesCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 8),
    _Ieee8021PSFPNotPassingFramesCount_Type()
)
ieee8021PSFPNotPassingFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPNotPassingFramesCount.setStatus("current")
_Ieee8021PSFPPassingSDUCount_Type = Counter64
_Ieee8021PSFPPassingSDUCount_Object = MibTableColumn
ieee8021PSFPPassingSDUCount = _Ieee8021PSFPPassingSDUCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 9),
    _Ieee8021PSFPPassingSDUCount_Type()
)
ieee8021PSFPPassingSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPPassingSDUCount.setStatus("current")
_Ieee8021PSFPNotPassingSDUCount_Type = Counter64
_Ieee8021PSFPNotPassingSDUCount_Object = MibTableColumn
ieee8021PSFPNotPassingSDUCount = _Ieee8021PSFPNotPassingSDUCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 10),
    _Ieee8021PSFPNotPassingSDUCount_Type()
)
ieee8021PSFPNotPassingSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPNotPassingSDUCount.setStatus("current")
_Ieee8021PSFPREDFramesCount_Type = Counter64
_Ieee8021PSFPREDFramesCount_Object = MibTableColumn
ieee8021PSFPREDFramesCount = _Ieee8021PSFPREDFramesCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 11),
    _Ieee8021PSFPREDFramesCount_Type()
)
ieee8021PSFPREDFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPREDFramesCount.setStatus("current")


class _Ieee8021PSFPStreamBlockedDueToOversizeFrameEnable_Type(TruthValue):
    """Custom type ieee8021PSFPStreamBlockedDueToOversizeFrameEnable based on TruthValue"""


_Ieee8021PSFPStreamBlockedDueToOversizeFrameEnable_Object = MibTableColumn
ieee8021PSFPStreamBlockedDueToOversizeFrameEnable = _Ieee8021PSFPStreamBlockedDueToOversizeFrameEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 12),
    _Ieee8021PSFPStreamBlockedDueToOversizeFrameEnable_Type()
)
ieee8021PSFPStreamBlockedDueToOversizeFrameEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamBlockedDueToOversizeFrameEnable.setStatus("current")


class _Ieee8021PSFPStreamBlockedDueToOversizeFrame_Type(TruthValue):
    """Custom type ieee8021PSFPStreamBlockedDueToOversizeFrame based on TruthValue"""


_Ieee8021PSFPStreamBlockedDueToOversizeFrame_Object = MibTableColumn
ieee8021PSFPStreamBlockedDueToOversizeFrame = _Ieee8021PSFPStreamBlockedDueToOversizeFrame_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 13),
    _Ieee8021PSFPStreamBlockedDueToOversizeFrame_Type()
)
ieee8021PSFPStreamBlockedDueToOversizeFrame.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamBlockedDueToOversizeFrame.setStatus("current")
_Ieee8021PSFPStreamFilterEntryRowStatus_Type = RowStatus
_Ieee8021PSFPStreamFilterEntryRowStatus_Object = MibTableColumn
ieee8021PSFPStreamFilterEntryRowStatus = _Ieee8021PSFPStreamFilterEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 1, 1, 1, 14),
    _Ieee8021PSFPStreamFilterEntryRowStatus_Type()
)
ieee8021PSFPStreamFilterEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamFilterEntryRowStatus.setStatus("current")
_Ieee8021PSFPStreamGateParameters_ObjectIdentity = ObjectIdentity
ieee8021PSFPStreamGateParameters = _Ieee8021PSFPStreamGateParameters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2)
)
_Ieee8021PSFPStreamGateTable_Object = MibTable
ieee8021PSFPStreamGateTable = _Ieee8021PSFPStreamGateTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021PSFPStreamGateTable.setStatus("current")
_Ieee8021PSFPStreamGateEntry_Object = MibTableRow
ieee8021PSFPStreamGateEntry = _Ieee8021PSFPStreamGateEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1)
)
ieee8021PSFPStreamGateEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-PSFP-MIB", "ieee8021PSFPStreamGateInstance"),
)
if mibBuilder.loadTexts:
    ieee8021PSFPStreamGateEntry.setStatus("current")
_Ieee8021PSFPStreamGateInstance_Type = Unsigned32
_Ieee8021PSFPStreamGateInstance_Object = MibTableColumn
ieee8021PSFPStreamGateInstance = _Ieee8021PSFPStreamGateInstance_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 1),
    _Ieee8021PSFPStreamGateInstance_Type()
)
ieee8021PSFPStreamGateInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamGateInstance.setStatus("current")


class _Ieee8021PSFPGateEnabled_Type(TruthValue):
    """Custom type ieee8021PSFPGateEnabled based on TruthValue"""


_Ieee8021PSFPGateEnabled_Object = MibTableColumn
ieee8021PSFPGateEnabled = _Ieee8021PSFPGateEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 2),
    _Ieee8021PSFPGateEnabled_Type()
)
ieee8021PSFPGateEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPGateEnabled.setStatus("current")


class _Ieee8021PSFPAdminGateStates_Type(Integer32):
    """Custom type ieee8021PSFPAdminGateStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_Ieee8021PSFPAdminGateStates_Type.__name__ = "Integer32"
_Ieee8021PSFPAdminGateStates_Object = MibTableColumn
ieee8021PSFPAdminGateStates = _Ieee8021PSFPAdminGateStates_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 3),
    _Ieee8021PSFPAdminGateStates_Type()
)
ieee8021PSFPAdminGateStates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminGateStates.setStatus("current")


class _Ieee8021PSFPOperGateStates_Type(Integer32):
    """Custom type ieee8021PSFPOperGateStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_Ieee8021PSFPOperGateStates_Type.__name__ = "Integer32"
_Ieee8021PSFPOperGateStates_Object = MibTableColumn
ieee8021PSFPOperGateStates = _Ieee8021PSFPOperGateStates_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 4),
    _Ieee8021PSFPOperGateStates_Type()
)
ieee8021PSFPOperGateStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPOperGateStates.setStatus("current")
_Ieee8021PSFPAdminControlListLength_Type = Unsigned32
_Ieee8021PSFPAdminControlListLength_Object = MibTableColumn
ieee8021PSFPAdminControlListLength = _Ieee8021PSFPAdminControlListLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 5),
    _Ieee8021PSFPAdminControlListLength_Type()
)
ieee8021PSFPAdminControlListLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminControlListLength.setStatus("current")
_Ieee8021PSFPOperControlListLength_Type = Unsigned32
_Ieee8021PSFPOperControlListLength_Object = MibTableColumn
ieee8021PSFPOperControlListLength = _Ieee8021PSFPOperControlListLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 6),
    _Ieee8021PSFPOperControlListLength_Type()
)
ieee8021PSFPOperControlListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPOperControlListLength.setStatus("current")
_Ieee8021PSFPAdminControlList_Type = OctetString
_Ieee8021PSFPAdminControlList_Object = MibTableColumn
ieee8021PSFPAdminControlList = _Ieee8021PSFPAdminControlList_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 7),
    _Ieee8021PSFPAdminControlList_Type()
)
ieee8021PSFPAdminControlList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminControlList.setStatus("current")
_Ieee8021PSFPOperControlList_Type = OctetString
_Ieee8021PSFPOperControlList_Object = MibTableColumn
ieee8021PSFPOperControlList = _Ieee8021PSFPOperControlList_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 8),
    _Ieee8021PSFPOperControlList_Type()
)
ieee8021PSFPOperControlList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPOperControlList.setStatus("current")
_Ieee8021PSFPAdminCycleTimeNumerator_Type = Unsigned32
_Ieee8021PSFPAdminCycleTimeNumerator_Object = MibTableColumn
ieee8021PSFPAdminCycleTimeNumerator = _Ieee8021PSFPAdminCycleTimeNumerator_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 9),
    _Ieee8021PSFPAdminCycleTimeNumerator_Type()
)
ieee8021PSFPAdminCycleTimeNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminCycleTimeNumerator.setStatus("current")
_Ieee8021PSFPAdminCycleTimeDenominator_Type = Unsigned32
_Ieee8021PSFPAdminCycleTimeDenominator_Object = MibTableColumn
ieee8021PSFPAdminCycleTimeDenominator = _Ieee8021PSFPAdminCycleTimeDenominator_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 10),
    _Ieee8021PSFPAdminCycleTimeDenominator_Type()
)
ieee8021PSFPAdminCycleTimeDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminCycleTimeDenominator.setStatus("current")
_Ieee8021PSFPOperCycleTimeNumerator_Type = Unsigned32
_Ieee8021PSFPOperCycleTimeNumerator_Object = MibTableColumn
ieee8021PSFPOperCycleTimeNumerator = _Ieee8021PSFPOperCycleTimeNumerator_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 11),
    _Ieee8021PSFPOperCycleTimeNumerator_Type()
)
ieee8021PSFPOperCycleTimeNumerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPOperCycleTimeNumerator.setStatus("current")
_Ieee8021PSFPOperCycleTimeDenominator_Type = Unsigned32
_Ieee8021PSFPOperCycleTimeDenominator_Object = MibTableColumn
ieee8021PSFPOperCycleTimeDenominator = _Ieee8021PSFPOperCycleTimeDenominator_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 12),
    _Ieee8021PSFPOperCycleTimeDenominator_Type()
)
ieee8021PSFPOperCycleTimeDenominator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPOperCycleTimeDenominator.setStatus("current")
_Ieee8021PSFPAdminCycleTimeExtension_Type = Unsigned32
_Ieee8021PSFPAdminCycleTimeExtension_Object = MibTableColumn
ieee8021PSFPAdminCycleTimeExtension = _Ieee8021PSFPAdminCycleTimeExtension_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 13),
    _Ieee8021PSFPAdminCycleTimeExtension_Type()
)
ieee8021PSFPAdminCycleTimeExtension.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminCycleTimeExtension.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminCycleTimeExtension.setUnits("nanoseconds")
_Ieee8021PSFPOperCycleTimeExtension_Type = Unsigned32
_Ieee8021PSFPOperCycleTimeExtension_Object = MibTableColumn
ieee8021PSFPOperCycleTimeExtension = _Ieee8021PSFPOperCycleTimeExtension_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 14),
    _Ieee8021PSFPOperCycleTimeExtension_Type()
)
ieee8021PSFPOperCycleTimeExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPOperCycleTimeExtension.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021PSFPOperCycleTimeExtension.setUnits("nanoseconds")
_Ieee8021PSFPAdminBaseTime_Type = IEEE8021STPTPtimeValue
_Ieee8021PSFPAdminBaseTime_Object = MibTableColumn
ieee8021PSFPAdminBaseTime = _Ieee8021PSFPAdminBaseTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 15),
    _Ieee8021PSFPAdminBaseTime_Type()
)
ieee8021PSFPAdminBaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminBaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminBaseTime.setUnits("PTP time")
_Ieee8021PSFPOperBaseTime_Type = IEEE8021STPTPtimeValue
_Ieee8021PSFPOperBaseTime_Object = MibTableColumn
ieee8021PSFPOperBaseTime = _Ieee8021PSFPOperBaseTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 16),
    _Ieee8021PSFPOperBaseTime_Type()
)
ieee8021PSFPOperBaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPOperBaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021PSFPOperBaseTime.setUnits("PTP time")
_Ieee8021PSFPConfigChange_Type = TruthValue
_Ieee8021PSFPConfigChange_Object = MibTableColumn
ieee8021PSFPConfigChange = _Ieee8021PSFPConfigChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 17),
    _Ieee8021PSFPConfigChange_Type()
)
ieee8021PSFPConfigChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPConfigChange.setStatus("current")
_Ieee8021PSFPConfigChangeTime_Type = IEEE8021STPTPtimeValue
_Ieee8021PSFPConfigChangeTime_Object = MibTableColumn
ieee8021PSFPConfigChangeTime = _Ieee8021PSFPConfigChangeTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 18),
    _Ieee8021PSFPConfigChangeTime_Type()
)
ieee8021PSFPConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPConfigChangeTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021PSFPConfigChangeTime.setUnits("PTP time")
_Ieee8021PSFPTickGranularity_Type = Unsigned32
_Ieee8021PSFPTickGranularity_Object = MibTableColumn
ieee8021PSFPTickGranularity = _Ieee8021PSFPTickGranularity_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 19),
    _Ieee8021PSFPTickGranularity_Type()
)
ieee8021PSFPTickGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPTickGranularity.setStatus("current")
_Ieee8021PSFPCurrentTime_Type = IEEE8021STPTPtimeValue
_Ieee8021PSFPCurrentTime_Object = MibTableColumn
ieee8021PSFPCurrentTime = _Ieee8021PSFPCurrentTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 20),
    _Ieee8021PSFPCurrentTime_Type()
)
ieee8021PSFPCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPCurrentTime.setStatus("current")
_Ieee8021PSFPConfigPending_Type = TruthValue
_Ieee8021PSFPConfigPending_Object = MibTableColumn
ieee8021PSFPConfigPending = _Ieee8021PSFPConfigPending_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 21),
    _Ieee8021PSFPConfigPending_Type()
)
ieee8021PSFPConfigPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPConfigPending.setStatus("current")
_Ieee8021PSFPConfigChangeError_Type = Counter64
_Ieee8021PSFPConfigChangeError_Object = MibTableColumn
ieee8021PSFPConfigChangeError = _Ieee8021PSFPConfigChangeError_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 23),
    _Ieee8021PSFPConfigChangeError_Type()
)
ieee8021PSFPConfigChangeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPConfigChangeError.setStatus("current")


class _Ieee8021PSFPAdminIPV_Type(Integer32):
    """Custom type ieee8021PSFPAdminIPV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Ieee8021PSFPAdminIPV_Type.__name__ = "Integer32"
_Ieee8021PSFPAdminIPV_Object = MibTableColumn
ieee8021PSFPAdminIPV = _Ieee8021PSFPAdminIPV_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 24),
    _Ieee8021PSFPAdminIPV_Type()
)
ieee8021PSFPAdminIPV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPAdminIPV.setStatus("current")


class _Ieee8021PSFPOperIPV_Type(Integer32):
    """Custom type ieee8021PSFPOperIPV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Ieee8021PSFPOperIPV_Type.__name__ = "Integer32"
_Ieee8021PSFPOperIPV_Object = MibTableColumn
ieee8021PSFPOperIPV = _Ieee8021PSFPOperIPV_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 25),
    _Ieee8021PSFPOperIPV_Type()
)
ieee8021PSFPOperIPV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPOperIPV.setStatus("current")


class _Ieee8021PSFPGateClosedDueToInvalidRxEnable_Type(TruthValue):
    """Custom type ieee8021PSFPGateClosedDueToInvalidRxEnable based on TruthValue"""


_Ieee8021PSFPGateClosedDueToInvalidRxEnable_Object = MibTableColumn
ieee8021PSFPGateClosedDueToInvalidRxEnable = _Ieee8021PSFPGateClosedDueToInvalidRxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 26),
    _Ieee8021PSFPGateClosedDueToInvalidRxEnable_Type()
)
ieee8021PSFPGateClosedDueToInvalidRxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPGateClosedDueToInvalidRxEnable.setStatus("current")


class _Ieee8021PSFPGateClosedDueToInvalidRx_Type(TruthValue):
    """Custom type ieee8021PSFPGateClosedDueToInvalidRx based on TruthValue"""


_Ieee8021PSFPGateClosedDueToInvalidRx_Object = MibTableColumn
ieee8021PSFPGateClosedDueToInvalidRx = _Ieee8021PSFPGateClosedDueToInvalidRx_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 27),
    _Ieee8021PSFPGateClosedDueToInvalidRx_Type()
)
ieee8021PSFPGateClosedDueToInvalidRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPGateClosedDueToInvalidRx.setStatus("current")


class _Ieee8021PSFPGateClosedDueToOctetsExceededEnable_Type(TruthValue):
    """Custom type ieee8021PSFPGateClosedDueToOctetsExceededEnable based on TruthValue"""


_Ieee8021PSFPGateClosedDueToOctetsExceededEnable_Object = MibTableColumn
ieee8021PSFPGateClosedDueToOctetsExceededEnable = _Ieee8021PSFPGateClosedDueToOctetsExceededEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 28),
    _Ieee8021PSFPGateClosedDueToOctetsExceededEnable_Type()
)
ieee8021PSFPGateClosedDueToOctetsExceededEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPGateClosedDueToOctetsExceededEnable.setStatus("current")


class _Ieee8021PSFPGateClosedDueToOctetsExceeded_Type(TruthValue):
    """Custom type ieee8021PSFPGateClosedDueToOctetsExceeded based on TruthValue"""


_Ieee8021PSFPGateClosedDueToOctetsExceeded_Object = MibTableColumn
ieee8021PSFPGateClosedDueToOctetsExceeded = _Ieee8021PSFPGateClosedDueToOctetsExceeded_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 29),
    _Ieee8021PSFPGateClosedDueToOctetsExceeded_Type()
)
ieee8021PSFPGateClosedDueToOctetsExceeded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPGateClosedDueToOctetsExceeded.setStatus("current")
_Ieee8021PSFPStreamGateEntryRowStatus_Type = RowStatus
_Ieee8021PSFPStreamGateEntryRowStatus_Object = MibTableColumn
ieee8021PSFPStreamGateEntryRowStatus = _Ieee8021PSFPStreamGateEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 2, 1, 1, 30),
    _Ieee8021PSFPStreamGateEntryRowStatus_Type()
)
ieee8021PSFPStreamGateEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPStreamGateEntryRowStatus.setStatus("current")
_Ieee8021PSFPFlowMeterParameters_ObjectIdentity = ObjectIdentity
ieee8021PSFPFlowMeterParameters = _Ieee8021PSFPFlowMeterParameters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3)
)
_Ieee8021PSFPFlowMeterTable_Object = MibTable
ieee8021PSFPFlowMeterTable = _Ieee8021PSFPFlowMeterTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterTable.setStatus("current")
_Ieee8021PSFPFlowMeterEntry_Object = MibTableRow
ieee8021PSFPFlowMeterEntry = _Ieee8021PSFPFlowMeterEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1)
)
ieee8021PSFPFlowMeterEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterInstance"),
)
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterEntry.setStatus("current")
_Ieee8021PSFPFlowMeterInstance_Type = Unsigned32
_Ieee8021PSFPFlowMeterInstance_Object = MibTableColumn
ieee8021PSFPFlowMeterInstance = _Ieee8021PSFPFlowMeterInstance_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 1),
    _Ieee8021PSFPFlowMeterInstance_Type()
)
ieee8021PSFPFlowMeterInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterInstance.setStatus("current")
_Ieee8021PSFPFlowMeterCIR_Type = Unsigned32
_Ieee8021PSFPFlowMeterCIR_Object = MibTableColumn
ieee8021PSFPFlowMeterCIR = _Ieee8021PSFPFlowMeterCIR_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 2),
    _Ieee8021PSFPFlowMeterCIR_Type()
)
ieee8021PSFPFlowMeterCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterCIR.setStatus("current")
_Ieee8021PSFPFlowMeterCBS_Type = Unsigned32
_Ieee8021PSFPFlowMeterCBS_Object = MibTableColumn
ieee8021PSFPFlowMeterCBS = _Ieee8021PSFPFlowMeterCBS_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 3),
    _Ieee8021PSFPFlowMeterCBS_Type()
)
ieee8021PSFPFlowMeterCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterCBS.setStatus("current")
_Ieee8021PSFPFlowMeterEIR_Type = Unsigned32
_Ieee8021PSFPFlowMeterEIR_Object = MibTableColumn
ieee8021PSFPFlowMeterEIR = _Ieee8021PSFPFlowMeterEIR_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 4),
    _Ieee8021PSFPFlowMeterEIR_Type()
)
ieee8021PSFPFlowMeterEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterEIR.setStatus("current")
_Ieee8021PSFPFlowMeterEBS_Type = Unsigned32
_Ieee8021PSFPFlowMeterEBS_Object = MibTableColumn
ieee8021PSFPFlowMeterEBS = _Ieee8021PSFPFlowMeterEBS_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 5),
    _Ieee8021PSFPFlowMeterEBS_Type()
)
ieee8021PSFPFlowMeterEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterEBS.setStatus("current")


class _Ieee8021PSFPFlowMeterCF_Type(Integer32):
    """Custom type ieee8021PSFPFlowMeterCF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ieee8021PSFPFlowMeterCF_Type.__name__ = "Integer32"
_Ieee8021PSFPFlowMeterCF_Object = MibTableColumn
ieee8021PSFPFlowMeterCF = _Ieee8021PSFPFlowMeterCF_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 6),
    _Ieee8021PSFPFlowMeterCF_Type()
)
ieee8021PSFPFlowMeterCF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterCF.setStatus("current")


class _Ieee8021PSFPFlowMeterCM_Type(Integer32):
    """Custom type ieee8021PSFPFlowMeterCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 2),
          ("colorBlind", 1))
    )


_Ieee8021PSFPFlowMeterCM_Type.__name__ = "Integer32"
_Ieee8021PSFPFlowMeterCM_Object = MibTableColumn
ieee8021PSFPFlowMeterCM = _Ieee8021PSFPFlowMeterCM_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 7),
    _Ieee8021PSFPFlowMeterCM_Type()
)
ieee8021PSFPFlowMeterCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterCM.setStatus("current")
_Ieee8021PSFPFlowMeterDropOnYellow_Type = TruthValue
_Ieee8021PSFPFlowMeterDropOnYellow_Object = MibTableColumn
ieee8021PSFPFlowMeterDropOnYellow = _Ieee8021PSFPFlowMeterDropOnYellow_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 8),
    _Ieee8021PSFPFlowMeterDropOnYellow_Type()
)
ieee8021PSFPFlowMeterDropOnYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterDropOnYellow.setStatus("current")


class _Ieee8021PSFPFlowMeterMarkAllFramesRedEnable_Type(TruthValue):
    """Custom type ieee8021PSFPFlowMeterMarkAllFramesRedEnable based on TruthValue"""


_Ieee8021PSFPFlowMeterMarkAllFramesRedEnable_Object = MibTableColumn
ieee8021PSFPFlowMeterMarkAllFramesRedEnable = _Ieee8021PSFPFlowMeterMarkAllFramesRedEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 9),
    _Ieee8021PSFPFlowMeterMarkAllFramesRedEnable_Type()
)
ieee8021PSFPFlowMeterMarkAllFramesRedEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterMarkAllFramesRedEnable.setStatus("current")


class _Ieee8021PSFPFlowMeterMarkAllFramesRed_Type(TruthValue):
    """Custom type ieee8021PSFPFlowMeterMarkAllFramesRed based on TruthValue"""


_Ieee8021PSFPFlowMeterMarkAllFramesRed_Object = MibTableColumn
ieee8021PSFPFlowMeterMarkAllFramesRed = _Ieee8021PSFPFlowMeterMarkAllFramesRed_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 10),
    _Ieee8021PSFPFlowMeterMarkAllFramesRed_Type()
)
ieee8021PSFPFlowMeterMarkAllFramesRed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterMarkAllFramesRed.setStatus("current")
_Ieee8021PSFPFlowMeterEntryRowStatus_Type = RowStatus
_Ieee8021PSFPFlowMeterEntryRowStatus_Object = MibTableColumn
ieee8021PSFPFlowMeterEntryRowStatus = _Ieee8021PSFPFlowMeterEntryRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 3, 1, 1, 11),
    _Ieee8021PSFPFlowMeterEntryRowStatus_Type()
)
ieee8021PSFPFlowMeterEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PSFPFlowMeterEntryRowStatus.setStatus("current")
_Ieee8021PSFPStreamParameters_ObjectIdentity = ObjectIdentity
ieee8021PSFPStreamParameters = _Ieee8021PSFPStreamParameters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 4)
)
_Ieee8021PSFPStreamParameterTable_Object = MibTable
ieee8021PSFPStreamParameterTable = _Ieee8021PSFPStreamParameterTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021PSFPStreamParameterTable.setStatus("current")
_Ieee8021PSFPStreamParameterEntry_Object = MibTableRow
ieee8021PSFPStreamParameterEntry = _Ieee8021PSFPStreamParameterEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1)
)
ieee8021PSFPStreamParameterEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021PSFPStreamParameterEntry.setStatus("current")
_Ieee8021PSFPMaxStreamFilterInstances_Type = Unsigned32
_Ieee8021PSFPMaxStreamFilterInstances_Object = MibTableColumn
ieee8021PSFPMaxStreamFilterInstances = _Ieee8021PSFPMaxStreamFilterInstances_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 1),
    _Ieee8021PSFPMaxStreamFilterInstances_Type()
)
ieee8021PSFPMaxStreamFilterInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPMaxStreamFilterInstances.setStatus("current")
_Ieee8021PSFPMaxStreamGateInstances_Type = Unsigned32
_Ieee8021PSFPMaxStreamGateInstances_Object = MibTableColumn
ieee8021PSFPMaxStreamGateInstances = _Ieee8021PSFPMaxStreamGateInstances_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 2),
    _Ieee8021PSFPMaxStreamGateInstances_Type()
)
ieee8021PSFPMaxStreamGateInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPMaxStreamGateInstances.setStatus("current")
_Ieee8021PSFPMaxFlowMeterInstances_Type = Unsigned32
_Ieee8021PSFPMaxFlowMeterInstances_Object = MibTableColumn
ieee8021PSFPMaxFlowMeterInstances = _Ieee8021PSFPMaxFlowMeterInstances_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 3),
    _Ieee8021PSFPMaxFlowMeterInstances_Type()
)
ieee8021PSFPMaxFlowMeterInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPMaxFlowMeterInstances.setStatus("current")
_Ieee8021PSFPSupportedListMax_Type = Unsigned32
_Ieee8021PSFPSupportedListMax_Object = MibTableColumn
ieee8021PSFPSupportedListMax = _Ieee8021PSFPSupportedListMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 31, 1, 4, 1, 1, 4),
    _Ieee8021PSFPSupportedListMax_Type()
)
ieee8021PSFPSupportedListMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PSFPSupportedListMax.setStatus("current")
_Ieee8021PSFPConformance_ObjectIdentity = ObjectIdentity
ieee8021PSFPConformance = _Ieee8021PSFPConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 2)
)
_Ieee8021PSFPCompliances_ObjectIdentity = ObjectIdentity
ieee8021PSFPCompliances = _Ieee8021PSFPCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 2, 1)
)
_Ieee8021PSFPGroups_ObjectIdentity = ObjectIdentity
ieee8021PSFPGroups = _Ieee8021PSFPGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 31, 2, 2)
)

# Managed Objects groups

ieee8021PSFPObjectsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 31, 2, 2, 1)
)
ieee8021PSFPObjectsGroup.setObjects(
      *(("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamHandleSpec"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPPrioritySpec"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamGateInstanceID"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFilterSpecificationList"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPMatchingFramesCount"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPPassingFramesCount"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPNotPassingFramesCount"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPPassingSDUCount"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPNotPassingSDUCount"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPREDFramesCount"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamBlockedDueToOversizeFrameEnable"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamBlockedDueToOversizeFrame"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamFilterEntryRowStatus"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateEnabled"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminGateStates"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperGateStates"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminControlListLength"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperControlListLength"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminControlList"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperControlList"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminCycleTimeNumerator"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminCycleTimeDenominator"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperCycleTimeNumerator"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperCycleTimeDenominator"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminCycleTimeExtension"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperCycleTimeExtension"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminBaseTime"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperBaseTime"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigChange"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigChangeTime"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPTickGranularity"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPCurrentTime"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigPending"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPConfigChangeError"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPAdminIPV"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPOperIPV"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToInvalidRxEnable"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToInvalidRx"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToOctetsExceededEnable"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPGateClosedDueToOctetsExceeded"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPStreamGateEntryRowStatus"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCIR"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCBS"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterEIR"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterEBS"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCF"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterCM"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterDropOnYellow"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterMarkAllFramesRedEnable"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterMarkAllFramesRed"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPFlowMeterEntryRowStatus"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPMaxStreamFilterInstances"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPMaxStreamGateInstances"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPMaxFlowMeterInstances"),
        ("IEEE8021-PSFP-MIB", "ieee8021PSFPSupportedListMax"))
)
if mibBuilder.loadTexts:
    ieee8021PSFPObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021PSFPCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 31, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PSFPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PSFP-MIB",
    **{"ieee8021PSFPMib": ieee8021PSFPMib,
       "ieee8021PSFPNotifications": ieee8021PSFPNotifications,
       "ieee8021PSFPObjects": ieee8021PSFPObjects,
       "ieee8021PSFPStreamFilterParameters": ieee8021PSFPStreamFilterParameters,
       "ieee8021PSFPStreamFilterTable": ieee8021PSFPStreamFilterTable,
       "ieee8021PSFPStreamFilterEntry": ieee8021PSFPStreamFilterEntry,
       "ieee8021PSFPStreamFilterInstance": ieee8021PSFPStreamFilterInstance,
       "ieee8021PSFPStreamHandleSpec": ieee8021PSFPStreamHandleSpec,
       "ieee8021PSFPPrioritySpec": ieee8021PSFPPrioritySpec,
       "ieee8021PSFPStreamGateInstanceID": ieee8021PSFPStreamGateInstanceID,
       "ieee8021PSFPFilterSpecificationList": ieee8021PSFPFilterSpecificationList,
       "ieee8021PSFPMatchingFramesCount": ieee8021PSFPMatchingFramesCount,
       "ieee8021PSFPPassingFramesCount": ieee8021PSFPPassingFramesCount,
       "ieee8021PSFPNotPassingFramesCount": ieee8021PSFPNotPassingFramesCount,
       "ieee8021PSFPPassingSDUCount": ieee8021PSFPPassingSDUCount,
       "ieee8021PSFPNotPassingSDUCount": ieee8021PSFPNotPassingSDUCount,
       "ieee8021PSFPREDFramesCount": ieee8021PSFPREDFramesCount,
       "ieee8021PSFPStreamBlockedDueToOversizeFrameEnable": ieee8021PSFPStreamBlockedDueToOversizeFrameEnable,
       "ieee8021PSFPStreamBlockedDueToOversizeFrame": ieee8021PSFPStreamBlockedDueToOversizeFrame,
       "ieee8021PSFPStreamFilterEntryRowStatus": ieee8021PSFPStreamFilterEntryRowStatus,
       "ieee8021PSFPStreamGateParameters": ieee8021PSFPStreamGateParameters,
       "ieee8021PSFPStreamGateTable": ieee8021PSFPStreamGateTable,
       "ieee8021PSFPStreamGateEntry": ieee8021PSFPStreamGateEntry,
       "ieee8021PSFPStreamGateInstance": ieee8021PSFPStreamGateInstance,
       "ieee8021PSFPGateEnabled": ieee8021PSFPGateEnabled,
       "ieee8021PSFPAdminGateStates": ieee8021PSFPAdminGateStates,
       "ieee8021PSFPOperGateStates": ieee8021PSFPOperGateStates,
       "ieee8021PSFPAdminControlListLength": ieee8021PSFPAdminControlListLength,
       "ieee8021PSFPOperControlListLength": ieee8021PSFPOperControlListLength,
       "ieee8021PSFPAdminControlList": ieee8021PSFPAdminControlList,
       "ieee8021PSFPOperControlList": ieee8021PSFPOperControlList,
       "ieee8021PSFPAdminCycleTimeNumerator": ieee8021PSFPAdminCycleTimeNumerator,
       "ieee8021PSFPAdminCycleTimeDenominator": ieee8021PSFPAdminCycleTimeDenominator,
       "ieee8021PSFPOperCycleTimeNumerator": ieee8021PSFPOperCycleTimeNumerator,
       "ieee8021PSFPOperCycleTimeDenominator": ieee8021PSFPOperCycleTimeDenominator,
       "ieee8021PSFPAdminCycleTimeExtension": ieee8021PSFPAdminCycleTimeExtension,
       "ieee8021PSFPOperCycleTimeExtension": ieee8021PSFPOperCycleTimeExtension,
       "ieee8021PSFPAdminBaseTime": ieee8021PSFPAdminBaseTime,
       "ieee8021PSFPOperBaseTime": ieee8021PSFPOperBaseTime,
       "ieee8021PSFPConfigChange": ieee8021PSFPConfigChange,
       "ieee8021PSFPConfigChangeTime": ieee8021PSFPConfigChangeTime,
       "ieee8021PSFPTickGranularity": ieee8021PSFPTickGranularity,
       "ieee8021PSFPCurrentTime": ieee8021PSFPCurrentTime,
       "ieee8021PSFPConfigPending": ieee8021PSFPConfigPending,
       "ieee8021PSFPConfigChangeError": ieee8021PSFPConfigChangeError,
       "ieee8021PSFPAdminIPV": ieee8021PSFPAdminIPV,
       "ieee8021PSFPOperIPV": ieee8021PSFPOperIPV,
       "ieee8021PSFPGateClosedDueToInvalidRxEnable": ieee8021PSFPGateClosedDueToInvalidRxEnable,
       "ieee8021PSFPGateClosedDueToInvalidRx": ieee8021PSFPGateClosedDueToInvalidRx,
       "ieee8021PSFPGateClosedDueToOctetsExceededEnable": ieee8021PSFPGateClosedDueToOctetsExceededEnable,
       "ieee8021PSFPGateClosedDueToOctetsExceeded": ieee8021PSFPGateClosedDueToOctetsExceeded,
       "ieee8021PSFPStreamGateEntryRowStatus": ieee8021PSFPStreamGateEntryRowStatus,
       "ieee8021PSFPFlowMeterParameters": ieee8021PSFPFlowMeterParameters,
       "ieee8021PSFPFlowMeterTable": ieee8021PSFPFlowMeterTable,
       "ieee8021PSFPFlowMeterEntry": ieee8021PSFPFlowMeterEntry,
       "ieee8021PSFPFlowMeterInstance": ieee8021PSFPFlowMeterInstance,
       "ieee8021PSFPFlowMeterCIR": ieee8021PSFPFlowMeterCIR,
       "ieee8021PSFPFlowMeterCBS": ieee8021PSFPFlowMeterCBS,
       "ieee8021PSFPFlowMeterEIR": ieee8021PSFPFlowMeterEIR,
       "ieee8021PSFPFlowMeterEBS": ieee8021PSFPFlowMeterEBS,
       "ieee8021PSFPFlowMeterCF": ieee8021PSFPFlowMeterCF,
       "ieee8021PSFPFlowMeterCM": ieee8021PSFPFlowMeterCM,
       "ieee8021PSFPFlowMeterDropOnYellow": ieee8021PSFPFlowMeterDropOnYellow,
       "ieee8021PSFPFlowMeterMarkAllFramesRedEnable": ieee8021PSFPFlowMeterMarkAllFramesRedEnable,
       "ieee8021PSFPFlowMeterMarkAllFramesRed": ieee8021PSFPFlowMeterMarkAllFramesRed,
       "ieee8021PSFPFlowMeterEntryRowStatus": ieee8021PSFPFlowMeterEntryRowStatus,
       "ieee8021PSFPStreamParameters": ieee8021PSFPStreamParameters,
       "ieee8021PSFPStreamParameterTable": ieee8021PSFPStreamParameterTable,
       "ieee8021PSFPStreamParameterEntry": ieee8021PSFPStreamParameterEntry,
       "ieee8021PSFPMaxStreamFilterInstances": ieee8021PSFPMaxStreamFilterInstances,
       "ieee8021PSFPMaxStreamGateInstances": ieee8021PSFPMaxStreamGateInstances,
       "ieee8021PSFPMaxFlowMeterInstances": ieee8021PSFPMaxFlowMeterInstances,
       "ieee8021PSFPSupportedListMax": ieee8021PSFPSupportedListMax,
       "ieee8021PSFPConformance": ieee8021PSFPConformance,
       "ieee8021PSFPCompliances": ieee8021PSFPCompliances,
       "ieee8021PSFPCompliance": ieee8021PSFPCompliance,
       "ieee8021PSFPGroups": ieee8021PSFPGroups,
       "ieee8021PSFPObjectsGroup": ieee8021PSFPObjectsGroup}
)
