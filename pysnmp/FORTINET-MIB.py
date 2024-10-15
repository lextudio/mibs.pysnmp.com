# SNMP MIB module (FORTINET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:36 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class AuthAlgorithm(Integer32):
    """Custom type AuthAlgorithm based on Integer32"""
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
        *(("aes128", 4),
          ("aes192", 5),
          ("aes256", 6),
          ("md5", 2),
          ("null", 1),
          ("sha1", 3))
    )





class EncrytionAlgorithm(Integer32):
    """Custom type EncrytionAlgorithm based on Integer32"""
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
        *(("aes128", 4),
          ("aes192", 5),
          ("aes256", 6),
          ("des", 2),
          ("null", 1),
          ("tripleDes", 3))
    )





class LanguageCode(Integer32):
    """Custom type LanguageCode based on Integer32"""
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
        *(("default", 6),
          ("japanese", 4),
          ("kerean", 5),
          ("simplifiedChinese", 2),
          ("traditionalChinese", 3),
          ("western", 1))
    )





class ItemState(Integer32):
    """Custom type ItemState based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fortinet_ObjectIdentity = ObjectIdentity
fortinet = _Fortinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356)
)
_FnSystem_ObjectIdentity = ObjectIdentity
fnSystem = _FnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1)
)
_FnSysStatus_ObjectIdentity = ObjectIdentity
fnSysStatus = _FnSysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1)
)


class _FnSysStatusOpMode_Type(Integer32):
    """Custom type fnSysStatusOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat", 1),
          ("transparent", 2))
    )


_FnSysStatusOpMode_Type.__name__ = "Integer32"
_FnSysStatusOpMode_Object = MibScalar
fnSysStatusOpMode = _FnSysStatusOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 1),
    _FnSysStatusOpMode_Type()
)
fnSysStatusOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysStatusOpMode.setStatus("mandatory")


class _FnSysStatusVersion_Type(DisplayString):
    """Custom type fnSysStatusVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysStatusVersion_Type.__name__ = "DisplayString"
_FnSysStatusVersion_Object = MibScalar
fnSysStatusVersion = _FnSysStatusVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 2),
    _FnSysStatusVersion_Type()
)
fnSysStatusVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysStatusVersion.setStatus("mandatory")


class _FnSysStatusAVDBVersion_Type(DisplayString):
    """Custom type fnSysStatusAVDBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysStatusAVDBVersion_Type.__name__ = "DisplayString"
_FnSysStatusAVDBVersion_Object = MibScalar
fnSysStatusAVDBVersion = _FnSysStatusAVDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 3),
    _FnSysStatusAVDBVersion_Type()
)
fnSysStatusAVDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysStatusAVDBVersion.setStatus("mandatory")


class _FnSysStatusNIDSDBVersion_Type(DisplayString):
    """Custom type fnSysStatusNIDSDBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysStatusNIDSDBVersion_Type.__name__ = "DisplayString"
_FnSysStatusNIDSDBVersion_Object = MibScalar
fnSysStatusNIDSDBVersion = _FnSysStatusNIDSDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 4),
    _FnSysStatusNIDSDBVersion_Type()
)
fnSysStatusNIDSDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysStatusNIDSDBVersion.setStatus("mandatory")


class _FnSysStatusSN_Type(DisplayString):
    """Custom type fnSysStatusSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnSysStatusSN_Type.__name__ = "DisplayString"
_FnSysStatusSN_Object = MibScalar
fnSysStatusSN = _FnSysStatusSN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 5),
    _FnSysStatusSN_Type()
)
fnSysStatusSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysStatusSN.setStatus("mandatory")
_FnSysMonitor_ObjectIdentity = ObjectIdentity
fnSysMonitor = _FnSysMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6)
)


class _FnSysMonCPUUsage_Type(Integer32):
    """Custom type fnSysMonCPUUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FnSysMonCPUUsage_Type.__name__ = "Integer32"
_FnSysMonCPUUsage_Object = MibScalar
fnSysMonCPUUsage = _FnSysMonCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 1),
    _FnSysMonCPUUsage_Type()
)
fnSysMonCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonCPUUsage.setStatus("mandatory")


class _FnSysMonCPUIdle_Type(Integer32):
    """Custom type fnSysMonCPUIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnSysMonCPUIdle_Type.__name__ = "Integer32"
_FnSysMonCPUIdle_Object = MibScalar
fnSysMonCPUIdle = _FnSysMonCPUIdle_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 2),
    _FnSysMonCPUIdle_Type()
)
fnSysMonCPUIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonCPUIdle.setStatus("mandatory")


class _FnSysMonCPUInt_Type(Integer32):
    """Custom type fnSysMonCPUInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnSysMonCPUInt_Type.__name__ = "Integer32"
_FnSysMonCPUInt_Object = MibScalar
fnSysMonCPUInt = _FnSysMonCPUInt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 3),
    _FnSysMonCPUInt_Type()
)
fnSysMonCPUInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonCPUInt.setStatus("mandatory")


class _FnSysMonMemUsage_Type(Integer32):
    """Custom type fnSysMonMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnSysMonMemUsage_Type.__name__ = "Integer32"
_FnSysMonMemUsage_Object = MibScalar
fnSysMonMemUsage = _FnSysMonMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 4),
    _FnSysMonMemUsage_Type()
)
fnSysMonMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonMemUsage.setStatus("mandatory")
_FnSysMonUpTime_Type = TimeTicks
_FnSysMonUpTime_Object = MibScalar
fnSysMonUpTime = _FnSysMonUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 5),
    _FnSysMonUpTime_Type()
)
fnSysMonUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonUpTime.setStatus("mandatory")


class _FnSysMonSessionNum_Type(Integer32):
    """Custom type fnSysMonSessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysMonSessionNum_Type.__name__ = "Integer32"
_FnSysMonSessionNum_Object = MibScalar
fnSysMonSessionNum = _FnSysMonSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 6),
    _FnSysMonSessionNum_Type()
)
fnSysMonSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonSessionNum.setStatus("mandatory")
_FnSysMonConnTable_Object = MibTable
fnSysMonConnTable = _FnSysMonConnTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    fnSysMonConnTable.setStatus("mandatory")
_FnSysMonConnEntry_Object = MibTableRow
fnSysMonConnEntry = _FnSysMonConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1)
)
fnSysMonConnEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysMonConnIndex"),
)
if mibBuilder.loadTexts:
    fnSysMonConnEntry.setStatus("mandatory")


class _FnSysMonConnIndex_Type(Integer32):
    """Custom type fnSysMonConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysMonConnIndex_Type.__name__ = "Integer32"
_FnSysMonConnIndex_Object = MibTableColumn
fnSysMonConnIndex = _FnSysMonConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1, 1),
    _FnSysMonConnIndex_Type()
)
fnSysMonConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysMonConnIndex.setStatus("mandatory")


class _FnSysMonConnProto_Type(Integer32):
    """Custom type fnSysMonConnProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_FnSysMonConnProto_Type.__name__ = "Integer32"
_FnSysMonConnProto_Object = MibTableColumn
fnSysMonConnProto = _FnSysMonConnProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1, 2),
    _FnSysMonConnProto_Type()
)
fnSysMonConnProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonConnProto.setStatus("mandatory")
_FnSysMonConnFromAddr_Type = IpAddress
_FnSysMonConnFromAddr_Object = MibTableColumn
fnSysMonConnFromAddr = _FnSysMonConnFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1, 3),
    _FnSysMonConnFromAddr_Type()
)
fnSysMonConnFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonConnFromAddr.setStatus("mandatory")


class _FnSysMonConnFromPort_Type(Integer32):
    """Custom type fnSysMonConnFromPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnSysMonConnFromPort_Type.__name__ = "Integer32"
_FnSysMonConnFromPort_Object = MibTableColumn
fnSysMonConnFromPort = _FnSysMonConnFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1, 4),
    _FnSysMonConnFromPort_Type()
)
fnSysMonConnFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonConnFromPort.setStatus("mandatory")
_FnSysMonConnToAddr_Type = IpAddress
_FnSysMonConnToAddr_Object = MibTableColumn
fnSysMonConnToAddr = _FnSysMonConnToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1, 5),
    _FnSysMonConnToAddr_Type()
)
fnSysMonConnToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonConnToAddr.setStatus("mandatory")


class _FnSysMonConnToPort_Type(Integer32):
    """Custom type fnSysMonConnToPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnSysMonConnToPort_Type.__name__ = "Integer32"
_FnSysMonConnToPort_Object = MibTableColumn
fnSysMonConnToPort = _FnSysMonConnToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1, 6),
    _FnSysMonConnToPort_Type()
)
fnSysMonConnToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonConnToPort.setStatus("mandatory")
_FnSysMonConnExp_Type = Integer32
_FnSysMonConnExp_Object = MibTableColumn
fnSysMonConnExp = _FnSysMonConnExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1, 6, 7, 1, 7),
    _FnSysMonConnExp_Type()
)
fnSysMonConnExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMonConnExp.setStatus("mandatory")
_FnSysUpdate_ObjectIdentity = ObjectIdentity
fnSysUpdate = _FnSysUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2)
)
_FnSysUpdateConnStatus1_Type = ItemState
_FnSysUpdateConnStatus1_Object = MibScalar
fnSysUpdateConnStatus1 = _FnSysUpdateConnStatus1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 1),
    _FnSysUpdateConnStatus1_Type()
)
fnSysUpdateConnStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateConnStatus1.setStatus("mandatory")
_FnSysUpdateConnStatus2_Type = ItemState
_FnSysUpdateConnStatus2_Object = MibScalar
fnSysUpdateConnStatus2 = _FnSysUpdateConnStatus2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 2),
    _FnSysUpdateConnStatus2_Type()
)
fnSysUpdateConnStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateConnStatus2.setStatus("mandatory")


class _FnSysUpdatePushUpState_Type(Integer32):
    """Custom type fnSysUpdatePushUpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_FnSysUpdatePushUpState_Type.__name__ = "Integer32"
_FnSysUpdatePushUpState_Object = MibScalar
fnSysUpdatePushUpState = _FnSysUpdatePushUpState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 3),
    _FnSysUpdatePushUpState_Type()
)
fnSysUpdatePushUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdatePushUpState.setStatus("mandatory")


class _FnSysUpdatePeriodicUpState_Type(Integer32):
    """Custom type fnSysUpdatePeriodicUpState based on Integer32"""
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


_FnSysUpdatePeriodicUpState_Type.__name__ = "Integer32"
_FnSysUpdatePeriodicUpState_Object = MibScalar
fnSysUpdatePeriodicUpState = _FnSysUpdatePeriodicUpState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 4),
    _FnSysUpdatePeriodicUpState_Type()
)
fnSysUpdatePeriodicUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdatePeriodicUpState.setStatus("mandatory")


class _FnSysUpdatePeriodicUpFreq_Type(Integer32):
    """Custom type fnSysUpdatePeriodicUpFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("other", 3),
          ("weekly", 2))
    )


_FnSysUpdatePeriodicUpFreq_Type.__name__ = "Integer32"
_FnSysUpdatePeriodicUpFreq_Object = MibScalar
fnSysUpdatePeriodicUpFreq = _FnSysUpdatePeriodicUpFreq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 5),
    _FnSysUpdatePeriodicUpFreq_Type()
)
fnSysUpdatePeriodicUpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdatePeriodicUpFreq.setStatus("mandatory")


class _FnSysUpdatePeriodicUpDay_Type(Integer32):
    """Custom type fnSysUpdatePeriodicUpDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_FnSysUpdatePeriodicUpDay_Type.__name__ = "Integer32"
_FnSysUpdatePeriodicUpDay_Object = MibScalar
fnSysUpdatePeriodicUpDay = _FnSysUpdatePeriodicUpDay_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 6),
    _FnSysUpdatePeriodicUpDay_Type()
)
fnSysUpdatePeriodicUpDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdatePeriodicUpDay.setStatus("mandatory")
_FnSysUpdatePeriodicUpTime_Type = DisplayString
_FnSysUpdatePeriodicUpTime_Object = MibScalar
fnSysUpdatePeriodicUpTime = _FnSysUpdatePeriodicUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 7),
    _FnSysUpdatePeriodicUpTime_Type()
)
fnSysUpdatePeriodicUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdatePeriodicUpTime.setStatus("mandatory")
_FnSysUpdateVirusDefUpStatus_Type = DisplayString
_FnSysUpdateVirusDefUpStatus_Object = MibScalar
fnSysUpdateVirusDefUpStatus = _FnSysUpdateVirusDefUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 8),
    _FnSysUpdateVirusDefUpStatus_Type()
)
fnSysUpdateVirusDefUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateVirusDefUpStatus.setStatus("mandatory")
_FnSysUpdateVirusDefUpLast_Type = DisplayString
_FnSysUpdateVirusDefUpLast_Object = MibScalar
fnSysUpdateVirusDefUpLast = _FnSysUpdateVirusDefUpLast_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 9),
    _FnSysUpdateVirusDefUpLast_Type()
)
fnSysUpdateVirusDefUpLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateVirusDefUpLast.setStatus("mandatory")
_FnSysUpdateIdsUpStatus_Type = DisplayString
_FnSysUpdateIdsUpStatus_Object = MibScalar
fnSysUpdateIdsUpStatus = _FnSysUpdateIdsUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 10),
    _FnSysUpdateIdsUpStatus_Type()
)
fnSysUpdateIdsUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateIdsUpStatus.setStatus("mandatory")
_FnSysUpdateIdsUpLast_Type = DisplayString
_FnSysUpdateIdsUpLast_Object = MibScalar
fnSysUpdateIdsUpLast = _FnSysUpdateIdsUpLast_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 11),
    _FnSysUpdateIdsUpLast_Type()
)
fnSysUpdateIdsUpLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateIdsUpLast.setStatus("mandatory")
_FnSysUpdateSpamDefUpStatus_Type = DisplayString
_FnSysUpdateSpamDefUpStatus_Object = MibScalar
fnSysUpdateSpamDefUpStatus = _FnSysUpdateSpamDefUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 12),
    _FnSysUpdateSpamDefUpStatus_Type()
)
fnSysUpdateSpamDefUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateSpamDefUpStatus.setStatus("mandatory")


class _FnSysUpdateSpamDefUpLast_Type(DisplayString):
    """Custom type fnSysUpdateSpamDefUpLast based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnSysUpdateSpamDefUpLast_Type.__name__ = "DisplayString"
_FnSysUpdateSpamDefUpLast_Object = MibScalar
fnSysUpdateSpamDefUpLast = _FnSysUpdateSpamDefUpLast_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2, 13),
    _FnSysUpdateSpamDefUpLast_Type()
)
fnSysUpdateSpamDefUpLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysUpdateSpamDefUpLast.setStatus("mandatory")
_FnSysNetwork_ObjectIdentity = ObjectIdentity
fnSysNetwork = _FnSysNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3)
)
_FnSysNetworkIfTable_Object = MibTable
fnSysNetworkIfTable = _FnSysNetworkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fnSysNetworkIfTable.setStatus("mandatory")
_FnSysNetworkIfEntry_Object = MibTableRow
fnSysNetworkIfEntry = _FnSysNetworkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1)
)
fnSysNetworkIfEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysNetworkIfIndex"),
)
if mibBuilder.loadTexts:
    fnSysNetworkIfEntry.setStatus("mandatory")


class _FnSysNetworkIfIndex_Type(Integer32):
    """Custom type fnSysNetworkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysNetworkIfIndex_Type.__name__ = "Integer32"
_FnSysNetworkIfIndex_Object = MibTableColumn
fnSysNetworkIfIndex = _FnSysNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 1),
    _FnSysNetworkIfIndex_Type()
)
fnSysNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfIndex.setStatus("mandatory")


class _FnSysNetworkIfName_Type(DisplayString):
    """Custom type fnSysNetworkIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnSysNetworkIfName_Type.__name__ = "DisplayString"
_FnSysNetworkIfName_Object = MibTableColumn
fnSysNetworkIfName = _FnSysNetworkIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 2),
    _FnSysNetworkIfName_Type()
)
fnSysNetworkIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfName.setStatus("mandatory")
_FnSysNetworkIfIp_Type = IpAddress
_FnSysNetworkIfIp_Object = MibTableColumn
fnSysNetworkIfIp = _FnSysNetworkIfIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 3),
    _FnSysNetworkIfIp_Type()
)
fnSysNetworkIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfIp.setStatus("mandatory")
_FnSysNetworkIfNetmask_Type = IpAddress
_FnSysNetworkIfNetmask_Object = MibTableColumn
fnSysNetworkIfNetmask = _FnSysNetworkIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 4),
    _FnSysNetworkIfNetmask_Type()
)
fnSysNetworkIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfNetmask.setStatus("mandatory")


class _FnSysNetworkIfMAC_Type(DisplayString):
    """Custom type fnSysNetworkIfMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnSysNetworkIfMAC_Type.__name__ = "DisplayString"
_FnSysNetworkIfMAC_Object = MibTableColumn
fnSysNetworkIfMAC = _FnSysNetworkIfMAC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 5),
    _FnSysNetworkIfMAC_Type()
)
fnSysNetworkIfMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfMAC.setStatus("mandatory")


class _FnSysNetworkIfSpeed_Type(DisplayString):
    """Custom type fnSysNetworkIfSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnSysNetworkIfSpeed_Type.__name__ = "DisplayString"
_FnSysNetworkIfSpeed_Object = MibTableColumn
fnSysNetworkIfSpeed = _FnSysNetworkIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 6),
    _FnSysNetworkIfSpeed_Type()
)
fnSysNetworkIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfSpeed.setStatus("mandatory")
_FnSysNetworkIfOutFrag_Type = ItemState
_FnSysNetworkIfOutFrag_Object = MibTableColumn
fnSysNetworkIfOutFrag = _FnSysNetworkIfOutFrag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 7),
    _FnSysNetworkIfOutFrag_Type()
)
fnSysNetworkIfOutFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfOutFrag.setStatus("mandatory")


class _FnSysNetworkIfStatus_Type(Integer32):
    """Custom type fnSysNetworkIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_FnSysNetworkIfStatus_Type.__name__ = "Integer32"
_FnSysNetworkIfStatus_Object = MibTableColumn
fnSysNetworkIfStatus = _FnSysNetworkIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 8),
    _FnSysNetworkIfStatus_Type()
)
fnSysNetworkIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfStatus.setStatus("mandatory")


class _FnSysNetworkIfAddrMode_Type(Integer32):
    """Custom type fnSysNetworkIfAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("manual", 1),
          ("pppoe", 3))
    )


_FnSysNetworkIfAddrMode_Type.__name__ = "Integer32"
_FnSysNetworkIfAddrMode_Object = MibTableColumn
fnSysNetworkIfAddrMode = _FnSysNetworkIfAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 9),
    _FnSysNetworkIfAddrMode_Type()
)
fnSysNetworkIfAddrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfAddrMode.setStatus("mandatory")
_FnSysNetworkIfAccHttps_Type = ItemState
_FnSysNetworkIfAccHttps_Object = MibTableColumn
fnSysNetworkIfAccHttps = _FnSysNetworkIfAccHttps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 10),
    _FnSysNetworkIfAccHttps_Type()
)
fnSysNetworkIfAccHttps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfAccHttps.setStatus("mandatory")
_FnSysNetworkIfAccPing_Type = ItemState
_FnSysNetworkIfAccPing_Object = MibTableColumn
fnSysNetworkIfAccPing = _FnSysNetworkIfAccPing_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 11),
    _FnSysNetworkIfAccPing_Type()
)
fnSysNetworkIfAccPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfAccPing.setStatus("mandatory")
_FnSysNetworkIfAccSsh_Type = ItemState
_FnSysNetworkIfAccSsh_Object = MibTableColumn
fnSysNetworkIfAccSsh = _FnSysNetworkIfAccSsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 12),
    _FnSysNetworkIfAccSsh_Type()
)
fnSysNetworkIfAccSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfAccSsh.setStatus("mandatory")
_FnSysNetworkIfAccSnmp_Type = ItemState
_FnSysNetworkIfAccSnmp_Object = MibTableColumn
fnSysNetworkIfAccSnmp = _FnSysNetworkIfAccSnmp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 13),
    _FnSysNetworkIfAccSnmp_Type()
)
fnSysNetworkIfAccSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfAccSnmp.setStatus("mandatory")
_FnSysNetworkIfAccHttp_Type = ItemState
_FnSysNetworkIfAccHttp_Object = MibTableColumn
fnSysNetworkIfAccHttp = _FnSysNetworkIfAccHttp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 14),
    _FnSysNetworkIfAccHttp_Type()
)
fnSysNetworkIfAccHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfAccHttp.setStatus("mandatory")
_FnSysNetworkIfAccTelnet_Type = ItemState
_FnSysNetworkIfAccTelnet_Object = MibTableColumn
fnSysNetworkIfAccTelnet = _FnSysNetworkIfAccTelnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 15),
    _FnSysNetworkIfAccTelnet_Type()
)
fnSysNetworkIfAccTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfAccTelnet.setStatus("mandatory")
_FnSysNetworkIfPingSrvState_Type = ItemState
_FnSysNetworkIfPingSrvState_Object = MibTableColumn
fnSysNetworkIfPingSrvState = _FnSysNetworkIfPingSrvState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 16),
    _FnSysNetworkIfPingSrvState_Type()
)
fnSysNetworkIfPingSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfPingSrvState.setStatus("mandatory")
_FnSysNetworkIfPingSrvAddr_Type = IpAddress
_FnSysNetworkIfPingSrvAddr_Object = MibTableColumn
fnSysNetworkIfPingSrvAddr = _FnSysNetworkIfPingSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 17),
    _FnSysNetworkIfPingSrvAddr_Type()
)
fnSysNetworkIfPingSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfPingSrvAddr.setStatus("mandatory")
_FnSysNetworkIfIp2_Type = IpAddress
_FnSysNetworkIfIp2_Object = MibTableColumn
fnSysNetworkIfIp2 = _FnSysNetworkIfIp2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 18),
    _FnSysNetworkIfIp2_Type()
)
fnSysNetworkIfIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfIp2.setStatus("mandatory")
_FnSysNetworkIfNetmask2_Type = IpAddress
_FnSysNetworkIfNetmask2_Object = MibTableColumn
fnSysNetworkIfNetmask2 = _FnSysNetworkIfNetmask2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 19),
    _FnSysNetworkIfNetmask2_Type()
)
fnSysNetworkIfNetmask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfNetmask2.setStatus("mandatory")
_FnSysNetworkIfPingSrvState2_Type = ItemState
_FnSysNetworkIfPingSrvState2_Object = MibTableColumn
fnSysNetworkIfPingSrvState2 = _FnSysNetworkIfPingSrvState2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 20),
    _FnSysNetworkIfPingSrvState2_Type()
)
fnSysNetworkIfPingSrvState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfPingSrvState2.setStatus("mandatory")
_FnSysNetworkIfPingSrvAddr2_Type = IpAddress
_FnSysNetworkIfPingSrvAddr2_Object = MibTableColumn
fnSysNetworkIfPingSrvAddr2 = _FnSysNetworkIfPingSrvAddr2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 1, 1, 21),
    _FnSysNetworkIfPingSrvAddr2_Type()
)
fnSysNetworkIfPingSrvAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkIfPingSrvAddr2.setStatus("mandatory")
_FnSysNetworkVlanTable_Object = MibTable
fnSysNetworkVlanTable = _FnSysNetworkVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fnSysNetworkVlanTable.setStatus("mandatory")
_FnSysNetworkVlanEntry_Object = MibTableRow
fnSysNetworkVlanEntry = _FnSysNetworkVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1)
)
fnSysNetworkVlanEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysNetworkVlanIndex"),
    (0, "FORTINET-MIB", "fnSysNetworkVlanName"),
)
if mibBuilder.loadTexts:
    fnSysNetworkVlanEntry.setStatus("mandatory")


class _FnSysNetworkVlanIndex_Type(Integer32):
    """Custom type fnSysNetworkVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysNetworkVlanIndex_Type.__name__ = "Integer32"
_FnSysNetworkVlanIndex_Object = MibTableColumn
fnSysNetworkVlanIndex = _FnSysNetworkVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 1),
    _FnSysNetworkVlanIndex_Type()
)
fnSysNetworkVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysNetworkVlanIndex.setStatus("mandatory")


class _FnSysNetworkVlanName_Type(DisplayString):
    """Custom type fnSysNetworkVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnSysNetworkVlanName_Type.__name__ = "DisplayString"
_FnSysNetworkVlanName_Object = MibTableColumn
fnSysNetworkVlanName = _FnSysNetworkVlanName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 2),
    _FnSysNetworkVlanName_Type()
)
fnSysNetworkVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysNetworkVlanName.setStatus("mandatory")
_FnSysNetworkVlanIf_Type = DisplayString
_FnSysNetworkVlanIf_Object = MibTableColumn
fnSysNetworkVlanIf = _FnSysNetworkVlanIf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 3),
    _FnSysNetworkVlanIf_Type()
)
fnSysNetworkVlanIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanIf.setStatus("mandatory")


class _FnSysNetworkVlanId_Type(Integer32):
    """Custom type fnSysNetworkVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnSysNetworkVlanId_Type.__name__ = "Integer32"
_FnSysNetworkVlanId_Object = MibTableColumn
fnSysNetworkVlanId = _FnSysNetworkVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 4),
    _FnSysNetworkVlanId_Type()
)
fnSysNetworkVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanId.setStatus("mandatory")
_FnSysNetworkVlanIp_Type = IpAddress
_FnSysNetworkVlanIp_Object = MibTableColumn
fnSysNetworkVlanIp = _FnSysNetworkVlanIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 5),
    _FnSysNetworkVlanIp_Type()
)
fnSysNetworkVlanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanIp.setStatus("mandatory")
_FnSysNetworkVlanNetmask_Type = IpAddress
_FnSysNetworkVlanNetmask_Object = MibTableColumn
fnSysNetworkVlanNetmask = _FnSysNetworkVlanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 6),
    _FnSysNetworkVlanNetmask_Type()
)
fnSysNetworkVlanNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanNetmask.setStatus("mandatory")
_FnSysNetworkVlanAccHttps_Type = ItemState
_FnSysNetworkVlanAccHttps_Object = MibTableColumn
fnSysNetworkVlanAccHttps = _FnSysNetworkVlanAccHttps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 7),
    _FnSysNetworkVlanAccHttps_Type()
)
fnSysNetworkVlanAccHttps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanAccHttps.setStatus("mandatory")
_FnSysNetworkVlanAccPing_Type = ItemState
_FnSysNetworkVlanAccPing_Object = MibTableColumn
fnSysNetworkVlanAccPing = _FnSysNetworkVlanAccPing_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 8),
    _FnSysNetworkVlanAccPing_Type()
)
fnSysNetworkVlanAccPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanAccPing.setStatus("mandatory")
_FnSysNetworkVlanAccSsh_Type = ItemState
_FnSysNetworkVlanAccSsh_Object = MibTableColumn
fnSysNetworkVlanAccSsh = _FnSysNetworkVlanAccSsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 9),
    _FnSysNetworkVlanAccSsh_Type()
)
fnSysNetworkVlanAccSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanAccSsh.setStatus("mandatory")
_FnSysNetworkVlanAccSnmp_Type = ItemState
_FnSysNetworkVlanAccSnmp_Object = MibTableColumn
fnSysNetworkVlanAccSnmp = _FnSysNetworkVlanAccSnmp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 10),
    _FnSysNetworkVlanAccSnmp_Type()
)
fnSysNetworkVlanAccSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanAccSnmp.setStatus("mandatory")
_FnSysNetworkVlanAccHttp_Type = ItemState
_FnSysNetworkVlanAccHttp_Object = MibTableColumn
fnSysNetworkVlanAccHttp = _FnSysNetworkVlanAccHttp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 11),
    _FnSysNetworkVlanAccHttp_Type()
)
fnSysNetworkVlanAccHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanAccHttp.setStatus("mandatory")
_FnSysNetworkVlanAccTelnet_Type = ItemState
_FnSysNetworkVlanAccTelnet_Object = MibTableColumn
fnSysNetworkVlanAccTelnet = _FnSysNetworkVlanAccTelnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 2, 1, 12),
    _FnSysNetworkVlanAccTelnet_Type()
)
fnSysNetworkVlanAccTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkVlanAccTelnet.setStatus("mandatory")
_FnSysNetworkAccessTable_Object = MibTable
fnSysNetworkAccessTable = _FnSysNetworkAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3)
)
if mibBuilder.loadTexts:
    fnSysNetworkAccessTable.setStatus("mandatory")
_FnSysNetworkAccessEntry_Object = MibTableRow
fnSysNetworkAccessEntry = _FnSysNetworkAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1)
)
fnSysNetworkAccessEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysNetworkAccessIfName"),
)
if mibBuilder.loadTexts:
    fnSysNetworkAccessEntry.setStatus("mandatory")


class _FnSysNetworkAccessIfName_Type(Integer32):
    """Custom type fnSysNetworkAccessIfName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnSysNetworkAccessIfName_Type.__name__ = "Integer32"
_FnSysNetworkAccessIfName_Object = MibTableColumn
fnSysNetworkAccessIfName = _FnSysNetworkAccessIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1, 1),
    _FnSysNetworkAccessIfName_Type()
)
fnSysNetworkAccessIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkAccessIfName.setStatus("mandatory")
_FnSysNetworkAccessHttps_Type = ItemState
_FnSysNetworkAccessHttps_Object = MibTableColumn
fnSysNetworkAccessHttps = _FnSysNetworkAccessHttps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1, 2),
    _FnSysNetworkAccessHttps_Type()
)
fnSysNetworkAccessHttps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkAccessHttps.setStatus("mandatory")
_FnSysNetworkAccessPing_Type = ItemState
_FnSysNetworkAccessPing_Object = MibTableColumn
fnSysNetworkAccessPing = _FnSysNetworkAccessPing_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1, 3),
    _FnSysNetworkAccessPing_Type()
)
fnSysNetworkAccessPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkAccessPing.setStatus("mandatory")
_FnSysNetworkAccessSsh_Type = ItemState
_FnSysNetworkAccessSsh_Object = MibTableColumn
fnSysNetworkAccessSsh = _FnSysNetworkAccessSsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1, 4),
    _FnSysNetworkAccessSsh_Type()
)
fnSysNetworkAccessSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkAccessSsh.setStatus("mandatory")
_FnSysNetworkAccessSnmp_Type = ItemState
_FnSysNetworkAccessSnmp_Object = MibTableColumn
fnSysNetworkAccessSnmp = _FnSysNetworkAccessSnmp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1, 5),
    _FnSysNetworkAccessSnmp_Type()
)
fnSysNetworkAccessSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkAccessSnmp.setStatus("mandatory")
_FnSysNetworkAccessHttp_Type = ItemState
_FnSysNetworkAccessHttp_Object = MibTableColumn
fnSysNetworkAccessHttp = _FnSysNetworkAccessHttp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1, 6),
    _FnSysNetworkAccessHttp_Type()
)
fnSysNetworkAccessHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkAccessHttp.setStatus("mandatory")
_FnSysNetworkAccessTelnet_Type = ItemState
_FnSysNetworkAccessTelnet_Object = MibTableColumn
fnSysNetworkAccessTelnet = _FnSysNetworkAccessTelnet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 3, 1, 7),
    _FnSysNetworkAccessTelnet_Type()
)
fnSysNetworkAccessTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkAccessTelnet.setStatus("mandatory")
_FnSysNetworkRouting_ObjectIdentity = ObjectIdentity
fnSysNetworkRouting = _FnSysNetworkRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4)
)
_FnSysNetworkRoutingTable_Object = MibTable
fnSysNetworkRoutingTable = _FnSysNetworkRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    fnSysNetworkRoutingTable.setStatus("mandatory")
_FnSysNetworkRoutingEntry_Object = MibTableRow
fnSysNetworkRoutingEntry = _FnSysNetworkRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1)
)
fnSysNetworkRoutingEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysNetworkRoutingIndex"),
)
if mibBuilder.loadTexts:
    fnSysNetworkRoutingEntry.setStatus("mandatory")


class _FnSysNetworkRoutingIndex_Type(Integer32):
    """Custom type fnSysNetworkRoutingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysNetworkRoutingIndex_Type.__name__ = "Integer32"
_FnSysNetworkRoutingIndex_Object = MibTableColumn
fnSysNetworkRoutingIndex = _FnSysNetworkRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 1),
    _FnSysNetworkRoutingIndex_Type()
)
fnSysNetworkRoutingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingIndex.setStatus("mandatory")
_FnSysNetworkRoutingSrcIP_Type = IpAddress
_FnSysNetworkRoutingSrcIP_Object = MibTableColumn
fnSysNetworkRoutingSrcIP = _FnSysNetworkRoutingSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 2),
    _FnSysNetworkRoutingSrcIP_Type()
)
fnSysNetworkRoutingSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingSrcIP.setStatus("mandatory")
_FnSysNetworkRoutingSrcNetmask_Type = IpAddress
_FnSysNetworkRoutingSrcNetmask_Object = MibTableColumn
fnSysNetworkRoutingSrcNetmask = _FnSysNetworkRoutingSrcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 3),
    _FnSysNetworkRoutingSrcNetmask_Type()
)
fnSysNetworkRoutingSrcNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingSrcNetmask.setStatus("mandatory")
_FnSysNetworkRoutingDstIP_Type = IpAddress
_FnSysNetworkRoutingDstIP_Object = MibTableColumn
fnSysNetworkRoutingDstIP = _FnSysNetworkRoutingDstIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 4),
    _FnSysNetworkRoutingDstIP_Type()
)
fnSysNetworkRoutingDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingDstIP.setStatus("mandatory")
_FnSysNetworkRoutingDstNetmask_Type = IpAddress
_FnSysNetworkRoutingDstNetmask_Object = MibTableColumn
fnSysNetworkRoutingDstNetmask = _FnSysNetworkRoutingDstNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 5),
    _FnSysNetworkRoutingDstNetmask_Type()
)
fnSysNetworkRoutingDstNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingDstNetmask.setStatus("mandatory")
_FnSysNetworkRoutingGW1_Type = IpAddress
_FnSysNetworkRoutingGW1_Object = MibTableColumn
fnSysNetworkRoutingGW1 = _FnSysNetworkRoutingGW1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 6),
    _FnSysNetworkRoutingGW1_Type()
)
fnSysNetworkRoutingGW1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingGW1.setStatus("mandatory")
_FnSysNetworkRoutingGW2_Type = IpAddress
_FnSysNetworkRoutingGW2_Object = MibTableColumn
fnSysNetworkRoutingGW2 = _FnSysNetworkRoutingGW2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 7),
    _FnSysNetworkRoutingGW2_Type()
)
fnSysNetworkRoutingGW2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingGW2.setStatus("mandatory")
_FnSysNetworkRoutingDev1_Type = DisplayString
_FnSysNetworkRoutingDev1_Object = MibTableColumn
fnSysNetworkRoutingDev1 = _FnSysNetworkRoutingDev1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 8),
    _FnSysNetworkRoutingDev1_Type()
)
fnSysNetworkRoutingDev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingDev1.setStatus("mandatory")
_FnSysNetworkRoutingDev2_Type = DisplayString
_FnSysNetworkRoutingDev2_Object = MibTableColumn
fnSysNetworkRoutingDev2 = _FnSysNetworkRoutingDev2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 1, 1, 9),
    _FnSysNetworkRoutingDev2_Type()
)
fnSysNetworkRoutingDev2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingDev2.setStatus("mandatory")


class _FnSysNetworkRoutingRIPSrv_Type(Integer32):
    """Custom type fnSysNetworkRoutingRIPSrv based on Integer32"""
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


_FnSysNetworkRoutingRIPSrv_Type.__name__ = "Integer32"
_FnSysNetworkRoutingRIPSrv_Object = MibScalar
fnSysNetworkRoutingRIPSrv = _FnSysNetworkRoutingRIPSrv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 3),
    _FnSysNetworkRoutingRIPSrv_Type()
)
fnSysNetworkRoutingRIPSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingRIPSrv.setStatus("mandatory")
_FnSysNetworkRoutingGWTable_Object = MibTable
fnSysNetworkRoutingGWTable = _FnSysNetworkRoutingGWTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    fnSysNetworkRoutingGWTable.setStatus("mandatory")
_FnSysNetworkRoutingGWEntry_Object = MibTableRow
fnSysNetworkRoutingGWEntry = _FnSysNetworkRoutingGWEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 4, 1)
)
fnSysNetworkRoutingGWEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysNetworkRoutingGWIndex"),
)
if mibBuilder.loadTexts:
    fnSysNetworkRoutingGWEntry.setStatus("mandatory")


class _FnSysNetworkRoutingGWIndex_Type(Integer32):
    """Custom type fnSysNetworkRoutingGWIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysNetworkRoutingGWIndex_Type.__name__ = "Integer32"
_FnSysNetworkRoutingGWIndex_Object = MibTableColumn
fnSysNetworkRoutingGWIndex = _FnSysNetworkRoutingGWIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 4, 1, 1),
    _FnSysNetworkRoutingGWIndex_Type()
)
fnSysNetworkRoutingGWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingGWIndex.setStatus("mandatory")
_FnSysNetworkRoutingGWIP_Type = IpAddress
_FnSysNetworkRoutingGWIP_Object = MibTableColumn
fnSysNetworkRoutingGWIP = _FnSysNetworkRoutingGWIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 4, 1, 2),
    _FnSysNetworkRoutingGWIP_Type()
)
fnSysNetworkRoutingGWIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingGWIP.setStatus("mandatory")
_FnSysNetworkRoutingGWDeadDet_Type = ItemState
_FnSysNetworkRoutingGWDeadDet_Object = MibTableColumn
fnSysNetworkRoutingGWDeadDet = _FnSysNetworkRoutingGWDeadDet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 4, 4, 1, 3),
    _FnSysNetworkRoutingGWDeadDet_Type()
)
fnSysNetworkRoutingGWDeadDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkRoutingGWDeadDet.setStatus("mandatory")
_FnSysNetworkDhcp_ObjectIdentity = ObjectIdentity
fnSysNetworkDhcp = _FnSysNetworkDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5)
)
_FnSysNetworkDhcpStatus_Type = ItemState
_FnSysNetworkDhcpStatus_Object = MibScalar
fnSysNetworkDhcpStatus = _FnSysNetworkDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 1),
    _FnSysNetworkDhcpStatus_Type()
)
fnSysNetworkDhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpStatus.setStatus("mandatory")
_FnSysNetworkDhcpSip_Type = IpAddress
_FnSysNetworkDhcpSip_Object = MibScalar
fnSysNetworkDhcpSip = _FnSysNetworkDhcpSip_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 2),
    _FnSysNetworkDhcpSip_Type()
)
fnSysNetworkDhcpSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpSip.setStatus("mandatory")
_FnSysNetworkDhcpEip_Type = IpAddress
_FnSysNetworkDhcpEip_Object = MibScalar
fnSysNetworkDhcpEip = _FnSysNetworkDhcpEip_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 3),
    _FnSysNetworkDhcpEip_Type()
)
fnSysNetworkDhcpEip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpEip.setStatus("mandatory")
_FnSysNetworkDhcpLeaseDur_Type = TimeTicks
_FnSysNetworkDhcpLeaseDur_Object = MibScalar
fnSysNetworkDhcpLeaseDur = _FnSysNetworkDhcpLeaseDur_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 4),
    _FnSysNetworkDhcpLeaseDur_Type()
)
fnSysNetworkDhcpLeaseDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpLeaseDur.setStatus("mandatory")
_FnSysNetworkDhcpDomain_Type = DisplayString
_FnSysNetworkDhcpDomain_Object = MibScalar
fnSysNetworkDhcpDomain = _FnSysNetworkDhcpDomain_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 5),
    _FnSysNetworkDhcpDomain_Type()
)
fnSysNetworkDhcpDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpDomain.setStatus("mandatory")
_FnSysNetworkDhcpDNS1_Type = IpAddress
_FnSysNetworkDhcpDNS1_Object = MibScalar
fnSysNetworkDhcpDNS1 = _FnSysNetworkDhcpDNS1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 6),
    _FnSysNetworkDhcpDNS1_Type()
)
fnSysNetworkDhcpDNS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpDNS1.setStatus("mandatory")
_FnSysNetworkDhcpDNS2_Type = IpAddress
_FnSysNetworkDhcpDNS2_Object = MibScalar
fnSysNetworkDhcpDNS2 = _FnSysNetworkDhcpDNS2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 7),
    _FnSysNetworkDhcpDNS2_Type()
)
fnSysNetworkDhcpDNS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpDNS2.setStatus("mandatory")
_FnSysNetworkDhcpDNS3_Type = IpAddress
_FnSysNetworkDhcpDNS3_Object = MibScalar
fnSysNetworkDhcpDNS3 = _FnSysNetworkDhcpDNS3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 8),
    _FnSysNetworkDhcpDNS3_Type()
)
fnSysNetworkDhcpDNS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpDNS3.setStatus("mandatory")
_FnSysNetworkDhcpDefRoute_Type = IpAddress
_FnSysNetworkDhcpDefRoute_Object = MibScalar
fnSysNetworkDhcpDefRoute = _FnSysNetworkDhcpDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 9),
    _FnSysNetworkDhcpDefRoute_Type()
)
fnSysNetworkDhcpDefRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpDefRoute.setStatus("mandatory")
_FnSysNetworkDhcpExclRange1S_Type = IpAddress
_FnSysNetworkDhcpExclRange1S_Object = MibScalar
fnSysNetworkDhcpExclRange1S = _FnSysNetworkDhcpExclRange1S_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 10),
    _FnSysNetworkDhcpExclRange1S_Type()
)
fnSysNetworkDhcpExclRange1S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpExclRange1S.setStatus("mandatory")
_FnSysNetworkDhcpExclRange1E_Type = IpAddress
_FnSysNetworkDhcpExclRange1E_Object = MibScalar
fnSysNetworkDhcpExclRange1E = _FnSysNetworkDhcpExclRange1E_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 11),
    _FnSysNetworkDhcpExclRange1E_Type()
)
fnSysNetworkDhcpExclRange1E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpExclRange1E.setStatus("mandatory")
_FnSysNetworkDhcpExclRange2S_Type = IpAddress
_FnSysNetworkDhcpExclRange2S_Object = MibScalar
fnSysNetworkDhcpExclRange2S = _FnSysNetworkDhcpExclRange2S_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 12),
    _FnSysNetworkDhcpExclRange2S_Type()
)
fnSysNetworkDhcpExclRange2S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpExclRange2S.setStatus("mandatory")
_FnSysNetworkDhcpExclRange2E_Type = IpAddress
_FnSysNetworkDhcpExclRange2E_Object = MibScalar
fnSysNetworkDhcpExclRange2E = _FnSysNetworkDhcpExclRange2E_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 13),
    _FnSysNetworkDhcpExclRange2E_Type()
)
fnSysNetworkDhcpExclRange2E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpExclRange2E.setStatus("mandatory")
_FnSysNetworkDhcpExclRange3S_Type = IpAddress
_FnSysNetworkDhcpExclRange3S_Object = MibScalar
fnSysNetworkDhcpExclRange3S = _FnSysNetworkDhcpExclRange3S_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 14),
    _FnSysNetworkDhcpExclRange3S_Type()
)
fnSysNetworkDhcpExclRange3S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpExclRange3S.setStatus("mandatory")
_FnSysNetworkDhcpExclRange3E_Type = IpAddress
_FnSysNetworkDhcpExclRange3E_Object = MibScalar
fnSysNetworkDhcpExclRange3E = _FnSysNetworkDhcpExclRange3E_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 5, 15),
    _FnSysNetworkDhcpExclRange3E_Type()
)
fnSysNetworkDhcpExclRange3E.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDhcpExclRange3E.setStatus("mandatory")
_FnSysZoneTable_Object = MibTable
fnSysZoneTable = _FnSysZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 6)
)
if mibBuilder.loadTexts:
    fnSysZoneTable.setStatus("mandatory")
_FnSysZoneEntry_Object = MibTableRow
fnSysZoneEntry = _FnSysZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 6, 1)
)
fnSysZoneEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysZoneId"),
)
if mibBuilder.loadTexts:
    fnSysZoneEntry.setStatus("mandatory")


class _FnSysZoneId_Type(Integer32):
    """Custom type fnSysZoneId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysZoneId_Type.__name__ = "Integer32"
_FnSysZoneId_Object = MibTableColumn
fnSysZoneId = _FnSysZoneId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 6, 1, 1),
    _FnSysZoneId_Type()
)
fnSysZoneId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysZoneId.setStatus("mandatory")
_FnSysZoneName_Type = DisplayString
_FnSysZoneName_Object = MibTableColumn
fnSysZoneName = _FnSysZoneName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 6, 1, 2),
    _FnSysZoneName_Type()
)
fnSysZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysZoneName.setStatus("mandatory")
_FnSysZoneSecLevel_Type = Integer32
_FnSysZoneSecLevel_Object = MibTableColumn
fnSysZoneSecLevel = _FnSysZoneSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 6, 1, 3),
    _FnSysZoneSecLevel_Type()
)
fnSysZoneSecLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysZoneSecLevel.setStatus("mandatory")
_FnSysZoneBlkTraffic_Type = ItemState
_FnSysZoneBlkTraffic_Object = MibTableColumn
fnSysZoneBlkTraffic = _FnSysZoneBlkTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 6, 1, 4),
    _FnSysZoneBlkTraffic_Type()
)
fnSysZoneBlkTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysZoneBlkTraffic.setStatus("mandatory")
_FnSysZoneLogTraffic_Type = ItemState
_FnSysZoneLogTraffic_Object = MibTableColumn
fnSysZoneLogTraffic = _FnSysZoneLogTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 6, 1, 5),
    _FnSysZoneLogTraffic_Type()
)
fnSysZoneLogTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysZoneLogTraffic.setStatus("mandatory")
_FnSysNetworkDNS_ObjectIdentity = ObjectIdentity
fnSysNetworkDNS = _FnSysNetworkDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 7)
)
_FnSysNetworkDNSPri_Type = IpAddress
_FnSysNetworkDNSPri_Object = MibScalar
fnSysNetworkDNSPri = _FnSysNetworkDNSPri_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 7, 1),
    _FnSysNetworkDNSPri_Type()
)
fnSysNetworkDNSPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDNSPri.setStatus("mandatory")
_FnSysNetworkDNSSecPri_Type = IpAddress
_FnSysNetworkDNSSecPri_Object = MibScalar
fnSysNetworkDNSSecPri = _FnSysNetworkDNSSecPri_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3, 7, 2),
    _FnSysNetworkDNSSecPri_Type()
)
fnSysNetworkDNSSecPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysNetworkDNSSecPri.setStatus("mandatory")
_FnSysConfig_ObjectIdentity = ObjectIdentity
fnSysConfig = _FnSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4)
)
_FnSysConfigTime_ObjectIdentity = ObjectIdentity
fnSysConfigTime = _FnSysConfigTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 1)
)


class _FnSysConfigTimeVal_Type(DisplayString):
    """Custom type fnSysConfigTimeVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysConfigTimeVal_Type.__name__ = "DisplayString"
_FnSysConfigTimeVal_Object = MibScalar
fnSysConfigTimeVal = _FnSysConfigTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 1, 1),
    _FnSysConfigTimeVal_Type()
)
fnSysConfigTimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigTimeVal.setStatus("mandatory")


class _FnSysConfigTimezone_Type(DisplayString):
    """Custom type fnSysConfigTimezone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnSysConfigTimezone_Type.__name__ = "DisplayString"
_FnSysConfigTimezone_Object = MibScalar
fnSysConfigTimezone = _FnSysConfigTimezone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 1, 2),
    _FnSysConfigTimezone_Type()
)
fnSysConfigTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigTimezone.setStatus("mandatory")
_FnSysConfigTimeDST_Type = ItemState
_FnSysConfigTimeDST_Object = MibScalar
fnSysConfigTimeDST = _FnSysConfigTimeDST_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 1, 3),
    _FnSysConfigTimeDST_Type()
)
fnSysConfigTimeDST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigTimeDST.setStatus("mandatory")
_FnSysConfigTimeNTPSrv_Type = IpAddress
_FnSysConfigTimeNTPSrv_Object = MibScalar
fnSysConfigTimeNTPSrv = _FnSysConfigTimeNTPSrv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 1, 4),
    _FnSysConfigTimeNTPSrv_Type()
)
fnSysConfigTimeNTPSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigTimeNTPSrv.setStatus("mandatory")
_FnSysConfigTimeNTPInt_Type = Integer32
_FnSysConfigTimeNTPInt_Object = MibScalar
fnSysConfigTimeNTPInt = _FnSysConfigTimeNTPInt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 1, 5),
    _FnSysConfigTimeNTPInt_Type()
)
fnSysConfigTimeNTPInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigTimeNTPInt.setStatus("mandatory")
_FnSysConfigNTPState_Type = ItemState
_FnSysConfigNTPState_Object = MibScalar
fnSysConfigNTPState = _FnSysConfigNTPState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 1, 6),
    _FnSysConfigNTPState_Type()
)
fnSysConfigNTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigNTPState.setStatus("mandatory")
_FnSysConfigOpts_ObjectIdentity = ObjectIdentity
fnSysConfigOpts = _FnSysConfigOpts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 2)
)
_FnSysConfigOptsIdleTimeout_Type = Integer32
_FnSysConfigOptsIdleTimeout_Object = MibScalar
fnSysConfigOptsIdleTimeout = _FnSysConfigOptsIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 2, 1),
    _FnSysConfigOptsIdleTimeout_Type()
)
fnSysConfigOptsIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigOptsIdleTimeout.setStatus("mandatory")


class _FnSysConfigOptsAuthTimeout_Type(Integer32):
    """Custom type fnSysConfigOptsAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnSysConfigOptsAuthTimeout_Type.__name__ = "Integer32"
_FnSysConfigOptsAuthTimeout_Object = MibScalar
fnSysConfigOptsAuthTimeout = _FnSysConfigOptsAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 2, 2),
    _FnSysConfigOptsAuthTimeout_Type()
)
fnSysConfigOptsAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigOptsAuthTimeout.setStatus("mandatory")
_FnSysConfigOptsLan_Type = LanguageCode
_FnSysConfigOptsLan_Object = MibScalar
fnSysConfigOptsLan = _FnSysConfigOptsLan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 2, 3),
    _FnSysConfigOptsLan_Type()
)
fnSysConfigOptsLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigOptsLan.setStatus("mandatory")
_FnSysConfigOptsLcdProt_Type = ItemState
_FnSysConfigOptsLcdProt_Object = MibScalar
fnSysConfigOptsLcdProt = _FnSysConfigOptsLcdProt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 2, 4),
    _FnSysConfigOptsLcdProt_Type()
)
fnSysConfigOptsLcdProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigOptsLcdProt.setStatus("mandatory")
_FnSysConfigOptsLcdProtPin_Type = OctetString
_FnSysConfigOptsLcdProtPin_Object = MibScalar
fnSysConfigOptsLcdProtPin = _FnSysConfigOptsLcdProtPin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 2, 5),
    _FnSysConfigOptsLcdProtPin_Type()
)
fnSysConfigOptsLcdProtPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigOptsLcdProtPin.setStatus("mandatory")
_FnSysConfigAdmin_ObjectIdentity = ObjectIdentity
fnSysConfigAdmin = _FnSysConfigAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3)
)
_FnSysConfigAdminUserTable_Object = MibTable
fnSysConfigAdminUserTable = _FnSysConfigAdminUserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    fnSysConfigAdminUserTable.setStatus("mandatory")
_FnSysConfigAdminUserEntry_Object = MibTableRow
fnSysConfigAdminUserEntry = _FnSysConfigAdminUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3, 1, 1)
)
fnSysConfigAdminUserEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysConfigAdminUserIndex"),
)
if mibBuilder.loadTexts:
    fnSysConfigAdminUserEntry.setStatus("mandatory")


class _FnSysConfigAdminUserIndex_Type(Integer32):
    """Custom type fnSysConfigAdminUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysConfigAdminUserIndex_Type.__name__ = "Integer32"
_FnSysConfigAdminUserIndex_Object = MibTableColumn
fnSysConfigAdminUserIndex = _FnSysConfigAdminUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3, 1, 1, 1),
    _FnSysConfigAdminUserIndex_Type()
)
fnSysConfigAdminUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigAdminUserIndex.setStatus("mandatory")


class _FnSysConfigAdminUserName_Type(DisplayString):
    """Custom type fnSysConfigAdminUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnSysConfigAdminUserName_Type.__name__ = "DisplayString"
_FnSysConfigAdminUserName_Object = MibTableColumn
fnSysConfigAdminUserName = _FnSysConfigAdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3, 1, 1, 2),
    _FnSysConfigAdminUserName_Type()
)
fnSysConfigAdminUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigAdminUserName.setStatus("mandatory")
_FnSysConfigAdminUserIp_Type = IpAddress
_FnSysConfigAdminUserIp_Object = MibTableColumn
fnSysConfigAdminUserIp = _FnSysConfigAdminUserIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3, 1, 1, 3),
    _FnSysConfigAdminUserIp_Type()
)
fnSysConfigAdminUserIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigAdminUserIp.setStatus("mandatory")
_FnSysConfigAdminUserNetmask_Type = IpAddress
_FnSysConfigAdminUserNetmask_Object = MibTableColumn
fnSysConfigAdminUserNetmask = _FnSysConfigAdminUserNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3, 1, 1, 4),
    _FnSysConfigAdminUserNetmask_Type()
)
fnSysConfigAdminUserNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigAdminUserNetmask.setStatus("mandatory")


class _FnSysConfigAdminUserPermission_Type(Integer32):
    """Custom type fnSysConfigAdminUserPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("read", 1),
          ("readWrite", 2))
    )


_FnSysConfigAdminUserPermission_Type.__name__ = "Integer32"
_FnSysConfigAdminUserPermission_Object = MibTableColumn
fnSysConfigAdminUserPermission = _FnSysConfigAdminUserPermission_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 3, 1, 1, 5),
    _FnSysConfigAdminUserPermission_Type()
)
fnSysConfigAdminUserPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigAdminUserPermission.setStatus("mandatory")
_FnSysConfigHA_ObjectIdentity = ObjectIdentity
fnSysConfigHA = _FnSysConfigHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 4)
)


class _FnSysConfigHAMode_Type(Integer32):
    """Custom type fnSysConfigHAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeActive", 2),
          ("activePassive", 3),
          ("standalone", 0))
    )


_FnSysConfigHAMode_Type.__name__ = "Integer32"
_FnSysConfigHAMode_Object = MibScalar
fnSysConfigHAMode = _FnSysConfigHAMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 4, 1),
    _FnSysConfigHAMode_Type()
)
fnSysConfigHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigHAMode.setStatus("mandatory")
_FnSysConfigHAGrpId_Type = Integer32
_FnSysConfigHAGrpId_Object = MibScalar
fnSysConfigHAGrpId = _FnSysConfigHAGrpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 4, 2),
    _FnSysConfigHAGrpId_Type()
)
fnSysConfigHAGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigHAGrpId.setStatus("mandatory")
_FnSysConfigHAPasswd_Type = OctetString
_FnSysConfigHAPasswd_Object = MibScalar
fnSysConfigHAPasswd = _FnSysConfigHAPasswd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 4, 3),
    _FnSysConfigHAPasswd_Type()
)
fnSysConfigHAPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigHAPasswd.setStatus("mandatory")
_FnSysConfigHAMonIf_Type = DisplayString
_FnSysConfigHAMonIf_Object = MibScalar
fnSysConfigHAMonIf = _FnSysConfigHAMonIf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 4, 4),
    _FnSysConfigHAMonIf_Type()
)
fnSysConfigHAMonIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigHAMonIf.setStatus("mandatory")


class _FnSysConfigHASchedule_Type(Integer32):
    """Custom type fnSysConfigHASchedule based on Integer32"""
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
        *(("hub", 2),
          ("ip", 7),
          ("ipPort", 8),
          ("leastConn", 3),
          ("none", 1),
          ("random", 6),
          ("roundRobin", 4),
          ("weightRoundRobin", 5))
    )


_FnSysConfigHASchedule_Type.__name__ = "Integer32"
_FnSysConfigHASchedule_Object = MibScalar
fnSysConfigHASchedule = _FnSysConfigHASchedule_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4, 4, 5),
    _FnSysConfigHASchedule_Type()
)
fnSysConfigHASchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysConfigHASchedule.setStatus("mandatory")
_FnSysSnmp_ObjectIdentity = ObjectIdentity
fnSysSnmp = _FnSysSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5)
)
_FnSysSnmpGen_ObjectIdentity = ObjectIdentity
fnSysSnmpGen = _FnSysSnmpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1)
)
_FnSysSnmpState_Type = ItemState
_FnSysSnmpState_Object = MibScalar
fnSysSnmpState = _FnSysSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 1),
    _FnSysSnmpState_Type()
)
fnSysSnmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpState.setStatus("mandatory")


class _FnSysSnmpSysName_Type(DisplayString):
    """Custom type fnSysSnmpSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnSysSnmpSysName_Type.__name__ = "DisplayString"
_FnSysSnmpSysName_Object = MibScalar
fnSysSnmpSysName = _FnSysSnmpSysName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 2),
    _FnSysSnmpSysName_Type()
)
fnSysSnmpSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSysName.setStatus("mandatory")
_FnSysSnmpSysLoc_Type = DisplayString
_FnSysSnmpSysLoc_Object = MibScalar
fnSysSnmpSysLoc = _FnSysSnmpSysLoc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 3),
    _FnSysSnmpSysLoc_Type()
)
fnSysSnmpSysLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSysLoc.setStatus("mandatory")
_FnSysSnmpInfo_Type = DisplayString
_FnSysSnmpInfo_Object = MibScalar
fnSysSnmpInfo = _FnSysSnmpInfo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 4),
    _FnSysSnmpInfo_Type()
)
fnSysSnmpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpInfo.setStatus("mandatory")
_FnSysSnmpGetCom_Type = DisplayString
_FnSysSnmpGetCom_Object = MibScalar
fnSysSnmpGetCom = _FnSysSnmpGetCom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 5),
    _FnSysSnmpGetCom_Type()
)
fnSysSnmpGetCom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpGetCom.setStatus("mandatory")
_FnSysSnmpTrapCom_Type = DisplayString
_FnSysSnmpTrapCom_Object = MibScalar
fnSysSnmpTrapCom = _FnSysSnmpTrapCom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 6),
    _FnSysSnmpTrapCom_Type()
)
fnSysSnmpTrapCom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpTrapCom.setStatus("mandatory")
_FnSysSnmp1stTrapIp_Type = IpAddress
_FnSysSnmp1stTrapIp_Object = MibScalar
fnSysSnmp1stTrapIp = _FnSysSnmp1stTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 7),
    _FnSysSnmp1stTrapIp_Type()
)
fnSysSnmp1stTrapIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmp1stTrapIp.setStatus("mandatory")
_FnSysSnmp2ndTrapIp_Type = IpAddress
_FnSysSnmp2ndTrapIp_Object = MibScalar
fnSysSnmp2ndTrapIp = _FnSysSnmp2ndTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 8),
    _FnSysSnmp2ndTrapIp_Type()
)
fnSysSnmp2ndTrapIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmp2ndTrapIp.setStatus("mandatory")
_FnSysSnmp3rdTrapIp_Type = IpAddress
_FnSysSnmp3rdTrapIp_Object = MibScalar
fnSysSnmp3rdTrapIp = _FnSysSnmp3rdTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 1, 9),
    _FnSysSnmp3rdTrapIp_Type()
)
fnSysSnmp3rdTrapIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmp3rdTrapIp.setStatus("mandatory")
_FnSysSnmpv3AccCtrl_ObjectIdentity = ObjectIdentity
fnSysSnmpv3AccCtrl = _FnSysSnmpv3AccCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2)
)
_FnSysSnmpv3ACState_Type = ItemState
_FnSysSnmpv3ACState_Object = MibScalar
fnSysSnmpv3ACState = _FnSysSnmpv3ACState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 1),
    _FnSysSnmpv3ACState_Type()
)
fnSysSnmpv3ACState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpv3ACState.setStatus("mandatory")
_FnSysSnmpv3ACTable_Object = MibTable
fnSysSnmpv3ACTable = _FnSysSnmpv3ACTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    fnSysSnmpv3ACTable.setStatus("mandatory")
_FnSysSnmpv3ACEntry_Object = MibTableRow
fnSysSnmpv3ACEntry = _FnSysSnmpv3ACEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1)
)
fnSysSnmpv3ACEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysSnmpACIndex"),
)
if mibBuilder.loadTexts:
    fnSysSnmpv3ACEntry.setStatus("mandatory")


class _FnSysSnmpACIndex_Type(Integer32):
    """Custom type fnSysSnmpACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysSnmpACIndex_Type.__name__ = "Integer32"
_FnSysSnmpACIndex_Object = MibTableColumn
fnSysSnmpACIndex = _FnSysSnmpACIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 1),
    _FnSysSnmpACIndex_Type()
)
fnSysSnmpACIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysSnmpACIndex.setStatus("mandatory")
_FnSysSnmpACGrpName_Type = DisplayString
_FnSysSnmpACGrpName_Object = MibTableColumn
fnSysSnmpACGrpName = _FnSysSnmpACGrpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 2),
    _FnSysSnmpACGrpName_Type()
)
fnSysSnmpACGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACGrpName.setStatus("mandatory")
_FnSysSnmpACSecLevelAuth_Type = ItemState
_FnSysSnmpACSecLevelAuth_Object = MibTableColumn
fnSysSnmpACSecLevelAuth = _FnSysSnmpACSecLevelAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 3),
    _FnSysSnmpACSecLevelAuth_Type()
)
fnSysSnmpACSecLevelAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACSecLevelAuth.setStatus("mandatory")
_FnSysSnmpACSecLevelPriv_Type = ItemState
_FnSysSnmpACSecLevelPriv_Object = MibTableColumn
fnSysSnmpACSecLevelPriv = _FnSysSnmpACSecLevelPriv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 4),
    _FnSysSnmpACSecLevelPriv_Type()
)
fnSysSnmpACSecLevelPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACSecLevelPriv.setStatus("mandatory")
_FnSysSnmpACContexPre_Type = DisplayString
_FnSysSnmpACContexPre_Object = MibTableColumn
fnSysSnmpACContexPre = _FnSysSnmpACContexPre_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 5),
    _FnSysSnmpACContexPre_Type()
)
fnSysSnmpACContexPre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACContexPre.setStatus("mandatory")


class _FnSysSnmpACContextMatch_Type(Integer32):
    """Custom type fnSysSnmpACContextMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exact", 1)
    )


_FnSysSnmpACContextMatch_Type.__name__ = "Integer32"
_FnSysSnmpACContextMatch_Object = MibTableColumn
fnSysSnmpACContextMatch = _FnSysSnmpACContextMatch_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 6),
    _FnSysSnmpACContextMatch_Type()
)
fnSysSnmpACContextMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACContextMatch.setStatus("mandatory")
_FnSysSnmpACRv_Type = DisplayString
_FnSysSnmpACRv_Object = MibTableColumn
fnSysSnmpACRv = _FnSysSnmpACRv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 7),
    _FnSysSnmpACRv_Type()
)
fnSysSnmpACRv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACRv.setStatus("mandatory")
_FnSysSnmpACWv_Type = DisplayString
_FnSysSnmpACWv_Object = MibTableColumn
fnSysSnmpACWv = _FnSysSnmpACWv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 8),
    _FnSysSnmpACWv_Type()
)
fnSysSnmpACWv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACWv.setStatus("mandatory")
_FnSysSnmpACNv_Type = DisplayString
_FnSysSnmpACNv_Object = MibTableColumn
fnSysSnmpACNv = _FnSysSnmpACNv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 2, 2, 1, 9),
    _FnSysSnmpACNv_Type()
)
fnSysSnmpACNv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpACNv.setStatus("mandatory")
_FnSysSnmpSecurity_ObjectIdentity = ObjectIdentity
fnSysSnmpSecurity = _FnSysSnmpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3)
)
_FnSysSnmpSecUserTable_Object = MibTable
fnSysSnmpSecUserTable = _FnSysSnmpSecUserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    fnSysSnmpSecUserTable.setStatus("mandatory")
_FnSysSnmpSecUserEntry_Object = MibTableRow
fnSysSnmpSecUserEntry = _FnSysSnmpSecUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1, 1)
)
fnSysSnmpSecUserEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysSnmpSecUserName"),
)
if mibBuilder.loadTexts:
    fnSysSnmpSecUserEntry.setStatus("mandatory")


class _FnSysSnmpSecUserName_Type(DisplayString):
    """Custom type fnSysSnmpSecUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnSysSnmpSecUserName_Type.__name__ = "DisplayString"
_FnSysSnmpSecUserName_Object = MibTableColumn
fnSysSnmpSecUserName = _FnSysSnmpSecUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1, 1, 1),
    _FnSysSnmpSecUserName_Type()
)
fnSysSnmpSecUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysSnmpSecUserName.setStatus("mandatory")
_FnSysSnmpSecUserSecLevelAuth_Type = ItemState
_FnSysSnmpSecUserSecLevelAuth_Object = MibTableColumn
fnSysSnmpSecUserSecLevelAuth = _FnSysSnmpSecUserSecLevelAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1, 1, 2),
    _FnSysSnmpSecUserSecLevelAuth_Type()
)
fnSysSnmpSecUserSecLevelAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSecUserSecLevelAuth.setStatus("mandatory")
_FnSysSnmpSecUserSecLevelPriv_Type = ItemState
_FnSysSnmpSecUserSecLevelPriv_Object = MibTableColumn
fnSysSnmpSecUserSecLevelPriv = _FnSysSnmpSecUserSecLevelPriv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1, 1, 3),
    _FnSysSnmpSecUserSecLevelPriv_Type()
)
fnSysSnmpSecUserSecLevelPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSecUserSecLevelPriv.setStatus("mandatory")
_FnSysSnmpSecUserAuthPasswd_Type = OctetString
_FnSysSnmpSecUserAuthPasswd_Object = MibTableColumn
fnSysSnmpSecUserAuthPasswd = _FnSysSnmpSecUserAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1, 1, 4),
    _FnSysSnmpSecUserAuthPasswd_Type()
)
fnSysSnmpSecUserAuthPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSecUserAuthPasswd.setStatus("mandatory")


class _FnSysSnmpSecUserAuthProto_Type(Integer32):
    """Custom type fnSysSnmpSecUserAuthProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmac-md5-96", 1),
          ("hmac-sha-96", 2))
    )


_FnSysSnmpSecUserAuthProto_Type.__name__ = "Integer32"
_FnSysSnmpSecUserAuthProto_Object = MibTableColumn
fnSysSnmpSecUserAuthProto = _FnSysSnmpSecUserAuthProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1, 1, 5),
    _FnSysSnmpSecUserAuthProto_Type()
)
fnSysSnmpSecUserAuthProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSecUserAuthProto.setStatus("mandatory")
_FnSysSnmpSecUserPrivPasswd_Type = OctetString
_FnSysSnmpSecUserPrivPasswd_Object = MibTableColumn
fnSysSnmpSecUserPrivPasswd = _FnSysSnmpSecUserPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 1, 1, 6),
    _FnSysSnmpSecUserPrivPasswd_Type()
)
fnSysSnmpSecUserPrivPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSecUserPrivPasswd.setStatus("mandatory")
_FnSysSnmpSecGrpTable_Object = MibTable
fnSysSnmpSecGrpTable = _FnSysSnmpSecGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    fnSysSnmpSecGrpTable.setStatus("mandatory")
_FnSysSnmpSecGrpEntry_Object = MibTableRow
fnSysSnmpSecGrpEntry = _FnSysSnmpSecGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 2, 1)
)
fnSysSnmpSecGrpEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysSnmpSecGrpName"),
)
if mibBuilder.loadTexts:
    fnSysSnmpSecGrpEntry.setStatus("mandatory")


class _FnSysSnmpSecGrpName_Type(DisplayString):
    """Custom type fnSysSnmpSecGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnSysSnmpSecGrpName_Type.__name__ = "DisplayString"
_FnSysSnmpSecGrpName_Object = MibTableColumn
fnSysSnmpSecGrpName = _FnSysSnmpSecGrpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 2, 1, 1),
    _FnSysSnmpSecGrpName_Type()
)
fnSysSnmpSecGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysSnmpSecGrpName.setStatus("mandatory")
_FnSysSnmpSecGrpMembers_Type = Integer32
_FnSysSnmpSecGrpMembers_Object = MibTableColumn
fnSysSnmpSecGrpMembers = _FnSysSnmpSecGrpMembers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 3, 2, 1, 2),
    _FnSysSnmpSecGrpMembers_Type()
)
fnSysSnmpSecGrpMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpSecGrpMembers.setStatus("mandatory")
_FnSysSnmpViewTable_Object = MibTable
fnSysSnmpViewTable = _FnSysSnmpViewTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 4)
)
if mibBuilder.loadTexts:
    fnSysSnmpViewTable.setStatus("mandatory")
_FnSysSnmpViewEntry_Object = MibTableRow
fnSysSnmpViewEntry = _FnSysSnmpViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 4, 1)
)
fnSysSnmpViewEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnSysSnmpViewName"),
)
if mibBuilder.loadTexts:
    fnSysSnmpViewEntry.setStatus("mandatory")


class _FnSysSnmpViewName_Type(Integer32):
    """Custom type fnSysSnmpViewName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnSysSnmpViewName_Type.__name__ = "Integer32"
_FnSysSnmpViewName_Object = MibTableColumn
fnSysSnmpViewName = _FnSysSnmpViewName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 4, 1, 1),
    _FnSysSnmpViewName_Type()
)
fnSysSnmpViewName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnSysSnmpViewName.setStatus("mandatory")
_FnSysSnmpViewSubtreeOid_Type = DisplayString
_FnSysSnmpViewSubtreeOid_Object = MibTableColumn
fnSysSnmpViewSubtreeOid = _FnSysSnmpViewSubtreeOid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 4, 1, 2),
    _FnSysSnmpViewSubtreeOid_Type()
)
fnSysSnmpViewSubtreeOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpViewSubtreeOid.setStatus("mandatory")
_FnSysSnmpViewMask_Type = Integer32
_FnSysSnmpViewMask_Object = MibTableColumn
fnSysSnmpViewMask = _FnSysSnmpViewMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 4, 1, 3),
    _FnSysSnmpViewMask_Type()
)
fnSysSnmpViewMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpViewMask.setStatus("mandatory")


class _FnSysSnmpViewType_Type(Integer32):
    """Custom type fnSysSnmpViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 2),
          ("included", 1))
    )


_FnSysSnmpViewType_Type.__name__ = "Integer32"
_FnSysSnmpViewType_Object = MibTableColumn
fnSysSnmpViewType = _FnSysSnmpViewType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5, 4, 1, 4),
    _FnSysSnmpViewType_Type()
)
fnSysSnmpViewType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSnmpViewType.setStatus("mandatory")
_FnFirewall_ObjectIdentity = ObjectIdentity
fnFirewall = _FnFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2)
)
_FnFirewallPolicy_ObjectIdentity = ObjectIdentity
fnFirewallPolicy = _FnFirewallPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1)
)
_FnFirewallPolicyTable_Object = MibTable
fnFirewallPolicyTable = _FnFirewallPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fnFirewallPolicyTable.setStatus("mandatory")
_FnFirewallPolicyEntry_Object = MibTableRow
fnFirewallPolicyEntry = _FnFirewallPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1)
)
fnFirewallPolicyEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallPolicyIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallPolicyEntry.setStatus("mandatory")


class _FnFirewallPolicyIndex_Type(Integer32):
    """Custom type fnFirewallPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallPolicyIndex_Type.__name__ = "Integer32"
_FnFirewallPolicyIndex_Object = MibTableColumn
fnFirewallPolicyIndex = _FnFirewallPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 1),
    _FnFirewallPolicyIndex_Type()
)
fnFirewallPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyIndex.setStatus("mandatory")


class _FnFirewallPolicySrcZone_Type(DisplayString):
    """Custom type fnFirewallPolicySrcZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicySrcZone_Type.__name__ = "DisplayString"
_FnFirewallPolicySrcZone_Object = MibTableColumn
fnFirewallPolicySrcZone = _FnFirewallPolicySrcZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 2),
    _FnFirewallPolicySrcZone_Type()
)
fnFirewallPolicySrcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicySrcZone.setStatus("mandatory")


class _FnFirewallPolicyDestZone_Type(DisplayString):
    """Custom type fnFirewallPolicyDestZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicyDestZone_Type.__name__ = "DisplayString"
_FnFirewallPolicyDestZone_Object = MibTableColumn
fnFirewallPolicyDestZone = _FnFirewallPolicyDestZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 3),
    _FnFirewallPolicyDestZone_Type()
)
fnFirewallPolicyDestZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyDestZone.setStatus("mandatory")


class _FnFirewallPolicySrcAddr_Type(DisplayString):
    """Custom type fnFirewallPolicySrcAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicySrcAddr_Type.__name__ = "DisplayString"
_FnFirewallPolicySrcAddr_Object = MibTableColumn
fnFirewallPolicySrcAddr = _FnFirewallPolicySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 4),
    _FnFirewallPolicySrcAddr_Type()
)
fnFirewallPolicySrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicySrcAddr.setStatus("mandatory")


class _FnFirewallPolicyDestAddr_Type(DisplayString):
    """Custom type fnFirewallPolicyDestAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicyDestAddr_Type.__name__ = "DisplayString"
_FnFirewallPolicyDestAddr_Object = MibTableColumn
fnFirewallPolicyDestAddr = _FnFirewallPolicyDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 5),
    _FnFirewallPolicyDestAddr_Type()
)
fnFirewallPolicyDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyDestAddr.setStatus("mandatory")


class _FnFirewallPolicySchedule_Type(DisplayString):
    """Custom type fnFirewallPolicySchedule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicySchedule_Type.__name__ = "DisplayString"
_FnFirewallPolicySchedule_Object = MibTableColumn
fnFirewallPolicySchedule = _FnFirewallPolicySchedule_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 6),
    _FnFirewallPolicySchedule_Type()
)
fnFirewallPolicySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicySchedule.setStatus("mandatory")


class _FnFirewallPolicyService_Type(DisplayString):
    """Custom type fnFirewallPolicyService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicyService_Type.__name__ = "DisplayString"
_FnFirewallPolicyService_Object = MibTableColumn
fnFirewallPolicyService = _FnFirewallPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 7),
    _FnFirewallPolicyService_Type()
)
fnFirewallPolicyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyService.setStatus("mandatory")


class _FnFirewallPolicyAction_Type(DisplayString):
    """Custom type fnFirewallPolicyAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicyAction_Type.__name__ = "DisplayString"
_FnFirewallPolicyAction_Object = MibTableColumn
fnFirewallPolicyAction = _FnFirewallPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 8),
    _FnFirewallPolicyAction_Type()
)
fnFirewallPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyAction.setStatus("mandatory")


class _FnFirewallPolicyNAT_Type(Integer32):
    """Custom type fnFirewallPolicyNAT based on Integer32"""
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


_FnFirewallPolicyNAT_Type.__name__ = "Integer32"
_FnFirewallPolicyNAT_Object = MibTableColumn
fnFirewallPolicyNAT = _FnFirewallPolicyNAT_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 9),
    _FnFirewallPolicyNAT_Type()
)
fnFirewallPolicyNAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyNAT.setStatus("mandatory")


class _FnFirewallPolicyDipPool_Type(Integer32):
    """Custom type fnFirewallPolicyDipPool based on Integer32"""
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


_FnFirewallPolicyDipPool_Type.__name__ = "Integer32"
_FnFirewallPolicyDipPool_Object = MibTableColumn
fnFirewallPolicyDipPool = _FnFirewallPolicyDipPool_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 10),
    _FnFirewallPolicyDipPool_Type()
)
fnFirewallPolicyDipPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyDipPool.setStatus("mandatory")


class _FnFirewallPolicyFixPort_Type(Integer32):
    """Custom type fnFirewallPolicyFixPort based on Integer32"""
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


_FnFirewallPolicyFixPort_Type.__name__ = "Integer32"
_FnFirewallPolicyFixPort_Object = MibTableColumn
fnFirewallPolicyFixPort = _FnFirewallPolicyFixPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 11),
    _FnFirewallPolicyFixPort_Type()
)
fnFirewallPolicyFixPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyFixPort.setStatus("mandatory")


class _FnFirewallPolicyAuth_Type(Integer32):
    """Custom type fnFirewallPolicyAuth based on Integer32"""
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


_FnFirewallPolicyAuth_Type.__name__ = "Integer32"
_FnFirewallPolicyAuth_Object = MibTableColumn
fnFirewallPolicyAuth = _FnFirewallPolicyAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 12),
    _FnFirewallPolicyAuth_Type()
)
fnFirewallPolicyAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyAuth.setStatus("mandatory")


class _FnFirewallPolicyVpnTunName_Type(DisplayString):
    """Custom type fnFirewallPolicyVpnTunName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallPolicyVpnTunName_Type.__name__ = "DisplayString"
_FnFirewallPolicyVpnTunName_Object = MibTableColumn
fnFirewallPolicyVpnTunName = _FnFirewallPolicyVpnTunName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 13),
    _FnFirewallPolicyVpnTunName_Type()
)
fnFirewallPolicyVpnTunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyVpnTunName.setStatus("mandatory")


class _FnFirewallPolicyVpnAllowIn_Type(Integer32):
    """Custom type fnFirewallPolicyVpnAllowIn based on Integer32"""
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


_FnFirewallPolicyVpnAllowIn_Type.__name__ = "Integer32"
_FnFirewallPolicyVpnAllowIn_Object = MibTableColumn
fnFirewallPolicyVpnAllowIn = _FnFirewallPolicyVpnAllowIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 14),
    _FnFirewallPolicyVpnAllowIn_Type()
)
fnFirewallPolicyVpnAllowIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyVpnAllowIn.setStatus("mandatory")


class _FnFirewallPolicyVpnAllowOut_Type(Integer32):
    """Custom type fnFirewallPolicyVpnAllowOut based on Integer32"""
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


_FnFirewallPolicyVpnAllowOut_Type.__name__ = "Integer32"
_FnFirewallPolicyVpnAllowOut_Object = MibTableColumn
fnFirewallPolicyVpnAllowOut = _FnFirewallPolicyVpnAllowOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 15),
    _FnFirewallPolicyVpnAllowOut_Type()
)
fnFirewallPolicyVpnAllowOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyVpnAllowOut.setStatus("mandatory")


class _FnFirewallPolicyVpnInNat_Type(Integer32):
    """Custom type fnFirewallPolicyVpnInNat based on Integer32"""
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


_FnFirewallPolicyVpnInNat_Type.__name__ = "Integer32"
_FnFirewallPolicyVpnInNat_Object = MibTableColumn
fnFirewallPolicyVpnInNat = _FnFirewallPolicyVpnInNat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 16),
    _FnFirewallPolicyVpnInNat_Type()
)
fnFirewallPolicyVpnInNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyVpnInNat.setStatus("mandatory")


class _FnFirewallPolicyVpnOutNat_Type(Integer32):
    """Custom type fnFirewallPolicyVpnOutNat based on Integer32"""
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


_FnFirewallPolicyVpnOutNat_Type.__name__ = "Integer32"
_FnFirewallPolicyVpnOutNat_Object = MibTableColumn
fnFirewallPolicyVpnOutNat = _FnFirewallPolicyVpnOutNat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 17),
    _FnFirewallPolicyVpnOutNat_Type()
)
fnFirewallPolicyVpnOutNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyVpnOutNat.setStatus("mandatory")


class _FnFirewallPolicyLog_Type(Integer32):
    """Custom type fnFirewallPolicyLog based on Integer32"""
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


_FnFirewallPolicyLog_Type.__name__ = "Integer32"
_FnFirewallPolicyLog_Object = MibTableColumn
fnFirewallPolicyLog = _FnFirewallPolicyLog_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 18),
    _FnFirewallPolicyLog_Type()
)
fnFirewallPolicyLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyLog.setStatus("mandatory")


class _FnFirewallPolicyAV_Type(Integer32):
    """Custom type fnFirewallPolicyAV based on Integer32"""
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


_FnFirewallPolicyAV_Type.__name__ = "Integer32"
_FnFirewallPolicyAV_Object = MibTableColumn
fnFirewallPolicyAV = _FnFirewallPolicyAV_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 19),
    _FnFirewallPolicyAV_Type()
)
fnFirewallPolicyAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyAV.setStatus("mandatory")
_FnFirewallPolicyGBand_Type = Integer32
_FnFirewallPolicyGBand_Object = MibTableColumn
fnFirewallPolicyGBand = _FnFirewallPolicyGBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 20),
    _FnFirewallPolicyGBand_Type()
)
fnFirewallPolicyGBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyGBand.setStatus("mandatory")
_FnFirewallPolicyMBand_Type = Integer32
_FnFirewallPolicyMBand_Object = MibTableColumn
fnFirewallPolicyMBand = _FnFirewallPolicyMBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 21),
    _FnFirewallPolicyMBand_Type()
)
fnFirewallPolicyMBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyMBand.setStatus("mandatory")


class _FnFirewallPolicyTrafficPri_Type(Integer32):
    """Custom type fnFirewallPolicyTrafficPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_FnFirewallPolicyTrafficPri_Type.__name__ = "Integer32"
_FnFirewallPolicyTrafficPri_Object = MibTableColumn
fnFirewallPolicyTrafficPri = _FnFirewallPolicyTrafficPri_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 22),
    _FnFirewallPolicyTrafficPri_Type()
)
fnFirewallPolicyTrafficPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyTrafficPri.setStatus("mandatory")
_FnFirewallPolicyProf_Type = DisplayString
_FnFirewallPolicyProf_Object = MibTableColumn
fnFirewallPolicyProf = _FnFirewallPolicyProf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1, 1, 1, 23),
    _FnFirewallPolicyProf_Type()
)
fnFirewallPolicyProf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallPolicyProf.setStatus("mandatory")
_FnFirewallAddress_ObjectIdentity = ObjectIdentity
fnFirewallAddress = _FnFirewallAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2)
)
_FnFirewallAddrTable_Object = MibTable
fnFirewallAddrTable = _FnFirewallAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fnFirewallAddrTable.setStatus("mandatory")
_FnFirewallAddrEntry_Object = MibTableRow
fnFirewallAddrEntry = _FnFirewallAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1)
)
fnFirewallAddrEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallAddrName"),
)
if mibBuilder.loadTexts:
    fnFirewallAddrEntry.setStatus("mandatory")


class _FnFirewallAddrName_Type(DisplayString):
    """Custom type fnFirewallAddrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallAddrName_Type.__name__ = "DisplayString"
_FnFirewallAddrName_Object = MibTableColumn
fnFirewallAddrName = _FnFirewallAddrName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1, 1),
    _FnFirewallAddrName_Type()
)
fnFirewallAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallAddrName.setStatus("mandatory")
_FnFirewallAddrIp_Type = IpAddress
_FnFirewallAddrIp_Object = MibTableColumn
fnFirewallAddrIp = _FnFirewallAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1, 2),
    _FnFirewallAddrIp_Type()
)
fnFirewallAddrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallAddrIp.setStatus("mandatory")
_FnFirewallAddressNetmask_Type = IpAddress
_FnFirewallAddressNetmask_Object = MibTableColumn
fnFirewallAddressNetmask = _FnFirewallAddressNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1, 3),
    _FnFirewallAddressNetmask_Type()
)
fnFirewallAddressNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallAddressNetmask.setStatus("mandatory")


class _FnFirewallAddrZone_Type(DisplayString):
    """Custom type fnFirewallAddrZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallAddrZone_Type.__name__ = "DisplayString"
_FnFirewallAddrZone_Object = MibTableColumn
fnFirewallAddrZone = _FnFirewallAddrZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1, 4),
    _FnFirewallAddrZone_Type()
)
fnFirewallAddrZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallAddrZone.setStatus("mandatory")


class _FnFirewallAddrVlanId_Type(Integer32):
    """Custom type fnFirewallAddrVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnFirewallAddrVlanId_Type.__name__ = "Integer32"
_FnFirewallAddrVlanId_Object = MibTableColumn
fnFirewallAddrVlanId = _FnFirewallAddrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1, 5),
    _FnFirewallAddrVlanId_Type()
)
fnFirewallAddrVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallAddrVlanId.setStatus("mandatory")
_FnFirewallAddrGrpTable_Object = MibTable
fnFirewallAddrGrpTable = _FnFirewallAddrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fnFirewallAddrGrpTable.setStatus("mandatory")
_FnFirewallAddrGrpEntry_Object = MibTableRow
fnFirewallAddrGrpEntry = _FnFirewallAddrGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 2, 1)
)
fnFirewallAddrGrpEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallAddrGrpIndex"),
    (0, "FORTINET-MIB", "fnFirewallAddrGrpZone"),
    (0, "FORTINET-MIB", "fnFirewallAddrGrpName"),
)
if mibBuilder.loadTexts:
    fnFirewallAddrGrpEntry.setStatus("mandatory")


class _FnFirewallAddrGrpIndex_Type(Integer32):
    """Custom type fnFirewallAddrGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallAddrGrpIndex_Type.__name__ = "Integer32"
_FnFirewallAddrGrpIndex_Object = MibTableColumn
fnFirewallAddrGrpIndex = _FnFirewallAddrGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 2, 1, 1),
    _FnFirewallAddrGrpIndex_Type()
)
fnFirewallAddrGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnFirewallAddrGrpIndex.setStatus("mandatory")


class _FnFirewallAddrGrpZone_Type(DisplayString):
    """Custom type fnFirewallAddrGrpZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallAddrGrpZone_Type.__name__ = "DisplayString"
_FnFirewallAddrGrpZone_Object = MibTableColumn
fnFirewallAddrGrpZone = _FnFirewallAddrGrpZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 2, 1, 2),
    _FnFirewallAddrGrpZone_Type()
)
fnFirewallAddrGrpZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallAddrGrpZone.setStatus("mandatory")


class _FnFirewallAddrGrpName_Type(DisplayString):
    """Custom type fnFirewallAddrGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallAddrGrpName_Type.__name__ = "DisplayString"
_FnFirewallAddrGrpName_Object = MibTableColumn
fnFirewallAddrGrpName = _FnFirewallAddrGrpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 2, 1, 3),
    _FnFirewallAddrGrpName_Type()
)
fnFirewallAddrGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnFirewallAddrGrpName.setStatus("mandatory")


class _FnFirewallAddrGrpMems_Type(DisplayString):
    """Custom type fnFirewallAddrGrpMems based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25555),
    )


_FnFirewallAddrGrpMems_Type.__name__ = "DisplayString"
_FnFirewallAddrGrpMems_Object = MibTableColumn
fnFirewallAddrGrpMems = _FnFirewallAddrGrpMems_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 2, 1, 4),
    _FnFirewallAddrGrpMems_Type()
)
fnFirewallAddrGrpMems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallAddrGrpMems.setStatus("mandatory")
_FnFirewallService_ObjectIdentity = ObjectIdentity
fnFirewallService = _FnFirewallService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3)
)
_FnFirewallServiceTable_Object = MibTable
fnFirewallServiceTable = _FnFirewallServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fnFirewallServiceTable.setStatus("mandatory")
_FnFirewallServiceEntry_Object = MibTableRow
fnFirewallServiceEntry = _FnFirewallServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1)
)
fnFirewallServiceEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallServiceIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallServiceEntry.setStatus("mandatory")


class _FnFirewallServiceIndex_Type(Integer32):
    """Custom type fnFirewallServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallServiceIndex_Type.__name__ = "Integer32"
_FnFirewallServiceIndex_Object = MibTableColumn
fnFirewallServiceIndex = _FnFirewallServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 1),
    _FnFirewallServiceIndex_Type()
)
fnFirewallServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceIndex.setStatus("mandatory")


class _FnFirewallServiceName_Type(DisplayString):
    """Custom type fnFirewallServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallServiceName_Type.__name__ = "DisplayString"
_FnFirewallServiceName_Object = MibTableColumn
fnFirewallServiceName = _FnFirewallServiceName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 2),
    _FnFirewallServiceName_Type()
)
fnFirewallServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceName.setStatus("mandatory")


class _FnFirewallServiceProto_Type(Integer32):
    """Custom type fnFirewallServiceProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_FnFirewallServiceProto_Type.__name__ = "Integer32"
_FnFirewallServiceProto_Object = MibTableColumn
fnFirewallServiceProto = _FnFirewallServiceProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 3),
    _FnFirewallServiceProto_Type()
)
fnFirewallServiceProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceProto.setStatus("mandatory")


class _FnFirewallServiceUsed_Type(Integer32):
    """Custom type fnFirewallServiceUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 2),
          ("used", 1))
    )


_FnFirewallServiceUsed_Type.__name__ = "Integer32"
_FnFirewallServiceUsed_Object = MibTableColumn
fnFirewallServiceUsed = _FnFirewallServiceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 4),
    _FnFirewallServiceUsed_Type()
)
fnFirewallServiceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceUsed.setStatus("mandatory")


class _FnFirewallServiceSrcPortLow_Type(Integer32):
    """Custom type fnFirewallServiceSrcPortLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FnFirewallServiceSrcPortLow_Type.__name__ = "Integer32"
_FnFirewallServiceSrcPortLow_Object = MibTableColumn
fnFirewallServiceSrcPortLow = _FnFirewallServiceSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 5),
    _FnFirewallServiceSrcPortLow_Type()
)
fnFirewallServiceSrcPortLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceSrcPortLow.setStatus("mandatory")


class _FnFirewallServiceSrcPortHigh_Type(Integer32):
    """Custom type fnFirewallServiceSrcPortHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FnFirewallServiceSrcPortHigh_Type.__name__ = "Integer32"
_FnFirewallServiceSrcPortHigh_Object = MibTableColumn
fnFirewallServiceSrcPortHigh = _FnFirewallServiceSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 6),
    _FnFirewallServiceSrcPortHigh_Type()
)
fnFirewallServiceSrcPortHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceSrcPortHigh.setStatus("mandatory")


class _FnFirewallServiceDstPortLow_Type(Integer32):
    """Custom type fnFirewallServiceDstPortLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FnFirewallServiceDstPortLow_Type.__name__ = "Integer32"
_FnFirewallServiceDstPortLow_Object = MibTableColumn
fnFirewallServiceDstPortLow = _FnFirewallServiceDstPortLow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 7),
    _FnFirewallServiceDstPortLow_Type()
)
fnFirewallServiceDstPortLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceDstPortLow.setStatus("mandatory")


class _FnFirewallServiceDstPortHigh_Type(Integer32):
    """Custom type fnFirewallServiceDstPortHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FnFirewallServiceDstPortHigh_Type.__name__ = "Integer32"
_FnFirewallServiceDstPortHigh_Object = MibTableColumn
fnFirewallServiceDstPortHigh = _FnFirewallServiceDstPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 8),
    _FnFirewallServiceDstPortHigh_Type()
)
fnFirewallServiceDstPortHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceDstPortHigh.setStatus("mandatory")


class _FnFirewallServiceType_Type(Integer32):
    """Custom type fnFirewallServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("predefined", 1))
    )


_FnFirewallServiceType_Type.__name__ = "Integer32"
_FnFirewallServiceType_Object = MibTableColumn
fnFirewallServiceType = _FnFirewallServiceType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 1, 1, 9),
    _FnFirewallServiceType_Type()
)
fnFirewallServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceType.setStatus("mandatory")
_FnFirewallServiceGroupTable_Object = MibTable
fnFirewallServiceGroupTable = _FnFirewallServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fnFirewallServiceGroupTable.setStatus("mandatory")
_FnFirewallServiceGroupEntry_Object = MibTableRow
fnFirewallServiceGroupEntry = _FnFirewallServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 2, 1)
)
fnFirewallServiceGroupEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallServiceGroupIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallServiceGroupEntry.setStatus("mandatory")


class _FnFirewallServiceGroupIndex_Type(Integer32):
    """Custom type fnFirewallServiceGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallServiceGroupIndex_Type.__name__ = "Integer32"
_FnFirewallServiceGroupIndex_Object = MibTableColumn
fnFirewallServiceGroupIndex = _FnFirewallServiceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 2, 1, 1),
    _FnFirewallServiceGroupIndex_Type()
)
fnFirewallServiceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceGroupIndex.setStatus("mandatory")


class _FnFirewallServiceGroupName_Type(DisplayString):
    """Custom type fnFirewallServiceGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallServiceGroupName_Type.__name__ = "DisplayString"
_FnFirewallServiceGroupName_Object = MibTableColumn
fnFirewallServiceGroupName = _FnFirewallServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 2, 1, 2),
    _FnFirewallServiceGroupName_Type()
)
fnFirewallServiceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceGroupName.setStatus("mandatory")


class _FnFirewallServiceGroupValue_Type(DisplayString):
    """Custom type fnFirewallServiceGroupValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnFirewallServiceGroupValue_Type.__name__ = "DisplayString"
_FnFirewallServiceGroupValue_Object = MibTableColumn
fnFirewallServiceGroupValue = _FnFirewallServiceGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 2, 1, 3),
    _FnFirewallServiceGroupValue_Type()
)
fnFirewallServiceGroupValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceGroupValue.setStatus("mandatory")


class _FnFirewallServiceGroupUsed_Type(Integer32):
    """Custom type fnFirewallServiceGroupUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 2),
          ("used", 1))
    )


_FnFirewallServiceGroupUsed_Type.__name__ = "Integer32"
_FnFirewallServiceGroupUsed_Object = MibTableColumn
fnFirewallServiceGroupUsed = _FnFirewallServiceGroupUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3, 2, 1, 4),
    _FnFirewallServiceGroupUsed_Type()
)
fnFirewallServiceGroupUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallServiceGroupUsed.setStatus("mandatory")
_FnFirewallSchedule_ObjectIdentity = ObjectIdentity
fnFirewallSchedule = _FnFirewallSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4)
)
_FnFirewallSchOneTable_Object = MibTable
fnFirewallSchOneTable = _FnFirewallSchOneTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fnFirewallSchOneTable.setStatus("mandatory")
_FnFirewallSchOneEntry_Object = MibTableRow
fnFirewallSchOneEntry = _FnFirewallSchOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1)
)
fnFirewallSchOneEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallSchOneIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallSchOneEntry.setStatus("mandatory")


class _FnFirewallSchOneIndex_Type(Integer32):
    """Custom type fnFirewallSchOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallSchOneIndex_Type.__name__ = "Integer32"
_FnFirewallSchOneIndex_Object = MibTableColumn
fnFirewallSchOneIndex = _FnFirewallSchOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1, 1),
    _FnFirewallSchOneIndex_Type()
)
fnFirewallSchOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchOneIndex.setStatus("mandatory")


class _FnFirewallSchOneName_Type(DisplayString):
    """Custom type fnFirewallSchOneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchOneName_Type.__name__ = "DisplayString"
_FnFirewallSchOneName_Object = MibTableColumn
fnFirewallSchOneName = _FnFirewallSchOneName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1, 2),
    _FnFirewallSchOneName_Type()
)
fnFirewallSchOneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchOneName.setStatus("mandatory")


class _FnFirewallSchOneStartDay_Type(DisplayString):
    """Custom type fnFirewallSchOneStartDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchOneStartDay_Type.__name__ = "DisplayString"
_FnFirewallSchOneStartDay_Object = MibTableColumn
fnFirewallSchOneStartDay = _FnFirewallSchOneStartDay_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1, 3),
    _FnFirewallSchOneStartDay_Type()
)
fnFirewallSchOneStartDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchOneStartDay.setStatus("mandatory")


class _FnFirewallSchOneStartTime_Type(DisplayString):
    """Custom type fnFirewallSchOneStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchOneStartTime_Type.__name__ = "DisplayString"
_FnFirewallSchOneStartTime_Object = MibTableColumn
fnFirewallSchOneStartTime = _FnFirewallSchOneStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1, 4),
    _FnFirewallSchOneStartTime_Type()
)
fnFirewallSchOneStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchOneStartTime.setStatus("mandatory")


class _FnFirewallSchOneEndDay_Type(DisplayString):
    """Custom type fnFirewallSchOneEndDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchOneEndDay_Type.__name__ = "DisplayString"
_FnFirewallSchOneEndDay_Object = MibTableColumn
fnFirewallSchOneEndDay = _FnFirewallSchOneEndDay_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1, 5),
    _FnFirewallSchOneEndDay_Type()
)
fnFirewallSchOneEndDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchOneEndDay.setStatus("mandatory")


class _FnFirewallSchOneEndTime_Type(DisplayString):
    """Custom type fnFirewallSchOneEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchOneEndTime_Type.__name__ = "DisplayString"
_FnFirewallSchOneEndTime_Object = MibTableColumn
fnFirewallSchOneEndTime = _FnFirewallSchOneEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1, 6),
    _FnFirewallSchOneEndTime_Type()
)
fnFirewallSchOneEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchOneEndTime.setStatus("mandatory")


class _FnFirewallSchOneUsed_Type(Integer32):
    """Custom type fnFirewallSchOneUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("used", 1))
    )


_FnFirewallSchOneUsed_Type.__name__ = "Integer32"
_FnFirewallSchOneUsed_Object = MibTableColumn
fnFirewallSchOneUsed = _FnFirewallSchOneUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 1, 1, 7),
    _FnFirewallSchOneUsed_Type()
)
fnFirewallSchOneUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchOneUsed.setStatus("mandatory")
_FnFirewallSchRecurTable_Object = MibTable
fnFirewallSchRecurTable = _FnFirewallSchRecurTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fnFirewallSchRecurTable.setStatus("mandatory")
_FnFirewallSchRecurEntry_Object = MibTableRow
fnFirewallSchRecurEntry = _FnFirewallSchRecurEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2, 1)
)
fnFirewallSchRecurEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallSchRecurIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallSchRecurEntry.setStatus("mandatory")


class _FnFirewallSchRecurIndex_Type(Integer32):
    """Custom type fnFirewallSchRecurIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallSchRecurIndex_Type.__name__ = "Integer32"
_FnFirewallSchRecurIndex_Object = MibTableColumn
fnFirewallSchRecurIndex = _FnFirewallSchRecurIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2, 1, 1),
    _FnFirewallSchRecurIndex_Type()
)
fnFirewallSchRecurIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchRecurIndex.setStatus("mandatory")


class _FnFirewallSchRecurName_Type(DisplayString):
    """Custom type fnFirewallSchRecurName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchRecurName_Type.__name__ = "DisplayString"
_FnFirewallSchRecurName_Object = MibTableColumn
fnFirewallSchRecurName = _FnFirewallSchRecurName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2, 1, 2),
    _FnFirewallSchRecurName_Type()
)
fnFirewallSchRecurName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchRecurName.setStatus("mandatory")


class _FnFirewallSchRecurWeekdays_Type(DisplayString):
    """Custom type fnFirewallSchRecurWeekdays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchRecurWeekdays_Type.__name__ = "DisplayString"
_FnFirewallSchRecurWeekdays_Object = MibTableColumn
fnFirewallSchRecurWeekdays = _FnFirewallSchRecurWeekdays_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2, 1, 3),
    _FnFirewallSchRecurWeekdays_Type()
)
fnFirewallSchRecurWeekdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchRecurWeekdays.setStatus("mandatory")


class _FnFirewallSchRecurStartTime_Type(DisplayString):
    """Custom type fnFirewallSchRecurStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchRecurStartTime_Type.__name__ = "DisplayString"
_FnFirewallSchRecurStartTime_Object = MibTableColumn
fnFirewallSchRecurStartTime = _FnFirewallSchRecurStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2, 1, 4),
    _FnFirewallSchRecurStartTime_Type()
)
fnFirewallSchRecurStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchRecurStartTime.setStatus("mandatory")


class _FnFirewallSchRecurEndTime_Type(DisplayString):
    """Custom type fnFirewallSchRecurEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallSchRecurEndTime_Type.__name__ = "DisplayString"
_FnFirewallSchRecurEndTime_Object = MibTableColumn
fnFirewallSchRecurEndTime = _FnFirewallSchRecurEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2, 1, 5),
    _FnFirewallSchRecurEndTime_Type()
)
fnFirewallSchRecurEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchRecurEndTime.setStatus("mandatory")


class _FnFirewallSchRecurUsed_Type(Integer32):
    """Custom type fnFirewallSchRecurUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 2),
          ("used", 1))
    )


_FnFirewallSchRecurUsed_Type.__name__ = "Integer32"
_FnFirewallSchRecurUsed_Object = MibTableColumn
fnFirewallSchRecurUsed = _FnFirewallSchRecurUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4, 2, 1, 6),
    _FnFirewallSchRecurUsed_Type()
)
fnFirewallSchRecurUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallSchRecurUsed.setStatus("mandatory")
_FnFirewallVirtualIP_ObjectIdentity = ObjectIdentity
fnFirewallVirtualIP = _FnFirewallVirtualIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5)
)
_FnFirewallVIPTable_Object = MibTable
fnFirewallVIPTable = _FnFirewallVIPTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1)
)
if mibBuilder.loadTexts:
    fnFirewallVIPTable.setStatus("mandatory")
_FnFirewallVIPEntry_Object = MibTableRow
fnFirewallVIPEntry = _FnFirewallVIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1)
)
fnFirewallVIPEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallVIPIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallVIPEntry.setStatus("mandatory")


class _FnFirewallVIPIndex_Type(Integer32):
    """Custom type fnFirewallVIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallVIPIndex_Type.__name__ = "Integer32"
_FnFirewallVIPIndex_Object = MibTableColumn
fnFirewallVIPIndex = _FnFirewallVIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 1),
    _FnFirewallVIPIndex_Type()
)
fnFirewallVIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPIndex.setStatus("mandatory")


class _FnFirewallVIPName_Type(DisplayString):
    """Custom type fnFirewallVIPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallVIPName_Type.__name__ = "DisplayString"
_FnFirewallVIPName_Object = MibTableColumn
fnFirewallVIPName = _FnFirewallVIPName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 2),
    _FnFirewallVIPName_Type()
)
fnFirewallVIPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPName.setStatus("mandatory")
_FnFirewallVIPExtIf_Type = DisplayString
_FnFirewallVIPExtIf_Object = MibTableColumn
fnFirewallVIPExtIf = _FnFirewallVIPExtIf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 3),
    _FnFirewallVIPExtIf_Type()
)
fnFirewallVIPExtIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPExtIf.setStatus("mandatory")


class _FnFirewallVIPType_Type(Integer32):
    """Custom type fnFirewallVIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portForwarding", 2),
          ("staticNat", 1))
    )


_FnFirewallVIPType_Type.__name__ = "Integer32"
_FnFirewallVIPType_Object = MibTableColumn
fnFirewallVIPType = _FnFirewallVIPType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 4),
    _FnFirewallVIPType_Type()
)
fnFirewallVIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPType.setStatus("mandatory")
_FnFirewallVIPExtIP_Type = IpAddress
_FnFirewallVIPExtIP_Object = MibTableColumn
fnFirewallVIPExtIP = _FnFirewallVIPExtIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 5),
    _FnFirewallVIPExtIP_Type()
)
fnFirewallVIPExtIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPExtIP.setStatus("mandatory")


class _FnFirewallVIPExtPort_Type(Integer32):
    """Custom type fnFirewallVIPExtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FnFirewallVIPExtPort_Type.__name__ = "Integer32"
_FnFirewallVIPExtPort_Object = MibTableColumn
fnFirewallVIPExtPort = _FnFirewallVIPExtPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 6),
    _FnFirewallVIPExtPort_Type()
)
fnFirewallVIPExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPExtPort.setStatus("mandatory")
_FnFirewallVIPMapIP_Type = IpAddress
_FnFirewallVIPMapIP_Object = MibTableColumn
fnFirewallVIPMapIP = _FnFirewallVIPMapIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 7),
    _FnFirewallVIPMapIP_Type()
)
fnFirewallVIPMapIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPMapIP.setStatus("mandatory")


class _FnFirewallVIPMapPort_Type(Integer32):
    """Custom type fnFirewallVIPMapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FnFirewallVIPMapPort_Type.__name__ = "Integer32"
_FnFirewallVIPMapPort_Object = MibTableColumn
fnFirewallVIPMapPort = _FnFirewallVIPMapPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 8),
    _FnFirewallVIPMapPort_Type()
)
fnFirewallVIPMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPMapPort.setStatus("mandatory")


class _FnFirewallVIPProto_Type(Integer32):
    """Custom type fnFirewallVIPProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_FnFirewallVIPProto_Type.__name__ = "Integer32"
_FnFirewallVIPProto_Object = MibTableColumn
fnFirewallVIPProto = _FnFirewallVIPProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 5, 1, 1, 9),
    _FnFirewallVIPProto_Type()
)
fnFirewallVIPProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallVIPProto.setStatus("mandatory")
_FnFirewallIpPool_ObjectIdentity = ObjectIdentity
fnFirewallIpPool = _FnFirewallIpPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 6)
)
_FnFirewallIpPoolTable_Object = MibTable
fnFirewallIpPoolTable = _FnFirewallIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 6, 1)
)
if mibBuilder.loadTexts:
    fnFirewallIpPoolTable.setStatus("mandatory")
_FnFirewallIpPoolEntry_Object = MibTableRow
fnFirewallIpPoolEntry = _FnFirewallIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 6, 1, 1)
)
fnFirewallIpPoolEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallIpPoolIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallIpPoolEntry.setStatus("mandatory")


class _FnFirewallIpPoolIndex_Type(Integer32):
    """Custom type fnFirewallIpPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnFirewallIpPoolIndex_Type.__name__ = "Integer32"
_FnFirewallIpPoolIndex_Object = MibTableColumn
fnFirewallIpPoolIndex = _FnFirewallIpPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 6, 1, 1, 1),
    _FnFirewallIpPoolIndex_Type()
)
fnFirewallIpPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnFirewallIpPoolIndex.setStatus("mandatory")


class _FnFirewallIpPoolIf_Type(DisplayString):
    """Custom type fnFirewallIpPoolIf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnFirewallIpPoolIf_Type.__name__ = "DisplayString"
_FnFirewallIpPoolIf_Object = MibTableColumn
fnFirewallIpPoolIf = _FnFirewallIpPoolIf_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 6, 1, 1, 2),
    _FnFirewallIpPoolIf_Type()
)
fnFirewallIpPoolIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIpPoolIf.setStatus("mandatory")
_FnFirewallIpPoolStartIp_Type = IpAddress
_FnFirewallIpPoolStartIp_Object = MibTableColumn
fnFirewallIpPoolStartIp = _FnFirewallIpPoolStartIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 6, 1, 1, 3),
    _FnFirewallIpPoolStartIp_Type()
)
fnFirewallIpPoolStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIpPoolStartIp.setStatus("mandatory")
_FnFirewallIpPoolEndIp_Type = IpAddress
_FnFirewallIpPoolEndIp_Object = MibTableColumn
fnFirewallIpPoolEndIp = _FnFirewallIpPoolEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 6, 1, 1, 4),
    _FnFirewallIpPoolEndIp_Type()
)
fnFirewallIpPoolEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIpPoolEndIp.setStatus("mandatory")
_FnFirewallIPMACBinding_ObjectIdentity = ObjectIdentity
fnFirewallIPMACBinding = _FnFirewallIPMACBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7)
)
_FnFirewallIPMACBindingTable_Object = MibTable
fnFirewallIPMACBindingTable = _FnFirewallIPMACBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 1)
)
if mibBuilder.loadTexts:
    fnFirewallIPMACBindingTable.setStatus("mandatory")
_FnFirewallIPMACBindingEntry_Object = MibTableRow
fnFirewallIPMACBindingEntry = _FnFirewallIPMACBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 1, 1)
)
fnFirewallIPMACBindingEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFirewallIPMACIndex"),
)
if mibBuilder.loadTexts:
    fnFirewallIPMACBindingEntry.setStatus("mandatory")


class _FnFirewallIPMACIndex_Type(Integer32):
    """Custom type fnFirewallIPMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnFirewallIPMACIndex_Type.__name__ = "Integer32"
_FnFirewallIPMACIndex_Object = MibTableColumn
fnFirewallIPMACIndex = _FnFirewallIPMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 1, 1, 1),
    _FnFirewallIPMACIndex_Type()
)
fnFirewallIPMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACIndex.setStatus("mandatory")


class _FnFirewallIPMACName_Type(DisplayString):
    """Custom type fnFirewallIPMACName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnFirewallIPMACName_Type.__name__ = "DisplayString"
_FnFirewallIPMACName_Object = MibTableColumn
fnFirewallIPMACName = _FnFirewallIPMACName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 1, 1, 2),
    _FnFirewallIPMACName_Type()
)
fnFirewallIPMACName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACName.setStatus("mandatory")
_FnFirewallIPMACIp_Type = IpAddress
_FnFirewallIPMACIp_Object = MibTableColumn
fnFirewallIPMACIp = _FnFirewallIPMACIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 1, 1, 3),
    _FnFirewallIPMACIp_Type()
)
fnFirewallIPMACIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACIp.setStatus("mandatory")


class _FnFirewallIPMACMac_Type(DisplayString):
    """Custom type fnFirewallIPMACMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnFirewallIPMACMac_Type.__name__ = "DisplayString"
_FnFirewallIPMACMac_Object = MibTableColumn
fnFirewallIPMACMac = _FnFirewallIPMACMac_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 1, 1, 4),
    _FnFirewallIPMACMac_Type()
)
fnFirewallIPMACMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACMac.setStatus("mandatory")


class _FnFirewallIPMACState_Type(Integer32):
    """Custom type fnFirewallIPMACState based on Integer32"""
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


_FnFirewallIPMACState_Type.__name__ = "Integer32"
_FnFirewallIPMACState_Object = MibTableColumn
fnFirewallIPMACState = _FnFirewallIPMACState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 1, 1, 5),
    _FnFirewallIPMACState_Type()
)
fnFirewallIPMACState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACState.setStatus("mandatory")


class _FnFirewallIPMACStatus_Type(Integer32):
    """Custom type fnFirewallIPMACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FnFirewallIPMACStatus_Type.__name__ = "Integer32"
_FnFirewallIPMACStatus_Object = MibScalar
fnFirewallIPMACStatus = _FnFirewallIPMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 2),
    _FnFirewallIPMACStatus_Type()
)
fnFirewallIPMACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACStatus.setStatus("mandatory")


class _FnFirewallIPMACAction_Type(Integer32):
    """Custom type fnFirewallIPMACAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("pass", 1))
    )


_FnFirewallIPMACAction_Type.__name__ = "Integer32"
_FnFirewallIPMACAction_Object = MibScalar
fnFirewallIPMACAction = _FnFirewallIPMACAction_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 3),
    _FnFirewallIPMACAction_Type()
)
fnFirewallIPMACAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACAction.setStatus("mandatory")


class _FnFirewallIPMACToFw_Type(Integer32):
    """Custom type fnFirewallIPMACToFw based on Integer32"""
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


_FnFirewallIPMACToFw_Type.__name__ = "Integer32"
_FnFirewallIPMACToFw_Object = MibScalar
fnFirewallIPMACToFw = _FnFirewallIPMACToFw_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 4),
    _FnFirewallIPMACToFw_Type()
)
fnFirewallIPMACToFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACToFw.setStatus("mandatory")


class _FnFirewallIPMACThruFw_Type(Integer32):
    """Custom type fnFirewallIPMACThruFw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_FnFirewallIPMACThruFw_Type.__name__ = "Integer32"
_FnFirewallIPMACThruFw_Object = MibScalar
fnFirewallIPMACThruFw = _FnFirewallIPMACThruFw_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 5),
    _FnFirewallIPMACThruFw_Type()
)
fnFirewallIPMACThruFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACThruFw.setStatus("mandatory")


class _FnFirewallIPMACTraffic_Type(Integer32):
    """Custom type fnFirewallIPMACTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_FnFirewallIPMACTraffic_Type.__name__ = "Integer32"
_FnFirewallIPMACTraffic_Object = MibScalar
fnFirewallIPMACTraffic = _FnFirewallIPMACTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 7, 6),
    _FnFirewallIPMACTraffic_Type()
)
fnFirewallIPMACTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFirewallIPMACTraffic.setStatus("mandatory")
_FnFirewallContProfiles_ObjectIdentity = ObjectIdentity
fnFirewallContProfiles = _FnFirewallContProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8)
)
_FnFwContProfTable_Object = MibTable
fnFwContProfTable = _FnFwContProfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1)
)
if mibBuilder.loadTexts:
    fnFwContProfTable.setStatus("mandatory")
_FnFwContProfEntry_Object = MibTableRow
fnFwContProfEntry = _FnFwContProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1)
)
fnFwContProfEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnFwContProfName"),
)
if mibBuilder.loadTexts:
    fnFwContProfEntry.setStatus("mandatory")


class _FnFwContProfName_Type(DisplayString):
    """Custom type fnFwContProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnFwContProfName_Type.__name__ = "DisplayString"
_FnFwContProfName_Object = MibTableColumn
fnFwContProfName = _FnFwContProfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 1),
    _FnFwContProfName_Type()
)
fnFwContProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnFwContProfName.setStatus("mandatory")
_FnFwContProfAvScan_Type = DisplayString
_FnFwContProfAvScan_Object = MibTableColumn
fnFwContProfAvScan = _FnFwContProfAvScan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 2),
    _FnFwContProfAvScan_Type()
)
fnFwContProfAvScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfAvScan.setStatus("mandatory")


class _FnFwContProfFileBlk_Type(DisplayString):
    """Custom type fnFwContProfFileBlk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnFwContProfFileBlk_Type.__name__ = "DisplayString"
_FnFwContProfFileBlk_Object = MibTableColumn
fnFwContProfFileBlk = _FnFwContProfFileBlk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 3),
    _FnFwContProfFileBlk_Type()
)
fnFwContProfFileBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfFileBlk.setStatus("mandatory")
_FnFwContProfQuarantine_Type = DisplayString
_FnFwContProfQuarantine_Object = MibTableColumn
fnFwContProfQuarantine = _FnFwContProfQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 4),
    _FnFwContProfQuarantine_Type()
)
fnFwContProfQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfQuarantine.setStatus("mandatory")
_FnFwContProfUrlBlkState_Type = ItemState
_FnFwContProfUrlBlkState_Object = MibTableColumn
fnFwContProfUrlBlkState = _FnFwContProfUrlBlkState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 5),
    _FnFwContProfUrlBlkState_Type()
)
fnFwContProfUrlBlkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfUrlBlkState.setStatus("mandatory")
_FnFwContProfBannedWordState_Type = ItemState
_FnFwContProfBannedWordState_Object = MibTableColumn
fnFwContProfBannedWordState = _FnFwContProfBannedWordState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 6),
    _FnFwContProfBannedWordState_Type()
)
fnFwContProfBannedWordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfBannedWordState.setStatus("mandatory")
_FnFwContProfRemvScriptState_Type = ItemState
_FnFwContProfRemvScriptState_Object = MibTableColumn
fnFwContProfRemvScriptState = _FnFwContProfRemvScriptState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 7),
    _FnFwContProfRemvScriptState_Type()
)
fnFwContProfRemvScriptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfRemvScriptState.setStatus("mandatory")
_FnFwContProfExptListState_Type = ItemState
_FnFwContProfExptListState_Object = MibTableColumn
fnFwContProfExptListState = _FnFwContProfExptListState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 8),
    _FnFwContProfExptListState_Type()
)
fnFwContProfExptListState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfExptListState.setStatus("mandatory")
_FnFwContProfSpamFilter_Type = DisplayString
_FnFwContProfSpamFilter_Object = MibTableColumn
fnFwContProfSpamFilter = _FnFwContProfSpamFilter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 9),
    _FnFwContProfSpamFilter_Type()
)
fnFwContProfSpamFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfSpamFilter.setStatus("mandatory")
_FnFwContProfSpamBlkList_Type = DisplayString
_FnFwContProfSpamBlkList_Object = MibTableColumn
fnFwContProfSpamBlkList = _FnFwContProfSpamBlkList_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 10),
    _FnFwContProfSpamBlkList_Type()
)
fnFwContProfSpamBlkList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfSpamBlkList.setStatus("mandatory")
_FnFwContProfSpamExptList_Type = DisplayString
_FnFwContProfSpamExptList_Object = MibTableColumn
fnFwContProfSpamExptList = _FnFwContProfSpamExptList_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 11),
    _FnFwContProfSpamExptList_Type()
)
fnFwContProfSpamExptList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfSpamExptList.setStatus("mandatory")
_FnFwContProfSpamBanWord_Type = DisplayString
_FnFwContProfSpamBanWord_Object = MibTableColumn
fnFwContProfSpamBanWord = _FnFwContProfSpamBanWord_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 12),
    _FnFwContProfSpamBanWord_Type()
)
fnFwContProfSpamBanWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfSpamBanWord.setStatus("mandatory")
_FnFwContProfBigFileBlk_Type = DisplayString
_FnFwContProfBigFileBlk_Object = MibTableColumn
fnFwContProfBigFileBlk = _FnFwContProfBigFileBlk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 13),
    _FnFwContProfBigFileBlk_Type()
)
fnFwContProfBigFileBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfBigFileBlk.setStatus("mandatory")
_FnFwContProfPassFragEmail_Type = DisplayString
_FnFwContProfPassFragEmail_Object = MibTableColumn
fnFwContProfPassFragEmail = _FnFwContProfPassFragEmail_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 8, 1, 1, 14),
    _FnFwContProfPassFragEmail_Type()
)
fnFwContProfPassFragEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwContProfPassFragEmail.setStatus("mandatory")
_FnUser_ObjectIdentity = ObjectIdentity
fnUser = _FnUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 3)
)
_FnUserLocalTable_Object = MibTable
fnUserLocalTable = _FnUserLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1)
)
if mibBuilder.loadTexts:
    fnUserLocalTable.setStatus("mandatory")
_FnUserLocalEntry_Object = MibTableRow
fnUserLocalEntry = _FnUserLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1)
)
fnUserLocalEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnUserLocalIndex"),
)
if mibBuilder.loadTexts:
    fnUserLocalEntry.setStatus("mandatory")


class _FnUserLocalIndex_Type(Integer32):
    """Custom type fnUserLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnUserLocalIndex_Type.__name__ = "Integer32"
_FnUserLocalIndex_Object = MibTableColumn
fnUserLocalIndex = _FnUserLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 1),
    _FnUserLocalIndex_Type()
)
fnUserLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserLocalIndex.setStatus("mandatory")


class _FnUserLocalName_Type(DisplayString):
    """Custom type fnUserLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnUserLocalName_Type.__name__ = "DisplayString"
_FnUserLocalName_Object = MibTableColumn
fnUserLocalName = _FnUserLocalName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 2),
    _FnUserLocalName_Type()
)
fnUserLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserLocalName.setStatus("mandatory")


class _FnUserLocalPasswd_Type(OctetString):
    """Custom type fnUserLocalPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnUserLocalPasswd_Type.__name__ = "OctetString"
_FnUserLocalPasswd_Object = MibTableColumn
fnUserLocalPasswd = _FnUserLocalPasswd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 3),
    _FnUserLocalPasswd_Type()
)
fnUserLocalPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserLocalPasswd.setStatus("mandatory")
_FnUserLocalState_Type = ItemState
_FnUserLocalState_Object = MibTableColumn
fnUserLocalState = _FnUserLocalState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 4),
    _FnUserLocalState_Type()
)
fnUserLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserLocalState.setStatus("mandatory")


class _FnUserLocalType_Type(Integer32):
    """Custom type fnUserLocalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2))
    )


_FnUserLocalType_Type.__name__ = "Integer32"
_FnUserLocalType_Object = MibTableColumn
fnUserLocalType = _FnUserLocalType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 5),
    _FnUserLocalType_Type()
)
fnUserLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserLocalType.setStatus("mandatory")
_FnUserLocalRadiusSrv_Type = DisplayString
_FnUserLocalRadiusSrv_Object = MibTableColumn
fnUserLocalRadiusSrv = _FnUserLocalRadiusSrv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 6),
    _FnUserLocalRadiusSrv_Type()
)
fnUserLocalRadiusSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserLocalRadiusSrv.setStatus("mandatory")
_FnUserLocalRadiusOther_Type = ItemState
_FnUserLocalRadiusOther_Object = MibTableColumn
fnUserLocalRadiusOther = _FnUserLocalRadiusOther_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 7),
    _FnUserLocalRadiusOther_Type()
)
fnUserLocalRadiusOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserLocalRadiusOther.setStatus("mandatory")
_FnUserRadiusSrvTable_Object = MibTable
fnUserRadiusSrvTable = _FnUserRadiusSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 2)
)
if mibBuilder.loadTexts:
    fnUserRadiusSrvTable.setStatus("mandatory")
_FnUserRadiusSrvEntry_Object = MibTableRow
fnUserRadiusSrvEntry = _FnUserRadiusSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 2, 1)
)
fnUserRadiusSrvEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnUserRadIndex"),
)
if mibBuilder.loadTexts:
    fnUserRadiusSrvEntry.setStatus("mandatory")


class _FnUserRadIndex_Type(Integer32):
    """Custom type fnUserRadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnUserRadIndex_Type.__name__ = "Integer32"
_FnUserRadIndex_Object = MibTableColumn
fnUserRadIndex = _FnUserRadIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 2, 1, 1),
    _FnUserRadIndex_Type()
)
fnUserRadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnUserRadIndex.setStatus("mandatory")
_FnUserRadName_Type = DisplayString
_FnUserRadName_Object = MibTableColumn
fnUserRadName = _FnUserRadName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 2, 1, 2),
    _FnUserRadName_Type()
)
fnUserRadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserRadName.setStatus("mandatory")
_FnUserRadAddr_Type = DisplayString
_FnUserRadAddr_Object = MibTableColumn
fnUserRadAddr = _FnUserRadAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 2, 1, 3),
    _FnUserRadAddr_Type()
)
fnUserRadAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserRadAddr.setStatus("mandatory")
_FnUserRadSecret_Type = OctetString
_FnUserRadSecret_Object = MibTableColumn
fnUserRadSecret = _FnUserRadSecret_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 2, 1, 4),
    _FnUserRadSecret_Type()
)
fnUserRadSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserRadSecret.setStatus("mandatory")
_FnUserGrpTable_Object = MibTable
fnUserGrpTable = _FnUserGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 3)
)
if mibBuilder.loadTexts:
    fnUserGrpTable.setStatus("mandatory")
_FnUserGrpEntry_Object = MibTableRow
fnUserGrpEntry = _FnUserGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 3, 1)
)
fnUserGrpEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnUserGrpIndex"),
)
if mibBuilder.loadTexts:
    fnUserGrpEntry.setStatus("mandatory")


class _FnUserGrpIndex_Type(Integer32):
    """Custom type fnUserGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnUserGrpIndex_Type.__name__ = "Integer32"
_FnUserGrpIndex_Object = MibTableColumn
fnUserGrpIndex = _FnUserGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 3, 1, 1),
    _FnUserGrpIndex_Type()
)
fnUserGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnUserGrpIndex.setStatus("mandatory")
_FnUserGrpName_Type = DisplayString
_FnUserGrpName_Object = MibTableColumn
fnUserGrpName = _FnUserGrpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 3, 1, 2),
    _FnUserGrpName_Type()
)
fnUserGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserGrpName.setStatus("mandatory")


class _FnUserGrpMembers_Type(DisplayString):
    """Custom type fnUserGrpMembers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7000),
    )


_FnUserGrpMembers_Type.__name__ = "DisplayString"
_FnUserGrpMembers_Object = MibTableColumn
fnUserGrpMembers = _FnUserGrpMembers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 3, 1, 3),
    _FnUserGrpMembers_Type()
)
fnUserGrpMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserGrpMembers.setStatus("mandatory")
_FnVpn_ObjectIdentity = ObjectIdentity
fnVpn = _FnVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 4)
)
_FnVpnIPSEC_ObjectIdentity = ObjectIdentity
fnVpnIPSEC = _FnVpnIPSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1)
)
_FnVpnIKETable_Object = MibTable
fnVpnIKETable = _FnVpnIKETable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2)
)
if mibBuilder.loadTexts:
    fnVpnIKETable.setStatus("mandatory")
_FnVpnIKEEntry_Object = MibTableRow
fnVpnIKEEntry = _FnVpnIKEEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1)
)
fnVpnIKEEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnVpnIKEIndex"),
)
if mibBuilder.loadTexts:
    fnVpnIKEEntry.setStatus("mandatory")


class _FnVpnIKEIndex_Type(Integer32):
    """Custom type fnVpnIKEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnVpnIKEIndex_Type.__name__ = "Integer32"
_FnVpnIKEIndex_Object = MibTableColumn
fnVpnIKEIndex = _FnVpnIKEIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 1),
    _FnVpnIKEIndex_Type()
)
fnVpnIKEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEIndex.setStatus("mandatory")


class _FnVpnIKEName_Type(DisplayString):
    """Custom type fnVpnIKEName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnVpnIKEName_Type.__name__ = "DisplayString"
_FnVpnIKEName_Object = MibTableColumn
fnVpnIKEName = _FnVpnIKEName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 2),
    _FnVpnIKEName_Type()
)
fnVpnIKEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEName.setStatus("mandatory")


class _FnVpnIKEGW1_Type(DisplayString):
    """Custom type fnVpnIKEGW1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnVpnIKEGW1_Type.__name__ = "DisplayString"
_FnVpnIKEGW1_Object = MibTableColumn
fnVpnIKEGW1 = _FnVpnIKEGW1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 4),
    _FnVpnIKEGW1_Type()
)
fnVpnIKEGW1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEGW1.setStatus("mandatory")
_FnVpnIKEPh2Encrp1_Type = EncrytionAlgorithm
_FnVpnIKEPh2Encrp1_Object = MibTableColumn
fnVpnIKEPh2Encrp1 = _FnVpnIKEPh2Encrp1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 5),
    _FnVpnIKEPh2Encrp1_Type()
)
fnVpnIKEPh2Encrp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEPh2Encrp1.setStatus("mandatory")
_FnVpnIKEPh2Auth1_Type = AuthAlgorithm
_FnVpnIKEPh2Auth1_Object = MibTableColumn
fnVpnIKEPh2Auth1 = _FnVpnIKEPh2Auth1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 6),
    _FnVpnIKEPh2Auth1_Type()
)
fnVpnIKEPh2Auth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEPh2Auth1.setStatus("mandatory")
_FnVpnIKEPh2Encrp2_Type = EncrytionAlgorithm
_FnVpnIKEPh2Encrp2_Object = MibTableColumn
fnVpnIKEPh2Encrp2 = _FnVpnIKEPh2Encrp2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 7),
    _FnVpnIKEPh2Encrp2_Type()
)
fnVpnIKEPh2Encrp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEPh2Encrp2.setStatus("mandatory")
_FnVpnIKEPh2Auth2_Type = AuthAlgorithm
_FnVpnIKEPh2Auth2_Object = MibTableColumn
fnVpnIKEPh2Auth2 = _FnVpnIKEPh2Auth2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 8),
    _FnVpnIKEPh2Auth2_Type()
)
fnVpnIKEPh2Auth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEPh2Auth2.setStatus("mandatory")
_FnVpnIKEPh2Encrp3_Type = EncrytionAlgorithm
_FnVpnIKEPh2Encrp3_Object = MibTableColumn
fnVpnIKEPh2Encrp3 = _FnVpnIKEPh2Encrp3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 9),
    _FnVpnIKEPh2Encrp3_Type()
)
fnVpnIKEPh2Encrp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEPh2Encrp3.setStatus("mandatory")
_FnVpnIKEPh2Auth3_Type = AuthAlgorithm
_FnVpnIKEPh2Auth3_Object = MibTableColumn
fnVpnIKEPh2Auth3 = _FnVpnIKEPh2Auth3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 10),
    _FnVpnIKEPh2Auth3_Type()
)
fnVpnIKEPh2Auth3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEPh2Auth3.setStatus("mandatory")
_FnVpnIKEReplayDet_Type = ItemState
_FnVpnIKEReplayDet_Object = MibTableColumn
fnVpnIKEReplayDet = _FnVpnIKEReplayDet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 11),
    _FnVpnIKEReplayDet_Type()
)
fnVpnIKEReplayDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEReplayDet.setStatus("mandatory")
_FnVpnIKEPFSState_Type = ItemState
_FnVpnIKEPFSState_Object = MibTableColumn
fnVpnIKEPFSState = _FnVpnIKEPFSState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 12),
    _FnVpnIKEPFSState_Type()
)
fnVpnIKEPFSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEPFSState.setStatus("mandatory")


class _FnVpnIKEDHGrp_Type(Integer32):
    """Custom type fnVpnIKEDHGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5))
    )


_FnVpnIKEDHGrp_Type.__name__ = "Integer32"
_FnVpnIKEDHGrp_Object = MibTableColumn
fnVpnIKEDHGrp = _FnVpnIKEDHGrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 13),
    _FnVpnIKEDHGrp_Type()
)
fnVpnIKEDHGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEDHGrp.setStatus("mandatory")


class _FnVpnIKEKeylifeType_Type(Integer32):
    """Custom type fnVpnIKEKeylifeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbs", 2),
          ("seconds", 1))
    )


_FnVpnIKEKeylifeType_Type.__name__ = "Integer32"
_FnVpnIKEKeylifeType_Object = MibTableColumn
fnVpnIKEKeylifeType = _FnVpnIKEKeylifeType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 14),
    _FnVpnIKEKeylifeType_Type()
)
fnVpnIKEKeylifeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEKeylifeType.setStatus("mandatory")


class _FnVpnIKEKLifeSec_Type(Integer32):
    """Custom type fnVpnIKEKLifeSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 700000),
    )


_FnVpnIKEKLifeSec_Type.__name__ = "Integer32"
_FnVpnIKEKLifeSec_Object = MibTableColumn
fnVpnIKEKLifeSec = _FnVpnIKEKLifeSec_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 15),
    _FnVpnIKEKLifeSec_Type()
)
fnVpnIKEKLifeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEKLifeSec.setStatus("mandatory")


class _FnVpnIKEKeylifeKb_Type(Integer32):
    """Custom type fnVpnIKEKeylifeKb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 2147483647),
    )


_FnVpnIKEKeylifeKb_Type.__name__ = "Integer32"
_FnVpnIKEKeylifeKb_Object = MibTableColumn
fnVpnIKEKeylifeKb = _FnVpnIKEKeylifeKb_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 16),
    _FnVpnIKEKeylifeKb_Type()
)
fnVpnIKEKeylifeKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEKeylifeKb.setStatus("mandatory")
_FnVpnIKEKeepAlive_Type = ItemState
_FnVpnIKEKeepAlive_Object = MibTableColumn
fnVpnIKEKeepAlive = _FnVpnIKEKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 17),
    _FnVpnIKEKeepAlive_Type()
)
fnVpnIKEKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEKeepAlive.setStatus("mandatory")


class _FnVpnIKEGW2_Type(DisplayString):
    """Custom type fnVpnIKEGW2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnIKEGW2_Type.__name__ = "DisplayString"
_FnVpnIKEGW2_Object = MibTableColumn
fnVpnIKEGW2 = _FnVpnIKEGW2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 18),
    _FnVpnIKEGW2_Type()
)
fnVpnIKEGW2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEGW2.setStatus("mandatory")


class _FnVpnIKEGW3_Type(DisplayString):
    """Custom type fnVpnIKEGW3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnIKEGW3_Type.__name__ = "DisplayString"
_FnVpnIKEGW3_Object = MibTableColumn
fnVpnIKEGW3 = _FnVpnIKEGW3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 19),
    _FnVpnIKEGW3_Type()
)
fnVpnIKEGW3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEGW3.setStatus("mandatory")


class _FnVpnIKEConcentrator_Type(DisplayString):
    """Custom type fnVpnIKEConcentrator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnVpnIKEConcentrator_Type.__name__ = "DisplayString"
_FnVpnIKEConcentrator_Object = MibTableColumn
fnVpnIKEConcentrator = _FnVpnIKEConcentrator_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 20),
    _FnVpnIKEConcentrator_Type()
)
fnVpnIKEConcentrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEConcentrator.setStatus("mandatory")


class _FnVpnIKEStatus_Type(Integer32):
    """Custom type fnVpnIKEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_FnVpnIKEStatus_Type.__name__ = "Integer32"
_FnVpnIKEStatus_Object = MibTableColumn
fnVpnIKEStatus = _FnVpnIKEStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 21),
    _FnVpnIKEStatus_Type()
)
fnVpnIKEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKEStatus.setStatus("mandatory")


class _FnVpnIKETimeout_Type(Integer32):
    """Custom type fnVpnIKETimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_FnVpnIKETimeout_Type.__name__ = "Integer32"
_FnVpnIKETimeout_Object = MibTableColumn
fnVpnIKETimeout = _FnVpnIKETimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 2, 1, 22),
    _FnVpnIKETimeout_Type()
)
fnVpnIKETimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnIKETimeout.setStatus("mandatory")
_FnVpnManualKeyTable_Object = MibTable
fnVpnManualKeyTable = _FnVpnManualKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3)
)
if mibBuilder.loadTexts:
    fnVpnManualKeyTable.setStatus("mandatory")
_FnVpnManualKeyEntry_Object = MibTableRow
fnVpnManualKeyEntry = _FnVpnManualKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1)
)
fnVpnManualKeyEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnVpnManualKeyIndex"),
)
if mibBuilder.loadTexts:
    fnVpnManualKeyEntry.setStatus("mandatory")


class _FnVpnManualKeyIndex_Type(Integer32):
    """Custom type fnVpnManualKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnVpnManualKeyIndex_Type.__name__ = "Integer32"
_FnVpnManualKeyIndex_Object = MibTableColumn
fnVpnManualKeyIndex = _FnVpnManualKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 1),
    _FnVpnManualKeyIndex_Type()
)
fnVpnManualKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyIndex.setStatus("mandatory")


class _FnVpnManualKeyName_Type(DisplayString):
    """Custom type fnVpnManualKeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnVpnManualKeyName_Type.__name__ = "DisplayString"
_FnVpnManualKeyName_Object = MibTableColumn
fnVpnManualKeyName = _FnVpnManualKeyName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 2),
    _FnVpnManualKeyName_Type()
)
fnVpnManualKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyName.setStatus("mandatory")


class _FnVpnManualKeyEngage_Type(Integer32):
    """Custom type fnVpnManualKeyEngage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FnVpnManualKeyEngage_Type.__name__ = "Integer32"
_FnVpnManualKeyEngage_Object = MibTableColumn
fnVpnManualKeyEngage = _FnVpnManualKeyEngage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 3),
    _FnVpnManualKeyEngage_Type()
)
fnVpnManualKeyEngage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyEngage.setStatus("mandatory")


class _FnVpnManualKeyLocalSPI_Type(DisplayString):
    """Custom type fnVpnManualKeyLocalSPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnManualKeyLocalSPI_Type.__name__ = "DisplayString"
_FnVpnManualKeyLocalSPI_Object = MibTableColumn
fnVpnManualKeyLocalSPI = _FnVpnManualKeyLocalSPI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 4),
    _FnVpnManualKeyLocalSPI_Type()
)
fnVpnManualKeyLocalSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyLocalSPI.setStatus("mandatory")
_FnVpnManualKeyRemoteSPI_Type = DisplayString
_FnVpnManualKeyRemoteSPI_Object = MibTableColumn
fnVpnManualKeyRemoteSPI = _FnVpnManualKeyRemoteSPI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 5),
    _FnVpnManualKeyRemoteSPI_Type()
)
fnVpnManualKeyRemoteSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyRemoteSPI.setStatus("mandatory")


class _FnVpnManualKeyRgw_Type(DisplayString):
    """Custom type fnVpnManualKeyRgw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnVpnManualKeyRgw_Type.__name__ = "DisplayString"
_FnVpnManualKeyRgw_Object = MibTableColumn
fnVpnManualKeyRgw = _FnVpnManualKeyRgw_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 6),
    _FnVpnManualKeyRgw_Type()
)
fnVpnManualKeyRgw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyRgw.setStatus("mandatory")
_FnVpnManualKeyReplayDet_Type = ItemState
_FnVpnManualKeyReplayDet_Object = MibTableColumn
fnVpnManualKeyReplayDet = _FnVpnManualKeyReplayDet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 7),
    _FnVpnManualKeyReplayDet_Type()
)
fnVpnManualKeyReplayDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyReplayDet.setStatus("mandatory")


class _FnVpnManualKeyEncrpAlgorithm_Type(DisplayString):
    """Custom type fnVpnManualKeyEncrpAlgorithm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnVpnManualKeyEncrpAlgorithm_Type.__name__ = "DisplayString"
_FnVpnManualKeyEncrpAlgorithm_Object = MibTableColumn
fnVpnManualKeyEncrpAlgorithm = _FnVpnManualKeyEncrpAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 8),
    _FnVpnManualKeyEncrpAlgorithm_Type()
)
fnVpnManualKeyEncrpAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyEncrpAlgorithm.setStatus("mandatory")


class _FnVpnManualKeyConcentrator_Type(DisplayString):
    """Custom type fnVpnManualKeyConcentrator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnVpnManualKeyConcentrator_Type.__name__ = "DisplayString"
_FnVpnManualKeyConcentrator_Object = MibTableColumn
fnVpnManualKeyConcentrator = _FnVpnManualKeyConcentrator_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 3, 1, 9),
    _FnVpnManualKeyConcentrator_Type()
)
fnVpnManualKeyConcentrator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnManualKeyConcentrator.setStatus("mandatory")
_FnVpnRemoteGWTable_Object = MibTable
fnVpnRemoteGWTable = _FnVpnRemoteGWTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4)
)
if mibBuilder.loadTexts:
    fnVpnRemoteGWTable.setStatus("mandatory")
_FnVpnRemoteGWEntry_Object = MibTableRow
fnVpnRemoteGWEntry = _FnVpnRemoteGWEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1)
)
fnVpnRemoteGWEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnVpnRemoteGWIndex"),
)
if mibBuilder.loadTexts:
    fnVpnRemoteGWEntry.setStatus("mandatory")


class _FnVpnRemoteGWIndex_Type(Integer32):
    """Custom type fnVpnRemoteGWIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnVpnRemoteGWIndex_Type.__name__ = "Integer32"
_FnVpnRemoteGWIndex_Object = MibTableColumn
fnVpnRemoteGWIndex = _FnVpnRemoteGWIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 1),
    _FnVpnRemoteGWIndex_Type()
)
fnVpnRemoteGWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnRemoteGWIndex.setStatus("mandatory")
_FnVpnRemoteGWName_Type = DisplayString
_FnVpnRemoteGWName_Object = MibTableColumn
fnVpnRemoteGWName = _FnVpnRemoteGWName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 2),
    _FnVpnRemoteGWName_Type()
)
fnVpnRemoteGWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWName.setStatus("mandatory")
_FnVpnRemoteGWIp_Type = IpAddress
_FnVpnRemoteGWIp_Object = MibTableColumn
fnVpnRemoteGWIp = _FnVpnRemoteGWIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 3),
    _FnVpnRemoteGWIp_Type()
)
fnVpnRemoteGWIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWIp.setStatus("mandatory")


class _FnVpnRemoteGWMode_Type(Integer32):
    """Custom type fnVpnRemoteGWMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_FnVpnRemoteGWMode_Type.__name__ = "Integer32"
_FnVpnRemoteGWMode_Object = MibTableColumn
fnVpnRemoteGWMode = _FnVpnRemoteGWMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 4),
    _FnVpnRemoteGWMode_Type()
)
fnVpnRemoteGWMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWMode.setStatus("mandatory")
_FnVpnRemoteGWPh1Encrp1_Type = EncrytionAlgorithm
_FnVpnRemoteGWPh1Encrp1_Object = MibTableColumn
fnVpnRemoteGWPh1Encrp1 = _FnVpnRemoteGWPh1Encrp1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 5),
    _FnVpnRemoteGWPh1Encrp1_Type()
)
fnVpnRemoteGWPh1Encrp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPh1Encrp1.setStatus("mandatory")
_FnVpnRemoteGWPh1Auth1_Type = AuthAlgorithm
_FnVpnRemoteGWPh1Auth1_Object = MibTableColumn
fnVpnRemoteGWPh1Auth1 = _FnVpnRemoteGWPh1Auth1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 6),
    _FnVpnRemoteGWPh1Auth1_Type()
)
fnVpnRemoteGWPh1Auth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPh1Auth1.setStatus("mandatory")
_FnVpnRemoteGWPh1Encrp2_Type = EncrytionAlgorithm
_FnVpnRemoteGWPh1Encrp2_Object = MibTableColumn
fnVpnRemoteGWPh1Encrp2 = _FnVpnRemoteGWPh1Encrp2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 7),
    _FnVpnRemoteGWPh1Encrp2_Type()
)
fnVpnRemoteGWPh1Encrp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPh1Encrp2.setStatus("mandatory")
_FnVpnRemoteGWPh1Auth2_Type = AuthAlgorithm
_FnVpnRemoteGWPh1Auth2_Object = MibTableColumn
fnVpnRemoteGWPh1Auth2 = _FnVpnRemoteGWPh1Auth2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 8),
    _FnVpnRemoteGWPh1Auth2_Type()
)
fnVpnRemoteGWPh1Auth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPh1Auth2.setStatus("mandatory")
_FnVpnRemoteGWPh1Encrp3_Type = EncrytionAlgorithm
_FnVpnRemoteGWPh1Encrp3_Object = MibTableColumn
fnVpnRemoteGWPh1Encrp3 = _FnVpnRemoteGWPh1Encrp3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 9),
    _FnVpnRemoteGWPh1Encrp3_Type()
)
fnVpnRemoteGWPh1Encrp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPh1Encrp3.setStatus("mandatory")
_FnVpnRemoteGWPh1Auth3_Type = AuthAlgorithm
_FnVpnRemoteGWPh1Auth3_Object = MibTableColumn
fnVpnRemoteGWPh1Auth3 = _FnVpnRemoteGWPh1Auth3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 10),
    _FnVpnRemoteGWPh1Auth3_Type()
)
fnVpnRemoteGWPh1Auth3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPh1Auth3.setStatus("mandatory")


class _FnVpnRemoteGWDhGrp_Type(Integer32):
    """Custom type fnVpnRemoteGWDhGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5))
    )


_FnVpnRemoteGWDhGrp_Type.__name__ = "Integer32"
_FnVpnRemoteGWDhGrp_Object = MibTableColumn
fnVpnRemoteGWDhGrp = _FnVpnRemoteGWDhGrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 11),
    _FnVpnRemoteGWDhGrp_Type()
)
fnVpnRemoteGWDhGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWDhGrp.setStatus("mandatory")


class _FnVpnRemoteGWKeylife_Type(Integer32):
    """Custom type fnVpnRemoteGWKeylife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 180000),
    )


_FnVpnRemoteGWKeylife_Type.__name__ = "Integer32"
_FnVpnRemoteGWKeylife_Object = MibTableColumn
fnVpnRemoteGWKeylife = _FnVpnRemoteGWKeylife_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 12),
    _FnVpnRemoteGWKeylife_Type()
)
fnVpnRemoteGWKeylife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWKeylife.setStatus("mandatory")
_FnVpnRemoteGWPreKey_Type = OctetString
_FnVpnRemoteGWPreKey_Object = MibTableColumn
fnVpnRemoteGWPreKey = _FnVpnRemoteGWPreKey_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 13),
    _FnVpnRemoteGWPreKey_Type()
)
fnVpnRemoteGWPreKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPreKey.setStatus("mandatory")
_FnVpnRemoteGWLocalID_Type = DisplayString
_FnVpnRemoteGWLocalID_Object = MibTableColumn
fnVpnRemoteGWLocalID = _FnVpnRemoteGWLocalID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 14),
    _FnVpnRemoteGWLocalID_Type()
)
fnVpnRemoteGWLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWLocalID.setStatus("optional")
_FnVpnRemoteGWNatT_Type = ItemState
_FnVpnRemoteGWNatT_Object = MibTableColumn
fnVpnRemoteGWNatT = _FnVpnRemoteGWNatT_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 15),
    _FnVpnRemoteGWNatT_Type()
)
fnVpnRemoteGWNatT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWNatT.setStatus("mandatory")


class _FnVpnRemoteGWKAFreq_Type(Integer32):
    """Custom type fnVpnRemoteGWKAFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnVpnRemoteGWKAFreq_Type.__name__ = "Integer32"
_FnVpnRemoteGWKAFreq_Object = MibTableColumn
fnVpnRemoteGWKAFreq = _FnVpnRemoteGWKAFreq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 16),
    _FnVpnRemoteGWKAFreq_Type()
)
fnVpnRemoteGWKAFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWKAFreq.setStatus("mandatory")


class _FnVpnRemoteGWType_Type(Integer32):
    """Custom type fnVpnRemoteGWType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialupUser", 2),
          ("staticIP", 1))
    )


_FnVpnRemoteGWType_Type.__name__ = "Integer32"
_FnVpnRemoteGWType_Object = MibTableColumn
fnVpnRemoteGWType = _FnVpnRemoteGWType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 17),
    _FnVpnRemoteGWType_Type()
)
fnVpnRemoteGWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWType.setStatus("mandatory")
_FnVpnRemoteGWUserGrp_Type = DisplayString
_FnVpnRemoteGWUserGrp_Object = MibTableColumn
fnVpnRemoteGWUserGrp = _FnVpnRemoteGWUserGrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 18),
    _FnVpnRemoteGWUserGrp_Type()
)
fnVpnRemoteGWUserGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWUserGrp.setStatus("mandatory")


class _FnVpnRemoteGWAuthMethod_Type(Integer32):
    """Custom type fnVpnRemoteGWAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preshared-key", 1),
          ("rsa", 2))
    )


_FnVpnRemoteGWAuthMethod_Type.__name__ = "Integer32"
_FnVpnRemoteGWAuthMethod_Object = MibTableColumn
fnVpnRemoteGWAuthMethod = _FnVpnRemoteGWAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 19),
    _FnVpnRemoteGWAuthMethod_Type()
)
fnVpnRemoteGWAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWAuthMethod.setStatus("mandatory")


class _FnVpnRemoteGWCertName_Type(Integer32):
    """Custom type fnVpnRemoteGWCertName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preshared-key", 1),
          ("rsa", 2))
    )


_FnVpnRemoteGWCertName_Type.__name__ = "Integer32"
_FnVpnRemoteGWCertName_Object = MibTableColumn
fnVpnRemoteGWCertName = _FnVpnRemoteGWCertName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 20),
    _FnVpnRemoteGWCertName_Type()
)
fnVpnRemoteGWCertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWCertName.setStatus("mandatory")


class _FnVpnRemoteGWPeerOpt_Type(Integer32):
    """Custom type fnVpnRemoteGWPeerOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acceptAnyPeerId", 1),
          ("acceptPeerIdInGrp", 3),
          ("acceptThisPeerId", 2))
    )


_FnVpnRemoteGWPeerOpt_Type.__name__ = "Integer32"
_FnVpnRemoteGWPeerOpt_Object = MibTableColumn
fnVpnRemoteGWPeerOpt = _FnVpnRemoteGWPeerOpt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 21),
    _FnVpnRemoteGWPeerOpt_Type()
)
fnVpnRemoteGWPeerOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPeerOpt.setStatus("mandatory")


class _FnVpnRemoteGWPeerGrpName_Type(Integer32):
    """Custom type fnVpnRemoteGWPeerGrpName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acceptAnyPeerId", 1),
          ("acceptPeerIdInGrp", 3),
          ("acceptThisPeerId", 2))
    )


_FnVpnRemoteGWPeerGrpName_Type.__name__ = "Integer32"
_FnVpnRemoteGWPeerGrpName_Object = MibTableColumn
fnVpnRemoteGWPeerGrpName = _FnVpnRemoteGWPeerGrpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 22),
    _FnVpnRemoteGWPeerGrpName_Type()
)
fnVpnRemoteGWPeerGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPeerGrpName.setStatus("mandatory")
_FnVpnRemoteGWPeerId_Type = DisplayString
_FnVpnRemoteGWPeerId_Object = MibTableColumn
fnVpnRemoteGWPeerId = _FnVpnRemoteGWPeerId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 23),
    _FnVpnRemoteGWPeerId_Type()
)
fnVpnRemoteGWPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWPeerId.setStatus("mandatory")


class _FnVpnRemoteGWXAuth_Type(Integer32):
    """Custom type fnVpnRemoteGWXAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diable", 3),
          ("enableAsClient", 1),
          ("enableAsServer", 2))
    )


_FnVpnRemoteGWXAuth_Type.__name__ = "Integer32"
_FnVpnRemoteGWXAuth_Object = MibTableColumn
fnVpnRemoteGWXAuth = _FnVpnRemoteGWXAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 24),
    _FnVpnRemoteGWXAuth_Type()
)
fnVpnRemoteGWXAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWXAuth.setStatus("mandatory")
_FnVpnRemoteGWXAuthUserName_Type = DisplayString
_FnVpnRemoteGWXAuthUserName_Object = MibTableColumn
fnVpnRemoteGWXAuthUserName = _FnVpnRemoteGWXAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 25),
    _FnVpnRemoteGWXAuthUserName_Type()
)
fnVpnRemoteGWXAuthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWXAuthUserName.setStatus("mandatory")
_FnVpnRemoteGWXAuthPasswd_Type = OctetString
_FnVpnRemoteGWXAuthPasswd_Object = MibTableColumn
fnVpnRemoteGWXAuthPasswd = _FnVpnRemoteGWXAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 26),
    _FnVpnRemoteGWXAuthPasswd_Type()
)
fnVpnRemoteGWXAuthPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWXAuthPasswd.setStatus("mandatory")


class _FnVpnRemoteGWXAuthPap_Type(Integer32):
    """Custom type fnVpnRemoteGWXAuthPap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_FnVpnRemoteGWXAuthPap_Type.__name__ = "Integer32"
_FnVpnRemoteGWXAuthPap_Object = MibTableColumn
fnVpnRemoteGWXAuthPap = _FnVpnRemoteGWXAuthPap_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 27),
    _FnVpnRemoteGWXAuthPap_Type()
)
fnVpnRemoteGWXAuthPap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWXAuthPap.setStatus("mandatory")
_FnVpnRemoteGWDeadPeerDet_Type = ItemState
_FnVpnRemoteGWDeadPeerDet_Object = MibTableColumn
fnVpnRemoteGWDeadPeerDet = _FnVpnRemoteGWDeadPeerDet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 28),
    _FnVpnRemoteGWDeadPeerDet_Type()
)
fnVpnRemoteGWDeadPeerDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWDeadPeerDet.setStatus("mandatory")


class _FnVpnRemoteGWDpdIdleWorry_Type(Integer32):
    """Custom type fnVpnRemoteGWDpdIdleWorry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnVpnRemoteGWDpdIdleWorry_Type.__name__ = "Integer32"
_FnVpnRemoteGWDpdIdleWorry_Object = MibTableColumn
fnVpnRemoteGWDpdIdleWorry = _FnVpnRemoteGWDpdIdleWorry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 29),
    _FnVpnRemoteGWDpdIdleWorry_Type()
)
fnVpnRemoteGWDpdIdleWorry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWDpdIdleWorry.setStatus("mandatory")


class _FnVpnRemoteGWDpdRetryCound_Type(Integer32):
    """Custom type fnVpnRemoteGWDpdRetryCound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnVpnRemoteGWDpdRetryCound_Type.__name__ = "Integer32"
_FnVpnRemoteGWDpdRetryCound_Object = MibTableColumn
fnVpnRemoteGWDpdRetryCound = _FnVpnRemoteGWDpdRetryCound_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 30),
    _FnVpnRemoteGWDpdRetryCound_Type()
)
fnVpnRemoteGWDpdRetryCound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWDpdRetryCound.setStatus("mandatory")


class _FnVpnRemoteGWDpdRetryInt_Type(Integer32):
    """Custom type fnVpnRemoteGWDpdRetryInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnVpnRemoteGWDpdRetryInt_Type.__name__ = "Integer32"
_FnVpnRemoteGWDpdRetryInt_Object = MibTableColumn
fnVpnRemoteGWDpdRetryInt = _FnVpnRemoteGWDpdRetryInt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 31),
    _FnVpnRemoteGWDpdRetryInt_Type()
)
fnVpnRemoteGWDpdRetryInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWDpdRetryInt.setStatus("mandatory")


class _FnVpnRemoteGWDpdIdleCleanup_Type(Integer32):
    """Custom type fnVpnRemoteGWDpdIdleCleanup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnVpnRemoteGWDpdIdleCleanup_Type.__name__ = "Integer32"
_FnVpnRemoteGWDpdIdleCleanup_Object = MibTableColumn
fnVpnRemoteGWDpdIdleCleanup = _FnVpnRemoteGWDpdIdleCleanup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 4, 1, 32),
    _FnVpnRemoteGWDpdIdleCleanup_Type()
)
fnVpnRemoteGWDpdIdleCleanup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnRemoteGWDpdIdleCleanup.setStatus("mandatory")
_FnVpnConTable_Object = MibTable
fnVpnConTable = _FnVpnConTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 5)
)
if mibBuilder.loadTexts:
    fnVpnConTable.setStatus("mandatory")
_FnVpnConEntry_Object = MibTableRow
fnVpnConEntry = _FnVpnConEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 5, 1)
)
fnVpnConEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnVpnConIndex"),
)
if mibBuilder.loadTexts:
    fnVpnConEntry.setStatus("mandatory")


class _FnVpnConIndex_Type(Integer32):
    """Custom type fnVpnConIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnVpnConIndex_Type.__name__ = "Integer32"
_FnVpnConIndex_Object = MibTableColumn
fnVpnConIndex = _FnVpnConIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 5, 1, 1),
    _FnVpnConIndex_Type()
)
fnVpnConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnConIndex.setStatus("mandatory")
_FnVpnConName_Type = DisplayString
_FnVpnConName_Object = MibTableColumn
fnVpnConName = _FnVpnConName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 5, 1, 2),
    _FnVpnConName_Type()
)
fnVpnConName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnConName.setStatus("mandatory")


class _FnVpnConMembers_Type(DisplayString):
    """Custom type fnVpnConMembers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7000),
    )


_FnVpnConMembers_Type.__name__ = "DisplayString"
_FnVpnConMembers_Object = MibTableColumn
fnVpnConMembers = _FnVpnConMembers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 5, 1, 3),
    _FnVpnConMembers_Type()
)
fnVpnConMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnConMembers.setStatus("mandatory")
_FnVpnDialupMonTable_Object = MibTable
fnVpnDialupMonTable = _FnVpnDialupMonTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6)
)
if mibBuilder.loadTexts:
    fnVpnDialupMonTable.setStatus("mandatory")
_FnVpnDialupMonEntry_Object = MibTableRow
fnVpnDialupMonEntry = _FnVpnDialupMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6, 1)
)
fnVpnDialupMonEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnVpnDialupMonIndex"),
)
if mibBuilder.loadTexts:
    fnVpnDialupMonEntry.setStatus("mandatory")


class _FnVpnDialupMonIndex_Type(Integer32):
    """Custom type fnVpnDialupMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnVpnDialupMonIndex_Type.__name__ = "Integer32"
_FnVpnDialupMonIndex_Object = MibTableColumn
fnVpnDialupMonIndex = _FnVpnDialupMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6, 1, 1),
    _FnVpnDialupMonIndex_Type()
)
fnVpnDialupMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnDialupMonIndex.setStatus("mandatory")
_FnVpnDialupMonRGwName_Type = DisplayString
_FnVpnDialupMonRGwName_Object = MibTableColumn
fnVpnDialupMonRGwName = _FnVpnDialupMonRGwName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6, 1, 2),
    _FnVpnDialupMonRGwName_Type()
)
fnVpnDialupMonRGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupMonRGwName.setStatus("mandatory")
_FnVpnDialupMonLifetime_Type = Integer32
_FnVpnDialupMonLifetime_Object = MibTableColumn
fnVpnDialupMonLifetime = _FnVpnDialupMonLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6, 1, 3),
    _FnVpnDialupMonLifetime_Type()
)
fnVpnDialupMonLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupMonLifetime.setStatus("mandatory")
_FnVpnDialupMonTimeout_Type = Integer32
_FnVpnDialupMonTimeout_Object = MibTableColumn
fnVpnDialupMonTimeout = _FnVpnDialupMonTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6, 1, 4),
    _FnVpnDialupMonTimeout_Type()
)
fnVpnDialupMonTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupMonTimeout.setStatus("mandatory")
_FnVpnDialupMonProxyIdSrc_Type = DisplayString
_FnVpnDialupMonProxyIdSrc_Object = MibTableColumn
fnVpnDialupMonProxyIdSrc = _FnVpnDialupMonProxyIdSrc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6, 1, 5),
    _FnVpnDialupMonProxyIdSrc_Type()
)
fnVpnDialupMonProxyIdSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupMonProxyIdSrc.setStatus("mandatory")
_FnVpnDialupMonProxyIdDst_Type = DisplayString
_FnVpnDialupMonProxyIdDst_Object = MibTableColumn
fnVpnDialupMonProxyIdDst = _FnVpnDialupMonProxyIdDst_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 1, 6, 1, 6),
    _FnVpnDialupMonProxyIdDst_Type()
)
fnVpnDialupMonProxyIdDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupMonProxyIdDst.setStatus("mandatory")
_FnVpnPPTP_ObjectIdentity = ObjectIdentity
fnVpnPPTP = _FnVpnPPTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2)
)
_FnVpnPPTPStatus_Type = ItemState
_FnVpnPPTPStatus_Object = MibScalar
fnVpnPPTPStatus = _FnVpnPPTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1),
    _FnVpnPPTPStatus_Type()
)
fnVpnPPTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnPPTPStatus.setStatus("mandatory")


class _FnVpnPPTPUserGrp_Type(DisplayString):
    """Custom type fnVpnPPTPUserGrp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnPPTPUserGrp_Type.__name__ = "DisplayString"
_FnVpnPPTPUserGrp_Object = MibScalar
fnVpnPPTPUserGrp = _FnVpnPPTPUserGrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 2),
    _FnVpnPPTPUserGrp_Type()
)
fnVpnPPTPUserGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnPPTPUserGrp.setStatus("mandatory")
_FnVpnPPTPStartIp_Type = IpAddress
_FnVpnPPTPStartIp_Object = MibScalar
fnVpnPPTPStartIp = _FnVpnPPTPStartIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 3),
    _FnVpnPPTPStartIp_Type()
)
fnVpnPPTPStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnPPTPStartIp.setStatus("mandatory")
_FnVpnPPTPEndIp_Type = IpAddress
_FnVpnPPTPEndIp_Object = MibScalar
fnVpnPPTPEndIp = _FnVpnPPTPEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 4),
    _FnVpnPPTPEndIp_Type()
)
fnVpnPPTPEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnPPTPEndIp.setStatus("mandatory")
_FnVpnL2TP_ObjectIdentity = ObjectIdentity
fnVpnL2TP = _FnVpnL2TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3)
)
_FnVpnL2TPStatus_Type = ItemState
_FnVpnL2TPStatus_Object = MibScalar
fnVpnL2TPStatus = _FnVpnL2TPStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3, 1),
    _FnVpnL2TPStatus_Type()
)
fnVpnL2TPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnL2TPStatus.setStatus("mandatory")


class _FnVpnL2TPUserGrp_Type(DisplayString):
    """Custom type fnVpnL2TPUserGrp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnL2TPUserGrp_Type.__name__ = "DisplayString"
_FnVpnL2TPUserGrp_Object = MibScalar
fnVpnL2TPUserGrp = _FnVpnL2TPUserGrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3, 2),
    _FnVpnL2TPUserGrp_Type()
)
fnVpnL2TPUserGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnL2TPUserGrp.setStatus("mandatory")
_FnVpnL2TPStartIp_Type = IpAddress
_FnVpnL2TPStartIp_Object = MibScalar
fnVpnL2TPStartIp = _FnVpnL2TPStartIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3, 3),
    _FnVpnL2TPStartIp_Type()
)
fnVpnL2TPStartIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnL2TPStartIp.setStatus("mandatory")
_FnVpnL2TPEndIp_Type = IpAddress
_FnVpnL2TPEndIp_Object = MibScalar
fnVpnL2TPEndIp = _FnVpnL2TPEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3, 4),
    _FnVpnL2TPEndIp_Type()
)
fnVpnL2TPEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnL2TPEndIp.setStatus("mandatory")
_FnVpnCert_ObjectIdentity = ObjectIdentity
fnVpnCert = _FnVpnCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4)
)
_FnVpnCertTable_Object = MibTable
fnVpnCertTable = _FnVpnCertTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1)
)
if mibBuilder.loadTexts:
    fnVpnCertTable.setStatus("mandatory")
_FnVpnCertEntry_Object = MibTableRow
fnVpnCertEntry = _FnVpnCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1)
)
fnVpnCertEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnVpnCertName"),
)
if mibBuilder.loadTexts:
    fnVpnCertEntry.setStatus("mandatory")


class _FnVpnCertName_Type(Integer32):
    """Custom type fnVpnCertName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnVpnCertName_Type.__name__ = "Integer32"
_FnVpnCertName_Object = MibTableColumn
fnVpnCertName = _FnVpnCertName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1, 1),
    _FnVpnCertName_Type()
)
fnVpnCertName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnCertName.setStatus("mandatory")


class _FnVpnCertIssuer_Type(DisplayString):
    """Custom type fnVpnCertIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnCertIssuer_Type.__name__ = "DisplayString"
_FnVpnCertIssuer_Object = MibTableColumn
fnVpnCertIssuer = _FnVpnCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1, 2),
    _FnVpnCertIssuer_Type()
)
fnVpnCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnCertIssuer.setStatus("mandatory")


class _FnVpnCertCommonName_Type(DisplayString):
    """Custom type fnVpnCertCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnCertCommonName_Type.__name__ = "DisplayString"
_FnVpnCertCommonName_Object = MibTableColumn
fnVpnCertCommonName = _FnVpnCertCommonName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1, 3),
    _FnVpnCertCommonName_Type()
)
fnVpnCertCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnCertCommonName.setStatus("mandatory")


class _FnVpnCertType_Type(DisplayString):
    """Custom type fnVpnCertType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnCertType_Type.__name__ = "DisplayString"
_FnVpnCertType_Object = MibTableColumn
fnVpnCertType = _FnVpnCertType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1, 4),
    _FnVpnCertType_Type()
)
fnVpnCertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnCertType.setStatus("mandatory")


class _FnVpnCertSerialNo_Type(Integer32):
    """Custom type fnVpnCertSerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnVpnCertSerialNo_Type.__name__ = "Integer32"
_FnVpnCertSerialNo_Object = MibTableColumn
fnVpnCertSerialNo = _FnVpnCertSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1, 5),
    _FnVpnCertSerialNo_Type()
)
fnVpnCertSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnCertSerialNo.setStatus("mandatory")


class _FnVpnCertExpDate_Type(DisplayString):
    """Custom type fnVpnCertExpDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnVpnCertExpDate_Type.__name__ = "DisplayString"
_FnVpnCertExpDate_Object = MibTableColumn
fnVpnCertExpDate = _FnVpnCertExpDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1, 6),
    _FnVpnCertExpDate_Type()
)
fnVpnCertExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnCertExpDate.setStatus("mandatory")


class _FnVpnCertStatus_Type(Integer32):
    """Custom type fnVpnCertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("pending", 2))
    )


_FnVpnCertStatus_Type.__name__ = "Integer32"
_FnVpnCertStatus_Object = MibTableColumn
fnVpnCertStatus = _FnVpnCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 4, 1, 1, 7),
    _FnVpnCertStatus_Type()
)
fnVpnCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnCertStatus.setStatus("mandatory")
_FnNIDS_ObjectIdentity = ObjectIdentity
fnNIDS = _FnNIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 5)
)
_FnNidsDetection_ObjectIdentity = ObjectIdentity
fnNidsDetection = _FnNidsDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1)
)
_FnNidsGen_ObjectIdentity = ObjectIdentity
fnNidsGen = _FnNidsGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 1)
)
_FnNidsMonIfs_Type = DisplayString
_FnNidsMonIfs_Object = MibScalar
fnNidsMonIfs = _FnNidsMonIfs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 1, 1),
    _FnNidsMonIfs_Type()
)
fnNidsMonIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsMonIfs.setStatus("mandatory")
_FnNidsTypeIP_Type = ItemState
_FnNidsTypeIP_Object = MibScalar
fnNidsTypeIP = _FnNidsTypeIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 1, 2),
    _FnNidsTypeIP_Type()
)
fnNidsTypeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsTypeIP.setStatus("mandatory")
_FnNidsTypeTcp_Type = ItemState
_FnNidsTypeTcp_Object = MibScalar
fnNidsTypeTcp = _FnNidsTypeTcp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 1, 3),
    _FnNidsTypeTcp_Type()
)
fnNidsTypeTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsTypeTcp.setStatus("mandatory")
_FnNidsTypeUdp_Type = ItemState
_FnNidsTypeUdp_Object = MibScalar
fnNidsTypeUdp = _FnNidsTypeUdp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 1, 4),
    _FnNidsTypeUdp_Type()
)
fnNidsTypeUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsTypeUdp.setStatus("mandatory")
_FnNidsTypeIcmp_Type = ItemState
_FnNidsTypeIcmp_Object = MibScalar
fnNidsTypeIcmp = _FnNidsTypeIcmp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 1, 5),
    _FnNidsTypeIcmp_Type()
)
fnNidsTypeIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsTypeIcmp.setStatus("mandatory")
_FnNidsSigTable_Object = MibTable
fnNidsSigTable = _FnNidsSigTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 2)
)
if mibBuilder.loadTexts:
    fnNidsSigTable.setStatus("mandatory")
_FnNidsSigEntry_Object = MibTableRow
fnNidsSigEntry = _FnNidsSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 2, 1)
)
fnNidsSigEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnNidsSigGrpName"),
    (0, "FORTINET-MIB", "fnNidsSigAttackId"),
)
if mibBuilder.loadTexts:
    fnNidsSigEntry.setStatus("mandatory")


class _FnNidsSigGrpName_Type(DisplayString):
    """Custom type fnNidsSigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnNidsSigGrpName_Type.__name__ = "DisplayString"
_FnNidsSigGrpName_Object = MibTableColumn
fnNidsSigGrpName = _FnNidsSigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 2, 1, 1),
    _FnNidsSigGrpName_Type()
)
fnNidsSigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnNidsSigGrpName.setStatus("mandatory")


class _FnNidsSigAttackId_Type(Integer32):
    """Custom type fnNidsSigAttackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnNidsSigAttackId_Type.__name__ = "Integer32"
_FnNidsSigAttackId_Object = MibTableColumn
fnNidsSigAttackId = _FnNidsSigAttackId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 2, 1, 2),
    _FnNidsSigAttackId_Type()
)
fnNidsSigAttackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnNidsSigAttackId.setStatus("mandatory")
_FnNidsSigAttackName_Type = Integer32
_FnNidsSigAttackName_Object = MibTableColumn
fnNidsSigAttackName = _FnNidsSigAttackName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 2, 1, 3),
    _FnNidsSigAttackName_Type()
)
fnNidsSigAttackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsSigAttackName.setStatus("mandatory")
_FnNidsSigAttackRuleState_Type = ItemState
_FnNidsSigAttackRuleState_Object = MibTableColumn
fnNidsSigAttackRuleState = _FnNidsSigAttackRuleState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 2, 1, 4),
    _FnNidsSigAttackRuleState_Type()
)
fnNidsSigAttackRuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsSigAttackRuleState.setStatus("mandatory")
_FnNidsSigUserDefTable_Object = MibTable
fnNidsSigUserDefTable = _FnNidsSigUserDefTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 3)
)
if mibBuilder.loadTexts:
    fnNidsSigUserDefTable.setStatus("mandatory")
_FnNidsSigUserDefEntry_Object = MibTableRow
fnNidsSigUserDefEntry = _FnNidsSigUserDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 3, 1)
)
fnNidsSigUserDefEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnNidsSigUserDefName"),
)
if mibBuilder.loadTexts:
    fnNidsSigUserDefEntry.setStatus("mandatory")


class _FnNidsSigUserDefName_Type(Integer32):
    """Custom type fnNidsSigUserDefName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnNidsSigUserDefName_Type.__name__ = "Integer32"
_FnNidsSigUserDefName_Object = MibTableColumn
fnNidsSigUserDefName = _FnNidsSigUserDefName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 3, 1, 1),
    _FnNidsSigUserDefName_Type()
)
fnNidsSigUserDefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnNidsSigUserDefName.setStatus("mandatory")
_FnNidsSigUserDefSum_Type = DisplayString
_FnNidsSigUserDefSum_Object = MibTableColumn
fnNidsSigUserDefSum = _FnNidsSigUserDefSum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 3, 1, 2),
    _FnNidsSigUserDefSum_Type()
)
fnNidsSigUserDefSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsSigUserDefSum.setStatus("mandatory")
_FnNidsSigUserDefProto_Type = DisplayString
_FnNidsSigUserDefProto_Object = MibTableColumn
fnNidsSigUserDefProto = _FnNidsSigUserDefProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 1, 3, 1, 3),
    _FnNidsSigUserDefProto_Type()
)
fnNidsSigUserDefProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsSigUserDefProto.setStatus("mandatory")
_FnNidsPrevention_ObjectIdentity = ObjectIdentity
fnNidsPrevention = _FnNidsPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2)
)
_FnNidsIdpState_Type = ItemState
_FnNidsIdpState_Object = MibScalar
fnNidsIdpState = _FnNidsIdpState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 1),
    _FnNidsIdpState_Type()
)
fnNidsIdpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsIdpState.setStatus("mandatory")
_FnNidsIdpTable_Object = MibTable
fnNidsIdpTable = _FnNidsIdpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2)
)
if mibBuilder.loadTexts:
    fnNidsIdpTable.setStatus("mandatory")
_FnNidsIdpEntry_Object = MibTableRow
fnNidsIdpEntry = _FnNidsIdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1)
)
fnNidsIdpEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnNidsIdpSigName"),
)
if mibBuilder.loadTexts:
    fnNidsIdpEntry.setStatus("mandatory")


class _FnNidsIdpSigName_Type(Integer32):
    """Custom type fnNidsIdpSigName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnNidsIdpSigName_Type.__name__ = "Integer32"
_FnNidsIdpSigName_Object = MibTableColumn
fnNidsIdpSigName = _FnNidsIdpSigName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1, 1),
    _FnNidsIdpSigName_Type()
)
fnNidsIdpSigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnNidsIdpSigName.setStatus("mandatory")
_FnNidsIdpSigSum_Type = DisplayString
_FnNidsIdpSigSum_Object = MibTableColumn
fnNidsIdpSigSum = _FnNidsIdpSigSum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1, 2),
    _FnNidsIdpSigSum_Type()
)
fnNidsIdpSigSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsIdpSigSum.setStatus("mandatory")
_FnNidsIdpSigProto_Type = DisplayString
_FnNidsIdpSigProto_Object = MibTableColumn
fnNidsIdpSigProto = _FnNidsIdpSigProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1, 3),
    _FnNidsIdpSigProto_Type()
)
fnNidsIdpSigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsIdpSigProto.setStatus("mandatory")
_FnNidsIdpSigState_Type = ItemState
_FnNidsIdpSigState_Object = MibTableColumn
fnNidsIdpSigState = _FnNidsIdpSigState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1, 4),
    _FnNidsIdpSigState_Type()
)
fnNidsIdpSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsIdpSigState.setStatus("mandatory")
_FnNidsIdpSigThreshold_Type = Integer32
_FnNidsIdpSigThreshold_Object = MibTableColumn
fnNidsIdpSigThreshold = _FnNidsIdpSigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1, 5),
    _FnNidsIdpSigThreshold_Type()
)
fnNidsIdpSigThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsIdpSigThreshold.setStatus("mandatory")
_FnNidsIdpSigQSize_Type = Integer32
_FnNidsIdpSigQSize_Object = MibTableColumn
fnNidsIdpSigQSize = _FnNidsIdpSigQSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1, 6),
    _FnNidsIdpSigQSize_Type()
)
fnNidsIdpSigQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsIdpSigQSize.setStatus("mandatory")
_FnNidsIdpSigKeepAlive_Type = Integer32
_FnNidsIdpSigKeepAlive_Object = MibTableColumn
fnNidsIdpSigKeepAlive = _FnNidsIdpSigKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 2, 2, 1, 7),
    _FnNidsIdpSigKeepAlive_Type()
)
fnNidsIdpSigKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsIdpSigKeepAlive.setStatus("mandatory")
_FnNidsResponse_ObjectIdentity = ObjectIdentity
fnNidsResponse = _FnNidsResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3)
)


class _FnNidsRespCfg_Type(Integer32):
    """Custom type fnNidsRespCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("tcp", 2))
    )


_FnNidsRespCfg_Type.__name__ = "Integer32"
_FnNidsRespCfg_Object = MibScalar
fnNidsRespCfg = _FnNidsRespCfg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3, 1),
    _FnNidsRespCfg_Type()
)
fnNidsRespCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsRespCfg.setStatus("mandatory")


class _FnNidsRespAlertMsg_Type(Integer32):
    """Custom type fnNidsRespAlertMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("summary", 1))
    )


_FnNidsRespAlertMsg_Type.__name__ = "Integer32"
_FnNidsRespAlertMsg_Object = MibScalar
fnNidsRespAlertMsg = _FnNidsRespAlertMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3, 2),
    _FnNidsRespAlertMsg_Type()
)
fnNidsRespAlertMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsRespAlertMsg.setStatus("mandatory")
_FnNidsRespAlertSrcAddrState_Type = ItemState
_FnNidsRespAlertSrcAddrState_Object = MibScalar
fnNidsRespAlertSrcAddrState = _FnNidsRespAlertSrcAddrState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3, 3),
    _FnNidsRespAlertSrcAddrState_Type()
)
fnNidsRespAlertSrcAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsRespAlertSrcAddrState.setStatus("mandatory")
_FnNidsRespAlertDstAddrState_Type = ItemState
_FnNidsRespAlertDstAddrState_Object = MibScalar
fnNidsRespAlertDstAddrState = _FnNidsRespAlertDstAddrState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3, 4),
    _FnNidsRespAlertDstAddrState_Type()
)
fnNidsRespAlertDstAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsRespAlertDstAddrState.setStatus("mandatory")


class _FnNidsRespLogMsg_Type(Integer32):
    """Custom type fnNidsRespLogMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("summary", 1))
    )


_FnNidsRespLogMsg_Type.__name__ = "Integer32"
_FnNidsRespLogMsg_Object = MibScalar
fnNidsRespLogMsg = _FnNidsRespLogMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3, 5),
    _FnNidsRespLogMsg_Type()
)
fnNidsRespLogMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsRespLogMsg.setStatus("mandatory")
_FnNidsRespLogSrcAddrState_Type = ItemState
_FnNidsRespLogSrcAddrState_Object = MibScalar
fnNidsRespLogSrcAddrState = _FnNidsRespLogSrcAddrState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3, 6),
    _FnNidsRespLogSrcAddrState_Type()
)
fnNidsRespLogSrcAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsRespLogSrcAddrState.setStatus("mandatory")
_FnNidsRespLogDstAddrState_Type = ItemState
_FnNidsRespLogDstAddrState_Object = MibScalar
fnNidsRespLogDstAddrState = _FnNidsRespLogDstAddrState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 5, 3, 7),
    _FnNidsRespLogDstAddrState_Type()
)
fnNidsRespLogDstAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNidsRespLogDstAddrState.setStatus("mandatory")
_FnAntiVirus_ObjectIdentity = ObjectIdentity
fnAntiVirus = _FnAntiVirus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 6)
)
_FnAvFileBlock_ObjectIdentity = ObjectIdentity
fnAvFileBlock = _FnAvFileBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1)
)
_FnAvFileBlkRuleTable_Object = MibTable
fnAvFileBlkRuleTable = _FnAvFileBlkRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fnAvFileBlkRuleTable.setStatus("mandatory")
_FnAvFileBlkRuleEntry_Object = MibTableRow
fnAvFileBlkRuleEntry = _FnAvFileBlkRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1)
)
fnAvFileBlkRuleEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnAvFbRuleIndex"),
)
if mibBuilder.loadTexts:
    fnAvFileBlkRuleEntry.setStatus("mandatory")


class _FnAvFbRuleIndex_Type(Integer32):
    """Custom type fnAvFbRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnAvFbRuleIndex_Type.__name__ = "Integer32"
_FnAvFbRuleIndex_Object = MibTableColumn
fnAvFbRuleIndex = _FnAvFbRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1, 1),
    _FnAvFbRuleIndex_Type()
)
fnAvFbRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAvFbRuleIndex.setStatus("mandatory")


class _FnAvFbRuleFilePat_Type(DisplayString):
    """Custom type fnAvFbRuleFilePat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnAvFbRuleFilePat_Type.__name__ = "DisplayString"
_FnAvFbRuleFilePat_Object = MibTableColumn
fnAvFbRuleFilePat = _FnAvFbRuleFilePat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1, 2),
    _FnAvFbRuleFilePat_Type()
)
fnAvFbRuleFilePat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFbRuleFilePat.setStatus("mandatory")
_FnAvFbRuleHttpBlk_Type = ItemState
_FnAvFbRuleHttpBlk_Object = MibTableColumn
fnAvFbRuleHttpBlk = _FnAvFbRuleHttpBlk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1, 4),
    _FnAvFbRuleHttpBlk_Type()
)
fnAvFbRuleHttpBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFbRuleHttpBlk.setStatus("mandatory")
_FnAvFbRuleFtpBlk_Type = ItemState
_FnAvFbRuleFtpBlk_Object = MibTableColumn
fnAvFbRuleFtpBlk = _FnAvFbRuleFtpBlk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1, 5),
    _FnAvFbRuleFtpBlk_Type()
)
fnAvFbRuleFtpBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFbRuleFtpBlk.setStatus("mandatory")
_FnAvFbRuleSmtpBlk_Type = ItemState
_FnAvFbRuleSmtpBlk_Object = MibTableColumn
fnAvFbRuleSmtpBlk = _FnAvFbRuleSmtpBlk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1, 6),
    _FnAvFbRuleSmtpBlk_Type()
)
fnAvFbRuleSmtpBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFbRuleSmtpBlk.setStatus("mandatory")
_FnAvFbRulePop3Blk_Type = ItemState
_FnAvFbRulePop3Blk_Object = MibTableColumn
fnAvFbRulePop3Blk = _FnAvFbRulePop3Blk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1, 9),
    _FnAvFbRulePop3Blk_Type()
)
fnAvFbRulePop3Blk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFbRulePop3Blk.setStatus("mandatory")
_FnAvFbRuleImapBlk_Type = ItemState
_FnAvFbRuleImapBlk_Object = MibTableColumn
fnAvFbRuleImapBlk = _FnAvFbRuleImapBlk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 1, 1, 1, 12),
    _FnAvFbRuleImapBlk_Type()
)
fnAvFbRuleImapBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFbRuleImapBlk.setStatus("mandatory")
_FnAvQuatantine_ObjectIdentity = ObjectIdentity
fnAvQuatantine = _FnAvQuatantine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2)
)
_FnAvQuarantineTable_Object = MibTable
fnAvQuarantineTable = _FnAvQuarantineTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1)
)
if mibBuilder.loadTexts:
    fnAvQuarantineTable.setStatus("mandatory")
_FnAvQuarantineEntry_Object = MibTableRow
fnAvQuarantineEntry = _FnAvQuarantineEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1)
)
fnAvQuarantineEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnAvQuarIndex"),
)
if mibBuilder.loadTexts:
    fnAvQuarantineEntry.setStatus("mandatory")


class _FnAvQuarIndex_Type(Integer32):
    """Custom type fnAvQuarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnAvQuarIndex_Type.__name__ = "Integer32"
_FnAvQuarIndex_Object = MibTableColumn
fnAvQuarIndex = _FnAvQuarIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 1),
    _FnAvQuarIndex_Type()
)
fnAvQuarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAvQuarIndex.setStatus("mandatory")
_FnAvQuarFileName_Type = DisplayString
_FnAvQuarFileName_Object = MibTableColumn
fnAvQuarFileName = _FnAvQuarFileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 2),
    _FnAvQuarFileName_Type()
)
fnAvQuarFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarFileName.setStatus("mandatory")
_FnAvQuarTime_Type = DisplayString
_FnAvQuarTime_Object = MibTableColumn
fnAvQuarTime = _FnAvQuarTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 3),
    _FnAvQuarTime_Type()
)
fnAvQuarTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarTime.setStatus("mandatory")
_FnAvQuarService_Type = DisplayString
_FnAvQuarService_Object = MibTableColumn
fnAvQuarService = _FnAvQuarService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 4),
    _FnAvQuarService_Type()
)
fnAvQuarService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarService.setStatus("mandatory")
_FnAvQuarStatus_Type = DisplayString
_FnAvQuarStatus_Object = MibTableColumn
fnAvQuarStatus = _FnAvQuarStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 5),
    _FnAvQuarStatus_Type()
)
fnAvQuarStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarStatus.setStatus("mandatory")
_FnAvQuarStatusDetail_Type = Integer32
_FnAvQuarStatusDetail_Object = MibTableColumn
fnAvQuarStatusDetail = _FnAvQuarStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 6),
    _FnAvQuarStatusDetail_Type()
)
fnAvQuarStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarStatusDetail.setStatus("mandatory")
_FnAvQuarDc_Type = DisplayString
_FnAvQuarDc_Object = MibTableColumn
fnAvQuarDc = _FnAvQuarDc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 7),
    _FnAvQuarDc_Type()
)
fnAvQuarDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarDc.setStatus("mandatory")
_FnAvQuarTtl_Type = Integer32
_FnAvQuarTtl_Object = MibTableColumn
fnAvQuarTtl = _FnAvQuarTtl_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 1, 1, 8),
    _FnAvQuarTtl_Type()
)
fnAvQuarTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarTtl.setStatus("mandatory")
_FnAvQuarantineCfg_ObjectIdentity = ObjectIdentity
fnAvQuarantineCfg = _FnAvQuarantineCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2)
)
_FnAvQuarCfgInfecFileHttp_Type = ItemState
_FnAvQuarCfgInfecFileHttp_Object = MibScalar
fnAvQuarCfgInfecFileHttp = _FnAvQuarCfgInfecFileHttp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 1),
    _FnAvQuarCfgInfecFileHttp_Type()
)
fnAvQuarCfgInfecFileHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgInfecFileHttp.setStatus("mandatory")
_FnAvQuarCfgInfecFileFtp_Type = ItemState
_FnAvQuarCfgInfecFileFtp_Object = MibScalar
fnAvQuarCfgInfecFileFtp = _FnAvQuarCfgInfecFileFtp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 2),
    _FnAvQuarCfgInfecFileFtp_Type()
)
fnAvQuarCfgInfecFileFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgInfecFileFtp.setStatus("mandatory")
_FnAvQuarCfgInfecFileImap_Type = ItemState
_FnAvQuarCfgInfecFileImap_Object = MibScalar
fnAvQuarCfgInfecFileImap = _FnAvQuarCfgInfecFileImap_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 3),
    _FnAvQuarCfgInfecFileImap_Type()
)
fnAvQuarCfgInfecFileImap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgInfecFileImap.setStatus("mandatory")
_FnAvQuarCfgInfecFilePop3_Type = ItemState
_FnAvQuarCfgInfecFilePop3_Object = MibScalar
fnAvQuarCfgInfecFilePop3 = _FnAvQuarCfgInfecFilePop3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 4),
    _FnAvQuarCfgInfecFilePop3_Type()
)
fnAvQuarCfgInfecFilePop3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgInfecFilePop3.setStatus("mandatory")
_FnAvQuarCfgInfecFileSmtp_Type = ItemState
_FnAvQuarCfgInfecFileSmtp_Object = MibScalar
fnAvQuarCfgInfecFileSmtp = _FnAvQuarCfgInfecFileSmtp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 5),
    _FnAvQuarCfgInfecFileSmtp_Type()
)
fnAvQuarCfgInfecFileSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgInfecFileSmtp.setStatus("mandatory")
_FnAvQuarCfgBlkFileHttp_Type = ItemState
_FnAvQuarCfgBlkFileHttp_Object = MibScalar
fnAvQuarCfgBlkFileHttp = _FnAvQuarCfgBlkFileHttp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 6),
    _FnAvQuarCfgBlkFileHttp_Type()
)
fnAvQuarCfgBlkFileHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgBlkFileHttp.setStatus("mandatory")
_FnAvQuarCfgBlkFileFtp_Type = ItemState
_FnAvQuarCfgBlkFileFtp_Object = MibScalar
fnAvQuarCfgBlkFileFtp = _FnAvQuarCfgBlkFileFtp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 7),
    _FnAvQuarCfgBlkFileFtp_Type()
)
fnAvQuarCfgBlkFileFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgBlkFileFtp.setStatus("mandatory")
_FnAvQuarCfgBlkFileImap_Type = ItemState
_FnAvQuarCfgBlkFileImap_Object = MibScalar
fnAvQuarCfgBlkFileImap = _FnAvQuarCfgBlkFileImap_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 8),
    _FnAvQuarCfgBlkFileImap_Type()
)
fnAvQuarCfgBlkFileImap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgBlkFileImap.setStatus("mandatory")
_FnAvQuarCfgBlkFilePop3_Type = ItemState
_FnAvQuarCfgBlkFilePop3_Object = MibScalar
fnAvQuarCfgBlkFilePop3 = _FnAvQuarCfgBlkFilePop3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 9),
    _FnAvQuarCfgBlkFilePop3_Type()
)
fnAvQuarCfgBlkFilePop3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgBlkFilePop3.setStatus("mandatory")
_FnAvQuarCfgBlkFileSmtp_Type = ItemState
_FnAvQuarCfgBlkFileSmtp_Object = MibScalar
fnAvQuarCfgBlkFileSmtp = _FnAvQuarCfgBlkFileSmtp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 10),
    _FnAvQuarCfgBlkFileSmtp_Type()
)
fnAvQuarCfgBlkFileSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgBlkFileSmtp.setStatus("mandatory")
_FnAvQuarCfgAgeLimit_Type = Integer32
_FnAvQuarCfgAgeLimit_Object = MibScalar
fnAvQuarCfgAgeLimit = _FnAvQuarCfgAgeLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 11),
    _FnAvQuarCfgAgeLimit_Type()
)
fnAvQuarCfgAgeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgAgeLimit.setStatus("mandatory")


class _FnAvQuarCfgMaxFileSize_Type(Integer32):
    """Custom type fnAvQuarCfgMaxFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FnAvQuarCfgMaxFileSize_Type.__name__ = "Integer32"
_FnAvQuarCfgMaxFileSize_Object = MibScalar
fnAvQuarCfgMaxFileSize = _FnAvQuarCfgMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 12),
    _FnAvQuarCfgMaxFileSize_Type()
)
fnAvQuarCfgMaxFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgMaxFileSize.setStatus("mandatory")


class _FnAvQuarCfgLowDiskOpt_Type(Integer32):
    """Custom type fnAvQuarCfgLowDiskOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropNewFile", 2),
          ("overwriteOldestFile", 1))
    )


_FnAvQuarCfgLowDiskOpt_Type.__name__ = "Integer32"
_FnAvQuarCfgLowDiskOpt_Object = MibScalar
fnAvQuarCfgLowDiskOpt = _FnAvQuarCfgLowDiskOpt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 2, 2, 13),
    _FnAvQuarCfgLowDiskOpt_Type()
)
fnAvQuarCfgLowDiskOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvQuarCfgLowDiskOpt.setStatus("mandatory")
_FnAVConfig_ObjectIdentity = ObjectIdentity
fnAVConfig = _FnAVConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3)
)
_FnAVVirusListTable_Object = MibTable
fnAVVirusListTable = _FnAVVirusListTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 1)
)
if mibBuilder.loadTexts:
    fnAVVirusListTable.setStatus("mandatory")
_FnAVVirusListEntry_Object = MibTableRow
fnAVVirusListEntry = _FnAVVirusListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 1, 1)
)
fnAVVirusListEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnAvVirusIndex"),
)
if mibBuilder.loadTexts:
    fnAVVirusListEntry.setStatus("mandatory")


class _FnAvVirusIndex_Type(Integer32):
    """Custom type fnAvVirusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnAvVirusIndex_Type.__name__ = "Integer32"
_FnAvVirusIndex_Object = MibTableColumn
fnAvVirusIndex = _FnAvVirusIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 1, 1, 1),
    _FnAvVirusIndex_Type()
)
fnAvVirusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAvVirusIndex.setStatus("mandatory")
_FnAvVirusName_Type = Integer32
_FnAvVirusName_Object = MibTableColumn
fnAvVirusName = _FnAvVirusName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 1, 1, 2),
    _FnAvVirusName_Type()
)
fnAvVirusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvVirusName.setStatus("mandatory")
_FnAvCfgMsgTable_Object = MibTable
fnAvCfgMsgTable = _FnAvCfgMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 2)
)
if mibBuilder.loadTexts:
    fnAvCfgMsgTable.setStatus("mandatory")
_FnAvCfgMsgEntry_Object = MibTableRow
fnAvCfgMsgEntry = _FnAvCfgMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 2, 1)
)
fnAvCfgMsgEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnAvCfgMsgIndex"),
)
if mibBuilder.loadTexts:
    fnAvCfgMsgEntry.setStatus("mandatory")


class _FnAvCfgMsgIndex_Type(Integer32):
    """Custom type fnAvCfgMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnAvCfgMsgIndex_Type.__name__ = "Integer32"
_FnAvCfgMsgIndex_Object = MibTableColumn
fnAvCfgMsgIndex = _FnAvCfgMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 2, 1, 1),
    _FnAvCfgMsgIndex_Type()
)
fnAvCfgMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAvCfgMsgIndex.setStatus("mandatory")
_FnAvCfgMsgName_Type = DisplayString
_FnAvCfgMsgName_Object = MibTableColumn
fnAvCfgMsgName = _FnAvCfgMsgName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 2, 1, 2),
    _FnAvCfgMsgName_Type()
)
fnAvCfgMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgMsgName.setStatus("mandatory")
_FnAvCfgMsgService_Type = DisplayString
_FnAvCfgMsgService_Object = MibTableColumn
fnAvCfgMsgService = _FnAvCfgMsgService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 2, 1, 3),
    _FnAvCfgMsgService_Type()
)
fnAvCfgMsgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgMsgService.setStatus("mandatory")
_FnAvCfgMsgDescription_Type = DisplayString
_FnAvCfgMsgDescription_Object = MibTableColumn
fnAvCfgMsgDescription = _FnAvCfgMsgDescription_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 2, 1, 4),
    _FnAvCfgMsgDescription_Type()
)
fnAvCfgMsgDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgMsgDescription.setStatus("mandatory")


class _FnAvCfgBlkFileHttp_Type(Integer32):
    """Custom type fnAvCfgBlkFileHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnAvCfgBlkFileHttp_Type.__name__ = "Integer32"
_FnAvCfgBlkFileHttp_Object = MibScalar
fnAvCfgBlkFileHttp = _FnAvCfgBlkFileHttp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 5),
    _FnAvCfgBlkFileHttp_Type()
)
fnAvCfgBlkFileHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgBlkFileHttp.setStatus("mandatory")


class _FnAvCfgBlkFileFtp_Type(Integer32):
    """Custom type fnAvCfgBlkFileFtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnAvCfgBlkFileFtp_Type.__name__ = "Integer32"
_FnAvCfgBlkFileFtp_Object = MibScalar
fnAvCfgBlkFileFtp = _FnAvCfgBlkFileFtp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 6),
    _FnAvCfgBlkFileFtp_Type()
)
fnAvCfgBlkFileFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgBlkFileFtp.setStatus("mandatory")


class _FnAvCfgBlkEmailImap_Type(Integer32):
    """Custom type fnAvCfgBlkEmailImap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnAvCfgBlkEmailImap_Type.__name__ = "Integer32"
_FnAvCfgBlkEmailImap_Object = MibScalar
fnAvCfgBlkEmailImap = _FnAvCfgBlkEmailImap_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 7),
    _FnAvCfgBlkEmailImap_Type()
)
fnAvCfgBlkEmailImap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgBlkEmailImap.setStatus("mandatory")


class _FnAvCfgBlkEmailPop3_Type(Integer32):
    """Custom type fnAvCfgBlkEmailPop3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnAvCfgBlkEmailPop3_Type.__name__ = "Integer32"
_FnAvCfgBlkEmailPop3_Object = MibScalar
fnAvCfgBlkEmailPop3 = _FnAvCfgBlkEmailPop3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 8),
    _FnAvCfgBlkEmailPop3_Type()
)
fnAvCfgBlkEmailPop3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgBlkEmailPop3.setStatus("mandatory")


class _FnAvCfgBlkEmailSmtp_Type(Integer32):
    """Custom type fnAvCfgBlkEmailSmtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnAvCfgBlkEmailSmtp_Type.__name__ = "Integer32"
_FnAvCfgBlkEmailSmtp_Object = MibScalar
fnAvCfgBlkEmailSmtp = _FnAvCfgBlkEmailSmtp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 6, 3, 9),
    _FnAvCfgBlkEmailSmtp_Type()
)
fnAvCfgBlkEmailSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvCfgBlkEmailSmtp.setStatus("mandatory")
_FnWebFilter_ObjectIdentity = ObjectIdentity
fnWebFilter = _FnWebFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 7)
)
_FnWebFilterBWords_ObjectIdentity = ObjectIdentity
fnWebFilterBWords = _FnWebFilterBWords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 7, 1)
)
_FnWebFilterBannedWordsTable_Object = MibTable
fnWebFilterBannedWordsTable = _FnWebFilterBannedWordsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 1, 1)
)
if mibBuilder.loadTexts:
    fnWebFilterBannedWordsTable.setStatus("mandatory")
_FnWebfilterBannedWordsEntry_Object = MibTableRow
fnWebfilterBannedWordsEntry = _FnWebfilterBannedWordsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 1, 1, 1)
)
fnWebfilterBannedWordsEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnWebFilterBannedWordIndex"),
)
if mibBuilder.loadTexts:
    fnWebfilterBannedWordsEntry.setStatus("mandatory")


class _FnWebFilterBannedWordIndex_Type(Integer32):
    """Custom type fnWebFilterBannedWordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnWebFilterBannedWordIndex_Type.__name__ = "Integer32"
_FnWebFilterBannedWordIndex_Object = MibTableColumn
fnWebFilterBannedWordIndex = _FnWebFilterBannedWordIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 1, 1, 1, 1),
    _FnWebFilterBannedWordIndex_Type()
)
fnWebFilterBannedWordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnWebFilterBannedWordIndex.setStatus("mandatory")
_FnWebFilterBannedWords_Type = DisplayString
_FnWebFilterBannedWords_Object = MibTableColumn
fnWebFilterBannedWords = _FnWebFilterBannedWords_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 1, 1, 1, 2),
    _FnWebFilterBannedWords_Type()
)
fnWebFilterBannedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterBannedWords.setStatus("mandatory")
_FnWebFilterBannedWordLan_Type = LanguageCode
_FnWebFilterBannedWordLan_Object = MibTableColumn
fnWebFilterBannedWordLan = _FnWebFilterBannedWordLan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 1, 1, 1, 3),
    _FnWebFilterBannedWordLan_Type()
)
fnWebFilterBannedWordLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterBannedWordLan.setStatus("mandatory")
_FnWebFilterBannedWordState_Type = ItemState
_FnWebFilterBannedWordState_Object = MibTableColumn
fnWebFilterBannedWordState = _FnWebFilterBannedWordState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 1, 1, 1, 4),
    _FnWebFilterBannedWordState_Type()
)
fnWebFilterBannedWordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterBannedWordState.setStatus("mandatory")
_FnWebFilterUrlBlk_ObjectIdentity = ObjectIdentity
fnWebFilterUrlBlk = _FnWebFilterUrlBlk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 7, 2)
)
_FnWebFilterUrlBlkState_Type = ItemState
_FnWebFilterUrlBlkState_Object = MibScalar
fnWebFilterUrlBlkState = _FnWebFilterUrlBlkState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 2, 1),
    _FnWebFilterUrlBlkState_Type()
)
fnWebFilterUrlBlkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterUrlBlkState.setStatus("mandatory")
_FnWebFilterUrlBlkTable_Object = MibTable
fnWebFilterUrlBlkTable = _FnWebFilterUrlBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 2, 2)
)
if mibBuilder.loadTexts:
    fnWebFilterUrlBlkTable.setStatus("mandatory")
_FnWebFilterUrlBlkEntry_Object = MibTableRow
fnWebFilterUrlBlkEntry = _FnWebFilterUrlBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 2, 2, 1)
)
fnWebFilterUrlBlkEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnWebFilterUrlBlkIndex"),
)
if mibBuilder.loadTexts:
    fnWebFilterUrlBlkEntry.setStatus("mandatory")


class _FnWebFilterUrlBlkIndex_Type(Integer32):
    """Custom type fnWebFilterUrlBlkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnWebFilterUrlBlkIndex_Type.__name__ = "Integer32"
_FnWebFilterUrlBlkIndex_Object = MibTableColumn
fnWebFilterUrlBlkIndex = _FnWebFilterUrlBlkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 2, 2, 1, 1),
    _FnWebFilterUrlBlkIndex_Type()
)
fnWebFilterUrlBlkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnWebFilterUrlBlkIndex.setStatus("mandatory")
_FnWebFilterUrlPat_Type = DisplayString
_FnWebFilterUrlPat_Object = MibTableColumn
fnWebFilterUrlPat = _FnWebFilterUrlPat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 2, 2, 1, 2),
    _FnWebFilterUrlPat_Type()
)
fnWebFilterUrlPat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterUrlPat.setStatus("mandatory")
_FnWebFilterUrlState_Type = ItemState
_FnWebFilterUrlState_Object = MibTableColumn
fnWebFilterUrlState = _FnWebFilterUrlState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 2, 2, 1, 3),
    _FnWebFilterUrlState_Type()
)
fnWebFilterUrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterUrlState.setStatus("mandatory")
_FnWebFilterScripts_ObjectIdentity = ObjectIdentity
fnWebFilterScripts = _FnWebFilterScripts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 7, 3)
)
_FnWebFilterApplet_Type = ItemState
_FnWebFilterApplet_Object = MibScalar
fnWebFilterApplet = _FnWebFilterApplet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 3, 1),
    _FnWebFilterApplet_Type()
)
fnWebFilterApplet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterApplet.setStatus("mandatory")
_FnWebFilterCookie_Type = ItemState
_FnWebFilterCookie_Object = MibScalar
fnWebFilterCookie = _FnWebFilterCookie_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 3, 2),
    _FnWebFilterCookie_Type()
)
fnWebFilterCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterCookie.setStatus("mandatory")
_FnWebFilterActiveX_Type = ItemState
_FnWebFilterActiveX_Object = MibScalar
fnWebFilterActiveX = _FnWebFilterActiveX_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 3, 3),
    _FnWebFilterActiveX_Type()
)
fnWebFilterActiveX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterActiveX.setStatus("mandatory")
_FnWebFilterExemptUrl_ObjectIdentity = ObjectIdentity
fnWebFilterExemptUrl = _FnWebFilterExemptUrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 7, 4)
)
_FnWebFilterExemptUrlTable_Object = MibTable
fnWebFilterExemptUrlTable = _FnWebFilterExemptUrlTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 4, 1)
)
if mibBuilder.loadTexts:
    fnWebFilterExemptUrlTable.setStatus("mandatory")
_FnWebFilterExemptUrlEntry_Object = MibTableRow
fnWebFilterExemptUrlEntry = _FnWebFilterExemptUrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 4, 1, 1)
)
fnWebFilterExemptUrlEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnWebFilterExemptUrlIndex"),
)
if mibBuilder.loadTexts:
    fnWebFilterExemptUrlEntry.setStatus("mandatory")


class _FnWebFilterExemptUrlIndex_Type(Integer32):
    """Custom type fnWebFilterExemptUrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnWebFilterExemptUrlIndex_Type.__name__ = "Integer32"
_FnWebFilterExemptUrlIndex_Object = MibTableColumn
fnWebFilterExemptUrlIndex = _FnWebFilterExemptUrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 4, 1, 1, 1),
    _FnWebFilterExemptUrlIndex_Type()
)
fnWebFilterExemptUrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnWebFilterExemptUrlIndex.setStatus("mandatory")
_FnWebFilterExemptUrlPat_Type = DisplayString
_FnWebFilterExemptUrlPat_Object = MibTableColumn
fnWebFilterExemptUrlPat = _FnWebFilterExemptUrlPat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 4, 1, 1, 2),
    _FnWebFilterExemptUrlPat_Type()
)
fnWebFilterExemptUrlPat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterExemptUrlPat.setStatus("mandatory")
_FnWebFilterExemptUrlState_Type = ItemState
_FnWebFilterExemptUrlState_Object = MibTableColumn
fnWebFilterExemptUrlState = _FnWebFilterExemptUrlState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 4, 1, 1, 3),
    _FnWebFilterExemptUrlState_Type()
)
fnWebFilterExemptUrlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWebFilterExemptUrlState.setStatus("mandatory")
_FnWebFilterCfg_ObjectIdentity = ObjectIdentity
fnWebFilterCfg = _FnWebFilterCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 7, 5)
)
_FnWfCfgMsgTable_Object = MibTable
fnWfCfgMsgTable = _FnWfCfgMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 5, 1)
)
if mibBuilder.loadTexts:
    fnWfCfgMsgTable.setStatus("mandatory")
_FnWfCfgMsgEntry_Object = MibTableRow
fnWfCfgMsgEntry = _FnWfCfgMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 5, 1, 1)
)
fnWfCfgMsgEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnWfCfgMsgIndex"),
)
if mibBuilder.loadTexts:
    fnWfCfgMsgEntry.setStatus("mandatory")


class _FnWfCfgMsgIndex_Type(Integer32):
    """Custom type fnWfCfgMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnWfCfgMsgIndex_Type.__name__ = "Integer32"
_FnWfCfgMsgIndex_Object = MibTableColumn
fnWfCfgMsgIndex = _FnWfCfgMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 5, 1, 1, 1),
    _FnWfCfgMsgIndex_Type()
)
fnWfCfgMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnWfCfgMsgIndex.setStatus("mandatory")
_FnWfCfgMsgName_Type = DisplayString
_FnWfCfgMsgName_Object = MibTableColumn
fnWfCfgMsgName = _FnWfCfgMsgName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 5, 1, 1, 2),
    _FnWfCfgMsgName_Type()
)
fnWfCfgMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfCfgMsgName.setStatus("mandatory")
_FnWfCfgMsgService_Type = DisplayString
_FnWfCfgMsgService_Object = MibTableColumn
fnWfCfgMsgService = _FnWfCfgMsgService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 5, 1, 1, 3),
    _FnWfCfgMsgService_Type()
)
fnWfCfgMsgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfCfgMsgService.setStatus("mandatory")
_FnWfCfgMsgDescription_Type = DisplayString
_FnWfCfgMsgDescription_Object = MibTableColumn
fnWfCfgMsgDescription = _FnWfCfgMsgDescription_Object(
    (1, 3, 6, 1, 4, 1, 12356, 7, 5, 1, 1, 4),
    _FnWfCfgMsgDescription_Type()
)
fnWfCfgMsgDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfCfgMsgDescription.setStatus("mandatory")
_FnAntiSpam_ObjectIdentity = ObjectIdentity
fnAntiSpam = _FnAntiSpam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 8)
)
_FnAntiSpamBlkTable_Object = MibTable
fnAntiSpamBlkTable = _FnAntiSpamBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1)
)
if mibBuilder.loadTexts:
    fnAntiSpamBlkTable.setStatus("mandatory")
_FnAntiSpamBlkEntry_Object = MibTableRow
fnAntiSpamBlkEntry = _FnAntiSpamBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1)
)
fnAntiSpamBlkEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnAntiSpamBlkIndex"),
)
if mibBuilder.loadTexts:
    fnAntiSpamBlkEntry.setStatus("mandatory")


class _FnAntiSpamBlkIndex_Type(Integer32):
    """Custom type fnAntiSpamBlkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnAntiSpamBlkIndex_Type.__name__ = "Integer32"
_FnAntiSpamBlkIndex_Object = MibTableColumn
fnAntiSpamBlkIndex = _FnAntiSpamBlkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 1),
    _FnAntiSpamBlkIndex_Type()
)
fnAntiSpamBlkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAntiSpamBlkIndex.setStatus("mandatory")
_FnAntiSpamBlkPat_Type = DisplayString
_FnAntiSpamBlkPat_Object = MibTableColumn
fnAntiSpamBlkPat = _FnAntiSpamBlkPat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 2),
    _FnAntiSpamBlkPat_Type()
)
fnAntiSpamBlkPat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamBlkPat.setStatus("mandatory")
_FnAntiSpamBlkImapState_Type = ItemState
_FnAntiSpamBlkImapState_Object = MibTableColumn
fnAntiSpamBlkImapState = _FnAntiSpamBlkImapState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 3),
    _FnAntiSpamBlkImapState_Type()
)
fnAntiSpamBlkImapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamBlkImapState.setStatus("mandatory")
_FnAntiSpamBlkPop3State_Type = ItemState
_FnAntiSpamBlkPop3State_Object = MibTableColumn
fnAntiSpamBlkPop3State = _FnAntiSpamBlkPop3State_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 4),
    _FnAntiSpamBlkPop3State_Type()
)
fnAntiSpamBlkPop3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamBlkPop3State.setStatus("mandatory")
_FnAntiSpamExemptTable_Object = MibTable
fnAntiSpamExemptTable = _FnAntiSpamExemptTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 2)
)
if mibBuilder.loadTexts:
    fnAntiSpamExemptTable.setStatus("mandatory")
_FnAntiSpamExemptEntry_Object = MibTableRow
fnAntiSpamExemptEntry = _FnAntiSpamExemptEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 2, 1)
)
fnAntiSpamExemptEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnAntiSpamExemptIndex"),
)
if mibBuilder.loadTexts:
    fnAntiSpamExemptEntry.setStatus("mandatory")


class _FnAntiSpamExemptIndex_Type(Integer32):
    """Custom type fnAntiSpamExemptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnAntiSpamExemptIndex_Type.__name__ = "Integer32"
_FnAntiSpamExemptIndex_Object = MibTableColumn
fnAntiSpamExemptIndex = _FnAntiSpamExemptIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 2, 1, 1),
    _FnAntiSpamExemptIndex_Type()
)
fnAntiSpamExemptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAntiSpamExemptIndex.setStatus("mandatory")
_FnAntiSpamBanWordPat_Type = DisplayString
_FnAntiSpamBanWordPat_Object = MibTableColumn
fnAntiSpamBanWordPat = _FnAntiSpamBanWordPat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 2, 1, 2),
    _FnAntiSpamBanWordPat_Type()
)
fnAntiSpamBanWordPat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamBanWordPat.setStatus("mandatory")
_FnAntiSpamExemptImapState_Type = ItemState
_FnAntiSpamExemptImapState_Object = MibTableColumn
fnAntiSpamExemptImapState = _FnAntiSpamExemptImapState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 2, 1, 3),
    _FnAntiSpamExemptImapState_Type()
)
fnAntiSpamExemptImapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamExemptImapState.setStatus("mandatory")
_FnAntiSpamExemptPop3State_Type = ItemState
_FnAntiSpamExemptPop3State_Object = MibTableColumn
fnAntiSpamExemptPop3State = _FnAntiSpamExemptPop3State_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 2, 1, 4),
    _FnAntiSpamExemptPop3State_Type()
)
fnAntiSpamExemptPop3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamExemptPop3State.setStatus("mandatory")
_FnAntiSpamBanWordTable_Object = MibTable
fnAntiSpamBanWordTable = _FnAntiSpamBanWordTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 3)
)
if mibBuilder.loadTexts:
    fnAntiSpamBanWordTable.setStatus("mandatory")
_FnAntiSpamBanWordEntry_Object = MibTableRow
fnAntiSpamBanWordEntry = _FnAntiSpamBanWordEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 3, 1)
)
fnAntiSpamBanWordEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnAntiSpamBanWordIndex"),
)
if mibBuilder.loadTexts:
    fnAntiSpamBanWordEntry.setStatus("mandatory")


class _FnAntiSpamBanWordIndex_Type(Integer32):
    """Custom type fnAntiSpamBanWordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnAntiSpamBanWordIndex_Type.__name__ = "Integer32"
_FnAntiSpamBanWordIndex_Object = MibTableColumn
fnAntiSpamBanWordIndex = _FnAntiSpamBanWordIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 3, 1, 1),
    _FnAntiSpamBanWordIndex_Type()
)
fnAntiSpamBanWordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAntiSpamBanWordIndex.setStatus("mandatory")
_FnAntiSpamBanWordImapState_Type = ItemState
_FnAntiSpamBanWordImapState_Object = MibTableColumn
fnAntiSpamBanWordImapState = _FnAntiSpamBanWordImapState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 3, 1, 3),
    _FnAntiSpamBanWordImapState_Type()
)
fnAntiSpamBanWordImapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamBanWordImapState.setStatus("mandatory")
_FnAntiSpamBanWordPop3State_Type = ItemState
_FnAntiSpamBanWordPop3State_Object = MibTableColumn
fnAntiSpamBanWordPop3State = _FnAntiSpamBanWordPop3State_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 3, 1, 4),
    _FnAntiSpamBanWordPop3State_Type()
)
fnAntiSpamBanWordPop3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamBanWordPop3State.setStatus("mandatory")
_FnAntiSpamCfgSubTag_Type = DisplayString
_FnAntiSpamCfgSubTag_Object = MibScalar
fnAntiSpamCfgSubTag = _FnAntiSpamCfgSubTag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 4),
    _FnAntiSpamCfgSubTag_Type()
)
fnAntiSpamCfgSubTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAntiSpamCfgSubTag.setStatus("mandatory")
_FnLogAndRpt_ObjectIdentity = ObjectIdentity
fnLogAndRpt = _FnLogAndRpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9)
)
_FnLogSetting_ObjectIdentity = ObjectIdentity
fnLogSetting = _FnLogSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1)
)
_FnLogToRemHostState_Type = ItemState
_FnLogToRemHostState_Object = MibScalar
fnLogToRemHostState = _FnLogToRemHostState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1),
    _FnLogToRemHostState_Type()
)
fnLogToRemHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToRemHostState.setStatus("mandatory")
_FnLogToRemHostAddr_Type = IpAddress
_FnLogToRemHostAddr_Object = MibScalar
fnLogToRemHostAddr = _FnLogToRemHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 2),
    _FnLogToRemHostAddr_Type()
)
fnLogToRemHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToRemHostAddr.setStatus("mandatory")
_FnLogToWebtrendsSrvState_Type = ItemState
_FnLogToWebtrendsSrvState_Object = MibScalar
fnLogToWebtrendsSrvState = _FnLogToWebtrendsSrvState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 3),
    _FnLogToWebtrendsSrvState_Type()
)
fnLogToWebtrendsSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToWebtrendsSrvState.setStatus("mandatory")
_FnLogToWebtrendsSrvAddr_Type = IpAddress
_FnLogToWebtrendsSrvAddr_Object = MibScalar
fnLogToWebtrendsSrvAddr = _FnLogToWebtrendsSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 4),
    _FnLogToWebtrendsSrvAddr_Type()
)
fnLogToWebtrendsSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToWebtrendsSrvAddr.setStatus("mandatory")
_FnLogToLocalState_Type = ItemState
_FnLogToLocalState_Object = MibScalar
fnLogToLocalState = _FnLogToLocalState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 5),
    _FnLogToLocalState_Type()
)
fnLogToLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToLocalState.setStatus("mandatory")
_FnLogTrafficIntToFw_Type = ItemState
_FnLogTrafficIntToFw_Object = MibScalar
fnLogTrafficIntToFw = _FnLogTrafficIntToFw_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 6),
    _FnLogTrafficIntToFw_Type()
)
fnLogTrafficIntToFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogTrafficIntToFw.setStatus("mandatory")
_FnLogTrafficExtToFw_Type = ItemState
_FnLogTrafficExtToFw_Object = MibScalar
fnLogTrafficExtToFw = _FnLogTrafficExtToFw_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 7),
    _FnLogTrafficExtToFw_Type()
)
fnLogTrafficExtToFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogTrafficExtToFw.setStatus("mandatory")
_FnLogAllEvents_Type = ItemState
_FnLogAllEvents_Object = MibScalar
fnLogAllEvents = _FnLogAllEvents_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 8),
    _FnLogAllEvents_Type()
)
fnLogAllEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogAllEvents.setStatus("mandatory")
_FnLogVirusEvents_Type = ItemState
_FnLogVirusEvents_Object = MibScalar
fnLogVirusEvents = _FnLogVirusEvents_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 9),
    _FnLogVirusEvents_Type()
)
fnLogVirusEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogVirusEvents.setStatus("mandatory")
_FnLogIntrusions_Type = ItemState
_FnLogIntrusions_Object = MibScalar
fnLogIntrusions = _FnLogIntrusions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 10),
    _FnLogIntrusions_Type()
)
fnLogIntrusions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogIntrusions.setStatus("mandatory")


class _FnLogToLocalFileSize_Type(Integer32):
    """Custom type fnLogToLocalFileSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_FnLogToLocalFileSize_Type.__name__ = "Integer32"
_FnLogToLocalFileSize_Object = MibScalar
fnLogToLocalFileSize = _FnLogToLocalFileSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 11),
    _FnLogToLocalFileSize_Type()
)
fnLogToLocalFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToLocalFileSize.setStatus("mandatory")


class _FnLogToLocalTime_Type(Integer32):
    """Custom type fnLogToLocalTime based on Integer32"""
    defaultValue = 10


_FnLogToLocalTime_Object = MibScalar
fnLogToLocalTime = _FnLogToLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 12),
    _FnLogToLocalTime_Type()
)
fnLogToLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToLocalTime.setStatus("mandatory")


class _FnLogToLocalOpt_Type(Integer32):
    """Custom type fnLogToLocalOpt based on Integer32"""
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
        *(("blockTraffic", 2),
          ("doNotLog", 3),
          ("overWrite", 1))
    )


_FnLogToLocalOpt_Type.__name__ = "Integer32"
_FnLogToLocalOpt_Object = MibScalar
fnLogToLocalOpt = _FnLogToLocalOpt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 13),
    _FnLogToLocalOpt_Type()
)
fnLogToLocalOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogToLocalOpt.setStatus("mandatory")
_FnLogSettingFilter_ObjectIdentity = ObjectIdentity
fnLogSettingFilter = _FnLogSettingFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14)
)
_FnLogSettingTrafficFilter_ObjectIdentity = ObjectIdentity
fnLogSettingTrafficFilter = _FnLogSettingTrafficFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 1)
)
_FnLSTrafficFilterState_Type = ItemState
_FnLSTrafficFilterState_Object = MibScalar
fnLSTrafficFilterState = _FnLSTrafficFilterState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 1, 1),
    _FnLSTrafficFilterState_Type()
)
fnLSTrafficFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficFilterState.setStatus("mandatory")
_FnLSTrafficFilterType_Type = Integer32
_FnLSTrafficFilterType_Object = MibScalar
fnLSTrafficFilterType = _FnLSTrafficFilterType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 1, 2),
    _FnLSTrafficFilterType_Type()
)
fnLSTrafficFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficFilterType.setStatus("mandatory")


class _FnLSTrafficFilterDisplay_Type(Integer32):
    """Custom type fnLSTrafficFilterDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portNumber", 1),
          ("serviceName", 2))
    )


_FnLSTrafficFilterDisplay_Type.__name__ = "Integer32"
_FnLSTrafficFilterDisplay_Object = MibScalar
fnLSTrafficFilterDisplay = _FnLSTrafficFilterDisplay_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 1, 3),
    _FnLSTrafficFilterDisplay_Type()
)
fnLSTrafficFilterDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficFilterDisplay.setStatus("mandatory")
_FnLSTrafficFilterResolveIp_Type = ItemState
_FnLSTrafficFilterResolveIp_Object = MibScalar
fnLSTrafficFilterResolveIp = _FnLSTrafficFilterResolveIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 1, 4),
    _FnLSTrafficFilterResolveIp_Type()
)
fnLSTrafficFilterResolveIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficFilterResolveIp.setStatus("mandatory")
_FnLogSettingEventFilter_ObjectIdentity = ObjectIdentity
fnLogSettingEventFilter = _FnLogSettingEventFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2)
)
_FnLSEventFilterCfgChg_Type = ItemState
_FnLSEventFilterCfgChg_Object = MibScalar
fnLSEventFilterCfgChg = _FnLSEventFilterCfgChg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 1),
    _FnLSEventFilterCfgChg_Type()
)
fnLSEventFilterCfgChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterCfgChg.setStatus("mandatory")
_FnLSEventFilterIpsecNeg_Type = ItemState
_FnLSEventFilterIpsecNeg_Object = MibScalar
fnLSEventFilterIpsecNeg = _FnLSEventFilterIpsecNeg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 2),
    _FnLSEventFilterIpsecNeg_Type()
)
fnLSEventFilterIpsecNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterIpsecNeg.setStatus("mandatory")
_FnLSEventFilterDhcpService_Type = ItemState
_FnLSEventFilterDhcpService_Object = MibScalar
fnLSEventFilterDhcpService = _FnLSEventFilterDhcpService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 3),
    _FnLSEventFilterDhcpService_Type()
)
fnLSEventFilterDhcpService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterDhcpService.setStatus("mandatory")
_FnLSEventFilterPppoeService_Type = ItemState
_FnLSEventFilterPppoeService_Object = MibScalar
fnLSEventFilterPppoeService = _FnLSEventFilterPppoeService_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 4),
    _FnLSEventFilterPppoeService_Type()
)
fnLSEventFilterPppoeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterPppoeService.setStatus("mandatory")
_FnLSEventFilterAdminLogin_Type = ItemState
_FnLSEventFilterAdminLogin_Object = MibScalar
fnLSEventFilterAdminLogin = _FnLSEventFilterAdminLogin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 5),
    _FnLSEventFilterAdminLogin_Type()
)
fnLSEventFilterAdminLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterAdminLogin.setStatus("mandatory")
_FnLSEventFilterIpmacStatus_Type = ItemState
_FnLSEventFilterIpmacStatus_Object = MibScalar
fnLSEventFilterIpmacStatus = _FnLSEventFilterIpmacStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 6),
    _FnLSEventFilterIpmacStatus_Type()
)
fnLSEventFilterIpmacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterIpmacStatus.setStatus("mandatory")
_FnLSEventFilterSysAct_Type = ItemState
_FnLSEventFilterSysAct_Object = MibScalar
fnLSEventFilterSysAct = _FnLSEventFilterSysAct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 7),
    _FnLSEventFilterSysAct_Type()
)
fnLSEventFilterSysAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterSysAct.setStatus("mandatory")
_FnLSEventFilterHaAct_Type = ItemState
_FnLSEventFilterHaAct_Object = MibScalar
fnLSEventFilterHaAct = _FnLSEventFilterHaAct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 8),
    _FnLSEventFilterHaAct_Type()
)
fnLSEventFilterHaAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterHaAct.setStatus("mandatory")
_FnLSEventFilterFwAuth_Type = ItemState
_FnLSEventFilterFwAuth_Object = MibScalar
fnLSEventFilterFwAuth = _FnLSEventFilterFwAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 9),
    _FnLSEventFilterFwAuth_Type()
)
fnLSEventFilterFwAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterFwAuth.setStatus("mandatory")
_FnLSEventFilterGwConn_Type = ItemState
_FnLSEventFilterGwConn_Object = MibScalar
fnLSEventFilterGwConn = _FnLSEventFilterGwConn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 2, 10),
    _FnLSEventFilterGwConn_Type()
)
fnLSEventFilterGwConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSEventFilterGwConn.setStatus("mandatory")
_FnLogSettingVirusFilter_ObjectIdentity = ObjectIdentity
fnLogSettingVirusFilter = _FnLogSettingVirusFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 3)
)
_FnLSVirusFilterDet_Type = ItemState
_FnLSVirusFilterDet_Object = MibScalar
fnLSVirusFilterDet = _FnLSVirusFilterDet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 3, 1),
    _FnLSVirusFilterDet_Type()
)
fnLSVirusFilterDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSVirusFilterDet.setStatus("mandatory")
_FnLSVirusFilterSigUpdate_Type = ItemState
_FnLSVirusFilterSigUpdate_Object = MibScalar
fnLSVirusFilterSigUpdate = _FnLSVirusFilterSigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 3, 2),
    _FnLSVirusFilterSigUpdate_Type()
)
fnLSVirusFilterSigUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSVirusFilterSigUpdate.setStatus("mandatory")
_FnLogSettingWebFilter_ObjectIdentity = ObjectIdentity
fnLogSettingWebFilter = _FnLogSettingWebFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 4)
)
_FnLSWebFilterBanDet_Type = ItemState
_FnLSWebFilterBanDet_Object = MibScalar
fnLSWebFilterBanDet = _FnLSWebFilterBanDet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 4, 1),
    _FnLSWebFilterBanDet_Type()
)
fnLSWebFilterBanDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSWebFilterBanDet.setStatus("mandatory")
_FnLSWebFilterScriptDet_Type = ItemState
_FnLSWebFilterScriptDet_Object = MibScalar
fnLSWebFilterScriptDet = _FnLSWebFilterScriptDet_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 4, 2),
    _FnLSWebFilterScriptDet_Type()
)
fnLSWebFilterScriptDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSWebFilterScriptDet.setStatus("mandatory")
_FnLSWebFilterPageBlk_Type = ItemState
_FnLSWebFilterPageBlk_Object = MibScalar
fnLSWebFilterPageBlk = _FnLSWebFilterPageBlk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 4, 3),
    _FnLSWebFilterPageBlk_Type()
)
fnLSWebFilterPageBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSWebFilterPageBlk.setStatus("mandatory")
_FnLSIdsFilterState_Type = ItemState
_FnLSIdsFilterState_Object = MibScalar
fnLSIdsFilterState = _FnLSIdsFilterState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 5),
    _FnLSIdsFilterState_Type()
)
fnLSIdsFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSIdsFilterState.setStatus("mandatory")


class _FnLSFilterSeverity_Type(Integer32):
    """Custom type fnLSFilterSeverity based on Integer32"""
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
        *(("alert", 3),
          ("critical", 4),
          ("debugging", 9),
          ("emergency", 2),
          ("error", 5),
          ("infomation", 8),
          ("none", 1),
          ("notification", 7),
          ("warning", 6))
    )


_FnLSFilterSeverity_Type.__name__ = "Integer32"
_FnLSFilterSeverity_Object = MibScalar
fnLSFilterSeverity = _FnLSFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 14, 6),
    _FnLSFilterSeverity_Type()
)
fnLSFilterSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSFilterSeverity.setStatus("mandatory")
_FnLSTrafficAddrTable_Object = MibTable
fnLSTrafficAddrTable = _FnLSTrafficAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15)
)
if mibBuilder.loadTexts:
    fnLSTrafficAddrTable.setStatus("mandatory")
_FnLSTrafficAddrEntry_Object = MibTableRow
fnLSTrafficAddrEntry = _FnLSTrafficAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1)
)
fnLSTrafficAddrEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnLSTrafficEntryIndex"),
)
if mibBuilder.loadTexts:
    fnLSTrafficAddrEntry.setStatus("mandatory")


class _FnLSTrafficEntryIndex_Type(Integer32):
    """Custom type fnLSTrafficEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnLSTrafficEntryIndex_Type.__name__ = "Integer32"
_FnLSTrafficEntryIndex_Object = MibTableColumn
fnLSTrafficEntryIndex = _FnLSTrafficEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 1),
    _FnLSTrafficEntryIndex_Type()
)
fnLSTrafficEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnLSTrafficEntryIndex.setStatus("mandatory")
_FnLSTrafficSrcAddr_Type = IpAddress
_FnLSTrafficSrcAddr_Object = MibTableColumn
fnLSTrafficSrcAddr = _FnLSTrafficSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 2),
    _FnLSTrafficSrcAddr_Type()
)
fnLSTrafficSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficSrcAddr.setStatus("mandatory")
_FnLSTrafficSrcNetmask_Type = IpAddress
_FnLSTrafficSrcNetmask_Object = MibTableColumn
fnLSTrafficSrcNetmask = _FnLSTrafficSrcNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 3),
    _FnLSTrafficSrcNetmask_Type()
)
fnLSTrafficSrcNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficSrcNetmask.setStatus("mandatory")


class _FnLSTrafficSrcPort_Type(Integer32):
    """Custom type fnLSTrafficSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_FnLSTrafficSrcPort_Type.__name__ = "Integer32"
_FnLSTrafficSrcPort_Object = MibTableColumn
fnLSTrafficSrcPort = _FnLSTrafficSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 4),
    _FnLSTrafficSrcPort_Type()
)
fnLSTrafficSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficSrcPort.setStatus("mandatory")
_FnLSTrafficDstAddr_Type = IpAddress
_FnLSTrafficDstAddr_Object = MibTableColumn
fnLSTrafficDstAddr = _FnLSTrafficDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 5),
    _FnLSTrafficDstAddr_Type()
)
fnLSTrafficDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficDstAddr.setStatus("mandatory")
_FnLSTrafficDstNetmask_Type = IpAddress
_FnLSTrafficDstNetmask_Object = MibTableColumn
fnLSTrafficDstNetmask = _FnLSTrafficDstNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 6),
    _FnLSTrafficDstNetmask_Type()
)
fnLSTrafficDstNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficDstNetmask.setStatus("mandatory")


class _FnLSTrafficDstPort_Type(Integer32):
    """Custom type fnLSTrafficDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_FnLSTrafficDstPort_Type.__name__ = "Integer32"
_FnLSTrafficDstPort_Object = MibTableColumn
fnLSTrafficDstPort = _FnLSTrafficDstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 7),
    _FnLSTrafficDstPort_Type()
)
fnLSTrafficDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficDstPort.setStatus("mandatory")


class _FnLSTrafficProto_Type(Integer32):
    """Custom type fnLSTrafficProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_FnLSTrafficProto_Type.__name__ = "Integer32"
_FnLSTrafficProto_Object = MibTableColumn
fnLSTrafficProto = _FnLSTrafficProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 15, 1, 8),
    _FnLSTrafficProto_Type()
)
fnLSTrafficProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLSTrafficProto.setStatus("mandatory")
_FnLog_ObjectIdentity = ObjectIdentity
fnLog = _FnLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2)
)
_FnLogHDTable_Object = MibTable
fnLogHDTable = _FnLogHDTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 1)
)
if mibBuilder.loadTexts:
    fnLogHDTable.setStatus("mandatory")
_FnLogHDEntry_Object = MibTableRow
fnLogHDEntry = _FnLogHDEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 1, 1)
)
fnLogHDEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnLogHDEntryIndex"),
)
if mibBuilder.loadTexts:
    fnLogHDEntry.setStatus("mandatory")


class _FnLogHDEntryIndex_Type(Integer32):
    """Custom type fnLogHDEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnLogHDEntryIndex_Type.__name__ = "Integer32"
_FnLogHDEntryIndex_Object = MibTableColumn
fnLogHDEntryIndex = _FnLogHDEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 1, 1, 1),
    _FnLogHDEntryIndex_Type()
)
fnLogHDEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnLogHDEntryIndex.setStatus("mandatory")
_FnLogHDLastAccTime_Type = DisplayString
_FnLogHDLastAccTime_Object = MibTableColumn
fnLogHDLastAccTime = _FnLogHDLastAccTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 1, 1, 2),
    _FnLogHDLastAccTime_Type()
)
fnLogHDLastAccTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogHDLastAccTime.setStatus("mandatory")
_FnLogHDFileSize_Type = Integer32
_FnLogHDFileSize_Object = MibTableColumn
fnLogHDFileSize = _FnLogHDFileSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 1, 1, 3),
    _FnLogHDFileSize_Type()
)
fnLogHDFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogHDFileSize.setStatus("mandatory")
_FnLogHDFileName_Type = DisplayString
_FnLogHDFileName_Object = MibTableColumn
fnLogHDFileName = _FnLogHDFileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 1, 1, 4),
    _FnLogHDFileName_Type()
)
fnLogHDFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogHDFileName.setStatus("mandatory")
_FnLogMemTable_Object = MibTable
fnLogMemTable = _FnLogMemTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 2)
)
if mibBuilder.loadTexts:
    fnLogMemTable.setStatus("mandatory")
_FnLogMemEntry_Object = MibTableRow
fnLogMemEntry = _FnLogMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 2, 1)
)
fnLogMemEntry.setIndexNames(
    (0, "FORTINET-MIB", "fnLogMemEntryIndex"),
)
if mibBuilder.loadTexts:
    fnLogMemEntry.setStatus("mandatory")


class _FnLogMemEntryIndex_Type(Integer32):
    """Custom type fnLogMemEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnLogMemEntryIndex_Type.__name__ = "Integer32"
_FnLogMemEntryIndex_Object = MibTableColumn
fnLogMemEntryIndex = _FnLogMemEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 2, 1, 1),
    _FnLogMemEntryIndex_Type()
)
fnLogMemEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnLogMemEntryIndex.setStatus("mandatory")
_FnLogMemDetail_Type = DisplayString
_FnLogMemDetail_Object = MibTableColumn
fnLogMemDetail = _FnLogMemDetail_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2, 2, 1, 2),
    _FnLogMemDetail_Type()
)
fnLogMemDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogMemDetail.setStatus("mandatory")
_FnAlertEmai_ObjectIdentity = ObjectIdentity
fnAlertEmai = _FnAlertEmai_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3)
)
_FnAlertEmaiCfg_ObjectIdentity = ObjectIdentity
fnAlertEmaiCfg = _FnAlertEmaiCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 1)
)


class _FnAlertEmaiCfgSmtpSrv_Type(DisplayString):
    """Custom type fnAlertEmaiCfgSmtpSrv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnAlertEmaiCfgSmtpSrv_Type.__name__ = "DisplayString"
_FnAlertEmaiCfgSmtpSrv_Object = MibScalar
fnAlertEmaiCfgSmtpSrv = _FnAlertEmaiCfgSmtpSrv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 1, 1),
    _FnAlertEmaiCfgSmtpSrv_Type()
)
fnAlertEmaiCfgSmtpSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlertEmaiCfgSmtpSrv.setStatus("mandatory")


class _FnAlertEmaiCfgSmtpUser_Type(DisplayString):
    """Custom type fnAlertEmaiCfgSmtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnAlertEmaiCfgSmtpUser_Type.__name__ = "DisplayString"
_FnAlertEmaiCfgSmtpUser_Object = MibScalar
fnAlertEmaiCfgSmtpUser = _FnAlertEmaiCfgSmtpUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 1, 2),
    _FnAlertEmaiCfgSmtpUser_Type()
)
fnAlertEmaiCfgSmtpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlertEmaiCfgSmtpUser.setStatus("mandatory")
_FnAlertEmaiCfgSmtpPasswd_Type = OctetString
_FnAlertEmaiCfgSmtpPasswd_Object = MibScalar
fnAlertEmaiCfgSmtpPasswd = _FnAlertEmaiCfgSmtpPasswd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 1, 3),
    _FnAlertEmaiCfgSmtpPasswd_Type()
)
fnAlertEmaiCfgSmtpPasswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlertEmaiCfgSmtpPasswd.setStatus("mandatory")


class _FnAlertEmaiCfgEmai1_Type(DisplayString):
    """Custom type fnAlertEmaiCfgEmai1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnAlertEmaiCfgEmai1_Type.__name__ = "DisplayString"
_FnAlertEmaiCfgEmai1_Object = MibScalar
fnAlertEmaiCfgEmai1 = _FnAlertEmaiCfgEmai1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 1, 4),
    _FnAlertEmaiCfgEmai1_Type()
)
fnAlertEmaiCfgEmai1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlertEmaiCfgEmai1.setStatus("mandatory")


class _FnAlertEmaiCfgEmail2_Type(DisplayString):
    """Custom type fnAlertEmaiCfgEmail2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnAlertEmaiCfgEmail2_Type.__name__ = "DisplayString"
_FnAlertEmaiCfgEmail2_Object = MibScalar
fnAlertEmaiCfgEmail2 = _FnAlertEmaiCfgEmail2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 1, 5),
    _FnAlertEmaiCfgEmail2_Type()
)
fnAlertEmaiCfgEmail2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlertEmaiCfgEmail2.setStatus("mandatory")


class _FnAlertEmaiCfgEmail3_Type(DisplayString):
    """Custom type fnAlertEmaiCfgEmail3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnAlertEmaiCfgEmail3_Type.__name__ = "DisplayString"
_FnAlertEmaiCfgEmail3_Object = MibScalar
fnAlertEmaiCfgEmail3 = _FnAlertEmaiCfgEmail3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 1, 6),
    _FnAlertEmaiCfgEmail3_Type()
)
fnAlertEmaiCfgEmail3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlertEmaiCfgEmail3.setStatus("mandatory")
_FnAlertEmailCat_ObjectIdentity = ObjectIdentity
fnAlertEmailCat = _FnAlertEmailCat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 2)
)
_FnAlearEmaiCatVirus_Type = ItemState
_FnAlearEmaiCatVirus_Object = MibScalar
fnAlearEmaiCatVirus = _FnAlearEmaiCatVirus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 2, 1),
    _FnAlearEmaiCatVirus_Type()
)
fnAlearEmaiCatVirus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlearEmaiCatVirus.setStatus("mandatory")
_FnAlertEmailCatNids_Type = ItemState
_FnAlertEmailCatNids_Object = MibScalar
fnAlertEmailCatNids = _FnAlertEmailCatNids_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 2, 2),
    _FnAlertEmailCatNids_Type()
)
fnAlertEmailCatNids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlertEmailCatNids.setStatus("mandatory")
_FnAlearEmailCatCrit_Type = ItemState
_FnAlearEmailCatCrit_Object = MibScalar
fnAlearEmailCatCrit = _FnAlearEmailCatCrit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3, 2, 3),
    _FnAlearEmailCatCrit_Type()
)
fnAlearEmailCatCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAlearEmailCatCrit.setStatus("mandatory")
_FortinetTrap_ObjectIdentity = ObjectIdentity
fortinetTrap = _FortinetTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 10)
)
_FortinetProducts_ObjectIdentity = ObjectIdentity
fortinetProducts = _FortinetProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15)
)
_FortigateGeneric_ObjectIdentity = ObjectIdentity
fortigateGeneric = _FortigateGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 1)
)
_Fortigate50_ObjectIdentity = ObjectIdentity
fortigate50 = _Fortigate50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 50)
)
_Fortigate60_ObjectIdentity = ObjectIdentity
fortigate60 = _Fortigate60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 60)
)
_Fortigate100_ObjectIdentity = ObjectIdentity
fortigate100 = _Fortigate100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 100)
)
_Fortigate200_ObjectIdentity = ObjectIdentity
fortigate200 = _Fortigate200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 200)
)
_Fortigate300_ObjectIdentity = ObjectIdentity
fortigate300 = _Fortigate300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 300)
)
_Fortigate400_ObjectIdentity = ObjectIdentity
fortigate400 = _Fortigate400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 400)
)
_Fortigate420_ObjectIdentity = ObjectIdentity
fortigate420 = _Fortigate420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 420)
)
_Fortigate500_ObjectIdentity = ObjectIdentity
fortigate500 = _Fortigate500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 500)
)
_Fortigate1000_ObjectIdentity = ObjectIdentity
fortigate1000 = _Fortigate1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 1000)
)
_Fortigate2000_ObjectIdentity = ObjectIdentity
fortigate2000 = _Fortigate2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 2000)
)
_Fortigate3000_ObjectIdentity = ObjectIdentity
fortigate3000 = _Fortigate3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 3000)
)
_Fortigate3600_ObjectIdentity = ObjectIdentity
fortigate3600 = _Fortigate3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15, 3600)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-MIB",
    **{"AuthAlgorithm": AuthAlgorithm,
       "EncrytionAlgorithm": EncrytionAlgorithm,
       "LanguageCode": LanguageCode,
       "ItemState": ItemState,
       "fortinet": fortinet,
       "fnSystem": fnSystem,
       "fnSysStatus": fnSysStatus,
       "fnSysStatusOpMode": fnSysStatusOpMode,
       "fnSysStatusVersion": fnSysStatusVersion,
       "fnSysStatusAVDBVersion": fnSysStatusAVDBVersion,
       "fnSysStatusNIDSDBVersion": fnSysStatusNIDSDBVersion,
       "fnSysStatusSN": fnSysStatusSN,
       "fnSysMonitor": fnSysMonitor,
       "fnSysMonCPUUsage": fnSysMonCPUUsage,
       "fnSysMonCPUIdle": fnSysMonCPUIdle,
       "fnSysMonCPUInt": fnSysMonCPUInt,
       "fnSysMonMemUsage": fnSysMonMemUsage,
       "fnSysMonUpTime": fnSysMonUpTime,
       "fnSysMonSessionNum": fnSysMonSessionNum,
       "fnSysMonConnTable": fnSysMonConnTable,
       "fnSysMonConnEntry": fnSysMonConnEntry,
       "fnSysMonConnIndex": fnSysMonConnIndex,
       "fnSysMonConnProto": fnSysMonConnProto,
       "fnSysMonConnFromAddr": fnSysMonConnFromAddr,
       "fnSysMonConnFromPort": fnSysMonConnFromPort,
       "fnSysMonConnToAddr": fnSysMonConnToAddr,
       "fnSysMonConnToPort": fnSysMonConnToPort,
       "fnSysMonConnExp": fnSysMonConnExp,
       "fnSysUpdate": fnSysUpdate,
       "fnSysUpdateConnStatus1": fnSysUpdateConnStatus1,
       "fnSysUpdateConnStatus2": fnSysUpdateConnStatus2,
       "fnSysUpdatePushUpState": fnSysUpdatePushUpState,
       "fnSysUpdatePeriodicUpState": fnSysUpdatePeriodicUpState,
       "fnSysUpdatePeriodicUpFreq": fnSysUpdatePeriodicUpFreq,
       "fnSysUpdatePeriodicUpDay": fnSysUpdatePeriodicUpDay,
       "fnSysUpdatePeriodicUpTime": fnSysUpdatePeriodicUpTime,
       "fnSysUpdateVirusDefUpStatus": fnSysUpdateVirusDefUpStatus,
       "fnSysUpdateVirusDefUpLast": fnSysUpdateVirusDefUpLast,
       "fnSysUpdateIdsUpStatus": fnSysUpdateIdsUpStatus,
       "fnSysUpdateIdsUpLast": fnSysUpdateIdsUpLast,
       "fnSysUpdateSpamDefUpStatus": fnSysUpdateSpamDefUpStatus,
       "fnSysUpdateSpamDefUpLast": fnSysUpdateSpamDefUpLast,
       "fnSysNetwork": fnSysNetwork,
       "fnSysNetworkIfTable": fnSysNetworkIfTable,
       "fnSysNetworkIfEntry": fnSysNetworkIfEntry,
       "fnSysNetworkIfIndex": fnSysNetworkIfIndex,
       "fnSysNetworkIfName": fnSysNetworkIfName,
       "fnSysNetworkIfIp": fnSysNetworkIfIp,
       "fnSysNetworkIfNetmask": fnSysNetworkIfNetmask,
       "fnSysNetworkIfMAC": fnSysNetworkIfMAC,
       "fnSysNetworkIfSpeed": fnSysNetworkIfSpeed,
       "fnSysNetworkIfOutFrag": fnSysNetworkIfOutFrag,
       "fnSysNetworkIfStatus": fnSysNetworkIfStatus,
       "fnSysNetworkIfAddrMode": fnSysNetworkIfAddrMode,
       "fnSysNetworkIfAccHttps": fnSysNetworkIfAccHttps,
       "fnSysNetworkIfAccPing": fnSysNetworkIfAccPing,
       "fnSysNetworkIfAccSsh": fnSysNetworkIfAccSsh,
       "fnSysNetworkIfAccSnmp": fnSysNetworkIfAccSnmp,
       "fnSysNetworkIfAccHttp": fnSysNetworkIfAccHttp,
       "fnSysNetworkIfAccTelnet": fnSysNetworkIfAccTelnet,
       "fnSysNetworkIfPingSrvState": fnSysNetworkIfPingSrvState,
       "fnSysNetworkIfPingSrvAddr": fnSysNetworkIfPingSrvAddr,
       "fnSysNetworkIfIp2": fnSysNetworkIfIp2,
       "fnSysNetworkIfNetmask2": fnSysNetworkIfNetmask2,
       "fnSysNetworkIfPingSrvState2": fnSysNetworkIfPingSrvState2,
       "fnSysNetworkIfPingSrvAddr2": fnSysNetworkIfPingSrvAddr2,
       "fnSysNetworkVlanTable": fnSysNetworkVlanTable,
       "fnSysNetworkVlanEntry": fnSysNetworkVlanEntry,
       "fnSysNetworkVlanIndex": fnSysNetworkVlanIndex,
       "fnSysNetworkVlanName": fnSysNetworkVlanName,
       "fnSysNetworkVlanIf": fnSysNetworkVlanIf,
       "fnSysNetworkVlanId": fnSysNetworkVlanId,
       "fnSysNetworkVlanIp": fnSysNetworkVlanIp,
       "fnSysNetworkVlanNetmask": fnSysNetworkVlanNetmask,
       "fnSysNetworkVlanAccHttps": fnSysNetworkVlanAccHttps,
       "fnSysNetworkVlanAccPing": fnSysNetworkVlanAccPing,
       "fnSysNetworkVlanAccSsh": fnSysNetworkVlanAccSsh,
       "fnSysNetworkVlanAccSnmp": fnSysNetworkVlanAccSnmp,
       "fnSysNetworkVlanAccHttp": fnSysNetworkVlanAccHttp,
       "fnSysNetworkVlanAccTelnet": fnSysNetworkVlanAccTelnet,
       "fnSysNetworkAccessTable": fnSysNetworkAccessTable,
       "fnSysNetworkAccessEntry": fnSysNetworkAccessEntry,
       "fnSysNetworkAccessIfName": fnSysNetworkAccessIfName,
       "fnSysNetworkAccessHttps": fnSysNetworkAccessHttps,
       "fnSysNetworkAccessPing": fnSysNetworkAccessPing,
       "fnSysNetworkAccessSsh": fnSysNetworkAccessSsh,
       "fnSysNetworkAccessSnmp": fnSysNetworkAccessSnmp,
       "fnSysNetworkAccessHttp": fnSysNetworkAccessHttp,
       "fnSysNetworkAccessTelnet": fnSysNetworkAccessTelnet,
       "fnSysNetworkRouting": fnSysNetworkRouting,
       "fnSysNetworkRoutingTable": fnSysNetworkRoutingTable,
       "fnSysNetworkRoutingEntry": fnSysNetworkRoutingEntry,
       "fnSysNetworkRoutingIndex": fnSysNetworkRoutingIndex,
       "fnSysNetworkRoutingSrcIP": fnSysNetworkRoutingSrcIP,
       "fnSysNetworkRoutingSrcNetmask": fnSysNetworkRoutingSrcNetmask,
       "fnSysNetworkRoutingDstIP": fnSysNetworkRoutingDstIP,
       "fnSysNetworkRoutingDstNetmask": fnSysNetworkRoutingDstNetmask,
       "fnSysNetworkRoutingGW1": fnSysNetworkRoutingGW1,
       "fnSysNetworkRoutingGW2": fnSysNetworkRoutingGW2,
       "fnSysNetworkRoutingDev1": fnSysNetworkRoutingDev1,
       "fnSysNetworkRoutingDev2": fnSysNetworkRoutingDev2,
       "fnSysNetworkRoutingRIPSrv": fnSysNetworkRoutingRIPSrv,
       "fnSysNetworkRoutingGWTable": fnSysNetworkRoutingGWTable,
       "fnSysNetworkRoutingGWEntry": fnSysNetworkRoutingGWEntry,
       "fnSysNetworkRoutingGWIndex": fnSysNetworkRoutingGWIndex,
       "fnSysNetworkRoutingGWIP": fnSysNetworkRoutingGWIP,
       "fnSysNetworkRoutingGWDeadDet": fnSysNetworkRoutingGWDeadDet,
       "fnSysNetworkDhcp": fnSysNetworkDhcp,
       "fnSysNetworkDhcpStatus": fnSysNetworkDhcpStatus,
       "fnSysNetworkDhcpSip": fnSysNetworkDhcpSip,
       "fnSysNetworkDhcpEip": fnSysNetworkDhcpEip,
       "fnSysNetworkDhcpLeaseDur": fnSysNetworkDhcpLeaseDur,
       "fnSysNetworkDhcpDomain": fnSysNetworkDhcpDomain,
       "fnSysNetworkDhcpDNS1": fnSysNetworkDhcpDNS1,
       "fnSysNetworkDhcpDNS2": fnSysNetworkDhcpDNS2,
       "fnSysNetworkDhcpDNS3": fnSysNetworkDhcpDNS3,
       "fnSysNetworkDhcpDefRoute": fnSysNetworkDhcpDefRoute,
       "fnSysNetworkDhcpExclRange1S": fnSysNetworkDhcpExclRange1S,
       "fnSysNetworkDhcpExclRange1E": fnSysNetworkDhcpExclRange1E,
       "fnSysNetworkDhcpExclRange2S": fnSysNetworkDhcpExclRange2S,
       "fnSysNetworkDhcpExclRange2E": fnSysNetworkDhcpExclRange2E,
       "fnSysNetworkDhcpExclRange3S": fnSysNetworkDhcpExclRange3S,
       "fnSysNetworkDhcpExclRange3E": fnSysNetworkDhcpExclRange3E,
       "fnSysZoneTable": fnSysZoneTable,
       "fnSysZoneEntry": fnSysZoneEntry,
       "fnSysZoneId": fnSysZoneId,
       "fnSysZoneName": fnSysZoneName,
       "fnSysZoneSecLevel": fnSysZoneSecLevel,
       "fnSysZoneBlkTraffic": fnSysZoneBlkTraffic,
       "fnSysZoneLogTraffic": fnSysZoneLogTraffic,
       "fnSysNetworkDNS": fnSysNetworkDNS,
       "fnSysNetworkDNSPri": fnSysNetworkDNSPri,
       "fnSysNetworkDNSSecPri": fnSysNetworkDNSSecPri,
       "fnSysConfig": fnSysConfig,
       "fnSysConfigTime": fnSysConfigTime,
       "fnSysConfigTimeVal": fnSysConfigTimeVal,
       "fnSysConfigTimezone": fnSysConfigTimezone,
       "fnSysConfigTimeDST": fnSysConfigTimeDST,
       "fnSysConfigTimeNTPSrv": fnSysConfigTimeNTPSrv,
       "fnSysConfigTimeNTPInt": fnSysConfigTimeNTPInt,
       "fnSysConfigNTPState": fnSysConfigNTPState,
       "fnSysConfigOpts": fnSysConfigOpts,
       "fnSysConfigOptsIdleTimeout": fnSysConfigOptsIdleTimeout,
       "fnSysConfigOptsAuthTimeout": fnSysConfigOptsAuthTimeout,
       "fnSysConfigOptsLan": fnSysConfigOptsLan,
       "fnSysConfigOptsLcdProt": fnSysConfigOptsLcdProt,
       "fnSysConfigOptsLcdProtPin": fnSysConfigOptsLcdProtPin,
       "fnSysConfigAdmin": fnSysConfigAdmin,
       "fnSysConfigAdminUserTable": fnSysConfigAdminUserTable,
       "fnSysConfigAdminUserEntry": fnSysConfigAdminUserEntry,
       "fnSysConfigAdminUserIndex": fnSysConfigAdminUserIndex,
       "fnSysConfigAdminUserName": fnSysConfigAdminUserName,
       "fnSysConfigAdminUserIp": fnSysConfigAdminUserIp,
       "fnSysConfigAdminUserNetmask": fnSysConfigAdminUserNetmask,
       "fnSysConfigAdminUserPermission": fnSysConfigAdminUserPermission,
       "fnSysConfigHA": fnSysConfigHA,
       "fnSysConfigHAMode": fnSysConfigHAMode,
       "fnSysConfigHAGrpId": fnSysConfigHAGrpId,
       "fnSysConfigHAPasswd": fnSysConfigHAPasswd,
       "fnSysConfigHAMonIf": fnSysConfigHAMonIf,
       "fnSysConfigHASchedule": fnSysConfigHASchedule,
       "fnSysSnmp": fnSysSnmp,
       "fnSysSnmpGen": fnSysSnmpGen,
       "fnSysSnmpState": fnSysSnmpState,
       "fnSysSnmpSysName": fnSysSnmpSysName,
       "fnSysSnmpSysLoc": fnSysSnmpSysLoc,
       "fnSysSnmpInfo": fnSysSnmpInfo,
       "fnSysSnmpGetCom": fnSysSnmpGetCom,
       "fnSysSnmpTrapCom": fnSysSnmpTrapCom,
       "fnSysSnmp1stTrapIp": fnSysSnmp1stTrapIp,
       "fnSysSnmp2ndTrapIp": fnSysSnmp2ndTrapIp,
       "fnSysSnmp3rdTrapIp": fnSysSnmp3rdTrapIp,
       "fnSysSnmpv3AccCtrl": fnSysSnmpv3AccCtrl,
       "fnSysSnmpv3ACState": fnSysSnmpv3ACState,
       "fnSysSnmpv3ACTable": fnSysSnmpv3ACTable,
       "fnSysSnmpv3ACEntry": fnSysSnmpv3ACEntry,
       "fnSysSnmpACIndex": fnSysSnmpACIndex,
       "fnSysSnmpACGrpName": fnSysSnmpACGrpName,
       "fnSysSnmpACSecLevelAuth": fnSysSnmpACSecLevelAuth,
       "fnSysSnmpACSecLevelPriv": fnSysSnmpACSecLevelPriv,
       "fnSysSnmpACContexPre": fnSysSnmpACContexPre,
       "fnSysSnmpACContextMatch": fnSysSnmpACContextMatch,
       "fnSysSnmpACRv": fnSysSnmpACRv,
       "fnSysSnmpACWv": fnSysSnmpACWv,
       "fnSysSnmpACNv": fnSysSnmpACNv,
       "fnSysSnmpSecurity": fnSysSnmpSecurity,
       "fnSysSnmpSecUserTable": fnSysSnmpSecUserTable,
       "fnSysSnmpSecUserEntry": fnSysSnmpSecUserEntry,
       "fnSysSnmpSecUserName": fnSysSnmpSecUserName,
       "fnSysSnmpSecUserSecLevelAuth": fnSysSnmpSecUserSecLevelAuth,
       "fnSysSnmpSecUserSecLevelPriv": fnSysSnmpSecUserSecLevelPriv,
       "fnSysSnmpSecUserAuthPasswd": fnSysSnmpSecUserAuthPasswd,
       "fnSysSnmpSecUserAuthProto": fnSysSnmpSecUserAuthProto,
       "fnSysSnmpSecUserPrivPasswd": fnSysSnmpSecUserPrivPasswd,
       "fnSysSnmpSecGrpTable": fnSysSnmpSecGrpTable,
       "fnSysSnmpSecGrpEntry": fnSysSnmpSecGrpEntry,
       "fnSysSnmpSecGrpName": fnSysSnmpSecGrpName,
       "fnSysSnmpSecGrpMembers": fnSysSnmpSecGrpMembers,
       "fnSysSnmpViewTable": fnSysSnmpViewTable,
       "fnSysSnmpViewEntry": fnSysSnmpViewEntry,
       "fnSysSnmpViewName": fnSysSnmpViewName,
       "fnSysSnmpViewSubtreeOid": fnSysSnmpViewSubtreeOid,
       "fnSysSnmpViewMask": fnSysSnmpViewMask,
       "fnSysSnmpViewType": fnSysSnmpViewType,
       "fnFirewall": fnFirewall,
       "fnFirewallPolicy": fnFirewallPolicy,
       "fnFirewallPolicyTable": fnFirewallPolicyTable,
       "fnFirewallPolicyEntry": fnFirewallPolicyEntry,
       "fnFirewallPolicyIndex": fnFirewallPolicyIndex,
       "fnFirewallPolicySrcZone": fnFirewallPolicySrcZone,
       "fnFirewallPolicyDestZone": fnFirewallPolicyDestZone,
       "fnFirewallPolicySrcAddr": fnFirewallPolicySrcAddr,
       "fnFirewallPolicyDestAddr": fnFirewallPolicyDestAddr,
       "fnFirewallPolicySchedule": fnFirewallPolicySchedule,
       "fnFirewallPolicyService": fnFirewallPolicyService,
       "fnFirewallPolicyAction": fnFirewallPolicyAction,
       "fnFirewallPolicyNAT": fnFirewallPolicyNAT,
       "fnFirewallPolicyDipPool": fnFirewallPolicyDipPool,
       "fnFirewallPolicyFixPort": fnFirewallPolicyFixPort,
       "fnFirewallPolicyAuth": fnFirewallPolicyAuth,
       "fnFirewallPolicyVpnTunName": fnFirewallPolicyVpnTunName,
       "fnFirewallPolicyVpnAllowIn": fnFirewallPolicyVpnAllowIn,
       "fnFirewallPolicyVpnAllowOut": fnFirewallPolicyVpnAllowOut,
       "fnFirewallPolicyVpnInNat": fnFirewallPolicyVpnInNat,
       "fnFirewallPolicyVpnOutNat": fnFirewallPolicyVpnOutNat,
       "fnFirewallPolicyLog": fnFirewallPolicyLog,
       "fnFirewallPolicyAV": fnFirewallPolicyAV,
       "fnFirewallPolicyGBand": fnFirewallPolicyGBand,
       "fnFirewallPolicyMBand": fnFirewallPolicyMBand,
       "fnFirewallPolicyTrafficPri": fnFirewallPolicyTrafficPri,
       "fnFirewallPolicyProf": fnFirewallPolicyProf,
       "fnFirewallAddress": fnFirewallAddress,
       "fnFirewallAddrTable": fnFirewallAddrTable,
       "fnFirewallAddrEntry": fnFirewallAddrEntry,
       "fnFirewallAddrName": fnFirewallAddrName,
       "fnFirewallAddrIp": fnFirewallAddrIp,
       "fnFirewallAddressNetmask": fnFirewallAddressNetmask,
       "fnFirewallAddrZone": fnFirewallAddrZone,
       "fnFirewallAddrVlanId": fnFirewallAddrVlanId,
       "fnFirewallAddrGrpTable": fnFirewallAddrGrpTable,
       "fnFirewallAddrGrpEntry": fnFirewallAddrGrpEntry,
       "fnFirewallAddrGrpIndex": fnFirewallAddrGrpIndex,
       "fnFirewallAddrGrpZone": fnFirewallAddrGrpZone,
       "fnFirewallAddrGrpName": fnFirewallAddrGrpName,
       "fnFirewallAddrGrpMems": fnFirewallAddrGrpMems,
       "fnFirewallService": fnFirewallService,
       "fnFirewallServiceTable": fnFirewallServiceTable,
       "fnFirewallServiceEntry": fnFirewallServiceEntry,
       "fnFirewallServiceIndex": fnFirewallServiceIndex,
       "fnFirewallServiceName": fnFirewallServiceName,
       "fnFirewallServiceProto": fnFirewallServiceProto,
       "fnFirewallServiceUsed": fnFirewallServiceUsed,
       "fnFirewallServiceSrcPortLow": fnFirewallServiceSrcPortLow,
       "fnFirewallServiceSrcPortHigh": fnFirewallServiceSrcPortHigh,
       "fnFirewallServiceDstPortLow": fnFirewallServiceDstPortLow,
       "fnFirewallServiceDstPortHigh": fnFirewallServiceDstPortHigh,
       "fnFirewallServiceType": fnFirewallServiceType,
       "fnFirewallServiceGroupTable": fnFirewallServiceGroupTable,
       "fnFirewallServiceGroupEntry": fnFirewallServiceGroupEntry,
       "fnFirewallServiceGroupIndex": fnFirewallServiceGroupIndex,
       "fnFirewallServiceGroupName": fnFirewallServiceGroupName,
       "fnFirewallServiceGroupValue": fnFirewallServiceGroupValue,
       "fnFirewallServiceGroupUsed": fnFirewallServiceGroupUsed,
       "fnFirewallSchedule": fnFirewallSchedule,
       "fnFirewallSchOneTable": fnFirewallSchOneTable,
       "fnFirewallSchOneEntry": fnFirewallSchOneEntry,
       "fnFirewallSchOneIndex": fnFirewallSchOneIndex,
       "fnFirewallSchOneName": fnFirewallSchOneName,
       "fnFirewallSchOneStartDay": fnFirewallSchOneStartDay,
       "fnFirewallSchOneStartTime": fnFirewallSchOneStartTime,
       "fnFirewallSchOneEndDay": fnFirewallSchOneEndDay,
       "fnFirewallSchOneEndTime": fnFirewallSchOneEndTime,
       "fnFirewallSchOneUsed": fnFirewallSchOneUsed,
       "fnFirewallSchRecurTable": fnFirewallSchRecurTable,
       "fnFirewallSchRecurEntry": fnFirewallSchRecurEntry,
       "fnFirewallSchRecurIndex": fnFirewallSchRecurIndex,
       "fnFirewallSchRecurName": fnFirewallSchRecurName,
       "fnFirewallSchRecurWeekdays": fnFirewallSchRecurWeekdays,
       "fnFirewallSchRecurStartTime": fnFirewallSchRecurStartTime,
       "fnFirewallSchRecurEndTime": fnFirewallSchRecurEndTime,
       "fnFirewallSchRecurUsed": fnFirewallSchRecurUsed,
       "fnFirewallVirtualIP": fnFirewallVirtualIP,
       "fnFirewallVIPTable": fnFirewallVIPTable,
       "fnFirewallVIPEntry": fnFirewallVIPEntry,
       "fnFirewallVIPIndex": fnFirewallVIPIndex,
       "fnFirewallVIPName": fnFirewallVIPName,
       "fnFirewallVIPExtIf": fnFirewallVIPExtIf,
       "fnFirewallVIPType": fnFirewallVIPType,
       "fnFirewallVIPExtIP": fnFirewallVIPExtIP,
       "fnFirewallVIPExtPort": fnFirewallVIPExtPort,
       "fnFirewallVIPMapIP": fnFirewallVIPMapIP,
       "fnFirewallVIPMapPort": fnFirewallVIPMapPort,
       "fnFirewallVIPProto": fnFirewallVIPProto,
       "fnFirewallIpPool": fnFirewallIpPool,
       "fnFirewallIpPoolTable": fnFirewallIpPoolTable,
       "fnFirewallIpPoolEntry": fnFirewallIpPoolEntry,
       "fnFirewallIpPoolIndex": fnFirewallIpPoolIndex,
       "fnFirewallIpPoolIf": fnFirewallIpPoolIf,
       "fnFirewallIpPoolStartIp": fnFirewallIpPoolStartIp,
       "fnFirewallIpPoolEndIp": fnFirewallIpPoolEndIp,
       "fnFirewallIPMACBinding": fnFirewallIPMACBinding,
       "fnFirewallIPMACBindingTable": fnFirewallIPMACBindingTable,
       "fnFirewallIPMACBindingEntry": fnFirewallIPMACBindingEntry,
       "fnFirewallIPMACIndex": fnFirewallIPMACIndex,
       "fnFirewallIPMACName": fnFirewallIPMACName,
       "fnFirewallIPMACIp": fnFirewallIPMACIp,
       "fnFirewallIPMACMac": fnFirewallIPMACMac,
       "fnFirewallIPMACState": fnFirewallIPMACState,
       "fnFirewallIPMACStatus": fnFirewallIPMACStatus,
       "fnFirewallIPMACAction": fnFirewallIPMACAction,
       "fnFirewallIPMACToFw": fnFirewallIPMACToFw,
       "fnFirewallIPMACThruFw": fnFirewallIPMACThruFw,
       "fnFirewallIPMACTraffic": fnFirewallIPMACTraffic,
       "fnFirewallContProfiles": fnFirewallContProfiles,
       "fnFwContProfTable": fnFwContProfTable,
       "fnFwContProfEntry": fnFwContProfEntry,
       "fnFwContProfName": fnFwContProfName,
       "fnFwContProfAvScan": fnFwContProfAvScan,
       "fnFwContProfFileBlk": fnFwContProfFileBlk,
       "fnFwContProfQuarantine": fnFwContProfQuarantine,
       "fnFwContProfUrlBlkState": fnFwContProfUrlBlkState,
       "fnFwContProfBannedWordState": fnFwContProfBannedWordState,
       "fnFwContProfRemvScriptState": fnFwContProfRemvScriptState,
       "fnFwContProfExptListState": fnFwContProfExptListState,
       "fnFwContProfSpamFilter": fnFwContProfSpamFilter,
       "fnFwContProfSpamBlkList": fnFwContProfSpamBlkList,
       "fnFwContProfSpamExptList": fnFwContProfSpamExptList,
       "fnFwContProfSpamBanWord": fnFwContProfSpamBanWord,
       "fnFwContProfBigFileBlk": fnFwContProfBigFileBlk,
       "fnFwContProfPassFragEmail": fnFwContProfPassFragEmail,
       "fnUser": fnUser,
       "fnUserLocalTable": fnUserLocalTable,
       "fnUserLocalEntry": fnUserLocalEntry,
       "fnUserLocalIndex": fnUserLocalIndex,
       "fnUserLocalName": fnUserLocalName,
       "fnUserLocalPasswd": fnUserLocalPasswd,
       "fnUserLocalState": fnUserLocalState,
       "fnUserLocalType": fnUserLocalType,
       "fnUserLocalRadiusSrv": fnUserLocalRadiusSrv,
       "fnUserLocalRadiusOther": fnUserLocalRadiusOther,
       "fnUserRadiusSrvTable": fnUserRadiusSrvTable,
       "fnUserRadiusSrvEntry": fnUserRadiusSrvEntry,
       "fnUserRadIndex": fnUserRadIndex,
       "fnUserRadName": fnUserRadName,
       "fnUserRadAddr": fnUserRadAddr,
       "fnUserRadSecret": fnUserRadSecret,
       "fnUserGrpTable": fnUserGrpTable,
       "fnUserGrpEntry": fnUserGrpEntry,
       "fnUserGrpIndex": fnUserGrpIndex,
       "fnUserGrpName": fnUserGrpName,
       "fnUserGrpMembers": fnUserGrpMembers,
       "fnVpn": fnVpn,
       "fnVpnIPSEC": fnVpnIPSEC,
       "fnVpnIKETable": fnVpnIKETable,
       "fnVpnIKEEntry": fnVpnIKEEntry,
       "fnVpnIKEIndex": fnVpnIKEIndex,
       "fnVpnIKEName": fnVpnIKEName,
       "fnVpnIKEGW1": fnVpnIKEGW1,
       "fnVpnIKEPh2Encrp1": fnVpnIKEPh2Encrp1,
       "fnVpnIKEPh2Auth1": fnVpnIKEPh2Auth1,
       "fnVpnIKEPh2Encrp2": fnVpnIKEPh2Encrp2,
       "fnVpnIKEPh2Auth2": fnVpnIKEPh2Auth2,
       "fnVpnIKEPh2Encrp3": fnVpnIKEPh2Encrp3,
       "fnVpnIKEPh2Auth3": fnVpnIKEPh2Auth3,
       "fnVpnIKEReplayDet": fnVpnIKEReplayDet,
       "fnVpnIKEPFSState": fnVpnIKEPFSState,
       "fnVpnIKEDHGrp": fnVpnIKEDHGrp,
       "fnVpnIKEKeylifeType": fnVpnIKEKeylifeType,
       "fnVpnIKEKLifeSec": fnVpnIKEKLifeSec,
       "fnVpnIKEKeylifeKb": fnVpnIKEKeylifeKb,
       "fnVpnIKEKeepAlive": fnVpnIKEKeepAlive,
       "fnVpnIKEGW2": fnVpnIKEGW2,
       "fnVpnIKEGW3": fnVpnIKEGW3,
       "fnVpnIKEConcentrator": fnVpnIKEConcentrator,
       "fnVpnIKEStatus": fnVpnIKEStatus,
       "fnVpnIKETimeout": fnVpnIKETimeout,
       "fnVpnManualKeyTable": fnVpnManualKeyTable,
       "fnVpnManualKeyEntry": fnVpnManualKeyEntry,
       "fnVpnManualKeyIndex": fnVpnManualKeyIndex,
       "fnVpnManualKeyName": fnVpnManualKeyName,
       "fnVpnManualKeyEngage": fnVpnManualKeyEngage,
       "fnVpnManualKeyLocalSPI": fnVpnManualKeyLocalSPI,
       "fnVpnManualKeyRemoteSPI": fnVpnManualKeyRemoteSPI,
       "fnVpnManualKeyRgw": fnVpnManualKeyRgw,
       "fnVpnManualKeyReplayDet": fnVpnManualKeyReplayDet,
       "fnVpnManualKeyEncrpAlgorithm": fnVpnManualKeyEncrpAlgorithm,
       "fnVpnManualKeyConcentrator": fnVpnManualKeyConcentrator,
       "fnVpnRemoteGWTable": fnVpnRemoteGWTable,
       "fnVpnRemoteGWEntry": fnVpnRemoteGWEntry,
       "fnVpnRemoteGWIndex": fnVpnRemoteGWIndex,
       "fnVpnRemoteGWName": fnVpnRemoteGWName,
       "fnVpnRemoteGWIp": fnVpnRemoteGWIp,
       "fnVpnRemoteGWMode": fnVpnRemoteGWMode,
       "fnVpnRemoteGWPh1Encrp1": fnVpnRemoteGWPh1Encrp1,
       "fnVpnRemoteGWPh1Auth1": fnVpnRemoteGWPh1Auth1,
       "fnVpnRemoteGWPh1Encrp2": fnVpnRemoteGWPh1Encrp2,
       "fnVpnRemoteGWPh1Auth2": fnVpnRemoteGWPh1Auth2,
       "fnVpnRemoteGWPh1Encrp3": fnVpnRemoteGWPh1Encrp3,
       "fnVpnRemoteGWPh1Auth3": fnVpnRemoteGWPh1Auth3,
       "fnVpnRemoteGWDhGrp": fnVpnRemoteGWDhGrp,
       "fnVpnRemoteGWKeylife": fnVpnRemoteGWKeylife,
       "fnVpnRemoteGWPreKey": fnVpnRemoteGWPreKey,
       "fnVpnRemoteGWLocalID": fnVpnRemoteGWLocalID,
       "fnVpnRemoteGWNatT": fnVpnRemoteGWNatT,
       "fnVpnRemoteGWKAFreq": fnVpnRemoteGWKAFreq,
       "fnVpnRemoteGWType": fnVpnRemoteGWType,
       "fnVpnRemoteGWUserGrp": fnVpnRemoteGWUserGrp,
       "fnVpnRemoteGWAuthMethod": fnVpnRemoteGWAuthMethod,
       "fnVpnRemoteGWCertName": fnVpnRemoteGWCertName,
       "fnVpnRemoteGWPeerOpt": fnVpnRemoteGWPeerOpt,
       "fnVpnRemoteGWPeerGrpName": fnVpnRemoteGWPeerGrpName,
       "fnVpnRemoteGWPeerId": fnVpnRemoteGWPeerId,
       "fnVpnRemoteGWXAuth": fnVpnRemoteGWXAuth,
       "fnVpnRemoteGWXAuthUserName": fnVpnRemoteGWXAuthUserName,
       "fnVpnRemoteGWXAuthPasswd": fnVpnRemoteGWXAuthPasswd,
       "fnVpnRemoteGWXAuthPap": fnVpnRemoteGWXAuthPap,
       "fnVpnRemoteGWDeadPeerDet": fnVpnRemoteGWDeadPeerDet,
       "fnVpnRemoteGWDpdIdleWorry": fnVpnRemoteGWDpdIdleWorry,
       "fnVpnRemoteGWDpdRetryCound": fnVpnRemoteGWDpdRetryCound,
       "fnVpnRemoteGWDpdRetryInt": fnVpnRemoteGWDpdRetryInt,
       "fnVpnRemoteGWDpdIdleCleanup": fnVpnRemoteGWDpdIdleCleanup,
       "fnVpnConTable": fnVpnConTable,
       "fnVpnConEntry": fnVpnConEntry,
       "fnVpnConIndex": fnVpnConIndex,
       "fnVpnConName": fnVpnConName,
       "fnVpnConMembers": fnVpnConMembers,
       "fnVpnDialupMonTable": fnVpnDialupMonTable,
       "fnVpnDialupMonEntry": fnVpnDialupMonEntry,
       "fnVpnDialupMonIndex": fnVpnDialupMonIndex,
       "fnVpnDialupMonRGwName": fnVpnDialupMonRGwName,
       "fnVpnDialupMonLifetime": fnVpnDialupMonLifetime,
       "fnVpnDialupMonTimeout": fnVpnDialupMonTimeout,
       "fnVpnDialupMonProxyIdSrc": fnVpnDialupMonProxyIdSrc,
       "fnVpnDialupMonProxyIdDst": fnVpnDialupMonProxyIdDst,
       "fnVpnPPTP": fnVpnPPTP,
       "fnVpnPPTPStatus": fnVpnPPTPStatus,
       "fnVpnPPTPUserGrp": fnVpnPPTPUserGrp,
       "fnVpnPPTPStartIp": fnVpnPPTPStartIp,
       "fnVpnPPTPEndIp": fnVpnPPTPEndIp,
       "fnVpnL2TP": fnVpnL2TP,
       "fnVpnL2TPStatus": fnVpnL2TPStatus,
       "fnVpnL2TPUserGrp": fnVpnL2TPUserGrp,
       "fnVpnL2TPStartIp": fnVpnL2TPStartIp,
       "fnVpnL2TPEndIp": fnVpnL2TPEndIp,
       "fnVpnCert": fnVpnCert,
       "fnVpnCertTable": fnVpnCertTable,
       "fnVpnCertEntry": fnVpnCertEntry,
       "fnVpnCertName": fnVpnCertName,
       "fnVpnCertIssuer": fnVpnCertIssuer,
       "fnVpnCertCommonName": fnVpnCertCommonName,
       "fnVpnCertType": fnVpnCertType,
       "fnVpnCertSerialNo": fnVpnCertSerialNo,
       "fnVpnCertExpDate": fnVpnCertExpDate,
       "fnVpnCertStatus": fnVpnCertStatus,
       "fnNIDS": fnNIDS,
       "fnNidsDetection": fnNidsDetection,
       "fnNidsGen": fnNidsGen,
       "fnNidsMonIfs": fnNidsMonIfs,
       "fnNidsTypeIP": fnNidsTypeIP,
       "fnNidsTypeTcp": fnNidsTypeTcp,
       "fnNidsTypeUdp": fnNidsTypeUdp,
       "fnNidsTypeIcmp": fnNidsTypeIcmp,
       "fnNidsSigTable": fnNidsSigTable,
       "fnNidsSigEntry": fnNidsSigEntry,
       "fnNidsSigGrpName": fnNidsSigGrpName,
       "fnNidsSigAttackId": fnNidsSigAttackId,
       "fnNidsSigAttackName": fnNidsSigAttackName,
       "fnNidsSigAttackRuleState": fnNidsSigAttackRuleState,
       "fnNidsSigUserDefTable": fnNidsSigUserDefTable,
       "fnNidsSigUserDefEntry": fnNidsSigUserDefEntry,
       "fnNidsSigUserDefName": fnNidsSigUserDefName,
       "fnNidsSigUserDefSum": fnNidsSigUserDefSum,
       "fnNidsSigUserDefProto": fnNidsSigUserDefProto,
       "fnNidsPrevention": fnNidsPrevention,
       "fnNidsIdpState": fnNidsIdpState,
       "fnNidsIdpTable": fnNidsIdpTable,
       "fnNidsIdpEntry": fnNidsIdpEntry,
       "fnNidsIdpSigName": fnNidsIdpSigName,
       "fnNidsIdpSigSum": fnNidsIdpSigSum,
       "fnNidsIdpSigProto": fnNidsIdpSigProto,
       "fnNidsIdpSigState": fnNidsIdpSigState,
       "fnNidsIdpSigThreshold": fnNidsIdpSigThreshold,
       "fnNidsIdpSigQSize": fnNidsIdpSigQSize,
       "fnNidsIdpSigKeepAlive": fnNidsIdpSigKeepAlive,
       "fnNidsResponse": fnNidsResponse,
       "fnNidsRespCfg": fnNidsRespCfg,
       "fnNidsRespAlertMsg": fnNidsRespAlertMsg,
       "fnNidsRespAlertSrcAddrState": fnNidsRespAlertSrcAddrState,
       "fnNidsRespAlertDstAddrState": fnNidsRespAlertDstAddrState,
       "fnNidsRespLogMsg": fnNidsRespLogMsg,
       "fnNidsRespLogSrcAddrState": fnNidsRespLogSrcAddrState,
       "fnNidsRespLogDstAddrState": fnNidsRespLogDstAddrState,
       "fnAntiVirus": fnAntiVirus,
       "fnAvFileBlock": fnAvFileBlock,
       "fnAvFileBlkRuleTable": fnAvFileBlkRuleTable,
       "fnAvFileBlkRuleEntry": fnAvFileBlkRuleEntry,
       "fnAvFbRuleIndex": fnAvFbRuleIndex,
       "fnAvFbRuleFilePat": fnAvFbRuleFilePat,
       "fnAvFbRuleHttpBlk": fnAvFbRuleHttpBlk,
       "fnAvFbRuleFtpBlk": fnAvFbRuleFtpBlk,
       "fnAvFbRuleSmtpBlk": fnAvFbRuleSmtpBlk,
       "fnAvFbRulePop3Blk": fnAvFbRulePop3Blk,
       "fnAvFbRuleImapBlk": fnAvFbRuleImapBlk,
       "fnAvQuatantine": fnAvQuatantine,
       "fnAvQuarantineTable": fnAvQuarantineTable,
       "fnAvQuarantineEntry": fnAvQuarantineEntry,
       "fnAvQuarIndex": fnAvQuarIndex,
       "fnAvQuarFileName": fnAvQuarFileName,
       "fnAvQuarTime": fnAvQuarTime,
       "fnAvQuarService": fnAvQuarService,
       "fnAvQuarStatus": fnAvQuarStatus,
       "fnAvQuarStatusDetail": fnAvQuarStatusDetail,
       "fnAvQuarDc": fnAvQuarDc,
       "fnAvQuarTtl": fnAvQuarTtl,
       "fnAvQuarantineCfg": fnAvQuarantineCfg,
       "fnAvQuarCfgInfecFileHttp": fnAvQuarCfgInfecFileHttp,
       "fnAvQuarCfgInfecFileFtp": fnAvQuarCfgInfecFileFtp,
       "fnAvQuarCfgInfecFileImap": fnAvQuarCfgInfecFileImap,
       "fnAvQuarCfgInfecFilePop3": fnAvQuarCfgInfecFilePop3,
       "fnAvQuarCfgInfecFileSmtp": fnAvQuarCfgInfecFileSmtp,
       "fnAvQuarCfgBlkFileHttp": fnAvQuarCfgBlkFileHttp,
       "fnAvQuarCfgBlkFileFtp": fnAvQuarCfgBlkFileFtp,
       "fnAvQuarCfgBlkFileImap": fnAvQuarCfgBlkFileImap,
       "fnAvQuarCfgBlkFilePop3": fnAvQuarCfgBlkFilePop3,
       "fnAvQuarCfgBlkFileSmtp": fnAvQuarCfgBlkFileSmtp,
       "fnAvQuarCfgAgeLimit": fnAvQuarCfgAgeLimit,
       "fnAvQuarCfgMaxFileSize": fnAvQuarCfgMaxFileSize,
       "fnAvQuarCfgLowDiskOpt": fnAvQuarCfgLowDiskOpt,
       "fnAVConfig": fnAVConfig,
       "fnAVVirusListTable": fnAVVirusListTable,
       "fnAVVirusListEntry": fnAVVirusListEntry,
       "fnAvVirusIndex": fnAvVirusIndex,
       "fnAvVirusName": fnAvVirusName,
       "fnAvCfgMsgTable": fnAvCfgMsgTable,
       "fnAvCfgMsgEntry": fnAvCfgMsgEntry,
       "fnAvCfgMsgIndex": fnAvCfgMsgIndex,
       "fnAvCfgMsgName": fnAvCfgMsgName,
       "fnAvCfgMsgService": fnAvCfgMsgService,
       "fnAvCfgMsgDescription": fnAvCfgMsgDescription,
       "fnAvCfgBlkFileHttp": fnAvCfgBlkFileHttp,
       "fnAvCfgBlkFileFtp": fnAvCfgBlkFileFtp,
       "fnAvCfgBlkEmailImap": fnAvCfgBlkEmailImap,
       "fnAvCfgBlkEmailPop3": fnAvCfgBlkEmailPop3,
       "fnAvCfgBlkEmailSmtp": fnAvCfgBlkEmailSmtp,
       "fnWebFilter": fnWebFilter,
       "fnWebFilterBWords": fnWebFilterBWords,
       "fnWebFilterBannedWordsTable": fnWebFilterBannedWordsTable,
       "fnWebfilterBannedWordsEntry": fnWebfilterBannedWordsEntry,
       "fnWebFilterBannedWordIndex": fnWebFilterBannedWordIndex,
       "fnWebFilterBannedWords": fnWebFilterBannedWords,
       "fnWebFilterBannedWordLan": fnWebFilterBannedWordLan,
       "fnWebFilterBannedWordState": fnWebFilterBannedWordState,
       "fnWebFilterUrlBlk": fnWebFilterUrlBlk,
       "fnWebFilterUrlBlkState": fnWebFilterUrlBlkState,
       "fnWebFilterUrlBlkTable": fnWebFilterUrlBlkTable,
       "fnWebFilterUrlBlkEntry": fnWebFilterUrlBlkEntry,
       "fnWebFilterUrlBlkIndex": fnWebFilterUrlBlkIndex,
       "fnWebFilterUrlPat": fnWebFilterUrlPat,
       "fnWebFilterUrlState": fnWebFilterUrlState,
       "fnWebFilterScripts": fnWebFilterScripts,
       "fnWebFilterApplet": fnWebFilterApplet,
       "fnWebFilterCookie": fnWebFilterCookie,
       "fnWebFilterActiveX": fnWebFilterActiveX,
       "fnWebFilterExemptUrl": fnWebFilterExemptUrl,
       "fnWebFilterExemptUrlTable": fnWebFilterExemptUrlTable,
       "fnWebFilterExemptUrlEntry": fnWebFilterExemptUrlEntry,
       "fnWebFilterExemptUrlIndex": fnWebFilterExemptUrlIndex,
       "fnWebFilterExemptUrlPat": fnWebFilterExemptUrlPat,
       "fnWebFilterExemptUrlState": fnWebFilterExemptUrlState,
       "fnWebFilterCfg": fnWebFilterCfg,
       "fnWfCfgMsgTable": fnWfCfgMsgTable,
       "fnWfCfgMsgEntry": fnWfCfgMsgEntry,
       "fnWfCfgMsgIndex": fnWfCfgMsgIndex,
       "fnWfCfgMsgName": fnWfCfgMsgName,
       "fnWfCfgMsgService": fnWfCfgMsgService,
       "fnWfCfgMsgDescription": fnWfCfgMsgDescription,
       "fnAntiSpam": fnAntiSpam,
       "fnAntiSpamBlkTable": fnAntiSpamBlkTable,
       "fnAntiSpamBlkEntry": fnAntiSpamBlkEntry,
       "fnAntiSpamBlkIndex": fnAntiSpamBlkIndex,
       "fnAntiSpamBlkPat": fnAntiSpamBlkPat,
       "fnAntiSpamBlkImapState": fnAntiSpamBlkImapState,
       "fnAntiSpamBlkPop3State": fnAntiSpamBlkPop3State,
       "fnAntiSpamExemptTable": fnAntiSpamExemptTable,
       "fnAntiSpamExemptEntry": fnAntiSpamExemptEntry,
       "fnAntiSpamExemptIndex": fnAntiSpamExemptIndex,
       "fnAntiSpamBanWordPat": fnAntiSpamBanWordPat,
       "fnAntiSpamExemptImapState": fnAntiSpamExemptImapState,
       "fnAntiSpamExemptPop3State": fnAntiSpamExemptPop3State,
       "fnAntiSpamBanWordTable": fnAntiSpamBanWordTable,
       "fnAntiSpamBanWordEntry": fnAntiSpamBanWordEntry,
       "fnAntiSpamBanWordIndex": fnAntiSpamBanWordIndex,
       "fnAntiSpamBanWordImapState": fnAntiSpamBanWordImapState,
       "fnAntiSpamBanWordPop3State": fnAntiSpamBanWordPop3State,
       "fnAntiSpamCfgSubTag": fnAntiSpamCfgSubTag,
       "fnLogAndRpt": fnLogAndRpt,
       "fnLogSetting": fnLogSetting,
       "fnLogToRemHostState": fnLogToRemHostState,
       "fnLogToRemHostAddr": fnLogToRemHostAddr,
       "fnLogToWebtrendsSrvState": fnLogToWebtrendsSrvState,
       "fnLogToWebtrendsSrvAddr": fnLogToWebtrendsSrvAddr,
       "fnLogToLocalState": fnLogToLocalState,
       "fnLogTrafficIntToFw": fnLogTrafficIntToFw,
       "fnLogTrafficExtToFw": fnLogTrafficExtToFw,
       "fnLogAllEvents": fnLogAllEvents,
       "fnLogVirusEvents": fnLogVirusEvents,
       "fnLogIntrusions": fnLogIntrusions,
       "fnLogToLocalFileSize": fnLogToLocalFileSize,
       "fnLogToLocalTime": fnLogToLocalTime,
       "fnLogToLocalOpt": fnLogToLocalOpt,
       "fnLogSettingFilter": fnLogSettingFilter,
       "fnLogSettingTrafficFilter": fnLogSettingTrafficFilter,
       "fnLSTrafficFilterState": fnLSTrafficFilterState,
       "fnLSTrafficFilterType": fnLSTrafficFilterType,
       "fnLSTrafficFilterDisplay": fnLSTrafficFilterDisplay,
       "fnLSTrafficFilterResolveIp": fnLSTrafficFilterResolveIp,
       "fnLogSettingEventFilter": fnLogSettingEventFilter,
       "fnLSEventFilterCfgChg": fnLSEventFilterCfgChg,
       "fnLSEventFilterIpsecNeg": fnLSEventFilterIpsecNeg,
       "fnLSEventFilterDhcpService": fnLSEventFilterDhcpService,
       "fnLSEventFilterPppoeService": fnLSEventFilterPppoeService,
       "fnLSEventFilterAdminLogin": fnLSEventFilterAdminLogin,
       "fnLSEventFilterIpmacStatus": fnLSEventFilterIpmacStatus,
       "fnLSEventFilterSysAct": fnLSEventFilterSysAct,
       "fnLSEventFilterHaAct": fnLSEventFilterHaAct,
       "fnLSEventFilterFwAuth": fnLSEventFilterFwAuth,
       "fnLSEventFilterGwConn": fnLSEventFilterGwConn,
       "fnLogSettingVirusFilter": fnLogSettingVirusFilter,
       "fnLSVirusFilterDet": fnLSVirusFilterDet,
       "fnLSVirusFilterSigUpdate": fnLSVirusFilterSigUpdate,
       "fnLogSettingWebFilter": fnLogSettingWebFilter,
       "fnLSWebFilterBanDet": fnLSWebFilterBanDet,
       "fnLSWebFilterScriptDet": fnLSWebFilterScriptDet,
       "fnLSWebFilterPageBlk": fnLSWebFilterPageBlk,
       "fnLSIdsFilterState": fnLSIdsFilterState,
       "fnLSFilterSeverity": fnLSFilterSeverity,
       "fnLSTrafficAddrTable": fnLSTrafficAddrTable,
       "fnLSTrafficAddrEntry": fnLSTrafficAddrEntry,
       "fnLSTrafficEntryIndex": fnLSTrafficEntryIndex,
       "fnLSTrafficSrcAddr": fnLSTrafficSrcAddr,
       "fnLSTrafficSrcNetmask": fnLSTrafficSrcNetmask,
       "fnLSTrafficSrcPort": fnLSTrafficSrcPort,
       "fnLSTrafficDstAddr": fnLSTrafficDstAddr,
       "fnLSTrafficDstNetmask": fnLSTrafficDstNetmask,
       "fnLSTrafficDstPort": fnLSTrafficDstPort,
       "fnLSTrafficProto": fnLSTrafficProto,
       "fnLog": fnLog,
       "fnLogHDTable": fnLogHDTable,
       "fnLogHDEntry": fnLogHDEntry,
       "fnLogHDEntryIndex": fnLogHDEntryIndex,
       "fnLogHDLastAccTime": fnLogHDLastAccTime,
       "fnLogHDFileSize": fnLogHDFileSize,
       "fnLogHDFileName": fnLogHDFileName,
       "fnLogMemTable": fnLogMemTable,
       "fnLogMemEntry": fnLogMemEntry,
       "fnLogMemEntryIndex": fnLogMemEntryIndex,
       "fnLogMemDetail": fnLogMemDetail,
       "fnAlertEmai": fnAlertEmai,
       "fnAlertEmaiCfg": fnAlertEmaiCfg,
       "fnAlertEmaiCfgSmtpSrv": fnAlertEmaiCfgSmtpSrv,
       "fnAlertEmaiCfgSmtpUser": fnAlertEmaiCfgSmtpUser,
       "fnAlertEmaiCfgSmtpPasswd": fnAlertEmaiCfgSmtpPasswd,
       "fnAlertEmaiCfgEmai1": fnAlertEmaiCfgEmai1,
       "fnAlertEmaiCfgEmail2": fnAlertEmaiCfgEmail2,
       "fnAlertEmaiCfgEmail3": fnAlertEmaiCfgEmail3,
       "fnAlertEmailCat": fnAlertEmailCat,
       "fnAlearEmaiCatVirus": fnAlearEmaiCatVirus,
       "fnAlertEmailCatNids": fnAlertEmailCatNids,
       "fnAlearEmailCatCrit": fnAlearEmailCatCrit,
       "fortinetTrap": fortinetTrap,
       "fortinetProducts": fortinetProducts,
       "fortigateGeneric": fortigateGeneric,
       "fortigate50": fortigate50,
       "fortigate60": fortigate60,
       "fortigate100": fortigate100,
       "fortigate200": fortigate200,
       "fortigate300": fortigate300,
       "fortigate400": fortigate400,
       "fortigate420": fortigate420,
       "fortigate500": fortigate500,
       "fortigate1000": fortigate1000,
       "fortigate2000": fortigate2000,
       "fortigate3000": fortigate3000,
       "fortigate3600": fortigate3600}
)
