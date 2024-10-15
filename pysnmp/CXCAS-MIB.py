# SNMP MIB module (CXCAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXCAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:10 2024
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

(cxCAS,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxCAS")

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

_Dsx1ExtAbcdTxSignalingTable_Object = MibTable
dsx1ExtAbcdTxSignalingTable = _Dsx1ExtAbcdTxSignalingTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10)
)
if mibBuilder.loadTexts:
    dsx1ExtAbcdTxSignalingTable.setStatus("mandatory")
_Dsx1ExtAbcdTxSignalingEntry_Object = MibTableRow
dsx1ExtAbcdTxSignalingEntry = _Dsx1ExtAbcdTxSignalingEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1)
)
dsx1ExtAbcdTxSignalingEntry.setIndexNames(
    (0, "CXCAS-MIB", "dsx1ExtAbcdTxSignalingTypeIndex"),
)
if mibBuilder.loadTexts:
    dsx1ExtAbcdTxSignalingEntry.setStatus("mandatory")


class _Dsx1ExtAbcdTxSignalingTypeIndex_Type(Integer32):
    """Custom type dsx1ExtAbcdTxSignalingTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Dsx1ExtAbcdTxSignalingTypeIndex_Type.__name__ = "Integer32"
_Dsx1ExtAbcdTxSignalingTypeIndex_Object = MibTableColumn
dsx1ExtAbcdTxSignalingTypeIndex = _Dsx1ExtAbcdTxSignalingTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 1),
    _Dsx1ExtAbcdTxSignalingTypeIndex_Type()
)
dsx1ExtAbcdTxSignalingTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtAbcdTxSignalingTypeIndex.setStatus("mandatory")


class _Dsx1ExtAbcdEmOnHook_Type(Integer32):
    """Custom type dsx1ExtAbcdEmOnHook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdEmOnHook_Type.__name__ = "Integer32"
_Dsx1ExtAbcdEmOnHook_Object = MibTableColumn
dsx1ExtAbcdEmOnHook = _Dsx1ExtAbcdEmOnHook_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 10),
    _Dsx1ExtAbcdEmOnHook_Type()
)
dsx1ExtAbcdEmOnHook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdEmOnHook.setStatus("mandatory")


class _Dsx1ExtAbcdEmOffHook_Type(Integer32):
    """Custom type dsx1ExtAbcdEmOffHook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdEmOffHook_Type.__name__ = "Integer32"
_Dsx1ExtAbcdEmOffHook_Object = MibTableColumn
dsx1ExtAbcdEmOffHook = _Dsx1ExtAbcdEmOffHook_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 11),
    _Dsx1ExtAbcdEmOffHook_Type()
)
dsx1ExtAbcdEmOffHook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdEmOffHook.setStatus("mandatory")


class _Dsx1ExtAbcdEmSeizeAck_Type(Integer32):
    """Custom type dsx1ExtAbcdEmSeizeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdEmSeizeAck_Type.__name__ = "Integer32"
_Dsx1ExtAbcdEmSeizeAck_Object = MibTableColumn
dsx1ExtAbcdEmSeizeAck = _Dsx1ExtAbcdEmSeizeAck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 12),
    _Dsx1ExtAbcdEmSeizeAck_Type()
)
dsx1ExtAbcdEmSeizeAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdEmSeizeAck.setStatus("mandatory")


class _Dsx1ExtAbcdEmClearForward_Type(Integer32):
    """Custom type dsx1ExtAbcdEmClearForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdEmClearForward_Type.__name__ = "Integer32"
_Dsx1ExtAbcdEmClearForward_Object = MibTableColumn
dsx1ExtAbcdEmClearForward = _Dsx1ExtAbcdEmClearForward_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 13),
    _Dsx1ExtAbcdEmClearForward_Type()
)
dsx1ExtAbcdEmClearForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdEmClearForward.setStatus("mandatory")


class _Dsx1ExtAbcdEmClearBackward_Type(Integer32):
    """Custom type dsx1ExtAbcdEmClearBackward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdEmClearBackward_Type.__name__ = "Integer32"
_Dsx1ExtAbcdEmClearBackward_Object = MibTableColumn
dsx1ExtAbcdEmClearBackward = _Dsx1ExtAbcdEmClearBackward_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 14),
    _Dsx1ExtAbcdEmClearBackward_Type()
)
dsx1ExtAbcdEmClearBackward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdEmClearBackward.setStatus("mandatory")


class _Dsx1ExtAbcdFxLo_Type(Integer32):
    """Custom type dsx1ExtAbcdFxLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdFxLo_Type.__name__ = "Integer32"
_Dsx1ExtAbcdFxLo_Object = MibTableColumn
dsx1ExtAbcdFxLo = _Dsx1ExtAbcdFxLo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 15),
    _Dsx1ExtAbcdFxLo_Type()
)
dsx1ExtAbcdFxLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdFxLo.setStatus("mandatory")


class _Dsx1ExtAbcdFxLc_Type(Integer32):
    """Custom type dsx1ExtAbcdFxLc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdFxLc_Type.__name__ = "Integer32"
_Dsx1ExtAbcdFxLc_Object = MibTableColumn
dsx1ExtAbcdFxLc = _Dsx1ExtAbcdFxLc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 16),
    _Dsx1ExtAbcdFxLc_Type()
)
dsx1ExtAbcdFxLc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdFxLc.setStatus("mandatory")


class _Dsx1ExtAbcdFxRingingOn_Type(Integer32):
    """Custom type dsx1ExtAbcdFxRingingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdFxRingingOn_Type.__name__ = "Integer32"
_Dsx1ExtAbcdFxRingingOn_Object = MibTableColumn
dsx1ExtAbcdFxRingingOn = _Dsx1ExtAbcdFxRingingOn_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 17),
    _Dsx1ExtAbcdFxRingingOn_Type()
)
dsx1ExtAbcdFxRingingOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdFxRingingOn.setStatus("mandatory")


class _Dsx1ExtAbcdFxLcf_Type(Integer32):
    """Custom type dsx1ExtAbcdFxLcf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdFxLcf_Type.__name__ = "Integer32"
_Dsx1ExtAbcdFxLcf_Object = MibTableColumn
dsx1ExtAbcdFxLcf = _Dsx1ExtAbcdFxLcf_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 18),
    _Dsx1ExtAbcdFxLcf_Type()
)
dsx1ExtAbcdFxLcf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdFxLcf.setStatus("mandatory")


class _Dsx1ExtAbcdFxLcfo_Type(Integer32):
    """Custom type dsx1ExtAbcdFxLcfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdFxLcfo_Type.__name__ = "Integer32"
_Dsx1ExtAbcdFxLcfo_Object = MibTableColumn
dsx1ExtAbcdFxLcfo = _Dsx1ExtAbcdFxLcfo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 19),
    _Dsx1ExtAbcdFxLcfo_Type()
)
dsx1ExtAbcdFxLcfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdFxLcfo.setStatus("mandatory")


class _Dsx1ExtAbcdFxRingingOff_Type(Integer32):
    """Custom type dsx1ExtAbcdFxRingingOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdFxRingingOff_Type.__name__ = "Integer32"
_Dsx1ExtAbcdFxRingingOff_Object = MibTableColumn
dsx1ExtAbcdFxRingingOff = _Dsx1ExtAbcdFxRingingOff_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 20),
    _Dsx1ExtAbcdFxRingingOff_Type()
)
dsx1ExtAbcdFxRingingOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdFxRingingOff.setStatus("mandatory")


class _Dsx1ExtAbcdAnswer_Type(Integer32):
    """Custom type dsx1ExtAbcdAnswer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdAnswer_Type.__name__ = "Integer32"
_Dsx1ExtAbcdAnswer_Object = MibTableColumn
dsx1ExtAbcdAnswer = _Dsx1ExtAbcdAnswer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 21),
    _Dsx1ExtAbcdAnswer_Type()
)
dsx1ExtAbcdAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdAnswer.setStatus("mandatory")


class _Dsx1ExtAbcdBusyOut_Type(Integer32):
    """Custom type dsx1ExtAbcdBusyOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdBusyOut_Type.__name__ = "Integer32"
_Dsx1ExtAbcdBusyOut_Object = MibTableColumn
dsx1ExtAbcdBusyOut = _Dsx1ExtAbcdBusyOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 22),
    _Dsx1ExtAbcdBusyOut_Type()
)
dsx1ExtAbcdBusyOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdBusyOut.setStatus("mandatory")


class _Dsx1ExtAbcdFaultyLink_Type(Integer32):
    """Custom type dsx1ExtAbcdFaultyLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx1ExtAbcdFaultyLink_Type.__name__ = "Integer32"
_Dsx1ExtAbcdFaultyLink_Object = MibTableColumn
dsx1ExtAbcdFaultyLink = _Dsx1ExtAbcdFaultyLink_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 10, 1, 23),
    _Dsx1ExtAbcdFaultyLink_Type()
)
dsx1ExtAbcdFaultyLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdFaultyLink.setStatus("mandatory")
_Dsx1ExtAbcdRxSignalingTable_Object = MibTable
dsx1ExtAbcdRxSignalingTable = _Dsx1ExtAbcdRxSignalingTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20)
)
if mibBuilder.loadTexts:
    dsx1ExtAbcdRxSignalingTable.setStatus("mandatory")
_Dsx1ExtAbcdRxSignalingEntry_Object = MibTableRow
dsx1ExtAbcdRxSignalingEntry = _Dsx1ExtAbcdRxSignalingEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1)
)
dsx1ExtAbcdRxSignalingEntry.setIndexNames(
    (0, "CXCAS-MIB", "dsx1ExtAbcdRxSignalingTypeIndex"),
    (0, "CXCAS-MIB", "dsx1ExtAbcdRxSignalingAbcdValue"),
)
if mibBuilder.loadTexts:
    dsx1ExtAbcdRxSignalingEntry.setStatus("mandatory")


class _Dsx1ExtAbcdRxSignalingTypeIndex_Type(Integer32):
    """Custom type dsx1ExtAbcdRxSignalingTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Dsx1ExtAbcdRxSignalingTypeIndex_Type.__name__ = "Integer32"
_Dsx1ExtAbcdRxSignalingTypeIndex_Object = MibTableColumn
dsx1ExtAbcdRxSignalingTypeIndex = _Dsx1ExtAbcdRxSignalingTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1, 1),
    _Dsx1ExtAbcdRxSignalingTypeIndex_Type()
)
dsx1ExtAbcdRxSignalingTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtAbcdRxSignalingTypeIndex.setStatus("mandatory")


class _Dsx1ExtAbcdRxSignalingAbcdValue_Type(Integer32):
    """Custom type dsx1ExtAbcdRxSignalingAbcdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Dsx1ExtAbcdRxSignalingAbcdValue_Type.__name__ = "Integer32"
_Dsx1ExtAbcdRxSignalingAbcdValue_Object = MibTableColumn
dsx1ExtAbcdRxSignalingAbcdValue = _Dsx1ExtAbcdRxSignalingAbcdValue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1, 2),
    _Dsx1ExtAbcdRxSignalingAbcdValue_Type()
)
dsx1ExtAbcdRxSignalingAbcdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtAbcdRxSignalingAbcdValue.setStatus("mandatory")


class _Dsx1ExtAbcdValue_Type(Integer32):
    """Custom type dsx1ExtAbcdValue based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("answer", 6),
          ("busy-out", 8),
          ("faulty-link", 9),
          ("lcf", 4),
          ("lcfo", 5),
          ("off-hook", 2),
          ("on-hook", 1),
          ("proceed", 11),
          ("ring-off", 7),
          ("ring-on", 3),
          ("seize", 10))
    )


_Dsx1ExtAbcdValue_Type.__name__ = "Integer32"
_Dsx1ExtAbcdValue_Object = MibTableColumn
dsx1ExtAbcdValue = _Dsx1ExtAbcdValue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 59, 20, 1, 10),
    _Dsx1ExtAbcdValue_Type()
)
dsx1ExtAbcdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtAbcdValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXCAS-MIB",
    **{"dsx1ExtAbcdTxSignalingTable": dsx1ExtAbcdTxSignalingTable,
       "dsx1ExtAbcdTxSignalingEntry": dsx1ExtAbcdTxSignalingEntry,
       "dsx1ExtAbcdTxSignalingTypeIndex": dsx1ExtAbcdTxSignalingTypeIndex,
       "dsx1ExtAbcdEmOnHook": dsx1ExtAbcdEmOnHook,
       "dsx1ExtAbcdEmOffHook": dsx1ExtAbcdEmOffHook,
       "dsx1ExtAbcdEmSeizeAck": dsx1ExtAbcdEmSeizeAck,
       "dsx1ExtAbcdEmClearForward": dsx1ExtAbcdEmClearForward,
       "dsx1ExtAbcdEmClearBackward": dsx1ExtAbcdEmClearBackward,
       "dsx1ExtAbcdFxLo": dsx1ExtAbcdFxLo,
       "dsx1ExtAbcdFxLc": dsx1ExtAbcdFxLc,
       "dsx1ExtAbcdFxRingingOn": dsx1ExtAbcdFxRingingOn,
       "dsx1ExtAbcdFxLcf": dsx1ExtAbcdFxLcf,
       "dsx1ExtAbcdFxLcfo": dsx1ExtAbcdFxLcfo,
       "dsx1ExtAbcdFxRingingOff": dsx1ExtAbcdFxRingingOff,
       "dsx1ExtAbcdAnswer": dsx1ExtAbcdAnswer,
       "dsx1ExtAbcdBusyOut": dsx1ExtAbcdBusyOut,
       "dsx1ExtAbcdFaultyLink": dsx1ExtAbcdFaultyLink,
       "dsx1ExtAbcdRxSignalingTable": dsx1ExtAbcdRxSignalingTable,
       "dsx1ExtAbcdRxSignalingEntry": dsx1ExtAbcdRxSignalingEntry,
       "dsx1ExtAbcdRxSignalingTypeIndex": dsx1ExtAbcdRxSignalingTypeIndex,
       "dsx1ExtAbcdRxSignalingAbcdValue": dsx1ExtAbcdRxSignalingAbcdValue,
       "dsx1ExtAbcdValue": dsx1ExtAbcdValue}
)
