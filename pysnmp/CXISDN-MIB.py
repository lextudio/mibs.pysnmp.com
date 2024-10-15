# SNMP MIB module (CXISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:32 2024
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
 cxISDN) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxISDN")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IsdnSoftwareVersion_Type = DisplayString
_IsdnSoftwareVersion_Object = MibScalar
isdnSoftwareVersion = _IsdnSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 1),
    _IsdnSoftwareVersion_Type()
)
isdnSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSoftwareVersion.setStatus("mandatory")


class _IsdnTraps_Type(Integer32):
    """Custom type isdnTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IsdnTraps_Type.__name__ = "Integer32"
_IsdnTraps_Object = MibScalar
isdnTraps = _IsdnTraps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 2),
    _IsdnTraps_Type()
)
isdnTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTraps.setStatus("mandatory")
_IsdnL3SapTable_Object = MibTable
isdnL3SapTable = _IsdnL3SapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20)
)
if mibBuilder.loadTexts:
    isdnL3SapTable.setStatus("mandatory")
_IsdnL3SapEntry_Object = MibTableRow
isdnL3SapEntry = _IsdnL3SapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1)
)
isdnL3SapEntry.setIndexNames(
    (0, "CXISDN-MIB", "isdnL3SapNumber"),
)
if mibBuilder.loadTexts:
    isdnL3SapEntry.setStatus("mandatory")
_IsdnL3SapNumber_Type = SapIndex
_IsdnL3SapNumber_Object = MibTableColumn
isdnL3SapNumber = _IsdnL3SapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 1),
    _IsdnL3SapNumber_Type()
)
isdnL3SapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnL3SapNumber.setStatus("mandatory")


class _IsdnL3SapRowStatus_Type(Integer32):
    """Custom type isdnL3SapRowStatus based on Integer32"""
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


_IsdnL3SapRowStatus_Type.__name__ = "Integer32"
_IsdnL3SapRowStatus_Object = MibTableColumn
isdnL3SapRowStatus = _IsdnL3SapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 2),
    _IsdnL3SapRowStatus_Type()
)
isdnL3SapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapRowStatus.setStatus("mandatory")
_IsdnL3SapAlias_Type = Alias
_IsdnL3SapAlias_Object = MibTableColumn
isdnL3SapAlias = _IsdnL3SapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 3),
    _IsdnL3SapAlias_Type()
)
isdnL3SapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapAlias.setStatus("mandatory")
_IsdnL3SapCompanionAlias_Type = Alias
_IsdnL3SapCompanionAlias_Object = MibTableColumn
isdnL3SapCompanionAlias = _IsdnL3SapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 4),
    _IsdnL3SapCompanionAlias_Type()
)
isdnL3SapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapCompanionAlias.setStatus("mandatory")


class _IsdnL3SapUserNetType_Type(Integer32):
    """Custom type isdnL3SapUserNetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_IsdnL3SapUserNetType_Type.__name__ = "Integer32"
_IsdnL3SapUserNetType_Object = MibTableColumn
isdnL3SapUserNetType = _IsdnL3SapUserNetType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 10),
    _IsdnL3SapUserNetType_Type()
)
isdnL3SapUserNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapUserNetType.setStatus("mandatory")


class _IsdnL3SapT303Timer_Type(Integer32):
    """Custom type isdnL3SapT303Timer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT303Timer_Type.__name__ = "Integer32"
_IsdnL3SapT303Timer_Object = MibTableColumn
isdnL3SapT303Timer = _IsdnL3SapT303Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 11),
    _IsdnL3SapT303Timer_Type()
)
isdnL3SapT303Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT303Timer.setStatus("mandatory")


class _IsdnL3SapT304Timer_Type(Integer32):
    """Custom type isdnL3SapT304Timer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT304Timer_Type.__name__ = "Integer32"
_IsdnL3SapT304Timer_Object = MibTableColumn
isdnL3SapT304Timer = _IsdnL3SapT304Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 12),
    _IsdnL3SapT304Timer_Type()
)
isdnL3SapT304Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT304Timer.setStatus("mandatory")


class _IsdnL3SapT305Timer_Type(Integer32):
    """Custom type isdnL3SapT305Timer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT305Timer_Type.__name__ = "Integer32"
_IsdnL3SapT305Timer_Object = MibTableColumn
isdnL3SapT305Timer = _IsdnL3SapT305Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 13),
    _IsdnL3SapT305Timer_Type()
)
isdnL3SapT305Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT305Timer.setStatus("mandatory")


class _IsdnL3SapT308Timer_Type(Integer32):
    """Custom type isdnL3SapT308Timer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT308Timer_Type.__name__ = "Integer32"
_IsdnL3SapT308Timer_Object = MibTableColumn
isdnL3SapT308Timer = _IsdnL3SapT308Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 14),
    _IsdnL3SapT308Timer_Type()
)
isdnL3SapT308Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT308Timer.setStatus("mandatory")


class _IsdnL3SapT310Timer_Type(Integer32):
    """Custom type isdnL3SapT310Timer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT310Timer_Type.__name__ = "Integer32"
_IsdnL3SapT310Timer_Object = MibTableColumn
isdnL3SapT310Timer = _IsdnL3SapT310Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 15),
    _IsdnL3SapT310Timer_Type()
)
isdnL3SapT310Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT310Timer.setStatus("mandatory")


class _IsdnL3SapT313Timer_Type(Integer32):
    """Custom type isdnL3SapT313Timer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT313Timer_Type.__name__ = "Integer32"
_IsdnL3SapT313Timer_Object = MibTableColumn
isdnL3SapT313Timer = _IsdnL3SapT313Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 16),
    _IsdnL3SapT313Timer_Type()
)
isdnL3SapT313Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT313Timer.setStatus("mandatory")


class _IsdnL3SapT318Timer_Type(Integer32):
    """Custom type isdnL3SapT318Timer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT318Timer_Type.__name__ = "Integer32"
_IsdnL3SapT318Timer_Object = MibTableColumn
isdnL3SapT318Timer = _IsdnL3SapT318Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 17),
    _IsdnL3SapT318Timer_Type()
)
isdnL3SapT318Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT318Timer.setStatus("mandatory")


class _IsdnL3SapT319Timer_Type(Integer32):
    """Custom type isdnL3SapT319Timer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnL3SapT319Timer_Type.__name__ = "Integer32"
_IsdnL3SapT319Timer_Object = MibTableColumn
isdnL3SapT319Timer = _IsdnL3SapT319Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 18),
    _IsdnL3SapT319Timer_Type()
)
isdnL3SapT319Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapT319Timer.setStatus("mandatory")


class _IsdnL3SapDefTimerCfg_Type(Integer32):
    """Custom type isdnL3SapDefTimerCfg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defCfg", 2),
          ("noDefCfg", 1))
    )


_IsdnL3SapDefTimerCfg_Type.__name__ = "Integer32"
_IsdnL3SapDefTimerCfg_Object = MibTableColumn
isdnL3SapDefTimerCfg = _IsdnL3SapDefTimerCfg_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 19),
    _IsdnL3SapDefTimerCfg_Type()
)
isdnL3SapDefTimerCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnL3SapDefTimerCfg.setStatus("mandatory")


class _IsdnL3SapStatusEvent_Type(Integer32):
    """Custom type isdnL3SapStatusEvent based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("badCfgVersion", 2),
          ("badDslID", 3),
          ("badSwitchType", 8),
          ("dslInUse", 4),
          ("dslNotInUse", 5),
          ("nlcbInitErr", 7),
          ("nlcbPoolErr", 9),
          ("noEvent", 1),
          ("noNLCB", 6))
    )


_IsdnL3SapStatusEvent_Type.__name__ = "Integer32"
_IsdnL3SapStatusEvent_Object = MibTableColumn
isdnL3SapStatusEvent = _IsdnL3SapStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 40),
    _IsdnL3SapStatusEvent_Type()
)
isdnL3SapStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnL3SapStatusEvent.setStatus("mandatory")


class _IsdnL3SapDslType_Type(Integer32):
    """Custom type isdnL3SapDslType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bri", 2),
          ("none", 1),
          ("pri", 3))
    )


_IsdnL3SapDslType_Type.__name__ = "Integer32"
_IsdnL3SapDslType_Object = MibTableColumn
isdnL3SapDslType = _IsdnL3SapDslType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 41),
    _IsdnL3SapDslType_Type()
)
isdnL3SapDslType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnL3SapDslType.setStatus("mandatory")


class _IsdnL3SapBRIType_Type(Integer32):
    """Custom type isdnL3SapBRIType based on Integer32"""
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
        *(("none", 1),
          ("s-t", 3),
          ("u", 2))
    )


_IsdnL3SapBRIType_Type.__name__ = "Integer32"
_IsdnL3SapBRIType_Object = MibTableColumn
isdnL3SapBRIType = _IsdnL3SapBRIType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 20, 1, 42),
    _IsdnL3SapBRIType_Type()
)
isdnL3SapBRIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnL3SapBRIType.setStatus("mandatory")
_IsdnCCSapTable_Object = MibTable
isdnCCSapTable = _IsdnCCSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21)
)
if mibBuilder.loadTexts:
    isdnCCSapTable.setStatus("mandatory")
_IsdnCCSapEntry_Object = MibTableRow
isdnCCSapEntry = _IsdnCCSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1)
)
isdnCCSapEntry.setIndexNames(
    (0, "CXISDN-MIB", "isdnCCSapNumber"),
)
if mibBuilder.loadTexts:
    isdnCCSapEntry.setStatus("mandatory")
_IsdnCCSapNumber_Type = SapIndex
_IsdnCCSapNumber_Object = MibTableColumn
isdnCCSapNumber = _IsdnCCSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 1),
    _IsdnCCSapNumber_Type()
)
isdnCCSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCCSapNumber.setStatus("mandatory")


class _IsdnCCSapRowStatus_Type(Integer32):
    """Custom type isdnCCSapRowStatus based on Integer32"""
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


_IsdnCCSapRowStatus_Type.__name__ = "Integer32"
_IsdnCCSapRowStatus_Object = MibTableColumn
isdnCCSapRowStatus = _IsdnCCSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 2),
    _IsdnCCSapRowStatus_Type()
)
isdnCCSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapRowStatus.setStatus("mandatory")
_IsdnCCSapAlias_Type = Alias
_IsdnCCSapAlias_Object = MibTableColumn
isdnCCSapAlias = _IsdnCCSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 3),
    _IsdnCCSapAlias_Type()
)
isdnCCSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapAlias.setStatus("mandatory")


class _IsdnCCSapSwitchType_Type(Integer32):
    """Custom type isdnCCSapSwitchType based on Integer32"""
    defaultValue = 8

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
        *(("bri-1TR6", 2),
          ("bri-5ESS", 3),
          ("bri-CCITT", 4),
          ("bri-DMS100", 5),
          ("bri-KDD", 6),
          ("bri-NET3", 7),
          ("bri-NI1", 8),
          ("bri-NI2", 9),
          ("bri-NTT", 10),
          ("bri-TS013", 11),
          ("bri-VN", 12),
          ("unspecified", 1))
    )


_IsdnCCSapSwitchType_Type.__name__ = "Integer32"
_IsdnCCSapSwitchType_Object = MibTableColumn
isdnCCSapSwitchType = _IsdnCCSapSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 10),
    _IsdnCCSapSwitchType_Type()
)
isdnCCSapSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapSwitchType.setStatus("mandatory")


class _IsdnCCSapInitTerminal_Type(Integer32):
    """Custom type isdnCCSapInitTerminal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fit", 2),
          ("nit", 1))
    )


_IsdnCCSapInitTerminal_Type.__name__ = "Integer32"
_IsdnCCSapInitTerminal_Object = MibTableColumn
isdnCCSapInitTerminal = _IsdnCCSapInitTerminal_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 11),
    _IsdnCCSapInitTerminal_Type()
)
isdnCCSapInitTerminal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapInitTerminal.setStatus("mandatory")


class _IsdnCCSapDNRouting_Type(Integer32):
    """Custom type isdnCCSapDNRouting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IsdnCCSapDNRouting_Type.__name__ = "Integer32"
_IsdnCCSapDNRouting_Object = MibTableColumn
isdnCCSapDNRouting = _IsdnCCSapDNRouting_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 12),
    _IsdnCCSapDNRouting_Type()
)
isdnCCSapDNRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapDNRouting.setStatus("mandatory")


class _IsdnCCSapBearerRouting_Type(Integer32):
    """Custom type isdnCCSapBearerRouting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IsdnCCSapBearerRouting_Type.__name__ = "Integer32"
_IsdnCCSapBearerRouting_Object = MibTableColumn
isdnCCSapBearerRouting = _IsdnCCSapBearerRouting_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 13),
    _IsdnCCSapBearerRouting_Type()
)
isdnCCSapBearerRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapBearerRouting.setStatus("mandatory")


class _IsdnCCSapBearerType_Type(Integer32):
    """Custom type isdnCCSapBearerType based on Integer32"""
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
        *(("circuit-sw-data-call", 2),
          ("packet-sw-data-call", 3),
          ("voice-call", 1))
    )


_IsdnCCSapBearerType_Type.__name__ = "Integer32"
_IsdnCCSapBearerType_Object = MibTableColumn
isdnCCSapBearerType = _IsdnCCSapBearerType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 14),
    _IsdnCCSapBearerType_Type()
)
isdnCCSapBearerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapBearerType.setStatus("mandatory")
_IsdnCCSapDirectoryNumber_Type = DisplayString
_IsdnCCSapDirectoryNumber_Object = MibTableColumn
isdnCCSapDirectoryNumber = _IsdnCCSapDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 15),
    _IsdnCCSapDirectoryNumber_Type()
)
isdnCCSapDirectoryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapDirectoryNumber.setStatus("mandatory")
_IsdnCCSapSPID_Type = DisplayString
_IsdnCCSapSPID_Object = MibTableColumn
isdnCCSapSPID = _IsdnCCSapSPID_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 16),
    _IsdnCCSapSPID_Type()
)
isdnCCSapSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapSPID.setStatus("mandatory")
_IsdnCCSapSubAddress_Type = DisplayString
_IsdnCCSapSubAddress_Object = MibTableColumn
isdnCCSapSubAddress = _IsdnCCSapSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 17),
    _IsdnCCSapSubAddress_Type()
)
isdnCCSapSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapSubAddress.setStatus("mandatory")


class _IsdnCCSapT415Timer_Type(Integer32):
    """Custom type isdnCCSapT415Timer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnCCSapT415Timer_Type.__name__ = "Integer32"
_IsdnCCSapT415Timer_Object = MibTableColumn
isdnCCSapT415Timer = _IsdnCCSapT415Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 18),
    _IsdnCCSapT415Timer_Type()
)
isdnCCSapT415Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCCSapT415Timer.setStatus("mandatory")


class _IsdnCCSapStatusEvent_Type(Integer32):
    """Custom type isdnCCSapStatusEvent based on Integer32"""
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
        *(("badCes", 4),
          ("badCfgVersion", 2),
          ("badDslID", 3),
          ("badSwitchType", 5),
          ("cbPollErr", 6),
          ("dslInUseErr", 7),
          ("dslNotCfgErr", 8),
          ("dslNotInUse", 9),
          ("noEvent", 1),
          ("noHostCB", 10),
          ("noT415", 11))
    )


_IsdnCCSapStatusEvent_Type.__name__ = "Integer32"
_IsdnCCSapStatusEvent_Object = MibTableColumn
isdnCCSapStatusEvent = _IsdnCCSapStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 40),
    _IsdnCCSapStatusEvent_Type()
)
isdnCCSapStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCCSapStatusEvent.setStatus("mandatory")


class _IsdnCCSapInUse_Type(Integer32):
    """Custom type isdnCCSapInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IsdnCCSapInUse_Type.__name__ = "Integer32"
_IsdnCCSapInUse_Object = MibTableColumn
isdnCCSapInUse = _IsdnCCSapInUse_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 41),
    _IsdnCCSapInUse_Type()
)
isdnCCSapInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCCSapInUse.setStatus("mandatory")
_IsdnCCSapActiveCalls_Type = Counter32
_IsdnCCSapActiveCalls_Object = MibTableColumn
isdnCCSapActiveCalls = _IsdnCCSapActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 21, 1, 42),
    _IsdnCCSapActiveCalls_Type()
)
isdnCCSapActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCCSapActiveCalls.setStatus("mandatory")
_IsdnDebugTable_Object = MibTable
isdnDebugTable = _IsdnDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22)
)
if mibBuilder.loadTexts:
    isdnDebugTable.setStatus("mandatory")
_IsdnDebugEntry_Object = MibTableRow
isdnDebugEntry = _IsdnDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1)
)
isdnDebugEntry.setIndexNames(
    (0, "CXISDN-MIB", "isdnDebugNumber"),
)
if mibBuilder.loadTexts:
    isdnDebugEntry.setStatus("mandatory")
_IsdnDebugNumber_Type = SapIndex
_IsdnDebugNumber_Object = MibTableColumn
isdnDebugNumber = _IsdnDebugNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 1),
    _IsdnDebugNumber_Type()
)
isdnDebugNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDebugNumber.setStatus("mandatory")
_IsdnDebugCCB_Type = Integer32
_IsdnDebugCCB_Object = MibTableColumn
isdnDebugCCB = _IsdnDebugCCB_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 10),
    _IsdnDebugCCB_Type()
)
isdnDebugCCB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    isdnDebugCCB.setStatus("mandatory")
_IsdnDebugHCB_Type = Integer32
_IsdnDebugHCB_Object = MibTableColumn
isdnDebugHCB = _IsdnDebugHCB_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 11),
    _IsdnDebugHCB_Type()
)
isdnDebugHCB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    isdnDebugHCB.setStatus("mandatory")
_IsdnDebugCCDsl_Type = Integer32
_IsdnDebugCCDsl_Object = MibTableColumn
isdnDebugCCDsl = _IsdnDebugCCDsl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 12),
    _IsdnDebugCCDsl_Type()
)
isdnDebugCCDsl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    isdnDebugCCDsl.setStatus("mandatory")
_IsdnDebugNLCB_Type = Integer32
_IsdnDebugNLCB_Object = MibTableColumn
isdnDebugNLCB = _IsdnDebugNLCB_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 22, 1, 13),
    _IsdnDebugNLCB_Type()
)
isdnDebugNLCB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    isdnDebugNLCB.setStatus("mandatory")

# Managed Objects groups


# Notification objects

isdnL3SapStatusIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 0, 1)
)
isdnL3SapStatusIndication.setObjects(
      *(("CXISDN-MIB", "isdnL3SapNumber"),
        ("CXISDN-MIB", "isdnL3SapStatusEvent"))
)
if mibBuilder.loadTexts:
    isdnL3SapStatusIndication.setStatus(
        ""
    )

isdnCCSapStatusIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 32, 0, 2)
)
isdnCCSapStatusIndication.setObjects(
      *(("CXISDN-MIB", "isdnCCSapNumber"),
        ("CXISDN-MIB", "isdnCCSapStatusEvent"))
)
if mibBuilder.loadTexts:
    isdnCCSapStatusIndication.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXISDN-MIB",
    **{"isdnL3SapStatusIndication": isdnL3SapStatusIndication,
       "isdnCCSapStatusIndication": isdnCCSapStatusIndication,
       "isdnSoftwareVersion": isdnSoftwareVersion,
       "isdnTraps": isdnTraps,
       "isdnL3SapTable": isdnL3SapTable,
       "isdnL3SapEntry": isdnL3SapEntry,
       "isdnL3SapNumber": isdnL3SapNumber,
       "isdnL3SapRowStatus": isdnL3SapRowStatus,
       "isdnL3SapAlias": isdnL3SapAlias,
       "isdnL3SapCompanionAlias": isdnL3SapCompanionAlias,
       "isdnL3SapUserNetType": isdnL3SapUserNetType,
       "isdnL3SapT303Timer": isdnL3SapT303Timer,
       "isdnL3SapT304Timer": isdnL3SapT304Timer,
       "isdnL3SapT305Timer": isdnL3SapT305Timer,
       "isdnL3SapT308Timer": isdnL3SapT308Timer,
       "isdnL3SapT310Timer": isdnL3SapT310Timer,
       "isdnL3SapT313Timer": isdnL3SapT313Timer,
       "isdnL3SapT318Timer": isdnL3SapT318Timer,
       "isdnL3SapT319Timer": isdnL3SapT319Timer,
       "isdnL3SapDefTimerCfg": isdnL3SapDefTimerCfg,
       "isdnL3SapStatusEvent": isdnL3SapStatusEvent,
       "isdnL3SapDslType": isdnL3SapDslType,
       "isdnL3SapBRIType": isdnL3SapBRIType,
       "isdnCCSapTable": isdnCCSapTable,
       "isdnCCSapEntry": isdnCCSapEntry,
       "isdnCCSapNumber": isdnCCSapNumber,
       "isdnCCSapRowStatus": isdnCCSapRowStatus,
       "isdnCCSapAlias": isdnCCSapAlias,
       "isdnCCSapSwitchType": isdnCCSapSwitchType,
       "isdnCCSapInitTerminal": isdnCCSapInitTerminal,
       "isdnCCSapDNRouting": isdnCCSapDNRouting,
       "isdnCCSapBearerRouting": isdnCCSapBearerRouting,
       "isdnCCSapBearerType": isdnCCSapBearerType,
       "isdnCCSapDirectoryNumber": isdnCCSapDirectoryNumber,
       "isdnCCSapSPID": isdnCCSapSPID,
       "isdnCCSapSubAddress": isdnCCSapSubAddress,
       "isdnCCSapT415Timer": isdnCCSapT415Timer,
       "isdnCCSapStatusEvent": isdnCCSapStatusEvent,
       "isdnCCSapInUse": isdnCCSapInUse,
       "isdnCCSapActiveCalls": isdnCCSapActiveCalls,
       "isdnDebugTable": isdnDebugTable,
       "isdnDebugEntry": isdnDebugEntry,
       "isdnDebugNumber": isdnDebugNumber,
       "isdnDebugCCB": isdnDebugCCB,
       "isdnDebugHCB": isdnDebugHCB,
       "isdnDebugCCDsl": isdnDebugCCDsl,
       "isdnDebugNLCB": isdnDebugNLCB}
)
