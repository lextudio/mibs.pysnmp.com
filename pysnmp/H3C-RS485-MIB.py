# SNMP MIB module (H3C-RS485-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-RS485-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:21 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cRS485 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cRS485Properties_ObjectIdentity = ObjectIdentity
h3cRS485Properties = _H3cRS485Properties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1)
)
_H3cRS485PropertiesTable_Object = MibTable
h3cRS485PropertiesTable = _H3cRS485PropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1)
)
if mibBuilder.loadTexts:
    h3cRS485PropertiesTable.setStatus("current")
_H3cRS485PropertiesEntry_Object = MibTableRow
h3cRS485PropertiesEntry = _H3cRS485PropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1)
)
h3cRS485PropertiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cRS485PropertiesEntry.setStatus("current")


class _H3cRS485RawSessionNextIndex_Type(Integer32):
    """Custom type h3cRS485RawSessionNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cRS485RawSessionNextIndex_Type.__name__ = "Integer32"
_H3cRS485RawSessionNextIndex_Object = MibTableColumn
h3cRS485RawSessionNextIndex = _H3cRS485RawSessionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 1),
    _H3cRS485RawSessionNextIndex_Type()
)
h3cRS485RawSessionNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRS485RawSessionNextIndex.setStatus("current")


class _H3cRS485BaudRate_Type(Integer32):
    """Custom type h3cRS485BaudRate based on Integer32"""
    defaultValue = 6

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
        *(("bautRate115200", 10),
          ("bautRate1200", 3),
          ("bautRate19200", 7),
          ("bautRate2400", 4),
          ("bautRate300", 1),
          ("bautRate38400", 8),
          ("bautRate4800", 5),
          ("bautRate57600", 9),
          ("bautRate600", 2),
          ("bautRate9600", 6))
    )


_H3cRS485BaudRate_Type.__name__ = "Integer32"
_H3cRS485BaudRate_Object = MibTableColumn
h3cRS485BaudRate = _H3cRS485BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 2),
    _H3cRS485BaudRate_Type()
)
h3cRS485BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485BaudRate.setStatus("current")


class _H3cRS485DataBits_Type(Integer32):
    """Custom type h3cRS485DataBits based on Integer32"""
    defaultValue = 4

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
        *(("eight", 4),
          ("five", 1),
          ("seven", 3),
          ("six", 2))
    )


_H3cRS485DataBits_Type.__name__ = "Integer32"
_H3cRS485DataBits_Object = MibTableColumn
h3cRS485DataBits = _H3cRS485DataBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 3),
    _H3cRS485DataBits_Type()
)
h3cRS485DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485DataBits.setStatus("current")
if mibBuilder.loadTexts:
    h3cRS485DataBits.setUnits("bit")


class _H3cRS485Parity_Type(Integer32):
    """Custom type h3cRS485Parity based on Integer32"""
    defaultValue = 1

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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_H3cRS485Parity_Type.__name__ = "Integer32"
_H3cRS485Parity_Object = MibTableColumn
h3cRS485Parity = _H3cRS485Parity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 4),
    _H3cRS485Parity_Type()
)
h3cRS485Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485Parity.setStatus("current")


class _H3cRS485StopBits_Type(Integer32):
    """Custom type h3cRS485StopBits based on Integer32"""
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
        *(("one", 1),
          ("oneAndHalf", 3),
          ("two", 2))
    )


_H3cRS485StopBits_Type.__name__ = "Integer32"
_H3cRS485StopBits_Object = MibTableColumn
h3cRS485StopBits = _H3cRS485StopBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 5),
    _H3cRS485StopBits_Type()
)
h3cRS485StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485StopBits.setStatus("current")
if mibBuilder.loadTexts:
    h3cRS485StopBits.setUnits("bit")


class _H3cRS485FlowControl_Type(Integer32):
    """Custom type h3cRS485FlowControl based on Integer32"""
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
        *(("hardware", 2),
          ("none", 1),
          ("xonOrxoff", 3))
    )


_H3cRS485FlowControl_Type.__name__ = "Integer32"
_H3cRS485FlowControl_Object = MibTableColumn
h3cRS485FlowControl = _H3cRS485FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 6),
    _H3cRS485FlowControl_Type()
)
h3cRS485FlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485FlowControl.setStatus("current")
_H3cRS485TXCharacters_Type = Integer32
_H3cRS485TXCharacters_Object = MibTableColumn
h3cRS485TXCharacters = _H3cRS485TXCharacters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 7),
    _H3cRS485TXCharacters_Type()
)
h3cRS485TXCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRS485TXCharacters.setStatus("current")
_H3cRS485RXCharacters_Type = Integer32
_H3cRS485RXCharacters_Object = MibTableColumn
h3cRS485RXCharacters = _H3cRS485RXCharacters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 8),
    _H3cRS485RXCharacters_Type()
)
h3cRS485RXCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRS485RXCharacters.setStatus("current")
_H3cRS485TXErrCharacters_Type = Integer32
_H3cRS485TXErrCharacters_Object = MibTableColumn
h3cRS485TXErrCharacters = _H3cRS485TXErrCharacters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 9),
    _H3cRS485TXErrCharacters_Type()
)
h3cRS485TXErrCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRS485TXErrCharacters.setStatus("current")
_H3cRS485RXErrCharacters_Type = Integer32
_H3cRS485RXErrCharacters_Object = MibTableColumn
h3cRS485RXErrCharacters = _H3cRS485RXErrCharacters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 10),
    _H3cRS485RXErrCharacters_Type()
)
h3cRS485RXErrCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRS485RXErrCharacters.setStatus("current")


class _H3cRS485ResetCharacters_Type(Integer32):
    """Custom type h3cRS485ResetCharacters based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("counting", 1))
    )


_H3cRS485ResetCharacters_Type.__name__ = "Integer32"
_H3cRS485ResetCharacters_Object = MibTableColumn
h3cRS485ResetCharacters = _H3cRS485ResetCharacters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 1, 1, 1, 11),
    _H3cRS485ResetCharacters_Type()
)
h3cRS485ResetCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485ResetCharacters.setStatus("current")
_H3cRS485RawSessions_ObjectIdentity = ObjectIdentity
h3cRS485RawSessions = _H3cRS485RawSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2)
)
_H3cRS485RawSessionSummary_ObjectIdentity = ObjectIdentity
h3cRS485RawSessionSummary = _H3cRS485RawSessionSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 1)
)


class _H3cRS485RawSessionMaxNum_Type(Integer32):
    """Custom type h3cRS485RawSessionMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cRS485RawSessionMaxNum_Type.__name__ = "Integer32"
_H3cRS485RawSessionMaxNum_Object = MibScalar
h3cRS485RawSessionMaxNum = _H3cRS485RawSessionMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 1, 1),
    _H3cRS485RawSessionMaxNum_Type()
)
h3cRS485RawSessionMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRS485RawSessionMaxNum.setStatus("current")
_H3cRS485RawSessionTable_Object = MibTable
h3cRS485RawSessionTable = _H3cRS485RawSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2)
)
if mibBuilder.loadTexts:
    h3cRS485RawSessionTable.setStatus("current")
_H3cRS485RawSessionEntry_Object = MibTableRow
h3cRS485RawSessionEntry = _H3cRS485RawSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1)
)
h3cRS485RawSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-RS485-MIB", "h3cRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    h3cRS485RawSessionEntry.setStatus("current")


class _H3cRS485SessionIndex_Type(Integer32):
    """Custom type h3cRS485SessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_H3cRS485SessionIndex_Type.__name__ = "Integer32"
_H3cRS485SessionIndex_Object = MibTableColumn
h3cRS485SessionIndex = _H3cRS485SessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1, 1),
    _H3cRS485SessionIndex_Type()
)
h3cRS485SessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRS485SessionIndex.setStatus("current")


class _H3cRS485SessionType_Type(Integer32):
    """Custom type h3cRS485SessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcpClient", 2),
          ("tcpServer", 3),
          ("udp", 1))
    )


_H3cRS485SessionType_Type.__name__ = "Integer32"
_H3cRS485SessionType_Object = MibTableColumn
h3cRS485SessionType = _H3cRS485SessionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1, 2),
    _H3cRS485SessionType_Type()
)
h3cRS485SessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485SessionType.setStatus("current")


class _H3cRS485SessionAddType_Type(InetAddressType):
    """Custom type h3cRS485SessionAddType based on InetAddressType"""


_H3cRS485SessionAddType_Object = MibTableColumn
h3cRS485SessionAddType = _H3cRS485SessionAddType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1, 3),
    _H3cRS485SessionAddType_Type()
)
h3cRS485SessionAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRS485SessionAddType.setStatus("current")
_H3cRS485SessionRemoteIP_Type = InetAddress
_H3cRS485SessionRemoteIP_Object = MibTableColumn
h3cRS485SessionRemoteIP = _H3cRS485SessionRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1, 4),
    _H3cRS485SessionRemoteIP_Type()
)
h3cRS485SessionRemoteIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRS485SessionRemoteIP.setStatus("current")


class _H3cRS485SessionRemotePort_Type(Integer32):
    """Custom type h3cRS485SessionRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_H3cRS485SessionRemotePort_Type.__name__ = "Integer32"
_H3cRS485SessionRemotePort_Object = MibTableColumn
h3cRS485SessionRemotePort = _H3cRS485SessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1, 5),
    _H3cRS485SessionRemotePort_Type()
)
h3cRS485SessionRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRS485SessionRemotePort.setStatus("current")


class _H3cRS485SessionLocalPort_Type(Integer32):
    """Custom type h3cRS485SessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_H3cRS485SessionLocalPort_Type.__name__ = "Integer32"
_H3cRS485SessionLocalPort_Object = MibTableColumn
h3cRS485SessionLocalPort = _H3cRS485SessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1, 6),
    _H3cRS485SessionLocalPort_Type()
)
h3cRS485SessionLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRS485SessionLocalPort.setStatus("current")
_H3cRS485SessionStatus_Type = RowStatus
_H3cRS485SessionStatus_Object = MibTableColumn
h3cRS485SessionStatus = _H3cRS485SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 2, 1, 7),
    _H3cRS485SessionStatus_Type()
)
h3cRS485SessionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRS485SessionStatus.setStatus("current")
_H3cRS485RawSessionErrInfoTable_Object = MibTable
h3cRS485RawSessionErrInfoTable = _H3cRS485RawSessionErrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 3)
)
if mibBuilder.loadTexts:
    h3cRS485RawSessionErrInfoTable.setStatus("current")
_H3cRS485RawSessionErrInfoEntry_Object = MibTableRow
h3cRS485RawSessionErrInfoEntry = _H3cRS485RawSessionErrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 3, 1)
)
h3cRS485RawSessionErrInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-RS485-MIB", "h3cRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    h3cRS485RawSessionErrInfoEntry.setStatus("current")
_H3cRS485RawSessionErrInfo_Type = DisplayString
_H3cRS485RawSessionErrInfo_Object = MibTableColumn
h3cRS485RawSessionErrInfo = _H3cRS485RawSessionErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 109, 2, 3, 1, 1),
    _H3cRS485RawSessionErrInfo_Type()
)
h3cRS485RawSessionErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRS485RawSessionErrInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-RS485-MIB",
    **{"h3cRS485": h3cRS485,
       "h3cRS485Properties": h3cRS485Properties,
       "h3cRS485PropertiesTable": h3cRS485PropertiesTable,
       "h3cRS485PropertiesEntry": h3cRS485PropertiesEntry,
       "h3cRS485RawSessionNextIndex": h3cRS485RawSessionNextIndex,
       "h3cRS485BaudRate": h3cRS485BaudRate,
       "h3cRS485DataBits": h3cRS485DataBits,
       "h3cRS485Parity": h3cRS485Parity,
       "h3cRS485StopBits": h3cRS485StopBits,
       "h3cRS485FlowControl": h3cRS485FlowControl,
       "h3cRS485TXCharacters": h3cRS485TXCharacters,
       "h3cRS485RXCharacters": h3cRS485RXCharacters,
       "h3cRS485TXErrCharacters": h3cRS485TXErrCharacters,
       "h3cRS485RXErrCharacters": h3cRS485RXErrCharacters,
       "h3cRS485ResetCharacters": h3cRS485ResetCharacters,
       "h3cRS485RawSessions": h3cRS485RawSessions,
       "h3cRS485RawSessionSummary": h3cRS485RawSessionSummary,
       "h3cRS485RawSessionMaxNum": h3cRS485RawSessionMaxNum,
       "h3cRS485RawSessionTable": h3cRS485RawSessionTable,
       "h3cRS485RawSessionEntry": h3cRS485RawSessionEntry,
       "h3cRS485SessionIndex": h3cRS485SessionIndex,
       "h3cRS485SessionType": h3cRS485SessionType,
       "h3cRS485SessionAddType": h3cRS485SessionAddType,
       "h3cRS485SessionRemoteIP": h3cRS485SessionRemoteIP,
       "h3cRS485SessionRemotePort": h3cRS485SessionRemotePort,
       "h3cRS485SessionLocalPort": h3cRS485SessionLocalPort,
       "h3cRS485SessionStatus": h3cRS485SessionStatus,
       "h3cRS485RawSessionErrInfoTable": h3cRS485RawSessionErrInfoTable,
       "h3cRS485RawSessionErrInfoEntry": h3cRS485RawSessionErrInfoEntry,
       "h3cRS485RawSessionErrInfo": h3cRS485RawSessionErrInfo}
)
