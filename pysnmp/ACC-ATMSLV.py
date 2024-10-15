# SNMP MIB module (ACC-ATMSLV) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ATMSLV
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:50 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accSysInfo,
 accTrapLogSeqNum) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accSysInfo",
    "accTrapLogSeqNum")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccVWSlvGrp_ObjectIdentity = ObjectIdentity
accVWSlvGrp = _AccVWSlvGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31)
)
_AccVWSlvConfTable_Object = MibTable
accVWSlvConfTable = _AccVWSlvConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    accVWSlvConfTable.setStatus("mandatory")
_AccVWSlvConfEntry_Object = MibTableRow
accVWSlvConfEntry = _AccVWSlvConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1)
)
accVWSlvConfEntry.setIndexNames(
    (0, "ACC-ATMSLV", "accVWSlvConfCPUID"),
)
if mibBuilder.loadTexts:
    accVWSlvConfEntry.setStatus("mandatory")
_AccVWSlvConfCPUID_Type = DisplayString
_AccVWSlvConfCPUID_Object = MibTableColumn
accVWSlvConfCPUID = _AccVWSlvConfCPUID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1, 1),
    _AccVWSlvConfCPUID_Type()
)
accVWSlvConfCPUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvConfCPUID.setStatus("mandatory")
_AccVWSlvConfSysDesc_Type = DisplayString
_AccVWSlvConfSysDesc_Object = MibTableColumn
accVWSlvConfSysDesc = _AccVWSlvConfSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1, 2),
    _AccVWSlvConfSysDesc_Type()
)
accVWSlvConfSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvConfSysDesc.setStatus("mandatory")
_AccVWSlvConfSWVers_Type = DisplayString
_AccVWSlvConfSWVers_Object = MibTableColumn
accVWSlvConfSWVers = _AccVWSlvConfSWVers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1, 3),
    _AccVWSlvConfSWVers_Type()
)
accVWSlvConfSWVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvConfSWVers.setStatus("mandatory")


class _AccVWSlvConfProcType_Type(Integer32):
    """Custom type accVWSlvConfProcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("idtMips4700", 1)
    )


_AccVWSlvConfProcType_Type.__name__ = "Integer32"
_AccVWSlvConfProcType_Object = MibTableColumn
accVWSlvConfProcType = _AccVWSlvConfProcType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1, 4),
    _AccVWSlvConfProcType_Type()
)
accVWSlvConfProcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvConfProcType.setStatus("mandatory")
_AccVWSlvConfLocalRam_Type = Integer32
_AccVWSlvConfLocalRam_Object = MibTableColumn
accVWSlvConfLocalRam = _AccVWSlvConfLocalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1, 5),
    _AccVWSlvConfLocalRam_Type()
)
accVWSlvConfLocalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvConfLocalRam.setStatus("mandatory")
_AccVWSlvConfGlobalRam_Type = Integer32
_AccVWSlvConfGlobalRam_Object = MibTableColumn
accVWSlvConfGlobalRam = _AccVWSlvConfGlobalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1, 6),
    _AccVWSlvConfGlobalRam_Type()
)
accVWSlvConfGlobalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvConfGlobalRam.setStatus("mandatory")
_AccVWSlvConfHWVers_Type = DisplayString
_AccVWSlvConfHWVers_Object = MibTableColumn
accVWSlvConfHWVers = _AccVWSlvConfHWVers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 1, 1, 7),
    _AccVWSlvConfHWVers_Type()
)
accVWSlvConfHWVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvConfHWVers.setStatus("mandatory")
_AccVWSlvMemStatTable_Object = MibTable
accVWSlvMemStatTable = _AccVWSlvMemStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2)
)
if mibBuilder.loadTexts:
    accVWSlvMemStatTable.setStatus("mandatory")
_AccVWSlvMemStatEntry_Object = MibTableRow
accVWSlvMemStatEntry = _AccVWSlvMemStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1)
)
accVWSlvMemStatEntry.setIndexNames(
    (0, "ACC-ATMSLV", "accVWSlvMemCPUID"),
    (0, "ACC-ATMSLV", "accVWSlvMemBlkPoolId"),
)
if mibBuilder.loadTexts:
    accVWSlvMemStatEntry.setStatus("mandatory")
_AccVWSlvMemCPUID_Type = DisplayString
_AccVWSlvMemCPUID_Object = MibTableColumn
accVWSlvMemCPUID = _AccVWSlvMemCPUID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1, 1),
    _AccVWSlvMemCPUID_Type()
)
accVWSlvMemCPUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvMemCPUID.setStatus("mandatory")


class _AccVWSlvMemBlkPoolId_Type(Integer32):
    """Custom type accVWSlvMemBlkPoolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_AccVWSlvMemBlkPoolId_Type.__name__ = "Integer32"
_AccVWSlvMemBlkPoolId_Object = MibTableColumn
accVWSlvMemBlkPoolId = _AccVWSlvMemBlkPoolId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1, 2),
    _AccVWSlvMemBlkPoolId_Type()
)
accVWSlvMemBlkPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvMemBlkPoolId.setStatus("mandatory")
_AccVWSlvMemBlkEntSize_Type = Integer32
_AccVWSlvMemBlkEntSize_Object = MibTableColumn
accVWSlvMemBlkEntSize = _AccVWSlvMemBlkEntSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1, 3),
    _AccVWSlvMemBlkEntSize_Type()
)
accVWSlvMemBlkEntSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvMemBlkEntSize.setStatus("mandatory")
_AccVWSlvMemBlkEntTotal_Type = Integer32
_AccVWSlvMemBlkEntTotal_Object = MibTableColumn
accVWSlvMemBlkEntTotal = _AccVWSlvMemBlkEntTotal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1, 4),
    _AccVWSlvMemBlkEntTotal_Type()
)
accVWSlvMemBlkEntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvMemBlkEntTotal.setStatus("mandatory")
_AccVWSlvMemBlkEntInUse_Type = Gauge32
_AccVWSlvMemBlkEntInUse_Object = MibTableColumn
accVWSlvMemBlkEntInUse = _AccVWSlvMemBlkEntInUse_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1, 5),
    _AccVWSlvMemBlkEntInUse_Type()
)
accVWSlvMemBlkEntInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvMemBlkEntInUse.setStatus("mandatory")
_AccVWSlvMemBlkEntFails_Type = Counter32
_AccVWSlvMemBlkEntFails_Object = MibTableColumn
accVWSlvMemBlkEntFails = _AccVWSlvMemBlkEntFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1, 6),
    _AccVWSlvMemBlkEntFails_Type()
)
accVWSlvMemBlkEntFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvMemBlkEntFails.setStatus("mandatory")
_AccVWSlvMemBlkEntAllocs_Type = Counter32
_AccVWSlvMemBlkEntAllocs_Object = MibTableColumn
accVWSlvMemBlkEntAllocs = _AccVWSlvMemBlkEntAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 2, 1, 7),
    _AccVWSlvMemBlkEntAllocs_Type()
)
accVWSlvMemBlkEntAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvMemBlkEntAllocs.setStatus("mandatory")
_AccVWSlvTimeTable_Object = MibTable
accVWSlvTimeTable = _AccVWSlvTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 3)
)
if mibBuilder.loadTexts:
    accVWSlvTimeTable.setStatus("mandatory")
_AccVWSlvTimeEntry_Object = MibTableRow
accVWSlvTimeEntry = _AccVWSlvTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 3, 1)
)
accVWSlvTimeEntry.setIndexNames(
    (0, "ACC-ATMSLV", "accVWSlvSysCPUID"),
)
if mibBuilder.loadTexts:
    accVWSlvTimeEntry.setStatus("mandatory")
_AccVWSlvSysCPUID_Type = DisplayString
_AccVWSlvSysCPUID_Object = MibTableColumn
accVWSlvSysCPUID = _AccVWSlvSysCPUID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 3, 1, 1),
    _AccVWSlvSysCPUID_Type()
)
accVWSlvSysCPUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvSysCPUID.setStatus("mandatory")
_AccVWSlvSysUpTime_Type = TimeTicks
_AccVWSlvSysUpTime_Object = MibTableColumn
accVWSlvSysUpTime = _AccVWSlvSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 3, 1, 2),
    _AccVWSlvSysUpTime_Type()
)
accVWSlvSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvSysUpTime.setStatus("mandatory")
_AccVWSlvSysCpuAvgShort_Type = Integer32
_AccVWSlvSysCpuAvgShort_Object = MibTableColumn
accVWSlvSysCpuAvgShort = _AccVWSlvSysCpuAvgShort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 3, 1, 3),
    _AccVWSlvSysCpuAvgShort_Type()
)
accVWSlvSysCpuAvgShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvSysCpuAvgShort.setStatus("mandatory")
_AccVWSlvSysCpuAvgLong_Type = Integer32
_AccVWSlvSysCpuAvgLong_Object = MibTableColumn
accVWSlvSysCpuAvgLong = _AccVWSlvSysCpuAvgLong_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 31, 3, 1, 4),
    _AccVWSlvSysCpuAvgLong_Type()
)
accVWSlvSysCpuAvgLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accVWSlvSysCpuAvgLong.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ATMSLV",
    **{"accVWSlvGrp": accVWSlvGrp,
       "accVWSlvConfTable": accVWSlvConfTable,
       "accVWSlvConfEntry": accVWSlvConfEntry,
       "accVWSlvConfCPUID": accVWSlvConfCPUID,
       "accVWSlvConfSysDesc": accVWSlvConfSysDesc,
       "accVWSlvConfSWVers": accVWSlvConfSWVers,
       "accVWSlvConfProcType": accVWSlvConfProcType,
       "accVWSlvConfLocalRam": accVWSlvConfLocalRam,
       "accVWSlvConfGlobalRam": accVWSlvConfGlobalRam,
       "accVWSlvConfHWVers": accVWSlvConfHWVers,
       "accVWSlvMemStatTable": accVWSlvMemStatTable,
       "accVWSlvMemStatEntry": accVWSlvMemStatEntry,
       "accVWSlvMemCPUID": accVWSlvMemCPUID,
       "accVWSlvMemBlkPoolId": accVWSlvMemBlkPoolId,
       "accVWSlvMemBlkEntSize": accVWSlvMemBlkEntSize,
       "accVWSlvMemBlkEntTotal": accVWSlvMemBlkEntTotal,
       "accVWSlvMemBlkEntInUse": accVWSlvMemBlkEntInUse,
       "accVWSlvMemBlkEntFails": accVWSlvMemBlkEntFails,
       "accVWSlvMemBlkEntAllocs": accVWSlvMemBlkEntAllocs,
       "accVWSlvTimeTable": accVWSlvTimeTable,
       "accVWSlvTimeEntry": accVWSlvTimeEntry,
       "accVWSlvSysCPUID": accVWSlvSysCPUID,
       "accVWSlvSysUpTime": accVWSlvSysUpTime,
       "accVWSlvSysCpuAvgShort": accVWSlvSysCpuAvgShort,
       "accVWSlvSysCpuAvgLong": accVWSlvSysCpuAvgLong}
)
