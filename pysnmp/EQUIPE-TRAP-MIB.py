# SNMP MIB module (EQUIPE-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQUIPE-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:19 2024
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

(EqApsLineState,
 EqAtmPvcType,
 EqIfType,
 EqSeverityLevel,
 eqFanUnitEid,
 eqFaultModule,
 eqFaultScope,
 eqFaultSwlm,
 eqFaultTime,
 eqHardDiskEid,
 eqHardDiskUsedHiMark,
 eqHardDiskUsedLowMark,
 eqModuleEid,
 eqModuleRedOperRole,
 eqModuleShelfId,
 eqModuleSlotId,
 eqStratumCentRedStatus,
 eqStratumCentStatus) = mibBuilder.importSymbols(
    "EQUIPE-SYSTEM-MIB",
    "EqApsLineState",
    "EqAtmPvcType",
    "EqIfType",
    "EqSeverityLevel",
    "eqFanUnitEid",
    "eqFaultModule",
    "eqFaultScope",
    "eqFaultSwlm",
    "eqFaultTime",
    "eqHardDiskEid",
    "eqHardDiskUsedHiMark",
    "eqHardDiskUsedLowMark",
    "eqModuleEid",
    "eqModuleRedOperRole",
    "eqModuleShelfId",
    "eqModuleSlotId",
    "eqStratumCentRedStatus",
    "eqStratumCentStatus")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eqTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Equipe_ObjectIdentity = ObjectIdentity
equipe = _Equipe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022)
)
_EqTrapObjects_ObjectIdentity = ObjectIdentity
eqTrapObjects = _EqTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1)
)
_EqSystemId_Type = DisplayString
_EqSystemId_Object = MibScalar
eqSystemId = _EqSystemId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 1),
    _EqSystemId_Type()
)
eqSystemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqSystemId.setStatus("current")


class _EqEid_Type(Integer32):
    """Custom type eqEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqEid_Type.__name__ = "Integer32"
_EqEid_Object = MibScalar
eqEid = _EqEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 2),
    _EqEid_Type()
)
eqEid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqEid.setStatus("current")
_EqIfName_Type = DisplayString
_EqIfName_Object = MibScalar
eqIfName = _EqIfName_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 3),
    _EqIfName_Type()
)
eqIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqIfName.setStatus("current")
_EqIpAddress_Type = IpAddress
_EqIpAddress_Object = MibScalar
eqIpAddress = _EqIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 4),
    _EqIpAddress_Type()
)
eqIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqIpAddress.setStatus("current")
_EqFileName_Type = DisplayString
_EqFileName_Object = MibScalar
eqFileName = _EqFileName_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 5),
    _EqFileName_Type()
)
eqFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqFileName.setStatus("current")
_EqTrapDescr_Type = DisplayString
_EqTrapDescr_Object = MibScalar
eqTrapDescr = _EqTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 6),
    _EqTrapDescr_Type()
)
eqTrapDescr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqTrapDescr.setStatus("current")


class _EqModuleFuseType_Type(Integer32):
    """Custom type eqModuleFuseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fuseTypeA", 1),
          ("fuseTypeB", 2))
    )


_EqModuleFuseType_Type.__name__ = "Integer32"
_EqModuleFuseType_Object = MibScalar
eqModuleFuseType = _EqModuleFuseType_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 7),
    _EqModuleFuseType_Type()
)
eqModuleFuseType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqModuleFuseType.setStatus("current")
_EqApsLineState_Type = EqApsLineState
_EqApsLineState_Object = MibScalar
eqApsLineState = _EqApsLineState_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 8),
    _EqApsLineState_Type()
)
eqApsLineState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqApsLineState.setStatus("current")
_EqIfType_Type = EqIfType
_EqIfType_Object = MibScalar
eqIfType = _EqIfType_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 9),
    _EqIfType_Type()
)
eqIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqIfType.setStatus("current")
_EqAtmPvcType_Type = EqAtmPvcType
_EqAtmPvcType_Object = MibScalar
eqAtmPvcType = _EqAtmPvcType_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 10),
    _EqAtmPvcType_Type()
)
eqAtmPvcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqAtmPvcType.setStatus("current")
_EqEventTime_Type = DateAndTime
_EqEventTime_Object = MibScalar
eqEventTime = _EqEventTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 11),
    _EqEventTime_Type()
)
eqEventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqEventTime.setStatus("current")


class _EqThresholdValue_Type(Integer32):
    """Custom type eqThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqThresholdValue_Type.__name__ = "Integer32"
_EqThresholdValue_Object = MibScalar
eqThresholdValue = _EqThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 12),
    _EqThresholdValue_Type()
)
eqThresholdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqThresholdValue.setStatus("current")


class _EqCurrentValue_Type(Integer32):
    """Custom type eqCurrentValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqCurrentValue_Type.__name__ = "Integer32"
_EqCurrentValue_Object = MibScalar
eqCurrentValue = _EqCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 13),
    _EqCurrentValue_Type()
)
eqCurrentValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqCurrentValue.setStatus("current")
_EqResourceId_Type = DisplayString
_EqResourceId_Object = MibScalar
eqResourceId = _EqResourceId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 14),
    _EqResourceId_Type()
)
eqResourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqResourceId.setStatus("current")
_EqSeverityLevel_Type = EqSeverityLevel
_EqSeverityLevel_Object = MibScalar
eqSeverityLevel = _EqSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5022, 4, 1, 15),
    _EqSeverityLevel_Type()
)
eqSeverityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqSeverityLevel.setStatus("current")
_EqSystemTraps_ObjectIdentity = ObjectIdentity
eqSystemTraps = _EqSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2)
)
_EqModuleTraps_ObjectIdentity = ObjectIdentity
eqModuleTraps = _EqModuleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3)
)
_EqIfTraps_ObjectIdentity = ObjectIdentity
eqIfTraps = _EqIfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 4)
)
_EqAppsTraps_ObjectIdentity = ObjectIdentity
eqAppsTraps = _EqAppsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5)
)
_EqSrmTraps_ObjectIdentity = ObjectIdentity
eqSrmTraps = _EqSrmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 1)
)
_EqSonetTraps_ObjectIdentity = ObjectIdentity
eqSonetTraps = _EqSonetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2)
)
_EqAtmTraps_ObjectIdentity = ObjectIdentity
eqAtmTraps = _EqAtmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 3)
)
_EqIpTraps_ObjectIdentity = ObjectIdentity
eqIpTraps = _EqIpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 4)
)
_EqMplsTraps_ObjectIdentity = ObjectIdentity
eqMplsTraps = _EqMplsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 5)
)

# Managed Objects groups


# Notification objects

eqHardDiskUsedHiMarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 1)
)
eqHardDiskUsedHiMarkReached.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqHardDiskEid"),
        ("EQUIPE-SYSTEM-MIB", "eqHardDiskUsedHiMark"))
)
if mibBuilder.loadTexts:
    eqHardDiskUsedHiMarkReached.setStatus(
        "current"
    )

eqHardDiskUsedLowMarkReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 2)
)
eqHardDiskUsedLowMarkReached.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqHardDiskEid"),
        ("EQUIPE-SYSTEM-MIB", "eqHardDiskUsedLowMark"))
)
if mibBuilder.loadTexts:
    eqHardDiskUsedLowMarkReached.setStatus(
        "current"
    )

eqFanUnitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 3)
)
eqFanUnitFailed.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqFanUnitEid"))
)
if mibBuilder.loadTexts:
    eqFanUnitFailed.setStatus(
        "current"
    )

eqFanUnitFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 4)
)
eqFanUnitFaulty.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqFanUnitEid"))
)
if mibBuilder.loadTexts:
    eqFanUnitFaulty.setStatus(
        "current"
    )

eqAcctDataWriteToDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 5)
)
eqAcctDataWriteToDiskFailed.setObjects(
    ("EQUIPE-TRAP-MIB", "eqTrapDescr")
)
if mibBuilder.loadTexts:
    eqAcctDataWriteToDiskFailed.setStatus(
        "current"
    )

eqAcctDataFileDeletedBeforeTransfer = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 6)
)
eqAcctDataFileDeletedBeforeTransfer.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-TRAP-MIB", "eqFileName"),
        ("EQUIPE-TRAP-MIB", "eqSystemId"))
)
if mibBuilder.loadTexts:
    eqAcctDataFileDeletedBeforeTransfer.setStatus(
        "current"
    )

eqAcctDataXferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 7)
)
eqAcctDataXferError.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-TRAP-MIB", "eqIpAddress"),
        ("EQUIPE-TRAP-MIB", "eqFileName"),
        ("EQUIPE-TRAP-MIB", "eqSystemId"))
)
if mibBuilder.loadTexts:
    eqAcctDataXferError.setStatus(
        "current"
    )

eqLogServerWriteToDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 8)
)
eqLogServerWriteToDiskFailed.setObjects(
    ("EQUIPE-TRAP-MIB", "eqTrapDescr")
)
if mibBuilder.loadTexts:
    eqLogServerWriteToDiskFailed.setStatus(
        "current"
    )

eqLogDataFileDeletedBeforeTransfer = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 9)
)
eqLogDataFileDeletedBeforeTransfer.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-TRAP-MIB", "eqFileName"),
        ("EQUIPE-TRAP-MIB", "eqSystemId"))
)
if mibBuilder.loadTexts:
    eqLogDataFileDeletedBeforeTransfer.setStatus(
        "current"
    )

eqLogDataXferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 10)
)
eqLogDataXferError.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-TRAP-MIB", "eqIpAddress"),
        ("EQUIPE-TRAP-MIB", "eqFileName"),
        ("EQUIPE-TRAP-MIB", "eqSystemId"))
)
if mibBuilder.loadTexts:
    eqLogDataXferError.setStatus(
        "current"
    )

eqMidPlaneParityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 11)
)
eqMidPlaneParityError.setObjects(
    ("EQUIPE-TRAP-MIB", "eqTrapDescr")
)
if mibBuilder.loadTexts:
    eqMidPlaneParityError.setStatus(
        "current"
    )

eqSonetTimingCfgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 12)
)
eqSonetTimingCfgChanged.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-TRAP-MIB", "eqEid"))
)
if mibBuilder.loadTexts:
    eqSonetTimingCfgChanged.setStatus(
        "current"
    )

eqRisingThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 13)
)
eqRisingThresholdAlert.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-TRAP-MIB", "eqEid"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqEventTime"),
        ("EQUIPE-TRAP-MIB", "eqThresholdValue"),
        ("EQUIPE-TRAP-MIB", "eqCurrentValue"),
        ("EQUIPE-TRAP-MIB", "eqResourceId"),
        ("EQUIPE-TRAP-MIB", "eqSeverityLevel"))
)
if mibBuilder.loadTexts:
    eqRisingThresholdAlert.setStatus(
        "current"
    )

eqFallingThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 2, 14)
)
eqFallingThresholdAlert.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-TRAP-MIB", "eqEid"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqEventTime"),
        ("EQUIPE-TRAP-MIB", "eqThresholdValue"),
        ("EQUIPE-TRAP-MIB", "eqCurrentValue"),
        ("EQUIPE-TRAP-MIB", "eqResourceId"),
        ("EQUIPE-TRAP-MIB", "eqSeverityLevel"))
)
if mibBuilder.loadTexts:
    eqFallingThresholdAlert.setStatus(
        "current"
    )

eqModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 1)
)
eqModuleInserted.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
)
if mibBuilder.loadTexts:
    eqModuleInserted.setStatus(
        "current"
    )

eqModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 2)
)
eqModuleRemoved.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
)
if mibBuilder.loadTexts:
    eqModuleRemoved.setStatus(
        "current"
    )

eqModuleWentOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 3)
)
eqModuleWentOffline.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
)
if mibBuilder.loadTexts:
    eqModuleWentOffline.setStatus(
        "current"
    )

eqModuleReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 4)
)
eqModuleReset.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
)
if mibBuilder.loadTexts:
    eqModuleReset.setStatus(
        "current"
    )

eqModuleFuseBlownMother = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 5)
)
eqModuleFuseBlownMother.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"),
        ("EQUIPE-TRAP-MIB", "eqModuleFuseType"))
)
if mibBuilder.loadTexts:
    eqModuleFuseBlownMother.setStatus(
        "current"
    )

eqModuleFuseBlownDaughter = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 6)
)
eqModuleFuseBlownDaughter.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"),
        ("EQUIPE-TRAP-MIB", "eqModuleFuseType"))
)
if mibBuilder.loadTexts:
    eqModuleFuseBlownDaughter.setStatus(
        "current"
    )

eqModulePowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 7)
)
eqModulePowerSupplyFailed.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
)
if mibBuilder.loadTexts:
    eqModulePowerSupplyFailed.setStatus(
        "current"
    )

eqModuleRedRoleChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 8)
)
eqModuleRedRoleChanged.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleRedOperRole"))
)
if mibBuilder.loadTexts:
    eqModuleRedRoleChanged.setStatus(
        "current"
    )

eqModuleTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 9)
)
eqModuleTypeMismatch.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
)
if mibBuilder.loadTexts:
    eqModuleTypeMismatch.setStatus(
        "current"
    )

eqModuleStratumCentStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 10)
)
eqModuleStratumCentStatusChanged.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"),
        ("EQUIPE-SYSTEM-MIB", "eqStratumCentStatus"))
)
if mibBuilder.loadTexts:
    eqModuleStratumCentStatusChanged.setStatus(
        "current"
    )

eqModuleStratumCentRedStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 3, 11)
)
eqModuleStratumCentRedStatusChanged.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleEid"),
        ("EQUIPE-SYSTEM-MIB", "eqStratumCentRedStatus"))
)
if mibBuilder.loadTexts:
    eqModuleStratumCentRedStatusChanged.setStatus(
        "current"
    )

eqIfAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 4, 1)
)
eqIfAdded.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqIfType"))
)
if mibBuilder.loadTexts:
    eqIfAdded.setStatus(
        "current"
    )

eqIfRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 4, 2)
)
eqIfRemoved.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqIfType"))
)
if mibBuilder.loadTexts:
    eqIfRemoved.setStatus(
        "current"
    )

eqIfModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 4, 3)
)
eqIfModified.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqIfType"))
)
if mibBuilder.loadTexts:
    eqIfModified.setStatus(
        "current"
    )

eqAtmPvcAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 4, 4)
)
eqAtmPvcAdded.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-TRAP-MIB", "eqEid"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqAtmPvcType"))
)
if mibBuilder.loadTexts:
    eqAtmPvcAdded.setStatus(
        "current"
    )

eqAtmPvcRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 4, 5)
)
eqAtmPvcRemoved.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-TRAP-MIB", "eqEid"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqAtmPvcType"))
)
if mibBuilder.loadTexts:
    eqAtmPvcRemoved.setStatus(
        "current"
    )

eqAtmPvcModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 4, 6)
)
eqAtmPvcModified.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("EQUIPE-TRAP-MIB", "eqEid"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqAtmPvcType"))
)
if mibBuilder.loadTexts:
    eqAtmPvcModified.setStatus(
        "current"
    )

eqSrmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 1, 1)
)
eqSrmFault.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqFaultTime"),
        ("EQUIPE-SYSTEM-MIB", "eqFaultScope"),
        ("EQUIPE-SYSTEM-MIB", "eqFaultModule"),
        ("EQUIPE-SYSTEM-MIB", "eqFaultSwlm"))
)
if mibBuilder.loadTexts:
    eqSrmFault.setStatus(
        "current"
    )

eqSonetApsSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 1)
)
eqSonetApsSwitchEvent.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"),
        ("EQUIPE-TRAP-MIB", "eqApsLineState"))
)
if mibBuilder.loadTexts:
    eqSonetApsSwitchEvent.setStatus(
        "current"
    )

eqSonetApsWorkingLineRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 2)
)
eqSonetApsWorkingLineRestored.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"))
)
if mibBuilder.loadTexts:
    eqSonetApsWorkingLineRestored.setStatus(
        "current"
    )

eqSonetApsModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 3)
)
eqSonetApsModeMismatch.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"))
)
if mibBuilder.loadTexts:
    eqSonetApsModeMismatch.setStatus(
        "current"
    )

eqSonetApsProtectLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 4)
)
eqSonetApsProtectLineFailure.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"))
)
if mibBuilder.loadTexts:
    eqSonetApsProtectLineFailure.setStatus(
        "current"
    )

eqSonetApsProtectLineRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 5)
)
eqSonetApsProtectLineRestored.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"))
)
if mibBuilder.loadTexts:
    eqSonetApsProtectLineRestored.setStatus(
        "current"
    )

eqSonetApsProtectByteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 6)
)
eqSonetApsProtectByteFailure.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"))
)
if mibBuilder.loadTexts:
    eqSonetApsProtectByteFailure.setStatus(
        "current"
    )

eqSonetApsFarEndProtectLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 7)
)
eqSonetApsFarEndProtectLineFailure.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"))
)
if mibBuilder.loadTexts:
    eqSonetApsFarEndProtectLineFailure.setStatus(
        "current"
    )

eqSonetApsFarEndProtectLineCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 8)
)
eqSonetApsFarEndProtectLineCleared.setObjects(
      *(("EQUIPE-TRAP-MIB", "eqTrapDescr"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"),
        ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"),
        ("IF-MIB", "ifIndex"),
        ("EQUIPE-TRAP-MIB", "eqIfName"))
)
if mibBuilder.loadTexts:
    eqSonetApsFarEndProtectLineCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQUIPE-TRAP-MIB",
    **{"equipe": equipe,
       "eqTraps": eqTraps,
       "eqTrapObjects": eqTrapObjects,
       "eqSystemId": eqSystemId,
       "eqEid": eqEid,
       "eqIfName": eqIfName,
       "eqIpAddress": eqIpAddress,
       "eqFileName": eqFileName,
       "eqTrapDescr": eqTrapDescr,
       "eqModuleFuseType": eqModuleFuseType,
       "eqApsLineState": eqApsLineState,
       "eqIfType": eqIfType,
       "eqAtmPvcType": eqAtmPvcType,
       "eqEventTime": eqEventTime,
       "eqThresholdValue": eqThresholdValue,
       "eqCurrentValue": eqCurrentValue,
       "eqResourceId": eqResourceId,
       "eqSeverityLevel": eqSeverityLevel,
       "eqSystemTraps": eqSystemTraps,
       "eqHardDiskUsedHiMarkReached": eqHardDiskUsedHiMarkReached,
       "eqHardDiskUsedLowMarkReached": eqHardDiskUsedLowMarkReached,
       "eqFanUnitFailed": eqFanUnitFailed,
       "eqFanUnitFaulty": eqFanUnitFaulty,
       "eqAcctDataWriteToDiskFailed": eqAcctDataWriteToDiskFailed,
       "eqAcctDataFileDeletedBeforeTransfer": eqAcctDataFileDeletedBeforeTransfer,
       "eqAcctDataXferError": eqAcctDataXferError,
       "eqLogServerWriteToDiskFailed": eqLogServerWriteToDiskFailed,
       "eqLogDataFileDeletedBeforeTransfer": eqLogDataFileDeletedBeforeTransfer,
       "eqLogDataXferError": eqLogDataXferError,
       "eqMidPlaneParityError": eqMidPlaneParityError,
       "eqSonetTimingCfgChanged": eqSonetTimingCfgChanged,
       "eqRisingThresholdAlert": eqRisingThresholdAlert,
       "eqFallingThresholdAlert": eqFallingThresholdAlert,
       "eqModuleTraps": eqModuleTraps,
       "eqModuleInserted": eqModuleInserted,
       "eqModuleRemoved": eqModuleRemoved,
       "eqModuleWentOffline": eqModuleWentOffline,
       "eqModuleReset": eqModuleReset,
       "eqModuleFuseBlownMother": eqModuleFuseBlownMother,
       "eqModuleFuseBlownDaughter": eqModuleFuseBlownDaughter,
       "eqModulePowerSupplyFailed": eqModulePowerSupplyFailed,
       "eqModuleRedRoleChanged": eqModuleRedRoleChanged,
       "eqModuleTypeMismatch": eqModuleTypeMismatch,
       "eqModuleStratumCentStatusChanged": eqModuleStratumCentStatusChanged,
       "eqModuleStratumCentRedStatusChanged": eqModuleStratumCentRedStatusChanged,
       "eqIfTraps": eqIfTraps,
       "eqIfAdded": eqIfAdded,
       "eqIfRemoved": eqIfRemoved,
       "eqIfModified": eqIfModified,
       "eqAtmPvcAdded": eqAtmPvcAdded,
       "eqAtmPvcRemoved": eqAtmPvcRemoved,
       "eqAtmPvcModified": eqAtmPvcModified,
       "eqAppsTraps": eqAppsTraps,
       "eqSrmTraps": eqSrmTraps,
       "eqSrmFault": eqSrmFault,
       "eqSonetTraps": eqSonetTraps,
       "eqSonetApsSwitchEvent": eqSonetApsSwitchEvent,
       "eqSonetApsWorkingLineRestored": eqSonetApsWorkingLineRestored,
       "eqSonetApsModeMismatch": eqSonetApsModeMismatch,
       "eqSonetApsProtectLineFailure": eqSonetApsProtectLineFailure,
       "eqSonetApsProtectLineRestored": eqSonetApsProtectLineRestored,
       "eqSonetApsProtectByteFailure": eqSonetApsProtectByteFailure,
       "eqSonetApsFarEndProtectLineFailure": eqSonetApsFarEndProtectLineFailure,
       "eqSonetApsFarEndProtectLineCleared": eqSonetApsFarEndProtectLineCleared,
       "eqAtmTraps": eqAtmTraps,
       "eqIpTraps": eqIpTraps,
       "eqMplsTraps": eqMplsTraps}
)
