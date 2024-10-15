# SNMP MIB module (ISOVIEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISOVIEW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:58 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bitec_ObjectIdentity = ObjectIdentity
bitec = _Bitec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170)
)
_Bdn_ObjectIdentity = ObjectIdentity
bdn = _Bdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1)
)
_Third_party_ObjectIdentity = ObjectIdentity
third_party = _Third_party_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1)
)
_Retix_ObjectIdentity = ObjectIdentity
retix = _Retix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1)
)
_Station_ObjectIdentity = ObjectIdentity
station = _Station_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1)
)


class _StationTime_Type(OctetString):
    """Custom type stationTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_StationTime_Type.__name__ = "OctetString"
_StationTime_Object = MibScalar
stationTime = _StationTime_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 1),
    _StationTime_Type()
)
stationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationTime.setStatus("mandatory")
_StationResetCounter_Type = Counter32
_StationResetCounter_Object = MibScalar
stationResetCounter = _StationResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 2),
    _StationResetCounter_Type()
)
stationResetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationResetCounter.setStatus("mandatory")
_FreeBufferCount_Type = Integer32
_FreeBufferCount_Object = MibScalar
freeBufferCount = _FreeBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 3),
    _FreeBufferCount_Type()
)
freeBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeBufferCount.setStatus("optional")
_FreeHeaderCount_Type = Integer32
_FreeHeaderCount_Object = MibScalar
freeHeaderCount = _FreeHeaderCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 4),
    _FreeHeaderCount_Type()
)
freeHeaderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeHeaderCount.setStatus("optional")


class _PhysBlkSize_Type(Integer32):
    """Custom type physBlkSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1600),
    )


_PhysBlkSize_Type.__name__ = "Integer32"
_PhysBlkSize_Object = MibScalar
physBlkSize = _PhysBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 5),
    _PhysBlkSize_Type()
)
physBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physBlkSize.setStatus("optional")


class _NewPhysBlkSize_Type(Integer32):
    """Custom type newPhysBlkSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1600),
    )


_NewPhysBlkSize_Type.__name__ = "Integer32"
_NewPhysBlkSize_Object = MibScalar
newPhysBlkSize = _NewPhysBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 6),
    _NewPhysBlkSize_Type()
)
newPhysBlkSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newPhysBlkSize.setStatus("optional")
_ResetStation_Type = Integer32
_ResetStation_Object = MibScalar
resetStation = _ResetStation_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 7),
    _ResetStation_Type()
)
resetStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStation.setStatus("mandatory")
_InitStation_Type = Integer32
_InitStation_Object = MibScalar
initStation = _InitStation_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 8),
    _InitStation_Type()
)
initStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initStation.setStatus("mandatory")
_ResetStats_Type = Integer32
_ResetStats_Object = MibScalar
resetStats = _ResetStats_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 9),
    _ResetStats_Type()
)
resetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStats.setStatus("mandatory")
_ProcessorLoading_Type = Integer32
_ProcessorLoading_Object = MibScalar
processorLoading = _ProcessorLoading_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 10),
    _ProcessorLoading_Type()
)
processorLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorLoading.setStatus("optional")
_TrapDestinationTable_ObjectIdentity = ObjectIdentity
trapDestinationTable = _TrapDestinationTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("mandatory")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "trapDestEntryIpAddr"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("mandatory")
_TrapDestEntryIpAddr_Type = IpAddress
_TrapDestEntryIpAddr_Object = MibTableColumn
trapDestEntryIpAddr = _TrapDestEntryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11, 1, 1, 1),
    _TrapDestEntryIpAddr_Type()
)
trapDestEntryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestEntryIpAddr.setStatus("mandatory")


class _TrapDestEntryCommunityName_Type(OctetString):
    """Custom type trapDestEntryCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TrapDestEntryCommunityName_Type.__name__ = "OctetString"
_TrapDestEntryCommunityName_Object = MibTableColumn
trapDestEntryCommunityName = _TrapDestEntryCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11, 1, 1, 2),
    _TrapDestEntryCommunityName_Type()
)
trapDestEntryCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestEntryCommunityName.setStatus("mandatory")
_TrapDestEntryType_Type = Integer32
_TrapDestEntryType_Object = MibTableColumn
trapDestEntryType = _TrapDestEntryType_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11, 1, 1, 3),
    _TrapDestEntryType_Type()
)
trapDestEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestEntryType.setStatus("mandatory")
_TrapDestAction_Type = Integer32
_TrapDestAction_Object = MibScalar
trapDestAction = _TrapDestAction_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11, 2),
    _TrapDestAction_Type()
)
trapDestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestAction.setStatus("mandatory")


class _TrapDestPage_Type(OctetString):
    """Custom type trapDestPage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(240, 240),
    )


_TrapDestPage_Type.__name__ = "OctetString"
_TrapDestPage_Object = MibScalar
trapDestPage = _TrapDestPage_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 11, 3),
    _TrapDestPage_Type()
)
trapDestPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestPage.setStatus("mandatory")


class _PassWord_Type(OctetString):
    """Custom type passWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PassWord_Type.__name__ = "OctetString"
_PassWord_Object = MibScalar
passWord = _PassWord_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 12),
    _PassWord_Type()
)
passWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passWord.setStatus("optional")
_SnmpAccessPolicyObject_ObjectIdentity = ObjectIdentity
snmpAccessPolicyObject = _SnmpAccessPolicyObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13)
)
_SnmpAccessPolicyTable_Object = MibTable
snmpAccessPolicyTable = _SnmpAccessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    snmpAccessPolicyTable.setStatus("mandatory")
_SnmpAccessPolicyEntry_Object = MibTableRow
snmpAccessPolicyEntry = _SnmpAccessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 1, 1)
)
snmpAccessPolicyEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "accessPolicyIndex"),
)
if mibBuilder.loadTexts:
    snmpAccessPolicyEntry.setStatus("mandatory")
_AccessPolicyIndex_Type = Integer32
_AccessPolicyIndex_Object = MibTableColumn
accessPolicyIndex = _AccessPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 1, 1, 1),
    _AccessPolicyIndex_Type()
)
accessPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPolicyIndex.setStatus("mandatory")


class _CommunityName_Type(OctetString):
    """Custom type communityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CommunityName_Type.__name__ = "OctetString"
_CommunityName_Object = MibTableColumn
communityName = _CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 1, 1, 2),
    _CommunityName_Type()
)
communityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityName.setStatus("mandatory")
_AccessMode_Type = Integer32
_AccessMode_Object = MibTableColumn
accessMode = _AccessMode_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 1, 1, 3),
    _AccessMode_Type()
)
accessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessMode.setStatus("mandatory")
_SnmpAccessPolicyType_Type = Integer32
_SnmpAccessPolicyType_Object = MibTableColumn
snmpAccessPolicyType = _SnmpAccessPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 1, 1, 4),
    _SnmpAccessPolicyType_Type()
)
snmpAccessPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessPolicyType.setStatus("mandatory")
_SnmpAccessPolicyAction_Type = Integer32
_SnmpAccessPolicyAction_Object = MibScalar
snmpAccessPolicyAction = _SnmpAccessPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 2),
    _SnmpAccessPolicyAction_Type()
)
snmpAccessPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessPolicyAction.setStatus("mandatory")


class _SnmpAccessPolicyPage_Type(OctetString):
    """Custom type snmpAccessPolicyPage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_SnmpAccessPolicyPage_Type.__name__ = "OctetString"
_SnmpAccessPolicyPage_Object = MibScalar
snmpAccessPolicyPage = _SnmpAccessPolicyPage_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 13, 3),
    _SnmpAccessPolicyPage_Type()
)
snmpAccessPolicyPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessPolicyPage.setStatus("mandatory")


class _AuthenticationTrapStatus_Type(Integer32):
    """Custom type authenticationTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AuthenticationTrapStatus_Type.__name__ = "Integer32"
_AuthenticationTrapStatus_Object = MibScalar
authenticationTrapStatus = _AuthenticationTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 14),
    _AuthenticationTrapStatus_Type()
)
authenticationTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationTrapStatus.setStatus("mandatory")


class _SerialTxQueueSize_Type(Integer32):
    """Custom type serialTxQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SerialTxQueueSize_Type.__name__ = "Integer32"
_SerialTxQueueSize_Object = MibScalar
serialTxQueueSize = _SerialTxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 15),
    _SerialTxQueueSize_Type()
)
serialTxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTxQueueSize.setStatus("optional")
_InternalQueueCurrentLength_Type = Integer32
_InternalQueueCurrentLength_Object = MibScalar
internalQueueCurrentLength = _InternalQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 16),
    _InternalQueueCurrentLength_Type()
)
internalQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalQueueCurrentLength.setStatus("optional")
_QueueUpperLimit_Type = Integer32
_QueueUpperLimit_Object = MibScalar
queueUpperLimit = _QueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 17),
    _QueueUpperLimit_Type()
)
queueUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueUpperLimit.setStatus("optional")
_LanQueueSize_Type = Integer32
_LanQueueSize_Object = MibScalar
lanQueueSize = _LanQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 1, 18),
    _LanQueueSize_Type()
)
lanQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanQueueSize.setStatus("optional")
_Lapb_ObjectIdentity = ObjectIdentity
lapb = _Lapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2)
)
_LapbNumber_Type = Integer32
_LapbNumber_Object = MibScalar
lapbNumber = _LapbNumber_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 1),
    _LapbNumber_Type()
)
lapbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbNumber.setStatus("mandatory")
_LapbTable_Object = MibTable
lapbTable = _LapbTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lapbTable.setStatus("mandatory")
_LapbEntry_Object = MibTableRow
lapbEntry = _LapbEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1)
)
lapbEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "lapbIndex"),
)
if mibBuilder.loadTexts:
    lapbEntry.setStatus("mandatory")
_LapbIndex_Type = Integer32
_LapbIndex_Object = MibTableColumn
lapbIndex = _LapbIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 1),
    _LapbIndex_Type()
)
lapbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbIndex.setStatus("mandatory")


class _LapbModeT1_Type(Integer32):
    """Custom type lapbModeT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LapbModeT1_Type.__name__ = "Integer32"
_LapbModeT1_Object = MibTableColumn
lapbModeT1 = _LapbModeT1_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 2),
    _LapbModeT1_Type()
)
lapbModeT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbModeT1.setStatus("mandatory")
_LapbAutoT1value_Type = Integer32
_LapbAutoT1value_Object = MibTableColumn
lapbAutoT1value = _LapbAutoT1value_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 3),
    _LapbAutoT1value_Type()
)
lapbAutoT1value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbAutoT1value.setStatus("mandatory")


class _LapbManualT1value_Type(Integer32):
    """Custom type lapbManualT1value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_LapbManualT1value_Type.__name__ = "Integer32"
_LapbManualT1value_Object = MibTableColumn
lapbManualT1value = _LapbManualT1value_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 4),
    _LapbManualT1value_Type()
)
lapbManualT1value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbManualT1value.setStatus("mandatory")


class _LapbWindow_Type(Integer32):
    """Custom type lapbWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 127),
    )


_LapbWindow_Type.__name__ = "Integer32"
_LapbWindow_Object = MibTableColumn
lapbWindow = _LapbWindow_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 5),
    _LapbWindow_Type()
)
lapbWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbWindow.setStatus("mandatory")


class _LapbPolarity_Type(Integer32):
    """Custom type lapbPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LapbPolarity_Type.__name__ = "Integer32"
_LapbPolarity_Object = MibTableColumn
lapbPolarity = _LapbPolarity_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 6),
    _LapbPolarity_Type()
)
lapbPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbPolarity.setStatus("mandatory")
_LapbResetCount_Type = Counter32
_LapbResetCount_Object = MibTableColumn
lapbResetCount = _LapbResetCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 7),
    _LapbResetCount_Type()
)
lapbResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbResetCount.setStatus("mandatory")
_LapbSendFrameCount_Type = Counter32
_LapbSendFrameCount_Object = MibTableColumn
lapbSendFrameCount = _LapbSendFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 8),
    _LapbSendFrameCount_Type()
)
lapbSendFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbSendFrameCount.setStatus("mandatory")
_LapbRcvFrameCount_Type = Counter32
_LapbRcvFrameCount_Object = MibTableColumn
lapbRcvFrameCount = _LapbRcvFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 9),
    _LapbRcvFrameCount_Type()
)
lapbRcvFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbRcvFrameCount.setStatus("mandatory")
_LapbSendOctetCount_Type = Counter32
_LapbSendOctetCount_Object = MibTableColumn
lapbSendOctetCount = _LapbSendOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 10),
    _LapbSendOctetCount_Type()
)
lapbSendOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbSendOctetCount.setStatus("mandatory")
_LapbRcvOctetCount_Type = Counter32
_LapbRcvOctetCount_Object = MibTableColumn
lapbRcvOctetCount = _LapbRcvOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 11),
    _LapbRcvOctetCount_Type()
)
lapbRcvOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbRcvOctetCount.setStatus("mandatory")
_LapbAbortCount_Type = Counter32
_LapbAbortCount_Object = MibTableColumn
lapbAbortCount = _LapbAbortCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 12),
    _LapbAbortCount_Type()
)
lapbAbortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbAbortCount.setStatus("mandatory")
_LapbCrcErrorCount_Type = Counter32
_LapbCrcErrorCount_Object = MibTableColumn
lapbCrcErrorCount = _LapbCrcErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 13),
    _LapbCrcErrorCount_Type()
)
lapbCrcErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCrcErrorCount.setStatus("mandatory")


class _LapbState_Type(Integer32):
    """Custom type lapbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LapbState_Type.__name__ = "Integer32"
_LapbState_Object = MibTableColumn
lapbState = _LapbState_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 14),
    _LapbState_Type()
)
lapbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbState.setStatus("mandatory")


class _LapbLastResetTime_Type(OctetString):
    """Custom type lapbLastResetTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_LapbLastResetTime_Type.__name__ = "OctetString"
_LapbLastResetTime_Object = MibTableColumn
lapbLastResetTime = _LapbLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 15),
    _LapbLastResetTime_Type()
)
lapbLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbLastResetTime.setStatus("mandatory")


class _LapbLastResetReason_Type(Integer32):
    """Custom type lapbLastResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_LapbLastResetReason_Type.__name__ = "Integer32"
_LapbLastResetReason_Object = MibTableColumn
lapbLastResetReason = _LapbLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 16),
    _LapbLastResetReason_Type()
)
lapbLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbLastResetReason.setStatus("mandatory")
_LapbLinkReset_Type = Integer32
_LapbLinkReset_Object = MibTableColumn
lapbLinkReset = _LapbLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 2, 1, 17),
    _LapbLinkReset_Type()
)
lapbLinkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbLinkReset.setStatus("mandatory")
_LapbRetryCount_Type = Integer32
_LapbRetryCount_Object = MibScalar
lapbRetryCount = _LapbRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 2, 3),
    _LapbRetryCount_Type()
)
lapbRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbRetryCount.setStatus("mandatory")
_Ieee8023_ObjectIdentity = ObjectIdentity
ieee8023 = _Ieee8023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3)
)
_Ieee8023Number_Type = Integer32
_Ieee8023Number_Object = MibScalar
ieee8023Number = _Ieee8023Number_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 1),
    _Ieee8023Number_Type()
)
ieee8023Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023Number.setStatus("mandatory")
_Ieee8023Table_Object = MibTable
ieee8023Table = _Ieee8023Table_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8023Table.setStatus("mandatory")
_Ieee8023Entry_Object = MibTableRow
ieee8023Entry = _Ieee8023Entry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1)
)
ieee8023Entry.setIndexNames(
    (0, "ISOVIEW-MIB", "ieee8023Index"),
)
if mibBuilder.loadTexts:
    ieee8023Entry.setStatus("mandatory")
_Ieee8023Index_Type = Integer32
_Ieee8023Index_Object = MibTableColumn
ieee8023Index = _Ieee8023Index_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 1),
    _Ieee8023Index_Type()
)
ieee8023Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023Index.setStatus("mandatory")
_Ieee8023FramesTransmittedOks_Type = Counter32
_Ieee8023FramesTransmittedOks_Object = MibTableColumn
ieee8023FramesTransmittedOks = _Ieee8023FramesTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 2),
    _Ieee8023FramesTransmittedOks_Type()
)
ieee8023FramesTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FramesTransmittedOks.setStatus("mandatory")
_Ieee8023SingleCollisionFrames_Type = Counter32
_Ieee8023SingleCollisionFrames_Object = MibTableColumn
ieee8023SingleCollisionFrames = _Ieee8023SingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 3),
    _Ieee8023SingleCollisionFrames_Type()
)
ieee8023SingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023SingleCollisionFrames.setStatus("mandatory")
_Ieee8023MultipleCollisionFrames_Type = Counter32
_Ieee8023MultipleCollisionFrames_Object = MibTableColumn
ieee8023MultipleCollisionFrames = _Ieee8023MultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 4),
    _Ieee8023MultipleCollisionFrames_Type()
)
ieee8023MultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MultipleCollisionFrames.setStatus("mandatory")
_Ieee8023OctetsTransmittedOks_Type = Counter32
_Ieee8023OctetsTransmittedOks_Object = MibTableColumn
ieee8023OctetsTransmittedOks = _Ieee8023OctetsTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 5),
    _Ieee8023OctetsTransmittedOks_Type()
)
ieee8023OctetsTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023OctetsTransmittedOks.setStatus("mandatory")
_Ieee8023DeferredTransmissions_Type = Counter32
_Ieee8023DeferredTransmissions_Object = MibTableColumn
ieee8023DeferredTransmissions = _Ieee8023DeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 6),
    _Ieee8023DeferredTransmissions_Type()
)
ieee8023DeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023DeferredTransmissions.setStatus("mandatory")
_Ieee8023MulticastFramesTransmittedOks_Type = Counter32
_Ieee8023MulticastFramesTransmittedOks_Object = MibTableColumn
ieee8023MulticastFramesTransmittedOks = _Ieee8023MulticastFramesTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 7),
    _Ieee8023MulticastFramesTransmittedOks_Type()
)
ieee8023MulticastFramesTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MulticastFramesTransmittedOks.setStatus("optional")
_Ieee8023BroadcastFramesTransmittedOks_Type = Counter32
_Ieee8023BroadcastFramesTransmittedOks_Object = MibTableColumn
ieee8023BroadcastFramesTransmittedOks = _Ieee8023BroadcastFramesTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 8),
    _Ieee8023BroadcastFramesTransmittedOks_Type()
)
ieee8023BroadcastFramesTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023BroadcastFramesTransmittedOks.setStatus("optional")
_Ieee8023LateCollisions_Type = Counter32
_Ieee8023LateCollisions_Object = MibScalar
ieee8023LateCollisions = _Ieee8023LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 9),
    _Ieee8023LateCollisions_Type()
)
ieee8023LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023LateCollisions.setStatus("mandatory")
_Ieee8023ExcessiveCollisions_Type = Counter32
_Ieee8023ExcessiveCollisions_Object = MibScalar
ieee8023ExcessiveCollisions = _Ieee8023ExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 10),
    _Ieee8023ExcessiveCollisions_Type()
)
ieee8023ExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023ExcessiveCollisions.setStatus("mandatory")
_Ieee8023InternalMACTransmitErrors_Type = Counter32
_Ieee8023InternalMACTransmitErrors_Object = MibScalar
ieee8023InternalMACTransmitErrors = _Ieee8023InternalMACTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 11),
    _Ieee8023InternalMACTransmitErrors_Type()
)
ieee8023InternalMACTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023InternalMACTransmitErrors.setStatus("mandatory")
_Ieee8023CarrierSenseErrors_Type = Counter32
_Ieee8023CarrierSenseErrors_Object = MibTableColumn
ieee8023CarrierSenseErrors = _Ieee8023CarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 12),
    _Ieee8023CarrierSenseErrors_Type()
)
ieee8023CarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023CarrierSenseErrors.setStatus("mandatory")
_Ieee8023ExcessiveDeferrals_Type = Counter32
_Ieee8023ExcessiveDeferrals_Object = MibScalar
ieee8023ExcessiveDeferrals = _Ieee8023ExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 13),
    _Ieee8023ExcessiveDeferrals_Type()
)
ieee8023ExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023ExcessiveDeferrals.setStatus("optional")
_Ieee8023FramesReceivedOks_Type = Counter32
_Ieee8023FramesReceivedOks_Object = MibTableColumn
ieee8023FramesReceivedOks = _Ieee8023FramesReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 14),
    _Ieee8023FramesReceivedOks_Type()
)
ieee8023FramesReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FramesReceivedOks.setStatus("mandatory")
_Ieee8023OctetsReceivedOks_Type = Counter32
_Ieee8023OctetsReceivedOks_Object = MibTableColumn
ieee8023OctetsReceivedOks = _Ieee8023OctetsReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 15),
    _Ieee8023OctetsReceivedOks_Type()
)
ieee8023OctetsReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023OctetsReceivedOks.setStatus("mandatory")
_Ieee8023MulticastFramesReceivedOks_Type = Counter32
_Ieee8023MulticastFramesReceivedOks_Object = MibTableColumn
ieee8023MulticastFramesReceivedOks = _Ieee8023MulticastFramesReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 16),
    _Ieee8023MulticastFramesReceivedOks_Type()
)
ieee8023MulticastFramesReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MulticastFramesReceivedOks.setStatus("optional")
_Ieee8023BroadcastFramesReceivedOks_Type = Counter32
_Ieee8023BroadcastFramesReceivedOks_Object = MibTableColumn
ieee8023BroadcastFramesReceivedOks = _Ieee8023BroadcastFramesReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 17),
    _Ieee8023BroadcastFramesReceivedOks_Type()
)
ieee8023BroadcastFramesReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023BroadcastFramesReceivedOks.setStatus("optional")
_Ieee8023FrameTooLongs_Type = Counter32
_Ieee8023FrameTooLongs_Object = MibTableColumn
ieee8023FrameTooLongs = _Ieee8023FrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 18),
    _Ieee8023FrameTooLongs_Type()
)
ieee8023FrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FrameTooLongs.setStatus("optional")
_Ieee8023AlignmentErrors_Type = Counter32
_Ieee8023AlignmentErrors_Object = MibTableColumn
ieee8023AlignmentErrors = _Ieee8023AlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 19),
    _Ieee8023AlignmentErrors_Type()
)
ieee8023AlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023AlignmentErrors.setStatus("mandatory")
_Ieee8023FCSErrors_Type = Counter32
_Ieee8023FCSErrors_Object = MibTableColumn
ieee8023FCSErrors = _Ieee8023FCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 20),
    _Ieee8023FCSErrors_Type()
)
ieee8023FCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FCSErrors.setStatus("mandatory")
_Ieee8023inRangeLengthErrors_Type = Counter32
_Ieee8023inRangeLengthErrors_Object = MibTableColumn
ieee8023inRangeLengthErrors = _Ieee8023inRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 21),
    _Ieee8023inRangeLengthErrors_Type()
)
ieee8023inRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023inRangeLengthErrors.setStatus("optional")
_Ieee8023outOfRangeLengthFields_Type = Counter32
_Ieee8023outOfRangeLengthFields_Object = MibTableColumn
ieee8023outOfRangeLengthFields = _Ieee8023outOfRangeLengthFields_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 22),
    _Ieee8023outOfRangeLengthFields_Type()
)
ieee8023outOfRangeLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023outOfRangeLengthFields.setStatus("optional")
_Ieee8023InternalMACReceiveErrors_Type = Counter32
_Ieee8023InternalMACReceiveErrors_Object = MibTableColumn
ieee8023InternalMACReceiveErrors = _Ieee8023InternalMACReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 23),
    _Ieee8023InternalMACReceiveErrors_Type()
)
ieee8023InternalMACReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023InternalMACReceiveErrors.setStatus("mandatory")


class _Ieee8023InitializeMAC_Type(Integer32):
    """Custom type ieee8023InitializeMAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initialize", 1)
    )


_Ieee8023InitializeMAC_Type.__name__ = "Integer32"
_Ieee8023InitializeMAC_Object = MibTableColumn
ieee8023InitializeMAC = _Ieee8023InitializeMAC_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 24),
    _Ieee8023InitializeMAC_Type()
)
ieee8023InitializeMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023InitializeMAC.setStatus("mandatory")


class _Ieee8023PromiscuousReceiveStatus_Type(Integer32):
    """Custom type ieee8023PromiscuousReceiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_Ieee8023PromiscuousReceiveStatus_Type.__name__ = "Integer32"
_Ieee8023PromiscuousReceiveStatus_Object = MibTableColumn
ieee8023PromiscuousReceiveStatus = _Ieee8023PromiscuousReceiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 25),
    _Ieee8023PromiscuousReceiveStatus_Type()
)
ieee8023PromiscuousReceiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023PromiscuousReceiveStatus.setStatus("mandatory")


class _Ieee8023MACSubLayerStatus_Type(Integer32):
    """Custom type ieee8023MACSubLayerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_Ieee8023MACSubLayerStatus_Type.__name__ = "Integer32"
_Ieee8023MACSubLayerStatus_Object = MibTableColumn
ieee8023MACSubLayerStatus = _Ieee8023MACSubLayerStatus_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 26),
    _Ieee8023MACSubLayerStatus_Type()
)
ieee8023MACSubLayerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023MACSubLayerStatus.setStatus("optional")


class _Ieee8023TransmitStatus_Type(Integer32):
    """Custom type ieee8023TransmitStatus based on Integer32"""
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


_Ieee8023TransmitStatus_Type.__name__ = "Integer32"
_Ieee8023TransmitStatus_Object = MibTableColumn
ieee8023TransmitStatus = _Ieee8023TransmitStatus_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 27),
    _Ieee8023TransmitStatus_Type()
)
ieee8023TransmitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023TransmitStatus.setStatus("optional")


class _Ieee8023MulticastReceiveStatus_Type(Integer32):
    """Custom type ieee8023MulticastReceiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_Ieee8023MulticastReceiveStatus_Type.__name__ = "Integer32"
_Ieee8023MulticastReceiveStatus_Object = MibTableColumn
ieee8023MulticastReceiveStatus = _Ieee8023MulticastReceiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 28),
    _Ieee8023MulticastReceiveStatus_Type()
)
ieee8023MulticastReceiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023MulticastReceiveStatus.setStatus("optional")


class _Ieee8023MACAddress_Type(OctetString):
    """Custom type ieee8023MACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ieee8023MACAddress_Type.__name__ = "OctetString"
_Ieee8023MACAddress_Object = MibTableColumn
ieee8023MACAddress = _Ieee8023MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 29),
    _Ieee8023MACAddress_Type()
)
ieee8023MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MACAddress.setStatus("optional")
_Ieee8023SQETestErrors_Type = Counter32
_Ieee8023SQETestErrors_Object = MibTableColumn
ieee8023SQETestErrors = _Ieee8023SQETestErrors_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 2, 1, 30),
    _Ieee8023SQETestErrors_Type()
)
ieee8023SQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023SQETestErrors.setStatus("mandatory")
_Ieee8023NewMACAddress_Object = MibTable
ieee8023NewMACAddress = _Ieee8023NewMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ieee8023NewMACAddress.setStatus("mandatory")
_Ieee8023NewMACAddressEntry_Object = MibTableRow
ieee8023NewMACAddressEntry = _Ieee8023NewMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 3, 1)
)
ieee8023NewMACAddressEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "ieee8023NewMACAddressIndex"),
)
if mibBuilder.loadTexts:
    ieee8023NewMACAddressEntry.setStatus("mandatory")
_Ieee8023NewMACAddressIndex_Type = Integer32
_Ieee8023NewMACAddressIndex_Object = MibTableColumn
ieee8023NewMACAddressIndex = _Ieee8023NewMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 3, 1, 1),
    _Ieee8023NewMACAddressIndex_Type()
)
ieee8023NewMACAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023NewMACAddressIndex.setStatus("mandatory")


class _Ieee8023NewMACAddressValue_Type(OctetString):
    """Custom type ieee8023NewMACAddressValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ieee8023NewMACAddressValue_Type.__name__ = "OctetString"
_Ieee8023NewMACAddressValue_Object = MibTableColumn
ieee8023NewMACAddressValue = _Ieee8023NewMACAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 3, 3, 1, 2),
    _Ieee8023NewMACAddressValue_Type()
)
ieee8023NewMACAddressValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023NewMACAddressValue.setStatus("mandatory")
_PhySerIf_ObjectIdentity = ObjectIdentity
phySerIf = _PhySerIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4)
)
_PhySerIfNumber_Type = Integer32
_PhySerIfNumber_Object = MibScalar
phySerIfNumber = _PhySerIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 1),
    _PhySerIfNumber_Type()
)
phySerIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfNumber.setStatus("mandatory")
_PhySerIfTable_Object = MibTable
phySerIfTable = _PhySerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    phySerIfTable.setStatus("mandatory")
_PhySerIfEntry_Object = MibTableRow
phySerIfEntry = _PhySerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1)
)
phySerIfEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "phySerIfIndex"),
)
if mibBuilder.loadTexts:
    phySerIfEntry.setStatus("mandatory")
_PhySerIfIndex_Type = Integer32
_PhySerIfIndex_Object = MibTableColumn
phySerIfIndex = _PhySerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 1),
    _PhySerIfIndex_Type()
)
phySerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfIndex.setStatus("mandatory")


class _PhySerIfInterfaceType_Type(Integer32):
    """Custom type phySerIfInterfaceType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("g703", 4),
          ("rs232", 7),
          ("rs449", 3),
          ("t1", 8),
          ("v35", 5),
          ("v35btb", 6),
          ("x21dce", 2),
          ("x21dte", 1))
    )


_PhySerIfInterfaceType_Type.__name__ = "Integer32"
_PhySerIfInterfaceType_Object = MibTableColumn
phySerIfInterfaceType = _PhySerIfInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 2),
    _PhySerIfInterfaceType_Type()
)
phySerIfInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfInterfaceType.setStatus("mandatory")
_PhySerIfMeasuredSpeed_Type = Integer32
_PhySerIfMeasuredSpeed_Object = MibTableColumn
phySerIfMeasuredSpeed = _PhySerIfMeasuredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 3),
    _PhySerIfMeasuredSpeed_Type()
)
phySerIfMeasuredSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfMeasuredSpeed.setStatus("mandatory")


class _PhySerIfIsSpeedsettable_Type(Integer32):
    """Custom type phySerIfIsSpeedsettable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PhySerIfIsSpeedsettable_Type.__name__ = "Integer32"
_PhySerIfIsSpeedsettable_Object = MibTableColumn
phySerIfIsSpeedsettable = _PhySerIfIsSpeedsettable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 4),
    _PhySerIfIsSpeedsettable_Type()
)
phySerIfIsSpeedsettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfIsSpeedsettable.setStatus("mandatory")


class _PhySerIfPortSpeed_Type(Integer32):
    """Custom type phySerIfPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200,
              24000,
              32000,
              48000,
              64000,
              256000,
              512000,
              1024000,
              2048000)
        )
    )
    namedValues = NamedValues(
        *(("b1024000", 1024000),
          ("b1200", 1200),
          ("b19200", 19200),
          ("b2048000", 2048000),
          ("b2400", 2400),
          ("b24000", 24000),
          ("b256000", 256000),
          ("b32000", 32000),
          ("b4800", 4800),
          ("b48000", 48000),
          ("b512000", 512000),
          ("b64000", 64000),
          ("b9600", 9600))
    )


_PhySerIfPortSpeed_Type.__name__ = "Integer32"
_PhySerIfPortSpeed_Object = MibTableColumn
phySerIfPortSpeed = _PhySerIfPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 5),
    _PhySerIfPortSpeed_Type()
)
phySerIfPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfPortSpeed.setStatus("mandatory")
_PhySerIfTransitDelay_Type = Integer32
_PhySerIfTransitDelay_Object = MibTableColumn
phySerIfTransitDelay = _PhySerIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 6),
    _PhySerIfTransitDelay_Type()
)
phySerIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfTransitDelay.setStatus("mandatory")


class _PhySerIfT1clockSource_Type(Integer32):
    """Custom type phySerIfT1clockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PhySerIfT1clockSource_Type.__name__ = "Integer32"
_PhySerIfT1clockSource_Object = MibTableColumn
phySerIfT1clockSource = _PhySerIfT1clockSource_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 7),
    _PhySerIfT1clockSource_Type()
)
phySerIfT1clockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfT1clockSource.setStatus("mandatory")


class _PhySerIfT1SlotLvalue_Type(Integer32):
    """Custom type phySerIfT1SlotLvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PhySerIfT1SlotLvalue_Type.__name__ = "Integer32"
_PhySerIfT1SlotLvalue_Object = MibTableColumn
phySerIfT1SlotLvalue = _PhySerIfT1SlotLvalue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 8),
    _PhySerIfT1SlotLvalue_Type()
)
phySerIfT1SlotLvalue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfT1SlotLvalue.setStatus("mandatory")


class _PhySerIfT1SlotHvalue_Type(Integer32):
    """Custom type phySerIfT1SlotHvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_PhySerIfT1SlotHvalue_Type.__name__ = "Integer32"
_PhySerIfT1SlotHvalue_Object = MibTableColumn
phySerIfT1SlotHvalue = _PhySerIfT1SlotHvalue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 9),
    _PhySerIfT1SlotHvalue_Type()
)
phySerIfT1SlotHvalue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfT1SlotHvalue.setStatus("mandatory")


class _PhySerIfT1dRatePerChan_Type(Integer32):
    """Custom type phySerIfT1dRatePerChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PhySerIfT1dRatePerChan_Type.__name__ = "Integer32"
_PhySerIfT1dRatePerChan_Object = MibTableColumn
phySerIfT1dRatePerChan = _PhySerIfT1dRatePerChan_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 10),
    _PhySerIfT1dRatePerChan_Type()
)
phySerIfT1dRatePerChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfT1dRatePerChan.setStatus("mandatory")


class _PhySerIfT1frameAndCode_Type(Integer32):
    """Custom type phySerIfT1frameAndCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PhySerIfT1frameAndCode_Type.__name__ = "Integer32"
_PhySerIfT1frameAndCode_Object = MibTableColumn
phySerIfT1frameAndCode = _PhySerIfT1frameAndCode_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 11),
    _PhySerIfT1frameAndCode_Type()
)
phySerIfT1frameAndCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfT1frameAndCode.setStatus("mandatory")


class _PhySerIfpartnerAddress_Type(OctetString):
    """Custom type phySerIfpartnerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PhySerIfpartnerAddress_Type.__name__ = "OctetString"
_PhySerIfpartnerAddress_Object = MibScalar
phySerIfpartnerAddress = _PhySerIfpartnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 4, 2, 1, 12),
    _PhySerIfpartnerAddress_Type()
)
phySerIfpartnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfpartnerAddress.setStatus("mandatory")
_Mlink_ObjectIdentity = ObjectIdentity
mlink = _Mlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5)
)
_MlinkNumber_Type = Integer32
_MlinkNumber_Object = MibScalar
mlinkNumber = _MlinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 1),
    _MlinkNumber_Type()
)
mlinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkNumber.setStatus("mandatory")
_MlinkTable_Object = MibTable
mlinkTable = _MlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    mlinkTable.setStatus("mandatory")
_MlinkEntry_Object = MibTableRow
mlinkEntry = _MlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1)
)
mlinkEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "mlinkIndex"),
)
if mibBuilder.loadTexts:
    mlinkEntry.setStatus("mandatory")
_MlinkIndex_Type = Integer32
_MlinkIndex_Object = MibTableColumn
mlinkIndex = _MlinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 1),
    _MlinkIndex_Type()
)
mlinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkIndex.setStatus("mandatory")


class _MlinkState_Type(Integer32):
    """Custom type mlinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MlinkState_Type.__name__ = "Integer32"
_MlinkState_Object = MibTableColumn
mlinkState = _MlinkState_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 2),
    _MlinkState_Type()
)
mlinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkState.setStatus("mandatory")
_MlinkSendSeq_Type = Integer32
_MlinkSendSeq_Object = MibTableColumn
mlinkSendSeq = _MlinkSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 3),
    _MlinkSendSeq_Type()
)
mlinkSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkSendSeq.setStatus("mandatory")
_MlinkRcvSeq_Type = Integer32
_MlinkRcvSeq_Object = MibTableColumn
mlinkRcvSeq = _MlinkRcvSeq_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 4),
    _MlinkRcvSeq_Type()
)
mlinkRcvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkRcvSeq.setStatus("mandatory")
_MlinkSendUpperEdge_Type = Integer32
_MlinkSendUpperEdge_Object = MibTableColumn
mlinkSendUpperEdge = _MlinkSendUpperEdge_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 5),
    _MlinkSendUpperEdge_Type()
)
mlinkSendUpperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkSendUpperEdge.setStatus("mandatory")
_MlinkRcvUpperEdge_Type = Integer32
_MlinkRcvUpperEdge_Object = MibTableColumn
mlinkRcvUpperEdge = _MlinkRcvUpperEdge_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 6),
    _MlinkRcvUpperEdge_Type()
)
mlinkRcvUpperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkRcvUpperEdge.setStatus("mandatory")
_MlinkFramesLost_Type = Counter32
_MlinkFramesLost_Object = MibTableColumn
mlinkFramesLost = _MlinkFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 7),
    _MlinkFramesLost_Type()
)
mlinkFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkFramesLost.setStatus("mandatory")
_DeletedMlinkFrames_Type = Counter32
_DeletedMlinkFrames_Object = MibTableColumn
deletedMlinkFrames = _DeletedMlinkFrames_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 8),
    _DeletedMlinkFrames_Type()
)
deletedMlinkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deletedMlinkFrames.setStatus("mandatory")
_ExpressQueueCurrentLength_Type = Integer32
_ExpressQueueCurrentLength_Object = MibTableColumn
expressQueueCurrentLength = _ExpressQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 9),
    _ExpressQueueCurrentLength_Type()
)
expressQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressQueueCurrentLength.setStatus("mandatory")
_ExpressQueueUpperLimit_Type = Integer32
_ExpressQueueUpperLimit_Object = MibTableColumn
expressQueueUpperLimit = _ExpressQueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 10),
    _ExpressQueueUpperLimit_Type()
)
expressQueueUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressQueueUpperLimit.setStatus("mandatory")
_HiPriQueueCurrentLength_Type = Integer32
_HiPriQueueCurrentLength_Object = MibTableColumn
hiPriQueueCurrentLength = _HiPriQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 11),
    _HiPriQueueCurrentLength_Type()
)
hiPriQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiPriQueueCurrentLength.setStatus("mandatory")
_HiPriQueueUpperLimit_Type = Integer32
_HiPriQueueUpperLimit_Object = MibTableColumn
hiPriQueueUpperLimit = _HiPriQueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 12),
    _HiPriQueueUpperLimit_Type()
)
hiPriQueueUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiPriQueueUpperLimit.setStatus("mandatory")
_LoPriQueueCurrentLength_Type = Integer32
_LoPriQueueCurrentLength_Object = MibTableColumn
loPriQueueCurrentLength = _LoPriQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 13),
    _LoPriQueueCurrentLength_Type()
)
loPriQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loPriQueueCurrentLength.setStatus("mandatory")
_LoPriQueueUpperLimit_Type = Integer32
_LoPriQueueUpperLimit_Object = MibTableColumn
loPriQueueUpperLimit = _LoPriQueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 2, 1, 14),
    _LoPriQueueUpperLimit_Type()
)
loPriQueueUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loPriQueueUpperLimit.setStatus("mandatory")
_MlinkWindow_Type = Integer32
_MlinkWindow_Object = MibScalar
mlinkWindow = _MlinkWindow_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 3),
    _MlinkWindow_Type()
)
mlinkWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlinkWindow.setStatus("mandatory")
_MlinkRxTimeout_Type = Integer32
_MlinkRxTimeout_Object = MibScalar
mlinkRxTimeout = _MlinkRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 5, 4),
    _MlinkRxTimeout_Type()
)
mlinkRxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlinkRxTimeout.setStatus("mandatory")
_Lan_ObjectIdentity = ObjectIdentity
lan = _Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 6)
)


class _LanInterfaceType_Type(Integer32):
    """Custom type lanInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LanInterfaceType_Type.__name__ = "Integer32"
_LanInterfaceType_Object = MibScalar
lanInterfaceType = _LanInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 6, 1),
    _LanInterfaceType_Type()
)
lanInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanInterfaceType.setStatus("mandatory")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7)
)
_PortNumber_Type = Integer32
_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("mandatory")
_BridgeStatsTable_Object = MibTable
bridgeStatsTable = _BridgeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    bridgeStatsTable.setStatus("mandatory")
_BridgeStatsEntry_Object = MibTableRow
bridgeStatsEntry = _BridgeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1)
)
bridgeStatsEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "bridgeStatsIndex"),
)
if mibBuilder.loadTexts:
    bridgeStatsEntry.setStatus("mandatory")
_BridgeStatsIndex_Type = Integer32
_BridgeStatsIndex_Object = MibTableColumn
bridgeStatsIndex = _BridgeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 1),
    _BridgeStatsIndex_Type()
)
bridgeStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsIndex.setStatus("mandatory")
_AverageForwarded_Type = Counter32
_AverageForwarded_Object = MibTableColumn
averageForwarded = _AverageForwarded_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 2),
    _AverageForwarded_Type()
)
averageForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageForwarded.setStatus("mandatory")
_MaxForwarded_Type = Counter32
_MaxForwarded_Object = MibTableColumn
maxForwarded = _MaxForwarded_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 3),
    _MaxForwarded_Type()
)
maxForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxForwarded.setStatus("mandatory")
_AverageRejected_Type = Counter32
_AverageRejected_Object = MibTableColumn
averageRejected = _AverageRejected_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 4),
    _AverageRejected_Type()
)
averageRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageRejected.setStatus("mandatory")
_MaxRejected_Type = Counter32
_MaxRejected_Object = MibTableColumn
maxRejected = _MaxRejected_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 5),
    _MaxRejected_Type()
)
maxRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRejected.setStatus("mandatory")
_LanAccepts_Type = Counter32
_LanAccepts_Object = MibTableColumn
lanAccepts = _LanAccepts_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 6),
    _LanAccepts_Type()
)
lanAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanAccepts.setStatus("mandatory")
_LanRejects_Type = Counter32
_LanRejects_Object = MibTableColumn
lanRejects = _LanRejects_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 7),
    _LanRejects_Type()
)
lanRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanRejects.setStatus("mandatory")
_DeletedLanFrames_Type = Counter32
_DeletedLanFrames_Object = MibScalar
deletedLanFrames = _DeletedLanFrames_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 2, 1, 8),
    _DeletedLanFrames_Type()
)
deletedLanFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deletedLanFrames.setStatus("mandatory")
_StpTable_Object = MibTable
stpTable = _StpTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    stpTable.setStatus("mandatory")
_StpEntry_Object = MibTableRow
stpEntry = _StpEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1)
)
stpEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "stpIndex"),
)
if mibBuilder.loadTexts:
    stpEntry.setStatus("mandatory")
_StpIndex_Type = Integer32
_StpIndex_Object = MibTableColumn
stpIndex = _StpIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 1),
    _StpIndex_Type()
)
stpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpIndex.setStatus("mandatory")


class _PathCostMode_Type(Integer32):
    """Custom type pathCostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PathCostMode_Type.__name__ = "Integer32"
_PathCostMode_Object = MibTableColumn
pathCostMode = _PathCostMode_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 2),
    _PathCostMode_Type()
)
pathCostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathCostMode.setStatus("mandatory")
_PathCostAutoValue_Type = Integer32
_PathCostAutoValue_Object = MibTableColumn
pathCostAutoValue = _PathCostAutoValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 3),
    _PathCostAutoValue_Type()
)
pathCostAutoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pathCostAutoValue.setStatus("mandatory")


class _PathCostManualValue_Type(Integer32):
    """Custom type pathCostManualValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PathCostManualValue_Type.__name__ = "Integer32"
_PathCostManualValue_Object = MibScalar
pathCostManualValue = _PathCostManualValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 4),
    _PathCostManualValue_Type()
)
pathCostManualValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathCostManualValue.setStatus("mandatory")
_PortSpatState_Type = Integer32
_PortSpatState_Object = MibTableColumn
portSpatState = _PortSpatState_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 5),
    _PortSpatState_Type()
)
portSpatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpatState.setStatus("mandatory")


class _PortPriorityMode_Type(Integer32):
    """Custom type portPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PortPriorityMode_Type.__name__ = "Integer32"
_PortPriorityMode_Object = MibTableColumn
portPriorityMode = _PortPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 6),
    _PortPriorityMode_Type()
)
portPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriorityMode.setStatus("mandatory")
_PortPriorityAutoValue_Type = Integer32
_PortPriorityAutoValue_Object = MibTableColumn
portPriorityAutoValue = _PortPriorityAutoValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 7),
    _PortPriorityAutoValue_Type()
)
portPriorityAutoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPriorityAutoValue.setStatus("mandatory")


class _PortPriorityManualValue_Type(Integer32):
    """Custom type portPriorityManualValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortPriorityManualValue_Type.__name__ = "Integer32"
_PortPriorityManualValue_Object = MibTableColumn
portPriorityManualValue = _PortPriorityManualValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 3, 1, 8),
    _PortPriorityManualValue_Type()
)
portPriorityManualValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriorityManualValue.setStatus("mandatory")


class _SpanningTree_Type(Integer32):
    """Custom type spanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SpanningTree_Type.__name__ = "Integer32"
_SpanningTree_Object = MibScalar
spanningTree = _SpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 4),
    _SpanningTree_Type()
)
spanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTree.setStatus("mandatory")


class _SpatPriority_Type(Integer32):
    """Custom type spatPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SpatPriority_Type.__name__ = "Integer32"
_SpatPriority_Object = MibScalar
spatPriority = _SpatPriority_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 5),
    _SpatPriority_Type()
)
spatPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spatPriority.setStatus("mandatory")


class _SpatHelloTimer_Type(Integer32):
    """Custom type spatHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SpatHelloTimer_Type.__name__ = "Integer32"
_SpatHelloTimer_Object = MibScalar
spatHelloTimer = _SpatHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 6),
    _SpatHelloTimer_Type()
)
spatHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spatHelloTimer.setStatus("mandatory")


class _SpatResetTimer_Type(Integer32):
    """Custom type spatResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_SpatResetTimer_Type.__name__ = "Integer32"
_SpatResetTimer_Object = MibScalar
spatResetTimer = _SpatResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 7),
    _SpatResetTimer_Type()
)
spatResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spatResetTimer.setStatus("mandatory")


class _SpatVersion_Type(Integer32):
    """Custom type spatVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("revision8", 8),
          ("revisionC", 3))
    )


_SpatVersion_Type.__name__ = "Integer32"
_SpatVersion_Object = MibScalar
spatVersion = _SpatVersion_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 8),
    _SpatVersion_Type()
)
spatVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spatVersion.setStatus("mandatory")


class _SpanningMcastAddr_Type(OctetString):
    """Custom type spanningMcastAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SpanningMcastAddr_Type.__name__ = "OctetString"
_SpanningMcastAddr_Object = MibScalar
spanningMcastAddr = _SpanningMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 9),
    _SpanningMcastAddr_Type()
)
spanningMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningMcastAddr.setStatus("mandatory")


class _OperatingMode_Type(Integer32):
    """Custom type operatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_OperatingMode_Type.__name__ = "Integer32"
_OperatingMode_Object = MibScalar
operatingMode = _OperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 10),
    _OperatingMode_Type()
)
operatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatingMode.setStatus("mandatory")


class _PreconfSourceFilter_Type(Integer32):
    """Custom type preconfSourceFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PreconfSourceFilter_Type.__name__ = "Integer32"
_PreconfSourceFilter_Object = MibScalar
preconfSourceFilter = _PreconfSourceFilter_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 11),
    _PreconfSourceFilter_Type()
)
preconfSourceFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preconfSourceFilter.setStatus("mandatory")


class _TypeFilter_Type(Integer32):
    """Custom type typeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TypeFilter_Type.__name__ = "Integer32"
_TypeFilter_Object = MibScalar
typeFilter = _TypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 12),
    _TypeFilter_Type()
)
typeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    typeFilter.setStatus("mandatory")


class _TypePrioritisation_Type(Integer32):
    """Custom type typePrioritisation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TypePrioritisation_Type.__name__ = "Integer32"
_TypePrioritisation_Object = MibScalar
typePrioritisation = _TypePrioritisation_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 13),
    _TypePrioritisation_Type()
)
typePrioritisation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    typePrioritisation.setStatus("mandatory")


class _DynamicLearningInLM_Type(Integer32):
    """Custom type dynamicLearningInLM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DynamicLearningInLM_Type.__name__ = "Integer32"
_DynamicLearningInLM_Object = MibScalar
dynamicLearningInLM = _DynamicLearningInLM_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 14),
    _DynamicLearningInLM_Type()
)
dynamicLearningInLM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicLearningInLM.setStatus("mandatory")


class _ForgetAddressTimer_Type(Integer32):
    """Custom type forgetAddressTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 1000),
    )


_ForgetAddressTimer_Type.__name__ = "Integer32"
_ForgetAddressTimer_Object = MibScalar
forgetAddressTimer = _ForgetAddressTimer_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 15),
    _ForgetAddressTimer_Type()
)
forgetAddressTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forgetAddressTimer.setStatus("mandatory")


class _DeleteAddressTimer_Type(Integer32):
    """Custom type deleteAddressTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_DeleteAddressTimer_Type.__name__ = "Integer32"
_DeleteAddressTimer_Object = MibScalar
deleteAddressTimer = _DeleteAddressTimer_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 16),
    _DeleteAddressTimer_Type()
)
deleteAddressTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deleteAddressTimer.setStatus("mandatory")


class _MulticastDisposition_Type(Integer32):
    """Custom type multicastDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MulticastDisposition_Type.__name__ = "Integer32"
_MulticastDisposition_Object = MibScalar
multicastDisposition = _MulticastDisposition_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 17),
    _MulticastDisposition_Type()
)
multicastDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastDisposition.setStatus("mandatory")


class _FilterMatches_Type(Integer32):
    """Custom type filterMatches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FilterMatches_Type.__name__ = "Integer32"
_FilterMatches_Object = MibScalar
filterMatches = _FilterMatches_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 18),
    _FilterMatches_Type()
)
filterMatches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterMatches.setStatus("mandatory")


class _IeeeFormatFilter_Type(Integer32):
    """Custom type ieeeFormatFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IeeeFormatFilter_Type.__name__ = "Integer32"
_IeeeFormatFilter_Object = MibScalar
ieeeFormatFilter = _IeeeFormatFilter_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 19),
    _IeeeFormatFilter_Type()
)
ieeeFormatFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieeeFormatFilter.setStatus("mandatory")


class _PriorityMatches_Type(Integer32):
    """Custom type priorityMatches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PriorityMatches_Type.__name__ = "Integer32"
_PriorityMatches_Object = MibScalar
priorityMatches = _PriorityMatches_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 20),
    _PriorityMatches_Type()
)
priorityMatches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityMatches.setStatus("mandatory")


class _IeeeFormatPriority_Type(Integer32):
    """Custom type ieeeFormatPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IeeeFormatPriority_Type.__name__ = "Integer32"
_IeeeFormatPriority_Object = MibScalar
ieeeFormatPriority = _IeeeFormatPriority_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 21),
    _IeeeFormatPriority_Type()
)
ieeeFormatPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieeeFormatPriority.setStatus("mandatory")
_AveragePeriod_Type = Integer32
_AveragePeriod_Object = MibScalar
averagePeriod = _AveragePeriod_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 22),
    _AveragePeriod_Type()
)
averagePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averagePeriod.setStatus("mandatory")


class _Triangulation_Type(Integer32):
    """Custom type triangulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Triangulation_Type.__name__ = "Integer32"
_Triangulation_Object = MibScalar
triangulation = _Triangulation_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 23),
    _Triangulation_Type()
)
triangulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    triangulation.setStatus("mandatory")


class _AdaptiveRouting_Type(Integer32):
    """Custom type adaptiveRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AdaptiveRouting_Type.__name__ = "Integer32"
_AdaptiveRouting_Object = MibScalar
adaptiveRouting = _AdaptiveRouting_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 24),
    _AdaptiveRouting_Type()
)
adaptiveRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveRouting.setStatus("mandatory")


class _AdaptiveMcastAddr_Type(OctetString):
    """Custom type adaptiveMcastAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AdaptiveMcastAddr_Type.__name__ = "OctetString"
_AdaptiveMcastAddr_Object = MibScalar
adaptiveMcastAddr = _AdaptiveMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 25),
    _AdaptiveMcastAddr_Type()
)
adaptiveMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveMcastAddr.setStatus("mandatory")
_ArAddressInfo_ObjectIdentity = ObjectIdentity
arAddressInfo = _ArAddressInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 26)
)
_StandbyRemote_Type = Integer32
_StandbyRemote_Object = MibScalar
standbyRemote = _StandbyRemote_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 26, 1),
    _StandbyRemote_Type()
)
standbyRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyRemote.setStatus("mandatory")
_StandbyLocal_Type = Integer32
_StandbyLocal_Object = MibScalar
standbyLocal = _StandbyLocal_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 26, 2),
    _StandbyLocal_Type()
)
standbyLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyLocal.setStatus("mandatory")
_ActiveRemote_Type = Integer32
_ActiveRemote_Object = MibScalar
activeRemote = _ActiveRemote_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 26, 3),
    _ActiveRemote_Type()
)
activeRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeRemote.setStatus("mandatory")
_ActiveLocal_Type = Integer32
_ActiveLocal_Object = MibScalar
activeLocal = _ActiveLocal_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 26, 4),
    _ActiveLocal_Type()
)
activeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeLocal.setStatus("mandatory")
_MaxSerialLoading_Type = Integer32
_MaxSerialLoading_Object = MibScalar
maxSerialLoading = _MaxSerialLoading_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 27),
    _MaxSerialLoading_Type()
)
maxSerialLoading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxSerialLoading.setStatus("mandatory")
_SerialLoadPeriod_Type = Integer32
_SerialLoadPeriod_Object = MibScalar
serialLoadPeriod = _SerialLoadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 28),
    _SerialLoadPeriod_Type()
)
serialLoadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialLoadPeriod.setStatus("mandatory")
_SerialLoading_Type = Integer32
_SerialLoading_Object = MibScalar
serialLoading = _SerialLoading_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 29),
    _SerialLoading_Type()
)
serialLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialLoading.setStatus("mandatory")
_FilteringDataBaseTable_ObjectIdentity = ObjectIdentity
filteringDataBaseTable = _FilteringDataBaseTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30)
)
_FilteringDbTable_Object = MibTable
filteringDbTable = _FilteringDbTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 1)
)
if mibBuilder.loadTexts:
    filteringDbTable.setStatus("mandatory")
_FilteringDbEntry_Object = MibTable
filteringDbEntry = _FilteringDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 1, 1)
)
if mibBuilder.loadTexts:
    filteringDbEntry.setStatus("mandatory")
_FilteringDbMacAddress_Type = OctetString
_FilteringDbMacAddress_Object = MibTableColumn
filteringDbMacAddress = _FilteringDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 1, 1, 1),
    _FilteringDbMacAddress_Type()
)
filteringDbMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbMacAddress.setStatus("mandatory")
_FilteringDbDisposition_Type = Integer32
_FilteringDbDisposition_Object = MibTableColumn
filteringDbDisposition = _FilteringDbDisposition_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 1, 1, 2),
    _FilteringDbDisposition_Type()
)
filteringDbDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbDisposition.setStatus("mandatory")
_FilteringDbStatus_Type = Integer32
_FilteringDbStatus_Object = MibTableColumn
filteringDbStatus = _FilteringDbStatus_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 1, 1, 3),
    _FilteringDbStatus_Type()
)
filteringDbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbStatus.setStatus("mandatory")
_FilteringDbType_Type = Integer32
_FilteringDbType_Object = MibTableColumn
filteringDbType = _FilteringDbType_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 1, 1, 4),
    _FilteringDbType_Type()
)
filteringDbType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbType.setStatus("mandatory")
_FilteringDbAction_Type = Integer32
_FilteringDbAction_Object = MibScalar
filteringDbAction = _FilteringDbAction_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 2),
    _FilteringDbAction_Type()
)
filteringDbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbAction.setStatus("mandatory")
_FilteringDbPage_ObjectIdentity = ObjectIdentity
filteringDbPage = _FilteringDbPage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 3)
)


class _FilteringDbPageValue_Type(OctetString):
    """Custom type filteringDbPageValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 640),
    )


_FilteringDbPageValue_Type.__name__ = "OctetString"
_FilteringDbPageValue_Object = MibScalar
filteringDbPageValue = _FilteringDbPageValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 30, 3, 1),
    _FilteringDbPageValue_Type()
)
filteringDbPageValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbPageValue.setStatus("mandatory")
_PriorityTable_ObjectIdentity = ObjectIdentity
priorityTable = _PriorityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 31)
)
_PrioritySubTable_Object = MibTable
prioritySubTable = _PrioritySubTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 31, 1)
)
if mibBuilder.loadTexts:
    prioritySubTable.setStatus("mandatory")
_PriorityTableEntry_Object = MibTableRow
priorityTableEntry = _PriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 31, 1, 1)
)
priorityTableEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "priorityTableEntryType"),
)
if mibBuilder.loadTexts:
    priorityTableEntry.setStatus("mandatory")
_PriorityTableEntryValue_Type = Integer32
_PriorityTableEntryValue_Object = MibTableColumn
priorityTableEntryValue = _PriorityTableEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 31, 1, 1, 1),
    _PriorityTableEntryValue_Type()
)
priorityTableEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityTableEntryValue.setStatus("mandatory")
_PriorityTableEntryType_Type = Integer32
_PriorityTableEntryType_Object = MibTableColumn
priorityTableEntryType = _PriorityTableEntryType_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 31, 1, 1, 2),
    _PriorityTableEntryType_Type()
)
priorityTableEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityTableEntryType.setStatus("mandatory")
_PriorityTableAction_Type = Integer32
_PriorityTableAction_Object = MibScalar
priorityTableAction = _PriorityTableAction_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 31, 2),
    _PriorityTableAction_Type()
)
priorityTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityTableAction.setStatus("mandatory")


class _PriorityPage_Type(OctetString):
    """Custom type priorityPage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PriorityPage_Type.__name__ = "OctetString"
_PriorityPage_Object = MibScalar
priorityPage = _PriorityPage_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 31, 3),
    _PriorityPage_Type()
)
priorityPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityPage.setStatus("mandatory")
_FilterTable_ObjectIdentity = ObjectIdentity
filterTable = _FilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 32)
)
_FilterSubTable_Object = MibTable
filterSubTable = _FilterSubTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 32, 1)
)
if mibBuilder.loadTexts:
    filterSubTable.setStatus("mandatory")
_FilterTableEntry_Object = MibTable
filterTableEntry = _FilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 32, 1, 1)
)
if mibBuilder.loadTexts:
    filterTableEntry.setStatus("mandatory")
_FilterTableEntryValue_Type = Integer32
_FilterTableEntryValue_Object = MibTableColumn
filterTableEntryValue = _FilterTableEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 32, 1, 1, 1),
    _FilterTableEntryValue_Type()
)
filterTableEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTableEntryValue.setStatus("mandatory")
_FilterTableEntryType_Type = Integer32
_FilterTableEntryType_Object = MibTableColumn
filterTableEntryType = _FilterTableEntryType_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 32, 1, 1, 2),
    _FilterTableEntryType_Type()
)
filterTableEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTableEntryType.setStatus("mandatory")
_FilterTableAction_Type = Integer32
_FilterTableAction_Object = MibScalar
filterTableAction = _FilterTableAction_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 32, 2),
    _FilterTableAction_Type()
)
filterTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTableAction.setStatus("mandatory")


class _FilterPage_Type(OctetString):
    """Custom type filterPage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FilterPage_Type.__name__ = "OctetString"
_FilterPage_Object = MibScalar
filterPage = _FilterPage_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 7, 32, 3),
    _FilterPage_Type()
)
filterPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPage.setStatus("mandatory")
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8)
)
_P4942_ObjectIdentity = ObjectIdentity
p4942 = _P4942_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 1)
)
_P2244m2_ObjectIdentity = ObjectIdentity
p2244m2 = _P2244m2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 2)
)
_P2265_ObjectIdentity = ObjectIdentity
p2265 = _P2265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 3)
)
_P4660_ObjectIdentity = ObjectIdentity
p4660 = _P4660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 4)
)
_P4820_ObjectIdentity = ObjectIdentity
p4820 = _P4820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 5)
)
_P4880_ObjectIdentity = ObjectIdentity
p4880 = _P4880_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 6)
)
_P4850_ObjectIdentity = ObjectIdentity
p4850 = _P4850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 7)
)
_P4760_ObjectIdentity = ObjectIdentity
p4760 = _P4760_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 8)
)
_P4941_ObjectIdentity = ObjectIdentity
p4941 = _P4941_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 8, 9)
)
_Br12_ObjectIdentity = ObjectIdentity
br12 = _Br12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 9)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10)
)
_IpRSTable_Object = MibTable
ipRSTable = _IpRSTable_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ipRSTable.setStatus("mandatory")
_IpRSEntry_Object = MibTableRow
ipRSEntry = _IpRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1)
)
ipRSEntry.setIndexNames(
    (0, "ISOVIEW-MIB", "ipRSIndex"),
)
if mibBuilder.loadTexts:
    ipRSEntry.setStatus("mandatory")
_IpRSIndex_Type = Integer32
_IpRSIndex_Object = MibTableColumn
ipRSIndex = _IpRSIndex_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1, 1),
    _IpRSIndex_Type()
)
ipRSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRSIndex.setStatus("mandatory")
_GwProtocol_Type = Integer32
_GwProtocol_Object = MibTableColumn
gwProtocol = _GwProtocol_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1, 2),
    _GwProtocol_Type()
)
gwProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwProtocol.setStatus("mandatory")
_IfStatus_Type = Integer32
_IfStatus_Object = MibTableColumn
ifStatus = _IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1, 3),
    _IfStatus_Type()
)
ifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStatus.setStatus("mandatory")
_ReceivedTotal_Type = Counter32
_ReceivedTotal_Object = MibTableColumn
receivedTotal = _ReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1, 4),
    _ReceivedTotal_Type()
)
receivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedTotal.setStatus("mandatory")
_TransmittedTotal_Type = Counter32
_TransmittedTotal_Object = MibTableColumn
transmittedTotal = _TransmittedTotal_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1, 5),
    _TransmittedTotal_Type()
)
transmittedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmittedTotal.setStatus("mandatory")
_OutDiscardsTotal_Type = Counter32
_OutDiscardsTotal_Object = MibTableColumn
outDiscardsTotal = _OutDiscardsTotal_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1, 6),
    _OutDiscardsTotal_Type()
)
outDiscardsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outDiscardsTotal.setStatus("mandatory")
_NoRouteTotal_Type = Counter32
_NoRouteTotal_Object = MibTableColumn
noRouteTotal = _NoRouteTotal_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 1, 1, 7),
    _NoRouteTotal_Type()
)
noRouteTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noRouteTotal.setStatus("mandatory")
_IcmpRSTable_ObjectIdentity = ObjectIdentity
icmpRSTable = _IcmpRSTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2)
)


class _DestUnreachLastRx_Type(OctetString):
    """Custom type destUnreachLastRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_DestUnreachLastRx_Type.__name__ = "OctetString"
_DestUnreachLastRx_Object = MibScalar
destUnreachLastRx = _DestUnreachLastRx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 1),
    _DestUnreachLastRx_Type()
)
destUnreachLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destUnreachLastRx.setStatus("mandatory")


class _DestUnreachLastTx_Type(OctetString):
    """Custom type destUnreachLastTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_DestUnreachLastTx_Type.__name__ = "OctetString"
_DestUnreachLastTx_Object = MibScalar
destUnreachLastTx = _DestUnreachLastTx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 2),
    _DestUnreachLastTx_Type()
)
destUnreachLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destUnreachLastTx.setStatus("mandatory")


class _SourceQuenchLastRx_Type(OctetString):
    """Custom type sourceQuenchLastRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_SourceQuenchLastRx_Type.__name__ = "OctetString"
_SourceQuenchLastRx_Object = MibScalar
sourceQuenchLastRx = _SourceQuenchLastRx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 3),
    _SourceQuenchLastRx_Type()
)
sourceQuenchLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceQuenchLastRx.setStatus("mandatory")


class _SourceQuenchLastTx_Type(OctetString):
    """Custom type sourceQuenchLastTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_SourceQuenchLastTx_Type.__name__ = "OctetString"
_SourceQuenchLastTx_Object = MibScalar
sourceQuenchLastTx = _SourceQuenchLastTx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 4),
    _SourceQuenchLastTx_Type()
)
sourceQuenchLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceQuenchLastTx.setStatus("mandatory")


class _RedirectsLastRx_Type(OctetString):
    """Custom type redirectsLastRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_RedirectsLastRx_Type.__name__ = "OctetString"
_RedirectsLastRx_Object = MibScalar
redirectsLastRx = _RedirectsLastRx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 5),
    _RedirectsLastRx_Type()
)
redirectsLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectsLastRx.setStatus("mandatory")


class _RedirectsLastTx_Type(OctetString):
    """Custom type redirectsLastTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_RedirectsLastTx_Type.__name__ = "OctetString"
_RedirectsLastTx_Object = MibScalar
redirectsLastTx = _RedirectsLastTx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 6),
    _RedirectsLastTx_Type()
)
redirectsLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectsLastTx.setStatus("mandatory")


class _EchoRequestsLastRx_Type(OctetString):
    """Custom type echoRequestsLastRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_EchoRequestsLastRx_Type.__name__ = "OctetString"
_EchoRequestsLastRx_Object = MibScalar
echoRequestsLastRx = _EchoRequestsLastRx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 7),
    _EchoRequestsLastRx_Type()
)
echoRequestsLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoRequestsLastRx.setStatus("mandatory")


class _EchoRequestsLastTx_Type(OctetString):
    """Custom type echoRequestsLastTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_EchoRequestsLastTx_Type.__name__ = "OctetString"
_EchoRequestsLastTx_Object = MibScalar
echoRequestsLastTx = _EchoRequestsLastTx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 8),
    _EchoRequestsLastTx_Type()
)
echoRequestsLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoRequestsLastTx.setStatus("mandatory")


class _TimeExceededLastRx_Type(OctetString):
    """Custom type timeExceededLastRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_TimeExceededLastRx_Type.__name__ = "OctetString"
_TimeExceededLastRx_Object = MibScalar
timeExceededLastRx = _TimeExceededLastRx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 9),
    _TimeExceededLastRx_Type()
)
timeExceededLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeExceededLastRx.setStatus("mandatory")


class _TimeExceededLastTx_Type(OctetString):
    """Custom type timeExceededLastTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_TimeExceededLastTx_Type.__name__ = "OctetString"
_TimeExceededLastTx_Object = MibScalar
timeExceededLastTx = _TimeExceededLastTx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 10),
    _TimeExceededLastTx_Type()
)
timeExceededLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeExceededLastTx.setStatus("mandatory")


class _ParamProbLastRx_Type(OctetString):
    """Custom type paramProbLastRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ParamProbLastRx_Type.__name__ = "OctetString"
_ParamProbLastRx_Object = MibScalar
paramProbLastRx = _ParamProbLastRx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 11),
    _ParamProbLastRx_Type()
)
paramProbLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramProbLastRx.setStatus("mandatory")


class _ParamProbLastTx_Type(OctetString):
    """Custom type paramProbLastTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ParamProbLastTx_Type.__name__ = "OctetString"
_ParamProbLastTx_Object = MibScalar
paramProbLastTx = _ParamProbLastTx_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 2, 12),
    _ParamProbLastTx_Type()
)
paramProbLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramProbLastTx.setStatus("mandatory")
_IpRouting_Type = Integer32
_IpRouting_Object = MibScalar
ipRouting = _IpRouting_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 10, 3),
    _IpRouting_Type()
)
ipRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouting.setStatus("mandatory")
_Boot_ObjectIdentity = ObjectIdentity
boot = _Boot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11)
)


class _BootpRetryCount_Type(Integer32):
    """Custom type bootpRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BootpRetryCount_Type.__name__ = "Integer32"
_BootpRetryCount_Object = MibScalar
bootpRetryCount = _BootpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 1),
    _BootpRetryCount_Type()
)
bootpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpRetryCount.setStatus("optional")


class _DownloadRetryCount_Type(Integer32):
    """Custom type downloadRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DownloadRetryCount_Type.__name__ = "Integer32"
_DownloadRetryCount_Object = MibScalar
downloadRetryCount = _DownloadRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 2),
    _DownloadRetryCount_Type()
)
downloadRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadRetryCount.setStatus("optional")


class _DownloadFilename_Type(OctetString):
    """Custom type downloadFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DownloadFilename_Type.__name__ = "OctetString"
_DownloadFilename_Object = MibScalar
downloadFilename = _DownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 3),
    _DownloadFilename_Type()
)
downloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFilename.setStatus("optional")
_BootserverIpAddress_Type = IpAddress
_BootserverIpAddress_Object = MibScalar
bootserverIpAddress = _BootserverIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 4),
    _BootserverIpAddress_Type()
)
bootserverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootserverIpAddress.setStatus("optional")
_LoadserverIpAddress_Type = IpAddress
_LoadserverIpAddress_Object = MibScalar
loadserverIpAddress = _LoadserverIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 5),
    _LoadserverIpAddress_Type()
)
loadserverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadserverIpAddress.setStatus("optional")
_UniqueBroadcastAddress_Type = IpAddress
_UniqueBroadcastAddress_Object = MibScalar
uniqueBroadcastAddress = _UniqueBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 6),
    _UniqueBroadcastAddress_Type()
)
uniqueBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniqueBroadcastAddress.setStatus("optional")


class _TftpRetryCount_Type(Integer32):
    """Custom type tftpRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TftpRetryCount_Type.__name__ = "Integer32"
_TftpRetryCount_Object = MibScalar
tftpRetryCount = _TftpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 7),
    _TftpRetryCount_Type()
)
tftpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRetryCount.setStatus("optional")


class _TftpRetryPeriod_Type(Integer32):
    """Custom type tftpRetryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TftpRetryPeriod_Type.__name__ = "Integer32"
_TftpRetryPeriod_Object = MibScalar
tftpRetryPeriod = _TftpRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 8),
    _TftpRetryPeriod_Type()
)
tftpRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRetryPeriod.setStatus("optional")
_InitiateBootpDll_Type = Integer32
_InitiateBootpDll_Object = MibScalar
initiateBootpDll = _InitiateBootpDll_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 11, 9),
    _InitiateBootpDll_Type()
)
initiateBootpDll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initiateBootpDll.setStatus("optional")
_Boothelper_ObjectIdentity = ObjectIdentity
boothelper = _Boothelper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 12)
)
_BoothelperEnabled_Type = Integer32
_BoothelperEnabled_Object = MibScalar
boothelperEnabled = _BoothelperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 12, 1),
    _BoothelperEnabled_Type()
)
boothelperEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boothelperEnabled.setStatus("optional")


class _BoothelperHopsLimit_Type(Integer32):
    """Custom type boothelperHopsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BoothelperHopsLimit_Type.__name__ = "Integer32"
_BoothelperHopsLimit_Object = MibScalar
boothelperHopsLimit = _BoothelperHopsLimit_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 12, 2),
    _BoothelperHopsLimit_Type()
)
boothelperHopsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boothelperHopsLimit.setStatus("optional")
_BoothelperForwardingAddress_Type = IpAddress
_BoothelperForwardingAddress_Object = MibScalar
boothelperForwardingAddress = _BoothelperForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 170, 1, 1, 1, 12, 3),
    _BoothelperForwardingAddress_Type()
)
boothelperForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boothelperForwardingAddress.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISOVIEW-MIB",
    **{"bitec": bitec,
       "bdn": bdn,
       "third-party": third_party,
       "retix": retix,
       "station": station,
       "stationTime": stationTime,
       "stationResetCounter": stationResetCounter,
       "freeBufferCount": freeBufferCount,
       "freeHeaderCount": freeHeaderCount,
       "physBlkSize": physBlkSize,
       "newPhysBlkSize": newPhysBlkSize,
       "resetStation": resetStation,
       "initStation": initStation,
       "resetStats": resetStats,
       "processorLoading": processorLoading,
       "trapDestinationTable": trapDestinationTable,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestEntryIpAddr": trapDestEntryIpAddr,
       "trapDestEntryCommunityName": trapDestEntryCommunityName,
       "trapDestEntryType": trapDestEntryType,
       "trapDestAction": trapDestAction,
       "trapDestPage": trapDestPage,
       "passWord": passWord,
       "snmpAccessPolicyObject": snmpAccessPolicyObject,
       "snmpAccessPolicyTable": snmpAccessPolicyTable,
       "snmpAccessPolicyEntry": snmpAccessPolicyEntry,
       "accessPolicyIndex": accessPolicyIndex,
       "communityName": communityName,
       "accessMode": accessMode,
       "snmpAccessPolicyType": snmpAccessPolicyType,
       "snmpAccessPolicyAction": snmpAccessPolicyAction,
       "snmpAccessPolicyPage": snmpAccessPolicyPage,
       "authenticationTrapStatus": authenticationTrapStatus,
       "serialTxQueueSize": serialTxQueueSize,
       "internalQueueCurrentLength": internalQueueCurrentLength,
       "queueUpperLimit": queueUpperLimit,
       "lanQueueSize": lanQueueSize,
       "lapb": lapb,
       "lapbNumber": lapbNumber,
       "lapbTable": lapbTable,
       "lapbEntry": lapbEntry,
       "lapbIndex": lapbIndex,
       "lapbModeT1": lapbModeT1,
       "lapbAutoT1value": lapbAutoT1value,
       "lapbManualT1value": lapbManualT1value,
       "lapbWindow": lapbWindow,
       "lapbPolarity": lapbPolarity,
       "lapbResetCount": lapbResetCount,
       "lapbSendFrameCount": lapbSendFrameCount,
       "lapbRcvFrameCount": lapbRcvFrameCount,
       "lapbSendOctetCount": lapbSendOctetCount,
       "lapbRcvOctetCount": lapbRcvOctetCount,
       "lapbAbortCount": lapbAbortCount,
       "lapbCrcErrorCount": lapbCrcErrorCount,
       "lapbState": lapbState,
       "lapbLastResetTime": lapbLastResetTime,
       "lapbLastResetReason": lapbLastResetReason,
       "lapbLinkReset": lapbLinkReset,
       "lapbRetryCount": lapbRetryCount,
       "ieee8023": ieee8023,
       "ieee8023Number": ieee8023Number,
       "ieee8023Table": ieee8023Table,
       "ieee8023Entry": ieee8023Entry,
       "ieee8023Index": ieee8023Index,
       "ieee8023FramesTransmittedOks": ieee8023FramesTransmittedOks,
       "ieee8023SingleCollisionFrames": ieee8023SingleCollisionFrames,
       "ieee8023MultipleCollisionFrames": ieee8023MultipleCollisionFrames,
       "ieee8023OctetsTransmittedOks": ieee8023OctetsTransmittedOks,
       "ieee8023DeferredTransmissions": ieee8023DeferredTransmissions,
       "ieee8023MulticastFramesTransmittedOks": ieee8023MulticastFramesTransmittedOks,
       "ieee8023BroadcastFramesTransmittedOks": ieee8023BroadcastFramesTransmittedOks,
       "ieee8023LateCollisions": ieee8023LateCollisions,
       "ieee8023ExcessiveCollisions": ieee8023ExcessiveCollisions,
       "ieee8023InternalMACTransmitErrors": ieee8023InternalMACTransmitErrors,
       "ieee8023CarrierSenseErrors": ieee8023CarrierSenseErrors,
       "ieee8023ExcessiveDeferrals": ieee8023ExcessiveDeferrals,
       "ieee8023FramesReceivedOks": ieee8023FramesReceivedOks,
       "ieee8023OctetsReceivedOks": ieee8023OctetsReceivedOks,
       "ieee8023MulticastFramesReceivedOks": ieee8023MulticastFramesReceivedOks,
       "ieee8023BroadcastFramesReceivedOks": ieee8023BroadcastFramesReceivedOks,
       "ieee8023FrameTooLongs": ieee8023FrameTooLongs,
       "ieee8023AlignmentErrors": ieee8023AlignmentErrors,
       "ieee8023FCSErrors": ieee8023FCSErrors,
       "ieee8023inRangeLengthErrors": ieee8023inRangeLengthErrors,
       "ieee8023outOfRangeLengthFields": ieee8023outOfRangeLengthFields,
       "ieee8023InternalMACReceiveErrors": ieee8023InternalMACReceiveErrors,
       "ieee8023InitializeMAC": ieee8023InitializeMAC,
       "ieee8023PromiscuousReceiveStatus": ieee8023PromiscuousReceiveStatus,
       "ieee8023MACSubLayerStatus": ieee8023MACSubLayerStatus,
       "ieee8023TransmitStatus": ieee8023TransmitStatus,
       "ieee8023MulticastReceiveStatus": ieee8023MulticastReceiveStatus,
       "ieee8023MACAddress": ieee8023MACAddress,
       "ieee8023SQETestErrors": ieee8023SQETestErrors,
       "ieee8023NewMACAddress": ieee8023NewMACAddress,
       "ieee8023NewMACAddressEntry": ieee8023NewMACAddressEntry,
       "ieee8023NewMACAddressIndex": ieee8023NewMACAddressIndex,
       "ieee8023NewMACAddressValue": ieee8023NewMACAddressValue,
       "phySerIf": phySerIf,
       "phySerIfNumber": phySerIfNumber,
       "phySerIfTable": phySerIfTable,
       "phySerIfEntry": phySerIfEntry,
       "phySerIfIndex": phySerIfIndex,
       "phySerIfInterfaceType": phySerIfInterfaceType,
       "phySerIfMeasuredSpeed": phySerIfMeasuredSpeed,
       "phySerIfIsSpeedsettable": phySerIfIsSpeedsettable,
       "phySerIfPortSpeed": phySerIfPortSpeed,
       "phySerIfTransitDelay": phySerIfTransitDelay,
       "phySerIfT1clockSource": phySerIfT1clockSource,
       "phySerIfT1SlotLvalue": phySerIfT1SlotLvalue,
       "phySerIfT1SlotHvalue": phySerIfT1SlotHvalue,
       "phySerIfT1dRatePerChan": phySerIfT1dRatePerChan,
       "phySerIfT1frameAndCode": phySerIfT1frameAndCode,
       "phySerIfpartnerAddress": phySerIfpartnerAddress,
       "mlink": mlink,
       "mlinkNumber": mlinkNumber,
       "mlinkTable": mlinkTable,
       "mlinkEntry": mlinkEntry,
       "mlinkIndex": mlinkIndex,
       "mlinkState": mlinkState,
       "mlinkSendSeq": mlinkSendSeq,
       "mlinkRcvSeq": mlinkRcvSeq,
       "mlinkSendUpperEdge": mlinkSendUpperEdge,
       "mlinkRcvUpperEdge": mlinkRcvUpperEdge,
       "mlinkFramesLost": mlinkFramesLost,
       "deletedMlinkFrames": deletedMlinkFrames,
       "expressQueueCurrentLength": expressQueueCurrentLength,
       "expressQueueUpperLimit": expressQueueUpperLimit,
       "hiPriQueueCurrentLength": hiPriQueueCurrentLength,
       "hiPriQueueUpperLimit": hiPriQueueUpperLimit,
       "loPriQueueCurrentLength": loPriQueueCurrentLength,
       "loPriQueueUpperLimit": loPriQueueUpperLimit,
       "mlinkWindow": mlinkWindow,
       "mlinkRxTimeout": mlinkRxTimeout,
       "lan": lan,
       "lanInterfaceType": lanInterfaceType,
       "bridge": bridge,
       "portNumber": portNumber,
       "bridgeStatsTable": bridgeStatsTable,
       "bridgeStatsEntry": bridgeStatsEntry,
       "bridgeStatsIndex": bridgeStatsIndex,
       "averageForwarded": averageForwarded,
       "maxForwarded": maxForwarded,
       "averageRejected": averageRejected,
       "maxRejected": maxRejected,
       "lanAccepts": lanAccepts,
       "lanRejects": lanRejects,
       "deletedLanFrames": deletedLanFrames,
       "stpTable": stpTable,
       "stpEntry": stpEntry,
       "stpIndex": stpIndex,
       "pathCostMode": pathCostMode,
       "pathCostAutoValue": pathCostAutoValue,
       "pathCostManualValue": pathCostManualValue,
       "portSpatState": portSpatState,
       "portPriorityMode": portPriorityMode,
       "portPriorityAutoValue": portPriorityAutoValue,
       "portPriorityManualValue": portPriorityManualValue,
       "spanningTree": spanningTree,
       "spatPriority": spatPriority,
       "spatHelloTimer": spatHelloTimer,
       "spatResetTimer": spatResetTimer,
       "spatVersion": spatVersion,
       "spanningMcastAddr": spanningMcastAddr,
       "operatingMode": operatingMode,
       "preconfSourceFilter": preconfSourceFilter,
       "typeFilter": typeFilter,
       "typePrioritisation": typePrioritisation,
       "dynamicLearningInLM": dynamicLearningInLM,
       "forgetAddressTimer": forgetAddressTimer,
       "deleteAddressTimer": deleteAddressTimer,
       "multicastDisposition": multicastDisposition,
       "filterMatches": filterMatches,
       "ieeeFormatFilter": ieeeFormatFilter,
       "priorityMatches": priorityMatches,
       "ieeeFormatPriority": ieeeFormatPriority,
       "averagePeriod": averagePeriod,
       "triangulation": triangulation,
       "adaptiveRouting": adaptiveRouting,
       "adaptiveMcastAddr": adaptiveMcastAddr,
       "arAddressInfo": arAddressInfo,
       "standbyRemote": standbyRemote,
       "standbyLocal": standbyLocal,
       "activeRemote": activeRemote,
       "activeLocal": activeLocal,
       "maxSerialLoading": maxSerialLoading,
       "serialLoadPeriod": serialLoadPeriod,
       "serialLoading": serialLoading,
       "filteringDataBaseTable": filteringDataBaseTable,
       "filteringDbTable": filteringDbTable,
       "filteringDbEntry": filteringDbEntry,
       "filteringDbMacAddress": filteringDbMacAddress,
       "filteringDbDisposition": filteringDbDisposition,
       "filteringDbStatus": filteringDbStatus,
       "filteringDbType": filteringDbType,
       "filteringDbAction": filteringDbAction,
       "filteringDbPage": filteringDbPage,
       "filteringDbPageValue": filteringDbPageValue,
       "priorityTable": priorityTable,
       "prioritySubTable": prioritySubTable,
       "priorityTableEntry": priorityTableEntry,
       "priorityTableEntryValue": priorityTableEntryValue,
       "priorityTableEntryType": priorityTableEntryType,
       "priorityTableAction": priorityTableAction,
       "priorityPage": priorityPage,
       "filterTable": filterTable,
       "filterSubTable": filterSubTable,
       "filterTableEntry": filterTableEntry,
       "filterTableEntryValue": filterTableEntryValue,
       "filterTableEntryType": filterTableEntryType,
       "filterTableAction": filterTableAction,
       "filterPage": filterPage,
       "product": product,
       "p4942": p4942,
       "p2244m2": p2244m2,
       "p2265": p2265,
       "p4660": p4660,
       "p4820": p4820,
       "p4880": p4880,
       "p4850": p4850,
       "p4760": p4760,
       "p4941": p4941,
       "br12": br12,
       "router": router,
       "ipRSTable": ipRSTable,
       "ipRSEntry": ipRSEntry,
       "ipRSIndex": ipRSIndex,
       "gwProtocol": gwProtocol,
       "ifStatus": ifStatus,
       "receivedTotal": receivedTotal,
       "transmittedTotal": transmittedTotal,
       "outDiscardsTotal": outDiscardsTotal,
       "noRouteTotal": noRouteTotal,
       "icmpRSTable": icmpRSTable,
       "destUnreachLastRx": destUnreachLastRx,
       "destUnreachLastTx": destUnreachLastTx,
       "sourceQuenchLastRx": sourceQuenchLastRx,
       "sourceQuenchLastTx": sourceQuenchLastTx,
       "redirectsLastRx": redirectsLastRx,
       "redirectsLastTx": redirectsLastTx,
       "echoRequestsLastRx": echoRequestsLastRx,
       "echoRequestsLastTx": echoRequestsLastTx,
       "timeExceededLastRx": timeExceededLastRx,
       "timeExceededLastTx": timeExceededLastTx,
       "paramProbLastRx": paramProbLastRx,
       "paramProbLastTx": paramProbLastTx,
       "ipRouting": ipRouting,
       "boot": boot,
       "bootpRetryCount": bootpRetryCount,
       "downloadRetryCount": downloadRetryCount,
       "downloadFilename": downloadFilename,
       "bootserverIpAddress": bootserverIpAddress,
       "loadserverIpAddress": loadserverIpAddress,
       "uniqueBroadcastAddress": uniqueBroadcastAddress,
       "tftpRetryCount": tftpRetryCount,
       "tftpRetryPeriod": tftpRetryPeriod,
       "initiateBootpDll": initiateBootpDll,
       "boothelper": boothelper,
       "boothelperEnabled": boothelperEnabled,
       "boothelperHopsLimit": boothelperHopsLimit,
       "boothelperForwardingAddress": boothelperForwardingAddress}
)
