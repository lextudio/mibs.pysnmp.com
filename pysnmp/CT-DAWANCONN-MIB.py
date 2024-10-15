# SNMP MIB module (CT-DAWANCONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-DAWANCONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:05 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_DaWanConnection_ObjectIdentity = ObjectIdentity
daWanConnection = _DaWanConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17)
)


class _DaWanNumConnections_Type(Integer32):
    """Custom type daWanNumConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DaWanNumConnections_Type.__name__ = "Integer32"
_DaWanNumConnections_Object = MibScalar
daWanNumConnections = _DaWanNumConnections_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 1),
    _DaWanNumConnections_Type()
)
daWanNumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanNumConnections.setStatus("mandatory")
_DaWanConnectionTable_Object = MibTable
daWanConnectionTable = _DaWanConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2)
)
if mibBuilder.loadTexts:
    daWanConnectionTable.setStatus("mandatory")
_DaWanConnectionEntry_Object = MibTableRow
daWanConnectionEntry = _DaWanConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1)
)
daWanConnectionEntry.setIndexNames(
    (0, "CT-DAWANCONN-MIB", "daWanConnectionIndex"),
)
if mibBuilder.loadTexts:
    daWanConnectionEntry.setStatus("mandatory")


class _DaWanConnectionIndex_Type(Integer32):
    """Custom type daWanConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DaWanConnectionIndex_Type.__name__ = "Integer32"
_DaWanConnectionIndex_Object = MibTableColumn
daWanConnectionIndex = _DaWanConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 1),
    _DaWanConnectionIndex_Type()
)
daWanConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionIndex.setStatus("mandatory")
_DaWanConnectionIfIndex_Type = Integer32
_DaWanConnectionIfIndex_Object = MibTableColumn
daWanConnectionIfIndex = _DaWanConnectionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 2),
    _DaWanConnectionIfIndex_Type()
)
daWanConnectionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionIfIndex.setStatus("mandatory")


class _DaWanConnectionState_Type(Integer32):
    """Custom type daWanConnectionState based on Integer32"""
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
        *(("active", 4),
          ("connected", 3),
          ("connecting", 2),
          ("disconnected", 6),
          ("disconnecting", 5),
          ("inactive", 1))
    )


_DaWanConnectionState_Type.__name__ = "Integer32"
_DaWanConnectionState_Object = MibTableColumn
daWanConnectionState = _DaWanConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 3),
    _DaWanConnectionState_Type()
)
daWanConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionState.setStatus("mandatory")


class _DaWanConnectionConnectControl_Type(Integer32):
    """Custom type daWanConnectionConnectControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2),
          ("unknown", 3))
    )


_DaWanConnectionConnectControl_Type.__name__ = "Integer32"
_DaWanConnectionConnectControl_Object = MibTableColumn
daWanConnectionConnectControl = _DaWanConnectionConnectControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 4),
    _DaWanConnectionConnectControl_Type()
)
daWanConnectionConnectControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daWanConnectionConnectControl.setStatus("mandatory")


class _DaWanConnectionConnectType_Type(Integer32):
    """Custom type daWanConnectionConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analogCircuit", 2),
          ("digitalCircuit", 1))
    )


_DaWanConnectionConnectType_Type.__name__ = "Integer32"
_DaWanConnectionConnectType_Object = MibTableColumn
daWanConnectionConnectType = _DaWanConnectionConnectType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 5),
    _DaWanConnectionConnectType_Type()
)
daWanConnectionConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionConnectType.setStatus("mandatory")
_DaWanConnectionDeviceIndex_Type = Integer32
_DaWanConnectionDeviceIndex_Object = MibTableColumn
daWanConnectionDeviceIndex = _DaWanConnectionDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 6),
    _DaWanConnectionDeviceIndex_Type()
)
daWanConnectionDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionDeviceIndex.setStatus("mandatory")
_DaWanConnectionConnectSpeed_Type = Gauge32
_DaWanConnectionConnectSpeed_Object = MibTableColumn
daWanConnectionConnectSpeed = _DaWanConnectionConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 7),
    _DaWanConnectionConnectSpeed_Type()
)
daWanConnectionConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionConnectSpeed.setStatus("mandatory")


class _DaWanConnectionLocalAddress_Type(DisplayString):
    """Custom type daWanConnectionLocalAddress based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DaWanConnectionLocalAddress_Type.__name__ = "DisplayString"
_DaWanConnectionLocalAddress_Object = MibTableColumn
daWanConnectionLocalAddress = _DaWanConnectionLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 8),
    _DaWanConnectionLocalAddress_Type()
)
daWanConnectionLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionLocalAddress.setStatus("mandatory")


class _DaWanConnectionPeerAddress_Type(DisplayString):
    """Custom type daWanConnectionPeerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DaWanConnectionPeerAddress_Type.__name__ = "DisplayString"
_DaWanConnectionPeerAddress_Object = MibTableColumn
daWanConnectionPeerAddress = _DaWanConnectionPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 9),
    _DaWanConnectionPeerAddress_Type()
)
daWanConnectionPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionPeerAddress.setStatus("mandatory")


class _DaWanConnectionSubAddress_Type(DisplayString):
    """Custom type daWanConnectionSubAddress based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DaWanConnectionSubAddress_Type.__name__ = "DisplayString"
_DaWanConnectionSubAddress_Object = MibTableColumn
daWanConnectionSubAddress = _DaWanConnectionSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 10),
    _DaWanConnectionSubAddress_Type()
)
daWanConnectionSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionSubAddress.setStatus("mandatory")


class _DaWanConnectionInfoType_Type(Integer32):
    """Custom type daWanConnectionInfoType based on Integer32"""
    defaultValue = 1

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
        *(("audio31", 6),
          ("audio7", 7),
          ("fax", 10),
          ("other", 1),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_DaWanConnectionInfoType_Type.__name__ = "Integer32"
_DaWanConnectionInfoType_Object = MibTableColumn
daWanConnectionInfoType = _DaWanConnectionInfoType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 11),
    _DaWanConnectionInfoType_Type()
)
daWanConnectionInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionInfoType.setStatus("mandatory")
_DaWanConnectionChargedUnits_Type = Integer32
_DaWanConnectionChargedUnits_Object = MibTableColumn
daWanConnectionChargedUnits = _DaWanConnectionChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 12),
    _DaWanConnectionChargedUnits_Type()
)
daWanConnectionChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionChargedUnits.setStatus("mandatory")
_DaWanConnectionConnectTime_Type = TimeStamp
_DaWanConnectionConnectTime_Object = MibTableColumn
daWanConnectionConnectTime = _DaWanConnectionConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 13),
    _DaWanConnectionConnectTime_Type()
)
daWanConnectionConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionConnectTime.setStatus("mandatory")


class _DaWanConnectionConnectDirection_Type(Integer32):
    """Custom type daWanConnectionConnectDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_DaWanConnectionConnectDirection_Type.__name__ = "Integer32"
_DaWanConnectionConnectDirection_Object = MibTableColumn
daWanConnectionConnectDirection = _DaWanConnectionConnectDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 14),
    _DaWanConnectionConnectDirection_Type()
)
daWanConnectionConnectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionConnectDirection.setStatus("mandatory")
_DaWanConnectionDisconnectTime_Type = TimeStamp
_DaWanConnectionDisconnectTime_Object = MibTableColumn
daWanConnectionDisconnectTime = _DaWanConnectionDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 15),
    _DaWanConnectionDisconnectTime_Type()
)
daWanConnectionDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionDisconnectTime.setStatus("mandatory")


class _DaWanConnectionDisconnectDirection_Type(Integer32):
    """Custom type daWanConnectionDisconnectDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_DaWanConnectionDisconnectDirection_Type.__name__ = "Integer32"
_DaWanConnectionDisconnectDirection_Object = MibTableColumn
daWanConnectionDisconnectDirection = _DaWanConnectionDisconnectDirection_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 16),
    _DaWanConnectionDisconnectDirection_Type()
)
daWanConnectionDisconnectDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionDisconnectDirection.setStatus("mandatory")
_DaWanConnectionDisconnectCause_Type = Integer32
_DaWanConnectionDisconnectCause_Object = MibTableColumn
daWanConnectionDisconnectCause = _DaWanConnectionDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 17),
    _DaWanConnectionDisconnectCause_Type()
)
daWanConnectionDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionDisconnectCause.setStatus("mandatory")


class _DaWanConnectionDisconnectText_Type(DisplayString):
    """Custom type daWanConnectionDisconnectText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DaWanConnectionDisconnectText_Type.__name__ = "DisplayString"
_DaWanConnectionDisconnectText_Object = MibTableColumn
daWanConnectionDisconnectText = _DaWanConnectionDisconnectText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 18),
    _DaWanConnectionDisconnectText_Type()
)
daWanConnectionDisconnectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionDisconnectText.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-DAWANCONN-MIB",
    **{"DisplayString": DisplayString,
       "ctSSA": ctSSA,
       "daWanConnection": daWanConnection,
       "daWanNumConnections": daWanNumConnections,
       "daWanConnectionTable": daWanConnectionTable,
       "daWanConnectionEntry": daWanConnectionEntry,
       "daWanConnectionIndex": daWanConnectionIndex,
       "daWanConnectionIfIndex": daWanConnectionIfIndex,
       "daWanConnectionState": daWanConnectionState,
       "daWanConnectionConnectControl": daWanConnectionConnectControl,
       "daWanConnectionConnectType": daWanConnectionConnectType,
       "daWanConnectionDeviceIndex": daWanConnectionDeviceIndex,
       "daWanConnectionConnectSpeed": daWanConnectionConnectSpeed,
       "daWanConnectionLocalAddress": daWanConnectionLocalAddress,
       "daWanConnectionPeerAddress": daWanConnectionPeerAddress,
       "daWanConnectionSubAddress": daWanConnectionSubAddress,
       "daWanConnectionInfoType": daWanConnectionInfoType,
       "daWanConnectionChargedUnits": daWanConnectionChargedUnits,
       "daWanConnectionConnectTime": daWanConnectionConnectTime,
       "daWanConnectionConnectDirection": daWanConnectionConnectDirection,
       "daWanConnectionDisconnectTime": daWanConnectionDisconnectTime,
       "daWanConnectionDisconnectDirection": daWanConnectionDisconnectDirection,
       "daWanConnectionDisconnectCause": daWanConnectionDisconnectCause,
       "daWanConnectionDisconnectText": daWanConnectionDisconnectText}
)
