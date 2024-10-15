# SNMP MIB module (Wellfleet-OC12-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-OC12-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:48 2024
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

_WfOc12ConfigTable_Object = MibTable
wfOc12ConfigTable = _WfOc12ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20)
)
if mibBuilder.loadTexts:
    wfOc12ConfigTable.setStatus("mandatory")
_WfOc12ConfigEntry_Object = MibTableRow
wfOc12ConfigEntry = _WfOc12ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1)
)
wfOc12ConfigEntry.setIndexNames(
    (0, "Wellfleet-OC12-MIB", "wfOc12ConfigIndex"),
)
if mibBuilder.loadTexts:
    wfOc12ConfigEntry.setStatus("mandatory")


class _WfOc12ConfigDelete_Type(Integer32):
    """Custom type wfOc12ConfigDelete based on Integer32"""
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


_WfOc12ConfigDelete_Type.__name__ = "Integer32"
_WfOc12ConfigDelete_Object = MibTableColumn
wfOc12ConfigDelete = _WfOc12ConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 1),
    _WfOc12ConfigDelete_Type()
)
wfOc12ConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc12ConfigDelete.setStatus("mandatory")


class _WfOc12ConfigDisable_Type(Integer32):
    """Custom type wfOc12ConfigDisable based on Integer32"""
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


_WfOc12ConfigDisable_Type.__name__ = "Integer32"
_WfOc12ConfigDisable_Object = MibTableColumn
wfOc12ConfigDisable = _WfOc12ConfigDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 2),
    _WfOc12ConfigDisable_Type()
)
wfOc12ConfigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc12ConfigDisable.setStatus("mandatory")
_WfOc12ConfigIndex_Type = Integer32
_WfOc12ConfigIndex_Object = MibTableColumn
wfOc12ConfigIndex = _WfOc12ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 3),
    _WfOc12ConfigIndex_Type()
)
wfOc12ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc12ConfigIndex.setStatus("mandatory")
_WfOc12ConfigIfIndex_Type = Integer32
_WfOc12ConfigIfIndex_Object = MibTableColumn
wfOc12ConfigIfIndex = _WfOc12ConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 4),
    _WfOc12ConfigIfIndex_Type()
)
wfOc12ConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc12ConfigIfIndex.setStatus("mandatory")


class _WfOc12ConfigState_Type(Integer32):
    """Custom type wfOc12ConfigState based on Integer32"""
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


_WfOc12ConfigState_Type.__name__ = "Integer32"
_WfOc12ConfigState_Object = MibTableColumn
wfOc12ConfigState = _WfOc12ConfigState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 5),
    _WfOc12ConfigState_Type()
)
wfOc12ConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc12ConfigState.setStatus("mandatory")


class _WfOc12ConfigLineStatus_Type(Integer32):
    """Custom type wfOc12ConfigLineStatus based on Integer32"""
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


_WfOc12ConfigLineStatus_Type.__name__ = "Integer32"
_WfOc12ConfigLineStatus_Object = MibTableColumn
wfOc12ConfigLineStatus = _WfOc12ConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 6),
    _WfOc12ConfigLineStatus_Type()
)
wfOc12ConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc12ConfigLineStatus.setStatus("mandatory")
_WfOc12ConfigLastChange_Type = TimeTicks
_WfOc12ConfigLastChange_Object = MibTableColumn
wfOc12ConfigLastChange = _WfOc12ConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 7),
    _WfOc12ConfigLastChange_Type()
)
wfOc12ConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc12ConfigLastChange.setStatus("mandatory")


class _WfOc12ConfigType_Type(Integer32):
    """Custom type wfOc12ConfigType based on Integer32"""
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


_WfOc12ConfigType_Type.__name__ = "Integer32"
_WfOc12ConfigType_Object = MibTableColumn
wfOc12ConfigType = _WfOc12ConfigType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 8),
    _WfOc12ConfigType_Type()
)
wfOc12ConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc12ConfigType.setStatus("mandatory")


class _WfOc12ConfigLineCoding_Type(Integer32):
    """Custom type wfOc12ConfigLineCoding based on Integer32"""
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


_WfOc12ConfigLineCoding_Type.__name__ = "Integer32"
_WfOc12ConfigLineCoding_Object = MibTableColumn
wfOc12ConfigLineCoding = _WfOc12ConfigLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 9),
    _WfOc12ConfigLineCoding_Type()
)
wfOc12ConfigLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc12ConfigLineCoding.setStatus("mandatory")


class _WfOc12ConfigLineType_Type(Integer32):
    """Custom type wfOc12ConfigLineType based on Integer32"""
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


_WfOc12ConfigLineType_Type.__name__ = "Integer32"
_WfOc12ConfigLineType_Object = MibTableColumn
wfOc12ConfigLineType = _WfOc12ConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 10),
    _WfOc12ConfigLineType_Type()
)
wfOc12ConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc12ConfigLineType.setStatus("mandatory")


class _WfOc12ConfigLoopbackConfig_Type(Integer32):
    """Custom type wfOc12ConfigLoopbackConfig based on Integer32"""
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
          ("payloadloop", 2))
    )


_WfOc12ConfigLoopbackConfig_Type.__name__ = "Integer32"
_WfOc12ConfigLoopbackConfig_Object = MibTableColumn
wfOc12ConfigLoopbackConfig = _WfOc12ConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 11),
    _WfOc12ConfigLoopbackConfig_Type()
)
wfOc12ConfigLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc12ConfigLoopbackConfig.setStatus("mandatory")


class _WfOc12ConfigManagerMethod_Type(Integer32):
    """Custom type wfOc12ConfigManagerMethod based on Integer32"""
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


_WfOc12ConfigManagerMethod_Type.__name__ = "Integer32"
_WfOc12ConfigManagerMethod_Object = MibTableColumn
wfOc12ConfigManagerMethod = _WfOc12ConfigManagerMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 20, 1, 12),
    _WfOc12ConfigManagerMethod_Type()
)
wfOc12ConfigManagerMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc12ConfigManagerMethod.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-OC12-MIB",
    **{"wfOc12ConfigTable": wfOc12ConfigTable,
       "wfOc12ConfigEntry": wfOc12ConfigEntry,
       "wfOc12ConfigDelete": wfOc12ConfigDelete,
       "wfOc12ConfigDisable": wfOc12ConfigDisable,
       "wfOc12ConfigIndex": wfOc12ConfigIndex,
       "wfOc12ConfigIfIndex": wfOc12ConfigIfIndex,
       "wfOc12ConfigState": wfOc12ConfigState,
       "wfOc12ConfigLineStatus": wfOc12ConfigLineStatus,
       "wfOc12ConfigLastChange": wfOc12ConfigLastChange,
       "wfOc12ConfigType": wfOc12ConfigType,
       "wfOc12ConfigLineCoding": wfOc12ConfigLineCoding,
       "wfOc12ConfigLineType": wfOc12ConfigLineType,
       "wfOc12ConfigLoopbackConfig": wfOc12ConfigLoopbackConfig,
       "wfOc12ConfigManagerMethod": wfOc12ConfigManagerMethod}
)
