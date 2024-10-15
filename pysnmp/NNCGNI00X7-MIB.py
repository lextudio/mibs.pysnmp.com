# SNMP MIB module (NNCGNI00X7-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X7-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:27 2024
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

(nncExtDevice,) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtDevice")

(PositionIndex,) = mibBuilder.importSymbols(
    "NNCGNI00X4-MIB",
    "PositionIndex")

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


# MODULE-IDENTITY


# Types definitions



class PortIndex(Integer32):
    """Custom type PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )





class CircuitIndex(Integer32):
    """Custom type CircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )





class LoopbackType(Integer32):
    """Custom type LoopbackType based on Integer32"""
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("devChannelLoopback", 5),
          ("devDD-BlkLoopback", 13),
          ("devDDSDSULoopback", 7),
          ("devDDSLatchCSULoopback", 9),
          ("devDDSLatchDSOLoopback", 10),
          ("devDDSLatchHL96Loopback", 11),
          ("devDDSLatchOCULoopback", 8),
          ("devDDSMJULoopback", 12),
          ("devDDSOCULoopback", 6),
          ("devLoopBackC", 4),
          ("devLoopbackA", 2),
          ("devLoopbackB", 3),
          ("devNoLoopback", 1))
    )





class SignallingBits(Integer32):
    """Custom type SignallingBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtDeviceTable_Object = MibTable
nncExtDeviceTable = _NncExtDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1)
)
if mibBuilder.loadTexts:
    nncExtDeviceTable.setStatus("mandatory")
_NncExtDeviceEntry_Object = MibTableRow
nncExtDeviceEntry = _NncExtDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1)
)
nncExtDeviceEntry.setIndexNames(
    (0, "NNCGNI00X7-MIB", "nncExtDevPosnIdx"),
    (0, "NNCGNI00X7-MIB", "nncExtDevPortIdx"),
    (0, "NNCGNI00X7-MIB", "nncExtDevCctIdx"),
)
if mibBuilder.loadTexts:
    nncExtDeviceEntry.setStatus("mandatory")
_NncExtDevPosnIdx_Type = PositionIndex
_NncExtDevPosnIdx_Object = MibTableColumn
nncExtDevPosnIdx = _NncExtDevPosnIdx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 1),
    _NncExtDevPosnIdx_Type()
)
nncExtDevPosnIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevPosnIdx.setStatus("mandatory")
_NncExtDevPortIdx_Type = PortIndex
_NncExtDevPortIdx_Object = MibTableColumn
nncExtDevPortIdx = _NncExtDevPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 2),
    _NncExtDevPortIdx_Type()
)
nncExtDevPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevPortIdx.setStatus("mandatory")
_NncExtDevCctIdx_Type = CircuitIndex
_NncExtDevCctIdx_Object = MibTableColumn
nncExtDevCctIdx = _NncExtDevCctIdx_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 3),
    _NncExtDevCctIdx_Type()
)
nncExtDevCctIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevCctIdx.setStatus("mandatory")


class _NncExtDevName_Type(DisplayString):
    """Custom type nncExtDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NncExtDevName_Type.__name__ = "DisplayString"
_NncExtDevName_Object = MibTableColumn
nncExtDevName = _NncExtDevName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 4),
    _NncExtDevName_Type()
)
nncExtDevName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDevName.setStatus("mandatory")


class _NncExtDevLoopback_Type(Integer32):
    """Custom type nncExtDevLoopback based on Integer32"""
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("devChannelLoopback", 5),
          ("devDD-BlkLoopback", 13),
          ("devDDSDSULoopback", 7),
          ("devDDSLatchCSULoopback", 9),
          ("devDDSLatchDSOLoopback", 10),
          ("devDDSLatchHL96Loopback", 11),
          ("devDDSLatchOCULoopback", 8),
          ("devDDSMJULoopback", 12),
          ("devDDSOCULoopback", 6),
          ("devLoopBackC", 4),
          ("devLoopbackA", 2),
          ("devLoopbackB", 3),
          ("devNoLoopback", 1))
    )


_NncExtDevLoopback_Type.__name__ = "Integer32"
_NncExtDevLoopback_Object = MibTableColumn
nncExtDevLoopback = _NncExtDevLoopback_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 5),
    _NncExtDevLoopback_Type()
)
nncExtDevLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDevLoopback.setStatus("mandatory")


class _NncExtDevCallStatus_Type(Integer32):
    """Custom type nncExtDevCallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NncExtDevCallStatus_Type.__name__ = "Integer32"
_NncExtDevCallStatus_Object = MibTableColumn
nncExtDevCallStatus = _NncExtDevCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 6),
    _NncExtDevCallStatus_Type()
)
nncExtDevCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevCallStatus.setStatus("mandatory")


class _NncExtDevBusyOut_Type(Integer32):
    """Custom type nncExtDevBusyOut based on Integer32"""
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


_NncExtDevBusyOut_Type.__name__ = "Integer32"
_NncExtDevBusyOut_Object = MibTableColumn
nncExtDevBusyOut = _NncExtDevBusyOut_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 7),
    _NncExtDevBusyOut_Type()
)
nncExtDevBusyOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDevBusyOut.setStatus("mandatory")
_NncExtDevOutputSignalling_Type = SignallingBits
_NncExtDevOutputSignalling_Object = MibTableColumn
nncExtDevOutputSignalling = _NncExtDevOutputSignalling_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 8),
    _NncExtDevOutputSignalling_Type()
)
nncExtDevOutputSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDevOutputSignalling.setStatus("mandatory")
_NncExtDevInputSignalling_Type = SignallingBits
_NncExtDevInputSignalling_Object = MibTableColumn
nncExtDevInputSignalling = _NncExtDevInputSignalling_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 9),
    _NncExtDevInputSignalling_Type()
)
nncExtDevInputSignalling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevInputSignalling.setStatus("mandatory")


class _NncExtDevConnectedTo_Type(OctetString):
    """Custom type nncExtDevConnectedTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_NncExtDevConnectedTo_Type.__name__ = "OctetString"
_NncExtDevConnectedTo_Object = MibTableColumn
nncExtDevConnectedTo = _NncExtDevConnectedTo_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 10),
    _NncExtDevConnectedTo_Type()
)
nncExtDevConnectedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDevConnectedTo.setStatus("mandatory")


class _NncExtDevUIName_Type(DisplayString):
    """Custom type nncExtDevUIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_NncExtDevUIName_Type.__name__ = "DisplayString"
_NncExtDevUIName_Object = MibTableColumn
nncExtDevUIName = _NncExtDevUIName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 11),
    _NncExtDevUIName_Type()
)
nncExtDevUIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevUIName.setStatus("mandatory")


class _NncExtDevUIType_Type(DisplayString):
    """Custom type nncExtDevUIType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 12),
    )


_NncExtDevUIType_Type.__name__ = "DisplayString"
_NncExtDevUIType_Object = MibTableColumn
nncExtDevUIType = _NncExtDevUIType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 12),
    _NncExtDevUIType_Type()
)
nncExtDevUIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevUIType.setStatus("mandatory")


class _NncExtDevConnectedToUIName_Type(DisplayString):
    """Custom type nncExtDevConnectedToUIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_NncExtDevConnectedToUIName_Type.__name__ = "DisplayString"
_NncExtDevConnectedToUIName_Object = MibTableColumn
nncExtDevConnectedToUIName = _NncExtDevConnectedToUIName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 9, 1, 1, 13),
    _NncExtDevConnectedToUIName_Type()
)
nncExtDevConnectedToUIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDevConnectedToUIName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X7-MIB",
    **{"PortIndex": PortIndex,
       "CircuitIndex": CircuitIndex,
       "LoopbackType": LoopbackType,
       "SignallingBits": SignallingBits,
       "nncExtDeviceTable": nncExtDeviceTable,
       "nncExtDeviceEntry": nncExtDeviceEntry,
       "nncExtDevPosnIdx": nncExtDevPosnIdx,
       "nncExtDevPortIdx": nncExtDevPortIdx,
       "nncExtDevCctIdx": nncExtDevCctIdx,
       "nncExtDevName": nncExtDevName,
       "nncExtDevLoopback": nncExtDevLoopback,
       "nncExtDevCallStatus": nncExtDevCallStatus,
       "nncExtDevBusyOut": nncExtDevBusyOut,
       "nncExtDevOutputSignalling": nncExtDevOutputSignalling,
       "nncExtDevInputSignalling": nncExtDevInputSignalling,
       "nncExtDevConnectedTo": nncExtDevConnectedTo,
       "nncExtDevUIName": nncExtDevUIName,
       "nncExtDevUIType": nncExtDevUIType,
       "nncExtDevConnectedToUIName": nncExtDevConnectedToUIName}
)
