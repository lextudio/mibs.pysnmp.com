# SNMP MIB module (CIENA-CES-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:01 2024
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2)
)
cienaCesModuleMIB.setRevisions(
        ("2014-01-23 00:00",
         "2013-12-05 00:00",
         "2013-04-16 00:00",
         "2013-03-28 00:00",
         "2013-03-07 00:00",
         "2012-08-23 00:00",
         "2012-06-28 00:00",
         "2012-06-14 00:00",
         "2011-06-06 00:00",
         "2010-12-13 00:00",
         "2010-05-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SwPkgStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("burning", 6),
          ("empty", 7),
          ("good", 1),
          ("invalid", 2),
          ("loading", 3),
          ("syncing", 4),
          ("unknown", 0),
          ("waiting", 5))
    )



class SwModuleState(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("booting", 2),
          ("disabled", 6),
          ("empty", 7),
          ("failed", 5),
          ("good", 4),
          ("initializing", 3),
          ("installing", 1),
          ("unknown", 9),
          ("unsupported", 8))
    )



class TceHealthCategory(Integer32, TextualConvention):
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
              35)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 2),
          ("datapath", 3),
          ("disk", 9),
          ("ethernet", 4),
          ("fabric", 5),
          ("fanRpm", 17),
          ("fanSpeedMismatch", 14),
          ("fanTray", 12),
          ("fanTraySpeedMismatch", 13),
          ("feedPower", 19),
          ("flash", 24),
          ("i2c", 23),
          ("iomStatus", 27),
          ("link", 26),
          ("linxstats", 29),
          ("mac", 22),
          ("memory", 21),
          ("power", 18),
          ("powerOutputVoltage", 35),
          ("powerParams", 34),
          ("samplesFan", 16),
          ("samplesModule", 11),
          ("samplesSm", 8),
          ("slotResource", 32),
          ("sm", 6),
          ("smFabric", 30),
          ("spi", 31),
          ("systemResource", 20),
          ("tempFan", 15),
          ("tempIom", 33),
          ("tempModule", 10),
          ("tempSm", 7),
          ("transceiver", 25),
          ("unknown", 1),
          ("usbFlash", 28))
    )



class TceHealthStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("degraded", 4),
          ("faulted", 5),
          ("normal", 2),
          ("unknown", 1),
          ("warning", 3))
    )



class HealthOriginType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 1),
          ("none", 0),
          ("port", 3),
          ("slot", 2),
          ("unit", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesModuleMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesModuleMIBObjects = _CienaCesModuleMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1)
)
_CienaCesModuleGlobal_ObjectIdentity = ObjectIdentity
cienaCesModuleGlobal = _CienaCesModuleGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 1)
)
_CienaCesModuleGlobalPostState_Type = CienaGlobalState
_CienaCesModuleGlobalPostState_Object = MibScalar
cienaCesModuleGlobalPostState = _CienaCesModuleGlobalPostState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 1, 1),
    _CienaCesModuleGlobalPostState_Type()
)
cienaCesModuleGlobalPostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleGlobalPostState.setStatus("current")
_CienaCesModule_ObjectIdentity = ObjectIdentity
cienaCesModule = _CienaCesModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2)
)
_CienaCesModuleTable_Object = MibTable
cienaCesModuleTable = _CienaCesModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesModuleTable.setStatus("current")
_CienaCesModuleEntry_Object = MibTableRow
cienaCesModuleEntry = _CienaCesModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1)
)
cienaCesModuleEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
)
if mibBuilder.loadTexts:
    cienaCesModuleEntry.setStatus("current")


class _CienaCesModuleChassisIndx_Type(Unsigned32):
    """Custom type cienaCesModuleChassisIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesModuleChassisIndx_Type.__name__ = "Unsigned32"
_CienaCesModuleChassisIndx_Object = MibTableColumn
cienaCesModuleChassisIndx = _CienaCesModuleChassisIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 1),
    _CienaCesModuleChassisIndx_Type()
)
cienaCesModuleChassisIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesModuleChassisIndx.setStatus("current")


class _CienaCesModuleShelfIndx_Type(Unsigned32):
    """Custom type cienaCesModuleShelfIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesModuleShelfIndx_Type.__name__ = "Unsigned32"
_CienaCesModuleShelfIndx_Object = MibTableColumn
cienaCesModuleShelfIndx = _CienaCesModuleShelfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 2),
    _CienaCesModuleShelfIndx_Type()
)
cienaCesModuleShelfIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesModuleShelfIndx.setStatus("current")


class _CienaCesModuleSlotIndx_Type(Unsigned32):
    """Custom type cienaCesModuleSlotIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesModuleSlotIndx_Type.__name__ = "Unsigned32"
_CienaCesModuleSlotIndx_Object = MibTableColumn
cienaCesModuleSlotIndx = _CienaCesModuleSlotIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 3),
    _CienaCesModuleSlotIndx_Type()
)
cienaCesModuleSlotIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesModuleSlotIndx.setStatus("current")
_CienaCesModuleModel_Type = DisplayString
_CienaCesModuleModel_Object = MibTableColumn
cienaCesModuleModel = _CienaCesModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 4),
    _CienaCesModuleModel_Type()
)
cienaCesModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleModel.setStatus("current")


class _CienaCesModuleType_Type(Integer32):
    """Custom type cienaCesModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ctm", 2),
          ("invalid", 0),
          ("lm", 3),
          ("sm", 4),
          ("unknown", 1))
    )


_CienaCesModuleType_Type.__name__ = "Integer32"
_CienaCesModuleType_Object = MibTableColumn
cienaCesModuleType = _CienaCesModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 5),
    _CienaCesModuleType_Type()
)
cienaCesModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleType.setStatus("current")
_CienaCesModuleDescription_Type = DisplayString
_CienaCesModuleDescription_Object = MibTableColumn
cienaCesModuleDescription = _CienaCesModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 6),
    _CienaCesModuleDescription_Type()
)
cienaCesModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescription.setStatus("current")


class _CienaCesModuleAdminState_Type(Integer32):
    """Custom type cienaCesModuleAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("shutdown", 3))
    )


_CienaCesModuleAdminState_Type.__name__ = "Integer32"
_CienaCesModuleAdminState_Object = MibTableColumn
cienaCesModuleAdminState = _CienaCesModuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 7),
    _CienaCesModuleAdminState_Type()
)
cienaCesModuleAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleAdminState.setStatus("current")


class _CienaCesModuleOperState_Type(Integer32):
    """Custom type cienaCesModuleOperState based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("appFault", 16),
          ("booting", 17),
          ("disabled", 4),
          ("enabled", 5),
          ("failed", 14),
          ("fastReload", 10),
          ("faulted", 6),
          ("hitlessInit", 9),
          ("hotswap", 7),
          ("init", 3),
          ("installing", 13),
          ("krnDisable", 15),
          ("krnInit", 11),
          ("powerdown", 18),
          ("poweroff", 8),
          ("unequipped", 2),
          ("uninstalled", 1),
          ("unsupported", 12))
    )


_CienaCesModuleOperState_Type.__name__ = "Integer32"
_CienaCesModuleOperState_Object = MibTableColumn
cienaCesModuleOperState = _CienaCesModuleOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 8),
    _CienaCesModuleOperState_Type()
)
cienaCesModuleOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleOperState.setStatus("current")


class _CienaCesModuleProtectionRole_Type(Integer32):
    """Custom type cienaCesModuleProtectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_CienaCesModuleProtectionRole_Type.__name__ = "Integer32"
_CienaCesModuleProtectionRole_Object = MibTableColumn
cienaCesModuleProtectionRole = _CienaCesModuleProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 9),
    _CienaCesModuleProtectionRole_Type()
)
cienaCesModuleProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleProtectionRole.setStatus("current")


class _CienaCesModuleStandbyStatus_Type(Integer32):
    """Custom type cienaCesModuleStandbyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("hot", 3),
          ("none", 0),
          ("protected", 4),
          ("warm", 2))
    )


_CienaCesModuleStandbyStatus_Type.__name__ = "Integer32"
_CienaCesModuleStandbyStatus_Object = MibTableColumn
cienaCesModuleStandbyStatus = _CienaCesModuleStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 10),
    _CienaCesModuleStandbyStatus_Type()
)
cienaCesModuleStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleStandbyStatus.setStatus("current")


class _CienaCesModuleLastRebootReason_Type(Integer32):
    """Custom type cienaCesModuleLastRebootReason based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("appLoad", 4),
          ("bootFailure", 15),
          ("cli", 8),
          ("coldRestart", 18),
          ("communicationFailure", 12),
          ("configurationRevert", 13),
          ("errorHandler", 5),
          ("failOver", 10),
          ("faultManager", 11),
          ("primaryRestart", 19),
          ("processorWarmRestart", 17),
          ("pwrFail", 3),
          ("resetButton", 9),
          ("snmp", 2),
          ("softwareRevert", 16),
          ("unknown", 1),
          ("unprotectedFailure", 14),
          ("upgrade", 7),
          ("watchdog", 6))
    )


_CienaCesModuleLastRebootReason_Type.__name__ = "Integer32"
_CienaCesModuleLastRebootReason_Object = MibTableColumn
cienaCesModuleLastRebootReason = _CienaCesModuleLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 11),
    _CienaCesModuleLastRebootReason_Type()
)
cienaCesModuleLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleLastRebootReason.setStatus("current")
_CienaCesModuleAdminPostState_Type = CienaGlobalState
_CienaCesModuleAdminPostState_Object = MibTableColumn
cienaCesModuleAdminPostState = _CienaCesModuleAdminPostState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 12),
    _CienaCesModuleAdminPostState_Type()
)
cienaCesModuleAdminPostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleAdminPostState.setStatus("current")
_CienaCesModuleOperPostState_Type = CienaGlobalState
_CienaCesModuleOperPostState_Object = MibTableColumn
cienaCesModuleOperPostState = _CienaCesModuleOperPostState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 13),
    _CienaCesModuleOperPostState_Type()
)
cienaCesModuleOperPostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleOperPostState.setStatus("current")


class _CienaCesModuleTrapState_Type(CienaGlobalState):
    """Custom type cienaCesModuleTrapState based on CienaGlobalState"""


_CienaCesModuleTrapState_Object = MibTableColumn
cienaCesModuleTrapState = _CienaCesModuleTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 16),
    _CienaCesModuleTrapState_Type()
)
cienaCesModuleTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesModuleTrapState.setStatus("current")


class _CienaCesModuleChassisNotifIndx_Type(Unsigned32):
    """Custom type cienaCesModuleChassisNotifIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesModuleChassisNotifIndx_Type.__name__ = "Unsigned32"
_CienaCesModuleChassisNotifIndx_Object = MibTableColumn
cienaCesModuleChassisNotifIndx = _CienaCesModuleChassisNotifIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 17),
    _CienaCesModuleChassisNotifIndx_Type()
)
cienaCesModuleChassisNotifIndx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleChassisNotifIndx.setStatus("current")


class _CienaCesModuleShelfNotifIndx_Type(Unsigned32):
    """Custom type cienaCesModuleShelfNotifIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesModuleShelfNotifIndx_Type.__name__ = "Unsigned32"
_CienaCesModuleShelfNotifIndx_Object = MibTableColumn
cienaCesModuleShelfNotifIndx = _CienaCesModuleShelfNotifIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 18),
    _CienaCesModuleShelfNotifIndx_Type()
)
cienaCesModuleShelfNotifIndx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleShelfNotifIndx.setStatus("current")


class _CienaCesModuleSlotNotifIndx_Type(Unsigned32):
    """Custom type cienaCesModuleSlotNotifIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesModuleSlotNotifIndx_Type.__name__ = "Unsigned32"
_CienaCesModuleSlotNotifIndx_Object = MibTableColumn
cienaCesModuleSlotNotifIndx = _CienaCesModuleSlotNotifIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 19),
    _CienaCesModuleSlotNotifIndx_Type()
)
cienaCesModuleSlotNotifIndx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleSlotNotifIndx.setStatus("current")
_CienaCesModuleSlotName_Type = DisplayString
_CienaCesModuleSlotName_Object = MibTableColumn
cienaCesModuleSlotName = _CienaCesModuleSlotName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 1, 1, 20),
    _CienaCesModuleSlotName_Type()
)
cienaCesModuleSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSlotName.setStatus("current")
_CienaCesModuleDescriptionTable_Object = MibTable
cienaCesModuleDescriptionTable = _CienaCesModuleDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionTable.setStatus("current")
_CienaCesModuleDescriptionEntry_Object = MibTableRow
cienaCesModuleDescriptionEntry = _CienaCesModuleDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1)
)
cienaCesModuleDescriptionEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
)
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionEntry.setStatus("current")
_CienaCesModuleDescriptionBoardName_Type = DisplayString
_CienaCesModuleDescriptionBoardName_Object = MibTableColumn
cienaCesModuleDescriptionBoardName = _CienaCesModuleDescriptionBoardName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 1),
    _CienaCesModuleDescriptionBoardName_Type()
)
cienaCesModuleDescriptionBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionBoardName.setStatus("current")
_CienaCesModuleDescriptionBoardPartNum_Type = DisplayString
_CienaCesModuleDescriptionBoardPartNum_Object = MibTableColumn
cienaCesModuleDescriptionBoardPartNum = _CienaCesModuleDescriptionBoardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 2),
    _CienaCesModuleDescriptionBoardPartNum_Type()
)
cienaCesModuleDescriptionBoardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionBoardPartNum.setStatus("current")
_CienaCesModuleDescriptionBoardSerialNum_Type = DisplayString
_CienaCesModuleDescriptionBoardSerialNum_Object = MibTableColumn
cienaCesModuleDescriptionBoardSerialNum = _CienaCesModuleDescriptionBoardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 3),
    _CienaCesModuleDescriptionBoardSerialNum_Type()
)
cienaCesModuleDescriptionBoardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionBoardSerialNum.setStatus("current")
_CienaCesModuleDescriptionBoardDesc_Type = DisplayString
_CienaCesModuleDescriptionBoardDesc_Object = MibTableColumn
cienaCesModuleDescriptionBoardDesc = _CienaCesModuleDescriptionBoardDesc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 4),
    _CienaCesModuleDescriptionBoardDesc_Type()
)
cienaCesModuleDescriptionBoardDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionBoardDesc.setStatus("current")
_CienaCesModuleDescriptionHwVersion_Type = DisplayString
_CienaCesModuleDescriptionHwVersion_Object = MibTableColumn
cienaCesModuleDescriptionHwVersion = _CienaCesModuleDescriptionHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 5),
    _CienaCesModuleDescriptionHwVersion_Type()
)
cienaCesModuleDescriptionHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionHwVersion.setStatus("current")
_CienaCesModuleDescriptionMfgDate_Type = DisplayString
_CienaCesModuleDescriptionMfgDate_Object = MibTableColumn
cienaCesModuleDescriptionMfgDate = _CienaCesModuleDescriptionMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 6),
    _CienaCesModuleDescriptionMfgDate_Type()
)
cienaCesModuleDescriptionMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionMfgDate.setStatus("current")
_CienaCesModuleDescriptionBaseMac_Type = MacAddress
_CienaCesModuleDescriptionBaseMac_Object = MibTableColumn
cienaCesModuleDescriptionBaseMac = _CienaCesModuleDescriptionBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 7),
    _CienaCesModuleDescriptionBaseMac_Type()
)
cienaCesModuleDescriptionBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionBaseMac.setStatus("current")
_CienaCesModuleDescriptionUpTime_Type = TimeTicks
_CienaCesModuleDescriptionUpTime_Object = MibTableColumn
cienaCesModuleDescriptionUpTime = _CienaCesModuleDescriptionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 8),
    _CienaCesModuleDescriptionUpTime_Type()
)
cienaCesModuleDescriptionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionUpTime.setStatus("current")
_CienaCesModuleDescriptionTotalNumPorts_Type = Integer32
_CienaCesModuleDescriptionTotalNumPorts_Object = MibTableColumn
cienaCesModuleDescriptionTotalNumPorts = _CienaCesModuleDescriptionTotalNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 2, 1, 9),
    _CienaCesModuleDescriptionTotalNumPorts_Type()
)
cienaCesModuleDescriptionTotalNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleDescriptionTotalNumPorts.setStatus("current")
_CienaCesModuleTempSensorTable_Object = MibTable
cienaCesModuleTempSensorTable = _CienaCesModuleTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesModuleTempSensorTable.setStatus("current")
_CienaCesModuleTempSensorEntry_Object = MibTableRow
cienaCesModuleTempSensorEntry = _CienaCesModuleTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1)
)
cienaCesModuleTempSensorEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSensorIndx"),
)
if mibBuilder.loadTexts:
    cienaCesModuleTempSensorEntry.setStatus("current")


class _CienaCesModuleSensorIndx_Type(Integer32):
    """Custom type cienaCesModuleSensorIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesModuleSensorIndx_Type.__name__ = "Integer32"
_CienaCesModuleSensorIndx_Object = MibTableColumn
cienaCesModuleSensorIndx = _CienaCesModuleSensorIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 1),
    _CienaCesModuleSensorIndx_Type()
)
cienaCesModuleSensorIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesModuleSensorIndx.setStatus("current")
_CienaCesModuleSensorDescription_Type = DisplayString
_CienaCesModuleSensorDescription_Object = MibTableColumn
cienaCesModuleSensorDescription = _CienaCesModuleSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 2),
    _CienaCesModuleSensorDescription_Type()
)
cienaCesModuleSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSensorDescription.setStatus("current")
_CienaCesModuleSensorCurrentTemp_Type = Integer32
_CienaCesModuleSensorCurrentTemp_Object = MibTableColumn
cienaCesModuleSensorCurrentTemp = _CienaCesModuleSensorCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 3),
    _CienaCesModuleSensorCurrentTemp_Type()
)
cienaCesModuleSensorCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSensorCurrentTemp.setStatus("current")
_CienaCesModuleSensorHighTemp_Type = Integer32
_CienaCesModuleSensorHighTemp_Object = MibTableColumn
cienaCesModuleSensorHighTemp = _CienaCesModuleSensorHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 4),
    _CienaCesModuleSensorHighTemp_Type()
)
cienaCesModuleSensorHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSensorHighTemp.setStatus("current")
_CienaCesModuleSensorLowTemp_Type = Integer32
_CienaCesModuleSensorLowTemp_Object = MibTableColumn
cienaCesModuleSensorLowTemp = _CienaCesModuleSensorLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 5),
    _CienaCesModuleSensorLowTemp_Type()
)
cienaCesModuleSensorLowTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSensorLowTemp.setStatus("current")


class _CienaCesModuleSensorHighTempThreshold_Type(Integer32):
    """Custom type cienaCesModuleSensorHighTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CienaCesModuleSensorHighTempThreshold_Type.__name__ = "Integer32"
_CienaCesModuleSensorHighTempThreshold_Object = MibTableColumn
cienaCesModuleSensorHighTempThreshold = _CienaCesModuleSensorHighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 6),
    _CienaCesModuleSensorHighTempThreshold_Type()
)
cienaCesModuleSensorHighTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSensorHighTempThreshold.setStatus("current")


class _CienaCesModuleSensorLowTempThreshold_Type(Integer32):
    """Custom type cienaCesModuleSensorLowTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CienaCesModuleSensorLowTempThreshold_Type.__name__ = "Integer32"
_CienaCesModuleSensorLowTempThreshold_Object = MibTableColumn
cienaCesModuleSensorLowTempThreshold = _CienaCesModuleSensorLowTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 7),
    _CienaCesModuleSensorLowTempThreshold_Type()
)
cienaCesModuleSensorLowTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSensorLowTempThreshold.setStatus("current")


class _CienaCesModuleSensorNotifIndx_Type(Integer32):
    """Custom type cienaCesModuleSensorNotifIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesModuleSensorNotifIndx_Type.__name__ = "Integer32"
_CienaCesModuleSensorNotifIndx_Object = MibTableColumn
cienaCesModuleSensorNotifIndx = _CienaCesModuleSensorNotifIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 3, 1, 8),
    _CienaCesModuleSensorNotifIndx_Type()
)
cienaCesModuleSensorNotifIndx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleSensorNotifIndx.setStatus("current")
_CienaCesSwModule_ObjectIdentity = ObjectIdentity
cienaCesSwModule = _CienaCesSwModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4)
)


class _CienaCesGlobalSwState_Type(Integer32):
    """Custom type cienaCesGlobalSwState based on Integer32"""
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
        *(("activating", 4),
          ("downloading", 2),
          ("idle", 1),
          ("installing", 3),
          ("reverting", 6),
          ("running", 7),
          ("validating", 5))
    )


_CienaCesGlobalSwState_Type.__name__ = "Integer32"
_CienaCesGlobalSwState_Object = MibScalar
cienaCesGlobalSwState = _CienaCesGlobalSwState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 1),
    _CienaCesGlobalSwState_Type()
)
cienaCesGlobalSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesGlobalSwState.setStatus("current")
_CienaCesModuleSwTable_Object = MibTable
cienaCesModuleSwTable = _CienaCesModuleSwTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    cienaCesModuleSwTable.setStatus("current")
_CienaCesModuleSwEntry_Object = MibTableRow
cienaCesModuleSwEntry = _CienaCesModuleSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1)
)
cienaCesModuleSwEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
)
if mibBuilder.loadTexts:
    cienaCesModuleSwEntry.setStatus("current")
_CienaCesModuleSwState_Type = SwModuleState
_CienaCesModuleSwState_Object = MibTableColumn
cienaCesModuleSwState = _CienaCesModuleSwState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 1),
    _CienaCesModuleSwState_Type()
)
cienaCesModuleSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwState.setStatus("current")


class _CienaCesModuleSwRunningRelease_Type(DisplayString):
    """Custom type cienaCesModuleSwRunningRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwRunningRelease_Type.__name__ = "DisplayString"
_CienaCesModuleSwRunningRelease_Object = MibTableColumn
cienaCesModuleSwRunningRelease = _CienaCesModuleSwRunningRelease_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 2),
    _CienaCesModuleSwRunningRelease_Type()
)
cienaCesModuleSwRunningRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwRunningRelease.setStatus("current")
_CienaCesModuleSwRunningReleasePartition_Type = Unsigned32
_CienaCesModuleSwRunningReleasePartition_Object = MibTableColumn
cienaCesModuleSwRunningReleasePartition = _CienaCesModuleSwRunningReleasePartition_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 3),
    _CienaCesModuleSwRunningReleasePartition_Type()
)
cienaCesModuleSwRunningReleasePartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwRunningReleasePartition.setStatus("current")


class _CienaCesModuleSwReleasePartition0Pkg_Type(DisplayString):
    """Custom type cienaCesModuleSwReleasePartition0Pkg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwReleasePartition0Pkg_Type.__name__ = "DisplayString"
_CienaCesModuleSwReleasePartition0Pkg_Object = MibTableColumn
cienaCesModuleSwReleasePartition0Pkg = _CienaCesModuleSwReleasePartition0Pkg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 4),
    _CienaCesModuleSwReleasePartition0Pkg_Type()
)
cienaCesModuleSwReleasePartition0Pkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwReleasePartition0Pkg.setStatus("current")
_CienaCesModuleSwReleasePartition0PkgStatus_Type = SwPkgStatus
_CienaCesModuleSwReleasePartition0PkgStatus_Object = MibTableColumn
cienaCesModuleSwReleasePartition0PkgStatus = _CienaCesModuleSwReleasePartition0PkgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 5),
    _CienaCesModuleSwReleasePartition0PkgStatus_Type()
)
cienaCesModuleSwReleasePartition0PkgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwReleasePartition0PkgStatus.setStatus("current")


class _CienaCesModuleSwReleasePartition1Pkg_Type(DisplayString):
    """Custom type cienaCesModuleSwReleasePartition1Pkg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwReleasePartition1Pkg_Type.__name__ = "DisplayString"
_CienaCesModuleSwReleasePartition1Pkg_Object = MibTableColumn
cienaCesModuleSwReleasePartition1Pkg = _CienaCesModuleSwReleasePartition1Pkg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 6),
    _CienaCesModuleSwReleasePartition1Pkg_Type()
)
cienaCesModuleSwReleasePartition1Pkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwReleasePartition1Pkg.setStatus("current")
_CienaCesModuleSwReleasePartition1PkgStatus_Type = SwPkgStatus
_CienaCesModuleSwReleasePartition1PkgStatus_Object = MibTableColumn
cienaCesModuleSwReleasePartition1PkgStatus = _CienaCesModuleSwReleasePartition1PkgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 7),
    _CienaCesModuleSwReleasePartition1PkgStatus_Type()
)
cienaCesModuleSwReleasePartition1PkgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwReleasePartition1PkgStatus.setStatus("current")


class _CienaCesModuleSwReleasePartition2Pkg_Type(DisplayString):
    """Custom type cienaCesModuleSwReleasePartition2Pkg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwReleasePartition2Pkg_Type.__name__ = "DisplayString"
_CienaCesModuleSwReleasePartition2Pkg_Object = MibTableColumn
cienaCesModuleSwReleasePartition2Pkg = _CienaCesModuleSwReleasePartition2Pkg_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 8),
    _CienaCesModuleSwReleasePartition2Pkg_Type()
)
cienaCesModuleSwReleasePartition2Pkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwReleasePartition2Pkg.setStatus("current")
_CienaCesModuleSwReleasePartition2PkgStatus_Type = SwPkgStatus
_CienaCesModuleSwReleasePartition2PkgStatus_Object = MibTableColumn
cienaCesModuleSwReleasePartition2PkgStatus = _CienaCesModuleSwReleasePartition2PkgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 9),
    _CienaCesModuleSwReleasePartition2PkgStatus_Type()
)
cienaCesModuleSwReleasePartition2PkgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwReleasePartition2PkgStatus.setStatus("current")


class _CienaCesModuleSwBank0KernelVersion_Type(DisplayString):
    """Custom type cienaCesModuleSwBank0KernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwBank0KernelVersion_Type.__name__ = "DisplayString"
_CienaCesModuleSwBank0KernelVersion_Object = MibTableColumn
cienaCesModuleSwBank0KernelVersion = _CienaCesModuleSwBank0KernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 10),
    _CienaCesModuleSwBank0KernelVersion_Type()
)
cienaCesModuleSwBank0KernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank0KernelVersion.setStatus("current")
_CienaCesModuleSwBank0KernelStatus_Type = SwPkgStatus
_CienaCesModuleSwBank0KernelStatus_Object = MibTableColumn
cienaCesModuleSwBank0KernelStatus = _CienaCesModuleSwBank0KernelStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 11),
    _CienaCesModuleSwBank0KernelStatus_Type()
)
cienaCesModuleSwBank0KernelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank0KernelStatus.setStatus("current")


class _CienaCesModuleSwBank1KernelVersion_Type(DisplayString):
    """Custom type cienaCesModuleSwBank1KernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwBank1KernelVersion_Type.__name__ = "DisplayString"
_CienaCesModuleSwBank1KernelVersion_Object = MibTableColumn
cienaCesModuleSwBank1KernelVersion = _CienaCesModuleSwBank1KernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 12),
    _CienaCesModuleSwBank1KernelVersion_Type()
)
cienaCesModuleSwBank1KernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank1KernelVersion.setStatus("current")
_CienaCesModuleSwBank1KernelStatus_Type = SwPkgStatus
_CienaCesModuleSwBank1KernelStatus_Object = MibTableColumn
cienaCesModuleSwBank1KernelStatus = _CienaCesModuleSwBank1KernelStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 13),
    _CienaCesModuleSwBank1KernelStatus_Type()
)
cienaCesModuleSwBank1KernelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank1KernelStatus.setStatus("current")


class _CienaCesModuleSwBank0UbootVersion_Type(DisplayString):
    """Custom type cienaCesModuleSwBank0UbootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwBank0UbootVersion_Type.__name__ = "DisplayString"
_CienaCesModuleSwBank0UbootVersion_Object = MibTableColumn
cienaCesModuleSwBank0UbootVersion = _CienaCesModuleSwBank0UbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 14),
    _CienaCesModuleSwBank0UbootVersion_Type()
)
cienaCesModuleSwBank0UbootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank0UbootVersion.setStatus("current")
_CienaCesModuleSwBank0UbootStatus_Type = SwPkgStatus
_CienaCesModuleSwBank0UbootStatus_Object = MibTableColumn
cienaCesModuleSwBank0UbootStatus = _CienaCesModuleSwBank0UbootStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 15),
    _CienaCesModuleSwBank0UbootStatus_Type()
)
cienaCesModuleSwBank0UbootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank0UbootStatus.setStatus("current")


class _CienaCesModuleSwBank1UbootVersion_Type(DisplayString):
    """Custom type cienaCesModuleSwBank1UbootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwBank1UbootVersion_Type.__name__ = "DisplayString"
_CienaCesModuleSwBank1UbootVersion_Object = MibTableColumn
cienaCesModuleSwBank1UbootVersion = _CienaCesModuleSwBank1UbootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 16),
    _CienaCesModuleSwBank1UbootVersion_Type()
)
cienaCesModuleSwBank1UbootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank1UbootVersion.setStatus("current")
_CienaCesModuleSwBank1UbootStatus_Type = SwPkgStatus
_CienaCesModuleSwBank1UbootStatus_Object = MibTableColumn
cienaCesModuleSwBank1UbootStatus = _CienaCesModuleSwBank1UbootStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 17),
    _CienaCesModuleSwBank1UbootStatus_Type()
)
cienaCesModuleSwBank1UbootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwBank1UbootStatus.setStatus("current")


class _CienaCesModuleSwUbootGoldVersion_Type(DisplayString):
    """Custom type cienaCesModuleSwUbootGoldVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CienaCesModuleSwUbootGoldVersion_Type.__name__ = "DisplayString"
_CienaCesModuleSwUbootGoldVersion_Object = MibTableColumn
cienaCesModuleSwUbootGoldVersion = _CienaCesModuleSwUbootGoldVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 18),
    _CienaCesModuleSwUbootGoldVersion_Type()
)
cienaCesModuleSwUbootGoldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwUbootGoldVersion.setStatus("current")
_CienaCesModuleSwUbootGoldStatus_Type = SwPkgStatus
_CienaCesModuleSwUbootGoldStatus_Object = MibTableColumn
cienaCesModuleSwUbootGoldStatus = _CienaCesModuleSwUbootGoldStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 19),
    _CienaCesModuleSwUbootGoldStatus_Type()
)
cienaCesModuleSwUbootGoldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwUbootGoldStatus.setStatus("current")


class _CienaCesModuleSwMIBVer_Type(DisplayString):
    """Custom type cienaCesModuleSwMIBVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CienaCesModuleSwMIBVer_Type.__name__ = "DisplayString"
_CienaCesModuleSwMIBVer_Object = MibTableColumn
cienaCesModuleSwMIBVer = _CienaCesModuleSwMIBVer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 4, 2, 1, 20),
    _CienaCesModuleSwMIBVer_Type()
)
cienaCesModuleSwMIBVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleSwMIBVer.setStatus("current")
_CienaCesModulePOSTErrorTable_Object = MibTable
cienaCesModulePOSTErrorTable = _CienaCesModulePOSTErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cienaCesModulePOSTErrorTable.setStatus("current")
_CienaCesModulePOSTErrorEntry_Object = MibTableRow
cienaCesModulePOSTErrorEntry = _CienaCesModulePOSTErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 5, 1)
)
cienaCesModulePOSTErrorEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModulePOSTErrorIndex"),
)
if mibBuilder.loadTexts:
    cienaCesModulePOSTErrorEntry.setStatus("current")
_CienaCesModulePOSTErrorIndex_Type = Integer32
_CienaCesModulePOSTErrorIndex_Object = MibTableColumn
cienaCesModulePOSTErrorIndex = _CienaCesModulePOSTErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 5, 1, 1),
    _CienaCesModulePOSTErrorIndex_Type()
)
cienaCesModulePOSTErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesModulePOSTErrorIndex.setStatus("current")
_CienaCesModulePOSTErrorDescription_Type = OctetString
_CienaCesModulePOSTErrorDescription_Object = MibTableColumn
cienaCesModulePOSTErrorDescription = _CienaCesModulePOSTErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 5, 1, 2),
    _CienaCesModulePOSTErrorDescription_Type()
)
cienaCesModulePOSTErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModulePOSTErrorDescription.setStatus("current")


class _CienaCesModulePOSTErrorSeverity_Type(Integer32):
    """Custom type cienaCesModulePOSTErrorSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fatal", 1),
          ("severe", 2),
          ("unknown", 0),
          ("warning", 3))
    )


_CienaCesModulePOSTErrorSeverity_Type.__name__ = "Integer32"
_CienaCesModulePOSTErrorSeverity_Object = MibTableColumn
cienaCesModulePOSTErrorSeverity = _CienaCesModulePOSTErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 5, 1, 3),
    _CienaCesModulePOSTErrorSeverity_Type()
)
cienaCesModulePOSTErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModulePOSTErrorSeverity.setStatus("current")


class _CienaCesModulePOSTErrorScope_Type(Integer32):
    """Custom type cienaCesModulePOSTErrorScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blade", 2),
          ("chassis", 1),
          ("port", 3),
          ("unknown", 0))
    )


_CienaCesModulePOSTErrorScope_Type.__name__ = "Integer32"
_CienaCesModulePOSTErrorScope_Object = MibTableColumn
cienaCesModulePOSTErrorScope = _CienaCesModulePOSTErrorScope_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 5, 1, 4),
    _CienaCesModulePOSTErrorScope_Type()
)
cienaCesModulePOSTErrorScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModulePOSTErrorScope.setStatus("current")
_CienaCesModulePOSTScopeIndex_Type = Integer32
_CienaCesModulePOSTScopeIndex_Object = MibTableColumn
cienaCesModulePOSTScopeIndex = _CienaCesModulePOSTScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 5, 1, 5),
    _CienaCesModulePOSTScopeIndex_Type()
)
cienaCesModulePOSTScopeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModulePOSTScopeIndex.setStatus("current")
_CienaCesModuleResourceHealthTable_Object = MibTable
cienaCesModuleResourceHealthTable = _CienaCesModuleResourceHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cienaCesModuleResourceHealthTable.setStatus("current")
_CienaCesModuleResourceHealthEntry_Object = MibTableRow
cienaCesModuleResourceHealthEntry = _CienaCesModuleResourceHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6, 1)
)
cienaCesModuleResourceHealthEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleResourceHealthSubCategory"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleResourceDeviceIndx"),
)
if mibBuilder.loadTexts:
    cienaCesModuleResourceHealthEntry.setStatus("current")


class _CienaCesModuleResourceHealthSubCategory_Type(Integer32):
    """Custom type cienaCesModuleResourceHealthSubCategory based on Integer32"""
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("accessFlow", 3),
          ("logicalInterfaces", 21),
          ("none", 0),
          ("pbtTransit", 6),
          ("pltfmAclTcamEntries", 10),
          ("pltfmBscp", 15),
          ("pltfmCLScheduler", 12),
          ("pltfmChildMeter", 19),
          ("pltfmEgressShapingCIR", 14),
          ("pltfmEgressTunnel", 8),
          ("pltfmFQScheduler", 13),
          ("pltfmHighRateTokenBucket", 16),
          ("pltfmL2UserTypes", 20),
          ("pltfmLmPowerBudget", 22),
          ("pltfmLowRateTokenBucket", 17),
          ("pltfmNpFastTimer100msec", 30),
          ("pltfmNpFastTimer10msec", 29),
          ("pltfmNpFastTimer1sec", 31),
          ("pltfmNpFastTimer300Hz", 28),
          ("pltfmNpMaintPoint", 26),
          ("pltfmNpMaintPointSession", 27),
          ("pltfmNpProtectionGroup", 34),
          ("pltfmNpSlowTimer", 32),
          ("pltfmNpWatchdogTimer", 33),
          ("pltfmParentMeter", 18),
          ("pltfmPpEgressL2Xform", 24),
          ("pltfmPpIngressL2Xform", 23),
          ("pltfmPpInternalTcam", 25),
          ("pltfmTokenBucket", 7),
          ("pltfmVOQ", 11),
          ("pltfmVirtTcamEntries", 9),
          ("qosFlow", 2),
          ("queueGroupInstance", 4),
          ("schedulerInstance", 5),
          ("subPort", 1))
    )


_CienaCesModuleResourceHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesModuleResourceHealthSubCategory_Object = MibTableColumn
cienaCesModuleResourceHealthSubCategory = _CienaCesModuleResourceHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6, 1, 1),
    _CienaCesModuleResourceHealthSubCategory_Type()
)
cienaCesModuleResourceHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesModuleResourceHealthSubCategory.setStatus("current")
_CienaCesModuleResourceDeviceIndx_Type = Unsigned32
_CienaCesModuleResourceDeviceIndx_Object = MibTableColumn
cienaCesModuleResourceDeviceIndx = _CienaCesModuleResourceDeviceIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6, 1, 2),
    _CienaCesModuleResourceDeviceIndx_Type()
)
cienaCesModuleResourceDeviceIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesModuleResourceDeviceIndx.setStatus("current")
_CienaCesModuleResourceHealthState_Type = TceHealthStatus
_CienaCesModuleResourceHealthState_Object = MibTableColumn
cienaCesModuleResourceHealthState = _CienaCesModuleResourceHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6, 1, 3),
    _CienaCesModuleResourceHealthState_Type()
)
cienaCesModuleResourceHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleResourceHealthState.setStatus("current")
_CienaCesModuleResourceHealthCurrMeasurement_Type = Unsigned32
_CienaCesModuleResourceHealthCurrMeasurement_Object = MibTableColumn
cienaCesModuleResourceHealthCurrMeasurement = _CienaCesModuleResourceHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6, 1, 4),
    _CienaCesModuleResourceHealthCurrMeasurement_Type()
)
cienaCesModuleResourceHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleResourceHealthCurrMeasurement.setStatus("current")
_CienaCesModuleResourceHealthMaxMeasurement_Type = Unsigned32
_CienaCesModuleResourceHealthMaxMeasurement_Object = MibTableColumn
cienaCesModuleResourceHealthMaxMeasurement = _CienaCesModuleResourceHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6, 1, 5),
    _CienaCesModuleResourceHealthMaxMeasurement_Type()
)
cienaCesModuleResourceHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleResourceHealthMaxMeasurement.setStatus("current")
_CienaCesModuleResourceHealthMaxThreshold_Type = Unsigned32
_CienaCesModuleResourceHealthMaxThreshold_Object = MibTableColumn
cienaCesModuleResourceHealthMaxThreshold = _CienaCesModuleResourceHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 6, 1, 6),
    _CienaCesModuleResourceHealthMaxThreshold_Type()
)
cienaCesModuleResourceHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleResourceHealthMaxThreshold.setStatus("current")
_CienaCesModuleIDPTable_Object = MibTable
cienaCesModuleIDPTable = _CienaCesModuleIDPTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cienaCesModuleIDPTable.setStatus("current")
_CienaCesModuleIDPEntry_Object = MibTableRow
cienaCesModuleIDPEntry = _CienaCesModuleIDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1)
)
cienaCesModuleIDPEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
)
if mibBuilder.loadTexts:
    cienaCesModuleIDPEntry.setStatus("current")
_CienaCesModuleIDPEthBaseMac_Type = MacAddress
_CienaCesModuleIDPEthBaseMac_Object = MibTableColumn
cienaCesModuleIDPEthBaseMac = _CienaCesModuleIDPEthBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 1),
    _CienaCesModuleIDPEthBaseMac_Type()
)
cienaCesModuleIDPEthBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPEthBaseMac.setStatus("current")
_CienaCesModuleIDPEthBaseMacRange_Type = Integer32
_CienaCesModuleIDPEthBaseMacRange_Object = MibTableColumn
cienaCesModuleIDPEthBaseMacRange = _CienaCesModuleIDPEthBaseMacRange_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 2),
    _CienaCesModuleIDPEthBaseMacRange_Type()
)
cienaCesModuleIDPEthBaseMacRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPEthBaseMacRange.setStatus("current")
_CienaCesModuleIDPModuleSerialNumber_Type = DisplayString
_CienaCesModuleIDPModuleSerialNumber_Object = MibTableColumn
cienaCesModuleIDPModuleSerialNumber = _CienaCesModuleIDPModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 3),
    _CienaCesModuleIDPModuleSerialNumber_Type()
)
cienaCesModuleIDPModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPModuleSerialNumber.setStatus("current")
_CienaCesModuleIDPModelPartNumber_Type = DisplayString
_CienaCesModuleIDPModelPartNumber_Object = MibTableColumn
cienaCesModuleIDPModelPartNumber = _CienaCesModuleIDPModelPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 4),
    _CienaCesModuleIDPModelPartNumber_Type()
)
cienaCesModuleIDPModelPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPModelPartNumber.setStatus("current")
_CienaCesModuleIDPModelRevision_Type = DisplayString
_CienaCesModuleIDPModelRevision_Object = MibTableColumn
cienaCesModuleIDPModelRevision = _CienaCesModuleIDPModelRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 5),
    _CienaCesModuleIDPModelRevision_Type()
)
cienaCesModuleIDPModelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPModelRevision.setStatus("current")
_CienaCesModuleIDPProductID_Type = DisplayString
_CienaCesModuleIDPProductID_Object = MibTableColumn
cienaCesModuleIDPProductID = _CienaCesModuleIDPProductID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 6),
    _CienaCesModuleIDPProductID_Type()
)
cienaCesModuleIDPProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPProductID.setStatus("current")
_CienaCesModuleIDPMfgDate_Type = DisplayString
_CienaCesModuleIDPMfgDate_Object = MibTableColumn
cienaCesModuleIDPMfgDate = _CienaCesModuleIDPMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 7),
    _CienaCesModuleIDPMfgDate_Type()
)
cienaCesModuleIDPMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPMfgDate.setStatus("current")
_CienaCesModuleIDPCleiCode_Type = DisplayString
_CienaCesModuleIDPCleiCode_Object = MibTableColumn
cienaCesModuleIDPCleiCode = _CienaCesModuleIDPCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 8),
    _CienaCesModuleIDPCleiCode_Type()
)
cienaCesModuleIDPCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPCleiCode.setStatus("current")
_CienaCesModuleIDPBarcode_Type = DisplayString
_CienaCesModuleIDPBarcode_Object = MibTableColumn
cienaCesModuleIDPBarcode = _CienaCesModuleIDPBarcode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 9),
    _CienaCesModuleIDPBarcode_Type()
)
cienaCesModuleIDPBarcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPBarcode.setStatus("current")
_CienaCesModuleIDPSWCompat_Type = Integer32
_CienaCesModuleIDPSWCompat_Object = MibTableColumn
cienaCesModuleIDPSWCompat = _CienaCesModuleIDPSWCompat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 10),
    _CienaCesModuleIDPSWCompat_Type()
)
cienaCesModuleIDPSWCompat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPSWCompat.setStatus("current")
_CienaCesModuleIDPFTC_Type = Integer32
_CienaCesModuleIDPFTC_Object = MibTableColumn
cienaCesModuleIDPFTC = _CienaCesModuleIDPFTC_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 2, 8, 1, 11),
    _CienaCesModuleIDPFTC_Type()
)
cienaCesModuleIDPFTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesModuleIDPFTC.setStatus("current")
_CienaCesModuleNotifAttrs_ObjectIdentity = ObjectIdentity
cienaCesModuleNotifAttrs = _CienaCesModuleNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3)
)


class _CienaCesModuleSystemProtectionMode_Type(Integer32):
    """Custom type cienaCesModuleSystemProtectionMode based on Integer32"""
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
        *(("cold", 2),
          ("hot", 4),
          ("unprotected", 1),
          ("warm", 3))
    )


_CienaCesModuleSystemProtectionMode_Type.__name__ = "Integer32"
_CienaCesModuleSystemProtectionMode_Object = MibScalar
cienaCesModuleSystemProtectionMode = _CienaCesModuleSystemProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 1),
    _CienaCesModuleSystemProtectionMode_Type()
)
cienaCesModuleSystemProtectionMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleSystemProtectionMode.setStatus("current")


class _CienaCesModuleSwitchOverReason_Type(Integer32):
    """Custom type cienaCesModuleSwitchOverReason based on Integer32"""
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
        *(("coldFailOver", 1),
          ("coldSwitchOver", 2),
          ("hotFailOver", 4),
          ("hotSwitchOver", 3))
    )


_CienaCesModuleSwitchOverReason_Type.__name__ = "Integer32"
_CienaCesModuleSwitchOverReason_Object = MibScalar
cienaCesModuleSwitchOverReason = _CienaCesModuleSwitchOverReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 2),
    _CienaCesModuleSwitchOverReason_Type()
)
cienaCesModuleSwitchOverReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleSwitchOverReason.setStatus("current")
_CienaCesModuleNotifTable_Object = MibTable
cienaCesModuleNotifTable = _CienaCesModuleNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cienaCesModuleNotifTable.setStatus("current")
_CienaCesModuleNotifEntry_Object = MibTableRow
cienaCesModuleNotifEntry = _CienaCesModuleNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1)
)
cienaCesModuleNotifEntry.setIndexNames(
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
    (0, "CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
)
if mibBuilder.loadTexts:
    cienaCesModuleNotifEntry.setStatus("current")
_CienaCesModuleHealthCategory_Type = TceHealthCategory
_CienaCesModuleHealthCategory_Object = MibTableColumn
cienaCesModuleHealthCategory = _CienaCesModuleHealthCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1, 1),
    _CienaCesModuleHealthCategory_Type()
)
cienaCesModuleHealthCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleHealthCategory.setStatus("current")
_CienaCesModuleHealthSubCategory_Type = Unsigned32
_CienaCesModuleHealthSubCategory_Object = MibTableColumn
cienaCesModuleHealthSubCategory = _CienaCesModuleHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1, 2),
    _CienaCesModuleHealthSubCategory_Type()
)
cienaCesModuleHealthSubCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleHealthSubCategory.setStatus("current")
_CienaCesModuleHealthStatus_Type = TceHealthStatus
_CienaCesModuleHealthStatus_Object = MibTableColumn
cienaCesModuleHealthStatus = _CienaCesModuleHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1, 3),
    _CienaCesModuleHealthStatus_Type()
)
cienaCesModuleHealthStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleHealthStatus.setStatus("current")
_CienaCesModuleHealthStatusLast_Type = TceHealthStatus
_CienaCesModuleHealthStatusLast_Object = MibTableColumn
cienaCesModuleHealthStatusLast = _CienaCesModuleHealthStatusLast_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1, 4),
    _CienaCesModuleHealthStatusLast_Type()
)
cienaCesModuleHealthStatusLast.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleHealthStatusLast.setStatus("current")
_CienaCesModuleHealthOriginType_Type = HealthOriginType
_CienaCesModuleHealthOriginType_Object = MibTableColumn
cienaCesModuleHealthOriginType = _CienaCesModuleHealthOriginType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1, 5),
    _CienaCesModuleHealthOriginType_Type()
)
cienaCesModuleHealthOriginType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleHealthOriginType.setStatus("current")


class _CienaCesModuleHealthOriginName_Type(DisplayString):
    """Custom type cienaCesModuleHealthOriginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CienaCesModuleHealthOriginName_Type.__name__ = "DisplayString"
_CienaCesModuleHealthOriginName_Object = MibTableColumn
cienaCesModuleHealthOriginName = _CienaCesModuleHealthOriginName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1, 6),
    _CienaCesModuleHealthOriginName_Type()
)
cienaCesModuleHealthOriginName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleHealthOriginName.setStatus("current")
_CienaCesModuleHealthOriginUnitId_Type = Unsigned32
_CienaCesModuleHealthOriginUnitId_Object = MibTableColumn
cienaCesModuleHealthOriginUnitId = _CienaCesModuleHealthOriginUnitId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 1, 3, 3, 1, 7),
    _CienaCesModuleHealthOriginUnitId_Type()
)
cienaCesModuleHealthOriginUnitId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesModuleHealthOriginUnitId.setStatus("current")
_CienaCesModuleConformance_ObjectIdentity = ObjectIdentity
cienaCesModuleConformance = _CienaCesModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2)
)
_CienaCesModuleMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesModuleMIBCompliances = _CienaCesModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2, 1)
)
_CienaCesModuleMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesModuleMIBGroups = _CienaCesModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2, 2)
)
_CienaCesModuleMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesModuleMIBNotificationPrefix = _CienaCesModuleMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3)
)
_CienaCesModuleMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesModuleMIBNotifications = _CienaCesModuleMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0)
)

# Managed Objects groups

moduleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2, 2, 1)
)
moduleConfigGroup.setObjects(
      *(("CIENA-CES-MODULE-MIB", "cienaCesModuleModel"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleType"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescription"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleAdminState"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleOperState"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleProtectionRole"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleStandbyStatus"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleLastRebootReason"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleAdminPostState"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleOperPostState"))
)
if mibBuilder.loadTexts:
    moduleConfigGroup.setStatus("current")

moduleDescriptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2, 2, 2)
)
moduleDescriptionGroup.setObjects(
      *(("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionBoardName"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionBoardDesc"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionTotalNumPorts"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionHwVersion"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionMfgDate"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionBaseMac"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionBoardSerialNum"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionBoardPartNum"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleDescriptionUpTime"))
)
if mibBuilder.loadTexts:
    moduleDescriptionGroup.setStatus("current")

moduleSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2, 2, 3)
)
moduleSensorGroup.setObjects(
      *(("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorDescription"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorCurrentTemp"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorHighTemp"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorLowTemp"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorHighTempThreshold"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorLowTempThreshold"))
)
if mibBuilder.loadTexts:
    moduleSensorGroup.setStatus("current")

modulePostErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2, 2, 5)
)
modulePostErrorGroup.setObjects(
      *(("CIENA-CES-MODULE-MIB", "cienaCesModulePOSTErrorDescription"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModulePOSTErrorSeverity"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModulePOSTErrorScope"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModulePOSTScopeIndex"))
)
if mibBuilder.loadTexts:
    modulePostErrorGroup.setStatus("current")


# Notification objects

cienaCesModuleStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 1)
)
cienaCesModuleStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleAdminState"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleOperState"))
)
if mibBuilder.loadTexts:
    cienaCesModuleStateChangeNotification.setStatus(
        "current"
    )

cienaCesModuleHealthStatusUnknownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 2)
)
cienaCesModuleHealthStatusUnknownNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginType"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginName"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginUnitId"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthSubCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatus"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesModuleHealthStatusUnknownNotification.setStatus(
        "current"
    )

cienaCesModuleHealthStatusWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 3)
)
cienaCesModuleHealthStatusWarningNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginType"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginName"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginUnitId"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthSubCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatus"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesModuleHealthStatusWarningNotification.setStatus(
        "current"
    )

cienaCesModuleHealthStatusFaultedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 4)
)
cienaCesModuleHealthStatusFaultedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginType"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginName"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginUnitId"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthSubCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatus"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesModuleHealthStatusFaultedNotification.setStatus(
        "current"
    )

cienaCesModuleHealthStatusDegradedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 5)
)
cienaCesModuleHealthStatusDegradedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginType"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginName"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginUnitId"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthSubCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatus"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesModuleHealthStatusDegradedNotification.setStatus(
        "current"
    )

cienaCesModuleHealthStatusGoodNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 6)
)
cienaCesModuleHealthStatusGoodNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginType"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginName"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthOriginUnitId"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthSubCategory"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatus"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesModuleHealthStatusGoodNotification.setStatus(
        "current"
    )

cienaCesModuleSensorHighTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 7)
)
cienaCesModuleSensorHighTempNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorDescription"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorCurrentTemp"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorHighTempThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesModuleSensorHighTempNotification.setStatus(
        "current"
    )

cienaCesModuleSensorLowTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 8)
)
cienaCesModuleSensorLowTempNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorDescription"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorCurrentTemp"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorLowTempThreshold"))
)
if mibBuilder.loadTexts:
    cienaCesModuleSensorLowTempNotification.setStatus(
        "current"
    )

cienaCesModuleSensorNormalTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 9)
)
cienaCesModuleSensorNormalTempNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorDescription"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorCurrentTemp"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorLowTemp"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorHighTemp"))
)
if mibBuilder.loadTexts:
    cienaCesModuleSensorNormalTempNotification.setStatus(
        "current"
    )

cienaCesModuleHASwitchOverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 10)
)
cienaCesModuleHASwitchOverNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSwitchOverReason"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleAdminState"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleOperState"))
)
if mibBuilder.loadTexts:
    cienaCesModuleHASwitchOverNotification.setStatus(
        "current"
    )

cienaCesModuleProtectionModeColdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 11)
)
cienaCesModuleProtectionModeColdNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSystemProtectionMode"))
)
if mibBuilder.loadTexts:
    cienaCesModuleProtectionModeColdNotification.setStatus(
        "current"
    )

cienaCesModuleProtectionModeWarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 12)
)
cienaCesModuleProtectionModeWarmNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSystemProtectionMode"))
)
if mibBuilder.loadTexts:
    cienaCesModuleProtectionModeWarmNotification.setStatus(
        "current"
    )

cienaCesModuleProtectionModeUnprotectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 13)
)
cienaCesModuleProtectionModeUnprotectedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSystemProtectionMode"))
)
if mibBuilder.loadTexts:
    cienaCesModuleProtectionModeUnprotectedNotification.setStatus(
        "current"
    )

cienaCesModuleProtectionModeHotNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 14)
)
cienaCesModuleProtectionModeHotNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSystemProtectionMode"))
)
if mibBuilder.loadTexts:
    cienaCesModuleProtectionModeHotNotification.setStatus(
        "current"
    )

cienaCesModulePostErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 15)
)
cienaCesModulePostErrorNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModulePOSTErrorDescription"))
)
if mibBuilder.loadTexts:
    cienaCesModulePostErrorNotification.setStatus(
        "current"
    )

cienaCesModuleFastReloadUnsuccessfulNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 16)
)
cienaCesModuleFastReloadUnsuccessfulNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleAdminState"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleOperState"))
)
if mibBuilder.loadTexts:
    cienaCesModuleFastReloadUnsuccessfulNotification.setStatus(
        "current"
    )

cienaCesModuleHitlessModeUnsuccessfulNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 17)
)
cienaCesModuleHitlessModeUnsuccessfulNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleAdminState"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleOperState"))
)
if mibBuilder.loadTexts:
    cienaCesModuleHitlessModeUnsuccessfulNotification.setStatus(
        "current"
    )

cienaCesModuleSwitchFabricDisruptedUnrecoverableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 18)
)
cienaCesModuleSwitchFabricDisruptedUnrecoverableNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"))
)
if mibBuilder.loadTexts:
    cienaCesModuleSwitchFabricDisruptedUnrecoverableNotification.setStatus(
        "current"
    )

cienaCesModuleSwitchFabricDisruptedRecoverableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 3, 0, 19)
)
cienaCesModuleSwitchFabricDisruptedRecoverableNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfNotifIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotNotifIndx"))
)
if mibBuilder.loadTexts:
    cienaCesModuleSwitchFabricDisruptedRecoverableNotification.setStatus(
        "current"
    )


# Notifications groups

moduleNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 2, 2, 2, 4)
)
moduleNotifGroup.setObjects(
      *(("CIENA-CES-MODULE-MIB", "cienaCesModuleStateChangeNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusUnknownNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusWarningNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusFaultedNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusDegradedNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHealthStatusGoodNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorHighTempNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorNormalTempNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSensorLowTempNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHASwitchOverNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleProtectionModeColdNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleProtectionModeWarmNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleProtectionModeUnprotectedNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleProtectionModeHotNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModulePostErrorNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleFastReloadUnsuccessfulNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleHitlessModeUnsuccessfulNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSwitchFabricDisruptedUnrecoverableNotification"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSwitchFabricDisruptedRecoverableNotification"))
)
if mibBuilder.loadTexts:
    moduleNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-MODULE-MIB",
    **{"SwPkgStatus": SwPkgStatus,
       "SwModuleState": SwModuleState,
       "TceHealthCategory": TceHealthCategory,
       "TceHealthStatus": TceHealthStatus,
       "HealthOriginType": HealthOriginType,
       "cienaCesModuleMIB": cienaCesModuleMIB,
       "cienaCesModuleMIBObjects": cienaCesModuleMIBObjects,
       "cienaCesModuleGlobal": cienaCesModuleGlobal,
       "cienaCesModuleGlobalPostState": cienaCesModuleGlobalPostState,
       "cienaCesModule": cienaCesModule,
       "cienaCesModuleTable": cienaCesModuleTable,
       "cienaCesModuleEntry": cienaCesModuleEntry,
       "cienaCesModuleChassisIndx": cienaCesModuleChassisIndx,
       "cienaCesModuleShelfIndx": cienaCesModuleShelfIndx,
       "cienaCesModuleSlotIndx": cienaCesModuleSlotIndx,
       "cienaCesModuleModel": cienaCesModuleModel,
       "cienaCesModuleType": cienaCesModuleType,
       "cienaCesModuleDescription": cienaCesModuleDescription,
       "cienaCesModuleAdminState": cienaCesModuleAdminState,
       "cienaCesModuleOperState": cienaCesModuleOperState,
       "cienaCesModuleProtectionRole": cienaCesModuleProtectionRole,
       "cienaCesModuleStandbyStatus": cienaCesModuleStandbyStatus,
       "cienaCesModuleLastRebootReason": cienaCesModuleLastRebootReason,
       "cienaCesModuleAdminPostState": cienaCesModuleAdminPostState,
       "cienaCesModuleOperPostState": cienaCesModuleOperPostState,
       "cienaCesModuleTrapState": cienaCesModuleTrapState,
       "cienaCesModuleChassisNotifIndx": cienaCesModuleChassisNotifIndx,
       "cienaCesModuleShelfNotifIndx": cienaCesModuleShelfNotifIndx,
       "cienaCesModuleSlotNotifIndx": cienaCesModuleSlotNotifIndx,
       "cienaCesModuleSlotName": cienaCesModuleSlotName,
       "cienaCesModuleDescriptionTable": cienaCesModuleDescriptionTable,
       "cienaCesModuleDescriptionEntry": cienaCesModuleDescriptionEntry,
       "cienaCesModuleDescriptionBoardName": cienaCesModuleDescriptionBoardName,
       "cienaCesModuleDescriptionBoardPartNum": cienaCesModuleDescriptionBoardPartNum,
       "cienaCesModuleDescriptionBoardSerialNum": cienaCesModuleDescriptionBoardSerialNum,
       "cienaCesModuleDescriptionBoardDesc": cienaCesModuleDescriptionBoardDesc,
       "cienaCesModuleDescriptionHwVersion": cienaCesModuleDescriptionHwVersion,
       "cienaCesModuleDescriptionMfgDate": cienaCesModuleDescriptionMfgDate,
       "cienaCesModuleDescriptionBaseMac": cienaCesModuleDescriptionBaseMac,
       "cienaCesModuleDescriptionUpTime": cienaCesModuleDescriptionUpTime,
       "cienaCesModuleDescriptionTotalNumPorts": cienaCesModuleDescriptionTotalNumPorts,
       "cienaCesModuleTempSensorTable": cienaCesModuleTempSensorTable,
       "cienaCesModuleTempSensorEntry": cienaCesModuleTempSensorEntry,
       "cienaCesModuleSensorIndx": cienaCesModuleSensorIndx,
       "cienaCesModuleSensorDescription": cienaCesModuleSensorDescription,
       "cienaCesModuleSensorCurrentTemp": cienaCesModuleSensorCurrentTemp,
       "cienaCesModuleSensorHighTemp": cienaCesModuleSensorHighTemp,
       "cienaCesModuleSensorLowTemp": cienaCesModuleSensorLowTemp,
       "cienaCesModuleSensorHighTempThreshold": cienaCesModuleSensorHighTempThreshold,
       "cienaCesModuleSensorLowTempThreshold": cienaCesModuleSensorLowTempThreshold,
       "cienaCesModuleSensorNotifIndx": cienaCesModuleSensorNotifIndx,
       "cienaCesSwModule": cienaCesSwModule,
       "cienaCesGlobalSwState": cienaCesGlobalSwState,
       "cienaCesModuleSwTable": cienaCesModuleSwTable,
       "cienaCesModuleSwEntry": cienaCesModuleSwEntry,
       "cienaCesModuleSwState": cienaCesModuleSwState,
       "cienaCesModuleSwRunningRelease": cienaCesModuleSwRunningRelease,
       "cienaCesModuleSwRunningReleasePartition": cienaCesModuleSwRunningReleasePartition,
       "cienaCesModuleSwReleasePartition0Pkg": cienaCesModuleSwReleasePartition0Pkg,
       "cienaCesModuleSwReleasePartition0PkgStatus": cienaCesModuleSwReleasePartition0PkgStatus,
       "cienaCesModuleSwReleasePartition1Pkg": cienaCesModuleSwReleasePartition1Pkg,
       "cienaCesModuleSwReleasePartition1PkgStatus": cienaCesModuleSwReleasePartition1PkgStatus,
       "cienaCesModuleSwReleasePartition2Pkg": cienaCesModuleSwReleasePartition2Pkg,
       "cienaCesModuleSwReleasePartition2PkgStatus": cienaCesModuleSwReleasePartition2PkgStatus,
       "cienaCesModuleSwBank0KernelVersion": cienaCesModuleSwBank0KernelVersion,
       "cienaCesModuleSwBank0KernelStatus": cienaCesModuleSwBank0KernelStatus,
       "cienaCesModuleSwBank1KernelVersion": cienaCesModuleSwBank1KernelVersion,
       "cienaCesModuleSwBank1KernelStatus": cienaCesModuleSwBank1KernelStatus,
       "cienaCesModuleSwBank0UbootVersion": cienaCesModuleSwBank0UbootVersion,
       "cienaCesModuleSwBank0UbootStatus": cienaCesModuleSwBank0UbootStatus,
       "cienaCesModuleSwBank1UbootVersion": cienaCesModuleSwBank1UbootVersion,
       "cienaCesModuleSwBank1UbootStatus": cienaCesModuleSwBank1UbootStatus,
       "cienaCesModuleSwUbootGoldVersion": cienaCesModuleSwUbootGoldVersion,
       "cienaCesModuleSwUbootGoldStatus": cienaCesModuleSwUbootGoldStatus,
       "cienaCesModuleSwMIBVer": cienaCesModuleSwMIBVer,
       "cienaCesModulePOSTErrorTable": cienaCesModulePOSTErrorTable,
       "cienaCesModulePOSTErrorEntry": cienaCesModulePOSTErrorEntry,
       "cienaCesModulePOSTErrorIndex": cienaCesModulePOSTErrorIndex,
       "cienaCesModulePOSTErrorDescription": cienaCesModulePOSTErrorDescription,
       "cienaCesModulePOSTErrorSeverity": cienaCesModulePOSTErrorSeverity,
       "cienaCesModulePOSTErrorScope": cienaCesModulePOSTErrorScope,
       "cienaCesModulePOSTScopeIndex": cienaCesModulePOSTScopeIndex,
       "cienaCesModuleResourceHealthTable": cienaCesModuleResourceHealthTable,
       "cienaCesModuleResourceHealthEntry": cienaCesModuleResourceHealthEntry,
       "cienaCesModuleResourceHealthSubCategory": cienaCesModuleResourceHealthSubCategory,
       "cienaCesModuleResourceDeviceIndx": cienaCesModuleResourceDeviceIndx,
       "cienaCesModuleResourceHealthState": cienaCesModuleResourceHealthState,
       "cienaCesModuleResourceHealthCurrMeasurement": cienaCesModuleResourceHealthCurrMeasurement,
       "cienaCesModuleResourceHealthMaxMeasurement": cienaCesModuleResourceHealthMaxMeasurement,
       "cienaCesModuleResourceHealthMaxThreshold": cienaCesModuleResourceHealthMaxThreshold,
       "cienaCesModuleIDPTable": cienaCesModuleIDPTable,
       "cienaCesModuleIDPEntry": cienaCesModuleIDPEntry,
       "cienaCesModuleIDPEthBaseMac": cienaCesModuleIDPEthBaseMac,
       "cienaCesModuleIDPEthBaseMacRange": cienaCesModuleIDPEthBaseMacRange,
       "cienaCesModuleIDPModuleSerialNumber": cienaCesModuleIDPModuleSerialNumber,
       "cienaCesModuleIDPModelPartNumber": cienaCesModuleIDPModelPartNumber,
       "cienaCesModuleIDPModelRevision": cienaCesModuleIDPModelRevision,
       "cienaCesModuleIDPProductID": cienaCesModuleIDPProductID,
       "cienaCesModuleIDPMfgDate": cienaCesModuleIDPMfgDate,
       "cienaCesModuleIDPCleiCode": cienaCesModuleIDPCleiCode,
       "cienaCesModuleIDPBarcode": cienaCesModuleIDPBarcode,
       "cienaCesModuleIDPSWCompat": cienaCesModuleIDPSWCompat,
       "cienaCesModuleIDPFTC": cienaCesModuleIDPFTC,
       "cienaCesModuleNotifAttrs": cienaCesModuleNotifAttrs,
       "cienaCesModuleSystemProtectionMode": cienaCesModuleSystemProtectionMode,
       "cienaCesModuleSwitchOverReason": cienaCesModuleSwitchOverReason,
       "cienaCesModuleNotifTable": cienaCesModuleNotifTable,
       "cienaCesModuleNotifEntry": cienaCesModuleNotifEntry,
       "cienaCesModuleHealthCategory": cienaCesModuleHealthCategory,
       "cienaCesModuleHealthSubCategory": cienaCesModuleHealthSubCategory,
       "cienaCesModuleHealthStatus": cienaCesModuleHealthStatus,
       "cienaCesModuleHealthStatusLast": cienaCesModuleHealthStatusLast,
       "cienaCesModuleHealthOriginType": cienaCesModuleHealthOriginType,
       "cienaCesModuleHealthOriginName": cienaCesModuleHealthOriginName,
       "cienaCesModuleHealthOriginUnitId": cienaCesModuleHealthOriginUnitId,
       "cienaCesModuleConformance": cienaCesModuleConformance,
       "cienaCesModuleMIBCompliances": cienaCesModuleMIBCompliances,
       "cienaCesModuleMIBGroups": cienaCesModuleMIBGroups,
       "moduleConfigGroup": moduleConfigGroup,
       "moduleDescriptionGroup": moduleDescriptionGroup,
       "moduleSensorGroup": moduleSensorGroup,
       "moduleNotifGroup": moduleNotifGroup,
       "modulePostErrorGroup": modulePostErrorGroup,
       "cienaCesModuleMIBNotificationPrefix": cienaCesModuleMIBNotificationPrefix,
       "cienaCesModuleMIBNotifications": cienaCesModuleMIBNotifications,
       "cienaCesModuleStateChangeNotification": cienaCesModuleStateChangeNotification,
       "cienaCesModuleHealthStatusUnknownNotification": cienaCesModuleHealthStatusUnknownNotification,
       "cienaCesModuleHealthStatusWarningNotification": cienaCesModuleHealthStatusWarningNotification,
       "cienaCesModuleHealthStatusFaultedNotification": cienaCesModuleHealthStatusFaultedNotification,
       "cienaCesModuleHealthStatusDegradedNotification": cienaCesModuleHealthStatusDegradedNotification,
       "cienaCesModuleHealthStatusGoodNotification": cienaCesModuleHealthStatusGoodNotification,
       "cienaCesModuleSensorHighTempNotification": cienaCesModuleSensorHighTempNotification,
       "cienaCesModuleSensorLowTempNotification": cienaCesModuleSensorLowTempNotification,
       "cienaCesModuleSensorNormalTempNotification": cienaCesModuleSensorNormalTempNotification,
       "cienaCesModuleHASwitchOverNotification": cienaCesModuleHASwitchOverNotification,
       "cienaCesModuleProtectionModeColdNotification": cienaCesModuleProtectionModeColdNotification,
       "cienaCesModuleProtectionModeWarmNotification": cienaCesModuleProtectionModeWarmNotification,
       "cienaCesModuleProtectionModeUnprotectedNotification": cienaCesModuleProtectionModeUnprotectedNotification,
       "cienaCesModuleProtectionModeHotNotification": cienaCesModuleProtectionModeHotNotification,
       "cienaCesModulePostErrorNotification": cienaCesModulePostErrorNotification,
       "cienaCesModuleFastReloadUnsuccessfulNotification": cienaCesModuleFastReloadUnsuccessfulNotification,
       "cienaCesModuleHitlessModeUnsuccessfulNotification": cienaCesModuleHitlessModeUnsuccessfulNotification,
       "cienaCesModuleSwitchFabricDisruptedUnrecoverableNotification": cienaCesModuleSwitchFabricDisruptedUnrecoverableNotification,
       "cienaCesModuleSwitchFabricDisruptedRecoverableNotification": cienaCesModuleSwitchFabricDisruptedRecoverableNotification}
)
