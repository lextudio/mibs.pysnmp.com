# SNMP MIB module (FORTINET-FORTIMAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-FORTIMAIL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:34 2024
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

(FnBoolState,
 FnIndex,
 FnSessionProto,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "FnSessionProto",
    "fortinet")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

fnFortiMailMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105)
)
fnFortiMailMib.setRevisions(
        ("2010-03-23 00:00",
         "2009-10-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FmlOpMode(Integer32, TextualConvention):
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
        *(("gateway", 1),
          ("server", 3),
          ("transparent", 2))
    )



class FmlSysEventCodeVal(Integer32, TextualConvention):
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
        *(("avDBUpdate", 8),
          ("guiUpgrade", 5),
          ("logdiskFormat", 6),
          ("maildiskFormat", 7),
          ("systemHalt", 1),
          ("systemReboot", 2),
          ("systemReload", 3),
          ("systemUpgrade", 4))
    )



class FmlRAIDCodeVal(Integer32, TextualConvention):
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
        *(("degradedArray", 1),
          ("fail", 5),
          ("failSpare", 6),
          ("rebuildFinished", 4),
          ("rebuildStarted", 3),
          ("spareActive", 7),
          ("sparesMissing", 2))
    )



class FmlHAEventIdVal(Integer32, TextualConvention):
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
        *(("masterUnitSwitch", 1),
          ("slaveUnitSwitch", 2),
          ("unitShutdown", 3))
    )



class FmlHAModeVal(Integer32, TextualConvention):
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
        *(("configMaster", 3),
          ("configSlave", 4),
          ("master", 1),
          ("off", 0),
          ("slave", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FmlTraps_ObjectIdentity = ObjectIdentity
fmlTraps = _FmlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0)
)
_FmlSystem_ObjectIdentity = ObjectIdentity
fmlSystem = _FmlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1)
)


class _FmlSysModel_Type(DisplayString):
    """Custom type fmlSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FmlSysModel_Type.__name__ = "DisplayString"
_FmlSysModel_Object = MibScalar
fmlSysModel = _FmlSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 1),
    _FmlSysModel_Type()
)
fmlSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysModel.setStatus("current")


class _FmlSysSerial_Type(DisplayString):
    """Custom type fmlSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmlSysSerial_Type.__name__ = "DisplayString"
_FmlSysSerial_Object = MibScalar
fmlSysSerial = _FmlSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 2),
    _FmlSysSerial_Type()
)
fmlSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysSerial.setStatus("current")


class _FmlSysVersion_Type(DisplayString):
    """Custom type fmlSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FmlSysVersion_Type.__name__ = "DisplayString"
_FmlSysVersion_Object = MibScalar
fmlSysVersion = _FmlSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 3),
    _FmlSysVersion_Type()
)
fmlSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysVersion.setStatus("current")


class _FmlSysVersionAv_Type(DisplayString):
    """Custom type fmlSysVersionAv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FmlSysVersionAv_Type.__name__ = "DisplayString"
_FmlSysVersionAv_Object = MibScalar
fmlSysVersionAv = _FmlSysVersionAv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 4),
    _FmlSysVersionAv_Type()
)
fmlSysVersionAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysVersionAv.setStatus("current")
_FmlSysOpMode_Type = FmlOpMode
_FmlSysOpMode_Object = MibScalar
fmlSysOpMode = _FmlSysOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 5),
    _FmlSysOpMode_Type()
)
fmlSysOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOpMode.setStatus("current")
_FmlSysCpuUsage_Type = Gauge32
_FmlSysCpuUsage_Object = MibScalar
fmlSysCpuUsage = _FmlSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 6),
    _FmlSysCpuUsage_Type()
)
fmlSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysCpuUsage.setStatus("current")
_FmlSysMemUsage_Type = Gauge32
_FmlSysMemUsage_Object = MibScalar
fmlSysMemUsage = _FmlSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 7),
    _FmlSysMemUsage_Type()
)
fmlSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysMemUsage.setStatus("current")
_FmlSysLogDiskUsage_Type = Gauge32
_FmlSysLogDiskUsage_Object = MibScalar
fmlSysLogDiskUsage = _FmlSysLogDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 8),
    _FmlSysLogDiskUsage_Type()
)
fmlSysLogDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysLogDiskUsage.setStatus("current")
_FmlSysMailDiskUsage_Type = Gauge32
_FmlSysMailDiskUsage_Object = MibScalar
fmlSysMailDiskUsage = _FmlSysMailDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 9),
    _FmlSysMailDiskUsage_Type()
)
fmlSysMailDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysMailDiskUsage.setStatus("current")
_FmlSysSesCount_Type = Gauge32
_FmlSysSesCount_Object = MibScalar
fmlSysSesCount = _FmlSysSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 10),
    _FmlSysSesCount_Type()
)
fmlSysSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysSesCount.setStatus("current")
_FmlSysEventCode_Type = FmlSysEventCodeVal
_FmlSysEventCode_Object = MibScalar
fmlSysEventCode = _FmlSysEventCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 11),
    _FmlSysEventCode_Type()
)
fmlSysEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmlSysEventCode.setStatus("current")
_FmlRAIDCode_Type = FmlRAIDCodeVal
_FmlRAIDCode_Object = MibScalar
fmlRAIDCode = _FmlRAIDCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 12),
    _FmlRAIDCode_Type()
)
fmlRAIDCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmlRAIDCode.setStatus("current")


class _FmlRAIDDevName_Type(DisplayString):
    """Custom type fmlRAIDDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmlRAIDDevName_Type.__name__ = "DisplayString"
_FmlRAIDDevName_Object = MibScalar
fmlRAIDDevName = _FmlRAIDDevName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 13),
    _FmlRAIDDevName_Type()
)
fmlRAIDDevName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmlRAIDDevName.setStatus("current")
_FmlHAEventId_Type = FmlHAEventIdVal
_FmlHAEventId_Object = MibScalar
fmlHAEventId = _FmlHAEventId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 14),
    _FmlHAEventId_Type()
)
fmlHAEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmlHAEventId.setStatus("current")
_FmlHAUnitIp_Type = IpAddress
_FmlHAUnitIp_Object = MibScalar
fmlHAUnitIp = _FmlHAUnitIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 15),
    _FmlHAUnitIp_Type()
)
fmlHAUnitIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmlHAUnitIp.setStatus("current")


class _FmlHAEventReason_Type(DisplayString):
    """Custom type fmlHAEventReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmlHAEventReason_Type.__name__ = "DisplayString"
_FmlHAEventReason_Object = MibScalar
fmlHAEventReason = _FmlHAEventReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 16),
    _FmlHAEventReason_Type()
)
fmlHAEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmlHAEventReason.setStatus("current")
_FmlSysLoad_Type = Gauge32
_FmlSysLoad_Object = MibScalar
fmlSysLoad = _FmlSysLoad_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 30),
    _FmlSysLoad_Type()
)
fmlSysLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysLoad.setStatus("current")
_FmlSysOptions_ObjectIdentity = ObjectIdentity
fmlSysOptions = _FmlSysOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 101)
)
_FmlSysOptIdleTimeout_Type = Integer32
_FmlSysOptIdleTimeout_Object = MibScalar
fmlSysOptIdleTimeout = _FmlSysOptIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 101, 1),
    _FmlSysOptIdleTimeout_Type()
)
fmlSysOptIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOptIdleTimeout.setStatus("current")
_FmlSysOptAuthTimeout_Type = Integer32
_FmlSysOptAuthTimeout_Object = MibScalar
fmlSysOptAuthTimeout = _FmlSysOptAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 101, 2),
    _FmlSysOptAuthTimeout_Type()
)
fmlSysOptAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOptAuthTimeout.setStatus("current")
_FmlSysOptsLcdProt_Type = FnBoolState
_FmlSysOptsLcdProt_Object = MibScalar
fmlSysOptsLcdProt = _FmlSysOptsLcdProt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 101, 4),
    _FmlSysOptsLcdProt_Type()
)
fmlSysOptsLcdProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOptsLcdProt.setStatus("current")
_FmlIp_ObjectIdentity = ObjectIdentity
fmlIp = _FmlIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102)
)
_FmlIpSessTable_Object = MibTable
fmlIpSessTable = _FmlIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2)
)
if mibBuilder.loadTexts:
    fmlIpSessTable.setStatus("current")
_FmlIpSessEntry_Object = MibTableRow
fmlIpSessEntry = _FmlIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1)
)
fmlIpSessEntry.setIndexNames(
    (0, "FORTINET-FORTIMAIL-MIB", "fmlIpSessIndex"),
)
if mibBuilder.loadTexts:
    fmlIpSessEntry.setStatus("current")
_FmlIpSessIndex_Type = FnIndex
_FmlIpSessIndex_Object = MibTableColumn
fmlIpSessIndex = _FmlIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1, 1),
    _FmlIpSessIndex_Type()
)
fmlIpSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmlIpSessIndex.setStatus("current")
_FmlIpSessProto_Type = FnSessionProto
_FmlIpSessProto_Object = MibTableColumn
fmlIpSessProto = _FmlIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1, 2),
    _FmlIpSessProto_Type()
)
fmlIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessProto.setStatus("current")
_FmlIpSessFromAddr_Type = IpAddress
_FmlIpSessFromAddr_Object = MibTableColumn
fmlIpSessFromAddr = _FmlIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1, 3),
    _FmlIpSessFromAddr_Type()
)
fmlIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessFromAddr.setStatus("current")


class _FmlIpSessFromPort_Type(Integer32):
    """Custom type fmlIpSessFromPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FmlIpSessFromPort_Type.__name__ = "Integer32"
_FmlIpSessFromPort_Object = MibTableColumn
fmlIpSessFromPort = _FmlIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1, 4),
    _FmlIpSessFromPort_Type()
)
fmlIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessFromPort.setStatus("current")
_FmlIpSessToAddr_Type = IpAddress
_FmlIpSessToAddr_Object = MibTableColumn
fmlIpSessToAddr = _FmlIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1, 5),
    _FmlIpSessToAddr_Type()
)
fmlIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessToAddr.setStatus("current")


class _FmlIpSessToPort_Type(Integer32):
    """Custom type fmlIpSessToPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FmlIpSessToPort_Type.__name__ = "Integer32"
_FmlIpSessToPort_Object = MibTableColumn
fmlIpSessToPort = _FmlIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1, 6),
    _FmlIpSessToPort_Type()
)
fmlIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessToPort.setStatus("current")
_FmlIpSessExp_Type = Gauge32
_FmlIpSessExp_Object = MibTableColumn
fmlIpSessExp = _FmlIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 102, 2, 1, 7),
    _FmlIpSessExp_Type()
)
fmlIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessExp.setStatus("current")
_FmlMailOptions_ObjectIdentity = ObjectIdentity
fmlMailOptions = _FmlMailOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 103)
)
_FmlMailOptionsDeferQueue_Type = Gauge32
_FmlMailOptionsDeferQueue_Object = MibScalar
fmlMailOptionsDeferQueue = _FmlMailOptionsDeferQueue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 103, 1),
    _FmlMailOptionsDeferQueue_Type()
)
fmlMailOptionsDeferQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlMailOptionsDeferQueue.setStatus("current")
_FmlHwSensors_ObjectIdentity = ObjectIdentity
fmlHwSensors = _FmlHwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110)
)
_FmlHwSensorCount_Type = Integer32
_FmlHwSensorCount_Object = MibScalar
fmlHwSensorCount = _FmlHwSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110, 1),
    _FmlHwSensorCount_Type()
)
fmlHwSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHwSensorCount.setStatus("current")
_FmlHwSensorTable_Object = MibTable
fmlHwSensorTable = _FmlHwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110, 2)
)
if mibBuilder.loadTexts:
    fmlHwSensorTable.setStatus("current")
_FmlHwSensorEntry_Object = MibTableRow
fmlHwSensorEntry = _FmlHwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110, 2, 1)
)
fmlHwSensorEntry.setIndexNames(
    (0, "FORTINET-FORTIMAIL-MIB", "fmlHwSensorEntIndex"),
)
if mibBuilder.loadTexts:
    fmlHwSensorEntry.setStatus("current")
_FmlHwSensorEntIndex_Type = FnIndex
_FmlHwSensorEntIndex_Object = MibTableColumn
fmlHwSensorEntIndex = _FmlHwSensorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110, 2, 1, 1),
    _FmlHwSensorEntIndex_Type()
)
fmlHwSensorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmlHwSensorEntIndex.setStatus("current")
_FmlHwSensorEntName_Type = DisplayString
_FmlHwSensorEntName_Object = MibTableColumn
fmlHwSensorEntName = _FmlHwSensorEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110, 2, 1, 2),
    _FmlHwSensorEntName_Type()
)
fmlHwSensorEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHwSensorEntName.setStatus("current")
_FmlHwSensorEntValue_Type = DisplayString
_FmlHwSensorEntValue_Object = MibTableColumn
fmlHwSensorEntValue = _FmlHwSensorEntValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110, 2, 1, 3),
    _FmlHwSensorEntValue_Type()
)
fmlHwSensorEntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHwSensorEntValue.setStatus("current")


class _FmlHwSensorEntAlarmStatus_Type(Integer32):
    """Custom type fmlHwSensorEntAlarmStatus based on Integer32"""
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


_FmlHwSensorEntAlarmStatus_Type.__name__ = "Integer32"
_FmlHwSensorEntAlarmStatus_Object = MibTableColumn
fmlHwSensorEntAlarmStatus = _FmlHwSensorEntAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 110, 2, 1, 4),
    _FmlHwSensorEntAlarmStatus_Type()
)
fmlHwSensorEntAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHwSensorEntAlarmStatus.setStatus("current")
_FmlSysHA_ObjectIdentity = ObjectIdentity
fmlSysHA = _FmlSysHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 200)
)
_FmlHAMode_Type = FmlHAModeVal
_FmlHAMode_Object = MibScalar
fmlHAMode = _FmlHAMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 200, 1),
    _FmlHAMode_Type()
)
fmlHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHAMode.setStatus("current")
_FmlHAEffectiveMode_Type = FmlHAModeVal
_FmlHAEffectiveMode_Object = MibScalar
fmlHAEffectiveMode = _FmlHAEffectiveMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 105, 1, 200, 2),
    _FmlHAEffectiveMode_Type()
)
fmlHAEffectiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHAEffectiveMode.setStatus("current")
_FmlMIBConformance_ObjectIdentity = ObjectIdentity
fmlMIBConformance = _FmlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600)
)

# Managed Objects groups

fmlSystemConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 1)
)
fmlSystemConformanceGroup.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlSysModel"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysVersion"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysVersionAv"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysOpMode"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysCpuUsage"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysMemUsage"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysLogDiskUsage"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysMailDiskUsage"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysSesCount"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysEventCode"),
        ("FORTINET-FORTIMAIL-MIB", "fmlRAIDCode"),
        ("FORTINET-FORTIMAIL-MIB", "fmlRAIDDevName"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHAEventId"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHAUnitIp"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHAEventReason"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysLoad"))
)
if mibBuilder.loadTexts:
    fmlSystemConformanceGroup.setStatus("current")

fmlSysOptionsConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 2)
)
fmlSysOptionsConformanceGroup.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlSysOptIdleTimeout"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysOptAuthTimeout"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysOptsLcdProt"))
)
if mibBuilder.loadTexts:
    fmlSysOptionsConformanceGroup.setStatus("current")

fmlIpConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 3)
)
fmlIpConformanceGroup.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlIpSessProto"),
        ("FORTINET-FORTIMAIL-MIB", "fmlIpSessFromAddr"),
        ("FORTINET-FORTIMAIL-MIB", "fmlIpSessFromPort"),
        ("FORTINET-FORTIMAIL-MIB", "fmlIpSessToAddr"),
        ("FORTINET-FORTIMAIL-MIB", "fmlIpSessToPort"),
        ("FORTINET-FORTIMAIL-MIB", "fmlIpSessExp"))
)
if mibBuilder.loadTexts:
    fmlIpConformanceGroup.setStatus("current")

fmlMailOptionsConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 4)
)
fmlMailOptionsConformanceGroup.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlMailOptionsDeferQueue")
)
if mibBuilder.loadTexts:
    fmlMailOptionsConformanceGroup.setStatus("current")

fmlHwSensorsConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 5)
)
fmlHwSensorsConformanceGroup.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlHwSensorCount"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHwSensorEntName"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHwSensorEntValue"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHwSensorEntAlarmStatus"))
)
if mibBuilder.loadTexts:
    fmlHwSensorsConformanceGroup.setStatus("current")

fmlHAModeConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 6)
)
fmlHAModeConformanceGroup.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlHAMode"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHAEffectiveMode"))
)
if mibBuilder.loadTexts:
    fmlHAModeConformanceGroup.setStatus("current")


# Notification objects

fmlTrapCpuHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 101)
)
fmlTrapCpuHighThreshold.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapCpuHighThreshold.setStatus(
        "obsolete"
    )

fmlTrapMemLowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 102)
)
fmlTrapMemLowThreshold.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapMemLowThreshold.setStatus(
        "obsolete"
    )

fmlTrapLogDiskHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 103)
)
fmlTrapLogDiskHighThreshold.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapLogDiskHighThreshold.setStatus(
        "obsolete"
    )

fmlTrapMailDiskHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 104)
)
fmlTrapMailDiskHighThreshold.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapMailDiskHighThreshold.setStatus(
        "current"
    )

fmlTrapMailDeferredQueueHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 105)
)
fmlTrapMailDeferredQueueHighThreshold.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapMailDeferredQueueHighThreshold.setStatus(
        "current"
    )

fmlTrapAvThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 106)
)
fmlTrapAvThresholdEvent.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapAvThresholdEvent.setStatus(
        "current"
    )

fmlTrapSpamThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 107)
)
fmlTrapSpamThresholdEvent.setObjects(
    ("FORTINET-FORTIMAIL-MIB", "fmlSysSerial")
)
if mibBuilder.loadTexts:
    fmlTrapSpamThresholdEvent.setStatus(
        "current"
    )

fmlTrapPSUFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 108)
)
fmlTrapPSUFailureEvent.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlSysSerial"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHwSensorEntName"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHwSensorEntValue"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHwSensorEntAlarmStatus"))
)
if mibBuilder.loadTexts:
    fmlTrapPSUFailureEvent.setStatus(
        "obsolete"
    )

fmlTrapSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 201)
)
fmlTrapSystemEvent.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlSysSerial"),
        ("FORTINET-FORTIMAIL-MIB", "fmlSysEventCode"))
)
if mibBuilder.loadTexts:
    fmlTrapSystemEvent.setStatus(
        "current"
    )

fmlTrapRAIDEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 202)
)
fmlTrapRAIDEvent.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlSysSerial"),
        ("FORTINET-FORTIMAIL-MIB", "fmlRAIDCode"),
        ("FORTINET-FORTIMAIL-MIB", "fmlRAIDDevName"))
)
if mibBuilder.loadTexts:
    fmlTrapRAIDEvent.setStatus(
        "current"
    )

fmlTrapHAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 203)
)
fmlTrapHAEvent.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlSysSerial"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHAEventId"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHAUnitIp"),
        ("FORTINET-FORTIMAIL-MIB", "fmlHAEventReason"))
)
if mibBuilder.loadTexts:
    fmlTrapHAEvent.setStatus(
        "current"
    )

fmlTrapIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 105, 0, 301)
)
fmlTrapIpChange.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlSysSerial"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    fmlTrapIpChange.setStatus(
        "obsolete"
    )


# Notifications groups

fmlTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 7)
)
fmlTrapsComplianceGroup.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlTrapMailDiskHighThreshold"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapMailDeferredQueueHighThreshold"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapAvThresholdEvent"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapSpamThresholdEvent"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapSystemEvent"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapRAIDEvent"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapHAEvent"))
)
if mibBuilder.loadTexts:
    fmlTrapsComplianceGroup.setStatus(
        "current"
    )

fmlObsoleteTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 8)
)
fmlObsoleteTrapsComplianceGroup.setObjects(
      *(("FORTINET-FORTIMAIL-MIB", "fmlTrapCpuHighThreshold"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapMemLowThreshold"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapLogDiskHighThreshold"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapPSUFailureEvent"),
        ("FORTINET-FORTIMAIL-MIB", "fmlTrapIpChange"))
)
if mibBuilder.loadTexts:
    fmlObsoleteTrapsComplianceGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

fmlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 100)
)
if mibBuilder.loadTexts:
    fmlMIBCompliance.setStatus(
        "current"
    )

fmlObsoleteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 105, 600, 101)
)
if mibBuilder.loadTexts:
    fmlObsoleteMIBCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIMAIL-MIB",
    **{"FmlOpMode": FmlOpMode,
       "FmlSysEventCodeVal": FmlSysEventCodeVal,
       "FmlRAIDCodeVal": FmlRAIDCodeVal,
       "FmlHAEventIdVal": FmlHAEventIdVal,
       "FmlHAModeVal": FmlHAModeVal,
       "fnFortiMailMib": fnFortiMailMib,
       "fmlTraps": fmlTraps,
       "fmlTrapCpuHighThreshold": fmlTrapCpuHighThreshold,
       "fmlTrapMemLowThreshold": fmlTrapMemLowThreshold,
       "fmlTrapLogDiskHighThreshold": fmlTrapLogDiskHighThreshold,
       "fmlTrapMailDiskHighThreshold": fmlTrapMailDiskHighThreshold,
       "fmlTrapMailDeferredQueueHighThreshold": fmlTrapMailDeferredQueueHighThreshold,
       "fmlTrapAvThresholdEvent": fmlTrapAvThresholdEvent,
       "fmlTrapSpamThresholdEvent": fmlTrapSpamThresholdEvent,
       "fmlTrapPSUFailureEvent": fmlTrapPSUFailureEvent,
       "fmlTrapSystemEvent": fmlTrapSystemEvent,
       "fmlTrapRAIDEvent": fmlTrapRAIDEvent,
       "fmlTrapHAEvent": fmlTrapHAEvent,
       "fmlTrapIpChange": fmlTrapIpChange,
       "fmlSystem": fmlSystem,
       "fmlSysModel": fmlSysModel,
       "fmlSysSerial": fmlSysSerial,
       "fmlSysVersion": fmlSysVersion,
       "fmlSysVersionAv": fmlSysVersionAv,
       "fmlSysOpMode": fmlSysOpMode,
       "fmlSysCpuUsage": fmlSysCpuUsage,
       "fmlSysMemUsage": fmlSysMemUsage,
       "fmlSysLogDiskUsage": fmlSysLogDiskUsage,
       "fmlSysMailDiskUsage": fmlSysMailDiskUsage,
       "fmlSysSesCount": fmlSysSesCount,
       "fmlSysEventCode": fmlSysEventCode,
       "fmlRAIDCode": fmlRAIDCode,
       "fmlRAIDDevName": fmlRAIDDevName,
       "fmlHAEventId": fmlHAEventId,
       "fmlHAUnitIp": fmlHAUnitIp,
       "fmlHAEventReason": fmlHAEventReason,
       "fmlSysLoad": fmlSysLoad,
       "fmlSysOptions": fmlSysOptions,
       "fmlSysOptIdleTimeout": fmlSysOptIdleTimeout,
       "fmlSysOptAuthTimeout": fmlSysOptAuthTimeout,
       "fmlSysOptsLcdProt": fmlSysOptsLcdProt,
       "fmlIp": fmlIp,
       "fmlIpSessTable": fmlIpSessTable,
       "fmlIpSessEntry": fmlIpSessEntry,
       "fmlIpSessIndex": fmlIpSessIndex,
       "fmlIpSessProto": fmlIpSessProto,
       "fmlIpSessFromAddr": fmlIpSessFromAddr,
       "fmlIpSessFromPort": fmlIpSessFromPort,
       "fmlIpSessToAddr": fmlIpSessToAddr,
       "fmlIpSessToPort": fmlIpSessToPort,
       "fmlIpSessExp": fmlIpSessExp,
       "fmlMailOptions": fmlMailOptions,
       "fmlMailOptionsDeferQueue": fmlMailOptionsDeferQueue,
       "fmlHwSensors": fmlHwSensors,
       "fmlHwSensorCount": fmlHwSensorCount,
       "fmlHwSensorTable": fmlHwSensorTable,
       "fmlHwSensorEntry": fmlHwSensorEntry,
       "fmlHwSensorEntIndex": fmlHwSensorEntIndex,
       "fmlHwSensorEntName": fmlHwSensorEntName,
       "fmlHwSensorEntValue": fmlHwSensorEntValue,
       "fmlHwSensorEntAlarmStatus": fmlHwSensorEntAlarmStatus,
       "fmlSysHA": fmlSysHA,
       "fmlHAMode": fmlHAMode,
       "fmlHAEffectiveMode": fmlHAEffectiveMode,
       "fmlMIBConformance": fmlMIBConformance,
       "fmlSystemConformanceGroup": fmlSystemConformanceGroup,
       "fmlSysOptionsConformanceGroup": fmlSysOptionsConformanceGroup,
       "fmlIpConformanceGroup": fmlIpConformanceGroup,
       "fmlMailOptionsConformanceGroup": fmlMailOptionsConformanceGroup,
       "fmlHwSensorsConformanceGroup": fmlHwSensorsConformanceGroup,
       "fmlHAModeConformanceGroup": fmlHAModeConformanceGroup,
       "fmlTrapsComplianceGroup": fmlTrapsComplianceGroup,
       "fmlObsoleteTrapsComplianceGroup": fmlObsoleteTrapsComplianceGroup,
       "fmlMIBCompliance": fmlMIBCompliance,
       "fmlObsoleteMIBCompliance": fmlObsoleteMIBCompliance}
)
