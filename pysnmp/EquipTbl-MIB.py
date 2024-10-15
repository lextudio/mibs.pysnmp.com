# SNMP MIB module (EquipTbl-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EquipTbl-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:12 2024
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

(chrComHwNe,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComHwNe")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ChrComHwNeId_Type(Integer32):
    """Custom type chrComHwNeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChrComHwNeId_Type.__name__ = "Integer32"
_ChrComHwNeId_Object = MibScalar
chrComHwNeId = _ChrComHwNeId_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 1),
    _ChrComHwNeId_Type()
)
chrComHwNeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeId.setStatus("current")


class _ChrComHwNeType_Type(Integer32):
    """Custom type chrComHwNeType based on Integer32"""
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
        *(("metropolis2000", 1),
          ("metropolis2500", 2),
          ("metropolis4000", 3),
          ("metropolis4500", 4))
    )


_ChrComHwNeType_Type.__name__ = "Integer32"
_ChrComHwNeType_Object = MibScalar
chrComHwNeType = _ChrComHwNeType_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 2),
    _ChrComHwNeType_Type()
)
chrComHwNeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeType.setStatus("current")


class _ChrComHwNeRunningSwVersion_Type(DisplayString):
    """Custom type chrComHwNeRunningSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ChrComHwNeRunningSwVersion_Type.__name__ = "DisplayString"
_ChrComHwNeRunningSwVersion_Object = MibScalar
chrComHwNeRunningSwVersion = _ChrComHwNeRunningSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 3),
    _ChrComHwNeRunningSwVersion_Type()
)
chrComHwNeRunningSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeRunningSwVersion.setStatus("current")


class _ChrComHwNeAvailableSwVersion_Type(DisplayString):
    """Custom type chrComHwNeAvailableSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_ChrComHwNeAvailableSwVersion_Type.__name__ = "DisplayString"
_ChrComHwNeAvailableSwVersion_Object = MibScalar
chrComHwNeAvailableSwVersion = _ChrComHwNeAvailableSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 4),
    _ChrComHwNeAvailableSwVersion_Type()
)
chrComHwNeAvailableSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeAvailableSwVersion.setStatus("current")


class _ChrComHwNeNextSessionSwVersion_Type(DisplayString):
    """Custom type chrComHwNeNextSessionSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ChrComHwNeNextSessionSwVersion_Type.__name__ = "DisplayString"
_ChrComHwNeNextSessionSwVersion_Object = MibScalar
chrComHwNeNextSessionSwVersion = _ChrComHwNeNextSessionSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 5),
    _ChrComHwNeNextSessionSwVersion_Type()
)
chrComHwNeNextSessionSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeNextSessionSwVersion.setStatus("current")


class _ChrComHwNeRunningConfigurationSet_Type(DisplayString):
    """Custom type chrComHwNeRunningConfigurationSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ChrComHwNeRunningConfigurationSet_Type.__name__ = "DisplayString"
_ChrComHwNeRunningConfigurationSet_Object = MibScalar
chrComHwNeRunningConfigurationSet = _ChrComHwNeRunningConfigurationSet_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 6),
    _ChrComHwNeRunningConfigurationSet_Type()
)
chrComHwNeRunningConfigurationSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeRunningConfigurationSet.setStatus("current")


class _ChrComHwNeAvailableConfigurationSets_Type(DisplayString):
    """Custom type chrComHwNeAvailableConfigurationSets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_ChrComHwNeAvailableConfigurationSets_Type.__name__ = "DisplayString"
_ChrComHwNeAvailableConfigurationSets_Object = MibScalar
chrComHwNeAvailableConfigurationSets = _ChrComHwNeAvailableConfigurationSets_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 7),
    _ChrComHwNeAvailableConfigurationSets_Type()
)
chrComHwNeAvailableConfigurationSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeAvailableConfigurationSets.setStatus("current")


class _ChrComHwNeNextSessionConfigurationSet_Type(DisplayString):
    """Custom type chrComHwNeNextSessionConfigurationSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ChrComHwNeNextSessionConfigurationSet_Type.__name__ = "DisplayString"
_ChrComHwNeNextSessionConfigurationSet_Object = MibScalar
chrComHwNeNextSessionConfigurationSet = _ChrComHwNeNextSessionConfigurationSet_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 8),
    _ChrComHwNeNextSessionConfigurationSet_Type()
)
chrComHwNeNextSessionConfigurationSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeNextSessionConfigurationSet.setStatus("current")
_ChrComHwNeTimeofDay_Type = DateAndTime
_ChrComHwNeTimeofDay_Object = MibScalar
chrComHwNeTimeofDay = _ChrComHwNeTimeofDay_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 9),
    _ChrComHwNeTimeofDay_Type()
)
chrComHwNeTimeofDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeTimeofDay.setStatus("current")


class _ChrComHwNeDailyPMStartOfTime_Type(Integer32):
    """Custom type chrComHwNeDailyPMStartOfTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ChrComHwNeDailyPMStartOfTime_Type.__name__ = "Integer32"
_ChrComHwNeDailyPMStartOfTime_Object = MibScalar
chrComHwNeDailyPMStartOfTime = _ChrComHwNeDailyPMStartOfTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 10),
    _ChrComHwNeDailyPMStartOfTime_Type()
)
chrComHwNeDailyPMStartOfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeDailyPMStartOfTime.setStatus("current")
_ChrComHwNeCriticalAlarmCounter_Type = Counter32
_ChrComHwNeCriticalAlarmCounter_Object = MibScalar
chrComHwNeCriticalAlarmCounter = _ChrComHwNeCriticalAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 11),
    _ChrComHwNeCriticalAlarmCounter_Type()
)
chrComHwNeCriticalAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeCriticalAlarmCounter.setStatus("current")
_ChrComHwNeMajorAlarmCounter_Type = Counter32
_ChrComHwNeMajorAlarmCounter_Object = MibScalar
chrComHwNeMajorAlarmCounter = _ChrComHwNeMajorAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 12),
    _ChrComHwNeMajorAlarmCounter_Type()
)
chrComHwNeMajorAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeMajorAlarmCounter.setStatus("current")
_ChrComHwNeMinorAlarmCounter_Type = Counter32
_ChrComHwNeMinorAlarmCounter_Object = MibScalar
chrComHwNeMinorAlarmCounter = _ChrComHwNeMinorAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 13),
    _ChrComHwNeMinorAlarmCounter_Type()
)
chrComHwNeMinorAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeMinorAlarmCounter.setStatus("current")


class _ChrComHwNeDetectionFaultStabilizationTime_Type(Integer32):
    """Custom type chrComHwNeDetectionFaultStabilizationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ChrComHwNeDetectionFaultStabilizationTime_Type.__name__ = "Integer32"
_ChrComHwNeDetectionFaultStabilizationTime_Object = MibScalar
chrComHwNeDetectionFaultStabilizationTime = _ChrComHwNeDetectionFaultStabilizationTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 14),
    _ChrComHwNeDetectionFaultStabilizationTime_Type()
)
chrComHwNeDetectionFaultStabilizationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeDetectionFaultStabilizationTime.setStatus("current")


class _ChrComHwNeRemovalFaultStabilizationTime_Type(Integer32):
    """Custom type chrComHwNeRemovalFaultStabilizationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_ChrComHwNeRemovalFaultStabilizationTime_Type.__name__ = "Integer32"
_ChrComHwNeRemovalFaultStabilizationTime_Object = MibScalar
chrComHwNeRemovalFaultStabilizationTime = _ChrComHwNeRemovalFaultStabilizationTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 15),
    _ChrComHwNeRemovalFaultStabilizationTime_Type()
)
chrComHwNeRemovalFaultStabilizationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeRemovalFaultStabilizationTime.setStatus("current")
_ChrComHwNeAlarmCutOffStatus_Type = TruthValue
_ChrComHwNeAlarmCutOffStatus_Object = MibScalar
chrComHwNeAlarmCutOffStatus = _ChrComHwNeAlarmCutOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 16),
    _ChrComHwNeAlarmCutOffStatus_Type()
)
chrComHwNeAlarmCutOffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeAlarmCutOffStatus.setStatus("current")
_ChrComHwNeAtmfM4NeSuppressZeroStats_Type = TruthValue
_ChrComHwNeAtmfM4NeSuppressZeroStats_Object = MibScalar
chrComHwNeAtmfM4NeSuppressZeroStats = _ChrComHwNeAtmfM4NeSuppressZeroStats_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 17),
    _ChrComHwNeAtmfM4NeSuppressZeroStats_Type()
)
chrComHwNeAtmfM4NeSuppressZeroStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeAtmfM4NeSuppressZeroStats.setStatus("current")
_ChrComHwNeResetPMCountersAction_Type = TruthValue
_ChrComHwNeResetPMCountersAction_Object = MibScalar
chrComHwNeResetPMCountersAction = _ChrComHwNeResetPMCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 18),
    _ChrComHwNeResetPMCountersAction_Type()
)
chrComHwNeResetPMCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeResetPMCountersAction.setStatus("current")
_ChrComHwNeACOActivationAction_Type = TruthValue
_ChrComHwNeACOActivationAction_Object = MibScalar
chrComHwNeACOActivationAction = _ChrComHwNeACOActivationAction_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 19),
    _ChrComHwNeACOActivationAction_Type()
)
chrComHwNeACOActivationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeACOActivationAction.setStatus("current")


class _ChrComHwNeAtmCbrRatesList_Type(OctetString):
    """Custom type chrComHwNeAtmCbrRatesList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChrComHwNeAtmCbrRatesList_Type.__name__ = "OctetString"
_ChrComHwNeAtmCbrRatesList_Object = MibScalar
chrComHwNeAtmCbrRatesList = _ChrComHwNeAtmCbrRatesList_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 20),
    _ChrComHwNeAtmCbrRatesList_Type()
)
chrComHwNeAtmCbrRatesList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeAtmCbrRatesList.setStatus("current")


class _ChrComHwNeAtmRtVbrRatesList_Type(OctetString):
    """Custom type chrComHwNeAtmRtVbrRatesList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ChrComHwNeAtmRtVbrRatesList_Type.__name__ = "OctetString"
_ChrComHwNeAtmRtVbrRatesList_Object = MibScalar
chrComHwNeAtmRtVbrRatesList = _ChrComHwNeAtmRtVbrRatesList_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 21),
    _ChrComHwNeAtmRtVbrRatesList_Type()
)
chrComHwNeAtmRtVbrRatesList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeAtmRtVbrRatesList.setStatus("current")


class _ChrComHwNeMaxPathPM_Type(Integer32):
    """Custom type chrComHwNeMaxPathPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChrComHwNeMaxPathPM_Type.__name__ = "Integer32"
_ChrComHwNeMaxPathPM_Object = MibScalar
chrComHwNeMaxPathPM = _ChrComHwNeMaxPathPM_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 22),
    _ChrComHwNeMaxPathPM_Type()
)
chrComHwNeMaxPathPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeMaxPathPM.setStatus("current")


class _ChrComHwNeCurrentPathPM_Type(Integer32):
    """Custom type chrComHwNeCurrentPathPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChrComHwNeCurrentPathPM_Type.__name__ = "Integer32"
_ChrComHwNeCurrentPathPM_Object = MibScalar
chrComHwNeCurrentPathPM = _ChrComHwNeCurrentPathPM_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 23),
    _ChrComHwNeCurrentPathPM_Type()
)
chrComHwNeCurrentPathPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComHwNeCurrentPathPM.setStatus("current")


class _ChrComHwNeGlobalSubnetID_Type(OctetString):
    """Custom type chrComHwNeGlobalSubnetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ChrComHwNeGlobalSubnetID_Type.__name__ = "OctetString"
_ChrComHwNeGlobalSubnetID_Object = MibScalar
chrComHwNeGlobalSubnetID = _ChrComHwNeGlobalSubnetID_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 1, 1, 24),
    _ChrComHwNeGlobalSubnetID_Type()
)
chrComHwNeGlobalSubnetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComHwNeGlobalSubnetID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EquipTbl-MIB",
    **{"chrComHwNeId": chrComHwNeId,
       "chrComHwNeType": chrComHwNeType,
       "chrComHwNeRunningSwVersion": chrComHwNeRunningSwVersion,
       "chrComHwNeAvailableSwVersion": chrComHwNeAvailableSwVersion,
       "chrComHwNeNextSessionSwVersion": chrComHwNeNextSessionSwVersion,
       "chrComHwNeRunningConfigurationSet": chrComHwNeRunningConfigurationSet,
       "chrComHwNeAvailableConfigurationSets": chrComHwNeAvailableConfigurationSets,
       "chrComHwNeNextSessionConfigurationSet": chrComHwNeNextSessionConfigurationSet,
       "chrComHwNeTimeofDay": chrComHwNeTimeofDay,
       "chrComHwNeDailyPMStartOfTime": chrComHwNeDailyPMStartOfTime,
       "chrComHwNeCriticalAlarmCounter": chrComHwNeCriticalAlarmCounter,
       "chrComHwNeMajorAlarmCounter": chrComHwNeMajorAlarmCounter,
       "chrComHwNeMinorAlarmCounter": chrComHwNeMinorAlarmCounter,
       "chrComHwNeDetectionFaultStabilizationTime": chrComHwNeDetectionFaultStabilizationTime,
       "chrComHwNeRemovalFaultStabilizationTime": chrComHwNeRemovalFaultStabilizationTime,
       "chrComHwNeAlarmCutOffStatus": chrComHwNeAlarmCutOffStatus,
       "chrComHwNeAtmfM4NeSuppressZeroStats": chrComHwNeAtmfM4NeSuppressZeroStats,
       "chrComHwNeResetPMCountersAction": chrComHwNeResetPMCountersAction,
       "chrComHwNeACOActivationAction": chrComHwNeACOActivationAction,
       "chrComHwNeAtmCbrRatesList": chrComHwNeAtmCbrRatesList,
       "chrComHwNeAtmRtVbrRatesList": chrComHwNeAtmRtVbrRatesList,
       "chrComHwNeMaxPathPM": chrComHwNeMaxPathPM,
       "chrComHwNeCurrentPathPM": chrComHwNeCurrentPathPM,
       "chrComHwNeGlobalSubnetID": chrComHwNeGlobalSubnetID}
)
