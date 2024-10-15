# SNMP MIB module (RETIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RETIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:59 2024
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

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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

_Retix_ObjectIdentity = ObjectIdentity
retix = _Retix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72)
)
_Station_ObjectIdentity = ObjectIdentity
station = _Station_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 1)
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
    (1, 3, 6, 1, 4, 1, 72, 1, 1),
    _StationTime_Type()
)
stationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationTime.setStatus("mandatory")
_StationCountResets_Type = Counter32
_StationCountResets_Object = MibScalar
stationCountResets = _StationCountResets_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 2),
    _StationCountResets_Type()
)
stationCountResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationCountResets.setStatus("mandatory")
_FreeBufferCount_Type = Integer32
_FreeBufferCount_Object = MibScalar
freeBufferCount = _FreeBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 3),
    _FreeBufferCount_Type()
)
freeBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeBufferCount.setStatus("mandatory")
_FreeHeaderCount_Type = Integer32
_FreeHeaderCount_Object = MibScalar
freeHeaderCount = _FreeHeaderCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 4),
    _FreeHeaderCount_Type()
)
freeHeaderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeHeaderCount.setStatus("mandatory")


class _PhysBlkSize_Type(Integer32):
    """Custom type physBlkSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1600),
    )


_PhysBlkSize_Type.__name__ = "Integer32"
_PhysBlkSize_Object = MibScalar
physBlkSize = _PhysBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 5),
    _PhysBlkSize_Type()
)
physBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physBlkSize.setStatus("mandatory")


class _NewPhysBlkSize_Type(Integer32):
    """Custom type newPhysBlkSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1600),
    )


_NewPhysBlkSize_Type.__name__ = "Integer32"
_NewPhysBlkSize_Object = MibScalar
newPhysBlkSize = _NewPhysBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 6),
    _NewPhysBlkSize_Type()
)
newPhysBlkSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newPhysBlkSize.setStatus("mandatory")


class _ResetStation_Type(Integer32):
    """Custom type resetStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetStation", 2))
    )


_ResetStation_Type.__name__ = "Integer32"
_ResetStation_Object = MibScalar
resetStation = _ResetStation_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 7),
    _ResetStation_Type()
)
resetStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStation.setStatus("mandatory")


class _InitStation_Type(Integer32):
    """Custom type initStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 2),
          ("noAction", 1))
    )


_InitStation_Type.__name__ = "Integer32"
_InitStation_Object = MibScalar
initStation = _InitStation_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 8),
    _InitStation_Type()
)
initStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initStation.setStatus("mandatory")


class _ResetStats_Type(Integer32):
    """Custom type resetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetStats", 2))
    )


_ResetStats_Type.__name__ = "Integer32"
_ResetStats_Object = MibScalar
resetStats = _ResetStats_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 9),
    _ResetStats_Type()
)
resetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetStats.setStatus("mandatory")
_ProcessorLoading_Type = Integer32
_ProcessorLoading_Object = MibScalar
processorLoading = _ProcessorLoading_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 10),
    _ProcessorLoading_Type()
)
processorLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorLoading.setStatus("mandatory")
_TrapDestinationTable_ObjectIdentity = ObjectIdentity
trapDestinationTable = _TrapDestinationTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 1, 11)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 11, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("mandatory")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 11, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "RETIX-MIB", "trapDestEntryIpAddr"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("mandatory")
_TrapDestEntryIpAddr_Type = IpAddress
_TrapDestEntryIpAddr_Object = MibTableColumn
trapDestEntryIpAddr = _TrapDestEntryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 11, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 1, 11, 1, 1, 2),
    _TrapDestEntryCommunityName_Type()
)
trapDestEntryCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestEntryCommunityName.setStatus("mandatory")


class _TrapDestEntryType_Type(Integer32):
    """Custom type trapDestEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TrapDestEntryType_Type.__name__ = "Integer32"
_TrapDestEntryType_Object = MibTableColumn
trapDestEntryType = _TrapDestEntryType_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 11, 1, 1, 3),
    _TrapDestEntryType_Type()
)
trapDestEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestEntryType.setStatus("mandatory")


class _TrapDestAction_Type(Integer32):
    """Custom type trapDestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearTable", 2),
          ("noAction", 1))
    )


_TrapDestAction_Type.__name__ = "Integer32"
_TrapDestAction_Object = MibScalar
trapDestAction = _TrapDestAction_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 11, 2),
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
    (1, 3, 6, 1, 4, 1, 72, 1, 11, 3),
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
    (1, 3, 6, 1, 4, 1, 72, 1, 12),
    _PassWord_Type()
)
passWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passWord.setStatus("mandatory")
_SnmpAccessPolicyObject_ObjectIdentity = ObjectIdentity
snmpAccessPolicyObject = _SnmpAccessPolicyObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 1, 13)
)
_SnmpAccessPolicyTable_Object = MibTable
snmpAccessPolicyTable = _SnmpAccessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 1)
)
if mibBuilder.loadTexts:
    snmpAccessPolicyTable.setStatus("mandatory")
_SnmpAccessPolicyEntry_Object = MibTableRow
snmpAccessPolicyEntry = _SnmpAccessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 1, 1)
)
snmpAccessPolicyEntry.setIndexNames(
    (0, "RETIX-MIB", "accessPolicyIndex"),
)
if mibBuilder.loadTexts:
    snmpAccessPolicyEntry.setStatus("mandatory")
_AccessPolicyIndex_Type = Integer32
_AccessPolicyIndex_Object = MibTableColumn
accessPolicyIndex = _AccessPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 1, 1, 2),
    _CommunityName_Type()
)
communityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityName.setStatus("mandatory")


class _AccessMode_Type(Integer32):
    """Custom type accessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccessMode_Type.__name__ = "Integer32"
_AccessMode_Object = MibTableColumn
accessMode = _AccessMode_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 1, 1, 3),
    _AccessMode_Type()
)
accessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessMode.setStatus("mandatory")


class _SnmpAccessPolicyType_Type(Integer32):
    """Custom type snmpAccessPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SnmpAccessPolicyType_Type.__name__ = "Integer32"
_SnmpAccessPolicyType_Object = MibTableColumn
snmpAccessPolicyType = _SnmpAccessPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 1, 1, 4),
    _SnmpAccessPolicyType_Type()
)
snmpAccessPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessPolicyType.setStatus("mandatory")


class _SnmpAccessPolicyAction_Type(Integer32):
    """Custom type snmpAccessPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearTable", 2),
          ("noAction", 1))
    )


_SnmpAccessPolicyAction_Type.__name__ = "Integer32"
_SnmpAccessPolicyAction_Object = MibScalar
snmpAccessPolicyAction = _SnmpAccessPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 2),
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
    (1, 3, 6, 1, 4, 1, 72, 1, 13, 3),
    _SnmpAccessPolicyPage_Type()
)
snmpAccessPolicyPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessPolicyPage.setStatus("mandatory")


class _AuthenticationTrapStatus_Type(Integer32):
    """Custom type authenticationTrapStatus based on Integer32"""
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


_AuthenticationTrapStatus_Type.__name__ = "Integer32"
_AuthenticationTrapStatus_Object = MibScalar
authenticationTrapStatus = _AuthenticationTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 72, 1, 15),
    _SerialTxQueueSize_Type()
)
serialTxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTxQueueSize.setStatus("mandatory")
_InternalQueueCurrentLength_Type = Integer32
_InternalQueueCurrentLength_Object = MibScalar
internalQueueCurrentLength = _InternalQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 16),
    _InternalQueueCurrentLength_Type()
)
internalQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalQueueCurrentLength.setStatus("mandatory")
_QueueUpperLimit_Type = Integer32
_QueueUpperLimit_Object = MibScalar
queueUpperLimit = _QueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 17),
    _QueueUpperLimit_Type()
)
queueUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueUpperLimit.setStatus("mandatory")
_LanQueueSize_Type = Integer32
_LanQueueSize_Object = MibScalar
lanQueueSize = _LanQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 1, 18),
    _LanQueueSize_Type()
)
lanQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanQueueSize.setStatus("mandatory")
_Lapb_ObjectIdentity = ObjectIdentity
lapb = _Lapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 2)
)
_LapbNumber_Type = Integer32
_LapbNumber_Object = MibScalar
lapbNumber = _LapbNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 1),
    _LapbNumber_Type()
)
lapbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbNumber.setStatus("mandatory")
_LapbTable_Object = MibTable
lapbTable = _LapbTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2)
)
if mibBuilder.loadTexts:
    lapbTable.setStatus("mandatory")
_LapbEntry_Object = MibTableRow
lapbEntry = _LapbEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1)
)
lapbEntry.setIndexNames(
    (0, "RETIX-MIB", "lapbIndex"),
)
if mibBuilder.loadTexts:
    lapbEntry.setStatus("mandatory")
_LapbIndex_Type = Integer32
_LapbIndex_Object = MibTableColumn
lapbIndex = _LapbIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 2),
    _LapbModeT1_Type()
)
lapbModeT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbModeT1.setStatus("mandatory")
_LapbAutoT1value_Type = Integer32
_LapbAutoT1value_Object = MibTableColumn
lapbAutoT1value = _LapbAutoT1value_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 6),
    _LapbPolarity_Type()
)
lapbPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbPolarity.setStatus("mandatory")
_LapbCountResets_Type = Counter32
_LapbCountResets_Object = MibTableColumn
lapbCountResets = _LapbCountResets_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 7),
    _LapbCountResets_Type()
)
lapbCountResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountResets.setStatus("mandatory")
_LapbCountSentFrames_Type = Counter32
_LapbCountSentFrames_Object = MibTableColumn
lapbCountSentFrames = _LapbCountSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 8),
    _LapbCountSentFrames_Type()
)
lapbCountSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountSentFrames.setStatus("mandatory")
_LapbCountRcvFrames_Type = Counter32
_LapbCountRcvFrames_Object = MibTableColumn
lapbCountRcvFrames = _LapbCountRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 9),
    _LapbCountRcvFrames_Type()
)
lapbCountRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountRcvFrames.setStatus("mandatory")
_LapbCountSentOctets_Type = Counter32
_LapbCountSentOctets_Object = MibTableColumn
lapbCountSentOctets = _LapbCountSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 10),
    _LapbCountSentOctets_Type()
)
lapbCountSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountSentOctets.setStatus("mandatory")
_LapbCountRcvOctets_Type = Counter32
_LapbCountRcvOctets_Object = MibTableColumn
lapbCountRcvOctets = _LapbCountRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 11),
    _LapbCountRcvOctets_Type()
)
lapbCountRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountRcvOctets.setStatus("mandatory")
_LapbCountAborts_Type = Counter32
_LapbCountAborts_Object = MibTableColumn
lapbCountAborts = _LapbCountAborts_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 12),
    _LapbCountAborts_Type()
)
lapbCountAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountAborts.setStatus("mandatory")
_LapbCountCrcErrors_Type = Counter32
_LapbCountCrcErrors_Object = MibTableColumn
lapbCountCrcErrors = _LapbCountCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 13),
    _LapbCountCrcErrors_Type()
)
lapbCountCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountCrcErrors.setStatus("mandatory")
_LapbState_Type = Integer32
_LapbState_Object = MibTableColumn
lapbState = _LapbState_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 16),
    _LapbLastResetReason_Type()
)
lapbLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbLastResetReason.setStatus("mandatory")


class _LapbLinkReset_Type(Integer32):
    """Custom type lapbLinkReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_LapbLinkReset_Type.__name__ = "Integer32"
_LapbLinkReset_Object = MibTableColumn
lapbLinkReset = _LapbLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 2, 1, 17),
    _LapbLinkReset_Type()
)
lapbLinkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbLinkReset.setStatus("mandatory")
_LapbRetryCount_Type = Integer32
_LapbRetryCount_Object = MibScalar
lapbRetryCount = _LapbRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 2, 3),
    _LapbRetryCount_Type()
)
lapbRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbRetryCount.setStatus("mandatory")
_Ieee8023_ObjectIdentity = ObjectIdentity
ieee8023 = _Ieee8023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 3)
)
_Ieee8023Number_Type = Integer32
_Ieee8023Number_Object = MibScalar
ieee8023Number = _Ieee8023Number_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 1),
    _Ieee8023Number_Type()
)
ieee8023Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023Number.setStatus("mandatory")
_Ieee8023Table_Object = MibTable
ieee8023Table = _Ieee8023Table_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8023Table.setStatus("mandatory")
_Ieee8023Entry_Object = MibTableRow
ieee8023Entry = _Ieee8023Entry_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1)
)
ieee8023Entry.setIndexNames(
    (0, "RETIX-MIB", "ieee8023Index"),
)
if mibBuilder.loadTexts:
    ieee8023Entry.setStatus("mandatory")
_Ieee8023Index_Type = Integer32
_Ieee8023Index_Object = MibTableColumn
ieee8023Index = _Ieee8023Index_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 1),
    _Ieee8023Index_Type()
)
ieee8023Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023Index.setStatus("mandatory")
_Ieee8023FramesTransmittedOks_Type = Counter32
_Ieee8023FramesTransmittedOks_Object = MibTableColumn
ieee8023FramesTransmittedOks = _Ieee8023FramesTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 2),
    _Ieee8023FramesTransmittedOks_Type()
)
ieee8023FramesTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FramesTransmittedOks.setStatus("mandatory")
_Ieee8023SingleCollisionFrames_Type = Counter32
_Ieee8023SingleCollisionFrames_Object = MibTableColumn
ieee8023SingleCollisionFrames = _Ieee8023SingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 3),
    _Ieee8023SingleCollisionFrames_Type()
)
ieee8023SingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023SingleCollisionFrames.setStatus("mandatory")
_Ieee8023MultipleCollisionFrames_Type = Counter32
_Ieee8023MultipleCollisionFrames_Object = MibTableColumn
ieee8023MultipleCollisionFrames = _Ieee8023MultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 4),
    _Ieee8023MultipleCollisionFrames_Type()
)
ieee8023MultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MultipleCollisionFrames.setStatus("mandatory")
_Ieee8023OctetsTransmittedOks_Type = Counter32
_Ieee8023OctetsTransmittedOks_Object = MibTableColumn
ieee8023OctetsTransmittedOks = _Ieee8023OctetsTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 5),
    _Ieee8023OctetsTransmittedOks_Type()
)
ieee8023OctetsTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023OctetsTransmittedOks.setStatus("mandatory")
_Ieee8023DeferredTransmissions_Type = Counter32
_Ieee8023DeferredTransmissions_Object = MibTableColumn
ieee8023DeferredTransmissions = _Ieee8023DeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 6),
    _Ieee8023DeferredTransmissions_Type()
)
ieee8023DeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023DeferredTransmissions.setStatus("mandatory")
_Ieee8023MulticastFramesTransmittedOks_Type = Counter32
_Ieee8023MulticastFramesTransmittedOks_Object = MibTableColumn
ieee8023MulticastFramesTransmittedOks = _Ieee8023MulticastFramesTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 7),
    _Ieee8023MulticastFramesTransmittedOks_Type()
)
ieee8023MulticastFramesTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MulticastFramesTransmittedOks.setStatus("mandatory")
_Ieee8023BroadcastFramesTransmittedOks_Type = Counter32
_Ieee8023BroadcastFramesTransmittedOks_Object = MibTableColumn
ieee8023BroadcastFramesTransmittedOks = _Ieee8023BroadcastFramesTransmittedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 8),
    _Ieee8023BroadcastFramesTransmittedOks_Type()
)
ieee8023BroadcastFramesTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023BroadcastFramesTransmittedOks.setStatus("mandatory")
_Ieee8023LateCollisions_Type = Counter32
_Ieee8023LateCollisions_Object = MibTableColumn
ieee8023LateCollisions = _Ieee8023LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 9),
    _Ieee8023LateCollisions_Type()
)
ieee8023LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023LateCollisions.setStatus("mandatory")
_Ieee8023ExcessiveCollisions_Type = Counter32
_Ieee8023ExcessiveCollisions_Object = MibTableColumn
ieee8023ExcessiveCollisions = _Ieee8023ExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 10),
    _Ieee8023ExcessiveCollisions_Type()
)
ieee8023ExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023ExcessiveCollisions.setStatus("mandatory")
_Ieee8023InternalMACTransmitErrors_Type = Counter32
_Ieee8023InternalMACTransmitErrors_Object = MibTableColumn
ieee8023InternalMACTransmitErrors = _Ieee8023InternalMACTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 11),
    _Ieee8023InternalMACTransmitErrors_Type()
)
ieee8023InternalMACTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023InternalMACTransmitErrors.setStatus("mandatory")
_Ieee8023CarrierSenseErrors_Type = Counter32
_Ieee8023CarrierSenseErrors_Object = MibTableColumn
ieee8023CarrierSenseErrors = _Ieee8023CarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 12),
    _Ieee8023CarrierSenseErrors_Type()
)
ieee8023CarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023CarrierSenseErrors.setStatus("mandatory")
_Ieee8023ExcessiveDeferrals_Type = Counter32
_Ieee8023ExcessiveDeferrals_Object = MibTableColumn
ieee8023ExcessiveDeferrals = _Ieee8023ExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 13),
    _Ieee8023ExcessiveDeferrals_Type()
)
ieee8023ExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023ExcessiveDeferrals.setStatus("mandatory")
_Ieee8023FramesReceivedOks_Type = Counter32
_Ieee8023FramesReceivedOks_Object = MibTableColumn
ieee8023FramesReceivedOks = _Ieee8023FramesReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 14),
    _Ieee8023FramesReceivedOks_Type()
)
ieee8023FramesReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FramesReceivedOks.setStatus("mandatory")
_Ieee8023OctetsReceivedOks_Type = Counter32
_Ieee8023OctetsReceivedOks_Object = MibTableColumn
ieee8023OctetsReceivedOks = _Ieee8023OctetsReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 15),
    _Ieee8023OctetsReceivedOks_Type()
)
ieee8023OctetsReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023OctetsReceivedOks.setStatus("mandatory")
_Ieee8023MulticastFramesReceivedOks_Type = Counter32
_Ieee8023MulticastFramesReceivedOks_Object = MibTableColumn
ieee8023MulticastFramesReceivedOks = _Ieee8023MulticastFramesReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 16),
    _Ieee8023MulticastFramesReceivedOks_Type()
)
ieee8023MulticastFramesReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MulticastFramesReceivedOks.setStatus("mandatory")
_Ieee8023BroadcastFramesReceivedOks_Type = Counter32
_Ieee8023BroadcastFramesReceivedOks_Object = MibTableColumn
ieee8023BroadcastFramesReceivedOks = _Ieee8023BroadcastFramesReceivedOks_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 17),
    _Ieee8023BroadcastFramesReceivedOks_Type()
)
ieee8023BroadcastFramesReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023BroadcastFramesReceivedOks.setStatus("mandatory")
_Ieee8023FrameTooLongs_Type = Counter32
_Ieee8023FrameTooLongs_Object = MibTableColumn
ieee8023FrameTooLongs = _Ieee8023FrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 18),
    _Ieee8023FrameTooLongs_Type()
)
ieee8023FrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FrameTooLongs.setStatus("mandatory")
_Ieee8023AlignmentErrors_Type = Counter32
_Ieee8023AlignmentErrors_Object = MibTableColumn
ieee8023AlignmentErrors = _Ieee8023AlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 19),
    _Ieee8023AlignmentErrors_Type()
)
ieee8023AlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023AlignmentErrors.setStatus("mandatory")
_Ieee8023FCSErrors_Type = Counter32
_Ieee8023FCSErrors_Object = MibTableColumn
ieee8023FCSErrors = _Ieee8023FCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 20),
    _Ieee8023FCSErrors_Type()
)
ieee8023FCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023FCSErrors.setStatus("mandatory")
_Ieee8023inRangeLengthErrors_Type = Counter32
_Ieee8023inRangeLengthErrors_Object = MibTableColumn
ieee8023inRangeLengthErrors = _Ieee8023inRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 21),
    _Ieee8023inRangeLengthErrors_Type()
)
ieee8023inRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023inRangeLengthErrors.setStatus("mandatory")
_Ieee8023outOfRangeLengthFields_Type = Counter32
_Ieee8023outOfRangeLengthFields_Object = MibTableColumn
ieee8023outOfRangeLengthFields = _Ieee8023outOfRangeLengthFields_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 22),
    _Ieee8023outOfRangeLengthFields_Type()
)
ieee8023outOfRangeLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023outOfRangeLengthFields.setStatus("mandatory")
_Ieee8023InternalMACReceiveErrors_Type = Counter32
_Ieee8023InternalMACReceiveErrors_Object = MibTableColumn
ieee8023InternalMACReceiveErrors = _Ieee8023InternalMACReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 25),
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
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 26),
    _Ieee8023MACSubLayerStatus_Type()
)
ieee8023MACSubLayerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023MACSubLayerStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 27),
    _Ieee8023TransmitStatus_Type()
)
ieee8023TransmitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023TransmitStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 28),
    _Ieee8023MulticastReceiveStatus_Type()
)
ieee8023MulticastReceiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023MulticastReceiveStatus.setStatus("mandatory")


class _Ieee8023MACAddress_Type(OctetString):
    """Custom type ieee8023MACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ieee8023MACAddress_Type.__name__ = "OctetString"
_Ieee8023MACAddress_Object = MibTableColumn
ieee8023MACAddress = _Ieee8023MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 29),
    _Ieee8023MACAddress_Type()
)
ieee8023MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023MACAddress.setStatus("mandatory")
_Ieee8023SQETestErrors_Type = Counter32
_Ieee8023SQETestErrors_Object = MibTableColumn
ieee8023SQETestErrors = _Ieee8023SQETestErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 2, 1, 30),
    _Ieee8023SQETestErrors_Type()
)
ieee8023SQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8023SQETestErrors.setStatus("mandatory")
_Ieee8023NewMACAddress_Object = MibTable
ieee8023NewMACAddress = _Ieee8023NewMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 3)
)
if mibBuilder.loadTexts:
    ieee8023NewMACAddress.setStatus("mandatory")
_Ieee8023NewMACAddressEntry_Object = MibTableRow
ieee8023NewMACAddressEntry = _Ieee8023NewMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 3, 1)
)
ieee8023NewMACAddressEntry.setIndexNames(
    (0, "RETIX-MIB", "ieee8023NewMACAddressIndex"),
)
if mibBuilder.loadTexts:
    ieee8023NewMACAddressEntry.setStatus("mandatory")
_Ieee8023NewMACAddressIndex_Type = Integer32
_Ieee8023NewMACAddressIndex_Object = MibTableColumn
ieee8023NewMACAddressIndex = _Ieee8023NewMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 3, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 3, 3, 1, 2),
    _Ieee8023NewMACAddressValue_Type()
)
ieee8023NewMACAddressValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8023NewMACAddressValue.setStatus("mandatory")
_PhySerIf_ObjectIdentity = ObjectIdentity
phySerIf = _PhySerIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 4)
)
_PhySerIfNumber_Type = Integer32
_PhySerIfNumber_Object = MibScalar
phySerIfNumber = _PhySerIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 1),
    _PhySerIfNumber_Type()
)
phySerIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfNumber.setStatus("mandatory")
_PhySerIfTable_Object = MibTable
phySerIfTable = _PhySerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 2)
)
if mibBuilder.loadTexts:
    phySerIfTable.setStatus("mandatory")
_PhySerIfEntry_Object = MibTableRow
phySerIfEntry = _PhySerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1)
)
phySerIfEntry.setIndexNames(
    (0, "RETIX-MIB", "phySerIfIndex"),
)
if mibBuilder.loadTexts:
    phySerIfEntry.setStatus("mandatory")
_PhySerIfIndex_Type = Integer32
_PhySerIfIndex_Object = MibTableColumn
phySerIfIndex = _PhySerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 2),
    _PhySerIfInterfaceType_Type()
)
phySerIfInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfInterfaceType.setStatus("mandatory")
_PhySerIfMeasuredSpeed_Type = Integer32
_PhySerIfMeasuredSpeed_Object = MibTableColumn
phySerIfMeasuredSpeed = _PhySerIfMeasuredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 5),
    _PhySerIfPortSpeed_Type()
)
phySerIfPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfPortSpeed.setStatus("mandatory")
_PhySerIfTransitDelay_Type = Integer32
_PhySerIfTransitDelay_Object = MibTableColumn
phySerIfTransitDelay = _PhySerIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 6),
    _PhySerIfTransitDelay_Type()
)
phySerIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfTransitDelay.setStatus("mandatory")
_PhySerIfT1clockSource_Type = Integer32
_PhySerIfT1clockSource_Object = MibTableColumn
phySerIfT1clockSource = _PhySerIfT1clockSource_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 11),
    _PhySerIfT1frameAndCode_Type()
)
phySerIfT1frameAndCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phySerIfT1frameAndCode.setStatus("mandatory")


class _PhySerIfPartnerAddress_Type(OctetString):
    """Custom type phySerIfPartnerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PhySerIfPartnerAddress_Type.__name__ = "OctetString"
_PhySerIfPartnerAddress_Object = MibTableColumn
phySerIfPartnerAddress = _PhySerIfPartnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 4, 2, 1, 12),
    _PhySerIfPartnerAddress_Type()
)
phySerIfPartnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phySerIfPartnerAddress.setStatus("mandatory")
_Mlink_ObjectIdentity = ObjectIdentity
mlink = _Mlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 5)
)
_MlinkNumber_Type = Integer32
_MlinkNumber_Object = MibScalar
mlinkNumber = _MlinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 1),
    _MlinkNumber_Type()
)
mlinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkNumber.setStatus("mandatory")
_MlinkTable_Object = MibTable
mlinkTable = _MlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2)
)
if mibBuilder.loadTexts:
    mlinkTable.setStatus("mandatory")
_MlinkEntry_Object = MibTableRow
mlinkEntry = _MlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1)
)
mlinkEntry.setIndexNames(
    (0, "RETIX-MIB", "mlinkIndex"),
)
if mibBuilder.loadTexts:
    mlinkEntry.setStatus("mandatory")
_MlinkIndex_Type = Integer32
_MlinkIndex_Object = MibTableColumn
mlinkIndex = _MlinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 2),
    _MlinkState_Type()
)
mlinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkState.setStatus("mandatory")
_MlinkSendSeq_Type = Integer32
_MlinkSendSeq_Object = MibTableColumn
mlinkSendSeq = _MlinkSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 3),
    _MlinkSendSeq_Type()
)
mlinkSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkSendSeq.setStatus("mandatory")
_MlinkRcvSeq_Type = Integer32
_MlinkRcvSeq_Object = MibTableColumn
mlinkRcvSeq = _MlinkRcvSeq_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 4),
    _MlinkRcvSeq_Type()
)
mlinkRcvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkRcvSeq.setStatus("mandatory")
_MlinkSendUpperEdge_Type = Integer32
_MlinkSendUpperEdge_Object = MibTableColumn
mlinkSendUpperEdge = _MlinkSendUpperEdge_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 5),
    _MlinkSendUpperEdge_Type()
)
mlinkSendUpperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkSendUpperEdge.setStatus("mandatory")
_MlinkRcvUpperEdge_Type = Integer32
_MlinkRcvUpperEdge_Object = MibTableColumn
mlinkRcvUpperEdge = _MlinkRcvUpperEdge_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 6),
    _MlinkRcvUpperEdge_Type()
)
mlinkRcvUpperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkRcvUpperEdge.setStatus("mandatory")
_MlinkLostFrames_Type = Counter32
_MlinkLostFrames_Object = MibTableColumn
mlinkLostFrames = _MlinkLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 7),
    _MlinkLostFrames_Type()
)
mlinkLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkLostFrames.setStatus("mandatory")
_DeletedMlinkFrames_Type = Counter32
_DeletedMlinkFrames_Object = MibTableColumn
deletedMlinkFrames = _DeletedMlinkFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 8),
    _DeletedMlinkFrames_Type()
)
deletedMlinkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deletedMlinkFrames.setStatus("mandatory")
_ExpressQueueCurrentLength_Type = Integer32
_ExpressQueueCurrentLength_Object = MibTableColumn
expressQueueCurrentLength = _ExpressQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 9),
    _ExpressQueueCurrentLength_Type()
)
expressQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressQueueCurrentLength.setStatus("mandatory")
_ExpressQueueUpperLimit_Type = Integer32
_ExpressQueueUpperLimit_Object = MibTableColumn
expressQueueUpperLimit = _ExpressQueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 10),
    _ExpressQueueUpperLimit_Type()
)
expressQueueUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressQueueUpperLimit.setStatus("mandatory")
_HiPriQueueCurrentLength_Type = Integer32
_HiPriQueueCurrentLength_Object = MibTableColumn
hiPriQueueCurrentLength = _HiPriQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 11),
    _HiPriQueueCurrentLength_Type()
)
hiPriQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiPriQueueCurrentLength.setStatus("mandatory")
_HiPriQueueUpperLimit_Type = Integer32
_HiPriQueueUpperLimit_Object = MibTableColumn
hiPriQueueUpperLimit = _HiPriQueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 12),
    _HiPriQueueUpperLimit_Type()
)
hiPriQueueUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiPriQueueUpperLimit.setStatus("mandatory")
_LoPriQueueCurrentLength_Type = Integer32
_LoPriQueueCurrentLength_Object = MibTableColumn
loPriQueueCurrentLength = _LoPriQueueCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 13),
    _LoPriQueueCurrentLength_Type()
)
loPriQueueCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loPriQueueCurrentLength.setStatus("mandatory")
_LoPriQueueUpperLimit_Type = Integer32
_LoPriQueueUpperLimit_Object = MibTableColumn
loPriQueueUpperLimit = _LoPriQueueUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 2, 1, 14),
    _LoPriQueueUpperLimit_Type()
)
loPriQueueUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loPriQueueUpperLimit.setStatus("mandatory")
_MlinkWindow_Type = Integer32
_MlinkWindow_Object = MibScalar
mlinkWindow = _MlinkWindow_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 3),
    _MlinkWindow_Type()
)
mlinkWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlinkWindow.setStatus("mandatory")
_MlinkRxTimeout_Type = Integer32
_MlinkRxTimeout_Object = MibScalar
mlinkRxTimeout = _MlinkRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 72, 5, 4),
    _MlinkRxTimeout_Type()
)
mlinkRxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlinkRxTimeout.setStatus("mandatory")
_Lan_ObjectIdentity = ObjectIdentity
lan = _Lan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 6)
)


class _LanInterfaceType_Type(Integer32):
    """Custom type lanInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneBase5", 2),
          ("tenBase2", 3),
          ("tenBase5", 1))
    )


_LanInterfaceType_Type.__name__ = "Integer32"
_LanInterfaceType_Object = MibScalar
lanInterfaceType = _LanInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 72, 6, 1),
    _LanInterfaceType_Type()
)
lanInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanInterfaceType.setStatus("mandatory")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 7)
)
_PortNumber_Type = Integer32
_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("mandatory")
_BridgeStatsTable_Object = MibTable
bridgeStatsTable = _BridgeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2)
)
if mibBuilder.loadTexts:
    bridgeStatsTable.setStatus("mandatory")
_BridgeStatsEntry_Object = MibTableRow
bridgeStatsEntry = _BridgeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1)
)
bridgeStatsEntry.setIndexNames(
    (0, "RETIX-MIB", "bridgeStatsIndex"),
)
if mibBuilder.loadTexts:
    bridgeStatsEntry.setStatus("mandatory")
_BridgeStatsIndex_Type = Integer32
_BridgeStatsIndex_Object = MibTableColumn
bridgeStatsIndex = _BridgeStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 1),
    _BridgeStatsIndex_Type()
)
bridgeStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsIndex.setStatus("mandatory")
_AverageForwardedFrames_Type = Counter32
_AverageForwardedFrames_Object = MibTableColumn
averageForwardedFrames = _AverageForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 2),
    _AverageForwardedFrames_Type()
)
averageForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageForwardedFrames.setStatus("mandatory")
_MaxForwardedFrames_Type = Counter32
_MaxForwardedFrames_Object = MibTableColumn
maxForwardedFrames = _MaxForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 3),
    _MaxForwardedFrames_Type()
)
maxForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxForwardedFrames.setStatus("mandatory")
_AverageRejectedFrames_Type = Counter32
_AverageRejectedFrames_Object = MibTableColumn
averageRejectedFrames = _AverageRejectedFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 4),
    _AverageRejectedFrames_Type()
)
averageRejectedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageRejectedFrames.setStatus("mandatory")
_MaxRejectedFrames_Type = Counter32
_MaxRejectedFrames_Object = MibTableColumn
maxRejectedFrames = _MaxRejectedFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 5),
    _MaxRejectedFrames_Type()
)
maxRejectedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRejectedFrames.setStatus("mandatory")
_LanAccepts_Type = Counter32
_LanAccepts_Object = MibTableColumn
lanAccepts = _LanAccepts_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 6),
    _LanAccepts_Type()
)
lanAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanAccepts.setStatus("mandatory")
_LanRejects_Type = Counter32
_LanRejects_Object = MibTableColumn
lanRejects = _LanRejects_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 7),
    _LanRejects_Type()
)
lanRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanRejects.setStatus("mandatory")
_DeletedLanFrames_Type = Counter32
_DeletedLanFrames_Object = MibTableColumn
deletedLanFrames = _DeletedLanFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 2, 1, 8),
    _DeletedLanFrames_Type()
)
deletedLanFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deletedLanFrames.setStatus("mandatory")
_StpTable_Object = MibTable
stpTable = _StpTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 3)
)
if mibBuilder.loadTexts:
    stpTable.setStatus("mandatory")
_StpEntry_Object = MibTableRow
stpEntry = _StpEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1)
)
stpEntry.setIndexNames(
    (0, "RETIX-MIB", "stpIndex"),
)
if mibBuilder.loadTexts:
    stpEntry.setStatus("mandatory")
_StpIndex_Type = Integer32
_StpIndex_Object = MibTableColumn
stpIndex = _StpIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 2),
    _PathCostMode_Type()
)
pathCostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathCostMode.setStatus("mandatory")
_PathCostAutoValue_Type = Integer32
_PathCostAutoValue_Object = MibTableColumn
pathCostAutoValue = _PathCostAutoValue_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 3),
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
_PathCostManualValue_Object = MibTableColumn
pathCostManualValue = _PathCostManualValue_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 4),
    _PathCostManualValue_Type()
)
pathCostManualValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathCostManualValue.setStatus("mandatory")
_PortSpatState_Type = Integer32
_PortSpatState_Object = MibTableColumn
portSpatState = _PortSpatState_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 6),
    _PortPriorityMode_Type()
)
portPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriorityMode.setStatus("mandatory")
_PortPriorityAutoValue_Type = Integer32
_PortPriorityAutoValue_Object = MibTableColumn
portPriorityAutoValue = _PortPriorityAutoValue_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 4),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 5),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 6),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 7),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 8),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 9),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 10),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 11),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 12),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 13),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 14),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 15),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 16),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 17),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 18),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 19),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 20),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 21),
    _IeeeFormatPriority_Type()
)
ieeeFormatPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieeeFormatPriority.setStatus("mandatory")
_AveragePeriod_Type = Integer32
_AveragePeriod_Object = MibScalar
averagePeriod = _AveragePeriod_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 22),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 23),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 24),
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
    (1, 3, 6, 1, 4, 1, 72, 7, 25),
    _AdaptiveMcastAddr_Type()
)
adaptiveMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveMcastAddr.setStatus("mandatory")
_ArAddressInfo_ObjectIdentity = ObjectIdentity
arAddressInfo = _ArAddressInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 7, 26)
)
_StandbyRemote_Type = Integer32
_StandbyRemote_Object = MibScalar
standbyRemote = _StandbyRemote_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 26, 1),
    _StandbyRemote_Type()
)
standbyRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyRemote.setStatus("mandatory")
_StandbyLocal_Type = Integer32
_StandbyLocal_Object = MibScalar
standbyLocal = _StandbyLocal_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 26, 2),
    _StandbyLocal_Type()
)
standbyLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbyLocal.setStatus("mandatory")
_ActiveRemote_Type = Integer32
_ActiveRemote_Object = MibScalar
activeRemote = _ActiveRemote_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 26, 3),
    _ActiveRemote_Type()
)
activeRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeRemote.setStatus("mandatory")
_ActiveLocal_Type = Integer32
_ActiveLocal_Object = MibScalar
activeLocal = _ActiveLocal_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 26, 4),
    _ActiveLocal_Type()
)
activeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeLocal.setStatus("mandatory")
_MaxSerialLoading_Type = Integer32
_MaxSerialLoading_Object = MibScalar
maxSerialLoading = _MaxSerialLoading_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 27),
    _MaxSerialLoading_Type()
)
maxSerialLoading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxSerialLoading.setStatus("mandatory")


class _SerialLoadPeriod_Type(Integer32):
    """Custom type serialLoadPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60)
        )
    )
    namedValues = NamedValues(
        *(("fifty", 50),
          ("forty", 40),
          ("sixty", 60),
          ("ten", 10),
          ("thirty", 30),
          ("twenty", 20))
    )


_SerialLoadPeriod_Type.__name__ = "Integer32"
_SerialLoadPeriod_Object = MibScalar
serialLoadPeriod = _SerialLoadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 28),
    _SerialLoadPeriod_Type()
)
serialLoadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialLoadPeriod.setStatus("mandatory")
_SerialLoading_Type = Integer32
_SerialLoading_Object = MibScalar
serialLoading = _SerialLoading_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 29),
    _SerialLoading_Type()
)
serialLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialLoading.setStatus("mandatory")
_FilteringDataBaseTable_ObjectIdentity = ObjectIdentity
filteringDataBaseTable = _FilteringDataBaseTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 7, 30)
)
_FilteringDbTable_Object = MibTable
filteringDbTable = _FilteringDbTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 30, 1)
)
if mibBuilder.loadTexts:
    filteringDbTable.setStatus("mandatory")
_FilteringDbEntry_Object = MibTableRow
filteringDbEntry = _FilteringDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 30, 1, 1)
)
filteringDbEntry.setIndexNames(
    (0, "RETIX-MIB", "filteringDbMacAddress"),
)
if mibBuilder.loadTexts:
    filteringDbEntry.setStatus("mandatory")


class _FilteringDbMacAddress_Type(OctetString):
    """Custom type filteringDbMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FilteringDbMacAddress_Type.__name__ = "OctetString"
_FilteringDbMacAddress_Object = MibTableColumn
filteringDbMacAddress = _FilteringDbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 30, 1, 1, 1),
    _FilteringDbMacAddress_Type()
)
filteringDbMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbMacAddress.setStatus("mandatory")
_FilteringDbDisposition_Type = Integer32
_FilteringDbDisposition_Object = MibTableColumn
filteringDbDisposition = _FilteringDbDisposition_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 30, 1, 1, 2),
    _FilteringDbDisposition_Type()
)
filteringDbDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbDisposition.setStatus("mandatory")
_FilteringDbStatus_Type = Integer32
_FilteringDbStatus_Object = MibTableColumn
filteringDbStatus = _FilteringDbStatus_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 30, 1, 1, 3),
    _FilteringDbStatus_Type()
)
filteringDbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbStatus.setStatus("mandatory")


class _FilteringDbType_Type(Integer32):
    """Custom type filteringDbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_FilteringDbType_Type.__name__ = "Integer32"
_FilteringDbType_Object = MibTableColumn
filteringDbType = _FilteringDbType_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 30, 1, 1, 4),
    _FilteringDbType_Type()
)
filteringDbType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbType.setStatus("mandatory")


class _FilteringDbAction_Type(Integer32):
    """Custom type filteringDbAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearTable", 2),
          ("noAction", 1))
    )


_FilteringDbAction_Type.__name__ = "Integer32"
_FilteringDbAction_Object = MibScalar
filteringDbAction = _FilteringDbAction_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 30, 2),
    _FilteringDbAction_Type()
)
filteringDbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filteringDbAction.setStatus("mandatory")
_PriorityTable_ObjectIdentity = ObjectIdentity
priorityTable = _PriorityTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 7, 31)
)
_PrioritySubTable_Object = MibTable
prioritySubTable = _PrioritySubTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 31, 1)
)
if mibBuilder.loadTexts:
    prioritySubTable.setStatus("mandatory")
_PriorityTableEntry_Object = MibTableRow
priorityTableEntry = _PriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 31, 1, 1)
)
priorityTableEntry.setIndexNames(
    (0, "RETIX-MIB", "priorityTableEntryValue"),
)
if mibBuilder.loadTexts:
    priorityTableEntry.setStatus("mandatory")
_PriorityTableEntryValue_Type = Integer32
_PriorityTableEntryValue_Object = MibTableColumn
priorityTableEntryValue = _PriorityTableEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 31, 1, 1, 1),
    _PriorityTableEntryValue_Type()
)
priorityTableEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityTableEntryValue.setStatus("mandatory")


class _PriorityTableEntryType_Type(Integer32):
    """Custom type priorityTableEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_PriorityTableEntryType_Type.__name__ = "Integer32"
_PriorityTableEntryType_Object = MibTableColumn
priorityTableEntryType = _PriorityTableEntryType_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 31, 1, 1, 2),
    _PriorityTableEntryType_Type()
)
priorityTableEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityTableEntryType.setStatus("mandatory")


class _PriorityTableAction_Type(Integer32):
    """Custom type priorityTableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearTable", 2),
          ("noAction", 1))
    )


_PriorityTableAction_Type.__name__ = "Integer32"
_PriorityTableAction_Object = MibScalar
priorityTableAction = _PriorityTableAction_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 31, 2),
    _PriorityTableAction_Type()
)
priorityTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityTableAction.setStatus("mandatory")


class _PriorityPage_Type(OctetString):
    """Custom type priorityPage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_PriorityPage_Type.__name__ = "OctetString"
_PriorityPage_Object = MibScalar
priorityPage = _PriorityPage_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 31, 3),
    _PriorityPage_Type()
)
priorityPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priorityPage.setStatus("optional")
_FilterTable_ObjectIdentity = ObjectIdentity
filterTable = _FilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 7, 32)
)
_FilterSubTable_Object = MibTable
filterSubTable = _FilterSubTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 32, 1)
)
if mibBuilder.loadTexts:
    filterSubTable.setStatus("mandatory")
_FilterTableEntry_Object = MibTableRow
filterTableEntry = _FilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 32, 1, 1)
)
filterTableEntry.setIndexNames(
    (0, "RETIX-MIB", "filterTableEntryValue"),
)
if mibBuilder.loadTexts:
    filterTableEntry.setStatus("mandatory")
_FilterTableEntryValue_Type = Integer32
_FilterTableEntryValue_Object = MibTableColumn
filterTableEntryValue = _FilterTableEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 32, 1, 1, 1),
    _FilterTableEntryValue_Type()
)
filterTableEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTableEntryValue.setStatus("mandatory")


class _FilterTableEntryType_Type(Integer32):
    """Custom type filterTableEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_FilterTableEntryType_Type.__name__ = "Integer32"
_FilterTableEntryType_Object = MibTableColumn
filterTableEntryType = _FilterTableEntryType_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 32, 1, 1, 2),
    _FilterTableEntryType_Type()
)
filterTableEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTableEntryType.setStatus("mandatory")


class _FilterTableAction_Type(Integer32):
    """Custom type filterTableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearTable", 2),
          ("noAction", 1))
    )


_FilterTableAction_Type.__name__ = "Integer32"
_FilterTableAction_Object = MibScalar
filterTableAction = _FilterTableAction_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 32, 2),
    _FilterTableAction_Type()
)
filterTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTableAction.setStatus("mandatory")


class _FilterPage_Type(OctetString):
    """Custom type filterPage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_FilterPage_Type.__name__ = "OctetString"
_FilterPage_Object = MibScalar
filterPage = _FilterPage_Object(
    (1, 3, 6, 1, 4, 1, 72, 7, 32, 3),
    _FilterPage_Type()
)
filterPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPage.setStatus("mandatory")
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 8)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 10)
)
_IpRSTable_Object = MibTable
ipRSTable = _IpRSTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1)
)
if mibBuilder.loadTexts:
    ipRSTable.setStatus("mandatory")
_IpRSEntry_Object = MibTableRow
ipRSEntry = _IpRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1)
)
ipRSEntry.setIndexNames(
    (0, "RETIX-MIB", "ipRSIndex"),
)
if mibBuilder.loadTexts:
    ipRSEntry.setStatus("mandatory")
_IpRSIndex_Type = Integer32
_IpRSIndex_Object = MibTableColumn
ipRSIndex = _IpRSIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1, 1),
    _IpRSIndex_Type()
)
ipRSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRSIndex.setStatus("mandatory")


class _GwProtocol_Type(Integer32):
    """Custom type gwProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rip", 8))
    )


_GwProtocol_Type.__name__ = "Integer32"
_GwProtocol_Object = MibTableColumn
gwProtocol = _GwProtocol_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1, 2),
    _GwProtocol_Type()
)
gwProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwProtocol.setStatus("mandatory")
_IfStatus_Type = Integer32
_IfStatus_Object = MibTableColumn
ifStatus = _IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1, 3),
    _IfStatus_Type()
)
ifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStatus.setStatus("mandatory")
_ReceivedTotalDgms_Type = Counter32
_ReceivedTotalDgms_Object = MibTableColumn
receivedTotalDgms = _ReceivedTotalDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1, 4),
    _ReceivedTotalDgms_Type()
)
receivedTotalDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedTotalDgms.setStatus("mandatory")
_TransmittedTotalDgms_Type = Counter32
_TransmittedTotalDgms_Object = MibTableColumn
transmittedTotalDgms = _TransmittedTotalDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1, 5),
    _TransmittedTotalDgms_Type()
)
transmittedTotalDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmittedTotalDgms.setStatus("mandatory")
_OutDiscardsTotalDgms_Type = Counter32
_OutDiscardsTotalDgms_Object = MibTableColumn
outDiscardsTotalDgms = _OutDiscardsTotalDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1, 6),
    _OutDiscardsTotalDgms_Type()
)
outDiscardsTotalDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outDiscardsTotalDgms.setStatus("mandatory")
_NoRouteTotalDgms_Type = Counter32
_NoRouteTotalDgms_Object = MibTableColumn
noRouteTotalDgms = _NoRouteTotalDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 1, 1, 7),
    _NoRouteTotalDgms_Type()
)
noRouteTotalDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noRouteTotalDgms.setStatus("mandatory")
_IcmpRSTable_ObjectIdentity = ObjectIdentity
icmpRSTable = _IcmpRSTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 10, 2)
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 7),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 8),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 9),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 10),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 11),
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
    (1, 3, 6, 1, 4, 1, 72, 10, 2, 12),
    _ParamProbLastTx_Type()
)
paramProbLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramProbLastTx.setStatus("mandatory")


class _IpRouting_Type(Integer32):
    """Custom type ipRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IpRouting_Type.__name__ = "Integer32"
_IpRouting_Object = MibScalar
ipRouting = _IpRouting_Object(
    (1, 3, 6, 1, 4, 1, 72, 10, 3),
    _IpRouting_Type()
)
ipRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouting.setStatus("mandatory")
_Boot_ObjectIdentity = ObjectIdentity
boot = _Boot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 11)
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
    (1, 3, 6, 1, 4, 1, 72, 11, 1),
    _BootpRetryCount_Type()
)
bootpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpRetryCount.setStatus("mandatory")


class _DownloadRetryCount_Type(Integer32):
    """Custom type downloadRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DownloadRetryCount_Type.__name__ = "Integer32"
_DownloadRetryCount_Object = MibScalar
downloadRetryCount = _DownloadRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 2),
    _DownloadRetryCount_Type()
)
downloadRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadRetryCount.setStatus("mandatory")


class _DownloadFilename_Type(OctetString):
    """Custom type downloadFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DownloadFilename_Type.__name__ = "OctetString"
_DownloadFilename_Object = MibScalar
downloadFilename = _DownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 3),
    _DownloadFilename_Type()
)
downloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFilename.setStatus("mandatory")
_BootserverIpAddress_Type = IpAddress
_BootserverIpAddress_Object = MibScalar
bootserverIpAddress = _BootserverIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 4),
    _BootserverIpAddress_Type()
)
bootserverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootserverIpAddress.setStatus("mandatory")
_LoadserverIpAddress_Type = IpAddress
_LoadserverIpAddress_Object = MibScalar
loadserverIpAddress = _LoadserverIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 5),
    _LoadserverIpAddress_Type()
)
loadserverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadserverIpAddress.setStatus("mandatory")
_UniqueBroadcastAddress_Type = IpAddress
_UniqueBroadcastAddress_Object = MibScalar
uniqueBroadcastAddress = _UniqueBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 6),
    _UniqueBroadcastAddress_Type()
)
uniqueBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniqueBroadcastAddress.setStatus("mandatory")


class _TftpRetryCount_Type(Integer32):
    """Custom type tftpRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TftpRetryCount_Type.__name__ = "Integer32"
_TftpRetryCount_Object = MibScalar
tftpRetryCount = _TftpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 7),
    _TftpRetryCount_Type()
)
tftpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRetryCount.setStatus("mandatory")


class _TftpRetryPeriod_Type(Integer32):
    """Custom type tftpRetryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TftpRetryPeriod_Type.__name__ = "Integer32"
_TftpRetryPeriod_Object = MibScalar
tftpRetryPeriod = _TftpRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 8),
    _TftpRetryPeriod_Type()
)
tftpRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRetryPeriod.setStatus("mandatory")


class _InitiateBootpDll_Type(Integer32):
    """Custom type initiateBootpDll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiateBoot", 2),
          ("noAction", 1))
    )


_InitiateBootpDll_Type.__name__ = "Integer32"
_InitiateBootpDll_Object = MibScalar
initiateBootpDll = _InitiateBootpDll_Object(
    (1, 3, 6, 1, 4, 1, 72, 11, 9),
    _InitiateBootpDll_Type()
)
initiateBootpDll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initiateBootpDll.setStatus("mandatory")
_Boothelper_ObjectIdentity = ObjectIdentity
boothelper = _Boothelper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 12)
)


class _BoothelperEnabled_Type(Integer32):
    """Custom type boothelperEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BoothelperEnabled_Type.__name__ = "Integer32"
_BoothelperEnabled_Object = MibScalar
boothelperEnabled = _BoothelperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 72, 12, 1),
    _BoothelperEnabled_Type()
)
boothelperEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boothelperEnabled.setStatus("mandatory")


class _BoothelperHopsLimit_Type(Integer32):
    """Custom type boothelperHopsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BoothelperHopsLimit_Type.__name__ = "Integer32"
_BoothelperHopsLimit_Object = MibScalar
boothelperHopsLimit = _BoothelperHopsLimit_Object(
    (1, 3, 6, 1, 4, 1, 72, 12, 2),
    _BoothelperHopsLimit_Type()
)
boothelperHopsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boothelperHopsLimit.setStatus("mandatory")
_BoothelperForwardingAddress_Type = IpAddress
_BoothelperForwardingAddress_Object = MibScalar
boothelperForwardingAddress = _BoothelperForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 12, 3),
    _BoothelperForwardingAddress_Type()
)
boothelperForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boothelperForwardingAddress.setStatus("mandatory")
_Remote_ObjectIdentity = ObjectIdentity
remote = _Remote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 13)
)
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 13, 1)
)


class _IpxRouting_Type(Integer32):
    """Custom type ipxRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IpxRouting_Type.__name__ = "Integer32"
_IpxRouting_Object = MibScalar
ipxRouting = _IpxRouting_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 1),
    _IpxRouting_Type()
)
ipxRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouting.setStatus("mandatory")
_IpxIfNumber_Type = Integer32
_IpxIfNumber_Object = MibScalar
ipxIfNumber = _IpxIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 2),
    _IpxIfNumber_Type()
)
ipxIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfNumber.setStatus("mandatory")
_IpxIfTable_Object = MibTable
ipxIfTable = _IpxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 3)
)
if mibBuilder.loadTexts:
    ipxIfTable.setStatus("mandatory")
_IpxIfEntry_Object = MibTableRow
ipxIfEntry = _IpxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 3, 1)
)
ipxIfEntry.setIndexNames(
    (0, "RETIX-MIB", "ipxIfIndex"),
)
if mibBuilder.loadTexts:
    ipxIfEntry.setStatus("mandatory")
_IpxIfIndex_Type = Integer32
_IpxIfIndex_Object = MibTableColumn
ipxIfIndex = _IpxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 3, 1, 1),
    _IpxIfIndex_Type()
)
ipxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfIndex.setStatus("mandatory")


class _IpxIfNwkNumber_Type(OctetString):
    """Custom type ipxIfNwkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IpxIfNwkNumber_Type.__name__ = "OctetString"
_IpxIfNwkNumber_Object = MibTableColumn
ipxIfNwkNumber = _IpxIfNwkNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 3, 1, 2),
    _IpxIfNwkNumber_Type()
)
ipxIfNwkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfNwkNumber.setStatus("mandatory")


class _IpxIfIPXAddress_Type(OctetString):
    """Custom type ipxIfIPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_IpxIfIPXAddress_Type.__name__ = "OctetString"
_IpxIfIPXAddress_Object = MibTableColumn
ipxIfIPXAddress = _IpxIfIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 3, 1, 3),
    _IpxIfIPXAddress_Type()
)
ipxIfIPXAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfIPXAddress.setStatus("mandatory")


class _IpxIfEncapsulation_Type(Integer32):
    """Custom type ipxIfEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_IpxIfEncapsulation_Type.__name__ = "Integer32"
_IpxIfEncapsulation_Object = MibTableColumn
ipxIfEncapsulation = _IpxIfEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 3, 1, 4),
    _IpxIfEncapsulation_Type()
)
ipxIfEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfEncapsulation.setStatus("mandatory")
_IpxIfDelay_Type = Integer32
_IpxIfDelay_Object = MibTableColumn
ipxIfDelay = _IpxIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 3, 1, 5),
    _IpxIfDelay_Type()
)
ipxIfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfDelay.setStatus("mandatory")
_IpxRoutingTable_Object = MibTable
ipxRoutingTable = _IpxRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4)
)
if mibBuilder.loadTexts:
    ipxRoutingTable.setStatus("mandatory")
_IpxRITEntry_Object = MibTableRow
ipxRITEntry = _IpxRITEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4, 1)
)
ipxRITEntry.setIndexNames(
    (0, "RETIX-MIB", "ipxRITDestNwkNumber"),
)
if mibBuilder.loadTexts:
    ipxRITEntry.setStatus("mandatory")
_IpxRITDestNwkNumber_Type = OctetString
_IpxRITDestNwkNumber_Object = MibTableColumn
ipxRITDestNwkNumber = _IpxRITDestNwkNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4, 1, 1),
    _IpxRITDestNwkNumber_Type()
)
ipxRITDestNwkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRITDestNwkNumber.setStatus("mandatory")


class _IpxRITGwyHostAddress_Type(OctetString):
    """Custom type ipxRITGwyHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IpxRITGwyHostAddress_Type.__name__ = "OctetString"
_IpxRITGwyHostAddress_Object = MibTableColumn
ipxRITGwyHostAddress = _IpxRITGwyHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4, 1, 2),
    _IpxRITGwyHostAddress_Type()
)
ipxRITGwyHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRITGwyHostAddress.setStatus("mandatory")
_IpxRITHopCount_Type = Integer32
_IpxRITHopCount_Object = MibTableColumn
ipxRITHopCount = _IpxRITHopCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4, 1, 3),
    _IpxRITHopCount_Type()
)
ipxRITHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRITHopCount.setStatus("mandatory")
_IpxRITDelay_Type = Integer32
_IpxRITDelay_Object = MibTableColumn
ipxRITDelay = _IpxRITDelay_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4, 1, 4),
    _IpxRITDelay_Type()
)
ipxRITDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRITDelay.setStatus("mandatory")
_IpxRITInterface_Type = Integer32
_IpxRITInterface_Object = MibTableColumn
ipxRITInterface = _IpxRITInterface_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4, 1, 5),
    _IpxRITInterface_Type()
)
ipxRITInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRITInterface.setStatus("mandatory")
_IpxRITDirectConnect_Type = Integer32
_IpxRITDirectConnect_Object = MibTableColumn
ipxRITDirectConnect = _IpxRITDirectConnect_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 4, 1, 6),
    _IpxRITDirectConnect_Type()
)
ipxRITDirectConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRITDirectConnect.setStatus("mandatory")
_IpxSAPBinderyTable_Object = MibTable
ipxSAPBinderyTable = _IpxSAPBinderyTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 5)
)
if mibBuilder.loadTexts:
    ipxSAPBinderyTable.setStatus("mandatory")
_IpxSAPBinderyEntry_Object = MibTableRow
ipxSAPBinderyEntry = _IpxSAPBinderyEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 5, 1)
)
ipxSAPBinderyEntry.setIndexNames(
    (0, "RETIX-MIB", "ipxSAPBinderyType"),
    (0, "RETIX-MIB", "ipxSAPBinderyServerIPXAddress"),
)
if mibBuilder.loadTexts:
    ipxSAPBinderyEntry.setStatus("mandatory")


class _IpxSAPBinderyType_Type(Integer32):
    """Custom type ipxSAPBinderyType based on Integer32"""
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
              36,
              71,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("administration", 11),
          ("advertizingPrintServer", 71),
          ("archiveQueue", 8),
          ("archiveServer", 9),
          ("fileServer", 4),
          ("gateway", 6),
          ("jobQueue", 10),
          ("jobServer", 5),
          ("printQueue", 3),
          ("printServer", 7),
          ("remoteBridgeServer", 36),
          ("user", 1),
          ("userGroup", 2),
          ("wild", 65535))
    )


_IpxSAPBinderyType_Type.__name__ = "Integer32"
_IpxSAPBinderyType_Object = MibTableColumn
ipxSAPBinderyType = _IpxSAPBinderyType_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 5, 1, 1),
    _IpxSAPBinderyType_Type()
)
ipxSAPBinderyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPBinderyType.setStatus("mandatory")


class _IpxSAPBinderyServerIPXAddress_Type(OctetString):
    """Custom type ipxSAPBinderyServerIPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_IpxSAPBinderyServerIPXAddress_Type.__name__ = "OctetString"
_IpxSAPBinderyServerIPXAddress_Object = MibTableColumn
ipxSAPBinderyServerIPXAddress = _IpxSAPBinderyServerIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 5, 1, 2),
    _IpxSAPBinderyServerIPXAddress_Type()
)
ipxSAPBinderyServerIPXAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPBinderyServerIPXAddress.setStatus("mandatory")


class _IpxSAPBinderyServerName_Type(OctetString):
    """Custom type ipxSAPBinderyServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxSAPBinderyServerName_Type.__name__ = "OctetString"
_IpxSAPBinderyServerName_Object = MibTableColumn
ipxSAPBinderyServerName = _IpxSAPBinderyServerName_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 5, 1, 3),
    _IpxSAPBinderyServerName_Type()
)
ipxSAPBinderyServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPBinderyServerName.setStatus("mandatory")
_IpxSAPBinderyHopCount_Type = Integer32
_IpxSAPBinderyHopCount_Object = MibTableColumn
ipxSAPBinderyHopCount = _IpxSAPBinderyHopCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 5, 1, 4),
    _IpxSAPBinderyHopCount_Type()
)
ipxSAPBinderyHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPBinderyHopCount.setStatus("mandatory")
_IpxSAPBinderySocket_Type = Integer32
_IpxSAPBinderySocket_Object = MibTableColumn
ipxSAPBinderySocket = _IpxSAPBinderySocket_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 5, 1, 5),
    _IpxSAPBinderySocket_Type()
)
ipxSAPBinderySocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSAPBinderySocket.setStatus("mandatory")
_IpxReceivedDgms_Type = Counter32
_IpxReceivedDgms_Object = MibScalar
ipxReceivedDgms = _IpxReceivedDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 6),
    _IpxReceivedDgms_Type()
)
ipxReceivedDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxReceivedDgms.setStatus("mandatory")
_IpxTransmittedDgms_Type = Counter32
_IpxTransmittedDgms_Object = MibScalar
ipxTransmittedDgms = _IpxTransmittedDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 7),
    _IpxTransmittedDgms_Type()
)
ipxTransmittedDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxTransmittedDgms.setStatus("mandatory")
_IpxNotRoutedRxDgms_Type = Counter32
_IpxNotRoutedRxDgms_Object = MibScalar
ipxNotRoutedRxDgms = _IpxNotRoutedRxDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 8),
    _IpxNotRoutedRxDgms_Type()
)
ipxNotRoutedRxDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxNotRoutedRxDgms.setStatus("mandatory")
_IpxForwardedDgms_Type = Counter32
_IpxForwardedDgms_Object = MibScalar
ipxForwardedDgms = _IpxForwardedDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 9),
    _IpxForwardedDgms_Type()
)
ipxForwardedDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxForwardedDgms.setStatus("mandatory")
_IpxInDelivers_Type = Counter32
_IpxInDelivers_Object = MibScalar
ipxInDelivers = _IpxInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 10),
    _IpxInDelivers_Type()
)
ipxInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInDelivers.setStatus("mandatory")
_IpxInHdrErrors_Type = Counter32
_IpxInHdrErrors_Object = MibScalar
ipxInHdrErrors = _IpxInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 11),
    _IpxInHdrErrors_Type()
)
ipxInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInHdrErrors.setStatus("mandatory")
_IpxAccessViolations_Type = Counter32
_IpxAccessViolations_Object = MibScalar
ipxAccessViolations = _IpxAccessViolations_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 12),
    _IpxAccessViolations_Type()
)
ipxAccessViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAccessViolations.setStatus("mandatory")
_IpxInDiscards_Type = Counter32
_IpxInDiscards_Object = MibScalar
ipxInDiscards = _IpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 13),
    _IpxInDiscards_Type()
)
ipxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInDiscards.setStatus("mandatory")
_IpxOutDiscards_Type = Counter32
_IpxOutDiscards_Object = MibScalar
ipxOutDiscards = _IpxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 14),
    _IpxOutDiscards_Type()
)
ipxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutDiscards.setStatus("mandatory")
_IpxOtherDiscards_Type = Counter32
_IpxOtherDiscards_Object = MibScalar
ipxOtherDiscards = _IpxOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 1, 15),
    _IpxOtherDiscards_Type()
)
ipxOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOtherDiscards.setStatus("mandatory")
_Decnet_ObjectIdentity = ObjectIdentity
decnet = _Decnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 13, 2)
)


class _DcntRouting_Type(Integer32):
    """Custom type dcntRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DcntRouting_Type.__name__ = "Integer32"
_DcntRouting_Object = MibScalar
dcntRouting = _DcntRouting_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 1),
    _DcntRouting_Type()
)
dcntRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntRouting.setStatus("mandatory")
_DcntIfNumber_Type = Integer32
_DcntIfNumber_Object = MibScalar
dcntIfNumber = _DcntIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 2),
    _DcntIfNumber_Type()
)
dcntIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntIfNumber.setStatus("mandatory")
_DcntIfTable_Object = MibTable
dcntIfTable = _DcntIfTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 3)
)
if mibBuilder.loadTexts:
    dcntIfTable.setStatus("mandatory")
_DcntIfTableEntry_Object = MibTableRow
dcntIfTableEntry = _DcntIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 3, 1)
)
dcntIfTableEntry.setIndexNames(
    (0, "RETIX-MIB", "dcntIfIndex"),
)
if mibBuilder.loadTexts:
    dcntIfTableEntry.setStatus("mandatory")
_DcntIfIndex_Type = Integer32
_DcntIfIndex_Object = MibTableColumn
dcntIfIndex = _DcntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 3, 1, 1),
    _DcntIfIndex_Type()
)
dcntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntIfIndex.setStatus("mandatory")


class _DcntIfCost_Type(Integer32):
    """Custom type dcntIfCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DcntIfCost_Type.__name__ = "Integer32"
_DcntIfCost_Object = MibTableColumn
dcntIfCost = _DcntIfCost_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 3, 1, 2),
    _DcntIfCost_Type()
)
dcntIfCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntIfCost.setStatus("mandatory")


class _DcntIfRtrPriority_Type(Integer32):
    """Custom type dcntIfRtrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DcntIfRtrPriority_Type.__name__ = "Integer32"
_DcntIfRtrPriority_Object = MibTableColumn
dcntIfRtrPriority = _DcntIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 3, 1, 3),
    _DcntIfRtrPriority_Type()
)
dcntIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntIfRtrPriority.setStatus("mandatory")


class _DcntIfDesgntdRtr_Type(Integer32):
    """Custom type dcntIfDesgntdRtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DcntIfDesgntdRtr_Type.__name__ = "Integer32"
_DcntIfDesgntdRtr_Object = MibTableColumn
dcntIfDesgntdRtr = _DcntIfDesgntdRtr_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 3, 1, 4),
    _DcntIfDesgntdRtr_Type()
)
dcntIfDesgntdRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntIfDesgntdRtr.setStatus("mandatory")


class _DcntIfHelloTimerBCT3_Type(Integer32):
    """Custom type dcntIfHelloTimerBCT3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_DcntIfHelloTimerBCT3_Type.__name__ = "Integer32"
_DcntIfHelloTimerBCT3_Object = MibTableColumn
dcntIfHelloTimerBCT3 = _DcntIfHelloTimerBCT3_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 3, 1, 5),
    _DcntIfHelloTimerBCT3_Type()
)
dcntIfHelloTimerBCT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntIfHelloTimerBCT3.setStatus("mandatory")
_DcntRoutingTable_Object = MibTable
dcntRoutingTable = _DcntRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 4)
)
if mibBuilder.loadTexts:
    dcntRoutingTable.setStatus("mandatory")
_DcntRITEntry_Object = MibTableRow
dcntRITEntry = _DcntRITEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 4, 1)
)
dcntRITEntry.setIndexNames(
    (0, "RETIX-MIB", "dcntRITDestNode"),
)
if mibBuilder.loadTexts:
    dcntRITEntry.setStatus("mandatory")
_DcntRITDestNode_Type = Integer32
_DcntRITDestNode_Object = MibTableColumn
dcntRITDestNode = _DcntRITDestNode_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 4, 1, 1),
    _DcntRITDestNode_Type()
)
dcntRITDestNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntRITDestNode.setStatus("mandatory")
_DcntRITNextHop_Type = OctetString
_DcntRITNextHop_Object = MibTableColumn
dcntRITNextHop = _DcntRITNextHop_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 4, 1, 2),
    _DcntRITNextHop_Type()
)
dcntRITNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntRITNextHop.setStatus("mandatory")
_DcntRITCost_Type = Integer32
_DcntRITCost_Object = MibTableColumn
dcntRITCost = _DcntRITCost_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 4, 1, 3),
    _DcntRITCost_Type()
)
dcntRITCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntRITCost.setStatus("mandatory")
_DcntRITHops_Type = Integer32
_DcntRITHops_Object = MibTableColumn
dcntRITHops = _DcntRITHops_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 4, 1, 4),
    _DcntRITHops_Type()
)
dcntRITHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntRITHops.setStatus("mandatory")
_DcntRITInterface_Type = Integer32
_DcntRITInterface_Object = MibTableColumn
dcntRITInterface = _DcntRITInterface_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 4, 1, 5),
    _DcntRITInterface_Type()
)
dcntRITInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntRITInterface.setStatus("mandatory")
_DcntAreaRoutingTable_Object = MibTable
dcntAreaRoutingTable = _DcntAreaRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 5)
)
if mibBuilder.loadTexts:
    dcntAreaRoutingTable.setStatus("mandatory")
_DcntAreaRITEntry_Object = MibTableRow
dcntAreaRITEntry = _DcntAreaRITEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 5, 1)
)
dcntAreaRITEntry.setIndexNames(
    (0, "RETIX-MIB", "dcntAreaRITDestArea"),
)
if mibBuilder.loadTexts:
    dcntAreaRITEntry.setStatus("mandatory")
_DcntAreaRITDestArea_Type = Integer32
_DcntAreaRITDestArea_Object = MibTableColumn
dcntAreaRITDestArea = _DcntAreaRITDestArea_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 5, 1, 1),
    _DcntAreaRITDestArea_Type()
)
dcntAreaRITDestArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntAreaRITDestArea.setStatus("mandatory")
_DcntAreaRITNextHop_Type = OctetString
_DcntAreaRITNextHop_Object = MibTableColumn
dcntAreaRITNextHop = _DcntAreaRITNextHop_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 5, 1, 2),
    _DcntAreaRITNextHop_Type()
)
dcntAreaRITNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntAreaRITNextHop.setStatus("mandatory")
_DcntAreaRITCost_Type = Integer32
_DcntAreaRITCost_Object = MibTableColumn
dcntAreaRITCost = _DcntAreaRITCost_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 5, 1, 3),
    _DcntAreaRITCost_Type()
)
dcntAreaRITCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntAreaRITCost.setStatus("mandatory")
_DcntAreaRITHops_Type = Integer32
_DcntAreaRITHops_Object = MibTableColumn
dcntAreaRITHops = _DcntAreaRITHops_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 5, 1, 4),
    _DcntAreaRITHops_Type()
)
dcntAreaRITHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntAreaRITHops.setStatus("mandatory")
_DcntAreaRITInterface_Type = Integer32
_DcntAreaRITInterface_Object = MibTableColumn
dcntAreaRITInterface = _DcntAreaRITInterface_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 5, 1, 5),
    _DcntAreaRITInterface_Type()
)
dcntAreaRITInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntAreaRITInterface.setStatus("mandatory")
_DcntNodeAddress_Type = OctetString
_DcntNodeAddress_Object = MibScalar
dcntNodeAddress = _DcntNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 6),
    _DcntNodeAddress_Type()
)
dcntNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntNodeAddress.setStatus("mandatory")


class _DcntInterAreaMaxCost_Type(Integer32):
    """Custom type dcntInterAreaMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DcntInterAreaMaxCost_Type.__name__ = "Integer32"
_DcntInterAreaMaxCost_Object = MibScalar
dcntInterAreaMaxCost = _DcntInterAreaMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 7),
    _DcntInterAreaMaxCost_Type()
)
dcntInterAreaMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntInterAreaMaxCost.setStatus("mandatory")


class _DcntInterAreaMaxHops_Type(Integer32):
    """Custom type dcntInterAreaMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DcntInterAreaMaxHops_Type.__name__ = "Integer32"
_DcntInterAreaMaxHops_Object = MibScalar
dcntInterAreaMaxHops = _DcntInterAreaMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 8),
    _DcntInterAreaMaxHops_Type()
)
dcntInterAreaMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntInterAreaMaxHops.setStatus("mandatory")


class _DcntIntraAreaMaxCost_Type(Integer32):
    """Custom type dcntIntraAreaMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DcntIntraAreaMaxCost_Type.__name__ = "Integer32"
_DcntIntraAreaMaxCost_Object = MibScalar
dcntIntraAreaMaxCost = _DcntIntraAreaMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 9),
    _DcntIntraAreaMaxCost_Type()
)
dcntIntraAreaMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntIntraAreaMaxCost.setStatus("mandatory")


class _DcntIntraAreaMaxHops_Type(Integer32):
    """Custom type dcntIntraAreaMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DcntIntraAreaMaxHops_Type.__name__ = "Integer32"
_DcntIntraAreaMaxHops_Object = MibScalar
dcntIntraAreaMaxHops = _DcntIntraAreaMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 10),
    _DcntIntraAreaMaxHops_Type()
)
dcntIntraAreaMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntIntraAreaMaxHops.setStatus("mandatory")


class _DcntMaxVisits_Type(Integer32):
    """Custom type dcntMaxVisits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DcntMaxVisits_Type.__name__ = "Integer32"
_DcntMaxVisits_Object = MibScalar
dcntMaxVisits = _DcntMaxVisits_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 11),
    _DcntMaxVisits_Type()
)
dcntMaxVisits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntMaxVisits.setStatus("mandatory")


class _DcntRtngMsgTimerBCT1_Type(Integer32):
    """Custom type dcntRtngMsgTimerBCT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_DcntRtngMsgTimerBCT1_Type.__name__ = "Integer32"
_DcntRtngMsgTimerBCT1_Object = MibScalar
dcntRtngMsgTimerBCT1 = _DcntRtngMsgTimerBCT1_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 12),
    _DcntRtngMsgTimerBCT1_Type()
)
dcntRtngMsgTimerBCT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntRtngMsgTimerBCT1.setStatus("mandatory")


class _DcntRateControlFreqTimerT2_Type(Integer32):
    """Custom type dcntRateControlFreqTimerT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DcntRateControlFreqTimerT2_Type.__name__ = "Integer32"
_DcntRateControlFreqTimerT2_Object = MibScalar
dcntRateControlFreqTimerT2 = _DcntRateControlFreqTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 13),
    _DcntRateControlFreqTimerT2_Type()
)
dcntRateControlFreqTimerT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcntRateControlFreqTimerT2.setStatus("mandatory")
_DcntReveivedDgms_Type = Counter32
_DcntReveivedDgms_Object = MibScalar
dcntReveivedDgms = _DcntReveivedDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 14),
    _DcntReveivedDgms_Type()
)
dcntReveivedDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntReveivedDgms.setStatus("mandatory")
_DcntForwardedDgms_Type = Counter32
_DcntForwardedDgms_Object = MibScalar
dcntForwardedDgms = _DcntForwardedDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 15),
    _DcntForwardedDgms_Type()
)
dcntForwardedDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntForwardedDgms.setStatus("mandatory")
_DcntOutRequestedDgms_Type = Counter32
_DcntOutRequestedDgms_Object = MibScalar
dcntOutRequestedDgms = _DcntOutRequestedDgms_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 16),
    _DcntOutRequestedDgms_Type()
)
dcntOutRequestedDgms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntOutRequestedDgms.setStatus("mandatory")
_DcntInDiscards_Type = Counter32
_DcntInDiscards_Object = MibScalar
dcntInDiscards = _DcntInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 17),
    _DcntInDiscards_Type()
)
dcntInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntInDiscards.setStatus("mandatory")
_DcntOutDiscards_Type = Counter32
_DcntOutDiscards_Object = MibScalar
dcntOutDiscards = _DcntOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 18),
    _DcntOutDiscards_Type()
)
dcntOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntOutDiscards.setStatus("mandatory")
_DcntNoRoutes_Type = Counter32
_DcntNoRoutes_Object = MibScalar
dcntNoRoutes = _DcntNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 19),
    _DcntNoRoutes_Type()
)
dcntNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntNoRoutes.setStatus("mandatory")
_DcntInHdrErrors_Type = Counter32
_DcntInHdrErrors_Object = MibScalar
dcntInHdrErrors = _DcntInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 2, 20),
    _DcntInHdrErrors_Type()
)
dcntInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcntInHdrErrors.setStatus("mandatory")
_RmtLapb_ObjectIdentity = ObjectIdentity
rmtLapb = _RmtLapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 13, 3)
)
_RmtLapbConfigTable_Object = MibTable
rmtLapbConfigTable = _RmtLapbConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1)
)
if mibBuilder.loadTexts:
    rmtLapbConfigTable.setStatus("mandatory")
_RmtLapbCTEntry_Object = MibTableRow
rmtLapbCTEntry = _RmtLapbCTEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1)
)
rmtLapbCTEntry.setIndexNames(
    (0, "RETIX-MIB", "rmtLapbCTIndex"),
)
if mibBuilder.loadTexts:
    rmtLapbCTEntry.setStatus("mandatory")
_RmtLapbCTIndex_Type = Integer32
_RmtLapbCTIndex_Object = MibTableColumn
rmtLapbCTIndex = _RmtLapbCTIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 1),
    _RmtLapbCTIndex_Type()
)
rmtLapbCTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbCTIndex.setStatus("mandatory")


class _RmtLapbCTLinkAddr_Type(Integer32):
    """Custom type rmtLapbCTLinkAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmtLapbCTLinkAddr_Type.__name__ = "Integer32"
_RmtLapbCTLinkAddr_Object = MibTableColumn
rmtLapbCTLinkAddr = _RmtLapbCTLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 2),
    _RmtLapbCTLinkAddr_Type()
)
rmtLapbCTLinkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTLinkAddr.setStatus("mandatory")


class _RmtLapbCTExtSeqNumbering_Type(Integer32):
    """Custom type rmtLapbCTExtSeqNumbering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmtLapbCTExtSeqNumbering_Type.__name__ = "Integer32"
_RmtLapbCTExtSeqNumbering_Object = MibTableColumn
rmtLapbCTExtSeqNumbering = _RmtLapbCTExtSeqNumbering_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 3),
    _RmtLapbCTExtSeqNumbering_Type()
)
rmtLapbCTExtSeqNumbering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTExtSeqNumbering.setStatus("mandatory")


class _RmtLapbCTWindow_Type(Integer32):
    """Custom type rmtLapbCTWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_RmtLapbCTWindow_Type.__name__ = "Integer32"
_RmtLapbCTWindow_Object = MibTableColumn
rmtLapbCTWindow = _RmtLapbCTWindow_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 4),
    _RmtLapbCTWindow_Type()
)
rmtLapbCTWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTWindow.setStatus("mandatory")


class _RmtLapbCTModeT1_Type(Integer32):
    """Custom type rmtLapbCTModeT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmtLapbCTModeT1_Type.__name__ = "Integer32"
_RmtLapbCTModeT1_Object = MibTableColumn
rmtLapbCTModeT1 = _RmtLapbCTModeT1_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 5),
    _RmtLapbCTModeT1_Type()
)
rmtLapbCTModeT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTModeT1.setStatus("mandatory")


class _RmtLapbCTManualT1Value_Type(Integer32):
    """Custom type rmtLapbCTManualT1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_RmtLapbCTManualT1Value_Type.__name__ = "Integer32"
_RmtLapbCTManualT1Value_Object = MibTableColumn
rmtLapbCTManualT1Value = _RmtLapbCTManualT1Value_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 6),
    _RmtLapbCTManualT1Value_Type()
)
rmtLapbCTManualT1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTManualT1Value.setStatus("mandatory")


class _RmtLapbCTT3LinkIdleTimer_Type(Integer32):
    """Custom type rmtLapbCTT3LinkIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmtLapbCTT3LinkIdleTimer_Type.__name__ = "Integer32"
_RmtLapbCTT3LinkIdleTimer_Object = MibTableColumn
rmtLapbCTT3LinkIdleTimer = _RmtLapbCTT3LinkIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 7),
    _RmtLapbCTT3LinkIdleTimer_Type()
)
rmtLapbCTT3LinkIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTT3LinkIdleTimer.setStatus("mandatory")


class _RmtLapbCTN2RetryCount_Type(Integer32):
    """Custom type rmtLapbCTN2RetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmtLapbCTN2RetryCount_Type.__name__ = "Integer32"
_RmtLapbCTN2RetryCount_Object = MibTableColumn
rmtLapbCTN2RetryCount = _RmtLapbCTN2RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 8),
    _RmtLapbCTN2RetryCount_Type()
)
rmtLapbCTN2RetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTN2RetryCount.setStatus("mandatory")


class _RmtLapbCTLinkReset_Type(Integer32):
    """Custom type rmtLapbCTLinkReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetLink", 2))
    )


_RmtLapbCTLinkReset_Type.__name__ = "Integer32"
_RmtLapbCTLinkReset_Object = MibTableColumn
rmtLapbCTLinkReset = _RmtLapbCTLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 9),
    _RmtLapbCTLinkReset_Type()
)
rmtLapbCTLinkReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTLinkReset.setStatus("mandatory")


class _RmtLapbCTX25PortLineSpeed_Type(Integer32):
    """Custom type rmtLapbCTX25PortLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200,
              32000,
              48000,
              64000)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b32000", 32000),
          ("b4800", 4800),
          ("b48000", 48000),
          ("b64000", 64000),
          ("b9600", 9600))
    )


_RmtLapbCTX25PortLineSpeed_Type.__name__ = "Integer32"
_RmtLapbCTX25PortLineSpeed_Object = MibTableColumn
rmtLapbCTX25PortLineSpeed = _RmtLapbCTX25PortLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 10),
    _RmtLapbCTX25PortLineSpeed_Type()
)
rmtLapbCTX25PortLineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTX25PortLineSpeed.setStatus("mandatory")


class _RmtLapbCTInitLinkConnect_Type(Integer32):
    """Custom type rmtLapbCTInitLinkConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 2),
          ("noAction", 1))
    )


_RmtLapbCTInitLinkConnect_Type.__name__ = "Integer32"
_RmtLapbCTInitLinkConnect_Object = MibTableColumn
rmtLapbCTInitLinkConnect = _RmtLapbCTInitLinkConnect_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 1, 1, 11),
    _RmtLapbCTInitLinkConnect_Type()
)
rmtLapbCTInitLinkConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmtLapbCTInitLinkConnect.setStatus("mandatory")
_RmtLapbStatsTable_Object = MibTable
rmtLapbStatsTable = _RmtLapbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2)
)
if mibBuilder.loadTexts:
    rmtLapbStatsTable.setStatus("mandatory")
_RmtLapbSTEntry_Object = MibTableRow
rmtLapbSTEntry = _RmtLapbSTEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1)
)
rmtLapbSTEntry.setIndexNames(
    (0, "RETIX-MIB", "rmtLapbSTIndex"),
)
if mibBuilder.loadTexts:
    rmtLapbSTEntry.setStatus("mandatory")
_RmtLapbSTIndex_Type = Integer32
_RmtLapbSTIndex_Object = MibTableColumn
rmtLapbSTIndex = _RmtLapbSTIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 1),
    _RmtLapbSTIndex_Type()
)
rmtLapbSTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTIndex.setStatus("mandatory")


class _RmtLapbSTState_Type(Integer32):
    """Custom type rmtLapbSTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_RmtLapbSTState_Type.__name__ = "Integer32"
_RmtLapbSTState_Object = MibTableColumn
rmtLapbSTState = _RmtLapbSTState_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 2),
    _RmtLapbSTState_Type()
)
rmtLapbSTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTState.setStatus("mandatory")
_RmtLapbSTAutoT1value_Type = Integer32
_RmtLapbSTAutoT1value_Object = MibTableColumn
rmtLapbSTAutoT1value = _RmtLapbSTAutoT1value_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 3),
    _RmtLapbSTAutoT1value_Type()
)
rmtLapbSTAutoT1value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTAutoT1value.setStatus("mandatory")


class _RmtLapbSTLastResetTime_Type(OctetString):
    """Custom type rmtLapbSTLastResetTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_RmtLapbSTLastResetTime_Type.__name__ = "OctetString"
_RmtLapbSTLastResetTime_Object = MibTableColumn
rmtLapbSTLastResetTime = _RmtLapbSTLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 4),
    _RmtLapbSTLastResetTime_Type()
)
rmtLapbSTLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTLastResetTime.setStatus("mandatory")


class _RmtLapbSTLastResetReason_Type(Integer32):
    """Custom type rmtLapbSTLastResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RmtLapbSTLastResetReason_Type.__name__ = "Integer32"
_RmtLapbSTLastResetReason_Object = MibTableColumn
rmtLapbSTLastResetReason = _RmtLapbSTLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 5),
    _RmtLapbSTLastResetReason_Type()
)
rmtLapbSTLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTLastResetReason.setStatus("mandatory")
_RmtLapbSTCountResets_Type = Counter32
_RmtLapbSTCountResets_Object = MibTableColumn
rmtLapbSTCountResets = _RmtLapbSTCountResets_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 6),
    _RmtLapbSTCountResets_Type()
)
rmtLapbSTCountResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTCountResets.setStatus("mandatory")
_RmtLapbSTCountSentFrames_Type = Counter32
_RmtLapbSTCountSentFrames_Object = MibTableColumn
rmtLapbSTCountSentFrames = _RmtLapbSTCountSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 7),
    _RmtLapbSTCountSentFrames_Type()
)
rmtLapbSTCountSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTCountSentFrames.setStatus("mandatory")
_RmtLapbSTCountRcvFrames_Type = Counter32
_RmtLapbSTCountRcvFrames_Object = MibTableColumn
rmtLapbSTCountRcvFrames = _RmtLapbSTCountRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 8),
    _RmtLapbSTCountRcvFrames_Type()
)
rmtLapbSTCountRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTCountRcvFrames.setStatus("mandatory")
_RmtLapbSTCountSentOctets_Type = Counter32
_RmtLapbSTCountSentOctets_Object = MibTableColumn
rmtLapbSTCountSentOctets = _RmtLapbSTCountSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 9),
    _RmtLapbSTCountSentOctets_Type()
)
rmtLapbSTCountSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTCountSentOctets.setStatus("mandatory")
_RmtLapbSTCountRcvOctets_Type = Counter32
_RmtLapbSTCountRcvOctets_Object = MibTableColumn
rmtLapbSTCountRcvOctets = _RmtLapbSTCountRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 10),
    _RmtLapbSTCountRcvOctets_Type()
)
rmtLapbSTCountRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTCountRcvOctets.setStatus("mandatory")
_RmtLapbSTCountAborts_Type = Counter32
_RmtLapbSTCountAborts_Object = MibTableColumn
rmtLapbSTCountAborts = _RmtLapbSTCountAborts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 11),
    _RmtLapbSTCountAborts_Type()
)
rmtLapbSTCountAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTCountAborts.setStatus("mandatory")
_RmtLapbSTCountCrcErrors_Type = Counter32
_RmtLapbSTCountCrcErrors_Object = MibTableColumn
rmtLapbSTCountCrcErrors = _RmtLapbSTCountCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 3, 2, 1, 12),
    _RmtLapbSTCountCrcErrors_Type()
)
rmtLapbSTCountCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmtLapbSTCountCrcErrors.setStatus("mandatory")
_X25_ObjectIdentity = ObjectIdentity
x25 = _X25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 72, 13, 4)
)


class _X25Operation_Type(Integer32):
    """Custom type x25Operation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25Operation_Type.__name__ = "Integer32"
_X25Operation_Object = MibScalar
x25Operation = _X25Operation_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 1),
    _X25Operation_Type()
)
x25Operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Operation.setStatus("mandatory")


class _X25OperNextReset_Type(Integer32):
    """Custom type x25OperNextReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25OperNextReset_Type.__name__ = "Integer32"
_X25OperNextReset_Object = MibScalar
x25OperNextReset = _X25OperNextReset_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 2),
    _X25OperNextReset_Type()
)
x25OperNextReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25OperNextReset.setStatus("mandatory")
_X25ConSetupTable_Object = MibTable
x25ConSetupTable = _X25ConSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3)
)
if mibBuilder.loadTexts:
    x25ConSetupTable.setStatus("mandatory")
_X25CSTEntry_Object = MibTableRow
x25CSTEntry = _X25CSTEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1)
)
x25CSTEntry.setIndexNames(
    (0, "RETIX-MIB", "x25CSTIndex"),
)
if mibBuilder.loadTexts:
    x25CSTEntry.setStatus("mandatory")
_X25CSTIndex_Type = Integer32
_X25CSTIndex_Object = MibTableColumn
x25CSTIndex = _X25CSTIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 1),
    _X25CSTIndex_Type()
)
x25CSTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CSTIndex.setStatus("mandatory")
_X25CST8084Switch_Type = Integer32
_X25CST8084Switch_Object = MibTableColumn
x25CST8084Switch = _X25CST8084Switch_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 2),
    _X25CST8084Switch_Type()
)
x25CST8084Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CST8084Switch.setStatus("mandatory")


class _X25CSTSrcDTEAddr_Type(OctetString):
    """Custom type x25CSTSrcDTEAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_X25CSTSrcDTEAddr_Type.__name__ = "OctetString"
_X25CSTSrcDTEAddr_Object = MibTableColumn
x25CSTSrcDTEAddr = _X25CSTSrcDTEAddr_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 3),
    _X25CSTSrcDTEAddr_Type()
)
x25CSTSrcDTEAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTSrcDTEAddr.setStatus("mandatory")


class _X25CSTDestDTEAddr_Type(OctetString):
    """Custom type x25CSTDestDTEAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_X25CSTDestDTEAddr_Type.__name__ = "OctetString"
_X25CSTDestDTEAddr_Object = MibTableColumn
x25CSTDestDTEAddr = _X25CSTDestDTEAddr_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 4),
    _X25CSTDestDTEAddr_Type()
)
x25CSTDestDTEAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTDestDTEAddr.setStatus("mandatory")


class _X25CST2WayLgclChanNum_Type(Integer32):
    """Custom type x25CST2WayLgclChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_X25CST2WayLgclChanNum_Type.__name__ = "Integer32"
_X25CST2WayLgclChanNum_Object = MibTableColumn
x25CST2WayLgclChanNum = _X25CST2WayLgclChanNum_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 5),
    _X25CST2WayLgclChanNum_Type()
)
x25CST2WayLgclChanNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CST2WayLgclChanNum.setStatus("mandatory")


class _X25CSTPktSeqNumFlg_Type(Integer32):
    """Custom type x25CSTPktSeqNumFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mod128", 4),
          ("mod8", 1))
    )


_X25CSTPktSeqNumFlg_Type.__name__ = "Integer32"
_X25CSTPktSeqNumFlg_Object = MibTableColumn
x25CSTPktSeqNumFlg = _X25CSTPktSeqNumFlg_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 6),
    _X25CSTPktSeqNumFlg_Type()
)
x25CSTPktSeqNumFlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTPktSeqNumFlg.setStatus("mandatory")


class _X25CSTFlowCntrlNeg_Type(Integer32):
    """Custom type x25CSTFlowCntrlNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25CSTFlowCntrlNeg_Type.__name__ = "Integer32"
_X25CSTFlowCntrlNeg_Object = MibTableColumn
x25CSTFlowCntrlNeg = _X25CSTFlowCntrlNeg_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 7),
    _X25CSTFlowCntrlNeg_Type()
)
x25CSTFlowCntrlNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTFlowCntrlNeg.setStatus("mandatory")


class _X25CSTDefaultWinSize_Type(Integer32):
    """Custom type x25CSTDefaultWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25CSTDefaultWinSize_Type.__name__ = "Integer32"
_X25CSTDefaultWinSize_Object = MibTableColumn
x25CSTDefaultWinSize = _X25CSTDefaultWinSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 8),
    _X25CSTDefaultWinSize_Type()
)
x25CSTDefaultWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTDefaultWinSize.setStatus("mandatory")
_X25CSTDefaultPktSize_Type = Integer32
_X25CSTDefaultPktSize_Object = MibTableColumn
x25CSTDefaultPktSize = _X25CSTDefaultPktSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 9),
    _X25CSTDefaultPktSize_Type()
)
x25CSTDefaultPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTDefaultPktSize.setStatus("mandatory")


class _X25CSTNegWinSize_Type(Integer32):
    """Custom type x25CSTNegWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_X25CSTNegWinSize_Type.__name__ = "Integer32"
_X25CSTNegWinSize_Object = MibTableColumn
x25CSTNegWinSize = _X25CSTNegWinSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 10),
    _X25CSTNegWinSize_Type()
)
x25CSTNegWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTNegWinSize.setStatus("mandatory")
_X25CSTNegPktSize_Type = Integer32
_X25CSTNegPktSize_Object = MibTableColumn
x25CSTNegPktSize = _X25CSTNegPktSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 11),
    _X25CSTNegPktSize_Type()
)
x25CSTNegPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTNegPktSize.setStatus("mandatory")


class _X25CSTCUGSub_Type(Integer32):
    """Custom type x25CSTCUGSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_X25CSTCUGSub_Type.__name__ = "Integer32"
_X25CSTCUGSub_Object = MibTableColumn
x25CSTCUGSub = _X25CSTCUGSub_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 12),
    _X25CSTCUGSub_Type()
)
x25CSTCUGSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTCUGSub.setStatus("mandatory")


class _X25CSTLclCUGValue_Type(Integer32):
    """Custom type x25CSTLclCUGValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_X25CSTLclCUGValue_Type.__name__ = "Integer32"
_X25CSTLclCUGValue_Object = MibTableColumn
x25CSTLclCUGValue = _X25CSTLclCUGValue_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 13),
    _X25CSTLclCUGValue_Type()
)
x25CSTLclCUGValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTLclCUGValue.setStatus("mandatory")


class _X25CSTRvrsChrgReq_Type(Integer32):
    """Custom type x25CSTRvrsChrgReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25CSTRvrsChrgReq_Type.__name__ = "Integer32"
_X25CSTRvrsChrgReq_Object = MibTableColumn
x25CSTRvrsChrgReq = _X25CSTRvrsChrgReq_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 14),
    _X25CSTRvrsChrgReq_Type()
)
x25CSTRvrsChrgReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTRvrsChrgReq.setStatus("mandatory")


class _X25CSTRvrsChrgAcc_Type(Integer32):
    """Custom type x25CSTRvrsChrgAcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25CSTRvrsChrgAcc_Type.__name__ = "Integer32"
_X25CSTRvrsChrgAcc_Object = MibTableColumn
x25CSTRvrsChrgAcc = _X25CSTRvrsChrgAcc_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 3, 1, 15),
    _X25CSTRvrsChrgAcc_Type()
)
x25CSTRvrsChrgAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CSTRvrsChrgAcc.setStatus("mandatory")
_X25ConControlTable_Object = MibTable
x25ConControlTable = _X25ConControlTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4)
)
if mibBuilder.loadTexts:
    x25ConControlTable.setStatus("mandatory")
_X25CCTEntry_Object = MibTableRow
x25CCTEntry = _X25CCTEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1)
)
x25CCTEntry.setIndexNames(
    (0, "RETIX-MIB", "x25CCTIndex"),
)
if mibBuilder.loadTexts:
    x25CCTEntry.setStatus("mandatory")
_X25CCTIndex_Type = Integer32
_X25CCTIndex_Object = MibTableColumn
x25CCTIndex = _X25CCTIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 1),
    _X25CCTIndex_Type()
)
x25CCTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CCTIndex.setStatus("mandatory")


class _X25CCTManualConnect_Type(Integer32):
    """Custom type x25CCTManualConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 2),
          ("noAction", 1))
    )


_X25CCTManualConnect_Type.__name__ = "Integer32"
_X25CCTManualConnect_Object = MibTableColumn
x25CCTManualConnect = _X25CCTManualConnect_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 2),
    _X25CCTManualConnect_Type()
)
x25CCTManualConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTManualConnect.setStatus("mandatory")


class _X25CCTManualDisconnect_Type(Integer32):
    """Custom type x25CCTManualDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 2),
          ("noAction", 1))
    )


_X25CCTManualDisconnect_Type.__name__ = "Integer32"
_X25CCTManualDisconnect_Object = MibTableColumn
x25CCTManualDisconnect = _X25CCTManualDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 3),
    _X25CCTManualDisconnect_Type()
)
x25CCTManualDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTManualDisconnect.setStatus("mandatory")


class _X25CCTCfgAutoConRetry_Type(Integer32):
    """Custom type x25CCTCfgAutoConRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25CCTCfgAutoConRetry_Type.__name__ = "Integer32"
_X25CCTCfgAutoConRetry_Object = MibTableColumn
x25CCTCfgAutoConRetry = _X25CCTCfgAutoConRetry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 4),
    _X25CCTCfgAutoConRetry_Type()
)
x25CCTCfgAutoConRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTCfgAutoConRetry.setStatus("mandatory")


class _X25CCTOperAutoConRetryFlg_Type(Integer32):
    """Custom type x25CCTOperAutoConRetryFlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25CCTOperAutoConRetryFlg_Type.__name__ = "Integer32"
_X25CCTOperAutoConRetryFlg_Object = MibTableColumn
x25CCTOperAutoConRetryFlg = _X25CCTOperAutoConRetryFlg_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 5),
    _X25CCTOperAutoConRetryFlg_Type()
)
x25CCTOperAutoConRetryFlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25CCTOperAutoConRetryFlg.setStatus("mandatory")


class _X25CCTAutoConRetryTimer_Type(Integer32):
    """Custom type x25CCTAutoConRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_X25CCTAutoConRetryTimer_Type.__name__ = "Integer32"
_X25CCTAutoConRetryTimer_Object = MibTableColumn
x25CCTAutoConRetryTimer = _X25CCTAutoConRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 6),
    _X25CCTAutoConRetryTimer_Type()
)
x25CCTAutoConRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTAutoConRetryTimer.setStatus("mandatory")


class _X25CCTMaxAutoConRetries_Type(Integer32):
    """Custom type x25CCTMaxAutoConRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25CCTMaxAutoConRetries_Type.__name__ = "Integer32"
_X25CCTMaxAutoConRetries_Object = MibTableColumn
x25CCTMaxAutoConRetries = _X25CCTMaxAutoConRetries_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 7),
    _X25CCTMaxAutoConRetries_Type()
)
x25CCTMaxAutoConRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTMaxAutoConRetries.setStatus("mandatory")


class _X25CCTCfgTODControl_Type(Integer32):
    """Custom type x25CCTCfgTODControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25CCTCfgTODControl_Type.__name__ = "Integer32"
_X25CCTCfgTODControl_Object = MibTableColumn
x25CCTCfgTODControl = _X25CCTCfgTODControl_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 8),
    _X25CCTCfgTODControl_Type()
)
x25CCTCfgTODControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTCfgTODControl.setStatus("mandatory")


class _X25CCTCurrentTODControl_Type(Integer32):
    """Custom type x25CCTCurrentTODControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_X25CCTCurrentTODControl_Type.__name__ = "Integer32"
_X25CCTCurrentTODControl_Object = MibTableColumn
x25CCTCurrentTODControl = _X25CCTCurrentTODControl_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 9),
    _X25CCTCurrentTODControl_Type()
)
x25CCTCurrentTODControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTCurrentTODControl.setStatus("mandatory")


class _X25CCTTODToConnect_Type(OctetString):
    """Custom type x25CCTTODToConnect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_X25CCTTODToConnect_Type.__name__ = "OctetString"
_X25CCTTODToConnect_Object = MibTableColumn
x25CCTTODToConnect = _X25CCTTODToConnect_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 10),
    _X25CCTTODToConnect_Type()
)
x25CCTTODToConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTTODToConnect.setStatus("mandatory")


class _X25CCTTODToDisconnect_Type(OctetString):
    """Custom type x25CCTTODToDisconnect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_X25CCTTODToDisconnect_Type.__name__ = "OctetString"
_X25CCTTODToDisconnect_Object = MibTableColumn
x25CCTTODToDisconnect = _X25CCTTODToDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 4, 1, 11),
    _X25CCTTODToDisconnect_Type()
)
x25CCTTODToDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25CCTTODToDisconnect.setStatus("mandatory")
_X25TimerTable_Object = MibTable
x25TimerTable = _X25TimerTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5)
)
if mibBuilder.loadTexts:
    x25TimerTable.setStatus("mandatory")
_X25TTEntry_Object = MibTableRow
x25TTEntry = _X25TTEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1)
)
x25TTEntry.setIndexNames(
    (0, "RETIX-MIB", "x25TTIndex"),
)
if mibBuilder.loadTexts:
    x25TTEntry.setStatus("mandatory")
_X25TTIndex_Type = Integer32
_X25TTIndex_Object = MibTableColumn
x25TTIndex = _X25TTIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 1),
    _X25TTIndex_Type()
)
x25TTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25TTIndex.setStatus("mandatory")


class _X25TTT20Timer_Type(Integer32):
    """Custom type x25TTT20Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_X25TTT20Timer_Type.__name__ = "Integer32"
_X25TTT20Timer_Object = MibTableColumn
x25TTT20Timer = _X25TTT20Timer_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 2),
    _X25TTT20Timer_Type()
)
x25TTT20Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25TTT20Timer.setStatus("mandatory")


class _X25TTT21Timer_Type(Integer32):
    """Custom type x25TTT21Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_X25TTT21Timer_Type.__name__ = "Integer32"
_X25TTT21Timer_Object = MibTableColumn
x25TTT21Timer = _X25TTT21Timer_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 3),
    _X25TTT21Timer_Type()
)
x25TTT21Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25TTT21Timer.setStatus("mandatory")


class _X25TTT22Timer_Type(Integer32):
    """Custom type x25TTT22Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_X25TTT22Timer_Type.__name__ = "Integer32"
_X25TTT22Timer_Object = MibTableColumn
x25TTT22Timer = _X25TTT22Timer_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 4),
    _X25TTT22Timer_Type()
)
x25TTT22Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25TTT22Timer.setStatus("mandatory")


class _X25TTT23Timer_Type(Integer32):
    """Custom type x25TTT23Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_X25TTT23Timer_Type.__name__ = "Integer32"
_X25TTT23Timer_Object = MibTableColumn
x25TTT23Timer = _X25TTT23Timer_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 5),
    _X25TTT23Timer_Type()
)
x25TTT23Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25TTT23Timer.setStatus("mandatory")


class _X25TTR20Limit_Type(Integer32):
    """Custom type x25TTR20Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_X25TTR20Limit_Type.__name__ = "Integer32"
_X25TTR20Limit_Object = MibTableColumn
x25TTR20Limit = _X25TTR20Limit_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 6),
    _X25TTR20Limit_Type()
)
x25TTR20Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25TTR20Limit.setStatus("mandatory")


class _X25TTR22Limit_Type(Integer32):
    """Custom type x25TTR22Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_X25TTR22Limit_Type.__name__ = "Integer32"
_X25TTR22Limit_Object = MibTableColumn
x25TTR22Limit = _X25TTR22Limit_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 7),
    _X25TTR22Limit_Type()
)
x25TTR22Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25TTR22Limit.setStatus("mandatory")


class _X25TTR23Limit_Type(Integer32):
    """Custom type x25TTR23Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_X25TTR23Limit_Type.__name__ = "Integer32"
_X25TTR23Limit_Object = MibTableColumn
x25TTR23Limit = _X25TTR23Limit_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 5, 1, 8),
    _X25TTR23Limit_Type()
)
x25TTR23Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25TTR23Limit.setStatus("mandatory")
_X25StatusTable_Object = MibTable
x25StatusTable = _X25StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6)
)
if mibBuilder.loadTexts:
    x25StatusTable.setStatus("mandatory")
_X25StatusTableEntry_Object = MibTableRow
x25StatusTableEntry = _X25StatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1)
)
x25StatusTableEntry.setIndexNames(
    (0, "RETIX-MIB", "x25StatusIndex"),
)
if mibBuilder.loadTexts:
    x25StatusTableEntry.setStatus("mandatory")
_X25StatusIndex_Type = Integer32
_X25StatusIndex_Object = MibTableColumn
x25StatusIndex = _X25StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1, 1),
    _X25StatusIndex_Type()
)
x25StatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatusIndex.setStatus("mandatory")
_X25StatusIfStatus_Type = Integer32
_X25StatusIfStatus_Object = MibTableColumn
x25StatusIfStatus = _X25StatusIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1, 2),
    _X25StatusIfStatus_Type()
)
x25StatusIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatusIfStatus.setStatus("mandatory")
_X25StatusSVCStatus_Type = Integer32
_X25StatusSVCStatus_Object = MibTableColumn
x25StatusSVCStatus = _X25StatusSVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1, 3),
    _X25StatusSVCStatus_Type()
)
x25StatusSVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatusSVCStatus.setStatus("mandatory")
_X25StatusWinSize_Type = Integer32
_X25StatusWinSize_Object = MibTableColumn
x25StatusWinSize = _X25StatusWinSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1, 4),
    _X25StatusWinSize_Type()
)
x25StatusWinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatusWinSize.setStatus("mandatory")
_X25StatusPktSize_Type = Integer32
_X25StatusPktSize_Object = MibTableColumn
x25StatusPktSize = _X25StatusPktSize_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1, 5),
    _X25StatusPktSize_Type()
)
x25StatusPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatusPktSize.setStatus("mandatory")


class _X25StatusCauseLastInClear_Type(Integer32):
    """Custom type x25StatusCauseLastInClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25StatusCauseLastInClear_Type.__name__ = "Integer32"
_X25StatusCauseLastInClear_Object = MibTableColumn
x25StatusCauseLastInClear = _X25StatusCauseLastInClear_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1, 6),
    _X25StatusCauseLastInClear_Type()
)
x25StatusCauseLastInClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatusCauseLastInClear.setStatus("mandatory")


class _X25StatusDiagLastInClear_Type(Integer32):
    """Custom type x25StatusDiagLastInClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_X25StatusDiagLastInClear_Type.__name__ = "Integer32"
_X25StatusDiagLastInClear_Object = MibTableColumn
x25StatusDiagLastInClear = _X25StatusDiagLastInClear_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 6, 1, 7),
    _X25StatusDiagLastInClear_Type()
)
x25StatusDiagLastInClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25StatusDiagLastInClear.setStatus("mandatory")
_X25StatsTable_Object = MibTable
x25StatsTable = _X25StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7)
)
if mibBuilder.loadTexts:
    x25StatsTable.setStatus("mandatory")
_X25StatsTableEntry_Object = MibTableRow
x25StatsTableEntry = _X25StatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1)
)
x25StatsTableEntry.setIndexNames(
    (0, "RETIX-MIB", "x25STSVCIndex"),
)
if mibBuilder.loadTexts:
    x25StatsTableEntry.setStatus("mandatory")
_X25STSVCIndex_Type = Integer32
_X25STSVCIndex_Object = MibTableColumn
x25STSVCIndex = _X25STSVCIndex_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 1),
    _X25STSVCIndex_Type()
)
x25STSVCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STSVCIndex.setStatus("mandatory")
_X25STTxDataPkts_Type = Counter32
_X25STTxDataPkts_Object = MibTableColumn
x25STTxDataPkts = _X25STTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 2),
    _X25STTxDataPkts_Type()
)
x25STTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STTxDataPkts.setStatus("mandatory")
_X25STRxDataPkts_Type = Counter32
_X25STRxDataPkts_Object = MibTableColumn
x25STRxDataPkts = _X25STRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 3),
    _X25STRxDataPkts_Type()
)
x25STRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STRxDataPkts.setStatus("mandatory")
_X25STTxConnectReqPkts_Type = Counter32
_X25STTxConnectReqPkts_Object = MibTableColumn
x25STTxConnectReqPkts = _X25STTxConnectReqPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 4),
    _X25STTxConnectReqPkts_Type()
)
x25STTxConnectReqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STTxConnectReqPkts.setStatus("mandatory")
_X25STRxIncomingCallPkts_Type = Counter32
_X25STRxIncomingCallPkts_Object = MibTableColumn
x25STRxIncomingCallPkts = _X25STRxIncomingCallPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 5),
    _X25STRxIncomingCallPkts_Type()
)
x25STRxIncomingCallPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STRxIncomingCallPkts.setStatus("mandatory")
_X25STTxClearReqPkts_Type = Counter32
_X25STTxClearReqPkts_Object = MibTableColumn
x25STTxClearReqPkts = _X25STTxClearReqPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 6),
    _X25STTxClearReqPkts_Type()
)
x25STTxClearReqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STTxClearReqPkts.setStatus("mandatory")
_X25STRxClearIndPkts_Type = Counter32
_X25STRxClearIndPkts_Object = MibTableColumn
x25STRxClearIndPkts = _X25STRxClearIndPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 7),
    _X25STRxClearIndPkts_Type()
)
x25STRxClearIndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STRxClearIndPkts.setStatus("mandatory")
_X25STTxResetReqPkts_Type = Counter32
_X25STTxResetReqPkts_Object = MibTableColumn
x25STTxResetReqPkts = _X25STTxResetReqPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 8),
    _X25STTxResetReqPkts_Type()
)
x25STTxResetReqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STTxResetReqPkts.setStatus("mandatory")
_X25STRxResetIndPkts_Type = Counter32
_X25STRxResetIndPkts_Object = MibTableColumn
x25STRxResetIndPkts = _X25STRxResetIndPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 9),
    _X25STRxResetIndPkts_Type()
)
x25STRxResetIndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STRxResetIndPkts.setStatus("mandatory")
_X25STTxRestartReqPkts_Type = Counter32
_X25STTxRestartReqPkts_Object = MibTableColumn
x25STTxRestartReqPkts = _X25STTxRestartReqPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 10),
    _X25STTxRestartReqPkts_Type()
)
x25STTxRestartReqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STTxRestartReqPkts.setStatus("mandatory")
_X25STRxRestartIndPkts_Type = Counter32
_X25STRxRestartIndPkts_Object = MibTableColumn
x25STRxRestartIndPkts = _X25STRxRestartIndPkts_Object(
    (1, 3, 6, 1, 4, 1, 72, 13, 4, 7, 1, 11),
    _X25STRxRestartIndPkts_Type()
)
x25STRxRestartIndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25STRxRestartIndPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RETIX-MIB",
    **{"retix": retix,
       "station": station,
       "stationTime": stationTime,
       "stationCountResets": stationCountResets,
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
       "lapbCountResets": lapbCountResets,
       "lapbCountSentFrames": lapbCountSentFrames,
       "lapbCountRcvFrames": lapbCountRcvFrames,
       "lapbCountSentOctets": lapbCountSentOctets,
       "lapbCountRcvOctets": lapbCountRcvOctets,
       "lapbCountAborts": lapbCountAborts,
       "lapbCountCrcErrors": lapbCountCrcErrors,
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
       "phySerIfPartnerAddress": phySerIfPartnerAddress,
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
       "mlinkLostFrames": mlinkLostFrames,
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
       "averageForwardedFrames": averageForwardedFrames,
       "maxForwardedFrames": maxForwardedFrames,
       "averageRejectedFrames": averageRejectedFrames,
       "maxRejectedFrames": maxRejectedFrames,
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
       "router": router,
       "ipRSTable": ipRSTable,
       "ipRSEntry": ipRSEntry,
       "ipRSIndex": ipRSIndex,
       "gwProtocol": gwProtocol,
       "ifStatus": ifStatus,
       "receivedTotalDgms": receivedTotalDgms,
       "transmittedTotalDgms": transmittedTotalDgms,
       "outDiscardsTotalDgms": outDiscardsTotalDgms,
       "noRouteTotalDgms": noRouteTotalDgms,
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
       "boothelperForwardingAddress": boothelperForwardingAddress,
       "remote": remote,
       "ipx": ipx,
       "ipxRouting": ipxRouting,
       "ipxIfNumber": ipxIfNumber,
       "ipxIfTable": ipxIfTable,
       "ipxIfEntry": ipxIfEntry,
       "ipxIfIndex": ipxIfIndex,
       "ipxIfNwkNumber": ipxIfNwkNumber,
       "ipxIfIPXAddress": ipxIfIPXAddress,
       "ipxIfEncapsulation": ipxIfEncapsulation,
       "ipxIfDelay": ipxIfDelay,
       "ipxRoutingTable": ipxRoutingTable,
       "ipxRITEntry": ipxRITEntry,
       "ipxRITDestNwkNumber": ipxRITDestNwkNumber,
       "ipxRITGwyHostAddress": ipxRITGwyHostAddress,
       "ipxRITHopCount": ipxRITHopCount,
       "ipxRITDelay": ipxRITDelay,
       "ipxRITInterface": ipxRITInterface,
       "ipxRITDirectConnect": ipxRITDirectConnect,
       "ipxSAPBinderyTable": ipxSAPBinderyTable,
       "ipxSAPBinderyEntry": ipxSAPBinderyEntry,
       "ipxSAPBinderyType": ipxSAPBinderyType,
       "ipxSAPBinderyServerIPXAddress": ipxSAPBinderyServerIPXAddress,
       "ipxSAPBinderyServerName": ipxSAPBinderyServerName,
       "ipxSAPBinderyHopCount": ipxSAPBinderyHopCount,
       "ipxSAPBinderySocket": ipxSAPBinderySocket,
       "ipxReceivedDgms": ipxReceivedDgms,
       "ipxTransmittedDgms": ipxTransmittedDgms,
       "ipxNotRoutedRxDgms": ipxNotRoutedRxDgms,
       "ipxForwardedDgms": ipxForwardedDgms,
       "ipxInDelivers": ipxInDelivers,
       "ipxInHdrErrors": ipxInHdrErrors,
       "ipxAccessViolations": ipxAccessViolations,
       "ipxInDiscards": ipxInDiscards,
       "ipxOutDiscards": ipxOutDiscards,
       "ipxOtherDiscards": ipxOtherDiscards,
       "decnet": decnet,
       "dcntRouting": dcntRouting,
       "dcntIfNumber": dcntIfNumber,
       "dcntIfTable": dcntIfTable,
       "dcntIfTableEntry": dcntIfTableEntry,
       "dcntIfIndex": dcntIfIndex,
       "dcntIfCost": dcntIfCost,
       "dcntIfRtrPriority": dcntIfRtrPriority,
       "dcntIfDesgntdRtr": dcntIfDesgntdRtr,
       "dcntIfHelloTimerBCT3": dcntIfHelloTimerBCT3,
       "dcntRoutingTable": dcntRoutingTable,
       "dcntRITEntry": dcntRITEntry,
       "dcntRITDestNode": dcntRITDestNode,
       "dcntRITNextHop": dcntRITNextHop,
       "dcntRITCost": dcntRITCost,
       "dcntRITHops": dcntRITHops,
       "dcntRITInterface": dcntRITInterface,
       "dcntAreaRoutingTable": dcntAreaRoutingTable,
       "dcntAreaRITEntry": dcntAreaRITEntry,
       "dcntAreaRITDestArea": dcntAreaRITDestArea,
       "dcntAreaRITNextHop": dcntAreaRITNextHop,
       "dcntAreaRITCost": dcntAreaRITCost,
       "dcntAreaRITHops": dcntAreaRITHops,
       "dcntAreaRITInterface": dcntAreaRITInterface,
       "dcntNodeAddress": dcntNodeAddress,
       "dcntInterAreaMaxCost": dcntInterAreaMaxCost,
       "dcntInterAreaMaxHops": dcntInterAreaMaxHops,
       "dcntIntraAreaMaxCost": dcntIntraAreaMaxCost,
       "dcntIntraAreaMaxHops": dcntIntraAreaMaxHops,
       "dcntMaxVisits": dcntMaxVisits,
       "dcntRtngMsgTimerBCT1": dcntRtngMsgTimerBCT1,
       "dcntRateControlFreqTimerT2": dcntRateControlFreqTimerT2,
       "dcntReveivedDgms": dcntReveivedDgms,
       "dcntForwardedDgms": dcntForwardedDgms,
       "dcntOutRequestedDgms": dcntOutRequestedDgms,
       "dcntInDiscards": dcntInDiscards,
       "dcntOutDiscards": dcntOutDiscards,
       "dcntNoRoutes": dcntNoRoutes,
       "dcntInHdrErrors": dcntInHdrErrors,
       "rmtLapb": rmtLapb,
       "rmtLapbConfigTable": rmtLapbConfigTable,
       "rmtLapbCTEntry": rmtLapbCTEntry,
       "rmtLapbCTIndex": rmtLapbCTIndex,
       "rmtLapbCTLinkAddr": rmtLapbCTLinkAddr,
       "rmtLapbCTExtSeqNumbering": rmtLapbCTExtSeqNumbering,
       "rmtLapbCTWindow": rmtLapbCTWindow,
       "rmtLapbCTModeT1": rmtLapbCTModeT1,
       "rmtLapbCTManualT1Value": rmtLapbCTManualT1Value,
       "rmtLapbCTT3LinkIdleTimer": rmtLapbCTT3LinkIdleTimer,
       "rmtLapbCTN2RetryCount": rmtLapbCTN2RetryCount,
       "rmtLapbCTLinkReset": rmtLapbCTLinkReset,
       "rmtLapbCTX25PortLineSpeed": rmtLapbCTX25PortLineSpeed,
       "rmtLapbCTInitLinkConnect": rmtLapbCTInitLinkConnect,
       "rmtLapbStatsTable": rmtLapbStatsTable,
       "rmtLapbSTEntry": rmtLapbSTEntry,
       "rmtLapbSTIndex": rmtLapbSTIndex,
       "rmtLapbSTState": rmtLapbSTState,
       "rmtLapbSTAutoT1value": rmtLapbSTAutoT1value,
       "rmtLapbSTLastResetTime": rmtLapbSTLastResetTime,
       "rmtLapbSTLastResetReason": rmtLapbSTLastResetReason,
       "rmtLapbSTCountResets": rmtLapbSTCountResets,
       "rmtLapbSTCountSentFrames": rmtLapbSTCountSentFrames,
       "rmtLapbSTCountRcvFrames": rmtLapbSTCountRcvFrames,
       "rmtLapbSTCountSentOctets": rmtLapbSTCountSentOctets,
       "rmtLapbSTCountRcvOctets": rmtLapbSTCountRcvOctets,
       "rmtLapbSTCountAborts": rmtLapbSTCountAborts,
       "rmtLapbSTCountCrcErrors": rmtLapbSTCountCrcErrors,
       "x25": x25,
       "x25Operation": x25Operation,
       "x25OperNextReset": x25OperNextReset,
       "x25ConSetupTable": x25ConSetupTable,
       "x25CSTEntry": x25CSTEntry,
       "x25CSTIndex": x25CSTIndex,
       "x25CST8084Switch": x25CST8084Switch,
       "x25CSTSrcDTEAddr": x25CSTSrcDTEAddr,
       "x25CSTDestDTEAddr": x25CSTDestDTEAddr,
       "x25CST2WayLgclChanNum": x25CST2WayLgclChanNum,
       "x25CSTPktSeqNumFlg": x25CSTPktSeqNumFlg,
       "x25CSTFlowCntrlNeg": x25CSTFlowCntrlNeg,
       "x25CSTDefaultWinSize": x25CSTDefaultWinSize,
       "x25CSTDefaultPktSize": x25CSTDefaultPktSize,
       "x25CSTNegWinSize": x25CSTNegWinSize,
       "x25CSTNegPktSize": x25CSTNegPktSize,
       "x25CSTCUGSub": x25CSTCUGSub,
       "x25CSTLclCUGValue": x25CSTLclCUGValue,
       "x25CSTRvrsChrgReq": x25CSTRvrsChrgReq,
       "x25CSTRvrsChrgAcc": x25CSTRvrsChrgAcc,
       "x25ConControlTable": x25ConControlTable,
       "x25CCTEntry": x25CCTEntry,
       "x25CCTIndex": x25CCTIndex,
       "x25CCTManualConnect": x25CCTManualConnect,
       "x25CCTManualDisconnect": x25CCTManualDisconnect,
       "x25CCTCfgAutoConRetry": x25CCTCfgAutoConRetry,
       "x25CCTOperAutoConRetryFlg": x25CCTOperAutoConRetryFlg,
       "x25CCTAutoConRetryTimer": x25CCTAutoConRetryTimer,
       "x25CCTMaxAutoConRetries": x25CCTMaxAutoConRetries,
       "x25CCTCfgTODControl": x25CCTCfgTODControl,
       "x25CCTCurrentTODControl": x25CCTCurrentTODControl,
       "x25CCTTODToConnect": x25CCTTODToConnect,
       "x25CCTTODToDisconnect": x25CCTTODToDisconnect,
       "x25TimerTable": x25TimerTable,
       "x25TTEntry": x25TTEntry,
       "x25TTIndex": x25TTIndex,
       "x25TTT20Timer": x25TTT20Timer,
       "x25TTT21Timer": x25TTT21Timer,
       "x25TTT22Timer": x25TTT22Timer,
       "x25TTT23Timer": x25TTT23Timer,
       "x25TTR20Limit": x25TTR20Limit,
       "x25TTR22Limit": x25TTR22Limit,
       "x25TTR23Limit": x25TTR23Limit,
       "x25StatusTable": x25StatusTable,
       "x25StatusTableEntry": x25StatusTableEntry,
       "x25StatusIndex": x25StatusIndex,
       "x25StatusIfStatus": x25StatusIfStatus,
       "x25StatusSVCStatus": x25StatusSVCStatus,
       "x25StatusWinSize": x25StatusWinSize,
       "x25StatusPktSize": x25StatusPktSize,
       "x25StatusCauseLastInClear": x25StatusCauseLastInClear,
       "x25StatusDiagLastInClear": x25StatusDiagLastInClear,
       "x25StatsTable": x25StatsTable,
       "x25StatsTableEntry": x25StatsTableEntry,
       "x25STSVCIndex": x25STSVCIndex,
       "x25STTxDataPkts": x25STTxDataPkts,
       "x25STRxDataPkts": x25STRxDataPkts,
       "x25STTxConnectReqPkts": x25STTxConnectReqPkts,
       "x25STRxIncomingCallPkts": x25STRxIncomingCallPkts,
       "x25STTxClearReqPkts": x25STTxClearReqPkts,
       "x25STRxClearIndPkts": x25STRxClearIndPkts,
       "x25STTxResetReqPkts": x25STTxResetReqPkts,
       "x25STRxResetIndPkts": x25STRxResetIndPkts,
       "x25STTxRestartReqPkts": x25STTxRestartReqPkts,
       "x25STRxRestartIndPkts": x25STRxRestartIndPkts}
)
