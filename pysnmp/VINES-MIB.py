# SNMP MIB module (VINES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VINES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:36 2024
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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Banyan_ObjectIdentity = ObjectIdentity
banyan = _Banyan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130)
)
_Vinesmibs_ObjectIdentity = ObjectIdentity
vinesmibs = _Vinesmibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1)
)
_Mib1_ObjectIdentity = ObjectIdentity
mib1 = _Mib1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 1)
)
_Mib2_ObjectIdentity = ObjectIdentity
mib2 = _Mib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2)
)
_Systemsummary_ObjectIdentity = ObjectIdentity
systemsummary = _Systemsummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1)
)
_SsName_Type = OctetString
_SsName_Object = MibScalar
ssName = _SsName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 1),
    _SsName_Type()
)
ssName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssName.setStatus("mandatory")
_SsNetid_Type = Integer32
_SsNetid_Object = MibScalar
ssNetid = _SsNetid_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 2),
    _SsNetid_Type()
)
ssNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNetid.setStatus("mandatory")
_SsSwRev_Type = OctetString
_SsSwRev_Object = MibScalar
ssSwRev = _SsSwRev_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 3),
    _SsSwRev_Type()
)
ssSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwRev.setStatus("mandatory")
_SsLoadAvg1_Type = Integer32
_SsLoadAvg1_Object = MibScalar
ssLoadAvg1 = _SsLoadAvg1_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 4),
    _SsLoadAvg1_Type()
)
ssLoadAvg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssLoadAvg1.setStatus("mandatory")
_SsLoadAvg5_Type = Integer32
_SsLoadAvg5_Object = MibScalar
ssLoadAvg5 = _SsLoadAvg5_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 5),
    _SsLoadAvg5_Type()
)
ssLoadAvg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssLoadAvg5.setStatus("mandatory")
_SsLoadAvg15_Type = Integer32
_SsLoadAvg15_Object = MibScalar
ssLoadAvg15 = _SsLoadAvg15_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 6),
    _SsLoadAvg15_Type()
)
ssLoadAvg15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssLoadAvg15.setStatus("mandatory")
_SsMsgAvg1_Type = Integer32
_SsMsgAvg1_Object = MibScalar
ssMsgAvg1 = _SsMsgAvg1_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 7),
    _SsMsgAvg1_Type()
)
ssMsgAvg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssMsgAvg1.setStatus("mandatory")
_SsMsgsIn_Type = Counter32
_SsMsgsIn_Object = MibScalar
ssMsgsIn = _SsMsgsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 8),
    _SsMsgsIn_Type()
)
ssMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssMsgsIn.setStatus("mandatory")
_SsMsgsOut_Type = Counter32
_SsMsgsOut_Object = MibScalar
ssMsgsOut = _SsMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 9),
    _SsMsgsOut_Type()
)
ssMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssMsgsOut.setStatus("mandatory")
_SsDrops_Type = Counter32
_SsDrops_Object = MibScalar
ssDrops = _SsDrops_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 10),
    _SsDrops_Type()
)
ssDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssDrops.setStatus("mandatory")
_SsSwapAvg_Type = Integer32
_SsSwapAvg_Object = MibScalar
ssSwapAvg = _SsSwapAvg_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 11),
    _SsSwapAvg_Type()
)
ssSwapAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwapAvg.setStatus("mandatory")


class _SsProcType_Type(Integer32):
    """Custom type ssProcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("i386", 2),
          ("i486", 3),
          ("other", 1))
    )


_SsProcType_Type.__name__ = "Integer32"
_SsProcType_Object = MibScalar
ssProcType = _SsProcType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 12),
    _SsProcType_Type()
)
ssProcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssProcType.setStatus("mandatory")


class _SsProdType_Type(Integer32):
    """Custom type ssProdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cns", 2),
          ("pcvines", 3),
          ("unused", 1))
    )


_SsProdType_Type.__name__ = "Integer32"
_SsProdType_Object = MibScalar
ssProdType = _SsProdType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 13),
    _SsProdType_Type()
)
ssProdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssProdType.setStatus("mandatory")
_SsProdDescr_Type = OctetString
_SsProdDescr_Object = MibScalar
ssProdDescr = _SsProdDescr_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 14),
    _SsProdDescr_Type()
)
ssProdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssProdDescr.setStatus("mandatory")
_SsRealMemory_Type = Integer32
_SsRealMemory_Object = MibScalar
ssRealMemory = _SsRealMemory_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 15),
    _SsRealMemory_Type()
)
ssRealMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRealMemory.setStatus("mandatory")


class _SsOsType_Type(Integer32):
    """Custom type ssOsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unixsystemv", 1)
    )


_SsOsType_Type.__name__ = "Integer32"
_SsOsType_Object = MibScalar
ssOsType = _SsOsType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 16),
    _SsOsType_Type()
)
ssOsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssOsType.setStatus("mandatory")
_SsOsRev_Type = OctetString
_SsOsRev_Object = MibScalar
ssOsRev = _SsOsRev_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 17),
    _SsOsRev_Type()
)
ssOsRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssOsRev.setStatus("mandatory")
_SsSystemUptime_Type = TimeTicks
_SsSystemUptime_Object = MibScalar
ssSystemUptime = _SsSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 18),
    _SsSystemUptime_Type()
)
ssSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSystemUptime.setStatus("mandatory")
_SsSystemDate_Type = Integer32
_SsSystemDate_Object = MibScalar
ssSystemDate = _SsSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 19),
    _SsSystemDate_Type()
)
ssSystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSystemDate.setStatus("mandatory")


class _SsSystemStatus_Type(Integer32):
    """Custom type ssSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 3),
          ("running", 1),
          ("shutdown", 2))
    )


_SsSystemStatus_Type.__name__ = "Integer32"
_SsSystemStatus_Object = MibScalar
ssSystemStatus = _SsSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 20),
    _SsSystemStatus_Type()
)
ssSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssSystemStatus.setStatus("mandatory")
_SsUserLicenseCfg_Type = Integer32
_SsUserLicenseCfg_Object = MibScalar
ssUserLicenseCfg = _SsUserLicenseCfg_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 1, 21),
    _SsUserLicenseCfg_Type()
)
ssUserLicenseCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssUserLicenseCfg.setStatus("mandatory")
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2)
)
_SvcNumber_Type = Integer32
_SvcNumber_Object = MibScalar
svcNumber = _SvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 1),
    _SvcNumber_Type()
)
svcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcNumber.setStatus("mandatory")
_SvcTable_Object = MibTable
svcTable = _SvcTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    svcTable.setStatus("mandatory")
_SvcEntry_Object = MibTableRow
svcEntry = _SvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1)
)
svcEntry.setIndexNames(
    (0, "VINES-MIB", "svcIndex"),
)
if mibBuilder.loadTexts:
    svcEntry.setStatus("mandatory")
_SvcIndex_Type = Integer32
_SvcIndex_Object = MibTableColumn
svcIndex = _SvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 1),
    _SvcIndex_Type()
)
svcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcIndex.setStatus("mandatory")
_SvcName_Type = OctetString
_SvcName_Object = MibTableColumn
svcName = _SvcName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 2),
    _SvcName_Type()
)
svcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcName.setStatus("mandatory")


class _SvcStatus_Type(Integer32):
    """Custom type svcStatus based on Integer32"""
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
        *(("crashing", 3),
          ("inconsistent", 4),
          ("initializing", 2),
          ("running", 1),
          ("stopped", 5))
    )


_SvcStatus_Type.__name__ = "Integer32"
_SvcStatus_Object = MibTableColumn
svcStatus = _SvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 3),
    _SvcStatus_Type()
)
svcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcStatus.setStatus("mandatory")
_SvcUpTime_Type = TimeTicks
_SvcUpTime_Object = MibTableColumn
svcUpTime = _SvcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 4),
    _SvcUpTime_Type()
)
svcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcUpTime.setStatus("mandatory")
_SvcMsgsIn_Type = Counter32
_SvcMsgsIn_Object = MibTableColumn
svcMsgsIn = _SvcMsgsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 5),
    _SvcMsgsIn_Type()
)
svcMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMsgsIn.setStatus("mandatory")
_SvcMsgsOut_Type = Counter32
_SvcMsgsOut_Object = MibTableColumn
svcMsgsOut = _SvcMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 6),
    _SvcMsgsOut_Type()
)
svcMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcMsgsOut.setStatus("mandatory")
_SvcLocIn_Type = Counter32
_SvcLocIn_Object = MibTableColumn
svcLocIn = _SvcLocIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 7),
    _SvcLocIn_Type()
)
svcLocIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcLocIn.setStatus("mandatory")
_SvcLocOut_Type = Counter32
_SvcLocOut_Object = MibTableColumn
svcLocOut = _SvcLocOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 8),
    _SvcLocOut_Type()
)
svcLocOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcLocOut.setStatus("mandatory")
_SvcActSess_Type = Integer32
_SvcActSess_Object = MibTableColumn
svcActSess = _SvcActSess_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 9),
    _SvcActSess_Type()
)
svcActSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcActSess.setStatus("mandatory")
_SvcTotSess_Type = Counter32
_SvcTotSess_Object = MibTableColumn
svcTotSess = _SvcTotSess_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 10),
    _SvcTotSess_Type()
)
svcTotSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTotSess.setStatus("mandatory")
_SvcCategory_Type = Integer32
_SvcCategory_Object = MibTableColumn
svcCategory = _SvcCategory_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 11),
    _SvcCategory_Type()
)
svcCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcCategory.setStatus("mandatory")
_SvcCpuTime_Type = TimeTicks
_SvcCpuTime_Object = MibTableColumn
svcCpuTime = _SvcCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 12),
    _SvcCpuTime_Type()
)
svcCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcCpuTime.setStatus("mandatory")
_SvcSize_Type = Integer32
_SvcSize_Object = MibTableColumn
svcSize = _SvcSize_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 13),
    _SvcSize_Type()
)
svcSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSize.setStatus("mandatory")
_SvcSockets_Type = Integer32
_SvcSockets_Object = MibTableColumn
svcSockets = _SvcSockets_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 14),
    _SvcSockets_Type()
)
svcSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSockets.setStatus("mandatory")
_SvcSPPs_Type = Integer32
_SvcSPPs_Object = MibTableColumn
svcSPPs = _SvcSPPs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 15),
    _SvcSPPs_Type()
)
svcSPPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcSPPs.setStatus("mandatory")


class _SvcLogMask_Type(Integer32):
    """Custom type svcLogMask based on Integer32"""
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
        *(("maskdef", 1),
          ("maskhigh", 4),
          ("masklow", 2),
          ("maskmed", 3))
    )


_SvcLogMask_Type.__name__ = "Integer32"
_SvcLogMask_Object = MibTableColumn
svcLogMask = _SvcLogMask_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 16),
    _SvcLogMask_Type()
)
svcLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcLogMask.setStatus("mandatory")
_SvcDiskName_Type = OctetString
_SvcDiskName_Object = MibTableColumn
svcDiskName = _SvcDiskName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 2, 1, 17),
    _SvcDiskName_Type()
)
svcDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcDiskName.setStatus("mandatory")
_SvcUserTable_Object = MibTable
svcUserTable = _SvcUserTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    svcUserTable.setStatus("mandatory")
_SvcUserEntry_Object = MibTableRow
svcUserEntry = _SvcUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 3, 1)
)
svcUserEntry.setIndexNames(
    (0, "VINES-MIB", "svcUserSvcIndex"),
    (0, "VINES-MIB", "svcUserIndex"),
)
if mibBuilder.loadTexts:
    svcUserEntry.setStatus("mandatory")
_SvcUserSvcIndex_Type = Integer32
_SvcUserSvcIndex_Object = MibTableColumn
svcUserSvcIndex = _SvcUserSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 3, 1, 1),
    _SvcUserSvcIndex_Type()
)
svcUserSvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcUserSvcIndex.setStatus("mandatory")
_SvcUserIndex_Type = Integer32
_SvcUserIndex_Object = MibTableColumn
svcUserIndex = _SvcUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 3, 1, 2),
    _SvcUserIndex_Type()
)
svcUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcUserIndex.setStatus("mandatory")
_SvcUserSvcName_Type = OctetString
_SvcUserSvcName_Object = MibTableColumn
svcUserSvcName = _SvcUserSvcName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 3, 1, 3),
    _SvcUserSvcName_Type()
)
svcUserSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcUserSvcName.setStatus("mandatory")
_SvcUserName_Type = OctetString
_SvcUserName_Object = MibTableColumn
svcUserName = _SvcUserName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 2, 3, 1, 4),
    _SvcUserName_Type()
)
svcUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcUserName.setStatus("mandatory")
_Peripherals_ObjectIdentity = ObjectIdentity
peripherals = _Peripherals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3)
)
_DskNumber_Type = Integer32
_DskNumber_Object = MibScalar
dskNumber = _DskNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 1),
    _DskNumber_Type()
)
dskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskNumber.setStatus("mandatory")
_DskTable_Object = MibTable
dskTable = _DskTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dskTable.setStatus("mandatory")
_DskEntry_Object = MibTableRow
dskEntry = _DskEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1)
)
dskEntry.setIndexNames(
    (0, "VINES-MIB", "dskIndex"),
)
if mibBuilder.loadTexts:
    dskEntry.setStatus("mandatory")
_DskIndex_Type = Integer32
_DskIndex_Object = MibTableColumn
dskIndex = _DskIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 1),
    _DskIndex_Type()
)
dskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskIndex.setStatus("mandatory")
_DskName_Type = OctetString
_DskName_Object = MibTableColumn
dskName = _DskName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 2),
    _DskName_Type()
)
dskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskName.setStatus("mandatory")
_DskUtil_Type = Integer32
_DskUtil_Object = MibTableColumn
dskUtil = _DskUtil_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 3),
    _DskUtil_Type()
)
dskUtil.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dskUtil.setStatus("mandatory")
_DskDemand_Type = Integer32
_DskDemand_Object = MibTableColumn
dskDemand = _DskDemand_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 4),
    _DskDemand_Type()
)
dskDemand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dskDemand.setStatus("mandatory")
_DskSizeMB_Type = Integer32
_DskSizeMB_Object = MibTableColumn
dskSizeMB = _DskSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 5),
    _DskSizeMB_Type()
)
dskSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskSizeMB.setStatus("mandatory")
_DskUsedPct_Type = Integer32
_DskUsedPct_Object = MibTableColumn
dskUsedPct = _DskUsedPct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 6),
    _DskUsedPct_Type()
)
dskUsedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsedPct.setStatus("mandatory")


class _DskStatus_Type(Integer32):
    """Custom type dskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_DskStatus_Type.__name__ = "Integer32"
_DskStatus_Object = MibTableColumn
dskStatus = _DskStatus_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 7),
    _DskStatus_Type()
)
dskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskStatus.setStatus("mandatory")
_DskNOperations_Type = Counter32
_DskNOperations_Object = MibTableColumn
dskNOperations = _DskNOperations_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 8),
    _DskNOperations_Type()
)
dskNOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskNOperations.setStatus("mandatory")
_DskNBlocks_Type = Counter32
_DskNBlocks_Object = MibTableColumn
dskNBlocks = _DskNBlocks_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 9),
    _DskNBlocks_Type()
)
dskNBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskNBlocks.setStatus("mandatory")
_DskResp_Type = TimeTicks
_DskResp_Object = MibTableColumn
dskResp = _DskResp_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 10),
    _DskResp_Type()
)
dskResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskResp.setStatus("mandatory")
_DskActive_Type = TimeTicks
_DskActive_Object = MibTableColumn
dskActive = _DskActive_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 11),
    _DskActive_Type()
)
dskActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskActive.setStatus("mandatory")
_DskBlkSize_Type = Integer32
_DskBlkSize_Object = MibTableColumn
dskBlkSize = _DskBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 12),
    _DskBlkSize_Type()
)
dskBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskBlkSize.setStatus("mandatory")
_DskNMisc_Type = Counter32
_DskNMisc_Object = MibTableColumn
dskNMisc = _DskNMisc_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 13),
    _DskNMisc_Type()
)
dskNMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskNMisc.setStatus("mandatory")
_DskNErrs_Type = Counter32
_DskNErrs_Object = MibTableColumn
dskNErrs = _DskNErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 14),
    _DskNErrs_Type()
)
dskNErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskNErrs.setStatus("mandatory")
_DskPctBusy_Type = Integer32
_DskPctBusy_Object = MibTableColumn
dskPctBusy = _DskPctBusy_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 15),
    _DskPctBusy_Type()
)
dskPctBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPctBusy.setStatus("optional")
_DskAvgWait_Type = Integer32
_DskAvgWait_Object = MibTableColumn
dskAvgWait = _DskAvgWait_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 16),
    _DskAvgWait_Type()
)
dskAvgWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvgWait.setStatus("optional")
_DskAvgService_Type = Integer32
_DskAvgService_Object = MibTableColumn
dskAvgService = _DskAvgService_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 3, 2, 1, 17),
    _DskAvgService_Type()
)
dskAvgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvgService.setStatus("optional")
_Filesystem_ObjectIdentity = ObjectIdentity
filesystem = _Filesystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4)
)
_FsTotCache_Type = Integer32
_FsTotCache_Object = MibScalar
fsTotCache = _FsTotCache_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 1),
    _FsTotCache_Type()
)
fsTotCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTotCache.setStatus("mandatory")
_FsCacheBufSize_Type = Integer32
_FsCacheBufSize_Object = MibScalar
fsCacheBufSize = _FsCacheBufSize_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 2),
    _FsCacheBufSize_Type()
)
fsCacheBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCacheBufSize.setStatus("mandatory")
_FsMaxOpenFiles_Type = Integer32
_FsMaxOpenFiles_Object = MibScalar
fsMaxOpenFiles = _FsMaxOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 3),
    _FsMaxOpenFiles_Type()
)
fsMaxOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMaxOpenFiles.setStatus("mandatory")
_FsOpenFiles_Type = Integer32
_FsOpenFiles_Object = MibScalar
fsOpenFiles = _FsOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 4),
    _FsOpenFiles_Type()
)
fsOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOpenFiles.setStatus("mandatory")
_FsMaxOpensOnFiles_Type = Integer32
_FsMaxOpensOnFiles_Object = MibScalar
fsMaxOpensOnFiles = _FsMaxOpensOnFiles_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 5),
    _FsMaxOpensOnFiles_Type()
)
fsMaxOpensOnFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMaxOpensOnFiles.setStatus("mandatory")
_FsOpensOnFiles_Type = Integer32
_FsOpensOnFiles_Object = MibScalar
fsOpensOnFiles = _FsOpensOnFiles_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 6),
    _FsOpensOnFiles_Type()
)
fsOpensOnFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOpensOnFiles.setStatus("mandatory")
_FsRecLocks_Type = Integer32
_FsRecLocks_Object = MibScalar
fsRecLocks = _FsRecLocks_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 7),
    _FsRecLocks_Type()
)
fsRecLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRecLocks.setStatus("mandatory")
_FsMaxRecLocks_Type = Integer32
_FsMaxRecLocks_Object = MibScalar
fsMaxRecLocks = _FsMaxRecLocks_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 8),
    _FsMaxRecLocks_Type()
)
fsMaxRecLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMaxRecLocks.setStatus("mandatory")
_FsPctCacheHits_Type = Integer32
_FsPctCacheHits_Object = MibScalar
fsPctCacheHits = _FsPctCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 9),
    _FsPctCacheHits_Type()
)
fsPctCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPctCacheHits.setStatus("mandatory")
_FsCacheUnavail_Type = Counter32
_FsCacheUnavail_Object = MibScalar
fsCacheUnavail = _FsCacheUnavail_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 4, 10),
    _FsCacheUnavail_Type()
)
fsCacheUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCacheUnavail.setStatus("mandatory")
_Commresources_ObjectIdentity = ObjectIdentity
commresources = _Commresources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 5)
)
_CommTotBufs_Type = Integer32
_CommTotBufs_Object = MibScalar
commTotBufs = _CommTotBufs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 5, 1),
    _CommTotBufs_Type()
)
commTotBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTotBufs.setStatus("mandatory")
_CommBufUsage_Type = Integer32
_CommBufUsage_Object = MibScalar
commBufUsage = _CommBufUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 5, 2),
    _CommBufUsage_Type()
)
commBufUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commBufUsage.setStatus("mandatory")
_CommAllocsFailed_Type = Counter32
_CommAllocsFailed_Object = MibScalar
commAllocsFailed = _CommAllocsFailed_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 5, 3),
    _CommAllocsFailed_Type()
)
commAllocsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commAllocsFailed.setStatus("mandatory")
_CommSocksCfg_Type = Integer32
_CommSocksCfg_Object = MibScalar
commSocksCfg = _CommSocksCfg_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 5, 4),
    _CommSocksCfg_Type()
)
commSocksCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSocksCfg.setStatus("mandatory")
_CommSocksInUse_Type = Integer32
_CommSocksInUse_Object = MibScalar
commSocksInUse = _CommSocksInUse_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 5, 5),
    _CommSocksInUse_Type()
)
commSocksInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commSocksInUse.setStatus("mandatory")
_CommMaxOpenSocks_Type = Integer32
_CommMaxOpenSocks_Object = MibScalar
commMaxOpenSocks = _CommMaxOpenSocks_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 5, 6),
    _CommMaxOpenSocks_Type()
)
commMaxOpenSocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commMaxOpenSocks.setStatus("mandatory")
_Vip_ObjectIdentity = ObjectIdentity
vip = _Vip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6)
)
_VipTotIn_Type = Counter32
_VipTotIn_Object = MibScalar
vipTotIn = _VipTotIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 1),
    _VipTotIn_Type()
)
vipTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipTotIn.setStatus("mandatory")
_VipTotOut_Type = Counter32
_VipTotOut_Object = MibScalar
vipTotOut = _VipTotOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 2),
    _VipTotOut_Type()
)
vipTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipTotOut.setStatus("mandatory")
_VipBad_Type = Counter32
_VipBad_Object = MibScalar
vipBad = _VipBad_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 3),
    _VipBad_Type()
)
vipBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipBad.setStatus("mandatory")
_VipRouted_Type = Counter32
_VipRouted_Object = MibScalar
vipRouted = _VipRouted_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 4),
    _VipRouted_Type()
)
vipRouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipRouted.setStatus("mandatory")
_VipRoutedHWM_Type = Integer32
_VipRoutedHWM_Object = MibScalar
vipRoutedHWM = _VipRoutedHWM_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 5),
    _VipRoutedHWM_Type()
)
vipRoutedHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipRoutedHWM.setStatus("mandatory")
_VipBcast_Type = Counter32
_VipBcast_Object = MibScalar
vipBcast = _VipBcast_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 6),
    _VipBcast_Type()
)
vipBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipBcast.setStatus("mandatory")
_VipBcastHWM_Type = Integer32
_VipBcastHWM_Object = MibScalar
vipBcastHWM = _VipBcastHWM_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 7),
    _VipBcastHWM_Type()
)
vipBcastHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipBcastHWM.setStatus("mandatory")
_VipReass_Type = Counter32
_VipReass_Object = MibScalar
vipReass = _VipReass_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 8),
    _VipReass_Type()
)
vipReass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipReass.setStatus("mandatory")
_VipFrags_Type = Counter32
_VipFrags_Object = MibScalar
vipFrags = _VipFrags_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 9),
    _VipFrags_Type()
)
vipFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipFrags.setStatus("mandatory")
_VipToDodIP_Type = Counter32
_VipToDodIP_Object = MibScalar
vipToDodIP = _VipToDodIP_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 10),
    _VipToDodIP_Type()
)
vipToDodIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipToDodIP.setStatus("mandatory")
_VipFromDodIP_Type = Counter32
_VipFromDodIP_Object = MibScalar
vipFromDodIP = _VipFromDodIP_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 11),
    _VipFromDodIP_Type()
)
vipFromDodIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipFromDodIP.setStatus("mandatory")
_VipInFragments_Type = Counter32
_VipInFragments_Object = MibScalar
vipInFragments = _VipInFragments_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 12),
    _VipInFragments_Type()
)
vipInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipInFragments.setStatus("mandatory")
_VipTooSmall_Type = Counter32
_VipTooSmall_Object = MibScalar
vipTooSmall = _VipTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 13),
    _VipTooSmall_Type()
)
vipTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipTooSmall.setStatus("mandatory")
_VipBadLength_Type = Counter32
_VipBadLength_Object = MibScalar
vipBadLength = _VipBadLength_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 14),
    _VipBadLength_Type()
)
vipBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipBadLength.setStatus("mandatory")
_VipNoBuffers_Type = Counter32
_VipNoBuffers_Object = MibScalar
vipNoBuffers = _VipNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 6, 15),
    _VipNoBuffers_Type()
)
vipNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vipNoBuffers.setStatus("mandatory")
_Vrtp_ObjectIdentity = ObjectIdentity
vrtp = _Vrtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7)
)
_VrtpNbrNumber_Type = Integer32
_VrtpNbrNumber_Object = MibScalar
vrtpNbrNumber = _VrtpNbrNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 1),
    _VrtpNbrNumber_Type()
)
vrtpNbrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrNumber.setStatus("mandatory")
_VrtpNbrTable_Object = MibTable
vrtpNbrTable = _VrtpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    vrtpNbrTable.setStatus("mandatory")
_VrtpNbrEntry_Object = MibTableRow
vrtpNbrEntry = _VrtpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1)
)
vrtpNbrEntry.setIndexNames(
    (0, "VINES-MIB", "vrtpNbrNetid"),
    (0, "VINES-MIB", "vrtpNbrSubNetid"),
    (0, "VINES-MIB", "vrtpNbrIfType"),
    (0, "VINES-MIB", "vrtpNbrLocSlot"),
    (0, "VINES-MIB", "vrtpNbrLocLine"),
)
if mibBuilder.loadTexts:
    vrtpNbrEntry.setStatus("mandatory")
_VrtpNbrNetid_Type = Integer32
_VrtpNbrNetid_Object = MibTableColumn
vrtpNbrNetid = _VrtpNbrNetid_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 1),
    _VrtpNbrNetid_Type()
)
vrtpNbrNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrNetid.setStatus("mandatory")
_VrtpNbrSubNetid_Type = Integer32
_VrtpNbrSubNetid_Object = MibTableColumn
vrtpNbrSubNetid = _VrtpNbrSubNetid_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 2),
    _VrtpNbrSubNetid_Type()
)
vrtpNbrSubNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrSubNetid.setStatus("mandatory")


class _VrtpNbrType_Type(Integer32):
    """Custom type vrtpNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("workstation", 2))
    )


_VrtpNbrType_Type.__name__ = "Integer32"
_VrtpNbrType_Object = MibTableColumn
vrtpNbrType = _VrtpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 3),
    _VrtpNbrType_Type()
)
vrtpNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrType.setStatus("mandatory")


class _VrtpNbrIfType_Type(Integer32):
    """Custom type vrtpNbrIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              99,
              100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 73),
          ("arcnetNDIS", 70),
          ("arcnetSMC", 6),
          ("arcnetSMCMC", 39),
          ("blkAsync", 12),
          ("ctrlerDATACO", 49),
          ("ctrllerGanges", 22),
          ("etherExpressIntel", 81),
          ("etherLink3COM16", 75),
          ("ethernet3Com", 1),
          ("ethernet3Com3C503", 31),
          ("ethernet3Com3C523", 32),
          ("ethernetBICC", 58),
          ("ethernetBICCMC", 78),
          ("ethernetCabletron", 68),
          ("ethernetDGCODE", 90),
          ("ethernetEplus3Com", 20),
          ("ethernetIBMMC", 54),
          ("ethernetICAMC", 42),
          ("ethernetIntelPC586E", 36),
          ("ethernetNDIS", 51),
          ("ethernetNI5010", 2),
          ("ethernetNI5210", 23),
          ("ethernetNI9210MC", 41),
          ("ethernetNT2R15", 59),
          ("ethernetNTMC", 60),
          ("ethernetNTTurbo", 61),
          ("ethernetNovellNE", 48),
          ("ethernetNovellNE3200", 65),
          ("ethernetPureData", 66),
          ("ethernetPureDataMC", 67),
          ("ethernetUB", 4),
          ("ethernetWDigital", 28),
          ("ethernetWDigitalMC", 56),
          ("frag", 9),
          ("ftp", 69),
          ("gatewayAPI", 52),
          ("hdlc", 11),
          ("hdlcTCPIP", 26),
          ("hughes", 50),
          ("icaPlus", 79),
          ("interlanEISA", 57),
          ("interlanNI6510", 76),
          ("intersys", 13),
          ("ipBanyan", 25),
          ("ipNSRouting", 80),
          ("ipTCPIP", 24),
          ("ipaDavidSys", 18),
          ("isdnBRIDatavoice", 91),
          ("isdnDchannel", 103),
          ("isoSvrSvr", 64),
          ("lanLinkNT", 21),
          ("lanLinkNTMC", 34),
          ("lapdT1", 102),
          ("llTurboNT", 46),
          ("localTalk", 74),
          ("omninetCorvus", 5),
          ("pcnetSytek", 7),
          ("proNetProteon", 8),
          ("promptusE1", 101),
          ("promptusT1", 100),
          ("pronetProteonMC", 38),
          ("prsystctrl", 10),
          ("ps2UBNICMC", 45),
          ("pseudoIBM", 43),
          ("serialVGsystems", 35),
          ("starlanATT", 29),
          ("starlanATT10", 37),
          ("starlanATT10MC", 44),
          ("starlanATTEISA", 72),
          ("starlanNI5210", 30),
          ("starlanWDigital", 27),
          ("tokenExpressIntelEISA", 87),
          ("tokenExpressIntelISA", 85),
          ("tokenExpressIntelMC", 86),
          ("tokenRing3Com3C603", 33),
          ("tokenRingCompaq", 63),
          ("tokenRingIBM", 15),
          ("tokenRingIBMBM", 55),
          ("tokenRingIBMMC", 40),
          ("tokenRingIrmaTracMCA", 89),
          ("tokenRingIrmaTracPCAT", 88),
          ("tokenRingMadge", 53),
          ("tokenRingNDIS", 71),
          ("tokenRingOlicamEISA", 84),
          ("tokenRingOlicom", 82),
          ("tokenRingOlicomMC", 83),
          ("tokenRingPronet", 62),
          ("tokenRingPronet4", 19),
          ("tokenRingProteon", 47),
          ("tokenRingProteonP1890", 77),
          ("tokenRingUB", 17),
          ("unused", 99),
          ("wavelanNCR", 92),
          ("x25", 16),
          ("x25EICON", 14))
    )


_VrtpNbrIfType_Type.__name__ = "Integer32"
_VrtpNbrIfType_Object = MibTableColumn
vrtpNbrIfType = _VrtpNbrIfType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 4),
    _VrtpNbrIfType_Type()
)
vrtpNbrIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrIfType.setStatus("mandatory")
_VrtpNbrRemAddress_Type = OctetString
_VrtpNbrRemAddress_Object = MibTableColumn
vrtpNbrRemAddress = _VrtpNbrRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 5),
    _VrtpNbrRemAddress_Type()
)
vrtpNbrRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrRemAddress.setStatus("mandatory")
_VrtpNbrLocAddress_Type = OctetString
_VrtpNbrLocAddress_Object = MibTableColumn
vrtpNbrLocAddress = _VrtpNbrLocAddress_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 6),
    _VrtpNbrLocAddress_Type()
)
vrtpNbrLocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrLocAddress.setStatus("mandatory")
_VrtpNbrLocSlot_Type = Integer32
_VrtpNbrLocSlot_Object = MibTableColumn
vrtpNbrLocSlot = _VrtpNbrLocSlot_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 7),
    _VrtpNbrLocSlot_Type()
)
vrtpNbrLocSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrLocSlot.setStatus("mandatory")
_VrtpNbrLocLine_Type = Integer32
_VrtpNbrLocLine_Object = MibTableColumn
vrtpNbrLocLine = _VrtpNbrLocLine_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 8),
    _VrtpNbrLocLine_Type()
)
vrtpNbrLocLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrLocLine.setStatus("mandatory")
_VrtpNbrSvrName_Type = OctetString
_VrtpNbrSvrName_Object = MibTableColumn
vrtpNbrSvrName = _VrtpNbrSvrName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 2, 1, 9),
    _VrtpNbrSvrName_Type()
)
vrtpNbrSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrSvrName.setStatus("optional")
_VrtpRtNumber_Type = Integer32
_VrtpRtNumber_Object = MibScalar
vrtpRtNumber = _VrtpRtNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 3),
    _VrtpRtNumber_Type()
)
vrtpRtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtNumber.setStatus("mandatory")
_VrtpRtTable_Object = MibTable
vrtpRtTable = _VrtpRtTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4)
)
if mibBuilder.loadTexts:
    vrtpRtTable.setStatus("mandatory")
_VrtpRtEntry_Object = MibTableRow
vrtpRtEntry = _VrtpRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4, 1)
)
vrtpRtEntry.setIndexNames(
    (0, "VINES-MIB", "vrtpRtNetid"),
)
if mibBuilder.loadTexts:
    vrtpRtEntry.setStatus("mandatory")
_VrtpRtNetid_Type = Integer32
_VrtpRtNetid_Object = MibTableColumn
vrtpRtNetid = _VrtpRtNetid_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4, 1, 1),
    _VrtpRtNetid_Type()
)
vrtpRtNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtNetid.setStatus("mandatory")
_VrtpRtMetric_Type = Integer32
_VrtpRtMetric_Object = MibTableColumn
vrtpRtMetric = _VrtpRtMetric_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4, 1, 2),
    _VrtpRtMetric_Type()
)
vrtpRtMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtMetric.setStatus("mandatory")
_VrtpRtIdle_Type = Integer32
_VrtpRtIdle_Object = MibTableColumn
vrtpRtIdle = _VrtpRtIdle_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4, 1, 3),
    _VrtpRtIdle_Type()
)
vrtpRtIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtIdle.setStatus("mandatory")
_VrtpRtGateNetid_Type = Integer32
_VrtpRtGateNetid_Object = MibTableColumn
vrtpRtGateNetid = _VrtpRtGateNetid_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4, 1, 4),
    _VrtpRtGateNetid_Type()
)
vrtpRtGateNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtGateNetid.setStatus("mandatory")
_VrtpRtSvrName_Type = OctetString
_VrtpRtSvrName_Object = MibTableColumn
vrtpRtSvrName = _VrtpRtSvrName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4, 1, 5),
    _VrtpRtSvrName_Type()
)
vrtpRtSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtSvrName.setStatus("optional")
_VrtpRtGateSvrName_Type = OctetString
_VrtpRtGateSvrName_Object = MibTableColumn
vrtpRtGateSvrName = _VrtpRtGateSvrName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 4, 1, 6),
    _VrtpRtGateSvrName_Type()
)
vrtpRtGateSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtGateSvrName.setStatus("optional")
_VrtpTotIn_Type = Counter32
_VrtpTotIn_Object = MibScalar
vrtpTotIn = _VrtpTotIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 5),
    _VrtpTotIn_Type()
)
vrtpTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpTotIn.setStatus("mandatory")
_VrtpTotOut_Type = Counter32
_VrtpTotOut_Object = MibScalar
vrtpTotOut = _VrtpTotOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 6),
    _VrtpTotOut_Type()
)
vrtpTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpTotOut.setStatus("mandatory")
_VrtpErrsIn_Type = Counter32
_VrtpErrsIn_Object = MibScalar
vrtpErrsIn = _VrtpErrsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 7),
    _VrtpErrsIn_Type()
)
vrtpErrsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpErrsIn.setStatus("mandatory")
_VrtpNoBuffersIn_Type = Counter32
_VrtpNoBuffersIn_Object = MibScalar
vrtpNoBuffersIn = _VrtpNoBuffersIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 8),
    _VrtpNoBuffersIn_Type()
)
vrtpNoBuffersIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNoBuffersIn.setStatus("optional")
_VrtpUpdatesIn_Type = Counter32
_VrtpUpdatesIn_Object = MibScalar
vrtpUpdatesIn = _VrtpUpdatesIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 9),
    _VrtpUpdatesIn_Type()
)
vrtpUpdatesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpUpdatesIn.setStatus("optional")
_VrtpResponsesIn_Type = Counter32
_VrtpResponsesIn_Object = MibScalar
vrtpResponsesIn = _VrtpResponsesIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 10),
    _VrtpResponsesIn_Type()
)
vrtpResponsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpResponsesIn.setStatus("optional")
_VrtpRqstsIn_Type = Counter32
_VrtpRqstsIn_Object = MibScalar
vrtpRqstsIn = _VrtpRqstsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 11),
    _VrtpRqstsIn_Type()
)
vrtpRqstsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRqstsIn.setStatus("optional")
_VrtpRqstLkUpIn_Type = Counter32
_VrtpRqstLkUpIn_Object = MibScalar
vrtpRqstLkUpIn = _VrtpRqstLkUpIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 12),
    _VrtpRqstLkUpIn_Type()
)
vrtpRqstLkUpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRqstLkUpIn.setStatus("optional")
_VrtpRqstSlrInfoIn_Type = Counter32
_VrtpRqstSlrInfoIn_Object = MibScalar
vrtpRqstSlrInfoIn = _VrtpRqstSlrInfoIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 13),
    _VrtpRqstSlrInfoIn_Type()
)
vrtpRqstSlrInfoIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRqstSlrInfoIn.setStatus("optional")
_VrtpReinitIn_Type = Counter32
_VrtpReinitIn_Object = MibScalar
vrtpReinitIn = _VrtpReinitIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 14),
    _VrtpReinitIn_Type()
)
vrtpReinitIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpReinitIn.setStatus("optional")
_VrtpResyncIn_Type = Counter32
_VrtpResyncIn_Object = MibScalar
vrtpResyncIn = _VrtpResyncIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 15),
    _VrtpResyncIn_Type()
)
vrtpResyncIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpResyncIn.setStatus("optional")
_VrtpRedirIn_Type = Counter32
_VrtpRedirIn_Object = MibScalar
vrtpRedirIn = _VrtpRedirIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 16),
    _VrtpRedirIn_Type()
)
vrtpRedirIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRedirIn.setStatus("optional")
_VrtpFragsIn_Type = Counter32
_VrtpFragsIn_Object = MibScalar
vrtpFragsIn = _VrtpFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 17),
    _VrtpFragsIn_Type()
)
vrtpFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsIn.setStatus("optional")
_VrtpFragsDropIn_Type = Counter32
_VrtpFragsDropIn_Object = MibScalar
vrtpFragsDropIn = _VrtpFragsDropIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 18),
    _VrtpFragsDropIn_Type()
)
vrtpFragsDropIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsDropIn.setStatus("optional")
_VrtpFragsBadIn_Type = Counter32
_VrtpFragsBadIn_Object = MibScalar
vrtpFragsBadIn = _VrtpFragsBadIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 19),
    _VrtpFragsBadIn_Type()
)
vrtpFragsBadIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsBadIn.setStatus("optional")
_VrtpFragsDupIn_Type = Counter32
_VrtpFragsDupIn_Object = MibScalar
vrtpFragsDupIn = _VrtpFragsDupIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 20),
    _VrtpFragsDupIn_Type()
)
vrtpFragsDupIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsDupIn.setStatus("optional")
_VrtpFragsDoneIn_Type = Counter32
_VrtpFragsDoneIn_Object = MibScalar
vrtpFragsDoneIn = _VrtpFragsDoneIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 21),
    _VrtpFragsDoneIn_Type()
)
vrtpFragsDoneIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsDoneIn.setStatus("optional")
_VrtpReassBadIn_Type = Counter32
_VrtpReassBadIn_Object = MibScalar
vrtpReassBadIn = _VrtpReassBadIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 22),
    _VrtpReassBadIn_Type()
)
vrtpReassBadIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpReassBadIn.setStatus("optional")
_VrtpOutdatedIn_Type = Counter32
_VrtpOutdatedIn_Object = MibScalar
vrtpOutdatedIn = _VrtpOutdatedIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 23),
    _VrtpOutdatedIn_Type()
)
vrtpOutdatedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpOutdatedIn.setStatus("optional")
_VrtpNetInfoBad_Type = Counter32
_VrtpNetInfoBad_Object = MibScalar
vrtpNetInfoBad = _VrtpNetInfoBad_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 24),
    _VrtpNetInfoBad_Type()
)
vrtpNetInfoBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNetInfoBad.setStatus("optional")
_VrtpBadRdrs_Type = Counter32
_VrtpBadRdrs_Object = MibScalar
vrtpBadRdrs = _VrtpBadRdrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 25),
    _VrtpBadRdrs_Type()
)
vrtpBadRdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpBadRdrs.setStatus("optional")
_VrtpBdcstIn_Type = Counter32
_VrtpBdcstIn_Object = MibScalar
vrtpBdcstIn = _VrtpBdcstIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 26),
    _VrtpBdcstIn_Type()
)
vrtpBdcstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpBdcstIn.setStatus("optional")
_VrtpNoBuffersOut_Type = Counter32
_VrtpNoBuffersOut_Object = MibScalar
vrtpNoBuffersOut = _VrtpNoBuffersOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 27),
    _VrtpNoBuffersOut_Type()
)
vrtpNoBuffersOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNoBuffersOut.setStatus("optional")
_VrtpUpdatesOut_Type = Counter32
_VrtpUpdatesOut_Object = MibScalar
vrtpUpdatesOut = _VrtpUpdatesOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 28),
    _VrtpUpdatesOut_Type()
)
vrtpUpdatesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpUpdatesOut.setStatus("optional")
_VrtpRqstLkUpOut_Type = Counter32
_VrtpRqstLkUpOut_Object = MibScalar
vrtpRqstLkUpOut = _VrtpRqstLkUpOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 29),
    _VrtpRqstLkUpOut_Type()
)
vrtpRqstLkUpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRqstLkUpOut.setStatus("optional")
_VrtpRqstSlrInfoOut_Type = Counter32
_VrtpRqstSlrInfoOut_Object = MibScalar
vrtpRqstSlrInfoOut = _VrtpRqstSlrInfoOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 30),
    _VrtpRqstSlrInfoOut_Type()
)
vrtpRqstSlrInfoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRqstSlrInfoOut.setStatus("optional")
_VrtpRqstsOut_Type = Counter32
_VrtpRqstsOut_Object = MibScalar
vrtpRqstsOut = _VrtpRqstsOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 31),
    _VrtpRqstsOut_Type()
)
vrtpRqstsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRqstsOut.setStatus("optional")
_VrtpReinitOut_Type = Counter32
_VrtpReinitOut_Object = MibScalar
vrtpReinitOut = _VrtpReinitOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 32),
    _VrtpReinitOut_Type()
)
vrtpReinitOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpReinitOut.setStatus("optional")
_VrtpResyncOut_Type = Counter32
_VrtpResyncOut_Object = MibScalar
vrtpResyncOut = _VrtpResyncOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 33),
    _VrtpResyncOut_Type()
)
vrtpResyncOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpResyncOut.setStatus("optional")
_VrtpRedirOut_Type = Counter32
_VrtpRedirOut_Object = MibScalar
vrtpRedirOut = _VrtpRedirOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 34),
    _VrtpRedirOut_Type()
)
vrtpRedirOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRedirOut.setStatus("optional")
_VrtpFragsOut_Type = Counter32
_VrtpFragsOut_Object = MibScalar
vrtpFragsOut = _VrtpFragsOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 35),
    _VrtpFragsOut_Type()
)
vrtpFragsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsOut.setStatus("optional")
_VrtpFragsDoneOut_Type = Counter32
_VrtpFragsDoneOut_Object = MibScalar
vrtpFragsDoneOut = _VrtpFragsDoneOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 36),
    _VrtpFragsDoneOut_Type()
)
vrtpFragsDoneOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsDoneOut.setStatus("optional")
_VrtpFragsBadOut_Type = Counter32
_VrtpFragsBadOut_Object = MibScalar
vrtpFragsBadOut = _VrtpFragsBadOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 37),
    _VrtpFragsBadOut_Type()
)
vrtpFragsBadOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsBadOut.setStatus("optional")
_VrtpFragsDropOut_Type = Counter32
_VrtpFragsDropOut_Object = MibScalar
vrtpFragsDropOut = _VrtpFragsDropOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 38),
    _VrtpFragsDropOut_Type()
)
vrtpFragsDropOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpFragsDropOut.setStatus("optional")
_VrtpBdcstOut_Type = Counter32
_VrtpBdcstOut_Object = MibScalar
vrtpBdcstOut = _VrtpBdcstOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 39),
    _VrtpBdcstOut_Type()
)
vrtpBdcstOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpBdcstOut.setStatus("optional")
_VrtpRtCr_Type = Counter32
_VrtpRtCr_Object = MibScalar
vrtpRtCr = _VrtpRtCr_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 40),
    _VrtpRtCr_Type()
)
vrtpRtCr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtCr.setStatus("optional")
_VrtpRtMod_Type = Counter32
_VrtpRtMod_Object = MibScalar
vrtpRtMod = _VrtpRtMod_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 41),
    _VrtpRtMod_Type()
)
vrtpRtMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpRtMod.setStatus("optional")
_VrtpNbrAnchors_Type = Counter32
_VrtpNbrAnchors_Object = MibScalar
vrtpNbrAnchors = _VrtpNbrAnchors_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 42),
    _VrtpNbrAnchors_Type()
)
vrtpNbrAnchors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrAnchors.setStatus("optional")
_VrtpNbrEntries_Type = Counter32
_VrtpNbrEntries_Object = MibScalar
vrtpNbrEntries = _VrtpNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 43),
    _VrtpNbrEntries_Type()
)
vrtpNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNbrEntries.setStatus("optional")
_VrtpNetEntries_Type = Counter32
_VrtpNetEntries_Object = MibScalar
vrtpNetEntries = _VrtpNetEntries_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 44),
    _VrtpNetEntries_Type()
)
vrtpNetEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNetEntries.setStatus("optional")
_VrtpLkUp_Type = Counter32
_VrtpLkUp_Object = MibScalar
vrtpLkUp = _VrtpLkUp_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 45),
    _VrtpLkUp_Type()
)
vrtpLkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpLkUp.setStatus("optional")
_VrtpBadLkUp_Type = Counter32
_VrtpBadLkUp_Object = MibScalar
vrtpBadLkUp = _VrtpBadLkUp_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 46),
    _VrtpBadLkUp_Type()
)
vrtpBadLkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpBadLkUp.setStatus("optional")
_VrtpNonSeqTotIn_Type = Counter32
_VrtpNonSeqTotIn_Object = MibScalar
vrtpNonSeqTotIn = _VrtpNonSeqTotIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 47),
    _VrtpNonSeqTotIn_Type()
)
vrtpNonSeqTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqTotIn.setStatus("optional")
_VrtpNonSeqTotOut_Type = Counter32
_VrtpNonSeqTotOut_Object = MibScalar
vrtpNonSeqTotOut = _VrtpNonSeqTotOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 48),
    _VrtpNonSeqTotOut_Type()
)
vrtpNonSeqTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqTotOut.setStatus("optional")
_VrtpNonSeqErrsIn_Type = Counter32
_VrtpNonSeqErrsIn_Object = MibScalar
vrtpNonSeqErrsIn = _VrtpNonSeqErrsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 49),
    _VrtpNonSeqErrsIn_Type()
)
vrtpNonSeqErrsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqErrsIn.setStatus("optional")
_VrtpNonSeqUpdIn_Type = Counter32
_VrtpNonSeqUpdIn_Object = MibScalar
vrtpNonSeqUpdIn = _VrtpNonSeqUpdIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 50),
    _VrtpNonSeqUpdIn_Type()
)
vrtpNonSeqUpdIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqUpdIn.setStatus("optional")
_VrtpNonSeqRspIn_Type = Counter32
_VrtpNonSeqRspIn_Object = MibScalar
vrtpNonSeqRspIn = _VrtpNonSeqRspIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 51),
    _VrtpNonSeqRspIn_Type()
)
vrtpNonSeqRspIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqRspIn.setStatus("optional")
_VrtpNonSeqRqstIn_Type = Counter32
_VrtpNonSeqRqstIn_Object = MibScalar
vrtpNonSeqRqstIn = _VrtpNonSeqRqstIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 52),
    _VrtpNonSeqRqstIn_Type()
)
vrtpNonSeqRqstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqRqstIn.setStatus("optional")
_VrtpNonSeqRdrIn_Type = Counter32
_VrtpNonSeqRdrIn_Object = MibScalar
vrtpNonSeqRdrIn = _VrtpNonSeqRdrIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 53),
    _VrtpNonSeqRdrIn_Type()
)
vrtpNonSeqRdrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqRdrIn.setStatus("optional")
_VrtpBadNonSeqRdrIn_Type = Counter32
_VrtpBadNonSeqRdrIn_Object = MibScalar
vrtpBadNonSeqRdrIn = _VrtpBadNonSeqRdrIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 54),
    _VrtpBadNonSeqRdrIn_Type()
)
vrtpBadNonSeqRdrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpBadNonSeqRdrIn.setStatus("optional")
_VrtpNonSeqBdcstIn_Type = Counter32
_VrtpNonSeqBdcstIn_Object = MibScalar
vrtpNonSeqBdcstIn = _VrtpNonSeqBdcstIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 55),
    _VrtpNonSeqBdcstIn_Type()
)
vrtpNonSeqBdcstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqBdcstIn.setStatus("optional")
_VrtpNonSeqUpdOut_Type = Counter32
_VrtpNonSeqUpdOut_Object = MibScalar
vrtpNonSeqUpdOut = _VrtpNonSeqUpdOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 56),
    _VrtpNonSeqUpdOut_Type()
)
vrtpNonSeqUpdOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqUpdOut.setStatus("optional")
_VrtpNonSeqRspOut_Type = Counter32
_VrtpNonSeqRspOut_Object = MibScalar
vrtpNonSeqRspOut = _VrtpNonSeqRspOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 57),
    _VrtpNonSeqRspOut_Type()
)
vrtpNonSeqRspOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqRspOut.setStatus("optional")
_VrtpNonSeqRqstOut_Type = Counter32
_VrtpNonSeqRqstOut_Object = MibScalar
vrtpNonSeqRqstOut = _VrtpNonSeqRqstOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 58),
    _VrtpNonSeqRqstOut_Type()
)
vrtpNonSeqRqstOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqRqstOut.setStatus("optional")
_VrtpNonSeqRdrOut_Type = Counter32
_VrtpNonSeqRdrOut_Object = MibScalar
vrtpNonSeqRdrOut = _VrtpNonSeqRdrOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 59),
    _VrtpNonSeqRdrOut_Type()
)
vrtpNonSeqRdrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqRdrOut.setStatus("optional")
_VrtpNonSeqBdcstOut_Type = Counter32
_VrtpNonSeqBdcstOut_Object = MibScalar
vrtpNonSeqBdcstOut = _VrtpNonSeqBdcstOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 60),
    _VrtpNonSeqBdcstOut_Type()
)
vrtpNonSeqBdcstOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpNonSeqBdcstOut.setStatus("optional")
_VrtpResponsesOut_Type = Counter32
_VrtpResponsesOut_Object = MibScalar
vrtpResponsesOut = _VrtpResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 7, 61),
    _VrtpResponsesOut_Type()
)
vrtpResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtpResponsesOut.setStatus("optional")
_Vspp_ObjectIdentity = ObjectIdentity
vspp = _Vspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8)
)
_VsppConnsInUse_Type = Integer32
_VsppConnsInUse_Object = MibScalar
vsppConnsInUse = _VsppConnsInUse_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 1),
    _VsppConnsInUse_Type()
)
vsppConnsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppConnsInUse.setStatus("mandatory")
_VsppConnsCfg_Type = Integer32
_VsppConnsCfg_Object = MibScalar
vsppConnsCfg = _VsppConnsCfg_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 2),
    _VsppConnsCfg_Type()
)
vsppConnsCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsppConnsCfg.setStatus("mandatory")
_VsppMaxConns_Type = Integer32
_VsppMaxConns_Object = MibScalar
vsppMaxConns = _VsppMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 3),
    _VsppMaxConns_Type()
)
vsppMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppMaxConns.setStatus("mandatory")
_VsppTotIn_Type = Counter32
_VsppTotIn_Object = MibScalar
vsppTotIn = _VsppTotIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 4),
    _VsppTotIn_Type()
)
vsppTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppTotIn.setStatus("mandatory")
_VsppTotOut_Type = Counter32
_VsppTotOut_Object = MibScalar
vsppTotOut = _VsppTotOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 5),
    _VsppTotOut_Type()
)
vsppTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppTotOut.setStatus("mandatory")
_VsppInErrs_Type = Counter32
_VsppInErrs_Object = MibScalar
vsppInErrs = _VsppInErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 6),
    _VsppInErrs_Type()
)
vsppInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppInErrs.setStatus("optional")
_VsppBadType_Type = Counter32
_VsppBadType_Object = MibScalar
vsppBadType = _VsppBadType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 7),
    _VsppBadType_Type()
)
vsppBadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppBadType.setStatus("optional")
_VsppNoBuffers_Type = Counter32
_VsppNoBuffers_Object = MibScalar
vsppNoBuffers = _VsppNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 8),
    _VsppNoBuffers_Type()
)
vsppNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppNoBuffers.setStatus("optional")
_VsppNoPort_Type = Counter32
_VsppNoPort_Object = MibScalar
vsppNoPort = _VsppNoPort_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 9),
    _VsppNoPort_Type()
)
vsppNoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppNoPort.setStatus("optional")
_VsppDups_Type = Counter32
_VsppDups_Object = MibScalar
vsppDups = _VsppDups_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 10),
    _VsppDups_Type()
)
vsppDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppDups.setStatus("optional")
_VsppBadOrder_Type = Counter32
_VsppBadOrder_Object = MibScalar
vsppBadOrder = _VsppBadOrder_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 11),
    _VsppBadOrder_Type()
)
vsppBadOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppBadOrder.setStatus("optional")
_VsppDataIn_Type = Counter32
_VsppDataIn_Object = MibScalar
vsppDataIn = _VsppDataIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 12),
    _VsppDataIn_Type()
)
vsppDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppDataIn.setStatus("optional")
_VsppAcksIn_Type = Counter32
_VsppAcksIn_Object = MibScalar
vsppAcksIn = _VsppAcksIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 13),
    _VsppAcksIn_Type()
)
vsppAcksIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppAcksIn.setStatus("optional")
_VsppDiscIn_Type = Counter32
_VsppDiscIn_Object = MibScalar
vsppDiscIn = _VsppDiscIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 14),
    _VsppDiscIn_Type()
)
vsppDiscIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppDiscIn.setStatus("optional")
_VsppProbesIn_Type = Counter32
_VsppProbesIn_Object = MibScalar
vsppProbesIn = _VsppProbesIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 15),
    _VsppProbesIn_Type()
)
vsppProbesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppProbesIn.setStatus("optional")
_VsppDataOut_Type = Counter32
_VsppDataOut_Object = MibScalar
vsppDataOut = _VsppDataOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 16),
    _VsppDataOut_Type()
)
vsppDataOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppDataOut.setStatus("optional")
_VsppAcksOut_Type = Counter32
_VsppAcksOut_Object = MibScalar
vsppAcksOut = _VsppAcksOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 17),
    _VsppAcksOut_Type()
)
vsppAcksOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppAcksOut.setStatus("optional")
_VsppDiscOut_Type = Counter32
_VsppDiscOut_Object = MibScalar
vsppDiscOut = _VsppDiscOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 18),
    _VsppDiscOut_Type()
)
vsppDiscOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppDiscOut.setStatus("optional")
_VsppProbesOut_Type = Counter32
_VsppProbesOut_Object = MibScalar
vsppProbesOut = _VsppProbesOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 19),
    _VsppProbesOut_Type()
)
vsppProbesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppProbesOut.setStatus("optional")
_VsppAbortsOut_Type = Counter32
_VsppAbortsOut_Object = MibScalar
vsppAbortsOut = _VsppAbortsOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 20),
    _VsppAbortsOut_Type()
)
vsppAbortsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppAbortsOut.setStatus("optional")
_VsppLocal_Type = Counter32
_VsppLocal_Object = MibScalar
vsppLocal = _VsppLocal_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 8, 21),
    _VsppLocal_Type()
)
vsppLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsppLocal.setStatus("optional")
_Vinterfaces_ObjectIdentity = ObjectIdentity
vinterfaces = _Vinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9)
)
_VifNumber_Type = Integer32
_VifNumber_Object = MibScalar
vifNumber = _VifNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 1),
    _VifNumber_Type()
)
vifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifNumber.setStatus("mandatory")
_VifTable_Object = MibTable
vifTable = _VifTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    vifTable.setStatus("mandatory")
_VifEntry_Object = MibTableRow
vifEntry = _VifEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1)
)
vifEntry.setIndexNames(
    (0, "VINES-MIB", "vifSlot"),
)
if mibBuilder.loadTexts:
    vifEntry.setStatus("mandatory")
_VifSlot_Type = Integer32
_VifSlot_Object = MibTableColumn
vifSlot = _VifSlot_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 1),
    _VifSlot_Type()
)
vifSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifSlot.setStatus("mandatory")


class _VifType_Type(Integer32):
    """Custom type vifType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              99,
              100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 73),
          ("arcnetNDIS", 70),
          ("arcnetSMC", 6),
          ("arcnetSMCMC", 39),
          ("blkAsync", 12),
          ("ctrlerDATACO", 49),
          ("ctrllerGanges", 22),
          ("etherExpressIntel", 81),
          ("etherLink3COM16", 75),
          ("ethernet3Com", 1),
          ("ethernet3Com3C503", 31),
          ("ethernet3Com3C523", 32),
          ("ethernetBICC", 58),
          ("ethernetBICCMC", 78),
          ("ethernetCabletron", 68),
          ("ethernetDGCODE", 90),
          ("ethernetEplus3Com", 20),
          ("ethernetIBMMC", 54),
          ("ethernetICAMC", 42),
          ("ethernetIntelPC586E", 36),
          ("ethernetNDIS", 51),
          ("ethernetNI5010", 2),
          ("ethernetNI5210", 23),
          ("ethernetNI9210MC", 41),
          ("ethernetNT2R15", 59),
          ("ethernetNTMC", 60),
          ("ethernetNTTurbo", 61),
          ("ethernetNovellNE", 48),
          ("ethernetNovellNE3200", 65),
          ("ethernetPureData", 66),
          ("ethernetPureDataMC", 67),
          ("ethernetUB", 4),
          ("ethernetWDigital", 28),
          ("ethernetWDigitalMC", 56),
          ("frag", 9),
          ("ftp", 69),
          ("gatewayAPI", 52),
          ("hdlc", 11),
          ("hdlcTCPIP", 26),
          ("hughes", 50),
          ("icaPlus", 79),
          ("interlanEISA", 57),
          ("interlanNI6510", 76),
          ("intersys", 13),
          ("ipBanyan", 25),
          ("ipNSRouting", 80),
          ("ipTCPIP", 24),
          ("ipaDavidSys", 18),
          ("isdnBRIDatavoice", 91),
          ("isdnDchannel", 103),
          ("isoSvrSvr", 64),
          ("lanLinkNT", 21),
          ("lanLinkNTMC", 34),
          ("lapdT1", 102),
          ("llTurboNT", 46),
          ("localTalk", 74),
          ("omninetCorvus", 5),
          ("pcnetSytek", 7),
          ("proNetProteon", 8),
          ("promptusE1", 101),
          ("promptusT1", 100),
          ("pronetProteonMC", 38),
          ("prsystctrl", 10),
          ("ps2UBNICMC", 45),
          ("pseudoIBM", 43),
          ("serialVGsystems", 35),
          ("starlanATT", 29),
          ("starlanATT10", 37),
          ("starlanATT10MC", 44),
          ("starlanATTEISA", 72),
          ("starlanNI5210", 30),
          ("starlanWDigital", 27),
          ("tokenExpressIntelEISA", 87),
          ("tokenExpressIntelISA", 85),
          ("tokenExpressIntelMC", 86),
          ("tokenRing3Com3C603", 33),
          ("tokenRingCompaq", 63),
          ("tokenRingIBM", 15),
          ("tokenRingIBMBM", 55),
          ("tokenRingIBMMC", 40),
          ("tokenRingIrmaTracMCA", 89),
          ("tokenRingIrmaTracPCAT", 88),
          ("tokenRingMadge", 53),
          ("tokenRingNDIS", 71),
          ("tokenRingOlicamEISA", 84),
          ("tokenRingOlicom", 82),
          ("tokenRingOlicomMC", 83),
          ("tokenRingPronet", 62),
          ("tokenRingPronet4", 19),
          ("tokenRingProteon", 47),
          ("tokenRingProteonP1890", 77),
          ("tokenRingUB", 17),
          ("unused", 99),
          ("wavelanNCR", 92),
          ("x25", 16),
          ("x25EICON", 14))
    )


_VifType_Type.__name__ = "Integer32"
_VifType_Object = MibTableColumn
vifType = _VifType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 2),
    _VifType_Type()
)
vifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifType.setStatus("mandatory")
_VifDescr_Type = OctetString
_VifDescr_Object = MibTableColumn
vifDescr = _VifDescr_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 3),
    _VifDescr_Type()
)
vifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifDescr.setStatus("mandatory")
_VifAddress_Type = OctetString
_VifAddress_Object = MibTableColumn
vifAddress = _VifAddress_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 4),
    _VifAddress_Type()
)
vifAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifAddress.setStatus("mandatory")
_VifInPkts_Type = Counter32
_VifInPkts_Object = MibTableColumn
vifInPkts = _VifInPkts_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 5),
    _VifInPkts_Type()
)
vifInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifInPkts.setStatus("mandatory")
_VifInErrs_Type = Counter32
_VifInErrs_Object = MibTableColumn
vifInErrs = _VifInErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 6),
    _VifInErrs_Type()
)
vifInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifInErrs.setStatus("mandatory")
_VifOutPkts_Type = Counter32
_VifOutPkts_Object = MibTableColumn
vifOutPkts = _VifOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 7),
    _VifOutPkts_Type()
)
vifOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifOutPkts.setStatus("mandatory")
_VifOutErrs_Type = Counter32
_VifOutErrs_Object = MibTableColumn
vifOutErrs = _VifOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 2, 1, 8),
    _VifOutErrs_Type()
)
vifOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifOutErrs.setStatus("mandatory")
_VifLnkNumber_Type = Integer32
_VifLnkNumber_Object = MibScalar
vifLnkNumber = _VifLnkNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 3),
    _VifLnkNumber_Type()
)
vifLnkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkNumber.setStatus("mandatory")
_VifLnkTable_Object = MibTable
vifLnkTable = _VifLnkTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4)
)
if mibBuilder.loadTexts:
    vifLnkTable.setStatus("mandatory")
_VifLnkEntry_Object = MibTableRow
vifLnkEntry = _VifLnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1)
)
vifLnkEntry.setIndexNames(
    (0, "VINES-MIB", "vifLnkSlot"),
    (0, "VINES-MIB", "vifLnkLine"),
)
if mibBuilder.loadTexts:
    vifLnkEntry.setStatus("mandatory")
_VifLnkSlot_Type = Integer32
_VifLnkSlot_Object = MibTableColumn
vifLnkSlot = _VifLnkSlot_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 1),
    _VifLnkSlot_Type()
)
vifLnkSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkSlot.setStatus("mandatory")
_VifLnkLine_Type = Integer32
_VifLnkLine_Object = MibTableColumn
vifLnkLine = _VifLnkLine_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 2),
    _VifLnkLine_Type()
)
vifLnkLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkLine.setStatus("mandatory")


class _VifLnkType_Type(Integer32):
    """Custom type vifLnkType based on Integer32"""
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
        *(("ate", 1),
          ("blkasynch", 7),
          ("bsc3270", 11),
          ("hdlc", 8),
          ("sdlcv1", 10),
          ("sdlcv2", 12),
          ("unused2", 2),
          ("unused3", 3),
          ("unused4", 4),
          ("unused5", 5),
          ("unused6", 6),
          ("x25", 9))
    )


_VifLnkType_Type.__name__ = "Integer32"
_VifLnkType_Object = MibTableColumn
vifLnkType = _VifLnkType_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 3),
    _VifLnkType_Type()
)
vifLnkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkType.setStatus("mandatory")
_VifLnkTotIn_Type = Counter32
_VifLnkTotIn_Object = MibTableColumn
vifLnkTotIn = _VifLnkTotIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 4),
    _VifLnkTotIn_Type()
)
vifLnkTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkTotIn.setStatus("mandatory")
_VifLnkTotOut_Type = Counter32
_VifLnkTotOut_Object = MibTableColumn
vifLnkTotOut = _VifLnkTotOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 5),
    _VifLnkTotOut_Type()
)
vifLnkTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkTotOut.setStatus("mandatory")
_VifLnkRetrans_Type = Counter32
_VifLnkRetrans_Object = MibTableColumn
vifLnkRetrans = _VifLnkRetrans_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 6),
    _VifLnkRetrans_Type()
)
vifLnkRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkRetrans.setStatus("mandatory")
_VifLnkCRCErrs_Type = Counter32
_VifLnkCRCErrs_Object = MibTableColumn
vifLnkCRCErrs = _VifLnkCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 7),
    _VifLnkCRCErrs_Type()
)
vifLnkCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkCRCErrs.setStatus("mandatory")
_VifLnkDrops_Type = Counter32
_VifLnkDrops_Object = MibTableColumn
vifLnkDrops = _VifLnkDrops_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 8),
    _VifLnkDrops_Type()
)
vifLnkDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkDrops.setStatus("mandatory")
_VifLnkUnders_Type = Counter32
_VifLnkUnders_Object = MibTableColumn
vifLnkUnders = _VifLnkUnders_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 9),
    _VifLnkUnders_Type()
)
vifLnkUnders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkUnders.setStatus("mandatory")
_VifLnkOvers_Type = Counter32
_VifLnkOvers_Object = MibTableColumn
vifLnkOvers = _VifLnkOvers_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 10),
    _VifLnkOvers_Type()
)
vifLnkOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkOvers.setStatus("mandatory")
_VifLnkFrmErrs_Type = Counter32
_VifLnkFrmErrs_Object = MibTableColumn
vifLnkFrmErrs = _VifLnkFrmErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 4, 1, 11),
    _VifLnkFrmErrs_Type()
)
vifLnkFrmErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifLnkFrmErrs.setStatus("mandatory")
_VifX25VCNumber_Type = Integer32
_VifX25VCNumber_Object = MibScalar
vifX25VCNumber = _VifX25VCNumber_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 5),
    _VifX25VCNumber_Type()
)
vifX25VCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCNumber.setStatus("mandatory")
_VifX25VCTable_Object = MibTable
vifX25VCTable = _VifX25VCTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6)
)
if mibBuilder.loadTexts:
    vifX25VCTable.setStatus("mandatory")
_VifX25VCEntry_Object = MibTableRow
vifX25VCEntry = _VifX25VCEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1)
)
vifX25VCEntry.setIndexNames(
    (0, "VINES-MIB", "vifX25VCSlot"),
    (0, "VINES-MIB", "vifX25VCLine"),
    (0, "VINES-MIB", "vifX25VCSession"),
)
if mibBuilder.loadTexts:
    vifX25VCEntry.setStatus("mandatory")
_VifX25VCSlot_Type = Integer32
_VifX25VCSlot_Object = MibTableColumn
vifX25VCSlot = _VifX25VCSlot_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 1),
    _VifX25VCSlot_Type()
)
vifX25VCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCSlot.setStatus("mandatory")
_VifX25VCLine_Type = Integer32
_VifX25VCLine_Object = MibTableColumn
vifX25VCLine = _VifX25VCLine_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 2),
    _VifX25VCLine_Type()
)
vifX25VCLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCLine.setStatus("mandatory")
_VifX25VCSession_Type = Integer32
_VifX25VCSession_Object = MibTableColumn
vifX25VCSession = _VifX25VCSession_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 3),
    _VifX25VCSession_Type()
)
vifX25VCSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCSession.setStatus("mandatory")
_VifX25VCTotIn_Type = Counter32
_VifX25VCTotIn_Object = MibTableColumn
vifX25VCTotIn = _VifX25VCTotIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 4),
    _VifX25VCTotIn_Type()
)
vifX25VCTotIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCTotIn.setStatus("mandatory")
_VifX25VCTotOut_Type = Counter32
_VifX25VCTotOut_Object = MibTableColumn
vifX25VCTotOut = _VifX25VCTotOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 5),
    _VifX25VCTotOut_Type()
)
vifX25VCTotOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCTotOut.setStatus("mandatory")
_VifX25VCInErrs_Type = Counter32
_VifX25VCInErrs_Object = MibTableColumn
vifX25VCInErrs = _VifX25VCInErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 6),
    _VifX25VCInErrs_Type()
)
vifX25VCInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCInErrs.setStatus("mandatory")
_VifX25VCOutErrs_Type = Counter32
_VifX25VCOutErrs_Object = MibTableColumn
vifX25VCOutErrs = _VifX25VCOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 7),
    _VifX25VCOutErrs_Type()
)
vifX25VCOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCOutErrs.setStatus("mandatory")
_VifX25VCPktsOut_Type = Counter32
_VifX25VCPktsOut_Object = MibTableColumn
vifX25VCPktsOut = _VifX25VCPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 8),
    _VifX25VCPktsOut_Type()
)
vifX25VCPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCPktsOut.setStatus("mandatory")
_VifX25VCPktsAwaitAck_Type = Integer32
_VifX25VCPktsAwaitAck_Object = MibTableColumn
vifX25VCPktsAwaitAck = _VifX25VCPktsAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 9),
    _VifX25VCPktsAwaitAck_Type()
)
vifX25VCPktsAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCPktsAwaitAck.setStatus("mandatory")
_VifX25VCBytesOut_Type = Counter32
_VifX25VCBytesOut_Object = MibTableColumn
vifX25VCBytesOut = _VifX25VCBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 10),
    _VifX25VCBytesOut_Type()
)
vifX25VCBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCBytesOut.setStatus("mandatory")
_VifX25VCBytesAwaitAck_Type = Integer32
_VifX25VCBytesAwaitAck_Object = MibTableColumn
vifX25VCBytesAwaitAck = _VifX25VCBytesAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 11),
    _VifX25VCBytesAwaitAck_Type()
)
vifX25VCBytesAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCBytesAwaitAck.setStatus("mandatory")
_VifX25VCPktsIn_Type = Counter32
_VifX25VCPktsIn_Object = MibTableColumn
vifX25VCPktsIn = _VifX25VCPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 12),
    _VifX25VCPktsIn_Type()
)
vifX25VCPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCPktsIn.setStatus("mandatory")
_VifX25VCBytesIn_Type = Counter32
_VifX25VCBytesIn_Object = MibTableColumn
vifX25VCBytesIn = _VifX25VCBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 13),
    _VifX25VCBytesIn_Type()
)
vifX25VCBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCBytesIn.setStatus("mandatory")
_VifX25VCResetsIn_Type = Counter32
_VifX25VCResetsIn_Object = MibTableColumn
vifX25VCResetsIn = _VifX25VCResetsIn_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 14),
    _VifX25VCResetsIn_Type()
)
vifX25VCResetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCResetsIn.setStatus("mandatory")
_VifX25VCResetsOut_Type = Counter32
_VifX25VCResetsOut_Object = MibTableColumn
vifX25VCResetsOut = _VifX25VCResetsOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 15),
    _VifX25VCResetsOut_Type()
)
vifX25VCResetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCResetsOut.setStatus("mandatory")
_VifX25VCLogChnNum_Type = Integer32
_VifX25VCLogChnNum_Object = MibTableColumn
vifX25VCLogChnNum = _VifX25VCLogChnNum_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 16),
    _VifX25VCLogChnNum_Type()
)
vifX25VCLogChnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCLogChnNum.setStatus("mandatory")
_VifX25VCRemAddr_Type = OctetString
_VifX25VCRemAddr_Object = MibTableColumn
vifX25VCRemAddr = _VifX25VCRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 6, 1, 17),
    _VifX25VCRemAddr_Type()
)
vifX25VCRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifX25VCRemAddr.setStatus("mandatory")
_VifStatsList_Object = MibTable
vifStatsList = _VifStatsList_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 7)
)
if mibBuilder.loadTexts:
    vifStatsList.setStatus("mandatory")
_VifStatEntry_Object = MibTableRow
vifStatEntry = _VifStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 7, 1)
)
vifStatEntry.setIndexNames(
    (0, "VINES-MIB", "vifStatSlot"),
    (0, "VINES-MIB", "vifStatIndex"),
)
if mibBuilder.loadTexts:
    vifStatEntry.setStatus("mandatory")
_VifStatSlot_Type = Integer32
_VifStatSlot_Object = MibTableColumn
vifStatSlot = _VifStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 7, 1, 1),
    _VifStatSlot_Type()
)
vifStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifStatSlot.setStatus("mandatory")
_VifStatIndex_Type = Integer32
_VifStatIndex_Object = MibTableColumn
vifStatIndex = _VifStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 7, 1, 2),
    _VifStatIndex_Type()
)
vifStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifStatIndex.setStatus("mandatory")
_VifStatDescr_Type = OctetString
_VifStatDescr_Object = MibTableColumn
vifStatDescr = _VifStatDescr_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 7, 1, 3),
    _VifStatDescr_Type()
)
vifStatDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifStatDescr.setStatus("mandatory")
_VifStatValue_Type = Integer32
_VifStatValue_Object = MibTableColumn
vifStatValue = _VifStatValue_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 9, 7, 1, 4),
    _VifStatValue_Type()
)
vifStatValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vifStatValue.setStatus("mandatory")
_Os_ObjectIdentity = ObjectIdentity
os = _Os_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10)
)
_Ossysstats_ObjectIdentity = ObjectIdentity
ossysstats = _Ossysstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1)
)
_OscpuNum_Type = Integer32
_OscpuNum_Object = MibScalar
oscpuNum = _OscpuNum_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 1),
    _OscpuNum_Type()
)
oscpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscpuNum.setStatus("mandatory")
_OscpuTable_Object = MibTable
oscpuTable = _OscpuTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    oscpuTable.setStatus("mandatory")
_OscpuEntry_Object = MibTableRow
oscpuEntry = _OscpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1)
)
oscpuEntry.setIndexNames(
    (0, "VINES-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    oscpuEntry.setStatus("mandatory")
_CpuIndex_Type = Integer32
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("mandatory")
_CpuIdleUsage_Type = TimeTicks
_CpuIdleUsage_Object = MibTableColumn
cpuIdleUsage = _CpuIdleUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 2),
    _CpuIdleUsage_Type()
)
cpuIdleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIdleUsage.setStatus("mandatory")
_CpuUserUsage_Type = TimeTicks
_CpuUserUsage_Object = MibTableColumn
cpuUserUsage = _CpuUserUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 3),
    _CpuUserUsage_Type()
)
cpuUserUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUserUsage.setStatus("mandatory")
_CpuSysUsage_Type = TimeTicks
_CpuSysUsage_Object = MibTableColumn
cpuSysUsage = _CpuSysUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 4),
    _CpuSysUsage_Type()
)
cpuSysUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuSysUsage.setStatus("mandatory")
_CpuWIOUserUsage_Type = TimeTicks
_CpuWIOUserUsage_Object = MibTableColumn
cpuWIOUserUsage = _CpuWIOUserUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 5),
    _CpuWIOUserUsage_Type()
)
cpuWIOUserUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWIOUserUsage.setStatus("mandatory")
_CpuProcSwappedOut_Type = TimeTicks
_CpuProcSwappedOut_Object = MibTableColumn
cpuProcSwappedOut = _CpuProcSwappedOut_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 6),
    _CpuProcSwappedOut_Type()
)
cpuProcSwappedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuProcSwappedOut.setStatus("mandatory")
_CpuWIOUsage_Type = TimeTicks
_CpuWIOUsage_Object = MibTableColumn
cpuWIOUsage = _CpuWIOUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 7),
    _CpuWIOUsage_Type()
)
cpuWIOUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWIOUsage.setStatus("mandatory")
_CpuWSUsage_Type = TimeTicks
_CpuWSUsage_Object = MibTableColumn
cpuWSUsage = _CpuWSUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 8),
    _CpuWSUsage_Type()
)
cpuWSUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWSUsage.setStatus("mandatory")
_CpuWPIOUsage_Type = TimeTicks
_CpuWPIOUsage_Object = MibTableColumn
cpuWPIOUsage = _CpuWPIOUsage_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 2, 1, 9),
    _CpuWPIOUsage_Type()
)
cpuWPIOUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWPIOUsage.setStatus("mandatory")
_OsBReads_Type = Counter32
_OsBReads_Object = MibScalar
osBReads = _OsBReads_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 3),
    _OsBReads_Type()
)
osBReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osBReads.setStatus("mandatory")
_OsBWrites_Type = Counter32
_OsBWrites_Object = MibScalar
osBWrites = _OsBWrites_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 4),
    _OsBWrites_Type()
)
osBWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osBWrites.setStatus("mandatory")
_OsLReads_Type = Counter32
_OsLReads_Object = MibScalar
osLReads = _OsLReads_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 5),
    _OsLReads_Type()
)
osLReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLReads.setStatus("mandatory")
_OsLWrites_Type = Counter32
_OsLWrites_Object = MibScalar
osLWrites = _OsLWrites_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 6),
    _OsLWrites_Type()
)
osLWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osLWrites.setStatus("mandatory")
_OsPReads_Type = Counter32
_OsPReads_Object = MibScalar
osPReads = _OsPReads_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 7),
    _OsPReads_Type()
)
osPReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPReads.setStatus("mandatory")
_OsPWrites_Type = Counter32
_OsPWrites_Object = MibScalar
osPWrites = _OsPWrites_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 8),
    _OsPWrites_Type()
)
osPWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPWrites.setStatus("mandatory")
_OsInSwaps_Type = Counter32
_OsInSwaps_Object = MibScalar
osInSwaps = _OsInSwaps_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 9),
    _OsInSwaps_Type()
)
osInSwaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osInSwaps.setStatus("mandatory")
_OsOutSwaps_Type = Counter32
_OsOutSwaps_Object = MibScalar
osOutSwaps = _OsOutSwaps_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 10),
    _OsOutSwaps_Type()
)
osOutSwaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOutSwaps.setStatus("mandatory")
_OsInBSwaps_Type = Counter32
_OsInBSwaps_Object = MibScalar
osInBSwaps = _OsInBSwaps_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 11),
    _OsInBSwaps_Type()
)
osInBSwaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osInBSwaps.setStatus("mandatory")
_OsOutBSwaps_Type = Counter32
_OsOutBSwaps_Object = MibScalar
osOutBSwaps = _OsOutBSwaps_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 12),
    _OsOutBSwaps_Type()
)
osOutBSwaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osOutBSwaps.setStatus("mandatory")
_OsProcessSwitches_Type = Counter32
_OsProcessSwitches_Object = MibScalar
osProcessSwitches = _OsProcessSwitches_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 13),
    _OsProcessSwitches_Type()
)
osProcessSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osProcessSwitches.setStatus("mandatory")
_OsSystemCalls_Type = Counter32
_OsSystemCalls_Object = MibScalar
osSystemCalls = _OsSystemCalls_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 14),
    _OsSystemCalls_Type()
)
osSystemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSystemCalls.setStatus("mandatory")
_OsSystemRead_Type = Counter32
_OsSystemRead_Object = MibScalar
osSystemRead = _OsSystemRead_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 15),
    _OsSystemRead_Type()
)
osSystemRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSystemRead.setStatus("mandatory")
_OsSystemWrite_Type = Counter32
_OsSystemWrite_Object = MibScalar
osSystemWrite = _OsSystemWrite_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 16),
    _OsSystemWrite_Type()
)
osSystemWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSystemWrite.setStatus("mandatory")
_OsSystemFork_Type = Counter32
_OsSystemFork_Object = MibScalar
osSystemFork = _OsSystemFork_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 17),
    _OsSystemFork_Type()
)
osSystemFork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSystemFork.setStatus("mandatory")
_OsSystemExec_Type = Counter32
_OsSystemExec_Object = MibScalar
osSystemExec = _OsSystemExec_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 18),
    _OsSystemExec_Type()
)
osSystemExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSystemExec.setStatus("mandatory")
_OsRunQueue_Type = Counter32
_OsRunQueue_Object = MibScalar
osRunQueue = _OsRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 19),
    _OsRunQueue_Type()
)
osRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osRunQueue.setStatus("mandatory")
_OsRunQueueOcc_Type = TimeTicks
_OsRunQueueOcc_Object = MibScalar
osRunQueueOcc = _OsRunQueueOcc_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 20),
    _OsRunQueueOcc_Type()
)
osRunQueueOcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osRunQueueOcc.setStatus("mandatory")
_OsSwapQueueTotals_Type = Counter32
_OsSwapQueueTotals_Object = MibScalar
osSwapQueueTotals = _OsSwapQueueTotals_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 21),
    _OsSwapQueueTotals_Type()
)
osSwapQueueTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSwapQueueTotals.setStatus("mandatory")
_OsSwapQueueOcc_Type = TimeTicks
_OsSwapQueueOcc_Object = MibScalar
osSwapQueueOcc = _OsSwapQueueOcc_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 22),
    _OsSwapQueueOcc_Type()
)
osSwapQueueOcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSwapQueueOcc.setStatus("mandatory")
_OsIPCMsgOps_Type = Counter32
_OsIPCMsgOps_Object = MibScalar
osIPCMsgOps = _OsIPCMsgOps_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 23),
    _OsIPCMsgOps_Type()
)
osIPCMsgOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osIPCMsgOps.setStatus("mandatory")
_OsSemOps_Type = Counter32
_OsSemOps_Object = MibScalar
osSemOps = _OsSemOps_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 24),
    _OsSemOps_Type()
)
osSemOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSemOps.setStatus("mandatory")
_OsPnpFault_Type = Counter32
_OsPnpFault_Object = MibScalar
osPnpFault = _OsPnpFault_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 25),
    _OsPnpFault_Type()
)
osPnpFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPnpFault.setStatus("mandatory")
_OsWrtFault_Type = Counter32
_OsWrtFault_Object = MibScalar
osWrtFault = _OsWrtFault_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 26),
    _OsWrtFault_Type()
)
osWrtFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWrtFault.setStatus("mandatory")
_OsCurrentInodes_Type = Integer32
_OsCurrentInodes_Object = MibScalar
osCurrentInodes = _OsCurrentInodes_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 27),
    _OsCurrentInodes_Type()
)
osCurrentInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCurrentInodes.setStatus("mandatory")
_OsHWInodes_Type = Integer32
_OsHWInodes_Object = MibScalar
osHWInodes = _OsHWInodes_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 28),
    _OsHWInodes_Type()
)
osHWInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osHWInodes.setStatus("mandatory")
_OsCurrentFiles_Type = Integer32
_OsCurrentFiles_Object = MibScalar
osCurrentFiles = _OsCurrentFiles_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 29),
    _OsCurrentFiles_Type()
)
osCurrentFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCurrentFiles.setStatus("mandatory")
_OsHWFiles_Type = Integer32
_OsHWFiles_Object = MibScalar
osHWFiles = _OsHWFiles_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 1, 30),
    _OsHWFiles_Type()
)
osHWFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osHWFiles.setStatus("mandatory")
_Osinfo_ObjectIdentity = ObjectIdentity
osinfo = _Osinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2)
)
_OsMaxInodes_Type = Integer32
_OsMaxInodes_Object = MibScalar
osMaxInodes = _OsMaxInodes_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 1),
    _OsMaxInodes_Type()
)
osMaxInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osMaxInodes.setStatus("mandatory")
_OsMaxFiles_Type = Integer32
_OsMaxFiles_Object = MibScalar
osMaxFiles = _OsMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 2),
    _OsMaxFiles_Type()
)
osMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osMaxFiles.setStatus("mandatory")
_OsMaxProcesses_Type = Integer32
_OsMaxProcesses_Object = MibScalar
osMaxProcesses = _OsMaxProcesses_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 3),
    _OsMaxProcesses_Type()
)
osMaxProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osMaxProcesses.setStatus("mandatory")
_OsSwapSpaceAvailable_Type = Integer32
_OsSwapSpaceAvailable_Object = MibScalar
osSwapSpaceAvailable = _OsSwapSpaceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 4),
    _OsSwapSpaceAvailable_Type()
)
osSwapSpaceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSwapSpaceAvailable.setStatus("mandatory")
_OsFreeMemoryTotal_Type = Integer32
_OsFreeMemoryTotal_Object = MibScalar
osFreeMemoryTotal = _OsFreeMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 5),
    _OsFreeMemoryTotal_Type()
)
osFreeMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osFreeMemoryTotal.setStatus("mandatory")
_OsIOBufs_Type = Integer32
_OsIOBufs_Object = MibScalar
osIOBufs = _OsIOBufs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 6),
    _OsIOBufs_Type()
)
osIOBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osIOBufs.setStatus("mandatory")
_OsMounts_Type = Integer32
_OsMounts_Object = MibScalar
osMounts = _OsMounts_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 7),
    _OsMounts_Type()
)
osMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osMounts.setStatus("mandatory")
_OsUserMaxPu_Type = Integer32
_OsUserMaxPu_Object = MibScalar
osUserMaxPu = _OsUserMaxPu_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 8),
    _OsUserMaxPu_Type()
)
osUserMaxPu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osUserMaxPu.setStatus("mandatory")
_OsUserMaxFp_Type = Integer32
_OsUserMaxFp_Object = MibScalar
osUserMaxFp = _OsUserMaxFp_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 2, 9),
    _OsUserMaxFp_Type()
)
osUserMaxFp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osUserMaxFp.setStatus("mandatory")
_Ossummstats_ObjectIdentity = ObjectIdentity
ossummstats = _Ossummstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3)
)
_OsCurrentProcesses_Type = Integer32
_OsCurrentProcesses_Object = MibScalar
osCurrentProcesses = _OsCurrentProcesses_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 1),
    _OsCurrentProcesses_Type()
)
osCurrentProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCurrentProcesses.setStatus("mandatory")
_OsSwapSpaceUsed_Type = Integer32
_OsSwapSpaceUsed_Object = MibScalar
osSwapSpaceUsed = _OsSwapSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 2),
    _OsSwapSpaceUsed_Type()
)
osSwapSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSwapSpaceUsed.setStatus("mandatory")
_OsFreeMemoryAvailable_Type = Integer32
_OsFreeMemoryAvailable_Object = MibScalar
osFreeMemoryAvailable = _OsFreeMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 3),
    _OsFreeMemoryAvailable_Type()
)
osFreeMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osFreeMemoryAvailable.setStatus("mandatory")
_OsUserUsagePct_Type = Integer32
_OsUserUsagePct_Object = MibScalar
osUserUsagePct = _OsUserUsagePct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 4),
    _OsUserUsagePct_Type()
)
osUserUsagePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osUserUsagePct.setStatus("optional")
_OsSysUsagePct_Type = Integer32
_OsSysUsagePct_Object = MibScalar
osSysUsagePct = _OsSysUsagePct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 5),
    _OsSysUsagePct_Type()
)
osSysUsagePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSysUsagePct.setStatus("mandatory")
_OsWIOUsagePct_Type = Integer32
_OsWIOUsagePct_Object = MibScalar
osWIOUsagePct = _OsWIOUsagePct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 6),
    _OsWIOUsagePct_Type()
)
osWIOUsagePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWIOUsagePct.setStatus("mandatory")
_OsIdleUsagePct_Type = Integer32
_OsIdleUsagePct_Object = MibScalar
osIdleUsagePct = _OsIdleUsagePct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 7),
    _OsIdleUsagePct_Type()
)
osIdleUsagePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osIdleUsagePct.setStatus("mandatory")
_OsRunOccPct_Type = Integer32
_OsRunOccPct_Object = MibScalar
osRunOccPct = _OsRunOccPct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 8),
    _OsRunOccPct_Type()
)
osRunOccPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osRunOccPct.setStatus("mandatory")
_OsSwapOccPct_Type = Integer32
_OsSwapOccPct_Object = MibScalar
osSwapOccPct = _OsSwapOccPct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 9),
    _OsSwapOccPct_Type()
)
osSwapOccPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSwapOccPct.setStatus("mandatory")
_OsBuffRdRate_Type = Integer32
_OsBuffRdRate_Object = MibScalar
osBuffRdRate = _OsBuffRdRate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 10),
    _OsBuffRdRate_Type()
)
osBuffRdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osBuffRdRate.setStatus("mandatory")
_OsRdCachePct_Type = Integer32
_OsRdCachePct_Object = MibScalar
osRdCachePct = _OsRdCachePct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 11),
    _OsRdCachePct_Type()
)
osRdCachePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osRdCachePct.setStatus("mandatory")
_OsBuffWrRate_Type = Integer32
_OsBuffWrRate_Object = MibScalar
osBuffWrRate = _OsBuffWrRate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 12),
    _OsBuffWrRate_Type()
)
osBuffWrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osBuffWrRate.setStatus("mandatory")
_OsWrCachePct_Type = Integer32
_OsWrCachePct_Object = MibScalar
osWrCachePct = _OsWrCachePct_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 13),
    _OsWrCachePct_Type()
)
osWrCachePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osWrCachePct.setStatus("mandatory")
_OsBswpInRate_Type = Integer32
_OsBswpInRate_Object = MibScalar
osBswpInRate = _OsBswpInRate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 14),
    _OsBswpInRate_Type()
)
osBswpInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osBswpInRate.setStatus("mandatory")
_OsBswpOutRate_Type = Integer32
_OsBswpOutRate_Object = MibScalar
osBswpOutRate = _OsBswpOutRate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 15),
    _OsBswpOutRate_Type()
)
osBswpOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osBswpOutRate.setStatus("mandatory")
_OsVfltRate_Type = Integer32
_OsVfltRate_Object = MibScalar
osVfltRate = _OsVfltRate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 16),
    _OsVfltRate_Type()
)
osVfltRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osVfltRate.setStatus("mandatory")
_OsSwitchRate_Type = Integer32
_OsSwitchRate_Object = MibScalar
osSwitchRate = _OsSwitchRate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 17),
    _OsSwitchRate_Type()
)
osSwitchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSwitchRate.setStatus("mandatory")
_OsSysCallRate_Type = Integer32
_OsSysCallRate_Object = MibScalar
osSysCallRate = _OsSysCallRate_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 10, 3, 18),
    _OsSysCallRate_Type()
)
osSysCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSysCallRate.setStatus("mandatory")
_Nmthresholds_ObjectIdentity = ObjectIdentity
nmthresholds = _Nmthresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11)
)
_NmLoadAvg15HighThres_Type = Integer32
_NmLoadAvg15HighThres_Object = MibScalar
nmLoadAvg15HighThres = _NmLoadAvg15HighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 1),
    _NmLoadAvg15HighThres_Type()
)
nmLoadAvg15HighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmLoadAvg15HighThres.setStatus("mandatory")
_NmSockInUseHighThres_Type = Integer32
_NmSockInUseHighThres_Object = MibScalar
nmSockInUseHighThres = _NmSockInUseHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 2),
    _NmSockInUseHighThres_Type()
)
nmSockInUseHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmSockInUseHighThres.setStatus("mandatory")
_NmDiskUseHighThres_Type = Integer32
_NmDiskUseHighThres_Object = MibScalar
nmDiskUseHighThres = _NmDiskUseHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 3),
    _NmDiskUseHighThres_Type()
)
nmDiskUseHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmDiskUseHighThres.setStatus("mandatory")
_NmSwapAvgHighThres_Type = Integer32
_NmSwapAvgHighThres_Object = MibScalar
nmSwapAvgHighThres = _NmSwapAvgHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 4),
    _NmSwapAvgHighThres_Type()
)
nmSwapAvgHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmSwapAvgHighThres.setStatus("mandatory")
_NmDropsHighThres_Type = Integer32
_NmDropsHighThres_Object = MibScalar
nmDropsHighThres = _NmDropsHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 5),
    _NmDropsHighThres_Type()
)
nmDropsHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmDropsHighThres.setStatus("mandatory")
_NmSwapSpaceLowThres_Type = Integer32
_NmSwapSpaceLowThres_Object = MibScalar
nmSwapSpaceLowThres = _NmSwapSpaceLowThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 6),
    _NmSwapSpaceLowThres_Type()
)
nmSwapSpaceLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmSwapSpaceLowThres.setStatus("mandatory")
_NmFreeMemLowThres_Type = Integer32
_NmFreeMemLowThres_Object = MibScalar
nmFreeMemLowThres = _NmFreeMemLowThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 7),
    _NmFreeMemLowThres_Type()
)
nmFreeMemLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmFreeMemLowThres.setStatus("mandatory")
_NmCommBuffHighThres_Type = Integer32
_NmCommBuffHighThres_Object = MibScalar
nmCommBuffHighThres = _NmCommBuffHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 8),
    _NmCommBuffHighThres_Type()
)
nmCommBuffHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCommBuffHighThres.setStatus("mandatory")
_NmAllocFailHighThres_Type = Integer32
_NmAllocFailHighThres_Object = MibScalar
nmAllocFailHighThres = _NmAllocFailHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 9),
    _NmAllocFailHighThres_Type()
)
nmAllocFailHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmAllocFailHighThres.setStatus("mandatory")
_NmCacheHitsLowThres_Type = Integer32
_NmCacheHitsLowThres_Object = MibScalar
nmCacheHitsLowThres = _NmCacheHitsLowThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 10),
    _NmCacheHitsLowThres_Type()
)
nmCacheHitsLowThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmCacheHitsLowThres.setStatus("mandatory")
_NmDiskBusyHighThres_Type = Integer32
_NmDiskBusyHighThres_Object = MibScalar
nmDiskBusyHighThres = _NmDiskBusyHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 11),
    _NmDiskBusyHighThres_Type()
)
nmDiskBusyHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmDiskBusyHighThres.setStatus("mandatory")
_NmMsgAvgHighThres_Type = Integer32
_NmMsgAvgHighThres_Object = MibScalar
nmMsgAvgHighThres = _NmMsgAvgHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 12),
    _NmMsgAvgHighThres_Type()
)
nmMsgAvgHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmMsgAvgHighThres.setStatus("mandatory")
_NmInodeUseHighThres_Type = Integer32
_NmInodeUseHighThres_Object = MibScalar
nmInodeUseHighThres = _NmInodeUseHighThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 11, 13),
    _NmInodeUseHighThres_Type()
)
nmInodeUseHighThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmInodeUseHighThres.setStatus("mandatory")
_Trapdata_ObjectIdentity = ObjectIdentity
trapdata = _Trapdata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12)
)
_TpAlertTime_Type = Integer32
_TpAlertTime_Object = MibScalar
tpAlertTime = _TpAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 1),
    _TpAlertTime_Type()
)
tpAlertTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpAlertTime.setStatus("mandatory")
_TpErrorCode_Type = Integer32
_TpErrorCode_Object = MibScalar
tpErrorCode = _TpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 2),
    _TpErrorCode_Type()
)
tpErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpErrorCode.setStatus("mandatory")
_TpUserName_Type = OctetString
_TpUserName_Object = MibScalar
tpUserName = _TpUserName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 3),
    _TpUserName_Type()
)
tpUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpUserName.setStatus("mandatory")
_TpSvcName_Type = OctetString
_TpSvcName_Object = MibScalar
tpSvcName = _TpSvcName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 4),
    _TpSvcName_Type()
)
tpSvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSvcName.setStatus("mandatory")
_TpSvrName_Type = OctetString
_TpSvrName_Object = MibScalar
tpSvrName = _TpSvrName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 5),
    _TpSvrName_Type()
)
tpSvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSvrName.setStatus("mandatory")
_TpRefSvcName_Type = OctetString
_TpRefSvcName_Object = MibScalar
tpRefSvcName = _TpRefSvcName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 6),
    _TpRefSvcName_Type()
)
tpRefSvcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpRefSvcName.setStatus("mandatory")
_TpRefSvrName_Type = OctetString
_TpRefSvrName_Object = MibScalar
tpRefSvrName = _TpRefSvrName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 7),
    _TpRefSvrName_Type()
)
tpRefSvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpRefSvrName.setStatus("mandatory")
_TpJobId_Type = Integer32
_TpJobId_Object = MibScalar
tpJobId = _TpJobId_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 8),
    _TpJobId_Type()
)
tpJobId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpJobId.setStatus("mandatory")
_TpPaperFormat_Type = OctetString
_TpPaperFormat_Object = MibScalar
tpPaperFormat = _TpPaperFormat_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 9),
    _TpPaperFormat_Type()
)
tpPaperFormat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpPaperFormat.setStatus("mandatory")
_TpJobTotal_Type = Integer32
_TpJobTotal_Object = MibScalar
tpJobTotal = _TpJobTotal_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 10),
    _TpJobTotal_Type()
)
tpJobTotal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpJobTotal.setStatus("mandatory")
_TpConnId_Type = Integer32
_TpConnId_Object = MibScalar
tpConnId = _TpConnId_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 11),
    _TpConnId_Type()
)
tpConnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpConnId.setStatus("mandatory")
_TpMailSender_Type = OctetString
_TpMailSender_Object = MibScalar
tpMailSender = _TpMailSender_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 12),
    _TpMailSender_Type()
)
tpMailSender.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpMailSender.setStatus("mandatory")
_TpPortId_Type = OctetString
_TpPortId_Object = MibScalar
tpPortId = _TpPortId_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 13),
    _TpPortId_Type()
)
tpPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpPortId.setStatus("mandatory")
_TpRtnName_Type = OctetString
_TpRtnName_Object = MibScalar
tpRtnName = _TpRtnName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 14),
    _TpRtnName_Type()
)
tpRtnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpRtnName.setStatus("mandatory")
_Tp162erravg_Type = Integer32
_Tp162erravg_Object = MibScalar
tp162erravg = _Tp162erravg_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 15),
    _Tp162erravg_Type()
)
tp162erravg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp162erravg.setStatus("mandatory")
_Tp162errThresHigh_Type = Integer32
_Tp162errThresHigh_Object = MibScalar
tp162errThresHigh = _Tp162errThresHigh_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 16),
    _Tp162errThresHigh_Type()
)
tp162errThresHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp162errThresHigh.setStatus("mandatory")
_Tp162errTotal_Type = Integer32
_Tp162errTotal_Object = MibScalar
tp162errTotal = _Tp162errTotal_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 17),
    _Tp162errTotal_Type()
)
tp162errTotal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp162errTotal.setStatus("mandatory")
_TpGrpName_Type = OctetString
_TpGrpName_Object = MibScalar
tpGrpName = _TpGrpName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 18),
    _TpGrpName_Type()
)
tpGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpGrpName.setStatus("mandatory")
_TpNumGrps_Type = Integer32
_TpNumGrps_Object = MibScalar
tpNumGrps = _TpNumGrps_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 19),
    _TpNumGrps_Type()
)
tpNumGrps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpNumGrps.setStatus("mandatory")
_TpGrpLimit_Type = Integer32
_TpGrpLimit_Object = MibScalar
tpGrpLimit = _TpGrpLimit_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 20),
    _TpGrpLimit_Type()
)
tpGrpLimit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpGrpLimit.setStatus("mandatory")
_TpOldSerNum_Type = Integer32
_TpOldSerNum_Object = MibScalar
tpOldSerNum = _TpOldSerNum_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 21),
    _TpOldSerNum_Type()
)
tpOldSerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpOldSerNum.setStatus("mandatory")
_TpNewSerNum_Type = Integer32
_TpNewSerNum_Object = MibScalar
tpNewSerNum = _TpNewSerNum_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 22),
    _TpNewSerNum_Type()
)
tpNewSerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpNewSerNum.setStatus("mandatory")
_TpDiskSpaceLeft_Type = Integer32
_TpDiskSpaceLeft_Object = MibScalar
tpDiskSpaceLeft = _TpDiskSpaceLeft_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 23),
    _TpDiskSpaceLeft_Type()
)
tpDiskSpaceLeft.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpDiskSpaceLeft.setStatus("mandatory")
_TpMailMessageId_Type = OctetString
_TpMailMessageId_Object = MibScalar
tpMailMessageId = _TpMailMessageId_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 24),
    _TpMailMessageId_Type()
)
tpMailMessageId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpMailMessageId.setStatus("mandatory")
_TpSockOvFlowNum_Type = Integer32
_TpSockOvFlowNum_Object = MibScalar
tpSockOvFlowNum = _TpSockOvFlowNum_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 25),
    _TpSockOvFlowNum_Type()
)
tpSockOvFlowNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSockOvFlowNum.setStatus("mandatory")
_TpDiskNName_Type = OctetString
_TpDiskNName_Object = MibScalar
tpDiskNName = _TpDiskNName_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 26),
    _TpDiskNName_Type()
)
tpDiskNName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpDiskNName.setStatus("mandatory")
_TpSvrNetId_Type = Integer32
_TpSvrNetId_Object = MibScalar
tpSvrNetId = _TpSvrNetId_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 27),
    _TpSvrNetId_Type()
)
tpSvrNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSvrNetId.setStatus("mandatory")
_TpSubNetId_Type = Integer32
_TpSubNetId_Object = MibScalar
tpSubNetId = _TpSubNetId_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 28),
    _TpSubNetId_Type()
)
tpSubNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSubNetId.setStatus("mandatory")
_TpSlotNum_Type = Integer32
_TpSlotNum_Object = MibScalar
tpSlotNum = _TpSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 29),
    _TpSlotNum_Type()
)
tpSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpSlotNum.setStatus("mandatory")
_TpLineNum_Type = Integer32
_TpLineNum_Object = MibScalar
tpLineNum = _TpLineNum_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 30),
    _TpLineNum_Type()
)
tpLineNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpLineNum.setStatus("mandatory")
_TpFRcvd_Type = Integer32
_TpFRcvd_Object = MibScalar
tpFRcvd = _TpFRcvd_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 31),
    _TpFRcvd_Type()
)
tpFRcvd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpFRcvd.setStatus("mandatory")
_TpFXmtd_Type = Integer32
_TpFXmtd_Object = MibScalar
tpFXmtd = _TpFXmtd_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 32),
    _TpFXmtd_Type()
)
tpFXmtd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpFXmtd.setStatus("mandatory")
_TpLnkDropsThres_Type = Integer32
_TpLnkDropsThres_Object = MibScalar
tpLnkDropsThres = _TpLnkDropsThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 33),
    _TpLnkDropsThres_Type()
)
tpLnkDropsThres.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpLnkDropsThres.setStatus("mandatory")
_TpLnkReXtThres_Type = Integer32
_TpLnkReXtThres_Object = MibScalar
tpLnkReXtThres = _TpLnkReXtThres_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 12, 34),
    _TpLnkReXtThres_Type()
)
tpLnkReXtThres.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpLnkReXtThres.setStatus("mandatory")
_Ams_ObjectIdentity = ObjectIdentity
ams = _Ams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13)
)
_AmsRegTable_Object = MibTable
amsRegTable = _AmsRegTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    amsRegTable.setStatus("mandatory")
_AmsRegEntry_Object = MibTableRow
amsRegEntry = _AmsRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1)
)
amsRegEntry.setIndexNames(
    (0, "VINES-MIB", "amsRegIndex"),
)
if mibBuilder.loadTexts:
    amsRegEntry.setStatus("mandatory")
_AmsRegIndex_Type = Integer32
_AmsRegIndex_Object = MibTableColumn
amsRegIndex = _AmsRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 1),
    _AmsRegIndex_Type()
)
amsRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegIndex.setStatus("mandatory")
_AmsRegIdInstance_Type = OctetString
_AmsRegIdInstance_Object = MibTableColumn
amsRegIdInstance = _AmsRegIdInstance_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 2),
    _AmsRegIdInstance_Type()
)
amsRegIdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegIdInstance.setStatus("mandatory")
_AmsRegIdClass_Type = Integer32
_AmsRegIdClass_Object = MibTableColumn
amsRegIdClass = _AmsRegIdClass_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 3),
    _AmsRegIdClass_Type()
)
amsRegIdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegIdClass.setStatus("mandatory")
_AmsRegIdTid_Type = Integer32
_AmsRegIdTid_Object = MibTableColumn
amsRegIdTid = _AmsRegIdTid_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 4),
    _AmsRegIdTid_Type()
)
amsRegIdTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegIdTid.setStatus("mandatory")
_AmsRegPort_Type = OctetString
_AmsRegPort_Object = MibTableColumn
amsRegPort = _AmsRegPort_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 5),
    _AmsRegPort_Type()
)
amsRegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegPort.setStatus("mandatory")
_AmsRegWhoAdded_Type = OctetString
_AmsRegWhoAdded_Object = MibTableColumn
amsRegWhoAdded = _AmsRegWhoAdded_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 6),
    _AmsRegWhoAdded_Type()
)
amsRegWhoAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegWhoAdded.setStatus("mandatory")
_AmsRegAlertee_Type = OctetString
_AmsRegAlertee_Object = MibTableColumn
amsRegAlertee = _AmsRegAlertee_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 7),
    _AmsRegAlertee_Type()
)
amsRegAlertee.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegAlertee.setStatus("mandatory")


class _AmsRegAction_Type(Integer32):
    """Custom type amsRegAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bleepstname", 2),
          ("sendipcport", 1))
    )


_AmsRegAction_Type.__name__ = "Integer32"
_AmsRegAction_Object = MibTableColumn
amsRegAction = _AmsRegAction_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 1, 1, 8),
    _AmsRegAction_Type()
)
amsRegAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsRegAction.setStatus("mandatory")
_AmsAlertLogTable_Object = MibTable
amsAlertLogTable = _AmsAlertLogTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    amsAlertLogTable.setStatus("mandatory")
_AmsLogEntry_Object = MibTableRow
amsLogEntry = _AmsLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1)
)
amsLogEntry.setIndexNames(
    (0, "VINES-MIB", "amsLogFileIndex"),
    (0, "VINES-MIB", "amsLogRecIndex"),
)
if mibBuilder.loadTexts:
    amsLogEntry.setStatus("mandatory")


class _AmsLogFileIndex_Type(Integer32):
    """Custom type amsLogFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 2),
          ("previous", 1))
    )


_AmsLogFileIndex_Type.__name__ = "Integer32"
_AmsLogFileIndex_Object = MibTableColumn
amsLogFileIndex = _AmsLogFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1, 1),
    _AmsLogFileIndex_Type()
)
amsLogFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLogFileIndex.setStatus("mandatory")
_AmsLogRecIndex_Type = Integer32
_AmsLogRecIndex_Object = MibTableColumn
amsLogRecIndex = _AmsLogRecIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1, 2),
    _AmsLogRecIndex_Type()
)
amsLogRecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLogRecIndex.setStatus("mandatory")
_AmsLogIdInstance_Type = OctetString
_AmsLogIdInstance_Object = MibTableColumn
amsLogIdInstance = _AmsLogIdInstance_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1, 3),
    _AmsLogIdInstance_Type()
)
amsLogIdInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLogIdInstance.setStatus("mandatory")
_AmsLogIdClass_Type = Integer32
_AmsLogIdClass_Object = MibTableColumn
amsLogIdClass = _AmsLogIdClass_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1, 4),
    _AmsLogIdClass_Type()
)
amsLogIdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLogIdClass.setStatus("mandatory")
_AmsLogIdTid_Type = Integer32
_AmsLogIdTid_Object = MibTableColumn
amsLogIdTid = _AmsLogIdTid_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1, 5),
    _AmsLogIdTid_Type()
)
amsLogIdTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLogIdTid.setStatus("mandatory")
_AmsLogAlertTime_Type = TimeTicks
_AmsLogAlertTime_Object = MibTableColumn
amsLogAlertTime = _AmsLogAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1, 6),
    _AmsLogAlertTime_Type()
)
amsLogAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLogAlertTime.setStatus("mandatory")
_AmsLogAlertString_Type = OctetString
_AmsLogAlertString_Object = MibTableColumn
amsLogAlertString = _AmsLogAlertString_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 13, 2, 1, 7),
    _AmsLogAlertString_Type()
)
amsLogAlertString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amsLogAlertString.setStatus("mandatory")
_Mailservice_ObjectIdentity = ObjectIdentity
mailservice = _Mailservice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 14)
)
_MlMailBoxTable_Object = MibTable
mlMailBoxTable = _MlMailBoxTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    mlMailBoxTable.setStatus("mandatory")
_MlMailBoxTableEntry_Object = MibTableRow
mlMailBoxTableEntry = _MlMailBoxTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 14, 1, 1)
)
mlMailBoxTableEntry.setIndexNames(
    (0, "VINES-MIB", "mlMBTableIndex"),
)
if mibBuilder.loadTexts:
    mlMailBoxTableEntry.setStatus("mandatory")
_MlMBTableIndex_Type = Integer32
_MlMBTableIndex_Object = MibTableColumn
mlMBTableIndex = _MlMBTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 14, 1, 1, 1),
    _MlMBTableIndex_Type()
)
mlMBTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlMBTableIndex.setStatus("mandatory")
_MlMBTableMBOwner_Type = OctetString
_MlMBTableMBOwner_Object = MibTableColumn
mlMBTableMBOwner = _MlMBTableMBOwner_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 14, 1, 1, 2),
    _MlMBTableMBOwner_Type()
)
mlMBTableMBOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlMBTableMBOwner.setStatus("mandatory")
_MlMBTableUnreadMsgs_Type = Integer32
_MlMBTableUnreadMsgs_Object = MibTableColumn
mlMBTableUnreadMsgs = _MlMBTableUnreadMsgs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 14, 1, 1, 3),
    _MlMBTableUnreadMsgs_Type()
)
mlMBTableUnreadMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlMBTableUnreadMsgs.setStatus("mandatory")
_MlMBTableTotalMsgs_Type = Integer32
_MlMBTableTotalMsgs_Object = MibTableColumn
mlMBTableTotalMsgs = _MlMBTableTotalMsgs_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 14, 1, 1, 4),
    _MlMBTableTotalMsgs_Type()
)
mlMBTableTotalMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlMBTableTotalMsgs.setStatus("mandatory")
_Vlogs_ObjectIdentity = ObjectIdentity
vlogs = _Vlogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 15)
)
_VlogsTable_Object = MibTable
vlogsTable = _VlogsTable_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    vlogsTable.setStatus("mandatory")
_VlogsEntry_Object = MibTableRow
vlogsEntry = _VlogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 15, 1, 1)
)
vlogsEntry.setIndexNames(
    (0, "VINES-MIB", "vlogsFileIndex"),
)
if mibBuilder.loadTexts:
    vlogsEntry.setStatus("mandatory")


class _VlogsFileIndex_Type(Integer32):
    """Custom type vlogsFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("patch", 1))
    )


_VlogsFileIndex_Type.__name__ = "Integer32"
_VlogsFileIndex_Object = MibTableColumn
vlogsFileIndex = _VlogsFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 15, 1, 1, 1),
    _VlogsFileIndex_Type()
)
vlogsFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlogsFileIndex.setStatus("mandatory")
_VlogsDescr_Type = OctetString
_VlogsDescr_Object = MibTableColumn
vlogsDescr = _VlogsDescr_Object(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 15, 1, 1, 2),
    _VlogsDescr_Type()
)
vlogsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlogsDescr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nmLoadAvgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 1)
)
nmLoadAvgHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmLoadAvg15HighThres"))
)
if mibBuilder.loadTexts:
    nmLoadAvgHigh.setStatus(
        ""
    )

nmSwapAvgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 2)
)
nmSwapAvgHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmSwapAvgHighThres"))
)
if mibBuilder.loadTexts:
    nmSwapAvgHigh.setStatus(
        ""
    )

nmDropsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 3)
)
nmDropsHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmDropsHighThres"))
)
if mibBuilder.loadTexts:
    nmDropsHigh.setStatus(
        ""
    )

nmFreeSwapLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 4)
)
nmFreeSwapLow.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmSwapSpaceLowThres"))
)
if mibBuilder.loadTexts:
    nmFreeSwapLow.setStatus(
        ""
    )

nmFreeMemLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 5)
)
nmFreeMemLow.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmFreeMemLowThres"))
)
if mibBuilder.loadTexts:
    nmFreeMemLow.setStatus(
        ""
    )

nmCommBuffHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 6)
)
nmCommBuffHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmCommBuffHighThres"))
)
if mibBuilder.loadTexts:
    nmCommBuffHigh.setStatus(
        ""
    )

nmSockInUseHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 7)
)
nmSockInUseHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmSockInUseHighThres"))
)
if mibBuilder.loadTexts:
    nmSockInUseHigh.setStatus(
        ""
    )

nmSockOvflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 8)
)
nmSockOvflow.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvcName"),
        ("VINES-MIB", "tpSockOvFlowNum"))
)
if mibBuilder.loadTexts:
    nmSockOvflow.setStatus(
        ""
    )

nmMsgAvgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 9)
)
nmMsgAvgHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmMsgAvgHighThres"))
)
if mibBuilder.loadTexts:
    nmMsgAvgHigh.setStatus(
        ""
    )

nmAllocFail_High = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 10)
)
nmAllocFail_High.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmAllocFailHighThres"))
)
if mibBuilder.loadTexts:
    nmAllocFail_High.setStatus(
        ""
    )

nmCacheHits_Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 11)
)
nmCacheHits_Low.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmCacheHitsLowThres"))
)
if mibBuilder.loadTexts:
    nmCacheHits_Low.setStatus(
        ""
    )

nmDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 12)
)
nmDiskFull.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpDiskNName"),
        ("VINES-MIB", "nmDiskUseHighThres"))
)
if mibBuilder.loadTexts:
    nmDiskFull.setStatus(
        ""
    )

nmDiskBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 13)
)
nmDiskBusy.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpDiskNName"),
        ("VINES-MIB", "nmDiskBusyHighThres"))
)
if mibBuilder.loadTexts:
    nmDiskBusy.setStatus(
        ""
    )

nmInodesHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 14)
)
nmInodesHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "nmInodeUseHighThres"))
)
if mibBuilder.loadTexts:
    nmInodesHigh.setStatus(
        ""
    )

nmProcsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 15)
)
nmProcsHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    nmProcsHigh.setStatus(
        ""
    )

nmTKRingOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 16)
)
nmTKRingOpen.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpSlotNum"))
)
if mibBuilder.loadTexts:
    nmTKRingOpen.setStatus(
        ""
    )

nmTKRingSigLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 17)
)
nmTKRingSigLoss.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpSlotNum"))
)
if mibBuilder.loadTexts:
    nmTKRingSigLoss.setStatus(
        ""
    )

nmTKRingHardErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 18)
)
nmTKRingHardErr.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpSlotNum"))
)
if mibBuilder.loadTexts:
    nmTKRingHardErr.setStatus(
        ""
    )

nmTKRingRmvHardErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 19)
)
nmTKRingRmvHardErr.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpSlotNum"))
)
if mibBuilder.loadTexts:
    nmTKRingRmvHardErr.setStatus(
        ""
    )

nmTKRingRmvMacFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 20)
)
nmTKRingRmvMacFrame.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpSlotNum"))
)
if mibBuilder.loadTexts:
    nmTKRingRmvMacFrame.setStatus(
        ""
    )

nmLnkDropsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 21)
)
nmLnkDropsHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpLnkDropsThres"),
        ("VINES-MIB", "tpSlotNum"),
        ("VINES-MIB", "tpLineNum"),
        ("VINES-MIB", "tpFRcvd"))
)
if mibBuilder.loadTexts:
    nmLnkDropsHigh.setStatus(
        ""
    )

nmLnkReTXHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 22)
)
nmLnkReTXHigh.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpLnkReXtThres"),
        ("VINES-MIB", "tpSlotNum"),
        ("VINES-MIB", "tpLineNum"),
        ("VINES-MIB", "tpFXmtd"))
)
if mibBuilder.loadTexts:
    nmLnkReTXHigh.setStatus(
        ""
    )

bsSysBkUpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 23)
)
bsSysBkUpFailed.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    bsSysBkUpFailed.setStatus(
        ""
    )

bsIncBkUpAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 24)
)
bsIncBkUpAborted.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    bsIncBkUpAborted.setStatus(
        ""
    )

bsIncBkUpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 25)
)
bsIncBkUpFailed.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    bsIncBkUpFailed.setStatus(
        ""
    )

bsSvcBkUpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 26)
)
bsSvcBkUpFailed.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    bsSvcBkUpFailed.setStatus(
        ""
    )

psFormUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 27)
)
psFormUnavail.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpJobId"),
        ("VINES-MIB", "tpPaperFormat"))
)
if mibBuilder.loadTexts:
    psFormUnavail.setStatus(
        ""
    )

psUserNoAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 28)
)
psUserNoAuth.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpUserName"),
        ("VINES-MIB", "tpRefSvcName"))
)
if mibBuilder.loadTexts:
    psUserNoAuth.setStatus(
        ""
    )

psBadDest = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 29)
)
psBadDest.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvcName"))
)
if mibBuilder.loadTexts:
    psBadDest.setStatus(
        ""
    )

psJobReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 30)
)
psJobReject.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpJobId"),
        ("VINES-MIB", "tpRefSvcName"),
        ("VINES-MIB", "tpUserName"))
)
if mibBuilder.loadTexts:
    psJobReject.setStatus(
        ""
    )

psQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 31)
)
psQueueFull.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvcName"),
        ("VINES-MIB", "tpJobTotal"))
)
if mibBuilder.loadTexts:
    psQueueFull.setStatus(
        ""
    )

psOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 32)
)
psOffline.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvcName"))
)
if mibBuilder.loadTexts:
    psOffline.setStatus(
        ""
    )

psPapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 33)
)
psPapError.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"),
        ("VINES-MIB", "tpConnId"))
)
if mibBuilder.loadTexts:
    psPapError.setStatus(
        ""
    )

psAtalkErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 34)
)
psAtalkErr.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    psAtalkErr.setStatus(
        ""
    )

psPsPrinterErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 35)
)
psPsPrinterErr.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    psPsPrinterErr.setStatus(
        ""
    )

ssSvcNoStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 36)
)
ssSvcNoStart.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvcName"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    ssSvcNoStart.setStatus(
        ""
    )

ssNoReconnVS = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 37)
)
ssNoReconnVS.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    ssNoReconnVS.setStatus(
        ""
    )

ssNoReconnST = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 38)
)
ssNoReconnST.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    ssNoReconnST.setStatus(
        ""
    )

ssSvcCrashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 39)
)
ssSvcCrashed.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvcName"))
)
if mibBuilder.loadTexts:
    ssSvcCrashed.setStatus(
        ""
    )

ssSvcRecrashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 40)
)
ssSvcRecrashed.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvcName"))
)
if mibBuilder.loadTexts:
    ssSvcRecrashed.setStatus(
        ""
    )

ssBadSvcDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 41)
)
ssBadSvcDB.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    ssBadSvcDB.setStatus(
        ""
    )

ssPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 42)
)
ssPowerFail.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    ssPowerFail.setStatus(
        ""
    )

ssDying = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 43)
)
ssDying.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    ssDying.setStatus(
        ""
    )

ssPanicDBWrite = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 44)
)
ssPanicDBWrite.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    ssPanicDBWrite.setStatus(
        ""
    )

ssPanicWait = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 45)
)
ssPanicWait.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    ssPanicWait.setStatus(
        ""
    )

ssPanicUlimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 46)
)
ssPanicUlimit.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    ssPanicUlimit.setStatus(
        ""
    )

ssNoMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 47)
)
ssNoMemory.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    ssNoMemory.setStatus(
        ""
    )

ssTimeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 48)
)
ssTimeSet.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    ssTimeSet.setStatus(
        ""
    )

msMBoxFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 49)
)
msMBoxFull.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpUserName"),
        ("VINES-MIB", "tpMailSender"))
)
if mibBuilder.loadTexts:
    msMBoxFull.setStatus(
        ""
    )

msDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 50)
)
msDiskFull.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpDiskSpaceLeft"))
)
if mibBuilder.loadTexts:
    msDiskFull.setStatus(
        ""
    )

msPanic = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 51)
)
msPanic.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    msPanic.setStatus(
        ""
    )

msCompressFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 52)
)
msCompressFail.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpMailMessageId"))
)
if mibBuilder.loadTexts:
    msCompressFail.setStatus(
        ""
    )

msDecompressFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 53)
)
msDecompressFail.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpMailMessageId"))
)
if mibBuilder.loadTexts:
    msDecompressFail.setStatus(
        ""
    )

msMasquerade = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 54)
)
msMasquerade.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpMailSender"),
        ("VINES-MIB", "tpUserName"))
)
if mibBuilder.loadTexts:
    msMasquerade.setStatus(
        ""
    )

msMTAPanic = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 55)
)
msMTAPanic.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    msMTAPanic.setStatus(
        ""
    )

msBMSPanic = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 56)
)
msBMSPanic.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    msBMSPanic.setStatus(
        ""
    )

vsNoReachST = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 57)
)
vsNoReachST.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    vsNoReachST.setStatus(
        ""
    )

vsBadLoginPhysLoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 58)
)
vsBadLoginPhysLoc.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpPortId"),
        ("VINES-MIB", "tpUserName"))
)
if mibBuilder.loadTexts:
    vsBadLoginPhysLoc.setStatus(
        ""
    )

vsBadLoginDialin = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 59)
)
vsBadLoginDialin.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpPortId"),
        ("VINES-MIB", "tpUserName"))
)
if mibBuilder.loadTexts:
    vsBadLoginDialin.setStatus(
        ""
    )

vsBadLoginTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 60)
)
vsBadLoginTime.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpUserName"))
)
if mibBuilder.loadTexts:
    vsBadLoginTime.setStatus(
        ""
    )

vsMaxBadLogins = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 61)
)
vsMaxBadLogins.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpPortId"),
        ("VINES-MIB", "tpUserName"))
)
if mibBuilder.loadTexts:
    vsMaxBadLogins.setStatus(
        ""
    )

vsSDBInconsist = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 62)
)
vsSDBInconsist.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    vsSDBInconsist.setStatus(
        ""
    )

vsNoSessAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 63)
)
vsNoSessAvail.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    vsNoSessAvail.setStatus(
        ""
    )

vsSvrSvrPwd = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 64)
)
vsSvrSvrPwd.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRefSvrName"))
)
if mibBuilder.loadTexts:
    vsSvrSvrPwd.setStatus(
        ""
    )

vsNoSTLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 65)
)
vsNoSTLogin.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    vsNoSTLogin.setStatus(
        ""
    )

vsNoSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 66)
)
vsNoSpace.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    vsNoSpace.setStatus(
        ""
    )

vsLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 67)
)
vsLinkDown.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpSvrNetId"))
)
if mibBuilder.loadTexts:
    vsLinkDown.setStatus(
        ""
    )

vsPCDialTerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 68)
)
vsPCDialTerm.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpUserName"),
        ("VINES-MIB", "tpSvrNetId"),
        ("VINES-MIB", "tpSubNetId"),
        ("VINES-MIB", "tpSlotNum"),
        ("VINES-MIB", "tpLineNum"))
)
if mibBuilder.loadTexts:
    vsPCDialTerm.setStatus(
        ""
    )

vsPCDialInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 69)
)
vsPCDialInit.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpUserName"),
        ("VINES-MIB", "tpSvrNetId"),
        ("VINES-MIB", "tpSubNetId"),
        ("VINES-MIB", "tpSlotNum"),
        ("VINES-MIB", "tpLineNum"))
)
if mibBuilder.loadTexts:
    vsPCDialInit.setStatus(
        ""
    )

afpAtalkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 70)
)
afpAtalkDown.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"))
)
if mibBuilder.loadTexts:
    afpAtalkDown.setStatus(
        ""
    )

afpSessDiscon = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 71)
)
afpSessDiscon.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpUserName"))
)
if mibBuilder.loadTexts:
    afpSessDiscon.setStatus(
        ""
    )

daGCoreDump = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 72)
)
daGCoreDump.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRtnName"))
)
if mibBuilder.loadTexts:
    daGCoreDump.setStatus(
        ""
    )

daSCoreDump = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 73)
)
daSCoreDump.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpRtnName"))
)
if mibBuilder.loadTexts:
    daSCoreDump.setStatus(
        ""
    )

stCoreDump = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 74)
)
stCoreDump.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpErrorCode"))
)
if mibBuilder.loadTexts:
    stCoreDump.setStatus(
        ""
    )

st162Errs = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 75)
)
st162Errs.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tp162erravg"),
        ("VINES-MIB", "tp162errThresHigh"),
        ("VINES-MIB", "tp162errTotal"))
)
if mibBuilder.loadTexts:
    st162Errs.setStatus(
        ""
    )

stAddedGrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 76)
)
stAddedGrp.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpGrpName"),
        ("VINES-MIB", "tpRefSvrName"))
)
if mibBuilder.loadTexts:
    stAddedGrp.setStatus(
        ""
    )

stDeletedGrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 77)
)
stDeletedGrp.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpGrpName"),
        ("VINES-MIB", "tpRefSvrName"))
)
if mibBuilder.loadTexts:
    stDeletedGrp.setStatus(
        ""
    )

stRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 78)
)
stRebuild.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpGrpName"))
)
if mibBuilder.loadTexts:
    stRebuild.setStatus(
        ""
    )

stGrpLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 79)
)
stGrpLimit.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpNumGrps"),
        ("VINES-MIB", "tpGrpLimit"))
)
if mibBuilder.loadTexts:
    stGrpLimit.setStatus(
        ""
    )

stSerialNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 80)
)
stSerialNum.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpOldSerNum"),
        ("VINES-MIB", "tpNewSerNum"))
)
if mibBuilder.loadTexts:
    stSerialNum.setStatus(
        ""
    )

stDupGrp = NotificationType(
    (1, 3, 6, 1, 4, 1, 130, 1, 2, 0, 81)
)
stDupGrp.setObjects(
      *(("VINES-MIB", "tpSvrName"),
        ("VINES-MIB", "tpSvcName"),
        ("VINES-MIB", "tpAlertTime"),
        ("VINES-MIB", "tpGrpName"),
        ("VINES-MIB", "tpSvrNetId"))
)
if mibBuilder.loadTexts:
    stDupGrp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VINES-MIB",
    **{"banyan": banyan,
       "vinesmibs": vinesmibs,
       "mib1": mib1,
       "mib2": mib2,
       "nmLoadAvgHigh": nmLoadAvgHigh,
       "nmSwapAvgHigh": nmSwapAvgHigh,
       "nmDropsHigh": nmDropsHigh,
       "nmFreeSwapLow": nmFreeSwapLow,
       "nmFreeMemLow": nmFreeMemLow,
       "nmCommBuffHigh": nmCommBuffHigh,
       "nmSockInUseHigh": nmSockInUseHigh,
       "nmSockOvflow": nmSockOvflow,
       "nmMsgAvgHigh": nmMsgAvgHigh,
       "nmAllocFail-High": nmAllocFail_High,
       "nmCacheHits-Low": nmCacheHits_Low,
       "nmDiskFull": nmDiskFull,
       "nmDiskBusy": nmDiskBusy,
       "nmInodesHigh": nmInodesHigh,
       "nmProcsHigh": nmProcsHigh,
       "nmTKRingOpen": nmTKRingOpen,
       "nmTKRingSigLoss": nmTKRingSigLoss,
       "nmTKRingHardErr": nmTKRingHardErr,
       "nmTKRingRmvHardErr": nmTKRingRmvHardErr,
       "nmTKRingRmvMacFrame": nmTKRingRmvMacFrame,
       "nmLnkDropsHigh": nmLnkDropsHigh,
       "nmLnkReTXHigh": nmLnkReTXHigh,
       "bsSysBkUpFailed": bsSysBkUpFailed,
       "bsIncBkUpAborted": bsIncBkUpAborted,
       "bsIncBkUpFailed": bsIncBkUpFailed,
       "bsSvcBkUpFailed": bsSvcBkUpFailed,
       "psFormUnavail": psFormUnavail,
       "psUserNoAuth": psUserNoAuth,
       "psBadDest": psBadDest,
       "psJobReject": psJobReject,
       "psQueueFull": psQueueFull,
       "psOffline": psOffline,
       "psPapError": psPapError,
       "psAtalkErr": psAtalkErr,
       "psPsPrinterErr": psPsPrinterErr,
       "ssSvcNoStart": ssSvcNoStart,
       "ssNoReconnVS": ssNoReconnVS,
       "ssNoReconnST": ssNoReconnST,
       "ssSvcCrashed": ssSvcCrashed,
       "ssSvcRecrashed": ssSvcRecrashed,
       "ssBadSvcDB": ssBadSvcDB,
       "ssPowerFail": ssPowerFail,
       "ssDying": ssDying,
       "ssPanicDBWrite": ssPanicDBWrite,
       "ssPanicWait": ssPanicWait,
       "ssPanicUlimit": ssPanicUlimit,
       "ssNoMemory": ssNoMemory,
       "ssTimeSet": ssTimeSet,
       "msMBoxFull": msMBoxFull,
       "msDiskFull": msDiskFull,
       "msPanic": msPanic,
       "msCompressFail": msCompressFail,
       "msDecompressFail": msDecompressFail,
       "msMasquerade": msMasquerade,
       "msMTAPanic": msMTAPanic,
       "msBMSPanic": msBMSPanic,
       "vsNoReachST": vsNoReachST,
       "vsBadLoginPhysLoc": vsBadLoginPhysLoc,
       "vsBadLoginDialin": vsBadLoginDialin,
       "vsBadLoginTime": vsBadLoginTime,
       "vsMaxBadLogins": vsMaxBadLogins,
       "vsSDBInconsist": vsSDBInconsist,
       "vsNoSessAvail": vsNoSessAvail,
       "vsSvrSvrPwd": vsSvrSvrPwd,
       "vsNoSTLogin": vsNoSTLogin,
       "vsNoSpace": vsNoSpace,
       "vsLinkDown": vsLinkDown,
       "vsPCDialTerm": vsPCDialTerm,
       "vsPCDialInit": vsPCDialInit,
       "afpAtalkDown": afpAtalkDown,
       "afpSessDiscon": afpSessDiscon,
       "daGCoreDump": daGCoreDump,
       "daSCoreDump": daSCoreDump,
       "stCoreDump": stCoreDump,
       "st162Errs": st162Errs,
       "stAddedGrp": stAddedGrp,
       "stDeletedGrp": stDeletedGrp,
       "stRebuild": stRebuild,
       "stGrpLimit": stGrpLimit,
       "stSerialNum": stSerialNum,
       "stDupGrp": stDupGrp,
       "systemsummary": systemsummary,
       "ssName": ssName,
       "ssNetid": ssNetid,
       "ssSwRev": ssSwRev,
       "ssLoadAvg1": ssLoadAvg1,
       "ssLoadAvg5": ssLoadAvg5,
       "ssLoadAvg15": ssLoadAvg15,
       "ssMsgAvg1": ssMsgAvg1,
       "ssMsgsIn": ssMsgsIn,
       "ssMsgsOut": ssMsgsOut,
       "ssDrops": ssDrops,
       "ssSwapAvg": ssSwapAvg,
       "ssProcType": ssProcType,
       "ssProdType": ssProdType,
       "ssProdDescr": ssProdDescr,
       "ssRealMemory": ssRealMemory,
       "ssOsType": ssOsType,
       "ssOsRev": ssOsRev,
       "ssSystemUptime": ssSystemUptime,
       "ssSystemDate": ssSystemDate,
       "ssSystemStatus": ssSystemStatus,
       "ssUserLicenseCfg": ssUserLicenseCfg,
       "services": services,
       "svcNumber": svcNumber,
       "svcTable": svcTable,
       "svcEntry": svcEntry,
       "svcIndex": svcIndex,
       "svcName": svcName,
       "svcStatus": svcStatus,
       "svcUpTime": svcUpTime,
       "svcMsgsIn": svcMsgsIn,
       "svcMsgsOut": svcMsgsOut,
       "svcLocIn": svcLocIn,
       "svcLocOut": svcLocOut,
       "svcActSess": svcActSess,
       "svcTotSess": svcTotSess,
       "svcCategory": svcCategory,
       "svcCpuTime": svcCpuTime,
       "svcSize": svcSize,
       "svcSockets": svcSockets,
       "svcSPPs": svcSPPs,
       "svcLogMask": svcLogMask,
       "svcDiskName": svcDiskName,
       "svcUserTable": svcUserTable,
       "svcUserEntry": svcUserEntry,
       "svcUserSvcIndex": svcUserSvcIndex,
       "svcUserIndex": svcUserIndex,
       "svcUserSvcName": svcUserSvcName,
       "svcUserName": svcUserName,
       "peripherals": peripherals,
       "dskNumber": dskNumber,
       "dskTable": dskTable,
       "dskEntry": dskEntry,
       "dskIndex": dskIndex,
       "dskName": dskName,
       "dskUtil": dskUtil,
       "dskDemand": dskDemand,
       "dskSizeMB": dskSizeMB,
       "dskUsedPct": dskUsedPct,
       "dskStatus": dskStatus,
       "dskNOperations": dskNOperations,
       "dskNBlocks": dskNBlocks,
       "dskResp": dskResp,
       "dskActive": dskActive,
       "dskBlkSize": dskBlkSize,
       "dskNMisc": dskNMisc,
       "dskNErrs": dskNErrs,
       "dskPctBusy": dskPctBusy,
       "dskAvgWait": dskAvgWait,
       "dskAvgService": dskAvgService,
       "filesystem": filesystem,
       "fsTotCache": fsTotCache,
       "fsCacheBufSize": fsCacheBufSize,
       "fsMaxOpenFiles": fsMaxOpenFiles,
       "fsOpenFiles": fsOpenFiles,
       "fsMaxOpensOnFiles": fsMaxOpensOnFiles,
       "fsOpensOnFiles": fsOpensOnFiles,
       "fsRecLocks": fsRecLocks,
       "fsMaxRecLocks": fsMaxRecLocks,
       "fsPctCacheHits": fsPctCacheHits,
       "fsCacheUnavail": fsCacheUnavail,
       "commresources": commresources,
       "commTotBufs": commTotBufs,
       "commBufUsage": commBufUsage,
       "commAllocsFailed": commAllocsFailed,
       "commSocksCfg": commSocksCfg,
       "commSocksInUse": commSocksInUse,
       "commMaxOpenSocks": commMaxOpenSocks,
       "vip": vip,
       "vipTotIn": vipTotIn,
       "vipTotOut": vipTotOut,
       "vipBad": vipBad,
       "vipRouted": vipRouted,
       "vipRoutedHWM": vipRoutedHWM,
       "vipBcast": vipBcast,
       "vipBcastHWM": vipBcastHWM,
       "vipReass": vipReass,
       "vipFrags": vipFrags,
       "vipToDodIP": vipToDodIP,
       "vipFromDodIP": vipFromDodIP,
       "vipInFragments": vipInFragments,
       "vipTooSmall": vipTooSmall,
       "vipBadLength": vipBadLength,
       "vipNoBuffers": vipNoBuffers,
       "vrtp": vrtp,
       "vrtpNbrNumber": vrtpNbrNumber,
       "vrtpNbrTable": vrtpNbrTable,
       "vrtpNbrEntry": vrtpNbrEntry,
       "vrtpNbrNetid": vrtpNbrNetid,
       "vrtpNbrSubNetid": vrtpNbrSubNetid,
       "vrtpNbrType": vrtpNbrType,
       "vrtpNbrIfType": vrtpNbrIfType,
       "vrtpNbrRemAddress": vrtpNbrRemAddress,
       "vrtpNbrLocAddress": vrtpNbrLocAddress,
       "vrtpNbrLocSlot": vrtpNbrLocSlot,
       "vrtpNbrLocLine": vrtpNbrLocLine,
       "vrtpNbrSvrName": vrtpNbrSvrName,
       "vrtpRtNumber": vrtpRtNumber,
       "vrtpRtTable": vrtpRtTable,
       "vrtpRtEntry": vrtpRtEntry,
       "vrtpRtNetid": vrtpRtNetid,
       "vrtpRtMetric": vrtpRtMetric,
       "vrtpRtIdle": vrtpRtIdle,
       "vrtpRtGateNetid": vrtpRtGateNetid,
       "vrtpRtSvrName": vrtpRtSvrName,
       "vrtpRtGateSvrName": vrtpRtGateSvrName,
       "vrtpTotIn": vrtpTotIn,
       "vrtpTotOut": vrtpTotOut,
       "vrtpErrsIn": vrtpErrsIn,
       "vrtpNoBuffersIn": vrtpNoBuffersIn,
       "vrtpUpdatesIn": vrtpUpdatesIn,
       "vrtpResponsesIn": vrtpResponsesIn,
       "vrtpRqstsIn": vrtpRqstsIn,
       "vrtpRqstLkUpIn": vrtpRqstLkUpIn,
       "vrtpRqstSlrInfoIn": vrtpRqstSlrInfoIn,
       "vrtpReinitIn": vrtpReinitIn,
       "vrtpResyncIn": vrtpResyncIn,
       "vrtpRedirIn": vrtpRedirIn,
       "vrtpFragsIn": vrtpFragsIn,
       "vrtpFragsDropIn": vrtpFragsDropIn,
       "vrtpFragsBadIn": vrtpFragsBadIn,
       "vrtpFragsDupIn": vrtpFragsDupIn,
       "vrtpFragsDoneIn": vrtpFragsDoneIn,
       "vrtpReassBadIn": vrtpReassBadIn,
       "vrtpOutdatedIn": vrtpOutdatedIn,
       "vrtpNetInfoBad": vrtpNetInfoBad,
       "vrtpBadRdrs": vrtpBadRdrs,
       "vrtpBdcstIn": vrtpBdcstIn,
       "vrtpNoBuffersOut": vrtpNoBuffersOut,
       "vrtpUpdatesOut": vrtpUpdatesOut,
       "vrtpRqstLkUpOut": vrtpRqstLkUpOut,
       "vrtpRqstSlrInfoOut": vrtpRqstSlrInfoOut,
       "vrtpRqstsOut": vrtpRqstsOut,
       "vrtpReinitOut": vrtpReinitOut,
       "vrtpResyncOut": vrtpResyncOut,
       "vrtpRedirOut": vrtpRedirOut,
       "vrtpFragsOut": vrtpFragsOut,
       "vrtpFragsDoneOut": vrtpFragsDoneOut,
       "vrtpFragsBadOut": vrtpFragsBadOut,
       "vrtpFragsDropOut": vrtpFragsDropOut,
       "vrtpBdcstOut": vrtpBdcstOut,
       "vrtpRtCr": vrtpRtCr,
       "vrtpRtMod": vrtpRtMod,
       "vrtpNbrAnchors": vrtpNbrAnchors,
       "vrtpNbrEntries": vrtpNbrEntries,
       "vrtpNetEntries": vrtpNetEntries,
       "vrtpLkUp": vrtpLkUp,
       "vrtpBadLkUp": vrtpBadLkUp,
       "vrtpNonSeqTotIn": vrtpNonSeqTotIn,
       "vrtpNonSeqTotOut": vrtpNonSeqTotOut,
       "vrtpNonSeqErrsIn": vrtpNonSeqErrsIn,
       "vrtpNonSeqUpdIn": vrtpNonSeqUpdIn,
       "vrtpNonSeqRspIn": vrtpNonSeqRspIn,
       "vrtpNonSeqRqstIn": vrtpNonSeqRqstIn,
       "vrtpNonSeqRdrIn": vrtpNonSeqRdrIn,
       "vrtpBadNonSeqRdrIn": vrtpBadNonSeqRdrIn,
       "vrtpNonSeqBdcstIn": vrtpNonSeqBdcstIn,
       "vrtpNonSeqUpdOut": vrtpNonSeqUpdOut,
       "vrtpNonSeqRspOut": vrtpNonSeqRspOut,
       "vrtpNonSeqRqstOut": vrtpNonSeqRqstOut,
       "vrtpNonSeqRdrOut": vrtpNonSeqRdrOut,
       "vrtpNonSeqBdcstOut": vrtpNonSeqBdcstOut,
       "vrtpResponsesOut": vrtpResponsesOut,
       "vspp": vspp,
       "vsppConnsInUse": vsppConnsInUse,
       "vsppConnsCfg": vsppConnsCfg,
       "vsppMaxConns": vsppMaxConns,
       "vsppTotIn": vsppTotIn,
       "vsppTotOut": vsppTotOut,
       "vsppInErrs": vsppInErrs,
       "vsppBadType": vsppBadType,
       "vsppNoBuffers": vsppNoBuffers,
       "vsppNoPort": vsppNoPort,
       "vsppDups": vsppDups,
       "vsppBadOrder": vsppBadOrder,
       "vsppDataIn": vsppDataIn,
       "vsppAcksIn": vsppAcksIn,
       "vsppDiscIn": vsppDiscIn,
       "vsppProbesIn": vsppProbesIn,
       "vsppDataOut": vsppDataOut,
       "vsppAcksOut": vsppAcksOut,
       "vsppDiscOut": vsppDiscOut,
       "vsppProbesOut": vsppProbesOut,
       "vsppAbortsOut": vsppAbortsOut,
       "vsppLocal": vsppLocal,
       "vinterfaces": vinterfaces,
       "vifNumber": vifNumber,
       "vifTable": vifTable,
       "vifEntry": vifEntry,
       "vifSlot": vifSlot,
       "vifType": vifType,
       "vifDescr": vifDescr,
       "vifAddress": vifAddress,
       "vifInPkts": vifInPkts,
       "vifInErrs": vifInErrs,
       "vifOutPkts": vifOutPkts,
       "vifOutErrs": vifOutErrs,
       "vifLnkNumber": vifLnkNumber,
       "vifLnkTable": vifLnkTable,
       "vifLnkEntry": vifLnkEntry,
       "vifLnkSlot": vifLnkSlot,
       "vifLnkLine": vifLnkLine,
       "vifLnkType": vifLnkType,
       "vifLnkTotIn": vifLnkTotIn,
       "vifLnkTotOut": vifLnkTotOut,
       "vifLnkRetrans": vifLnkRetrans,
       "vifLnkCRCErrs": vifLnkCRCErrs,
       "vifLnkDrops": vifLnkDrops,
       "vifLnkUnders": vifLnkUnders,
       "vifLnkOvers": vifLnkOvers,
       "vifLnkFrmErrs": vifLnkFrmErrs,
       "vifX25VCNumber": vifX25VCNumber,
       "vifX25VCTable": vifX25VCTable,
       "vifX25VCEntry": vifX25VCEntry,
       "vifX25VCSlot": vifX25VCSlot,
       "vifX25VCLine": vifX25VCLine,
       "vifX25VCSession": vifX25VCSession,
       "vifX25VCTotIn": vifX25VCTotIn,
       "vifX25VCTotOut": vifX25VCTotOut,
       "vifX25VCInErrs": vifX25VCInErrs,
       "vifX25VCOutErrs": vifX25VCOutErrs,
       "vifX25VCPktsOut": vifX25VCPktsOut,
       "vifX25VCPktsAwaitAck": vifX25VCPktsAwaitAck,
       "vifX25VCBytesOut": vifX25VCBytesOut,
       "vifX25VCBytesAwaitAck": vifX25VCBytesAwaitAck,
       "vifX25VCPktsIn": vifX25VCPktsIn,
       "vifX25VCBytesIn": vifX25VCBytesIn,
       "vifX25VCResetsIn": vifX25VCResetsIn,
       "vifX25VCResetsOut": vifX25VCResetsOut,
       "vifX25VCLogChnNum": vifX25VCLogChnNum,
       "vifX25VCRemAddr": vifX25VCRemAddr,
       "vifStatsList": vifStatsList,
       "vifStatEntry": vifStatEntry,
       "vifStatSlot": vifStatSlot,
       "vifStatIndex": vifStatIndex,
       "vifStatDescr": vifStatDescr,
       "vifStatValue": vifStatValue,
       "os": os,
       "ossysstats": ossysstats,
       "oscpuNum": oscpuNum,
       "oscpuTable": oscpuTable,
       "oscpuEntry": oscpuEntry,
       "cpuIndex": cpuIndex,
       "cpuIdleUsage": cpuIdleUsage,
       "cpuUserUsage": cpuUserUsage,
       "cpuSysUsage": cpuSysUsage,
       "cpuWIOUserUsage": cpuWIOUserUsage,
       "cpuProcSwappedOut": cpuProcSwappedOut,
       "cpuWIOUsage": cpuWIOUsage,
       "cpuWSUsage": cpuWSUsage,
       "cpuWPIOUsage": cpuWPIOUsage,
       "osBReads": osBReads,
       "osBWrites": osBWrites,
       "osLReads": osLReads,
       "osLWrites": osLWrites,
       "osPReads": osPReads,
       "osPWrites": osPWrites,
       "osInSwaps": osInSwaps,
       "osOutSwaps": osOutSwaps,
       "osInBSwaps": osInBSwaps,
       "osOutBSwaps": osOutBSwaps,
       "osProcessSwitches": osProcessSwitches,
       "osSystemCalls": osSystemCalls,
       "osSystemRead": osSystemRead,
       "osSystemWrite": osSystemWrite,
       "osSystemFork": osSystemFork,
       "osSystemExec": osSystemExec,
       "osRunQueue": osRunQueue,
       "osRunQueueOcc": osRunQueueOcc,
       "osSwapQueueTotals": osSwapQueueTotals,
       "osSwapQueueOcc": osSwapQueueOcc,
       "osIPCMsgOps": osIPCMsgOps,
       "osSemOps": osSemOps,
       "osPnpFault": osPnpFault,
       "osWrtFault": osWrtFault,
       "osCurrentInodes": osCurrentInodes,
       "osHWInodes": osHWInodes,
       "osCurrentFiles": osCurrentFiles,
       "osHWFiles": osHWFiles,
       "osinfo": osinfo,
       "osMaxInodes": osMaxInodes,
       "osMaxFiles": osMaxFiles,
       "osMaxProcesses": osMaxProcesses,
       "osSwapSpaceAvailable": osSwapSpaceAvailable,
       "osFreeMemoryTotal": osFreeMemoryTotal,
       "osIOBufs": osIOBufs,
       "osMounts": osMounts,
       "osUserMaxPu": osUserMaxPu,
       "osUserMaxFp": osUserMaxFp,
       "ossummstats": ossummstats,
       "osCurrentProcesses": osCurrentProcesses,
       "osSwapSpaceUsed": osSwapSpaceUsed,
       "osFreeMemoryAvailable": osFreeMemoryAvailable,
       "osUserUsagePct": osUserUsagePct,
       "osSysUsagePct": osSysUsagePct,
       "osWIOUsagePct": osWIOUsagePct,
       "osIdleUsagePct": osIdleUsagePct,
       "osRunOccPct": osRunOccPct,
       "osSwapOccPct": osSwapOccPct,
       "osBuffRdRate": osBuffRdRate,
       "osRdCachePct": osRdCachePct,
       "osBuffWrRate": osBuffWrRate,
       "osWrCachePct": osWrCachePct,
       "osBswpInRate": osBswpInRate,
       "osBswpOutRate": osBswpOutRate,
       "osVfltRate": osVfltRate,
       "osSwitchRate": osSwitchRate,
       "osSysCallRate": osSysCallRate,
       "nmthresholds": nmthresholds,
       "nmLoadAvg15HighThres": nmLoadAvg15HighThres,
       "nmSockInUseHighThres": nmSockInUseHighThres,
       "nmDiskUseHighThres": nmDiskUseHighThres,
       "nmSwapAvgHighThres": nmSwapAvgHighThres,
       "nmDropsHighThres": nmDropsHighThres,
       "nmSwapSpaceLowThres": nmSwapSpaceLowThres,
       "nmFreeMemLowThres": nmFreeMemLowThres,
       "nmCommBuffHighThres": nmCommBuffHighThres,
       "nmAllocFailHighThres": nmAllocFailHighThres,
       "nmCacheHitsLowThres": nmCacheHitsLowThres,
       "nmDiskBusyHighThres": nmDiskBusyHighThres,
       "nmMsgAvgHighThres": nmMsgAvgHighThres,
       "nmInodeUseHighThres": nmInodeUseHighThres,
       "trapdata": trapdata,
       "tpAlertTime": tpAlertTime,
       "tpErrorCode": tpErrorCode,
       "tpUserName": tpUserName,
       "tpSvcName": tpSvcName,
       "tpSvrName": tpSvrName,
       "tpRefSvcName": tpRefSvcName,
       "tpRefSvrName": tpRefSvrName,
       "tpJobId": tpJobId,
       "tpPaperFormat": tpPaperFormat,
       "tpJobTotal": tpJobTotal,
       "tpConnId": tpConnId,
       "tpMailSender": tpMailSender,
       "tpPortId": tpPortId,
       "tpRtnName": tpRtnName,
       "tp162erravg": tp162erravg,
       "tp162errThresHigh": tp162errThresHigh,
       "tp162errTotal": tp162errTotal,
       "tpGrpName": tpGrpName,
       "tpNumGrps": tpNumGrps,
       "tpGrpLimit": tpGrpLimit,
       "tpOldSerNum": tpOldSerNum,
       "tpNewSerNum": tpNewSerNum,
       "tpDiskSpaceLeft": tpDiskSpaceLeft,
       "tpMailMessageId": tpMailMessageId,
       "tpSockOvFlowNum": tpSockOvFlowNum,
       "tpDiskNName": tpDiskNName,
       "tpSvrNetId": tpSvrNetId,
       "tpSubNetId": tpSubNetId,
       "tpSlotNum": tpSlotNum,
       "tpLineNum": tpLineNum,
       "tpFRcvd": tpFRcvd,
       "tpFXmtd": tpFXmtd,
       "tpLnkDropsThres": tpLnkDropsThres,
       "tpLnkReXtThres": tpLnkReXtThres,
       "ams": ams,
       "amsRegTable": amsRegTable,
       "amsRegEntry": amsRegEntry,
       "amsRegIndex": amsRegIndex,
       "amsRegIdInstance": amsRegIdInstance,
       "amsRegIdClass": amsRegIdClass,
       "amsRegIdTid": amsRegIdTid,
       "amsRegPort": amsRegPort,
       "amsRegWhoAdded": amsRegWhoAdded,
       "amsRegAlertee": amsRegAlertee,
       "amsRegAction": amsRegAction,
       "amsAlertLogTable": amsAlertLogTable,
       "amsLogEntry": amsLogEntry,
       "amsLogFileIndex": amsLogFileIndex,
       "amsLogRecIndex": amsLogRecIndex,
       "amsLogIdInstance": amsLogIdInstance,
       "amsLogIdClass": amsLogIdClass,
       "amsLogIdTid": amsLogIdTid,
       "amsLogAlertTime": amsLogAlertTime,
       "amsLogAlertString": amsLogAlertString,
       "mailservice": mailservice,
       "mlMailBoxTable": mlMailBoxTable,
       "mlMailBoxTableEntry": mlMailBoxTableEntry,
       "mlMBTableIndex": mlMBTableIndex,
       "mlMBTableMBOwner": mlMBTableMBOwner,
       "mlMBTableUnreadMsgs": mlMBTableUnreadMsgs,
       "mlMBTableTotalMsgs": mlMBTableTotalMsgs,
       "vlogs": vlogs,
       "vlogsTable": vlogsTable,
       "vlogsEntry": vlogsEntry,
       "vlogsFileIndex": vlogsFileIndex,
       "vlogsDescr": vlogsDescr}
)
