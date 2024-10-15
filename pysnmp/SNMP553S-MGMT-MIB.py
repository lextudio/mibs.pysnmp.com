# SNMP MIB module (SNMP553S-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP553S-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:14 2024
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

(dsx1,) = mibBuilder.importSymbols(
    "GDCDSX1-MIB",
    "dsx1")

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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

_Snmp553s_ObjectIdentity = ObjectIdentity
snmp553s = _Snmp553s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3)
)
_Snmp553sAlarmData_ObjectIdentity = ObjectIdentity
snmp553sAlarmData = _Snmp553sAlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1)
)
_Snmp553sNoResponseAlm_ObjectIdentity = ObjectIdentity
snmp553sNoResponseAlm = _Snmp553sNoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 1)
)
_Snmp553sDiagRxErrAlm_ObjectIdentity = ObjectIdentity
snmp553sDiagRxErrAlm = _Snmp553sDiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 2)
)
_Snmp553sPowerUpAlm_ObjectIdentity = ObjectIdentity
snmp553sPowerUpAlm = _Snmp553sPowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 3)
)
_Snmp553sNvRamCorrupt_ObjectIdentity = ObjectIdentity
snmp553sNvRamCorrupt = _Snmp553sNvRamCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 4)
)
_Snmp553sUnitFailure_ObjectIdentity = ObjectIdentity
snmp553sUnitFailure = _Snmp553sUnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 5)
)
_Snmp553sMbiLock_ObjectIdentity = ObjectIdentity
snmp553sMbiLock = _Snmp553sMbiLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 6)
)
_Snmp553sLocalPwrFail_ObjectIdentity = ObjectIdentity
snmp553sLocalPwrFail = _Snmp553sLocalPwrFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 7)
)
_Snmp553sTimingLoss_ObjectIdentity = ObjectIdentity
snmp553sTimingLoss = _Snmp553sTimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 8)
)
_Snmp553sStatusChange_ObjectIdentity = ObjectIdentity
snmp553sStatusChange = _Snmp553sStatusChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 9)
)
_Snmp553sUnsoTest_ObjectIdentity = ObjectIdentity
snmp553sUnsoTest = _Snmp553sUnsoTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 10)
)
_Snmp553sLossOfSignal_ObjectIdentity = ObjectIdentity
snmp553sLossOfSignal = _Snmp553sLossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 11)
)
_Snmp553sLossOfFrame_ObjectIdentity = ObjectIdentity
snmp553sLossOfFrame = _Snmp553sLossOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 12)
)
_Snmp553sAis_ObjectIdentity = ObjectIdentity
snmp553sAis = _Snmp553sAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 13)
)
_Snmp553sReceivedYellow_ObjectIdentity = ObjectIdentity
snmp553sReceivedYellow = _Snmp553sReceivedYellow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 14)
)
_Snmp553sUnavailSignalState_ObjectIdentity = ObjectIdentity
snmp553sUnavailSignalState = _Snmp553sUnavailSignalState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 15)
)
_Snmp553sExcessiveZeros_ObjectIdentity = ObjectIdentity
snmp553sExcessiveZeros = _Snmp553sExcessiveZeros_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 16)
)
_Snmp553sLowAverageDensity_ObjectIdentity = ObjectIdentity
snmp553sLowAverageDensity = _Snmp553sLowAverageDensity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 17)
)
_Snmp553sControlledSlips_ObjectIdentity = ObjectIdentity
snmp553sControlledSlips = _Snmp553sControlledSlips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 18)
)
_Snmp553sBipolarViolations_ObjectIdentity = ObjectIdentity
snmp553sBipolarViolations = _Snmp553sBipolarViolations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 19)
)
_Snmp553sCrcErrors_ObjectIdentity = ObjectIdentity
snmp553sCrcErrors = _Snmp553sCrcErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 1, 20)
)


class _Snmp553sMIBversion_Type(DisplayString):
    """Custom type snmp553sMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Snmp553sMIBversion_Type.__name__ = "DisplayString"
_Snmp553sMIBversion_Object = MibScalar
snmp553sMIBversion = _Snmp553sMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 2),
    _Snmp553sMIBversion_Type()
)
snmp553sMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sMIBversion.setStatus("mandatory")
_Snmp553sMaintenanceTable_Object = MibTable
snmp553sMaintenanceTable = _Snmp553sMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3)
)
if mibBuilder.loadTexts:
    snmp553sMaintenanceTable.setStatus("mandatory")
_Snmp553sMaintenanceEntry_Object = MibTableRow
snmp553sMaintenanceEntry = _Snmp553sMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1)
)
snmp553sMaintenanceEntry.setIndexNames(
    (0, "SNMP553S-MGMT-MIB", "snmp553sMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    snmp553sMaintenanceEntry.setStatus("mandatory")
_Snmp553sMaintenanceIndex_Type = SCinstance
_Snmp553sMaintenanceIndex_Object = MibTableColumn
snmp553sMaintenanceIndex = _Snmp553sMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 1),
    _Snmp553sMaintenanceIndex_Type()
)
snmp553sMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sMaintenanceIndex.setStatus("mandatory")


class _Snmp553sCascadePresent_Type(Integer32):
    """Custom type snmp553sCascadePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_Snmp553sCascadePresent_Type.__name__ = "Integer32"
_Snmp553sCascadePresent_Object = MibTableColumn
snmp553sCascadePresent = _Snmp553sCascadePresent_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 2),
    _Snmp553sCascadePresent_Type()
)
snmp553sCascadePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sCascadePresent.setStatus("mandatory")


class _Snmp553sExtModemPresent_Type(Integer32):
    """Custom type snmp553sExtModemPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_Snmp553sExtModemPresent_Type.__name__ = "Integer32"
_Snmp553sExtModemPresent_Object = MibTableColumn
snmp553sExtModemPresent = _Snmp553sExtModemPresent_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 3),
    _Snmp553sExtModemPresent_Type()
)
snmp553sExtModemPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sExtModemPresent.setStatus("mandatory")


class _Snmp553sUnitType_Type(Integer32):
    """Custom type snmp553sUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("remote", 2))
    )


_Snmp553sUnitType_Type.__name__ = "Integer32"
_Snmp553sUnitType_Object = MibTableColumn
snmp553sUnitType = _Snmp553sUnitType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 4),
    _Snmp553sUnitType_Type()
)
snmp553sUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sUnitType.setStatus("mandatory")


class _Snmp553sManagementSource_Type(Integer32):
    """Custom type snmp553sManagementSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bus485", 5),
          ("daisyChain", 4),
          ("fdl", 3),
          ("localSnmp", 6),
          ("modemSnmp", 1),
          ("secondaryChannel", 2))
    )


_Snmp553sManagementSource_Type.__name__ = "Integer32"
_Snmp553sManagementSource_Object = MibTableColumn
snmp553sManagementSource = _Snmp553sManagementSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 5),
    _Snmp553sManagementSource_Type()
)
snmp553sManagementSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sManagementSource.setStatus("mandatory")


class _Snmp553sProductType_Type(Integer32):
    """Custom type snmp553sProductType based on Integer32"""
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
        *(("nms553c", 7),
          ("nms553cifp", 8),
          ("nms553d1", 4),
          ("nms553d1ifp", 5),
          ("nms553d3ifp", 6),
          ("snmp553scifp", 3),
          ("snmp553sd1ifp", 1),
          ("snmp553sd3ifp", 2))
    )


_Snmp553sProductType_Type.__name__ = "Integer32"
_Snmp553sProductType_Object = MibTableColumn
snmp553sProductType = _Snmp553sProductType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 6),
    _Snmp553sProductType_Type()
)
snmp553sProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sProductType.setStatus("mandatory")


class _Snmp553sLedStatus_Type(OctetString):
    """Custom type snmp553sLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Snmp553sLedStatus_Type.__name__ = "OctetString"
_Snmp553sLedStatus_Object = MibTableColumn
snmp553sLedStatus = _Snmp553sLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 7),
    _Snmp553sLedStatus_Type()
)
snmp553sLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sLedStatus.setStatus("mandatory")


class _Snmp553sUnitSerialNumber_Type(OctetString):
    """Custom type snmp553sUnitSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Snmp553sUnitSerialNumber_Type.__name__ = "OctetString"
_Snmp553sUnitSerialNumber_Object = MibTableColumn
snmp553sUnitSerialNumber = _Snmp553sUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 8),
    _Snmp553sUnitSerialNumber_Type()
)
snmp553sUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sUnitSerialNumber.setStatus("mandatory")


class _Snmp553sSaveAllConfig_Type(Integer32):
    """Custom type snmp553sSaveAllConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("saveConfig", 2))
    )


_Snmp553sSaveAllConfig_Type.__name__ = "Integer32"
_Snmp553sSaveAllConfig_Object = MibTableColumn
snmp553sSaveAllConfig = _Snmp553sSaveAllConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 3, 1, 9),
    _Snmp553sSaveAllConfig_Type()
)
snmp553sSaveAllConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sSaveAllConfig.setStatus("mandatory")
_Snmp553sUnitConfigTable_Object = MibTable
snmp553sUnitConfigTable = _Snmp553sUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 4)
)
if mibBuilder.loadTexts:
    snmp553sUnitConfigTable.setStatus("mandatory")
_Snmp553sUnitConfigEntry_Object = MibTableRow
snmp553sUnitConfigEntry = _Snmp553sUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 4, 1)
)
snmp553sUnitConfigEntry.setIndexNames(
    (0, "SNMP553S-MGMT-MIB", "snmp553sUnitConfigIndex"),
)
if mibBuilder.loadTexts:
    snmp553sUnitConfigEntry.setStatus("mandatory")
_Snmp553sUnitConfigIndex_Type = SCinstance
_Snmp553sUnitConfigIndex_Object = MibTableColumn
snmp553sUnitConfigIndex = _Snmp553sUnitConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 4, 1, 1),
    _Snmp553sUnitConfigIndex_Type()
)
snmp553sUnitConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sUnitConfigIndex.setStatus("mandatory")


class _Snmp553sSaveCsuConfig_Type(Integer32):
    """Custom type snmp553sSaveCsuConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("saveConfig", 2))
    )


_Snmp553sSaveCsuConfig_Type.__name__ = "Integer32"
_Snmp553sSaveCsuConfig_Object = MibTableColumn
snmp553sSaveCsuConfig = _Snmp553sSaveCsuConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 4, 1, 2),
    _Snmp553sSaveCsuConfig_Type()
)
snmp553sSaveCsuConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sSaveCsuConfig.setStatus("mandatory")


class _Snmp553sShelfCommander_Type(Integer32):
    """Custom type snmp553sShelfCommander based on Integer32"""
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


_Snmp553sShelfCommander_Type.__name__ = "Integer32"
_Snmp553sShelfCommander_Object = MibTableColumn
snmp553sShelfCommander = _Snmp553sShelfCommander_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 4, 1, 3),
    _Snmp553sShelfCommander_Type()
)
snmp553sShelfCommander.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sShelfCommander.setStatus("mandatory")


class _Snmp553sForceFakeMaster_Type(Integer32):
    """Custom type snmp553sForceFakeMaster based on Integer32"""
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


_Snmp553sForceFakeMaster_Type.__name__ = "Integer32"
_Snmp553sForceFakeMaster_Object = MibTableColumn
snmp553sForceFakeMaster = _Snmp553sForceFakeMaster_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 4, 1, 4),
    _Snmp553sForceFakeMaster_Type()
)
snmp553sForceFakeMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sForceFakeMaster.setStatus("mandatory")


class _Snmp553sDaisyChainBps_Type(Integer32):
    """Custom type snmp553sDaisyChainBps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bps75", 2),
          ("bps9600", 3),
          ("none", 1))
    )


_Snmp553sDaisyChainBps_Type.__name__ = "Integer32"
_Snmp553sDaisyChainBps_Object = MibTableColumn
snmp553sDaisyChainBps = _Snmp553sDaisyChainBps_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 4, 1, 5),
    _Snmp553sDaisyChainBps_Type()
)
snmp553sDaisyChainBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sDaisyChainBps.setStatus("mandatory")
_Snmp553sChannelConfigTable_Object = MibTable
snmp553sChannelConfigTable = _Snmp553sChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 5)
)
if mibBuilder.loadTexts:
    snmp553sChannelConfigTable.setStatus("mandatory")
_Snmp553sChannelConfigEntry_Object = MibTableRow
snmp553sChannelConfigEntry = _Snmp553sChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 5, 1)
)
snmp553sChannelConfigEntry.setIndexNames(
    (0, "SNMP553S-MGMT-MIB", "snmp553sChannelConfigIndex"),
)
if mibBuilder.loadTexts:
    snmp553sChannelConfigEntry.setStatus("mandatory")
_Snmp553sChannelConfigIndex_Type = SCinstance
_Snmp553sChannelConfigIndex_Object = MibTableColumn
snmp553sChannelConfigIndex = _Snmp553sChannelConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 5, 1, 1),
    _Snmp553sChannelConfigIndex_Type()
)
snmp553sChannelConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sChannelConfigIndex.setStatus("mandatory")


class _Snmp553sDCCCompatibilityMode_Type(Integer32):
    """Custom type snmp553sDCCCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nms510", 2),
          ("nms553", 1),
          ("other", 3))
    )


_Snmp553sDCCCompatibilityMode_Type.__name__ = "Integer32"
_Snmp553sDCCCompatibilityMode_Object = MibTableColumn
snmp553sDCCCompatibilityMode = _Snmp553sDCCCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 5, 1, 2),
    _Snmp553sDCCCompatibilityMode_Type()
)
snmp553sDCCCompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sDCCCompatibilityMode.setStatus("mandatory")


class _Snmp553sSaveDsuConfig_Type(Integer32):
    """Custom type snmp553sSaveDsuConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("saveConfig", 2))
    )


_Snmp553sSaveDsuConfig_Type.__name__ = "Integer32"
_Snmp553sSaveDsuConfig_Object = MibTableColumn
snmp553sSaveDsuConfig = _Snmp553sSaveDsuConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 5, 1, 3),
    _Snmp553sSaveDsuConfig_Type()
)
snmp553sSaveDsuConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sSaveDsuConfig.setStatus("mandatory")
_Snmp553sDiagTable_Object = MibTable
snmp553sDiagTable = _Snmp553sDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 6)
)
if mibBuilder.loadTexts:
    snmp553sDiagTable.setStatus("mandatory")
_Snmp553sDiagEntry_Object = MibTableRow
snmp553sDiagEntry = _Snmp553sDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 6, 1)
)
snmp553sDiagEntry.setIndexNames(
    (0, "SNMP553S-MGMT-MIB", "snmp553sDiagIndex"),
)
if mibBuilder.loadTexts:
    snmp553sDiagEntry.setStatus("mandatory")
_Snmp553sDiagIndex_Type = SCinstance
_Snmp553sDiagIndex_Object = MibTableColumn
snmp553sDiagIndex = _Snmp553sDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 6, 1, 1),
    _Snmp553sDiagIndex_Type()
)
snmp553sDiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sDiagIndex.setStatus("mandatory")


class _Snmp553sDiagTestDuration_Type(Integer32):
    """Custom type snmp553sDiagTestDuration based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 1),
          ("testTime10Mins", 11),
          ("testTime15Mins", 12),
          ("testTime1Min", 2),
          ("testTime20Mins", 13),
          ("testTime25Mins", 14),
          ("testTime2Mins", 3),
          ("testTime30Mins", 15),
          ("testTime30Secs", 16),
          ("testTime3Mins", 4),
          ("testTime4Mins", 5),
          ("testTime5Mins", 6),
          ("testTime6Mins", 7),
          ("testTime7Mins", 8),
          ("testTime8Mins", 9),
          ("testTime9Mins", 10))
    )


_Snmp553sDiagTestDuration_Type.__name__ = "Integer32"
_Snmp553sDiagTestDuration_Object = MibTableColumn
snmp553sDiagTestDuration = _Snmp553sDiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 6, 1, 2),
    _Snmp553sDiagTestDuration_Type()
)
snmp553sDiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sDiagTestDuration.setStatus("mandatory")


class _Snmp553sDiagProgPattern_Type(Integer32):
    """Custom type snmp553sDiagProgPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Snmp553sDiagProgPattern_Type.__name__ = "Integer32"
_Snmp553sDiagProgPattern_Object = MibTableColumn
snmp553sDiagProgPattern = _Snmp553sDiagProgPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 6, 1, 3),
    _Snmp553sDiagProgPattern_Type()
)
snmp553sDiagProgPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sDiagProgPattern.setStatus("mandatory")
_Snmp553sAlarmHistoryTable_Object = MibTable
snmp553sAlarmHistoryTable = _Snmp553sAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7)
)
if mibBuilder.loadTexts:
    snmp553sAlarmHistoryTable.setStatus("mandatory")
_Snmp553sAlarmHistoryEntry_Object = MibTableRow
snmp553sAlarmHistoryEntry = _Snmp553sAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1)
)
snmp553sAlarmHistoryEntry.setIndexNames(
    (0, "SNMP553S-MGMT-MIB", "snmp553sAlarmHistoryIndex"),
    (0, "SNMP553S-MGMT-MIB", "snmp553sAlarmHistoryIdentifier"),
)
if mibBuilder.loadTexts:
    snmp553sAlarmHistoryEntry.setStatus("mandatory")
_Snmp553sAlarmHistoryIndex_Type = SCinstance
_Snmp553sAlarmHistoryIndex_Object = MibTableColumn
snmp553sAlarmHistoryIndex = _Snmp553sAlarmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 1),
    _Snmp553sAlarmHistoryIndex_Type()
)
snmp553sAlarmHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmHistoryIndex.setStatus("mandatory")
_Snmp553sAlarmHistoryIdentifier_Type = ObjectIdentifier
_Snmp553sAlarmHistoryIdentifier_Object = MibTableColumn
snmp553sAlarmHistoryIdentifier = _Snmp553sAlarmHistoryIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 2),
    _Snmp553sAlarmHistoryIdentifier_Type()
)
snmp553sAlarmHistoryIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmHistoryIdentifier.setStatus("mandatory")
_Snmp553sAlarmCount_Type = Gauge32
_Snmp553sAlarmCount_Object = MibTableColumn
snmp553sAlarmCount = _Snmp553sAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 3),
    _Snmp553sAlarmCount_Type()
)
snmp553sAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmCount.setStatus("mandatory")
_Snmp553sAlarmFirstOccurrenceHours_Type = Integer32
_Snmp553sAlarmFirstOccurrenceHours_Object = MibTableColumn
snmp553sAlarmFirstOccurrenceHours = _Snmp553sAlarmFirstOccurrenceHours_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 4),
    _Snmp553sAlarmFirstOccurrenceHours_Type()
)
snmp553sAlarmFirstOccurrenceHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmFirstOccurrenceHours.setStatus("mandatory")
_Snmp553sAlarmFirstOccurrenceMinutes_Type = Integer32
_Snmp553sAlarmFirstOccurrenceMinutes_Object = MibTableColumn
snmp553sAlarmFirstOccurrenceMinutes = _Snmp553sAlarmFirstOccurrenceMinutes_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 5),
    _Snmp553sAlarmFirstOccurrenceMinutes_Type()
)
snmp553sAlarmFirstOccurrenceMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmFirstOccurrenceMinutes.setStatus("mandatory")
_Snmp553sAlarmFirstOccurrenceSeconds_Type = Integer32
_Snmp553sAlarmFirstOccurrenceSeconds_Object = MibTableColumn
snmp553sAlarmFirstOccurrenceSeconds = _Snmp553sAlarmFirstOccurrenceSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 6),
    _Snmp553sAlarmFirstOccurrenceSeconds_Type()
)
snmp553sAlarmFirstOccurrenceSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmFirstOccurrenceSeconds.setStatus("mandatory")
_Snmp553sAlarmFirstOccurrenceMonth_Type = Integer32
_Snmp553sAlarmFirstOccurrenceMonth_Object = MibTableColumn
snmp553sAlarmFirstOccurrenceMonth = _Snmp553sAlarmFirstOccurrenceMonth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 7),
    _Snmp553sAlarmFirstOccurrenceMonth_Type()
)
snmp553sAlarmFirstOccurrenceMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmFirstOccurrenceMonth.setStatus("mandatory")
_Snmp553sAlarmFirstOccurrenceDay_Type = Integer32
_Snmp553sAlarmFirstOccurrenceDay_Object = MibTableColumn
snmp553sAlarmFirstOccurrenceDay = _Snmp553sAlarmFirstOccurrenceDay_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 8),
    _Snmp553sAlarmFirstOccurrenceDay_Type()
)
snmp553sAlarmFirstOccurrenceDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmFirstOccurrenceDay.setStatus("mandatory")
_Snmp553sAlarmFirstOccurrenceYear_Type = Integer32
_Snmp553sAlarmFirstOccurrenceYear_Object = MibTableColumn
snmp553sAlarmFirstOccurrenceYear = _Snmp553sAlarmFirstOccurrenceYear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 9),
    _Snmp553sAlarmFirstOccurrenceYear_Type()
)
snmp553sAlarmFirstOccurrenceYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmFirstOccurrenceYear.setStatus("mandatory")
_Snmp553sAlarmLastOccurrenceHours_Type = Integer32
_Snmp553sAlarmLastOccurrenceHours_Object = MibTableColumn
snmp553sAlarmLastOccurrenceHours = _Snmp553sAlarmLastOccurrenceHours_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 10),
    _Snmp553sAlarmLastOccurrenceHours_Type()
)
snmp553sAlarmLastOccurrenceHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmLastOccurrenceHours.setStatus("mandatory")
_Snmp553sAlarmLastOccurrenceMinutes_Type = Integer32
_Snmp553sAlarmLastOccurrenceMinutes_Object = MibTableColumn
snmp553sAlarmLastOccurrenceMinutes = _Snmp553sAlarmLastOccurrenceMinutes_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 11),
    _Snmp553sAlarmLastOccurrenceMinutes_Type()
)
snmp553sAlarmLastOccurrenceMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmLastOccurrenceMinutes.setStatus("mandatory")
_Snmp553sAlarmLastOccurrenceSeconds_Type = Integer32
_Snmp553sAlarmLastOccurrenceSeconds_Object = MibTableColumn
snmp553sAlarmLastOccurrenceSeconds = _Snmp553sAlarmLastOccurrenceSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 12),
    _Snmp553sAlarmLastOccurrenceSeconds_Type()
)
snmp553sAlarmLastOccurrenceSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmLastOccurrenceSeconds.setStatus("mandatory")
_Snmp553sAlarmLastOccurrenceMonth_Type = Integer32
_Snmp553sAlarmLastOccurrenceMonth_Object = MibTableColumn
snmp553sAlarmLastOccurrenceMonth = _Snmp553sAlarmLastOccurrenceMonth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 13),
    _Snmp553sAlarmLastOccurrenceMonth_Type()
)
snmp553sAlarmLastOccurrenceMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmLastOccurrenceMonth.setStatus("mandatory")
_Snmp553sAlarmLastOccurrenceDay_Type = Integer32
_Snmp553sAlarmLastOccurrenceDay_Object = MibTableColumn
snmp553sAlarmLastOccurrenceDay = _Snmp553sAlarmLastOccurrenceDay_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 14),
    _Snmp553sAlarmLastOccurrenceDay_Type()
)
snmp553sAlarmLastOccurrenceDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmLastOccurrenceDay.setStatus("mandatory")
_Snmp553sAlarmLastOccurrenceYear_Type = Integer32
_Snmp553sAlarmLastOccurrenceYear_Object = MibTableColumn
snmp553sAlarmLastOccurrenceYear = _Snmp553sAlarmLastOccurrenceYear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 7, 1, 15),
    _Snmp553sAlarmLastOccurrenceYear_Type()
)
snmp553sAlarmLastOccurrenceYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmLastOccurrenceYear.setStatus("mandatory")
_Snmp553sAlarmMaintenanceTable_Object = MibTable
snmp553sAlarmMaintenanceTable = _Snmp553sAlarmMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8)
)
if mibBuilder.loadTexts:
    snmp553sAlarmMaintenanceTable.setStatus("mandatory")
_Snmp553sAlarmMaintenanceEntry_Object = MibTableRow
snmp553sAlarmMaintenanceEntry = _Snmp553sAlarmMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1)
)
snmp553sAlarmMaintenanceEntry.setIndexNames(
    (0, "SNMP553S-MGMT-MIB", "snmp553sAlarmMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    snmp553sAlarmMaintenanceEntry.setStatus("mandatory")
_Snmp553sAlarmMaintenanceIndex_Type = SCinstance
_Snmp553sAlarmMaintenanceIndex_Object = MibTableColumn
snmp553sAlarmMaintenanceIndex = _Snmp553sAlarmMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 1),
    _Snmp553sAlarmMaintenanceIndex_Type()
)
snmp553sAlarmMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sAlarmMaintenanceIndex.setStatus("mandatory")


class _Snmp553sClearAlarmHistory_Type(Integer32):
    """Custom type snmp553sClearAlarmHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("norm", 2))
    )


_Snmp553sClearAlarmHistory_Type.__name__ = "Integer32"
_Snmp553sClearAlarmHistory_Object = MibTableColumn
snmp553sClearAlarmHistory = _Snmp553sClearAlarmHistory_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 2),
    _Snmp553sClearAlarmHistory_Type()
)
snmp553sClearAlarmHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sClearAlarmHistory.setStatus("mandatory")
_Snmp553sRTCHours_Type = Integer32
_Snmp553sRTCHours_Object = MibTableColumn
snmp553sRTCHours = _Snmp553sRTCHours_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 3),
    _Snmp553sRTCHours_Type()
)
snmp553sRTCHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sRTCHours.setStatus("mandatory")
_Snmp553sRTCMinutes_Type = Integer32
_Snmp553sRTCMinutes_Object = MibTableColumn
snmp553sRTCMinutes = _Snmp553sRTCMinutes_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 4),
    _Snmp553sRTCMinutes_Type()
)
snmp553sRTCMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sRTCMinutes.setStatus("mandatory")
_Snmp553sRTCSeconds_Type = Integer32
_Snmp553sRTCSeconds_Object = MibTableColumn
snmp553sRTCSeconds = _Snmp553sRTCSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 5),
    _Snmp553sRTCSeconds_Type()
)
snmp553sRTCSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sRTCSeconds.setStatus("mandatory")
_Snmp553sRTCMonth_Type = Integer32
_Snmp553sRTCMonth_Object = MibTableColumn
snmp553sRTCMonth = _Snmp553sRTCMonth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 6),
    _Snmp553sRTCMonth_Type()
)
snmp553sRTCMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sRTCMonth.setStatus("mandatory")
_Snmp553sRTCDay_Type = Integer32
_Snmp553sRTCDay_Object = MibTableColumn
snmp553sRTCDay = _Snmp553sRTCDay_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 7),
    _Snmp553sRTCDay_Type()
)
snmp553sRTCDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sRTCDay.setStatus("mandatory")
_Snmp553sRTCYear_Type = Integer32
_Snmp553sRTCYear_Object = MibTableColumn
snmp553sRTCYear = _Snmp553sRTCYear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 8),
    _Snmp553sRTCYear_Type()
)
snmp553sRTCYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sRTCYear.setStatus("mandatory")


class _Snmp553sTimeOfLastAlarmClear_Type(OctetString):
    """Custom type snmp553sTimeOfLastAlarmClear based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Snmp553sTimeOfLastAlarmClear_Type.__name__ = "OctetString"
_Snmp553sTimeOfLastAlarmClear_Object = MibTableColumn
snmp553sTimeOfLastAlarmClear = _Snmp553sTimeOfLastAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 8, 1, 9),
    _Snmp553sTimeOfLastAlarmClear_Type()
)
snmp553sTimeOfLastAlarmClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sTimeOfLastAlarmClear.setStatus("mandatory")
_Snmp553sc_ObjectIdentity = ObjectIdentity
snmp553sc = _Snmp553sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP553S-MGMT-MIB",
    **{"snmp553s": snmp553s,
       "snmp553sAlarmData": snmp553sAlarmData,
       "snmp553sNoResponseAlm": snmp553sNoResponseAlm,
       "snmp553sDiagRxErrAlm": snmp553sDiagRxErrAlm,
       "snmp553sPowerUpAlm": snmp553sPowerUpAlm,
       "snmp553sNvRamCorrupt": snmp553sNvRamCorrupt,
       "snmp553sUnitFailure": snmp553sUnitFailure,
       "snmp553sMbiLock": snmp553sMbiLock,
       "snmp553sLocalPwrFail": snmp553sLocalPwrFail,
       "snmp553sTimingLoss": snmp553sTimingLoss,
       "snmp553sStatusChange": snmp553sStatusChange,
       "snmp553sUnsoTest": snmp553sUnsoTest,
       "snmp553sLossOfSignal": snmp553sLossOfSignal,
       "snmp553sLossOfFrame": snmp553sLossOfFrame,
       "snmp553sAis": snmp553sAis,
       "snmp553sReceivedYellow": snmp553sReceivedYellow,
       "snmp553sUnavailSignalState": snmp553sUnavailSignalState,
       "snmp553sExcessiveZeros": snmp553sExcessiveZeros,
       "snmp553sLowAverageDensity": snmp553sLowAverageDensity,
       "snmp553sControlledSlips": snmp553sControlledSlips,
       "snmp553sBipolarViolations": snmp553sBipolarViolations,
       "snmp553sCrcErrors": snmp553sCrcErrors,
       "snmp553sMIBversion": snmp553sMIBversion,
       "snmp553sMaintenanceTable": snmp553sMaintenanceTable,
       "snmp553sMaintenanceEntry": snmp553sMaintenanceEntry,
       "snmp553sMaintenanceIndex": snmp553sMaintenanceIndex,
       "snmp553sCascadePresent": snmp553sCascadePresent,
       "snmp553sExtModemPresent": snmp553sExtModemPresent,
       "snmp553sUnitType": snmp553sUnitType,
       "snmp553sManagementSource": snmp553sManagementSource,
       "snmp553sProductType": snmp553sProductType,
       "snmp553sLedStatus": snmp553sLedStatus,
       "snmp553sUnitSerialNumber": snmp553sUnitSerialNumber,
       "snmp553sSaveAllConfig": snmp553sSaveAllConfig,
       "snmp553sUnitConfigTable": snmp553sUnitConfigTable,
       "snmp553sUnitConfigEntry": snmp553sUnitConfigEntry,
       "snmp553sUnitConfigIndex": snmp553sUnitConfigIndex,
       "snmp553sSaveCsuConfig": snmp553sSaveCsuConfig,
       "snmp553sShelfCommander": snmp553sShelfCommander,
       "snmp553sForceFakeMaster": snmp553sForceFakeMaster,
       "snmp553sDaisyChainBps": snmp553sDaisyChainBps,
       "snmp553sChannelConfigTable": snmp553sChannelConfigTable,
       "snmp553sChannelConfigEntry": snmp553sChannelConfigEntry,
       "snmp553sChannelConfigIndex": snmp553sChannelConfigIndex,
       "snmp553sDCCCompatibilityMode": snmp553sDCCCompatibilityMode,
       "snmp553sSaveDsuConfig": snmp553sSaveDsuConfig,
       "snmp553sDiagTable": snmp553sDiagTable,
       "snmp553sDiagEntry": snmp553sDiagEntry,
       "snmp553sDiagIndex": snmp553sDiagIndex,
       "snmp553sDiagTestDuration": snmp553sDiagTestDuration,
       "snmp553sDiagProgPattern": snmp553sDiagProgPattern,
       "snmp553sAlarmHistoryTable": snmp553sAlarmHistoryTable,
       "snmp553sAlarmHistoryEntry": snmp553sAlarmHistoryEntry,
       "snmp553sAlarmHistoryIndex": snmp553sAlarmHistoryIndex,
       "snmp553sAlarmHistoryIdentifier": snmp553sAlarmHistoryIdentifier,
       "snmp553sAlarmCount": snmp553sAlarmCount,
       "snmp553sAlarmFirstOccurrenceHours": snmp553sAlarmFirstOccurrenceHours,
       "snmp553sAlarmFirstOccurrenceMinutes": snmp553sAlarmFirstOccurrenceMinutes,
       "snmp553sAlarmFirstOccurrenceSeconds": snmp553sAlarmFirstOccurrenceSeconds,
       "snmp553sAlarmFirstOccurrenceMonth": snmp553sAlarmFirstOccurrenceMonth,
       "snmp553sAlarmFirstOccurrenceDay": snmp553sAlarmFirstOccurrenceDay,
       "snmp553sAlarmFirstOccurrenceYear": snmp553sAlarmFirstOccurrenceYear,
       "snmp553sAlarmLastOccurrenceHours": snmp553sAlarmLastOccurrenceHours,
       "snmp553sAlarmLastOccurrenceMinutes": snmp553sAlarmLastOccurrenceMinutes,
       "snmp553sAlarmLastOccurrenceSeconds": snmp553sAlarmLastOccurrenceSeconds,
       "snmp553sAlarmLastOccurrenceMonth": snmp553sAlarmLastOccurrenceMonth,
       "snmp553sAlarmLastOccurrenceDay": snmp553sAlarmLastOccurrenceDay,
       "snmp553sAlarmLastOccurrenceYear": snmp553sAlarmLastOccurrenceYear,
       "snmp553sAlarmMaintenanceTable": snmp553sAlarmMaintenanceTable,
       "snmp553sAlarmMaintenanceEntry": snmp553sAlarmMaintenanceEntry,
       "snmp553sAlarmMaintenanceIndex": snmp553sAlarmMaintenanceIndex,
       "snmp553sClearAlarmHistory": snmp553sClearAlarmHistory,
       "snmp553sRTCHours": snmp553sRTCHours,
       "snmp553sRTCMinutes": snmp553sRTCMinutes,
       "snmp553sRTCSeconds": snmp553sRTCSeconds,
       "snmp553sRTCMonth": snmp553sRTCMonth,
       "snmp553sRTCDay": snmp553sRTCDay,
       "snmp553sRTCYear": snmp553sRTCYear,
       "snmp553sTimeOfLastAlarmClear": snmp553sTimeOfLastAlarmClear,
       "snmp553sc": snmp553sc}
)
