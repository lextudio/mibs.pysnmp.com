# SNMP MIB module (S5-ETH-MULTISEG-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-ETH-MULTISEG-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:05 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(s5EnMsTop,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5EnMsTop")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(SnpxBackplaneType,
 SnpxChassisType) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "SnpxBackplaneType",
    "SnpxChassisType")


# MODULE-IDENTITY

s5EthMultisegTopologyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 0)
)
s5EthMultisegTopologyMib.setRevisions(
        ("2009-08-18 00:00",
         "2006-09-13 00:00",
         "2006-09-12 00:00",
         "2004-07-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5EnMsTopInfo_ObjectIdentity = ObjectIdentity
s5EnMsTopInfo = _S5EnMsTopInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1)
)
_S5EnMsTopIpAddr_Type = IpAddress
_S5EnMsTopIpAddr_Object = MibScalar
s5EnMsTopIpAddr = _S5EnMsTopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 1),
    _S5EnMsTopIpAddr_Type()
)
s5EnMsTopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopIpAddr.setStatus("current")


class _S5EnMsTopStatus_Type(Integer32):
    """Custom type s5EnMsTopStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("topOff", 2),
          ("topOn", 1))
    )


_S5EnMsTopStatus_Type.__name__ = "Integer32"
_S5EnMsTopStatus_Object = MibScalar
s5EnMsTopStatus = _S5EnMsTopStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 2),
    _S5EnMsTopStatus_Type()
)
s5EnMsTopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnMsTopStatus.setStatus("current")
_S5EnMsTopNmmLstChg_Type = TimeTicks
_S5EnMsTopNmmLstChg_Object = MibScalar
s5EnMsTopNmmLstChg = _S5EnMsTopNmmLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 3),
    _S5EnMsTopNmmLstChg_Type()
)
s5EnMsTopNmmLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmLstChg.setStatus("current")
_S5EnMsTopBdgLstChg_Type = TimeTicks
_S5EnMsTopBdgLstChg_Object = MibScalar
s5EnMsTopBdgLstChg = _S5EnMsTopBdgLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 4),
    _S5EnMsTopBdgLstChg_Type()
)
s5EnMsTopBdgLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgLstChg.setStatus("deprecated")


class _S5EnMsTopNmmMaxNum_Type(Integer32):
    """Custom type s5EnMsTopNmmMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5EnMsTopNmmMaxNum_Type.__name__ = "Integer32"
_S5EnMsTopNmmMaxNum_Object = MibScalar
s5EnMsTopNmmMaxNum = _S5EnMsTopNmmMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 5),
    _S5EnMsTopNmmMaxNum_Type()
)
s5EnMsTopNmmMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmMaxNum.setStatus("current")


class _S5EnMsTopNmmCurNum_Type(Integer32):
    """Custom type s5EnMsTopNmmCurNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5EnMsTopNmmCurNum_Type.__name__ = "Integer32"
_S5EnMsTopNmmCurNum_Object = MibScalar
s5EnMsTopNmmCurNum = _S5EnMsTopNmmCurNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 6),
    _S5EnMsTopNmmCurNum_Type()
)
s5EnMsTopNmmCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmCurNum.setStatus("current")


class _S5EnMsTopBdgMaxNum_Type(Integer32):
    """Custom type s5EnMsTopBdgMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5EnMsTopBdgMaxNum_Type.__name__ = "Integer32"
_S5EnMsTopBdgMaxNum_Object = MibScalar
s5EnMsTopBdgMaxNum = _S5EnMsTopBdgMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 7),
    _S5EnMsTopBdgMaxNum_Type()
)
s5EnMsTopBdgMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgMaxNum.setStatus("deprecated")


class _S5EnMsTopBdgCurNum_Type(Integer32):
    """Custom type s5EnMsTopBdgCurNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5EnMsTopBdgCurNum_Type.__name__ = "Integer32"
_S5EnMsTopBdgCurNum_Object = MibScalar
s5EnMsTopBdgCurNum = _S5EnMsTopBdgCurNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 1, 8),
    _S5EnMsTopBdgCurNum_Type()
)
s5EnMsTopBdgCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgCurNum.setStatus("deprecated")
_S5EnMsTopNmm_ObjectIdentity = ObjectIdentity
s5EnMsTopNmm = _S5EnMsTopNmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2)
)
_S5EnMsTopNmmTable_Object = MibTable
s5EnMsTopNmmTable = _S5EnMsTopNmmTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1)
)
if mibBuilder.loadTexts:
    s5EnMsTopNmmTable.setStatus("current")
_S5EnMsTopNmmEntry_Object = MibTableRow
s5EnMsTopNmmEntry = _S5EnMsTopNmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1)
)
s5EnMsTopNmmEntry.setIndexNames(
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSlot"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmPort"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmIpAddr"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSegId"),
)
if mibBuilder.loadTexts:
    s5EnMsTopNmmEntry.setStatus("current")


class _S5EnMsTopNmmSlot_Type(Integer32):
    """Custom type s5EnMsTopNmmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5EnMsTopNmmSlot_Type.__name__ = "Integer32"
_S5EnMsTopNmmSlot_Object = MibTableColumn
s5EnMsTopNmmSlot = _S5EnMsTopNmmSlot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 1),
    _S5EnMsTopNmmSlot_Type()
)
s5EnMsTopNmmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmSlot.setStatus("current")


class _S5EnMsTopNmmPort_Type(Integer32):
    """Custom type s5EnMsTopNmmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5EnMsTopNmmPort_Type.__name__ = "Integer32"
_S5EnMsTopNmmPort_Object = MibTableColumn
s5EnMsTopNmmPort = _S5EnMsTopNmmPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 2),
    _S5EnMsTopNmmPort_Type()
)
s5EnMsTopNmmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmPort.setStatus("current")
_S5EnMsTopNmmIpAddr_Type = IpAddress
_S5EnMsTopNmmIpAddr_Object = MibTableColumn
s5EnMsTopNmmIpAddr = _S5EnMsTopNmmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 3),
    _S5EnMsTopNmmIpAddr_Type()
)
s5EnMsTopNmmIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmIpAddr.setStatus("current")


class _S5EnMsTopNmmSegId_Type(Integer32):
    """Custom type s5EnMsTopNmmSegId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_S5EnMsTopNmmSegId_Type.__name__ = "Integer32"
_S5EnMsTopNmmSegId_Object = MibTableColumn
s5EnMsTopNmmSegId = _S5EnMsTopNmmSegId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 4),
    _S5EnMsTopNmmSegId_Type()
)
s5EnMsTopNmmSegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmSegId.setStatus("current")
_S5EnMsTopNmmMacAddr_Type = MacAddress
_S5EnMsTopNmmMacAddr_Object = MibTableColumn
s5EnMsTopNmmMacAddr = _S5EnMsTopNmmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 5),
    _S5EnMsTopNmmMacAddr_Type()
)
s5EnMsTopNmmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmMacAddr.setStatus("current")
_S5EnMsTopNmmChassisType_Type = SnpxChassisType
_S5EnMsTopNmmChassisType_Object = MibTableColumn
s5EnMsTopNmmChassisType = _S5EnMsTopNmmChassisType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 6),
    _S5EnMsTopNmmChassisType_Type()
)
s5EnMsTopNmmChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmChassisType.setStatus("current")
_S5EnMsTopNmmBkplType_Type = SnpxBackplaneType
_S5EnMsTopNmmBkplType_Object = MibTableColumn
s5EnMsTopNmmBkplType = _S5EnMsTopNmmBkplType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 7),
    _S5EnMsTopNmmBkplType_Type()
)
s5EnMsTopNmmBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmBkplType.setStatus("current")


class _S5EnMsTopNmmLocalSeg_Type(Integer32):
    """Custom type s5EnMsTopNmmLocalSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_S5EnMsTopNmmLocalSeg_Type.__name__ = "Integer32"
_S5EnMsTopNmmLocalSeg_Object = MibTableColumn
s5EnMsTopNmmLocalSeg = _S5EnMsTopNmmLocalSeg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 8),
    _S5EnMsTopNmmLocalSeg_Type()
)
s5EnMsTopNmmLocalSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmLocalSeg.setStatus("current")


class _S5EnMsTopNmmCurState_Type(Integer32):
    """Custom type s5EnMsTopNmmCurState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("heartbeat", 2),
          ("new", 3),
          ("topChanged", 1))
    )


_S5EnMsTopNmmCurState_Type.__name__ = "Integer32"
_S5EnMsTopNmmCurState_Object = MibTableColumn
s5EnMsTopNmmCurState = _S5EnMsTopNmmCurState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 1, 1, 9),
    _S5EnMsTopNmmCurState_Type()
)
s5EnMsTopNmmCurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmCurState.setStatus("current")


class _S5EnMsTopNmmEosSize_Type(Integer32):
    """Custom type s5EnMsTopNmmEosSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_S5EnMsTopNmmEosSize_Type.__name__ = "Integer32"
_S5EnMsTopNmmEosSize_Object = MibScalar
s5EnMsTopNmmEosSize = _S5EnMsTopNmmEosSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 2),
    _S5EnMsTopNmmEosSize_Type()
)
s5EnMsTopNmmEosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmEosSize.setStatus("current")
_S5EnMsTopNmmEosTable_Object = MibTable
s5EnMsTopNmmEosTable = _S5EnMsTopNmmEosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 3)
)
if mibBuilder.loadTexts:
    s5EnMsTopNmmEosTable.setStatus("current")
_S5EnMsTopNmmEosEntry_Object = MibTableRow
s5EnMsTopNmmEosEntry = _S5EnMsTopNmmEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 3, 1)
)
s5EnMsTopNmmEosEntry.setIndexNames(
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSlot"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmPort"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmIpAddr"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopNmmSegId"),
)
if mibBuilder.loadTexts:
    s5EnMsTopNmmEosEntry.setStatus("current")


class _S5EnMsTopNmmEos_Type(OctetString):
    """Custom type s5EnMsTopNmmEos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S5EnMsTopNmmEos_Type.__name__ = "OctetString"
_S5EnMsTopNmmEos_Object = MibTableColumn
s5EnMsTopNmmEos = _S5EnMsTopNmmEos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 2, 3, 1, 1),
    _S5EnMsTopNmmEos_Type()
)
s5EnMsTopNmmEos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopNmmEos.setStatus("current")
_S5EnMsTopBdg_ObjectIdentity = ObjectIdentity
s5EnMsTopBdg = _S5EnMsTopBdg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3)
)
_S5EnMsTopBdgTable_Object = MibTable
s5EnMsTopBdgTable = _S5EnMsTopBdgTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1)
)
if mibBuilder.loadTexts:
    s5EnMsTopBdgTable.setStatus("deprecated")
_S5EnMsTopBdgEntry_Object = MibTableRow
s5EnMsTopBdgEntry = _S5EnMsTopBdgEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1)
)
s5EnMsTopBdgEntry.setIndexNames(
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgSlotNum"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgPortNum"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgIpAddr"),
)
if mibBuilder.loadTexts:
    s5EnMsTopBdgEntry.setStatus("deprecated")


class _S5EnMsTopBdgSlotNum_Type(Integer32):
    """Custom type s5EnMsTopBdgSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5EnMsTopBdgSlotNum_Type.__name__ = "Integer32"
_S5EnMsTopBdgSlotNum_Object = MibTableColumn
s5EnMsTopBdgSlotNum = _S5EnMsTopBdgSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 1),
    _S5EnMsTopBdgSlotNum_Type()
)
s5EnMsTopBdgSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgSlotNum.setStatus("deprecated")


class _S5EnMsTopBdgPortNum_Type(Integer32):
    """Custom type s5EnMsTopBdgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5EnMsTopBdgPortNum_Type.__name__ = "Integer32"
_S5EnMsTopBdgPortNum_Object = MibTableColumn
s5EnMsTopBdgPortNum = _S5EnMsTopBdgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 2),
    _S5EnMsTopBdgPortNum_Type()
)
s5EnMsTopBdgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgPortNum.setStatus("deprecated")
_S5EnMsTopBdgIpAddr_Type = IpAddress
_S5EnMsTopBdgIpAddr_Object = MibTableColumn
s5EnMsTopBdgIpAddr = _S5EnMsTopBdgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 3),
    _S5EnMsTopBdgIpAddr_Type()
)
s5EnMsTopBdgIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgIpAddr.setStatus("deprecated")


class _S5EnMsTopBdgNumber_Type(Integer32):
    """Custom type s5EnMsTopBdgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5EnMsTopBdgNumber_Type.__name__ = "Integer32"
_S5EnMsTopBdgNumber_Object = MibTableColumn
s5EnMsTopBdgNumber = _S5EnMsTopBdgNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 4),
    _S5EnMsTopBdgNumber_Type()
)
s5EnMsTopBdgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgNumber.setStatus("deprecated")
_S5EnMsTopBdgMacAddr_Type = MacAddress
_S5EnMsTopBdgMacAddr_Object = MibTableColumn
s5EnMsTopBdgMacAddr = _S5EnMsTopBdgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 5),
    _S5EnMsTopBdgMacAddr_Type()
)
s5EnMsTopBdgMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgMacAddr.setStatus("deprecated")


class _S5EnMsTopBdgType_Type(Integer32):
    """Custom type s5EnMsTopBdgType based on Integer32"""
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
        *(("kalpana", 4),
          ("localSyn", 2),
          ("other", 1),
          ("remoteSyn", 3))
    )


_S5EnMsTopBdgType_Type.__name__ = "Integer32"
_S5EnMsTopBdgType_Object = MibTableColumn
s5EnMsTopBdgType = _S5EnMsTopBdgType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 6),
    _S5EnMsTopBdgType_Type()
)
s5EnMsTopBdgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgType.setStatus("deprecated")
_S5EnMsTopBdgNumPorts_Type = Integer32
_S5EnMsTopBdgNumPorts_Object = MibTableColumn
s5EnMsTopBdgNumPorts = _S5EnMsTopBdgNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 7),
    _S5EnMsTopBdgNumPorts_Type()
)
s5EnMsTopBdgNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgNumPorts.setStatus("deprecated")


class _S5EnMsTopBdgStatus_Type(Integer32):
    """Custom type s5EnMsTopBdgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1),
          ("standby", 3))
    )


_S5EnMsTopBdgStatus_Type.__name__ = "Integer32"
_S5EnMsTopBdgStatus_Object = MibTableColumn
s5EnMsTopBdgStatus = _S5EnMsTopBdgStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 8),
    _S5EnMsTopBdgStatus_Type()
)
s5EnMsTopBdgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgStatus.setStatus("deprecated")


class _S5EnMsTopBdgHelloPortNum_Type(Integer32):
    """Custom type s5EnMsTopBdgHelloPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5EnMsTopBdgHelloPortNum_Type.__name__ = "Integer32"
_S5EnMsTopBdgHelloPortNum_Object = MibTableColumn
s5EnMsTopBdgHelloPortNum = _S5EnMsTopBdgHelloPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 9),
    _S5EnMsTopBdgHelloPortNum_Type()
)
s5EnMsTopBdgHelloPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgHelloPortNum.setStatus("deprecated")


class _S5EnMsTopBdgHelloPortType_Type(Integer32):
    """Custom type s5EnMsTopBdgHelloPortType based on Integer32"""
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
        *(("eth", 2),
          ("fddi", 5),
          ("other", 1),
          ("t1", 6),
          ("tok16", 4),
          ("tok4", 3))
    )


_S5EnMsTopBdgHelloPortType_Type.__name__ = "Integer32"
_S5EnMsTopBdgHelloPortType_Object = MibTableColumn
s5EnMsTopBdgHelloPortType = _S5EnMsTopBdgHelloPortType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 10),
    _S5EnMsTopBdgHelloPortType_Type()
)
s5EnMsTopBdgHelloPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgHelloPortType.setStatus("deprecated")


class _S5EnMsTopBdgHelloPortStatus_Type(Integer32):
    """Custom type s5EnMsTopBdgHelloPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1),
          ("standby", 3))
    )


_S5EnMsTopBdgHelloPortStatus_Type.__name__ = "Integer32"
_S5EnMsTopBdgHelloPortStatus_Object = MibTableColumn
s5EnMsTopBdgHelloPortStatus = _S5EnMsTopBdgHelloPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 11),
    _S5EnMsTopBdgHelloPortStatus_Type()
)
s5EnMsTopBdgHelloPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgHelloPortStatus.setStatus("deprecated")
_S5EnMsTopBdgCompBdgMac1_Type = MacAddress
_S5EnMsTopBdgCompBdgMac1_Object = MibTableColumn
s5EnMsTopBdgCompBdgMac1 = _S5EnMsTopBdgCompBdgMac1_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 12),
    _S5EnMsTopBdgCompBdgMac1_Type()
)
s5EnMsTopBdgCompBdgMac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgCompBdgMac1.setStatus("deprecated")
_S5EnMsTopBdgCompBdgMac2_Type = MacAddress
_S5EnMsTopBdgCompBdgMac2_Object = MibTableColumn
s5EnMsTopBdgCompBdgMac2 = _S5EnMsTopBdgCompBdgMac2_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 1, 1, 13),
    _S5EnMsTopBdgCompBdgMac2_Type()
)
s5EnMsTopBdgCompBdgMac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgCompBdgMac2.setStatus("deprecated")


class _S5EnMsTopBdgEosSize_Type(Integer32):
    """Custom type s5EnMsTopBdgEosSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_S5EnMsTopBdgEosSize_Type.__name__ = "Integer32"
_S5EnMsTopBdgEosSize_Object = MibScalar
s5EnMsTopBdgEosSize = _S5EnMsTopBdgEosSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 2),
    _S5EnMsTopBdgEosSize_Type()
)
s5EnMsTopBdgEosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgEosSize.setStatus("deprecated")
_S5EnMsTopBdgEosTable_Object = MibTable
s5EnMsTopBdgEosTable = _S5EnMsTopBdgEosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 3)
)
if mibBuilder.loadTexts:
    s5EnMsTopBdgEosTable.setStatus("deprecated")
_S5EnMsTopBdgEosEntry_Object = MibTableRow
s5EnMsTopBdgEosEntry = _S5EnMsTopBdgEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 3, 1)
)
s5EnMsTopBdgEosEntry.setIndexNames(
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgSlotNum"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgPortNum"),
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopBdgIpAddr"),
)
if mibBuilder.loadTexts:
    s5EnMsTopBdgEosEntry.setStatus("deprecated")


class _S5EnMsTopBdgEos_Type(OctetString):
    """Custom type s5EnMsTopBdgEos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S5EnMsTopBdgEos_Type.__name__ = "OctetString"
_S5EnMsTopBdgEos_Object = MibTableColumn
s5EnMsTopBdgEos = _S5EnMsTopBdgEos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 3, 3, 1, 1),
    _S5EnMsTopBdgEos_Type()
)
s5EnMsTopBdgEos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopBdgEos.setStatus("deprecated")
_S5EnMsTopSrcMac_ObjectIdentity = ObjectIdentity
s5EnMsTopSrcMac = _S5EnMsTopSrcMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4)
)
_S5EnMsTopSrcMacAddrTable_Object = MibTable
s5EnMsTopSrcMacAddrTable = _S5EnMsTopSrcMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1)
)
if mibBuilder.loadTexts:
    s5EnMsTopSrcMacAddrTable.setStatus("deprecated")
_S5EnMsTopSrcMacAddrEntry_Object = MibTableRow
s5EnMsTopSrcMacAddrEntry = _S5EnMsTopSrcMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1, 1)
)
s5EnMsTopSrcMacAddrEntry.setIndexNames(
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopSrcMacAddr"),
)
if mibBuilder.loadTexts:
    s5EnMsTopSrcMacAddrEntry.setStatus("deprecated")
_S5EnMsTopSrcMacAddr_Type = MacAddress
_S5EnMsTopSrcMacAddr_Object = MibTableColumn
s5EnMsTopSrcMacAddr = _S5EnMsTopSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1, 1, 1),
    _S5EnMsTopSrcMacAddr_Type()
)
s5EnMsTopSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopSrcMacAddr.setStatus("deprecated")


class _S5EnMsTopSrcMacSegId_Type(Integer32):
    """Custom type s5EnMsTopSrcMacSegId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_S5EnMsTopSrcMacSegId_Type.__name__ = "Integer32"
_S5EnMsTopSrcMacSegId_Object = MibTableColumn
s5EnMsTopSrcMacSegId = _S5EnMsTopSrcMacSegId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 1, 1, 2),
    _S5EnMsTopSrcMacSegId_Type()
)
s5EnMsTopSrcMacSegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopSrcMacSegId.setStatus("deprecated")
_S5EnMsTopSrcMacAddrLstChg_Type = TimeTicks
_S5EnMsTopSrcMacAddrLstChg_Object = MibScalar
s5EnMsTopSrcMacAddrLstChg = _S5EnMsTopSrcMacAddrLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 4, 2),
    _S5EnMsTopSrcMacAddrLstChg_Type()
)
s5EnMsTopSrcMacAddrLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnMsTopSrcMacAddrLstChg.setStatus("deprecated")
_S5EnMsTopPort_ObjectIdentity = ObjectIdentity
s5EnMsTopPort = _S5EnMsTopPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5)
)
_S5EnMsTopPortTable_Object = MibTable
s5EnMsTopPortTable = _S5EnMsTopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1)
)
if mibBuilder.loadTexts:
    s5EnMsTopPortTable.setStatus("current")
_S5EnMsTopPortEntry_Object = MibTableRow
s5EnMsTopPortEntry = _S5EnMsTopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1, 1)
)
s5EnMsTopPortEntry.setIndexNames(
    (0, "S5-ETH-MULTISEG-TOPOLOGY-MIB", "s5EnMsTopPortIfIndex"),
)
if mibBuilder.loadTexts:
    s5EnMsTopPortEntry.setStatus("current")
_S5EnMsTopPortIfIndex_Type = InterfaceIndex
_S5EnMsTopPortIfIndex_Object = MibTableColumn
s5EnMsTopPortIfIndex = _S5EnMsTopPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1, 1, 1),
    _S5EnMsTopPortIfIndex_Type()
)
s5EnMsTopPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5EnMsTopPortIfIndex.setStatus("current")


class _S5EnMsTopPortState_Type(Integer32):
    """Custom type s5EnMsTopPortState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("topActive", 1),
          ("topPassthru", 2))
    )


_S5EnMsTopPortState_Type.__name__ = "Integer32"
_S5EnMsTopPortState_Object = MibTableColumn
s5EnMsTopPortState = _S5EnMsTopPortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 13, 5, 1, 1, 2),
    _S5EnMsTopPortState_Type()
)
s5EnMsTopPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnMsTopPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-ETH-MULTISEG-TOPOLOGY-MIB",
    **{"s5EthMultisegTopologyMib": s5EthMultisegTopologyMib,
       "s5EnMsTopInfo": s5EnMsTopInfo,
       "s5EnMsTopIpAddr": s5EnMsTopIpAddr,
       "s5EnMsTopStatus": s5EnMsTopStatus,
       "s5EnMsTopNmmLstChg": s5EnMsTopNmmLstChg,
       "s5EnMsTopBdgLstChg": s5EnMsTopBdgLstChg,
       "s5EnMsTopNmmMaxNum": s5EnMsTopNmmMaxNum,
       "s5EnMsTopNmmCurNum": s5EnMsTopNmmCurNum,
       "s5EnMsTopBdgMaxNum": s5EnMsTopBdgMaxNum,
       "s5EnMsTopBdgCurNum": s5EnMsTopBdgCurNum,
       "s5EnMsTopNmm": s5EnMsTopNmm,
       "s5EnMsTopNmmTable": s5EnMsTopNmmTable,
       "s5EnMsTopNmmEntry": s5EnMsTopNmmEntry,
       "s5EnMsTopNmmSlot": s5EnMsTopNmmSlot,
       "s5EnMsTopNmmPort": s5EnMsTopNmmPort,
       "s5EnMsTopNmmIpAddr": s5EnMsTopNmmIpAddr,
       "s5EnMsTopNmmSegId": s5EnMsTopNmmSegId,
       "s5EnMsTopNmmMacAddr": s5EnMsTopNmmMacAddr,
       "s5EnMsTopNmmChassisType": s5EnMsTopNmmChassisType,
       "s5EnMsTopNmmBkplType": s5EnMsTopNmmBkplType,
       "s5EnMsTopNmmLocalSeg": s5EnMsTopNmmLocalSeg,
       "s5EnMsTopNmmCurState": s5EnMsTopNmmCurState,
       "s5EnMsTopNmmEosSize": s5EnMsTopNmmEosSize,
       "s5EnMsTopNmmEosTable": s5EnMsTopNmmEosTable,
       "s5EnMsTopNmmEosEntry": s5EnMsTopNmmEosEntry,
       "s5EnMsTopNmmEos": s5EnMsTopNmmEos,
       "s5EnMsTopBdg": s5EnMsTopBdg,
       "s5EnMsTopBdgTable": s5EnMsTopBdgTable,
       "s5EnMsTopBdgEntry": s5EnMsTopBdgEntry,
       "s5EnMsTopBdgSlotNum": s5EnMsTopBdgSlotNum,
       "s5EnMsTopBdgPortNum": s5EnMsTopBdgPortNum,
       "s5EnMsTopBdgIpAddr": s5EnMsTopBdgIpAddr,
       "s5EnMsTopBdgNumber": s5EnMsTopBdgNumber,
       "s5EnMsTopBdgMacAddr": s5EnMsTopBdgMacAddr,
       "s5EnMsTopBdgType": s5EnMsTopBdgType,
       "s5EnMsTopBdgNumPorts": s5EnMsTopBdgNumPorts,
       "s5EnMsTopBdgStatus": s5EnMsTopBdgStatus,
       "s5EnMsTopBdgHelloPortNum": s5EnMsTopBdgHelloPortNum,
       "s5EnMsTopBdgHelloPortType": s5EnMsTopBdgHelloPortType,
       "s5EnMsTopBdgHelloPortStatus": s5EnMsTopBdgHelloPortStatus,
       "s5EnMsTopBdgCompBdgMac1": s5EnMsTopBdgCompBdgMac1,
       "s5EnMsTopBdgCompBdgMac2": s5EnMsTopBdgCompBdgMac2,
       "s5EnMsTopBdgEosSize": s5EnMsTopBdgEosSize,
       "s5EnMsTopBdgEosTable": s5EnMsTopBdgEosTable,
       "s5EnMsTopBdgEosEntry": s5EnMsTopBdgEosEntry,
       "s5EnMsTopBdgEos": s5EnMsTopBdgEos,
       "s5EnMsTopSrcMac": s5EnMsTopSrcMac,
       "s5EnMsTopSrcMacAddrTable": s5EnMsTopSrcMacAddrTable,
       "s5EnMsTopSrcMacAddrEntry": s5EnMsTopSrcMacAddrEntry,
       "s5EnMsTopSrcMacAddr": s5EnMsTopSrcMacAddr,
       "s5EnMsTopSrcMacSegId": s5EnMsTopSrcMacSegId,
       "s5EnMsTopSrcMacAddrLstChg": s5EnMsTopSrcMacAddrLstChg,
       "s5EnMsTopPort": s5EnMsTopPort,
       "s5EnMsTopPortTable": s5EnMsTopPortTable,
       "s5EnMsTopPortEntry": s5EnMsTopPortEntry,
       "s5EnMsTopPortIfIndex": s5EnMsTopPortIfIndex,
       "s5EnMsTopPortState": s5EnMsTopPortState}
)
