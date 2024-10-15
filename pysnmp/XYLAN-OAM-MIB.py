# SNMP MIB module (XYLAN-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:10 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanOamArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanOamArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanOam_ObjectIdentity = ObjectIdentity
xylanOam = _XylanOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1)
)
_XylanOamF4VPTable_Object = MibTable
xylanOamF4VPTable = _XylanOamF4VPTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1)
)
if mibBuilder.loadTexts:
    xylanOamF4VPTable.setStatus("mandatory")
_XylanOamF4VPEntry_Object = MibTableRow
xylanOamF4VPEntry = _XylanOamF4VPEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1)
)
xylanOamF4VPEntry.setIndexNames(
    (0, "XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"),
    (0, "XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"),
    (0, "XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"),
)
if mibBuilder.loadTexts:
    xylanOamF4VPEntry.setStatus("mandatory")


class _XylanOamF4VPSlotIndex_Type(Integer32):
    """Custom type xylanOamF4VPSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylanOamF4VPSlotIndex_Type.__name__ = "Integer32"
_XylanOamF4VPSlotIndex_Object = MibTableColumn
xylanOamF4VPSlotIndex = _XylanOamF4VPSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 1),
    _XylanOamF4VPSlotIndex_Type()
)
xylanOamF4VPSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPSlotIndex.setStatus("mandatory")


class _XylanOamF4VPPortIndex_Type(Integer32):
    """Custom type xylanOamF4VPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XylanOamF4VPPortIndex_Type.__name__ = "Integer32"
_XylanOamF4VPPortIndex_Object = MibTableColumn
xylanOamF4VPPortIndex = _XylanOamF4VPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 2),
    _XylanOamF4VPPortIndex_Type()
)
xylanOamF4VPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPPortIndex.setStatus("mandatory")
_XylanOamF4VPVpiIndex_Type = Integer32
_XylanOamF4VPVpiIndex_Object = MibTableColumn
xylanOamF4VPVpiIndex = _XylanOamF4VPVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 3),
    _XylanOamF4VPVpiIndex_Type()
)
xylanOamF4VPVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPVpiIndex.setStatus("mandatory")


class _XylanOamF4VPAdminEnable_Type(Integer32):
    """Custom type xylanOamF4VPAdminEnable based on Integer32"""
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


_XylanOamF4VPAdminEnable_Type.__name__ = "Integer32"
_XylanOamF4VPAdminEnable_Object = MibTableColumn
xylanOamF4VPAdminEnable = _XylanOamF4VPAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 4),
    _XylanOamF4VPAdminEnable_Type()
)
xylanOamF4VPAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPAdminEnable.setStatus("mandatory")


class _XylanOamF4VPAisEnable_Type(Integer32):
    """Custom type xylanOamF4VPAisEnable based on Integer32"""
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


_XylanOamF4VPAisEnable_Type.__name__ = "Integer32"
_XylanOamF4VPAisEnable_Object = MibTableColumn
xylanOamF4VPAisEnable = _XylanOamF4VPAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 5),
    _XylanOamF4VPAisEnable_Type()
)
xylanOamF4VPAisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPAisEnable.setStatus("mandatory")


class _XylanOamF4VPRdiEnable_Type(Integer32):
    """Custom type xylanOamF4VPRdiEnable based on Integer32"""
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


_XylanOamF4VPRdiEnable_Type.__name__ = "Integer32"
_XylanOamF4VPRdiEnable_Object = MibTableColumn
xylanOamF4VPRdiEnable = _XylanOamF4VPRdiEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 6),
    _XylanOamF4VPRdiEnable_Type()
)
xylanOamF4VPRdiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPRdiEnable.setStatus("mandatory")


class _XylanOamF4VPContCheckEnable_Type(Integer32):
    """Custom type xylanOamF4VPContCheckEnable based on Integer32"""
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


_XylanOamF4VPContCheckEnable_Type.__name__ = "Integer32"
_XylanOamF4VPContCheckEnable_Object = MibTableColumn
xylanOamF4VPContCheckEnable = _XylanOamF4VPContCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 7),
    _XylanOamF4VPContCheckEnable_Type()
)
xylanOamF4VPContCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPContCheckEnable.setStatus("mandatory")


class _XylanOamF4VPTrapOnAlarmEnable_Type(Integer32):
    """Custom type xylanOamF4VPTrapOnAlarmEnable based on Integer32"""
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


_XylanOamF4VPTrapOnAlarmEnable_Type.__name__ = "Integer32"
_XylanOamF4VPTrapOnAlarmEnable_Object = MibTableColumn
xylanOamF4VPTrapOnAlarmEnable = _XylanOamF4VPTrapOnAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 8),
    _XylanOamF4VPTrapOnAlarmEnable_Type()
)
xylanOamF4VPTrapOnAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPTrapOnAlarmEnable.setStatus("mandatory")


class _XylanOamF4VPLoopbackEnable_Type(Integer32):
    """Custom type xylanOamF4VPLoopbackEnable based on Integer32"""
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


_XylanOamF4VPLoopbackEnable_Type.__name__ = "Integer32"
_XylanOamF4VPLoopbackEnable_Object = MibTableColumn
xylanOamF4VPLoopbackEnable = _XylanOamF4VPLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 9),
    _XylanOamF4VPLoopbackEnable_Type()
)
xylanOamF4VPLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPLoopbackEnable.setStatus("mandatory")


class _XylanOamF4VPLoopbackType_Type(Integer32):
    """Custom type xylanOamF4VPLoopbackType based on Integer32"""
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
        *(("access-line", 2),
          ("end-to-end", 1),
          ("inter-domain", 3),
          ("intra-domain", 5),
          ("network-to-endpoint", 4))
    )


_XylanOamF4VPLoopbackType_Type.__name__ = "Integer32"
_XylanOamF4VPLoopbackType_Object = MibTableColumn
xylanOamF4VPLoopbackType = _XylanOamF4VPLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 10),
    _XylanOamF4VPLoopbackType_Type()
)
xylanOamF4VPLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPLoopbackType.setStatus("mandatory")


class _XylanOamF4VPLoopbackStatus_Type(Integer32):
    """Custom type xylanOamF4VPLoopbackStatus based on Integer32"""
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
        *(("disabled", 1),
          ("responsewaiting", 4),
          ("successful", 2),
          ("unsuccessful", 3))
    )


_XylanOamF4VPLoopbackStatus_Type.__name__ = "Integer32"
_XylanOamF4VPLoopbackStatus_Object = MibTableColumn
xylanOamF4VPLoopbackStatus = _XylanOamF4VPLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 11),
    _XylanOamF4VPLoopbackStatus_Type()
)
xylanOamF4VPLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPLoopbackStatus.setStatus("mandatory")


class _XylanOamF4VPContCheckStatus_Type(Integer32):
    """Custom type xylanOamF4VPContCheckStatus based on Integer32"""
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
          ("disabled", 5),
          ("ready", 1),
          ("waitingActivate", 2),
          ("waitingDeactivate", 3))
    )


_XylanOamF4VPContCheckStatus_Type.__name__ = "Integer32"
_XylanOamF4VPContCheckStatus_Object = MibTableColumn
xylanOamF4VPContCheckStatus = _XylanOamF4VPContCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 12),
    _XylanOamF4VPContCheckStatus_Type()
)
xylanOamF4VPContCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPContCheckStatus.setStatus("mandatory")
_XylanOamF4VPAisRxCount_Type = Integer32
_XylanOamF4VPAisRxCount_Object = MibTableColumn
xylanOamF4VPAisRxCount = _XylanOamF4VPAisRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 13),
    _XylanOamF4VPAisRxCount_Type()
)
xylanOamF4VPAisRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPAisRxCount.setStatus("mandatory")
_XylanOamF4VPAisTxCount_Type = Integer32
_XylanOamF4VPAisTxCount_Object = MibTableColumn
xylanOamF4VPAisTxCount = _XylanOamF4VPAisTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 14),
    _XylanOamF4VPAisTxCount_Type()
)
xylanOamF4VPAisTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPAisTxCount.setStatus("mandatory")
_XylanOamF4VPRdiRxCount_Type = Integer32
_XylanOamF4VPRdiRxCount_Object = MibTableColumn
xylanOamF4VPRdiRxCount = _XylanOamF4VPRdiRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 15),
    _XylanOamF4VPRdiRxCount_Type()
)
xylanOamF4VPRdiRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPRdiRxCount.setStatus("mandatory")
_XylanOamF4VPRdiTxCount_Type = Integer32
_XylanOamF4VPRdiTxCount_Object = MibTableColumn
xylanOamF4VPRdiTxCount = _XylanOamF4VPRdiTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 16),
    _XylanOamF4VPRdiTxCount_Type()
)
xylanOamF4VPRdiTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPRdiTxCount.setStatus("mandatory")
_XylanOamF4VPLoopbackRxCount_Type = Integer32
_XylanOamF4VPLoopbackRxCount_Object = MibTableColumn
xylanOamF4VPLoopbackRxCount = _XylanOamF4VPLoopbackRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 17),
    _XylanOamF4VPLoopbackRxCount_Type()
)
xylanOamF4VPLoopbackRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPLoopbackRxCount.setStatus("mandatory")
_XylanOamF4VPLoopbackTxCount_Type = Integer32
_XylanOamF4VPLoopbackTxCount_Object = MibTableColumn
xylanOamF4VPLoopbackTxCount = _XylanOamF4VPLoopbackTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 18),
    _XylanOamF4VPLoopbackTxCount_Type()
)
xylanOamF4VPLoopbackTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPLoopbackTxCount.setStatus("mandatory")
_XylanOamF4VPContCheckRxCount_Type = Integer32
_XylanOamF4VPContCheckRxCount_Object = MibTableColumn
xylanOamF4VPContCheckRxCount = _XylanOamF4VPContCheckRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 19),
    _XylanOamF4VPContCheckRxCount_Type()
)
xylanOamF4VPContCheckRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPContCheckRxCount.setStatus("mandatory")
_XylanOamF4VPContCheckTxCount_Type = Integer32
_XylanOamF4VPContCheckTxCount_Object = MibTableColumn
xylanOamF4VPContCheckTxCount = _XylanOamF4VPContCheckTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 20),
    _XylanOamF4VPContCheckTxCount_Type()
)
xylanOamF4VPContCheckTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPContCheckTxCount.setStatus("mandatory")
_XylanOamF4VPLOCCount_Type = Integer32
_XylanOamF4VPLOCCount_Object = MibTableColumn
xylanOamF4VPLOCCount = _XylanOamF4VPLOCCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 21),
    _XylanOamF4VPLOCCount_Type()
)
xylanOamF4VPLOCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPLOCCount.setStatus("mandatory")
_XylanOamF4VPLoopbackSuccessCount_Type = Integer32
_XylanOamF4VPLoopbackSuccessCount_Object = MibTableColumn
xylanOamF4VPLoopbackSuccessCount = _XylanOamF4VPLoopbackSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 22),
    _XylanOamF4VPLoopbackSuccessCount_Type()
)
xylanOamF4VPLoopbackSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPLoopbackSuccessCount.setStatus("mandatory")
_XylanOamF4VPLoopbackFailureCount_Type = Integer32
_XylanOamF4VPLoopbackFailureCount_Object = MibTableColumn
xylanOamF4VPLoopbackFailureCount = _XylanOamF4VPLoopbackFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 23),
    _XylanOamF4VPLoopbackFailureCount_Type()
)
xylanOamF4VPLoopbackFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF4VPLoopbackFailureCount.setStatus("mandatory")


class _XylanOamF4VPSegmentAction_Type(Integer32):
    """Custom type xylanOamF4VPSegmentAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("extract", 3),
          ("none", 1))
    )


_XylanOamF4VPSegmentAction_Type.__name__ = "Integer32"
_XylanOamF4VPSegmentAction_Object = MibTableColumn
xylanOamF4VPSegmentAction = _XylanOamF4VPSegmentAction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 24),
    _XylanOamF4VPSegmentAction_Type()
)
xylanOamF4VPSegmentAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPSegmentAction.setStatus("mandatory")


class _XylanOamF4VPEndtoendAction_Type(Integer32):
    """Custom type xylanOamF4VPEndtoendAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("extract", 3),
          ("none", 1))
    )


_XylanOamF4VPEndtoendAction_Type.__name__ = "Integer32"
_XylanOamF4VPEndtoendAction_Object = MibTableColumn
xylanOamF4VPEndtoendAction = _XylanOamF4VPEndtoendAction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 1, 1, 25),
    _XylanOamF4VPEndtoendAction_Type()
)
xylanOamF4VPEndtoendAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF4VPEndtoendAction.setStatus("mandatory")
_XylanOamF5VCTable_Object = MibTable
xylanOamF5VCTable = _XylanOamF5VCTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2)
)
if mibBuilder.loadTexts:
    xylanOamF5VCTable.setStatus("mandatory")
_XylanOamF5VCEntry_Object = MibTableRow
xylanOamF5VCEntry = _XylanOamF5VCEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1)
)
xylanOamF5VCEntry.setIndexNames(
    (0, "XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"),
    (0, "XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"),
    (0, "XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"),
    (0, "XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"),
)
if mibBuilder.loadTexts:
    xylanOamF5VCEntry.setStatus("mandatory")


class _XylanOamF5VCSlotIndex_Type(Integer32):
    """Custom type xylanOamF5VCSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylanOamF5VCSlotIndex_Type.__name__ = "Integer32"
_XylanOamF5VCSlotIndex_Object = MibTableColumn
xylanOamF5VCSlotIndex = _XylanOamF5VCSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 1),
    _XylanOamF5VCSlotIndex_Type()
)
xylanOamF5VCSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCSlotIndex.setStatus("mandatory")


class _XylanOamF5VCPortIndex_Type(Integer32):
    """Custom type xylanOamF5VCPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_XylanOamF5VCPortIndex_Type.__name__ = "Integer32"
_XylanOamF5VCPortIndex_Object = MibTableColumn
xylanOamF5VCPortIndex = _XylanOamF5VCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 2),
    _XylanOamF5VCPortIndex_Type()
)
xylanOamF5VCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCPortIndex.setStatus("mandatory")
_XylanOamF5VCVpiIndex_Type = Integer32
_XylanOamF5VCVpiIndex_Object = MibTableColumn
xylanOamF5VCVpiIndex = _XylanOamF5VCVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 3),
    _XylanOamF5VCVpiIndex_Type()
)
xylanOamF5VCVpiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCVpiIndex.setStatus("mandatory")
_XylanOamF5VCVciIndex_Type = Integer32
_XylanOamF5VCVciIndex_Object = MibTableColumn
xylanOamF5VCVciIndex = _XylanOamF5VCVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 4),
    _XylanOamF5VCVciIndex_Type()
)
xylanOamF5VCVciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCVciIndex.setStatus("mandatory")


class _XylanOamF5VCAdminEnable_Type(Integer32):
    """Custom type xylanOamF5VCAdminEnable based on Integer32"""
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


_XylanOamF5VCAdminEnable_Type.__name__ = "Integer32"
_XylanOamF5VCAdminEnable_Object = MibTableColumn
xylanOamF5VCAdminEnable = _XylanOamF5VCAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 5),
    _XylanOamF5VCAdminEnable_Type()
)
xylanOamF5VCAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCAdminEnable.setStatus("mandatory")


class _XylanOamF5VCAisEnable_Type(Integer32):
    """Custom type xylanOamF5VCAisEnable based on Integer32"""
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


_XylanOamF5VCAisEnable_Type.__name__ = "Integer32"
_XylanOamF5VCAisEnable_Object = MibTableColumn
xylanOamF5VCAisEnable = _XylanOamF5VCAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 6),
    _XylanOamF5VCAisEnable_Type()
)
xylanOamF5VCAisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCAisEnable.setStatus("mandatory")


class _XylanOamF5VCRdiEnable_Type(Integer32):
    """Custom type xylanOamF5VCRdiEnable based on Integer32"""
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


_XylanOamF5VCRdiEnable_Type.__name__ = "Integer32"
_XylanOamF5VCRdiEnable_Object = MibTableColumn
xylanOamF5VCRdiEnable = _XylanOamF5VCRdiEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 7),
    _XylanOamF5VCRdiEnable_Type()
)
xylanOamF5VCRdiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCRdiEnable.setStatus("mandatory")


class _XylanOamF5VCContCheckEnable_Type(Integer32):
    """Custom type xylanOamF5VCContCheckEnable based on Integer32"""
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


_XylanOamF5VCContCheckEnable_Type.__name__ = "Integer32"
_XylanOamF5VCContCheckEnable_Object = MibTableColumn
xylanOamF5VCContCheckEnable = _XylanOamF5VCContCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 8),
    _XylanOamF5VCContCheckEnable_Type()
)
xylanOamF5VCContCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCContCheckEnable.setStatus("mandatory")


class _XylanOamF5VCTrapOnAlarmEnable_Type(Integer32):
    """Custom type xylanOamF5VCTrapOnAlarmEnable based on Integer32"""
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


_XylanOamF5VCTrapOnAlarmEnable_Type.__name__ = "Integer32"
_XylanOamF5VCTrapOnAlarmEnable_Object = MibTableColumn
xylanOamF5VCTrapOnAlarmEnable = _XylanOamF5VCTrapOnAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 9),
    _XylanOamF5VCTrapOnAlarmEnable_Type()
)
xylanOamF5VCTrapOnAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCTrapOnAlarmEnable.setStatus("mandatory")


class _XylanOamF5VCLoopbackEnable_Type(Integer32):
    """Custom type xylanOamF5VCLoopbackEnable based on Integer32"""
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


_XylanOamF5VCLoopbackEnable_Type.__name__ = "Integer32"
_XylanOamF5VCLoopbackEnable_Object = MibTableColumn
xylanOamF5VCLoopbackEnable = _XylanOamF5VCLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 10),
    _XylanOamF5VCLoopbackEnable_Type()
)
xylanOamF5VCLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCLoopbackEnable.setStatus("mandatory")


class _XylanOamF5VCLoopbackType_Type(Integer32):
    """Custom type xylanOamF5VCLoopbackType based on Integer32"""
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
        *(("access-line", 2),
          ("end-to-end", 1),
          ("inter-domain", 3),
          ("intra-domain", 5),
          ("network-to-endpoint", 4))
    )


_XylanOamF5VCLoopbackType_Type.__name__ = "Integer32"
_XylanOamF5VCLoopbackType_Object = MibTableColumn
xylanOamF5VCLoopbackType = _XylanOamF5VCLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 11),
    _XylanOamF5VCLoopbackType_Type()
)
xylanOamF5VCLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCLoopbackType.setStatus("mandatory")


class _XylanOamF5VCLoopbackStatus_Type(Integer32):
    """Custom type xylanOamF5VCLoopbackStatus based on Integer32"""
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
        *(("disabled", 1),
          ("responsewaiting", 4),
          ("successful", 2),
          ("unsuccessful", 3))
    )


_XylanOamF5VCLoopbackStatus_Type.__name__ = "Integer32"
_XylanOamF5VCLoopbackStatus_Object = MibTableColumn
xylanOamF5VCLoopbackStatus = _XylanOamF5VCLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 12),
    _XylanOamF5VCLoopbackStatus_Type()
)
xylanOamF5VCLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCLoopbackStatus.setStatus("mandatory")


class _XylanOamF5VCContCheckStatus_Type(Integer32):
    """Custom type xylanOamF5VCContCheckStatus based on Integer32"""
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
          ("disabled", 5),
          ("ready", 1),
          ("waitingActivate", 2),
          ("waitingDeactivate", 3))
    )


_XylanOamF5VCContCheckStatus_Type.__name__ = "Integer32"
_XylanOamF5VCContCheckStatus_Object = MibTableColumn
xylanOamF5VCContCheckStatus = _XylanOamF5VCContCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 13),
    _XylanOamF5VCContCheckStatus_Type()
)
xylanOamF5VCContCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCContCheckStatus.setStatus("mandatory")
_XylanOamF5VCAisRxCount_Type = Integer32
_XylanOamF5VCAisRxCount_Object = MibTableColumn
xylanOamF5VCAisRxCount = _XylanOamF5VCAisRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 14),
    _XylanOamF5VCAisRxCount_Type()
)
xylanOamF5VCAisRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCAisRxCount.setStatus("mandatory")
_XylanOamF5VCAisTxCount_Type = Integer32
_XylanOamF5VCAisTxCount_Object = MibTableColumn
xylanOamF5VCAisTxCount = _XylanOamF5VCAisTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 15),
    _XylanOamF5VCAisTxCount_Type()
)
xylanOamF5VCAisTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCAisTxCount.setStatus("mandatory")
_XylanOamF5VCRdiRxCount_Type = Integer32
_XylanOamF5VCRdiRxCount_Object = MibTableColumn
xylanOamF5VCRdiRxCount = _XylanOamF5VCRdiRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 16),
    _XylanOamF5VCRdiRxCount_Type()
)
xylanOamF5VCRdiRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCRdiRxCount.setStatus("mandatory")
_XylanOamF5VCRdiTxCount_Type = Integer32
_XylanOamF5VCRdiTxCount_Object = MibTableColumn
xylanOamF5VCRdiTxCount = _XylanOamF5VCRdiTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 17),
    _XylanOamF5VCRdiTxCount_Type()
)
xylanOamF5VCRdiTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCRdiTxCount.setStatus("mandatory")
_XylanOamF5VCLoopbackRxCount_Type = Integer32
_XylanOamF5VCLoopbackRxCount_Object = MibTableColumn
xylanOamF5VCLoopbackRxCount = _XylanOamF5VCLoopbackRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 18),
    _XylanOamF5VCLoopbackRxCount_Type()
)
xylanOamF5VCLoopbackRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCLoopbackRxCount.setStatus("mandatory")
_XylanOamF5VCLoopbackTxCount_Type = Integer32
_XylanOamF5VCLoopbackTxCount_Object = MibTableColumn
xylanOamF5VCLoopbackTxCount = _XylanOamF5VCLoopbackTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 19),
    _XylanOamF5VCLoopbackTxCount_Type()
)
xylanOamF5VCLoopbackTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCLoopbackTxCount.setStatus("mandatory")
_XylanOamF5VCContCheckRxCount_Type = Integer32
_XylanOamF5VCContCheckRxCount_Object = MibTableColumn
xylanOamF5VCContCheckRxCount = _XylanOamF5VCContCheckRxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 20),
    _XylanOamF5VCContCheckRxCount_Type()
)
xylanOamF5VCContCheckRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCContCheckRxCount.setStatus("mandatory")
_XylanOamF5VCContCheckTxCount_Type = Integer32
_XylanOamF5VCContCheckTxCount_Object = MibTableColumn
xylanOamF5VCContCheckTxCount = _XylanOamF5VCContCheckTxCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 21),
    _XylanOamF5VCContCheckTxCount_Type()
)
xylanOamF5VCContCheckTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCContCheckTxCount.setStatus("mandatory")
_XylanOamF5VCLOCCount_Type = Integer32
_XylanOamF5VCLOCCount_Object = MibTableColumn
xylanOamF5VCLOCCount = _XylanOamF5VCLOCCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 22),
    _XylanOamF5VCLOCCount_Type()
)
xylanOamF5VCLOCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCLOCCount.setStatus("mandatory")
_XylanOamF5VCLoopbackSuccessCount_Type = Integer32
_XylanOamF5VCLoopbackSuccessCount_Object = MibTableColumn
xylanOamF5VCLoopbackSuccessCount = _XylanOamF5VCLoopbackSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 23),
    _XylanOamF5VCLoopbackSuccessCount_Type()
)
xylanOamF5VCLoopbackSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCLoopbackSuccessCount.setStatus("mandatory")
_XylanOamF5VCLoopbackFailureCount_Type = Integer32
_XylanOamF5VCLoopbackFailureCount_Object = MibTableColumn
xylanOamF5VCLoopbackFailureCount = _XylanOamF5VCLoopbackFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 24),
    _XylanOamF5VCLoopbackFailureCount_Type()
)
xylanOamF5VCLoopbackFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanOamF5VCLoopbackFailureCount.setStatus("mandatory")


class _XylanOamF5VCSegmentAction_Type(Integer32):
    """Custom type xylanOamF5VCSegmentAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("extract", 3),
          ("none", 1))
    )


_XylanOamF5VCSegmentAction_Type.__name__ = "Integer32"
_XylanOamF5VCSegmentAction_Object = MibTableColumn
xylanOamF5VCSegmentAction = _XylanOamF5VCSegmentAction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 25),
    _XylanOamF5VCSegmentAction_Type()
)
xylanOamF5VCSegmentAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCSegmentAction.setStatus("mandatory")


class _XylanOamF5VCEndtoendAction_Type(Integer32):
    """Custom type xylanOamF5VCEndtoendAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("extract", 3),
          ("none", 1))
    )


_XylanOamF5VCEndtoendAction_Type.__name__ = "Integer32"
_XylanOamF5VCEndtoendAction_Object = MibTableColumn
xylanOamF5VCEndtoendAction = _XylanOamF5VCEndtoendAction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 2, 1, 26),
    _XylanOamF5VCEndtoendAction_Type()
)
xylanOamF5VCEndtoendAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanOamF5VCEndtoendAction.setStatus("mandatory")
_XylanOamTraps_ObjectIdentity = ObjectIdentity
xylanOamTraps = _XylanOamTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3)
)

# Managed Objects groups


# Notification objects

xylanOamTrapVCAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 1)
)
xylanOamTrapVCAIS.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVCAIS.setStatus(
        ""
    )

xylanOamTrapVCRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 2)
)
xylanOamTrapVCRDI.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVCRDI.setStatus(
        ""
    )

xylanOamTrapVCLOC = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 3)
)
xylanOamTrapVCLOC.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVCLOC.setStatus(
        ""
    )

xylanOamTrapVCUnsuccessLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 4)
)
xylanOamTrapVCUnsuccessLoop.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF5VCSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVpiIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF5VCVciIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVCUnsuccessLoop.setStatus(
        ""
    )

xylanOamTrapVPAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 5)
)
xylanOamTrapVPAIS.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVPAIS.setStatus(
        ""
    )

xylanOamTrapVPRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 6)
)
xylanOamTrapVPRDI.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVPRDI.setStatus(
        ""
    )

xylanOamTrapVPLOC = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 7)
)
xylanOamTrapVPLOC.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVPLOC.setStatus(
        ""
    )

xylanOamTrapVPUnsuccessLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 2, 28, 1, 3, 0, 8)
)
xylanOamTrapVPUnsuccessLoop.setObjects(
      *(("XYLAN-OAM-MIB", "xylanOamF4VPSlotIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPPortIndex"),
        ("XYLAN-OAM-MIB", "xylanOamF4VPVpiIndex"))
)
if mibBuilder.loadTexts:
    xylanOamTrapVPUnsuccessLoop.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-OAM-MIB",
    **{"xylanOam": xylanOam,
       "xylanOamF4VPTable": xylanOamF4VPTable,
       "xylanOamF4VPEntry": xylanOamF4VPEntry,
       "xylanOamF4VPSlotIndex": xylanOamF4VPSlotIndex,
       "xylanOamF4VPPortIndex": xylanOamF4VPPortIndex,
       "xylanOamF4VPVpiIndex": xylanOamF4VPVpiIndex,
       "xylanOamF4VPAdminEnable": xylanOamF4VPAdminEnable,
       "xylanOamF4VPAisEnable": xylanOamF4VPAisEnable,
       "xylanOamF4VPRdiEnable": xylanOamF4VPRdiEnable,
       "xylanOamF4VPContCheckEnable": xylanOamF4VPContCheckEnable,
       "xylanOamF4VPTrapOnAlarmEnable": xylanOamF4VPTrapOnAlarmEnable,
       "xylanOamF4VPLoopbackEnable": xylanOamF4VPLoopbackEnable,
       "xylanOamF4VPLoopbackType": xylanOamF4VPLoopbackType,
       "xylanOamF4VPLoopbackStatus": xylanOamF4VPLoopbackStatus,
       "xylanOamF4VPContCheckStatus": xylanOamF4VPContCheckStatus,
       "xylanOamF4VPAisRxCount": xylanOamF4VPAisRxCount,
       "xylanOamF4VPAisTxCount": xylanOamF4VPAisTxCount,
       "xylanOamF4VPRdiRxCount": xylanOamF4VPRdiRxCount,
       "xylanOamF4VPRdiTxCount": xylanOamF4VPRdiTxCount,
       "xylanOamF4VPLoopbackRxCount": xylanOamF4VPLoopbackRxCount,
       "xylanOamF4VPLoopbackTxCount": xylanOamF4VPLoopbackTxCount,
       "xylanOamF4VPContCheckRxCount": xylanOamF4VPContCheckRxCount,
       "xylanOamF4VPContCheckTxCount": xylanOamF4VPContCheckTxCount,
       "xylanOamF4VPLOCCount": xylanOamF4VPLOCCount,
       "xylanOamF4VPLoopbackSuccessCount": xylanOamF4VPLoopbackSuccessCount,
       "xylanOamF4VPLoopbackFailureCount": xylanOamF4VPLoopbackFailureCount,
       "xylanOamF4VPSegmentAction": xylanOamF4VPSegmentAction,
       "xylanOamF4VPEndtoendAction": xylanOamF4VPEndtoendAction,
       "xylanOamF5VCTable": xylanOamF5VCTable,
       "xylanOamF5VCEntry": xylanOamF5VCEntry,
       "xylanOamF5VCSlotIndex": xylanOamF5VCSlotIndex,
       "xylanOamF5VCPortIndex": xylanOamF5VCPortIndex,
       "xylanOamF5VCVpiIndex": xylanOamF5VCVpiIndex,
       "xylanOamF5VCVciIndex": xylanOamF5VCVciIndex,
       "xylanOamF5VCAdminEnable": xylanOamF5VCAdminEnable,
       "xylanOamF5VCAisEnable": xylanOamF5VCAisEnable,
       "xylanOamF5VCRdiEnable": xylanOamF5VCRdiEnable,
       "xylanOamF5VCContCheckEnable": xylanOamF5VCContCheckEnable,
       "xylanOamF5VCTrapOnAlarmEnable": xylanOamF5VCTrapOnAlarmEnable,
       "xylanOamF5VCLoopbackEnable": xylanOamF5VCLoopbackEnable,
       "xylanOamF5VCLoopbackType": xylanOamF5VCLoopbackType,
       "xylanOamF5VCLoopbackStatus": xylanOamF5VCLoopbackStatus,
       "xylanOamF5VCContCheckStatus": xylanOamF5VCContCheckStatus,
       "xylanOamF5VCAisRxCount": xylanOamF5VCAisRxCount,
       "xylanOamF5VCAisTxCount": xylanOamF5VCAisTxCount,
       "xylanOamF5VCRdiRxCount": xylanOamF5VCRdiRxCount,
       "xylanOamF5VCRdiTxCount": xylanOamF5VCRdiTxCount,
       "xylanOamF5VCLoopbackRxCount": xylanOamF5VCLoopbackRxCount,
       "xylanOamF5VCLoopbackTxCount": xylanOamF5VCLoopbackTxCount,
       "xylanOamF5VCContCheckRxCount": xylanOamF5VCContCheckRxCount,
       "xylanOamF5VCContCheckTxCount": xylanOamF5VCContCheckTxCount,
       "xylanOamF5VCLOCCount": xylanOamF5VCLOCCount,
       "xylanOamF5VCLoopbackSuccessCount": xylanOamF5VCLoopbackSuccessCount,
       "xylanOamF5VCLoopbackFailureCount": xylanOamF5VCLoopbackFailureCount,
       "xylanOamF5VCSegmentAction": xylanOamF5VCSegmentAction,
       "xylanOamF5VCEndtoendAction": xylanOamF5VCEndtoendAction,
       "xylanOamTraps": xylanOamTraps,
       "xylanOamTrapVCAIS": xylanOamTrapVCAIS,
       "xylanOamTrapVCRDI": xylanOamTrapVCRDI,
       "xylanOamTrapVCLOC": xylanOamTrapVCLOC,
       "xylanOamTrapVCUnsuccessLoop": xylanOamTrapVCUnsuccessLoop,
       "xylanOamTrapVPAIS": xylanOamTrapVPAIS,
       "xylanOamTrapVPRDI": xylanOamTrapVPRDI,
       "xylanOamTrapVPLOC": xylanOamTrapVPLOC,
       "xylanOamTrapVPUnsuccessLoop": xylanOamTrapVPUnsuccessLoop}
)
