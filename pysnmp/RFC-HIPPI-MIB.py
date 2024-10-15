# SNMP MIB module (RFC-HIPPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC-HIPPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:03 2024
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

(nscTransmission,) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nscTransmission")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NscHippi_ObjectIdentity = ObjectIdentity
nscHippi = _NscHippi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1)
)
_HippiNumber_Type = Integer32
_HippiNumber_Object = MibScalar
hippiNumber = _HippiNumber_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 1),
    _HippiNumber_Type()
)
hippiNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiNumber.setStatus("mandatory")
_HippiTable_Object = MibTable
hippiTable = _HippiTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hippiTable.setStatus("mandatory")
_HippiEntry_Object = MibTableRow
hippiEntry = _HippiEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1)
)
hippiEntry.setIndexNames(
    (0, "RFC-HIPPI-MIB", "hippiPortNumber"),
)
if mibBuilder.loadTexts:
    hippiEntry.setStatus("mandatory")
_HippiPortNumber_Type = Integer32
_HippiPortNumber_Object = MibTableColumn
hippiPortNumber = _HippiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 1),
    _HippiPortNumber_Type()
)
hippiPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiPortNumber.setStatus("mandatory")


class _HippiWordSize_Type(Integer32):
    """Custom type hippiWordSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hippi32bitDataBus", 1),
          ("hippi64bitDataBus", 2))
    )


_HippiWordSize_Type.__name__ = "Integer32"
_HippiWordSize_Object = MibTableColumn
hippiWordSize = _HippiWordSize_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 2),
    _HippiWordSize_Type()
)
hippiWordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiWordSize.setStatus("mandatory")


class _HippiEndPointType_Type(Integer32):
    """Custom type hippiEndPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hippiDestinationEndPoint", 2),
          ("hippiSourceEndPoint", 1))
    )


_HippiEndPointType_Type.__name__ = "Integer32"
_HippiEndPointType_Object = MibTableColumn
hippiEndPointType = _HippiEndPointType_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 3),
    _HippiEndPointType_Type()
)
hippiEndPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiEndPointType.setStatus("mandatory")


class _HippiWordCountHigh_Type(Integer32):
    """Custom type hippiWordCountHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HippiWordCountHigh_Type.__name__ = "Integer32"
_HippiWordCountHigh_Object = MibTableColumn
hippiWordCountHigh = _HippiWordCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 4),
    _HippiWordCountHigh_Type()
)
hippiWordCountHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiWordCountHigh.setStatus("mandatory")


class _HippiWordCountLow_Type(Integer32):
    """Custom type hippiWordCountLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_HippiWordCountLow_Type.__name__ = "Integer32"
_HippiWordCountLow_Object = MibTableColumn
hippiWordCountLow = _HippiWordCountLow_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 5),
    _HippiWordCountLow_Type()
)
hippiWordCountLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiWordCountLow.setStatus("mandatory")


class _HippiBurstCountHigh_Type(Integer32):
    """Custom type hippiBurstCountHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HippiBurstCountHigh_Type.__name__ = "Integer32"
_HippiBurstCountHigh_Object = MibTableColumn
hippiBurstCountHigh = _HippiBurstCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 6),
    _HippiBurstCountHigh_Type()
)
hippiBurstCountHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiBurstCountHigh.setStatus("mandatory")


class _HippiBurstCountLow_Type(Integer32):
    """Custom type hippiBurstCountLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_HippiBurstCountLow_Type.__name__ = "Integer32"
_HippiBurstCountLow_Object = MibTableColumn
hippiBurstCountLow = _HippiBurstCountLow_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 7),
    _HippiBurstCountLow_Type()
)
hippiBurstCountLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiBurstCountLow.setStatus("mandatory")


class _HippiPacketCountHigh_Type(Integer32):
    """Custom type hippiPacketCountHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HippiPacketCountHigh_Type.__name__ = "Integer32"
_HippiPacketCountHigh_Object = MibTableColumn
hippiPacketCountHigh = _HippiPacketCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 8),
    _HippiPacketCountHigh_Type()
)
hippiPacketCountHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiPacketCountHigh.setStatus("mandatory")


class _HippiPacketCountLow_Type(Integer32):
    """Custom type hippiPacketCountLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_HippiPacketCountLow_Type.__name__ = "Integer32"
_HippiPacketCountLow_Object = MibTableColumn
hippiPacketCountLow = _HippiPacketCountLow_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 9),
    _HippiPacketCountLow_Type()
)
hippiPacketCountLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiPacketCountLow.setStatus("mandatory")
_HippiParityErrors_Type = Counter32
_HippiParityErrors_Object = MibTableColumn
hippiParityErrors = _HippiParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 10),
    _HippiParityErrors_Type()
)
hippiParityErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiParityErrors.setStatus("mandatory")
_HippiInputPortRejectCount_Type = Counter32
_HippiInputPortRejectCount_Object = MibTableColumn
hippiInputPortRejectCount = _HippiInputPortRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 11),
    _HippiInputPortRejectCount_Type()
)
hippiInputPortRejectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiInputPortRejectCount.setStatus("mandatory")
_HippiDestRejectCount_Type = Counter32
_HippiDestRejectCount_Object = MibTableColumn
hippiDestRejectCount = _HippiDestRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 12),
    _HippiDestRejectCount_Type()
)
hippiDestRejectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiDestRejectCount.setStatus("mandatory")
_HippiSourceRejectCount_Type = Counter32
_HippiSourceRejectCount_Object = MibTableColumn
hippiSourceRejectCount = _HippiSourceRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 13),
    _HippiSourceRejectCount_Type()
)
hippiSourceRejectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiSourceRejectCount.setStatus("mandatory")
_HippiDestDisconnectCount_Type = Counter32
_HippiDestDisconnectCount_Object = MibTableColumn
hippiDestDisconnectCount = _HippiDestDisconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 14),
    _HippiDestDisconnectCount_Type()
)
hippiDestDisconnectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiDestDisconnectCount.setStatus("mandatory")
_HippiSourceDisconnectCount_Type = Counter32
_HippiSourceDisconnectCount_Object = MibTableColumn
hippiSourceDisconnectCount = _HippiSourceDisconnectCount_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 15),
    _HippiSourceDisconnectCount_Type()
)
hippiSourceDisconnectCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hippiSourceDisconnectCount.setStatus("mandatory")


class _HippiLastIField_Type(OctetString):
    """Custom type hippiLastIField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HippiLastIField_Type.__name__ = "OctetString"
_HippiLastIField_Object = MibTableColumn
hippiLastIField = _HippiLastIField_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 16),
    _HippiLastIField_Type()
)
hippiLastIField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiLastIField.setStatus("mandatory")


class _HippiConnectState_Type(Integer32):
    """Custom type hippiConnectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hippiConnectRequest", 2),
          ("hippiConnected", 3),
          ("hippiDisconnect", 1))
    )


_HippiConnectState_Type.__name__ = "Integer32"
_HippiConnectState_Object = MibTableColumn
hippiConnectState = _HippiConnectState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 17),
    _HippiConnectState_Type()
)
hippiConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiConnectState.setStatus("mandatory")


class _HippiLastErrorType_Type(Integer32):
    """Custom type hippiLastErrorType based on Integer32"""
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
        *(("hippiErrorTypeBusy", 2),
          ("hippiErrorTypeInvalidAddress", 5),
          ("hippiErrorTypeParityError", 4),
          ("hippiErrorTypeReject", 1),
          ("hippiErrorTypeTimeout", 3))
    )


_HippiLastErrorType_Type.__name__ = "Integer32"
_HippiLastErrorType_Object = MibTableColumn
hippiLastErrorType = _HippiLastErrorType_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 18),
    _HippiLastErrorType_Type()
)
hippiLastErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiLastErrorType.setStatus("mandatory")


class _HippiLastErrorIField_Type(OctetString):
    """Custom type hippiLastErrorIField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HippiLastErrorIField_Type.__name__ = "OctetString"
_HippiLastErrorIField_Object = MibTableColumn
hippiLastErrorIField = _HippiLastErrorIField_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 19),
    _HippiLastErrorIField_Type()
)
hippiLastErrorIField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiLastErrorIField.setStatus("mandatory")


class _HippiInterconnectStatus_Type(Integer32):
    """Custom type hippiInterconnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HippiInterconnectStatus_Type.__name__ = "Integer32"
_HippiInterconnectStatus_Object = MibTableColumn
hippiInterconnectStatus = _HippiInterconnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1, 2, 1, 20),
    _HippiInterconnectStatus_Type()
)
hippiInterconnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hippiInterconnectStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC-HIPPI-MIB",
    **{"nscHippi": nscHippi,
       "hippiNumber": hippiNumber,
       "hippiTable": hippiTable,
       "hippiEntry": hippiEntry,
       "hippiPortNumber": hippiPortNumber,
       "hippiWordSize": hippiWordSize,
       "hippiEndPointType": hippiEndPointType,
       "hippiWordCountHigh": hippiWordCountHigh,
       "hippiWordCountLow": hippiWordCountLow,
       "hippiBurstCountHigh": hippiBurstCountHigh,
       "hippiBurstCountLow": hippiBurstCountLow,
       "hippiPacketCountHigh": hippiPacketCountHigh,
       "hippiPacketCountLow": hippiPacketCountLow,
       "hippiParityErrors": hippiParityErrors,
       "hippiInputPortRejectCount": hippiInputPortRejectCount,
       "hippiDestRejectCount": hippiDestRejectCount,
       "hippiSourceRejectCount": hippiSourceRejectCount,
       "hippiDestDisconnectCount": hippiDestDisconnectCount,
       "hippiSourceDisconnectCount": hippiSourceDisconnectCount,
       "hippiLastIField": hippiLastIField,
       "hippiConnectState": hippiConnectState,
       "hippiLastErrorType": hippiLastErrorType,
       "hippiLastErrorIField": hippiLastErrorIField,
       "hippiInterconnectStatus": hippiInterconnectStatus}
)
