# SNMP MIB module (CPQSRVMN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQSRVMN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:44 2024
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

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

_CpqServerManager_ObjectIdentity = ObjectIdentity
cpqServerManager = _CpqServerManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4)
)
_CpqSmMibRev_ObjectIdentity = ObjectIdentity
cpqSmMibRev = _CpqSmMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 1)
)
_CpqSmComponent_ObjectIdentity = ObjectIdentity
cpqSmComponent = _CpqSmComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 2)
)
_CpqSmInterface_ObjectIdentity = ObjectIdentity
cpqSmInterface = _CpqSmInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1)
)
_CpqSmOsNetWare3x_ObjectIdentity = ObjectIdentity
cpqSmOsNetWare3x = _CpqSmOsNetWare3x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1)
)


class _CpqSmNw3xDriverName_Type(DisplayString):
    """Custom type cpqSmNw3xDriverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSmNw3xDriverName_Type.__name__ = "DisplayString"
_CpqSmNw3xDriverName_Object = MibScalar
cpqSmNw3xDriverName = _CpqSmNw3xDriverName_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 1),
    _CpqSmNw3xDriverName_Type()
)
cpqSmNw3xDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverName.setStatus("mandatory")


class _CpqSmNw3xDriverDate_Type(DisplayString):
    """Custom type cpqSmNw3xDriverDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpqSmNw3xDriverDate_Type.__name__ = "DisplayString"
_CpqSmNw3xDriverDate_Object = MibScalar
cpqSmNw3xDriverDate = _CpqSmNw3xDriverDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 2),
    _CpqSmNw3xDriverDate_Type()
)
cpqSmNw3xDriverDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverDate.setStatus("mandatory")


class _CpqSmNw3xDriverVersion_Type(DisplayString):
    """Custom type cpqSmNw3xDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSmNw3xDriverVersion_Type.__name__ = "DisplayString"
_CpqSmNw3xDriverVersion_Object = MibScalar
cpqSmNw3xDriverVersion = _CpqSmNw3xDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 3),
    _CpqSmNw3xDriverVersion_Type()
)
cpqSmNw3xDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverVersion.setStatus("mandatory")
_CpqSmNw3xDriverIssuedCommands_Type = Counter32
_CpqSmNw3xDriverIssuedCommands_Object = MibScalar
cpqSmNw3xDriverIssuedCommands = _CpqSmNw3xDriverIssuedCommands_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 4),
    _CpqSmNw3xDriverIssuedCommands_Type()
)
cpqSmNw3xDriverIssuedCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverIssuedCommands.setStatus("mandatory")
_CpqSmNw3xDriverReceivedCommands_Type = Counter32
_CpqSmNw3xDriverReceivedCommands_Object = MibScalar
cpqSmNw3xDriverReceivedCommands = _CpqSmNw3xDriverReceivedCommands_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 5),
    _CpqSmNw3xDriverReceivedCommands_Type()
)
cpqSmNw3xDriverReceivedCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverReceivedCommands.setStatus("mandatory")


class _CpqSmNw3xDriverWatchdogFrequency_Type(Integer32):
    """Custom type cpqSmNw3xDriverWatchdogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmNw3xDriverWatchdogFrequency_Type.__name__ = "Integer32"
_CpqSmNw3xDriverWatchdogFrequency_Object = MibScalar
cpqSmNw3xDriverWatchdogFrequency = _CpqSmNw3xDriverWatchdogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 6),
    _CpqSmNw3xDriverWatchdogFrequency_Type()
)
cpqSmNw3xDriverWatchdogFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverWatchdogFrequency.setStatus("mandatory")


class _CpqSmNw3xDriverClockSyncFrequency_Type(Integer32):
    """Custom type cpqSmNw3xDriverClockSyncFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSmNw3xDriverClockSyncFrequency_Type.__name__ = "Integer32"
_CpqSmNw3xDriverClockSyncFrequency_Object = MibScalar
cpqSmNw3xDriverClockSyncFrequency = _CpqSmNw3xDriverClockSyncFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 7),
    _CpqSmNw3xDriverClockSyncFrequency_Type()
)
cpqSmNw3xDriverClockSyncFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverClockSyncFrequency.setStatus("mandatory")
_CpqSmNw3xDriverIssuedWatchdogs_Type = Counter32
_CpqSmNw3xDriverIssuedWatchdogs_Object = MibScalar
cpqSmNw3xDriverIssuedWatchdogs = _CpqSmNw3xDriverIssuedWatchdogs_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 8),
    _CpqSmNw3xDriverIssuedWatchdogs_Type()
)
cpqSmNw3xDriverIssuedWatchdogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverIssuedWatchdogs.setStatus("mandatory")
_CpqSmNw3xDriverIssuedClockSyncs_Type = Counter32
_CpqSmNw3xDriverIssuedClockSyncs_Object = MibScalar
cpqSmNw3xDriverIssuedClockSyncs = _CpqSmNw3xDriverIssuedClockSyncs_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 9),
    _CpqSmNw3xDriverIssuedClockSyncs_Type()
)
cpqSmNw3xDriverIssuedClockSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverIssuedClockSyncs.setStatus("mandatory")
_CpqSmNw3xDriverMemoryAllocationFailedErrs_Type = Counter32
_CpqSmNw3xDriverMemoryAllocationFailedErrs_Object = MibScalar
cpqSmNw3xDriverMemoryAllocationFailedErrs = _CpqSmNw3xDriverMemoryAllocationFailedErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 10),
    _CpqSmNw3xDriverMemoryAllocationFailedErrs_Type()
)
cpqSmNw3xDriverMemoryAllocationFailedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverMemoryAllocationFailedErrs.setStatus("mandatory")
_CpqSmNw3xDriverBoardResets_Type = Counter32
_CpqSmNw3xDriverBoardResets_Object = MibScalar
cpqSmNw3xDriverBoardResets = _CpqSmNw3xDriverBoardResets_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 11),
    _CpqSmNw3xDriverBoardResets_Type()
)
cpqSmNw3xDriverBoardResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xDriverBoardResets.setStatus("mandatory")


class _CpqSmNw3xBoardState_Type(Integer32):
    """Custom type cpqSmNw3xBoardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("ok", 2),
          ("other", 1))
    )


_CpqSmNw3xBoardState_Type.__name__ = "Integer32"
_CpqSmNw3xBoardState_Object = MibScalar
cpqSmNw3xBoardState = _CpqSmNw3xBoardState_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 12),
    _CpqSmNw3xBoardState_Type()
)
cpqSmNw3xBoardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmNw3xBoardState.setStatus("mandatory")
_CpqSmCntlr_ObjectIdentity = ObjectIdentity
cpqSmCntlr = _CpqSmCntlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2)
)


class _CpqSmCntlrBoardName_Type(DisplayString):
    """Custom type cpqSmCntlrBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqSmCntlrBoardName_Type.__name__ = "DisplayString"
_CpqSmCntlrBoardName_Object = MibScalar
cpqSmCntlrBoardName = _CpqSmCntlrBoardName_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 1),
    _CpqSmCntlrBoardName_Type()
)
cpqSmCntlrBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrBoardName.setStatus("mandatory")


class _CpqSmCntlrBoardId_Type(DisplayString):
    """Custom type cpqSmCntlrBoardId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqSmCntlrBoardId_Type.__name__ = "DisplayString"
_CpqSmCntlrBoardId_Object = MibScalar
cpqSmCntlrBoardId = _CpqSmCntlrBoardId_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 2),
    _CpqSmCntlrBoardId_Type()
)
cpqSmCntlrBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrBoardId.setStatus("mandatory")


class _CpqSmCntlrRomDate_Type(DisplayString):
    """Custom type cpqSmCntlrRomDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CpqSmCntlrRomDate_Type.__name__ = "DisplayString"
_CpqSmCntlrRomDate_Object = MibScalar
cpqSmCntlrRomDate = _CpqSmCntlrRomDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 3),
    _CpqSmCntlrRomDate_Type()
)
cpqSmCntlrRomDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrRomDate.setStatus("mandatory")


class _CpqSmCntlrCountryCode_Type(DisplayString):
    """Custom type cpqSmCntlrCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CpqSmCntlrCountryCode_Type.__name__ = "DisplayString"
_CpqSmCntlrCountryCode_Object = MibScalar
cpqSmCntlrCountryCode = _CpqSmCntlrCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 4),
    _CpqSmCntlrCountryCode_Type()
)
cpqSmCntlrCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrCountryCode.setStatus("mandatory")


class _CpqSmCntlrVoiceRomStatus_Type(Integer32):
    """Custom type cpqSmCntlrVoiceRomStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installed", 3),
          ("notInstalled", 2),
          ("other", 1))
    )


_CpqSmCntlrVoiceRomStatus_Type.__name__ = "Integer32"
_CpqSmCntlrVoiceRomStatus_Object = MibScalar
cpqSmCntlrVoiceRomStatus = _CpqSmCntlrVoiceRomStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 5),
    _CpqSmCntlrVoiceRomStatus_Type()
)
cpqSmCntlrVoiceRomStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrVoiceRomStatus.setStatus("mandatory")


class _CpqSmCntlrBatteryStatus_Type(Integer32):
    """Custom type cpqSmCntlrBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 3),
          ("other", 1))
    )


_CpqSmCntlrBatteryStatus_Type.__name__ = "Integer32"
_CpqSmCntlrBatteryStatus_Object = MibScalar
cpqSmCntlrBatteryStatus = _CpqSmCntlrBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 6),
    _CpqSmCntlrBatteryStatus_Type()
)
cpqSmCntlrBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrBatteryStatus.setStatus("mandatory")


class _CpqSmCntlrDormantModeStatus_Type(Integer32):
    """Custom type cpqSmCntlrDormantModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dormantOnPowerDown", 3),
          ("normal", 2),
          ("other", 1))
    )


_CpqSmCntlrDormantModeStatus_Type.__name__ = "Integer32"
_CpqSmCntlrDormantModeStatus_Object = MibScalar
cpqSmCntlrDormantModeStatus = _CpqSmCntlrDormantModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 7),
    _CpqSmCntlrDormantModeStatus_Type()
)
cpqSmCntlrDormantModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrDormantModeStatus.setStatus("mandatory")


class _CpqSmCntlrSelfTestErrorCode_Type(Integer32):
    """Custom type cpqSmCntlrSelfTestErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSmCntlrSelfTestErrorCode_Type.__name__ = "Integer32"
_CpqSmCntlrSelfTestErrorCode_Object = MibScalar
cpqSmCntlrSelfTestErrorCode = _CpqSmCntlrSelfTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 8),
    _CpqSmCntlrSelfTestErrorCode_Type()
)
cpqSmCntlrSelfTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrSelfTestErrorCode.setStatus("mandatory")


class _CpqSmCntlrOsId_Type(Integer32):
    """Custom type cpqSmCntlrOsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              177,
              178,
              179,
              180,
              181,
              182)
        )
    )
    namedValues = NamedValues(
        *(("banyan", 181),
          ("dos", 182),
          ("netware286", 177),
          ("netware386", 178),
          ("os2LanManager", 179),
          ("other", 1),
          ("unix", 180))
    )


_CpqSmCntlrOsId_Type.__name__ = "Integer32"
_CpqSmCntlrOsId_Object = MibScalar
cpqSmCntlrOsId = _CpqSmCntlrOsId_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 9),
    _CpqSmCntlrOsId_Type()
)
cpqSmCntlrOsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrOsId.setStatus("mandatory")


class _CpqSmCntlrOsMajorRev_Type(Integer32):
    """Custom type cpqSmCntlrOsMajorRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmCntlrOsMajorRev_Type.__name__ = "Integer32"
_CpqSmCntlrOsMajorRev_Object = MibScalar
cpqSmCntlrOsMajorRev = _CpqSmCntlrOsMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 10),
    _CpqSmCntlrOsMajorRev_Type()
)
cpqSmCntlrOsMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrOsMajorRev.setStatus("mandatory")


class _CpqSmCntlrOsMinorRev_Type(Integer32):
    """Custom type cpqSmCntlrOsMinorRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmCntlrOsMinorRev_Type.__name__ = "Integer32"
_CpqSmCntlrOsMinorRev_Object = MibScalar
cpqSmCntlrOsMinorRev = _CpqSmCntlrOsMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 11),
    _CpqSmCntlrOsMinorRev_Type()
)
cpqSmCntlrOsMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrOsMinorRev.setStatus("mandatory")


class _CpqSmCntlrPostTimeout_Type(Integer32):
    """Custom type cpqSmCntlrPostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CpqSmCntlrPostTimeout_Type.__name__ = "Integer32"
_CpqSmCntlrPostTimeout_Object = MibScalar
cpqSmCntlrPostTimeout = _CpqSmCntlrPostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 12),
    _CpqSmCntlrPostTimeout_Type()
)
cpqSmCntlrPostTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrPostTimeout.setStatus("mandatory")


class _CpqSmCntlrCondition_Type(Integer32):
    """Custom type cpqSmCntlrCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqSmCntlrCondition_Type.__name__ = "Integer32"
_CpqSmCntlrCondition_Object = MibScalar
cpqSmCntlrCondition = _CpqSmCntlrCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 13),
    _CpqSmCntlrCondition_Type()
)
cpqSmCntlrCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCntlrCondition.setStatus("mandatory")
_CpqSmObjData_ObjectIdentity = ObjectIdentity
cpqSmObjData = _CpqSmObjData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3)
)


class _CpqSmObjDataTotalObjects_Type(Integer32):
    """Custom type cpqSmObjDataTotalObjects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSmObjDataTotalObjects_Type.__name__ = "Integer32"
_CpqSmObjDataTotalObjects_Object = MibScalar
cpqSmObjDataTotalObjects = _CpqSmObjDataTotalObjects_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 1),
    _CpqSmObjDataTotalObjects_Type()
)
cpqSmObjDataTotalObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjDataTotalObjects.setStatus("mandatory")


class _CpqSmObjDataObjectTotalSpace_Type(Integer32):
    """Custom type cpqSmObjDataObjectTotalSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSmObjDataObjectTotalSpace_Type.__name__ = "Integer32"
_CpqSmObjDataObjectTotalSpace_Object = MibScalar
cpqSmObjDataObjectTotalSpace = _CpqSmObjDataObjectTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 2),
    _CpqSmObjDataObjectTotalSpace_Type()
)
cpqSmObjDataObjectTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjDataObjectTotalSpace.setStatus("mandatory")


class _CpqSmObjDataObjectSpaceAvailable_Type(Integer32):
    """Custom type cpqSmObjDataObjectSpaceAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqSmObjDataObjectSpaceAvailable_Type.__name__ = "Integer32"
_CpqSmObjDataObjectSpaceAvailable_Object = MibScalar
cpqSmObjDataObjectSpaceAvailable = _CpqSmObjDataObjectSpaceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 3),
    _CpqSmObjDataObjectSpaceAvailable_Type()
)
cpqSmObjDataObjectSpaceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjDataObjectSpaceAvailable.setStatus("mandatory")


class _CpqSmObjDataInnateMonitoringStatus_Type(Integer32):
    """Custom type cpqSmObjDataInnateMonitoringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmObjDataInnateMonitoringStatus_Type.__name__ = "Integer32"
_CpqSmObjDataInnateMonitoringStatus_Object = MibScalar
cpqSmObjDataInnateMonitoringStatus = _CpqSmObjDataInnateMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 4),
    _CpqSmObjDataInnateMonitoringStatus_Type()
)
cpqSmObjDataInnateMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjDataInnateMonitoringStatus.setStatus("mandatory")
_CpqSmObjectTable_Object = MibTable
cpqSmObjectTable = _CpqSmObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cpqSmObjectTable.setStatus("mandatory")
_CpqSmObjectEntry_Object = MibTableRow
cpqSmObjectEntry = _CpqSmObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1)
)
cpqSmObjectEntry.setIndexNames(
    (0, "CPQSRVMN-MIB", "cpqSmObjectIndex"),
    (0, "CPQSRVMN-MIB", "cpqSmObjectInstIndex"),
)
if mibBuilder.loadTexts:
    cpqSmObjectEntry.setStatus("mandatory")


class _CpqSmObjectIndex_Type(Integer32):
    """Custom type cpqSmObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpqSmObjectIndex_Type.__name__ = "Integer32"
_CpqSmObjectIndex_Object = MibTableColumn
cpqSmObjectIndex = _CpqSmObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 1),
    _CpqSmObjectIndex_Type()
)
cpqSmObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjectIndex.setStatus("mandatory")


class _CpqSmObjectInstIndex_Type(Integer32):
    """Custom type cpqSmObjectInstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmObjectInstIndex_Type.__name__ = "Integer32"
_CpqSmObjectInstIndex_Object = MibTableColumn
cpqSmObjectInstIndex = _CpqSmObjectInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 2),
    _CpqSmObjectInstIndex_Type()
)
cpqSmObjectInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjectInstIndex.setStatus("mandatory")
_CpqSmObjectClass_Type = Integer32
_CpqSmObjectClass_Object = MibTableColumn
cpqSmObjectClass = _CpqSmObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 3),
    _CpqSmObjectClass_Type()
)
cpqSmObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjectClass.setStatus("mandatory")


class _CpqSmObjectLabel_Type(DisplayString):
    """Custom type cpqSmObjectLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqSmObjectLabel_Type.__name__ = "DisplayString"
_CpqSmObjectLabel_Object = MibTableColumn
cpqSmObjectLabel = _CpqSmObjectLabel_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 4),
    _CpqSmObjectLabel_Type()
)
cpqSmObjectLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmObjectLabel.setStatus("mandatory")
_CpqSmMonItemTable_Object = MibTable
cpqSmMonItemTable = _CpqSmMonItemTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6)
)
if mibBuilder.loadTexts:
    cpqSmMonItemTable.setStatus("mandatory")
_CpqSmMonItemEntry_Object = MibTableRow
cpqSmMonItemEntry = _CpqSmMonItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1)
)
cpqSmMonItemEntry.setIndexNames(
    (0, "CPQSRVMN-MIB", "cpqSmMonItemObjIndex"),
    (0, "CPQSRVMN-MIB", "cpqSmMonItemInstIndex"),
    (0, "CPQSRVMN-MIB", "cpqSmMonItemIndex"),
)
if mibBuilder.loadTexts:
    cpqSmMonItemEntry.setStatus("mandatory")


class _CpqSmMonItemObjIndex_Type(Integer32):
    """Custom type cpqSmMonItemObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CpqSmMonItemObjIndex_Type.__name__ = "Integer32"
_CpqSmMonItemObjIndex_Object = MibTableColumn
cpqSmMonItemObjIndex = _CpqSmMonItemObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 1),
    _CpqSmMonItemObjIndex_Type()
)
cpqSmMonItemObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemObjIndex.setStatus("mandatory")


class _CpqSmMonItemInstIndex_Type(Integer32):
    """Custom type cpqSmMonItemInstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmMonItemInstIndex_Type.__name__ = "Integer32"
_CpqSmMonItemInstIndex_Object = MibTableColumn
cpqSmMonItemInstIndex = _CpqSmMonItemInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 2),
    _CpqSmMonItemInstIndex_Type()
)
cpqSmMonItemInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemInstIndex.setStatus("mandatory")


class _CpqSmMonItemIndex_Type(Integer32):
    """Custom type cpqSmMonItemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmMonItemIndex_Type.__name__ = "Integer32"
_CpqSmMonItemIndex_Object = MibTableColumn
cpqSmMonItemIndex = _CpqSmMonItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 3),
    _CpqSmMonItemIndex_Type()
)
cpqSmMonItemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemIndex.setStatus("mandatory")


class _CpqSmMonItemOnNetAlertStatus_Type(Integer32):
    """Custom type cpqSmMonItemOnNetAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmMonItemOnNetAlertStatus_Type.__name__ = "Integer32"
_CpqSmMonItemOnNetAlertStatus_Object = MibTableColumn
cpqSmMonItemOnNetAlertStatus = _CpqSmMonItemOnNetAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 4),
    _CpqSmMonItemOnNetAlertStatus_Type()
)
cpqSmMonItemOnNetAlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemOnNetAlertStatus.setStatus("mandatory")


class _CpqSmMonItemRemoteAlertStatus_Type(Integer32):
    """Custom type cpqSmMonItemRemoteAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmMonItemRemoteAlertStatus_Type.__name__ = "Integer32"
_CpqSmMonItemRemoteAlertStatus_Object = MibTableColumn
cpqSmMonItemRemoteAlertStatus = _CpqSmMonItemRemoteAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 5),
    _CpqSmMonItemRemoteAlertStatus_Type()
)
cpqSmMonItemRemoteAlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemRemoteAlertStatus.setStatus("mandatory")


class _CpqSmMonItemInnateStatus_Type(Integer32):
    """Custom type cpqSmMonItemInnateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("externallyManaged", 2),
          ("innate", 3),
          ("other", 1))
    )


_CpqSmMonItemInnateStatus_Type.__name__ = "Integer32"
_CpqSmMonItemInnateStatus_Object = MibTableColumn
cpqSmMonItemInnateStatus = _CpqSmMonItemInnateStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 6),
    _CpqSmMonItemInnateStatus_Type()
)
cpqSmMonItemInnateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemInnateStatus.setStatus("mandatory")


class _CpqSmMonItemHostNotify_Type(Integer32):
    """Custom type cpqSmMonItemHostNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmMonItemHostNotify_Type.__name__ = "Integer32"
_CpqSmMonItemHostNotify_Object = MibTableColumn
cpqSmMonItemHostNotify = _CpqSmMonItemHostNotify_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 7),
    _CpqSmMonItemHostNotify_Type()
)
cpqSmMonItemHostNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemHostNotify.setStatus("mandatory")


class _CpqSmMonItemLogicalOperator_Type(Integer32):
    """Custom type cpqSmMonItemLogicalOperator based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("greaterThan", 5),
          ("greaterThanOrEqual", 7),
          ("inside", 8),
          ("lessThan", 4),
          ("lessThanOrEqual", 6),
          ("notEqual", 3),
          ("other", 1),
          ("outside", 9))
    )


_CpqSmMonItemLogicalOperator_Type.__name__ = "Integer32"
_CpqSmMonItemLogicalOperator_Object = MibTableColumn
cpqSmMonItemLogicalOperator = _CpqSmMonItemLogicalOperator_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 8),
    _CpqSmMonItemLogicalOperator_Type()
)
cpqSmMonItemLogicalOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemLogicalOperator.setStatus("mandatory")


class _CpqSmMonItemSeverity_Type(Integer32):
    """Custom type cpqSmMonItemSeverity based on Integer32"""
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
        *(("catastrophic", 5),
          ("critical", 4),
          ("other", 1),
          ("status", 2),
          ("warning", 3))
    )


_CpqSmMonItemSeverity_Type.__name__ = "Integer32"
_CpqSmMonItemSeverity_Object = MibTableColumn
cpqSmMonItemSeverity = _CpqSmMonItemSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 9),
    _CpqSmMonItemSeverity_Type()
)
cpqSmMonItemSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemSeverity.setStatus("mandatory")


class _CpqSmMonItemDataType_Type(Integer32):
    """Custom type cpqSmMonItemDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("data", 6),
          ("other", 1),
          ("queue", 7),
          ("range", 4),
          ("state", 3),
          ("string", 5))
    )


_CpqSmMonItemDataType_Type.__name__ = "Integer32"
_CpqSmMonItemDataType_Object = MibTableColumn
cpqSmMonItemDataType = _CpqSmMonItemDataType_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 10),
    _CpqSmMonItemDataType_Type()
)
cpqSmMonItemDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemDataType.setStatus("mandatory")


class _CpqSmMonItemVoiceMsgNum_Type(Integer32):
    """Custom type cpqSmMonItemVoiceMsgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_CpqSmMonItemVoiceMsgNum_Type.__name__ = "Integer32"
_CpqSmMonItemVoiceMsgNum_Object = MibTableColumn
cpqSmMonItemVoiceMsgNum = _CpqSmMonItemVoiceMsgNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 11),
    _CpqSmMonItemVoiceMsgNum_Type()
)
cpqSmMonItemVoiceMsgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemVoiceMsgNum.setStatus("mandatory")


class _CpqSmMonItemLabel_Type(DisplayString):
    """Custom type cpqSmMonItemLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqSmMonItemLabel_Type.__name__ = "DisplayString"
_CpqSmMonItemLabel_Object = MibTableColumn
cpqSmMonItemLabel = _CpqSmMonItemLabel_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 12),
    _CpqSmMonItemLabel_Type()
)
cpqSmMonItemLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemLabel.setStatus("mandatory")
_CpqSmMonItemLimit_Type = Integer32
_CpqSmMonItemLimit_Object = MibTableColumn
cpqSmMonItemLimit = _CpqSmMonItemLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 13),
    _CpqSmMonItemLimit_Type()
)
cpqSmMonItemLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemLimit.setStatus("mandatory")
_CpqSmMonItemOptional_Type = Integer32
_CpqSmMonItemOptional_Object = MibTableColumn
cpqSmMonItemOptional = _CpqSmMonItemOptional_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 14),
    _CpqSmMonItemOptional_Type()
)
cpqSmMonItemOptional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemOptional.setStatus("mandatory")
_CpqSmMonItemDefVal_Type = Integer32
_CpqSmMonItemDefVal_Object = MibTableColumn
cpqSmMonItemDefVal = _CpqSmMonItemDefVal_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 15),
    _CpqSmMonItemDefVal_Type()
)
cpqSmMonItemDefVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemDefVal.setStatus("mandatory")
_CpqSmMonItemCurVal_Type = Integer32
_CpqSmMonItemCurVal_Object = MibTableColumn
cpqSmMonItemCurVal = _CpqSmMonItemCurVal_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 16),
    _CpqSmMonItemCurVal_Type()
)
cpqSmMonItemCurVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemCurVal.setStatus("mandatory")


class _CpqSmMonItemCurString_Type(DisplayString):
    """Custom type cpqSmMonItemCurString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqSmMonItemCurString_Type.__name__ = "DisplayString"
_CpqSmMonItemCurString_Object = MibTableColumn
cpqSmMonItemCurString = _CpqSmMonItemCurString_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 17),
    _CpqSmMonItemCurString_Type()
)
cpqSmMonItemCurString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemCurString.setStatus("mandatory")


class _CpqSmMonItemCurContents_Type(OctetString):
    """Custom type cpqSmMonItemCurContents based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpqSmMonItemCurContents_Type.__name__ = "OctetString"
_CpqSmMonItemCurContents_Object = MibTableColumn
cpqSmMonItemCurContents = _CpqSmMonItemCurContents_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 18),
    _CpqSmMonItemCurContents_Type()
)
cpqSmMonItemCurContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemCurContents.setStatus("mandatory")


class _CpqSmMonItemTimeStamp_Type(OctetString):
    """Custom type cpqSmMonItemTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqSmMonItemTimeStamp_Type.__name__ = "OctetString"
_CpqSmMonItemTimeStamp_Object = MibTableColumn
cpqSmMonItemTimeStamp = _CpqSmMonItemTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 19),
    _CpqSmMonItemTimeStamp_Type()
)
cpqSmMonItemTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmMonItemTimeStamp.setStatus("mandatory")
_CpqSmAsyncComm_ObjectIdentity = ObjectIdentity
cpqSmAsyncComm = _CpqSmAsyncComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4)
)


class _CpqSmCommAsyncCommunicationStatus_Type(Integer32):
    """Custom type cpqSmCommAsyncCommunicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmCommAsyncCommunicationStatus_Type.__name__ = "Integer32"
_CpqSmCommAsyncCommunicationStatus_Object = MibScalar
cpqSmCommAsyncCommunicationStatus = _CpqSmCommAsyncCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 1),
    _CpqSmCommAsyncCommunicationStatus_Type()
)
cpqSmCommAsyncCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCommAsyncCommunicationStatus.setStatus("mandatory")


class _CpqSmCommInternalModemMaxBaudRate_Type(Integer32):
    """Custom type cpqSmCommInternalModemMaxBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSmCommInternalModemMaxBaudRate_Type.__name__ = "Integer32"
_CpqSmCommInternalModemMaxBaudRate_Object = MibScalar
cpqSmCommInternalModemMaxBaudRate = _CpqSmCommInternalModemMaxBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 2),
    _CpqSmCommInternalModemMaxBaudRate_Type()
)
cpqSmCommInternalModemMaxBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCommInternalModemMaxBaudRate.setStatus("mandatory")


class _CpqSmCommAudibleIndicatorStatus_Type(Integer32):
    """Custom type cpqSmCommAudibleIndicatorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmCommAudibleIndicatorStatus_Type.__name__ = "Integer32"
_CpqSmCommAudibleIndicatorStatus_Object = MibScalar
cpqSmCommAudibleIndicatorStatus = _CpqSmCommAudibleIndicatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 3),
    _CpqSmCommAudibleIndicatorStatus_Type()
)
cpqSmCommAudibleIndicatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCommAudibleIndicatorStatus.setStatus("mandatory")


class _CpqSmCommRemoteSessionStatus_Type(Integer32):
    """Custom type cpqSmCommRemoteSessionStatus based on Integer32"""
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
        *(("noSessionActive", 3),
          ("notSupported", 2),
          ("other", 1),
          ("pgrVoiceSessionActive", 5),
          ("remoteConsoleActive", 6),
          ("remoteSessionActive", 4))
    )


_CpqSmCommRemoteSessionStatus_Type.__name__ = "Integer32"
_CpqSmCommRemoteSessionStatus_Object = MibScalar
cpqSmCommRemoteSessionStatus = _CpqSmCommRemoteSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 4),
    _CpqSmCommRemoteSessionStatus_Type()
)
cpqSmCommRemoteSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCommRemoteSessionStatus.setStatus("mandatory")


class _CpqSmCommCallbackStatus_Type(Integer32):
    """Custom type cpqSmCommCallbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmCommCallbackStatus_Type.__name__ = "Integer32"
_CpqSmCommCallbackStatus_Object = MibScalar
cpqSmCommCallbackStatus = _CpqSmCommCallbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 5),
    _CpqSmCommCallbackStatus_Type()
)
cpqSmCommCallbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmCommCallbackStatus.setStatus("mandatory")
_CpqSmModemSettingsTable_Object = MibTable
cpqSmModemSettingsTable = _CpqSmModemSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6)
)
if mibBuilder.loadTexts:
    cpqSmModemSettingsTable.setStatus("mandatory")
_CpqSmModemSettingsEntry_Object = MibTableRow
cpqSmModemSettingsEntry = _CpqSmModemSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1)
)
cpqSmModemSettingsEntry.setIndexNames(
    (0, "CPQSRVMN-MIB", "cpqSmModemSettingsIndex"),
)
if mibBuilder.loadTexts:
    cpqSmModemSettingsEntry.setStatus("mandatory")


class _CpqSmModemSettingsIndex_Type(Integer32):
    """Custom type cpqSmModemSettingsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(48,
              49,
              50)
        )
    )
    namedValues = NamedValues(
        *(("externalModem", 49),
          ("internalModem", 48),
          ("pager", 50))
    )


_CpqSmModemSettingsIndex_Type.__name__ = "Integer32"
_CpqSmModemSettingsIndex_Object = MibTableColumn
cpqSmModemSettingsIndex = _CpqSmModemSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 1),
    _CpqSmModemSettingsIndex_Type()
)
cpqSmModemSettingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsIndex.setStatus("mandatory")


class _CpqSmModemSettingsStatus_Type(Integer32):
    """Custom type cpqSmModemSettingsStatus based on Integer32"""
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
        *(("internalIntnlModem", 4),
          ("internalUSModem", 3),
          ("noInternalModem", 2),
          ("other", 1),
          ("pagerInformationData", 8),
          ("serialDirectConnect", 6),
          ("serialExternalModem", 7),
          ("serialPortNotSetup", 5))
    )


_CpqSmModemSettingsStatus_Type.__name__ = "Integer32"
_CpqSmModemSettingsStatus_Object = MibTableColumn
cpqSmModemSettingsStatus = _CpqSmModemSettingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 2),
    _CpqSmModemSettingsStatus_Type()
)
cpqSmModemSettingsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsStatus.setStatus("mandatory")


class _CpqSmModemSettingsBaudRate_Type(Integer32):
    """Custom type cpqSmModemSettingsBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSmModemSettingsBaudRate_Type.__name__ = "Integer32"
_CpqSmModemSettingsBaudRate_Object = MibTableColumn
cpqSmModemSettingsBaudRate = _CpqSmModemSettingsBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 3),
    _CpqSmModemSettingsBaudRate_Type()
)
cpqSmModemSettingsBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsBaudRate.setStatus("mandatory")


class _CpqSmModemSettingsParity_Type(Integer32):
    """Custom type cpqSmModemSettingsParity based on Integer32"""
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
        *(("even", 4),
          ("none", 2),
          ("odd", 3),
          ("other", 1))
    )


_CpqSmModemSettingsParity_Type.__name__ = "Integer32"
_CpqSmModemSettingsParity_Object = MibTableColumn
cpqSmModemSettingsParity = _CpqSmModemSettingsParity_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 4),
    _CpqSmModemSettingsParity_Type()
)
cpqSmModemSettingsParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsParity.setStatus("mandatory")


class _CpqSmModemSettingsDataLength_Type(Integer32):
    """Custom type cpqSmModemSettingsDataLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmModemSettingsDataLength_Type.__name__ = "Integer32"
_CpqSmModemSettingsDataLength_Object = MibTableColumn
cpqSmModemSettingsDataLength = _CpqSmModemSettingsDataLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 5),
    _CpqSmModemSettingsDataLength_Type()
)
cpqSmModemSettingsDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsDataLength.setStatus("mandatory")


class _CpqSmModemSettingsStopBits_Type(Integer32):
    """Custom type cpqSmModemSettingsStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CpqSmModemSettingsStopBits_Type.__name__ = "Integer32"
_CpqSmModemSettingsStopBits_Object = MibTableColumn
cpqSmModemSettingsStopBits = _CpqSmModemSettingsStopBits_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 6),
    _CpqSmModemSettingsStopBits_Type()
)
cpqSmModemSettingsStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsStopBits.setStatus("mandatory")


class _CpqSmModemSettingsDialString_Type(DisplayString):
    """Custom type cpqSmModemSettingsDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSmModemSettingsDialString_Type.__name__ = "DisplayString"
_CpqSmModemSettingsDialString_Object = MibTableColumn
cpqSmModemSettingsDialString = _CpqSmModemSettingsDialString_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 7),
    _CpqSmModemSettingsDialString_Type()
)
cpqSmModemSettingsDialString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsDialString.setStatus("mandatory")


class _CpqSmModemSettingsHangUpString_Type(DisplayString):
    """Custom type cpqSmModemSettingsHangUpString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSmModemSettingsHangUpString_Type.__name__ = "DisplayString"
_CpqSmModemSettingsHangUpString_Object = MibTableColumn
cpqSmModemSettingsHangUpString = _CpqSmModemSettingsHangUpString_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 8),
    _CpqSmModemSettingsHangUpString_Type()
)
cpqSmModemSettingsHangUpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsHangUpString.setStatus("mandatory")


class _CpqSmModemSettingsAnswerString_Type(DisplayString):
    """Custom type cpqSmModemSettingsAnswerString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSmModemSettingsAnswerString_Type.__name__ = "DisplayString"
_CpqSmModemSettingsAnswerString_Object = MibTableColumn
cpqSmModemSettingsAnswerString = _CpqSmModemSettingsAnswerString_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 9),
    _CpqSmModemSettingsAnswerString_Type()
)
cpqSmModemSettingsAnswerString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsAnswerString.setStatus("mandatory")


class _CpqSmModemSettingsOriginateString_Type(DisplayString):
    """Custom type cpqSmModemSettingsOriginateString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSmModemSettingsOriginateString_Type.__name__ = "DisplayString"
_CpqSmModemSettingsOriginateString_Object = MibTableColumn
cpqSmModemSettingsOriginateString = _CpqSmModemSettingsOriginateString_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 10),
    _CpqSmModemSettingsOriginateString_Type()
)
cpqSmModemSettingsOriginateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmModemSettingsOriginateString.setStatus("mandatory")
_CpqSmAlert_ObjectIdentity = ObjectIdentity
cpqSmAlert = _CpqSmAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5)
)


class _CpqSmAlertStatus_Type(Integer32):
    """Custom type cpqSmAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CpqSmAlertStatus_Type.__name__ = "Integer32"
_CpqSmAlertStatus_Object = MibScalar
cpqSmAlertStatus = _CpqSmAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 1),
    _CpqSmAlertStatus_Type()
)
cpqSmAlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertStatus.setStatus("mandatory")
_CpqSmAlertDestTable_Object = MibTable
cpqSmAlertDestTable = _CpqSmAlertDestTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cpqSmAlertDestTable.setStatus("mandatory")
_CpqSmAlertDestEntry_Object = MibTableRow
cpqSmAlertDestEntry = _CpqSmAlertDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1)
)
cpqSmAlertDestEntry.setIndexNames(
    (0, "CPQSRVMN-MIB", "cpqSmAlertDestPriorityIndex"),
)
if mibBuilder.loadTexts:
    cpqSmAlertDestEntry.setStatus("mandatory")


class _CpqSmAlertDestPriorityIndex_Type(Integer32):
    """Custom type cpqSmAlertDestPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqSmAlertDestPriorityIndex_Type.__name__ = "Integer32"
_CpqSmAlertDestPriorityIndex_Object = MibTableColumn
cpqSmAlertDestPriorityIndex = _CpqSmAlertDestPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 1),
    _CpqSmAlertDestPriorityIndex_Type()
)
cpqSmAlertDestPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestPriorityIndex.setStatus("mandatory")


class _CpqSmAlertDestType_Type(Integer32):
    """Custom type cpqSmAlertDestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              161,
              162,
              163,
              164,
              165,
              166)
        )
    )
    namedValues = NamedValues(
        *(("externalDirectToSmf", 166),
          ("externalModemToPager", 165),
          ("externalModemToSmf", 164),
          ("internalModemToPager", 162),
          ("internalModemToSmf", 161),
          ("internalModemToVoice", 163),
          ("other", 1))
    )


_CpqSmAlertDestType_Type.__name__ = "Integer32"
_CpqSmAlertDestType_Object = MibTableColumn
cpqSmAlertDestType = _CpqSmAlertDestType_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 2),
    _CpqSmAlertDestType_Type()
)
cpqSmAlertDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestType.setStatus("mandatory")


class _CpqSmAlertDestRetries_Type(Integer32):
    """Custom type cpqSmAlertDestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CpqSmAlertDestRetries_Type.__name__ = "Integer32"
_CpqSmAlertDestRetries_Object = MibTableColumn
cpqSmAlertDestRetries = _CpqSmAlertDestRetries_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 3),
    _CpqSmAlertDestRetries_Type()
)
cpqSmAlertDestRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestRetries.setStatus("mandatory")


class _CpqSmAlertDestConnectFlags_Type(Integer32):
    """Custom type cpqSmAlertDestConnectFlags based on Integer32"""
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
        *(("alertAndCallback", 4),
          ("alertOnly", 2),
          ("callbackOnly", 3),
          ("other", 1))
    )


_CpqSmAlertDestConnectFlags_Type.__name__ = "Integer32"
_CpqSmAlertDestConnectFlags_Object = MibTableColumn
cpqSmAlertDestConnectFlags = _CpqSmAlertDestConnectFlags_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 4),
    _CpqSmAlertDestConnectFlags_Type()
)
cpqSmAlertDestConnectFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestConnectFlags.setStatus("mandatory")


class _CpqSmAlertDestPhoneNumber_Type(DisplayString):
    """Custom type cpqSmAlertDestPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CpqSmAlertDestPhoneNumber_Type.__name__ = "DisplayString"
_CpqSmAlertDestPhoneNumber_Object = MibTableColumn
cpqSmAlertDestPhoneNumber = _CpqSmAlertDestPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 5),
    _CpqSmAlertDestPhoneNumber_Type()
)
cpqSmAlertDestPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestPhoneNumber.setStatus("mandatory")


class _CpqSmAlertDestTimeMask_Type(OctetString):
    """Custom type cpqSmAlertDestTimeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 21),
    )


_CpqSmAlertDestTimeMask_Type.__name__ = "OctetString"
_CpqSmAlertDestTimeMask_Object = MibTableColumn
cpqSmAlertDestTimeMask = _CpqSmAlertDestTimeMask_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 6),
    _CpqSmAlertDestTimeMask_Type()
)
cpqSmAlertDestTimeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestTimeMask.setStatus("mandatory")


class _CpqSmAlertDestPagerType_Type(Integer32):
    """Custom type cpqSmAlertDestPagerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alphanumeric", 3),
          ("numericOnly", 2),
          ("other", 1))
    )


_CpqSmAlertDestPagerType_Type.__name__ = "Integer32"
_CpqSmAlertDestPagerType_Object = MibTableColumn
cpqSmAlertDestPagerType = _CpqSmAlertDestPagerType_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 7),
    _CpqSmAlertDestPagerType_Type()
)
cpqSmAlertDestPagerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestPagerType.setStatus("mandatory")


class _CpqSmAlertDestPagerId_Type(DisplayString):
    """Custom type cpqSmAlertDestPagerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqSmAlertDestPagerId_Type.__name__ = "DisplayString"
_CpqSmAlertDestPagerId_Object = MibTableColumn
cpqSmAlertDestPagerId = _CpqSmAlertDestPagerId_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 8),
    _CpqSmAlertDestPagerId_Type()
)
cpqSmAlertDestPagerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestPagerId.setStatus("mandatory")


class _CpqSmAlertDestPagerDisplayLength_Type(Integer32):
    """Custom type cpqSmAlertDestPagerDisplayLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_CpqSmAlertDestPagerDisplayLength_Type.__name__ = "Integer32"
_CpqSmAlertDestPagerDisplayLength_Object = MibTableColumn
cpqSmAlertDestPagerDisplayLength = _CpqSmAlertDestPagerDisplayLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 9),
    _CpqSmAlertDestPagerDisplayLength_Type()
)
cpqSmAlertDestPagerDisplayLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmAlertDestPagerDisplayLength.setStatus("mandatory")
_CpqSmTrap_ObjectIdentity = ObjectIdentity
cpqSmTrap = _CpqSmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 4, 3)
)
_CpqSmTrapPkts_Type = Counter32
_CpqSmTrapPkts_Object = MibScalar
cpqSmTrapPkts = _CpqSmTrapPkts_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 3, 1),
    _CpqSmTrapPkts_Type()
)
cpqSmTrapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmTrapPkts.setStatus("mandatory")


class _CpqSmTrapLogMaxSize_Type(Integer32):
    """Custom type cpqSmTrapLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSmTrapLogMaxSize_Type.__name__ = "Integer32"
_CpqSmTrapLogMaxSize_Object = MibScalar
cpqSmTrapLogMaxSize = _CpqSmTrapLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 3, 2),
    _CpqSmTrapLogMaxSize_Type()
)
cpqSmTrapLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmTrapLogMaxSize.setStatus("mandatory")
_CpqSmTrapLogTable_Object = MibTable
cpqSmTrapLogTable = _CpqSmTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 3, 3)
)
if mibBuilder.loadTexts:
    cpqSmTrapLogTable.setStatus("mandatory")
_CpqSmTrapLogEntry_Object = MibTableRow
cpqSmTrapLogEntry = _CpqSmTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1)
)
cpqSmTrapLogEntry.setIndexNames(
    (0, "CPQSRVMN-MIB", "cpqSmTrapLogIndex"),
)
if mibBuilder.loadTexts:
    cpqSmTrapLogEntry.setStatus("mandatory")


class _CpqSmTrapLogIndex_Type(Integer32):
    """Custom type cpqSmTrapLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqSmTrapLogIndex_Type.__name__ = "Integer32"
_CpqSmTrapLogIndex_Object = MibTableColumn
cpqSmTrapLogIndex = _CpqSmTrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1, 1),
    _CpqSmTrapLogIndex_Type()
)
cpqSmTrapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmTrapLogIndex.setStatus("mandatory")


class _CpqSmTrapType_Type(Integer32):
    """Custom type cpqSmTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cpqSmAlertDestinationBlacklisted", 7),
          ("cpqSmBatteryFailed", 5),
          ("cpqSmBoardFailed", 1),
          ("cpqSmBoardReset", 2),
          ("cpqSmBoardTimeout", 6),
          ("cpqSmCommFailed", 4),
          ("cpqSmServerManagerAlert", 3))
    )


_CpqSmTrapType_Type.__name__ = "Integer32"
_CpqSmTrapType_Object = MibTableColumn
cpqSmTrapType = _CpqSmTrapType_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1, 2),
    _CpqSmTrapType_Type()
)
cpqSmTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmTrapType.setStatus("mandatory")


class _CpqSmTrapTime_Type(OctetString):
    """Custom type cpqSmTrapTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CpqSmTrapTime_Type.__name__ = "OctetString"
_CpqSmTrapTime_Object = MibTableColumn
cpqSmTrapTime = _CpqSmTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1, 3),
    _CpqSmTrapTime_Type()
)
cpqSmTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqSmTrapTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqSmBoardFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 4, 0, 1)
)
if mibBuilder.loadTexts:
    cpqSmBoardFailed.setStatus(
        ""
    )

cpqSmBoardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 4, 0, 2)
)
if mibBuilder.loadTexts:
    cpqSmBoardReset.setStatus(
        ""
    )

cpqSmServerManagerAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 4, 0, 3)
)
cpqSmServerManagerAlert.setObjects(
      *(("CPQSRVMN-MIB", "cpqSmMonItemCurVal"),
        ("CPQSRVMN-MIB", "cpqSmObjectLabel"),
        ("CPQSRVMN-MIB", "cpqSmMonItemLabel"),
        ("CPQSRVMN-MIB", "cpqSmMonItemDataType"),
        ("CPQSRVMN-MIB", "cpqSmMonItemSeverity"),
        ("CPQSRVMN-MIB", "cpqSmMonItemLimit"),
        ("CPQSRVMN-MIB", "cpqSmMonItemOptional"),
        ("CPQSRVMN-MIB", "cpqSmMonItemLogicalOperator"),
        ("CPQSRVMN-MIB", "cpqSmMonItemTimeStamp"))
)
if mibBuilder.loadTexts:
    cpqSmServerManagerAlert.setStatus(
        ""
    )

cpqSmCommFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 4, 0, 4)
)
if mibBuilder.loadTexts:
    cpqSmCommFailed.setStatus(
        ""
    )

cpqSmBatteryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 4, 0, 5)
)
if mibBuilder.loadTexts:
    cpqSmBatteryFailed.setStatus(
        ""
    )

cpqSmBoardTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 4, 0, 6)
)
if mibBuilder.loadTexts:
    cpqSmBoardTimeout.setStatus(
        ""
    )

cpqSmAlertDestinationBlacklisted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 4, 0, 7)
)
cpqSmAlertDestinationBlacklisted.setObjects(
      *(("CPQSRVMN-MIB", "cpqSmAlertDestType"),
        ("CPQSRVMN-MIB", "cpqSmAlertDestPhoneNumber"),
        ("CPQSRVMN-MIB", "cpqSmAlertDestPagerId"))
)
if mibBuilder.loadTexts:
    cpqSmAlertDestinationBlacklisted.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSRVMN-MIB",
    **{"cpqServerManager": cpqServerManager,
       "cpqSmBoardFailed": cpqSmBoardFailed,
       "cpqSmBoardReset": cpqSmBoardReset,
       "cpqSmServerManagerAlert": cpqSmServerManagerAlert,
       "cpqSmCommFailed": cpqSmCommFailed,
       "cpqSmBatteryFailed": cpqSmBatteryFailed,
       "cpqSmBoardTimeout": cpqSmBoardTimeout,
       "cpqSmAlertDestinationBlacklisted": cpqSmAlertDestinationBlacklisted,
       "cpqSmMibRev": cpqSmMibRev,
       "cpqSmComponent": cpqSmComponent,
       "cpqSmInterface": cpqSmInterface,
       "cpqSmOsNetWare3x": cpqSmOsNetWare3x,
       "cpqSmNw3xDriverName": cpqSmNw3xDriverName,
       "cpqSmNw3xDriverDate": cpqSmNw3xDriverDate,
       "cpqSmNw3xDriverVersion": cpqSmNw3xDriverVersion,
       "cpqSmNw3xDriverIssuedCommands": cpqSmNw3xDriverIssuedCommands,
       "cpqSmNw3xDriverReceivedCommands": cpqSmNw3xDriverReceivedCommands,
       "cpqSmNw3xDriverWatchdogFrequency": cpqSmNw3xDriverWatchdogFrequency,
       "cpqSmNw3xDriverClockSyncFrequency": cpqSmNw3xDriverClockSyncFrequency,
       "cpqSmNw3xDriverIssuedWatchdogs": cpqSmNw3xDriverIssuedWatchdogs,
       "cpqSmNw3xDriverIssuedClockSyncs": cpqSmNw3xDriverIssuedClockSyncs,
       "cpqSmNw3xDriverMemoryAllocationFailedErrs": cpqSmNw3xDriverMemoryAllocationFailedErrs,
       "cpqSmNw3xDriverBoardResets": cpqSmNw3xDriverBoardResets,
       "cpqSmNw3xBoardState": cpqSmNw3xBoardState,
       "cpqSmCntlr": cpqSmCntlr,
       "cpqSmCntlrBoardName": cpqSmCntlrBoardName,
       "cpqSmCntlrBoardId": cpqSmCntlrBoardId,
       "cpqSmCntlrRomDate": cpqSmCntlrRomDate,
       "cpqSmCntlrCountryCode": cpqSmCntlrCountryCode,
       "cpqSmCntlrVoiceRomStatus": cpqSmCntlrVoiceRomStatus,
       "cpqSmCntlrBatteryStatus": cpqSmCntlrBatteryStatus,
       "cpqSmCntlrDormantModeStatus": cpqSmCntlrDormantModeStatus,
       "cpqSmCntlrSelfTestErrorCode": cpqSmCntlrSelfTestErrorCode,
       "cpqSmCntlrOsId": cpqSmCntlrOsId,
       "cpqSmCntlrOsMajorRev": cpqSmCntlrOsMajorRev,
       "cpqSmCntlrOsMinorRev": cpqSmCntlrOsMinorRev,
       "cpqSmCntlrPostTimeout": cpqSmCntlrPostTimeout,
       "cpqSmCntlrCondition": cpqSmCntlrCondition,
       "cpqSmObjData": cpqSmObjData,
       "cpqSmObjDataTotalObjects": cpqSmObjDataTotalObjects,
       "cpqSmObjDataObjectTotalSpace": cpqSmObjDataObjectTotalSpace,
       "cpqSmObjDataObjectSpaceAvailable": cpqSmObjDataObjectSpaceAvailable,
       "cpqSmObjDataInnateMonitoringStatus": cpqSmObjDataInnateMonitoringStatus,
       "cpqSmObjectTable": cpqSmObjectTable,
       "cpqSmObjectEntry": cpqSmObjectEntry,
       "cpqSmObjectIndex": cpqSmObjectIndex,
       "cpqSmObjectInstIndex": cpqSmObjectInstIndex,
       "cpqSmObjectClass": cpqSmObjectClass,
       "cpqSmObjectLabel": cpqSmObjectLabel,
       "cpqSmMonItemTable": cpqSmMonItemTable,
       "cpqSmMonItemEntry": cpqSmMonItemEntry,
       "cpqSmMonItemObjIndex": cpqSmMonItemObjIndex,
       "cpqSmMonItemInstIndex": cpqSmMonItemInstIndex,
       "cpqSmMonItemIndex": cpqSmMonItemIndex,
       "cpqSmMonItemOnNetAlertStatus": cpqSmMonItemOnNetAlertStatus,
       "cpqSmMonItemRemoteAlertStatus": cpqSmMonItemRemoteAlertStatus,
       "cpqSmMonItemInnateStatus": cpqSmMonItemInnateStatus,
       "cpqSmMonItemHostNotify": cpqSmMonItemHostNotify,
       "cpqSmMonItemLogicalOperator": cpqSmMonItemLogicalOperator,
       "cpqSmMonItemSeverity": cpqSmMonItemSeverity,
       "cpqSmMonItemDataType": cpqSmMonItemDataType,
       "cpqSmMonItemVoiceMsgNum": cpqSmMonItemVoiceMsgNum,
       "cpqSmMonItemLabel": cpqSmMonItemLabel,
       "cpqSmMonItemLimit": cpqSmMonItemLimit,
       "cpqSmMonItemOptional": cpqSmMonItemOptional,
       "cpqSmMonItemDefVal": cpqSmMonItemDefVal,
       "cpqSmMonItemCurVal": cpqSmMonItemCurVal,
       "cpqSmMonItemCurString": cpqSmMonItemCurString,
       "cpqSmMonItemCurContents": cpqSmMonItemCurContents,
       "cpqSmMonItemTimeStamp": cpqSmMonItemTimeStamp,
       "cpqSmAsyncComm": cpqSmAsyncComm,
       "cpqSmCommAsyncCommunicationStatus": cpqSmCommAsyncCommunicationStatus,
       "cpqSmCommInternalModemMaxBaudRate": cpqSmCommInternalModemMaxBaudRate,
       "cpqSmCommAudibleIndicatorStatus": cpqSmCommAudibleIndicatorStatus,
       "cpqSmCommRemoteSessionStatus": cpqSmCommRemoteSessionStatus,
       "cpqSmCommCallbackStatus": cpqSmCommCallbackStatus,
       "cpqSmModemSettingsTable": cpqSmModemSettingsTable,
       "cpqSmModemSettingsEntry": cpqSmModemSettingsEntry,
       "cpqSmModemSettingsIndex": cpqSmModemSettingsIndex,
       "cpqSmModemSettingsStatus": cpqSmModemSettingsStatus,
       "cpqSmModemSettingsBaudRate": cpqSmModemSettingsBaudRate,
       "cpqSmModemSettingsParity": cpqSmModemSettingsParity,
       "cpqSmModemSettingsDataLength": cpqSmModemSettingsDataLength,
       "cpqSmModemSettingsStopBits": cpqSmModemSettingsStopBits,
       "cpqSmModemSettingsDialString": cpqSmModemSettingsDialString,
       "cpqSmModemSettingsHangUpString": cpqSmModemSettingsHangUpString,
       "cpqSmModemSettingsAnswerString": cpqSmModemSettingsAnswerString,
       "cpqSmModemSettingsOriginateString": cpqSmModemSettingsOriginateString,
       "cpqSmAlert": cpqSmAlert,
       "cpqSmAlertStatus": cpqSmAlertStatus,
       "cpqSmAlertDestTable": cpqSmAlertDestTable,
       "cpqSmAlertDestEntry": cpqSmAlertDestEntry,
       "cpqSmAlertDestPriorityIndex": cpqSmAlertDestPriorityIndex,
       "cpqSmAlertDestType": cpqSmAlertDestType,
       "cpqSmAlertDestRetries": cpqSmAlertDestRetries,
       "cpqSmAlertDestConnectFlags": cpqSmAlertDestConnectFlags,
       "cpqSmAlertDestPhoneNumber": cpqSmAlertDestPhoneNumber,
       "cpqSmAlertDestTimeMask": cpqSmAlertDestTimeMask,
       "cpqSmAlertDestPagerType": cpqSmAlertDestPagerType,
       "cpqSmAlertDestPagerId": cpqSmAlertDestPagerId,
       "cpqSmAlertDestPagerDisplayLength": cpqSmAlertDestPagerDisplayLength,
       "cpqSmTrap": cpqSmTrap,
       "cpqSmTrapPkts": cpqSmTrapPkts,
       "cpqSmTrapLogMaxSize": cpqSmTrapLogMaxSize,
       "cpqSmTrapLogTable": cpqSmTrapLogTable,
       "cpqSmTrapLogEntry": cpqSmTrapLogEntry,
       "cpqSmTrapLogIndex": cpqSmTrapLogIndex,
       "cpqSmTrapType": cpqSmTrapType,
       "cpqSmTrapTime": cpqSmTrapTime}
)
