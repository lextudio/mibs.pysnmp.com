# SNMP MIB module (COM21-HCXOC3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXOC3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:36 2024
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

(com21,
 com21Hcx,
 com21Traps) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx",
    "com21Traps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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


# MODULE-IDENTITY

com21HcxOc3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 90)
)


# Types definitions



class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxOc3UnitGroup_ObjectIdentity = ObjectIdentity
com21HcxOc3UnitGroup = _Com21HcxOc3UnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91)
)
_Com21HcxOc3UnitTable_Object = MibTable
com21HcxOc3UnitTable = _Com21HcxOc3UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1)
)
if mibBuilder.loadTexts:
    com21HcxOc3UnitTable.setStatus("current")
_Com21HcxOc3UnitEntry_Object = MibTableRow
com21HcxOc3UnitEntry = _Com21HcxOc3UnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1)
)
com21HcxOc3UnitEntry.setIndexNames(
    (0, "COM21-HCXOC3-MIB", "hcxOc3UnitShelfId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3UnitSlotId"),
)
if mibBuilder.loadTexts:
    com21HcxOc3UnitEntry.setStatus("current")


class _HcxOc3UnitShelfId_Type(Integer32):
    """Custom type hcxOc3UnitShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HcxOc3UnitShelfId_Type.__name__ = "Integer32"
_HcxOc3UnitShelfId_Object = MibTableColumn
hcxOc3UnitShelfId = _HcxOc3UnitShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 1),
    _HcxOc3UnitShelfId_Type()
)
hcxOc3UnitShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3UnitShelfId.setStatus("current")
_HcxOc3UnitSlotId_Type = Integer32
_HcxOc3UnitSlotId_Object = MibTableColumn
hcxOc3UnitSlotId = _HcxOc3UnitSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 2),
    _HcxOc3UnitSlotId_Type()
)
hcxOc3UnitSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3UnitSlotId.setStatus("current")


class _HcxOc3HardwareVersion_Type(DisplayString):
    """Custom type hcxOc3HardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxOc3HardwareVersion_Type.__name__ = "DisplayString"
_HcxOc3HardwareVersion_Object = MibTableColumn
hcxOc3HardwareVersion = _HcxOc3HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 3),
    _HcxOc3HardwareVersion_Type()
)
hcxOc3HardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3HardwareVersion.setStatus("current")


class _HcxOc3BootVersion_Type(DisplayString):
    """Custom type hcxOc3BootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxOc3BootVersion_Type.__name__ = "DisplayString"
_HcxOc3BootVersion_Object = MibTableColumn
hcxOc3BootVersion = _HcxOc3BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 4),
    _HcxOc3BootVersion_Type()
)
hcxOc3BootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3BootVersion.setStatus("current")
_HcxOc3UnitPrimServState_Type = PrimServiceState
_HcxOc3UnitPrimServState_Object = MibTableColumn
hcxOc3UnitPrimServState = _HcxOc3UnitPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 5),
    _HcxOc3UnitPrimServState_Type()
)
hcxOc3UnitPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3UnitPrimServState.setStatus("current")


class _HcxOc3UnitSecServState_Type(DisplayString):
    """Custom type hcxOc3UnitSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxOc3UnitSecServState_Type.__name__ = "DisplayString"
_HcxOc3UnitSecServState_Object = MibTableColumn
hcxOc3UnitSecServState = _HcxOc3UnitSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 6),
    _HcxOc3UnitSecServState_Type()
)
hcxOc3UnitSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3UnitSecServState.setStatus("current")


class _HcxOc3RestartAction_Type(Integer32):
    """Custom type hcxOc3RestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("restart", 2))
    )


_HcxOc3RestartAction_Type.__name__ = "Integer32"
_HcxOc3RestartAction_Object = MibTableColumn
hcxOc3RestartAction = _HcxOc3RestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 7),
    _HcxOc3RestartAction_Type()
)
hcxOc3RestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3RestartAction.setStatus("current")


class _HcxOc3TestStatusLed_Type(Integer32):
    """Custom type hcxOc3TestStatusLed based on Integer32"""
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


_HcxOc3TestStatusLed_Type.__name__ = "Integer32"
_HcxOc3TestStatusLed_Object = MibTableColumn
hcxOc3TestStatusLed = _HcxOc3TestStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 8),
    _HcxOc3TestStatusLed_Type()
)
hcxOc3TestStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3TestStatusLed.setStatus("current")


class _HcxOc3FaultStatusLed_Type(Integer32):
    """Custom type hcxOc3FaultStatusLed based on Integer32"""
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


_HcxOc3FaultStatusLed_Type.__name__ = "Integer32"
_HcxOc3FaultStatusLed_Object = MibTableColumn
hcxOc3FaultStatusLed = _HcxOc3FaultStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 9),
    _HcxOc3FaultStatusLed_Type()
)
hcxOc3FaultStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3FaultStatusLed.setStatus("current")


class _HcxOc3SerialNumber_Type(DisplayString):
    """Custom type hcxOc3SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxOc3SerialNumber_Type.__name__ = "DisplayString"
_HcxOc3SerialNumber_Object = MibTableColumn
hcxOc3SerialNumber = _HcxOc3SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 10),
    _HcxOc3SerialNumber_Type()
)
hcxOc3SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3SerialNumber.setStatus("current")


class _HcxOc3SyncClkConfigure_Type(Integer32):
    """Custom type hcxOc3SyncClkConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("priSrc", 2),
          ("secSrc", 3))
    )


_HcxOc3SyncClkConfigure_Type.__name__ = "Integer32"
_HcxOc3SyncClkConfigure_Object = MibTableColumn
hcxOc3SyncClkConfigure = _HcxOc3SyncClkConfigure_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 91, 1, 1, 11),
    _HcxOc3SyncClkConfigure_Type()
)
hcxOc3SyncClkConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3SyncClkConfigure.setStatus("current")
_Com21HcxOc3PortGroup_ObjectIdentity = ObjectIdentity
com21HcxOc3PortGroup = _Com21HcxOc3PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92)
)
_Com21HcxOc3PortTable_Object = MibTable
com21HcxOc3PortTable = _Com21HcxOc3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1)
)
if mibBuilder.loadTexts:
    com21HcxOc3PortTable.setStatus("current")
_Com21HcxOc3PortEntry_Object = MibTableRow
com21HcxOc3PortEntry = _Com21HcxOc3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1)
)
com21HcxOc3PortEntry.setIndexNames(
    (0, "COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3PortId"),
)
if mibBuilder.loadTexts:
    com21HcxOc3PortEntry.setStatus("current")


class _HcxOc3PortShelfId_Type(Integer32):
    """Custom type hcxOc3PortShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HcxOc3PortShelfId_Type.__name__ = "Integer32"
_HcxOc3PortShelfId_Object = MibTableColumn
hcxOc3PortShelfId = _HcxOc3PortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 1),
    _HcxOc3PortShelfId_Type()
)
hcxOc3PortShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortShelfId.setStatus("current")
_HcxOc3PortSlotId_Type = Integer32
_HcxOc3PortSlotId_Object = MibTableColumn
hcxOc3PortSlotId = _HcxOc3PortSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 2),
    _HcxOc3PortSlotId_Type()
)
hcxOc3PortSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortSlotId.setStatus("current")


class _HcxOc3PortId_Type(Integer32):
    """Custom type hcxOc3PortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HcxOc3PortId_Type.__name__ = "Integer32"
_HcxOc3PortId_Object = MibTableColumn
hcxOc3PortId = _HcxOc3PortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 3),
    _HcxOc3PortId_Type()
)
hcxOc3PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortId.setStatus("current")
_HcxOc3PortPrimServState_Type = PrimServiceState
_HcxOc3PortPrimServState_Object = MibTableColumn
hcxOc3PortPrimServState = _HcxOc3PortPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 4),
    _HcxOc3PortPrimServState_Type()
)
hcxOc3PortPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortPrimServState.setStatus("current")


class _HcxOc3PortSecServState_Type(DisplayString):
    """Custom type hcxOc3PortSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxOc3PortSecServState_Type.__name__ = "DisplayString"
_HcxOc3PortSecServState_Object = MibTableColumn
hcxOc3PortSecServState = _HcxOc3PortSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 5),
    _HcxOc3PortSecServState_Type()
)
hcxOc3PortSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortSecServState.setStatus("current")


class _HcxOc3MaxBandwidth_Type(Integer32):
    """Custom type hcxOc3MaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22222),
    )


_HcxOc3MaxBandwidth_Type.__name__ = "Integer32"
_HcxOc3MaxBandwidth_Object = MibTableColumn
hcxOc3MaxBandwidth = _HcxOc3MaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 6),
    _HcxOc3MaxBandwidth_Type()
)
hcxOc3MaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3MaxBandwidth.setStatus("current")
_HcxOc3AggrDnStrmCbrRate_Type = Integer32
_HcxOc3AggrDnStrmCbrRate_Object = MibTableColumn
hcxOc3AggrDnStrmCbrRate = _HcxOc3AggrDnStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 7),
    _HcxOc3AggrDnStrmCbrRate_Type()
)
hcxOc3AggrDnStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrDnStrmCbrRate.setStatus("current")
_HcxOc3AggrDnStrmPcrRate_Type = Integer32
_HcxOc3AggrDnStrmPcrRate_Object = MibTableColumn
hcxOc3AggrDnStrmPcrRate = _HcxOc3AggrDnStrmPcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 8),
    _HcxOc3AggrDnStrmPcrRate_Type()
)
hcxOc3AggrDnStrmPcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrDnStrmPcrRate.setStatus("current")
_HcxOc3AggrUpStrmCbrRate_Type = Integer32
_HcxOc3AggrUpStrmCbrRate_Object = MibTableColumn
hcxOc3AggrUpStrmCbrRate = _HcxOc3AggrUpStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 9),
    _HcxOc3AggrUpStrmCbrRate_Type()
)
hcxOc3AggrUpStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrUpStrmCbrRate.setStatus("current")
_HcxOc3AggrUpStrmMinRate_Type = Integer32
_HcxOc3AggrUpStrmMinRate_Object = MibTableColumn
hcxOc3AggrUpStrmMinRate = _HcxOc3AggrUpStrmMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 10),
    _HcxOc3AggrUpStrmMinRate_Type()
)
hcxOc3AggrUpStrmMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrUpStrmMinRate.setStatus("current")
_HcxOc3AggrUpStrmMaxRate_Type = Integer32
_HcxOc3AggrUpStrmMaxRate_Object = MibTableColumn
hcxOc3AggrUpStrmMaxRate = _HcxOc3AggrUpStrmMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 11),
    _HcxOc3AggrUpStrmMaxRate_Type()
)
hcxOc3AggrUpStrmMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrUpStrmMaxRate.setStatus("current")
_HcxOc3AgeTime_Type = Integer32
_HcxOc3AgeTime_Object = MibTableColumn
hcxOc3AgeTime = _HcxOc3AgeTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 12),
    _HcxOc3AgeTime_Type()
)
hcxOc3AgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3AgeTime.setStatus("current")


class _HcxOc3PortConfigState_Type(Integer32):
    """Custom type hcxOc3PortConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2000,
              2001,
              2002)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2000),
          ("online", 2001),
          ("test", 2002))
    )


_HcxOc3PortConfigState_Type.__name__ = "Integer32"
_HcxOc3PortConfigState_Object = MibTableColumn
hcxOc3PortConfigState = _HcxOc3PortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 13),
    _HcxOc3PortConfigState_Type()
)
hcxOc3PortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3PortConfigState.setStatus("current")


class _HcxOc3PortRestartAction_Type(Integer32):
    """Custom type hcxOc3PortRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("restart", 2))
    )


_HcxOc3PortRestartAction_Type.__name__ = "Integer32"
_HcxOc3PortRestartAction_Object = MibTableColumn
hcxOc3PortRestartAction = _HcxOc3PortRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 14),
    _HcxOc3PortRestartAction_Type()
)
hcxOc3PortRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3PortRestartAction.setStatus("current")


class _HcxOc3PortDiagTestAction_Type(Integer32):
    """Custom type hcxOc3PortDiagTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("nil", 1))
    )


_HcxOc3PortDiagTestAction_Type.__name__ = "Integer32"
_HcxOc3PortDiagTestAction_Object = MibTableColumn
hcxOc3PortDiagTestAction = _HcxOc3PortDiagTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 15),
    _HcxOc3PortDiagTestAction_Type()
)
hcxOc3PortDiagTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3PortDiagTestAction.setStatus("current")


class _HcxOc3PortDiagTestResult_Type(Integer32):
    """Custom type hcxOc3PortDiagTestResult based on Integer32"""
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
        *(("failure", 3),
          ("inprogress", 1),
          ("invalidState", 4),
          ("success", 2))
    )


_HcxOc3PortDiagTestResult_Type.__name__ = "Integer32"
_HcxOc3PortDiagTestResult_Object = MibTableColumn
hcxOc3PortDiagTestResult = _HcxOc3PortDiagTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 16),
    _HcxOc3PortDiagTestResult_Type()
)
hcxOc3PortDiagTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortDiagTestResult.setStatus("current")


class _HcxOc3PortLOSLed_Type(Integer32):
    """Custom type hcxOc3PortLOSLed based on Integer32"""
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


_HcxOc3PortLOSLed_Type.__name__ = "Integer32"
_HcxOc3PortLOSLed_Object = MibTableColumn
hcxOc3PortLOSLed = _HcxOc3PortLOSLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 17),
    _HcxOc3PortLOSLed_Type()
)
hcxOc3PortLOSLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortLOSLed.setStatus("current")
_HcxOc3AggrActDnStrmCbrRate_Type = Integer32
_HcxOc3AggrActDnStrmCbrRate_Object = MibTableColumn
hcxOc3AggrActDnStrmCbrRate = _HcxOc3AggrActDnStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 18),
    _HcxOc3AggrActDnStrmCbrRate_Type()
)
hcxOc3AggrActDnStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrActDnStrmCbrRate.setStatus("current")
_HcxOc3AggrActDnStrmPcrRate_Type = Integer32
_HcxOc3AggrActDnStrmPcrRate_Object = MibTableColumn
hcxOc3AggrActDnStrmPcrRate = _HcxOc3AggrActDnStrmPcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 19),
    _HcxOc3AggrActDnStrmPcrRate_Type()
)
hcxOc3AggrActDnStrmPcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrActDnStrmPcrRate.setStatus("current")
_HcxOc3AggrActUpStrmCbrRate_Type = Integer32
_HcxOc3AggrActUpStrmCbrRate_Object = MibTableColumn
hcxOc3AggrActUpStrmCbrRate = _HcxOc3AggrActUpStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 20),
    _HcxOc3AggrActUpStrmCbrRate_Type()
)
hcxOc3AggrActUpStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrActUpStrmCbrRate.setStatus("current")
_HcxOc3AggrActUpStrmMinRate_Type = Integer32
_HcxOc3AggrActUpStrmMinRate_Object = MibTableColumn
hcxOc3AggrActUpStrmMinRate = _HcxOc3AggrActUpStrmMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 21),
    _HcxOc3AggrActUpStrmMinRate_Type()
)
hcxOc3AggrActUpStrmMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrActUpStrmMinRate.setStatus("current")
_HcxOc3AggrActUpStrmMaxRate_Type = Integer32
_HcxOc3AggrActUpStrmMaxRate_Object = MibTableColumn
hcxOc3AggrActUpStrmMaxRate = _HcxOc3AggrActUpStrmMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 22),
    _HcxOc3AggrActUpStrmMaxRate_Type()
)
hcxOc3AggrActUpStrmMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3AggrActUpStrmMaxRate.setStatus("current")
_HcxOc3PortIpAddr_Type = IpAddress
_HcxOc3PortIpAddr_Object = MibTableColumn
hcxOc3PortIpAddr = _HcxOc3PortIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 23),
    _HcxOc3PortIpAddr_Type()
)
hcxOc3PortIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3PortIpAddr.setStatus("current")
_HcxOc3PortIpMask_Type = IpAddress
_HcxOc3PortIpMask_Object = MibTableColumn
hcxOc3PortIpMask = _HcxOc3PortIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 24),
    _HcxOc3PortIpMask_Type()
)
hcxOc3PortIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3PortIpMask.setStatus("current")
_HcxOc3PortMacAddr_Type = MacAddress
_HcxOc3PortMacAddr_Object = MibTableColumn
hcxOc3PortMacAddr = _HcxOc3PortMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 25),
    _HcxOc3PortMacAddr_Type()
)
hcxOc3PortMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortMacAddr.setStatus("current")


class _HcxOc3Port1483EncapEnbl_Type(Integer32):
    """Custom type hcxOc3Port1483EncapEnbl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxOc3Port1483EncapEnbl_Type.__name__ = "Integer32"
_HcxOc3Port1483EncapEnbl_Object = MibTableColumn
hcxOc3Port1483EncapEnbl = _HcxOc3Port1483EncapEnbl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 26),
    _HcxOc3Port1483EncapEnbl_Type()
)
hcxOc3Port1483EncapEnbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3Port1483EncapEnbl.setStatus("current")


class _HcxOc3PortSectionLOS_Type(Integer32):
    """Custom type hcxOc3PortSectionLOS based on Integer32"""
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


_HcxOc3PortSectionLOS_Type.__name__ = "Integer32"
_HcxOc3PortSectionLOS_Object = MibTableColumn
hcxOc3PortSectionLOS = _HcxOc3PortSectionLOS_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 27),
    _HcxOc3PortSectionLOS_Type()
)
hcxOc3PortSectionLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortSectionLOS.setStatus("current")


class _HcxOc3PortSectionLOF_Type(Integer32):
    """Custom type hcxOc3PortSectionLOF based on Integer32"""
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


_HcxOc3PortSectionLOF_Type.__name__ = "Integer32"
_HcxOc3PortSectionLOF_Object = MibTableColumn
hcxOc3PortSectionLOF = _HcxOc3PortSectionLOF_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 28),
    _HcxOc3PortSectionLOF_Type()
)
hcxOc3PortSectionLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortSectionLOF.setStatus("current")


class _HcxOc3PortLineAIS_Type(Integer32):
    """Custom type hcxOc3PortLineAIS based on Integer32"""
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


_HcxOc3PortLineAIS_Type.__name__ = "Integer32"
_HcxOc3PortLineAIS_Object = MibTableColumn
hcxOc3PortLineAIS = _HcxOc3PortLineAIS_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 29),
    _HcxOc3PortLineAIS_Type()
)
hcxOc3PortLineAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortLineAIS.setStatus("current")


class _HcxOc3PortLineRDI_Type(Integer32):
    """Custom type hcxOc3PortLineRDI based on Integer32"""
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


_HcxOc3PortLineRDI_Type.__name__ = "Integer32"
_HcxOc3PortLineRDI_Object = MibTableColumn
hcxOc3PortLineRDI = _HcxOc3PortLineRDI_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 30),
    _HcxOc3PortLineRDI_Type()
)
hcxOc3PortLineRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortLineRDI.setStatus("current")


class _HcxOc3PortPathRDI_Type(Integer32):
    """Custom type hcxOc3PortPathRDI based on Integer32"""
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


_HcxOc3PortPathRDI_Type.__name__ = "Integer32"
_HcxOc3PortPathRDI_Object = MibTableColumn
hcxOc3PortPathRDI = _HcxOc3PortPathRDI_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 31),
    _HcxOc3PortPathRDI_Type()
)
hcxOc3PortPathRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortPathRDI.setStatus("current")
_HcxOc3PortAggrVoiceRate_Type = Integer32
_HcxOc3PortAggrVoiceRate_Object = MibTableColumn
hcxOc3PortAggrVoiceRate = _HcxOc3PortAggrVoiceRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 32),
    _HcxOc3PortAggrVoiceRate_Type()
)
hcxOc3PortAggrVoiceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortAggrVoiceRate.setStatus("current")
_HcxOc3PortAggrActVoiceRate_Type = Integer32
_HcxOc3PortAggrActVoiceRate_Object = MibTableColumn
hcxOc3PortAggrActVoiceRate = _HcxOc3PortAggrActVoiceRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 33),
    _HcxOc3PortAggrActVoiceRate_Type()
)
hcxOc3PortAggrActVoiceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortAggrActVoiceRate.setStatus("current")


class _HcxOc3PortLOFLed_Type(Integer32):
    """Custom type hcxOc3PortLOFLed based on Integer32"""
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


_HcxOc3PortLOFLed_Type.__name__ = "Integer32"
_HcxOc3PortLOFLed_Object = MibTableColumn
hcxOc3PortLOFLed = _HcxOc3PortLOFLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 92, 1, 1, 34),
    _HcxOc3PortLOFLed_Type()
)
hcxOc3PortLOFLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3PortLOFLed.setStatus("current")
_Com21HcxOc3VccGroup_ObjectIdentity = ObjectIdentity
com21HcxOc3VccGroup = _Com21HcxOc3VccGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93)
)
_Com21HcxOc3VccTable_Object = MibTable
com21HcxOc3VccTable = _Com21HcxOc3VccTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1)
)
if mibBuilder.loadTexts:
    com21HcxOc3VccTable.setStatus("current")
_Com21HcxOc3VccEntry_Object = MibTableRow
com21HcxOc3VccEntry = _Com21HcxOc3VccEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1, 1)
)
com21HcxOc3VccEntry.setIndexNames(
    (0, "COM21-HCXOC3-MIB", "hcxOc3VccShelfId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3VccSlotId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3VccPortId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3VccVpi"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3VccVci"),
)
if mibBuilder.loadTexts:
    com21HcxOc3VccEntry.setStatus("current")
_HcxOc3VccShelfId_Type = Integer32
_HcxOc3VccShelfId_Object = MibTableColumn
hcxOc3VccShelfId = _HcxOc3VccShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1, 1, 1),
    _HcxOc3VccShelfId_Type()
)
hcxOc3VccShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VccShelfId.setStatus("current")
_HcxOc3VccSlotId_Type = Integer32
_HcxOc3VccSlotId_Object = MibTableColumn
hcxOc3VccSlotId = _HcxOc3VccSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1, 1, 2),
    _HcxOc3VccSlotId_Type()
)
hcxOc3VccSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VccSlotId.setStatus("current")
_HcxOc3VccPortId_Type = Integer32
_HcxOc3VccPortId_Object = MibTableColumn
hcxOc3VccPortId = _HcxOc3VccPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1, 1, 3),
    _HcxOc3VccPortId_Type()
)
hcxOc3VccPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VccPortId.setStatus("current")
_HcxOc3VccVpi_Type = Integer32
_HcxOc3VccVpi_Object = MibTableColumn
hcxOc3VccVpi = _HcxOc3VccVpi_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1, 1, 4),
    _HcxOc3VccVpi_Type()
)
hcxOc3VccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VccVpi.setStatus("current")
_HcxOc3VccVci_Type = Integer32
_HcxOc3VccVci_Object = MibTableColumn
hcxOc3VccVci = _HcxOc3VccVci_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1, 1, 5),
    _HcxOc3VccVci_Type()
)
hcxOc3VccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VccVci.setStatus("current")


class _HcxOc3VccType_Type(Integer32):
    """Custom type hcxOc3VccType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_HcxOc3VccType_Type.__name__ = "Integer32"
_HcxOc3VccType_Object = MibTableColumn
hcxOc3VccType = _HcxOc3VccType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 93, 1, 1, 6),
    _HcxOc3VccType_Type()
)
hcxOc3VccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3VccType.setStatus("current")
_Com21HcxOc3StatsGroup_ObjectIdentity = ObjectIdentity
com21HcxOc3StatsGroup = _Com21HcxOc3StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94)
)
_Com21HcxOc3StatsTable_Object = MibTable
com21HcxOc3StatsTable = _Com21HcxOc3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1)
)
if mibBuilder.loadTexts:
    com21HcxOc3StatsTable.setStatus("current")
_Com21HcxOc3StatsEntry_Object = MibTableRow
com21HcxOc3StatsEntry = _Com21HcxOc3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1)
)
com21HcxOc3StatsEntry.setIndexNames(
    (0, "COM21-HCXOC3-MIB", "hcxOc3StatsShelfId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3StatsSlotId"),
    (0, "COM21-HCXOC3-MIB", "hcxOc3StatsPortId"),
)
if mibBuilder.loadTexts:
    com21HcxOc3StatsEntry.setStatus("current")
_HcxOc3StatsShelfId_Type = Integer32
_HcxOc3StatsShelfId_Object = MibTableColumn
hcxOc3StatsShelfId = _HcxOc3StatsShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 1),
    _HcxOc3StatsShelfId_Type()
)
hcxOc3StatsShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsShelfId.setStatus("current")
_HcxOc3StatsSlotId_Type = Integer32
_HcxOc3StatsSlotId_Object = MibTableColumn
hcxOc3StatsSlotId = _HcxOc3StatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 2),
    _HcxOc3StatsSlotId_Type()
)
hcxOc3StatsSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsSlotId.setStatus("current")
_HcxOc3StatsPortId_Type = Integer32
_HcxOc3StatsPortId_Object = MibTableColumn
hcxOc3StatsPortId = _HcxOc3StatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 3),
    _HcxOc3StatsPortId_Type()
)
hcxOc3StatsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsPortId.setStatus("current")
_HcxOc3StatsCurrSectionBIPErr_Type = Integer32
_HcxOc3StatsCurrSectionBIPErr_Object = MibTableColumn
hcxOc3StatsCurrSectionBIPErr = _HcxOc3StatsCurrSectionBIPErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 4),
    _HcxOc3StatsCurrSectionBIPErr_Type()
)
hcxOc3StatsCurrSectionBIPErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsCurrSectionBIPErr.setStatus("current")
_HcxOc3StatsCurrLineBIPErr_Type = Integer32
_HcxOc3StatsCurrLineBIPErr_Object = MibTableColumn
hcxOc3StatsCurrLineBIPErr = _HcxOc3StatsCurrLineBIPErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 5),
    _HcxOc3StatsCurrLineBIPErr_Type()
)
hcxOc3StatsCurrLineBIPErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsCurrLineBIPErr.setStatus("current")
_HcxOc3StatsCurrPathBIPErr_Type = Integer32
_HcxOc3StatsCurrPathBIPErr_Object = MibTableColumn
hcxOc3StatsCurrPathBIPErr = _HcxOc3StatsCurrPathBIPErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 6),
    _HcxOc3StatsCurrPathBIPErr_Type()
)
hcxOc3StatsCurrPathBIPErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsCurrPathBIPErr.setStatus("current")
_HcxOc3StatsCurrLineFEndBlockErr_Type = Integer32
_HcxOc3StatsCurrLineFEndBlockErr_Object = MibTableColumn
hcxOc3StatsCurrLineFEndBlockErr = _HcxOc3StatsCurrLineFEndBlockErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 7),
    _HcxOc3StatsCurrLineFEndBlockErr_Type()
)
hcxOc3StatsCurrLineFEndBlockErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsCurrLineFEndBlockErr.setStatus("current")
_HcxOc3StatsCurrPathFEndBlockErr_Type = Integer32
_HcxOc3StatsCurrPathFEndBlockErr_Object = MibTableColumn
hcxOc3StatsCurrPathFEndBlockErr = _HcxOc3StatsCurrPathFEndBlockErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 8),
    _HcxOc3StatsCurrPathFEndBlockErr_Type()
)
hcxOc3StatsCurrPathFEndBlockErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsCurrPathFEndBlockErr.setStatus("current")
_HcxOc3StatsPrevSectionBIPErr_Type = Integer32
_HcxOc3StatsPrevSectionBIPErr_Object = MibTableColumn
hcxOc3StatsPrevSectionBIPErr = _HcxOc3StatsPrevSectionBIPErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 9),
    _HcxOc3StatsPrevSectionBIPErr_Type()
)
hcxOc3StatsPrevSectionBIPErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsPrevSectionBIPErr.setStatus("current")
_HcxOc3StatsPrevLineBIPErr_Type = Integer32
_HcxOc3StatsPrevLineBIPErr_Object = MibTableColumn
hcxOc3StatsPrevLineBIPErr = _HcxOc3StatsPrevLineBIPErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 10),
    _HcxOc3StatsPrevLineBIPErr_Type()
)
hcxOc3StatsPrevLineBIPErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsPrevLineBIPErr.setStatus("current")
_HcxOc3StatsPrevPathBIPErr_Type = Integer32
_HcxOc3StatsPrevPathBIPErr_Object = MibTableColumn
hcxOc3StatsPrevPathBIPErr = _HcxOc3StatsPrevPathBIPErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 11),
    _HcxOc3StatsPrevPathBIPErr_Type()
)
hcxOc3StatsPrevPathBIPErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsPrevPathBIPErr.setStatus("current")
_HcxOc3StatsPrevLineFEndBlockErr_Type = Integer32
_HcxOc3StatsPrevLineFEndBlockErr_Object = MibTableColumn
hcxOc3StatsPrevLineFEndBlockErr = _HcxOc3StatsPrevLineFEndBlockErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 12),
    _HcxOc3StatsPrevLineFEndBlockErr_Type()
)
hcxOc3StatsPrevLineFEndBlockErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsPrevLineFEndBlockErr.setStatus("current")
_HcxOc3StatsPrevPathFEndBlockErr_Type = Integer32
_HcxOc3StatsPrevPathFEndBlockErr_Object = MibTableColumn
hcxOc3StatsPrevPathFEndBlockErr = _HcxOc3StatsPrevPathFEndBlockErr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 13),
    _HcxOc3StatsPrevPathFEndBlockErr_Type()
)
hcxOc3StatsPrevPathFEndBlockErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxOc3StatsPrevPathFEndBlockErr.setStatus("current")


class _HcxOc3StatsClear_Type(Integer32):
    """Custom type hcxOc3StatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxOc3StatsClear_Type.__name__ = "Integer32"
_HcxOc3StatsClear_Object = MibTableColumn
hcxOc3StatsClear = _HcxOc3StatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 94, 1, 1, 14),
    _HcxOc3StatsClear_Type()
)
hcxOc3StatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxOc3StatsClear.setStatus("current")

# Managed Objects groups


# Notification objects

hcxOc3UnitPrimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 150)
)
hcxOc3UnitPrimStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitPrimServState"))
)
if mibBuilder.loadTexts:
    hcxOc3UnitPrimStateChange.setStatus(
        "current"
    )

hcxOc3UnitSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 151)
)
hcxOc3UnitSecStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitSecServState"))
)
if mibBuilder.loadTexts:
    hcxOc3UnitSecStateChange.setStatus(
        "current"
    )

hcxOc3TestStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 152)
)
hcxOc3TestStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3TestStatusLed"))
)
if mibBuilder.loadTexts:
    hcxOc3TestStatusLedChange.setStatus(
        "current"
    )

hcxOc3FaultStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 153)
)
hcxOc3FaultStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3UnitSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3FaultStatusLed"))
)
if mibBuilder.loadTexts:
    hcxOc3FaultStatusLedChange.setStatus(
        "current"
    )

hcxOc3PortPrimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 154)
)
hcxOc3PortPrimStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortPrimServState"))
)
if mibBuilder.loadTexts:
    hcxOc3PortPrimStateChange.setStatus(
        "current"
    )

hcxOc3PortSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 155)
)
hcxOc3PortSecStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSecServState"))
)
if mibBuilder.loadTexts:
    hcxOc3PortSecStateChange.setStatus(
        "current"
    )

hcxOc3PortDiagTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 156)
)
hcxOc3PortDiagTestComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortDiagTestResult"))
)
if mibBuilder.loadTexts:
    hcxOc3PortDiagTestComplete.setStatus(
        "current"
    )

hcxOc3OperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 157)
)
hcxOc3OperationFailure.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3OperationFailure.setStatus(
        "current"
    )

hcxOc3PortLOSLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 158)
)
hcxOc3PortLOSLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortLOSLed"))
)
if mibBuilder.loadTexts:
    hcxOc3PortLOSLedChange.setStatus(
        "current"
    )

hcxOc3PortSectionLOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 159)
)
hcxOc3PortSectionLOSDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortSectionLOSDetected.setStatus(
        "current"
    )

hcxOc3PortSectionLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 160)
)
hcxOc3PortSectionLOSClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortSectionLOSClear.setStatus(
        "current"
    )

hcxOc3PortSectionLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 161)
)
hcxOc3PortSectionLOFDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortSectionLOFDetected.setStatus(
        "current"
    )

hcxOc3PortSectionLOFClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 162)
)
hcxOc3PortSectionLOFClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortSectionLOFClear.setStatus(
        "current"
    )

hcxOc3PortLineAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 163)
)
hcxOc3PortLineAISDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortLineAISDetected.setStatus(
        "current"
    )

hcxOc3PortLineAISClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 164)
)
hcxOc3PortLineAISClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortLineAISClear.setStatus(
        "current"
    )

hcxOc3PortLineRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 165)
)
hcxOc3PortLineRDIDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortLineRDIDetected.setStatus(
        "current"
    )

hcxOc3PortLineRDIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 166)
)
hcxOc3PortLineRDIClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortLineRDIClear.setStatus(
        "current"
    )

hcxOc3PortPathRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 167)
)
hcxOc3PortPathRDIDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortPathRDIDetected.setStatus(
        "current"
    )

hcxOc3PortPathRDIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 168)
)
hcxOc3PortPathRDIClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"))
)
if mibBuilder.loadTexts:
    hcxOc3PortPathRDIClear.setStatus(
        "current"
    )

hcxOc3PortLOFLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 169)
)
hcxOc3PortLOFLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortShelfId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortSlotId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortId"),
        ("COM21-HCXOC3-MIB", "hcxOc3PortLOFLed"))
)
if mibBuilder.loadTexts:
    hcxOc3PortLOFLedChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXOC3-MIB",
    **{"PrimServiceState": PrimServiceState,
       "Com21RowStatus": Com21RowStatus,
       "com21HcxOc3": com21HcxOc3,
       "com21HcxOc3UnitGroup": com21HcxOc3UnitGroup,
       "com21HcxOc3UnitTable": com21HcxOc3UnitTable,
       "com21HcxOc3UnitEntry": com21HcxOc3UnitEntry,
       "hcxOc3UnitShelfId": hcxOc3UnitShelfId,
       "hcxOc3UnitSlotId": hcxOc3UnitSlotId,
       "hcxOc3HardwareVersion": hcxOc3HardwareVersion,
       "hcxOc3BootVersion": hcxOc3BootVersion,
       "hcxOc3UnitPrimServState": hcxOc3UnitPrimServState,
       "hcxOc3UnitSecServState": hcxOc3UnitSecServState,
       "hcxOc3RestartAction": hcxOc3RestartAction,
       "hcxOc3TestStatusLed": hcxOc3TestStatusLed,
       "hcxOc3FaultStatusLed": hcxOc3FaultStatusLed,
       "hcxOc3SerialNumber": hcxOc3SerialNumber,
       "hcxOc3SyncClkConfigure": hcxOc3SyncClkConfigure,
       "com21HcxOc3PortGroup": com21HcxOc3PortGroup,
       "com21HcxOc3PortTable": com21HcxOc3PortTable,
       "com21HcxOc3PortEntry": com21HcxOc3PortEntry,
       "hcxOc3PortShelfId": hcxOc3PortShelfId,
       "hcxOc3PortSlotId": hcxOc3PortSlotId,
       "hcxOc3PortId": hcxOc3PortId,
       "hcxOc3PortPrimServState": hcxOc3PortPrimServState,
       "hcxOc3PortSecServState": hcxOc3PortSecServState,
       "hcxOc3MaxBandwidth": hcxOc3MaxBandwidth,
       "hcxOc3AggrDnStrmCbrRate": hcxOc3AggrDnStrmCbrRate,
       "hcxOc3AggrDnStrmPcrRate": hcxOc3AggrDnStrmPcrRate,
       "hcxOc3AggrUpStrmCbrRate": hcxOc3AggrUpStrmCbrRate,
       "hcxOc3AggrUpStrmMinRate": hcxOc3AggrUpStrmMinRate,
       "hcxOc3AggrUpStrmMaxRate": hcxOc3AggrUpStrmMaxRate,
       "hcxOc3AgeTime": hcxOc3AgeTime,
       "hcxOc3PortConfigState": hcxOc3PortConfigState,
       "hcxOc3PortRestartAction": hcxOc3PortRestartAction,
       "hcxOc3PortDiagTestAction": hcxOc3PortDiagTestAction,
       "hcxOc3PortDiagTestResult": hcxOc3PortDiagTestResult,
       "hcxOc3PortLOSLed": hcxOc3PortLOSLed,
       "hcxOc3AggrActDnStrmCbrRate": hcxOc3AggrActDnStrmCbrRate,
       "hcxOc3AggrActDnStrmPcrRate": hcxOc3AggrActDnStrmPcrRate,
       "hcxOc3AggrActUpStrmCbrRate": hcxOc3AggrActUpStrmCbrRate,
       "hcxOc3AggrActUpStrmMinRate": hcxOc3AggrActUpStrmMinRate,
       "hcxOc3AggrActUpStrmMaxRate": hcxOc3AggrActUpStrmMaxRate,
       "hcxOc3PortIpAddr": hcxOc3PortIpAddr,
       "hcxOc3PortIpMask": hcxOc3PortIpMask,
       "hcxOc3PortMacAddr": hcxOc3PortMacAddr,
       "hcxOc3Port1483EncapEnbl": hcxOc3Port1483EncapEnbl,
       "hcxOc3PortSectionLOS": hcxOc3PortSectionLOS,
       "hcxOc3PortSectionLOF": hcxOc3PortSectionLOF,
       "hcxOc3PortLineAIS": hcxOc3PortLineAIS,
       "hcxOc3PortLineRDI": hcxOc3PortLineRDI,
       "hcxOc3PortPathRDI": hcxOc3PortPathRDI,
       "hcxOc3PortAggrVoiceRate": hcxOc3PortAggrVoiceRate,
       "hcxOc3PortAggrActVoiceRate": hcxOc3PortAggrActVoiceRate,
       "hcxOc3PortLOFLed": hcxOc3PortLOFLed,
       "com21HcxOc3VccGroup": com21HcxOc3VccGroup,
       "com21HcxOc3VccTable": com21HcxOc3VccTable,
       "com21HcxOc3VccEntry": com21HcxOc3VccEntry,
       "hcxOc3VccShelfId": hcxOc3VccShelfId,
       "hcxOc3VccSlotId": hcxOc3VccSlotId,
       "hcxOc3VccPortId": hcxOc3VccPortId,
       "hcxOc3VccVpi": hcxOc3VccVpi,
       "hcxOc3VccVci": hcxOc3VccVci,
       "hcxOc3VccType": hcxOc3VccType,
       "com21HcxOc3StatsGroup": com21HcxOc3StatsGroup,
       "com21HcxOc3StatsTable": com21HcxOc3StatsTable,
       "com21HcxOc3StatsEntry": com21HcxOc3StatsEntry,
       "hcxOc3StatsShelfId": hcxOc3StatsShelfId,
       "hcxOc3StatsSlotId": hcxOc3StatsSlotId,
       "hcxOc3StatsPortId": hcxOc3StatsPortId,
       "hcxOc3StatsCurrSectionBIPErr": hcxOc3StatsCurrSectionBIPErr,
       "hcxOc3StatsCurrLineBIPErr": hcxOc3StatsCurrLineBIPErr,
       "hcxOc3StatsCurrPathBIPErr": hcxOc3StatsCurrPathBIPErr,
       "hcxOc3StatsCurrLineFEndBlockErr": hcxOc3StatsCurrLineFEndBlockErr,
       "hcxOc3StatsCurrPathFEndBlockErr": hcxOc3StatsCurrPathFEndBlockErr,
       "hcxOc3StatsPrevSectionBIPErr": hcxOc3StatsPrevSectionBIPErr,
       "hcxOc3StatsPrevLineBIPErr": hcxOc3StatsPrevLineBIPErr,
       "hcxOc3StatsPrevPathBIPErr": hcxOc3StatsPrevPathBIPErr,
       "hcxOc3StatsPrevLineFEndBlockErr": hcxOc3StatsPrevLineFEndBlockErr,
       "hcxOc3StatsPrevPathFEndBlockErr": hcxOc3StatsPrevPathFEndBlockErr,
       "hcxOc3StatsClear": hcxOc3StatsClear,
       "hcxOc3UnitPrimStateChange": hcxOc3UnitPrimStateChange,
       "hcxOc3UnitSecStateChange": hcxOc3UnitSecStateChange,
       "hcxOc3TestStatusLedChange": hcxOc3TestStatusLedChange,
       "hcxOc3FaultStatusLedChange": hcxOc3FaultStatusLedChange,
       "hcxOc3PortPrimStateChange": hcxOc3PortPrimStateChange,
       "hcxOc3PortSecStateChange": hcxOc3PortSecStateChange,
       "hcxOc3PortDiagTestComplete": hcxOc3PortDiagTestComplete,
       "hcxOc3OperationFailure": hcxOc3OperationFailure,
       "hcxOc3PortLOSLedChange": hcxOc3PortLOSLedChange,
       "hcxOc3PortSectionLOSDetected": hcxOc3PortSectionLOSDetected,
       "hcxOc3PortSectionLOSClear": hcxOc3PortSectionLOSClear,
       "hcxOc3PortSectionLOFDetected": hcxOc3PortSectionLOFDetected,
       "hcxOc3PortSectionLOFClear": hcxOc3PortSectionLOFClear,
       "hcxOc3PortLineAISDetected": hcxOc3PortLineAISDetected,
       "hcxOc3PortLineAISClear": hcxOc3PortLineAISClear,
       "hcxOc3PortLineRDIDetected": hcxOc3PortLineRDIDetected,
       "hcxOc3PortLineRDIClear": hcxOc3PortLineRDIClear,
       "hcxOc3PortPathRDIDetected": hcxOc3PortPathRDIDetected,
       "hcxOc3PortPathRDIClear": hcxOc3PortPathRDIClear,
       "hcxOc3PortLOFLedChange": hcxOc3PortLOFLedChange}
)
