# SNMP MIB module (CXV34-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXV34-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:58 2024
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

(Alias,
 SapIndex,
 cxV34) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxV34")

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

_V34SlotTable_Object = MibTable
v34SlotTable = _V34SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1)
)
if mibBuilder.loadTexts:
    v34SlotTable.setStatus("mandatory")
_V34SlotEntry_Object = MibTableRow
v34SlotEntry = _V34SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1)
)
v34SlotEntry.setIndexNames(
    (0, "CXV34-MIB", "v34SlotNumber"),
)
if mibBuilder.loadTexts:
    v34SlotEntry.setStatus("mandatory")
_V34SlotNumber_Type = SapIndex
_V34SlotNumber_Object = MibTableColumn
v34SlotNumber = _V34SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 1),
    _V34SlotNumber_Type()
)
v34SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotNumber.setStatus("mandatory")
_V34SlotAlias_Type = Alias
_V34SlotAlias_Object = MibTableColumn
v34SlotAlias = _V34SlotAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 2),
    _V34SlotAlias_Type()
)
v34SlotAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v34SlotAlias.setStatus("mandatory")


class _V34SlotRowStatus_Type(Integer32):
    """Custom type v34SlotRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_V34SlotRowStatus_Type.__name__ = "Integer32"
_V34SlotRowStatus_Object = MibTableColumn
v34SlotRowStatus = _V34SlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 3),
    _V34SlotRowStatus_Type()
)
v34SlotRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v34SlotRowStatus.setStatus("mandatory")


class _V34SlotStatus_Type(Integer32):
    """Custom type v34SlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v34-not-present", 1),
          ("v34-present", 2),
          ("v34-present-failed", 3))
    )


_V34SlotStatus_Type.__name__ = "Integer32"
_V34SlotStatus_Object = MibTableColumn
v34SlotStatus = _V34SlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 4),
    _V34SlotStatus_Type()
)
v34SlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotStatus.setStatus("mandatory")


class _V34SlotModemString_Type(DisplayString):
    """Custom type v34SlotModemString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_V34SlotModemString_Type.__name__ = "DisplayString"
_V34SlotModemString_Object = MibTableColumn
v34SlotModemString = _V34SlotModemString_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 5),
    _V34SlotModemString_Type()
)
v34SlotModemString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v34SlotModemString.setStatus("mandatory")


class _V34SlotDialNumber_Type(DisplayString):
    """Custom type v34SlotDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_V34SlotDialNumber_Type.__name__ = "DisplayString"
_V34SlotDialNumber_Object = MibTableColumn
v34SlotDialNumber = _V34SlotDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 6),
    _V34SlotDialNumber_Type()
)
v34SlotDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v34SlotDialNumber.setStatus("mandatory")


class _V34SlotAnswerMode_Type(Integer32):
    """Custom type v34SlotAnswerMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer-disabled", 1),
          ("answer-enabled", 2),
          ("test-mode", 3))
    )


_V34SlotAnswerMode_Type.__name__ = "Integer32"
_V34SlotAnswerMode_Object = MibTableColumn
v34SlotAnswerMode = _V34SlotAnswerMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 7),
    _V34SlotAnswerMode_Type()
)
v34SlotAnswerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v34SlotAnswerMode.setStatus("mandatory")


class _V34SlotSpeedStatus_Type(Integer32):
    """Custom type v34SlotSpeedStatus based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("speed-0-300", 1),
          ("speed-1200", 3),
          ("speed-12000", 8),
          ("speed-14400", 9),
          ("speed-16800", 10),
          ("speed-19200", 11),
          ("speed-21600", 12),
          ("speed-2400", 4),
          ("speed-24000", 13),
          ("speed-26400", 14),
          ("speed-28800", 15),
          ("speed-4800", 5),
          ("speed-600", 2),
          ("speed-7200", 6),
          ("speed-9600", 7))
    )


_V34SlotSpeedStatus_Type.__name__ = "Integer32"
_V34SlotSpeedStatus_Object = MibTableColumn
v34SlotSpeedStatus = _V34SlotSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 8),
    _V34SlotSpeedStatus_Type()
)
v34SlotSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotSpeedStatus.setStatus("mandatory")


class _V34SlotRetrainStatus_Type(Integer32):
    """Custom type v34SlotRetrainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-retraining", 1),
          ("retraining", 2))
    )


_V34SlotRetrainStatus_Type.__name__ = "Integer32"
_V34SlotRetrainStatus_Object = MibTableColumn
v34SlotRetrainStatus = _V34SlotRetrainStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 9),
    _V34SlotRetrainStatus_Type()
)
v34SlotRetrainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotRetrainStatus.setStatus("mandatory")


class _V34SlotHookStatus_Type(Integer32):
    """Custom type v34SlotHookStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-hook", 2),
          ("on-hook", 1))
    )


_V34SlotHookStatus_Type.__name__ = "Integer32"
_V34SlotHookStatus_Object = MibTableColumn
v34SlotHookStatus = _V34SlotHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 10),
    _V34SlotHookStatus_Type()
)
v34SlotHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotHookStatus.setStatus("mandatory")


class _V34SlotRingStatus_Type(Integer32):
    """Custom type v34SlotRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-ring", 1),
          ("ring", 2))
    )


_V34SlotRingStatus_Type.__name__ = "Integer32"
_V34SlotRingStatus_Object = MibTableColumn
v34SlotRingStatus = _V34SlotRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 11),
    _V34SlotRingStatus_Type()
)
v34SlotRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotRingStatus.setStatus("mandatory")


class _V34SlotDsrStatus_Type(Integer32):
    """Custom type v34SlotDsrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsr-asserted", 2),
          ("dsr-deasserted", 1))
    )


_V34SlotDsrStatus_Type.__name__ = "Integer32"
_V34SlotDsrStatus_Object = MibTableColumn
v34SlotDsrStatus = _V34SlotDsrStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 12),
    _V34SlotDsrStatus_Type()
)
v34SlotDsrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotDsrStatus.setStatus("mandatory")


class _V34SlotDtrStatus_Type(Integer32):
    """Custom type v34SlotDtrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr-asserted", 2),
          ("dtr-deasserted", 1))
    )


_V34SlotDtrStatus_Type.__name__ = "Integer32"
_V34SlotDtrStatus_Object = MibTableColumn
v34SlotDtrStatus = _V34SlotDtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 13),
    _V34SlotDtrStatus_Type()
)
v34SlotDtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotDtrStatus.setStatus("mandatory")


class _V34SlotModel_Type(Integer32):
    """Custom type v34SlotModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_V34SlotModel_Type.__name__ = "Integer32"
_V34SlotModel_Object = MibTableColumn
v34SlotModel = _V34SlotModel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 14),
    _V34SlotModel_Type()
)
v34SlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotModel.setStatus("mandatory")


class _V34SlotRevision_Type(Integer32):
    """Custom type v34SlotRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_V34SlotRevision_Type.__name__ = "Integer32"
_V34SlotRevision_Object = MibTableColumn
v34SlotRevision = _V34SlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 15),
    _V34SlotRevision_Type()
)
v34SlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotRevision.setStatus("mandatory")


class _V34SlotEco_Type(Integer32):
    """Custom type v34SlotEco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_V34SlotEco_Type.__name__ = "Integer32"
_V34SlotEco_Object = MibTableColumn
v34SlotEco = _V34SlotEco_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 42, 1, 1, 16),
    _V34SlotEco_Type()
)
v34SlotEco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34SlotEco.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXV34-MIB",
    **{"v34SlotTable": v34SlotTable,
       "v34SlotEntry": v34SlotEntry,
       "v34SlotNumber": v34SlotNumber,
       "v34SlotAlias": v34SlotAlias,
       "v34SlotRowStatus": v34SlotRowStatus,
       "v34SlotStatus": v34SlotStatus,
       "v34SlotModemString": v34SlotModemString,
       "v34SlotDialNumber": v34SlotDialNumber,
       "v34SlotAnswerMode": v34SlotAnswerMode,
       "v34SlotSpeedStatus": v34SlotSpeedStatus,
       "v34SlotRetrainStatus": v34SlotRetrainStatus,
       "v34SlotHookStatus": v34SlotHookStatus,
       "v34SlotRingStatus": v34SlotRingStatus,
       "v34SlotDsrStatus": v34SlotDsrStatus,
       "v34SlotDtrStatus": v34SlotDtrStatus,
       "v34SlotModel": v34SlotModel,
       "v34SlotRevision": v34SlotRevision,
       "v34SlotEco": v34SlotEco}
)
