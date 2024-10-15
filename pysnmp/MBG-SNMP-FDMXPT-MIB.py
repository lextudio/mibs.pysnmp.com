# SNMP MIB module (MBG-SNMP-FDMXPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MBG-SNMP-FDMXPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:34 2024
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

(mbgSnmpRoot,) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "mbgSnmpRoot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

mbgFDM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 15)
)
mbgFDM.setRevisions(
        ("2012-01-25 00:00",
         "2006-01-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MbgFDMData_ObjectIdentity = ObjectIdentity
mbgFDMData = _MbgFDMData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2)
)
_MbgFDMMode_Type = DisplayString
_MbgFDMMode_Object = MibScalar
mbgFDMMode = _MbgFDMMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 1),
    _MbgFDMMode_Type()
)
mbgFDMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMMode.setStatus("current")


class _MbgFDMModeVal_Type(Integer32):
    """Custom type mbgFDMModeVal based on Integer32"""
    defaultValue = 0


_MbgFDMModeVal_Object = MibScalar
mbgFDMModeVal = _MbgFDMModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 2),
    _MbgFDMModeVal_Type()
)
mbgFDMModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMModeVal.setStatus("current")
_MbgFDMFrequency_Type = DisplayString
_MbgFDMFrequency_Object = MibScalar
mbgFDMFrequency = _MbgFDMFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 3),
    _MbgFDMFrequency_Type()
)
mbgFDMFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMFrequency.setStatus("current")


class _MbgFDMFrequencyVal_Type(Integer32):
    """Custom type mbgFDMFrequencyVal based on Integer32"""
    defaultValue = 0


_MbgFDMFrequencyVal_Object = MibScalar
mbgFDMFrequencyVal = _MbgFDMFrequencyVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 4),
    _MbgFDMFrequencyVal_Type()
)
mbgFDMFrequencyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMFrequencyVal.setStatus("current")
_MbgFDMRefTime_Type = DisplayString
_MbgFDMRefTime_Object = MibScalar
mbgFDMRefTime = _MbgFDMRefTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 5),
    _MbgFDMRefTime_Type()
)
mbgFDMRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMRefTime.setStatus("current")
_MbgFDMPLTime_Type = DisplayString
_MbgFDMPLTime_Object = MibScalar
mbgFDMPLTime = _MbgFDMPLTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 6),
    _MbgFDMPLTime_Type()
)
mbgFDMPLTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMPLTime.setStatus("current")
_MbgFDMFreqDev_Type = DisplayString
_MbgFDMFreqDev_Object = MibScalar
mbgFDMFreqDev = _MbgFDMFreqDev_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 7),
    _MbgFDMFreqDev_Type()
)
mbgFDMFreqDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMFreqDev.setStatus("current")


class _MbgFDMFreqDevVal_Type(Integer32):
    """Custom type mbgFDMFreqDevVal based on Integer32"""
    defaultValue = 0


_MbgFDMFreqDevVal_Object = MibScalar
mbgFDMFreqDevVal = _MbgFDMFreqDevVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 8),
    _MbgFDMFreqDevVal_Type()
)
mbgFDMFreqDevVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMFreqDevVal.setStatus("current")
_MbgFDMTimeDev_Type = DisplayString
_MbgFDMTimeDev_Object = MibScalar
mbgFDMTimeDev = _MbgFDMTimeDev_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 9),
    _MbgFDMTimeDev_Type()
)
mbgFDMTimeDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMTimeDev.setStatus("current")


class _MbgFDMTimeDevVal_Type(Integer32):
    """Custom type mbgFDMTimeDevVal based on Integer32"""
    defaultValue = 0


_MbgFDMTimeDevVal_Object = MibScalar
mbgFDMTimeDevVal = _MbgFDMTimeDevVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 10),
    _MbgFDMTimeDevVal_Type()
)
mbgFDMTimeDevVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMTimeDevVal.setStatus("current")
_MbgFDMErrorStatus_Type = DisplayString
_MbgFDMErrorStatus_Object = MibScalar
mbgFDMErrorStatus = _MbgFDMErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5597, 15, 2, 11),
    _MbgFDMErrorStatus_Type()
)
mbgFDMErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgFDMErrorStatus.setStatus("current")
_MbgFDMTraps_ObjectIdentity = ObjectIdentity
mbgFDMTraps = _MbgFDMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3)
)
_MbgFDMConformance_ObjectIdentity = ObjectIdentity
mbgFDMConformance = _MbgFDMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 15, 90)
)
_MbgFDMCompliances_ObjectIdentity = ObjectIdentity
mbgFDMCompliances = _MbgFDMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 15, 90, 1)
)
_MbgFDMGroups_ObjectIdentity = ObjectIdentity
mbgFDMGroups = _MbgFDMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 15, 90, 2)
)

# Managed Objects groups

mbgFDMObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5597, 15, 90, 2, 1)
)
mbgFDMObjectsGroup.setObjects(
      *(("MBG-SNMP-FDMXPT-MIB", "mbgFDMMode"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMModeVal"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFrequency"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFrequencyVal"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMRefTime"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMPLTime"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFreqDev"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFreqDevVal"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTimeDev"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTimeDevVal"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMErrorStatus"))
)
if mibBuilder.loadTexts:
    mbgFDMObjectsGroup.setStatus("current")


# Notification objects

mbgFDMTrapInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 1)
)
if mibBuilder.loadTexts:
    mbgFDMTrapInternalError.setStatus(
        "current"
    )

mbgFDMTrapNoTimeString = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 2)
)
if mibBuilder.loadTexts:
    mbgFDMTrapNoTimeString.setStatus(
        "current"
    )

mbgFDMTrapNo10Mhz = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 3)
)
if mibBuilder.loadTexts:
    mbgFDMTrapNo10Mhz.setStatus(
        "current"
    )

mbgFDMTrapNoPPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 4)
)
if mibBuilder.loadTexts:
    mbgFDMTrapNoPPS.setStatus(
        "current"
    )

mbgFDMTrapNoPowerline = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 5)
)
if mibBuilder.loadTexts:
    mbgFDMTrapNoPowerline.setStatus(
        "current"
    )

mbgFDMTrapTimeDeviationOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 6)
)
if mibBuilder.loadTexts:
    mbgFDMTrapTimeDeviationOverflow.setStatus(
        "current"
    )

mbgFDMTrapA1Overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 7)
)
if mibBuilder.loadTexts:
    mbgFDMTrapA1Overflow.setStatus(
        "current"
    )

mbgFDMTrapA2Overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 8)
)
if mibBuilder.loadTexts:
    mbgFDMTrapA2Overflow.setStatus(
        "current"
    )

mbgFDMTrapFreqLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 9)
)
if mibBuilder.loadTexts:
    mbgFDMTrapFreqLimitExceeded.setStatus(
        "current"
    )

mbgFDMXPTReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 10)
)
if mibBuilder.loadTexts:
    mbgFDMXPTReboot.setStatus(
        "current"
    )

mbgFDMNormalOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 15, 3, 99)
)
if mibBuilder.loadTexts:
    mbgFDMNormalOperation.setStatus(
        "current"
    )


# Notifications groups

mbgFDMTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5597, 15, 90, 2, 2)
)
mbgFDMTrapsGroup.setObjects(
      *(("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapInternalError"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoTimeString"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNo10Mhz"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoPPS"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoPowerline"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapTimeDeviationOverflow"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapA1Overflow"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapA2Overflow"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapFreqLimitExceeded"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMXPTReboot"),
        ("MBG-SNMP-FDMXPT-MIB", "mbgFDMNormalOperation"))
)
if mibBuilder.loadTexts:
    mbgFDMTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbgFDMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5597, 15, 90, 1, 1)
)
if mibBuilder.loadTexts:
    mbgFDMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-SNMP-FDMXPT-MIB",
    **{"mbgFDM": mbgFDM,
       "mbgFDMData": mbgFDMData,
       "mbgFDMMode": mbgFDMMode,
       "mbgFDMModeVal": mbgFDMModeVal,
       "mbgFDMFrequency": mbgFDMFrequency,
       "mbgFDMFrequencyVal": mbgFDMFrequencyVal,
       "mbgFDMRefTime": mbgFDMRefTime,
       "mbgFDMPLTime": mbgFDMPLTime,
       "mbgFDMFreqDev": mbgFDMFreqDev,
       "mbgFDMFreqDevVal": mbgFDMFreqDevVal,
       "mbgFDMTimeDev": mbgFDMTimeDev,
       "mbgFDMTimeDevVal": mbgFDMTimeDevVal,
       "mbgFDMErrorStatus": mbgFDMErrorStatus,
       "mbgFDMTraps": mbgFDMTraps,
       "mbgFDMTrapInternalError": mbgFDMTrapInternalError,
       "mbgFDMTrapNoTimeString": mbgFDMTrapNoTimeString,
       "mbgFDMTrapNo10Mhz": mbgFDMTrapNo10Mhz,
       "mbgFDMTrapNoPPS": mbgFDMTrapNoPPS,
       "mbgFDMTrapNoPowerline": mbgFDMTrapNoPowerline,
       "mbgFDMTrapTimeDeviationOverflow": mbgFDMTrapTimeDeviationOverflow,
       "mbgFDMTrapA1Overflow": mbgFDMTrapA1Overflow,
       "mbgFDMTrapA2Overflow": mbgFDMTrapA2Overflow,
       "mbgFDMTrapFreqLimitExceeded": mbgFDMTrapFreqLimitExceeded,
       "mbgFDMXPTReboot": mbgFDMXPTReboot,
       "mbgFDMNormalOperation": mbgFDMNormalOperation,
       "mbgFDMConformance": mbgFDMConformance,
       "mbgFDMCompliances": mbgFDMCompliances,
       "mbgFDMCompliance": mbgFDMCompliance,
       "mbgFDMGroups": mbgFDMGroups,
       "mbgFDMObjectsGroup": mbgFDMObjectsGroup,
       "mbgFDMTrapsGroup": mbgFDMTrapsGroup}
)
