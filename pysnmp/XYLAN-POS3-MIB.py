# SNMP MIB module (XYLAN-POS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-POS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:11 2024
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

(xylanPportArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanPportArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetPort_ObjectIdentity = ObjectIdentity
sonetPort = _SonetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4)
)
_SonetPortConfigTable_Object = MibTable
sonetPortConfigTable = _SonetPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1)
)
if mibBuilder.loadTexts:
    sonetPortConfigTable.setStatus("mandatory")
_SonetPortConfigEntry_Object = MibTableRow
sonetPortConfigEntry = _SonetPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1)
)
sonetPortConfigEntry.setIndexNames(
    (0, "XYLAN-POS3-MIB", "sonetPortConfigSlotIndex"),
    (0, "XYLAN-POS3-MIB", "sonetPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    sonetPortConfigEntry.setStatus("mandatory")


class _SonetPortConfigSlotIndex_Type(Integer32):
    """Custom type sonetPortConfigSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SonetPortConfigSlotIndex_Type.__name__ = "Integer32"
_SonetPortConfigSlotIndex_Object = MibTableColumn
sonetPortConfigSlotIndex = _SonetPortConfigSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 1),
    _SonetPortConfigSlotIndex_Type()
)
sonetPortConfigSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPortConfigSlotIndex.setStatus("mandatory")


class _SonetPortConfigPortIndex_Type(Integer32):
    """Custom type sonetPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonetPortConfigPortIndex_Type.__name__ = "Integer32"
_SonetPortConfigPortIndex_Object = MibTableColumn
sonetPortConfigPortIndex = _SonetPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 2),
    _SonetPortConfigPortIndex_Type()
)
sonetPortConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPortConfigPortIndex.setStatus("mandatory")
_SonetPortDescription_Type = DisplayString
_SonetPortDescription_Object = MibTableColumn
sonetPortDescription = _SonetPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 3),
    _SonetPortDescription_Type()
)
sonetPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortDescription.setStatus("mandatory")


class _SonetPortFramingType_Type(Integer32):
    """Custom type sonetPortFramingType based on Integer32"""
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


_SonetPortFramingType_Type.__name__ = "Integer32"
_SonetPortFramingType_Object = MibTableColumn
sonetPortFramingType = _SonetPortFramingType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 4),
    _SonetPortFramingType_Type()
)
sonetPortFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortFramingType.setStatus("mandatory")


class _SonetPortLoopbackConfig_Type(Integer32):
    """Custom type sonetPortLoopbackConfig based on Integer32"""
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
        *(("sonetLineLoop", 3),
          ("sonetNoLoop", 1),
          ("sonetOtherLoop", 4),
          ("sonetPayloadLoop", 2))
    )


_SonetPortLoopbackConfig_Type.__name__ = "Integer32"
_SonetPortLoopbackConfig_Object = MibTableColumn
sonetPortLoopbackConfig = _SonetPortLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 5),
    _SonetPortLoopbackConfig_Type()
)
sonetPortLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortLoopbackConfig.setStatus("mandatory")


class _SonetPortTransmitClockSource_Type(Integer32):
    """Custom type sonetPortTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1))
    )


_SonetPortTransmitClockSource_Type.__name__ = "Integer32"
_SonetPortTransmitClockSource_Object = MibTableColumn
sonetPortTransmitClockSource = _SonetPortTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 6),
    _SonetPortTransmitClockSource_Type()
)
sonetPortTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortTransmitClockSource.setStatus("mandatory")


class _SonetPortPlScramble_Type(Integer32):
    """Custom type sonetPortPlScramble based on Integer32"""
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


_SonetPortPlScramble_Type.__name__ = "Integer32"
_SonetPortPlScramble_Object = MibTableColumn
sonetPortPlScramble = _SonetPortPlScramble_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 7),
    _SonetPortPlScramble_Type()
)
sonetPortPlScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortPlScramble.setStatus("mandatory")


class _SonetPortStatusChangeTrapEnable_Type(Integer32):
    """Custom type sonetPortStatusChangeTrapEnable based on Integer32"""
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


_SonetPortStatusChangeTrapEnable_Type.__name__ = "Integer32"
_SonetPortStatusChangeTrapEnable_Object = MibTableColumn
sonetPortStatusChangeTrapEnable = _SonetPortStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 8),
    _SonetPortStatusChangeTrapEnable_Type()
)
sonetPortStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortStatusChangeTrapEnable.setStatus("mandatory")


class _SonetPortFcsSize_Type(Integer32):
    """Custom type sonetPortFcsSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcs16", 1),
          ("fcs32", 2))
    )


_SonetPortFcsSize_Type.__name__ = "Integer32"
_SonetPortFcsSize_Object = MibTableColumn
sonetPortFcsSize = _SonetPortFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 4, 1, 1, 9),
    _SonetPortFcsSize_Type()
)
sonetPortFcsSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPortFcsSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-POS3-MIB",
    **{"sonetPort": sonetPort,
       "sonetPortConfigTable": sonetPortConfigTable,
       "sonetPortConfigEntry": sonetPortConfigEntry,
       "sonetPortConfigSlotIndex": sonetPortConfigSlotIndex,
       "sonetPortConfigPortIndex": sonetPortConfigPortIndex,
       "sonetPortDescription": sonetPortDescription,
       "sonetPortFramingType": sonetPortFramingType,
       "sonetPortLoopbackConfig": sonetPortLoopbackConfig,
       "sonetPortTransmitClockSource": sonetPortTransmitClockSource,
       "sonetPortPlScramble": sonetPortPlScramble,
       "sonetPortStatusChangeTrapEnable": sonetPortStatusChangeTrapEnable,
       "sonetPortFcsSize": sonetPortFcsSize}
)
