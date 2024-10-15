# SNMP MIB module (FOUNDRY-BGP4V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-BGP4V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:40 2024
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

(Bgp4V2AddressFamilyIdentifierTC,
 Bgp4V2IdentifierTC,
 Bgp4V2SubsequentAddressFamilyIdentifierTC) = mibBuilder.importSymbols(
    "FOUNDRY-BGP4V2-TC-MIB",
    "Bgp4V2AddressFamilyIdentifierTC",
    "Bgp4V2IdentifierTC",
    "Bgp4V2SubsequentAddressFamilyIdentifierTC")

(bgp4V2Root,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "bgp4V2Root")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

bgp4V2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1)
)
bgp4V2.setRevisions(
        ("2014-01-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bgp4V2Notifications_ObjectIdentity = ObjectIdentity
bgp4V2Notifications = _Bgp4V2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 0)
)
_Bgp4V2Objects_ObjectIdentity = ObjectIdentity
bgp4V2Objects = _Bgp4V2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1)
)
_Bgp4V2DiscontinuityTable_Object = MibTable
bgp4V2DiscontinuityTable = _Bgp4V2DiscontinuityTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bgp4V2DiscontinuityTable.setStatus("current")
_Bgp4V2DiscontinuityEntry_Object = MibTableRow
bgp4V2DiscontinuityEntry = _Bgp4V2DiscontinuityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 1, 1)
)
bgp4V2DiscontinuityEntry.setIndexNames(
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInstance"),
)
if mibBuilder.loadTexts:
    bgp4V2DiscontinuityEntry.setStatus("current")
_Bgp4V2DiscontinuityTime_Type = TimeStamp
_Bgp4V2DiscontinuityTime_Object = MibTableColumn
bgp4V2DiscontinuityTime = _Bgp4V2DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 1, 1, 1),
    _Bgp4V2DiscontinuityTime_Type()
)
bgp4V2DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2DiscontinuityTime.setStatus("current")
_Bgp4V2PeerTable_Object = MibTable
bgp4V2PeerTable = _Bgp4V2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    bgp4V2PeerTable.setStatus("current")
_Bgp4V2PeerEntry_Object = MibTableRow
bgp4V2PeerEntry = _Bgp4V2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1)
)
bgp4V2PeerEntry.setIndexNames(
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInstance"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalAddrType"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalAddr"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddrType"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    bgp4V2PeerEntry.setStatus("current")


class _Bgp4V2PeerInstance_Type(Unsigned32):
    """Custom type bgp4V2PeerInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Bgp4V2PeerInstance_Type.__name__ = "Unsigned32"
_Bgp4V2PeerInstance_Object = MibTableColumn
bgp4V2PeerInstance = _Bgp4V2PeerInstance_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 1),
    _Bgp4V2PeerInstance_Type()
)
bgp4V2PeerInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2PeerInstance.setStatus("current")
_Bgp4V2PeerLocalAddrType_Type = InetAddressType
_Bgp4V2PeerLocalAddrType_Object = MibTableColumn
bgp4V2PeerLocalAddrType = _Bgp4V2PeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 2),
    _Bgp4V2PeerLocalAddrType_Type()
)
bgp4V2PeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLocalAddrType.setStatus("current")
_Bgp4V2PeerLocalAddr_Type = InetAddress
_Bgp4V2PeerLocalAddr_Object = MibTableColumn
bgp4V2PeerLocalAddr = _Bgp4V2PeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 3),
    _Bgp4V2PeerLocalAddr_Type()
)
bgp4V2PeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLocalAddr.setStatus("current")
_Bgp4V2PeerRemoteAddrType_Type = InetAddressType
_Bgp4V2PeerRemoteAddrType_Object = MibTableColumn
bgp4V2PeerRemoteAddrType = _Bgp4V2PeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 4),
    _Bgp4V2PeerRemoteAddrType_Type()
)
bgp4V2PeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2PeerRemoteAddrType.setStatus("current")
_Bgp4V2PeerRemoteAddr_Type = InetAddress
_Bgp4V2PeerRemoteAddr_Object = MibTableColumn
bgp4V2PeerRemoteAddr = _Bgp4V2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 5),
    _Bgp4V2PeerRemoteAddr_Type()
)
bgp4V2PeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2PeerRemoteAddr.setStatus("current")
_Bgp4V2PeerLocalPort_Type = InetPortNumber
_Bgp4V2PeerLocalPort_Object = MibTableColumn
bgp4V2PeerLocalPort = _Bgp4V2PeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 6),
    _Bgp4V2PeerLocalPort_Type()
)
bgp4V2PeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLocalPort.setStatus("current")
_Bgp4V2PeerLocalAs_Type = InetAutonomousSystemNumber
_Bgp4V2PeerLocalAs_Object = MibTableColumn
bgp4V2PeerLocalAs = _Bgp4V2PeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 7),
    _Bgp4V2PeerLocalAs_Type()
)
bgp4V2PeerLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLocalAs.setStatus("current")
_Bgp4V2PeerLocalIdentifier_Type = SnmpAdminString
_Bgp4V2PeerLocalIdentifier_Object = MibTableColumn
bgp4V2PeerLocalIdentifier = _Bgp4V2PeerLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 8),
    _Bgp4V2PeerLocalIdentifier_Type()
)
bgp4V2PeerLocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLocalIdentifier.setStatus("current")
_Bgp4V2PeerRemotePort_Type = InetPortNumber
_Bgp4V2PeerRemotePort_Object = MibTableColumn
bgp4V2PeerRemotePort = _Bgp4V2PeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 9),
    _Bgp4V2PeerRemotePort_Type()
)
bgp4V2PeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerRemotePort.setStatus("current")
_Bgp4V2PeerRemoteAs_Type = InetAutonomousSystemNumber
_Bgp4V2PeerRemoteAs_Object = MibTableColumn
bgp4V2PeerRemoteAs = _Bgp4V2PeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 10),
    _Bgp4V2PeerRemoteAs_Type()
)
bgp4V2PeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerRemoteAs.setStatus("current")
_Bgp4V2PeerRemoteIdentifier_Type = SnmpAdminString
_Bgp4V2PeerRemoteIdentifier_Object = MibTableColumn
bgp4V2PeerRemoteIdentifier = _Bgp4V2PeerRemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 11),
    _Bgp4V2PeerRemoteIdentifier_Type()
)
bgp4V2PeerRemoteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerRemoteIdentifier.setStatus("current")


class _Bgp4V2PeerAdminStatus_Type(Integer32):
    """Custom type bgp4V2PeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halted", 1),
          ("running", 2))
    )


_Bgp4V2PeerAdminStatus_Type.__name__ = "Integer32"
_Bgp4V2PeerAdminStatus_Object = MibTableColumn
bgp4V2PeerAdminStatus = _Bgp4V2PeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 12),
    _Bgp4V2PeerAdminStatus_Type()
)
bgp4V2PeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerAdminStatus.setStatus("current")


class _Bgp4V2PeerState_Type(Integer32):
    """Custom type bgp4V2PeerState based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_Bgp4V2PeerState_Type.__name__ = "Integer32"
_Bgp4V2PeerState_Object = MibTableColumn
bgp4V2PeerState = _Bgp4V2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 13),
    _Bgp4V2PeerState_Type()
)
bgp4V2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerState.setStatus("current")
_Bgp4V2PeerDescription_Type = SnmpAdminString
_Bgp4V2PeerDescription_Object = MibTableColumn
bgp4V2PeerDescription = _Bgp4V2PeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 2, 1, 14),
    _Bgp4V2PeerDescription_Type()
)
bgp4V2PeerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerDescription.setStatus("current")
_Bgp4V2PeerErrorsTable_Object = MibTable
bgp4V2PeerErrorsTable = _Bgp4V2PeerErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    bgp4V2PeerErrorsTable.setStatus("current")
_Bgp4V2PeerErrorsEntry_Object = MibTableRow
bgp4V2PeerErrorsEntry = _Bgp4V2PeerErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bgp4V2PeerErrorsEntry.setStatus("current")


class _Bgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):
    """Custom type bgp4V2PeerLastErrorCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Bgp4V2PeerLastErrorCodeReceived_Type.__name__ = "Unsigned32"
_Bgp4V2PeerLastErrorCodeReceived_Object = MibTableColumn
bgp4V2PeerLastErrorCodeReceived = _Bgp4V2PeerLastErrorCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 1),
    _Bgp4V2PeerLastErrorCodeReceived_Type()
)
bgp4V2PeerLastErrorCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorCodeReceived.setStatus("current")


class _Bgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):
    """Custom type bgp4V2PeerLastErrorSubCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Bgp4V2PeerLastErrorSubCodeReceived_Type.__name__ = "Unsigned32"
_Bgp4V2PeerLastErrorSubCodeReceived_Object = MibTableColumn
bgp4V2PeerLastErrorSubCodeReceived = _Bgp4V2PeerLastErrorSubCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 2),
    _Bgp4V2PeerLastErrorSubCodeReceived_Type()
)
bgp4V2PeerLastErrorSubCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorSubCodeReceived.setStatus("current")
_Bgp4V2PeerLastErrorReceivedTime_Type = TimeStamp
_Bgp4V2PeerLastErrorReceivedTime_Object = MibTableColumn
bgp4V2PeerLastErrorReceivedTime = _Bgp4V2PeerLastErrorReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 3),
    _Bgp4V2PeerLastErrorReceivedTime_Type()
)
bgp4V2PeerLastErrorReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorReceivedTime.setStatus("current")
_Bgp4V2PeerLastErrorReceivedText_Type = SnmpAdminString
_Bgp4V2PeerLastErrorReceivedText_Object = MibTableColumn
bgp4V2PeerLastErrorReceivedText = _Bgp4V2PeerLastErrorReceivedText_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 4),
    _Bgp4V2PeerLastErrorReceivedText_Type()
)
bgp4V2PeerLastErrorReceivedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorReceivedText.setStatus("current")


class _Bgp4V2PeerLastErrorReceivedData_Type(OctetString):
    """Custom type bgp4V2PeerLastErrorReceivedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_Bgp4V2PeerLastErrorReceivedData_Type.__name__ = "OctetString"
_Bgp4V2PeerLastErrorReceivedData_Object = MibTableColumn
bgp4V2PeerLastErrorReceivedData = _Bgp4V2PeerLastErrorReceivedData_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 5),
    _Bgp4V2PeerLastErrorReceivedData_Type()
)
bgp4V2PeerLastErrorReceivedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorReceivedData.setStatus("current")


class _Bgp4V2PeerLastErrorCodeSent_Type(Unsigned32):
    """Custom type bgp4V2PeerLastErrorCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Bgp4V2PeerLastErrorCodeSent_Type.__name__ = "Unsigned32"
_Bgp4V2PeerLastErrorCodeSent_Object = MibTableColumn
bgp4V2PeerLastErrorCodeSent = _Bgp4V2PeerLastErrorCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 6),
    _Bgp4V2PeerLastErrorCodeSent_Type()
)
bgp4V2PeerLastErrorCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorCodeSent.setStatus("current")


class _Bgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):
    """Custom type bgp4V2PeerLastErrorSubCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Bgp4V2PeerLastErrorSubCodeSent_Type.__name__ = "Unsigned32"
_Bgp4V2PeerLastErrorSubCodeSent_Object = MibTableColumn
bgp4V2PeerLastErrorSubCodeSent = _Bgp4V2PeerLastErrorSubCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 7),
    _Bgp4V2PeerLastErrorSubCodeSent_Type()
)
bgp4V2PeerLastErrorSubCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorSubCodeSent.setStatus("current")
_Bgp4V2PeerLastErrorSentTime_Type = TimeStamp
_Bgp4V2PeerLastErrorSentTime_Object = MibTableColumn
bgp4V2PeerLastErrorSentTime = _Bgp4V2PeerLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 8),
    _Bgp4V2PeerLastErrorSentTime_Type()
)
bgp4V2PeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorSentTime.setStatus("current")
_Bgp4V2PeerLastErrorSentText_Type = SnmpAdminString
_Bgp4V2PeerLastErrorSentText_Object = MibTableColumn
bgp4V2PeerLastErrorSentText = _Bgp4V2PeerLastErrorSentText_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 9),
    _Bgp4V2PeerLastErrorSentText_Type()
)
bgp4V2PeerLastErrorSentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorSentText.setStatus("current")


class _Bgp4V2PeerLastErrorSentData_Type(OctetString):
    """Custom type bgp4V2PeerLastErrorSentData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_Bgp4V2PeerLastErrorSentData_Type.__name__ = "OctetString"
_Bgp4V2PeerLastErrorSentData_Object = MibTableColumn
bgp4V2PeerLastErrorSentData = _Bgp4V2PeerLastErrorSentData_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 3, 1, 10),
    _Bgp4V2PeerLastErrorSentData_Type()
)
bgp4V2PeerLastErrorSentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerLastErrorSentData.setStatus("current")
_Bgp4V2PeerEventTimesTable_Object = MibTable
bgp4V2PeerEventTimesTable = _Bgp4V2PeerEventTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    bgp4V2PeerEventTimesTable.setStatus("current")
_Bgp4V2PeerEventTimesEntry_Object = MibTableRow
bgp4V2PeerEventTimesEntry = _Bgp4V2PeerEventTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bgp4V2PeerEventTimesEntry.setStatus("current")
_Bgp4V2PeerFsmEstablishedTime_Type = Gauge32
_Bgp4V2PeerFsmEstablishedTime_Object = MibTableColumn
bgp4V2PeerFsmEstablishedTime = _Bgp4V2PeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 4, 1, 1),
    _Bgp4V2PeerFsmEstablishedTime_Type()
)
bgp4V2PeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerFsmEstablishedTime.setUnits("seconds")
_Bgp4V2PeerInUpdatesElapsedTime_Type = Gauge32
_Bgp4V2PeerInUpdatesElapsedTime_Object = MibTableColumn
bgp4V2PeerInUpdatesElapsedTime = _Bgp4V2PeerInUpdatesElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 4, 1, 2),
    _Bgp4V2PeerInUpdatesElapsedTime_Type()
)
bgp4V2PeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerInUpdatesElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerInUpdatesElapsedTime.setUnits("seconds")
_Bgp4V2PeerConfiguredTimersTable_Object = MibTable
bgp4V2PeerConfiguredTimersTable = _Bgp4V2PeerConfiguredTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    bgp4V2PeerConfiguredTimersTable.setStatus("current")
_Bgp4V2PeerConfiguredTimersEntry_Object = MibTableRow
bgp4V2PeerConfiguredTimersEntry = _Bgp4V2PeerConfiguredTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    bgp4V2PeerConfiguredTimersEntry.setStatus("current")


class _Bgp4V2PeerConnectRetryInterval_Type(Unsigned32):
    """Custom type bgp4V2PeerConnectRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Bgp4V2PeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_Bgp4V2PeerConnectRetryInterval_Object = MibTableColumn
bgp4V2PeerConnectRetryInterval = _Bgp4V2PeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 5, 1, 1),
    _Bgp4V2PeerConnectRetryInterval_Type()
)
bgp4V2PeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerConnectRetryInterval.setUnits("seconds")


class _Bgp4V2PeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type bgp4V2PeerHoldTimeConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_Bgp4V2PeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_Bgp4V2PeerHoldTimeConfigured_Object = MibTableColumn
bgp4V2PeerHoldTimeConfigured = _Bgp4V2PeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 5, 1, 2),
    _Bgp4V2PeerHoldTimeConfigured_Type()
)
bgp4V2PeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerHoldTimeConfigured.setUnits("seconds")


class _Bgp4V2PeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type bgp4V2PeerKeepAliveConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_Bgp4V2PeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_Bgp4V2PeerKeepAliveConfigured_Object = MibTableColumn
bgp4V2PeerKeepAliveConfigured = _Bgp4V2PeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 5, 1, 3),
    _Bgp4V2PeerKeepAliveConfigured_Type()
)
bgp4V2PeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerKeepAliveConfigured.setUnits("seconds")


class _Bgp4V2PeerMinASOrigInterval_Type(Unsigned32):
    """Custom type bgp4V2PeerMinASOrigInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Bgp4V2PeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_Bgp4V2PeerMinASOrigInterval_Object = MibTableColumn
bgp4V2PeerMinASOrigInterval = _Bgp4V2PeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 5, 1, 4),
    _Bgp4V2PeerMinASOrigInterval_Type()
)
bgp4V2PeerMinASOrigInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerMinASOrigInterval.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerMinASOrigInterval.setUnits("seconds")


class _Bgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):
    """Custom type bgp4V2PeerMinRouteAdverInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Bgp4V2PeerMinRouteAdverInterval_Type.__name__ = "Unsigned32"
_Bgp4V2PeerMinRouteAdverInterval_Object = MibTableColumn
bgp4V2PeerMinRouteAdverInterval = _Bgp4V2PeerMinRouteAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 5, 1, 5),
    _Bgp4V2PeerMinRouteAdverInterval_Type()
)
bgp4V2PeerMinRouteAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerMinRouteAdverInterval.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerMinRouteAdverInterval.setUnits("seconds")
_Bgp4V2PeerNegotiatedTimersTable_Object = MibTable
bgp4V2PeerNegotiatedTimersTable = _Bgp4V2PeerNegotiatedTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    bgp4V2PeerNegotiatedTimersTable.setStatus("current")
_Bgp4V2PeerNegotiatedTimersEntry_Object = MibTableRow
bgp4V2PeerNegotiatedTimersEntry = _Bgp4V2PeerNegotiatedTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    bgp4V2PeerNegotiatedTimersEntry.setStatus("current")


class _Bgp4V2PeerHoldTime_Type(Unsigned32):
    """Custom type bgp4V2PeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_Bgp4V2PeerHoldTime_Type.__name__ = "Unsigned32"
_Bgp4V2PeerHoldTime_Object = MibTableColumn
bgp4V2PeerHoldTime = _Bgp4V2PeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 6, 1, 1),
    _Bgp4V2PeerHoldTime_Type()
)
bgp4V2PeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerHoldTime.setUnits("seconds")


class _Bgp4V2PeerKeepAlive_Type(Unsigned32):
    """Custom type bgp4V2PeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_Bgp4V2PeerKeepAlive_Type.__name__ = "Unsigned32"
_Bgp4V2PeerKeepAlive_Object = MibTableColumn
bgp4V2PeerKeepAlive = _Bgp4V2PeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 6, 1, 2),
    _Bgp4V2PeerKeepAlive_Type()
)
bgp4V2PeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    bgp4V2PeerKeepAlive.setUnits("seconds")
_Bgp4V2PeerCountersTable_Object = MibTable
bgp4V2PeerCountersTable = _Bgp4V2PeerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    bgp4V2PeerCountersTable.setStatus("current")
_Bgp4V2PeerCountersEntry_Object = MibTableRow
bgp4V2PeerCountersEntry = _Bgp4V2PeerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    bgp4V2PeerCountersEntry.setStatus("current")
_Bgp4V2PeerInUpdates_Type = Counter32
_Bgp4V2PeerInUpdates_Object = MibTableColumn
bgp4V2PeerInUpdates = _Bgp4V2PeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 7, 1, 1),
    _Bgp4V2PeerInUpdates_Type()
)
bgp4V2PeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerInUpdates.setStatus("current")
_Bgp4V2PeerOutUpdates_Type = Counter32
_Bgp4V2PeerOutUpdates_Object = MibTableColumn
bgp4V2PeerOutUpdates = _Bgp4V2PeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 7, 1, 2),
    _Bgp4V2PeerOutUpdates_Type()
)
bgp4V2PeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerOutUpdates.setStatus("current")
_Bgp4V2PeerInTotalMessages_Type = Counter32
_Bgp4V2PeerInTotalMessages_Object = MibTableColumn
bgp4V2PeerInTotalMessages = _Bgp4V2PeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 7, 1, 3),
    _Bgp4V2PeerInTotalMessages_Type()
)
bgp4V2PeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerInTotalMessages.setStatus("current")
_Bgp4V2PeerOutTotalMessages_Type = Counter32
_Bgp4V2PeerOutTotalMessages_Object = MibTableColumn
bgp4V2PeerOutTotalMessages = _Bgp4V2PeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 7, 1, 4),
    _Bgp4V2PeerOutTotalMessages_Type()
)
bgp4V2PeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerOutTotalMessages.setStatus("current")
_Bgp4V2PeerFsmEstablishedTransitions_Type = Counter32
_Bgp4V2PeerFsmEstablishedTransitions_Object = MibTableColumn
bgp4V2PeerFsmEstablishedTransitions = _Bgp4V2PeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 7, 1, 5),
    _Bgp4V2PeerFsmEstablishedTransitions_Type()
)
bgp4V2PeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PeerFsmEstablishedTransitions.setStatus("current")
_Bgp4V2PrefixGaugesTable_Object = MibTable
bgp4V2PrefixGaugesTable = _Bgp4V2PrefixGaugesTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    bgp4V2PrefixGaugesTable.setStatus("current")
_Bgp4V2PrefixGaugesEntry_Object = MibTableRow
bgp4V2PrefixGaugesEntry = _Bgp4V2PrefixGaugesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 8, 1)
)
bgp4V2PrefixGaugesEntry.setIndexNames(
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInstance"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddrType"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddr"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PrefixGaugesAfi"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PrefixGaugesSafi"),
)
if mibBuilder.loadTexts:
    bgp4V2PrefixGaugesEntry.setStatus("current")
_Bgp4V2PrefixGaugesAfi_Type = Bgp4V2AddressFamilyIdentifierTC
_Bgp4V2PrefixGaugesAfi_Object = MibTableColumn
bgp4V2PrefixGaugesAfi = _Bgp4V2PrefixGaugesAfi_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 8, 1, 1),
    _Bgp4V2PrefixGaugesAfi_Type()
)
bgp4V2PrefixGaugesAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2PrefixGaugesAfi.setStatus("current")
_Bgp4V2PrefixGaugesSafi_Type = Bgp4V2SubsequentAddressFamilyIdentifierTC
_Bgp4V2PrefixGaugesSafi_Object = MibTableColumn
bgp4V2PrefixGaugesSafi = _Bgp4V2PrefixGaugesSafi_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 8, 1, 2),
    _Bgp4V2PrefixGaugesSafi_Type()
)
bgp4V2PrefixGaugesSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2PrefixGaugesSafi.setStatus("current")
_Bgp4V2PrefixInPrefixes_Type = Gauge32
_Bgp4V2PrefixInPrefixes_Object = MibTableColumn
bgp4V2PrefixInPrefixes = _Bgp4V2PrefixInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 8, 1, 3),
    _Bgp4V2PrefixInPrefixes_Type()
)
bgp4V2PrefixInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PrefixInPrefixes.setStatus("current")
_Bgp4V2PrefixInPrefixesAccepted_Type = Gauge32
_Bgp4V2PrefixInPrefixesAccepted_Object = MibTableColumn
bgp4V2PrefixInPrefixesAccepted = _Bgp4V2PrefixInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 8, 1, 4),
    _Bgp4V2PrefixInPrefixesAccepted_Type()
)
bgp4V2PrefixInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PrefixInPrefixesAccepted.setStatus("current")
_Bgp4V2PrefixOutPrefixes_Type = Gauge32
_Bgp4V2PrefixOutPrefixes_Object = MibTableColumn
bgp4V2PrefixOutPrefixes = _Bgp4V2PrefixOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 8, 1, 5),
    _Bgp4V2PrefixOutPrefixes_Type()
)
bgp4V2PrefixOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2PrefixOutPrefixes.setStatus("current")
_Bgp4V2NlriTable_Object = MibTable
bgp4V2NlriTable = _Bgp4V2NlriTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    bgp4V2NlriTable.setStatus("current")
_Bgp4V2NlriEntry_Object = MibTableRow
bgp4V2NlriEntry = _Bgp4V2NlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1)
)
bgp4V2NlriEntry.setIndexNames(
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriIndex"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInstance"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAfi"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriSafi"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriPrefixType"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriPrefix"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriPrefixLen"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddrType"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    bgp4V2NlriEntry.setStatus("current")


class _Bgp4V2NlriIndex_Type(Unsigned32):
    """Custom type bgp4V2NlriIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Bgp4V2NlriIndex_Type.__name__ = "Unsigned32"
_Bgp4V2NlriIndex_Object = MibTableColumn
bgp4V2NlriIndex = _Bgp4V2NlriIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 1),
    _Bgp4V2NlriIndex_Type()
)
bgp4V2NlriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2NlriIndex.setStatus("current")
_Bgp4V2NlriAfi_Type = Bgp4V2AddressFamilyIdentifierTC
_Bgp4V2NlriAfi_Object = MibTableColumn
bgp4V2NlriAfi = _Bgp4V2NlriAfi_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 2),
    _Bgp4V2NlriAfi_Type()
)
bgp4V2NlriAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2NlriAfi.setStatus("current")
_Bgp4V2NlriSafi_Type = Bgp4V2SubsequentAddressFamilyIdentifierTC
_Bgp4V2NlriSafi_Object = MibTableColumn
bgp4V2NlriSafi = _Bgp4V2NlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 3),
    _Bgp4V2NlriSafi_Type()
)
bgp4V2NlriSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2NlriSafi.setStatus("current")
_Bgp4V2NlriPrefixType_Type = InetAddressType
_Bgp4V2NlriPrefixType_Object = MibTableColumn
bgp4V2NlriPrefixType = _Bgp4V2NlriPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 4),
    _Bgp4V2NlriPrefixType_Type()
)
bgp4V2NlriPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2NlriPrefixType.setStatus("current")
_Bgp4V2NlriPrefix_Type = InetAddress
_Bgp4V2NlriPrefix_Object = MibTableColumn
bgp4V2NlriPrefix = _Bgp4V2NlriPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 5),
    _Bgp4V2NlriPrefix_Type()
)
bgp4V2NlriPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2NlriPrefix.setStatus("current")
_Bgp4V2NlriPrefixLen_Type = InetAddressPrefixLength
_Bgp4V2NlriPrefixLen_Object = MibTableColumn
bgp4V2NlriPrefixLen = _Bgp4V2NlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 6),
    _Bgp4V2NlriPrefixLen_Type()
)
bgp4V2NlriPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2NlriPrefixLen.setStatus("current")
_Bgp4V2NlriBest_Type = TruthValue
_Bgp4V2NlriBest_Object = MibTableColumn
bgp4V2NlriBest = _Bgp4V2NlriBest_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 7),
    _Bgp4V2NlriBest_Type()
)
bgp4V2NlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriBest.setStatus("current")
_Bgp4V2NlriCalcLocalPref_Type = Unsigned32
_Bgp4V2NlriCalcLocalPref_Object = MibTableColumn
bgp4V2NlriCalcLocalPref = _Bgp4V2NlriCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 8),
    _Bgp4V2NlriCalcLocalPref_Type()
)
bgp4V2NlriCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriCalcLocalPref.setStatus("current")


class _Bgp4V2NlriOrigin_Type(Integer32):
    """Custom type bgp4V2NlriOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_Bgp4V2NlriOrigin_Type.__name__ = "Integer32"
_Bgp4V2NlriOrigin_Object = MibTableColumn
bgp4V2NlriOrigin = _Bgp4V2NlriOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 9),
    _Bgp4V2NlriOrigin_Type()
)
bgp4V2NlriOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriOrigin.setStatus("current")
_Bgp4V2NlriNextHopAddrType_Type = InetAddressType
_Bgp4V2NlriNextHopAddrType_Object = MibTableColumn
bgp4V2NlriNextHopAddrType = _Bgp4V2NlriNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 10),
    _Bgp4V2NlriNextHopAddrType_Type()
)
bgp4V2NlriNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriNextHopAddrType.setStatus("current")


class _Bgp4V2NlriNextHopAddr_Type(InetAddress):
    """Custom type bgp4V2NlriNextHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_Bgp4V2NlriNextHopAddr_Type.__name__ = "InetAddress"
_Bgp4V2NlriNextHopAddr_Object = MibTableColumn
bgp4V2NlriNextHopAddr = _Bgp4V2NlriNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 11),
    _Bgp4V2NlriNextHopAddr_Type()
)
bgp4V2NlriNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriNextHopAddr.setStatus("current")
_Bgp4V2NlriLinkLocalNextHopAddrType_Type = InetAddressType
_Bgp4V2NlriLinkLocalNextHopAddrType_Object = MibTableColumn
bgp4V2NlriLinkLocalNextHopAddrType = _Bgp4V2NlriLinkLocalNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 12),
    _Bgp4V2NlriLinkLocalNextHopAddrType_Type()
)
bgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriLinkLocalNextHopAddrType.setStatus("current")
_Bgp4V2NlriLinkLocalNextHopAddr_Type = InetAddress
_Bgp4V2NlriLinkLocalNextHopAddr_Object = MibTableColumn
bgp4V2NlriLinkLocalNextHopAddr = _Bgp4V2NlriLinkLocalNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 13),
    _Bgp4V2NlriLinkLocalNextHopAddr_Type()
)
bgp4V2NlriLinkLocalNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriLinkLocalNextHopAddr.setStatus("current")
_Bgp4V2NlriLocalPrefPresent_Type = TruthValue
_Bgp4V2NlriLocalPrefPresent_Object = MibTableColumn
bgp4V2NlriLocalPrefPresent = _Bgp4V2NlriLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 14),
    _Bgp4V2NlriLocalPrefPresent_Type()
)
bgp4V2NlriLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriLocalPrefPresent.setStatus("current")
_Bgp4V2NlriLocalPref_Type = Unsigned32
_Bgp4V2NlriLocalPref_Object = MibTableColumn
bgp4V2NlriLocalPref = _Bgp4V2NlriLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 15),
    _Bgp4V2NlriLocalPref_Type()
)
bgp4V2NlriLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriLocalPref.setStatus("current")
_Bgp4V2NlriMedPresent_Type = TruthValue
_Bgp4V2NlriMedPresent_Object = MibTableColumn
bgp4V2NlriMedPresent = _Bgp4V2NlriMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 16),
    _Bgp4V2NlriMedPresent_Type()
)
bgp4V2NlriMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriMedPresent.setStatus("current")
_Bgp4V2NlriMed_Type = Unsigned32
_Bgp4V2NlriMed_Object = MibTableColumn
bgp4V2NlriMed = _Bgp4V2NlriMed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 17),
    _Bgp4V2NlriMed_Type()
)
bgp4V2NlriMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriMed.setStatus("current")
_Bgp4V2NlriAtomicAggregate_Type = TruthValue
_Bgp4V2NlriAtomicAggregate_Object = MibTableColumn
bgp4V2NlriAtomicAggregate = _Bgp4V2NlriAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 18),
    _Bgp4V2NlriAtomicAggregate_Type()
)
bgp4V2NlriAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriAtomicAggregate.setStatus("current")
_Bgp4V2NlriAggregatorPresent_Type = TruthValue
_Bgp4V2NlriAggregatorPresent_Object = MibTableColumn
bgp4V2NlriAggregatorPresent = _Bgp4V2NlriAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 19),
    _Bgp4V2NlriAggregatorPresent_Type()
)
bgp4V2NlriAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriAggregatorPresent.setStatus("current")
_Bgp4V2NlriAggregatorAS_Type = InetAutonomousSystemNumber
_Bgp4V2NlriAggregatorAS_Object = MibTableColumn
bgp4V2NlriAggregatorAS = _Bgp4V2NlriAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 20),
    _Bgp4V2NlriAggregatorAS_Type()
)
bgp4V2NlriAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriAggregatorAS.setStatus("current")
_Bgp4V2NlriAggregatorAddr_Type = Bgp4V2IdentifierTC
_Bgp4V2NlriAggregatorAddr_Object = MibTableColumn
bgp4V2NlriAggregatorAddr = _Bgp4V2NlriAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 21),
    _Bgp4V2NlriAggregatorAddr_Type()
)
bgp4V2NlriAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriAggregatorAddr.setStatus("current")
_Bgp4V2NlriAsPathCalcLength_Type = Unsigned32
_Bgp4V2NlriAsPathCalcLength_Object = MibTableColumn
bgp4V2NlriAsPathCalcLength = _Bgp4V2NlriAsPathCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 22),
    _Bgp4V2NlriAsPathCalcLength_Type()
)
bgp4V2NlriAsPathCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriAsPathCalcLength.setStatus("current")
_Bgp4V2NlriAsPathString_Type = SnmpAdminString
_Bgp4V2NlriAsPathString_Object = MibTableColumn
bgp4V2NlriAsPathString = _Bgp4V2NlriAsPathString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 23),
    _Bgp4V2NlriAsPathString_Type()
)
bgp4V2NlriAsPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriAsPathString.setStatus("current")


class _Bgp4V2NlriAsPath_Type(OctetString):
    """Custom type bgp4V2NlriAsPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4072),
    )


_Bgp4V2NlriAsPath_Type.__name__ = "OctetString"
_Bgp4V2NlriAsPath_Object = MibTableColumn
bgp4V2NlriAsPath = _Bgp4V2NlriAsPath_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 24),
    _Bgp4V2NlriAsPath_Type()
)
bgp4V2NlriAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriAsPath.setStatus("current")


class _Bgp4V2NlriPathAttrUnknown_Type(OctetString):
    """Custom type bgp4V2NlriPathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4072),
    )


_Bgp4V2NlriPathAttrUnknown_Type.__name__ = "OctetString"
_Bgp4V2NlriPathAttrUnknown_Object = MibTableColumn
bgp4V2NlriPathAttrUnknown = _Bgp4V2NlriPathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 9, 1, 25),
    _Bgp4V2NlriPathAttrUnknown_Type()
)
bgp4V2NlriPathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2NlriPathAttrUnknown.setStatus("current")
_Bgp4V2AdjRibsOutTable_Object = MibTable
bgp4V2AdjRibsOutTable = _Bgp4V2AdjRibsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    bgp4V2AdjRibsOutTable.setStatus("current")
_Bgp4V2AdjRibsOutEntry_Object = MibTableRow
bgp4V2AdjRibsOutEntry = _Bgp4V2AdjRibsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 10, 1)
)
bgp4V2AdjRibsOutEntry.setIndexNames(
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInstance"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAfi"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriSafi"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriPrefixType"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriPrefix"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2NlriPrefixLen"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddrType"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAddr"),
    (0, "FOUNDRY-BGP4V2-MIB", "bgp4V2AdjRibsOutIndex"),
)
if mibBuilder.loadTexts:
    bgp4V2AdjRibsOutEntry.setStatus("current")


class _Bgp4V2AdjRibsOutIndex_Type(Unsigned32):
    """Custom type bgp4V2AdjRibsOutIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Bgp4V2AdjRibsOutIndex_Type.__name__ = "Unsigned32"
_Bgp4V2AdjRibsOutIndex_Object = MibTableColumn
bgp4V2AdjRibsOutIndex = _Bgp4V2AdjRibsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 10, 1, 1),
    _Bgp4V2AdjRibsOutIndex_Type()
)
bgp4V2AdjRibsOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgp4V2AdjRibsOutIndex.setStatus("current")
_Bgp4V2AdjRibsOutRoute_Type = RowPointer
_Bgp4V2AdjRibsOutRoute_Object = MibTableColumn
bgp4V2AdjRibsOutRoute = _Bgp4V2AdjRibsOutRoute_Object(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 1, 10, 1, 2),
    _Bgp4V2AdjRibsOutRoute_Type()
)
bgp4V2AdjRibsOutRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgp4V2AdjRibsOutRoute.setStatus("current")
_Bgp4V2Conformance_ObjectIdentity = ObjectIdentity
bgp4V2Conformance = _Bgp4V2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2)
)
_Bgp4V2Compliances_ObjectIdentity = ObjectIdentity
bgp4V2Compliances = _Bgp4V2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 1)
)
_Bgp4V2Groups_ObjectIdentity = ObjectIdentity
bgp4V2Groups = _Bgp4V2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2)
)
bgp4V2PeerEntry.registerAugmentions(
    ("FOUNDRY-BGP4V2-MIB",
     "bgp4V2PeerErrorsEntry")
)
bgp4V2PeerErrorsEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions(
    ("FOUNDRY-BGP4V2-MIB",
     "bgp4V2PeerEventTimesEntry")
)
bgp4V2PeerEventTimesEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions(
    ("FOUNDRY-BGP4V2-MIB",
     "bgp4V2PeerConfiguredTimersEntry")
)
bgp4V2PeerConfiguredTimersEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions(
    ("FOUNDRY-BGP4V2-MIB",
     "bgp4V2PeerNegotiatedTimersEntry")
)
bgp4V2PeerNegotiatedTimersEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions(
    ("FOUNDRY-BGP4V2-MIB",
     "bgp4V2PeerCountersEntry")
)
bgp4V2PeerCountersEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())

# Managed Objects groups

bgp4V2GlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2, 1)
)
bgp4V2GlobalsGroup.setObjects(
    ("FOUNDRY-BGP4V2-MIB", "bgp4V2DiscontinuityTime")
)
if mibBuilder.loadTexts:
    bgp4V2GlobalsGroup.setStatus("current")

bgp4V2StdMIBTimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2, 2)
)
bgp4V2StdMIBTimersGroup.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerFsmEstablishedTime"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInUpdatesElapsedTime"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerConnectRetryInterval"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerHoldTimeConfigured"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerKeepAliveConfigured"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerMinASOrigInterval"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerMinRouteAdverInterval"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerHoldTime"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerKeepAlive"))
)
if mibBuilder.loadTexts:
    bgp4V2StdMIBTimersGroup.setStatus("current")

bgp4V2StdMIBCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2, 3)
)
bgp4V2StdMIBCountersGroup.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInUpdates"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerOutUpdates"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerInTotalMessages"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerOutTotalMessages"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerFsmEstablishedTransitions"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PrefixInPrefixes"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PrefixInPrefixesAccepted"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PrefixOutPrefixes"))
)
if mibBuilder.loadTexts:
    bgp4V2StdMIBCountersGroup.setStatus("current")

bgp4V2StdMIBErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2, 5)
)
bgp4V2StdMIBErrorsGroup.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorCodeReceived"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorSubCodeReceived"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorReceivedData"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorReceivedTime"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorReceivedText"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorCodeSent"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorSubCodeSent"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorSentData"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorSentTime"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorSentText"))
)
if mibBuilder.loadTexts:
    bgp4V2StdMIBErrorsGroup.setStatus("current")

bgp4V2StdMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2, 6)
)
bgp4V2StdMIBPeerGroup.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerState"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerAdminStatus"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalAddrType"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalAddr"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalPort"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalAs"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemotePort"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteAs"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalIdentifier"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemoteIdentifier"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerDescription"))
)
if mibBuilder.loadTexts:
    bgp4V2StdMIBPeerGroup.setStatus("current")

bgp4V2StdMIBNlriGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2, 7)
)
bgp4V2StdMIBNlriGroup.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAsPathCalcLength"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAsPathString"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriBest"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriCalcLocalPref"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2AdjRibsOutRoute"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAggregatorPresent"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAggregatorAS"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAggregatorAddr"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAtomicAggregate"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriLocalPref"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriLocalPrefPresent"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriMed"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriMedPresent"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriNextHopAddr"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriNextHopAddrType"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriLinkLocalNextHopAddrType"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriLinkLocalNextHopAddr"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriOrigin"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriAsPath"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2NlriPathAttrUnknown"))
)
if mibBuilder.loadTexts:
    bgp4V2StdMIBNlriGroup.setStatus("current")


# Notification objects

bgp4V2EstablishedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 0, 1)
)
bgp4V2EstablishedNotification.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerState"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalPort"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemotePort"))
)
if mibBuilder.loadTexts:
    bgp4V2EstablishedNotification.setStatus(
        "current"
    )

bgp4V2BackwardTransitionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 0, 2)
)
bgp4V2BackwardTransitionNotification.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerState"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLocalPort"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerRemotePort"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorCodeReceived"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorSubCodeReceived"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2PeerLastErrorReceivedText"))
)
if mibBuilder.loadTexts:
    bgp4V2BackwardTransitionNotification.setStatus(
        "current"
    )


# Notifications groups

bgp4V2StdMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 2, 8)
)
bgp4V2StdMIBNotificationGroup.setObjects(
      *(("FOUNDRY-BGP4V2-MIB", "bgp4V2EstablishedNotification"),
        ("FOUNDRY-BGP4V2-MIB", "bgp4V2BackwardTransitionNotification"))
)
if mibBuilder.loadTexts:
    bgp4V2StdMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bgp4V2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 3, 5, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    bgp4V2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-BGP4V2-MIB",
    **{"bgp4V2": bgp4V2,
       "bgp4V2Notifications": bgp4V2Notifications,
       "bgp4V2EstablishedNotification": bgp4V2EstablishedNotification,
       "bgp4V2BackwardTransitionNotification": bgp4V2BackwardTransitionNotification,
       "bgp4V2Objects": bgp4V2Objects,
       "bgp4V2DiscontinuityTable": bgp4V2DiscontinuityTable,
       "bgp4V2DiscontinuityEntry": bgp4V2DiscontinuityEntry,
       "bgp4V2DiscontinuityTime": bgp4V2DiscontinuityTime,
       "bgp4V2PeerTable": bgp4V2PeerTable,
       "bgp4V2PeerEntry": bgp4V2PeerEntry,
       "bgp4V2PeerInstance": bgp4V2PeerInstance,
       "bgp4V2PeerLocalAddrType": bgp4V2PeerLocalAddrType,
       "bgp4V2PeerLocalAddr": bgp4V2PeerLocalAddr,
       "bgp4V2PeerRemoteAddrType": bgp4V2PeerRemoteAddrType,
       "bgp4V2PeerRemoteAddr": bgp4V2PeerRemoteAddr,
       "bgp4V2PeerLocalPort": bgp4V2PeerLocalPort,
       "bgp4V2PeerLocalAs": bgp4V2PeerLocalAs,
       "bgp4V2PeerLocalIdentifier": bgp4V2PeerLocalIdentifier,
       "bgp4V2PeerRemotePort": bgp4V2PeerRemotePort,
       "bgp4V2PeerRemoteAs": bgp4V2PeerRemoteAs,
       "bgp4V2PeerRemoteIdentifier": bgp4V2PeerRemoteIdentifier,
       "bgp4V2PeerAdminStatus": bgp4V2PeerAdminStatus,
       "bgp4V2PeerState": bgp4V2PeerState,
       "bgp4V2PeerDescription": bgp4V2PeerDescription,
       "bgp4V2PeerErrorsTable": bgp4V2PeerErrorsTable,
       "bgp4V2PeerErrorsEntry": bgp4V2PeerErrorsEntry,
       "bgp4V2PeerLastErrorCodeReceived": bgp4V2PeerLastErrorCodeReceived,
       "bgp4V2PeerLastErrorSubCodeReceived": bgp4V2PeerLastErrorSubCodeReceived,
       "bgp4V2PeerLastErrorReceivedTime": bgp4V2PeerLastErrorReceivedTime,
       "bgp4V2PeerLastErrorReceivedText": bgp4V2PeerLastErrorReceivedText,
       "bgp4V2PeerLastErrorReceivedData": bgp4V2PeerLastErrorReceivedData,
       "bgp4V2PeerLastErrorCodeSent": bgp4V2PeerLastErrorCodeSent,
       "bgp4V2PeerLastErrorSubCodeSent": bgp4V2PeerLastErrorSubCodeSent,
       "bgp4V2PeerLastErrorSentTime": bgp4V2PeerLastErrorSentTime,
       "bgp4V2PeerLastErrorSentText": bgp4V2PeerLastErrorSentText,
       "bgp4V2PeerLastErrorSentData": bgp4V2PeerLastErrorSentData,
       "bgp4V2PeerEventTimesTable": bgp4V2PeerEventTimesTable,
       "bgp4V2PeerEventTimesEntry": bgp4V2PeerEventTimesEntry,
       "bgp4V2PeerFsmEstablishedTime": bgp4V2PeerFsmEstablishedTime,
       "bgp4V2PeerInUpdatesElapsedTime": bgp4V2PeerInUpdatesElapsedTime,
       "bgp4V2PeerConfiguredTimersTable": bgp4V2PeerConfiguredTimersTable,
       "bgp4V2PeerConfiguredTimersEntry": bgp4V2PeerConfiguredTimersEntry,
       "bgp4V2PeerConnectRetryInterval": bgp4V2PeerConnectRetryInterval,
       "bgp4V2PeerHoldTimeConfigured": bgp4V2PeerHoldTimeConfigured,
       "bgp4V2PeerKeepAliveConfigured": bgp4V2PeerKeepAliveConfigured,
       "bgp4V2PeerMinASOrigInterval": bgp4V2PeerMinASOrigInterval,
       "bgp4V2PeerMinRouteAdverInterval": bgp4V2PeerMinRouteAdverInterval,
       "bgp4V2PeerNegotiatedTimersTable": bgp4V2PeerNegotiatedTimersTable,
       "bgp4V2PeerNegotiatedTimersEntry": bgp4V2PeerNegotiatedTimersEntry,
       "bgp4V2PeerHoldTime": bgp4V2PeerHoldTime,
       "bgp4V2PeerKeepAlive": bgp4V2PeerKeepAlive,
       "bgp4V2PeerCountersTable": bgp4V2PeerCountersTable,
       "bgp4V2PeerCountersEntry": bgp4V2PeerCountersEntry,
       "bgp4V2PeerInUpdates": bgp4V2PeerInUpdates,
       "bgp4V2PeerOutUpdates": bgp4V2PeerOutUpdates,
       "bgp4V2PeerInTotalMessages": bgp4V2PeerInTotalMessages,
       "bgp4V2PeerOutTotalMessages": bgp4V2PeerOutTotalMessages,
       "bgp4V2PeerFsmEstablishedTransitions": bgp4V2PeerFsmEstablishedTransitions,
       "bgp4V2PrefixGaugesTable": bgp4V2PrefixGaugesTable,
       "bgp4V2PrefixGaugesEntry": bgp4V2PrefixGaugesEntry,
       "bgp4V2PrefixGaugesAfi": bgp4V2PrefixGaugesAfi,
       "bgp4V2PrefixGaugesSafi": bgp4V2PrefixGaugesSafi,
       "bgp4V2PrefixInPrefixes": bgp4V2PrefixInPrefixes,
       "bgp4V2PrefixInPrefixesAccepted": bgp4V2PrefixInPrefixesAccepted,
       "bgp4V2PrefixOutPrefixes": bgp4V2PrefixOutPrefixes,
       "bgp4V2NlriTable": bgp4V2NlriTable,
       "bgp4V2NlriEntry": bgp4V2NlriEntry,
       "bgp4V2NlriIndex": bgp4V2NlriIndex,
       "bgp4V2NlriAfi": bgp4V2NlriAfi,
       "bgp4V2NlriSafi": bgp4V2NlriSafi,
       "bgp4V2NlriPrefixType": bgp4V2NlriPrefixType,
       "bgp4V2NlriPrefix": bgp4V2NlriPrefix,
       "bgp4V2NlriPrefixLen": bgp4V2NlriPrefixLen,
       "bgp4V2NlriBest": bgp4V2NlriBest,
       "bgp4V2NlriCalcLocalPref": bgp4V2NlriCalcLocalPref,
       "bgp4V2NlriOrigin": bgp4V2NlriOrigin,
       "bgp4V2NlriNextHopAddrType": bgp4V2NlriNextHopAddrType,
       "bgp4V2NlriNextHopAddr": bgp4V2NlriNextHopAddr,
       "bgp4V2NlriLinkLocalNextHopAddrType": bgp4V2NlriLinkLocalNextHopAddrType,
       "bgp4V2NlriLinkLocalNextHopAddr": bgp4V2NlriLinkLocalNextHopAddr,
       "bgp4V2NlriLocalPrefPresent": bgp4V2NlriLocalPrefPresent,
       "bgp4V2NlriLocalPref": bgp4V2NlriLocalPref,
       "bgp4V2NlriMedPresent": bgp4V2NlriMedPresent,
       "bgp4V2NlriMed": bgp4V2NlriMed,
       "bgp4V2NlriAtomicAggregate": bgp4V2NlriAtomicAggregate,
       "bgp4V2NlriAggregatorPresent": bgp4V2NlriAggregatorPresent,
       "bgp4V2NlriAggregatorAS": bgp4V2NlriAggregatorAS,
       "bgp4V2NlriAggregatorAddr": bgp4V2NlriAggregatorAddr,
       "bgp4V2NlriAsPathCalcLength": bgp4V2NlriAsPathCalcLength,
       "bgp4V2NlriAsPathString": bgp4V2NlriAsPathString,
       "bgp4V2NlriAsPath": bgp4V2NlriAsPath,
       "bgp4V2NlriPathAttrUnknown": bgp4V2NlriPathAttrUnknown,
       "bgp4V2AdjRibsOutTable": bgp4V2AdjRibsOutTable,
       "bgp4V2AdjRibsOutEntry": bgp4V2AdjRibsOutEntry,
       "bgp4V2AdjRibsOutIndex": bgp4V2AdjRibsOutIndex,
       "bgp4V2AdjRibsOutRoute": bgp4V2AdjRibsOutRoute,
       "bgp4V2Conformance": bgp4V2Conformance,
       "bgp4V2Compliances": bgp4V2Compliances,
       "bgp4V2Compliance": bgp4V2Compliance,
       "bgp4V2Groups": bgp4V2Groups,
       "bgp4V2GlobalsGroup": bgp4V2GlobalsGroup,
       "bgp4V2StdMIBTimersGroup": bgp4V2StdMIBTimersGroup,
       "bgp4V2StdMIBCountersGroup": bgp4V2StdMIBCountersGroup,
       "bgp4V2StdMIBErrorsGroup": bgp4V2StdMIBErrorsGroup,
       "bgp4V2StdMIBPeerGroup": bgp4V2StdMIBPeerGroup,
       "bgp4V2StdMIBNlriGroup": bgp4V2StdMIBNlriGroup,
       "bgp4V2StdMIBNotificationGroup": bgp4V2StdMIBNotificationGroup}
)
