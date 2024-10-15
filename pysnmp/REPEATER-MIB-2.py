# SNMP MIB module (REPEATER-MIB-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REPEATER-MIB-2
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:18 2024
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

(commonRev1,
 product,
 repeaterRev1,
 repeaterRev2,
 subSysMMAC,
 sysChassis,
 sysRepeaters) = mibBuilder.importSymbols(
    "IRM-OIDS",
    "commonRev1",
    "product",
    "repeaterRev1",
    "repeaterRev2",
    "subSysMMAC",
    "sysChassis",
    "sysRepeaters")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

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
        ValueSizeConstraint(7, 7),
    )


_CurrentTime_Type.__name__ = "OctetString"
_CurrentTime_Object = MibScalar
currentTime = _CurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 4),
    _CurrentTime_Type()
)
currentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentTime.setStatus("optional")


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
    currentDate.setStatus("optional")
_MACAddress_Type = OctetString
_MACAddress_Object = MibScalar
mACAddress = _MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 6),
    _MACAddress_Type()
)
mACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mACAddress.setStatus("mandatory")
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
_SoidMINIMMAC_ObjectIdentity = ObjectIdentity
soidMINIMMAC = _SoidMINIMMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3, 1)
)
_SoidMRXI_ObjectIdentity = ObjectIdentity
soidMRXI = _SoidMRXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3, 2)
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("mMAC3", 1),
          ("mMAC3FNBShunt", 10),
          ("mMAC5", 2),
          ("mMAC5FNBShunt", 11),
          ("mMAC8FNBShunt", 9),
          ("mMACm3Shunt", 7),
          ("mMACm5Shunt", 8),
          ("mMACm8FNB", 12),
          ("mMACm8Shunt", 6),
          ("minimmac", 3),
          ("mrxi1", 4),
          ("mrxi2", 5))
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
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("mMAC3", 3),
          ("mMAC5", 5),
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
devicePortsOn.setMaxAccess("read-write")
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
    deviceTotalErrors.setStatus("optional")
_DeviceTransmitColls_Type = Counter32
_DeviceTransmitColls_Object = MibScalar
deviceTransmitColls = _DeviceTransmitColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 9),
    _DeviceTransmitColls_Type()
)
deviceTransmitColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTransmitColls.setStatus("optional")
_DeviceRecColls_Type = Counter32
_DeviceRecColls_Object = MibScalar
deviceRecColls = _DeviceRecColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 10),
    _DeviceRecColls_Type()
)
deviceRecColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRecColls.setStatus("optional")
_DeviceAligns_Type = Counter32
_DeviceAligns_Object = MibScalar
deviceAligns = _DeviceAligns_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 11),
    _DeviceAligns_Type()
)
deviceAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAligns.setStatus("optional")
_DeviceCRCs_Type = Counter32
_DeviceCRCs_Object = MibScalar
deviceCRCs = _DeviceCRCs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 12),
    _DeviceCRCs_Type()
)
deviceCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCRCs.setStatus("optional")
_DeviceRunts_Type = Counter32
_DeviceRunts_Object = MibScalar
deviceRunts = _DeviceRunts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 13),
    _DeviceRunts_Type()
)
deviceRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRunts.setStatus("optional")
_DeviceOOWColls_Type = Counter32
_DeviceOOWColls_Object = MibScalar
deviceOOWColls = _DeviceOOWColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 14),
    _DeviceOOWColls_Type()
)
deviceOOWColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOOWColls.setStatus("optional")
_DeviceNoResources_Type = Counter32
_DeviceNoResources_Object = MibScalar
deviceNoResources = _DeviceNoResources_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 15),
    _DeviceNoResources_Type()
)
deviceNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNoResources.setStatus("optional")
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
    deviceGiantFrames.setStatus("optional")
_DeviceRestart_Type = Integer32
_DeviceRestart_Object = MibScalar
deviceRestart = _DeviceRestart_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 18),
    _DeviceRestart_Type()
)
deviceRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceRestart.setStatus("mandatory")
_DeviceResetCounters_Type = Integer32
_DeviceResetCounters_Object = MibScalar
deviceResetCounters = _DeviceResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 19),
    _DeviceResetCounters_Type()
)
deviceResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceResetCounters.setStatus("mandatory")
_DeviceRedundantCts_Type = Integer32
_DeviceRedundantCts_Object = MibScalar
deviceRedundantCts = _DeviceRedundantCts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 20),
    _DeviceRedundantCts_Type()
)
deviceRedundantCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRedundantCts.setStatus("optional")


class _DeviceTimeBase_Type(Integer32):
    """Custom type deviceTimeBase based on Integer32"""
    defaultValue = 10


_DeviceTimeBase_Object = MibScalar
deviceTimeBase = _DeviceTimeBase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 24),
    _DeviceTimeBase_Type()
)
deviceTimeBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceTimeBase.setStatus("optional")
_DeviceResetRedundancy_Type = Integer32
_DeviceResetRedundancy_Object = MibScalar
deviceResetRedundancy = _DeviceResetRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 25),
    _DeviceResetRedundancy_Type()
)
deviceResetRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceResetRedundancy.setStatus("optional")


class _DeviceSrcAddrAgingTime_Type(Integer32):
    """Custom type deviceSrcAddrAgingTime based on Integer32"""
    defaultValue = 60


_DeviceSrcAddrAgingTime_Object = MibScalar
deviceSrcAddrAgingTime = _DeviceSrcAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 26),
    _DeviceSrcAddrAgingTime_Type()
)
deviceSrcAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSrcAddrAgingTime.setStatus("optional")


class _DeviceSrcAddrTraps_Type(Integer32):
    """Custom type deviceSrcAddrTraps based on Integer32"""
    defaultValue = 2

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
    deviceSrcAddrTraps.setStatus("optional")


class _DeviceSrcAddrLocked_Type(Integer32):
    """Custom type deviceSrcAddrLocked based on Integer32"""
    defaultValue = 1

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
    deviceSrcAddrLocked.setStatus("optional")
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
_DeviceRestoreDefaults_Type = Integer32
_DeviceRestoreDefaults_Object = MibScalar
deviceRestoreDefaults = _DeviceRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 32),
    _DeviceRestoreDefaults_Type()
)
deviceRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceRestoreDefaults.setStatus("optional")
_DeviceActiveUsers_Type = Integer32
_DeviceActiveUsers_Object = MibScalar
deviceActiveUsers = _DeviceActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 33),
    _DeviceActiveUsers_Type()
)
deviceActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceActiveUsers.setStatus("optional")
_DeviceBroadPkts_Type = Counter32
_DeviceBroadPkts_Object = MibScalar
deviceBroadPkts = _DeviceBroadPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 48),
    _DeviceBroadPkts_Type()
)
deviceBroadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceBroadPkts.setStatus("optional")
_DeviceMultPkts_Type = Counter32
_DeviceMultPkts_Object = MibScalar
deviceMultPkts = _DeviceMultPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 49),
    _DeviceMultPkts_Type()
)
deviceMultPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMultPkts.setStatus("optional")
_DeviceThdPartyOccupiedSlots_Type = Integer32
_DeviceThdPartyOccupiedSlots_Object = MibScalar
deviceThdPartyOccupiedSlots = _DeviceThdPartyOccupiedSlots_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 51),
    _DeviceThdPartyOccupiedSlots_Type()
)
deviceThdPartyOccupiedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceThdPartyOccupiedSlots.setStatus("optional")
_DeviceImimOccupiedSlots_Type = Integer32
_DeviceImimOccupiedSlots_Object = MibScalar
deviceImimOccupiedSlots = _DeviceImimOccupiedSlots_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 52),
    _DeviceImimOccupiedSlots_Type()
)
deviceImimOccupiedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceImimOccupiedSlots.setStatus("optional")


class _DeviceLinkTraps_Type(Integer32):
    """Custom type deviceLinkTraps based on Integer32"""
    defaultValue = 2

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


_DeviceLinkTraps_Type.__name__ = "Integer32"
_DeviceLinkTraps_Object = MibScalar
deviceLinkTraps = _DeviceLinkTraps_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 54),
    _DeviceLinkTraps_Type()
)
deviceLinkTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceLinkTraps.setStatus("optional")


class _DeviceSegTraps_Type(Integer32):
    """Custom type deviceSegTraps based on Integer32"""
    defaultValue = 2

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


_DeviceSegTraps_Type.__name__ = "Integer32"
_DeviceSegTraps_Object = MibScalar
deviceSegTraps = _DeviceSegTraps_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 55),
    _DeviceSegTraps_Type()
)
deviceSegTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSegTraps.setStatus("optional")


class _CtIPDefaultFrameType_Type(Integer32):
    """Custom type ctIPDefaultFrameType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("snap8022", 2))
    )


_CtIPDefaultFrameType_Type.__name__ = "Integer32"
_CtIPDefaultFrameType_Object = MibScalar
ctIPDefaultFrameType = _CtIPDefaultFrameType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 1, 56),
    _CtIPDefaultFrameType_Type()
)
ctIPDefaultFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIPDefaultFrameType.setStatus("mandatory")
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


class _RedundancyPollInterval_Type(Integer32):
    """Custom type redundancyPollInterval based on Integer32"""
    defaultValue = 3


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


class _RedundancyRetryCount_Type(Integer32):
    """Custom type redundancyRetryCount based on Integer32"""
    defaultValue = 0


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
    defaultValue = 1

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
    defaultValue = 1

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


class _DevTrafficThreshold_Type(Integer32):
    """Custom type devTrafficThreshold based on Integer32"""
    defaultValue = 1000


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
    defaultValue = 1

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
    defaultValue = 1

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


class _DevErrorThreshold_Type(Integer32):
    """Custom type devErrorThreshold based on Integer32"""
    defaultValue = 10


_DevErrorThreshold_Object = MibScalar
devErrorThreshold = _DevErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 3, 2),
    _DevErrorThreshold_Type()
)
devErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devErrorThreshold.setStatus("mandatory")


class _DevErrorSource_Type(Integer32):
    """Custom type devErrorSource based on Integer32"""
    defaultValue = 63


_DevErrorSource_Object = MibScalar
devErrorSource = _DevErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 3, 3),
    _DevErrorSource_Type()
)
devErrorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devErrorSource.setStatus("mandatory")
_DevBroad_ObjectIdentity = ObjectIdentity
devBroad = _DevBroad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 4)
)


class _DevBroadEnable_Type(Integer32):
    """Custom type devBroadEnable based on Integer32"""
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


_DevBroadEnable_Type.__name__ = "Integer32"
_DevBroadEnable_Object = MibScalar
devBroadEnable = _DevBroadEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 4, 1),
    _DevBroadEnable_Type()
)
devBroadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devBroadEnable.setStatus("mandatory")
_DevBroadThreshold_Type = Integer32
_DevBroadThreshold_Object = MibScalar
devBroadThreshold = _DevBroadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 1, 4, 2),
    _DevBroadThreshold_Type()
)
devBroadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devBroadThreshold.setStatus("mandatory")
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
    defaultValue = 1

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


class _BdTrafficThreshold_Type(Integer32):
    """Custom type bdTrafficThreshold based on Integer32"""
    defaultValue = 100


_BdTrafficThreshold_Object = MibScalar
bdTrafficThreshold = _BdTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 1, 2),
    _BdTrafficThreshold_Type()
)
bdTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdTrafficThreshold.setStatus("mandatory")


class _BdTrafficBdDisable_Type(Integer32):
    """Custom type bdTrafficBdDisable based on Integer32"""
    defaultValue = 1

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


_BdTrafficBdDisable_Type.__name__ = "Integer32"
_BdTrafficBdDisable_Object = MibScalar
bdTrafficBdDisable = _BdTrafficBdDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 1, 3),
    _BdTrafficBdDisable_Type()
)
bdTrafficBdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdTrafficBdDisable.setStatus("mandatory")
_BdColls_ObjectIdentity = ObjectIdentity
bdColls = _BdColls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 2)
)


class _BdCollsEnable_Type(Integer32):
    """Custom type bdCollsEnable based on Integer32"""
    defaultValue = 1

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


class _BdCollsThreshold_Type(Integer32):
    """Custom type bdCollsThreshold based on Integer32"""
    defaultValue = 1


_BdCollsThreshold_Object = MibScalar
bdCollsThreshold = _BdCollsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 2, 2),
    _BdCollsThreshold_Type()
)
bdCollsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdCollsThreshold.setStatus("mandatory")


class _BdCollsBdDisable_Type(Integer32):
    """Custom type bdCollsBdDisable based on Integer32"""
    defaultValue = 1

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


_BdCollsBdDisable_Type.__name__ = "Integer32"
_BdCollsBdDisable_Object = MibScalar
bdCollsBdDisable = _BdCollsBdDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 2, 3),
    _BdCollsBdDisable_Type()
)
bdCollsBdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdCollsBdDisable.setStatus("mandatory")
_BdError_ObjectIdentity = ObjectIdentity
bdError = _BdError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3)
)


class _BdErrorEnable_Type(Integer32):
    """Custom type bdErrorEnable based on Integer32"""
    defaultValue = 1

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


class _BdErrorThreshold_Type(Integer32):
    """Custom type bdErrorThreshold based on Integer32"""
    defaultValue = 10


_BdErrorThreshold_Object = MibScalar
bdErrorThreshold = _BdErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3, 2),
    _BdErrorThreshold_Type()
)
bdErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdErrorThreshold.setStatus("mandatory")


class _BdErrorSource_Type(Integer32):
    """Custom type bdErrorSource based on Integer32"""
    defaultValue = 63


_BdErrorSource_Object = MibScalar
bdErrorSource = _BdErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3, 3),
    _BdErrorSource_Type()
)
bdErrorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdErrorSource.setStatus("mandatory")


class _BdErrorBdDisable_Type(Integer32):
    """Custom type bdErrorBdDisable based on Integer32"""
    defaultValue = 1

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


_BdErrorBdDisable_Type.__name__ = "Integer32"
_BdErrorBdDisable_Object = MibScalar
bdErrorBdDisable = _BdErrorBdDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 3, 4),
    _BdErrorBdDisable_Type()
)
bdErrorBdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdErrorBdDisable.setStatus("mandatory")
_BdBroad_ObjectIdentity = ObjectIdentity
bdBroad = _BdBroad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 4)
)


class _BdBroadEnable_Type(Integer32):
    """Custom type bdBroadEnable based on Integer32"""
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


_BdBroadEnable_Type.__name__ = "Integer32"
_BdBroadEnable_Object = MibScalar
bdBroadEnable = _BdBroadEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 4, 1),
    _BdBroadEnable_Type()
)
bdBroadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdBroadEnable.setStatus("mandatory")
_BdBroadThreshold_Type = Integer32
_BdBroadThreshold_Object = MibScalar
bdBroadThreshold = _BdBroadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 4, 2),
    _BdBroadThreshold_Type()
)
bdBroadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdBroadThreshold.setStatus("mandatory")


class _BdBroadDisable_Type(Integer32):
    """Custom type bdBroadDisable based on Integer32"""
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


_BdBroadDisable_Type.__name__ = "Integer32"
_BdBroadDisable_Object = MibScalar
bdBroadDisable = _BdBroadDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 2, 4, 3),
    _BdBroadDisable_Type()
)
bdBroadDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdBroadDisable.setStatus("mandatory")
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
    defaultValue = 1

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


class _PortTrafficThreshold_Type(Integer32):
    """Custom type portTrafficThreshold based on Integer32"""
    defaultValue = 100


_PortTrafficThreshold_Object = MibScalar
portTrafficThreshold = _PortTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 1, 2),
    _PortTrafficThreshold_Type()
)
portTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrafficThreshold.setStatus("mandatory")


class _PortTrafficPortDisable_Type(Integer32):
    """Custom type portTrafficPortDisable based on Integer32"""
    defaultValue = 1

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


_PortTrafficPortDisable_Type.__name__ = "Integer32"
_PortTrafficPortDisable_Object = MibScalar
portTrafficPortDisable = _PortTrafficPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 1, 3),
    _PortTrafficPortDisable_Type()
)
portTrafficPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrafficPortDisable.setStatus("mandatory")
_PortColls_ObjectIdentity = ObjectIdentity
portColls = _PortColls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 2)
)


class _PortCollsEnable_Type(Integer32):
    """Custom type portCollsEnable based on Integer32"""
    defaultValue = 1

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


class _PortCollsThreshold_Type(Integer32):
    """Custom type portCollsThreshold based on Integer32"""
    defaultValue = 1


_PortCollsThreshold_Object = MibScalar
portCollsThreshold = _PortCollsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 2, 2),
    _PortCollsThreshold_Type()
)
portCollsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCollsThreshold.setStatus("mandatory")


class _PortCollsPortDisable_Type(Integer32):
    """Custom type portCollsPortDisable based on Integer32"""
    defaultValue = 1

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


_PortCollsPortDisable_Type.__name__ = "Integer32"
_PortCollsPortDisable_Object = MibScalar
portCollsPortDisable = _PortCollsPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 2, 3),
    _PortCollsPortDisable_Type()
)
portCollsPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCollsPortDisable.setStatus("mandatory")
_PortError_ObjectIdentity = ObjectIdentity
portError = _PortError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3)
)


class _PortErrorEnable_Type(Integer32):
    """Custom type portErrorEnable based on Integer32"""
    defaultValue = 1

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


class _PortErrorThreshold_Type(Integer32):
    """Custom type portErrorThreshold based on Integer32"""
    defaultValue = 10


_PortErrorThreshold_Object = MibScalar
portErrorThreshold = _PortErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3, 2),
    _PortErrorThreshold_Type()
)
portErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrorThreshold.setStatus("mandatory")


class _PortErrorSource_Type(Integer32):
    """Custom type portErrorSource based on Integer32"""
    defaultValue = 63


_PortErrorSource_Object = MibScalar
portErrorSource = _PortErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3, 3),
    _PortErrorSource_Type()
)
portErrorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrorSource.setStatus("mandatory")


class _PortErrorPortDisable_Type(Integer32):
    """Custom type portErrorPortDisable based on Integer32"""
    defaultValue = 1

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


_PortErrorPortDisable_Type.__name__ = "Integer32"
_PortErrorPortDisable_Object = MibScalar
portErrorPortDisable = _PortErrorPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 3, 4),
    _PortErrorPortDisable_Type()
)
portErrorPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrorPortDisable.setStatus("mandatory")
_PortBroad_ObjectIdentity = ObjectIdentity
portBroad = _PortBroad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 4)
)


class _PortBroadEnable_Type(Integer32):
    """Custom type portBroadEnable based on Integer32"""
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


_PortBroadEnable_Type.__name__ = "Integer32"
_PortBroadEnable_Object = MibScalar
portBroadEnable = _PortBroadEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 4, 1),
    _PortBroadEnable_Type()
)
portBroadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBroadEnable.setStatus("mandatory")
_PortBroadThreshold_Type = Counter32
_PortBroadThreshold_Object = MibScalar
portBroadThreshold = _PortBroadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 4, 2),
    _PortBroadThreshold_Type()
)
portBroadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBroadThreshold.setStatus("mandatory")


class _PortBroadDisable_Type(Integer32):
    """Custom type portBroadDisable based on Integer32"""
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


_PortBroadDisable_Type.__name__ = "Integer32"
_PortBroadDisable_Object = MibScalar
portBroadDisable = _PortBroadDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 1, 9, 3, 4, 3),
    _PortBroadDisable_Type()
)
portBroadDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBroadDisable.setStatus("mandatory")
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
    deviceTRTokenRingPortsOn.setStatus("deprecated")
_DeviceTRTotalTokenRingPorts_Type = Integer32
_DeviceTRTotalTokenRingPorts_Object = MibScalar
deviceTRTotalTokenRingPorts = _DeviceTRTotalTokenRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 2),
    _DeviceTRTotalTokenRingPorts_Type()
)
deviceTRTotalTokenRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingPorts.setStatus("deprecated")
_DeviceTRTotalTokenRingRingPortsOn_Type = Integer32
_DeviceTRTotalTokenRingRingPortsOn_Object = MibScalar
deviceTRTotalTokenRingRingPortsOn = _DeviceTRTotalTokenRingRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 3),
    _DeviceTRTotalTokenRingRingPortsOn_Type()
)
deviceTRTotalTokenRingRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingRingPortsOn.setStatus("deprecated")
_DeviceTRTotalTokenRingRingPorts_Type = Integer32
_DeviceTRTotalTokenRingRingPorts_Object = MibScalar
deviceTRTotalTokenRingRingPorts = _DeviceTRTotalTokenRingRingPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 4),
    _DeviceTRTotalTokenRingRingPorts_Type()
)
deviceTRTotalTokenRingRingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingRingPorts.setStatus("deprecated")
_DeviceTRTotalTokenRingRings_Type = Integer32
_DeviceTRTotalTokenRingRings_Object = MibScalar
deviceTRTotalTokenRingRings = _DeviceTRTotalTokenRingRings_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 5),
    _DeviceTRTotalTokenRingRings_Type()
)
deviceTRTotalTokenRingRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingRings.setStatus("deprecated")
_DeviceTRTotalTokenRingBoards_Type = Integer32
_DeviceTRTotalTokenRingBoards_Object = MibScalar
deviceTRTotalTokenRingBoards = _DeviceTRTotalTokenRingBoards_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 6),
    _DeviceTRTotalTokenRingBoards_Type()
)
deviceTRTotalTokenRingBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTotalTokenRingBoards.setStatus("deprecated")
_DeviceTRTokenRingBoardMap_Type = Integer32
_DeviceTRTokenRingBoardMap_Object = MibScalar
deviceTRTokenRingBoardMap = _DeviceTRTokenRingBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 1, 3, 7),
    _DeviceTRTokenRingBoardMap_Type()
)
deviceTRTokenRingBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTRTokenRingBoardMap.setStatus("deprecated")
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
_BoardPortsOn_Type = Integer32
_BoardPortsOn_Object = MibScalar
boardPortsOn = _BoardPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 6),
    _BoardPortsOn_Type()
)
boardPortsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardPortsOn.setStatus("mandatory")
_BoardActiveUsers_Type = Integer32
_BoardActiveUsers_Object = MibScalar
boardActiveUsers = _BoardActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 1, 8),
    _BoardActiveUsers_Type()
)
boardActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardActiveUsers.setStatus("mandatory")
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
_BoardTotalErrors_Type = Counter32
_BoardTotalErrors_Object = MibScalar
boardTotalErrors = _BoardTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 2),
    _BoardTotalErrors_Type()
)
boardTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalErrors.setStatus("mandatory")
_BoardTransColls_Type = Counter32
_BoardTransColls_Object = MibScalar
boardTransColls = _BoardTransColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 3),
    _BoardTransColls_Type()
)
boardTransColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTransColls.setStatus("mandatory")
_BoardRecColls_Type = Counter32
_BoardRecColls_Object = MibScalar
boardRecColls = _BoardRecColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 4),
    _BoardRecColls_Type()
)
boardRecColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRecColls.setStatus("mandatory")
_BoardAligns_Type = Counter32
_BoardAligns_Object = MibScalar
boardAligns = _BoardAligns_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 5),
    _BoardAligns_Type()
)
boardAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardAligns.setStatus("mandatory")
_BoardCRCs_Type = Counter32
_BoardCRCs_Object = MibScalar
boardCRCs = _BoardCRCs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 6),
    _BoardCRCs_Type()
)
boardCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardCRCs.setStatus("mandatory")
_BoardRunts_Type = Counter32
_BoardRunts_Object = MibScalar
boardRunts = _BoardRunts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 7),
    _BoardRunts_Type()
)
boardRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRunts.setStatus("mandatory")
_BoardOOWColls_Type = Counter32
_BoardOOWColls_Object = MibScalar
boardOOWColls = _BoardOOWColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 8),
    _BoardOOWColls_Type()
)
boardOOWColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardOOWColls.setStatus("mandatory")
_BoardNoResources_Type = Counter32
_BoardNoResources_Object = MibScalar
boardNoResources = _BoardNoResources_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 9),
    _BoardNoResources_Type()
)
boardNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardNoResources.setStatus("mandatory")
_BoardRecBytes_Type = Counter32
_BoardRecBytes_Object = MibScalar
boardRecBytes = _BoardRecBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 10),
    _BoardRecBytes_Type()
)
boardRecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRecBytes.setStatus("mandatory")
_BoardGiants_Type = Counter32
_BoardGiants_Object = MibScalar
boardGiants = _BoardGiants_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 11),
    _BoardGiants_Type()
)
boardGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardGiants.setStatus("mandatory")
_BoardBroadPkts_Type = Counter32
_BoardBroadPkts_Object = MibScalar
boardBroadPkts = _BoardBroadPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 26),
    _BoardBroadPkts_Type()
)
boardBroadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardBroadPkts.setStatus("mandatory")
_BoardMultPkts_Type = Counter32
_BoardMultPkts_Object = MibScalar
boardMultPkts = _BoardMultPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 2, 27),
    _BoardMultPkts_Type()
)
boardMultPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardMultPkts.setStatus("mandatory")
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
    boardTotalRingPorts.setStatus("deprecated")
_BoardTotalStationPorts_Type = Integer32
_BoardTotalStationPorts_Object = MibScalar
boardTotalStationPorts = _BoardTotalStationPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 2),
    _BoardTotalStationPorts_Type()
)
boardTotalStationPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalStationPorts.setStatus("deprecated")


class _BoardModeStatus_Type(Integer32):
    """Custom type boardModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("management", 1))
    )


_BoardModeStatus_Type.__name__ = "Integer32"
_BoardModeStatus_Object = MibScalar
boardModeStatus = _BoardModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 3),
    _BoardModeStatus_Type()
)
boardModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardModeStatus.setStatus("deprecated")
_BoardTotalRingPortsOn_Type = Integer32
_BoardTotalRingPortsOn_Object = MibScalar
boardTotalRingPortsOn = _BoardTotalRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 4),
    _BoardTotalRingPortsOn_Type()
)
boardTotalRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalRingPortsOn.setStatus("deprecated")
_BoardTotalStationPortsOn_Type = Integer32
_BoardTotalStationPortsOn_Object = MibScalar
boardTotalStationPortsOn = _BoardTotalStationPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 5),
    _BoardTotalStationPortsOn_Type()
)
boardTotalStationPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardTotalStationPortsOn.setStatus("deprecated")


class _BoardSpeed_Type(Integer32):
    """Custom type boardSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("fourMhz", 4),
          ("sixteenMhz", 16))
    )


_BoardSpeed_Type.__name__ = "Integer32"
_BoardSpeed_Object = MibScalar
boardSpeed = _BoardSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 6),
    _BoardSpeed_Type()
)
boardSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardSpeed.setStatus("deprecated")


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
    boardRingSpeedFault.setStatus("deprecated")
_BoardFirstRingPort_Type = Integer32
_BoardFirstRingPort_Object = MibScalar
boardFirstRingPort = _BoardFirstRingPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 3, 3, 9),
    _BoardFirstRingPort_Type()
)
boardFirstRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardFirstRingPort.setStatus("deprecated")
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
    portSourceAddr.setStatus("optional")
_PortActiveUsers_Type = Integer32
_PortActiveUsers_Object = MibScalar
portActiveUsers = _PortActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 1, 6),
    _PortActiveUsers_Type()
)
portActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portActiveUsers.setStatus("optional")
_EthernetP_ObjectIdentity = ObjectIdentity
ethernetP = _EthernetP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2)
)


class _PortTopologyType_Type(Integer32):
    """Custom type portTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("station", 1),
          ("trunk", 2))
    )


_PortTopologyType_Type.__name__ = "Integer32"
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
_PortTotalPkts_Type = Counter32
_PortTotalPkts_Object = MibScalar
portTotalPkts = _PortTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 4),
    _PortTotalPkts_Type()
)
portTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTotalPkts.setStatus("mandatory")
_PortTotalErrors_Type = Counter32
_PortTotalErrors_Object = MibScalar
portTotalErrors = _PortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 5),
    _PortTotalErrors_Type()
)
portTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTotalErrors.setStatus("mandatory")
_PortTransmitColls_Type = Counter32
_PortTransmitColls_Object = MibScalar
portTransmitColls = _PortTransmitColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 6),
    _PortTransmitColls_Type()
)
portTransmitColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTransmitColls.setStatus("mandatory")
_PortRecColls_Type = Counter32
_PortRecColls_Object = MibScalar
portRecColls = _PortRecColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 7),
    _PortRecColls_Type()
)
portRecColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRecColls.setStatus("mandatory")
_PortAligns_Type = Counter32
_PortAligns_Object = MibScalar
portAligns = _PortAligns_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 8),
    _PortAligns_Type()
)
portAligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAligns.setStatus("mandatory")
_PortCRCs_Type = Counter32
_PortCRCs_Object = MibScalar
portCRCs = _PortCRCs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 9),
    _PortCRCs_Type()
)
portCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCRCs.setStatus("mandatory")
_PortRunts_Type = Counter32
_PortRunts_Object = MibScalar
portRunts = _PortRunts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 10),
    _PortRunts_Type()
)
portRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRunts.setStatus("mandatory")
_PortOOWColls_Type = Counter32
_PortOOWColls_Object = MibScalar
portOOWColls = _PortOOWColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 11),
    _PortOOWColls_Type()
)
portOOWColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOOWColls.setStatus("mandatory")
_PortNoResources_Type = Counter32
_PortNoResources_Object = MibScalar
portNoResources = _PortNoResources_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 12),
    _PortNoResources_Type()
)
portNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNoResources.setStatus("mandatory")
_PortRecBytes_Type = Counter32
_PortRecBytes_Object = MibScalar
portRecBytes = _PortRecBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 13),
    _PortRecBytes_Type()
)
portRecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRecBytes.setStatus("mandatory")
_PortGiantFrames_Type = Counter32
_PortGiantFrames_Object = MibScalar
portGiantFrames = _PortGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 14),
    _PortGiantFrames_Type()
)
portGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGiantFrames.setStatus("mandatory")
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


class _PortForceTrunkType_Type(Integer32):
    """Custom type portForceTrunkType based on Integer32"""
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


_PortForceTrunkType_Type.__name__ = "Integer32"
_PortForceTrunkType_Object = MibScalar
portForceTrunkType = _PortForceTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 18),
    _PortForceTrunkType_Type()
)
portForceTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForceTrunkType.setStatus("mandatory")
_PortBroadPkts_Type = Counter32
_PortBroadPkts_Object = MibScalar
portBroadPkts = _PortBroadPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 33),
    _PortBroadPkts_Type()
)
portBroadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBroadPkts.setStatus("mandatory")
_PortMultPkts_Type = Counter32
_PortMultPkts_Object = MibScalar
portMultPkts = _PortMultPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 2, 34),
    _PortMultPkts_Type()
)
portMultPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMultPkts.setStatus("mandatory")
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
    stationPortLinkStatus.setStatus("deprecated")
_StationPortLinkStateTime_Type = Integer32
_StationPortLinkStateTime_Object = MibScalar
stationPortLinkStateTime = _StationPortLinkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 1, 2),
    _StationPortLinkStateTime_Type()
)
stationPortLinkStateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationPortLinkStateTime.setStatus("deprecated")
_RingP_ObjectIdentity = ObjectIdentity
ringP = _RingP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 3, 2)
)
_FddiP_ObjectIdentity = ObjectIdentity
fddiP = _FddiP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 4, 4)
)
_RepeaterTables_ObjectIdentity = ObjectIdentity
repeaterTables = _RepeaterTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 2, 2, 5)
)
_ProductRev1_ObjectIdentity = ObjectIdentity
productRev1 = _ProductRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1)
)
_Target_ObjectIdentity = ObjectIdentity
target = _Target_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1, 1)
)
_TargetRevision_Type = Integer32
_TargetRevision_Object = MibScalar
targetRevision = _TargetRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1, 1, 1),
    _TargetRevision_Type()
)
targetRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetRevision.setStatus("mandatory")
_TargetPortAssociation_Type = Integer32
_TargetPortAssociation_Object = MibScalar
targetPortAssociation = _TargetPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 5, 1, 1, 2),
    _TargetPortAssociation_Type()
)
targetPortAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetPortAssociation.setStatus("mandatory")
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
_AudibleAlarm_ObjectIdentity = ObjectIdentity
audibleAlarm = _AudibleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2)
)


class _AudibleAlarmEnable_Type(Integer32):
    """Custom type audibleAlarmEnable based on Integer32"""
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


_AudibleAlarmEnable_Type.__name__ = "Integer32"
_AudibleAlarmEnable_Object = MibScalar
audibleAlarmEnable = _AudibleAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1),
    _AudibleAlarmEnable_Type()
)
audibleAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audibleAlarmEnable.setStatus("mandatory")


class _AudibleAlarmOff_Type(Integer32):
    """Custom type audibleAlarmOff based on Integer32"""
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


_AudibleAlarmOff_Type.__name__ = "Integer32"
_AudibleAlarmOff_Object = MibScalar
audibleAlarmOff = _AudibleAlarmOff_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2),
    _AudibleAlarmOff_Type()
)
audibleAlarmOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audibleAlarmOff.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REPEATER-MIB-2",
    **{"deviceType": deviceType,
       "deviceName": deviceName,
       "deviceIPAddress": deviceIPAddress,
       "currentTime": currentTime,
       "currentDate": currentDate,
       "mACAddress": mACAddress,
       "soidIRMSNMP": soidIRMSNMP,
       "soidIRBM": soidIRBM,
       "soidIRM2": soidIRM2,
       "soidMINIMMAC": soidMINIMMAC,
       "soidMRXI": soidMRXI,
       "device": device,
       "deviceMMACType": deviceMMACType,
       "deviceSlots": deviceSlots,
       "deviceOccupiedSlots": deviceOccupiedSlots,
       "devicePortsOn": devicePortsOn,
       "deviceTotalPorts": deviceTotalPorts,
       "deviceTotalPkts": deviceTotalPkts,
       "deviceTotalErrors": deviceTotalErrors,
       "deviceTransmitColls": deviceTransmitColls,
       "deviceRecColls": deviceRecColls,
       "deviceAligns": deviceAligns,
       "deviceCRCs": deviceCRCs,
       "deviceRunts": deviceRunts,
       "deviceOOWColls": deviceOOWColls,
       "deviceNoResources": deviceNoResources,
       "deviceRecBytes": deviceRecBytes,
       "deviceGiantFrames": deviceGiantFrames,
       "deviceRestart": deviceRestart,
       "deviceResetCounters": deviceResetCounters,
       "deviceRedundantCts": deviceRedundantCts,
       "deviceTimeBase": deviceTimeBase,
       "deviceResetRedundancy": deviceResetRedundancy,
       "deviceSrcAddrAgingTime": deviceSrcAddrAgingTime,
       "deviceSrcAddrTraps": deviceSrcAddrTraps,
       "deviceSrcAddrLocked": deviceSrcAddrLocked,
       "deviceEnetBoardMap": deviceEnetBoardMap,
       "deviceTokenRingBoardMap": deviceTokenRingBoardMap,
       "deviceFDDIBoardMap": deviceFDDIBoardMap,
       "deviceRestoreDefaults": deviceRestoreDefaults,
       "deviceActiveUsers": deviceActiveUsers,
       "deviceBroadPkts": deviceBroadPkts,
       "deviceMultPkts": deviceMultPkts,
       "deviceThdPartyOccupiedSlots": deviceThdPartyOccupiedSlots,
       "deviceImimOccupiedSlots": deviceImimOccupiedSlots,
       "deviceLinkTraps": deviceLinkTraps,
       "deviceSegTraps": deviceSegTraps,
       "ctIPDefaultFrameType": ctIPDefaultFrameType,
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
       "devBroad": devBroad,
       "devBroadEnable": devBroadEnable,
       "devBroadThreshold": devBroadThreshold,
       "bdAlrm": bdAlrm,
       "bdTraffic": bdTraffic,
       "bdTrafficEnable": bdTrafficEnable,
       "bdTrafficThreshold": bdTrafficThreshold,
       "bdTrafficBdDisable": bdTrafficBdDisable,
       "bdColls": bdColls,
       "bdCollsEnable": bdCollsEnable,
       "bdCollsThreshold": bdCollsThreshold,
       "bdCollsBdDisable": bdCollsBdDisable,
       "bdError": bdError,
       "bdErrorEnable": bdErrorEnable,
       "bdErrorThreshold": bdErrorThreshold,
       "bdErrorSource": bdErrorSource,
       "bdErrorBdDisable": bdErrorBdDisable,
       "bdBroad": bdBroad,
       "bdBroadEnable": bdBroadEnable,
       "bdBroadThreshold": bdBroadThreshold,
       "bdBroadDisable": bdBroadDisable,
       "portAlrm": portAlrm,
       "portTraffic": portTraffic,
       "portTrafficEnable": portTrafficEnable,
       "portTrafficThreshold": portTrafficThreshold,
       "portTrafficPortDisable": portTrafficPortDisable,
       "portColls": portColls,
       "portCollsEnable": portCollsEnable,
       "portCollsThreshold": portCollsThreshold,
       "portCollsPortDisable": portCollsPortDisable,
       "portError": portError,
       "portErrorEnable": portErrorEnable,
       "portErrorThreshold": portErrorThreshold,
       "portErrorSource": portErrorSource,
       "portErrorPortDisable": portErrorPortDisable,
       "portBroad": portBroad,
       "portBroadEnable": portBroadEnable,
       "portBroadThreshold": portBroadThreshold,
       "portBroadDisable": portBroadDisable,
       "rr2device": rr2device,
       "commonD": commonD,
       "ethernetD": ethernetD,
       "tokenRingD": tokenRingD,
       "deviceTRTokenRingPortsOn": deviceTRTokenRingPortsOn,
       "deviceTRTotalTokenRingPorts": deviceTRTotalTokenRingPorts,
       "deviceTRTotalTokenRingRingPortsOn": deviceTRTotalTokenRingRingPortsOn,
       "deviceTRTotalTokenRingRingPorts": deviceTRTotalTokenRingRingPorts,
       "deviceTRTotalTokenRingRings": deviceTRTotalTokenRingRings,
       "deviceTRTotalTokenRingBoards": deviceTRTotalTokenRingBoards,
       "deviceTRTokenRingBoardMap": deviceTRTokenRingBoardMap,
       "network": network,
       "rr2board": rr2board,
       "commonB": commonB,
       "boardIndex": boardIndex,
       "boardName": boardName,
       "boardType": boardType,
       "boardTotalPorts": boardTotalPorts,
       "boardPortsOn": boardPortsOn,
       "boardActiveUsers": boardActiveUsers,
       "ethernetB": ethernetB,
       "boardTotalPkts": boardTotalPkts,
       "boardTotalErrors": boardTotalErrors,
       "boardTransColls": boardTransColls,
       "boardRecColls": boardRecColls,
       "boardAligns": boardAligns,
       "boardCRCs": boardCRCs,
       "boardRunts": boardRunts,
       "boardOOWColls": boardOOWColls,
       "boardNoResources": boardNoResources,
       "boardRecBytes": boardRecBytes,
       "boardGiants": boardGiants,
       "boardBroadPkts": boardBroadPkts,
       "boardMultPkts": boardMultPkts,
       "tokenRingB": tokenRingB,
       "boardTotalRingPorts": boardTotalRingPorts,
       "boardTotalStationPorts": boardTotalStationPorts,
       "boardModeStatus": boardModeStatus,
       "boardTotalRingPortsOn": boardTotalRingPortsOn,
       "boardTotalStationPortsOn": boardTotalStationPortsOn,
       "boardSpeed": boardSpeed,
       "boardRingSpeedFault": boardRingSpeedFault,
       "boardFirstRingPort": boardFirstRingPort,
       "fddiB": fddiB,
       "rr2port": rr2port,
       "commonP": commonP,
       "portIndex": portIndex,
       "portMediaType": portMediaType,
       "portAdminState": portAdminState,
       "portSourceAddr": portSourceAddr,
       "portActiveUsers": portActiveUsers,
       "ethernetP": ethernetP,
       "portTopologyType": portTopologyType,
       "portLinkStatus": portLinkStatus,
       "portStatus": portStatus,
       "portTotalPkts": portTotalPkts,
       "portTotalErrors": portTotalErrors,
       "portTransmitColls": portTransmitColls,
       "portRecColls": portRecColls,
       "portAligns": portAligns,
       "portCRCs": portCRCs,
       "portRunts": portRunts,
       "portOOWColls": portOOWColls,
       "portNoResources": portNoResources,
       "portRecBytes": portRecBytes,
       "portGiantFrames": portGiantFrames,
       "portRedundCrt": portRedundCrt,
       "portRedundType": portRedundType,
       "portRedundStatus": portRedundStatus,
       "portForceTrunkType": portForceTrunkType,
       "portBroadPkts": portBroadPkts,
       "portMultPkts": portMultPkts,
       "tokenRingP": tokenRingP,
       "stationP": stationP,
       "stationPortLinkStatus": stationPortLinkStatus,
       "stationPortLinkStateTime": stationPortLinkStateTime,
       "ringP": ringP,
       "fddiP": fddiP,
       "repeaterTables": repeaterTables,
       "productRev1": productRev1,
       "target": target,
       "targetRevision": targetRevision,
       "targetPortAssociation": targetPortAssociation,
       "fnb": fnb,
       "fnbConnectedLeft": fnbConnectedLeft,
       "fnbConnectedRight": fnbConnectedRight,
       "fnbBoardBypassState": fnbBoardBypassState,
       "audibleAlarm": audibleAlarm,
       "audibleAlarmEnable": audibleAlarmEnable,
       "audibleAlarmOff": audibleAlarmOff}
)
