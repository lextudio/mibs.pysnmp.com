# SNMP MIB module (WS-INFRA-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:26 2024
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

(wsInfraDiag,) = mibBuilder.importSymbols(
    "WS-INFRA-SMI-MIB",
    "wsInfraDiag")


# MODULE-IDENTITY

wsInfraDiagMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1)
)
wsInfraDiagMib.setRevisions(
        ("2006-06-06 10:31",
         "2006-04-05 13:30",
         "2006-01-05 17:55",
         "2005-12-01 16:30",
         "2005-05-19 15:37",
         "2005-05-18 16:54")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraDiagTempControl_ObjectIdentity = ObjectIdentity
wsInfraDiagTempControl = _WsInfraDiagTempControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 1)
)


class _WsInfraDiagTempCurrentTemp_Type(Integer32):
    """Custom type wsInfraDiagTempCurrentTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 450),
        ValueRangeConstraint(1000, 1000),
    )


_WsInfraDiagTempCurrentTemp_Type.__name__ = "Integer32"
_WsInfraDiagTempCurrentTemp_Object = MibScalar
wsInfraDiagTempCurrentTemp = _WsInfraDiagTempCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 1, 1),
    _WsInfraDiagTempCurrentTemp_Type()
)
wsInfraDiagTempCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagTempCurrentTemp.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsInfraDiagTempCurrentTemp.setUnits("0.1C")


class _WsInfraDiagTempHighTemp_Type(Integer32):
    """Custom type wsInfraDiagTempHighTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 450),
        ValueRangeConstraint(1000, 1001),
    )


_WsInfraDiagTempHighTemp_Type.__name__ = "Integer32"
_WsInfraDiagTempHighTemp_Object = MibScalar
wsInfraDiagTempHighTemp = _WsInfraDiagTempHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 1, 2),
    _WsInfraDiagTempHighTemp_Type()
)
wsInfraDiagTempHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagTempHighTemp.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsInfraDiagTempHighTemp.setUnits("0.1C")


class _WsInfraDiagTempHighTempHysteresis_Type(Integer32):
    """Custom type wsInfraDiagTempHighTempHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsInfraDiagTempHighTempHysteresis_Type.__name__ = "Integer32"
_WsInfraDiagTempHighTempHysteresis_Object = MibScalar
wsInfraDiagTempHighTempHysteresis = _WsInfraDiagTempHighTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 1, 3),
    _WsInfraDiagTempHighTempHysteresis_Type()
)
wsInfraDiagTempHighTempHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagTempHighTempHysteresis.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsInfraDiagTempHighTempHysteresis.setUnits("0.1C")
_WsInfraDiagFanControl_ObjectIdentity = ObjectIdentity
wsInfraDiagFanControl = _WsInfraDiagFanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 2)
)


class _WsInfraDiagSysFanSpeed_Type(Integer32):
    """Custom type wsInfraDiagSysFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WsInfraDiagSysFanSpeed_Type.__name__ = "Integer32"
_WsInfraDiagSysFanSpeed_Object = MibScalar
wsInfraDiagSysFanSpeed = _WsInfraDiagSysFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 2, 1),
    _WsInfraDiagSysFanSpeed_Type()
)
wsInfraDiagSysFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagSysFanSpeed.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsInfraDiagSysFanSpeed.setUnits("1 rpm")


class _WsDiagProcFanSpeed_Type(Integer32):
    """Custom type wsDiagProcFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WsDiagProcFanSpeed_Type.__name__ = "Integer32"
_WsDiagProcFanSpeed_Object = MibScalar
wsDiagProcFanSpeed = _WsDiagProcFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 2, 2),
    _WsDiagProcFanSpeed_Type()
)
wsDiagProcFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsDiagProcFanSpeed.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsDiagProcFanSpeed.setUnits("1 rpm")
_WsInfraHwBuildInfo_ObjectIdentity = ObjectIdentity
wsInfraHwBuildInfo = _WsInfraHwBuildInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3)
)


class _WsInfraHwTotalNum_Type(Integer32):
    """Custom type wsInfraHwTotalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WsInfraHwTotalNum_Type.__name__ = "Integer32"
_WsInfraHwTotalNum_Object = MibScalar
wsInfraHwTotalNum = _WsInfraHwTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 1),
    _WsInfraHwTotalNum_Type()
)
wsInfraHwTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraHwTotalNum.setStatus("obsolete")
_WsInfraHwBuildInfoTable_Object = MibTable
wsInfraHwBuildInfoTable = _WsInfraHwBuildInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wsInfraHwBuildInfoTable.setStatus("current")
_WsInfraHwBuildInfoEntry_Object = MibTableRow
wsInfraHwBuildInfoEntry = _WsInfraHwBuildInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 2, 1)
)
wsInfraHwBuildInfoEntry.setIndexNames(
    (0, "WS-INFRA-DIAG-MIB", "wsInfraHwBuildInfoModuleIndex"),
)
if mibBuilder.loadTexts:
    wsInfraHwBuildInfoEntry.setStatus("current")


class _WsInfraHwBuildInfoModuleIndex_Type(Integer32):
    """Custom type wsInfraHwBuildInfoModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WsInfraHwBuildInfoModuleIndex_Type.__name__ = "Integer32"
_WsInfraHwBuildInfoModuleIndex_Object = MibTableColumn
wsInfraHwBuildInfoModuleIndex = _WsInfraHwBuildInfoModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 2, 1, 1),
    _WsInfraHwBuildInfoModuleIndex_Type()
)
wsInfraHwBuildInfoModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsInfraHwBuildInfoModuleIndex.setStatus("current")
_WsInfraHwBuildInfoModuleName_Type = DisplayString
_WsInfraHwBuildInfoModuleName_Object = MibTableColumn
wsInfraHwBuildInfoModuleName = _WsInfraHwBuildInfoModuleName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 2, 1, 2),
    _WsInfraHwBuildInfoModuleName_Type()
)
wsInfraHwBuildInfoModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraHwBuildInfoModuleName.setStatus("current")
_WsInfraHwBuildInfoVersion_Type = DisplayString
_WsInfraHwBuildInfoVersion_Object = MibTableColumn
wsInfraHwBuildInfoVersion = _WsInfraHwBuildInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 2, 1, 3),
    _WsInfraHwBuildInfoVersion_Type()
)
wsInfraHwBuildInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraHwBuildInfoVersion.setStatus("current")
_WsInfraHwBuildInfoManufacturer_Type = DisplayString
_WsInfraHwBuildInfoManufacturer_Object = MibTableColumn
wsInfraHwBuildInfoManufacturer = _WsInfraHwBuildInfoManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 2, 1, 4),
    _WsInfraHwBuildInfoManufacturer_Type()
)
wsInfraHwBuildInfoManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraHwBuildInfoManufacturer.setStatus("current")
_WsInfraHwBuildInfoDesc_Type = DisplayString
_WsInfraHwBuildInfoDesc_Object = MibTableColumn
wsInfraHwBuildInfoDesc = _WsInfraHwBuildInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 3, 2, 1, 5),
    _WsInfraHwBuildInfoDesc_Type()
)
wsInfraHwBuildInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraHwBuildInfoDesc.setStatus("current")
_WsInfraResStats_ObjectIdentity = ObjectIdentity
wsInfraResStats = _WsInfraResStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4)
)


class _WsInfraResCpuLoad1_Type(Integer32):
    """Custom type wsInfraResCpuLoad1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraResCpuLoad1_Type.__name__ = "Integer32"
_WsInfraResCpuLoad1_Object = MibScalar
wsInfraResCpuLoad1 = _WsInfraResCpuLoad1_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 1),
    _WsInfraResCpuLoad1_Type()
)
wsInfraResCpuLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad1.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad1.setUnits("%")


class _WsInfraResCpuLoad5_Type(Integer32):
    """Custom type wsInfraResCpuLoad5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraResCpuLoad5_Type.__name__ = "Integer32"
_WsInfraResCpuLoad5_Object = MibScalar
wsInfraResCpuLoad5 = _WsInfraResCpuLoad5_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 2),
    _WsInfraResCpuLoad5_Type()
)
wsInfraResCpuLoad5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad5.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad5.setUnits("%")


class _WsInfraResCpuLoad15_Type(Integer32):
    """Custom type wsInfraResCpuLoad15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraResCpuLoad15_Type.__name__ = "Integer32"
_WsInfraResCpuLoad15_Object = MibScalar
wsInfraResCpuLoad15 = _WsInfraResCpuLoad15_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 3),
    _WsInfraResCpuLoad15_Type()
)
wsInfraResCpuLoad15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad15.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad15.setUnits("%")
_WsInfraFreeMemory_Type = Unsigned32
_WsInfraFreeMemory_Object = MibScalar
wsInfraFreeMemory = _WsInfraFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 4),
    _WsInfraFreeMemory_Type()
)
wsInfraFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFreeMemory.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsInfraFreeMemory.setUnits("KB")
_WsInfraRootFSFree_Type = Unsigned32
_WsInfraRootFSFree_Object = MibScalar
wsInfraRootFSFree = _WsInfraRootFSFree_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 5),
    _WsInfraRootFSFree_Type()
)
wsInfraRootFSFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraRootFSFree.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsInfraRootFSFree.setUnits("KB")
_WsInfraRootFSInodesFree_Type = Unsigned32
_WsInfraRootFSInodesFree_Object = MibScalar
wsInfraRootFSInodesFree = _WsInfraRootFSInodesFree_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 6),
    _WsInfraRootFSInodesFree_Type()
)
wsInfraRootFSInodesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraRootFSInodesFree.setStatus("obsolete")
_WsInfraRamFSFree_Type = Unsigned32
_WsInfraRamFSFree_Object = MibScalar
wsInfraRamFSFree = _WsInfraRamFSFree_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 7),
    _WsInfraRamFSFree_Type()
)
wsInfraRamFSFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraRamFSFree.setStatus("obsolete")
if mibBuilder.loadTexts:
    wsInfraRamFSFree.setUnits("KB")
_WsInfraRamFSInodesFree_Type = Unsigned32
_WsInfraRamFSInodesFree_Object = MibScalar
wsInfraRamFSInodesFree = _WsInfraRamFSInodesFree_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 8),
    _WsInfraRamFSInodesFree_Type()
)
wsInfraRamFSInodesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraRamFSInodesFree.setStatus("obsolete")
_WsInfraFreeFileDesc_Type = Unsigned32
_WsInfraFreeFileDesc_Object = MibScalar
wsInfraFreeFileDesc = _WsInfraFreeFileDesc_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 9),
    _WsInfraFreeFileDesc_Type()
)
wsInfraFreeFileDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFreeFileDesc.setStatus("obsolete")
_WsInfraUsedKernBuff32_Type = Unsigned32
_WsInfraUsedKernBuff32_Object = MibScalar
wsInfraUsedKernBuff32 = _WsInfraUsedKernBuff32_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 10),
    _WsInfraUsedKernBuff32_Type()
)
wsInfraUsedKernBuff32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff32.setStatus("current")
_WsInfraUsedKernBuff64_Type = Unsigned32
_WsInfraUsedKernBuff64_Object = MibScalar
wsInfraUsedKernBuff64 = _WsInfraUsedKernBuff64_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 11),
    _WsInfraUsedKernBuff64_Type()
)
wsInfraUsedKernBuff64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff64.setStatus("current")
_WsInfraUsedKernBuff128_Type = Unsigned32
_WsInfraUsedKernBuff128_Object = MibScalar
wsInfraUsedKernBuff128 = _WsInfraUsedKernBuff128_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 12),
    _WsInfraUsedKernBuff128_Type()
)
wsInfraUsedKernBuff128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff128.setStatus("current")
_WsInfraUsedKernBuff256_Type = Unsigned32
_WsInfraUsedKernBuff256_Object = MibScalar
wsInfraUsedKernBuff256 = _WsInfraUsedKernBuff256_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 13),
    _WsInfraUsedKernBuff256_Type()
)
wsInfraUsedKernBuff256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff256.setStatus("current")
_WsInfraUsedKernBuff512_Type = Unsigned32
_WsInfraUsedKernBuff512_Object = MibScalar
wsInfraUsedKernBuff512 = _WsInfraUsedKernBuff512_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 14),
    _WsInfraUsedKernBuff512_Type()
)
wsInfraUsedKernBuff512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff512.setStatus("current")
_WsInfraUsedKernBuff1024_Type = Unsigned32
_WsInfraUsedKernBuff1024_Object = MibScalar
wsInfraUsedKernBuff1024 = _WsInfraUsedKernBuff1024_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 15),
    _WsInfraUsedKernBuff1024_Type()
)
wsInfraUsedKernBuff1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff1024.setStatus("current")
_WsInfraUsedKernBuff2048_Type = Unsigned32
_WsInfraUsedKernBuff2048_Object = MibScalar
wsInfraUsedKernBuff2048 = _WsInfraUsedKernBuff2048_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 16),
    _WsInfraUsedKernBuff2048_Type()
)
wsInfraUsedKernBuff2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff2048.setStatus("current")
_WsInfraUsedKernBuff4096_Type = Unsigned32
_WsInfraUsedKernBuff4096_Object = MibScalar
wsInfraUsedKernBuff4096 = _WsInfraUsedKernBuff4096_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 17),
    _WsInfraUsedKernBuff4096_Type()
)
wsInfraUsedKernBuff4096.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff4096.setStatus("current")
_WsInfraUsedKernBuff8192_Type = Unsigned32
_WsInfraUsedKernBuff8192_Object = MibScalar
wsInfraUsedKernBuff8192 = _WsInfraUsedKernBuff8192_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 18),
    _WsInfraUsedKernBuff8192_Type()
)
wsInfraUsedKernBuff8192.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff8192.setStatus("current")
_WsInfraUsedKernBuff16384_Type = Unsigned32
_WsInfraUsedKernBuff16384_Object = MibScalar
wsInfraUsedKernBuff16384 = _WsInfraUsedKernBuff16384_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 19),
    _WsInfraUsedKernBuff16384_Type()
)
wsInfraUsedKernBuff16384.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff16384.setStatus("current")
_WsInfraUsedKernBuff32768_Type = Unsigned32
_WsInfraUsedKernBuff32768_Object = MibScalar
wsInfraUsedKernBuff32768 = _WsInfraUsedKernBuff32768_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 20),
    _WsInfraUsedKernBuff32768_Type()
)
wsInfraUsedKernBuff32768.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff32768.setStatus("current")
_WsInfraUsedKernBuff65536_Type = Unsigned32
_WsInfraUsedKernBuff65536_Object = MibScalar
wsInfraUsedKernBuff65536 = _WsInfraUsedKernBuff65536_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 21),
    _WsInfraUsedKernBuff65536_Type()
)
wsInfraUsedKernBuff65536.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff65536.setStatus("current")
_WsInfraUsedKernBuff131072_Type = Unsigned32
_WsInfraUsedKernBuff131072_Object = MibScalar
wsInfraUsedKernBuff131072 = _WsInfraUsedKernBuff131072_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 22),
    _WsInfraUsedKernBuff131072_Type()
)
wsInfraUsedKernBuff131072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff131072.setStatus("current")


class _WsInfraResCpuLoad1MinLimit_Type(Integer32):
    """Custom type wsInfraResCpuLoad1MinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraResCpuLoad1MinLimit_Type.__name__ = "Integer32"
_WsInfraResCpuLoad1MinLimit_Object = MibScalar
wsInfraResCpuLoad1MinLimit = _WsInfraResCpuLoad1MinLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 23),
    _WsInfraResCpuLoad1MinLimit_Type()
)
wsInfraResCpuLoad1MinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad1MinLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad1MinLimit.setUnits("%")


class _WsInfraResCpuLoad5MinLimit_Type(Integer32):
    """Custom type wsInfraResCpuLoad5MinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraResCpuLoad5MinLimit_Type.__name__ = "Integer32"
_WsInfraResCpuLoad5MinLimit_Object = MibScalar
wsInfraResCpuLoad5MinLimit = _WsInfraResCpuLoad5MinLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 24),
    _WsInfraResCpuLoad5MinLimit_Type()
)
wsInfraResCpuLoad5MinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad5MinLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad5MinLimit.setUnits("0.1%")


class _WsInfraResCpuLoad15MinLimit_Type(Integer32):
    """Custom type wsInfraResCpuLoad15MinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraResCpuLoad15MinLimit_Type.__name__ = "Integer32"
_WsInfraResCpuLoad15MinLimit_Object = MibScalar
wsInfraResCpuLoad15MinLimit = _WsInfraResCpuLoad15MinLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 25),
    _WsInfraResCpuLoad15MinLimit_Type()
)
wsInfraResCpuLoad15MinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad15MinLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraResCpuLoad15MinLimit.setUnits("0.1%")


class _WsInfraUsedKernBuff32Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff32Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff32Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff32Limit_Object = MibScalar
wsInfraUsedKernBuff32Limit = _WsInfraUsedKernBuff32Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 26),
    _WsInfraUsedKernBuff32Limit_Type()
)
wsInfraUsedKernBuff32Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff32Limit.setStatus("current")


class _WsInfraUsedKernBuff64Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff64Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff64Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff64Limit_Object = MibScalar
wsInfraUsedKernBuff64Limit = _WsInfraUsedKernBuff64Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 27),
    _WsInfraUsedKernBuff64Limit_Type()
)
wsInfraUsedKernBuff64Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff64Limit.setStatus("current")


class _WsInfraUsedKernBuff128Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff128Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff128Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff128Limit_Object = MibScalar
wsInfraUsedKernBuff128Limit = _WsInfraUsedKernBuff128Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 28),
    _WsInfraUsedKernBuff128Limit_Type()
)
wsInfraUsedKernBuff128Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff128Limit.setStatus("current")


class _WsInfraUsedKernBuff256Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff256Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff256Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff256Limit_Object = MibScalar
wsInfraUsedKernBuff256Limit = _WsInfraUsedKernBuff256Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 29),
    _WsInfraUsedKernBuff256Limit_Type()
)
wsInfraUsedKernBuff256Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff256Limit.setStatus("current")


class _WsInfraUsedKernBuff512Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff512Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff512Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff512Limit_Object = MibScalar
wsInfraUsedKernBuff512Limit = _WsInfraUsedKernBuff512Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 30),
    _WsInfraUsedKernBuff512Limit_Type()
)
wsInfraUsedKernBuff512Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff512Limit.setStatus("current")


class _WsInfraUsedKernBuff1024Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff1024Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff1024Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff1024Limit_Object = MibScalar
wsInfraUsedKernBuff1024Limit = _WsInfraUsedKernBuff1024Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 31),
    _WsInfraUsedKernBuff1024Limit_Type()
)
wsInfraUsedKernBuff1024Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff1024Limit.setStatus("current")


class _WsInfraUsedKernBuff2048Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff2048Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff2048Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff2048Limit_Object = MibScalar
wsInfraUsedKernBuff2048Limit = _WsInfraUsedKernBuff2048Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 32),
    _WsInfraUsedKernBuff2048Limit_Type()
)
wsInfraUsedKernBuff2048Limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff2048Limit.setStatus("current")


class _WsInfraUsedKernBuff4096Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff4096Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff4096Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff4096Limit_Object = MibScalar
wsInfraUsedKernBuff4096Limit = _WsInfraUsedKernBuff4096Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 33),
    _WsInfraUsedKernBuff4096Limit_Type()
)
wsInfraUsedKernBuff4096Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff4096Limit.setStatus("current")


class _WsInfraUsedKernBuff8192Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff8192Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff8192Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff8192Limit_Object = MibScalar
wsInfraUsedKernBuff8192Limit = _WsInfraUsedKernBuff8192Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 34),
    _WsInfraUsedKernBuff8192Limit_Type()
)
wsInfraUsedKernBuff8192Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff8192Limit.setStatus("current")


class _WsInfraUsedKernBuff16384Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff16384Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff16384Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff16384Limit_Object = MibScalar
wsInfraUsedKernBuff16384Limit = _WsInfraUsedKernBuff16384Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 35),
    _WsInfraUsedKernBuff16384Limit_Type()
)
wsInfraUsedKernBuff16384Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff16384Limit.setStatus("current")


class _WsInfraUsedKernBuff32768Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff32768Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff32768Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff32768Limit_Object = MibScalar
wsInfraUsedKernBuff32768Limit = _WsInfraUsedKernBuff32768Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 36),
    _WsInfraUsedKernBuff32768Limit_Type()
)
wsInfraUsedKernBuff32768Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff32768Limit.setStatus("current")


class _WsInfraUsedKernBuff65536Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff65536Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff65536Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff65536Limit_Object = MibScalar
wsInfraUsedKernBuff65536Limit = _WsInfraUsedKernBuff65536Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 37),
    _WsInfraUsedKernBuff65536Limit_Type()
)
wsInfraUsedKernBuff65536Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff65536Limit.setStatus("current")


class _WsInfraUsedKernBuff131072Limit_Type(Integer32):
    """Custom type wsInfraUsedKernBuff131072Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraUsedKernBuff131072Limit_Type.__name__ = "Integer32"
_WsInfraUsedKernBuff131072Limit_Object = MibScalar
wsInfraUsedKernBuff131072Limit = _WsInfraUsedKernBuff131072Limit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 4, 38),
    _WsInfraUsedKernBuff131072Limit_Type()
)
wsInfraUsedKernBuff131072Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraUsedKernBuff131072Limit.setStatus("current")


class _WsInfraDiagControl_Type(Integer32):
    """Custom type wsInfraDiagControl based on Integer32"""
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


_WsInfraDiagControl_Type.__name__ = "Integer32"
_WsInfraDiagControl_Object = MibScalar
wsInfraDiagControl = _WsInfraDiagControl_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 6),
    _WsInfraDiagControl_Type()
)
wsInfraDiagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagControl.setStatus("current")


class _WsInfraDiagPeriod_Type(Integer32):
    """Custom type wsInfraDiagPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_WsInfraDiagPeriod_Type.__name__ = "Integer32"
_WsInfraDiagPeriod_Object = MibScalar
wsInfraDiagPeriod = _WsInfraDiagPeriod_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 7),
    _WsInfraDiagPeriod_Type()
)
wsInfraDiagPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagPeriod.setUnits("millisecond")


class _WsInfraDiagFanNum_Type(Integer32):
    """Custom type wsInfraDiagFanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WsInfraDiagFanNum_Type.__name__ = "Integer32"
_WsInfraDiagFanNum_Object = MibScalar
wsInfraDiagFanNum = _WsInfraDiagFanNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 8),
    _WsInfraDiagFanNum_Type()
)
wsInfraDiagFanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagFanNum.setStatus("current")


class _WsInfraDiagTempSensorNum_Type(Integer32):
    """Custom type wsInfraDiagTempSensorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WsInfraDiagTempSensorNum_Type.__name__ = "Integer32"
_WsInfraDiagTempSensorNum_Object = MibScalar
wsInfraDiagTempSensorNum = _WsInfraDiagTempSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 9),
    _WsInfraDiagTempSensorNum_Type()
)
wsInfraDiagTempSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagTempSensorNum.setStatus("current")
_WsInfraDiagPlatform_Type = DisplayString
_WsInfraDiagPlatform_Object = MibScalar
wsInfraDiagPlatform = _WsInfraDiagPlatform_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 10),
    _WsInfraDiagPlatform_Type()
)
wsInfraDiagPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagPlatform.setStatus("current")
_WsInfraDiagMonitoredFSTable_Object = MibTable
wsInfraDiagMonitoredFSTable = _WsInfraDiagMonitoredFSTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11)
)
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSTable.setStatus("current")
_WsInfraDiagMonitoredFSEntry_Object = MibTableRow
wsInfraDiagMonitoredFSEntry = _WsInfraDiagMonitoredFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1)
)
wsInfraDiagMonitoredFSEntry.setIndexNames(
    (0, "WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSTableIndex"),
)
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSEntry.setStatus("current")


class _WsInfraDiagMonitoredFSTableIndex_Type(Unsigned32):
    """Custom type wsInfraDiagMonitoredFSTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WsInfraDiagMonitoredFSTableIndex_Type.__name__ = "Unsigned32"
_WsInfraDiagMonitoredFSTableIndex_Object = MibTableColumn
wsInfraDiagMonitoredFSTableIndex = _WsInfraDiagMonitoredFSTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 1),
    _WsInfraDiagMonitoredFSTableIndex_Type()
)
wsInfraDiagMonitoredFSTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSTableIndex.setStatus("current")
_WsInfraDiagMonitoredFSName_Type = DisplayString
_WsInfraDiagMonitoredFSName_Object = MibTableColumn
wsInfraDiagMonitoredFSName = _WsInfraDiagMonitoredFSName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 2),
    _WsInfraDiagMonitoredFSName_Type()
)
wsInfraDiagMonitoredFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSName.setStatus("current")
_WsInfraDiagMonitoredFSFreeSpace_Type = Unsigned32
_WsInfraDiagMonitoredFSFreeSpace_Object = MibTableColumn
wsInfraDiagMonitoredFSFreeSpace = _WsInfraDiagMonitoredFSFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 3),
    _WsInfraDiagMonitoredFSFreeSpace_Type()
)
wsInfraDiagMonitoredFSFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSFreeSpace.setUnits("KB")
_WsInfraDiagMonitoredFSFreeSpacePercent_Type = Integer32
_WsInfraDiagMonitoredFSFreeSpacePercent_Object = MibTableColumn
wsInfraDiagMonitoredFSFreeSpacePercent = _WsInfraDiagMonitoredFSFreeSpacePercent_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 4),
    _WsInfraDiagMonitoredFSFreeSpacePercent_Type()
)
wsInfraDiagMonitoredFSFreeSpacePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSFreeSpacePercent.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSFreeSpacePercent.setUnits("0.1%")


class _WsInfraDiagMonitoredFSFreeSpaceLimit_Type(Integer32):
    """Custom type wsInfraDiagMonitoredFSFreeSpaceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraDiagMonitoredFSFreeSpaceLimit_Type.__name__ = "Integer32"
_WsInfraDiagMonitoredFSFreeSpaceLimit_Object = MibTableColumn
wsInfraDiagMonitoredFSFreeSpaceLimit = _WsInfraDiagMonitoredFSFreeSpaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 5),
    _WsInfraDiagMonitoredFSFreeSpaceLimit_Type()
)
wsInfraDiagMonitoredFSFreeSpaceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSFreeSpaceLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSFreeSpaceLimit.setUnits("0.1%")
_WsInfraDiagMonitoredFSSize_Type = Integer32
_WsInfraDiagMonitoredFSSize_Object = MibTableColumn
wsInfraDiagMonitoredFSSize = _WsInfraDiagMonitoredFSSize_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 6),
    _WsInfraDiagMonitoredFSSize_Type()
)
wsInfraDiagMonitoredFSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSSize.setStatus("current")
_WsInfraDiagMonitoredFSUsed_Type = Integer32
_WsInfraDiagMonitoredFSUsed_Object = MibTableColumn
wsInfraDiagMonitoredFSUsed = _WsInfraDiagMonitoredFSUsed_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 7),
    _WsInfraDiagMonitoredFSUsed_Type()
)
wsInfraDiagMonitoredFSUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSUsed.setStatus("current")
_WsInfraDiagMonitoredFSINodesFree_Type = Integer32
_WsInfraDiagMonitoredFSINodesFree_Object = MibTableColumn
wsInfraDiagMonitoredFSINodesFree = _WsInfraDiagMonitoredFSINodesFree_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 8),
    _WsInfraDiagMonitoredFSINodesFree_Type()
)
wsInfraDiagMonitoredFSINodesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSINodesFree.setStatus("current")


class _WsInfraDiagMonitoredFSINodesLimit_Type(Integer32):
    """Custom type wsInfraDiagMonitoredFSINodesLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WsInfraDiagMonitoredFSINodesLimit_Type.__name__ = "Integer32"
_WsInfraDiagMonitoredFSINodesLimit_Object = MibTableColumn
wsInfraDiagMonitoredFSINodesLimit = _WsInfraDiagMonitoredFSINodesLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 11, 1, 9),
    _WsInfraDiagMonitoredFSINodesLimit_Type()
)
wsInfraDiagMonitoredFSINodesLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSINodesLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagMonitoredFSINodesLimit.setUnits("0.1%")
_WsInfraDiagTempTable_Object = MibTable
wsInfraDiagTempTable = _WsInfraDiagTempTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 12)
)
if mibBuilder.loadTexts:
    wsInfraDiagTempTable.setStatus("current")
_WsInfraDiagTempEntry_Object = MibTableRow
wsInfraDiagTempEntry = _WsInfraDiagTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 12, 1)
)
wsInfraDiagTempEntry.setIndexNames(
    (0, "WS-INFRA-DIAG-MIB", "wsInfraDiagTempIndex"),
)
if mibBuilder.loadTexts:
    wsInfraDiagTempEntry.setStatus("current")


class _WsInfraDiagTempIndex_Type(Integer32):
    """Custom type wsInfraDiagTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WsInfraDiagTempIndex_Type.__name__ = "Integer32"
_WsInfraDiagTempIndex_Object = MibTableColumn
wsInfraDiagTempIndex = _WsInfraDiagTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 12, 1, 1),
    _WsInfraDiagTempIndex_Type()
)
wsInfraDiagTempIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraDiagTempIndex.setStatus("current")
_WsInfraDiagTempSensorName_Type = DisplayString
_WsInfraDiagTempSensorName_Object = MibTableColumn
wsInfraDiagTempSensorName = _WsInfraDiagTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 12, 1, 2),
    _WsInfraDiagTempSensorName_Type()
)
wsInfraDiagTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagTempSensorName.setStatus("current")
_WsInfraDiagTempCurrTemp_Type = Integer32
_WsInfraDiagTempCurrTemp_Object = MibTableColumn
wsInfraDiagTempCurrTemp = _WsInfraDiagTempCurrTemp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 12, 1, 3),
    _WsInfraDiagTempCurrTemp_Type()
)
wsInfraDiagTempCurrTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagTempCurrTemp.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagTempCurrTemp.setUnits("0.1C")


class _WsInfraDiagTempMaxTemp_Type(Integer32):
    """Custom type wsInfraDiagTempMaxTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WsInfraDiagTempMaxTemp_Type.__name__ = "Integer32"
_WsInfraDiagTempMaxTemp_Object = MibTableColumn
wsInfraDiagTempMaxTemp = _WsInfraDiagTempMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 12, 1, 4),
    _WsInfraDiagTempMaxTemp_Type()
)
wsInfraDiagTempMaxTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagTempMaxTemp.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagTempMaxTemp.setUnits("0.1C")


class _WsInfraDiagTempOverTemp_Type(Integer32):
    """Custom type wsInfraDiagTempOverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WsInfraDiagTempOverTemp_Type.__name__ = "Integer32"
_WsInfraDiagTempOverTemp_Object = MibTableColumn
wsInfraDiagTempOverTemp = _WsInfraDiagTempOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 12, 1, 5),
    _WsInfraDiagTempOverTemp_Type()
)
wsInfraDiagTempOverTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagTempOverTemp.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagTempOverTemp.setUnits("0.1C")
_WsInfraDiagFanTable_Object = MibTable
wsInfraDiagFanTable = _WsInfraDiagFanTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 13)
)
if mibBuilder.loadTexts:
    wsInfraDiagFanTable.setStatus("current")
_WsInfraDiagFanEntry_Object = MibTableRow
wsInfraDiagFanEntry = _WsInfraDiagFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 13, 1)
)
wsInfraDiagFanEntry.setIndexNames(
    (0, "WS-INFRA-DIAG-MIB", "wsInfraDiagFanIndex"),
)
if mibBuilder.loadTexts:
    wsInfraDiagFanEntry.setStatus("current")


class _WsInfraDiagFanIndex_Type(Integer32):
    """Custom type wsInfraDiagFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_WsInfraDiagFanIndex_Type.__name__ = "Integer32"
_WsInfraDiagFanIndex_Object = MibTableColumn
wsInfraDiagFanIndex = _WsInfraDiagFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 13, 1, 1),
    _WsInfraDiagFanIndex_Type()
)
wsInfraDiagFanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraDiagFanIndex.setStatus("current")
_WsInfraDiagFanName_Type = DisplayString
_WsInfraDiagFanName_Object = MibTableColumn
wsInfraDiagFanName = _WsInfraDiagFanName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 13, 1, 2),
    _WsInfraDiagFanName_Type()
)
wsInfraDiagFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagFanName.setStatus("current")


class _WsInfraDiagFanSpeed_Type(Integer32):
    """Custom type wsInfraDiagFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15000),
    )


_WsInfraDiagFanSpeed_Type.__name__ = "Integer32"
_WsInfraDiagFanSpeed_Object = MibTableColumn
wsInfraDiagFanSpeed = _WsInfraDiagFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 13, 1, 3),
    _WsInfraDiagFanSpeed_Type()
)
wsInfraDiagFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagFanSpeed.setUnits("1 rpm")


class _WsInfraDiagFanLowSpeedLimit_Type(Integer32):
    """Custom type wsInfraDiagFanLowSpeedLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 15000),
    )


_WsInfraDiagFanLowSpeedLimit_Type.__name__ = "Integer32"
_WsInfraDiagFanLowSpeedLimit_Object = MibTableColumn
wsInfraDiagFanLowSpeedLimit = _WsInfraDiagFanLowSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 13, 1, 4),
    _WsInfraDiagFanLowSpeedLimit_Type()
)
wsInfraDiagFanLowSpeedLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagFanLowSpeedLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagFanLowSpeedLimit.setUnits("1 rpm")
_WsInfraDiagProcTable_Object = MibTable
wsInfraDiagProcTable = _WsInfraDiagProcTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 14)
)
if mibBuilder.loadTexts:
    wsInfraDiagProcTable.setStatus("current")
_WsInfraDiagProcEntry_Object = MibTableRow
wsInfraDiagProcEntry = _WsInfraDiagProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 14, 1)
)
wsInfraDiagProcEntry.setIndexNames(
    (0, "WS-INFRA-DIAG-MIB", "wsInfraDiagProcIndex"),
)
if mibBuilder.loadTexts:
    wsInfraDiagProcEntry.setStatus("current")


class _WsInfraDiagProcIndex_Type(Integer32):
    """Custom type wsInfraDiagProcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WsInfraDiagProcIndex_Type.__name__ = "Integer32"
_WsInfraDiagProcIndex_Object = MibTableColumn
wsInfraDiagProcIndex = _WsInfraDiagProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 14, 1, 1),
    _WsInfraDiagProcIndex_Type()
)
wsInfraDiagProcIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraDiagProcIndex.setStatus("current")
_WsInfraDiagProcName_Type = DisplayString
_WsInfraDiagProcName_Object = MibTableColumn
wsInfraDiagProcName = _WsInfraDiagProcName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 14, 1, 2),
    _WsInfraDiagProcName_Type()
)
wsInfraDiagProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagProcName.setStatus("current")


class _WsInfraDiagProcPercentCPU_Type(Integer32):
    """Custom type wsInfraDiagProcPercentCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraDiagProcPercentCPU_Type.__name__ = "Integer32"
_WsInfraDiagProcPercentCPU_Object = MibTableColumn
wsInfraDiagProcPercentCPU = _WsInfraDiagProcPercentCPU_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 14, 1, 3),
    _WsInfraDiagProcPercentCPU_Type()
)
wsInfraDiagProcPercentCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagProcPercentCPU.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagProcPercentCPU.setUnits("0.1%")


class _WsInfraDiagProcPercentMem_Type(Integer32):
    """Custom type wsInfraDiagProcPercentMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraDiagProcPercentMem_Type.__name__ = "Integer32"
_WsInfraDiagProcPercentMem_Object = MibTableColumn
wsInfraDiagProcPercentMem = _WsInfraDiagProcPercentMem_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 14, 1, 4),
    _WsInfraDiagProcPercentMem_Type()
)
wsInfraDiagProcPercentMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagProcPercentMem.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagProcPercentMem.setUnits("0.1%")
_WsInfraDiagRamStats_ObjectIdentity = ObjectIdentity
wsInfraDiagRamStats = _WsInfraDiagRamStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 15)
)
_WsInfraDiagRamStatsTotal_Type = Integer32
_WsInfraDiagRamStatsTotal_Object = MibScalar
wsInfraDiagRamStatsTotal = _WsInfraDiagRamStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 15, 1),
    _WsInfraDiagRamStatsTotal_Type()
)
wsInfraDiagRamStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagRamStatsTotal.setStatus("current")
_WsInfraDiagRamStatsUsed_Type = Integer32
_WsInfraDiagRamStatsUsed_Object = MibScalar
wsInfraDiagRamStatsUsed = _WsInfraDiagRamStatsUsed_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 15, 2),
    _WsInfraDiagRamStatsUsed_Type()
)
wsInfraDiagRamStatsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagRamStatsUsed.setStatus("current")
_WsInfraDiagRamStatsFree_Type = Integer32
_WsInfraDiagRamStatsFree_Object = MibScalar
wsInfraDiagRamStatsFree = _WsInfraDiagRamStatsFree_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 15, 3),
    _WsInfraDiagRamStatsFree_Type()
)
wsInfraDiagRamStatsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagRamStatsFree.setStatus("current")


class _WsInfraDiagRamStatsPercentFree_Type(Integer32):
    """Custom type wsInfraDiagRamStatsPercentFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraDiagRamStatsPercentFree_Type.__name__ = "Integer32"
_WsInfraDiagRamStatsPercentFree_Object = MibScalar
wsInfraDiagRamStatsPercentFree = _WsInfraDiagRamStatsPercentFree_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 15, 4),
    _WsInfraDiagRamStatsPercentFree_Type()
)
wsInfraDiagRamStatsPercentFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagRamStatsPercentFree.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagRamStatsPercentFree.setUnits("0.1%")


class _WsInfraDiagRamStatsPercentFreeLimit_Type(Integer32):
    """Custom type wsInfraDiagRamStatsPercentFreeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_WsInfraDiagRamStatsPercentFreeLimit_Type.__name__ = "Integer32"
_WsInfraDiagRamStatsPercentFreeLimit_Object = MibScalar
wsInfraDiagRamStatsPercentFreeLimit = _WsInfraDiagRamStatsPercentFreeLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 15, 5),
    _WsInfraDiagRamStatsPercentFreeLimit_Type()
)
wsInfraDiagRamStatsPercentFreeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagRamStatsPercentFreeLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagRamStatsPercentFreeLimit.setUnits("0.1 %")
_WsInfraDiagPktBuffStats_ObjectIdentity = ObjectIdentity
wsInfraDiagPktBuffStats = _WsInfraDiagPktBuffStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 17)
)
_WsInfraDiagPktBuffAlloc_Type = Integer32
_WsInfraDiagPktBuffAlloc_Object = MibScalar
wsInfraDiagPktBuffAlloc = _WsInfraDiagPktBuffAlloc_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 17, 1),
    _WsInfraDiagPktBuffAlloc_Type()
)
wsInfraDiagPktBuffAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagPktBuffAlloc.setStatus("current")
_WsInfraDiagPktBuffUsed_Type = Integer32
_WsInfraDiagPktBuffUsed_Object = MibScalar
wsInfraDiagPktBuffUsed = _WsInfraDiagPktBuffUsed_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 17, 2),
    _WsInfraDiagPktBuffUsed_Type()
)
wsInfraDiagPktBuffUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagPktBuffUsed.setStatus("current")


class _WsInfraDiagPktBuffMax_Type(Integer32):
    """Custom type wsInfraDiagPktBuffMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraDiagPktBuffMax_Type.__name__ = "Integer32"
_WsInfraDiagPktBuffMax_Object = MibScalar
wsInfraDiagPktBuffMax = _WsInfraDiagPktBuffMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 17, 3),
    _WsInfraDiagPktBuffMax_Type()
)
wsInfraDiagPktBuffMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagPktBuffMax.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagPktBuffMax.setUnits("KB")
_WsInfraDiagIpRouteCacheStats_ObjectIdentity = ObjectIdentity
wsInfraDiagIpRouteCacheStats = _WsInfraDiagIpRouteCacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 18)
)
_WsInfraDiagIpRouteCacheAlloc_Type = Integer32
_WsInfraDiagIpRouteCacheAlloc_Object = MibScalar
wsInfraDiagIpRouteCacheAlloc = _WsInfraDiagIpRouteCacheAlloc_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 18, 1),
    _WsInfraDiagIpRouteCacheAlloc_Type()
)
wsInfraDiagIpRouteCacheAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagIpRouteCacheAlloc.setStatus("current")
_WsInfraDiagIpRouteCacheUsed_Type = Integer32
_WsInfraDiagIpRouteCacheUsed_Object = MibScalar
wsInfraDiagIpRouteCacheUsed = _WsInfraDiagIpRouteCacheUsed_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 18, 2),
    _WsInfraDiagIpRouteCacheUsed_Type()
)
wsInfraDiagIpRouteCacheUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagIpRouteCacheUsed.setStatus("current")


class _WsInfraDiagIpRouteCacheMax_Type(Integer32):
    """Custom type wsInfraDiagIpRouteCacheMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsInfraDiagIpRouteCacheMax_Type.__name__ = "Integer32"
_WsInfraDiagIpRouteCacheMax_Object = MibScalar
wsInfraDiagIpRouteCacheMax = _WsInfraDiagIpRouteCacheMax_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 18, 3),
    _WsInfraDiagIpRouteCacheMax_Type()
)
wsInfraDiagIpRouteCacheMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagIpRouteCacheMax.setStatus("current")
_WsInfraDiagFileDescStats_ObjectIdentity = ObjectIdentity
wsInfraDiagFileDescStats = _WsInfraDiagFileDescStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 19)
)
_WsInfraDiagFileDescInUse_Type = Integer32
_WsInfraDiagFileDescInUse_Object = MibScalar
wsInfraDiagFileDescInUse = _WsInfraDiagFileDescInUse_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 19, 1),
    _WsInfraDiagFileDescInUse_Type()
)
wsInfraDiagFileDescInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagFileDescInUse.setStatus("current")
_WsInfraDiagFileDescHWM_Type = Integer32
_WsInfraDiagFileDescHWM_Object = MibScalar
wsInfraDiagFileDescHWM = _WsInfraDiagFileDescHWM_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 19, 2),
    _WsInfraDiagFileDescHWM_Type()
)
wsInfraDiagFileDescHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagFileDescHWM.setStatus("current")


class _WsInfraDiagFileDescLimit_Type(Integer32):
    """Custom type wsInfraDiagFileDescLimit based on Integer32"""
    defaultBinValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WsInfraDiagFileDescLimit_Type.__name__ = "Integer32"
_WsInfraDiagFileDescLimit_Object = MibScalar
wsInfraDiagFileDescLimit = _WsInfraDiagFileDescLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 19, 3),
    _WsInfraDiagFileDescLimit_Type()
)
wsInfraDiagFileDescLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagFileDescLimit.setStatus("current")
_WsInfraDiagProcNum_Type = Integer32
_WsInfraDiagProcNum_Object = MibScalar
wsInfraDiagProcNum = _WsInfraDiagProcNum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 20),
    _WsInfraDiagProcNum_Type()
)
wsInfraDiagProcNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraDiagProcNum.setStatus("current")


class _WsInfraDiagProcMemLimit_Type(Integer32):
    """Custom type wsInfraDiagProcMemLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WsInfraDiagProcMemLimit_Type.__name__ = "Integer32"
_WsInfraDiagProcMemLimit_Object = MibScalar
wsInfraDiagProcMemLimit = _WsInfraDiagProcMemLimit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 21),
    _WsInfraDiagProcMemLimit_Type()
)
wsInfraDiagProcMemLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraDiagProcMemLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraDiagProcMemLimit.setUnits("%")
_WsInfraDiagMIBConformance_ObjectIdentity = ObjectIdentity
wsInfraDiagMIBConformance = _WsInfraDiagMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 100)
)
_WsInfraDiagMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfraDiagMIBCompliances = _WsInfraDiagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 100, 1)
)
_WsInfraDiagMIBGroups_ObjectIdentity = ObjectIdentity
wsInfraDiagMIBGroups = _WsInfraDiagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 100, 2)
)

# Managed Objects groups

wsInfraMIBDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 100, 2, 1)
)
wsInfraMIBDiagGroup.setObjects(
      *(("WS-INFRA-DIAG-MIB", "wsInfraHwBuildInfoModuleName"),
        ("WS-INFRA-DIAG-MIB", "wsInfraHwBuildInfoVersion"),
        ("WS-INFRA-DIAG-MIB", "wsInfraHwBuildInfoManufacturer"),
        ("WS-INFRA-DIAG-MIB", "wsInfraHwBuildInfoDesc"),
        ("WS-INFRA-DIAG-MIB", "wsInfraResCpuLoad1"),
        ("WS-INFRA-DIAG-MIB", "wsInfraResCpuLoad5"),
        ("WS-INFRA-DIAG-MIB", "wsInfraResCpuLoad15"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff32"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff64"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff128"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff256"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff512"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff1024"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff2048"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff4096"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff8192"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff16384"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff32768"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff65536"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff131072"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagControl"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagPeriod"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFanNum"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempSensorNum"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagPlatform"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSFreeSpaceLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraResCpuLoad1MinLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff32Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff64Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff128Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff256Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff512Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff1024Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff2048Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff4096Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff8192Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff16384Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff32768Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff65536Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraUsedKernBuff131072Limit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSSize"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSUsed"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSINodesFree"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSINodesLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempIndex"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempSensorName"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempCurrTemp"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempMaxTemp"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempOverTemp"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFanIndex"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFanName"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFanSpeed"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFanLowSpeedLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagProcIndex"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagProcName"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagProcPercentCPU"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagProcPercentMem"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagPktBuffAlloc"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagPktBuffUsed"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagPktBuffMax"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagIpRouteCacheAlloc"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagIpRouteCacheUsed"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagIpRouteCacheMax"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFileDescInUse"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFileDescHWM"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagFileDescLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagProcNum"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagProcMemLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagRamStatsTotal"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagRamStatsUsed"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagRamStatsFree"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagRamStatsPercentFree"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagRamStatsPercentFreeLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraResCpuLoad15MinLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraResCpuLoad5MinLimit"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSFreeSpacePercent"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSFreeSpace"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagMonitoredFSName"))
)
if mibBuilder.loadTexts:
    wsInfraMIBDiagGroup.setStatus("current")

wsInfraMIBDiagObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 100, 2, 2)
)
wsInfraMIBDiagObsoleteGroup.setObjects(
      *(("WS-INFRA-DIAG-MIB", "wsInfraDiagTempCurrentTemp"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempHighTemp"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagTempHighTempHysteresis"),
        ("WS-INFRA-DIAG-MIB", "wsInfraDiagSysFanSpeed"),
        ("WS-INFRA-DIAG-MIB", "wsDiagProcFanSpeed"),
        ("WS-INFRA-DIAG-MIB", "wsInfraFreeMemory"),
        ("WS-INFRA-DIAG-MIB", "wsInfraRootFSFree"),
        ("WS-INFRA-DIAG-MIB", "wsInfraRootFSInodesFree"),
        ("WS-INFRA-DIAG-MIB", "wsInfraRamFSFree"),
        ("WS-INFRA-DIAG-MIB", "wsInfraRamFSInodesFree"),
        ("WS-INFRA-DIAG-MIB", "wsInfraFreeFileDesc"),
        ("WS-INFRA-DIAG-MIB", "wsInfraHwTotalNum"))
)
if mibBuilder.loadTexts:
    wsInfraMIBDiagObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfraDiagMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    wsInfraDiagMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-DIAG-MIB",
    **{"wsInfraDiagMib": wsInfraDiagMib,
       "wsInfraDiagTempControl": wsInfraDiagTempControl,
       "wsInfraDiagTempCurrentTemp": wsInfraDiagTempCurrentTemp,
       "wsInfraDiagTempHighTemp": wsInfraDiagTempHighTemp,
       "wsInfraDiagTempHighTempHysteresis": wsInfraDiagTempHighTempHysteresis,
       "wsInfraDiagFanControl": wsInfraDiagFanControl,
       "wsInfraDiagSysFanSpeed": wsInfraDiagSysFanSpeed,
       "wsDiagProcFanSpeed": wsDiagProcFanSpeed,
       "wsInfraHwBuildInfo": wsInfraHwBuildInfo,
       "wsInfraHwTotalNum": wsInfraHwTotalNum,
       "wsInfraHwBuildInfoTable": wsInfraHwBuildInfoTable,
       "wsInfraHwBuildInfoEntry": wsInfraHwBuildInfoEntry,
       "wsInfraHwBuildInfoModuleIndex": wsInfraHwBuildInfoModuleIndex,
       "wsInfraHwBuildInfoModuleName": wsInfraHwBuildInfoModuleName,
       "wsInfraHwBuildInfoVersion": wsInfraHwBuildInfoVersion,
       "wsInfraHwBuildInfoManufacturer": wsInfraHwBuildInfoManufacturer,
       "wsInfraHwBuildInfoDesc": wsInfraHwBuildInfoDesc,
       "wsInfraResStats": wsInfraResStats,
       "wsInfraResCpuLoad1": wsInfraResCpuLoad1,
       "wsInfraResCpuLoad5": wsInfraResCpuLoad5,
       "wsInfraResCpuLoad15": wsInfraResCpuLoad15,
       "wsInfraFreeMemory": wsInfraFreeMemory,
       "wsInfraRootFSFree": wsInfraRootFSFree,
       "wsInfraRootFSInodesFree": wsInfraRootFSInodesFree,
       "wsInfraRamFSFree": wsInfraRamFSFree,
       "wsInfraRamFSInodesFree": wsInfraRamFSInodesFree,
       "wsInfraFreeFileDesc": wsInfraFreeFileDesc,
       "wsInfraUsedKernBuff32": wsInfraUsedKernBuff32,
       "wsInfraUsedKernBuff64": wsInfraUsedKernBuff64,
       "wsInfraUsedKernBuff128": wsInfraUsedKernBuff128,
       "wsInfraUsedKernBuff256": wsInfraUsedKernBuff256,
       "wsInfraUsedKernBuff512": wsInfraUsedKernBuff512,
       "wsInfraUsedKernBuff1024": wsInfraUsedKernBuff1024,
       "wsInfraUsedKernBuff2048": wsInfraUsedKernBuff2048,
       "wsInfraUsedKernBuff4096": wsInfraUsedKernBuff4096,
       "wsInfraUsedKernBuff8192": wsInfraUsedKernBuff8192,
       "wsInfraUsedKernBuff16384": wsInfraUsedKernBuff16384,
       "wsInfraUsedKernBuff32768": wsInfraUsedKernBuff32768,
       "wsInfraUsedKernBuff65536": wsInfraUsedKernBuff65536,
       "wsInfraUsedKernBuff131072": wsInfraUsedKernBuff131072,
       "wsInfraResCpuLoad1MinLimit": wsInfraResCpuLoad1MinLimit,
       "wsInfraResCpuLoad5MinLimit": wsInfraResCpuLoad5MinLimit,
       "wsInfraResCpuLoad15MinLimit": wsInfraResCpuLoad15MinLimit,
       "wsInfraUsedKernBuff32Limit": wsInfraUsedKernBuff32Limit,
       "wsInfraUsedKernBuff64Limit": wsInfraUsedKernBuff64Limit,
       "wsInfraUsedKernBuff128Limit": wsInfraUsedKernBuff128Limit,
       "wsInfraUsedKernBuff256Limit": wsInfraUsedKernBuff256Limit,
       "wsInfraUsedKernBuff512Limit": wsInfraUsedKernBuff512Limit,
       "wsInfraUsedKernBuff1024Limit": wsInfraUsedKernBuff1024Limit,
       "wsInfraUsedKernBuff2048Limit": wsInfraUsedKernBuff2048Limit,
       "wsInfraUsedKernBuff4096Limit": wsInfraUsedKernBuff4096Limit,
       "wsInfraUsedKernBuff8192Limit": wsInfraUsedKernBuff8192Limit,
       "wsInfraUsedKernBuff16384Limit": wsInfraUsedKernBuff16384Limit,
       "wsInfraUsedKernBuff32768Limit": wsInfraUsedKernBuff32768Limit,
       "wsInfraUsedKernBuff65536Limit": wsInfraUsedKernBuff65536Limit,
       "wsInfraUsedKernBuff131072Limit": wsInfraUsedKernBuff131072Limit,
       "wsInfraDiagControl": wsInfraDiagControl,
       "wsInfraDiagPeriod": wsInfraDiagPeriod,
       "wsInfraDiagFanNum": wsInfraDiagFanNum,
       "wsInfraDiagTempSensorNum": wsInfraDiagTempSensorNum,
       "wsInfraDiagPlatform": wsInfraDiagPlatform,
       "wsInfraDiagMonitoredFSTable": wsInfraDiagMonitoredFSTable,
       "wsInfraDiagMonitoredFSEntry": wsInfraDiagMonitoredFSEntry,
       "wsInfraDiagMonitoredFSTableIndex": wsInfraDiagMonitoredFSTableIndex,
       "wsInfraDiagMonitoredFSName": wsInfraDiagMonitoredFSName,
       "wsInfraDiagMonitoredFSFreeSpace": wsInfraDiagMonitoredFSFreeSpace,
       "wsInfraDiagMonitoredFSFreeSpacePercent": wsInfraDiagMonitoredFSFreeSpacePercent,
       "wsInfraDiagMonitoredFSFreeSpaceLimit": wsInfraDiagMonitoredFSFreeSpaceLimit,
       "wsInfraDiagMonitoredFSSize": wsInfraDiagMonitoredFSSize,
       "wsInfraDiagMonitoredFSUsed": wsInfraDiagMonitoredFSUsed,
       "wsInfraDiagMonitoredFSINodesFree": wsInfraDiagMonitoredFSINodesFree,
       "wsInfraDiagMonitoredFSINodesLimit": wsInfraDiagMonitoredFSINodesLimit,
       "wsInfraDiagTempTable": wsInfraDiagTempTable,
       "wsInfraDiagTempEntry": wsInfraDiagTempEntry,
       "wsInfraDiagTempIndex": wsInfraDiagTempIndex,
       "wsInfraDiagTempSensorName": wsInfraDiagTempSensorName,
       "wsInfraDiagTempCurrTemp": wsInfraDiagTempCurrTemp,
       "wsInfraDiagTempMaxTemp": wsInfraDiagTempMaxTemp,
       "wsInfraDiagTempOverTemp": wsInfraDiagTempOverTemp,
       "wsInfraDiagFanTable": wsInfraDiagFanTable,
       "wsInfraDiagFanEntry": wsInfraDiagFanEntry,
       "wsInfraDiagFanIndex": wsInfraDiagFanIndex,
       "wsInfraDiagFanName": wsInfraDiagFanName,
       "wsInfraDiagFanSpeed": wsInfraDiagFanSpeed,
       "wsInfraDiagFanLowSpeedLimit": wsInfraDiagFanLowSpeedLimit,
       "wsInfraDiagProcTable": wsInfraDiagProcTable,
       "wsInfraDiagProcEntry": wsInfraDiagProcEntry,
       "wsInfraDiagProcIndex": wsInfraDiagProcIndex,
       "wsInfraDiagProcName": wsInfraDiagProcName,
       "wsInfraDiagProcPercentCPU": wsInfraDiagProcPercentCPU,
       "wsInfraDiagProcPercentMem": wsInfraDiagProcPercentMem,
       "wsInfraDiagRamStats": wsInfraDiagRamStats,
       "wsInfraDiagRamStatsTotal": wsInfraDiagRamStatsTotal,
       "wsInfraDiagRamStatsUsed": wsInfraDiagRamStatsUsed,
       "wsInfraDiagRamStatsFree": wsInfraDiagRamStatsFree,
       "wsInfraDiagRamStatsPercentFree": wsInfraDiagRamStatsPercentFree,
       "wsInfraDiagRamStatsPercentFreeLimit": wsInfraDiagRamStatsPercentFreeLimit,
       "wsInfraDiagPktBuffStats": wsInfraDiagPktBuffStats,
       "wsInfraDiagPktBuffAlloc": wsInfraDiagPktBuffAlloc,
       "wsInfraDiagPktBuffUsed": wsInfraDiagPktBuffUsed,
       "wsInfraDiagPktBuffMax": wsInfraDiagPktBuffMax,
       "wsInfraDiagIpRouteCacheStats": wsInfraDiagIpRouteCacheStats,
       "wsInfraDiagIpRouteCacheAlloc": wsInfraDiagIpRouteCacheAlloc,
       "wsInfraDiagIpRouteCacheUsed": wsInfraDiagIpRouteCacheUsed,
       "wsInfraDiagIpRouteCacheMax": wsInfraDiagIpRouteCacheMax,
       "wsInfraDiagFileDescStats": wsInfraDiagFileDescStats,
       "wsInfraDiagFileDescInUse": wsInfraDiagFileDescInUse,
       "wsInfraDiagFileDescHWM": wsInfraDiagFileDescHWM,
       "wsInfraDiagFileDescLimit": wsInfraDiagFileDescLimit,
       "wsInfraDiagProcNum": wsInfraDiagProcNum,
       "wsInfraDiagProcMemLimit": wsInfraDiagProcMemLimit,
       "wsInfraDiagMIBConformance": wsInfraDiagMIBConformance,
       "wsInfraDiagMIBCompliances": wsInfraDiagMIBCompliances,
       "wsInfraDiagMIBCompliance": wsInfraDiagMIBCompliance,
       "wsInfraDiagMIBGroups": wsInfraDiagMIBGroups,
       "wsInfraMIBDiagGroup": wsInfraMIBDiagGroup,
       "wsInfraMIBDiagObsoleteGroup": wsInfraMIBDiagObsoleteGroup}
)
