# SNMP MIB module (COM21-HCXETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXETH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:35 2024
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

com21HcxEth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 40)
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

_Com21HcxEtherUnitGroup_ObjectIdentity = ObjectIdentity
com21HcxEtherUnitGroup = _Com21HcxEtherUnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41)
)
_Com21HcxEtherUnitTable_Object = MibTable
com21HcxEtherUnitTable = _Com21HcxEtherUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1)
)
if mibBuilder.loadTexts:
    com21HcxEtherUnitTable.setStatus("current")
_Com21HcxEtherUnitEntry_Object = MibTableRow
com21HcxEtherUnitEntry = _Com21HcxEtherUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1)
)
com21HcxEtherUnitEntry.setIndexNames(
    (0, "COM21-HCXETH-MIB", "hcxEtherShelfId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherSlotId"),
)
if mibBuilder.loadTexts:
    com21HcxEtherUnitEntry.setStatus("current")


class _HcxEtherShelfId_Type(Integer32):
    """Custom type hcxEtherShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxEtherShelfId_Type.__name__ = "Integer32"
_HcxEtherShelfId_Object = MibTableColumn
hcxEtherShelfId = _HcxEtherShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 1),
    _HcxEtherShelfId_Type()
)
hcxEtherShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherShelfId.setStatus("current")
_HcxEtherSlotId_Type = Integer32
_HcxEtherSlotId_Object = MibTableColumn
hcxEtherSlotId = _HcxEtherSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 2),
    _HcxEtherSlotId_Type()
)
hcxEtherSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherSlotId.setStatus("current")


class _HcxEtherCardType_Type(Integer32):
    """Custom type hcxEtherCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onehundredBaseT", 2),
          ("tenBaseT", 1))
    )


_HcxEtherCardType_Type.__name__ = "Integer32"
_HcxEtherCardType_Object = MibTableColumn
hcxEtherCardType = _HcxEtherCardType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 3),
    _HcxEtherCardType_Type()
)
hcxEtherCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCardType.setStatus("current")


class _HcxEtherNoPorts_Type(Integer32):
    """Custom type hcxEtherNoPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HcxEtherNoPorts_Type.__name__ = "Integer32"
_HcxEtherNoPorts_Object = MibTableColumn
hcxEtherNoPorts = _HcxEtherNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 4),
    _HcxEtherNoPorts_Type()
)
hcxEtherNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherNoPorts.setStatus("current")


class _HcxEtherHardwareVersion_Type(DisplayString):
    """Custom type hcxEtherHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxEtherHardwareVersion_Type.__name__ = "DisplayString"
_HcxEtherHardwareVersion_Object = MibTableColumn
hcxEtherHardwareVersion = _HcxEtherHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 5),
    _HcxEtherHardwareVersion_Type()
)
hcxEtherHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherHardwareVersion.setStatus("current")


class _HcxEtherBootVersion_Type(DisplayString):
    """Custom type hcxEtherBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxEtherBootVersion_Type.__name__ = "DisplayString"
_HcxEtherBootVersion_Object = MibTableColumn
hcxEtherBootVersion = _HcxEtherBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 6),
    _HcxEtherBootVersion_Type()
)
hcxEtherBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherBootVersion.setStatus("current")
_HcxEtherUnitPrimServState_Type = PrimServiceState
_HcxEtherUnitPrimServState_Object = MibTableColumn
hcxEtherUnitPrimServState = _HcxEtherUnitPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 7),
    _HcxEtherUnitPrimServState_Type()
)
hcxEtherUnitPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherUnitPrimServState.setStatus("current")


class _HcxEtherUnitSecServState_Type(DisplayString):
    """Custom type hcxEtherUnitSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxEtherUnitSecServState_Type.__name__ = "DisplayString"
_HcxEtherUnitSecServState_Object = MibTableColumn
hcxEtherUnitSecServState = _HcxEtherUnitSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 8),
    _HcxEtherUnitSecServState_Type()
)
hcxEtherUnitSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherUnitSecServState.setStatus("current")


class _HcxEtherRestartAction_Type(Integer32):
    """Custom type hcxEtherRestartAction based on Integer32"""
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


_HcxEtherRestartAction_Type.__name__ = "Integer32"
_HcxEtherRestartAction_Object = MibTableColumn
hcxEtherRestartAction = _HcxEtherRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 9),
    _HcxEtherRestartAction_Type()
)
hcxEtherRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherRestartAction.setStatus("current")


class _HcxEtherTestStatusLed_Type(Integer32):
    """Custom type hcxEtherTestStatusLed based on Integer32"""
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


_HcxEtherTestStatusLed_Type.__name__ = "Integer32"
_HcxEtherTestStatusLed_Object = MibTableColumn
hcxEtherTestStatusLed = _HcxEtherTestStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 10),
    _HcxEtherTestStatusLed_Type()
)
hcxEtherTestStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherTestStatusLed.setStatus("current")


class _HcxEtherFaultStatusLed_Type(Integer32):
    """Custom type hcxEtherFaultStatusLed based on Integer32"""
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


_HcxEtherFaultStatusLed_Type.__name__ = "Integer32"
_HcxEtherFaultStatusLed_Object = MibTableColumn
hcxEtherFaultStatusLed = _HcxEtherFaultStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 11),
    _HcxEtherFaultStatusLed_Type()
)
hcxEtherFaultStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherFaultStatusLed.setStatus("current")


class _HcxEtherSerialNumber_Type(DisplayString):
    """Custom type hcxEtherSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxEtherSerialNumber_Type.__name__ = "DisplayString"
_HcxEtherSerialNumber_Object = MibTableColumn
hcxEtherSerialNumber = _HcxEtherSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 41, 1, 1, 12),
    _HcxEtherSerialNumber_Type()
)
hcxEtherSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherSerialNumber.setStatus("current")
_Com21HcxEtherPortGroup_ObjectIdentity = ObjectIdentity
com21HcxEtherPortGroup = _Com21HcxEtherPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42)
)
_Com21HcxEtherPortTable_Object = MibTable
com21HcxEtherPortTable = _Com21HcxEtherPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1)
)
if mibBuilder.loadTexts:
    com21HcxEtherPortTable.setStatus("current")
_Com21HcxEtherPortEntry_Object = MibTableRow
com21HcxEtherPortEntry = _Com21HcxEtherPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1)
)
com21HcxEtherPortEntry.setIndexNames(
    (0, "COM21-HCXETH-MIB", "hcxEtherPortShelfId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherPortSlotId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherPortId"),
)
if mibBuilder.loadTexts:
    com21HcxEtherPortEntry.setStatus("current")


class _HcxEtherPortShelfId_Type(Integer32):
    """Custom type hcxEtherPortShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxEtherPortShelfId_Type.__name__ = "Integer32"
_HcxEtherPortShelfId_Object = MibTableColumn
hcxEtherPortShelfId = _HcxEtherPortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 1),
    _HcxEtherPortShelfId_Type()
)
hcxEtherPortShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortShelfId.setStatus("current")
_HcxEtherPortSlotId_Type = Integer32
_HcxEtherPortSlotId_Object = MibTableColumn
hcxEtherPortSlotId = _HcxEtherPortSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 2),
    _HcxEtherPortSlotId_Type()
)
hcxEtherPortSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortSlotId.setStatus("current")


class _HcxEtherPortId_Type(Integer32):
    """Custom type hcxEtherPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HcxEtherPortId_Type.__name__ = "Integer32"
_HcxEtherPortId_Object = MibTableColumn
hcxEtherPortId = _HcxEtherPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 3),
    _HcxEtherPortId_Type()
)
hcxEtherPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortId.setStatus("current")


class _HcxEtherPortType_Type(Integer32):
    """Custom type hcxEtherPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onehundredBaseT", 2),
          ("tenBaseT", 1))
    )


_HcxEtherPortType_Type.__name__ = "Integer32"
_HcxEtherPortType_Object = MibTableColumn
hcxEtherPortType = _HcxEtherPortType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 4),
    _HcxEtherPortType_Type()
)
hcxEtherPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortType.setStatus("current")


class _HcxEtherPortService_Type(DisplayString):
    """Custom type hcxEtherPortService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxEtherPortService_Type.__name__ = "DisplayString"
_HcxEtherPortService_Object = MibTableColumn
hcxEtherPortService = _HcxEtherPortService_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 5),
    _HcxEtherPortService_Type()
)
hcxEtherPortService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortService.setStatus("current")
_HcxEtherPortPrimServState_Type = PrimServiceState
_HcxEtherPortPrimServState_Object = MibTableColumn
hcxEtherPortPrimServState = _HcxEtherPortPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 6),
    _HcxEtherPortPrimServState_Type()
)
hcxEtherPortPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortPrimServState.setStatus("current")


class _HcxEtherPortSecServState_Type(DisplayString):
    """Custom type hcxEtherPortSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxEtherPortSecServState_Type.__name__ = "DisplayString"
_HcxEtherPortSecServState_Object = MibTableColumn
hcxEtherPortSecServState = _HcxEtherPortSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 7),
    _HcxEtherPortSecServState_Type()
)
hcxEtherPortSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortSecServState.setStatus("current")


class _HcxEtherMaxBandwidth_Type(Integer32):
    """Custom type hcxEtherMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22222),
    )


_HcxEtherMaxBandwidth_Type.__name__ = "Integer32"
_HcxEtherMaxBandwidth_Object = MibTableColumn
hcxEtherMaxBandwidth = _HcxEtherMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 9),
    _HcxEtherMaxBandwidth_Type()
)
hcxEtherMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherMaxBandwidth.setStatus("current")
_HcxEtherAggrDnStrmCbrRate_Type = Integer32
_HcxEtherAggrDnStrmCbrRate_Object = MibTableColumn
hcxEtherAggrDnStrmCbrRate = _HcxEtherAggrDnStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 12),
    _HcxEtherAggrDnStrmCbrRate_Type()
)
hcxEtherAggrDnStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrDnStrmCbrRate.setStatus("current")
_HcxEtherAggrDnStrmPcrRate_Type = Integer32
_HcxEtherAggrDnStrmPcrRate_Object = MibTableColumn
hcxEtherAggrDnStrmPcrRate = _HcxEtherAggrDnStrmPcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 13),
    _HcxEtherAggrDnStrmPcrRate_Type()
)
hcxEtherAggrDnStrmPcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrDnStrmPcrRate.setStatus("current")
_HcxEtherAggrUpStrmCbrRate_Type = Integer32
_HcxEtherAggrUpStrmCbrRate_Object = MibTableColumn
hcxEtherAggrUpStrmCbrRate = _HcxEtherAggrUpStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 14),
    _HcxEtherAggrUpStrmCbrRate_Type()
)
hcxEtherAggrUpStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrUpStrmCbrRate.setStatus("current")
_HcxEtherAggrUpStrmMinRate_Type = Integer32
_HcxEtherAggrUpStrmMinRate_Object = MibTableColumn
hcxEtherAggrUpStrmMinRate = _HcxEtherAggrUpStrmMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 15),
    _HcxEtherAggrUpStrmMinRate_Type()
)
hcxEtherAggrUpStrmMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrUpStrmMinRate.setStatus("current")
_HcxEtherAggrUpStrmMaxRate_Type = Integer32
_HcxEtherAggrUpStrmMaxRate_Object = MibTableColumn
hcxEtherAggrUpStrmMaxRate = _HcxEtherAggrUpStrmMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 16),
    _HcxEtherAggrUpStrmMaxRate_Type()
)
hcxEtherAggrUpStrmMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrUpStrmMaxRate.setStatus("current")
_HcxEtherAgeTime_Type = Integer32
_HcxEtherAgeTime_Object = MibTableColumn
hcxEtherAgeTime = _HcxEtherAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 17),
    _HcxEtherAgeTime_Type()
)
hcxEtherAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherAgeTime.setStatus("current")


class _HcxEtherPortConfigState_Type(Integer32):
    """Custom type hcxEtherPortConfigState based on Integer32"""
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


_HcxEtherPortConfigState_Type.__name__ = "Integer32"
_HcxEtherPortConfigState_Object = MibTableColumn
hcxEtherPortConfigState = _HcxEtherPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 18),
    _HcxEtherPortConfigState_Type()
)
hcxEtherPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortConfigState.setStatus("current")


class _HcxEtherPortRestartAction_Type(Integer32):
    """Custom type hcxEtherPortRestartAction based on Integer32"""
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


_HcxEtherPortRestartAction_Type.__name__ = "Integer32"
_HcxEtherPortRestartAction_Object = MibTableColumn
hcxEtherPortRestartAction = _HcxEtherPortRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 19),
    _HcxEtherPortRestartAction_Type()
)
hcxEtherPortRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortRestartAction.setStatus("current")


class _HcxEtherPortDiagTestAction_Type(Integer32):
    """Custom type hcxEtherPortDiagTestAction based on Integer32"""
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


_HcxEtherPortDiagTestAction_Type.__name__ = "Integer32"
_HcxEtherPortDiagTestAction_Object = MibTableColumn
hcxEtherPortDiagTestAction = _HcxEtherPortDiagTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 20),
    _HcxEtherPortDiagTestAction_Type()
)
hcxEtherPortDiagTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortDiagTestAction.setStatus("current")


class _HcxEtherPortDiagTestResult_Type(Integer32):
    """Custom type hcxEtherPortDiagTestResult based on Integer32"""
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


_HcxEtherPortDiagTestResult_Type.__name__ = "Integer32"
_HcxEtherPortDiagTestResult_Object = MibTableColumn
hcxEtherPortDiagTestResult = _HcxEtherPortDiagTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 21),
    _HcxEtherPortDiagTestResult_Type()
)
hcxEtherPortDiagTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortDiagTestResult.setStatus("current")


class _HcxEtherPortLinkStatusLed_Type(Integer32):
    """Custom type hcxEtherPortLinkStatusLed based on Integer32"""
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


_HcxEtherPortLinkStatusLed_Type.__name__ = "Integer32"
_HcxEtherPortLinkStatusLed_Object = MibTableColumn
hcxEtherPortLinkStatusLed = _HcxEtherPortLinkStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 22),
    _HcxEtherPortLinkStatusLed_Type()
)
hcxEtherPortLinkStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortLinkStatusLed.setStatus("current")


class _HcxEtherPortArpFiltRate_Type(Integer32):
    """Custom type hcxEtherPortArpFiltRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 150000),
    )


_HcxEtherPortArpFiltRate_Type.__name__ = "Integer32"
_HcxEtherPortArpFiltRate_Object = MibTableColumn
hcxEtherPortArpFiltRate = _HcxEtherPortArpFiltRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 24),
    _HcxEtherPortArpFiltRate_Type()
)
hcxEtherPortArpFiltRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortArpFiltRate.setStatus("deprecated")
_HcxEtherAggrActDnStrmCbrRate_Type = Integer32
_HcxEtherAggrActDnStrmCbrRate_Object = MibTableColumn
hcxEtherAggrActDnStrmCbrRate = _HcxEtherAggrActDnStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 25),
    _HcxEtherAggrActDnStrmCbrRate_Type()
)
hcxEtherAggrActDnStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrActDnStrmCbrRate.setStatus("current")
_HcxEtherAggrActDnStrmPcrRate_Type = Integer32
_HcxEtherAggrActDnStrmPcrRate_Object = MibTableColumn
hcxEtherAggrActDnStrmPcrRate = _HcxEtherAggrActDnStrmPcrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 26),
    _HcxEtherAggrActDnStrmPcrRate_Type()
)
hcxEtherAggrActDnStrmPcrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrActDnStrmPcrRate.setStatus("current")
_HcxEtherAggrActUpStrmCbrRate_Type = Integer32
_HcxEtherAggrActUpStrmCbrRate_Object = MibTableColumn
hcxEtherAggrActUpStrmCbrRate = _HcxEtherAggrActUpStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 27),
    _HcxEtherAggrActUpStrmCbrRate_Type()
)
hcxEtherAggrActUpStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrActUpStrmCbrRate.setStatus("current")
_HcxEtherAggrActUpStrmMinRate_Type = Integer32
_HcxEtherAggrActUpStrmMinRate_Object = MibTableColumn
hcxEtherAggrActUpStrmMinRate = _HcxEtherAggrActUpStrmMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 28),
    _HcxEtherAggrActUpStrmMinRate_Type()
)
hcxEtherAggrActUpStrmMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrActUpStrmMinRate.setStatus("current")
_HcxEtherAggrActUpStrmMaxRate_Type = Integer32
_HcxEtherAggrActUpStrmMaxRate_Object = MibTableColumn
hcxEtherAggrActUpStrmMaxRate = _HcxEtherAggrActUpStrmMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 29),
    _HcxEtherAggrActUpStrmMaxRate_Type()
)
hcxEtherAggrActUpStrmMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherAggrActUpStrmMaxRate.setStatus("current")
_HcxEtherPortIpAddr_Type = IpAddress
_HcxEtherPortIpAddr_Object = MibTableColumn
hcxEtherPortIpAddr = _HcxEtherPortIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 30),
    _HcxEtherPortIpAddr_Type()
)
hcxEtherPortIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortIpAddr.setStatus("current")
_HcxEtherPortIpMask_Type = IpAddress
_HcxEtherPortIpMask_Object = MibTableColumn
hcxEtherPortIpMask = _HcxEtherPortIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 31),
    _HcxEtherPortIpMask_Type()
)
hcxEtherPortIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortIpMask.setStatus("current")
_HcxEtherPortMacAddr_Type = MacAddress
_HcxEtherPortMacAddr_Object = MibTableColumn
hcxEtherPortMacAddr = _HcxEtherPortMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 32),
    _HcxEtherPortMacAddr_Type()
)
hcxEtherPortMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPortMacAddr.setStatus("current")


class _HcxEtherPortAutoNegEnable_Type(Integer32):
    """Custom type hcxEtherPortAutoNegEnable based on Integer32"""
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


_HcxEtherPortAutoNegEnable_Type.__name__ = "Integer32"
_HcxEtherPortAutoNegEnable_Object = MibTableColumn
hcxEtherPortAutoNegEnable = _HcxEtherPortAutoNegEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 33),
    _HcxEtherPortAutoNegEnable_Type()
)
hcxEtherPortAutoNegEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortAutoNegEnable.setStatus("current")


class _HcxEtherPortSpeedSelect_Type(Integer32):
    """Custom type hcxEtherPortSpeedSelect based on Integer32"""
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
        *(("hundredMbpsFullDuplex", 4),
          ("hundredMbpsHalfDulplex", 3),
          ("tenMbpsFullDuplex", 2),
          ("tenMbpsHalfDuplex", 1))
    )


_HcxEtherPortSpeedSelect_Type.__name__ = "Integer32"
_HcxEtherPortSpeedSelect_Object = MibTableColumn
hcxEtherPortSpeedSelect = _HcxEtherPortSpeedSelect_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 34),
    _HcxEtherPortSpeedSelect_Type()
)
hcxEtherPortSpeedSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherPortSpeedSelect.setStatus("current")


class _HcxEtherCurrPortState_Type(Integer32):
    """Custom type hcxEtherCurrPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoNegFailure", 3),
          ("autoNegPending", 2),
          ("hundredMbpsFullDuplex", 7),
          ("hundredMbpsHalfDulplex", 6),
          ("linkFail", 1),
          ("tenMbpsFullDuplex", 5),
          ("tenMbpsHalfDuplex", 4))
    )


_HcxEtherCurrPortState_Type.__name__ = "Integer32"
_HcxEtherCurrPortState_Object = MibTableColumn
hcxEtherCurrPortState = _HcxEtherCurrPortState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 42, 1, 1, 35),
    _HcxEtherCurrPortState_Type()
)
hcxEtherCurrPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCurrPortState.setStatus("current")
_Com21HcxEtherStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxEtherStatsGroup = _Com21HcxEtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43)
)
_Com21HcxEtherStatsTable_Object = MibTable
com21HcxEtherStatsTable = _Com21HcxEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1)
)
if mibBuilder.loadTexts:
    com21HcxEtherStatsTable.setStatus("current")
_Com21HcxEtherStatsEntry_Object = MibTableRow
com21HcxEtherStatsEntry = _Com21HcxEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1)
)
com21HcxEtherStatsEntry.setIndexNames(
    (0, "COM21-HCXETH-MIB", "hcxEtherStatsShelfId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherStatsSlotId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherStatsPortId"),
)
if mibBuilder.loadTexts:
    com21HcxEtherStatsEntry.setStatus("current")


class _HcxEtherStatsShelfId_Type(Integer32):
    """Custom type hcxEtherStatsShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxEtherStatsShelfId_Type.__name__ = "Integer32"
_HcxEtherStatsShelfId_Object = MibTableColumn
hcxEtherStatsShelfId = _HcxEtherStatsShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 1),
    _HcxEtherStatsShelfId_Type()
)
hcxEtherStatsShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStatsShelfId.setStatus("current")
_HcxEtherStatsSlotId_Type = Integer32
_HcxEtherStatsSlotId_Object = MibTableColumn
hcxEtherStatsSlotId = _HcxEtherStatsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 2),
    _HcxEtherStatsSlotId_Type()
)
hcxEtherStatsSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStatsSlotId.setStatus("current")


class _HcxEtherStatsPortId_Type(Integer32):
    """Custom type hcxEtherStatsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HcxEtherStatsPortId_Type.__name__ = "Integer32"
_HcxEtherStatsPortId_Object = MibTableColumn
hcxEtherStatsPortId = _HcxEtherStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 3),
    _HcxEtherStatsPortId_Type()
)
hcxEtherStatsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStatsPortId.setStatus("current")
_HcxEtherCurrCollisions_Type = Gauge32
_HcxEtherCurrCollisions_Object = MibTableColumn
hcxEtherCurrCollisions = _HcxEtherCurrCollisions_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 4),
    _HcxEtherCurrCollisions_Type()
)
hcxEtherCurrCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCurrCollisions.setStatus("current")
_HcxEtherCurrRunts_Type = Gauge32
_HcxEtherCurrRunts_Object = MibTableColumn
hcxEtherCurrRunts = _HcxEtherCurrRunts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 5),
    _HcxEtherCurrRunts_Type()
)
hcxEtherCurrRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCurrRunts.setStatus("current")
_HcxEtherCurrGrunts_Type = Gauge32
_HcxEtherCurrGrunts_Object = MibTableColumn
hcxEtherCurrGrunts = _HcxEtherCurrGrunts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 6),
    _HcxEtherCurrGrunts_Type()
)
hcxEtherCurrGrunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCurrGrunts.setStatus("current")
_HcxEtherCurrCrcPkts_Type = Gauge32
_HcxEtherCurrCrcPkts_Object = MibTableColumn
hcxEtherCurrCrcPkts = _HcxEtherCurrCrcPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 7),
    _HcxEtherCurrCrcPkts_Type()
)
hcxEtherCurrCrcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCurrCrcPkts.setStatus("current")
_HcxEtherCurrTxPkts_Type = Gauge32
_HcxEtherCurrTxPkts_Object = MibTableColumn
hcxEtherCurrTxPkts = _HcxEtherCurrTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 8),
    _HcxEtherCurrTxPkts_Type()
)
hcxEtherCurrTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCurrTxPkts.setStatus("current")
_HcxEtherCurrRxPkts_Type = Gauge32
_HcxEtherCurrRxPkts_Object = MibTableColumn
hcxEtherCurrRxPkts = _HcxEtherCurrRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 9),
    _HcxEtherCurrRxPkts_Type()
)
hcxEtherCurrRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherCurrRxPkts.setStatus("current")
_HcxEtherPrevCollisions_Type = Gauge32
_HcxEtherPrevCollisions_Object = MibTableColumn
hcxEtherPrevCollisions = _HcxEtherPrevCollisions_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 10),
    _HcxEtherPrevCollisions_Type()
)
hcxEtherPrevCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPrevCollisions.setStatus("current")
_HcxEtherPrevRunts_Type = Gauge32
_HcxEtherPrevRunts_Object = MibTableColumn
hcxEtherPrevRunts = _HcxEtherPrevRunts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 11),
    _HcxEtherPrevRunts_Type()
)
hcxEtherPrevRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPrevRunts.setStatus("current")
_HcxEtherPrevGrunts_Type = Gauge32
_HcxEtherPrevGrunts_Object = MibTableColumn
hcxEtherPrevGrunts = _HcxEtherPrevGrunts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 12),
    _HcxEtherPrevGrunts_Type()
)
hcxEtherPrevGrunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPrevGrunts.setStatus("current")
_HcxEtherPrevCrcPkts_Type = Gauge32
_HcxEtherPrevCrcPkts_Object = MibTableColumn
hcxEtherPrevCrcPkts = _HcxEtherPrevCrcPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 13),
    _HcxEtherPrevCrcPkts_Type()
)
hcxEtherPrevCrcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPrevCrcPkts.setStatus("current")
_HcxEtherPrevTxPkts_Type = Gauge32
_HcxEtherPrevTxPkts_Object = MibTableColumn
hcxEtherPrevTxPkts = _HcxEtherPrevTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 14),
    _HcxEtherPrevTxPkts_Type()
)
hcxEtherPrevTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPrevTxPkts.setStatus("current")
_HcxEtherPrevRxPkts_Type = Gauge32
_HcxEtherPrevRxPkts_Object = MibTableColumn
hcxEtherPrevRxPkts = _HcxEtherPrevRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 15),
    _HcxEtherPrevRxPkts_Type()
)
hcxEtherPrevRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherPrevRxPkts.setStatus("current")


class _HcxEtherClearStats_Type(Integer32):
    """Custom type hcxEtherClearStats based on Integer32"""
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


_HcxEtherClearStats_Type.__name__ = "Integer32"
_HcxEtherClearStats_Object = MibTableColumn
hcxEtherClearStats = _HcxEtherClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 43, 1, 1, 16),
    _HcxEtherClearStats_Type()
)
hcxEtherClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherClearStats.setStatus("current")
_Com21HcxEtherIpAddrGroup_ObjectIdentity = ObjectIdentity
com21HcxEtherIpAddrGroup = _Com21HcxEtherIpAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44)
)
_Com21HcxEtherIpAddrTable_Object = MibTable
com21HcxEtherIpAddrTable = _Com21HcxEtherIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1)
)
if mibBuilder.loadTexts:
    com21HcxEtherIpAddrTable.setStatus("current")
_Com21HcxEtherIpAddrEntry_Object = MibTableRow
com21HcxEtherIpAddrEntry = _Com21HcxEtherIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1, 1)
)
com21HcxEtherIpAddrEntry.setIndexNames(
    (0, "COM21-HCXETH-MIB", "hcxEtherIpAddrShelfId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherIpAddrSlotId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherIpAddrPortId"),
    (0, "COM21-HCXETH-MIB", "hcxEtherIpAddrIPAddr"),
)
if mibBuilder.loadTexts:
    com21HcxEtherIpAddrEntry.setStatus("current")


class _HcxEtherIpAddrShelfId_Type(Integer32):
    """Custom type hcxEtherIpAddrShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxEtherIpAddrShelfId_Type.__name__ = "Integer32"
_HcxEtherIpAddrShelfId_Object = MibTableColumn
hcxEtherIpAddrShelfId = _HcxEtherIpAddrShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1, 1, 1),
    _HcxEtherIpAddrShelfId_Type()
)
hcxEtherIpAddrShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherIpAddrShelfId.setStatus("current")
_HcxEtherIpAddrSlotId_Type = Integer32
_HcxEtherIpAddrSlotId_Object = MibTableColumn
hcxEtherIpAddrSlotId = _HcxEtherIpAddrSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1, 1, 2),
    _HcxEtherIpAddrSlotId_Type()
)
hcxEtherIpAddrSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherIpAddrSlotId.setStatus("current")


class _HcxEtherIpAddrPortId_Type(Integer32):
    """Custom type hcxEtherIpAddrPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HcxEtherIpAddrPortId_Type.__name__ = "Integer32"
_HcxEtherIpAddrPortId_Object = MibTableColumn
hcxEtherIpAddrPortId = _HcxEtherIpAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1, 1, 3),
    _HcxEtherIpAddrPortId_Type()
)
hcxEtherIpAddrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherIpAddrPortId.setStatus("current")
_HcxEtherIpAddrIPAddr_Type = IpAddress
_HcxEtherIpAddrIPAddr_Object = MibTableColumn
hcxEtherIpAddrIPAddr = _HcxEtherIpAddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1, 1, 4),
    _HcxEtherIpAddrIPAddr_Type()
)
hcxEtherIpAddrIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherIpAddrIPAddr.setStatus("current")
_HcxEtherIpAddrIPMask_Type = IpAddress
_HcxEtherIpAddrIPMask_Object = MibTableColumn
hcxEtherIpAddrIPMask = _HcxEtherIpAddrIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1, 1, 5),
    _HcxEtherIpAddrIPMask_Type()
)
hcxEtherIpAddrIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherIpAddrIPMask.setStatus("current")
_HcxEtherIpAddrIPStatus_Type = Com21RowStatus
_HcxEtherIpAddrIPStatus_Object = MibTableColumn
hcxEtherIpAddrIPStatus = _HcxEtherIpAddrIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 44, 1, 1, 6),
    _HcxEtherIpAddrIPStatus_Type()
)
hcxEtherIpAddrIPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxEtherIpAddrIPStatus.setStatus("current")
_Com21HcxEtherStuStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxEtherStuStatsGroup = _Com21HcxEtherStuStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45)
)
_Com21HcxEtherStuStatsTable_Object = MibTable
com21HcxEtherStuStatsTable = _Com21HcxEtherStuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1)
)
if mibBuilder.loadTexts:
    com21HcxEtherStuStatsTable.setStatus("current")
_Com21HcxEtherStuStatsEntry_Object = MibTableRow
com21HcxEtherStuStatsEntry = _Com21HcxEtherStuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1)
)
com21HcxEtherStuStatsEntry.setIndexNames(
    (0, "COM21-HCXETH-MIB", "hcxEtherStuStatsMacAddr"),
)
if mibBuilder.loadTexts:
    com21HcxEtherStuStatsEntry.setStatus("current")
_HcxEtherStuStatsMacAddr_Type = MacAddress
_HcxEtherStuStatsMacAddr_Object = MibTableColumn
hcxEtherStuStatsMacAddr = _HcxEtherStuStatsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 1),
    _HcxEtherStuStatsMacAddr_Type()
)
hcxEtherStuStatsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuStatsMacAddr.setStatus("current")
_HcxEtherStuCurrDnstrmBytes_Type = Gauge32
_HcxEtherStuCurrDnstrmBytes_Object = MibTableColumn
hcxEtherStuCurrDnstrmBytes = _HcxEtherStuCurrDnstrmBytes_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 2),
    _HcxEtherStuCurrDnstrmBytes_Type()
)
hcxEtherStuCurrDnstrmBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuCurrDnstrmBytes.setStatus("current")
_HcxEtherStuCurrUpstrmBytes_Type = Gauge32
_HcxEtherStuCurrUpstrmBytes_Object = MibTableColumn
hcxEtherStuCurrUpstrmBytes = _HcxEtherStuCurrUpstrmBytes_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 3),
    _HcxEtherStuCurrUpstrmBytes_Type()
)
hcxEtherStuCurrUpstrmBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuCurrUpstrmBytes.setStatus("current")
_HcxEtherStuCurrUpstrmAal5CrcErrs_Type = Gauge32
_HcxEtherStuCurrUpstrmAal5CrcErrs_Object = MibTableColumn
hcxEtherStuCurrUpstrmAal5CrcErrs = _HcxEtherStuCurrUpstrmAal5CrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 4),
    _HcxEtherStuCurrUpstrmAal5CrcErrs_Type()
)
hcxEtherStuCurrUpstrmAal5CrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuCurrUpstrmAal5CrcErrs.setStatus("current")
_HcxEtherStuCurrDnstrmDropPkts_Type = Gauge32
_HcxEtherStuCurrDnstrmDropPkts_Object = MibTableColumn
hcxEtherStuCurrDnstrmDropPkts = _HcxEtherStuCurrDnstrmDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 5),
    _HcxEtherStuCurrDnstrmDropPkts_Type()
)
hcxEtherStuCurrDnstrmDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuCurrDnstrmDropPkts.setStatus("current")
_HcxEtherStuPrevDnstrmBytes_Type = Gauge32
_HcxEtherStuPrevDnstrmBytes_Object = MibTableColumn
hcxEtherStuPrevDnstrmBytes = _HcxEtherStuPrevDnstrmBytes_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 6),
    _HcxEtherStuPrevDnstrmBytes_Type()
)
hcxEtherStuPrevDnstrmBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuPrevDnstrmBytes.setStatus("current")
_HcxEtherStuPrevUpstrmBytes_Type = Gauge32
_HcxEtherStuPrevUpstrmBytes_Object = MibTableColumn
hcxEtherStuPrevUpstrmBytes = _HcxEtherStuPrevUpstrmBytes_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 7),
    _HcxEtherStuPrevUpstrmBytes_Type()
)
hcxEtherStuPrevUpstrmBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuPrevUpstrmBytes.setStatus("current")
_HcxEtherStuPrevUpstrmAal5CrcErrs_Type = Gauge32
_HcxEtherStuPrevUpstrmAal5CrcErrs_Object = MibTableColumn
hcxEtherStuPrevUpstrmAal5CrcErrs = _HcxEtherStuPrevUpstrmAal5CrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 8),
    _HcxEtherStuPrevUpstrmAal5CrcErrs_Type()
)
hcxEtherStuPrevUpstrmAal5CrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuPrevUpstrmAal5CrcErrs.setStatus("current")
_HcxEtherStuPrevDnstrmDropPkts_Type = Gauge32
_HcxEtherStuPrevDnstrmDropPkts_Object = MibTableColumn
hcxEtherStuPrevDnstrmDropPkts = _HcxEtherStuPrevDnstrmDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 9),
    _HcxEtherStuPrevDnstrmDropPkts_Type()
)
hcxEtherStuPrevDnstrmDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEtherStuPrevDnstrmDropPkts.setStatus("current")


class _HcxEtherStuClearStats_Type(Integer32):
    """Custom type hcxEtherStuClearStats based on Integer32"""
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


_HcxEtherStuClearStats_Type.__name__ = "Integer32"
_HcxEtherStuClearStats_Object = MibTableColumn
hcxEtherStuClearStats = _HcxEtherStuClearStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 45, 1, 1, 10),
    _HcxEtherStuClearStats_Type()
)
hcxEtherStuClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEtherStuClearStats.setStatus("current")
_Com21HcxServGrpAssocGroup_ObjectIdentity = ObjectIdentity
com21HcxServGrpAssocGroup = _Com21HcxServGrpAssocGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46)
)
_Com21HcxServGrpAssocTable_Object = MibTable
com21HcxServGrpAssocTable = _Com21HcxServGrpAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1)
)
if mibBuilder.loadTexts:
    com21HcxServGrpAssocTable.setStatus("current")
_Com21HcxServGrpAssocEntry_Object = MibTableRow
com21HcxServGrpAssocEntry = _Com21HcxServGrpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1)
)
com21HcxServGrpAssocEntry.setIndexNames(
    (0, "COM21-HCXETH-MIB", "hcxServGrpAssocShelfId"),
    (0, "COM21-HCXETH-MIB", "hcxServGrpAssocSlotId"),
    (0, "COM21-HCXETH-MIB", "hcxServGrpAssocCardType"),
    (0, "COM21-HCXETH-MIB", "hcxServGrpAssocPortId"),
    (0, "COM21-HCXETH-MIB", "hcxServGrpAssocEntryId"),
)
if mibBuilder.loadTexts:
    com21HcxServGrpAssocEntry.setStatus("current")


class _HcxServGrpAssocShelfId_Type(Integer32):
    """Custom type hcxServGrpAssocShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxServGrpAssocShelfId_Type.__name__ = "Integer32"
_HcxServGrpAssocShelfId_Object = MibTableColumn
hcxServGrpAssocShelfId = _HcxServGrpAssocShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 1),
    _HcxServGrpAssocShelfId_Type()
)
hcxServGrpAssocShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocShelfId.setStatus("current")


class _HcxServGrpAssocSlotId_Type(Integer32):
    """Custom type hcxServGrpAssocSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxServGrpAssocSlotId_Type.__name__ = "Integer32"
_HcxServGrpAssocSlotId_Object = MibTableColumn
hcxServGrpAssocSlotId = _HcxServGrpAssocSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 2),
    _HcxServGrpAssocSlotId_Type()
)
hcxServGrpAssocSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocSlotId.setStatus("current")


class _HcxServGrpAssocCardType_Type(Integer32):
    """Custom type hcxServGrpAssocCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oc3", 3),
          ("onehundredBaseT", 2),
          ("tenBaseT", 1))
    )


_HcxServGrpAssocCardType_Type.__name__ = "Integer32"
_HcxServGrpAssocCardType_Object = MibTableColumn
hcxServGrpAssocCardType = _HcxServGrpAssocCardType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 3),
    _HcxServGrpAssocCardType_Type()
)
hcxServGrpAssocCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocCardType.setStatus("current")
_HcxServGrpAssocPortId_Type = Integer32
_HcxServGrpAssocPortId_Object = MibTableColumn
hcxServGrpAssocPortId = _HcxServGrpAssocPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 4),
    _HcxServGrpAssocPortId_Type()
)
hcxServGrpAssocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocPortId.setStatus("current")
_HcxServGrpAssocEntryId_Type = Integer32
_HcxServGrpAssocEntryId_Object = MibTableColumn
hcxServGrpAssocEntryId = _HcxServGrpAssocEntryId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 5),
    _HcxServGrpAssocEntryId_Type()
)
hcxServGrpAssocEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocEntryId.setStatus("current")
_HcxServGrpAssocRate_Type = Integer32
_HcxServGrpAssocRate_Object = MibTableColumn
hcxServGrpAssocRate = _HcxServGrpAssocRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 6),
    _HcxServGrpAssocRate_Type()
)
hcxServGrpAssocRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocRate.setStatus("current")


class _HcxServGrpAssocType_Type(Integer32):
    """Custom type hcxServGrpAssocType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("ondemand", 2))
    )


_HcxServGrpAssocType_Type.__name__ = "Integer32"
_HcxServGrpAssocType_Object = MibTableColumn
hcxServGrpAssocType = _HcxServGrpAssocType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 7),
    _HcxServGrpAssocType_Type()
)
hcxServGrpAssocType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocType.setStatus("current")
_HcxServGrpAssocNumOfVlans_Type = Integer32
_HcxServGrpAssocNumOfVlans_Object = MibTableColumn
hcxServGrpAssocNumOfVlans = _HcxServGrpAssocNumOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 8),
    _HcxServGrpAssocNumOfVlans_Type()
)
hcxServGrpAssocNumOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocNumOfVlans.setStatus("current")
_HcxServGrpAssocNumOfStus_Type = Integer32
_HcxServGrpAssocNumOfStus_Object = MibTableColumn
hcxServGrpAssocNumOfStus = _HcxServGrpAssocNumOfStus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 46, 1, 1, 9),
    _HcxServGrpAssocNumOfStus_Type()
)
hcxServGrpAssocNumOfStus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServGrpAssocNumOfStus.setStatus("current")

# Managed Objects groups


# Notification objects

hcxEtherUnitPrimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 20)
)
hcxEtherUnitPrimStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherUnitPrimServState"))
)
if mibBuilder.loadTexts:
    hcxEtherUnitPrimStateChange.setStatus(
        "current"
    )

hcxEtherUnitSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 21)
)
hcxEtherUnitSecStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherUnitSecServState"))
)
if mibBuilder.loadTexts:
    hcxEtherUnitSecStateChange.setStatus(
        "current"
    )

hcxEtherTestStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 22)
)
hcxEtherTestStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherTestStatusLed"))
)
if mibBuilder.loadTexts:
    hcxEtherTestStatusLedChange.setStatus(
        "current"
    )

hcxEtherFaultStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 23)
)
hcxEtherFaultStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherFaultStatusLed"))
)
if mibBuilder.loadTexts:
    hcxEtherFaultStatusLedChange.setStatus(
        "current"
    )

hcxEtherPortPrimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 24)
)
hcxEtherPortPrimStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherPortShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortPrimServState"))
)
if mibBuilder.loadTexts:
    hcxEtherPortPrimStateChange.setStatus(
        "current"
    )

hcxEtherPortSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 25)
)
hcxEtherPortSecStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherPortShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortSecServState"))
)
if mibBuilder.loadTexts:
    hcxEtherPortSecStateChange.setStatus(
        "current"
    )

hcxEtherPortDiagTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 26)
)
hcxEtherPortDiagTestComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherPortShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortDiagTestResult"))
)
if mibBuilder.loadTexts:
    hcxEtherPortDiagTestComplete.setStatus(
        "current"
    )

hcxEtherOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 27)
)
hcxEtherOperationFailure.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherPortShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortId"))
)
if mibBuilder.loadTexts:
    hcxEtherOperationFailure.setStatus(
        "current"
    )

hcxEtherPortLinkStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 28)
)
hcxEtherPortLinkStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXETH-MIB", "hcxEtherPortShelfId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortSlotId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortId"),
        ("COM21-HCXETH-MIB", "hcxEtherPortLinkStatusLed"))
)
if mibBuilder.loadTexts:
    hcxEtherPortLinkStatusLedChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXETH-MIB",
    **{"PrimServiceState": PrimServiceState,
       "Com21RowStatus": Com21RowStatus,
       "com21HcxEth": com21HcxEth,
       "com21HcxEtherUnitGroup": com21HcxEtherUnitGroup,
       "com21HcxEtherUnitTable": com21HcxEtherUnitTable,
       "com21HcxEtherUnitEntry": com21HcxEtherUnitEntry,
       "hcxEtherShelfId": hcxEtherShelfId,
       "hcxEtherSlotId": hcxEtherSlotId,
       "hcxEtherCardType": hcxEtherCardType,
       "hcxEtherNoPorts": hcxEtherNoPorts,
       "hcxEtherHardwareVersion": hcxEtherHardwareVersion,
       "hcxEtherBootVersion": hcxEtherBootVersion,
       "hcxEtherUnitPrimServState": hcxEtherUnitPrimServState,
       "hcxEtherUnitSecServState": hcxEtherUnitSecServState,
       "hcxEtherRestartAction": hcxEtherRestartAction,
       "hcxEtherTestStatusLed": hcxEtherTestStatusLed,
       "hcxEtherFaultStatusLed": hcxEtherFaultStatusLed,
       "hcxEtherSerialNumber": hcxEtherSerialNumber,
       "com21HcxEtherPortGroup": com21HcxEtherPortGroup,
       "com21HcxEtherPortTable": com21HcxEtherPortTable,
       "com21HcxEtherPortEntry": com21HcxEtherPortEntry,
       "hcxEtherPortShelfId": hcxEtherPortShelfId,
       "hcxEtherPortSlotId": hcxEtherPortSlotId,
       "hcxEtherPortId": hcxEtherPortId,
       "hcxEtherPortType": hcxEtherPortType,
       "hcxEtherPortService": hcxEtherPortService,
       "hcxEtherPortPrimServState": hcxEtherPortPrimServState,
       "hcxEtherPortSecServState": hcxEtherPortSecServState,
       "hcxEtherMaxBandwidth": hcxEtherMaxBandwidth,
       "hcxEtherAggrDnStrmCbrRate": hcxEtherAggrDnStrmCbrRate,
       "hcxEtherAggrDnStrmPcrRate": hcxEtherAggrDnStrmPcrRate,
       "hcxEtherAggrUpStrmCbrRate": hcxEtherAggrUpStrmCbrRate,
       "hcxEtherAggrUpStrmMinRate": hcxEtherAggrUpStrmMinRate,
       "hcxEtherAggrUpStrmMaxRate": hcxEtherAggrUpStrmMaxRate,
       "hcxEtherAgeTime": hcxEtherAgeTime,
       "hcxEtherPortConfigState": hcxEtherPortConfigState,
       "hcxEtherPortRestartAction": hcxEtherPortRestartAction,
       "hcxEtherPortDiagTestAction": hcxEtherPortDiagTestAction,
       "hcxEtherPortDiagTestResult": hcxEtherPortDiagTestResult,
       "hcxEtherPortLinkStatusLed": hcxEtherPortLinkStatusLed,
       "hcxEtherPortArpFiltRate": hcxEtherPortArpFiltRate,
       "hcxEtherAggrActDnStrmCbrRate": hcxEtherAggrActDnStrmCbrRate,
       "hcxEtherAggrActDnStrmPcrRate": hcxEtherAggrActDnStrmPcrRate,
       "hcxEtherAggrActUpStrmCbrRate": hcxEtherAggrActUpStrmCbrRate,
       "hcxEtherAggrActUpStrmMinRate": hcxEtherAggrActUpStrmMinRate,
       "hcxEtherAggrActUpStrmMaxRate": hcxEtherAggrActUpStrmMaxRate,
       "hcxEtherPortIpAddr": hcxEtherPortIpAddr,
       "hcxEtherPortIpMask": hcxEtherPortIpMask,
       "hcxEtherPortMacAddr": hcxEtherPortMacAddr,
       "hcxEtherPortAutoNegEnable": hcxEtherPortAutoNegEnable,
       "hcxEtherPortSpeedSelect": hcxEtherPortSpeedSelect,
       "hcxEtherCurrPortState": hcxEtherCurrPortState,
       "com21HcxEtherStatsGroup": com21HcxEtherStatsGroup,
       "com21HcxEtherStatsTable": com21HcxEtherStatsTable,
       "com21HcxEtherStatsEntry": com21HcxEtherStatsEntry,
       "hcxEtherStatsShelfId": hcxEtherStatsShelfId,
       "hcxEtherStatsSlotId": hcxEtherStatsSlotId,
       "hcxEtherStatsPortId": hcxEtherStatsPortId,
       "hcxEtherCurrCollisions": hcxEtherCurrCollisions,
       "hcxEtherCurrRunts": hcxEtherCurrRunts,
       "hcxEtherCurrGrunts": hcxEtherCurrGrunts,
       "hcxEtherCurrCrcPkts": hcxEtherCurrCrcPkts,
       "hcxEtherCurrTxPkts": hcxEtherCurrTxPkts,
       "hcxEtherCurrRxPkts": hcxEtherCurrRxPkts,
       "hcxEtherPrevCollisions": hcxEtherPrevCollisions,
       "hcxEtherPrevRunts": hcxEtherPrevRunts,
       "hcxEtherPrevGrunts": hcxEtherPrevGrunts,
       "hcxEtherPrevCrcPkts": hcxEtherPrevCrcPkts,
       "hcxEtherPrevTxPkts": hcxEtherPrevTxPkts,
       "hcxEtherPrevRxPkts": hcxEtherPrevRxPkts,
       "hcxEtherClearStats": hcxEtherClearStats,
       "com21HcxEtherIpAddrGroup": com21HcxEtherIpAddrGroup,
       "com21HcxEtherIpAddrTable": com21HcxEtherIpAddrTable,
       "com21HcxEtherIpAddrEntry": com21HcxEtherIpAddrEntry,
       "hcxEtherIpAddrShelfId": hcxEtherIpAddrShelfId,
       "hcxEtherIpAddrSlotId": hcxEtherIpAddrSlotId,
       "hcxEtherIpAddrPortId": hcxEtherIpAddrPortId,
       "hcxEtherIpAddrIPAddr": hcxEtherIpAddrIPAddr,
       "hcxEtherIpAddrIPMask": hcxEtherIpAddrIPMask,
       "hcxEtherIpAddrIPStatus": hcxEtherIpAddrIPStatus,
       "com21HcxEtherStuStatsGroup": com21HcxEtherStuStatsGroup,
       "com21HcxEtherStuStatsTable": com21HcxEtherStuStatsTable,
       "com21HcxEtherStuStatsEntry": com21HcxEtherStuStatsEntry,
       "hcxEtherStuStatsMacAddr": hcxEtherStuStatsMacAddr,
       "hcxEtherStuCurrDnstrmBytes": hcxEtherStuCurrDnstrmBytes,
       "hcxEtherStuCurrUpstrmBytes": hcxEtherStuCurrUpstrmBytes,
       "hcxEtherStuCurrUpstrmAal5CrcErrs": hcxEtherStuCurrUpstrmAal5CrcErrs,
       "hcxEtherStuCurrDnstrmDropPkts": hcxEtherStuCurrDnstrmDropPkts,
       "hcxEtherStuPrevDnstrmBytes": hcxEtherStuPrevDnstrmBytes,
       "hcxEtherStuPrevUpstrmBytes": hcxEtherStuPrevUpstrmBytes,
       "hcxEtherStuPrevUpstrmAal5CrcErrs": hcxEtherStuPrevUpstrmAal5CrcErrs,
       "hcxEtherStuPrevDnstrmDropPkts": hcxEtherStuPrevDnstrmDropPkts,
       "hcxEtherStuClearStats": hcxEtherStuClearStats,
       "com21HcxServGrpAssocGroup": com21HcxServGrpAssocGroup,
       "com21HcxServGrpAssocTable": com21HcxServGrpAssocTable,
       "com21HcxServGrpAssocEntry": com21HcxServGrpAssocEntry,
       "hcxServGrpAssocShelfId": hcxServGrpAssocShelfId,
       "hcxServGrpAssocSlotId": hcxServGrpAssocSlotId,
       "hcxServGrpAssocCardType": hcxServGrpAssocCardType,
       "hcxServGrpAssocPortId": hcxServGrpAssocPortId,
       "hcxServGrpAssocEntryId": hcxServGrpAssocEntryId,
       "hcxServGrpAssocRate": hcxServGrpAssocRate,
       "hcxServGrpAssocType": hcxServGrpAssocType,
       "hcxServGrpAssocNumOfVlans": hcxServGrpAssocNumOfVlans,
       "hcxServGrpAssocNumOfStus": hcxServGrpAssocNumOfStus,
       "hcxEtherUnitPrimStateChange": hcxEtherUnitPrimStateChange,
       "hcxEtherUnitSecStateChange": hcxEtherUnitSecStateChange,
       "hcxEtherTestStatusLedChange": hcxEtherTestStatusLedChange,
       "hcxEtherFaultStatusLedChange": hcxEtherFaultStatusLedChange,
       "hcxEtherPortPrimStateChange": hcxEtherPortPrimStateChange,
       "hcxEtherPortSecStateChange": hcxEtherPortSecStateChange,
       "hcxEtherPortDiagTestComplete": hcxEtherPortDiagTestComplete,
       "hcxEtherOperationFailure": hcxEtherOperationFailure,
       "hcxEtherPortLinkStatusLedChange": hcxEtherPortLinkStatusLedChange}
)
