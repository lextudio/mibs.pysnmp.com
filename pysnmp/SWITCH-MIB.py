# SNMP MIB module (SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:16 2024
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
 NotificationType,
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
    "NotificationType",
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vendor_ObjectIdentity = ObjectIdentity
vendor = _Vendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295)
)
_EthernetSwitchingDevice_ObjectIdentity = ObjectIdentity
ethernetSwitchingDevice = _EthernetSwitchingDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3)
)
_DeviceHardware_ObjectIdentity = ObjectIdentity
deviceHardware = _DeviceHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1)
)
_DeviceChassis_ObjectIdentity = ObjectIdentity
deviceChassis = _DeviceChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 1)
)
_DevicePort_ObjectIdentity = ObjectIdentity
devicePort = _DevicePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2)
)
_EthernetPort_ObjectIdentity = ObjectIdentity
ethernetPort = _EthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 1)
)
_WaveBusPort_ObjectIdentity = ObjectIdentity
waveBusPort = _WaveBusPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 2)
)
_FddiPort_ObjectIdentity = ObjectIdentity
fddiPort = _FddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 3)
)
_DeviceSoftware_ObjectIdentity = ObjectIdentity
deviceSoftware = _DeviceSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 2)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1)
)
_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("mandatory")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1)
)
chassisEntry.setIndexNames(
    (0, "SWITCH-MIB", "chassisIndex"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("mandatory")
_ChassisProductCode_Type = DisplayString
_ChassisProductCode_Object = MibTableColumn
chassisProductCode = _ChassisProductCode_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 1),
    _ChassisProductCode_Type()
)
chassisProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisProductCode.setStatus("mandatory")
_ChassisSerialNumber_Type = DisplayString
_ChassisSerialNumber_Object = MibTableColumn
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 2),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("mandatory")


class _ChassisPlaceOfManufacture_Type(Integer32):
    """Custom type chassisPlaceOfManufacture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ottawa", 1)
    )


_ChassisPlaceOfManufacture_Type.__name__ = "Integer32"
_ChassisPlaceOfManufacture_Object = MibTableColumn
chassisPlaceOfManufacture = _ChassisPlaceOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 3),
    _ChassisPlaceOfManufacture_Type()
)
chassisPlaceOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPlaceOfManufacture.setStatus("mandatory")
_ChassisDateOfManufacture_Type = DisplayString
_ChassisDateOfManufacture_Object = MibTableColumn
chassisDateOfManufacture = _ChassisDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 4),
    _ChassisDateOfManufacture_Type()
)
chassisDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisDateOfManufacture.setStatus("mandatory")
_ChassisMacAddress_Type = MacAddress
_ChassisMacAddress_Object = MibTableColumn
chassisMacAddress = _ChassisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 5),
    _ChassisMacAddress_Type()
)
chassisMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMacAddress.setStatus("mandatory")
_ChassisCodeVersion_Type = DisplayString
_ChassisCodeVersion_Object = MibTableColumn
chassisCodeVersion = _ChassisCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 6),
    _ChassisCodeVersion_Type()
)
chassisCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCodeVersion.setStatus("mandatory")
_ChassisBpeEnabled_Type = Integer32
_ChassisBpeEnabled_Object = MibTableColumn
chassisBpeEnabled = _ChassisBpeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 7),
    _ChassisBpeEnabled_Type()
)
chassisBpeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisBpeEnabled.setStatus("mandatory")
_ChassisEraseSnmpConfigInfo_Type = Integer32
_ChassisEraseSnmpConfigInfo_Object = MibTableColumn
chassisEraseSnmpConfigInfo = _ChassisEraseSnmpConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 8),
    _ChassisEraseSnmpConfigInfo_Type()
)
chassisEraseSnmpConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisEraseSnmpConfigInfo.setStatus("mandatory")
_ChassisRestoreDot1dDefaults_Type = Integer32
_ChassisRestoreDot1dDefaults_Object = MibTableColumn
chassisRestoreDot1dDefaults = _ChassisRestoreDot1dDefaults_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 9),
    _ChassisRestoreDot1dDefaults_Type()
)
chassisRestoreDot1dDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisRestoreDot1dDefaults.setStatus("mandatory")
_ChassisPerformReset_Type = Integer32
_ChassisPerformReset_Object = MibTableColumn
chassisPerformReset = _ChassisPerformReset_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 10),
    _ChassisPerformReset_Type()
)
chassisPerformReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisPerformReset.setStatus("mandatory")
_ChassisIdentPressed_Type = Integer32
_ChassisIdentPressed_Object = MibTableColumn
chassisIdentPressed = _ChassisIdentPressed_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 11),
    _ChassisIdentPressed_Type()
)
chassisIdentPressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIdentPressed.setStatus("mandatory")
_ChassisAgeFilterDatabase_Type = Integer32
_ChassisAgeFilterDatabase_Object = MibTableColumn
chassisAgeFilterDatabase = _ChassisAgeFilterDatabase_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 12),
    _ChassisAgeFilterDatabase_Type()
)
chassisAgeFilterDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAgeFilterDatabase.setStatus("mandatory")
_ChassisClearStatistics_Type = Integer32
_ChassisClearStatistics_Object = MibTableColumn
chassisClearStatistics = _ChassisClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 13),
    _ChassisClearStatistics_Type()
)
chassisClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisClearStatistics.setStatus("mandatory")
_ChassisTcpKeepAlivesEnabled_Type = Integer32
_ChassisTcpKeepAlivesEnabled_Object = MibTableColumn
chassisTcpKeepAlivesEnabled = _ChassisTcpKeepAlivesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 14),
    _ChassisTcpKeepAlivesEnabled_Type()
)
chassisTcpKeepAlivesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisTcpKeepAlivesEnabled.setStatus("mandatory")
_ChassisTcpKeepAlivePeriod_Type = Integer32
_ChassisTcpKeepAlivePeriod_Object = MibTableColumn
chassisTcpKeepAlivePeriod = _ChassisTcpKeepAlivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 15),
    _ChassisTcpKeepAlivePeriod_Type()
)
chassisTcpKeepAlivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisTcpKeepAlivePeriod.setStatus("mandatory")
_ChassisIndex_Type = Integer32
_ChassisIndex_Object = MibTableColumn
chassisIndex = _ChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 100),
    _ChassisIndex_Type()
)
chassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIndex.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1)
)
portEntry.setIndexNames(
    (0, "SWITCH-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_PortProductCode_Type = DisplayString
_PortProductCode_Object = MibTableColumn
portProductCode = _PortProductCode_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 2),
    _PortProductCode_Type()
)
portProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portProductCode.setStatus("mandatory")
_PortSerialNumber_Type = DisplayString
_PortSerialNumber_Object = MibTableColumn
portSerialNumber = _PortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 3),
    _PortSerialNumber_Type()
)
portSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSerialNumber.setStatus("mandatory")


class _PortPlaceOfManufacture_Type(Integer32):
    """Custom type portPlaceOfManufacture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ottawa", 1)
    )


_PortPlaceOfManufacture_Type.__name__ = "Integer32"
_PortPlaceOfManufacture_Object = MibTableColumn
portPlaceOfManufacture = _PortPlaceOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 4),
    _PortPlaceOfManufacture_Type()
)
portPlaceOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPlaceOfManufacture.setStatus("mandatory")
_PortDateOfManufacture_Type = DisplayString
_PortDateOfManufacture_Object = MibTableColumn
portDateOfManufacture = _PortDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 5),
    _PortDateOfManufacture_Type()
)
portDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDateOfManufacture.setStatus("mandatory")
_PortState_Type = DisplayString
_PortState_Object = MibTableColumn
portState = _PortState_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 6),
    _PortState_Type()
)
portState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portState.setStatus("mandatory")
_PortHighSensitivity_Type = Integer32
_PortHighSensitivity_Object = MibTableColumn
portHighSensitivity = _PortHighSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 7),
    _PortHighSensitivity_Type()
)
portHighSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portHighSensitivity.setStatus("mandatory")
_PortRestoreFddiMibDefaults_Type = Integer32
_PortRestoreFddiMibDefaults_Object = MibTableColumn
portRestoreFddiMibDefaults = _PortRestoreFddiMibDefaults_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 8),
    _PortRestoreFddiMibDefaults_Type()
)
portRestoreFddiMibDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRestoreFddiMibDefaults.setStatus("mandatory")
_PortTranslateAllEthertypes_Type = Integer32
_PortTranslateAllEthertypes_Object = MibTableColumn
portTranslateAllEthertypes = _PortTranslateAllEthertypes_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 9),
    _PortTranslateAllEthertypes_Type()
)
portTranslateAllEthertypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTranslateAllEthertypes.setStatus("mandatory")
_PortTxFrames_Type = Counter32
_PortTxFrames_Object = MibTableColumn
portTxFrames = _PortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 10),
    _PortTxFrames_Type()
)
portTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTxFrames.setStatus("mandatory")
_PortRxFrames_Type = Counter32
_PortRxFrames_Object = MibTableColumn
portRxFrames = _PortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 11),
    _PortRxFrames_Type()
)
portRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxFrames.setStatus("mandatory")
_PortFcsErrors_Type = Counter32
_PortFcsErrors_Object = MibTableColumn
portFcsErrors = _PortFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 12),
    _PortFcsErrors_Type()
)
portFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFcsErrors.setStatus("mandatory")
_PortFilterDiscards_Type = Counter32
_PortFilterDiscards_Object = MibTableColumn
portFilterDiscards = _PortFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 13),
    _PortFilterDiscards_Type()
)
portFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFilterDiscards.setStatus("mandatory")
_PortDelayExceededDiscards_Type = Counter32
_PortDelayExceededDiscards_Object = MibTableColumn
portDelayExceededDiscards = _PortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 14),
    _PortDelayExceededDiscards_Type()
)
portDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDelayExceededDiscards.setStatus("mandatory")
_PortMtuExceededDiscards_Type = Counter32
_PortMtuExceededDiscards_Object = MibTableColumn
portMtuExceededDiscards = _PortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 15),
    _PortMtuExceededDiscards_Type()
)
portMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMtuExceededDiscards.setStatus("mandatory")
_PortFddiTooLongNonIpFrames_Type = Counter32
_PortFddiTooLongNonIpFrames_Object = MibTableColumn
portFddiTooLongNonIpFrames = _PortFddiTooLongNonIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 16),
    _PortFddiTooLongNonIpFrames_Type()
)
portFddiTooLongNonIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFddiTooLongNonIpFrames.setStatus("mandatory")
_PortConnected_Type = Integer32
_PortConnected_Object = MibTableColumn
portConnected = _PortConnected_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 17),
    _PortConnected_Type()
)
portConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConnected.setStatus("mandatory")
_SttTable_Object = MibTable
sttTable = _SttTable_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sttTable.setStatus("mandatory")
_SttEntry_Object = MibTableRow
sttEntry = _SttEntry_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1)
)
sttEntry.setIndexNames(
    (0, "SWITCH-MIB", "sttPortIndex"),
)
if mibBuilder.loadTexts:
    sttEntry.setStatus("mandatory")
_SttPortIndex_Type = Integer32
_SttPortIndex_Object = MibTableColumn
sttPortIndex = _SttPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 1),
    _SttPortIndex_Type()
)
sttPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sttPortIndex.setStatus("mandatory")
_SttEthertype1_Type = Integer32
_SttEthertype1_Object = MibTableColumn
sttEthertype1 = _SttEthertype1_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 2),
    _SttEthertype1_Type()
)
sttEthertype1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sttEthertype1.setStatus("mandatory")
_SttEntryValid1_Type = Integer32
_SttEntryValid1_Object = MibTableColumn
sttEntryValid1 = _SttEntryValid1_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 3),
    _SttEntryValid1_Type()
)
sttEntryValid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sttEntryValid1.setStatus("mandatory")
_SttEthertype2_Type = Integer32
_SttEthertype2_Object = MibTableColumn
sttEthertype2 = _SttEthertype2_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 4),
    _SttEthertype2_Type()
)
sttEthertype2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sttEthertype2.setStatus("mandatory")
_SttEntryValid2_Type = Integer32
_SttEntryValid2_Object = MibTableColumn
sttEntryValid2 = _SttEntryValid2_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 5),
    _SttEntryValid2_Type()
)
sttEntryValid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sttEntryValid2.setStatus("mandatory")
_SttEthertype3_Type = Integer32
_SttEthertype3_Object = MibTableColumn
sttEthertype3 = _SttEthertype3_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 6),
    _SttEthertype3_Type()
)
sttEthertype3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sttEthertype3.setStatus("mandatory")
_SttEntryValid3_Type = Integer32
_SttEntryValid3_Object = MibTableColumn
sttEntryValid3 = _SttEntryValid3_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 7),
    _SttEntryValid3_Type()
)
sttEntryValid3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sttEntryValid3.setStatus("mandatory")

# Managed Objects groups


# Notification objects

touched = NotificationType(
    (1, 3, 6, 1, 4, 1, 295, 0, 9)
)
touched.setObjects(
    ("SWITCH-MIB", "chassisIdentPressed")
)
if mibBuilder.loadTexts:
    touched.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-MIB",
    **{"MacAddress": MacAddress,
       "vendor": vendor,
       "touched": touched,
       "ethernetSwitchingDevice": ethernetSwitchingDevice,
       "deviceHardware": deviceHardware,
       "deviceChassis": deviceChassis,
       "devicePort": devicePort,
       "ethernetPort": ethernetPort,
       "waveBusPort": waveBusPort,
       "fddiPort": fddiPort,
       "deviceSoftware": deviceSoftware,
       "deviceInfo": deviceInfo,
       "chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisProductCode": chassisProductCode,
       "chassisSerialNumber": chassisSerialNumber,
       "chassisPlaceOfManufacture": chassisPlaceOfManufacture,
       "chassisDateOfManufacture": chassisDateOfManufacture,
       "chassisMacAddress": chassisMacAddress,
       "chassisCodeVersion": chassisCodeVersion,
       "chassisBpeEnabled": chassisBpeEnabled,
       "chassisEraseSnmpConfigInfo": chassisEraseSnmpConfigInfo,
       "chassisRestoreDot1dDefaults": chassisRestoreDot1dDefaults,
       "chassisPerformReset": chassisPerformReset,
       "chassisIdentPressed": chassisIdentPressed,
       "chassisAgeFilterDatabase": chassisAgeFilterDatabase,
       "chassisClearStatistics": chassisClearStatistics,
       "chassisTcpKeepAlivesEnabled": chassisTcpKeepAlivesEnabled,
       "chassisTcpKeepAlivePeriod": chassisTcpKeepAlivePeriod,
       "chassisIndex": chassisIndex,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portProductCode": portProductCode,
       "portSerialNumber": portSerialNumber,
       "portPlaceOfManufacture": portPlaceOfManufacture,
       "portDateOfManufacture": portDateOfManufacture,
       "portState": portState,
       "portHighSensitivity": portHighSensitivity,
       "portRestoreFddiMibDefaults": portRestoreFddiMibDefaults,
       "portTranslateAllEthertypes": portTranslateAllEthertypes,
       "portTxFrames": portTxFrames,
       "portRxFrames": portRxFrames,
       "portFcsErrors": portFcsErrors,
       "portFilterDiscards": portFilterDiscards,
       "portDelayExceededDiscards": portDelayExceededDiscards,
       "portMtuExceededDiscards": portMtuExceededDiscards,
       "portFddiTooLongNonIpFrames": portFddiTooLongNonIpFrames,
       "portConnected": portConnected,
       "sttTable": sttTable,
       "sttEntry": sttEntry,
       "sttPortIndex": sttPortIndex,
       "sttEthertype1": sttEthertype1,
       "sttEntryValid1": sttEntryValid1,
       "sttEthertype2": sttEthertype2,
       "sttEntryValid2": sttEntryValid2,
       "sttEthertype3": sttEthertype3,
       "sttEntryValid3": sttEntryValid3}
)
