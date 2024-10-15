# SNMP MIB module (QBSYS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QBSYS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:37 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qbSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DateAndTimeForm(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )



class QbStorageType(Integer32, TextualConvention):
    status = "obsolete"
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
        *(("bootflash", 2),
          ("flash", 3),
          ("network", 1),
          ("nvram", 5),
          ("ram", 4))
    )



class QbFileType(Integer32, TextualConvention):
    status = "obsolete"
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
        *(("config", 2),
          ("diags", 5),
          ("dump", 3),
          ("eventLog", 4),
          ("image", 1))
    )



class QbFileImageType(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iotImage", 3),
          ("switchImage", 1),
          ("systemImage", 2))
    )



class QbTransferStatus(Integer32, TextualConvention):
    status = "obsolete"
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
        *(("aborted", 12),
          ("accessViolation", 2),
          ("alreadyRunning", 16),
          ("checksumError", 11),
          ("fileAlreadyExists", 6),
          ("fileNotFound", 1),
          ("generalError", 8),
          ("illegalOperation", 4),
          ("inProgress", 15),
          ("incompatibleFile", 9),
          ("noResponseFromServer", 10),
          ("noUser", 7),
          ("notEnoughSpace", 3),
          ("statusUnknown", 13),
          ("success", 14),
          ("unknownTransferID", 5))
    )



class QbSysApplId(Integer32, TextualConvention):
    status = "obsolete"
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
        *(("nfs", 3),
          ("snmp", 4),
          ("telnet", 2),
          ("www", 1))
    )



class ProtectionMode(Integer32, TextualConvention):
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
        *(("active", 2),
          ("clear", 6),
          ("force", 4),
          ("lockout", 3),
          ("manual", 5),
          ("protection", 1),
          ("standby", 8),
          ("unequipped", 9),
          ("unprotected", 7))
    )



class QbApsGroupMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 2))
    )



class QbApsSwitchMode(Integer32, TextualConvention):
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
        *(("clear", 2),
          ("force", 3),
          ("lockout", 5),
          ("manual", 4),
          ("noop", 1))
    )



class TimeStamp(TimeTicks, TextualConvention):
    status = "current"


class QbEventSrvAffect(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonServiceAffecting", 1),
          ("serviceAffecting", 2))
    )



class QbEventSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("off", 1))
    )



class QbAlarmCondition(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmClear", 2),
          ("alarmRaise", 1))
    )



class QbIoasSlot(Integer32, TextualConvention):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("au-1", 1),
          ("au-2", 2),
          ("au-3", 3),
          ("au-4", 4),
          ("au-5", 11),
          ("au-6", 12),
          ("au-7", 13),
          ("au-8", 14),
          ("main-a", 7),
          ("main-b", 8),
          ("proc-a", 6),
          ("proc-b", 10),
          ("sw-a", 5),
          ("sw-b", 9),
          ("sysctl", 15))
    )



class QbSysPortLoc(Integer32, TextualConvention):
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ioasDwsPort", 3),
          ("ioasPort", 1),
          ("ioasWanPort", 2),
          ("iotDs1Port1", 6),
          ("iotDs1Port2", 7),
          ("iotDs1Port3", 8),
          ("iotDs1Port4", 9),
          ("iotDwsPort", 4),
          ("iotEnetPort", 5),
          ("none", 0))
    )



class QbSysLedState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ledOff", 0),
          ("ledOn", 1))
    )



class QbNotificationAlarmCondition(Integer32, TextualConvention):
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
        *(("alarmClear", 2),
          ("alarmRaise", 1),
          ("none", 3))
    )



class QbNotificationType(Integer32, TextualConvention):
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
        *(("other", 3),
          ("qbAlarmNotification", 1),
          ("qbEventNotification", 2))
    )



class QbNotificationAction(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("added", 1),
          ("fault", 3),
          ("informational", 8),
          ("operStatusChange", 5),
          ("provisionedAttributeChange", 7),
          ("recovery", 4),
          ("removed", 2),
          ("stateChange", 6))
    )



class QbIotType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9,
              20,
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
              54)
        )
    )
    namedValues = NamedValues(
        *(("qb100", 9),
          ("qb100e", 20),
          ("qb100es", 45),
          ("qb100ew", 44),
          ("qb100s", 43),
          ("qb100w", 42),
          ("qb101", 46),
          ("qb101s", 48),
          ("qb101sw", 49),
          ("qb101w", 47),
          ("qb105", 50),
          ("qb105s", 52),
          ("qb105sw", 53),
          ("qb105w", 51),
          ("qb616sw", 54),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_QbSysObjects_ObjectIdentity = ObjectIdentity
qbSysObjects = _QbSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1)
)
_QbSysGeneralGroup_ObjectIdentity = ObjectIdentity
qbSysGeneralGroup = _QbSysGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1)
)
_QbSysDateTime_Type = DateAndTimeForm
_QbSysDateTime_Object = MibScalar
qbSysDateTime = _QbSysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 1),
    _QbSysDateTime_Type()
)
qbSysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysDateTime.setStatus("current")


class _QbSysOperStatus_Type(Integer32):
    """Custom type qbSysOperStatus based on Integer32"""
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
        *(("running", 2),
          ("testing", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_QbSysOperStatus_Type.__name__ = "Integer32"
_QbSysOperStatus_Object = MibScalar
qbSysOperStatus = _QbSysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 2),
    _QbSysOperStatus_Type()
)
qbSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysOperStatus.setStatus("current")


class _QbSysResetCtl_Type(Integer32):
    """Custom type qbSysResetCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2))
    )


_QbSysResetCtl_Type.__name__ = "Integer32"
_QbSysResetCtl_Object = MibScalar
qbSysResetCtl = _QbSysResetCtl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 3),
    _QbSysResetCtl_Type()
)
qbSysResetCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysResetCtl.setStatus("current")
_QbSysBootDiagsCode_Type = Integer32
_QbSysBootDiagsCode_Object = MibScalar
qbSysBootDiagsCode = _QbSysBootDiagsCode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 4),
    _QbSysBootDiagsCode_Type()
)
qbSysBootDiagsCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysBootDiagsCode.setStatus("current")


class _QbSysWatchdogUpdate_Type(Integer32):
    """Custom type qbSysWatchdogUpdate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 60),
    )


_QbSysWatchdogUpdate_Type.__name__ = "Integer32"
_QbSysWatchdogUpdate_Object = MibScalar
qbSysWatchdogUpdate = _QbSysWatchdogUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 5),
    _QbSysWatchdogUpdate_Type()
)
qbSysWatchdogUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysWatchdogUpdate.setStatus("current")
if mibBuilder.loadTexts:
    qbSysWatchdogUpdate.setUnits("seconds")
_QbSysRunningImageVersion_Type = DisplayString
_QbSysRunningImageVersion_Object = MibScalar
qbSysRunningImageVersion = _QbSysRunningImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 6),
    _QbSysRunningImageVersion_Type()
)
qbSysRunningImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysRunningImageVersion.setStatus("current")


class _QbSysPowerSupplyType_Type(Integer32):
    """Custom type qbSysPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_QbSysPowerSupplyType_Type.__name__ = "Integer32"
_QbSysPowerSupplyType_Object = MibScalar
qbSysPowerSupplyType = _QbSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 7),
    _QbSysPowerSupplyType_Type()
)
qbSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysPowerSupplyType.setStatus("current")


class _QbSysAcoCtl_Type(Integer32):
    """Custom type qbSysAcoCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("on", 1))
    )


_QbSysAcoCtl_Type.__name__ = "Integer32"
_QbSysAcoCtl_Object = MibScalar
qbSysAcoCtl = _QbSysAcoCtl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 8),
    _QbSysAcoCtl_Type()
)
qbSysAcoCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysAcoCtl.setStatus("current")


class _QbSysAutonomousStatus_Type(Integer32):
    """Custom type qbSysAutonomousStatus based on Integer32"""
    defaultValue = 2

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


_QbSysAutonomousStatus_Type.__name__ = "Integer32"
_QbSysAutonomousStatus_Object = MibScalar
qbSysAutonomousStatus = _QbSysAutonomousStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 9),
    _QbSysAutonomousStatus_Type()
)
qbSysAutonomousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAutonomousStatus.setStatus("current")
_QbSysDiscreteInputTable_Object = MibTable
qbSysDiscreteInputTable = _QbSysDiscreteInputTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    qbSysDiscreteInputTable.setStatus("current")
_QbSysDiscreteInputEntry_Object = MibTableRow
qbSysDiscreteInputEntry = _QbSysDiscreteInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 10, 1)
)
qbSysDiscreteInputEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysDiscreteInputType"),
)
if mibBuilder.loadTexts:
    qbSysDiscreteInputEntry.setStatus("current")


class _QbSysDiscreteInputType_Type(Integer32):
    """Custom type qbSysDiscreteInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QbSysDiscreteInputType_Type.__name__ = "Integer32"
_QbSysDiscreteInputType_Object = MibTableColumn
qbSysDiscreteInputType = _QbSysDiscreteInputType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 10, 1, 1),
    _QbSysDiscreteInputType_Type()
)
qbSysDiscreteInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysDiscreteInputType.setStatus("current")


class _QbSysDiscreteInputName_Type(DisplayString):
    """Custom type qbSysDiscreteInputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QbSysDiscreteInputName_Type.__name__ = "DisplayString"
_QbSysDiscreteInputName_Object = MibTableColumn
qbSysDiscreteInputName = _QbSysDiscreteInputName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 10, 1, 2),
    _QbSysDiscreteInputName_Type()
)
qbSysDiscreteInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysDiscreteInputName.setStatus("current")


class _QbSysDiscreteInputAdminStatus_Type(Integer32):
    """Custom type qbSysDiscreteInputAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )


_QbSysDiscreteInputAdminStatus_Type.__name__ = "Integer32"
_QbSysDiscreteInputAdminStatus_Object = MibTableColumn
qbSysDiscreteInputAdminStatus = _QbSysDiscreteInputAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 10, 1, 3),
    _QbSysDiscreteInputAdminStatus_Type()
)
qbSysDiscreteInputAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysDiscreteInputAdminStatus.setStatus("current")


class _QbSysDiscreteInputState_Type(Integer32):
    """Custom type qbSysDiscreteInputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("unknown", 1))
    )


_QbSysDiscreteInputState_Type.__name__ = "Integer32"
_QbSysDiscreteInputState_Object = MibTableColumn
qbSysDiscreteInputState = _QbSysDiscreteInputState_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 10, 1, 4),
    _QbSysDiscreteInputState_Type()
)
qbSysDiscreteInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysDiscreteInputState.setStatus("current")
_QbSysAgentGroup_ObjectIdentity = ObjectIdentity
qbSysAgentGroup = _QbSysAgentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11)
)
_QbSysSnmpRevision_Type = Unsigned32
_QbSysSnmpRevision_Object = MibScalar
qbSysSnmpRevision = _QbSysSnmpRevision_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 1),
    _QbSysSnmpRevision_Type()
)
qbSysSnmpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysSnmpRevision.setStatus("current")
_QbSysMgmtIpAddr_Type = IpAddress
_QbSysMgmtIpAddr_Object = MibScalar
qbSysMgmtIpAddr = _QbSysMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 2),
    _QbSysMgmtIpAddr_Type()
)
qbSysMgmtIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysMgmtIpAddr.setStatus("current")
_QbSysMgmtIpMask_Type = IpAddress
_QbSysMgmtIpMask_Object = MibScalar
qbSysMgmtIpMask = _QbSysMgmtIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 3),
    _QbSysMgmtIpMask_Type()
)
qbSysMgmtIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysMgmtIpMask.setStatus("current")
_QbSysDefaultIpRouter_Type = IpAddress
_QbSysDefaultIpRouter_Object = MibScalar
qbSysDefaultIpRouter = _QbSysDefaultIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 4),
    _QbSysDefaultIpRouter_Type()
)
qbSysDefaultIpRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysDefaultIpRouter.setStatus("current")


class _QbSysAgentReadCommunity_Type(DisplayString):
    """Custom type qbSysAgentReadCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_QbSysAgentReadCommunity_Type.__name__ = "DisplayString"
_QbSysAgentReadCommunity_Object = MibScalar
qbSysAgentReadCommunity = _QbSysAgentReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 5),
    _QbSysAgentReadCommunity_Type()
)
qbSysAgentReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysAgentReadCommunity.setStatus("current")


class _QbSysAgentReadWriteCommunity_Type(DisplayString):
    """Custom type qbSysAgentReadWriteCommunity based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_QbSysAgentReadWriteCommunity_Type.__name__ = "DisplayString"
_QbSysAgentReadWriteCommunity_Object = MibScalar
qbSysAgentReadWriteCommunity = _QbSysAgentReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 6),
    _QbSysAgentReadWriteCommunity_Type()
)
qbSysAgentReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysAgentReadWriteCommunity.setStatus("current")
_QbSysAgentTrapDestTable_Object = MibTable
qbSysAgentTrapDestTable = _QbSysAgentTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 7)
)
if mibBuilder.loadTexts:
    qbSysAgentTrapDestTable.setStatus("current")
_QbSysAgentTrapDestEntry_Object = MibTableRow
qbSysAgentTrapDestEntry = _QbSysAgentTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 7, 1)
)
qbSysAgentTrapDestEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysAgentTrapDestAddr"),
)
if mibBuilder.loadTexts:
    qbSysAgentTrapDestEntry.setStatus("current")
_QbSysAgentTrapDestAddr_Type = IpAddress
_QbSysAgentTrapDestAddr_Object = MibTableColumn
qbSysAgentTrapDestAddr = _QbSysAgentTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 7, 1, 1),
    _QbSysAgentTrapDestAddr_Type()
)
qbSysAgentTrapDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysAgentTrapDestAddr.setStatus("current")


class _QbSysAgentTrapDestFilter_Type(Integer32):
    """Custom type qbSysAgentTrapDestFilter based on Integer32"""
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
        *(("all", 4),
          ("critical", 3),
          ("major", 2),
          ("minor", 1))
    )


_QbSysAgentTrapDestFilter_Type.__name__ = "Integer32"
_QbSysAgentTrapDestFilter_Object = MibTableColumn
qbSysAgentTrapDestFilter = _QbSysAgentTrapDestFilter_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 7, 1, 2),
    _QbSysAgentTrapDestFilter_Type()
)
qbSysAgentTrapDestFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysAgentTrapDestFilter.setStatus("current")


class _QbSysAgentTrapDestComm_Type(DisplayString):
    """Custom type qbSysAgentTrapDestComm based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysAgentTrapDestComm_Type.__name__ = "DisplayString"
_QbSysAgentTrapDestComm_Object = MibTableColumn
qbSysAgentTrapDestComm = _QbSysAgentTrapDestComm_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 7, 1, 3),
    _QbSysAgentTrapDestComm_Type()
)
qbSysAgentTrapDestComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysAgentTrapDestComm.setStatus("current")
_QbSysAgentTrapDestRowStatus_Type = RowStatus
_QbSysAgentTrapDestRowStatus_Object = MibTableColumn
qbSysAgentTrapDestRowStatus = _QbSysAgentTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 7, 1, 4),
    _QbSysAgentTrapDestRowStatus_Type()
)
qbSysAgentTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysAgentTrapDestRowStatus.setStatus("current")


class _QbSysAgentTrapDestPort_Type(Integer32):
    """Custom type qbSysAgentTrapDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QbSysAgentTrapDestPort_Type.__name__ = "Integer32"
_QbSysAgentTrapDestPort_Object = MibTableColumn
qbSysAgentTrapDestPort = _QbSysAgentTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 7, 1, 5),
    _QbSysAgentTrapDestPort_Type()
)
qbSysAgentTrapDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysAgentTrapDestPort.setStatus("current")


class _QbSysDefaultRouterType_Type(Integer32):
    """Custom type qbSysDefaultRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmmgt", 2),
          ("enetmgt", 1),
          ("unknown", 0))
    )


_QbSysDefaultRouterType_Type.__name__ = "Integer32"
_QbSysDefaultRouterType_Object = MibScalar
qbSysDefaultRouterType = _QbSysDefaultRouterType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 8),
    _QbSysDefaultRouterType_Type()
)
qbSysDefaultRouterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysDefaultRouterType.setStatus("current")
_QbSysCliMsgCode_Type = Unsigned32
_QbSysCliMsgCode_Object = MibScalar
qbSysCliMsgCode = _QbSysCliMsgCode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 9),
    _QbSysCliMsgCode_Type()
)
qbSysCliMsgCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysCliMsgCode.setStatus("current")


class _QbRIPConfig_Type(Integer32):
    """Custom type qbRIPConfig based on Integer32"""
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


_QbRIPConfig_Type.__name__ = "Integer32"
_QbRIPConfig_Object = MibScalar
qbRIPConfig = _QbRIPConfig_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 11, 10),
    _QbRIPConfig_Type()
)
qbRIPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbRIPConfig.setStatus("current")
_QbSysFileGroup_ObjectIdentity = ObjectIdentity
qbSysFileGroup = _QbSysFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12)
)
_QbSysBootImageTable_Object = MibTable
qbSysBootImageTable = _QbSysBootImageTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    qbSysBootImageTable.setStatus("obsolete")
_QbSysBootImageEntry_Object = MibTableRow
qbSysBootImageEntry = _QbSysBootImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 1, 1)
)
qbSysBootImageEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysBootImageIndex"),
)
if mibBuilder.loadTexts:
    qbSysBootImageEntry.setStatus("obsolete")


class _QbSysBootImageIndex_Type(Integer32):
    """Custom type qbSysBootImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_QbSysBootImageIndex_Type.__name__ = "Integer32"
_QbSysBootImageIndex_Object = MibTableColumn
qbSysBootImageIndex = _QbSysBootImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 1, 1, 1),
    _QbSysBootImageIndex_Type()
)
qbSysBootImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysBootImageIndex.setStatus("obsolete")


class _QbSysBootImageName_Type(DisplayString):
    """Custom type qbSysBootImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_QbSysBootImageName_Type.__name__ = "DisplayString"
_QbSysBootImageName_Object = MibTableColumn
qbSysBootImageName = _QbSysBootImageName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 1, 1, 2),
    _QbSysBootImageName_Type()
)
qbSysBootImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysBootImageName.setStatus("obsolete")
_QbSysBootImageAddress_Type = Unsigned32
_QbSysBootImageAddress_Object = MibTableColumn
qbSysBootImageAddress = _QbSysBootImageAddress_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 1, 1, 3),
    _QbSysBootImageAddress_Type()
)
qbSysBootImageAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysBootImageAddress.setStatus("obsolete")
_QbSysTransferTable_Object = MibTable
qbSysTransferTable = _QbSysTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    qbSysTransferTable.setStatus("obsolete")
_QbSysTransferEntry_Object = MibTableRow
qbSysTransferEntry = _QbSysTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1)
)
qbSysTransferEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysTransferIndex"),
)
if mibBuilder.loadTexts:
    qbSysTransferEntry.setStatus("obsolete")


class _QbSysTransferIndex_Type(Unsigned32):
    """Custom type qbSysTransferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_QbSysTransferIndex_Type.__name__ = "Unsigned32"
_QbSysTransferIndex_Object = MibTableColumn
qbSysTransferIndex = _QbSysTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 1),
    _QbSysTransferIndex_Type()
)
qbSysTransferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysTransferIndex.setStatus("obsolete")


class _QbSysTransferSrc_Type(QbStorageType):
    """Custom type qbSysTransferSrc based on QbStorageType"""


_QbSysTransferSrc_Object = MibTableColumn
qbSysTransferSrc = _QbSysTransferSrc_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 2),
    _QbSysTransferSrc_Type()
)
qbSysTransferSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysTransferSrc.setStatus("obsolete")


class _QbSysTransferSrcName_Type(DisplayString):
    """Custom type qbSysTransferSrcName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_QbSysTransferSrcName_Type.__name__ = "DisplayString"
_QbSysTransferSrcName_Object = MibTableColumn
qbSysTransferSrcName = _QbSysTransferSrcName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 3),
    _QbSysTransferSrcName_Type()
)
qbSysTransferSrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysTransferSrcName.setStatus("obsolete")


class _QbSysTransferDest_Type(QbStorageType):
    """Custom type qbSysTransferDest based on QbStorageType"""


_QbSysTransferDest_Object = MibTableColumn
qbSysTransferDest = _QbSysTransferDest_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 4),
    _QbSysTransferDest_Type()
)
qbSysTransferDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysTransferDest.setStatus("obsolete")


class _QbSysTransferDestName_Type(DisplayString):
    """Custom type qbSysTransferDestName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_QbSysTransferDestName_Type.__name__ = "DisplayString"
_QbSysTransferDestName_Object = MibTableColumn
qbSysTransferDestName = _QbSysTransferDestName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 5),
    _QbSysTransferDestName_Type()
)
qbSysTransferDestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysTransferDestName.setStatus("obsolete")


class _QbSysTransferServerAddr_Type(IpAddress):
    """Custom type qbSysTransferServerAddr based on IpAddress"""
    defaultValue = 0


_QbSysTransferServerAddr_Object = MibTableColumn
qbSysTransferServerAddr = _QbSysTransferServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 6),
    _QbSysTransferServerAddr_Type()
)
qbSysTransferServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysTransferServerAddr.setStatus("obsolete")


class _QbSysTransferIot_Type(Unsigned32):
    """Custom type qbSysTransferIot based on Unsigned32"""
    defaultHexValue = 0


_QbSysTransferIot_Object = MibTableColumn
qbSysTransferIot = _QbSysTransferIot_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 7),
    _QbSysTransferIot_Type()
)
qbSysTransferIot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysTransferIot.setStatus("obsolete")
_QbSysTransferOperStatus_Type = QbTransferStatus
_QbSysTransferOperStatus_Object = MibTableColumn
qbSysTransferOperStatus = _QbSysTransferOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 8),
    _QbSysTransferOperStatus_Type()
)
qbSysTransferOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysTransferOperStatus.setStatus("obsolete")


class _QbSysTransferOperProgress_Type(Integer32):
    """Custom type qbSysTransferOperProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QbSysTransferOperProgress_Type.__name__ = "Integer32"
_QbSysTransferOperProgress_Object = MibTableColumn
qbSysTransferOperProgress = _QbSysTransferOperProgress_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 9),
    _QbSysTransferOperProgress_Type()
)
qbSysTransferOperProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysTransferOperProgress.setStatus("obsolete")
_QbSysTransferRowStatus_Type = RowStatus
_QbSysTransferRowStatus_Object = MibTableColumn
qbSysTransferRowStatus = _QbSysTransferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 12, 2, 1, 10),
    _QbSysTransferRowStatus_Type()
)
qbSysTransferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysTransferRowStatus.setStatus("obsolete")


class _QbSysResetVersion_Type(DisplayString):
    """Custom type qbSysResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbSysResetVersion_Type.__name__ = "DisplayString"
_QbSysResetVersion_Object = MibScalar
qbSysResetVersion = _QbSysResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 13),
    _QbSysResetVersion_Type()
)
qbSysResetVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysResetVersion.setStatus("current")


class _QbSysFeatureKeys_Type(Bits):
    """Custom type qbSysFeatureKeys based on Bits"""
    namedValues = NamedValues(
        *(("qbSysAtmKey", 0),
          ("qbSysTdmKey", 1))
    )

_QbSysFeatureKeys_Type.__name__ = "Bits"
_QbSysFeatureKeys_Object = MibScalar
qbSysFeatureKeys = _QbSysFeatureKeys_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 14),
    _QbSysFeatureKeys_Type()
)
qbSysFeatureKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysFeatureKeys.setStatus("current")


class _QbSysPortBwSharing_Type(Integer32):
    """Custom type qbSysPortBwSharing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(155, 155),
        ValueRangeConstraint(311, 311),
        ValueRangeConstraint(466, 466),
        ValueRangeConstraint(622, 622),
    )


_QbSysPortBwSharing_Type.__name__ = "Integer32"
_QbSysPortBwSharing_Object = MibScalar
qbSysPortBwSharing = _QbSysPortBwSharing_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 15),
    _QbSysPortBwSharing_Type()
)
qbSysPortBwSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysPortBwSharing.setStatus("current")


class _QbSysTestLeds_Type(Integer32):
    """Custom type qbSysTestLeds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("test", 2))
    )


_QbSysTestLeds_Type.__name__ = "Integer32"
_QbSysTestLeds_Object = MibScalar
qbSysTestLeds = _QbSysTestLeds_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 16),
    _QbSysTestLeds_Type()
)
qbSysTestLeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysTestLeds.setStatus("current")
_QbSysSwAccepted_Type = TruthValue
_QbSysSwAccepted_Object = MibScalar
qbSysSwAccepted = _QbSysSwAccepted_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 17),
    _QbSysSwAccepted_Type()
)
qbSysSwAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysSwAccepted.setStatus("current")


class _QbChassisSysType_Type(Integer32):
    """Custom type qbChassisSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("qb3000", 3),
          ("qb5000", 2))
    )


_QbChassisSysType_Type.__name__ = "Integer32"
_QbChassisSysType_Object = MibScalar
qbChassisSysType = _QbChassisSysType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 18),
    _QbChassisSysType_Type()
)
qbChassisSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbChassisSysType.setStatus("current")


class _QbChassisBkplType_Type(Integer32):
    """Custom type qbChassisBkplType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("giga2", 2),
          ("giga5", 3),
          ("other", 1))
    )


_QbChassisBkplType_Type.__name__ = "Integer32"
_QbChassisBkplType_Object = MibScalar
qbChassisBkplType = _QbChassisBkplType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 19),
    _QbChassisBkplType_Type()
)
qbChassisBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbChassisBkplType.setStatus("current")


class _QbChassisNumSlots_Type(Integer32):
    """Custom type qbChassisNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QbChassisNumSlots_Type.__name__ = "Integer32"
_QbChassisNumSlots_Object = MibScalar
qbChassisNumSlots = _QbChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 20),
    _QbChassisNumSlots_Type()
)
qbChassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbChassisNumSlots.setStatus("current")


class _QbChassisBulkStatsCtl_Type(Integer32):
    """Custom type qbChassisBulkStatsCtl based on Integer32"""
    defaultValue = 2

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


_QbChassisBulkStatsCtl_Type.__name__ = "Integer32"
_QbChassisBulkStatsCtl_Object = MibScalar
qbChassisBulkStatsCtl = _QbChassisBulkStatsCtl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 1, 21),
    _QbChassisBulkStatsCtl_Type()
)
qbChassisBulkStatsCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbChassisBulkStatsCtl.setStatus("current")
_QbSysConfigParamsGroup_ObjectIdentity = ObjectIdentity
qbSysConfigParamsGroup = _QbSysConfigParamsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 2)
)
_QbSysConfigLastWriteDateTime_Type = DateAndTimeForm
_QbSysConfigLastWriteDateTime_Object = MibScalar
qbSysConfigLastWriteDateTime = _QbSysConfigLastWriteDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 2, 1),
    _QbSysConfigLastWriteDateTime_Type()
)
qbSysConfigLastWriteDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysConfigLastWriteDateTime.setStatus("current")
_QbSysConfigLastWriteSource_Type = IpAddress
_QbSysConfigLastWriteSource_Object = MibScalar
qbSysConfigLastWriteSource = _QbSysConfigLastWriteSource_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 2, 2),
    _QbSysConfigLastWriteSource_Type()
)
qbSysConfigLastWriteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysConfigLastWriteSource.setStatus("current")


class _QbSysProvType_Type(Integer32):
    """Custom type qbSysProvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("provConnection", 2),
          ("provIot", 1))
    )


_QbSysProvType_Type.__name__ = "Integer32"
_QbSysProvType_Object = MibScalar
qbSysProvType = _QbSysProvType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 2, 3),
    _QbSysProvType_Type()
)
qbSysProvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysProvType.setStatus("current")
_QbSysEventsGroup_ObjectIdentity = ObjectIdentity
qbSysEventsGroup = _QbSysEventsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3)
)
_QbSysEventHistoryTable_Object = MibTable
qbSysEventHistoryTable = _QbSysEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qbSysEventHistoryTable.setStatus("current")
_QbSysEventHistoryEntry_Object = MibTableRow
qbSysEventHistoryEntry = _QbSysEventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1)
)
qbSysEventHistoryEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysEventHistoryIndex"),
)
if mibBuilder.loadTexts:
    qbSysEventHistoryEntry.setStatus("current")
_QbSysEventHistoryIndex_Type = Unsigned32
_QbSysEventHistoryIndex_Object = MibTableColumn
qbSysEventHistoryIndex = _QbSysEventHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1, 1),
    _QbSysEventHistoryIndex_Type()
)
qbSysEventHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysEventHistoryIndex.setStatus("current")
_QbSysEventHistoryDateTime_Type = DateAndTimeForm
_QbSysEventHistoryDateTime_Object = MibTableColumn
qbSysEventHistoryDateTime = _QbSysEventHistoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1, 2),
    _QbSysEventHistoryDateTime_Type()
)
qbSysEventHistoryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistoryDateTime.setStatus("current")
_QbSysEventHistorySubsystem_Type = DisplayString
_QbSysEventHistorySubsystem_Object = MibTableColumn
qbSysEventHistorySubsystem = _QbSysEventHistorySubsystem_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1, 3),
    _QbSysEventHistorySubsystem_Type()
)
qbSysEventHistorySubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistorySubsystem.setStatus("current")
_QbSysEventHistorySrvAffect_Type = QbEventSrvAffect
_QbSysEventHistorySrvAffect_Object = MibTableColumn
qbSysEventHistorySrvAffect = _QbSysEventHistorySrvAffect_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1, 4),
    _QbSysEventHistorySrvAffect_Type()
)
qbSysEventHistorySrvAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistorySrvAffect.setStatus("current")
_QbSysEventHistorySeverity_Type = QbEventSeverity
_QbSysEventHistorySeverity_Object = MibTableColumn
qbSysEventHistorySeverity = _QbSysEventHistorySeverity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1, 5),
    _QbSysEventHistorySeverity_Type()
)
qbSysEventHistorySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistorySeverity.setStatus("current")


class _QbSysEventHistoryId_Type(Unsigned32):
    """Custom type qbSysEventHistoryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbSysEventHistoryId_Type.__name__ = "Unsigned32"
_QbSysEventHistoryId_Object = MibTableColumn
qbSysEventHistoryId = _QbSysEventHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1, 6),
    _QbSysEventHistoryId_Type()
)
qbSysEventHistoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistoryId.setStatus("current")
_QbSysEventHistoryMsg_Type = DisplayString
_QbSysEventHistoryMsg_Object = MibTableColumn
qbSysEventHistoryMsg = _QbSysEventHistoryMsg_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 1, 1, 7),
    _QbSysEventHistoryMsg_Type()
)
qbSysEventHistoryMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistoryMsg.setStatus("current")


class _QbSysEventHistoryMaxTableSize_Type(Integer32):
    """Custom type qbSysEventHistoryMaxTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QbSysEventHistoryMaxTableSize_Type.__name__ = "Integer32"
_QbSysEventHistoryMaxTableSize_Object = MibScalar
qbSysEventHistoryMaxTableSize = _QbSysEventHistoryMaxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 2),
    _QbSysEventHistoryMaxTableSize_Type()
)
qbSysEventHistoryMaxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistoryMaxTableSize.setStatus("current")
if mibBuilder.loadTexts:
    qbSysEventHistoryMaxTableSize.setUnits("number of events")
_QbSysEventHistoryOutFilterLevel_Type = QbEventSeverity
_QbSysEventHistoryOutFilterLevel_Object = MibScalar
qbSysEventHistoryOutFilterLevel = _QbSysEventHistoryOutFilterLevel_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 3),
    _QbSysEventHistoryOutFilterLevel_Type()
)
qbSysEventHistoryOutFilterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistoryOutFilterLevel.setStatus("obsolete")
_QbSysEventHistoryOutFilterDateTime_Type = DateAndTimeForm
_QbSysEventHistoryOutFilterDateTime_Object = MibScalar
qbSysEventHistoryOutFilterDateTime = _QbSysEventHistoryOutFilterDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 4),
    _QbSysEventHistoryOutFilterDateTime_Type()
)
qbSysEventHistoryOutFilterDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistoryOutFilterDateTime.setStatus("obsolete")


class _QbSysEventHistoryClearAllCtl_Type(Integer32):
    """Custom type qbSysEventHistoryClearAllCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ready", 1))
    )


_QbSysEventHistoryClearAllCtl_Type.__name__ = "Integer32"
_QbSysEventHistoryClearAllCtl_Object = MibScalar
qbSysEventHistoryClearAllCtl = _QbSysEventHistoryClearAllCtl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 5),
    _QbSysEventHistoryClearAllCtl_Type()
)
qbSysEventHistoryClearAllCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysEventHistoryClearAllCtl.setStatus("current")
_QbSysAlarmTable_Object = MibTable
qbSysAlarmTable = _QbSysAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    qbSysAlarmTable.setStatus("current")
_QbSysAlarmEntry_Object = MibTableRow
qbSysAlarmEntry = _QbSysAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1)
)
qbSysAlarmEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysAlarmIndex"),
)
if mibBuilder.loadTexts:
    qbSysAlarmEntry.setStatus("current")
_QbSysAlarmIndex_Type = Unsigned32
_QbSysAlarmIndex_Object = MibTableColumn
qbSysAlarmIndex = _QbSysAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 1),
    _QbSysAlarmIndex_Type()
)
qbSysAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysAlarmIndex.setStatus("current")
_QbSysAlarmDateTime_Type = DateAndTimeForm
_QbSysAlarmDateTime_Object = MibTableColumn
qbSysAlarmDateTime = _QbSysAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 2),
    _QbSysAlarmDateTime_Type()
)
qbSysAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmDateTime.setStatus("current")
_QbSysAlarmSubsystem_Type = DisplayString
_QbSysAlarmSubsystem_Object = MibTableColumn
qbSysAlarmSubsystem = _QbSysAlarmSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 3),
    _QbSysAlarmSubsystem_Type()
)
qbSysAlarmSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmSubsystem.setStatus("current")
_QbSysAlarmSrvAffect_Type = QbEventSrvAffect
_QbSysAlarmSrvAffect_Object = MibTableColumn
qbSysAlarmSrvAffect = _QbSysAlarmSrvAffect_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 4),
    _QbSysAlarmSrvAffect_Type()
)
qbSysAlarmSrvAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmSrvAffect.setStatus("current")
_QbSysAlarmSeverity_Type = QbEventSeverity
_QbSysAlarmSeverity_Object = MibTableColumn
qbSysAlarmSeverity = _QbSysAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 5),
    _QbSysAlarmSeverity_Type()
)
qbSysAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmSeverity.setStatus("current")
_QbSysAlarmCondition_Type = QbAlarmCondition
_QbSysAlarmCondition_Object = MibTableColumn
qbSysAlarmCondition = _QbSysAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 6),
    _QbSysAlarmCondition_Type()
)
qbSysAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmCondition.setStatus("current")


class _QbSysAlarmId_Type(Unsigned32):
    """Custom type qbSysAlarmId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbSysAlarmId_Type.__name__ = "Unsigned32"
_QbSysAlarmId_Object = MibTableColumn
qbSysAlarmId = _QbSysAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 7),
    _QbSysAlarmId_Type()
)
qbSysAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmId.setStatus("current")
_QbSysAlarmMsg_Type = DisplayString
_QbSysAlarmMsg_Object = MibTableColumn
qbSysAlarmMsg = _QbSysAlarmMsg_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 8),
    _QbSysAlarmMsg_Type()
)
qbSysAlarmMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmMsg.setStatus("current")
_QbSysAlarmResource_Type = ObjectIdentifier
_QbSysAlarmResource_Object = MibTableColumn
qbSysAlarmResource = _QbSysAlarmResource_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 6, 1, 9),
    _QbSysAlarmResource_Type()
)
qbSysAlarmResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmResource.setStatus("current")
_QbSysAlarmHistoryTable_Object = MibTable
qbSysAlarmHistoryTable = _QbSysAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    qbSysAlarmHistoryTable.setStatus("current")
_QbSysAlarmHistoryEntry_Object = MibTableRow
qbSysAlarmHistoryEntry = _QbSysAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1)
)
qbSysAlarmHistoryEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysAlarmHistoryIndex"),
)
if mibBuilder.loadTexts:
    qbSysAlarmHistoryEntry.setStatus("current")
_QbSysAlarmHistoryIndex_Type = Unsigned32
_QbSysAlarmHistoryIndex_Object = MibTableColumn
qbSysAlarmHistoryIndex = _QbSysAlarmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 1),
    _QbSysAlarmHistoryIndex_Type()
)
qbSysAlarmHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryIndex.setStatus("current")
_QbSysAlarmHistoryDateTime_Type = DateAndTimeForm
_QbSysAlarmHistoryDateTime_Object = MibTableColumn
qbSysAlarmHistoryDateTime = _QbSysAlarmHistoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 2),
    _QbSysAlarmHistoryDateTime_Type()
)
qbSysAlarmHistoryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryDateTime.setStatus("current")
_QbSysAlarmHistorySubsystem_Type = DisplayString
_QbSysAlarmHistorySubsystem_Object = MibTableColumn
qbSysAlarmHistorySubsystem = _QbSysAlarmHistorySubsystem_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 3),
    _QbSysAlarmHistorySubsystem_Type()
)
qbSysAlarmHistorySubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistorySubsystem.setStatus("current")
_QbSysAlarmHistorySrvAffect_Type = QbEventSrvAffect
_QbSysAlarmHistorySrvAffect_Object = MibTableColumn
qbSysAlarmHistorySrvAffect = _QbSysAlarmHistorySrvAffect_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 4),
    _QbSysAlarmHistorySrvAffect_Type()
)
qbSysAlarmHistorySrvAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistorySrvAffect.setStatus("current")
_QbSysAlarmHistorySeverity_Type = QbEventSeverity
_QbSysAlarmHistorySeverity_Object = MibTableColumn
qbSysAlarmHistorySeverity = _QbSysAlarmHistorySeverity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 5),
    _QbSysAlarmHistorySeverity_Type()
)
qbSysAlarmHistorySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistorySeverity.setStatus("current")
_QbSysAlarmHistoryCondition_Type = QbAlarmCondition
_QbSysAlarmHistoryCondition_Object = MibTableColumn
qbSysAlarmHistoryCondition = _QbSysAlarmHistoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 6),
    _QbSysAlarmHistoryCondition_Type()
)
qbSysAlarmHistoryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryCondition.setStatus("current")


class _QbSysAlarmHistoryId_Type(Unsigned32):
    """Custom type qbSysAlarmHistoryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbSysAlarmHistoryId_Type.__name__ = "Unsigned32"
_QbSysAlarmHistoryId_Object = MibTableColumn
qbSysAlarmHistoryId = _QbSysAlarmHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 7),
    _QbSysAlarmHistoryId_Type()
)
qbSysAlarmHistoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryId.setStatus("current")
_QbSysAlarmHistoryMsg_Type = DisplayString
_QbSysAlarmHistoryMsg_Object = MibTableColumn
qbSysAlarmHistoryMsg = _QbSysAlarmHistoryMsg_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 7, 1, 8),
    _QbSysAlarmHistoryMsg_Type()
)
qbSysAlarmHistoryMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryMsg.setStatus("current")


class _QbSysAlarmHistoryMaxTableSize_Type(Integer32):
    """Custom type qbSysAlarmHistoryMaxTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QbSysAlarmHistoryMaxTableSize_Type.__name__ = "Integer32"
_QbSysAlarmHistoryMaxTableSize_Object = MibScalar
qbSysAlarmHistoryMaxTableSize = _QbSysAlarmHistoryMaxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 8),
    _QbSysAlarmHistoryMaxTableSize_Type()
)
qbSysAlarmHistoryMaxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryMaxTableSize.setStatus("current")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryMaxTableSize.setUnits("number of events")
_QbSysAlarmHistoryOutFilterLevel_Type = QbEventSeverity
_QbSysAlarmHistoryOutFilterLevel_Object = MibScalar
qbSysAlarmHistoryOutFilterLevel = _QbSysAlarmHistoryOutFilterLevel_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 9),
    _QbSysAlarmHistoryOutFilterLevel_Type()
)
qbSysAlarmHistoryOutFilterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryOutFilterLevel.setStatus("obsolete")
_QbSysAlarmHistoryOutFilterDateTime_Type = DateAndTimeForm
_QbSysAlarmHistoryOutFilterDateTime_Object = MibScalar
qbSysAlarmHistoryOutFilterDateTime = _QbSysAlarmHistoryOutFilterDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 10),
    _QbSysAlarmHistoryOutFilterDateTime_Type()
)
qbSysAlarmHistoryOutFilterDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryOutFilterDateTime.setStatus("current")


class _QbSysAlarmHistoryClearAllCtl_Type(Integer32):
    """Custom type qbSysAlarmHistoryClearAllCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ready", 1))
    )


_QbSysAlarmHistoryClearAllCtl_Type.__name__ = "Integer32"
_QbSysAlarmHistoryClearAllCtl_Object = MibScalar
qbSysAlarmHistoryClearAllCtl = _QbSysAlarmHistoryClearAllCtl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 11),
    _QbSysAlarmHistoryClearAllCtl_Type()
)
qbSysAlarmHistoryClearAllCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryClearAllCtl.setStatus("current")
_QbSysEventIdTable_Object = MibTable
qbSysEventIdTable = _QbSysEventIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 12)
)
if mibBuilder.loadTexts:
    qbSysEventIdTable.setStatus("current")
_QbSysEventIdEntry_Object = MibTableRow
qbSysEventIdEntry = _QbSysEventIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 12, 1)
)
qbSysEventIdEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysEventDescrId"),
)
if mibBuilder.loadTexts:
    qbSysEventIdEntry.setStatus("current")
_QbSysEventDescrId_Type = Unsigned32
_QbSysEventDescrId_Object = MibTableColumn
qbSysEventDescrId = _QbSysEventDescrId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 12, 1, 1),
    _QbSysEventDescrId_Type()
)
qbSysEventDescrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysEventDescrId.setStatus("current")


class _QbSysEventIdName_Type(DisplayString):
    """Custom type qbSysEventIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QbSysEventIdName_Type.__name__ = "DisplayString"
_QbSysEventIdName_Object = MibTableColumn
qbSysEventIdName = _QbSysEventIdName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 12, 1, 2),
    _QbSysEventIdName_Type()
)
qbSysEventIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventIdName.setStatus("current")
_QbSysEventIdSeverity_Type = QbEventSeverity
_QbSysEventIdSeverity_Object = MibTableColumn
qbSysEventIdSeverity = _QbSysEventIdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 12, 1, 3),
    _QbSysEventIdSeverity_Type()
)
qbSysEventIdSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventIdSeverity.setStatus("current")
_QbSysEventIdSASeverity_Type = QbEventSeverity
_QbSysEventIdSASeverity_Object = MibTableColumn
qbSysEventIdSASeverity = _QbSysEventIdSASeverity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 12, 1, 4),
    _QbSysEventIdSASeverity_Type()
)
qbSysEventIdSASeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventIdSASeverity.setStatus("current")
_QbSysEventAsTrap_Type = TruthValue
_QbSysEventAsTrap_Object = MibTableColumn
qbSysEventAsTrap = _QbSysEventAsTrap_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 12, 1, 5),
    _QbSysEventAsTrap_Type()
)
qbSysEventAsTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventAsTrap.setStatus("current")
_QbSysAlarmIdTable_Object = MibTable
qbSysAlarmIdTable = _QbSysAlarmIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 13)
)
if mibBuilder.loadTexts:
    qbSysAlarmIdTable.setStatus("current")
_QbSysAlarmIdEntry_Object = MibTableRow
qbSysAlarmIdEntry = _QbSysAlarmIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 13, 1)
)
qbSysAlarmIdEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysAlarmId"),
)
if mibBuilder.loadTexts:
    qbSysAlarmIdEntry.setStatus("current")
_QbSysAlarmDescrId_Type = Unsigned32
_QbSysAlarmDescrId_Object = MibTableColumn
qbSysAlarmDescrId = _QbSysAlarmDescrId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 13, 1, 1),
    _QbSysAlarmDescrId_Type()
)
qbSysAlarmDescrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysAlarmDescrId.setStatus("current")


class _QbSysAlarmIdName_Type(DisplayString):
    """Custom type qbSysAlarmIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QbSysAlarmIdName_Type.__name__ = "DisplayString"
_QbSysAlarmIdName_Object = MibTableColumn
qbSysAlarmIdName = _QbSysAlarmIdName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 13, 1, 2),
    _QbSysAlarmIdName_Type()
)
qbSysAlarmIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmIdName.setStatus("current")
_QbSysAlarmIdSeverity_Type = QbEventSeverity
_QbSysAlarmIdSeverity_Object = MibTableColumn
qbSysAlarmIdSeverity = _QbSysAlarmIdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 13, 1, 3),
    _QbSysAlarmIdSeverity_Type()
)
qbSysAlarmIdSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmIdSeverity.setStatus("current")
_QbSysAlarmIdSASeverity_Type = QbEventSeverity
_QbSysAlarmIdSASeverity_Object = MibTableColumn
qbSysAlarmIdSASeverity = _QbSysAlarmIdSASeverity_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 13, 1, 4),
    _QbSysAlarmIdSASeverity_Type()
)
qbSysAlarmIdSASeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmIdSASeverity.setStatus("current")
_QbSysAlarmAsTrap_Type = TruthValue
_QbSysAlarmAsTrap_Object = MibTableColumn
qbSysAlarmAsTrap = _QbSysAlarmAsTrap_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 13, 1, 5),
    _QbSysAlarmAsTrap_Type()
)
qbSysAlarmAsTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmAsTrap.setStatus("current")
_QbSysNotificationHistoryTable_Object = MibTable
qbSysNotificationHistoryTable = _QbSysNotificationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14)
)
if mibBuilder.loadTexts:
    qbSysNotificationHistoryTable.setStatus("current")
_QbSysNotificationHistoryEntry_Object = MibTableRow
qbSysNotificationHistoryEntry = _QbSysNotificationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1)
)
qbSysNotificationHistoryEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryIndex"),
)
if mibBuilder.loadTexts:
    qbSysNotificationHistoryEntry.setStatus("current")
_QbSysNotificationHistoryIndex_Type = Unsigned32
_QbSysNotificationHistoryIndex_Object = MibTableColumn
qbSysNotificationHistoryIndex = _QbSysNotificationHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 1),
    _QbSysNotificationHistoryIndex_Type()
)
qbSysNotificationHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryIndex.setStatus("current")
_QbSysNotificationOID_Type = ObjectIdentifier
_QbSysNotificationOID_Object = MibTableColumn
qbSysNotificationOID = _QbSysNotificationOID_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 2),
    _QbSysNotificationOID_Type()
)
qbSysNotificationOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationOID.setStatus("current")
_QbSysNotificationHistoryType_Type = QbNotificationType
_QbSysNotificationHistoryType_Object = MibTableColumn
qbSysNotificationHistoryType = _QbSysNotificationHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 3),
    _QbSysNotificationHistoryType_Type()
)
qbSysNotificationHistoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryType.setStatus("current")
_QbSysNotificationHistoryTypeId_Type = Unsigned32
_QbSysNotificationHistoryTypeId_Object = MibTableColumn
qbSysNotificationHistoryTypeId = _QbSysNotificationHistoryTypeId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 4),
    _QbSysNotificationHistoryTypeId_Type()
)
qbSysNotificationHistoryTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryTypeId.setStatus("current")
_QbSysNotificationHistoryAction_Type = QbNotificationAction
_QbSysNotificationHistoryAction_Object = MibTableColumn
qbSysNotificationHistoryAction = _QbSysNotificationHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 5),
    _QbSysNotificationHistoryAction_Type()
)
qbSysNotificationHistoryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryAction.setStatus("current")
_QbSysNotificationHistoryResource_Type = ObjectIdentifier
_QbSysNotificationHistoryResource_Object = MibTableColumn
qbSysNotificationHistoryResource = _QbSysNotificationHistoryResource_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 6),
    _QbSysNotificationHistoryResource_Type()
)
qbSysNotificationHistoryResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryResource.setStatus("current")
_QbSysNotificationHistoryCookie_Type = Unsigned32
_QbSysNotificationHistoryCookie_Object = MibTableColumn
qbSysNotificationHistoryCookie = _QbSysNotificationHistoryCookie_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 7),
    _QbSysNotificationHistoryCookie_Type()
)
qbSysNotificationHistoryCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryCookie.setStatus("current")
_QbSysNotificationHistoryDateTime_Type = DateAndTimeForm
_QbSysNotificationHistoryDateTime_Object = MibTableColumn
qbSysNotificationHistoryDateTime = _QbSysNotificationHistoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 8),
    _QbSysNotificationHistoryDateTime_Type()
)
qbSysNotificationHistoryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryDateTime.setStatus("current")
_QbSysNotificationHistoryAlarmCondition_Type = QbNotificationAlarmCondition
_QbSysNotificationHistoryAlarmCondition_Object = MibTableColumn
qbSysNotificationHistoryAlarmCondition = _QbSysNotificationHistoryAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 9),
    _QbSysNotificationHistoryAlarmCondition_Type()
)
qbSysNotificationHistoryAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryAlarmCondition.setStatus("current")
_QbSysNotificationHistoryServiceAffecting_Type = QbEventSrvAffect
_QbSysNotificationHistoryServiceAffecting_Object = MibTableColumn
qbSysNotificationHistoryServiceAffecting = _QbSysNotificationHistoryServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 14, 1, 10),
    _QbSysNotificationHistoryServiceAffecting_Type()
)
qbSysNotificationHistoryServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryServiceAffecting.setStatus("current")


class _QbSysNotificationHistoryMaxTableSize_Type(Integer32):
    """Custom type qbSysNotificationHistoryMaxTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QbSysNotificationHistoryMaxTableSize_Type.__name__ = "Integer32"
_QbSysNotificationHistoryMaxTableSize_Object = MibScalar
qbSysNotificationHistoryMaxTableSize = _QbSysNotificationHistoryMaxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 15),
    _QbSysNotificationHistoryMaxTableSize_Type()
)
qbSysNotificationHistoryMaxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryMaxTableSize.setStatus("current")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryMaxTableSize.setUnits("number of events")
_QbSysNotificationHistoryOutFilterLevel_Type = QbEventSeverity
_QbSysNotificationHistoryOutFilterLevel_Object = MibScalar
qbSysNotificationHistoryOutFilterLevel = _QbSysNotificationHistoryOutFilterLevel_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 16),
    _QbSysNotificationHistoryOutFilterLevel_Type()
)
qbSysNotificationHistoryOutFilterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryOutFilterLevel.setStatus("obsolete")
_QbSysNotificationHistoryOutFilterDateTime_Type = DateAndTimeForm
_QbSysNotificationHistoryOutFilterDateTime_Object = MibScalar
qbSysNotificationHistoryOutFilterDateTime = _QbSysNotificationHistoryOutFilterDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 17),
    _QbSysNotificationHistoryOutFilterDateTime_Type()
)
qbSysNotificationHistoryOutFilterDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryOutFilterDateTime.setStatus("obsolete")


class _QbSysNotificationHistoryClearAllCtl_Type(Integer32):
    """Custom type qbSysNotificationHistoryClearAllCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ready", 1))
    )


_QbSysNotificationHistoryClearAllCtl_Type.__name__ = "Integer32"
_QbSysNotificationHistoryClearAllCtl_Object = MibScalar
qbSysNotificationHistoryClearAllCtl = _QbSysNotificationHistoryClearAllCtl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 18),
    _QbSysNotificationHistoryClearAllCtl_Type()
)
qbSysNotificationHistoryClearAllCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysNotificationHistoryClearAllCtl.setStatus("obsolete")
_QbSysAlarmHistoryLastIndex_Type = Integer32
_QbSysAlarmHistoryLastIndex_Object = MibScalar
qbSysAlarmHistoryLastIndex = _QbSysAlarmHistoryLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 19),
    _QbSysAlarmHistoryLastIndex_Type()
)
qbSysAlarmHistoryLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysAlarmHistoryLastIndex.setStatus("current")
_QbSysEventHistoryLastIndex_Type = Integer32
_QbSysEventHistoryLastIndex_Object = MibScalar
qbSysEventHistoryLastIndex = _QbSysEventHistoryLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 20),
    _QbSysEventHistoryLastIndex_Type()
)
qbSysEventHistoryLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysEventHistoryLastIndex.setStatus("current")
_QbSysGlobalHistoryLastIndex_Type = Integer32
_QbSysGlobalHistoryLastIndex_Object = MibScalar
qbSysGlobalHistoryLastIndex = _QbSysGlobalHistoryLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 3, 21),
    _QbSysGlobalHistoryLastIndex_Type()
)
qbSysGlobalHistoryLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysGlobalHistoryLastIndex.setStatus("current")
_QbSysModuleGroup_ObjectIdentity = ObjectIdentity
qbSysModuleGroup = _QbSysModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4)
)
_QbSysModuleTable_Object = MibTable
qbSysModuleTable = _QbSysModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qbSysModuleTable.setStatus("current")
_QbSysModuleEntry_Object = MibTableRow
qbSysModuleEntry = _QbSysModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1)
)
qbSysModuleEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
)
if mibBuilder.loadTexts:
    qbSysModuleEntry.setStatus("current")


class _QbSysModuleSlot_Type(Integer32):
    """Custom type qbSysModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QbSysModuleSlot_Type.__name__ = "Integer32"
_QbSysModuleSlot_Object = MibTableColumn
qbSysModuleSlot = _QbSysModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 1),
    _QbSysModuleSlot_Type()
)
qbSysModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleSlot.setStatus("current")


class _QbSysModuleType_Type(Integer32):
    """Custom type qbSysModuleType based on Integer32"""
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
              15,
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
              1000)
        )
    )
    namedValues = NamedValues(
        *(("dws", 2),
          ("dws155s", 22),
          ("dws155sw", 29),
          ("dws622s", 24),
          ("dws622sw", 8),
          ("dws622w", 21),
          ("empty", 19),
          ("enhSwitchProc", 20),
          ("es24-10-100", 25),
          ("gigesw", 32),
          ("main", 1),
          ("other", 18),
          ("q155", 5),
          ("q155-T", 9),
          ("q155LR", 30),
          ("q155LR-T", 31),
          ("s622", 7),
          ("s622-T", 11),
          ("s622LR", 27),
          ("s622LR-T", 28),
          ("switch", 4),
          ("switchGiga2", 15),
          ("switchProc", 3),
          ("syscon", 17),
          ("sysconII", 23),
          ("t1E1-16", 26),
          ("unknown", 1000),
          ("vt155", 6),
          ("vt155-T", 10))
    )


_QbSysModuleType_Type.__name__ = "Integer32"
_QbSysModuleType_Object = MibTableColumn
qbSysModuleType = _QbSysModuleType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 2),
    _QbSysModuleType_Type()
)
qbSysModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleType.setStatus("current")


class _QbSysModuleName_Type(DisplayString):
    """Custom type qbSysModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysModuleName_Type.__name__ = "DisplayString"
_QbSysModuleName_Object = MibTableColumn
qbSysModuleName = _QbSysModuleName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 3),
    _QbSysModuleName_Type()
)
qbSysModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysModuleName.setStatus("current")


class _QbSysModuleOperStatus_Type(Integer32):
    """Custom type qbSysModuleOperStatus based on Integer32"""
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
        *(("empty", 2),
          ("failed", 7),
          ("inService", 5),
          ("init", 3),
          ("other", 1),
          ("recovery", 4),
          ("removed", 6))
    )


_QbSysModuleOperStatus_Type.__name__ = "Integer32"
_QbSysModuleOperStatus_Object = MibTableColumn
qbSysModuleOperStatus = _QbSysModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 4),
    _QbSysModuleOperStatus_Type()
)
qbSysModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleOperStatus.setStatus("current")


class _QbSysModuleAdminStatus_Type(Integer32):
    """Custom type qbSysModuleAdminStatus based on Integer32"""
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
        *(("clearslot", 5),
          ("disable", 4),
          ("enable", 3),
          ("other", 1),
          ("reset", 2))
    )


_QbSysModuleAdminStatus_Type.__name__ = "Integer32"
_QbSysModuleAdminStatus_Object = MibTableColumn
qbSysModuleAdminStatus = _QbSysModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 5),
    _QbSysModuleAdminStatus_Type()
)
qbSysModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysModuleAdminStatus.setStatus("current")


class _QbSysModuleTestResult_Type(Integer32):
    """Custom type qbSysModuleTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QbSysModuleTestResult_Type.__name__ = "Integer32"
_QbSysModuleTestResult_Object = MibTableColumn
qbSysModuleTestResult = _QbSysModuleTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 6),
    _QbSysModuleTestResult_Type()
)
qbSysModuleTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleTestResult.setStatus("current")


class _QbSysModuleNumPorts_Type(Integer32):
    """Custom type qbSysModuleNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QbSysModuleNumPorts_Type.__name__ = "Integer32"
_QbSysModuleNumPorts_Object = MibTableColumn
qbSysModuleNumPorts = _QbSysModuleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 7),
    _QbSysModuleNumPorts_Type()
)
qbSysModuleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleNumPorts.setStatus("current")


class _QbSysModulePortStatus_Type(OctetString):
    """Custom type qbSysModulePortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QbSysModulePortStatus_Type.__name__ = "OctetString"
_QbSysModulePortStatus_Object = MibTableColumn
qbSysModulePortStatus = _QbSysModulePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 8),
    _QbSysModulePortStatus_Type()
)
qbSysModulePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModulePortStatus.setStatus("current")


class _QbSysModuleModel_Type(DisplayString):
    """Custom type qbSysModuleModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysModuleModel_Type.__name__ = "DisplayString"
_QbSysModuleModel_Object = MibTableColumn
qbSysModuleModel = _QbSysModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 9),
    _QbSysModuleModel_Type()
)
qbSysModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleModel.setStatus("current")


class _QbSysModuleSerialNum_Type(DisplayString):
    """Custom type qbSysModuleSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysModuleSerialNum_Type.__name__ = "DisplayString"
_QbSysModuleSerialNum_Object = MibTableColumn
qbSysModuleSerialNum = _QbSysModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 10),
    _QbSysModuleSerialNum_Type()
)
qbSysModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleSerialNum.setStatus("current")


class _QbSysModuleEqId_Type(DisplayString):
    """Custom type qbSysModuleEqId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysModuleEqId_Type.__name__ = "DisplayString"
_QbSysModuleEqId_Object = MibTableColumn
qbSysModuleEqId = _QbSysModuleEqId_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 11),
    _QbSysModuleEqId_Type()
)
qbSysModuleEqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleEqId.setStatus("current")


class _QbSysModuleHwVersion_Type(DisplayString):
    """Custom type qbSysModuleHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_QbSysModuleHwVersion_Type.__name__ = "DisplayString"
_QbSysModuleHwVersion_Object = MibTableColumn
qbSysModuleHwVersion = _QbSysModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 12),
    _QbSysModuleHwVersion_Type()
)
qbSysModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleHwVersion.setStatus("current")


class _QbSysModuleSwVersion_Type(DisplayString):
    """Custom type qbSysModuleSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_QbSysModuleSwVersion_Type.__name__ = "DisplayString"
_QbSysModuleSwVersion_Object = MibTableColumn
qbSysModuleSwVersion = _QbSysModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 13),
    _QbSysModuleSwVersion_Type()
)
qbSysModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleSwVersion.setStatus("current")


class _QbSysModuleProtectionMode_Type(ProtectionMode):
    """Custom type qbSysModuleProtectionMode based on ProtectionMode"""


_QbSysModuleProtectionMode_Object = MibTableColumn
qbSysModuleProtectionMode = _QbSysModuleProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 14),
    _QbSysModuleProtectionMode_Type()
)
qbSysModuleProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysModuleProtectionMode.setStatus("current")
_QbSysModuleLastSwitchoverTime_Type = TimeStamp
_QbSysModuleLastSwitchoverTime_Object = MibTableColumn
qbSysModuleLastSwitchoverTime = _QbSysModuleLastSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 15),
    _QbSysModuleLastSwitchoverTime_Type()
)
qbSysModuleLastSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleLastSwitchoverTime.setStatus("current")


class _QbSysModuleSwitchoverReason_Type(Integer32):
    """Custom type qbSysModuleSwitchoverReason based on Integer32"""
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
        *(("moduleFailed", 4),
          ("moduleInserted", 7),
          ("moduleRecovered", 5),
          ("moduleRemoved", 6),
          ("none", 1),
          ("unknown", 2),
          ("userInitiated", 3))
    )


_QbSysModuleSwitchoverReason_Type.__name__ = "Integer32"
_QbSysModuleSwitchoverReason_Object = MibTableColumn
qbSysModuleSwitchoverReason = _QbSysModuleSwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 16),
    _QbSysModuleSwitchoverReason_Type()
)
qbSysModuleSwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleSwitchoverReason.setStatus("current")


class _QbSysModuleLedStatus_Type(OctetString):
    """Custom type qbSysModuleLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbSysModuleLedStatus_Type.__name__ = "OctetString"
_QbSysModuleLedStatus_Object = MibTableColumn
qbSysModuleLedStatus = _QbSysModuleLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 17),
    _QbSysModuleLedStatus_Type()
)
qbSysModuleLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleLedStatus.setStatus("current")


class _QbSysModuleProductName_Type(DisplayString):
    """Custom type qbSysModuleProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysModuleProductName_Type.__name__ = "DisplayString"
_QbSysModuleProductName_Object = MibTableColumn
qbSysModuleProductName = _QbSysModuleProductName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 18),
    _QbSysModuleProductName_Type()
)
qbSysModuleProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleProductName.setStatus("current")


class _QbSysModuleTestLeds_Type(Integer32):
    """Custom type qbSysModuleTestLeds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("test", 2))
    )


_QbSysModuleTestLeds_Type.__name__ = "Integer32"
_QbSysModuleTestLeds_Object = MibTableColumn
qbSysModuleTestLeds = _QbSysModuleTestLeds_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 1, 1, 19),
    _QbSysModuleTestLeds_Type()
)
qbSysModuleTestLeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysModuleTestLeds.setStatus("current")


class _QbSysApsAlarmStatus_Type(Integer32):
    """Custom type qbSysApsAlarmStatus based on Integer32"""
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


_QbSysApsAlarmStatus_Type.__name__ = "Integer32"
_QbSysApsAlarmStatus_Object = MibScalar
qbSysApsAlarmStatus = _QbSysApsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 2),
    _QbSysApsAlarmStatus_Type()
)
qbSysApsAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysApsAlarmStatus.setStatus("current")
_QbSysModuleApsTable_Object = MibTable
qbSysModuleApsTable = _QbSysModuleApsTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    qbSysModuleApsTable.setStatus("current")
_QbSysModuleApsEntry_Object = MibTableRow
qbSysModuleApsEntry = _QbSysModuleApsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 3, 1)
)
qbSysModuleApsEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
)
if mibBuilder.loadTexts:
    qbSysModuleApsEntry.setStatus("current")
_QbSysModuleApsGroupAdminMode_Type = QbApsGroupMode
_QbSysModuleApsGroupAdminMode_Object = MibTableColumn
qbSysModuleApsGroupAdminMode = _QbSysModuleApsGroupAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 3, 1, 1),
    _QbSysModuleApsGroupAdminMode_Type()
)
qbSysModuleApsGroupAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysModuleApsGroupAdminMode.setStatus("current")


class _QbSysModuleApsGroupOperMode_Type(Integer32):
    """Custom type qbSysModuleApsGroupOperMode based on Integer32"""
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
        *(("active", 3),
          ("standby", 4),
          ("unavailable", 1),
          ("unprotected", 2))
    )


_QbSysModuleApsGroupOperMode_Type.__name__ = "Integer32"
_QbSysModuleApsGroupOperMode_Object = MibTableColumn
qbSysModuleApsGroupOperMode = _QbSysModuleApsGroupOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 3, 1, 2),
    _QbSysModuleApsGroupOperMode_Type()
)
qbSysModuleApsGroupOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleApsGroupOperMode.setStatus("current")
_QbSysModuleApsSwitchAdminMode_Type = QbApsSwitchMode
_QbSysModuleApsSwitchAdminMode_Object = MibTableColumn
qbSysModuleApsSwitchAdminMode = _QbSysModuleApsSwitchAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 3, 1, 3),
    _QbSysModuleApsSwitchAdminMode_Type()
)
qbSysModuleApsSwitchAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysModuleApsSwitchAdminMode.setStatus("current")


class _QbSysModuleApsSwitchOperMode_Type(Integer32):
    """Custom type qbSysModuleApsSwitchOperMode based on Integer32"""
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
        *(("clear", 2),
          ("fail", 8),
          ("force", 4),
          ("lockout", 3),
          ("manual", 5),
          ("noop", 1),
          ("sd", 7),
          ("sf", 6))
    )


_QbSysModuleApsSwitchOperMode_Type.__name__ = "Integer32"
_QbSysModuleApsSwitchOperMode_Object = MibTableColumn
qbSysModuleApsSwitchOperMode = _QbSysModuleApsSwitchOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 3, 1, 4),
    _QbSysModuleApsSwitchOperMode_Type()
)
qbSysModuleApsSwitchOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleApsSwitchOperMode.setStatus("current")
_QbSysModuleApsLastSwitchoverTime_Type = TimeStamp
_QbSysModuleApsLastSwitchoverTime_Object = MibTableColumn
qbSysModuleApsLastSwitchoverTime = _QbSysModuleApsLastSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 4, 3, 1, 5),
    _QbSysModuleApsLastSwitchoverTime_Type()
)
qbSysModuleApsLastSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysModuleApsLastSwitchoverTime.setStatus("current")
_QbSysPortGroup_ObjectIdentity = ObjectIdentity
qbSysPortGroup = _QbSysPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5)
)
_QbSysPortTable_Object = MibTable
qbSysPortTable = _QbSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    qbSysPortTable.setStatus("current")
_QbSysPortEntry_Object = MibTableRow
qbSysPortEntry = _QbSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1, 1)
)
qbSysPortEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
    (0, "QBSYS-SYSTEM-MIB", "qbSysPort"),
)
if mibBuilder.loadTexts:
    qbSysPortEntry.setStatus("current")


class _QbSysPort_Type(Integer32):
    """Custom type qbSysPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QbSysPort_Type.__name__ = "Integer32"
_QbSysPort_Object = MibTableColumn
qbSysPort = _QbSysPort_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1, 1, 1),
    _QbSysPort_Type()
)
qbSysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysPort.setStatus("current")


class _QbSysPortName_Type(DisplayString):
    """Custom type qbSysPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysPortName_Type.__name__ = "DisplayString"
_QbSysPortName_Object = MibTableColumn
qbSysPortName = _QbSysPortName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1, 1, 2),
    _QbSysPortName_Type()
)
qbSysPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysPortName.setStatus("current")


class _QbSysPortType_Type(Integer32):
    """Custom type qbSysPortType based on Integer32"""
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
        *(("atmOc3", 5),
          ("dws", 4),
          ("e10100BaseT", 2),
          ("main", 3),
          ("unknown", 1))
    )


_QbSysPortType_Type.__name__ = "Integer32"
_QbSysPortType_Object = MibTableColumn
qbSysPortType = _QbSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1, 1, 3),
    _QbSysPortType_Type()
)
qbSysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysPortType.setStatus("current")


class _QbSysPortOperStatus_Type(Integer32):
    """Custom type qbSysPortOperStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_QbSysPortOperStatus_Type.__name__ = "Integer32"
_QbSysPortOperStatus_Object = MibTableColumn
qbSysPortOperStatus = _QbSysPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1, 1, 4),
    _QbSysPortOperStatus_Type()
)
qbSysPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysPortOperStatus.setStatus("current")


class _QbSysPortIfIndex_Type(Unsigned32):
    """Custom type qbSysPortIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QbSysPortIfIndex_Type.__name__ = "Unsigned32"
_QbSysPortIfIndex_Object = MibTableColumn
qbSysPortIfIndex = _QbSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1, 1, 5),
    _QbSysPortIfIndex_Type()
)
qbSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysPortIfIndex.setStatus("current")


class _QbSysPortLoopbackConfig_Type(Integer32):
    """Custom type qbSysPortLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("facility", 2),
          ("terminal", 3),
          ("unloop", 1))
    )


_QbSysPortLoopbackConfig_Type.__name__ = "Integer32"
_QbSysPortLoopbackConfig_Object = MibTableColumn
qbSysPortLoopbackConfig = _QbSysPortLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 5, 1, 1, 6),
    _QbSysPortLoopbackConfig_Type()
)
qbSysPortLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysPortLoopbackConfig.setStatus("current")
_QbSysIotGroup_ObjectIdentity = ObjectIdentity
qbSysIotGroup = _QbSysIotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6)
)
_QbSysIotTable_Object = MibTable
qbSysIotTable = _QbSysIotTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9)
)
if mibBuilder.loadTexts:
    qbSysIotTable.setStatus("current")
_QbSysIotEntry_Object = MibTableRow
qbSysIotEntry = _QbSysIotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1)
)
qbSysIotEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysIotSerialNumber"),
)
if mibBuilder.loadTexts:
    qbSysIotEntry.setStatus("current")
_QbSysIotSerialNumber_Type = Unsigned32
_QbSysIotSerialNumber_Object = MibTableColumn
qbSysIotSerialNumber = _QbSysIotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 1),
    _QbSysIotSerialNumber_Type()
)
qbSysIotSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysIotSerialNumber.setStatus("current")
_QbSysIoasDwsIfIndex_Type = InterfaceIndex
_QbSysIoasDwsIfIndex_Object = MibTableColumn
qbSysIoasDwsIfIndex = _QbSysIoasDwsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 2),
    _QbSysIoasDwsIfIndex_Type()
)
qbSysIoasDwsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIoasDwsIfIndex.setStatus("current")


class _QbSysIotAddr_Type(Unsigned32):
    """Custom type qbSysIotAddr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QbSysIotAddr_Type.__name__ = "Unsigned32"
_QbSysIotAddr_Object = MibTableColumn
qbSysIotAddr = _QbSysIotAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 3),
    _QbSysIotAddr_Type()
)
qbSysIotAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotAddr.setStatus("current")


class _QbSysIotDescr_Type(DisplayString):
    """Custom type qbSysIotDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QbSysIotDescr_Type.__name__ = "DisplayString"
_QbSysIotDescr_Object = MibTableColumn
qbSysIotDescr = _QbSysIotDescr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 4),
    _QbSysIotDescr_Type()
)
qbSysIotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotDescr.setStatus("current")


class _QbSysIotName_Type(DisplayString):
    """Custom type qbSysIotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QbSysIotName_Type.__name__ = "DisplayString"
_QbSysIotName_Object = MibTableColumn
qbSysIotName = _QbSysIotName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 5),
    _QbSysIotName_Type()
)
qbSysIotName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotName.setStatus("current")


class _QbSysIotLocation_Type(DisplayString):
    """Custom type qbSysIotLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QbSysIotLocation_Type.__name__ = "DisplayString"
_QbSysIotLocation_Object = MibTableColumn
qbSysIotLocation = _QbSysIotLocation_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 6),
    _QbSysIotLocation_Type()
)
qbSysIotLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotLocation.setStatus("current")


class _QbSysIotSwVersion_Type(DisplayString):
    """Custom type qbSysIotSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbSysIotSwVersion_Type.__name__ = "DisplayString"
_QbSysIotSwVersion_Object = MibTableColumn
qbSysIotSwVersion = _QbSysIotSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 7),
    _QbSysIotSwVersion_Type()
)
qbSysIotSwVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotSwVersion.setStatus("current")


class _QbSysIotHwVersion_Type(DisplayString):
    """Custom type qbSysIotHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_QbSysIotHwVersion_Type.__name__ = "DisplayString"
_QbSysIotHwVersion_Object = MibTableColumn
qbSysIotHwVersion = _QbSysIotHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 8),
    _QbSysIotHwVersion_Type()
)
qbSysIotHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotHwVersion.setStatus("current")


class _QbSysIotAdminStatus_Type(Integer32):
    """Custom type qbSysIotAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 6),
          ("enable", 5),
          ("range", 3),
          ("reset", 1),
          ("standby", 4))
    )


_QbSysIotAdminStatus_Type.__name__ = "Integer32"
_QbSysIotAdminStatus_Object = MibTableColumn
qbSysIotAdminStatus = _QbSysIotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 9),
    _QbSysIotAdminStatus_Type()
)
qbSysIotAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotAdminStatus.setStatus("current")


class _QbSysIotOperStatus_Type(Integer32):
    """Custom type qbSysIotOperStatus based on Integer32"""
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
        *(("down", 3),
          ("fault", 6),
          ("inService", 8),
          ("maintenance", 7),
          ("other", 1),
          ("rangingInProgress", 5),
          ("running", 2),
          ("standBy", 4))
    )


_QbSysIotOperStatus_Type.__name__ = "Integer32"
_QbSysIotOperStatus_Object = MibTableColumn
qbSysIotOperStatus = _QbSysIotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 10),
    _QbSysIotOperStatus_Type()
)
qbSysIotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotOperStatus.setStatus("current")


class _QbSysIotDsx1LineCoding_Type(Integer32):
    """Custom type qbSysIotDsx1LineCoding based on Integer32"""
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
        *(("dsx1AMI", 5),
          ("dsx1B6ZS", 7),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1JBZS", 1),
          ("dsx1ZBTSI", 4),
          ("other", 6))
    )


_QbSysIotDsx1LineCoding_Type.__name__ = "Integer32"
_QbSysIotDsx1LineCoding_Object = MibTableColumn
qbSysIotDsx1LineCoding = _QbSysIotDsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 11),
    _QbSysIotDsx1LineCoding_Type()
)
qbSysIotDsx1LineCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotDsx1LineCoding.setStatus("current")


class _QbSysIotSerialStr_Type(DisplayString):
    """Custom type qbSysIotSerialStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbSysIotSerialStr_Type.__name__ = "DisplayString"
_QbSysIotSerialStr_Object = MibTableColumn
qbSysIotSerialStr = _QbSysIotSerialStr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 12),
    _QbSysIotSerialStr_Type()
)
qbSysIotSerialStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotSerialStr.setStatus("current")
_QbSysIotRowStatus_Type = RowStatus
_QbSysIotRowStatus_Object = MibTableColumn
qbSysIotRowStatus = _QbSysIotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 13),
    _QbSysIotRowStatus_Type()
)
qbSysIotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotRowStatus.setStatus("current")


class _QbSysIotManufSerialNum_Type(DisplayString):
    """Custom type qbSysIotManufSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_QbSysIotManufSerialNum_Type.__name__ = "DisplayString"
_QbSysIotManufSerialNum_Object = MibTableColumn
qbSysIotManufSerialNum = _QbSysIotManufSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 14),
    _QbSysIotManufSerialNum_Type()
)
qbSysIotManufSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotManufSerialNum.setStatus("current")
_QbSysIotType_Type = QbIotType
_QbSysIotType_Object = MibTableColumn
qbSysIotType = _QbSysIotType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 15),
    _QbSysIotType_Type()
)
qbSysIotType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotType.setStatus("current")


class _QbSysIotProductName_Type(DisplayString):
    """Custom type qbSysIotProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QbSysIotProductName_Type.__name__ = "DisplayString"
_QbSysIotProductName_Object = MibTableColumn
qbSysIotProductName = _QbSysIotProductName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 16),
    _QbSysIotProductName_Type()
)
qbSysIotProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotProductName.setStatus("current")


class _QbSysIotSignalFmt_Type(Integer32):
    """Custom type qbSysIotSignalFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("e1", 2))
    )


_QbSysIotSignalFmt_Type.__name__ = "Integer32"
_QbSysIotSignalFmt_Object = MibTableColumn
qbSysIotSignalFmt = _QbSysIotSignalFmt_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 17),
    _QbSysIotSignalFmt_Type()
)
qbSysIotSignalFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotSignalFmt.setStatus("current")
_QbSysIotRollSerialNumber_Type = Unsigned32
_QbSysIotRollSerialNumber_Object = MibTableColumn
qbSysIotRollSerialNumber = _QbSysIotRollSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 18),
    _QbSysIotRollSerialNumber_Type()
)
qbSysIotRollSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qbSysIotRollSerialNumber.setStatus("current")


class _QbSysIotNumSlots_Type(Integer32):
    """Custom type qbSysIotNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_QbSysIotNumSlots_Type.__name__ = "Integer32"
_QbSysIotNumSlots_Object = MibTableColumn
qbSysIotNumSlots = _QbSysIotNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 9, 1, 19),
    _QbSysIotNumSlots_Type()
)
qbSysIotNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotNumSlots.setStatus("current")
_QbSysIotFileTable_Object = MibTable
qbSysIotFileTable = _QbSysIotFileTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10)
)
if mibBuilder.loadTexts:
    qbSysIotFileTable.setStatus("current")
_QbSysIotFileEntry_Object = MibTableRow
qbSysIotFileEntry = _QbSysIotFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1)
)
qbSysIotFileEntry.setIndexNames(
    (0, "QBSYS-SYSTEM-MIB", "qbSysIotFileSerialNumber"),
)
if mibBuilder.loadTexts:
    qbSysIotFileEntry.setStatus("current")
_QbSysIotFileSerialNumber_Type = Unsigned32
_QbSysIotFileSerialNumber_Object = MibTableColumn
qbSysIotFileSerialNumber = _QbSysIotFileSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 1),
    _QbSysIotFileSerialNumber_Type()
)
qbSysIotFileSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbSysIotFileSerialNumber.setStatus("current")


class _QbSysIotFileAvailableVersion1_Type(DisplayString):
    """Custom type qbSysIotFileAvailableVersion1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysIotFileAvailableVersion1_Type.__name__ = "DisplayString"
_QbSysIotFileAvailableVersion1_Object = MibTableColumn
qbSysIotFileAvailableVersion1 = _QbSysIotFileAvailableVersion1_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 2),
    _QbSysIotFileAvailableVersion1_Type()
)
qbSysIotFileAvailableVersion1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileAvailableVersion1.setStatus("current")


class _QbSysIotFileAvailableVersion2_Type(DisplayString):
    """Custom type qbSysIotFileAvailableVersion2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysIotFileAvailableVersion2_Type.__name__ = "DisplayString"
_QbSysIotFileAvailableVersion2_Object = MibTableColumn
qbSysIotFileAvailableVersion2 = _QbSysIotFileAvailableVersion2_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 3),
    _QbSysIotFileAvailableVersion2_Type()
)
qbSysIotFileAvailableVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileAvailableVersion2.setStatus("current")


class _QbSysIotFileRunningVersion_Type(DisplayString):
    """Custom type qbSysIotFileRunningVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysIotFileRunningVersion_Type.__name__ = "DisplayString"
_QbSysIotFileRunningVersion_Object = MibTableColumn
qbSysIotFileRunningVersion = _QbSysIotFileRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 4),
    _QbSysIotFileRunningVersion_Type()
)
qbSysIotFileRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileRunningVersion.setStatus("current")


class _QbSysIotFileAcceptedVersion_Type(DisplayString):
    """Custom type qbSysIotFileAcceptedVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysIotFileAcceptedVersion_Type.__name__ = "DisplayString"
_QbSysIotFileAcceptedVersion_Object = MibTableColumn
qbSysIotFileAcceptedVersion = _QbSysIotFileAcceptedVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 5),
    _QbSysIotFileAcceptedVersion_Type()
)
qbSysIotFileAcceptedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileAcceptedVersion.setStatus("current")


class _QbSysIotFileDownLoadVersion_Type(DisplayString):
    """Custom type qbSysIotFileDownLoadVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QbSysIotFileDownLoadVersion_Type.__name__ = "DisplayString"
_QbSysIotFileDownLoadVersion_Object = MibTableColumn
qbSysIotFileDownLoadVersion = _QbSysIotFileDownLoadVersion_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 6),
    _QbSysIotFileDownLoadVersion_Type()
)
qbSysIotFileDownLoadVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysIotFileDownLoadVersion.setStatus("current")
_QbSysIotFileSysUpTime_Type = TimeTicks
_QbSysIotFileSysUpTime_Object = MibTableColumn
qbSysIotFileSysUpTime = _QbSysIotFileSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 7),
    _QbSysIotFileSysUpTime_Type()
)
qbSysIotFileSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileSysUpTime.setStatus("current")
_QbSysIotFileLastModification_Type = TimeTicks
_QbSysIotFileLastModification_Object = MibTableColumn
qbSysIotFileLastModification = _QbSysIotFileLastModification_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 8),
    _QbSysIotFileLastModification_Type()
)
qbSysIotFileLastModification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileLastModification.setStatus("current")


class _QbSysIotFileAction_Type(Integer32):
    """Custom type qbSysIotFileAction based on Integer32"""
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
        *(("accept", 2),
          ("downLoad", 3),
          ("downLoadAbort", 4),
          ("noAction", 1))
    )


_QbSysIotFileAction_Type.__name__ = "Integer32"
_QbSysIotFileAction_Object = MibTableColumn
qbSysIotFileAction = _QbSysIotFileAction_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 9),
    _QbSysIotFileAction_Type()
)
qbSysIotFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbSysIotFileAction.setStatus("current")


class _QbSysIotFileDownLoadStatus_Type(Integer32):
    """Custom type qbSysIotFileDownLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("failed", 3),
          ("idle", 1))
    )


_QbSysIotFileDownLoadStatus_Type.__name__ = "Integer32"
_QbSysIotFileDownLoadStatus_Object = MibTableColumn
qbSysIotFileDownLoadStatus = _QbSysIotFileDownLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 10),
    _QbSysIotFileDownLoadStatus_Type()
)
qbSysIotFileDownLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileDownLoadStatus.setStatus("current")


class _QbSysIotFileErrorMsg_Type(DisplayString):
    """Custom type qbSysIotFileErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_QbSysIotFileErrorMsg_Type.__name__ = "DisplayString"
_QbSysIotFileErrorMsg_Object = MibTableColumn
qbSysIotFileErrorMsg = _QbSysIotFileErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 6, 10, 1, 11),
    _QbSysIotFileErrorMsg_Type()
)
qbSysIotFileErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbSysIotFileErrorMsg.setStatus("current")
_QbSysInterfacesGroup_ObjectIdentity = ObjectIdentity
qbSysInterfacesGroup = _QbSysInterfacesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7)
)
_QbSysIfLocationTable_Object = MibTable
qbSysIfLocationTable = _QbSysIfLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    qbSysIfLocationTable.setStatus("current")
_QbSysIfLocationEntry_Object = MibTableRow
qbSysIfLocationEntry = _QbSysIfLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7, 1, 1)
)
qbSysIfLocationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qbSysIfLocationEntry.setStatus("current")
_QbIfLocationSlot_Type = QbIoasSlot
_QbIfLocationSlot_Object = MibTableColumn
qbIfLocationSlot = _QbIfLocationSlot_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7, 1, 1, 1),
    _QbIfLocationSlot_Type()
)
qbIfLocationSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfLocationSlot.setStatus("current")
_QbIfLocationAddr_Type = Unsigned32
_QbIfLocationAddr_Object = MibTableColumn
qbIfLocationAddr = _QbIfLocationAddr_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7, 1, 1, 2),
    _QbIfLocationAddr_Type()
)
qbIfLocationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfLocationAddr.setStatus("current")
_QbIfLocationPort_Type = QbSysPortLoc
_QbIfLocationPort_Object = MibTableColumn
qbIfLocationPort = _QbIfLocationPort_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7, 1, 1, 3),
    _QbIfLocationPort_Type()
)
qbIfLocationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfLocationPort.setStatus("current")


class _QbIfLocationType_Type(Integer32):
    """Custom type qbIfLocationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ioas", 1),
          ("iot", 2))
    )


_QbIfLocationType_Type.__name__ = "Integer32"
_QbIfLocationType_Object = MibTableColumn
qbIfLocationType = _QbIfLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7, 1, 1, 4),
    _QbIfLocationType_Type()
)
qbIfLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfLocationType.setStatus("current")
_QbIfLocationSerialNumber_Type = Unsigned32
_QbIfLocationSerialNumber_Object = MibTableColumn
qbIfLocationSerialNumber = _QbIfLocationSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 1, 7, 1, 1, 5),
    _QbIfLocationSerialNumber_Type()
)
qbIfLocationSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbIfLocationSerialNumber.setStatus("current")
_QbSysNotifications_ObjectIdentity = ObjectIdentity
qbSysNotifications = _QbSysNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2)
)
_QbSysNotificationPrefix_ObjectIdentity = ObjectIdentity
qbSysNotificationPrefix = _QbSysNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0)
)
_QbSysConformance_ObjectIdentity = ObjectIdentity
qbSysConformance = _QbSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3)
)
_QbSysCompliances_ObjectIdentity = ObjectIdentity
qbSysCompliances = _QbSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 1)
)
_QbSysGroups_ObjectIdentity = ObjectIdentity
qbSysGroups = _QbSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2)
)

# Managed Objects groups

qbSysGeneralGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2, 1)
)
qbSysGeneralGroupInfo.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysOperStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysResetCtl"),
        ("QBSYS-SYSTEM-MIB", "qbSysBootDiagsCode"),
        ("QBSYS-SYSTEM-MIB", "qbSysWatchdogUpdate"),
        ("QBSYS-SYSTEM-MIB", "qbSysRunningImageVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysPowerSupplyType"),
        ("QBSYS-SYSTEM-MIB", "qbSysAcoCtl"),
        ("QBSYS-SYSTEM-MIB", "qbSysAutonomousStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysDiscreteInputType"),
        ("QBSYS-SYSTEM-MIB", "qbSysDiscreteInputName"),
        ("QBSYS-SYSTEM-MIB", "qbSysDiscreteInputAdminStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysDiscreteInputState"),
        ("QBSYS-SYSTEM-MIB", "qbSysSnmpRevision"),
        ("QBSYS-SYSTEM-MIB", "qbSysMgmtIpAddr"),
        ("QBSYS-SYSTEM-MIB", "qbSysMgmtIpMask"),
        ("QBSYS-SYSTEM-MIB", "qbSysAgentReadCommunity"),
        ("QBSYS-SYSTEM-MIB", "qbSysAgentReadWriteCommunity"),
        ("QBSYS-SYSTEM-MIB", "qbSysDefaultIpRouter"),
        ("QBSYS-SYSTEM-MIB", "qbSysAgentTrapDestFilter"),
        ("QBSYS-SYSTEM-MIB", "qbSysAgentTrapDestComm"),
        ("QBSYS-SYSTEM-MIB", "qbSysAgentTrapDestRowStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysDefaultRouterType"),
        ("QBSYS-SYSTEM-MIB", "qbSysCliMsgCode"),
        ("QBSYS-SYSTEM-MIB", "qbSysResetVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysFeatureKeys"))
)
if mibBuilder.loadTexts:
    qbSysGeneralGroupInfo.setStatus("current")

qbSysConfigParamsGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2, 2)
)
qbSysConfigParamsGroupInfo.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysConfigLastWriteDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysConfigLastWriteSource"),
        ("QBSYS-SYSTEM-MIB", "qbSysProvType"))
)
if mibBuilder.loadTexts:
    qbSysConfigParamsGroupInfo.setStatus("current")

qbSysEventGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2, 3)
)
qbSysEventGroupInfo.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysEventHistoryDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistorySubsystem"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistorySrvAffect"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistorySeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryId"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryMsg"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryMaxTableSize"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmSubsystem"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmSrvAffect"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmSeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmCondition"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmId"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmMsg"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmResource"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistoryDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistorySubsystem"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistorySrvAffect"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistorySeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistoryCondition"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryId"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryMsg"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistoryMaxTableSize"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistoryClearAllCtl"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventIdName"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventIdSeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventIdSASeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventAsTrap"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmIdName"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmIdSeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmIdSASeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmAsTrap"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationOID"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryType"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryTypeId"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryAction"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryResource"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryCookie"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryAlarmCondition"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryMaxTableSize"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmHistoryLastIndex"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryLastIndex"),
        ("QBSYS-SYSTEM-MIB", "qbSysGlobalHistoryLastIndex"))
)
if mibBuilder.loadTexts:
    qbSysEventGroupInfo.setStatus("current")

qbSysModuleGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2, 4)
)
qbSysModuleGroupInfo.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleType"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleName"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleOperStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleAdminStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleTestResult"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleNumPorts"),
        ("QBSYS-SYSTEM-MIB", "qbSysModulePortStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleModel"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleSerialNum"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleEqId"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleHwVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleSwVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleProtectionMode"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleLastSwitchoverTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleSwitchoverReason"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleLedStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleProductName"))
)
if mibBuilder.loadTexts:
    qbSysModuleGroupInfo.setStatus("current")

qbSysPortGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2, 5)
)
qbSysPortGroupInfo.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysPort"),
        ("QBSYS-SYSTEM-MIB", "qbSysPortName"),
        ("QBSYS-SYSTEM-MIB", "qbSysPortType"),
        ("QBSYS-SYSTEM-MIB", "qbSysPortOperStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysPortIfIndex"),
        ("QBSYS-SYSTEM-MIB", "qbSysPortLoopbackConfig"))
)
if mibBuilder.loadTexts:
    qbSysPortGroupInfo.setStatus("current")

qbSysIotGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2, 6)
)
qbSysIotGroupInfo.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysIoasDwsIfIndex"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotAddr"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotName"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotLocation"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotSwVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotHwVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotOperStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotAdminStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotDsx1LineCoding"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotSerialStr"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotRowStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileAvailableVersion1"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileAvailableVersion2"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileRunningVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileAcceptedVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileDownLoadVersion"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileLastModification"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileAction"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileDownLoadStatus"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotFileErrorMsg"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotProductName"))
)
if mibBuilder.loadTexts:
    qbSysIotGroupInfo.setStatus("current")

qbSysInterfaceGroupInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 2, 7)
)
qbSysInterfaceGroupInfo.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbIfLocationSlot"),
        ("QBSYS-SYSTEM-MIB", "qbIfLocationAddr"),
        ("QBSYS-SYSTEM-MIB", "qbIfLocationPort"),
        ("QBSYS-SYSTEM-MIB", "qbIfLocationType"),
        ("QBSYS-SYSTEM-MIB", "qbIfLocationSerialNumber"))
)
if mibBuilder.loadTexts:
    qbSysInterfaceGroupInfo.setStatus("current")


# Notification objects

qbSysAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 1)
)
qbSysAlarm.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysAlarmDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmSubsystem"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmSrvAffect"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmSeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmCondition"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmId"),
        ("QBSYS-SYSTEM-MIB", "qbSysAlarmMsg"))
)
if mibBuilder.loadTexts:
    qbSysAlarm.setStatus(
        "current"
    )

qbSysEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 2)
)
qbSysEvent.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysEventHistoryDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistorySubsystem"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistorySrvAffect"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistorySeverity"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryId"),
        ("QBSYS-SYSTEM-MIB", "qbSysEventHistoryMsg"))
)
if mibBuilder.loadTexts:
    qbSysEvent.setStatus(
        "current"
    )

qbSysModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 3)
)
qbSysModuleDown.setObjects(
    ("QBSYS-SYSTEM-MIB", "qbSysModuleSlot")
)
if mibBuilder.loadTexts:
    qbSysModuleDown.setStatus(
        "current"
    )

qbSysModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 4)
)
qbSysModuleInserted.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleType"))
)
if mibBuilder.loadTexts:
    qbSysModuleInserted.setStatus(
        "current"
    )

qbSysModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 5)
)
qbSysModuleRemoved.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleType"))
)
if mibBuilder.loadTexts:
    qbSysModuleRemoved.setStatus(
        "current"
    )

qbSysIotDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 6)
)
qbSysIotDiscovered.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotAddr"))
)
if mibBuilder.loadTexts:
    qbSysIotDiscovered.setStatus(
        "current"
    )

qbSysIotRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 7)
)
qbSysIotRemoved.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotAddr"))
)
if mibBuilder.loadTexts:
    qbSysIotRemoved.setStatus(
        "current"
    )

qbSysIotLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 8)
)
qbSysIotLos.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
        ("QBSYS-SYSTEM-MIB", "qbSysIotAddr"))
)
if mibBuilder.loadTexts:
    qbSysIotLos.setStatus(
        "current"
    )

qbSysModuleSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 9)
)
qbSysModuleSwitchover.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysModuleSlot"),
        ("QBSYS-SYSTEM-MIB", "qbSysModuleProtectionMode"))
)
if mibBuilder.loadTexts:
    qbSysModuleSwitchover.setStatus(
        "current"
    )

qbSysFlashInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 10)
)
qbSysFlashInserted.setObjects(
    ("QBSYS-SYSTEM-MIB", "qbSysModuleSlot")
)
if mibBuilder.loadTexts:
    qbSysFlashInserted.setStatus(
        "current"
    )

qbSysFlashRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 11)
)
qbSysFlashRemoved.setObjects(
    ("QBSYS-SYSTEM-MIB", "qbSysModuleSlot")
)
if mibBuilder.loadTexts:
    qbSysFlashRemoved.setStatus(
        "current"
    )

qbSysProvChanges = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 12)
)
qbSysProvChanges.setObjects(
    ("QBSYS-SYSTEM-MIB", "qbSysProvType")
)
if mibBuilder.loadTexts:
    qbSysProvChanges.setStatus(
        "current"
    )

qbWanRxLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 13)
)
qbWanRxLos.setObjects(
    ("QBSYS-SYSTEM-MIB", "qbSysModuleSlot")
)
if mibBuilder.loadTexts:
    qbWanRxLos.setStatus(
        "current"
    )

qbSysUnsolicitedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 14)
)
qbSysUnsolicitedEvent.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryType"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryTypeId"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryAction"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryResource"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryCookie"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryAlarmCondition"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryServiceAffecting"))
)
if mibBuilder.loadTexts:
    qbSysUnsolicitedEvent.setStatus(
        "current"
    )

qbSysConfigurationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 2, 0, 15)
)
qbSysConfigurationEvent.setObjects(
      *(("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryType"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryTypeId"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryAction"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryResource"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryCookie"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryDateTime"),
        ("QBSYS-SYSTEM-MIB", "qbSysNotificationHistoryAlarmCondition"))
)
if mibBuilder.loadTexts:
    qbSysConfigurationEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qbSysCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbSysCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QBSYS-SYSTEM-MIB",
    **{"DateAndTimeForm": DateAndTimeForm,
       "QbStorageType": QbStorageType,
       "QbFileType": QbFileType,
       "QbFileImageType": QbFileImageType,
       "QbTransferStatus": QbTransferStatus,
       "QbSysApplId": QbSysApplId,
       "ProtectionMode": ProtectionMode,
       "QbApsGroupMode": QbApsGroupMode,
       "QbApsSwitchMode": QbApsSwitchMode,
       "TimeStamp": TimeStamp,
       "QbEventSrvAffect": QbEventSrvAffect,
       "QbEventSeverity": QbEventSeverity,
       "QbAlarmCondition": QbAlarmCondition,
       "QbIoasSlot": QbIoasSlot,
       "QbSysPortLoc": QbSysPortLoc,
       "QbSysLedState": QbSysLedState,
       "QbNotificationAlarmCondition": QbNotificationAlarmCondition,
       "QbNotificationType": QbNotificationType,
       "QbNotificationAction": QbNotificationAction,
       "QbIotType": QbIotType,
       "qbSysMIB": qbSysMIB,
       "qbSysObjects": qbSysObjects,
       "qbSysGeneralGroup": qbSysGeneralGroup,
       "qbSysDateTime": qbSysDateTime,
       "qbSysOperStatus": qbSysOperStatus,
       "qbSysResetCtl": qbSysResetCtl,
       "qbSysBootDiagsCode": qbSysBootDiagsCode,
       "qbSysWatchdogUpdate": qbSysWatchdogUpdate,
       "qbSysRunningImageVersion": qbSysRunningImageVersion,
       "qbSysPowerSupplyType": qbSysPowerSupplyType,
       "qbSysAcoCtl": qbSysAcoCtl,
       "qbSysAutonomousStatus": qbSysAutonomousStatus,
       "qbSysDiscreteInputTable": qbSysDiscreteInputTable,
       "qbSysDiscreteInputEntry": qbSysDiscreteInputEntry,
       "qbSysDiscreteInputType": qbSysDiscreteInputType,
       "qbSysDiscreteInputName": qbSysDiscreteInputName,
       "qbSysDiscreteInputAdminStatus": qbSysDiscreteInputAdminStatus,
       "qbSysDiscreteInputState": qbSysDiscreteInputState,
       "qbSysAgentGroup": qbSysAgentGroup,
       "qbSysSnmpRevision": qbSysSnmpRevision,
       "qbSysMgmtIpAddr": qbSysMgmtIpAddr,
       "qbSysMgmtIpMask": qbSysMgmtIpMask,
       "qbSysDefaultIpRouter": qbSysDefaultIpRouter,
       "qbSysAgentReadCommunity": qbSysAgentReadCommunity,
       "qbSysAgentReadWriteCommunity": qbSysAgentReadWriteCommunity,
       "qbSysAgentTrapDestTable": qbSysAgentTrapDestTable,
       "qbSysAgentTrapDestEntry": qbSysAgentTrapDestEntry,
       "qbSysAgentTrapDestAddr": qbSysAgentTrapDestAddr,
       "qbSysAgentTrapDestFilter": qbSysAgentTrapDestFilter,
       "qbSysAgentTrapDestComm": qbSysAgentTrapDestComm,
       "qbSysAgentTrapDestRowStatus": qbSysAgentTrapDestRowStatus,
       "qbSysAgentTrapDestPort": qbSysAgentTrapDestPort,
       "qbSysDefaultRouterType": qbSysDefaultRouterType,
       "qbSysCliMsgCode": qbSysCliMsgCode,
       "qbRIPConfig": qbRIPConfig,
       "qbSysFileGroup": qbSysFileGroup,
       "qbSysBootImageTable": qbSysBootImageTable,
       "qbSysBootImageEntry": qbSysBootImageEntry,
       "qbSysBootImageIndex": qbSysBootImageIndex,
       "qbSysBootImageName": qbSysBootImageName,
       "qbSysBootImageAddress": qbSysBootImageAddress,
       "qbSysTransferTable": qbSysTransferTable,
       "qbSysTransferEntry": qbSysTransferEntry,
       "qbSysTransferIndex": qbSysTransferIndex,
       "qbSysTransferSrc": qbSysTransferSrc,
       "qbSysTransferSrcName": qbSysTransferSrcName,
       "qbSysTransferDest": qbSysTransferDest,
       "qbSysTransferDestName": qbSysTransferDestName,
       "qbSysTransferServerAddr": qbSysTransferServerAddr,
       "qbSysTransferIot": qbSysTransferIot,
       "qbSysTransferOperStatus": qbSysTransferOperStatus,
       "qbSysTransferOperProgress": qbSysTransferOperProgress,
       "qbSysTransferRowStatus": qbSysTransferRowStatus,
       "qbSysResetVersion": qbSysResetVersion,
       "qbSysFeatureKeys": qbSysFeatureKeys,
       "qbSysPortBwSharing": qbSysPortBwSharing,
       "qbSysTestLeds": qbSysTestLeds,
       "qbSysSwAccepted": qbSysSwAccepted,
       "qbChassisSysType": qbChassisSysType,
       "qbChassisBkplType": qbChassisBkplType,
       "qbChassisNumSlots": qbChassisNumSlots,
       "qbChassisBulkStatsCtl": qbChassisBulkStatsCtl,
       "qbSysConfigParamsGroup": qbSysConfigParamsGroup,
       "qbSysConfigLastWriteDateTime": qbSysConfigLastWriteDateTime,
       "qbSysConfigLastWriteSource": qbSysConfigLastWriteSource,
       "qbSysProvType": qbSysProvType,
       "qbSysEventsGroup": qbSysEventsGroup,
       "qbSysEventHistoryTable": qbSysEventHistoryTable,
       "qbSysEventHistoryEntry": qbSysEventHistoryEntry,
       "qbSysEventHistoryIndex": qbSysEventHistoryIndex,
       "qbSysEventHistoryDateTime": qbSysEventHistoryDateTime,
       "qbSysEventHistorySubsystem": qbSysEventHistorySubsystem,
       "qbSysEventHistorySrvAffect": qbSysEventHistorySrvAffect,
       "qbSysEventHistorySeverity": qbSysEventHistorySeverity,
       "qbSysEventHistoryId": qbSysEventHistoryId,
       "qbSysEventHistoryMsg": qbSysEventHistoryMsg,
       "qbSysEventHistoryMaxTableSize": qbSysEventHistoryMaxTableSize,
       "qbSysEventHistoryOutFilterLevel": qbSysEventHistoryOutFilterLevel,
       "qbSysEventHistoryOutFilterDateTime": qbSysEventHistoryOutFilterDateTime,
       "qbSysEventHistoryClearAllCtl": qbSysEventHistoryClearAllCtl,
       "qbSysAlarmTable": qbSysAlarmTable,
       "qbSysAlarmEntry": qbSysAlarmEntry,
       "qbSysAlarmIndex": qbSysAlarmIndex,
       "qbSysAlarmDateTime": qbSysAlarmDateTime,
       "qbSysAlarmSubsystem": qbSysAlarmSubsystem,
       "qbSysAlarmSrvAffect": qbSysAlarmSrvAffect,
       "qbSysAlarmSeverity": qbSysAlarmSeverity,
       "qbSysAlarmCondition": qbSysAlarmCondition,
       "qbSysAlarmId": qbSysAlarmId,
       "qbSysAlarmMsg": qbSysAlarmMsg,
       "qbSysAlarmResource": qbSysAlarmResource,
       "qbSysAlarmHistoryTable": qbSysAlarmHistoryTable,
       "qbSysAlarmHistoryEntry": qbSysAlarmHistoryEntry,
       "qbSysAlarmHistoryIndex": qbSysAlarmHistoryIndex,
       "qbSysAlarmHistoryDateTime": qbSysAlarmHistoryDateTime,
       "qbSysAlarmHistorySubsystem": qbSysAlarmHistorySubsystem,
       "qbSysAlarmHistorySrvAffect": qbSysAlarmHistorySrvAffect,
       "qbSysAlarmHistorySeverity": qbSysAlarmHistorySeverity,
       "qbSysAlarmHistoryCondition": qbSysAlarmHistoryCondition,
       "qbSysAlarmHistoryId": qbSysAlarmHistoryId,
       "qbSysAlarmHistoryMsg": qbSysAlarmHistoryMsg,
       "qbSysAlarmHistoryMaxTableSize": qbSysAlarmHistoryMaxTableSize,
       "qbSysAlarmHistoryOutFilterLevel": qbSysAlarmHistoryOutFilterLevel,
       "qbSysAlarmHistoryOutFilterDateTime": qbSysAlarmHistoryOutFilterDateTime,
       "qbSysAlarmHistoryClearAllCtl": qbSysAlarmHistoryClearAllCtl,
       "qbSysEventIdTable": qbSysEventIdTable,
       "qbSysEventIdEntry": qbSysEventIdEntry,
       "qbSysEventDescrId": qbSysEventDescrId,
       "qbSysEventIdName": qbSysEventIdName,
       "qbSysEventIdSeverity": qbSysEventIdSeverity,
       "qbSysEventIdSASeverity": qbSysEventIdSASeverity,
       "qbSysEventAsTrap": qbSysEventAsTrap,
       "qbSysAlarmIdTable": qbSysAlarmIdTable,
       "qbSysAlarmIdEntry": qbSysAlarmIdEntry,
       "qbSysAlarmDescrId": qbSysAlarmDescrId,
       "qbSysAlarmIdName": qbSysAlarmIdName,
       "qbSysAlarmIdSeverity": qbSysAlarmIdSeverity,
       "qbSysAlarmIdSASeverity": qbSysAlarmIdSASeverity,
       "qbSysAlarmAsTrap": qbSysAlarmAsTrap,
       "qbSysNotificationHistoryTable": qbSysNotificationHistoryTable,
       "qbSysNotificationHistoryEntry": qbSysNotificationHistoryEntry,
       "qbSysNotificationHistoryIndex": qbSysNotificationHistoryIndex,
       "qbSysNotificationOID": qbSysNotificationOID,
       "qbSysNotificationHistoryType": qbSysNotificationHistoryType,
       "qbSysNotificationHistoryTypeId": qbSysNotificationHistoryTypeId,
       "qbSysNotificationHistoryAction": qbSysNotificationHistoryAction,
       "qbSysNotificationHistoryResource": qbSysNotificationHistoryResource,
       "qbSysNotificationHistoryCookie": qbSysNotificationHistoryCookie,
       "qbSysNotificationHistoryDateTime": qbSysNotificationHistoryDateTime,
       "qbSysNotificationHistoryAlarmCondition": qbSysNotificationHistoryAlarmCondition,
       "qbSysNotificationHistoryServiceAffecting": qbSysNotificationHistoryServiceAffecting,
       "qbSysNotificationHistoryMaxTableSize": qbSysNotificationHistoryMaxTableSize,
       "qbSysNotificationHistoryOutFilterLevel": qbSysNotificationHistoryOutFilterLevel,
       "qbSysNotificationHistoryOutFilterDateTime": qbSysNotificationHistoryOutFilterDateTime,
       "qbSysNotificationHistoryClearAllCtl": qbSysNotificationHistoryClearAllCtl,
       "qbSysAlarmHistoryLastIndex": qbSysAlarmHistoryLastIndex,
       "qbSysEventHistoryLastIndex": qbSysEventHistoryLastIndex,
       "qbSysGlobalHistoryLastIndex": qbSysGlobalHistoryLastIndex,
       "qbSysModuleGroup": qbSysModuleGroup,
       "qbSysModuleTable": qbSysModuleTable,
       "qbSysModuleEntry": qbSysModuleEntry,
       "qbSysModuleSlot": qbSysModuleSlot,
       "qbSysModuleType": qbSysModuleType,
       "qbSysModuleName": qbSysModuleName,
       "qbSysModuleOperStatus": qbSysModuleOperStatus,
       "qbSysModuleAdminStatus": qbSysModuleAdminStatus,
       "qbSysModuleTestResult": qbSysModuleTestResult,
       "qbSysModuleNumPorts": qbSysModuleNumPorts,
       "qbSysModulePortStatus": qbSysModulePortStatus,
       "qbSysModuleModel": qbSysModuleModel,
       "qbSysModuleSerialNum": qbSysModuleSerialNum,
       "qbSysModuleEqId": qbSysModuleEqId,
       "qbSysModuleHwVersion": qbSysModuleHwVersion,
       "qbSysModuleSwVersion": qbSysModuleSwVersion,
       "qbSysModuleProtectionMode": qbSysModuleProtectionMode,
       "qbSysModuleLastSwitchoverTime": qbSysModuleLastSwitchoverTime,
       "qbSysModuleSwitchoverReason": qbSysModuleSwitchoverReason,
       "qbSysModuleLedStatus": qbSysModuleLedStatus,
       "qbSysModuleProductName": qbSysModuleProductName,
       "qbSysModuleTestLeds": qbSysModuleTestLeds,
       "qbSysApsAlarmStatus": qbSysApsAlarmStatus,
       "qbSysModuleApsTable": qbSysModuleApsTable,
       "qbSysModuleApsEntry": qbSysModuleApsEntry,
       "qbSysModuleApsGroupAdminMode": qbSysModuleApsGroupAdminMode,
       "qbSysModuleApsGroupOperMode": qbSysModuleApsGroupOperMode,
       "qbSysModuleApsSwitchAdminMode": qbSysModuleApsSwitchAdminMode,
       "qbSysModuleApsSwitchOperMode": qbSysModuleApsSwitchOperMode,
       "qbSysModuleApsLastSwitchoverTime": qbSysModuleApsLastSwitchoverTime,
       "qbSysPortGroup": qbSysPortGroup,
       "qbSysPortTable": qbSysPortTable,
       "qbSysPortEntry": qbSysPortEntry,
       "qbSysPort": qbSysPort,
       "qbSysPortName": qbSysPortName,
       "qbSysPortType": qbSysPortType,
       "qbSysPortOperStatus": qbSysPortOperStatus,
       "qbSysPortIfIndex": qbSysPortIfIndex,
       "qbSysPortLoopbackConfig": qbSysPortLoopbackConfig,
       "qbSysIotGroup": qbSysIotGroup,
       "qbSysIotTable": qbSysIotTable,
       "qbSysIotEntry": qbSysIotEntry,
       "qbSysIotSerialNumber": qbSysIotSerialNumber,
       "qbSysIoasDwsIfIndex": qbSysIoasDwsIfIndex,
       "qbSysIotAddr": qbSysIotAddr,
       "qbSysIotDescr": qbSysIotDescr,
       "qbSysIotName": qbSysIotName,
       "qbSysIotLocation": qbSysIotLocation,
       "qbSysIotSwVersion": qbSysIotSwVersion,
       "qbSysIotHwVersion": qbSysIotHwVersion,
       "qbSysIotAdminStatus": qbSysIotAdminStatus,
       "qbSysIotOperStatus": qbSysIotOperStatus,
       "qbSysIotDsx1LineCoding": qbSysIotDsx1LineCoding,
       "qbSysIotSerialStr": qbSysIotSerialStr,
       "qbSysIotRowStatus": qbSysIotRowStatus,
       "qbSysIotManufSerialNum": qbSysIotManufSerialNum,
       "qbSysIotType": qbSysIotType,
       "qbSysIotProductName": qbSysIotProductName,
       "qbSysIotSignalFmt": qbSysIotSignalFmt,
       "qbSysIotRollSerialNumber": qbSysIotRollSerialNumber,
       "qbSysIotNumSlots": qbSysIotNumSlots,
       "qbSysIotFileTable": qbSysIotFileTable,
       "qbSysIotFileEntry": qbSysIotFileEntry,
       "qbSysIotFileSerialNumber": qbSysIotFileSerialNumber,
       "qbSysIotFileAvailableVersion1": qbSysIotFileAvailableVersion1,
       "qbSysIotFileAvailableVersion2": qbSysIotFileAvailableVersion2,
       "qbSysIotFileRunningVersion": qbSysIotFileRunningVersion,
       "qbSysIotFileAcceptedVersion": qbSysIotFileAcceptedVersion,
       "qbSysIotFileDownLoadVersion": qbSysIotFileDownLoadVersion,
       "qbSysIotFileSysUpTime": qbSysIotFileSysUpTime,
       "qbSysIotFileLastModification": qbSysIotFileLastModification,
       "qbSysIotFileAction": qbSysIotFileAction,
       "qbSysIotFileDownLoadStatus": qbSysIotFileDownLoadStatus,
       "qbSysIotFileErrorMsg": qbSysIotFileErrorMsg,
       "qbSysInterfacesGroup": qbSysInterfacesGroup,
       "qbSysIfLocationTable": qbSysIfLocationTable,
       "qbSysIfLocationEntry": qbSysIfLocationEntry,
       "qbIfLocationSlot": qbIfLocationSlot,
       "qbIfLocationAddr": qbIfLocationAddr,
       "qbIfLocationPort": qbIfLocationPort,
       "qbIfLocationType": qbIfLocationType,
       "qbIfLocationSerialNumber": qbIfLocationSerialNumber,
       "qbSysNotifications": qbSysNotifications,
       "qbSysNotificationPrefix": qbSysNotificationPrefix,
       "qbSysAlarm": qbSysAlarm,
       "qbSysEvent": qbSysEvent,
       "qbSysModuleDown": qbSysModuleDown,
       "qbSysModuleInserted": qbSysModuleInserted,
       "qbSysModuleRemoved": qbSysModuleRemoved,
       "qbSysIotDiscovered": qbSysIotDiscovered,
       "qbSysIotRemoved": qbSysIotRemoved,
       "qbSysIotLos": qbSysIotLos,
       "qbSysModuleSwitchover": qbSysModuleSwitchover,
       "qbSysFlashInserted": qbSysFlashInserted,
       "qbSysFlashRemoved": qbSysFlashRemoved,
       "qbSysProvChanges": qbSysProvChanges,
       "qbWanRxLos": qbWanRxLos,
       "qbSysUnsolicitedEvent": qbSysUnsolicitedEvent,
       "qbSysConfigurationEvent": qbSysConfigurationEvent,
       "qbSysConformance": qbSysConformance,
       "qbSysCompliances": qbSysCompliances,
       "qbSysCompliance": qbSysCompliance,
       "qbSysGroups": qbSysGroups,
       "qbSysGeneralGroupInfo": qbSysGeneralGroupInfo,
       "qbSysConfigParamsGroupInfo": qbSysConfigParamsGroupInfo,
       "qbSysEventGroupInfo": qbSysEventGroupInfo,
       "qbSysModuleGroupInfo": qbSysModuleGroupInfo,
       "qbSysPortGroupInfo": qbSysPortGroupInfo,
       "qbSysIotGroupInfo": qbSysIotGroupInfo,
       "qbSysInterfaceGroupInfo": qbSysInterfaceGroupInfo}
)
