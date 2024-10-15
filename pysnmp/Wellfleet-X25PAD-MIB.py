# SNMP MIB module (Wellfleet-X25PAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-X25PAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:33 2024
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

(wfX25PadGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfX25PadGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfX25PadDefaultCfgTable_Object = MibTable
wfX25PadDefaultCfgTable = _WfX25PadDefaultCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1)
)
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgTable.setStatus("mandatory")
_WfX25PadDefaultCfgEntry_Object = MibTableRow
wfX25PadDefaultCfgEntry = _WfX25PadDefaultCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1)
)
wfX25PadDefaultCfgEntry.setIndexNames(
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadDefaultCfgSlot"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadDefaultCfgConnector"),
)
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgEntry.setStatus("mandatory")


class _WfX25PadDefaultCfgDelete_Type(Integer32):
    """Custom type wfX25PadDefaultCfgDelete based on Integer32"""
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


_WfX25PadDefaultCfgDelete_Type.__name__ = "Integer32"
_WfX25PadDefaultCfgDelete_Object = MibTableColumn
wfX25PadDefaultCfgDelete = _WfX25PadDefaultCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 1),
    _WfX25PadDefaultCfgDelete_Type()
)
wfX25PadDefaultCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgDelete.setStatus("mandatory")


class _WfX25PadDefaultCfgDisable_Type(Integer32):
    """Custom type wfX25PadDefaultCfgDisable based on Integer32"""
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


_WfX25PadDefaultCfgDisable_Type.__name__ = "Integer32"
_WfX25PadDefaultCfgDisable_Object = MibTableColumn
wfX25PadDefaultCfgDisable = _WfX25PadDefaultCfgDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 2),
    _WfX25PadDefaultCfgDisable_Type()
)
wfX25PadDefaultCfgDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgDisable.setStatus("mandatory")


class _WfX25PadDefaultCfgState_Type(Integer32):
    """Custom type wfX25PadDefaultCfgState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfX25PadDefaultCfgState_Type.__name__ = "Integer32"
_WfX25PadDefaultCfgState_Object = MibTableColumn
wfX25PadDefaultCfgState = _WfX25PadDefaultCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 3),
    _WfX25PadDefaultCfgState_Type()
)
wfX25PadDefaultCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgState.setStatus("mandatory")
_WfX25PadDefaultCfgSlot_Type = Integer32
_WfX25PadDefaultCfgSlot_Object = MibTableColumn
wfX25PadDefaultCfgSlot = _WfX25PadDefaultCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 4),
    _WfX25PadDefaultCfgSlot_Type()
)
wfX25PadDefaultCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgSlot.setStatus("mandatory")
_WfX25PadDefaultCfgConnector_Type = Integer32
_WfX25PadDefaultCfgConnector_Object = MibTableColumn
wfX25PadDefaultCfgConnector = _WfX25PadDefaultCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 5),
    _WfX25PadDefaultCfgConnector_Type()
)
wfX25PadDefaultCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgConnector.setStatus("mandatory")
_WfX25PadDefaultCfgCircuit_Type = Integer32
_WfX25PadDefaultCfgCircuit_Object = MibTableColumn
wfX25PadDefaultCfgCircuit = _WfX25PadDefaultCfgCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 6),
    _WfX25PadDefaultCfgCircuit_Type()
)
wfX25PadDefaultCfgCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgCircuit.setStatus("mandatory")


class _WfX25PadDefaultCfgX121Addr_Type(DisplayString):
    """Custom type wfX25PadDefaultCfgX121Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WfX25PadDefaultCfgX121Addr_Type.__name__ = "DisplayString"
_WfX25PadDefaultCfgX121Addr_Object = MibTableColumn
wfX25PadDefaultCfgX121Addr = _WfX25PadDefaultCfgX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 7),
    _WfX25PadDefaultCfgX121Addr_Type()
)
wfX25PadDefaultCfgX121Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgX121Addr.setStatus("mandatory")


class _WfX25PadDefaultCfgDNIC_Type(DisplayString):
    """Custom type wfX25PadDefaultCfgDNIC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_WfX25PadDefaultCfgDNIC_Type.__name__ = "DisplayString"
_WfX25PadDefaultCfgDNIC_Object = MibTableColumn
wfX25PadDefaultCfgDNIC = _WfX25PadDefaultCfgDNIC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 8),
    _WfX25PadDefaultCfgDNIC_Type()
)
wfX25PadDefaultCfgDNIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgDNIC.setStatus("mandatory")


class _WfX25PadDefaultCfgLenSubAddress_Type(Integer32):
    """Custom type wfX25PadDefaultCfgLenSubAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WfX25PadDefaultCfgLenSubAddress_Type.__name__ = "Integer32"
_WfX25PadDefaultCfgLenSubAddress_Object = MibTableColumn
wfX25PadDefaultCfgLenSubAddress = _WfX25PadDefaultCfgLenSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 9),
    _WfX25PadDefaultCfgLenSubAddress_Type()
)
wfX25PadDefaultCfgLenSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgLenSubAddress.setStatus("mandatory")


class _WfX25PadDefaultCfgLCNLow_Type(Integer32):
    """Custom type wfX25PadDefaultCfgLCNLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfX25PadDefaultCfgLCNLow_Type.__name__ = "Integer32"
_WfX25PadDefaultCfgLCNLow_Object = MibTableColumn
wfX25PadDefaultCfgLCNLow = _WfX25PadDefaultCfgLCNLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 10),
    _WfX25PadDefaultCfgLCNLow_Type()
)
wfX25PadDefaultCfgLCNLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgLCNLow.setStatus("mandatory")


class _WfX25PadDefaultCfgLCNHigh_Type(Integer32):
    """Custom type wfX25PadDefaultCfgLCNHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfX25PadDefaultCfgLCNHigh_Type.__name__ = "Integer32"
_WfX25PadDefaultCfgLCNHigh_Object = MibTableColumn
wfX25PadDefaultCfgLCNHigh = _WfX25PadDefaultCfgLCNHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 1, 1, 11),
    _WfX25PadDefaultCfgLCNHigh_Type()
)
wfX25PadDefaultCfgLCNHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadDefaultCfgLCNHigh.setStatus("mandatory")
_WfX25PadCurrentCfgTable_Object = MibTable
wfX25PadCurrentCfgTable = _WfX25PadCurrentCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2)
)
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgTable.setStatus("mandatory")
_WfX25PadCurrentCfgEntry_Object = MibTableRow
wfX25PadCurrentCfgEntry = _WfX25PadCurrentCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1)
)
wfX25PadCurrentCfgEntry.setIndexNames(
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadCurrentCfgSlot"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadCurrentCfgConnector"),
)
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgEntry.setStatus("mandatory")


class _WfX25PadCurrentCfgState_Type(Integer32):
    """Custom type wfX25PadCurrentCfgState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfX25PadCurrentCfgState_Type.__name__ = "Integer32"
_WfX25PadCurrentCfgState_Object = MibTableColumn
wfX25PadCurrentCfgState = _WfX25PadCurrentCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 1),
    _WfX25PadCurrentCfgState_Type()
)
wfX25PadCurrentCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgState.setStatus("mandatory")
_WfX25PadCurrentCfgSlot_Type = Integer32
_WfX25PadCurrentCfgSlot_Object = MibTableColumn
wfX25PadCurrentCfgSlot = _WfX25PadCurrentCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 2),
    _WfX25PadCurrentCfgSlot_Type()
)
wfX25PadCurrentCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgSlot.setStatus("mandatory")
_WfX25PadCurrentCfgConnector_Type = Integer32
_WfX25PadCurrentCfgConnector_Object = MibTableColumn
wfX25PadCurrentCfgConnector = _WfX25PadCurrentCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 3),
    _WfX25PadCurrentCfgConnector_Type()
)
wfX25PadCurrentCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgConnector.setStatus("mandatory")
_WfX25PadCurrentCfgCircuit_Type = Integer32
_WfX25PadCurrentCfgCircuit_Object = MibTableColumn
wfX25PadCurrentCfgCircuit = _WfX25PadCurrentCfgCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 4),
    _WfX25PadCurrentCfgCircuit_Type()
)
wfX25PadCurrentCfgCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgCircuit.setStatus("mandatory")


class _WfX25PadCurrentCfgX121Addr_Type(DisplayString):
    """Custom type wfX25PadCurrentCfgX121Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WfX25PadCurrentCfgX121Addr_Type.__name__ = "DisplayString"
_WfX25PadCurrentCfgX121Addr_Object = MibTableColumn
wfX25PadCurrentCfgX121Addr = _WfX25PadCurrentCfgX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 5),
    _WfX25PadCurrentCfgX121Addr_Type()
)
wfX25PadCurrentCfgX121Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgX121Addr.setStatus("mandatory")


class _WfX25PadCurrentCfgDNIC_Type(DisplayString):
    """Custom type wfX25PadCurrentCfgDNIC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_WfX25PadCurrentCfgDNIC_Type.__name__ = "DisplayString"
_WfX25PadCurrentCfgDNIC_Object = MibTableColumn
wfX25PadCurrentCfgDNIC = _WfX25PadCurrentCfgDNIC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 6),
    _WfX25PadCurrentCfgDNIC_Type()
)
wfX25PadCurrentCfgDNIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgDNIC.setStatus("mandatory")


class _WfX25PadCurrentCfgLenSubAddress_Type(Integer32):
    """Custom type wfX25PadCurrentCfgLenSubAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WfX25PadCurrentCfgLenSubAddress_Type.__name__ = "Integer32"
_WfX25PadCurrentCfgLenSubAddress_Object = MibTableColumn
wfX25PadCurrentCfgLenSubAddress = _WfX25PadCurrentCfgLenSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 7),
    _WfX25PadCurrentCfgLenSubAddress_Type()
)
wfX25PadCurrentCfgLenSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgLenSubAddress.setStatus("mandatory")


class _WfX25PadCurrentCfgLCNLow_Type(Integer32):
    """Custom type wfX25PadCurrentCfgLCNLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfX25PadCurrentCfgLCNLow_Type.__name__ = "Integer32"
_WfX25PadCurrentCfgLCNLow_Object = MibTableColumn
wfX25PadCurrentCfgLCNLow = _WfX25PadCurrentCfgLCNLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 8),
    _WfX25PadCurrentCfgLCNLow_Type()
)
wfX25PadCurrentCfgLCNLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgLCNLow.setStatus("mandatory")


class _WfX25PadCurrentCfgLCNHigh_Type(Integer32):
    """Custom type wfX25PadCurrentCfgLCNHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfX25PadCurrentCfgLCNHigh_Type.__name__ = "Integer32"
_WfX25PadCurrentCfgLCNHigh_Object = MibTableColumn
wfX25PadCurrentCfgLCNHigh = _WfX25PadCurrentCfgLCNHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 2, 1, 9),
    _WfX25PadCurrentCfgLCNHigh_Type()
)
wfX25PadCurrentCfgLCNHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadCurrentCfgLCNHigh.setStatus("mandatory")
_WfX25PadStatTable_Object = MibTable
wfX25PadStatTable = _WfX25PadStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3)
)
if mibBuilder.loadTexts:
    wfX25PadStatTable.setStatus("mandatory")
_WfX25PadStatEntry_Object = MibTableRow
wfX25PadStatEntry = _WfX25PadStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1)
)
wfX25PadStatEntry.setIndexNames(
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadStatSlot"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadStatConnector"),
)
if mibBuilder.loadTexts:
    wfX25PadStatEntry.setStatus("mandatory")


class _WfX25PadStatState_Type(Integer32):
    """Custom type wfX25PadStatState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfX25PadStatState_Type.__name__ = "Integer32"
_WfX25PadStatState_Object = MibTableColumn
wfX25PadStatState = _WfX25PadStatState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 1),
    _WfX25PadStatState_Type()
)
wfX25PadStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatState.setStatus("mandatory")
_WfX25PadStatSlot_Type = Integer32
_WfX25PadStatSlot_Object = MibTableColumn
wfX25PadStatSlot = _WfX25PadStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 2),
    _WfX25PadStatSlot_Type()
)
wfX25PadStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatSlot.setStatus("mandatory")
_WfX25PadStatConnector_Type = Integer32
_WfX25PadStatConnector_Object = MibTableColumn
wfX25PadStatConnector = _WfX25PadStatConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 3),
    _WfX25PadStatConnector_Type()
)
wfX25PadStatConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatConnector.setStatus("mandatory")
_WfX25PadStatTotalConnCount_Type = Counter32
_WfX25PadStatTotalConnCount_Object = MibTableColumn
wfX25PadStatTotalConnCount = _WfX25PadStatTotalConnCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 4),
    _WfX25PadStatTotalConnCount_Type()
)
wfX25PadStatTotalConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatTotalConnCount.setStatus("mandatory")
_WfX25PadStatRxRR_Type = Counter32
_WfX25PadStatRxRR_Object = MibTableColumn
wfX25PadStatRxRR = _WfX25PadStatRxRR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 5),
    _WfX25PadStatRxRR_Type()
)
wfX25PadStatRxRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatRxRR.setStatus("mandatory")
_WfX25PadStatTxRR_Type = Counter32
_WfX25PadStatTxRR_Object = MibTableColumn
wfX25PadStatTxRR = _WfX25PadStatTxRR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 6),
    _WfX25PadStatTxRR_Type()
)
wfX25PadStatTxRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatTxRR.setStatus("mandatory")
_WfX25PadStatRxRNR_Type = Counter32
_WfX25PadStatRxRNR_Object = MibTableColumn
wfX25PadStatRxRNR = _WfX25PadStatRxRNR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 7),
    _WfX25PadStatRxRNR_Type()
)
wfX25PadStatRxRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatRxRNR.setStatus("mandatory")
_WfX25PadStatTxRNR_Type = Counter32
_WfX25PadStatTxRNR_Object = MibTableColumn
wfX25PadStatTxRNR = _WfX25PadStatTxRNR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 8),
    _WfX25PadStatTxRNR_Type()
)
wfX25PadStatTxRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatTxRNR.setStatus("mandatory")
_WfX25PadStatRxRestart_Type = Counter32
_WfX25PadStatRxRestart_Object = MibTableColumn
wfX25PadStatRxRestart = _WfX25PadStatRxRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 9),
    _WfX25PadStatRxRestart_Type()
)
wfX25PadStatRxRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatRxRestart.setStatus("mandatory")
_WfX25PadStatTxRestart_Type = Counter32
_WfX25PadStatTxRestart_Object = MibTableColumn
wfX25PadStatTxRestart = _WfX25PadStatTxRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 3, 1, 10),
    _WfX25PadStatTxRestart_Type()
)
wfX25PadStatTxRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadStatTxRestart.setStatus("mandatory")
_WfX25PadPortDefaultCfgTable_Object = MibTable
wfX25PadPortDefaultCfgTable = _WfX25PadPortDefaultCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4)
)
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgTable.setStatus("mandatory")
_WfX25PadPortDefaultCfgEntry_Object = MibTableRow
wfX25PadPortDefaultCfgEntry = _WfX25PadPortDefaultCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1)
)
wfX25PadPortDefaultCfgEntry.setIndexNames(
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortDefaultCfgSlot"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortDefaultCfgConnector"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortDefaultCfgNumber"),
)
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgEntry.setStatus("mandatory")


class _WfX25PadPortDefaultCfgDelete_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgDelete based on Integer32"""
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


_WfX25PadPortDefaultCfgDelete_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgDelete_Object = MibTableColumn
wfX25PadPortDefaultCfgDelete = _WfX25PadPortDefaultCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 1),
    _WfX25PadPortDefaultCfgDelete_Type()
)
wfX25PadPortDefaultCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgDelete.setStatus("mandatory")


class _WfX25PadPortDefaultCfgDisable_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgDisable based on Integer32"""
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


_WfX25PadPortDefaultCfgDisable_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgDisable_Object = MibTableColumn
wfX25PadPortDefaultCfgDisable = _WfX25PadPortDefaultCfgDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 2),
    _WfX25PadPortDefaultCfgDisable_Type()
)
wfX25PadPortDefaultCfgDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgDisable.setStatus("mandatory")


class _WfX25PadPortDefaultCfgState_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfX25PadPortDefaultCfgState_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgState_Object = MibTableColumn
wfX25PadPortDefaultCfgState = _WfX25PadPortDefaultCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 3),
    _WfX25PadPortDefaultCfgState_Type()
)
wfX25PadPortDefaultCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgState.setStatus("mandatory")
_WfX25PadPortDefaultCfgSlot_Type = Integer32
_WfX25PadPortDefaultCfgSlot_Object = MibTableColumn
wfX25PadPortDefaultCfgSlot = _WfX25PadPortDefaultCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 4),
    _WfX25PadPortDefaultCfgSlot_Type()
)
wfX25PadPortDefaultCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgSlot.setStatus("mandatory")
_WfX25PadPortDefaultCfgConnector_Type = Integer32
_WfX25PadPortDefaultCfgConnector_Object = MibTableColumn
wfX25PadPortDefaultCfgConnector = _WfX25PadPortDefaultCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 5),
    _WfX25PadPortDefaultCfgConnector_Type()
)
wfX25PadPortDefaultCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgConnector.setStatus("mandatory")
_WfX25PadPortDefaultCfgNumber_Type = Integer32
_WfX25PadPortDefaultCfgNumber_Object = MibTableColumn
wfX25PadPortDefaultCfgNumber = _WfX25PadPortDefaultCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 6),
    _WfX25PadPortDefaultCfgNumber_Type()
)
wfX25PadPortDefaultCfgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgNumber.setStatus("mandatory")


class _WfX25PadPortDefaultCfgSubAddress_Type(DisplayString):
    """Custom type wfX25PadPortDefaultCfgSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WfX25PadPortDefaultCfgSubAddress_Type.__name__ = "DisplayString"
_WfX25PadPortDefaultCfgSubAddress_Object = MibTableColumn
wfX25PadPortDefaultCfgSubAddress = _WfX25PadPortDefaultCfgSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 7),
    _WfX25PadPortDefaultCfgSubAddress_Type()
)
wfX25PadPortDefaultCfgSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgSubAddress.setStatus("mandatory")


class _WfX25PadPortDefaultCfgLenSubAddress_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgLenSubAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WfX25PadPortDefaultCfgLenSubAddress_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgLenSubAddress_Object = MibTableColumn
wfX25PadPortDefaultCfgLenSubAddress = _WfX25PadPortDefaultCfgLenSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 8),
    _WfX25PadPortDefaultCfgLenSubAddress_Type()
)
wfX25PadPortDefaultCfgLenSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgLenSubAddress.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3escape_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3escape based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WfX25PadPortDefaultCfgX3escape_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3escape_Object = MibTableColumn
wfX25PadPortDefaultCfgX3escape = _WfX25PadPortDefaultCfgX3escape_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 9),
    _WfX25PadPortDefaultCfgX3escape_Type()
)
wfX25PadPortDefaultCfgX3escape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3escape.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3echo_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3echo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WfX25PadPortDefaultCfgX3echo_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3echo_Object = MibTableColumn
wfX25PadPortDefaultCfgX3echo = _WfX25PadPortDefaultCfgX3echo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 10),
    _WfX25PadPortDefaultCfgX3echo_Type()
)
wfX25PadPortDefaultCfgX3echo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3echo.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3forward_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3forward based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WfX25PadPortDefaultCfgX3forward_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3forward_Object = MibTableColumn
wfX25PadPortDefaultCfgX3forward = _WfX25PadPortDefaultCfgX3forward_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 11),
    _WfX25PadPortDefaultCfgX3forward_Type()
)
wfX25PadPortDefaultCfgX3forward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3forward.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3idle_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3idle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortDefaultCfgX3idle_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3idle_Object = MibTableColumn
wfX25PadPortDefaultCfgX3idle = _WfX25PadPortDefaultCfgX3idle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 12),
    _WfX25PadPortDefaultCfgX3idle_Type()
)
wfX25PadPortDefaultCfgX3idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3idle.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3device_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3device based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WfX25PadPortDefaultCfgX3device_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3device_Object = MibTableColumn
wfX25PadPortDefaultCfgX3device = _WfX25PadPortDefaultCfgX3device_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 13),
    _WfX25PadPortDefaultCfgX3device_Type()
)
wfX25PadPortDefaultCfgX3device.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3device.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3signals_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3signals based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WfX25PadPortDefaultCfgX3signals_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3signals_Object = MibTableColumn
wfX25PadPortDefaultCfgX3signals = _WfX25PadPortDefaultCfgX3signals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 14),
    _WfX25PadPortDefaultCfgX3signals_Type()
)
wfX25PadPortDefaultCfgX3signals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3signals.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3break_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3break based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_WfX25PadPortDefaultCfgX3break_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3break_Object = MibTableColumn
wfX25PadPortDefaultCfgX3break = _WfX25PadPortDefaultCfgX3break_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 15),
    _WfX25PadPortDefaultCfgX3break_Type()
)
wfX25PadPortDefaultCfgX3break.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3break.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3discard_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3discard based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfX25PadPortDefaultCfgX3discard_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3discard_Object = MibTableColumn
wfX25PadPortDefaultCfgX3discard = _WfX25PadPortDefaultCfgX3discard_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 16),
    _WfX25PadPortDefaultCfgX3discard_Type()
)
wfX25PadPortDefaultCfgX3discard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3discard.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3CRpad_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3CRpad based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortDefaultCfgX3CRpad_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3CRpad_Object = MibTableColumn
wfX25PadPortDefaultCfgX3CRpad = _WfX25PadPortDefaultCfgX3CRpad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 17),
    _WfX25PadPortDefaultCfgX3CRpad_Type()
)
wfX25PadPortDefaultCfgX3CRpad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3CRpad.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3folding_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3folding based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortDefaultCfgX3folding_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3folding_Object = MibTableColumn
wfX25PadPortDefaultCfgX3folding = _WfX25PadPortDefaultCfgX3folding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 18),
    _WfX25PadPortDefaultCfgX3folding_Type()
)
wfX25PadPortDefaultCfgX3folding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3folding.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3speed_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3speed based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_WfX25PadPortDefaultCfgX3speed_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3speed_Object = MibTableColumn
wfX25PadPortDefaultCfgX3speed = _WfX25PadPortDefaultCfgX3speed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 19),
    _WfX25PadPortDefaultCfgX3speed_Type()
)
wfX25PadPortDefaultCfgX3speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3speed.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3flow_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3flow based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfX25PadPortDefaultCfgX3flow_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3flow_Object = MibTableColumn
wfX25PadPortDefaultCfgX3flow = _WfX25PadPortDefaultCfgX3flow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 20),
    _WfX25PadPortDefaultCfgX3flow_Type()
)
wfX25PadPortDefaultCfgX3flow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3flow.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3LFinsert_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3LFinsert based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WfX25PadPortDefaultCfgX3LFinsert_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3LFinsert_Object = MibTableColumn
wfX25PadPortDefaultCfgX3LFinsert = _WfX25PadPortDefaultCfgX3LFinsert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 21),
    _WfX25PadPortDefaultCfgX3LFinsert_Type()
)
wfX25PadPortDefaultCfgX3LFinsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3LFinsert.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3LFpad_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3LFpad based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortDefaultCfgX3LFpad_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3LFpad_Object = MibTableColumn
wfX25PadPortDefaultCfgX3LFpad = _WfX25PadPortDefaultCfgX3LFpad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 22),
    _WfX25PadPortDefaultCfgX3LFpad_Type()
)
wfX25PadPortDefaultCfgX3LFpad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3LFpad.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3Edit_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3Edit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfX25PadPortDefaultCfgX3Edit_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3Edit_Object = MibTableColumn
wfX25PadPortDefaultCfgX3Edit = _WfX25PadPortDefaultCfgX3Edit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 23),
    _WfX25PadPortDefaultCfgX3Edit_Type()
)
wfX25PadPortDefaultCfgX3Edit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3Edit.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3Cdelete_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3Cdelete based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfX25PadPortDefaultCfgX3Cdelete_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3Cdelete_Object = MibTableColumn
wfX25PadPortDefaultCfgX3Cdelete = _WfX25PadPortDefaultCfgX3Cdelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 24),
    _WfX25PadPortDefaultCfgX3Cdelete_Type()
)
wfX25PadPortDefaultCfgX3Cdelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3Cdelete.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3Ldelete_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3Ldelete based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfX25PadPortDefaultCfgX3Ldelete_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3Ldelete_Object = MibTableColumn
wfX25PadPortDefaultCfgX3Ldelete = _WfX25PadPortDefaultCfgX3Ldelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 25),
    _WfX25PadPortDefaultCfgX3Ldelete_Type()
)
wfX25PadPortDefaultCfgX3Ldelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3Ldelete.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3Ldisplay_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3Ldisplay based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfX25PadPortDefaultCfgX3Ldisplay_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3Ldisplay_Object = MibTableColumn
wfX25PadPortDefaultCfgX3Ldisplay = _WfX25PadPortDefaultCfgX3Ldisplay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 26),
    _WfX25PadPortDefaultCfgX3Ldisplay_Type()
)
wfX25PadPortDefaultCfgX3Ldisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3Ldisplay.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3Esignals_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3Esignals based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WfX25PadPortDefaultCfgX3Esignals_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3Esignals_Object = MibTableColumn
wfX25PadPortDefaultCfgX3Esignals = _WfX25PadPortDefaultCfgX3Esignals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 27),
    _WfX25PadPortDefaultCfgX3Esignals_Type()
)
wfX25PadPortDefaultCfgX3Esignals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3Esignals.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3Mask_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3Mask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortDefaultCfgX3Mask_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3Mask_Object = MibTableColumn
wfX25PadPortDefaultCfgX3Mask = _WfX25PadPortDefaultCfgX3Mask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 28),
    _WfX25PadPortDefaultCfgX3Mask_Type()
)
wfX25PadPortDefaultCfgX3Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3Mask.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3parity_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3parity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WfX25PadPortDefaultCfgX3parity_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3parity_Object = MibTableColumn
wfX25PadPortDefaultCfgX3parity = _WfX25PadPortDefaultCfgX3parity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 29),
    _WfX25PadPortDefaultCfgX3parity_Type()
)
wfX25PadPortDefaultCfgX3parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3parity.setStatus("mandatory")


class _WfX25PadPortDefaultCfgX3page_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgX3page based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortDefaultCfgX3page_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgX3page_Object = MibTableColumn
wfX25PadPortDefaultCfgX3page = _WfX25PadPortDefaultCfgX3page_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 30),
    _WfX25PadPortDefaultCfgX3page_Type()
)
wfX25PadPortDefaultCfgX3page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgX3page.setStatus("mandatory")


class _WfX25PadPortDefaultCfgLenUserData_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgLenUserData based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfX25PadPortDefaultCfgLenUserData_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgLenUserData_Object = MibTableColumn
wfX25PadPortDefaultCfgLenUserData = _WfX25PadPortDefaultCfgLenUserData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 31),
    _WfX25PadPortDefaultCfgLenUserData_Type()
)
wfX25PadPortDefaultCfgLenUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgLenUserData.setStatus("mandatory")


class _WfX25PadPortDefaultCfgUserData_Type(OctetString):
    """Custom type wfX25PadPortDefaultCfgUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WfX25PadPortDefaultCfgUserData_Type.__name__ = "OctetString"
_WfX25PadPortDefaultCfgUserData_Object = MibTableColumn
wfX25PadPortDefaultCfgUserData = _WfX25PadPortDefaultCfgUserData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 32),
    _WfX25PadPortDefaultCfgUserData_Type()
)
wfX25PadPortDefaultCfgUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgUserData.setStatus("mandatory")


class _WfX25PadPortDefaultCfgLenRawFacilities_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgLenRawFacilities based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WfX25PadPortDefaultCfgLenRawFacilities_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgLenRawFacilities_Object = MibTableColumn
wfX25PadPortDefaultCfgLenRawFacilities = _WfX25PadPortDefaultCfgLenRawFacilities_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 33),
    _WfX25PadPortDefaultCfgLenRawFacilities_Type()
)
wfX25PadPortDefaultCfgLenRawFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgLenRawFacilities.setStatus("mandatory")


class _WfX25PadPortDefaultCfgRawFacilitiesData_Type(OctetString):
    """Custom type wfX25PadPortDefaultCfgRawFacilitiesData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_WfX25PadPortDefaultCfgRawFacilitiesData_Type.__name__ = "OctetString"
_WfX25PadPortDefaultCfgRawFacilitiesData_Object = MibTableColumn
wfX25PadPortDefaultCfgRawFacilitiesData = _WfX25PadPortDefaultCfgRawFacilitiesData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 34),
    _WfX25PadPortDefaultCfgRawFacilitiesData_Type()
)
wfX25PadPortDefaultCfgRawFacilitiesData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgRawFacilitiesData.setStatus("mandatory")


class _WfX25PadPortDefaultCfgReverseCharge_Type(OctetString):
    """Custom type wfX25PadPortDefaultCfgReverseCharge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_WfX25PadPortDefaultCfgReverseCharge_Type.__name__ = "OctetString"
_WfX25PadPortDefaultCfgReverseCharge_Object = MibTableColumn
wfX25PadPortDefaultCfgReverseCharge = _WfX25PadPortDefaultCfgReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 35),
    _WfX25PadPortDefaultCfgReverseCharge_Type()
)
wfX25PadPortDefaultCfgReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgReverseCharge.setStatus("mandatory")


class _WfX25PadPortDefaultCfgThruClassNegotiation_Type(OctetString):
    """Custom type wfX25PadPortDefaultCfgThruClassNegotiation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_WfX25PadPortDefaultCfgThruClassNegotiation_Type.__name__ = "OctetString"
_WfX25PadPortDefaultCfgThruClassNegotiation_Object = MibTableColumn
wfX25PadPortDefaultCfgThruClassNegotiation = _WfX25PadPortDefaultCfgThruClassNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 36),
    _WfX25PadPortDefaultCfgThruClassNegotiation_Type()
)
wfX25PadPortDefaultCfgThruClassNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgThruClassNegotiation.setStatus("mandatory")


class _WfX25PadPortDefaultCfgPacketSizeNegotiation_Type(OctetString):
    """Custom type wfX25PadPortDefaultCfgPacketSizeNegotiation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_WfX25PadPortDefaultCfgPacketSizeNegotiation_Type.__name__ = "OctetString"
_WfX25PadPortDefaultCfgPacketSizeNegotiation_Object = MibTableColumn
wfX25PadPortDefaultCfgPacketSizeNegotiation = _WfX25PadPortDefaultCfgPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 37),
    _WfX25PadPortDefaultCfgPacketSizeNegotiation_Type()
)
wfX25PadPortDefaultCfgPacketSizeNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgPacketSizeNegotiation.setStatus("mandatory")


class _WfX25PadPortDefaultCfgWindowSizeNegotiation_Type(OctetString):
    """Custom type wfX25PadPortDefaultCfgWindowSizeNegotiation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_WfX25PadPortDefaultCfgWindowSizeNegotiation_Type.__name__ = "OctetString"
_WfX25PadPortDefaultCfgWindowSizeNegotiation_Object = MibTableColumn
wfX25PadPortDefaultCfgWindowSizeNegotiation = _WfX25PadPortDefaultCfgWindowSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 38),
    _WfX25PadPortDefaultCfgWindowSizeNegotiation_Type()
)
wfX25PadPortDefaultCfgWindowSizeNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgWindowSizeNegotiation.setStatus("mandatory")


class _WfX25PadPortDefaultCfgIntervalTimer_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgIntervalTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WfX25PadPortDefaultCfgIntervalTimer_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgIntervalTimer_Object = MibTableColumn
wfX25PadPortDefaultCfgIntervalTimer = _WfX25PadPortDefaultCfgIntervalTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 39),
    _WfX25PadPortDefaultCfgIntervalTimer_Type()
)
wfX25PadPortDefaultCfgIntervalTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgIntervalTimer.setStatus("mandatory")


class _WfX25PadPortDefaultCfgFullAddressing_Type(Integer32):
    """Custom type wfX25PadPortDefaultCfgFullAddressing based on Integer32"""
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


_WfX25PadPortDefaultCfgFullAddressing_Type.__name__ = "Integer32"
_WfX25PadPortDefaultCfgFullAddressing_Object = MibTableColumn
wfX25PadPortDefaultCfgFullAddressing = _WfX25PadPortDefaultCfgFullAddressing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 4, 1, 40),
    _WfX25PadPortDefaultCfgFullAddressing_Type()
)
wfX25PadPortDefaultCfgFullAddressing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortDefaultCfgFullAddressing.setStatus("mandatory")
_WfX25PadPortCurrentCfgTable_Object = MibTable
wfX25PadPortCurrentCfgTable = _WfX25PadPortCurrentCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5)
)
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgTable.setStatus("mandatory")
_WfX25PadPortCurrentCfgEntry_Object = MibTableRow
wfX25PadPortCurrentCfgEntry = _WfX25PadPortCurrentCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1)
)
wfX25PadPortCurrentCfgEntry.setIndexNames(
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortCurrentCfgSlot"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortCurrentCfgConnector"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortCurrentCfgNumber"),
)
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgEntry.setStatus("mandatory")


class _WfX25PadPortCurrentCfgState_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfX25PadPortCurrentCfgState_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgState_Object = MibTableColumn
wfX25PadPortCurrentCfgState = _WfX25PadPortCurrentCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 1),
    _WfX25PadPortCurrentCfgState_Type()
)
wfX25PadPortCurrentCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgState.setStatus("mandatory")
_WfX25PadPortCurrentCfgSlot_Type = Integer32
_WfX25PadPortCurrentCfgSlot_Object = MibTableColumn
wfX25PadPortCurrentCfgSlot = _WfX25PadPortCurrentCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 2),
    _WfX25PadPortCurrentCfgSlot_Type()
)
wfX25PadPortCurrentCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgSlot.setStatus("mandatory")
_WfX25PadPortCurrentCfgConnector_Type = Integer32
_WfX25PadPortCurrentCfgConnector_Object = MibTableColumn
wfX25PadPortCurrentCfgConnector = _WfX25PadPortCurrentCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 3),
    _WfX25PadPortCurrentCfgConnector_Type()
)
wfX25PadPortCurrentCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgConnector.setStatus("mandatory")
_WfX25PadPortCurrentCfgNumber_Type = Integer32
_WfX25PadPortCurrentCfgNumber_Object = MibTableColumn
wfX25PadPortCurrentCfgNumber = _WfX25PadPortCurrentCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 4),
    _WfX25PadPortCurrentCfgNumber_Type()
)
wfX25PadPortCurrentCfgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgNumber.setStatus("mandatory")


class _WfX25PadPortCurrentCfgSubAddress_Type(DisplayString):
    """Custom type wfX25PadPortCurrentCfgSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WfX25PadPortCurrentCfgSubAddress_Type.__name__ = "DisplayString"
_WfX25PadPortCurrentCfgSubAddress_Object = MibTableColumn
wfX25PadPortCurrentCfgSubAddress = _WfX25PadPortCurrentCfgSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 5),
    _WfX25PadPortCurrentCfgSubAddress_Type()
)
wfX25PadPortCurrentCfgSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgSubAddress.setStatus("mandatory")


class _WfX25PadPortCurrentCfgLenSubAddress_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgLenSubAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WfX25PadPortCurrentCfgLenSubAddress_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgLenSubAddress_Object = MibTableColumn
wfX25PadPortCurrentCfgLenSubAddress = _WfX25PadPortCurrentCfgLenSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 6),
    _WfX25PadPortCurrentCfgLenSubAddress_Type()
)
wfX25PadPortCurrentCfgLenSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgLenSubAddress.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3escape_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3escape based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WfX25PadPortCurrentCfgX3escape_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3escape_Object = MibTableColumn
wfX25PadPortCurrentCfgX3escape = _WfX25PadPortCurrentCfgX3escape_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 7),
    _WfX25PadPortCurrentCfgX3escape_Type()
)
wfX25PadPortCurrentCfgX3escape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3escape.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3echo_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3echo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WfX25PadPortCurrentCfgX3echo_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3echo_Object = MibTableColumn
wfX25PadPortCurrentCfgX3echo = _WfX25PadPortCurrentCfgX3echo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 8),
    _WfX25PadPortCurrentCfgX3echo_Type()
)
wfX25PadPortCurrentCfgX3echo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3echo.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3forward_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3forward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WfX25PadPortCurrentCfgX3forward_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3forward_Object = MibTableColumn
wfX25PadPortCurrentCfgX3forward = _WfX25PadPortCurrentCfgX3forward_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 9),
    _WfX25PadPortCurrentCfgX3forward_Type()
)
wfX25PadPortCurrentCfgX3forward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3forward.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3idle_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3idle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortCurrentCfgX3idle_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3idle_Object = MibTableColumn
wfX25PadPortCurrentCfgX3idle = _WfX25PadPortCurrentCfgX3idle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 10),
    _WfX25PadPortCurrentCfgX3idle_Type()
)
wfX25PadPortCurrentCfgX3idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3idle.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3device_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3device based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WfX25PadPortCurrentCfgX3device_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3device_Object = MibTableColumn
wfX25PadPortCurrentCfgX3device = _WfX25PadPortCurrentCfgX3device_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 11),
    _WfX25PadPortCurrentCfgX3device_Type()
)
wfX25PadPortCurrentCfgX3device.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3device.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3signals_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3signals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_WfX25PadPortCurrentCfgX3signals_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3signals_Object = MibTableColumn
wfX25PadPortCurrentCfgX3signals = _WfX25PadPortCurrentCfgX3signals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 12),
    _WfX25PadPortCurrentCfgX3signals_Type()
)
wfX25PadPortCurrentCfgX3signals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3signals.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3break_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3break based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_WfX25PadPortCurrentCfgX3break_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3break_Object = MibTableColumn
wfX25PadPortCurrentCfgX3break = _WfX25PadPortCurrentCfgX3break_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 13),
    _WfX25PadPortCurrentCfgX3break_Type()
)
wfX25PadPortCurrentCfgX3break.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3break.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3discard_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3discard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfX25PadPortCurrentCfgX3discard_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3discard_Object = MibTableColumn
wfX25PadPortCurrentCfgX3discard = _WfX25PadPortCurrentCfgX3discard_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 14),
    _WfX25PadPortCurrentCfgX3discard_Type()
)
wfX25PadPortCurrentCfgX3discard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3discard.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3CRpad_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3CRpad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortCurrentCfgX3CRpad_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3CRpad_Object = MibTableColumn
wfX25PadPortCurrentCfgX3CRpad = _WfX25PadPortCurrentCfgX3CRpad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 15),
    _WfX25PadPortCurrentCfgX3CRpad_Type()
)
wfX25PadPortCurrentCfgX3CRpad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3CRpad.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3folding_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3folding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortCurrentCfgX3folding_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3folding_Object = MibTableColumn
wfX25PadPortCurrentCfgX3folding = _WfX25PadPortCurrentCfgX3folding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 16),
    _WfX25PadPortCurrentCfgX3folding_Type()
)
wfX25PadPortCurrentCfgX3folding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3folding.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3speed_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_WfX25PadPortCurrentCfgX3speed_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3speed_Object = MibTableColumn
wfX25PadPortCurrentCfgX3speed = _WfX25PadPortCurrentCfgX3speed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 17),
    _WfX25PadPortCurrentCfgX3speed_Type()
)
wfX25PadPortCurrentCfgX3speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3speed.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3flow_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3flow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfX25PadPortCurrentCfgX3flow_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3flow_Object = MibTableColumn
wfX25PadPortCurrentCfgX3flow = _WfX25PadPortCurrentCfgX3flow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 18),
    _WfX25PadPortCurrentCfgX3flow_Type()
)
wfX25PadPortCurrentCfgX3flow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3flow.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3LFinsert_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3LFinsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WfX25PadPortCurrentCfgX3LFinsert_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3LFinsert_Object = MibTableColumn
wfX25PadPortCurrentCfgX3LFinsert = _WfX25PadPortCurrentCfgX3LFinsert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 19),
    _WfX25PadPortCurrentCfgX3LFinsert_Type()
)
wfX25PadPortCurrentCfgX3LFinsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3LFinsert.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3LFpad_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3LFpad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortCurrentCfgX3LFpad_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3LFpad_Object = MibTableColumn
wfX25PadPortCurrentCfgX3LFpad = _WfX25PadPortCurrentCfgX3LFpad_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 20),
    _WfX25PadPortCurrentCfgX3LFpad_Type()
)
wfX25PadPortCurrentCfgX3LFpad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3LFpad.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3Edit_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3Edit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WfX25PadPortCurrentCfgX3Edit_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3Edit_Object = MibTableColumn
wfX25PadPortCurrentCfgX3Edit = _WfX25PadPortCurrentCfgX3Edit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 21),
    _WfX25PadPortCurrentCfgX3Edit_Type()
)
wfX25PadPortCurrentCfgX3Edit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3Edit.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3Cdelete_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3Cdelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfX25PadPortCurrentCfgX3Cdelete_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3Cdelete_Object = MibTableColumn
wfX25PadPortCurrentCfgX3Cdelete = _WfX25PadPortCurrentCfgX3Cdelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 22),
    _WfX25PadPortCurrentCfgX3Cdelete_Type()
)
wfX25PadPortCurrentCfgX3Cdelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3Cdelete.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3Ldelete_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3Ldelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfX25PadPortCurrentCfgX3Ldelete_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3Ldelete_Object = MibTableColumn
wfX25PadPortCurrentCfgX3Ldelete = _WfX25PadPortCurrentCfgX3Ldelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 23),
    _WfX25PadPortCurrentCfgX3Ldelete_Type()
)
wfX25PadPortCurrentCfgX3Ldelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3Ldelete.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3Ldisplay_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3Ldisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfX25PadPortCurrentCfgX3Ldisplay_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3Ldisplay_Object = MibTableColumn
wfX25PadPortCurrentCfgX3Ldisplay = _WfX25PadPortCurrentCfgX3Ldisplay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 24),
    _WfX25PadPortCurrentCfgX3Ldisplay_Type()
)
wfX25PadPortCurrentCfgX3Ldisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3Ldisplay.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3Esignals_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3Esignals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WfX25PadPortCurrentCfgX3Esignals_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3Esignals_Object = MibTableColumn
wfX25PadPortCurrentCfgX3Esignals = _WfX25PadPortCurrentCfgX3Esignals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 25),
    _WfX25PadPortCurrentCfgX3Esignals_Type()
)
wfX25PadPortCurrentCfgX3Esignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3Esignals.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3Mask_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortCurrentCfgX3Mask_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3Mask_Object = MibTableColumn
wfX25PadPortCurrentCfgX3Mask = _WfX25PadPortCurrentCfgX3Mask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 26),
    _WfX25PadPortCurrentCfgX3Mask_Type()
)
wfX25PadPortCurrentCfgX3Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3Mask.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3parity_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3parity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WfX25PadPortCurrentCfgX3parity_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3parity_Object = MibTableColumn
wfX25PadPortCurrentCfgX3parity = _WfX25PadPortCurrentCfgX3parity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 27),
    _WfX25PadPortCurrentCfgX3parity_Type()
)
wfX25PadPortCurrentCfgX3parity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3parity.setStatus("mandatory")


class _WfX25PadPortCurrentCfgX3page_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgX3page based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfX25PadPortCurrentCfgX3page_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgX3page_Object = MibTableColumn
wfX25PadPortCurrentCfgX3page = _WfX25PadPortCurrentCfgX3page_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 28),
    _WfX25PadPortCurrentCfgX3page_Type()
)
wfX25PadPortCurrentCfgX3page.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgX3page.setStatus("mandatory")


class _WfX25PadPortCurrentCfgLenUserData_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgLenUserData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfX25PadPortCurrentCfgLenUserData_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgLenUserData_Object = MibTableColumn
wfX25PadPortCurrentCfgLenUserData = _WfX25PadPortCurrentCfgLenUserData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 29),
    _WfX25PadPortCurrentCfgLenUserData_Type()
)
wfX25PadPortCurrentCfgLenUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgLenUserData.setStatus("mandatory")


class _WfX25PadPortCurrentCfgUserData_Type(OctetString):
    """Custom type wfX25PadPortCurrentCfgUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WfX25PadPortCurrentCfgUserData_Type.__name__ = "OctetString"
_WfX25PadPortCurrentCfgUserData_Object = MibTableColumn
wfX25PadPortCurrentCfgUserData = _WfX25PadPortCurrentCfgUserData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 30),
    _WfX25PadPortCurrentCfgUserData_Type()
)
wfX25PadPortCurrentCfgUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgUserData.setStatus("mandatory")


class _WfX25PadPortCurrentCfgLenRawFacilities_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgLenRawFacilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WfX25PadPortCurrentCfgLenRawFacilities_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgLenRawFacilities_Object = MibTableColumn
wfX25PadPortCurrentCfgLenRawFacilities = _WfX25PadPortCurrentCfgLenRawFacilities_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 31),
    _WfX25PadPortCurrentCfgLenRawFacilities_Type()
)
wfX25PadPortCurrentCfgLenRawFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgLenRawFacilities.setStatus("mandatory")


class _WfX25PadPortCurrentCfgRawFacilitiesData_Type(OctetString):
    """Custom type wfX25PadPortCurrentCfgRawFacilitiesData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_WfX25PadPortCurrentCfgRawFacilitiesData_Type.__name__ = "OctetString"
_WfX25PadPortCurrentCfgRawFacilitiesData_Object = MibTableColumn
wfX25PadPortCurrentCfgRawFacilitiesData = _WfX25PadPortCurrentCfgRawFacilitiesData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 32),
    _WfX25PadPortCurrentCfgRawFacilitiesData_Type()
)
wfX25PadPortCurrentCfgRawFacilitiesData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgRawFacilitiesData.setStatus("mandatory")


class _WfX25PadPortCurrentCfgReverseCharge_Type(OctetString):
    """Custom type wfX25PadPortCurrentCfgReverseCharge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_WfX25PadPortCurrentCfgReverseCharge_Type.__name__ = "OctetString"
_WfX25PadPortCurrentCfgReverseCharge_Object = MibTableColumn
wfX25PadPortCurrentCfgReverseCharge = _WfX25PadPortCurrentCfgReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 33),
    _WfX25PadPortCurrentCfgReverseCharge_Type()
)
wfX25PadPortCurrentCfgReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgReverseCharge.setStatus("mandatory")


class _WfX25PadPortCurrentCfgThruClassNegotiation_Type(OctetString):
    """Custom type wfX25PadPortCurrentCfgThruClassNegotiation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_WfX25PadPortCurrentCfgThruClassNegotiation_Type.__name__ = "OctetString"
_WfX25PadPortCurrentCfgThruClassNegotiation_Object = MibTableColumn
wfX25PadPortCurrentCfgThruClassNegotiation = _WfX25PadPortCurrentCfgThruClassNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 34),
    _WfX25PadPortCurrentCfgThruClassNegotiation_Type()
)
wfX25PadPortCurrentCfgThruClassNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgThruClassNegotiation.setStatus("mandatory")


class _WfX25PadPortCurrentCfgPacketSizeNegotiation_Type(OctetString):
    """Custom type wfX25PadPortCurrentCfgPacketSizeNegotiation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_WfX25PadPortCurrentCfgPacketSizeNegotiation_Type.__name__ = "OctetString"
_WfX25PadPortCurrentCfgPacketSizeNegotiation_Object = MibTableColumn
wfX25PadPortCurrentCfgPacketSizeNegotiation = _WfX25PadPortCurrentCfgPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 35),
    _WfX25PadPortCurrentCfgPacketSizeNegotiation_Type()
)
wfX25PadPortCurrentCfgPacketSizeNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgPacketSizeNegotiation.setStatus("mandatory")


class _WfX25PadPortCurrentCfgWindowSizeNegotiation_Type(OctetString):
    """Custom type wfX25PadPortCurrentCfgWindowSizeNegotiation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_WfX25PadPortCurrentCfgWindowSizeNegotiation_Type.__name__ = "OctetString"
_WfX25PadPortCurrentCfgWindowSizeNegotiation_Object = MibTableColumn
wfX25PadPortCurrentCfgWindowSizeNegotiation = _WfX25PadPortCurrentCfgWindowSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 36),
    _WfX25PadPortCurrentCfgWindowSizeNegotiation_Type()
)
wfX25PadPortCurrentCfgWindowSizeNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgWindowSizeNegotiation.setStatus("mandatory")


class _WfX25PadPortCurrentCfgIntervalTimer_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgIntervalTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_WfX25PadPortCurrentCfgIntervalTimer_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgIntervalTimer_Object = MibTableColumn
wfX25PadPortCurrentCfgIntervalTimer = _WfX25PadPortCurrentCfgIntervalTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 37),
    _WfX25PadPortCurrentCfgIntervalTimer_Type()
)
wfX25PadPortCurrentCfgIntervalTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgIntervalTimer.setStatus("mandatory")


class _WfX25PadPortCurrentCfgFullAddressing_Type(Integer32):
    """Custom type wfX25PadPortCurrentCfgFullAddressing based on Integer32"""
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


_WfX25PadPortCurrentCfgFullAddressing_Type.__name__ = "Integer32"
_WfX25PadPortCurrentCfgFullAddressing_Object = MibTableColumn
wfX25PadPortCurrentCfgFullAddressing = _WfX25PadPortCurrentCfgFullAddressing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 5, 1, 38),
    _WfX25PadPortCurrentCfgFullAddressing_Type()
)
wfX25PadPortCurrentCfgFullAddressing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfX25PadPortCurrentCfgFullAddressing.setStatus("mandatory")
_WfX25PadPortStatTable_Object = MibTable
wfX25PadPortStatTable = _WfX25PadPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6)
)
if mibBuilder.loadTexts:
    wfX25PadPortStatTable.setStatus("mandatory")
_WfX25PadPortStatEntry_Object = MibTableRow
wfX25PadPortStatEntry = _WfX25PadPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1)
)
wfX25PadPortStatEntry.setIndexNames(
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortStatSlot"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortStatConnector"),
    (0, "Wellfleet-X25PAD-MIB", "wfX25PadPortStatNumber"),
)
if mibBuilder.loadTexts:
    wfX25PadPortStatEntry.setStatus("mandatory")


class _WfX25PadPortStatState_Type(Integer32):
    """Custom type wfX25PadPortStatState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfX25PadPortStatState_Type.__name__ = "Integer32"
_WfX25PadPortStatState_Object = MibTableColumn
wfX25PadPortStatState = _WfX25PadPortStatState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 1),
    _WfX25PadPortStatState_Type()
)
wfX25PadPortStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatState.setStatus("mandatory")
_WfX25PadPortStatSlot_Type = Integer32
_WfX25PadPortStatSlot_Object = MibTableColumn
wfX25PadPortStatSlot = _WfX25PadPortStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 2),
    _WfX25PadPortStatSlot_Type()
)
wfX25PadPortStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatSlot.setStatus("mandatory")
_WfX25PadPortStatConnector_Type = Integer32
_WfX25PadPortStatConnector_Object = MibTableColumn
wfX25PadPortStatConnector = _WfX25PadPortStatConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 3),
    _WfX25PadPortStatConnector_Type()
)
wfX25PadPortStatConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatConnector.setStatus("mandatory")
_WfX25PadPortStatNumber_Type = Integer32
_WfX25PadPortStatNumber_Object = MibTableColumn
wfX25PadPortStatNumber = _WfX25PadPortStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 4),
    _WfX25PadPortStatNumber_Type()
)
wfX25PadPortStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatNumber.setStatus("mandatory")
_WfX25PadPortStatRxOctets_Type = Counter32
_WfX25PadPortStatRxOctets_Object = MibTableColumn
wfX25PadPortStatRxOctets = _WfX25PadPortStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 5),
    _WfX25PadPortStatRxOctets_Type()
)
wfX25PadPortStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRxOctets.setStatus("mandatory")
_WfX25PadPortStatTxOctets_Type = Counter32
_WfX25PadPortStatTxOctets_Object = MibTableColumn
wfX25PadPortStatTxOctets = _WfX25PadPortStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 6),
    _WfX25PadPortStatTxOctets_Type()
)
wfX25PadPortStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatTxOctets.setStatus("mandatory")
_WfX25PadPortStatRxPackets_Type = Counter32
_WfX25PadPortStatRxPackets_Object = MibTableColumn
wfX25PadPortStatRxPackets = _WfX25PadPortStatRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 7),
    _WfX25PadPortStatRxPackets_Type()
)
wfX25PadPortStatRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRxPackets.setStatus("mandatory")
_WfX25PadPortStatTxPackets_Type = Counter32
_WfX25PadPortStatTxPackets_Object = MibTableColumn
wfX25PadPortStatTxPackets = _WfX25PadPortStatTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 8),
    _WfX25PadPortStatTxPackets_Type()
)
wfX25PadPortStatTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatTxPackets.setStatus("mandatory")


class _WfX25PadPortStatRemoteX121Addr_Type(DisplayString):
    """Custom type wfX25PadPortStatRemoteX121Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WfX25PadPortStatRemoteX121Addr_Type.__name__ = "DisplayString"
_WfX25PadPortStatRemoteX121Addr_Object = MibTableColumn
wfX25PadPortStatRemoteX121Addr = _WfX25PadPortStatRemoteX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 9),
    _WfX25PadPortStatRemoteX121Addr_Type()
)
wfX25PadPortStatRemoteX121Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRemoteX121Addr.setStatus("mandatory")
_WfX25PadPortStatLCN_Type = Integer32
_WfX25PadPortStatLCN_Object = MibTableColumn
wfX25PadPortStatLCN = _WfX25PadPortStatLCN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 10),
    _WfX25PadPortStatLCN_Type()
)
wfX25PadPortStatLCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatLCN.setStatus("mandatory")
_WfX25PadPortStatDuration_Type = Integer32
_WfX25PadPortStatDuration_Object = MibTableColumn
wfX25PadPortStatDuration = _WfX25PadPortStatDuration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 11),
    _WfX25PadPortStatDuration_Type()
)
wfX25PadPortStatDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatDuration.setStatus("mandatory")
_WfX25PadPortStatRxRR_Type = Counter32
_WfX25PadPortStatRxRR_Object = MibTableColumn
wfX25PadPortStatRxRR = _WfX25PadPortStatRxRR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 12),
    _WfX25PadPortStatRxRR_Type()
)
wfX25PadPortStatRxRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRxRR.setStatus("mandatory")
_WfX25PadPortStatTxRR_Type = Counter32
_WfX25PadPortStatTxRR_Object = MibTableColumn
wfX25PadPortStatTxRR = _WfX25PadPortStatTxRR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 13),
    _WfX25PadPortStatTxRR_Type()
)
wfX25PadPortStatTxRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatTxRR.setStatus("mandatory")
_WfX25PadPortStatRxRNR_Type = Counter32
_WfX25PadPortStatRxRNR_Object = MibTableColumn
wfX25PadPortStatRxRNR = _WfX25PadPortStatRxRNR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 14),
    _WfX25PadPortStatRxRNR_Type()
)
wfX25PadPortStatRxRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRxRNR.setStatus("mandatory")
_WfX25PadPortStatTxRNR_Type = Counter32
_WfX25PadPortStatTxRNR_Object = MibTableColumn
wfX25PadPortStatTxRNR = _WfX25PadPortStatTxRNR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 15),
    _WfX25PadPortStatTxRNR_Type()
)
wfX25PadPortStatTxRNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatTxRNR.setStatus("mandatory")
_WfX25PadPortStatRxClr_Type = Counter32
_WfX25PadPortStatRxClr_Object = MibTableColumn
wfX25PadPortStatRxClr = _WfX25PadPortStatRxClr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 16),
    _WfX25PadPortStatRxClr_Type()
)
wfX25PadPortStatRxClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRxClr.setStatus("mandatory")
_WfX25PadPortStatTxClr_Type = Counter32
_WfX25PadPortStatTxClr_Object = MibTableColumn
wfX25PadPortStatTxClr = _WfX25PadPortStatTxClr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 17),
    _WfX25PadPortStatTxClr_Type()
)
wfX25PadPortStatTxClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatTxClr.setStatus("mandatory")
_WfX25PadPortStatRxReset_Type = Counter32
_WfX25PadPortStatRxReset_Object = MibTableColumn
wfX25PadPortStatRxReset = _WfX25PadPortStatRxReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 18),
    _WfX25PadPortStatRxReset_Type()
)
wfX25PadPortStatRxReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRxReset.setStatus("mandatory")
_WfX25PadPortStatTxReset_Type = Counter32
_WfX25PadPortStatTxReset_Object = MibTableColumn
wfX25PadPortStatTxReset = _WfX25PadPortStatTxReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 19),
    _WfX25PadPortStatTxReset_Type()
)
wfX25PadPortStatTxReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatTxReset.setStatus("mandatory")
_WfX25PadPortStatRxCall_Type = Counter32
_WfX25PadPortStatRxCall_Object = MibTableColumn
wfX25PadPortStatRxCall = _WfX25PadPortStatRxCall_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 20),
    _WfX25PadPortStatRxCall_Type()
)
wfX25PadPortStatRxCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatRxCall.setStatus("mandatory")
_WfX25PadPortStatTxCall_Type = Counter32
_WfX25PadPortStatTxCall_Object = MibTableColumn
wfX25PadPortStatTxCall = _WfX25PadPortStatTxCall_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 21),
    _WfX25PadPortStatTxCall_Type()
)
wfX25PadPortStatTxCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatTxCall.setStatus("mandatory")
_WfX25PadPortStatConnections_Type = Counter32
_WfX25PadPortStatConnections_Object = MibTableColumn
wfX25PadPortStatConnections = _WfX25PadPortStatConnections_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 22),
    _WfX25PadPortStatConnections_Type()
)
wfX25PadPortStatConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatConnections.setStatus("mandatory")
_WfX25PadPortStatDisconnects_Type = Counter32
_WfX25PadPortStatDisconnects_Object = MibTableColumn
wfX25PadPortStatDisconnects = _WfX25PadPortStatDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 23),
    _WfX25PadPortStatDisconnects_Type()
)
wfX25PadPortStatDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatDisconnects.setStatus("mandatory")
_WfX25PadPortStatLastCause_Type = Integer32
_WfX25PadPortStatLastCause_Object = MibTableColumn
wfX25PadPortStatLastCause = _WfX25PadPortStatLastCause_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 24),
    _WfX25PadPortStatLastCause_Type()
)
wfX25PadPortStatLastCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatLastCause.setStatus("mandatory")
_WfX25PadPortStatLastDiag_Type = Integer32
_WfX25PadPortStatLastDiag_Object = MibTableColumn
wfX25PadPortStatLastDiag = _WfX25PadPortStatLastDiag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 12, 6, 1, 25),
    _WfX25PadPortStatLastDiag_Type()
)
wfX25PadPortStatLastDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfX25PadPortStatLastDiag.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-X25PAD-MIB",
    **{"wfX25PadDefaultCfgTable": wfX25PadDefaultCfgTable,
       "wfX25PadDefaultCfgEntry": wfX25PadDefaultCfgEntry,
       "wfX25PadDefaultCfgDelete": wfX25PadDefaultCfgDelete,
       "wfX25PadDefaultCfgDisable": wfX25PadDefaultCfgDisable,
       "wfX25PadDefaultCfgState": wfX25PadDefaultCfgState,
       "wfX25PadDefaultCfgSlot": wfX25PadDefaultCfgSlot,
       "wfX25PadDefaultCfgConnector": wfX25PadDefaultCfgConnector,
       "wfX25PadDefaultCfgCircuit": wfX25PadDefaultCfgCircuit,
       "wfX25PadDefaultCfgX121Addr": wfX25PadDefaultCfgX121Addr,
       "wfX25PadDefaultCfgDNIC": wfX25PadDefaultCfgDNIC,
       "wfX25PadDefaultCfgLenSubAddress": wfX25PadDefaultCfgLenSubAddress,
       "wfX25PadDefaultCfgLCNLow": wfX25PadDefaultCfgLCNLow,
       "wfX25PadDefaultCfgLCNHigh": wfX25PadDefaultCfgLCNHigh,
       "wfX25PadCurrentCfgTable": wfX25PadCurrentCfgTable,
       "wfX25PadCurrentCfgEntry": wfX25PadCurrentCfgEntry,
       "wfX25PadCurrentCfgState": wfX25PadCurrentCfgState,
       "wfX25PadCurrentCfgSlot": wfX25PadCurrentCfgSlot,
       "wfX25PadCurrentCfgConnector": wfX25PadCurrentCfgConnector,
       "wfX25PadCurrentCfgCircuit": wfX25PadCurrentCfgCircuit,
       "wfX25PadCurrentCfgX121Addr": wfX25PadCurrentCfgX121Addr,
       "wfX25PadCurrentCfgDNIC": wfX25PadCurrentCfgDNIC,
       "wfX25PadCurrentCfgLenSubAddress": wfX25PadCurrentCfgLenSubAddress,
       "wfX25PadCurrentCfgLCNLow": wfX25PadCurrentCfgLCNLow,
       "wfX25PadCurrentCfgLCNHigh": wfX25PadCurrentCfgLCNHigh,
       "wfX25PadStatTable": wfX25PadStatTable,
       "wfX25PadStatEntry": wfX25PadStatEntry,
       "wfX25PadStatState": wfX25PadStatState,
       "wfX25PadStatSlot": wfX25PadStatSlot,
       "wfX25PadStatConnector": wfX25PadStatConnector,
       "wfX25PadStatTotalConnCount": wfX25PadStatTotalConnCount,
       "wfX25PadStatRxRR": wfX25PadStatRxRR,
       "wfX25PadStatTxRR": wfX25PadStatTxRR,
       "wfX25PadStatRxRNR": wfX25PadStatRxRNR,
       "wfX25PadStatTxRNR": wfX25PadStatTxRNR,
       "wfX25PadStatRxRestart": wfX25PadStatRxRestart,
       "wfX25PadStatTxRestart": wfX25PadStatTxRestart,
       "wfX25PadPortDefaultCfgTable": wfX25PadPortDefaultCfgTable,
       "wfX25PadPortDefaultCfgEntry": wfX25PadPortDefaultCfgEntry,
       "wfX25PadPortDefaultCfgDelete": wfX25PadPortDefaultCfgDelete,
       "wfX25PadPortDefaultCfgDisable": wfX25PadPortDefaultCfgDisable,
       "wfX25PadPortDefaultCfgState": wfX25PadPortDefaultCfgState,
       "wfX25PadPortDefaultCfgSlot": wfX25PadPortDefaultCfgSlot,
       "wfX25PadPortDefaultCfgConnector": wfX25PadPortDefaultCfgConnector,
       "wfX25PadPortDefaultCfgNumber": wfX25PadPortDefaultCfgNumber,
       "wfX25PadPortDefaultCfgSubAddress": wfX25PadPortDefaultCfgSubAddress,
       "wfX25PadPortDefaultCfgLenSubAddress": wfX25PadPortDefaultCfgLenSubAddress,
       "wfX25PadPortDefaultCfgX3escape": wfX25PadPortDefaultCfgX3escape,
       "wfX25PadPortDefaultCfgX3echo": wfX25PadPortDefaultCfgX3echo,
       "wfX25PadPortDefaultCfgX3forward": wfX25PadPortDefaultCfgX3forward,
       "wfX25PadPortDefaultCfgX3idle": wfX25PadPortDefaultCfgX3idle,
       "wfX25PadPortDefaultCfgX3device": wfX25PadPortDefaultCfgX3device,
       "wfX25PadPortDefaultCfgX3signals": wfX25PadPortDefaultCfgX3signals,
       "wfX25PadPortDefaultCfgX3break": wfX25PadPortDefaultCfgX3break,
       "wfX25PadPortDefaultCfgX3discard": wfX25PadPortDefaultCfgX3discard,
       "wfX25PadPortDefaultCfgX3CRpad": wfX25PadPortDefaultCfgX3CRpad,
       "wfX25PadPortDefaultCfgX3folding": wfX25PadPortDefaultCfgX3folding,
       "wfX25PadPortDefaultCfgX3speed": wfX25PadPortDefaultCfgX3speed,
       "wfX25PadPortDefaultCfgX3flow": wfX25PadPortDefaultCfgX3flow,
       "wfX25PadPortDefaultCfgX3LFinsert": wfX25PadPortDefaultCfgX3LFinsert,
       "wfX25PadPortDefaultCfgX3LFpad": wfX25PadPortDefaultCfgX3LFpad,
       "wfX25PadPortDefaultCfgX3Edit": wfX25PadPortDefaultCfgX3Edit,
       "wfX25PadPortDefaultCfgX3Cdelete": wfX25PadPortDefaultCfgX3Cdelete,
       "wfX25PadPortDefaultCfgX3Ldelete": wfX25PadPortDefaultCfgX3Ldelete,
       "wfX25PadPortDefaultCfgX3Ldisplay": wfX25PadPortDefaultCfgX3Ldisplay,
       "wfX25PadPortDefaultCfgX3Esignals": wfX25PadPortDefaultCfgX3Esignals,
       "wfX25PadPortDefaultCfgX3Mask": wfX25PadPortDefaultCfgX3Mask,
       "wfX25PadPortDefaultCfgX3parity": wfX25PadPortDefaultCfgX3parity,
       "wfX25PadPortDefaultCfgX3page": wfX25PadPortDefaultCfgX3page,
       "wfX25PadPortDefaultCfgLenUserData": wfX25PadPortDefaultCfgLenUserData,
       "wfX25PadPortDefaultCfgUserData": wfX25PadPortDefaultCfgUserData,
       "wfX25PadPortDefaultCfgLenRawFacilities": wfX25PadPortDefaultCfgLenRawFacilities,
       "wfX25PadPortDefaultCfgRawFacilitiesData": wfX25PadPortDefaultCfgRawFacilitiesData,
       "wfX25PadPortDefaultCfgReverseCharge": wfX25PadPortDefaultCfgReverseCharge,
       "wfX25PadPortDefaultCfgThruClassNegotiation": wfX25PadPortDefaultCfgThruClassNegotiation,
       "wfX25PadPortDefaultCfgPacketSizeNegotiation": wfX25PadPortDefaultCfgPacketSizeNegotiation,
       "wfX25PadPortDefaultCfgWindowSizeNegotiation": wfX25PadPortDefaultCfgWindowSizeNegotiation,
       "wfX25PadPortDefaultCfgIntervalTimer": wfX25PadPortDefaultCfgIntervalTimer,
       "wfX25PadPortDefaultCfgFullAddressing": wfX25PadPortDefaultCfgFullAddressing,
       "wfX25PadPortCurrentCfgTable": wfX25PadPortCurrentCfgTable,
       "wfX25PadPortCurrentCfgEntry": wfX25PadPortCurrentCfgEntry,
       "wfX25PadPortCurrentCfgState": wfX25PadPortCurrentCfgState,
       "wfX25PadPortCurrentCfgSlot": wfX25PadPortCurrentCfgSlot,
       "wfX25PadPortCurrentCfgConnector": wfX25PadPortCurrentCfgConnector,
       "wfX25PadPortCurrentCfgNumber": wfX25PadPortCurrentCfgNumber,
       "wfX25PadPortCurrentCfgSubAddress": wfX25PadPortCurrentCfgSubAddress,
       "wfX25PadPortCurrentCfgLenSubAddress": wfX25PadPortCurrentCfgLenSubAddress,
       "wfX25PadPortCurrentCfgX3escape": wfX25PadPortCurrentCfgX3escape,
       "wfX25PadPortCurrentCfgX3echo": wfX25PadPortCurrentCfgX3echo,
       "wfX25PadPortCurrentCfgX3forward": wfX25PadPortCurrentCfgX3forward,
       "wfX25PadPortCurrentCfgX3idle": wfX25PadPortCurrentCfgX3idle,
       "wfX25PadPortCurrentCfgX3device": wfX25PadPortCurrentCfgX3device,
       "wfX25PadPortCurrentCfgX3signals": wfX25PadPortCurrentCfgX3signals,
       "wfX25PadPortCurrentCfgX3break": wfX25PadPortCurrentCfgX3break,
       "wfX25PadPortCurrentCfgX3discard": wfX25PadPortCurrentCfgX3discard,
       "wfX25PadPortCurrentCfgX3CRpad": wfX25PadPortCurrentCfgX3CRpad,
       "wfX25PadPortCurrentCfgX3folding": wfX25PadPortCurrentCfgX3folding,
       "wfX25PadPortCurrentCfgX3speed": wfX25PadPortCurrentCfgX3speed,
       "wfX25PadPortCurrentCfgX3flow": wfX25PadPortCurrentCfgX3flow,
       "wfX25PadPortCurrentCfgX3LFinsert": wfX25PadPortCurrentCfgX3LFinsert,
       "wfX25PadPortCurrentCfgX3LFpad": wfX25PadPortCurrentCfgX3LFpad,
       "wfX25PadPortCurrentCfgX3Edit": wfX25PadPortCurrentCfgX3Edit,
       "wfX25PadPortCurrentCfgX3Cdelete": wfX25PadPortCurrentCfgX3Cdelete,
       "wfX25PadPortCurrentCfgX3Ldelete": wfX25PadPortCurrentCfgX3Ldelete,
       "wfX25PadPortCurrentCfgX3Ldisplay": wfX25PadPortCurrentCfgX3Ldisplay,
       "wfX25PadPortCurrentCfgX3Esignals": wfX25PadPortCurrentCfgX3Esignals,
       "wfX25PadPortCurrentCfgX3Mask": wfX25PadPortCurrentCfgX3Mask,
       "wfX25PadPortCurrentCfgX3parity": wfX25PadPortCurrentCfgX3parity,
       "wfX25PadPortCurrentCfgX3page": wfX25PadPortCurrentCfgX3page,
       "wfX25PadPortCurrentCfgLenUserData": wfX25PadPortCurrentCfgLenUserData,
       "wfX25PadPortCurrentCfgUserData": wfX25PadPortCurrentCfgUserData,
       "wfX25PadPortCurrentCfgLenRawFacilities": wfX25PadPortCurrentCfgLenRawFacilities,
       "wfX25PadPortCurrentCfgRawFacilitiesData": wfX25PadPortCurrentCfgRawFacilitiesData,
       "wfX25PadPortCurrentCfgReverseCharge": wfX25PadPortCurrentCfgReverseCharge,
       "wfX25PadPortCurrentCfgThruClassNegotiation": wfX25PadPortCurrentCfgThruClassNegotiation,
       "wfX25PadPortCurrentCfgPacketSizeNegotiation": wfX25PadPortCurrentCfgPacketSizeNegotiation,
       "wfX25PadPortCurrentCfgWindowSizeNegotiation": wfX25PadPortCurrentCfgWindowSizeNegotiation,
       "wfX25PadPortCurrentCfgIntervalTimer": wfX25PadPortCurrentCfgIntervalTimer,
       "wfX25PadPortCurrentCfgFullAddressing": wfX25PadPortCurrentCfgFullAddressing,
       "wfX25PadPortStatTable": wfX25PadPortStatTable,
       "wfX25PadPortStatEntry": wfX25PadPortStatEntry,
       "wfX25PadPortStatState": wfX25PadPortStatState,
       "wfX25PadPortStatSlot": wfX25PadPortStatSlot,
       "wfX25PadPortStatConnector": wfX25PadPortStatConnector,
       "wfX25PadPortStatNumber": wfX25PadPortStatNumber,
       "wfX25PadPortStatRxOctets": wfX25PadPortStatRxOctets,
       "wfX25PadPortStatTxOctets": wfX25PadPortStatTxOctets,
       "wfX25PadPortStatRxPackets": wfX25PadPortStatRxPackets,
       "wfX25PadPortStatTxPackets": wfX25PadPortStatTxPackets,
       "wfX25PadPortStatRemoteX121Addr": wfX25PadPortStatRemoteX121Addr,
       "wfX25PadPortStatLCN": wfX25PadPortStatLCN,
       "wfX25PadPortStatDuration": wfX25PadPortStatDuration,
       "wfX25PadPortStatRxRR": wfX25PadPortStatRxRR,
       "wfX25PadPortStatTxRR": wfX25PadPortStatTxRR,
       "wfX25PadPortStatRxRNR": wfX25PadPortStatRxRNR,
       "wfX25PadPortStatTxRNR": wfX25PadPortStatTxRNR,
       "wfX25PadPortStatRxClr": wfX25PadPortStatRxClr,
       "wfX25PadPortStatTxClr": wfX25PadPortStatTxClr,
       "wfX25PadPortStatRxReset": wfX25PadPortStatRxReset,
       "wfX25PadPortStatTxReset": wfX25PadPortStatTxReset,
       "wfX25PadPortStatRxCall": wfX25PadPortStatRxCall,
       "wfX25PadPortStatTxCall": wfX25PadPortStatTxCall,
       "wfX25PadPortStatConnections": wfX25PadPortStatConnections,
       "wfX25PadPortStatDisconnects": wfX25PadPortStatDisconnects,
       "wfX25PadPortStatLastCause": wfX25PadPortStatLastCause,
       "wfX25PadPortStatLastDiag": wfX25PadPortStatLastDiag}
)
