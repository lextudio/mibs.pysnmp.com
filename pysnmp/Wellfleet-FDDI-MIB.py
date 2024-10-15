# SNMP MIB module (Wellfleet-FDDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-FDDI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:12 2024
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

(wfFddiGroup,
 wfLine) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFddiGroup",
    "wfLine")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfFddiTable_Object = MibTable
wfFddiTable = _WfFddiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4)
)
if mibBuilder.loadTexts:
    wfFddiTable.setStatus("mandatory")
_WfFddiEntry_Object = MibTableRow
wfFddiEntry = _WfFddiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1)
)
wfFddiEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFDDISlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFDDINode"),
)
if mibBuilder.loadTexts:
    wfFddiEntry.setStatus("mandatory")


class _WfFDDIDelete_Type(Integer32):
    """Custom type wfFDDIDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfFDDIDelete_Type.__name__ = "Integer32"
_WfFDDIDelete_Object = MibTableColumn
wfFDDIDelete = _WfFDDIDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 1),
    _WfFDDIDelete_Type()
)
wfFDDIDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIDelete.setStatus("mandatory")


class _WfFDDIEnable_Type(Integer32):
    """Custom type wfFDDIEnable based on Integer32"""
    defaultValue = 1

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


_WfFDDIEnable_Type.__name__ = "Integer32"
_WfFDDIEnable_Object = MibTableColumn
wfFDDIEnable = _WfFDDIEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 2),
    _WfFDDIEnable_Type()
)
wfFDDIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIEnable.setStatus("mandatory")


class _WfFDDIState_Type(Integer32):
    """Custom type wfFDDIState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfFDDIState_Type.__name__ = "Integer32"
_WfFDDIState_Object = MibTableColumn
wfFDDIState = _WfFDDIState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 3),
    _WfFDDIState_Type()
)
wfFDDIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIState.setStatus("mandatory")


class _WfFDDISlot_Type(Integer32):
    """Custom type wfFDDISlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfFDDISlot_Type.__name__ = "Integer32"
_WfFDDISlot_Object = MibTableColumn
wfFDDISlot = _WfFDDISlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 4),
    _WfFDDISlot_Type()
)
wfFDDISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDISlot.setStatus("mandatory")


class _WfFDDINode_Type(Integer32):
    """Custom type wfFDDINode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfFDDINode_Type.__name__ = "Integer32"
_WfFDDINode_Object = MibTableColumn
wfFDDINode = _WfFDDINode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 5),
    _WfFDDINode_Type()
)
wfFDDINode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDINode.setStatus("mandatory")


class _WfFDDICct_Type(Integer32):
    """Custom type wfFDDICct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfFDDICct_Type.__name__ = "Integer32"
_WfFDDICct_Object = MibTableColumn
wfFDDICct = _WfFDDICct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 6),
    _WfFDDICct_Type()
)
wfFDDICct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDICct.setStatus("mandatory")


class _WfFDDIBofl_Type(Integer32):
    """Custom type wfFDDIBofl based on Integer32"""
    defaultValue = 1

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


_WfFDDIBofl_Type.__name__ = "Integer32"
_WfFDDIBofl_Object = MibTableColumn
wfFDDIBofl = _WfFDDIBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 7),
    _WfFDDIBofl_Type()
)
wfFDDIBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIBofl.setStatus("mandatory")


class _WfFDDIBoflTmo_Type(Integer32):
    """Custom type wfFDDIBoflTmo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WfFDDIBoflTmo_Type.__name__ = "Integer32"
_WfFDDIBoflTmo_Object = MibTableColumn
wfFDDIBoflTmo = _WfFDDIBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 8),
    _WfFDDIBoflTmo_Type()
)
wfFDDIBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIBoflTmo.setStatus("mandatory")


class _WfFDDIMtu_Type(Integer32):
    """Custom type wfFDDIMtu based on Integer32"""
    defaultValue = 4495

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4495
        )
    )
    namedValues = NamedValues(
        ("default", 4495)
    )


_WfFDDIMtu_Type.__name__ = "Integer32"
_WfFDDIMtu_Object = MibTableColumn
wfFDDIMtu = _WfFDDIMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 9),
    _WfFDDIMtu_Type()
)
wfFDDIMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMtu.setStatus("mandatory")
_WfFDDIMadr_Type = OctetString
_WfFDDIMadr_Object = MibTableColumn
wfFDDIMadr = _WfFDDIMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 10),
    _WfFDDIMadr_Type()
)
wfFDDIMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMadr.setStatus("mandatory")
_WfFDDIOctetsRxOk_Type = Counter32
_WfFDDIOctetsRxOk_Object = MibTableColumn
wfFDDIOctetsRxOk = _WfFDDIOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 11),
    _WfFDDIOctetsRxOk_Type()
)
wfFDDIOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIOctetsRxOk.setStatus("mandatory")
_WfFDDIFramesRxOk_Type = Counter32
_WfFDDIFramesRxOk_Object = MibTableColumn
wfFDDIFramesRxOk = _WfFDDIFramesRxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 12),
    _WfFDDIFramesRxOk_Type()
)
wfFDDIFramesRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIFramesRxOk.setStatus("mandatory")
_WfFDDIOctetsTxOk_Type = Counter32
_WfFDDIOctetsTxOk_Object = MibTableColumn
wfFDDIOctetsTxOk = _WfFDDIOctetsTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 13),
    _WfFDDIOctetsTxOk_Type()
)
wfFDDIOctetsTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIOctetsTxOk.setStatus("mandatory")
_WfFDDIFramesTxOk_Type = Counter32
_WfFDDIFramesTxOk_Object = MibTableColumn
wfFDDIFramesTxOk = _WfFDDIFramesTxOk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 14),
    _WfFDDIFramesTxOk_Type()
)
wfFDDIFramesTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIFramesTxOk.setStatus("mandatory")
_WfFDDICrcErrRx_Type = Counter32
_WfFDDICrcErrRx_Object = MibTableColumn
wfFDDICrcErrRx = _WfFDDICrcErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 15),
    _WfFDDICrcErrRx_Type()
)
wfFDDICrcErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDICrcErrRx.setStatus("mandatory")
_WfFDDIOverrunRx_Type = Counter32
_WfFDDIOverrunRx_Object = MibTableColumn
wfFDDIOverrunRx = _WfFDDIOverrunRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 16),
    _WfFDDIOverrunRx_Type()
)
wfFDDIOverrunRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIOverrunRx.setStatus("mandatory")
_WfFDDIParityErrRx_Type = Counter32
_WfFDDIParityErrRx_Object = MibTableColumn
wfFDDIParityErrRx = _WfFDDIParityErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 17),
    _WfFDDIParityErrRx_Type()
)
wfFDDIParityErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIParityErrRx.setStatus("mandatory")
_WfFDDIMacErrRx_Type = Counter32
_WfFDDIMacErrRx_Object = MibTableColumn
wfFDDIMacErrRx = _WfFDDIMacErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 18),
    _WfFDDIMacErrRx_Type()
)
wfFDDIMacErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacErrRx.setStatus("mandatory")
_WfFDDIRingErrRx_Type = Counter32
_WfFDDIRingErrRx_Object = MibTableColumn
wfFDDIRingErrRx = _WfFDDIRingErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 19),
    _WfFDDIRingErrRx_Type()
)
wfFDDIRingErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRingErrRx.setStatus("mandatory")
_WfFDDISmtRingErrRx_Type = Counter32
_WfFDDISmtRingErrRx_Object = MibTableColumn
wfFDDISmtRingErrRx = _WfFDDISmtRingErrRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 20),
    _WfFDDISmtRingErrRx_Type()
)
wfFDDISmtRingErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDISmtRingErrRx.setStatus("mandatory")
_WfFDDIRingOverrunRx_Type = Counter32
_WfFDDIRingOverrunRx_Object = MibTableColumn
wfFDDIRingOverrunRx = _WfFDDIRingOverrunRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 21),
    _WfFDDIRingOverrunRx_Type()
)
wfFDDIRingOverrunRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRingOverrunRx.setStatus("mandatory")
_WfFDDISmtRingOverrunRx_Type = Counter32
_WfFDDISmtRingOverrunRx_Object = MibTableColumn
wfFDDISmtRingOverrunRx = _WfFDDISmtRingOverrunRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 22),
    _WfFDDISmtRingOverrunRx_Type()
)
wfFDDISmtRingOverrunRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDISmtRingOverrunRx.setStatus("mandatory")
_WfFDDIAbortTx_Type = Counter32
_WfFDDIAbortTx_Object = MibTableColumn
wfFDDIAbortTx = _WfFDDIAbortTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 23),
    _WfFDDIAbortTx_Type()
)
wfFDDIAbortTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIAbortTx.setStatus("mandatory")
_WfFDDIUnderrunTx_Type = Counter32
_WfFDDIUnderrunTx_Object = MibTableColumn
wfFDDIUnderrunTx = _WfFDDIUnderrunTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 24),
    _WfFDDIUnderrunTx_Type()
)
wfFDDIUnderrunTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIUnderrunTx.setStatus("mandatory")
_WfFDDIParityErrTx_Type = Counter32
_WfFDDIParityErrTx_Object = MibTableColumn
wfFDDIParityErrTx = _WfFDDIParityErrTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 25),
    _WfFDDIParityErrTx_Type()
)
wfFDDIParityErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIParityErrTx.setStatus("mandatory")
_WfFDDIRingErrTx_Type = Counter32
_WfFDDIRingErrTx_Object = MibTableColumn
wfFDDIRingErrTx = _WfFDDIRingErrTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 26),
    _WfFDDIRingErrTx_Type()
)
wfFDDIRingErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRingErrTx.setStatus("mandatory")
_WfFDDIPortOpErr_Type = Counter32
_WfFDDIPortOpErr_Object = MibTableColumn
wfFDDIPortOpErr = _WfFDDIPortOpErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 27),
    _WfFDDIPortOpErr_Type()
)
wfFDDIPortOpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIPortOpErr.setStatus("mandatory")
_WfFDDIInternOpErr_Type = Counter32
_WfFDDIInternOpErr_Object = MibTableColumn
wfFDDIInternOpErr = _WfFDDIInternOpErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 28),
    _WfFDDIInternOpErr_Type()
)
wfFDDIInternOpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIInternOpErr.setStatus("mandatory")
_WfFDDIHostErr_Type = Counter32
_WfFDDIHostErr_Object = MibTableColumn
wfFDDIHostErr = _WfFDDIHostErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 29),
    _WfFDDIHostErr_Type()
)
wfFDDIHostErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIHostErr.setStatus("mandatory")


class _WfFDDISmtConnectionPolicy_Type(Integer32):
    """Custom type wfFDDISmtConnectionPolicy based on Integer32"""
    defaultValue = 65381

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65381
        )
    )
    namedValues = NamedValues(
        ("default", 65381)
    )


_WfFDDISmtConnectionPolicy_Type.__name__ = "Integer32"
_WfFDDISmtConnectionPolicy_Object = MibTableColumn
wfFDDISmtConnectionPolicy = _WfFDDISmtConnectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 30),
    _WfFDDISmtConnectionPolicy_Type()
)
wfFDDISmtConnectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDISmtConnectionPolicy.setStatus("mandatory")


class _WfFDDISmtTNotify_Type(Integer32):
    """Custom type wfFDDISmtTNotify based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_WfFDDISmtTNotify_Type.__name__ = "Integer32"
_WfFDDISmtTNotify_Object = MibTableColumn
wfFDDISmtTNotify = _WfFDDISmtTNotify_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 31),
    _WfFDDISmtTNotify_Type()
)
wfFDDISmtTNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDISmtTNotify.setStatus("mandatory")


class _WfFDDIMacTReq_Type(Integer32):
    """Custom type wfFDDIMacTReq based on Integer32"""
    defaultValue = 2062500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2062500
        )
    )
    namedValues = NamedValues(
        ("default", 2062500)
    )


_WfFDDIMacTReq_Type.__name__ = "Integer32"
_WfFDDIMacTReq_Object = MibTableColumn
wfFDDIMacTReq = _WfFDDIMacTReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 32),
    _WfFDDIMacTReq_Type()
)
wfFDDIMacTReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIMacTReq.setStatus("mandatory")
_WfFDDIMacTMax_Type = Integer32
_WfFDDIMacTMax_Object = MibTableColumn
wfFDDIMacTMax = _WfFDDIMacTMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 33),
    _WfFDDIMacTMax_Type()
)
wfFDDIMacTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacTMax.setStatus("mandatory")
_WfFDDIMacTvxValue_Type = Integer32
_WfFDDIMacTvxValue_Object = MibTableColumn
wfFDDIMacTvxValue = _WfFDDIMacTvxValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 34),
    _WfFDDIMacTvxValue_Type()
)
wfFDDIMacTvxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacTvxValue.setStatus("mandatory")


class _WfFDDIMacTMin_Type(Integer32):
    """Custom type wfFDDIMacTMin based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50000
        )
    )
    namedValues = NamedValues(
        ("default", 50000)
    )


_WfFDDIMacTMin_Type.__name__ = "Integer32"
_WfFDDIMacTMin_Object = MibTableColumn
wfFDDIMacTMin = _WfFDDIMacTMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 35),
    _WfFDDIMacTMin_Type()
)
wfFDDIMacTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIMacTMin.setStatus("mandatory")


class _WfFDDIHardwareFilter_Type(Integer32):
    """Custom type wfFDDIHardwareFilter based on Integer32"""
    defaultValue = 2

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


_WfFDDIHardwareFilter_Type.__name__ = "Integer32"
_WfFDDIHardwareFilter_Object = MibTableColumn
wfFDDIHardwareFilter = _WfFDDIHardwareFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 36),
    _WfFDDIHardwareFilter_Type()
)
wfFDDIHardwareFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIHardwareFilter.setStatus("mandatory")


class _WfFDDISmtEnable_Type(Integer32):
    """Custom type wfFDDISmtEnable based on Integer32"""
    defaultValue = 1

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


_WfFDDISmtEnable_Type.__name__ = "Integer32"
_WfFDDISmtEnable_Object = MibTableColumn
wfFDDISmtEnable = _WfFDDISmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 37),
    _WfFDDISmtEnable_Type()
)
wfFDDISmtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDISmtEnable.setStatus("mandatory")
_WfFDDITxQueueLength_Type = Integer32
_WfFDDITxQueueLength_Object = MibTableColumn
wfFDDITxQueueLength = _WfFDDITxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 38),
    _WfFDDITxQueueLength_Type()
)
wfFDDITxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDITxQueueLength.setStatus("mandatory")
_WfFDDIRxQueueLength_Type = Integer32
_WfFDDIRxQueueLength_Object = MibTableColumn
wfFDDIRxQueueLength = _WfFDDIRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 39),
    _WfFDDIRxQueueLength_Type()
)
wfFDDIRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxQueueLength.setStatus("mandatory")
_WfFDDITxClipFrames_Type = Counter32
_WfFDDITxClipFrames_Object = MibTableColumn
wfFDDITxClipFrames = _WfFDDITxClipFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 40),
    _WfFDDITxClipFrames_Type()
)
wfFDDITxClipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDITxClipFrames.setStatus("mandatory")
_WfFDDIRxReplenMisses_Type = Counter32
_WfFDDIRxReplenMisses_Object = MibTableColumn
wfFDDIRxReplenMisses = _WfFDDIRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 41),
    _WfFDDIRxReplenMisses_Type()
)
wfFDDIRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxReplenMisses.setStatus("mandatory")


class _WfFDDICfgTxQueueLength_Type(Integer32):
    """Custom type wfFDDICfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfFDDICfgTxQueueLength_Type.__name__ = "Integer32"
_WfFDDICfgTxQueueLength_Object = MibTableColumn
wfFDDICfgTxQueueLength = _WfFDDICfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 42),
    _WfFDDICfgTxQueueLength_Type()
)
wfFDDICfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDICfgTxQueueLength.setStatus("mandatory")


class _WfFDDICfgRxQueueLength_Type(Integer32):
    """Custom type wfFDDICfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfFDDICfgRxQueueLength_Type.__name__ = "Integer32"
_WfFDDICfgRxQueueLength_Object = MibTableColumn
wfFDDICfgRxQueueLength = _WfFDDICfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 43),
    _WfFDDICfgRxQueueLength_Type()
)
wfFDDICfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDICfgRxQueueLength.setStatus("mandatory")
_WfFDDILineNumber_Type = Integer32
_WfFDDILineNumber_Object = MibTableColumn
wfFDDILineNumber = _WfFDDILineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 44),
    _WfFDDILineNumber_Type()
)
wfFDDILineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDILineNumber.setStatus("mandatory")


class _WfFDDIForcePeerTree_Type(Integer32):
    """Custom type wfFDDIForcePeerTree based on Integer32"""
    defaultValue = 2

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


_WfFDDIForcePeerTree_Type.__name__ = "Integer32"
_WfFDDIForcePeerTree_Object = MibTableColumn
wfFDDIForcePeerTree = _WfFDDIForcePeerTree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 45),
    _WfFDDIForcePeerTree_Type()
)
wfFDDIForcePeerTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIForcePeerTree.setStatus("mandatory")
_WfFDDIInvalidFrameStatusRx_Type = Counter32
_WfFDDIInvalidFrameStatusRx_Object = MibTableColumn
wfFDDIInvalidFrameStatusRx = _WfFDDIInvalidFrameStatusRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 46),
    _WfFDDIInvalidFrameStatusRx_Type()
)
wfFDDIInvalidFrameStatusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIInvalidFrameStatusRx.setStatus("mandatory")
_WfFDDIRxOversizedFrames_Type = Counter32
_WfFDDIRxOversizedFrames_Object = MibTableColumn
wfFDDIRxOversizedFrames = _WfFDDIRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 47),
    _WfFDDIRxOversizedFrames_Type()
)
wfFDDIRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxOversizedFrames.setStatus("mandatory")
_WfFDDIRxSmtOversizedFrames_Type = Counter32
_WfFDDIRxSmtOversizedFrames_Object = MibTableColumn
wfFDDIRxSmtOversizedFrames = _WfFDDIRxSmtOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 48),
    _WfFDDIRxSmtOversizedFrames_Type()
)
wfFDDIRxSmtOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxSmtOversizedFrames.setStatus("mandatory")
_WfFDDIRxUndersizedFrames_Type = Counter32
_WfFDDIRxUndersizedFrames_Object = MibTableColumn
wfFDDIRxUndersizedFrames = _WfFDDIRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 49),
    _WfFDDIRxUndersizedFrames_Type()
)
wfFDDIRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxUndersizedFrames.setStatus("mandatory")
_WfFDDIRxSmtUndersizedFrames_Type = Counter32
_WfFDDIRxSmtUndersizedFrames_Object = MibTableColumn
wfFDDIRxSmtUndersizedFrames = _WfFDDIRxSmtUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 50),
    _WfFDDIRxSmtUndersizedFrames_Type()
)
wfFDDIRxSmtUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxSmtUndersizedFrames.setStatus("mandatory")


class _WfFDDIModule_Type(Integer32):
    """Custom type wfFDDIModule based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfFDDIModule_Type.__name__ = "Integer32"
_WfFDDIModule_Object = MibTableColumn
wfFDDIModule = _WfFDDIModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 51),
    _WfFDDIModule_Type()
)
wfFDDIModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIModule.setStatus("mandatory")


class _WfFDDIActualNode_Type(Integer32):
    """Custom type wfFDDIActualNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfFDDIActualNode_Type.__name__ = "Integer32"
_WfFDDIActualNode_Object = MibTableColumn
wfFDDIActualNode = _WfFDDIActualNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 52),
    _WfFDDIActualNode_Type()
)
wfFDDIActualNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIActualNode.setStatus("mandatory")
_WfFDDILastChange_Type = TimeTicks
_WfFDDILastChange_Object = MibTableColumn
wfFDDILastChange = _WfFDDILastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 53),
    _WfFDDILastChange_Type()
)
wfFDDILastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDILastChange.setStatus("mandatory")
_WfFDDIOutQLen_Type = Gauge32
_WfFDDIOutQLen_Object = MibTableColumn
wfFDDIOutQLen = _WfFDDIOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 54),
    _WfFDDIOutQLen_Type()
)
wfFDDIOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIOutQLen.setStatus("mandatory")
_WfFDDIRxSmtOctets_Type = Counter32
_WfFDDIRxSmtOctets_Object = MibTableColumn
wfFDDIRxSmtOctets = _WfFDDIRxSmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 55),
    _WfFDDIRxSmtOctets_Type()
)
wfFDDIRxSmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxSmtOctets.setStatus("mandatory")
_WfFDDIRxSmtFrames_Type = Counter32
_WfFDDIRxSmtFrames_Object = MibTableColumn
wfFDDIRxSmtFrames = _WfFDDIRxSmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 56),
    _WfFDDIRxSmtFrames_Type()
)
wfFDDIRxSmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxSmtFrames.setStatus("mandatory")
_WfFDDIIntProcessings_Type = Counter32
_WfFDDIIntProcessings_Object = MibTableColumn
wfFDDIIntProcessings = _WfFDDIIntProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 57),
    _WfFDDIIntProcessings_Type()
)
wfFDDIIntProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIIntProcessings.setStatus("mandatory")
_WfFDDITxProcessings_Type = Counter32
_WfFDDITxProcessings_Object = MibTableColumn
wfFDDITxProcessings = _WfFDDITxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 58),
    _WfFDDITxProcessings_Type()
)
wfFDDITxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDITxProcessings.setStatus("mandatory")
_WfFDDIRxProcessings_Type = Counter32
_WfFDDIRxProcessings_Object = MibTableColumn
wfFDDIRxProcessings = _WfFDDIRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 59),
    _WfFDDIRxProcessings_Type()
)
wfFDDIRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIRxProcessings.setStatus("mandatory")
_WfFDDITxRNRProcessings_Type = Counter32
_WfFDDITxRNRProcessings_Object = MibTableColumn
wfFDDITxRNRProcessings = _WfFDDITxRNRProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 60),
    _WfFDDITxRNRProcessings_Type()
)
wfFDDITxRNRProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDITxRNRProcessings.setStatus("mandatory")
_WfFDDISmtRxProcessings_Type = Counter32
_WfFDDISmtRxProcessings_Object = MibTableColumn
wfFDDISmtRxProcessings = _WfFDDISmtRxProcessings_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 61),
    _WfFDDISmtRxProcessings_Type()
)
wfFDDISmtRxProcessings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDISmtRxProcessings.setStatus("mandatory")
_WfFDDIPhyALogPtr_Type = Integer32
_WfFDDIPhyALogPtr_Object = MibTableColumn
wfFDDIPhyALogPtr = _WfFDDIPhyALogPtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 62),
    _WfFDDIPhyALogPtr_Type()
)
wfFDDIPhyALogPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIPhyALogPtr.setStatus("mandatory")
_WfFDDIPhyBLogPtr_Type = Integer32
_WfFDDIPhyBLogPtr_Object = MibTableColumn
wfFDDIPhyBLogPtr = _WfFDDIPhyBLogPtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 63),
    _WfFDDIPhyBLogPtr_Type()
)
wfFDDIPhyBLogPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFDDIPhyBLogPtr.setStatus("mandatory")


class _WfFDDIPromiscuous_Type(Integer32):
    """Custom type wfFDDIPromiscuous based on Integer32"""
    defaultValue = 1

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


_WfFDDIPromiscuous_Type.__name__ = "Integer32"
_WfFDDIPromiscuous_Object = MibTableColumn
wfFDDIPromiscuous = _WfFDDIPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 64),
    _WfFDDIPromiscuous_Type()
)
wfFDDIPromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIPromiscuous.setStatus("mandatory")


class _WfFDDILLCFrameControl_Type(Integer32):
    """Custom type wfFDDILLCFrameControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("sync", 2))
    )


_WfFDDILLCFrameControl_Type.__name__ = "Integer32"
_WfFDDILLCFrameControl_Object = MibTableColumn
wfFDDILLCFrameControl = _WfFDDILLCFrameControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 65),
    _WfFDDILLCFrameControl_Type()
)
wfFDDILLCFrameControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDILLCFrameControl.setStatus("mandatory")


class _WfFDDITurboBofl_Type(Integer32):
    """Custom type wfFDDITurboBofl based on Integer32"""
    defaultValue = 2

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


_WfFDDITurboBofl_Type.__name__ = "Integer32"
_WfFDDITurboBofl_Object = MibTableColumn
wfFDDITurboBofl = _WfFDDITurboBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 66),
    _WfFDDITurboBofl_Type()
)
wfFDDITurboBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDITurboBofl.setStatus("mandatory")


class _WfFDDIBoflNum_Type(Integer32):
    """Custom type wfFDDIBoflNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfFDDIBoflNum_Type.__name__ = "Integer32"
_WfFDDIBoflNum_Object = MibTableColumn
wfFDDIBoflNum = _WfFDDIBoflNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 67),
    _WfFDDIBoflNum_Type()
)
wfFDDIBoflNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIBoflNum.setStatus("mandatory")


class _WfFDDIBoflLen_Type(Integer32):
    """Custom type wfFDDIBoflLen based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 4450),
    )


_WfFDDIBoflLen_Type.__name__ = "Integer32"
_WfFDDIBoflLen_Object = MibTableColumn
wfFDDIBoflLen = _WfFDDIBoflLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 4, 1, 68),
    _WfFDDIBoflLen_Type()
)
wfFDDIBoflLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFDDIBoflLen.setStatus("mandatory")
_WfFddiSmtGroup_ObjectIdentity = ObjectIdentity
wfFddiSmtGroup = _WfFddiSmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1)
)
_WfFddiSmtTable_Object = MibTable
wfFddiSmtTable = _WfFddiSmtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2)
)
if mibBuilder.loadTexts:
    wfFddiSmtTable.setStatus("mandatory")
_WfFddiSmtEntry_Object = MibTableRow
wfFddiSmtEntry = _WfFddiSmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1)
)
wfFddiSmtEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiSmtSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiSmtNode"),
)
if mibBuilder.loadTexts:
    wfFddiSmtEntry.setStatus("mandatory")
_WfFddiSmtSlot_Type = Integer32
_WfFddiSmtSlot_Object = MibTableColumn
wfFddiSmtSlot = _WfFddiSmtSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 1),
    _WfFddiSmtSlot_Type()
)
wfFddiSmtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtSlot.setStatus("mandatory")
_WfFddiSmtNode_Type = Integer32
_WfFddiSmtNode_Object = MibTableColumn
wfFddiSmtNode = _WfFddiSmtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 2),
    _WfFddiSmtNode_Type()
)
wfFddiSmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtNode.setStatus("mandatory")
_WfFddiSmtCct_Type = Integer32
_WfFddiSmtCct_Object = MibTableColumn
wfFddiSmtCct = _WfFddiSmtCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 3),
    _WfFddiSmtCct_Type()
)
wfFddiSmtCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtCct.setStatus("mandatory")
_WfFddiSmtStationId_Type = OctetString
_WfFddiSmtStationId_Object = MibTableColumn
wfFddiSmtStationId = _WfFddiSmtStationId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 4),
    _WfFddiSmtStationId_Type()
)
wfFddiSmtStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtStationId.setStatus("mandatory")
_WfFddiSmtOpVersionId_Type = Integer32
_WfFddiSmtOpVersionId_Object = MibTableColumn
wfFddiSmtOpVersionId = _WfFddiSmtOpVersionId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 5),
    _WfFddiSmtOpVersionId_Type()
)
wfFddiSmtOpVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtOpVersionId.setStatus("mandatory")
_WfFddiSmtMacCt_Type = Integer32
_WfFddiSmtMacCt_Object = MibTableColumn
wfFddiSmtMacCt = _WfFddiSmtMacCt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 6),
    _WfFddiSmtMacCt_Type()
)
wfFddiSmtMacCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtMacCt.setStatus("mandatory")
_WfFddiSmtNonMasterCt_Type = Integer32
_WfFddiSmtNonMasterCt_Object = MibTableColumn
wfFddiSmtNonMasterCt = _WfFddiSmtNonMasterCt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 7),
    _WfFddiSmtNonMasterCt_Type()
)
wfFddiSmtNonMasterCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtNonMasterCt.setStatus("mandatory")


class _WfFddiSmtEcmState_Type(Integer32):
    """Custom type wfFddiSmtEcmState based on Integer32"""
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
        *(("check", 7),
          ("deinsert", 8),
          ("in", 2),
          ("insert", 6),
          ("leave", 4),
          ("out", 1),
          ("pathtest", 5),
          ("trace", 3))
    )


_WfFddiSmtEcmState_Type.__name__ = "Integer32"
_WfFddiSmtEcmState_Object = MibTableColumn
wfFddiSmtEcmState = _WfFddiSmtEcmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 8),
    _WfFddiSmtEcmState_Type()
)
wfFddiSmtEcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtEcmState.setStatus("mandatory")


class _WfFddiSmtCfState_Type(Integer32):
    """Custom type wfFddiSmtCfState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("cwrapa", 11),
          ("cwrapb", 12),
          ("cwraps", 13),
          ("isolated", 1),
          ("locala", 7),
          ("localab", 9),
          ("localb", 8),
          ("locals", 10),
          ("thru", 6),
          ("wrapa", 3),
          ("wrapab", 5),
          ("wrapb", 4),
          ("wraps", 2))
    )


_WfFddiSmtCfState_Type.__name__ = "Integer32"
_WfFddiSmtCfState_Object = MibTableColumn
wfFddiSmtCfState = _WfFddiSmtCfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 9),
    _WfFddiSmtCfState_Type()
)
wfFddiSmtCfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtCfState.setStatus("mandatory")


class _WfFddiSmtBypassPresent_Type(Integer32):
    """Custom type wfFddiSmtBypassPresent based on Integer32"""
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


_WfFddiSmtBypassPresent_Type.__name__ = "Integer32"
_WfFddiSmtBypassPresent_Object = MibTableColumn
wfFddiSmtBypassPresent = _WfFddiSmtBypassPresent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 10),
    _WfFddiSmtBypassPresent_Type()
)
wfFddiSmtBypassPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtBypassPresent.setStatus("mandatory")


class _WfFddiSmtRemoteDisconnectFlag_Type(Integer32):
    """Custom type wfFddiSmtRemoteDisconnectFlag based on Integer32"""
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


_WfFddiSmtRemoteDisconnectFlag_Type.__name__ = "Integer32"
_WfFddiSmtRemoteDisconnectFlag_Object = MibTableColumn
wfFddiSmtRemoteDisconnectFlag = _WfFddiSmtRemoteDisconnectFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 11),
    _WfFddiSmtRemoteDisconnectFlag_Type()
)
wfFddiSmtRemoteDisconnectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtRemoteDisconnectFlag.setStatus("mandatory")


class _WfFddiSmtStationStatus_Type(Integer32):
    """Custom type wfFddiSmtStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concatenated", 1),
          ("seperated", 2),
          ("thru", 3))
    )


_WfFddiSmtStationStatus_Type.__name__ = "Integer32"
_WfFddiSmtStationStatus_Object = MibTableColumn
wfFddiSmtStationStatus = _WfFddiSmtStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 12),
    _WfFddiSmtStationStatus_Type()
)
wfFddiSmtStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtStationStatus.setStatus("mandatory")


class _WfFddiSmtPeerWrapFlag_Type(Integer32):
    """Custom type wfFddiSmtPeerWrapFlag based on Integer32"""
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


_WfFddiSmtPeerWrapFlag_Type.__name__ = "Integer32"
_WfFddiSmtPeerWrapFlag_Object = MibTableColumn
wfFddiSmtPeerWrapFlag = _WfFddiSmtPeerWrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 2, 1, 13),
    _WfFddiSmtPeerWrapFlag_Type()
)
wfFddiSmtPeerWrapFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtPeerWrapFlag.setStatus("mandatory")
_WfFddiSmtExtTable_Object = MibTable
wfFddiSmtExtTable = _WfFddiSmtExtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3)
)
if mibBuilder.loadTexts:
    wfFddiSmtExtTable.setStatus("mandatory")
_WfFddiSmtExtEntry_Object = MibTableRow
wfFddiSmtExtEntry = _WfFddiSmtExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1)
)
wfFddiSmtExtEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiSmtExtSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiSmtExtNode"),
)
if mibBuilder.loadTexts:
    wfFddiSmtExtEntry.setStatus("mandatory")


class _WfFddiSmtDelete_Type(Integer32):
    """Custom type wfFddiSmtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfFddiSmtDelete_Type.__name__ = "Integer32"
_WfFddiSmtDelete_Object = MibTableColumn
wfFddiSmtDelete = _WfFddiSmtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 1),
    _WfFddiSmtDelete_Type()
)
wfFddiSmtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiSmtDelete.setStatus("mandatory")
_WfFddiSmtExtSlot_Type = Integer32
_WfFddiSmtExtSlot_Object = MibTableColumn
wfFddiSmtExtSlot = _WfFddiSmtExtSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 2),
    _WfFddiSmtExtSlot_Type()
)
wfFddiSmtExtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtExtSlot.setStatus("mandatory")
_WfFddiSmtExtNode_Type = Integer32
_WfFddiSmtExtNode_Object = MibTableColumn
wfFddiSmtExtNode = _WfFddiSmtExtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 3),
    _WfFddiSmtExtNode_Type()
)
wfFddiSmtExtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtExtNode.setStatus("mandatory")
_WfFddiSmtExtCct_Type = Integer32
_WfFddiSmtExtCct_Object = MibTableColumn
wfFddiSmtExtCct = _WfFddiSmtExtCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 4),
    _WfFddiSmtExtCct_Type()
)
wfFddiSmtExtCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtExtCct.setStatus("mandatory")


class _WfFddiSmtHiVersionId_Type(Integer32):
    """Custom type wfFddiSmtHiVersionId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("id", 2)
    )


_WfFddiSmtHiVersionId_Type.__name__ = "Integer32"
_WfFddiSmtHiVersionId_Object = MibTableColumn
wfFddiSmtHiVersionId = _WfFddiSmtHiVersionId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 5),
    _WfFddiSmtHiVersionId_Type()
)
wfFddiSmtHiVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtHiVersionId.setStatus("mandatory")


class _WfFddiSmtLoVersionId_Type(Integer32):
    """Custom type wfFddiSmtLoVersionId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("id", 2)
    )


_WfFddiSmtLoVersionId_Type.__name__ = "Integer32"
_WfFddiSmtLoVersionId_Object = MibTableColumn
wfFddiSmtLoVersionId = _WfFddiSmtLoVersionId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 6),
    _WfFddiSmtLoVersionId_Type()
)
wfFddiSmtLoVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtLoVersionId.setStatus("mandatory")
_WfFddiSmtManufacturerData_Type = OctetString
_WfFddiSmtManufacturerData_Object = MibTableColumn
wfFddiSmtManufacturerData = _WfFddiSmtManufacturerData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 7),
    _WfFddiSmtManufacturerData_Type()
)
wfFddiSmtManufacturerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtManufacturerData.setStatus("mandatory")
_WfFddiSmtUserData_Type = DisplayString
_WfFddiSmtUserData_Object = MibTableColumn
wfFddiSmtUserData = _WfFddiSmtUserData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 8),
    _WfFddiSmtUserData_Type()
)
wfFddiSmtUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiSmtUserData.setStatus("mandatory")


class _WfFddiSmtMibVersionId_Type(Integer32):
    """Custom type wfFddiSmtMibVersionId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("id", 1)
    )


_WfFddiSmtMibVersionId_Type.__name__ = "Integer32"
_WfFddiSmtMibVersionId_Object = MibTableColumn
wfFddiSmtMibVersionId = _WfFddiSmtMibVersionId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 9),
    _WfFddiSmtMibVersionId_Type()
)
wfFddiSmtMibVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtMibVersionId.setStatus("mandatory")
_WfFddiSmtMasterCts_Type = Integer32
_WfFddiSmtMasterCts_Object = MibTableColumn
wfFddiSmtMasterCts = _WfFddiSmtMasterCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 10),
    _WfFddiSmtMasterCts_Type()
)
wfFddiSmtMasterCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtMasterCts.setStatus("mandatory")


class _WfFddiSmtAvailablePaths_Type(Integer32):
    """Custom type wfFddiSmtAvailablePaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l", 4),
          ("p", 1),
          ("s", 2))
    )


_WfFddiSmtAvailablePaths_Type.__name__ = "Integer32"
_WfFddiSmtAvailablePaths_Object = MibTableColumn
wfFddiSmtAvailablePaths = _WfFddiSmtAvailablePaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 11),
    _WfFddiSmtAvailablePaths_Type()
)
wfFddiSmtAvailablePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtAvailablePaths.setStatus("mandatory")


class _WfFddiSmtConfigCapabilities_Type(Integer32):
    """Custom type wfFddiSmtConfigCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ab", 2),
          ("avail", 1))
    )


_WfFddiSmtConfigCapabilities_Type.__name__ = "Integer32"
_WfFddiSmtConfigCapabilities_Object = MibTableColumn
wfFddiSmtConfigCapabilities = _WfFddiSmtConfigCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 12),
    _WfFddiSmtConfigCapabilities_Type()
)
wfFddiSmtConfigCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtConfigCapabilities.setStatus("mandatory")
_WfFddiSmtConfigPolicy_Type = Integer32
_WfFddiSmtConfigPolicy_Object = MibTableColumn
wfFddiSmtConfigPolicy = _WfFddiSmtConfigPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 13),
    _WfFddiSmtConfigPolicy_Type()
)
wfFddiSmtConfigPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtConfigPolicy.setStatus("mandatory")


class _WfFddiSmtStatRptPolicy_Type(Integer32):
    """Custom type wfFddiSmtStatRptPolicy based on Integer32"""
    defaultValue = 1

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


_WfFddiSmtStatRptPolicy_Type.__name__ = "Integer32"
_WfFddiSmtStatRptPolicy_Object = MibTableColumn
wfFddiSmtStatRptPolicy = _WfFddiSmtStatRptPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 14),
    _WfFddiSmtStatRptPolicy_Type()
)
wfFddiSmtStatRptPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiSmtStatRptPolicy.setStatus("mandatory")


class _WfFddiSmtTraceMaxExpiration_Type(Integer32):
    """Custom type wfFddiSmtTraceMaxExpiration based on Integer32"""
    defaultValue = 7000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6001, 256000),
    )


_WfFddiSmtTraceMaxExpiration_Type.__name__ = "Integer32"
_WfFddiSmtTraceMaxExpiration_Object = MibTableColumn
wfFddiSmtTraceMaxExpiration = _WfFddiSmtTraceMaxExpiration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 15),
    _WfFddiSmtTraceMaxExpiration_Type()
)
wfFddiSmtTraceMaxExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiSmtTraceMaxExpiration.setStatus("mandatory")
_WfFddiSmtTimeStamp_Type = OctetString
_WfFddiSmtTimeStamp_Object = MibTableColumn
wfFddiSmtTimeStamp = _WfFddiSmtTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 16),
    _WfFddiSmtTimeStamp_Type()
)
wfFddiSmtTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtTimeStamp.setStatus("mandatory")
_WfFddiSmtTransitionTimeStamp_Type = OctetString
_WfFddiSmtTransitionTimeStamp_Object = MibTableColumn
wfFddiSmtTransitionTimeStamp = _WfFddiSmtTransitionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 17),
    _WfFddiSmtTransitionTimeStamp_Type()
)
wfFddiSmtTransitionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtTransitionTimeStamp.setStatus("mandatory")


class _WfFddiSmtDatProtocol_Type(Integer32):
    """Custom type wfFddiSmtDatProtocol based on Integer32"""
    defaultValue = 1

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


_WfFddiSmtDatProtocol_Type.__name__ = "Integer32"
_WfFddiSmtDatProtocol_Object = MibTableColumn
wfFddiSmtDatProtocol = _WfFddiSmtDatProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 3, 1, 18),
    _WfFddiSmtDatProtocol_Type()
)
wfFddiSmtDatProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiSmtDatProtocol.setStatus("mandatory")
_WfFddiSmtActionTable_Object = MibTable
wfFddiSmtActionTable = _WfFddiSmtActionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 4)
)
if mibBuilder.loadTexts:
    wfFddiSmtActionTable.setStatus("mandatory")
_WfFddiSmtActionEntry_Object = MibTableRow
wfFddiSmtActionEntry = _WfFddiSmtActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 4, 1)
)
wfFddiSmtActionEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiSmtActionSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiSmtActionNode"),
)
if mibBuilder.loadTexts:
    wfFddiSmtActionEntry.setStatus("mandatory")


class _WfFddiSmtActionDelete_Type(Integer32):
    """Custom type wfFddiSmtActionDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfFddiSmtActionDelete_Type.__name__ = "Integer32"
_WfFddiSmtActionDelete_Object = MibTableColumn
wfFddiSmtActionDelete = _WfFddiSmtActionDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 4, 1, 1),
    _WfFddiSmtActionDelete_Type()
)
wfFddiSmtActionDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiSmtActionDelete.setStatus("mandatory")
_WfFddiSmtActionSlot_Type = Integer32
_WfFddiSmtActionSlot_Object = MibTableColumn
wfFddiSmtActionSlot = _WfFddiSmtActionSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 4, 1, 2),
    _WfFddiSmtActionSlot_Type()
)
wfFddiSmtActionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtActionSlot.setStatus("mandatory")
_WfFddiSmtActionNode_Type = Integer32
_WfFddiSmtActionNode_Object = MibTableColumn
wfFddiSmtActionNode = _WfFddiSmtActionNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 4, 1, 3),
    _WfFddiSmtActionNode_Type()
)
wfFddiSmtActionNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtActionNode.setStatus("mandatory")
_WfFddiSmtActionCct_Type = Integer32
_WfFddiSmtActionCct_Object = MibTableColumn
wfFddiSmtActionCct = _WfFddiSmtActionCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 4, 1, 4),
    _WfFddiSmtActionCct_Type()
)
wfFddiSmtActionCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiSmtActionCct.setStatus("mandatory")


class _WfFddiSmtStationAction_Type(Integer32):
    """Custom type wfFddiSmtStationAction based on Integer32"""
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
        *(("connect", 2),
          ("disablea", 6),
          ("disableb", 7),
          ("disablem", 8),
          ("disconnect", 3),
          ("other", 1),
          ("pathtest", 4),
          ("selftest", 5))
    )


_WfFddiSmtStationAction_Type.__name__ = "Integer32"
_WfFddiSmtStationAction_Object = MibTableColumn
wfFddiSmtStationAction = _WfFddiSmtStationAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 1, 4, 1, 5),
    _WfFddiSmtStationAction_Type()
)
wfFddiSmtStationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiSmtStationAction.setStatus("mandatory")
_WfFddiMacGroup_ObjectIdentity = ObjectIdentity
wfFddiMacGroup = _WfFddiMacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2)
)
_WfFddiMacTable_Object = MibTable
wfFddiMacTable = _WfFddiMacTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2)
)
if mibBuilder.loadTexts:
    wfFddiMacTable.setStatus("mandatory")
_WfFddiMacEntry_Object = MibTableRow
wfFddiMacEntry = _WfFddiMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1)
)
wfFddiMacEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiMacSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiMacNode"),
)
if mibBuilder.loadTexts:
    wfFddiMacEntry.setStatus("mandatory")
_WfFddiMacSlot_Type = Integer32
_WfFddiMacSlot_Object = MibTableColumn
wfFddiMacSlot = _WfFddiMacSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 1),
    _WfFddiMacSlot_Type()
)
wfFddiMacSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacSlot.setStatus("mandatory")
_WfFddiMacNode_Type = Integer32
_WfFddiMacNode_Object = MibTableColumn
wfFddiMacNode = _WfFddiMacNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 2),
    _WfFddiMacNode_Type()
)
wfFddiMacNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacNode.setStatus("mandatory")
_WfFddiMacCct_Type = Integer32
_WfFddiMacCct_Object = MibTableColumn
wfFddiMacCct = _WfFddiMacCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 3),
    _WfFddiMacCct_Type()
)
wfFddiMacCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacCct.setStatus("mandatory")
_WfFddiMacUpstreamNbr_Type = OctetString
_WfFddiMacUpstreamNbr_Object = MibTableColumn
wfFddiMacUpstreamNbr = _WfFddiMacUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 4),
    _WfFddiMacUpstreamNbr_Type()
)
wfFddiMacUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacUpstreamNbr.setStatus("mandatory")
_WfFddiMacDownstreamNbr_Type = OctetString
_WfFddiMacDownstreamNbr_Object = MibTableColumn
wfFddiMacDownstreamNbr = _WfFddiMacDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 5),
    _WfFddiMacDownstreamNbr_Type()
)
wfFddiMacDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacDownstreamNbr.setStatus("mandatory")
_WfFddiMacSmtAddress_Type = OctetString
_WfFddiMacSmtAddress_Object = MibTableColumn
wfFddiMacSmtAddress = _WfFddiMacSmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 6),
    _WfFddiMacSmtAddress_Type()
)
wfFddiMacSmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacSmtAddress.setStatus("mandatory")
_WfFddiMacTNeg_Type = Integer32
_WfFddiMacTNeg_Object = MibTableColumn
wfFddiMacTNeg = _WfFddiMacTNeg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 7),
    _WfFddiMacTNeg_Type()
)
wfFddiMacTNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacTNeg.setStatus("mandatory")


class _WfFddiMacRmtState_Type(Integer32):
    """Custom type wfFddiMacRmtState based on Integer32"""
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
        *(("detect", 4),
          ("directed", 7),
          ("isolated", 1),
          ("nonop", 2),
          ("nonopdup", 5),
          ("ringop", 3),
          ("ringopdup", 6),
          ("trace", 8))
    )


_WfFddiMacRmtState_Type.__name__ = "Integer32"
_WfFddiMacRmtState_Object = MibTableColumn
wfFddiMacRmtState = _WfFddiMacRmtState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 8),
    _WfFddiMacRmtState_Type()
)
wfFddiMacRmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacRmtState.setStatus("mandatory")
_WfFddiMacOldUpstreamNbr_Type = OctetString
_WfFddiMacOldUpstreamNbr_Object = MibTableColumn
wfFddiMacOldUpstreamNbr = _WfFddiMacOldUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 9),
    _WfFddiMacOldUpstreamNbr_Type()
)
wfFddiMacOldUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacOldUpstreamNbr.setStatus("mandatory")
_WfFddiMacOldDownstreamNbr_Type = OctetString
_WfFddiMacOldDownstreamNbr_Object = MibTableColumn
wfFddiMacOldDownstreamNbr = _WfFddiMacOldDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 10),
    _WfFddiMacOldDownstreamNbr_Type()
)
wfFddiMacOldDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacOldDownstreamNbr.setStatus("mandatory")
_WfFddiMacTokenCts_Type = OctetString
_WfFddiMacTokenCts_Object = MibTableColumn
wfFddiMacTokenCts = _WfFddiMacTokenCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 11),
    _WfFddiMacTokenCts_Type()
)
wfFddiMacTokenCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacTokenCts.setStatus("mandatory")
_WfFddiMacErrorCts_Type = OctetString
_WfFddiMacErrorCts_Object = MibTableColumn
wfFddiMacErrorCts = _WfFddiMacErrorCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 12),
    _WfFddiMacErrorCts_Type()
)
wfFddiMacErrorCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacErrorCts.setStatus("mandatory")
_WfFddiMacLostCts_Type = OctetString
_WfFddiMacLostCts_Object = MibTableColumn
wfFddiMacLostCts = _WfFddiMacLostCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 13),
    _WfFddiMacLostCts_Type()
)
wfFddiMacLostCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacLostCts.setStatus("mandatory")


class _WfFddiMacDaFlag_Type(Integer32):
    """Custom type wfFddiMacDaFlag based on Integer32"""
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


_WfFddiMacDaFlag_Type.__name__ = "Integer32"
_WfFddiMacDaFlag_Object = MibTableColumn
wfFddiMacDaFlag = _WfFddiMacDaFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 14),
    _WfFddiMacDaFlag_Type()
)
wfFddiMacDaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacDaFlag.setStatus("mandatory")


class _WfFddiMacUnaDaFlag_Type(Integer32):
    """Custom type wfFddiMacUnaDaFlag based on Integer32"""
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


_WfFddiMacUnaDaFlag_Type.__name__ = "Integer32"
_WfFddiMacUnaDaFlag_Object = MibTableColumn
wfFddiMacUnaDaFlag = _WfFddiMacUnaDaFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 15),
    _WfFddiMacUnaDaFlag_Type()
)
wfFddiMacUnaDaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacUnaDaFlag.setStatus("mandatory")


class _WfFddiMacFrameErrorFlag_Type(Integer32):
    """Custom type wfFddiMacFrameErrorFlag based on Integer32"""
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


_WfFddiMacFrameErrorFlag_Type.__name__ = "Integer32"
_WfFddiMacFrameErrorFlag_Object = MibTableColumn
wfFddiMacFrameErrorFlag = _WfFddiMacFrameErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 16),
    _WfFddiMacFrameErrorFlag_Type()
)
wfFddiMacFrameErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacFrameErrorFlag.setStatus("mandatory")


class _WfFddiMacMaUnitDataAvailable_Type(Integer32):
    """Custom type wfFddiMacMaUnitDataAvailable based on Integer32"""
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


_WfFddiMacMaUnitDataAvailable_Type.__name__ = "Integer32"
_WfFddiMacMaUnitDataAvailable_Object = MibTableColumn
wfFddiMacMaUnitDataAvailable = _WfFddiMacMaUnitDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 17),
    _WfFddiMacMaUnitDataAvailable_Type()
)
wfFddiMacMaUnitDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacMaUnitDataAvailable.setStatus("mandatory")


class _WfFddiMacDownstreamPortType_Type(Integer32):
    """Custom type wfFddiMacDownstreamPortType based on Integer32"""
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
        *(("typea", 1),
          ("typeb", 2),
          ("typem", 4),
          ("typenone", 5),
          ("types", 3))
    )


_WfFddiMacDownstreamPortType_Type.__name__ = "Integer32"
_WfFddiMacDownstreamPortType_Object = MibTableColumn
wfFddiMacDownstreamPortType = _WfFddiMacDownstreamPortType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 2, 1, 18),
    _WfFddiMacDownstreamPortType_Type()
)
wfFddiMacDownstreamPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacDownstreamPortType.setStatus("mandatory")
_WfFddiMacExtTable_Object = MibTable
wfFddiMacExtTable = _WfFddiMacExtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3)
)
if mibBuilder.loadTexts:
    wfFddiMacExtTable.setStatus("mandatory")
_WfFddiMacExtEntry_Object = MibTableRow
wfFddiMacExtEntry = _WfFddiMacExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1)
)
wfFddiMacExtEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiMacExtSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiMacExtNode"),
)
if mibBuilder.loadTexts:
    wfFddiMacExtEntry.setStatus("mandatory")


class _WfFddiMacDelete_Type(Integer32):
    """Custom type wfFddiMacDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfFddiMacDelete_Type.__name__ = "Integer32"
_WfFddiMacDelete_Object = MibTableColumn
wfFddiMacDelete = _WfFddiMacDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 1),
    _WfFddiMacDelete_Type()
)
wfFddiMacDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiMacDelete.setStatus("mandatory")
_WfFddiMacExtSlot_Type = Integer32
_WfFddiMacExtSlot_Object = MibTableColumn
wfFddiMacExtSlot = _WfFddiMacExtSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 2),
    _WfFddiMacExtSlot_Type()
)
wfFddiMacExtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacExtSlot.setStatus("mandatory")
_WfFddiMacExtNode_Type = Integer32
_WfFddiMacExtNode_Object = MibTableColumn
wfFddiMacExtNode = _WfFddiMacExtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 3),
    _WfFddiMacExtNode_Type()
)
wfFddiMacExtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacExtNode.setStatus("mandatory")
_WfFddiMacExtCct_Type = Integer32
_WfFddiMacExtCct_Object = MibTableColumn
wfFddiMacExtCct = _WfFddiMacExtCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 4),
    _WfFddiMacExtCct_Type()
)
wfFddiMacExtCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacExtCct.setStatus("mandatory")


class _WfFddiMacFrameStatusFunctions_Type(Integer32):
    """Custom type wfFddiMacFrameStatusFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 4),
          ("repeat", 1),
          ("set", 2))
    )


_WfFddiMacFrameStatusFunctions_Type.__name__ = "Integer32"
_WfFddiMacFrameStatusFunctions_Object = MibTableColumn
wfFddiMacFrameStatusFunctions = _WfFddiMacFrameStatusFunctions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 5),
    _WfFddiMacFrameStatusFunctions_Type()
)
wfFddiMacFrameStatusFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacFrameStatusFunctions.setStatus("mandatory")


class _WfFddiMacBridgeFunctions_Type(Integer32):
    """Custom type wfFddiMacBridgeFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("srcroute", 2),
          ("srt", 4),
          ("transparent", 1))
    )


_WfFddiMacBridgeFunctions_Type.__name__ = "Integer32"
_WfFddiMacBridgeFunctions_Object = MibTableColumn
wfFddiMacBridgeFunctions = _WfFddiMacBridgeFunctions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 6),
    _WfFddiMacBridgeFunctions_Type()
)
wfFddiMacBridgeFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacBridgeFunctions.setStatus("mandatory")


class _WfFddiMacTMaxCapability_Type(Integer32):
    """Custom type wfFddiMacTMaxCapability based on Integer32"""
    defaultValue = 1336934400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1336934400
        )
    )
    namedValues = NamedValues(
        ("default", 1336934400)
    )


_WfFddiMacTMaxCapability_Type.__name__ = "Integer32"
_WfFddiMacTMaxCapability_Object = MibTableColumn
wfFddiMacTMaxCapability = _WfFddiMacTMaxCapability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 7),
    _WfFddiMacTMaxCapability_Type()
)
wfFddiMacTMaxCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacTMaxCapability.setStatus("mandatory")


class _WfFddiMacTvxCapability_Type(Integer32):
    """Custom type wfFddiMacTvxCapability based on Integer32"""
    defaultValue = 5222400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5222400
        )
    )
    namedValues = NamedValues(
        ("default", 5222400)
    )


_WfFddiMacTvxCapability_Type.__name__ = "Integer32"
_WfFddiMacTvxCapability_Object = MibTableColumn
wfFddiMacTvxCapability = _WfFddiMacTvxCapability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 8),
    _WfFddiMacTvxCapability_Type()
)
wfFddiMacTvxCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacTvxCapability.setStatus("mandatory")


class _WfFddiMacAvailablePaths_Type(Integer32):
    """Custom type wfFddiMacAvailablePaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l", 4),
          ("p", 1),
          ("s", 2))
    )


_WfFddiMacAvailablePaths_Type.__name__ = "Integer32"
_WfFddiMacAvailablePaths_Object = MibTableColumn
wfFddiMacAvailablePaths = _WfFddiMacAvailablePaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 9),
    _WfFddiMacAvailablePaths_Type()
)
wfFddiMacAvailablePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacAvailablePaths.setStatus("mandatory")


class _WfFddiMacCurrentPath_Type(Integer32):
    """Custom type wfFddiMacCurrentPath based on Integer32"""
    defaultValue = 1

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
        *(("concatenated", 5),
          ("isolated", 1),
          ("local", 2),
          ("primary", 4),
          ("secondary", 3),
          ("thru", 6))
    )


_WfFddiMacCurrentPath_Type.__name__ = "Integer32"
_WfFddiMacCurrentPath_Object = MibTableColumn
wfFddiMacCurrentPath = _WfFddiMacCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 10),
    _WfFddiMacCurrentPath_Type()
)
wfFddiMacCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacCurrentPath.setStatus("mandatory")


class _WfFddiMacDupAddrTest_Type(Integer32):
    """Custom type wfFddiMacDupAddrTest based on Integer32"""
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
        *(("fail", 3),
          ("none", 1),
          ("pass", 2))
    )


_WfFddiMacDupAddrTest_Type.__name__ = "Integer32"
_WfFddiMacDupAddrTest_Object = MibTableColumn
wfFddiMacDupAddrTest = _WfFddiMacDupAddrTest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 11),
    _WfFddiMacDupAddrTest_Type()
)
wfFddiMacDupAddrTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacDupAddrTest.setStatus("mandatory")


class _WfFddiMacRequestedPaths_Type(Integer32):
    """Custom type wfFddiMacRequestedPaths based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("calt", 8),
          ("cpref", 64),
          ("local", 1),
          ("palt", 4),
          ("ppref", 32),
          ("salt", 2),
          ("spref", 16),
          ("thru", 128))
    )


_WfFddiMacRequestedPaths_Type.__name__ = "Integer32"
_WfFddiMacRequestedPaths_Object = MibTableColumn
wfFddiMacRequestedPaths = _WfFddiMacRequestedPaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 12),
    _WfFddiMacRequestedPaths_Type()
)
wfFddiMacRequestedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacRequestedPaths.setStatus("mandatory")
_WfFddiMacCopiedCts_Type = Counter32
_WfFddiMacCopiedCts_Object = MibTableColumn
wfFddiMacCopiedCts = _WfFddiMacCopiedCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 13),
    _WfFddiMacCopiedCts_Type()
)
wfFddiMacCopiedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacCopiedCts.setStatus("mandatory")


class _WfFddiMacFrameErrorThreshold_Type(Integer32):
    """Custom type wfFddiMacFrameErrorThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfFddiMacFrameErrorThreshold_Type.__name__ = "Integer32"
_WfFddiMacFrameErrorThreshold_Object = MibTableColumn
wfFddiMacFrameErrorThreshold = _WfFddiMacFrameErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 14),
    _WfFddiMacFrameErrorThreshold_Type()
)
wfFddiMacFrameErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiMacFrameErrorThreshold.setStatus("mandatory")
_WfFddiMacFrameErrorRatio_Type = Integer32
_WfFddiMacFrameErrorRatio_Object = MibTableColumn
wfFddiMacFrameErrorRatio = _WfFddiMacFrameErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 15),
    _WfFddiMacFrameErrorRatio_Type()
)
wfFddiMacFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacFrameErrorRatio.setStatus("mandatory")


class _WfFddiMacHardwarePresent_Type(Integer32):
    """Custom type wfFddiMacHardwarePresent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("present", 2))
    )


_WfFddiMacHardwarePresent_Type.__name__ = "Integer32"
_WfFddiMacHardwarePresent_Object = MibTableColumn
wfFddiMacHardwarePresent = _WfFddiMacHardwarePresent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 16),
    _WfFddiMacHardwarePresent_Type()
)
wfFddiMacHardwarePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacHardwarePresent.setStatus("mandatory")


class _WfFddiMacMaUnitDataEnable_Type(Integer32):
    """Custom type wfFddiMacMaUnitDataEnable based on Integer32"""
    defaultValue = 1

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


_WfFddiMacMaUnitDataEnable_Type.__name__ = "Integer32"
_WfFddiMacMaUnitDataEnable_Object = MibTableColumn
wfFddiMacMaUnitDataEnable = _WfFddiMacMaUnitDataEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 17),
    _WfFddiMacMaUnitDataEnable_Type()
)
wfFddiMacMaUnitDataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiMacMaUnitDataEnable.setStatus("mandatory")
_WfFddiMacTvxExpiredCts_Type = Counter32
_WfFddiMacTvxExpiredCts_Object = MibTableColumn
wfFddiMacTvxExpiredCts = _WfFddiMacTvxExpiredCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 18),
    _WfFddiMacTvxExpiredCts_Type()
)
wfFddiMacTvxExpiredCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacTvxExpiredCts.setStatus("mandatory")
_WfFddiMacLateCts_Type = Counter32
_WfFddiMacLateCts_Object = MibTableColumn
wfFddiMacLateCts = _WfFddiMacLateCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 19),
    _WfFddiMacLateCts_Type()
)
wfFddiMacLateCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacLateCts.setStatus("mandatory")
_WfFddiMacRingOpCts_Type = Counter32
_WfFddiMacRingOpCts_Object = MibTableColumn
wfFddiMacRingOpCts = _WfFddiMacRingOpCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 20),
    _WfFddiMacRingOpCts_Type()
)
wfFddiMacRingOpCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacRingOpCts.setStatus("mandatory")
_WfFddiMacDuplicateTokenCts_Type = Counter32
_WfFddiMacDuplicateTokenCts_Object = MibTableColumn
wfFddiMacDuplicateTokenCts = _WfFddiMacDuplicateTokenCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 2, 3, 1, 21),
    _WfFddiMacDuplicateTokenCts_Type()
)
wfFddiMacDuplicateTokenCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiMacDuplicateTokenCts.setStatus("mandatory")
_WfFddiPathGroup_ObjectIdentity = ObjectIdentity
wfFddiPathGroup = _WfFddiPathGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3)
)
_WfFddiPathTable_Object = MibTable
wfFddiPathTable = _WfFddiPathTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 2)
)
if mibBuilder.loadTexts:
    wfFddiPathTable.setStatus("mandatory")
_WfFddiPathEntry_Object = MibTableRow
wfFddiPathEntry = _WfFddiPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 2, 1)
)
wfFddiPathEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiPathSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPathNode"),
)
if mibBuilder.loadTexts:
    wfFddiPathEntry.setStatus("mandatory")
_WfFddiPathSlot_Type = Integer32
_WfFddiPathSlot_Object = MibTableColumn
wfFddiPathSlot = _WfFddiPathSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 2, 1, 1),
    _WfFddiPathSlot_Type()
)
wfFddiPathSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathSlot.setStatus("mandatory")
_WfFddiPathNode_Type = Integer32
_WfFddiPathNode_Object = MibTableColumn
wfFddiPathNode = _WfFddiPathNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 2, 1, 2),
    _WfFddiPathNode_Type()
)
wfFddiPathNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathNode.setStatus("mandatory")
_WfFddiPathCct_Type = Integer32
_WfFddiPathCct_Object = MibTableColumn
wfFddiPathCct = _WfFddiPathCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 2, 1, 3),
    _WfFddiPathCct_Type()
)
wfFddiPathCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathCct.setStatus("mandatory")
_WfFddiPathConfiguration_Type = OctetString
_WfFddiPathConfiguration_Object = MibTableColumn
wfFddiPathConfiguration = _WfFddiPathConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 2, 1, 4),
    _WfFddiPathConfiguration_Type()
)
wfFddiPathConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathConfiguration.setStatus("mandatory")
_WfFddiPathExtTable_Object = MibTable
wfFddiPathExtTable = _WfFddiPathExtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3)
)
if mibBuilder.loadTexts:
    wfFddiPathExtTable.setStatus("mandatory")
_WfFddiPathExtEntry_Object = MibTableRow
wfFddiPathExtEntry = _WfFddiPathExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1)
)
wfFddiPathExtEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiPathExtSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPathExtNode"),
)
if mibBuilder.loadTexts:
    wfFddiPathExtEntry.setStatus("mandatory")


class _WfFddiPathDelete_Type(Integer32):
    """Custom type wfFddiPathDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfFddiPathDelete_Type.__name__ = "Integer32"
_WfFddiPathDelete_Object = MibTableColumn
wfFddiPathDelete = _WfFddiPathDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1, 1),
    _WfFddiPathDelete_Type()
)
wfFddiPathDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPathDelete.setStatus("mandatory")
_WfFddiPathExtSlot_Type = Integer32
_WfFddiPathExtSlot_Object = MibTableColumn
wfFddiPathExtSlot = _WfFddiPathExtSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1, 2),
    _WfFddiPathExtSlot_Type()
)
wfFddiPathExtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathExtSlot.setStatus("mandatory")
_WfFddiPathExtNode_Type = Integer32
_WfFddiPathExtNode_Object = MibTableColumn
wfFddiPathExtNode = _WfFddiPathExtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1, 3),
    _WfFddiPathExtNode_Type()
)
wfFddiPathExtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathExtNode.setStatus("mandatory")
_WfFddiPathExtCct_Type = Integer32
_WfFddiPathExtCct_Object = MibTableColumn
wfFddiPathExtCct = _WfFddiPathExtCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1, 4),
    _WfFddiPathExtCct_Type()
)
wfFddiPathExtCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathExtCct.setStatus("mandatory")


class _WfFddiPathTvxLowerBound_Type(Integer32):
    """Custom type wfFddiPathTvxLowerBound based on Integer32"""
    defaultValue = 2500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2500000
        )
    )
    namedValues = NamedValues(
        ("default", 2500000)
    )


_WfFddiPathTvxLowerBound_Type.__name__ = "Integer32"
_WfFddiPathTvxLowerBound_Object = MibTableColumn
wfFddiPathTvxLowerBound = _WfFddiPathTvxLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1, 5),
    _WfFddiPathTvxLowerBound_Type()
)
wfFddiPathTvxLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPathTvxLowerBound.setStatus("mandatory")


class _WfFddiPathTMaxLowerBound_Type(Integer32):
    """Custom type wfFddiPathTMaxLowerBound based on Integer32"""
    defaultValue = 165000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            165000000
        )
    )
    namedValues = NamedValues(
        ("default", 165000000)
    )


_WfFddiPathTMaxLowerBound_Type.__name__ = "Integer32"
_WfFddiPathTMaxLowerBound_Object = MibTableColumn
wfFddiPathTMaxLowerBound = _WfFddiPathTMaxLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1, 6),
    _WfFddiPathTMaxLowerBound_Type()
)
wfFddiPathTMaxLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPathTMaxLowerBound.setStatus("mandatory")
_WfFddiPathMaxTReq_Type = Integer32
_WfFddiPathMaxTReq_Object = MibTableColumn
wfFddiPathMaxTReq = _WfFddiPathMaxTReq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 3, 3, 1, 7),
    _WfFddiPathMaxTReq_Type()
)
wfFddiPathMaxTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPathMaxTReq.setStatus("mandatory")
_WfFddiPortGroup_ObjectIdentity = ObjectIdentity
wfFddiPortGroup = _WfFddiPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4)
)
_WfFddiPortTable_Object = MibTable
wfFddiPortTable = _WfFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2)
)
if mibBuilder.loadTexts:
    wfFddiPortTable.setStatus("mandatory")
_WfFddiPortEntry_Object = MibTableRow
wfFddiPortEntry = _WfFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1)
)
wfFddiPortEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortNode"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortIndex"),
)
if mibBuilder.loadTexts:
    wfFddiPortEntry.setStatus("mandatory")
_WfFddiPortSlot_Type = Integer32
_WfFddiPortSlot_Object = MibTableColumn
wfFddiPortSlot = _WfFddiPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 1),
    _WfFddiPortSlot_Type()
)
wfFddiPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortSlot.setStatus("mandatory")
_WfFddiPortNode_Type = Integer32
_WfFddiPortNode_Object = MibTableColumn
wfFddiPortNode = _WfFddiPortNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 2),
    _WfFddiPortNode_Type()
)
wfFddiPortNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortNode.setStatus("mandatory")
_WfFddiPortCct_Type = Integer32
_WfFddiPortCct_Object = MibTableColumn
wfFddiPortCct = _WfFddiPortCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 3),
    _WfFddiPortCct_Type()
)
wfFddiPortCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortCct.setStatus("mandatory")
_WfFddiPortIndex_Type = Integer32
_WfFddiPortIndex_Object = MibTableColumn
wfFddiPortIndex = _WfFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 4),
    _WfFddiPortIndex_Type()
)
wfFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortIndex.setStatus("mandatory")


class _WfFddiPortPcType_Type(Integer32):
    """Custom type wfFddiPortPcType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("none", 5),
          ("s", 3))
    )


_WfFddiPortPcType_Type.__name__ = "Integer32"
_WfFddiPortPcType_Object = MibTableColumn
wfFddiPortPcType = _WfFddiPortPcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 5),
    _WfFddiPortPcType_Type()
)
wfFddiPortPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPcType.setStatus("mandatory")


class _WfFddiPortPcNeighbor_Type(Integer32):
    """Custom type wfFddiPortPcNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("s", 3),
          ("unknown", 5))
    )


_WfFddiPortPcNeighbor_Type.__name__ = "Integer32"
_WfFddiPortPcNeighbor_Object = MibTableColumn
wfFddiPortPcNeighbor = _WfFddiPortPcNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 6),
    _WfFddiPortPcNeighbor_Type()
)
wfFddiPortPcNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPcNeighbor.setStatus("mandatory")


class _WfFddiPortPcmState_Type(Integer32):
    """Custom type wfFddiPortPcmState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 9),
          ("break", 2),
          ("connect", 4),
          ("join", 7),
          ("maint", 10),
          ("next", 5),
          ("off", 1),
          ("signal", 6),
          ("trace", 3),
          ("verify", 8))
    )


_WfFddiPortPcmState_Type.__name__ = "Integer32"
_WfFddiPortPcmState_Object = MibTableColumn
wfFddiPortPcmState = _WfFddiPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 7),
    _WfFddiPortPcmState_Type()
)
wfFddiPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPcmState.setStatus("mandatory")
_WfFddiPortRequestedPaths_Type = Integer32
_WfFddiPortRequestedPaths_Object = MibTableColumn
wfFddiPortRequestedPaths = _WfFddiPortRequestedPaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 8),
    _WfFddiPortRequestedPaths_Type()
)
wfFddiPortRequestedPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortRequestedPaths.setStatus("mandatory")


class _WfFddiPortBsFlag_Type(Integer32):
    """Custom type wfFddiPortBsFlag based on Integer32"""
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


_WfFddiPortBsFlag_Type.__name__ = "Integer32"
_WfFddiPortBsFlag_Object = MibTableColumn
wfFddiPortBsFlag = _WfFddiPortBsFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 9),
    _WfFddiPortBsFlag_Type()
)
wfFddiPortBsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortBsFlag.setStatus("mandatory")


class _WfFddiPortLerFlag_Type(Integer32):
    """Custom type wfFddiPortLerFlag based on Integer32"""
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


_WfFddiPortLerFlag_Type.__name__ = "Integer32"
_WfFddiPortLerFlag_Object = MibTableColumn
wfFddiPortLerFlag = _WfFddiPortLerFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 10),
    _WfFddiPortLerFlag_Type()
)
wfFddiPortLerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortLerFlag.setStatus("mandatory")


class _WfFddiPortConnectState_Type(Integer32):
    """Custom type wfFddiPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3),
          ("unknown", 5))
    )


_WfFddiPortConnectState_Type.__name__ = "Integer32"
_WfFddiPortConnectState_Object = MibTableColumn
wfFddiPortConnectState = _WfFddiPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 11),
    _WfFddiPortConnectState_Type()
)
wfFddiPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortConnectState.setStatus("mandatory")


class _WfFddiPortMacIndicated_Type(Integer32):
    """Custom type wfFddiPortMacIndicated based on Integer32"""
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
        *(("ff", 1),
          ("ft", 2),
          ("tf", 3),
          ("tt", 4))
    )


_WfFddiPortMacIndicated_Type.__name__ = "Integer32"
_WfFddiPortMacIndicated_Object = MibTableColumn
wfFddiPortMacIndicated = _WfFddiPortMacIndicated_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 2, 1, 12),
    _WfFddiPortMacIndicated_Type()
)
wfFddiPortMacIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortMacIndicated.setStatus("mandatory")
_WfFddiPortExtTable_Object = MibTable
wfFddiPortExtTable = _WfFddiPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3)
)
if mibBuilder.loadTexts:
    wfFddiPortExtTable.setStatus("mandatory")
_WfFddiPortExtEntry_Object = MibTableRow
wfFddiPortExtEntry = _WfFddiPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1)
)
wfFddiPortExtEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortExtSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortExtNode"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortExtIndex"),
)
if mibBuilder.loadTexts:
    wfFddiPortExtEntry.setStatus("mandatory")


class _WfFddiPortDelete_Type(Integer32):
    """Custom type wfFddiPortDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfFddiPortDelete_Type.__name__ = "Integer32"
_WfFddiPortDelete_Object = MibTableColumn
wfFddiPortDelete = _WfFddiPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 1),
    _WfFddiPortDelete_Type()
)
wfFddiPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPortDelete.setStatus("mandatory")
_WfFddiPortExtSlot_Type = Integer32
_WfFddiPortExtSlot_Object = MibTableColumn
wfFddiPortExtSlot = _WfFddiPortExtSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 2),
    _WfFddiPortExtSlot_Type()
)
wfFddiPortExtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortExtSlot.setStatus("mandatory")
_WfFddiPortExtNode_Type = Integer32
_WfFddiPortExtNode_Object = MibTableColumn
wfFddiPortExtNode = _WfFddiPortExtNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 3),
    _WfFddiPortExtNode_Type()
)
wfFddiPortExtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortExtNode.setStatus("mandatory")
_WfFddiPortExtCct_Type = Integer32
_WfFddiPortExtCct_Object = MibTableColumn
wfFddiPortExtCct = _WfFddiPortExtCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 4),
    _WfFddiPortExtCct_Type()
)
wfFddiPortExtCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortExtCct.setStatus("mandatory")
_WfFddiPortExtIndex_Type = Integer32
_WfFddiPortExtIndex_Object = MibTableColumn
wfFddiPortExtIndex = _WfFddiPortExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 5),
    _WfFddiPortExtIndex_Type()
)
wfFddiPortExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortExtIndex.setStatus("mandatory")


class _WfFddiPortConnectionPolicies_Type(Integer32):
    """Custom type wfFddiPortConnectionPolicies based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maclct", 1),
          ("macloop", 2))
    )


_WfFddiPortConnectionPolicies_Type.__name__ = "Integer32"
_WfFddiPortConnectionPolicies_Object = MibTableColumn
wfFddiPortConnectionPolicies = _WfFddiPortConnectionPolicies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 6),
    _WfFddiPortConnectionPolicies_Type()
)
wfFddiPortConnectionPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortConnectionPolicies.setStatus("mandatory")


class _WfFddiPortCurrentPath_Type(Integer32):
    """Custom type wfFddiPortCurrentPath based on Integer32"""
    defaultValue = 1

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
        *(("concatenated", 5),
          ("isolated", 1),
          ("local", 2),
          ("primary", 4),
          ("secondary", 3),
          ("thru", 6))
    )


_WfFddiPortCurrentPath_Type.__name__ = "Integer32"
_WfFddiPortCurrentPath_Object = MibTableColumn
wfFddiPortCurrentPath = _WfFddiPortCurrentPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 7),
    _WfFddiPortCurrentPath_Type()
)
wfFddiPortCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortCurrentPath.setStatus("mandatory")
_WfFddiPortMacPlacement_Type = Integer32
_WfFddiPortMacPlacement_Object = MibTableColumn
wfFddiPortMacPlacement = _WfFddiPortMacPlacement_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 8),
    _WfFddiPortMacPlacement_Type()
)
wfFddiPortMacPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortMacPlacement.setStatus("mandatory")


class _WfFddiPortAvailablePaths_Type(Integer32):
    """Custom type wfFddiPortAvailablePaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l", 4),
          ("p", 1),
          ("s", 2))
    )


_WfFddiPortAvailablePaths_Type.__name__ = "Integer32"
_WfFddiPortAvailablePaths_Object = MibTableColumn
wfFddiPortAvailablePaths = _WfFddiPortAvailablePaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 9),
    _WfFddiPortAvailablePaths_Type()
)
wfFddiPortAvailablePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortAvailablePaths.setStatus("mandatory")


class _WfFddiPortPmdClass_Type(Integer32):
    """Custom type wfFddiPortPmdClass based on Integer32"""
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
        *(("fiber", 5),
          ("mode1", 2),
          ("mode2", 3),
          ("multimode", 1),
          ("sonet", 4),
          ("twistedpair", 6),
          ("unknown", 7),
          ("unspecified", 8))
    )


_WfFddiPortPmdClass_Type.__name__ = "Integer32"
_WfFddiPortPmdClass_Object = MibTableColumn
wfFddiPortPmdClass = _WfFddiPortPmdClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 10),
    _WfFddiPortPmdClass_Type()
)
wfFddiPortPmdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPmdClass.setStatus("mandatory")


class _WfFddiPortConnectionCapabilities_Type(Integer32):
    """Custom type wfFddiPortConnectionCapabilities based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maclct", 1),
          ("macloop", 2))
    )


_WfFddiPortConnectionCapabilities_Type.__name__ = "Integer32"
_WfFddiPortConnectionCapabilities_Object = MibTableColumn
wfFddiPortConnectionCapabilities = _WfFddiPortConnectionCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 11),
    _WfFddiPortConnectionCapabilities_Type()
)
wfFddiPortConnectionCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortConnectionCapabilities.setStatus("mandatory")
_WfFddiPortEbErrorCts_Type = Integer32
_WfFddiPortEbErrorCts_Object = MibTableColumn
wfFddiPortEbErrorCts = _WfFddiPortEbErrorCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 12),
    _WfFddiPortEbErrorCts_Type()
)
wfFddiPortEbErrorCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortEbErrorCts.setStatus("mandatory")
_WfFddiPortLctFailCts_Type = Counter32
_WfFddiPortLctFailCts_Object = MibTableColumn
wfFddiPortLctFailCts = _WfFddiPortLctFailCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 13),
    _WfFddiPortLctFailCts_Type()
)
wfFddiPortLctFailCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortLctFailCts.setStatus("mandatory")


class _WfFddiPortLerEstimate_Type(Integer32):
    """Custom type wfFddiPortLerEstimate based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_WfFddiPortLerEstimate_Type.__name__ = "Integer32"
_WfFddiPortLerEstimate_Object = MibTableColumn
wfFddiPortLerEstimate = _WfFddiPortLerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 14),
    _WfFddiPortLerEstimate_Type()
)
wfFddiPortLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortLerEstimate.setStatus("mandatory")
_WfFddiPortLemRejectCts_Type = Counter32
_WfFddiPortLemRejectCts_Object = MibTableColumn
wfFddiPortLemRejectCts = _WfFddiPortLemRejectCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 15),
    _WfFddiPortLemRejectCts_Type()
)
wfFddiPortLemRejectCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortLemRejectCts.setStatus("mandatory")
_WfFddiPortLemCts_Type = Counter32
_WfFddiPortLemCts_Object = MibTableColumn
wfFddiPortLemCts = _WfFddiPortLemCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 16),
    _WfFddiPortLemCts_Type()
)
wfFddiPortLemCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortLemCts.setStatus("mandatory")


class _WfFddiPortLerCutOff_Type(Integer32):
    """Custom type wfFddiPortLerCutOff based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_WfFddiPortLerCutOff_Type.__name__ = "Integer32"
_WfFddiPortLerCutOff_Object = MibTableColumn
wfFddiPortLerCutOff = _WfFddiPortLerCutOff_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 17),
    _WfFddiPortLerCutOff_Type()
)
wfFddiPortLerCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPortLerCutOff.setStatus("mandatory")


class _WfFddiPortLerAlarm_Type(Integer32):
    """Custom type wfFddiPortLerAlarm based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_WfFddiPortLerAlarm_Type.__name__ = "Integer32"
_WfFddiPortLerAlarm_Object = MibTableColumn
wfFddiPortLerAlarm = _WfFddiPortLerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 18),
    _WfFddiPortLerAlarm_Type()
)
wfFddiPortLerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPortLerAlarm.setStatus("mandatory")


class _WfFddiPortPcWithhold_Type(Integer32):
    """Custom type wfFddiPortPcWithhold based on Integer32"""
    defaultValue = 1

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
        *(("mtom", 2),
          ("none", 1),
          ("otherincompatible", 3),
          ("pathnotavailable", 4))
    )


_WfFddiPortPcWithhold_Type.__name__ = "Integer32"
_WfFddiPortPcWithhold_Object = MibTableColumn
wfFddiPortPcWithhold = _WfFddiPortPcWithhold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 19),
    _WfFddiPortPcWithhold_Type()
)
wfFddiPortPcWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortPcWithhold.setStatus("mandatory")


class _WfFddiPortHardwarePresent_Type(Integer32):
    """Custom type wfFddiPortHardwarePresent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("present", 2))
    )


_WfFddiPortHardwarePresent_Type.__name__ = "Integer32"
_WfFddiPortHardwarePresent_Object = MibTableColumn
wfFddiPortHardwarePresent = _WfFddiPortHardwarePresent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 3, 1, 20),
    _WfFddiPortHardwarePresent_Type()
)
wfFddiPortHardwarePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortHardwarePresent.setStatus("mandatory")
_WfFddiPortActionTable_Object = MibTable
wfFddiPortActionTable = _WfFddiPortActionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4)
)
if mibBuilder.loadTexts:
    wfFddiPortActionTable.setStatus("mandatory")
_WfFddiPortActionEntry_Object = MibTableRow
wfFddiPortActionEntry = _WfFddiPortActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4, 1)
)
wfFddiPortActionEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortActionSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortActionNode"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiPortActionIndex"),
)
if mibBuilder.loadTexts:
    wfFddiPortActionEntry.setStatus("mandatory")


class _WfFddiPortActionDelete_Type(Integer32):
    """Custom type wfFddiPortActionDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfFddiPortActionDelete_Type.__name__ = "Integer32"
_WfFddiPortActionDelete_Object = MibTableColumn
wfFddiPortActionDelete = _WfFddiPortActionDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4, 1, 1),
    _WfFddiPortActionDelete_Type()
)
wfFddiPortActionDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPortActionDelete.setStatus("mandatory")
_WfFddiPortActionSlot_Type = Integer32
_WfFddiPortActionSlot_Object = MibTableColumn
wfFddiPortActionSlot = _WfFddiPortActionSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4, 1, 2),
    _WfFddiPortActionSlot_Type()
)
wfFddiPortActionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortActionSlot.setStatus("mandatory")
_WfFddiPortActionNode_Type = Integer32
_WfFddiPortActionNode_Object = MibTableColumn
wfFddiPortActionNode = _WfFddiPortActionNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4, 1, 3),
    _WfFddiPortActionNode_Type()
)
wfFddiPortActionNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortActionNode.setStatus("mandatory")
_WfFddiPortActionCct_Type = Integer32
_WfFddiPortActionCct_Object = MibTableColumn
wfFddiPortActionCct = _WfFddiPortActionCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4, 1, 4),
    _WfFddiPortActionCct_Type()
)
wfFddiPortActionCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortActionCct.setStatus("mandatory")
_WfFddiPortActionIndex_Type = Integer32
_WfFddiPortActionIndex_Object = MibTableColumn
wfFddiPortActionIndex = _WfFddiPortActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4, 1, 5),
    _WfFddiPortActionIndex_Type()
)
wfFddiPortActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiPortActionIndex.setStatus("mandatory")


class _WfFddiPortAction_Type(Integer32):
    """Custom type wfFddiPortAction based on Integer32"""
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
        *(("disable", 4),
          ("enable", 3),
          ("maint", 2),
          ("other", 1),
          ("start", 5),
          ("stop", 6))
    )


_WfFddiPortAction_Type.__name__ = "Integer32"
_WfFddiPortAction_Object = MibTableColumn
wfFddiPortAction = _WfFddiPortAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 4, 4, 1, 6),
    _WfFddiPortAction_Type()
)
wfFddiPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiPortAction.setStatus("mandatory")
_WfFddiXGroup_ObjectIdentity = ObjectIdentity
wfFddiXGroup = _WfFddiXGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5)
)
_WfFddiXLineCfgTable_Object = MibTable
wfFddiXLineCfgTable = _WfFddiXLineCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1)
)
if mibBuilder.loadTexts:
    wfFddiXLineCfgTable.setStatus("mandatory")
_WfFddiXLineCfgEntry_Object = MibTableRow
wfFddiXLineCfgEntry = _WfFddiXLineCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1)
)
wfFddiXLineCfgEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiXLineCfgSlot"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiXLineCfgNode"),
)
if mibBuilder.loadTexts:
    wfFddiXLineCfgEntry.setStatus("mandatory")


class _WfFddiXLineCfgDelete_Type(Integer32):
    """Custom type wfFddiXLineCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfFddiXLineCfgDelete_Type.__name__ = "Integer32"
_WfFddiXLineCfgDelete_Object = MibTableColumn
wfFddiXLineCfgDelete = _WfFddiXLineCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 1),
    _WfFddiXLineCfgDelete_Type()
)
wfFddiXLineCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgDelete.setStatus("mandatory")


class _WfFddiXLineCfgEnable_Type(Integer32):
    """Custom type wfFddiXLineCfgEnable based on Integer32"""
    defaultValue = 1

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


_WfFddiXLineCfgEnable_Type.__name__ = "Integer32"
_WfFddiXLineCfgEnable_Object = MibTableColumn
wfFddiXLineCfgEnable = _WfFddiXLineCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 2),
    _WfFddiXLineCfgEnable_Type()
)
wfFddiXLineCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgEnable.setStatus("mandatory")


class _WfFddiXLineCfgLossOfServiceTmo_Type(Integer32):
    """Custom type wfFddiXLineCfgLossOfServiceTmo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFddiXLineCfgLossOfServiceTmo_Type.__name__ = "Integer32"
_WfFddiXLineCfgLossOfServiceTmo_Object = MibTableColumn
wfFddiXLineCfgLossOfServiceTmo = _WfFddiXLineCfgLossOfServiceTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 3),
    _WfFddiXLineCfgLossOfServiceTmo_Type()
)
wfFddiXLineCfgLossOfServiceTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgLossOfServiceTmo.setStatus("mandatory")


class _WfFddiXLineCfgSmtEnable_Type(Integer32):
    """Custom type wfFddiXLineCfgSmtEnable based on Integer32"""
    defaultValue = 1

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


_WfFddiXLineCfgSmtEnable_Type.__name__ = "Integer32"
_WfFddiXLineCfgSmtEnable_Object = MibTableColumn
wfFddiXLineCfgSmtEnable = _WfFddiXLineCfgSmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 4),
    _WfFddiXLineCfgSmtEnable_Type()
)
wfFddiXLineCfgSmtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgSmtEnable.setStatus("mandatory")


class _WfFddiXLineCfgSmtDatProtocol_Type(Integer32):
    """Custom type wfFddiXLineCfgSmtDatProtocol based on Integer32"""
    defaultValue = 1

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


_WfFddiXLineCfgSmtDatProtocol_Type.__name__ = "Integer32"
_WfFddiXLineCfgSmtDatProtocol_Object = MibTableColumn
wfFddiXLineCfgSmtDatProtocol = _WfFddiXLineCfgSmtDatProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 5),
    _WfFddiXLineCfgSmtDatProtocol_Type()
)
wfFddiXLineCfgSmtDatProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgSmtDatProtocol.setStatus("mandatory")
_WfFddiXLineCfgLineNumber_Type = Integer32
_WfFddiXLineCfgLineNumber_Object = MibTableColumn
wfFddiXLineCfgLineNumber = _WfFddiXLineCfgLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 6),
    _WfFddiXLineCfgLineNumber_Type()
)
wfFddiXLineCfgLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgLineNumber.setStatus("mandatory")


class _WfFddiXLineCfgForcePeerTree_Type(Integer32):
    """Custom type wfFddiXLineCfgForcePeerTree based on Integer32"""
    defaultValue = 2

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


_WfFddiXLineCfgForcePeerTree_Type.__name__ = "Integer32"
_WfFddiXLineCfgForcePeerTree_Object = MibTableColumn
wfFddiXLineCfgForcePeerTree = _WfFddiXLineCfgForcePeerTree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 7),
    _WfFddiXLineCfgForcePeerTree_Type()
)
wfFddiXLineCfgForcePeerTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgForcePeerTree.setStatus("mandatory")


class _WfFddiXLineCfgSlot_Type(Integer32):
    """Custom type wfFddiXLineCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfFddiXLineCfgSlot_Type.__name__ = "Integer32"
_WfFddiXLineCfgSlot_Object = MibTableColumn
wfFddiXLineCfgSlot = _WfFddiXLineCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 8),
    _WfFddiXLineCfgSlot_Type()
)
wfFddiXLineCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineCfgSlot.setStatus("mandatory")


class _WfFddiXLineCfgModule_Type(Integer32):
    """Custom type wfFddiXLineCfgModule based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfFddiXLineCfgModule_Type.__name__ = "Integer32"
_WfFddiXLineCfgModule_Object = MibTableColumn
wfFddiXLineCfgModule = _WfFddiXLineCfgModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 9),
    _WfFddiXLineCfgModule_Type()
)
wfFddiXLineCfgModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineCfgModule.setStatus("mandatory")


class _WfFddiXLineCfgActualNode_Type(Integer32):
    """Custom type wfFddiXLineCfgActualNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfFddiXLineCfgActualNode_Type.__name__ = "Integer32"
_WfFddiXLineCfgActualNode_Object = MibTableColumn
wfFddiXLineCfgActualNode = _WfFddiXLineCfgActualNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 10),
    _WfFddiXLineCfgActualNode_Type()
)
wfFddiXLineCfgActualNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineCfgActualNode.setStatus("mandatory")


class _WfFddiXLineCfgNode_Type(Integer32):
    """Custom type wfFddiXLineCfgNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfFddiXLineCfgNode_Type.__name__ = "Integer32"
_WfFddiXLineCfgNode_Object = MibTableColumn
wfFddiXLineCfgNode = _WfFddiXLineCfgNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 11),
    _WfFddiXLineCfgNode_Type()
)
wfFddiXLineCfgNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineCfgNode.setStatus("mandatory")
_WfFddiXLineCfgSmtIndex_Type = Integer32
_WfFddiXLineCfgSmtIndex_Object = MibTableColumn
wfFddiXLineCfgSmtIndex = _WfFddiXLineCfgSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 12),
    _WfFddiXLineCfgSmtIndex_Type()
)
wfFddiXLineCfgSmtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineCfgSmtIndex.setStatus("mandatory")
_WfFddiXLineCfgIfIndex_Type = Integer32
_WfFddiXLineCfgIfIndex_Object = MibTableColumn
wfFddiXLineCfgIfIndex = _WfFddiXLineCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 1, 1, 13),
    _WfFddiXLineCfgIfIndex_Type()
)
wfFddiXLineCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineCfgIfIndex.setStatus("mandatory")
_WfFddiXLineTable_Object = MibTable
wfFddiXLineTable = _WfFddiXLineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2)
)
if mibBuilder.loadTexts:
    wfFddiXLineTable.setStatus("mandatory")
_WfFddiXLineEntry_Object = MibTableRow
wfFddiXLineEntry = _WfFddiXLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1)
)
wfFddiXLineEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiXLineIfIndex"),
)
if mibBuilder.loadTexts:
    wfFddiXLineEntry.setStatus("mandatory")


class _WfFddiXLineSlot_Type(Integer32):
    """Custom type wfFddiXLineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfFddiXLineSlot_Type.__name__ = "Integer32"
_WfFddiXLineSlot_Object = MibTableColumn
wfFddiXLineSlot = _WfFddiXLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 1),
    _WfFddiXLineSlot_Type()
)
wfFddiXLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineSlot.setStatus("mandatory")


class _WfFddiXLineModule_Type(Integer32):
    """Custom type wfFddiXLineModule based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfFddiXLineModule_Type.__name__ = "Integer32"
_WfFddiXLineModule_Object = MibTableColumn
wfFddiXLineModule = _WfFddiXLineModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 2),
    _WfFddiXLineModule_Type()
)
wfFddiXLineModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineModule.setStatus("mandatory")


class _WfFddiXLineActualNode_Type(Integer32):
    """Custom type wfFddiXLineActualNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfFddiXLineActualNode_Type.__name__ = "Integer32"
_WfFddiXLineActualNode_Object = MibTableColumn
wfFddiXLineActualNode = _WfFddiXLineActualNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 3),
    _WfFddiXLineActualNode_Type()
)
wfFddiXLineActualNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineActualNode.setStatus("mandatory")


class _WfFddiXLineNode_Type(Integer32):
    """Custom type wfFddiXLineNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_WfFddiXLineNode_Type.__name__ = "Integer32"
_WfFddiXLineNode_Object = MibTableColumn
wfFddiXLineNode = _WfFddiXLineNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 4),
    _WfFddiXLineNode_Type()
)
wfFddiXLineNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineNode.setStatus("mandatory")
_WfFddiXLineSmtIndex_Type = Integer32
_WfFddiXLineSmtIndex_Object = MibTableColumn
wfFddiXLineSmtIndex = _WfFddiXLineSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 5),
    _WfFddiXLineSmtIndex_Type()
)
wfFddiXLineSmtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFddiXLineSmtIndex.setStatus("mandatory")
_WfFddiXLineIfIndex_Type = Integer32
_WfFddiXLineIfIndex_Object = MibTableColumn
wfFddiXLineIfIndex = _WfFddiXLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 6),
    _WfFddiXLineIfIndex_Type()
)
wfFddiXLineIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineIfIndex.setStatus("mandatory")
_WfFddiXLineTxErrors_Type = Counter32
_WfFddiXLineTxErrors_Object = MibTableColumn
wfFddiXLineTxErrors = _WfFddiXLineTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 7),
    _WfFddiXLineTxErrors_Type()
)
wfFddiXLineTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineTxErrors.setStatus("mandatory")
_WfFddiXLineTxAborts_Type = Counter32
_WfFddiXLineTxAborts_Object = MibTableColumn
wfFddiXLineTxAborts = _WfFddiXLineTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 8),
    _WfFddiXLineTxAborts_Type()
)
wfFddiXLineTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineTxAborts.setStatus("mandatory")
_WfFddiXLineTxOverruns_Type = Counter32
_WfFddiXLineTxOverruns_Object = MibTableColumn
wfFddiXLineTxOverruns = _WfFddiXLineTxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 9),
    _WfFddiXLineTxOverruns_Type()
)
wfFddiXLineTxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineTxOverruns.setStatus("mandatory")
_WfFddiXLineTxUnderruns_Type = Counter32
_WfFddiXLineTxUnderruns_Object = MibTableColumn
wfFddiXLineTxUnderruns = _WfFddiXLineTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 10),
    _WfFddiXLineTxUnderruns_Type()
)
wfFddiXLineTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineTxUnderruns.setStatus("mandatory")
_WfFddiXLineRxErrors_Type = Counter32
_WfFddiXLineRxErrors_Object = MibTableColumn
wfFddiXLineRxErrors = _WfFddiXLineRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 11),
    _WfFddiXLineRxErrors_Type()
)
wfFddiXLineRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxErrors.setStatus("mandatory")
_WfFddiXLineRxCrcErrors_Type = Counter32
_WfFddiXLineRxCrcErrors_Object = MibTableColumn
wfFddiXLineRxCrcErrors = _WfFddiXLineRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 12),
    _WfFddiXLineRxCrcErrors_Type()
)
wfFddiXLineRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxCrcErrors.setStatus("mandatory")
_WfFddiXLineRxSmtCrcErrors_Type = Counter32
_WfFddiXLineRxSmtCrcErrors_Object = MibTableColumn
wfFddiXLineRxSmtCrcErrors = _WfFddiXLineRxSmtCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 13),
    _WfFddiXLineRxSmtCrcErrors_Type()
)
wfFddiXLineRxSmtCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtCrcErrors.setStatus("mandatory")
_WfFddiXLineRxInvalidFrameStatusErrors_Type = Counter32
_WfFddiXLineRxInvalidFrameStatusErrors_Object = MibTableColumn
wfFddiXLineRxInvalidFrameStatusErrors = _WfFddiXLineRxInvalidFrameStatusErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 14),
    _WfFddiXLineRxInvalidFrameStatusErrors_Type()
)
wfFddiXLineRxInvalidFrameStatusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxInvalidFrameStatusErrors.setStatus("mandatory")
_WfFddiXLineRxSmtInvalidFrameStatusErrors_Type = Counter32
_WfFddiXLineRxSmtInvalidFrameStatusErrors_Object = MibTableColumn
wfFddiXLineRxSmtInvalidFrameStatusErrors = _WfFddiXLineRxSmtInvalidFrameStatusErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 15),
    _WfFddiXLineRxSmtInvalidFrameStatusErrors_Type()
)
wfFddiXLineRxSmtInvalidFrameStatusErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtInvalidFrameStatusErrors.setStatus("mandatory")
_WfFddiXLineRxMacErrors_Type = Counter32
_WfFddiXLineRxMacErrors_Object = MibTableColumn
wfFddiXLineRxMacErrors = _WfFddiXLineRxMacErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 16),
    _WfFddiXLineRxMacErrors_Type()
)
wfFddiXLineRxMacErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxMacErrors.setStatus("mandatory")
_WfFddiXLineRxSmtMacErrors_Type = Counter32
_WfFddiXLineRxSmtMacErrors_Object = MibTableColumn
wfFddiXLineRxSmtMacErrors = _WfFddiXLineRxSmtMacErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 17),
    _WfFddiXLineRxSmtMacErrors_Type()
)
wfFddiXLineRxSmtMacErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtMacErrors.setStatus("mandatory")
_WfFddiXLineRxFormatErrors_Type = Counter32
_WfFddiXLineRxFormatErrors_Object = MibTableColumn
wfFddiXLineRxFormatErrors = _WfFddiXLineRxFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 18),
    _WfFddiXLineRxFormatErrors_Type()
)
wfFddiXLineRxFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxFormatErrors.setStatus("mandatory")
_WfFddiXLineRxSmtFormatErrors_Type = Counter32
_WfFddiXLineRxSmtFormatErrors_Object = MibTableColumn
wfFddiXLineRxSmtFormatErrors = _WfFddiXLineRxSmtFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 19),
    _WfFddiXLineRxSmtFormatErrors_Type()
)
wfFddiXLineRxSmtFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtFormatErrors.setStatus("mandatory")
_WfFddiXLineRxFragmentErrors_Type = Counter32
_WfFddiXLineRxFragmentErrors_Object = MibTableColumn
wfFddiXLineRxFragmentErrors = _WfFddiXLineRxFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 20),
    _WfFddiXLineRxFragmentErrors_Type()
)
wfFddiXLineRxFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxFragmentErrors.setStatus("mandatory")
_WfFddiXLineRxSmtFragmentErrors_Type = Counter32
_WfFddiXLineRxSmtFragmentErrors_Object = MibTableColumn
wfFddiXLineRxSmtFragmentErrors = _WfFddiXLineRxSmtFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 21),
    _WfFddiXLineRxSmtFragmentErrors_Type()
)
wfFddiXLineRxSmtFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtFragmentErrors.setStatus("mandatory")
_WfFddiXLineRxInvalidLengthErrors_Type = Counter32
_WfFddiXLineRxInvalidLengthErrors_Object = MibTableColumn
wfFddiXLineRxInvalidLengthErrors = _WfFddiXLineRxInvalidLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 22),
    _WfFddiXLineRxInvalidLengthErrors_Type()
)
wfFddiXLineRxInvalidLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxInvalidLengthErrors.setStatus("mandatory")
_WfFddiXLineRxSmtInvalidLengthErrors_Type = Counter32
_WfFddiXLineRxSmtInvalidLengthErrors_Object = MibTableColumn
wfFddiXLineRxSmtInvalidLengthErrors = _WfFddiXLineRxSmtInvalidLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 23),
    _WfFddiXLineRxSmtInvalidLengthErrors_Type()
)
wfFddiXLineRxSmtInvalidLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtInvalidLengthErrors.setStatus("mandatory")
_WfFddiXLineRxAbortErrors_Type = Counter32
_WfFddiXLineRxAbortErrors_Object = MibTableColumn
wfFddiXLineRxAbortErrors = _WfFddiXLineRxAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 24),
    _WfFddiXLineRxAbortErrors_Type()
)
wfFddiXLineRxAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxAbortErrors.setStatus("mandatory")
_WfFddiXLineRxSmtAbortErrors_Type = Counter32
_WfFddiXLineRxSmtAbortErrors_Object = MibTableColumn
wfFddiXLineRxSmtAbortErrors = _WfFddiXLineRxSmtAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 25),
    _WfFddiXLineRxSmtAbortErrors_Type()
)
wfFddiXLineRxSmtAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtAbortErrors.setStatus("mandatory")
_WfFddiXLineRxEDataUnknownErrors_Type = Counter32
_WfFddiXLineRxEDataUnknownErrors_Object = MibTableColumn
wfFddiXLineRxEDataUnknownErrors = _WfFddiXLineRxEDataUnknownErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 26),
    _WfFddiXLineRxEDataUnknownErrors_Type()
)
wfFddiXLineRxEDataUnknownErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxEDataUnknownErrors.setStatus("mandatory")
_WfFddiXLineRxSmtEDataUnknownErrors_Type = Counter32
_WfFddiXLineRxSmtEDataUnknownErrors_Object = MibTableColumn
wfFddiXLineRxSmtEDataUnknownErrors = _WfFddiXLineRxSmtEDataUnknownErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 27),
    _WfFddiXLineRxSmtEDataUnknownErrors_Type()
)
wfFddiXLineRxSmtEDataUnknownErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtEDataUnknownErrors.setStatus("mandatory")
_WfFddiXLineRxLastEDataFStatusErrorVal_Type = Integer32
_WfFddiXLineRxLastEDataFStatusErrorVal_Object = MibTableColumn
wfFddiXLineRxLastEDataFStatusErrorVal = _WfFddiXLineRxLastEDataFStatusErrorVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 28),
    _WfFddiXLineRxLastEDataFStatusErrorVal_Type()
)
wfFddiXLineRxLastEDataFStatusErrorVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxLastEDataFStatusErrorVal.setStatus("mandatory")
_WfFddiXLineRxSmtLastEDataFStatusErrorVal_Type = Integer32
_WfFddiXLineRxSmtLastEDataFStatusErrorVal_Object = MibTableColumn
wfFddiXLineRxSmtLastEDataFStatusErrorVal = _WfFddiXLineRxSmtLastEDataFStatusErrorVal_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 29),
    _WfFddiXLineRxSmtLastEDataFStatusErrorVal_Type()
)
wfFddiXLineRxSmtLastEDataFStatusErrorVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtLastEDataFStatusErrorVal.setStatus("mandatory")
_WfFddiXLineRxOverruns_Type = Counter32
_WfFddiXLineRxOverruns_Object = MibTableColumn
wfFddiXLineRxOverruns = _WfFddiXLineRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 30),
    _WfFddiXLineRxOverruns_Type()
)
wfFddiXLineRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxOverruns.setStatus("mandatory")
_WfFddiXLineRxUnderruns_Type = Counter32
_WfFddiXLineRxUnderruns_Object = MibTableColumn
wfFddiXLineRxUnderruns = _WfFddiXLineRxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 31),
    _WfFddiXLineRxUnderruns_Type()
)
wfFddiXLineRxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxUnderruns.setStatus("mandatory")
_WfFddiXLineRxOversizedFrames_Type = Counter32
_WfFddiXLineRxOversizedFrames_Object = MibTableColumn
wfFddiXLineRxOversizedFrames = _WfFddiXLineRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 32),
    _WfFddiXLineRxOversizedFrames_Type()
)
wfFddiXLineRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxOversizedFrames.setStatus("mandatory")
_WfFddiXLineRxSmtOversizedFrames_Type = Counter32
_WfFddiXLineRxSmtOversizedFrames_Object = MibTableColumn
wfFddiXLineRxSmtOversizedFrames = _WfFddiXLineRxSmtOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 33),
    _WfFddiXLineRxSmtOversizedFrames_Type()
)
wfFddiXLineRxSmtOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtOversizedFrames.setStatus("mandatory")
_WfFddiXLineRxUndersizedFrames_Type = Counter32
_WfFddiXLineRxUndersizedFrames_Object = MibTableColumn
wfFddiXLineRxUndersizedFrames = _WfFddiXLineRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 34),
    _WfFddiXLineRxUndersizedFrames_Type()
)
wfFddiXLineRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxUndersizedFrames.setStatus("mandatory")
_WfFddiXLineRxSmtUndersizedFrames_Type = Counter32
_WfFddiXLineRxSmtUndersizedFrames_Object = MibTableColumn
wfFddiXLineRxSmtUndersizedFrames = _WfFddiXLineRxSmtUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 35),
    _WfFddiXLineRxSmtUndersizedFrames_Type()
)
wfFddiXLineRxSmtUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtUndersizedFrames.setStatus("mandatory")
_WfFddiXLineRxSmtSecondaryNsaFrames_Type = Counter32
_WfFddiXLineRxSmtSecondaryNsaFrames_Object = MibTableColumn
wfFddiXLineRxSmtSecondaryNsaFrames = _WfFddiXLineRxSmtSecondaryNsaFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 36),
    _WfFddiXLineRxSmtSecondaryNsaFrames_Type()
)
wfFddiXLineRxSmtSecondaryNsaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtSecondaryNsaFrames.setStatus("mandatory")
_WfFddiXLineUnexpectedFrames_Type = Counter32
_WfFddiXLineUnexpectedFrames_Object = MibTableColumn
wfFddiXLineUnexpectedFrames = _WfFddiXLineUnexpectedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 37),
    _WfFddiXLineUnexpectedFrames_Type()
)
wfFddiXLineUnexpectedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineUnexpectedFrames.setStatus("mandatory")
_WfFddiXLineRxSmtOctets_Type = Counter32
_WfFddiXLineRxSmtOctets_Object = MibTableColumn
wfFddiXLineRxSmtOctets = _WfFddiXLineRxSmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 38),
    _WfFddiXLineRxSmtOctets_Type()
)
wfFddiXLineRxSmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtOctets.setStatus("mandatory")
_WfFddiXLineRxSmtFrames_Type = Counter32
_WfFddiXLineRxSmtFrames_Object = MibTableColumn
wfFddiXLineRxSmtFrames = _WfFddiXLineRxSmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 39),
    _WfFddiXLineRxSmtFrames_Type()
)
wfFddiXLineRxSmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineRxSmtFrames.setStatus("mandatory")
_WfFddiXLineTxSmtOctets_Type = Counter32
_WfFddiXLineTxSmtOctets_Object = MibTableColumn
wfFddiXLineTxSmtOctets = _WfFddiXLineTxSmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 40),
    _WfFddiXLineTxSmtOctets_Type()
)
wfFddiXLineTxSmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineTxSmtOctets.setStatus("mandatory")
_WfFddiXLineTxSmtFrames_Type = Counter32
_WfFddiXLineTxSmtFrames_Object = MibTableColumn
wfFddiXLineTxSmtFrames = _WfFddiXLineTxSmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 41),
    _WfFddiXLineTxSmtFrames_Type()
)
wfFddiXLineTxSmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLineTxSmtFrames.setStatus("mandatory")
_WfFddiXLinePhyALogPtr_Type = Integer32
_WfFddiXLinePhyALogPtr_Object = MibTableColumn
wfFddiXLinePhyALogPtr = _WfFddiXLinePhyALogPtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 42),
    _WfFddiXLinePhyALogPtr_Type()
)
wfFddiXLinePhyALogPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLinePhyALogPtr.setStatus("mandatory")
_WfFddiXLinePhyBLogPtr_Type = Integer32
_WfFddiXLinePhyBLogPtr_Object = MibTableColumn
wfFddiXLinePhyBLogPtr = _WfFddiXLinePhyBLogPtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 2, 1, 43),
    _WfFddiXLinePhyBLogPtr_Type()
)
wfFddiXLinePhyBLogPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXLinePhyBLogPtr.setStatus("mandatory")
_WfFddiXSmtTable_Object = MibTable
wfFddiXSmtTable = _WfFddiXSmtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 3)
)
if mibBuilder.loadTexts:
    wfFddiXSmtTable.setStatus("mandatory")
_WfFddiXSmtEntry_Object = MibTableRow
wfFddiXSmtEntry = _WfFddiXSmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 3, 1)
)
wfFddiXSmtEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiXSmtIndex"),
)
if mibBuilder.loadTexts:
    wfFddiXSmtEntry.setStatus("mandatory")


class _WfFddiXSmtIndex_Type(Integer32):
    """Custom type wfFddiXSmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfFddiXSmtIndex_Type.__name__ = "Integer32"
_WfFddiXSmtIndex_Object = MibTableColumn
wfFddiXSmtIndex = _WfFddiXSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 3, 1, 1),
    _WfFddiXSmtIndex_Type()
)
wfFddiXSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXSmtIndex.setStatus("mandatory")
_WfFddiXSmtManufacturerData_Type = OctetString
_WfFddiXSmtManufacturerData_Object = MibTableColumn
wfFddiXSmtManufacturerData = _WfFddiXSmtManufacturerData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 3, 1, 2),
    _WfFddiXSmtManufacturerData_Type()
)
wfFddiXSmtManufacturerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXSmtManufacturerData.setStatus("mandatory")
_WfFddiXMacTable_Object = MibTable
wfFddiXMacTable = _WfFddiXMacTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 4)
)
if mibBuilder.loadTexts:
    wfFddiXMacTable.setStatus("mandatory")
_WfFddiXMacEntry_Object = MibTableRow
wfFddiXMacEntry = _WfFddiXMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 4, 1)
)
wfFddiXMacEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiXMacSmtIndex"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiXMacIndex"),
)
if mibBuilder.loadTexts:
    wfFddiXMacEntry.setStatus("mandatory")


class _WfFddiXMacSmtIndex_Type(Integer32):
    """Custom type wfFddiXMacSmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfFddiXMacSmtIndex_Type.__name__ = "Integer32"
_WfFddiXMacSmtIndex_Object = MibTableColumn
wfFddiXMacSmtIndex = _WfFddiXMacSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 4, 1, 1),
    _WfFddiXMacSmtIndex_Type()
)
wfFddiXMacSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXMacSmtIndex.setStatus("mandatory")


class _WfFddiXMacIndex_Type(Integer32):
    """Custom type wfFddiXMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfFddiXMacIndex_Type.__name__ = "Integer32"
_WfFddiXMacIndex_Object = MibTableColumn
wfFddiXMacIndex = _WfFddiXMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 4, 1, 2),
    _WfFddiXMacIndex_Type()
)
wfFddiXMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXMacIndex.setStatus("mandatory")


class _WfFddiXMacBridgeFunctions_Type(Integer32):
    """Custom type wfFddiXMacBridgeFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("srcroute", 2),
          ("srt", 4),
          ("transparent", 1))
    )


_WfFddiXMacBridgeFunctions_Type.__name__ = "Integer32"
_WfFddiXMacBridgeFunctions_Object = MibTableColumn
wfFddiXMacBridgeFunctions = _WfFddiXMacBridgeFunctions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 4, 1, 3),
    _WfFddiXMacBridgeFunctions_Type()
)
wfFddiXMacBridgeFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXMacBridgeFunctions.setStatus("mandatory")
_WfFddiXMacDuplicateTokenCts_Type = Counter32
_WfFddiXMacDuplicateTokenCts_Object = MibTableColumn
wfFddiXMacDuplicateTokenCts = _WfFddiXMacDuplicateTokenCts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 4, 1, 4),
    _WfFddiXMacDuplicateTokenCts_Type()
)
wfFddiXMacDuplicateTokenCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXMacDuplicateTokenCts.setStatus("mandatory")
_WfFddiXPortTable_Object = MibTable
wfFddiXPortTable = _WfFddiXPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 5)
)
if mibBuilder.loadTexts:
    wfFddiXPortTable.setStatus("mandatory")
_WfFddiXPortEntry_Object = MibTableRow
wfFddiXPortEntry = _WfFddiXPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 5, 1)
)
wfFddiXPortEntry.setIndexNames(
    (0, "Wellfleet-FDDI-MIB", "wfFddiXPortSmtIndex"),
    (0, "Wellfleet-FDDI-MIB", "wfFddiXPortIndex"),
)
if mibBuilder.loadTexts:
    wfFddiXPortEntry.setStatus("mandatory")


class _WfFddiXPortSmtIndex_Type(Integer32):
    """Custom type wfFddiXPortSmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfFddiXPortSmtIndex_Type.__name__ = "Integer32"
_WfFddiXPortSmtIndex_Object = MibTableColumn
wfFddiXPortSmtIndex = _WfFddiXPortSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 5, 1, 1),
    _WfFddiXPortSmtIndex_Type()
)
wfFddiXPortSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXPortSmtIndex.setStatus("mandatory")


class _WfFddiXPortIndex_Type(Integer32):
    """Custom type wfFddiXPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfFddiXPortIndex_Type.__name__ = "Integer32"
_WfFddiXPortIndex_Object = MibTableColumn
wfFddiXPortIndex = _WfFddiXPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 5, 1, 2),
    _WfFddiXPortIndex_Type()
)
wfFddiXPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXPortIndex.setStatus("mandatory")
_WfFddiXPortEbErrors_Type = Integer32
_WfFddiXPortEbErrors_Object = MibTableColumn
wfFddiXPortEbErrors = _WfFddiXPortEbErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 15, 5, 5, 1, 3),
    _WfFddiXPortEbErrors_Type()
)
wfFddiXPortEbErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFddiXPortEbErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-FDDI-MIB",
    **{"wfFddiTable": wfFddiTable,
       "wfFddiEntry": wfFddiEntry,
       "wfFDDIDelete": wfFDDIDelete,
       "wfFDDIEnable": wfFDDIEnable,
       "wfFDDIState": wfFDDIState,
       "wfFDDISlot": wfFDDISlot,
       "wfFDDINode": wfFDDINode,
       "wfFDDICct": wfFDDICct,
       "wfFDDIBofl": wfFDDIBofl,
       "wfFDDIBoflTmo": wfFDDIBoflTmo,
       "wfFDDIMtu": wfFDDIMtu,
       "wfFDDIMadr": wfFDDIMadr,
       "wfFDDIOctetsRxOk": wfFDDIOctetsRxOk,
       "wfFDDIFramesRxOk": wfFDDIFramesRxOk,
       "wfFDDIOctetsTxOk": wfFDDIOctetsTxOk,
       "wfFDDIFramesTxOk": wfFDDIFramesTxOk,
       "wfFDDICrcErrRx": wfFDDICrcErrRx,
       "wfFDDIOverrunRx": wfFDDIOverrunRx,
       "wfFDDIParityErrRx": wfFDDIParityErrRx,
       "wfFDDIMacErrRx": wfFDDIMacErrRx,
       "wfFDDIRingErrRx": wfFDDIRingErrRx,
       "wfFDDISmtRingErrRx": wfFDDISmtRingErrRx,
       "wfFDDIRingOverrunRx": wfFDDIRingOverrunRx,
       "wfFDDISmtRingOverrunRx": wfFDDISmtRingOverrunRx,
       "wfFDDIAbortTx": wfFDDIAbortTx,
       "wfFDDIUnderrunTx": wfFDDIUnderrunTx,
       "wfFDDIParityErrTx": wfFDDIParityErrTx,
       "wfFDDIRingErrTx": wfFDDIRingErrTx,
       "wfFDDIPortOpErr": wfFDDIPortOpErr,
       "wfFDDIInternOpErr": wfFDDIInternOpErr,
       "wfFDDIHostErr": wfFDDIHostErr,
       "wfFDDISmtConnectionPolicy": wfFDDISmtConnectionPolicy,
       "wfFDDISmtTNotify": wfFDDISmtTNotify,
       "wfFDDIMacTReq": wfFDDIMacTReq,
       "wfFDDIMacTMax": wfFDDIMacTMax,
       "wfFDDIMacTvxValue": wfFDDIMacTvxValue,
       "wfFDDIMacTMin": wfFDDIMacTMin,
       "wfFDDIHardwareFilter": wfFDDIHardwareFilter,
       "wfFDDISmtEnable": wfFDDISmtEnable,
       "wfFDDITxQueueLength": wfFDDITxQueueLength,
       "wfFDDIRxQueueLength": wfFDDIRxQueueLength,
       "wfFDDITxClipFrames": wfFDDITxClipFrames,
       "wfFDDIRxReplenMisses": wfFDDIRxReplenMisses,
       "wfFDDICfgTxQueueLength": wfFDDICfgTxQueueLength,
       "wfFDDICfgRxQueueLength": wfFDDICfgRxQueueLength,
       "wfFDDILineNumber": wfFDDILineNumber,
       "wfFDDIForcePeerTree": wfFDDIForcePeerTree,
       "wfFDDIInvalidFrameStatusRx": wfFDDIInvalidFrameStatusRx,
       "wfFDDIRxOversizedFrames": wfFDDIRxOversizedFrames,
       "wfFDDIRxSmtOversizedFrames": wfFDDIRxSmtOversizedFrames,
       "wfFDDIRxUndersizedFrames": wfFDDIRxUndersizedFrames,
       "wfFDDIRxSmtUndersizedFrames": wfFDDIRxSmtUndersizedFrames,
       "wfFDDIModule": wfFDDIModule,
       "wfFDDIActualNode": wfFDDIActualNode,
       "wfFDDILastChange": wfFDDILastChange,
       "wfFDDIOutQLen": wfFDDIOutQLen,
       "wfFDDIRxSmtOctets": wfFDDIRxSmtOctets,
       "wfFDDIRxSmtFrames": wfFDDIRxSmtFrames,
       "wfFDDIIntProcessings": wfFDDIIntProcessings,
       "wfFDDITxProcessings": wfFDDITxProcessings,
       "wfFDDIRxProcessings": wfFDDIRxProcessings,
       "wfFDDITxRNRProcessings": wfFDDITxRNRProcessings,
       "wfFDDISmtRxProcessings": wfFDDISmtRxProcessings,
       "wfFDDIPhyALogPtr": wfFDDIPhyALogPtr,
       "wfFDDIPhyBLogPtr": wfFDDIPhyBLogPtr,
       "wfFDDIPromiscuous": wfFDDIPromiscuous,
       "wfFDDILLCFrameControl": wfFDDILLCFrameControl,
       "wfFDDITurboBofl": wfFDDITurboBofl,
       "wfFDDIBoflNum": wfFDDIBoflNum,
       "wfFDDIBoflLen": wfFDDIBoflLen,
       "wfFddiSmtGroup": wfFddiSmtGroup,
       "wfFddiSmtTable": wfFddiSmtTable,
       "wfFddiSmtEntry": wfFddiSmtEntry,
       "wfFddiSmtSlot": wfFddiSmtSlot,
       "wfFddiSmtNode": wfFddiSmtNode,
       "wfFddiSmtCct": wfFddiSmtCct,
       "wfFddiSmtStationId": wfFddiSmtStationId,
       "wfFddiSmtOpVersionId": wfFddiSmtOpVersionId,
       "wfFddiSmtMacCt": wfFddiSmtMacCt,
       "wfFddiSmtNonMasterCt": wfFddiSmtNonMasterCt,
       "wfFddiSmtEcmState": wfFddiSmtEcmState,
       "wfFddiSmtCfState": wfFddiSmtCfState,
       "wfFddiSmtBypassPresent": wfFddiSmtBypassPresent,
       "wfFddiSmtRemoteDisconnectFlag": wfFddiSmtRemoteDisconnectFlag,
       "wfFddiSmtStationStatus": wfFddiSmtStationStatus,
       "wfFddiSmtPeerWrapFlag": wfFddiSmtPeerWrapFlag,
       "wfFddiSmtExtTable": wfFddiSmtExtTable,
       "wfFddiSmtExtEntry": wfFddiSmtExtEntry,
       "wfFddiSmtDelete": wfFddiSmtDelete,
       "wfFddiSmtExtSlot": wfFddiSmtExtSlot,
       "wfFddiSmtExtNode": wfFddiSmtExtNode,
       "wfFddiSmtExtCct": wfFddiSmtExtCct,
       "wfFddiSmtHiVersionId": wfFddiSmtHiVersionId,
       "wfFddiSmtLoVersionId": wfFddiSmtLoVersionId,
       "wfFddiSmtManufacturerData": wfFddiSmtManufacturerData,
       "wfFddiSmtUserData": wfFddiSmtUserData,
       "wfFddiSmtMibVersionId": wfFddiSmtMibVersionId,
       "wfFddiSmtMasterCts": wfFddiSmtMasterCts,
       "wfFddiSmtAvailablePaths": wfFddiSmtAvailablePaths,
       "wfFddiSmtConfigCapabilities": wfFddiSmtConfigCapabilities,
       "wfFddiSmtConfigPolicy": wfFddiSmtConfigPolicy,
       "wfFddiSmtStatRptPolicy": wfFddiSmtStatRptPolicy,
       "wfFddiSmtTraceMaxExpiration": wfFddiSmtTraceMaxExpiration,
       "wfFddiSmtTimeStamp": wfFddiSmtTimeStamp,
       "wfFddiSmtTransitionTimeStamp": wfFddiSmtTransitionTimeStamp,
       "wfFddiSmtDatProtocol": wfFddiSmtDatProtocol,
       "wfFddiSmtActionTable": wfFddiSmtActionTable,
       "wfFddiSmtActionEntry": wfFddiSmtActionEntry,
       "wfFddiSmtActionDelete": wfFddiSmtActionDelete,
       "wfFddiSmtActionSlot": wfFddiSmtActionSlot,
       "wfFddiSmtActionNode": wfFddiSmtActionNode,
       "wfFddiSmtActionCct": wfFddiSmtActionCct,
       "wfFddiSmtStationAction": wfFddiSmtStationAction,
       "wfFddiMacGroup": wfFddiMacGroup,
       "wfFddiMacTable": wfFddiMacTable,
       "wfFddiMacEntry": wfFddiMacEntry,
       "wfFddiMacSlot": wfFddiMacSlot,
       "wfFddiMacNode": wfFddiMacNode,
       "wfFddiMacCct": wfFddiMacCct,
       "wfFddiMacUpstreamNbr": wfFddiMacUpstreamNbr,
       "wfFddiMacDownstreamNbr": wfFddiMacDownstreamNbr,
       "wfFddiMacSmtAddress": wfFddiMacSmtAddress,
       "wfFddiMacTNeg": wfFddiMacTNeg,
       "wfFddiMacRmtState": wfFddiMacRmtState,
       "wfFddiMacOldUpstreamNbr": wfFddiMacOldUpstreamNbr,
       "wfFddiMacOldDownstreamNbr": wfFddiMacOldDownstreamNbr,
       "wfFddiMacTokenCts": wfFddiMacTokenCts,
       "wfFddiMacErrorCts": wfFddiMacErrorCts,
       "wfFddiMacLostCts": wfFddiMacLostCts,
       "wfFddiMacDaFlag": wfFddiMacDaFlag,
       "wfFddiMacUnaDaFlag": wfFddiMacUnaDaFlag,
       "wfFddiMacFrameErrorFlag": wfFddiMacFrameErrorFlag,
       "wfFddiMacMaUnitDataAvailable": wfFddiMacMaUnitDataAvailable,
       "wfFddiMacDownstreamPortType": wfFddiMacDownstreamPortType,
       "wfFddiMacExtTable": wfFddiMacExtTable,
       "wfFddiMacExtEntry": wfFddiMacExtEntry,
       "wfFddiMacDelete": wfFddiMacDelete,
       "wfFddiMacExtSlot": wfFddiMacExtSlot,
       "wfFddiMacExtNode": wfFddiMacExtNode,
       "wfFddiMacExtCct": wfFddiMacExtCct,
       "wfFddiMacFrameStatusFunctions": wfFddiMacFrameStatusFunctions,
       "wfFddiMacBridgeFunctions": wfFddiMacBridgeFunctions,
       "wfFddiMacTMaxCapability": wfFddiMacTMaxCapability,
       "wfFddiMacTvxCapability": wfFddiMacTvxCapability,
       "wfFddiMacAvailablePaths": wfFddiMacAvailablePaths,
       "wfFddiMacCurrentPath": wfFddiMacCurrentPath,
       "wfFddiMacDupAddrTest": wfFddiMacDupAddrTest,
       "wfFddiMacRequestedPaths": wfFddiMacRequestedPaths,
       "wfFddiMacCopiedCts": wfFddiMacCopiedCts,
       "wfFddiMacFrameErrorThreshold": wfFddiMacFrameErrorThreshold,
       "wfFddiMacFrameErrorRatio": wfFddiMacFrameErrorRatio,
       "wfFddiMacHardwarePresent": wfFddiMacHardwarePresent,
       "wfFddiMacMaUnitDataEnable": wfFddiMacMaUnitDataEnable,
       "wfFddiMacTvxExpiredCts": wfFddiMacTvxExpiredCts,
       "wfFddiMacLateCts": wfFddiMacLateCts,
       "wfFddiMacRingOpCts": wfFddiMacRingOpCts,
       "wfFddiMacDuplicateTokenCts": wfFddiMacDuplicateTokenCts,
       "wfFddiPathGroup": wfFddiPathGroup,
       "wfFddiPathTable": wfFddiPathTable,
       "wfFddiPathEntry": wfFddiPathEntry,
       "wfFddiPathSlot": wfFddiPathSlot,
       "wfFddiPathNode": wfFddiPathNode,
       "wfFddiPathCct": wfFddiPathCct,
       "wfFddiPathConfiguration": wfFddiPathConfiguration,
       "wfFddiPathExtTable": wfFddiPathExtTable,
       "wfFddiPathExtEntry": wfFddiPathExtEntry,
       "wfFddiPathDelete": wfFddiPathDelete,
       "wfFddiPathExtSlot": wfFddiPathExtSlot,
       "wfFddiPathExtNode": wfFddiPathExtNode,
       "wfFddiPathExtCct": wfFddiPathExtCct,
       "wfFddiPathTvxLowerBound": wfFddiPathTvxLowerBound,
       "wfFddiPathTMaxLowerBound": wfFddiPathTMaxLowerBound,
       "wfFddiPathMaxTReq": wfFddiPathMaxTReq,
       "wfFddiPortGroup": wfFddiPortGroup,
       "wfFddiPortTable": wfFddiPortTable,
       "wfFddiPortEntry": wfFddiPortEntry,
       "wfFddiPortSlot": wfFddiPortSlot,
       "wfFddiPortNode": wfFddiPortNode,
       "wfFddiPortCct": wfFddiPortCct,
       "wfFddiPortIndex": wfFddiPortIndex,
       "wfFddiPortPcType": wfFddiPortPcType,
       "wfFddiPortPcNeighbor": wfFddiPortPcNeighbor,
       "wfFddiPortPcmState": wfFddiPortPcmState,
       "wfFddiPortRequestedPaths": wfFddiPortRequestedPaths,
       "wfFddiPortBsFlag": wfFddiPortBsFlag,
       "wfFddiPortLerFlag": wfFddiPortLerFlag,
       "wfFddiPortConnectState": wfFddiPortConnectState,
       "wfFddiPortMacIndicated": wfFddiPortMacIndicated,
       "wfFddiPortExtTable": wfFddiPortExtTable,
       "wfFddiPortExtEntry": wfFddiPortExtEntry,
       "wfFddiPortDelete": wfFddiPortDelete,
       "wfFddiPortExtSlot": wfFddiPortExtSlot,
       "wfFddiPortExtNode": wfFddiPortExtNode,
       "wfFddiPortExtCct": wfFddiPortExtCct,
       "wfFddiPortExtIndex": wfFddiPortExtIndex,
       "wfFddiPortConnectionPolicies": wfFddiPortConnectionPolicies,
       "wfFddiPortCurrentPath": wfFddiPortCurrentPath,
       "wfFddiPortMacPlacement": wfFddiPortMacPlacement,
       "wfFddiPortAvailablePaths": wfFddiPortAvailablePaths,
       "wfFddiPortPmdClass": wfFddiPortPmdClass,
       "wfFddiPortConnectionCapabilities": wfFddiPortConnectionCapabilities,
       "wfFddiPortEbErrorCts": wfFddiPortEbErrorCts,
       "wfFddiPortLctFailCts": wfFddiPortLctFailCts,
       "wfFddiPortLerEstimate": wfFddiPortLerEstimate,
       "wfFddiPortLemRejectCts": wfFddiPortLemRejectCts,
       "wfFddiPortLemCts": wfFddiPortLemCts,
       "wfFddiPortLerCutOff": wfFddiPortLerCutOff,
       "wfFddiPortLerAlarm": wfFddiPortLerAlarm,
       "wfFddiPortPcWithhold": wfFddiPortPcWithhold,
       "wfFddiPortHardwarePresent": wfFddiPortHardwarePresent,
       "wfFddiPortActionTable": wfFddiPortActionTable,
       "wfFddiPortActionEntry": wfFddiPortActionEntry,
       "wfFddiPortActionDelete": wfFddiPortActionDelete,
       "wfFddiPortActionSlot": wfFddiPortActionSlot,
       "wfFddiPortActionNode": wfFddiPortActionNode,
       "wfFddiPortActionCct": wfFddiPortActionCct,
       "wfFddiPortActionIndex": wfFddiPortActionIndex,
       "wfFddiPortAction": wfFddiPortAction,
       "wfFddiXGroup": wfFddiXGroup,
       "wfFddiXLineCfgTable": wfFddiXLineCfgTable,
       "wfFddiXLineCfgEntry": wfFddiXLineCfgEntry,
       "wfFddiXLineCfgDelete": wfFddiXLineCfgDelete,
       "wfFddiXLineCfgEnable": wfFddiXLineCfgEnable,
       "wfFddiXLineCfgLossOfServiceTmo": wfFddiXLineCfgLossOfServiceTmo,
       "wfFddiXLineCfgSmtEnable": wfFddiXLineCfgSmtEnable,
       "wfFddiXLineCfgSmtDatProtocol": wfFddiXLineCfgSmtDatProtocol,
       "wfFddiXLineCfgLineNumber": wfFddiXLineCfgLineNumber,
       "wfFddiXLineCfgForcePeerTree": wfFddiXLineCfgForcePeerTree,
       "wfFddiXLineCfgSlot": wfFddiXLineCfgSlot,
       "wfFddiXLineCfgModule": wfFddiXLineCfgModule,
       "wfFddiXLineCfgActualNode": wfFddiXLineCfgActualNode,
       "wfFddiXLineCfgNode": wfFddiXLineCfgNode,
       "wfFddiXLineCfgSmtIndex": wfFddiXLineCfgSmtIndex,
       "wfFddiXLineCfgIfIndex": wfFddiXLineCfgIfIndex,
       "wfFddiXLineTable": wfFddiXLineTable,
       "wfFddiXLineEntry": wfFddiXLineEntry,
       "wfFddiXLineSlot": wfFddiXLineSlot,
       "wfFddiXLineModule": wfFddiXLineModule,
       "wfFddiXLineActualNode": wfFddiXLineActualNode,
       "wfFddiXLineNode": wfFddiXLineNode,
       "wfFddiXLineSmtIndex": wfFddiXLineSmtIndex,
       "wfFddiXLineIfIndex": wfFddiXLineIfIndex,
       "wfFddiXLineTxErrors": wfFddiXLineTxErrors,
       "wfFddiXLineTxAborts": wfFddiXLineTxAborts,
       "wfFddiXLineTxOverruns": wfFddiXLineTxOverruns,
       "wfFddiXLineTxUnderruns": wfFddiXLineTxUnderruns,
       "wfFddiXLineRxErrors": wfFddiXLineRxErrors,
       "wfFddiXLineRxCrcErrors": wfFddiXLineRxCrcErrors,
       "wfFddiXLineRxSmtCrcErrors": wfFddiXLineRxSmtCrcErrors,
       "wfFddiXLineRxInvalidFrameStatusErrors": wfFddiXLineRxInvalidFrameStatusErrors,
       "wfFddiXLineRxSmtInvalidFrameStatusErrors": wfFddiXLineRxSmtInvalidFrameStatusErrors,
       "wfFddiXLineRxMacErrors": wfFddiXLineRxMacErrors,
       "wfFddiXLineRxSmtMacErrors": wfFddiXLineRxSmtMacErrors,
       "wfFddiXLineRxFormatErrors": wfFddiXLineRxFormatErrors,
       "wfFddiXLineRxSmtFormatErrors": wfFddiXLineRxSmtFormatErrors,
       "wfFddiXLineRxFragmentErrors": wfFddiXLineRxFragmentErrors,
       "wfFddiXLineRxSmtFragmentErrors": wfFddiXLineRxSmtFragmentErrors,
       "wfFddiXLineRxInvalidLengthErrors": wfFddiXLineRxInvalidLengthErrors,
       "wfFddiXLineRxSmtInvalidLengthErrors": wfFddiXLineRxSmtInvalidLengthErrors,
       "wfFddiXLineRxAbortErrors": wfFddiXLineRxAbortErrors,
       "wfFddiXLineRxSmtAbortErrors": wfFddiXLineRxSmtAbortErrors,
       "wfFddiXLineRxEDataUnknownErrors": wfFddiXLineRxEDataUnknownErrors,
       "wfFddiXLineRxSmtEDataUnknownErrors": wfFddiXLineRxSmtEDataUnknownErrors,
       "wfFddiXLineRxLastEDataFStatusErrorVal": wfFddiXLineRxLastEDataFStatusErrorVal,
       "wfFddiXLineRxSmtLastEDataFStatusErrorVal": wfFddiXLineRxSmtLastEDataFStatusErrorVal,
       "wfFddiXLineRxOverruns": wfFddiXLineRxOverruns,
       "wfFddiXLineRxUnderruns": wfFddiXLineRxUnderruns,
       "wfFddiXLineRxOversizedFrames": wfFddiXLineRxOversizedFrames,
       "wfFddiXLineRxSmtOversizedFrames": wfFddiXLineRxSmtOversizedFrames,
       "wfFddiXLineRxUndersizedFrames": wfFddiXLineRxUndersizedFrames,
       "wfFddiXLineRxSmtUndersizedFrames": wfFddiXLineRxSmtUndersizedFrames,
       "wfFddiXLineRxSmtSecondaryNsaFrames": wfFddiXLineRxSmtSecondaryNsaFrames,
       "wfFddiXLineUnexpectedFrames": wfFddiXLineUnexpectedFrames,
       "wfFddiXLineRxSmtOctets": wfFddiXLineRxSmtOctets,
       "wfFddiXLineRxSmtFrames": wfFddiXLineRxSmtFrames,
       "wfFddiXLineTxSmtOctets": wfFddiXLineTxSmtOctets,
       "wfFddiXLineTxSmtFrames": wfFddiXLineTxSmtFrames,
       "wfFddiXLinePhyALogPtr": wfFddiXLinePhyALogPtr,
       "wfFddiXLinePhyBLogPtr": wfFddiXLinePhyBLogPtr,
       "wfFddiXSmtTable": wfFddiXSmtTable,
       "wfFddiXSmtEntry": wfFddiXSmtEntry,
       "wfFddiXSmtIndex": wfFddiXSmtIndex,
       "wfFddiXSmtManufacturerData": wfFddiXSmtManufacturerData,
       "wfFddiXMacTable": wfFddiXMacTable,
       "wfFddiXMacEntry": wfFddiXMacEntry,
       "wfFddiXMacSmtIndex": wfFddiXMacSmtIndex,
       "wfFddiXMacIndex": wfFddiXMacIndex,
       "wfFddiXMacBridgeFunctions": wfFddiXMacBridgeFunctions,
       "wfFddiXMacDuplicateTokenCts": wfFddiXMacDuplicateTokenCts,
       "wfFddiXPortTable": wfFddiXPortTable,
       "wfFddiXPortEntry": wfFddiXPortEntry,
       "wfFddiXPortSmtIndex": wfFddiXPortSmtIndex,
       "wfFddiXPortIndex": wfFddiXPortIndex,
       "wfFddiXPortEbErrors": wfFddiXPortEbErrors}
)
