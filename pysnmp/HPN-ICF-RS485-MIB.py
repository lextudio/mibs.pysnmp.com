# SNMP MIB module (HPN-ICF-RS485-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RS485-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:45 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfRS485 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfRS485Properties_ObjectIdentity = ObjectIdentity
hpnicfRS485Properties = _HpnicfRS485Properties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1)
)
_HpnicfRS485PropertiesTable_Object = MibTable
hpnicfRS485PropertiesTable = _HpnicfRS485PropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfRS485PropertiesTable.setStatus("current")
_HpnicfRS485PropertiesEntry_Object = MibTableRow
hpnicfRS485PropertiesEntry = _HpnicfRS485PropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1)
)
hpnicfRS485PropertiesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRS485PropertiesEntry.setStatus("current")


class _HpnicfRS485RawSessionNextIndex_Type(Integer32):
    """Custom type hpnicfRS485RawSessionNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfRS485RawSessionNextIndex_Type.__name__ = "Integer32"
_HpnicfRS485RawSessionNextIndex_Object = MibTableColumn
hpnicfRS485RawSessionNextIndex = _HpnicfRS485RawSessionNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 1),
    _HpnicfRS485RawSessionNextIndex_Type()
)
hpnicfRS485RawSessionNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRS485RawSessionNextIndex.setStatus("current")


class _HpnicfRS485BaudRate_Type(Integer32):
    """Custom type hpnicfRS485BaudRate based on Integer32"""
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


_HpnicfRS485BaudRate_Type.__name__ = "Integer32"
_HpnicfRS485BaudRate_Object = MibTableColumn
hpnicfRS485BaudRate = _HpnicfRS485BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 2),
    _HpnicfRS485BaudRate_Type()
)
hpnicfRS485BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485BaudRate.setStatus("current")


class _HpnicfRS485DataBits_Type(Integer32):
    """Custom type hpnicfRS485DataBits based on Integer32"""
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


_HpnicfRS485DataBits_Type.__name__ = "Integer32"
_HpnicfRS485DataBits_Object = MibTableColumn
hpnicfRS485DataBits = _HpnicfRS485DataBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 3),
    _HpnicfRS485DataBits_Type()
)
hpnicfRS485DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485DataBits.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRS485DataBits.setUnits("bit")


class _HpnicfRS485Parity_Type(Integer32):
    """Custom type hpnicfRS485Parity based on Integer32"""
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


_HpnicfRS485Parity_Type.__name__ = "Integer32"
_HpnicfRS485Parity_Object = MibTableColumn
hpnicfRS485Parity = _HpnicfRS485Parity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 4),
    _HpnicfRS485Parity_Type()
)
hpnicfRS485Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485Parity.setStatus("current")


class _HpnicfRS485StopBits_Type(Integer32):
    """Custom type hpnicfRS485StopBits based on Integer32"""
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


_HpnicfRS485StopBits_Type.__name__ = "Integer32"
_HpnicfRS485StopBits_Object = MibTableColumn
hpnicfRS485StopBits = _HpnicfRS485StopBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 5),
    _HpnicfRS485StopBits_Type()
)
hpnicfRS485StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485StopBits.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRS485StopBits.setUnits("bit")


class _HpnicfRS485FlowControl_Type(Integer32):
    """Custom type hpnicfRS485FlowControl based on Integer32"""
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


_HpnicfRS485FlowControl_Type.__name__ = "Integer32"
_HpnicfRS485FlowControl_Object = MibTableColumn
hpnicfRS485FlowControl = _HpnicfRS485FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 6),
    _HpnicfRS485FlowControl_Type()
)
hpnicfRS485FlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485FlowControl.setStatus("current")
_HpnicfRS485TXCharacters_Type = Integer32
_HpnicfRS485TXCharacters_Object = MibTableColumn
hpnicfRS485TXCharacters = _HpnicfRS485TXCharacters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 7),
    _HpnicfRS485TXCharacters_Type()
)
hpnicfRS485TXCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRS485TXCharacters.setStatus("current")
_HpnicfRS485RXCharacters_Type = Integer32
_HpnicfRS485RXCharacters_Object = MibTableColumn
hpnicfRS485RXCharacters = _HpnicfRS485RXCharacters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 8),
    _HpnicfRS485RXCharacters_Type()
)
hpnicfRS485RXCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRS485RXCharacters.setStatus("current")
_HpnicfRS485TXErrCharacters_Type = Integer32
_HpnicfRS485TXErrCharacters_Object = MibTableColumn
hpnicfRS485TXErrCharacters = _HpnicfRS485TXErrCharacters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 9),
    _HpnicfRS485TXErrCharacters_Type()
)
hpnicfRS485TXErrCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRS485TXErrCharacters.setStatus("current")
_HpnicfRS485RXErrCharacters_Type = Integer32
_HpnicfRS485RXErrCharacters_Object = MibTableColumn
hpnicfRS485RXErrCharacters = _HpnicfRS485RXErrCharacters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 10),
    _HpnicfRS485RXErrCharacters_Type()
)
hpnicfRS485RXErrCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRS485RXErrCharacters.setStatus("current")


class _HpnicfRS485ResetCharacters_Type(Integer32):
    """Custom type hpnicfRS485ResetCharacters based on Integer32"""
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


_HpnicfRS485ResetCharacters_Type.__name__ = "Integer32"
_HpnicfRS485ResetCharacters_Object = MibTableColumn
hpnicfRS485ResetCharacters = _HpnicfRS485ResetCharacters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 1, 1, 1, 11),
    _HpnicfRS485ResetCharacters_Type()
)
hpnicfRS485ResetCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485ResetCharacters.setStatus("current")
_HpnicfRS485RawSessions_ObjectIdentity = ObjectIdentity
hpnicfRS485RawSessions = _HpnicfRS485RawSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2)
)
_HpnicfRS485RawSessionSummary_ObjectIdentity = ObjectIdentity
hpnicfRS485RawSessionSummary = _HpnicfRS485RawSessionSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 1)
)


class _HpnicfRS485RawSessionMaxNum_Type(Integer32):
    """Custom type hpnicfRS485RawSessionMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfRS485RawSessionMaxNum_Type.__name__ = "Integer32"
_HpnicfRS485RawSessionMaxNum_Object = MibScalar
hpnicfRS485RawSessionMaxNum = _HpnicfRS485RawSessionMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 1, 1),
    _HpnicfRS485RawSessionMaxNum_Type()
)
hpnicfRS485RawSessionMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRS485RawSessionMaxNum.setStatus("current")
_HpnicfRS485RawSessionTable_Object = MibTable
hpnicfRS485RawSessionTable = _HpnicfRS485RawSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfRS485RawSessionTable.setStatus("current")
_HpnicfRS485RawSessionEntry_Object = MibTableRow
hpnicfRS485RawSessionEntry = _HpnicfRS485RawSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1)
)
hpnicfRS485RawSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-RS485-MIB", "hpnicfRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRS485RawSessionEntry.setStatus("current")


class _HpnicfRS485SessionIndex_Type(Integer32):
    """Custom type hpnicfRS485SessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfRS485SessionIndex_Type.__name__ = "Integer32"
_HpnicfRS485SessionIndex_Object = MibTableColumn
hpnicfRS485SessionIndex = _HpnicfRS485SessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1, 1),
    _HpnicfRS485SessionIndex_Type()
)
hpnicfRS485SessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRS485SessionIndex.setStatus("current")


class _HpnicfRS485SessionType_Type(Integer32):
    """Custom type hpnicfRS485SessionType based on Integer32"""
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


_HpnicfRS485SessionType_Type.__name__ = "Integer32"
_HpnicfRS485SessionType_Object = MibTableColumn
hpnicfRS485SessionType = _HpnicfRS485SessionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1, 2),
    _HpnicfRS485SessionType_Type()
)
hpnicfRS485SessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485SessionType.setStatus("current")


class _HpnicfRS485SessionAddType_Type(InetAddressType):
    """Custom type hpnicfRS485SessionAddType based on InetAddressType"""


_HpnicfRS485SessionAddType_Object = MibTableColumn
hpnicfRS485SessionAddType = _HpnicfRS485SessionAddType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1, 3),
    _HpnicfRS485SessionAddType_Type()
)
hpnicfRS485SessionAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRS485SessionAddType.setStatus("current")
_HpnicfRS485SessionRemoteIP_Type = InetAddress
_HpnicfRS485SessionRemoteIP_Object = MibTableColumn
hpnicfRS485SessionRemoteIP = _HpnicfRS485SessionRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1, 4),
    _HpnicfRS485SessionRemoteIP_Type()
)
hpnicfRS485SessionRemoteIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRS485SessionRemoteIP.setStatus("current")


class _HpnicfRS485SessionRemotePort_Type(Integer32):
    """Custom type hpnicfRS485SessionRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HpnicfRS485SessionRemotePort_Type.__name__ = "Integer32"
_HpnicfRS485SessionRemotePort_Object = MibTableColumn
hpnicfRS485SessionRemotePort = _HpnicfRS485SessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1, 5),
    _HpnicfRS485SessionRemotePort_Type()
)
hpnicfRS485SessionRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRS485SessionRemotePort.setStatus("current")


class _HpnicfRS485SessionLocalPort_Type(Integer32):
    """Custom type hpnicfRS485SessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HpnicfRS485SessionLocalPort_Type.__name__ = "Integer32"
_HpnicfRS485SessionLocalPort_Object = MibTableColumn
hpnicfRS485SessionLocalPort = _HpnicfRS485SessionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1, 6),
    _HpnicfRS485SessionLocalPort_Type()
)
hpnicfRS485SessionLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRS485SessionLocalPort.setStatus("current")
_HpnicfRS485SessionStatus_Type = RowStatus
_HpnicfRS485SessionStatus_Object = MibTableColumn
hpnicfRS485SessionStatus = _HpnicfRS485SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 2, 1, 7),
    _HpnicfRS485SessionStatus_Type()
)
hpnicfRS485SessionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRS485SessionStatus.setStatus("current")
_HpnicfRS485RawSessionErrInfoTable_Object = MibTable
hpnicfRS485RawSessionErrInfoTable = _HpnicfRS485RawSessionErrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfRS485RawSessionErrInfoTable.setStatus("current")
_HpnicfRS485RawSessionErrInfoEntry_Object = MibTableRow
hpnicfRS485RawSessionErrInfoEntry = _HpnicfRS485RawSessionErrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 3, 1)
)
hpnicfRS485RawSessionErrInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-RS485-MIB", "hpnicfRS485SessionIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRS485RawSessionErrInfoEntry.setStatus("current")
_HpnicfRS485RawSessionErrInfo_Type = DisplayString
_HpnicfRS485RawSessionErrInfo_Object = MibTableColumn
hpnicfRS485RawSessionErrInfo = _HpnicfRS485RawSessionErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109, 2, 3, 1, 1),
    _HpnicfRS485RawSessionErrInfo_Type()
)
hpnicfRS485RawSessionErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRS485RawSessionErrInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RS485-MIB",
    **{"hpnicfRS485": hpnicfRS485,
       "hpnicfRS485Properties": hpnicfRS485Properties,
       "hpnicfRS485PropertiesTable": hpnicfRS485PropertiesTable,
       "hpnicfRS485PropertiesEntry": hpnicfRS485PropertiesEntry,
       "hpnicfRS485RawSessionNextIndex": hpnicfRS485RawSessionNextIndex,
       "hpnicfRS485BaudRate": hpnicfRS485BaudRate,
       "hpnicfRS485DataBits": hpnicfRS485DataBits,
       "hpnicfRS485Parity": hpnicfRS485Parity,
       "hpnicfRS485StopBits": hpnicfRS485StopBits,
       "hpnicfRS485FlowControl": hpnicfRS485FlowControl,
       "hpnicfRS485TXCharacters": hpnicfRS485TXCharacters,
       "hpnicfRS485RXCharacters": hpnicfRS485RXCharacters,
       "hpnicfRS485TXErrCharacters": hpnicfRS485TXErrCharacters,
       "hpnicfRS485RXErrCharacters": hpnicfRS485RXErrCharacters,
       "hpnicfRS485ResetCharacters": hpnicfRS485ResetCharacters,
       "hpnicfRS485RawSessions": hpnicfRS485RawSessions,
       "hpnicfRS485RawSessionSummary": hpnicfRS485RawSessionSummary,
       "hpnicfRS485RawSessionMaxNum": hpnicfRS485RawSessionMaxNum,
       "hpnicfRS485RawSessionTable": hpnicfRS485RawSessionTable,
       "hpnicfRS485RawSessionEntry": hpnicfRS485RawSessionEntry,
       "hpnicfRS485SessionIndex": hpnicfRS485SessionIndex,
       "hpnicfRS485SessionType": hpnicfRS485SessionType,
       "hpnicfRS485SessionAddType": hpnicfRS485SessionAddType,
       "hpnicfRS485SessionRemoteIP": hpnicfRS485SessionRemoteIP,
       "hpnicfRS485SessionRemotePort": hpnicfRS485SessionRemotePort,
       "hpnicfRS485SessionLocalPort": hpnicfRS485SessionLocalPort,
       "hpnicfRS485SessionStatus": hpnicfRS485SessionStatus,
       "hpnicfRS485RawSessionErrInfoTable": hpnicfRS485RawSessionErrInfoTable,
       "hpnicfRS485RawSessionErrInfoEntry": hpnicfRS485RawSessionErrInfoEntry,
       "hpnicfRS485RawSessionErrInfo": hpnicfRS485RawSessionErrInfo}
)
