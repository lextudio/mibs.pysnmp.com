# SNMP MIB module (IEEE8021-ST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-ST-MIB
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

(ieee8021BridgeBaseComponentId,
 ieee8021BridgeBasePort) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId",
    "ieee8021BridgeBasePort")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021STMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30)
)
ieee8021STMib.setRevisions(
        ("2018-06-21 00:00",
         "2016-08-15 00:00",
         "2016-02-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021STTrafficClassValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class IEEE8021STPTPtimeValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021STNotifications_ObjectIdentity = ObjectIdentity
ieee8021STNotifications = _Ieee8021STNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30, 0)
)
_Ieee8021STObjects_ObjectIdentity = ObjectIdentity
ieee8021STObjects = _Ieee8021STObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30, 1)
)
_Ieee8021STMaxSDUSubtree_ObjectIdentity = ObjectIdentity
ieee8021STMaxSDUSubtree = _Ieee8021STMaxSDUSubtree_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 1)
)
_Ieee8021STMaxSDUTable_Object = MibTable
ieee8021STMaxSDUTable = _Ieee8021STMaxSDUTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021STMaxSDUTable.setStatus("current")
_Ieee8021STMaxSDUEntry_Object = MibTableRow
ieee8021STMaxSDUEntry = _Ieee8021STMaxSDUEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1)
)
ieee8021STMaxSDUEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-ST-MIB", "ieee8021STTrafficClass"),
)
if mibBuilder.loadTexts:
    ieee8021STMaxSDUEntry.setStatus("current")
_Ieee8021STTrafficClass_Type = IEEE8021STTrafficClassValue
_Ieee8021STTrafficClass_Object = MibTableColumn
ieee8021STTrafficClass = _Ieee8021STTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 1),
    _Ieee8021STTrafficClass_Type()
)
ieee8021STTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021STTrafficClass.setStatus("current")


class _Ieee8021STMaxSDU_Type(Unsigned32):
    """Custom type ieee8021STMaxSDU based on Unsigned32"""
    defaultValue = 0


_Ieee8021STMaxSDU_Object = MibTableColumn
ieee8021STMaxSDU = _Ieee8021STMaxSDU_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 2),
    _Ieee8021STMaxSDU_Type()
)
ieee8021STMaxSDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STMaxSDU.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021STMaxSDU.setUnits("octets")


class _Ieee8021TransmissionOverrun_Type(Counter64):
    """Custom type ieee8021TransmissionOverrun based on Counter64"""
    defaultValue = 0


_Ieee8021TransmissionOverrun_Object = MibTableColumn
ieee8021TransmissionOverrun = _Ieee8021TransmissionOverrun_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 1, 1, 1, 3),
    _Ieee8021TransmissionOverrun_Type()
)
ieee8021TransmissionOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TransmissionOverrun.setStatus("current")
_Ieee8021STParameters_ObjectIdentity = ObjectIdentity
ieee8021STParameters = _Ieee8021STParameters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2)
)
_Ieee8021STParametersTable_Object = MibTable
ieee8021STParametersTable = _Ieee8021STParametersTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021STParametersTable.setStatus("current")
_Ieee8021STParametersEntry_Object = MibTableRow
ieee8021STParametersEntry = _Ieee8021STParametersEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1)
)
ieee8021STParametersEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021STParametersEntry.setStatus("current")


class _Ieee8021STGateEnabled_Type(TruthValue):
    """Custom type ieee8021STGateEnabled based on TruthValue"""


_Ieee8021STGateEnabled_Object = MibTableColumn
ieee8021STGateEnabled = _Ieee8021STGateEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 1),
    _Ieee8021STGateEnabled_Type()
)
ieee8021STGateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STGateEnabled.setStatus("current")


class _Ieee8021STAdminGateStates_Type(OctetString):
    """Custom type ieee8021STAdminGateStates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ieee8021STAdminGateStates_Type.__name__ = "OctetString"
_Ieee8021STAdminGateStates_Object = MibTableColumn
ieee8021STAdminGateStates = _Ieee8021STAdminGateStates_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 2),
    _Ieee8021STAdminGateStates_Type()
)
ieee8021STAdminGateStates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STAdminGateStates.setStatus("current")


class _Ieee8021STOperGateStates_Type(OctetString):
    """Custom type ieee8021STOperGateStates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ieee8021STOperGateStates_Type.__name__ = "OctetString"
_Ieee8021STOperGateStates_Object = MibTableColumn
ieee8021STOperGateStates = _Ieee8021STOperGateStates_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 3),
    _Ieee8021STOperGateStates_Type()
)
ieee8021STOperGateStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STOperGateStates.setStatus("current")
_Ieee8021STAdminControlListLength_Type = Unsigned32
_Ieee8021STAdminControlListLength_Object = MibTableColumn
ieee8021STAdminControlListLength = _Ieee8021STAdminControlListLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 4),
    _Ieee8021STAdminControlListLength_Type()
)
ieee8021STAdminControlListLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STAdminControlListLength.setStatus("current")
_Ieee8021STOperControlListLength_Type = Unsigned32
_Ieee8021STOperControlListLength_Object = MibTableColumn
ieee8021STOperControlListLength = _Ieee8021STOperControlListLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 5),
    _Ieee8021STOperControlListLength_Type()
)
ieee8021STOperControlListLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STOperControlListLength.setStatus("current")
_Ieee8021STAdminControlList_Type = OctetString
_Ieee8021STAdminControlList_Object = MibTableColumn
ieee8021STAdminControlList = _Ieee8021STAdminControlList_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 6),
    _Ieee8021STAdminControlList_Type()
)
ieee8021STAdminControlList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STAdminControlList.setStatus("current")
_Ieee8021STOperControlList_Type = OctetString
_Ieee8021STOperControlList_Object = MibTableColumn
ieee8021STOperControlList = _Ieee8021STOperControlList_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 7),
    _Ieee8021STOperControlList_Type()
)
ieee8021STOperControlList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STOperControlList.setStatus("current")
_Ieee8021STAdminCycleTimeNumerator_Type = Unsigned32
_Ieee8021STAdminCycleTimeNumerator_Object = MibTableColumn
ieee8021STAdminCycleTimeNumerator = _Ieee8021STAdminCycleTimeNumerator_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 8),
    _Ieee8021STAdminCycleTimeNumerator_Type()
)
ieee8021STAdminCycleTimeNumerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STAdminCycleTimeNumerator.setStatus("current")
_Ieee8021STAdminCycleTimeDenominator_Type = Unsigned32
_Ieee8021STAdminCycleTimeDenominator_Object = MibTableColumn
ieee8021STAdminCycleTimeDenominator = _Ieee8021STAdminCycleTimeDenominator_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 9),
    _Ieee8021STAdminCycleTimeDenominator_Type()
)
ieee8021STAdminCycleTimeDenominator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STAdminCycleTimeDenominator.setStatus("current")
_Ieee8021STOperCycleTimeNumerator_Type = Unsigned32
_Ieee8021STOperCycleTimeNumerator_Object = MibTableColumn
ieee8021STOperCycleTimeNumerator = _Ieee8021STOperCycleTimeNumerator_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 10),
    _Ieee8021STOperCycleTimeNumerator_Type()
)
ieee8021STOperCycleTimeNumerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STOperCycleTimeNumerator.setStatus("current")
_Ieee8021STOperCycleTimeDenominator_Type = Unsigned32
_Ieee8021STOperCycleTimeDenominator_Object = MibTableColumn
ieee8021STOperCycleTimeDenominator = _Ieee8021STOperCycleTimeDenominator_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 11),
    _Ieee8021STOperCycleTimeDenominator_Type()
)
ieee8021STOperCycleTimeDenominator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STOperCycleTimeDenominator.setStatus("current")
_Ieee8021STAdminCycleTimeExtension_Type = Unsigned32
_Ieee8021STAdminCycleTimeExtension_Object = MibTableColumn
ieee8021STAdminCycleTimeExtension = _Ieee8021STAdminCycleTimeExtension_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 12),
    _Ieee8021STAdminCycleTimeExtension_Type()
)
ieee8021STAdminCycleTimeExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STAdminCycleTimeExtension.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021STAdminCycleTimeExtension.setUnits("nanoseconds")
_Ieee8021STOperCycleTimeExtension_Type = Unsigned32
_Ieee8021STOperCycleTimeExtension_Object = MibTableColumn
ieee8021STOperCycleTimeExtension = _Ieee8021STOperCycleTimeExtension_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 13),
    _Ieee8021STOperCycleTimeExtension_Type()
)
ieee8021STOperCycleTimeExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STOperCycleTimeExtension.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021STOperCycleTimeExtension.setUnits("nanoseconds")
_Ieee8021STAdminBaseTime_Type = IEEE8021STPTPtimeValue
_Ieee8021STAdminBaseTime_Object = MibTableColumn
ieee8021STAdminBaseTime = _Ieee8021STAdminBaseTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 14),
    _Ieee8021STAdminBaseTime_Type()
)
ieee8021STAdminBaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STAdminBaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021STAdminBaseTime.setUnits("PTP time")
_Ieee8021STOperBaseTime_Type = IEEE8021STPTPtimeValue
_Ieee8021STOperBaseTime_Object = MibTableColumn
ieee8021STOperBaseTime = _Ieee8021STOperBaseTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 15),
    _Ieee8021STOperBaseTime_Type()
)
ieee8021STOperBaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STOperBaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021STOperBaseTime.setUnits("PTP time")
_Ieee8021STConfigChange_Type = TruthValue
_Ieee8021STConfigChange_Object = MibTableColumn
ieee8021STConfigChange = _Ieee8021STConfigChange_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 16),
    _Ieee8021STConfigChange_Type()
)
ieee8021STConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021STConfigChange.setStatus("current")
_Ieee8021STConfigChangeTime_Type = IEEE8021STPTPtimeValue
_Ieee8021STConfigChangeTime_Object = MibTableColumn
ieee8021STConfigChangeTime = _Ieee8021STConfigChangeTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 17),
    _Ieee8021STConfigChangeTime_Type()
)
ieee8021STConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STConfigChangeTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021STConfigChangeTime.setUnits("PTP time")
_Ieee8021STTickGranularity_Type = Unsigned32
_Ieee8021STTickGranularity_Object = MibTableColumn
ieee8021STTickGranularity = _Ieee8021STTickGranularity_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 18),
    _Ieee8021STTickGranularity_Type()
)
ieee8021STTickGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STTickGranularity.setStatus("current")
_Ieee8021STCurrentTime_Type = IEEE8021STPTPtimeValue
_Ieee8021STCurrentTime_Object = MibTableColumn
ieee8021STCurrentTime = _Ieee8021STCurrentTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 19),
    _Ieee8021STCurrentTime_Type()
)
ieee8021STCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STCurrentTime.setStatus("current")
_Ieee8021STConfigPending_Type = TruthValue
_Ieee8021STConfigPending_Object = MibTableColumn
ieee8021STConfigPending = _Ieee8021STConfigPending_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 20),
    _Ieee8021STConfigPending_Type()
)
ieee8021STConfigPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STConfigPending.setStatus("current")
_Ieee8021STConfigChangeError_Type = Counter64
_Ieee8021STConfigChangeError_Object = MibTableColumn
ieee8021STConfigChangeError = _Ieee8021STConfigChangeError_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 21),
    _Ieee8021STConfigChangeError_Type()
)
ieee8021STConfigChangeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STConfigChangeError.setStatus("current")
_Ieee8021STSupportedListMax_Type = Unsigned32
_Ieee8021STSupportedListMax_Object = MibTableColumn
ieee8021STSupportedListMax = _Ieee8021STSupportedListMax_Object(
    (1, 3, 111, 2, 802, 1, 1, 30, 1, 2, 1, 1, 22),
    _Ieee8021STSupportedListMax_Type()
)
ieee8021STSupportedListMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021STSupportedListMax.setStatus("current")
_Ieee8021STConformance_ObjectIdentity = ObjectIdentity
ieee8021STConformance = _Ieee8021STConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30, 2)
)
_Ieee8021STCompliances_ObjectIdentity = ObjectIdentity
ieee8021STCompliances = _Ieee8021STCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30, 2, 1)
)
_Ieee8021STGroups_ObjectIdentity = ObjectIdentity
ieee8021STGroups = _Ieee8021STGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 30, 2, 2)
)

# Managed Objects groups

ieee8021STObjectsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 30, 2, 2, 1)
)
ieee8021STObjectsGroup.setObjects(
      *(("IEEE8021-ST-MIB", "ieee8021STMaxSDU"),
        ("IEEE8021-ST-MIB", "ieee8021TransmissionOverrun"),
        ("IEEE8021-ST-MIB", "ieee8021STGateEnabled"),
        ("IEEE8021-ST-MIB", "ieee8021STAdminGateStates"),
        ("IEEE8021-ST-MIB", "ieee8021STOperGateStates"),
        ("IEEE8021-ST-MIB", "ieee8021STAdminControlListLength"),
        ("IEEE8021-ST-MIB", "ieee8021STOperControlListLength"),
        ("IEEE8021-ST-MIB", "ieee8021STAdminControlList"),
        ("IEEE8021-ST-MIB", "ieee8021STOperControlList"),
        ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeNumerator"),
        ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeDenominator"),
        ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeNumerator"),
        ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeDenominator"),
        ("IEEE8021-ST-MIB", "ieee8021STAdminCycleTimeExtension"),
        ("IEEE8021-ST-MIB", "ieee8021STOperCycleTimeExtension"),
        ("IEEE8021-ST-MIB", "ieee8021STAdminBaseTime"),
        ("IEEE8021-ST-MIB", "ieee8021STOperBaseTime"),
        ("IEEE8021-ST-MIB", "ieee8021STConfigChange"),
        ("IEEE8021-ST-MIB", "ieee8021STConfigChangeTime"),
        ("IEEE8021-ST-MIB", "ieee8021STTickGranularity"),
        ("IEEE8021-ST-MIB", "ieee8021STCurrentTime"),
        ("IEEE8021-ST-MIB", "ieee8021STConfigPending"),
        ("IEEE8021-ST-MIB", "ieee8021STConfigChangeError"),
        ("IEEE8021-ST-MIB", "ieee8021STSupportedListMax"))
)
if mibBuilder.loadTexts:
    ieee8021STObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021STCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 30, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021STCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-ST-MIB",
    **{"IEEE8021STTrafficClassValue": IEEE8021STTrafficClassValue,
       "IEEE8021STPTPtimeValue": IEEE8021STPTPtimeValue,
       "ieee8021STMib": ieee8021STMib,
       "ieee8021STNotifications": ieee8021STNotifications,
       "ieee8021STObjects": ieee8021STObjects,
       "ieee8021STMaxSDUSubtree": ieee8021STMaxSDUSubtree,
       "ieee8021STMaxSDUTable": ieee8021STMaxSDUTable,
       "ieee8021STMaxSDUEntry": ieee8021STMaxSDUEntry,
       "ieee8021STTrafficClass": ieee8021STTrafficClass,
       "ieee8021STMaxSDU": ieee8021STMaxSDU,
       "ieee8021TransmissionOverrun": ieee8021TransmissionOverrun,
       "ieee8021STParameters": ieee8021STParameters,
       "ieee8021STParametersTable": ieee8021STParametersTable,
       "ieee8021STParametersEntry": ieee8021STParametersEntry,
       "ieee8021STGateEnabled": ieee8021STGateEnabled,
       "ieee8021STAdminGateStates": ieee8021STAdminGateStates,
       "ieee8021STOperGateStates": ieee8021STOperGateStates,
       "ieee8021STAdminControlListLength": ieee8021STAdminControlListLength,
       "ieee8021STOperControlListLength": ieee8021STOperControlListLength,
       "ieee8021STAdminControlList": ieee8021STAdminControlList,
       "ieee8021STOperControlList": ieee8021STOperControlList,
       "ieee8021STAdminCycleTimeNumerator": ieee8021STAdminCycleTimeNumerator,
       "ieee8021STAdminCycleTimeDenominator": ieee8021STAdminCycleTimeDenominator,
       "ieee8021STOperCycleTimeNumerator": ieee8021STOperCycleTimeNumerator,
       "ieee8021STOperCycleTimeDenominator": ieee8021STOperCycleTimeDenominator,
       "ieee8021STAdminCycleTimeExtension": ieee8021STAdminCycleTimeExtension,
       "ieee8021STOperCycleTimeExtension": ieee8021STOperCycleTimeExtension,
       "ieee8021STAdminBaseTime": ieee8021STAdminBaseTime,
       "ieee8021STOperBaseTime": ieee8021STOperBaseTime,
       "ieee8021STConfigChange": ieee8021STConfigChange,
       "ieee8021STConfigChangeTime": ieee8021STConfigChangeTime,
       "ieee8021STTickGranularity": ieee8021STTickGranularity,
       "ieee8021STCurrentTime": ieee8021STCurrentTime,
       "ieee8021STConfigPending": ieee8021STConfigPending,
       "ieee8021STConfigChangeError": ieee8021STConfigChangeError,
       "ieee8021STSupportedListMax": ieee8021STSupportedListMax,
       "ieee8021STConformance": ieee8021STConformance,
       "ieee8021STCompliances": ieee8021STCompliances,
       "ieee8021STCompliance": ieee8021STCompliance,
       "ieee8021STGroups": ieee8021STGroups,
       "ieee8021STObjectsGroup": ieee8021STObjectsGroup}
)
