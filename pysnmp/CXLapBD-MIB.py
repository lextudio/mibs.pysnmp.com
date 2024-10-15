# SNMP MIB module (CXLapBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXLapBD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:36 2024
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
 cxLapBD) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxLapBD")

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



class Sapi(Integer32):
    """Custom type Sapi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              63)
        )
    )
    namedValues = NamedValues(
        *(("mngmt", 63),
          ("q930-q931", 0),
          ("x25", 16))
    )





class Tei(Integer32):
    """Custom type Tei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _LapbdLowerPoolThreshold_Type(Integer32):
    """Custom type lapbdLowerPoolThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LapbdLowerPoolThreshold_Type.__name__ = "Integer32"
_LapbdLowerPoolThreshold_Object = MibScalar
lapbdLowerPoolThreshold = _LapbdLowerPoolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 1),
    _LapbdLowerPoolThreshold_Type()
)
lapbdLowerPoolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdLowerPoolThreshold.setStatus("mandatory")


class _LapbdUpperPoolThreshold_Type(Integer32):
    """Custom type lapbdUpperPoolThreshold based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_LapbdUpperPoolThreshold_Type.__name__ = "Integer32"
_LapbdUpperPoolThreshold_Object = MibScalar
lapbdUpperPoolThreshold = _LapbdUpperPoolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 2),
    _LapbdUpperPoolThreshold_Type()
)
lapbdUpperPoolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdUpperPoolThreshold.setStatus("mandatory")


class _LapbdTraceSize_Type(Integer32):
    """Custom type lapbdTraceSize based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_LapbdTraceSize_Type.__name__ = "Integer32"
_LapbdTraceSize_Object = MibScalar
lapbdTraceSize = _LapbdTraceSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 3),
    _LapbdTraceSize_Type()
)
lapbdTraceSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdTraceSize.setStatus("mandatory")


class _LapbdTraceFlags_Type(Integer32):
    """Custom type lapbdTraceFlags based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LapbdTraceFlags_Type.__name__ = "Integer32"
_LapbdTraceFlags_Object = MibScalar
lapbdTraceFlags = _LapbdTraceFlags_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 4),
    _LapbdTraceFlags_Type()
)
lapbdTraceFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdTraceFlags.setStatus("mandatory")


class _LapbdTraps_Type(Integer32):
    """Custom type lapbdTraps based on Integer32"""
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


_LapbdTraps_Type.__name__ = "Integer32"
_LapbdTraps_Object = MibScalar
lapbdTraps = _LapbdTraps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 7),
    _LapbdTraps_Type()
)
lapbdTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdTraps.setStatus("mandatory")


class _LapbdStatusEvent_Type(Integer32):
    """Custom type lapbdStatusEvent based on Integer32"""
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
        *(("enteringCongestion", 2),
          ("exitingCongestion", 3),
          ("invTeiRemovalAttempt", 7),
          ("linkDown", 5),
          ("linkUp", 4),
          ("noEvent", 1),
          ("protocolError", 6))
    )


_LapbdStatusEvent_Type.__name__ = "Integer32"
_LapbdStatusEvent_Object = MibScalar
lapbdStatusEvent = _LapbdStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 8),
    _LapbdStatusEvent_Type()
)
lapbdStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdStatusEvent.setStatus("mandatory")
_LapbdSoftwareVersions_Type = DisplayString
_LapbdSoftwareVersions_Object = MibScalar
lapbdSoftwareVersions = _LapbdSoftwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 10),
    _LapbdSoftwareVersions_Type()
)
lapbdSoftwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdSoftwareVersions.setStatus("mandatory")
_LapbdMacSapTable_Object = MibTable
lapbdMacSapTable = _LapbdMacSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20)
)
if mibBuilder.loadTexts:
    lapbdMacSapTable.setStatus("mandatory")
_LapbdMacSapEntry_Object = MibTableRow
lapbdMacSapEntry = _LapbdMacSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1)
)
lapbdMacSapEntry.setIndexNames(
    (0, "CXLapBD-MIB", "lapbdMacSapNumber"),
)
if mibBuilder.loadTexts:
    lapbdMacSapEntry.setStatus("mandatory")
_LapbdMacSapNumber_Type = SapIndex
_LapbdMacSapNumber_Object = MibTableColumn
lapbdMacSapNumber = _LapbdMacSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 1),
    _LapbdMacSapNumber_Type()
)
lapbdMacSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapNumber.setStatus("mandatory")


class _LapbdMacSapRowStatus_Type(Integer32):
    """Custom type lapbdMacSapRowStatus based on Integer32"""
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


_LapbdMacSapRowStatus_Type.__name__ = "Integer32"
_LapbdMacSapRowStatus_Object = MibTableColumn
lapbdMacSapRowStatus = _LapbdMacSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 2),
    _LapbdMacSapRowStatus_Type()
)
lapbdMacSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapRowStatus.setStatus("mandatory")
_LapbdMacSapAlias_Type = Alias
_LapbdMacSapAlias_Object = MibTableColumn
lapbdMacSapAlias = _LapbdMacSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 3),
    _LapbdMacSapAlias_Type()
)
lapbdMacSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapAlias.setStatus("mandatory")
_LapbdMacSapCompanionAlias_Type = Alias
_LapbdMacSapCompanionAlias_Object = MibTableColumn
lapbdMacSapCompanionAlias = _LapbdMacSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 4),
    _LapbdMacSapCompanionAlias_Type()
)
lapbdMacSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapCompanionAlias.setStatus("mandatory")


class _LapbdMacSapLapType_Type(Integer32):
    """Custom type lapbdMacSapLapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lapb", 1),
          ("lapd", 2))
    )


_LapbdMacSapLapType_Type.__name__ = "Integer32"
_LapbdMacSapLapType_Object = MibTableColumn
lapbdMacSapLapType = _LapbdMacSapLapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 5),
    _LapbdMacSapLapType_Type()
)
lapbdMacSapLapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapLapType.setStatus("mandatory")


class _LapbdMacSapLogicalInterfaceType_Type(Integer32):
    """Custom type lapbdMacSapLogicalInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_LapbdMacSapLogicalInterfaceType_Type.__name__ = "Integer32"
_LapbdMacSapLogicalInterfaceType_Object = MibTableColumn
lapbdMacSapLogicalInterfaceType = _LapbdMacSapLogicalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 6),
    _LapbdMacSapLogicalInterfaceType_Type()
)
lapbdMacSapLogicalInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapLogicalInterfaceType.setStatus("mandatory")


class _LapbdMacSapArbitrationLogic_Type(Integer32):
    """Custom type lapbdMacSapArbitrationLogic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_LapbdMacSapArbitrationLogic_Type.__name__ = "Integer32"
_LapbdMacSapArbitrationLogic_Object = MibTableColumn
lapbdMacSapArbitrationLogic = _LapbdMacSapArbitrationLogic_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 7),
    _LapbdMacSapArbitrationLogic_Type()
)
lapbdMacSapArbitrationLogic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapArbitrationLogic.setStatus("mandatory")


class _LapbdMacSapLapDProtocolFlavor_Type(Integer32):
    """Custom type lapbdMacSapLapDProtocolFlavor based on Integer32"""
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
        *(("ccitt", 1),
          ("etsi", 3),
          ("vn3", 2))
    )


_LapbdMacSapLapDProtocolFlavor_Type.__name__ = "Integer32"
_LapbdMacSapLapDProtocolFlavor_Object = MibTableColumn
lapbdMacSapLapDProtocolFlavor = _LapbdMacSapLapDProtocolFlavor_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 8),
    _LapbdMacSapLapDProtocolFlavor_Type()
)
lapbdMacSapLapDProtocolFlavor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapLapDProtocolFlavor.setStatus("mandatory")


class _LapbdMacSapLapBProtocolFlavor_Type(Integer32):
    """Custom type lapbdMacSapLapBProtocolFlavor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("v8022", 2))
    )


_LapbdMacSapLapBProtocolFlavor_Type.__name__ = "Integer32"
_LapbdMacSapLapBProtocolFlavor_Object = MibTableColumn
lapbdMacSapLapBProtocolFlavor = _LapbdMacSapLapBProtocolFlavor_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 9),
    _LapbdMacSapLapBProtocolFlavor_Type()
)
lapbdMacSapLapBProtocolFlavor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapLapBProtocolFlavor.setStatus("mandatory")


class _LapbdMacSapWindow_Type(Integer32):
    """Custom type lapbdMacSapWindow based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbdMacSapWindow_Type.__name__ = "Integer32"
_LapbdMacSapWindow_Object = MibTableColumn
lapbdMacSapWindow = _LapbdMacSapWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 10),
    _LapbdMacSapWindow_Type()
)
lapbdMacSapWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapWindow.setStatus("mandatory")


class _LapbdMacSapTxQUpperThreshold_Type(Integer32):
    """Custom type lapbdMacSapTxQUpperThreshold based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LapbdMacSapTxQUpperThreshold_Type.__name__ = "Integer32"
_LapbdMacSapTxQUpperThreshold_Object = MibTableColumn
lapbdMacSapTxQUpperThreshold = _LapbdMacSapTxQUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 11),
    _LapbdMacSapTxQUpperThreshold_Type()
)
lapbdMacSapTxQUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapTxQUpperThreshold.setStatus("mandatory")


class _LapbdMacSapTxQLowerThreshold_Type(Integer32):
    """Custom type lapbdMacSapTxQLowerThreshold based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LapbdMacSapTxQLowerThreshold_Type.__name__ = "Integer32"
_LapbdMacSapTxQLowerThreshold_Object = MibTableColumn
lapbdMacSapTxQLowerThreshold = _LapbdMacSapTxQLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 12),
    _LapbdMacSapTxQLowerThreshold_Type()
)
lapbdMacSapTxQLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapTxQLowerThreshold.setStatus("mandatory")


class _LapbdMacSapConnectionTimer_Type(Integer32):
    """Custom type lapbdMacSapConnectionTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_LapbdMacSapConnectionTimer_Type.__name__ = "Integer32"
_LapbdMacSapConnectionTimer_Object = MibTableColumn
lapbdMacSapConnectionTimer = _LapbdMacSapConnectionTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 13),
    _LapbdMacSapConnectionTimer_Type()
)
lapbdMacSapConnectionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapConnectionTimer.setStatus("mandatory")


class _LapbdMacSapT202Timer_Type(Integer32):
    """Custom type lapbdMacSapT202Timer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_LapbdMacSapT202Timer_Type.__name__ = "Integer32"
_LapbdMacSapT202Timer_Object = MibTableColumn
lapbdMacSapT202Timer = _LapbdMacSapT202Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 14),
    _LapbdMacSapT202Timer_Type()
)
lapbdMacSapT202Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapT202Timer.setStatus("mandatory")


class _LapbdMacSapN202Counter_Type(Integer32):
    """Custom type lapbdMacSapN202Counter based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_LapbdMacSapN202Counter_Type.__name__ = "Integer32"
_LapbdMacSapN202Counter_Object = MibTableColumn
lapbdMacSapN202Counter = _LapbdMacSapN202Counter_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 15),
    _LapbdMacSapN202Counter_Type()
)
lapbdMacSapN202Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapN202Counter.setStatus("mandatory")


class _LapbdMacSapTeiCheckTimer_Type(Integer32):
    """Custom type lapbdMacSapTeiCheckTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_LapbdMacSapTeiCheckTimer_Type.__name__ = "Integer32"
_LapbdMacSapTeiCheckTimer_Object = MibTableColumn
lapbdMacSapTeiCheckTimer = _LapbdMacSapTeiCheckTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 16),
    _LapbdMacSapTeiCheckTimer_Type()
)
lapbdMacSapTeiCheckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapTeiCheckTimer.setStatus("mandatory")


class _LapbdMacSapT201Timer_Type(Integer32):
    """Custom type lapbdMacSapT201Timer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_LapbdMacSapT201Timer_Type.__name__ = "Integer32"
_LapbdMacSapT201Timer_Object = MibTableColumn
lapbdMacSapT201Timer = _LapbdMacSapT201Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 17),
    _LapbdMacSapT201Timer_Type()
)
lapbdMacSapT201Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapT201Timer.setStatus("mandatory")


class _LapbdMacSapLowTei_Type(Integer32):
    """Custom type lapbdMacSapLowTei based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LapbdMacSapLowTei_Type.__name__ = "Integer32"
_LapbdMacSapLowTei_Object = MibTableColumn
lapbdMacSapLowTei = _LapbdMacSapLowTei_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 18),
    _LapbdMacSapLowTei_Type()
)
lapbdMacSapLowTei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapLowTei.setStatus("mandatory")


class _LapbdMacSapKeepL1Up_Type(Integer32):
    """Custom type lapbdMacSapKeepL1Up based on Integer32"""
    defaultValue = 2

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


_LapbdMacSapKeepL1Up_Type.__name__ = "Integer32"
_LapbdMacSapKeepL1Up_Object = MibTableColumn
lapbdMacSapKeepL1Up = _LapbdMacSapKeepL1Up_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 19),
    _LapbdMacSapKeepL1Up_Type()
)
lapbdMacSapKeepL1Up.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdMacSapKeepL1Up.setStatus("mandatory")


class _LapbdMacSapControl_Type(Integer32):
    """Custom type lapbdMacSapControl based on Integer32"""
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
        *(("clearStats", 1),
          ("disableMacSap", 5),
          ("disableTrace", 3),
          ("enableMacSap", 4),
          ("enableTrace", 2))
    )


_LapbdMacSapControl_Type.__name__ = "Integer32"
_LapbdMacSapControl_Object = MibTableColumn
lapbdMacSapControl = _LapbdMacSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 30),
    _LapbdMacSapControl_Type()
)
lapbdMacSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lapbdMacSapControl.setStatus("mandatory")


class _LapbdMacSapHighLevelState_Type(Integer32):
    """Custom type lapbdMacSapHighLevelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("configured", 2),
          ("unbound", 1))
    )


_LapbdMacSapHighLevelState_Type.__name__ = "Integer32"
_LapbdMacSapHighLevelState_Object = MibTableColumn
lapbdMacSapHighLevelState = _LapbdMacSapHighLevelState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 35),
    _LapbdMacSapHighLevelState_Type()
)
lapbdMacSapHighLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapHighLevelState.setStatus("mandatory")


class _LapbdMacSapFlowControlState_Type(Integer32):
    """Custom type lapbdMacSapFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flowNormal", 1),
          ("flowStopped", 2),
          ("noFlow", 3))
    )


_LapbdMacSapFlowControlState_Type.__name__ = "Integer32"
_LapbdMacSapFlowControlState_Object = MibTableColumn
lapbdMacSapFlowControlState = _LapbdMacSapFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 36),
    _LapbdMacSapFlowControlState_Type()
)
lapbdMacSapFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapFlowControlState.setStatus("mandatory")
_LapbdMacSapOutstandingFrames_Type = Counter32
_LapbdMacSapOutstandingFrames_Object = MibTableColumn
lapbdMacSapOutstandingFrames = _LapbdMacSapOutstandingFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 37),
    _LapbdMacSapOutstandingFrames_Type()
)
lapbdMacSapOutstandingFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapOutstandingFrames.setStatus("mandatory")
_LapbdMacSapTotalFramesDropped_Type = Counter32
_LapbdMacSapTotalFramesDropped_Object = MibTableColumn
lapbdMacSapTotalFramesDropped = _LapbdMacSapTotalFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 38),
    _LapbdMacSapTotalFramesDropped_Type()
)
lapbdMacSapTotalFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTotalFramesDropped.setStatus("mandatory")
_LapbdMacSapActiveSaps_Type = Counter32
_LapbdMacSapActiveSaps_Object = MibTableColumn
lapbdMacSapActiveSaps = _LapbdMacSapActiveSaps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 39),
    _LapbdMacSapActiveSaps_Type()
)
lapbdMacSapActiveSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapActiveSaps.setStatus("mandatory")
_LapbdMacSapTxIFrames_Type = Counter32
_LapbdMacSapTxIFrames_Object = MibTableColumn
lapbdMacSapTxIFrames = _LapbdMacSapTxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 50),
    _LapbdMacSapTxIFrames_Type()
)
lapbdMacSapTxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxIFrames.setStatus("mandatory")
_LapbdMacSapRxIFrames_Type = Counter32
_LapbdMacSapRxIFrames_Object = MibTableColumn
lapbdMacSapRxIFrames = _LapbdMacSapRxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 51),
    _LapbdMacSapRxIFrames_Type()
)
lapbdMacSapRxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxIFrames.setStatus("mandatory")
_LapbdMacSapTxRrFrames_Type = Counter32
_LapbdMacSapTxRrFrames_Object = MibTableColumn
lapbdMacSapTxRrFrames = _LapbdMacSapTxRrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 52),
    _LapbdMacSapTxRrFrames_Type()
)
lapbdMacSapTxRrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxRrFrames.setStatus("mandatory")
_LapbdMacSapRxRrFrames_Type = Counter32
_LapbdMacSapRxRrFrames_Object = MibTableColumn
lapbdMacSapRxRrFrames = _LapbdMacSapRxRrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 53),
    _LapbdMacSapRxRrFrames_Type()
)
lapbdMacSapRxRrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxRrFrames.setStatus("mandatory")
_LapbdMacSapTxRnrFrames_Type = Counter32
_LapbdMacSapTxRnrFrames_Object = MibTableColumn
lapbdMacSapTxRnrFrames = _LapbdMacSapTxRnrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 54),
    _LapbdMacSapTxRnrFrames_Type()
)
lapbdMacSapTxRnrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxRnrFrames.setStatus("mandatory")
_LapbdMacSapRxRnrFrames_Type = Counter32
_LapbdMacSapRxRnrFrames_Object = MibTableColumn
lapbdMacSapRxRnrFrames = _LapbdMacSapRxRnrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 55),
    _LapbdMacSapRxRnrFrames_Type()
)
lapbdMacSapRxRnrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxRnrFrames.setStatus("mandatory")
_LapbdMacSapTxRejFrames_Type = Counter32
_LapbdMacSapTxRejFrames_Object = MibTableColumn
lapbdMacSapTxRejFrames = _LapbdMacSapTxRejFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 56),
    _LapbdMacSapTxRejFrames_Type()
)
lapbdMacSapTxRejFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxRejFrames.setStatus("mandatory")
_LapbdMacSapRxRejFrames_Type = Counter32
_LapbdMacSapRxRejFrames_Object = MibTableColumn
lapbdMacSapRxRejFrames = _LapbdMacSapRxRejFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 57),
    _LapbdMacSapRxRejFrames_Type()
)
lapbdMacSapRxRejFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxRejFrames.setStatus("mandatory")
_LapbdMacSapTxSabmFrames_Type = Counter32
_LapbdMacSapTxSabmFrames_Object = MibTableColumn
lapbdMacSapTxSabmFrames = _LapbdMacSapTxSabmFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 58),
    _LapbdMacSapTxSabmFrames_Type()
)
lapbdMacSapTxSabmFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxSabmFrames.setStatus("mandatory")
_LapbdMacSapRxSabmFrames_Type = Counter32
_LapbdMacSapRxSabmFrames_Object = MibTableColumn
lapbdMacSapRxSabmFrames = _LapbdMacSapRxSabmFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 59),
    _LapbdMacSapRxSabmFrames_Type()
)
lapbdMacSapRxSabmFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxSabmFrames.setStatus("mandatory")
_LapbdMacSapTxDiscFrames_Type = Counter32
_LapbdMacSapTxDiscFrames_Object = MibTableColumn
lapbdMacSapTxDiscFrames = _LapbdMacSapTxDiscFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 60),
    _LapbdMacSapTxDiscFrames_Type()
)
lapbdMacSapTxDiscFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxDiscFrames.setStatus("mandatory")
_LapbdMacSapRxDiscFrames_Type = Counter32
_LapbdMacSapRxDiscFrames_Object = MibTableColumn
lapbdMacSapRxDiscFrames = _LapbdMacSapRxDiscFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 61),
    _LapbdMacSapRxDiscFrames_Type()
)
lapbdMacSapRxDiscFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxDiscFrames.setStatus("mandatory")
_LapbdMacSapTxUaFrames_Type = Counter32
_LapbdMacSapTxUaFrames_Object = MibTableColumn
lapbdMacSapTxUaFrames = _LapbdMacSapTxUaFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 62),
    _LapbdMacSapTxUaFrames_Type()
)
lapbdMacSapTxUaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxUaFrames.setStatus("mandatory")
_LapbdMacSapRxUaFrames_Type = Counter32
_LapbdMacSapRxUaFrames_Object = MibTableColumn
lapbdMacSapRxUaFrames = _LapbdMacSapRxUaFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 63),
    _LapbdMacSapRxUaFrames_Type()
)
lapbdMacSapRxUaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxUaFrames.setStatus("mandatory")
_LapbdMacSapTxDmFrames_Type = Counter32
_LapbdMacSapTxDmFrames_Object = MibTableColumn
lapbdMacSapTxDmFrames = _LapbdMacSapTxDmFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 64),
    _LapbdMacSapTxDmFrames_Type()
)
lapbdMacSapTxDmFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxDmFrames.setStatus("mandatory")
_LapbdMacSapRxDmFrames_Type = Counter32
_LapbdMacSapRxDmFrames_Object = MibTableColumn
lapbdMacSapRxDmFrames = _LapbdMacSapRxDmFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 65),
    _LapbdMacSapRxDmFrames_Type()
)
lapbdMacSapRxDmFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxDmFrames.setStatus("mandatory")
_LapbdMacSapTxFrmrFrames_Type = Counter32
_LapbdMacSapTxFrmrFrames_Object = MibTableColumn
lapbdMacSapTxFrmrFrames = _LapbdMacSapTxFrmrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 66),
    _LapbdMacSapTxFrmrFrames_Type()
)
lapbdMacSapTxFrmrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxFrmrFrames.setStatus("mandatory")
_LapbdMacSapRxFrmrFrames_Type = Counter32
_LapbdMacSapRxFrmrFrames_Object = MibTableColumn
lapbdMacSapRxFrmrFrames = _LapbdMacSapRxFrmrFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 67),
    _LapbdMacSapRxFrmrFrames_Type()
)
lapbdMacSapRxFrmrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxFrmrFrames.setStatus("mandatory")
_LapbdMacSapTxUiFrames_Type = Counter32
_LapbdMacSapTxUiFrames_Object = MibTableColumn
lapbdMacSapTxUiFrames = _LapbdMacSapTxUiFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 68),
    _LapbdMacSapTxUiFrames_Type()
)
lapbdMacSapTxUiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxUiFrames.setStatus("mandatory")
_LapbdMacSapRxUiFrames_Type = Counter32
_LapbdMacSapRxUiFrames_Object = MibTableColumn
lapbdMacSapRxUiFrames = _LapbdMacSapRxUiFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 69),
    _LapbdMacSapRxUiFrames_Type()
)
lapbdMacSapRxUiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxUiFrames.setStatus("mandatory")
_LapbdMacSapTxXidFrames_Type = Counter32
_LapbdMacSapTxXidFrames_Object = MibTableColumn
lapbdMacSapTxXidFrames = _LapbdMacSapTxXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 70),
    _LapbdMacSapTxXidFrames_Type()
)
lapbdMacSapTxXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapTxXidFrames.setStatus("mandatory")
_LapbdMacSapRxXidFrames_Type = Counter32
_LapbdMacSapRxXidFrames_Object = MibTableColumn
lapbdMacSapRxXidFrames = _LapbdMacSapRxXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 71),
    _LapbdMacSapRxXidFrames_Type()
)
lapbdMacSapRxXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxXidFrames.setStatus("mandatory")
_LapbdMacSapRxInvalidFrames_Type = Counter32
_LapbdMacSapRxInvalidFrames_Object = MibTableColumn
lapbdMacSapRxInvalidFrames = _LapbdMacSapRxInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 72),
    _LapbdMacSapRxInvalidFrames_Type()
)
lapbdMacSapRxInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxInvalidFrames.setStatus("mandatory")
_LapbdMacSapRxInvalidDiscards_Type = Counter32
_LapbdMacSapRxInvalidDiscards_Object = MibTableColumn
lapbdMacSapRxInvalidDiscards = _LapbdMacSapRxInvalidDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 73),
    _LapbdMacSapRxInvalidDiscards_Type()
)
lapbdMacSapRxInvalidDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapRxInvalidDiscards.setStatus("mandatory")
_LapbdMacSapSabmErrors_Type = Counter32
_LapbdMacSapSabmErrors_Object = MibTableColumn
lapbdMacSapSabmErrors = _LapbdMacSapSabmErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 74),
    _LapbdMacSapSabmErrors_Type()
)
lapbdMacSapSabmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapSabmErrors.setStatus("mandatory")
_LapbdMacSapFrmrErrors_Type = Counter32
_LapbdMacSapFrmrErrors_Object = MibTableColumn
lapbdMacSapFrmrErrors = _LapbdMacSapFrmrErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 20, 1, 75),
    _LapbdMacSapFrmrErrors_Type()
)
lapbdMacSapFrmrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdMacSapFrmrErrors.setStatus("mandatory")
_LapbdDlSapTable_Object = MibTable
lapbdDlSapTable = _LapbdDlSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21)
)
if mibBuilder.loadTexts:
    lapbdDlSapTable.setStatus("mandatory")
_LapbdDlSapEntry_Object = MibTableRow
lapbdDlSapEntry = _LapbdDlSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1)
)
lapbdDlSapEntry.setIndexNames(
    (0, "CXLapBD-MIB", "lapbdDlSapMacSapNumber"),
    (0, "CXLapBD-MIB", "lapbdDlSapNumber"),
)
if mibBuilder.loadTexts:
    lapbdDlSapEntry.setStatus("mandatory")
_LapbdDlSapMacSapNumber_Type = SapIndex
_LapbdDlSapMacSapNumber_Object = MibTableColumn
lapbdDlSapMacSapNumber = _LapbdDlSapMacSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 1),
    _LapbdDlSapMacSapNumber_Type()
)
lapbdDlSapMacSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlSapMacSapNumber.setStatus("mandatory")
_LapbdDlSapNumber_Type = Sapi
_LapbdDlSapNumber_Object = MibTableColumn
lapbdDlSapNumber = _LapbdDlSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 2),
    _LapbdDlSapNumber_Type()
)
lapbdDlSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlSapNumber.setStatus("mandatory")
_LapbdDlSapAlias_Type = Alias
_LapbdDlSapAlias_Object = MibTableColumn
lapbdDlSapAlias = _LapbdDlSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 4),
    _LapbdDlSapAlias_Type()
)
lapbdDlSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapAlias.setStatus("mandatory")


class _LapbdDlSapMaxFrameSize_Type(Integer32):
    """Custom type lapbdDlSapMaxFrameSize based on Integer32"""
    defaultValue = 1380

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_LapbdDlSapMaxFrameSize_Type.__name__ = "Integer32"
_LapbdDlSapMaxFrameSize_Object = MibTableColumn
lapbdDlSapMaxFrameSize = _LapbdDlSapMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 5),
    _LapbdDlSapMaxFrameSize_Type()
)
lapbdDlSapMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapMaxFrameSize.setStatus("mandatory")


class _LapbdDlSapWindowSize_Type(Integer32):
    """Custom type lapbdDlSapWindowSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbdDlSapWindowSize_Type.__name__ = "Integer32"
_LapbdDlSapWindowSize_Object = MibTableColumn
lapbdDlSapWindowSize = _LapbdDlSapWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 6),
    _LapbdDlSapWindowSize_Type()
)
lapbdDlSapWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapWindowSize.setStatus("mandatory")


class _LapbdDlSapMaxRetransmissions_Type(Integer32):
    """Custom type lapbdDlSapMaxRetransmissions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbdDlSapMaxRetransmissions_Type.__name__ = "Integer32"
_LapbdDlSapMaxRetransmissions_Object = MibTableColumn
lapbdDlSapMaxRetransmissions = _LapbdDlSapMaxRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 7),
    _LapbdDlSapMaxRetransmissions_Type()
)
lapbdDlSapMaxRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapMaxRetransmissions.setStatus("mandatory")


class _LapbdDlSapCongestionTimer_Type(Integer32):
    """Custom type lapbdDlSapCongestionTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_LapbdDlSapCongestionTimer_Type.__name__ = "Integer32"
_LapbdDlSapCongestionTimer_Object = MibTableColumn
lapbdDlSapCongestionTimer = _LapbdDlSapCongestionTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 8),
    _LapbdDlSapCongestionTimer_Type()
)
lapbdDlSapCongestionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapCongestionTimer.setStatus("mandatory")


class _LapbdDlSapT1T200Timer_Type(Integer32):
    """Custom type lapbdDlSapT1T200Timer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_LapbdDlSapT1T200Timer_Type.__name__ = "Integer32"
_LapbdDlSapT1T200Timer_Object = MibTableColumn
lapbdDlSapT1T200Timer = _LapbdDlSapT1T200Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 9),
    _LapbdDlSapT1T200Timer_Type()
)
lapbdDlSapT1T200Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapT1T200Timer.setStatus("mandatory")


class _LapbdDlSapT2Timer_Type(Integer32):
    """Custom type lapbdDlSapT2Timer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_LapbdDlSapT2Timer_Type.__name__ = "Integer32"
_LapbdDlSapT2Timer_Object = MibTableColumn
lapbdDlSapT2Timer = _LapbdDlSapT2Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 10),
    _LapbdDlSapT2Timer_Type()
)
lapbdDlSapT2Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapT2Timer.setStatus("mandatory")


class _LapbdDlSapT3T203Timer_Type(Integer32):
    """Custom type lapbdDlSapT3T203Timer based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_LapbdDlSapT3T203Timer_Type.__name__ = "Integer32"
_LapbdDlSapT3T203Timer_Object = MibTableColumn
lapbdDlSapT3T203Timer = _LapbdDlSapT3T203Timer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 11),
    _LapbdDlSapT3T203Timer_Type()
)
lapbdDlSapT3T203Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapT3T203Timer.setStatus("mandatory")


class _LapbdDlSapModulo_Type(Integer32):
    """Custom type lapbdDlSapModulo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_LapbdDlSapModulo_Type.__name__ = "Integer32"
_LapbdDlSapModulo_Object = MibTableColumn
lapbdDlSapModulo = _LapbdDlSapModulo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 12),
    _LapbdDlSapModulo_Type()
)
lapbdDlSapModulo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapModulo.setStatus("mandatory")


class _LapbdDlSapMaxDlcs_Type(Integer32):
    """Custom type lapbdDlSapMaxDlcs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbdDlSapMaxDlcs_Type.__name__ = "Integer32"
_LapbdDlSapMaxDlcs_Object = MibTableColumn
lapbdDlSapMaxDlcs = _LapbdDlSapMaxDlcs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 13),
    _LapbdDlSapMaxDlcs_Type()
)
lapbdDlSapMaxDlcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapMaxDlcs.setStatus("mandatory")


class _LapbdDlSapTeiAssignmentMode_Type(Integer32):
    """Custom type lapbdDlSapTeiAssignmentMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("nonAutomatic", 1))
    )


_LapbdDlSapTeiAssignmentMode_Type.__name__ = "Integer32"
_LapbdDlSapTeiAssignmentMode_Object = MibTableColumn
lapbdDlSapTeiAssignmentMode = _LapbdDlSapTeiAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 14),
    _LapbdDlSapTeiAssignmentMode_Type()
)
lapbdDlSapTeiAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdDlSapTeiAssignmentMode.setStatus("mandatory")


class _LapbdDlSapHighLevelState_Type(Integer32):
    """Custom type lapbdDlSapHighLevelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("configured", 2),
          ("unbound", 1))
    )


_LapbdDlSapHighLevelState_Type.__name__ = "Integer32"
_LapbdDlSapHighLevelState_Object = MibTableColumn
lapbdDlSapHighLevelState = _LapbdDlSapHighLevelState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 15),
    _LapbdDlSapHighLevelState_Type()
)
lapbdDlSapHighLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlSapHighLevelState.setStatus("mandatory")
_LapbdDlSapActiveDlcs_Type = Counter32
_LapbdDlSapActiveDlcs_Object = MibTableColumn
lapbdDlSapActiveDlcs = _LapbdDlSapActiveDlcs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 21, 1, 16),
    _LapbdDlSapActiveDlcs_Type()
)
lapbdDlSapActiveDlcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlSapActiveDlcs.setStatus("mandatory")
_LapbdTeiTable_Object = MibTable
lapbdTeiTable = _LapbdTeiTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22)
)
if mibBuilder.loadTexts:
    lapbdTeiTable.setStatus("mandatory")
_LapbdTeiEntry_Object = MibTableRow
lapbdTeiEntry = _LapbdTeiEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1)
)
lapbdTeiEntry.setIndexNames(
    (0, "CXLapBD-MIB", "lapbdTeiMacSapNumber"),
    (0, "CXLapBD-MIB", "lapbdTeiSapi"),
    (0, "CXLapBD-MIB", "lapbdTeiNumber"),
)
if mibBuilder.loadTexts:
    lapbdTeiEntry.setStatus("mandatory")
_LapbdTeiMacSapNumber_Type = SapIndex
_LapbdTeiMacSapNumber_Object = MibTableColumn
lapbdTeiMacSapNumber = _LapbdTeiMacSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 1),
    _LapbdTeiMacSapNumber_Type()
)
lapbdTeiMacSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdTeiMacSapNumber.setStatus("mandatory")
_LapbdTeiSapi_Type = Sapi
_LapbdTeiSapi_Object = MibTableColumn
lapbdTeiSapi = _LapbdTeiSapi_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 2),
    _LapbdTeiSapi_Type()
)
lapbdTeiSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdTeiSapi.setStatus("mandatory")
_LapbdTeiNumber_Type = Tei
_LapbdTeiNumber_Object = MibTableColumn
lapbdTeiNumber = _LapbdTeiNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 3),
    _LapbdTeiNumber_Type()
)
lapbdTeiNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdTeiNumber.setStatus("mandatory")


class _LapbdTeiRowStatus_Type(Integer32):
    """Custom type lapbdTeiRowStatus based on Integer32"""
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


_LapbdTeiRowStatus_Type.__name__ = "Integer32"
_LapbdTeiRowStatus_Object = MibTableColumn
lapbdTeiRowStatus = _LapbdTeiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 22, 1, 4),
    _LapbdTeiRowStatus_Type()
)
lapbdTeiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbdTeiRowStatus.setStatus("mandatory")
_LapbdDlcStatusTable_Object = MibTable
lapbdDlcStatusTable = _LapbdDlcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23)
)
if mibBuilder.loadTexts:
    lapbdDlcStatusTable.setStatus("mandatory")
_LapbdDlcStatusEntry_Object = MibTableRow
lapbdDlcStatusEntry = _LapbdDlcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1)
)
lapbdDlcStatusEntry.setIndexNames(
    (0, "CXLapBD-MIB", "lapbdDlcMacSapNumber"),
    (0, "CXLapBD-MIB", "lapbdDlcSapi"),
    (0, "CXLapBD-MIB", "lapbdDlcTei"),
)
if mibBuilder.loadTexts:
    lapbdDlcStatusEntry.setStatus("mandatory")
_LapbdDlcMacSapNumber_Type = SapIndex
_LapbdDlcMacSapNumber_Object = MibTableColumn
lapbdDlcMacSapNumber = _LapbdDlcMacSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 1),
    _LapbdDlcMacSapNumber_Type()
)
lapbdDlcMacSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcMacSapNumber.setStatus("mandatory")
_LapbdDlcSapi_Type = Sapi
_LapbdDlcSapi_Object = MibTableColumn
lapbdDlcSapi = _LapbdDlcSapi_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 2),
    _LapbdDlcSapi_Type()
)
lapbdDlcSapi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcSapi.setStatus("mandatory")
_LapbdDlcTei_Type = Tei
_LapbdDlcTei_Object = MibTableColumn
lapbdDlcTei = _LapbdDlcTei_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 3),
    _LapbdDlcTei_Type()
)
lapbdDlcTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcTei.setStatus("mandatory")


class _LapbdDlcLinkLevelState_Type(Integer32):
    """Custom type lapbdDlcLinkLevelState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("assignAwaitingTei", 10),
          ("connectingAwaitingTei", 5),
          ("connectingLinkLevel", 2),
          ("dataTransfer", 3),
          ("disconnectedDisabled", 1),
          ("disconnectedEnabled", 9),
          ("disconnectingLinkLevel", 4),
          ("frameRejection", 8),
          ("resettingLinkLevelDisabled", 7),
          ("resettingLinkLevelEnabled", 6))
    )


_LapbdDlcLinkLevelState_Type.__name__ = "Integer32"
_LapbdDlcLinkLevelState_Object = MibTableColumn
lapbdDlcLinkLevelState = _LapbdDlcLinkLevelState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 4),
    _LapbdDlcLinkLevelState_Type()
)
lapbdDlcLinkLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcLinkLevelState.setStatus("mandatory")
_LapbdDlcNextTxNs_Type = Integer32
_LapbdDlcNextTxNs_Object = MibTableColumn
lapbdDlcNextTxNs = _LapbdDlcNextTxNs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 5),
    _LapbdDlcNextTxNs_Type()
)
lapbdDlcNextTxNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcNextTxNs.setStatus("mandatory")
_LapbdDlcNextRxNs_Type = Integer32
_LapbdDlcNextRxNs_Object = MibTableColumn
lapbdDlcNextRxNs = _LapbdDlcNextRxNs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 6),
    _LapbdDlcNextRxNs_Type()
)
lapbdDlcNextRxNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcNextRxNs.setStatus("mandatory")
_LapbdDlcRetransmissionCount_Type = Integer32
_LapbdDlcRetransmissionCount_Object = MibTableColumn
lapbdDlcRetransmissionCount = _LapbdDlcRetransmissionCount_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 7),
    _LapbdDlcRetransmissionCount_Type()
)
lapbdDlcRetransmissionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcRetransmissionCount.setStatus("mandatory")


class _LapbdDlcLocalFlowControlState_Type(Integer32):
    """Custom type lapbdDlcLocalFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localFlowNormal", 1),
          ("localFlowStopped", 2))
    )


_LapbdDlcLocalFlowControlState_Type.__name__ = "Integer32"
_LapbdDlcLocalFlowControlState_Object = MibTableColumn
lapbdDlcLocalFlowControlState = _LapbdDlcLocalFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 8),
    _LapbdDlcLocalFlowControlState_Type()
)
lapbdDlcLocalFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcLocalFlowControlState.setStatus("mandatory")


class _LapbdDlcRemoteFlowControlState_Type(Integer32):
    """Custom type lapbdDlcRemoteFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteFlowNormal", 1),
          ("remoteFlowStopped", 2))
    )


_LapbdDlcRemoteFlowControlState_Type.__name__ = "Integer32"
_LapbdDlcRemoteFlowControlState_Object = MibTableColumn
lapbdDlcRemoteFlowControlState = _LapbdDlcRemoteFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 9),
    _LapbdDlcRemoteFlowControlState_Type()
)
lapbdDlcRemoteFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcRemoteFlowControlState.setStatus("mandatory")


class _LapbdDlcMacTxFlowControlState_Type(Integer32):
    """Custom type lapbdDlcMacTxFlowControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowNormal", 1),
          ("flowStopped", 2))
    )


_LapbdDlcMacTxFlowControlState_Type.__name__ = "Integer32"
_LapbdDlcMacTxFlowControlState_Object = MibTableColumn
lapbdDlcMacTxFlowControlState = _LapbdDlcMacTxFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 10),
    _LapbdDlcMacTxFlowControlState_Type()
)
lapbdDlcMacTxFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcMacTxFlowControlState.setStatus("mandatory")
_LapbdDlcTxQSize_Type = Integer32
_LapbdDlcTxQSize_Object = MibTableColumn
lapbdDlcTxQSize = _LapbdDlcTxQSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 23, 1, 11),
    _LapbdDlcTxQSize_Type()
)
lapbdDlcTxQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbdDlcTxQSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lapbdStatusIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 27, 0, 1)
)
lapbdStatusIndication.setObjects(
      *(("CXLapBD-MIB", "lapbdTeiMacSapNumber"),
        ("CXLapBD-MIB", "lapbdTeiSapi"),
        ("CXLapBD-MIB", "lapbdTeiNumber"),
        ("CXLapBD-MIB", "lapbdStatusEvent"))
)
if mibBuilder.loadTexts:
    lapbdStatusIndication.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXLapBD-MIB",
    **{"Sapi": Sapi,
       "Tei": Tei,
       "lapbdStatusIndication": lapbdStatusIndication,
       "lapbdLowerPoolThreshold": lapbdLowerPoolThreshold,
       "lapbdUpperPoolThreshold": lapbdUpperPoolThreshold,
       "lapbdTraceSize": lapbdTraceSize,
       "lapbdTraceFlags": lapbdTraceFlags,
       "lapbdTraps": lapbdTraps,
       "lapbdStatusEvent": lapbdStatusEvent,
       "lapbdSoftwareVersions": lapbdSoftwareVersions,
       "lapbdMacSapTable": lapbdMacSapTable,
       "lapbdMacSapEntry": lapbdMacSapEntry,
       "lapbdMacSapNumber": lapbdMacSapNumber,
       "lapbdMacSapRowStatus": lapbdMacSapRowStatus,
       "lapbdMacSapAlias": lapbdMacSapAlias,
       "lapbdMacSapCompanionAlias": lapbdMacSapCompanionAlias,
       "lapbdMacSapLapType": lapbdMacSapLapType,
       "lapbdMacSapLogicalInterfaceType": lapbdMacSapLogicalInterfaceType,
       "lapbdMacSapArbitrationLogic": lapbdMacSapArbitrationLogic,
       "lapbdMacSapLapDProtocolFlavor": lapbdMacSapLapDProtocolFlavor,
       "lapbdMacSapLapBProtocolFlavor": lapbdMacSapLapBProtocolFlavor,
       "lapbdMacSapWindow": lapbdMacSapWindow,
       "lapbdMacSapTxQUpperThreshold": lapbdMacSapTxQUpperThreshold,
       "lapbdMacSapTxQLowerThreshold": lapbdMacSapTxQLowerThreshold,
       "lapbdMacSapConnectionTimer": lapbdMacSapConnectionTimer,
       "lapbdMacSapT202Timer": lapbdMacSapT202Timer,
       "lapbdMacSapN202Counter": lapbdMacSapN202Counter,
       "lapbdMacSapTeiCheckTimer": lapbdMacSapTeiCheckTimer,
       "lapbdMacSapT201Timer": lapbdMacSapT201Timer,
       "lapbdMacSapLowTei": lapbdMacSapLowTei,
       "lapbdMacSapKeepL1Up": lapbdMacSapKeepL1Up,
       "lapbdMacSapControl": lapbdMacSapControl,
       "lapbdMacSapHighLevelState": lapbdMacSapHighLevelState,
       "lapbdMacSapFlowControlState": lapbdMacSapFlowControlState,
       "lapbdMacSapOutstandingFrames": lapbdMacSapOutstandingFrames,
       "lapbdMacSapTotalFramesDropped": lapbdMacSapTotalFramesDropped,
       "lapbdMacSapActiveSaps": lapbdMacSapActiveSaps,
       "lapbdMacSapTxIFrames": lapbdMacSapTxIFrames,
       "lapbdMacSapRxIFrames": lapbdMacSapRxIFrames,
       "lapbdMacSapTxRrFrames": lapbdMacSapTxRrFrames,
       "lapbdMacSapRxRrFrames": lapbdMacSapRxRrFrames,
       "lapbdMacSapTxRnrFrames": lapbdMacSapTxRnrFrames,
       "lapbdMacSapRxRnrFrames": lapbdMacSapRxRnrFrames,
       "lapbdMacSapTxRejFrames": lapbdMacSapTxRejFrames,
       "lapbdMacSapRxRejFrames": lapbdMacSapRxRejFrames,
       "lapbdMacSapTxSabmFrames": lapbdMacSapTxSabmFrames,
       "lapbdMacSapRxSabmFrames": lapbdMacSapRxSabmFrames,
       "lapbdMacSapTxDiscFrames": lapbdMacSapTxDiscFrames,
       "lapbdMacSapRxDiscFrames": lapbdMacSapRxDiscFrames,
       "lapbdMacSapTxUaFrames": lapbdMacSapTxUaFrames,
       "lapbdMacSapRxUaFrames": lapbdMacSapRxUaFrames,
       "lapbdMacSapTxDmFrames": lapbdMacSapTxDmFrames,
       "lapbdMacSapRxDmFrames": lapbdMacSapRxDmFrames,
       "lapbdMacSapTxFrmrFrames": lapbdMacSapTxFrmrFrames,
       "lapbdMacSapRxFrmrFrames": lapbdMacSapRxFrmrFrames,
       "lapbdMacSapTxUiFrames": lapbdMacSapTxUiFrames,
       "lapbdMacSapRxUiFrames": lapbdMacSapRxUiFrames,
       "lapbdMacSapTxXidFrames": lapbdMacSapTxXidFrames,
       "lapbdMacSapRxXidFrames": lapbdMacSapRxXidFrames,
       "lapbdMacSapRxInvalidFrames": lapbdMacSapRxInvalidFrames,
       "lapbdMacSapRxInvalidDiscards": lapbdMacSapRxInvalidDiscards,
       "lapbdMacSapSabmErrors": lapbdMacSapSabmErrors,
       "lapbdMacSapFrmrErrors": lapbdMacSapFrmrErrors,
       "lapbdDlSapTable": lapbdDlSapTable,
       "lapbdDlSapEntry": lapbdDlSapEntry,
       "lapbdDlSapMacSapNumber": lapbdDlSapMacSapNumber,
       "lapbdDlSapNumber": lapbdDlSapNumber,
       "lapbdDlSapAlias": lapbdDlSapAlias,
       "lapbdDlSapMaxFrameSize": lapbdDlSapMaxFrameSize,
       "lapbdDlSapWindowSize": lapbdDlSapWindowSize,
       "lapbdDlSapMaxRetransmissions": lapbdDlSapMaxRetransmissions,
       "lapbdDlSapCongestionTimer": lapbdDlSapCongestionTimer,
       "lapbdDlSapT1T200Timer": lapbdDlSapT1T200Timer,
       "lapbdDlSapT2Timer": lapbdDlSapT2Timer,
       "lapbdDlSapT3T203Timer": lapbdDlSapT3T203Timer,
       "lapbdDlSapModulo": lapbdDlSapModulo,
       "lapbdDlSapMaxDlcs": lapbdDlSapMaxDlcs,
       "lapbdDlSapTeiAssignmentMode": lapbdDlSapTeiAssignmentMode,
       "lapbdDlSapHighLevelState": lapbdDlSapHighLevelState,
       "lapbdDlSapActiveDlcs": lapbdDlSapActiveDlcs,
       "lapbdTeiTable": lapbdTeiTable,
       "lapbdTeiEntry": lapbdTeiEntry,
       "lapbdTeiMacSapNumber": lapbdTeiMacSapNumber,
       "lapbdTeiSapi": lapbdTeiSapi,
       "lapbdTeiNumber": lapbdTeiNumber,
       "lapbdTeiRowStatus": lapbdTeiRowStatus,
       "lapbdDlcStatusTable": lapbdDlcStatusTable,
       "lapbdDlcStatusEntry": lapbdDlcStatusEntry,
       "lapbdDlcMacSapNumber": lapbdDlcMacSapNumber,
       "lapbdDlcSapi": lapbdDlcSapi,
       "lapbdDlcTei": lapbdDlcTei,
       "lapbdDlcLinkLevelState": lapbdDlcLinkLevelState,
       "lapbdDlcNextTxNs": lapbdDlcNextTxNs,
       "lapbdDlcNextRxNs": lapbdDlcNextRxNs,
       "lapbdDlcRetransmissionCount": lapbdDlcRetransmissionCount,
       "lapbdDlcLocalFlowControlState": lapbdDlcLocalFlowControlState,
       "lapbdDlcRemoteFlowControlState": lapbdDlcRemoteFlowControlState,
       "lapbdDlcMacTxFlowControlState": lapbdDlcMacTxFlowControlState,
       "lapbdDlcTxQSize": lapbdDlcTxQSize}
)
