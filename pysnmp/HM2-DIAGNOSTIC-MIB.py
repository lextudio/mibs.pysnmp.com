# SNMP MIB module (HM2-DIAGNOSTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-DIAGNOSTIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:53 2024
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

(hm2IfacePhysIndex,) = mibBuilder.importSymbols(
    "HM2-DEVMGMT-MIB",
    "hm2IfacePhysIndex")

(hm2PSID,) = mibBuilder.importSymbols(
    "HM2-PWRMGMT-MIB",
    "hm2PSID")

(HmEnabledStatus,
 HmTimeSeconds1970,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "HmTimeSeconds1970",
    "hm2ConfigurationMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2DiagnosticMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22)
)
hm2DiagnosticMib.setRevisions(
        ("2012-08-28 00:00",
         "2011-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2LedType(Integer32, TextualConvention):
    status = "current"
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
        *(("envm", 4),
          ("i1", 5),
          ("i2", 6),
          ("power", 1),
          ("rm", 3),
          ("status", 2))
    )



class Hm2LedStatus(Integer32, TextualConvention):
    status = "current"
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
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("greenBlink1", 3),
          ("greenBlink3", 4),
          ("greenBlink4", 5),
          ("greenBlink5", 6),
          ("greenBlink5i", 7),
          ("greenSolid", 2),
          ("off", 1),
          ("redBlink1", 14),
          ("redBlink3", 15),
          ("redBlink4", 16),
          ("redBlink5", 17),
          ("redSolid", 13),
          ("yellowBlink1", 9),
          ("yellowBlink3", 10),
          ("yellowBlink4", 11),
          ("yellowBlink5", 12),
          ("yellowSolid", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2DiagnosticMibNotifications_ObjectIdentity = ObjectIdentity
hm2DiagnosticMibNotifications = _Hm2DiagnosticMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 0)
)
_Hm2DiagnosticMibObjects_ObjectIdentity = ObjectIdentity
hm2DiagnosticMibObjects = _Hm2DiagnosticMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1)
)
_Hm2DiagSelftestGroup_ObjectIdentity = ObjectIdentity
hm2DiagSelftestGroup = _Hm2DiagSelftestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 1)
)


class _Hm2DiagSelftestRAM_Type(HmEnabledStatus):
    """Custom type hm2DiagSelftestRAM based on HmEnabledStatus"""


_Hm2DiagSelftestRAM_Object = MibScalar
hm2DiagSelftestRAM = _Hm2DiagSelftestRAM_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 1, 1),
    _Hm2DiagSelftestRAM_Type()
)
hm2DiagSelftestRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagSelftestRAM.setStatus("current")
_Hm2DiagSelftestBootTime_Type = Integer32
_Hm2DiagSelftestBootTime_Object = MibScalar
hm2DiagSelftestBootTime = _Hm2DiagSelftestBootTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 1, 2),
    _Hm2DiagSelftestBootTime_Type()
)
hm2DiagSelftestBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagSelftestBootTime.setStatus("current")
_Hm2DiagSelftestActionTable_Object = MibTable
hm2DiagSelftestActionTable = _Hm2DiagSelftestActionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hm2DiagSelftestActionTable.setStatus("current")
_Hm2DiagSelftestActionEntry_Object = MibTableRow
hm2DiagSelftestActionEntry = _Hm2DiagSelftestActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 1, 10, 1)
)
hm2DiagSelftestActionEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DiagSelftestActionCause"),
)
if mibBuilder.loadTexts:
    hm2DiagSelftestActionEntry.setStatus("current")


class _Hm2DiagSelftestActionCause_Type(Integer32):
    """Custom type hm2DiagSelftestActionCause based on Integer32"""
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
        *(("hardware", 4),
          ("resource", 2),
          ("software", 3),
          ("task", 1))
    )


_Hm2DiagSelftestActionCause_Type.__name__ = "Integer32"
_Hm2DiagSelftestActionCause_Object = MibTableColumn
hm2DiagSelftestActionCause = _Hm2DiagSelftestActionCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 1, 10, 1, 1),
    _Hm2DiagSelftestActionCause_Type()
)
hm2DiagSelftestActionCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagSelftestActionCause.setStatus("current")


class _Hm2DiagSelftestAction_Type(Integer32):
    """Custom type hm2DiagSelftestAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("logOnly", 1),
          ("reboot", 3),
          ("sendTrap", 2))
    )


_Hm2DiagSelftestAction_Type.__name__ = "Integer32"
_Hm2DiagSelftestAction_Object = MibTableColumn
hm2DiagSelftestAction = _Hm2DiagSelftestAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 1, 10, 1, 2),
    _Hm2DiagSelftestAction_Type()
)
hm2DiagSelftestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagSelftestAction.setStatus("current")
_Hm2DiagBootGroup_ObjectIdentity = ObjectIdentity
hm2DiagBootGroup = _Hm2DiagBootGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 2)
)


class _Hm2BootSystemMonitor_Type(HmEnabledStatus):
    """Custom type hm2BootSystemMonitor based on HmEnabledStatus"""


_Hm2BootSystemMonitor_Object = MibScalar
hm2BootSystemMonitor = _Hm2BootSystemMonitor_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 2, 1),
    _Hm2BootSystemMonitor_Type()
)
hm2BootSystemMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2BootSystemMonitor.setStatus("current")


class _Hm2BootDefaultConfigOnError_Type(HmEnabledStatus):
    """Custom type hm2BootDefaultConfigOnError based on HmEnabledStatus"""


_Hm2BootDefaultConfigOnError_Object = MibScalar
hm2BootDefaultConfigOnError = _Hm2BootDefaultConfigOnError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 2, 2),
    _Hm2BootDefaultConfigOnError_Type()
)
hm2BootDefaultConfigOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2BootDefaultConfigOnError.setStatus("current")


class _Hm2BootConfigPushButton_Type(HmEnabledStatus):
    """Custom type hm2BootConfigPushButton based on HmEnabledStatus"""


_Hm2BootConfigPushButton_Object = MibScalar
hm2BootConfigPushButton = _Hm2BootConfigPushButton_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 2, 3),
    _Hm2BootConfigPushButton_Type()
)
hm2BootConfigPushButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2BootConfigPushButton.setStatus("current")
_Hm2DiagDeviceMonitorGroup_ObjectIdentity = ObjectIdentity
hm2DiagDeviceMonitorGroup = _Hm2DiagDeviceMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3)
)
_Hm2SignalContactGroup_ObjectIdentity = ObjectIdentity
hm2SignalContactGroup = _Hm2SignalContactGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1)
)
_Hm2SigConCommonTable_Object = MibTable
hm2SigConCommonTable = _Hm2SigConCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hm2SigConCommonTable.setStatus("current")
_Hm2SigConCommonEntry_Object = MibTableRow
hm2SigConCommonEntry = _Hm2SigConCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1)
)
hm2SigConCommonEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2SigConID"),
)
if mibBuilder.loadTexts:
    hm2SigConCommonEntry.setStatus("current")


class _Hm2SigConID_Type(Integer32):
    """Custom type hm2SigConID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hm2SigConID_Type.__name__ = "Integer32"
_Hm2SigConID_Object = MibTableColumn
hm2SigConID = _Hm2SigConID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 1),
    _Hm2SigConID_Type()
)
hm2SigConID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConID.setStatus("current")


class _Hm2SigConTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2SigConTrapEnable based on HmEnabledStatus"""


_Hm2SigConTrapEnable_Object = MibTableColumn
hm2SigConTrapEnable = _Hm2SigConTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 2),
    _Hm2SigConTrapEnable_Type()
)
hm2SigConTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConTrapEnable.setStatus("current")


class _Hm2SigConTrapCause_Type(Integer32):
    """Custom type hm2SigConTrapCause based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-ip-enabled", 25),
          ("ext-nvm-config-load-unsecure", 21),
          ("ext-nvm-not-in-sync", 8),
          ("ext-nvm-removal", 7),
          ("ext-nvm-update-enabled", 18),
          ("fan-failure", 5),
          ("hidisc-write-enabled", 20),
          ("http-enabled", 15),
          ("https-certificate-warning", 23),
          ("link-failure", 3),
          ("modbus-tcp-enabled", 24),
          ("module-removal", 6),
          ("no-link", 19),
          ("none", 1),
          ("password-change", 10),
          ("password-min-length", 11),
          ("password-policy-inactive", 13),
          ("password-policy-not-configured", 12),
          ("power-supply", 2),
          ("profinet-io-enabled", 26),
          ("ring-redundancy", 9),
          ("snmp-unsecure", 16),
          ("sysmon-enabled", 17),
          ("telnet-enabled", 14),
          ("temperature", 4))
    )


_Hm2SigConTrapCause_Type.__name__ = "Integer32"
_Hm2SigConTrapCause_Object = MibTableColumn
hm2SigConTrapCause = _Hm2SigConTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 3),
    _Hm2SigConTrapCause_Type()
)
hm2SigConTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConTrapCause.setStatus("current")
_Hm2SigConTrapCauseIndex_Type = Integer32
_Hm2SigConTrapCauseIndex_Object = MibTableColumn
hm2SigConTrapCauseIndex = _Hm2SigConTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 4),
    _Hm2SigConTrapCauseIndex_Type()
)
hm2SigConTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConTrapCauseIndex.setStatus("current")


class _Hm2SigConMode_Type(Integer32):
    """Custom type hm2SigConMode based on Integer32"""
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
        *(("deviceSecurity", 4),
          ("deviceState", 3),
          ("deviceStateAndSecurity", 5),
          ("manual", 1),
          ("monitor", 2))
    )


_Hm2SigConMode_Type.__name__ = "Integer32"
_Hm2SigConMode_Object = MibTableColumn
hm2SigConMode = _Hm2SigConMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 5),
    _Hm2SigConMode_Type()
)
hm2SigConMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConMode.setStatus("current")


class _Hm2SigConOperState_Type(Integer32):
    """Custom type hm2SigConOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_Hm2SigConOperState_Type.__name__ = "Integer32"
_Hm2SigConOperState_Object = MibTableColumn
hm2SigConOperState = _Hm2SigConOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 6),
    _Hm2SigConOperState_Type()
)
hm2SigConOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConOperState.setStatus("current")
_Hm2SigConOperTimeStamp_Type = HmTimeSeconds1970
_Hm2SigConOperTimeStamp_Object = MibTableColumn
hm2SigConOperTimeStamp = _Hm2SigConOperTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 7),
    _Hm2SigConOperTimeStamp_Type()
)
hm2SigConOperTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConOperTimeStamp.setStatus("current")


class _Hm2SigConManualActivate_Type(Integer32):
    """Custom type hm2SigConManualActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_Hm2SigConManualActivate_Type.__name__ = "Integer32"
_Hm2SigConManualActivate_Object = MibTableColumn
hm2SigConManualActivate = _Hm2SigConManualActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 8),
    _Hm2SigConManualActivate_Type()
)
hm2SigConManualActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConManualActivate.setStatus("current")


class _Hm2SigConSenseLinkFailure_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseLinkFailure based on HmEnabledStatus"""


_Hm2SigConSenseLinkFailure_Object = MibTableColumn
hm2SigConSenseLinkFailure = _Hm2SigConSenseLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 9),
    _Hm2SigConSenseLinkFailure_Type()
)
hm2SigConSenseLinkFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseLinkFailure.setStatus("current")


class _Hm2SigConSenseTemperature_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseTemperature based on HmEnabledStatus"""


_Hm2SigConSenseTemperature_Object = MibTableColumn
hm2SigConSenseTemperature = _Hm2SigConSenseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 10),
    _Hm2SigConSenseTemperature_Type()
)
hm2SigConSenseTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseTemperature.setStatus("current")


class _Hm2SigConSenseFan_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseFan based on HmEnabledStatus"""


_Hm2SigConSenseFan_Object = MibTableColumn
hm2SigConSenseFan = _Hm2SigConSenseFan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 11),
    _Hm2SigConSenseFan_Type()
)
hm2SigConSenseFan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseFan.setStatus("current")


class _Hm2SigConSenseModuleRemoval_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseModuleRemoval based on HmEnabledStatus"""


_Hm2SigConSenseModuleRemoval_Object = MibTableColumn
hm2SigConSenseModuleRemoval = _Hm2SigConSenseModuleRemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 12),
    _Hm2SigConSenseModuleRemoval_Type()
)
hm2SigConSenseModuleRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseModuleRemoval.setStatus("current")


class _Hm2SigConSenseExtNvmRemoval_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseExtNvmRemoval based on HmEnabledStatus"""


_Hm2SigConSenseExtNvmRemoval_Object = MibTableColumn
hm2SigConSenseExtNvmRemoval = _Hm2SigConSenseExtNvmRemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 13),
    _Hm2SigConSenseExtNvmRemoval_Type()
)
hm2SigConSenseExtNvmRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseExtNvmRemoval.setStatus("current")


class _Hm2SigConSenseExtNvmNotInSync_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseExtNvmNotInSync based on HmEnabledStatus"""


_Hm2SigConSenseExtNvmNotInSync_Object = MibTableColumn
hm2SigConSenseExtNvmNotInSync = _Hm2SigConSenseExtNvmNotInSync_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 14),
    _Hm2SigConSenseExtNvmNotInSync_Type()
)
hm2SigConSenseExtNvmNotInSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseExtNvmNotInSync.setStatus("current")


class _Hm2SigConSenseRingRedundancy_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseRingRedundancy based on HmEnabledStatus"""


_Hm2SigConSenseRingRedundancy_Object = MibTableColumn
hm2SigConSenseRingRedundancy = _Hm2SigConSenseRingRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 1, 1, 15),
    _Hm2SigConSenseRingRedundancy_Type()
)
hm2SigConSenseRingRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseRingRedundancy.setStatus("current")
_Hm2SigConPSTable_Object = MibTable
hm2SigConPSTable = _Hm2SigConPSTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hm2SigConPSTable.setStatus("current")
_Hm2SigConPSEntry_Object = MibTableRow
hm2SigConPSEntry = _Hm2SigConPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 2, 1)
)
hm2SigConPSEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2SigConID"),
    (0, "HM2-PWRMGMT-MIB", "hm2PSID"),
)
if mibBuilder.loadTexts:
    hm2SigConPSEntry.setStatus("current")


class _Hm2SigConSensePSState_Type(HmEnabledStatus):
    """Custom type hm2SigConSensePSState based on HmEnabledStatus"""


_Hm2SigConSensePSState_Object = MibTableColumn
hm2SigConSensePSState = _Hm2SigConSensePSState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 2, 1, 1),
    _Hm2SigConSensePSState_Type()
)
hm2SigConSensePSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSensePSState.setStatus("current")
_Hm2SigConInterfaceTable_Object = MibTable
hm2SigConInterfaceTable = _Hm2SigConInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hm2SigConInterfaceTable.setStatus("current")
_Hm2SigConInterfaceEntry_Object = MibTableRow
hm2SigConInterfaceEntry = _Hm2SigConInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 3, 1)
)
hm2SigConInterfaceEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2SigConID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2SigConInterfaceEntry.setStatus("current")


class _Hm2SigConSenseIfLinkAlarm_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseIfLinkAlarm based on HmEnabledStatus"""


_Hm2SigConSenseIfLinkAlarm_Object = MibTableColumn
hm2SigConSenseIfLinkAlarm = _Hm2SigConSenseIfLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 3, 1, 1),
    _Hm2SigConSenseIfLinkAlarm_Type()
)
hm2SigConSenseIfLinkAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseIfLinkAlarm.setStatus("current")
_Hm2SigConModuleTable_Object = MibTable
hm2SigConModuleTable = _Hm2SigConModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hm2SigConModuleTable.setStatus("current")
_Hm2SigConModuleEntry_Object = MibTableRow
hm2SigConModuleEntry = _Hm2SigConModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 4, 1)
)
hm2SigConModuleEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2SigConID"),
    (0, "HM2-DIAGNOSTIC-MIB", "hm2SigConModID"),
)
if mibBuilder.loadTexts:
    hm2SigConModuleEntry.setStatus("current")


class _Hm2SigConModID_Type(Integer32):
    """Custom type hm2SigConModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Hm2SigConModID_Type.__name__ = "Integer32"
_Hm2SigConModID_Object = MibTableColumn
hm2SigConModID = _Hm2SigConModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 4, 1, 1),
    _Hm2SigConModID_Type()
)
hm2SigConModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConModID.setStatus("current")


class _Hm2SigConSenseModule_Type(HmEnabledStatus):
    """Custom type hm2SigConSenseModule based on HmEnabledStatus"""


_Hm2SigConSenseModule_Object = MibTableColumn
hm2SigConSenseModule = _Hm2SigConSenseModule_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 4, 1, 2),
    _Hm2SigConSenseModule_Type()
)
hm2SigConSenseModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2SigConSenseModule.setStatus("current")
_Hm2SigConStatusTable_Object = MibTable
hm2SigConStatusTable = _Hm2SigConStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hm2SigConStatusTable.setStatus("current")
_Hm2SigConStatusEntry_Object = MibTableRow
hm2SigConStatusEntry = _Hm2SigConStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 10, 1)
)
hm2SigConStatusEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2SigConID"),
    (0, "HM2-DIAGNOSTIC-MIB", "hm2SigConStatusIndex"),
)
if mibBuilder.loadTexts:
    hm2SigConStatusEntry.setStatus("current")
_Hm2SigConStatusIndex_Type = Integer32
_Hm2SigConStatusIndex_Object = MibTableColumn
hm2SigConStatusIndex = _Hm2SigConStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 10, 1, 1),
    _Hm2SigConStatusIndex_Type()
)
hm2SigConStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2SigConStatusIndex.setStatus("current")
_Hm2SigConStatusTimeStamp_Type = HmTimeSeconds1970
_Hm2SigConStatusTimeStamp_Object = MibTableColumn
hm2SigConStatusTimeStamp = _Hm2SigConStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 10, 1, 2),
    _Hm2SigConStatusTimeStamp_Type()
)
hm2SigConStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConStatusTimeStamp.setStatus("current")


class _Hm2SigConStatusTrapCause_Type(Integer32):
    """Custom type hm2SigConStatusTrapCause based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-ip-enabled", 25),
          ("ext-nvm-config-load-unsecure", 21),
          ("ext-nvm-not-in-sync", 8),
          ("ext-nvm-removal", 7),
          ("ext-nvm-update-enabled", 18),
          ("fan-failure", 5),
          ("hidisc-write-enabled", 20),
          ("http-enabled", 15),
          ("https-certificate-warning", 23),
          ("iec61850-mms-enabled", 22),
          ("link-failure", 3),
          ("modbus-tcp-enabled", 24),
          ("module-removal", 6),
          ("no-link", 19),
          ("none", 1),
          ("password-change", 10),
          ("password-min-length", 11),
          ("password-policy-inactive", 13),
          ("password-policy-not-configured", 12),
          ("power-supply", 2),
          ("profinet-io-enabled", 26),
          ("ring-redundancy", 9),
          ("snmp-unsecure", 16),
          ("sysmon-enabled", 17),
          ("telnet-enabled", 14),
          ("temperature", 4))
    )


_Hm2SigConStatusTrapCause_Type.__name__ = "Integer32"
_Hm2SigConStatusTrapCause_Object = MibTableColumn
hm2SigConStatusTrapCause = _Hm2SigConStatusTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 10, 1, 3),
    _Hm2SigConStatusTrapCause_Type()
)
hm2SigConStatusTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConStatusTrapCause.setStatus("current")
_Hm2SigConStatusTrapCauseIndex_Type = Integer32
_Hm2SigConStatusTrapCauseIndex_Object = MibTableColumn
hm2SigConStatusTrapCauseIndex = _Hm2SigConStatusTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 1, 10, 1, 4),
    _Hm2SigConStatusTrapCauseIndex_Type()
)
hm2SigConStatusTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2SigConStatusTrapCauseIndex.setStatus("current")
_Hm2DeviceMonitorGroup_ObjectIdentity = ObjectIdentity
hm2DeviceMonitorGroup = _Hm2DeviceMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2)
)
_Hm2DevMonCommonTable_Object = MibTable
hm2DevMonCommonTable = _Hm2DevMonCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DevMonCommonTable.setStatus("current")
_Hm2DevMonCommonEntry_Object = MibTableRow
hm2DevMonCommonEntry = _Hm2DevMonCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1)
)
hm2DevMonCommonEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevMonID"),
)
if mibBuilder.loadTexts:
    hm2DevMonCommonEntry.setStatus("current")


class _Hm2DevMonID_Type(Integer32):
    """Custom type hm2DevMonID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Hm2DevMonID_Type.__name__ = "Integer32"
_Hm2DevMonID_Object = MibTableColumn
hm2DevMonID = _Hm2DevMonID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 1),
    _Hm2DevMonID_Type()
)
hm2DevMonID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonID.setStatus("current")


class _Hm2DevMonTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2DevMonTrapEnable based on HmEnabledStatus"""


_Hm2DevMonTrapEnable_Object = MibTableColumn
hm2DevMonTrapEnable = _Hm2DevMonTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 2),
    _Hm2DevMonTrapEnable_Type()
)
hm2DevMonTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonTrapEnable.setStatus("current")


class _Hm2DevMonTrapCause_Type(Integer32):
    """Custom type hm2DevMonTrapCause based on Integer32"""
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
        *(("ext-nvm-not-in-sync", 8),
          ("ext-nvm-removal", 7),
          ("fan-failure", 5),
          ("link-failure", 3),
          ("module-removal", 6),
          ("none", 1),
          ("power-supply", 2),
          ("ring-redundancy", 9),
          ("temperature", 4))
    )


_Hm2DevMonTrapCause_Type.__name__ = "Integer32"
_Hm2DevMonTrapCause_Object = MibTableColumn
hm2DevMonTrapCause = _Hm2DevMonTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 3),
    _Hm2DevMonTrapCause_Type()
)
hm2DevMonTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonTrapCause.setStatus("current")
_Hm2DevMonTrapCauseIndex_Type = Integer32
_Hm2DevMonTrapCauseIndex_Object = MibTableColumn
hm2DevMonTrapCauseIndex = _Hm2DevMonTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 4),
    _Hm2DevMonTrapCauseIndex_Type()
)
hm2DevMonTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonTrapCauseIndex.setStatus("current")


class _Hm2DevMonOperState_Type(Integer32):
    """Custom type hm2DevMonOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("noerror", 1))
    )


_Hm2DevMonOperState_Type.__name__ = "Integer32"
_Hm2DevMonOperState_Object = MibTableColumn
hm2DevMonOperState = _Hm2DevMonOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 5),
    _Hm2DevMonOperState_Type()
)
hm2DevMonOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonOperState.setStatus("current")
_Hm2DevMonOperTimeStamp_Type = HmTimeSeconds1970
_Hm2DevMonOperTimeStamp_Object = MibTableColumn
hm2DevMonOperTimeStamp = _Hm2DevMonOperTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 6),
    _Hm2DevMonOperTimeStamp_Type()
)
hm2DevMonOperTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonOperTimeStamp.setStatus("current")


class _Hm2DevMonSenseLinkFailure_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseLinkFailure based on HmEnabledStatus"""


_Hm2DevMonSenseLinkFailure_Object = MibTableColumn
hm2DevMonSenseLinkFailure = _Hm2DevMonSenseLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 7),
    _Hm2DevMonSenseLinkFailure_Type()
)
hm2DevMonSenseLinkFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseLinkFailure.setStatus("current")


class _Hm2DevMonSenseTemperature_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseTemperature based on HmEnabledStatus"""


_Hm2DevMonSenseTemperature_Object = MibTableColumn
hm2DevMonSenseTemperature = _Hm2DevMonSenseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 8),
    _Hm2DevMonSenseTemperature_Type()
)
hm2DevMonSenseTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseTemperature.setStatus("current")


class _Hm2DevMonSenseFan_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseFan based on HmEnabledStatus"""


_Hm2DevMonSenseFan_Object = MibTableColumn
hm2DevMonSenseFan = _Hm2DevMonSenseFan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 9),
    _Hm2DevMonSenseFan_Type()
)
hm2DevMonSenseFan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseFan.setStatus("current")


class _Hm2DevMonSenseModuleRemoval_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseModuleRemoval based on HmEnabledStatus"""


_Hm2DevMonSenseModuleRemoval_Object = MibTableColumn
hm2DevMonSenseModuleRemoval = _Hm2DevMonSenseModuleRemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 10),
    _Hm2DevMonSenseModuleRemoval_Type()
)
hm2DevMonSenseModuleRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseModuleRemoval.setStatus("current")


class _Hm2DevMonSenseExtNvmRemoval_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseExtNvmRemoval based on HmEnabledStatus"""


_Hm2DevMonSenseExtNvmRemoval_Object = MibTableColumn
hm2DevMonSenseExtNvmRemoval = _Hm2DevMonSenseExtNvmRemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 11),
    _Hm2DevMonSenseExtNvmRemoval_Type()
)
hm2DevMonSenseExtNvmRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseExtNvmRemoval.setStatus("current")


class _Hm2DevMonSenseExtNvmNotInSync_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseExtNvmNotInSync based on HmEnabledStatus"""


_Hm2DevMonSenseExtNvmNotInSync_Object = MibTableColumn
hm2DevMonSenseExtNvmNotInSync = _Hm2DevMonSenseExtNvmNotInSync_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 12),
    _Hm2DevMonSenseExtNvmNotInSync_Type()
)
hm2DevMonSenseExtNvmNotInSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseExtNvmNotInSync.setStatus("current")


class _Hm2DevMonSenseRingRedundancy_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseRingRedundancy based on HmEnabledStatus"""


_Hm2DevMonSenseRingRedundancy_Object = MibTableColumn
hm2DevMonSenseRingRedundancy = _Hm2DevMonSenseRingRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 1, 1, 13),
    _Hm2DevMonSenseRingRedundancy_Type()
)
hm2DevMonSenseRingRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseRingRedundancy.setStatus("current")
_Hm2DevMonPSTable_Object = MibTable
hm2DevMonPSTable = _Hm2DevMonPSTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hm2DevMonPSTable.setStatus("current")
_Hm2DevMonPSEntry_Object = MibTableRow
hm2DevMonPSEntry = _Hm2DevMonPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 2, 1)
)
hm2DevMonPSEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevMonID"),
    (0, "HM2-PWRMGMT-MIB", "hm2PSID"),
)
if mibBuilder.loadTexts:
    hm2DevMonPSEntry.setStatus("current")


class _Hm2DevMonSensePSState_Type(HmEnabledStatus):
    """Custom type hm2DevMonSensePSState based on HmEnabledStatus"""


_Hm2DevMonSensePSState_Object = MibTableColumn
hm2DevMonSensePSState = _Hm2DevMonSensePSState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 2, 1, 1),
    _Hm2DevMonSensePSState_Type()
)
hm2DevMonSensePSState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSensePSState.setStatus("current")
_Hm2DevMonInterfaceTable_Object = MibTable
hm2DevMonInterfaceTable = _Hm2DevMonInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hm2DevMonInterfaceTable.setStatus("current")
_Hm2DevMonInterfaceEntry_Object = MibTableRow
hm2DevMonInterfaceEntry = _Hm2DevMonInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 3, 1)
)
hm2DevMonInterfaceEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevMonID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2DevMonInterfaceEntry.setStatus("current")


class _Hm2DevMonSenseIfLinkAlarm_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseIfLinkAlarm based on HmEnabledStatus"""


_Hm2DevMonSenseIfLinkAlarm_Object = MibTableColumn
hm2DevMonSenseIfLinkAlarm = _Hm2DevMonSenseIfLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 3, 1, 1),
    _Hm2DevMonSenseIfLinkAlarm_Type()
)
hm2DevMonSenseIfLinkAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseIfLinkAlarm.setStatus("current")
_Hm2DevMonModuleTable_Object = MibTable
hm2DevMonModuleTable = _Hm2DevMonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hm2DevMonModuleTable.setStatus("current")
_Hm2DevMonModuleEntry_Object = MibTableRow
hm2DevMonModuleEntry = _Hm2DevMonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 4, 1)
)
hm2DevMonModuleEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevMonID"),
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevMonModID"),
)
if mibBuilder.loadTexts:
    hm2DevMonModuleEntry.setStatus("current")


class _Hm2DevMonModID_Type(Integer32):
    """Custom type hm2DevMonModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Hm2DevMonModID_Type.__name__ = "Integer32"
_Hm2DevMonModID_Object = MibTableColumn
hm2DevMonModID = _Hm2DevMonModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 4, 1, 1),
    _Hm2DevMonModID_Type()
)
hm2DevMonModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonModID.setStatus("current")


class _Hm2DevMonSenseModule_Type(HmEnabledStatus):
    """Custom type hm2DevMonSenseModule based on HmEnabledStatus"""


_Hm2DevMonSenseModule_Object = MibTableColumn
hm2DevMonSenseModule = _Hm2DevMonSenseModule_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 4, 1, 2),
    _Hm2DevMonSenseModule_Type()
)
hm2DevMonSenseModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevMonSenseModule.setStatus("current")
_Hm2DevMonStatusTable_Object = MibTable
hm2DevMonStatusTable = _Hm2DevMonStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 10)
)
if mibBuilder.loadTexts:
    hm2DevMonStatusTable.setStatus("current")
_Hm2DevMonStatusEntry_Object = MibTableRow
hm2DevMonStatusEntry = _Hm2DevMonStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 10, 1)
)
hm2DevMonStatusEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevMonID"),
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevMonStatusIndex"),
)
if mibBuilder.loadTexts:
    hm2DevMonStatusEntry.setStatus("current")
_Hm2DevMonStatusIndex_Type = Integer32
_Hm2DevMonStatusIndex_Object = MibTableColumn
hm2DevMonStatusIndex = _Hm2DevMonStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 10, 1, 1),
    _Hm2DevMonStatusIndex_Type()
)
hm2DevMonStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DevMonStatusIndex.setStatus("current")
_Hm2DevMonStatusTimeStamp_Type = HmTimeSeconds1970
_Hm2DevMonStatusTimeStamp_Object = MibTableColumn
hm2DevMonStatusTimeStamp = _Hm2DevMonStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 10, 1, 2),
    _Hm2DevMonStatusTimeStamp_Type()
)
hm2DevMonStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonStatusTimeStamp.setStatus("current")


class _Hm2DevMonStatusTrapCause_Type(Integer32):
    """Custom type hm2DevMonStatusTrapCause based on Integer32"""
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
        *(("ext-nvm-not-in-sync", 8),
          ("ext-nvm-removal", 7),
          ("fan-failure", 5),
          ("link-failure", 3),
          ("module-removal", 6),
          ("none", 1),
          ("power-supply", 2),
          ("ring-redundancy", 9),
          ("temperature", 4))
    )


_Hm2DevMonStatusTrapCause_Type.__name__ = "Integer32"
_Hm2DevMonStatusTrapCause_Object = MibTableColumn
hm2DevMonStatusTrapCause = _Hm2DevMonStatusTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 10, 1, 3),
    _Hm2DevMonStatusTrapCause_Type()
)
hm2DevMonStatusTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonStatusTrapCause.setStatus("current")
_Hm2DevMonStatusTrapCauseIndex_Type = Integer32
_Hm2DevMonStatusTrapCauseIndex_Object = MibTableColumn
hm2DevMonStatusTrapCauseIndex = _Hm2DevMonStatusTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 2, 10, 1, 4),
    _Hm2DevMonStatusTrapCauseIndex_Type()
)
hm2DevMonStatusTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevMonStatusTrapCauseIndex.setStatus("current")
_Hm2DeviceSecurityGroup_ObjectIdentity = ObjectIdentity
hm2DeviceSecurityGroup = _Hm2DeviceSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3)
)
_Hm2DevSecConfigGroup_ObjectIdentity = ObjectIdentity
hm2DevSecConfigGroup = _Hm2DevSecConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1)
)


class _Hm2DevSecTrapEnable_Type(HmEnabledStatus):
    """Custom type hm2DevSecTrapEnable based on HmEnabledStatus"""


_Hm2DevSecTrapEnable_Object = MibScalar
hm2DevSecTrapEnable = _Hm2DevSecTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 1),
    _Hm2DevSecTrapEnable_Type()
)
hm2DevSecTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecTrapEnable.setStatus("current")


class _Hm2DevSecTrapCause_Type(Integer32):
    """Custom type hm2DevSecTrapCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-ip-enabled", 25),
          ("ext-nvm-config-load-unsecure", 21),
          ("ext-nvm-update-enabled", 18),
          ("hidisc-write-enabled", 20),
          ("http-enabled", 15),
          ("https-certificate-warning", 23),
          ("iec61850-mms-enabled", 22),
          ("modbus-tcp-enabled", 24),
          ("no-link", 19),
          ("none", 1),
          ("password-change", 10),
          ("password-min-length", 11),
          ("password-policy-inactive", 13),
          ("password-policy-not-configured", 12),
          ("profinet-io-enabled", 26),
          ("snmp-unsecure", 16),
          ("sysmon-enabled", 17),
          ("telnet-enabled", 14))
    )


_Hm2DevSecTrapCause_Type.__name__ = "Integer32"
_Hm2DevSecTrapCause_Object = MibScalar
hm2DevSecTrapCause = _Hm2DevSecTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 2),
    _Hm2DevSecTrapCause_Type()
)
hm2DevSecTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevSecTrapCause.setStatus("current")
_Hm2DevSecTrapCauseIndex_Type = Integer32
_Hm2DevSecTrapCauseIndex_Object = MibScalar
hm2DevSecTrapCauseIndex = _Hm2DevSecTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 3),
    _Hm2DevSecTrapCauseIndex_Type()
)
hm2DevSecTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevSecTrapCauseIndex.setStatus("current")


class _Hm2DevSecOperState_Type(Integer32):
    """Custom type hm2DevSecOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("noerror", 1))
    )


_Hm2DevSecOperState_Type.__name__ = "Integer32"
_Hm2DevSecOperState_Object = MibScalar
hm2DevSecOperState = _Hm2DevSecOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 4),
    _Hm2DevSecOperState_Type()
)
hm2DevSecOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevSecOperState.setStatus("current")
_Hm2DevSecOperTimeStamp_Type = HmTimeSeconds1970
_Hm2DevSecOperTimeStamp_Object = MibScalar
hm2DevSecOperTimeStamp = _Hm2DevSecOperTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 5),
    _Hm2DevSecOperTimeStamp_Type()
)
hm2DevSecOperTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevSecOperTimeStamp.setStatus("current")


class _Hm2DevSecSensePasswordChange_Type(HmEnabledStatus):
    """Custom type hm2DevSecSensePasswordChange based on HmEnabledStatus"""


_Hm2DevSecSensePasswordChange_Object = MibScalar
hm2DevSecSensePasswordChange = _Hm2DevSecSensePasswordChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 6),
    _Hm2DevSecSensePasswordChange_Type()
)
hm2DevSecSensePasswordChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSensePasswordChange.setStatus("current")


class _Hm2DevSecSensePasswordMinLength_Type(HmEnabledStatus):
    """Custom type hm2DevSecSensePasswordMinLength based on HmEnabledStatus"""


_Hm2DevSecSensePasswordMinLength_Object = MibScalar
hm2DevSecSensePasswordMinLength = _Hm2DevSecSensePasswordMinLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 7),
    _Hm2DevSecSensePasswordMinLength_Type()
)
hm2DevSecSensePasswordMinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSensePasswordMinLength.setStatus("current")


class _Hm2DevSecSensePasswordStrengthNotConfigured_Type(HmEnabledStatus):
    """Custom type hm2DevSecSensePasswordStrengthNotConfigured based on HmEnabledStatus"""


_Hm2DevSecSensePasswordStrengthNotConfigured_Object = MibScalar
hm2DevSecSensePasswordStrengthNotConfigured = _Hm2DevSecSensePasswordStrengthNotConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 8),
    _Hm2DevSecSensePasswordStrengthNotConfigured_Type()
)
hm2DevSecSensePasswordStrengthNotConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSensePasswordStrengthNotConfigured.setStatus("current")


class _Hm2DevSecSenseBypassPasswordStrength_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseBypassPasswordStrength based on HmEnabledStatus"""


_Hm2DevSecSenseBypassPasswordStrength_Object = MibScalar
hm2DevSecSenseBypassPasswordStrength = _Hm2DevSecSenseBypassPasswordStrength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 9),
    _Hm2DevSecSenseBypassPasswordStrength_Type()
)
hm2DevSecSenseBypassPasswordStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseBypassPasswordStrength.setStatus("current")


class _Hm2DevSecSenseTelnetEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseTelnetEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseTelnetEnabled_Object = MibScalar
hm2DevSecSenseTelnetEnabled = _Hm2DevSecSenseTelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 10),
    _Hm2DevSecSenseTelnetEnabled_Type()
)
hm2DevSecSenseTelnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseTelnetEnabled.setStatus("current")


class _Hm2DevSecSenseHttpEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseHttpEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseHttpEnabled_Object = MibScalar
hm2DevSecSenseHttpEnabled = _Hm2DevSecSenseHttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 11),
    _Hm2DevSecSenseHttpEnabled_Type()
)
hm2DevSecSenseHttpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseHttpEnabled.setStatus("current")


class _Hm2DevSecSenseSnmpUnsecure_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseSnmpUnsecure based on HmEnabledStatus"""


_Hm2DevSecSenseSnmpUnsecure_Object = MibScalar
hm2DevSecSenseSnmpUnsecure = _Hm2DevSecSenseSnmpUnsecure_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 12),
    _Hm2DevSecSenseSnmpUnsecure_Type()
)
hm2DevSecSenseSnmpUnsecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseSnmpUnsecure.setStatus("current")


class _Hm2DevSecSenseSysmonEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseSysmonEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseSysmonEnabled_Object = MibScalar
hm2DevSecSenseSysmonEnabled = _Hm2DevSecSenseSysmonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 13),
    _Hm2DevSecSenseSysmonEnabled_Type()
)
hm2DevSecSenseSysmonEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseSysmonEnabled.setStatus("current")


class _Hm2DevSecSenseExtNvmUpdateEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseExtNvmUpdateEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseExtNvmUpdateEnabled_Object = MibScalar
hm2DevSecSenseExtNvmUpdateEnabled = _Hm2DevSecSenseExtNvmUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 14),
    _Hm2DevSecSenseExtNvmUpdateEnabled_Type()
)
hm2DevSecSenseExtNvmUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseExtNvmUpdateEnabled.setStatus("current")


class _Hm2DevSecSenseNoLinkEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseNoLinkEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseNoLinkEnabled_Object = MibScalar
hm2DevSecSenseNoLinkEnabled = _Hm2DevSecSenseNoLinkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 15),
    _Hm2DevSecSenseNoLinkEnabled_Type()
)
hm2DevSecSenseNoLinkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseNoLinkEnabled.setStatus("current")


class _Hm2DevSecSenseHiDiscoveryEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseHiDiscoveryEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseHiDiscoveryEnabled_Object = MibScalar
hm2DevSecSenseHiDiscoveryEnabled = _Hm2DevSecSenseHiDiscoveryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 16),
    _Hm2DevSecSenseHiDiscoveryEnabled_Type()
)
hm2DevSecSenseHiDiscoveryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseHiDiscoveryEnabled.setStatus("current")


class _Hm2DevSecSenseExtNvmConfigLoadUnsecure_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseExtNvmConfigLoadUnsecure based on HmEnabledStatus"""


_Hm2DevSecSenseExtNvmConfigLoadUnsecure_Object = MibScalar
hm2DevSecSenseExtNvmConfigLoadUnsecure = _Hm2DevSecSenseExtNvmConfigLoadUnsecure_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 17),
    _Hm2DevSecSenseExtNvmConfigLoadUnsecure_Type()
)
hm2DevSecSenseExtNvmConfigLoadUnsecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseExtNvmConfigLoadUnsecure.setStatus("current")


class _Hm2DevSecSenseIec61850MmsEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseIec61850MmsEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseIec61850MmsEnabled_Object = MibScalar
hm2DevSecSenseIec61850MmsEnabled = _Hm2DevSecSenseIec61850MmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 18),
    _Hm2DevSecSenseIec61850MmsEnabled_Type()
)
hm2DevSecSenseIec61850MmsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseIec61850MmsEnabled.setStatus("current")


class _Hm2DevSecSenseHttpsCertificateWarning_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseHttpsCertificateWarning based on HmEnabledStatus"""


_Hm2DevSecSenseHttpsCertificateWarning_Object = MibScalar
hm2DevSecSenseHttpsCertificateWarning = _Hm2DevSecSenseHttpsCertificateWarning_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 19),
    _Hm2DevSecSenseHttpsCertificateWarning_Type()
)
hm2DevSecSenseHttpsCertificateWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseHttpsCertificateWarning.setStatus("current")


class _Hm2DevSecSenseModbusTcpEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseModbusTcpEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseModbusTcpEnabled_Object = MibScalar
hm2DevSecSenseModbusTcpEnabled = _Hm2DevSecSenseModbusTcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 20),
    _Hm2DevSecSenseModbusTcpEnabled_Type()
)
hm2DevSecSenseModbusTcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseModbusTcpEnabled.setStatus("current")


class _Hm2DevSecSenseEtherNetIpEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseEtherNetIpEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseEtherNetIpEnabled_Object = MibScalar
hm2DevSecSenseEtherNetIpEnabled = _Hm2DevSecSenseEtherNetIpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 21),
    _Hm2DevSecSenseEtherNetIpEnabled_Type()
)
hm2DevSecSenseEtherNetIpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseEtherNetIpEnabled.setStatus("current")


class _Hm2DevSecSenseProfinetIOEnabled_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseProfinetIOEnabled based on HmEnabledStatus"""


_Hm2DevSecSenseProfinetIOEnabled_Object = MibScalar
hm2DevSecSenseProfinetIOEnabled = _Hm2DevSecSenseProfinetIOEnabled_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 1, 22),
    _Hm2DevSecSenseProfinetIOEnabled_Type()
)
hm2DevSecSenseProfinetIOEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseProfinetIOEnabled.setStatus("current")
_Hm2DevSecInterfaceTable_Object = MibTable
hm2DevSecInterfaceTable = _Hm2DevSecInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hm2DevSecInterfaceTable.setStatus("current")
_Hm2DevSecInterfaceEntry_Object = MibTableRow
hm2DevSecInterfaceEntry = _Hm2DevSecInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 2, 1)
)
hm2DevSecInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2DevSecInterfaceEntry.setStatus("current")


class _Hm2DevSecSenseIfNoLink_Type(HmEnabledStatus):
    """Custom type hm2DevSecSenseIfNoLink based on HmEnabledStatus"""


_Hm2DevSecSenseIfNoLink_Object = MibTableColumn
hm2DevSecSenseIfNoLink = _Hm2DevSecSenseIfNoLink_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 2, 1, 1),
    _Hm2DevSecSenseIfNoLink_Type()
)
hm2DevSecSenseIfNoLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DevSecSenseIfNoLink.setStatus("current")
_Hm2DevSecStatusTable_Object = MibTable
hm2DevSecStatusTable = _Hm2DevSecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 10)
)
if mibBuilder.loadTexts:
    hm2DevSecStatusTable.setStatus("current")
_Hm2DevSecStatusEntry_Object = MibTableRow
hm2DevSecStatusEntry = _Hm2DevSecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 10, 1)
)
hm2DevSecStatusEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DevSecStatusIndex"),
)
if mibBuilder.loadTexts:
    hm2DevSecStatusEntry.setStatus("current")
_Hm2DevSecStatusIndex_Type = Integer32
_Hm2DevSecStatusIndex_Object = MibTableColumn
hm2DevSecStatusIndex = _Hm2DevSecStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 10, 1, 1),
    _Hm2DevSecStatusIndex_Type()
)
hm2DevSecStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DevSecStatusIndex.setStatus("current")
_Hm2DevSecStatusTimeStamp_Type = HmTimeSeconds1970
_Hm2DevSecStatusTimeStamp_Object = MibTableColumn
hm2DevSecStatusTimeStamp = _Hm2DevSecStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 10, 1, 2),
    _Hm2DevSecStatusTimeStamp_Type()
)
hm2DevSecStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevSecStatusTimeStamp.setStatus("current")


class _Hm2DevSecStatusTrapCause_Type(Integer32):
    """Custom type hm2DevSecStatusTrapCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-ip-enabled", 25),
          ("ext-nvm-config-load-unsecure", 21),
          ("ext-nvm-update-enabled", 18),
          ("hidisc-write-enabled", 20),
          ("http-enabled", 15),
          ("https-certificate-warning", 23),
          ("iec61850-mms-enabled", 22),
          ("modbus-tcp-enabled", 24),
          ("no-link", 19),
          ("none", 1),
          ("password-change", 10),
          ("password-min-length", 11),
          ("password-policy-inactive", 13),
          ("password-policy-not-configured", 12),
          ("profinet-io-enabled", 26),
          ("snmp-unsecure", 16),
          ("sysmon-enabled", 17),
          ("telnet-enabled", 14))
    )


_Hm2DevSecStatusTrapCause_Type.__name__ = "Integer32"
_Hm2DevSecStatusTrapCause_Object = MibTableColumn
hm2DevSecStatusTrapCause = _Hm2DevSecStatusTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 10, 1, 3),
    _Hm2DevSecStatusTrapCause_Type()
)
hm2DevSecStatusTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevSecStatusTrapCause.setStatus("current")
_Hm2DevSecStatusTrapCauseIndex_Type = Integer32
_Hm2DevSecStatusTrapCauseIndex_Object = MibTableColumn
hm2DevSecStatusTrapCauseIndex = _Hm2DevSecStatusTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 3, 3, 10, 1, 4),
    _Hm2DevSecStatusTrapCauseIndex_Type()
)
hm2DevSecStatusTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DevSecStatusTrapCauseIndex.setStatus("current")
_Hm2DiagLedGroup_ObjectIdentity = ObjectIdentity
hm2DiagLedGroup = _Hm2DiagLedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4)
)
_Hm2LedGlobalTable_Object = MibTable
hm2LedGlobalTable = _Hm2LedGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hm2LedGlobalTable.setStatus("current")
_Hm2LedGlobalEntry_Object = MibTableRow
hm2LedGlobalEntry = _Hm2LedGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 1, 1)
)
hm2LedGlobalEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2LedGlobalLedType"),
)
if mibBuilder.loadTexts:
    hm2LedGlobalEntry.setStatus("current")
_Hm2LedGlobalLedType_Type = Hm2LedType
_Hm2LedGlobalLedType_Object = MibTableColumn
hm2LedGlobalLedType = _Hm2LedGlobalLedType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 1, 1, 1),
    _Hm2LedGlobalLedType_Type()
)
hm2LedGlobalLedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2LedGlobalLedType.setStatus("current")
_Hm2LedGlobalStatus_Type = Hm2LedStatus
_Hm2LedGlobalStatus_Object = MibTableColumn
hm2LedGlobalStatus = _Hm2LedGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 1, 1, 2),
    _Hm2LedGlobalStatus_Type()
)
hm2LedGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LedGlobalStatus.setStatus("current")
_Hm2LedPortTable_Object = MibTable
hm2LedPortTable = _Hm2LedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hm2LedPortTable.setStatus("current")
_Hm2LedPortEntry_Object = MibTableRow
hm2LedPortEntry = _Hm2LedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 2, 1)
)
hm2LedPortEntry.setIndexNames(
    (0, "HM2-DEVMGMT-MIB", "hm2IfacePhysIndex"),
)
if mibBuilder.loadTexts:
    hm2LedPortEntry.setStatus("current")
_Hm2LedPortStatus_Type = Hm2LedStatus
_Hm2LedPortStatus_Object = MibTableColumn
hm2LedPortStatus = _Hm2LedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 2, 1, 1),
    _Hm2LedPortStatus_Type()
)
hm2LedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LedPortStatus.setStatus("current")
_Hm2LedPortPoeStatus_Type = Hm2LedStatus
_Hm2LedPortPoeStatus_Object = MibTableColumn
hm2LedPortPoeStatus = _Hm2LedPortPoeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 2, 1, 2),
    _Hm2LedPortPoeStatus_Type()
)
hm2LedPortPoeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LedPortPoeStatus.setStatus("current")


class _Hm2LedPortSignaling_Type(HmEnabledStatus):
    """Custom type hm2LedPortSignaling based on HmEnabledStatus"""


_Hm2LedPortSignaling_Object = MibTableColumn
hm2LedPortSignaling = _Hm2LedPortSignaling_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 2, 1, 3),
    _Hm2LedPortSignaling_Type()
)
hm2LedPortSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LedPortSignaling.setStatus("current")
_Hm2LedControlGroup_ObjectIdentity = ObjectIdentity
hm2LedControlGroup = _Hm2LedControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 3)
)


class _Hm2LedPortMode_Type(Integer32):
    """Custom type hm2LedPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("portpanel", 0),
          ("servicepanel", 1))
    )


_Hm2LedPortMode_Type.__name__ = "Integer32"
_Hm2LedPortMode_Object = MibScalar
hm2LedPortMode = _Hm2LedPortMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 4, 3, 1),
    _Hm2LedPortMode_Type()
)
hm2LedPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LedPortMode.setStatus("current")
_Hm2DiagIfaceUtilizationGroup_ObjectIdentity = ObjectIdentity
hm2DiagIfaceUtilizationGroup = _Hm2DiagIfaceUtilizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5)
)
_Hm2DiagIfaceUtilizationTable_Object = MibTable
hm2DiagIfaceUtilizationTable = _Hm2DiagIfaceUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilizationTable.setStatus("current")
_Hm2DiagIfaceUtilizationEntry_Object = MibTableRow
hm2DiagIfaceUtilizationEntry = _Hm2DiagIfaceUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5, 1, 1)
)
hm2DiagIfaceUtilizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilizationEntry.setStatus("current")


class _Hm2DiagIfaceUtilization_Type(Integer32):
    """Custom type hm2DiagIfaceUtilization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hm2DiagIfaceUtilization_Type.__name__ = "Integer32"
_Hm2DiagIfaceUtilization_Object = MibTableColumn
hm2DiagIfaceUtilization = _Hm2DiagIfaceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5, 1, 1, 1),
    _Hm2DiagIfaceUtilization_Type()
)
hm2DiagIfaceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilization.setStatus("current")


class _Hm2DiagIfaceUtilizationControlInterval_Type(Integer32):
    """Custom type hm2DiagIfaceUtilizationControlInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hm2DiagIfaceUtilizationControlInterval_Type.__name__ = "Integer32"
_Hm2DiagIfaceUtilizationControlInterval_Object = MibTableColumn
hm2DiagIfaceUtilizationControlInterval = _Hm2DiagIfaceUtilizationControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5, 1, 1, 2),
    _Hm2DiagIfaceUtilizationControlInterval_Type()
)
hm2DiagIfaceUtilizationControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilizationControlInterval.setStatus("current")


class _Hm2DiagIfaceUtilizationAlarmLowerThreshold_Type(Integer32):
    """Custom type hm2DiagIfaceUtilizationAlarmLowerThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hm2DiagIfaceUtilizationAlarmLowerThreshold_Type.__name__ = "Integer32"
_Hm2DiagIfaceUtilizationAlarmLowerThreshold_Object = MibTableColumn
hm2DiagIfaceUtilizationAlarmLowerThreshold = _Hm2DiagIfaceUtilizationAlarmLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5, 1, 1, 3),
    _Hm2DiagIfaceUtilizationAlarmLowerThreshold_Type()
)
hm2DiagIfaceUtilizationAlarmLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilizationAlarmLowerThreshold.setStatus("current")


class _Hm2DiagIfaceUtilizationAlarmUpperThreshold_Type(Integer32):
    """Custom type hm2DiagIfaceUtilizationAlarmUpperThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hm2DiagIfaceUtilizationAlarmUpperThreshold_Type.__name__ = "Integer32"
_Hm2DiagIfaceUtilizationAlarmUpperThreshold_Object = MibTableColumn
hm2DiagIfaceUtilizationAlarmUpperThreshold = _Hm2DiagIfaceUtilizationAlarmUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5, 1, 1, 4),
    _Hm2DiagIfaceUtilizationAlarmUpperThreshold_Type()
)
hm2DiagIfaceUtilizationAlarmUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilizationAlarmUpperThreshold.setStatus("current")
_Hm2DiagIfaceUtilizationAlarmCondition_Type = TruthValue
_Hm2DiagIfaceUtilizationAlarmCondition_Object = MibTableColumn
hm2DiagIfaceUtilizationAlarmCondition = _Hm2DiagIfaceUtilizationAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 5, 1, 1, 5),
    _Hm2DiagIfaceUtilizationAlarmCondition_Type()
)
hm2DiagIfaceUtilizationAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilizationAlarmCondition.setStatus("current")
_Hm2DiagCableTesterGroup_ObjectIdentity = ObjectIdentity
hm2DiagCableTesterGroup = _Hm2DiagCableTesterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6)
)


class _Hm2DiagCableTesterStatus_Type(Integer32):
    """Custom type hm2DiagCableTesterStatus based on Integer32"""
    defaultValue = 4

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
        *(("active", 1),
          ("failure", 3),
          ("success", 2),
          ("uninitialized", 4))
    )


_Hm2DiagCableTesterStatus_Type.__name__ = "Integer32"
_Hm2DiagCableTesterStatus_Object = MibScalar
hm2DiagCableTesterStatus = _Hm2DiagCableTesterStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 1),
    _Hm2DiagCableTesterStatus_Type()
)
hm2DiagCableTesterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagCableTesterStatus.setStatus("current")


class _Hm2DiagCableTesterIfIndex_Type(Unsigned32):
    """Custom type hm2DiagCableTesterIfIndex based on Unsigned32"""
    defaultValue = 0


_Hm2DiagCableTesterIfIndex_Object = MibScalar
hm2DiagCableTesterIfIndex = _Hm2DiagCableTesterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 2),
    _Hm2DiagCableTesterIfIndex_Type()
)
hm2DiagCableTesterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagCableTesterIfIndex.setStatus("current")
_Hm2DiagCableTesterCableTable_Object = MibTable
hm2DiagCableTesterCableTable = _Hm2DiagCableTesterCableTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 10)
)
if mibBuilder.loadTexts:
    hm2DiagCableTesterCableTable.setStatus("current")
_Hm2DiagCableTesterCableEntry_Object = MibTableRow
hm2DiagCableTesterCableEntry = _Hm2DiagCableTesterCableEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 10, 1)
)
hm2DiagCableTesterCableEntry.setIndexNames(
    (0, "HM2-DIAGNOSTIC-MIB", "hm2DiagCableTesterCablePair"),
)
if mibBuilder.loadTexts:
    hm2DiagCableTesterCableEntry.setStatus("current")


class _Hm2DiagCableTesterCablePair_Type(Integer32):
    """Custom type hm2DiagCableTesterCablePair based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2DiagCableTesterCablePair_Type.__name__ = "Integer32"
_Hm2DiagCableTesterCablePair_Object = MibTableColumn
hm2DiagCableTesterCablePair = _Hm2DiagCableTesterCablePair_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 10, 1, 1),
    _Hm2DiagCableTesterCablePair_Type()
)
hm2DiagCableTesterCablePair.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2DiagCableTesterCablePair.setStatus("current")


class _Hm2DiagCableTesterCableStatus_Type(Integer32):
    """Custom type hm2DiagCableTesterCableStatus based on Integer32"""
    defaultValue = 4

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
        *(("normal", 1),
          ("open", 2),
          ("short", 3),
          ("unknown", 4))
    )


_Hm2DiagCableTesterCableStatus_Type.__name__ = "Integer32"
_Hm2DiagCableTesterCableStatus_Object = MibTableColumn
hm2DiagCableTesterCableStatus = _Hm2DiagCableTesterCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 10, 1, 2),
    _Hm2DiagCableTesterCableStatus_Type()
)
hm2DiagCableTesterCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCableTesterCableStatus.setStatus("current")


class _Hm2DiagCableTesterCableMinimumLength_Type(Unsigned32):
    """Custom type hm2DiagCableTesterCableMinimumLength based on Unsigned32"""
    defaultValue = 0


_Hm2DiagCableTesterCableMinimumLength_Object = MibTableColumn
hm2DiagCableTesterCableMinimumLength = _Hm2DiagCableTesterCableMinimumLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 10, 1, 3),
    _Hm2DiagCableTesterCableMinimumLength_Type()
)
hm2DiagCableTesterCableMinimumLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCableTesterCableMinimumLength.setStatus("current")


class _Hm2DiagCableTesterCableMaximumLength_Type(Unsigned32):
    """Custom type hm2DiagCableTesterCableMaximumLength based on Unsigned32"""
    defaultValue = 0


_Hm2DiagCableTesterCableMaximumLength_Object = MibTableColumn
hm2DiagCableTesterCableMaximumLength = _Hm2DiagCableTesterCableMaximumLength_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 10, 1, 4),
    _Hm2DiagCableTesterCableMaximumLength_Type()
)
hm2DiagCableTesterCableMaximumLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCableTesterCableMaximumLength.setStatus("current")


class _Hm2DiagCableTesterCableFailureLocation_Type(Unsigned32):
    """Custom type hm2DiagCableTesterCableFailureLocation based on Unsigned32"""
    defaultValue = 0


_Hm2DiagCableTesterCableFailureLocation_Object = MibTableColumn
hm2DiagCableTesterCableFailureLocation = _Hm2DiagCableTesterCableFailureLocation_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 6, 10, 1, 5),
    _Hm2DiagCableTesterCableFailureLocation_Type()
)
hm2DiagCableTesterCableFailureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCableTesterCableFailureLocation.setStatus("current")
_Hm2PortMonitorGroup_ObjectIdentity = ObjectIdentity
hm2PortMonitorGroup = _Hm2PortMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7)
)


class _Hm2PortMonitorAdminMode_Type(TruthValue):
    """Custom type hm2PortMonitorAdminMode based on TruthValue"""


_Hm2PortMonitorAdminMode_Object = MibScalar
hm2PortMonitorAdminMode = _Hm2PortMonitorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 1),
    _Hm2PortMonitorAdminMode_Type()
)
hm2PortMonitorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorAdminMode.setStatus("current")
_Hm2PortMonitorIntfTable_Object = MibTable
hm2PortMonitorIntfTable = _Hm2PortMonitorIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hm2PortMonitorIntfTable.setStatus("current")
_Hm2PortMonitorIntfEntry_Object = MibTableRow
hm2PortMonitorIntfEntry = _Hm2PortMonitorIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 2, 1)
)
hm2PortMonitorIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2PortMonitorIntfEntry.setStatus("current")


class _Hm2PortMonitorIntfReset_Type(TruthValue):
    """Custom type hm2PortMonitorIntfReset based on TruthValue"""


_Hm2PortMonitorIntfReset_Object = MibTableColumn
hm2PortMonitorIntfReset = _Hm2PortMonitorIntfReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 2, 1, 2),
    _Hm2PortMonitorIntfReset_Type()
)
hm2PortMonitorIntfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorIntfReset.setStatus("current")


class _Hm2PortMonitorIntfAction_Type(Integer32):
    """Custom type hm2PortMonitorIntfAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-disable", 3),
          ("port-disable", 1),
          ("trap-only", 2))
    )


_Hm2PortMonitorIntfAction_Type.__name__ = "Integer32"
_Hm2PortMonitorIntfAction_Object = MibTableColumn
hm2PortMonitorIntfAction = _Hm2PortMonitorIntfAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 2, 1, 3),
    _Hm2PortMonitorIntfAction_Type()
)
hm2PortMonitorIntfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorIntfAction.setStatus("current")
_Hm2PortMonitorConditionGroup_ObjectIdentity = ObjectIdentity
hm2PortMonitorConditionGroup = _Hm2PortMonitorConditionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3)
)
_Hm2PortMonitorConditionIntfTable_Object = MibTable
hm2PortMonitorConditionIntfTable = _Hm2PortMonitorConditionIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionIntfTable.setStatus("current")
_Hm2PortMonitorConditionIntfEntry_Object = MibTableRow
hm2PortMonitorConditionIntfEntry = _Hm2PortMonitorConditionIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1, 1)
)
hm2PortMonitorConditionIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionIntfEntry.setStatus("current")


class _Hm2PortMonitorConditionField_Type(Bits):
    """Custom type hm2PortMonitorConditionField based on Bits"""
    namedValues = NamedValues(
        *(("crcFragments", 2),
          ("duplexMismatch", 3),
          ("link-flap", 1),
          ("none", 0),
          ("overload-detection", 4),
          ("speed-duplex", 5))
    )

_Hm2PortMonitorConditionField_Type.__name__ = "Bits"
_Hm2PortMonitorConditionField_Object = MibTableColumn
hm2PortMonitorConditionField = _Hm2PortMonitorConditionField_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1, 1, 1),
    _Hm2PortMonitorConditionField_Type()
)
hm2PortMonitorConditionField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionField.setStatus("current")


class _Hm2PortMonitorConditionLinkFlapMode_Type(TruthValue):
    """Custom type hm2PortMonitorConditionLinkFlapMode based on TruthValue"""


_Hm2PortMonitorConditionLinkFlapMode_Object = MibTableColumn
hm2PortMonitorConditionLinkFlapMode = _Hm2PortMonitorConditionLinkFlapMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1, 1, 2),
    _Hm2PortMonitorConditionLinkFlapMode_Type()
)
hm2PortMonitorConditionLinkFlapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionLinkFlapMode.setStatus("current")


class _Hm2PortMonitorConditionCrcFragmentsMode_Type(TruthValue):
    """Custom type hm2PortMonitorConditionCrcFragmentsMode based on TruthValue"""


_Hm2PortMonitorConditionCrcFragmentsMode_Object = MibTableColumn
hm2PortMonitorConditionCrcFragmentsMode = _Hm2PortMonitorConditionCrcFragmentsMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1, 1, 3),
    _Hm2PortMonitorConditionCrcFragmentsMode_Type()
)
hm2PortMonitorConditionCrcFragmentsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionCrcFragmentsMode.setStatus("current")


class _Hm2PortMonitorConditionDuplexMismatchDetectionMode_Type(TruthValue):
    """Custom type hm2PortMonitorConditionDuplexMismatchDetectionMode based on TruthValue"""


_Hm2PortMonitorConditionDuplexMismatchDetectionMode_Object = MibTableColumn
hm2PortMonitorConditionDuplexMismatchDetectionMode = _Hm2PortMonitorConditionDuplexMismatchDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1, 1, 4),
    _Hm2PortMonitorConditionDuplexMismatchDetectionMode_Type()
)
hm2PortMonitorConditionDuplexMismatchDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionDuplexMismatchDetectionMode.setStatus("current")


class _Hm2PortMonitorConditionOverloadDetectionMode_Type(TruthValue):
    """Custom type hm2PortMonitorConditionOverloadDetectionMode based on TruthValue"""


_Hm2PortMonitorConditionOverloadDetectionMode_Object = MibTableColumn
hm2PortMonitorConditionOverloadDetectionMode = _Hm2PortMonitorConditionOverloadDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1, 1, 5),
    _Hm2PortMonitorConditionOverloadDetectionMode_Type()
)
hm2PortMonitorConditionOverloadDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOverloadDetectionMode.setStatus("current")


class _Hm2PortMonitorConditionSpeedDuplexMode_Type(TruthValue):
    """Custom type hm2PortMonitorConditionSpeedDuplexMode based on TruthValue"""


_Hm2PortMonitorConditionSpeedDuplexMode_Object = MibTableColumn
hm2PortMonitorConditionSpeedDuplexMode = _Hm2PortMonitorConditionSpeedDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 1, 1, 6),
    _Hm2PortMonitorConditionSpeedDuplexMode_Type()
)
hm2PortMonitorConditionSpeedDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionSpeedDuplexMode.setStatus("current")
_Hm2PortMonitorConditionLinkFlapGroup_ObjectIdentity = ObjectIdentity
hm2PortMonitorConditionLinkFlapGroup = _Hm2PortMonitorConditionLinkFlapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 2)
)
_Hm2PortMonitorConditionLinkFlapIntfTable_Object = MibTable
hm2PortMonitorConditionLinkFlapIntfTable = _Hm2PortMonitorConditionLinkFlapIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionLinkFlapIntfTable.setStatus("current")
_Hm2PortMonitorConditionLinkFlapIntfEntry_Object = MibTableRow
hm2PortMonitorConditionLinkFlapIntfEntry = _Hm2PortMonitorConditionLinkFlapIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 2, 1, 1)
)
hm2PortMonitorConditionLinkFlapIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionLinkFlapIntfEntry.setStatus("current")


class _Hm2PortMonitorConditionLinkFlapInterval_Type(Integer32):
    """Custom type hm2PortMonitorConditionLinkFlapInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_Hm2PortMonitorConditionLinkFlapInterval_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionLinkFlapInterval_Object = MibTableColumn
hm2PortMonitorConditionLinkFlapInterval = _Hm2PortMonitorConditionLinkFlapInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 2, 1, 1, 1),
    _Hm2PortMonitorConditionLinkFlapInterval_Type()
)
hm2PortMonitorConditionLinkFlapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionLinkFlapInterval.setStatus("current")


class _Hm2PortMonitorConditionLinkFlapCount_Type(Integer32):
    """Custom type hm2PortMonitorConditionLinkFlapCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hm2PortMonitorConditionLinkFlapCount_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionLinkFlapCount_Object = MibTableColumn
hm2PortMonitorConditionLinkFlapCount = _Hm2PortMonitorConditionLinkFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 2, 1, 1, 2),
    _Hm2PortMonitorConditionLinkFlapCount_Type()
)
hm2PortMonitorConditionLinkFlapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionLinkFlapCount.setStatus("current")
_Hm2PortMonitorConditionLinkFlapCountInterval_Type = Integer32
_Hm2PortMonitorConditionLinkFlapCountInterval_Object = MibTableColumn
hm2PortMonitorConditionLinkFlapCountInterval = _Hm2PortMonitorConditionLinkFlapCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 2, 1, 1, 3),
    _Hm2PortMonitorConditionLinkFlapCountInterval_Type()
)
hm2PortMonitorConditionLinkFlapCountInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionLinkFlapCountInterval.setStatus("current")
_Hm2PortMonitorConditionLinkFlapCountTotal_Type = Integer32
_Hm2PortMonitorConditionLinkFlapCountTotal_Object = MibTableColumn
hm2PortMonitorConditionLinkFlapCountTotal = _Hm2PortMonitorConditionLinkFlapCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 2, 1, 1, 4),
    _Hm2PortMonitorConditionLinkFlapCountTotal_Type()
)
hm2PortMonitorConditionLinkFlapCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionLinkFlapCountTotal.setStatus("current")
_Hm2PortMonitorConditionCrcFragmentsGroup_ObjectIdentity = ObjectIdentity
hm2PortMonitorConditionCrcFragmentsGroup = _Hm2PortMonitorConditionCrcFragmentsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 3)
)
_Hm2PortMonitorConditionCrcFragmentsIntfTable_Object = MibTable
hm2PortMonitorConditionCrcFragmentsIntfTable = _Hm2PortMonitorConditionCrcFragmentsIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionCrcFragmentsIntfTable.setStatus("current")
_Hm2PortMonitorConditionCrcFragmentsIntfEntry_Object = MibTableRow
hm2PortMonitorConditionCrcFragmentsIntfEntry = _Hm2PortMonitorConditionCrcFragmentsIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 3, 1, 1)
)
hm2PortMonitorConditionCrcFragmentsIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionCrcFragmentsIntfEntry.setStatus("current")


class _Hm2PortMonitorConditionCrcFragmentsInterval_Type(Integer32):
    """Custom type hm2PortMonitorConditionCrcFragmentsInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 180),
    )


_Hm2PortMonitorConditionCrcFragmentsInterval_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionCrcFragmentsInterval_Object = MibTableColumn
hm2PortMonitorConditionCrcFragmentsInterval = _Hm2PortMonitorConditionCrcFragmentsInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 3, 1, 1, 1),
    _Hm2PortMonitorConditionCrcFragmentsInterval_Type()
)
hm2PortMonitorConditionCrcFragmentsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionCrcFragmentsInterval.setStatus("current")


class _Hm2PortMonitorConditionCrcFragmentsCount_Type(Integer32):
    """Custom type hm2PortMonitorConditionCrcFragmentsCount based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Hm2PortMonitorConditionCrcFragmentsCount_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionCrcFragmentsCount_Object = MibTableColumn
hm2PortMonitorConditionCrcFragmentsCount = _Hm2PortMonitorConditionCrcFragmentsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 3, 1, 1, 2),
    _Hm2PortMonitorConditionCrcFragmentsCount_Type()
)
hm2PortMonitorConditionCrcFragmentsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionCrcFragmentsCount.setStatus("current")
_Hm2PortMonitorConditionCrcFragmentsCountInterval_Type = Integer32
_Hm2PortMonitorConditionCrcFragmentsCountInterval_Object = MibTableColumn
hm2PortMonitorConditionCrcFragmentsCountInterval = _Hm2PortMonitorConditionCrcFragmentsCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 3, 1, 1, 3),
    _Hm2PortMonitorConditionCrcFragmentsCountInterval_Type()
)
hm2PortMonitorConditionCrcFragmentsCountInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionCrcFragmentsCountInterval.setStatus("current")
_Hm2PortMonitorConditionCrcFragmentsCountTotal_Type = Integer32
_Hm2PortMonitorConditionCrcFragmentsCountTotal_Object = MibTableColumn
hm2PortMonitorConditionCrcFragmentsCountTotal = _Hm2PortMonitorConditionCrcFragmentsCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 3, 1, 1, 4),
    _Hm2PortMonitorConditionCrcFragmentsCountTotal_Type()
)
hm2PortMonitorConditionCrcFragmentsCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionCrcFragmentsCountTotal.setStatus("current")
_Hm2PortMonitorConditionOverloadDetectionGroup_ObjectIdentity = ObjectIdentity
hm2PortMonitorConditionOverloadDetectionGroup = _Hm2PortMonitorConditionOverloadDetectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4)
)
_Hm2PortMonitorConditionOvldDetIntfTable_Object = MibTable
hm2PortMonitorConditionOvldDetIntfTable = _Hm2PortMonitorConditionOvldDetIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1)
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetIntfTable.setStatus("current")
_Hm2PortMonitorConditionOvldDetIntfEntry_Object = MibTableRow
hm2PortMonitorConditionOvldDetIntfEntry = _Hm2PortMonitorConditionOvldDetIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1)
)
hm2PortMonitorConditionOvldDetIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetIntfEntry.setStatus("current")


class _Hm2PortMonitorConditionOvldDetTrfcType_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetTrfcType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bc", 2),
          ("bc-mc", 3))
    )


_Hm2PortMonitorConditionOvldDetTrfcType_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionOvldDetTrfcType_Object = MibTableColumn
hm2PortMonitorConditionOvldDetTrfcType = _Hm2PortMonitorConditionOvldDetTrfcType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 1),
    _Hm2PortMonitorConditionOvldDetTrfcType_Type()
)
hm2PortMonitorConditionOvldDetTrfcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetTrfcType.setStatus("current")


class _Hm2PortMonitorConditionOvldDetTholdType_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetTholdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("pps", 1))
    )


_Hm2PortMonitorConditionOvldDetTholdType_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionOvldDetTholdType_Object = MibTableColumn
hm2PortMonitorConditionOvldDetTholdType = _Hm2PortMonitorConditionOvldDetTholdType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 2),
    _Hm2PortMonitorConditionOvldDetTholdType_Type()
)
hm2PortMonitorConditionOvldDetTholdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetTholdType.setStatus("current")


class _Hm2PortMonitorConditionOvldDetLwrTholdVal_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetLwrTholdVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_Hm2PortMonitorConditionOvldDetLwrTholdVal_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionOvldDetLwrTholdVal_Object = MibTableColumn
hm2PortMonitorConditionOvldDetLwrTholdVal = _Hm2PortMonitorConditionOvldDetLwrTholdVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 3),
    _Hm2PortMonitorConditionOvldDetLwrTholdVal_Type()
)
hm2PortMonitorConditionOvldDetLwrTholdVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetLwrTholdVal.setStatus("current")


class _Hm2PortMonitorConditionOvldDetUprTholdVal_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetUprTholdVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_Hm2PortMonitorConditionOvldDetUprTholdVal_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionOvldDetUprTholdVal_Object = MibTableColumn
hm2PortMonitorConditionOvldDetUprTholdVal = _Hm2PortMonitorConditionOvldDetUprTholdVal_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 4),
    _Hm2PortMonitorConditionOvldDetUprTholdVal_Type()
)
hm2PortMonitorConditionOvldDetUprTholdVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetUprTholdVal.setStatus("current")


class _Hm2PortMonitorConditionOvldDetIntvl_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetIntvl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hm2PortMonitorConditionOvldDetIntvl_Type.__name__ = "Integer32"
_Hm2PortMonitorConditionOvldDetIntvl_Object = MibTableColumn
hm2PortMonitorConditionOvldDetIntvl = _Hm2PortMonitorConditionOvldDetIntvl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 5),
    _Hm2PortMonitorConditionOvldDetIntvl_Type()
)
hm2PortMonitorConditionOvldDetIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetIntvl.setStatus("current")


class _Hm2PortMonitorConditionOvldDetPkgCntAll_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetPkgCntAll based on Integer32"""
    defaultValue = 0


_Hm2PortMonitorConditionOvldDetPkgCntAll_Object = MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntAll = _Hm2PortMonitorConditionOvldDetPkgCntAll_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 6),
    _Hm2PortMonitorConditionOvldDetPkgCntAll_Type()
)
hm2PortMonitorConditionOvldDetPkgCntAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetPkgCntAll.setStatus("current")


class _Hm2PortMonitorConditionOvldDetPkgCntBC_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetPkgCntBC based on Integer32"""
    defaultValue = 0


_Hm2PortMonitorConditionOvldDetPkgCntBC_Object = MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntBC = _Hm2PortMonitorConditionOvldDetPkgCntBC_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 7),
    _Hm2PortMonitorConditionOvldDetPkgCntBC_Type()
)
hm2PortMonitorConditionOvldDetPkgCntBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetPkgCntBC.setStatus("current")


class _Hm2PortMonitorConditionOvldDetPkgCntMC_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetPkgCntMC based on Integer32"""
    defaultValue = 0


_Hm2PortMonitorConditionOvldDetPkgCntMC_Object = MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntMC = _Hm2PortMonitorConditionOvldDetPkgCntMC_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 8),
    _Hm2PortMonitorConditionOvldDetPkgCntMC_Type()
)
hm2PortMonitorConditionOvldDetPkgCntMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetPkgCntMC.setStatus("current")


class _Hm2PortMonitorConditionOvldDetPkgCntKbit_Type(Integer32):
    """Custom type hm2PortMonitorConditionOvldDetPkgCntKbit based on Integer32"""
    defaultValue = 0


_Hm2PortMonitorConditionOvldDetPkgCntKbit_Object = MibTableColumn
hm2PortMonitorConditionOvldDetPkgCntKbit = _Hm2PortMonitorConditionOvldDetPkgCntKbit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 4, 1, 1, 9),
    _Hm2PortMonitorConditionOvldDetPkgCntKbit_Type()
)
hm2PortMonitorConditionOvldDetPkgCntKbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionOvldDetPkgCntKbit.setStatus("current")
_Hm2PortMonitorConditionSpeedDuplexGroup_ObjectIdentity = ObjectIdentity
hm2PortMonitorConditionSpeedDuplexGroup = _Hm2PortMonitorConditionSpeedDuplexGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 5)
)
_Hm2PortMonitorConditionSpeedDuplexTable_Object = MibTable
hm2PortMonitorConditionSpeedDuplexTable = _Hm2PortMonitorConditionSpeedDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 5, 1)
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionSpeedDuplexTable.setStatus("current")
_Hm2PortMonitorConditionSpeedDuplexEntry_Object = MibTableRow
hm2PortMonitorConditionSpeedDuplexEntry = _Hm2PortMonitorConditionSpeedDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 5, 1, 1)
)
hm2PortMonitorConditionSpeedDuplexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2PortMonitorConditionSpeedDuplexEntry.setStatus("current")


class _Hm2PortMonitorConditionSpeedDuplexValue_Type(Bits):
    """Custom type hm2PortMonitorConditionSpeedDuplexValue based on Bits"""
    defaultBinValue = "1111111"

    namedValues = NamedValues(
        *(("fdx-10", 1),
          ("fdx-100", 3),
          ("fdx-1000", 5),
          ("fdx-2500", 6),
          ("hdx-10", 0),
          ("hdx-100", 2),
          ("hdx-1000", 4))
    )

_Hm2PortMonitorConditionSpeedDuplexValue_Type.__name__ = "Bits"
_Hm2PortMonitorConditionSpeedDuplexValue_Object = MibTableColumn
hm2PortMonitorConditionSpeedDuplexValue = _Hm2PortMonitorConditionSpeedDuplexValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 3, 5, 1, 1, 1),
    _Hm2PortMonitorConditionSpeedDuplexValue_Type()
)
hm2PortMonitorConditionSpeedDuplexValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PortMonitorConditionSpeedDuplexValue.setStatus("current")
_Hm2KbpsUnitTrafficTypeInvalid_ObjectIdentity = ObjectIdentity
hm2KbpsUnitTrafficTypeInvalid = _Hm2KbpsUnitTrafficTypeInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 7, 4)
)
if mibBuilder.loadTexts:
    hm2KbpsUnitTrafficTypeInvalid.setStatus("current")
_Hm2DiagResourcesGroup_ObjectIdentity = ObjectIdentity
hm2DiagResourcesGroup = _Hm2DiagResourcesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8)
)


class _Hm2DiagEnableMeasurement_Type(HmEnabledStatus):
    """Custom type hm2DiagEnableMeasurement based on HmEnabledStatus"""


_Hm2DiagEnableMeasurement_Object = MibScalar
hm2DiagEnableMeasurement = _Hm2DiagEnableMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 1),
    _Hm2DiagEnableMeasurement_Type()
)
hm2DiagEnableMeasurement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DiagEnableMeasurement.setStatus("current")
_Hm2DiagCpuResourcesGroup_ObjectIdentity = ObjectIdentity
hm2DiagCpuResourcesGroup = _Hm2DiagCpuResourcesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 10)
)


class _Hm2DiagCpuUtilization_Type(Integer32):
    """Custom type hm2DiagCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hm2DiagCpuUtilization_Type.__name__ = "Integer32"
_Hm2DiagCpuUtilization_Object = MibScalar
hm2DiagCpuUtilization = _Hm2DiagCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 10, 1),
    _Hm2DiagCpuUtilization_Type()
)
hm2DiagCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagCpuUtilization.setUnits("percent")


class _Hm2DiagCpuAverageUtilization_Type(Integer32):
    """Custom type hm2DiagCpuAverageUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hm2DiagCpuAverageUtilization_Type.__name__ = "Integer32"
_Hm2DiagCpuAverageUtilization_Object = MibScalar
hm2DiagCpuAverageUtilization = _Hm2DiagCpuAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 10, 2),
    _Hm2DiagCpuAverageUtilization_Type()
)
hm2DiagCpuAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCpuAverageUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagCpuAverageUtilization.setUnits("percent")


class _Hm2DiagCpuRunningProcesses_Type(Integer32):
    """Custom type hm2DiagCpuRunningProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_Hm2DiagCpuRunningProcesses_Type.__name__ = "Integer32"
_Hm2DiagCpuRunningProcesses_Object = MibScalar
hm2DiagCpuRunningProcesses = _Hm2DiagCpuRunningProcesses_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 10, 3),
    _Hm2DiagCpuRunningProcesses_Type()
)
hm2DiagCpuRunningProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCpuRunningProcesses.setStatus("current")


class _Hm2DiagCpuMaxRunningProcesses_Type(Integer32):
    """Custom type hm2DiagCpuMaxRunningProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_Hm2DiagCpuMaxRunningProcesses_Type.__name__ = "Integer32"
_Hm2DiagCpuMaxRunningProcesses_Object = MibScalar
hm2DiagCpuMaxRunningProcesses = _Hm2DiagCpuMaxRunningProcesses_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 10, 4),
    _Hm2DiagCpuMaxRunningProcesses_Type()
)
hm2DiagCpuMaxRunningProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagCpuMaxRunningProcesses.setStatus("current")
_Hm2DiagMemoryResourcesGroup_ObjectIdentity = ObjectIdentity
hm2DiagMemoryResourcesGroup = _Hm2DiagMemoryResourcesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11)
)


class _Hm2DiagMemoryRamAllocated_Type(Integer32):
    """Custom type hm2DiagMemoryRamAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryRamAllocated_Type.__name__ = "Integer32"
_Hm2DiagMemoryRamAllocated_Object = MibScalar
hm2DiagMemoryRamAllocated = _Hm2DiagMemoryRamAllocated_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 1),
    _Hm2DiagMemoryRamAllocated_Type()
)
hm2DiagMemoryRamAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamAllocated.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamAllocated.setUnits("kBytes")


class _Hm2DiagMemoryRamFree_Type(Integer32):
    """Custom type hm2DiagMemoryRamFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryRamFree_Type.__name__ = "Integer32"
_Hm2DiagMemoryRamFree_Object = MibScalar
hm2DiagMemoryRamFree = _Hm2DiagMemoryRamFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 2),
    _Hm2DiagMemoryRamFree_Type()
)
hm2DiagMemoryRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamFree.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamFree.setUnits("kBytes")


class _Hm2DiagMemoryRamAllocatedAverage_Type(Integer32):
    """Custom type hm2DiagMemoryRamAllocatedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryRamAllocatedAverage_Type.__name__ = "Integer32"
_Hm2DiagMemoryRamAllocatedAverage_Object = MibScalar
hm2DiagMemoryRamAllocatedAverage = _Hm2DiagMemoryRamAllocatedAverage_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 3),
    _Hm2DiagMemoryRamAllocatedAverage_Type()
)
hm2DiagMemoryRamAllocatedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamAllocatedAverage.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamAllocatedAverage.setUnits("kBytes")


class _Hm2DiagMemoryRamFreeAverage_Type(Integer32):
    """Custom type hm2DiagMemoryRamFreeAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryRamFreeAverage_Type.__name__ = "Integer32"
_Hm2DiagMemoryRamFreeAverage_Object = MibScalar
hm2DiagMemoryRamFreeAverage = _Hm2DiagMemoryRamFreeAverage_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 4),
    _Hm2DiagMemoryRamFreeAverage_Type()
)
hm2DiagMemoryRamFreeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamFreeAverage.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryRamFreeAverage.setUnits("kBytes")


class _Hm2DiagMemoryRawFlashMainAllocated_Type(Integer32):
    """Custom type hm2DiagMemoryRawFlashMainAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryRawFlashMainAllocated_Type.__name__ = "Integer32"
_Hm2DiagMemoryRawFlashMainAllocated_Object = MibScalar
hm2DiagMemoryRawFlashMainAllocated = _Hm2DiagMemoryRawFlashMainAllocated_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 10),
    _Hm2DiagMemoryRawFlashMainAllocated_Type()
)
hm2DiagMemoryRawFlashMainAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryRawFlashMainAllocated.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryRawFlashMainAllocated.setUnits("kBytes")


class _Hm2DiagMemoryRawFlashMainFree_Type(Integer32):
    """Custom type hm2DiagMemoryRawFlashMainFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryRawFlashMainFree_Type.__name__ = "Integer32"
_Hm2DiagMemoryRawFlashMainFree_Object = MibScalar
hm2DiagMemoryRawFlashMainFree = _Hm2DiagMemoryRawFlashMainFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 11),
    _Hm2DiagMemoryRawFlashMainFree_Type()
)
hm2DiagMemoryRawFlashMainFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryRawFlashMainFree.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryRawFlashMainFree.setUnits("kBytes")


class _Hm2DiagMemoryFlashFileSystemAllocated_Type(Integer32):
    """Custom type hm2DiagMemoryFlashFileSystemAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryFlashFileSystemAllocated_Type.__name__ = "Integer32"
_Hm2DiagMemoryFlashFileSystemAllocated_Object = MibScalar
hm2DiagMemoryFlashFileSystemAllocated = _Hm2DiagMemoryFlashFileSystemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 12),
    _Hm2DiagMemoryFlashFileSystemAllocated_Type()
)
hm2DiagMemoryFlashFileSystemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryFlashFileSystemAllocated.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryFlashFileSystemAllocated.setUnits("kBytes")


class _Hm2DiagMemoryFlashFileSystemFree_Type(Integer32):
    """Custom type hm2DiagMemoryFlashFileSystemFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2DiagMemoryFlashFileSystemFree_Type.__name__ = "Integer32"
_Hm2DiagMemoryFlashFileSystemFree_Object = MibScalar
hm2DiagMemoryFlashFileSystemFree = _Hm2DiagMemoryFlashFileSystemFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 11, 13),
    _Hm2DiagMemoryFlashFileSystemFree_Type()
)
hm2DiagMemoryFlashFileSystemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagMemoryFlashFileSystemFree.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagMemoryFlashFileSystemFree.setUnits("kBytes")
_Hm2DiagNetworkResourcesGroup_ObjectIdentity = ObjectIdentity
hm2DiagNetworkResourcesGroup = _Hm2DiagNetworkResourcesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 12)
)


class _Hm2DiagNetworkCpuIfUtilization_Type(Integer32):
    """Custom type hm2DiagNetworkCpuIfUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hm2DiagNetworkCpuIfUtilization_Type.__name__ = "Integer32"
_Hm2DiagNetworkCpuIfUtilization_Object = MibScalar
hm2DiagNetworkCpuIfUtilization = _Hm2DiagNetworkCpuIfUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 12, 1),
    _Hm2DiagNetworkCpuIfUtilization_Type()
)
hm2DiagNetworkCpuIfUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagNetworkCpuIfUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagNetworkCpuIfUtilization.setUnits("precent")


class _Hm2DiagNetworkCpuIfAverageUtilization_Type(Integer32):
    """Custom type hm2DiagNetworkCpuIfAverageUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hm2DiagNetworkCpuIfAverageUtilization_Type.__name__ = "Integer32"
_Hm2DiagNetworkCpuIfAverageUtilization_Object = MibScalar
hm2DiagNetworkCpuIfAverageUtilization = _Hm2DiagNetworkCpuIfAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 1, 8, 12, 2),
    _Hm2DiagNetworkCpuIfAverageUtilization_Type()
)
hm2DiagNetworkCpuIfAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DiagNetworkCpuIfAverageUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hm2DiagNetworkCpuIfAverageUtilization.setUnits("precent")
_Hm2DiagnosticSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2DiagnosticSNMPExtensionGroup = _Hm2DiagnosticSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 3)
)
_Hm2PortMonitorSpeedDuplexErrorReturn_ObjectIdentity = ObjectIdentity
hm2PortMonitorSpeedDuplexErrorReturn = _Hm2PortMonitorSpeedDuplexErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 3, 1)
)
if mibBuilder.loadTexts:
    hm2PortMonitorSpeedDuplexErrorReturn.setStatus("current")
_Hm2PortMonitorCndOvldDetInconsistenTholdVal_ObjectIdentity = ObjectIdentity
hm2PortMonitorCndOvldDetInconsistenTholdVal = _Hm2PortMonitorCndOvldDetInconsistenTholdVal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 3, 2)
)
if mibBuilder.loadTexts:
    hm2PortMonitorCndOvldDetInconsistenTholdVal.setStatus("current")

# Managed Objects groups


# Notification objects

hm2SigConStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 0, 1)
)
hm2SigConStateChangeTrap.setObjects(
      *(("HM2-DIAGNOSTIC-MIB", "hm2SigConID"),
        ("HM2-DIAGNOSTIC-MIB", "hm2SigConOperState"),
        ("HM2-DIAGNOSTIC-MIB", "hm2SigConTrapCause"),
        ("HM2-DIAGNOSTIC-MIB", "hm2SigConTrapCauseIndex"))
)
if mibBuilder.loadTexts:
    hm2SigConStateChangeTrap.setStatus(
        "current"
    )

hm2DevMonStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 0, 2)
)
hm2DevMonStateChangeTrap.setObjects(
      *(("HM2-DIAGNOSTIC-MIB", "hm2DevMonID"),
        ("HM2-DIAGNOSTIC-MIB", "hm2DevMonOperState"),
        ("HM2-DIAGNOSTIC-MIB", "hm2DevMonTrapCause"),
        ("HM2-DIAGNOSTIC-MIB", "hm2DevMonTrapCauseIndex"))
)
if mibBuilder.loadTexts:
    hm2DevMonStateChangeTrap.setStatus(
        "current"
    )

hm2DevSecStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 0, 3)
)
hm2DevSecStateChangeTrap.setObjects(
      *(("HM2-DIAGNOSTIC-MIB", "hm2DevSecOperState"),
        ("HM2-DIAGNOSTIC-MIB", "hm2DevSecTrapCause"),
        ("HM2-DIAGNOSTIC-MIB", "hm2DevSecTrapCauseIndex"))
)
if mibBuilder.loadTexts:
    hm2DevSecStateChangeTrap.setStatus(
        "current"
    )

hm2DiagSelftestActionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 0, 4)
)
hm2DiagSelftestActionTrap.setObjects(
    ("HM2-DIAGNOSTIC-MIB", "hm2DiagSelftestActionCause")
)
if mibBuilder.loadTexts:
    hm2DiagSelftestActionTrap.setStatus(
        "current"
    )

hm2DiagIfaceUtilizationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 0, 5)
)
hm2DiagIfaceUtilizationTrap.setObjects(
      *(("HM2-DIAGNOSTIC-MIB", "hm2DiagIfaceUtilization"),
        ("HM2-DIAGNOSTIC-MIB", "hm2DiagIfaceUtilizationAlarmCondition"))
)
if mibBuilder.loadTexts:
    hm2DiagIfaceUtilizationTrap.setStatus(
        "current"
    )

hm2PortMonitorPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 22, 0, 6)
)
hm2PortMonitorPortTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HM2-DIAGNOSTIC-MIB", "hm2PortMonitorConditionField"))
)
if mibBuilder.loadTexts:
    hm2PortMonitorPortTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-DIAGNOSTIC-MIB",
    **{"Hm2LedType": Hm2LedType,
       "Hm2LedStatus": Hm2LedStatus,
       "hm2DiagnosticMib": hm2DiagnosticMib,
       "hm2DiagnosticMibNotifications": hm2DiagnosticMibNotifications,
       "hm2SigConStateChangeTrap": hm2SigConStateChangeTrap,
       "hm2DevMonStateChangeTrap": hm2DevMonStateChangeTrap,
       "hm2DevSecStateChangeTrap": hm2DevSecStateChangeTrap,
       "hm2DiagSelftestActionTrap": hm2DiagSelftestActionTrap,
       "hm2DiagIfaceUtilizationTrap": hm2DiagIfaceUtilizationTrap,
       "hm2PortMonitorPortTrap": hm2PortMonitorPortTrap,
       "hm2DiagnosticMibObjects": hm2DiagnosticMibObjects,
       "hm2DiagSelftestGroup": hm2DiagSelftestGroup,
       "hm2DiagSelftestRAM": hm2DiagSelftestRAM,
       "hm2DiagSelftestBootTime": hm2DiagSelftestBootTime,
       "hm2DiagSelftestActionTable": hm2DiagSelftestActionTable,
       "hm2DiagSelftestActionEntry": hm2DiagSelftestActionEntry,
       "hm2DiagSelftestActionCause": hm2DiagSelftestActionCause,
       "hm2DiagSelftestAction": hm2DiagSelftestAction,
       "hm2DiagBootGroup": hm2DiagBootGroup,
       "hm2BootSystemMonitor": hm2BootSystemMonitor,
       "hm2BootDefaultConfigOnError": hm2BootDefaultConfigOnError,
       "hm2BootConfigPushButton": hm2BootConfigPushButton,
       "hm2DiagDeviceMonitorGroup": hm2DiagDeviceMonitorGroup,
       "hm2SignalContactGroup": hm2SignalContactGroup,
       "hm2SigConCommonTable": hm2SigConCommonTable,
       "hm2SigConCommonEntry": hm2SigConCommonEntry,
       "hm2SigConID": hm2SigConID,
       "hm2SigConTrapEnable": hm2SigConTrapEnable,
       "hm2SigConTrapCause": hm2SigConTrapCause,
       "hm2SigConTrapCauseIndex": hm2SigConTrapCauseIndex,
       "hm2SigConMode": hm2SigConMode,
       "hm2SigConOperState": hm2SigConOperState,
       "hm2SigConOperTimeStamp": hm2SigConOperTimeStamp,
       "hm2SigConManualActivate": hm2SigConManualActivate,
       "hm2SigConSenseLinkFailure": hm2SigConSenseLinkFailure,
       "hm2SigConSenseTemperature": hm2SigConSenseTemperature,
       "hm2SigConSenseFan": hm2SigConSenseFan,
       "hm2SigConSenseModuleRemoval": hm2SigConSenseModuleRemoval,
       "hm2SigConSenseExtNvmRemoval": hm2SigConSenseExtNvmRemoval,
       "hm2SigConSenseExtNvmNotInSync": hm2SigConSenseExtNvmNotInSync,
       "hm2SigConSenseRingRedundancy": hm2SigConSenseRingRedundancy,
       "hm2SigConPSTable": hm2SigConPSTable,
       "hm2SigConPSEntry": hm2SigConPSEntry,
       "hm2SigConSensePSState": hm2SigConSensePSState,
       "hm2SigConInterfaceTable": hm2SigConInterfaceTable,
       "hm2SigConInterfaceEntry": hm2SigConInterfaceEntry,
       "hm2SigConSenseIfLinkAlarm": hm2SigConSenseIfLinkAlarm,
       "hm2SigConModuleTable": hm2SigConModuleTable,
       "hm2SigConModuleEntry": hm2SigConModuleEntry,
       "hm2SigConModID": hm2SigConModID,
       "hm2SigConSenseModule": hm2SigConSenseModule,
       "hm2SigConStatusTable": hm2SigConStatusTable,
       "hm2SigConStatusEntry": hm2SigConStatusEntry,
       "hm2SigConStatusIndex": hm2SigConStatusIndex,
       "hm2SigConStatusTimeStamp": hm2SigConStatusTimeStamp,
       "hm2SigConStatusTrapCause": hm2SigConStatusTrapCause,
       "hm2SigConStatusTrapCauseIndex": hm2SigConStatusTrapCauseIndex,
       "hm2DeviceMonitorGroup": hm2DeviceMonitorGroup,
       "hm2DevMonCommonTable": hm2DevMonCommonTable,
       "hm2DevMonCommonEntry": hm2DevMonCommonEntry,
       "hm2DevMonID": hm2DevMonID,
       "hm2DevMonTrapEnable": hm2DevMonTrapEnable,
       "hm2DevMonTrapCause": hm2DevMonTrapCause,
       "hm2DevMonTrapCauseIndex": hm2DevMonTrapCauseIndex,
       "hm2DevMonOperState": hm2DevMonOperState,
       "hm2DevMonOperTimeStamp": hm2DevMonOperTimeStamp,
       "hm2DevMonSenseLinkFailure": hm2DevMonSenseLinkFailure,
       "hm2DevMonSenseTemperature": hm2DevMonSenseTemperature,
       "hm2DevMonSenseFan": hm2DevMonSenseFan,
       "hm2DevMonSenseModuleRemoval": hm2DevMonSenseModuleRemoval,
       "hm2DevMonSenseExtNvmRemoval": hm2DevMonSenseExtNvmRemoval,
       "hm2DevMonSenseExtNvmNotInSync": hm2DevMonSenseExtNvmNotInSync,
       "hm2DevMonSenseRingRedundancy": hm2DevMonSenseRingRedundancy,
       "hm2DevMonPSTable": hm2DevMonPSTable,
       "hm2DevMonPSEntry": hm2DevMonPSEntry,
       "hm2DevMonSensePSState": hm2DevMonSensePSState,
       "hm2DevMonInterfaceTable": hm2DevMonInterfaceTable,
       "hm2DevMonInterfaceEntry": hm2DevMonInterfaceEntry,
       "hm2DevMonSenseIfLinkAlarm": hm2DevMonSenseIfLinkAlarm,
       "hm2DevMonModuleTable": hm2DevMonModuleTable,
       "hm2DevMonModuleEntry": hm2DevMonModuleEntry,
       "hm2DevMonModID": hm2DevMonModID,
       "hm2DevMonSenseModule": hm2DevMonSenseModule,
       "hm2DevMonStatusTable": hm2DevMonStatusTable,
       "hm2DevMonStatusEntry": hm2DevMonStatusEntry,
       "hm2DevMonStatusIndex": hm2DevMonStatusIndex,
       "hm2DevMonStatusTimeStamp": hm2DevMonStatusTimeStamp,
       "hm2DevMonStatusTrapCause": hm2DevMonStatusTrapCause,
       "hm2DevMonStatusTrapCauseIndex": hm2DevMonStatusTrapCauseIndex,
       "hm2DeviceSecurityGroup": hm2DeviceSecurityGroup,
       "hm2DevSecConfigGroup": hm2DevSecConfigGroup,
       "hm2DevSecTrapEnable": hm2DevSecTrapEnable,
       "hm2DevSecTrapCause": hm2DevSecTrapCause,
       "hm2DevSecTrapCauseIndex": hm2DevSecTrapCauseIndex,
       "hm2DevSecOperState": hm2DevSecOperState,
       "hm2DevSecOperTimeStamp": hm2DevSecOperTimeStamp,
       "hm2DevSecSensePasswordChange": hm2DevSecSensePasswordChange,
       "hm2DevSecSensePasswordMinLength": hm2DevSecSensePasswordMinLength,
       "hm2DevSecSensePasswordStrengthNotConfigured": hm2DevSecSensePasswordStrengthNotConfigured,
       "hm2DevSecSenseBypassPasswordStrength": hm2DevSecSenseBypassPasswordStrength,
       "hm2DevSecSenseTelnetEnabled": hm2DevSecSenseTelnetEnabled,
       "hm2DevSecSenseHttpEnabled": hm2DevSecSenseHttpEnabled,
       "hm2DevSecSenseSnmpUnsecure": hm2DevSecSenseSnmpUnsecure,
       "hm2DevSecSenseSysmonEnabled": hm2DevSecSenseSysmonEnabled,
       "hm2DevSecSenseExtNvmUpdateEnabled": hm2DevSecSenseExtNvmUpdateEnabled,
       "hm2DevSecSenseNoLinkEnabled": hm2DevSecSenseNoLinkEnabled,
       "hm2DevSecSenseHiDiscoveryEnabled": hm2DevSecSenseHiDiscoveryEnabled,
       "hm2DevSecSenseExtNvmConfigLoadUnsecure": hm2DevSecSenseExtNvmConfigLoadUnsecure,
       "hm2DevSecSenseIec61850MmsEnabled": hm2DevSecSenseIec61850MmsEnabled,
       "hm2DevSecSenseHttpsCertificateWarning": hm2DevSecSenseHttpsCertificateWarning,
       "hm2DevSecSenseModbusTcpEnabled": hm2DevSecSenseModbusTcpEnabled,
       "hm2DevSecSenseEtherNetIpEnabled": hm2DevSecSenseEtherNetIpEnabled,
       "hm2DevSecSenseProfinetIOEnabled": hm2DevSecSenseProfinetIOEnabled,
       "hm2DevSecInterfaceTable": hm2DevSecInterfaceTable,
       "hm2DevSecInterfaceEntry": hm2DevSecInterfaceEntry,
       "hm2DevSecSenseIfNoLink": hm2DevSecSenseIfNoLink,
       "hm2DevSecStatusTable": hm2DevSecStatusTable,
       "hm2DevSecStatusEntry": hm2DevSecStatusEntry,
       "hm2DevSecStatusIndex": hm2DevSecStatusIndex,
       "hm2DevSecStatusTimeStamp": hm2DevSecStatusTimeStamp,
       "hm2DevSecStatusTrapCause": hm2DevSecStatusTrapCause,
       "hm2DevSecStatusTrapCauseIndex": hm2DevSecStatusTrapCauseIndex,
       "hm2DiagLedGroup": hm2DiagLedGroup,
       "hm2LedGlobalTable": hm2LedGlobalTable,
       "hm2LedGlobalEntry": hm2LedGlobalEntry,
       "hm2LedGlobalLedType": hm2LedGlobalLedType,
       "hm2LedGlobalStatus": hm2LedGlobalStatus,
       "hm2LedPortTable": hm2LedPortTable,
       "hm2LedPortEntry": hm2LedPortEntry,
       "hm2LedPortStatus": hm2LedPortStatus,
       "hm2LedPortPoeStatus": hm2LedPortPoeStatus,
       "hm2LedPortSignaling": hm2LedPortSignaling,
       "hm2LedControlGroup": hm2LedControlGroup,
       "hm2LedPortMode": hm2LedPortMode,
       "hm2DiagIfaceUtilizationGroup": hm2DiagIfaceUtilizationGroup,
       "hm2DiagIfaceUtilizationTable": hm2DiagIfaceUtilizationTable,
       "hm2DiagIfaceUtilizationEntry": hm2DiagIfaceUtilizationEntry,
       "hm2DiagIfaceUtilization": hm2DiagIfaceUtilization,
       "hm2DiagIfaceUtilizationControlInterval": hm2DiagIfaceUtilizationControlInterval,
       "hm2DiagIfaceUtilizationAlarmLowerThreshold": hm2DiagIfaceUtilizationAlarmLowerThreshold,
       "hm2DiagIfaceUtilizationAlarmUpperThreshold": hm2DiagIfaceUtilizationAlarmUpperThreshold,
       "hm2DiagIfaceUtilizationAlarmCondition": hm2DiagIfaceUtilizationAlarmCondition,
       "hm2DiagCableTesterGroup": hm2DiagCableTesterGroup,
       "hm2DiagCableTesterStatus": hm2DiagCableTesterStatus,
       "hm2DiagCableTesterIfIndex": hm2DiagCableTesterIfIndex,
       "hm2DiagCableTesterCableTable": hm2DiagCableTesterCableTable,
       "hm2DiagCableTesterCableEntry": hm2DiagCableTesterCableEntry,
       "hm2DiagCableTesterCablePair": hm2DiagCableTesterCablePair,
       "hm2DiagCableTesterCableStatus": hm2DiagCableTesterCableStatus,
       "hm2DiagCableTesterCableMinimumLength": hm2DiagCableTesterCableMinimumLength,
       "hm2DiagCableTesterCableMaximumLength": hm2DiagCableTesterCableMaximumLength,
       "hm2DiagCableTesterCableFailureLocation": hm2DiagCableTesterCableFailureLocation,
       "hm2PortMonitorGroup": hm2PortMonitorGroup,
       "hm2PortMonitorAdminMode": hm2PortMonitorAdminMode,
       "hm2PortMonitorIntfTable": hm2PortMonitorIntfTable,
       "hm2PortMonitorIntfEntry": hm2PortMonitorIntfEntry,
       "hm2PortMonitorIntfReset": hm2PortMonitorIntfReset,
       "hm2PortMonitorIntfAction": hm2PortMonitorIntfAction,
       "hm2PortMonitorConditionGroup": hm2PortMonitorConditionGroup,
       "hm2PortMonitorConditionIntfTable": hm2PortMonitorConditionIntfTable,
       "hm2PortMonitorConditionIntfEntry": hm2PortMonitorConditionIntfEntry,
       "hm2PortMonitorConditionField": hm2PortMonitorConditionField,
       "hm2PortMonitorConditionLinkFlapMode": hm2PortMonitorConditionLinkFlapMode,
       "hm2PortMonitorConditionCrcFragmentsMode": hm2PortMonitorConditionCrcFragmentsMode,
       "hm2PortMonitorConditionDuplexMismatchDetectionMode": hm2PortMonitorConditionDuplexMismatchDetectionMode,
       "hm2PortMonitorConditionOverloadDetectionMode": hm2PortMonitorConditionOverloadDetectionMode,
       "hm2PortMonitorConditionSpeedDuplexMode": hm2PortMonitorConditionSpeedDuplexMode,
       "hm2PortMonitorConditionLinkFlapGroup": hm2PortMonitorConditionLinkFlapGroup,
       "hm2PortMonitorConditionLinkFlapIntfTable": hm2PortMonitorConditionLinkFlapIntfTable,
       "hm2PortMonitorConditionLinkFlapIntfEntry": hm2PortMonitorConditionLinkFlapIntfEntry,
       "hm2PortMonitorConditionLinkFlapInterval": hm2PortMonitorConditionLinkFlapInterval,
       "hm2PortMonitorConditionLinkFlapCount": hm2PortMonitorConditionLinkFlapCount,
       "hm2PortMonitorConditionLinkFlapCountInterval": hm2PortMonitorConditionLinkFlapCountInterval,
       "hm2PortMonitorConditionLinkFlapCountTotal": hm2PortMonitorConditionLinkFlapCountTotal,
       "hm2PortMonitorConditionCrcFragmentsGroup": hm2PortMonitorConditionCrcFragmentsGroup,
       "hm2PortMonitorConditionCrcFragmentsIntfTable": hm2PortMonitorConditionCrcFragmentsIntfTable,
       "hm2PortMonitorConditionCrcFragmentsIntfEntry": hm2PortMonitorConditionCrcFragmentsIntfEntry,
       "hm2PortMonitorConditionCrcFragmentsInterval": hm2PortMonitorConditionCrcFragmentsInterval,
       "hm2PortMonitorConditionCrcFragmentsCount": hm2PortMonitorConditionCrcFragmentsCount,
       "hm2PortMonitorConditionCrcFragmentsCountInterval": hm2PortMonitorConditionCrcFragmentsCountInterval,
       "hm2PortMonitorConditionCrcFragmentsCountTotal": hm2PortMonitorConditionCrcFragmentsCountTotal,
       "hm2PortMonitorConditionOverloadDetectionGroup": hm2PortMonitorConditionOverloadDetectionGroup,
       "hm2PortMonitorConditionOvldDetIntfTable": hm2PortMonitorConditionOvldDetIntfTable,
       "hm2PortMonitorConditionOvldDetIntfEntry": hm2PortMonitorConditionOvldDetIntfEntry,
       "hm2PortMonitorConditionOvldDetTrfcType": hm2PortMonitorConditionOvldDetTrfcType,
       "hm2PortMonitorConditionOvldDetTholdType": hm2PortMonitorConditionOvldDetTholdType,
       "hm2PortMonitorConditionOvldDetLwrTholdVal": hm2PortMonitorConditionOvldDetLwrTholdVal,
       "hm2PortMonitorConditionOvldDetUprTholdVal": hm2PortMonitorConditionOvldDetUprTholdVal,
       "hm2PortMonitorConditionOvldDetIntvl": hm2PortMonitorConditionOvldDetIntvl,
       "hm2PortMonitorConditionOvldDetPkgCntAll": hm2PortMonitorConditionOvldDetPkgCntAll,
       "hm2PortMonitorConditionOvldDetPkgCntBC": hm2PortMonitorConditionOvldDetPkgCntBC,
       "hm2PortMonitorConditionOvldDetPkgCntMC": hm2PortMonitorConditionOvldDetPkgCntMC,
       "hm2PortMonitorConditionOvldDetPkgCntKbit": hm2PortMonitorConditionOvldDetPkgCntKbit,
       "hm2PortMonitorConditionSpeedDuplexGroup": hm2PortMonitorConditionSpeedDuplexGroup,
       "hm2PortMonitorConditionSpeedDuplexTable": hm2PortMonitorConditionSpeedDuplexTable,
       "hm2PortMonitorConditionSpeedDuplexEntry": hm2PortMonitorConditionSpeedDuplexEntry,
       "hm2PortMonitorConditionSpeedDuplexValue": hm2PortMonitorConditionSpeedDuplexValue,
       "hm2KbpsUnitTrafficTypeInvalid": hm2KbpsUnitTrafficTypeInvalid,
       "hm2DiagResourcesGroup": hm2DiagResourcesGroup,
       "hm2DiagEnableMeasurement": hm2DiagEnableMeasurement,
       "hm2DiagCpuResourcesGroup": hm2DiagCpuResourcesGroup,
       "hm2DiagCpuUtilization": hm2DiagCpuUtilization,
       "hm2DiagCpuAverageUtilization": hm2DiagCpuAverageUtilization,
       "hm2DiagCpuRunningProcesses": hm2DiagCpuRunningProcesses,
       "hm2DiagCpuMaxRunningProcesses": hm2DiagCpuMaxRunningProcesses,
       "hm2DiagMemoryResourcesGroup": hm2DiagMemoryResourcesGroup,
       "hm2DiagMemoryRamAllocated": hm2DiagMemoryRamAllocated,
       "hm2DiagMemoryRamFree": hm2DiagMemoryRamFree,
       "hm2DiagMemoryRamAllocatedAverage": hm2DiagMemoryRamAllocatedAverage,
       "hm2DiagMemoryRamFreeAverage": hm2DiagMemoryRamFreeAverage,
       "hm2DiagMemoryRawFlashMainAllocated": hm2DiagMemoryRawFlashMainAllocated,
       "hm2DiagMemoryRawFlashMainFree": hm2DiagMemoryRawFlashMainFree,
       "hm2DiagMemoryFlashFileSystemAllocated": hm2DiagMemoryFlashFileSystemAllocated,
       "hm2DiagMemoryFlashFileSystemFree": hm2DiagMemoryFlashFileSystemFree,
       "hm2DiagNetworkResourcesGroup": hm2DiagNetworkResourcesGroup,
       "hm2DiagNetworkCpuIfUtilization": hm2DiagNetworkCpuIfUtilization,
       "hm2DiagNetworkCpuIfAverageUtilization": hm2DiagNetworkCpuIfAverageUtilization,
       "hm2DiagnosticSNMPExtensionGroup": hm2DiagnosticSNMPExtensionGroup,
       "hm2PortMonitorSpeedDuplexErrorReturn": hm2PortMonitorSpeedDuplexErrorReturn,
       "hm2PortMonitorCndOvldDetInconsistenTholdVal": hm2PortMonitorCndOvldDetInconsistenTholdVal}
)
