# SNMP MIB module (PLAINTREE-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PLAINTREE-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:00 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1286-MIB",
    "MacAddress")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vendor_ObjectIdentity = ObjectIdentity
vendor = _Vendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3)
)
_SwitchHardware_ObjectIdentity = ObjectIdentity
switchHardware = _SwitchHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1)
)
_SwitchChassis_ObjectIdentity = ObjectIdentity
switchChassis = _SwitchChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 1)
)
_SwitchPort_ObjectIdentity = ObjectIdentity
switchPort = _SwitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2)
)
_SwitchEthernetPort_ObjectIdentity = ObjectIdentity
switchEthernetPort = _SwitchEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 1)
)
_SwitchWaveBusPort_ObjectIdentity = ObjectIdentity
switchWaveBusPort = _SwitchWaveBusPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 2)
)
_SwitchFddiPort_ObjectIdentity = ObjectIdentity
switchFddiPort = _SwitchFddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 3)
)
_SwitchSoftware_ObjectIdentity = ObjectIdentity
switchSoftware = _SwitchSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 2)
)
_SwitchInfo_ObjectIdentity = ObjectIdentity
switchInfo = _SwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1)
)
_SwitchBasicTable_Object = MibTable
switchBasicTable = _SwitchBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    switchBasicTable.setStatus("mandatory")
_SwitchBasicEntry_Object = MibTableRow
switchBasicEntry = _SwitchBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1)
)
switchBasicEntry.setIndexNames(
    (0, "PLAINTREE-SWITCH-MIB", "switchBasicIndex"),
)
if mibBuilder.loadTexts:
    switchBasicEntry.setStatus("mandatory")
_SwitchProductCode_Type = DisplayString
_SwitchProductCode_Object = MibTableColumn
switchProductCode = _SwitchProductCode_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 1),
    _SwitchProductCode_Type()
)
switchProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchProductCode.setStatus("mandatory")
_SwitchSerialNumber_Type = DisplayString
_SwitchSerialNumber_Object = MibTableColumn
switchSerialNumber = _SwitchSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 2),
    _SwitchSerialNumber_Type()
)
switchSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchSerialNumber.setStatus("mandatory")


class _SwitchPlaceOfManufacture_Type(Integer32):
    """Custom type switchPlaceOfManufacture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("inOttawa", 1)
    )


_SwitchPlaceOfManufacture_Type.__name__ = "Integer32"
_SwitchPlaceOfManufacture_Object = MibTableColumn
switchPlaceOfManufacture = _SwitchPlaceOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 3),
    _SwitchPlaceOfManufacture_Type()
)
switchPlaceOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPlaceOfManufacture.setStatus("mandatory")
_SwitchDateOfManufacture_Type = DisplayString
_SwitchDateOfManufacture_Object = MibTableColumn
switchDateOfManufacture = _SwitchDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 4),
    _SwitchDateOfManufacture_Type()
)
switchDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDateOfManufacture.setStatus("mandatory")
_SwitchMacAddress_Type = MacAddress
_SwitchMacAddress_Object = MibTableColumn
switchMacAddress = _SwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 5),
    _SwitchMacAddress_Type()
)
switchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchMacAddress.setStatus("mandatory")
_SwitchCodeVersion_Type = DisplayString
_SwitchCodeVersion_Object = MibTableColumn
switchCodeVersion = _SwitchCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 6),
    _SwitchCodeVersion_Type()
)
switchCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchCodeVersion.setStatus("mandatory")
_SwitchBpeEnabled_Type = Integer32
_SwitchBpeEnabled_Object = MibTableColumn
switchBpeEnabled = _SwitchBpeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 7),
    _SwitchBpeEnabled_Type()
)
switchBpeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchBpeEnabled.setStatus("mandatory")
_EraseSwitchSnmpConfigInfo_Type = Integer32
_EraseSwitchSnmpConfigInfo_Object = MibTableColumn
eraseSwitchSnmpConfigInfo = _EraseSwitchSnmpConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 8),
    _EraseSwitchSnmpConfigInfo_Type()
)
eraseSwitchSnmpConfigInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eraseSwitchSnmpConfigInfo.setStatus("mandatory")
_RestoreSwitchDot1dDefaults_Type = Integer32
_RestoreSwitchDot1dDefaults_Object = MibTableColumn
restoreSwitchDot1dDefaults = _RestoreSwitchDot1dDefaults_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 9),
    _RestoreSwitchDot1dDefaults_Type()
)
restoreSwitchDot1dDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreSwitchDot1dDefaults.setStatus("mandatory")
_PerformSwitchReset_Type = Integer32
_PerformSwitchReset_Object = MibTableColumn
performSwitchReset = _PerformSwitchReset_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 10),
    _PerformSwitchReset_Type()
)
performSwitchReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    performSwitchReset.setStatus("mandatory")
_SwitchIdentPressed_Type = Integer32
_SwitchIdentPressed_Object = MibTableColumn
switchIdentPressed = _SwitchIdentPressed_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 11),
    _SwitchIdentPressed_Type()
)
switchIdentPressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIdentPressed.setStatus("mandatory")
_AgeFilterDatabase_Type = Integer32
_AgeFilterDatabase_Object = MibTableColumn
ageFilterDatabase = _AgeFilterDatabase_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 12),
    _AgeFilterDatabase_Type()
)
ageFilterDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ageFilterDatabase.setStatus("mandatory")
_ClearStatistics_Type = Integer32
_ClearStatistics_Object = MibTableColumn
clearStatistics = _ClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 13),
    _ClearStatistics_Type()
)
clearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearStatistics.setStatus("mandatory")
_SwitchBasicIndex_Type = Integer32
_SwitchBasicIndex_Object = MibTableColumn
switchBasicIndex = _SwitchBasicIndex_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 100),
    _SwitchBasicIndex_Type()
)
switchBasicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchBasicIndex.setStatus("mandatory")
_SwitchPortTable_Object = MibTable
switchPortTable = _SwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    switchPortTable.setStatus("mandatory")
_SwitchPortEntry_Object = MibTableRow
switchPortEntry = _SwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1)
)
switchPortEntry.setIndexNames(
    (0, "PLAINTREE-SWITCH-MIB", "switchPortIndex"),
)
if mibBuilder.loadTexts:
    switchPortEntry.setStatus("mandatory")
_SwitchPortIndex_Type = Integer32
_SwitchPortIndex_Object = MibTableColumn
switchPortIndex = _SwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 1),
    _SwitchPortIndex_Type()
)
switchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortIndex.setStatus("mandatory")
_SwitchPortProductCode_Type = DisplayString
_SwitchPortProductCode_Object = MibTableColumn
switchPortProductCode = _SwitchPortProductCode_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 2),
    _SwitchPortProductCode_Type()
)
switchPortProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortProductCode.setStatus("mandatory")
_SwitchPortSerialNumber_Type = DisplayString
_SwitchPortSerialNumber_Object = MibTableColumn
switchPortSerialNumber = _SwitchPortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 3),
    _SwitchPortSerialNumber_Type()
)
switchPortSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortSerialNumber.setStatus("mandatory")


class _SwitchPortPlaceOfManufacture_Type(Integer32):
    """Custom type switchPortPlaceOfManufacture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("inOttawa", 1)
    )


_SwitchPortPlaceOfManufacture_Type.__name__ = "Integer32"
_SwitchPortPlaceOfManufacture_Object = MibTableColumn
switchPortPlaceOfManufacture = _SwitchPortPlaceOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 4),
    _SwitchPortPlaceOfManufacture_Type()
)
switchPortPlaceOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortPlaceOfManufacture.setStatus("mandatory")
_SwitchPortDateOfManufacture_Type = DisplayString
_SwitchPortDateOfManufacture_Object = MibTableColumn
switchPortDateOfManufacture = _SwitchPortDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 5),
    _SwitchPortDateOfManufacture_Type()
)
switchPortDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortDateOfManufacture.setStatus("mandatory")
_SwitchPortState_Type = DisplayString
_SwitchPortState_Object = MibTableColumn
switchPortState = _SwitchPortState_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 6),
    _SwitchPortState_Type()
)
switchPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortState.setStatus("mandatory")
_SwitchPortHighSensitivity_Type = Integer32
_SwitchPortHighSensitivity_Object = MibTableColumn
switchPortHighSensitivity = _SwitchPortHighSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 7),
    _SwitchPortHighSensitivity_Type()
)
switchPortHighSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPortHighSensitivity.setStatus("mandatory")
_RestoreFddiMibDefaults_Type = Integer32
_RestoreFddiMibDefaults_Object = MibTableColumn
restoreFddiMibDefaults = _RestoreFddiMibDefaults_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 8),
    _RestoreFddiMibDefaults_Type()
)
restoreFddiMibDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreFddiMibDefaults.setStatus("mandatory")
_TranslateAllEthertypes_Type = Integer32
_TranslateAllEthertypes_Object = MibTableColumn
translateAllEthertypes = _TranslateAllEthertypes_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 9),
    _TranslateAllEthertypes_Type()
)
translateAllEthertypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    translateAllEthertypes.setStatus("mandatory")
_SwitchPortTxFrames_Type = Counter32
_SwitchPortTxFrames_Object = MibTableColumn
switchPortTxFrames = _SwitchPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 10),
    _SwitchPortTxFrames_Type()
)
switchPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortTxFrames.setStatus("mandatory")
_SwitchPortRxFrames_Type = Counter32
_SwitchPortRxFrames_Object = MibTableColumn
switchPortRxFrames = _SwitchPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 11),
    _SwitchPortRxFrames_Type()
)
switchPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortRxFrames.setStatus("mandatory")
_SwitchPortFcsErrors_Type = Counter32
_SwitchPortFcsErrors_Object = MibTableColumn
switchPortFcsErrors = _SwitchPortFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 12),
    _SwitchPortFcsErrors_Type()
)
switchPortFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortFcsErrors.setStatus("mandatory")
_SwitchPortFilterDiscards_Type = Counter32
_SwitchPortFilterDiscards_Object = MibTableColumn
switchPortFilterDiscards = _SwitchPortFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 13),
    _SwitchPortFilterDiscards_Type()
)
switchPortFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortFilterDiscards.setStatus("mandatory")
_SwitchPortDelayExceededDiscards_Type = Counter32
_SwitchPortDelayExceededDiscards_Object = MibTableColumn
switchPortDelayExceededDiscards = _SwitchPortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 14),
    _SwitchPortDelayExceededDiscards_Type()
)
switchPortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortDelayExceededDiscards.setStatus("mandatory")
_SwitchPortMtuExceededDiscards_Type = Counter32
_SwitchPortMtuExceededDiscards_Object = MibTableColumn
switchPortMtuExceededDiscards = _SwitchPortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 15),
    _SwitchPortMtuExceededDiscards_Type()
)
switchPortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPortMtuExceededDiscards.setStatus("mandatory")
_SwitchSelectiveTranslationTable_Object = MibTable
switchSelectiveTranslationTable = _SwitchSelectiveTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    switchSelectiveTranslationTable.setStatus("mandatory")
_TranslationTableEntry_Object = MibTableRow
translationTableEntry = _TranslationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1)
)
translationTableEntry.setIndexNames(
    (0, "PLAINTREE-SWITCH-MIB", "translationTablePortIndex"),
)
if mibBuilder.loadTexts:
    translationTableEntry.setStatus("mandatory")
_TranslationTablePortIndex_Type = Integer32
_TranslationTablePortIndex_Object = MibTableColumn
translationTablePortIndex = _TranslationTablePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 1),
    _TranslationTablePortIndex_Type()
)
translationTablePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    translationTablePortIndex.setStatus("mandatory")
_TranslationTableEthertype1_Type = Integer32
_TranslationTableEthertype1_Object = MibTableColumn
translationTableEthertype1 = _TranslationTableEthertype1_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 2),
    _TranslationTableEthertype1_Type()
)
translationTableEthertype1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    translationTableEthertype1.setStatus("mandatory")
_TranslationTableEntryValid1_Type = Integer32
_TranslationTableEntryValid1_Object = MibTableColumn
translationTableEntryValid1 = _TranslationTableEntryValid1_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 3),
    _TranslationTableEntryValid1_Type()
)
translationTableEntryValid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    translationTableEntryValid1.setStatus("mandatory")
_TranslationTableEthertype2_Type = Integer32
_TranslationTableEthertype2_Object = MibTableColumn
translationTableEthertype2 = _TranslationTableEthertype2_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 4),
    _TranslationTableEthertype2_Type()
)
translationTableEthertype2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    translationTableEthertype2.setStatus("mandatory")
_TranslationTableEntryValid2_Type = Integer32
_TranslationTableEntryValid2_Object = MibTableColumn
translationTableEntryValid2 = _TranslationTableEntryValid2_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 5),
    _TranslationTableEntryValid2_Type()
)
translationTableEntryValid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    translationTableEntryValid2.setStatus("mandatory")
_TranslationTableEthertype3_Type = Integer32
_TranslationTableEthertype3_Object = MibTableColumn
translationTableEthertype3 = _TranslationTableEthertype3_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 6),
    _TranslationTableEthertype3_Type()
)
translationTableEthertype3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    translationTableEthertype3.setStatus("mandatory")
_TranslationTableEntryValid3_Type = Integer32
_TranslationTableEntryValid3_Object = MibTableColumn
translationTableEntryValid3 = _TranslationTableEntryValid3_Object(
    (1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 7),
    _TranslationTableEntryValid3_Type()
)
translationTableEntryValid3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    translationTableEntryValid3.setStatus("mandatory")

# Managed Objects groups


# Notification objects

switchTouched = NotificationType(
    (1, 3, 6, 1, 4, 1, 295, 0, 9)
)
switchTouched.setObjects(
    ("PLAINTREE-SWITCH-MIB", "switchIdentPressed")
)
if mibBuilder.loadTexts:
    switchTouched.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PLAINTREE-SWITCH-MIB",
    **{"vendor": vendor,
       "switchTouched": switchTouched,
       "switch": switch,
       "switchHardware": switchHardware,
       "switchChassis": switchChassis,
       "switchPort": switchPort,
       "switchEthernetPort": switchEthernetPort,
       "switchWaveBusPort": switchWaveBusPort,
       "switchFddiPort": switchFddiPort,
       "switchSoftware": switchSoftware,
       "switchInfo": switchInfo,
       "switchBasicTable": switchBasicTable,
       "switchBasicEntry": switchBasicEntry,
       "switchProductCode": switchProductCode,
       "switchSerialNumber": switchSerialNumber,
       "switchPlaceOfManufacture": switchPlaceOfManufacture,
       "switchDateOfManufacture": switchDateOfManufacture,
       "switchMacAddress": switchMacAddress,
       "switchCodeVersion": switchCodeVersion,
       "switchBpeEnabled": switchBpeEnabled,
       "eraseSwitchSnmpConfigInfo": eraseSwitchSnmpConfigInfo,
       "restoreSwitchDot1dDefaults": restoreSwitchDot1dDefaults,
       "performSwitchReset": performSwitchReset,
       "switchIdentPressed": switchIdentPressed,
       "ageFilterDatabase": ageFilterDatabase,
       "clearStatistics": clearStatistics,
       "switchBasicIndex": switchBasicIndex,
       "switchPortTable": switchPortTable,
       "switchPortEntry": switchPortEntry,
       "switchPortIndex": switchPortIndex,
       "switchPortProductCode": switchPortProductCode,
       "switchPortSerialNumber": switchPortSerialNumber,
       "switchPortPlaceOfManufacture": switchPortPlaceOfManufacture,
       "switchPortDateOfManufacture": switchPortDateOfManufacture,
       "switchPortState": switchPortState,
       "switchPortHighSensitivity": switchPortHighSensitivity,
       "restoreFddiMibDefaults": restoreFddiMibDefaults,
       "translateAllEthertypes": translateAllEthertypes,
       "switchPortTxFrames": switchPortTxFrames,
       "switchPortRxFrames": switchPortRxFrames,
       "switchPortFcsErrors": switchPortFcsErrors,
       "switchPortFilterDiscards": switchPortFilterDiscards,
       "switchPortDelayExceededDiscards": switchPortDelayExceededDiscards,
       "switchPortMtuExceededDiscards": switchPortMtuExceededDiscards,
       "switchSelectiveTranslationTable": switchSelectiveTranslationTable,
       "translationTableEntry": translationTableEntry,
       "translationTablePortIndex": translationTablePortIndex,
       "translationTableEthertype1": translationTableEthertype1,
       "translationTableEntryValid1": translationTableEntryValid1,
       "translationTableEthertype2": translationTableEthertype2,
       "translationTableEntryValid2": translationTableEntryValid2,
       "translationTableEthertype3": translationTableEthertype3,
       "translationTableEntryValid3": translationTableEntryValid3}
)
