# SNMP MIB module (Cabletron-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Cabletron-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:28 2024
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

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_CommsDevice_ObjectIdentity = ObjectIdentity
commsDevice = _CommsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1)
)
_CommonRev1_ObjectIdentity = ObjectIdentity
commonRev1 = _CommonRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1)
)
_DeviceType_Type = Integer32
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 1),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("mandatory")
_DeviceName_Type = OctetString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")
_DeviceIPAddress_Type = IpAddress
_DeviceIPAddress_Object = MibScalar
deviceIPAddress = _DeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 3),
    _DeviceIPAddress_Type()
)
deviceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIPAddress.setStatus("mandatory")


class _CurrentTime_Type(OctetString):
    """Custom type currentTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CurrentTime_Type.__name__ = "OctetString"
_CurrentTime_Object = MibScalar
currentTime = _CurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 4),
    _CurrentTime_Type()
)
currentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentTime.setStatus("mandatory")


class _CurrentDate_Type(OctetString):
    """Custom type currentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CurrentDate_Type.__name__ = "OctetString"
_CurrentDate_Object = MibScalar
currentDate = _CurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 5),
    _CurrentDate_Type()
)
currentDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentDate.setStatus("mandatory")
_MACAddress_Type = OctetString
_MACAddress_Object = MibScalar
mACAddress = _MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 6),
    _MACAddress_Type()
)
mACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mACAddress.setStatus("mandatory")
_SysOIDs_ObjectIdentity = ObjectIdentity
sysOIDs = _SysOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2)
)
_SysOtherType_ObjectIdentity = ObjectIdentity
sysOtherType = _SysOtherType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 1)
)
_SysIRMType_ObjectIdentity = ObjectIdentity
sysIRMType = _SysIRMType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2)
)
_SoidIRMSNMP_ObjectIdentity = ObjectIdentity
soidIRMSNMP = _SoidIRMSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2, 1)
)
_SoidIRBM_ObjectIdentity = ObjectIdentity
soidIRBM = _SoidIRBM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2, 2)
)
_SoidIRM2_ObjectIdentity = ObjectIdentity
soidIRM2 = _SoidIRM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2, 3)
)
_SysRepType_ObjectIdentity = ObjectIdentity
sysRepType = _SysRepType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3)
)
_SoidMINIMMAC_ObjectIdentity = ObjectIdentity
soidMINIMMAC = _SoidMINIMMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3, 1)
)
_SoidMRXI_ObjectIdentity = ObjectIdentity
soidMRXI = _SoidMRXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3, 2)
)
_SysBDGType_ObjectIdentity = ObjectIdentity
sysBDGType = _SysBDGType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 4)
)
_Repeater_ObjectIdentity = ObjectIdentity
repeater = _Repeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2)
)
_RepeaterRev1_ObjectIdentity = ObjectIdentity
repeaterRev1 = _RepeaterRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1)
)


class _DeviceMMACType_Type(Integer32):
    """Custom type deviceMMACType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mMAC3", 1),
          ("mMAC8", 0))
    )


_DeviceMMACType_Type.__name__ = "Integer32"
_DeviceMMACType_Object = MibScalar
deviceMMACType = _DeviceMMACType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 2),
    _DeviceMMACType_Type()
)
deviceMMACType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMMACType.setStatus("mandatory")


class _DeviceSlots_Type(Integer32):
    """Custom type deviceSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("mMAC3", 3),
          ("mMAC8", 8))
    )


_DeviceSlots_Type.__name__ = "Integer32"
_DeviceSlots_Object = MibScalar
deviceSlots = _DeviceSlots_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 3),
    _DeviceSlots_Type()
)
deviceSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSlots.setStatus("mandatory")
_DeviceOccupiedSlots_Type = Integer32
_DeviceOccupiedSlots_Object = MibScalar
deviceOccupiedSlots = _DeviceOccupiedSlots_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 4),
    _DeviceOccupiedSlots_Type()
)
deviceOccupiedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOccupiedSlots.setStatus("mandatory")
_DevicePortsOn_Type = Integer32
_DevicePortsOn_Object = MibScalar
devicePortsOn = _DevicePortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 5),
    _DevicePortsOn_Type()
)
devicePortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePortsOn.setStatus("mandatory")
_DeviceTotalPorts_Type = Integer32
_DeviceTotalPorts_Object = MibScalar
deviceTotalPorts = _DeviceTotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 6),
    _DeviceTotalPorts_Type()
)
deviceTotalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTotalPorts.setStatus("mandatory")
_DeviceTotalPkts_Type = Counter32
_DeviceTotalPkts_Object = MibScalar
deviceTotalPkts = _DeviceTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 7),
    _DeviceTotalPkts_Type()
)
deviceTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTotalPkts.setStatus("mandatory")
_DeviceTotalErrors_Type = Counter32
_DeviceTotalErrors_Object = MibScalar
deviceTotalErrors = _DeviceTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 8),
    _DeviceTotalErrors_Type()
)
deviceTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTotalErrors.setStatus("mandatory")
_DeviceTransmitColl_Type = Counter32
_DeviceTransmitColl_Object = MibScalar
deviceTransmitColl = _DeviceTransmitColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 9),
    _DeviceTransmitColl_Type()
)
deviceTransmitColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTransmitColl.setStatus("optional")
_DeviceRecColls_Type = Counter32
_DeviceRecColls_Object = MibScalar
deviceRecColls = _DeviceRecColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 10),
    _DeviceRecColls_Type()
)
deviceRecColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRecColls.setStatus("optional")
_DeviceAlign_Type = Counter32
_DeviceAlign_Object = MibScalar
deviceAlign = _DeviceAlign_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 11),
    _DeviceAlign_Type()
)
deviceAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlign.setStatus("optional")
_DeviceCRC_Type = Counter32
_DeviceCRC_Object = MibScalar
deviceCRC = _DeviceCRC_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 12),
    _DeviceCRC_Type()
)
deviceCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCRC.setStatus("optional")
_DeviceRunt_Type = Counter32
_DeviceRunt_Object = MibScalar
deviceRunt = _DeviceRunt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 13),
    _DeviceRunt_Type()
)
deviceRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRunt.setStatus("optional")
_DeviceOOWColl_Type = Counter32
_DeviceOOWColl_Object = MibScalar
deviceOOWColl = _DeviceOOWColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 14),
    _DeviceOOWColl_Type()
)
deviceOOWColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOOWColl.setStatus("optional")
_DeviceNoResources_Type = Counter32
_DeviceNoResources_Object = MibScalar
deviceNoResources = _DeviceNoResources_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 15),
    _DeviceNoResources_Type()
)
deviceNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNoResources.setStatus("mandatory")
_DeviceRecBytes_Type = Counter32
_DeviceRecBytes_Object = MibScalar
deviceRecBytes = _DeviceRecBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 16),
    _DeviceRecBytes_Type()
)
deviceRecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRecBytes.setStatus("optional")
_DeviceGiantFrames_Type = Counter32
_DeviceGiantFrames_Object = MibScalar
deviceGiantFrames = _DeviceGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 17),
    _DeviceGiantFrames_Type()
)
deviceGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceGiantFrames.setStatus("mandatory")
_DeviceRestart_Type = Integer32
_DeviceRestart_Object = MibScalar
deviceRestart = _DeviceRestart_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 18),
    _DeviceRestart_Type()
)
deviceRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceRestart.setStatus("mandatory")
_DeviceResetCounter_Type = Counter32
_DeviceResetCounter_Object = MibScalar
deviceResetCounter = _DeviceResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 19),
    _DeviceResetCounter_Type()
)
deviceResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceResetCounter.setStatus("mandatory")
_DeviceRedundantCts_Type = Integer32
_DeviceRedundantCts_Object = MibScalar
deviceRedundantCts = _DeviceRedundantCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 20),
    _DeviceRedundantCts_Type()
)
deviceRedundantCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRedundantCts.setStatus("mandatory")
_DeviceTimeBase_Type = Integer32
_DeviceTimeBase_Object = MibScalar
deviceTimeBase = _DeviceTimeBase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 24),
    _DeviceTimeBase_Type()
)
deviceTimeBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceTimeBase.setStatus("mandatory")
_DeviceResetRedundancy_Type = Integer32
_DeviceResetRedundancy_Object = MibScalar
deviceResetRedundancy = _DeviceResetRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 25),
    _DeviceResetRedundancy_Type()
)
deviceResetRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceResetRedundancy.setStatus("mandatory")
_DeviceSrcAddrAgingTime_Type = Integer32
_DeviceSrcAddrAgingTime_Object = MibScalar
deviceSrcAddrAgingTime = _DeviceSrcAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 26),
    _DeviceSrcAddrAgingTime_Type()
)
deviceSrcAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSrcAddrAgingTime.setStatus("mandatory")


class _DeviceSrcAddrTraps_Type(Integer32):
    """Custom type deviceSrcAddrTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapsoff", 1),
          ("trapson", 2))
    )


_DeviceSrcAddrTraps_Type.__name__ = "Integer32"
_DeviceSrcAddrTraps_Object = MibScalar
deviceSrcAddrTraps = _DeviceSrcAddrTraps_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 27),
    _DeviceSrcAddrTraps_Type()
)
deviceSrcAddrTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSrcAddrTraps.setStatus("mandatory")


class _DeviceSrcAddrLocked_Type(Integer32):
    """Custom type deviceSrcAddrLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockoff", 1),
          ("lockon", 2))
    )


_DeviceSrcAddrLocked_Type.__name__ = "Integer32"
_DeviceSrcAddrLocked_Object = MibScalar
deviceSrcAddrLocked = _DeviceSrcAddrLocked_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 28),
    _DeviceSrcAddrLocked_Type()
)
deviceSrcAddrLocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSrcAddrLocked.setStatus("mandatory")
_DeviceEnetBoardMap_Type = Integer32
_DeviceEnetBoardMap_Object = MibScalar
deviceEnetBoardMap = _DeviceEnetBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 29),
    _DeviceEnetBoardMap_Type()
)
deviceEnetBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceEnetBoardMap.setStatus("mandatory")
_DeviceTokenRingBoardMap_Type = Integer32
_DeviceTokenRingBoardMap_Object = MibScalar
deviceTokenRingBoardMap = _DeviceTokenRingBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 30),
    _DeviceTokenRingBoardMap_Type()
)
deviceTokenRingBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTokenRingBoardMap.setStatus("mandatory")
_DeviceFDDIBoardMap_Type = Integer32
_DeviceFDDIBoardMap_Object = MibScalar
deviceFDDIBoardMap = _DeviceFDDIBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 31),
    _DeviceFDDIBoardMap_Type()
)
deviceFDDIBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFDDIBoardMap.setStatus("mandatory")
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 2)
)
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 3)
)
_SourceAddr_ObjectIdentity = ObjectIdentity
sourceAddr = _SourceAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 7)
)
_SourceAddrBoard_Type = Integer32
_SourceAddrBoard_Object = MibScalar
sourceAddrBoard = _SourceAddrBoard_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 7, 1),
    _SourceAddrBoard_Type()
)
sourceAddrBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceAddrBoard.setStatus("mandatory")
_SourceAddrPort_Type = Integer32
_SourceAddrPort_Object = MibScalar
sourceAddrPort = _SourceAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 7, 2),
    _SourceAddrPort_Type()
)
sourceAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceAddrPort.setStatus("mandatory")
_Redundancy_ObjectIdentity = ObjectIdentity
redundancy = _Redundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8)
)
_RedundancyPollInterval_Type = Integer32
_RedundancyPollInterval_Object = MibScalar
redundancyPollInterval = _RedundancyPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 1),
    _RedundancyPollInterval_Type()
)
redundancyPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyPollInterval.setStatus("mandatory")
_RedundancyTestTod_Type = OctetString
_RedundancyTestTod_Object = MibScalar
redundancyTestTod = _RedundancyTestTod_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 2),
    _RedundancyTestTod_Type()
)
redundancyTestTod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyTestTod.setStatus("mandatory")


class _RedundancyPerformTest_Type(Integer32):
    """Custom type redundancyPerformTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("performTest", 1)
    )


_RedundancyPerformTest_Type.__name__ = "Integer32"
_RedundancyPerformTest_Object = MibScalar
redundancyPerformTest = _RedundancyPerformTest_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 3),
    _RedundancyPerformTest_Type()
)
redundancyPerformTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyPerformTest.setStatus("mandatory")
_RedundancyCircuitName_Type = OctetString
_RedundancyCircuitName_Object = MibScalar
redundancyCircuitName = _RedundancyCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 4),
    _RedundancyCircuitName_Type()
)
redundancyCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyCircuitName.setStatus("mandatory")
_RedundancyRetryCount_Type = Integer32
_RedundancyRetryCount_Object = MibScalar
redundancyRetryCount = _RedundancyRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 5),
    _RedundancyRetryCount_Type()
)
redundancyRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyRetryCount.setStatus("mandatory")
_RedundancyNumBPs_Type = Integer32
_RedundancyNumBPs_Object = MibScalar
redundancyNumBPs = _RedundancyNumBPs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 6),
    _RedundancyNumBPs_Type()
)
redundancyNumBPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyNumBPs.setStatus("mandatory")
_RedundancyCircuitBoards_Type = Integer32
_RedundancyCircuitBoards_Object = MibScalar
redundancyCircuitBoards = _RedundancyCircuitBoards_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 7),
    _RedundancyCircuitBoards_Type()
)
redundancyCircuitBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyCircuitBoards.setStatus("mandatory")
_RedundancyCircuitPort_Type = Integer32
_RedundancyCircuitPort_Object = MibScalar
redundancyCircuitPort = _RedundancyCircuitPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 8),
    _RedundancyCircuitPort_Type()
)
redundancyCircuitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyCircuitPort.setStatus("mandatory")
_RedundancyCircuitTypes_Type = Integer32
_RedundancyCircuitTypes_Object = MibScalar
redundancyCircuitTypes = _RedundancyCircuitTypes_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 9),
    _RedundancyCircuitTypes_Type()
)
redundancyCircuitTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyCircuitTypes.setStatus("mandatory")
_RedundancyCircuitNumAddr_Type = Integer32
_RedundancyCircuitNumAddr_Object = MibScalar
redundancyCircuitNumAddr = _RedundancyCircuitNumAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 10),
    _RedundancyCircuitNumAddr_Type()
)
redundancyCircuitNumAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyCircuitNumAddr.setStatus("mandatory")
_RedundancyCircuitMACAddrAdd_Type = OctetString
_RedundancyCircuitMACAddrAdd_Object = MibScalar
redundancyCircuitMACAddrAdd = _RedundancyCircuitMACAddrAdd_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 11),
    _RedundancyCircuitMACAddrAdd_Type()
)
redundancyCircuitMACAddrAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyCircuitMACAddrAdd.setStatus("mandatory")
_RedundancyCircuitMACAddrDel_Type = OctetString
_RedundancyCircuitMACAddrDel_Object = MibScalar
redundancyCircuitMACAddrDel = _RedundancyCircuitMACAddrDel_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 12),
    _RedundancyCircuitMACAddrDel_Type()
)
redundancyCircuitMACAddrDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyCircuitMACAddrDel.setStatus("mandatory")
_RedundancyCircuitMACAddrDisp_Type = OctetString
_RedundancyCircuitMACAddrDisp_Object = MibScalar
redundancyCircuitMACAddrDisp = _RedundancyCircuitMACAddrDisp_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 13),
    _RedundancyCircuitMACAddrDisp_Type()
)
redundancyCircuitMACAddrDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyCircuitMACAddrDisp.setStatus("mandatory")


class _RedundancyCircuitEnable_Type(Integer32):
    """Custom type redundancyCircuitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_RedundancyCircuitEnable_Type.__name__ = "Integer32"
_RedundancyCircuitEnable_Object = MibScalar
redundancyCircuitEnable = _RedundancyCircuitEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 14),
    _RedundancyCircuitEnable_Type()
)
redundancyCircuitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyCircuitEnable.setStatus("mandatory")


class _RedundancyCircuitReset_Type(Integer32):
    """Custom type redundancyCircuitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_RedundancyCircuitReset_Type.__name__ = "Integer32"
_RedundancyCircuitReset_Object = MibScalar
redundancyCircuitReset = _RedundancyCircuitReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 8, 15),
    _RedundancyCircuitReset_Type()
)
redundancyCircuitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyCircuitReset.setStatus("mandatory")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9)
)
_DevAlrm_ObjectIdentity = ObjectIdentity
devAlrm = _DevAlrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1)
)
_DevTraffic_ObjectIdentity = ObjectIdentity
devTraffic = _DevTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 1)
)


class _DevTrafficEnable_Type(Integer32):
    """Custom type devTrafficEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DevTrafficEnable_Type.__name__ = "Integer32"
_DevTrafficEnable_Object = MibScalar
devTrafficEnable = _DevTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 1, 1),
    _DevTrafficEnable_Type()
)
devTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTrafficEnable.setStatus("mandatory")
_DevTrafficThreshold_Type = Counter32
_DevTrafficThreshold_Object = MibScalar
devTrafficThreshold = _DevTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 1, 2),
    _DevTrafficThreshold_Type()
)
devTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTrafficThreshold.setStatus("mandatory")
_DevColls_ObjectIdentity = ObjectIdentity
devColls = _DevColls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 2)
)


class _DevCollsEnable_Type(Integer32):
    """Custom type devCollsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DevCollsEnable_Type.__name__ = "Integer32"
_DevCollsEnable_Object = MibScalar
devCollsEnable = _DevCollsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 2, 1),
    _DevCollsEnable_Type()
)
devCollsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devCollsEnable.setStatus("mandatory")
_DevCollsThreshold_Type = Integer32
_DevCollsThreshold_Object = MibScalar
devCollsThreshold = _DevCollsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 2, 2),
    _DevCollsThreshold_Type()
)
devCollsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devCollsThreshold.setStatus("mandatory")
_DevError_ObjectIdentity = ObjectIdentity
devError = _DevError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 3)
)


class _DevErrorEnable_Type(Integer32):
    """Custom type devErrorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DevErrorEnable_Type.__name__ = "Integer32"
_DevErrorEnable_Object = MibScalar
devErrorEnable = _DevErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 3, 1),
    _DevErrorEnable_Type()
)
devErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devErrorEnable.setStatus("mandatory")
_DevErrorThreshold_Type = Integer32
_DevErrorThreshold_Object = MibScalar
devErrorThreshold = _DevErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 3, 2),
    _DevErrorThreshold_Type()
)
devErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devErrorThreshold.setStatus("mandatory")
_DevErrorSource_Type = Integer32
_DevErrorSource_Object = MibScalar
devErrorSource = _DevErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 3, 3),
    _DevErrorSource_Type()
)
devErrorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devErrorSource.setStatus("mandatory")
_BdAlrm_ObjectIdentity = ObjectIdentity
bdAlrm = _BdAlrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2)
)
_BdTraffic_ObjectIdentity = ObjectIdentity
bdTraffic = _BdTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 1)
)


class _BdTrafficEnable_Type(Integer32):
    """Custom type bdTrafficEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BdTrafficEnable_Type.__name__ = "Integer32"
_BdTrafficEnable_Object = MibScalar
bdTrafficEnable = _BdTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 1, 1),
    _BdTrafficEnable_Type()
)
bdTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdTrafficEnable.setStatus("mandatory")
_BdTrafficThreshold_Type = Counter32
_BdTrafficThreshold_Object = MibScalar
bdTrafficThreshold = _BdTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 1, 2),
    _BdTrafficThreshold_Type()
)
bdTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdTrafficThreshold.setStatus("mandatory")
_BdColls_ObjectIdentity = ObjectIdentity
bdColls = _BdColls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 2)
)


class _BdCollsEnable_Type(Integer32):
    """Custom type bdCollsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BdCollsEnable_Type.__name__ = "Integer32"
_BdCollsEnable_Object = MibScalar
bdCollsEnable = _BdCollsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 2, 1),
    _BdCollsEnable_Type()
)
bdCollsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdCollsEnable.setStatus("mandatory")
_BdCollsThreshold_Type = Integer32
_BdCollsThreshold_Object = MibScalar
bdCollsThreshold = _BdCollsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 2, 2),
    _BdCollsThreshold_Type()
)
bdCollsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdCollsThreshold.setStatus("mandatory")
_BdError_ObjectIdentity = ObjectIdentity
bdError = _BdError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3)
)


class _BdErrorEnable_Type(Integer32):
    """Custom type bdErrorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BdErrorEnable_Type.__name__ = "Integer32"
_BdErrorEnable_Object = MibScalar
bdErrorEnable = _BdErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3, 1),
    _BdErrorEnable_Type()
)
bdErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdErrorEnable.setStatus("mandatory")
_BdErrorThreshold_Type = Integer32
_BdErrorThreshold_Object = MibScalar
bdErrorThreshold = _BdErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3, 2),
    _BdErrorThreshold_Type()
)
bdErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdErrorThreshold.setStatus("mandatory")
_BdErrorSource_Type = Integer32
_BdErrorSource_Object = MibScalar
bdErrorSource = _BdErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3, 3),
    _BdErrorSource_Type()
)
bdErrorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdErrorSource.setStatus("mandatory")
_PortAlrm_ObjectIdentity = ObjectIdentity
portAlrm = _PortAlrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3)
)
_PortTraffic_ObjectIdentity = ObjectIdentity
portTraffic = _PortTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 1)
)


class _PortTrafficEnable_Type(Integer32):
    """Custom type portTrafficEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortTrafficEnable_Type.__name__ = "Integer32"
_PortTrafficEnable_Object = MibScalar
portTrafficEnable = _PortTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 1, 1),
    _PortTrafficEnable_Type()
)
portTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrafficEnable.setStatus("mandatory")
_PortTrafficThreshold_Type = Counter32
_PortTrafficThreshold_Object = MibScalar
portTrafficThreshold = _PortTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 1, 2),
    _PortTrafficThreshold_Type()
)
portTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrafficThreshold.setStatus("mandatory")
_PortColls_ObjectIdentity = ObjectIdentity
portColls = _PortColls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 2)
)


class _PortCollsEnable_Type(Integer32):
    """Custom type portCollsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortCollsEnable_Type.__name__ = "Integer32"
_PortCollsEnable_Object = MibScalar
portCollsEnable = _PortCollsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 2, 1),
    _PortCollsEnable_Type()
)
portCollsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCollsEnable.setStatus("mandatory")
_PortCollsThreshold_Type = Integer32
_PortCollsThreshold_Object = MibScalar
portCollsThreshold = _PortCollsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 2, 2),
    _PortCollsThreshold_Type()
)
portCollsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCollsThreshold.setStatus("mandatory")
_PortError_ObjectIdentity = ObjectIdentity
portError = _PortError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3)
)


class _PortErrorEnable_Type(Integer32):
    """Custom type portErrorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortErrorEnable_Type.__name__ = "Integer32"
_PortErrorEnable_Object = MibScalar
portErrorEnable = _PortErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3, 1),
    _PortErrorEnable_Type()
)
portErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrorEnable.setStatus("mandatory")
_PortErrorThreshold_Type = Integer32
_PortErrorThreshold_Object = MibScalar
portErrorThreshold = _PortErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3, 2),
    _PortErrorThreshold_Type()
)
portErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrorThreshold.setStatus("mandatory")
_PortErrorSource_Type = Integer32
_PortErrorSource_Object = MibScalar
portErrorSource = _PortErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3, 3),
    _PortErrorSource_Type()
)
portErrorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrorSource.setStatus("mandatory")
_RepeaterRev2_ObjectIdentity = ObjectIdentity
repeaterRev2 = _RepeaterRev2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2)
)
_Rr2device_ObjectIdentity = ObjectIdentity
rr2device = _Rr2device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1)
)
_CommonD_ObjectIdentity = ObjectIdentity
commonD = _CommonD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 1)
)
_EthernetD_ObjectIdentity = ObjectIdentity
ethernetD = _EthernetD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 2)
)
_TokenRingD_ObjectIdentity = ObjectIdentity
tokenRingD = _TokenRingD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3)
)
_DeviceTRTokenRingPortsOn_Type = Integer32
_DeviceTRTokenRingPortsOn_Object = MibScalar
deviceTRTokenRingPortsOn = _DeviceTRTokenRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 1),
    _DeviceTRTokenRingPortsOn_Type()
)
deviceTRTokenRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTokenRingPortsOn.setStatus("mandatory")
_DeviceTRTotalTokenRingPorts_Type = Integer32
_DeviceTRTotalTokenRingPorts_Object = MibScalar
deviceTRTotalTokenRingPorts = _DeviceTRTotalTokenRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 2),
    _DeviceTRTotalTokenRingPorts_Type()
)
deviceTRTotalTokenRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingPorts.setStatus("mandatory")
_DeviceTRTotalTokenRingRingPortsOn_Type = Integer32
_DeviceTRTotalTokenRingRingPortsOn_Object = MibScalar
deviceTRTotalTokenRingRingPortsOn = _DeviceTRTotalTokenRingRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 3),
    _DeviceTRTotalTokenRingRingPortsOn_Type()
)
deviceTRTotalTokenRingRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingRingPortsOn.setStatus("mandatory")
_DeviceTRTotalTokenRingRingPorts_Type = Integer32
_DeviceTRTotalTokenRingRingPorts_Object = MibScalar
deviceTRTotalTokenRingRingPorts = _DeviceTRTotalTokenRingRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 4),
    _DeviceTRTotalTokenRingRingPorts_Type()
)
deviceTRTotalTokenRingRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingRingPorts.setStatus("mandatory")
_DeviceTRTotalTokenRingRings_Type = Integer32
_DeviceTRTotalTokenRingRings_Object = MibScalar
deviceTRTotalTokenRingRings = _DeviceTRTotalTokenRingRings_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 5),
    _DeviceTRTotalTokenRingRings_Type()
)
deviceTRTotalTokenRingRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingRings.setStatus("mandatory")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 2)
)
_Rr2board_ObjectIdentity = ObjectIdentity
rr2board = _Rr2board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3)
)
_CommonB_ObjectIdentity = ObjectIdentity
commonB = _CommonB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1)
)
_BoardIndex_Type = Integer32
_BoardIndex_Object = MibScalar
boardIndex = _BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 1),
    _BoardIndex_Type()
)
boardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardIndex.setStatus("mandatory")
_BoardName_Type = OctetString
_BoardName_Object = MibScalar
boardName = _BoardName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 2),
    _BoardName_Type()
)
boardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardName.setStatus("mandatory")
_BoardType_Type = Integer32
_BoardType_Object = MibScalar
boardType = _BoardType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 3),
    _BoardType_Type()
)
boardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardType.setStatus("mandatory")
_BoardTotalPorts_Type = Integer32
_BoardTotalPorts_Object = MibScalar
boardTotalPorts = _BoardTotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 4),
    _BoardTotalPorts_Type()
)
boardTotalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalPorts.setStatus("mandatory")


class _BoardSTATUS_Type(Integer32):
    """Custom type boardSTATUS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BoardSTATUS_Type.__name__ = "Integer32"
_BoardSTATUS_Object = MibScalar
boardSTATUS = _BoardSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 5),
    _BoardSTATUS_Type()
)
boardSTATUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardSTATUS.setStatus("optional")
_BoardPortsOn_Type = Integer32
_BoardPortsOn_Object = MibScalar
boardPortsOn = _BoardPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 6),
    _BoardPortsOn_Type()
)
boardPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPortsOn.setStatus("mandatory")
_EthernetB_ObjectIdentity = ObjectIdentity
ethernetB = _EthernetB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2)
)
_BoardTotalPkts_Type = Counter32
_BoardTotalPkts_Object = MibScalar
boardTotalPkts = _BoardTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 1),
    _BoardTotalPkts_Type()
)
boardTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalPkts.setStatus("mandatory")
_BoardErrorPkts_Type = Counter32
_BoardErrorPkts_Object = MibScalar
boardErrorPkts = _BoardErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 2),
    _BoardErrorPkts_Type()
)
boardErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardErrorPkts.setStatus("mandatory")
_BoardTransColl_Type = Counter32
_BoardTransColl_Object = MibScalar
boardTransColl = _BoardTransColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 3),
    _BoardTransColl_Type()
)
boardTransColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTransColl.setStatus("optional")
_BoardRecColl_Type = Counter32
_BoardRecColl_Object = MibScalar
boardRecColl = _BoardRecColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 4),
    _BoardRecColl_Type()
)
boardRecColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRecColl.setStatus("optional")
_BoardAlign_Type = Counter32
_BoardAlign_Object = MibScalar
boardAlign = _BoardAlign_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 5),
    _BoardAlign_Type()
)
boardAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardAlign.setStatus("optional")
_BoardCRC_Type = Counter32
_BoardCRC_Object = MibScalar
boardCRC = _BoardCRC_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 6),
    _BoardCRC_Type()
)
boardCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardCRC.setStatus("optional")
_BoardRunt_Type = Counter32
_BoardRunt_Object = MibScalar
boardRunt = _BoardRunt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 7),
    _BoardRunt_Type()
)
boardRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRunt.setStatus("optional")
_BoardOOWColl_Type = Counter32
_BoardOOWColl_Object = MibScalar
boardOOWColl = _BoardOOWColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 8),
    _BoardOOWColl_Type()
)
boardOOWColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardOOWColl.setStatus("optional")
_BoardNoResources_Type = Counter32
_BoardNoResources_Object = MibScalar
boardNoResources = _BoardNoResources_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 9),
    _BoardNoResources_Type()
)
boardNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardNoResources.setStatus("optional")
_BoardRecBytes_Type = Counter32
_BoardRecBytes_Object = MibScalar
boardRecBytes = _BoardRecBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 10),
    _BoardRecBytes_Type()
)
boardRecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRecBytes.setStatus("optional")
_BoardGiants_Type = Counter32
_BoardGiants_Object = MibScalar
boardGiants = _BoardGiants_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 11),
    _BoardGiants_Type()
)
boardGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardGiants.setStatus("mandatory")
_TokenRingB_ObjectIdentity = ObjectIdentity
tokenRingB = _TokenRingB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3)
)
_BoardTotalRingPorts_Type = Integer32
_BoardTotalRingPorts_Object = MibScalar
boardTotalRingPorts = _BoardTotalRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 1),
    _BoardTotalRingPorts_Type()
)
boardTotalRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalRingPorts.setStatus("mandatory")
_BoardTotalStationPorts_Type = Integer32
_BoardTotalStationPorts_Object = MibScalar
boardTotalStationPorts = _BoardTotalStationPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 2),
    _BoardTotalStationPorts_Type()
)
boardTotalStationPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalStationPorts.setStatus("mandatory")
_BoardModeStatus_Type = Integer32
_BoardModeStatus_Object = MibScalar
boardModeStatus = _BoardModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 3),
    _BoardModeStatus_Type()
)
boardModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardModeStatus.setStatus("mandatory")
_BoardTotalRingPortsOn_Type = Integer32
_BoardTotalRingPortsOn_Object = MibScalar
boardTotalRingPortsOn = _BoardTotalRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 4),
    _BoardTotalRingPortsOn_Type()
)
boardTotalRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalRingPortsOn.setStatus("mandatory")
_BoardTotalStationPortsOn_Type = Integer32
_BoardTotalStationPortsOn_Object = MibScalar
boardTotalStationPortsOn = _BoardTotalStationPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 5),
    _BoardTotalStationPortsOn_Type()
)
boardTotalStationPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalStationPortsOn.setStatus("mandatory")
_BoardSpeed_Type = Integer32
_BoardSpeed_Object = MibScalar
boardSpeed = _BoardSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 6),
    _BoardSpeed_Type()
)
boardSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardSpeed.setStatus("mandatory")


class _BoardRingSpeedFault_Type(Integer32):
    """Custom type boardRingSpeedFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faultDetected", 2),
          ("noFaultDetected", 1))
    )


_BoardRingSpeedFault_Type.__name__ = "Integer32"
_BoardRingSpeedFault_Object = MibScalar
boardRingSpeedFault = _BoardRingSpeedFault_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 7),
    _BoardRingSpeedFault_Type()
)
boardRingSpeedFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRingSpeedFault.setStatus("mandatory")
_FddiB_ObjectIdentity = ObjectIdentity
fddiB = _FddiB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 4)
)
_Rr2port_ObjectIdentity = ObjectIdentity
rr2port = _Rr2port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4)
)
_CommonP_ObjectIdentity = ObjectIdentity
commonP = _CommonP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 1)
)
_PortIndex_Type = Integer32
_PortIndex_Object = MibScalar
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_PortMediaType_Type = Integer32
_PortMediaType_Object = MibScalar
portMediaType = _PortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 1, 2),
    _PortMediaType_Type()
)
portMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaType.setStatus("mandatory")


class _PortAdminState_Type(Integer32):
    """Custom type portAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PortAdminState_Type.__name__ = "Integer32"
_PortAdminState_Object = MibScalar
portAdminState = _PortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 1, 3),
    _PortAdminState_Type()
)
portAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminState.setStatus("mandatory")
_PortSourceAddr_Type = OctetString
_PortSourceAddr_Object = MibScalar
portSourceAddr = _PortSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 1, 4),
    _PortSourceAddr_Type()
)
portSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSourceAddr.setStatus("mandatory")
_EthernetP_ObjectIdentity = ObjectIdentity
ethernetP = _EthernetP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2)
)
_PortTopologyType_Type = Integer32
_PortTopologyType_Object = MibScalar
portTopologyType = _PortTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 1),
    _PortTopologyType_Type()
)
portTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopologyType.setStatus("mandatory")


class _PortLinkStatus_Type(Integer32):
    """Custom type portLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkSignalActive", 2),
          ("linkSignalInactive", 1),
          ("linkSignalNotSupported", 3))
    )


_PortLinkStatus_Type.__name__ = "Integer32"
_PortLinkStatus_Object = MibScalar
portLinkStatus = _PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 2),
    _PortLinkStatus_Type()
)
portLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkStatus.setStatus("mandatory")


class _PortStatus_Type(Integer32):
    """Custom type portStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("segmented", 2))
    )


_PortStatus_Type.__name__ = "Integer32"
_PortStatus_Object = MibScalar
portStatus = _PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 3),
    _PortStatus_Type()
)
portStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatus.setStatus("mandatory")
_PortTotalPkts_Type = Integer32
_PortTotalPkts_Object = MibScalar
portTotalPkts = _PortTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 4),
    _PortTotalPkts_Type()
)
portTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTotalPkts.setStatus("mandatory")
_PortErrorPkts_Type = Counter32
_PortErrorPkts_Object = MibScalar
portErrorPkts = _PortErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 5),
    _PortErrorPkts_Type()
)
portErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrorPkts.setStatus("mandatory")
_PortXmitColls_Type = Counter32
_PortXmitColls_Object = MibScalar
portXmitColls = _PortXmitColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 6),
    _PortXmitColls_Type()
)
portXmitColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portXmitColls.setStatus("optional")
_PortRecColls_Type = Counter32
_PortRecColls_Object = MibScalar
portRecColls = _PortRecColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 7),
    _PortRecColls_Type()
)
portRecColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRecColls.setStatus("optional")
_PortAlign_Type = Counter32
_PortAlign_Object = MibScalar
portAlign = _PortAlign_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 8),
    _PortAlign_Type()
)
portAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAlign.setStatus("optional")
_PortCRC_Type = Counter32
_PortCRC_Object = MibScalar
portCRC = _PortCRC_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 9),
    _PortCRC_Type()
)
portCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCRC.setStatus("optional")
_PortRunt_Type = Counter32
_PortRunt_Object = MibScalar
portRunt = _PortRunt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 10),
    _PortRunt_Type()
)
portRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRunt.setStatus("optional")
_PortOOWColl_Type = Counter32
_PortOOWColl_Object = MibScalar
portOOWColl = _PortOOWColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 11),
    _PortOOWColl_Type()
)
portOOWColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOOWColl.setStatus("optional")
_PortNoResorces_Type = Counter32
_PortNoResorces_Object = MibScalar
portNoResorces = _PortNoResorces_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 12),
    _PortNoResorces_Type()
)
portNoResorces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNoResorces.setStatus("optional")
_PortRecBytes_Type = Counter32
_PortRecBytes_Object = MibScalar
portRecBytes = _PortRecBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 13),
    _PortRecBytes_Type()
)
portRecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRecBytes.setStatus("optional")
_PortGiants_Type = Counter32
_PortGiants_Object = MibScalar
portGiants = _PortGiants_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 14),
    _PortGiants_Type()
)
portGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGiants.setStatus("optional")
_PortRedundCrt_Type = Integer32
_PortRedundCrt_Object = MibScalar
portRedundCrt = _PortRedundCrt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 15),
    _PortRedundCrt_Type()
)
portRedundCrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRedundCrt.setStatus("mandatory")


class _PortRedundType_Type(Integer32):
    """Custom type portRedundType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backup", 4),
          ("notUsed", 1),
          ("primary", 3))
    )


_PortRedundType_Type.__name__ = "Integer32"
_PortRedundType_Object = MibScalar
portRedundType = _PortRedundType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 16),
    _PortRedundType_Type()
)
portRedundType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRedundType.setStatus("mandatory")


class _PortRedundStatus_Type(Integer32):
    """Custom type portRedundStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("notUsed", 1))
    )


_PortRedundStatus_Type.__name__ = "Integer32"
_PortRedundStatus_Object = MibScalar
portRedundStatus = _PortRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 17),
    _PortRedundStatus_Type()
)
portRedundStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRedundStatus.setStatus("mandatory")


class _PortForceLinkType_Type(Integer32):
    """Custom type portForceLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("notForced", 1))
    )


_PortForceLinkType_Type.__name__ = "Integer32"
_PortForceLinkType_Object = MibScalar
portForceLinkType = _PortForceLinkType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 18),
    _PortForceLinkType_Type()
)
portForceLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForceLinkType.setStatus("mandatory")
_TokenRingP_ObjectIdentity = ObjectIdentity
tokenRingP = _TokenRingP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3)
)
_StationP_ObjectIdentity = ObjectIdentity
stationP = _StationP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 1)
)


class _StationPortLinkStatus_Type(Integer32):
    """Custom type stationPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkSignalActive", 2),
          ("linkSignalInactive", 1))
    )


_StationPortLinkStatus_Type.__name__ = "Integer32"
_StationPortLinkStatus_Object = MibScalar
stationPortLinkStatus = _StationPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 1, 1),
    _StationPortLinkStatus_Type()
)
stationPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationPortLinkStatus.setStatus("mandatory")
_StationPortLinkStateTime_Type = Integer32
_StationPortLinkStateTime_Object = MibScalar
stationPortLinkStateTime = _StationPortLinkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 1, 2),
    _StationPortLinkStateTime_Type()
)
stationPortLinkStateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationPortLinkStateTime.setStatus("mandatory")
_RingP_ObjectIdentity = ObjectIdentity
ringP = _RingP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 2)
)


class _RingPortLinkStatus_Type(Integer32):
    """Custom type ringPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RingPortLinkStatus_Type.__name__ = "Integer32"
_RingPortLinkStatus_Object = MibScalar
ringPortLinkStatus = _RingPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 2, 1),
    _RingPortLinkStatus_Type()
)
ringPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringPortLinkStatus.setStatus("mandatory")
_RingPortLinkStateTime_Type = Integer32
_RingPortLinkStateTime_Object = MibScalar
ringPortLinkStateTime = _RingPortLinkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 2, 2),
    _RingPortLinkStateTime_Type()
)
ringPortLinkStateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringPortLinkStateTime.setStatus("mandatory")
_FddiP_ObjectIdentity = ObjectIdentity
fddiP = _FddiP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 4)
)
_RepeaterTables_ObjectIdentity = ObjectIdentity
repeaterTables = _RepeaterTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 5)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3)
)
_BridgeRev1_ObjectIdentity = ObjectIdentity
bridgeRev1 = _BridgeRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1)
)
_Bdgdevice_ObjectIdentity = ObjectIdentity
bdgdevice = _Bdgdevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1)
)


class _BdgdeviceDisableBdg_Type(Integer32):
    """Custom type bdgdeviceDisableBdg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableBridge", 0),
          ("enableBridge", 1))
    )


_BdgdeviceDisableBdg_Type.__name__ = "Integer32"
_BdgdeviceDisableBdg_Object = MibScalar
bdgdeviceDisableBdg = _BdgdeviceDisableBdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 1),
    _BdgdeviceDisableBdg_Type()
)
bdgdeviceDisableBdg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceDisableBdg.setStatus("mandatory")


class _BdgdeviceRestoreSettings_Type(Integer32):
    """Custom type bdgdeviceRestoreSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("restoreSettings", 0)
    )


_BdgdeviceRestoreSettings_Type.__name__ = "Integer32"
_BdgdeviceRestoreSettings_Object = MibScalar
bdgdeviceRestoreSettings = _BdgdeviceRestoreSettings_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 2),
    _BdgdeviceRestoreSettings_Type()
)
bdgdeviceRestoreSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceRestoreSettings.setStatus("mandatory")
_BdgdeviceBdgName_Type = OctetString
_BdgdeviceBdgName_Object = MibScalar
bdgdeviceBdgName = _BdgdeviceBdgName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 4),
    _BdgdeviceBdgName_Type()
)
bdgdeviceBdgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgName.setStatus("mandatory")
_BdgdeviceNumPorts_Type = Integer32
_BdgdeviceNumPorts_Object = MibScalar
bdgdeviceNumPorts = _BdgdeviceNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 5),
    _BdgdeviceNumPorts_Type()
)
bdgdeviceNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceNumPorts.setStatus("mandatory")
_BdgdeviceType_Type = OctetString
_BdgdeviceType_Object = MibScalar
bdgdeviceType = _BdgdeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 6),
    _BdgdeviceType_Type()
)
bdgdeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceType.setStatus("mandatory")
_BdgdeviceVersion_Type = OctetString
_BdgdeviceVersion_Object = MibScalar
bdgdeviceVersion = _BdgdeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 7),
    _BdgdeviceVersion_Type()
)
bdgdeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceVersion.setStatus("mandatory")
_BdgdeviceLocation_Type = OctetString
_BdgdeviceLocation_Object = MibScalar
bdgdeviceLocation = _BdgdeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 8),
    _BdgdeviceLocation_Type()
)
bdgdeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceLocation.setStatus("mandatory")
_BdgdeviceStatus_Type = OctetString
_BdgdeviceStatus_Object = MibScalar
bdgdeviceStatus = _BdgdeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 9),
    _BdgdeviceStatus_Type()
)
bdgdeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceStatus.setStatus("mandatory")


class _BdgdeviceRestartBdg_Type(Integer32):
    """Custom type bdgdeviceRestartBdg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("restartBridge", 0)
    )


_BdgdeviceRestartBdg_Type.__name__ = "Integer32"
_BdgdeviceRestartBdg_Object = MibScalar
bdgdeviceRestartBdg = _BdgdeviceRestartBdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 10),
    _BdgdeviceRestartBdg_Type()
)
bdgdeviceRestartBdg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceRestartBdg.setStatus("mandatory")
_BdgdeviceFrFwd_Type = Counter32
_BdgdeviceFrFwd_Object = MibScalar
bdgdeviceFrFwd = _BdgdeviceFrFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 11),
    _BdgdeviceFrFwd_Type()
)
bdgdeviceFrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFrFwd.setStatus("mandatory")
_BdgdeviceFrRx_Type = Counter32
_BdgdeviceFrRx_Object = MibScalar
bdgdeviceFrRx = _BdgdeviceFrRx_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 12),
    _BdgdeviceFrRx_Type()
)
bdgdeviceFrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFrRx.setStatus("mandatory")
_BdgdeviceFrFlt_Type = Counter32
_BdgdeviceFrFlt_Object = MibScalar
bdgdeviceFrFlt = _BdgdeviceFrFlt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 13),
    _BdgdeviceFrFlt_Type()
)
bdgdeviceFrFlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFrFlt.setStatus("mandatory")
_BdgdeviceErr_Type = Counter32
_BdgdeviceErr_Object = MibScalar
bdgdeviceErr = _BdgdeviceErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 14),
    _BdgdeviceErr_Type()
)
bdgdeviceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceErr.setStatus("mandatory")
_BdgdeviceSwitchSetting_Type = OctetString
_BdgdeviceSwitchSetting_Object = MibScalar
bdgdeviceSwitchSetting = _BdgdeviceSwitchSetting_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 15),
    _BdgdeviceSwitchSetting_Type()
)
bdgdeviceSwitchSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceSwitchSetting.setStatus("mandatory")
_BdgdeviceNumRestarts_Type = Counter32
_BdgdeviceNumRestarts_Object = MibScalar
bdgdeviceNumRestarts = _BdgdeviceNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 16),
    _BdgdeviceNumRestarts_Type()
)
bdgdeviceNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceNumRestarts.setStatus("mandatory")


class _BdgdeviceTypeFiltering_Type(Integer32):
    """Custom type bdgdeviceTypeFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("ieee8021", 0),
          ("specialDB", 1))
    )


_BdgdeviceTypeFiltering_Type.__name__ = "Integer32"
_BdgdeviceTypeFiltering_Object = MibScalar
bdgdeviceTypeFiltering = _BdgdeviceTypeFiltering_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 17),
    _BdgdeviceTypeFiltering_Type()
)
bdgdeviceTypeFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceTypeFiltering.setStatus("mandatory")


class _BdgdeviceSTAProtocol_Type(Integer32):
    """Custom type bdgdeviceSTAProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dec", 1),
          ("ieee8021", 0),
          ("none", 2))
    )


_BdgdeviceSTAProtocol_Type.__name__ = "Integer32"
_BdgdeviceSTAProtocol_Object = MibScalar
bdgdeviceSTAProtocol = _BdgdeviceSTAProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 18),
    _BdgdeviceSTAProtocol_Type()
)
bdgdeviceSTAProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceSTAProtocol.setStatus("mandatory")
_BdgdeviceBridgeID_Type = OctetString
_BdgdeviceBridgeID_Object = MibScalar
bdgdeviceBridgeID = _BdgdeviceBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 19),
    _BdgdeviceBridgeID_Type()
)
bdgdeviceBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceBridgeID.setStatus("mandatory")
_BdgdeviceTopChgCnt_Type = Counter32
_BdgdeviceTopChgCnt_Object = MibScalar
bdgdeviceTopChgCnt = _BdgdeviceTopChgCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 20),
    _BdgdeviceTopChgCnt_Type()
)
bdgdeviceTopChgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTopChgCnt.setStatus("mandatory")
_BdgdeviceRootCost_Type = Integer32
_BdgdeviceRootCost_Object = MibScalar
bdgdeviceRootCost = _BdgdeviceRootCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 21),
    _BdgdeviceRootCost_Type()
)
bdgdeviceRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceRootCost.setStatus("mandatory")
_BdgdeviceRootPort_Type = Integer32
_BdgdeviceRootPort_Object = MibScalar
bdgdeviceRootPort = _BdgdeviceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 22),
    _BdgdeviceRootPort_Type()
)
bdgdeviceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceRootPort.setStatus("mandatory")
_BdgdeviceHelloTime_Type = Integer32
_BdgdeviceHelloTime_Object = MibScalar
bdgdeviceHelloTime = _BdgdeviceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 23),
    _BdgdeviceHelloTime_Type()
)
bdgdeviceHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceHelloTime.setStatus("mandatory")
_BdgdeviceBdgMaxAge_Type = Integer32
_BdgdeviceBdgMaxAge_Object = MibScalar
bdgdeviceBdgMaxAge = _BdgdeviceBdgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 24),
    _BdgdeviceBdgMaxAge_Type()
)
bdgdeviceBdgMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgMaxAge.setStatus("mandatory")
_BdgdeviceBdgFwdDly_Type = Integer32
_BdgdeviceBdgFwdDly_Object = MibScalar
bdgdeviceBdgFwdDly = _BdgdeviceBdgFwdDly_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 25),
    _BdgdeviceBdgFwdDly_Type()
)
bdgdeviceBdgFwdDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgFwdDly.setStatus("mandatory")
_BdgdeviceTimeTopChg_Type = Integer32
_BdgdeviceTimeTopChg_Object = MibScalar
bdgdeviceTimeTopChg = _BdgdeviceTimeTopChg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 26),
    _BdgdeviceTimeTopChg_Type()
)
bdgdeviceTimeTopChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTimeTopChg.setStatus("mandatory")


class _BdgdeviceTopChg_Type(Integer32):
    """Custom type bdgdeviceTopChg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noTopologyChangeInProgress", 0),
          ("topologyChangeInProgress", 1))
    )


_BdgdeviceTopChg_Type.__name__ = "Integer32"
_BdgdeviceTopChg_Object = MibScalar
bdgdeviceTopChg = _BdgdeviceTopChg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 27),
    _BdgdeviceTopChg_Type()
)
bdgdeviceTopChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTopChg.setStatus("mandatory")
_BdgdeviceDesigRoot_Type = OctetString
_BdgdeviceDesigRoot_Object = MibScalar
bdgdeviceDesigRoot = _BdgdeviceDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 28),
    _BdgdeviceDesigRoot_Type()
)
bdgdeviceDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceDesigRoot.setStatus("mandatory")
_BdgdeviceMaxAge_Type = Integer32
_BdgdeviceMaxAge_Object = MibScalar
bdgdeviceMaxAge = _BdgdeviceMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 29),
    _BdgdeviceMaxAge_Type()
)
bdgdeviceMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceMaxAge.setStatus("mandatory")
_BdgdeviceHoldTime_Type = Integer32
_BdgdeviceHoldTime_Object = MibScalar
bdgdeviceHoldTime = _BdgdeviceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 30),
    _BdgdeviceHoldTime_Type()
)
bdgdeviceHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceHoldTime.setStatus("mandatory")
_BdgdeviceFwdDly_Type = Integer32
_BdgdeviceFwdDly_Object = MibScalar
bdgdeviceFwdDly = _BdgdeviceFwdDly_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 31),
    _BdgdeviceFwdDly_Type()
)
bdgdeviceFwdDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFwdDly.setStatus("mandatory")
_BdgdeviceBdgHello_Type = Integer32
_BdgdeviceBdgHello_Object = MibScalar
bdgdeviceBdgHello = _BdgdeviceBdgHello_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 32),
    _BdgdeviceBdgHello_Type()
)
bdgdeviceBdgHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgHello.setStatus("mandatory")
_BdgdeviceBdgPriority_Type = Integer32
_BdgdeviceBdgPriority_Object = MibScalar
bdgdeviceBdgPriority = _BdgdeviceBdgPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 33),
    _BdgdeviceBdgPriority_Type()
)
bdgdeviceBdgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgPriority.setStatus("mandatory")


class _BdgdeviceResetCounts_Type(Integer32):
    """Custom type bdgdeviceResetCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("resetCounts", 0)
    )


_BdgdeviceResetCounts_Type.__name__ = "Integer32"
_BdgdeviceResetCounts_Object = MibScalar
bdgdeviceResetCounts = _BdgdeviceResetCounts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 34),
    _BdgdeviceResetCounts_Type()
)
bdgdeviceResetCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceResetCounts.setStatus("mandatory")
_BdgdeviceUptime_Type = Integer32
_BdgdeviceUptime_Object = MibScalar
bdgdeviceUptime = _BdgdeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 35),
    _BdgdeviceUptime_Type()
)
bdgdeviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceUptime.setStatus("mandatory")
_BdgdeviceTrapType_Type = ObjectIdentifier
_BdgdeviceTrapType_Object = MibScalar
bdgdeviceTrapType = _BdgdeviceTrapType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 36),
    _BdgdeviceTrapType_Type()
)
bdgdeviceTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTrapType.setStatus("mandatory")
_BdgPort_ObjectIdentity = ObjectIdentity
bdgPort = _BdgPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2)
)
_BdgPortAddress_Type = OctetString
_BdgPortAddress_Object = MibScalar
bdgPortAddress = _BdgPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 1),
    _BdgPortAddress_Type()
)
bdgPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortAddress.setStatus("mandatory")
_BdgPortName_Type = OctetString
_BdgPortName_Object = MibScalar
bdgPortName = _BdgPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 2),
    _BdgPortName_Type()
)
bdgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortName.setStatus("mandatory")
_BdgPortType_Type = OctetString
_BdgPortType_Object = MibScalar
bdgPortType = _BdgPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 3),
    _BdgPortType_Type()
)
bdgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortType.setStatus("mandatory")
_BdgPortStatus_Type = OctetString
_BdgPortStatus_Object = MibScalar
bdgPortStatus = _BdgPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 4),
    _BdgPortStatus_Type()
)
bdgPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortStatus.setStatus("mandatory")
_BdgPortNetName_Type = OctetString
_BdgPortNetName_Object = MibScalar
bdgPortNetName = _BdgPortNetName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 5),
    _BdgPortNetName_Type()
)
bdgPortNetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortNetName.setStatus("mandatory")
_BdgPortFrRx_Type = Counter32
_BdgPortFrRx_Object = MibScalar
bdgPortFrRx = _BdgPortFrRx_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 6),
    _BdgPortFrRx_Type()
)
bdgPortFrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFrRx.setStatus("mandatory")
_BdgPortDisInb_Type = Counter32
_BdgPortDisInb_Object = MibScalar
bdgPortDisInb = _BdgPortDisInb_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 7),
    _BdgPortDisInb_Type()
)
bdgPortDisInb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisInb.setStatus("mandatory")
_BdgPortFwdOutb_Type = Counter32
_BdgPortFwdOutb_Object = MibScalar
bdgPortFwdOutb = _BdgPortFwdOutb_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 8),
    _BdgPortFwdOutb_Type()
)
bdgPortFwdOutb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFwdOutb.setStatus("mandatory")
_BdgPortDisLOB_Type = Counter32
_BdgPortDisLOB_Object = MibScalar
bdgPortDisLOB = _BdgPortDisLOB_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 9),
    _BdgPortDisLOB_Type()
)
bdgPortDisLOB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisLOB.setStatus("mandatory")
_BdgPortDisTDE_Type = Counter32
_BdgPortDisTDE_Object = MibScalar
bdgPortDisTDE = _BdgPortDisTDE_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 10),
    _BdgPortDisTDE_Type()
)
bdgPortDisTDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisTDE.setStatus("mandatory")
_BdgPortDisErr_Type = Counter32
_BdgPortDisErr_Object = MibScalar
bdgPortDisErr = _BdgPortDisErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 11),
    _BdgPortDisErr_Type()
)
bdgPortDisErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisErr.setStatus("mandatory")
_BdgPortColl_Type = Counter32
_BdgPortColl_Object = MibScalar
bdgPortColl = _BdgPortColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 12),
    _BdgPortColl_Type()
)
bdgPortColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortColl.setStatus("mandatory")
_BdgPortTxAbrt_Type = Counter32
_BdgPortTxAbrt_Object = MibScalar
bdgPortTxAbrt = _BdgPortTxAbrt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 13),
    _BdgPortTxAbrt_Type()
)
bdgPortTxAbrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortTxAbrt.setStatus("mandatory")
_BdgPortOowColl_Type = Counter32
_BdgPortOowColl_Object = MibScalar
bdgPortOowColl = _BdgPortOowColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 14),
    _BdgPortOowColl_Type()
)
bdgPortOowColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortOowColl.setStatus("mandatory")
_BdgPortCRCErr_Type = Counter32
_BdgPortCRCErr_Object = MibScalar
bdgPortCRCErr = _BdgPortCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 15),
    _BdgPortCRCErr_Type()
)
bdgPortCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortCRCErr.setStatus("mandatory")
_BdgPortFrAlErr_Type = Counter32
_BdgPortFrAlErr_Object = MibScalar
bdgPortFrAlErr = _BdgPortFrAlErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 16),
    _BdgPortFrAlErr_Type()
)
bdgPortFrAlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFrAlErr.setStatus("mandatory")
_BdgPortPriority_Type = Integer32
_BdgPortPriority_Object = MibScalar
bdgPortPriority = _BdgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 17),
    _BdgPortPriority_Type()
)
bdgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortPriority.setStatus("mandatory")
_BdgPortState_Type = OctetString
_BdgPortState_Object = MibScalar
bdgPortState = _BdgPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 18),
    _BdgPortState_Type()
)
bdgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortState.setStatus("mandatory")
_BdgPortPathCost_Type = Integer32
_BdgPortPathCost_Object = MibScalar
bdgPortPathCost = _BdgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 19),
    _BdgPortPathCost_Type()
)
bdgPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortPathCost.setStatus("mandatory")
_BdgPortDesigCost_Type = Integer32
_BdgPortDesigCost_Object = MibScalar
bdgPortDesigCost = _BdgPortDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 20),
    _BdgPortDesigCost_Type()
)
bdgPortDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigCost.setStatus("mandatory")
_BdgPortDesigBrdg_Type = OctetString
_BdgPortDesigBrdg_Object = MibScalar
bdgPortDesigBrdg = _BdgPortDesigBrdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 21),
    _BdgPortDesigBrdg_Type()
)
bdgPortDesigBrdg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigBrdg.setStatus("mandatory")
_BdgPortDesigPort_Type = Integer32
_BdgPortDesigPort_Object = MibScalar
bdgPortDesigPort = _BdgPortDesigPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 22),
    _BdgPortDesigPort_Type()
)
bdgPortDesigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigPort.setStatus("mandatory")


class _BdgPortTopChgAck_Type(Integer32):
    """Custom type bdgPortTopChgAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noTopologyChangeIsOccurring", 0),
          ("topologyChangeIsOccurring", 1))
    )


_BdgPortTopChgAck_Type.__name__ = "Integer32"
_BdgPortTopChgAck_Object = MibScalar
bdgPortTopChgAck = _BdgPortTopChgAck_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 23),
    _BdgPortTopChgAck_Type()
)
bdgPortTopChgAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortTopChgAck.setStatus("mandatory")
_BdgPortDesigRoot_Type = OctetString
_BdgPortDesigRoot_Object = MibScalar
bdgPortDesigRoot = _BdgPortDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 24),
    _BdgPortDesigRoot_Type()
)
bdgPortDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigRoot.setStatus("mandatory")
_BdgPortRuntPackets_Type = Counter32
_BdgPortRuntPackets_Object = MibScalar
bdgPortRuntPackets = _BdgPortRuntPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 25),
    _BdgPortRuntPackets_Type()
)
bdgPortRuntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortRuntPackets.setStatus("mandatory")
_BdgPortOversizePackets_Type = Counter32
_BdgPortOversizePackets_Object = MibScalar
bdgPortOversizePackets = _BdgPortOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 26),
    _BdgPortOversizePackets_Type()
)
bdgPortOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortOversizePackets.setStatus("mandatory")
_BdgPortFrFilt_Type = Counter32
_BdgPortFrFilt_Object = MibScalar
bdgPortFrFilt = _BdgPortFrFilt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 27),
    _BdgPortFrFilt_Type()
)
bdgPortFrFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFrFilt.setStatus("mandatory")
_FilterDB_ObjectIdentity = ObjectIdentity
filterDB = _FilterDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3)
)
_AcqDB_ObjectIdentity = ObjectIdentity
acqDB = _AcqDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1)
)
_AcqStats_ObjectIdentity = ObjectIdentity
acqStats = _AcqStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1)
)
_AcqTotalEntries_Type = Integer32
_AcqTotalEntries_Object = MibScalar
acqTotalEntries = _AcqTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 1),
    _AcqTotalEntries_Type()
)
acqTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqTotalEntries.setStatus("mandatory")
_AcqMaxEntries_Type = Integer32
_AcqMaxEntries_Object = MibScalar
acqMaxEntries = _AcqMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 2),
    _AcqMaxEntries_Type()
)
acqMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqMaxEntries.setStatus("mandatory")
_AcqStaticEntries_Type = Integer32
_AcqStaticEntries_Object = MibScalar
acqStaticEntries = _AcqStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 3),
    _AcqStaticEntries_Type()
)
acqStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqStaticEntries.setStatus("mandatory")
_AcqStaticAgeTime_Type = Integer32
_AcqStaticAgeTime_Object = MibScalar
acqStaticAgeTime = _AcqStaticAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 4),
    _AcqStaticAgeTime_Type()
)
acqStaticAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqStaticAgeTime.setStatus("mandatory")
_AcqDynEntries_Type = Integer32
_AcqDynEntries_Object = MibScalar
acqDynEntries = _AcqDynEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 5),
    _AcqDynEntries_Type()
)
acqDynEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDynEntries.setStatus("mandatory")
_AcqDynAgeTime_Type = Integer32
_AcqDynAgeTime_Object = MibScalar
acqDynAgeTime = _AcqDynAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 6),
    _AcqDynAgeTime_Type()
)
acqDynAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqDynAgeTime.setStatus("mandatory")


class _AcqEraseDatabase_Type(Integer32):
    """Custom type acqEraseDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("eraseAcquiredDatabase", 0)
    )


_AcqEraseDatabase_Type.__name__ = "Integer32"
_AcqEraseDatabase_Object = MibScalar
acqEraseDatabase = _AcqEraseDatabase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 7),
    _AcqEraseDatabase_Type()
)
acqEraseDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqEraseDatabase.setStatus("mandatory")
_AcqOptions_ObjectIdentity = ObjectIdentity
acqOptions = _AcqOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2)
)


class _AcqCreate00_Type(Integer32):
    """Custom type acqCreate00 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryFilterPort1FilterPort2", 0)
    )


_AcqCreate00_Type.__name__ = "Integer32"
_AcqCreate00_Object = MibScalar
acqCreate00 = _AcqCreate00_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 1),
    _AcqCreate00_Type()
)
acqCreate00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate00.setStatus("mandatory")


class _AcqCreate20_Type(Integer32):
    """Custom type acqCreate20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryForwardPort1FilterPort2", 0)
    )


_AcqCreate20_Type.__name__ = "Integer32"
_AcqCreate20_Object = MibScalar
acqCreate20 = _AcqCreate20_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 2),
    _AcqCreate20_Type()
)
acqCreate20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate20.setStatus("mandatory")


class _AcqCreate01_Type(Integer32):
    """Custom type acqCreate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryFilterPort1ForwardPort2", 0)
    )


_AcqCreate01_Type.__name__ = "Integer32"
_AcqCreate01_Object = MibScalar
acqCreate01 = _AcqCreate01_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 3),
    _AcqCreate01_Type()
)
acqCreate01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate01.setStatus("mandatory")


class _AcqCreate21_Type(Integer32):
    """Custom type acqCreate21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryForwardPort1ForwardPort2", 0)
    )


_AcqCreate21_Type.__name__ = "Integer32"
_AcqCreate21_Object = MibScalar
acqCreate21 = _AcqCreate21_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 4),
    _AcqCreate21_Type()
)
acqCreate21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate21.setStatus("mandatory")


class _AcqDelete_Type(Integer32):
    """Custom type acqDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("deleteAcquiredEntry", 0)
    )


_AcqDelete_Type.__name__ = "Integer32"
_AcqDelete_Object = MibScalar
acqDelete = _AcqDelete_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 5),
    _AcqDelete_Type()
)
acqDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqDelete.setStatus("mandatory")
_AcqDispType_Type = OctetString
_AcqDispType_Object = MibScalar
acqDispType = _AcqDispType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 6),
    _AcqDispType_Type()
)
acqDispType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDispType.setStatus("mandatory")


class _AcqDispOutp1_Type(Integer32):
    """Custom type acqDispOutp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 2))
    )


_AcqDispOutp1_Type.__name__ = "Integer32"
_AcqDispOutp1_Object = MibScalar
acqDispOutp1 = _AcqDispOutp1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 7),
    _AcqDispOutp1_Type()
)
acqDispOutp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDispOutp1.setStatus("mandatory")


class _AcqDispOutp2_Type(Integer32):
    """Custom type acqDispOutp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 1))
    )


_AcqDispOutp2_Type.__name__ = "Integer32"
_AcqDispOutp2_Object = MibScalar
acqDispOutp2 = _AcqDispOutp2_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 8),
    _AcqDispOutp2_Type()
)
acqDispOutp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDispOutp2.setStatus("mandatory")
_AcqSrcAddress_Type = OctetString
_AcqSrcAddress_Object = MibScalar
acqSrcAddress = _AcqSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 9),
    _AcqSrcAddress_Type()
)
acqSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqSrcAddress.setStatus("mandatory")
_PermDB_ObjectIdentity = ObjectIdentity
permDB = _PermDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2)
)
_PermStats_ObjectIdentity = ObjectIdentity
permStats = _PermStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1)
)
_PermMaxEntries_Type = Integer32
_PermMaxEntries_Object = MibScalar
permMaxEntries = _PermMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 1),
    _PermMaxEntries_Type()
)
permMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permMaxEntries.setStatus("mandatory")
_PermCurrEntries_Type = Integer32
_PermCurrEntries_Object = MibScalar
permCurrEntries = _PermCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 2),
    _PermCurrEntries_Type()
)
permCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permCurrEntries.setStatus("mandatory")


class _PermEraseDatabase_Type(Integer32):
    """Custom type permEraseDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("erasePermanentDatabase", 0)
    )


_PermEraseDatabase_Type.__name__ = "Integer32"
_PermEraseDatabase_Object = MibScalar
permEraseDatabase = _PermEraseDatabase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 3),
    _PermEraseDatabase_Type()
)
permEraseDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permEraseDatabase.setStatus("mandatory")
_PermOptions_ObjectIdentity = ObjectIdentity
permOptions = _PermOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2)
)


class _PermCreate00_Type(Integer32):
    """Custom type permCreate00 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryFilterPort1FilterPort2", 0)
    )


_PermCreate00_Type.__name__ = "Integer32"
_PermCreate00_Object = MibScalar
permCreate00 = _PermCreate00_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 1),
    _PermCreate00_Type()
)
permCreate00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate00.setStatus("mandatory")


class _PermCreate20_Type(Integer32):
    """Custom type permCreate20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryForwardPort1FilterPort2", 0)
    )


_PermCreate20_Type.__name__ = "Integer32"
_PermCreate20_Object = MibScalar
permCreate20 = _PermCreate20_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 2),
    _PermCreate20_Type()
)
permCreate20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate20.setStatus("mandatory")


class _PermCreate01_Type(Integer32):
    """Custom type permCreate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryFilterPort1ForwardPort2", 0)
    )


_PermCreate01_Type.__name__ = "Integer32"
_PermCreate01_Object = MibScalar
permCreate01 = _PermCreate01_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 3),
    _PermCreate01_Type()
)
permCreate01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate01.setStatus("mandatory")


class _PermCreate21_Type(Integer32):
    """Custom type permCreate21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryForwardPort1ForwardPort2", 0)
    )


_PermCreate21_Type.__name__ = "Integer32"
_PermCreate21_Object = MibScalar
permCreate21 = _PermCreate21_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 4),
    _PermCreate21_Type()
)
permCreate21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate21.setStatus("mandatory")


class _PermDelete_Type(Integer32):
    """Custom type permDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("deletePermanentEntry", 0)
    )


_PermDelete_Type.__name__ = "Integer32"
_PermDelete_Object = MibScalar
permDelete = _PermDelete_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 5),
    _PermDelete_Type()
)
permDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permDelete.setStatus("mandatory")
_PermDispType_Type = OctetString
_PermDispType_Object = MibScalar
permDispType = _PermDispType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 6),
    _PermDispType_Type()
)
permDispType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permDispType.setStatus("mandatory")


class _PermDispOutp1_Type(Integer32):
    """Custom type permDispOutp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 2))
    )


_PermDispOutp1_Type.__name__ = "Integer32"
_PermDispOutp1_Object = MibScalar
permDispOutp1 = _PermDispOutp1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 7),
    _PermDispOutp1_Type()
)
permDispOutp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permDispOutp1.setStatus("mandatory")


class _PermDispOutp2_Type(Integer32):
    """Custom type permDispOutp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 1))
    )


_PermDispOutp2_Type.__name__ = "Integer32"
_PermDispOutp2_Object = MibScalar
permDispOutp2 = _PermDispOutp2_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 8),
    _PermDispOutp2_Type()
)
permDispOutp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permDispOutp2.setStatus("mandatory")
_PermSrcAddress_Type = OctetString
_PermSrcAddress_Object = MibScalar
permSrcAddress = _PermSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 9),
    _PermSrcAddress_Type()
)
permSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permSrcAddress.setStatus("mandatory")
_SpecialDB_ObjectIdentity = ObjectIdentity
specialDB = _SpecialDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3)
)
_SpecStats_ObjectIdentity = ObjectIdentity
specStats = _SpecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1)
)
_SpecNumEntries_Type = Integer32
_SpecNumEntries_Object = MibScalar
specNumEntries = _SpecNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 1),
    _SpecNumEntries_Type()
)
specNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specNumEntries.setStatus("mandatory")
_SpecMaxEntries_Type = Integer32
_SpecMaxEntries_Object = MibScalar
specMaxEntries = _SpecMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 2),
    _SpecMaxEntries_Type()
)
specMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specMaxEntries.setStatus("mandatory")
_SpecNextFilterNum_Type = Integer32
_SpecNextFilterNum_Object = MibScalar
specNextFilterNum = _SpecNextFilterNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 3),
    _SpecNextFilterNum_Type()
)
specNextFilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specNextFilterNum.setStatus("mandatory")
_SpecFilters_ObjectIdentity = ObjectIdentity
specFilters = _SpecFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2)
)


class _SpecEnable_Type(Integer32):
    """Custom type specEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableFilter", 0),
          ("enableFilter", 1))
    )


_SpecEnable_Type.__name__ = "Integer32"
_SpecEnable_Object = MibScalar
specEnable = _SpecEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 1),
    _SpecEnable_Type()
)
specEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specEnable.setStatus("mandatory")


class _SpecPort1_Type(Integer32):
    """Custom type specPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 2))
    )


_SpecPort1_Type.__name__ = "Integer32"
_SpecPort1_Object = MibScalar
specPort1 = _SpecPort1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 2),
    _SpecPort1_Type()
)
specPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specPort1.setStatus("mandatory")


class _SpecPort2_Type(Integer32):
    """Custom type specPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 1))
    )


_SpecPort2_Type.__name__ = "Integer32"
_SpecPort2_Object = MibScalar
specPort2 = _SpecPort2_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 3),
    _SpecPort2_Type()
)
specPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specPort2.setStatus("mandatory")
_SpecDestAddress_Type = OctetString
_SpecDestAddress_Object = MibScalar
specDestAddress = _SpecDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 4),
    _SpecDestAddress_Type()
)
specDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specDestAddress.setStatus("mandatory")
_SpecSrcAddress_Type = OctetString
_SpecSrcAddress_Object = MibScalar
specSrcAddress = _SpecSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 5),
    _SpecSrcAddress_Type()
)
specSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specSrcAddress.setStatus("mandatory")
_SpecType_Type = OctetString
_SpecType_Object = MibScalar
specType = _SpecType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 6),
    _SpecType_Type()
)
specType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specType.setStatus("mandatory")
_SpecDataField_Type = OctetString
_SpecDataField_Object = MibScalar
specDataField = _SpecDataField_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 7),
    _SpecDataField_Type()
)
specDataField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specDataField.setStatus("mandatory")


class _SpecDeleteFilter_Type(Integer32):
    """Custom type specDeleteFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("deleteFilter", 0)
    )


_SpecDeleteFilter_Type.__name__ = "Integer32"
_SpecDeleteFilter_Object = MibScalar
specDeleteFilter = _SpecDeleteFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 8),
    _SpecDeleteFilter_Type()
)
specDeleteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specDeleteFilter.setStatus("mandatory")
_TrapTypes_ObjectIdentity = ObjectIdentity
trapTypes = _TrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 4)
)
_BdgTables_ObjectIdentity = ObjectIdentity
bdgTables = _BdgTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 5)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 4)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 5)
)
_ProductRev1_ObjectIdentity = ObjectIdentity
productRev1 = _ProductRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1)
)
_IRBM_ObjectIdentity = ObjectIdentity
iRBM = _IRBM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1, 1)
)


class _IRBMRevision_Type(Integer32):
    """Custom type iRBMRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rev0", 0),
          ("rev1", 1),
          ("rev2", 2),
          ("rev3", 3))
    )


_IRBMRevision_Type.__name__ = "Integer32"
_IRBMRevision_Object = MibScalar
iRBMRevision = _IRBMRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1, 1, 1),
    _IRBMRevision_Type()
)
iRBMRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iRBMRevision.setStatus("mandatory")
_IRBMPortAssociation_Type = Integer32
_IRBMPortAssociation_Object = MibScalar
iRBMPortAssociation = _IRBMPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1, 1, 2),
    _IRBMPortAssociation_Type()
)
iRBMPortAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iRBMPortAssociation.setStatus("mandatory")
_Subsystem_ObjectIdentity = ObjectIdentity
subsystem = _Subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6)
)
_MMAC_ObjectIdentity = ObjectIdentity
mMAC = _MMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1)
)
_Fnb_ObjectIdentity = ObjectIdentity
fnb = _Fnb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 1)
)
_FnbConnectedLeft_Type = Integer32
_FnbConnectedLeft_Object = MibScalar
fnbConnectedLeft = _FnbConnectedLeft_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 1, 1),
    _FnbConnectedLeft_Type()
)
fnbConnectedLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbConnectedLeft.setStatus("mandatory")
_FnbConnectedRight_Type = Integer32
_FnbConnectedRight_Object = MibScalar
fnbConnectedRight = _FnbConnectedRight_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 1, 2),
    _FnbConnectedRight_Type()
)
fnbConnectedRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbConnectedRight.setStatus("mandatory")
_FnbBoardBypassState_Type = Integer32
_FnbBoardBypassState_Object = MibScalar
fnbBoardBypassState = _FnbBoardBypassState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 1, 3),
    _FnbBoardBypassState_Type()
)
fnbBoardBypassState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbBoardBypassState.setStatus("mandatory")
_LayerMgmt_ObjectIdentity = ObjectIdentity
layerMgmt = _LayerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2)
)
_Lmcommon_ObjectIdentity = ObjectIdentity
lmcommon = _Lmcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 1)
)
_MAC_ObjectIdentity = ObjectIdentity
mAC = _MAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2)
)
_Ieee8023_ObjectIdentity = ObjectIdentity
ieee8023 = _Ieee8023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1)
)
_PcIF_ObjectIdentity = ObjectIdentity
pcIF = _PcIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1)
)
_PcIfRev_ObjectIdentity = ObjectIdentity
pcIfRev = _PcIfRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1)
)
_PcDeviceName_Type = OctetString
_PcDeviceName_Object = MibScalar
pcDeviceName = _PcDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 1),
    _PcDeviceName_Type()
)
pcDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcDeviceName.setStatus("mandatory")
_PcBoardType_Type = ObjectIdentifier
_PcBoardType_Object = MibScalar
pcBoardType = _PcBoardType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 2),
    _PcBoardType_Type()
)
pcBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBoardType.setStatus("mandatory")
_PcOwnerName_Type = OctetString
_PcOwnerName_Object = MibScalar
pcOwnerName = _PcOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 3),
    _PcOwnerName_Type()
)
pcOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcOwnerName.setStatus("mandatory")
_PcLocation_Type = OctetString
_PcLocation_Object = MibScalar
pcLocation = _PcLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 4),
    _PcLocation_Type()
)
pcLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcLocation.setStatus("mandatory")
_PcMMACAddr_Type = OctetString
_PcMMACAddr_Object = MibScalar
pcMMACAddr = _PcMMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 5),
    _PcMMACAddr_Type()
)
pcMMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMMACAddr.setStatus("mandatory")
_PcMMACBoard_Type = OctetString
_PcMMACBoard_Object = MibScalar
pcMMACBoard = _PcMMACBoard_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 6),
    _PcMMACBoard_Type()
)
pcMMACBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMMACBoard.setStatus("mandatory")
_PcMMACPort_Type = OctetString
_PcMMACPort_Object = MibScalar
pcMMACPort = _PcMMACPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 7),
    _PcMMACPort_Type()
)
pcMMACPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMMACPort.setStatus("mandatory")
_PcApplication_Type = OctetString
_PcApplication_Object = MibScalar
pcApplication = _PcApplication_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 8),
    _PcApplication_Type()
)
pcApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcApplication.setStatus("mandatory")
_PcDriverRev_Type = OctetString
_PcDriverRev_Object = MibScalar
pcDriverRev = _PcDriverRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 9),
    _PcDriverRev_Type()
)
pcDriverRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcDriverRev.setStatus("mandatory")
_PcOnboardMemory_Type = Integer32
_PcOnboardMemory_Object = MibScalar
pcOnboardMemory = _PcOnboardMemory_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 10),
    _PcOnboardMemory_Type()
)
pcOnboardMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcOnboardMemory.setStatus("mandatory")
_PcComment_Type = OctetString
_PcComment_Object = MibScalar
pcComment = _PcComment_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 11),
    _PcComment_Type()
)
pcComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcComment.setStatus("mandatory")
_PcMACAddr_Type = OctetString
_PcMACAddr_Object = MibScalar
pcMACAddr = _PcMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 12),
    _PcMACAddr_Type()
)
pcMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMACAddr.setStatus("mandatory")
_PcFramesXmit_Type = Integer32
_PcFramesXmit_Object = MibScalar
pcFramesXmit = _PcFramesXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 13),
    _PcFramesXmit_Type()
)
pcFramesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcFramesXmit.setStatus("mandatory")
_PcBytesXmit_Type = Integer32
_PcBytesXmit_Object = MibScalar
pcBytesXmit = _PcBytesXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 14),
    _PcBytesXmit_Type()
)
pcBytesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBytesXmit.setStatus("mandatory")
_PcMcastXmit_Type = Integer32
_PcMcastXmit_Object = MibScalar
pcMcastXmit = _PcMcastXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 15),
    _PcMcastXmit_Type()
)
pcMcastXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMcastXmit.setStatus("mandatory")
_PcBcastXmit_Type = Integer32
_PcBcastXmit_Object = MibScalar
pcBcastXmit = _PcBcastXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 16),
    _PcBcastXmit_Type()
)
pcBcastXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBcastXmit.setStatus("mandatory")
_PcDeferXmit_Type = Integer32
_PcDeferXmit_Object = MibScalar
pcDeferXmit = _PcDeferXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 17),
    _PcDeferXmit_Type()
)
pcDeferXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcDeferXmit.setStatus("mandatory")
_PcSglColl_Type = Integer32
_PcSglColl_Object = MibScalar
pcSglColl = _PcSglColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 18),
    _PcSglColl_Type()
)
pcSglColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcSglColl.setStatus("mandatory")
_PcMultiColl_Type = Integer32
_PcMultiColl_Object = MibScalar
pcMultiColl = _PcMultiColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 19),
    _PcMultiColl_Type()
)
pcMultiColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMultiColl.setStatus("mandatory")
_PcTotXmitErrs_Type = Integer32
_PcTotXmitErrs_Object = MibScalar
pcTotXmitErrs = _PcTotXmitErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 20),
    _PcTotXmitErrs_Type()
)
pcTotXmitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTotXmitErrs.setStatus("mandatory")
_PcLateColls_Type = Integer32
_PcLateColls_Object = MibScalar
pcLateColls = _PcLateColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 21),
    _PcLateColls_Type()
)
pcLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcLateColls.setStatus("mandatory")
_PcXcessColls_Type = Integer32
_PcXcessColls_Object = MibScalar
pcXcessColls = _PcXcessColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 22),
    _PcXcessColls_Type()
)
pcXcessColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcXcessColls.setStatus("mandatory")
_PcCarrErr_Type = Integer32
_PcCarrErr_Object = MibScalar
pcCarrErr = _PcCarrErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 23),
    _PcCarrErr_Type()
)
pcCarrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCarrErr.setStatus("mandatory")
_PcFramesRec_Type = Integer32
_PcFramesRec_Object = MibScalar
pcFramesRec = _PcFramesRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 24),
    _PcFramesRec_Type()
)
pcFramesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcFramesRec.setStatus("mandatory")
_PcBytesRec_Type = Integer32
_PcBytesRec_Object = MibScalar
pcBytesRec = _PcBytesRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 25),
    _PcBytesRec_Type()
)
pcBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBytesRec.setStatus("mandatory")
_PcMcastRec_Type = Integer32
_PcMcastRec_Object = MibScalar
pcMcastRec = _PcMcastRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 26),
    _PcMcastRec_Type()
)
pcMcastRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMcastRec.setStatus("mandatory")
_PcBcastRec_Type = Integer32
_PcBcastRec_Object = MibScalar
pcBcastRec = _PcBcastRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 27),
    _PcBcastRec_Type()
)
pcBcastRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBcastRec.setStatus("mandatory")
_PcTotRecErrs_Type = Integer32
_PcTotRecErrs_Object = MibScalar
pcTotRecErrs = _PcTotRecErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 28),
    _PcTotRecErrs_Type()
)
pcTotRecErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTotRecErrs.setStatus("mandatory")
_PcTooLong_Type = Integer32
_PcTooLong_Object = MibScalar
pcTooLong = _PcTooLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 29),
    _PcTooLong_Type()
)
pcTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTooLong.setStatus("mandatory")
_PcTooShort_Type = Integer32
_PcTooShort_Object = MibScalar
pcTooShort = _PcTooShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 30),
    _PcTooShort_Type()
)
pcTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTooShort.setStatus("mandatory")
_PcAlignErrs_Type = Integer32
_PcAlignErrs_Object = MibScalar
pcAlignErrs = _PcAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 31),
    _PcAlignErrs_Type()
)
pcAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcAlignErrs.setStatus("mandatory")
_PcCRCErrs_Type = Integer32
_PcCRCErrs_Object = MibScalar
pcCRCErrs = _PcCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 32),
    _PcCRCErrs_Type()
)
pcCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCRCErrs.setStatus("mandatory")
_PcLenErrs_Type = Integer32
_PcLenErrs_Object = MibScalar
pcLenErrs = _PcLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 33),
    _PcLenErrs_Type()
)
pcLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcLenErrs.setStatus("mandatory")
_PcIntRecErr_Type = Integer32
_PcIntRecErr_Object = MibScalar
pcIntRecErr = _PcIntRecErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 34),
    _PcIntRecErr_Type()
)
pcIntRecErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcIntRecErr.setStatus("mandatory")
_PcSqeErr_Type = Integer32
_PcSqeErr_Object = MibScalar
pcSqeErr = _PcSqeErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 35),
    _PcSqeErr_Type()
)
pcSqeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcSqeErr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Cabletron-MIB",
    **{"cabletron": cabletron,
       "commsDevice": commsDevice,
       "common": common,
       "commonRev1": commonRev1,
       "deviceType": deviceType,
       "deviceName": deviceName,
       "deviceIPAddress": deviceIPAddress,
       "currentTime": currentTime,
       "currentDate": currentDate,
       "mACAddress": mACAddress,
       "sysOIDs": sysOIDs,
       "sysOtherType": sysOtherType,
       "sysIRMType": sysIRMType,
       "soidIRMSNMP": soidIRMSNMP,
       "soidIRBM": soidIRBM,
       "soidIRM2": soidIRM2,
       "sysRepType": sysRepType,
       "soidMINIMMAC": soidMINIMMAC,
       "soidMRXI": soidMRXI,
       "sysBDGType": sysBDGType,
       "repeater": repeater,
       "repeaterRev1": repeaterRev1,
       "device": device,
       "deviceMMACType": deviceMMACType,
       "deviceSlots": deviceSlots,
       "deviceOccupiedSlots": deviceOccupiedSlots,
       "devicePortsOn": devicePortsOn,
       "deviceTotalPorts": deviceTotalPorts,
       "deviceTotalPkts": deviceTotalPkts,
       "deviceTotalErrors": deviceTotalErrors,
       "deviceTransmitColl": deviceTransmitColl,
       "deviceRecColls": deviceRecColls,
       "deviceAlign": deviceAlign,
       "deviceCRC": deviceCRC,
       "deviceRunt": deviceRunt,
       "deviceOOWColl": deviceOOWColl,
       "deviceNoResources": deviceNoResources,
       "deviceRecBytes": deviceRecBytes,
       "deviceGiantFrames": deviceGiantFrames,
       "deviceRestart": deviceRestart,
       "deviceResetCounter": deviceResetCounter,
       "deviceRedundantCts": deviceRedundantCts,
       "deviceTimeBase": deviceTimeBase,
       "deviceResetRedundancy": deviceResetRedundancy,
       "deviceSrcAddrAgingTime": deviceSrcAddrAgingTime,
       "deviceSrcAddrTraps": deviceSrcAddrTraps,
       "deviceSrcAddrLocked": deviceSrcAddrLocked,
       "deviceEnetBoardMap": deviceEnetBoardMap,
       "deviceTokenRingBoardMap": deviceTokenRingBoardMap,
       "deviceFDDIBoardMap": deviceFDDIBoardMap,
       "board": board,
       "port": port,
       "sourceAddr": sourceAddr,
       "sourceAddrBoard": sourceAddrBoard,
       "sourceAddrPort": sourceAddrPort,
       "redundancy": redundancy,
       "redundancyPollInterval": redundancyPollInterval,
       "redundancyTestTod": redundancyTestTod,
       "redundancyPerformTest": redundancyPerformTest,
       "redundancyCircuitName": redundancyCircuitName,
       "redundancyRetryCount": redundancyRetryCount,
       "redundancyNumBPs": redundancyNumBPs,
       "redundancyCircuitBoards": redundancyCircuitBoards,
       "redundancyCircuitPort": redundancyCircuitPort,
       "redundancyCircuitTypes": redundancyCircuitTypes,
       "redundancyCircuitNumAddr": redundancyCircuitNumAddr,
       "redundancyCircuitMACAddrAdd": redundancyCircuitMACAddrAdd,
       "redundancyCircuitMACAddrDel": redundancyCircuitMACAddrDel,
       "redundancyCircuitMACAddrDisp": redundancyCircuitMACAddrDisp,
       "redundancyCircuitEnable": redundancyCircuitEnable,
       "redundancyCircuitReset": redundancyCircuitReset,
       "alarm": alarm,
       "devAlrm": devAlrm,
       "devTraffic": devTraffic,
       "devTrafficEnable": devTrafficEnable,
       "devTrafficThreshold": devTrafficThreshold,
       "devColls": devColls,
       "devCollsEnable": devCollsEnable,
       "devCollsThreshold": devCollsThreshold,
       "devError": devError,
       "devErrorEnable": devErrorEnable,
       "devErrorThreshold": devErrorThreshold,
       "devErrorSource": devErrorSource,
       "bdAlrm": bdAlrm,
       "bdTraffic": bdTraffic,
       "bdTrafficEnable": bdTrafficEnable,
       "bdTrafficThreshold": bdTrafficThreshold,
       "bdColls": bdColls,
       "bdCollsEnable": bdCollsEnable,
       "bdCollsThreshold": bdCollsThreshold,
       "bdError": bdError,
       "bdErrorEnable": bdErrorEnable,
       "bdErrorThreshold": bdErrorThreshold,
       "bdErrorSource": bdErrorSource,
       "portAlrm": portAlrm,
       "portTraffic": portTraffic,
       "portTrafficEnable": portTrafficEnable,
       "portTrafficThreshold": portTrafficThreshold,
       "portColls": portColls,
       "portCollsEnable": portCollsEnable,
       "portCollsThreshold": portCollsThreshold,
       "portError": portError,
       "portErrorEnable": portErrorEnable,
       "portErrorThreshold": portErrorThreshold,
       "portErrorSource": portErrorSource,
       "repeaterRev2": repeaterRev2,
       "rr2device": rr2device,
       "commonD": commonD,
       "ethernetD": ethernetD,
       "tokenRingD": tokenRingD,
       "deviceTRTokenRingPortsOn": deviceTRTokenRingPortsOn,
       "deviceTRTotalTokenRingPorts": deviceTRTotalTokenRingPorts,
       "deviceTRTotalTokenRingRingPortsOn": deviceTRTotalTokenRingRingPortsOn,
       "deviceTRTotalTokenRingRingPorts": deviceTRTotalTokenRingRingPorts,
       "deviceTRTotalTokenRingRings": deviceTRTotalTokenRingRings,
       "network": network,
       "rr2board": rr2board,
       "commonB": commonB,
       "boardIndex": boardIndex,
       "boardName": boardName,
       "boardType": boardType,
       "boardTotalPorts": boardTotalPorts,
       "boardSTATUS": boardSTATUS,
       "boardPortsOn": boardPortsOn,
       "ethernetB": ethernetB,
       "boardTotalPkts": boardTotalPkts,
       "boardErrorPkts": boardErrorPkts,
       "boardTransColl": boardTransColl,
       "boardRecColl": boardRecColl,
       "boardAlign": boardAlign,
       "boardCRC": boardCRC,
       "boardRunt": boardRunt,
       "boardOOWColl": boardOOWColl,
       "boardNoResources": boardNoResources,
       "boardRecBytes": boardRecBytes,
       "boardGiants": boardGiants,
       "tokenRingB": tokenRingB,
       "boardTotalRingPorts": boardTotalRingPorts,
       "boardTotalStationPorts": boardTotalStationPorts,
       "boardModeStatus": boardModeStatus,
       "boardTotalRingPortsOn": boardTotalRingPortsOn,
       "boardTotalStationPortsOn": boardTotalStationPortsOn,
       "boardSpeed": boardSpeed,
       "boardRingSpeedFault": boardRingSpeedFault,
       "fddiB": fddiB,
       "rr2port": rr2port,
       "commonP": commonP,
       "portIndex": portIndex,
       "portMediaType": portMediaType,
       "portAdminState": portAdminState,
       "portSourceAddr": portSourceAddr,
       "ethernetP": ethernetP,
       "portTopologyType": portTopologyType,
       "portLinkStatus": portLinkStatus,
       "portStatus": portStatus,
       "portTotalPkts": portTotalPkts,
       "portErrorPkts": portErrorPkts,
       "portXmitColls": portXmitColls,
       "portRecColls": portRecColls,
       "portAlign": portAlign,
       "portCRC": portCRC,
       "portRunt": portRunt,
       "portOOWColl": portOOWColl,
       "portNoResorces": portNoResorces,
       "portRecBytes": portRecBytes,
       "portGiants": portGiants,
       "portRedundCrt": portRedundCrt,
       "portRedundType": portRedundType,
       "portRedundStatus": portRedundStatus,
       "portForceLinkType": portForceLinkType,
       "tokenRingP": tokenRingP,
       "stationP": stationP,
       "stationPortLinkStatus": stationPortLinkStatus,
       "stationPortLinkStateTime": stationPortLinkStateTime,
       "ringP": ringP,
       "ringPortLinkStatus": ringPortLinkStatus,
       "ringPortLinkStateTime": ringPortLinkStateTime,
       "fddiP": fddiP,
       "repeaterTables": repeaterTables,
       "bridge": bridge,
       "bridgeRev1": bridgeRev1,
       "bdgdevice": bdgdevice,
       "bdgdeviceDisableBdg": bdgdeviceDisableBdg,
       "bdgdeviceRestoreSettings": bdgdeviceRestoreSettings,
       "bdgdeviceBdgName": bdgdeviceBdgName,
       "bdgdeviceNumPorts": bdgdeviceNumPorts,
       "bdgdeviceType": bdgdeviceType,
       "bdgdeviceVersion": bdgdeviceVersion,
       "bdgdeviceLocation": bdgdeviceLocation,
       "bdgdeviceStatus": bdgdeviceStatus,
       "bdgdeviceRestartBdg": bdgdeviceRestartBdg,
       "bdgdeviceFrFwd": bdgdeviceFrFwd,
       "bdgdeviceFrRx": bdgdeviceFrRx,
       "bdgdeviceFrFlt": bdgdeviceFrFlt,
       "bdgdeviceErr": bdgdeviceErr,
       "bdgdeviceSwitchSetting": bdgdeviceSwitchSetting,
       "bdgdeviceNumRestarts": bdgdeviceNumRestarts,
       "bdgdeviceTypeFiltering": bdgdeviceTypeFiltering,
       "bdgdeviceSTAProtocol": bdgdeviceSTAProtocol,
       "bdgdeviceBridgeID": bdgdeviceBridgeID,
       "bdgdeviceTopChgCnt": bdgdeviceTopChgCnt,
       "bdgdeviceRootCost": bdgdeviceRootCost,
       "bdgdeviceRootPort": bdgdeviceRootPort,
       "bdgdeviceHelloTime": bdgdeviceHelloTime,
       "bdgdeviceBdgMaxAge": bdgdeviceBdgMaxAge,
       "bdgdeviceBdgFwdDly": bdgdeviceBdgFwdDly,
       "bdgdeviceTimeTopChg": bdgdeviceTimeTopChg,
       "bdgdeviceTopChg": bdgdeviceTopChg,
       "bdgdeviceDesigRoot": bdgdeviceDesigRoot,
       "bdgdeviceMaxAge": bdgdeviceMaxAge,
       "bdgdeviceHoldTime": bdgdeviceHoldTime,
       "bdgdeviceFwdDly": bdgdeviceFwdDly,
       "bdgdeviceBdgHello": bdgdeviceBdgHello,
       "bdgdeviceBdgPriority": bdgdeviceBdgPriority,
       "bdgdeviceResetCounts": bdgdeviceResetCounts,
       "bdgdeviceUptime": bdgdeviceUptime,
       "bdgdeviceTrapType": bdgdeviceTrapType,
       "bdgPort": bdgPort,
       "bdgPortAddress": bdgPortAddress,
       "bdgPortName": bdgPortName,
       "bdgPortType": bdgPortType,
       "bdgPortStatus": bdgPortStatus,
       "bdgPortNetName": bdgPortNetName,
       "bdgPortFrRx": bdgPortFrRx,
       "bdgPortDisInb": bdgPortDisInb,
       "bdgPortFwdOutb": bdgPortFwdOutb,
       "bdgPortDisLOB": bdgPortDisLOB,
       "bdgPortDisTDE": bdgPortDisTDE,
       "bdgPortDisErr": bdgPortDisErr,
       "bdgPortColl": bdgPortColl,
       "bdgPortTxAbrt": bdgPortTxAbrt,
       "bdgPortOowColl": bdgPortOowColl,
       "bdgPortCRCErr": bdgPortCRCErr,
       "bdgPortFrAlErr": bdgPortFrAlErr,
       "bdgPortPriority": bdgPortPriority,
       "bdgPortState": bdgPortState,
       "bdgPortPathCost": bdgPortPathCost,
       "bdgPortDesigCost": bdgPortDesigCost,
       "bdgPortDesigBrdg": bdgPortDesigBrdg,
       "bdgPortDesigPort": bdgPortDesigPort,
       "bdgPortTopChgAck": bdgPortTopChgAck,
       "bdgPortDesigRoot": bdgPortDesigRoot,
       "bdgPortRuntPackets": bdgPortRuntPackets,
       "bdgPortOversizePackets": bdgPortOversizePackets,
       "bdgPortFrFilt": bdgPortFrFilt,
       "filterDB": filterDB,
       "acqDB": acqDB,
       "acqStats": acqStats,
       "acqTotalEntries": acqTotalEntries,
       "acqMaxEntries": acqMaxEntries,
       "acqStaticEntries": acqStaticEntries,
       "acqStaticAgeTime": acqStaticAgeTime,
       "acqDynEntries": acqDynEntries,
       "acqDynAgeTime": acqDynAgeTime,
       "acqEraseDatabase": acqEraseDatabase,
       "acqOptions": acqOptions,
       "acqCreate00": acqCreate00,
       "acqCreate20": acqCreate20,
       "acqCreate01": acqCreate01,
       "acqCreate21": acqCreate21,
       "acqDelete": acqDelete,
       "acqDispType": acqDispType,
       "acqDispOutp1": acqDispOutp1,
       "acqDispOutp2": acqDispOutp2,
       "acqSrcAddress": acqSrcAddress,
       "permDB": permDB,
       "permStats": permStats,
       "permMaxEntries": permMaxEntries,
       "permCurrEntries": permCurrEntries,
       "permEraseDatabase": permEraseDatabase,
       "permOptions": permOptions,
       "permCreate00": permCreate00,
       "permCreate20": permCreate20,
       "permCreate01": permCreate01,
       "permCreate21": permCreate21,
       "permDelete": permDelete,
       "permDispType": permDispType,
       "permDispOutp1": permDispOutp1,
       "permDispOutp2": permDispOutp2,
       "permSrcAddress": permSrcAddress,
       "specialDB": specialDB,
       "specStats": specStats,
       "specNumEntries": specNumEntries,
       "specMaxEntries": specMaxEntries,
       "specNextFilterNum": specNextFilterNum,
       "specFilters": specFilters,
       "specEnable": specEnable,
       "specPort1": specPort1,
       "specPort2": specPort2,
       "specDestAddress": specDestAddress,
       "specSrcAddress": specSrcAddress,
       "specType": specType,
       "specDataField": specDataField,
       "specDeleteFilter": specDeleteFilter,
       "trapTypes": trapTypes,
       "bdgTables": bdgTables,
       "router": router,
       "product": product,
       "productRev1": productRev1,
       "iRBM": iRBM,
       "iRBMRevision": iRBMRevision,
       "iRBMPortAssociation": iRBMPortAssociation,
       "subsystem": subsystem,
       "mMAC": mMAC,
       "fnb": fnb,
       "fnbConnectedLeft": fnbConnectedLeft,
       "fnbConnectedRight": fnbConnectedRight,
       "fnbBoardBypassState": fnbBoardBypassState,
       "layerMgmt": layerMgmt,
       "lmcommon": lmcommon,
       "mAC": mAC,
       "ieee8023": ieee8023,
       "pcIF": pcIF,
       "pcIfRev": pcIfRev,
       "pcDeviceName": pcDeviceName,
       "pcBoardType": pcBoardType,
       "pcOwnerName": pcOwnerName,
       "pcLocation": pcLocation,
       "pcMMACAddr": pcMMACAddr,
       "pcMMACBoard": pcMMACBoard,
       "pcMMACPort": pcMMACPort,
       "pcApplication": pcApplication,
       "pcDriverRev": pcDriverRev,
       "pcOnboardMemory": pcOnboardMemory,
       "pcComment": pcComment,
       "pcMACAddr": pcMACAddr,
       "pcFramesXmit": pcFramesXmit,
       "pcBytesXmit": pcBytesXmit,
       "pcMcastXmit": pcMcastXmit,
       "pcBcastXmit": pcBcastXmit,
       "pcDeferXmit": pcDeferXmit,
       "pcSglColl": pcSglColl,
       "pcMultiColl": pcMultiColl,
       "pcTotXmitErrs": pcTotXmitErrs,
       "pcLateColls": pcLateColls,
       "pcXcessColls": pcXcessColls,
       "pcCarrErr": pcCarrErr,
       "pcFramesRec": pcFramesRec,
       "pcBytesRec": pcBytesRec,
       "pcMcastRec": pcMcastRec,
       "pcBcastRec": pcBcastRec,
       "pcTotRecErrs": pcTotRecErrs,
       "pcTooLong": pcTooLong,
       "pcTooShort": pcTooShort,
       "pcAlignErrs": pcAlignErrs,
       "pcCRCErrs": pcCRCErrs,
       "pcLenErrs": pcLenErrs,
       "pcIntRecErr": pcIntRecErr,
       "pcSqeErr": pcSqeErr}
)
