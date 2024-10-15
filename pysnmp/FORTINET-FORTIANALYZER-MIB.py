# SNMP MIB module (FORTINET-FORTIANALYZER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-FORTIANALYZER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:32 2024
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

(FnIndex,
 fnGenTrapMsg,
 fnSysSerial,
 fnTrapsPrefix,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnIndex",
    "fnGenTrapMsg",
    "fnSysSerial",
    "fnTrapsPrefix",
    "fortinet")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

fnFortiAnalyzerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102)
)
fnFortiAnalyzerMib.setRevisions(
        ("2009-09-21 00:00",
         "2009-02-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FaSessProto(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              89,
              103,
              108,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("comp", 108),
          ("egp", 8),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("idp", 22),
          ("igmp", 2),
          ("ip", 0),
          ("ipip", 4),
          ("ipv6", 41),
          ("ospf", 89),
          ("pim", 103),
          ("pup", 12),
          ("raw", 255),
          ("rsvp", 46),
          ("tcp", 6),
          ("udp", 17))
    )



class FaRAIDStatusCode(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("arrayDegraded", 2),
          ("arrayInitializing", 7),
          ("arrayInitializingFinished", 9),
          ("arrayInitializingStarted", 8),
          ("arrayInoperable", 3),
          ("arrayOK", 1),
          ("arrayRebuilding", 4),
          ("arrayRebuildingFinished", 6),
          ("arrayRebuildingStarted", 5),
          ("diskDegraded", 11),
          ("diskFailEvent", 12),
          ("diskOK", 10))
    )



class FaSysEventCode(Integer32, TextualConvention):
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
        *(("logdiskFormat", 5),
          ("systemHalt", 1),
          ("systemReboot", 2),
          ("systemUpgrade", 4),
          ("upgradeConfig", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FaTraps_ObjectIdentity = ObjectIdentity
faTraps = _FaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0)
)
_FaTrapPrefix_ObjectIdentity = ObjectIdentity
faTrapPrefix = _FaTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 0)
)
_FaTrapObject_ObjectIdentity = ObjectIdentity
faTrapObject = _FaTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 1)
)
_FaSystemEvent_Type = FaSysEventCode
_FaSystemEvent_Object = MibScalar
faSystemEvent = _FaSystemEvent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 1),
    _FaSystemEvent_Type()
)
faSystemEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faSystemEvent.setStatus("current")
_FaRAIDStatus_Type = FaRAIDStatusCode
_FaRAIDStatus_Object = MibScalar
faRAIDStatus = _FaRAIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 2),
    _FaRAIDStatus_Type()
)
faRAIDStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faRAIDStatus.setStatus("current")


class _FaRAIDDevIndex_Type(DisplayString):
    """Custom type faRAIDDevIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FaRAIDDevIndex_Type.__name__ = "DisplayString"
_FaRAIDDevIndex_Object = MibScalar
faRAIDDevIndex = _FaRAIDDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 3),
    _FaRAIDDevIndex_Type()
)
faRAIDDevIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    faRAIDDevIndex.setStatus("current")
_FaGenAlert_Type = DisplayString
_FaGenAlert_Object = MibScalar
faGenAlert = _FaGenAlert_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 1, 4),
    _FaGenAlert_Type()
)
faGenAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faGenAlert.setStatus("current")
_FaModel_ObjectIdentity = ObjectIdentity
faModel = _FaModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1)
)
_Faz100_ObjectIdentity = ObjectIdentity
faz100 = _Faz100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 1000)
)
_Faz100A_ObjectIdentity = ObjectIdentity
faz100A = _Faz100A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 1001)
)
_Faz100B_ObjectIdentity = ObjectIdentity
faz100B = _Faz100B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 1002)
)
_Faz100C_ObjectIdentity = ObjectIdentity
faz100C = _Faz100C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 1003)
)
_Faz400_ObjectIdentity = ObjectIdentity
faz400 = _Faz400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 4000)
)
_Faz400B_ObjectIdentity = ObjectIdentity
faz400B = _Faz400B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 4002)
)
_Faz800_ObjectIdentity = ObjectIdentity
faz800 = _Faz800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 8000)
)
_Faz800B_ObjectIdentity = ObjectIdentity
faz800B = _Faz800B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 8002)
)
_Faz1000B_ObjectIdentity = ObjectIdentity
faz1000B = _Faz1000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 10002)
)
_Faz2000_ObjectIdentity = ObjectIdentity
faz2000 = _Faz2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 20000)
)
_Faz2000A_ObjectIdentity = ObjectIdentity
faz2000A = _Faz2000A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 20001)
)
_Faz4000_ObjectIdentity = ObjectIdentity
faz4000 = _Faz4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 40000)
)
_Faz4000A_ObjectIdentity = ObjectIdentity
faz4000A = _Faz4000A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 1, 40001)
)
_FaInetProto_ObjectIdentity = ObjectIdentity
faInetProto = _FaInetProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2)
)
_FaInetProtoInfo_ObjectIdentity = ObjectIdentity
faInetProtoInfo = _FaInetProtoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 1)
)
_FaInetProtoTables_ObjectIdentity = ObjectIdentity
faInetProtoTables = _FaInetProtoTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2)
)
_FaIpSessTable_Object = MibTable
faIpSessTable = _FaIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1)
)
if mibBuilder.loadTexts:
    faIpSessTable.setStatus("current")
_FaIpSessEntry_Object = MibTableRow
faIpSessEntry = _FaIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1)
)
faIpSessEntry.setIndexNames(
    (0, "FORTINET-FORTIANALYZER-MIB", "faIpSessIndex"),
)
if mibBuilder.loadTexts:
    faIpSessEntry.setStatus("current")
_FaIpSessIndex_Type = FnIndex
_FaIpSessIndex_Object = MibTableColumn
faIpSessIndex = _FaIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 1),
    _FaIpSessIndex_Type()
)
faIpSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    faIpSessIndex.setStatus("current")
_FaIpSessProto_Type = FaSessProto
_FaIpSessProto_Object = MibTableColumn
faIpSessProto = _FaIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 2),
    _FaIpSessProto_Type()
)
faIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faIpSessProto.setStatus("current")
_FaIpSessFromAddr_Type = IpAddress
_FaIpSessFromAddr_Object = MibTableColumn
faIpSessFromAddr = _FaIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 3),
    _FaIpSessFromAddr_Type()
)
faIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faIpSessFromAddr.setStatus("current")
_FaIpSessFromPort_Type = InetPortNumber
_FaIpSessFromPort_Object = MibTableColumn
faIpSessFromPort = _FaIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 4),
    _FaIpSessFromPort_Type()
)
faIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faIpSessFromPort.setStatus("current")
_FaIpSessToAddr_Type = IpAddress
_FaIpSessToAddr_Object = MibTableColumn
faIpSessToAddr = _FaIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 5),
    _FaIpSessToAddr_Type()
)
faIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faIpSessToAddr.setStatus("current")
_FaIpSessToPort_Type = InetPortNumber
_FaIpSessToPort_Object = MibTableColumn
faIpSessToPort = _FaIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 6),
    _FaIpSessToPort_Type()
)
faIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faIpSessToPort.setStatus("current")
_FaIpSessExp_Type = Counter32
_FaIpSessExp_Object = MibTableColumn
faIpSessExp = _FaIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 2, 2, 1, 1, 7),
    _FaIpSessExp_Type()
)
faIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faIpSessExp.setStatus("current")
_Fa300Compat_ObjectIdentity = ObjectIdentity
fa300Compat = _Fa300Compat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99)
)
_FaHwSensors_ObjectIdentity = ObjectIdentity
faHwSensors = _FaHwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1)
)
_FaHwSensorCount_Type = Integer32
_FaHwSensorCount_Object = MibScalar
faHwSensorCount = _FaHwSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 1),
    _FaHwSensorCount_Type()
)
faHwSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faHwSensorCount.setStatus("deprecated")
_FaHwSensorTable_Object = MibTable
faHwSensorTable = _FaHwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2)
)
if mibBuilder.loadTexts:
    faHwSensorTable.setStatus("deprecated")
_FaHwSensorEntry_Object = MibTableRow
faHwSensorEntry = _FaHwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1)
)
faHwSensorEntry.setIndexNames(
    (0, "FORTINET-FORTIANALYZER-MIB", "faHwSensorEntIndex"),
)
if mibBuilder.loadTexts:
    faHwSensorEntry.setStatus("deprecated")
_FaHwSensorEntIndex_Type = FnIndex
_FaHwSensorEntIndex_Object = MibTableColumn
faHwSensorEntIndex = _FaHwSensorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 1),
    _FaHwSensorEntIndex_Type()
)
faHwSensorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    faHwSensorEntIndex.setStatus("deprecated")
_FaHwSensorEntName_Type = DisplayString
_FaHwSensorEntName_Object = MibTableColumn
faHwSensorEntName = _FaHwSensorEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 2),
    _FaHwSensorEntName_Type()
)
faHwSensorEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faHwSensorEntName.setStatus("deprecated")
_FaHwSensorEntValue_Type = DisplayString
_FaHwSensorEntValue_Object = MibTableColumn
faHwSensorEntValue = _FaHwSensorEntValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 3),
    _FaHwSensorEntValue_Type()
)
faHwSensorEntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faHwSensorEntValue.setStatus("deprecated")


class _FaHwSensorEntAlarmStatus_Type(Integer32):
    """Custom type faHwSensorEntAlarmStatus based on Integer32"""
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


_FaHwSensorEntAlarmStatus_Type.__name__ = "Integer32"
_FaHwSensorEntAlarmStatus_Object = MibTableColumn
faHwSensorEntAlarmStatus = _FaHwSensorEntAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 1, 2, 1, 4),
    _FaHwSensorEntAlarmStatus_Type()
)
faHwSensorEntAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faHwSensorEntAlarmStatus.setStatus("deprecated")
_Fa300System_ObjectIdentity = ObjectIdentity
fa300System = _Fa300System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2)
)


class _Fa300SysSerial_Type(DisplayString):
    """Custom type fa300SysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fa300SysSerial_Type.__name__ = "DisplayString"
_Fa300SysSerial_Object = MibScalar
fa300SysSerial = _Fa300SysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 1),
    _Fa300SysSerial_Type()
)
fa300SysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysSerial.setStatus("current")


class _Fa300SysVersion_Type(DisplayString):
    """Custom type fa300SysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Fa300SysVersion_Type.__name__ = "DisplayString"
_Fa300SysVersion_Object = MibScalar
fa300SysVersion = _Fa300SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 2),
    _Fa300SysVersion_Type()
)
fa300SysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysVersion.setStatus("current")


class _Fa300SysCpuUsage_Type(Gauge32):
    """Custom type fa300SysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fa300SysCpuUsage_Type.__name__ = "Gauge32"
_Fa300SysCpuUsage_Object = MibScalar
fa300SysCpuUsage = _Fa300SysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 3),
    _Fa300SysCpuUsage_Type()
)
fa300SysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysCpuUsage.setStatus("current")


class _Fa300SysMemUsage_Type(Gauge32):
    """Custom type fa300SysMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fa300SysMemUsage_Type.__name__ = "Gauge32"
_Fa300SysMemUsage_Object = MibScalar
fa300SysMemUsage = _Fa300SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 4),
    _Fa300SysMemUsage_Type()
)
fa300SysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysMemUsage.setStatus("current")
_Fa300SysSesCount_Type = Gauge32
_Fa300SysSesCount_Object = MibScalar
fa300SysSesCount = _Fa300SysSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 5),
    _Fa300SysSesCount_Type()
)
fa300SysSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysSesCount.setStatus("current")
_Fa300SysDiskCapacity_Type = Gauge32
_Fa300SysDiskCapacity_Object = MibScalar
fa300SysDiskCapacity = _Fa300SysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 6),
    _Fa300SysDiskCapacity_Type()
)
fa300SysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysDiskCapacity.setStatus("current")
_Fa300SysDiskUsage_Type = Gauge32
_Fa300SysDiskUsage_Object = MibScalar
fa300SysDiskUsage = _Fa300SysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 7),
    _Fa300SysDiskUsage_Type()
)
fa300SysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysDiskUsage.setStatus("current")
_Fa300SysMemCapacity_Type = Gauge32
_Fa300SysMemCapacity_Object = MibScalar
fa300SysMemCapacity = _Fa300SysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 102, 99, 2, 8),
    _Fa300SysMemCapacity_Type()
)
fa300SysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fa300SysMemCapacity.setStatus("current")
_FaMIBConformance_ObjectIdentity = ObjectIdentity
faMIBConformance = _FaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100)
)

# Managed Objects groups

faSystemComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 1)
)
faSystemComplianceGroup.setObjects(
      *(("FORTINET-FORTIANALYZER-MIB", "fa300SysSerial"),
        ("FORTINET-FORTIANALYZER-MIB", "fa300SysVersion"),
        ("FORTINET-FORTIANALYZER-MIB", "fa300SysCpuUsage"),
        ("FORTINET-FORTIANALYZER-MIB", "fa300SysMemUsage"),
        ("FORTINET-FORTIANALYZER-MIB", "fa300SysDiskCapacity"),
        ("FORTINET-FORTIANALYZER-MIB", "fa300SysDiskUsage"),
        ("FORTINET-FORTIANALYZER-MIB", "fa300SysMemCapacity"),
        ("FORTINET-FORTIANALYZER-MIB", "fa300SysSesCount"),
        ("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"))
)
if mibBuilder.loadTexts:
    faSystemComplianceGroup.setStatus("current")

faSessionComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 3)
)
faSessionComplianceGroup.setObjects(
      *(("FORTINET-FORTIANALYZER-MIB", "faIpSessProto"),
        ("FORTINET-FORTIANALYZER-MIB", "faIpSessFromAddr"),
        ("FORTINET-FORTIANALYZER-MIB", "faIpSessFromPort"),
        ("FORTINET-FORTIANALYZER-MIB", "faIpSessToAddr"),
        ("FORTINET-FORTIANALYZER-MIB", "faIpSessToPort"),
        ("FORTINET-FORTIANALYZER-MIB", "faIpSessExp"))
)
if mibBuilder.loadTexts:
    faSessionComplianceGroup.setStatus("current")

faMiscComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 4)
)
faMiscComplianceGroup.setObjects(
    ("FORTINET-FORTIANALYZER-MIB", "faGenAlert")
)
if mibBuilder.loadTexts:
    faMiscComplianceGroup.setStatus("current")

faHwSensorComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 5)
)
faHwSensorComplianceGroup.setObjects(
      *(("FORTINET-FORTIANALYZER-MIB", "faHwSensorCount"),
        ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntName"),
        ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntValue"),
        ("FORTINET-FORTIANALYZER-MIB", "faHwSensorEntAlarmStatus"))
)
if mibBuilder.loadTexts:
    faHwSensorComplianceGroup.setStatus("deprecated")

faNotificationObjectsComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 6)
)
faNotificationObjectsComplianceGroup.setObjects(
      *(("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"),
        ("FORTINET-FORTIANALYZER-MIB", "faRAIDStatus"),
        ("FORTINET-FORTIANALYZER-MIB", "faRAIDDevIndex"))
)
if mibBuilder.loadTexts:
    faNotificationObjectsComplianceGroup.setStatus("current")


# Notification objects

faTrapLogRateThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 1005)
)
faTrapLogRateThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    faTrapLogRateThreshold.setStatus(
        "current"
    )

faTrapDataRateThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 1006)
)
faTrapDataRateThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    faTrapDataRateThreshold.setStatus(
        "current"
    )

faTrapSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1001)
)
faTrapSystemEvent.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("FORTINET-FORTIANALYZER-MIB", "faSystemEvent"))
)
if mibBuilder.loadTexts:
    faTrapSystemEvent.setStatus(
        "current"
    )

faTrapRAIDStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1002)
)
faTrapRAIDStatusChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("FORTINET-FORTIANALYZER-MIB", "faRAIDStatus"),
        ("FORTINET-FORTIANALYZER-MIB", "faRAIDDevIndex"))
)
if mibBuilder.loadTexts:
    faTrapRAIDStatusChange.setStatus(
        "current"
    )

faTrapGenAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 102, 0, 0, 1003)
)
faTrapGenAlert.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    faTrapGenAlert.setStatus(
        "current"
    )


# Notifications groups

faTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 2)
)
faTrapsComplianceGroup.setObjects(
      *(("FORTINET-FORTIANALYZER-MIB", "faTrapSystemEvent"),
        ("FORTINET-FORTIANALYZER-MIB", "faTrapRAIDStatusChange"),
        ("FORTINET-FORTIANALYZER-MIB", "faTrapGenAlert"),
        ("FORTINET-FORTIANALYZER-MIB", "faTrapLogRateThreshold"),
        ("FORTINET-FORTIANALYZER-MIB", "faTrapDataRateThreshold"))
)
if mibBuilder.loadTexts:
    faTrapsComplianceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

faMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 100)
)
if mibBuilder.loadTexts:
    faMIBCompliance.setStatus(
        "current"
    )

faObsoleteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 102, 100, 101)
)
if mibBuilder.loadTexts:
    faObsoleteMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIANALYZER-MIB",
    **{"FaSessProto": FaSessProto,
       "FaRAIDStatusCode": FaRAIDStatusCode,
       "FaSysEventCode": FaSysEventCode,
       "faTrapLogRateThreshold": faTrapLogRateThreshold,
       "faTrapDataRateThreshold": faTrapDataRateThreshold,
       "fnFortiAnalyzerMib": fnFortiAnalyzerMib,
       "faTraps": faTraps,
       "faTrapPrefix": faTrapPrefix,
       "faTrapSystemEvent": faTrapSystemEvent,
       "faTrapRAIDStatusChange": faTrapRAIDStatusChange,
       "faTrapGenAlert": faTrapGenAlert,
       "faTrapObject": faTrapObject,
       "faSystemEvent": faSystemEvent,
       "faRAIDStatus": faRAIDStatus,
       "faRAIDDevIndex": faRAIDDevIndex,
       "faGenAlert": faGenAlert,
       "faModel": faModel,
       "faz100": faz100,
       "faz100A": faz100A,
       "faz100B": faz100B,
       "faz100C": faz100C,
       "faz400": faz400,
       "faz400B": faz400B,
       "faz800": faz800,
       "faz800B": faz800B,
       "faz1000B": faz1000B,
       "faz2000": faz2000,
       "faz2000A": faz2000A,
       "faz4000": faz4000,
       "faz4000A": faz4000A,
       "faInetProto": faInetProto,
       "faInetProtoInfo": faInetProtoInfo,
       "faInetProtoTables": faInetProtoTables,
       "faIpSessTable": faIpSessTable,
       "faIpSessEntry": faIpSessEntry,
       "faIpSessIndex": faIpSessIndex,
       "faIpSessProto": faIpSessProto,
       "faIpSessFromAddr": faIpSessFromAddr,
       "faIpSessFromPort": faIpSessFromPort,
       "faIpSessToAddr": faIpSessToAddr,
       "faIpSessToPort": faIpSessToPort,
       "faIpSessExp": faIpSessExp,
       "fa300Compat": fa300Compat,
       "faHwSensors": faHwSensors,
       "faHwSensorCount": faHwSensorCount,
       "faHwSensorTable": faHwSensorTable,
       "faHwSensorEntry": faHwSensorEntry,
       "faHwSensorEntIndex": faHwSensorEntIndex,
       "faHwSensorEntName": faHwSensorEntName,
       "faHwSensorEntValue": faHwSensorEntValue,
       "faHwSensorEntAlarmStatus": faHwSensorEntAlarmStatus,
       "fa300System": fa300System,
       "fa300SysSerial": fa300SysSerial,
       "fa300SysVersion": fa300SysVersion,
       "fa300SysCpuUsage": fa300SysCpuUsage,
       "fa300SysMemUsage": fa300SysMemUsage,
       "fa300SysSesCount": fa300SysSesCount,
       "fa300SysDiskCapacity": fa300SysDiskCapacity,
       "fa300SysDiskUsage": fa300SysDiskUsage,
       "fa300SysMemCapacity": fa300SysMemCapacity,
       "faMIBConformance": faMIBConformance,
       "faSystemComplianceGroup": faSystemComplianceGroup,
       "faTrapsComplianceGroup": faTrapsComplianceGroup,
       "faSessionComplianceGroup": faSessionComplianceGroup,
       "faMiscComplianceGroup": faMiscComplianceGroup,
       "faHwSensorComplianceGroup": faHwSensorComplianceGroup,
       "faNotificationObjectsComplianceGroup": faNotificationObjectsComplianceGroup,
       "faMIBCompliance": faMIBCompliance,
       "faObsoleteMIBCompliance": faObsoleteMIBCompliance}
)
