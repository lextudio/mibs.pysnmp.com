# SNMP MIB module (ALCATEL-IND1-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:45 2024
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

(hardentIND1Chassis,
 hardentIND1Physical) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardentIND1Chassis",
    "hardentIND1Physical")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1ChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1)
)
alcatelIND1ChassisMIB.setRevisions(
        ("2011-10-31 00:00",
         "2011-10-14 00:00",
         "2011-08-05 00:00",
         "2011-03-23 00:00",
         "2010-05-13 00:00",
         "2007-06-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaChasBpsShelfId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class ChasTrapsBPSPowerSupply(Integer32, TextualConvention):
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
        *(("bpsPoePower1", 3),
          ("bpsPoePower2", 4),
          ("bpsPoePower3", 5),
          ("bpsSysPower1", 1),
          ("bpsSysPower2", 2),
          ("notApplicable", 6))
    )



class ChasTrapsBPSFetState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("off", 2),
          ("on", 1))
    )



class ChasTrapsBPSEventAlert(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bpsPsPlugged", 1),
          ("bpsPsUnPlugged", 2),
          ("notApplicable", 3))
    )



class ChasEntPhysLed(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("amberBlink", 5),
          ("amberOn", 4),
          ("greenBlink", 3),
          ("greenOn", 2),
          ("notApplicable", 0),
          ("off", 1))
    )



class ChassisTrapsStrLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strApplicationFatal", 2),
          ("strFatal", 3),
          ("strNotFatal", 1))
    )



class ChassisTrapsStrAppID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ChassisTrapsStrSnapID(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ChassisTrapsStrfileLineNb(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class ChassisTrapsStrErrorNb(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ChassisTrapsStrdataInfo(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class ChassisTrapsObjectType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 1),
          ("cmm", 5),
          ("fabric", 6),
          ("fan", 4),
          ("gbic", 7),
          ("ni", 2),
          ("powerSuply", 3))
    )



class ChassisTrapsObjectNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ChassisTrapsAlertNumber(Integer32, TextualConvention):
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("activateScheduled", 44),
          ("activateStarted", 45),
          ("airflowReverse", 58),
          ("c20NiFailed", 57),
          ("c20RestoreFailed", 56),
          ("c20RestoreOk", 55),
          ("c20UpgradeFailed", 54),
          ("c20UpgradeOk", 53),
          ("certifyCompleted", 5),
          ("certifyFailed", 6),
          ("certifyFlashSyncStarted", 4),
          ("certifyStarted", 3),
          ("cmmAPlugged", 33),
          ("cmmAUnPlugged", 35),
          ("cmmBPlugged", 34),
          ("cmmBUnPlugged", 36),
          ("cmmStartingAsPrimary", 30),
          ("cmmStartingAsSecondary", 31),
          ("cmmStartupCompleted", 32),
          ("fanFailed", 18),
          ("fanOk", 19),
          ("fansOk", 20),
          ("getAfileCompleted", 46),
          ("getAfileFailed", 47),
          ("imageFileChecksumChanged", 62),
          ("lowNvramBattery", 37),
          ("macAllocFailed", 16),
          ("macRangeFailed", 17),
          ("notEnoughFabricsOperational", 38),
          ("powerMissing", 24),
          ("psAllOperational", 27),
          ("psNotOperational", 25),
          ("psOperational", 26),
          ("redundancyDisabledCertifyNeeded", 29),
          ("redundancyNotSupported", 28),
          ("reloadInProgress", 52),
          ("restoreCompleted", 11),
          ("restoreFailed", 12),
          ("restoreStarted", 10),
          ("runningCertified", 2),
          ("runningWorking", 1),
          ("secAutoActivate", 40),
          ("secAutoCertifyCompleted", 42),
          ("secAutoCertifyStarted", 41),
          ("secInactiveReset", 43),
          ("simplexNoSynchro", 39),
          ("synchroCompleted", 8),
          ("synchroFailed", 9),
          ("synchroStarted", 7),
          ("sysUpdateEnd", 51),
          ("sysUpdateError", 50),
          ("sysUpdateInProgress", 49),
          ("sysUpdateStart", 48),
          ("takeoverCompleted", 15),
          ("takeoverDeferred", 14),
          ("takeoverStarted", 13),
          ("tempDanger", 61),
          ("tempHWHigh", 60),
          ("tempOverDangerThreshold", 23),
          ("tempOverThreshold", 21),
          ("tempSWHigh", 59),
          ("tempUnderThreshold", 22))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1ChassisPhysMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBObjects = _AlcatelIND1ChassisPhysMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBObjects.setStatus("current")
_ChasEntPhysicalTable_Object = MibTable
chasEntPhysicalTable = _ChasEntPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chasEntPhysicalTable.setStatus("current")
_ChasEntPhysicalEntry_Object = MibTableRow
chasEntPhysicalEntry = _ChasEntPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1)
)
chasEntPhysicalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasEntPhysicalEntry.setStatus("current")


class _ChasEntPhysAdminStatus_Type(Integer32):
    """Custom type chasEntPhysAdminStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("powerOff", 2),
          ("powerOn", 3),
          ("reset", 4),
          ("resetAll", 6),
          ("resetVcAll", 11),
          ("resetWithFabric", 8),
          ("standby", 7),
          ("takeover", 5),
          ("takeoverWithFabrc", 9),
          ("unknown", 1),
          ("vcTakeover", 10))
    )


_ChasEntPhysAdminStatus_Type.__name__ = "Integer32"
_ChasEntPhysAdminStatus_Object = MibTableColumn
chasEntPhysAdminStatus = _ChasEntPhysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 1),
    _ChasEntPhysAdminStatus_Type()
)
chasEntPhysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasEntPhysAdminStatus.setStatus("current")


class _ChasEntPhysOperStatus_Type(Integer32):
    """Custom type chasEntPhysOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("idle", 9),
          ("master", 8),
          ("notPresent", 6),
          ("pwrsave", 10),
          ("secondary", 5),
          ("testing", 3),
          ("unknown", 4),
          ("unpowered", 7),
          ("up", 1))
    )


_ChasEntPhysOperStatus_Type.__name__ = "Integer32"
_ChasEntPhysOperStatus_Object = MibTableColumn
chasEntPhysOperStatus = _ChasEntPhysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 2),
    _ChasEntPhysOperStatus_Type()
)
chasEntPhysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysOperStatus.setStatus("current")


class _ChasEntPhysPower_Type(Integer32):
    """Custom type chasEntPhysPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysPower_Type.__name__ = "Integer32"
_ChasEntPhysPower_Object = MibTableColumn
chasEntPhysPower = _ChasEntPhysPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 3),
    _ChasEntPhysPower_Type()
)
chasEntPhysPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPower.setStatus("current")
_ChasEntPhysModuleType_Type = SnmpAdminString
_ChasEntPhysModuleType_Object = MibTableColumn
chasEntPhysModuleType = _ChasEntPhysModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 4),
    _ChasEntPhysModuleType_Type()
)
chasEntPhysModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysModuleType.setStatus("current")


class _ChasEntPhysPartNumber_Type(SnmpAdminString):
    """Custom type chasEntPhysPartNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChasEntPhysPartNumber_Type.__name__ = "SnmpAdminString"
_ChasEntPhysPartNumber_Object = MibTableColumn
chasEntPhysPartNumber = _ChasEntPhysPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 5),
    _ChasEntPhysPartNumber_Type()
)
chasEntPhysPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPartNumber.setStatus("current")
_ChasEntPhysLedStatusOk1_Type = ChasEntPhysLed
_ChasEntPhysLedStatusOk1_Object = MibTableColumn
chasEntPhysLedStatusOk1 = _ChasEntPhysLedStatusOk1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 6),
    _ChasEntPhysLedStatusOk1_Type()
)
chasEntPhysLedStatusOk1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusOk1.setStatus("current")
_ChasEntPhysLedStatusOk2_Type = ChasEntPhysLed
_ChasEntPhysLedStatusOk2_Object = MibTableColumn
chasEntPhysLedStatusOk2 = _ChasEntPhysLedStatusOk2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 7),
    _ChasEntPhysLedStatusOk2_Type()
)
chasEntPhysLedStatusOk2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusOk2.setStatus("current")
_ChasEntPhysLedStatusPrimaryCMM_Type = ChasEntPhysLed
_ChasEntPhysLedStatusPrimaryCMM_Object = MibTableColumn
chasEntPhysLedStatusPrimaryCMM = _ChasEntPhysLedStatusPrimaryCMM_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 8),
    _ChasEntPhysLedStatusPrimaryCMM_Type()
)
chasEntPhysLedStatusPrimaryCMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusPrimaryCMM.setStatus("current")
_ChasEntPhysLedStatusSecondaryCMM_Type = ChasEntPhysLed
_ChasEntPhysLedStatusSecondaryCMM_Object = MibTableColumn
chasEntPhysLedStatusSecondaryCMM = _ChasEntPhysLedStatusSecondaryCMM_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 9),
    _ChasEntPhysLedStatusSecondaryCMM_Type()
)
chasEntPhysLedStatusSecondaryCMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusSecondaryCMM.setStatus("current")
_ChasEntPhysLedStatusTemperature_Type = ChasEntPhysLed
_ChasEntPhysLedStatusTemperature_Object = MibTableColumn
chasEntPhysLedStatusTemperature = _ChasEntPhysLedStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 10),
    _ChasEntPhysLedStatusTemperature_Type()
)
chasEntPhysLedStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusTemperature.setStatus("current")
_ChasEntPhysLedStatusFan_Type = ChasEntPhysLed
_ChasEntPhysLedStatusFan_Object = MibTableColumn
chasEntPhysLedStatusFan = _ChasEntPhysLedStatusFan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 11),
    _ChasEntPhysLedStatusFan_Type()
)
chasEntPhysLedStatusFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusFan.setStatus("current")
_ChasEntPhysLedStatusBackupPS_Type = ChasEntPhysLed
_ChasEntPhysLedStatusBackupPS_Object = MibTableColumn
chasEntPhysLedStatusBackupPS = _ChasEntPhysLedStatusBackupPS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 12),
    _ChasEntPhysLedStatusBackupPS_Type()
)
chasEntPhysLedStatusBackupPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusBackupPS.setStatus("current")
_ChasEntPhysLedStatusInternalPS_Type = ChasEntPhysLed
_ChasEntPhysLedStatusInternalPS_Object = MibTableColumn
chasEntPhysLedStatusInternalPS = _ChasEntPhysLedStatusInternalPS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 13),
    _ChasEntPhysLedStatusInternalPS_Type()
)
chasEntPhysLedStatusInternalPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusInternalPS.setStatus("current")
_ChasEntPhysLedStatusControl_Type = ChasEntPhysLed
_ChasEntPhysLedStatusControl_Object = MibTableColumn
chasEntPhysLedStatusControl = _ChasEntPhysLedStatusControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 14),
    _ChasEntPhysLedStatusControl_Type()
)
chasEntPhysLedStatusControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusControl.setStatus("current")
_ChasEntPhysLedStatusFabric_Type = ChasEntPhysLed
_ChasEntPhysLedStatusFabric_Object = MibTableColumn
chasEntPhysLedStatusFabric = _ChasEntPhysLedStatusFabric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 15),
    _ChasEntPhysLedStatusFabric_Type()
)
chasEntPhysLedStatusFabric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusFabric.setStatus("current")
_ChasEntPhysLedStatusPS_Type = ChasEntPhysLed
_ChasEntPhysLedStatusPS_Object = MibTableColumn
chasEntPhysLedStatusPS = _ChasEntPhysLedStatusPS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 16),
    _ChasEntPhysLedStatusPS_Type()
)
chasEntPhysLedStatusPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusPS.setStatus("current")


class _ChasEntPhysAsic1Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysAsic1Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysAsic1Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysAsic1Rev_Object = MibTableColumn
chasEntPhysAsic1Rev = _ChasEntPhysAsic1Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 17),
    _ChasEntPhysAsic1Rev_Type()
)
chasEntPhysAsic1Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAsic1Rev.setStatus("current")


class _ChasEntPhysAsic2Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysAsic2Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysAsic2Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysAsic2Rev_Object = MibTableColumn
chasEntPhysAsic2Rev = _ChasEntPhysAsic2Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 18),
    _ChasEntPhysAsic2Rev_Type()
)
chasEntPhysAsic2Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAsic2Rev.setStatus("current")


class _ChasEntPhysAsic3Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysAsic3Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysAsic3Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysAsic3Rev_Object = MibTableColumn
chasEntPhysAsic3Rev = _ChasEntPhysAsic3Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 19),
    _ChasEntPhysAsic3Rev_Type()
)
chasEntPhysAsic3Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAsic3Rev.setStatus("current")


class _ChasEntPhysAsic4Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysAsic4Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysAsic4Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysAsic4Rev_Object = MibTableColumn
chasEntPhysAsic4Rev = _ChasEntPhysAsic4Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 20),
    _ChasEntPhysAsic4Rev_Type()
)
chasEntPhysAsic4Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAsic4Rev.setStatus("current")


class _ChasEntPhysAsic5Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysAsic5Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysAsic5Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysAsic5Rev_Object = MibTableColumn
chasEntPhysAsic5Rev = _ChasEntPhysAsic5Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 21),
    _ChasEntPhysAsic5Rev_Type()
)
chasEntPhysAsic5Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAsic5Rev.setStatus("current")


class _ChasEntPhysAsic6Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysAsic6Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysAsic6Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysAsic6Rev_Object = MibTableColumn
chasEntPhysAsic6Rev = _ChasEntPhysAsic6Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 22),
    _ChasEntPhysAsic6Rev_Type()
)
chasEntPhysAsic6Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAsic6Rev.setStatus("current")


class _ChasEntPhysCpldRev_Type(SnmpAdminString):
    """Custom type chasEntPhysCpldRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysCpldRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysCpldRev_Object = MibTableColumn
chasEntPhysCpldRev = _ChasEntPhysCpldRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 23),
    _ChasEntPhysCpldRev_Type()
)
chasEntPhysCpldRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysCpldRev.setStatus("current")


class _ChasEntPhysDaughterFpga1Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysDaughterFpga1Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysDaughterFpga1Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysDaughterFpga1Rev_Object = MibTableColumn
chasEntPhysDaughterFpga1Rev = _ChasEntPhysDaughterFpga1Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 24),
    _ChasEntPhysDaughterFpga1Rev_Type()
)
chasEntPhysDaughterFpga1Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysDaughterFpga1Rev.setStatus("current")


class _ChasEntPhysDaughterFpga2Rev_Type(SnmpAdminString):
    """Custom type chasEntPhysDaughterFpga2Rev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysDaughterFpga2Rev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysDaughterFpga2Rev_Object = MibTableColumn
chasEntPhysDaughterFpga2Rev = _ChasEntPhysDaughterFpga2Rev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 25),
    _ChasEntPhysDaughterFpga2Rev_Type()
)
chasEntPhysDaughterFpga2Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysDaughterFpga2Rev.setStatus("current")


class _ChasEntPhysNiNum_Type(Integer32):
    """Custom type chasEntPhysNiNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysNiNum_Type.__name__ = "Integer32"
_ChasEntPhysNiNum_Object = MibTableColumn
chasEntPhysNiNum = _ChasEntPhysNiNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 26),
    _ChasEntPhysNiNum_Type()
)
chasEntPhysNiNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysNiNum.setStatus("current")


class _ChasEntPhysGbicNum_Type(Integer32):
    """Custom type chasEntPhysGbicNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysGbicNum_Type.__name__ = "Integer32"
_ChasEntPhysGbicNum_Object = MibTableColumn
chasEntPhysGbicNum = _ChasEntPhysGbicNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 27),
    _ChasEntPhysGbicNum_Type()
)
chasEntPhysGbicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysGbicNum.setStatus("current")


class _ChasEntPhysWaveLen_Type(Integer32):
    """Custom type chasEntPhysWaveLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysWaveLen_Type.__name__ = "Integer32"
_ChasEntPhysWaveLen_Object = MibTableColumn
chasEntPhysWaveLen = _ChasEntPhysWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 28),
    _ChasEntPhysWaveLen_Type()
)
chasEntPhysWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysWaveLen.setStatus("current")


class _ChasEntPhysUbootRev_Type(SnmpAdminString):
    """Custom type chasEntPhysUbootRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysUbootRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysUbootRev_Object = MibTableColumn
chasEntPhysUbootRev = _ChasEntPhysUbootRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 29),
    _ChasEntPhysUbootRev_Type()
)
chasEntPhysUbootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysUbootRev.setStatus("current")


class _ChasEntPhysUbootMinibootRev_Type(SnmpAdminString):
    """Custom type chasEntPhysUbootMinibootRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysUbootMinibootRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysUbootMinibootRev_Object = MibTableColumn
chasEntPhysUbootMinibootRev = _ChasEntPhysUbootMinibootRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 30),
    _ChasEntPhysUbootMinibootRev_Type()
)
chasEntPhysUbootMinibootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysUbootMinibootRev.setStatus("current")
_ChasEntPhysMacAddress_Type = MacAddress
_ChasEntPhysMacAddress_Object = MibTableColumn
chasEntPhysMacAddress = _ChasEntPhysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 31),
    _ChasEntPhysMacAddress_Type()
)
chasEntPhysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysMacAddress.setStatus("current")


class _ChasEntPhysCpuModel_Type(SnmpAdminString):
    """Custom type chasEntPhysCpuModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasEntPhysCpuModel_Type.__name__ = "SnmpAdminString"
_ChasEntPhysCpuModel_Object = MibTableColumn
chasEntPhysCpuModel = _ChasEntPhysCpuModel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 32),
    _ChasEntPhysCpuModel_Type()
)
chasEntPhysCpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysCpuModel.setStatus("current")


class _ChasEntPhysAirflow_Type(Integer32):
    """Custom type chasEntPhysAirflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frontToRear", 0),
          ("notApplicable", 2),
          ("rearToFront", 1))
    )


_ChasEntPhysAirflow_Type.__name__ = "Integer32"
_ChasEntPhysAirflow_Object = MibTableColumn
chasEntPhysAirflow = _ChasEntPhysAirflow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 33),
    _ChasEntPhysAirflow_Type()
)
chasEntPhysAirflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAirflow.setStatus("current")


class _ChasEntPhysPowerUsed_Type(Integer32):
    """Custom type chasEntPhysPowerUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysPowerUsed_Type.__name__ = "Integer32"
_ChasEntPhysPowerUsed_Object = MibTableColumn
chasEntPhysPowerUsed = _ChasEntPhysPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 1, 1, 34),
    _ChasEntPhysPowerUsed_Type()
)
chasEntPhysPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPowerUsed.setStatus("current")
_ChasEntTemperatureTable_Object = MibTable
chasEntTemperatureTable = _ChasEntTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    chasEntTemperatureTable.setStatus("current")
_ChasEntTemperatureEntry_Object = MibTableRow
chasEntTemperatureEntry = _ChasEntTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 2, 1)
)
chasEntTemperatureEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasEntTemperatureEntry.setStatus("current")


class _ChasEntTempCurrent_Type(Integer32):
    """Custom type chasEntTempCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasEntTempCurrent_Type.__name__ = "Integer32"
_ChasEntTempCurrent_Object = MibTableColumn
chasEntTempCurrent = _ChasEntTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 2, 1, 1),
    _ChasEntTempCurrent_Type()
)
chasEntTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntTempCurrent.setStatus("current")


class _ChasEntTempThreshold_Type(Integer32):
    """Custom type chasEntTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_ChasEntTempThreshold_Type.__name__ = "Integer32"
_ChasEntTempThreshold_Object = MibTableColumn
chasEntTempThreshold = _ChasEntTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 2, 1, 2),
    _ChasEntTempThreshold_Type()
)
chasEntTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntTempThreshold.setStatus("current")


class _ChasEntTempDangerThreshold_Type(Integer32):
    """Custom type chasEntTempDangerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 150),
    )


_ChasEntTempDangerThreshold_Type.__name__ = "Integer32"
_ChasEntTempDangerThreshold_Object = MibTableColumn
chasEntTempDangerThreshold = _ChasEntTempDangerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 2, 1, 3),
    _ChasEntTempDangerThreshold_Type()
)
chasEntTempDangerThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntTempDangerThreshold.setStatus("current")


class _ChasEntTempStatus_Type(Integer32):
    """Custom type chasEntTempStatus based on Integer32"""
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
        *(("notPresent", 2),
          ("overDangerThreshold", 5),
          ("overFirstThreshold", 4),
          ("underThreshold", 3),
          ("unknown", 1))
    )


_ChasEntTempStatus_Type.__name__ = "Integer32"
_ChasEntTempStatus_Object = MibTableColumn
chasEntTempStatus = _ChasEntTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 1, 2, 1, 4),
    _ChasEntTempStatus_Type()
)
chasEntTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntTempStatus.setStatus("current")
_AlcatelIND1ChassisPhysMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBConformance = _AlcatelIND1ChassisPhysMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBConformance.setStatus("current")
_AlcatelIND1ChassisPhysMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBGroups = _AlcatelIND1ChassisPhysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBGroups.setStatus("current")
_AlcatelIND1ChassisPhysMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBCompliances = _AlcatelIND1ChassisPhysMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBCompliances.setStatus("current")
_AlcatelIND1ChassisMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBNotifications = _AlcatelIND1ChassisMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBNotifications.setStatus("current")
_AlcatelIND1ChassisMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBObjects = _AlcatelIND1ChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBObjects.setStatus("current")
_ChasControlModuleTable_Object = MibTable
chasControlModuleTable = _ChasControlModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chasControlModuleTable.setStatus("current")
_ChasControlModuleEntry_Object = MibTableRow
chasControlModuleEntry = _ChasControlModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1)
)
chasControlModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasControlModuleEntry.setStatus("current")


class _ChasControlActivateTimeout_Type(Integer32):
    """Custom type chasControlActivateTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ChasControlActivateTimeout_Type.__name__ = "Integer32"
_ChasControlActivateTimeout_Object = MibTableColumn
chasControlActivateTimeout = _ChasControlActivateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 1),
    _ChasControlActivateTimeout_Type()
)
chasControlActivateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlActivateTimeout.setStatus("current")


class _ChasControlVersionMngt_Type(Integer32):
    """Custom type chasControlVersionMngt based on Integer32"""
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
        *(("activate", 6),
          ("certifyNoSynchro", 3),
          ("certifySynchro", 2),
          ("flashSynchro", 4),
          ("issu", 7),
          ("notSignificant", 1),
          ("restore", 5),
          ("shutdown", 8),
          ("vcConvert", 9))
    )


_ChasControlVersionMngt_Type.__name__ = "Integer32"
_ChasControlVersionMngt_Object = MibTableColumn
chasControlVersionMngt = _ChasControlVersionMngt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 2),
    _ChasControlVersionMngt_Type()
)
chasControlVersionMngt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlVersionMngt.setStatus("current")


class _ChasControlDelayedActivateTimer_Type(Unsigned32):
    """Custom type chasControlDelayedActivateTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31622400),
    )


_ChasControlDelayedActivateTimer_Type.__name__ = "Unsigned32"
_ChasControlDelayedActivateTimer_Object = MibTableColumn
chasControlDelayedActivateTimer = _ChasControlDelayedActivateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 3),
    _ChasControlDelayedActivateTimer_Type()
)
chasControlDelayedActivateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDelayedActivateTimer.setStatus("current")


class _ChasControlCertifyStatus_Type(Integer32):
    """Custom type chasControlCertifyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("certified", 3),
          ("needCertify", 2),
          ("unknown", 1))
    )


_ChasControlCertifyStatus_Type.__name__ = "Integer32"
_ChasControlCertifyStatus_Object = MibTableColumn
chasControlCertifyStatus = _ChasControlCertifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 4),
    _ChasControlCertifyStatus_Type()
)
chasControlCertifyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlCertifyStatus.setStatus("current")


class _ChasControlSynchronizationStatus_Type(Integer32):
    """Custom type chasControlSynchronizationStatus based on Integer32"""
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
        *(("monoControlModule", 2),
          ("notSynchronized", 3),
          ("synchronized", 4),
          ("unknown", 1))
    )


_ChasControlSynchronizationStatus_Type.__name__ = "Integer32"
_ChasControlSynchronizationStatus_Object = MibTableColumn
chasControlSynchronizationStatus = _ChasControlSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 5),
    _ChasControlSynchronizationStatus_Type()
)
chasControlSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlSynchronizationStatus.setStatus("current")


class _ChasControlAcrossCmmWorkingSynchroStatus_Type(Integer32):
    """Custom type chasControlAcrossCmmWorkingSynchroStatus based on Integer32"""
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
        *(("monoCMM", 2),
          ("no", 3),
          ("unknown", 1),
          ("yes", 4))
    )


_ChasControlAcrossCmmWorkingSynchroStatus_Type.__name__ = "Integer32"
_ChasControlAcrossCmmWorkingSynchroStatus_Object = MibTableColumn
chasControlAcrossCmmWorkingSynchroStatus = _ChasControlAcrossCmmWorkingSynchroStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 6),
    _ChasControlAcrossCmmWorkingSynchroStatus_Type()
)
chasControlAcrossCmmWorkingSynchroStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlAcrossCmmWorkingSynchroStatus.setStatus("current")


class _ChasControlAcrossCmmCertifiedSynchroStatus_Type(Integer32):
    """Custom type chasControlAcrossCmmCertifiedSynchroStatus based on Integer32"""
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
        *(("monoCMM", 2),
          ("no", 3),
          ("unknown", 1),
          ("yes", 4))
    )


_ChasControlAcrossCmmCertifiedSynchroStatus_Type.__name__ = "Integer32"
_ChasControlAcrossCmmCertifiedSynchroStatus_Object = MibTableColumn
chasControlAcrossCmmCertifiedSynchroStatus = _ChasControlAcrossCmmCertifiedSynchroStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 7),
    _ChasControlAcrossCmmCertifiedSynchroStatus_Type()
)
chasControlAcrossCmmCertifiedSynchroStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlAcrossCmmCertifiedSynchroStatus.setStatus("current")
_ChasControlNextRunningVersion_Type = SnmpAdminString
_ChasControlNextRunningVersion_Object = MibTableColumn
chasControlNextRunningVersion = _ChasControlNextRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 8),
    _ChasControlNextRunningVersion_Type()
)
chasControlNextRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlNextRunningVersion.setStatus("current")
_ChasControlCurrentRunningVersion_Type = SnmpAdminString
_ChasControlCurrentRunningVersion_Object = MibTableColumn
chasControlCurrentRunningVersion = _ChasControlCurrentRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 9),
    _ChasControlCurrentRunningVersion_Type()
)
chasControlCurrentRunningVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlCurrentRunningVersion.setStatus("current")
_ChasControlWorkingVersion_Type = SnmpAdminString
_ChasControlWorkingVersion_Object = MibTableColumn
chasControlWorkingVersion = _ChasControlWorkingVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 10),
    _ChasControlWorkingVersion_Type()
)
chasControlWorkingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlWorkingVersion.setStatus("current")


class _ChasControlRedundancyTime_Type(Integer32):
    """Custom type chasControlRedundancyTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ChasControlRedundancyTime_Type.__name__ = "Integer32"
_ChasControlRedundancyTime_Object = MibTableColumn
chasControlRedundancyTime = _ChasControlRedundancyTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 11),
    _ChasControlRedundancyTime_Type()
)
chasControlRedundancyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlRedundancyTime.setStatus("current")
_ChasControlEmpIpAddress_Type = IpAddress
_ChasControlEmpIpAddress_Object = MibTableColumn
chasControlEmpIpAddress = _ChasControlEmpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 12),
    _ChasControlEmpIpAddress_Type()
)
chasControlEmpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEmpIpAddress.setStatus("deprecated")
_ChasControlEmpIpMask_Type = IpAddress
_ChasControlEmpIpMask_Object = MibTableColumn
chasControlEmpIpMask = _ChasControlEmpIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 13),
    _ChasControlEmpIpMask_Type()
)
chasControlEmpIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlEmpIpMask.setStatus("deprecated")


class _ChasControlChassisId_Type(Integer32):
    """Custom type chasControlChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ChasControlChassisId_Type.__name__ = "Integer32"
_ChasControlChassisId_Object = MibTableColumn
chasControlChassisId = _ChasControlChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 1, 1, 14),
    _ChasControlChassisId_Type()
)
chasControlChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlChassisId.setStatus("current")
_ChasControlRedundantTable_Object = MibTable
chasControlRedundantTable = _ChasControlRedundantTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    chasControlRedundantTable.setStatus("current")
_ChasControlRedundantEntry_Object = MibTableRow
chasControlRedundantEntry = _ChasControlRedundantEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 2, 1)
)
chasControlRedundantEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasControlRedundantEntry.setStatus("current")
_ChasControlNumberOfTakeover_Type = Counter32
_ChasControlNumberOfTakeover_Object = MibTableColumn
chasControlNumberOfTakeover = _ChasControlNumberOfTakeover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 2, 1, 1),
    _ChasControlNumberOfTakeover_Type()
)
chasControlNumberOfTakeover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlNumberOfTakeover.setStatus("current")


class _ChasControlDelayedRebootTimer_Type(Unsigned32):
    """Custom type chasControlDelayedRebootTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31622400),
    )


_ChasControlDelayedRebootTimer_Type.__name__ = "Unsigned32"
_ChasControlDelayedRebootTimer_Object = MibTableColumn
chasControlDelayedRebootTimer = _ChasControlDelayedRebootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 2, 1, 2),
    _ChasControlDelayedRebootTimer_Type()
)
chasControlDelayedRebootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDelayedRebootTimer.setStatus("current")


class _ChasControlDelayedResetAll_Type(Integer32):
    """Custom type chasControlDelayedResetAll based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_ChasControlDelayedResetAll_Type.__name__ = "Integer32"
_ChasControlDelayedResetAll_Object = MibTableColumn
chasControlDelayedResetAll = _ChasControlDelayedResetAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 2, 1, 3),
    _ChasControlDelayedResetAll_Type()
)
chasControlDelayedResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDelayedResetAll.setStatus("current")
_ChasChassisTable_Object = MibTable
chasChassisTable = _ChasChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    chasChassisTable.setStatus("current")
_ChasChassisEntry_Object = MibTableRow
chasChassisEntry = _ChasChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1)
)
chasChassisEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasChassisEntry.setStatus("current")


class _ChasFreeSlots_Type(Unsigned32):
    """Custom type chasFreeSlots based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_ChasFreeSlots_Type.__name__ = "Unsigned32"
_ChasFreeSlots_Object = MibTableColumn
chasFreeSlots = _ChasFreeSlots_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 1),
    _ChasFreeSlots_Type()
)
chasFreeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFreeSlots.setStatus("current")


class _ChasPowerLeft_Type(Integer32):
    """Custom type chasPowerLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_ChasPowerLeft_Type.__name__ = "Integer32"
_ChasPowerLeft_Object = MibTableColumn
chasPowerLeft = _ChasPowerLeft_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 2),
    _ChasPowerLeft_Type()
)
chasPowerLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerLeft.setStatus("current")
_ChasNumberOfResets_Type = Counter32
_ChasNumberOfResets_Object = MibTableColumn
chasNumberOfResets = _ChasNumberOfResets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 3),
    _ChasNumberOfResets_Type()
)
chasNumberOfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNumberOfResets.setStatus("current")


class _ChasTempRange_Type(Integer32):
    """Custom type chasTempRange based on Integer32"""
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
        *(("notPresent", 2),
          ("overDangerThreshold", 5),
          ("overFirstThreshold", 4),
          ("underThreshold", 3),
          ("unknown", 1))
    )


_ChasTempRange_Type.__name__ = "Integer32"
_ChasTempRange_Object = MibTableColumn
chasTempRange = _ChasTempRange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 4),
    _ChasTempRange_Type()
)
chasTempRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTempRange.setStatus("current")


class _ChasTempThreshold_Type(Integer32):
    """Custom type chasTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_ChasTempThreshold_Type.__name__ = "Integer32"
_ChasTempThreshold_Object = MibTableColumn
chasTempThreshold = _ChasTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 5),
    _ChasTempThreshold_Type()
)
chasTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasTempThreshold.setStatus("current")


class _ChasDangerTempThreshold_Type(Integer32):
    """Custom type chasDangerTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 150),
    )


_ChasDangerTempThreshold_Type.__name__ = "Integer32"
_ChasDangerTempThreshold_Object = MibTableColumn
chasDangerTempThreshold = _ChasDangerTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 6),
    _ChasDangerTempThreshold_Type()
)
chasDangerTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasDangerTempThreshold.setStatus("current")


class _ChasPrimaryPhysicalIndex_Type(Integer32):
    """Custom type chasPrimaryPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChasPrimaryPhysicalIndex_Type.__name__ = "Integer32"
_ChasPrimaryPhysicalIndex_Object = MibTableColumn
chasPrimaryPhysicalIndex = _ChasPrimaryPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 7),
    _ChasPrimaryPhysicalIndex_Type()
)
chasPrimaryPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPrimaryPhysicalIndex.setStatus("current")


class _ChasCPMAHardwareBoardTemp_Type(Integer32):
    """Custom type chasCPMAHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasCPMAHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasCPMAHardwareBoardTemp_Object = MibTableColumn
chasCPMAHardwareBoardTemp = _ChasCPMAHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 8),
    _ChasCPMAHardwareBoardTemp_Type()
)
chasCPMAHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasCPMAHardwareBoardTemp.setStatus("current")


class _ChasCFMAHardwareBoardTemp_Type(Integer32):
    """Custom type chasCFMAHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasCFMAHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasCFMAHardwareBoardTemp_Object = MibTableColumn
chasCFMAHardwareBoardTemp = _ChasCFMAHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 9),
    _ChasCFMAHardwareBoardTemp_Type()
)
chasCFMAHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasCFMAHardwareBoardTemp.setStatus("current")


class _ChasCPMBHardwareBoardTemp_Type(Integer32):
    """Custom type chasCPMBHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasCPMBHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasCPMBHardwareBoardTemp_Object = MibTableColumn
chasCPMBHardwareBoardTemp = _ChasCPMBHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 10),
    _ChasCPMBHardwareBoardTemp_Type()
)
chasCPMBHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasCPMBHardwareBoardTemp.setStatus("current")


class _ChasCFMBHardwareBoardTemp_Type(Integer32):
    """Custom type chasCFMBHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasCFMBHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasCFMBHardwareBoardTemp_Object = MibTableColumn
chasCFMBHardwareBoardTemp = _ChasCFMBHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 11),
    _ChasCFMBHardwareBoardTemp_Type()
)
chasCFMBHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasCFMBHardwareBoardTemp.setStatus("current")


class _ChasCFMCHardwareBoardTemp_Type(Integer32):
    """Custom type chasCFMCHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasCFMCHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasCFMCHardwareBoardTemp_Object = MibTableColumn
chasCFMCHardwareBoardTemp = _ChasCFMCHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 12),
    _ChasCFMCHardwareBoardTemp_Type()
)
chasCFMCHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasCFMCHardwareBoardTemp.setStatus("current")


class _ChasCFMDHardwareBoardTemp_Type(Integer32):
    """Custom type chasCFMDHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasCFMDHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasCFMDHardwareBoardTemp_Object = MibTableColumn
chasCFMDHardwareBoardTemp = _ChasCFMDHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 13),
    _ChasCFMDHardwareBoardTemp_Type()
)
chasCFMDHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasCFMDHardwareBoardTemp.setStatus("current")


class _ChasFTAHardwareBoardTemp_Type(Integer32):
    """Custom type chasFTAHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasFTAHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasFTAHardwareBoardTemp_Object = MibTableColumn
chasFTAHardwareBoardTemp = _ChasFTAHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 14),
    _ChasFTAHardwareBoardTemp_Type()
)
chasFTAHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFTAHardwareBoardTemp.setStatus("current")


class _ChasFTBHardwareBoardTemp_Type(Integer32):
    """Custom type chasFTBHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasFTBHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasFTBHardwareBoardTemp_Object = MibTableColumn
chasFTBHardwareBoardTemp = _ChasFTBHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 15),
    _ChasFTBHardwareBoardTemp_Type()
)
chasFTBHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFTBHardwareBoardTemp.setStatus("current")


class _ChasNI1HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI1HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI1HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI1HardwareBoardTemp_Object = MibTableColumn
chasNI1HardwareBoardTemp = _ChasNI1HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 16),
    _ChasNI1HardwareBoardTemp_Type()
)
chasNI1HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI1HardwareBoardTemp.setStatus("current")


class _ChasNI2HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI2HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI2HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI2HardwareBoardTemp_Object = MibTableColumn
chasNI2HardwareBoardTemp = _ChasNI2HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 17),
    _ChasNI2HardwareBoardTemp_Type()
)
chasNI2HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI2HardwareBoardTemp.setStatus("current")


class _ChasNI3HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI3HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI3HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI3HardwareBoardTemp_Object = MibTableColumn
chasNI3HardwareBoardTemp = _ChasNI3HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 18),
    _ChasNI3HardwareBoardTemp_Type()
)
chasNI3HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI3HardwareBoardTemp.setStatus("current")


class _ChasNI4HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI4HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI4HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI4HardwareBoardTemp_Object = MibTableColumn
chasNI4HardwareBoardTemp = _ChasNI4HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 19),
    _ChasNI4HardwareBoardTemp_Type()
)
chasNI4HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI4HardwareBoardTemp.setStatus("current")


class _ChasNI5HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI5HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI5HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI5HardwareBoardTemp_Object = MibTableColumn
chasNI5HardwareBoardTemp = _ChasNI5HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 20),
    _ChasNI5HardwareBoardTemp_Type()
)
chasNI5HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI5HardwareBoardTemp.setStatus("current")


class _ChasNI6HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI6HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI6HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI6HardwareBoardTemp_Object = MibTableColumn
chasNI6HardwareBoardTemp = _ChasNI6HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 21),
    _ChasNI6HardwareBoardTemp_Type()
)
chasNI6HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI6HardwareBoardTemp.setStatus("current")


class _ChasNI7HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI7HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI7HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI7HardwareBoardTemp_Object = MibTableColumn
chasNI7HardwareBoardTemp = _ChasNI7HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 22),
    _ChasNI7HardwareBoardTemp_Type()
)
chasNI7HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI7HardwareBoardTemp.setStatus("current")


class _ChasNI8HardwareBoardTemp_Type(Integer32):
    """Custom type chasNI8HardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasNI8HardwareBoardTemp_Type.__name__ = "Integer32"
_ChasNI8HardwareBoardTemp_Object = MibTableColumn
chasNI8HardwareBoardTemp = _ChasNI8HardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 23),
    _ChasNI8HardwareBoardTemp_Type()
)
chasNI8HardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNI8HardwareBoardTemp.setStatus("current")


class _ChasPowerSupplyRedundancy_Type(Integer32):
    """Custom type chasPowerSupplyRedundancy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ChasPowerSupplyRedundancy_Type.__name__ = "Integer32"
_ChasPowerSupplyRedundancy_Object = MibTableColumn
chasPowerSupplyRedundancy = _ChasPowerSupplyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 3, 1, 24),
    _ChasPowerSupplyRedundancy_Type()
)
chasPowerSupplyRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPowerSupplyRedundancy.setStatus("current")
_ChasSupervisionRfsLsTable_Object = MibTable
chasSupervisionRfsLsTable = _ChasSupervisionRfsLsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    chasSupervisionRfsLsTable.setStatus("current")
_ChasSupervisionRfsLsEntry_Object = MibTableRow
chasSupervisionRfsLsEntry = _ChasSupervisionRfsLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1)
)
chasSupervisionRfsLsEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileIndex"),
)
if mibBuilder.loadTexts:
    chasSupervisionRfsLsEntry.setStatus("current")


class _ChasSupervisionRfsLsFileIndex_Type(Integer32):
    """Custom type chasSupervisionRfsLsFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChasSupervisionRfsLsFileIndex_Type.__name__ = "Integer32"
_ChasSupervisionRfsLsFileIndex_Object = MibTableColumn
chasSupervisionRfsLsFileIndex = _ChasSupervisionRfsLsFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 1),
    _ChasSupervisionRfsLsFileIndex_Type()
)
chasSupervisionRfsLsFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileIndex.setStatus("current")
_ChasSupervisionRfsLsSlot_Type = Unsigned32
_ChasSupervisionRfsLsSlot_Object = MibTableColumn
chasSupervisionRfsLsSlot = _ChasSupervisionRfsLsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 2),
    _ChasSupervisionRfsLsSlot_Type()
)
chasSupervisionRfsLsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsSlot.setStatus("current")


class _ChasSupervisionRfsLsDirName_Type(SnmpAdminString):
    """Custom type chasSupervisionRfsLsDirName based on SnmpAdminString"""
    defaultValue = OctetString("/flash")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsLsDirName_Type.__name__ = "SnmpAdminString"
_ChasSupervisionRfsLsDirName_Object = MibTableColumn
chasSupervisionRfsLsDirName = _ChasSupervisionRfsLsDirName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 3),
    _ChasSupervisionRfsLsDirName_Type()
)
chasSupervisionRfsLsDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsDirName.setStatus("current")


class _ChasSupervisionRfsLsFileName_Type(SnmpAdminString):
    """Custom type chasSupervisionRfsLsFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ChasSupervisionRfsLsFileName_Type.__name__ = "SnmpAdminString"
_ChasSupervisionRfsLsFileName_Object = MibTableColumn
chasSupervisionRfsLsFileName = _ChasSupervisionRfsLsFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 4),
    _ChasSupervisionRfsLsFileName_Type()
)
chasSupervisionRfsLsFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileName.setStatus("current")


class _ChasSupervisionRfsLsFileType_Type(Integer32):
    """Custom type chasSupervisionRfsLsFileType based on Integer32"""
    defaultValue = 3

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
        *(("directory", 2),
          ("file", 1),
          ("tarArchive", 4),
          ("undefined", 3))
    )


_ChasSupervisionRfsLsFileType_Type.__name__ = "Integer32"
_ChasSupervisionRfsLsFileType_Object = MibTableColumn
chasSupervisionRfsLsFileType = _ChasSupervisionRfsLsFileType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 5),
    _ChasSupervisionRfsLsFileType_Type()
)
chasSupervisionRfsLsFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileType.setStatus("current")


class _ChasSupervisionRfsLsFileSize_Type(Unsigned32):
    """Custom type chasSupervisionRfsLsFileSize based on Unsigned32"""
    defaultValue = 0


_ChasSupervisionRfsLsFileSize_Object = MibTableColumn
chasSupervisionRfsLsFileSize = _ChasSupervisionRfsLsFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 6),
    _ChasSupervisionRfsLsFileSize_Type()
)
chasSupervisionRfsLsFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileSize.setStatus("current")


class _ChasSupervisionRfsLsFileAttr_Type(Integer32):
    """Custom type chasSupervisionRfsLsFileAttr based on Integer32"""
    defaultValue = 1

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
        *(("readOnly", 2),
          ("readWrite", 3),
          ("undefined", 1),
          ("writeOnly", 4))
    )


_ChasSupervisionRfsLsFileAttr_Type.__name__ = "Integer32"
_ChasSupervisionRfsLsFileAttr_Object = MibTableColumn
chasSupervisionRfsLsFileAttr = _ChasSupervisionRfsLsFileAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 7),
    _ChasSupervisionRfsLsFileAttr_Type()
)
chasSupervisionRfsLsFileAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileAttr.setStatus("current")


class _ChasSupervisionRfsLsFileDateTime_Type(SnmpAdminString):
    """Custom type chasSupervisionRfsLsFileDateTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChasSupervisionRfsLsFileDateTime_Type.__name__ = "SnmpAdminString"
_ChasSupervisionRfsLsFileDateTime_Object = MibTableColumn
chasSupervisionRfsLsFileDateTime = _ChasSupervisionRfsLsFileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 4, 1, 8),
    _ChasSupervisionRfsLsFileDateTime_Type()
)
chasSupervisionRfsLsFileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileDateTime.setStatus("current")
_AlcatelIND1ChassisSupervisionRfsCommands_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisSupervisionRfsCommands = _AlcatelIND1ChassisSupervisionRfsCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisSupervisionRfsCommands.setStatus("current")
_ChasSupervisionRfsCommandsSlot_Type = Unsigned32
_ChasSupervisionRfsCommandsSlot_Object = MibScalar
chasSupervisionRfsCommandsSlot = _ChasSupervisionRfsCommandsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 1),
    _ChasSupervisionRfsCommandsSlot_Type()
)
chasSupervisionRfsCommandsSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsSlot.setStatus("current")


class _ChasSupervisionRfsCommandsCommand_Type(Integer32):
    """Custom type chasSupervisionRfsCommandsCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notSignificant", 0),
          ("rcp", 2),
          ("rdf", 4),
          ("reserved", 7),
          ("rget", 5),
          ("rls", 3),
          ("rput", 6),
          ("rrm", 1))
    )


_ChasSupervisionRfsCommandsCommand_Type.__name__ = "Integer32"
_ChasSupervisionRfsCommandsCommand_Object = MibScalar
chasSupervisionRfsCommandsCommand = _ChasSupervisionRfsCommandsCommand_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 2),
    _ChasSupervisionRfsCommandsCommand_Type()
)
chasSupervisionRfsCommandsCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsCommand.setStatus("current")


class _ChasSupervisionRfsCommandsSrcFileName_Type(SnmpAdminString):
    """Custom type chasSupervisionRfsCommandsSrcFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsCommandsSrcFileName_Type.__name__ = "SnmpAdminString"
_ChasSupervisionRfsCommandsSrcFileName_Object = MibScalar
chasSupervisionRfsCommandsSrcFileName = _ChasSupervisionRfsCommandsSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 3),
    _ChasSupervisionRfsCommandsSrcFileName_Type()
)
chasSupervisionRfsCommandsSrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsSrcFileName.setStatus("current")


class _ChasSupervisionRfsCommandsDestFileName_Type(SnmpAdminString):
    """Custom type chasSupervisionRfsCommandsDestFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsCommandsDestFileName_Type.__name__ = "SnmpAdminString"
_ChasSupervisionRfsCommandsDestFileName_Object = MibScalar
chasSupervisionRfsCommandsDestFileName = _ChasSupervisionRfsCommandsDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 4),
    _ChasSupervisionRfsCommandsDestFileName_Type()
)
chasSupervisionRfsCommandsDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsDestFileName.setStatus("current")


class _ChasSupervisionRfsCommandsRlsDirName_Type(SnmpAdminString):
    """Custom type chasSupervisionRfsCommandsRlsDirName based on SnmpAdminString"""
    defaultValue = OctetString("/flash")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsCommandsRlsDirName_Type.__name__ = "SnmpAdminString"
_ChasSupervisionRfsCommandsRlsDirName_Object = MibScalar
chasSupervisionRfsCommandsRlsDirName = _ChasSupervisionRfsCommandsRlsDirName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 5),
    _ChasSupervisionRfsCommandsRlsDirName_Type()
)
chasSupervisionRfsCommandsRlsDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsRlsDirName.setStatus("current")


class _ChasSupervisionRfsCommandsRlsFileName_Type(SnmpAdminString):
    """Custom type chasSupervisionRfsCommandsRlsFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsCommandsRlsFileName_Type.__name__ = "SnmpAdminString"
_ChasSupervisionRfsCommandsRlsFileName_Object = MibScalar
chasSupervisionRfsCommandsRlsFileName = _ChasSupervisionRfsCommandsRlsFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 6),
    _ChasSupervisionRfsCommandsRlsFileName_Type()
)
chasSupervisionRfsCommandsRlsFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsRlsFileName.setStatus("current")


class _ChasSupervisionRfsCommandsProcessingState_Type(Integer32):
    """Custom type chasSupervisionRfsCommandsProcessingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("ready", 2))
    )


_ChasSupervisionRfsCommandsProcessingState_Type.__name__ = "Integer32"
_ChasSupervisionRfsCommandsProcessingState_Object = MibScalar
chasSupervisionRfsCommandsProcessingState = _ChasSupervisionRfsCommandsProcessingState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 7),
    _ChasSupervisionRfsCommandsProcessingState_Type()
)
chasSupervisionRfsCommandsProcessingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsProcessingState.setStatus("current")


class _ChasSupervisionRfsCommandsStatusCode_Type(Integer32):
    """Custom type chasSupervisionRfsCommandsStatusCode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("directoryNotAllowToRemove", 10),
          ("directoryNotExist", 4),
          ("fileNotExist", 5),
          ("maximumFilesExceed", 6),
          ("noDiskSpace", 7),
          ("permissionDenied", 11),
          ("slotIsPrimary", 2),
          ("slotNotExist", 3),
          ("success", 1),
          ("systemBusy", 8),
          ("systemError", 9))
    )


_ChasSupervisionRfsCommandsStatusCode_Type.__name__ = "Integer32"
_ChasSupervisionRfsCommandsStatusCode_Object = MibScalar
chasSupervisionRfsCommandsStatusCode = _ChasSupervisionRfsCommandsStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 5, 8),
    _ChasSupervisionRfsCommandsStatusCode_Type()
)
chasSupervisionRfsCommandsStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsStatusCode.setStatus("current")
_ChasControlReloadStatusTable_Object = MibTable
chasControlReloadStatusTable = _ChasControlReloadStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    chasControlReloadStatusTable.setStatus("current")
_ChasControlReloadEntry_Object = MibTableRow
chasControlReloadEntry = _ChasControlReloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 6, 1)
)
chasControlReloadEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasControlReloadIndex"),
)
if mibBuilder.loadTexts:
    chasControlReloadEntry.setStatus("current")


class _ChasControlReloadIndex_Type(Integer32):
    """Custom type chasControlReloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ChasControlReloadIndex_Type.__name__ = "Integer32"
_ChasControlReloadIndex_Object = MibTableColumn
chasControlReloadIndex = _ChasControlReloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 6, 1, 1),
    _ChasControlReloadIndex_Type()
)
chasControlReloadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasControlReloadIndex.setStatus("current")


class _ChasControlReloadStatus_Type(Integer32):
    """Custom type chasControlReloadStatus based on Integer32"""
    defaultValue = 2

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
        *(("noInterface", 3),
          ("reloadDisabled", 2),
          ("reloadEnabled", 1),
          ("unknown", 4))
    )


_ChasControlReloadStatus_Type.__name__ = "Integer32"
_ChasControlReloadStatus_Object = MibTableColumn
chasControlReloadStatus = _ChasControlReloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 6, 1, 2),
    _ChasControlReloadStatus_Type()
)
chasControlReloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlReloadStatus.setStatus("current")
_ChasGlobalControl_ObjectIdentity = ObjectIdentity
chasGlobalControl = _ChasGlobalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7)
)


class _ChasGlobalControlDelayedResetAll_Type(Integer32):
    """Custom type chasGlobalControlDelayedResetAll based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_ChasGlobalControlDelayedResetAll_Type.__name__ = "Integer32"
_ChasGlobalControlDelayedResetAll_Object = MibScalar
chasGlobalControlDelayedResetAll = _ChasGlobalControlDelayedResetAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 1),
    _ChasGlobalControlDelayedResetAll_Type()
)
chasGlobalControlDelayedResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasGlobalControlDelayedResetAll.setStatus("current")


class _ChasGlobalControlLongCommand_Type(Integer32):
    """Custom type chasGlobalControlLongCommand based on Integer32"""
    defaultValue = 1

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("certifyNoSynchro", 3),
          ("certifySynchro", 2),
          ("flashSynchro", 4),
          ("issu", 8),
          ("macRelease", 11),
          ("none", 1),
          ("reload", 6),
          ("restore", 5),
          ("rfs", 7),
          ("shutdown", 9),
          ("vcConvert", 10))
    )


_ChasGlobalControlLongCommand_Type.__name__ = "Integer32"
_ChasGlobalControlLongCommand_Object = MibScalar
chasGlobalControlLongCommand = _ChasGlobalControlLongCommand_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 2),
    _ChasGlobalControlLongCommand_Type()
)
chasGlobalControlLongCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasGlobalControlLongCommand.setStatus("current")


class _ChasGlobalControlLongCommandStatus_Type(Integer32):
    """Custom type chasGlobalControlLongCommandStatus based on Integer32"""
    defaultValue = 1

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
        *(("completeFailure", 4),
          ("completeSuccess", 3),
          ("confirmationRequired", 5),
          ("inProgress", 2),
          ("none", 1))
    )


_ChasGlobalControlLongCommandStatus_Type.__name__ = "Integer32"
_ChasGlobalControlLongCommandStatus_Object = MibScalar
chasGlobalControlLongCommandStatus = _ChasGlobalControlLongCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 3),
    _ChasGlobalControlLongCommandStatus_Type()
)
chasGlobalControlLongCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasGlobalControlLongCommandStatus.setStatus("current")


class _ChasGlobalControlUpdateFirmware_Type(Integer32):
    """Custom type chasGlobalControlUpdateFirmware based on Integer32"""
    defaultValue = 1

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fpgaCmm", 6),
          ("fpgaCmmAll", 10),
          ("fpgaNi", 7),
          ("fpgaNiDaughterBoard1", 8),
          ("fpgaNiDaughterBoard2", 9),
          ("none", 1),
          ("ubootCmm", 2),
          ("ubootCmmAll", 5),
          ("ubootNi", 3),
          ("ubootNiAll", 4))
    )


_ChasGlobalControlUpdateFirmware_Type.__name__ = "Integer32"
_ChasGlobalControlUpdateFirmware_Object = MibScalar
chasGlobalControlUpdateFirmware = _ChasGlobalControlUpdateFirmware_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 4),
    _ChasGlobalControlUpdateFirmware_Type()
)
chasGlobalControlUpdateFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasGlobalControlUpdateFirmware.setStatus("current")
_ChasGlobalControlUpdateSlot_Type = Integer32
_ChasGlobalControlUpdateSlot_Object = MibScalar
chasGlobalControlUpdateSlot = _ChasGlobalControlUpdateSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 5),
    _ChasGlobalControlUpdateSlot_Type()
)
chasGlobalControlUpdateSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasGlobalControlUpdateSlot.setStatus("current")


class _ChasGlobalControlUpdateFilename_Type(SnmpAdminString):
    """Custom type chasGlobalControlUpdateFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasGlobalControlUpdateFilename_Type.__name__ = "SnmpAdminString"
_ChasGlobalControlUpdateFilename_Object = MibScalar
chasGlobalControlUpdateFilename = _ChasGlobalControlUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 6),
    _ChasGlobalControlUpdateFilename_Type()
)
chasGlobalControlUpdateFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasGlobalControlUpdateFilename.setStatus("current")


class _ChasGlobalControlUpdateStatus_Type(Integer32):
    """Custom type chasGlobalControlUpdateStatus based on Integer32"""
    defaultValue = 1

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
        *(("noUpdate", 1),
          ("updateFailed", 4),
          ("updateInProgress", 2),
          ("updateSuccess", 3))
    )


_ChasGlobalControlUpdateStatus_Type.__name__ = "Integer32"
_ChasGlobalControlUpdateStatus_Object = MibScalar
chasGlobalControlUpdateStatus = _ChasGlobalControlUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 7),
    _ChasGlobalControlUpdateStatus_Type()
)
chasGlobalControlUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasGlobalControlUpdateStatus.setStatus("current")
_ChasGlobalControlConfirmOperation_Type = TruthValue
_ChasGlobalControlConfirmOperation_Object = MibScalar
chasGlobalControlConfirmOperation = _ChasGlobalControlConfirmOperation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 8),
    _ChasGlobalControlConfirmOperation_Type()
)
chasGlobalControlConfirmOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasGlobalControlConfirmOperation.setStatus("current")
_ChasGlobalControlConfirmMessage_Type = DisplayString
_ChasGlobalControlConfirmMessage_Object = MibScalar
chasGlobalControlConfirmMessage = _ChasGlobalControlConfirmMessage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 7, 9),
    _ChasGlobalControlConfirmMessage_Type()
)
chasGlobalControlConfirmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasGlobalControlConfirmMessage.setStatus("current")
_ChasSupervisionRfsDfTable_Object = MibTable
chasSupervisionRfsDfTable = _ChasSupervisionRfsDfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    chasSupervisionRfsDfTable.setStatus("current")
_ChasSupervisionRfsDfEntry_Object = MibTableRow
chasSupervisionRfsDfEntry = _ChasSupervisionRfsDfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 8, 1)
)
chasSupervisionRfsDfEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsDfSlot"),
)
if mibBuilder.loadTexts:
    chasSupervisionRfsDfEntry.setStatus("current")


class _ChasSupervisionRfsDfSlot_Type(Integer32):
    """Custom type chasSupervisionRfsDfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChasSupervisionRfsDfSlot_Type.__name__ = "Integer32"
_ChasSupervisionRfsDfSlot_Object = MibTableColumn
chasSupervisionRfsDfSlot = _ChasSupervisionRfsDfSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 8, 1, 1),
    _ChasSupervisionRfsDfSlot_Type()
)
chasSupervisionRfsDfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfSlot.setStatus("current")
_ChasSupervisionRfsDfFlashFree_Type = Unsigned32
_ChasSupervisionRfsDfFlashFree_Object = MibTableColumn
chasSupervisionRfsDfFlashFree = _ChasSupervisionRfsDfFlashFree_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 8, 1, 2),
    _ChasSupervisionRfsDfFlashFree_Type()
)
chasSupervisionRfsDfFlashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfFlashFree.setStatus("current")
_ChasSupervisionRfsDfFlashSize_Type = Unsigned32
_ChasSupervisionRfsDfFlashSize_Object = MibTableColumn
chasSupervisionRfsDfFlashSize = _ChasSupervisionRfsDfFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 8, 1, 3),
    _ChasSupervisionRfsDfFlashSize_Type()
)
chasSupervisionRfsDfFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfFlashSize.setStatus("current")
_ChasSupervisionRfsDfUsbFree_Type = Unsigned32
_ChasSupervisionRfsDfUsbFree_Object = MibTableColumn
chasSupervisionRfsDfUsbFree = _ChasSupervisionRfsDfUsbFree_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 8, 1, 4),
    _ChasSupervisionRfsDfUsbFree_Type()
)
chasSupervisionRfsDfUsbFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfUsbFree.setStatus("current")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfUsbFree.setUnits("kb")
_ChasSupervisionRfsDfUsbSize_Type = Unsigned32
_ChasSupervisionRfsDfUsbSize_Object = MibTableColumn
chasSupervisionRfsDfUsbSize = _ChasSupervisionRfsDfUsbSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 8, 1, 5),
    _ChasSupervisionRfsDfUsbSize_Type()
)
chasSupervisionRfsDfUsbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfUsbSize.setStatus("current")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfUsbSize.setUnits("kb")
_ChasSupervisionFlashMemTable_Object = MibTable
chasSupervisionFlashMemTable = _ChasSupervisionFlashMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    chasSupervisionFlashMemTable.setStatus("current")
_ChasSupervisionFlashMemEntry_Object = MibTableRow
chasSupervisionFlashMemEntry = _ChasSupervisionFlashMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 9, 1)
)
chasSupervisionFlashMemEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionSlot"),
)
if mibBuilder.loadTexts:
    chasSupervisionFlashMemEntry.setStatus("current")


class _ChasSupervisionSlot_Type(Integer32):
    """Custom type chasSupervisionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChasSupervisionSlot_Type.__name__ = "Integer32"
_ChasSupervisionSlot_Object = MibTableColumn
chasSupervisionSlot = _ChasSupervisionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 9, 1, 1),
    _ChasSupervisionSlot_Type()
)
chasSupervisionSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasSupervisionSlot.setStatus("current")
_ChasSupervisionFlashSize_Type = Unsigned32
_ChasSupervisionFlashSize_Object = MibTableColumn
chasSupervisionFlashSize = _ChasSupervisionFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 9, 1, 2),
    _ChasSupervisionFlashSize_Type()
)
chasSupervisionFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionFlashSize.setStatus("current")
_ChasSupervisionFlashFree_Type = Unsigned32
_ChasSupervisionFlashFree_Object = MibTableColumn
chasSupervisionFlashFree = _ChasSupervisionFlashFree_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 9, 1, 3),
    _ChasSupervisionFlashFree_Type()
)
chasSupervisionFlashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionFlashFree.setStatus("current")


class _ChasSupervisionFlashUsed_Type(Integer32):
    """Custom type chasSupervisionFlashUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChasSupervisionFlashUsed_Type.__name__ = "Integer32"
_ChasSupervisionFlashUsed_Object = MibTableColumn
chasSupervisionFlashUsed = _ChasSupervisionFlashUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 9, 1, 4),
    _ChasSupervisionFlashUsed_Type()
)
chasSupervisionFlashUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionFlashUsed.setStatus("current")
_ChasSupervisionCmmCertifiedTable_Object = MibTable
chasSupervisionCmmCertifiedTable = _ChasSupervisionCmmCertifiedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    chasSupervisionCmmCertifiedTable.setStatus("current")
_ChasSupervisionCmmCertifiedEntry_Object = MibTableRow
chasSupervisionCmmCertifiedEntry = _ChasSupervisionCmmCertifiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 10, 1)
)
chasSupervisionCmmCertifiedEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionCmmNum"),
)
if mibBuilder.loadTexts:
    chasSupervisionCmmCertifiedEntry.setStatus("current")


class _ChasSupervisionCmmNum_Type(Integer32):
    """Custom type chasSupervisionCmmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChasSupervisionCmmNum_Type.__name__ = "Integer32"
_ChasSupervisionCmmNum_Object = MibTableColumn
chasSupervisionCmmNum = _ChasSupervisionCmmNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 10, 1, 1),
    _ChasSupervisionCmmNum_Type()
)
chasSupervisionCmmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasSupervisionCmmNum.setStatus("current")


class _ChasSupervisionCmmCertifiedStatus_Type(Integer32):
    """Custom type chasSupervisionCmmCertifiedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notPresent", 0),
          ("yes", 1))
    )


_ChasSupervisionCmmCertifiedStatus_Type.__name__ = "Integer32"
_ChasSupervisionCmmCertifiedStatus_Object = MibTableColumn
chasSupervisionCmmCertifiedStatus = _ChasSupervisionCmmCertifiedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 10, 1, 2),
    _ChasSupervisionCmmCertifiedStatus_Type()
)
chasSupervisionCmmCertifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionCmmCertifiedStatus.setStatus("current")
_AlaChasEntPhysFanTable_Object = MibTable
alaChasEntPhysFanTable = _AlaChasEntPhysFanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaChasEntPhysFanTable.setStatus("current")
_AlaChasEntPhysFanEntry_Object = MibTableRow
alaChasEntPhysFanEntry = _AlaChasEntPhysFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 11, 1)
)
alaChasEntPhysFanEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasEntPhysFanLocalIndex"),
)
if mibBuilder.loadTexts:
    alaChasEntPhysFanEntry.setStatus("current")


class _AlaChasEntPhysFanLocalIndex_Type(Integer32):
    """Custom type alaChasEntPhysFanLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaChasEntPhysFanLocalIndex_Type.__name__ = "Integer32"
_AlaChasEntPhysFanLocalIndex_Object = MibTableColumn
alaChasEntPhysFanLocalIndex = _AlaChasEntPhysFanLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 11, 1, 1),
    _AlaChasEntPhysFanLocalIndex_Type()
)
alaChasEntPhysFanLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaChasEntPhysFanLocalIndex.setStatus("current")


class _AlaChasEntPhysFanStatus_Type(Integer32):
    """Custom type alaChasEntPhysFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 0),
          ("notRunning", 1),
          ("running", 2))
    )


_AlaChasEntPhysFanStatus_Type.__name__ = "Integer32"
_AlaChasEntPhysFanStatus_Object = MibTableColumn
alaChasEntPhysFanStatus = _AlaChasEntPhysFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 11, 1, 2),
    _AlaChasEntPhysFanStatus_Type()
)
alaChasEntPhysFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasEntPhysFanStatus.setStatus("current")


class _AlaChasEntPhysFanAirflow_Type(Integer32):
    """Custom type alaChasEntPhysFanAirflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frontToRear", 0),
          ("notApplicable", 2),
          ("rearToFront", 1))
    )


_AlaChasEntPhysFanAirflow_Type.__name__ = "Integer32"
_AlaChasEntPhysFanAirflow_Object = MibTableColumn
alaChasEntPhysFanAirflow = _AlaChasEntPhysFanAirflow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 11, 1, 3),
    _AlaChasEntPhysFanAirflow_Type()
)
alaChasEntPhysFanAirflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasEntPhysFanAirflow.setStatus("current")
_ChassisTrapsObj_ObjectIdentity = ObjectIdentity
chassisTrapsObj = _ChassisTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13)
)
_ChassisTrapsStrLevel_Type = ChassisTrapsStrLevel
_ChassisTrapsStrLevel_Object = MibScalar
chassisTrapsStrLevel = _ChassisTrapsStrLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 1),
    _ChassisTrapsStrLevel_Type()
)
chassisTrapsStrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrLevel.setStatus("current")
_ChassisTrapsStrAppID_Type = ChassisTrapsStrAppID
_ChassisTrapsStrAppID_Object = MibScalar
chassisTrapsStrAppID = _ChassisTrapsStrAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 2),
    _ChassisTrapsStrAppID_Type()
)
chassisTrapsStrAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrAppID.setStatus("current")
_ChassisTrapsStrSnapID_Type = ChassisTrapsStrSnapID
_ChassisTrapsStrSnapID_Object = MibScalar
chassisTrapsStrSnapID = _ChassisTrapsStrSnapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 3),
    _ChassisTrapsStrSnapID_Type()
)
chassisTrapsStrSnapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrSnapID.setStatus("current")


class _ChassisTrapsStrfileName_Type(SnmpAdminString):
    """Custom type chassisTrapsStrfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ChassisTrapsStrfileName_Type.__name__ = "SnmpAdminString"
_ChassisTrapsStrfileName_Object = MibScalar
chassisTrapsStrfileName = _ChassisTrapsStrfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 4),
    _ChassisTrapsStrfileName_Type()
)
chassisTrapsStrfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrfileName.setStatus("current")
_ChassisTrapsStrfileLineNb_Type = ChassisTrapsStrfileLineNb
_ChassisTrapsStrfileLineNb_Object = MibScalar
chassisTrapsStrfileLineNb = _ChassisTrapsStrfileLineNb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 5),
    _ChassisTrapsStrfileLineNb_Type()
)
chassisTrapsStrfileLineNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrfileLineNb.setStatus("current")
_ChassisTrapsStrErrorNb_Type = ChassisTrapsStrErrorNb
_ChassisTrapsStrErrorNb_Object = MibScalar
chassisTrapsStrErrorNb = _ChassisTrapsStrErrorNb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 6),
    _ChassisTrapsStrErrorNb_Type()
)
chassisTrapsStrErrorNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrErrorNb.setStatus("current")


class _ChassisTrapsStrcomments_Type(SnmpAdminString):
    """Custom type chassisTrapsStrcomments based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ChassisTrapsStrcomments_Type.__name__ = "SnmpAdminString"
_ChassisTrapsStrcomments_Object = MibScalar
chassisTrapsStrcomments = _ChassisTrapsStrcomments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 7),
    _ChassisTrapsStrcomments_Type()
)
chassisTrapsStrcomments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrcomments.setStatus("current")
_ChassisTrapsStrdataInfo_Type = ChassisTrapsStrdataInfo
_ChassisTrapsStrdataInfo_Object = MibScalar
chassisTrapsStrdataInfo = _ChassisTrapsStrdataInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 8),
    _ChassisTrapsStrdataInfo_Type()
)
chassisTrapsStrdataInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrdataInfo.setStatus("current")
_ChassisTrapsObjectType_Type = ChassisTrapsObjectType
_ChassisTrapsObjectType_Object = MibScalar
chassisTrapsObjectType = _ChassisTrapsObjectType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 9),
    _ChassisTrapsObjectType_Type()
)
chassisTrapsObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsObjectType.setStatus("current")
_ChassisTrapsObjectNumber_Type = ChassisTrapsObjectNumber
_ChassisTrapsObjectNumber_Object = MibScalar
chassisTrapsObjectNumber = _ChassisTrapsObjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 10),
    _ChassisTrapsObjectNumber_Type()
)
chassisTrapsObjectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsObjectNumber.setStatus("current")
_ChassisTrapsAlertNumber_Type = ChassisTrapsAlertNumber
_ChassisTrapsAlertNumber_Object = MibScalar
chassisTrapsAlertNumber = _ChassisTrapsAlertNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 11),
    _ChassisTrapsAlertNumber_Type()
)
chassisTrapsAlertNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsAlertNumber.setStatus("current")


class _ChassisTrapsAlertDescr_Type(SnmpAdminString):
    """Custom type chassisTrapsAlertDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ChassisTrapsAlertDescr_Type.__name__ = "SnmpAdminString"
_ChassisTrapsAlertDescr_Object = MibScalar
chassisTrapsAlertDescr = _ChassisTrapsAlertDescr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 12),
    _ChassisTrapsAlertDescr_Type()
)
chassisTrapsAlertDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsAlertDescr.setStatus("current")
_PhysicalIndex_Type = PhysicalIndex
_PhysicalIndex_Object = MibScalar
physicalIndex = _PhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 13),
    _PhysicalIndex_Type()
)
physicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalIndex.setStatus("current")


class _ChasTrapsNiRqstdBpsSysPower_Type(Integer32):
    """Custom type chasTrapsNiRqstdBpsSysPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_ChasTrapsNiRqstdBpsSysPower_Type.__name__ = "Integer32"
_ChasTrapsNiRqstdBpsSysPower_Object = MibScalar
chasTrapsNiRqstdBpsSysPower = _ChasTrapsNiRqstdBpsSysPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 14),
    _ChasTrapsNiRqstdBpsSysPower_Type()
)
chasTrapsNiRqstdBpsSysPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapsNiRqstdBpsSysPower.setStatus("current")


class _ChasTrapsNiGrantdBpsSysPower_Type(Integer32):
    """Custom type chasTrapsNiGrantdBpsSysPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_ChasTrapsNiGrantdBpsSysPower_Type.__name__ = "Integer32"
_ChasTrapsNiGrantdBpsSysPower_Object = MibScalar
chasTrapsNiGrantdBpsSysPower = _ChasTrapsNiGrantdBpsSysPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 15),
    _ChasTrapsNiGrantdBpsSysPower_Type()
)
chasTrapsNiGrantdBpsSysPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapsNiGrantdBpsSysPower.setStatus("current")


class _ChasTrapBPSShelfId_Type(Integer32):
    """Custom type chasTrapBPSShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ChasTrapBPSShelfId_Type.__name__ = "Integer32"
_ChasTrapBPSShelfId_Object = MibScalar
chasTrapBPSShelfId = _ChasTrapBPSShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 16),
    _ChasTrapBPSShelfId_Type()
)
chasTrapBPSShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapBPSShelfId.setStatus("current")
_ChasTrapsBPSPowerSupply_Type = ChasTrapsBPSPowerSupply
_ChasTrapsBPSPowerSupply_Object = MibScalar
chasTrapsBPSPowerSupply = _ChasTrapsBPSPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 17),
    _ChasTrapsBPSPowerSupply_Type()
)
chasTrapsBPSPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapsBPSPowerSupply.setStatus("current")
_ChasTrapsBPSEventAlert_Type = ChasTrapsBPSEventAlert
_ChasTrapsBPSEventAlert_Object = MibScalar
chasTrapsBPSEventAlert = _ChasTrapsBPSEventAlert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 18),
    _ChasTrapsBPSEventAlert_Type()
)
chasTrapsBPSEventAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapsBPSEventAlert.setStatus("current")
_ChasTrapsBPSSystemFETChange_Type = ChasTrapsBPSFetState
_ChasTrapsBPSSystemFETChange_Object = MibScalar
chasTrapsBPSSystemFETChange = _ChasTrapsBPSSystemFETChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 19),
    _ChasTrapsBPSSystemFETChange_Type()
)
chasTrapsBPSSystemFETChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapsBPSSystemFETChange.setStatus("current")
_ChasTrapsBPSPoeFETChange_Type = ChasTrapsBPSFetState
_ChasTrapsBPSPoeFETChange_Object = MibScalar
chasTrapsBPSPoeFETChange = _ChasTrapsBPSPoeFETChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 13, 20),
    _ChasTrapsBPSPoeFETChange_Type()
)
chasTrapsBPSPoeFETChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapsBPSPoeFETChange.setStatus("current")
_AlaChasBpsObjects_ObjectIdentity = ObjectIdentity
alaChasBpsObjects = _AlaChasBpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14)
)
_AlaChasBpsFwTable_Object = MibTable
alaChasBpsFwTable = _AlaChasBpsFwTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    alaChasBpsFwTable.setStatus("current")
_AlaChasBpsFwEntry_Object = MibTableRow
alaChasBpsFwEntry = _AlaChasBpsFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 1, 1)
)
alaChasBpsFwEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsShelfId"),
)
if mibBuilder.loadTexts:
    alaChasBpsFwEntry.setStatus("current")
_AlaChasBpsShelfId_Type = AlaChasBpsShelfId
_AlaChasBpsShelfId_Object = MibTableColumn
alaChasBpsShelfId = _AlaChasBpsShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 1, 1, 1),
    _AlaChasBpsShelfId_Type()
)
alaChasBpsShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaChasBpsShelfId.setStatus("current")


class _AlaChasBpsUpdateFirmware_Type(Integer32):
    """Custom type alaChasBpsUpdateFirmware based on Integer32"""
    defaultValue = 1

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


_AlaChasBpsUpdateFirmware_Type.__name__ = "Integer32"
_AlaChasBpsUpdateFirmware_Object = MibTableColumn
alaChasBpsUpdateFirmware = _AlaChasBpsUpdateFirmware_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 1, 1, 2),
    _AlaChasBpsUpdateFirmware_Type()
)
alaChasBpsUpdateFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaChasBpsUpdateFirmware.setStatus("current")


class _AlaChasBpsCpldRev_Type(SnmpAdminString):
    """Custom type alaChasBpsCpldRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AlaChasBpsCpldRev_Type.__name__ = "SnmpAdminString"
_AlaChasBpsCpldRev_Object = MibTableColumn
alaChasBpsCpldRev = _AlaChasBpsCpldRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 1, 1, 3),
    _AlaChasBpsCpldRev_Type()
)
alaChasBpsCpldRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsCpldRev.setStatus("current")


class _AlaChasBpsMmcuRev_Type(SnmpAdminString):
    """Custom type alaChasBpsMmcuRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AlaChasBpsMmcuRev_Type.__name__ = "SnmpAdminString"
_AlaChasBpsMmcuRev_Object = MibTableColumn
alaChasBpsMmcuRev = _AlaChasBpsMmcuRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 1, 1, 4),
    _AlaChasBpsMmcuRev_Type()
)
alaChasBpsMmcuRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsMmcuRev.setStatus("current")


class _AlaChasBpsCmcuRev_Type(SnmpAdminString):
    """Custom type alaChasBpsCmcuRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AlaChasBpsCmcuRev_Type.__name__ = "SnmpAdminString"
_AlaChasBpsCmcuRev_Object = MibTableColumn
alaChasBpsCmcuRev = _AlaChasBpsCmcuRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 1, 1, 5),
    _AlaChasBpsCmcuRev_Type()
)
alaChasBpsCmcuRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsCmcuRev.setStatus("current")
_AlaChasBpsConnectorPriorityTable_Object = MibTable
alaChasBpsConnectorPriorityTable = _AlaChasBpsConnectorPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    alaChasBpsConnectorPriorityTable.setStatus("current")
_AlaChasBpsConnectorPriorityEntry_Object = MibTableRow
alaChasBpsConnectorPriorityEntry = _AlaChasBpsConnectorPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 2, 1)
)
alaChasBpsConnectorPriorityEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsChassisId"),
)
if mibBuilder.loadTexts:
    alaChasBpsConnectorPriorityEntry.setStatus("current")


class _AlaChasBpsChassisId_Type(Integer32):
    """Custom type alaChasBpsChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlaChasBpsChassisId_Type.__name__ = "Integer32"
_AlaChasBpsChassisId_Object = MibTableColumn
alaChasBpsChassisId = _AlaChasBpsChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 2, 1, 1),
    _AlaChasBpsChassisId_Type()
)
alaChasBpsChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaChasBpsChassisId.setStatus("current")
_AlaChasBpsConnectorShelfId_Type = AlaChasBpsShelfId
_AlaChasBpsConnectorShelfId_Object = MibTableColumn
alaChasBpsConnectorShelfId = _AlaChasBpsConnectorShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 2, 1, 2),
    _AlaChasBpsConnectorShelfId_Type()
)
alaChasBpsConnectorShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsConnectorShelfId.setStatus("current")


class _AlaChasBpsConnectorPriority_Type(Integer32):
    """Custom type alaChasBpsConnectorPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AlaChasBpsConnectorPriority_Type.__name__ = "Integer32"
_AlaChasBpsConnectorPriority_Object = MibTableColumn
alaChasBpsConnectorPriority = _AlaChasBpsConnectorPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 2, 1, 3),
    _AlaChasBpsConnectorPriority_Type()
)
alaChasBpsConnectorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaChasBpsConnectorPriority.setStatus("current")


class _AlaChasBpsConnectorNum_Type(SnmpAdminString):
    """Custom type alaChasBpsConnectorNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AlaChasBpsConnectorNum_Type.__name__ = "SnmpAdminString"
_AlaChasBpsConnectorNum_Object = MibTableColumn
alaChasBpsConnectorNum = _AlaChasBpsConnectorNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 2, 1, 4),
    _AlaChasBpsConnectorNum_Type()
)
alaChasBpsConnectorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsConnectorNum.setStatus("current")


class _AlaChasBpsSerialNum_Type(SnmpAdminString):
    """Custom type alaChasBpsSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AlaChasBpsSerialNum_Type.__name__ = "SnmpAdminString"
_AlaChasBpsSerialNum_Object = MibTableColumn
alaChasBpsSerialNum = _AlaChasBpsSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 2, 1, 5),
    _AlaChasBpsSerialNum_Type()
)
alaChasBpsSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsSerialNum.setStatus("current")
_AlaChasBpsModeTable_Object = MibTable
alaChasBpsModeTable = _AlaChasBpsModeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 3)
)
if mibBuilder.loadTexts:
    alaChasBpsModeTable.setStatus("current")
_AlaChasBpsModeEntry_Object = MibTableRow
alaChasBpsModeEntry = _AlaChasBpsModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 3, 1)
)
alaChasBpsModeEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsShelfId"),
)
if mibBuilder.loadTexts:
    alaChasBpsModeEntry.setStatus("current")


class _AlaChasBpsMode_Type(Integer32):
    """Custom type alaChasBpsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("notApplicable", 3),
          ("single", 1))
    )


_AlaChasBpsMode_Type.__name__ = "Integer32"
_AlaChasBpsMode_Object = MibTableColumn
alaChasBpsMode = _AlaChasBpsMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 3, 1, 1),
    _AlaChasBpsMode_Type()
)
alaChasBpsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaChasBpsMode.setStatus("current")
_AlaChasBpsPowerSupplyTable_Object = MibTable
alaChasBpsPowerSupplyTable = _AlaChasBpsPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4)
)
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyTable.setStatus("current")
_AlaChasBpsPowerSupplyEntry_Object = MibTableRow
alaChasBpsPowerSupplyEntry = _AlaChasBpsPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1)
)
alaChasBpsPowerSupplyEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyShelfId"),
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyEntry.setStatus("current")
_AlaChasBpsPowerSupplyShelfId_Type = AlaChasBpsShelfId
_AlaChasBpsPowerSupplyShelfId_Object = MibTableColumn
alaChasBpsPowerSupplyShelfId = _AlaChasBpsPowerSupplyShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 1),
    _AlaChasBpsPowerSupplyShelfId_Type()
)
alaChasBpsPowerSupplyShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyShelfId.setStatus("current")


class _AlaChasBpsPowerSupplyIndex_Type(Integer32):
    """Custom type alaChasBpsPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AlaChasBpsPowerSupplyIndex_Type.__name__ = "Integer32"
_AlaChasBpsPowerSupplyIndex_Object = MibTableColumn
alaChasBpsPowerSupplyIndex = _AlaChasBpsPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 2),
    _AlaChasBpsPowerSupplyIndex_Type()
)
alaChasBpsPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyIndex.setStatus("current")


class _AlaChasBpsPowerSupplyName_Type(SnmpAdminString):
    """Custom type alaChasBpsPowerSupplyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaChasBpsPowerSupplyName_Type.__name__ = "SnmpAdminString"
_AlaChasBpsPowerSupplyName_Object = MibTableColumn
alaChasBpsPowerSupplyName = _AlaChasBpsPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 3),
    _AlaChasBpsPowerSupplyName_Type()
)
alaChasBpsPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyName.setStatus("current")


class _AlaChasBpsPowerSupplyDescr_Type(SnmpAdminString):
    """Custom type alaChasBpsPowerSupplyDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaChasBpsPowerSupplyDescr_Type.__name__ = "SnmpAdminString"
_AlaChasBpsPowerSupplyDescr_Object = MibTableColumn
alaChasBpsPowerSupplyDescr = _AlaChasBpsPowerSupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 4),
    _AlaChasBpsPowerSupplyDescr_Type()
)
alaChasBpsPowerSupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyDescr.setStatus("current")


class _AlaChasBpsPowerSupplyModuleType_Type(SnmpAdminString):
    """Custom type alaChasBpsPowerSupplyModuleType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaChasBpsPowerSupplyModuleType_Type.__name__ = "SnmpAdminString"
_AlaChasBpsPowerSupplyModuleType_Object = MibTableColumn
alaChasBpsPowerSupplyModuleType = _AlaChasBpsPowerSupplyModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 5),
    _AlaChasBpsPowerSupplyModuleType_Type()
)
alaChasBpsPowerSupplyModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyModuleType.setStatus("current")


class _AlaChasBpsPowerSupplyPartNumber_Type(SnmpAdminString):
    """Custom type alaChasBpsPowerSupplyPartNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlaChasBpsPowerSupplyPartNumber_Type.__name__ = "SnmpAdminString"
_AlaChasBpsPowerSupplyPartNumber_Object = MibTableColumn
alaChasBpsPowerSupplyPartNumber = _AlaChasBpsPowerSupplyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 6),
    _AlaChasBpsPowerSupplyPartNumber_Type()
)
alaChasBpsPowerSupplyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyPartNumber.setStatus("current")


class _AlaChasBpsPowerSupplyHardwareRev_Type(SnmpAdminString):
    """Custom type alaChasBpsPowerSupplyHardwareRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AlaChasBpsPowerSupplyHardwareRev_Type.__name__ = "SnmpAdminString"
_AlaChasBpsPowerSupplyHardwareRev_Object = MibTableColumn
alaChasBpsPowerSupplyHardwareRev = _AlaChasBpsPowerSupplyHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 7),
    _AlaChasBpsPowerSupplyHardwareRev_Type()
)
alaChasBpsPowerSupplyHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyHardwareRev.setStatus("current")


class _AlaChasBpsPowerSupplySerialNum_Type(SnmpAdminString):
    """Custom type alaChasBpsPowerSupplySerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaChasBpsPowerSupplySerialNum_Type.__name__ = "SnmpAdminString"
_AlaChasBpsPowerSupplySerialNum_Object = MibTableColumn
alaChasBpsPowerSupplySerialNum = _AlaChasBpsPowerSupplySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 8),
    _AlaChasBpsPowerSupplySerialNum_Type()
)
alaChasBpsPowerSupplySerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplySerialNum.setStatus("current")


class _AlaChasBpsPowerSupplyMfgDate_Type(SnmpAdminString):
    """Custom type alaChasBpsPowerSupplyMfgDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AlaChasBpsPowerSupplyMfgDate_Type.__name__ = "SnmpAdminString"
_AlaChasBpsPowerSupplyMfgDate_Object = MibTableColumn
alaChasBpsPowerSupplyMfgDate = _AlaChasBpsPowerSupplyMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 9),
    _AlaChasBpsPowerSupplyMfgDate_Type()
)
alaChasBpsPowerSupplyMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyMfgDate.setStatus("current")


class _AlaChasBpsPowerSupplyOperStatus_Type(Integer32):
    """Custom type alaChasBpsPowerSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_AlaChasBpsPowerSupplyOperStatus_Type.__name__ = "Integer32"
_AlaChasBpsPowerSupplyOperStatus_Object = MibTableColumn
alaChasBpsPowerSupplyOperStatus = _AlaChasBpsPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 10),
    _AlaChasBpsPowerSupplyOperStatus_Type()
)
alaChasBpsPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyOperStatus.setStatus("current")


class _AlaChasBpsPowerSupplyPowerProv_Type(Integer32):
    """Custom type alaChasBpsPowerSupplyPowerProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AlaChasBpsPowerSupplyPowerProv_Type.__name__ = "Integer32"
_AlaChasBpsPowerSupplyPowerProv_Object = MibTableColumn
alaChasBpsPowerSupplyPowerProv = _AlaChasBpsPowerSupplyPowerProv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 4, 1, 11),
    _AlaChasBpsPowerSupplyPowerProv_Type()
)
alaChasBpsPowerSupplyPowerProv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyPowerProv.setStatus("current")
_AlaChasBpsTotalPowerAllocTable_Object = MibTable
alaChasBpsTotalPowerAllocTable = _AlaChasBpsTotalPowerAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 5)
)
if mibBuilder.loadTexts:
    alaChasBpsTotalPowerAllocTable.setStatus("current")
_AlaChasBpsTotalPowerAllocEntry_Object = MibTableRow
alaChasBpsTotalPowerAllocEntry = _AlaChasBpsTotalPowerAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 5, 1)
)
alaChasBpsTotalPowerAllocEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsShelfId"),
)
if mibBuilder.loadTexts:
    alaChasBpsTotalPowerAllocEntry.setStatus("current")


class _AlaChasBpsSysTotalAvailablePower_Type(Integer32):
    """Custom type alaChasBpsSysTotalAvailablePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AlaChasBpsSysTotalAvailablePower_Type.__name__ = "Integer32"
_AlaChasBpsSysTotalAvailablePower_Object = MibTableColumn
alaChasBpsSysTotalAvailablePower = _AlaChasBpsSysTotalAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 5, 1, 1),
    _AlaChasBpsSysTotalAvailablePower_Type()
)
alaChasBpsSysTotalAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsSysTotalAvailablePower.setStatus("current")


class _AlaChasBpsSysTotalAllocation_Type(Integer32):
    """Custom type alaChasBpsSysTotalAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AlaChasBpsSysTotalAllocation_Type.__name__ = "Integer32"
_AlaChasBpsSysTotalAllocation_Object = MibTableColumn
alaChasBpsSysTotalAllocation = _AlaChasBpsSysTotalAllocation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 5, 1, 2),
    _AlaChasBpsSysTotalAllocation_Type()
)
alaChasBpsSysTotalAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsSysTotalAllocation.setStatus("current")


class _AlaChasBpsPoeTotalAvailablePower_Type(Integer32):
    """Custom type alaChasBpsPoeTotalAvailablePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_AlaChasBpsPoeTotalAvailablePower_Type.__name__ = "Integer32"
_AlaChasBpsPoeTotalAvailablePower_Object = MibTableColumn
alaChasBpsPoeTotalAvailablePower = _AlaChasBpsPoeTotalAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 5, 1, 3),
    _AlaChasBpsPoeTotalAvailablePower_Type()
)
alaChasBpsPoeTotalAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPoeTotalAvailablePower.setStatus("current")


class _AlaChasBpsPoeTotalAllocation_Type(Integer32):
    """Custom type alaChasBpsPoeTotalAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_AlaChasBpsPoeTotalAllocation_Type.__name__ = "Integer32"
_AlaChasBpsPoeTotalAllocation_Object = MibTableColumn
alaChasBpsPoeTotalAllocation = _AlaChasBpsPoeTotalAllocation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 1, 14, 5, 1, 4),
    _AlaChasBpsPoeTotalAllocation_Type()
)
alaChasBpsPoeTotalAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasBpsPoeTotalAllocation.setStatus("current")
_AlcatelIND1ChassisMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBConformance = _AlcatelIND1ChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBConformance.setStatus("current")
_AlcatelIND1ChassisMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBGroups = _AlcatelIND1ChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBGroups.setStatus("current")
_AlcatelIND1ChassisMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBCompliances = _AlcatelIND1ChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBCompliances.setStatus("current")

# Managed Objects groups

chasEntPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 2, 1, 1)
)
chasEntPhysicalGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAdminStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysOperStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysPower"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysModuleType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysPartNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusOk1"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusOk2"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusPrimaryCMM"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusSecondaryCMM"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusTemperature"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusFan"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusBackupPS"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusInternalPS"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusControl"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusFabric"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusPS"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAsic1Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAsic2Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAsic3Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAsic4Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAsic5Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAsic6Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysCpldRev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysDaughterFpga1Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysDaughterFpga2Rev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysNiNum"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysGbicNum"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysWaveLen"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysUbootRev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysUbootMinibootRev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysMacAddress"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysCpuModel"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAirflow"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysPowerUsed"))
)
if mibBuilder.loadTexts:
    chasEntPhysicalGroup.setStatus("current")

chassisTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 2, 1, 3)
)
chassisTemperatureGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasEntTempCurrent"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntTempDangerThreshold"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntTempStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntTempThreshold"))
)
if mibBuilder.loadTexts:
    chassisTemperatureGroup.setStatus("current")

chasControlModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 1)
)
chasControlModuleGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasControlActivateTimeout"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlVersionMngt"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlDelayedActivateTimer"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlCertifyStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlSynchronizationStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlAcrossCmmWorkingSynchroStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlAcrossCmmCertifiedSynchroStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlNextRunningVersion"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlCurrentRunningVersion"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlWorkingVersion"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlRedundancyTime"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlEmpIpAddress"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlEmpIpMask"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlChassisId"))
)
if mibBuilder.loadTexts:
    chasControlModuleGroup.setStatus("current")

chasControlRedundantGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 2)
)
chasControlRedundantGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasControlNumberOfTakeover"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlDelayedRebootTimer"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlDelayedResetAll"))
)
if mibBuilder.loadTexts:
    chasControlRedundantGroup.setStatus("current")

chasChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 3)
)
chasChassisGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasFreeSlots"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasPowerLeft"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNumberOfResets"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTempRange"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTempThreshold"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasDangerTempThreshold"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasPrimaryPhysicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasCPMAHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasCFMAHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasCPMBHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasCFMBHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasCFMCHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasCFMDHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasFTAHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasFTBHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI1HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI2HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI3HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI4HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI5HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI6HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI7HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNI8HardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasPowerSupplyRedundancy"))
)
if mibBuilder.loadTexts:
    chasChassisGroup.setStatus("current")

chasControlReloadStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 4)
)
chasControlReloadStatusGroup.setObjects(
    ("ALCATEL-IND1-CHASSIS-MIB", "chasControlReloadStatus")
)
if mibBuilder.loadTexts:
    chasControlReloadStatusGroup.setStatus("current")

chasGlobalControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 5)
)
chasGlobalControlGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlDelayedResetAll"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlLongCommand"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlLongCommandStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlUpdateFirmware"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlUpdateSlot"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlUpdateFilename"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlUpdateStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlConfirmOperation"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlConfirmMessage"))
)
if mibBuilder.loadTexts:
    chasGlobalControlGroup.setStatus("current")

alaChasEntPhysFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 7)
)
alaChasEntPhysFanGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "alaChasEntPhysFanStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasEntPhysFanAirflow"))
)
if mibBuilder.loadTexts:
    alaChasEntPhysFanGroup.setStatus("current")

alaChasNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 9)
)
alaChasNotificationObjectGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrLevel"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrAppID"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrSnapID"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrfileName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrfileLineNb"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrErrorNb"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrcomments"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrdataInfo"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlertNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlertDescr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsNiRqstdBpsSysPower"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsNiGrantdBpsSysPower"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapBPSShelfId"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSPowerSupply"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSEventAlert"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSSystemFETChange"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSPoeFETChange"))
)
if mibBuilder.loadTexts:
    alaChasNotificationObjectGroup.setStatus("current")

chassisSupervisionRfsCommandsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 10)
)
chassisSupervisionRfsCommandsGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsSlot"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsCommand"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsSrcFileName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsDestFileName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsRlsDirName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsRlsFileName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsProcessingState"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsCommandsStatusCode"))
)
if mibBuilder.loadTexts:
    chassisSupervisionRfsCommandsGroup.setStatus("current")

chasSupervisionCmmCertifiedEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 11)
)
chasSupervisionCmmCertifiedEntryGroup.setObjects(
    ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionCmmCertifiedStatus")
)
if mibBuilder.loadTexts:
    chasSupervisionCmmCertifiedEntryGroup.setStatus("current")

chasSupervisionFlashMemEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 12)
)
chasSupervisionFlashMemEntryGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionFlashSize"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionFlashFree"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionFlashUsed"))
)
if mibBuilder.loadTexts:
    chasSupervisionFlashMemEntryGroup.setStatus("current")

chasSupervisionRfsDfEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 13)
)
chasSupervisionRfsDfEntryGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsDfFlashFree"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsDfFlashSize"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsDfUsbFree"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsDfUsbSize"))
)
if mibBuilder.loadTexts:
    chasSupervisionRfsDfEntryGroup.setStatus("current")

chasSupervisionRfsLsEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 14)
)
chasSupervisionRfsLsEntryGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsSlot"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsDirName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileSize"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileAttr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileDateTime"))
)
if mibBuilder.loadTexts:
    chasSupervisionRfsLsEntryGroup.setStatus("current")

alaChasBpsFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 15)
)
alaChasBpsFwGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsUpdateFirmware"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsCpldRev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsMmcuRev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsCmcuRev"))
)
if mibBuilder.loadTexts:
    alaChasBpsFwGroup.setStatus("current")

alaChasBpsConnectorPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 16)
)
alaChasBpsConnectorPriorityGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsConnectorShelfId"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsConnectorPriority"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsConnectorNum"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsSerialNum"))
)
if mibBuilder.loadTexts:
    alaChasBpsConnectorPriorityGroup.setStatus("current")

alaChasBpsModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 17)
)
alaChasBpsModeGroup.setObjects(
    ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsMode")
)
if mibBuilder.loadTexts:
    alaChasBpsModeGroup.setStatus("current")

alaChasBpsPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 18)
)
alaChasBpsPowerSupplyGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyDescr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyModuleType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyPartNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyHardwareRev"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplySerialNum"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyMfgDate"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyOperStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPowerSupplyPowerProv"))
)
if mibBuilder.loadTexts:
    alaChasBpsPowerSupplyGroup.setStatus("current")

alaChasBpsTotalPowerAllocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 19)
)
alaChasBpsTotalPowerAllocGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsSysTotalAvailablePower"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsSysTotalAllocation"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPoeTotalAvailablePower"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasBpsPoeTotalAllocation"))
)
if mibBuilder.loadTexts:
    alaChasBpsTotalPowerAllocGroup.setStatus("current")


# Notification objects

chassisTrapsStr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 0, 1)
)
chassisTrapsStr.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrLevel"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrAppID"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrSnapID"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrfileName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrfileLineNb"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrErrorNb"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrcomments"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrdataInfo"))
)
if mibBuilder.loadTexts:
    chassisTrapsStr.setStatus(
        "current"
    )

chassisTrapsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 0, 2)
)
chassisTrapsAlert.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlertNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlertDescr"))
)
if mibBuilder.loadTexts:
    chassisTrapsAlert.setStatus(
        "current"
    )

chassisTrapsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 0, 3)
)
chassisTrapsStateChange.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysOperStatus"))
)
if mibBuilder.loadTexts:
    chassisTrapsStateChange.setStatus(
        "current"
    )

chasTrapsBPSLessAllocSysPwr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 0, 4)
)
chasTrapsBPSLessAllocSysPwr.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsNiRqstdBpsSysPower"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsNiGrantdBpsSysPower"))
)
if mibBuilder.loadTexts:
    chasTrapsBPSLessAllocSysPwr.setStatus(
        "current"
    )

chasTrapsBPSStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 0, 5)
)
chasTrapsBPSStateChange.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasTrapBPSShelfId"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSPowerSupply"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSEventAlert"))
)
if mibBuilder.loadTexts:
    chasTrapsBPSStateChange.setStatus(
        "current"
    )

chasTrapsNiBPSFETStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 0, 6)
)
chasTrapsNiBPSFETStateChange.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSSystemFETChange"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSPoeFETChange"))
)
if mibBuilder.loadTexts:
    chasTrapsNiBPSFETStateChange.setStatus(
        "current"
    )


# Notifications groups

chassisPhysNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 2, 1, 2)
)
chassisPhysNotificationGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlert"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStateChange"))
)
if mibBuilder.loadTexts:
    chassisPhysNotificationGroup.setStatus(
        "current"
    )

chassisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 1, 6)
)
chassisNotificationGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlert"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSLessAllocSysPwr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsBPSStateChange"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTrapsNiBPSFETStateChange"))
)
if mibBuilder.loadTexts:
    chassisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1ChassisPhysMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBCompliance.setStatus(
        "current"
    )

alcatelIND1ChassisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-CHASSIS-MIB",
    **{"AlaChasBpsShelfId": AlaChasBpsShelfId,
       "ChasTrapsBPSPowerSupply": ChasTrapsBPSPowerSupply,
       "ChasTrapsBPSFetState": ChasTrapsBPSFetState,
       "ChasTrapsBPSEventAlert": ChasTrapsBPSEventAlert,
       "ChasEntPhysLed": ChasEntPhysLed,
       "ChassisTrapsStrLevel": ChassisTrapsStrLevel,
       "ChassisTrapsStrAppID": ChassisTrapsStrAppID,
       "ChassisTrapsStrSnapID": ChassisTrapsStrSnapID,
       "ChassisTrapsStrfileLineNb": ChassisTrapsStrfileLineNb,
       "ChassisTrapsStrErrorNb": ChassisTrapsStrErrorNb,
       "ChassisTrapsStrdataInfo": ChassisTrapsStrdataInfo,
       "ChassisTrapsObjectType": ChassisTrapsObjectType,
       "ChassisTrapsObjectNumber": ChassisTrapsObjectNumber,
       "ChassisTrapsAlertNumber": ChassisTrapsAlertNumber,
       "alcatelIND1ChassisPhysMIBObjects": alcatelIND1ChassisPhysMIBObjects,
       "chasEntPhysicalTable": chasEntPhysicalTable,
       "chasEntPhysicalEntry": chasEntPhysicalEntry,
       "chasEntPhysAdminStatus": chasEntPhysAdminStatus,
       "chasEntPhysOperStatus": chasEntPhysOperStatus,
       "chasEntPhysPower": chasEntPhysPower,
       "chasEntPhysModuleType": chasEntPhysModuleType,
       "chasEntPhysPartNumber": chasEntPhysPartNumber,
       "chasEntPhysLedStatusOk1": chasEntPhysLedStatusOk1,
       "chasEntPhysLedStatusOk2": chasEntPhysLedStatusOk2,
       "chasEntPhysLedStatusPrimaryCMM": chasEntPhysLedStatusPrimaryCMM,
       "chasEntPhysLedStatusSecondaryCMM": chasEntPhysLedStatusSecondaryCMM,
       "chasEntPhysLedStatusTemperature": chasEntPhysLedStatusTemperature,
       "chasEntPhysLedStatusFan": chasEntPhysLedStatusFan,
       "chasEntPhysLedStatusBackupPS": chasEntPhysLedStatusBackupPS,
       "chasEntPhysLedStatusInternalPS": chasEntPhysLedStatusInternalPS,
       "chasEntPhysLedStatusControl": chasEntPhysLedStatusControl,
       "chasEntPhysLedStatusFabric": chasEntPhysLedStatusFabric,
       "chasEntPhysLedStatusPS": chasEntPhysLedStatusPS,
       "chasEntPhysAsic1Rev": chasEntPhysAsic1Rev,
       "chasEntPhysAsic2Rev": chasEntPhysAsic2Rev,
       "chasEntPhysAsic3Rev": chasEntPhysAsic3Rev,
       "chasEntPhysAsic4Rev": chasEntPhysAsic4Rev,
       "chasEntPhysAsic5Rev": chasEntPhysAsic5Rev,
       "chasEntPhysAsic6Rev": chasEntPhysAsic6Rev,
       "chasEntPhysCpldRev": chasEntPhysCpldRev,
       "chasEntPhysDaughterFpga1Rev": chasEntPhysDaughterFpga1Rev,
       "chasEntPhysDaughterFpga2Rev": chasEntPhysDaughterFpga2Rev,
       "chasEntPhysNiNum": chasEntPhysNiNum,
       "chasEntPhysGbicNum": chasEntPhysGbicNum,
       "chasEntPhysWaveLen": chasEntPhysWaveLen,
       "chasEntPhysUbootRev": chasEntPhysUbootRev,
       "chasEntPhysUbootMinibootRev": chasEntPhysUbootMinibootRev,
       "chasEntPhysMacAddress": chasEntPhysMacAddress,
       "chasEntPhysCpuModel": chasEntPhysCpuModel,
       "chasEntPhysAirflow": chasEntPhysAirflow,
       "chasEntPhysPowerUsed": chasEntPhysPowerUsed,
       "chasEntTemperatureTable": chasEntTemperatureTable,
       "chasEntTemperatureEntry": chasEntTemperatureEntry,
       "chasEntTempCurrent": chasEntTempCurrent,
       "chasEntTempThreshold": chasEntTempThreshold,
       "chasEntTempDangerThreshold": chasEntTempDangerThreshold,
       "chasEntTempStatus": chasEntTempStatus,
       "alcatelIND1ChassisPhysMIBConformance": alcatelIND1ChassisPhysMIBConformance,
       "alcatelIND1ChassisPhysMIBGroups": alcatelIND1ChassisPhysMIBGroups,
       "chasEntPhysicalGroup": chasEntPhysicalGroup,
       "chassisPhysNotificationGroup": chassisPhysNotificationGroup,
       "chassisTemperatureGroup": chassisTemperatureGroup,
       "alcatelIND1ChassisPhysMIBCompliances": alcatelIND1ChassisPhysMIBCompliances,
       "alcatelIND1ChassisPhysMIBCompliance": alcatelIND1ChassisPhysMIBCompliance,
       "alcatelIND1ChassisMIB": alcatelIND1ChassisMIB,
       "alcatelIND1ChassisMIBNotifications": alcatelIND1ChassisMIBNotifications,
       "chassisTrapsStr": chassisTrapsStr,
       "chassisTrapsAlert": chassisTrapsAlert,
       "chassisTrapsStateChange": chassisTrapsStateChange,
       "chasTrapsBPSLessAllocSysPwr": chasTrapsBPSLessAllocSysPwr,
       "chasTrapsBPSStateChange": chasTrapsBPSStateChange,
       "chasTrapsNiBPSFETStateChange": chasTrapsNiBPSFETStateChange,
       "alcatelIND1ChassisMIBObjects": alcatelIND1ChassisMIBObjects,
       "chasControlModuleTable": chasControlModuleTable,
       "chasControlModuleEntry": chasControlModuleEntry,
       "chasControlActivateTimeout": chasControlActivateTimeout,
       "chasControlVersionMngt": chasControlVersionMngt,
       "chasControlDelayedActivateTimer": chasControlDelayedActivateTimer,
       "chasControlCertifyStatus": chasControlCertifyStatus,
       "chasControlSynchronizationStatus": chasControlSynchronizationStatus,
       "chasControlAcrossCmmWorkingSynchroStatus": chasControlAcrossCmmWorkingSynchroStatus,
       "chasControlAcrossCmmCertifiedSynchroStatus": chasControlAcrossCmmCertifiedSynchroStatus,
       "chasControlNextRunningVersion": chasControlNextRunningVersion,
       "chasControlCurrentRunningVersion": chasControlCurrentRunningVersion,
       "chasControlWorkingVersion": chasControlWorkingVersion,
       "chasControlRedundancyTime": chasControlRedundancyTime,
       "chasControlEmpIpAddress": chasControlEmpIpAddress,
       "chasControlEmpIpMask": chasControlEmpIpMask,
       "chasControlChassisId": chasControlChassisId,
       "chasControlRedundantTable": chasControlRedundantTable,
       "chasControlRedundantEntry": chasControlRedundantEntry,
       "chasControlNumberOfTakeover": chasControlNumberOfTakeover,
       "chasControlDelayedRebootTimer": chasControlDelayedRebootTimer,
       "chasControlDelayedResetAll": chasControlDelayedResetAll,
       "chasChassisTable": chasChassisTable,
       "chasChassisEntry": chasChassisEntry,
       "chasFreeSlots": chasFreeSlots,
       "chasPowerLeft": chasPowerLeft,
       "chasNumberOfResets": chasNumberOfResets,
       "chasTempRange": chasTempRange,
       "chasTempThreshold": chasTempThreshold,
       "chasDangerTempThreshold": chasDangerTempThreshold,
       "chasPrimaryPhysicalIndex": chasPrimaryPhysicalIndex,
       "chasCPMAHardwareBoardTemp": chasCPMAHardwareBoardTemp,
       "chasCFMAHardwareBoardTemp": chasCFMAHardwareBoardTemp,
       "chasCPMBHardwareBoardTemp": chasCPMBHardwareBoardTemp,
       "chasCFMBHardwareBoardTemp": chasCFMBHardwareBoardTemp,
       "chasCFMCHardwareBoardTemp": chasCFMCHardwareBoardTemp,
       "chasCFMDHardwareBoardTemp": chasCFMDHardwareBoardTemp,
       "chasFTAHardwareBoardTemp": chasFTAHardwareBoardTemp,
       "chasFTBHardwareBoardTemp": chasFTBHardwareBoardTemp,
       "chasNI1HardwareBoardTemp": chasNI1HardwareBoardTemp,
       "chasNI2HardwareBoardTemp": chasNI2HardwareBoardTemp,
       "chasNI3HardwareBoardTemp": chasNI3HardwareBoardTemp,
       "chasNI4HardwareBoardTemp": chasNI4HardwareBoardTemp,
       "chasNI5HardwareBoardTemp": chasNI5HardwareBoardTemp,
       "chasNI6HardwareBoardTemp": chasNI6HardwareBoardTemp,
       "chasNI7HardwareBoardTemp": chasNI7HardwareBoardTemp,
       "chasNI8HardwareBoardTemp": chasNI8HardwareBoardTemp,
       "chasPowerSupplyRedundancy": chasPowerSupplyRedundancy,
       "chasSupervisionRfsLsTable": chasSupervisionRfsLsTable,
       "chasSupervisionRfsLsEntry": chasSupervisionRfsLsEntry,
       "chasSupervisionRfsLsFileIndex": chasSupervisionRfsLsFileIndex,
       "chasSupervisionRfsLsSlot": chasSupervisionRfsLsSlot,
       "chasSupervisionRfsLsDirName": chasSupervisionRfsLsDirName,
       "chasSupervisionRfsLsFileName": chasSupervisionRfsLsFileName,
       "chasSupervisionRfsLsFileType": chasSupervisionRfsLsFileType,
       "chasSupervisionRfsLsFileSize": chasSupervisionRfsLsFileSize,
       "chasSupervisionRfsLsFileAttr": chasSupervisionRfsLsFileAttr,
       "chasSupervisionRfsLsFileDateTime": chasSupervisionRfsLsFileDateTime,
       "alcatelIND1ChassisSupervisionRfsCommands": alcatelIND1ChassisSupervisionRfsCommands,
       "chasSupervisionRfsCommandsSlot": chasSupervisionRfsCommandsSlot,
       "chasSupervisionRfsCommandsCommand": chasSupervisionRfsCommandsCommand,
       "chasSupervisionRfsCommandsSrcFileName": chasSupervisionRfsCommandsSrcFileName,
       "chasSupervisionRfsCommandsDestFileName": chasSupervisionRfsCommandsDestFileName,
       "chasSupervisionRfsCommandsRlsDirName": chasSupervisionRfsCommandsRlsDirName,
       "chasSupervisionRfsCommandsRlsFileName": chasSupervisionRfsCommandsRlsFileName,
       "chasSupervisionRfsCommandsProcessingState": chasSupervisionRfsCommandsProcessingState,
       "chasSupervisionRfsCommandsStatusCode": chasSupervisionRfsCommandsStatusCode,
       "chasControlReloadStatusTable": chasControlReloadStatusTable,
       "chasControlReloadEntry": chasControlReloadEntry,
       "chasControlReloadIndex": chasControlReloadIndex,
       "chasControlReloadStatus": chasControlReloadStatus,
       "chasGlobalControl": chasGlobalControl,
       "chasGlobalControlDelayedResetAll": chasGlobalControlDelayedResetAll,
       "chasGlobalControlLongCommand": chasGlobalControlLongCommand,
       "chasGlobalControlLongCommandStatus": chasGlobalControlLongCommandStatus,
       "chasGlobalControlUpdateFirmware": chasGlobalControlUpdateFirmware,
       "chasGlobalControlUpdateSlot": chasGlobalControlUpdateSlot,
       "chasGlobalControlUpdateFilename": chasGlobalControlUpdateFilename,
       "chasGlobalControlUpdateStatus": chasGlobalControlUpdateStatus,
       "chasGlobalControlConfirmOperation": chasGlobalControlConfirmOperation,
       "chasGlobalControlConfirmMessage": chasGlobalControlConfirmMessage,
       "chasSupervisionRfsDfTable": chasSupervisionRfsDfTable,
       "chasSupervisionRfsDfEntry": chasSupervisionRfsDfEntry,
       "chasSupervisionRfsDfSlot": chasSupervisionRfsDfSlot,
       "chasSupervisionRfsDfFlashFree": chasSupervisionRfsDfFlashFree,
       "chasSupervisionRfsDfFlashSize": chasSupervisionRfsDfFlashSize,
       "chasSupervisionRfsDfUsbFree": chasSupervisionRfsDfUsbFree,
       "chasSupervisionRfsDfUsbSize": chasSupervisionRfsDfUsbSize,
       "chasSupervisionFlashMemTable": chasSupervisionFlashMemTable,
       "chasSupervisionFlashMemEntry": chasSupervisionFlashMemEntry,
       "chasSupervisionSlot": chasSupervisionSlot,
       "chasSupervisionFlashSize": chasSupervisionFlashSize,
       "chasSupervisionFlashFree": chasSupervisionFlashFree,
       "chasSupervisionFlashUsed": chasSupervisionFlashUsed,
       "chasSupervisionCmmCertifiedTable": chasSupervisionCmmCertifiedTable,
       "chasSupervisionCmmCertifiedEntry": chasSupervisionCmmCertifiedEntry,
       "chasSupervisionCmmNum": chasSupervisionCmmNum,
       "chasSupervisionCmmCertifiedStatus": chasSupervisionCmmCertifiedStatus,
       "alaChasEntPhysFanTable": alaChasEntPhysFanTable,
       "alaChasEntPhysFanEntry": alaChasEntPhysFanEntry,
       "alaChasEntPhysFanLocalIndex": alaChasEntPhysFanLocalIndex,
       "alaChasEntPhysFanStatus": alaChasEntPhysFanStatus,
       "alaChasEntPhysFanAirflow": alaChasEntPhysFanAirflow,
       "chassisTrapsObj": chassisTrapsObj,
       "chassisTrapsStrLevel": chassisTrapsStrLevel,
       "chassisTrapsStrAppID": chassisTrapsStrAppID,
       "chassisTrapsStrSnapID": chassisTrapsStrSnapID,
       "chassisTrapsStrfileName": chassisTrapsStrfileName,
       "chassisTrapsStrfileLineNb": chassisTrapsStrfileLineNb,
       "chassisTrapsStrErrorNb": chassisTrapsStrErrorNb,
       "chassisTrapsStrcomments": chassisTrapsStrcomments,
       "chassisTrapsStrdataInfo": chassisTrapsStrdataInfo,
       "chassisTrapsObjectType": chassisTrapsObjectType,
       "chassisTrapsObjectNumber": chassisTrapsObjectNumber,
       "chassisTrapsAlertNumber": chassisTrapsAlertNumber,
       "chassisTrapsAlertDescr": chassisTrapsAlertDescr,
       "physicalIndex": physicalIndex,
       "chasTrapsNiRqstdBpsSysPower": chasTrapsNiRqstdBpsSysPower,
       "chasTrapsNiGrantdBpsSysPower": chasTrapsNiGrantdBpsSysPower,
       "chasTrapBPSShelfId": chasTrapBPSShelfId,
       "chasTrapsBPSPowerSupply": chasTrapsBPSPowerSupply,
       "chasTrapsBPSEventAlert": chasTrapsBPSEventAlert,
       "chasTrapsBPSSystemFETChange": chasTrapsBPSSystemFETChange,
       "chasTrapsBPSPoeFETChange": chasTrapsBPSPoeFETChange,
       "alaChasBpsObjects": alaChasBpsObjects,
       "alaChasBpsFwTable": alaChasBpsFwTable,
       "alaChasBpsFwEntry": alaChasBpsFwEntry,
       "alaChasBpsShelfId": alaChasBpsShelfId,
       "alaChasBpsUpdateFirmware": alaChasBpsUpdateFirmware,
       "alaChasBpsCpldRev": alaChasBpsCpldRev,
       "alaChasBpsMmcuRev": alaChasBpsMmcuRev,
       "alaChasBpsCmcuRev": alaChasBpsCmcuRev,
       "alaChasBpsConnectorPriorityTable": alaChasBpsConnectorPriorityTable,
       "alaChasBpsConnectorPriorityEntry": alaChasBpsConnectorPriorityEntry,
       "alaChasBpsChassisId": alaChasBpsChassisId,
       "alaChasBpsConnectorShelfId": alaChasBpsConnectorShelfId,
       "alaChasBpsConnectorPriority": alaChasBpsConnectorPriority,
       "alaChasBpsConnectorNum": alaChasBpsConnectorNum,
       "alaChasBpsSerialNum": alaChasBpsSerialNum,
       "alaChasBpsModeTable": alaChasBpsModeTable,
       "alaChasBpsModeEntry": alaChasBpsModeEntry,
       "alaChasBpsMode": alaChasBpsMode,
       "alaChasBpsPowerSupplyTable": alaChasBpsPowerSupplyTable,
       "alaChasBpsPowerSupplyEntry": alaChasBpsPowerSupplyEntry,
       "alaChasBpsPowerSupplyShelfId": alaChasBpsPowerSupplyShelfId,
       "alaChasBpsPowerSupplyIndex": alaChasBpsPowerSupplyIndex,
       "alaChasBpsPowerSupplyName": alaChasBpsPowerSupplyName,
       "alaChasBpsPowerSupplyDescr": alaChasBpsPowerSupplyDescr,
       "alaChasBpsPowerSupplyModuleType": alaChasBpsPowerSupplyModuleType,
       "alaChasBpsPowerSupplyPartNumber": alaChasBpsPowerSupplyPartNumber,
       "alaChasBpsPowerSupplyHardwareRev": alaChasBpsPowerSupplyHardwareRev,
       "alaChasBpsPowerSupplySerialNum": alaChasBpsPowerSupplySerialNum,
       "alaChasBpsPowerSupplyMfgDate": alaChasBpsPowerSupplyMfgDate,
       "alaChasBpsPowerSupplyOperStatus": alaChasBpsPowerSupplyOperStatus,
       "alaChasBpsPowerSupplyPowerProv": alaChasBpsPowerSupplyPowerProv,
       "alaChasBpsTotalPowerAllocTable": alaChasBpsTotalPowerAllocTable,
       "alaChasBpsTotalPowerAllocEntry": alaChasBpsTotalPowerAllocEntry,
       "alaChasBpsSysTotalAvailablePower": alaChasBpsSysTotalAvailablePower,
       "alaChasBpsSysTotalAllocation": alaChasBpsSysTotalAllocation,
       "alaChasBpsPoeTotalAvailablePower": alaChasBpsPoeTotalAvailablePower,
       "alaChasBpsPoeTotalAllocation": alaChasBpsPoeTotalAllocation,
       "alcatelIND1ChassisMIBConformance": alcatelIND1ChassisMIBConformance,
       "alcatelIND1ChassisMIBGroups": alcatelIND1ChassisMIBGroups,
       "chasControlModuleGroup": chasControlModuleGroup,
       "chasControlRedundantGroup": chasControlRedundantGroup,
       "chasChassisGroup": chasChassisGroup,
       "chasControlReloadStatusGroup": chasControlReloadStatusGroup,
       "chasGlobalControlGroup": chasGlobalControlGroup,
       "chassisNotificationGroup": chassisNotificationGroup,
       "alaChasEntPhysFanGroup": alaChasEntPhysFanGroup,
       "alaChasNotificationObjectGroup": alaChasNotificationObjectGroup,
       "chassisSupervisionRfsCommandsGroup": chassisSupervisionRfsCommandsGroup,
       "chasSupervisionCmmCertifiedEntryGroup": chasSupervisionCmmCertifiedEntryGroup,
       "chasSupervisionFlashMemEntryGroup": chasSupervisionFlashMemEntryGroup,
       "chasSupervisionRfsDfEntryGroup": chasSupervisionRfsDfEntryGroup,
       "chasSupervisionRfsLsEntryGroup": chasSupervisionRfsLsEntryGroup,
       "alaChasBpsFwGroup": alaChasBpsFwGroup,
       "alaChasBpsConnectorPriorityGroup": alaChasBpsConnectorPriorityGroup,
       "alaChasBpsModeGroup": alaChasBpsModeGroup,
       "alaChasBpsPowerSupplyGroup": alaChasBpsPowerSupplyGroup,
       "alaChasBpsTotalPowerAllocGroup": alaChasBpsTotalPowerAllocGroup,
       "alcatelIND1ChassisMIBCompliances": alcatelIND1ChassisMIBCompliances,
       "alcatelIND1ChassisMIBCompliance": alcatelIND1ChassisMIBCompliance}
)
