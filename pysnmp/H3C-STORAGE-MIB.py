# SNMP MIB module (H3C-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-STORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:26 2024
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

(h3cDiskPowerOffReason,) = mibBuilder.importSymbols(
    "H3C-DISK-MIB",
    "h3cDiskPowerOffReason")

(h3cEntityExtCriticalLowerTemperatureThreshold,
 h3cEntityExtOperStatus,
 h3cEntityExtPhysicalIndex,
 h3cEntityExtShutdownLowerTemperatureThreshold,
 h3cEntityExtTemperature) = mibBuilder.importSymbols(
    "H3C-ENTITY-EXT-MIB",
    "h3cEntityExtCriticalLowerTemperatureThreshold",
    "h3cEntityExtOperStatus",
    "h3cEntityExtPhysicalIndex",
    "h3cEntityExtShutdownLowerTemperatureThreshold",
    "h3cEntityExtTemperature")

(h3cRaidHideState,
 h3cRaidName,
 h3cRaidRunState,
 h3cRaidUuid) = mibBuilder.importSymbols(
    "H3C-RAID-MIB",
    "h3cRaidHideState",
    "h3cRaidName",
    "h3cRaidRunState",
    "h3cRaidUuid")

(H3cSoftwareInfoString,
 H3cStorageActionType,
 H3cStorageCapableState,
 H3cStorageEnableState,
 H3cStorageLedStateType,
 H3cWwpnListType,
 h3cStorageRef) = mibBuilder.importSymbols(
    "H3C-STORAGE-REF-MIB",
    "H3cSoftwareInfoString",
    "H3cStorageActionType",
    "H3cStorageCapableState",
    "H3cStorageEnableState",
    "H3cStorageLedStateType",
    "H3cWwpnListType",
    "h3cStorageRef")

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

h3cStorageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cStorageMibObjects_ObjectIdentity = ObjectIdentity
h3cStorageMibObjects = _H3cStorageMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1)
)
_H3cStorageServerInfo_ObjectIdentity = ObjectIdentity
h3cStorageServerInfo = _H3cStorageServerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1)
)
_H3cStorageServerCapability_ObjectIdentity = ObjectIdentity
h3cStorageServerCapability = _H3cStorageServerCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1)
)
_H3cRaidCapability_Type = H3cStorageCapableState
_H3cRaidCapability_Object = MibScalar
h3cRaidCapability = _H3cRaidCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 1),
    _H3cRaidCapability_Type()
)
h3cRaidCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRaidCapability.setStatus("current")
_H3cFcCapability_Type = H3cStorageCapableState
_H3cFcCapability_Object = MibScalar
h3cFcCapability = _H3cFcCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 2),
    _H3cFcCapability_Type()
)
h3cFcCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcCapability.setStatus("current")
_H3cNasCapability_Type = H3cStorageCapableState
_H3cNasCapability_Object = MibScalar
h3cNasCapability = _H3cNasCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 3),
    _H3cNasCapability_Type()
)
h3cNasCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNasCapability.setStatus("current")
_H3cAdaptiveRepCapability_Type = H3cStorageCapableState
_H3cAdaptiveRepCapability_Object = MibScalar
h3cAdaptiveRepCapability = _H3cAdaptiveRepCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 4),
    _H3cAdaptiveRepCapability_Type()
)
h3cAdaptiveRepCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAdaptiveRepCapability.setStatus("current")
_H3cRemoteRepCapability_Type = H3cStorageCapableState
_H3cRemoteRepCapability_Object = MibScalar
h3cRemoteRepCapability = _H3cRemoteRepCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 5),
    _H3cRemoteRepCapability_Type()
)
h3cRemoteRepCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRemoteRepCapability.setStatus("current")
_H3cSafeCacheCapability_Type = H3cStorageCapableState
_H3cSafeCacheCapability_Object = MibScalar
h3cSafeCacheCapability = _H3cSafeCacheCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 6),
    _H3cSafeCacheCapability_Type()
)
h3cSafeCacheCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSafeCacheCapability.setStatus("current")
_H3cSyncMirrorCapability_Type = H3cStorageCapableState
_H3cSyncMirrorCapability_Object = MibScalar
h3cSyncMirrorCapability = _H3cSyncMirrorCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 7),
    _H3cSyncMirrorCapability_Type()
)
h3cSyncMirrorCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSyncMirrorCapability.setStatus("current")
_H3cAsyncMirrorCapability_Type = H3cStorageCapableState
_H3cAsyncMirrorCapability_Object = MibScalar
h3cAsyncMirrorCapability = _H3cAsyncMirrorCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 8),
    _H3cAsyncMirrorCapability_Type()
)
h3cAsyncMirrorCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAsyncMirrorCapability.setStatus("current")
_H3cTimeMarkCapability_Type = H3cStorageCapableState
_H3cTimeMarkCapability_Object = MibScalar
h3cTimeMarkCapability = _H3cTimeMarkCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 9),
    _H3cTimeMarkCapability_Type()
)
h3cTimeMarkCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTimeMarkCapability.setStatus("current")
_H3cSseCapability_Type = H3cStorageCapableState
_H3cSseCapability_Object = MibScalar
h3cSseCapability = _H3cSseCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 1, 10),
    _H3cSseCapability_Type()
)
h3cSseCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSseCapability.setStatus("current")
_H3cStorageTargetConfig_ObjectIdentity = ObjectIdentity
h3cStorageTargetConfig = _H3cStorageTargetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 2)
)


class _H3ciSCSITargetEnable_Type(H3cStorageEnableState):
    """Custom type h3ciSCSITargetEnable based on H3cStorageEnableState"""


_H3ciSCSITargetEnable_Object = MibScalar
h3ciSCSITargetEnable = _H3ciSCSITargetEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 2, 1),
    _H3ciSCSITargetEnable_Type()
)
h3ciSCSITargetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3ciSCSITargetEnable.setStatus("current")
_H3cFcTargetEnable_Type = H3cStorageEnableState
_H3cFcTargetEnable_Object = MibScalar
h3cFcTargetEnable = _H3cFcTargetEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 2, 2),
    _H3cFcTargetEnable_Type()
)
h3cFcTargetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcTargetEnable.setStatus("current")
_H3cStorageServerPhysInfo_ObjectIdentity = ObjectIdentity
h3cStorageServerPhysInfo = _H3cStorageServerPhysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3)
)
_H3cServerLocationLedState_Type = H3cStorageLedStateType
_H3cServerLocationLedState_Object = MibScalar
h3cServerLocationLedState = _H3cServerLocationLedState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 1),
    _H3cServerLocationLedState_Type()
)
h3cServerLocationLedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cServerLocationLedState.setStatus("current")


class _H3cServerResetButtonState_Type(H3cStorageEnableState):
    """Custom type h3cServerResetButtonState based on H3cStorageEnableState"""


_H3cServerResetButtonState_Object = MibScalar
h3cServerResetButtonState = _H3cServerResetButtonState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 2),
    _H3cServerResetButtonState_Type()
)
h3cServerResetButtonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cServerResetButtonState.setStatus("current")


class _H3cServerPowerButtonState_Type(H3cStorageEnableState):
    """Custom type h3cServerPowerButtonState based on H3cStorageEnableState"""


_H3cServerPowerButtonState_Object = MibScalar
h3cServerPowerButtonState = _H3cServerPowerButtonState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 3),
    _H3cServerPowerButtonState_Type()
)
h3cServerPowerButtonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cServerPowerButtonState.setStatus("current")


class _H3cServerPowerState_Type(Integer32):
    """Custom type h3cServerPowerState based on Integer32"""
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


_H3cServerPowerState_Type.__name__ = "Integer32"
_H3cServerPowerState_Object = MibScalar
h3cServerPowerState = _H3cServerPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 1, 3, 4),
    _H3cServerPowerState_Type()
)
h3cServerPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cServerPowerState.setStatus("current")
_H3cStoragePhysicalInfo_ObjectIdentity = ObjectIdentity
h3cStoragePhysicalInfo = _H3cStoragePhysicalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2)
)
_H3cDeuTable_Object = MibTable
h3cDeuTable = _H3cDeuTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDeuTable.setStatus("current")
_H3cDeuEntry_Object = MibTableRow
h3cDeuEntry = _H3cDeuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1)
)
h3cDeuEntry.setIndexNames(
    (0, "H3C-STORAGE-MIB", "h3cDeuIndex"),
)
if mibBuilder.loadTexts:
    h3cDeuEntry.setStatus("current")
_H3cDeuIndex_Type = Integer32
_H3cDeuIndex_Object = MibTableColumn
h3cDeuIndex = _H3cDeuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1, 1),
    _H3cDeuIndex_Type()
)
h3cDeuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDeuIndex.setStatus("current")


class _H3cDeuIDLed_Type(H3cStorageLedStateType):
    """Custom type h3cDeuIDLed based on H3cStorageLedStateType"""


_H3cDeuIDLed_Object = MibTableColumn
h3cDeuIDLed = _H3cDeuIDLed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1, 2),
    _H3cDeuIDLed_Type()
)
h3cDeuIDLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDeuIDLed.setStatus("current")
_H3cDeuDiskScan_Type = H3cStorageActionType
_H3cDeuDiskScan_Object = MibTableColumn
h3cDeuDiskScan = _H3cDeuDiskScan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 1, 1, 3),
    _H3cDeuDiskScan_Type()
)
h3cDeuDiskScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDeuDiskScan.setStatus("current")
_H3cStorageInterfaceTable_Object = MibTable
h3cStorageInterfaceTable = _H3cStorageInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cStorageInterfaceTable.setStatus("current")
_H3cStorageInterfaceEntry_Object = MibTableRow
h3cStorageInterfaceEntry = _H3cStorageInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1)
)
h3cStorageInterfaceEntry.setIndexNames(
    (0, "H3C-STORAGE-MIB", "h3cStorageInterfaceIndex"),
)
if mibBuilder.loadTexts:
    h3cStorageInterfaceEntry.setStatus("current")
_H3cStorageInterfaceIndex_Type = Integer32
_H3cStorageInterfaceIndex_Object = MibTableColumn
h3cStorageInterfaceIndex = _H3cStorageInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 1),
    _H3cStorageInterfaceIndex_Type()
)
h3cStorageInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cStorageInterfaceIndex.setStatus("current")
_H3cStorageInterfaceGateway_Type = InetAddress
_H3cStorageInterfaceGateway_Object = MibTableColumn
h3cStorageInterfaceGateway = _H3cStorageInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 2),
    _H3cStorageInterfaceGateway_Type()
)
h3cStorageInterfaceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStorageInterfaceGateway.setStatus("current")
_H3cStorageInterfaceGatewayType_Type = InetAddressType
_H3cStorageInterfaceGatewayType_Object = MibTableColumn
h3cStorageInterfaceGatewayType = _H3cStorageInterfaceGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 3),
    _H3cStorageInterfaceGatewayType_Type()
)
h3cStorageInterfaceGatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStorageInterfaceGatewayType.setStatus("current")


class _H3cStorageInterfaceMTU_Type(Integer32):
    """Custom type h3cStorageInterfaceMTU based on Integer32"""
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


_H3cStorageInterfaceMTU_Type.__name__ = "Integer32"
_H3cStorageInterfaceMTU_Object = MibTableColumn
h3cStorageInterfaceMTU = _H3cStorageInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 2, 1, 4),
    _H3cStorageInterfaceMTU_Type()
)
h3cStorageInterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cStorageInterfaceMTU.setStatus("current")
_H3cBondingTable_Object = MibTable
h3cBondingTable = _H3cBondingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cBondingTable.setStatus("current")
_H3cBondingEntry_Object = MibTableRow
h3cBondingEntry = _H3cBondingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3, 1)
)
h3cBondingEntry.setIndexNames(
    (0, "H3C-STORAGE-MIB", "h3cBondingIndex"),
)
if mibBuilder.loadTexts:
    h3cBondingEntry.setStatus("current")
_H3cBondingIndex_Type = Integer32
_H3cBondingIndex_Object = MibTableColumn
h3cBondingIndex = _H3cBondingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3, 1, 1),
    _H3cBondingIndex_Type()
)
h3cBondingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBondingIndex.setStatus("current")
_H3cBondingPortList_Type = OctetString
_H3cBondingPortList_Object = MibTableColumn
h3cBondingPortList = _H3cBondingPortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 3, 1, 2),
    _H3cBondingPortList_Type()
)
h3cBondingPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cBondingPortList.setStatus("current")
_H3cScsiAdapterTable_Object = MibTable
h3cScsiAdapterTable = _H3cScsiAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cScsiAdapterTable.setStatus("current")
_H3cScsiAdapterEntry_Object = MibTableRow
h3cScsiAdapterEntry = _H3cScsiAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1)
)
h3cScsiAdapterEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "H3C-STORAGE-MIB", "h3cAdapterNumber"),
)
if mibBuilder.loadTexts:
    h3cScsiAdapterEntry.setStatus("current")
_H3cAdapterNumber_Type = Integer32
_H3cAdapterNumber_Object = MibTableColumn
h3cAdapterNumber = _H3cAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 1),
    _H3cAdapterNumber_Type()
)
h3cAdapterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAdapterNumber.setStatus("current")
_H3cAdapterDesc_Type = OctetString
_H3cAdapterDesc_Object = MibTableColumn
h3cAdapterDesc = _H3cAdapterDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 2),
    _H3cAdapterDesc_Type()
)
h3cAdapterDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAdapterDesc.setStatus("current")


class _H3cAdapterType_Type(Integer32):
    """Custom type h3cAdapterType based on Integer32"""
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


_H3cAdapterType_Type.__name__ = "Integer32"
_H3cAdapterType_Object = MibTableColumn
h3cAdapterType = _H3cAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 3),
    _H3cAdapterType_Type()
)
h3cAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAdapterType.setStatus("current")


class _H3cFcAdapterMode_Type(Integer32):
    """Custom type h3cFcAdapterMode based on Integer32"""
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


_H3cFcAdapterMode_Type.__name__ = "Integer32"
_H3cFcAdapterMode_Object = MibTableColumn
h3cFcAdapterMode = _H3cFcAdapterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 4),
    _H3cFcAdapterMode_Type()
)
h3cFcAdapterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcAdapterMode.setStatus("current")
_H3cFcAdapterInitiatorWwpnName_Type = H3cWwpnListType
_H3cFcAdapterInitiatorWwpnName_Object = MibTableColumn
h3cFcAdapterInitiatorWwpnName = _H3cFcAdapterInitiatorWwpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 5),
    _H3cFcAdapterInitiatorWwpnName_Type()
)
h3cFcAdapterInitiatorWwpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcAdapterInitiatorWwpnName.setStatus("current")
_H3cFcAdapterTargetWwpnName_Type = H3cWwpnListType
_H3cFcAdapterTargetWwpnName_Object = MibTableColumn
h3cFcAdapterTargetWwpnName = _H3cFcAdapterTargetWwpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 6),
    _H3cFcAdapterTargetWwpnName_Type()
)
h3cFcAdapterTargetWwpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcAdapterTargetWwpnName.setStatus("current")


class _H3cFcAdapterPortState_Type(Integer32):
    """Custom type h3cFcAdapterPortState based on Integer32"""
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


_H3cFcAdapterPortState_Type.__name__ = "Integer32"
_H3cFcAdapterPortState_Object = MibTableColumn
h3cFcAdapterPortState = _H3cFcAdapterPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 7),
    _H3cFcAdapterPortState_Type()
)
h3cFcAdapterPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcAdapterPortState.setStatus("current")


class _H3cFcAdapterModeSwitch_Type(H3cStorageEnableState):
    """Custom type h3cFcAdapterModeSwitch based on H3cStorageEnableState"""


_H3cFcAdapterModeSwitch_Object = MibTableColumn
h3cFcAdapterModeSwitch = _H3cFcAdapterModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 4, 1, 8),
    _H3cFcAdapterModeSwitch_Type()
)
h3cFcAdapterModeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcAdapterModeSwitch.setStatus("current")
_H3cExtVoltageTable_Object = MibTable
h3cExtVoltageTable = _H3cExtVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    h3cExtVoltageTable.setStatus("current")
_H3cExtVoltageEntry_Object = MibTableRow
h3cExtVoltageEntry = _H3cExtVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1)
)
h3cExtVoltageEntry.setIndexNames(
    (0, "H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cExtVoltageEntry.setStatus("current")
_H3cExtVoltagePhysicalIndex_Type = PhysicalIndex
_H3cExtVoltagePhysicalIndex_Object = MibTableColumn
h3cExtVoltagePhysicalIndex = _H3cExtVoltagePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 1),
    _H3cExtVoltagePhysicalIndex_Type()
)
h3cExtVoltagePhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cExtVoltagePhysicalIndex.setStatus("current")
_H3cExtVoltagePhysicalName_Type = SnmpAdminString
_H3cExtVoltagePhysicalName_Object = MibTableColumn
h3cExtVoltagePhysicalName = _H3cExtVoltagePhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 2),
    _H3cExtVoltagePhysicalName_Type()
)
h3cExtVoltagePhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cExtVoltagePhysicalName.setStatus("current")
_H3cExtVoltage_Type = Integer32
_H3cExtVoltage_Object = MibTableColumn
h3cExtVoltage = _H3cExtVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 3),
    _H3cExtVoltage_Type()
)
h3cExtVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cExtVoltage.setStatus("current")
_H3cExtVoltageLowThreshold_Type = Integer32
_H3cExtVoltageLowThreshold_Object = MibTableColumn
h3cExtVoltageLowThreshold = _H3cExtVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 4),
    _H3cExtVoltageLowThreshold_Type()
)
h3cExtVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cExtVoltageLowThreshold.setStatus("current")
_H3cExtVoltageHighThreshold_Type = Integer32
_H3cExtVoltageHighThreshold_Object = MibTableColumn
h3cExtVoltageHighThreshold = _H3cExtVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 5),
    _H3cExtVoltageHighThreshold_Type()
)
h3cExtVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cExtVoltageHighThreshold.setStatus("current")
_H3cExtCriticalVoltageLowThreshold_Type = Integer32
_H3cExtCriticalVoltageLowThreshold_Object = MibTableColumn
h3cExtCriticalVoltageLowThreshold = _H3cExtCriticalVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 6),
    _H3cExtCriticalVoltageLowThreshold_Type()
)
h3cExtCriticalVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cExtCriticalVoltageLowThreshold.setStatus("current")
_H3cExtCriticalVoltageHighThreshold_Type = Integer32
_H3cExtCriticalVoltageHighThreshold_Object = MibTableColumn
h3cExtCriticalVoltageHighThreshold = _H3cExtCriticalVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 7),
    _H3cExtCriticalVoltageHighThreshold_Type()
)
h3cExtCriticalVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cExtCriticalVoltageHighThreshold.setStatus("current")
_H3cExtShutdownVoltageLowThreshold_Type = Integer32
_H3cExtShutdownVoltageLowThreshold_Object = MibTableColumn
h3cExtShutdownVoltageLowThreshold = _H3cExtShutdownVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 8),
    _H3cExtShutdownVoltageLowThreshold_Type()
)
h3cExtShutdownVoltageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cExtShutdownVoltageLowThreshold.setStatus("current")
_H3cExtShutdownVoltageHighThreshold_Type = Integer32
_H3cExtShutdownVoltageHighThreshold_Object = MibTableColumn
h3cExtShutdownVoltageHighThreshold = _H3cExtShutdownVoltageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 2, 5, 1, 9),
    _H3cExtShutdownVoltageHighThreshold_Type()
)
h3cExtShutdownVoltageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cExtShutdownVoltageHighThreshold.setStatus("current")
_H3cStorageTraps_ObjectIdentity = ObjectIdentity
h3cStorageTraps = _H3cStorageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3)
)
_H3cStorageTrapsPrefix_ObjectIdentity = ObjectIdentity
h3cStorageTrapsPrefix = _H3cStorageTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0)
)
_H3cStorageTrapsObjects_ObjectIdentity = ObjectIdentity
h3cStorageTrapsObjects = _H3cStorageTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 1)
)
_H3cSoftwareInfoString_Type = H3cSoftwareInfoString
_H3cSoftwareInfoString_Object = MibScalar
h3cSoftwareInfoString = _H3cSoftwareInfoString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 1, 1),
    _H3cSoftwareInfoString_Type()
)
h3cSoftwareInfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSoftwareInfoString.setStatus("current")

# Managed Objects groups


# Notification objects

h3cStorCriticalLowerTemperatureThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 1)
)
h3cStorCriticalLowerTemperatureThresholdNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtCriticalLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    h3cStorCriticalLowerTemperatureThresholdNotification.setStatus(
        "current"
    )

h3cStorTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 2)
)
h3cStorTemperatureTooLow.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtTemperature"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtShutdownLowerTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    h3cStorTemperatureTooLow.setStatus(
        "current"
    )

h3cExtVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 3)
)
h3cExtVoltageLowThresholdNotification.setObjects(
      *(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
        ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"),
        ("H3C-STORAGE-MIB", "h3cExtVoltage"),
        ("H3C-STORAGE-MIB", "h3cExtVoltageLowThreshold"))
)
if mibBuilder.loadTexts:
    h3cExtVoltageLowThresholdNotification.setStatus(
        "current"
    )

h3cExtVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 4)
)
h3cExtVoltageHighThresholdNotification.setObjects(
      *(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
        ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"),
        ("H3C-STORAGE-MIB", "h3cExtVoltage"),
        ("H3C-STORAGE-MIB", "h3cExtVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    h3cExtVoltageHighThresholdNotification.setStatus(
        "current"
    )

h3cExtCriticalVoltageLowThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 5)
)
h3cExtCriticalVoltageLowThresholdNotification.setObjects(
      *(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
        ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"),
        ("H3C-STORAGE-MIB", "h3cExtVoltage"),
        ("H3C-STORAGE-MIB", "h3cExtCriticalVoltageLowThreshold"))
)
if mibBuilder.loadTexts:
    h3cExtCriticalVoltageLowThresholdNotification.setStatus(
        "current"
    )

h3cExtCriticalVoltageHighThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 6)
)
h3cExtCriticalVoltageHighThresholdNotification.setObjects(
      *(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
        ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"),
        ("H3C-STORAGE-MIB", "h3cExtVoltage"),
        ("H3C-STORAGE-MIB", "h3cExtCriticalVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    h3cExtCriticalVoltageHighThresholdNotification.setStatus(
        "current"
    )

h3cExtVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 7)
)
h3cExtVoltageTooLow.setObjects(
      *(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
        ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"),
        ("H3C-STORAGE-MIB", "h3cExtVoltage"),
        ("H3C-STORAGE-MIB", "h3cExtShutdownVoltageLowThreshold"))
)
if mibBuilder.loadTexts:
    h3cExtVoltageTooLow.setStatus(
        "current"
    )

h3cExtVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 8)
)
h3cExtVoltageTooHigh.setObjects(
      *(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
        ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"),
        ("H3C-STORAGE-MIB", "h3cExtVoltage"),
        ("H3C-STORAGE-MIB", "h3cExtShutdownVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    h3cExtVoltageTooHigh.setStatus(
        "current"
    )

h3cExtBatteryStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 9)
)
h3cExtBatteryStateNotification.setObjects(
      *(("H3C-ENTITY-EXT-MIB", "h3cEntityExtPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("H3C-ENTITY-EXT-MIB", "h3cEntityExtOperStatus"))
)
if mibBuilder.loadTexts:
    h3cExtBatteryStateNotification.setStatus(
        "current"
    )

h3cDiskIOErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 10)
)
h3cDiskIOErrorNotification.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    h3cDiskIOErrorNotification.setStatus(
        "current"
    )

h3cRaidCreateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 11)
)
h3cRaidCreateNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidCreateNotification.setStatus(
        "current"
    )

h3cRaidDeleteNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 12)
)
h3cRaidDeleteNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidDeleteNotification.setStatus(
        "current"
    )

h3cRaidHideStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 13)
)
h3cRaidHideStateNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"),
        ("H3C-RAID-MIB", "h3cRaidHideState"))
)
if mibBuilder.loadTexts:
    h3cRaidHideStateNotification.setStatus(
        "current"
    )

h3cRaidRunStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 14)
)
h3cRaidRunStateNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"),
        ("H3C-RAID-MIB", "h3cRaidRunState"))
)
if mibBuilder.loadTexts:
    h3cRaidRunStateNotification.setStatus(
        "current"
    )

h3cRaidImportNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 15)
)
h3cRaidImportNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidImportNotification.setStatus(
        "current"
    )

h3cRaidRebuildStartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 16)
)
h3cRaidRebuildStartNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidRebuildStartNotification.setStatus(
        "current"
    )

h3cRaidRebuildFinishNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 17)
)
h3cRaidRebuildFinishNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidRebuildFinishNotification.setStatus(
        "current"
    )

h3cRaidRebuildPauseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 18)
)
h3cRaidRebuildPauseNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidRebuildPauseNotification.setStatus(
        "current"
    )

h3cRaidRebuildInterruptNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 19)
)
h3cRaidRebuildInterruptNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidRebuildInterruptNotification.setStatus(
        "current"
    )

h3cSoftwareModuleFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 20)
)
h3cSoftwareModuleFailNotification.setObjects(
    ("H3C-STORAGE-MIB", "h3cSoftwareInfoString")
)
if mibBuilder.loadTexts:
    h3cSoftwareModuleFailNotification.setStatus(
        "current"
    )

h3cRaidBatteryExpiredNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 21)
)
if mibBuilder.loadTexts:
    h3cRaidBatteryExpiredNotification.setStatus(
        "current"
    )

h3cRaidBatteryWillExpireNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 22)
)
if mibBuilder.loadTexts:
    h3cRaidBatteryWillExpireNotification.setStatus(
        "current"
    )

h3cLvOnlineFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 23)
)
h3cLvOnlineFailNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cLvOnlineFailNotification.setStatus(
        "current"
    )

h3cLvOfflineFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 24)
)
h3cLvOfflineFailNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cLvOfflineFailNotification.setStatus(
        "current"
    )

h3cRaidRunNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 25)
)
h3cRaidRunNotification.setObjects(
      *(("H3C-RAID-MIB", "h3cRaidUuid"),
        ("H3C-RAID-MIB", "h3cRaidName"))
)
if mibBuilder.loadTexts:
    h3cRaidRunNotification.setStatus(
        "current"
    )

h3cExtVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 26)
)
h3cExtVoltageNormal.setObjects(
      *(("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalIndex"),
        ("H3C-STORAGE-MIB", "h3cExtVoltagePhysicalName"),
        ("H3C-STORAGE-MIB", "h3cExtVoltage"),
        ("H3C-STORAGE-MIB", "h3cExtVoltageLowThreshold"),
        ("H3C-STORAGE-MIB", "h3cExtVoltageHighThreshold"))
)
if mibBuilder.loadTexts:
    h3cExtVoltageNormal.setStatus(
        "current"
    )

h3cDiskPowerOnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 27)
)
h3cDiskPowerOnNotification.setObjects(
    ("ENTITY-MIB", "entPhysicalDescr")
)
if mibBuilder.loadTexts:
    h3cDiskPowerOnNotification.setStatus(
        "current"
    )

h3cDiskPowerOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 1, 1, 3, 0, 28)
)
h3cDiskPowerOffNotification.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("H3C-DISK-MIB", "h3cDiskPowerOffReason"))
)
if mibBuilder.loadTexts:
    h3cDiskPowerOffNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-STORAGE-MIB",
    **{"h3cStorageMIB": h3cStorageMIB,
       "h3cStorageMibObjects": h3cStorageMibObjects,
       "h3cStorageServerInfo": h3cStorageServerInfo,
       "h3cStorageServerCapability": h3cStorageServerCapability,
       "h3cRaidCapability": h3cRaidCapability,
       "h3cFcCapability": h3cFcCapability,
       "h3cNasCapability": h3cNasCapability,
       "h3cAdaptiveRepCapability": h3cAdaptiveRepCapability,
       "h3cRemoteRepCapability": h3cRemoteRepCapability,
       "h3cSafeCacheCapability": h3cSafeCacheCapability,
       "h3cSyncMirrorCapability": h3cSyncMirrorCapability,
       "h3cAsyncMirrorCapability": h3cAsyncMirrorCapability,
       "h3cTimeMarkCapability": h3cTimeMarkCapability,
       "h3cSseCapability": h3cSseCapability,
       "h3cStorageTargetConfig": h3cStorageTargetConfig,
       "h3ciSCSITargetEnable": h3ciSCSITargetEnable,
       "h3cFcTargetEnable": h3cFcTargetEnable,
       "h3cStorageServerPhysInfo": h3cStorageServerPhysInfo,
       "h3cServerLocationLedState": h3cServerLocationLedState,
       "h3cServerResetButtonState": h3cServerResetButtonState,
       "h3cServerPowerButtonState": h3cServerPowerButtonState,
       "h3cServerPowerState": h3cServerPowerState,
       "h3cStoragePhysicalInfo": h3cStoragePhysicalInfo,
       "h3cDeuTable": h3cDeuTable,
       "h3cDeuEntry": h3cDeuEntry,
       "h3cDeuIndex": h3cDeuIndex,
       "h3cDeuIDLed": h3cDeuIDLed,
       "h3cDeuDiskScan": h3cDeuDiskScan,
       "h3cStorageInterfaceTable": h3cStorageInterfaceTable,
       "h3cStorageInterfaceEntry": h3cStorageInterfaceEntry,
       "h3cStorageInterfaceIndex": h3cStorageInterfaceIndex,
       "h3cStorageInterfaceGateway": h3cStorageInterfaceGateway,
       "h3cStorageInterfaceGatewayType": h3cStorageInterfaceGatewayType,
       "h3cStorageInterfaceMTU": h3cStorageInterfaceMTU,
       "h3cBondingTable": h3cBondingTable,
       "h3cBondingEntry": h3cBondingEntry,
       "h3cBondingIndex": h3cBondingIndex,
       "h3cBondingPortList": h3cBondingPortList,
       "h3cScsiAdapterTable": h3cScsiAdapterTable,
       "h3cScsiAdapterEntry": h3cScsiAdapterEntry,
       "h3cAdapterNumber": h3cAdapterNumber,
       "h3cAdapterDesc": h3cAdapterDesc,
       "h3cAdapterType": h3cAdapterType,
       "h3cFcAdapterMode": h3cFcAdapterMode,
       "h3cFcAdapterInitiatorWwpnName": h3cFcAdapterInitiatorWwpnName,
       "h3cFcAdapterTargetWwpnName": h3cFcAdapterTargetWwpnName,
       "h3cFcAdapterPortState": h3cFcAdapterPortState,
       "h3cFcAdapterModeSwitch": h3cFcAdapterModeSwitch,
       "h3cExtVoltageTable": h3cExtVoltageTable,
       "h3cExtVoltageEntry": h3cExtVoltageEntry,
       "h3cExtVoltagePhysicalIndex": h3cExtVoltagePhysicalIndex,
       "h3cExtVoltagePhysicalName": h3cExtVoltagePhysicalName,
       "h3cExtVoltage": h3cExtVoltage,
       "h3cExtVoltageLowThreshold": h3cExtVoltageLowThreshold,
       "h3cExtVoltageHighThreshold": h3cExtVoltageHighThreshold,
       "h3cExtCriticalVoltageLowThreshold": h3cExtCriticalVoltageLowThreshold,
       "h3cExtCriticalVoltageHighThreshold": h3cExtCriticalVoltageHighThreshold,
       "h3cExtShutdownVoltageLowThreshold": h3cExtShutdownVoltageLowThreshold,
       "h3cExtShutdownVoltageHighThreshold": h3cExtShutdownVoltageHighThreshold,
       "h3cStorageTraps": h3cStorageTraps,
       "h3cStorageTrapsPrefix": h3cStorageTrapsPrefix,
       "h3cStorCriticalLowerTemperatureThresholdNotification": h3cStorCriticalLowerTemperatureThresholdNotification,
       "h3cStorTemperatureTooLow": h3cStorTemperatureTooLow,
       "h3cExtVoltageLowThresholdNotification": h3cExtVoltageLowThresholdNotification,
       "h3cExtVoltageHighThresholdNotification": h3cExtVoltageHighThresholdNotification,
       "h3cExtCriticalVoltageLowThresholdNotification": h3cExtCriticalVoltageLowThresholdNotification,
       "h3cExtCriticalVoltageHighThresholdNotification": h3cExtCriticalVoltageHighThresholdNotification,
       "h3cExtVoltageTooLow": h3cExtVoltageTooLow,
       "h3cExtVoltageTooHigh": h3cExtVoltageTooHigh,
       "h3cExtBatteryStateNotification": h3cExtBatteryStateNotification,
       "h3cDiskIOErrorNotification": h3cDiskIOErrorNotification,
       "h3cRaidCreateNotification": h3cRaidCreateNotification,
       "h3cRaidDeleteNotification": h3cRaidDeleteNotification,
       "h3cRaidHideStateNotification": h3cRaidHideStateNotification,
       "h3cRaidRunStateNotification": h3cRaidRunStateNotification,
       "h3cRaidImportNotification": h3cRaidImportNotification,
       "h3cRaidRebuildStartNotification": h3cRaidRebuildStartNotification,
       "h3cRaidRebuildFinishNotification": h3cRaidRebuildFinishNotification,
       "h3cRaidRebuildPauseNotification": h3cRaidRebuildPauseNotification,
       "h3cRaidRebuildInterruptNotification": h3cRaidRebuildInterruptNotification,
       "h3cSoftwareModuleFailNotification": h3cSoftwareModuleFailNotification,
       "h3cRaidBatteryExpiredNotification": h3cRaidBatteryExpiredNotification,
       "h3cRaidBatteryWillExpireNotification": h3cRaidBatteryWillExpireNotification,
       "h3cLvOnlineFailNotification": h3cLvOnlineFailNotification,
       "h3cLvOfflineFailNotification": h3cLvOfflineFailNotification,
       "h3cRaidRunNotification": h3cRaidRunNotification,
       "h3cExtVoltageNormal": h3cExtVoltageNormal,
       "h3cDiskPowerOnNotification": h3cDiskPowerOnNotification,
       "h3cDiskPowerOffNotification": h3cDiskPowerOffNotification,
       "h3cStorageTrapsObjects": h3cStorageTrapsObjects,
       "h3cSoftwareInfoString": h3cSoftwareInfoString}
)
