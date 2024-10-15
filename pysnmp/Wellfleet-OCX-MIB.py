# SNMP MIB module (Wellfleet-OCX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-OCX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:50 2024
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

(wfSonetGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSonetGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfOcxConfigTable_Object = MibTable
wfOcxConfigTable = _WfOcxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21)
)
if mibBuilder.loadTexts:
    wfOcxConfigTable.setStatus("mandatory")
_WfOcxConfigEntry_Object = MibTableRow
wfOcxConfigEntry = _WfOcxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1)
)
wfOcxConfigEntry.setIndexNames(
    (0, "Wellfleet-OCX-MIB", "wfOcxConfigIndex"),
)
if mibBuilder.loadTexts:
    wfOcxConfigEntry.setStatus("mandatory")


class _WfOcxConfigDelete_Type(Integer32):
    """Custom type wfOcxConfigDelete based on Integer32"""
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


_WfOcxConfigDelete_Type.__name__ = "Integer32"
_WfOcxConfigDelete_Object = MibTableColumn
wfOcxConfigDelete = _WfOcxConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 1),
    _WfOcxConfigDelete_Type()
)
wfOcxConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigDelete.setStatus("mandatory")


class _WfOcxConfigDisable_Type(Integer32):
    """Custom type wfOcxConfigDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOcxConfigDisable_Type.__name__ = "Integer32"
_WfOcxConfigDisable_Object = MibTableColumn
wfOcxConfigDisable = _WfOcxConfigDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 2),
    _WfOcxConfigDisable_Type()
)
wfOcxConfigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigDisable.setStatus("mandatory")
_WfOcxConfigIndex_Type = Integer32
_WfOcxConfigIndex_Object = MibTableColumn
wfOcxConfigIndex = _WfOcxConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 3),
    _WfOcxConfigIndex_Type()
)
wfOcxConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOcxConfigIndex.setStatus("mandatory")
_WfOcxConfigIfIndex_Type = Integer32
_WfOcxConfigIfIndex_Object = MibTableColumn
wfOcxConfigIfIndex = _WfOcxConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 4),
    _WfOcxConfigIfIndex_Type()
)
wfOcxConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOcxConfigIfIndex.setStatus("mandatory")


class _WfOcxConfigState_Type(Integer32):
    """Custom type wfOcxConfigState based on Integer32"""
    defaultValue = 20

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
              20)
        )
    )
    namedValues = NamedValues(
        *(("ais", 5),
          ("down", 2),
          ("lof", 4),
          ("loopback", 7),
          ("los", 3),
          ("notpresent", 20),
          ("rdi", 6),
          ("up", 1))
    )


_WfOcxConfigState_Type.__name__ = "Integer32"
_WfOcxConfigState_Object = MibTableColumn
wfOcxConfigState = _WfOcxConfigState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 5),
    _WfOcxConfigState_Type()
)
wfOcxConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOcxConfigState.setStatus("mandatory")


class _WfOcxConfigLineStatus_Type(Integer32):
    """Custom type wfOcxConfigLineStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              128,
              512)
        )
    )
    namedValues = NamedValues(
        *(("ais", 8),
          ("lof", 4),
          ("loopback", 128),
          ("los", 2),
          ("noalarm", 1),
          ("otherfailure", 512),
          ("rdi", 16))
    )


_WfOcxConfigLineStatus_Type.__name__ = "Integer32"
_WfOcxConfigLineStatus_Object = MibTableColumn
wfOcxConfigLineStatus = _WfOcxConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 6),
    _WfOcxConfigLineStatus_Type()
)
wfOcxConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOcxConfigLineStatus.setStatus("mandatory")
_WfOcxConfigLastChange_Type = TimeTicks
_WfOcxConfigLastChange_Object = MibTableColumn
wfOcxConfigLastChange = _WfOcxConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 7),
    _WfOcxConfigLastChange_Type()
)
wfOcxConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOcxConfigLastChange.setStatus("mandatory")


class _WfOcxConfigConnType_Type(Integer32):
    """Custom type wfOcxConfigConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oc12", 2),
          ("oc3", 1),
          ("oc48", 3))
    )


_WfOcxConfigConnType_Type.__name__ = "Integer32"
_WfOcxConfigConnType_Object = MibTableColumn
wfOcxConfigConnType = _WfOcxConfigConnType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 8),
    _WfOcxConfigConnType_Type()
)
wfOcxConfigConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigConnType.setStatus("mandatory")


class _WfOcxConfigType_Type(Integer32):
    """Custom type wfOcxConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_WfOcxConfigType_Type.__name__ = "Integer32"
_WfOcxConfigType_Object = MibTableColumn
wfOcxConfigType = _WfOcxConfigType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 9),
    _WfOcxConfigType_Type()
)
wfOcxConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOcxConfigType.setStatus("mandatory")


class _WfOcxConfigLineCoding_Type(Integer32):
    """Custom type wfOcxConfigLineCoding based on Integer32"""
    defaultValue = 4

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
        *(("b3zs", 2),
          ("cmi", 3),
          ("nrz", 4),
          ("other", 1),
          ("rz", 5))
    )


_WfOcxConfigLineCoding_Type.__name__ = "Integer32"
_WfOcxConfigLineCoding_Object = MibTableColumn
wfOcxConfigLineCoding = _WfOcxConfigLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 10),
    _WfOcxConfigLineCoding_Type()
)
wfOcxConfigLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigLineCoding.setStatus("mandatory")


class _WfOcxConfigLineType_Type(Integer32):
    """Custom type wfOcxConfigLineType based on Integer32"""
    defaultValue = 2

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
        *(("coax", 5),
          ("longsinglemode", 3),
          ("multimode", 4),
          ("other", 1),
          ("shortsinglemode", 2),
          ("utp", 6))
    )


_WfOcxConfigLineType_Type.__name__ = "Integer32"
_WfOcxConfigLineType_Object = MibTableColumn
wfOcxConfigLineType = _WfOcxConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 11),
    _WfOcxConfigLineType_Type()
)
wfOcxConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigLineType.setStatus("mandatory")


class _WfOcxConfigLoopbackConfig_Type(Integer32):
    """Custom type wfOcxConfigLoopbackConfig based on Integer32"""
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
        *(("lineloop", 3),
          ("noloop", 1),
          ("selfloop", 2))
    )


_WfOcxConfigLoopbackConfig_Type.__name__ = "Integer32"
_WfOcxConfigLoopbackConfig_Object = MibTableColumn
wfOcxConfigLoopbackConfig = _WfOcxConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 12),
    _WfOcxConfigLoopbackConfig_Type()
)
wfOcxConfigLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigLoopbackConfig.setStatus("mandatory")


class _WfOcxConfigManagerMethod_Type(Integer32):
    """Custom type wfOcxConfigManagerMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("frac", 1))
    )


_WfOcxConfigManagerMethod_Type.__name__ = "Integer32"
_WfOcxConfigManagerMethod_Object = MibTableColumn
wfOcxConfigManagerMethod = _WfOcxConfigManagerMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 13),
    _WfOcxConfigManagerMethod_Type()
)
wfOcxConfigManagerMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigManagerMethod.setStatus("mandatory")


class _WfOcxConfigApsEnable_Type(Integer32):
    """Custom type wfOcxConfigApsEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfOcxConfigApsEnable_Type.__name__ = "Integer32"
_WfOcxConfigApsEnable_Object = MibTableColumn
wfOcxConfigApsEnable = _WfOcxConfigApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 14),
    _WfOcxConfigApsEnable_Type()
)
wfOcxConfigApsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigApsEnable.setStatus("mandatory")


class _WfOcxConfigScrambling_Type(Integer32):
    """Custom type wfOcxConfigScrambling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfOcxConfigScrambling_Type.__name__ = "Integer32"
_WfOcxConfigScrambling_Object = MibTableColumn
wfOcxConfigScrambling = _WfOcxConfigScrambling_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 15),
    _WfOcxConfigScrambling_Type()
)
wfOcxConfigScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigScrambling.setStatus("mandatory")


class _WfOcxConfigClkSource_Type(Integer32):
    """Custom type wfOcxConfigClkSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extrn", 2),
          ("intrn", 1))
    )


_WfOcxConfigClkSource_Type.__name__ = "Integer32"
_WfOcxConfigClkSource_Object = MibTableColumn
wfOcxConfigClkSource = _WfOcxConfigClkSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 21, 1, 16),
    _WfOcxConfigClkSource_Type()
)
wfOcxConfigClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOcxConfigClkSource.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-OCX-MIB",
    **{"wfOcxConfigTable": wfOcxConfigTable,
       "wfOcxConfigEntry": wfOcxConfigEntry,
       "wfOcxConfigDelete": wfOcxConfigDelete,
       "wfOcxConfigDisable": wfOcxConfigDisable,
       "wfOcxConfigIndex": wfOcxConfigIndex,
       "wfOcxConfigIfIndex": wfOcxConfigIfIndex,
       "wfOcxConfigState": wfOcxConfigState,
       "wfOcxConfigLineStatus": wfOcxConfigLineStatus,
       "wfOcxConfigLastChange": wfOcxConfigLastChange,
       "wfOcxConfigConnType": wfOcxConfigConnType,
       "wfOcxConfigType": wfOcxConfigType,
       "wfOcxConfigLineCoding": wfOcxConfigLineCoding,
       "wfOcxConfigLineType": wfOcxConfigLineType,
       "wfOcxConfigLoopbackConfig": wfOcxConfigLoopbackConfig,
       "wfOcxConfigManagerMethod": wfOcxConfigManagerMethod,
       "wfOcxConfigApsEnable": wfOcxConfigApsEnable,
       "wfOcxConfigScrambling": wfOcxConfigScrambling,
       "wfOcxConfigClkSource": wfOcxConfigClkSource}
)
