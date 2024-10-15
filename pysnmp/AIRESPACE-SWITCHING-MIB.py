# SNMP MIB module (AIRESPACE-SWITCHING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIRESPACE-SWITCHING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:15 2024
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

(airespace,) = mibBuilder.importSymbols(
    "AIRESPACE-REF-MIB",
    "airespace")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(dot1qFdbId,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qFdbId",
    "dot1qVlanIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bsnSwitching = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1)
)
bsnSwitching.setRevisions(
        ("2006-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentInfoGroup_ObjectIdentity = ObjectIdentity
agentInfoGroup = _AgentInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1)
)
_AgentInventoryGroup_ObjectIdentity = ObjectIdentity
agentInventoryGroup = _AgentInventoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1)
)
_AgentInventorySysDescription_Type = DisplayString
_AgentInventorySysDescription_Object = MibScalar
agentInventorySysDescription = _AgentInventorySysDescription_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 1),
    _AgentInventorySysDescription_Type()
)
agentInventorySysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySysDescription.setStatus("current")
_AgentInventoryMachineType_Type = DisplayString
_AgentInventoryMachineType_Object = MibScalar
agentInventoryMachineType = _AgentInventoryMachineType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 2),
    _AgentInventoryMachineType_Type()
)
agentInventoryMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMachineType.setStatus("current")
_AgentInventoryMachineModel_Type = DisplayString
_AgentInventoryMachineModel_Object = MibScalar
agentInventoryMachineModel = _AgentInventoryMachineModel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 3),
    _AgentInventoryMachineModel_Type()
)
agentInventoryMachineModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMachineModel.setStatus("current")
_AgentInventorySerialNumber_Type = DisplayString
_AgentInventorySerialNumber_Object = MibScalar
agentInventorySerialNumber = _AgentInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 4),
    _AgentInventorySerialNumber_Type()
)
agentInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventorySerialNumber.setStatus("current")
_AgentInventoryMaintenanceLevel_Type = DisplayString
_AgentInventoryMaintenanceLevel_Object = MibScalar
agentInventoryMaintenanceLevel = _AgentInventoryMaintenanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 6),
    _AgentInventoryMaintenanceLevel_Type()
)
agentInventoryMaintenanceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMaintenanceLevel.setStatus("current")
_AgentInventoryBurnedInMacAddress_Type = PhysAddress
_AgentInventoryBurnedInMacAddress_Object = MibScalar
agentInventoryBurnedInMacAddress = _AgentInventoryBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 9),
    _AgentInventoryBurnedInMacAddress_Type()
)
agentInventoryBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryBurnedInMacAddress.setStatus("current")
_AgentInventoryOperatingSystem_Type = DisplayString
_AgentInventoryOperatingSystem_Object = MibScalar
agentInventoryOperatingSystem = _AgentInventoryOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 10),
    _AgentInventoryOperatingSystem_Type()
)
agentInventoryOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryOperatingSystem.setStatus("current")
_AgentInventoryManufacturerName_Type = DisplayString
_AgentInventoryManufacturerName_Object = MibScalar
agentInventoryManufacturerName = _AgentInventoryManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 12),
    _AgentInventoryManufacturerName_Type()
)
agentInventoryManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryManufacturerName.setStatus("current")
_AgentInventoryProductName_Type = DisplayString
_AgentInventoryProductName_Object = MibScalar
agentInventoryProductName = _AgentInventoryProductName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 13),
    _AgentInventoryProductName_Type()
)
agentInventoryProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryProductName.setStatus("current")
_AgentInventoryProductVersion_Type = DisplayString
_AgentInventoryProductVersion_Object = MibScalar
agentInventoryProductVersion = _AgentInventoryProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 14),
    _AgentInventoryProductVersion_Type()
)
agentInventoryProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryProductVersion.setStatus("current")
_AgentInventoryIsGigECardPresent_Type = TruthValue
_AgentInventoryIsGigECardPresent_Object = MibScalar
agentInventoryIsGigECardPresent = _AgentInventoryIsGigECardPresent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 15),
    _AgentInventoryIsGigECardPresent_Type()
)
agentInventoryIsGigECardPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryIsGigECardPresent.setStatus("current")
_AgentInventoryIsCryptoCardPresent_Type = TruthValue
_AgentInventoryIsCryptoCardPresent_Object = MibScalar
agentInventoryIsCryptoCardPresent = _AgentInventoryIsCryptoCardPresent_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 16),
    _AgentInventoryIsCryptoCardPresent_Type()
)
agentInventoryIsCryptoCardPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryIsCryptoCardPresent.setStatus("current")
_AgentInventoryIsForeignAPSupported_Type = TruthValue
_AgentInventoryIsForeignAPSupported_Object = MibScalar
agentInventoryIsForeignAPSupported = _AgentInventoryIsForeignAPSupported_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 17),
    _AgentInventoryIsForeignAPSupported_Type()
)
agentInventoryIsForeignAPSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryIsForeignAPSupported.setStatus("current")
_AgentInventoryMaxNumberOfAPsSupported_Type = Integer32
_AgentInventoryMaxNumberOfAPsSupported_Object = MibScalar
agentInventoryMaxNumberOfAPsSupported = _AgentInventoryMaxNumberOfAPsSupported_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 18),
    _AgentInventoryMaxNumberOfAPsSupported_Type()
)
agentInventoryMaxNumberOfAPsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryMaxNumberOfAPsSupported.setStatus("current")
_AgentInventoryIsCryptoCard2Present_Type = TruthValue
_AgentInventoryIsCryptoCard2Present_Object = MibScalar
agentInventoryIsCryptoCard2Present = _AgentInventoryIsCryptoCard2Present_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 19),
    _AgentInventoryIsCryptoCard2Present_Type()
)
agentInventoryIsCryptoCard2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryIsCryptoCard2Present.setStatus("current")


class _AgentInventoryFipsModeEnabled_Type(TruthValue):
    """Custom type agentInventoryFipsModeEnabled based on TruthValue"""


_AgentInventoryFipsModeEnabled_Object = MibScalar
agentInventoryFipsModeEnabled = _AgentInventoryFipsModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 1, 20),
    _AgentInventoryFipsModeEnabled_Type()
)
agentInventoryFipsModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryFipsModeEnabled.setStatus("current")
_AgentTrapLogGroup_ObjectIdentity = ObjectIdentity
agentTrapLogGroup = _AgentTrapLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2)
)
_AgentTrapLogTotal_Type = Integer32
_AgentTrapLogTotal_Object = MibScalar
agentTrapLogTotal = _AgentTrapLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 1),
    _AgentTrapLogTotal_Type()
)
agentTrapLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTotal.setStatus("current")
_AgentTrapLogTotalSinceLastViewed_Type = Integer32
_AgentTrapLogTotalSinceLastViewed_Object = MibScalar
agentTrapLogTotalSinceLastViewed = _AgentTrapLogTotalSinceLastViewed_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 3),
    _AgentTrapLogTotalSinceLastViewed_Type()
)
agentTrapLogTotalSinceLastViewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTotalSinceLastViewed.setStatus("current")
_AgentTrapLogTable_Object = MibTable
agentTrapLogTable = _AgentTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    agentTrapLogTable.setStatus("current")
_AgentTrapLogEntry_Object = MibTableRow
agentTrapLogEntry = _AgentTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 4, 1)
)
agentTrapLogEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentTrapLogIndex"),
)
if mibBuilder.loadTexts:
    agentTrapLogEntry.setStatus("current")
_AgentTrapLogIndex_Type = Integer32
_AgentTrapLogIndex_Object = MibTableColumn
agentTrapLogIndex = _AgentTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 4, 1, 1),
    _AgentTrapLogIndex_Type()
)
agentTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogIndex.setStatus("current")
_AgentTrapLogSystemTime_Type = DisplayString
_AgentTrapLogSystemTime_Object = MibTableColumn
agentTrapLogSystemTime = _AgentTrapLogSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 4, 1, 2),
    _AgentTrapLogSystemTime_Type()
)
agentTrapLogSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogSystemTime.setStatus("current")


class _AgentTrapLogTrap_Type(OctetString):
    """Custom type agentTrapLogTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AgentTrapLogTrap_Type.__name__ = "OctetString"
_AgentTrapLogTrap_Object = MibTableColumn
agentTrapLogTrap = _AgentTrapLogTrap_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 4, 1, 22),
    _AgentTrapLogTrap_Type()
)
agentTrapLogTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrapLogTrap.setStatus("current")
_AgentRadioUpDownTrapCount_Type = Integer32
_AgentRadioUpDownTrapCount_Object = MibScalar
agentRadioUpDownTrapCount = _AgentRadioUpDownTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 5),
    _AgentRadioUpDownTrapCount_Type()
)
agentRadioUpDownTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadioUpDownTrapCount.setStatus("current")
_AgentApAssociateDisassociateTrapCount_Type = Integer32
_AgentApAssociateDisassociateTrapCount_Object = MibScalar
agentApAssociateDisassociateTrapCount = _AgentApAssociateDisassociateTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 6),
    _AgentApAssociateDisassociateTrapCount_Type()
)
agentApAssociateDisassociateTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentApAssociateDisassociateTrapCount.setStatus("current")
_AgentApLoadProfileFailTrapCount_Type = Integer32
_AgentApLoadProfileFailTrapCount_Object = MibScalar
agentApLoadProfileFailTrapCount = _AgentApLoadProfileFailTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 7),
    _AgentApLoadProfileFailTrapCount_Type()
)
agentApLoadProfileFailTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentApLoadProfileFailTrapCount.setStatus("current")
_AgentApNoiseProfileFailTrapCount_Type = Integer32
_AgentApNoiseProfileFailTrapCount_Object = MibScalar
agentApNoiseProfileFailTrapCount = _AgentApNoiseProfileFailTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 8),
    _AgentApNoiseProfileFailTrapCount_Type()
)
agentApNoiseProfileFailTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentApNoiseProfileFailTrapCount.setStatus("current")
_AgentApInterferenceProfileFailTrapCount_Type = Integer32
_AgentApInterferenceProfileFailTrapCount_Object = MibScalar
agentApInterferenceProfileFailTrapCount = _AgentApInterferenceProfileFailTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 9),
    _AgentApInterferenceProfileFailTrapCount_Type()
)
agentApInterferenceProfileFailTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentApInterferenceProfileFailTrapCount.setStatus("current")
_AgentApCoverageProfileFailTrapCount_Type = Integer32
_AgentApCoverageProfileFailTrapCount_Object = MibScalar
agentApCoverageProfileFailTrapCount = _AgentApCoverageProfileFailTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 2, 10),
    _AgentApCoverageProfileFailTrapCount_Type()
)
agentApCoverageProfileFailTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentApCoverageProfileFailTrapCount.setStatus("current")
_AgentSwitchInfoGroup_ObjectIdentity = ObjectIdentity
agentSwitchInfoGroup = _AgentSwitchInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 3)
)


class _AgentSwitchInfoLwappTransportMode_Type(Integer32):
    """Custom type agentSwitchInfoLwappTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )


_AgentSwitchInfoLwappTransportMode_Type.__name__ = "Integer32"
_AgentSwitchInfoLwappTransportMode_Object = MibScalar
agentSwitchInfoLwappTransportMode = _AgentSwitchInfoLwappTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 3, 1),
    _AgentSwitchInfoLwappTransportMode_Type()
)
agentSwitchInfoLwappTransportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchInfoLwappTransportMode.setStatus("current")


class _AgentSwitchInfoPowerSupply1Present_Type(Integer32):
    """Custom type agentSwitchInfoPowerSupply1Present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentSwitchInfoPowerSupply1Present_Type.__name__ = "Integer32"
_AgentSwitchInfoPowerSupply1Present_Object = MibScalar
agentSwitchInfoPowerSupply1Present = _AgentSwitchInfoPowerSupply1Present_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 3, 2),
    _AgentSwitchInfoPowerSupply1Present_Type()
)
agentSwitchInfoPowerSupply1Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchInfoPowerSupply1Present.setStatus("current")


class _AgentSwitchInfoPowerSupply1Operational_Type(Integer32):
    """Custom type agentSwitchInfoPowerSupply1Operational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentSwitchInfoPowerSupply1Operational_Type.__name__ = "Integer32"
_AgentSwitchInfoPowerSupply1Operational_Object = MibScalar
agentSwitchInfoPowerSupply1Operational = _AgentSwitchInfoPowerSupply1Operational_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 3, 3),
    _AgentSwitchInfoPowerSupply1Operational_Type()
)
agentSwitchInfoPowerSupply1Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchInfoPowerSupply1Operational.setStatus("current")


class _AgentSwitchInfoPowerSupply2Present_Type(Integer32):
    """Custom type agentSwitchInfoPowerSupply2Present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentSwitchInfoPowerSupply2Present_Type.__name__ = "Integer32"
_AgentSwitchInfoPowerSupply2Present_Object = MibScalar
agentSwitchInfoPowerSupply2Present = _AgentSwitchInfoPowerSupply2Present_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 3, 4),
    _AgentSwitchInfoPowerSupply2Present_Type()
)
agentSwitchInfoPowerSupply2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchInfoPowerSupply2Present.setStatus("current")


class _AgentSwitchInfoPowerSupply2Operational_Type(Integer32):
    """Custom type agentSwitchInfoPowerSupply2Operational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AgentSwitchInfoPowerSupply2Operational_Type.__name__ = "Integer32"
_AgentSwitchInfoPowerSupply2Operational_Object = MibScalar
agentSwitchInfoPowerSupply2Operational = _AgentSwitchInfoPowerSupply2Operational_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 3, 5),
    _AgentSwitchInfoPowerSupply2Operational_Type()
)
agentSwitchInfoPowerSupply2Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchInfoPowerSupply2Operational.setStatus("current")
_AgentProductGroup_ObjectIdentity = ObjectIdentity
agentProductGroup = _AgentProductGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 4)
)
_ProductGroup1_ObjectIdentity = ObjectIdentity
productGroup1 = _ProductGroup1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 4, 1)
)
_ProductGroup2_ObjectIdentity = ObjectIdentity
productGroup2 = _ProductGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 4, 2)
)
_ProductGroup3_ObjectIdentity = ObjectIdentity
productGroup3 = _ProductGroup3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 4, 3)
)
_ProductGroup4_ObjectIdentity = ObjectIdentity
productGroup4 = _ProductGroup4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 4, 4)
)
_AgentResourceInfoGroup_ObjectIdentity = ObjectIdentity
agentResourceInfoGroup = _AgentResourceInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 5)
)


class _AgentCurrentCPUUtilization_Type(Integer32):
    """Custom type agentCurrentCPUUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentCurrentCPUUtilization_Type.__name__ = "Integer32"
_AgentCurrentCPUUtilization_Object = MibScalar
agentCurrentCPUUtilization = _AgentCurrentCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 5, 1),
    _AgentCurrentCPUUtilization_Type()
)
agentCurrentCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCurrentCPUUtilization.setStatus("current")
_AgentTotalMemory_Type = Integer32
_AgentTotalMemory_Object = MibScalar
agentTotalMemory = _AgentTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 5, 2),
    _AgentTotalMemory_Type()
)
agentTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTotalMemory.setStatus("current")
_AgentFreeMemory_Type = Integer32
_AgentFreeMemory_Object = MibScalar
agentFreeMemory = _AgentFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 5, 3),
    _AgentFreeMemory_Type()
)
agentFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFreeMemory.setStatus("current")
_AgentWcpInfoGroup_ObjectIdentity = ObjectIdentity
agentWcpInfoGroup = _AgentWcpInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6)
)


class _AgentWcpDeviceName_Type(DisplayString):
    """Custom type agentWcpDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentWcpDeviceName_Type.__name__ = "DisplayString"
_AgentWcpDeviceName_Object = MibScalar
agentWcpDeviceName = _AgentWcpDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 1),
    _AgentWcpDeviceName_Type()
)
agentWcpDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpDeviceName.setStatus("current")


class _AgentWcpSlotNumber_Type(Unsigned32):
    """Custom type agentWcpSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AgentWcpSlotNumber_Type.__name__ = "Unsigned32"
_AgentWcpSlotNumber_Object = MibScalar
agentWcpSlotNumber = _AgentWcpSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 2),
    _AgentWcpSlotNumber_Type()
)
agentWcpSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpSlotNumber.setStatus("current")


class _AgentWcpPortNumber_Type(Unsigned32):
    """Custom type agentWcpPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AgentWcpPortNumber_Type.__name__ = "Unsigned32"
_AgentWcpPortNumber_Object = MibScalar
agentWcpPortNumber = _AgentWcpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 3),
    _AgentWcpPortNumber_Type()
)
agentWcpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpPortNumber.setStatus("current")


class _AgentWcpPeerPortNumber_Type(Unsigned32):
    """Custom type agentWcpPeerPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AgentWcpPeerPortNumber_Type.__name__ = "Unsigned32"
_AgentWcpPeerPortNumber_Object = MibScalar
agentWcpPeerPortNumber = _AgentWcpPeerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 4),
    _AgentWcpPeerPortNumber_Type()
)
agentWcpPeerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpPeerPortNumber.setStatus("current")
_AgentWcpPeerIpAddress_Type = IpAddress
_AgentWcpPeerIpAddress_Object = MibScalar
agentWcpPeerIpAddress = _AgentWcpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 5),
    _AgentWcpPeerIpAddress_Type()
)
agentWcpPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpPeerIpAddress.setStatus("current")
_AgentWcpControllerTableChecksum_Type = Integer32
_AgentWcpControllerTableChecksum_Object = MibScalar
agentWcpControllerTableChecksum = _AgentWcpControllerTableChecksum_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 6),
    _AgentWcpControllerTableChecksum_Type()
)
agentWcpControllerTableChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpControllerTableChecksum.setStatus("current")
_AgentWcpControllerInfoTable_Object = MibTable
agentWcpControllerInfoTable = _AgentWcpControllerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    agentWcpControllerInfoTable.setStatus("current")
_AgentWcpControllerInfoEntry_Object = MibTableRow
agentWcpControllerInfoEntry = _AgentWcpControllerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 7, 1)
)
agentWcpControllerInfoEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentWcpControllerInfoSlotNumber"),
    (0, "AIRESPACE-SWITCHING-MIB", "agentWcpControllerInfoPortNumber"),
)
if mibBuilder.loadTexts:
    agentWcpControllerInfoEntry.setStatus("current")


class _AgentWcpControllerInfoSlotNumber_Type(Unsigned32):
    """Custom type agentWcpControllerInfoSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AgentWcpControllerInfoSlotNumber_Type.__name__ = "Unsigned32"
_AgentWcpControllerInfoSlotNumber_Object = MibTableColumn
agentWcpControllerInfoSlotNumber = _AgentWcpControllerInfoSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 7, 1, 1),
    _AgentWcpControllerInfoSlotNumber_Type()
)
agentWcpControllerInfoSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpControllerInfoSlotNumber.setStatus("current")


class _AgentWcpControllerInfoPortNumber_Type(Unsigned32):
    """Custom type agentWcpControllerInfoPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AgentWcpControllerInfoPortNumber_Type.__name__ = "Unsigned32"
_AgentWcpControllerInfoPortNumber_Object = MibTableColumn
agentWcpControllerInfoPortNumber = _AgentWcpControllerInfoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 7, 1, 2),
    _AgentWcpControllerInfoPortNumber_Type()
)
agentWcpControllerInfoPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpControllerInfoPortNumber.setStatus("current")
_AgentWcpControllerInfoIpAddress_Type = IpAddress
_AgentWcpControllerInfoIpAddress_Object = MibTableColumn
agentWcpControllerInfoIpAddress = _AgentWcpControllerInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 1, 6, 7, 1, 10),
    _AgentWcpControllerInfoIpAddress_Type()
)
agentWcpControllerInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentWcpControllerInfoIpAddress.setStatus("current")
_AgentConfigGroup_ObjectIdentity = ObjectIdentity
agentConfigGroup = _AgentConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2)
)
_AgentCLIConfigGroup_ObjectIdentity = ObjectIdentity
agentCLIConfigGroup = _AgentCLIConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1)
)
_AgentLoginSessionTable_Object = MibTable
agentLoginSessionTable = _AgentLoginSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    agentLoginSessionTable.setStatus("current")
_AgentLoginSessionEntry_Object = MibTableRow
agentLoginSessionEntry = _AgentLoginSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1)
)
agentLoginSessionEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentLoginSessionIndex"),
)
if mibBuilder.loadTexts:
    agentLoginSessionEntry.setStatus("current")
_AgentLoginSessionIndex_Type = Integer32
_AgentLoginSessionIndex_Object = MibTableColumn
agentLoginSessionIndex = _AgentLoginSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1, 1),
    _AgentLoginSessionIndex_Type()
)
agentLoginSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIndex.setStatus("current")
_AgentLoginSessionUserName_Type = DisplayString
_AgentLoginSessionUserName_Object = MibTableColumn
agentLoginSessionUserName = _AgentLoginSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1, 2),
    _AgentLoginSessionUserName_Type()
)
agentLoginSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionUserName.setStatus("current")
_AgentLoginSessionIPAddress_Type = IpAddress
_AgentLoginSessionIPAddress_Object = MibTableColumn
agentLoginSessionIPAddress = _AgentLoginSessionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1, 3),
    _AgentLoginSessionIPAddress_Type()
)
agentLoginSessionIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIPAddress.setStatus("current")


class _AgentLoginSessionConnectionType_Type(Integer32):
    """Custom type agentLoginSessionConnectionType based on Integer32"""
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
        *(("serial", 1),
          ("ssl", 4),
          ("telnet", 2),
          ("web", 3))
    )


_AgentLoginSessionConnectionType_Type.__name__ = "Integer32"
_AgentLoginSessionConnectionType_Object = MibTableColumn
agentLoginSessionConnectionType = _AgentLoginSessionConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1, 4),
    _AgentLoginSessionConnectionType_Type()
)
agentLoginSessionConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionConnectionType.setStatus("current")
_AgentLoginSessionIdleTime_Type = TimeTicks
_AgentLoginSessionIdleTime_Object = MibTableColumn
agentLoginSessionIdleTime = _AgentLoginSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1, 5),
    _AgentLoginSessionIdleTime_Type()
)
agentLoginSessionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionIdleTime.setStatus("current")
_AgentLoginSessionSessionTime_Type = TimeTicks
_AgentLoginSessionSessionTime_Object = MibTableColumn
agentLoginSessionSessionTime = _AgentLoginSessionSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1, 6),
    _AgentLoginSessionSessionTime_Type()
)
agentLoginSessionSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLoginSessionSessionTime.setStatus("current")
_AgentLoginSessionStatus_Type = RowStatus
_AgentLoginSessionStatus_Object = MibTableColumn
agentLoginSessionStatus = _AgentLoginSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 1, 1, 26),
    _AgentLoginSessionStatus_Type()
)
agentLoginSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLoginSessionStatus.setStatus("current")
_AgentTelnetConfigGroup_ObjectIdentity = ObjectIdentity
agentTelnetConfigGroup = _AgentTelnetConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 2)
)


class _AgentTelnetLoginTimeout_Type(Integer32):
    """Custom type agentTelnetLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_AgentTelnetLoginTimeout_Type.__name__ = "Integer32"
_AgentTelnetLoginTimeout_Object = MibScalar
agentTelnetLoginTimeout = _AgentTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 2, 1),
    _AgentTelnetLoginTimeout_Type()
)
agentTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetLoginTimeout.setStatus("current")


class _AgentTelnetMaxSessions_Type(Integer32):
    """Custom type agentTelnetMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentTelnetMaxSessions_Type.__name__ = "Integer32"
_AgentTelnetMaxSessions_Object = MibScalar
agentTelnetMaxSessions = _AgentTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 2, 2),
    _AgentTelnetMaxSessions_Type()
)
agentTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetMaxSessions.setStatus("current")


class _AgentTelnetAllowNewMode_Type(Integer32):
    """Custom type agentTelnetAllowNewMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentTelnetAllowNewMode_Type.__name__ = "Integer32"
_AgentTelnetAllowNewMode_Object = MibScalar
agentTelnetAllowNewMode = _AgentTelnetAllowNewMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 2, 3),
    _AgentTelnetAllowNewMode_Type()
)
agentTelnetAllowNewMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTelnetAllowNewMode.setStatus("current")


class _AgentSSHAllowNewMode_Type(Integer32):
    """Custom type agentSSHAllowNewMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSSHAllowNewMode_Type.__name__ = "Integer32"
_AgentSSHAllowNewMode_Object = MibScalar
agentSSHAllowNewMode = _AgentSSHAllowNewMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 2, 4),
    _AgentSSHAllowNewMode_Type()
)
agentSSHAllowNewMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHAllowNewMode.setStatus("current")
_AgentSerialGroup_ObjectIdentity = ObjectIdentity
agentSerialGroup = _AgentSerialGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 5)
)
_AgentSerialTimeout_Type = Integer32
_AgentSerialTimeout_Object = MibScalar
agentSerialTimeout = _AgentSerialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 5, 1),
    _AgentSerialTimeout_Type()
)
agentSerialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialTimeout.setStatus("current")


class _AgentSerialBaudrate_Type(Integer32):
    """Custom type agentSerialBaudrate based on Integer32"""
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
        *(("baud115200", 8),
          ("baud1200", 1),
          ("baud19200", 5),
          ("baud2400", 2),
          ("baud38400", 6),
          ("baud4800", 3),
          ("baud57600", 7),
          ("baud9600", 4))
    )


_AgentSerialBaudrate_Type.__name__ = "Integer32"
_AgentSerialBaudrate_Object = MibScalar
agentSerialBaudrate = _AgentSerialBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 5, 2),
    _AgentSerialBaudrate_Type()
)
agentSerialBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialBaudrate.setStatus("current")
_AgentSerialCharacterSize_Type = Integer32
_AgentSerialCharacterSize_Object = MibScalar
agentSerialCharacterSize = _AgentSerialCharacterSize_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 5, 3),
    _AgentSerialCharacterSize_Type()
)
agentSerialCharacterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialCharacterSize.setStatus("current")


class _AgentSerialHWFlowControlMode_Type(Integer32):
    """Custom type agentSerialHWFlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSerialHWFlowControlMode_Type.__name__ = "Integer32"
_AgentSerialHWFlowControlMode_Object = MibScalar
agentSerialHWFlowControlMode = _AgentSerialHWFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 5, 4),
    _AgentSerialHWFlowControlMode_Type()
)
agentSerialHWFlowControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialHWFlowControlMode.setStatus("current")
_AgentSerialStopBits_Type = Integer32
_AgentSerialStopBits_Object = MibScalar
agentSerialStopBits = _AgentSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 5, 5),
    _AgentSerialStopBits_Type()
)
agentSerialStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialStopBits.setStatus("current")


class _AgentSerialParityType_Type(Integer32):
    """Custom type agentSerialParityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("none", 3),
          ("odd", 2))
    )


_AgentSerialParityType_Type.__name__ = "Integer32"
_AgentSerialParityType_Object = MibScalar
agentSerialParityType = _AgentSerialParityType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 1, 5, 6),
    _AgentSerialParityType_Type()
)
agentSerialParityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialParityType.setStatus("current")
_AgentLagConfigGroup_ObjectIdentity = ObjectIdentity
agentLagConfigGroup = _AgentLagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2)
)


class _AgentLagConfigCreate_Type(DisplayString):
    """Custom type agentLagConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentLagConfigCreate_Type.__name__ = "DisplayString"
_AgentLagConfigCreate_Object = MibScalar
agentLagConfigCreate = _AgentLagConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 1),
    _AgentLagConfigCreate_Type()
)
agentLagConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagConfigCreate.setStatus("obsolete")
_AgentLagSummaryConfigTable_Object = MibTable
agentLagSummaryConfigTable = _AgentLagSummaryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    agentLagSummaryConfigTable.setStatus("obsolete")
_AgentLagSummaryConfigEntry_Object = MibTableRow
agentLagSummaryConfigEntry = _AgentLagSummaryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1)
)
agentLagSummaryConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentLagSummaryName"),
)
if mibBuilder.loadTexts:
    agentLagSummaryConfigEntry.setStatus("obsolete")


class _AgentLagSummaryName_Type(DisplayString):
    """Custom type agentLagSummaryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentLagSummaryName_Type.__name__ = "DisplayString"
_AgentLagSummaryName_Object = MibTableColumn
agentLagSummaryName = _AgentLagSummaryName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 1),
    _AgentLagSummaryName_Type()
)
agentLagSummaryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryName.setStatus("obsolete")
_AgentLagSummaryLagIndex_Type = Integer32
_AgentLagSummaryLagIndex_Object = MibTableColumn
agentLagSummaryLagIndex = _AgentLagSummaryLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 2),
    _AgentLagSummaryLagIndex_Type()
)
agentLagSummaryLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagSummaryLagIndex.setStatus("obsolete")
_AgentLagSummaryFlushTimer_Type = Integer32
_AgentLagSummaryFlushTimer_Object = MibTableColumn
agentLagSummaryFlushTimer = _AgentLagSummaryFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 3),
    _AgentLagSummaryFlushTimer_Type()
)
agentLagSummaryFlushTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryFlushTimer.setStatus("obsolete")


class _AgentLagSummaryLinkTrap_Type(Integer32):
    """Custom type agentLagSummaryLinkTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagSummaryLinkTrap_Type.__name__ = "Integer32"
_AgentLagSummaryLinkTrap_Object = MibTableColumn
agentLagSummaryLinkTrap = _AgentLagSummaryLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 4),
    _AgentLagSummaryLinkTrap_Type()
)
agentLagSummaryLinkTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryLinkTrap.setStatus("obsolete")


class _AgentLagSummaryAdminMode_Type(Integer32):
    """Custom type agentLagSummaryAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentLagSummaryAdminMode_Type.__name__ = "Integer32"
_AgentLagSummaryAdminMode_Object = MibTableColumn
agentLagSummaryAdminMode = _AgentLagSummaryAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 5),
    _AgentLagSummaryAdminMode_Type()
)
agentLagSummaryAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryAdminMode.setStatus("obsolete")


class _AgentLagSummaryStpMode_Type(Integer32):
    """Custom type agentLagSummaryStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("fast", 2),
          ("off", 3))
    )


_AgentLagSummaryStpMode_Type.__name__ = "Integer32"
_AgentLagSummaryStpMode_Object = MibTableColumn
agentLagSummaryStpMode = _AgentLagSummaryStpMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 6),
    _AgentLagSummaryStpMode_Type()
)
agentLagSummaryStpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryStpMode.setStatus("obsolete")
_AgentLagSummaryAddPort_Type = Integer32
_AgentLagSummaryAddPort_Object = MibTableColumn
agentLagSummaryAddPort = _AgentLagSummaryAddPort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 7),
    _AgentLagSummaryAddPort_Type()
)
agentLagSummaryAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryAddPort.setStatus("obsolete")
_AgentLagSummaryDeletePort_Type = Integer32
_AgentLagSummaryDeletePort_Object = MibTableColumn
agentLagSummaryDeletePort = _AgentLagSummaryDeletePort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 8),
    _AgentLagSummaryDeletePort_Type()
)
agentLagSummaryDeletePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryDeletePort.setStatus("obsolete")
_AgentLagSummaryPortsBitMask_Type = Unsigned32
_AgentLagSummaryPortsBitMask_Object = MibTableColumn
agentLagSummaryPortsBitMask = _AgentLagSummaryPortsBitMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 9),
    _AgentLagSummaryPortsBitMask_Type()
)
agentLagSummaryPortsBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryPortsBitMask.setStatus("obsolete")
_AgentLagSummaryStatus_Type = RowStatus
_AgentLagSummaryStatus_Object = MibTableColumn
agentLagSummaryStatus = _AgentLagSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 2, 1, 30),
    _AgentLagSummaryStatus_Type()
)
agentLagSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLagSummaryStatus.setStatus("obsolete")
_AgentLagDetailedConfigTable_Object = MibTable
agentLagDetailedConfigTable = _AgentLagDetailedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    agentLagDetailedConfigTable.setStatus("obsolete")
_AgentLagDetailedConfigEntry_Object = MibTableRow
agentLagDetailedConfigEntry = _AgentLagDetailedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 3, 1)
)
agentLagDetailedConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentLagDetailedLagIndex"),
    (0, "AIRESPACE-SWITCHING-MIB", "agentLagDetailedIfIndex"),
)
if mibBuilder.loadTexts:
    agentLagDetailedConfigEntry.setStatus("obsolete")
_AgentLagDetailedLagIndex_Type = Integer32
_AgentLagDetailedLagIndex_Object = MibTableColumn
agentLagDetailedLagIndex = _AgentLagDetailedLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 3, 1, 1),
    _AgentLagDetailedLagIndex_Type()
)
agentLagDetailedLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedLagIndex.setStatus("obsolete")
_AgentLagDetailedIfIndex_Type = Integer32
_AgentLagDetailedIfIndex_Object = MibTableColumn
agentLagDetailedIfIndex = _AgentLagDetailedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 3, 1, 2),
    _AgentLagDetailedIfIndex_Type()
)
agentLagDetailedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedIfIndex.setStatus("obsolete")
_AgentLagDetailedPortSpeed_Type = ObjectIdentifier
_AgentLagDetailedPortSpeed_Object = MibTableColumn
agentLagDetailedPortSpeed = _AgentLagDetailedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 3, 1, 22),
    _AgentLagDetailedPortSpeed_Type()
)
agentLagDetailedPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLagDetailedPortSpeed.setStatus("obsolete")


class _AgentLagConfigMode_Type(Integer32):
    """Custom type agentLagConfigMode based on Integer32"""
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


_AgentLagConfigMode_Type.__name__ = "Integer32"
_AgentLagConfigMode_Object = MibScalar
agentLagConfigMode = _AgentLagConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 2, 4),
    _AgentLagConfigMode_Type()
)
agentLagConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLagConfigMode.setStatus("obsolete")
_AgentNetworkConfigGroup_ObjectIdentity = ObjectIdentity
agentNetworkConfigGroup = _AgentNetworkConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3)
)
_AgentNetworkIPAddress_Type = IpAddress
_AgentNetworkIPAddress_Object = MibScalar
agentNetworkIPAddress = _AgentNetworkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 1),
    _AgentNetworkIPAddress_Type()
)
agentNetworkIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkIPAddress.setStatus("current")
_AgentNetworkSubnetMask_Type = IpAddress
_AgentNetworkSubnetMask_Object = MibScalar
agentNetworkSubnetMask = _AgentNetworkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 2),
    _AgentNetworkSubnetMask_Type()
)
agentNetworkSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkSubnetMask.setStatus("current")
_AgentNetworkDefaultGateway_Type = IpAddress
_AgentNetworkDefaultGateway_Object = MibScalar
agentNetworkDefaultGateway = _AgentNetworkDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 3),
    _AgentNetworkDefaultGateway_Type()
)
agentNetworkDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDefaultGateway.setStatus("current")
_AgentNetworkBurnedInMacAddress_Type = PhysAddress
_AgentNetworkBurnedInMacAddress_Object = MibScalar
agentNetworkBurnedInMacAddress = _AgentNetworkBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 4),
    _AgentNetworkBurnedInMacAddress_Type()
)
agentNetworkBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkBurnedInMacAddress.setStatus("current")


class _AgentNetworkConfigProtocol_Type(Integer32):
    """Custom type agentNetworkConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_AgentNetworkConfigProtocol_Type.__name__ = "Integer32"
_AgentNetworkConfigProtocol_Object = MibScalar
agentNetworkConfigProtocol = _AgentNetworkConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 7),
    _AgentNetworkConfigProtocol_Type()
)
agentNetworkConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkConfigProtocol.setStatus("current")


class _AgentNetworkWebMode_Type(Integer32):
    """Custom type agentNetworkWebMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentNetworkWebMode_Type.__name__ = "Integer32"
_AgentNetworkWebMode_Object = MibScalar
agentNetworkWebMode = _AgentNetworkWebMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 8),
    _AgentNetworkWebMode_Type()
)
agentNetworkWebMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkWebMode.setStatus("current")


class _AgentNetworkSecureWebMode_Type(Integer32):
    """Custom type agentNetworkSecureWebMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentNetworkSecureWebMode_Type.__name__ = "Integer32"
_AgentNetworkSecureWebMode_Object = MibScalar
agentNetworkSecureWebMode = _AgentNetworkSecureWebMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 9),
    _AgentNetworkSecureWebMode_Type()
)
agentNetworkSecureWebMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkSecureWebMode.setStatus("current")


class _AgentNetworkMulticastMode_Type(Integer32):
    """Custom type agentNetworkMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("multicast", 2),
          ("unicast", 1))
    )


_AgentNetworkMulticastMode_Type.__name__ = "Integer32"
_AgentNetworkMulticastMode_Object = MibScalar
agentNetworkMulticastMode = _AgentNetworkMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 10),
    _AgentNetworkMulticastMode_Type()
)
agentNetworkMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkMulticastMode.setStatus("current")
_AgentNetworkDsPortNumber_Type = Integer32
_AgentNetworkDsPortNumber_Object = MibScalar
agentNetworkDsPortNumber = _AgentNetworkDsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 11),
    _AgentNetworkDsPortNumber_Type()
)
agentNetworkDsPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDsPortNumber.setStatus("current")


class _AgentNetworkUserIdleTimeout_Type(Unsigned32):
    """Custom type agentNetworkUserIdleTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_AgentNetworkUserIdleTimeout_Type.__name__ = "Unsigned32"
_AgentNetworkUserIdleTimeout_Object = MibScalar
agentNetworkUserIdleTimeout = _AgentNetworkUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 12),
    _AgentNetworkUserIdleTimeout_Type()
)
agentNetworkUserIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkUserIdleTimeout.setStatus("current")


class _AgentNetworkArpTimeout_Type(Unsigned32):
    """Custom type agentNetworkArpTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_AgentNetworkArpTimeout_Type.__name__ = "Unsigned32"
_AgentNetworkArpTimeout_Object = MibScalar
agentNetworkArpTimeout = _AgentNetworkArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 13),
    _AgentNetworkArpTimeout_Type()
)
agentNetworkArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkArpTimeout.setStatus("current")


class _AgentNetworkManagementVlan_Type(Unsigned32):
    """Custom type agentNetworkManagementVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AgentNetworkManagementVlan_Type.__name__ = "Unsigned32"
_AgentNetworkManagementVlan_Object = MibScalar
agentNetworkManagementVlan = _AgentNetworkManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 14),
    _AgentNetworkManagementVlan_Type()
)
agentNetworkManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkManagementVlan.setStatus("current")


class _AgentNetworkGvrpStatus_Type(Integer32):
    """Custom type agentNetworkGvrpStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AgentNetworkGvrpStatus_Type.__name__ = "Integer32"
_AgentNetworkGvrpStatus_Object = MibScalar
agentNetworkGvrpStatus = _AgentNetworkGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 15),
    _AgentNetworkGvrpStatus_Type()
)
agentNetworkGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkGvrpStatus.setStatus("obsolete")


class _AgentNetworkAllowMgmtViaWireless_Type(Integer32):
    """Custom type agentNetworkAllowMgmtViaWireless based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentNetworkAllowMgmtViaWireless_Type.__name__ = "Integer32"
_AgentNetworkAllowMgmtViaWireless_Object = MibScalar
agentNetworkAllowMgmtViaWireless = _AgentNetworkAllowMgmtViaWireless_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 16),
    _AgentNetworkAllowMgmtViaWireless_Type()
)
agentNetworkAllowMgmtViaWireless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkAllowMgmtViaWireless.setStatus("current")


class _AgentNetworkBroadcastSsidMode_Type(Integer32):
    """Custom type agentNetworkBroadcastSsidMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentNetworkBroadcastSsidMode_Type.__name__ = "Integer32"
_AgentNetworkBroadcastSsidMode_Object = MibScalar
agentNetworkBroadcastSsidMode = _AgentNetworkBroadcastSsidMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 17),
    _AgentNetworkBroadcastSsidMode_Type()
)
agentNetworkBroadcastSsidMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkBroadcastSsidMode.setStatus("current")


class _AgentNetworkSecureWebPassword_Type(OctetString):
    """Custom type agentNetworkSecureWebPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentNetworkSecureWebPassword_Type.__name__ = "OctetString"
_AgentNetworkSecureWebPassword_Object = MibScalar
agentNetworkSecureWebPassword = _AgentNetworkSecureWebPassword_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 18),
    _AgentNetworkSecureWebPassword_Type()
)
agentNetworkSecureWebPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkSecureWebPassword.setStatus("current")


class _AgentNetworkWebAdminCertType_Type(DisplayString):
    """Custom type agentNetworkWebAdminCertType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AgentNetworkWebAdminCertType_Type.__name__ = "DisplayString"
_AgentNetworkWebAdminCertType_Object = MibScalar
agentNetworkWebAdminCertType = _AgentNetworkWebAdminCertType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 19),
    _AgentNetworkWebAdminCertType_Type()
)
agentNetworkWebAdminCertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkWebAdminCertType.setStatus("current")


class _AgentNetworkWebAdminCertRegenerateCmdInvoke_Type(Integer32):
    """Custom type agentNetworkWebAdminCertRegenerateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_AgentNetworkWebAdminCertRegenerateCmdInvoke_Type.__name__ = "Integer32"
_AgentNetworkWebAdminCertRegenerateCmdInvoke_Object = MibScalar
agentNetworkWebAdminCertRegenerateCmdInvoke = _AgentNetworkWebAdminCertRegenerateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 20),
    _AgentNetworkWebAdminCertRegenerateCmdInvoke_Type()
)
agentNetworkWebAdminCertRegenerateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkWebAdminCertRegenerateCmdInvoke.setStatus("current")


class _AgentNetworkWebAuthCertType_Type(DisplayString):
    """Custom type agentNetworkWebAuthCertType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AgentNetworkWebAuthCertType_Type.__name__ = "DisplayString"
_AgentNetworkWebAuthCertType_Object = MibScalar
agentNetworkWebAuthCertType = _AgentNetworkWebAuthCertType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 21),
    _AgentNetworkWebAuthCertType_Type()
)
agentNetworkWebAuthCertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetworkWebAuthCertType.setStatus("current")


class _AgentNetworkWebAuthCertRegenerateCmdInvoke_Type(Integer32):
    """Custom type agentNetworkWebAuthCertRegenerateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("default", 0))
    )


_AgentNetworkWebAuthCertRegenerateCmdInvoke_Type.__name__ = "Integer32"
_AgentNetworkWebAuthCertRegenerateCmdInvoke_Object = MibScalar
agentNetworkWebAuthCertRegenerateCmdInvoke = _AgentNetworkWebAuthCertRegenerateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 22),
    _AgentNetworkWebAuthCertRegenerateCmdInvoke_Type()
)
agentNetworkWebAuthCertRegenerateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkWebAuthCertRegenerateCmdInvoke.setStatus("current")
_AgentNetworkRouteConfigTable_Object = MibTable
agentNetworkRouteConfigTable = _AgentNetworkRouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 23)
)
if mibBuilder.loadTexts:
    agentNetworkRouteConfigTable.setStatus("current")
_AgentNetworkRouteConfigEntry_Object = MibTableRow
agentNetworkRouteConfigEntry = _AgentNetworkRouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 23, 1)
)
agentNetworkRouteConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentNetworkRouteIPAddress"),
)
if mibBuilder.loadTexts:
    agentNetworkRouteConfigEntry.setStatus("current")
_AgentNetworkRouteIPAddress_Type = IpAddress
_AgentNetworkRouteIPAddress_Object = MibTableColumn
agentNetworkRouteIPAddress = _AgentNetworkRouteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 23, 1, 1),
    _AgentNetworkRouteIPAddress_Type()
)
agentNetworkRouteIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNetworkRouteIPAddress.setStatus("current")
_AgentNetworkRouteIPNetmask_Type = IpAddress
_AgentNetworkRouteIPNetmask_Object = MibTableColumn
agentNetworkRouteIPNetmask = _AgentNetworkRouteIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 23, 1, 2),
    _AgentNetworkRouteIPNetmask_Type()
)
agentNetworkRouteIPNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNetworkRouteIPNetmask.setStatus("current")
_AgentNetworkRouteGateway_Type = IpAddress
_AgentNetworkRouteGateway_Object = MibTableColumn
agentNetworkRouteGateway = _AgentNetworkRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 23, 1, 3),
    _AgentNetworkRouteGateway_Type()
)
agentNetworkRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNetworkRouteGateway.setStatus("current")
_AgentNetworkRouteStatus_Type = RowStatus
_AgentNetworkRouteStatus_Object = MibTableColumn
agentNetworkRouteStatus = _AgentNetworkRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 23, 1, 23),
    _AgentNetworkRouteStatus_Type()
)
agentNetworkRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNetworkRouteStatus.setStatus("current")


class _AgentNetworkPeerToPeerBlockingMode_Type(Integer32):
    """Custom type agentNetworkPeerToPeerBlockingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentNetworkPeerToPeerBlockingMode_Type.__name__ = "Integer32"
_AgentNetworkPeerToPeerBlockingMode_Object = MibScalar
agentNetworkPeerToPeerBlockingMode = _AgentNetworkPeerToPeerBlockingMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 24),
    _AgentNetworkPeerToPeerBlockingMode_Type()
)
agentNetworkPeerToPeerBlockingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkPeerToPeerBlockingMode.setStatus("current")
_AgentNetworkMulticastGroupAddress_Type = IpAddress
_AgentNetworkMulticastGroupAddress_Object = MibScalar
agentNetworkMulticastGroupAddress = _AgentNetworkMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 3, 25),
    _AgentNetworkMulticastGroupAddress_Type()
)
agentNetworkMulticastGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkMulticastGroupAddress.setStatus("current")
_AgentServicePortConfigGroup_ObjectIdentity = ObjectIdentity
agentServicePortConfigGroup = _AgentServicePortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 4)
)
_AgentServicePortIPAddress_Type = IpAddress
_AgentServicePortIPAddress_Object = MibScalar
agentServicePortIPAddress = _AgentServicePortIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 4, 1),
    _AgentServicePortIPAddress_Type()
)
agentServicePortIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortIPAddress.setStatus("obsolete")
_AgentServicePortSubnetMask_Type = IpAddress
_AgentServicePortSubnetMask_Object = MibScalar
agentServicePortSubnetMask = _AgentServicePortSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 4, 2),
    _AgentServicePortSubnetMask_Type()
)
agentServicePortSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortSubnetMask.setStatus("obsolete")
_AgentServicePortDefaultGateway_Type = IpAddress
_AgentServicePortDefaultGateway_Object = MibScalar
agentServicePortDefaultGateway = _AgentServicePortDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 4, 3),
    _AgentServicePortDefaultGateway_Type()
)
agentServicePortDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortDefaultGateway.setStatus("obsolete")
_AgentServicePortBurnedInMacAddress_Type = PhysAddress
_AgentServicePortBurnedInMacAddress_Object = MibScalar
agentServicePortBurnedInMacAddress = _AgentServicePortBurnedInMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 4, 4),
    _AgentServicePortBurnedInMacAddress_Type()
)
agentServicePortBurnedInMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentServicePortBurnedInMacAddress.setStatus("obsolete")


class _AgentServicePortConfigProtocol_Type(Integer32):
    """Custom type agentServicePortConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 3),
          ("none", 1))
    )


_AgentServicePortConfigProtocol_Type.__name__ = "Integer32"
_AgentServicePortConfigProtocol_Object = MibScalar
agentServicePortConfigProtocol = _AgentServicePortConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 4, 5),
    _AgentServicePortConfigProtocol_Type()
)
agentServicePortConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentServicePortConfigProtocol.setStatus("obsolete")
_AgentSnmpConfigGroup_ObjectIdentity = ObjectIdentity
agentSnmpConfigGroup = _AgentSnmpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5)
)


class _AgentSnmpTrapPortNumber_Type(Unsigned32):
    """Custom type agentSnmpTrapPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_AgentSnmpTrapPortNumber_Type.__name__ = "Unsigned32"
_AgentSnmpTrapPortNumber_Object = MibScalar
agentSnmpTrapPortNumber = _AgentSnmpTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 1),
    _AgentSnmpTrapPortNumber_Type()
)
agentSnmpTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapPortNumber.setStatus("current")


class _AgentSnmpVersion1Status_Type(Integer32):
    """Custom type agentSnmpVersion1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSnmpVersion1Status_Type.__name__ = "Integer32"
_AgentSnmpVersion1Status_Object = MibScalar
agentSnmpVersion1Status = _AgentSnmpVersion1Status_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 2),
    _AgentSnmpVersion1Status_Type()
)
agentSnmpVersion1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpVersion1Status.setStatus("current")


class _AgentSnmpVersion2cStatus_Type(Integer32):
    """Custom type agentSnmpVersion2cStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSnmpVersion2cStatus_Type.__name__ = "Integer32"
_AgentSnmpVersion2cStatus_Object = MibScalar
agentSnmpVersion2cStatus = _AgentSnmpVersion2cStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 3),
    _AgentSnmpVersion2cStatus_Type()
)
agentSnmpVersion2cStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpVersion2cStatus.setStatus("current")
_AgentSnmpCommunityConfigTable_Object = MibTable
agentSnmpCommunityConfigTable = _AgentSnmpCommunityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    agentSnmpCommunityConfigTable.setStatus("current")
_AgentSnmpCommunityConfigEntry_Object = MibTableRow
agentSnmpCommunityConfigEntry = _AgentSnmpCommunityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5, 1)
)
agentSnmpCommunityConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentSnmpCommunityName"),
)
if mibBuilder.loadTexts:
    agentSnmpCommunityConfigEntry.setStatus("current")


class _AgentSnmpCommunityName_Type(DisplayString):
    """Custom type agentSnmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpCommunityName_Type.__name__ = "DisplayString"
_AgentSnmpCommunityName_Object = MibTableColumn
agentSnmpCommunityName = _AgentSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5, 1, 1),
    _AgentSnmpCommunityName_Type()
)
agentSnmpCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpCommunityName.setStatus("current")
_AgentSnmpCommunityIPAddress_Type = IpAddress
_AgentSnmpCommunityIPAddress_Object = MibTableColumn
agentSnmpCommunityIPAddress = _AgentSnmpCommunityIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5, 1, 2),
    _AgentSnmpCommunityIPAddress_Type()
)
agentSnmpCommunityIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpCommunityIPAddress.setStatus("current")
_AgentSnmpCommunityIPMask_Type = IpAddress
_AgentSnmpCommunityIPMask_Object = MibTableColumn
agentSnmpCommunityIPMask = _AgentSnmpCommunityIPMask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5, 1, 3),
    _AgentSnmpCommunityIPMask_Type()
)
agentSnmpCommunityIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpCommunityIPMask.setStatus("current")


class _AgentSnmpCommunityAccessMode_Type(Integer32):
    """Custom type agentSnmpCommunityAccessMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_AgentSnmpCommunityAccessMode_Type.__name__ = "Integer32"
_AgentSnmpCommunityAccessMode_Object = MibTableColumn
agentSnmpCommunityAccessMode = _AgentSnmpCommunityAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5, 1, 4),
    _AgentSnmpCommunityAccessMode_Type()
)
agentSnmpCommunityAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpCommunityAccessMode.setStatus("current")


class _AgentSnmpCommunityEnabled_Type(Integer32):
    """Custom type agentSnmpCommunityEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AgentSnmpCommunityEnabled_Type.__name__ = "Integer32"
_AgentSnmpCommunityEnabled_Object = MibTableColumn
agentSnmpCommunityEnabled = _AgentSnmpCommunityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5, 1, 5),
    _AgentSnmpCommunityEnabled_Type()
)
agentSnmpCommunityEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpCommunityEnabled.setStatus("current")
_AgentSnmpCommunityStatus_Type = RowStatus
_AgentSnmpCommunityStatus_Object = MibTableColumn
agentSnmpCommunityStatus = _AgentSnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 5, 1, 25),
    _AgentSnmpCommunityStatus_Type()
)
agentSnmpCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpCommunityStatus.setStatus("current")
_AgentSnmpTrapReceiverConfigTable_Object = MibTable
agentSnmpTrapReceiverConfigTable = _AgentSnmpTrapReceiverConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverConfigTable.setStatus("current")
_AgentSnmpTrapReceiverConfigEntry_Object = MibTableRow
agentSnmpTrapReceiverConfigEntry = _AgentSnmpTrapReceiverConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 6, 1)
)
agentSnmpTrapReceiverConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentSnmpTrapReceiverName"),
)
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverConfigEntry.setStatus("current")


class _AgentSnmpTrapReceiverName_Type(OctetString):
    """Custom type agentSnmpTrapReceiverName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentSnmpTrapReceiverName_Type.__name__ = "OctetString"
_AgentSnmpTrapReceiverName_Object = MibTableColumn
agentSnmpTrapReceiverName = _AgentSnmpTrapReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 6, 1, 1),
    _AgentSnmpTrapReceiverName_Type()
)
agentSnmpTrapReceiverName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverName.setStatus("current")
_AgentSnmpTrapReceiverIPAddress_Type = IpAddress
_AgentSnmpTrapReceiverIPAddress_Object = MibTableColumn
agentSnmpTrapReceiverIPAddress = _AgentSnmpTrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 6, 1, 2),
    _AgentSnmpTrapReceiverIPAddress_Type()
)
agentSnmpTrapReceiverIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverIPAddress.setStatus("current")


class _AgentSnmpTrapReceiverEnabled_Type(Integer32):
    """Custom type agentSnmpTrapReceiverEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AgentSnmpTrapReceiverEnabled_Type.__name__ = "Integer32"
_AgentSnmpTrapReceiverEnabled_Object = MibTableColumn
agentSnmpTrapReceiverEnabled = _AgentSnmpTrapReceiverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 6, 1, 3),
    _AgentSnmpTrapReceiverEnabled_Type()
)
agentSnmpTrapReceiverEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverEnabled.setStatus("current")
_AgentSnmpTrapReceiverStatus_Type = RowStatus
_AgentSnmpTrapReceiverStatus_Object = MibTableColumn
agentSnmpTrapReceiverStatus = _AgentSnmpTrapReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 6, 1, 23),
    _AgentSnmpTrapReceiverStatus_Type()
)
agentSnmpTrapReceiverStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpTrapReceiverStatus.setStatus("current")
_AgentSnmpTrapFlagsConfigGroup_ObjectIdentity = ObjectIdentity
agentSnmpTrapFlagsConfigGroup = _AgentSnmpTrapFlagsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 7)
)


class _AgentSnmpAuthenticationTrapFlag_Type(Integer32):
    """Custom type agentSnmpAuthenticationTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpAuthenticationTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpAuthenticationTrapFlag_Object = MibScalar
agentSnmpAuthenticationTrapFlag = _AgentSnmpAuthenticationTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 7, 1),
    _AgentSnmpAuthenticationTrapFlag_Type()
)
agentSnmpAuthenticationTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpAuthenticationTrapFlag.setStatus("current")


class _AgentSnmpLinkUpDownTrapFlag_Type(Integer32):
    """Custom type agentSnmpLinkUpDownTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpLinkUpDownTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpLinkUpDownTrapFlag_Object = MibScalar
agentSnmpLinkUpDownTrapFlag = _AgentSnmpLinkUpDownTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 7, 2),
    _AgentSnmpLinkUpDownTrapFlag_Type()
)
agentSnmpLinkUpDownTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpLinkUpDownTrapFlag.setStatus("current")


class _AgentSnmpMultipleUsersTrapFlag_Type(Integer32):
    """Custom type agentSnmpMultipleUsersTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpMultipleUsersTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpMultipleUsersTrapFlag_Object = MibScalar
agentSnmpMultipleUsersTrapFlag = _AgentSnmpMultipleUsersTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 7, 3),
    _AgentSnmpMultipleUsersTrapFlag_Type()
)
agentSnmpMultipleUsersTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpMultipleUsersTrapFlag.setStatus("current")


class _AgentSnmpSpanningTreeTrapFlag_Type(Integer32):
    """Custom type agentSnmpSpanningTreeTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpSpanningTreeTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpSpanningTreeTrapFlag_Object = MibScalar
agentSnmpSpanningTreeTrapFlag = _AgentSnmpSpanningTreeTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 7, 4),
    _AgentSnmpSpanningTreeTrapFlag_Type()
)
agentSnmpSpanningTreeTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpSpanningTreeTrapFlag.setStatus("current")


class _AgentSnmpBroadcastStormTrapFlag_Type(Integer32):
    """Custom type agentSnmpBroadcastStormTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSnmpBroadcastStormTrapFlag_Type.__name__ = "Integer32"
_AgentSnmpBroadcastStormTrapFlag_Object = MibScalar
agentSnmpBroadcastStormTrapFlag = _AgentSnmpBroadcastStormTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 5, 7, 5),
    _AgentSnmpBroadcastStormTrapFlag_Type()
)
agentSnmpBroadcastStormTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpBroadcastStormTrapFlag.setStatus("obsolete")
_AgentSnmpV3ConfigGroup_ObjectIdentity = ObjectIdentity
agentSnmpV3ConfigGroup = _AgentSnmpV3ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6)
)


class _AgentSnmpVersion3Status_Type(Integer32):
    """Custom type agentSnmpVersion3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentSnmpVersion3Status_Type.__name__ = "Integer32"
_AgentSnmpVersion3Status_Object = MibScalar
agentSnmpVersion3Status = _AgentSnmpVersion3Status_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 1),
    _AgentSnmpVersion3Status_Type()
)
agentSnmpVersion3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpVersion3Status.setStatus("current")
_AgentSnmpV3UserConfigTable_Object = MibTable
agentSnmpV3UserConfigTable = _AgentSnmpV3UserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    agentSnmpV3UserConfigTable.setStatus("current")
_AgentSnmpV3UserConfigEntry_Object = MibTableRow
agentSnmpV3UserConfigEntry = _AgentSnmpV3UserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1)
)
agentSnmpV3UserConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserName"),
)
if mibBuilder.loadTexts:
    agentSnmpV3UserConfigEntry.setStatus("current")


class _AgentSnmpV3UserName_Type(OctetString):
    """Custom type agentSnmpV3UserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentSnmpV3UserName_Type.__name__ = "OctetString"
_AgentSnmpV3UserName_Object = MibTableColumn
agentSnmpV3UserName = _AgentSnmpV3UserName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1, 1),
    _AgentSnmpV3UserName_Type()
)
agentSnmpV3UserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpV3UserName.setStatus("current")


class _AgentSnmpV3UserAccessMode_Type(Integer32):
    """Custom type agentSnmpV3UserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_AgentSnmpV3UserAccessMode_Type.__name__ = "Integer32"
_AgentSnmpV3UserAccessMode_Object = MibTableColumn
agentSnmpV3UserAccessMode = _AgentSnmpV3UserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1, 2),
    _AgentSnmpV3UserAccessMode_Type()
)
agentSnmpV3UserAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpV3UserAccessMode.setStatus("current")


class _AgentSnmpV3UserAuthenticationType_Type(Integer32):
    """Custom type agentSnmpV3UserAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hmacmd5", 2),
          ("hmacsha", 3),
          ("none", 1))
    )


_AgentSnmpV3UserAuthenticationType_Type.__name__ = "Integer32"
_AgentSnmpV3UserAuthenticationType_Object = MibTableColumn
agentSnmpV3UserAuthenticationType = _AgentSnmpV3UserAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1, 3),
    _AgentSnmpV3UserAuthenticationType_Type()
)
agentSnmpV3UserAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpV3UserAuthenticationType.setStatus("current")


class _AgentSnmpV3UserEncryptionType_Type(Integer32):
    """Custom type agentSnmpV3UserEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("none", 1))
    )


_AgentSnmpV3UserEncryptionType_Type.__name__ = "Integer32"
_AgentSnmpV3UserEncryptionType_Object = MibTableColumn
agentSnmpV3UserEncryptionType = _AgentSnmpV3UserEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1, 4),
    _AgentSnmpV3UserEncryptionType_Type()
)
agentSnmpV3UserEncryptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpV3UserEncryptionType.setStatus("current")


class _AgentSnmpV3UserAuthenticationPassword_Type(OctetString):
    """Custom type agentSnmpV3UserAuthenticationPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentSnmpV3UserAuthenticationPassword_Type.__name__ = "OctetString"
_AgentSnmpV3UserAuthenticationPassword_Object = MibTableColumn
agentSnmpV3UserAuthenticationPassword = _AgentSnmpV3UserAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1, 5),
    _AgentSnmpV3UserAuthenticationPassword_Type()
)
agentSnmpV3UserAuthenticationPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpV3UserAuthenticationPassword.setStatus("current")


class _AgentSnmpV3UserEncryptionPassword_Type(OctetString):
    """Custom type agentSnmpV3UserEncryptionPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentSnmpV3UserEncryptionPassword_Type.__name__ = "OctetString"
_AgentSnmpV3UserEncryptionPassword_Object = MibTableColumn
agentSnmpV3UserEncryptionPassword = _AgentSnmpV3UserEncryptionPassword_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1, 6),
    _AgentSnmpV3UserEncryptionPassword_Type()
)
agentSnmpV3UserEncryptionPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpV3UserEncryptionPassword.setStatus("current")
_AgentSnmpV3UserStatus_Type = RowStatus
_AgentSnmpV3UserStatus_Object = MibTableColumn
agentSnmpV3UserStatus = _AgentSnmpV3UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 6, 2, 1, 26),
    _AgentSnmpV3UserStatus_Type()
)
agentSnmpV3UserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSnmpV3UserStatus.setStatus("current")
_AgentSpanningTreeConfigGroup_ObjectIdentity = ObjectIdentity
agentSpanningTreeConfigGroup = _AgentSpanningTreeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 7)
)


class _AgentSpanningTreeMode_Type(Integer32):
    """Custom type agentSpanningTreeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSpanningTreeMode_Type.__name__ = "Integer32"
_AgentSpanningTreeMode_Object = MibScalar
agentSpanningTreeMode = _AgentSpanningTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 7, 1),
    _AgentSpanningTreeMode_Type()
)
agentSpanningTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSpanningTreeMode.setStatus("current")
_AgentSwitchConfigGroup_ObjectIdentity = ObjectIdentity
agentSwitchConfigGroup = _AgentSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 8)
)


class _AgentSwitchBroadcastControlMode_Type(Integer32):
    """Custom type agentSwitchBroadcastControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchBroadcastControlMode_Type.__name__ = "Integer32"
_AgentSwitchBroadcastControlMode_Object = MibScalar
agentSwitchBroadcastControlMode = _AgentSwitchBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 8, 2),
    _AgentSwitchBroadcastControlMode_Type()
)
agentSwitchBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBroadcastControlMode.setStatus("current")


class _AgentSwitchDot3FlowControlMode_Type(Integer32):
    """Custom type agentSwitchDot3FlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSwitchDot3FlowControlMode_Type.__name__ = "Integer32"
_AgentSwitchDot3FlowControlMode_Object = MibScalar
agentSwitchDot3FlowControlMode = _AgentSwitchDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 8, 3),
    _AgentSwitchDot3FlowControlMode_Type()
)
agentSwitchDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDot3FlowControlMode.setStatus("current")
_AgentSwitchAddressAgingTimeoutTable_Object = MibTable
agentSwitchAddressAgingTimeoutTable = _AgentSwitchAddressAgingTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeoutTable.setStatus("current")
_AgentSwitchAddressAgingTimeoutEntry_Object = MibTableRow
agentSwitchAddressAgingTimeoutEntry = _AgentSwitchAddressAgingTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 8, 4, 1)
)
agentSwitchAddressAgingTimeoutEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeoutEntry.setStatus("current")


class _AgentSwitchAddressAgingTimeout_Type(Integer32):
    """Custom type agentSwitchAddressAgingTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AgentSwitchAddressAgingTimeout_Type.__name__ = "Integer32"
_AgentSwitchAddressAgingTimeout_Object = MibTableColumn
agentSwitchAddressAgingTimeout = _AgentSwitchAddressAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 8, 4, 1, 10),
    _AgentSwitchAddressAgingTimeout_Type()
)
agentSwitchAddressAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchAddressAgingTimeout.setStatus("current")


class _AgentSwitchLwappTransportMode_Type(Integer32):
    """Custom type agentSwitchLwappTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )


_AgentSwitchLwappTransportMode_Type.__name__ = "Integer32"
_AgentSwitchLwappTransportMode_Object = MibScalar
agentSwitchLwappTransportMode = _AgentSwitchLwappTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 8, 5),
    _AgentSwitchLwappTransportMode_Type()
)
agentSwitchLwappTransportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchLwappTransportMode.setStatus("current")
_AgentTransferConfigGroup_ObjectIdentity = ObjectIdentity
agentTransferConfigGroup = _AgentTransferConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9)
)
_AgentTransferUploadGroup_ObjectIdentity = ObjectIdentity
agentTransferUploadGroup = _AgentTransferUploadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1)
)


class _AgentTransferUploadMode_Type(Integer32):
    """Custom type agentTransferUploadMode based on Integer32"""
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
        *(("tftp", 1),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_AgentTransferUploadMode_Type.__name__ = "Integer32"
_AgentTransferUploadMode_Object = MibScalar
agentTransferUploadMode = _AgentTransferUploadMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1, 1),
    _AgentTransferUploadMode_Type()
)
agentTransferUploadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadMode.setStatus("current")
_AgentTransferUploadServerIP_Type = IpAddress
_AgentTransferUploadServerIP_Object = MibScalar
agentTransferUploadServerIP = _AgentTransferUploadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1, 2),
    _AgentTransferUploadServerIP_Type()
)
agentTransferUploadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadServerIP.setStatus("current")


class _AgentTransferUploadPath_Type(DisplayString):
    """Custom type agentTransferUploadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgentTransferUploadPath_Type.__name__ = "DisplayString"
_AgentTransferUploadPath_Object = MibScalar
agentTransferUploadPath = _AgentTransferUploadPath_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1, 3),
    _AgentTransferUploadPath_Type()
)
agentTransferUploadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadPath.setStatus("current")


class _AgentTransferUploadFilename_Type(DisplayString):
    """Custom type agentTransferUploadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgentTransferUploadFilename_Type.__name__ = "DisplayString"
_AgentTransferUploadFilename_Object = MibScalar
agentTransferUploadFilename = _AgentTransferUploadFilename_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1, 4),
    _AgentTransferUploadFilename_Type()
)
agentTransferUploadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadFilename.setStatus("current")


class _AgentTransferUploadDataType_Type(Integer32):
    """Custom type agentTransferUploadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("crashfile", 6),
          ("errorlog", 3),
          ("signatures", 7),
          ("systemtrace", 4),
          ("traplog", 5),
          ("unknown", 99))
    )


_AgentTransferUploadDataType_Type.__name__ = "Integer32"
_AgentTransferUploadDataType_Object = MibScalar
agentTransferUploadDataType = _AgentTransferUploadDataType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1, 5),
    _AgentTransferUploadDataType_Type()
)
agentTransferUploadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadDataType.setStatus("current")


class _AgentTransferUploadStart_Type(Integer32):
    """Custom type agentTransferUploadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentTransferUploadStart_Type.__name__ = "Integer32"
_AgentTransferUploadStart_Object = MibScalar
agentTransferUploadStart = _AgentTransferUploadStart_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1, 6),
    _AgentTransferUploadStart_Type()
)
agentTransferUploadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferUploadStart.setStatus("current")


class _AgentTransferUploadStatus_Type(Integer32):
    """Custom type agentTransferUploadStatus based on Integer32"""
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
              12,
              13,
              99)
        )
    )
    namedValues = NamedValues(
        *(("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknown", 99),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_AgentTransferUploadStatus_Type.__name__ = "Integer32"
_AgentTransferUploadStatus_Object = MibScalar
agentTransferUploadStatus = _AgentTransferUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 1, 7),
    _AgentTransferUploadStatus_Type()
)
agentTransferUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferUploadStatus.setStatus("current")
_AgentTransferDownloadGroup_ObjectIdentity = ObjectIdentity
agentTransferDownloadGroup = _AgentTransferDownloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2)
)


class _AgentTransferDownloadMode_Type(Integer32):
    """Custom type agentTransferDownloadMode based on Integer32"""
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
        *(("tftp", 1),
          ("xmodem", 2),
          ("ymodem", 3),
          ("zmodem", 4))
    )


_AgentTransferDownloadMode_Type.__name__ = "Integer32"
_AgentTransferDownloadMode_Object = MibScalar
agentTransferDownloadMode = _AgentTransferDownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 1),
    _AgentTransferDownloadMode_Type()
)
agentTransferDownloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadMode.setStatus("current")
_AgentTransferDownloadServerIP_Type = IpAddress
_AgentTransferDownloadServerIP_Object = MibScalar
agentTransferDownloadServerIP = _AgentTransferDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 2),
    _AgentTransferDownloadServerIP_Type()
)
agentTransferDownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadServerIP.setStatus("current")


class _AgentTransferDownloadPath_Type(DisplayString):
    """Custom type agentTransferDownloadPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgentTransferDownloadPath_Type.__name__ = "DisplayString"
_AgentTransferDownloadPath_Object = MibScalar
agentTransferDownloadPath = _AgentTransferDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 3),
    _AgentTransferDownloadPath_Type()
)
agentTransferDownloadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadPath.setStatus("current")


class _AgentTransferDownloadFilename_Type(DisplayString):
    """Custom type agentTransferDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AgentTransferDownloadFilename_Type.__name__ = "DisplayString"
_AgentTransferDownloadFilename_Object = MibScalar
agentTransferDownloadFilename = _AgentTransferDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 4),
    _AgentTransferDownloadFilename_Type()
)
agentTransferDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadFilename.setStatus("current")


class _AgentTransferDownloadDataType_Type(Integer32):
    """Custom type agentTransferDownloadDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("code", 2),
          ("config", 3),
          ("customWebAuth", 7),
          ("signatures", 6),
          ("unknown", 99),
          ("webadmincert", 5),
          ("webauthcert", 4))
    )


_AgentTransferDownloadDataType_Type.__name__ = "Integer32"
_AgentTransferDownloadDataType_Object = MibScalar
agentTransferDownloadDataType = _AgentTransferDownloadDataType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 5),
    _AgentTransferDownloadDataType_Type()
)
agentTransferDownloadDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadDataType.setStatus("current")


class _AgentTransferDownloadStart_Type(Integer32):
    """Custom type agentTransferDownloadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentTransferDownloadStart_Type.__name__ = "Integer32"
_AgentTransferDownloadStart_Object = MibScalar
agentTransferDownloadStart = _AgentTransferDownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 6),
    _AgentTransferDownloadStart_Type()
)
agentTransferDownloadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadStart.setStatus("current")


class _AgentTransferDownloadStatus_Type(Integer32):
    """Custom type agentTransferDownloadStatus based on Integer32"""
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
              12,
              13,
              14,
              15,
              99)
        )
    )
    namedValues = NamedValues(
        *(("bootBreakOff", 14),
          ("checkingCRC", 9),
          ("errorStarting", 3),
          ("failedCRC", 10),
          ("failureWritingToFlash", 8),
          ("invalidConfigFile", 6),
          ("invalidTarFile", 15),
          ("notInitiated", 1),
          ("transferFailed", 13),
          ("transferStarting", 2),
          ("transferSuccessful", 12),
          ("unknown", 99),
          ("unknownDirection", 11),
          ("updatingConfig", 5),
          ("writingToFlash", 7),
          ("wrongFileType", 4))
    )


_AgentTransferDownloadStatus_Type.__name__ = "Integer32"
_AgentTransferDownloadStatus_Object = MibScalar
agentTransferDownloadStatus = _AgentTransferDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 7),
    _AgentTransferDownloadStatus_Type()
)
agentTransferDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferDownloadStatus.setStatus("current")


class _AgentTransferDownloadTftpMaxRetries_Type(Unsigned32):
    """Custom type agentTransferDownloadTftpMaxRetries based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AgentTransferDownloadTftpMaxRetries_Type.__name__ = "Unsigned32"
_AgentTransferDownloadTftpMaxRetries_Object = MibScalar
agentTransferDownloadTftpMaxRetries = _AgentTransferDownloadTftpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 8),
    _AgentTransferDownloadTftpMaxRetries_Type()
)
agentTransferDownloadTftpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadTftpMaxRetries.setStatus("current")


class _AgentTransferDownloadTftpTimeout_Type(Unsigned32):
    """Custom type agentTransferDownloadTftpTimeout based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AgentTransferDownloadTftpTimeout_Type.__name__ = "Unsigned32"
_AgentTransferDownloadTftpTimeout_Object = MibScalar
agentTransferDownloadTftpTimeout = _AgentTransferDownloadTftpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 2, 9),
    _AgentTransferDownloadTftpTimeout_Type()
)
agentTransferDownloadTftpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDownloadTftpTimeout.setStatus("current")


class _AgentTransferConfigurationFileEncryption_Type(Integer32):
    """Custom type agentTransferConfigurationFileEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentTransferConfigurationFileEncryption_Type.__name__ = "Integer32"
_AgentTransferConfigurationFileEncryption_Object = MibScalar
agentTransferConfigurationFileEncryption = _AgentTransferConfigurationFileEncryption_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 3),
    _AgentTransferConfigurationFileEncryption_Type()
)
agentTransferConfigurationFileEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferConfigurationFileEncryption.setStatus("current")


class _AgentTransferConfigurationFileEncryptionKey_Type(DisplayString):
    """Custom type agentTransferConfigurationFileEncryptionKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgentTransferConfigurationFileEncryptionKey_Type.__name__ = "DisplayString"
_AgentTransferConfigurationFileEncryptionKey_Object = MibScalar
agentTransferConfigurationFileEncryptionKey = _AgentTransferConfigurationFileEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 9, 4),
    _AgentTransferConfigurationFileEncryptionKey_Type()
)
agentTransferConfigurationFileEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferConfigurationFileEncryptionKey.setStatus("current")
_AgentDot3adAggPortTable_Object = MibTable
agentDot3adAggPortTable = _AgentDot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 11)
)
if mibBuilder.loadTexts:
    agentDot3adAggPortTable.setStatus("obsolete")
_AgentDot3adAggPortEntry_Object = MibTableRow
agentDot3adAggPortEntry = _AgentDot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 11, 1)
)
agentDot3adAggPortEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentDot3adAggPort"),
)
if mibBuilder.loadTexts:
    agentDot3adAggPortEntry.setStatus("obsolete")
_AgentDot3adAggPort_Type = Integer32
_AgentDot3adAggPort_Object = MibTableColumn
agentDot3adAggPort = _AgentDot3adAggPort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 11, 1, 1),
    _AgentDot3adAggPort_Type()
)
agentDot3adAggPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDot3adAggPort.setStatus("obsolete")


class _AgentDot3adAggPortLACPMode_Type(Integer32):
    """Custom type agentDot3adAggPortLACPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentDot3adAggPortLACPMode_Type.__name__ = "Integer32"
_AgentDot3adAggPortLACPMode_Object = MibTableColumn
agentDot3adAggPortLACPMode = _AgentDot3adAggPortLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 11, 1, 21),
    _AgentDot3adAggPortLACPMode_Type()
)
agentDot3adAggPortLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot3adAggPortLACPMode.setStatus("obsolete")
_AgentPortConfigTable_Object = MibTable
agentPortConfigTable = _AgentPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12)
)
if mibBuilder.loadTexts:
    agentPortConfigTable.setStatus("current")
_AgentPortConfigEntry_Object = MibTableRow
agentPortConfigEntry = _AgentPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1)
)
agentPortConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    agentPortConfigEntry.setStatus("current")


class _AgentPortDot1dBasePort_Type(Integer32):
    """Custom type agentPortDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentPortDot1dBasePort_Type.__name__ = "Integer32"
_AgentPortDot1dBasePort_Object = MibTableColumn
agentPortDot1dBasePort = _AgentPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 1),
    _AgentPortDot1dBasePort_Type()
)
agentPortDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortDot1dBasePort.setStatus("current")
_AgentPortIfIndex_Type = Integer32
_AgentPortIfIndex_Object = MibTableColumn
agentPortIfIndex = _AgentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 2),
    _AgentPortIfIndex_Type()
)
agentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortIfIndex.setStatus("current")
_AgentPortIanaType_Type = IANAifType
_AgentPortIanaType_Object = MibTableColumn
agentPortIanaType = _AgentPortIanaType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 3),
    _AgentPortIanaType_Type()
)
agentPortIanaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortIanaType.setStatus("current")


class _AgentPortSTPMode_Type(Integer32):
    """Custom type agentPortSTPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("fast", 2),
          ("off", 3))
    )


_AgentPortSTPMode_Type.__name__ = "Integer32"
_AgentPortSTPMode_Object = MibTableColumn
agentPortSTPMode = _AgentPortSTPMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 4),
    _AgentPortSTPMode_Type()
)
agentPortSTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSTPMode.setStatus("current")


class _AgentPortSTPState_Type(Integer32):
    """Custom type agentPortSTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("disabled", 5),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )


_AgentPortSTPState_Type.__name__ = "Integer32"
_AgentPortSTPState_Object = MibTableColumn
agentPortSTPState = _AgentPortSTPState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 5),
    _AgentPortSTPState_Type()
)
agentPortSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortSTPState.setStatus("current")


class _AgentPortAdminMode_Type(Integer32):
    """Custom type agentPortAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortAdminMode_Type.__name__ = "Integer32"
_AgentPortAdminMode_Object = MibTableColumn
agentPortAdminMode = _AgentPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 6),
    _AgentPortAdminMode_Type()
)
agentPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortAdminMode.setStatus("current")


class _AgentPortPhysicalMode_Type(Integer32):
    """Custom type agentPortPhysicalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("full10", 3),
          ("full100", 5),
          ("full1000sx", 8),
          ("half10", 2),
          ("half100", 4))
    )


_AgentPortPhysicalMode_Type.__name__ = "Integer32"
_AgentPortPhysicalMode_Object = MibTableColumn
agentPortPhysicalMode = _AgentPortPhysicalMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 7),
    _AgentPortPhysicalMode_Type()
)
agentPortPhysicalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortPhysicalMode.setStatus("current")


class _AgentPortPhysicalStatus_Type(Integer32):
    """Custom type agentPortPhysicalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("autonegotiate", 1),
          ("full10", 3),
          ("full100", 5),
          ("full1000sx", 8),
          ("half10", 2),
          ("half100", 4),
          ("unknown", 9))
    )


_AgentPortPhysicalStatus_Type.__name__ = "Integer32"
_AgentPortPhysicalStatus_Object = MibTableColumn
agentPortPhysicalStatus = _AgentPortPhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 8),
    _AgentPortPhysicalStatus_Type()
)
agentPortPhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortPhysicalStatus.setStatus("current")


class _AgentPortLinkTrapMode_Type(Integer32):
    """Custom type agentPortLinkTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortLinkTrapMode_Type.__name__ = "Integer32"
_AgentPortLinkTrapMode_Object = MibTableColumn
agentPortLinkTrapMode = _AgentPortLinkTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 9),
    _AgentPortLinkTrapMode_Type()
)
agentPortLinkTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortLinkTrapMode.setStatus("current")


class _AgentPortClearStats_Type(Integer32):
    """Custom type agentPortClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortClearStats_Type.__name__ = "Integer32"
_AgentPortClearStats_Object = MibTableColumn
agentPortClearStats = _AgentPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 10),
    _AgentPortClearStats_Type()
)
agentPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortClearStats.setStatus("current")
_AgentPortDefaultType_Type = ObjectIdentifier
_AgentPortDefaultType_Object = MibTableColumn
agentPortDefaultType = _AgentPortDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 11),
    _AgentPortDefaultType_Type()
)
agentPortDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDefaultType.setStatus("current")
_AgentPortType_Type = ObjectIdentifier
_AgentPortType_Object = MibTableColumn
agentPortType = _AgentPortType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 12),
    _AgentPortType_Type()
)
agentPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortType.setStatus("current")


class _AgentPortAutoNegAdminStatus_Type(Integer32):
    """Custom type agentPortAutoNegAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortAutoNegAdminStatus_Type.__name__ = "Integer32"
_AgentPortAutoNegAdminStatus_Object = MibTableColumn
agentPortAutoNegAdminStatus = _AgentPortAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 13),
    _AgentPortAutoNegAdminStatus_Type()
)
agentPortAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortAutoNegAdminStatus.setStatus("current")


class _AgentPortDot3FlowControlMode_Type(Integer32):
    """Custom type agentPortDot3FlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentPortDot3FlowControlMode_Type.__name__ = "Integer32"
_AgentPortDot3FlowControlMode_Object = MibTableColumn
agentPortDot3FlowControlMode = _AgentPortDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 14),
    _AgentPortDot3FlowControlMode_Type()
)
agentPortDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortDot3FlowControlMode.setStatus("current")


class _AgentPortPowerMode_Type(Integer32):
    """Custom type agentPortPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentPortPowerMode_Type.__name__ = "Integer32"
_AgentPortPowerMode_Object = MibTableColumn
agentPortPowerMode = _AgentPortPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 15),
    _AgentPortPowerMode_Type()
)
agentPortPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortPowerMode.setStatus("current")


class _AgentPortGvrpStatus_Type(Integer32):
    """Custom type agentPortGvrpStatus based on Integer32"""
    defaultValue = 1

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


_AgentPortGvrpStatus_Type.__name__ = "Integer32"
_AgentPortGvrpStatus_Object = MibTableColumn
agentPortGvrpStatus = _AgentPortGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 16),
    _AgentPortGvrpStatus_Type()
)
agentPortGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortGvrpStatus.setStatus("obsolete")


class _AgentPortGarpJoinTime_Type(Unsigned32):
    """Custom type agentPortGarpJoinTime based on Unsigned32"""
    defaultValue = 20


_AgentPortGarpJoinTime_Object = MibTableColumn
agentPortGarpJoinTime = _AgentPortGarpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 17),
    _AgentPortGarpJoinTime_Type()
)
agentPortGarpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortGarpJoinTime.setStatus("obsolete")


class _AgentPortGarpLeaveTime_Type(Unsigned32):
    """Custom type agentPortGarpLeaveTime based on Unsigned32"""
    defaultValue = 60


_AgentPortGarpLeaveTime_Object = MibTableColumn
agentPortGarpLeaveTime = _AgentPortGarpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 18),
    _AgentPortGarpLeaveTime_Type()
)
agentPortGarpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortGarpLeaveTime.setStatus("obsolete")


class _AgentPortGarpLeaveAllTime_Type(Unsigned32):
    """Custom type agentPortGarpLeaveAllTime based on Unsigned32"""
    defaultValue = 1000


_AgentPortGarpLeaveAllTime_Object = MibTableColumn
agentPortGarpLeaveAllTime = _AgentPortGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 19),
    _AgentPortGarpLeaveAllTime_Type()
)
agentPortGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortGarpLeaveAllTime.setStatus("obsolete")


class _AgentPortMirrorMode_Type(Integer32):
    """Custom type agentPortMirrorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentPortMirrorMode_Type.__name__ = "Integer32"
_AgentPortMirrorMode_Object = MibTableColumn
agentPortMirrorMode = _AgentPortMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 20),
    _AgentPortMirrorMode_Type()
)
agentPortMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMirrorMode.setStatus("current")


class _AgentPortMulticastApplianceMode_Type(Integer32):
    """Custom type agentPortMulticastApplianceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentPortMulticastApplianceMode_Type.__name__ = "Integer32"
_AgentPortMulticastApplianceMode_Object = MibTableColumn
agentPortMulticastApplianceMode = _AgentPortMulticastApplianceMode_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 21),
    _AgentPortMulticastApplianceMode_Type()
)
agentPortMulticastApplianceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortMulticastApplianceMode.setStatus("current")


class _AgentPortOperationalStatus_Type(Integer32):
    """Custom type agentPortOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AgentPortOperationalStatus_Type.__name__ = "Integer32"
_AgentPortOperationalStatus_Object = MibTableColumn
agentPortOperationalStatus = _AgentPortOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 12, 1, 40),
    _AgentPortOperationalStatus_Type()
)
agentPortOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortOperationalStatus.setStatus("current")
_AgentInterfaceConfigTable_Object = MibTable
agentInterfaceConfigTable = _AgentInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13)
)
if mibBuilder.loadTexts:
    agentInterfaceConfigTable.setStatus("current")
_AgentInterfaceConfigEntry_Object = MibTableRow
agentInterfaceConfigEntry = _AgentInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1)
)
agentInterfaceConfigEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentInterfaceName"),
)
if mibBuilder.loadTexts:
    agentInterfaceConfigEntry.setStatus("current")


class _AgentInterfaceName_Type(OctetString):
    """Custom type agentInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentInterfaceName_Type.__name__ = "OctetString"
_AgentInterfaceName_Object = MibTableColumn
agentInterfaceName = _AgentInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 1),
    _AgentInterfaceName_Type()
)
agentInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceName.setStatus("current")


class _AgentInterfaceVlanId_Type(Integer32):
    """Custom type agentInterfaceVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AgentInterfaceVlanId_Type.__name__ = "Integer32"
_AgentInterfaceVlanId_Object = MibTableColumn
agentInterfaceVlanId = _AgentInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 2),
    _AgentInterfaceVlanId_Type()
)
agentInterfaceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceVlanId.setStatus("current")


class _AgentInterfaceType_Type(Integer32):
    """Custom type agentInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )


_AgentInterfaceType_Type.__name__ = "Integer32"
_AgentInterfaceType_Object = MibTableColumn
agentInterfaceType = _AgentInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 3),
    _AgentInterfaceType_Type()
)
agentInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInterfaceType.setStatus("current")
_AgentInterfaceMacAddress_Type = MacAddress
_AgentInterfaceMacAddress_Object = MibTableColumn
agentInterfaceMacAddress = _AgentInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 4),
    _AgentInterfaceMacAddress_Type()
)
agentInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInterfaceMacAddress.setStatus("current")
_AgentInterfaceIPAddress_Type = IpAddress
_AgentInterfaceIPAddress_Object = MibTableColumn
agentInterfaceIPAddress = _AgentInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 5),
    _AgentInterfaceIPAddress_Type()
)
agentInterfaceIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceIPAddress.setStatus("current")
_AgentInterfaceIPNetmask_Type = IpAddress
_AgentInterfaceIPNetmask_Object = MibTableColumn
agentInterfaceIPNetmask = _AgentInterfaceIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 6),
    _AgentInterfaceIPNetmask_Type()
)
agentInterfaceIPNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceIPNetmask.setStatus("current")
_AgentInterfaceIPGateway_Type = IpAddress
_AgentInterfaceIPGateway_Object = MibTableColumn
agentInterfaceIPGateway = _AgentInterfaceIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 7),
    _AgentInterfaceIPGateway_Type()
)
agentInterfaceIPGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceIPGateway.setStatus("current")


class _AgentInterfacePortNo_Type(Integer32):
    """Custom type agentInterfacePortNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_AgentInterfacePortNo_Type.__name__ = "Integer32"
_AgentInterfacePortNo_Object = MibTableColumn
agentInterfacePortNo = _AgentInterfacePortNo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 8),
    _AgentInterfacePortNo_Type()
)
agentInterfacePortNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfacePortNo.setStatus("current")
_AgentInterfacePrimaryDhcpAddress_Type = IpAddress
_AgentInterfacePrimaryDhcpAddress_Object = MibTableColumn
agentInterfacePrimaryDhcpAddress = _AgentInterfacePrimaryDhcpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 9),
    _AgentInterfacePrimaryDhcpAddress_Type()
)
agentInterfacePrimaryDhcpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfacePrimaryDhcpAddress.setStatus("current")
_AgentInterfaceSecondaryDhcpAddress_Type = IpAddress
_AgentInterfaceSecondaryDhcpAddress_Object = MibTableColumn
agentInterfaceSecondaryDhcpAddress = _AgentInterfaceSecondaryDhcpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 10),
    _AgentInterfaceSecondaryDhcpAddress_Type()
)
agentInterfaceSecondaryDhcpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceSecondaryDhcpAddress.setStatus("current")


class _AgentInterfaceDhcpProtocol_Type(Integer32):
    """Custom type agentInterfaceDhcpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AgentInterfaceDhcpProtocol_Type.__name__ = "Integer32"
_AgentInterfaceDhcpProtocol_Object = MibTableColumn
agentInterfaceDhcpProtocol = _AgentInterfaceDhcpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 11),
    _AgentInterfaceDhcpProtocol_Type()
)
agentInterfaceDhcpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceDhcpProtocol.setStatus("current")


class _AgentInterfaceDnsHostName_Type(DisplayString):
    """Custom type agentInterfaceDnsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AgentInterfaceDnsHostName_Type.__name__ = "DisplayString"
_AgentInterfaceDnsHostName_Object = MibTableColumn
agentInterfaceDnsHostName = _AgentInterfaceDnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 12),
    _AgentInterfaceDnsHostName_Type()
)
agentInterfaceDnsHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceDnsHostName.setStatus("current")


class _AgentInterfaceAclName_Type(DisplayString):
    """Custom type agentInterfaceAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentInterfaceAclName_Type.__name__ = "DisplayString"
_AgentInterfaceAclName_Object = MibTableColumn
agentInterfaceAclName = _AgentInterfaceAclName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 13),
    _AgentInterfaceAclName_Type()
)
agentInterfaceAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceAclName.setStatus("current")


class _AgentInterfaceAPManagementFeature_Type(Integer32):
    """Custom type agentInterfaceAPManagementFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentInterfaceAPManagementFeature_Type.__name__ = "Integer32"
_AgentInterfaceAPManagementFeature_Object = MibTableColumn
agentInterfaceAPManagementFeature = _AgentInterfaceAPManagementFeature_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 14),
    _AgentInterfaceAPManagementFeature_Type()
)
agentInterfaceAPManagementFeature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceAPManagementFeature.setStatus("current")


class _AgentInterfaceActivePortNo_Type(Integer32):
    """Custom type agentInterfaceActivePortNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_AgentInterfaceActivePortNo_Type.__name__ = "Integer32"
_AgentInterfaceActivePortNo_Object = MibTableColumn
agentInterfaceActivePortNo = _AgentInterfaceActivePortNo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 15),
    _AgentInterfaceActivePortNo_Type()
)
agentInterfaceActivePortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInterfaceActivePortNo.setStatus("current")


class _AgentInterfaceBackupPortNo_Type(Integer32):
    """Custom type agentInterfaceBackupPortNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AgentInterfaceBackupPortNo_Type.__name__ = "Integer32"
_AgentInterfaceBackupPortNo_Object = MibTableColumn
agentInterfaceBackupPortNo = _AgentInterfaceBackupPortNo_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 16),
    _AgentInterfaceBackupPortNo_Type()
)
agentInterfaceBackupPortNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceBackupPortNo.setStatus("current")


class _AgentInterfaceVlanQuarantine_Type(TruthValue):
    """Custom type agentInterfaceVlanQuarantine based on TruthValue"""


_AgentInterfaceVlanQuarantine_Object = MibTableColumn
agentInterfaceVlanQuarantine = _AgentInterfaceVlanQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 17),
    _AgentInterfaceVlanQuarantine_Type()
)
agentInterfaceVlanQuarantine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceVlanQuarantine.setStatus("current")
_AgentInterfaceRowStatus_Type = RowStatus
_AgentInterfaceRowStatus_Object = MibTableColumn
agentInterfaceRowStatus = _AgentInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 13, 1, 31),
    _AgentInterfaceRowStatus_Type()
)
agentInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentInterfaceRowStatus.setStatus("current")
_AgentNtpConfigGroup_ObjectIdentity = ObjectIdentity
agentNtpConfigGroup = _AgentNtpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 14)
)


class _AgentNtpPollingInterval_Type(Integer32):
    """Custom type agentNtpPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 604800),
    )


_AgentNtpPollingInterval_Type.__name__ = "Integer32"
_AgentNtpPollingInterval_Object = MibScalar
agentNtpPollingInterval = _AgentNtpPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 14, 1),
    _AgentNtpPollingInterval_Type()
)
agentNtpPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpPollingInterval.setStatus("current")
_AgentNtpServerTable_Object = MibTable
agentNtpServerTable = _AgentNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    agentNtpServerTable.setStatus("current")
_AgentNtpServerEntry_Object = MibTableRow
agentNtpServerEntry = _AgentNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 14, 2, 1)
)
agentNtpServerEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentNtpServerIndex"),
)
if mibBuilder.loadTexts:
    agentNtpServerEntry.setStatus("current")


class _AgentNtpServerIndex_Type(Integer32):
    """Custom type agentNtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AgentNtpServerIndex_Type.__name__ = "Integer32"
_AgentNtpServerIndex_Object = MibTableColumn
agentNtpServerIndex = _AgentNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 14, 2, 1, 1),
    _AgentNtpServerIndex_Type()
)
agentNtpServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpServerIndex.setStatus("current")
_AgentNtpServerAddress_Type = IpAddress
_AgentNtpServerAddress_Object = MibTableColumn
agentNtpServerAddress = _AgentNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 14, 2, 1, 2),
    _AgentNtpServerAddress_Type()
)
agentNtpServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpServerAddress.setStatus("current")
_AgentNtpServerRowStatus_Type = RowStatus
_AgentNtpServerRowStatus_Object = MibTableColumn
agentNtpServerRowStatus = _AgentNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 14, 2, 1, 20),
    _AgentNtpServerRowStatus_Type()
)
agentNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpServerRowStatus.setStatus("current")
_AgentDhcpConfigGroup_ObjectIdentity = ObjectIdentity
agentDhcpConfigGroup = _AgentDhcpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15)
)
_AgentDhcpScopeTable_Object = MibTable
agentDhcpScopeTable = _AgentDhcpScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    agentDhcpScopeTable.setStatus("current")
_AgentDhcpScopeEntry_Object = MibTableRow
agentDhcpScopeEntry = _AgentDhcpScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1)
)
agentDhcpScopeEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "agentDhcpScopeIndex"),
)
if mibBuilder.loadTexts:
    agentDhcpScopeEntry.setStatus("current")


class _AgentDhcpScopeIndex_Type(Unsigned32):
    """Custom type agentDhcpScopeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AgentDhcpScopeIndex_Type.__name__ = "Unsigned32"
_AgentDhcpScopeIndex_Object = MibTableColumn
agentDhcpScopeIndex = _AgentDhcpScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 1),
    _AgentDhcpScopeIndex_Type()
)
agentDhcpScopeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeIndex.setStatus("current")


class _AgentDhcpScopeName_Type(DisplayString):
    """Custom type agentDhcpScopeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 79),
    )


_AgentDhcpScopeName_Type.__name__ = "DisplayString"
_AgentDhcpScopeName_Object = MibTableColumn
agentDhcpScopeName = _AgentDhcpScopeName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 2),
    _AgentDhcpScopeName_Type()
)
agentDhcpScopeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeName.setStatus("current")


class _AgentDhcpScopeLeaseTime_Type(Integer32):
    """Custom type agentDhcpScopeLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 8640000),
    )


_AgentDhcpScopeLeaseTime_Type.__name__ = "Integer32"
_AgentDhcpScopeLeaseTime_Object = MibTableColumn
agentDhcpScopeLeaseTime = _AgentDhcpScopeLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 3),
    _AgentDhcpScopeLeaseTime_Type()
)
agentDhcpScopeLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeLeaseTime.setStatus("current")
_AgentDhcpScopeNetwork_Type = IpAddress
_AgentDhcpScopeNetwork_Object = MibTableColumn
agentDhcpScopeNetwork = _AgentDhcpScopeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 4),
    _AgentDhcpScopeNetwork_Type()
)
agentDhcpScopeNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeNetwork.setStatus("current")
_AgentDhcpScopeNetmask_Type = IpAddress
_AgentDhcpScopeNetmask_Object = MibTableColumn
agentDhcpScopeNetmask = _AgentDhcpScopeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 5),
    _AgentDhcpScopeNetmask_Type()
)
agentDhcpScopeNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeNetmask.setStatus("current")
_AgentDhcpScopePoolStartAddress_Type = IpAddress
_AgentDhcpScopePoolStartAddress_Object = MibTableColumn
agentDhcpScopePoolStartAddress = _AgentDhcpScopePoolStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 6),
    _AgentDhcpScopePoolStartAddress_Type()
)
agentDhcpScopePoolStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopePoolStartAddress.setStatus("current")
_AgentDhcpScopePoolEndAddress_Type = IpAddress
_AgentDhcpScopePoolEndAddress_Object = MibTableColumn
agentDhcpScopePoolEndAddress = _AgentDhcpScopePoolEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 7),
    _AgentDhcpScopePoolEndAddress_Type()
)
agentDhcpScopePoolEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopePoolEndAddress.setStatus("current")
_AgentDhcpScopeDefaultRouterAddress1_Type = IpAddress
_AgentDhcpScopeDefaultRouterAddress1_Object = MibTableColumn
agentDhcpScopeDefaultRouterAddress1 = _AgentDhcpScopeDefaultRouterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 8),
    _AgentDhcpScopeDefaultRouterAddress1_Type()
)
agentDhcpScopeDefaultRouterAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeDefaultRouterAddress1.setStatus("current")
_AgentDhcpScopeDefaultRouterAddress2_Type = IpAddress
_AgentDhcpScopeDefaultRouterAddress2_Object = MibTableColumn
agentDhcpScopeDefaultRouterAddress2 = _AgentDhcpScopeDefaultRouterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 9),
    _AgentDhcpScopeDefaultRouterAddress2_Type()
)
agentDhcpScopeDefaultRouterAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeDefaultRouterAddress2.setStatus("current")
_AgentDhcpScopeDefaultRouterAddress3_Type = IpAddress
_AgentDhcpScopeDefaultRouterAddress3_Object = MibTableColumn
agentDhcpScopeDefaultRouterAddress3 = _AgentDhcpScopeDefaultRouterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 10),
    _AgentDhcpScopeDefaultRouterAddress3_Type()
)
agentDhcpScopeDefaultRouterAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeDefaultRouterAddress3.setStatus("current")


class _AgentDhcpScopeDnsDomainName_Type(DisplayString):
    """Custom type agentDhcpScopeDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AgentDhcpScopeDnsDomainName_Type.__name__ = "DisplayString"
_AgentDhcpScopeDnsDomainName_Object = MibTableColumn
agentDhcpScopeDnsDomainName = _AgentDhcpScopeDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 11),
    _AgentDhcpScopeDnsDomainName_Type()
)
agentDhcpScopeDnsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeDnsDomainName.setStatus("current")
_AgentDhcpScopeDnsServerAddress1_Type = IpAddress
_AgentDhcpScopeDnsServerAddress1_Object = MibTableColumn
agentDhcpScopeDnsServerAddress1 = _AgentDhcpScopeDnsServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 12),
    _AgentDhcpScopeDnsServerAddress1_Type()
)
agentDhcpScopeDnsServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeDnsServerAddress1.setStatus("current")
_AgentDhcpScopeDnsServerAddress2_Type = IpAddress
_AgentDhcpScopeDnsServerAddress2_Object = MibTableColumn
agentDhcpScopeDnsServerAddress2 = _AgentDhcpScopeDnsServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 13),
    _AgentDhcpScopeDnsServerAddress2_Type()
)
agentDhcpScopeDnsServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeDnsServerAddress2.setStatus("current")
_AgentDhcpScopeDnsServerAddress3_Type = IpAddress
_AgentDhcpScopeDnsServerAddress3_Object = MibTableColumn
agentDhcpScopeDnsServerAddress3 = _AgentDhcpScopeDnsServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 14),
    _AgentDhcpScopeDnsServerAddress3_Type()
)
agentDhcpScopeDnsServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeDnsServerAddress3.setStatus("current")
_AgentDhcpScopeNetbiosNameServerAddress1_Type = IpAddress
_AgentDhcpScopeNetbiosNameServerAddress1_Object = MibTableColumn
agentDhcpScopeNetbiosNameServerAddress1 = _AgentDhcpScopeNetbiosNameServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 15),
    _AgentDhcpScopeNetbiosNameServerAddress1_Type()
)
agentDhcpScopeNetbiosNameServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeNetbiosNameServerAddress1.setStatus("current")
_AgentDhcpScopeNetbiosNameServerAddress2_Type = IpAddress
_AgentDhcpScopeNetbiosNameServerAddress2_Object = MibTableColumn
agentDhcpScopeNetbiosNameServerAddress2 = _AgentDhcpScopeNetbiosNameServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 16),
    _AgentDhcpScopeNetbiosNameServerAddress2_Type()
)
agentDhcpScopeNetbiosNameServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeNetbiosNameServerAddress2.setStatus("current")
_AgentDhcpScopeNetbiosNameServerAddress3_Type = IpAddress
_AgentDhcpScopeNetbiosNameServerAddress3_Object = MibTableColumn
agentDhcpScopeNetbiosNameServerAddress3 = _AgentDhcpScopeNetbiosNameServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 17),
    _AgentDhcpScopeNetbiosNameServerAddress3_Type()
)
agentDhcpScopeNetbiosNameServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeNetbiosNameServerAddress3.setStatus("current")


class _AgentDhcpScopeState_Type(Integer32):
    """Custom type agentDhcpScopeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentDhcpScopeState_Type.__name__ = "Integer32"
_AgentDhcpScopeState_Object = MibTableColumn
agentDhcpScopeState = _AgentDhcpScopeState_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 18),
    _AgentDhcpScopeState_Type()
)
agentDhcpScopeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeState.setStatus("current")
_AgentDhcpScopeRowStatus_Type = RowStatus
_AgentDhcpScopeRowStatus_Object = MibTableColumn
agentDhcpScopeRowStatus = _AgentDhcpScopeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 2, 15, 1, 1, 30),
    _AgentDhcpScopeRowStatus_Type()
)
agentDhcpScopeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentDhcpScopeRowStatus.setStatus("current")
_AgentSystemGroup_ObjectIdentity = ObjectIdentity
agentSystemGroup = _AgentSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3)
)


class _AgentSaveConfig_Type(Integer32):
    """Custom type agentSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSaveConfig_Type.__name__ = "Integer32"
_AgentSaveConfig_Object = MibScalar
agentSaveConfig = _AgentSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 1),
    _AgentSaveConfig_Type()
)
agentSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSaveConfig.setStatus("current")


class _AgentClearConfig_Type(Integer32):
    """Custom type agentClearConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearConfig_Type.__name__ = "Integer32"
_AgentClearConfig_Object = MibScalar
agentClearConfig = _AgentClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 2),
    _AgentClearConfig_Type()
)
agentClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearConfig.setStatus("current")


class _AgentClearLags_Type(Integer32):
    """Custom type agentClearLags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearLags_Type.__name__ = "Integer32"
_AgentClearLags_Object = MibScalar
agentClearLags = _AgentClearLags_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 3),
    _AgentClearLags_Type()
)
agentClearLags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearLags.setStatus("current")


class _AgentClearLoginSessions_Type(Integer32):
    """Custom type agentClearLoginSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearLoginSessions_Type.__name__ = "Integer32"
_AgentClearLoginSessions_Object = MibScalar
agentClearLoginSessions = _AgentClearLoginSessions_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 4),
    _AgentClearLoginSessions_Type()
)
agentClearLoginSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearLoginSessions.setStatus("current")


class _AgentClearPortStats_Type(Integer32):
    """Custom type agentClearPortStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearPortStats_Type.__name__ = "Integer32"
_AgentClearPortStats_Object = MibScalar
agentClearPortStats = _AgentClearPortStats_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 6),
    _AgentClearPortStats_Type()
)
agentClearPortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearPortStats.setStatus("current")


class _AgentClearSwitchStats_Type(Integer32):
    """Custom type agentClearSwitchStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearSwitchStats_Type.__name__ = "Integer32"
_AgentClearSwitchStats_Object = MibScalar
agentClearSwitchStats = _AgentClearSwitchStats_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 7),
    _AgentClearSwitchStats_Type()
)
agentClearSwitchStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearSwitchStats.setStatus("current")


class _AgentClearTrapLog_Type(Integer32):
    """Custom type agentClearTrapLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentClearTrapLog_Type.__name__ = "Integer32"
_AgentClearTrapLog_Object = MibScalar
agentClearTrapLog = _AgentClearTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 8),
    _AgentClearTrapLog_Type()
)
agentClearTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentClearTrapLog.setStatus("current")


class _AgentResetSystem_Type(Integer32):
    """Custom type agentResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentResetSystem_Type.__name__ = "Integer32"
_AgentResetSystem_Object = MibScalar
agentResetSystem = _AgentResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 3, 10),
    _AgentResetSystem_Type()
)
agentResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentResetSystem.setStatus("current")
_Stats_ObjectIdentity = ObjectIdentity
stats = _Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4)
)
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("current")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1)
)
portStatsEntry.setIndexNames(
    (0, "AIRESPACE-SWITCHING-MIB", "portStatsIndex"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("current")


class _PortStatsIndex_Type(Integer32):
    """Custom type portStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortStatsIndex_Type.__name__ = "Integer32"
_PortStatsIndex_Object = MibTableColumn
portStatsIndex = _PortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 1),
    _PortStatsIndex_Type()
)
portStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsIndex.setStatus("current")
_PortStatsPktsTx64Octets_Type = Counter32
_PortStatsPktsTx64Octets_Object = MibTableColumn
portStatsPktsTx64Octets = _PortStatsPktsTx64Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 2),
    _PortStatsPktsTx64Octets_Type()
)
portStatsPktsTx64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTx64Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTx64Octets.setUnits("Packets")
_PortStatsPktsTx65to127Octets_Type = Counter32
_PortStatsPktsTx65to127Octets_Object = MibTableColumn
portStatsPktsTx65to127Octets = _PortStatsPktsTx65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 3),
    _PortStatsPktsTx65to127Octets_Type()
)
portStatsPktsTx65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTx65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTx65to127Octets.setUnits("Packets")
_PortStatsPktsTx128to255Octets_Type = Counter32
_PortStatsPktsTx128to255Octets_Object = MibTableColumn
portStatsPktsTx128to255Octets = _PortStatsPktsTx128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 4),
    _PortStatsPktsTx128to255Octets_Type()
)
portStatsPktsTx128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTx128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTx128to255Octets.setUnits("Packets")
_PortStatsPktsTx256to511Octets_Type = Counter32
_PortStatsPktsTx256to511Octets_Object = MibTableColumn
portStatsPktsTx256to511Octets = _PortStatsPktsTx256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 5),
    _PortStatsPktsTx256to511Octets_Type()
)
portStatsPktsTx256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTx256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTx256to511Octets.setUnits("Packets")
_PortStatsPktsTx512to1023Octets_Type = Counter32
_PortStatsPktsTx512to1023Octets_Object = MibTableColumn
portStatsPktsTx512to1023Octets = _PortStatsPktsTx512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 6),
    _PortStatsPktsTx512to1023Octets_Type()
)
portStatsPktsTx512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTx512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTx512to1023Octets.setUnits("Packets")
_PortStatsPktsTx1024to1518Octets_Type = Counter32
_PortStatsPktsTx1024to1518Octets_Object = MibTableColumn
portStatsPktsTx1024to1518Octets = _PortStatsPktsTx1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 7),
    _PortStatsPktsTx1024to1518Octets_Type()
)
portStatsPktsTx1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTx1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTx1024to1518Octets.setUnits("Packets")
_PortStatsPktsRx1519to1530Octets_Type = Counter32
_PortStatsPktsRx1519to1530Octets_Object = MibTableColumn
portStatsPktsRx1519to1530Octets = _PortStatsPktsRx1519to1530Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 8),
    _PortStatsPktsRx1519to1530Octets_Type()
)
portStatsPktsRx1519to1530Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsRx1519to1530Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsRx1519to1530Octets.setUnits("Packets")
_PortStatsPktsTx1519to1530Octets_Type = Counter32
_PortStatsPktsTx1519to1530Octets_Object = MibTableColumn
portStatsPktsTx1519to1530Octets = _PortStatsPktsTx1519to1530Octets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 9),
    _PortStatsPktsTx1519to1530Octets_Type()
)
portStatsPktsTx1519to1530Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTx1519to1530Octets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTx1519to1530Octets.setUnits("Packets")
_PortStatsPktsTxOversizeOctets_Type = Counter32
_PortStatsPktsTxOversizeOctets_Object = MibTableColumn
portStatsPktsTxOversizeOctets = _PortStatsPktsTxOversizeOctets_Object(
    (1, 3, 6, 1, 4, 1, 14179, 1, 4, 1, 1, 30),
    _PortStatsPktsTxOversizeOctets_Type()
)
portStatsPktsTxOversizeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsTxOversizeOctets.setStatus("current")
if mibBuilder.loadTexts:
    portStatsPktsTxOversizeOctets.setUnits("Packets")
_SwitchingTraps_ObjectIdentity = ObjectIdentity
switchingTraps = _SwitchingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50)
)
_BsnSwitchingGroups_ObjectIdentity = ObjectIdentity
bsnSwitchingGroups = _BsnSwitchingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 51)
)
_BsnSwitchingCompliances_ObjectIdentity = ObjectIdentity
bsnSwitchingCompliances = _BsnSwitchingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 1, 52)
)

# Managed Objects groups

bsnSwitchingAgentInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 1, 51, 1)
)
bsnSwitchingAgentInfoGroup.setObjects(
      *(("AIRESPACE-SWITCHING-MIB", "agentInventorySysDescription"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryMachineType"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryMachineModel"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventorySerialNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryMaintenanceLevel"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryBurnedInMacAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryOperatingSystem"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryManufacturerName"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryProductName"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryProductVersion"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryIsGigECardPresent"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryIsCryptoCardPresent"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryIsForeignAPSupported"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryMaxNumberOfAPsSupported"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryIsCryptoCard2Present"),
        ("AIRESPACE-SWITCHING-MIB", "agentInventoryFipsModeEnabled"),
        ("AIRESPACE-SWITCHING-MIB", "agentTrapLogTotal"),
        ("AIRESPACE-SWITCHING-MIB", "agentTrapLogTotalSinceLastViewed"),
        ("AIRESPACE-SWITCHING-MIB", "agentTrapLogIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentTrapLogSystemTime"),
        ("AIRESPACE-SWITCHING-MIB", "agentTrapLogTrap"),
        ("AIRESPACE-SWITCHING-MIB", "agentRadioUpDownTrapCount"),
        ("AIRESPACE-SWITCHING-MIB", "agentApAssociateDisassociateTrapCount"),
        ("AIRESPACE-SWITCHING-MIB", "agentApLoadProfileFailTrapCount"),
        ("AIRESPACE-SWITCHING-MIB", "agentApNoiseProfileFailTrapCount"),
        ("AIRESPACE-SWITCHING-MIB", "agentApInterferenceProfileFailTrapCount"),
        ("AIRESPACE-SWITCHING-MIB", "agentApCoverageProfileFailTrapCount"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchInfoLwappTransportMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchInfoPowerSupply1Present"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchInfoPowerSupply1Operational"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchInfoPowerSupply2Present"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchInfoPowerSupply2Operational"),
        ("AIRESPACE-SWITCHING-MIB", "agentCurrentCPUUtilization"),
        ("AIRESPACE-SWITCHING-MIB", "agentTotalMemory"),
        ("AIRESPACE-SWITCHING-MIB", "agentFreeMemory"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpDeviceName"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpSlotNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpPortNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpPeerPortNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpPeerIpAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpControllerTableChecksum"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpControllerInfoSlotNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpControllerInfoPortNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentWcpControllerInfoIpAddress"))
)
if mibBuilder.loadTexts:
    bsnSwitchingAgentInfoGroup.setStatus("current")

bsnSwitchingAgentConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 1, 51, 2)
)
bsnSwitchingAgentConfigGroup.setObjects(
      *(("AIRESPACE-SWITCHING-MIB", "agentLoginSessionIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentLoginSessionUserName"),
        ("AIRESPACE-SWITCHING-MIB", "agentLoginSessionIPAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentLoginSessionConnectionType"),
        ("AIRESPACE-SWITCHING-MIB", "agentLoginSessionIdleTime"),
        ("AIRESPACE-SWITCHING-MIB", "agentLoginSessionSessionTime"),
        ("AIRESPACE-SWITCHING-MIB", "agentLoginSessionStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentTelnetLoginTimeout"),
        ("AIRESPACE-SWITCHING-MIB", "agentTelnetMaxSessions"),
        ("AIRESPACE-SWITCHING-MIB", "agentTelnetAllowNewMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSSHAllowNewMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSerialTimeout"),
        ("AIRESPACE-SWITCHING-MIB", "agentSerialBaudrate"),
        ("AIRESPACE-SWITCHING-MIB", "agentSerialCharacterSize"),
        ("AIRESPACE-SWITCHING-MIB", "agentSerialHWFlowControlMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSerialStopBits"),
        ("AIRESPACE-SWITCHING-MIB", "agentSerialParityType"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkIPAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkSubnetMask"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkDefaultGateway"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkBurnedInMacAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkConfigProtocol"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkWebMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkSecureWebMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkMulticastMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkDsPortNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkUserIdleTimeout"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkArpTimeout"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkManagementVlan"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkAllowMgmtViaWireless"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkBroadcastSsidMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkSecureWebPassword"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkWebAdminCertType"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkWebAuthCertRegenerateCmdInvoke"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkWebAdminCertRegenerateCmdInvoke"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkWebAuthCertType"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkRouteIPAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkRouteIPNetmask"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkRouteGateway"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkRouteStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkPeerToPeerBlockingMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkMulticastGroupAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceName"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceVlanId"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceType"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceMacAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceIPAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceIPNetmask"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceIPGateway"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfacePortNo"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfacePrimaryDhcpAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceSecondaryDhcpAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceDhcpProtocol"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceDnsHostName"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceAclName"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceAPManagementFeature"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceActivePortNo"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceBackupPortNo"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceVlanQuarantine"),
        ("AIRESPACE-SWITCHING-MIB", "agentInterfaceRowStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentNtpPollingInterval"),
        ("AIRESPACE-SWITCHING-MIB", "agentNtpServerIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentNtpServerAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentNtpServerRowStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeName"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeLeaseTime"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeNetwork"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeNetmask"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopePoolStartAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopePoolEndAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeDefaultRouterAddress1"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeDefaultRouterAddress2"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeDefaultRouterAddress3"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeDnsDomainName"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeDnsServerAddress1"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeDnsServerAddress2"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeDnsServerAddress3"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeNetbiosNameServerAddress1"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeNetbiosNameServerAddress2"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeNetbiosNameServerAddress3"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeState"),
        ("AIRESPACE-SWITCHING-MIB", "agentDhcpScopeRowStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpTrapPortNumber"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpVersion1Status"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpVersion2cStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpCommunityName"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpCommunityIPAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpCommunityIPMask"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpCommunityAccessMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpCommunityEnabled"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpCommunityStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpTrapReceiverName"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpTrapReceiverIPAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpTrapReceiverEnabled"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpTrapReceiverStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpAuthenticationTrapFlag"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpLinkUpDownTrapFlag"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpMultipleUsersTrapFlag"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpSpanningTreeTrapFlag"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpVersion3Status"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserName"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserAccessMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserAuthenticationType"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserEncryptionType"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserAuthenticationPassword"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserEncryptionPassword"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpV3UserStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentSpanningTreeMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchAddressAgingTimeout"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchBroadcastControlMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchDot3FlowControlMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentSwitchLwappTransportMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferUploadMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferUploadServerIP"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferUploadPath"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferUploadFilename"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferUploadDataType"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferUploadStart"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferUploadStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferConfigurationFileEncryption"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferConfigurationFileEncryptionKey"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadServerIP"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadPath"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadFilename"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadDataType"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadStart"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadTftpMaxRetries"),
        ("AIRESPACE-SWITCHING-MIB", "agentTransferDownloadTftpTimeout"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortDot1dBasePort"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortIfIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortIanaType"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortSTPMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortSTPState"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortAdminMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortPhysicalMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortPhysicalStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortLinkTrapMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortClearStats"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortDefaultType"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortType"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortAutoNegAdminStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortDot3FlowControlMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortPowerMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortMirrorMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortMulticastApplianceMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortOperationalStatus"))
)
if mibBuilder.loadTexts:
    bsnSwitchingAgentConfigGroup.setStatus("current")

bsnSwitchingAgentSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 1, 51, 3)
)
bsnSwitchingAgentSystemGroup.setObjects(
      *(("AIRESPACE-SWITCHING-MIB", "agentSaveConfig"),
        ("AIRESPACE-SWITCHING-MIB", "agentClearConfig"),
        ("AIRESPACE-SWITCHING-MIB", "agentClearLags"),
        ("AIRESPACE-SWITCHING-MIB", "agentClearLoginSessions"),
        ("AIRESPACE-SWITCHING-MIB", "agentClearPortStats"),
        ("AIRESPACE-SWITCHING-MIB", "agentClearSwitchStats"),
        ("AIRESPACE-SWITCHING-MIB", "agentClearTrapLog"),
        ("AIRESPACE-SWITCHING-MIB", "agentResetSystem"))
)
if mibBuilder.loadTexts:
    bsnSwitchingAgentSystemGroup.setStatus("current")

bsnSwitchingAgentStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 1, 51, 4)
)
bsnSwitchingAgentStatsGroup.setObjects(
      *(("AIRESPACE-SWITCHING-MIB", "portStatsIndex"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTx64Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTx65to127Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTx128to255Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTx256to511Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTx512to1023Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTx1024to1518Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsRx1519to1530Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTx1519to1530Octets"),
        ("AIRESPACE-SWITCHING-MIB", "portStatsPktsTxOversizeOctets"))
)
if mibBuilder.loadTexts:
    bsnSwitchingAgentStatsGroup.setStatus("current")

bsnSwitchingObsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 1, 51, 5)
)
bsnSwitchingObsGroup.setObjects(
      *(("AIRESPACE-SWITCHING-MIB", "agentLagConfigCreate"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryName"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryLagIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryLinkTrap"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryAdminMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryStpMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryAddPort"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryDeletePort"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryPortsBitMask"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagDetailedLagIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagDetailedIfIndex"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagDetailedPortSpeed"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagConfigMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentServicePortIPAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentServicePortSubnetMask"),
        ("AIRESPACE-SWITCHING-MIB", "agentServicePortBurnedInMacAddress"),
        ("AIRESPACE-SWITCHING-MIB", "agentServicePortConfigProtocol"),
        ("AIRESPACE-SWITCHING-MIB", "agentSnmpBroadcastStormTrapFlag"),
        ("AIRESPACE-SWITCHING-MIB", "agentDot3adAggPort"),
        ("AIRESPACE-SWITCHING-MIB", "agentDot3adAggPortLACPMode"),
        ("AIRESPACE-SWITCHING-MIB", "agentNetworkGvrpStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortGvrpStatus"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortGarpJoinTime"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortGarpLeaveTime"),
        ("AIRESPACE-SWITCHING-MIB", "agentPortGarpLeaveAllTime"),
        ("AIRESPACE-SWITCHING-MIB", "agentLagSummaryFlushTimer"),
        ("AIRESPACE-SWITCHING-MIB", "agentServicePortDefaultGateway"))
)
if mibBuilder.loadTexts:
    bsnSwitchingObsGroup.setStatus("obsolete")


# Notification objects

multipleUsersTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 1)
)
if mibBuilder.loadTexts:
    multipleUsersTrap.setStatus(
        "current"
    )

broadcastStormStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 2)
)
if mibBuilder.loadTexts:
    broadcastStormStartTrap.setStatus(
        "current"
    )

broadcastStormEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 3)
)
if mibBuilder.loadTexts:
    broadcastStormEndTrap.setStatus(
        "current"
    )

linkFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 4)
)
if mibBuilder.loadTexts:
    linkFailureTrap.setStatus(
        "current"
    )

vlanRequestFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 5)
)
vlanRequestFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRequestFailureTrap.setStatus(
        "current"
    )

vlanDeleteLastTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 6)
)
vlanDeleteLastTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDeleteLastTrap.setStatus(
        "current"
    )

vlanDefaultCfgFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 7)
)
vlanDefaultCfgFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanDefaultCfgFailureTrap.setStatus(
        "current"
    )

vlanRestoreFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 8)
)
vlanRestoreFailureTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    vlanRestoreFailureTrap.setStatus(
        "current"
    )

fanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 9)
)
if mibBuilder.loadTexts:
    fanFailureTrap.setStatus(
        "current"
    )

stpInstanceNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 10)
)
stpInstanceNewRootTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    stpInstanceNewRootTrap.setStatus(
        "current"
    )

stpInstanceTopologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 11)
)
stpInstanceTopologyChangeTrap.setObjects(
    ("Q-BRIDGE-MIB", "dot1qVlanIndex")
)
if mibBuilder.loadTexts:
    stpInstanceTopologyChangeTrap.setStatus(
        "current"
    )

powerSupplyStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14179, 1, 50, 12)
)
if mibBuilder.loadTexts:
    powerSupplyStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups

bsnSwitchingTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 14179, 1, 51, 6)
)
bsnSwitchingTrap.setObjects(
      *(("AIRESPACE-SWITCHING-MIB", "multipleUsersTrap"),
        ("AIRESPACE-SWITCHING-MIB", "broadcastStormStartTrap"),
        ("AIRESPACE-SWITCHING-MIB", "broadcastStormEndTrap"),
        ("AIRESPACE-SWITCHING-MIB", "linkFailureTrap"),
        ("AIRESPACE-SWITCHING-MIB", "vlanRequestFailureTrap"),
        ("AIRESPACE-SWITCHING-MIB", "vlanDeleteLastTrap"),
        ("AIRESPACE-SWITCHING-MIB", "vlanDefaultCfgFailureTrap"),
        ("AIRESPACE-SWITCHING-MIB", "vlanRestoreFailureTrap"),
        ("AIRESPACE-SWITCHING-MIB", "fanFailureTrap"),
        ("AIRESPACE-SWITCHING-MIB", "stpInstanceNewRootTrap"),
        ("AIRESPACE-SWITCHING-MIB", "stpInstanceTopologyChangeTrap"),
        ("AIRESPACE-SWITCHING-MIB", "powerSupplyStatusChangeTrap"))
)
if mibBuilder.loadTexts:
    bsnSwitchingTrap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bsnSwitchingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14179, 1, 52, 1)
)
if mibBuilder.loadTexts:
    bsnSwitchingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRESPACE-SWITCHING-MIB",
    **{"bsnSwitching": bsnSwitching,
       "agentInfoGroup": agentInfoGroup,
       "agentInventoryGroup": agentInventoryGroup,
       "agentInventorySysDescription": agentInventorySysDescription,
       "agentInventoryMachineType": agentInventoryMachineType,
       "agentInventoryMachineModel": agentInventoryMachineModel,
       "agentInventorySerialNumber": agentInventorySerialNumber,
       "agentInventoryMaintenanceLevel": agentInventoryMaintenanceLevel,
       "agentInventoryBurnedInMacAddress": agentInventoryBurnedInMacAddress,
       "agentInventoryOperatingSystem": agentInventoryOperatingSystem,
       "agentInventoryManufacturerName": agentInventoryManufacturerName,
       "agentInventoryProductName": agentInventoryProductName,
       "agentInventoryProductVersion": agentInventoryProductVersion,
       "agentInventoryIsGigECardPresent": agentInventoryIsGigECardPresent,
       "agentInventoryIsCryptoCardPresent": agentInventoryIsCryptoCardPresent,
       "agentInventoryIsForeignAPSupported": agentInventoryIsForeignAPSupported,
       "agentInventoryMaxNumberOfAPsSupported": agentInventoryMaxNumberOfAPsSupported,
       "agentInventoryIsCryptoCard2Present": agentInventoryIsCryptoCard2Present,
       "agentInventoryFipsModeEnabled": agentInventoryFipsModeEnabled,
       "agentTrapLogGroup": agentTrapLogGroup,
       "agentTrapLogTotal": agentTrapLogTotal,
       "agentTrapLogTotalSinceLastViewed": agentTrapLogTotalSinceLastViewed,
       "agentTrapLogTable": agentTrapLogTable,
       "agentTrapLogEntry": agentTrapLogEntry,
       "agentTrapLogIndex": agentTrapLogIndex,
       "agentTrapLogSystemTime": agentTrapLogSystemTime,
       "agentTrapLogTrap": agentTrapLogTrap,
       "agentRadioUpDownTrapCount": agentRadioUpDownTrapCount,
       "agentApAssociateDisassociateTrapCount": agentApAssociateDisassociateTrapCount,
       "agentApLoadProfileFailTrapCount": agentApLoadProfileFailTrapCount,
       "agentApNoiseProfileFailTrapCount": agentApNoiseProfileFailTrapCount,
       "agentApInterferenceProfileFailTrapCount": agentApInterferenceProfileFailTrapCount,
       "agentApCoverageProfileFailTrapCount": agentApCoverageProfileFailTrapCount,
       "agentSwitchInfoGroup": agentSwitchInfoGroup,
       "agentSwitchInfoLwappTransportMode": agentSwitchInfoLwappTransportMode,
       "agentSwitchInfoPowerSupply1Present": agentSwitchInfoPowerSupply1Present,
       "agentSwitchInfoPowerSupply1Operational": agentSwitchInfoPowerSupply1Operational,
       "agentSwitchInfoPowerSupply2Present": agentSwitchInfoPowerSupply2Present,
       "agentSwitchInfoPowerSupply2Operational": agentSwitchInfoPowerSupply2Operational,
       "agentProductGroup": agentProductGroup,
       "productGroup1": productGroup1,
       "productGroup2": productGroup2,
       "productGroup3": productGroup3,
       "productGroup4": productGroup4,
       "agentResourceInfoGroup": agentResourceInfoGroup,
       "agentCurrentCPUUtilization": agentCurrentCPUUtilization,
       "agentTotalMemory": agentTotalMemory,
       "agentFreeMemory": agentFreeMemory,
       "agentWcpInfoGroup": agentWcpInfoGroup,
       "agentWcpDeviceName": agentWcpDeviceName,
       "agentWcpSlotNumber": agentWcpSlotNumber,
       "agentWcpPortNumber": agentWcpPortNumber,
       "agentWcpPeerPortNumber": agentWcpPeerPortNumber,
       "agentWcpPeerIpAddress": agentWcpPeerIpAddress,
       "agentWcpControllerTableChecksum": agentWcpControllerTableChecksum,
       "agentWcpControllerInfoTable": agentWcpControllerInfoTable,
       "agentWcpControllerInfoEntry": agentWcpControllerInfoEntry,
       "agentWcpControllerInfoSlotNumber": agentWcpControllerInfoSlotNumber,
       "agentWcpControllerInfoPortNumber": agentWcpControllerInfoPortNumber,
       "agentWcpControllerInfoIpAddress": agentWcpControllerInfoIpAddress,
       "agentConfigGroup": agentConfigGroup,
       "agentCLIConfigGroup": agentCLIConfigGroup,
       "agentLoginSessionTable": agentLoginSessionTable,
       "agentLoginSessionEntry": agentLoginSessionEntry,
       "agentLoginSessionIndex": agentLoginSessionIndex,
       "agentLoginSessionUserName": agentLoginSessionUserName,
       "agentLoginSessionIPAddress": agentLoginSessionIPAddress,
       "agentLoginSessionConnectionType": agentLoginSessionConnectionType,
       "agentLoginSessionIdleTime": agentLoginSessionIdleTime,
       "agentLoginSessionSessionTime": agentLoginSessionSessionTime,
       "agentLoginSessionStatus": agentLoginSessionStatus,
       "agentTelnetConfigGroup": agentTelnetConfigGroup,
       "agentTelnetLoginTimeout": agentTelnetLoginTimeout,
       "agentTelnetMaxSessions": agentTelnetMaxSessions,
       "agentTelnetAllowNewMode": agentTelnetAllowNewMode,
       "agentSSHAllowNewMode": agentSSHAllowNewMode,
       "agentSerialGroup": agentSerialGroup,
       "agentSerialTimeout": agentSerialTimeout,
       "agentSerialBaudrate": agentSerialBaudrate,
       "agentSerialCharacterSize": agentSerialCharacterSize,
       "agentSerialHWFlowControlMode": agentSerialHWFlowControlMode,
       "agentSerialStopBits": agentSerialStopBits,
       "agentSerialParityType": agentSerialParityType,
       "agentLagConfigGroup": agentLagConfigGroup,
       "agentLagConfigCreate": agentLagConfigCreate,
       "agentLagSummaryConfigTable": agentLagSummaryConfigTable,
       "agentLagSummaryConfigEntry": agentLagSummaryConfigEntry,
       "agentLagSummaryName": agentLagSummaryName,
       "agentLagSummaryLagIndex": agentLagSummaryLagIndex,
       "agentLagSummaryFlushTimer": agentLagSummaryFlushTimer,
       "agentLagSummaryLinkTrap": agentLagSummaryLinkTrap,
       "agentLagSummaryAdminMode": agentLagSummaryAdminMode,
       "agentLagSummaryStpMode": agentLagSummaryStpMode,
       "agentLagSummaryAddPort": agentLagSummaryAddPort,
       "agentLagSummaryDeletePort": agentLagSummaryDeletePort,
       "agentLagSummaryPortsBitMask": agentLagSummaryPortsBitMask,
       "agentLagSummaryStatus": agentLagSummaryStatus,
       "agentLagDetailedConfigTable": agentLagDetailedConfigTable,
       "agentLagDetailedConfigEntry": agentLagDetailedConfigEntry,
       "agentLagDetailedLagIndex": agentLagDetailedLagIndex,
       "agentLagDetailedIfIndex": agentLagDetailedIfIndex,
       "agentLagDetailedPortSpeed": agentLagDetailedPortSpeed,
       "agentLagConfigMode": agentLagConfigMode,
       "agentNetworkConfigGroup": agentNetworkConfigGroup,
       "agentNetworkIPAddress": agentNetworkIPAddress,
       "agentNetworkSubnetMask": agentNetworkSubnetMask,
       "agentNetworkDefaultGateway": agentNetworkDefaultGateway,
       "agentNetworkBurnedInMacAddress": agentNetworkBurnedInMacAddress,
       "agentNetworkConfigProtocol": agentNetworkConfigProtocol,
       "agentNetworkWebMode": agentNetworkWebMode,
       "agentNetworkSecureWebMode": agentNetworkSecureWebMode,
       "agentNetworkMulticastMode": agentNetworkMulticastMode,
       "agentNetworkDsPortNumber": agentNetworkDsPortNumber,
       "agentNetworkUserIdleTimeout": agentNetworkUserIdleTimeout,
       "agentNetworkArpTimeout": agentNetworkArpTimeout,
       "agentNetworkManagementVlan": agentNetworkManagementVlan,
       "agentNetworkGvrpStatus": agentNetworkGvrpStatus,
       "agentNetworkAllowMgmtViaWireless": agentNetworkAllowMgmtViaWireless,
       "agentNetworkBroadcastSsidMode": agentNetworkBroadcastSsidMode,
       "agentNetworkSecureWebPassword": agentNetworkSecureWebPassword,
       "agentNetworkWebAdminCertType": agentNetworkWebAdminCertType,
       "agentNetworkWebAdminCertRegenerateCmdInvoke": agentNetworkWebAdminCertRegenerateCmdInvoke,
       "agentNetworkWebAuthCertType": agentNetworkWebAuthCertType,
       "agentNetworkWebAuthCertRegenerateCmdInvoke": agentNetworkWebAuthCertRegenerateCmdInvoke,
       "agentNetworkRouteConfigTable": agentNetworkRouteConfigTable,
       "agentNetworkRouteConfigEntry": agentNetworkRouteConfigEntry,
       "agentNetworkRouteIPAddress": agentNetworkRouteIPAddress,
       "agentNetworkRouteIPNetmask": agentNetworkRouteIPNetmask,
       "agentNetworkRouteGateway": agentNetworkRouteGateway,
       "agentNetworkRouteStatus": agentNetworkRouteStatus,
       "agentNetworkPeerToPeerBlockingMode": agentNetworkPeerToPeerBlockingMode,
       "agentNetworkMulticastGroupAddress": agentNetworkMulticastGroupAddress,
       "agentServicePortConfigGroup": agentServicePortConfigGroup,
       "agentServicePortIPAddress": agentServicePortIPAddress,
       "agentServicePortSubnetMask": agentServicePortSubnetMask,
       "agentServicePortDefaultGateway": agentServicePortDefaultGateway,
       "agentServicePortBurnedInMacAddress": agentServicePortBurnedInMacAddress,
       "agentServicePortConfigProtocol": agentServicePortConfigProtocol,
       "agentSnmpConfigGroup": agentSnmpConfigGroup,
       "agentSnmpTrapPortNumber": agentSnmpTrapPortNumber,
       "agentSnmpVersion1Status": agentSnmpVersion1Status,
       "agentSnmpVersion2cStatus": agentSnmpVersion2cStatus,
       "agentSnmpCommunityConfigTable": agentSnmpCommunityConfigTable,
       "agentSnmpCommunityConfigEntry": agentSnmpCommunityConfigEntry,
       "agentSnmpCommunityName": agentSnmpCommunityName,
       "agentSnmpCommunityIPAddress": agentSnmpCommunityIPAddress,
       "agentSnmpCommunityIPMask": agentSnmpCommunityIPMask,
       "agentSnmpCommunityAccessMode": agentSnmpCommunityAccessMode,
       "agentSnmpCommunityEnabled": agentSnmpCommunityEnabled,
       "agentSnmpCommunityStatus": agentSnmpCommunityStatus,
       "agentSnmpTrapReceiverConfigTable": agentSnmpTrapReceiverConfigTable,
       "agentSnmpTrapReceiverConfigEntry": agentSnmpTrapReceiverConfigEntry,
       "agentSnmpTrapReceiverName": agentSnmpTrapReceiverName,
       "agentSnmpTrapReceiverIPAddress": agentSnmpTrapReceiverIPAddress,
       "agentSnmpTrapReceiverEnabled": agentSnmpTrapReceiverEnabled,
       "agentSnmpTrapReceiverStatus": agentSnmpTrapReceiverStatus,
       "agentSnmpTrapFlagsConfigGroup": agentSnmpTrapFlagsConfigGroup,
       "agentSnmpAuthenticationTrapFlag": agentSnmpAuthenticationTrapFlag,
       "agentSnmpLinkUpDownTrapFlag": agentSnmpLinkUpDownTrapFlag,
       "agentSnmpMultipleUsersTrapFlag": agentSnmpMultipleUsersTrapFlag,
       "agentSnmpSpanningTreeTrapFlag": agentSnmpSpanningTreeTrapFlag,
       "agentSnmpBroadcastStormTrapFlag": agentSnmpBroadcastStormTrapFlag,
       "agentSnmpV3ConfigGroup": agentSnmpV3ConfigGroup,
       "agentSnmpVersion3Status": agentSnmpVersion3Status,
       "agentSnmpV3UserConfigTable": agentSnmpV3UserConfigTable,
       "agentSnmpV3UserConfigEntry": agentSnmpV3UserConfigEntry,
       "agentSnmpV3UserName": agentSnmpV3UserName,
       "agentSnmpV3UserAccessMode": agentSnmpV3UserAccessMode,
       "agentSnmpV3UserAuthenticationType": agentSnmpV3UserAuthenticationType,
       "agentSnmpV3UserEncryptionType": agentSnmpV3UserEncryptionType,
       "agentSnmpV3UserAuthenticationPassword": agentSnmpV3UserAuthenticationPassword,
       "agentSnmpV3UserEncryptionPassword": agentSnmpV3UserEncryptionPassword,
       "agentSnmpV3UserStatus": agentSnmpV3UserStatus,
       "agentSpanningTreeConfigGroup": agentSpanningTreeConfigGroup,
       "agentSpanningTreeMode": agentSpanningTreeMode,
       "agentSwitchConfigGroup": agentSwitchConfigGroup,
       "agentSwitchBroadcastControlMode": agentSwitchBroadcastControlMode,
       "agentSwitchDot3FlowControlMode": agentSwitchDot3FlowControlMode,
       "agentSwitchAddressAgingTimeoutTable": agentSwitchAddressAgingTimeoutTable,
       "agentSwitchAddressAgingTimeoutEntry": agentSwitchAddressAgingTimeoutEntry,
       "agentSwitchAddressAgingTimeout": agentSwitchAddressAgingTimeout,
       "agentSwitchLwappTransportMode": agentSwitchLwappTransportMode,
       "agentTransferConfigGroup": agentTransferConfigGroup,
       "agentTransferUploadGroup": agentTransferUploadGroup,
       "agentTransferUploadMode": agentTransferUploadMode,
       "agentTransferUploadServerIP": agentTransferUploadServerIP,
       "agentTransferUploadPath": agentTransferUploadPath,
       "agentTransferUploadFilename": agentTransferUploadFilename,
       "agentTransferUploadDataType": agentTransferUploadDataType,
       "agentTransferUploadStart": agentTransferUploadStart,
       "agentTransferUploadStatus": agentTransferUploadStatus,
       "agentTransferDownloadGroup": agentTransferDownloadGroup,
       "agentTransferDownloadMode": agentTransferDownloadMode,
       "agentTransferDownloadServerIP": agentTransferDownloadServerIP,
       "agentTransferDownloadPath": agentTransferDownloadPath,
       "agentTransferDownloadFilename": agentTransferDownloadFilename,
       "agentTransferDownloadDataType": agentTransferDownloadDataType,
       "agentTransferDownloadStart": agentTransferDownloadStart,
       "agentTransferDownloadStatus": agentTransferDownloadStatus,
       "agentTransferDownloadTftpMaxRetries": agentTransferDownloadTftpMaxRetries,
       "agentTransferDownloadTftpTimeout": agentTransferDownloadTftpTimeout,
       "agentTransferConfigurationFileEncryption": agentTransferConfigurationFileEncryption,
       "agentTransferConfigurationFileEncryptionKey": agentTransferConfigurationFileEncryptionKey,
       "agentDot3adAggPortTable": agentDot3adAggPortTable,
       "agentDot3adAggPortEntry": agentDot3adAggPortEntry,
       "agentDot3adAggPort": agentDot3adAggPort,
       "agentDot3adAggPortLACPMode": agentDot3adAggPortLACPMode,
       "agentPortConfigTable": agentPortConfigTable,
       "agentPortConfigEntry": agentPortConfigEntry,
       "agentPortDot1dBasePort": agentPortDot1dBasePort,
       "agentPortIfIndex": agentPortIfIndex,
       "agentPortIanaType": agentPortIanaType,
       "agentPortSTPMode": agentPortSTPMode,
       "agentPortSTPState": agentPortSTPState,
       "agentPortAdminMode": agentPortAdminMode,
       "agentPortPhysicalMode": agentPortPhysicalMode,
       "agentPortPhysicalStatus": agentPortPhysicalStatus,
       "agentPortLinkTrapMode": agentPortLinkTrapMode,
       "agentPortClearStats": agentPortClearStats,
       "agentPortDefaultType": agentPortDefaultType,
       "agentPortType": agentPortType,
       "agentPortAutoNegAdminStatus": agentPortAutoNegAdminStatus,
       "agentPortDot3FlowControlMode": agentPortDot3FlowControlMode,
       "agentPortPowerMode": agentPortPowerMode,
       "agentPortGvrpStatus": agentPortGvrpStatus,
       "agentPortGarpJoinTime": agentPortGarpJoinTime,
       "agentPortGarpLeaveTime": agentPortGarpLeaveTime,
       "agentPortGarpLeaveAllTime": agentPortGarpLeaveAllTime,
       "agentPortMirrorMode": agentPortMirrorMode,
       "agentPortMulticastApplianceMode": agentPortMulticastApplianceMode,
       "agentPortOperationalStatus": agentPortOperationalStatus,
       "agentInterfaceConfigTable": agentInterfaceConfigTable,
       "agentInterfaceConfigEntry": agentInterfaceConfigEntry,
       "agentInterfaceName": agentInterfaceName,
       "agentInterfaceVlanId": agentInterfaceVlanId,
       "agentInterfaceType": agentInterfaceType,
       "agentInterfaceMacAddress": agentInterfaceMacAddress,
       "agentInterfaceIPAddress": agentInterfaceIPAddress,
       "agentInterfaceIPNetmask": agentInterfaceIPNetmask,
       "agentInterfaceIPGateway": agentInterfaceIPGateway,
       "agentInterfacePortNo": agentInterfacePortNo,
       "agentInterfacePrimaryDhcpAddress": agentInterfacePrimaryDhcpAddress,
       "agentInterfaceSecondaryDhcpAddress": agentInterfaceSecondaryDhcpAddress,
       "agentInterfaceDhcpProtocol": agentInterfaceDhcpProtocol,
       "agentInterfaceDnsHostName": agentInterfaceDnsHostName,
       "agentInterfaceAclName": agentInterfaceAclName,
       "agentInterfaceAPManagementFeature": agentInterfaceAPManagementFeature,
       "agentInterfaceActivePortNo": agentInterfaceActivePortNo,
       "agentInterfaceBackupPortNo": agentInterfaceBackupPortNo,
       "agentInterfaceVlanQuarantine": agentInterfaceVlanQuarantine,
       "agentInterfaceRowStatus": agentInterfaceRowStatus,
       "agentNtpConfigGroup": agentNtpConfigGroup,
       "agentNtpPollingInterval": agentNtpPollingInterval,
       "agentNtpServerTable": agentNtpServerTable,
       "agentNtpServerEntry": agentNtpServerEntry,
       "agentNtpServerIndex": agentNtpServerIndex,
       "agentNtpServerAddress": agentNtpServerAddress,
       "agentNtpServerRowStatus": agentNtpServerRowStatus,
       "agentDhcpConfigGroup": agentDhcpConfigGroup,
       "agentDhcpScopeTable": agentDhcpScopeTable,
       "agentDhcpScopeEntry": agentDhcpScopeEntry,
       "agentDhcpScopeIndex": agentDhcpScopeIndex,
       "agentDhcpScopeName": agentDhcpScopeName,
       "agentDhcpScopeLeaseTime": agentDhcpScopeLeaseTime,
       "agentDhcpScopeNetwork": agentDhcpScopeNetwork,
       "agentDhcpScopeNetmask": agentDhcpScopeNetmask,
       "agentDhcpScopePoolStartAddress": agentDhcpScopePoolStartAddress,
       "agentDhcpScopePoolEndAddress": agentDhcpScopePoolEndAddress,
       "agentDhcpScopeDefaultRouterAddress1": agentDhcpScopeDefaultRouterAddress1,
       "agentDhcpScopeDefaultRouterAddress2": agentDhcpScopeDefaultRouterAddress2,
       "agentDhcpScopeDefaultRouterAddress3": agentDhcpScopeDefaultRouterAddress3,
       "agentDhcpScopeDnsDomainName": agentDhcpScopeDnsDomainName,
       "agentDhcpScopeDnsServerAddress1": agentDhcpScopeDnsServerAddress1,
       "agentDhcpScopeDnsServerAddress2": agentDhcpScopeDnsServerAddress2,
       "agentDhcpScopeDnsServerAddress3": agentDhcpScopeDnsServerAddress3,
       "agentDhcpScopeNetbiosNameServerAddress1": agentDhcpScopeNetbiosNameServerAddress1,
       "agentDhcpScopeNetbiosNameServerAddress2": agentDhcpScopeNetbiosNameServerAddress2,
       "agentDhcpScopeNetbiosNameServerAddress3": agentDhcpScopeNetbiosNameServerAddress3,
       "agentDhcpScopeState": agentDhcpScopeState,
       "agentDhcpScopeRowStatus": agentDhcpScopeRowStatus,
       "agentSystemGroup": agentSystemGroup,
       "agentSaveConfig": agentSaveConfig,
       "agentClearConfig": agentClearConfig,
       "agentClearLags": agentClearLags,
       "agentClearLoginSessions": agentClearLoginSessions,
       "agentClearPortStats": agentClearPortStats,
       "agentClearSwitchStats": agentClearSwitchStats,
       "agentClearTrapLog": agentClearTrapLog,
       "agentResetSystem": agentResetSystem,
       "stats": stats,
       "portStatsTable": portStatsTable,
       "portStatsEntry": portStatsEntry,
       "portStatsIndex": portStatsIndex,
       "portStatsPktsTx64Octets": portStatsPktsTx64Octets,
       "portStatsPktsTx65to127Octets": portStatsPktsTx65to127Octets,
       "portStatsPktsTx128to255Octets": portStatsPktsTx128to255Octets,
       "portStatsPktsTx256to511Octets": portStatsPktsTx256to511Octets,
       "portStatsPktsTx512to1023Octets": portStatsPktsTx512to1023Octets,
       "portStatsPktsTx1024to1518Octets": portStatsPktsTx1024to1518Octets,
       "portStatsPktsRx1519to1530Octets": portStatsPktsRx1519to1530Octets,
       "portStatsPktsTx1519to1530Octets": portStatsPktsTx1519to1530Octets,
       "portStatsPktsTxOversizeOctets": portStatsPktsTxOversizeOctets,
       "switchingTraps": switchingTraps,
       "multipleUsersTrap": multipleUsersTrap,
       "broadcastStormStartTrap": broadcastStormStartTrap,
       "broadcastStormEndTrap": broadcastStormEndTrap,
       "linkFailureTrap": linkFailureTrap,
       "vlanRequestFailureTrap": vlanRequestFailureTrap,
       "vlanDeleteLastTrap": vlanDeleteLastTrap,
       "vlanDefaultCfgFailureTrap": vlanDefaultCfgFailureTrap,
       "vlanRestoreFailureTrap": vlanRestoreFailureTrap,
       "fanFailureTrap": fanFailureTrap,
       "stpInstanceNewRootTrap": stpInstanceNewRootTrap,
       "stpInstanceTopologyChangeTrap": stpInstanceTopologyChangeTrap,
       "powerSupplyStatusChangeTrap": powerSupplyStatusChangeTrap,
       "bsnSwitchingGroups": bsnSwitchingGroups,
       "bsnSwitchingAgentInfoGroup": bsnSwitchingAgentInfoGroup,
       "bsnSwitchingAgentConfigGroup": bsnSwitchingAgentConfigGroup,
       "bsnSwitchingAgentSystemGroup": bsnSwitchingAgentSystemGroup,
       "bsnSwitchingAgentStatsGroup": bsnSwitchingAgentStatsGroup,
       "bsnSwitchingObsGroup": bsnSwitchingObsGroup,
       "bsnSwitchingTrap": bsnSwitchingTrap,
       "bsnSwitchingCompliances": bsnSwitchingCompliances,
       "bsnSwitchingCompliance": bsnSwitchingCompliance}
)
