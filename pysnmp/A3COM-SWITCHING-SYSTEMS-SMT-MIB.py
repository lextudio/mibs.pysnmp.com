# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-SMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-SMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:54 2024
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
 enterprises,
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
    "enterprises",
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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComSysSmt_ObjectIdentity = ObjectIdentity
a3ComSysSmt = _A3ComSysSmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9)
)
_A3ComSysSmtCount_Type = Integer32
_A3ComSysSmtCount_Object = MibScalar
a3ComSysSmtCount = _A3ComSysSmtCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 1),
    _A3ComSysSmtCount_Type()
)
a3ComSysSmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtCount.setStatus("mandatory")
_A3ComSysSmtFddiMacRateTable_Object = MibTable
a3ComSysSmtFddiMacRateTable = _A3ComSysSmtFddiMacRateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateTable.setStatus("mandatory")
_A3ComSysSmtFddiMacRateEntry_Object = MibTableRow
a3ComSysSmtFddiMacRateEntry = _A3ComSysSmtFddiMacRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1)
)
a3ComSysSmtFddiMacRateEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-SMT-MIB", "a3ComSysSmtFddiMacRateSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-SMT-MIB", "a3ComSysSmtFddiMacRateIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateEntry.setStatus("mandatory")


class _A3ComSysSmtFddiMacRateSmtIndex_Type(Integer32):
    """Custom type a3ComSysSmtFddiMacRateSmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysSmtFddiMacRateSmtIndex_Type.__name__ = "Integer32"
_A3ComSysSmtFddiMacRateSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiMacRateSmtIndex = _A3ComSysSmtFddiMacRateSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 1),
    _A3ComSysSmtFddiMacRateSmtIndex_Type()
)
a3ComSysSmtFddiMacRateSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateSmtIndex.setStatus("mandatory")


class _A3ComSysSmtFddiMacRateIndex_Type(Integer32):
    """Custom type a3ComSysSmtFddiMacRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysSmtFddiMacRateIndex_Type.__name__ = "Integer32"
_A3ComSysSmtFddiMacRateIndex_Object = MibTableColumn
a3ComSysSmtFddiMacRateIndex = _A3ComSysSmtFddiMacRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 2),
    _A3ComSysSmtFddiMacRateIndex_Type()
)
a3ComSysSmtFddiMacRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateIndex.setStatus("mandatory")
_A3ComSysSmtFddiMacRateByteReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRateByteReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateByteReceiveRate = _A3ComSysSmtFddiMacRateByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 3),
    _A3ComSysSmtFddiMacRateByteReceiveRate_Type()
)
a3ComSysSmtFddiMacRateByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateByteReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakByteReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakByteReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakByteReceiveRate = _A3ComSysSmtFddiMacRatePeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 4),
    _A3ComSysSmtFddiMacRatePeakByteReceiveRate_Type()
)
a3ComSysSmtFddiMacRatePeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakByteReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRateFrameReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRateFrameReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateFrameReceiveRate = _A3ComSysSmtFddiMacRateFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 5),
    _A3ComSysSmtFddiMacRateFrameReceiveRate_Type()
)
a3ComSysSmtFddiMacRateFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateFrameReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakFrameReceiveRate = _A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 6),
    _A3ComSysSmtFddiMacRatePeakFrameReceiveRate_Type()
)
a3ComSysSmtFddiMacRatePeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakFrameReceiveRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRateByteTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRateByteTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateByteTransmitRate = _A3ComSysSmtFddiMacRateByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 7),
    _A3ComSysSmtFddiMacRateByteTransmitRate_Type()
)
a3ComSysSmtFddiMacRateByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateByteTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakByteTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakByteTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakByteTransmitRate = _A3ComSysSmtFddiMacRatePeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 8),
    _A3ComSysSmtFddiMacRatePeakByteTransmitRate_Type()
)
a3ComSysSmtFddiMacRatePeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakByteTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRateFrameTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRateFrameTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRateFrameTransmitRate = _A3ComSysSmtFddiMacRateFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 9),
    _A3ComSysSmtFddiMacRateFrameTransmitRate_Type()
)
a3ComSysSmtFddiMacRateFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRateFrameTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Type = Integer32
_A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Object = MibTableColumn
a3ComSysSmtFddiMacRatePeakFrameTransmitRate = _A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 5, 1, 10),
    _A3ComSysSmtFddiMacRatePeakFrameTransmitRate_Type()
)
a3ComSysSmtFddiMacRatePeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiMacRatePeakFrameTransmitRate.setStatus("mandatory")
_A3ComSysSmtFddiPortTable_Object = MibTable
a3ComSysSmtFddiPortTable = _A3ComSysSmtFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortTable.setStatus("mandatory")
_A3ComSysSmtFddiPortEntry_Object = MibTableRow
a3ComSysSmtFddiPortEntry = _A3ComSysSmtFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1)
)
a3ComSysSmtFddiPortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-SMT-MIB", "a3ComSysSmtFddiPortSmtIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-SMT-MIB", "a3ComSysSmtFddiPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortEntry.setStatus("mandatory")


class _A3ComSysSmtFddiPortSmtIndex_Type(Integer32):
    """Custom type a3ComSysSmtFddiPortSmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysSmtFddiPortSmtIndex_Type.__name__ = "Integer32"
_A3ComSysSmtFddiPortSmtIndex_Object = MibTableColumn
a3ComSysSmtFddiPortSmtIndex = _A3ComSysSmtFddiPortSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 1),
    _A3ComSysSmtFddiPortSmtIndex_Type()
)
a3ComSysSmtFddiPortSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortSmtIndex.setStatus("mandatory")


class _A3ComSysSmtFddiPortIndex_Type(Integer32):
    """Custom type a3ComSysSmtFddiPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysSmtFddiPortIndex_Type.__name__ = "Integer32"
_A3ComSysSmtFddiPortIndex_Object = MibTableColumn
a3ComSysSmtFddiPortIndex = _A3ComSysSmtFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 2),
    _A3ComSysSmtFddiPortIndex_Type()
)
a3ComSysSmtFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortIndex.setStatus("mandatory")


class _A3ComSysSmtFddiPortLocationType_Type(Integer32):
    """Custom type a3ComSysSmtFddiPortLocationType based on Integer32"""
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
        *(("chassis", 3),
          ("modularCard", 4),
          ("modularSlot", 2),
          ("other", 1))
    )


_A3ComSysSmtFddiPortLocationType_Type.__name__ = "Integer32"
_A3ComSysSmtFddiPortLocationType_Object = MibTableColumn
a3ComSysSmtFddiPortLocationType = _A3ComSysSmtFddiPortLocationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 3),
    _A3ComSysSmtFddiPortLocationType_Type()
)
a3ComSysSmtFddiPortLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLocationType.setStatus("mandatory")
_A3ComSysSmtFddiPortLocationTypeIndex_Type = Integer32
_A3ComSysSmtFddiPortLocationTypeIndex_Object = MibTableColumn
a3ComSysSmtFddiPortLocationTypeIndex = _A3ComSysSmtFddiPortLocationTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 4),
    _A3ComSysSmtFddiPortLocationTypeIndex_Type()
)
a3ComSysSmtFddiPortLocationTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLocationTypeIndex.setStatus("mandatory")
_A3ComSysSmtFddiPortLocationLocalIndex_Type = Integer32
_A3ComSysSmtFddiPortLocationLocalIndex_Object = MibTableColumn
a3ComSysSmtFddiPortLocationLocalIndex = _A3ComSysSmtFddiPortLocationLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 5),
    _A3ComSysSmtFddiPortLocationLocalIndex_Type()
)
a3ComSysSmtFddiPortLocationLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLocationLocalIndex.setStatus("mandatory")


class _A3ComSysSmtFddiPortLabel_Type(DisplayString):
    """Custom type a3ComSysSmtFddiPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComSysSmtFddiPortLabel_Type.__name__ = "DisplayString"
_A3ComSysSmtFddiPortLabel_Object = MibTableColumn
a3ComSysSmtFddiPortLabel = _A3ComSysSmtFddiPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 6),
    _A3ComSysSmtFddiPortLabel_Type()
)
a3ComSysSmtFddiPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortLabel.setStatus("mandatory")
_A3ComSysSmtFddiPortSystemPhysicalConnectorId_Type = Integer32
_A3ComSysSmtFddiPortSystemPhysicalConnectorId_Object = MibTableColumn
a3ComSysSmtFddiPortSystemPhysicalConnectorId = _A3ComSysSmtFddiPortSystemPhysicalConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 6, 1, 7),
    _A3ComSysSmtFddiPortSystemPhysicalConnectorId_Type()
)
a3ComSysSmtFddiPortSystemPhysicalConnectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiPortSystemPhysicalConnectorId.setStatus("mandatory")
_A3ComSysSmtFddiStationModeTable_Object = MibTable
a3ComSysSmtFddiStationModeTable = _A3ComSysSmtFddiStationModeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 10)
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiStationModeTable.setStatus("mandatory")
_A3ComSysSmtFddiStationModeEntry_Object = MibTableRow
a3ComSysSmtFddiStationModeEntry = _A3ComSysSmtFddiStationModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 10, 1)
)
a3ComSysSmtFddiStationModeEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-SMT-MIB", "a3ComSysSmtFddiStationModeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-SMT-MIB", "a3ComSysSmtFddiStationModePortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysSmtFddiStationModeEntry.setStatus("mandatory")
_A3ComSysSmtFddiStationModeIndex_Type = Integer32
_A3ComSysSmtFddiStationModeIndex_Object = MibTableColumn
a3ComSysSmtFddiStationModeIndex = _A3ComSysSmtFddiStationModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 10, 1, 1),
    _A3ComSysSmtFddiStationModeIndex_Type()
)
a3ComSysSmtFddiStationModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiStationModeIndex.setStatus("mandatory")
_A3ComSysSmtFddiStationModePortIndex_Type = Integer32
_A3ComSysSmtFddiStationModePortIndex_Object = MibTableColumn
a3ComSysSmtFddiStationModePortIndex = _A3ComSysSmtFddiStationModePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 10, 1, 2),
    _A3ComSysSmtFddiStationModePortIndex_Type()
)
a3ComSysSmtFddiStationModePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiStationModePortIndex.setStatus("mandatory")


class _A3ComSysSmtFddiStationModeSelectablePorts_Type(Integer32):
    """Custom type a3ComSysSmtFddiStationModeSelectablePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysSmtFddiStationModeSelectablePorts_Type.__name__ = "Integer32"
_A3ComSysSmtFddiStationModeSelectablePorts_Object = MibTableColumn
a3ComSysSmtFddiStationModeSelectablePorts = _A3ComSysSmtFddiStationModeSelectablePorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 10, 1, 3),
    _A3ComSysSmtFddiStationModeSelectablePorts_Type()
)
a3ComSysSmtFddiStationModeSelectablePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiStationModeSelectablePorts.setStatus("mandatory")


class _A3ComSysSmtFddiStationModeCurrentMode_Type(Integer32):
    """Custom type a3ComSysSmtFddiStationModeCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("das", 3),
          ("sas-m", 1),
          ("sas-s", 2))
    )


_A3ComSysSmtFddiStationModeCurrentMode_Type.__name__ = "Integer32"
_A3ComSysSmtFddiStationModeCurrentMode_Object = MibTableColumn
a3ComSysSmtFddiStationModeCurrentMode = _A3ComSysSmtFddiStationModeCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 10, 1, 4),
    _A3ComSysSmtFddiStationModeCurrentMode_Type()
)
a3ComSysSmtFddiStationModeCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiStationModeCurrentMode.setStatus("mandatory")


class _A3ComSysSmtFddiStationModeRequestedMode_Type(Integer32):
    """Custom type a3ComSysSmtFddiStationModeRequestedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("das", 3),
          ("sas-m", 1),
          ("sas-s", 2))
    )


_A3ComSysSmtFddiStationModeRequestedMode_Type.__name__ = "Integer32"
_A3ComSysSmtFddiStationModeRequestedMode_Object = MibTableColumn
a3ComSysSmtFddiStationModeRequestedMode = _A3ComSysSmtFddiStationModeRequestedMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 9, 10, 1, 5),
    _A3ComSysSmtFddiStationModeRequestedMode_Type()
)
a3ComSysSmtFddiStationModeRequestedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysSmtFddiStationModeRequestedMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-SMT-MIB",
    **{"a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComSysSmt": a3ComSysSmt,
       "a3ComSysSmtCount": a3ComSysSmtCount,
       "a3ComSysSmtFddiMacRateTable": a3ComSysSmtFddiMacRateTable,
       "a3ComSysSmtFddiMacRateEntry": a3ComSysSmtFddiMacRateEntry,
       "a3ComSysSmtFddiMacRateSmtIndex": a3ComSysSmtFddiMacRateSmtIndex,
       "a3ComSysSmtFddiMacRateIndex": a3ComSysSmtFddiMacRateIndex,
       "a3ComSysSmtFddiMacRateByteReceiveRate": a3ComSysSmtFddiMacRateByteReceiveRate,
       "a3ComSysSmtFddiMacRatePeakByteReceiveRate": a3ComSysSmtFddiMacRatePeakByteReceiveRate,
       "a3ComSysSmtFddiMacRateFrameReceiveRate": a3ComSysSmtFddiMacRateFrameReceiveRate,
       "a3ComSysSmtFddiMacRatePeakFrameReceiveRate": a3ComSysSmtFddiMacRatePeakFrameReceiveRate,
       "a3ComSysSmtFddiMacRateByteTransmitRate": a3ComSysSmtFddiMacRateByteTransmitRate,
       "a3ComSysSmtFddiMacRatePeakByteTransmitRate": a3ComSysSmtFddiMacRatePeakByteTransmitRate,
       "a3ComSysSmtFddiMacRateFrameTransmitRate": a3ComSysSmtFddiMacRateFrameTransmitRate,
       "a3ComSysSmtFddiMacRatePeakFrameTransmitRate": a3ComSysSmtFddiMacRatePeakFrameTransmitRate,
       "a3ComSysSmtFddiPortTable": a3ComSysSmtFddiPortTable,
       "a3ComSysSmtFddiPortEntry": a3ComSysSmtFddiPortEntry,
       "a3ComSysSmtFddiPortSmtIndex": a3ComSysSmtFddiPortSmtIndex,
       "a3ComSysSmtFddiPortIndex": a3ComSysSmtFddiPortIndex,
       "a3ComSysSmtFddiPortLocationType": a3ComSysSmtFddiPortLocationType,
       "a3ComSysSmtFddiPortLocationTypeIndex": a3ComSysSmtFddiPortLocationTypeIndex,
       "a3ComSysSmtFddiPortLocationLocalIndex": a3ComSysSmtFddiPortLocationLocalIndex,
       "a3ComSysSmtFddiPortLabel": a3ComSysSmtFddiPortLabel,
       "a3ComSysSmtFddiPortSystemPhysicalConnectorId": a3ComSysSmtFddiPortSystemPhysicalConnectorId,
       "a3ComSysSmtFddiStationModeTable": a3ComSysSmtFddiStationModeTable,
       "a3ComSysSmtFddiStationModeEntry": a3ComSysSmtFddiStationModeEntry,
       "a3ComSysSmtFddiStationModeIndex": a3ComSysSmtFddiStationModeIndex,
       "a3ComSysSmtFddiStationModePortIndex": a3ComSysSmtFddiStationModePortIndex,
       "a3ComSysSmtFddiStationModeSelectablePorts": a3ComSysSmtFddiStationModeSelectablePorts,
       "a3ComSysSmtFddiStationModeCurrentMode": a3ComSysSmtFddiStationModeCurrentMode,
       "a3ComSysSmtFddiStationModeRequestedMode": a3ComSysSmtFddiStationModeRequestedMode}
)
