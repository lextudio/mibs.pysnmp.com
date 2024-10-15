# SNMP MIB module (CISCO-MGX82XX-VIRTUAL-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-VIRTUAL-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:38 2024
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

(virtualInterface,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "virtualInterface")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoMgx82xxVirtualPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 38)
)
ciscoMgx82xxVirtualPortMIB.setRevisions(
        ("2002-08-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VirtualInterfaceCnf_ObjectIdentity = ObjectIdentity
virtualInterfaceCnf = _VirtualInterfaceCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1)
)
_VrtlIntrConfigTable_Object = MibTable
vrtlIntrConfigTable = _VrtlIntrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    vrtlIntrConfigTable.setStatus("current")
_VrtlIntrConfigEntry_Object = MibTableRow
vrtlIntrConfigEntry = _VrtlIntrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1)
)
vrtlIntrConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "configVrtlIntrNum"),
)
if mibBuilder.loadTexts:
    vrtlIntrConfigEntry.setStatus("current")


class _ConfigVrtlIntrNum_Type(Integer32):
    """Custom type configVrtlIntrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ConfigVrtlIntrNum_Type.__name__ = "Integer32"
_ConfigVrtlIntrNum_Object = MibTableColumn
configVrtlIntrNum = _ConfigVrtlIntrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 1),
    _ConfigVrtlIntrNum_Type()
)
configVrtlIntrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVrtlIntrNum.setStatus("current")


class _VrtlIntrPortNum_Type(Integer32):
    """Custom type vrtlIntrPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VrtlIntrPortNum_Type.__name__ = "Integer32"
_VrtlIntrPortNum_Object = MibTableColumn
vrtlIntrPortNum = _VrtlIntrPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 2),
    _VrtlIntrPortNum_Type()
)
vrtlIntrPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrPortNum.setStatus("current")


class _VrtlIntrState_Type(Integer32):
    """Custom type vrtlIntrState based on Integer32"""
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


_VrtlIntrState_Type.__name__ = "Integer32"
_VrtlIntrState_Object = MibTableColumn
vrtlIntrState = _VrtlIntrState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 3),
    _VrtlIntrState_Type()
)
vrtlIntrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrState.setStatus("current")


class _VrtlIntrMaxQueMem_Type(Integer32):
    """Custom type vrtlIntrMaxQueMem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VrtlIntrMaxQueMem_Type.__name__ = "Integer32"
_VrtlIntrMaxQueMem_Object = MibTableColumn
vrtlIntrMaxQueMem = _VrtlIntrMaxQueMem_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 4),
    _VrtlIntrMaxQueMem_Type()
)
vrtlIntrMaxQueMem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrMaxQueMem.setStatus("current")


class _VrtlIntrMinCellRate_Type(Integer32):
    """Custom type vrtlIntrMinCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(103384, 353208),
    )


_VrtlIntrMinCellRate_Type.__name__ = "Integer32"
_VrtlIntrMinCellRate_Object = MibTableColumn
vrtlIntrMinCellRate = _VrtlIntrMinCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 5),
    _VrtlIntrMinCellRate_Type()
)
vrtlIntrMinCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrMinCellRate.setStatus("current")


class _VrtlIntrMaxCellRate_Type(Integer32):
    """Custom type vrtlIntrMaxCellRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(103384, 353208),
    )


_VrtlIntrMaxCellRate_Type.__name__ = "Integer32"
_VrtlIntrMaxCellRate_Object = MibTableColumn
vrtlIntrMaxCellRate = _VrtlIntrMaxCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 6),
    _VrtlIntrMaxCellRate_Type()
)
vrtlIntrMaxCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrMaxCellRate.setStatus("current")
_VrtlIntrCurrConfigPaths_Type = Integer32
_VrtlIntrCurrConfigPaths_Object = MibTableColumn
vrtlIntrCurrConfigPaths = _VrtlIntrCurrConfigPaths_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 1, 1, 1, 7),
    _VrtlIntrCurrConfigPaths_Type()
)
vrtlIntrCurrConfigPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrCurrConfigPaths.setStatus("current")
_VirtualInterfaceCnt_ObjectIdentity = ObjectIdentity
virtualInterfaceCnt = _VirtualInterfaceCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2)
)
_VrtlIntrCounterTable_Object = MibTable
vrtlIntrCounterTable = _VrtlIntrCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vrtlIntrCounterTable.setStatus("current")
_VrtlIntrCounterEntry_Object = MibTableRow
vrtlIntrCounterEntry = _VrtlIntrCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1)
)
vrtlIntrCounterEntry.setIndexNames(
    (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "countVrtlIntrNum"),
)
if mibBuilder.loadTexts:
    vrtlIntrCounterEntry.setStatus("current")


class _CountVrtlIntrNum_Type(Integer32):
    """Custom type countVrtlIntrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CountVrtlIntrNum_Type.__name__ = "Integer32"
_CountVrtlIntrNum_Object = MibTableColumn
countVrtlIntrNum = _CountVrtlIntrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 1),
    _CountVrtlIntrNum_Type()
)
countVrtlIntrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countVrtlIntrNum.setStatus("current")
_VrtlIntrTotalCellCnt_Type = Counter32
_VrtlIntrTotalCellCnt_Object = MibTableColumn
vrtlIntrTotalCellCnt = _VrtlIntrTotalCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 2),
    _VrtlIntrTotalCellCnt_Type()
)
vrtlIntrTotalCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrTotalCellCnt.setStatus("current")
_VrtlIntrTotalQbinCellCnt_Type = Counter32
_VrtlIntrTotalQbinCellCnt_Object = MibTableColumn
vrtlIntrTotalQbinCellCnt = _VrtlIntrTotalQbinCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 3),
    _VrtlIntrTotalQbinCellCnt_Type()
)
vrtlIntrTotalQbinCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrTotalQbinCellCnt.setStatus("current")
_VrtlIntrRxdValidOAMCellCnt_Type = Counter32
_VrtlIntrRxdValidOAMCellCnt_Object = MibTableColumn
vrtlIntrRxdValidOAMCellCnt = _VrtlIntrRxdValidOAMCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 4),
    _VrtlIntrRxdValidOAMCellCnt_Type()
)
vrtlIntrRxdValidOAMCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrRxdValidOAMCellCnt.setStatus("current")
_VrtlIntrRxdRmCellCnt_Type = Counter32
_VrtlIntrRxdRmCellCnt_Object = MibTableColumn
vrtlIntrRxdRmCellCnt = _VrtlIntrRxdRmCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 5),
    _VrtlIntrRxdRmCellCnt_Type()
)
vrtlIntrRxdRmCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrRxdRmCellCnt.setStatus("current")
_VrtlIntrRxdClpUntaggedCellCnt_Type = Counter32
_VrtlIntrRxdClpUntaggedCellCnt_Object = MibTableColumn
vrtlIntrRxdClpUntaggedCellCnt = _VrtlIntrRxdClpUntaggedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 6),
    _VrtlIntrRxdClpUntaggedCellCnt_Type()
)
vrtlIntrRxdClpUntaggedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrRxdClpUntaggedCellCnt.setStatus("current")
_VrtlIntrRxdClpTaggedCellCnt_Type = Counter32
_VrtlIntrRxdClpTaggedCellCnt_Object = MibTableColumn
vrtlIntrRxdClpTaggedCellCnt = _VrtlIntrRxdClpTaggedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 7),
    _VrtlIntrRxdClpTaggedCellCnt_Type()
)
vrtlIntrRxdClpTaggedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrRxdClpTaggedCellCnt.setStatus("current")
_VrtlIntrRxdClpUntaggedDiscardedCellCnt_Type = Counter32
_VrtlIntrRxdClpUntaggedDiscardedCellCnt_Object = MibTableColumn
vrtlIntrRxdClpUntaggedDiscardedCellCnt = _VrtlIntrRxdClpUntaggedDiscardedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 8),
    _VrtlIntrRxdClpUntaggedDiscardedCellCnt_Type()
)
vrtlIntrRxdClpUntaggedDiscardedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrRxdClpUntaggedDiscardedCellCnt.setStatus("current")
_VrtlIntrRxdClpTaggedDiscardedCellCnt_Type = Counter32
_VrtlIntrRxdClpTaggedDiscardedCellCnt_Object = MibTableColumn
vrtlIntrRxdClpTaggedDiscardedCellCnt = _VrtlIntrRxdClpTaggedDiscardedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 9),
    _VrtlIntrRxdClpTaggedDiscardedCellCnt_Type()
)
vrtlIntrRxdClpTaggedDiscardedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrRxdClpTaggedDiscardedCellCnt.setStatus("current")
_VrtlIntrXmtdOAMCellCnt_Type = Counter32
_VrtlIntrXmtdOAMCellCnt_Object = MibTableColumn
vrtlIntrXmtdOAMCellCnt = _VrtlIntrXmtdOAMCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 10),
    _VrtlIntrXmtdOAMCellCnt_Type()
)
vrtlIntrXmtdOAMCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrXmtdOAMCellCnt.setStatus("current")
_VrtlIntrXmtdRmCellCnt_Type = Counter32
_VrtlIntrXmtdRmCellCnt_Object = MibTableColumn
vrtlIntrXmtdRmCellCnt = _VrtlIntrXmtdRmCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 11),
    _VrtlIntrXmtdRmCellCnt_Type()
)
vrtlIntrXmtdRmCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrXmtdRmCellCnt.setStatus("current")
_VrtlIntrXmtdClpUntaggedCellCnt_Type = Counter32
_VrtlIntrXmtdClpUntaggedCellCnt_Object = MibTableColumn
vrtlIntrXmtdClpUntaggedCellCnt = _VrtlIntrXmtdClpUntaggedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 12),
    _VrtlIntrXmtdClpUntaggedCellCnt_Type()
)
vrtlIntrXmtdClpUntaggedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrXmtdClpUntaggedCellCnt.setStatus("current")
_VrtlIntrXmtdClpTaggedCellCnt_Type = Counter32
_VrtlIntrXmtdClpTaggedCellCnt_Object = MibTableColumn
vrtlIntrXmtdClpTaggedCellCnt = _VrtlIntrXmtdClpTaggedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 2, 1, 1, 13),
    _VrtlIntrXmtdClpTaggedCellCnt_Type()
)
vrtlIntrXmtdClpTaggedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrXmtdClpTaggedCellCnt.setStatus("current")
_VirtualInterfaceQbinCnf_ObjectIdentity = ObjectIdentity
virtualInterfaceQbinCnf = _VirtualInterfaceQbinCnf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3)
)
_VrtlIntrQbinConfigTable_Object = MibTable
vrtlIntrQbinConfigTable = _VrtlIntrQbinConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    vrtlIntrQbinConfigTable.setStatus("current")
_VrtlIntrQbinConfigEntry_Object = MibTableRow
vrtlIntrQbinConfigEntry = _VrtlIntrQbinConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1)
)
vrtlIntrQbinConfigEntry.setIndexNames(
    (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrNum"),
    (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrQbinNum"),
)
if mibBuilder.loadTexts:
    vrtlIntrQbinConfigEntry.setStatus("current")


class _QueConfigVrtlIntrNum_Type(Integer32):
    """Custom type queConfigVrtlIntrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QueConfigVrtlIntrNum_Type.__name__ = "Integer32"
_QueConfigVrtlIntrNum_Object = MibTableColumn
queConfigVrtlIntrNum = _QueConfigVrtlIntrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 1),
    _QueConfigVrtlIntrNum_Type()
)
queConfigVrtlIntrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queConfigVrtlIntrNum.setStatus("current")


class _QueConfigVrtlIntrQbinNum_Type(Integer32):
    """Custom type queConfigVrtlIntrQbinNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QueConfigVrtlIntrQbinNum_Type.__name__ = "Integer32"
_QueConfigVrtlIntrQbinNum_Object = MibTableColumn
queConfigVrtlIntrQbinNum = _QueConfigVrtlIntrQbinNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 2),
    _QueConfigVrtlIntrQbinNum_Type()
)
queConfigVrtlIntrQbinNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queConfigVrtlIntrQbinNum.setStatus("current")


class _VrtlIntrQbinState_Type(Integer32):
    """Custom type vrtlIntrQbinState based on Integer32"""
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


_VrtlIntrQbinState_Type.__name__ = "Integer32"
_VrtlIntrQbinState_Object = MibTableColumn
vrtlIntrQbinState = _VrtlIntrQbinState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 3),
    _VrtlIntrQbinState_Type()
)
vrtlIntrQbinState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinState.setStatus("current")


class _VrtlIntrQbinPri_Type(Integer32):
    """Custom type vrtlIntrQbinPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VrtlIntrQbinPri_Type.__name__ = "Integer32"
_VrtlIntrQbinPri_Object = MibTableColumn
vrtlIntrQbinPri = _VrtlIntrQbinPri_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 4),
    _VrtlIntrQbinPri_Type()
)
vrtlIntrQbinPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinPri.setStatus("current")


class _VrtlIntrQbinRate_Type(Integer32):
    """Custom type vrtlIntrQbinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_VrtlIntrQbinRate_Type.__name__ = "Integer32"
_VrtlIntrQbinRate_Object = MibTableColumn
vrtlIntrQbinRate = _VrtlIntrQbinRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 5),
    _VrtlIntrQbinRate_Type()
)
vrtlIntrQbinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinRate.setStatus("current")


class _VrtlIntrQbinDiscardSelection_Type(Integer32):
    """Custom type vrtlIntrQbinDiscardSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clpHysteresis", 1),
          ("frameDiscard", 3))
    )


_VrtlIntrQbinDiscardSelection_Type.__name__ = "Integer32"
_VrtlIntrQbinDiscardSelection_Object = MibTableColumn
vrtlIntrQbinDiscardSelection = _VrtlIntrQbinDiscardSelection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 6),
    _VrtlIntrQbinDiscardSelection_Type()
)
vrtlIntrQbinDiscardSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinDiscardSelection.setStatus("current")


class _VrtlIntrQbinMaxThreshold_Type(Integer32):
    """Custom type vrtlIntrQbinMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_VrtlIntrQbinMaxThreshold_Type.__name__ = "Integer32"
_VrtlIntrQbinMaxThreshold_Object = MibTableColumn
vrtlIntrQbinMaxThreshold = _VrtlIntrQbinMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 7),
    _VrtlIntrQbinMaxThreshold_Type()
)
vrtlIntrQbinMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinMaxThreshold.setStatus("current")


class _VrtlIntrQbinClpHiThreshold_Type(Integer32):
    """Custom type vrtlIntrQbinClpHiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_VrtlIntrQbinClpHiThreshold_Type.__name__ = "Integer32"
_VrtlIntrQbinClpHiThreshold_Object = MibTableColumn
vrtlIntrQbinClpHiThreshold = _VrtlIntrQbinClpHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 8),
    _VrtlIntrQbinClpHiThreshold_Type()
)
vrtlIntrQbinClpHiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinClpHiThreshold.setStatus("current")


class _VrtlIntrQbinClpLoThreshold_Type(Integer32):
    """Custom type vrtlIntrQbinClpLoThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_VrtlIntrQbinClpLoThreshold_Type.__name__ = "Integer32"
_VrtlIntrQbinClpLoThreshold_Object = MibTableColumn
vrtlIntrQbinClpLoThreshold = _VrtlIntrQbinClpLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 9),
    _VrtlIntrQbinClpLoThreshold_Type()
)
vrtlIntrQbinClpLoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinClpLoThreshold.setStatus("current")


class _VrtlIntrQbinFrameDiscardThreshold_Type(Integer32):
    """Custom type vrtlIntrQbinFrameDiscardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_VrtlIntrQbinFrameDiscardThreshold_Type.__name__ = "Integer32"
_VrtlIntrQbinFrameDiscardThreshold_Object = MibTableColumn
vrtlIntrQbinFrameDiscardThreshold = _VrtlIntrQbinFrameDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 10),
    _VrtlIntrQbinFrameDiscardThreshold_Type()
)
vrtlIntrQbinFrameDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinFrameDiscardThreshold.setStatus("current")


class _VrtlIntrQbinEfciThreshold_Type(Integer32):
    """Custom type vrtlIntrQbinEfciThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_VrtlIntrQbinEfciThreshold_Type.__name__ = "Integer32"
_VrtlIntrQbinEfciThreshold_Object = MibTableColumn
vrtlIntrQbinEfciThreshold = _VrtlIntrQbinEfciThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 3, 1, 1, 11),
    _VrtlIntrQbinEfciThreshold_Type()
)
vrtlIntrQbinEfciThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrtlIntrQbinEfciThreshold.setStatus("current")
_VirtualInterfaceQbinCnt_ObjectIdentity = ObjectIdentity
virtualInterfaceQbinCnt = _VirtualInterfaceQbinCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4)
)
_VrtlIntrQbinCounterTable_Object = MibTable
vrtlIntrQbinCounterTable = _VrtlIntrQbinCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    vrtlIntrQbinCounterTable.setStatus("current")
_VrtlIntrQbinCounterEntry_Object = MibTableRow
vrtlIntrQbinCounterEntry = _VrtlIntrQbinCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1)
)
vrtlIntrQbinCounterEntry.setIndexNames(
    (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConuterVrtlIntrNum"),
    (0, "CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queCounterVrtlIntrQbinNum"),
)
if mibBuilder.loadTexts:
    vrtlIntrQbinCounterEntry.setStatus("current")


class _QueConuterVrtlIntrNum_Type(Integer32):
    """Custom type queConuterVrtlIntrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QueConuterVrtlIntrNum_Type.__name__ = "Integer32"
_QueConuterVrtlIntrNum_Object = MibTableColumn
queConuterVrtlIntrNum = _QueConuterVrtlIntrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 1),
    _QueConuterVrtlIntrNum_Type()
)
queConuterVrtlIntrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queConuterVrtlIntrNum.setStatus("current")


class _QueCounterVrtlIntrQbinNum_Type(Integer32):
    """Custom type queCounterVrtlIntrQbinNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QueCounterVrtlIntrQbinNum_Type.__name__ = "Integer32"
_QueCounterVrtlIntrQbinNum_Object = MibTableColumn
queCounterVrtlIntrQbinNum = _QueCounterVrtlIntrQbinNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 2),
    _QueCounterVrtlIntrQbinNum_Type()
)
queCounterVrtlIntrQbinNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queCounterVrtlIntrQbinNum.setStatus("current")
_VrtlIntrQbinCurrentCellCnt_Type = Counter32
_VrtlIntrQbinCurrentCellCnt_Object = MibTableColumn
vrtlIntrQbinCurrentCellCnt = _VrtlIntrQbinCurrentCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 3),
    _VrtlIntrQbinCurrentCellCnt_Type()
)
vrtlIntrQbinCurrentCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrQbinCurrentCellCnt.setStatus("current")
_VrtlIntrQbinRxdCellCnt_Type = Counter32
_VrtlIntrQbinRxdCellCnt_Object = MibTableColumn
vrtlIntrQbinRxdCellCnt = _VrtlIntrQbinRxdCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 4),
    _VrtlIntrQbinRxdCellCnt_Type()
)
vrtlIntrQbinRxdCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrQbinRxdCellCnt.setStatus("current")
_VrtlIntrQbinTxdCellCnt_Type = Counter32
_VrtlIntrQbinTxdCellCnt_Object = MibTableColumn
vrtlIntrQbinTxdCellCnt = _VrtlIntrQbinTxdCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 5),
    _VrtlIntrQbinTxdCellCnt_Type()
)
vrtlIntrQbinTxdCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrQbinTxdCellCnt.setStatus("current")
_VrtlIntrQbinDiscardedCellCnt_Type = Counter32
_VrtlIntrQbinDiscardedCellCnt_Object = MibTableColumn
vrtlIntrQbinDiscardedCellCnt = _VrtlIntrQbinDiscardedCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8, 4, 1, 1, 6),
    _VrtlIntrQbinDiscardedCellCnt_Type()
)
vrtlIntrQbinDiscardedCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrtlIntrQbinDiscardedCellCnt.setStatus("current")
_CmvPortMIBConformance_ObjectIdentity = ObjectIdentity
cmvPortMIBConformance = _CmvPortMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2)
)
_CmvPortMIBGroups_ObjectIdentity = ObjectIdentity
cmvPortMIBGroups = _CmvPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1)
)
_CmvPortMIBCompliances_ObjectIdentity = ObjectIdentity
cmvPortMIBCompliances = _CmvPortMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 2)
)

# Managed Objects groups

cmvPortConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 1)
)
cmvPortConfGroup.setObjects(
      *(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "configVrtlIntrNum"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrPortNum"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrState"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMaxQueMem"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMinCellRate"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrMaxCellRate"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrCurrConfigPaths"))
)
if mibBuilder.loadTexts:
    cmvPortConfGroup.setStatus("current")

cmvPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 2)
)
cmvPortStatsGroup.setObjects(
      *(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "countVrtlIntrNum"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrTotalCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrTotalQbinCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdValidOAMCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdRmCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpUntaggedCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpTaggedCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpUntaggedDiscardedCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrRxdClpTaggedDiscardedCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdOAMCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdRmCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdClpUntaggedCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrXmtdClpTaggedCellCnt"))
)
if mibBuilder.loadTexts:
    cmvPortStatsGroup.setStatus("current")

cmvPortQbinConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 3)
)
cmvPortQbinConfGroup.setObjects(
      *(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrNum"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConfigVrtlIntrQbinNum"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinState"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinPri"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinRate"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinDiscardSelection"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinMaxThreshold"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinClpHiThreshold"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinClpLoThreshold"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinFrameDiscardThreshold"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinEfciThreshold"))
)
if mibBuilder.loadTexts:
    cmvPortQbinConfGroup.setStatus("current")

cmvPortQbinStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 1, 4)
)
cmvPortQbinStatsGroup.setObjects(
      *(("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queConuterVrtlIntrNum"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "queCounterVrtlIntrQbinNum"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinCurrentCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinRxdCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinTxdCellCnt"),
        ("CISCO-MGX82XX-VIRTUAL-PORT-MIB", "vrtlIntrQbinDiscardedCellCnt"))
)
if mibBuilder.loadTexts:
    cmvPortQbinStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmvPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmvPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-VIRTUAL-PORT-MIB",
    **{"virtualInterfaceCnf": virtualInterfaceCnf,
       "vrtlIntrConfigTable": vrtlIntrConfigTable,
       "vrtlIntrConfigEntry": vrtlIntrConfigEntry,
       "configVrtlIntrNum": configVrtlIntrNum,
       "vrtlIntrPortNum": vrtlIntrPortNum,
       "vrtlIntrState": vrtlIntrState,
       "vrtlIntrMaxQueMem": vrtlIntrMaxQueMem,
       "vrtlIntrMinCellRate": vrtlIntrMinCellRate,
       "vrtlIntrMaxCellRate": vrtlIntrMaxCellRate,
       "vrtlIntrCurrConfigPaths": vrtlIntrCurrConfigPaths,
       "virtualInterfaceCnt": virtualInterfaceCnt,
       "vrtlIntrCounterTable": vrtlIntrCounterTable,
       "vrtlIntrCounterEntry": vrtlIntrCounterEntry,
       "countVrtlIntrNum": countVrtlIntrNum,
       "vrtlIntrTotalCellCnt": vrtlIntrTotalCellCnt,
       "vrtlIntrTotalQbinCellCnt": vrtlIntrTotalQbinCellCnt,
       "vrtlIntrRxdValidOAMCellCnt": vrtlIntrRxdValidOAMCellCnt,
       "vrtlIntrRxdRmCellCnt": vrtlIntrRxdRmCellCnt,
       "vrtlIntrRxdClpUntaggedCellCnt": vrtlIntrRxdClpUntaggedCellCnt,
       "vrtlIntrRxdClpTaggedCellCnt": vrtlIntrRxdClpTaggedCellCnt,
       "vrtlIntrRxdClpUntaggedDiscardedCellCnt": vrtlIntrRxdClpUntaggedDiscardedCellCnt,
       "vrtlIntrRxdClpTaggedDiscardedCellCnt": vrtlIntrRxdClpTaggedDiscardedCellCnt,
       "vrtlIntrXmtdOAMCellCnt": vrtlIntrXmtdOAMCellCnt,
       "vrtlIntrXmtdRmCellCnt": vrtlIntrXmtdRmCellCnt,
       "vrtlIntrXmtdClpUntaggedCellCnt": vrtlIntrXmtdClpUntaggedCellCnt,
       "vrtlIntrXmtdClpTaggedCellCnt": vrtlIntrXmtdClpTaggedCellCnt,
       "virtualInterfaceQbinCnf": virtualInterfaceQbinCnf,
       "vrtlIntrQbinConfigTable": vrtlIntrQbinConfigTable,
       "vrtlIntrQbinConfigEntry": vrtlIntrQbinConfigEntry,
       "queConfigVrtlIntrNum": queConfigVrtlIntrNum,
       "queConfigVrtlIntrQbinNum": queConfigVrtlIntrQbinNum,
       "vrtlIntrQbinState": vrtlIntrQbinState,
       "vrtlIntrQbinPri": vrtlIntrQbinPri,
       "vrtlIntrQbinRate": vrtlIntrQbinRate,
       "vrtlIntrQbinDiscardSelection": vrtlIntrQbinDiscardSelection,
       "vrtlIntrQbinMaxThreshold": vrtlIntrQbinMaxThreshold,
       "vrtlIntrQbinClpHiThreshold": vrtlIntrQbinClpHiThreshold,
       "vrtlIntrQbinClpLoThreshold": vrtlIntrQbinClpLoThreshold,
       "vrtlIntrQbinFrameDiscardThreshold": vrtlIntrQbinFrameDiscardThreshold,
       "vrtlIntrQbinEfciThreshold": vrtlIntrQbinEfciThreshold,
       "virtualInterfaceQbinCnt": virtualInterfaceQbinCnt,
       "vrtlIntrQbinCounterTable": vrtlIntrQbinCounterTable,
       "vrtlIntrQbinCounterEntry": vrtlIntrQbinCounterEntry,
       "queConuterVrtlIntrNum": queConuterVrtlIntrNum,
       "queCounterVrtlIntrQbinNum": queCounterVrtlIntrQbinNum,
       "vrtlIntrQbinCurrentCellCnt": vrtlIntrQbinCurrentCellCnt,
       "vrtlIntrQbinRxdCellCnt": vrtlIntrQbinRxdCellCnt,
       "vrtlIntrQbinTxdCellCnt": vrtlIntrQbinTxdCellCnt,
       "vrtlIntrQbinDiscardedCellCnt": vrtlIntrQbinDiscardedCellCnt,
       "ciscoMgx82xxVirtualPortMIB": ciscoMgx82xxVirtualPortMIB,
       "cmvPortMIBConformance": cmvPortMIBConformance,
       "cmvPortMIBGroups": cmvPortMIBGroups,
       "cmvPortConfGroup": cmvPortConfGroup,
       "cmvPortStatsGroup": cmvPortStatsGroup,
       "cmvPortQbinConfGroup": cmvPortQbinConfGroup,
       "cmvPortQbinStatsGroup": cmvPortQbinStatsGroup,
       "cmvPortMIBCompliances": cmvPortMIBCompliances,
       "cmvPortCompliance": cmvPortCompliance}
)
