# SNMP MIB module (NMS-EPON-ONU-SERIAL-PORT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-ONU-SERIAL-PORT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:51 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOnuSerialPort_ObjectIdentity = ObjectIdentity
nmsEponOnuSerialPort = _NmsEponOnuSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27)
)
_NmsEponOnuSerialPortTable_Object = MibTable
nmsEponOnuSerialPortTable = _NmsEponOnuSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1)
)
if mibBuilder.loadTexts:
    nmsEponOnuSerialPortTable.setStatus("mandatory")
_NmsEponOnuSerialPortEntry_Object = MibTableRow
nmsEponOnuSerialPortEntry = _NmsEponOnuSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1)
)
nmsEponOnuSerialPortEntry.setIndexNames(
    (0, "NMS-EPON-ONU-SERIAL-PORT", "llidIfIndex"),
    (0, "NMS-EPON-ONU-SERIAL-PORT", "onuSerialPortSeqNo"),
)
if mibBuilder.loadTexts:
    nmsEponOnuSerialPortEntry.setStatus("mandatory")
_LlidIfIndex_Type = Integer32
_LlidIfIndex_Object = MibTableColumn
llidIfIndex = _LlidIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 1),
    _LlidIfIndex_Type()
)
llidIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidIfIndex.setStatus("mandatory")


class _OnuSerialPortSeqNo_Type(Integer32):
    """Custom type onuSerialPortSeqNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(224, 239),
    )


_OnuSerialPortSeqNo_Type.__name__ = "Integer32"
_OnuSerialPortSeqNo_Object = MibTableColumn
onuSerialPortSeqNo = _OnuSerialPortSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 2),
    _OnuSerialPortSeqNo_Type()
)
onuSerialPortSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSerialPortSeqNo.setStatus("mandatory")


class _OnuSerialPortSpeed_Type(Integer32):
    """Custom type onuSerialPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 115200),
    )


_OnuSerialPortSpeed_Type.__name__ = "Integer32"
_OnuSerialPortSpeed_Object = MibTableColumn
onuSerialPortSpeed = _OnuSerialPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 3),
    _OnuSerialPortSpeed_Type()
)
onuSerialPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortSpeed.setStatus("mandatory")


class _OnuSerialPortDataBits_Type(Integer32):
    """Custom type onuSerialPortDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_OnuSerialPortDataBits_Type.__name__ = "Integer32"
_OnuSerialPortDataBits_Object = MibTableColumn
onuSerialPortDataBits = _OnuSerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 4),
    _OnuSerialPortDataBits_Type()
)
onuSerialPortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortDataBits.setStatus("mandatory")


class _OnuSerialPortHaltBits_Type(Integer32):
    """Custom type onuSerialPortHaltBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OnuSerialPortHaltBits_Type.__name__ = "Integer32"
_OnuSerialPortHaltBits_Object = MibTableColumn
onuSerialPortHaltBits = _OnuSerialPortHaltBits_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 5),
    _OnuSerialPortHaltBits_Type()
)
onuSerialPortHaltBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortHaltBits.setStatus("mandatory")


class _OnuSerialPortParity_Type(Integer32):
    """Custom type onuSerialPortParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 0),
          ("odd", 1))
    )


_OnuSerialPortParity_Type.__name__ = "Integer32"
_OnuSerialPortParity_Object = MibTableColumn
onuSerialPortParity = _OnuSerialPortParity_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 6),
    _OnuSerialPortParity_Type()
)
onuSerialPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortParity.setStatus("mandatory")


class _OnuSerialPortFlowControl_Type(Integer32):
    """Custom type onuSerialPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("none", 0),
          ("software", 1))
    )


_OnuSerialPortFlowControl_Type.__name__ = "Integer32"
_OnuSerialPortFlowControl_Object = MibTableColumn
onuSerialPortFlowControl = _OnuSerialPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 7),
    _OnuSerialPortFlowControl_Type()
)
onuSerialPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortFlowControl.setStatus("mandatory")
_OnuSerialPortPropRowStatus_Type = RowStatus
_OnuSerialPortPropRowStatus_Object = MibTableColumn
onuSerialPortPropRowStatus = _OnuSerialPortPropRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 8),
    _OnuSerialPortPropRowStatus_Type()
)
onuSerialPortPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuSerialPortPropRowStatus.setStatus("mandatory")


class _OnuSerialPortDataReadInterval_Type(Integer32):
    """Custom type onuSerialPortDataReadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_OnuSerialPortDataReadInterval_Type.__name__ = "Integer32"
_OnuSerialPortDataReadInterval_Object = MibTableColumn
onuSerialPortDataReadInterval = _OnuSerialPortDataReadInterval_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 9),
    _OnuSerialPortDataReadInterval_Type()
)
onuSerialPortDataReadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortDataReadInterval.setStatus("mandatory")


class _OnuSerialPortDataReadBytes_Type(Integer32):
    """Custom type onuSerialPortDataReadBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_OnuSerialPortDataReadBytes_Type.__name__ = "Integer32"
_OnuSerialPortDataReadBytes_Object = MibTableColumn
onuSerialPortDataReadBytes = _OnuSerialPortDataReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 10),
    _OnuSerialPortDataReadBytes_Type()
)
onuSerialPortDataReadBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortDataReadBytes.setStatus("mandatory")
_OnuSerialPortBufferRowStatus_Type = RowStatus
_OnuSerialPortBufferRowStatus_Object = MibTableColumn
onuSerialPortBufferRowStatus = _OnuSerialPortBufferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 11),
    _OnuSerialPortBufferRowStatus_Type()
)
onuSerialPortBufferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuSerialPortBufferRowStatus.setStatus("mandatory")


class _OnuSerialPortKeepaliveMode_Type(Integer32):
    """Custom type onuSerialPortKeepaliveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuSerialPortKeepaliveMode_Type.__name__ = "Integer32"
_OnuSerialPortKeepaliveMode_Object = MibTableColumn
onuSerialPortKeepaliveMode = _OnuSerialPortKeepaliveMode_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 12),
    _OnuSerialPortKeepaliveMode_Type()
)
onuSerialPortKeepaliveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortKeepaliveMode.setStatus("mandatory")


class _OnuSerialPortKeepaliveIdle_Type(Integer32):
    """Custom type onuSerialPortKeepaliveIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_OnuSerialPortKeepaliveIdle_Type.__name__ = "Integer32"
_OnuSerialPortKeepaliveIdle_Object = MibTableColumn
onuSerialPortKeepaliveIdle = _OnuSerialPortKeepaliveIdle_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 13),
    _OnuSerialPortKeepaliveIdle_Type()
)
onuSerialPortKeepaliveIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortKeepaliveIdle.setStatus("mandatory")


class _OnuSerialPortKeepaliveTimeout_Type(Integer32):
    """Custom type onuSerialPortKeepaliveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_OnuSerialPortKeepaliveTimeout_Type.__name__ = "Integer32"
_OnuSerialPortKeepaliveTimeout_Object = MibTableColumn
onuSerialPortKeepaliveTimeout = _OnuSerialPortKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 14),
    _OnuSerialPortKeepaliveTimeout_Type()
)
onuSerialPortKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortKeepaliveTimeout.setStatus("mandatory")


class _OnuSerialPortKeepaliveProbeCount_Type(Integer32):
    """Custom type onuSerialPortKeepaliveProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_OnuSerialPortKeepaliveProbeCount_Type.__name__ = "Integer32"
_OnuSerialPortKeepaliveProbeCount_Object = MibTableColumn
onuSerialPortKeepaliveProbeCount = _OnuSerialPortKeepaliveProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 15),
    _OnuSerialPortKeepaliveProbeCount_Type()
)
onuSerialPortKeepaliveProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortKeepaliveProbeCount.setStatus("mandatory")
_OnuSerialPortKeepaliveRowStatus_Type = RowStatus
_OnuSerialPortKeepaliveRowStatus_Object = MibTableColumn
onuSerialPortKeepaliveRowStatus = _OnuSerialPortKeepaliveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 16),
    _OnuSerialPortKeepaliveRowStatus_Type()
)
onuSerialPortKeepaliveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuSerialPortKeepaliveRowStatus.setStatus("mandatory")
_OnuSerialPortLoopback_Type = TruthValue
_OnuSerialPortLoopback_Object = MibTableColumn
onuSerialPortLoopback = _OnuSerialPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 27, 1, 1, 17),
    _OnuSerialPortLoopback_Type()
)
onuSerialPortLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuSerialPortLoopback.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-ONU-SERIAL-PORT",
    **{"nmsEponOnuSerialPort": nmsEponOnuSerialPort,
       "nmsEponOnuSerialPortTable": nmsEponOnuSerialPortTable,
       "nmsEponOnuSerialPortEntry": nmsEponOnuSerialPortEntry,
       "llidIfIndex": llidIfIndex,
       "onuSerialPortSeqNo": onuSerialPortSeqNo,
       "onuSerialPortSpeed": onuSerialPortSpeed,
       "onuSerialPortDataBits": onuSerialPortDataBits,
       "onuSerialPortHaltBits": onuSerialPortHaltBits,
       "onuSerialPortParity": onuSerialPortParity,
       "onuSerialPortFlowControl": onuSerialPortFlowControl,
       "onuSerialPortPropRowStatus": onuSerialPortPropRowStatus,
       "onuSerialPortDataReadInterval": onuSerialPortDataReadInterval,
       "onuSerialPortDataReadBytes": onuSerialPortDataReadBytes,
       "onuSerialPortBufferRowStatus": onuSerialPortBufferRowStatus,
       "onuSerialPortKeepaliveMode": onuSerialPortKeepaliveMode,
       "onuSerialPortKeepaliveIdle": onuSerialPortKeepaliveIdle,
       "onuSerialPortKeepaliveTimeout": onuSerialPortKeepaliveTimeout,
       "onuSerialPortKeepaliveProbeCount": onuSerialPortKeepaliveProbeCount,
       "onuSerialPortKeepaliveRowStatus": onuSerialPortKeepaliveRowStatus,
       "onuSerialPortLoopback": onuSerialPortLoopback}
)
