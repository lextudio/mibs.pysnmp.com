# SNMP MIB module (HH3C-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-STORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:59 2024
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

(PhysicalIndex,
 entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalName")

(hh3cDiskPowerOffReason,) = mibBuilder.importSymbols(
    "HH3C-DISK-MIB",
    "hh3cDiskPowerOffReason")

(hh3cEntityExtCriticalLowerTemperatureThreshold,
 hh3cEntityExtOperStatus,
 hh3cEntityExtPhysicalIndex,
 hh3cEntityExtShutdownLowerTemperatureThreshold,
 hh3cEntityExtTemperature) = mibBuilder.importSymbols(
    "HH3C-ENTITY-EXT-MIB",
    "hh3cEntityExtCriticalLowerTemperatureThreshold",
    "hh3cEntityExtOperStatus",
    "hh3cEntityExtPhysicalIndex",
    "hh3cEntityExtShutdownLowerTemperatureThreshold",
    "hh3cEntityExtTemperature")

(hh3cRaidHideState,
 hh3cRaidName,
 hh3cRaidRunState,
 hh3cRaidUuid) = mibBuilder.importSymbols(
    "HH3C-RAID-MIB",
    "hh3cRaidHideState",
    "hh3cRaidName",
    "hh3cRaidRunState",
    "hh3cRaidUuid")

(Hh3cSoftwareInfoString,
 Hh3cStorageActionType,
 Hh3cStorageCapableState,
 Hh3cStorageEnableState,
 Hh3cStorageLedStateType,
 Hh3cWwpnListType,
 hh3cStorageRef) = mibBuilder.importSymbols(
    "HH3C-STORAGE-REF-MIB",
    "Hh3cSoftwareInfoString",
    "Hh3cStorageActionType",
    "Hh3cStorageCapableState",
    "Hh3cStorageEnableState",
    "Hh3cStorageLedStateType",
    "Hh3cWwpnListType",
    "hh3cStorageRef")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hh3cStorageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cStorageMibObjects_ObjectIdentity = ObjectIdentity
hh3cStorageMibObjects = _Hh3cStorageMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1)
)
_Hh3cStorageServerInfo_ObjectIdentity = ObjectIdentity
hh3cStorageServerInfo = _Hh3cStorageServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1)
)
_Hh3cStorageServerCapability_ObjectIdentity = ObjectIdentity
hh3cStorageServerCapability = _Hh3cStorageServerCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1)
)
_Hh3cRaidCapability_Type = Hh3cStorageCapableState
_Hh3cRaidCapability_Object = MibScalar
hh3cRaidCapability = _Hh3cRaidCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 1),
    _Hh3cRaidCapability_Type()
)
hh3cRaidCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRaidCapability.setStatus("current")
_Hh3cFcCapability_Type = Hh3cStorageCapableState
_Hh3cFcCapability_Object = MibScalar
hh3cFcCapability = _Hh3cFcCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 2),
    _Hh3cFcCapability_Type()
)
hh3cFcCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcCapability.setStatus("current")
_Hh3cNasCapability_Type = Hh3cStorageCapableState
_Hh3cNasCapability_Object = MibScalar
hh3cNasCapability = _Hh3cNasCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 3),
    _Hh3cNasCapability_Type()
)
hh3cNasCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNasCapability.setStatus("current")
_Hh3cAdaptiveRepCapability_Type = Hh3cStorageCapableState
_Hh3cAdaptiveRepCapability_Object = MibScalar
hh3cAdaptiveRepCapability = _Hh3cAdaptiveRepCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 4),
    _Hh3cAdaptiveRepCapability_Type()
)
hh3cAdaptiveRepCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAdaptiveRepCapability.setStatus("current")
_Hh3cRemoteRepCapability_Type = Hh3cStorageCapableState
_Hh3cRemoteRepCapability_Object = MibScalar
hh3cRemoteRepCapability = _Hh3cRemoteRepCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 5),
    _Hh3cRemoteRepCapability_Type()
)
hh3cRemoteRepCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRemoteRepCapability.setStatus("current")
_Hh3cSafeCacheCapability_Type = Hh3cStorageCapableState
_Hh3cSafeCacheCapability_Object = MibScalar
hh3cSafeCacheCapability = _Hh3cSafeCacheCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 6),
    _Hh3cSafeCacheCapability_Type()
)
hh3cSafeCacheCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSafeCacheCapability.setStatus("current")
_Hh3cSyncMirrorCapability_Type = Hh3cStorageCapableState
_Hh3cSyncMirrorCapability_Object = MibScalar
hh3cSyncMirrorCapability = _Hh3cSyncMirrorCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 7),
    _Hh3cSyncMirrorCapability_Type()
)
hh3cSyncMirrorCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSyncMirrorCapability.setStatus("current")
_Hh3cAsyncMirrorCapability_Type = Hh3cStorageCapableState
_Hh3cAsyncMirrorCapability_Object = MibScalar
hh3cAsyncMirrorCapability = _Hh3cAsyncMirrorCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 8),
    _Hh3cAsyncMirrorCapability_Type()
)
hh3cAsyncMirrorCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAsyncMirrorCapability.setStatus("current")
_Hh3cTimeMarkCapability_Type = Hh3cStorageCapableState
_Hh3cTimeMarkCapability_Object = MibScalar
hh3cTimeMarkCapability = _Hh3cTimeMarkCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 9),
    _Hh3cTimeMarkCapability_Type()
)
hh3cTimeMarkCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTimeMarkCapability.setStatus("current")
_Hh3cSseCapability_Type = Hh3cStorageCapableState
_Hh3cSseCapability_Object = MibScalar
hh3cSseCapability = _Hh3cSseCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 1, 10),
    _Hh3cSseCapability_Type()
)
hh3cSseCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSseCapability.setStatus("current")
_Hh3cStorageTargetConfig_ObjectIdentity = ObjectIdentity
hh3cStorageTargetConfig = _Hh3cStorageTargetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 2)
)


class _Hh3ciSCSITargetEnable_Type(Hh3cStorageEnableState):
    """Custom type hh3ciSCSITargetEnable based on Hh3cStorageEnableState"""


_Hh3ciSCSITargetEnable_Object = MibScalar
hh3ciSCSITargetEnable = _Hh3ciSCSITargetEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 2, 1),
    _Hh3ciSCSITargetEnable_Type()
)
hh3ciSCSITargetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3ciSCSITargetEnable.setStatus("current")
_Hh3cFcTargetEnable_Type = Hh3cStorageEnableState
_Hh3cFcTargetEnable_Object = MibScalar
hh3cFcTargetEnable = _Hh3cFcTargetEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 2, 2),
    _Hh3cFcTargetEnable_Type()
)
hh3cFcTargetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcTargetEnable.setStatus("current")
_Hh3cStorageServerPhysInfo_ObjectIdentity = ObjectIdentity
hh3cStorageServerPhysInfo = _Hh3cStorageServerPhysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3)
)
_Hh3cServerLocationLedState_Type = Hh3cStorageLedStateType
_Hh3cServerLocationLedState_Object = MibScalar
hh3cServerLocationLedState = _Hh3cServerLocationLedState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 1),
    _Hh3cServerLocationLedState_Type()
)
hh3cServerLocationLedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cServerLocationLedState.setStatus("current")


class _Hh3cServerResetButtonState_Type(Hh3cStorageEnableState):
    """Custom type hh3cServerResetButtonState based on Hh3cStorageEnableState"""


_Hh3cServerResetButtonState_Object = MibScalar
hh3cServerResetButtonState = _Hh3cServerResetButtonState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 2),
    _Hh3cServerResetButtonState_Type()
)
hh3cServerResetButtonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cServerResetButtonState.setStatus("current")


class _Hh3cServerPowerButtonState_Type(Hh3cStorageEnableState):
    """Custom type hh3cServerPowerButtonState based on Hh3cStorageEnableState"""


_Hh3cServerPowerButtonState_Object = MibScalar
hh3cServerPowerButtonState = _Hh3cServerPowerButtonState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 3),
    _Hh3cServerPowerButtonState_Type()
)
hh3cServerPowerButtonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cServerPowerButtonState.setStatus("current")


class _Hh3cServerPowerState_Type(Integer32):
    """Custom type hh3cServerPowerState based on Integer32"""
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
        *(("onbattery", 3),
          ("online", 1),
          ("onlinebypass", 2),
          ("unknown", 4))
    )


_Hh3cServerPowerState_Type.__name__ = "Integer32"
_Hh3cServerPowerState_Object = MibScalar
hh3cServerPowerState = _Hh3cServerPowerState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 1, 3, 4),
    _Hh3cServerPowerState_Type()
)
hh3cServerPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cServerPowerState.setStatus("current")
_Hh3cStoragePhysicalInfo_ObjectIdentity = ObjectIdentity
hh3cStoragePhysicalInfo = _Hh3cStoragePhysicalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2)
)
_Hh3cDeuTable_Object = MibTable
hh3cDeuTable = _Hh3cDeuTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDeuTable.setStatus("current")
_Hh3cDeuEntry_Object = MibTableRow
hh3cDeuEntry = _Hh3cDeuEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1)
)
hh3cDeuEntry.setIndexNames(
    (0, "HH3C-STORAGE-MIB", "hh3cDeuIndex"),
)
if mibBuilder.loadTexts:
    hh3cDeuEntry.setStatus("current")
_Hh3cDeuIndex_Type = Integer32
_Hh3cDeuIndex_Object = MibTableColumn
hh3cDeuIndex = _Hh3cDeuIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1, 1),
    _Hh3cDeuIndex_Type()
)
hh3cDeuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDeuIndex.setStatus("current")


class _Hh3cDeuIDLed_Type(Hh3cStorageLedStateType):
    """Custom type hh3cDeuIDLed based on Hh3cStorageLedStateType"""


_Hh3cDeuIDLed_Object = MibTableColumn
hh3cDeuIDLed = _Hh3cDeuIDLed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1, 2),
    _Hh3cDeuIDLed_Type()
)
hh3cDeuIDLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDeuIDLed.setStatus("current")
_Hh3cDeuDiskScan_Type = Hh3cStorageActionType
_Hh3cDeuDiskScan_Object = MibTableColumn
hh3cDeuDiskScan = _Hh3cDeuDiskScan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 1, 1, 3),
    _Hh3cDeuDiskScan_Type()
)
hh3cDeuDiskScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDeuDiskScan.setStatus("current")
_Hh3cStorageInterfaceTable_Object = MibTable
hh3cStorageInterfaceTable = _Hh3cStorageInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cStorageInterfaceTable.setStatus("current")
_Hh3cStorageInterfaceEntry_Object = MibTableRow
hh3cStorageInterfaceEntry = _Hh3cStorageInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1)
)
hh3cStorageInterfaceEntry.setIndexNames(
    (0, "HH3C-STORAGE-MIB", "hh3cStorageInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hh3cStorageInterfaceEntry.setStatus("current")
_Hh3cStorageInterfaceIndex_Type = Integer32
_Hh3cStorageInterfaceIndex_Object = MibTableColumn
hh3cStorageInterfaceIndex = _Hh3cStorageInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 1),
    _Hh3cStorageInterfaceIndex_Type()
)
hh3cStorageInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cStorageInterfaceIndex.setStatus("current")
_Hh3cStorageInterfaceGateway_Type = InetAddress
_Hh3cStorageInterfaceGateway_Object = MibTableColumn
hh3cStorageInterfaceGateway = _Hh3cStorageInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 2),
    _Hh3cStorageInterfaceGateway_Type()
)
hh3cStorageInterfaceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStorageInterfaceGateway.setStatus("current")
_Hh3cStorageInterfaceGatewayType_Type = InetAddressType
_Hh3cStorageInterfaceGatewayType_Object = MibTableColumn
hh3cStorageInterfaceGatewayType = _Hh3cStorageInterfaceGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 3),
    _Hh3cStorageInterfaceGatewayType_Type()
)
hh3cStorageInterfaceGatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStorageInterfaceGatewayType.setStatus("current")


class _Hh3cStorageInterfaceMTU_Type(Integer32):
    """Custom type hh3cStorageInterfaceMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1500,
              9000)
        )
    )
    namedValues = NamedValues(
        *(("mtu1", 1500),
          ("mtu2", 9000))
    )


_Hh3cStorageInterfaceMTU_Type.__name__ = "Integer32"
_Hh3cStorageInterfaceMTU_Object = MibTableColumn
hh3cStorageInterfaceMTU = _Hh3cStorageInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 2, 1, 4),
    _Hh3cStorageInterfaceMTU_Type()
)
hh3cStorageInterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStorageInterfaceMTU.setStatus("current")
_Hh3cBondingTable_Object = MibTable
hh3cBondingTable = _Hh3cBondingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cBondingTable.setStatus("current")
_Hh3cBondingEntry_Object = MibTableRow
hh3cBondingEntry = _Hh3cBondingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3, 1)
)
hh3cBondingEntry.setIndexNames(
    (0, "HH3C-STORAGE-MIB", "hh3cBondingIndex"),
)
if mibBuilder.loadTexts:
    hh3cBondingEntry.setStatus("current")
_Hh3cBondingIndex_Type = Integer32
_Hh3cBondingIndex_Object = MibTableColumn
hh3cBondingIndex = _Hh3cBondingIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3, 1, 1),
    _Hh3cBondingIndex_Type()
)
hh3cBondingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBondingIndex.setStatus("current")
_Hh3cBondingPortList_Type = OctetString
_Hh3cBondingPortList_Object = MibTableColumn
hh3cBondingPortList = _Hh3cBondingPortList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 3, 1, 2),
    _Hh3cBondingPortList_Type()
)
hh3cBondingPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBondingPortList.setStatus("current")
_Hh3cScsiAdapterTable_Object = MibTable
hh3cScsiAdapterTable = _Hh3cScsiAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cScsiAdapterTable.setStatus("current")
_Hh3cScsiAdapterEntry_Object = MibTableRow
hh3cScsiAdapterEntry = _Hh3cScsiAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1)
)
hh3cScsiAdapterEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HH3C-STORAGE-MIB", "hh3cAdapterNumber"),
)
if mibBuilder.loadTexts:
    hh3cScsiAdapterEntry.setStatus("current")
_Hh3cAdapterNumber_Type = Integer32
_Hh3cAdapterNumber_Object = MibTableColumn
hh3cAdapterNumber = _Hh3cAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 1),
    _Hh3cAdapterNumber_Type()
)
hh3cAdapterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAdapterNumber.setStatus("current")
_Hh3cAdapterDesc_Type = OctetString
_Hh3cAdapterDesc_Object = MibTableColumn
hh3cAdapterDesc = _Hh3cAdapterDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 2),
    _Hh3cAdapterDesc_Type()
)
hh3cAdapterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAdapterDesc.setStatus("current")


class _Hh3cAdapterType_Type(Integer32):
    """Custom type hh3cAdapterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fc", 2),
          ("scsi", 1))
    )


_Hh3cAdapterType_Type.__name__ = "Integer32"
_Hh3cAdapterType_Object = MibTableColumn
hh3cAdapterType = _Hh3cAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 3),
    _Hh3cAdapterType_Type()
)
hh3cAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAdapterType.setStatus("current")


class _Hh3cFcAdapterMode_Type(Integer32):
    """Custom type hh3cFcAdapterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 3),
          ("initiator", 1),
          ("target", 2))
    )


_Hh3cFcAdapterMode_Type.__name__ = "Integer32"
_Hh3cFcAdapterMode_Object = MibTableColumn
hh3cFcAdapterMode = _Hh3cFcAdapterMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 4),
    _Hh3cFcAdapterMode_Type()
)
hh3cFcAdapterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcAdapterMode.setStatus("current")
_Hh3cFcAdapterInitiatorWwpnName_Type = Hh3cWwpnListType
_Hh3cFcAdapterInitiatorWwpnName_Object = MibTableColumn
hh3cFcAdapterInitiatorWwpnName = _Hh3cFcAdapterInitiatorWwpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 5),
    _Hh3cFcAdapterInitiatorWwpnName_Type()
)
hh3cFcAdapterInitiatorWwpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcAdapterInitiatorWwpnName.setStatus("current")
_Hh3cFcAdapterTargetWwpnName_Type = Hh3cWwpnListType
_Hh3cFcAdapterTargetWwpnName_Object = MibTableColumn
hh3cFcAdapterTargetWwpnName = _Hh3cFcAdapterTargetWwpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 6),
    _Hh3cFcAdapterTargetWwpnName_Type()
)
hh3cFcAdapterTargetWwpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcAdapterTargetWwpnName.setStatus("current")


class _Hh3cFcAdapterPortState_Type(Integer32):
    """Custom type hh3cFcAdapterPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 2),
          ("linkup", 1))
    )


_Hh3cFcAdapterPortState_Type.__name__ = "Integer32"
_Hh3cFcAdapterPortState_Object = MibTableColumn
hh3cFcAdapterPortState = _Hh3cFcAdapterPortState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 7),
    _Hh3cFcAdapterPortState_Type()
)
hh3cFcAdapterPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcAdapterPortState.setStatus("current")


class _Hh3cFcAdapterModeSwitch_Type(Hh3cStorageEnableState):
    """Custom type hh3cFcAdapterModeSwitch based on Hh3cStorageEnableState"""


_Hh3cFcAdapterModeSwitch_Object = MibTableColumn
hh3cFcAdapterModeSwitch = _Hh3cFcAdapterModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 4, 1, 8),
    _Hh3cFcAdapterModeSwitch_Type()
)
hh3cFcAdapterModeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcAdapterModeSwitch.setStatus("current")
_Hh3cExtVoltageTable_Object = MibTable
hh3cExtVoltageTable = _Hh3cExtVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cExtVoltageTable.setStatus("current")
_Hh3cExtVoltageEntry_Object = MibTableRow
hh3cExtVoltageEntry = _Hh3cExtVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1)
)
hh3cExtVoltageEntry.setIndexNames(
    (0, "HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cExtVoltageEntry.setStatus("current")
_Hh3cExtVoltagePhysicalIndex_Type = PhysicalIndex
_Hh3cExtVoltagePhysicalIndex_Object = MibTableColumn
hh3cExtVoltagePhysicalIndex = _Hh3cExtVoltagePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 1),
    _Hh3cExtVoltagePhysicalIndex_Type()
)
hh3cExtVoltagePhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cExtVoltagePhysicalIndex.setStatus("current")
_Hh3cExtVoltagePhysicalName_Type = SnmpAdminString
_Hh3cExtVoltagePhysicalName_Object = MibTableColumn
hh3cExtVoltagePhysicalName = _Hh3cExtVoltagePhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 2),
    _Hh3cExtVoltagePhysicalName_Type()
)
hh3cExtVoltagePhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cExtVoltagePhysicalName.setStatus("current")
_Hh3cExtVoltage_Type = Integer32
_Hh3cExtVoltage_Object = MibTableColumn
hh3cExtVoltage = _Hh3cExtVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 3),
    _Hh3cExtVoltage_Type()
)
hh3cExtVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cExtVoltage.setStatus("current")
_Hh3cExtVoltageLowThreshold_Type = Integer32
_Hh3cExtVoltageLowThreshold_Object = MibTableColumn
hh3cExtVoltageLowThreshold = _Hh3cExtVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 4),
    _Hh3cExtVoltageLowThreshold_Type()
)
hh3cExtVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExtVoltageLowThreshold.setStatus("current")
_Hh3cExtVoltageHighThreshold_Type = Integer32
_Hh3cExtVoltageHighThreshold_Object = MibTableColumn
hh3cExtVoltageHighThreshold = _Hh3cExtVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 5),
    _Hh3cExtVoltageHighThreshold_Type()
)
hh3cExtVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExtVoltageHighThreshold.setStatus("current")
_Hh3cExtCriticalVoltageLowThreshold_Type = Integer32
_Hh3cExtCriticalVoltageLowThreshold_Object = MibTableColumn
hh3cExtCriticalVoltageLowThreshold = _Hh3cExtCriticalVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 6),
    _Hh3cExtCriticalVoltageLowThreshold_Type()
)
hh3cExtCriticalVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExtCriticalVoltageLowThreshold.setStatus("current")
_Hh3cExtCriticalVoltageHighThreshold_Type = Integer32
_Hh3cExtCriticalVoltageHighThreshold_Object = MibTableColumn
hh3cExtCriticalVoltageHighThreshold = _Hh3cExtCriticalVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 7),
    _Hh3cExtCriticalVoltageHighThreshold_Type()
)
hh3cExtCriticalVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExtCriticalVoltageHighThreshold.setStatus("current")
_Hh3cExtShutdownVoltageLowThreshold_Type = Integer32
_Hh3cExtShutdownVoltageLowThreshold_Object = MibTableColumn
hh3cExtShutdownVoltageLowThreshold = _Hh3cExtShutdownVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 8),
    _Hh3cExtShutdownVoltageLowThreshold_Type()
)
hh3cExtShutdownVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExtShutdownVoltageLowThreshold.setStatus("current")
_Hh3cExtShutdownVoltageHighThreshold_Type = Integer32
_Hh3cExtShutdownVoltageHighThreshold_Object = MibTableColumn
hh3cExtShutdownVoltageHighThreshold = _Hh3cExtShutdownVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 2, 5, 1, 9),
    _Hh3cExtShutdownVoltageHighThreshold_Type()
)
hh3cExtShutdownVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExtShutdownVoltageHighThreshold.setStatus("current")
_Hh3cStorageTraps_ObjectIdentity = ObjectIdentity
hh3cStorageTraps = _Hh3cStorageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3)
)
_Hh3cStorageTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cStorageTrapsPrefix = _Hh3cStorageTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0)
)
_Hh3cStorageTrapsObjects_ObjectIdentity = ObjectIdentity
hh3cStorageTrapsObjects = _Hh3cStorageTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 1)
)
_Hh3cSoftwareInfoString_Type = Hh3cSoftwareInfoString
_Hh3cSoftwareInfoString_Object = MibScalar
hh3cSoftwareInfoString = _Hh3cSoftwareInfoString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 1, 1),
    _Hh3cSoftwareInfoString_Type()
)
hh3cSoftwareInfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSoftwareInfoString.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cStorCriticalLowerTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 1)
)
hh3cStorCriticalLowerTemperatureThresholdNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtCriticalLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    hh3cStorCriticalLowerTemperatureThresholdNotification.setStatus(
        "current"
    )

hh3cStorTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 2)
)
hh3cStorTemperatureTooLow.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtTemperature"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtShutdownLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    hh3cStorTemperatureTooLow.setStatus(
        "current"
    )

hh3cExtVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 3)
)
hh3cExtVoltageLowThresholdNotification.setObjects(
      *(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltage"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltageLowThreshold"))
)
if mibBuilder.loadTexts:
    hh3cExtVoltageLowThresholdNotification.setStatus(
        "current"
    )

hh3cExtVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 4)
)
hh3cExtVoltageHighThresholdNotification.setObjects(
      *(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltage"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    hh3cExtVoltageHighThresholdNotification.setStatus(
        "current"
    )

hh3cExtCriticalVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 5)
)
hh3cExtCriticalVoltageLowThresholdNotification.setObjects(
      *(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltage"),
        ("HH3C-STORAGE-MIB", "hh3cExtCriticalVoltageLowThreshold"))
)
if mibBuilder.loadTexts:
    hh3cExtCriticalVoltageLowThresholdNotification.setStatus(
        "current"
    )

hh3cExtCriticalVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 6)
)
hh3cExtCriticalVoltageHighThresholdNotification.setObjects(
      *(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltage"),
        ("HH3C-STORAGE-MIB", "hh3cExtCriticalVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    hh3cExtCriticalVoltageHighThresholdNotification.setStatus(
        "current"
    )

hh3cExtVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 7)
)
hh3cExtVoltageTooLow.setObjects(
      *(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltage"),
        ("HH3C-STORAGE-MIB", "hh3cExtShutdownVoltageLowThreshold"))
)
if mibBuilder.loadTexts:
    hh3cExtVoltageTooLow.setStatus(
        "current"
    )

hh3cExtVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 8)
)
hh3cExtVoltageTooHigh.setObjects(
      *(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltage"),
        ("HH3C-STORAGE-MIB", "hh3cExtShutdownVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    hh3cExtVoltageTooHigh.setStatus(
        "current"
    )

hh3cExtBatteryStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 9)
)
hh3cExtBatteryStateNotification.setObjects(
      *(("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HH3C-ENTITY-EXT-MIB", "hh3cEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    hh3cExtBatteryStateNotification.setStatus(
        "current"
    )

hh3cDiskIOErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 10)
)
hh3cDiskIOErrorNotification.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    hh3cDiskIOErrorNotification.setStatus(
        "current"
    )

hh3cRaidCreateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 11)
)
hh3cRaidCreateNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidCreateNotification.setStatus(
        "current"
    )

hh3cRaidDeleteNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 12)
)
hh3cRaidDeleteNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidDeleteNotification.setStatus(
        "current"
    )

hh3cRaidHideStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 13)
)
hh3cRaidHideStateNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"),
        ("HH3C-RAID-MIB", "hh3cRaidHideState"))
)
if mibBuilder.loadTexts:
    hh3cRaidHideStateNotification.setStatus(
        "current"
    )

hh3cRaidRunStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 14)
)
hh3cRaidRunStateNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"),
        ("HH3C-RAID-MIB", "hh3cRaidRunState"))
)
if mibBuilder.loadTexts:
    hh3cRaidRunStateNotification.setStatus(
        "current"
    )

hh3cRaidImportNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 15)
)
hh3cRaidImportNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidImportNotification.setStatus(
        "current"
    )

hh3cRaidRebuildStartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 16)
)
hh3cRaidRebuildStartNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidRebuildStartNotification.setStatus(
        "current"
    )

hh3cRaidRebuildFinishNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 17)
)
hh3cRaidRebuildFinishNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidRebuildFinishNotification.setStatus(
        "current"
    )

hh3cRaidRebuildPauseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 18)
)
hh3cRaidRebuildPauseNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidRebuildPauseNotification.setStatus(
        "current"
    )

hh3cRaidRebuildInterruptNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 19)
)
hh3cRaidRebuildInterruptNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidRebuildInterruptNotification.setStatus(
        "current"
    )

hh3cSoftwareModuleFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 20)
)
hh3cSoftwareModuleFailNotification.setObjects(
    ("HH3C-STORAGE-MIB", "hh3cSoftwareInfoString")
)
if mibBuilder.loadTexts:
    hh3cSoftwareModuleFailNotification.setStatus(
        "current"
    )

hh3cRaidBatteryExpiredNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 21)
)
if mibBuilder.loadTexts:
    hh3cRaidBatteryExpiredNotification.setStatus(
        "current"
    )

hh3cRaidBatteryWillExpireNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 22)
)
if mibBuilder.loadTexts:
    hh3cRaidBatteryWillExpireNotification.setStatus(
        "current"
    )

hh3cLvOnlineFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 23)
)
hh3cLvOnlineFailNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cLvOnlineFailNotification.setStatus(
        "current"
    )

hh3cLvOfflineFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 24)
)
hh3cLvOfflineFailNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cLvOfflineFailNotification.setStatus(
        "current"
    )

hh3cRaidRunNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 25)
)
hh3cRaidRunNotification.setObjects(
      *(("HH3C-RAID-MIB", "hh3cRaidUuid"),
        ("HH3C-RAID-MIB", "hh3cRaidName"))
)
if mibBuilder.loadTexts:
    hh3cRaidRunNotification.setStatus(
        "current"
    )

hh3cExtVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 26)
)
hh3cExtVoltageNormal.setObjects(
      *(("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalIndex"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltagePhysicalName"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltage"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltageLowThreshold"),
        ("HH3C-STORAGE-MIB", "hh3cExtVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    hh3cExtVoltageNormal.setStatus(
        "current"
    )

hh3cDiskPowerOnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 27)
)
hh3cDiskPowerOnNotification.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    hh3cDiskPowerOnNotification.setStatus(
        "current"
    )

hh3cDiskPowerOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1, 1, 3, 0, 28)
)
hh3cDiskPowerOffNotification.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("HH3C-DISK-MIB", "hh3cDiskPowerOffReason"))
)
if mibBuilder.loadTexts:
    hh3cDiskPowerOffNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-STORAGE-MIB",
    **{"hh3cStorageMIB": hh3cStorageMIB,
       "hh3cStorageMibObjects": hh3cStorageMibObjects,
       "hh3cStorageServerInfo": hh3cStorageServerInfo,
       "hh3cStorageServerCapability": hh3cStorageServerCapability,
       "hh3cRaidCapability": hh3cRaidCapability,
       "hh3cFcCapability": hh3cFcCapability,
       "hh3cNasCapability": hh3cNasCapability,
       "hh3cAdaptiveRepCapability": hh3cAdaptiveRepCapability,
       "hh3cRemoteRepCapability": hh3cRemoteRepCapability,
       "hh3cSafeCacheCapability": hh3cSafeCacheCapability,
       "hh3cSyncMirrorCapability": hh3cSyncMirrorCapability,
       "hh3cAsyncMirrorCapability": hh3cAsyncMirrorCapability,
       "hh3cTimeMarkCapability": hh3cTimeMarkCapability,
       "hh3cSseCapability": hh3cSseCapability,
       "hh3cStorageTargetConfig": hh3cStorageTargetConfig,
       "hh3ciSCSITargetEnable": hh3ciSCSITargetEnable,
       "hh3cFcTargetEnable": hh3cFcTargetEnable,
       "hh3cStorageServerPhysInfo": hh3cStorageServerPhysInfo,
       "hh3cServerLocationLedState": hh3cServerLocationLedState,
       "hh3cServerResetButtonState": hh3cServerResetButtonState,
       "hh3cServerPowerButtonState": hh3cServerPowerButtonState,
       "hh3cServerPowerState": hh3cServerPowerState,
       "hh3cStoragePhysicalInfo": hh3cStoragePhysicalInfo,
       "hh3cDeuTable": hh3cDeuTable,
       "hh3cDeuEntry": hh3cDeuEntry,
       "hh3cDeuIndex": hh3cDeuIndex,
       "hh3cDeuIDLed": hh3cDeuIDLed,
       "hh3cDeuDiskScan": hh3cDeuDiskScan,
       "hh3cStorageInterfaceTable": hh3cStorageInterfaceTable,
       "hh3cStorageInterfaceEntry": hh3cStorageInterfaceEntry,
       "hh3cStorageInterfaceIndex": hh3cStorageInterfaceIndex,
       "hh3cStorageInterfaceGateway": hh3cStorageInterfaceGateway,
       "hh3cStorageInterfaceGatewayType": hh3cStorageInterfaceGatewayType,
       "hh3cStorageInterfaceMTU": hh3cStorageInterfaceMTU,
       "hh3cBondingTable": hh3cBondingTable,
       "hh3cBondingEntry": hh3cBondingEntry,
       "hh3cBondingIndex": hh3cBondingIndex,
       "hh3cBondingPortList": hh3cBondingPortList,
       "hh3cScsiAdapterTable": hh3cScsiAdapterTable,
       "hh3cScsiAdapterEntry": hh3cScsiAdapterEntry,
       "hh3cAdapterNumber": hh3cAdapterNumber,
       "hh3cAdapterDesc": hh3cAdapterDesc,
       "hh3cAdapterType": hh3cAdapterType,
       "hh3cFcAdapterMode": hh3cFcAdapterMode,
       "hh3cFcAdapterInitiatorWwpnName": hh3cFcAdapterInitiatorWwpnName,
       "hh3cFcAdapterTargetWwpnName": hh3cFcAdapterTargetWwpnName,
       "hh3cFcAdapterPortState": hh3cFcAdapterPortState,
       "hh3cFcAdapterModeSwitch": hh3cFcAdapterModeSwitch,
       "hh3cExtVoltageTable": hh3cExtVoltageTable,
       "hh3cExtVoltageEntry": hh3cExtVoltageEntry,
       "hh3cExtVoltagePhysicalIndex": hh3cExtVoltagePhysicalIndex,
       "hh3cExtVoltagePhysicalName": hh3cExtVoltagePhysicalName,
       "hh3cExtVoltage": hh3cExtVoltage,
       "hh3cExtVoltageLowThreshold": hh3cExtVoltageLowThreshold,
       "hh3cExtVoltageHighThreshold": hh3cExtVoltageHighThreshold,
       "hh3cExtCriticalVoltageLowThreshold": hh3cExtCriticalVoltageLowThreshold,
       "hh3cExtCriticalVoltageHighThreshold": hh3cExtCriticalVoltageHighThreshold,
       "hh3cExtShutdownVoltageLowThreshold": hh3cExtShutdownVoltageLowThreshold,
       "hh3cExtShutdownVoltageHighThreshold": hh3cExtShutdownVoltageHighThreshold,
       "hh3cStorageTraps": hh3cStorageTraps,
       "hh3cStorageTrapsPrefix": hh3cStorageTrapsPrefix,
       "hh3cStorCriticalLowerTemperatureThresholdNotification": hh3cStorCriticalLowerTemperatureThresholdNotification,
       "hh3cStorTemperatureTooLow": hh3cStorTemperatureTooLow,
       "hh3cExtVoltageLowThresholdNotification": hh3cExtVoltageLowThresholdNotification,
       "hh3cExtVoltageHighThresholdNotification": hh3cExtVoltageHighThresholdNotification,
       "hh3cExtCriticalVoltageLowThresholdNotification": hh3cExtCriticalVoltageLowThresholdNotification,
       "hh3cExtCriticalVoltageHighThresholdNotification": hh3cExtCriticalVoltageHighThresholdNotification,
       "hh3cExtVoltageTooLow": hh3cExtVoltageTooLow,
       "hh3cExtVoltageTooHigh": hh3cExtVoltageTooHigh,
       "hh3cExtBatteryStateNotification": hh3cExtBatteryStateNotification,
       "hh3cDiskIOErrorNotification": hh3cDiskIOErrorNotification,
       "hh3cRaidCreateNotification": hh3cRaidCreateNotification,
       "hh3cRaidDeleteNotification": hh3cRaidDeleteNotification,
       "hh3cRaidHideStateNotification": hh3cRaidHideStateNotification,
       "hh3cRaidRunStateNotification": hh3cRaidRunStateNotification,
       "hh3cRaidImportNotification": hh3cRaidImportNotification,
       "hh3cRaidRebuildStartNotification": hh3cRaidRebuildStartNotification,
       "hh3cRaidRebuildFinishNotification": hh3cRaidRebuildFinishNotification,
       "hh3cRaidRebuildPauseNotification": hh3cRaidRebuildPauseNotification,
       "hh3cRaidRebuildInterruptNotification": hh3cRaidRebuildInterruptNotification,
       "hh3cSoftwareModuleFailNotification": hh3cSoftwareModuleFailNotification,
       "hh3cRaidBatteryExpiredNotification": hh3cRaidBatteryExpiredNotification,
       "hh3cRaidBatteryWillExpireNotification": hh3cRaidBatteryWillExpireNotification,
       "hh3cLvOnlineFailNotification": hh3cLvOnlineFailNotification,
       "hh3cLvOfflineFailNotification": hh3cLvOfflineFailNotification,
       "hh3cRaidRunNotification": hh3cRaidRunNotification,
       "hh3cExtVoltageNormal": hh3cExtVoltageNormal,
       "hh3cDiskPowerOnNotification": hh3cDiskPowerOnNotification,
       "hh3cDiskPowerOffNotification": hh3cDiskPowerOffNotification,
       "hh3cStorageTrapsObjects": hh3cStorageTrapsObjects,
       "hh3cSoftwareInfoString": hh3cSoftwareInfoString}
)
