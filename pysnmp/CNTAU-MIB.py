# SNMP MIB module (CNTAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNTAU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:01 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cnt_ObjectIdentity = ObjectIdentity
cnt = _Cnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333)
)
_Cntau_ObjectIdentity = ObjectIdentity
cntau = _Cntau_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1)
)
_Cntsystem_ObjectIdentity = ObjectIdentity
cntsystem = _Cntsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 1)
)
_CntSysNodeAddress_Type = IpAddress
_CntSysNodeAddress_Object = MibScalar
cntSysNodeAddress = _CntSysNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 1),
    _CntSysNodeAddress_Type()
)
cntSysNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSysNodeAddress.setStatus("mandatory")
_CntSysTimeofDay_Type = DisplayString
_CntSysTimeofDay_Object = MibScalar
cntSysTimeofDay = _CntSysTimeofDay_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 2),
    _CntSysTimeofDay_Type()
)
cntSysTimeofDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSysTimeofDay.setStatus("mandatory")
_CntSysMsgTable_Object = MibTable
cntSysMsgTable = _CntSysMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cntSysMsgTable.setStatus("mandatory")
_CntMsgEntry_Object = MibTableRow
cntMsgEntry = _CntMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1)
)
cntMsgEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntMsgIndex"),
)
if mibBuilder.loadTexts:
    cntMsgEntry.setStatus("mandatory")
_CntMsgIndex_Type = Integer32
_CntMsgIndex_Object = MibTableColumn
cntMsgIndex = _CntMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 1),
    _CntMsgIndex_Type()
)
cntMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgIndex.setStatus("mandatory")


class _CntMsgSeverity_Type(Integer32):
    """Custom type cntMsgSeverity based on Integer32"""
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
        *(("fatal-error", 4),
          ("information-msg", 1),
          ("possible-error", 2),
          ("recoverable-error", 3))
    )


_CntMsgSeverity_Type.__name__ = "Integer32"
_CntMsgSeverity_Object = MibTableColumn
cntMsgSeverity = _CntMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 2),
    _CntMsgSeverity_Type()
)
cntMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgSeverity.setStatus("mandatory")
_CntMsgTaskName_Type = DisplayString
_CntMsgTaskName_Object = MibTableColumn
cntMsgTaskName = _CntMsgTaskName_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 3),
    _CntMsgTaskName_Type()
)
cntMsgTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgTaskName.setStatus("mandatory")
_CntMsgNumber_Type = Integer32
_CntMsgNumber_Object = MibTableColumn
cntMsgNumber = _CntMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 4),
    _CntMsgNumber_Type()
)
cntMsgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgNumber.setStatus("mandatory")


class _CntMsgCpuNumber_Type(Integer32):
    """Custom type cntMsgCpuNumber based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CntMsgCpuNumber_Type.__name__ = "Integer32"
_CntMsgCpuNumber_Object = MibTableColumn
cntMsgCpuNumber = _CntMsgCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 5),
    _CntMsgCpuNumber_Type()
)
cntMsgCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgCpuNumber.setStatus("mandatory")
_CntMsgNodeNumber_Type = DisplayString
_CntMsgNodeNumber_Object = MibTableColumn
cntMsgNodeNumber = _CntMsgNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 6),
    _CntMsgNodeNumber_Type()
)
cntMsgNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgNodeNumber.setStatus("mandatory")
_CntMsgDateTime_Type = DisplayString
_CntMsgDateTime_Object = MibTableColumn
cntMsgDateTime = _CntMsgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 7),
    _CntMsgDateTime_Type()
)
cntMsgDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgDateTime.setStatus("mandatory")
_CntMsgContent_Type = DisplayString
_CntMsgContent_Object = MibTableColumn
cntMsgContent = _CntMsgContent_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 8),
    _CntMsgContent_Type()
)
cntMsgContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgContent.setStatus("mandatory")
_CntMsgSeqNumber_Type = Integer32
_CntMsgSeqNumber_Object = MibTableColumn
cntMsgSeqNumber = _CntMsgSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 3, 1, 9),
    _CntMsgSeqNumber_Type()
)
cntMsgSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMsgSeqNumber.setStatus("mandatory")
_CntSysHardware_ObjectIdentity = ObjectIdentity
cntSysHardware = _CntSysHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4)
)


class _CntHwBBramType_Type(Integer32):
    """Custom type cntHwBBramType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bbram-6500", 1),
          ("bbram-6704", 2))
    )


_CntHwBBramType_Type.__name__ = "Integer32"
_CntHwBBramType_Object = MibScalar
cntHwBBramType = _CntHwBBramType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 1),
    _CntHwBBramType_Type()
)
cntHwBBramType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwBBramType.setStatus("mandatory")


class _CntHwBBramStatus_Type(Integer32):
    """Custom type cntHwBBramStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failing", 2),
          ("good", 1))
    )


_CntHwBBramStatus_Type.__name__ = "Integer32"
_CntHwBBramStatus_Object = MibScalar
cntHwBBramStatus = _CntHwBBramStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 2),
    _CntHwBBramStatus_Type()
)
cntHwBBramStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwBBramStatus.setStatus("mandatory")


class _CntHwFailedCpu_Type(Integer32):
    """Custom type cntHwFailedCpu based on Integer32"""
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
        *(("lcp-1", 2),
          ("lcp-2", 3),
          ("lcp-3", 4),
          ("lcp-4", 5),
          ("lcp-5", 6),
          ("lcp-6", 7),
          ("lcp-7", 8),
          ("no-failure", 1))
    )


_CntHwFailedCpu_Type.__name__ = "Integer32"
_CntHwFailedCpu_Object = MibScalar
cntHwFailedCpu = _CntHwFailedCpu_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 3),
    _CntHwFailedCpu_Type()
)
cntHwFailedCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwFailedCpu.setStatus("mandatory")


class _CntHwMonCpu_Type(Integer32):
    """Custom type cntHwMonCpu based on Integer32"""
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
        *(("lcp-1", 2),
          ("lcp-2", 3),
          ("lcp-3", 4),
          ("lcp-4", 5),
          ("lcp-5", 6),
          ("lcp-6", 7),
          ("lcp-7", 8),
          ("no-failure", 1))
    )


_CntHwMonCpu_Type.__name__ = "Integer32"
_CntHwMonCpu_Object = MibScalar
cntHwMonCpu = _CntHwMonCpu_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 4),
    _CntHwMonCpu_Type()
)
cntHwMonCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwMonCpu.setStatus("mandatory")


class _CntHwFailStatus_Type(Integer32):
    """Custom type cntHwFailStatus based on Integer32"""
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
        *(("abort-remote", 4),
          ("abort-switch", 3),
          ("ac-failure", 6),
          ("not-up", 1),
          ("ok", 2),
          ("parity-error", 5),
          ("system-failure", 7))
    )


_CntHwFailStatus_Type.__name__ = "Integer32"
_CntHwFailStatus_Object = MibScalar
cntHwFailStatus = _CntHwFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 5),
    _CntHwFailStatus_Type()
)
cntHwFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwFailStatus.setStatus("mandatory")


class _CntHwMonFailStatus_Type(Integer32):
    """Custom type cntHwMonFailStatus based on Integer32"""
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
        *(("failed", 3),
          ("mdm-error", 4),
          ("not-up", 1),
          ("ok", 2),
          ("poll-error", 5))
    )


_CntHwMonFailStatus_Type.__name__ = "Integer32"
_CntHwMonFailStatus_Object = MibScalar
cntHwMonFailStatus = _CntHwMonFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 6),
    _CntHwMonFailStatus_Type()
)
cntHwMonFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwMonFailStatus.setStatus("mandatory")
_CntHwFailDate_Type = DisplayString
_CntHwFailDate_Object = MibScalar
cntHwFailDate = _CntHwFailDate_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 7),
    _CntHwFailDate_Type()
)
cntHwFailDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwFailDate.setStatus("mandatory")
_CntHwReset1Why_Type = DisplayString
_CntHwReset1Why_Object = MibScalar
cntHwReset1Why = _CntHwReset1Why_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 8),
    _CntHwReset1Why_Type()
)
cntHwReset1Why.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwReset1Why.setStatus("mandatory")
_CntHwReset1Date_Type = DisplayString
_CntHwReset1Date_Object = MibScalar
cntHwReset1Date = _CntHwReset1Date_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 9),
    _CntHwReset1Date_Type()
)
cntHwReset1Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwReset1Date.setStatus("mandatory")
_CntHwReset2Why_Type = DisplayString
_CntHwReset2Why_Object = MibScalar
cntHwReset2Why = _CntHwReset2Why_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 10),
    _CntHwReset2Why_Type()
)
cntHwReset2Why.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwReset2Why.setStatus("mandatory")
_CntHwReset2Date_Type = DisplayString
_CntHwReset2Date_Object = MibScalar
cntHwReset2Date = _CntHwReset2Date_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 11),
    _CntHwReset2Date_Type()
)
cntHwReset2Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwReset2Date.setStatus("mandatory")
_CntHwReset3Why_Type = DisplayString
_CntHwReset3Why_Object = MibScalar
cntHwReset3Why = _CntHwReset3Why_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 12),
    _CntHwReset3Why_Type()
)
cntHwReset3Why.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwReset3Why.setStatus("mandatory")
_CntHwReset3Date_Type = DisplayString
_CntHwReset3Date_Object = MibScalar
cntHwReset3Date = _CntHwReset3Date_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 13),
    _CntHwReset3Date_Type()
)
cntHwReset3Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwReset3Date.setStatus("mandatory")


class _CntHwPowerSupply_Type(Integer32):
    """Custom type cntHwPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_CntHwPowerSupply_Type.__name__ = "Integer32"
_CntHwPowerSupply_Object = MibScalar
cntHwPowerSupply = _CntHwPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 14),
    _CntHwPowerSupply_Type()
)
cntHwPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwPowerSupply.setStatus("mandatory")
_CntHwCpuTable_Object = MibTable
cntHwCpuTable = _CntHwCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15)
)
if mibBuilder.loadTexts:
    cntHwCpuTable.setStatus("mandatory")
_CntHwCpuEntry_Object = MibTableRow
cntHwCpuEntry = _CntHwCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1)
)
cntHwCpuEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntCpuNum"),
)
if mibBuilder.loadTexts:
    cntHwCpuEntry.setStatus("mandatory")


class _CntCpuNum_Type(Integer32):
    """Custom type cntCpuNum based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CntCpuNum_Type.__name__ = "Integer32"
_CntCpuNum_Object = MibTableColumn
cntCpuNum = _CntCpuNum_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 1),
    _CntCpuNum_Type()
)
cntCpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuNum.setStatus("mandatory")


class _CntCpuType_Type(Integer32):
    """Custom type cntCpuType based on Integer32"""
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
        *(("lcp-type1", 2),
          ("lcp-type2", 3),
          ("lcp-type3", 4),
          ("lcp-type4", 5),
          ("no-cpu", 1))
    )


_CntCpuType_Type.__name__ = "Integer32"
_CntCpuType_Object = MibTableColumn
cntCpuType = _CntCpuType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 2),
    _CntCpuType_Type()
)
cntCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuType.setStatus("mandatory")
_CntCpuSemCount_Type = Integer32
_CntCpuSemCount_Object = MibTableColumn
cntCpuSemCount = _CntCpuSemCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 3),
    _CntCpuSemCount_Type()
)
cntCpuSemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuSemCount.setStatus("mandatory")
_CntCpuSemLost_Type = Integer32
_CntCpuSemLost_Object = MibTableColumn
cntCpuSemLost = _CntCpuSemLost_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 4),
    _CntCpuSemLost_Type()
)
cntCpuSemLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuSemLost.setStatus("mandatory")


class _CntCpuStatus_Type(Integer32):
    """Custom type cntCpuStatus based on Integer32"""
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
        *(("abort-remote", 4),
          ("abort-switch", 3),
          ("ac-failure", 6),
          ("not-up", 1),
          ("ok", 2),
          ("parity-error", 5),
          ("system-failure", 7))
    )


_CntCpuStatus_Type.__name__ = "Integer32"
_CntCpuStatus_Object = MibTableColumn
cntCpuStatus = _CntCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 5),
    _CntCpuStatus_Type()
)
cntCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuStatus.setStatus("mandatory")


class _CntCpuMonStatus_Type(Integer32):
    """Custom type cntCpuMonStatus based on Integer32"""
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
        *(("failed", 3),
          ("mdm-error", 4),
          ("not-up", 1),
          ("ok", 2),
          ("poll-error", 5))
    )


_CntCpuMonStatus_Type.__name__ = "Integer32"
_CntCpuMonStatus_Object = MibTableColumn
cntCpuMonStatus = _CntCpuMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 6),
    _CntCpuMonStatus_Type()
)
cntCpuMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuMonStatus.setStatus("mandatory")


class _CntCpuPollStatus_Type(Integer32):
    """Custom type cntCpuPollStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("normal", 2))
    )


_CntCpuPollStatus_Type.__name__ = "Integer32"
_CntCpuPollStatus_Object = MibTableColumn
cntCpuPollStatus = _CntCpuPollStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 7),
    _CntCpuPollStatus_Type()
)
cntCpuPollStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuPollStatus.setStatus("mandatory")
_CntCpuPolls_Type = Counter32
_CntCpuPolls_Object = MibTableColumn
cntCpuPolls = _CntCpuPolls_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 8),
    _CntCpuPolls_Type()
)
cntCpuPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuPolls.setStatus("mandatory")
_CntCpuResetDelayTime_Type = Integer32
_CntCpuResetDelayTime_Object = MibTableColumn
cntCpuResetDelayTime = _CntCpuResetDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 9),
    _CntCpuResetDelayTime_Type()
)
cntCpuResetDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuResetDelayTime.setStatus("mandatory")


class _CntCpuMonBy_Type(Integer32):
    """Custom type cntCpuMonBy based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CntCpuMonBy_Type.__name__ = "Integer32"
_CntCpuMonBy_Object = MibTableColumn
cntCpuMonBy = _CntCpuMonBy_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 10),
    _CntCpuMonBy_Type()
)
cntCpuMonBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuMonBy.setStatus("mandatory")
_CntCpuPort_Type = Integer32
_CntCpuPort_Object = MibTableColumn
cntCpuPort = _CntCpuPort_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 11),
    _CntCpuPort_Type()
)
cntCpuPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuPort.setStatus("mandatory")
_CntCpuUnclaims_Type = Counter32
_CntCpuUnclaims_Object = MibTableColumn
cntCpuUnclaims = _CntCpuUnclaims_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 12),
    _CntCpuUnclaims_Type()
)
cntCpuUnclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuUnclaims.setStatus("mandatory")
_CntCpuXtraInts_Type = Counter32
_CntCpuXtraInts_Object = MibTableColumn
cntCpuXtraInts = _CntCpuXtraInts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 13),
    _CntCpuXtraInts_Type()
)
cntCpuXtraInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuXtraInts.setStatus("mandatory")
_CntCpuLevel7s_Type = Counter32
_CntCpuLevel7s_Object = MibTableColumn
cntCpuLevel7s = _CntCpuLevel7s_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 14),
    _CntCpuLevel7s_Type()
)
cntCpuLevel7s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuLevel7s.setStatus("mandatory")
_CntCpuMsgRets_Type = Counter32
_CntCpuMsgRets_Object = MibTableColumn
cntCpuMsgRets = _CntCpuMsgRets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 15),
    _CntCpuMsgRets_Type()
)
cntCpuMsgRets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuMsgRets.setStatus("mandatory")
_CntCpuMsgHolds_Type = Counter32
_CntCpuMsgHolds_Object = MibTableColumn
cntCpuMsgHolds = _CntCpuMsgHolds_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 16),
    _CntCpuMsgHolds_Type()
)
cntCpuMsgHolds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuMsgHolds.setStatus("mandatory")


class _CntCpuResetFlag_Type(Integer32):
    """Custom type cntCpuResetFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CntCpuResetFlag_Type.__name__ = "Integer32"
_CntCpuResetFlag_Object = MibTableColumn
cntCpuResetFlag = _CntCpuResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 17),
    _CntCpuResetFlag_Type()
)
cntCpuResetFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuResetFlag.setStatus("mandatory")
_CntCpuUtil_Type = Integer32
_CntCpuUtil_Object = MibTableColumn
cntCpuUtil = _CntCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 18),
    _CntCpuUtil_Type()
)
cntCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuUtil.setStatus("mandatory")
_CntCpuLastFailDate_Type = DisplayString
_CntCpuLastFailDate_Object = MibTableColumn
cntCpuLastFailDate = _CntCpuLastFailDate_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 19),
    _CntCpuLastFailDate_Type()
)
cntCpuLastFailDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuLastFailDate.setStatus("mandatory")
_CntCpuLastChgDate_Type = DisplayString
_CntCpuLastChgDate_Object = MibTableColumn
cntCpuLastChgDate = _CntCpuLastChgDate_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 15, 1, 20),
    _CntCpuLastChgDate_Type()
)
cntCpuLastChgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuLastChgDate.setStatus("mandatory")
_CntHwStatusLED_Type = Integer32
_CntHwStatusLED_Object = MibScalar
cntHwStatusLED = _CntHwStatusLED_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 4, 16),
    _CntHwStatusLED_Type()
)
cntHwStatusLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHwStatusLED.setStatus("mandatory")
_CntSysBuild_ObjectIdentity = ObjectIdentity
cntSysBuild = _CntSysBuild_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5)
)
_CntRevDate_Type = IpAddress
_CntRevDate_Object = MibScalar
cntRevDate = _CntRevDate_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 1),
    _CntRevDate_Type()
)
cntRevDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRevDate.setStatus("mandatory")
_CntCustomer_Type = DisplayString
_CntCustomer_Object = MibScalar
cntCustomer = _CntCustomer_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 2),
    _CntCustomer_Type()
)
cntCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCustomer.setStatus("mandatory")
_CntMachineType_Type = DisplayString
_CntMachineType_Object = MibScalar
cntMachineType = _CntMachineType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 3),
    _CntMachineType_Type()
)
cntMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMachineType.setStatus("mandatory")
_CntSerialNumber_Type = Integer32
_CntSerialNumber_Object = MibScalar
cntSerialNumber = _CntSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 4),
    _CntSerialNumber_Type()
)
cntSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSerialNumber.setStatus("mandatory")
_CntWorkOrderNumber_Type = Integer32
_CntWorkOrderNumber_Object = MibScalar
cntWorkOrderNumber = _CntWorkOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 5),
    _CntWorkOrderNumber_Type()
)
cntWorkOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntWorkOrderNumber.setStatus("mandatory")
_CntChassisNumber_Type = Integer32
_CntChassisNumber_Object = MibScalar
cntChassisNumber = _CntChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 6),
    _CntChassisNumber_Type()
)
cntChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntChassisNumber.setStatus("mandatory")
_CntModelNumber_Type = DisplayString
_CntModelNumber_Object = MibScalar
cntModelNumber = _CntModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 7),
    _CntModelNumber_Type()
)
cntModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntModelNumber.setStatus("mandatory")
_CntReleaseLevel_Type = DisplayString
_CntReleaseLevel_Object = MibScalar
cntReleaseLevel = _CntReleaseLevel_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 8),
    _CntReleaseLevel_Type()
)
cntReleaseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntReleaseLevel.setStatus("mandatory")
_CntRevEditDate_Type = IpAddress
_CntRevEditDate_Object = MibScalar
cntRevEditDate = _CntRevEditDate_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 9),
    _CntRevEditDate_Type()
)
cntRevEditDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRevEditDate.setStatus("mandatory")
_CntRevEditTime_Type = IpAddress
_CntRevEditTime_Object = MibScalar
cntRevEditTime = _CntRevEditTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 10),
    _CntRevEditTime_Type()
)
cntRevEditTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRevEditTime.setStatus("mandatory")
_CntFeatureTable_Object = MibTable
cntFeatureTable = _CntFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 11)
)
if mibBuilder.loadTexts:
    cntFeatureTable.setStatus("mandatory")
_CntFeatureEntry_Object = MibTableRow
cntFeatureEntry = _CntFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 11, 1)
)
cntFeatureEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntFeatureIndex"),
)
if mibBuilder.loadTexts:
    cntFeatureEntry.setStatus("mandatory")
_CntFeatureIndex_Type = Integer32
_CntFeatureIndex_Object = MibTableColumn
cntFeatureIndex = _CntFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 11, 1, 1),
    _CntFeatureIndex_Type()
)
cntFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFeatureIndex.setStatus("mandatory")
_CntFeatureName_Type = DisplayString
_CntFeatureName_Object = MibTableColumn
cntFeatureName = _CntFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 11, 1, 2),
    _CntFeatureName_Type()
)
cntFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFeatureName.setStatus("mandatory")
_CntFeatureQuantity_Type = Integer32
_CntFeatureQuantity_Object = MibTableColumn
cntFeatureQuantity = _CntFeatureQuantity_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 11, 1, 3),
    _CntFeatureQuantity_Type()
)
cntFeatureQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFeatureQuantity.setStatus("mandatory")
_CntFeatureDescr_Type = DisplayString
_CntFeatureDescr_Object = MibTableColumn
cntFeatureDescr = _CntFeatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 11, 1, 4),
    _CntFeatureDescr_Type()
)
cntFeatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFeatureDescr.setStatus("mandatory")
_CntSlotTable_Object = MibTable
cntSlotTable = _CntSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12)
)
if mibBuilder.loadTexts:
    cntSlotTable.setStatus("mandatory")
_CntSlotEntry_Object = MibTableRow
cntSlotEntry = _CntSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1)
)
cntSlotEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntSlotIndex"),
)
if mibBuilder.loadTexts:
    cntSlotEntry.setStatus("mandatory")
_CntSlotIndex_Type = Integer32
_CntSlotIndex_Object = MibTableColumn
cntSlotIndex = _CntSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 1),
    _CntSlotIndex_Type()
)
cntSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotIndex.setStatus("mandatory")
_CntSlotName_Type = DisplayString
_CntSlotName_Object = MibTableColumn
cntSlotName = _CntSlotName_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 2),
    _CntSlotName_Type()
)
cntSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotName.setStatus("mandatory")
_CntSlotPartNumber_Type = Integer32
_CntSlotPartNumber_Object = MibTableColumn
cntSlotPartNumber = _CntSlotPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 3),
    _CntSlotPartNumber_Type()
)
cntSlotPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotPartNumber.setStatus("mandatory")
_CntSlotSerialNumber_Type = Integer32
_CntSlotSerialNumber_Object = MibTableColumn
cntSlotSerialNumber = _CntSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 4),
    _CntSlotSerialNumber_Type()
)
cntSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotSerialNumber.setStatus("mandatory")
_CntSlotRevLevel_Type = DisplayString
_CntSlotRevLevel_Object = MibTableColumn
cntSlotRevLevel = _CntSlotRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 5),
    _CntSlotRevLevel_Type()
)
cntSlotRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotRevLevel.setStatus("mandatory")
_CntSlotInterface_Type = Integer32
_CntSlotInterface_Object = MibTableColumn
cntSlotInterface = _CntSlotInterface_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 6),
    _CntSlotInterface_Type()
)
cntSlotInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotInterface.setStatus("mandatory")


class _CntSlotCpuNumber_Type(Integer32):
    """Custom type cntSlotCpuNumber based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CntSlotCpuNumber_Type.__name__ = "Integer32"
_CntSlotCpuNumber_Object = MibTableColumn
cntSlotCpuNumber = _CntSlotCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 7),
    _CntSlotCpuNumber_Type()
)
cntSlotCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotCpuNumber.setStatus("mandatory")
_CntSlotVMEbusGrant_Type = Integer32
_CntSlotVMEbusGrant_Object = MibTableColumn
cntSlotVMEbusGrant = _CntSlotVMEbusGrant_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 12, 1, 8),
    _CntSlotVMEbusGrant_Type()
)
cntSlotVMEbusGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSlotVMEbusGrant.setStatus("mandatory")
_CntIOTable_Object = MibTable
cntIOTable = _CntIOTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13)
)
if mibBuilder.loadTexts:
    cntIOTable.setStatus("mandatory")
_CntIOEntry_Object = MibTableRow
cntIOEntry = _CntIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1)
)
cntIOEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntIOIndex"),
)
if mibBuilder.loadTexts:
    cntIOEntry.setStatus("mandatory")
_CntIOIndex_Type = Integer32
_CntIOIndex_Object = MibTableColumn
cntIOIndex = _CntIOIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1, 1),
    _CntIOIndex_Type()
)
cntIOIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIOIndex.setStatus("mandatory")
_CntIOName_Type = DisplayString
_CntIOName_Object = MibTableColumn
cntIOName = _CntIOName_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1, 2),
    _CntIOName_Type()
)
cntIOName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIOName.setStatus("mandatory")
_CntIOPartNumber_Type = Integer32
_CntIOPartNumber_Object = MibTableColumn
cntIOPartNumber = _CntIOPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1, 3),
    _CntIOPartNumber_Type()
)
cntIOPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIOPartNumber.setStatus("mandatory")
_CntIOSerialNumber_Type = Integer32
_CntIOSerialNumber_Object = MibTableColumn
cntIOSerialNumber = _CntIOSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1, 4),
    _CntIOSerialNumber_Type()
)
cntIOSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIOSerialNumber.setStatus("mandatory")
_CntIORevLevel_Type = DisplayString
_CntIORevLevel_Object = MibTableColumn
cntIORevLevel = _CntIORevLevel_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1, 5),
    _CntIORevLevel_Type()
)
cntIORevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIORevLevel.setStatus("mandatory")
_CntIOInterface_Type = Integer32
_CntIOInterface_Object = MibTableColumn
cntIOInterface = _CntIOInterface_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1, 6),
    _CntIOInterface_Type()
)
cntIOInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIOInterface.setStatus("mandatory")


class _CntIOCpuNumber_Type(Integer32):
    """Custom type cntIOCpuNumber based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CntIOCpuNumber_Type.__name__ = "Integer32"
_CntIOCpuNumber_Object = MibTableColumn
cntIOCpuNumber = _CntIOCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 13, 1, 7),
    _CntIOCpuNumber_Type()
)
cntIOCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIOCpuNumber.setStatus("mandatory")
_CntPowerTable_Object = MibTable
cntPowerTable = _CntPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 14)
)
if mibBuilder.loadTexts:
    cntPowerTable.setStatus("mandatory")
_CntPowerEntry_Object = MibTableRow
cntPowerEntry = _CntPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 14, 1)
)
cntPowerEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntPowerIndex"),
)
if mibBuilder.loadTexts:
    cntPowerEntry.setStatus("mandatory")
_CntPowerIndex_Type = Integer32
_CntPowerIndex_Object = MibTableColumn
cntPowerIndex = _CntPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 14, 1, 1),
    _CntPowerIndex_Type()
)
cntPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPowerIndex.setStatus("mandatory")
_CntPowerName_Type = DisplayString
_CntPowerName_Object = MibTableColumn
cntPowerName = _CntPowerName_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 14, 1, 2),
    _CntPowerName_Type()
)
cntPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPowerName.setStatus("mandatory")
_CntPowerPartNumber_Type = Integer32
_CntPowerPartNumber_Object = MibTableColumn
cntPowerPartNumber = _CntPowerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 14, 1, 3),
    _CntPowerPartNumber_Type()
)
cntPowerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPowerPartNumber.setStatus("mandatory")
_CntPowerSerialNumber_Type = Integer32
_CntPowerSerialNumber_Object = MibTableColumn
cntPowerSerialNumber = _CntPowerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 14, 1, 4),
    _CntPowerSerialNumber_Type()
)
cntPowerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPowerSerialNumber.setStatus("mandatory")
_CntPowerRevLevel_Type = DisplayString
_CntPowerRevLevel_Object = MibTableColumn
cntPowerRevLevel = _CntPowerRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 14, 1, 5),
    _CntPowerRevLevel_Type()
)
cntPowerRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPowerRevLevel.setStatus("mandatory")
_CntSCRTable_Object = MibTable
cntSCRTable = _CntSCRTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 15)
)
if mibBuilder.loadTexts:
    cntSCRTable.setStatus("mandatory")
_CntSCREntry_Object = MibTableRow
cntSCREntry = _CntSCREntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 15, 1)
)
cntSCREntry.setIndexNames(
    (0, "CNTAU-MIB", "cntSCRIndex"),
)
if mibBuilder.loadTexts:
    cntSCREntry.setStatus("mandatory")
_CntSCRIndex_Type = Integer32
_CntSCRIndex_Object = MibTableColumn
cntSCRIndex = _CntSCRIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 15, 1, 1),
    _CntSCRIndex_Type()
)
cntSCRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSCRIndex.setStatus("mandatory")
_CntSCRNumber_Type = Integer32
_CntSCRNumber_Object = MibTableColumn
cntSCRNumber = _CntSCRNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 15, 1, 2),
    _CntSCRNumber_Type()
)
cntSCRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSCRNumber.setStatus("mandatory")
_CntSerialAlfaNumber_Type = DisplayString
_CntSerialAlfaNumber_Object = MibScalar
cntSerialAlfaNumber = _CntSerialAlfaNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 5, 16),
    _CntSerialAlfaNumber_Type()
)
cntSerialAlfaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSerialAlfaNumber.setStatus("mandatory")
_CntSysMemory_ObjectIdentity = ObjectIdentity
cntSysMemory = _CntSysMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 6)
)
_CntMemBBramAddress_Type = Integer32
_CntMemBBramAddress_Object = MibScalar
cntMemBBramAddress = _CntMemBBramAddress_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 6, 1),
    _CntMemBBramAddress_Type()
)
cntMemBBramAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMemBBramAddress.setStatus("mandatory")
_CntMemBBramSpace_Type = Integer32
_CntMemBBramSpace_Object = MibScalar
cntMemBBramSpace = _CntMemBBramSpace_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 6, 2),
    _CntMemBBramSpace_Type()
)
cntMemBBramSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMemBBramSpace.setStatus("mandatory")
_CntMemBBramFree_Type = Integer32
_CntMemBBramFree_Object = MibScalar
cntMemBBramFree = _CntMemBBramFree_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 6, 3),
    _CntMemBBramFree_Type()
)
cntMemBBramFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMemBBramFree.setStatus("mandatory")
_CntMemSramAddress_Type = Integer32
_CntMemSramAddress_Object = MibScalar
cntMemSramAddress = _CntMemSramAddress_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 6, 4),
    _CntMemSramAddress_Type()
)
cntMemSramAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMemSramAddress.setStatus("mandatory")
_CntMemSramSpace_Type = Integer32
_CntMemSramSpace_Object = MibScalar
cntMemSramSpace = _CntMemSramSpace_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 6, 5),
    _CntMemSramSpace_Type()
)
cntMemSramSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMemSramSpace.setStatus("mandatory")
_CntMemSramFree_Type = Integer32
_CntMemSramFree_Object = MibScalar
cntMemSramFree = _CntMemSramFree_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 6, 6),
    _CntMemSramFree_Type()
)
cntMemSramFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMemSramFree.setStatus("mandatory")
_CntSysCpuTable_Object = MibTable
cntSysCpuTable = _CntSysCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cntSysCpuTable.setStatus("mandatory")
_CntSysCpuEntry_Object = MibTableRow
cntSysCpuEntry = _CntSysCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1)
)
cntSysCpuEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntCpuIndex"),
)
if mibBuilder.loadTexts:
    cntSysCpuEntry.setStatus("mandatory")


class _CntCpuIndex_Type(Integer32):
    """Custom type cntCpuIndex based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CntCpuIndex_Type.__name__ = "Integer32"
_CntCpuIndex_Object = MibTableColumn
cntCpuIndex = _CntCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1, 1),
    _CntCpuIndex_Type()
)
cntCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuIndex.setStatus("mandatory")
_CntCpuMemSpace_Type = Integer32
_CntCpuMemSpace_Object = MibTableColumn
cntCpuMemSpace = _CntCpuMemSpace_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1, 2),
    _CntCpuMemSpace_Type()
)
cntCpuMemSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuMemSpace.setStatus("mandatory")
_CntCpuMemFree_Type = Integer32
_CntCpuMemFree_Object = MibTableColumn
cntCpuMemFree = _CntCpuMemFree_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1, 3),
    _CntCpuMemFree_Type()
)
cntCpuMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuMemFree.setStatus("mandatory")
_CntCpuTaskTable_Object = MibTable
cntCpuTaskTable = _CntCpuTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    cntCpuTaskTable.setStatus("mandatory")
_CntCpuTaskEntry_Object = MibTableRow
cntCpuTaskEntry = _CntCpuTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1, 4, 1)
)
cntCpuTaskEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntCpuTaskIndex"),
)
if mibBuilder.loadTexts:
    cntCpuTaskEntry.setStatus("mandatory")
_CntCpuTaskIndex_Type = Integer32
_CntCpuTaskIndex_Object = MibTableColumn
cntCpuTaskIndex = _CntCpuTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1, 4, 1, 1),
    _CntCpuTaskIndex_Type()
)
cntCpuTaskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuTaskIndex.setStatus("mandatory")
_CntCpuTaskName_Type = DisplayString
_CntCpuTaskName_Object = MibTableColumn
cntCpuTaskName = _CntCpuTaskName_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 1, 7, 1, 4, 1, 2),
    _CntCpuTaskName_Type()
)
cntCpuTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCpuTaskName.setStatus("mandatory")
_Cntinterfaces_ObjectIdentity = ObjectIdentity
cntinterfaces = _Cntinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 2)
)
_CntifTable_Object = MibTable
cntifTable = _CntifTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cntifTable.setStatus("mandatory")
_CntifEntry_Object = MibTableRow
cntifEntry = _CntifEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 2, 1, 1)
)
cntifEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntifIndex"),
)
if mibBuilder.loadTexts:
    cntifEntry.setStatus("mandatory")
_CntifIndex_Type = Integer32
_CntifIndex_Object = MibTableColumn
cntifIndex = _CntifIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 2, 1, 1, 1),
    _CntifIndex_Type()
)
cntifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntifIndex.setStatus("mandatory")


class _CntifType_Type(Integer32):
    """Custom type cntifType based on Integer32"""
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
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("atm", 61),
          ("basicIsdn", 20),
          ("cept", 19),
          ("channel-to-channel", 38),
          ("cray-hyperchannel", 46),
          ("crayfullduplex", 36),
          ("ddn-x25", 4),
          ("ds3", 30),
          ("dual-trunk", 44),
          ("eon", 25),
          ("escon-host", 50),
          ("escon-peripheral", 51),
          ("escon-srdf", 63),
          ("ethernet", 6),
          ("ethernet-3Mbit", 26),
          ("ethernet-geni", 59),
          ("ethernet88023", 7),
          ("fddi", 15),
          ("fddi-ss", 55),
          ("fibre-trunk", 34),
          ("frame-relay", 32),
          ("hdh1822", 3),
          ("hippi", 35),
          ("hssi-dce", 42),
          ("hssi-dte", 33),
          ("hssi-ss", 56),
          ("hyperchannel", 14),
          ("ibm-channel", 43),
          ("lapb", 16),
          ("maintenance", 22),
          ("nsip", 27),
          ("other", 1),
          ("peripheral-gateway", 39),
          ("ppp", 23),
          ("ppp-async", 49),
          ("primaryIsdn", 21),
          ("proteon-10MBit", 12),
          ("proteon-80MBit", 13),
          ("pt-to-pt-fiber", 37),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("scsi-initiator", 62),
          ("scsi-target", 47),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("smds", 10),
          ("snmp-gateway", 48),
          ("sofwareLoopback", 24),
          ("stackstarter", 58),
          ("starLan", 11),
          ("t1", 18),
          ("tape-dasd", 41),
          ("tape-pipelining", 40),
          ("tapecontrol-rs232", 52),
          ("teradata", 45),
          ("tokenBus", 8),
          ("tokenRing", 9),
          ("tokenring-geni", 60),
          ("tunneling", 57),
          ("ultra", 29),
          ("ultra-dce", 54),
          ("ultra-dte", 53))
    )


_CntifType_Type.__name__ = "Integer32"
_CntifType_Object = MibTableColumn
cntifType = _CntifType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 2, 1, 1, 2),
    _CntifType_Type()
)
cntifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntifType.setStatus("mandatory")


class _CntifCpu_Type(Integer32):
    """Custom type cntifCpu based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CntifCpu_Type.__name__ = "Integer32"
_CntifCpu_Object = MibTableColumn
cntifCpu = _CntifCpu_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 2, 1, 1, 3),
    _CntifCpu_Type()
)
cntifCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntifCpu.setStatus("mandatory")
_CntifSubIndex_Type = Integer32
_CntifSubIndex_Object = MibTableColumn
cntifSubIndex = _CntifSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 2, 1, 1, 4),
    _CntifSubIndex_Type()
)
cntifSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntifSubIndex.setStatus("mandatory")
_CntIfsState_Type = Integer32
_CntIfsState_Object = MibScalar
cntIfsState = _CntIfsState_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 2, 2),
    _CntIfsState_Type()
)
cntIfsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIfsState.setStatus("mandatory")
_Cnticmp_ObjectIdentity = ObjectIdentity
cnticmp = _Cnticmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 5)
)
_CnticmpInDuNets_Type = Counter32
_CnticmpInDuNets_Object = MibScalar
cnticmpInDuNets = _CnticmpInDuNets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 1),
    _CnticmpInDuNets_Type()
)
cnticmpInDuNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInDuNets.setStatus("mandatory")
_CnticmpInDuHosts_Type = Counter32
_CnticmpInDuHosts_Object = MibScalar
cnticmpInDuHosts = _CnticmpInDuHosts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 2),
    _CnticmpInDuHosts_Type()
)
cnticmpInDuHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInDuHosts.setStatus("mandatory")
_CnticmpInDuProtos_Type = Counter32
_CnticmpInDuProtos_Object = MibScalar
cnticmpInDuProtos = _CnticmpInDuProtos_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 3),
    _CnticmpInDuProtos_Type()
)
cnticmpInDuProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInDuProtos.setStatus("mandatory")
_CnticmpInDuPorts_Type = Counter32
_CnticmpInDuPorts_Object = MibScalar
cnticmpInDuPorts = _CnticmpInDuPorts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 4),
    _CnticmpInDuPorts_Type()
)
cnticmpInDuPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInDuPorts.setStatus("mandatory")
_CnticmpInDuFrags_Type = Counter32
_CnticmpInDuFrags_Object = MibScalar
cnticmpInDuFrags = _CnticmpInDuFrags_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 5),
    _CnticmpInDuFrags_Type()
)
cnticmpInDuFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInDuFrags.setStatus("mandatory")
_CnticmpInDuSources_Type = Counter32
_CnticmpInDuSources_Object = MibScalar
cnticmpInDuSources = _CnticmpInDuSources_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 6),
    _CnticmpInDuSources_Type()
)
cnticmpInDuSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInDuSources.setStatus("mandatory")
_CnticmpInTmXceeds_Type = Counter32
_CnticmpInTmXceeds_Object = MibScalar
cnticmpInTmXceeds = _CnticmpInTmXceeds_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 7),
    _CnticmpInTmXceeds_Type()
)
cnticmpInTmXceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInTmXceeds.setStatus("mandatory")
_CnticmpInTmFrags_Type = Counter32
_CnticmpInTmFrags_Object = MibScalar
cnticmpInTmFrags = _CnticmpInTmFrags_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 8),
    _CnticmpInTmFrags_Type()
)
cnticmpInTmFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInTmFrags.setStatus("mandatory")
_CnticmpInReNets_Type = Counter32
_CnticmpInReNets_Object = MibScalar
cnticmpInReNets = _CnticmpInReNets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 9),
    _CnticmpInReNets_Type()
)
cnticmpInReNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInReNets.setStatus("mandatory")
_CnticmpInReHosts_Type = Counter32
_CnticmpInReHosts_Object = MibScalar
cnticmpInReHosts = _CnticmpInReHosts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 10),
    _CnticmpInReHosts_Type()
)
cnticmpInReHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInReHosts.setStatus("mandatory")
_CnticmpInReServnets_Type = Counter32
_CnticmpInReServnets_Object = MibScalar
cnticmpInReServnets = _CnticmpInReServnets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 11),
    _CnticmpInReServnets_Type()
)
cnticmpInReServnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInReServnets.setStatus("mandatory")
_CnticmpInReServhosts_Type = Counter32
_CnticmpInReServhosts_Object = MibScalar
cnticmpInReServhosts = _CnticmpInReServhosts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 12),
    _CnticmpInReServhosts_Type()
)
cnticmpInReServhosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpInReServhosts.setStatus("mandatory")
_CnticmpOutDuNets_Type = Counter32
_CnticmpOutDuNets_Object = MibScalar
cnticmpOutDuNets = _CnticmpOutDuNets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 13),
    _CnticmpOutDuNets_Type()
)
cnticmpOutDuNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutDuNets.setStatus("mandatory")
_CnticmpOutDuHosts_Type = Counter32
_CnticmpOutDuHosts_Object = MibScalar
cnticmpOutDuHosts = _CnticmpOutDuHosts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 14),
    _CnticmpOutDuHosts_Type()
)
cnticmpOutDuHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutDuHosts.setStatus("mandatory")
_CnticmpOutDuProtos_Type = Counter32
_CnticmpOutDuProtos_Object = MibScalar
cnticmpOutDuProtos = _CnticmpOutDuProtos_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 15),
    _CnticmpOutDuProtos_Type()
)
cnticmpOutDuProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutDuProtos.setStatus("mandatory")
_CnticmpOutDuPorts_Type = Counter32
_CnticmpOutDuPorts_Object = MibScalar
cnticmpOutDuPorts = _CnticmpOutDuPorts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 16),
    _CnticmpOutDuPorts_Type()
)
cnticmpOutDuPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutDuPorts.setStatus("mandatory")
_CnticmpOutDuFrags_Type = Counter32
_CnticmpOutDuFrags_Object = MibScalar
cnticmpOutDuFrags = _CnticmpOutDuFrags_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 17),
    _CnticmpOutDuFrags_Type()
)
cnticmpOutDuFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutDuFrags.setStatus("mandatory")
_CnticmpOutDuSources_Type = Counter32
_CnticmpOutDuSources_Object = MibScalar
cnticmpOutDuSources = _CnticmpOutDuSources_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 18),
    _CnticmpOutDuSources_Type()
)
cnticmpOutDuSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutDuSources.setStatus("mandatory")
_CnticmpOutTmXceeds_Type = Counter32
_CnticmpOutTmXceeds_Object = MibScalar
cnticmpOutTmXceeds = _CnticmpOutTmXceeds_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 19),
    _CnticmpOutTmXceeds_Type()
)
cnticmpOutTmXceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutTmXceeds.setStatus("mandatory")
_CnticmpOutTmFrags_Type = Counter32
_CnticmpOutTmFrags_Object = MibScalar
cnticmpOutTmFrags = _CnticmpOutTmFrags_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 20),
    _CnticmpOutTmFrags_Type()
)
cnticmpOutTmFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutTmFrags.setStatus("mandatory")
_CnticmpOutReNets_Type = Counter32
_CnticmpOutReNets_Object = MibScalar
cnticmpOutReNets = _CnticmpOutReNets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 21),
    _CnticmpOutReNets_Type()
)
cnticmpOutReNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutReNets.setStatus("mandatory")
_CnticmpOutReHosts_Type = Counter32
_CnticmpOutReHosts_Object = MibScalar
cnticmpOutReHosts = _CnticmpOutReHosts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 22),
    _CnticmpOutReHosts_Type()
)
cnticmpOutReHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutReHosts.setStatus("mandatory")
_CnticmpOutReServnets_Type = Counter32
_CnticmpOutReServnets_Object = MibScalar
cnticmpOutReServnets = _CnticmpOutReServnets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 23),
    _CnticmpOutReServnets_Type()
)
cnticmpOutReServnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutReServnets.setStatus("mandatory")
_CnticmpOutReServhosts_Type = Counter32
_CnticmpOutReServhosts_Object = MibScalar
cnticmpOutReServhosts = _CnticmpOutReServhosts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 5, 24),
    _CnticmpOutReServhosts_Type()
)
cnticmpOutReServhosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnticmpOutReServhosts.setStatus("mandatory")
_Cnttransmission_ObjectIdentity = ObjectIdentity
cnttransmission = _Cnttransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 10)
)
_Cntdot3_ObjectIdentity = ObjectIdentity
cntdot3 = _Cntdot3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1)
)
_Cntdot3Table_Object = MibTable
cntdot3Table = _Cntdot3Table_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    cntdot3Table.setStatus("mandatory")
_Cntdot3Entry_Object = MibTableRow
cntdot3Entry = _Cntdot3Entry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1)
)
cntdot3Entry.setIndexNames(
    (0, "CNTAU-MIB", "cntdot3Index"),
)
if mibBuilder.loadTexts:
    cntdot3Entry.setStatus("mandatory")
_Cntdot3Index_Type = Integer32
_Cntdot3Index_Object = MibTableColumn
cntdot3Index = _Cntdot3Index_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 1),
    _Cntdot3Index_Type()
)
cntdot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3Index.setStatus("mandatory")
_Cntdot3SoftwareID_Type = IpAddress
_Cntdot3SoftwareID_Object = MibTableColumn
cntdot3SoftwareID = _Cntdot3SoftwareID_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 2),
    _Cntdot3SoftwareID_Type()
)
cntdot3SoftwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3SoftwareID.setStatus("mandatory")
_Cntdot3BufsAllocated_Type = Integer32
_Cntdot3BufsAllocated_Object = MibTableColumn
cntdot3BufsAllocated = _Cntdot3BufsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 3),
    _Cntdot3BufsAllocated_Type()
)
cntdot3BufsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3BufsAllocated.setStatus("mandatory")
_Cntdot3BufTooManys_Type = Counter32
_Cntdot3BufTooManys_Object = MibTableColumn
cntdot3BufTooManys = _Cntdot3BufTooManys_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 4),
    _Cntdot3BufTooManys_Type()
)
cntdot3BufTooManys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3BufTooManys.setStatus("mandatory")
_Cntdot3BufNotAvails_Type = Counter32
_Cntdot3BufNotAvails_Object = MibTableColumn
cntdot3BufNotAvails = _Cntdot3BufNotAvails_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 5),
    _Cntdot3BufNotAvails_Type()
)
cntdot3BufNotAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3BufNotAvails.setStatus("mandatory")
_Cntdot3BufPriority_Type = Integer32
_Cntdot3BufPriority_Object = MibTableColumn
cntdot3BufPriority = _Cntdot3BufPriority_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 6),
    _Cntdot3BufPriority_Type()
)
cntdot3BufPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3BufPriority.setStatus("mandatory")
_Cntdot3PICBusErrs_Type = Counter32
_Cntdot3PICBusErrs_Object = MibTableColumn
cntdot3PICBusErrs = _Cntdot3PICBusErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 7),
    _Cntdot3PICBusErrs_Type()
)
cntdot3PICBusErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3PICBusErrs.setStatus("mandatory")
_Cntdot3PICDMAErrs_Type = Counter32
_Cntdot3PICDMAErrs_Object = MibTableColumn
cntdot3PICDMAErrs = _Cntdot3PICDMAErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 8),
    _Cntdot3PICDMAErrs_Type()
)
cntdot3PICDMAErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3PICDMAErrs.setStatus("mandatory")
_Cntdot3PICMemSeqErrs_Type = Counter32
_Cntdot3PICMemSeqErrs_Object = MibTableColumn
cntdot3PICMemSeqErrs = _Cntdot3PICMemSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 9),
    _Cntdot3PICMemSeqErrs_Type()
)
cntdot3PICMemSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3PICMemSeqErrs.setStatus("mandatory")
_Cntdot3PICMemParityErrs_Type = Counter32
_Cntdot3PICMemParityErrs_Object = MibTableColumn
cntdot3PICMemParityErrs = _Cntdot3PICMemParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 10),
    _Cntdot3PICMemParityErrs_Type()
)
cntdot3PICMemParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3PICMemParityErrs.setStatus("mandatory")
_Cntdot3PICSpuriousInts_Type = Counter32
_Cntdot3PICSpuriousInts_Object = MibTableColumn
cntdot3PICSpuriousInts = _Cntdot3PICSpuriousInts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 11),
    _Cntdot3PICSpuriousInts_Type()
)
cntdot3PICSpuriousInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3PICSpuriousInts.setStatus("mandatory")
_Cntdot3LanceInts_Type = Counter32
_Cntdot3LanceInts_Object = MibTableColumn
cntdot3LanceInts = _Cntdot3LanceInts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 12),
    _Cntdot3LanceInts_Type()
)
cntdot3LanceInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LanceInts.setStatus("mandatory")
_Cntdot3LanceParityErrs_Type = Counter32
_Cntdot3LanceParityErrs_Object = MibTableColumn
cntdot3LanceParityErrs = _Cntdot3LanceParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 13),
    _Cntdot3LanceParityErrs_Type()
)
cntdot3LanceParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LanceParityErrs.setStatus("mandatory")
_Cntdot3LanceMemErrs_Type = Counter32
_Cntdot3LanceMemErrs_Object = MibTableColumn
cntdot3LanceMemErrs = _Cntdot3LanceMemErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 14),
    _Cntdot3LanceMemErrs_Type()
)
cntdot3LanceMemErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LanceMemErrs.setStatus("mandatory")
_Cntdot3LanceMissedPkts_Type = Counter32
_Cntdot3LanceMissedPkts_Object = MibTableColumn
cntdot3LanceMissedPkts = _Cntdot3LanceMissedPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 15),
    _Cntdot3LanceMissedPkts_Type()
)
cntdot3LanceMissedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LanceMissedPkts.setStatus("mandatory")
_Cntdot3LanceUnderFlows_Type = Counter32
_Cntdot3LanceUnderFlows_Object = MibTableColumn
cntdot3LanceUnderFlows = _Cntdot3LanceUnderFlows_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 16),
    _Cntdot3LanceUnderFlows_Type()
)
cntdot3LanceUnderFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LanceUnderFlows.setStatus("mandatory")
_Cntdot3LanceOverFlows_Type = Counter32
_Cntdot3LanceOverFlows_Object = MibTableColumn
cntdot3LanceOverFlows = _Cntdot3LanceOverFlows_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 17),
    _Cntdot3LanceOverFlows_Type()
)
cntdot3LanceOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LanceOverFlows.setStatus("mandatory")
_Cntdot3LanceTxWaitQ_Type = Integer32
_Cntdot3LanceTxWaitQ_Object = MibTableColumn
cntdot3LanceTxWaitQ = _Cntdot3LanceTxWaitQ_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 18),
    _Cntdot3LanceTxWaitQ_Type()
)
cntdot3LanceTxWaitQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LanceTxWaitQ.setStatus("mandatory")


class _Cntdot3DMAChan1RxErr_Type(Integer32):
    """Custom type cntdot3DMAChan1RxErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              6,
              7,
              9,
              10,
              11,
              13,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("address-bar", 7),
          ("address-dar", 6),
          ("address-mar", 5),
          ("buserr-bar", 11),
          ("buserr-dar", 10),
          ("buserr-mar", 9),
          ("config", 1),
          ("count-btc", 15),
          ("count-mtc", 13),
          ("external-abort", 16),
          ("external-software-abort", 17),
          ("no-error", 0),
          ("operation-timing", 2))
    )


_Cntdot3DMAChan1RxErr_Type.__name__ = "Integer32"
_Cntdot3DMAChan1RxErr_Object = MibTableColumn
cntdot3DMAChan1RxErr = _Cntdot3DMAChan1RxErr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 19),
    _Cntdot3DMAChan1RxErr_Type()
)
cntdot3DMAChan1RxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan1RxErr.setStatus("mandatory")


class _Cntdot3DMAChan3RxErr_Type(Integer32):
    """Custom type cntdot3DMAChan3RxErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              10,
              11,
              12,
              14,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("address-bar", 8),
          ("address-dar", 7),
          ("address-mar", 6),
          ("buserr-bar", 12),
          ("buserr-dar", 11),
          ("buserr-mar", 10),
          ("config", 2),
          ("count-btc", 16),
          ("count-mtc", 14),
          ("external-abort", 17),
          ("external-software-abort", 18),
          ("no-error", 1),
          ("operation-timing", 3))
    )


_Cntdot3DMAChan3RxErr_Type.__name__ = "Integer32"
_Cntdot3DMAChan3RxErr_Object = MibTableColumn
cntdot3DMAChan3RxErr = _Cntdot3DMAChan3RxErr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 20),
    _Cntdot3DMAChan3RxErr_Type()
)
cntdot3DMAChan3RxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan3RxErr.setStatus("mandatory")


class _Cntdot3DMAChan0TxErr_Type(Integer32):
    """Custom type cntdot3DMAChan0TxErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              10,
              11,
              12,
              14,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("address-bar", 8),
          ("address-dar", 7),
          ("address-mar", 6),
          ("buserr-bar", 12),
          ("buserr-dar", 11),
          ("buserr-mar", 10),
          ("config", 2),
          ("count-btc", 16),
          ("count-mtc", 14),
          ("external-abort", 17),
          ("external-software-abort", 18),
          ("no-error", 1),
          ("operation-timing", 3))
    )


_Cntdot3DMAChan0TxErr_Type.__name__ = "Integer32"
_Cntdot3DMAChan0TxErr_Object = MibTableColumn
cntdot3DMAChan0TxErr = _Cntdot3DMAChan0TxErr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 21),
    _Cntdot3DMAChan0TxErr_Type()
)
cntdot3DMAChan0TxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan0TxErr.setStatus("mandatory")


class _Cntdot3DMAChan2TxErr_Type(Integer32):
    """Custom type cntdot3DMAChan2TxErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              10,
              11,
              12,
              14,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("address-bar", 8),
          ("address-dar", 7),
          ("address-mar", 6),
          ("buserr-bar", 12),
          ("buserr-dar", 11),
          ("buserr-mar", 10),
          ("config", 2),
          ("count-btc", 16),
          ("count-mtc", 14),
          ("external-abort", 17),
          ("external-software-abort", 18),
          ("no-error", 1),
          ("operation-timing", 3))
    )


_Cntdot3DMAChan2TxErr_Type.__name__ = "Integer32"
_Cntdot3DMAChan2TxErr_Object = MibTableColumn
cntdot3DMAChan2TxErr = _Cntdot3DMAChan2TxErr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 22),
    _Cntdot3DMAChan2TxErr_Type()
)
cntdot3DMAChan2TxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan2TxErr.setStatus("mandatory")
_Cntdot3DMAChan1RxErrs_Type = Counter32
_Cntdot3DMAChan1RxErrs_Object = MibTableColumn
cntdot3DMAChan1RxErrs = _Cntdot3DMAChan1RxErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 23),
    _Cntdot3DMAChan1RxErrs_Type()
)
cntdot3DMAChan1RxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan1RxErrs.setStatus("mandatory")
_Cntdot3DMAChan3RxErrs_Type = Counter32
_Cntdot3DMAChan3RxErrs_Object = MibTableColumn
cntdot3DMAChan3RxErrs = _Cntdot3DMAChan3RxErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 24),
    _Cntdot3DMAChan3RxErrs_Type()
)
cntdot3DMAChan3RxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan3RxErrs.setStatus("mandatory")
_Cntdot3DMAChan0TxErrs_Type = Counter32
_Cntdot3DMAChan0TxErrs_Object = MibTableColumn
cntdot3DMAChan0TxErrs = _Cntdot3DMAChan0TxErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 25),
    _Cntdot3DMAChan0TxErrs_Type()
)
cntdot3DMAChan0TxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan0TxErrs.setStatus("mandatory")
_Cntdot3DMAChan2TxErrs_Type = Counter32
_Cntdot3DMAChan2TxErrs_Object = MibTableColumn
cntdot3DMAChan2TxErrs = _Cntdot3DMAChan2TxErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 26),
    _Cntdot3DMAChan2TxErrs_Type()
)
cntdot3DMAChan2TxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMAChan2TxErrs.setStatus("mandatory")
_Cntdot3DMARxWaitQ_Type = Integer32
_Cntdot3DMARxWaitQ_Object = MibTableColumn
cntdot3DMARxWaitQ = _Cntdot3DMARxWaitQ_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 27),
    _Cntdot3DMARxWaitQ_Type()
)
cntdot3DMARxWaitQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMARxWaitQ.setStatus("mandatory")
_Cntdot3DMATxWaitQ_Type = Integer32
_Cntdot3DMATxWaitQ_Object = MibTableColumn
cntdot3DMATxWaitQ = _Cntdot3DMATxWaitQ_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 28),
    _Cntdot3DMATxWaitQ_Type()
)
cntdot3DMATxWaitQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3DMATxWaitQ.setStatus("mandatory")
_Cntdot3LPXParityErrs_Type = Counter32
_Cntdot3LPXParityErrs_Object = MibTableColumn
cntdot3LPXParityErrs = _Cntdot3LPXParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 29),
    _Cntdot3LPXParityErrs_Type()
)
cntdot3LPXParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3LPXParityErrs.setStatus("mandatory")
_Cntdot3Chan1Misreads_Type = Counter32
_Cntdot3Chan1Misreads_Object = MibTableColumn
cntdot3Chan1Misreads = _Cntdot3Chan1Misreads_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 1, 1, 1, 30),
    _Cntdot3Chan1Misreads_Type()
)
cntdot3Chan1Misreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdot3Chan1Misreads.setStatus("mandatory")
_Cntfddi_ObjectIdentity = ObjectIdentity
cntfddi = _Cntfddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2)
)
_CntFddiSMT_ObjectIdentity = ObjectIdentity
cntFddiSMT = _CntFddiSMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1)
)


class _CntFddiSMTNumber_Type(Integer32):
    """Custom type cntFddiSMTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CntFddiSMTNumber_Type.__name__ = "Integer32"
_CntFddiSMTNumber_Object = MibScalar
cntFddiSMTNumber = _CntFddiSMTNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 1),
    _CntFddiSMTNumber_Type()
)
cntFddiSMTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTNumber.setStatus("mandatory")
_CntFddiSMTTable_Object = MibTable
cntFddiSMTTable = _CntFddiSMTTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cntFddiSMTTable.setStatus("mandatory")
_CntFddiSMTEntry_Object = MibTableRow
cntFddiSMTEntry = _CntFddiSMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1)
)
cntFddiSMTEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntFddiSMTIndex"),
)
if mibBuilder.loadTexts:
    cntFddiSMTEntry.setStatus("mandatory")


class _CntFddiSMTIndex_Type(Integer32):
    """Custom type cntFddiSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntFddiSMTIndex_Type.__name__ = "Integer32"
_CntFddiSMTIndex_Object = MibTableColumn
cntFddiSMTIndex = _CntFddiSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 1),
    _CntFddiSMTIndex_Type()
)
cntFddiSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTIndex.setStatus("mandatory")
_CntFddiSMTManufacturerData_Type = OctetString
_CntFddiSMTManufacturerData_Object = MibTableColumn
cntFddiSMTManufacturerData = _CntFddiSMTManufacturerData_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 2),
    _CntFddiSMTManufacturerData_Type()
)
cntFddiSMTManufacturerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTManufacturerData.setStatus("optional")
_CntFddiSMTUserData_Type = OctetString
_CntFddiSMTUserData_Object = MibTableColumn
cntFddiSMTUserData = _CntFddiSMTUserData_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 3),
    _CntFddiSMTUserData_Type()
)
cntFddiSMTUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTUserData.setStatus("optional")
_CntFddiSMTReportLimit_Type = Integer32
_CntFddiSMTReportLimit_Object = MibTableColumn
cntFddiSMTReportLimit = _CntFddiSMTReportLimit_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 4),
    _CntFddiSMTReportLimit_Type()
)
cntFddiSMTReportLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTReportLimit.setStatus("optional")
_CntFddiSMTMsgTimeStamp_Type = OctetString
_CntFddiSMTMsgTimeStamp_Object = MibTableColumn
cntFddiSMTMsgTimeStamp = _CntFddiSMTMsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 5),
    _CntFddiSMTMsgTimeStamp_Type()
)
cntFddiSMTMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTMsgTimeStamp.setStatus("mandatory")
_CntFddiSMTTransitionTimeStamp_Type = OctetString
_CntFddiSMTTransitionTimeStamp_Object = MibTableColumn
cntFddiSMTTransitionTimeStamp = _CntFddiSMTTransitionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 6),
    _CntFddiSMTTransitionTimeStamp_Type()
)
cntFddiSMTTransitionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTTransitionTimeStamp.setStatus("mandatory")
_CntFddiSMTSetCount_Type = OctetString
_CntFddiSMTSetCount_Object = MibTableColumn
cntFddiSMTSetCount = _CntFddiSMTSetCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 7),
    _CntFddiSMTSetCount_Type()
)
cntFddiSMTSetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTSetCount.setStatus("optional")
_CntFddiSMTLastSetStationID_Type = OctetString
_CntFddiSMTLastSetStationID_Object = MibTableColumn
cntFddiSMTLastSetStationID = _CntFddiSMTLastSetStationID_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 1, 2, 1, 8),
    _CntFddiSMTLastSetStationID_Type()
)
cntFddiSMTLastSetStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiSMTLastSetStationID.setStatus("optional")
_CntFddiMAC_ObjectIdentity = ObjectIdentity
cntFddiMAC = _CntFddiMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2)
)
_CntFddiMACNumber_Type = Integer32
_CntFddiMACNumber_Object = MibScalar
cntFddiMACNumber = _CntFddiMACNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 1),
    _CntFddiMACNumber_Type()
)
cntFddiMACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACNumber.setStatus("mandatory")
_CntFddiMACTable_Object = MibTable
cntFddiMACTable = _CntFddiMACTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cntFddiMACTable.setStatus("mandatory")
_CntFddiMACEntry_Object = MibTableRow
cntFddiMACEntry = _CntFddiMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1)
)
cntFddiMACEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntFddiMACSMTIndex"),
)
if mibBuilder.loadTexts:
    cntFddiMACEntry.setStatus("mandatory")


class _CntFddiMACSMTIndex_Type(Integer32):
    """Custom type cntFddiMACSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntFddiMACSMTIndex_Type.__name__ = "Integer32"
_CntFddiMACSMTIndex_Object = MibTableColumn
cntFddiMACSMTIndex = _CntFddiMACSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 1),
    _CntFddiMACSMTIndex_Type()
)
cntFddiMACSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACSMTIndex.setStatus("mandatory")


class _CntFddiMACIndex_Type(Integer32):
    """Custom type cntFddiMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntFddiMACIndex_Type.__name__ = "Integer32"
_CntFddiMACIndex_Object = MibTableColumn
cntFddiMACIndex = _CntFddiMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 2),
    _CntFddiMACIndex_Type()
)
cntFddiMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACIndex.setStatus("mandatory")
_CntFddiMACBridgeFunction_Type = Integer32
_CntFddiMACBridgeFunction_Object = MibTableColumn
cntFddiMACBridgeFunction = _CntFddiMACBridgeFunction_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 3),
    _CntFddiMACBridgeFunction_Type()
)
cntFddiMACBridgeFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBridgeFunction.setStatus("optional")
_CntFddiMACDownstreamNbr_Type = OctetString
_CntFddiMACDownstreamNbr_Object = MibTableColumn
cntFddiMACDownstreamNbr = _CntFddiMACDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 4),
    _CntFddiMACDownstreamNbr_Type()
)
cntFddiMACDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACDownstreamNbr.setStatus("optional")
_CntFddiMACOldDownstreamNbr_Type = OctetString
_CntFddiMACOldDownstreamNbr_Object = MibTableColumn
cntFddiMACOldDownstreamNbr = _CntFddiMACOldDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 5),
    _CntFddiMACOldDownstreamNbr_Type()
)
cntFddiMACOldDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACOldDownstreamNbr.setStatus("optional")
_CntFddiMACRootConcentratorMac_Type = Integer32
_CntFddiMACRootConcentratorMac_Object = MibTableColumn
cntFddiMACRootConcentratorMac = _CntFddiMACRootConcentratorMac_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 6),
    _CntFddiMACRootConcentratorMac_Type()
)
cntFddiMACRootConcentratorMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACRootConcentratorMac.setStatus("optional")
_CntFddiMACLongAlias_Type = Integer32
_CntFddiMACLongAlias_Object = MibTableColumn
cntFddiMACLongAlias = _CntFddiMACLongAlias_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 7),
    _CntFddiMACLongAlias_Type()
)
cntFddiMACLongAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACLongAlias.setStatus("optional")
_CntFddiMACShortAlias_Type = Integer32
_CntFddiMACShortAlias_Object = MibTableColumn
cntFddiMACShortAlias = _CntFddiMACShortAlias_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 8),
    _CntFddiMACShortAlias_Type()
)
cntFddiMACShortAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACShortAlias.setStatus("optional")
_CntFddiMACLongGrpAddr_Type = Integer32
_CntFddiMACLongGrpAddr_Object = MibTableColumn
cntFddiMACLongGrpAddr = _CntFddiMACLongGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 9),
    _CntFddiMACLongGrpAddr_Type()
)
cntFddiMACLongGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACLongGrpAddr.setStatus("optional")
_CntFddiMACShortGrpAddr_Type = Integer32
_CntFddiMACShortGrpAddr_Object = MibTableColumn
cntFddiMACShortGrpAddr = _CntFddiMACShortGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 10),
    _CntFddiMACShortGrpAddr_Type()
)
cntFddiMACShortGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACShortGrpAddr.setStatus("optional")
_CntFddiMACTPri0_Type = Integer32
_CntFddiMACTPri0_Object = MibTableColumn
cntFddiMACTPri0 = _CntFddiMACTPri0_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 11),
    _CntFddiMACTPri0_Type()
)
cntFddiMACTPri0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTPri0.setStatus("optional")
_CntFddiMACTPri1_Type = Integer32
_CntFddiMACTPri1_Object = MibTableColumn
cntFddiMACTPri1 = _CntFddiMACTPri1_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 12),
    _CntFddiMACTPri1_Type()
)
cntFddiMACTPri1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTPri1.setStatus("optional")
_CntFddiMACTPri2_Type = Integer32
_CntFddiMACTPri2_Object = MibTableColumn
cntFddiMACTPri2 = _CntFddiMACTPri2_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 13),
    _CntFddiMACTPri2_Type()
)
cntFddiMACTPri2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTPri2.setStatus("optional")
_CntFddiMACTPri3_Type = Integer32
_CntFddiMACTPri3_Object = MibTableColumn
cntFddiMACTPri3 = _CntFddiMACTPri3_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 14),
    _CntFddiMACTPri3_Type()
)
cntFddiMACTPri3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTPri3.setStatus("optional")
_CntFddiMACTPri4_Type = Integer32
_CntFddiMACTPri4_Object = MibTableColumn
cntFddiMACTPri4 = _CntFddiMACTPri4_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 15),
    _CntFddiMACTPri4_Type()
)
cntFddiMACTPri4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTPri4.setStatus("optional")
_CntFddiMACTPri5_Type = Integer32
_CntFddiMACTPri5_Object = MibTableColumn
cntFddiMACTPri5 = _CntFddiMACTPri5_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 16),
    _CntFddiMACTPri5_Type()
)
cntFddiMACTPri5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTPri5.setStatus("optional")
_CntFddiMACTPri6_Type = Integer32
_CntFddiMACTPri6_Object = MibTableColumn
cntFddiMACTPri6 = _CntFddiMACTPri6_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 17),
    _CntFddiMACTPri6_Type()
)
cntFddiMACTPri6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTPri6.setStatus("optional")
_CntFddiMACCopies_Type = Counter32
_CntFddiMACCopies_Object = MibTableColumn
cntFddiMACCopies = _CntFddiMACCopies_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 18),
    _CntFddiMACCopies_Type()
)
cntFddiMACCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACCopies.setStatus("optional")
_CntFddiMACTransmits_Type = Counter32
_CntFddiMACTransmits_Object = MibTableColumn
cntFddiMACTransmits = _CntFddiMACTransmits_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 19),
    _CntFddiMACTransmits_Type()
)
cntFddiMACTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTransmits.setStatus("optional")
_CntFddiMACTokens_Type = Counter32
_CntFddiMACTokens_Object = MibTableColumn
cntFddiMACTokens = _CntFddiMACTokens_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 20),
    _CntFddiMACTokens_Type()
)
cntFddiMACTokens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTokens.setStatus("optional")
_CntFddiMACTvxExpires_Type = Counter32
_CntFddiMACTvxExpires_Object = MibTableColumn
cntFddiMACTvxExpires = _CntFddiMACTvxExpires_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 21),
    _CntFddiMACTvxExpires_Type()
)
cntFddiMACTvxExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACTvxExpires.setStatus("optional")
_CntFddiMACNotCopies_Type = Counter32
_CntFddiMACNotCopies_Object = MibTableColumn
cntFddiMACNotCopies = _CntFddiMACNotCopies_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 22),
    _CntFddiMACNotCopies_Type()
)
cntFddiMACNotCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACNotCopies.setStatus("optional")
_CntFddiMACLates_Type = Counter32
_CntFddiMACLates_Object = MibTableColumn
cntFddiMACLates = _CntFddiMACLates_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 23),
    _CntFddiMACLates_Type()
)
cntFddiMACLates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACLates.setStatus("optional")
_CntFddiMACRingOps_Type = Counter32
_CntFddiMACRingOps_Object = MibTableColumn
cntFddiMACRingOps = _CntFddiMACRingOps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 24),
    _CntFddiMACRingOps_Type()
)
cntFddiMACRingOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACRingOps.setStatus("optional")
_CntFddiMACBaseFrames_Type = Counter32
_CntFddiMACBaseFrames_Object = MibTableColumn
cntFddiMACBaseFrames = _CntFddiMACBaseFrames_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 25),
    _CntFddiMACBaseFrames_Type()
)
cntFddiMACBaseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBaseFrames.setStatus("optional")
_CntFddiMACBaseErrs_Type = Counter32
_CntFddiMACBaseErrs_Object = MibTableColumn
cntFddiMACBaseErrs = _CntFddiMACBaseErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 26),
    _CntFddiMACBaseErrs_Type()
)
cntFddiMACBaseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBaseErrs.setStatus("optional")
_CntFddiMACBaseLosts_Type = Counter32
_CntFddiMACBaseLosts_Object = MibTableColumn
cntFddiMACBaseLosts = _CntFddiMACBaseLosts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 27),
    _CntFddiMACBaseLosts_Type()
)
cntFddiMACBaseLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBaseLosts.setStatus("optional")
_CntFddiMACBaseTimeFrameError_Type = OctetString
_CntFddiMACBaseTimeFrameError_Object = MibTableColumn
cntFddiMACBaseTimeFrameError = _CntFddiMACBaseTimeFrameError_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 28),
    _CntFddiMACBaseTimeFrameError_Type()
)
cntFddiMACBaseTimeFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBaseTimeFrameError.setStatus("optional")
_CntFddiMACBaseNotCopies_Type = Counter32
_CntFddiMACBaseNotCopies_Object = MibTableColumn
cntFddiMACBaseNotCopies = _CntFddiMACBaseNotCopies_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 29),
    _CntFddiMACBaseNotCopies_Type()
)
cntFddiMACBaseNotCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBaseNotCopies.setStatus("optional")
_CntFddiMACBaseTimeNotCopied_Type = OctetString
_CntFddiMACBaseTimeNotCopied_Object = MibTableColumn
cntFddiMACBaseTimeNotCopied = _CntFddiMACBaseTimeNotCopied_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 30),
    _CntFddiMACBaseTimeNotCopied_Type()
)
cntFddiMACBaseTimeNotCopied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBaseTimeNotCopied.setStatus("optional")
_CntFddiMACNotCopiedThreshold_Type = Integer32
_CntFddiMACNotCopiedThreshold_Object = MibTableColumn
cntFddiMACNotCopiedThreshold = _CntFddiMACNotCopiedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 31),
    _CntFddiMACNotCopiedThreshold_Type()
)
cntFddiMACNotCopiedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACNotCopiedThreshold.setStatus("optional")
_CntFddiMACBaseCopies_Type = Counter32
_CntFddiMACBaseCopies_Object = MibTableColumn
cntFddiMACBaseCopies = _CntFddiMACBaseCopies_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 32),
    _CntFddiMACBaseCopies_Type()
)
cntFddiMACBaseCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACBaseCopies.setStatus("optional")
_CntFddiMACNotCopiedRatio_Type = Integer32
_CntFddiMACNotCopiedRatio_Object = MibTableColumn
cntFddiMACNotCopiedRatio = _CntFddiMACNotCopiedRatio_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 33),
    _CntFddiMACNotCopiedRatio_Type()
)
cntFddiMACNotCopiedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACNotCopiedRatio.setStatus("optional")
_CntFddiMACNotCopiedCondition_Type = Integer32
_CntFddiMACNotCopiedCondition_Object = MibTableColumn
cntFddiMACNotCopiedCondition = _CntFddiMACNotCopiedCondition_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 34),
    _CntFddiMACNotCopiedCondition_Type()
)
cntFddiMACNotCopiedCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACNotCopiedCondition.setStatus("optional")
_CntFddiMACLLCServiceAvailable_Type = Integer32
_CntFddiMACLLCServiceAvailable_Object = MibTableColumn
cntFddiMACLLCServiceAvailable = _CntFddiMACLLCServiceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 35),
    _CntFddiMACLLCServiceAvailable_Type()
)
cntFddiMACLLCServiceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACLLCServiceAvailable.setStatus("optional")
_CntFddiMACMasterSlaveLoopStatus_Type = Integer32
_CntFddiMACMasterSlaveLoopStatus_Object = MibTableColumn
cntFddiMACMasterSlaveLoopStatus = _CntFddiMACMasterSlaveLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 36),
    _CntFddiMACMasterSlaveLoopStatus_Type()
)
cntFddiMACMasterSlaveLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACMasterSlaveLoopStatus.setStatus("optional")
_CntFddiMACRootMACDownStreamPORTType_Type = Integer32
_CntFddiMACRootMACDownStreamPORTType_Object = MibTableColumn
cntFddiMACRootMACDownStreamPORTType = _CntFddiMACRootMACDownStreamPORTType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 37),
    _CntFddiMACRootMACDownStreamPORTType_Type()
)
cntFddiMACRootMACDownStreamPORTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACRootMACDownStreamPORTType.setStatus("optional")
_CntFddiMACRootMACCurrentPath_Type = Integer32
_CntFddiMACRootMACCurrentPath_Object = MibTableColumn
cntFddiMACRootMACCurrentPath = _CntFddiMACRootMACCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 2, 2, 1, 38),
    _CntFddiMACRootMACCurrentPath_Type()
)
cntFddiMACRootMACCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiMACRootMACCurrentPath.setStatus("optional")
_CntFddiPATH_ObjectIdentity = ObjectIdentity
cntFddiPATH = _CntFddiPATH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3)
)


class _CntFddiPATHNumber_Type(Integer32):
    """Custom type cntFddiPATHNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CntFddiPATHNumber_Type.__name__ = "Integer32"
_CntFddiPATHNumber_Object = MibScalar
cntFddiPATHNumber = _CntFddiPATHNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 1),
    _CntFddiPATHNumber_Type()
)
cntFddiPATHNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHNumber.setStatus("mandatory")
_CntFddiPATHTable_Object = MibTable
cntFddiPATHTable = _CntFddiPATHTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cntFddiPATHTable.setStatus("mandatory")
_CntFddiPATHEntry_Object = MibTableRow
cntFddiPATHEntry = _CntFddiPATHEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1)
)
cntFddiPATHEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntFddiPATHSMTIndex"),
)
if mibBuilder.loadTexts:
    cntFddiPATHEntry.setStatus("mandatory")


class _CntFddiPATHSMTIndex_Type(Integer32):
    """Custom type cntFddiPATHSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntFddiPATHSMTIndex_Type.__name__ = "Integer32"
_CntFddiPATHSMTIndex_Object = MibTableColumn
cntFddiPATHSMTIndex = _CntFddiPATHSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 1),
    _CntFddiPATHSMTIndex_Type()
)
cntFddiPATHSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHSMTIndex.setStatus("mandatory")


class _CntFddiPATHIndex_Type(Integer32):
    """Custom type cntFddiPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntFddiPATHIndex_Type.__name__ = "Integer32"
_CntFddiPATHIndex_Object = MibTableColumn
cntFddiPATHIndex = _CntFddiPATHIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 2),
    _CntFddiPATHIndex_Type()
)
cntFddiPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHIndex.setStatus("mandatory")
_CntFddiPATHTraceMaxExpiration_Type = Integer32
_CntFddiPATHTraceMaxExpiration_Object = MibTableColumn
cntFddiPATHTraceMaxExpiration = _CntFddiPATHTraceMaxExpiration_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 3),
    _CntFddiPATHTraceMaxExpiration_Type()
)
cntFddiPATHTraceMaxExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHTraceMaxExpiration.setStatus("mandatory")
_CntFddiPATHTVXLowerBound_Type = Integer32
_CntFddiPATHTVXLowerBound_Object = MibTableColumn
cntFddiPATHTVXLowerBound = _CntFddiPATHTVXLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 4),
    _CntFddiPATHTVXLowerBound_Type()
)
cntFddiPATHTVXLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHTVXLowerBound.setStatus("optional")
_CntFddiPATHTMaxLowerBound_Type = Integer32
_CntFddiPATHTMaxLowerBound_Object = MibTableColumn
cntFddiPATHTMaxLowerBound = _CntFddiPATHTMaxLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 5),
    _CntFddiPATHTMaxLowerBound_Type()
)
cntFddiPATHTMaxLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHTMaxLowerBound.setStatus("optional")
_CntFddiPATHType_Type = Integer32
_CntFddiPATHType_Object = MibTableColumn
cntFddiPATHType = _CntFddiPATHType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 6),
    _CntFddiPATHType_Type()
)
cntFddiPATHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHType.setStatus("mandatory")
_CntFddiPATHPORTOrder_Type = Integer32
_CntFddiPATHPORTOrder_Object = MibTableColumn
cntFddiPATHPORTOrder = _CntFddiPATHPORTOrder_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 7),
    _CntFddiPATHPORTOrder_Type()
)
cntFddiPATHPORTOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHPORTOrder.setStatus("mandatory")
_CntFddiPATHRingLatency_Type = Integer32
_CntFddiPATHRingLatency_Object = MibTableColumn
cntFddiPATHRingLatency = _CntFddiPATHRingLatency_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 8),
    _CntFddiPATHRingLatency_Type()
)
cntFddiPATHRingLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHRingLatency.setStatus("optional")
_CntFddiPATHTraceStatus_Type = Integer32
_CntFddiPATHTraceStatus_Object = MibTableColumn
cntFddiPATHTraceStatus = _CntFddiPATHTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 9),
    _CntFddiPATHTraceStatus_Type()
)
cntFddiPATHTraceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHTraceStatus.setStatus("optional")
_CntFddiPATHSba_Type = Integer32
_CntFddiPATHSba_Object = MibTableColumn
cntFddiPATHSba = _CntFddiPATHSba_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 10),
    _CntFddiPATHSba_Type()
)
cntFddiPATHSba.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHSba.setStatus("mandatory")
_CntFddiPATHSbaOverhead_Type = Integer32
_CntFddiPATHSbaOverhead_Object = MibTableColumn
cntFddiPATHSbaOverhead = _CntFddiPATHSbaOverhead_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 11),
    _CntFddiPATHSbaOverhead_Type()
)
cntFddiPATHSbaOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHSbaOverhead.setStatus("mandatory")
_CntFddiPATHStatus_Type = Integer32
_CntFddiPATHStatus_Object = MibTableColumn
cntFddiPATHStatus = _CntFddiPATHStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 12),
    _CntFddiPATHStatus_Type()
)
cntFddiPATHStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHStatus.setStatus("mandatory")
_CntFddiPATHTRmode_Type = Integer32
_CntFddiPATHTRmode_Object = MibTableColumn
cntFddiPATHTRmode = _CntFddiPATHTRmode_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 3, 2, 1, 13),
    _CntFddiPATHTRmode_Type()
)
cntFddiPATHTRmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPATHTRmode.setStatus("optional")
_CntFddiPORT_ObjectIdentity = ObjectIdentity
cntFddiPORT = _CntFddiPORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4)
)


class _CntFddiPORTNumber_Type(Integer32):
    """Custom type cntFddiPORTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CntFddiPORTNumber_Type.__name__ = "Integer32"
_CntFddiPORTNumber_Object = MibScalar
cntFddiPORTNumber = _CntFddiPORTNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 1),
    _CntFddiPORTNumber_Type()
)
cntFddiPORTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTNumber.setStatus("mandatory")
_CntFddiPORTTable_Object = MibTable
cntFddiPORTTable = _CntFddiPORTTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2)
)
if mibBuilder.loadTexts:
    cntFddiPORTTable.setStatus("mandatory")
_CntFddiPORTEntry_Object = MibTableRow
cntFddiPORTEntry = _CntFddiPORTEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1)
)
cntFddiPORTEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntFddiPORTSMTIndex"),
)
if mibBuilder.loadTexts:
    cntFddiPORTEntry.setStatus("mandatory")


class _CntFddiPORTSMTIndex_Type(Integer32):
    """Custom type cntFddiPORTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntFddiPORTSMTIndex_Type.__name__ = "Integer32"
_CntFddiPORTSMTIndex_Object = MibTableColumn
cntFddiPORTSMTIndex = _CntFddiPORTSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 1),
    _CntFddiPORTSMTIndex_Type()
)
cntFddiPORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTSMTIndex.setStatus("mandatory")


class _CntFddiPORTIndex_Type(Integer32):
    """Custom type cntFddiPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntFddiPORTIndex_Type.__name__ = "Integer32"
_CntFddiPORTIndex_Object = MibTableColumn
cntFddiPORTIndex = _CntFddiPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 2),
    _CntFddiPORTIndex_Type()
)
cntFddiPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTIndex.setStatus("mandatory")
_CntFddiPORTFotxClass_Type = Integer32
_CntFddiPORTFotxClass_Object = MibTableColumn
cntFddiPORTFotxClass = _CntFddiPORTFotxClass_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 3),
    _CntFddiPORTFotxClass_Type()
)
cntFddiPORTFotxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTFotxClass.setStatus("optional")
_CntFddiPORTMaintLineState_Type = Integer32
_CntFddiPORTMaintLineState_Object = MibTableColumn
cntFddiPORTMaintLineState = _CntFddiPORTMaintLineState_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 4),
    _CntFddiPORTMaintLineState_Type()
)
cntFddiPORTMaintLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTMaintLineState.setStatus("optional")
_CntFddiPORTEBErrs_Type = Counter32
_CntFddiPORTEBErrs_Object = MibTableColumn
cntFddiPORTEBErrs = _CntFddiPORTEBErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 5),
    _CntFddiPORTEBErrs_Type()
)
cntFddiPORTEBErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTEBErrs.setStatus("optional")
_CntFddiPORTBaseLerEstimate_Type = Integer32
_CntFddiPORTBaseLerEstimate_Object = MibTableColumn
cntFddiPORTBaseLerEstimate = _CntFddiPORTBaseLerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 6),
    _CntFddiPORTBaseLerEstimate_Type()
)
cntFddiPORTBaseLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTBaseLerEstimate.setStatus("mandatory")
_CntFddiPORTBaseLemRejects_Type = Counter32
_CntFddiPORTBaseLemRejects_Object = MibTableColumn
cntFddiPORTBaseLemRejects = _CntFddiPORTBaseLemRejects_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 7),
    _CntFddiPORTBaseLemRejects_Type()
)
cntFddiPORTBaseLemRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTBaseLemRejects.setStatus("mandatory")
_CntFddiPORTBaseLems_Type = Counter32
_CntFddiPORTBaseLems_Object = MibTableColumn
cntFddiPORTBaseLems = _CntFddiPORTBaseLems_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 8),
    _CntFddiPORTBaseLems_Type()
)
cntFddiPORTBaseLems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTBaseLems.setStatus("mandatory")
_CntFddiPORTBaseLerTimeStamp_Type = OctetString
_CntFddiPORTBaseLerTimeStamp_Object = MibTableColumn
cntFddiPORTBaseLerTimeStamp = _CntFddiPORTBaseLerTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 10, 2, 4, 2, 1, 9),
    _CntFddiPORTBaseLerTimeStamp_Type()
)
cntFddiPORTBaseLerTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPORTBaseLerTimeStamp.setStatus("mandatory")
_Cntsnmp_ObjectIdentity = ObjectIdentity
cntsnmp = _Cntsnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 11)
)
_Cntsnmpconfig_ObjectIdentity = ObjectIdentity
cntsnmpconfig = _Cntsnmpconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1)
)
_CntMibVersion_Type = IpAddress
_CntMibVersion_Object = MibScalar
cntMibVersion = _CntMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 1),
    _CntMibVersion_Type()
)
cntMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMibVersion.setStatus("mandatory")
_CntMibObjectCount_Type = Integer32
_CntMibObjectCount_Object = MibScalar
cntMibObjectCount = _CntMibObjectCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 2),
    _CntMibObjectCount_Type()
)
cntMibObjectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMibObjectCount.setStatus("mandatory")
_CntConfigVersion_Type = Integer32
_CntConfigVersion_Object = MibScalar
cntConfigVersion = _CntConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 3),
    _CntConfigVersion_Type()
)
cntConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntConfigVersion.setStatus("mandatory")


class _CntProxyStatus_Type(Integer32):
    """Custom type cntProxyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-proxy", 1),
          ("proxied-node", 3),
          ("proxy-agent", 2))
    )


_CntProxyStatus_Type.__name__ = "Integer32"
_CntProxyStatus_Object = MibScalar
cntProxyStatus = _CntProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 4),
    _CntProxyStatus_Type()
)
cntProxyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntProxyStatus.setStatus("mandatory")
_CntProxyCount_Type = Integer32
_CntProxyCount_Object = MibScalar
cntProxyCount = _CntProxyCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 5),
    _CntProxyCount_Type()
)
cntProxyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntProxyCount.setStatus("mandatory")
_CntSnmpBufferCount_Type = Integer32
_CntSnmpBufferCount_Object = MibScalar
cntSnmpBufferCount = _CntSnmpBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 6),
    _CntSnmpBufferCount_Type()
)
cntSnmpBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSnmpBufferCount.setStatus("mandatory")
_CntIfPollInterval_Type = Integer32
_CntIfPollInterval_Object = MibScalar
cntIfPollInterval = _CntIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 7),
    _CntIfPollInterval_Type()
)
cntIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIfPollInterval.setStatus("mandatory")
_CntIfNextPoll_Type = Integer32
_CntIfNextPoll_Object = MibScalar
cntIfNextPoll = _CntIfNextPoll_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 8),
    _CntIfNextPoll_Type()
)
cntIfNextPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntIfNextPoll.setStatus("mandatory")
_CntDoDIPCount_Type = Integer32
_CntDoDIPCount_Object = MibScalar
cntDoDIPCount = _CntDoDIPCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 9),
    _CntDoDIPCount_Type()
)
cntDoDIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntDoDIPCount.setStatus("mandatory")
_CntDot3Count_Type = Integer32
_CntDot3Count_Object = MibScalar
cntDot3Count = _CntDot3Count_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 10),
    _CntDot3Count_Type()
)
cntDot3Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntDot3Count.setStatus("mandatory")
_CntFddiCount_Type = Integer32
_CntFddiCount_Object = MibScalar
cntFddiCount = _CntFddiCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 11),
    _CntFddiCount_Type()
)
cntFddiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiCount.setStatus("mandatory")
_CntFddiPortCount_Type = Integer32
_CntFddiPortCount_Object = MibScalar
cntFddiPortCount = _CntFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 12),
    _CntFddiPortCount_Type()
)
cntFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiPortCount.setStatus("mandatory")
_CntDataLinkCount_Type = Integer32
_CntDataLinkCount_Object = MibScalar
cntDataLinkCount = _CntDataLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 13),
    _CntDataLinkCount_Type()
)
cntDataLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntDataLinkCount.setStatus("mandatory")
_CntLLC1Count_Type = Integer32
_CntLLC1Count_Object = MibScalar
cntLLC1Count = _CntLLC1Count_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 14),
    _CntLLC1Count_Type()
)
cntLLC1Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntLLC1Count.setStatus("mandatory")
_CntCofiVersion_Type = IpAddress
_CntCofiVersion_Object = MibScalar
cntCofiVersion = _CntCofiVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 1, 15),
    _CntCofiVersion_Type()
)
cntCofiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCofiVersion.setStatus("mandatory")
_Cntsnmpstat_ObjectIdentity = ObjectIdentity
cntsnmpstat = _Cntsnmpstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2)
)
_CntMib2Requests_Type = Counter32
_CntMib2Requests_Object = MibScalar
cntMib2Requests = _CntMib2Requests_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 1),
    _CntMib2Requests_Type()
)
cntMib2Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMib2Requests.setStatus("mandatory")
_CntFddiRequests_Type = Counter32
_CntFddiRequests_Object = MibScalar
cntFddiRequests = _CntFddiRequests_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 2),
    _CntFddiRequests_Type()
)
cntFddiRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntFddiRequests.setStatus("mandatory")
_CntDot3Requests_Type = Counter32
_CntDot3Requests_Object = MibScalar
cntDot3Requests = _CntDot3Requests_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 3),
    _CntDot3Requests_Type()
)
cntDot3Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntDot3Requests.setStatus("mandatory")
_CntCntRequests_Type = Counter32
_CntCntRequests_Object = MibScalar
cntCntRequests = _CntCntRequests_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 4),
    _CntCntRequests_Type()
)
cntCntRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCntRequests.setStatus("mandatory")
_CntRowAdditions_Type = Counter32
_CntRowAdditions_Object = MibScalar
cntRowAdditions = _CntRowAdditions_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 5),
    _CntRowAdditions_Type()
)
cntRowAdditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRowAdditions.setStatus("mandatory")
_CntRowModifies_Type = Counter32
_CntRowModifies_Object = MibScalar
cntRowModifies = _CntRowModifies_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 6),
    _CntRowModifies_Type()
)
cntRowModifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRowModifies.setStatus("mandatory")
_CntRowDeletions_Type = Counter32
_CntRowDeletions_Object = MibScalar
cntRowDeletions = _CntRowDeletions_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 7),
    _CntRowDeletions_Type()
)
cntRowDeletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRowDeletions.setStatus("mandatory")
_CntRowErrors_Type = Counter32
_CntRowErrors_Object = MibScalar
cntRowErrors = _CntRowErrors_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 8),
    _CntRowErrors_Type()
)
cntRowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntRowErrors.setStatus("mandatory")
_CntBadVersions_Type = Counter32
_CntBadVersions_Object = MibScalar
cntBadVersions = _CntBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 9),
    _CntBadVersions_Type()
)
cntBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntBadVersions.setStatus("mandatory")
_CntNoBuffers_Type = Counter32
_CntNoBuffers_Object = MibScalar
cntNoBuffers = _CntNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 10),
    _CntNoBuffers_Type()
)
cntNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntNoBuffers.setStatus("mandatory")
_CntMailTimeouts_Type = Counter32
_CntMailTimeouts_Object = MibScalar
cntMailTimeouts = _CntMailTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 11),
    _CntMailTimeouts_Type()
)
cntMailTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntMailTimeouts.setStatus("mandatory")
_CntCachedResponses_Type = Counter32
_CntCachedResponses_Object = MibScalar
cntCachedResponses = _CntCachedResponses_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 12),
    _CntCachedResponses_Type()
)
cntCachedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntCachedResponses.setStatus("mandatory")
_CntUsedCaches_Type = Counter32
_CntUsedCaches_Object = MibScalar
cntUsedCaches = _CntUsedCaches_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 2, 13),
    _CntUsedCaches_Type()
)
cntUsedCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntUsedCaches.setStatus("mandatory")
_Cntsnmptrap_ObjectIdentity = ObjectIdentity
cntsnmptrap = _Cntsnmptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3)
)
_CntTrapDestCount_Type = Integer32
_CntTrapDestCount_Object = MibScalar
cntTrapDestCount = _CntTrapDestCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 1),
    _CntTrapDestCount_Type()
)
cntTrapDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntTrapDestCount.setStatus("mandatory")
_CntLastTrapMsg_Type = DisplayString
_CntLastTrapMsg_Object = MibScalar
cntLastTrapMsg = _CntLastTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 2),
    _CntLastTrapMsg_Type()
)
cntLastTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntLastTrapMsg.setStatus("mandatory")
_CntTrapTable_Object = MibTable
cntTrapTable = _CntTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    cntTrapTable.setStatus("mandatory")
_CnttrapEntry_Object = MibTableRow
cnttrapEntry = _CnttrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 3, 1)
)
cnttrapEntry.setIndexNames(
    (0, "CNTAU-MIB", "cnttrapIndex"),
)
if mibBuilder.loadTexts:
    cnttrapEntry.setStatus("mandatory")
_CnttrapIndex_Type = Integer32
_CnttrapIndex_Object = MibTableColumn
cnttrapIndex = _CnttrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 3, 1, 1),
    _CnttrapIndex_Type()
)
cnttrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnttrapIndex.setStatus("mandatory")
_CnttrapAddress_Type = IpAddress
_CnttrapAddress_Object = MibTableColumn
cnttrapAddress = _CnttrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 3, 1, 2),
    _CnttrapAddress_Type()
)
cnttrapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnttrapAddress.setStatus("mandatory")
_CntsnmpTrapFlags_Type = Integer32
_CntsnmpTrapFlags_Object = MibTableColumn
cntsnmpTrapFlags = _CntsnmpTrapFlags_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 3, 1, 3),
    _CntsnmpTrapFlags_Type()
)
cntsnmpTrapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsnmpTrapFlags.setStatus("mandatory")
_CntTrapFlags_Type = Integer32
_CntTrapFlags_Object = MibTableColumn
cntTrapFlags = _CntTrapFlags_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 3, 1, 4),
    _CntTrapFlags_Type()
)
cntTrapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntTrapFlags.setStatus("mandatory")
_CnttrapIf_Type = IpAddress
_CnttrapIf_Object = MibTableColumn
cnttrapIf = _CnttrapIf_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 3, 3, 1, 5),
    _CnttrapIf_Type()
)
cnttrapIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnttrapIf.setStatus("mandatory")
_Cntsnmpproxy_ObjectIdentity = ObjectIdentity
cntsnmpproxy = _Cntsnmpproxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 4)
)
_CntProxyTable_Object = MibTable
cntProxyTable = _CntProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    cntProxyTable.setStatus("mandatory")
_CntproxyEntry_Object = MibTableRow
cntproxyEntry = _CntproxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 4, 1, 1)
)
cntproxyEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntproxyIndex"),
)
if mibBuilder.loadTexts:
    cntproxyEntry.setStatus("mandatory")
_CntproxyIndex_Type = Integer32
_CntproxyIndex_Object = MibTableColumn
cntproxyIndex = _CntproxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 4, 1, 1, 1),
    _CntproxyIndex_Type()
)
cntproxyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntproxyIndex.setStatus("mandatory")
_CntproxyAddress_Type = IpAddress
_CntproxyAddress_Object = MibTableColumn
cntproxyAddress = _CntproxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 4, 1, 1, 2),
    _CntproxyAddress_Type()
)
cntproxyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntproxyAddress.setStatus("mandatory")
_CntproxyNode_Type = IpAddress
_CntproxyNode_Object = MibTableColumn
cntproxyNode = _CntproxyNode_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 11, 4, 1, 1, 3),
    _CntproxyNode_Type()
)
cntproxyNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntproxyNode.setStatus("mandatory")
_Cntdiagnostics_ObjectIdentity = ObjectIdentity
cntdiagnostics = _Cntdiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 12)
)
_CntTraceTable_Object = MibTable
cntTraceTable = _CntTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cntTraceTable.setStatus("mandatory")
_CnttraceEntry_Object = MibTableRow
cnttraceEntry = _CnttraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 1, 1)
)
cnttraceEntry.setIndexNames(
    (0, "CNTAU-MIB", "cnttraceIndex"),
)
if mibBuilder.loadTexts:
    cnttraceEntry.setStatus("mandatory")
_CnttraceIndex_Type = Integer32
_CnttraceIndex_Object = MibTableColumn
cnttraceIndex = _CnttraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 1, 1, 1),
    _CnttraceIndex_Type()
)
cnttraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnttraceIndex.setStatus("mandatory")
_CnttraceType_Type = Integer32
_CnttraceType_Object = MibTableColumn
cnttraceType = _CnttraceType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 1, 1, 2),
    _CnttraceType_Type()
)
cnttraceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnttraceType.setStatus("mandatory")


class _CnttraceCpu_Type(Integer32):
    """Custom type cnttraceCpu based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_CnttraceCpu_Type.__name__ = "Integer32"
_CnttraceCpu_Object = MibTableColumn
cnttraceCpu = _CnttraceCpu_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 1, 1, 3),
    _CnttraceCpu_Type()
)
cnttraceCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnttraceCpu.setStatus("mandatory")
_CnttraceData_Type = OctetString
_CnttraceData_Object = MibTableColumn
cnttraceData = _CnttraceData_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 1, 1, 4),
    _CnttraceData_Type()
)
cnttraceData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnttraceData.setStatus("mandatory")
_CntMailQueue_ObjectIdentity = ObjectIdentity
cntMailQueue = _CntMailQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2)
)
_CntMDMTable_Object = MibTable
cntMDMTable = _CntMDMTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    cntMDMTable.setStatus("mandatory")
_CntMDMEntry_Object = MibTableRow
cntMDMEntry = _CntMDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2, 1, 1)
)
cntMDMEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntmdmQIndex"),
)
if mibBuilder.loadTexts:
    cntMDMEntry.setStatus("mandatory")
_CntmdmQIndex_Type = Integer32
_CntmdmQIndex_Object = MibTableColumn
cntmdmQIndex = _CntmdmQIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2, 1, 1, 1),
    _CntmdmQIndex_Type()
)
cntmdmQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntmdmQIndex.setStatus("mandatory")
_CntmdmQName_Type = DisplayString
_CntmdmQName_Object = MibTableColumn
cntmdmQName = _CntmdmQName_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2, 1, 1, 2),
    _CntmdmQName_Type()
)
cntmdmQName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntmdmQName.setStatus("mandatory")
_CntmdmQProcessId_Type = Integer32
_CntmdmQProcessId_Object = MibTableColumn
cntmdmQProcessId = _CntmdmQProcessId_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2, 1, 1, 3),
    _CntmdmQProcessId_Type()
)
cntmdmQProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntmdmQProcessId.setStatus("mandatory")
_CntmdmQTaskId_Type = Integer32
_CntmdmQTaskId_Object = MibTableColumn
cntmdmQTaskId = _CntmdmQTaskId_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2, 1, 1, 4),
    _CntmdmQTaskId_Type()
)
cntmdmQTaskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntmdmQTaskId.setStatus("mandatory")
_CntmdmQList_Type = DisplayString
_CntmdmQList_Object = MibScalar
cntmdmQList = _CntmdmQList_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 12, 2, 2),
    _CntmdmQList_Type()
)
cntmdmQList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntmdmQList.setStatus("mandatory")
_Cntdatalink_ObjectIdentity = ObjectIdentity
cntdatalink = _Cntdatalink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 13)
)
_CntdlNumber_Type = Integer32
_CntdlNumber_Object = MibScalar
cntdlNumber = _CntdlNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 1),
    _CntdlNumber_Type()
)
cntdlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlNumber.setStatus("mandatory")
_CntdlTable_Object = MibTable
cntdlTable = _CntdlTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2)
)
if mibBuilder.loadTexts:
    cntdlTable.setStatus("mandatory")
_CntdlEntry_Object = MibTableRow
cntdlEntry = _CntdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1)
)
cntdlEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntdlIndex"),
)
if mibBuilder.loadTexts:
    cntdlEntry.setStatus("mandatory")
_CntdlIndex_Type = Integer32
_CntdlIndex_Object = MibTableColumn
cntdlIndex = _CntdlIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 1),
    _CntdlIndex_Type()
)
cntdlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlIndex.setStatus("mandatory")
_CntdlDescr_Type = DisplayString
_CntdlDescr_Object = MibTableColumn
cntdlDescr = _CntdlDescr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 2),
    _CntdlDescr_Type()
)
cntdlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlDescr.setStatus("mandatory")


class _CntdlType_Type(Integer32):
    """Custom type cntdlType based on Integer32"""
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
        *(("cnet", 5),
          ("dnls", 6),
          ("llc1", 1),
          ("llc2", 2),
          ("llc3", 3),
          ("ppp", 8),
          ("snap", 4),
          ("strp", 7))
    )


_CntdlType_Type.__name__ = "Integer32"
_CntdlType_Object = MibTableColumn
cntdlType = _CntdlType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 3),
    _CntdlType_Type()
)
cntdlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlType.setStatus("mandatory")


class _CntdlTypeofService_Type(Integer32):
    """Custom type cntdlTypeofService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acked-connectionless", 3),
          ("connection-oriented", 2),
          ("unacked-connectionless", 1))
    )


_CntdlTypeofService_Type.__name__ = "Integer32"
_CntdlTypeofService_Object = MibTableColumn
cntdlTypeofService = _CntdlTypeofService_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 4),
    _CntdlTypeofService_Type()
)
cntdlTypeofService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlTypeofService.setStatus("mandatory")
_CntdlMtu_Type = Integer32
_CntdlMtu_Object = MibTableColumn
cntdlMtu = _CntdlMtu_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 5),
    _CntdlMtu_Type()
)
cntdlMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlMtu.setStatus("mandatory")
_CntdlPortAddrLen_Type = Integer32
_CntdlPortAddrLen_Object = MibTableColumn
cntdlPortAddrLen = _CntdlPortAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 6),
    _CntdlPortAddrLen_Type()
)
cntdlPortAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlPortAddrLen.setStatus("mandatory")
_CntdlMaxPort_Type = Integer32
_CntdlMaxPort_Object = MibTableColumn
cntdlMaxPort = _CntdlMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 7),
    _CntdlMaxPort_Type()
)
cntdlMaxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlMaxPort.setStatus("mandatory")
_CntdlActivePort_Type = Integer32
_CntdlActivePort_Object = MibTableColumn
cntdlActivePort = _CntdlActivePort_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 8),
    _CntdlActivePort_Type()
)
cntdlActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlActivePort.setStatus("mandatory")
_CntdlInOctets_Type = Counter32
_CntdlInOctets_Object = MibTableColumn
cntdlInOctets = _CntdlInOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 9),
    _CntdlInOctets_Type()
)
cntdlInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlInOctets.setStatus("mandatory")
_CntdlInUcastPkts_Type = Counter32
_CntdlInUcastPkts_Object = MibTableColumn
cntdlInUcastPkts = _CntdlInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 10),
    _CntdlInUcastPkts_Type()
)
cntdlInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlInUcastPkts.setStatus("mandatory")
_CntdlInNUcastPkts_Type = Counter32
_CntdlInNUcastPkts_Object = MibTableColumn
cntdlInNUcastPkts = _CntdlInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 11),
    _CntdlInNUcastPkts_Type()
)
cntdlInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlInNUcastPkts.setStatus("mandatory")
_CntdlInDiscards_Type = Counter32
_CntdlInDiscards_Object = MibTableColumn
cntdlInDiscards = _CntdlInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 12),
    _CntdlInDiscards_Type()
)
cntdlInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlInDiscards.setStatus("mandatory")
_CntdlInErrors_Type = Counter32
_CntdlInErrors_Object = MibTableColumn
cntdlInErrors = _CntdlInErrors_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 13),
    _CntdlInErrors_Type()
)
cntdlInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlInErrors.setStatus("mandatory")
_CntdlInUnknownProtos_Type = Counter32
_CntdlInUnknownProtos_Object = MibTableColumn
cntdlInUnknownProtos = _CntdlInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 14),
    _CntdlInUnknownProtos_Type()
)
cntdlInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlInUnknownProtos.setStatus("mandatory")
_CntdlOutOctets_Type = Counter32
_CntdlOutOctets_Object = MibTableColumn
cntdlOutOctets = _CntdlOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 15),
    _CntdlOutOctets_Type()
)
cntdlOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlOutOctets.setStatus("mandatory")
_CntdlOutUcastPkts_Type = Counter32
_CntdlOutUcastPkts_Object = MibTableColumn
cntdlOutUcastPkts = _CntdlOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 16),
    _CntdlOutUcastPkts_Type()
)
cntdlOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlOutUcastPkts.setStatus("mandatory")
_CntdlOutNUcastPkts_Type = Counter32
_CntdlOutNUcastPkts_Object = MibTableColumn
cntdlOutNUcastPkts = _CntdlOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 17),
    _CntdlOutNUcastPkts_Type()
)
cntdlOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlOutNUcastPkts.setStatus("mandatory")
_CntdlOutDiscards_Type = Counter32
_CntdlOutDiscards_Object = MibTableColumn
cntdlOutDiscards = _CntdlOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 18),
    _CntdlOutDiscards_Type()
)
cntdlOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlOutDiscards.setStatus("mandatory")
_CntdlOutErrors_Type = Counter32
_CntdlOutErrors_Object = MibTableColumn
cntdlOutErrors = _CntdlOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 19),
    _CntdlOutErrors_Type()
)
cntdlOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlOutErrors.setStatus("mandatory")
_CntdlOutQLen_Type = Gauge32
_CntdlOutQLen_Object = MibTableColumn
cntdlOutQLen = _CntdlOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 20),
    _CntdlOutQLen_Type()
)
cntdlOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlOutQLen.setStatus("mandatory")
_CntdlPortTable_Object = MibTable
cntdlPortTable = _CntdlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 21)
)
if mibBuilder.loadTexts:
    cntdlPortTable.setStatus("mandatory")
_CntdlPortEntry_Object = MibTableRow
cntdlPortEntry = _CntdlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 21, 1)
)
cntdlPortEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntdlPortIndex"),
)
if mibBuilder.loadTexts:
    cntdlPortEntry.setStatus("mandatory")
_CntdlPortIndex_Type = Integer32
_CntdlPortIndex_Object = MibTableColumn
cntdlPortIndex = _CntdlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 21, 1, 1),
    _CntdlPortIndex_Type()
)
cntdlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlPortIndex.setStatus("mandatory")


class _CntdlState_Type(Integer32):
    """Custom type cntdlState based on Integer32"""
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
        *(("ack-sent", 8),
          ("closed", 6),
          ("connected", 1),
          ("data-transfer", 2),
          ("disconnected", 3),
          ("down", 5),
          ("listen", 7),
          ("waiting-for-ack", 4))
    )


_CntdlState_Type.__name__ = "Integer32"
_CntdlState_Object = MibTableColumn
cntdlState = _CntdlState_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 21, 1, 2),
    _CntdlState_Type()
)
cntdlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlState.setStatus("mandatory")
_CntdlSourcePort_Type = Integer32
_CntdlSourcePort_Object = MibTableColumn
cntdlSourcePort = _CntdlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 21, 1, 3),
    _CntdlSourcePort_Type()
)
cntdlSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlSourcePort.setStatus("mandatory")
_CntdlDestPort_Type = Integer32
_CntdlDestPort_Object = MibTableColumn
cntdlDestPort = _CntdlDestPort_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 21, 1, 4),
    _CntdlDestPort_Type()
)
cntdlDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlDestPort.setStatus("mandatory")


class _CntdlPortType_Type(Integer32):
    """Custom type cntdlPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 2),
          ("dod-ip", 1),
          ("snmp", 3))
    )


_CntdlPortType_Type.__name__ = "Integer32"
_CntdlPortType_Object = MibTableColumn
cntdlPortType = _CntdlPortType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 2, 1, 21, 1, 5),
    _CntdlPortType_Type()
)
cntdlPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntdlPortType.setStatus("mandatory")
_Cntllc1_ObjectIdentity = ObjectIdentity
cntllc1 = _Cntllc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3)
)
_Cntllc1ConfigTable_Object = MibTable
cntllc1ConfigTable = _Cntllc1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    cntllc1ConfigTable.setStatus("mandatory")
_Cntllc1ConfigEntry_Object = MibTableRow
cntllc1ConfigEntry = _Cntllc1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1)
)
cntllc1ConfigEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntllc1ConfigIndex"),
)
if mibBuilder.loadTexts:
    cntllc1ConfigEntry.setStatus("mandatory")
_Cntllc1ConfigIndex_Type = Integer32
_Cntllc1ConfigIndex_Object = MibTableColumn
cntllc1ConfigIndex = _Cntllc1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 1),
    _Cntllc1ConfigIndex_Type()
)
cntllc1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1ConfigIndex.setStatus("mandatory")


class _Cntllc1DriverType_Type(Integer32):
    """Custom type cntllc1DriverType based on Integer32"""
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
        *(("cnt-node", 1),
          ("ethernet", 5),
          ("fddi", 2),
          ("fibre-trunk", 3),
          ("hippi", 6),
          ("native", 4))
    )


_Cntllc1DriverType_Type.__name__ = "Integer32"
_Cntllc1DriverType_Object = MibTableColumn
cntllc1DriverType = _Cntllc1DriverType_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 2),
    _Cntllc1DriverType_Type()
)
cntllc1DriverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1DriverType.setStatus("mandatory")
_Cntllc1Addr_Type = OctetString
_Cntllc1Addr_Object = MibTableColumn
cntllc1Addr = _Cntllc1Addr_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 3),
    _Cntllc1Addr_Type()
)
cntllc1Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1Addr.setStatus("mandatory")


class _Cntllc1InitFlag_Type(Integer32):
    """Custom type cntllc1InitFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 2),
          ("uninitialized", 1))
    )


_Cntllc1InitFlag_Type.__name__ = "Integer32"
_Cntllc1InitFlag_Object = MibTableColumn
cntllc1InitFlag = _Cntllc1InitFlag_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 4),
    _Cntllc1InitFlag_Type()
)
cntllc1InitFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InitFlag.setStatus("mandatory")
_Cntllc1TraceFlag_Type = Integer32
_Cntllc1TraceFlag_Object = MibTableColumn
cntllc1TraceFlag = _Cntllc1TraceFlag_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 5),
    _Cntllc1TraceFlag_Type()
)
cntllc1TraceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1TraceFlag.setStatus("mandatory")
_Cntllc1BufCnt_Type = Integer32
_Cntllc1BufCnt_Object = MibTableColumn
cntllc1BufCnt = _Cntllc1BufCnt_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 6),
    _Cntllc1BufCnt_Type()
)
cntllc1BufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1BufCnt.setStatus("mandatory")
_Cntllc1BusId_Type = Integer32
_Cntllc1BusId_Object = MibTableColumn
cntllc1BusId = _Cntllc1BusId_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 7),
    _Cntllc1BusId_Type()
)
cntllc1BusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1BusId.setStatus("mandatory")


class _Cntllc1CpuNum_Type(Integer32):
    """Custom type cntllc1CpuNum based on Integer32"""
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
        *(("lcp-1", 1),
          ("lcp-2", 2),
          ("lcp-3", 3),
          ("lcp-4", 4),
          ("lcp-5", 5),
          ("lcp-6", 6),
          ("lcp-7", 7))
    )


_Cntllc1CpuNum_Type.__name__ = "Integer32"
_Cntllc1CpuNum_Object = MibTableColumn
cntllc1CpuNum = _Cntllc1CpuNum_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 8),
    _Cntllc1CpuNum_Type()
)
cntllc1CpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1CpuNum.setStatus("mandatory")
_Cntllc1BufPriority_Type = Integer32
_Cntllc1BufPriority_Object = MibTableColumn
cntllc1BufPriority = _Cntllc1BufPriority_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 9),
    _Cntllc1BufPriority_Type()
)
cntllc1BufPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1BufPriority.setStatus("mandatory")
_Cntllc1WaitTimeOut_Type = Integer32
_Cntllc1WaitTimeOut_Object = MibTableColumn
cntllc1WaitTimeOut = _Cntllc1WaitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 1, 1, 10),
    _Cntllc1WaitTimeOut_Type()
)
cntllc1WaitTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1WaitTimeOut.setStatus("mandatory")
_Cntllc1StatsTable_Object = MibTable
cntllc1StatsTable = _Cntllc1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2)
)
if mibBuilder.loadTexts:
    cntllc1StatsTable.setStatus("mandatory")
_Cntllc1StatsEntry_Object = MibTableRow
cntllc1StatsEntry = _Cntllc1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1)
)
cntllc1StatsEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntllc1StatIndex"),
)
if mibBuilder.loadTexts:
    cntllc1StatsEntry.setStatus("mandatory")
_Cntllc1StatIndex_Type = Integer32
_Cntllc1StatIndex_Object = MibTableColumn
cntllc1StatIndex = _Cntllc1StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 1),
    _Cntllc1StatIndex_Type()
)
cntllc1StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1StatIndex.setStatus("mandatory")
_Cntllc1InXids_Type = Counter32
_Cntllc1InXids_Object = MibTableColumn
cntllc1InXids = _Cntllc1InXids_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 2),
    _Cntllc1InXids_Type()
)
cntllc1InXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InXids.setStatus("mandatory")
_Cntllc1InTests_Type = Counter32
_Cntllc1InTests_Object = MibTableColumn
cntllc1InTests = _Cntllc1InTests_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 3),
    _Cntllc1InTests_Type()
)
cntllc1InTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InTests.setStatus("mandatory")
_Cntllc1InUIs_Type = Counter32
_Cntllc1InUIs_Object = MibTableColumn
cntllc1InUIs = _Cntllc1InUIs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 4),
    _Cntllc1InUIs_Type()
)
cntllc1InUIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InUIs.setStatus("mandatory")
_Cntllc1InNoDsaps_Type = Counter32
_Cntllc1InNoDsaps_Object = MibTableColumn
cntllc1InNoDsaps = _Cntllc1InNoDsaps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 5),
    _Cntllc1InNoDsaps_Type()
)
cntllc1InNoDsaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InNoDsaps.setStatus("mandatory")
_Cntllc1InXidOks_Type = Counter32
_Cntllc1InXidOks_Object = MibTableColumn
cntllc1InXidOks = _Cntllc1InXidOks_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 6),
    _Cntllc1InXidOks_Type()
)
cntllc1InXidOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InXidOks.setStatus("mandatory")
_Cntllc1InTestOks_Type = Counter32
_Cntllc1InTestOks_Object = MibTableColumn
cntllc1InTestOks = _Cntllc1InTestOks_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 7),
    _Cntllc1InTestOks_Type()
)
cntllc1InTestOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InTestOks.setStatus("mandatory")
_Cntllc1InSnapIps_Type = Counter32
_Cntllc1InSnapIps_Object = MibTableColumn
cntllc1InSnapIps = _Cntllc1InSnapIps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 8),
    _Cntllc1InSnapIps_Type()
)
cntllc1InSnapIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InSnapIps.setStatus("mandatory")
_Cntllc1InSnapArps_Type = Counter32
_Cntllc1InSnapArps_Object = MibTableColumn
cntllc1InSnapArps = _Cntllc1InSnapArps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 9),
    _Cntllc1InSnapArps_Type()
)
cntllc1InSnapArps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InSnapArps.setStatus("mandatory")
_Cntllc1InSnapNoProts_Type = Counter32
_Cntllc1InSnapNoProts_Object = MibTableColumn
cntllc1InSnapNoProts = _Cntllc1InSnapNoProts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 10),
    _Cntllc1InSnapNoProts_Type()
)
cntllc1InSnapNoProts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InSnapNoProts.setStatus("mandatory")
_Cntllc1InSnapNoTypes_Type = Counter32
_Cntllc1InSnapNoTypes_Object = MibTableColumn
cntllc1InSnapNoTypes = _Cntllc1InSnapNoTypes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 11),
    _Cntllc1InSnapNoTypes_Type()
)
cntllc1InSnapNoTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InSnapNoTypes.setStatus("mandatory")
_Cntllc1OutSnapIps_Type = Counter32
_Cntllc1OutSnapIps_Object = MibTableColumn
cntllc1OutSnapIps = _Cntllc1OutSnapIps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 12),
    _Cntllc1OutSnapIps_Type()
)
cntllc1OutSnapIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutSnapIps.setStatus("mandatory")
_Cntllc1OutSnapArps_Type = Counter32
_Cntllc1OutSnapArps_Object = MibTableColumn
cntllc1OutSnapArps = _Cntllc1OutSnapArps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 13),
    _Cntllc1OutSnapArps_Type()
)
cntllc1OutSnapArps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutSnapArps.setStatus("mandatory")
_Cntllc1OutXids_Type = Counter32
_Cntllc1OutXids_Object = MibTableColumn
cntllc1OutXids = _Cntllc1OutXids_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 14),
    _Cntllc1OutXids_Type()
)
cntllc1OutXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutXids.setStatus("mandatory")
_Cntllc1OutXidResps_Type = Counter32
_Cntllc1OutXidResps_Object = MibTableColumn
cntllc1OutXidResps = _Cntllc1OutXidResps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 15),
    _Cntllc1OutXidResps_Type()
)
cntllc1OutXidResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutXidResps.setStatus("mandatory")
_Cntllc1OutTests_Type = Counter32
_Cntllc1OutTests_Object = MibTableColumn
cntllc1OutTests = _Cntllc1OutTests_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 16),
    _Cntllc1OutTests_Type()
)
cntllc1OutTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutTests.setStatus("mandatory")
_Cntllc1OutTestResps_Type = Counter32
_Cntllc1OutTestResps_Object = MibTableColumn
cntllc1OutTestResps = _Cntllc1OutTestResps_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 17),
    _Cntllc1OutTestResps_Type()
)
cntllc1OutTestResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutTestResps.setStatus("mandatory")
_Cntllc1OutRetOks_Type = Counter32
_Cntllc1OutRetOks_Object = MibTableColumn
cntllc1OutRetOks = _Cntllc1OutRetOks_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 18),
    _Cntllc1OutRetOks_Type()
)
cntllc1OutRetOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutRetOks.setStatus("mandatory")
_Cntllc1OutFragPkts_Type = Counter32
_Cntllc1OutFragPkts_Object = MibTableColumn
cntllc1OutFragPkts = _Cntllc1OutFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 2, 1, 19),
    _Cntllc1OutFragPkts_Type()
)
cntllc1OutFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutFragPkts.setStatus("mandatory")
_Cntllc1ErrorTable_Object = MibTable
cntllc1ErrorTable = _Cntllc1ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3)
)
if mibBuilder.loadTexts:
    cntllc1ErrorTable.setStatus("mandatory")
_Cntllc1ErrorEntry_Object = MibTableRow
cntllc1ErrorEntry = _Cntllc1ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1)
)
cntllc1ErrorEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntllc1ErrorIndex"),
)
if mibBuilder.loadTexts:
    cntllc1ErrorEntry.setStatus("mandatory")
_Cntllc1ErrorIndex_Type = Integer32
_Cntllc1ErrorIndex_Object = MibTableColumn
cntllc1ErrorIndex = _Cntllc1ErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 1),
    _Cntllc1ErrorIndex_Type()
)
cntllc1ErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1ErrorIndex.setStatus("mandatory")
_Cntllc1ArpMailErrs_Type = Counter32
_Cntllc1ArpMailErrs_Object = MibTableColumn
cntllc1ArpMailErrs = _Cntllc1ArpMailErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 2),
    _Cntllc1ArpMailErrs_Type()
)
cntllc1ArpMailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1ArpMailErrs.setStatus("mandatory")
_Cntllc1IpMailErrs_Type = Counter32
_Cntllc1IpMailErrs_Object = MibTableColumn
cntllc1IpMailErrs = _Cntllc1IpMailErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 3),
    _Cntllc1IpMailErrs_Type()
)
cntllc1IpMailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1IpMailErrs.setStatus("mandatory")
_Cntllc1OutXmitErrs_Type = Counter32
_Cntllc1OutXmitErrs_Object = MibTableColumn
cntllc1OutXmitErrs = _Cntllc1OutXmitErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 4),
    _Cntllc1OutXmitErrs_Type()
)
cntllc1OutXmitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutXmitErrs.setStatus("mandatory")
_Cntllc1OutMcastErrs_Type = Counter32
_Cntllc1OutMcastErrs_Object = MibTableColumn
cntllc1OutMcastErrs = _Cntllc1OutMcastErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 5),
    _Cntllc1OutMcastErrs_Type()
)
cntllc1OutMcastErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutMcastErrs.setStatus("mandatory")
_Cntllc1XidErrs_Type = Counter32
_Cntllc1XidErrs_Object = MibTableColumn
cntllc1XidErrs = _Cntllc1XidErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 6),
    _Cntllc1XidErrs_Type()
)
cntllc1XidErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1XidErrs.setStatus("mandatory")
_Cntllc1TestErrs_Type = Counter32
_Cntllc1TestErrs_Object = MibTableColumn
cntllc1TestErrs = _Cntllc1TestErrs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 7),
    _Cntllc1TestErrs_Type()
)
cntllc1TestErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1TestErrs.setStatus("mandatory")
_Cntllc1InBadTypes_Type = Counter32
_Cntllc1InBadTypes_Object = MibTableColumn
cntllc1InBadTypes = _Cntllc1InBadTypes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 8),
    _Cntllc1InBadTypes_Type()
)
cntllc1InBadTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InBadTypes.setStatus("mandatory")
_Cntllc1OutMismIpSizes_Type = Counter32
_Cntllc1OutMismIpSizes_Object = MibTableColumn
cntllc1OutMismIpSizes = _Cntllc1OutMismIpSizes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 9),
    _Cntllc1OutMismIpSizes_Type()
)
cntllc1OutMismIpSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutMismIpSizes.setStatus("mandatory")
_Cntllc1OutBadIpSizes_Type = Counter32
_Cntllc1OutBadIpSizes_Object = MibTableColumn
cntllc1OutBadIpSizes = _Cntllc1OutBadIpSizes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 10),
    _Cntllc1OutBadIpSizes_Type()
)
cntllc1OutBadIpSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutBadIpSizes.setStatus("mandatory")
_Cntllc1InMismIpSizes_Type = Counter32
_Cntllc1InMismIpSizes_Object = MibTableColumn
cntllc1InMismIpSizes = _Cntllc1InMismIpSizes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 11),
    _Cntllc1InMismIpSizes_Type()
)
cntllc1InMismIpSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InMismIpSizes.setStatus("mandatory")
_Cntllc1InBadIpSizes_Type = Counter32
_Cntllc1InBadIpSizes_Object = MibTableColumn
cntllc1InBadIpSizes = _Cntllc1InBadIpSizes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 12),
    _Cntllc1InBadIpSizes_Type()
)
cntllc1InBadIpSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InBadIpSizes.setStatus("mandatory")
_Cntllc1InLateXids_Type = Counter32
_Cntllc1InLateXids_Object = MibTableColumn
cntllc1InLateXids = _Cntllc1InLateXids_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 13),
    _Cntllc1InLateXids_Type()
)
cntllc1InLateXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InLateXids.setStatus("mandatory")
_Cntllc1InLateTests_Type = Counter32
_Cntllc1InLateTests_Object = MibTableColumn
cntllc1InLateTests = _Cntllc1InLateTests_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 14),
    _Cntllc1InLateTests_Type()
)
cntllc1InLateTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1InLateTests.setStatus("mandatory")
_Cntllc1OutTooBigs_Type = Counter32
_Cntllc1OutTooBigs_Object = MibTableColumn
cntllc1OutTooBigs = _Cntllc1OutTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 15),
    _Cntllc1OutTooBigs_Type()
)
cntllc1OutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutTooBigs.setStatus("mandatory")
_Cntllc1OutNoRooms_Type = Counter32
_Cntllc1OutNoRooms_Object = MibTableColumn
cntllc1OutNoRooms = _Cntllc1OutNoRooms_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 16),
    _Cntllc1OutNoRooms_Type()
)
cntllc1OutNoRooms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutNoRooms.setStatus("mandatory")
_Cntllc1OutRetBads_Type = Counter32
_Cntllc1OutRetBads_Object = MibTableColumn
cntllc1OutRetBads = _Cntllc1OutRetBads_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 13, 3, 3, 1, 17),
    _Cntllc1OutRetBads_Type()
)
cntllc1OutRetBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntllc1OutRetBads.setStatus("mandatory")
_Cntlua_ObjectIdentity = ObjectIdentity
cntlua = _Cntlua_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 1, 14)
)
_CntLuaCount_Type = Integer32
_CntLuaCount_Object = MibScalar
cntLuaCount = _CntLuaCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 1),
    _CntLuaCount_Type()
)
cntLuaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntLuaCount.setStatus("mandatory")
_CntLuaTable_Object = MibTable
cntLuaTable = _CntLuaTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2)
)
if mibBuilder.loadTexts:
    cntLuaTable.setStatus("mandatory")
_CntluaEntry_Object = MibTableRow
cntluaEntry = _CntluaEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1)
)
cntluaEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntluaIf"),
)
if mibBuilder.loadTexts:
    cntluaEntry.setStatus("mandatory")
_CntluaIf_Type = Integer32
_CntluaIf_Object = MibTableColumn
cntluaIf = _CntluaIf_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 1),
    _CntluaIf_Type()
)
cntluaIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntluaIf.setStatus("mandatory")
_CntluaNumber_Type = Integer32
_CntluaNumber_Object = MibTableColumn
cntluaNumber = _CntluaNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 2),
    _CntluaNumber_Type()
)
cntluaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntluaNumber.setStatus("mandatory")
_CntSubChanCount_Type = Integer32
_CntSubChanCount_Object = MibTableColumn
cntSubChanCount = _CntSubChanCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 3),
    _CntSubChanCount_Type()
)
cntSubChanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntSubChanCount.setStatus("mandatory")
_CntSubChanTable_Object = MibTable
cntSubChanTable = _CntSubChanTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cntSubChanTable.setStatus("mandatory")
_CntsubchanEntry_Object = MibTableRow
cntsubchanEntry = _CntsubchanEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1)
)
cntsubchanEntry.setIndexNames(
    (0, "CNTAU-MIB", "cntsctIndex"),
)
if mibBuilder.loadTexts:
    cntsubchanEntry.setStatus("mandatory")
_CntsctIndex_Type = Integer32
_CntsctIndex_Object = MibTableColumn
cntsctIndex = _CntsctIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 1),
    _CntsctIndex_Type()
)
cntsctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctIndex.setStatus("mandatory")
_CntsctNumber_Type = Integer32
_CntsctNumber_Object = MibTableColumn
cntsctNumber = _CntsctNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 2),
    _CntsctNumber_Type()
)
cntsctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctNumber.setStatus("mandatory")
_CntsctTxStatus_Type = Integer32
_CntsctTxStatus_Object = MibTableColumn
cntsctTxStatus = _CntsctTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 3),
    _CntsctTxStatus_Type()
)
cntsctTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctTxStatus.setStatus("mandatory")
_CntsctRxStatus_Type = Integer32
_CntsctRxStatus_Object = MibTableColumn
cntsctRxStatus = _CntsctRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 4),
    _CntsctRxStatus_Type()
)
cntsctRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctRxStatus.setStatus("mandatory")
_CntsctSubChanStatus_Type = Integer32
_CntsctSubChanStatus_Object = MibTableColumn
cntsctSubChanStatus = _CntsctSubChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 5),
    _CntsctSubChanStatus_Type()
)
cntsctSubChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctSubChanStatus.setStatus("mandatory")
_CntsctState_Type = Integer32
_CntsctState_Object = MibTableColumn
cntsctState = _CntsctState_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 6),
    _CntsctState_Type()
)
cntsctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctState.setStatus("mandatory")
_CntsctRxCredit_Type = Integer32
_CntsctRxCredit_Object = MibTableColumn
cntsctRxCredit = _CntsctRxCredit_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 7),
    _CntsctRxCredit_Type()
)
cntsctRxCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctRxCredit.setStatus("mandatory")
_CntsctRxMsgs_Type = Counter32
_CntsctRxMsgs_Object = MibTableColumn
cntsctRxMsgs = _CntsctRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 8),
    _CntsctRxMsgs_Type()
)
cntsctRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctRxMsgs.setStatus("mandatory")
_CntsctRxMsgBytes_Type = Counter32
_CntsctRxMsgBytes_Object = MibTableColumn
cntsctRxMsgBytes = _CntsctRxMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 9),
    _CntsctRxMsgBytes_Type()
)
cntsctRxMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctRxMsgBytes.setStatus("mandatory")
_CntsctRxDataBytes_Type = Counter32
_CntsctRxDataBytes_Object = MibTableColumn
cntsctRxDataBytes = _CntsctRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 10),
    _CntsctRxDataBytes_Type()
)
cntsctRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctRxDataBytes.setStatus("mandatory")
_CntsctTxMsgs_Type = Counter32
_CntsctTxMsgs_Object = MibTableColumn
cntsctTxMsgs = _CntsctTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 11),
    _CntsctTxMsgs_Type()
)
cntsctTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctTxMsgs.setStatus("mandatory")
_CntsctTxMsgBytes_Type = Counter32
_CntsctTxMsgBytes_Object = MibTableColumn
cntsctTxMsgBytes = _CntsctTxMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 12),
    _CntsctTxMsgBytes_Type()
)
cntsctTxMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctTxMsgBytes.setStatus("mandatory")
_CntsctTxDataBytes_Type = Counter32
_CntsctTxDataBytes_Object = MibTableColumn
cntsctTxDataBytes = _CntsctTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 13),
    _CntsctTxDataBytes_Type()
)
cntsctTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctTxDataBytes.setStatus("mandatory")
_CntsctTxErrMsgs_Type = Counter32
_CntsctTxErrMsgs_Object = MibTableColumn
cntsctTxErrMsgs = _CntsctTxErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 14),
    _CntsctTxErrMsgs_Type()
)
cntsctTxErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctTxErrMsgs.setStatus("mandatory")
_CntsctTotalBytes_Type = Counter32
_CntsctTotalBytes_Object = MibTableColumn
cntsctTotalBytes = _CntsctTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 15),
    _CntsctTotalBytes_Type()
)
cntsctTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctTotalBytes.setStatus("mandatory")
_CntsctDrecPid_Type = DisplayString
_CntsctDrecPid_Object = MibTableColumn
cntsctDrecPid = _CntsctDrecPid_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 16),
    _CntsctDrecPid_Type()
)
cntsctDrecPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctDrecPid.setStatus("mandatory")
_CntsctDrecTask_Type = DisplayString
_CntsctDrecTask_Object = MibTableColumn
cntsctDrecTask = _CntsctDrecTask_Object(
    (1, 3, 6, 1, 4, 1, 333, 1, 14, 2, 1, 4, 1, 17),
    _CntsctDrecTask_Type()
)
cntsctDrecTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntsctDrecTask.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cntInformationalMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 1, 0, 1)
)
cntInformationalMsg.setObjects(
      *(("CNTAU-MIB", "cntMsgTaskName"),
        ("CNTAU-MIB", "cntMsgNumber"),
        ("CNTAU-MIB", "cntMsgCpuNumber"),
        ("CNTAU-MIB", "cntMsgNodeNumber"),
        ("CNTAU-MIB", "cntMsgDateTime"),
        ("CNTAU-MIB", "cntMsgContent"))
)
if mibBuilder.loadTexts:
    cntInformationalMsg.setStatus(
        ""
    )

cntPossibleErrMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 1, 0, 2)
)
cntPossibleErrMsg.setObjects(
      *(("CNTAU-MIB", "cntMsgTaskName"),
        ("CNTAU-MIB", "cntMsgNumber"),
        ("CNTAU-MIB", "cntMsgCpuNumber"),
        ("CNTAU-MIB", "cntMsgNodeNumber"),
        ("CNTAU-MIB", "cntMsgDateTime"),
        ("CNTAU-MIB", "cntMsgContent"))
)
if mibBuilder.loadTexts:
    cntPossibleErrMsg.setStatus(
        ""
    )

cntSevereErrMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 1, 0, 3)
)
cntSevereErrMsg.setObjects(
      *(("CNTAU-MIB", "cntMsgTaskName"),
        ("CNTAU-MIB", "cntMsgNumber"),
        ("CNTAU-MIB", "cntMsgCpuNumber"),
        ("CNTAU-MIB", "cntMsgNodeNumber"),
        ("CNTAU-MIB", "cntMsgDateTime"),
        ("CNTAU-MIB", "cntMsgContent"))
)
if mibBuilder.loadTexts:
    cntSevereErrMsg.setStatus(
        ""
    )

cntCriticalErrMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 1, 0, 4)
)
cntCriticalErrMsg.setObjects(
      *(("CNTAU-MIB", "cntMsgTaskName"),
        ("CNTAU-MIB", "cntMsgNumber"),
        ("CNTAU-MIB", "cntMsgCpuNumber"),
        ("CNTAU-MIB", "cntMsgNodeNumber"),
        ("CNTAU-MIB", "cntMsgDateTime"),
        ("CNTAU-MIB", "cntMsgContent"))
)
if mibBuilder.loadTexts:
    cntCriticalErrMsg.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNTAU-MIB",
    **{"cnt": cnt,
       "cntau": cntau,
       "cntInformationalMsg": cntInformationalMsg,
       "cntPossibleErrMsg": cntPossibleErrMsg,
       "cntSevereErrMsg": cntSevereErrMsg,
       "cntCriticalErrMsg": cntCriticalErrMsg,
       "cntsystem": cntsystem,
       "cntSysNodeAddress": cntSysNodeAddress,
       "cntSysTimeofDay": cntSysTimeofDay,
       "cntSysMsgTable": cntSysMsgTable,
       "cntMsgEntry": cntMsgEntry,
       "cntMsgIndex": cntMsgIndex,
       "cntMsgSeverity": cntMsgSeverity,
       "cntMsgTaskName": cntMsgTaskName,
       "cntMsgNumber": cntMsgNumber,
       "cntMsgCpuNumber": cntMsgCpuNumber,
       "cntMsgNodeNumber": cntMsgNodeNumber,
       "cntMsgDateTime": cntMsgDateTime,
       "cntMsgContent": cntMsgContent,
       "cntMsgSeqNumber": cntMsgSeqNumber,
       "cntSysHardware": cntSysHardware,
       "cntHwBBramType": cntHwBBramType,
       "cntHwBBramStatus": cntHwBBramStatus,
       "cntHwFailedCpu": cntHwFailedCpu,
       "cntHwMonCpu": cntHwMonCpu,
       "cntHwFailStatus": cntHwFailStatus,
       "cntHwMonFailStatus": cntHwMonFailStatus,
       "cntHwFailDate": cntHwFailDate,
       "cntHwReset1Why": cntHwReset1Why,
       "cntHwReset1Date": cntHwReset1Date,
       "cntHwReset2Why": cntHwReset2Why,
       "cntHwReset2Date": cntHwReset2Date,
       "cntHwReset3Why": cntHwReset3Why,
       "cntHwReset3Date": cntHwReset3Date,
       "cntHwPowerSupply": cntHwPowerSupply,
       "cntHwCpuTable": cntHwCpuTable,
       "cntHwCpuEntry": cntHwCpuEntry,
       "cntCpuNum": cntCpuNum,
       "cntCpuType": cntCpuType,
       "cntCpuSemCount": cntCpuSemCount,
       "cntCpuSemLost": cntCpuSemLost,
       "cntCpuStatus": cntCpuStatus,
       "cntCpuMonStatus": cntCpuMonStatus,
       "cntCpuPollStatus": cntCpuPollStatus,
       "cntCpuPolls": cntCpuPolls,
       "cntCpuResetDelayTime": cntCpuResetDelayTime,
       "cntCpuMonBy": cntCpuMonBy,
       "cntCpuPort": cntCpuPort,
       "cntCpuUnclaims": cntCpuUnclaims,
       "cntCpuXtraInts": cntCpuXtraInts,
       "cntCpuLevel7s": cntCpuLevel7s,
       "cntCpuMsgRets": cntCpuMsgRets,
       "cntCpuMsgHolds": cntCpuMsgHolds,
       "cntCpuResetFlag": cntCpuResetFlag,
       "cntCpuUtil": cntCpuUtil,
       "cntCpuLastFailDate": cntCpuLastFailDate,
       "cntCpuLastChgDate": cntCpuLastChgDate,
       "cntHwStatusLED": cntHwStatusLED,
       "cntSysBuild": cntSysBuild,
       "cntRevDate": cntRevDate,
       "cntCustomer": cntCustomer,
       "cntMachineType": cntMachineType,
       "cntSerialNumber": cntSerialNumber,
       "cntWorkOrderNumber": cntWorkOrderNumber,
       "cntChassisNumber": cntChassisNumber,
       "cntModelNumber": cntModelNumber,
       "cntReleaseLevel": cntReleaseLevel,
       "cntRevEditDate": cntRevEditDate,
       "cntRevEditTime": cntRevEditTime,
       "cntFeatureTable": cntFeatureTable,
       "cntFeatureEntry": cntFeatureEntry,
       "cntFeatureIndex": cntFeatureIndex,
       "cntFeatureName": cntFeatureName,
       "cntFeatureQuantity": cntFeatureQuantity,
       "cntFeatureDescr": cntFeatureDescr,
       "cntSlotTable": cntSlotTable,
       "cntSlotEntry": cntSlotEntry,
       "cntSlotIndex": cntSlotIndex,
       "cntSlotName": cntSlotName,
       "cntSlotPartNumber": cntSlotPartNumber,
       "cntSlotSerialNumber": cntSlotSerialNumber,
       "cntSlotRevLevel": cntSlotRevLevel,
       "cntSlotInterface": cntSlotInterface,
       "cntSlotCpuNumber": cntSlotCpuNumber,
       "cntSlotVMEbusGrant": cntSlotVMEbusGrant,
       "cntIOTable": cntIOTable,
       "cntIOEntry": cntIOEntry,
       "cntIOIndex": cntIOIndex,
       "cntIOName": cntIOName,
       "cntIOPartNumber": cntIOPartNumber,
       "cntIOSerialNumber": cntIOSerialNumber,
       "cntIORevLevel": cntIORevLevel,
       "cntIOInterface": cntIOInterface,
       "cntIOCpuNumber": cntIOCpuNumber,
       "cntPowerTable": cntPowerTable,
       "cntPowerEntry": cntPowerEntry,
       "cntPowerIndex": cntPowerIndex,
       "cntPowerName": cntPowerName,
       "cntPowerPartNumber": cntPowerPartNumber,
       "cntPowerSerialNumber": cntPowerSerialNumber,
       "cntPowerRevLevel": cntPowerRevLevel,
       "cntSCRTable": cntSCRTable,
       "cntSCREntry": cntSCREntry,
       "cntSCRIndex": cntSCRIndex,
       "cntSCRNumber": cntSCRNumber,
       "cntSerialAlfaNumber": cntSerialAlfaNumber,
       "cntSysMemory": cntSysMemory,
       "cntMemBBramAddress": cntMemBBramAddress,
       "cntMemBBramSpace": cntMemBBramSpace,
       "cntMemBBramFree": cntMemBBramFree,
       "cntMemSramAddress": cntMemSramAddress,
       "cntMemSramSpace": cntMemSramSpace,
       "cntMemSramFree": cntMemSramFree,
       "cntSysCpuTable": cntSysCpuTable,
       "cntSysCpuEntry": cntSysCpuEntry,
       "cntCpuIndex": cntCpuIndex,
       "cntCpuMemSpace": cntCpuMemSpace,
       "cntCpuMemFree": cntCpuMemFree,
       "cntCpuTaskTable": cntCpuTaskTable,
       "cntCpuTaskEntry": cntCpuTaskEntry,
       "cntCpuTaskIndex": cntCpuTaskIndex,
       "cntCpuTaskName": cntCpuTaskName,
       "cntinterfaces": cntinterfaces,
       "cntifTable": cntifTable,
       "cntifEntry": cntifEntry,
       "cntifIndex": cntifIndex,
       "cntifType": cntifType,
       "cntifCpu": cntifCpu,
       "cntifSubIndex": cntifSubIndex,
       "cntIfsState": cntIfsState,
       "cnticmp": cnticmp,
       "cnticmpInDuNets": cnticmpInDuNets,
       "cnticmpInDuHosts": cnticmpInDuHosts,
       "cnticmpInDuProtos": cnticmpInDuProtos,
       "cnticmpInDuPorts": cnticmpInDuPorts,
       "cnticmpInDuFrags": cnticmpInDuFrags,
       "cnticmpInDuSources": cnticmpInDuSources,
       "cnticmpInTmXceeds": cnticmpInTmXceeds,
       "cnticmpInTmFrags": cnticmpInTmFrags,
       "cnticmpInReNets": cnticmpInReNets,
       "cnticmpInReHosts": cnticmpInReHosts,
       "cnticmpInReServnets": cnticmpInReServnets,
       "cnticmpInReServhosts": cnticmpInReServhosts,
       "cnticmpOutDuNets": cnticmpOutDuNets,
       "cnticmpOutDuHosts": cnticmpOutDuHosts,
       "cnticmpOutDuProtos": cnticmpOutDuProtos,
       "cnticmpOutDuPorts": cnticmpOutDuPorts,
       "cnticmpOutDuFrags": cnticmpOutDuFrags,
       "cnticmpOutDuSources": cnticmpOutDuSources,
       "cnticmpOutTmXceeds": cnticmpOutTmXceeds,
       "cnticmpOutTmFrags": cnticmpOutTmFrags,
       "cnticmpOutReNets": cnticmpOutReNets,
       "cnticmpOutReHosts": cnticmpOutReHosts,
       "cnticmpOutReServnets": cnticmpOutReServnets,
       "cnticmpOutReServhosts": cnticmpOutReServhosts,
       "cnttransmission": cnttransmission,
       "cntdot3": cntdot3,
       "cntdot3Table": cntdot3Table,
       "cntdot3Entry": cntdot3Entry,
       "cntdot3Index": cntdot3Index,
       "cntdot3SoftwareID": cntdot3SoftwareID,
       "cntdot3BufsAllocated": cntdot3BufsAllocated,
       "cntdot3BufTooManys": cntdot3BufTooManys,
       "cntdot3BufNotAvails": cntdot3BufNotAvails,
       "cntdot3BufPriority": cntdot3BufPriority,
       "cntdot3PICBusErrs": cntdot3PICBusErrs,
       "cntdot3PICDMAErrs": cntdot3PICDMAErrs,
       "cntdot3PICMemSeqErrs": cntdot3PICMemSeqErrs,
       "cntdot3PICMemParityErrs": cntdot3PICMemParityErrs,
       "cntdot3PICSpuriousInts": cntdot3PICSpuriousInts,
       "cntdot3LanceInts": cntdot3LanceInts,
       "cntdot3LanceParityErrs": cntdot3LanceParityErrs,
       "cntdot3LanceMemErrs": cntdot3LanceMemErrs,
       "cntdot3LanceMissedPkts": cntdot3LanceMissedPkts,
       "cntdot3LanceUnderFlows": cntdot3LanceUnderFlows,
       "cntdot3LanceOverFlows": cntdot3LanceOverFlows,
       "cntdot3LanceTxWaitQ": cntdot3LanceTxWaitQ,
       "cntdot3DMAChan1RxErr": cntdot3DMAChan1RxErr,
       "cntdot3DMAChan3RxErr": cntdot3DMAChan3RxErr,
       "cntdot3DMAChan0TxErr": cntdot3DMAChan0TxErr,
       "cntdot3DMAChan2TxErr": cntdot3DMAChan2TxErr,
       "cntdot3DMAChan1RxErrs": cntdot3DMAChan1RxErrs,
       "cntdot3DMAChan3RxErrs": cntdot3DMAChan3RxErrs,
       "cntdot3DMAChan0TxErrs": cntdot3DMAChan0TxErrs,
       "cntdot3DMAChan2TxErrs": cntdot3DMAChan2TxErrs,
       "cntdot3DMARxWaitQ": cntdot3DMARxWaitQ,
       "cntdot3DMATxWaitQ": cntdot3DMATxWaitQ,
       "cntdot3LPXParityErrs": cntdot3LPXParityErrs,
       "cntdot3Chan1Misreads": cntdot3Chan1Misreads,
       "cntfddi": cntfddi,
       "cntFddiSMT": cntFddiSMT,
       "cntFddiSMTNumber": cntFddiSMTNumber,
       "cntFddiSMTTable": cntFddiSMTTable,
       "cntFddiSMTEntry": cntFddiSMTEntry,
       "cntFddiSMTIndex": cntFddiSMTIndex,
       "cntFddiSMTManufacturerData": cntFddiSMTManufacturerData,
       "cntFddiSMTUserData": cntFddiSMTUserData,
       "cntFddiSMTReportLimit": cntFddiSMTReportLimit,
       "cntFddiSMTMsgTimeStamp": cntFddiSMTMsgTimeStamp,
       "cntFddiSMTTransitionTimeStamp": cntFddiSMTTransitionTimeStamp,
       "cntFddiSMTSetCount": cntFddiSMTSetCount,
       "cntFddiSMTLastSetStationID": cntFddiSMTLastSetStationID,
       "cntFddiMAC": cntFddiMAC,
       "cntFddiMACNumber": cntFddiMACNumber,
       "cntFddiMACTable": cntFddiMACTable,
       "cntFddiMACEntry": cntFddiMACEntry,
       "cntFddiMACSMTIndex": cntFddiMACSMTIndex,
       "cntFddiMACIndex": cntFddiMACIndex,
       "cntFddiMACBridgeFunction": cntFddiMACBridgeFunction,
       "cntFddiMACDownstreamNbr": cntFddiMACDownstreamNbr,
       "cntFddiMACOldDownstreamNbr": cntFddiMACOldDownstreamNbr,
       "cntFddiMACRootConcentratorMac": cntFddiMACRootConcentratorMac,
       "cntFddiMACLongAlias": cntFddiMACLongAlias,
       "cntFddiMACShortAlias": cntFddiMACShortAlias,
       "cntFddiMACLongGrpAddr": cntFddiMACLongGrpAddr,
       "cntFddiMACShortGrpAddr": cntFddiMACShortGrpAddr,
       "cntFddiMACTPri0": cntFddiMACTPri0,
       "cntFddiMACTPri1": cntFddiMACTPri1,
       "cntFddiMACTPri2": cntFddiMACTPri2,
       "cntFddiMACTPri3": cntFddiMACTPri3,
       "cntFddiMACTPri4": cntFddiMACTPri4,
       "cntFddiMACTPri5": cntFddiMACTPri5,
       "cntFddiMACTPri6": cntFddiMACTPri6,
       "cntFddiMACCopies": cntFddiMACCopies,
       "cntFddiMACTransmits": cntFddiMACTransmits,
       "cntFddiMACTokens": cntFddiMACTokens,
       "cntFddiMACTvxExpires": cntFddiMACTvxExpires,
       "cntFddiMACNotCopies": cntFddiMACNotCopies,
       "cntFddiMACLates": cntFddiMACLates,
       "cntFddiMACRingOps": cntFddiMACRingOps,
       "cntFddiMACBaseFrames": cntFddiMACBaseFrames,
       "cntFddiMACBaseErrs": cntFddiMACBaseErrs,
       "cntFddiMACBaseLosts": cntFddiMACBaseLosts,
       "cntFddiMACBaseTimeFrameError": cntFddiMACBaseTimeFrameError,
       "cntFddiMACBaseNotCopies": cntFddiMACBaseNotCopies,
       "cntFddiMACBaseTimeNotCopied": cntFddiMACBaseTimeNotCopied,
       "cntFddiMACNotCopiedThreshold": cntFddiMACNotCopiedThreshold,
       "cntFddiMACBaseCopies": cntFddiMACBaseCopies,
       "cntFddiMACNotCopiedRatio": cntFddiMACNotCopiedRatio,
       "cntFddiMACNotCopiedCondition": cntFddiMACNotCopiedCondition,
       "cntFddiMACLLCServiceAvailable": cntFddiMACLLCServiceAvailable,
       "cntFddiMACMasterSlaveLoopStatus": cntFddiMACMasterSlaveLoopStatus,
       "cntFddiMACRootMACDownStreamPORTType": cntFddiMACRootMACDownStreamPORTType,
       "cntFddiMACRootMACCurrentPath": cntFddiMACRootMACCurrentPath,
       "cntFddiPATH": cntFddiPATH,
       "cntFddiPATHNumber": cntFddiPATHNumber,
       "cntFddiPATHTable": cntFddiPATHTable,
       "cntFddiPATHEntry": cntFddiPATHEntry,
       "cntFddiPATHSMTIndex": cntFddiPATHSMTIndex,
       "cntFddiPATHIndex": cntFddiPATHIndex,
       "cntFddiPATHTraceMaxExpiration": cntFddiPATHTraceMaxExpiration,
       "cntFddiPATHTVXLowerBound": cntFddiPATHTVXLowerBound,
       "cntFddiPATHTMaxLowerBound": cntFddiPATHTMaxLowerBound,
       "cntFddiPATHType": cntFddiPATHType,
       "cntFddiPATHPORTOrder": cntFddiPATHPORTOrder,
       "cntFddiPATHRingLatency": cntFddiPATHRingLatency,
       "cntFddiPATHTraceStatus": cntFddiPATHTraceStatus,
       "cntFddiPATHSba": cntFddiPATHSba,
       "cntFddiPATHSbaOverhead": cntFddiPATHSbaOverhead,
       "cntFddiPATHStatus": cntFddiPATHStatus,
       "cntFddiPATHTRmode": cntFddiPATHTRmode,
       "cntFddiPORT": cntFddiPORT,
       "cntFddiPORTNumber": cntFddiPORTNumber,
       "cntFddiPORTTable": cntFddiPORTTable,
       "cntFddiPORTEntry": cntFddiPORTEntry,
       "cntFddiPORTSMTIndex": cntFddiPORTSMTIndex,
       "cntFddiPORTIndex": cntFddiPORTIndex,
       "cntFddiPORTFotxClass": cntFddiPORTFotxClass,
       "cntFddiPORTMaintLineState": cntFddiPORTMaintLineState,
       "cntFddiPORTEBErrs": cntFddiPORTEBErrs,
       "cntFddiPORTBaseLerEstimate": cntFddiPORTBaseLerEstimate,
       "cntFddiPORTBaseLemRejects": cntFddiPORTBaseLemRejects,
       "cntFddiPORTBaseLems": cntFddiPORTBaseLems,
       "cntFddiPORTBaseLerTimeStamp": cntFddiPORTBaseLerTimeStamp,
       "cntsnmp": cntsnmp,
       "cntsnmpconfig": cntsnmpconfig,
       "cntMibVersion": cntMibVersion,
       "cntMibObjectCount": cntMibObjectCount,
       "cntConfigVersion": cntConfigVersion,
       "cntProxyStatus": cntProxyStatus,
       "cntProxyCount": cntProxyCount,
       "cntSnmpBufferCount": cntSnmpBufferCount,
       "cntIfPollInterval": cntIfPollInterval,
       "cntIfNextPoll": cntIfNextPoll,
       "cntDoDIPCount": cntDoDIPCount,
       "cntDot3Count": cntDot3Count,
       "cntFddiCount": cntFddiCount,
       "cntFddiPortCount": cntFddiPortCount,
       "cntDataLinkCount": cntDataLinkCount,
       "cntLLC1Count": cntLLC1Count,
       "cntCofiVersion": cntCofiVersion,
       "cntsnmpstat": cntsnmpstat,
       "cntMib2Requests": cntMib2Requests,
       "cntFddiRequests": cntFddiRequests,
       "cntDot3Requests": cntDot3Requests,
       "cntCntRequests": cntCntRequests,
       "cntRowAdditions": cntRowAdditions,
       "cntRowModifies": cntRowModifies,
       "cntRowDeletions": cntRowDeletions,
       "cntRowErrors": cntRowErrors,
       "cntBadVersions": cntBadVersions,
       "cntNoBuffers": cntNoBuffers,
       "cntMailTimeouts": cntMailTimeouts,
       "cntCachedResponses": cntCachedResponses,
       "cntUsedCaches": cntUsedCaches,
       "cntsnmptrap": cntsnmptrap,
       "cntTrapDestCount": cntTrapDestCount,
       "cntLastTrapMsg": cntLastTrapMsg,
       "cntTrapTable": cntTrapTable,
       "cnttrapEntry": cnttrapEntry,
       "cnttrapIndex": cnttrapIndex,
       "cnttrapAddress": cnttrapAddress,
       "cntsnmpTrapFlags": cntsnmpTrapFlags,
       "cntTrapFlags": cntTrapFlags,
       "cnttrapIf": cnttrapIf,
       "cntsnmpproxy": cntsnmpproxy,
       "cntProxyTable": cntProxyTable,
       "cntproxyEntry": cntproxyEntry,
       "cntproxyIndex": cntproxyIndex,
       "cntproxyAddress": cntproxyAddress,
       "cntproxyNode": cntproxyNode,
       "cntdiagnostics": cntdiagnostics,
       "cntTraceTable": cntTraceTable,
       "cnttraceEntry": cnttraceEntry,
       "cnttraceIndex": cnttraceIndex,
       "cnttraceType": cnttraceType,
       "cnttraceCpu": cnttraceCpu,
       "cnttraceData": cnttraceData,
       "cntMailQueue": cntMailQueue,
       "cntMDMTable": cntMDMTable,
       "cntMDMEntry": cntMDMEntry,
       "cntmdmQIndex": cntmdmQIndex,
       "cntmdmQName": cntmdmQName,
       "cntmdmQProcessId": cntmdmQProcessId,
       "cntmdmQTaskId": cntmdmQTaskId,
       "cntmdmQList": cntmdmQList,
       "cntdatalink": cntdatalink,
       "cntdlNumber": cntdlNumber,
       "cntdlTable": cntdlTable,
       "cntdlEntry": cntdlEntry,
       "cntdlIndex": cntdlIndex,
       "cntdlDescr": cntdlDescr,
       "cntdlType": cntdlType,
       "cntdlTypeofService": cntdlTypeofService,
       "cntdlMtu": cntdlMtu,
       "cntdlPortAddrLen": cntdlPortAddrLen,
       "cntdlMaxPort": cntdlMaxPort,
       "cntdlActivePort": cntdlActivePort,
       "cntdlInOctets": cntdlInOctets,
       "cntdlInUcastPkts": cntdlInUcastPkts,
       "cntdlInNUcastPkts": cntdlInNUcastPkts,
       "cntdlInDiscards": cntdlInDiscards,
       "cntdlInErrors": cntdlInErrors,
       "cntdlInUnknownProtos": cntdlInUnknownProtos,
       "cntdlOutOctets": cntdlOutOctets,
       "cntdlOutUcastPkts": cntdlOutUcastPkts,
       "cntdlOutNUcastPkts": cntdlOutNUcastPkts,
       "cntdlOutDiscards": cntdlOutDiscards,
       "cntdlOutErrors": cntdlOutErrors,
       "cntdlOutQLen": cntdlOutQLen,
       "cntdlPortTable": cntdlPortTable,
       "cntdlPortEntry": cntdlPortEntry,
       "cntdlPortIndex": cntdlPortIndex,
       "cntdlState": cntdlState,
       "cntdlSourcePort": cntdlSourcePort,
       "cntdlDestPort": cntdlDestPort,
       "cntdlPortType": cntdlPortType,
       "cntllc1": cntllc1,
       "cntllc1ConfigTable": cntllc1ConfigTable,
       "cntllc1ConfigEntry": cntllc1ConfigEntry,
       "cntllc1ConfigIndex": cntllc1ConfigIndex,
       "cntllc1DriverType": cntllc1DriverType,
       "cntllc1Addr": cntllc1Addr,
       "cntllc1InitFlag": cntllc1InitFlag,
       "cntllc1TraceFlag": cntllc1TraceFlag,
       "cntllc1BufCnt": cntllc1BufCnt,
       "cntllc1BusId": cntllc1BusId,
       "cntllc1CpuNum": cntllc1CpuNum,
       "cntllc1BufPriority": cntllc1BufPriority,
       "cntllc1WaitTimeOut": cntllc1WaitTimeOut,
       "cntllc1StatsTable": cntllc1StatsTable,
       "cntllc1StatsEntry": cntllc1StatsEntry,
       "cntllc1StatIndex": cntllc1StatIndex,
       "cntllc1InXids": cntllc1InXids,
       "cntllc1InTests": cntllc1InTests,
       "cntllc1InUIs": cntllc1InUIs,
       "cntllc1InNoDsaps": cntllc1InNoDsaps,
       "cntllc1InXidOks": cntllc1InXidOks,
       "cntllc1InTestOks": cntllc1InTestOks,
       "cntllc1InSnapIps": cntllc1InSnapIps,
       "cntllc1InSnapArps": cntllc1InSnapArps,
       "cntllc1InSnapNoProts": cntllc1InSnapNoProts,
       "cntllc1InSnapNoTypes": cntllc1InSnapNoTypes,
       "cntllc1OutSnapIps": cntllc1OutSnapIps,
       "cntllc1OutSnapArps": cntllc1OutSnapArps,
       "cntllc1OutXids": cntllc1OutXids,
       "cntllc1OutXidResps": cntllc1OutXidResps,
       "cntllc1OutTests": cntllc1OutTests,
       "cntllc1OutTestResps": cntllc1OutTestResps,
       "cntllc1OutRetOks": cntllc1OutRetOks,
       "cntllc1OutFragPkts": cntllc1OutFragPkts,
       "cntllc1ErrorTable": cntllc1ErrorTable,
       "cntllc1ErrorEntry": cntllc1ErrorEntry,
       "cntllc1ErrorIndex": cntllc1ErrorIndex,
       "cntllc1ArpMailErrs": cntllc1ArpMailErrs,
       "cntllc1IpMailErrs": cntllc1IpMailErrs,
       "cntllc1OutXmitErrs": cntllc1OutXmitErrs,
       "cntllc1OutMcastErrs": cntllc1OutMcastErrs,
       "cntllc1XidErrs": cntllc1XidErrs,
       "cntllc1TestErrs": cntllc1TestErrs,
       "cntllc1InBadTypes": cntllc1InBadTypes,
       "cntllc1OutMismIpSizes": cntllc1OutMismIpSizes,
       "cntllc1OutBadIpSizes": cntllc1OutBadIpSizes,
       "cntllc1InMismIpSizes": cntllc1InMismIpSizes,
       "cntllc1InBadIpSizes": cntllc1InBadIpSizes,
       "cntllc1InLateXids": cntllc1InLateXids,
       "cntllc1InLateTests": cntllc1InLateTests,
       "cntllc1OutTooBigs": cntllc1OutTooBigs,
       "cntllc1OutNoRooms": cntllc1OutNoRooms,
       "cntllc1OutRetBads": cntllc1OutRetBads,
       "cntlua": cntlua,
       "cntLuaCount": cntLuaCount,
       "cntLuaTable": cntLuaTable,
       "cntluaEntry": cntluaEntry,
       "cntluaIf": cntluaIf,
       "cntluaNumber": cntluaNumber,
       "cntSubChanCount": cntSubChanCount,
       "cntSubChanTable": cntSubChanTable,
       "cntsubchanEntry": cntsubchanEntry,
       "cntsctIndex": cntsctIndex,
       "cntsctNumber": cntsctNumber,
       "cntsctTxStatus": cntsctTxStatus,
       "cntsctRxStatus": cntsctRxStatus,
       "cntsctSubChanStatus": cntsctSubChanStatus,
       "cntsctState": cntsctState,
       "cntsctRxCredit": cntsctRxCredit,
       "cntsctRxMsgs": cntsctRxMsgs,
       "cntsctRxMsgBytes": cntsctRxMsgBytes,
       "cntsctRxDataBytes": cntsctRxDataBytes,
       "cntsctTxMsgs": cntsctTxMsgs,
       "cntsctTxMsgBytes": cntsctTxMsgBytes,
       "cntsctTxDataBytes": cntsctTxDataBytes,
       "cntsctTxErrMsgs": cntsctTxErrMsgs,
       "cntsctTotalBytes": cntsctTotalBytes,
       "cntsctDrecPid": cntsctDrecPid,
       "cntsctDrecTask": cntsctDrecTask}
)
