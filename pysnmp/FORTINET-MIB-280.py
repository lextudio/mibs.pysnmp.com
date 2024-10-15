# SNMP MIB module (FORTINET-MIB-280) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORTINET-MIB-280
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:37 2024
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



class FnBoolState(Integer32):
    """Custom type FnBoolState based on Integer32"""
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





class FnIndex(Integer32):
    """Custom type FnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class FnOpMode(Integer32):
    """Custom type FnOpMode based on Integer32"""
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





class FnHaMode(Integer32):
    """Custom type FnHaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active-active", 2),
          ("active-passive", 3),
          ("standalone", 1))
    )





class FnHaSchedule(Integer32):
    """Custom type FnHaSchedule based on Integer32"""
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
          ("ip-based", 7),
          ("ip-port-based", 8),
          ("least-connections", 3),
          ("none", 1),
          ("random", 6),
          ("round-robin", 4),
          ("weighted-round-robin", 5))
    )





class FnAdminPerm(Integer32):
    """Custom type FnAdminPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("domain-admin", 15),
          ("read-admin", 0),
          ("super-admin", 255),
          ("write-admin", 1))
    )





class FnUserAuth(Integer32):
    """Custom type FnUserAuth based on Integer32"""
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
        *(("ldap", 4),
          ("local", 1),
          ("radius-multiple", 3),
          ("radius-single", 2))
    )





class FnIfAddrMode(Integer32):
    """Custom type FnIfAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )





class FnSessProto(Integer32):
    """Custom type FnSessProto based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fortinet_ObjectIdentity = ObjectIdentity
fortinet = _Fortinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356)
)
_FnTraps_ObjectIdentity = ObjectIdentity
fnTraps = _FnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 0)
)
_FnSystem_ObjectIdentity = ObjectIdentity
fnSystem = _FnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1)
)
_FnSysModel_Type = Integer32
_FnSysModel_Object = MibScalar
fnSysModel = _FnSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1),
    _FnSysModel_Type()
)
fnSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysModel.setStatus("current")


class _FnSysSerial_Type(DisplayString):
    """Custom type fnSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnSysSerial_Type.__name__ = "DisplayString"
_FnSysSerial_Object = MibScalar
fnSysSerial = _FnSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2),
    _FnSysSerial_Type()
)
fnSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSerial.setStatus("current")


class _FnSysVersion_Type(DisplayString):
    """Custom type fnSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysVersion_Type.__name__ = "DisplayString"
_FnSysVersion_Object = MibScalar
fnSysVersion = _FnSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3),
    _FnSysVersion_Type()
)
fnSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysVersion.setStatus("current")


class _FnSysVersionAv_Type(DisplayString):
    """Custom type fnSysVersionAv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysVersionAv_Type.__name__ = "DisplayString"
_FnSysVersionAv_Object = MibScalar
fnSysVersionAv = _FnSysVersionAv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4),
    _FnSysVersionAv_Type()
)
fnSysVersionAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysVersionAv.setStatus("current")


class _FnSysVersionNids_Type(DisplayString):
    """Custom type fnSysVersionNids based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysVersionNids_Type.__name__ = "DisplayString"
_FnSysVersionNids_Object = MibScalar
fnSysVersionNids = _FnSysVersionNids_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5),
    _FnSysVersionNids_Type()
)
fnSysVersionNids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysVersionNids.setStatus("current")
_FnSysHaMode_Type = FnHaMode
_FnSysHaMode_Object = MibScalar
fnSysHaMode = _FnSysHaMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 6),
    _FnSysHaMode_Type()
)
fnSysHaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysHaMode.setStatus("current")
_FnSysOpMode_Type = FnOpMode
_FnSysOpMode_Object = MibScalar
fnSysOpMode = _FnSysOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 7),
    _FnSysOpMode_Type()
)
fnSysOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysOpMode.setStatus("current")
_FnSysCpuUsage_Type = Gauge32
_FnSysCpuUsage_Object = MibScalar
fnSysCpuUsage = _FnSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 8),
    _FnSysCpuUsage_Type()
)
fnSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysCpuUsage.setStatus("current")
_FnSysMemUsage_Type = Gauge32
_FnSysMemUsage_Object = MibScalar
fnSysMemUsage = _FnSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 9),
    _FnSysMemUsage_Type()
)
fnSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMemUsage.setStatus("current")
_FnSysSesCount_Type = Gauge32
_FnSysSesCount_Object = MibScalar
fnSysSesCount = _FnSysSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 10),
    _FnSysSesCount_Type()
)
fnSysSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSesCount.setStatus("current")
_FnHa_ObjectIdentity = ObjectIdentity
fnHa = _FnHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100)
)
_FnHaGroupId_Type = Integer32
_FnHaGroupId_Object = MibScalar
fnHaGroupId = _FnHaGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 1),
    _FnHaGroupId_Type()
)
fnHaGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaGroupId.setStatus("current")


class _FnHaPriority_Type(Integer32):
    """Custom type fnHaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FnHaPriority_Type.__name__ = "Integer32"
_FnHaPriority_Object = MibScalar
fnHaPriority = _FnHaPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 2),
    _FnHaPriority_Type()
)
fnHaPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaPriority.setStatus("current")
_FnHaOverride_Type = FnBoolState
_FnHaOverride_Object = MibScalar
fnHaOverride = _FnHaOverride_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 3),
    _FnHaOverride_Type()
)
fnHaOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaOverride.setStatus("current")
_FnHaAutoSync_Type = FnBoolState
_FnHaAutoSync_Object = MibScalar
fnHaAutoSync = _FnHaAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 4),
    _FnHaAutoSync_Type()
)
fnHaAutoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaAutoSync.setStatus("current")
_FnHaSchedule_Type = FnHaSchedule
_FnHaSchedule_Object = MibScalar
fnHaSchedule = _FnHaSchedule_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 5),
    _FnHaSchedule_Type()
)
fnHaSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaSchedule.setStatus("current")
_FnHaStatsTable_Object = MibTable
fnHaStatsTable = _FnHaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6)
)
if mibBuilder.loadTexts:
    fnHaStatsTable.setStatus("current")
_FnHaStatsEntry_Object = MibTableRow
fnHaStatsEntry = _FnHaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1)
)
fnHaStatsEntry.setIndexNames(
    (0, "FORTINET-MIB-280", "fnHaStatsIndex"),
)
if mibBuilder.loadTexts:
    fnHaStatsEntry.setStatus("current")
_FnHaStatsIndex_Type = FnIndex
_FnHaStatsIndex_Object = MibTableColumn
fnHaStatsIndex = _FnHaStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 1),
    _FnHaStatsIndex_Type()
)
fnHaStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsIndex.setStatus("current")


class _FnHaStatsSerial_Type(DisplayString):
    """Custom type fnHaStatsSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnHaStatsSerial_Type.__name__ = "DisplayString"
_FnHaStatsSerial_Object = MibTableColumn
fnHaStatsSerial = _FnHaStatsSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 2),
    _FnHaStatsSerial_Type()
)
fnHaStatsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsSerial.setStatus("current")
_FnHaStatsCpuUsage_Type = Gauge32
_FnHaStatsCpuUsage_Object = MibTableColumn
fnHaStatsCpuUsage = _FnHaStatsCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 3),
    _FnHaStatsCpuUsage_Type()
)
fnHaStatsCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsCpuUsage.setStatus("current")
_FnHaStatsMemUsage_Type = Gauge32
_FnHaStatsMemUsage_Object = MibTableColumn
fnHaStatsMemUsage = _FnHaStatsMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 4),
    _FnHaStatsMemUsage_Type()
)
fnHaStatsMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsMemUsage.setStatus("current")
_FnHaStatsNetUsage_Type = Gauge32
_FnHaStatsNetUsage_Object = MibTableColumn
fnHaStatsNetUsage = _FnHaStatsNetUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 5),
    _FnHaStatsNetUsage_Type()
)
fnHaStatsNetUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsNetUsage.setStatus("current")
_FnHaStatsSesCount_Type = Gauge32
_FnHaStatsSesCount_Object = MibTableColumn
fnHaStatsSesCount = _FnHaStatsSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 6),
    _FnHaStatsSesCount_Type()
)
fnHaStatsSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsSesCount.setStatus("current")
_FnHaStatsPktCount_Type = Counter32
_FnHaStatsPktCount_Object = MibTableColumn
fnHaStatsPktCount = _FnHaStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 7),
    _FnHaStatsPktCount_Type()
)
fnHaStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsPktCount.setStatus("current")
_FnHaStatsByteCount_Type = Counter32
_FnHaStatsByteCount_Object = MibTableColumn
fnHaStatsByteCount = _FnHaStatsByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 8),
    _FnHaStatsByteCount_Type()
)
fnHaStatsByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsByteCount.setStatus("current")
_FnHaStatsIdsCount_Type = Counter32
_FnHaStatsIdsCount_Object = MibTableColumn
fnHaStatsIdsCount = _FnHaStatsIdsCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 9),
    _FnHaStatsIdsCount_Type()
)
fnHaStatsIdsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsIdsCount.setStatus("current")
_FnHaStatsAvCount_Type = Counter32
_FnHaStatsAvCount_Object = MibTableColumn
fnHaStatsAvCount = _FnHaStatsAvCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 10),
    _FnHaStatsAvCount_Type()
)
fnHaStatsAvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsAvCount.setStatus("current")
_FnAdmin_ObjectIdentity = ObjectIdentity
fnAdmin = _FnAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101)
)
_FnAdminNumber_Type = Integer32
_FnAdminNumber_Object = MibScalar
fnAdminNumber = _FnAdminNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 1),
    _FnAdminNumber_Type()
)
fnAdminNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminNumber.setStatus("current")
_FnAdminTable_Object = MibTable
fnAdminTable = _FnAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2)
)
if mibBuilder.loadTexts:
    fnAdminTable.setStatus("current")
_FnAdminEntry_Object = MibTableRow
fnAdminEntry = _FnAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1)
)
fnAdminEntry.setIndexNames(
    (0, "FORTINET-MIB-280", "fnAdminIndex"),
)
if mibBuilder.loadTexts:
    fnAdminEntry.setStatus("current")
_FnAdminIndex_Type = FnIndex
_FnAdminIndex_Object = MibTableColumn
fnAdminIndex = _FnAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 1),
    _FnAdminIndex_Type()
)
fnAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminIndex.setStatus("current")
_FnAdminName_Type = DisplayString
_FnAdminName_Object = MibTableColumn
fnAdminName = _FnAdminName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 2),
    _FnAdminName_Type()
)
fnAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminName.setStatus("current")
_FnAdminAddr_Type = IpAddress
_FnAdminAddr_Object = MibTableColumn
fnAdminAddr = _FnAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 3),
    _FnAdminAddr_Type()
)
fnAdminAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminAddr.setStatus("current")
_FnAdminMask_Type = IpAddress
_FnAdminMask_Object = MibTableColumn
fnAdminMask = _FnAdminMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 4),
    _FnAdminMask_Type()
)
fnAdminMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminMask.setStatus("current")
_FnAdminPerm_Type = FnAdminPerm
_FnAdminPerm_Object = MibTableColumn
fnAdminPerm = _FnAdminPerm_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 5),
    _FnAdminPerm_Type()
)
fnAdminPerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminPerm.setStatus("current")
_FnUsers_ObjectIdentity = ObjectIdentity
fnUsers = _FnUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102)
)
_FnUserNumber_Type = Integer32
_FnUserNumber_Object = MibScalar
fnUserNumber = _FnUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 1),
    _FnUserNumber_Type()
)
fnUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserNumber.setStatus("current")
_FnUserTable_Object = MibTable
fnUserTable = _FnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2)
)
if mibBuilder.loadTexts:
    fnUserTable.setStatus("current")
_FnUserEntry_Object = MibTableRow
fnUserEntry = _FnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1)
)
fnUserEntry.setIndexNames(
    (0, "FORTINET-MIB-280", "fnUserIndex"),
)
if mibBuilder.loadTexts:
    fnUserEntry.setStatus("current")
_FnUserIndex_Type = FnIndex
_FnUserIndex_Object = MibTableColumn
fnUserIndex = _FnUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 1),
    _FnUserIndex_Type()
)
fnUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserIndex.setStatus("current")
_FnUserName_Type = DisplayString
_FnUserName_Object = MibTableColumn
fnUserName = _FnUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 2),
    _FnUserName_Type()
)
fnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserName.setStatus("current")
_FnUserAuth_Type = FnUserAuth
_FnUserAuth_Object = MibTableColumn
fnUserAuth = _FnUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 3),
    _FnUserAuth_Type()
)
fnUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserAuth.setStatus("current")
_FnUserState_Type = FnBoolState
_FnUserState_Object = MibTableColumn
fnUserState = _FnUserState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 4),
    _FnUserState_Type()
)
fnUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserState.setStatus("current")
_FnOptions_ObjectIdentity = ObjectIdentity
fnOptions = _FnOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 103)
)
_FnOptIdleTimeout_Type = Integer32
_FnOptIdleTimeout_Object = MibScalar
fnOptIdleTimeout = _FnOptIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 103, 1),
    _FnOptIdleTimeout_Type()
)
fnOptIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOptIdleTimeout.setStatus("current")
_FnLogging_ObjectIdentity = ObjectIdentity
fnLogging = _FnLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 104)
)
_FnLogOption_Type = Integer32
_FnLogOption_Object = MibScalar
fnLogOption = _FnLogOption_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 104, 1),
    _FnLogOption_Type()
)
fnLogOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLogOption.setStatus("current")
_FnMessages_ObjectIdentity = ObjectIdentity
fnMessages = _FnMessages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 105)
)
_FnMesgNumber_Type = Integer32
_FnMesgNumber_Object = MibScalar
fnMesgNumber = _FnMesgNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 105, 1),
    _FnMesgNumber_Type()
)
fnMesgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnMesgNumber.setStatus("current")
_FnDomains_ObjectIdentity = ObjectIdentity
fnDomains = _FnDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2)
)
_FnVdNumber_Type = Integer32
_FnVdNumber_Object = MibScalar
fnVdNumber = _FnVdNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1),
    _FnVdNumber_Type()
)
fnVdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdNumber.setStatus("current")
_FnVdTable_Object = MibTable
fnVdTable = _FnVdTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2)
)
if mibBuilder.loadTexts:
    fnVdTable.setStatus("current")
_FnVdEntry_Object = MibTableRow
fnVdEntry = _FnVdEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1)
)
fnVdEntry.setIndexNames(
    (0, "FORTINET-MIB-280", "fnVdIndex"),
)
if mibBuilder.loadTexts:
    fnVdEntry.setStatus("current")
_FnVdIndex_Type = FnIndex
_FnVdIndex_Object = MibTableColumn
fnVdIndex = _FnVdIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1),
    _FnVdIndex_Type()
)
fnVdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdIndex.setStatus("current")
_FnVdName_Type = DisplayString
_FnVdName_Object = MibTableColumn
fnVdName = _FnVdName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 2),
    _FnVdName_Type()
)
fnVdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdName.setStatus("current")
_FnIp_ObjectIdentity = ObjectIdentity
fnIp = _FnIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 4)
)
_FnIpSessTable_Object = MibTable
fnIpSessTable = _FnIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2)
)
if mibBuilder.loadTexts:
    fnIpSessTable.setStatus("current")
_FnIpSessEntry_Object = MibTableRow
fnIpSessEntry = _FnIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1)
)
fnIpSessEntry.setIndexNames(
    (0, "FORTINET-MIB-280", "fnIpSessIndex"),
)
if mibBuilder.loadTexts:
    fnIpSessEntry.setStatus("current")
_FnIpSessIndex_Type = FnIndex
_FnIpSessIndex_Object = MibTableColumn
fnIpSessIndex = _FnIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 1),
    _FnIpSessIndex_Type()
)
fnIpSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessIndex.setStatus("current")
_FnIpSessProto_Type = FnSessProto
_FnIpSessProto_Object = MibTableColumn
fnIpSessProto = _FnIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 2),
    _FnIpSessProto_Type()
)
fnIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessProto.setStatus("current")
_FnIpSessFromAddr_Type = IpAddress
_FnIpSessFromAddr_Object = MibTableColumn
fnIpSessFromAddr = _FnIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 3),
    _FnIpSessFromAddr_Type()
)
fnIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessFromAddr.setStatus("current")


class _FnIpSessFromPort_Type(Integer32):
    """Custom type fnIpSessFromPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnIpSessFromPort_Type.__name__ = "Integer32"
_FnIpSessFromPort_Object = MibTableColumn
fnIpSessFromPort = _FnIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 4),
    _FnIpSessFromPort_Type()
)
fnIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessFromPort.setStatus("current")
_FnIpSessToAddr_Type = IpAddress
_FnIpSessToAddr_Object = MibTableColumn
fnIpSessToAddr = _FnIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 5),
    _FnIpSessToAddr_Type()
)
fnIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessToAddr.setStatus("current")


class _FnIpSessToPort_Type(Integer32):
    """Custom type fnIpSessToPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnIpSessToPort_Type.__name__ = "Integer32"
_FnIpSessToPort_Object = MibTableColumn
fnIpSessToPort = _FnIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 6),
    _FnIpSessToPort_Type()
)
fnIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessToPort.setStatus("current")
_FnIpSessExp_Type = Counter32
_FnIpSessExp_Object = MibTableColumn
fnIpSessExp = _FnIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 7),
    _FnIpSessExp_Type()
)
fnIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessExp.setStatus("current")
_FnVpn_ObjectIdentity = ObjectIdentity
fnVpn = _FnVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9)
)
_FnVpnDialupTable_Object = MibTable
fnVpnDialupTable = _FnVpnDialupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1)
)
if mibBuilder.loadTexts:
    fnVpnDialupTable.setStatus("current")
_FnVpnDialupEntry_Object = MibTableRow
fnVpnDialupEntry = _FnVpnDialupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1)
)
fnVpnDialupEntry.setIndexNames(
    (0, "FORTINET-MIB-280", "fnVpnDialupIndex"),
)
if mibBuilder.loadTexts:
    fnVpnDialupEntry.setStatus("current")
_FnVpnDialupIndex_Type = FnIndex
_FnVpnDialupIndex_Object = MibTableColumn
fnVpnDialupIndex = _FnVpnDialupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 1),
    _FnVpnDialupIndex_Type()
)
fnVpnDialupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupIndex.setStatus("current")
_FnVpnDialupGateway_Type = IpAddress
_FnVpnDialupGateway_Object = MibTableColumn
fnVpnDialupGateway = _FnVpnDialupGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 2),
    _FnVpnDialupGateway_Type()
)
fnVpnDialupGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupGateway.setStatus("current")
_FnVpnDialupLifetime_Type = Integer32
_FnVpnDialupLifetime_Object = MibTableColumn
fnVpnDialupLifetime = _FnVpnDialupLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 3),
    _FnVpnDialupLifetime_Type()
)
fnVpnDialupLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupLifetime.setStatus("current")
_FnVpnDialupTimeout_Type = Integer32
_FnVpnDialupTimeout_Object = MibTableColumn
fnVpnDialupTimeout = _FnVpnDialupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 4),
    _FnVpnDialupTimeout_Type()
)
fnVpnDialupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupTimeout.setStatus("current")
_FnVpnDialupSrcBegin_Type = IpAddress
_FnVpnDialupSrcBegin_Object = MibTableColumn
fnVpnDialupSrcBegin = _FnVpnDialupSrcBegin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 5),
    _FnVpnDialupSrcBegin_Type()
)
fnVpnDialupSrcBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupSrcBegin.setStatus("current")
_FnVpnDialupSrcEnd_Type = IpAddress
_FnVpnDialupSrcEnd_Object = MibTableColumn
fnVpnDialupSrcEnd = _FnVpnDialupSrcEnd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 6),
    _FnVpnDialupSrcEnd_Type()
)
fnVpnDialupSrcEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupSrcEnd.setStatus("current")
_FnVpnDialupDstAddr_Type = IpAddress
_FnVpnDialupDstAddr_Object = MibTableColumn
fnVpnDialupDstAddr = _FnVpnDialupDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 7),
    _FnVpnDialupDstAddr_Type()
)
fnVpnDialupDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupDstAddr.setStatus("current")
_FnIps_ObjectIdentity = ObjectIdentity
fnIps = _FnIps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 12)
)
_FnIpsSigId_Type = FnIndex
_FnIpsSigId_Object = MibScalar
fnIpsSigId = _FnIpsSigId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 12, 1),
    _FnIpsSigId_Type()
)
fnIpsSigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsSigId.setStatus("current")
_FnIpsSigSrcIp_Type = IpAddress
_FnIpsSigSrcIp_Object = MibScalar
fnIpsSigSrcIp = _FnIpsSigSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 12, 2),
    _FnIpsSigSrcIp_Type()
)
fnIpsSigSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsSigSrcIp.setStatus("current")
_FnBridge_ObjectIdentity = ObjectIdentity
fnBridge = _FnBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 15)
)
_FnBridgeFgtFailure_Type = DisplayString
_FnBridgeFgtFailure_Object = MibScalar
fnBridgeFgtFailure = _FnBridgeFgtFailure_Object(
    (1, 3, 6, 1, 4, 1, 12356, 15, 1),
    _FnBridgeFgtFailure_Type()
)
fnBridgeFgtFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnBridgeFgtFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-MIB-280",
    **{"FnBoolState": FnBoolState,
       "FnIndex": FnIndex,
       "FnOpMode": FnOpMode,
       "FnHaMode": FnHaMode,
       "FnHaSchedule": FnHaSchedule,
       "FnAdminPerm": FnAdminPerm,
       "FnUserAuth": FnUserAuth,
       "FnIfAddrMode": FnIfAddrMode,
       "FnSessProto": FnSessProto,
       "fortinet": fortinet,
       "fnTraps": fnTraps,
       "fnSystem": fnSystem,
       "fnSysModel": fnSysModel,
       "fnSysSerial": fnSysSerial,
       "fnSysVersion": fnSysVersion,
       "fnSysVersionAv": fnSysVersionAv,
       "fnSysVersionNids": fnSysVersionNids,
       "fnSysHaMode": fnSysHaMode,
       "fnSysOpMode": fnSysOpMode,
       "fnSysCpuUsage": fnSysCpuUsage,
       "fnSysMemUsage": fnSysMemUsage,
       "fnSysSesCount": fnSysSesCount,
       "fnHa": fnHa,
       "fnHaGroupId": fnHaGroupId,
       "fnHaPriority": fnHaPriority,
       "fnHaOverride": fnHaOverride,
       "fnHaAutoSync": fnHaAutoSync,
       "fnHaSchedule": fnHaSchedule,
       "fnHaStatsTable": fnHaStatsTable,
       "fnHaStatsEntry": fnHaStatsEntry,
       "fnHaStatsIndex": fnHaStatsIndex,
       "fnHaStatsSerial": fnHaStatsSerial,
       "fnHaStatsCpuUsage": fnHaStatsCpuUsage,
       "fnHaStatsMemUsage": fnHaStatsMemUsage,
       "fnHaStatsNetUsage": fnHaStatsNetUsage,
       "fnHaStatsSesCount": fnHaStatsSesCount,
       "fnHaStatsPktCount": fnHaStatsPktCount,
       "fnHaStatsByteCount": fnHaStatsByteCount,
       "fnHaStatsIdsCount": fnHaStatsIdsCount,
       "fnHaStatsAvCount": fnHaStatsAvCount,
       "fnAdmin": fnAdmin,
       "fnAdminNumber": fnAdminNumber,
       "fnAdminTable": fnAdminTable,
       "fnAdminEntry": fnAdminEntry,
       "fnAdminIndex": fnAdminIndex,
       "fnAdminName": fnAdminName,
       "fnAdminAddr": fnAdminAddr,
       "fnAdminMask": fnAdminMask,
       "fnAdminPerm": fnAdminPerm,
       "fnUsers": fnUsers,
       "fnUserNumber": fnUserNumber,
       "fnUserTable": fnUserTable,
       "fnUserEntry": fnUserEntry,
       "fnUserIndex": fnUserIndex,
       "fnUserName": fnUserName,
       "fnUserAuth": fnUserAuth,
       "fnUserState": fnUserState,
       "fnOptions": fnOptions,
       "fnOptIdleTimeout": fnOptIdleTimeout,
       "fnLogging": fnLogging,
       "fnLogOption": fnLogOption,
       "fnMessages": fnMessages,
       "fnMesgNumber": fnMesgNumber,
       "fnDomains": fnDomains,
       "fnVdNumber": fnVdNumber,
       "fnVdTable": fnVdTable,
       "fnVdEntry": fnVdEntry,
       "fnVdIndex": fnVdIndex,
       "fnVdName": fnVdName,
       "fnIp": fnIp,
       "fnIpSessTable": fnIpSessTable,
       "fnIpSessEntry": fnIpSessEntry,
       "fnIpSessIndex": fnIpSessIndex,
       "fnIpSessProto": fnIpSessProto,
       "fnIpSessFromAddr": fnIpSessFromAddr,
       "fnIpSessFromPort": fnIpSessFromPort,
       "fnIpSessToAddr": fnIpSessToAddr,
       "fnIpSessToPort": fnIpSessToPort,
       "fnIpSessExp": fnIpSessExp,
       "fnVpn": fnVpn,
       "fnVpnDialupTable": fnVpnDialupTable,
       "fnVpnDialupEntry": fnVpnDialupEntry,
       "fnVpnDialupIndex": fnVpnDialupIndex,
       "fnVpnDialupGateway": fnVpnDialupGateway,
       "fnVpnDialupLifetime": fnVpnDialupLifetime,
       "fnVpnDialupTimeout": fnVpnDialupTimeout,
       "fnVpnDialupSrcBegin": fnVpnDialupSrcBegin,
       "fnVpnDialupSrcEnd": fnVpnDialupSrcEnd,
       "fnVpnDialupDstAddr": fnVpnDialupDstAddr,
       "fnIps": fnIps,
       "fnIpsSigId": fnIpsSigId,
       "fnIpsSigSrcIp": fnIpsSigSrcIp,
       "fnBridge": fnBridge,
       "fnBridgeFgtFailure": fnBridgeFgtFailure}
)
